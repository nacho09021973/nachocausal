# OP-1.1 — Target esferico y clausura dual en Schwarzschild 3+1D

**Estado:** `THEORY_DRAFT / NO_IMPLEMENTATION / NO_RECOVERY_RESULT`

**Dependencia satisfecha:** `PHASE_0_AUDIT_READY` por
`docs/auditor/auditor_report_013_op01-survival-matrix.md` y
`docs/auditor/auditor_report_014_op02-claim-grammar.md`.

**Revisiones autorizadas:**
`docs/comite/comite_decision_027_phase1-theory-package-first-review.md` §8-§11 y
`docs/comite/comite_decision_028_phase1-theory-package-second-review.md` §8-§11 y
`docs/comite/comite_decision_029_phase1-theory-package-third-review.md` §8-§11 y
`docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md` §8-§11;
sign-off Nacho / PI, 2026-07-15.

## 1. Alcance

Este documento define una familia continua provisional, su involucion temporal, el target fisico
y el contrato de scoring. No define todavia un reconstructor de horizonte ni autoriza simulacion.
El target es valido solo dentro de Schwarzschild maximal, esfericamente simetrico, con patch y
truncaciones declarados. No identifica el horizonte de eventos de una continuacion arbitraria.

## 2. Familia geometrica

Usamos coordenadas de Kruskal adimensionales `(U,V,omega)`, `omega in S^2`, con convencion

```text
-U V = (r/(2M)-1) exp(r/(2M)),
ds^2 = -(32 M^3/r) exp(-r/(2M)) dU dV + r^2 dOmega_2^2.
```

`[UNVERIFIED_EXACT_KRUSKAL_NORMALIZATION_LOCAL_SNAPSHOT]` El coeficiente `32 M^3/r` se mantiene
como convencion declarada del elemento de linea. El snapshot local imprime un factor `16 M^3/r`
en una presentacion bidimensional y no declara literalmente la convencion de producto cruzado que
resolveria el factor dos. Ningun teorema de este paquete usa la eleccion entre el coeficiente
combinado `32` y el componente simetrico `16`, salvo como normalizacion positiva de la misma
metrica declarada.

Sea el vector de forma de patch

```text
lambda = (v0, v1, u_out, u_in, epsilon_s),
0 < v0 < v1,
u_out > 0,
u_in > 0,
u_in v1 <= 1-epsilon_s,
0 < epsilon_s < 1.
```

El patch BH es

```text
K^+_{M,lambda} = {
  (U,V,omega):
  V in [v0,v1],
  U in [-u_out,u_in],
  omega in S^2
}.
```

La ultima desigualdad mantiene el borde interior separado de `UV=1`, la singularidad. Los limites
finitos en `U,V` dan truncacion radial y temporal; `S^2` completo significa que no hay truncacion
angular. Esta eleccion es deliberada: las esferas de simetria cerradas caben enteras en el patch.

Definimos

```text
D(U,V,omega) = (-V,-U,omega),
K^-_{M,lambda} = D(K^+_{M,lambda}).
```

`D` conserva `UV`, `r` y la metrica, invierte la orientacion temporal y manda `I union II` a
`I union IV`. Cada componente del borde de `K^+` tiene una imagen declarada en `K^-`; en
particular, el corte `U=0` de `H^+` se manda al corte `V=0` de `H^-`.

Cada modelo se tipa como la tupla

```text
g^sigma_{M,lambda} = (K^sigma_{M,lambda}, metric_M, T^sigma, mu_M, prec^sigma),
```

donde `T^sigma` es la orientacion temporal, `mu_M=|dVol_{metric_M}|` es la medida positiva de
volumen y `prec^sigma` es la causalidad ambiente de Schwarzschild maximal restringida a pares de
puntos del patch. Una curva que establece `x prec y` no esta obligada a permanecer dentro de `K`:
el objeto observado es el suborden inducido por el espaciotiempo maximal. Elegir causalidad interna
al patch definiria otro experimento y activa `FAILED_DATA_CONTRACT`.

