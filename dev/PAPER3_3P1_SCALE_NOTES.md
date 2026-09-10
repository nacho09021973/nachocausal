# Paper III (3+1D) — Formalización de la ley de escala order-only

STATUS: NOTAS_DE_EXPLORACION / NO_ES_PREREGISTRO / NO_SELLA_NADA
DATE: 2026-09-08
CAPA: dev/ (exploración). No toca `nachocausal/` ni ningún seal.

---

## 0. ADVERTENCIA DE ASIGNACIÓN EDITORIAL (leer antes que nada)

> **Este material pertenece al trabajo preparatorio del Paper III (3+1D).**
>
> **Paper II queda reservado al puente matemático en 1+1D** y no debe citar,
> incorporar ni apoyarse en nada de este documento.
>
> Este fichero se llamó `dev/PAPER2_3P1_SCALE_NOTES.md` durante su redacción
> inicial (2026-09-08, sin commit). Renombrado a `PAPER3_...` en el mismo
> commit de preservación; no había ninguna referencia externa que romper, y la
> única referencia interna (`dev/explore_3p1_scale_calibration.py`) se actualizó
> en el mismo commit. Cualquier nota anterior que hable de «Paper II» en
> relación con 3+1D está mal asignada y debe leerse como Paper III.

Este documento ejecuta el paso 1 del orden propuesto en el protocolo revisado
(«formalizar el teorema/hipótesis»), corrige dos entradas de su tabla de estado
lógico, y deja medidas las dos primeras magnitudes.

---

## 1. Notación (compatible con el repo)

Para `i` en un causet finito `C` obtenido por sprinkling en una región `D`:

```text
V(i) = |J^+(i) cap D|                  (cardinalidad del futuro, order-only)
L(i) = longitud de la cadena futura maxima desde i   (order-only)
Vol_+(x) = vol(J^+(x) cap D)           (volumen continuo; NO se llama V)
R(i) = L(i)^4 / V(i)
```

La convención `V`/`L` sobre minimales ya existe congelada en el repo:
`docs/preregistration_new_geometry_future_observables.md` §1.

---

## 2. Tabla de estado lógico — corregida

| Afirmación | Estado propuesto | Estado corregido |
|---|---|---|
| `E[V(i) | x] = rho · Vol_+(x)` | identidad elemental | **correcto** (Campbell/Poisson) |
| `V(i)/rho -> Vol_+(x)` | no demostrado | **conocido y elemental**: LGN para el Poisson; la varianza es `rho·Vol_+`, luego el error relativo es `O((rho·Vol_+)^{-1/2})`. No hace falta demostrarlo, hace falta *acotar el borde* |
| `L(i) ~ c_4 [rho·Vol_+]^{1/4}` | **hipótesis nueva** | **NO es nueva y NO está autorizada en esa generalidad.** Es el teorema de Brightwell–Gregory (1991), **cuyo dominio de validez son los intervalos de Alexandrov**: `L (rho V)^{-1/d} -> m_d` en probabilidad, con `m_2 = 2` exacto y `m_4` sólo acotado. Ancla local: `biblioteca/derived-md/Dynamics_of_Causal_Sets_arXiv_gr-qc0212064.md:283`; `biblioteca/derived-md/Directions_in_Causal_Set_QG_arXiv1103.6272.md:131` |
| `L(i) ~ c_4 V(i)^{1/4}` | consecuencia condicional | **consecuencia condicional con constante NO universal**: `J^+(i) cap D` es un futuro *truncado por la caja*, no un intervalo. `L` mide el tiempo propio máximo disponible `tau_max(x)`; `V` mide un volumen. Son funcionales de forma independientes |
| Detección de horizonte vía `V` | imposible por el confound | **correcto, y ya registrado en el repo** (ver §5) |
| Detección vía perfil conjunto | objetivo abierto | **abierto, con siete cierres negativos previos en 1+1D** (§5) |

### 2.1 Salvaguardas que deben viajar con cualquier uso de estas fórmulas

1. **Brightwell–Gregory se aplica a intervalos de Alexandrov.** Ese es su
   enunciado y su dominio de validez.
