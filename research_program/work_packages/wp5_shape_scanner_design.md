# WP5 — Shape scanner design spec (Paso B of the WP5 roadmap)

> **Status: DESIGN_ONLY / NO_NUMERICS / NO_IMPLEMENTATION / NO_PUBLIC_NOVELTY_CLAIM.** Este
> documento no ejecuta código, no genera datos, no modifica ningún seal, no crea ni modifica
> ningún script. Es la especificación de contrato para el **Paso B** del roadmap de
> `research_program/work_packages/wp5_order_only_blindness_map_definition.md` §5 ("Escáner
> determinista de formas, extendiendo el método ya existente y verificado de
> `wp4_kappa_numeric_reference.py`"). Ninguna función, flag, ruta de import o API nueva se declara
> aquí como existente: todo lo citado es literal del código ya presente en el repo (leído, no
> modificado), y todo lo que falta se marca explícitamente como "required minimal
> extraction/refactor" — no implementado, no resuelto por invención.

**Ficheros leídos para esta especificación (sin modificar ninguno):**
`research_program/work_packages/wp5_order_only_blindness_map_definition.md` (en adelante
"WP5-def"), `research_program/work_packages/wp4_fisher_localization_floor.md` (en adelante
"WP4-floor"), `research_program/work_packages/wp4_kappa_numeric_reference.py` (en adelante
"kappa-script" — **untracked** en este repo al momento de escribir esto: `git status --short`
lo lista con `??`; ver §8), y los documentos que WP5-def cita explícitamente
(`wp4_two_point_theorem.md`, `research_program/models/first_witness_pair_candidates.md`, §1 y
Lema 1).

## 1. Estado

WP5 scanner design draft. `DESIGN_ONLY / NO_NUMERICS / NO_IMPLEMENTATION /
NOT_A_PUBLIC_NOVELTY_CLAIM`. No se ha escrito, ejecutado ni planificado en detalle ningún código;
esto es un contrato, no un esqueleto de implementación.

## 2. Pregunta física concreta

**No es** "reconstruir el horizonte". **Es**: para la familia regular QMD ya definida y probada en
WP4-floor §4 (diamantes causales con esquinas EF fijas, régimen 3 de WP5-def §4), cartografiar —
sobre el espacio adimensional de formas de ese diamante — las regiones donde la cota order-only ya
probada garantiza ceguera a escala `ell`, frente a las regiones donde esa cota simplemente no
aplica (sin que eso implique visibilidad).

La asimetría lógica de WP5-def §3 se repite aquí sin modificación, porque el escáner **no la
cierra, solo la evalúa numéricamente shape por shape**:

`ell * sqrt( n * I_points ) << 1  ==>  blindness proven`
`ell * sqrt( n * I_points ) >> 1  ==>  candidate visible, NOT proven`

El escáner produce, para cada forma, un número (`kappa`, en dos variantes no intercambiables —
`kappa_point` / `kappa_bar`, ver §3 — y de ahí `delta_theta_floor/ell`) que solo certifica el lado
izquierdo de esa asimetría, y solo cuando la variante usada es la que WP4-floor licencia para ese
propósito. Ningún output del escáner, presente o futuro, puede etiquetarse "visible" o
"recuperable" — solo "candidate visible" (WP5-def §1.b, §3).

## 3. Objeto matemático

**`kappa_point(tau0) := V(tau0) * I(tau0)`.** WP4-floor §5a, Proposición 6, define
`kappa(tau) := V(tau) * I(tau)` y prueba que es exactamente invariante bajo dilatación (depende
solo de la forma adimensional, nunca del tamaño absoluto). Este documento lo llama `kappa_point`
para distinguirlo de `kappa_bar` (subsección siguiente). El kappa-script implementa exactamente
esta convención puntual: `kappa_reference(...)` devuelve `V * ests[-1]` (línea 130), donde
`V = fam0["A"]` (línea 122, el área `g_tau` exacta, `det g_t = -1`, WP4-floor §4) y `ests[-1]` es
la estimación de `I(tau0)` con el `delta` más fino del barrido (línea 128, vía la expansión QMD de
la Proposición 4). **No hay discrepancia de normalización en la definición de `kappa_point` en
sí**: coincide con WP4-floor Proposición 6 símbolo a símbolo. Su estatus como salida validable — no
como definición — se resuelve en la subsección siguiente.

**`delta_theta_floor / ell`.** WP4-floor §5a da `delta_n / ell = 1 / sqrt(V(tau)*Ibar) =: 1 /
sqrt(kappa_bar)` (con `Ibar` el supremo de intervalo definido abajo, no `I(tau0)` puntual). Aquí
`theta` es el nombre genérico del parámetro de WP5-def §1 (`B(theta, theta', n)`); en la
instanciación concreta del régimen 3 ese parámetro se llama `tau` en WP4-floor. Este documento usa
`delta_theta_floor` únicamente como sinónimo notacional de `delta_tau` de WP4-floor §5a — no se
introduce ningún objeto nuevo.

### Normalization decision required before implementation

WP4-floor define dos objetos relacionados pero **no intercambiables**. Cualquier implementación de
Paso B debe distinguirlos explícitamente y nunca reportarlos bajo el mismo nombre o columna.

**A. `kappa_point(form; tau0) := V(tau0) * I(tau0)`.** Es exactamente el objeto de la Proposición 6
de WP4-floor (§5a): un invariante de dilatación *probado*, evaluado puntualmente en un `tau0`
concreto (`I(tau0)` estimado vía la expansión QMD de la Proposición 4, tal como ya hace
`kappa_reference` del kappa-script, línea 130). Es un resultado matemático genuino y citable
**como diagnóstico de forma** — pero WP4-floor **no lo licencia** como sustituto directo del
objeto que respalda el suelo estadístico probado (ver B): el Teorema de §5 y su cota de `TV` usan
`Ibar := sup_{tau in [tau0,tau1]} I(tau)` (Proposición 4), el supremo sobre un intervalo, y por
definición de supremo `Ibar >= I(tau0)` para cualquier `tau0` dentro de ese intervalo. Sustituir
`Ibar` por `I(tau0)` en la cota de `TV` puede **subestimar** el verdadero `Ibar` y así invalidar la
cota como cota superior. Por eso toda curva `delta_theta_floor/ell = 1/sqrt(kappa_point)` debe
marcarse **`DIAGNOSTIC_ONLY`**: informa sobre la geometría de la forma, pero no es, por sí sola, el
suelo de localización que WP4-floor prueba.

**B. `kappa_bar(form; tau0, tau1) := V_ref * Ibar_{[tau0,tau1]}`, con `Ibar := sup_{tau in
[tau0,tau1]} I(tau)`.** Es el objeto que el Teorema de §5 de WP4-floor y su Corolario de §5a usan
realmente para el suelo estadístico probado (`TV(Q^n) <= (|delta|/2) sqrt(n*Ibar)`, y
`delta_n/ell ~ 1/sqrt(kappa_bar)`). WP4-floor mismo advierte que evaluar `V` en un único punto de
referencia del intervalo es "exacto si `V` es constante a través de `[tau_0, tau_1]`, una
aproximación `O(1)` para un rango estrecho ... en otro caso rastreado como función de `tau`" — esa
advertencia debe propagarse íntegra a cualquier fila del CSV que reporte `kappa_bar`
(`check_summary`, §6), nunca silenciarse. **Esta es la única salida `VALIDATION_GRADE`** para las
curvas de nivel de `delta_theta_floor/ell` de la figura de §6 — pero exige computar `Ibar` como
supremo genuino sobre un intervalo `[tau0,tau1]` explícito, algo que **ninguna pieza del
kappa-script implementa hoy** (`kappa_reference` solo evalúa `I` en un único `t0`, nunca un supremo
sobre un rango de `tau`; ver §5). Construir esa maquinaria (evaluar `I(tau)` en una malla de `tau`
dentro de `[tau0,tau1]` y tomar el máximo, con su propio control de estabilidad) es **required
minimal extraction**, no algo a inventar ni implementar en este documento.

**Decisión tomada en este documento (no queda como blocker conceptual — WP4-floor sí lo fija).**
`kappa_bar`, no `kappa_point`, es el objeto que respalda el suelo estadístico probado. El
kappa-script, tal y como existe hoy, solo calcula `kappa_point`. En consecuencia, **ninguna cifra
que el kappa-script produce hoy** (ni las tres formas de referencia ni el barrido `lambda` de
`__main__`) **es, en sentido estricto, un `kappa_bar` validado** — son, con la propia terminología
de WP4-floor, "numerically illustrated (NUMERICAL, not proved)" (§5a/§6 de WP4-floor), consistente
con marcarlas `DIAGNOSTIC_ONLY` en el contrato de este documento. El blocker que queda (§8.1) no es
"cuál normalización corresponde" (resuelto arriba) sino **la ausencia de una implementación del
supremo sobre intervalo** — un gap de implementación, no de definición física.

**Regla fail-closed obligatoria.** Si al implementar Paso B no puede determinarse, para una forma o
punto de malla dado, que `kappa_bar` se calculó como supremo genuino sobre un intervalo
`[tau0,tau1]` explícitamente declarado (con `V` constante en ese intervalo o con la aproximación
`O(1)` explícitamente registrada en `check_summary`), el escáner **puede** reportar `V`, `I`
(puntual) y `kappa_point` como diagnóstico, pero **no puede** reportar `delta_theta_floor/ell` con
estatus `VALIDATED_BOUND`. En ese caso el estatus debe ser `BLOCKED_NORMALIZATION_AMBIGUITY` (§6),
nunca omitir el campo silenciosamente ni rellenarlo con el valor puntual sin la etiqueta.

## 4. Parámetros de forma

**Nombres reales (no inventados), del kappa-script:** `make_builder(r_p, r_q, v_p, v_q)` y
`kappa_reference(r_p, r_q, v_p, v_q, t0=1.0, deltas=(0.04, 0.02, 0.01))`. No hay en el script
ninguna variable ya nombrada `r_p_over_tau` ni equivalente: las razones adimensionales de WP4-floor
§5a (`r_p/tau_0`, `r_q/tau_0`, `v_p/tau_0`, `v_q/tau_0`) se obtienen hoy **solo por convención**,
porque las tres llamadas existentes en `__main__` (líneas 136-138, 149-158) siempre fijan
`t0 = 1.0` (el default), de modo que `r_p`, `r_q`, `v_p`, `v_q` pasados son numéricamente idénticos
a sus razones sobre `tau`. El script **no divide explícitamente por `t0` en ningún punto** para
formar esas razones; si un futuro escáner quisiera barrer también `t0 != 1` tendría que introducir
esa normalización explícita — **required minimal extraction**: una función que tome
`(r_p, r_q, v_p, v_q, t0)` y devuelva las cuatro razones adimensionales, hoy inexistente.

**Malla 2D propuesta (ejemplo, no vinculante).** Usando exactamente los nombres reales del script:
barrer `r_p` (con `t0=1.0` fijo, luego `r_p` ≡ `r_p/tau`) contra `r_q` (ídem), manteniendo `v_p =
0.0` y `v_q` fijo a un valor de referencia — replicando la convención de las tres formas ya
existentes en `__main__` (líneas 136-138), que siempre usan `v_p=0.0`. **Esto es una elección de
diseño para el Paso B, no algo que el script ya haga**: las tres formas de referencia y el barrido
`lambda` del script (líneas 149-158) varían `r_p`, `r_q` y `v_q` **acoplados** (no hay hoy en el
script ninguna rebanada 2D con `v_q` fijo) — se ofrece aquí como la generalización más simple de
esas llamadas, consistente con sus variables, pero no como algo ya probado o ejecutado.

**`v_p = 0.0` como WLOG.** Las tres formas de referencia y el barrido `lambda` fijan `v_p = 0.0`
sin que WP4-floor declare explícitamente una invarianza bajo traslación en `v` que lo justifique
como "sin pérdida de generalidad" (WP4-floor sí prueba invarianza bajo **dilatación**, Proposición
6 — no bajo traslación en `v`). Es plausible por la estaticidad de `g_tau` (§4 de WP4-floor), pero
no está escrito como lema. El escáner heredaría esta convención sin re-derivarla — se marca como
supuesto heredado, no resuelto aquí (ver §8.2).

**Dominio admisible.** El único chequeo ejecutable existente es el `assert Up < 0 < Uq,
"reference shape must straddle the horizon (Up<0<Uq)"` dentro de `build_family` (línea 75 del
kappa-script), que — dado `Utilde(t,v,r) = -exp(-v/2t)*W(t,r)` y el signo de
`W(t,r)=exp(r/t)*(r/t-1)` cambiando en `r=t` — equivale exactamente a la condición textual de
WP4-floor §4 ("Construction": `0 < r_q < tau_0 <= tau_1 < r_p`). No hay ningún límite numérico
adicional derivado físicamente: el bracket `(1e-10, 60.0)` de `brentq` dentro de `r_of_U` (línea
69) es un rango numérico de conveniencia para la búsqueda de raíces, no una cota física — un
barrido de malla que empuje `r_p/tau` fuera de ese bracket simplemente hará fallar `brentq`
(comportamiento a preservar como fail-closed, §7, no a ampliar sin criterio). **No se fijan aquí
límites numéricos definitivos de malla** (p.ej. `r_p/tau in [1.05, 5]`); cualquier rango concreto
para Paso B debe marcarse en el propio código como placeholder auditable, citando qué chequeo
existente (el `assert` de la línea 75, o el bracket de la línea 69) lo motiva.

## 5. Reutilización del pipeline existente

Todo lo listado es código ya presente en `wp4_kappa_numeric_reference.py`, citado por nombre y
línea; nada de esto es una función nueva.

- **Cuadratura determinista:** `np.trapz` para `m1`, `m2`, `A` (líneas 83-86, inline dentro de
  `build_family`); `cumulative_trapezoid` para las CDFs `F`, `G` (líneas 88-89, ídem); rejilla vía
  `np.linspace` (líneas 76-77); cuadratura de punto medio sobre el cuadrado unidad en
  `hellinger_sq(copula_density, fam_a, fam_b, M=16)` (líneas 108-116, **esta sí es una función de
  nivel de módulo, reutilizable directamente**).
- **Búsqueda de raíces:** closure `r_of_U(t, v, Utarget, bracket=(1e-10, 60.0))` (líneas 69-71),
  definida dentro de `make_builder`, vía `scipy.optimize.brentq` con `xtol=rtol=1e-14`. No es una
  función de nivel de módulo — está anidada (inline), cerrada sobre `r_p, r_q, v_p, v_q` de
  `make_builder`.
- **Cálculo de `V(tau)`:** `A = np.trapz(m2, vgrid)` (línea 85, inline dentro de `build_family`),
  expuesto como `fam["A"]` en el diccionario devuelto (línea 92), y reexpuesto como `V =
  fam0["A"]` dentro de `kappa_reference` (línea 122). No existe una función independiente
  `V(tau)`; es un valor intermedio del diccionario `fam`.
- **Cálculo de `I(tau)`:** no es una función aislada tampoco — es el bloque `for delta in deltas:
  ... ests.append(4.0 * H2 / delta**2)` dentro de `kappa_reference` (líneas 124-128), que llama a
  `build_family` dos veces (`t0 ± delta/2`) y a `hellinger_sq`.
- **Checks de estabilidad:** (a) `assert abs(A - A_check) / A < 1e-6, "cross-axis mass mismatch"`
  (línea 87, inline dentro de `build_family` — chequeo de consistencia cruzada de masa, no una
  función); (b) `stability = abs(ests[-1] - ests[0]) / ests[-1]` (línea 129, dentro de
  `kappa_reference`) — **calculado y devuelto, pero no aserta ni falla nada**: solo se imprime en
  `__main__` (línea 157) para inspección manual. Esto es relevante para §7: hoy el kappa-script
  **no falla automáticamente** si la estabilidad es mala: eso requeriría un umbral explícito, hoy
  inexistente (**required minimal extraction**).
- **Normalización / cópula:** closure `copula_density(fam, x, y)` (líneas 98-103) y los
  interpoladores PCHIP `Finv`, `Ginv`, `m1`, `m2` (líneas 93-94, `PchipInterpolator`) — todos
  inline dentro de `make_builder`, no funciones de módulo independientes.
- **Discrepancia a señalar (no una pieza reutilizable):** el docstring del kappa-script (líneas
  37-40) describe como "sanity check performed (printed)" que "the copula integrates to ~1 over
  the unit square". **Este check no está implementado en el código leído** (ningún cómputo de
  `∫∫ c_tau(x,y) dx dy` sobre el cuadrado unidad aparece en `wp4_kappa_numeric_reference.py`) — se
  documenta aquí como **`required future check, not currently implemented`**, no como una pieza ya
  existente, salvo que una relectura futura del código demuestre lo contrario. El único chequeo de
  masa realmente implementado es el cruce `A` vs `A_check` (línea 87) — y debe describirse **solo
  con su alcance exacto**: es una comprobación de consistencia de la masa total integrada por los
  dos ejes del `(Ũ,v)`-box (`np.trapz(m1, Ugrid)` vs `np.trapz(m2, vgrid)`), no una comprobación de
  que la densidad de cópula `c_tau(x,y)` normalizada en `(x,y)` integra a 1 sobre el cuadrado
  unidad — son afirmaciones distintas y no deben presentarse como equivalentes.
