# WP4 — Derivación analítica del score directo para `I(tau)` en el diamante de registro

**Estado:** `DERIVATION_ONLY / NO_IMPLEMENTATION / NO_EXECUTION / NO_LABEL_CHANGE`.

Este documento deriva, en forma exacta e implícita, el score `partial_tau log c_tau` de la cópula
del diamante de registro, para sustituir en una fase futura el estimador Hellinger por diferencias
finitas. **No implementa nada, no ejecuta nada, no evalúa ningún número, no cambia etiquetas.**

Relación con lo ya cerrado:

- El contrato Hellinger (`wp4_ibar_interval_executable_contract.md`) fue ejecutado por
  `wp4_ibar_interval_verifier.py` (commit `ba6f747`) y emitió su terminal
  `NUMERICAL_NONCONVERGENCE` en dos ejecuciones deterministas idénticas. Ese contrato queda
  **cerrado e intacto**; este documento no lo reabre ni lo enmienda.
- Permanecen literalmente los estados congelados:

```text
IBAR_DIAMOND_INTERVAL = INCONCLUSIVE_NUMERICAL_NONCONVERGENCE
CONSTANT_LEVEL_DEFEATER = NOT_EVALUATED_IBAR_UNAVAILABLE
```

- La ruta de score analítico está anticipada como validación independiente admisible en
  `wp4_ibar_interval_numerical_design.md` §6 (líneas 104–107: "diferenciación
  automática/analítica del score si se deriva"). Este documento es esa derivación.
- Queda registrado el **rechazo del complex-step / AD ingenuo a través del pipeline existente**:
  `brentq` es un método real de bisección/acotación con comparaciones (no una continuación
  holomorfa), `PchipInterpolator` es un algoritmo real dependiente de signos de pendientes, y el
  pipeline contiene clipping, ramas y `abs`. La función matemática es suave; el algoritmo no es
  complex-step-compatible. La ruta correcta es la derivación implícita de este documento, en la
  que la raíz nunca se diferencia numéricamente: sus derivadas se obtienen del teorema de la
  función implícita en forma cerrada.

## 0. Mapa de ítems encargados → secciones

```text
(1) f_tau, marginales y derivadas exactas ............ §3, §5
(2) derivada implícita de los cuantiles .............. §6
(3) fórmula completa del score a (x,y) fijos ......... §6, §7
(4) soporte dependiente de tau ....................... §4
(5) identidad E_c[s]=0 (y refuerzos por rebanada) .... §8
(6) finitud de E_c[s^2] .............................. §9
(7) integral en coordenadas físicas sin inversión .... §7
(8) normalización por dv (régimen del Anexo C) ....... §10
```

## 1. Objeto congelado y notación

Familia y objeto exactamente los del contrato §1 y el diseño §1:

```text
r_p = 3.0, r_q = 0.5, v_p = 0.0, v_q = 0.02, dv := v_q - v_p = 0.02,
tau in [1.0, 1.2],
I(tau) = integral_[0,1]^2 (partial_tau log c_tau(x,y))^2 c_tau(x,y) dx dy,
Ibar = sup_{tau in [1.0,1.2]} I(tau).
```

Métrica EF `g_tau = -(1 - tau/r) dv^2 + 2 dv dr` con `sqrt(-det g_tau) = 1`, de modo que la
medida de volumen es `dv dr` (Anexo C, `wp4_comparable_pair_separation.md:59`). Esta derivación
cambia el **estimador**, nunca el objeto: `c_tau` sigue siendo la densidad de cópula de la medida
de volumen normalizada del diamante `D_tau`.

Funciones básicas (idénticas a `wp4_kappa_numeric_reference.py:56-66`):

```text
W(tau,r)      = exp(r/tau) * (r/tau - 1)
W'(tau,r)     = partial_r W = (r/tau^2) * exp(r/tau)          [ > 0 para r > 0 ]
Utilde(tau,v,r) = -exp(-v/(2 tau)) * W(tau,r)
```

Identidad útil (verificada por cálculo directo):

```text
partial_tau W(tau,r) = -(r^2/tau^3) exp(r/tau) = -(r/tau) * W'(tau,r).
```

## 2. Coordenada nula, raíz y dominio

**Lema 2.1 (rectángulo).** `Utilde` es constante a lo largo de geodésicas nulas salientes
(`dr/dv = (1 - tau/r)/2`): sustituyendo, `dUtilde/dv = exp(-v/2tau) [ W/(2tau) - W'(1-tau/r)/2 ]
= 0` porque `W'(1 - tau/r) = W/tau`. Con `v` (nula entrante) esto da coordenadas doblemente nulas
y el diamante es el rectángulo

```text
R_tau = [Up(tau), Uq(tau)] x [v_p, v_q],
Up(tau) = Utilde(tau, v_p, r_p),   Uq(tau) = Utilde(tau, v_q, r_q).
```

**Lema 2.2 (straddle en todo el intervalo).** Para todo `tau in [1.0,1.2]`: `r_p = 3 > tau` da
`W(tau,r_p) > 0` luego `Up(tau) < 0`; `r_q = 0.5 < tau` da `W(tau,r_q) < 0` luego `Uq(tau) > 0`.
Por tanto `DeltaU(tau) := Uq - Up > 0` y el horizonte `r = tau` (la línea `Utilde = 0`) cruza el
rectángulo para todo `tau` del intervalo.

**Lema 2.3 (raíz única y contención).** A `(tau,v)` fijos, `partial_r Utilde = -exp(-v/2tau) W'
< 0` para `r > 0`, con `Utilde -> exp(-v/2tau) > 0` cuando `r -> 0+` y `Utilde -> -infty` cuando
`r -> infty`. Existe raíz única `r_tau(U,v) in (0,infty)` para todo `U < exp(-v/(2tau))`. Para
`U = Uq` esto exige `|W(tau,r_q)| < exp((v_q - v)/(2tau))`; como el lado derecho es `>= 1` para
`v <= v_q` y `e^rho (1-rho) < 1` para todo `rho = r_q/tau in (0,1)` (la función `e^rho(1-rho)`
vale 1 en 0 y es estrictamente decreciente), la condición se cumple en todo `R_tau`.

**Lema 2.4 (rango compacto de `r`).** Dos pasos de monotonía, ambos derivados de las fórmulas
implícitas cerradas de más abajo, dan el rango de `r` sin evaluar nada numéricamente.

*Paso 1 (monotonía en `U`, a `v` fijo).* `partial_U r|_{tau,v} = -exp(v/(2tau))/W'(tau,r) < 0`
para todo `r>0` (pues `W'>0` y la exponencial es positiva). Luego, a `(tau,v)` fijos, `r` es
estrictamente decreciente en `U`: el mínimo de `r` sobre cualquier segmento `{v} x [Up,Uq]` se
alcanza en `U=Uq` y el máximo en `U=Up`, para **cualquier** `v`.

*Paso 2 (monotonía en `v`, a lo largo de cada borde vertical `U` fijo).* `partial_v r|_{tau,U} =
(r-tau)/(2r)`, cuyo signo depende solo de si `r` está antes o después del horizonte. Por la
identidad `Utilde>0 <=> W(tau,r)<0 <=> r<tau` (válida para todo `v`, ya que el factor
`exp(-v/2tau)` que multiplica a `W` en `Utilde` es siempre positivo y no cambia el signo), el
signo de `r-tau` a lo largo de un borde vertical entero `U` fijo está determinado únicamente por
el signo de ese `U`, no por `v`:

- en el borde `U=Uq(tau)>0` (Lema 2.2): `r<tau` en todo el borde, luego `partial_v r<0` en todo
  el borde, luego `r` es estrictamente decreciente en `v` a lo largo de él; su mínimo se alcanza
  en `v=v_q` (el mayor `v`), y ese punto es exactamente la esquina `q`, donde `r=r_q=0.5` por
  construcción (`Uq(tau):=Utilde(tau,v_q,r_q)`).
- en el borde `U=Up(tau)<0`: `r>tau` en todo el borde, luego `partial_v r>0` en todo el borde,
  luego `r` es estrictamente creciente en `v`; su máximo se alcanza en `v=v_q`, dando
  `r_max(tau) := r_tau(Up(tau), v_q)`, caracterizado por `W(tau, r_max) = exp(dv/(2tau)) W(tau,
  r_p)` (igualando `Utilde(tau,v_q,r_max) = Up(tau) = Utilde(tau,v_p,r_p)` y despejando, con
  `v_p=0`, `v_q=dv`).

Combinando los dos pasos: el mínimo global de `r` sobre todo `R_tau` es el mínimo-en-`U` (que por
el Paso 1 está en `U=Uq`, para cualquier `v`) del mínimo-en-`v` a lo largo de ese borde (que por
el Paso 2 está en `v=v_q`) — es decir, la esquina `(Uq,v_q)`, con `r=r_q=0.5` exactamente. El
máximo global es, simétricamente, la esquina `(Up,v_q)`, con `r=r_max(tau)` como arriba. Ninguna
otra combinación de bordes puede dar un extremo más allá de estas dos esquinas, porque el Paso 1
ya fija que el extremo-en-`U` (para cualquier `v` dado) está en `U in {Up,Uq}`, y el Paso 2 fija
el extremo-en-`v` en cada uno de esos dos bordes por separado.

Cota superior de `r_max(tau)`, con holgura deliberada (el objetivo es excluir singularidades del
denominador, no optimizar el valor de `r_max`; se usa `3.2`, no el óptimo `3.1`, para que ningún
eslabón dependa de una coincidencia numérica fina):

```text
W(tau,3.2)/W(tau,3) = exp(0.2/tau) * (3.2-tau)/(3-tau)
                    > exp(0.2/tau) * 1                       [pues 3.2-tau > 3-tau > 0 para tau<3]
                    >= exp(0.2/1.2) = exp(1/6)                [pues 0.2/tau es decreciente en tau, tau<=1.2]
                    >  exp(1/100)                              [pues 1/6 > 1/100, sin necesidad de decimales]
                    >= exp(dv/(2tau)) = exp(0.01/tau)         [pues dv/(2tau) = 0.01/tau <= 0.01 para tau>=1],
```

y como `W(tau,.)` es estrictamente creciente para `r>tau` (pues `W'>0`), `W(tau,r_max) =
exp(dv/(2tau)) W(tau,3) < W(tau,3.2)` implica `r_max(tau) < 3.2` para todo `tau in [1.0,1.2]`, con
margen amplio y no ajustado (`exp(1/6) approx 1.181` frente a `exp(0.01) approx 1.010`: casi un
18% de margen, no ~0.005% como con la cota anterior de `3.1`). En resumen:

```text
r_tau(U,v) in [0.5, 3.2]   sobre todo R_tau y todo tau in [1.0, 1.2].
```

**Derivadas implícitas de la raíz** (teorema de la función implícita sobre
`Utilde(tau,v,r) = U`; nunca se diferencia `brentq`):

```text
partial_U r|_{tau,v}   = -exp(v/(2tau)) / W'(tau,r)
partial_v r|_{tau,U}   = (r - tau) / (2r)
partial_tau r|_{U,v}   = r/tau - (v/2) * (1/tau - 1/r)
```

Comprobaciones internas exactas: sobre el horizonte (`Utilde=0`, `r=tau`): `partial_v r = 0` y
`partial_tau r = 1`, consistentes con que la línea `Utilde=0` es `r = tau` para todo `v`. En
`v = 0` a `U` fijo: `partial_tau r = r/tau`, consistente con la autosimilitud `W(tau,r) =
w(r/tau)`.

## 3. Densidad conjunta y derivadas cerradas (ítem 1, parte puntual)

La medida `dv dr` empujada a `(Utilde, v)` tiene densidad sin normalizar (idéntica a
`wp4_kappa_numeric_reference.py:82`):

```text
h_tau(U,v) = |partial r / partial U|_v = exp(v/(2tau)) / W'(tau, r_tau(U,v)),
log h      = v/(2tau) + 2 log tau - log r - r/tau.
```

Sus tres derivadas parciales, usando §2, se cierran en formas notablemente simples
(cálculo directo, con las cancelaciones detalladas abajo):

```text
partial_U  log h |_{tau,v} = (1/r + 1/tau) * exp(v/(2tau)) / W'(tau,r)
partial_v  log h |_{tau,U} = tau / (2 r^2)
partial_tau log h |_{U,v}  = 1/tau - v / (2 r^2)
```

Verificación de la segunda: `1/(2tau) - (1/r + 1/tau)(r-tau)/(2r) = 1/(2tau) -
(r^2 - tau^2)/(2 r^2 tau) = tau/(2 r^2)`. Verificación de la tercera: `-v/(2tau^2) + 2/tau +
r/tau^2 - (1/r + 1/tau)[ r/tau - (v/2)(1/tau - 1/r) ] = 1/tau - v/(2 r^2)`. La derivada mixta,
necesaria en §10, es

```text
partial^2_{U v} log h = -(tau/r^3) partial_U r = (tau/r^3) * exp(v/(2tau)) / W'(tau,r) > 0.
```

Todas las cantidades son funciones elementales de `(tau, v, r)`; la única cantidad no cerrada es
la raíz `r_tau(U,v)`, que se evalúa (p. ej. con `brentq`) pero **jamás se diferencia
numéricamente**.

## 4. Soporte móvil resuelto: dominio fijo `(w,v)` (ítem 4)

El soporte en `U` depende de `tau` a través de `Up(tau), Uq(tau)`. Se elimina con la
reparametrización afín creciente

```text
w = (U - Up(tau)) / DeltaU(tau)  in [0,1],
U(w,tau) = Up(tau) + w * DeltaU(tau),
Omega = [0,1] x [v_p, v_q]   (dominio fijo, independiente de tau).
```

**La cópula no cambia:** para cada `tau` fijo, `w` es una transformación estrictamente creciente
de `U`, y la cópula es invariante bajo transformaciones marginales estrictamente crecientes
(marginales continuas por §9; hecho estándar, Sklar / Nelsen 2006, Thm 2.4.3). Además los rangos
coinciden: `F_1(w) = F_U(U(w))`. Por tanto `c_tau` y su score a rangos fijos pueden derivarse
íntegramente sobre el dominio fijo `Omega`, y **toda diferenciación en `tau` bajo el signo
integral tiene límites de integración fijos: no aparecen términos de frontera**.

Densidad sin normalizar sobre `Omega`:

```text
htilde_tau(w,v) = h_tau(U(w,tau), v) * DeltaU(tau).
```

Movimiento de las esquinas (cerrado; con `partial_tau W = -(r/tau)W'`):

```text
Uc'(tau) = d/dtau [ -exp(-v_c/(2tau)) W(tau,r_c) ]
         = -exp(-v_c/(2tau)) [ (v_c/(2tau^2)) W(tau,r_c) - (r_c^2/tau^3) exp(r_c/tau) ],
para (v_c, r_c) = (v_p, r_p) y (v_q, r_q);  DeltaU'(tau) = Uq'(tau) - Up'(tau).
```

Derivada total en `tau` a `(w,v)` fijos:

```text
beta_tau(w) = Up'(tau) + w * DeltaU'(tau)      [ = partial_tau U a w fijo ]

D(w,v) := partial_tau log htilde |_{w,v}
        = [ 1/tau - v/(2 r^2) ]
        + [ (1/r + 1/tau) * exp(v/(2tau)) / W'(tau,r) ] * beta_tau(w)
        + DeltaU'(tau)/DeltaU(tau),
partial_w log htilde |_{v} = (1/r + 1/tau) * exp(v/(2tau)) / W'(tau,r) * DeltaU(tau),
partial_v log htilde |_{w} = tau / (2 r^2),
```

con `r = r_tau(U(w,tau), v)` en todas partes.

**Identidades de esquina (comprobación exacta gratuita para cualquier implementación futura):**
en `(w,v) = (0, v_p)` se tiene `r = r_p` idénticamente en `tau`, y en `(w,v) = (1, v_q)`,
`r = r_q` idénticamente; equivalentemente `partial_tau r|_U + partial_U r * Uc'(tau) = 0` en esas
esquinas (verificado simbólicamente en la derivación de §2).

## 5. Marginales, CDFs y sus derivadas en `tau` (ítems 1 y 2, parte integral)

Sobre `Omega`, con integrales de límites fijos e integrandos cerrados (dada la raíz):

```text
m1(w)   = integral_{v_p}^{v_q} htilde(w,v) dv          (marginal sin normalizar en w)
m2(v)   = integral_0^1       htilde(w,v) dw            (marginal sin normalizar en v)
A(tau)  = integral integral_Omega htilde dw dv         (= V(tau), masa total)
f(w,v)  = htilde/A,   f1 = m1/A,   f2 = m2/A,
F1(w)   = integral_0^w f1,   F2(v) = integral_{v_p}^v f2.
```

Las marginales no tienen forma cerrada; su resolución exacta consiste en que son **integrales
1D de integrandos cerrados**, junto con sus derivadas en `tau`, que se obtienen diferenciando
bajo el signo integral (legítimo por §4 y §9):

```text
E[D | w]  = (1/m1(w)) integral htilde(w,v) D(w,v) dv
E[D | v]  = (1/m2(v)) integral htilde(w,v) D(w,v) dw
E[D]      = A'(tau)/A(tau) = (1/A) integral integral htilde D dw dv

partial_tau f1(w) = f1(w) * ( E[D|w] - E[D] )
partial_tau f2(v) = f2(v) * ( E[D|v] - E[D] )
partial_tau F1(w) = integral_0^w f1(w') ( E[D|w'] - E[D] ) dw'
partial_tau F2(v) = integral_{v_p}^v f2(v') ( E[D|v'] - E[D] ) dv'
```

Consistencias automáticas exigibles a toda implementación futura: `partial_tau F1(1) = 0` y
`partial_tau F2(v_q) = 0`.

## 6. Derivada implícita de los cuantiles y score a rangos fijos (ítems 2 y 3)

Cuantiles `Q1 = F1^{-1}`, `Q2 = F2^{-1}` (existen y son suaves por §9). **Son objetos
matemáticos usados aquí sólo para definir qué significa "a rango `x` fijo"** — es decir, para
plantear correctamente la derivada `partial_tau Q1(tau,x)|_x` vía el teorema de la función
implícita. Ni `Q1` ni `Q2` se evalúan nunca numéricamente en lo que sigue: la fórmula resultante
de `a1(w)` (más abajo) y, con ella, toda la construcción de §6-§7, se expresa enteramente en
`w` (o `v`), nunca en `x` (o `y`), y sólo requiere `F1, F2` **hacia delante** (integrales
acumuladas de §5), nunca su inversa. Sus derivadas en `tau` **no** se obtienen diferenciando
ninguna inversión numérica sino implícitamente, de `F1(tau, Q1(tau,x)) = x`:

```text
a1(w) := partial_tau Q1(x) |_{x=F1(w)} = - partial_tau F1(w) / f1(w)
a2(v) := partial_tau Q2(y) |_{y=F2(v)} = - partial_tau F2(v) / f2(v)
```

Con `g_tau(w,v) := log c_tau(F1(w), F2(v)) = log htilde + log A - log m1 - log m2`, el score a
rangos `(x,y)` fijos, evaluado en `w = Q1(x)`, `v = Q2(y)`, es

```text
s_tau(x,y) = partial_tau g |_{w,v} + a1(w) * partial_w g + a2(v) * partial_v g,
```

donde cada pieza tiene estructura de residuo centrado (ANOVA), consecuencia directa de §5:

```text
partial_tau g = D - E[D|w] - E[D|v] + E[D]                     (doble centrado)
partial_w  g  = partial_w log htilde - E[ partial_w log htilde | w ]   (centrado en v|w)
partial_v  g  = partial_v log htilde - E[ partial_v log htilde | v ]
             = (tau/2) * ( 1/r^2 - E[ 1/r^2 | v ] ).
```

Observaciones estructurales: (i) las constantes en `(w,v)` de `D` (los términos `1/tau` y
`DeltaU'/DeltaU`) se cancelan exactamente en el doble centrado; (ii) no hay resta de dos
densidades casi idénticas en ninguna parte: cada término es una cantidad centrada calculada a un
único `tau`; (iii) el factor `4/d^2` del estimador Hellinger ha desaparecido porque no hay
diferencia finita en `tau`.

## 7. Integral de Fisher en coordenadas físicas, sin inversión (ítem 7)

Cambio de variables `x = F1(w)`, `y = F2(v)` (`dx dy = f1 f2 dw dv`,
`c_tau(F1(w),F2(v)) = f/(f1 f2)`):

```text
sigma(w,v) := s_tau(F1(w), F2(v))
            = [ D - E[D|w] - E[D|v] + E[D] ]
              + a1(w) * partial_w g(w,v)
              + a2(v) * partial_v g(w,v),

I(tau) = integral integral_Omega f(w,v) * sigma(w,v)^2 dw dv.
```

Esta es la forma final. Requisitos computacionales de la ruta completa:

- evaluar la raíz `r_tau(U(w,tau),v)` (p. ej. `brentq`), con derivadas cerradas de §2;
- integrales 1D y 2D **hacia delante** sobre dominios fijos (`m1, m2, A, E[D|.], F, partial_tau F`);
- **ninguna** inversión de cuantiles, **ningún** PCHIP, **ninguna** escalera en `d`,
  **ninguna** diferencia finita en `tau`.

## 8. Identidades obligatorias (ítem 5, reforzado)

**Puente §6→§8 (por qué la fórmula explícita hereda las identidades condicionales sin verificación
término a término).** `sigma(w,v)` de §7 no es una fórmula propuesta que deba compararse con el
score verdadero: **es** el score verdadero, por construcción, y esto se ve sin sumar ni cancelar
ningún término. `g(tau,w,v) = log c_tau(F1(tau,w), F2(tau,v))` es la única función involucrada;
`s_tau(x,y)` (a rango fijo) es, por definición, la derivada total en `tau` de
`tau |-> g(tau, w(tau,x), v(tau,y))` a lo largo del camino `w(tau)=Q1(tau,x)`, `v(tau)=Q2(tau,y)`
que mantiene `(x,y)=(F1(tau,w(tau)), F2(tau,v(tau)))` constante. La regla de la cadena
multivariable da esa derivada total como exactamente

```text
d/dtau [ g(tau,w(tau),v(tau)) ] = partial_tau g|_{w,v} + (dw/dtau)*partial_w g + (dv/dtau)*partial_v g,
```

con `dw/dtau|_x = a1(w)` y `dv/dtau|_y = a2(v)` por definición de `a1, a2` (§6). Esta identidad es
álgebra elemental de derivadas totales, no una elección de representación: **no hay una "fórmula
de §6" y un "score verdadero de §8" que deban coincidir por coincidencia — son el mismo objeto,
descrito dos veces.** Por tanto, todo lo que sea cierto para el score verdadero `s_tau(x,y)` es
automáticamente cierto para `sigma(w,v) = s_tau(F1(w),F2(v))` sin ningún paso adicional. En
particular, las identidades condicionales que siguen —consecuencia general de que las marginales
de toda cópula son uniformes, independiente de cualquier fórmula concreta para el score— se
heredan directamente, y **no requieren, ni admiten como ruta alternativa de verificación, una
cancelación explícita término a término de los sumandos `D`, `E[D|w]`, `E[D|v]`, `E[D]`,
`a1*partial_w g`, `a2*partial_v g` de §6-§7**: intentar esa ruta directa deja un residuo
(`E[D] - E[E[D|v]|w]` frente a `E[a2(v) partial_v g|w]`) cuya cancelación mutua no es manifiesta
por inspección de los sumandos por separado — es exactamente la razón por la que el argumento
correcto pasa por la identidad de derivada total de este párrafo y no por la cancelación directa.

**(I1) Por rebanada.** Las marginales de toda cópula son uniformes:
`integral_0^1 c_tau(x,y) dx = 1` para todo `y` y todo `tau`. Diferenciando en `tau` (legítimo por
§9) y cambiando variables como en §7:

```text
integral_0^1 f(w,v) sigma(w,v) dw = 0    para TODO v in [v_p, v_q],
integral f(w,v) sigma(w,v) dv     = 0    para TODO w in [0,1].
```

**(I2) Global (la identidad del encargo).** Integrando (I1):

```text
E_{c_tau}[ s_tau ] = integral integral f sigma dw dv = 0,
```

y por tanto `I(tau) = Var_{c_tau}(s_tau)`.

**(I3) Esquinas.** `r(0, v_p) = r_p` y `r(1, v_q) = r_q` idénticamente en `tau` (§4).

**(I4) CDFs.** `partial_tau F1(1) = 0`, `partial_tau F2(v_q) = 0` (§5).

Toda implementación futura de esta ruta deberá verificar (I1)–(I4) como comprobaciones
fail-closed, con tolerancias que fijará su propio contrato; (I1) es puntual en cada rebanada, no
solo en promedio, y es por tanto mucho más exigente que (I2).

## 9. Finitud y regularidad de `E[s^2]` (ítem 6)

**Lema 9.1.** Sobre `K = [1.0,1.2] x Omega`, con `Omega = [0,1] x [v_p,v_q]` (dominio fijo,
cerrado y acotado — §4):

**(a) `htilde` acotada entre constantes positivas.** `r in [0.5, 3.2]` (Lema 2.4) sobre todo `K`.
En ese rango, `W'(tau,r) = (r/tau^2)exp(r/tau)` es composición de funciones elementales continuas
y estrictamente positivas de `(tau,r) in [1.0,1.2] x [0.5,3.2]` (compacto), luego alcanza en él un
mínimo y un máximo positivos finitos: `0 < W'_min <= W' <= W'_max < infty`. Además
`r_tau(U,v)` es `C^infty` en `(tau,U,v)` por el teorema de la función implícita, ya que
`partial_r Utilde = -exp(-v/2tau)W' < 0` está separado de cero sobre `K` (mismo argumento de
compacidad, aplicado a `exp(-v/2tau)W'`). Por tanto `htilde(tau,w,v) = exp(v/2tau)/W'(tau,r) *
DeltaU(tau)` es `C^infty` y, siendo un cociente de funciones continuas positivas acotadas
(`exp(v/2tau)` acotada en `[exp(v_p/2*1.2), exp(v_q/2*1.0)]`, `DeltaU(tau)>0` continua en el
compacto `[1.0,1.2]` luego acotada entre extremos positivos por Lema 2.2), está acotada entre dos
constantes positivas sobre todo `K`.

**(b) `f1, f2` acotadas lejos de cero — argumento de compacidad completo (cierra el hueco
señalado explícitamente por el PI: que `r` esté acotado no basta por sí solo).** El argumento
tiene cuatro pasos, cada uno necesario:

1. *Continuidad.* `f1(tau,w) = (1/A(tau)) integral_{v_p}^{v_q} htilde(tau,w,v) dv` es continua en
   `(tau,w)` — integral de un integrando continuo (por (a)) sobre un intervalo de longitud fija
   `v_q-v_p`, con `A(tau)` continua y positiva (integral de `htilde>0` sobre `Omega`, compacto).
2. *Positividad estricta.* `htilde>0` en todo punto de `K` (cociente de exponenciales y `W'>0`,
   sin ceros posibles — ninguna resta, ningún cambio de signo). Luego `f1(tau,w)>0` para todo
   `(tau,w)`: es la integral de una función estrictamente positiva y continua sobre un intervalo
   de longitud positiva fija, luego estrictamente positiva (no puede anularse por cancelación,
   porque no hay signos opuestos que cancelar).
3. *Dominio compacto.* `(tau,w) in [1.0,1.2] x [0,1]` es cerrado y acotado, incluidos los bordes
   `w=0,1` (que son los bordes `x=0,1` del cuadrado unidad, tras la identificación de rangos de
   §4 — no son un límite abierto excluido, son parte del dominio cerrado).
4. *Conclusión (compacidad elemental).* Una función continua y estrictamente positiva sobre un
   conjunto compacto alcanza un mínimo, y ese mínimo es estrictamente positivo (si fuera `<=0`
   contradiría la positividad puntual en el punto donde se alcanza). Luego existe
   `m_1 > 0` con `f1(tau,w) >= m_1` para todo `(tau,w) in [1.0,1.2] x [0,1]`, y análogamente
   `f2(tau,v) >= m_2 > 0` para todo `(tau,v) in [1.0,1.2] x [v_p,v_q]`, con cotas superiores
   `f1 <= M_1 < infty`, `f2 <= M_2 < infty` por el mismo argumento aplicado al máximo.

**(b′) Corolario — acotación de `a1, a2` (los denominadores nombrados explícitamente por el
PI).** `a1(w) = -partial_tau F1(w)/f1(w)`: el numerador `partial_tau F1(w) =
integral_0^w f1(w')(E[D|w']-E[D]) dw'` es una integral, sobre un intervalo de longitud a lo sumo
1, de un integrando acotado (`f1` acotada por (b); `E[D|w'], E[D]` acotadas por ser promedios de
`D`, que es acotada por ser función continua de cantidades acotadas — ver (a) y §3), luego
`partial_tau F1(w)` está uniformemente acotada en valor absoluto por alguna constante `C_1<infty`.
El denominador `f1(w) >= m_1 > 0` por (b). Luego `|a1(w)| <= C_1/m_1 < infty` uniformemente en
`w in [0,1]`, **incluidos los extremos `w=0,1`** (no solo en el interior). Simétricamente,
`|a2(v)| <= C_2/m_2 < infty` uniformemente en `v in [v_p,v_q]`, incluidos `v=v_p,v_q`. **No hay,
por tanto, ninguna singularidad de borde en `a1, a2` ni en `sigma`** cuando `(x,y) -> (0,1)` en el
cuadrado unidad: esos bordes corresponden exactamente a `w in {0,1}`, `v in {v_p,v_q}`, que están
cubiertos por la misma cota uniforme sobre el dominio cerrado, no excluidos de ella.

**(c)** `F1, F2` son estrictamente crecientes con derivada `f1, f2` separada de cero por (b),
luego `Q1=F1^{-1}, Q2=F2^{-1}` son `C^infty` (teorema de la función inversa, aplicable porque la
derivada no se anula en ningún punto del dominio cerrado).

**(d)** Todas las integrales paramétricas de §5 son de integrandos continuos sobre compactos
(por (a)–(b)), luego diferenciables bajo el signo integral y `C^infty` en `tau`.

**Consecuencia.** `sigma` está acotada sobre `K` (suma y producto de piezas acotadas: `D, E[D|w],
E[D|v], E[D]` acotadas por (a); `a1, a2` acotadas por (b′); `partial_w g, partial_v g` acotadas
por diferencia de cantidades acotadas), y

```text
I(tau) = E_{c_tau}[ s_tau^2 ] < infty,   I(.) es C^infty en [1.0, 1.2],
```

el supremo `Ibar` se alcanza y es finito. Las condiciones de finitud son exactamente las
verificadas: straddle (Lema 2.2), contención de la raíz en `[0.5, 3.2]` (Lema 2.4), `DeltaU > 0`,
y la cadena de compacidad continuidad-positividad-dominio-cerrado de (b)-(b′), que cubre
explícitamente los bordes `w,v` (equivalentemente `x,y -> 0,1`) y no solo el interior. **Para
esta familia concreta no existe singularidad matemática de dominio ni de score, ni en el interior
ni en el borde del cuadrado unidad**: si una implementación futura dispara
`DOMAIN_OR_SCORE_SINGULARITY`, será un defecto de implementación, no del objeto. La suavidad
`C^infty` en `tau` es además la base de regularidad que la envolvente del diseño §7 necesita
(cotas de derivada entre nodos), aunque su construcción queda fuera de este documento.

## 10. Normalización por `dv` y régimen del Anexo C (ítem 8)

El Anexo C (§4b, `wp4_comparable_pair_separation.md:281,292`) fija el requisito del defeater y la
heurística `[UNVERIFIED]` de escala:

```text
zeta_1 * Ibar >= kappa^2 dv^2 / 54,   zeta_1 = 1/36 + O(dv^2)  (Thm C9),
heurística: Ibar ~ C dv^2.
```

**Nota de desambiguación:** el `kappa(r_p,r_q)` del Anexo C es el coeficiente de separación de
`p(tau)`; el `kappa = V*I` de `wp4_kappa_numeric_reference.py` es la cantidad del floor de
localización (WP4-floor §5a). Son objetos distintos con el mismo nombre; todo documento posterior
debe escribir `kappa_sep` y `kappa_loc` si los usa a la vez.

Cantidades normalizadas que cualquier diagnóstico futuro debe reportar **junto a** las brutas:

```text
sigma_hat = sigma / dv,        I_hat(tau) = I(tau) / dv^2,
defeater normalizado:  Ibar_hat >= kappa_sep^2 / (54 * zeta_1) = (2/3) kappa_sep^2 * (1 + O(dv^2)).
```

El criterio de lectura del diagnóstico queda así protegido contra el error señalado en la
revisión del PI: un score puntual de orden `10^-2` con `dv = 0.02` es **compatible con
dependencia regular** (`sigma_hat = O(1)`); solo `I_hat` mucho menor que la escala
`(2/3) kappa_sep^2` indicaría una supresión adicional de información de forma más allá del límite
de independencia. Ninguna evaluación puntual finita demuestra "score uniformemente minúsculo";
esa conclusión requeriría una cota superior certificada de `I_hat`, no muestras.

**Esbozo estructural (no probado aquí; obligaciones listadas).** La derivada exacta
`partial_v log h|_U = tau/(2r^2)` da la representación factorizada

```text
h(U,v) = h(U, v_p) * exp( integral_{v_p}^v tau/(2 r_tau(U,v')^2) dv' ),
```

cuya parte no aditiva en `(U,v)` está controlada por la derivada mixta
`partial^2_{Uv} log h = (tau/r^3) exp(v/2tau)/W'`, acotada sobre `K` (§9). Integrada sobre la
banda de anchura `dv`, la interacción log-densidad es `O(dv)`; el doble centrado de §6 anula las
partes aditivas, lo que sugiere `sigma = O(dv)` y por tanto `I = O(dv^2)`, en línea con la
heurística del Anexo C. Quedan como obligaciones de una prueba futura, marcadas `[UNVERIFIED]`:
(a) una cota explícita `sup |sigma| <= C dv` vía las cotas de §9, incluyendo los términos de
cuantil `a1, a2`; (b) su uniformidad en `tau` sobre `[1.0,1.2]`.

## 11. Qué elimina esta ruta y qué conserva

Elimina, respecto del estimador cerrado por `NUMERICAL_NONCONVERGENCE`:

1. la diferencia finita en `tau` y con ella el factor amplificador `4/d^2 = 4e4`;
2. la resta de dos densidades casi idénticas (cancelación catastrófica);
3. PCHIP y toda inversión de cuantiles (solo CDFs hacia delante);
4. la escalera `D` completa (queda un único eje de refinamiento: el espacial);
5. la diferenciación numérica a través de `brentq` (las derivadas de la raíz son cerradas, §2).

Conserva: la definición exacta de `I(tau)` e `Ibar` (contrato §1); `brentq` como evaluador de la
raíz (no diferenciado); la exigencia de dos rutas independientes y terminales fail-closed que
deberá fijar el contrato futuro; y la prohibición de identificar un máximo de malla con `Ibar`.

## 12. Frontera de este documento

```text
derivación (este documento) -> auditoría documental -> decisión del PI
  -> [si procede] diagnóstico numérico acotado en dev/ con contrato propio
  -> [si procede] contrato ejecutable confirmatorio nuevo + auditoría + autorizaciones separadas
```

- Este documento no concede `IMPLEMENTATION_AUTHORIZATION` ni `EXECUTION_AUTHORIZATION`.
- No modifica el contrato Hellinger cerrado, su terminal, ni los estados
  `IBAR_DIAMOND_INTERVAL` / `CONSTANT_LEVEL_DEFEATER`.
- Ningún resultado futuro de esta ruta cambia etiquetas científicas sin auditoría e instrucción
  posterior del PI.
- Alcance científico: esta ruta sirve únicamente al ítem de eficiencia constante de `S_n`
  (defeater del Anexo C §6). No toca el cuello de botella mayor identificado por el PI (la
  ausencia de un objeto local específicamente sensible al horizonte) ni nada de 3+1D.
