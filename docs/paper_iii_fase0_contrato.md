# Paper III — Fase 0: contrato de calibración y auditoría de entrada

Fecha: 2026-09-10. Ejecuta la primera iteración de
[la hoja de ruta](hoja_de_ruta_paper_iii.md) («Fase 0 — contrato matemático y
auditoría de entrada»).

```text
PAPER_III_PHASE=0
GATE_0=BLOCKED
NEW_VALIDATION_RUNS=NONE_EXECUTED
NEW_OBSERVABLES=NONE_DEFINED
SWEEPS_EXECUTED=NONE
HORIZON_CLAIM=NONE
BLOCKERS_OPEN=9
```

No se ejecutó ningún barrido, no se definió ningún observable nuevo y no se
tocó ningún instrumento sellado. Todo lo que sigue es aritmética sobre los
artefactos ya comprometidos, inspección de código y una auditoría del proceso
puntual del generador.

Verificadores:

```bash
python3 dev/verify_3p1_notes_figures.py     # notas <-> JSON   (preexistente)
python3 dev/verify_3p1_phase0_contract.py   # JSON <-> JSON, código <-> código, generador <-> medida
```

Ambos salen con código 0. El primero certifica `ALL FIGURES MATCH`. El segundo
certifica `STRUCTURAL CHECKS: ALL PASS` y **abre nueve bloqueos de `GATE_0`**:
un bloqueo no es un fallo del script, es una ambigüedad que la hoja de ruta
obliga a resolver antes de avanzar.

---

## 1. Definiciones fijadas

### 1.1 El intervalo de Alexandrov en Minkowski 3+1

Métrica `ds^2 = -dt^2 + dx^2` con `x` en `R^3`, coordenadas inerciales, `c = 1`.
Para `p = (0, 0)` y `q = (tau, 0)`:

```text
I(p, q) = { (t, x) : |x| <= t  y  |x| <= tau - t }
```

Su volumen de Minkowski es exactamente

```text
Vol_4(tau) = (pi / 24) tau^4
```

y el radio espacial máximo del rombo es `tau/2`, alcanzado en `t = tau/2`.

Implementación: `dev/explore_3p1_bg_reference.py:26-41`, con `tau = 1`. El
muestreo es por rechazo desde `t ~ U[0, tau]`, `x ~ U[-tau/2, tau/2]^3`. La
caja de propuesta **contiene** el rombo, porque la bola de radio `tau/2` está
inscrita en ese cubo; luego no hay recorte. Confirmado numéricamente: la tasa
de aceptación es `0.130791` contra `pi/24 = 0.130900` exacto, y ningún punto
aceptado supera el radio `tau/2`.

### 1.2 La caja truncante (pierna secundaria)

`D = [0, 1] x [0, 1]^3`, volumen 1, en las mismas coordenadas inerciales
(`dev/explore_3p1_scale_calibration.py:44-46`). **No es un intervalo de
Alexandrov** y por tanto Brightwell–Gregory no se le aplica; es el objeto sobre
el que `R` sería un funcional de forma, no un calibrador.

### 1.3 Relación entre `N`, `rho`, volumen y tiempo propio

| Pierna | Región | Volumen | Proceso | Relación |
|---|---|---|---|---|
| Intervalo | `I(p,q)`, `tau=1` | `pi/24 = 0.130900` | `N` fijo | `rho = N / Vol_4(tau) = 24 N / pi` |
| Caja | `[0,1]^4` | `1` | Poisson | `E[N] = rho`, `tau` no definido |

Para la pierna intervalar, `rho * Vol = N` **exactamente**, luego la
normalización `L / (rho Vol)^{1/4}` de Brightwell–Gregory y la
`L / N^{1/4}` que reportan las notas coinciden sin aproximación. Esa
identidad es la razón por la que la pierna intervalar es el ancla y la de caja
no lo es.

### 1.4 Proceso puntual — auditoría (deliverable «la nube es Poisson homogénea»)