- **Funciones de nivel de módulo directamente importables (en principio):** `W`, `Wp`, `Utilde`,
  `make_builder`, `hellinger_sq`, `kappa_reference`. **Pero:** no hay ningún `__init__.py` en
  `research_program/` (verificado: `find research_program -name "__init__.py"` no devuelve nada),
  y el propio kappa-script está **untracked** (§8.3) — no se puede asumir un mecanismo de import
  de paquete ya funcional. Cómo importar estas funciones desde un futuro script de escaneo (vía
  manipulación de `sys.path`, colocación en el mismo directorio, o un refactor mínimo hacia módulo
  empaquetado) es una decisión abierta de Paso B, no resuelta ni inventada aquí.

## 6. Salidas futuras (sin generarlas)

**CSV futuro — columnas mínimas** (nombres, no contenido — nada se genera aquí). Por la decisión de
§3, `kappa_point` y `kappa_bar` van en **columnas separadas y nunca se mezclan** en la misma
columna ni en la misma curva de la figura sin la etiqueta de estatus correspondiente:

`shape_id; r_p_over_tau; r_q_over_tau; v_p_over_tau; v_q_over_tau; V; I_point; kappa_point;
kappa_bar; kappa_normalization; delta_theta_floor_over_ell; delta_theta_floor_status; status;
failure_reason; check_summary`

