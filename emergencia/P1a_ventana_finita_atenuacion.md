# P1a — Atenuación de ventana finita: el objetivo poblacional de `fig04`

> **ESTADO: RESULTADO ANALÍTICO EXACTO · CUADRATURA DETERMINISTA · SIN DATOS
> ESTOCÁSTICOS NUEVOS EN `resultados/` · NO TOCA EL SELLO · NO CONSUME LA BANDA DE
> SEMILLAS RESERVADA.**
>
> Ejecutable: `emergencia/p1a_ventana_finita_atenuacion_d2.py`. Dos ejecuciones dan
> salida idéntica.

## 0. Qué establece y qué no

La correlación `-0.951` que imprime `viz/fig04_box_wall.py` es una **correlación
muestral**. Este documento identifica el objetivo poblacional que estima, lo calcula
**por cuadratura sin sortear un solo punto**, y da en forma cerrada el sesgo finito
que separa uno de otro.

No establece nada sobre el elemento **seleccionado** por un argmax sobre el causet
completo. Allí la ley binomial de §1 deja de aplicar y el fenómeno es de extremos
(§5): distinto mecanismo, distinta dependencia en `n`.

## 1. La ley del observable en un elemento genérico

Sea `W` la ventana `(t,r)` del experimento. Como `det g = -1`, la forma de volumen es
`dt dr` y un sprinkling condicionado a `N = n` son `n` puntos iid uniformes en `W`.

Fijado uno de ellos, `x`, cada uno de los `n-1` restantes cae en `J^+(x) ∩ W` de forma
independiente y con probabilidad

```text
P = p(x) = Vol(J^+(x) ∩ W) / Vol(W),
```

que es una cantidad **puramente geométrica**: no depende de `n`. Por tanto

```text
K = |J^+(x)|  |  x, N=n   ~   Binomial(n-1, P).
```

Es exacto, no asintótico. `P` es determinista dado `x`; la aleatoriedad de `x`
(uniforme en `W`) es la que hace de `P` y de `T = t(x)` variables aleatorias.

## 2. Proposición 1 — atenuación exacta

Con `X` uniforme en `W`, `P = p(X)`, `T = t(X)` y `K` como en §1:

```text
Var(K)     = (n-1)^2 Var(P) + (n-1) E[P(1-P)]
Cov(K,P)   = (n-1) Var(P)
Cov(K,T)   = (n-1) Cov(P,T)
```

y por tanto, con

```text
A(n) = ( 1 + E[P(1-P)] / ((n-1) Var(P)) )^(-1/2),
```

se obtiene

```text
Corr(K,P) = A(n),          Corr(K,T) = Corr(P,T) · A(n).
```

**Demostración.** `Var(K) = Var(E[K|X]) + E[Var(K|X)] = Var((n-1)P) + E[(n-1)P(1-P)]`.
Para las covarianzas, dado `X` tanto `P` como `T` son constantes, luego
`Cov(K,P) = Cov(E[K|X], P) = (n-1)Var(P)` y análogamente para `T`. Sustituyendo en la
definición de correlación y simplificando `√Var(P)` sale `A(n)`. `QED`

**Tres lecturas que conviene no perder:**

1. **Ambas correlaciones comparten exactamente el mismo factor.** `A(n)` no depende de
   qué se correlacione con `K`, solo del par `(Var(P), E[P(1-P)])`.
2. `Corr(K,P) → 1` y `Corr(K,T) → Corr(P,T)`: el límite es geométrico, no estadístico.
3. **La atenuación es `O(1/n)`** —`1 - A(n) ≈ E[P(1-P)] / (2(n-1)Var(P))`— aunque la
   fluctuación relativa condicional de `K` a `p` fijo sea `O(n^{-1/2})`. La correlación
   es un cociente de momentos segundos: el ruido entra en varianza, no en desviación
   típica.

## 3. Los objetivos, por cuadratura

`X` es uniforme en el rectángulo, luego los momentos son integrales con peso constante.
Salida del ejecutable (malla `1601×1201`; control con `801×601` coincide en `1.9e-06`):

| ventana | `E[P]` | `Var(P)` | `E[P(1-P)]` | `Corr(p,t)` |
|---|---:|---:|---:|---:|
| `fig04` `t∈[0,6] r∈[1.1,4.0]` | 0.270235 | 5.0785e-02 | 0.146423 | **−0.951387** |
| alta `t∈[0,12] r∈[1.1,4.0]` | 0.367851 | 7.1901e-02 | 0.160635 | −0.986176 |
| baja `t∈[0,3] r∈[1.1,4.0]` | 0.163794 | 2.2757e-02 | 0.114208 | −0.907415 |
| ancha `t∈[0,6] r∈[1.1,8.0]` | 0.177207 | 2.5709e-02 | 0.120096 | −0.922495 |

**El objetivo es un funcional de la ventana, no una constante universal.** Va de
`-0.907` a `-0.986` sobre razones de aspecto razonables. Eso es una virtud: convierte
el enunciado en una afirmación sobre el **diseño del experimento**, y lo hace falsable
del modo más barato posible — cambia la caja y el número debe moverse como predice la
cuadratura.

