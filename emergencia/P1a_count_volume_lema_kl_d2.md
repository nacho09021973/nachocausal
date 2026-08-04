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
E[Var(Y|m)]  =  E_s[ Var(ell|s) ]  +  E_m[ Var_s( E[ell|s] | m ) ].
                └── pieza Beta-producto ──┘   └──── requiere w ────┘
```

Este lema se ocupa **únicamente del primer sumando**, y dentro de él solo del
comportamiento de `Var(ell|s)` para una forma `s=(k,l)` dada. No calcula
`E_s[·]` (eso necesita la ley de formas), no toca el segundo sumando, y por tanto
**no demuestra `b = O(1/n)`**.

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

Esto es lo que permite pasar de una cota sobre el **coeficiente de variación** a una
cota sobre la **varianza**:

```text
Var(ell|s) = E[ell|s]^2 * CV^2(ell|s) <= CV^2(ell|s).
```

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

Ambas proposiciones son **algebraicas**; no dependen de ninguna evaluación numérica.
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

(ii)  CV^2(ell|k,l) <= (1 + 1/(2k))(1 + 1/(2l)) - 1
                     = 1/(2k) + 1/(2l) + 1/(4kl);

(iii) si ademas k >= eps*n y l >= eps*n para algun eps > 0, entonces
      CV^2(ell|k,l) <= 1/(eps n) + 1/(4 eps^2 n^2) = O(1/n);

(iv)  como E[ell|s] <= 1 (Seccion 1),
      Var(ell | s_n) <= CV^2(ell | s_n) = O(1/n)  UNIFORMEMENTE sobre toda
      sucesion de formas que cumpla la no-degeneracion (iii).
```

**No se supone convergencia de `k_n/n` ni de `l_n/n`.** La no-degeneración uniforme
basta para el **orden**; la constante límite sí requeriría las proporciones, y no se
afirma aquí.

Los pasos (i)–(iv) están escritos pero **no auditados**. El estado permanece
`NOT_PROVED` hasta que la auditoría verifique la cadena, incluida la forma exacta de
la desigualdad de Wendel y el paso `A(n+1) <= 1`.

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
problema porque acota, no aproxima. Y confirma la advertencia del PI: la constante
límite depende de las proporciones `(k_n/n, l_n/n)`, no solo del orden.

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

## 6. Los cuatro límites explícitos

1. **Dominio.** Todo lo anterior vale solo para `1 <= k,l <= n`. Fuera de ahí la
   Beta no es propia y `A(x)` no está definida en `x=0`.
2. **Cota de `ell`.** El paso de `CV^2` a `Var` usa `E[ell|s] <= 1`, que se sigue
   del soporte `[0,1]` del modelo congelado. En cualquier reformulación sin esa
   normalización, el paso (iv) del lema **no** se traslada.
3. **La identidad exacta debe leerse en §2, no en §5.** Las Proposiciones 1 y 2
   están demostradas algebraicamente; la malla numérica es control de
   transcripción. Una malla no es una demostración.
4. **El lema no controla `E_m[ Var_s( E[ell|s] | m ) ]`.** Ese sumando —la
   dispersión entre formas que `m` no resuelve— sigue requiriendo `w`. Por tanto
   este lema **no** establece `b = O(1/n)`, ni siquiera si se demuestra.

## 7. Qué quedaría aislado si el lema pasa a demostrado

La pieza Beta-producto dejaría de ser el obstáculo, y lo pendiente sería, en orden:

1. que la ley de formas del selector cumpla la no-degeneración uniforme `k_n,l_n >= eps n`
   —una afirmación sobre `MIN_COVERAGE_LEX`, no sobre la geometría—;
2. el segundo sumando, `E_m[Var_s(E[ell|s]|m)]`, que sí necesita `w`;
3. y solo después `a = n Var(Y_n)`, que es la parte realmente difícil porque es
   íntegramente una propiedad de la distribución de salida del selector.

## 8. Estado de control

```text
BETA_PRODUCT_IDENTITY = NUMERICALLY_VERIFIED_DERIVATION_PENDING
UNIFORM_NONDEGENERACY_LEMMA = NOT_PROVED
FULL_B_SCALING = NOT_ESTABLISHED
NEW_DATA = NONE
```

> **Nota para la auditoría.** Las Proposiciones 1 y 2 de §2 están escritas con
> demostración algebraica completa, y §3 contiene la cadena de Wendel entera. Los
> dos primeros estados son por tanto candidatos a ascenso **en la auditoría**, no
> por decisión propia. Se registran conservadoramente a propósito: dos rondas
> previas de auditoría en esta línea devolvieron `FAIL_MATERIAL` por sobreafirmación
> y por retractaciones formuladas pero no aplicadas.

```text
LEMMA_SCOPE = BETA_PRODUCT_PIECE_ONLY
LEMMA_ASSUMES_PROPORTION_LIMITS = NO (solo no-degeneracion uniforme)
LEMMA_IDENTIFIES_LIMITING_CONSTANT = NO
HEURISTIC_1_OVER_4K = REJECTED_AS_PROOF_BASIS (Seccion 4, error hasta +143%)
NEW_SCRIPT_ADDED = NO
NOVELTY_CERTIFIED = NO
```
