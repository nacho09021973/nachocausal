# Paper III — Fase 1: suelo de resolución interno de la pierna intervalar

```text
REPORT_ID=PAPER_III_F1_INTERNAL_FLOOR
DATE=2026-09-10
MODE=INTERNAL_CALIBRATION_CONTROL
STATUS=UNSIGNED
INTERNAL_CALIBRATOR_FOUND=YES
CALIBRATOR=k-chain abundance C_k, k = 2,3,4, in a 3+1 Alexandrov interval
SAME_POSETS_AS_BETA=YES
NEW_SEEDS=NONE
NEW_N=NONE
NEW_RHO=NONE
NEW_PHYSICAL_OBSERVABLES=NONE
MINIMAL_CHANNEL_USED=NO
BOX_LEG_RUN=NO
PHASE_2_STARTED=NO
R_INTERPRETATION=DEFERRED
GATE_1=PENDING_INTERNAL_CALIBRATION
```

La ampliación a 17 réplicas dejó `beta − 1/4 = +0.0105` comparado contra un suelo
de `0.0179` **importado de la pierna de caja**. La pierna intervalar no tenía
calibrador exactamente conocido propio, porque `N` es fijo y `ρ·Vol = N` por
construcción. Este informe construye uno y mide qué desviación aparente produce
nuestro propio diseño sobre una magnitud cuya respuesta ya se conoce.

`C_k` es un **control de calibración**. No es un observable candidato, no se
promueve, no se interpreta y no forma parte de ninguna afirmación de Paper III.

---

## 1. THEORETICAL_CONTROL

### 1.1 Qué se buscó y qué se descartó

El candidato prioritario del PI era el *ordering fraction* / número de relaciones.
Resultó ser el caso `k = 2` de una familia más general y mejor: la **abundancia de
`k`-cadenas**, que además se acerca estructuralmente a `L` conforme crece `k`.

### 1.2 Fuente primaria

*Discrete geometry of a small causal diamond*, Roy, Sinha y Surya, §2, que
reproduce explícitamente el resultado de Meyer. Copia local en
`biblioteca/derived-md/Discrete geometry of a small causal diamond.md`. La sección
se titula «The Abundance of k-Chains in Flat Spacetime» y dice, literalmente, «We
now reproduce Meyer's results in n-dimensional flat spacetime».

Ecuación (9), transcrita sin alterar:

```text
chi_k = (1/k) (Gamma(n+1)/2)^(k-1) Gamma(n/2) Gamma(n)
                                 / ( Gamma(kn/2) Gamma((k+1)n/2) )
```

y ecuación (8): `<C_k>_eta = rho^k chi_k V_0^k`.

**Ninguna fórmula de este informe es inventada.** `chi_k` se transcribe; todo lo
demás se deriva de ella por álgebra elemental declarada en §3.

### 1.3 Las cinco verificaciones exigidas antes de programar nada

| # | pregunta | respuesta | evidencia |
|---|---|---|---|
| 1 | ¿esperanza conocida exacta o con corrección finita conocida? | **exacta, y sin corrección finita alguna** | §3 |
| 2 | ¿corresponde al ensemble binomial a `N` fijo? | la fuente da la forma **Poisson**; la binomial se deriva y se verifica | §3 |
| 3 | ¿válido en 3+1? | sí, `n` general; `n = 4` da `chi_2 = 1/20` | §1.4 |
| 4 | ¿depende sólo de `N` y `d`? | **sólo de `n` y `N`**: no de `ρ`, ni de `τ`, ni del tamaño del intervalo | eq. (9) |
| 5 | ¿fórmula finita exacta? | `E[C_k] = chi_k · N(N−1)···(N−k+1)` | §3 |

### 1.4 Preflight numérico

Ejecutado **antes** de tocar ningún artefacto de Paper III:

```text
[P1] eq.(9) autoconsistente:  chi_1 = 1 para n = 2,3,4,5, y chi_2 == eq.(11) en las cuatro
[P2] comprobacion propia del paper: "In 2 spacetime dimensions f(2) = 1/2"
     f0(2) = 0.25  ->  f(2) = 2 f0(2) = 0.500000000000   OK
[P3] eq.(4) da zeta_0(n=4) = 0.130899693899575
     dev/explore_3p1_bg_reference.py:23  DIAMOND_VOL_COEFF = np.pi/24 = 0.130899693899575
     MATCH exacto  ->  el intervalo de la fuente ES nuestro intervalo
[P4] chi_2(n=4) por cuadratura INDEPENDIENTE de eq.(9):  0.050000000000
     eq.(9):                                             0.050000000000   (= 1/20)
     coinciden a 6.9e-18
[P5] chi_2 = 5.000000e-02   chi_3 = 4.761905e-04   chi_4 = 1.417234e-06
```

`[P3]` es la comprobación que autoriza el resto: la constante geométrica de la
fuente y la del generador son el mismo número, luego no se está calibrando contra
otro intervalo.

