# P1a — Lema de la pieza Beta-producto en términos de `(k,l)` (`d=2`)

> **ESTADO: OBJETIVO ANALÍTICO MÍNIMO · `NOT_PROVED` · ALCANCE RESTRINGIDO A LA
> PIEZA BETA-PRODUCTO · SIN DATOS NUEVOS · SIN EJECUCIÓN ESTOCÁSTICA.**
>
> Primer paso de la ruta abierta en `emergencia/HOJA_DE_RUTA.md` §18 y en
> `P1a_count_volume_canal_sigma_m_d2.md`: si `Var(Y_n)` y `E[Var(Y_n|G_n)]` son
> ambas `O(1/n)`, entonces `rho_max` tiene meseta no trivial. Este documento **no**
> aborda esa hipótesis completa. Aborda **solo** la pieza que la ley Beta-producto
> puede alcanzar, y deja explícito lo que queda fuera.

## 0. Qué es y qué no es este documento

La descomposición exacta del objetivo es

```text
b_n := E[Var(Y|m)]  =  P_{1,n} + P_{2,n},
P_{1,n} := E_s[ Var(ell|s) ],
P_{2,n} := E_m[ Var_s( E[ell|s] | m ) ].
                         └─ pieza Beta-producto ─┘   └── requiere w ──┘
```

Este lema se ocupa **únicamente del primer sumando**. Conserva el condicionamiento
por la forma `s=(k,l)`, pero obtiene una cota puntual uniforme en todas las formas
admisibles. Por ello puede tomar `E_s[·]` sin conocer la ley de formas `w_n`. No
toca el segundo sumando y, por tanto, **no demuestra `b_n = O(1/n)`**.

```text
LEMMA_SCOPE = BETA_PRODUCT_PIECE_ONLY
LEMMA_DOES_NOT_COVER = E_m[ Var_s( E[ell|s] | m ) ]
```

## 1. Dominio admisible y cotas de partida

Del modelo congelado (`P1a_contrato_representaciones_alternativas_d2.md` §2):
`(u_i,v_i)` iid `Uniform([0,1]^2)` condicionado a `N=n`, y
`ell(x,y) = sqrt((u_y-u_x)(v_y-v_x))`.

```text
DOMINIO:  1 <= k <= n,  1 <= l <= n     (para que Beta(k,n+1-k) sea propia)
X ~ Beta(k, n+1-k),  Y ~ Beta(l, n+1-l),  X perp Y     (CV-3.5, ya demostrado)
ell = sqrt(X Y)
```

**Cota uniforme de `ell` (no es una hipótesis: se sigue del modelo).** `X,Y in [0,1]`
casi seguramente, luego `ell = sqrt(XY) in [0,1]` y `E[ell|s] <= 1` para todo
`(k,l,n)` admisible. Verificado numéricamente en todo el dominio de `n=64,96,128`
como control, pero la razón es el soporte de la Beta, no el cálculo.

Esto da el control auxiliar

```text
Var(ell|s) = E[ell|s]^2 * CV^2(ell|s) <= CV^2(ell|s).
```

La nueva cadena principal no usa este paso: trabaja directamente con la identidad
exacta de la varianza de la Proposición 3. Se conserva aquí como control del modelo.

## 2. Identidad exacta (derivación algebraica)

Defínase el **déficit de medio momento**

```text
A(x) := Gamma(x+1/2)^2 / ( x * Gamma(x)^2 ),        x > 0.
```

**Proposición 1.** Para `X ~ Beta(k,n+1-k)`,

```text
R(k,n) := (E[sqrt(X)])^2 / E[X] = A(k) / A(n+1).
```

*Demostración.* `E[sqrt(X)] = B(k+1/2, n+1-k)/B(k, n+1-k)
= Gamma(k+1/2)Gamma(n+1) / (Gamma(k)Gamma(n+3/2))` y `E[X] = k/(n+1)`. Luego

