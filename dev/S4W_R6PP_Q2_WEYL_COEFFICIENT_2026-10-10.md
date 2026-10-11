# S4W / R6″ pregunta 2 — `F3`/`F4` se disuelve, y el coeficiente del candidato era correcto

**Fecha:** 2026-10-10
**Autorizado por:** el PI, tras la retirada del no-go (`30f7fda`)
**Encargo:** la única pregunta viva — manteniendo `U_y` dentro de la integral, ¿sale el coeficiente de orden `rho^{-1/2}` proporcional al invariante `C^2`, o sobrevive la mezcla dependiente del observador?
**Fuentes:** Wang arXiv:1904.01034 ecs. (2), (76)–(77) y (79); Pfeiffer 2022 §3.4.1

```text
ANALYTIC_RESULT / NO_SIMULATION / NO_SEEDS / SEAL_UNTOUCHED
TRUNCACION: orden ALGEBRAICO R^2 — ∇Riem y ∇∇Riem fuera de orden (ver §7.3)
BLIND-REVIEWED (3 casas): grok-4.6 CONFIRMADO / gpt-6-astra CONFIRMADO_CON_CORRECCIONES /
                          deepseek-v4-pro REFUTADO (objecion verificada y fallida) — ver §7, §8
```

---

## 0. Veredicto

```text
R6_PRIMEPRIME_Q2_LOCAL = PROPORTIONAL_TO_K        <- establecido, 3 casas
COEFICIENTE_DE_W       = CERO EN EL CANAL rho^{-1/2}   <- no "en todo", ver §8 defecto 2
F3 / F4                = SE DISUELVEN AL ORDEN ALGEBRAICO LOCAL
C_W1_COEFFICIENT       = DETERMINADO               <- la auditoria lo tenia en FAIL

NO ESTABLECIDO (rev.2, defecto material de Astra):
  el RESTO global o(rho^{-1/2}), y por tanto la formula completa para E[B_*1].
  La prueba heredada de W2 = O(rho^{-1}) pasa cotas de norma suprema por un operador
  diferencial que NO preserva desigualdades.  Ver §8.3.
```

```
coeficiente local algebraico, orden R^2, canal rho^{-1/2}:

    -(73 sqrt6 / (1575 pi)) · C_abcd C^abcd

y NO, como decia la rev.1 de este documento:
    E[B_*1] = -(73 sqrt6/(1575 pi)) C^2 rho^{-1/2} + o(rho^{-1/2})
porque el control del resto no esta demostrado (§8.3).
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
- `F3`/`F4` caen **al orden algebraico local**: la pieza dependiente del observador no
  contribuye al canal `rho^{-1/2}`.

> **Corregido en rev.2 (defecto material de Astra, §8.3).** La rev.1 decía aquí que «caen `F1`,
> `C0` y `F3`/`F4`» y que «sobreviven sólo los fallos documentales». **Afirmaba de más.** `F1`
> y `C0` dependen de que `W2 = O(rho^{-1})`, y esa prueba —heredada de Pfeiffer (3.15)–(3.22)—
> tiene un paso inválido. Siguen abiertos: el resto global, la uniformidad cerca de `u=0`, y la
> definición de `B_*1` sobre un pasado no compacto.

**Sigue prohibido**, y esto no lo toca nada de lo anterior — es la frontera de claims del brief:

```
NO afirmar: convergencia realizacion-por-realizacion; varianza finita o controlada;
            detector practico de horizonte; Page-Shoom discreto; reconstruccion de
            Schwarzschild; emergencia del cono causal; prioridad sin auditoria bibliografica.
