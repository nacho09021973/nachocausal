# S4W / R6″ — EL NO-GO SE RETIRA: el logaritmo sí se anula

**Fecha:** 2026-10-10
**Estado:** `WITHDRAWN_BY_AUTHOR_AFTER_BLIND_REVIEW`
**Autorizado por:** el PI, tras R6′ (`dev/S4W_R6PRIME_W1_CHANNEL_2026-10-10.md`, commit `e4d9365`)
**Revisión ciega:** `revisiones/2026-10-10-r6primeprime/` — **las dos casas, por separado: `REFUTADO`**

```text
R6_PRIMEPRIME_Q1       = ZERO            (el no-go afirmaba NOT_ZERO: era FALSO)
NOGO                   = WITHDRAWN
S4W_W1_LOG_REMAINDER   = RESUELTO — la cuarta raiz lo quita en TODO el canal (3,3), para todo l
S4W_5LAYER_ESTIMATOR   = SIGUE BLOQUEADO, pero solo por F3/F4 (no por F1)
```

---

## 0. Qué pasó, en claro

Este documento afirmaba que el coeficiente del logaritmo de la vía `(ii')` valía **10** y que
por tanto el estimador divergía como `log(rho)`. **Es falso.** El coeficiente físico es **cero**
y el estimador no diverge.

**El error.** Apliqué `Ô_*` a `G_2(s)` cuando el objeto físico es `Ô_*[rho^l G_mu(s)]`: el
`rho^l` que sale del desarrollo de la exponencial es función de `rho` y **va dentro** de la
acción del operador. Pfeiffer (3.35) lo escribe literalmente —`Ô_d rho^l e^{-rho c_d (uv)^{d/2}}`—
y la prueba estructural es que la `l` aparece **dentro** de `A_{kappa+1,l}(n)` y dentro de
`kappa = (2/d)(k+1)+l-1`: si `rho^l` fuese un prefactor constante, `l` no podría estar ahí.

**La consecuencia, y es mayor que el error.** El `rho^l = (s/c)^l` cancela exactamente las
`s^{-l}` de más de `G_{l+1}`, así que **todos** los sectores `l` del canal diagonal `(3,3)`
tienen potencia efectiva `s^{-2}`:

```
l=0:  (1 log s + C)/s^2        ->  Ô_* = -1/(2 s^2)       sin log
l=1:  (2 log s + C)/(c s^2)    ->  Ô_* = -1/(c s^2)       sin log
l=2:  (6 log s + C)/(c^2 s^2)  ->  Ô_* = -3/(c^2 s^2)     sin log
l=3:  (24 log s + C)/(c^3 s^2) ->  Ô_* = -12/(c^3 s^2)    sin log
```

Y la formulación limpia es la tercera vía: los logaritmos salen del **primer** término de
(3.43), el que multiplica `A_{kappa+1,l}(n) = prod_{zeta=0}^{n} 2(zeta-k)`, que se anula si y
sólo si `k <= n` — **condición que no involucra `l`**. El canal `(3,3)` tiene `k = 3`, luego con
cinco capas (`n=3`) queda aniquilado para todo `l`; con el minimal (`n=2`) sobrevive.

**Luego `F1` no estaba abierto: estaba resuelto, y por el propio operador de cinco capas.** Esto
corrige también a R6′, que había concluido que `l >= 1` quedaba contaminado: es el mismo error,
cometido en R6′ y heredado aquí.

**La contradicción estaba dentro de mis propios documentos**, y es lo que Grok nombró: R6′ §1
usa el `rho^{l-mu-1}` de (3.43) para demostrar que el orden en `B̄` **no depende de `l`**, y
R6′ §2 aplica `Ô_*` a `G_mu ~ s^{-(2+l)}` **sin** el `rho^l`. Las dos cosas no pueden ser a la
vez: la independencia en `l` del orden **es** el enunciado de que `rho^l G_{1+l} ~ (log s)/s^2`.
Tenía el hecho correcto en §1 y lo contradije en §2.

## 0.1 Lo que sí queda establecido, y es el resultado útil de esta ronda

Las dos casas confirmaron `N1` (conversión de convenciones) y `N2` (canal y coeficiente), que
son las partes caras de la cuenta. Sobreviven:

- `eps_2 = u^2 v^2 (41K + 688W)/151200`, con el control exacto
  `V_plano(l_W=sqrt(uv/2)) = (pi/6)u^2v^2 = V_0` de Pfeiffer.