2. **BG no autoriza `L ~ c_4 V^{1/4}` para futuros truncados de forma
   arbitraria.** Extenderlo a `J^+(i) cap D` con `D` de forma cualquiera es una
   extrapolación fuera del teorema, no un corolario.
3. **`R = L^4 / V` es un CANDIDATO a observable de forma, no un calibrador
   universal.** No puede usarse para fijar escala absoluta ni para normalizar
   entre geometrías distintas.
4. **El fallo medido a `N` accesible es fallo del TEST OPERATIVO de
   estabilización, no refutación del límite asintótico.** BG sigue siendo
   verdadero; lo que estas medidas muestran es que el régimen asintótico no se
   alcanza a los `N` que podemos correr.
5. **Ocho semillas y `N <= 32 000` sólo permiten una conclusión exploratoria.**
   Ninguna cifra de §3 tiene estatus confirmatorio, ni control de error de tipo
   I, ni umbral pre-registrado.
6. **La bola excindida de Minkowski (§4.1) introduce una frontera timelike, no
   un horizonte nulo.** Es un control de truncación, no un modelo de horizonte.

### 2.2 Lo que sí es nuevo, y es el contenido real del protocolo

`R(i) = L(i)^4 / V(i)` es **adimensional y libre de `rho`**: bajo el escalado
exacto de un Poisson en región fija, `V ~ rho` y `L ~ rho^{1/4}`, luego `R` es
asintóticamente una **funcional de la forma del futuro truncado**. En el caso
intervalo, `R -> m_4^4`. Cualquier desviación de ese valor mediría *cuánto se
aparta el futuro truncado de un intervalo* — sujeto a la salvaguarda 3.

Esa es la formulación defendible para el Paper III: **`R` como candidato a
estimador de forma**, siendo la forma (no el déficit de volumen) lo único que
podría distinguir truncación por interfaz de truncación por borde de caja.

---

## 3. Medidas hechas (3+1 Minkowski, 2026-09-08) — EXPLORATORIAS

Scripts: `dev/explore_3p1_bg_reference.py`, `dev/explore_3p1_scale_calibration.py`.

Estatus de toda esta sección: **exploratorio**. Ver salvaguarda 5 (§2.1).

### 3.1 Pierna de referencia (intervalo de Alexandrov 4D, donde BG *es* teorema)

> **Clase de proceso puntual (R003, 2026-09-10).** Esta pierna es un **proceso
> binomial**: extrae un número fijo de puntos i.i.d. uniformes en el intervalo de
> Alexandrov, es decir un Poisson condicionado a `N = n`
> (`dev/explore_3p1_bg_reference.py:32-41`). La elección de `N` fijo es
> deliberada y legítima — es el canal `N = n` de `CLAUDE.md` — pero no debe
> describirse como «sprinkling de Poisson».

Cadena máxima extremo-a-extremo, **8 semillas** (101..108) por punto:

| N | `<L>` ± e.e. | `L/N^{1/4}` |
|---|---|---|
| 2 000 | 12.625 ± 0.375 | 1.8879 |
| 8 000 | 18.000 ± 0.189 | 1.9033 |
| 16 000 | 22.625 ± 0.420 | 2.0117 |
| 32 000 | 27.625 ± 0.375 | 2.0655 |

Pendientes locales: `[0.2559, 0.3299, 0.2881]`. En la última década: **0.2881**.

`L/N^{1/4}` cae dentro de la banda conocida para `m_4` y **sigue subiendo** a
`N = 3.2e4`: el régimen asintótico de BG no se ha alcanzado. Esto es
consistente con BG, no contra BG (salvaguarda 4).

Existe además una pierna preliminar de 3 semillas (21..23, `N <= 16 000`) en
`dev/explore_3p1_bg_reference_results.json`, con pendiente global 0.2902. No es
la tabla de arriba y no debe mezclarse con ella.

### 3.2 Pierna de caja (futuros truncados, `rho` = 500 … 8 000, 3 semillas)

