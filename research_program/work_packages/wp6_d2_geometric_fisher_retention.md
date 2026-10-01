# WP6 — Retención Fisher del poset no etiquetado para tangentes conformes rank-one simétricos

```text
ESTADO: S2_GEOMETRIC_FISHER_RETENTION = PROVED_BY_ASSEMBLY
ALCANCE: d=2, diamante de Minkowski 1+1 como PUNTO BASE,
         perturbado conformemente por g_epsilon.
         Sector rank-one simetrico. No es reconstruccion. No es horizonte.
NATURALEZA: ensamblaje deductivo. Cero matematica nueva, cero semillas,
            cero simulacion, sello intacto.
GOBERNANZA: docs/program_s2_authorization_2026-08-28.md
            docs/program_reopening_note_2026-08-28_R4.md
ANCLA_S1: 2219f21dea2cbd82ba9d959a6d55e1cf87a0bcf6
FECHA: 2026-08-28
SELLO: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4 intacto
SEMILLAS: banda virgen [2,000,000–2,999,999] sin quemar
STOP_AFTER_S2 = SI
S3_NOT_OPENED
S4_NOT_OPENED
NO_HORIZON_CLAIM
NO_BENCHMARK_TRANSFER_CLAIM
NO_PRIORITY_CLAIM
NOVELTY_CERTIFIED = NO
MINKOWSKI_DIAMOND_PERTURBATIVE
```

Este documento **no demuestra nada que no esté ya demostrado**. Eleva a un
teorema autónomo la composición

```text
S1 (3.5), Teorema 6, (5.3)
  + Teorema 7
  + Teorema 5
  + Lema 11.1, Lema 11.2
  = (11.6)
```

registrada como corolario condicional en
`wp6_d2_geometric_tangent_classification.md` §11.5. S2 no busca un límite
nuevo: nombra el que ya se sigue.

## 0. En una frase

En una clase explícita de deformaciones conformes simétricas rank-one de un
diamante `1+1`, el poset no etiquetado retiene asintóticamente toda la
información Fisher relativa disponible en la permutación de rangos.

Ese es el techo de la hoja de ruta §3.2. Nada por encima.

## 1. Experimento estadístico

**Punto base.** Diamante causal de Minkowski en `1+1`, reducido a
`D=[0,1]^2` con el orden producto y medida de volumen normalizada
`mu_0=du dv`. El punto `epsilon=0` es plano. Las perturbaciones con
componente de interacción no tienen por qué serlo.

**Familia.** Para `psi in C(D;R)` y `epsilon` real pequeño,

\[
g_\varepsilon
=\frac{e^{2\varepsilon\psi}}{Z(\varepsilon)}\,g_0,
\qquad
Z(\varepsilon)=\int_D e^{2\varepsilon\psi}\,d\mu_0.
\]

Un sprinkling de Poisson condicionado a `N` puntos es `N` iid de
`mu_epsilon = q_epsilon\,du dv`, `q_epsilon=e^{2 epsilon psi}/Z(epsilon)>0`
para todo `epsilon`.

**Antes del cociente.** `Pi_N` es la permutación de rangos del realizador
`(U,V)`: depende de los dos órdenes lineales. No es order-only.

**Después del cociente.** `[P_{Pi_N}]` es la clase de isomorfismo del poset
orientado 2-dimensional inducido. Ése es el observable order-only.

**Punto nulo de Fisher.** `epsilon=0`. El score es
`S_{N,psi}(pi)=partial_epsilon log p_epsilon(pi)|_0`.

**Clase geométrica.** `lambda != 0` y `f in C[0,1]` con
`int_0^1 f=0` y `int_0^1 f^2>0`, y

\[
\psi(u,v)=\alpha(u)+\beta(v)+\lambda f(u)f(v),
\qquad
\alpha,\beta\in C[0,1].
\]

`int f=0` es solubilidad de `P psi = lambda f tensor f` (Lema 9.2 / Corolario
9.3 de S1), no una normalización cosmética. `lambda != 0` excluye el caso
degenerado `0/0` del cociente Fisher (Lema 11.1 de S1).

## 2. Teorema

**Teorema 8 (`GEOMETRIC_TO_UNLABELED_POSET_FISHER_RETENTION`).**
En el experimento de §1, con la clase geométrica de §1,

\[
\frac{I_N^{[P]}(g_\varepsilon)}{I_N^\Pi(g_\varepsilon)}
\longrightarrow 1
\qquad(N\to\infty,\ N\ge N_A),
\]

y más precisamente, con las constantes `C_A,N_A` de (7.5) del WP6 modular,
no inventadas aquí,

\[
1-\frac{I_N^{[P]}}{I_N^\Pi}
\le
\left(
\frac{\sqrt{240C_A}\,\|f\|_\infty^4}{4\bigl(\int_0^1 f^2\bigr)^2}+o(1)
\right)N^{-1/2}.
\]

La cota no depende de `lambda`, ni de `alpha`, ni de `beta`. El canal
Fisher del miembro izquierdo es el order-only `Pi_N -> [P_{Pi_N}]`.

Esto es (11.6) de S1, restated as autonomous theorem. No hay tasa mejor
que la del Teorema 5.

## 3. Prueba modular — cuatro pasos, cero matemática nueva

