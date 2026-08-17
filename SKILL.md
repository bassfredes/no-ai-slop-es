---
name: no-ia-slop-es
description: >
  Reduce IA slop al redactar, editar o auditar texto en español: relleno,
  repetición, baja densidad informativa, formulismo, abstracción, tono genérico,
  conectores mecánicos, simetría artificial y calcos. Úsala cuando el usuario
  pida naturalizar un texto, quitar tono de IA, hacerlo más directo o propio,
  preservar su voz, evitar prosa corporativa/genérica o auditar estos patrones.
  No la uses como detector de autoría ni para optimizar contra detectores de IA.
compatibility: >
  Diseñada para agentes compatibles con Agent Skills, incluidos OpenAI Codex y Claude Code.
metadata:
  author: "bassfredes"
  version: "1.1.0"
  language: "es"
  scope: "writing-editing-audit"
---

# No IA slop — español

Edita como un editor de español, no como un “humanizador”. Aumenta precisión, densidad y naturalidad sin inventar contenido ni imponer una voz única.

La meta es que el texto diga algo concreto, con el registro que corresponde y con la voz de quien lo firma. No intentes demostrar que el texto es humano ni modificarlo para bajar un score de detección.

## Elige un modo

Determina el modo por la petición del usuario y no los mezcles sin necesidad:

1. **Editar** — existe un borrador y el usuario pide mejorarlo, naturalizarlo, quitar relleno o reducir tono de IA.
2. **Redactar** — pide crear un texto nuevo y quiere evitar prosa genérica, corporativa o formulaica.
3. **Auditar** — pide localizar y explicar problemas sin reescribir.

Si el usuario solo pide ortografía, traducción, resumen u otra transformación que no implique estos criterios editoriales, no amplíes el trabajo a una auditoría de slop.

## Antes de escribir

Identifica internamente:

- qué debe conseguir el texto;
- quién lo leerá y en qué canal, si se sabe;
- variedad regional presente o solicitada;
- tesis, decisión o mensaje central;
- 3–5 señales de voz que conviene preservar: vocabulario, cadencia, nivel de formalidad, brusquedad, humor, dudas, tecnicismos, oralidad o nivel de pulido.

Si el borrador ya tiene una voz clara, esa voz manda sobre cualquier preferencia por defecto de esta skill.

No neutralices automáticamente chilenismos, rioplatensismos, mexicanismos, peninsularismos u otros rasgos regionales. No inventes datos concretos para volver el texto “más humano”.

## Orden de prioridad

Resuelve problemas en este orden:

1. **Fidelidad y factualidad.** No cambies el sentido, certeza, posición ni hechos disponibles.
2. **Densidad informativa.** Elimina reformulaciones y frases que ocupan espacio sin aportar información o función.
3. **Coherencia.** Haz que cada idea aparezca donde cumple una función; no vuelvas a presentarla después como si fuera nueva.
4. **Voz y registro.** Conserva el idioma real del autor y adecua la formalidad al género.
5. **Microestilo.** Solo después corrige conectores, ritmo, nominalizaciones, adjetivos o sintaxis.

No sacrifiques una prioridad superior para mejorar una inferior.

## Principios

### Preserva antes de pulir

Deja intactas las frases que ya son claras, específicas y propias del autor. No uniformes el texto por estética.

Una voz válida puede contener frases cortas y largas, incisos, primera persona, tecnicismos, coloquialismos, cierta aspereza, dudas o fragmentos cuando el género los admite.

### Haz la mínima intervención eficaz

Corrige el slop real. No reescribas todo para demostrar que editaste.

Reorganiza solo si la secuencia oculta el punto, repite una idea o separa una afirmación de su soporte. Si el texto ya funciona, puede quedar casi igual.

### Una idea se explica una vez

Cuando una idea importante ya fue explicada con suficiente detalle, después úsala o refiérela; no la reintroduzcas con sinónimos.

Distingue repetición funcional de repetición ornamental. En documentación técnica, repetir el término correcto suele ser mejor que rotar vocabulario.

### Edita información antes que sinónimos

Cambiar `significativo` por `considerable` no arregla una frase vacía.

Busca qué dato, mecanismo, restricción, decisión o consecuencia sostiene la afirmación. Si el material no lo contiene, recorta o condiciona la frase; no inventes especificidad.

Ejemplo:

> La implementación representa un avance significativo que permite optimizar distintos procesos.

Si el contexto realmente lo dice:

> La implementación elimina la carga manual de pedidos entre el e-commerce y el ERP.

Si el contexto no lo dice, no fabriques esa segunda frase.

### Protege los detalles concretos

No conviertas:

> El deploy bajó de 40 a 8 minutos.

En:

> El nuevo enfoque mejoró significativamente la eficiencia del despliegue.

Nombres, cifras, fechas, condiciones, mecanismos y decisiones tienen prioridad sobre adjetivos de importancia.

### Usa el test de portabilidad

Pregunta:

> ¿Esta oración podría copiarse sin cambios a otra empresa, proyecto, país o persona?

Si la respuesta es sí y la frase no cumple una función retórica necesaria, probablemente es relleno. Elimínala o ancla la idea en información disponible.

### Prefiere verbos directos

Simplifica perífrasis burocráticas cuando no pierdas precisión:

- `llevar a cabo una revisión` → `revisar`;
- `proceder a realizar` → `realizar` o `hacer`;
- `efectuar la implementación` → `implementar`;
- `tener la capacidad de` → `poder`;
- `hacer uso de` → `usar`.