- `I_point`: `I(tau0)` puntual (única cantidad que el kappa-script computa hoy).
- `kappa_point` := `V(tau0)*I_point` (§3.A) — siempre diagnosticable; nunca por sí sola
  `VALIDATED_BOUND`.
- `kappa_bar` := `V_ref*Ibar_{[tau0,tau1]}` (§3.B) — vacío/`NaN` mientras no exista la maquinaria de
  supremo sobre intervalo (§3, §5); solo se rellena cuando esa maquinaria exista y se haya aplicado.
- `kappa_normalization` ∈ `{POINT, INTERVAL_SUP, NONE}` — cuál de las dos columnas anteriores
  respalda, si alguna, el valor de `delta_theta_floor_over_ell` de esa fila.
- `delta_theta_floor_over_ell` — `1/sqrt(kappa_bar)` si `kappa_normalization=INTERVAL_SUP`;
  `1/sqrt(kappa_point)` (rotulado diagnóstico) si `kappa_normalization=POINT`; vacío si `NONE`.
- `delta_theta_floor_status` ∈ `{VALIDATED_BOUND, DIAGNOSTIC_ONLY, BLOCKED_NORMALIZATION_AMBIGUITY,
  FAILED_CHECKS}` — ver regla fail-closed de §3: `VALIDATED_BOUND` exige `kappa_normalization=
  INTERVAL_SUP` con el supremo genuinamente calculado; con la maquinaria de hoy (solo `kappa_point`)
  el estatus más alto alcanzable es `DIAGNOSTIC_ONLY`.
