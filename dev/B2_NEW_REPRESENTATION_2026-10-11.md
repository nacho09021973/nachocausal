# B2 — representación nueva de `Delta_max`: tiempo propio 2D, calibración y geodésica

**Fecha:** 2026-10-11
**Autorizado por:** el PI («buscamos una nueva representación»).
**Sondas:** `dev/explore_b2_calibration_band.py` (banda por par),
`dev/explore_b2_gate_ideal_interval.py` (intervalo ideal de `S`). Diagnóstico, **no certificado**:
tablas en coma flotante, sin redondeo dirigido. Guardarraíles intactos (`t0`, curva y puntos
congelados; sin búsqueda sobre `lambda`).

```text
BANDA [recta, CS]               anchura mediana 3.5e-2
BANDA [geodésica, calibración]  anchura mediana 3.6e-5        (~1000x más estrecha)
S_ideal(t0) con la banda nueva = [+0.00276, +0.00346]          EXCLUYE CERO
drho/dt(t0) ideal              = [+0.0142, +0.0179]            signo positivo
rho(t0) ideal                  = [0.02016, 0.02055]
ESTADO: la compuerta firmada TIENE AHORA UNA REPRESENTACIÓN QUE PUEDE PASARLA.
        No hay certificado. Construirlo requiere autorización.
```

---

## 1. La observación

B1.2 §2 define

```text
Delta_max(x,y) = min(pi, sup_U  int q(U(V)V) sqrt(U'(V)) dV),   U monótona.
```

Eso es exactamente el **tiempo propio máximo** entre `x` e `y` en la métrica lorentziana 2D

```text
ds² = F(w) dU dV,     F = q²,   w = UV.
```

(Es el sector radial de Schwarzschild reescalado por `1/r²`.) En coordenadas `(w, nu) = (UV, ln V)`
la métrica es `F(w)(dw dnu − w dnu²)`: no depende de `nu` —el boost es Killing— y es regular a
través de `w = 0`. La representación anterior no usaba nada de esta estructura.

## 2. Cota superior: calibración de Hamilton–Jacobi

Para una tangente causal futura, `a = nu' >= 0`, `b = w' − w nu' >= 0` (`b ∝ U'`), y
`dtau = sqrt(F a b)`. Para `W = c nu + Phi(w)`, por AM-GM,

```text
dW = Phi' b + (Phi' w + c) a  >=  2 sqrt(Phi'(Phi' w + c) a b)  >=  dtau
   siempre que  Phi' >= 0,  Phi' w + c >= 0,  4 Phi'(Phi' w + c) >= F.
```

La menor `Phi'` admisible es

```text
Phi_c'(w) = F(w) / (2 (c + sqrt(c² + F(w) w))),
```

válida donde `c² + F w >= 0` y `c + sqrt(...) > 0` (si el rectángulo causal cruza `w < 0`, eso
exige `c > 0` y `c² >= max(−F w)`). Entonces, para **todo** `c` válido en el rectángulo causal,

```text
Delta_max(x,y)  <=  c (nu_y − nu_x) + Phi_c(w_y) − Phi_c(w_x).
```

Es la integral completa de Hamilton–Jacobi con la constante de separación del boost. Cauchy–Schwarz
es un caso degenerado mucho más flojo: la calibración queda en mediana un **10 % por debajo** de CS.

**Propiedad que importa para certificar:** para `c` fijo, la cota es **separable** en `x` e `y`,
`A_c(y) − A_c(x)`. Eso es lo que permitiría reproducir el colapso por Fubini de B1.5.

## 3. Cota inferior: la geodésica de constante `c`

La igualdad en AM-GM fija `b/a`, lo que da la geodésica

```text
dw/dnu = 2w + c / Phi_c'(w) = 2w + 2c (c + sqrt(c² + F w)) / F,
```

