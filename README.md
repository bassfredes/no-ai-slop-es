# no-ia-slop-es

Skill de Agent Skills para redactar, editar y auditar texto en español reduciendo IA slop sin tratar el estilo como prueba de autoría.

La skill prioriza fidelidad, densidad informativa, coherencia, voz y registro. No usa una blacklist de “palabras de ChatGPT”: evalúa patrones en contexto y evita sobreeditar texto técnico, académico o regional que ya cumple su función.

## Estructura

```text
no-ia-slop-es/
├── SKILL.md
├── eval.md
├── references/
│   ├── patrones-es.md
│   └── calibracion-editorial.md
├── evals/
│   ├── README.md
│   ├── evals.json
│   ├── trigger-evals.json
│   ├── calibration-corpus.json
│   └── rubric.md
└── scripts/
    ├── run_evals.py
    └── validate.py
```

`SKILL.md` contiene las instrucciones de runtime. `references/` mantiene el detalle lingüístico y la calibración editorial fuera del contexto inicial. `evals/` y `scripts/` son infraestructura de desarrollo y no deben copiarse al runtime durante una evaluación.

## Instalación

Para Codex, instala la carpeta en el nivel de proyecto:

```text
.agents/skills/no-ia-slop-es/
```

Para Claude Code:

```text
.claude/skills/no-ia-slop-es/
```

Copia al menos `SKILL.md`, `eval.md` y `references/`.

## Filosofía editorial

La regla central es simple: una idea importante se explica completamente una vez; después se usa o se referencia, no se vuelve a presentar con sinónimos. La skill prefiere estructura sobre synonym cycling, términos técnicos estables sobre variación ornamental y datos/mecanismos sobre adjetivos de importancia.

La calibración por defecto es directa y profesional, pero la voz real del autor siempre tiene prioridad. Español chileno, oralidad, formalidad académica o terminología de producto/ingeniería no son slop por sí mismos.

La skill separa tres trabajos: redactar, editar y auditar. En auditoría no atribuye autoría ni asigna porcentajes de IA. Tampoco introduce faltas, “burstiness” ni otras manipulaciones para reducir scores de detectores.

## Validación local

El validador ligero comprueba frontmatter, nombre, longitud, referencias y JSON:

```bash
python scripts/validate.py
```

Cuando esté disponible la implementación oficial de referencia, úsala además para validar el formato de Agent Skills:

```bash
skills-ref validate .
```

## Evals

`eval.md` es el quality gate interno de cada ejecución. `evals/evals.json` contiene regresiones funcionales; `trigger-evals.json` separa activaciones positivas de near-misses; `calibration-corpus.json` conserva casos de voz y sobreedición; `rubric.md` define comparación ciega por pares.

El runner ejecuta cada caso en un repositorio temporal limpio y mantiene los fixtures fuera del workspace del agente. Por defecto compara con skill y sin skill:

```bash
python scripts/run_evals.py --agent codex --iteration v1.1
python scripts/run_evals.py --agent claude --iteration v1.1
```

También permite limitar casos, fijar modelo, repetir ejecuciones y probar activación implícita:

```bash
python scripts/run_evals.py --agent codex --eval-id legitimate-formality --repeat 3
python scripts/run_evals.py --agent claude --activation implicit --mode with-skill
```

Los resultados quedan fuera del repositorio, en `../no-ia-slop-es-workspace/`, para no contaminar el paquete ni los siguientes runs.

## Desarrollo

Al cambiar una regla editorial:

1. agrega o ajusta primero un caso que reproduzca el fallo;
2. ejecuta baseline sin skill y versión actual con skill en contexto limpio;
3. verifica assertions antes de aplicar la rúbrica holística;
4. revisa especialmente falsos positivos y sobreedición;
5. conserva el cambio solo si mejora el comportamiento sin degradar fidelidad o voz.