- `status` ∈ `{ok, failed}` (nivel geometría/cómputo, independiente del punto anterior);
  `failure_reason` vacío si `status=ok`, con el motivo de fallo — geometría inválida, `NaN`/`Inf`,
  mismatch de masa, root-finding ambiguo — si no; `check_summary` un resumen legible de qué
  chequeos pasaron (p.ej. cross-axis-mass, estabilidad-QMD, y si el check de normalización de
  cópula de §5 llegó a implementarse).

**Figura futura:** curvas de nivel de `delta_theta_floor/ell` sobre la malla 2D de forma (p.ej.
`= 1, 5, 10, 35, ...` — `35` citado porque es el valor de referencia ya obtenido en WP4-floor §5a
para la forma "moderada", con el propio WP4-floor calificándolo "NUMERICAL, not proved", es decir
`DIAGNOSTIC_ONLY` bajo este contrato). Toda curva debe indicar en su leyenda o pie si proviene de
`kappa_point` (`DIAGNOSTIC_ONLY`) o de `kappa_bar` (`VALIDATED_BOUND`) — nunca combinarlas en una
misma curva sin esa distinción. **Leyenda obligatoria** (WP5-def §1.b, §3): el lado de señal baja
(`delta_theta_floor/ell` grande, `ell*sqrt(n*I)<<1`) rotulado **"blindness proven"** — y solo con
esa etiqueta cuando el estatus subyacente sea `VALIDATED_BOUND`, "blindness proven (diagnostic)" o
similar si es `DIAGNOSTIC_ONLY`; el lado de señal alta (`delta_theta_floor/ell` pequeño,
`ell*sqrt(n*I)>>1`) rotulado **"candidate visible / not proven"** — nunca "visible" a secas, bajo
ningún estatus.