- La vía `(ii')` alimenta un **único** monomio diagonal `u^5 v^5` con coeficiente
  `+pi rho (41K+688W)/907200`. Sin cancelación interna.
- Lo que sobrevive a orden `rho^{-1/2}` es, por tanto, un resto **finito** —no logarítmico—
  proporcional a `41K + 688W`, conviviendo con la vía `(i)` limpia.

Y un hecho nuevo que aporta la revisión y que afila `F3`/`F4`:

```
41 K + 688 W  =  1016 E^2 + 360 B^2
```

**definida positiva**. Luego el contaminante **no puede anularse punto a punto** y no es
proporcional a `K`. En Schwarzschild estático (`B=0`) vale `127 K`. La cota de Grok
`W >= |K|/8` da `41K+688W >= 45|K|` en el peor caso y `>= 127K` si `K>0`.

Mi argumento de "inmunidad a `F3`/`F4`" era **incorrecto en su forma** —un escalar más un
término direccional sí puede cancelarse al integrar, así que "`K` es escalar" no basta— y
además era innecesario: sin logaritmo, la inmunidad no cerraba nada. Lo que lo reemplaza es
mejor: la combinación es definida positiva.

## 0.2 Y lo que queda, que es una sola pregunta

```
R6'' PREGUNTA 2 (la unica viva).  Mantener U_y DENTRO de la integral en (u,v) -- su rapidez
  va como (v-u)/(v+u), luego W NO se factoriza fuera, cosa que este documento hizo mal
  (defecto 4 de Grok) -- y calcular si el peso integrado de 1016 E^2 + 360 B^2, sumado a la
  via (i) limpia, da algo proporcional a K.
    Siendo la combinacion definida positiva, no hay cancelacion punto a punto posible: solo
    una conspiracion del peso integrado salvaria al estimador.  La expectativa honesta sigue
    siendo negativa, pero ahora por F3/F4 y con un resto FINITO, no por una divergencia.
  Es analitico.  No necesita simulacion ni semillas.
```

Queda también anulada la discusión del `O_10` de siete capas de la versión retirada: con las
potencias correctas, los dos sectores que importan ya son `s^{-2}` y la cuarta raíz del de cinco
capas les quita el logaritmo. El candidato no se quedó corto de capas.

---

> **Lo que sigue (§1-§6) es el texto retirado, conservado como registro del error.** `N1` y
> `N2` (§1 y §2) son correctos y las dos casas los confirmaron. `N3` y `N4` (§3 y §4) contienen
> el error del `rho^l`, y §5 el del `O_10`. No se borran.

---

## 1. `eps_2`: la corrección de volumen a `O(R^2)` en vacío

De Wang ec. (79) en `d = 4`, con `D^2 = 4E^2` y la identidad de la auditoría
`2032E^2 + 360H^2 = 82K + 1376W`:

```
V_plano  = 2 pi l_W^4 / 3
delta V  = pi l_W^8 (41 K + 688 W) / 56700
eps_2    = delta V / V_plano = l_W^4 (41 K + 688 W) / 37800
```

**Control de convenciones, que es donde esto se podía torcer.** Pfeiffer usa `tau^2 = 2uv` y
`V_0 = c_4 (uv)^2` con `c_4 = pi/6`; Wang parametriza por el semitiempo propio `l_W`, con
`tau = 2 l_W`, luego `l_W = sqrt(uv/2)`. Sustituyendo:

```
V_plano(l_W = sqrt(uv/2)) = pi u^2 v^2 / 6 = V_0 de Pfeiffer      [VERIFICADO, identidad exacta]
eps_2 = u^2 v^2 (41 K + 688 W) / 151200
```

Las dos convenciones encajan exactamente. Sin este control el resto no valdría nada.

---

## 2. Qué canal alimenta, y con qué coeficiente

El término `l = 1` del desarrollo de `e^{-rho delta V}` aporta al integrando
`-rho V_0 eps_2`, multiplicado por la medida `[(v-u)/sqrt2]^{d-2} = (v-u)^2/2`. Con `phi = 1`
y una potencia de `C^2` ya gastada en `eps_2`, `sqrt(-g) -> 1`. Desarrollando:

