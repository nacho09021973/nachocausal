# S4W / R6′ — ¿limpia la cuarta raíz el canal local de `W1`?

**Fecha:** 2026-10-10
**Autorizado por:** el PI, tras la auditoría `dev/S4W_5LAYER_INDEPENDENT_AUDIT_2026-10-10.md` (rev. 2.1, commit `1e03a54`)
**Encargo:** `R6'` de esa auditoría §9, en la forma reescrita tras el defecto 5 de la revisión de Grok
**Maquinaria:** Pfeiffer 2022 §3.4.1, ecs. (3.34)–(3.43) y (3.50)–(3.52). PDF en `biblioteca/`, sha256 en `revisiones/2026-10-10-s4w-auditoria/fuente_pfeiffer2022.sha256`

**Estado:**

```text
ANALYTIC_RESULT / NO_SIMULATION / NO_SEEDS / SEAL_UNTOUCHED
REV 3 — ver el bloque de REVISION 3: el §2 contenia un error material, corregido
```
---

## REVISIÓN 3 — 2026-10-10, tras la revisión ciega de R6″

**Este documento contiene un error material, y lo corrige aquí sin borrarlo.**

Su §2 concluía que la cuarta raíz limpia **sólo** el sector `l=0` y que `l >= 1` queda
contaminado con logaritmos. **Es falso.** La cuarta raíz limpia el canal diagonal `(3,3)`
**entero, para todo `l`**.

**El error:** apliqué `Ô_*` a `G_nu(s)` cuando el objeto físico es `Ô_*[rho^l G_nu(s)]`. El
`rho^l` del desarrollo de la exponencial es función de `rho` y va **dentro** del operador —
Pfeiffer (3.35) lo escribe así, y la `l` aparece dentro de `A_{kappa+1,l}(n)` y de `kappa`,
lo que sería imposible si `rho^l` fuese un prefactor. Como `rho^l = (s/c)^l` cancela las
`s^{-l}` de más de `G_{l+1}`, **todos** los sectores `l` del canal tienen potencia efectiva
`s^{-2}`, y `Ô_*` la aniquila y convierte el logaritmo en potencia:

```
l=0: Ô_* = -1/(2s^2)   l=1: -1/(c s^2)   l=2: -3/(c^2 s^2)   l=3: -12/(c^3 s^2)    todos sin log
```

Equivalentemente, y más limpio: los logaritmos salen del primer término de (3.43), que
multiplica `A_{kappa+1,l}(n) = prod 2(zeta-k) = 0  <=>  k <= n`, condición que **no involucra
`l`**. El canal `(3,3)` tiene `k=3`: con cinco capas (`n=3`) aniquilado para todo `l`.

**La contradicción estaba dentro de este mismo documento.** Su §1 demuestra que el orden en
`B̄` **no depende de `l`** usando el `rho^{l-mu-1}` de (3.43) —con el `rho^l` dentro—, y su §2
aplica el operador a `s^{-(2+l)}` —con el `rho^l` fuera—. La independencia en `l` del orden
**es** el enunciado de que `rho^l G_{1+l} ~ (log s)/s^2`. Tenía el hecho correcto y lo
contradije dos secciones después.

**Qué cambia y qué no:**

| | rev. 2 decía | rev. 3 |
|---|---|---|
| `l = 0` limpio | sí | **sí, sigue en pie** (y el apéndice §6 lo pincha numéricamente) |
| `l >= 1` | contaminado con log | **limpio también** |
| `F1` | abierta, decisiva | **RESUELTA** por la cuarta raíz |
| `C0` | reparada sólo en `l=0` | reparada en todo el canal |
| límite `□-R/2` (§3) | preservado | **sin cambio: el control sigue siendo válido** |
| `F3`/`F4` | intactos | **intactos, y ahora son lo único que bloquea** |

Lo que sobrevive a orden `rho^{-1/2}` es un resto **finito** proporcional a
`41K + 688W = 1016 E^2 + 360 B^2`, definida positiva, luego imposible de anular punto a punto.
Ésa es la única pregunta viva, y es `F3`/`F4`. Detalle completo en
`dev/S4W_R6PRIMEPRIME_NOGO_2026-10-10.md` §0.

`R6_PRIME` pasa de `PARTIAL` a:

```text
R6_PRIME = CONFIRMADO — la cuarta raiz limpia el canal (3,3) de logaritmo y de corte,
           para todo l.  Lo que queda a rho^{-1/2} es un resto finito, y es F3/F4.
```