No se re-prueba el cuarto momento ni la fibra típica. Se citan con
hipótesis verificadas una por una (hoja de ruta §3.3).

### 3.1 Geometría → tangente de cópula

Por S1 (3.5),

\[
h_\psi=2\,\mathcal P\psi,
\qquad
\mathcal P\psi=\psi-\psi_U-\psi_V+\bar\psi.
\]

Por el Teorema 6 de S1, para `int f=0` son equivalentes
`P psi = lambda f tensor f`, `h_psi = 2 lambda f tensor f`, y
`psi = alpha + beta + lambda f tensor f`. Convención B (G2): `lambda`
parametriza `P psi`, no el tangente de cópula.

Fuente: `wp6_d2_geometric_tangent_classification.md` (3.5), Teorema 6;
`docs/hoja_de_ruta_septiembre_2026.md` §2.2 (G2).

### 3.2 Tangente de cópula → score de rangos simétrico

Por S1 (5.3) con `kappa = 2 lambda`,

\[
S_{N,\psi}(\pi)
=2\lambda\sum_{i=1}^N a_{i,N}a_{\pi(i),N},
\qquad
a_{i,N}=\mathbb E[f(U_{(i)})].
\]

`Pi_N` depende del realizador; la factorización usa la independencia
rango ⊥ estadísticos de orden bajo el nulo uniforme.

Fuente: S1 (5.3) y §5.2.

### 3.3 Score simétrico → teorema combinatorio ya probado

El array `a_{i,N}` es triangular y determinista. El Teorema 7 de S1
afirma las tres hipótesis del Teorema 5:

```text
(H1)  sup_N max_i |a_{i,N}| <= ||f||_inf < infty
(H2)  sum_i a_{i,N} = 0 exactamente, para todo N >= 1
(H3)  (1/N) sum_i a_{i,N}^2  ->  int f^2 = c > 0
```

El Teorema 5 del WP6 modular, para la permutación uniforme y el canal
exacto `Pi_N -> [P]`, concluye `q_N := 1 - L_N/I_N^Pi -> 1` con tasa
`O(N^{-1/2})` para `N >= N_A`. No se reabre su prueba. Hipótesis, una a
una:

- nulo uniforme: `mu_0 = du dv`, `N` iid, `epsilon=0`;
- canal exacto `Pi_N -> [P_{Pi_N}]`: el del Teorema 5;
- array determinista centrado acotado de energía no degenerada: Teorema 7.

Fuente: S1 Teorema 7; `wp6_d2_modular_fiber_score.md` Teorema 5, (7.5),
(7.7). Cuarto momento y fibra típica: ya probados allí; no se tocan.

### 3.4 Conclusión Fisher en el canal order-only

Lema 11.1 de S1: `q_N` es invariante bajo `S -> lambda S` con
`lambda != 0`. Lema 11.2 de S1: `I_N^{[P]} = I_N^Pi - L_N`, luego
`I_N^{[P]}/I_N^Pi = q_N`. Sustituir `M_*` por `||f||_inf` es una
debilitación válida porque la cota del Teorema 5 crece en `M_*` y
`M_* <= ||f||_inf` por (H1). Se obtiene el Teorema 8.

Fuente: S1 §11.5, (11.6).

## 4. Claim ceiling — lo que este teorema no afirma

```text
NO_METRIC_RECONSTRUCTION
NO_SUFFICIENCY_VS_FULL_CONTINUOUS_COORDINATES
NO_UNIVERSALITY_OVER_GEOMETRIC_TANGENTS
NO_HORIZON_CLAIM
NO_2PLUS1
NO_3PLUS1
NO_BENCHMARK_TRANSFER_CLAIM
NO_RATE_IMPROVEMENT
NO_ASYMMETRIC_SECTOR
NO_FINITE_RANK
NO_PRIORITY_CLAIM
NOVELTY_CERTIFIED = NO
```

En particular:

- no se recupera la métrica ni las coordenadas continuas completas;
- no vale para un tangente geométrico genérico, sólo para la clase §1;
- no es un resultado sobre horizontes, Schwarzschild, ni el benchmark
  histórico `(t*, r)`;
- `BENCHMARK_COORDINATE_BRIDGE` permanece
  `OPEN_NOT_REQUIRED_FOR_S2` (R4 §7bis);
- el núcleo algebraico de `P` es ANOVA / Hoeffding, ya registrado en S1.

El experimento es local sobre un diamante de Minkowski `1+1` **como punto
base**, perturbado conformemente. El punto `epsilon=0` es plano;
`P psi != 0` no tiene por qué serlo.

## 5. S2 cerrado. Frontera fuerte.

```text
S2_GEOMETRIC_FISHER_RETENTION = PROVED_BY_ASSEMBLY
STOP_AFTER_S2 = SI
S3_NOT_OPENED
S4_NOT_OPENED
DECISION_S3: NOT_AUTHORIZED
DECISION_S4: NOT_AUTHORIZED
```

S2 no autoriza S3 (auditoría de prioridad), S4, finite-rank, el sector
asimétrico, ni `2+1`/`3+1`, ni por existir este teorema ni por existir
esas fases en la hoja de ruta. Tras este cierre se vuelve a decidir desde
cero qué parte, si alguna, sirve al objetivo físico de nachocausal.

T20 no forma parte de S2.