| monomio | coeficiente | `(m,k)` con `l=1`, `d=4` | |
|---|---|---|---|
| `u^4 v^6` | `-pi rho (41K+688W)/1814400` | (4,2) | `rho^{-1}` |
| **`u^5 v^5`** | **`+pi rho (41K+688W)/907200`** | **(3,3)** | **diagonal, `rho^{-1/2}`** |
| `u^6 v^4` | `-pi rho (41K+688W)/1814400` | (2,4) ≡ (4,2) | `rho^{-1}` |

La diagonal la alimenta el **término cruzado** `-2uv` de `(v-u)^2`, con coeficiente no nulo y
proporcional a `41K + 688W`. No hay cancelación interna posible: es un único monomio.

---

## 3. La acción del operador, y el logaritmo que sobrevive

Con `x = u^2`, `y = v^2` el jacobiano da `u^5 v^5 du dv = (1/4) x^2 y^2 dx dy`, luego el canal
es `G_2`:

```
G_2(s) = [ A^2 s + (log(A^4 s^2) - 3 + 2 gamma_E) e^{A^2 s} - 2 e^{A^2 s} Ei(-A^2 s) + 3 ] e^{-A^2 s}/s^3
       = ( 2 log(s) + 4 log A - 3 + 2 gamma_E ) / s^3  +  (exponencialmente pequeño)
```

coeficiente del logaritmo **2**. Aplicando el operador de cinco capas:

```
Ô_* G_2 = 2 ( 15 log(s) + 30 log A - 61 + 15 gamma_E ) / (3 s^3)
```

```
coeficiente del logaritmo superviviente  =  10  !=  0
```

Era de esperar por R6′ §2: la potencia del canal es `s^{-3}` y `Ô_*` solo aniquila
`s^{-1/2}, s^{-1}, s^{-3/2}, s^{-2}`. Lo que R6″ añade es que el **prefactor tensorial** de ese
logaritmo tampoco se anula.

---

## 4. Ensamblado y no-go cuantitativo

```
contribución a B_bar  =  rho^{3/2} · b_0 · (integral angular) · coef(u^5v^5) · (1/4) · Ô_*[G_2]
```

con `b_0 = 8 sqrt6/3` (prefactor del operador de cinco capas, auditoría §1) y, para la **parte
invariante**, `integral angular = 4 pi` porque `K` es escalar. Resultado:

```
B_bar[1]  ⊃  [ 2 sqrt6 (41 K + 688 W) / (315 pi) ] · log(rho) · rho^{-1/2}
```

En vacío `R = 0`, de modo que el término de orden `rho^0` —el `-R/2` φ— **se desvanece**, y
este log-realzado queda como el primer término no nulo. Sobre el estimador del candidato:

```
K_hat_rho = -(1575 pi/(73 sqrt6)) rho^{1/2} B_*1
          = -(10/73) (41 K + 688 W) log(rho) + O(1)
          = -(410/73) K log(rho) - (6880/73) W log(rho) + O(1)
```

- **Diverge** como `log(rho)`. No es un problema de normalización: no hay reescalado que arregle
  una divergencia.
- El coeficiente de `K` es `-410/73 ≈ -5.616`, ni la magnitud ni el signo de un estimador de `K`.
- La razón entre contenido dependiente del observador e invariante es `688/41 ≈ 16.8`, el mismo
  número que la auditoría §3.2 ya había encontrado en `F3`. **El contaminante logarítmico y el
  problema de `U_y` son el mismo objeto**, como anticipaba R6′ §4.
- Comparado con la señal limpia que el candidato reclamaba, `-(73 sqrt6/1575 pi) C^2 rho^{-1/2}`:
  el término log-realzado es `10(41K+688W)/(73 C^2) · log(rho)` veces mayor. Con `C^2 = K` eso
  son `≈ 5.6 log(rho)` sólo de la parte invariante. A cualquier densidad de interés, decenas o
  centenas de veces la señal.

---

## 5. Qué queda cerrado, qué no, y el sucesor nombrado

El brief original (`S4W_5LAYER_INDEPENDENT_AUDIT_BRIEF.md`, pregunta C0) fijó el criterio:
si la contribución dependiente de la prescripción no es `o(rho^{-1/2})`, el estado se promueve.
Aquí es peor que no-`o(rho^{-1/2})`: es `log(rho) rho^{-1/2}`, **por encima** del orden
objetivo, con coeficiente calculado y no nulo.