La familia cerrada es

```text
G_3p1_pm(lambda, I_M)
  = {g^+_{M,lambda}, g^-_{M,lambda}: M in I_M},
K^- = D(K^+),
metric^- = D_* metric^+,
T^- = -D_*T^+,
mu^- = D_# mu^+,
x prec^+ y iff D(y) prec^- D(x),
0 < M_min <= M <= M_max < infinity.
```

La notacion `D_*` de las lineas de componentes no denota por si sola el modelo dual: el signo de
`T` y la equivalencia puntual de `prec` son parte indispensable de la definicion. La clausura es
exacta por construccion: `D^2=id` y `D(G_3p1_pm)=G_3p1_pm`. `D` es una isometria que invierte `T`,
preserva la medida positiva `mu` y revierte la 4-forma orientada. Literalmente,

```text
D_# mu_{g+} = mu_{g-},
D^* dVol_oriented = -dVol_oriented.
```

## 3. Orientacion temporal y direccion exterior

Son datos distintos.

1. La orientacion futura de `g^+` es la de Kruskal BH; la de `g^-` es su pullback por `D` con
   signo temporal invertido.
2. La direccion nula `out` se fija en la region I como la familia cuya derivada de radio areal es
   positiva. Se continua suavemente dentro de cada sector.
3. `D` transporta la convencion exterior, pero invierte futuro. No se permite reconstruir una de
   estas elecciones a partir de la otra.

En una esfera de simetria de radio areal `r`, para cualquier normal nula futura `k` reescalada por
un factor positivo,

```text
theta_k = (2/r) k(r).
```

Por tanto, el signo de cada expansion es independiente de la normalizacion positiva de `k`.

## 4. Target continuo

Definimos el escalar de localizacion, solo para scoring geometrico,

```text
h_M(x) = r(x)/(2M)-1,
H(g) = {x in K_g: h_M(x)=0}.
```

Dentro de esta familia, `H(g)` coincide con la frontera puntual entre esferas no atrapadas y
atrapadas/anti-atrapadas. La etiqueta de lado es

```text
y_g(x) = sign(h_M(x)) in {-1,+1},  h_M(x) != 0.
```

El campo fisico puntual de trapping es

```text
c_g(x) = -1  si ambas expansiones nulas futuras son negativas,
c_g(x) = +1  si ambas son positivas,
c_g(x) =  0  en exterior o sobre una esfera marginal.
```

Separadamente, el caracter sectorial escalar es

```text
Chi(g^+_{M,lambda}) = -1,
Chi(g^-_{M,lambda}) = +1.
```

`Chi` etiqueta el miembro BH/WH de la familia; no es el valor del campo en cada elemento. En el
sector BH, `c=-1` en II; en el sector WH, `c=+1` en IV. Bajo `D`,

```text
h_{Dg}(Dx)   = h_g(x),
y_{Dg}(Dx)   = y_g(x),
c_{Dg}(Dx)   = -c_g(x),
Chi(Dg)      = -Chi(g).
```

Esto separa localizacion de caracter sin apelar a un horizonte aparente dependiente de foliacion.
La igualdad con `r=2M` esta condicionada a la familia Schwarzschild; no se exporta a geometria
dinamica o no esferica.

## 5. Canal observado y ley dual

Se congelan dos experimentos distintos:

```text
fixed_n:
  X_1,...,X_n iid de mu_g / mu_g(K_g);
  observar la clase de isomorfismo orientada [Ord_g(X)].

order+number:
  X ~ PPP(rho mu_g), con rho conocida;
  observar ([Ord_g(X)], N).
```

Para cada representante concreto `P=(S(P),prec_P)`, el dual se define sobre el mismo portador:

```text
P^op = (S(P),prec_P^op),
x prec_P^op y iff y prec_P x,
iota_P = id_{S(P)},
iota_{P^op} o iota_P = id_{S(P)}.
```

