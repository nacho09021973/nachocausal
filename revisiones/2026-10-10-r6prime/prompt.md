# Encargo: revisión ciega de un resultado analítico

---

Revisas **un resultado**, no una auditoría: `S4W_R6PRIME_W1_CHANNEL_2026-10-10.md`. Van
adjuntos la auditoría que lo encargó (para contexto y para que veas qué se esperaba) y la
fuente de la que sale la maquinaria (tesis de C.-D. Pfeiffer, 2022).

Contexto mínimo: en teoría de conjuntos causales el operador de d'Alembert discreto `B` tiene
límite continuo `□ − R/2`. Hay un candidato de operador de cinco capas en `d=4` del que se
quería extraer el escalar de Kretschmann `C_abcd C^abcd`. Una auditoría previa lo dejó en
`AUDIT_REQUIRES_MAJOR_FIX` y dejó abierta una comprobación, `R6'`: si la cuarta raíz del
operador limpia los logaritmos de la región cercana `W1` y si el canal `y^4` donde vive `C^2`
sobrevive o se aniquila. Este documento es la respuesta a esa comprobación.

## Objetivo

Decidir si el resultado es correcto. Tres afirmaciones lo sostienen y las tres son
recomputables con lo adjunto:

**C1 — la estructura del canal.** Que el orden en `B̄` de cada canal es
`rho^{(d+2)/d − (2/d)(m+1)}` y por tanto **no depende de `l`**; que a orden `rho^{-1/2}` con
`alpha+beta = 4` sólo contribuye la diagonal `(m,k) = (3,3)`; y que `mu = (2/d)(m+1)+l−1`.
¿Es correcto el recuento? ¿Hay canales que se hayan dejado fuera (fuera de la diagonal,
`m < k`, términos de frontera de (3.43), el sector `W2` reentrando)?

**C2 — la acción del operador.** Que `Ô_* = (2/3)(H+½)(H+1)(H+3/2)(H+2)` sobre el canal
`l=0` da `Ô_*[log(s) s^{-2}] = −1/(2s²)` y `Ô_*[s^{-2}] = 0`, de modo que aniquila a la vez
el logaritmo y la dependencia del corte `a`; y que para `l >= 1` no aniquila nada. Y que
`G_1(s) = (log s + 2 log A − 1 + gamma_E)/s² + exp. pequeño`, con el coeficiente del logaritmo
igual a 1 e independiente de `A`. Recomponlo.

**C3 — el control del límite.** Que los dos operadores dan la misma contribución física
`4 sqrt6/9` al canal `(2,2)`, porque el cociente de prefactores `b_0` (4) cancela el de
coeficientes de canal (1/4). Si esto fallara, algo estaría mal normalizado en todo lo demás.

## Qué más atacar

- ¿Es correcta la clasificación de §4, que el contenido `C^2` a orden `R^2` llega a la
  diagonal `(3,3)` por exactamente tres vías `l = 0, 1, 2`? ¿Falta alguna, o sobra?
- ¿Es legítimo llamar "reparación de `C0`" al hecho de que `Ô_*[s^{-2}] = 0`? ¿O la
  dependencia del corte reentra por otro sitio (los términos `B_{kappa+1,l}` de (3.43), la
  desalineación entre las fronteras de `W1` y `W2`, el propio `A` dentro de la gamma
  incompleta)?
- El veredicto `R6_PRIME = PARTIAL`: ¿debería ser más fuerte o más débil?
- ¿Se afirma en algún punto más de lo que la cuenta sostiene? El documento intenta acotarse en
  su §5; dime si no basta.

Si encuentras un error, dilo con detalle. Un resultado "limpio" sostenido sobre un fallo de
recuento es peor que un resultado parcial.

## Resultado esperado

Prosa seca, sin preámbulo, y al final:

```
C1_ESTRUCTURA = CORRECTA | INCORRECTA | NO_CONCLUYENTE   + por qué, en tres líneas
C2_OPERADOR   = CORRECTA | INCORRECTA | NO_CONCLUYENTE   + por qué, en tres líneas
C3_CONTROL    = CORRECTA | INCORRECTA | NO_CONCLUYENTE   + por qué, en tres líneas
VEREDICTO_R6_PRIME = CONFIRMADO | CONFIRMADO_CON_CORRECCIONES | REFUTADO
DEFECTOS_ENCONTRADOS = lista, o NINGUNO
```

## Condiciones

- **Una sola ronda.** No hay réplica.
- **Cierra el encargo** emitir los cinco campos con sus razones. Si no puedes decidir algo con
  lo adjunto, `NO_CONCLUYENTE` y di exactamente qué falta; eso también cierra.
- Sesión sellada: sin herramientas, ficheros ni web. Todo lo que puede contar como fuente está
  adjunto. No cites nada que no esté adjunto; si te falta un resultado externo, dilo como
  laguna en vez de reconstruirlo de memoria.
- No reescribas el documento ni propongas redacción. Juzga.

---