De las tres salidas que quedaban, dos están cerradas y una **no**:

- **Con más capas SÍ se podría arreglar, y esto corrige un borrador previo de este documento.**
  La primera versión afirmaba que alargar el operador abre una torre infinita que no converge.
  **Es falso**, y conviene dejarlo escrito porque es el tipo de exceso que las dos revisiones
  anteriores ya habían corregido dos veces.

  En vacío `delta V = O(R^2)`, luego el sector `l` del desarrollo de la exponencial lleva orden
  de curvatura `R^{2l}`. **A orden exactamente `R^2` solo contribuyen `l = 0` y `l = 1`**; los
  `l >= 2` son `R^4` o más, fuera del orden. No hay infinitos sectores que limpiar: hay dos.

  Limpiarlos exige aniquilar `s^{-2}` (sector `l=0`) y `s^{-3}` (sector `l=1`), es decir las
  raíces `theta = -2` y `theta = -3`. Recorriendo la torre de Dowker–Glaser en `d=4`
  (raíces `theta = -(k+1)/2`, `k = 0..n`, y `n+2` capas):

  | operador | capas | raíces `theta` | sectores `l` limpios |
  |---|---|---|---|
  | `O_4` | 4 | −1/2, −1, −3/2 | ninguno |
  | `O_6` | 5 | … , −2 | `l=0`  ← el candidato |
  | `O_8` | 6 | … , −5/2 | `l=0` |
  | **`O_10`** | **7** | **… , −3** | **`l=0` y `l=1`** |

  Es decir: la raíz que hace falta no es la del `O_8` —que añade `theta=-5/2` y no sirve— sino
  la del **`O_10`, un operador de siete capas** en `d=4`. Mi borrador decía `O_8`; estaba mal.

  Lo que R6″ establece es que el de **cinco** capas no puede. Si el de siete lo consigue es una
  pregunta distinta y abierta, y tendría su propio precio: habría que reproducir para él todo
  lo que la auditoría §1 verificó para el de cinco (que sigue dentro de la familia GCD, que
  preserva la normalización (3c), que conserva `□ − R/2`), y además el canal `(3,3)` con `l=1`
  arrastra `82K + 1376W`, así que incluso limpio de logaritmo seguiría topando con `F3`/`F4`.
- **CERRADA: no se arregla con la orientación.** El coeficiente de `K` no depende de `U_y`, así
  que ninguna elección de marco ni ninguna integral angular lo anula.
- **CERRADA: no se arregla con el corte.** El término sobrevive con `log A` y sin él: el
  `log(rho)` está ahí para cualquier `a`.

Lo que sobrevive del candidato es exactamente lo que la auditoría ya había admitido en su §7:
un enunciado algebraico exacto sobre la familia GCD, más la propiedad asintótica de R6′ (la
cuarta raíz limpia el sector `l=0`). Nada físico. El estimador de Kretschmann **de cinco capas**
queda **refutado**, no pendiente.

Y queda una continuación con nombre y dirección, que es más de lo que la línea tenía esta
mañana: subir un escalón más la torre de Dowker–Glaser. Nótese la simetría con el hallazgo de
prioridad de la auditoría §6.1 —que `Ô_*` *era* el `O_6` usado en `d=4`—: el operador que
haría falta para `C^2` en `d=4` sería el `O_10`, el de `d=10` usado en `d=4`. Todo el asunto es
un paseo por esa torre, y el candidato se quedó dos peldaños corto.

---

## 6. Lo que este documento NO afirma

- No refuta el operador de cinco capas. Es un GCD legítimo con límite `□ − R/2`, verificado en
  la auditoría §1 y recontrolado en R6′ §3.
- No refuta la vía `(i)`: el `C^2` limpio del sector `l=0` existe, es `a`-independiente, y la
  cuarta raíz lo aísla. Lo que ocurre es que está **dominado** por el logaritmo de `(ii')`.
- No dice nada sobre si la integral angular de `W` colapsa a un invariante (`F3`/`F4`). La
  pregunta queda abierta y **ya no importa**: el argumento de §0 es inmune a su respuesta.
- **No cierra la línea entera**, sólo el estimador de cinco capas. El sucesor de siete capas
  (§5) queda explícitamente sin evaluar: ni respaldado ni descartado.
- No cierra el programa `nachocausal`, que ya estaba cerrado por el comité 049 el 2026-07-30.