La familia `iota` es natural bajo relabeling: para todo isomorfismo
`sigma:S(P)->S(Q)`, `iota_Q o sigma = sigma o iota_P`. Esta identidad combinatoria no usa
etiquetas de embedding ni una correspondencia entre sprinklings distintos. En clases no
etiquetadas, la dualizacion es `d([P])=[P^op]`; las salidas elemento a elemento se definen sobre
representantes y deben respetar esa naturalidad. Como `D` preserva `mu`, invierte `T` y transporta
la causalidad ambiente al orden opuesto,

```text
Law_K(Dg) = d_# Law_K(g)
```

en ambos canales. Esto es una identidad de la familia generativa, no una propiedad asumida de un
estimador.

## 6. Salida order-only y scoring

Una futura inferencia recibe solo el poset orientado y su cardinalidad cuando el canal lo incluya.
Su salida minima sera

```text
y_hat_P: S(P) -> {-1,+1,ABSTAIN},
H_hat(P) in P(S(P)) union {ABSTAIN},
c_hat_P: S(P) -> {-1,0,+1,ABSTAIN},
Chi_hat(P) in {-1,+1,ABSTAIN}.
```

Aqui `P(S(P))` es el conjunto potencia. En particular, `H_hat(P)=empty` es una prediccion valida
que se puntua; solo el simbolo suma separado `H_hat(P)=ABSTAIN` es abstencion. Definimos las
acciones totales

```text
nu(-1)=+1, nu(+1)=-1, nu(0)=0, nu(ABSTAIN)=ABSTAIN,
iota_*^A(A)=iota_P(A) si A subset S(P),
iota_*^A(ABSTAIN)=ABSTAIN.
```

Todas las salidas deben ser equivariantes bajo relabeling. El contrato dual candidato es

```text
H_hat(P^op)   = iota_*^A(H_hat(P)),
y_hat_{P^op}  = y_hat_P o iota_P^{-1},
c_hat_{P^op}  = nu o c_hat_P o iota_P^{-1},
Chi_hat(P^op) = nu(Chi_hat(P)).
```

Las coordenadas, `r`, `M`, las expansiones y las etiquetas continuas quedan prohibidas en
construccion, seleccion, orientacion y abstencion. Solo entran en una capa de scoring separada.

Perdidas candidatas, que deberan congelarse antes de inferencia:

1. `L_side`: error balanceado de `y_hat` sobre los elementos con `h_M != 0`;
2. para una anchura de scoring congelada `delta_H>0`, definir

   ```text
   B_H(delta_H;g,X) = {x in X: |h_M(x)| <= delta_H},
   L_H(H_hat;delta_H) = 0.5 * (FNR_H + FPR_H),
   FNR_H = |B_H minus H_hat| / |B_H|,
   FPR_H = |H_hat minus B_H| / |X minus B_H|;
   ```

3. `L_trapping`: error balanceado de `c_hat` sobre las clases puntuales presentes;
4. `L_character = 1{Chi_hat(P) != Chi(g)}` para el target sectorial BH/WH, solo si el claim
   incluye caracter y ningun terminal de abstencion de mayor precedencia esta activo.

Para las dos perdidas puntuales se congela la politica fail-closed:

```text
e_side(x) = 1{y_hat_P(x) != y_g(x)},              h_M(x) != 0,
L_side = 0.5 * sum_{s in {-1,+1}} mean_{x:y_g(x)=s} e_side(x),

e_trapping(x) = 1{c_hat_P(x) != c_g(x)},
C_g(X) = {c_g(x): x in X},
L_trapping = (1/|C_g(X)|) * sum_{k in C_g(X)} mean_{x:c_g(x)=k} e_trapping(x).
```

Todo `ABSTAIN` por elemento cuenta como error en el indicador correspondiente y permanece en su
denominador de clase. Se reportan `A_side` y `A_trapping` por separado:

```text
A_side = |{x:h_M(x)!=0 and y_hat_P(x)=ABSTAIN}| / |{x:h_M(x)!=0}|,
A_trapping = |{x:c_hat_P(x)=ABSTAIN}| / |X|.
```