```text
pierna intervalar : exactamente n_target puntos i.i.d. uniformes en I(p,q)
                    -> proceso BINOMIAL = Poisson condicionado a N = n
pierna de caja    : rng.poisson(rho * Vol(D)) puntos i.i.d. uniformes en D
                    -> proceso de POISSON homogéneo
```

Ambos son homogéneos respecto a la medida de Lebesgue, que en coordenadas
inerciales **es** el volumen de Minkowski (`sqrt(-g) = 1`). Ésta es la única
geometría 3+1 donde el atajo «uniforme en coordenadas» es legítimo; en
Schwarzschild 3+1 no lo es (`sqrt(-g) = r^2 sin(theta)`), y ése es uno de los
bloqueos de la Fase 4.

Contrastes ejecutados sobre la pierna intervalar (semillas de auditoría
declaradas 101–103, `N = 200 000`, más la semilla 999 para la tasa de
aceptación; ninguna produce cifra reportada):

| Contraste | Estadístico | Resultado |
|---|---|---|
| marginal en `t` contra la densidad exacta `min(t, tau-t)^3`, 20 bins con masa integrada | `chi2 = 26.56 / 16.73 / 5.14`, dof 19, crítico al 1% = 36.19 | pasa |
| marginal radial: `u = (\|x\| / min(t, tau-t))^3` debe ser `U[0,1]` | `KS = 0.00233 / 0.00096 / 0.00116`, crítico al 5% = 0.00304 | pasa |
| tasa de aceptación del rechazo | `0.130791` vs `pi/24` | pasa |

**Veredicto parcial: la nube es homogénea respecto al volumen de Minkowski y el
muestreador del rombo es correcto.** Ésta es la única parte de la Fase 0 que
cierra limpia.

---

## 2. El bloqueo central: la definición de `L` no es única en el repositorio

Tres implementaciones, un mismo poset explícito de tres elementos
`a < b < c` (`dev/verify_3p1_phase0_contract.py`, sección `[B]`):

| Implementación | Resultado | Convención |
|---|---|---|
| `nachocausal/estimator.py:47` (sellado) | `Lfut = [3, 2, 1]` | **elementos** (un maximal vale 1) |
| `dev/explore_3p1_bg_reference.py:53,65` | `L = 3` | **elementos** |
| `dev/explore_3p1_scale_calibration.py:94,98` | `L = [2, 1, 0]` | **relaciones** (un maximal vale 0) |

`dev/PAPER3_3P1_SCALE_NOTES.md` §1 afirma que ambas piernas siguen la
convención congelada en
`docs/preregistration_new_geometry_future_observables.md` §1. **La pierna de
caja no la sigue: difiere en exactamente uno.**

La literatura resuelve el punto sin ambigüedad. Rideout, *Dynamics of Causal
Sets* (gr-qc/0212064), en el mismo documento del que las notas toman el
teorema: *«An n-chain is a chain with n elements. […] The length of a path is
its number of elements»*
(`biblioteca/derived-md/Dynamics_of_Causal_Sets_arXiv_gr-qc0212064.md:178`), y
la cadena que se mide es *«the longest chain connecting x and y»*
(idem `:249`). La convención de la ley es **elementos, extremos incluidos**.

---

## 3. El bloqueo decisivo: la cota rigurosa de `m_4` discrimina la convención

La misma fuente da cotas **rigurosas** (idem `:283`), para `d >= 3`:

```text
1.77 <= 2^(1-1/d) / Gamma(1+1/d) <= m_d <= 2^(1-1/d) e Gamma(d+1)^(1/d) / d <= 2.62
```

Evaluadas en `d = 4`:

```text
1.8555 <= m_4 <= 2.5296
```

Ninguna normalización admisible de `L` puede caer fuera de esa banda. Aplicada
a los artefactos ya comprometidos:

| Pierna | `N` | `<L>` | `L / N^(1/4)` | ¿en banda? | `(L+2) / N^(1/4)` | ¿en banda? |
|---|---|---|---|---|---|---|
| precisión | 2 000 | 12.625 | 1.8879 | sí | 2.1869 | sí |
| precisión | 8 000 | 18.000 | 1.9033 | sí | 2.1147 | sí |
| precisión | 16 000 | 22.625 | 2.0117 | sí | 2.1895 | sí |
| precisión | 32 000 | 27.625 | 2.0655 | sí | 2.2150 | sí |
| base (3 semillas) | 500 | 8.333 | 1.7623 | **NO** | 2.1852 | sí |
| base (3 semillas) | 1 000 | 9.333 | 1.6597 | **NO** | 2.0154 | sí |
| base (3 semillas) | 2 000 | 11.667 | 1.7446 | **NO** | 2.0436 | sí |
| base (3 semillas) | 4 000 | 15.333 | 1.9281 | sí | 2.1796 | sí |
| base (3 semillas) | 8 000 | 17.667 | 1.8680 | sí | 2.0795 | sí |
| base (3 semillas) | 16 000 | 22.000 | 1.9561 | sí | 2.1339 | sí |

**Tres de diez filas violan la cota inferior rigurosa bajo la normalización que
las notas reportan. Ninguna la viola contando los dos extremos.**

Y la consecuencia sobre la lectura de §3.1 es cualitativa, no cosmética:

```text
convención              N=2000   N=8000  N=16000  N=32000     pendientes locales     global
L   (como se reporta)   1.8879   1.9033   2.0117   2.0655   0.2559 0.3299 0.2881     0.2835
L+1                     2.0374   2.0090   2.1006   2.1402   0.2399 0.3143 0.2770     0.2686
L+2 (con p y q)         2.1869   2.1147   2.1895   2.2150   0.2258 0.3001 0.2667     0.2552
```

El mismo artefacto, las mismas ocho semillas: un ascenso monótono del `+9.4 %`
se convierte en una dispersión del `+4.7 %` sin tendencia limpia, y la pendiente
global pasa de `0.2835` a `0.2552`.

> La afirmación de §3.3 de las notas — «el exponente efectivo medido es ~0.29 y
> el régimen asintótico no se ha alcanzado» — **descansa sobre la convención de
> conteo de extremos, no sobre los datos.** No está refutada; está sin decidir.

Esto es exactamente lo que la hoja de ruta anticipa al escribir que la Fase 0
existe «para impedir que una corrección de tamaño finito se interprete como una
señal geométrica». Aquí ni siquiera hay todavía una corrección de tamaño
finito medida: hay un desplazamiento de `O(1)` compitiendo con el efecto que se
quiere medir, en un rango donde `L ~ 12–28` y por tanto `2/L` vale entre el 7 %
y el 16 %.

---

## 4. Bloqueos sobre la pierna de caja

### 4.1 Las filas restringidas a minimales no contrastan el exponente de BG

`dev/explore_3p1_scale_calibration.py:184-186` anota «expect 1» y «expect 1/4»
para `<V>_min` y `<L>_min`. `Min(C)` es una selección **dependiente de `rho`**:
al crecer la densidad los minimales se concentran contra la esquina pasada de
la caja y su volumen futuro medio crece. Los artefactos lo muestran:

| `rho` | `<V>_min / rho` | `<V>_all / rho` |
|---|---|---|
| 500 | 0.25299 | 0.08446 |
| 1 000 | 0.25886 | 0.08472 |
| 2 000 | 0.27703 | 0.08647 |
| 4 000 | 0.28733 | 0.08794 |
| 8 000 | 0.29914 | 0.08821 |

`<V>_all / rho` es plano (`+4.4 %`), como debe ser: `E[sum V]` es exactamente
cuadrático en `rho`. `<V>_min / rho` deriva `+18.2 %`. La línea base contra la
que se comparan las tres filas de minimales no se cumple, de modo que la
desviación «0.3195 frente a 0.25» no mide lo que la anotación dice que mide.
Es el confundido de selección que `CLAUDE.md` obliga a mantener separado del
uso de cardinalidades.

