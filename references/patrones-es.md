# Patrones de IA slop en español

Referencia editorial para `no-ia-slop-es`.

Esta guía describe señales de **calidad textual**, no fingerprints de autoría. Ninguna palabra, conector, longitud de frase o patrón de puntuación demuestra que un texto haya sido generado por IA.

## Cómo usar esta referencia

Consulta este archivo cuando:

- un texto “suena a IA” pero no es evidente por qué;
- necesitas distinguir un giro legítimo de un patrón repetido;
- quieres revisar español técnico, profesional, académico o comercial;
- el texto parece traducido o excesivamente neutro;
- estás auditando sin reescribir.

No cargues esta referencia para una corrección trivial de una o dos frases.

## 1. Densidad informativa

### Señal

El texto ocupa espacio sin añadir proposiciones nuevas.

### Preguntas

- ¿Cada párrafo agrega un hecho, razón, mecanismo, restricción, ejemplo, decisión o consecuencia?
- ¿La segunda mitad del párrafo solo reformula la primera?
- ¿Los adjetivos podrían sustituirse por información concreta disponible?
- ¿La conclusión se limita a repetir la introducción?

### Ejemplo

Débil:
> La migración representa un paso importante para optimizar la operación y mejorar la eficiencia general del proceso.

Mejor, si el contexto lo sustenta:
> La migración elimina la carga manual de stock entre el ERP y VTEX.

No inventes la segunda frase si el borrador no contiene ese mecanismo.

## 2. Carácter formulaico

### Señal

La estructura parece decidir el contenido en vez de al revés.

Patrones frecuentes:

- introducción general;
- lista simétrica de beneficios;
- lista simétrica de desafíos;
- llamado a un “enfoque equilibrado”;
- cierre con `en conclusión` o `en última instancia`.

### Corrección

Conserva solo las etapas que el argumento necesite. No es obligatorio tener apertura, contraste y cierre en cada pieza.

## 3. Conectores seriales

Conectores normales del español pueden convertirse en muletas si aparecen con una cadencia mecánica:

- `en este sentido`;
- `asimismo`;
- `por otra parte`;
- `por otro lado`;
- `sin embargo`;
- `de este modo`;
- `por lo tanto`;
- `en consecuencia`;
- `en última instancia`.

La regla no es “eliminar conectores”. La regla es evitar que sustituyan relaciones lógicas que deberían ser evidentes por el contenido.

## 4. Marcadores de importancia

Revisa:

- `es importante destacar`;
- `cabe destacar`;
- `cabe señalar`;
- `resulta fundamental`;
- `es crucial`;
- `es clave`;
- `cobra relevancia`;
- `merece especial atención`;
- `no debe pasarse por alto`.

Tres resultados posibles:

1. **Eliminar** si la frase siguiente ya demuestra la importancia.
2. **Concretar** si falta explicar por qué importa.
3. **Conservar** si el género necesita señalización explícita, por ejemplo una recomendación ejecutiva o una advertencia.

## 5. Sustantivos abstractos y verbos débiles

Acumulaciones frecuentes:

- `implementación de la optimización`;
- `realización de la revisión`;
- `ejecución de la validación`;
- `generación de una mejora`;
- `aplicación de un enfoque`.

Busca un verbo claro cuando no se pierda precisión:

- `revisar`;
- `validar`;
- `mejorar`;
- `implementar`;
- `aplicar`.

No destruyas conceptos técnicos nominales. `implementación`, `validación` o `arquitectura` pueden ser los términos correctos.

## 6. Adjetivación corporativa

Vocabulario de riesgo cuando no tiene referente:

- `robusto`;
- `integral`;
- `estratégico`;
- `innovador`;
- `transformador`;
- `escalable`;
- `fluido`;
- `eficiente`;
- `significativo`;
- `relevante`;
- `dinámico`;
- `sostenible`;
- `potente`.

Pregunta: ¿qué propiedad observable justifica el adjetivo?

`arquitectura escalable` puede ser exacto si el texto explica cómo escala.
`solución robusta y escalable` como cierre promocional probablemente no dice nada.

## 7. Tríadas automáticas

Los modelos tienden a producir enumeraciones limpias porque son fáciles de completar.

Ejemplos:

- `claridad, precisión y eficiencia`;
- `ágil, segura y escalable`;
- `personas, procesos y tecnología`.

No reduzcas automáticamente a dos. Revisa si cada elemento tiene desarrollo o evidencia.

## 8. Contrastes prefabricados

Patrones:

- `no se trata de X, sino de Y`;
- `no solo X, sino también Y`;
- `más que X, Y`;
- `si bien X, Y`;
- `por un lado X; por otro, Y`.

Conserva cuando el contraste es real y útil. Corrige cuando funciona como dramatización o produce un falso equilibrio.

## 9. Metadiscurso

Señales:

- `la clave aquí es`;
- `el punto central es`;
- `como podemos observar`;
- `esto demuestra`;
- `lo anterior pone de manifiesto`;
- `en otras palabras`;
- `dicho de otro modo`;
- `conviene entender que`.

El metadiscurso no es malo. Es slop cuando comenta un argumento que ya se entiende o le asigna peso sin aportar evidencia.

## 10. Cierres de falsa profundidad

Tipos:

- aforismo genérico;
- metáfora final no preparada;
- frase tipo eslogan;
- conclusión que infla la escala del tema;
- `el futuro no es X; es Y`.

Prefiere terminar en:

- una decisión;
- un dato;
- una consecuencia;
- una pregunta real;
- un siguiente paso;
- la última evidencia útil.

## 11. Simetría de párrafos

Revisa si todos los párrafos:

- tienen longitud parecida;
- empiezan con conector;
- contienen una afirmación, dos apoyos y una frase de cierre;
- terminan con una mini-conclusión.

No rompas la simetría por aleatoriedad. Une, corta o expande según la complejidad real de cada idea.

## 12. Formalidad no motivada

Un registro formal puede ser apropiado en un informe y artificial en:

- un mensaje de Slack;
- una reseña;
- una respuesta breve;
- una conversación interna;
- una nota personal.

Señales de desajuste:

- tratamiento distante sin motivo;
- léxico administrativo en conversación;
- oraciones impersonales innecesarias;
- nominalizaciones en cadena.

La solución es adecuar el registro al canal, no “hacerlo casual” por sistema.

## 13. Impersonales y pasivas reflejas

Revisa acumulaciones de:

- `se procede a`;
- `se realiza`;
- `se lleva a cabo`;
- `se considera`;
- `se evidencia`;
- `se observa`;
- `fue realizado por`.

Pueden ser correctas en ciencia, procesos o cuando el agente no importa. Prefiere sujeto explícito cuando mejora responsabilidad o claridad:

> El equipo de QA ejecutó las pruebas.

en vez de:

> Se llevó a cabo la ejecución de las pruebas.

## 14. Calcos y español deslocalizado

No existe un catálogo universal. Revisa contexto y variedad.

Posibles señales:

- sintaxis que sigue demasiado de cerca una fuente inglesa;
- términos técnicos traducidos de varias formas;
- colocaciones comprensibles pero poco naturales;
- conservación artificial del orden de la frase original;
- español excesivamente “internacional” cuando el autor usa una variedad regional clara.

Evita prescriptivismo innecesario. Una construcción puede ser natural en Chile y extraña en España, o viceversa.

## 15. Sinónimos rotatorios

Problema:

> El agente revisa el borrador. Luego el asistente puntúa el documento. Finalmente la herramienta propone cambios.

Si es la misma entidad:

> El agente revisa el borrador, lo evalúa y propone cambios.

En documentación técnica, consistencia > variación decorativa.

## 16. Listas innecesarias y formato decorativo

Señales:

- cinco bullets que podrían ser dos frases;
- encabezado para un único párrafo;
- negritas en cada oración;
- emojis como sustituto de jerarquía;
- tablas para información que no se compara.

No elimines listas útiles. La forma debe corresponder a la estructura de la información.

## 17. Falta de trazabilidad factual

Señales:

- cifras sin fuente;
- citas vagas;
- `estudios demuestran`;
- nombres o fechas introducidos sin respaldo;
- afirmaciones de causalidad sin mecanismo.

No “humanices” inventando detalles. Cuando falta sustento:

- conserva la incertidumbre;
- elimina el dato;
- pide la fuente si es indispensable;
- marca el hueco si el formato lo permite.

## 18. Voice drift

Después de editar, compara el inicio y el final del texto.

Problemas:

- el autor empieza directo y termina corporativo;
- un texto chileno acaba en español peninsular;
- un documento técnico pierde terminología propia;
- una voz seca se convierte en entusiasmo;
- desaparecen dudas legítimas.

La consistencia de voz no exige uniformidad sintáctica.

## 19. Prueba de portabilidad

Marca como candidata a slop cualquier frase que pueda pasar a otro contexto sin cambiar nada:

> La transformación digital se ha convertido en un factor clave para las organizaciones modernas.

Preguntas:

- ¿qué organización?;
- ¿qué transformación?;
- ¿qué cambió?;
- ¿qué decisión depende de esto?

Si el texto no necesita responderlas, quizá la oración completa sobra.

## 20. Qué no usar como detector

No concluyas “esto es IA” por:

- una palabra;
- uso correcto de tildes;
- ausencia de errores;
- em dash o raya;
- frases largas;
- frases cortas;
- primera persona;
- falta de primera persona;
- un conector;
- una metáfora;
- puntuación uniforme;
- lenguaje formal.

Evalúa perfiles de calidad y función, no procedencia.
