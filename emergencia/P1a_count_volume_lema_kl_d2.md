# P1a — Cierre formal de `P_{1,n}` y aislamiento de `P_{2,n}` (`d=2`)

> **ESTADO: `PROVED` PARA `P_{1,n}` · CANAL `fixed-n`, `d=2` ·
> PIEZA BETA-PRODUCTO ÚNICAMENTE · SIN EJECUCIÓN NUMÉRICA NUEVA.**
>
> El resultado probado es uniforme respecto de la ley de formas seleccionadas.
> `P_{2,n}` queda definido, pero no resuelto. No se reabre ningún gate.

## 0. Enunciado

Fíjense `n`, un lado `h in {PAST,FUTURE}` y el evento `S` de selección única de
`MIN_COVERAGE_LEX`, con `P_n(S)>0`. Se suprime `h,S` de la notación cuando no hay
ambigüedad. Si `T=(K,L)` es la forma del intervalo seleccionado y `ell` su duración
relativa normalizada, entonces

```text
P_{1,n} := E[ Var(ell | T,n,h,S) | n,h,S ]
           <= (n+1/4)/(n+1)^2
           <= 1/n.
```

Por tanto `P_{1,n} -> 0`. La convergencia es uniforme respecto de cualquier ley
seleccionada de `T` compatible con el experimento. La prueba no usa `w_n`, balance
de la forma, no degeneración asintótica ni simulación.

## 1. Experimento, selector y variables

El experimento congelado en
`P1a_count_volume_experimento_condicionado_d2.md` §1 y
`P1a_contrato_representaciones_alternativas_d2.md` §2 es

```text
(U_i,V_i) iid Uniform([0,1]^2), i=1,...,n, condicionado a N=n,
x_i prec x_j  iff  U_i<U_j y V_i<V_j,
ds^2 = du dv,
ell(x,y) = sqrt((U_y-U_x)(V_y-V_x)) in [0,1].
```

La normalización es la del cuadrado unidad; `ell` es una duración relativa y
adimensional, no una escala propia absoluta.

El poset queda representado por la permutación `Pi` que asigna a cada rango en `U`
el rango en `V`. El selector examina cuádruplas
`q=(a,b,c,d)` con `a prec b prec c prec d` y con los dos intervalos cerrados de
cardinalidad al menos tres. Maximiza lexicográficamente

```text
( min(m_-(q),m_+(q)), m_-(q)+m_+(q) )
```

y solo observa la cuádrupla ganadora `q*` cuando es única; ese es el evento `S`.
Tanto `S` como `q*`, las cardinalidades `m_-,m_+` y todos los rangos son funciones
de `Pi`.

Para el lado pasado, escribiendo

```text
alpha=rank_U(a), beta=rank_U(b),
alpha'=rank_V(a), beta'=rank_V(b),
K=beta-alpha, L=beta'-alpha', M=m_-(q*),
```

se tiene

```text
Delta U = U_(beta)-U_(alpha),
Delta V = V_(beta')-V_(alpha'),
ell = sqrt(Delta U Delta V).
```

El lado futuro es idéntico sustituyendo `(a,b)` por `(c,d)`. En adelante
`T=(K,L)` significa la forma **del lado fijado**; no la cuádrupla completa.

### 1.1 Dominio real y bordes

Los rangos de endpoints comparables son estrictamente crecientes, luego `K,L>=1` y
los casos `K=0` o `L=0` tienen probabilidad cero y no pertenecen al soporte. Además,
el contrato exige `M>=3` en ambos lados. Cada intervalo contiene por tanto al menos
un punto interior, lo que fuerza `K,L>=2` en el lado considerado y también gaps de
al menos dos rangos en el otro lado. Entre ambos lados hay al menos un gap porque
`b prec c`. En consecuencia, si `S` ocurre,

```text
n >= 6,                 2 <= K,L <= n-4.
```

La prueba analítica se formula en el sobreconjunto `1<=k,l<=n`, donde las Betas
siguen siendo propias. Esto cubre todo el soporte seleccionado y deja claro que no
se ha eliminado ningún borde por conveniencia.

## 2. Ley Beta-producto bajo el selector

### 2.1 Independencia rango–magnitud

