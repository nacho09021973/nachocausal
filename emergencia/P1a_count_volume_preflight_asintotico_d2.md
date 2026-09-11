# `NC-1` — preflight de la cota Beta para el canal normalizado `sigma(M)`

> **ESTADO: PREFLIGHT MATEMÁTICO EJECUTADO · SIN DATOS, SEMILLAS, CÓDIGO NI
> ARTEFACTOS NUMÉRICOS NUEVOS · IMPLICACIÓN SUFICIENTE PROBADA · SUS HIPÓTESIS
> ASINTÓTICAS SIGUEN ABIERTAS.**

Autorización firmada:
`docs/program_reopening_note_2026-08-17_nc1_asymptotic_conditions.md`.

## 1. Pregunta y dominio

Para `h in {PAST,FUTURE}`, sea

\[
D_h=\{n\ge 6:\Pr_n(S)>0\}.
\]

Para `n in D_h`, todas las esperanzas y varianzas siguientes están condicionadas
a `(n,h,S)`. Definimos

\[
A_n^h=\mathbb E[\operatorname{Var}(\ell\mid M,n,h,S)\mid n,h,S],
\qquad
V_n^h=\operatorname{Var}(\ell\mid n,h,S),
\qquad
T_n^h=\frac{A_n^h}{V_n^h}.
\]

La ronda 4 de `NC-0` probó la positividad puntual de `V_n^h` en `D_h`, no que
`D_h` contenga una cola completa ni una cota uniforme para `V_n^h`.

El objetivo primario permanece

\[
\liminf_{n\to\infty}T_n^h>0
\quad\text{para cada lado }h.
\]

## 2. Ingrediente estructural ya demostrado

Para cada `m` factible, defínase

\[
b_n(m)=\min_{(k,l)\in F_{\rm relax}(m,n)}
\left\{
\frac{kl}{(n+1)^2}
-
\bigl(\mathbb E\sqrt{X_k}\,\mathbb E\sqrt{Y_l}\bigr)^2
\right\},
\]

donde

```text
X_k ~ Beta(k,n+1-k),
Y_l ~ Beta(l,n+1-l),
F_relax(m,n) = {(k,l): k,l>=m-1, k+l<=n+m-2, 2<=k,l<=n-1}.
```

El Teorema CV-4.1 de
`emergencia/P1a_count_volume_cota_resolucion_d2.md` demuestra, sin conocer la ley
completa de selección `w`, que

\[
\operatorname{Var}(\ell\mid M=m,n,h,S)\ge b_n(m).
\]

Tomando esperanza respecto de la ley seleccionada de `M`, se obtiene el corolario
poblacional

\[
A_n^h
\ge
L_n^h
:=\mathbb E[b_n(M)\mid n,h,S],
\]

y por tanto

\[
T_n^h\ge \frac{L_n^h}{V_n^h}.
\tag{NC1.1}
\]

Este paso es deductivo: usa una cota puntual en `m` y la monotonía de la
esperanza. No identifica `w` ni afirma una tasa.

## 3. Condición suficiente agregada

### Condición `C_h(a,p,c,C)`

Existen `n_0`, constantes `p,c,C>0`, una escala determinista `a_n>0` y conjuntos
deterministas de enteros `I_n` tales que, para todo `n>=n_0`:

1. **existencia eventual:** `n in D_h`, es decir, `Pr_n(S)>0`;
2. **masa seleccionada:**
   \[
   \Pr(M\in I_n\mid n,h,S)\ge p;
   \]
3. **ruido Beta en la ventana:**
   \[
   \inf_{m\in I_n} b_n(m)\ge c\,a_n^2;
   \]
4. **escala de variabilidad total:**
   \[
   \operatorname{Var}(\ell\mid n,h,S)\le C\,a_n^2.
   \]

La condición no menciona `T_n^h`, `rho_max` ni `eta`. Se expresa mediante la ley
condicionada de `(ell,M)`, la función geométrica explícita `b_n` y una escala
externa. No exige recuperar la ley completa
`w(s|m,n,h,S)`: basta una cota de masa para el *pushforward* `M`.

### Proposición `NC1-P`

Si `C_h(a,p,c,C)` vale, entonces

\[
\liminf_{n\to\infty}T_n^h\ge \frac{pc}{C}>0.
\]

**Demostración.** Para cada `n>=n_0`,

\[
L_n^h
=\mathbb E[b_n(M)\mid n,h,S]
\ge
\mathbb E[b_n(M)\mathbf 1_{\{M\in I_n\}}\mid n,h,S]
\ge
pca_n^2.
\]

Por (NC1.1) y la cota `V_n^h<=Ca_n^2`, se sigue

\[
T_n^h\ge \frac{pca_n^2}{Ca_n^2}=\frac{pc}{C}.
\]

Tomar `liminf` prueba la afirmación. `QED`

### Forma agregada equivalente para el ataque

La ventana es una forma interpretable, pero no necesaria. También basta demostrar
directamente, para alguna escala `a_n`,