### 4.2 Ninguna pendiente de §3.2 lleva incertidumbre

Reconstruida pendiente por semilla desde las filas comprometidas:

| magnitud | semilla 11 | 12 | 13 | agregada | s.d. | anotada como |
|---|---|---|---|---|---|---|
| `logV_all_vs_logrho` | 1.0365 | 1.0313 | 0.9890 | 1.0179 | 0.0261 | 1 (exacto) |
| `logL_all_vs_logrho` | 0.3089 | 0.3148 | 0.3251 | 0.3161 | 0.0082 | 1/4 |
| `logL_vs_logV_all` | 0.2979 | 0.3053 | 0.3283 | 0.3106 | 0.0159 | 1/4 |
| `logV_min_vs_logrho` | 1.0899 | 1.0629 | 1.0407 | 1.0634 | 0.0247 | 1 — véase §4.1 |
| `logL_min_vs_logrho` | 0.3214 | 0.3123 | 0.3250 | 0.3195 | 0.0065 | 1/4 — véase §4.1 |
| `logL_vs_logV_min` | 0.2948 | 0.2938 | 0.3123 | 0.3005 | 0.0104 | 1/4 — véase §4.1 |

El exponente **exactamente conocido** vale 1 y el diseño lo devuelve como
`1.0179`. Ése es el suelo empírico de ruido y tamaño finito de este diseño con
tres semillas, y debe declararse junto a cualquier desviación que se reporte.

### 4.3 `R = L^4 / V` es cuárticamente sensible al desfase de uno

| `rho` | `<L>_min` | `((L+1)/L)^4` | mediana `R_min` reportada | estimación de primer orden bajo la convención de elementos |
|---|---|---|---|---|
| 500 | 4.498 | 2.232 | 3.449 | 7.70 |
| 1 000 | 5.580 | 1.934 | 3.790 | 7.33 |
| 2 000 | 7.155 | 1.688 | 4.792 | 8.09 |
| 4 000 | 8.755 | 1.541 | 5.248 | 8.09 |
| 8 000 | 10.867 | 1.422 | 5.975 | 8.50 |

La deriva reportada `x1.73` pasa a ser del orden de `x1.10`. La columna de la
derecha es una **estimación de sensibilidad, no un recálculo**: reescala la
mediana por un factor evaluado en la media, y la mediana exacta de
`(L+1)^4 / V` exige volver a correr la pierna, lo cual es trabajo de Fase 1.
Basta, sin embargo, para el propósito de la Fase 0: el titular «`R` deriva
monótonamente y no estabiliza» no es invariante bajo la convención y por tanto
no puede sostenerse todavía.

---

## 5. Procedencia

`dev/verify_3p1_notes_figures.py` certifica **notas contra JSON** y nada más:
no importa ningún generador ni ejecuta ningún barrido. Su veredicto
`ALL FIGURES MATCH` es correcto y se ha reproducido en esta iteración.

El verificador nuevo añade **JSON contra sí mismo**: `mean_L`, `sem_L`,
`L/N^(1/4)`, `local_slopes`, `global_slope` y las seis pendientes de la pierna
de caja se re-derivan desde las `Ls` y las filas crudas; el recuento de
réplicas coincide con la lista de semillas declarada; y toda `N` realizada cae
dentro de 6 sigma de `Poisson(rho * Vol(D))`. Todo pasa.

Lo que **nada** certifica todavía: que los JSON comprometidos sean la salida de
los generadores comprometidos. No hay hash del generador dentro del artefacto
ni commit productor registrado. Cerrarlo requiere una re-ejecución determinista,
que la hoja de ruta asigna explícitamente a la Fase 1 («reproducir primero los
artefactos existentes»), no a la Fase 0.

### 5.1 Tabla única de entradas