Los vectores de muestras `(U_i)_{i=1}^n` y `(V_i)_{i=1}^n` son independientes. Para
una muestra iid continua, su permutación de rangos es uniforme e independiente de
sus estadísticos de orden: al particionar el dominio según los `n!` órdenes
posibles, la densidad es la misma en cada región y la ordenación no altera la
densidad conjunta de los valores ordenados. Sean `R_U,R_V` esas dos permutaciones
de rangos. La independencia de los vectores de coordenadas implica que `R_U,R_V`
son independientes entre sí y conjuntamente independientes de ambos vectores de
estadísticos de orden. Como `Pi=R_V circ R_U^{-1}`, se obtiene

```text
Pi perp (U_(1),...,U_(n), V_(1),...,V_(n)),
(U_(1),...,U_(n)) perp (V_(1),...,V_(n)).
```

### 2.2 Ley de los gaps

Para los estadísticos de orden uniformes, los `n+1` spacings, incluidos los dos
bordes, tienen ley `Dirichlet(1,...,1)`: la densidad conjunta de
`U_(1)<...<U_(n)` es la constante `n!`, y el cambio triangular a spacings tiene
Jacobiano uno y lleva el dominio al simplex. La propiedad de agregación se prueba
con la representación `D_i=E_i/sum_j E_j`, donde `E_0,...,E_n` son exponenciales
iid: las sumas disjuntas son Gamma independientes. Así, la suma de `k` componentes
y la suma de las `n+1-k` restantes forman una `Dirichlet(k,n+1-k)`. Por tanto, para
`1<=i<j<=n`,

```text
U_(j)-U_(i) ~ Beta(j-i,n+1-j+i).
```

### 2.3 Condicionamiento por selección

Fíjese `Pi=p` compatible con `S`. El selector y los rangos de los endpoints quedan
entonces determinados, mientras que la ley de las magnitudes ordenadas no cambia
por la independencia de §2.1. Si la forma lateral es `T=(k,l)`, §2.2 y la
independencia entre coordenadas dan

```text
X_k := Delta U ~ Beta(k,n+1-k),
Y_l := Delta V ~ Beta(l,n+1-l),
X_k perp Y_l,
ell = sqrt(X_k Y_l).
```

Esta ley depende de `p` solo mediante `(k,l)`. Mezclar sobre todos los `p`
compatibles con un mismo `(T,M,S)` no la cambia. En particular,

```text
L(ell | T=(k,l),M=m,n,h,S) = L(ell | T=(k,l),n,h,S)
                            = L(sqrt(X_k Y_l)).                 (2.1)
```

Así queda verificada la hipótesis del resultado condicionado existente
(`P1a_count_volume_ley_condicionada_d2.md` §§4 y 7): la selección modifica la ley
de la forma, no la geometría condicionada por una forma fija.

## 3. Identidades exactas

Para `X_k~Beta(k,n+1-k)`, la fórmula de momentos de una Beta da

```text
E[X_k] = k/(n+1),

E[sqrt(X_k)]
  = B(k+1/2,n+1-k)/B(k,n+1-k)
  = Gamma(k+1/2) Gamma(n+1) / (Gamma(k) Gamma(n+3/2)).          (3.1)
```

Defínase

```text
R(k,n) := (E[sqrt(X_k)])^2 / E[X_k]
        = [ Gamma(k+1/2) Gamma(n+1)
            / (Gamma(k) Gamma(n+3/2)) ]^2 * (n+1)/k.           (3.2)
```

No hay desplazamiento de índices: el segundo parámetro es `n+1-k` porque el gap
entre los rangos `i<j` agrega `k=j-i` de los `n+1` spacings.

Por independencia de `X_k,Y_l`,

```text
E[ell^2 | k,l] = E[X_k]E[Y_l] = kl/(n+1)^2,

E[ell | k,l]^2
  = E[sqrt(X_k)]^2 E[sqrt(Y_l)]^2
  = kl R(k,n)R(l,n)/(n+1)^2.
```

Restando se obtiene algebraicamente, no mediante una malla,

```text
Var(ell | k,l)
  = kl/(n+1)^2 * (1-R(k,n)R(l,n)).                            (3.3)
```

## 4. Paso especial de Wendel: prueba autocontenida

Para `x>0` defínase

```text
A(x) := Gamma(x+1/2)^2 / (x Gamma(x)^2).
```

Primero se prueba la única desigualdad gamma necesaria. La función `Gamma` es
log-convexa en `(0,infinity)`: para `a,b>0` y `0<theta<1`, Hölder aplicado a la
integral de Euler da

```text
Gamma(theta*a+(1-theta)*b)
 <= Gamma(a)^theta Gamma(b)^(1-theta).
```