```text
R(k,n) = [Gamma(k+1/2)^2 Gamma(n+1)^2] / [Gamma(k)^2 Gamma(n+3/2)^2] * (n+1)/k
       = { Gamma(k+1/2)^2 / (k Gamma(k)^2) } * { (n+1) Gamma(n+1)^2 / Gamma(n+3/2)^2 }
       = A(k) / A(n+1).                                                        QED
```

**Proposición 2 (identidad del coeficiente de variación).** Para todo `(k,l,n)`
admisible,

```text
CV^2(ell | k,l) := Var(ell|k,l) / E[ell|k,l]^2 = 1/( R(k,n) R(l,n) ) - 1.
```

*Demostración.* Por independencia de `X` e `Y`, `E[ell] = E[sqrt(X)]E[sqrt(Y)]` y
`E[ell^2] = E[XY] = E[X]E[Y]`. Entonces

```text
CV^2 = E[ell^2]/E[ell]^2 - 1
     = E[X]E[Y] / ( (E[sqrt X])^2 (E[sqrt Y])^2 ) - 1
     = { E[X]/(E[sqrt X])^2 } * { E[Y]/(E[sqrt Y])^2 } - 1
     = 1/( R(k,n) R(l,n) ) - 1.                                                QED
```

**Proposición 3 (identidad exacta de la varianza).** Escribiendo
`R_k := R(k,n)` y `R_l := R(l,n)`,

```text
Var(ell | k,l) = kl/(n+1)^2 * (1 - R_k R_l).
```

*Demostración.* Por la Proposición 1,
`E[sqrt(X)]^2 = E[X]R_k = kR_k/(n+1)` y análogamente para `Y`. Por independencia,

```text
E[ell]^2 = E[sqrt(X)]^2 E[sqrt(Y)]^2 = kl R_k R_l/(n+1)^2,
E[ell^2] = E[XY] = E[X]E[Y] = kl/(n+1)^2.
```

Restando ambas expresiones se obtiene la identidad. `QED`

Las tres proposiciones son **algebraicas**; no dependen de ninguna evaluación numérica.
La malla numérica de §5 es un control de transcripción, **no** una demostración.

## 3. Cadena de Wendel — objetivo del lema

**Desigualdad de Wendel.** Para `0 < s < 1` y `x > 0`,
`(x/(x+s))^{1-s} <= Gamma(x+s)/(x^s Gamma(x)) <= 1`. Con `s = 1/2` y elevando al
cuadrado:

```text
x/(x+1/2) <= A(x) <= 1,        x > 0.
```

> Referencia estándar: J. G. Wendel, *Note on the gamma function*, Amer. Math.
> Monthly **55** (1948), 563–564. `[UNVERIFIED-LOCALLY]` — no está en
> `biblioteca/`; procede verificarla contra la fuente en la auditoría. La
> desigualdad sí está comprobada numéricamente en todo el rango usado (§5).

**Lema CV-4.4a (`NOT_PROVED`, cadena escrita).** Sea `1 <= k,l <= n`. Entonces

```text
(i)   R(k,n) = A(k)/A(n+1) >= A(k) >= k/(k+1/2),
      usando A(n+1) <= 1 y la cota inferior de Wendel en A(k);

(ii)  Var(ell|k,l)
      = kl/(n+1)^2 * (1 - R_k R_l)
      <= [((k+l)/2 + 1/4)/(n+1)^2]
         * [k/(k+1/2)] * [l/(l+1/2)];

(iii) como k+l <= 2n y los dos ultimos factores son <= 1,
      Var(ell|k,l) <= (n+1/4)/(n+1)^2 <= 1/n
      UNIFORMEMENTE para todo 1 <= k,l <= n;

(iv)  P_{1,n} := E_s[Var(ell|s)]
      <= (n+1/4)/(n+1)^2 <= 1/n.
```