| Artefacto | sha256 (16) | Semillas | Réplicas | Tamaños | Proceso | Región |
|---|---|---|---|---|---|---|
| `dev/explore_3p1_bg_reference.py` | `f9a181e2524b7d79` | — | — | — | — | generador intervalar |
| `dev/explore_3p1_bg_reference_precision_results.json` | `eb101d3f63ac6a36` | 101–108 | 8 | `N = 2 000, 8 000, 16 000, 32 000` | binomial | `I(p,q)`, `tau=1` |
| `dev/explore_3p1_bg_reference_results.json` | `5dbb04bc7b1b3f4c` | 21–23 | 3 | `N = 500 … 16 000` | binomial | `I(p,q)`, `tau=1` |
| `dev/explore_3p1_scale_calibration.py` | `a1b67a37a2eed73b` | — | — | — | — | generador de caja |
| `dev/explore_3p1_scale_calibration_results.json` | `e5cb5fb7ba5c3635` | 11–13 | 3 | `rho = 500 … 8 000` | Poisson | `[0,1]^4` |
| `dev/verify_3p1_notes_figures.py` | `816b476eb48c1262` | — | — | — | — | verificador notas↔JSON |
| `dev/PAPER3_3P1_SCALE_NOTES.md` | `230c9c955881cfdd` | — | — | — | — | nota exploratoria |

Commit productor de los cinco primeros: `0338307`. Las tres listas de semillas
son disjuntas, de modo que las tres piernas son independientes; las semillas de
auditoría de esta fase (101–103 para los contrastes de uniformidad, 999 para la
tasa de aceptación) reutilizan deliberadamente las de la pierna de precisión
sólo en contrastes que no producen ninguna cifra reportada.

---

## 6. Separación entre el límite conocido y la corrección que se quiere medir

Lo que es teorema y no se mide:

```text
L (rho V)^(-1/d) -> m_d   en probabilidad, sobre INTERVALOS DE ALEXANDROV
m_2 = 2 exacto;  1.8555 <= m_4 <= 2.5296  (cotas rigurosas)
```

Lo que la Fase 1 se propone medir:

```text
delta(N) := L(N) / N^(1/4) - m_4      con L en la convención que fije GATE_0
```

Es decir, una **corrección de tamaño finito a `N` accesible**, con `m_4`
desconocido dentro de su banda. De aquí se siguen dos consecuencias que la
Fase 1 debe respetar:

1. `m_4` no se conoce puntualmente, sólo acotado. Una curva de `L/N^(1/4)`
   frente a `N` **no puede** separar «la constante vale 2.1» de «la constante
   vale 2.0 más un transitorio» sin una parametrización elegida antes de mirar.
   La hoja de ruta ya lo exige («elegir una parametrización de corrección
   finita antes de mirar resultados nuevos»); este contrato añade que la
   convención de `L` debe fijarse antes que la parametrización, porque la
   desplaza en `O(1)`.
2. Todo lo medido en la caja `[0,1]^4` está fuera del dominio del teorema y no
   puede prestarle apoyo ni recibirlo.

---

## 7. Bloqueos abiertos de `GATE_0`

| id | Bloqueo | Tipo | Cierra en |
|---|---|---|---|
| G0-1 | `dev/explore_3p1_scale_calibration.py:94` cuenta relaciones; el sellado y la pierna intervalar cuentan elementos. §1 de las notas afirma una convención única | definición | decisión + reejecución (Fase 1) |
| G0-2 | La pierna intervalar excluye `p` y `q`; la pendiente global va de `0.2835` a `0.2552` según se cuenten | definición | decisión |
| G0-3 | Ninguna pendiente de §3.2 lleva incertidumbre; el exponente exacto 1 sale `1.0179` | estadística | redacción + réplicas (Fase 1) |
| G0-4 | «expect 1» y «expect 1/4» son líneas base falsas para las filas de minimales: `<V>_min/rho` deriva `+18.2 %` | línea base | corrección de anotación |
| G0-5 | `R` es cuártico en `L`: la deriva `x1.73` pasa a `~x1.10` bajo la otra convención | interpretación | reejecución (Fase 1) |
| G0-6 | Notas y hoja de ruta llaman Poisson a ambas piernas; la intervalar es binomial | documentación | redacción |
| G0-7 | Nada certifica JSON contra generador | procedencia | reejecución (Fase 1) |
| G0-8 | `dev/explore_3p1_bg_reference.py:1` y `dev/explore_3p1_scale_calibration.py:1` siguen diciendo «Paper II», lo que §0 de las notas prohíbe explícitamente | documentación | redacción |
| G0-9 | 3 de 10 filas violan la cota inferior rigurosa de `m_4` bajo la normalización reportada; 0 de 10 la violan contando extremos | **decide G0-2** | decisión |