---

## 2. ENSEMBLE_APPLICABILITY

La fuente enuncia la forma **Poisson**. Nuestra pierna es **binomial**: exactamente
`N` puntos i.i.d. uniformes (contrato §1.4, firmado en R003). La diferencia
importa y no se ignora.

`chi_k` es una fracción de volumen — es `P(x_1 ≺ x_2 ≺ ⋯ ≺ x_k)` para `k` puntos
i.i.d. uniformes —, luego **no depende del ensemble**. Lo único que cambia es el
recuento. Un `k`-subconjunto forma cadena en exactamente una de sus `k!`
ordenaciones, y esos `k!` sucesos son disjuntos, de modo que

```text
E[C_k] = C(N,k) · k! · chi_k = N(N-1)(N-2)···(N-k+1) · chi_k
```

**factorial descendente** donde la forma de Poisson lleva `N^k`. Usar la forma de
Poisson sobre nuestra pierna introduciría un sesgo espurio de orden `1/N`.

Verificado por fuerza bruta en `n = 2`, con un muestreador **independiente** del de
Paper III (coordenadas de cono de luz: el rombo es el cuadrado unidad en `(u,v)` y
`x ≺ y` sii `u_x<u_y` y `v_x<v_y`):

```text
   n=2 N=  6 k=2: 7.5020 / 7.5000 = 1.00026    k=3: 1.00010    k=4: 0.99777
   n=2 N= 10 k=2: 22.5055 / 22.5000 = 1.00024  k=3: 1.00071    k=4: 1.00129
   n=2 N= 14 k=2: 45.4836 / 45.5000 = 0.99964  k=3: 0.99968    k=4: 0.99993
```

---

## 3. EXACT_EXPECTATION

```text
E[C_k] = chi_k · N(N-1)···(N-k+1)        EXACTA EN TODO N FINITO
chi_2(n=4) = 1/20      chi_3(n=4) = 1/2100      chi_4(n=4) = 1.417233560091e-06
```

Esto es lo que hace del control un suelo y no otra incógnita: **no lleva
corrección de tamaño finito en absoluto**. No asintóticamente, no a primer orden:
exactamente.

### 3.1 Los mismos causal sets

Los posets de la corrida de 17 réplicas no están almacenados, sólo sus `L`. El
control los **regenera determinísticamente** importando el propio muestreador que
los produjo, y recalcula `L` con la rutina de cadena comprometida para poder
comprobar la identidad semilla a semilla:

```text
N=  2000  L regenerada == Ls comprometidas del artefacto de 17 replicas: True
N=  8000  True        N= 16000  True        N= 32000  True
semillas 101..117 (17) == semillas de la corrida de beta: True
SAME_POSETS_AS_BETA = True
```

```text
generador   dev/explore_3p1_internal_floor.py
gen sha256  d25dd13c95524ff9d1b8f8f4e32625be7d28131a996c7cbae93723cfc3e9915c
commit      427be6c3279b35100390517d944ef10e6378a740  (HEAD al correr)
artefacto   dev/explore_3p1_internal_floor_results.json
art sha256  72e2211919bff0c3638c3e6b1dfe4539d87d7317d2d3c3c2561e2da0c3b9a60d
runtime     21:10.66 wall, 163 MB RSS pico, exit 0
```

El contador de `C_k` se validó contra fuerza bruta (matriz de relación completa,
sin bloquear) en `N = 150, 400, 900`: idéntico en los tres, y `C_3` confirmado
además por producto de matrices.

---

## 4. MEASURED_DEVIATION

### 4.1 Amplitud — sin ningún parámetro libre

`g_k(N) ≡ C_k / [chi_k N(N−1)···(N−k+1)]`, cuya esperanza es **1 en todo `N`**.

| `N` | `g_2` | `g_3` | `g_4` |
|---|---|---|---|
| 2 000 | 0.99382 ± 0.01090 | 0.99613 ± 0.02890 | 1.00094 ± 0.05437 |
| 8 000 | 1.00277 ± 0.00697 | 1.00436 ± 0.01708 | 1.00585 ± 0.02855 |
| 16 000 | 1.00750 ± 0.00355 | 1.01591 ± 0.00824 | 1.02610 ± 0.01526 |
| 32 000 | 1.00003 ± 0.00205 | 1.00132 ± 0.00552 | 1.00379 ± 0.00965 |

Agrupado por varianza inversa:

```text
g2 = 1.001737 +/- 0.001705   ->  1.02 sigma de lo exacto
g3 = 1.005437 +/- 0.004402   ->  1.24 sigma
g4 = 1.009471 +/- 0.007834   ->  1.21 sigma
```

**El muestreador y la relación causal reproducen una ley exactamente conocida a
1.0–1.2 sigma en los tres `k`.** No hay error de implementación grueso.