## 7. Criterios de aceptación futura

- **Determinista:** cuadratura + `brentq` + PCHIP únicamente; sin generador de números aleatorios
  en ninguna ruta (coincide con el diseño ya existente del kappa-script).
- **Sin sprinkling, sin estimadores Monte Carlo:** ninguna llamada a un proceso de Poisson ni a un
  estimador order-only real (coincide con el alcance ya declarado del kappa-script, líneas 14-17).
- **Reproduce el caso de referencia de WP4 antes de barrer mallas:** el primer chequeo de
  aceptación de cualquier implementación de Paso B debe ser reproducir la forma "A moderate"
  (`r_p=2.0, r_q=0.5, v_p=0.0, v_q=1.0, tau=1`) y obtener `V ~= 1.4717`, `I_point ~= 5.415e-4`,
  `kappa_point ~= 7.97e-4`, `delta_theta_floor/ell ~= 35.4` (WP4-floor §5a, cifras ya publicadas)
  antes de escanear cualquier malla nueva. **Nota de estatus:** esta cifra de referencia es, en el
  propio WP4-floor, "NUMERICAL, not proved" — bajo el contrato de §3/§6 de este documento se
  reproduce y reporta como `kappa_point` / `delta_theta_floor_status=DIAGNOSTIC_ONLY`, no como
  `VALIDATED_BOUND`; reproducirla exactamente es el criterio de aceptación, no una promoción de
  estatus.