Atenuación para la ventana de `fig04`:

| `n` | `A(n)` | `1-A(n)` | `Corr(K,T)` predicho |
|---:|---:|---:|---:|
| 225 | 0.993626 | 6.37e−03 | −0.945323 |
| 900 | 0.998400 | 1.60e−03 | −0.949865 |
| 3 600 | 0.999600 | 4.00e−04 | −0.951007 |
| 14 400 | 0.999900 | 1.00e−04 | −0.951292 |

## 4. Controles

**Premisa binomial (falsable).** Si la cuadratura de `p` o la geometría discreparan,
este control falla. Para tres posiciones fijas se compara `p(x)` con `E[K]/(n-1)`
estimado sobre 300 sprinklings de `n = 400`:

| `x = (t,r)` | `p(x)` cuadratura | `E[K]/(n-1)` simulado | `\|dif\|` |
|---|---:|---:|---:|
| (1.0, 1.5) | 0.470153 | 0.472089 | 1.94e−03 |
| (3.0, 2.5) | 0.285197 | 0.285422 | 2.25e−04 |
| (5.0, 3.5) | 0.038770 | 0.038822 | 5.17e−05 |

Peor discrepancia `1.94e-03` frente a una cota holgada de `3 SE = 4.34e-03`: **PASS**.

**Convergencia de la cuadratura.** Dos mallas dan `|Δ Corr(p,t)| = 1.9e-06`.

**Lo que NO es un control.** La tabla de correlaciones muestrales frente a `n` que
motivó este documento procede de **una sola realización por `n`, con una semilla**. No
permite separar fluctuación muestral de la dependencia intra-realización —los `K_i` de
un mismo causet no son independientes—, y por eso no se usa como contraste de la
Proposición 1, sino como control cualitativo. Verificar el residuo pediría réplicas:
análisis nuevo, no abierto aquí.

Por la misma razón **no se asignan errores estándar iid a la correlación interna de un
causet**. La cuadratura elimina el problema en la raíz: el objetivo se calcula, no se
estima.

## 5. Lo que este resultado separa

| | `fig04` | selector de `emergencia` |
|---|---|---|
| elemento | genérico, `X` uniforme en `W` | elegido por argmax sobre el causet completo |
| ley de `K` | `Binomial(n-1, p(X))`, exacta | la binomial **no** aplica tras el argmax |
| efecto en `n` | `Corr(K,T) → Corr(p,T)`, constante geométrica | enriquecimiento fronterizo **creciente**: ×1.52 (`n=32`) a ×2.47 (`n=128`) |
| mecanismo | truncamiento de un observable no local por la ventana | estadística de extremos sobre el conjunto |

Los dos son manifestaciones de **ventana finita**, y ese es el enunciado defendible.
**No son el mismo obstáculo**: tienen dependencia en `n` distinta —plana uno, creciente
el otro—, y esa diferencia es empíricamente distinguible. Fundirlos, como se hizo en
una primera lectura de las figuras, borra precisamente el criterio que permite
clasificar un candidato futuro.

## 6. Techo de afirmación

No se establece:

- nada sobre el régimen del selector (§5, columna derecha);
- que el enriquecimiento fronteriza del selector crezca sin límite: los cinco valores
  de `n` medidos son evidencia monótona en el régimen estudiado, no una ley asintótica;
- ninguna afirmación sobre `d ≥ 3`: `p(x)` se calcula con la estructura de conos de
  `1+1` Schwarzschild;
- que `Corr(p,t)` tenga valor privilegiado alguno: es un funcional de la ventana (§3).

## 7. Estado de control

```text
FINITE_WINDOW_TARGET_fig04 = -0.951387 (cuadratura, malla 1601x1201)
TARGET_IS_WINDOW_FUNCTIONAL = YES (4 ventanas, -0.907 a -0.986)
ATTENUATION_IS_EXACT_IDENTITY = YES (Prop. 1, no requiere iid entre elementos)
ATTENUATION_ORDER = O(1/n)
BINOMIAL_PREMISE_CONTROL = PASS
QUADRATURE_CONVERGENCE = 1.9e-06
SAMPLING_TABLE_STATUS = CONTROL_ONLY_SINGLE_REALISATION_NOT_A_TEST
SELECTOR_REGIME = OUT_OF_SCOPE_ARGMAX_BREAKS_THE_BINOMIAL_LAW
MANUSCRIPT_HOME = docs/manuscript_limits_draft.md §5.4.1
NEW_STOCHASTIC_DATA_WRITTEN = NO
SEED_BAND_CONSUMED = NO
SEAL_TOUCHED = NO
```

## 8. Artefactos

```text
emergencia/p1a_ventana_finita_atenuacion_d2.py
```

Determinista, no escribe en `resultados/`. Reutiliza `viz/causet_core.py` (geometría y
orden) sin duplicarlo.