### 4.2 Exponente — la comparación *apples-to-apples*

`beta` se obtuvo ajustando `L = A N^beta` y comparando con el `1/4` asintótico.
Equivalentemente: normalizar `L` por su ley asintótica, `y = L/N^(1/4)`, y ajustar
`y = A N^delta`; entonces `delta = beta − 1/4 = +0.0105` **es** todo el efecto.

El control se construye con la misma forma: normalizar `C_k` por su ley **exacta** y
ajustar `g_k = A N^delta`, donde la respuesta exacta es `delta = 0` sin
aproximación alguna. Así `delta(g_k)` y `delta(y)` son el mismo tipo de número,
producidos por el mismo pipeline desde los mismos causal sets, y uno de ellos
tiene respuesta conocida.

Dos reglas declaradas: **W** = WLS en log-log con pesos `1/relsem_i²`; **O** = OLS
log-log sin ponderar.

| cantidad | `delta` exacto | `delta` (W) | `delta` (O) |
|---|---|---|---|
| `g_2` | **0** | −0.001444 | +0.003119 |
| `g_3` | **0** | −0.004171 | +0.003594 |
| `g_4` | **0** | −0.006594 | +0.003691 |
| `y = L/N^(1/4)` | *desconocido* | **+0.010933** | **+0.009962** |

**Anclaje**: `delta(y)` reproduce `beta − 1/4 = +0.0105` bajo ambas reglas. La
comparación está anclada a la cifra que se quiere calibrar.

Bootstrap sobre las 17 semillas comprometidas (20 000 remuestreos, semilla
`20260910`):

```text
  g2: delta = -0.001444  sd = 0.003005  CI95 [-0.007646, +0.004211]  contiene 0: SI
  g3: delta = -0.004171  sd = 0.008688  CI95 [-0.021045, +0.013092]  contiene 0: SI
  g4: delta = -0.006594  sd = 0.016155  CI95 [-0.037613, +0.025859]  contiene 0: SI
   y: delta = +0.010933  sd = 0.004445  CI95 [+0.001787, +0.019201]  contiene 0: NO
```

Leave-one-out (regla W):

```text
  g2: -0.005743  -0.001595  +0.000725  +0.006608   max|.| = 0.006608
  g3: -0.010404  -0.005826  +0.000268  +0.010776   max|.| = 0.010776
  g4: -0.013339  -0.010624  -0.000107  +0.015670   max|.| = 0.015670
   y: +0.014516  +0.008666  +0.010470  +0.011865   SIEMPRE positivo, nunca cerca de 0
```

### 4.3 Un resultado negativo que conviene registrar

El primer intento aplicó la regla de `L` **literalmente** a `C_k` crudo — WLS en
escala lineal con una sigma constante agrupada — y comparó el exponente ajustado
con el que implica la ley exacta en la misma malla:

| `k` | `gamma_hat` | `gamma_exact` | desviación | vs 0.0105 |
|---|---|---|---|---|
| 2 | 1.991160 | 2.000050 | −0.008890 | 0.85× |
| 3 | 2.980400 | 3.000140 | −0.019740 | 1.88× |
| 4 | 3.969050 | 4.000270 | −0.031220 | 2.97× |

Esas desviaciones de hasta `0.031` son **artefacto de una ponderación mal
especificada**, no una propiedad del pipeline: la sigma constante agrupada es
correcta para `L`, cuya `sd` es casi plana en `N` (`0.85 … 1.06`), y es
inadecuada para `C_k`, cuya escala **absoluta** recorre un factor `2.6·10⁵` en el
barrido, de modo que el `N` mayor domina el ajuste por completo. Normalizar por la
ley exacta antes de ajustar elimina ese rango dinámico y las dos reglas pasan a
coincidir en magnitud. Se registra porque es la comparación que uno haría primero,
y es incorrecta.

---

## 5. COMPARISON_WITH_BETA_SHIFT

```text
mayor |delta| medido sobre una cantidad cuyo delta es exactamente 0 : 0.006594  (g4, regla W)
mayor |delta| bajo la regla O                                       : 0.003691  (g4)
resolucion mas fina del control (bootstrap sd)                      : 0.003005  (g2)
resolucion mas gruesa del control                                   : 0.016155  (g4)

beta - 1/4                                                          : +0.0100 .. +0.0109
resolucion de beta (bootstrap sd)                                   : 0.004445

beta / resolucion mas fina del control (g2)     = 3.32
beta / mayor |delta| del control                = 1.51
beta / resolucion mas gruesa del control (g4)   = 0.62
```

Tres hechos, y apuntan en direcciones distintas:

1. **A favor de que el efecto no es del pipeline.** El control más preciso (`g_2`)
   resuelve `delta` a `±0.0030` y mide `|delta| = 0.0014`, compatible con cero. Los
   tres intervalos CI95 del control **contienen el 0**; el de `y` **no**. Y bajo la
   regla ponderada los tres controles salen **negativos**, es decir del signo
   *contrario* al de `beta`: no hay un sesgo de modo común que empuje ambos hacia
   arriba.
