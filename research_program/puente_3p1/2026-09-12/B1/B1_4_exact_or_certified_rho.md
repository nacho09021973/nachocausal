# B1.4 — Separación numérica de `rho` para el par congelado

> **STATUS: `FROZEN_PAIR / NUMERICAL_SEPARATION / NO_SEARCH / NO_SEEDS`.**
> El par es exactamente el de B1.3 y no puede sustituirse.

## 1. Método

Para cada par radial ordenado se integra la probabilidad angular
`(1-cos(Delta_max))/2`. La cota superior usa la UB rigurosa de B1.2. La cota inferior usa una
trayectoria causal explícita de dos tramos, escogida por una malla fija de puntos de control; toda
trayectoria de esa familia es admisible, de modo que el resultado sigue siendo una cota inferior
válida aunque la malla no encuentre el supremo variacional.

Las cotas angulares para cada par son inequalities válidas punto a punto. La integración radial
usa cuadratura de Gauss–Legendre determinista de orden fijo. Se repite con dos órdenes para
reportar estabilidad numérica. El spread entre órdenes es sólo un diagnóstico de estabilidad:
no es un remainder formal de cuadratura. No hay Monte Carlo, semillas, ajuste, búsqueda de pares
ni tuning de `lambda`.

Por tanto, las bandas que siguen son bandas numéricas bajo el esquema de cuadratura utilizado,
no un enclosure formal global de `rho`.

## 2. Terminal

```text
B1.4_CORRECTED_NUMERICALLY_SEPARATED   si las bandas numéricas quedan separadas;
B1.4_CORRECTED_NUMERICALLY_INCONCLUSIVE si se solapan;
B1.4_NULL_FOR_FROZEN_PAIR              sólo si la igualdad se demuestra formalmente.
```

La separación numérica es evidencia de no-degeneración para el par congelado, pero no implica
un certificado formal global ni permite afirmar formalmente que se ha excluido un isomorfismo.
La inconclusión tampoco implica igualdad, isomorfismo ni `TV=0`.

## 3. Resultado para el par congelado

La ejecución de `verify_certified_rho_frozen_pair.py` con el kernel corregido
`q(s)=2 exp(-s/2)/s^(3/2)` da, incluyendo el margen numérico reportado por las cuadraturas de
órdenes 10 y 14,

```text
numerical_rho(lambda0) in [0.01275619, 0.01879423]
numerical_rho(lambda1) in [0.02793126, 0.04383500]

numerical separation gap = 0.00913704
TERMINAL = B1.4_CORRECTED_NUMERICALLY_SEPARATED
```

La cota inferior procede de trayectorias causales explícitas de dos tramos y la superior de la
cota Cauchy–Schwarz de B1.2. Las inequalities angulares son válidas; la integración global y su
error son numéricos. El resultado es evidencia numérica de no-degeneración de la ley del poset no
etiquetado a `n=2` para este par congelado. No demuestra reconstrucción, la identificabilidad
general de `phi` ni una separación formal global.

Los extremos congelados aparecen numéricamente separados bajo el kernel físico corregido. No se
afirma formalmente que esto descarte un isomorfismo causal-medida.

```text
FROZEN_ENDPOINT_ISOMORPHISM = NUMERICALLY_SEPARATED_ONLY
```

Este resultado se refiere sólo a los extremos congelados y conserva explícitamente:

```text
B1_FORMAL_CERTIFICATE = NOT_ESTABLISHED
```

No establece ni refuta la existencia de isomorfismos entre puntos arbitrariamente próximos de la
curva de B2.

**Artefacto de verificación:** `verification_certified_rho_frozen_pair.json`.

## 4. Continuación

El estado `B1_FORMAL_CERTIFICATE = NOT_ESTABLISHED` de §3 es el que tenía esta unidad al
cerrarse, y se conserva tal cual. Fue superado después, para el mismo par congelado y sin
recalcular `rho`, por una cadena de desigualdades con toda cuadratura reducida a dimensión 1:
véase `B1_5_analytic_separation_certificate.md` y
`verification_b1_5_analytic_separation.json` (`B1_FORMAL_CERTIFICATE = ESTABLISHED`,
`U0 = 0.01990853592 < L1 = 0.02282676120`). Las bandas numéricas de §3 quedan estrictamente
contenidas en los intervalos rigurosos de B1.5, que es la comprobación cruzada entre ambas
unidades.
