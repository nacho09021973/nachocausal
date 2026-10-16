# M1 — Comparación métrica y cota superior \(n^{-1/2}\) en cajas EF fijas de cualquier dimensión

```text
ESTADO: LEMMA_M1_PROVED; THEOREM_M2_CONDITIONAL_ON_M3; PROPOSITION_M3_PROOF_SKETCH
FECHA: 2026-10-16
GOBERNANZA: el PI abrió el frente 3+1D para exploración el 2026-10-16 (ver README)
NATURALEZA: prueba analítica; comprobación numérica en dev/ (banda de exploración 2+1)
METRIC_COMPARISON_MONOTONICITY = PROVED (cualquier dimensión, coordenadas EF entrantes)
ORDER_ONLY_UPPER_RATE_3P1 = N_POW_MINUS_HALF_CONDITIONAL_ON_M3
STRICT_DERIVATIVE_BOUND_3P1 (M3) = PROOF_SKETCH (falta rigor)
ORDER_ONLY_LOWER_RATE_3P1 = OPEN
NO_HORIZON_OBJECT_CLAIM
REVIEW = NONE_YET
```

## 0. Procedencia

Escrito por Claude (Opus 5.5) el 2026-10-16. Generaliza el Lema G de
`research_program/work_packages/wp6_uniform_n_horizon_quotient.md` §9 (manuscrito,
Lema 3.14). Allí la monotonía se probó caso por caso en 1+1D; aquí se obtiene por
comparación de métricas, y el resultado de 1+1D sirve como comprobación por otra
vía. No ha tenido revisión de otra familia ni lectura humana.

## 1. Lema M1 (los conos se estrechan al crecer la masa)

En coordenadas Eddington–Finkelstein entrantes \((v,r,\Omega)\) de Schwarzschild de
dimensión \(d+1\) (\(d=1,2,3\)), con \(r>0\),

\[
g_M=-(1-\tfrac{2M}{r})\,dv^2+2\,dv\,dr+r^2\,d\Omega_{d-1}^2 .
\]

Para todo vector \(X=(\dot v,\dot r,\dot\Omega)\) y \(M'>M\),

\[
g_{M'}(X,X)-g_M(X,X)=\frac{2(M'-M)}{r}\,\dot v^2\ \ge 0 .
\]