2. **En contra de una comparación limpia.** La mayor desviación aparente que el
   control produce es `0.0066`, sólo un factor `1.5` por debajo de `0.0105`, y sus
   excursiones leave-one-out llegan a `0.0108` (`g_3`) y `0.0157` (`g_4`), es decir
   **al nivel del efecto o por encima**.
3. **El problema estructural.** La resolución del control **se degrada
   monótonamente al crecer `k`** — `0.0030`, `0.0087`, `0.0162` — y `k` creciente es
   precisamente la dirección en que el control se parece más a una cadena. El
   control es estrecho exactamente donde menos se parece a `L`, e inservible donde
   más se le parece.

---

## 6. LIMITATIONS

**L1 — el control no tiene corrección de tamaño finito, y `L` sí.** `E[C_k]` es
exacta en todo `N`. La ley de Brightwell–Gregory es asintótica y `m₄` sólo está
**acotado**, no conocido. Por tanto el control acota el sesgo de **implementación y
muestreo**, pero **no puede acotar la aproximación de tamaño finito** de un
estadístico de valor extremo. Y esa aproximación es la explicación más plausible
de `+0.0105`. El control no ve la magnitud que decidiría la cuestión.

**L2 — clase de estadístico distinta.** `C_k` es un recuento auto-promediante sobre
`~N^k/k!` subconjuntos; `L` es un máximo. Sus sesgos de frontera y de
discretización no tienen por qué coincidir.

**L3 — la resolución se agota antes de llegar a `L`.** `L ≈ 29` en `N = 32000`. El
control llega a `k = 4`, y ya en `k = 4` su resolución (`0.0162`) supera al efecto
que debe calibrar. Extenderlo a `k` grande es inviable: contar `k`-cadenas exige
recorrer la estructura de relaciones y el coste crece con `k`.

**L4 — y esto no es un descuido, es estructural.** Que la pierna intervalar carezca
de calibrador exacto **para `L`** no es una omisión del diseño: es que la ley finita
de la cadena más larga es exactamente lo que no se conoce. Que `m₄` esté sólo
acotado *es* esa afirmación. La familia de `k`-cadenas es el sustituto más cercano
disponible y se agota antes de alcanzar el carácter de `L`.

**L5 — el suelo importado no queda sustituido.** El `0.0179` de la pierna de caja
sigue siendo el único número que mide un exponente de valor exactamente conocido
en un diseño de sprinkling completo. Este informe **no lo reemplaza**; añade una
cota independiente sobre otro tipo de sesgo.

---

## 7. Clasificación

```text
VERDICT = C) INTERNAL_CALIBRATION_INCONCLUSIVE
```

**No es (B).** El criterio de B exige que el control interno sea *claramente* más
estrecho que `0.0105`. La mayor desviación aparente que el control produce es
`0.0066` — factor `1.5`, no un orden de magnitud — y bajo leave-one-out `g_3` y
`g_4` alcanzan `0.0108` y `0.0157`, al nivel del efecto o por encima. Además la
precisión del control se degrada justo en la dirección que importa (`k` creciente
= más parecido a una cadena). «Claramente más estrecho» no se sostiene.

**No es (A).** El control no demuestra que el diseño genere desviaciones aparentes
`≥ 0.0105`. Sus valores centrales son compatibles con cero en los tres `k`, los tres
CI95 contienen el 0, y el control más preciso es `3.3×` más estrecho que el efecto.
Las cifras grandes de §4.3 son artefacto de ponderación, no del diseño.

Es **C**: el control no permite una comparación limpia sobre la pregunta que
decide `beta`.

### 7.1 Lo que sí queda establecido

C no es un no-resultado. Con este control, dos cosas quedan cerradas:

1. **`beta` no es un artefacto de implementación.** El muestreador y la relación
   causal reproducen una ley exactamente conocida a `1.0–1.2 sigma` en `k = 2,3,4`,
   sobre los mismos causal sets, con las mismas semillas. Si hubiera un error en el
   sprinkler por rechazo o en la relación causal, `g_k` no valdría 1.
2. **El pipeline de regresión no fabrica desplazamientos positivos de exponente.**
   Sobre tres cantidades cuyo `delta` es exactamente 0, devuelve `delta` compatible
   con 0 y, bajo la regla ponderada, de signo contrario al de `beta`.

Lo que queda abierto es exactamente lo que L1 y L4 describen, y no es un problema
de esfuerzo: es que la ley finita de la cadena más larga no se conoce.

---

## 8. GATE_1_RECOMMENDATION

```text
GATE_1 = PENDING_INTERNAL_CALIBRATION   ->   se mantiene; este informe NO lo cierra
RECOMENDACION = decision del PI entre dos vias, ninguna de las cuales es GATE_1=PASS
```