creciente en `c`. Se dispara en `c` por bisección hasta llegar a `w_y` en `nu_y`, y su tiempo
propio, integrado a lo largo de la curva, es una cota inferior (toda curva admisible lo es). La
recta resultó estar ya muy cerca de la geodésica: la geodésica la mejora solo en un **+0.27 %**
en mediana. **La holgura de la banda antigua estaba casi entera en Cauchy–Schwarz.**

## 4. Resultados

Banda por par (1973 pares ordenados, muestreados uniformemente en el rectángulo de `t0`):

```text
pares con cota inferior > superior        0
anchura mediana  [recta, CS]              0.03455
anchura mediana  [geodésica, calibración] 0.0000361
anchura relativa mediana / máxima         1.3e-4 / 0.124
```

Las dos cotas se calculan por vías independientes (una curva explícita y una función de
calibración) y no se cruzan en ningún par: es el control de coherencia principal.

Intervalo ideal de `S = B' − 2(Z'/Z)B` en `t0` (la misma sonda que dio `[-0.00336, +0.01125]`
con la banda antigua):

| orden | `rho` | `S` | `drho/dt` |
|---|---|---|---|
| 16 | [0.020090, 0.020486] | [+0.002767, +0.003469] | [+0.01426, +0.01787] |
| 24 | [0.020157, 0.020553] | [+0.002758, +0.003464] | [+0.01421, +0.01785] |

Excluye cero con un margen de unas **4 veces** la anchura del intervalo. Coherente con todo lo
anterior: `rho` cae dentro de la envolvente de B2.1 (`[0.0195, 0.0347]`) y del intervalo ideal
antiguo (`[0.0198, 0.0310]`); el signo es el que indicaban B1.5 y B2.1, y `S` queda entre los dos
valores `+0.0029` y `+0.0050` que daban las cotas antiguas tomadas como exactas.

## 5. Qué falta para un certificado

Esto es un intervalo **ideal en coma flotante**, no una envolvente certificada. Construirla exige:

1. **Capa escalar de `Phi_c`**: integral 1D de `F/(2(c+sqrt(c²+Fw)))` con redondeo dirigido. Usa
   solo el enclosure de `s(w)` que B1.5 ya tiene, sin Lambert W.
2. **Colapso del par**: con `c` fijo por bloque, la cota superior `A_c(y) − A_c(x)` es separable, y
   `p(a) <= a²/4` la convierte en productos de integrales 1D, como en B1.5 §3. Falta diseñar la
   asignación de `c` por bloque y medir cuánto ensancha.
3. **Cota inferior**: la geodésica depende del par y **no** es separable. Hay que encontrar la forma
   de no discretizar el par en 4D. Una posibilidad, sin explorar: curvas de una familia que
   dependa solo del bloque, como el anclaje de B1.5. Es el punto difícil.
4. **Margen disponible**: el ensanchamiento total de 1–3 debe quedar por debajo de `~0.0028` en `S`
   (unas 4 veces la anchura ideal). Es un presupuesto medible antes de construir nada.

Nada de esto está autorizado. Sí lo está —y es lo que esta nota registra— que la compuerta firmada
deja de estar agotada: con esta representación, su intervalo ideal excluye cero.

## 6. Adenda: la geodésica no hace falta

Misma sonda, orden 16, con la banda `[recta, calibración]`, es decir, la cota inferior antigua de
siempre y solo la superior nueva:

```text
rho in [0.019661, 0.020486]   B in [0.003816, 0.003976]   B' in [0.008886, 0.009925]
S_ideal(t0) = [+0.002419, +0.003718]        EXCLUYE CERO
```

Esto disuelve el «punto difícil» de §5.3: la recta, que B1.5 ya certifica, basta como cota
inferior. Además solo hace falta `S_lo > 0`, y eso pide la cota **inferior** de `Delta` únicamente
en las tres caras con `v_n > 0` (integrales 3D, cara × volumen); en `B` (4D) y en la cara `V=v1`
solo entra la **superior**, que es la separable. Presupuesto de ensanchamiento para un
certificado: `~0.0024` en `S`, del orden de un 15 % combinado sobre `B` y `B'`.
