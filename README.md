# no-ia-slop-es

Skill de Agent Skills para redactar, editar y auditar texto en español reduciendo IA slop sin tratar el estilo como prueba de autoría.

## Estructura

```text
no-ia-slop-es/
├── SKILL.md
├── eval.md
├── references/
│   └── patrones-es.md
└── evals/
    ├── evals.json
    └── trigger-evals.json
```

## Instalación

Coloca la carpeta completa en el directorio de skills que utilice tu agente. El formato sigue la especificación abierta de Agent Skills.

Ejemplos de ubicaciones dependen del cliente. En entornos compatibles con `.agents/skills/`, la ruta puede ser:

```text
.agents/skills/no-ia-slop-es/
```

## Filosofía

La skill no intenta crear una blacklist de “palabras de ChatGPT”. Prioriza:

1. fidelidad al contenido;
2. densidad informativa;
3. coherencia;
4. registro y voz;
5. naturalidad idiomática;
6. edición mínima.

También separa tres trabajos: redactar, editar y auditar. En auditoría no atribuye autoría ni asigna porcentajes de IA.

## Evaluación

`eval.md` es el quality gate interno para una ejecución.

`evals/evals.json` contiene casos de regresión de calidad para comparar:
- con skill vs. sin skill;
- versión actual vs. versión anterior.

Los evals cubren además falsos positivos editoriales: formalidad técnica legítima, español regional y borradores que ya tienen una voz clara.

`evals/trigger-evals.json` separa casos que deberían activar la skill de near-misses que no deberían activarla.