**No se recomienda `GATE_1 = PASS`.** La calibración interna intentada no resuelve
la cuestión que lo bloqueaba.

Las dos vías que quedan, y la razón de cada una:

- **Vía 1 — cerrar la Fase 1 como `NULL_NOT_REJECTED`.**
  [R002 §5](paper_iii_resolucion_002_reescopado_fase1.md) ya define ese desenlace
  como *válido y suficiente para abrir la Fase 2 como control*. El modelo constante
  nunca fue rechazado (`χ²/dof = 1.54`, `p = 0.202`, `m₄` en banda). El
  desplazamiento `+0.0105` quedaría **registrado como residuo abierto y no
  resuelto**, no como señal. Esta vía usa la puerta tal como está escrita.
- **Vía 2 — seguir persiguiendo el suelo.** Requeriría un calibrador que sea a la
  vez exacto a `N` finito **y** de tipo valor-extremo. L4 dice que eso es
  precisamente lo que no se conoce, así que esta vía es investigación teórica
  abierta, no una corrida más.

**Lo que NO se recomienda en ningún caso:** más réplicas (el error estadístico ya
está por debajo del suelo), más `N` (no es la limitación), ni promover `+0.0105` a
señal física.

---

## 9. Qué NO autoriza este informe

- No declara `GATE_1 = PASS` ni ningún otro valor de `GATE_1`.
- No declara señal física. `+0.0105` sigue sin explicación y sin promoción.
- No promueve `C_k` a observable de Paper III. Es un control y muere como control.
- No interpreta `R`: `R_INTERPRETATION=DEFERRED`.
- No reabre el canal de minimales, suspendido por R004.
- No ejecuta ni autoriza la pierna de caja ni la Fase 2.
- No añade semillas, `N`, `rho` ni geometrías.
- No declara alcanzado ni no alcanzado ningún régimen asintótico.

## 10. Validación ejecutada

```text
python3 dev/verify_3p1_notes_figures.py      -> exit 0   ALL FIGURES MATCH
python3 dev/verify_3p1_phase0_contract.py    -> exit 0   STRUCTURAL CHECKS: ALL PASS
                                                         GATE_0 BLOCKERS: 0 open
```

Ningún verificador se relajó ni se modificó para acomodar este resultado.
Artefactos históricos intactos, comprobados por hash: precisión 8 réplicas
`eb101d3f…91e7`, precisión 17 réplicas `62403ded…5a10`, caja histórica
`e5cb5fb7…0bcd6`, caja R001 `0aa22402…c55b68`.

---

## Apéndice A — script de análisis

```text
sha256 = e89f400fb796dc4942e0285fa5555eb7c70475b4865af64e08192ae11f5b1658
```

