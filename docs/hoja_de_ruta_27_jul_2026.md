# Hoja de ruta — 27 jul 2026 · comité 045 emitido; candidato 7.1 adjudicado en `fixed_n`

> **Plan REVISABLE, no congelado.** No es pre-registración, no fija umbrales, no autoriza
> ejecuciones ni implementaciones por sí mismo. Mantener `RESPECT_SEAL_FREEZE`,
> `NO_RECONSTRUCTION_CLAIM`, `NO_GROUND_TRUTH_LEAKAGE`, `NO_POST_HOC_TUNING` y
> `NO_THRESHOLD_LOOSENING`. Registro de sesión, una por fecha; no sustituye a las hojas anteriores
> (`docs/hoja_de_ruta_23_jun_2026.md` … `docs/hoja_de_ruta_25_jul_2026.md`, `docs/roadmap.md`) ni al
> marcador de pausa.
>
> **Nota de fecha, declarada.** Este documento se redactó el **26 jul 2026** al cierre de la sesión
> del comité, y se fecha **27 jul** porque su función es servir de punto de reentrada para la
> sesión siguiente, en otra máquina, tras `git pull`. No hay hoja del 26 jul: el trabajo de esa
> fecha (comité 045 y los cuatro commits de §1) queda registrado aquí.

## 0. Relación con la pausa del programa

El programa sigue en `PROGRAMA_EN_PAUSA_LIMPIA` (`docs/marcador_reentrada_2026-07-19.md`, firmado
PI). La línea de localizadores C1–C6 sigue cerrada (C6 = `BLOCKED_NO_STABLE_CODIM2`, comités
043/044) y la **recomendación viva sigue siendo consolidar (paper), no abrir C7**. Nada de esta
sesión la toca: no se ejecutó ningún script del banco sellado, no se tocó
`nachocausal/thresholds.py`, no se consumió ninguna semilla reservada, no se abrió ningún candidato.