- **Checks de estabilidad iguales o más estrictos que WP4:** como mínimo, (a) el assert de
  masa cruzada (`<1e-6`, ya existente, con el alcance exacto descrito en §5 — masa total del
  `(Ũ,v)`-box, no normalización de cópula) por cada punto de malla, no solo por las 3-6 formas
  puntuales originales; (b) un umbral explícito y *aserta­do* (no solo impreso) sobre la
  estabilidad QMD del delta-scan — hoy inexistente, **required minimal extraction**; (c) el check
  de normalización de cópula (`∫∫ c_tau(x,y) dx dy ~= 1`) — **required future check, not currently
  implemented** (§5) — necesario, no opcional, si se quiere igualar o superar el rigor que el
  propio docstring del kappa-script *afirma* (aunque no implementa) tener.
- **Fail-closed ante geometría inválida, `NaN`, `Inf`, integración no normalizada o root-finding
  ambiguo:** cada punto de malla que dispare el `assert` de la línea 75, una excepción de
  `brentq` (bracket sin cambio de signo), un `NaN`/`Inf` en `V`, `I` o `kappa`, o que falle el
  chequeo de masa cruzada, debe registrarse con `status=failed` y `failure_reason` explícito en el
  CSV (§6) — **nunca** silenciarse, interpolarse, ni sustituirse por un valor por defecto.
  Ninguno de estos manejadores de fallo existe hoy en el kappa-script (que usa `assert` desnudo,
  que aborta el proceso) — traducirlos a un registro por-fila fail-closed es **required minimal
  extraction**, no algo ya implementado.