```

Lo calculado es **el valor medio sobre sprinklings**, `E[B_* 1]`. Belenchia–Benincasa–Dowker ya
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



---

## 7. Revisión ciega — **las dos casas discrepan**

`revisiones/2026-10-10-r6pp-q2/`. Entrada idéntica para las dos (302 KB): este documento, el
no-go retirado, R6′, la auditoría y la tesis de Pfeiffer.

| casa | P1 | P2 | P3 | P4 | veredicto |
|---|---|---|---|---|---|
| `grok-4.6` | CORRECTA | CORRECTA | CORRECTA | CORRECTA | **`CONFIRMADO`** |
| `deepseek-v4-pro` | INCORRECTA | INCORRECTA | INCORRECTA | CORRECTA | **`REFUTADO`** |

**Hay que decirlo así: no hay unanimidad.** Es la primera vez en las cuatro rondas del día.

### 7.1 La objeción de DeepSeek, y por qué no se sostiene

Sostiene que `C^{ga}_{mn} y^m y^n = 0` por antisimetría, luego la primera forma cuártica sería
nula, y da como contraejemplo `u=v`.

Es una **lectura equivocada de los índices**. En Wang, `C^{ga}_{mn}` significa
`C^g{}_m{}^a{}_n = C_{gamma mu alpha nu}`: los pares antisimétricos son `(gamma mu)` y
`(alpha nu)`, y las `y` contraen el **segundo** slot de cada par, no dentro de un par. Se ve en
su propia ec. (6), de la que (76) sale contrayendo `alpha` con `beta`:
`R^gamma_{mu alpha nu} R_{gamma rho beta sigma} x^mu x^nu x^rho x^sigma`. El cálculo usa esa
estructura.

Y su contraejemplo se refuta evaluándolo: en `u=v` el vector `y` es puramente temporal, luego
`C_{gamma 0 alpha 0} = E_{gamma alpha}` y `Q = E^2 (y^0)^4 != 0`. Verificado:

```
evaluacion directa  4pi E^2 (y^0)^4 |_{u=v}  =  16 pi E^2 u^4
el polinomio de §1  8pi W u^4 + pi K u^4     =  16 pi E^2 u^4        IDENTICOS
```

> **Corregido en rev.2 (Astra, defecto 1).** La rev.1 escribía `32 pi u^4 E^2` en las dos
> líneas. El `32` era el coeficiente de la **forma reducida**
> `e1^2+e1 e4+e2^2+e3^2+e4^2+e5^2` que devuelve `sympy`, no el de `E^2`, que vale el doble:
> `E^2 = 2(e1^2+e1 e4+e2^2+e3^2+e4^2+e5^2)`. El cálculo era correcto; la prosa confundía las dos
> normalizaciones, de modo que el control **tal como estaba escrito** no era el control que el
> documento decía haber hecho. Corregido a `16`, y la identidad se verifica.

(porque `8pi(E^2+B^2) + 8pi(E^2-B^2) = 16 pi E^2`). El contraejemplo, bien evaluado,
**confirma** la fórmula. Y Grok la rederiva por otra vía (§7.2), lo que la hace triplemente
independiente: fuerza bruta, identidad de Bel–Robinson, y control en el eje.

Lo que sí vale del informe de DeepSeek: confirma `P3` para la vía (ii′) de forma independiente,
y descarta que el régimen de boost grande sea el problema —*"las integrales angulares
convierten los `gamma^4` en polinomios finitos y `W1` es compacta"*—, que era una de las dudas
declaradas en §6.

### 7.2 La derivación de Grok, mejor que la mía

```
Q  =  (1/2) T(y^4)  +  (K/16) (y·y)^2          con  (y·y)^2 = (2uv)^2 = 4 u^2 v^2
```

De ahí, en dos líneas: `int dOmega Q = (8pi/5) W (u^4+...+v^4) + pi K u^2 v^2`. Y explica **por
qué** la cancelación de §1 ocurre: la pieza uniforme *es* `T(y^4)`, y el único añadido no
uniforme es `K (y·y)^2`, que es puro `u^2 v^2` y puro invariante. Toda cuártica isótropa
construida con Weyl² es combinación de esas dos. Adoptada: es más comprobable a mano que mi
contracción bruta.

### 7.3 Defectos de Grok, incorporados

1. **Truncación de Riemann congelado no declarada.** Todo el cálculo evalúa la curvatura en `x`
   y descarta `∇Riem`, que es de otro orden. Queda declarado aquí: la línea entera trabaja a
   orden **algebraico** `R^2`, con `∇Riem` y `∇∇Riem` fuera. Las ecs. (6) y (36) de Wang los
   llevan explícitos y no se han usado.
2. **Wang arXiv:1904.01034 no iba en el lote enviado.** Las ecs. (76)–(77) y (79) se heredan de
   la transcripción ya auditada (auditoría §3.2, y `N1`/`N2` confirmadas por las dos casas en
   la ronda de R6″), no de lectura directa en esta ronda. Es la misma laguna de higiene que la
   auditoría §6.5 señaló: ninguna de las cinco fuentes del brief está en `biblioteca/`.
3. La exhaustividad del recuento de vías a orden `R^2` **sigue siendo mía**. Grok la revisa y la
   da por buena —`alpha+beta` impar muere por paridad, `l>=2` es `R^4`, `W2` está en
   `O(rho^{-1})` con cinco capas— pero no la prueba.

### 7.4 Cómo leer la discrepancia

El desempate no es un voto: es que la objeción de DeepSeek es verificable y falla al
verificarla, mientras la de Grok aporta una derivación independiente que coincide. Dicho eso,
un resultado **positivo** que reproduce al dígito el número que el autor del candidato quería
obtener, con una casa en contra, no debería promocionarse sobre dos revisiones. Si esto va a
sostener algo, pide una tercera casa (`astra` o `gemini` en `revision-ciega`) — decisión del PI.

---

## 8. (rev.2) Tercera casa: Astra — `CONFIRMADO_CON_CORRECCIONES`

Pedida por el PI como desempate. `revisiones/2026-10-10-r6pp-q2-astra/`, `gpt-6-astra` vía
`codex exec`, sellado. **Diferencia con las dos rondas anteriores: el artículo de Wang iba en
el lote** —en extracción de texto, `biblioteca/derived-md/Wang_2019_…md`, sha256 del original
`4f682665…59dc1`—, así que pudo verificar las ecuaciones en la fuente en vez de heredar la
transcripción. Era la laguna que Grok había declarado.

Recuento final de las tres casas:

| casa | veredicto | sobre `P0`/`P1` (el punto en disputa) |
|---|---|---|
| `grok-4.6` | `CONFIRMADO` | correcta, con derivación propia `Q = T/2 + K(y·y)²/16` |
| `gpt-6-astra` | `CONFIRMADO_CON_CORRECCIONES` | **correcta, verificada en el original de Wang** |
| `deepseek-v4-pro` | `REFUTADO` | incorrecta — objeción verificada y fallida (§7.1) |

### 8.1 Lo que Astra añade a favor

Verificó `P0` en el original y además **rederivó el `-1/180` de Wang (76) desde su ec. (6)**,
por una vía que no estaba en ningún documento: con `g = eta + h_2 + h_4 + …`,

```
(1/2) tr h_4  =  (1/45) Q ,      -(1/4) tr(h_2^2)  =  -(1/36) Q ,      suma = -(1/180) Q
```

Comprobado aquí: `1/45 - 1/36 = 4/180 - 5/180 = -1/180`. Con eso, la objeción de nulidad por
antisimetría queda descartada desde la fuente, no por mi lectura. El coeficiente local y la
cancelación de `W` en el canal quedan confirmados por las **tres** casas en sustancia.

### 8.2 Correcciones menores, aplicadas

1. **El `32` debía ser `16`** en el control de §7.1. Aplicado, con la explicación.
2. **Alcance de la cancelación.** `(v-u)^2 S_4 = u^6 - u^5 v - u v^5 + v^6`: desaparecen los
   coeficientes interiores —incluido `u^3 v^3`— pero **no el polinomio entero**. La frase «la
   medida aniquila cualquier reparto uniforme» hay que restringirla a **la proyección sobre el
   canal relevante**, y no vale como «la contribución de `W` al valor medio es cero». Corregido
   en §0.
3. **§3 no explicitaba el signo negativo** de la inserción exponencial, que va absorbido en el
   `+41 pi^2 K/226800`. Queda dicho.
4. **El argumento de paridad de R6′ §1 es falso como se escribió.** La integración angular
   elimina un número impar de componentes **espaciales**, no un grado total impar: un término
   `t^3` sobrevive. No añade ninguna vía a orden `R^2` —eso lo confirma Astra por homogeneidad,
   las dos vías tienen `alpha+beta = 4`— pero el argumento auxiliar no vale.
5. **La truncación `∇∇Riem` estaba mal justificada.** No es «de otro orden»: aparece al **mismo**
   grado cuártico en Wang (6). La justificación correcta es otra: en vacío exacto la traza
   correspondiente del determinante se reduce a derivadas de Ricci y se anula, y para el volumen
   Wang ya trató esas contribuciones antes de (79).

### 8.3 El defecto material: la prueba de `W2` que R6′ heredó no vale

Y esto sí cambia el alcance de todo el día.

La prueba de `W2 = O(rho^{-1})` con cinco capas descansa en los pasos (3.15)–(3.22) de
Pfeiffer, que **trasladan valores absolutos y cotas de norma suprema a través de un operador
diferencial**. Un operador diferencial no preserva desigualdades. Que `A_{lambda,l}` anule la
integral de un monomio es correcto; que anule una cota obtenida sustituyendo funciones por sus
normas supremas **no se sigue**, y la identidad (3.17) no lo legitima.

Astra da un ejemplo funcional: una amplitud positiva y acotada que contenga `U^3 log U`, con
fase `V = U^2 f_0`, produce

```
int U^3 log U e^{-rho f_0 U^2} dU  =  -log(rho)/(4 f_0^2 rho^2)  +  cte/rho^2  +  resto exp.
```

y la cuarta raíz convierte ese logaritmo en una contribución de orden `rho^{-1/2}`. No es un
contraejemplo geométrico Ricci-flat suave —lo dice él mismo—, pero demuestra que las hipótesis
de **mera acotación** no bastan. Haría falta una expansión transversal con regularidad
suficiente, y hay que proporcionarla.

Consecuencias, y hay que asumirlas:

- **`B_W2` de R6′ baja** de `PASS_CONDITIONAL` a `PASS_CONDICIONADO_A_UNA_PRUEBA_QUE_FALTA`.
- **`F1` y `C0` no están cerrados.** Dependen de ese `O(rho^{-1})`.
- Queda abierta la **uniformidad de los restos cerca de `u=0`**: el resto de Wang está formulado
  para diamantes pequeños a orientación fija, y que las coordenadas sean compactas no es lo
  mismo que acotar un resto expresado en variables de boost cuando `U_y` tiende a nula.
- Y `B_*1` sobre un pasado **no compacto** no está definido: Pfeiffer presupone soporte compacto.

### 8.4 Dónde queda esto, dicho sin adornos

**Establecido, y por tres casas:** el coeficiente local algebraico a orden `R^2` en el canal
`rho^{-1/2}` vale `-73 sqrt6/(1575 pi)` por `C_abcd C^abcd`, la pieza dependiente del observador
no contribuye a ese canal, y es el número que el candidato había escrito.

**No establecido:** que eso sea el valor medio completo con resto `o(rho^{-1/2})`. Ese salto
—del coeficiente local al enunciado global— es el exceso que la rev.1 cometió y que Astra
identificó. De los cinco fallos de la auditoría, `F3`/`F4` caen al orden local; `F1` y `C0`
**vuelven a estar abiertos**, ahora por una razón distinta y más profunda que la original: no
falta un cálculo, falta una prueba en la literatura de la que todo esto cuelga.

Récord del día, para que conste: cuatro rondas, tres casas, y en las cuatro me corrigieron algo.
En tres de ellas tenían razón. En la cuarta —la objeción de antisimetría de DeepSeek— no, y hizo
falta una tercera casa con la fuente delante para zanjarlo.
