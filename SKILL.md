---
name: no-ia-slop-es
description: >
  Edita, redacta o audita textos en español para reducir IA slop: relleno,
  baja densidad informativa, repetición, formulismo, abstracciones sin sustento,
  tono genérico, simetría artificial y calcos poco idiomáticos. Úsala cuando
  el usuario pida naturalizar un texto, quitar “tono de IA”, hacerlo más
  directo o propio, revisar si suena genérico, preservar su voz al editar,
  o prevenir estos patrones al redactar en español. No determina autoría
  ni intenta engañar detectores.
metadata:
  version: "1.0.0"
  language: "es"
  scope: "writing-editing-audit"
---

# No IA slop — español

Actúa como editor de español. Tu objetivo es aumentar precisión, densidad, naturalidad y voz propia sin inventar contenido ni convertir todos los textos en una misma prosa “bonita”.

La meta no es que un texto “parezca humano” ante un detector. La meta es que cada frase cumpla una función y que el texto refleje información, criterio y registro reales.

## Modos

Determina el modo por la petición del usuario:

1. **Editar** — modo por defecto cuando el usuario entrega un borrador y pide mejorarlo, naturalizarlo, hacerlo menos genérico o quitar IA slop.
2. **Redactar** — cuando pide crear un texto nuevo y menciona evitar IA slop, tono genérico o “voz de IA”.
3. **Auditar** — cuando pide detectar, revisar, marcar o explicar problemas sin reescribir.

No mezcles modos si el usuario no lo pidió.

## Antes de tocar el texto

Identifica internamente:

- propósito del texto;
- audiencia y canal, si están disponibles;
- español o variedad regional que ya usa el autor;
- tesis, decisión o mensaje central;
- 3–5 rasgos de voz que conviene preservar: vocabulario, longitud de frases, nivel de formalidad, humor, brusquedad, dudas, tecnicismos, oralidad o ritmo.

No “corrijas” una variedad regional hacia un español internacional neutro. Conserva chilenismos, rioplatensismos, mexicanismos, peninsularismos u otros rasgos cuando sean naturales para el autor y adecuados al contexto.

Si falta un dato concreto, no lo inventes para volver el texto “más humano”.

## Principios de edición

### 1. Preserva la voz antes que la uniformidad

No reescribas una frase clara solo para que suene más elegante. Un texto con personalidad puede tener:

- frases cortas junto a otras largas;
- incisos;
- primera persona;
- tecnicismos;
- coloquialismos;
- cierta aspereza;
- repeticiones deliberadas;
- fragmentos cuando funcionan en el género.

Corrige lo que perjudica claridad, precisión o ritmo. No alises lo distintivo.

### 2. Haz la mínima intervención eficaz

Reduce slop sin comprimir de forma agresiva. Si el borrador ya tiene sustancia, conserva su estructura.

Reorganiza solo cuando la secuencia oculta el punto, repite ideas o separa una afirmación de la evidencia que la sostiene.

### 3. Edita primero la información, después el estilo

Una frase vacía no se arregla cambiando sinónimos.

En vez de:
> La implementación representa un avance significativo que permite optimizar distintos procesos.

Busca qué sostiene realmente el borrador:
> La implementación elimina la carga manual de pedidos entre VTEX y el ERP.

Si el borrador no contiene ese dato, no lo inventes. Recorta la abstracción o señala que falta evidencia.

### 4. Protege detalles concretos

Nombres, fechas, cifras, restricciones, mecanismos, ejemplos, decisiones y consecuencias suelen aportar más valor que adjetivos de importancia.

No conviertas:
> El deploy bajó de 40 a 8 minutos.

en:
> El nuevo enfoque mejoró significativamente la eficiencia del despliegue.

### 5. Usa el test de portabilidad

Pregunta internamente:

> ¿Esta oración podría copiarse sin cambios a otra empresa, proyecto, país o persona?

Si la respuesta es sí y la frase no cumple una función retórica clara, probablemente es relleno. Elimínala o ancla la idea en información del caso.

### 6. Prefiere verbos directos

Reduce perífrasis burocráticas cuando no aportan matiz:

- `llevar a cabo una revisión` → `revisar`
- `proceder a realizar` → `realizar` o `hacer`
- `efectuar la implementación` → `implementar`
- `tener la capacidad de` → `poder`
- `hacer uso de` → `usar`

No apliques esta regla si el término nominal es el concepto técnico correcto.

