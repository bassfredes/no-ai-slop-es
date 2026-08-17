# Calibración editorial por defecto

Usa esta referencia cuando el usuario no haya definido una voz suficientemente clara o cuando una edición extensa necesite un criterio consistente. Si el borrador ya tiene una voz identificable, esa voz tiene prioridad.

Esta calibración proviene de decisiones editoriales reales en español profesional, técnico y académico. No es una plantilla de estilo y no pretende convertir todas las salidas en la voz de una persona concreta.

## Criterio central

**Una idea importante se explica completamente una vez; después se utiliza, no se vuelve a presentar.**

Antes de añadir un párrafo, conector o reformulación, pregunta qué información nueva aporta.

## Preferencias por defecto

- Directo antes que ceremonial.
- Preciso antes que elegante.
- Estructura antes que sustitución de sinónimos.
- Terminología estable antes que “variedad léxica”.
- Una afirmación respaldada antes que tres adjetivos.
- Edición mínima antes que reescritura masiva.
- Español regional natural antes que neutralización automática.
- Formalidad funcional antes que tono corporativo.

## Patrones especialmente sensibles

### Repetir la misma idea con otra redacción

Débil:

> El sistema busca reducir el trabajo manual. De esta manera, permite disminuir la intervención humana en el proceso. Por lo tanto, se optimiza la automatización de tareas que antes se realizaban manualmente.

Mejor:

> El sistema reduce el trabajo manual en el proceso de correspondencia.

Si existe un mecanismo concreto, añádelo. Si no, termina ahí.

### `permite` como verbo comodín

No sustituyas cada `permite` por `facilita` o `posibilita`. Revisa qué relación expresa.

Débil:

> La capa permite validar contratos, permite detectar errores y permite mejorar la trazabilidad.

Más directo:

> La capa valida contratos, detecta errores y registra la trazabilidad.

Solo usa la segunda versión si esos verbos describen realmente el comportamiento.

### Conectores por defecto

Revisa especialmente secuencias con:

- `en este contexto`;
- `de esta manera`;
- `por lo tanto`;
- `en este sentido`;
- `asimismo`.

No los reemplaces por otros conectores para ocultar el patrón. Elimina el conector cuando la relación ya sea evidente.

### Contraste prefabricado

`No solo X, sino también Y` suele inflar una enumeración simple. Si no hay un contraste real, escribe X e Y directamente.

### Tríadas decorativas

`robusto, escalable y eficiente` no mejora un texto si ninguna propiedad está desarrollada. Mantén solo propiedades verificables.

## Español chileno y profesional

No sustituyas automáticamente expresiones naturales como `acá`, `al tiro`, `cachamos` o giros locales si el canal y la audiencia los admiten.

Tampoco fuerces chilenismos. La variedad regional se preserva cuando ya existe o cuando el usuario la pide.

En comunicación técnica interna puede convivir español chileno con términos ingleses establecidos: `workspace`, `checkout`, `endpoint`, `deploy`, `HEAD`, `seller`. No traduzcas por consistencia superficial.

## Escritura académica

Naturalizar no significa volver coloquial un texto académico.

Ejemplo de intervención aceptable:

> Revisar y seleccionar técnicas, herramientas y enfoques de correspondencia semántica de esquemas que resulten adecuados para el problema abordado en el proyecto.

Puede simplificarse a:

> Revisar y escoger técnicas, herramientas y enfoques de correspondencia semántica de esquemas que sean convenientes para el problema que trata el proyecto.

La mejora buscada es sintáctica y léxica; no se elimina la precisión del dominio.

## Escritura técnica

Un fragmento como este ya tiene una voz útil:

> El checkout se puede mantener. El problema está principalmente en logística y en separar qué parte queda en la plataforma y qué parte pasa a headless.

No lo conviertas en:

> Resulta fundamental adoptar un enfoque integral que permita mantener el checkout mientras se optimiza la separación estratégica de responsabilidades.

El segundo texto pierde mecanismo y añade grandilocuencia.

## Tickets, Jira y decisiones

Prioriza:

- contexto necesario;
- estado observable;
- acción requerida;
- criterio de aceptación verificable.

Evita introducciones de cortesía, resúmenes duplicados y cierres genéricos cuando el artefacto es operativo.

## Comunicaciones profesionales

Natural no significa brusco. Conserva saludos, agradecimientos o fórmulas de cortesía cuando cumplen una función social real. Recorta únicamente la cortesía repetida o excesivamente ceremoniosa.

## Señal de sobre-edición

Detente cuando ocurre cualquiera de estos cambios sin necesidad:

- desaparecen expresiones que el autor usaría;
- sube el registro sin que cambie la audiencia;
- aparecen adjetivos o conclusiones más fuertes;
- una frase clara se convierte en dos frases “perfectas”;
- los párrafos quedan demasiado simétricos;
- cambia terminología técnica correcta;
- se agrega explicación que el lector objetivo ya conoce.