Con `theta=1/2`, los pares `(x,x+1)` y `(x+1/2,x+3/2)` dan respectivamente

```text
Gamma(x+1/2)^2 <= Gamma(x)Gamma(x+1) = x Gamma(x)^2,

Gamma(x+1)^2 <= Gamma(x+1/2)Gamma(x+3/2)
              = (x+1/2)Gamma(x+1/2)^2.
```

Como `Gamma(x+1)=x Gamma(x)`, ambas desigualdades equivalen a

```text
x/(x+1/2) <= A(x) <= 1,        x>0.                           (4.1)
```

Esta es exactamente la especialización `s=1/2`, elevada al cuadrado, de la
desigualdad habitualmente atribuida a Wendel. La prueba anterior es autocontenida;
la referencia bibliográfica verificada es J. G. Wendel, *Note on the Gamma
Function*, **American Mathematical Monthly** 55(9) (1948), 563–564,
[doi:10.2307/2304460](https://doi.org/10.2307/2304460).

De (3.1)–(3.2),

```text
R(k,n) = A(k)/A(n+1).
```

Como `A(n+1)<=1` y `A(k)>=k/(k+1/2)`, se concluye para todo `1<=k<=n`:

```text
R(k,n) >= A(k) >= k/(k+1/2).                                 (4.2)
```

## 5. Cota puntual uniforme

Por Cauchy–Schwarz, `0<R(k,n)<=1`. Sean `a_k=k/(k+1/2)` y
`a_l=l/(l+1/2)`. Por (3.3), (4.2) y la positividad de todos los factores,

```text
Var(ell | k,l)
 <= kl/(n+1)^2 * (1-a_k a_l).
```

La igualdad algebraica

```text
kl(1-a_k a_l)
 = ((k+l)/2+1/4) * k/(k+1/2) * l/(l+1/2)
```

produce

```text
Var(ell | k,l)
 <= [((k+l)/2+1/4)/(n+1)^2]
    * [k/(k+1/2)] * [l/(l+1/2)].                            (5.1)
```

Para `1<=k,l<=n`, se tiene `k+l<=2n` y cada uno de los dos últimos factores está
en `(0,1)`. Luego

```text
Var(ell | k,l) <= (n+1/4)/(n+1)^2.                           (5.2)
```

Finalmente, para `n>0`,

```text
n(n+1/4) <= (n+1)^2
```

porque la diferencia es `7n/4+1>0`. Por tanto

```text
sup_{1<=k,l<=n} Var(ell | k,l)
 <= (n+1/4)/(n+1)^2
 <= 1/n.                                                       (5.3)
```

El soporte seleccionado real `2<=k,l<=n-4` es un subconjunto de este dominio. La
cota incluye, con margen, cualquier forma extremadamente desbalanceada admisible.

## 6. Integración sobre la ley seleccionada: cierre de `P_{1,n}`

Sea

```text
w_n^h(s|S) = P(T=s | n,h,S)
```

la ley marginal de la forma del lado fijado. Es una probabilidad sobre un soporte
finito, aunque no se conozca su expresión. Por (2.1) y (5.2),

```text
P_{1,n}
 := E[ Var(ell | T,n,h,S) | n,h,S ]
  = sum_s w_n^h(s|S) Var(ell | s)
 <= sum_s w_n^h(s|S) (n+1/4)/(n+1)^2
  = (n+1/4)/(n+1)^2
 <= 1/n.                                                       (6.1)
```

La expectativa no pierde el condicionamiento por `T`: promedia varianzas
condicionadas. Tampoco se escribe `P_{1,n}=E_s(1/n)`; `1/n` es una cota puntual,
no el integrando. Como (6.1) vale para toda probabilidad `w_n^h`, el resultado es
uniforme respecto de la ley de formas y `P_{1,n}->0`.

```text
P1_STATUS = PROVED
P1_RATE_UPPER_BOUND = O(1/n)
P1_REQUIRES_W_N = NO
P1_REQUIRES_BALANCE_OR_NONDEGENERACY = NO
```

## 7. Descomposición correcta y único objetivo posterior `P_{2,n}`

`M` y `T=(K,L)` son funciones de la permutación `Pi`, pero **no se supone que `M`
sea función del par `T`**. De hecho, la ley hipergeométrica del candidato fijado en
`P1a_count_volume_ley_condicionada_d2.md` §5 muestra por qué la forma lateral no
determina algebraicamente el conteo. La sigma-álgebra correcta para refinar el
condicionamiento es siempre

```text
sigma(M) subseteq sigma(M,T).
```

Aquí `M` es la cardinalidad del intervalo causal cerrado del lado seleccionado,
incluidos sus extremos: `M=m_-(q*)=|I[a,b]|` en `PAST` y
`M=m_+(q*)=|I[c,d]|` en `FUTURE`. En cambio, `K,L` son los gaps discretos entre
los rangos de esos extremos en las dos coordenadas; no son extensiones nulas
continuas ni están determinados algebraicamente por `M`.

Defínase, usando la ley Beta-producto,

```text
mu_n(s) := E[ell | T=s,n,h,S]
         = E[sqrt(X_k)] E[sqrt(Y_l)],       s=(k,l),

v_n(s)  := Var(ell | T=s,n,h,S).
```

La identidad (2.1) da la independencia condicional necesaria:

```text
E[ell | M,T,n,h,S]   = mu_n(T),
Var(ell | M,T,n,h,S) = v_n(T).
```

La ley de varianza total, primero dentro de cada valor de `M` y después promediada
sobre `M`, da rigurosamente

```text
Var(ell | M,n,h,S)
 = E[v_n(T) | M,n,h,S]
   + Var(mu_n(T) | M,n,h,S),

E[Var(ell | M,n,h,S) | n,h,S]
 = P_{1,n} + P_{2,n},                                         (7.1)

P_{2,n}
 := E_M[ Var_T(mu_n(T) | M,n,h,S) | n,h,S ].                  (7.2)
```

Si

```text
w_n^h(s|m,S) = P(T=s | M=m,n,h,S),
```

entonces el objetivo analítico equivalente es

```text
P_{2,n}
 = sum_m P(M=m | n,h,S)
   * { sum_s w_n^h(s|m,S) mu_n(s)^2
       - [sum_s w_n^h(s|m,S) mu_n(s)]^2 }.                    (7.3)
```

### 7.1 Reducción escalar: basta el `pushforward` por `sqrt(KL)`

Escribiendo

```text
g_n(k) := E[sqrt(X_k)],
```

la identidad (3.2) equivale a

```text
g_n(k)^2 = k R(k,n)/(n+1).
```

Todos los factores son positivos, luego

```text
mu_n(k,l)
 = sqrt(kl)/(n+1) * sqrt(R(k,n)R(l,n)).                       (7.4)
```

Defínase el estadístico simétrico

```text
H_n(k,l) := sqrt(kl)/(n+1).
Z_n := H_n(K,L) = sqrt(KL)/(n+1).
```

Por §5, `0<R(k,n)<=1`; por (4.2),
`R(k,n)>=k/(k+1/2)`. Para `a,b in [0,1]` se tiene
`sqrt(ab)>=ab` y `1-ab<=(1-a)+(1-b)`. Por tanto, uniformemente para
`1<=k,l<=n`,

```text
0 <= H_n(k,l)-mu_n(k,l)
   = H_n(k,l) [1-sqrt(R(k,n)R(l,n))]
  <= H_n(k,l) [(1-R(k,n))+(1-R(l,n))]
  <= H_n(k,l) [1/(2k)+1/(2l)]
   = [sqrt(l/k)+sqrt(k/l)]/[2(n+1)]
  <= 1/(2sqrt(n)).                                            (7.5)
```

La última desigualdad usa que, si `1<=k,l<=n`, el cociente entre el mayor y el
menor no supera `n`; la función `t+1/t` es creciente para `t>=1`, de modo que el
máximo es `sqrt(n)+1/sqrt(n)=(n+1)/sqrt(n)`.

Sea

```text
Q_{2,n}
 := E_M[ Var_T(H_n(T) | M,n,h,S) | n,h,S ].                  (7.6)
```

En el espacio de probabilidad ya condicionado por `(n,h,S)`, sea
`P_M Z=E[Z|M,n,h,S]`. El operador `I-P_M` es la proyección ortogonal sobre el
complemento de las variables `sigma(M)`-medibles y es una contracción en `L^2`.
Así,

```text
sqrt(P_{2,n}) = ||(I-P_M)mu_n(T)||_2,
sqrt(Q_{2,n}) = ||(I-P_M)H_n(T)||_2.
```

La desigualdad triangular inversa, la contracción y (7.5) dan

```text
|sqrt(P_{2,n})-sqrt(Q_{2,n})|
 <= ||(I-P_M)(mu_n(T)-H_n(T))||_2
 <= ||mu_n(T)-H_n(T)||_2
 <= 1/(2sqrt(n)).                                             (7.7)
```

Como `mu_n(T),H_n(T) in [0,1]`, Popoviciu da
`P_{2,n},Q_{2,n}<=1/4`. Multiplicando (7.7) por
`sqrt(P_{2,n})+sqrt(Q_{2,n})<=1`, se obtiene además

```text
|P_{2,n}-Q_{2,n}| <= 1/(2sqrt(n)).                           (7.8)
```

Finalmente, al ser `H_n(K,L)=sqrt(KL)/(n+1)`,

```text
Q_{2,n}
 = E_M[Var(sqrt(KL) | M,n,h,S)]/(n+1)^2.                     (7.9)
```

De (7.7)–(7.9) se siguen las equivalencias asintóticas rigurosas

```text
P_{2,n}->0
 iff Q_{2,n}->0
 iff E_M[Var(sqrt(KL) | M,n,h,S)] = o(n^2),                  (7.10)

liminf P_{2,n}>0 iff liminf Q_{2,n}>0.                       (7.11)
```

Por (7.8), de hecho `P_{2,n}` y `Q_{2,n}` tienen el mismo `liminf`. La ley
bidimensional completa `w_n^h(k,l|m,S)` no es necesaria para decidir (7.10) o
(7.11): basta su `pushforward` escalar por `(k,l) -> sqrt(kl)`. Esto es una
caracterización asintótica del término de riesgo `P_{2,n}` mediante `Z_n`, no una
afirmación de que `Z_n` sea un estadístico suficiente en sentido formal para la ley
finito-muestral completa.

#### 7.1.1 La concentración de `K` es solo un criterio suficiente

La recurrencia gamma en (3.1) da

```text
g_n(k+1)/g_n(k) = (k+1/2)/k = 1+1/(2k).
```

Como `0<=mu_n<=1` y el soporte condicionado por `M=m` satisface
`k,l>=m-1`, telescopar en cada coordenada produce

```text
|mu_n(k,l)-mu_n(k',l')|
 <= [|k-k'|+|l-l'|]/[2(m-1)].                                (7.12)
```

Aplicando `Var(Z)=E[(Z-Z')^2]/2` a dos formas condicionalmente independientes y
`(a+b)^2<=2a^2+2b^2`,

```text
Var(mu_n(T)|M=m,n,h,S)
 <= [Var(K|M=m,n,h,S)+Var(L|M=m,n,h,S)]/[2(m-1)^2].           (7.13)
```

El intercambio de coordenadas manda la permutación uniforme a su inversa, conserva
el poset, el score, `M` y la unicidad `S`, y permuta `K,L`; por ello sus varianzas
condicionales coinciden. Integrando (7.13),

```text
P_{2,n}
 <= E_M[Var(K|M,n,h,S)/(M-1)^2].                             (7.14)
```

Esta condición es suficiente, pero no necesaria. Una ley con masa `1/2` en
`(a,b)` y `1/2` en `(b,a)` puede tener `Var(K)=Theta(n^2)`, mientras que
`mu_n(a,b)=mu_n(b,a)` y su contribución a `P_{2,n}` es cero. El objeto intrínseco
es la dispersión condicional de `sqrt(KL)`, no la de cada coordenada por separado.

### 7.2 Qué contienen los artefactos existentes

La inspección, sin ejecutar nada, muestra que
`resultados/p1a_representaciones_intervalos_d2.csv` registra `M` y `ell`, pero no
`K,L` ni `T`; `resultados/p1a_enumeracion_exacta_d2.csv` registra estados y
probabilidades del selector, pero tampoco formas. La derivación existente deja
explícitamente `w_n^h(s|m,S)` sin calcular. Por tanto los runs actuales no permiten
separar `P_{2,n}` de la varianza condicional total ni decidir su asintótica.

El paso mínimo posterior es caracterizar o acotar la ley condicional unidimensional
de `Z_n=sqrt(KL)/(n+1)` dado `(M,n,h,S)`. Solo si este `pushforward` no puede
controlarse directamente será necesario caracterizar la ley bidimensional completa
`w_n^h(s|m,S)`. En particular, exhibir dos formas con el mismo `m` no prueba una
obstrucción persistente: una cota `liminf P_{2,n}>0` requiere masa no evanescente y
separación cuantitativa de `sqrt(kl)/(n+1)`.

Ni siquiera es obligatorio construir toda la tabla del `pushforward`. Si

```text
C_n^h(m,r) := #{pi : S(pi), M_h(pi)=m, K(pi)L(pi)=r},
```

entonces normalizar `C_n^h(m,r)` sí daría su ley completa, pero para `Q_{2,n}`
basta obtener directamente, por ejemplo mediante una recurrencia o función
generatriz, los dos momentos

```text
E[Z_n | M=m,n,h,S],    E[Z_n^2 | M=m,n,h,S].
```

Las dos rutas analíticas prioritarias —no una dicotomía exclusiva ni exhaustiva— son:

1. concentración condicional de `sqrt(KL)/(n+1)`, que por (7.10) implica
   `P_{2,n}->0`; junto con (6.1), el estimador de Bayes
   `E[ell|M,n,h,S]` reconstruye la duración relativa con error cuadrático tendente a
   cero;
2. separación persistente con masa no evanescente en el `pushforward`, que por
   (7.11) implica `liminf P_{2,n}>0` y una obstrucción persistente para la
   reconstrucción basada solo en `M`.

También son posibles comportamientos no cubiertos por esas dos rutas, por ejemplo
oscilaciones entre subsecuencias o convergencia a cero sin una ley simple. No se
presentan concentración y separación como clasificación exhaustiva.

El alcance negativo se obtiene exactamente de la proyección de Bayes:

```text
inf_f E[(ell-f(M))^2 | n,h,S]
 = E[Var(ell | M,n,h,S) | n,h,S]
 = P_{1,n}+P_{2,n},                                           (7.15)
```

donde el ínfimo recorre las funciones `sigma(M)`-medibles de cuadrado integrable.
Como `P_{1,n}->0` y (7.10) caracteriza `P_{2,n}->0`, si `Q_{2,n}` no converge a
cero no existe reconstrucción consistente de `ell` basada solo en `M`. Para una
obstrucción persistentemente positiva hace falta la condición más fuerte
`liminf Q_{2,n}>0`. Ninguno de los dos enunciados excluye estimadores que usen otra
información de la cuádrupla ganadora o del poset completo.

Ninguna obstrucción del canal `sigma(M)` es un no-go para el poset completo ni para
orden+número.

```text
P2_STATUS = OPEN
CHARACTERIZATION_BY_Z_N = PROVED
VAR_K_CRITERION = SUFFICIENT_NOT_NECESSARY
NEXT_OBJECTIVE = CONDITIONAL_PUSHFORWARD_LAW_OF_SQRT_KL
```

## 8. Techo de afirmación

El cierre de `P_{1,n}` controla solo el ruido Beta-producto dentro de una forma en
el canal `fixed-n`, `d=2`. No demuestra:

- `P_{2,n}->0` ni ninguno de los otros desenlaces de §7;
- el escalado del residual completo de (7.1);
- una meseta de `rho_max`;
- ningún resultado sobre `a_n=Var(Y_n)`;
- consistencia fuera del estimando lateral seleccionado;
- escala temporal absoluta, tiempo propio general u horizontes;
- nada para `d>2`, el canal de Poisson o el poset completo.

No modifica los gates congelados de `COUNT_VOLUME`, ratio, dimensiones superiores
o ejecución numérica.

## 9. Controles previos y estado final

Las mallas y tablas numéricas preexistentes son controles de transcripción de
(3.2)–(5.3); no intervienen en ninguna implicación de la prueba. En esta auditoría no
se ejecutó ningún script, test científico, simulación ni generador de artefactos.

```text
P1_BETA_PRODUCT_UNDER_SELECTION = PROVED
P1_ACTUAL_SELECTED_DOMAIN = 2<=k,l<=n-4 (n>=6, condicionado a S)
P1_GAMMA_IDENTITY = PROVED_ALGEBRAICALLY
P1_WENDEL_SPECIAL_CASE = PROVED_SELF_CONTAINED
P1_UNIFORM_BOUND = PROVED
P1_INTEGRATED_BOUND = PROVED_UNIFORM_IN_w_n
P1_STATUS = PROVED
P2_STATUS = OPEN
CHARACTERIZATION_BY_Z_N = PROVED
VAR_K_CRITERION = SUFFICIENT_NOT_NECESSARY
NEXT_OBJECTIVE = CONDITIONAL_PUSHFORWARD_LAW_OF_SQRT_KL
NEW_RUNS = NONE
NEW_ARTIFACTS = NONE
NEW_SCRIPTS = NONE
GATES_REOPENED = NONE
NOVELTY_CERTIFIED = NO
```