---


Álgebra simbólica exacta (`sympy` 1.14.0, `.venv` del repo, solo lectura). Sin simulación, sin
semillas, sin `make dry-run/gate/op21-terminal`. `thresholds.py` intacto
(`6e2c3888…bfefd4`).

---

## 0. Veredicto

```text
R6_PRIME = PARTIAL

(a) ¿aniquila la cuarta raíz los logaritmos de W1?
      SI  en el sector l = 0   — y además aniquila la dependencia del corte
      NO  en los sectores l >= 1
(b) ¿sobrevive el canal y^4 donde vive C^2?
      SI, y limpio, en l = 0.  Contaminado en l >= 1.

S4W_W1_LOG_REMAINDER       = CLEANED_AT_L0 / SURVIVES_AT_L>=1
S4W_W1_CUTOFF_DEPENDENCE   = ANNIHILATED_AT_L0        <- nuevo, mejora C0 en ese sector
S4W_C2_CHANNEL             = OPEN_AND_CLEAN_AT_L0 / CONTAMINATED_AT_L>=1
LIMITE □-R/2               = EXACTAMENTE PRESERVADO   <- control, ver §3
```

**No es ninguno de los dos escenarios que la auditoría anticipaba.** No es "los logaritmos
caen y el canal queda limpio" ni es "la quinta capa mata su propia señal". Es un tercero: la
cuarta raíz limpia **completamente** el sector `l=0` —logaritmo y corte a la vez— y no toca
`l >= 1`, que vive en el mismo orden.

El cambio que importa no es de cuenta sino de **naturaleza del obstáculo**: antes de R6′, `F1`
era un resto log-realzado que BBD declaran no poder estimar. Después de R6′ es **un solo
término explícito**, con `l`, potencia y acción del operador conocidas.

> **Corregido en rev. 2 (defectos 1-4 de la revisión ciega, §7).** La rev. 1 decía aquí que
> quedaban coeficientes en `l = 1, 2` *"cuya cancelación es una contracción tensorial finita,
> no un problema abierto"*. **Afirmaba de más y por partida doble.** Primero, en vacío las dos
> vías que yo listaba en `l = 1, 2` se anulan idénticamente (§4). Segundo, aunque no se
> anularan, esa cancelación no es el cálculo que decide `F1`. Lo que de verdad queda es una
> única vía contaminante sin pareja contra la que cancelar, y eso empeora la expectativa en
> vez de mejorarla. Ver §4 y §5.

---

## 1. La maquinaria, tomada de la fuente

En `W1`, Pfeiffer (3.34) desarrolla `sqrt(-g)`, `phi`, el volumen y la exponencial, y tras la
integración angular todo queda en términos de la forma (3.35):

```
int_0^a dv int_0^v du  (v-u)^{d-2} (v-u)^alpha (v+u)^beta (uv)^{l d/2}  Ô_d  rho^l e^{-rho c_d (uv)^{d/2}}
```

donde `alpha, beta` son las potencias de `y` del desarrollo y **`l` cuenta las potencias de la
corrección de volumen** `delta V` al expandir la exponencial. El binomio (3.39) lleva a (3.40):

```
int int dv du  v^{m + l d/2} u^{k + l d/2}  Ô_d  e^{-rho c_d (uv)^{d/2}} ,     m + k = alpha+beta+d-2
```

con, por (3.41), `max(m,k) >= ceil((alpha+beta+d-2)/2)`. El cambio `x = u^{d/2}`, `y = v^{d/2}`
da (3.42) con

```
mu = (2/d)(m+1) + l - 1 ,     kappa = (2/d)(k+1) + l - 1
```

(reobtenido del jacobiano, no copiado: `v^{m+ld/2} dv = (2/d) y^{(2/d)(m+1)+l-1} dy`).

**El orden en `B̄` de cada canal.** El término 2 de (3.43) va como `rho^{l-mu-1}`, y
`l - mu - 1 = -(2/d)(m+1)`, luego con el prefactor `rho^{(d+2)/d}`:

```
orden en B_bar  =  rho^{(d+2)/d - (2/d)(m+1)}        <- INDEPENDIENTE de l
```

Mapa para `d = 4`:

| `(m,k)` | `m+k` | `alpha+beta` | orden en `B̄` | |
|---|---|---|---|---|
| (0,0) | 0 | −2 | `rho^1` | diagonal |
| (1,1) | 2 | 0 | `rho^{1/2}` | diagonal |
| **(2,2)** | 4 | **2** | **`rho^0`** | **diagonal — es el límite `□−R/2`** |
| **(3,3)** | 6 | **4** | **`rho^{-1/2}`** | **diagonal — es donde vive `C^2`** |
| (4,2) | 6 | 4 | `rho^{-1}` | fuera de la diagonal |
| (5,1) | 6 | 4 | `rho^{-3/2}` | fuera de la diagonal |
| (6,0) | 6 | 4 | `rho^{-2}` | fuera de la diagonal (añadida en rev.2) |

Dos cosas que esto fija y que la auditoría no tenía:

1. **A orden `rho^{-1/2}`, la contribución de `alpha+beta = 4` viene SOLO de la diagonal
   `(3,3)`.** Las demás particiones de `m+k = 6` están por debajo. Y la diagonal `mu = kappa`
   es exactamente donde aparecen los logaritmos (Belenchia §3.2: *"when m = n logarithmic
   terms, which are not annihilated by Ô, are also present"*).
2. **El orden no depende de `l`**, así que `l = 0, 1, 2, …` con `m = 3` caen todos en
   `rho^{-1/2}`. Esto es lo que la auditoría pasó por alto y lo que hace que R6′ salga parcial.

Tres salvedades añadidas en rev. 2 tras la revisión ciega, porque la rev. 1 leía este mapa como
más completo de lo que era:

- **La fórmula de orden sale del término 2 de (3.43) e ignora el término 1**, que lleva
  `A_{kappa+1,l}(n)`. No vale como enunciado universal. Para los canales de esta tabla sí vale,
  y por una razón concreta que aportó la revisión: con `n = 3` todas las particiones de
  `m+k = 6` tienen `k <= 3`, luego `A_{kappa+1,l}(3) = 0` las aniquila y **las de fuera de la
  diagonal no reentran** en `rho^{-1/2}`.
- **`alpha+beta` impar también alcanza `rho^{-1/2}`** —por ejemplo `(3,2)`, con `alpha+beta=3`—
  pero se anula en la integración angular por paridad (Wang ecs. (7)-(8): las integrales de un
  número impar de `n^i` son cero). Había que decirlo; la rev. 1 no lo decía.
- **`W2` no reentra a este orden** con `n = 3`: está en `O(rho^{-1})` por §2.3 de la auditoría.
  Y los términos `B_{kappa+1,l}` viven al mismo orden `l - mu - 1` y quedan absorbidos en
  `G_nu`.

---

## 2. La cuenta

El canal diagonal es `G_nu(s) = int_0^A int_0^A (xy)^nu e^{-s x y} dx dy` con `s = rho c_d`,
`A = a^{d/2}`, `nu = mu = kappa`. Forma cerrada exacta para `nu = 1` (el caso `(3,3), l=0`):

```
G_1(s) = [ (log(A^2 s) - Ei(-A^2 s) - 1 + gamma_E) e^{A^2 s} + 1 ] e^{-A^2 s} / s^2
       = ( log(s) + 2 log A - 1 + gamma_E ) / s^2   +  (exponencialmente pequeño)
```

Nótese la estructura, que es la clave de todo: **el coeficiente del logaritmo es 1 y no
depende de `A`; toda la dependencia del corte (`2 log A`) está en la potencia pura.**

Acción de los dos operadores, exacta. Conviene la forma por autovalores, que es más limpia que
la mía original y la aportaron las dos revisiones: sobre `s^{-q}` el operador actúa por el
escalar `p(q)`, y sobre `log(s) s^{-q}` como `p(q) log s - p'(q)`, con

```
p_*(q) = (2/3)(1/2 - q)(1 - q)(3/2 - q)(2 - q)      ->   p_*(2) = 0 ,  p_*'(2) = 1/2
```

de donde `Ô_*[s^{-2}] = 0` y `Ô_*[log(s) s^{-2}] = -1/(2 s^2)` sin tocar la integral:

| | sobre `log(s) s^{-2}` | sobre `s^{-2}` |
|---|---|---|
| `Ô_BD = (4/3)(H+½)(H+1)(H+3/2)` | `(11/3 - log s)/s^2` → **log sobrevive** | `-1/s^2` → **corte sobrevive** |
| `Ô_* = (2/3)(H+½)(H+1)(H+3/2)(H+2)` | `-1/(2 s^2)` → **sin log** | `0` → **corte aniquilado** |

Es decir, para `l = 0`:

```
Ô_BD G_1  = ( -log(A^6 s^3) - 3 gamma_E + 14 ) / (3 s^2)      log + dependencia de a
Ô_*  G_1  = -1 / (2 s^2)                                      limpio, no nulo, sin a
```

La cuarta raíz hace **dos** cosas, no una: convierte el logaritmo en potencia
(`(H+s)(log(rho) rho^{-s}) = rho^{-s}`, la observación de Grok) y aniquila la potencia pura,
que es justo donde vivía el corte. Lo que queda es `-1/2` por el coeficiente del logaritmo, y
ese coeficiente es `a`-independiente.

**Esto repara `C0` en el sector `l=0`:** la auditoría puso `C0 = REGULATED_ONLY` porque la
dependencia de la prescripción no se había mostrado `o(rho^{-1/2})`. Aquí no es que sea
`o(rho^{-1/2})`: es **exactamente cero**.

> **rev.3: lo que sigue es el error.** La potencia del canal **no** es `s^{-(2+l)}`: es `s^{-2}`
> para todo `l`, porque falta el `rho^l = (s/c)^l` dentro del operador. La tabla de abajo da la
> acción de `Ô_*` sobre potencias que no son las del canal físico. Ver el bloque de REVISIÓN 3.

Y para `l >= 1` la potencia del canal es `s^{-(2+l)}`, que `Ô_*` no aniquila:

| `l` | potencia | `Ô_*[log(s) s^{-q}]` | `Ô_*[s^{-q}]` | |
|---|---|---|---|---|
| 0 | `s^{-2}` | `-1/2` | `0` | **limpio** |
| 1 | `s^{-3}` | `5 log s - 77/6` | `5` | log y corte sobreviven |
| 2 | `s^{-4}` | `35 log s - 319/6` | `35` | log y corte sobreviven |
| 3 | `s^{-5}` | `126 log s - 275/2` | `126` | log y corte sobreviven |

---

## 3. Control: el límite `□ − R/2` se conserva exacto

Canal `(2,2)`, potencia `s^{-3/2}`. Los dos operadores anulan la potencia pura y dejan el
logaritmo, que es el que da el límite finito:

```
Ô_BD[log(s) s^{-3/2}] = (2/3) s^{-3/2} ,   prefactor b_0 = 2 sqrt6/3  ->  contribución 4 sqrt6/9
Ô_* [log(s) s^{-3/2}] = (1/6) s^{-3/2} ,   prefactor b_0 = 8 sqrt6/3  ->  contribución 4 sqrt6/9
```

**Idénticas.** El cociente de prefactores (4) cancela exactamente el cociente de coeficientes
de canal (1/4). Es el teorema de universalidad de Belenchia reobtenido por una vía
completamente distinta —descomposición en canales de `W1` en vez de su §3.5—, y sirve de
control de que nada de lo anterior está mal normalizado.

---

## 4. (rev.2) Dónde entra `C^2` en vacío — DOS vías, no tres

> La rev. 1 listaba **tres** vías. **Es falso en vacío**, y las dos revisiones ciegas lo
> señalaron por separado y coincidiendo (§7, defectos 1-2). Se conserva el error y su
> corrección, no se borra.

**Por qué caían las vías (ii) y (iii) de la rev. 1.** Pfeiffer (3.4) escribe la corrección de
volumen como

```
V = V_0^d [ 1 - d R eta_{mu nu} y^mu y^nu /(24(d+1)(d+2)) + d R_{mu nu} y^mu y^nu /(24(d+1)) + O(R^2) ]
```

y (3.3) da `sqrt(-g) = 1 - (1/6) R_{mu nu} y^mu y^nu + ...`. En **Ricci-flat**, `R = 0` y
`R_{mu nu} = 0`: los dos términos explícitos de primer orden se anulan. Llámese
`V = V_0 (1 + eps_1 + eps_2)` con `eps_1 ∝ R, R_{mu nu}` y `eps_2 = O(R^2)`. Entonces en vacío
`eps_1 = 0` en `x`, y con ello:

- la vía (ii) de la rev. 1, `(eps_1) x (término R de sqrt(-g))`, tiene **los dos factores nulos**;
- la vía (iii), `(eps_1)^2`, es nula por el mismo motivo.

**Lo que ocupa su lugar** es el término que la rev. 1 no contó: `eps_2`, el `O(R^2)` **propio**
del volumen —explícito en (3.4) y luego absorbido dentro de `S(y)` en (3.34)—, que es
precisamente la corrección de Wang ec. (79). Entra **lineal**, con `l = 1`.

Clasificación correcta, con `phi = 1` y a orden de curvatura exactamente `R^2`:

| vía | origen | `l` | potencia | bajo `Ô_*` |
|---|---|---|---|---|
| **(i)** | término `y^4` de `sqrt(-g)`: el `-(1/180) C C y^4` de Wang ec.(76)-(77) | 0 | `s^{-2}` | **limpia** — log y corte aniquilados |
| **(ii′)** | `eps_2`, el `O(R^2)` propio de `V(x,y)` — Wang ec.(79) | 1 | `s^{-3}` | log + corte sobreviven |

Y aquí está lo que esto destapa, que no es un detalle de contabilidad: **la vía (ii′) arrastra
exactamente `82K + 1376W`**, la mezcla que la auditoría §3.2 identificó como el fallo `F3`.
Es decir, el contaminante logarítmico y el problema de la dirección temporal **no son dos
problemas, son el mismo**. Lo que sobrevive al operador en `l=1` es el término dependiente del
observador, con coeficiente ~17 veces mayor que la parte invariante.

**Consecuencia sobre R6′.** El `C^2` limpio de la vía (i) existe y es `a`-independiente, pero
convive al mismo orden `rho^{-1/2}` con una vía contaminada **única**, sin pareja contra la que
cancelar. Eso es peor que lo que decía la rev. 1: no hay cancelación posible entre dos
términos; o el coeficiente de (ii′) es nulo por sí solo, o el logaritmo sobrevive y `F1` mata
el estimador.

---

## 5. (rev.2) Qué queda, exactamente

```
R6'' (REFORMULADO EN rev.2; la version de rev.1 preguntaba lo que no decide).

  La rev.1 preguntaba: "se cancela el logaritmo entre (ii) y (iii)?"  Esa pregunta esta MAL
  PLANTEADA en vacio: (ii) y (iii) no existen (§4).  La pregunta que decide es otra y es una
  sola:

  1. Calcular el coeficiente del logaritmo de la via (ii'), es decir la contribucion del
     O(R^2) propio del volumen -- eps_2, Wang ec.(79) -- al canal diagonal (3,3) con l=1,
     manteniendo U_y DENTRO de la integral.
       si NO es nulo -> el logaritmo sobrevive a orden rho^{-1/2} y el estimador muere por F1.
                        DEFINITIVO.  La linea cierra con un no-go nitido.
       si SI es nulo -> el orden rho^{-1/2} queda limpio y el coeficiente es el de la via (i).
     No hay escenario de cancelacion entre dos terminos: no hay dos.  Un termino aislado no
     tiene por que anularse, asi que la expectativa honesta es la primera rama.

  2. Solo si 1 sale nulo: la via (i) da el coeficiente, y entonces hay que preguntar si la
     integral angular sobre U_y colapsa a un invariante o sobrevive la mezcla 82K + 1376W.
     Esto es F3/F4 y R6' no lo toca.

  Nota que ahorra trabajo: por §4, la via (ii') arrastra 82K + 1376W.  Luego 1 y 2 miran el
  MISMO objeto por dos lados.  Si la integral angular de W no colapsa (F3/F4), es dificil que
  el coeficiente de 1 se anule.  Las dos ramas estan correlacionadas, y las dos apuntan al
  mismo sitio.

  Es analitico.  No necesita simulacion ni semillas.
```

**Lo que R6′ NO establece,** y conviene decirlo antes de que alguien lo lea de más:

- No da ningún coeficiente. Da la estructura del canal y qué sobrevive al operador.
- No toca `F3` ni `F4`. Y por §4 resulta que **no podría**: el contaminante que sobrevive *es*
  el objeto de `F3`.
- La vía (i) está limpia **en el sector `l=0`**, no "el canal está limpio".
- La reparación de `C0` vale en ese sector y para la **parte algebraica**: `A` entra en `G_1`
  por `2 log A`, que se aniquila, y por `Ei(-A^2 s)`, que es exponencialmente pequeño. Los
  términos `B_{kappa+1,l}` del mismo canal llevan `gamma(·, A^2 c rho) -> Gamma(·)` con resto
  exponencial, sin reentrada polinómica de `A`. Fuera quedan los sectores `l >= 1` y la
  desalineación `a`–`a'` entre las fronteras de `W1` y `W2`.

Con eso, el balance honesto, y es menos halagüeño que el de la rev. 1: el operador de cinco
capas **sí** tiene una propiedad demostrada que no es álgebra —aniquila a la vez el logaritmo y
la dependencia del corte en el sector `l=0` del canal local, cosa que el minimal no hace—, pero
el obstáculo que queda es un término solo, sin pareja, y es el mismo objeto que ya bloqueaba la
línea por `F3`. La línea no se ha reabierto: se ha estrechado hasta una única pregunta con
respuesta probable negativa. Que es, de todas formas, mucho mejor que un cabo colgando.

---

## 6. Apéndice (añadido después de enviar a revisión): confirmación numérica independiente

Las secciones 1–5 son álgebra simbólica. Esto es la misma cosa por un método distinto:
cuadratura de alta precisión (`mpmath`, 40 dígitos) del canal diagonal
`G_nu(s) = int_0^A int_0^A (xy)^nu e^{-sxy} dx dy`, con las derivadas en `H = s d/ds` tomadas
por diferencias centradas en `log s`. Sin simulación, sin semillas.

**Provenance:** los dos encargos de revisión ciega de `revisiones/2026-10-10-r6prime/` se
enviaron con la versión **anterior** a este apéndice, sha256
`ea8dfb63119175d3204038d06deb9c5452f6300837efdcfcf7ea3f7f3c1f13ec` (el valor exacto consta en la cabecera de cada
`informe_*.md`). Este apéndice confirma, no modifica, lo que juzgaron.

Lectura: un factor 4 en `s` produce un incremento de `log 4 = 1.386294` por fila **si queda
logaritmo**; si la columna es constante, está limpio.

```
         canal   nu        s |      O_BD G * s^p |       O_* G * s^p
  (2,2) limite  0.5      200 |    0.590817950297 |    0.147704487568
  (2,2) limite  0.5      800 |    0.590817950294 |    0.147704487562
  (2,2) limite  0.5     3200 |    0.590817950290 |    0.147704487556

 (3,3) l=0 C^2  1.0      200 |   -0.495516476925 |   -0.500000000034
 (3,3) l=0 C^2  1.0      800 |   -1.881810838060 |   -0.500000000058
 (3,3) l=0 C^2  1.0     3200 |   -3.268105199190 |   -0.500000000082

     (3,3) l=1  2.0      200 |   -41.9103295384  |    10.9551647686
     (3,3) l=1  2.0      800 |   -69.6362167610  |    24.8181083795
     (3,3) l=1  2.0     3200 |   -97.3621039836  |    38.6810519904
```

**Las tres afirmaciones quedan confirmadas, y con los coeficientes pinchados:**

- **`C2`, el resultado central.** `Ô_* G_1 · s^2 = -0.500000000` en las tres densidades, sin
  deriva. Y barriendo el corte: `-0.5000000001` para `A = 0.4`, `0.7` y `1.1`. Es
  `-1/2` exacto e **independiente del corte**, como predice §2.
  El operador minimal, en cambio, deriva `-1.386294 = -log 4` por fila: logaritmo puro con
  coeficiente `-1`, que es exactamente el `-log(A^6 s^3)/(3s^2)` de §2.
- **`l = 1` no se limpia.** `Ô_*` deriva `+13.863 = 10 log 4` por fila. Cuadra: la asintótica
  del canal es `G_2 = (4 log A + 2 log s - 3 + 2 gamma_E)/s^3`, con coeficiente de logaritmo
  **2**, y `Ô_*[log(s) s^{-3}] = 5 log s - 77/6`; `2 x 5 = 10`. (Para `Ô_BD`, `2 x (-10) = -20`,
  y se mide `-27.726 = -20 log 4`.) Nótese para evitar confusión: la tabla de §2 da la acción
  sobre `log(s) s^{-q}`, no sobre `G`; el coeficiente de logaritmo de `G_nu` es `nu`.
- **`C3`, el control del límite.** Las dos columnas del canal `(2,2)` son constantes —ningún
  logaritmo— y su cociente es `0.590817950297 / 0.147704487568 = 4.000000000`, que cancela
  exactamente el cociente de prefactores `b_0`. El límite `□ - R/2` se conserva al dígito.
  De paso queda identificado el coeficiente de logaritmo de ese canal:
  `0.5908.../(2/3) = 0.886227 = sqrt(pi)/2`.

---

## 7. (rev.2) Revisión ciega externa — dos familias

Mismo patrón que la auditoría: dos encargos separados, en ciego sellado, con `revision-ciega`
del PATH (`~/herramientas` @ `783f078`). **No** sanedrín. Encargo, entradas exactas y
respuestas sin editar en `revisiones/2026-10-10-r6prime/`.

Se envió la versión previa al apéndice §6 (sha256
`ea8dfb63119175d3204038d06deb9c5452f6300837efdcfcf7ea3f7f3c1f13ec`), junto con la auditoría y
la tesis de Pfeiffer. Entrada idéntica para las dos casas,
`178b7fb482aa056ea2bc53afc676a7f050ffef9c6644a22c480b74d8aefbc6d0`, 267 KB.

| casa | `C1` estructura | `C2` operador | `C3` control | veredicto |
|---|---|---|---|---|
| `deepseek-v4-pro` | CORRECTA | CORRECTA | CORRECTA | `CONFIRMADO_CON_CORRECCIONES` |
| `grok-4.6` | CORRECTA | CORRECTA | CORRECTA | `CONFIRMADO_CON_CORRECCIONES` |

Las tres afirmaciones que sostienen el resultado quedan confirmadas por las dos casas, y el
token `PARTIAL` se sostiene. Las dos recomputaron `G_1`, la acción del operador y el control
del límite `4 sqrt6/9`.

**Defectos, y los dos primeros los encontraron las dos por separado:**

| # | casa | defecto | corregido en |
|---|---|---|---|
| 1 | **ambas** | §4 contaba **tres** vías a `C^2` y omitía `eps_2`, el `O(R^2)` propio del volumen (Wang ec. 79), que entra lineal con `l=1` | **§4 reescrita** |
| 2 | **ambas** | en vacío las vías (ii) y (iii) de la rev. 1 **se anulan**: `eps_1 ∝ R, R_{mu nu} = 0`. El logaritmo residual es el de la vía omitida, sin pareja | **§4, §5** |
| 3 | Grok | el `R6''` de la rev. 1 preguntaba por la cancelación (ii)–(iii): no es la pregunta que decide `F1` | **§5 reescrita** |
| 4 | Grok | §0/§4 afirmaba de más al llamar a esa cancelación *"contracción tensorial finita, no un problema abierto"*; §5 no cubría el exceso | **§0, §5** |
| 5 | DeepSeek | la fórmula de orden de §1 no es universal: ignora el término 1 de (3.43) cuando `k > n` | §1, salvedad 1 |
| 6 | DeepSeek | la tabla de §1 omitía la partición `(6,0)` | §1, tabla |
| 7 | DeepSeek | no se discutía que los canales con `alpha+beta` impar, como `(3,2)`, los mata la paridad | §1, salvedad 2 |
| 8 | ambas | "corte exactamente cero" necesita el adjetivo: vale para la parte algebraica, las colas exponenciales siguen dependiendo de `A` (son `o(rho^{-1/2})`) | §5 |

Aportaciones que mejoran el documento más allá de corregirlo: la forma por autovalores
`p(q) log s - p'(q)` con `p_*(2)=0`, `p_*'(2)=1/2`, que da el `-1/2` sin integrar (ambas); que
`A_{kappa+1,l}(3) = 0` cierra la reentrada de las particiones fuera de la diagonal, porque
todas tienen `k <= 3` (Grok); y que los `B_{kappa+1,l}` llevan `gamma -> Gamma` con resto
exponencial, sin reentrada polinómica del corte (Grok).

**Lectura honesta.** Las dos casas confirman la cuenta y las dos tumban la interpretación. El
error no estaba en el álgebra sino en el mapa físico: clasifiqué las vías a `C^2` sin imponer
Ricci-flat, que es el régimen del propio estimador. El resultado neto de la revisión es que R6′
deja la línea **peor** de lo que la rev. 1 pintaba —un contaminante único, sin cancelación
posible, y que es el mismo objeto de `F3`— y a la vez **mejor planteada**: una sola pregunta,
analítica, con respuesta probable negativa y definitiva en cualquiera de los dos sentidos.
