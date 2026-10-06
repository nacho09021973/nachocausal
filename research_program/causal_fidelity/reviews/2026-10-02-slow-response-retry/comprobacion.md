# Contraste del informe independiente

Fecha: 2026-10-02. Estado: `REVIEW_RECEIVED / TWO_OBJECTIONS_RESPONDIDAS`.
El informe sin editar está en informe_deepseek.md. Veredicto del revisor:
`REQUIERE_CORRECCION`. No se sustituye por el juicio del autor.

## 1. Procedencia y alcance de la revisión

El usuario autorizó un nuevo intento con «pues pasala con deep o gemini».
Se usó la herramienta compartida revision-ciega,
~/herramientas @ `f1b54d7e9a79252605aa3ed5fc2dc06f51cf7096`.
La herramienta recibió opciones para thinking=disabled, max_tokens=8192
y conservación de finish_reason. Se comprobaron sintaxis Bash y diff.
No se copiaron herramientas compartidas al repo.

Opciones contrastadas con documentación primaria de la API:
https://api-docs.deepseek.com/api/create-chat-completion/, campos thinking,
max_tokens y finish_reason, consultados el 2026-10-02.

La entrada tiene la misma huella que el intento anterior:
`1ca2dec8208ae1bf4df9a21dcfbbe651972eef8ae39f1486b278eeeb122c9fef`.
Los documentos pertenecen al commit 71a5adf, no a sus modificaciones
posteriores. La cabecera del informe conserva sus hashes individuales.
Modelo: deepseek-v4-pro; petición 575b2f32-6d1d-40b2-b742-9ce852bdc92a.
La API registra finish_reason=stop, 8885 tokens de entrada y 3792 de salida.
Se recibió texto completo. El modo sin razonamiento es una limitación de
esta revisión; un informe de otra familia tampoco constituye una prueba.
No se ejecuta otra ronda.

## 2. Registro de objeciones

| ID | Afirmación atacada | Estado | Condición de cierre |
| --- | --- | --- | --- |
| O1 | Interpretar insuficiencia de tau como refutación del contrato histórico | respondida | Un revisor o persona comprueba que el texto limita el contraejemplo a lecturas del blanco ampliado y no descarta el test histórico ni todos los Q |
| O2 | Falta de detalle en la retención de modos y convergencia fuerte de Pi_n | respondida | Un revisor o persona comprueba normalización del muestreo, corte cuadrado, cota de error y argumento de densidad escritos en §5 |

Respondida significa que el texto contesta. Ninguna fila se declara
resuelta por esta comprobación del autor.

## 3. O1: contraste de alcance

El documento revisado SLOW_PROTOCOL_RESPONSE §1 ya declaraba ampliación
del blanco y que no satisfacía el gate físico. Su §4 limitaba la suficiencia
a lecturas lineales. GROWING_FAMILY_RESPONSE §7 afirmaba insuficiencia para
su respuesta lineal lenta, no una refutación general del contrato histórico.
Por tanto no se acepta la lectura amplia del revisor como una refutación
matemática de esas frases. Sí se añade una aclaración explícita en ambos
documentos para impedir confundir los dos blancos.

El argumento desde cero es: misma entrada marcada y mismo tau proporcionan
la misma entrada a una regla que sólo usa esos datos; dos lecturas distintas
no pueden ser reconstruidas ambas por esa regla. Esto demuestra únicamente
no determinación de esas lecturas por tau. No exige que el contrato histórico
autorice las lecturas y no invalida su igualdad de llegada. Tampoco prueba
insuficiencia de cualquier escalar Q: el contrato admite una regla q adicional.
No se incorpora la sugerencia de declarar demasiado restrictivo todo ese
contrato para cualquier objetivo.

Evidencia de respuesta: SLOW_PROTOCOL_RESPONSE §1 y GROWING_FAMILY_RESPONSE §7.

## 4. O2: derivación correcta del lema

Se acepta añadir detalle de la prueba. El lema propuesto por el revisor
contiene dos errores, por lo que no se copia:

1. La condición espectral es lambda<=epsilon^2=1/(4n), no
   lambda<=(4n)^(-1/2). Comparar con epsilon sólo verifica un corte más amplio.
2. El vector muestreado debe ser phi_j(centro)/sqrt(n). Con el muestreo
   sin ese factor, E_n introduce sqrt(n), y no converge a phi_j como se afirma
   en la corrección sugerida. Para j=0, ese error ya hace que la norma crezca.

Se rederiva en GROWING_FAMILY_RESPONSE §5: lambda<=pi^2 j^2/(16n^2)
y por tanto se retiene el modo para n>=ceil(pi^2 j^2/4), j>=1 fijo.
E_n del muestreo normalizado es la aproximación por centros de celda.
La cota de derivada da error L2<=pi j/(4sqrt(2)n). El modo cero es
exacto. Se extiende a una suma finita por desigualdad triangular y luego
a cada h por densidad y ||I-Pi_n||<=1. Los cuantificadores aproximan
primero h por una suma fija y luego hacen crecer n.

Esta ampliación justifica convergencia fuerte, no convergencia en norma.
La lectura constante 93/256 se comprueba además sin ese argumento de
convergencia, pues está retenida exactamente para cada n.

Evidencia de respuesta: GROWING_FAMILY_RESPONSE §5, lema y cotas explícitas.

## 5. Estado posterior

El informe y el intento fallido anterior se conservan sin sobrescribirlos.
Las aclaraciones añadidas son posteriores a la revisión y no tienen un
veredicto externo nuevo. El PR sigue en borrador; no se declara promoción,
cierre de objeciones ni autorización para simulaciones o fusión.