La expectativa de (iv) elimina cualquier dependencia de `w_n` porque la cota de
(iii) es puntual y uniforme. No se escribe `P_{1,n} = E_s(1/n)`: `1/n` es una
cota, no el valor de la varianza condicionada. No se exige balance, no degeneración
uniforme ni convergencia de `k_n/n` o `l_n/n`; la cadena incluye las formas
extremadamente desbalanceadas.

Los pasos (i)–(iv) están escritos pero **no auditados**. El estado permanece
`NOT_PROVED` hasta que la auditoría verifique la cadena, incluida la forma exacta de
la identidad de la Proposición 3, la desigualdad de Wendel y el paso
`A(n+1) <= 1`.

## 4. Diagnóstico: por qué NO se usa la heurística `1/(4k)+1/(4l)`

**Este apartado es diagnóstico. No forma parte de la demostración.**

La intuición de «ruido de conteo» sugiere `CV^2 ~ 1/(4k) + 1/(4l)`. En el régimen
relevante (`k,l = Theta(n)`) esa aproximación **falla**: la expansión asintótica
tiene un término `-1/(2n)` del mismo orden que el principal y de signo opuesto.

| `n` | `k=l` | `CV^2` exacto | `1/(4k)+1/(4l)` | error | `+(-1/(2n))` | error |
|---:|---:|---:|---:|---:|---:|---:|
| 64 | 12 | 0.034546 | 0.041667 | +21 % | 0.033854 | −2.0 % |
| 64 | 25 | 0.012382 | 0.020000 | +62 % | 0.012188 | −1.6 % |
| 64 | 38 | 0.005480 | 0.013158 | **+140 %** | 0.005345 | −2.5 % |
| 128 | 25 | 0.016253 | 0.020000 | +23 % | 0.016094 | −1.0 % |
| 128 | 51 | 0.005945 | 0.009804 | +65 % | 0.005898 | −0.8 % |
| 128 | 76 | 0.002707 | 0.006579 | **+143 %** | 0.002673 | −1.3 % |

**Consecuencia operativa:** cualquier intento de identificar la constante `b` a
partir de la heurística ingenua está mal fundado. La cadena de Wendel evita el
problema porque acota, no aproxima. La nueva cota uniforme tampoco identifica una
constante límite para `P_{1,n}` ni para `b_n`.

## 5. Controles numéricos (transcripción, no demostración)

Deterministas, solo lectura, reutilizando `e_sqrt_beta` y `var_ell_given_shape` de
`emergencia/p1a_count_volume_cota_resolucion_evaluacion_d2.py` (ya auditado). No se
añade script nuevo.

```text
(1) max |R(k,n) - A(k)/A(n+1)|  sobre 1<=k<=n, n=64,96,128   =  1.7e-13
(2) x/(x+1/2) <= A(x) <= 1  para x=1..600 y x=64,96,128,129  =  True
(3) (1+1/2k)(1+1/2l)-1 >= CV^2 exacto en TODO 1<=k,l<=n,
    n=64,96,128                                              =  True
    holgura maxima 2.05x, en la esquina degenerada (k,l)=(1,1)
(4) E[ell|s] <= 1 en todo el dominio                          =  True
```

El control (3) es el falsable: una cadena mal escrita habría producido una cota por
debajo del valor exacto en algún `(k,l)`.

La comparación documental de la nueva cota uniforme con el máximo exacto ya
disponible es:

| `n` | máximo exacto | cota uniforme | cota − máximo | máximo/cota |
|---:|---:|---:|---:|---:|
| 64 | 0.00345920 | 0.01520710 | 0.01174790 | 22.75 % |
| 96 | 0.00236862 | 0.01022957 | 0.00786095 | 23.15 % |
| 128 | 0.00180384 | 0.00770687 | 0.00590303 | 23.41 % |

Esta tabla no interviene en la demostración ni autoriza una ejecución nueva.

## 6. Los cuatro límites explícitos

