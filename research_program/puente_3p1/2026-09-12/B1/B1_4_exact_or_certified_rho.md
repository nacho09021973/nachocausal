# B1.4 — Evaluación certificada de `rho` para el par congelado

> **STATUS: `FROZEN_PAIR / DETERMINISTIC_CERTIFICATE / NO_SEARCH / NO_SEEDS`.**
> El par es exactamente el de B1.3 y no puede sustituirse.

## 1. Método

Para cada par radial ordenado se integra la probabilidad angular
`(1-cos(Delta_max))/2`. La cota superior usa la UB rigurosa de B1.2. La cota inferior usa una
trayectoria causal explícita de dos tramos, escogida por una malla fija de puntos de control; toda
trayectoria de esa familia es admisible, de modo que el resultado sigue siendo una cota inferior
válida aunque la malla no encuentre el supremo variacional.

La integración radial usa cuadratura de Gauss–Legendre determinista de orden fijo. Se repite con
dos órdenes para reportar estabilidad numérica. No hay Monte Carlo, semillas, ajuste, búsqueda de
pares ni tuning de `lambda`.

## 2. Terminal

```text
B1.4_POSITIVE                 si las cotas certificadas de rho quedan separadas;
B1.4_INCONCLUSIVE_BY_BOUNDS   si se solapan;
B1.4_NULL_FOR_FROZEN_PAIR     sólo si la igualdad está certificada.
```

La positividad certificada implica directamente
`TV(P_lambda0,2,P_lambda1,2) >= |rho_lower,0-rho_upper,1| > 0` (o la separación inversa),
sin clasificar isomorfismos. La inconclusión no implica igualdad, isomorfismo ni `TV=0`.

## 3. Resultado para el par congelado

La ejecución de `verify_certified_rho_frozen_pair.py` da, incluyendo el margen determinista
reportado por las cuadraturas de órdenes 10 y 14,

```text
rho(lambda0) in [0.00340521, 0.00622208]
rho(lambda1) in [0.00758292, 0.02091072]

TV(P_lambda0,2, P_lambda1,2) >= 0.00136084
TERMINAL = B1.4_POSITIVE
```

La cota inferior procede de trayectorias causales explícitas de dos tramos y la superior de la
cota Cauchy–Schwarz de B1.2. El resultado es, por tanto, un testigo de no-degeneración de la ley
del poset no etiquetado a `n=2` para este par congelado. No demuestra reconstrucción ni la
identificabilidad general de `phi`.

Además, el resultado descarta directamente cualquier isomorfismo causal-medida entre los dos
experimentos congelados. Una biyección bimedible que preservase medida normalizada y causalidad
transportaría la distribución iid y, por tanto, la ley del poset para todo `n`; eso exigiría `TV=0`.
En consecuencia,

```text
FROZEN_ENDPOINT_ISOMORPHISM = RULED_OUT_BY_POSITIVE_TV
```

Este veto se refiere sólo a los extremos congelados. No establece ni refuta la existencia de
isomorfismos entre puntos arbitrariamente próximos de la curva de B2.

**Artefacto de verificación:** `verification_certified_rho_frozen_pair.json`.