```text
GATE_0 = BLOCKED
```

La hoja de ruta lo prescribe: «Si hay ambigüedad en el conteo de extremos, en
la normalización o en la procedencia de una cifra, la fase no avanza». Hay
ambigüedad en las tres.

---

## 8. Resolución propuesta (requiere firma; nada de esto se ha aplicado)

Ninguna de estas decisiones se ha ejecutado. Se proponen para su firma porque
la Fase 0 debe *fijar* definiciones, y fijarlas es una decisión del PI, no del
auditor.

1. **Convención única de `L`, en toda la línea 3+1**: número de **elementos**,
   con los dos extremos de Alexandrov incluidos en la pierna intervalar.
   Justificación: es la convención del enunciado de Brightwell–Gregory tal como
   lo cita la fuente local, es la del estimador sellado, y es la única de las
   tres candidatas bajo la cual ninguna fila viola la cota rigurosa de `m_4`
   (G0-9). Consecuencia: `dev/explore_3p1_scale_calibration.py` debe reportar
   `L + 1` y sus `R` deben recalcularse; ambas cosas son trabajo de Fase 1.
2. **`N` sigue siendo el interior**, sin los extremos, porque los extremos no
   son puntos sembrados. Con eso `rho * Vol = N` exactamente y la normalización
   de BG es literal.
3. **Declarar la pierna intervalar como binomial** (Poisson condicionado a
   `N = n`) en las notas y en la hoja de ruta. La elección es legítima y además
   deseable — es el canal `N = n` del que ya habla `CLAUDE.md` — pero debe
   decirse.
4. **Retirar «expect 1» y «expect 1/4» de las filas de minimales** y
   reetiquetarlas como magnitudes con línea base desconocida y dependiente de
   `rho`, o retirarlas del contraste de escala.
5. **Toda pendiente reportada lleva su dispersión entre semillas**, y toda
   desviación se compara contra el suelo que devuelve el exponente exactamente
   conocido en el mismo diseño.
6. **Corregir las dos cabeceras «Paper II»** a Paper III.
7. **`R` no se interpreta en absoluto** hasta que 1 y 5 estén aplicados y la
   pierna de caja reejecutada. La frase «`R` deriva y no estabiliza» queda
   retirada del techo de claims hasta entonces.

Aplicados 1–7, `GATE_0` puede reevaluarse; G0-1, G0-5 y G0-7 sólo cierran con
la reejecución determinista que la Fase 1 ya tiene autorizada como su primer
paso.

## 9. Techo de claims tras esta iteración

Se **estrecha** respecto al de la hoja de ruta, porque la corrección de tamaño
finito todavía no está medida:

> En intervalos de Alexandrov de Minkowski 3+1, y en el rango `N <= 32 000`
> explorado, la longitud de cadena normalizada `L / N^(1/4)` es compatible con
> la banda rigurosa `1.8555 <= m_4 <= 2.5296`. La magnitud y el signo de su
> desviación respecto al límite dependen todavía de la convención de conteo de
> extremos y no están determinados por los datos existentes.

Queda fuera: cualquier afirmación sobre el exponente efectivo, sobre si el
régimen asintótico se ha alcanzado, sobre la deriva de `R`, y todo lo que la
hoja de ruta ya excluía.
