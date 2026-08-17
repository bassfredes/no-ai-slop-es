#!/usr/bin/env python3
"""Run no-ia-slop-es eval prompts through Codex CLI or Claude Code.

Each execution uses a fresh temporary Git repository. With-skill runs install only
runtime skill files in the agent-specific project directory; eval fixtures and
rubrics stay outside the workspace to avoid benchmark leakage.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

SKILL_NAME = "no-ia-slop-es"
ROOT = Path(__file__).resolve().parents[1]
EVALS_FILE = ROOT / "evals" / "evals.json"
RUNTIME_FILES = ["SKILL.md", "eval.md"]
RUNTIME_DIRS = ["references"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", choices=["codex", "claude"], required=True)
    parser.add_argument("--mode", choices=["with-skill", "without-skill", "both"], default="both")
    parser.add_argument("--activation", choices=["explicit", "implicit"], default="explicit")
    parser.add_argument("--model", help="Optional model override passed to the selected CLI")
    parser.add_argument("--iteration", default="iteration-1")
    parser.add_argument("--output-root", type=Path, default=ROOT.parent / f"{SKILL_NAME}-workspace")
    parser.add_argument("--eval-id", action="append", dest="eval_ids", help="Run only this eval id; repeatable")
    parser.add_argument("--repeat", type=int, default=1)
    return parser.parse_args()


def load_evals() -> list[dict]:
    data = json.loads(EVALS_FILE.read_text(encoding="utf-8"))
    return data["evals"]


def ensure_binary(binary: str) -> None:
    if shutil.which(binary) is None:
        raise SystemExit(f"Missing CLI: {binary}. Install and authenticate it before running evals.")


def ensure_cli(agent: str) -> None:
    ensure_binary("git")
    ensure_binary("codex" if agent == "codex" else "claude")


def init_workspace(workspace: Path) -> None:
    proc = subprocess.run(
        ["git", "init", "-q", "-b", "main"],
        cwd=workspace,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        # Older Git versions may not support `git init -b`.
        proc = subprocess.run(["git", "init", "-q"], cwd=workspace, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(f"Could not initialize temporary Git repo: {proc.stderr.strip()}")


def install_runtime_skill(workspace: Path, agent: str) -> None:
    if agent == "codex":
        target = workspace / ".agents" / "skills" / SKILL_NAME
    else:
        target = workspace / ".claude" / "skills" / SKILL_NAME
    target.mkdir(parents=True, exist_ok=True)

    for filename in RUNTIME_FILES:
        shutil.copy2(ROOT / filename, target / filename)
    for dirname in RUNTIME_DIRS:
        shutil.copytree(ROOT / dirname, target / dirname, dirs_exist_ok=True)


def build_prompt(agent: str, prompt: str, with_skill: bool, activation: str) -> str:
    if not with_skill or activation == "implicit":
        return prompt
    if agent == "codex":
        return f"${SKILL_NAME}\n\n{prompt}"
    return f"/{SKILL_NAME}\n\n{prompt}"


def run_codex(workspace: Path, prompt: str, model: str | None) -> tuple[int, str, str, str]:
    last_message = workspace / ".eval-last-message.txt"
    cmd = [
        "codex",
        "exec",
        "--sandbox",
        "read-only",
        "--json",
        "--output-last-message",
        str(last_message),
    ]
    if model:
        cmd.extend(["--model", model])
    cmd.append(prompt)
    proc = subprocess.run(cmd, cwd=workspace, text=True, capture_output=True)
    final = last_message.read_text(encoding="utf-8") if last_message.exists() else ""
    return proc.returncode, final, proc.stdout, proc.stderr


def extract_claude_result(raw: str) -> str:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return raw.strip()
    if isinstance(data, dict):
        for key in ("result", "response", "content"):
            value = data.get(key)
            if isinstance(value, str):
                return value
    return raw.strip()


def run_claude(workspace: Path, prompt: str, model: str | None) -> tuple[int, str, str, str]:
    cmd = ["claude", "-p", prompt, "--output-format", "json", "--max-turns", "1"]
    if model:
        cmd.extend(["--model", model])
    proc = subprocess.run(cmd, cwd=workspace, text=True, capture_output=True)
    return proc.returncode, extract_claude_result(proc.stdout), proc.stdout, proc.stderr


def walk_dicts(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_dicts(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_dicts(child)


def usage_from_codex_jsonl(raw: str) -> dict:
    usage: dict = {}
    for line in raw.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        for node in walk_dicts(event):
            candidate = node.get("usage")
            if isinstance(candidate, dict):
                usage.update(candidate)
    return usage


def usage_from_claude_json(raw: str) -> dict:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return {}
    if not isinstance(data, dict):
        return {}
    usage = data.get("usage")
    return usage if isinstance(usage, dict) else {}


def run_one(
    agent: str,
    eval_case: dict,
    with_skill: bool,
    activation: str,
    model: str | None,
    destination: Path,
    repeat_index: int,
) -> None:
    run_dir = destination / (f"run-{repeat_index}" if repeat_index > 1 else "")
    run_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix=f"{SKILL_NAME}-eval-") as tmp:
        workspace = Path(tmp)
        init_workspace(workspace)
        if with_skill:
            install_runtime_skill(workspace, agent)
        prompt = build_prompt(agent, eval_case["prompt"], with_skill, activation)

        started = time.perf_counter()
        if agent == "codex":
            code, final, raw, stderr = run_codex(workspace, prompt, model)
            usage = usage_from_codex_jsonl(raw)
            raw_name = "events.jsonl"
        else:
            code, final, raw, stderr = run_claude(workspace, prompt, model)
            usage = usage_from_claude_json(raw)
            raw_name = "raw.json"
        duration_ms = round((time.perf_counter() - started) * 1000)

    (run_dir / "output.txt").write_text(final, encoding="utf-8")
    (run_dir / raw_name).write_text(raw, encoding="utf-8")
    (run_dir / "stderr.txt").write_text(stderr, encoding="utf-8")
    (run_dir / "timing.json").write_text(
        json.dumps({"duration_ms": duration_ms, "usage": usage}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (run_dir / "run.json").write_text(
        json.dumps(
            {
                "eval_id": eval_case["id"],
                "agent": agent,
                "model": model,
                "configuration": "with_skill" if with_skill else "without_skill",
                "activation": activation if with_skill else None,
                "exit_code": code,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    if code != 0:
        print(f"FAIL {eval_case['id']} ({destination.name}) exit={code}", file=sys.stderr)
    else:
        print(f"OK   {eval_case['id']} ({destination.name})")


def main() -> int:
    args = parse_args()
    ensure_cli(args.agent)
    if args.repeat < 1:
        raise SystemExit("--repeat must be >= 1")

    evals = load_evals()
    if args.eval_ids:
        wanted = set(args.eval_ids)
        evals = [case for case in evals if case["id"] in wanted]
        missing = wanted - {case["id"] for case in evals}
        if missing:
            raise SystemExit(f"Unknown eval id(s): {', '.join(sorted(missing))}")

    configs = [True, False] if args.mode == "both" else [args.mode == "with-skill"]
    for case in evals:
        for with_skill in configs:
            label = "with_skill" if with_skill else "without_skill"
            dest = args.output_root / args.iteration / case["id"] / args.agent / label
            for idx in range(1, args.repeat + 1):
                run_one(args.agent, case, with_skill, args.activation, args.model, dest, idx if args.repeat > 1 else 1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