1. **Dominio.** Todo lo anterior vale solo para `1 <= k,l <= n`. Fuera de ahí la
   Beta no es propia y `A(x)` no está definida en `x=0`.
2. **Modelo y dimensión.** La identidad usa la factorización Beta-producto del
   modelo `fixed-n` en `d=2`. No se extrapola a otras dimensiones, al canal de
   Poisson ni a una escala física absoluta sin rederivación.
3. **La identidad exacta debe leerse en §2, no en §5.** Las Proposiciones 1–3
   están demostradas algebraicamente; la malla numérica es control de
   transcripción. Una malla no es una demostración.
4. **El lema no controla `E_m[ Var_s( E[ell|s] | m ) ]`.** Ese sumando —la
   dispersión entre formas que `m` no resuelve— sigue requiriendo `w`. Por tanto
   este lema **no** establece `b_n = O(1/n)`, ni siquiera si se demuestra.

## 7. Qué quedaría aislado si el lema pasa a demostrado

La pieza Beta-producto dejaría de ser el obstáculo, y lo pendiente sería, en orden:

1. el segundo sumando, `P_{2,n} = E_m[Var_s(E[ell|s]|m)]`, que sí necesita `w_n`;
2. y solo después `a_n = n Var(Y_n)`, que es la parte realmente difícil porque es
   íntegramente una propiedad de la distribución de salida del selector.

No hace falta controlar las colas del selector ni demostrar no degeneración de
`(k,l)` para cerrar `P_{1,n}`. Bajo las dos entradas pendientes de auditoría
(identidad algebraica y Wendel), su régimen analítico queda resuelto y no requiere
ejecución.

## 8. Estado de control

```text
BETA_PRODUCT_IDENTITY = NUMERICALLY_VERIFIED_DERIVATION_PENDING
WENDEL_SOURCE = UNVERIFIED_LOCALLY
A2_CONDITIONAL_VARIANCE_BOUND = UNIFORM_ALL_SHAPES_WRITTEN_PENDING_AUDIT
A3_SELECTOR_TAIL_OR_NONDEGENERACY_CONTROL_FOR_P1 = UNNECESSARY
A4_P1_ANALYTIC_REGIME = RESOLVED_PENDING_IDENTITY_AND_WENDEL_AUDIT
A4_NEW_EXECUTION_REQUIRED = NO
P2_SCALING = OPEN_REQUIRES_W_N
FULL_B_SCALING = NOT_ESTABLISHED
NEW_DATA = NONE
```

> **Nota para la auditoría.** Las Proposiciones 1–3 de §2 están escritas con
> demostración algebraica completa, y §3 contiene la cadena de Wendel entera. La
> identidad y la cota uniforme son por tanto candidatas a ascenso **en la auditoría**,
> no por decisión propia. Se registran conservadoramente a propósito: dos rondas
> previas de auditoría en esta línea devolvieron `FAIL_MATERIAL` por sobreafirmación
> y por retractaciones formuladas pero no aplicadas.

```text
LEMMA_SCOPE = BETA_PRODUCT_PIECE_ONLY
LEMMA_REQUIRES_BALANCE_OR_NONDEGENERACY = NO
LEMMA_IDENTIFIES_LIMITING_CONSTANT = NO
HEURISTIC_1_OVER_4K = REJECTED_AS_PROOF_BASIS (Seccion 4, error hasta +143%)
NEW_SCRIPT_ADDED = NO
NOVELTY_CERTIFIED = NO
```

**Consecuencia científica, con techo de afirmación:** el ruido Beta-producto dentro
de una forma desaparece uniformemente como `O(1/n)`, incluso para formas
degeneradas. Esto aporta una pieza de emergencia métrica. No establece el escalado
del residual completo `b_n = P_{1,n}+P_{2,n}`, porque `P_{2,n}` permanece abierto,
ni demuestra la meseta de `rho_max`.