Si un denominador requerido esta vacio se emite `LOSS_UNSCORABLE`; nunca se eliminan elementos
abstaining del scoring ni se escoge la politica mirando `h_M` o `c_g` durante inferencia.

`L_H` puntua una banda de elementos, no hits exactos sobre la superficie continua. Si `B_H` o su
complemento estan vacios, emite `LOSS_UNSCORABLE`. Si `H_hat(P)=ABSTAIN`, emite
`ESTIMATOR_ABSTAIN_NO_INTERFACE` antes de scoring; si `H_hat(P)=empty`, calcula `L_H` normalmente y
por tanto conserva sus falsos negativos. `H_hat` no se construye a partir de `B_H`; la banda existe
exclusivamente en la capa embedding-only-scores.

Toda evaluacion sobre `m` realizaciones debe reportar separadamente

```text
A_H = (1/m) sum_i 1{H_hat(P_i)=ABSTAIN},
```

ademas de las perdidas condicionadas a no abstencion. Una tasa de abstencion alta no puede
ocultarse dentro de `L_H` ni interpretarse como localizacion correcta.

`H(g)` tiene medida de volumen cero, por lo que exigir que un elemento sprinkled caiga exactamente
en `r=2M` seria un target vacio casi seguramente. `L_side` y `L_H` evitan ese error de tipo.

## 7. Abstenciones y terminales negativos

Precedencia:

```text
FAILED_DATA_CONTRACT
  > OUT_OF_DUAL_FAMILY
  > PATCH_DUALITY_MISMATCH
  > TARGET_NOT_SPECIFIABLE
  > LOSS_UNSCORABLE
  > CHARACTER_ABSTAIN_SELF_DUAL
  > ESTIMATOR_ABSTAIN_NO_INTERFACE
  > SCIENTIFIC_PASS_OR_FAIL
```

Condiciones concretas de fallo:

- patch angular truncado que no contiene las esferas completas: `TARGET_NOT_SPECIFIABLE`;
- una frontera de `K^+` sin imagen congelada en `K^-`: `PATCH_DUALITY_MISMATCH`;
- causalidad interna al patch donde se congelo causalidad ambiente: `FAILED_DATA_CONTRACT`;
- mezclar `fixed_n` con Poisson no condicionado: `FAILED_DATA_CONTRACT`;
- usar embedding para construir `H_hat`: `FAILED_DATA_CONTRACT`;
- clase de scoring vacia para `L_side`, `L_H` o `L_trapping`: `LOSS_UNSCORABLE`;
- interpretar una clase autodual como BH o WH: `CHARACTER_ABSTAIN_SELF_DUAL`.

## 8. Resultado y limites

**Resultado documental probado:** la familia parametrica anterior esta cerrada bajo `D`, el target
continuo es compatible con el patch completo en angulos y la ley observada es dual-covariante.

```text
OP_1_1_AUTHOR_TERMINAL = DUAL_FAMILY_CLOSED
```

Este terminal no prueba que exista `H_hat`, no fija un selector relacional `R(C)`, no prueba
convergencia y no autoriza un claim 3+1D de recovery.

## 9. Fuentes primarias y anclajes

- Convencion Kruskal local en
  `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2550-2562,3628-3663`;
  el snapshot no verifica literalmente el coeficiente combinado `32 M^3/r`.
  `[UNVERIFIED_EXACT_KRUSKAL_NORMALIZATION_LOCAL_SNAPSHOT]`
- Ashtekar y Krishnan, *Isolated and dynamical horizons and their applications*,
  arXiv:gr-qc/0407042: target cuasi-local por expansiones nulas. `[UNVERIFIED_LOCAL_SNAPSHOT]`
- He y Rideout, *A Causal Set Black Hole*, arXiv:0811.4235: causalidad Schwarzschild 3+1D.
- Eichhorn, Gamito y Stokes, arXiv:2605.06813; lectura local en
  `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-230`:
  expansion/trapping y limite literal del toy 1+1D.
- Limites de claim: `docs/claim_grammar.md:57-188`.