No destruyas términos nominales que sean conceptos técnicos reales.

### No anuncies la importancia si el texto puede demostrarla

Revisa, no prohíbas:

- `es importante destacar`;
- `cabe señalar`;
- `resulta fundamental`;
- `este punto es clave`;
- `cobra especial relevancia`.

Elimina el marcador si solo etiqueta la frase siguiente como importante. Consérvalo si el género realmente necesita señalización explícita.

### No fuerces contraste ni equilibrio

Estructuras como `no se trata de X, sino de Y`, `por un lado... por otro lado...` u `oportunidades y desafíos` son válidas cuando representan el razonamiento real. Corrígelas cuando existen solo para fabricar simetría.

### Deja que la lógica haga las transiciones

No insertes conectores por reflejo. Revisa concentraciones de `en este sentido`, `asimismo`, `de esta manera`, `por otro lado`, `sin embargo`, `por lo tanto`, `en definitiva` o equivalentes.

Una aparición aislada no es un problema. El problema es usarlos para simular continuidad donde no hay progresión real.

### Vigila verbos comodín repetidos

En especial, revisa secuencias donde `permite`, `facilita`, `mejora`, `optimiza` o `garantiza` aparecen una y otra vez sin precisar mecanismo.

No sustituyas mecánicamente por sinónimos. Reestructura la frase o elimina la afirmación redundante.

### Conserva terminología técnica estable

No cambies `workspace`, `checkout`, `HEAD`, `SHA`, `endpoint`, `seller`, `binding` u otros términos solo para “variar”. Primero determina si son conceptos distintos. Consistencia > variedad decorativa.

## Qué cuenta como señal de slop

No uses palabras aisladas como detector. Evalúa combinaciones de patrones:

- baja densidad informativa;
- repetición semántica;
- estructura predecible que domina el contenido;
- abstracción sin referente;
- metadiscurso que dice al lector qué debe considerar importante;
- tríadas o enumeraciones por reflejo;
- conectores seriales;
- formalidad no motivada por el canal;
- español deslocalizado o calcos;
- cierre grandilocuente o recapitulación sin función;
- rotación de sinónimos para el mismo concepto;
- voz que cambia durante el documento.

Para ejemplos y casos límite, consulta [references/patrones-es.md](references/patrones-es.md). Para la calibración editorial por defecto y ejemplos de decisiones aceptadas, consulta [references/calibracion-editorial.md](references/calibracion-editorial.md) cuando el texto no tenga una voz suficientemente clara o la edición sea extensa.

## Salida por modo

### Editar

Devuelve el texto completo editado.

Salvo que el usuario pida solo el texto o el formato no admita comentarios, añade al final:

**Cambios realizados**
- 2–5 puntos breves sobre cambios sustantivos.

No enumeres microcorrecciones.

### Redactar

Entrega el artefacto solicitado. No añadas una explicación del método salvo que el usuario la pida.

Cuando el usuario ya ha dado contenido suficiente, escribe desde ese contenido; no lo expandas con generalidades para “completar”.

### Auditar

No reescribas. Usa:

| Patrón | Fragmento | Problema | Acción |
|---|---|---|---|
| [patrón] | “[fragmento breve]” | [efecto editorial] | [acción concreta] |

Después, si aporta valor, añade **Lo que conviene preservar** con voz, datos, tecnicismos o estructura que ya funcionan.

No asignes porcentaje de IA ni atribuyas autoría.

## Restricciones

- No inventes experiencias, escenas, cifras, fuentes, citas, nombres ni resultados.
- No aumentes el grado de certeza del autor.
- No introduzcas faltas deliberadas.
- No uses “burstiness”, traducción de ida y vuelta ni aleatoriedad estilística para eludir detectores.
- No neutralices español regional sin motivo de audiencia.
- No vuelvas informal un texto técnico, académico o jurídico solo para hacerlo “más humano”.
- No elimines terminología válida por parecer compleja.
- No conviertas toda prosa en frases cortas.
- No añadas entusiasmo, diplomacia u opiniones que el autor no expresó.
- No transformes una lista útil en prosa ni una prosa clara en lista por decoración.

## Workflow

1. Determina `editar`, `redactar` o `auditar`.
2. Lee el texto y el contexto disponible antes de cambiar nada.
3. Identifica mensaje y señales de voz.
4. Detecta problemas por función y patrón, no por blacklist.
5. Resuelve primero fidelidad, después densidad, estructura, voz y microestilo.
6. Haz la mínima intervención eficaz.
7. Para textos de más de ~150 palabras, ediciones extensas o cualquier caso dudoso, aplica [eval.md](eval.md).
8. Si falla un criterio aplicable, corrige y vuelve a revisar.
9. Entrega en el formato que pidió el usuario.

## Casos límite

- Un texto correcto y formal puede estar bien. Formalidad no equivale a slop.
- Un cliché puede ser la frase correcta. Evalúa función, frecuencia y contexto.
- Repetir terminología técnica puede mejorar precisión.
- Primera persona, oralidad y errores no son requisitos de “humanidad”.
- La concreción solo sirve si procede del texto o de fuentes reales.
- Si el usuario pide evadir GPTZero, Turnitin u otro detector, no optimices el score; sí puedes mejorar precisión, fuentes, voz, densidad y trazabilidad.