\[
\mathbb E[b_n(M)\mid n,h,S]\ge c a_n^2,
\qquad
\operatorname{Var}(\ell\mid n,h,S)\le C a_n^2
\]

en una cola completa. Esta versión deja claro que solo se requieren consecuencias
agregadas de la selección.

## 4. Por qué la condición no decide el teorema por definición

- **No es circular.** Sus cuatro cláusulas no contienen el cociente objetivo ni la
  correlación máxima.
- **Es refutable.** Falla si `S` deja de tener probabilidad positiva en una
  subsucesión; si la masa de `M` escapa de toda ventana con cota Beta a escala
  `a_n^2`; o si la varianza total domina esa escala.
- **Es satisfacible como contrato probabilístico.** Cualquier cola de leyes
  condicionadas que coloque masa al menos `p` en una ventana con
  `b_n(m)>=ca_n^2` y tenga varianza total `<=Ca_n^2` la satisface. El preflight no
  afirma que la ley inducida por `MIN_COVERAGE_LEX` pertenezca a esa clase: probar
  precisamente eso es la obligación posterior.
- **Tiene ancla finita.** Para un estrato finito, el funcional
  \[
  R_{b,n}^{h,\mathrm{emp}}
  =\frac{\mathbb E_{\rm emp}[b_n(M)]}
  {\operatorname{Var}_{\rm emp}(\ell)}
  \]
  se calcula sobre los artefactos sellados ya existentes. El verificador auditado
  lo reporta como `B_n/Var` entre `0.2654` y `0.3087` para los seis estratos de
  `n in {64,96,128}`. Estos valores no prueban uniformidad ni eligen una ventana.

La satisfacibilidad anterior es lógica dentro del contrato de leyes condicionadas;
la **realizabilidad por el selector concreto a lo largo de una cola** sigue abierta
y está incluida explícitamente en las obligaciones de §5. No se usa una
construcción abstracta como sustituto de esa prueba.

## 5. Tres obligaciones analíticas separadas

### `NC1-O1` — existencia de la cola condicionada

Probar que para cada lado existe `n_0(h)` tal que

\[
\Pr_n(S)>0\quad\text{para todo }n\ge n_0(h).
\]

La positividad puntual del denominador demostrada en `NC-0` solo opera después de
condicionar; no prueba esta afirmación.

### `NC1-O2` — masa de `M` donde la cota Beta conserva escala

Encontrar `I_n`, `p>0` y una escala `a_n` tales que

\[
\Pr(M\in I_n\mid n,h,S)\ge p,
\qquad
\inf_{m\in I_n}b_n(m)\gtrsim a_n^2.
\]

Esto requiere controlar solo el marginal seleccionado de `M`, no la distribución
completa de formas `w`. Una prueba sobre `w` sería suficiente, pero es una ruta más
fuerte de lo necesario.

### `NC1-O3` — escala superior de la varianza total

Probar

\[
\operatorname{Var}(\ell\mid n,h,S)\lesssim a_n^2
\]

con la misma escala de `NC1-O2`. Una tasa del numerador sin este control no decide
el cociente.

Las tres obligaciones son independientes en el sentido operativo: resolver dos no
permite omitir la tercera.

## 6. Inventario de lo que existe y lo que falta

```text
BETA_POINTWISE_LOWER_BOUND = PROVED
POPULATION_AVERAGING_STEP = PROVED
DENOMINATOR_POINTWISE_POSITIVITY_ON_D_H = PROVED
SEALED_FINITE_ANCHOR = N_64_96_128_ONLY
SEALED_B_N_OVER_VAR_RANGE = 0.2654_TO_0.3087
EVENTUAL_CONDITIONAL_LAW = OPEN
SELECTED_M_MASS_CONTROL = OPEN
TOTAL_VARIANCE_ASYMPTOTIC_SCALE = OPEN
FULL_W_REQUIRED = NO_ONLY_AGGREGATE_CONSEQUENCES_NEEDED
COMPACTNESS_ARGUMENT_IN_REPOSITORY = NONE
CONVEXITY_ARGUMENT_IN_REPOSITORY = NONE
LIMINF_T_N_POSITIVE = NOT_PROVED
```

No existe en el repositorio una cota que cierre `NC1-O1`, `NC1-O2` o `NC1-O3`.
Los tres tamaños sellados son compatibles con la proposición, pero no prueban
ninguna de sus hipótesis uniformes.

## 7. Terminal

La desigualdad estructural es válida, la condición suficiente no es una
reformulación del cociente y sus tres obligaciones quedan separadas con un ancla
finita refutable. El terminal del preflight es:

```text
NC1_TERMINAL = NC1_READY_FOR_ANALYTIC_ATTACK
NC1_TARGET = PRIMARY_LIMINF
NC1_SUFFICIENT_IMPLICATION = PROVED
NC1_CONDITIONS_HOLD_IN_MODEL = OPEN
NC1_ASYMPTOTIC_THEOREM = NOT_PROVED
NC1_NEW_DATA = NO
NC1_NEW_CODE = NO
NC1_ANALYTIC_ATTACK_AUTHORISED = NO
```
