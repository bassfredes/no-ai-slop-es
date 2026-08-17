# Evals

La evaluación separa tres preguntas:

1. **Trigger:** ¿la descripción activa la skill donde corresponde y evita near-misses?
2. **Output quality:** ¿la skill mejora la salida frente a no usarla o frente a la versión anterior?
3. **Over-editing:** ¿deja intacto un texto que ya funciona?

## Protocolo

Cada caso debe ejecutarse en contexto limpio. Para calidad, ejecuta el mismo prompt con y sin skill. No agregues instrucciones editoriales adicionales al baseline.

Guarda cada iteración fuera del directorio de la skill:

```text
no-ia-slop-es-workspace/
└── iteration-1/
    └── <eval-id>/
        ├── codex/
        │   ├── with_skill/
        │   └── without_skill/
        └── claude/
            ├── with_skill/
            └── without_skill/
```

`scripts/run_evals.py` crea esta estructura y ejecuta Codex CLI o Claude Code si están instalados y autenticados.

## Comparación entre versiones

Para evitar que “sin skill” sea un baseline demasiado fácil, conserva el commit o tag de la versión anterior. En iteraciones posteriores compara:

- versión nueva vs. versión anterior;
- versión nueva vs. sin skill, en una muestra menor;
- Codex vs. Claude para detectar instrucciones dependientes del agente.

## Grading

Primero evalúa las `assertions` de `evals.json`. Después realiza comparación ciega con `rubric.md`.

No conviertas la rúbrica en una blacklist. Una expresión como `en este sentido` solo es un fallo si el caso y la función textual lo justifican.

## Corpus de calibración

`calibration-corpus.json` conserva ejemplos representativos del criterio editorial. Sirve para diseñar evals y revisar regresiones, no para cargar todos los ejemplos en cada ejecución.