```python
"""EXPLORATION -- Paper III, Phase 1: INTERNAL RESOLUTION FLOOR of the interval leg.

Reads committed artifacts only. Runs no generator, adds no seed/N/rho, defines no
physical observable. C_k is a CONTROL, never promoted.

THE COMPARISON. beta was obtained by fitting L = A N^beta and comparing beta to
the asymptotic 1/4. Equivalently: normalise L by its asymptotic law, y = L/N^(1/4),
and fit y = A N^delta; then delta = beta - 1/4 = +0.0105 is the whole effect.

The control is built to be the same shape. Normalise C_k by its EXACT law,

    g_k(N) = C_k / [chi_k N(N-1)...(N-k+1)]     ->   E[g_k] = 1 at EVERY N, exactly,

and fit g_k = A N^delta. Here the exact answer is delta = 0 with no approximation
whatsoever: not asymptotically, not to leading order, exactly. So delta(g_k) and
delta(y) are the same kind of number, produced by the same pipeline from the same
causal sets, and one of them has a known answer.
"""
import json
import numpy as np
from math import gamma as G

FLOOR = "dev/explore_3p1_internal_floor_results.json"
P17 = "dev/explore_3p1_bg_reference_precision17_results.json"
KS = (2, 3, 4)
NREP = 17


def chi(k, n=4):
    return (1.0 / k) * (G(n + 1) / 2.0) ** (k - 1) * G(n / 2) * G(n) \
        / (G(k * n / 2) * G((k + 1) * n / 2))


def falling(N, k):
    out = 1.0
    for i in range(k):
        out *= (N - i)
    return out


d = json.load(open(FLOOR))
p17 = json.load(open(P17))
N = np.array(d["Ns"], float)
rows = {r["N"]: r for r in d["rows"]}

# per-seed normalised quantities. Columns = seeds, rows = N.
G_k = {k: np.array([np.asarray(rows[n][f"C{k}"], float) / (chi(k) * falling(n, k))
                    for n in d["Ns"]]) for k in KS}
Lm = np.array([np.asarray(r["L"], float) + 2.0 for r in d["rows"]])      # R001
Y = Lm / N[:, None] ** 0.25                                             # y per seed


def fit_log(N, q, w=None):
    """delta from log q = log A + delta log N. w = weights (1/relsem^2) or None."""
    X = np.column_stack([np.ones_like(N), np.log(N)])
    lq = np.log(q)
    if w is None:
        w = np.ones_like(N)
    A = X.T @ (X * w[:, None])
    return float(np.linalg.solve(A, X.T @ (w * lq))[1])


def relsem(M):
    return M.std(1, ddof=1) / np.sqrt(M.shape[1]) / M.mean(1)


print("=" * 96)
print("[1] PROVENANCE -- the SAME causal sets, checked seed by seed")
ok = all(r["L"] == r17["Ls"] and r["N"] == r17["N"]
         for r, r17 in zip(d["rows"], p17["rows"])) and d["seeds"] == p17["seeds"]
print(f"   regenerated L == committed 17-replicate Ls at all four N, same 17 seeds: {ok}")
print(f"   SAME_POSETS_AS_BETA = {ok}")

print("\n" + "=" * 96)
print("[2] AMPLITUDE -- g_k = C_k / exact.  E[g_k] = 1 at every N, EXACTLY.")
print(f"   chi_k(n=4): " + "  ".join(f"chi_{k}={chi(k):.10e}" for k in KS))
print(f"\n   {'N':>7}" + "".join(f"{'g'+str(k):>24}" for k in KS))
for i, n in enumerate(d["Ns"]):
    print(f"   {n:7d}" + "".join(
        f"   {G_k[k][i].mean():.5f} +/- {relsem(G_k[k])[i]:.5f}" for k in KS))
print("\n   inverse-variance pooled over the four N:")
for k in KS:
    m, s = G_k[k].mean(1), relsem(G_k[k]) * G_k[k].mean(1)
    w = 1 / s ** 2
    mu, se = (w * m).sum() / w.sum(), 1 / np.sqrt(w.sum())
    print(f"     g{k} = {mu:.6f} +/- {se:.6f}   -> {abs(mu-1)/se:.2f} sigma from exact")

print("\n" + "=" * 96)
print("[3] THE EXPONENT OF THE NORMALISED QUANTITY.")
print("    Exact answer for g_k: delta = 0, with no approximation at any N.")
print("    Same rule applied to y = L/N^(1/4), where delta IS beta - 1/4.")
print("\n    RULE W : WLS in log-log, weights 1/relsem_i^2 (each point's own dispersion)")
print("    RULE O : unweighted OLS in log-log (no weighting choice at all)")
print(f"\n   {'quantity':>10}{'exact delta':>13}{'delta (W)':>12}{'delta (O)':>12}"
      f"{'relsem range':>22}")
res = {}
for k in KS:
    M = G_k[k]
    rs = relsem(M)
    dW, dO = fit_log(N, M.mean(1), 1 / rs ** 2), fit_log(N, M.mean(1))
    res[f"g{k}"] = (dW, dO, rs)
    print(f"   {'g'+str(k):>10}{0.0:13.6f}{dW:+12.6f}{dO:+12.6f}"
          f"   {rs.min():.5f}..{rs.max():.5f}")
rsY = relsem(Y)
dWY, dOY = fit_log(N, Y.mean(1), 1 / rsY ** 2), fit_log(N, Y.mean(1))
res["y"] = (dWY, dOY, rsY)
print(f"   {'y = L/N^.25':>10}{'(unknown)':>13}{dWY:+12.6f}{dOY:+12.6f}"
      f"   {rsY.min():.5f}..{rsY.max():.5f}")
print(f"\n   ANCHOR: delta(y) must reproduce beta - 1/4 = +0.0105 from the beta run.")
print(f"           rule W: {dWY:+.6f}   rule O: {dOY:+.6f}   -> anchored: "
      f"{abs(dOY-0.0105) < 0.002}")

print("\n" + "=" * 96)
print("[4] SEED BOOTSTRAP of delta -- same 17 committed replicas, resampled together")
rng = np.random.default_rng(20260910)
B = 20000
idx = rng.integers(0, NREP, (B, NREP))
boot = {}
for name, M in [(f"g{k}", G_k[k]) for k in KS] + [("y", Y)]:
    ds = np.empty(B)
    for b in range(B):
        s = M[:, idx[b]]
        ds[b] = fit_log(N, s.mean(1), 1 / relsem(s) ** 2)
    boot[name] = ds
    lo, hi = np.percentile(ds, [2.5, 97.5])
    tgt = 0.0 if name != "y" else 0.25 - 0.25
    extra = ""
    if name != "y":
        extra = f"   contains 0: {lo <= 0 <= hi}"
    else:
        extra = f"   contains 0: {lo <= 0 <= hi}  (i.e. contains beta = 1/4)"
    print(f"   {name:>4}: delta = {res[name][0]:+.6f}   sd = {ds.std():.6f}"
          f"   CI95 [{lo:+.6f}, {hi:+.6f}]{extra}")

print("\n" + "=" * 96)
print("[5] LEAVE-ONE-OUT of delta (rule W)")
for name, M in [(f"g{k}", G_k[k]) for k in KS] + [("y", Y)]:
    ds = []
    for i in range(len(N)):
        j = [m for m in range(len(N)) if m != i]
        s = M[j]
        ds.append(fit_log(N[j], s.mean(1), 1 / relsem(s) ** 2))
    ds = np.asarray(ds)
    print(f"   {name:>4}: " + "  ".join(f"{v:+.6f}" for v in ds)
          + f"   | range {ds.min():+.6f}..{ds.max():+.6f}  max|.| = {abs(ds).max():.6f}")

print("\n" + "=" * 96)
print("[6] THE FLOOR")
cands = []
for k in KS:
    cands.append((f"g{k} |delta|", abs(res[f'g{k}'][0])))
    cands.append((f"g{k} bootstrap sd", boot[f'g{k}'].std()))
for nm, v in cands:
    print(f"   {nm:>22} = {v:.6f}")
bias = max(abs(res[f"g{k}"][0]) for k in KS)
noise = max(boot[f"g{k}"].std() for k in KS)
tight = min(boot[f"g{k}"].std() for k in KS)
print(f"\n   largest measured |delta| on a quantity whose delta is exactly 0 : {bias:.6f}")
print(f"   best  (tightest) resolution on delta, over k                     : {tight:.6f}  (g2)")
print(f"   worst (loosest)  resolution on delta, over k                     : {noise:.6f}  (g4)")
print(f"\n   beta - 1/4 = {dOY:+.6f}  (bootstrap sd {boot['y'].std():.6f})")
print(f"   beta shift / tightest control resolution = {abs(dOY)/tight:.2f}")
print(f"   beta shift / largest control |delta|     = {abs(dOY)/bias:.2f}")
print(f"   beta shift / loosest control resolution  = {abs(dOY)/noise:.2f}")

print("\n" + "=" * 96)
print("[7] WHY THE NAIVE 'SAME PIPELINE' COMPARISON WAS ABANDONED (negative result)")
print("    First attempt: apply the L rule LITERALLY to raw C_k -- WLS on the linear")
print("    scale with one pooled constant sigma across the sweep -- and compare the")
print("    fitted exponent with the exponent the exact law implies on the same grid.")
print("    That rule is right for L, whose sd is nearly flat in N (0.85..1.06). It is")
print("    badly wrong for C_k, whose ABSOLUTE scale spans a factor 2.6e5 across the")
print("    sweep, so one constant sigma makes the largest N dominate completely.")
GRID = np.linspace(0.5, 5.0, 450001)


def fit_lin_pooled(N, Q, sigma):
    w = 1.0 / sigma ** 2
    F = N[None, :] ** GRID[:, None]
    A = (F * Q).sum(1) / (F * F).sum(1)
    return float(GRID[int(np.argmin((w * (Q - A[:, None] * F) ** 2).sum(1)))])


print(f"\n   {'k':>3}{'gamma_hat':>12}{'gamma_exact':>13}{'deviation':>12}{'vs 0.0105':>12}")
for k in KS:
    Q = np.array([np.asarray(rows[n][f"C{k}"], float).mean() for n in d["Ns"]])
    sd = np.array([np.asarray(rows[n][f"C{k}"], float).std(ddof=1) for n in d["Ns"]])
    Qex = np.array([chi(k) * falling(n, k) for n in d["Ns"]])
    s1 = np.full(len(N), float(np.sqrt(np.mean(sd ** 2))) / np.sqrt(NREP))
    gh, ge = fit_lin_pooled(N, Q, s1), fit_lin_pooled(N, Qex, s1)
    print(f"   {k:>3}{gh:12.6f}{ge:13.6f}{gh-ge:+12.6f}{abs(gh-ge)/0.0105:>11.2f}x")
print("\n   Those deviations (up to 0.031) are an artifact of the mis-specified")
print("   weighting, not a property of the pipeline: normalising by the exact law")
print("   first, as in sections [3]-[6], removes the dynamic range and the two")
print("   weighting rules then agree on magnitude. The naive table is reported")
print("   because it is the comparison one would reach for first, and it is wrong.")
```