Sello sin drift, verificado esta sesión:
`6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (= `docs/preregistration_002.md:8`).

## 1. Qué se hizo (sesión del 26 jul)

Se convocó `/comite` para adjudicar **exclusivamente** el estado lógico del candidato 7.1 (conteo de
pares comparables `S_n`) en el canal `fixed_n`, a raíz del **Finding 1** del informe de auditoría 026,
que dictaminó que la nota **infra-afirmaba**: sostenía que la des-Poissonización bloqueaba la Forma L
cuando la ruta Chebyshev en `fixed_n` no la necesita.

Cuatro commits, cada uno solo, en el orden que exige la disciplina del repo:

| Commit | Objeto |
|---|---|
| `4124be2` | `docs/auditor/auditor_report_026_...md` — registro independiente de la auditoría (condición C1) |
| `2955bc5` | `docs/comite/comite_decision_045_...md` — acta del comité (7 roles, dos oleadas) |
| `d7cc685` | `wp4_comparable_pair_separation_checks.py` — generador §4b, checks `[10]`–`[13]` (C2, «script primero») |
| `bccd67d` | Anexo C §4b + ficha §2.2 puntos 3-4 — los literales (C2, «literales después») |

**Ningún cambio de etiqueta se ha aplicado todavía.** Forma L sigue `[OPEN]` en el árbol
(`wp4_comparable_pair_separation.md:381`).

### 1.1 Lo que el comité resolvió (consenso 7/7)

- **La cadena es correcta en `fixed_n`.** `Delta_p != 0` ⇒ gap de medias `Theta(n^2)`;
  `Var(S_n) = O(n^3)` por las cotas triviales `zeta_1, zeta_2 <= 1/4`; data processing (`S_n` es
  invariante de isomorfismo) + Chebyshev en el punto medio ⇒
  `TV(Q^n_tau, Q^n_tau') >= 1 - 4(2n-3)/(n(n-1) Delta_p^2) -> 1`.
  Verificada por **tres rutas independientes**: el autor del Anexo C, el auditor (informe 026 §6) y
  el matemático del comité **a mano, término a término**.
- **No hace falta nada importado.** Ni CLT de Reitzner–Schulte, ni des-Poissonización, ni ajuste
  empírico de exponente. Por FWP Lema 0 los `n` puntos son i.i.d., luego `S_n` es un U-estadístico
  **binomial**, no un funcional de Poisson: los dos momentos son identidades exactas. Confirmación
  textual decisiva: **Reitzner–Schulte dicen ellos mismos (p.23) que no hay puente de
  des-Poissonización** («it seems to be difficult to prove one result by the other, especially with
  keeping rates of convergence»).
- **El exponente `1/2` está demostrado**, y por matemática de 1948 (descomposición de Hoeffding) más
  Chebyshev. No se ajustó ningún exponente: los Monte-Carlo a `n = 5, 10, 20` sólo verifican la
  fórmula exacta de varianza.
- **La tasa `n^{-1/2}` es óptima en exponente, por ambos lados.** La cota de WP4 §5 es **no
  asintótica** (descansa en Cauchy–Schwarz integrado, no en el desarrollo QMD) y acota `TV(Q^n)`, que
  por definición es el supremo sobre **toda** función del poset: ningún procedimiento order-only
  separa a `delta = o(n^{-1/2})`.

### 1.2 Hallazgo nuevo — el comité también BAJA una etiqueta

Por el **teorema del valor intermedio**: `Delta_p(0.02) = +1.142952e-04` y
`Delta_p(4) = -3.875520e-04`, con `p` continua en `dv` ⇒ **existe `dv* ∈ (0.02, 4)` con
`Delta_p(dv*) = 0` exactamente**. En ese lapso `S_n` es **exactamente ciego a nivel de medias** y
toda la cadena de dos momentos es vacua para **cualquier** `n`.

No rompe el teorema (Teo C4 excluye ceros por debajo de `dv_0`): lo **acota**, y prohíbe toda
extrapolación en `dv`. Pero **refuta `ficha:483-485` tal como está escrita** («el estadístico nunca
es ciego ahí»). Esta sesión, por tanto, no es una sesión de promoción: sube una etiqueta y baja otra.

## 2. Estado actual — qué cambia y qué no

**Cambia.** La des-Poissonización **nunca estuvo** en la ruta `fixed_n`. La afirmación de ficha §2
(«no existe en el repo ninguna técnica para acotar `TV(Q)` por debajo») es **falsa** desde este
comité: la técnica es la que la propia ficha §5 anticipaba — estadístico order-only + data processing
+ Chebyshev. Es la primera instancia de cota inferior de TV a nivel poset del repositorio.

**No cambia.** El hueco central de la ficha sigue abierto en todo lo demás: canal Poisson sin
condicionar (donde la marginal `N` separa sola), otras familias (`[OPEN por par]`), candidatos
7.2–7.4, y Formas U y D. Y sobre todo:

**Delimitación, vinculante para cualquier cita futura.** El resultado es **discriminación binaria
entre dos completions fijadas de antemano** mediante una función del poset. **NO** es localización
del horizonte (no se produce ningún locus `r = 2M`, ningún elemento queda etiquetado «horizonte»),
**NO** es reconstrucción (el Teorema A prueba que toda la órbita de dilatación es una sola ley de
poset a todo `n`), **NO** es estimación de `tau` ni conjunto de confianza, **NO** es 3+1D, **NO** es
horizonte asintótico. Disidencia del físico, adoptada como límite: la señal es una **firma de
curvatura/forma, no del locus del horizonte** — `kappa > 0` vale para todo `0 < r_q < r_p` **sin
ninguna condición sobre `tau`**, luego nada se dispara *porque* el diamante cruce el horizonte.

**Y no es ejecutable.** `n ~ 10^8`–`10^10` implica `ell ~ 10^{-4}`–`10^{-6}` del radio del horizonte
y supera en `~10^5` el mayor nivel de la escalera congelada `{1500, 3000, 6000, 12000}`. Eso es la
cardinalidad total fija del poset, **no** el tamaño del parche ni la intensidad de Poisson.

## 3. Condiciones pendientes del acta 045 (§9.2)

| | Estado |
|---|---|
| **C1** — auditor 026 registrado por su propio pie | ✅ `4124be2` |
| **C2a** — script antes que literales | ✅ `d7cc685` |
| **C2b** — literales respaldados por script commiteado | ✅ `bccd67d` (26/26 verbatim) |
| **C2c** — el paso 7 de la cadena sigue **sin generador** | ❌ **pendiente** |
| **C3** — congelar `dv` por escrito | ❌ **pendiente — decisión del PI** |
| **C4** — las tres etiquetas, como bloque | ❌ **pendiente — autorización del PI** |

**C2c, el bloqueo real.** El check `[13]` imprime el requisito `zeta_1*Ibar >= kappa^2 dv^2/54`,
**no** la cota TV. Los `n ~ 10^8`–`10^10` existen únicamente en la prosa del informe 026 (`:164-166`),
sin generador. Consecuencia operativa: la reetiquetación **puede hacerse sin publicar ningún literal
numérico nuevo** — la Etiqueta 1 no contiene ninguno —, pero **cualquier cifra `n*` exigiría antes**
el check `[14]` de §9.5 del acta. Precedente vinculante: `auditor_report_024 = AUDIT_FAIL` por
exactamente este defecto.

**C3, pendiente de decisión.** El registro contiene dos `dv`: `0.02` (dentro del régimen probado) y
`4` (demostrablemente fuera — allí `p` **decrece** en `tau`, signo opuesto al Teo C4). Elegir después
el que dé mejor `n` sería `NO_POST_HOC_TUNING` puro. *Recomendación del presidente, no ejecutada:*
fijar `dv = 0.02` como el valor afirmado, y reportar `dv = 4` explícitamente marcado como fuera del
régimen — no destacar uno en silencio.

## 4. Próximos pasos (ninguno ejecutado ni autorizado por este documento)

Orden de prioridad, uno cada vez. Los tres primeros son ediciones o cálculos compatibles con la
pausa; el cuarto no lo es.

1. **Aplicar las tres etiquetas del acta 045 §8.3, como bloque** (C4), más las correcciones internas
   que deben caer con ellas: acotar §6.3 de la ficha (su viñeta de anti-concentración, leída
   literalmente, **bloquea la propia cadena adjudicada**), *narrow* — no borrar — la viñeta del hueco
   central de §2, arreglar el choque de convención del factor 2 entre §2.1(B) y §7.1 (mueve toda
   constante de Chebyshev por 4 si se mezclan), y separar canales en §7.1 punto 3. Es una edición
   documental sin literales nuevos. **Requiere C3 y C4.**
2. **`Ibar` para las esquinas del diamante de registro.** Prioridad analítica 1: un único escalar que
   cierra tres cosas a la vez — ejecuta el *defeater* `zeta_1*Ibar >= kappa^2 dv^2/54`, cuantifica el
   prefactor, y da la primera medida real de la pérdida por compresión `Iso_n -> S_n`. Cuadratura
   determinista de un objeto ya definido en WP4. Es un cálculo, no una ejecución.
3. **Escribir la cota de resto `O(dv^2)`, uniforme en `tau`.** El único ingrediente que falta: cierra
   el paso (i) argumentado-no-escrito **y** hace efectivos `dv_0` **y** `n_0(dv, delta)`
   **simultáneamente**. Convertiría la Etiqueta 1 en `[PROVED]` sin cualificar y con constantes.
4. **Reetiquetar la hoja del 25 jul** (§3 ítem 2: des-Poissonización de bloqueo a herramienta
   opcional para constantes; §4 primera viñeta: acotarla a «sin acotar canal, familia, par y régimen
   `dv`»), y corregir la mis-ancla «ficha §2.4» del informe 026 — la ficha no tiene §2.4; la regla
   viva es `docs/hoja_de_ruta_24_jul_2026.md:66-70`.

## 5. No hacer

- **No presentar el candidato 7.1 como Forma L sin acotar canal, familia, par y régimen `dv`.** La
  prohibición del 25 jul §4 sigue en pie en su forma *procedimental*; el comité sólo revisó su
  premisa sustantiva (dos de sus cuatro «bloqueos» eran erróneos), no su cautela.
- **No usar la expresión «viabilidad matemática demostrada».** Convergencia asintótica en un régimen
  no efectivo, con un *defeater* sin ejecutar y una ceguera exacta garantizada fuera del régimen, no
  es viabilidad. El comité confirmó que la prohibición está justificada.
- **No usar `PROVED_BUT_VACUOUS_IN_PRACTICE`** (sugerida por el informe 026): sobre-afirma en
  dirección **pesimista**. Lo enorme es la cota de Chebyshev, no la TV verdadera, que es desconocida.
- **No publicar ninguna cifra `n*` ni cota TV** hasta que un script determinista commiteado la emita
  verbatim (C2c).
- **No extrapolar en `dv`**: existe `dv*` donde `S_n` es exactamente ciego (§1.2).
- **No abrir un observable nuevo, no abrir `CANDIDATE_7`, no implementar `S_n` como estimador**, no
  ejecutar el banco sellado, no consumir semillas, no tocar ningún umbral congelado.
- **No extrapolar a otras familias**: `kappa > 0` es un enunciado sobre la familia diamante de WP4 §4.

## 6. Checklist de reentrada (otra máquina)

1. `git pull` — deben aparecer los cinco commits: `4124be2`, `2955bc5`, `d7cc685`, `bccd67d` y el de
   esta hoja.
2. `make verify-seal` debe dar
   `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
3. `git status --short` debe salir **limpio**.
4. Leer primero `docs/comite/comite_decision_045_candidate-7-1-fixed-n-logical-status.md` §8 (síntesis
   y etiquetas) y §9 (condiciones y plan). Es el documento que gobierna el siguiente paso.
5. `biblioteca/` es git-ignored: **no viaja con el clon**. Si se necesita bibliografía en la otra
   máquina, hay que copiarla aparte.