> **Clase de proceso puntual (R003, 2026-09-10).** Esta pierna sí es un proceso
> de **Poisson** homogéneo de intensidad `rho`
> (`dev/explore_3p1_scale_calibration.py:59`). Ambas piernas son homogéneas
> respecto a la medida de Lebesgue, que en coordenadas inerciales coincide con el
> volumen de Minkowski, pero **no son la misma clase de proceso** que la pierna
> intervalar de §3.1.

```text
d log <V>_all / d log rho     = 1.0179    (esperado 1)       -> OK
d log <L>_all / d log rho     = 0.3161    (esperado 0.25)
d log <L>_all / d log <V>_all = 0.3106    (esperado 0.25)
d log <V>_min / d log rho     = 1.0634    (esperado 1)
d log <L>_min / d log rho     = 0.3195    (esperado 0.25)
d log <L>_min / d log <V>_min = 0.3005    (esperado 0.25)
```

Mediana de `R` sobre minimales, **promediada sobre las 3 semillas**, al subir
`rho` x16:

```text
rho =   500 -> 3.449
rho =  1000 -> 3.790
rho =  2000 -> 4.792
rho =  4000 -> 5.248
rho =  8000 -> 5.975      (deriva monótona; NO estabiliza)
```

### 3.3 Consecuencia operativa

> El test primario propuesto — `d log L / d log V -> 1/4` — **no pasa a los `N`
> accesibles ni siquiera en el caso intervalo, donde la ley es un teorema.**
> El exponente efectivo medido es ~0.29–0.31 y `R` deriva monótonamente.

Lectura correcta (salvaguarda 4): esto **falsa el test operativo de
estabilización a `N` accesible**, no el límite asintótico. Un Paper III que
apoyara una afirmación en «`R` se estabiliza» estaría leyendo un transitorio de
tamaño finito. La Fase I debe reformularse como **medida de la corrección de
tamaño finito** (`L/N^{1/4}` vs `N`), con la pierna intervalo como ancla, y no
como verificación del exponente 1/4.

### 3.4 Procedencia de cada cifra (cada número → su artefacto)

| Cifra en el texto | Artefacto | Campo |
|---|---|---|
| Tabla §3.1 (`<L>`, e.e., `L/N^{1/4}`) | `dev/explore_3p1_bg_reference_precision_results.json` | `rows[*].mean_L`, `.sem_L`, `.L_over_N_quarter` |
| Pendientes locales §3.1 | idem | `local_slopes` |
| Pendiente global 0.2902 (pierna 3 semillas) | `dev/explore_3p1_bg_reference_results.json` | `global_slope` |
| Las 6 pendientes de §3.2 | `dev/explore_3p1_scale_calibration_results.json` | `slopes.*` |
| Medianas de `R` §3.2 | idem | media sobre `rows[*].median_R_min` agrupadas por `rho` |

Reproducción:

```bash
python3 dev/explore_3p1_bg_reference.py              # pierna 3 semillas
python3 dev/explore_3p1_bg_reference.py --precision   # tabla de 3.1
python3 dev/explore_3p1_scale_calibration.py          # pierna de caja
python3 dev/verify_3p1_notes_figures.py               # comprueba nota vs JSON
```

`dev/verify_3p1_notes_figures.py` no ejecuta ningún barrido: sólo lee los JSON
y sale con codigo 0 si y solo si cada cifra de 3.1 y 3.2 coincide con su
artefacto. Verificado en verde el 2026-09-08.

Todo es determinista (semillas fijas en el código); no hay estado externo.

---

## 4. El bloqueo 3+1 es de tres capas, no una

El protocolo dice «el generador existente produce embeddings de dimensión 2».
Es cierto pero incompleto:

1. **Generador congelado.** `nachocausal/generator.py:37` es 2D por
   construcción y está sellado. No debe tocarse. Todo 3+1 vive en `dev/`.