## Apéndice B — salida íntegra

```text
================================================================================================
[1] PROVENANCE -- the SAME causal sets, checked seed by seed
   regenerated L == committed 17-replicate Ls at all four N, same 17 seeds: True
   SAME_POSETS_AS_BETA = True

================================================================================================
[2] AMPLITUDE -- g_k = C_k / exact.  E[g_k] = 1 at every N, EXACTLY.
   chi_k(n=4): chi_2=5.0000000000e-02  chi_3=4.7619047619e-04  chi_4=1.4172335601e-06

         N                      g2                      g3                      g4
      2000   0.99382 +/- 0.01090   0.99613 +/- 0.02890   1.00094 +/- 0.05437
      8000   1.00277 +/- 0.00697   1.00436 +/- 0.01708   1.00585 +/- 0.02855
     16000   1.00750 +/- 0.00355   1.01591 +/- 0.00824   1.02610 +/- 0.01526
     32000   1.00003 +/- 0.00205   1.00132 +/- 0.00552   1.00379 +/- 0.00965

   inverse-variance pooled over the four N:
     g2 = 1.001737 +/- 0.001705   -> 1.02 sigma from exact
     g3 = 1.005437 +/- 0.004402   -> 1.24 sigma from exact
     g4 = 1.009471 +/- 0.007834   -> 1.21 sigma from exact

================================================================================================
[3] THE EXPONENT OF THE NORMALISED QUANTITY.
    Exact answer for g_k: delta = 0, with no approximation at any N.
    Same rule applied to y = L/N^(1/4), where delta IS beta - 1/4.

    RULE W : WLS in log-log, weights 1/relsem_i^2 (each point's own dispersion)
    RULE O : unweighted OLS in log-log (no weighting choice at all)

     quantity  exact delta   delta (W)   delta (O)          relsem range
           g2     0.000000   -0.001444   +0.003119   0.00205..0.01090
           g3     0.000000   -0.004171   +0.003594   0.00552..0.02890
           g4     0.000000   -0.006594   +0.003691   0.00965..0.05437
   y = L/N^.25    (unknown)   +0.010933   +0.009962   0.00761..0.01440

   ANCHOR: delta(y) must reproduce beta - 1/4 = +0.0105 from the beta run.
           rule W: +0.010933   rule O: +0.009962   -> anchored: True

================================================================================================
[4] SEED BOOTSTRAP of delta -- same 17 committed replicas, resampled together
     g2: delta = -0.001444   sd = 0.003005   CI95 [-0.007646, +0.004211]   contains 0: True
     g3: delta = -0.004171   sd = 0.008688   CI95 [-0.021045, +0.013092]   contains 0: True
     g4: delta = -0.006594   sd = 0.016155   CI95 [-0.037613, +0.025859]   contains 0: True
      y: delta = +0.010933   sd = 0.004445   CI95 [+0.001787, +0.019201]   contains 0: False  (i.e. contains beta = 1/4)

================================================================================================
[5] LEAVE-ONE-OUT of delta (rule W)
     g2: -0.005743  -0.001595  +0.000725  +0.006608   | range -0.005743..+0.006608  max|.| = 0.006608
     g3: -0.010404  -0.005826  +0.000268  +0.010776   | range -0.010404..+0.010776  max|.| = 0.010776
     g4: -0.013339  -0.010624  -0.000107  +0.015670   | range -0.013339..+0.015670  max|.| = 0.015670
      y: +0.014516  +0.008666  +0.010470  +0.011865   | range +0.008666..+0.014516  max|.| = 0.014516

================================================================================================
[6] THE FLOOR
               g2 |delta| = 0.001444
          g2 bootstrap sd = 0.003005
               g3 |delta| = 0.004171
          g3 bootstrap sd = 0.008688
               g4 |delta| = 0.006594
          g4 bootstrap sd = 0.016155

   largest measured |delta| on a quantity whose delta is exactly 0 : 0.006594
   best  (tightest) resolution on delta, over k                     : 0.003005  (g2)
   worst (loosest)  resolution on delta, over k                     : 0.016155  (g4)

   beta - 1/4 = +0.009962  (bootstrap sd 0.004445)
   beta shift / tightest control resolution = 3.32
   beta shift / largest control |delta|     = 1.51
   beta shift / loosest control resolution  = 0.62

================================================================================================
[7] WHY THE NAIVE 'SAME PIPELINE' COMPARISON WAS ABANDONED (negative result)
    First attempt: apply the L rule LITERALLY to raw C_k -- WLS on the linear
    scale with one pooled constant sigma across the sweep -- and compare the
    fitted exponent with the exponent the exact law implies on the same grid.
    That rule is right for L, whose sd is nearly flat in N (0.85..1.06). It is
    badly wrong for C_k, whose ABSOLUTE scale spans a factor 2.6e5 across the
    sweep, so one constant sigma makes the largest N dominate completely.

     k   gamma_hat  gamma_exact   deviation   vs 0.0105
     2    1.991160     2.000050   -0.008890       0.85x
     3    2.980400     3.000140   -0.019740       1.88x
     4    3.969050     4.000270   -0.031220       2.97x

   Those deviations (up to 0.031) are an artifact of the mis-specified
   weighting, not a property of the pipeline: normalising by the exact law
   first, as in sections [3]-[6], removes the dynamic range and the two
   weighting rules then agree on magnitude. The naive table is reported
   because it is the comparison one would reach for first, and it is wrong.
```