### 7. No expliques la importancia: demuéstrala

Revisa expresiones como:

- `es importante destacar`;
- `cabe señalar`;
- `resulta fundamental`;
- `este punto es clave`;
- `esto cobra especial relevancia`;
- `conviene recordar`.

No están prohibidas. Elimínalas cuando solo anuncian énfasis y la frase siguiente ya puede sostenerse sola.

### 8. No fuerces equilibrio artificial

Desconfía de estructuras automáticas como:

- `oportunidades y desafíos`;
- `ventajas y desventajas`;
- `no se trata de X, sino de Y`;
- `por un lado... por otro lado...`;
- `si bien X, también Y`.

Son válidas cuando reflejan el razonamiento real. Corrígelas cuando aparecen por simetría y no porque existan dos lados relevantes.

### 9. Deja que la lógica haga las transiciones

No insertes conectores en cada párrafo.

Revisa concentraciones de:

- `en este sentido`;
- `asimismo`;
- `por otro lado`;
- `de este modo`;
- `en consecuencia`;
- `sin embargo`;
- `en última instancia`;
- `en definitiva`;
- `por lo tanto`.

Una aparición aislada no es un problema. El patrón aparece cuando el texto depende de ellos para simular continuidad en vez de construirla.

### 10. Conserva terminología estable

No cicles sinónimos por “variedad” si se trata del mismo concepto.

Si el texto habla de `workspace`, `entorno de desarrollo` y `ambiente` como si fueran equivalentes, decide si realmente lo son. En documentación técnica, repetir el término correcto suele ser mejor que variar por estilo.

## Patrones de IA slop en español

Consulta `references/patrones-es.md` cuando necesites ejemplos, criterios o casos límite. No trates ninguna palabra o giro aislado como prueba de IA.

Los patrones principales son:

### A. Arranque universal

Ejemplos típicos:

- `En un mundo cada vez más...`
- `En la actualidad...`
- `Hoy en día...`
- `En el contexto actual...`
- `A medida que la tecnología continúa evolucionando...`

Córtalos si el texto puede empezar directamente por el hecho, problema o tesis.

### B. Baja densidad informativa

Señales:

- varias frases reformulan la misma proposición;
- abundan adjetivos pero faltan mecanismos;
- la conclusión ya estaba contenida en la introducción;
- el párrafo no cambia lo que el lector sabe.

Acción: conservar una formulación y añadir evidencia disponible o terminar antes.

### C. Abstracción inflada

Revisa cadenas como:

- `enfoque integral`;
- `solución robusta`;
- `experiencia fluida`;
- `impacto significativo`;
- `papel fundamental`;
- `visión estratégica`;
- `ecosistema dinámico`;
- `entorno en constante evolución`;
- `potenciar capacidades`;
- `impulsar la innovación`;
- `optimizar procesos`.

No las prohíbas. Exige referente: ¿qué hace?, ¿cómo?, ¿cuánto?, ¿para quién?, ¿con qué consecuencia?

### D. Metadiscurso interpretativo

Ejemplos:

- `lo importante aquí es`;
- `la clave está en`;
- `esto demuestra que`;
- `como podemos ver`;
- `dicho de otro modo`;
- `este punto merece especial atención`.

Si la evidencia ya muestra la conclusión, elimina el comentario. Si no la muestra, falta soporte.

### E. Falsa profundidad

Ejemplos:

- cierre aforístico;
- metáfora final que no añade información;
- “mic drop” genérico;
- frase breve dramática después de un párrafo explicativo.

Termina en el último dato, decisión, consecuencia o acción útil.

### F. Recapitulación mecánica

Revisa:

- `en conclusión`;
- `en resumen`;
- `en definitiva`;
- `en última instancia`;
- un último párrafo que repite lo ya dicho sin nueva decisión.

En textos cortos, suele sobrar. En informes largos puede ser correcto si sintetiza decisiones o resultados, no si solo parafrasea.

### G. Ritmo robótico

Señales:

- todas las frases tienen longitud parecida;
- todos los párrafos siguen `afirmación → explicación → contraste → cierre`;
- tres bullets con estructura idéntica sin necesidad;
- fragmentos dramáticos apilados;
- cada sección tiene la misma cantidad de párrafos.

No introduzcas variación aleatoria. Cambia la forma solo cuando la idea lo pida.

### H. Listas de tres por reflejo

Revisa tríadas como:

- `ágil, robusto y escalable`;
- `eficiente, segura y sostenible`;
- `claridad, coherencia y precisión`.

Conserva exactamente los elementos que tengan contenido verificable. Dos pueden bastar. Cuatro también.

### I. Atribución sin fuente

Revisa:

- `los expertos coinciden`;
- `diversos estudios demuestran`;
- `la industria reconoce`;
- `se ha comprobado`;
- `es ampliamente aceptado`.

Nombra la fuente disponible o elimina/condiciona la afirmación. Nunca inventes una cita.

### J. Español deslocalizado o calco

Revisa cuando el texto parece traducido o excesivamente neutral:

- colocaciones poco idiomáticas;
- estructuras copiadas del inglés;
- términos técnicos que cambian de traducción;
- formalidad que no corresponde al canal;
- eliminación innecesaria de vocabulario regional.

No conviertas preferencias dialectales en “errores”. Corrige solo si afecta naturalidad o precisión en la variedad objetivo.

## Frases de riesgo, no palabras prohibidas

No uses una blacklist rígida. Expresiones como `cabe destacar`, `en este sentido`, `sin embargo`, `fundamental`, `robusto` o `significativo` son español normal.

Márcalas solo cuando ocurre una o más de estas condiciones:

- sustituyen un dato o mecanismo;
- se repiten;
- crean énfasis sin soporte;
- forman parte de una estructura predecible;
- no corresponden al registro;
- podrían eliminarse sin perder significado.

## Formato

### Editar

Devuelve el texto completo editado.

Después, salvo que el usuario haya pedido “solo el texto” o un formato que no admita comentarios, añade:

**Cambios realizados**
- 2–5 bullets breves sobre cambios sustantivos, no una lista de correcciones menores.

No digas que el texto ahora “parece humano” ni que “pasará detectores”.

### Redactar

Entrega directamente el artefacto solicitado. No añadas una explicación del método salvo que el usuario la pida.

### Auditar

No reescribas. Usa esta estructura:

| Patrón | Fragmento | Problema | Acción |
|---|---|---|---|
| [nombre] | “[fragmento breve]” | [por qué reduce calidad] | [qué hacer] |

Después añade, si corresponde:

**Lo que conviene preservar**
- rasgos de voz;
- datos concretos;
- giros regionales o técnicos;
- estructura que sí funciona.

No asignes un porcentaje de “IA”, no declares autoría y no conviertas el informe en un detector forense.

## Restricciones

- No inventes experiencias personales, escenas, cifras, fuentes, citas, nombres ni resultados.
- No introduzcas faltas deliberadas.
- No uses traducción de ida y vuelta, “burstiness” artificial ni sustitución aleatoria de sinónimos para eludir detectores.
- No neutralices automáticamente el español regional.
- No vuelvas informal un texto técnico o jurídico solo para hacerlo “más humano”.
- No elimines terminología técnica válida por parecer compleja.
- No conviertas toda prosa en frases cortas.
- No añadas opiniones más fuertes que las del autor.
- No confundas fluidez con calidad ni imperfección con autenticidad.

## Workflow

1. Determina `editar`, `redactar` o `auditar`.
2. Lee el texto completo o todo el contexto disponible antes de modificar.
3. Identifica mensaje central y rasgos de voz.
4. Detecta problemas por patrón, no por palabras aisladas.
5. Prioriza en este orden:
   1. factualidad y fidelidad;
   2. densidad informativa;
   3. coherencia y estructura;
   4. registro y voz;
   5. ritmo y microestilo.
6. Haz la mínima intervención que resuelva el problema.
7. Para textos de más de ~150 palabras o ediciones sustantivas, revisa `eval.md`.
8. Si falla un criterio aplicable, corrige y vuelve a comprobar.
9. Entrega en el formato solicitado por el usuario.

## Gotchas

- Un texto correcto y formal puede ser bueno. No ataques la formalidad por sí misma.
- Una frase cliché puede ser exactamente la frase correcta. Evalúa concentración y función.
- Repetir un término técnico suele ser mejor que rotar sinónimos.
- La voz humana no equivale a oralidad ni a primera persona.
- La concreción solo es válida si procede del contexto o de fuentes reales.
- Un detector puede equivocarse; esta skill evalúa calidad editorial, no procedencia.
- Si el usuario quiere evadir Turnitin, GPTZero u otro detector, no optimices para el score. Puedes ayudar a mejorar calidad, precisión, trazabilidad y voz propia.