Además, \(-\partial_r\) es nulo y orientado al futuro para todo \(M\), y
\(g_M(X,-\partial_r)=-\dot v\). Por tanto un vector causal está orientado al futuro si y
solo si \(\dot v\ge0\), con una condición que no depende de \(M\). En consecuencia, toda
curva causal futura para \(g_{M'}\) lo es también para \(g_M\), y a coordenadas fijas

\[
J^+_{M'}(x)\subseteq J^+_M(x)\qquad(M'\ge M).
\]

**Corolario.** Para cada par fijo de puntos, "estar relacionados" es no creciente en
\(M\). En una caja de coordenadas fija \(B\), el elemento de volumen
\(\sqrt{-g}=r^{d-1}\times(\text{factor angular})\) no depende de \(M\). Por tanto la ley del
sprinkling condicionado a \(N=n\) no depende de \(M\), y la probabilidad \(p(M)\) de
que dos puntos estén relacionados es no creciente.

*Prueba.* Es la identidad algebraica de arriba. La relación del causet es la causalidad
ambiente, la misma convención de `nachocausal/generator.py`: cualquier curva en
\(r>0\). \(\square\)

En 1+1D, esto da de nuevo la parte de monotonía del Lema G de wp6 (los cuatro
casos y los cruces del horizonte), sin hacer casos.

## 2. Teorema M2 (cota superior basada solo en el orden, condicional)

Sea \(B\) una caja de coordenadas EF fija, compacta, en \(r>0\), y \(K\) un intervalo
compacto de masas. Sea \(U_n\) la fracción de pares relacionados del causet con
\(N=n\), y supóngase

**(M3)** \(p\in C^1(K)\) y \(m:=\min_K|p'|>0\).

Entonces \(\widehat M=p^{-1}(\mathrm{clip}_{p(K)}U_n)\), que solo usa el número de relaciones
del poset sin etiquetas, cumple, para \(n\ge2\),

\[
\sup_{M\in K}E_M|\widehat M-M|\le\frac{2\sup_K\sqrt{p(1-p)}}{m\sqrt n}.
\]

*Prueba.* Es la misma que la de la Proposición F de wp6. Condicionado a \(N=n\), los
puntos son i.i.d. (manuscrito, Lema 2.1). \(U_n\) es un U-estadístico de núcleo en
\(\{0,1\}\), así que \(\operatorname{Var}U_n\le4p(1-p)/n\). Por (M3), \(p^{-1}\) es
\(1/m\)-lipschitziana. \(\square\)

## 3. Proposición M3 (bosquejo): \(\min_K|p'|>0\) en 3+1D

**Idea.** Por simetría esférica, la relación entre dos puntos depende solo de
\((v_1,r_1,v_2,r_2,\alpha)\), donde \(\alpha\) es su separación angular. Rotando el gran
círculo que los contiene hasta el ecuador, coincide con la relación de 2+1D con
\(\Delta\phi=\alpha\) (Lema E1, `2026-10-12/E1_equatorial_restriction_lemma.md`). Con
\(\alpha=0\), coincide con la relación radial de 1+1D. Fijados \((r_1,r_2,\alpha)\), la
relación equivale a \(\Delta v\ge\Delta v^*_M(r_1,r_2,\alpha)\), donde el umbral lo alcanza
una geodésica nula. Por M1, \(\Delta v^*\) es no decreciente en \(M\). En \(\alpha=0\), con
ambos puntos fuera y \(r_2>r_1\), se tiene \(\partial_M\Delta v^*=\gamma(r_2)-\gamma(r_1)>0\),
uniformemente sobre compactos (wp6 §9).

**Paso pendiente de rigor.** Hay que probar que \(\partial_M\Delta v^*\) es continuo en
\(\alpha\) cerca de 0 en el exterior. Las geodésicas nulas casi radiales sin puntos
conjugados dependen de forma suave de los extremos y del parámetro; es teoría estándar
de EDO, pero no está escrita. Con esa continuidad, \(\partial_M\Delta v^*\ge c/2\) para
\(\alpha\le\alpha_0\) en un conjunto de medida positiva. Como la densidad de \(\Delta v\) en
el umbral está acotada inferiormente, el argumento de Fatou de wp6 §9 da
\(-p'(M)\ge c'>0\), uniformemente en \(K\).

## 4. Comprobación numérica

`dev/explore_metric_comparison_2p1.py` (criterios fijados antes de ejecutar). Caja
\(t^*\in[0,4]\), \(r\in[0.15,1.3]\), \(\phi\in S^1\), densidad \(\propto r\). Usa la relación
auditada de `dev/gen2p1_efbox.py` con reescalado de masa: la relación es invariante
por un factor conforme constante. Veredicto **MONOTONE_2P1_CONSISTENT**:
- M0: los pares a igual ángulo coinciden con la forma cerrada de 1+1D (0 discrepancias
  en 78 910 pares).
- M1: 10 semillas de 500 puntos y 7 valores de \(2M\in[0.40,0.70]\); ningún par pasa de
  no relacionado a relacionado. Solo 6 pares quedaron numéricamente cerca de la
  frontera del cono, y ninguno dio violación.
- M2: \(p\) baja de 0.295 a 0.172; en cada paso, \(|\Delta p|/\mathrm{se}\) está entre 70 y 90.

Es 2+1D, que por E1 es el corte ecuatorial exacto de 3+1D. Una comprobación en
3+1D completo puede usar la misma relación con \(\Delta\phi=\alpha\), la separación
angular en \(S^2\).

## 5. Qué falta para el resultado en 3+1D

1. **M3 con rigor.** Continuidad de \(\partial_M\Delta v^*\) en \(\alpha\) y una cota uniforme
   en \(K\).
2. **Comprobación en 3+1D completo** de \(p(M)\) monótona, con la relación de 2+1D
   aplicada a \(\alpha\).
3. **Cota inferior en 3+1D** (abierta). El cociente de wp6 usaba que el orden es un
   orden producto, y eso no vale aquí. Sin la cota inferior, M2 da la tasa superior
   \(n^{-1/2}\), pero no la minimax.
4. **Revisión ciega** de M1–M3 por otra familia, y lectura del PI.
