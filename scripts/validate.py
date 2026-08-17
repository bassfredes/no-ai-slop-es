#!/usr/bin/env python3
"""Lightweight local validation for no-ia-slop-es.

This complements, not replaces, `skills-ref validate` from the Agent Skills
reference implementation.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    try:
        block = text.split("---\n", 2)[1]
    except IndexError:
        fail("SKILL.md frontmatter is not closed")
    values: dict[str, str] = {}
    current = None
    for line in block.splitlines():
        if re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*:\s*", line):
            key, value = line.split(":", 1)
            current = key
            clean = value.strip().strip('\"')
            values[key] = '' if clean in {'>', '|'} else clean
        elif current == "description" and line.startswith("  "):
            values[current] = (values[current] + " " + line.strip()).strip()
    return values


def main() -> int:
    text = SKILL.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    name = fm.get("name", "")
    description = fm.get("description", "")

    if name != ROOT.name:
        fail(f"frontmatter name {name!r} must match directory {ROOT.name!r}")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail("name must contain lowercase letters, numbers, and single hyphens only")
    if not (1 <= len(name) <= 64):
        fail("name must be 1-64 characters")
    if not description:
        fail("description must be non-empty")
    if len(description) > 1024:
        fail(f"description is {len(description)} characters; max is 1024")
    if len(text.splitlines()) > 500:
        fail("SKILL.md exceeds the recommended 500-line limit")

    for rel in ["eval.md", "references/patrones-es.md", "references/calibracion-editorial.md"]:
        if not (ROOT / rel).is_file():
            fail(f"missing referenced file: {rel}")

    for rel in ["evals/evals.json", "evals/trigger-evals.json", "evals/calibration-corpus.json"]:
        try:
            json.loads((ROOT / rel).read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"invalid JSON in {rel}: {exc}")

    print(f"PASS name={name} description_chars={len(description)} skill_lines={len(text.splitlines())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