2. **La medida de sprinkling no porta.** El argumento Glue-3 del repo
   (`nachocausal/generator.py:10-12`) es que en EF 2D `det g = -1`, luego
   uniforme-en-coordenadas == Poisson de volumen natural. En EF 3+1
   `sqrt(-g) = r^2 sin(theta)`: un sprinkle uniforme en coordenadas sería
   **incorrecto**, y el gate chi-cuadrado de uniformidad marginal por eje
   (`generator.py:53-84`) no es el gate adecuado.
3. **No hay causalidad en forma cerrada.** `past_matrix_fast`
   (`nachocausal/generator.py:88-133`) es cerrado sólo porque la causalidad
   Schwarzschild 2D se integra exactamente vía la coordenada tortuga. En
   Schwarzschild 3+1 decidir `p < q` exige un **problema de contorno de
   geodésicas nulas** (rama de llegada más temprana, He–Rideout), con ramas
   multi-vuelta inestables cerca de la esfera de fotones `r = 3M`. Ancla
   local: `biblioteca/Investigación Causalidad Schwarzschild R19M.md`.

**3+1 Minkowski, en cambio, es gratis** (`dt >= |dx|`, cerrado y vectorizable):
por eso la Fase I ya pudo correrse.

### 4.1 Peldaño intermedio propuesto: excisión esférica estática

Antes del BVP geodésico hay un control de coste bajo que da una **interfaz
truncante** con causalidad cerrada: Minkowski 3+1 con una bola espacial
excindida. `p < q` sii `dt >= d_obs(x_p, x_q)`, donde `d_obs` es la longitud
del camino espacial más corto que evita la bola (tangente–arco–tangente, forma
cerrada). `d_obs` es una métrica, luego la relación es transitiva.

**Advertencia obligatoria (salvaguarda 6):** esa frontera es **timelike, no un
horizonte nulo** — trunca futuros pero no es unidireccional. Pasar ese control
es **necesario y no suficiente** para hablar de horizonte. Sirve exactamente
para lo que el protocolo pide: separar «hay una interfaz que trunca» de «la
interfaz es un horizonte».

---

## 5. Lo que el repo ya cerró y no debe re-abrirse como si fuera nuevo

- El gemelo Minkowski emparejado **ya es el diseño del repo**: el mismo point
  cloud genera BH y MINK (`nachocausal/generator.py:41-49`). La Fase III no
  necesita inventarlo.
- `V(i)`, `L(i)` sobre minimales **ya se corrieron en 1+1D** bajo contrato
  congelado y el resultado está sellado:
  `docs/new_geometry_future_observables_addendum.md` —
  `BH_MINK_DISPERSION_DIFFERENCE_DETECTED`, explícitamente **sin localizar**
  horizonte.
- La línea de localizadores está **cerrada**:
  `docs/comite/comite_decision_042_c1-c5-localizer-line-closure.md`
  (`C1_TO_C5_LOCALIZER_LINE = EXHAUSTED_FOR_LOCALIZATION`), y el ledger de
  siete fracasos con el mismo obstáculo está firmado en la decisión 046.
  Lectura del programa: *el orden RECUERDA pero no DEFINE*.

Conclusión: la Fase II en 1+1D **no debe re-ejecutarse**. Su veredicto ya
existe (separación sí, localización no) y `wp5_gated_by_3plus1d_goal` obliga a
que todo trabajo 1+1D sea instrumental al objetivo 3+1D.

---

## 6. Orden revisado (Paper III)

```text
(0) formalizar        -> este documento (atribución BG correcta; R como
                         CANDIDATO a funcional de forma, no calibrador)
(1) Fase I 3+1 MINK   -> HECHO (exploratorio): exponente efectivo ~0.29-0.31,
                         R deriva. Reformular Fase I como medida de corrección
                         de tamaño finito, con pierna intervalo como ancla.
(2) excisión esférica -> causalidad cerrada, interfaz truncante TIMELIKE.
                         Fases II y III con caja gemela emparejada.
                         Necesario-no-suficiente para «horizonte».
(3) Schwarzschild 3+1 -> subproyecto propio: BVP nulo He-Rideout,
                         medida r^2 sin(theta), gate de uniformidad nuevo.
                         No abrir antes de (2).
```

Nada de lo anterior está congelado ni autorizado a ejecución de validación.
