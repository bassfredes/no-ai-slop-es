# Rúbrica de evaluación

Usa esta rúbrica para comparar salidas **a ciegas**. No reveles al juez cuál salida usó la skill.

Puntúa cada dimensión de 0 a 4. Usa evidencia textual; no premies cambios por el mero hecho de existir.

## 1. Fidelidad — peso 25 %

- **4:** conserva mensaje, hechos, certeza, posición y terminología relevante.
- **3:** cambio menor sin efecto material.
- **2:** introduce una interpretación no necesaria o pierde un detalle útil.
- **1:** altera parte sustantiva del contenido.
- **0:** inventa o contradice información.

## 2. Densidad y especificidad — peso 20 %

- **4:** elimina relleno/repetición y protege hechos o mecanismos concretos.
- **3:** mejora clara con residual menor.
- **2:** mezcla mejoras con abstracciones nuevas.
- **1:** conserva la mayor parte del slop o lo reemplaza por otro.
- **0:** empeora densidad o inventa especificidad.

## 3. Voz y registro — peso 20 %

- **4:** la salida podría haber sido escrita por el mismo autor en ese canal.
- **3:** pequeña homogeneización sin pérdida relevante.
- **2:** neutraliza rasgos reconocibles o cambia formalidad.
- **1:** impone una voz genérica/corporativa.
- **0:** contradice explícitamente la variedad o el registro pedido.

## 4. Precisión lingüística y terminológica — peso 15 %

- **4:** español idiomático y terminología estable.
- **3:** detalle menor mejorable.
- **2:** alguna colocación o sustitución dudosa.
- **1:** calcos, synonym cycling o tecnicismos degradados.
- **0:** cambia significado técnico.

## 5. Proporcionalidad de la edición — peso 15 %

- **4:** mínima intervención eficaz; deja intacto lo que ya funciona.
- **3:** algo más de edición de la necesaria, sin daño relevante.
- **2:** reescritura visible que aporta poco.
- **1:** sobre-edición clara.
- **0:** transforma por completo un texto que no lo necesitaba.

## 6. Integridad — peso 5 %

- **4:** no inventa datos ni optimiza contra detectores.
- **2:** lenguaje ambiguo sobre procedencia o detección.
- **0:** añade datos ficticios, errores deliberados o técnicas de evasión.

## Reglas de comparación

1. Evalúa primero las assertions del caso.
2. Después aplica esta rúbrica.
3. Si una salida obtiene mejor estilo pero peor fidelidad, la fidelidad prevalece.
4. Un texto sin cambios puede ganar si el original ya era bueno.
5. No uses “suena más humano” como criterio.
6. En empate, prefiere la salida más corta solo si no perdió contenido ni voz.

## Resultado

Registra:

```json
{
  "winner": "A | B | tie",
  "scores": {
    "A": {"fidelity": 0, "density": 0, "voice": 0, "language": 0, "proportionality": 0, "integrity": 0},
    "B": {"fidelity": 0, "density": 0, "voice": 0, "language": 0, "proportionality": 0, "integrity": 0}
  },
  "evidence": ["..."],
  "notes": "..."
}
```
