# Encargo: revisión ciega de un resultado negativo

---

Revisas un **no-go**: `S4W_R6PRIMEPRIME_NOGO_2026-10-10.md`. Van adjuntos los dos documentos
que lo preceden (`S4W_R6PRIME_W1_CHANNEL`, el resultado parcial que lo encargó, y la auditoría
original) y la fuente de la maquinaria (tesis de C.-D. Pfeiffer, 2022).

Contexto: en teoría de conjuntos causales se propuso un operador de cinco capas en `d=4` del
que extraer el escalar de Kretschmann `C_abcd C^abcd`. Dos rondas previas lo dejaron en
`AUDIT_REQUIRES_MAJOR_FIX` y reducieron todo a una pregunta: ¿es nulo el coeficiente del
logaritmo de la vía contaminante? Este documento dice que no, y concluye que el estimador
diverge.

**Un no-go es más fácil de equivocar que un resultado positivo, porque nadie lo contrasta con
un experimento.** Esa es la razón de este encargo.

## Objetivo

Decidir si el no-go se sostiene. Cuatro afirmaciones lo sustentan:

**N1 — la conversión de convenciones.** Que `tau = 2 l_W`, luego `l_W = sqrt(uv/2)`, y que con
eso el volumen plano de Wang coincide **idénticamente** con el `V_0 = (pi/6) u^2 v^2` de
Pfeiffer. De aquí sale `eps_2 = u^2v^2(41K+688W)/151200`. Si esta conversión está mal, todo lo
demás cae. Recompónla.

**N2 — el canal y su coeficiente.** Que el término `l=1` da, al desarrollar `(v-u)^2`, el
monomio `u^5v^5` con coeficiente `+pi rho (41K+688W)/907200`, que corresponde a la diagonal
`(m,k)=(3,3)`; y que por tanto no hay cancelación interna posible al ser un único monomio.

**N3 — el logaritmo superviviente.** Que `G_2` tiene coeficiente de log igual a 2, que
`Ô_*[G_2] = 2(15 log s + 30 log A - 61 + 15 gamma_E)/(3 s^3)` y que el coeficiente del
logaritmo que sobrevive es **10**.

**N4 — el ensamblado y la inmunidad a `F3`/`F4`.** Que `B̄[1]` contiene
`[2 sqrt6 (41K+688W)/(315 pi)] log(rho) rho^{-1/2}`, que el estimador va entonces como
`-(10/73)(41K+688W) log(rho)`, y —el punto decisivo— que **la parte invariante `K` basta**:
siendo `K` escalar, su coeficiente sobrevive a cualquier integral angular, luego no hace falta
resolver si la integral de `W` colapsa. ¿Es correcto ese argumento de inmunidad?

## Qué más atacar

- ¿Falta alguna vía a orden `R^2` que pudiera cancelar el logaritmo de `(ii')`? El documento
  afirma que no hay pareja. Las dos rondas anteriores fallaron precisamente en clasificar vías.
- El §5 sostiene que a orden `R^2` solo contribuyen `l=0` y `l=1`, porque en vacío
  `delta V = O(R^2)` y el sector `l` lleva `R^{2l}`. ¿Es correcto? ¿Y la consecuencia, que el
  `O_10` de siete capas limpiaría los dos?
- ¿Se afirma de más en algún punto? El documento se declara explícitamente **no** concluyente
  sobre el sucesor de siete capas; dime si el resto del texto respeta esa acotación.
- ¿Debería el veredicto ser más débil (`NO_CONCLUYENTE`) o más fuerte?

## Resultado esperado

Prosa seca, sin preámbulo, y al final:

```
N1_CONVENCIONES = CORRECTA | INCORRECTA | NO_CONCLUYENTE   + por qué, en tres líneas
N2_CANAL        = CORRECTA | INCORRECTA | NO_CONCLUYENTE   + por qué
N3_LOGARITMO    = CORRECTA | INCORRECTA | NO_CONCLUYENTE   + por qué
N4_INMUNIDAD    = CORRECTA | INCORRECTA | NO_CONCLUYENTE   + por qué
VEREDICTO_NOGO = CONFIRMADO | CONFIRMADO_CON_CORRECCIONES | REFUTADO
DEFECTOS_ENCONTRADOS = lista, o NINGUNO
```

## Condiciones

- **Una sola ronda.** No hay réplica.
- **Cierra el encargo** emitir los seis campos con sus razones. `NO_CONCLUYENTE` con la laguna
  dicha también cierra.
- Sesión sellada: sin herramientas, ficheros ni web. No cites nada que no esté adjunto.
- No reescribas el documento. Juzga.

---
