# S4W / R6″ pregunta 2 — `F3`/`F4` se disuelve, y el coeficiente del candidato era correcto

**Fecha:** 2026-10-10
**Autorizado por:** el PI, tras la retirada del no-go (`30f7fda`)
**Encargo:** la única pregunta viva — manteniendo `U_y` dentro de la integral, ¿sale el coeficiente de orden `rho^{-1/2}` proporcional al invariante `C^2`, o sobrevive la mezcla dependiente del observador?
**Fuentes:** Wang arXiv:1904.01034 ecs. (2), (76)–(77) y (79); Pfeiffer 2022 §3.4.1

```text
ANALYTIC_RESULT / NO_SIMULATION / NO_SEEDS / SEAL_UNTOUCHED
INDEPENDENT_REVIEW_REQUIRED — no tomar por firme hasta §7
```

---

## 0. Veredicto

```text
R6_PRIMEPRIME_Q2 = PROPORTIONAL_TO_K
COEFICIENTE_DE_W = EXACTAMENTE CERO          <- en las DOS vias, por separado
F3 / F4          = SE DISUELVEN
C_W1_COEFFICIENT = DETERMINADO               <- la auditoria lo tenia en FAIL
```

```
E[B_* 1](x)  =  -(73 sqrt6 / (1575 pi)) · C_abcd C^abcd · rho^{-1/2}  +  o(rho^{-1/2})
```

**Es, exactamente, la fórmula que el §7 del candidato escribía con signo de interrogación.**
Y el estimador normalizado que proponía, `K_hat = -(1575 pi/(73 sqrt6)) rho^{1/2} B_*1`, es el
correcto.

El `73` no se ha ajustado a nada: sale de `(105 + 41)/2`, donde `105` viene de la vía (i)
—calculada de la ec. (76) de Wang— y `41` de la vía (ii′) —calculada de su ec. (79)—, por
separado y sin mirar el número del candidato hasta el final.

---

## 1. La razón estructural de que `W` desaparezca

Ésta es la pieza conceptual, y es sencilla una vez vista.

Las dos formas cuárticas que intervienen, integradas sobre ángulos y expresadas en los
invariantes `K = 8(E^2-B^2)` y `W = E^2+B^2` (con `E`, `B` **genéricas**, no Schwarzschild):

```
int dOmega  C^{ga}_{mn} C_{gras} y^m y^n y^r y^s
      = (8pi/5) W · (u^4 + u^3 v + u^2 v^2 + u v^3 + v^4)   +   pi K · u^2 v^2

int dOmega  T_{abcd} y^a y^b y^c y^d
      = (16pi/5) W · (u^4 + u^3 v + u^2 v^2 + u v^3 + v^4)
```

**La parte `W` entra con coeficiente UNIFORME** sobre los cinco monomios. Y la medida de la
región cercana es `[(v-u)/sqrt2]^{d-2} = (v-u)^2/2` en `d=4`, con

```
(v-u)^2 = v^2 - 2uv + u^2        coeficientes  1, -2, 1   ->   SUMAN CERO
```

Luego **la medida aniquila cualquier reparto uniforme**. Lo único que sobrevive es el exceso no
uniforme, que en la primera forma está en `u^2 v^2` y es **puro `K`**; y en la segunda no hay
exceso, así que la vía (ii′) sólo aporta por su término `K` explícito.

Esto resuelve la tensión que la auditoría no sabía resolver: el integrando **es**
manifiestamente dependiente del observador y crece como `gamma^4` —la rapidez no está acotada
en `W1`, `tanh eta = (v-u)/(v+u)`—, y sin embargo el resultado es invariante, porque el factor
`(v-u)^{d-2}` de la medida mata exactamente la pieza direccional. No es una conspiración del
peso integrado: es una cancelación algebraica de tres términos.

Consistente, además, con que `T_{abcd}` sea sin traza en vacío 4D: la pieza direccional no
tiene por dónde sobrevivir.

---

## 2. Vía (i) — el `y^4` de `sqrt(-g)`, sector `l = 0`

`sqrt(-g) = 1 - (1/180) Q(y)` (Wang ec. 76–77). Multiplicando por `(v-u)^2/2` y extrayendo el
canal diagonal `u^3 v^3`:

```
u^3 v^1  x  v^2    ->   +4pi W/5
u^2 v^2  x  -2uv   ->   -pi(5K + 8W)/5
u^1 v^3  x  u^2    ->   +4pi W/5
                   ------------------
                        -pi K          (la parte W: 4/5 - 8/5 + 4/5 = 0)
```

y con el `-1/180`: coeficiente del canal `= +pi K/180`. **Parte `W` = 0.**

## 3. Vía (ii′) — el `O(R^2)` propio del volumen, sector `l = 1`

`eps_2 = u^2v^2 · 41K/151200  +  688 · T(y,y,y,y)/604800`, de la ec. (79) con
`l_W = sqrt(uv/2)`. Multiplicado por `V_0 = (pi/6)u^2v^2` y por la medida, el canal diagonal
`u^5 v^5` da

```
coeficiente = 41 pi^2 K / 226800        parte W = 0
```

La parte `T` se cancela por el mismo mecanismo de §1: su reparto es uniforme.

## 4. Ensamblado

Con el `rho^l` **dentro** del operador (la corrección de `30f7fda`), la simetrización
triangular→cuadrado `1/2` de Pfeiffer (3.36) y el jacobiano `1/4` de `x=u^2, y=v^2`:

```
Ô_*[rho^0 G_1] = -1/(2 s^2)        Ô_*[rho^1 G_2] = -1/(c s^2)          s = c_4 rho , c_4 = pi/6

via (i)    :  rho^{3/2} · (8 sqrt6/3) · (1/2) · (1/4) · (pi K/180)        · (-1/(2s^2))
              = - sqrt6 K / (30 pi sqrt(rho))          = -105 sqrt6 K/(3150 pi sqrt(rho))
via (ii')  :  rho^{3/2} · (8 sqrt6/3) · (1/2) · (1/4) · (41 pi^2 K/226800) · (-1/(c_4 s^2))
              = -41 sqrt6 K / (3150 pi sqrt(rho))

suma       :  -(105+41) sqrt6 K/(3150 pi sqrt(rho))  =  -73 sqrt6 K/(1575 pi sqrt(rho))
```

---

## 5. Qué queda establecido y qué sigue prohibido

**Establecido** (a reserva de §7):

- El coeficiente local de `C^2` existe, es `a`-independiente (R6′ §2: el corte lo aniquila la
  cuarta raíz) y vale `-73 sqrt6/(1575 pi)`.
- La contribución dependiente del observador es **exactamente cero**, no pequeña.
- Con ello caen `F1` (ya en `30f7fda`), `C0` y `F3`/`F4`. De los cinco fallos de la auditoría
  sobreviven sólo los documentales: `F5`, la prioridad (`Ô_*` es el `O_6` de Dowker–Glaser, y
  el programa está publicado en 2301.13525).

**Sigue prohibido**, y esto no lo toca nada de lo anterior — es la frontera de claims del brief:

```
NO afirmar: convergencia realizacion-por-realizacion; varianza finita o controlada;
            detector practico de horizonte; Page-Shoom discreto; reconstruccion de
            Schwarzschild; emergencia del cono causal; prioridad sin auditoria bibliografica.
```

Lo calculado es **el valor medio sobre sprinklings**, `E[B_* 1]`. Benincasa–Dowker–Dowker ya
advierten que las fluctuaciones del operador minimal crecen con la densidad; nada aquí dice que
las del de cinco capas no lo hagan. Un coeficiente correcto en la media no es un estimador
utilizable.

## 6. Lo que no he verificado

- Que no haya otras combinaciones `(l, alpha+beta)` a orden de curvatura `R^2` que caigan en
  `rho^{-1/2}`. Las dos revisiones de R6″ confirmaron la clasificación en dos vías, y los
  canales con `alpha+beta` impar mueren por paridad, pero el recuento es mío.
- La cadena de normalización `b_0`, prefactor `rho^{(d+2)/d}` y `c_4` más allá de lo que
  verificó la auditoría §1.
- Las fluctuaciones. Nada.

## 7. Revisión ciega — PENDIENTE

Este documento **no es firme**. Va a DeepSeek y a Grok por separado, como los tres anteriores.
Récord del día: de tres rondas, las dos casas me corrigieron en las tres, y en una de ellas
retiré un no-go completo. Un resultado positivo que confirma exactamente el número que el autor
del candidato había escrito es precisamente el tipo de resultado que más conviene someter a
otra familia antes de creérselo.