- **No convierte `kappa ~ lambda^6` en teorema:** el escáner (Paso B) es, por diseño, exactamente
  el tipo de evidencia que WP4-floor y WP5-def ya califican como "observación numérica /
  ajuste empírico" (WP5-def §4, §6); ampliar la cobertura de formas no cambia ese estatus. Ninguna
  salida del escáner debe presentarse como derivación del exponente — esa sigue siendo el Paso C,
  no iniciado (WP5-def §5).

## 8. Riesgos / blockers

1. **Normalización `kappa_point` vs `kappa_bar` — RESUELTO conceptualmente, `REQUIRED_BEFORE_
   VALIDATION` en implementación (§3).** WP4-floor sí fija cuál objeto respalda el suelo
   estadístico probado: `kappa_bar` (vía `Ibar` como supremo sobre `[tau_0,tau_1]`), no
   `kappa_point` (Proposición 6, puntual) — ver la decisión de §3. Esto ya **no es una ambigüedad
   sin resolver desde WP4**. Lo que sigue pendiente, y sí bloquea cualquier `VALIDATED_BOUND`, es
   puramente de implementación: el kappa-script no calcula `Ibar` como supremo genuino sobre un
   intervalo (solo `I(tau0)` puntual) — construir esa maquinaria es **required minimal
   extraction**, no algo a resolver por invención. Hasta que exista, todo output del escáner queda
   como máximo en `DIAGNOSTIC_ONLY` o `BLOCKED_NORMALIZATION_AMBIGUITY` (§6), nunca
   `VALIDATED_BOUND`.
2. **`v_p = 0.0` como "sin pérdida de generalidad" no está probado en WP4-floor** — es un supuesto
   heredado de la convención del kappa-script (§4), plausible por estaticidad pero no un lema
   citable.
3. **Estado untracked de `wp4_kappa_numeric_reference.py`.** `git status --short` lo lista como
   `??` en este repo — no está commiteado. Cualquier Paso B que dependa de importarlo como módulo
   debe primero decidir (no aquí) si se commitea, y cómo se referencia desde un script nuevo sin
   empaquetado (`research_program/` no tiene `__init__.py`, §5).
4. **Tightness order-only sigue abierta** (WP5-def §3, WP4-floor §6 item 3): ningún output del
   escáner, por denso que sea el barrido de malla, convierte el lado `candidate visible` en
   `visible` — eso exigiría un estimador order-only explícito o una cota inferior a nivel de
   poset, ninguno de los cuales existe ni se propone aquí. **No bloquea** implementar el escáner en
   modo diagnóstico (`DIAGNOSTIC_ONLY` / incluso un futuro `VALIDATED_BOUND` de `kappa_bar`, que
   certifica solo el lado ciego); **sí bloquea** cualquier claim de visibilidad derivado de sus
   outputs.
5. **Revisión bibliográfica independiente sigue pendiente** (WP5-def §5, Paso D, condición de
   bloqueo explícita) — ningún resultado de Paso B (ni siquiera una malla densa que confirme
   `kappa ~ lambda^6` en más puntos) habilita un claim público de novedad antes de completar ese
   paso. **No bloquea** la implementación diagnóstica del escáner en sí; **sí bloquea** cualquier
   claim público de novedad basado en sus resultados.
6. **`REQUIRED_BEFORE_VALIDATION`: check de normalización de cópula.** El docstring del
   kappa-script afirma haber "impreso" un chequeo de que la cópula integra ~1 sobre el cuadrado
   unidad; ese chequeo **no está implementado** en el código leído (§5) — se documenta como
   `required future check, not currently implemented`, no como pieza ya existente. Necesario para
   que los checks de estabilidad del escáner igualen o superen el rigor que WP4 afirma tener
   (§7), no solo el que efectivamente implementa hoy.
