# Hoja de ruta — 25 jun 2026 · PR-003 Fase #3: consolidar la cota de Le Cam como resultado

> **Plan REVISABLE, no congelado.** No es una pre-registración y no fija ningún umbral vinculante.
> Toda regla/umbral se congela en su documento sellado **antes** de cualquier paso *committing*
> (reglas fundacionales en `CLAUDE.md`, `docs/preregistration.md`). Sucesora de
> `docs/hoja_de_ruta_24_jun_2026.md`. Avalada por
> `docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md`
> (`COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP`, ACEPTADA, firmada 24-jun).

## Punto de partida (verificado, 25-jun-2026) — leer esto primero al retomar

- **prereg-002 `PASS`**, sello `nachocausal/thresholds.py` sha256 =
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (`make verify-seal`). Camino
  sellado intacto; nada de esta fase lo toca.
- **PR-003 está en Fase #3.** El cascade #1 (expansión Θ, S1/S2 NEGATIVE) y #2 (re-sembrado
  iterativo S3, NO converge: cobertura honesta 51→48→44 % al subir densidad) cerraron en negativo.
  El objeto *extendido* se aparta; **PR-003 consolida sobre la cota O(ℓ) medida** (`BARE_RELOCALISATION`).
- **El resultado Fase #3 es la cota inferior de Le Cam/Fano** sobre la localización order-only de
  `r_S`, *para ESTE estimador sellado, a V y ρ finitos* — NO un no-go universal/asintótico, NO 3+1D.

## Lo hecho en esta sesión (24-25 jun; dev / reversible / nada congelado)

Todo en GPU local (NVIDIA RTX 5060) vía `dev/backend.py` (CuPy) donde aplica; sello `6e2c3888…`
verificado antes y después de cada corrida; solo `EXPLORE_POOL`; `RESERVED_002` jamás tocado.

1. **R0 — gate de desacoplamiento TDA** (`dev/PR003_TDA_DECOUPLING_GATE_NOTES.md`): la
   conectividad/persistencia (90→95→93 %) está **desacoplada** de la cobertura honesta (51→48→44 %)
   → un sondeo TDA ciego está **descalificado** como evidencia de recuperabilidad. TDA queda diferido
   tras sus 3 prerequisitos (Guard-v fallable; literatura 0902.0434/MRS2007/CS2018 en `biblioteca/`;
   ancla de grosor declarada antes de datos puntuados).
2. **R1 + O1/O2/O3 — la cota de Le Cam** (`dev/PR003_INFO_BOUND_NOTES.md`, 7 secciones):
   - **§1-§4** dos-puntos Le Cam → `Error(r̂−r_S) ≳ K·ℓ = K·ρ^(-1/2)` (★), alcance acotado a este
     estimador; ancla in-repo (§3): los thresholds sellados ya adoptan `K_LOC=2`.
   - **§6 / O3 (numérico, GPU)** `dev/measure_info_bound_o3.py`, 24 seeds × 4 intensidades frozen:
     el suelo escala como ℓ — scatter `σ(r̂) ≈ 0.40·ℓ` **density-invariante** (×8 densidad), curvas
     `TVg(r̂)` colapsan vs `s/ℓ`, separación resoluble `2s/ℓ ≈ 0.6`. Constante O(1) **< K_LOC=2 ⇒
     K_LOC=2 es conservador** (suelo seguro). GPU=CPU bit-idéntico para el observable (maxdiff=0).
   - **§7 / O1-O2 (analítico, sketch)** O2: `dO/dr = ρ·dA_fut/dr` (log-realzado en `r_S` por la
     tortuga `func`); ρ se cancela → `δr = ℓ·√(A_fut)/(dA_fut/dr)` ∝ ℓ, constante ≈0.4 fijada por O3.
     O1: KL de la salida `≈ 3.1·(2s/ℓ)²` = 1 en `2s ≈ 0.57·ℓ`; Bretagnolle–Huber → suelo O(ℓ).
3. **R2 — falsificación K-beam del peel-off** (`dev/measure_kbeam_peeloff.py`,
   `dev/PR003_KBEAM_PEELOFF_NOTES.md`; GPU build + matmul `C·C`, K-beam en numba): el peel-off **NO
   se cura con K**. Al crecer K 1→64 (n@k=8: 2→103) la top-1 order-only se queda en ~5-7ℓ a
   profundidad 8 y la min-beam se estanca en ~4-6ℓ; solo la cabeza (k≤3) adhiere ~2ℓ. → evidencia de
   muro **físico** (no miopía greedy) → **endurece** la cota. **CAVEAT honesto:** under-reach a
   t_edge=6 (reach≥8 ≤23 %); etiqueta = "PHYSICAL dentro del alcance de la caja", no incondicional.

**Estado neto:** el resultado Fase #3 (cota Le Cam) ya tiene sus **tres patas** — ancla sellada (§3),
ilustración numérica (§6/O3), derivación analítica (§7/O1-O2) — más R2 endureciéndolo. Falta solo el
paso *committing* (C1) y la literatura (O4).

## Disciplina que gobierna TODA esta fase (pre-comprometida, no negociable)

Cada paso es **dev / reversible**: semillas solo de `EXPLORE_POOL` (`dev/explore_seeds.py`), nunca la
banda virgen `RESERVED_002 [2_000_000, 2_999_999]`, nunca `nachocausal/thresholds.py` ni el camino
sellado. `make verify-seal` = `6e2c3888…` antes y después. `r` solo PUNTÚA, nunca siembra/construye/
selecciona/corta (leakage gate `docs/pr003_leakage_gate.md`, contrato #5). Nada se congela sin nueva
prereg + `/comite` + `/auditor`. Rama: trabajar SOLO en `main` (peligro de checkout compartido
`formula`); commits atómicos; `git status` sin `M nachocausal/` ni `M docs/preregistration_*`.

## Próximos pasos (en orden; el primero es committing — necesita tu OK)

### C1 — Congelar el resultado Fase #3 (COMMITTING — requiere `/comite` + `/auditor` + tu autorización)
Redactar `docs/preregistration_003.md` que consolide la cota `Error(r̂−r_S) ≳ K·ℓ` como el resultado
Fase #3, con su forma precisa y alcance (este estimador, V/ρ finitos, singular-Schwarzschild, no
universal/asintótico, no 3+1D). Incorporar R2 (peel-off físico, con su caveat under-reach) como
endurecimiento. **NO** congelar ninguna constante nueva tuneada por datos puntuados (la `K` es
`K_LOC=2`, ya sellada; O3 muestra que es conservadora — eso se reporta, no se re-sella). Pasos:
  1. Borrador de la prereg-003 (dev, sin sellar) listando la afirmación exacta y los caveats.
  2. `/comite` sobre el borrador (paso one-way) → freeze-check + falsación.
  3. `/auditor` para verificar que cada número publicado es salida literal de script committeado.
  4. Solo entonces sellar.

### O4 — Literatura (reversible, no committing)
Meter en `biblioteca/` la base del marco Le Cam (Tsybakov 2009, *Introduction to Nonparametric
Estimation*, Thm 2.2 — texto estándar) y cualquier precedente de teoría-de-información en causal sets,
antes de citarlos en la prereg-003. (Las citas TDA 0902.0434 / Major-Rideout-Surya 2007 /
Cunningham-Surya 2018 siguen SIN verificar y solo hacen falta si se reabre TDA.)

### Opcional A — Prereg de caja alta (COMMITTING) para cerrar el caveat de R2
Único camino que queda para *reabrir* la extensión: un run con `t*/r_S ∈ [0,50]` (~8× más alto, como
EGS). Es una **NUEVA prereg** (distinta `BOX_AREA`/tabla ℓ), fuera del alcance de un paso dev. Solo si
se quiere atacar el under-reach; en su defecto, R2 ya disfavorece la lectura "algorítmica/curable".

### Opcional B — TDA, solo si se cumplen sus 3 prerequisitos (ver R0). Hoy NINGUNO se cumple → diferido.

## Cómo retomar en el otro PC (checklist de arranque)

1. `git clone https://github.com/nacho09021973/nachocausal.git && cd nachocausal`
2. Venv sellado (CPU, numpy 1.26.4): `python -m venv .venv && .venv/bin/pip install -r requirements.txt`.
   Verificar el sello: `make verify-seal` → debe leer `6e2c3888…`.
3. (Opcional, para los sondeos GPU) en una máquina CUDA: `python -m venv .venv-gpu &&
   .venv-gpu/bin/pip install -r requirements-gpu.txt` (CuPy + numba). En WSL2 usar `dev/run-gpu.sh`
   (antepone `/usr/lib/wsl/lib` por el gotcha de libcuda). Sin GPU, `dev/backend.py` cae a numpy solo.
4. Reproducir los sondeos de esta sesión (regeneran sus logs git-ignored):
   - `NACHO_MODULE=dev.measure_info_bound_o3 dev/run-gpu.sh --seeds 24`   (O3, ~45 s GPU)
   - `NACHO_MODULE=dev.measure_kbeam_peeloff dev/run-gpu.sh --seeds 6`     (R2, ~160 s GPU)
   - (sin GPU: `python3 dev/measure_info_bound_o3.py --device cpu`, etc.)
5. Leer, en orden: `dev/PR003_INFO_BOUND_NOTES.md` (la cota, 7 secciones) →
   `dev/PR003_KBEAM_PEELOFF_NOTES.md` (R2) → `dev/PR003_TDA_DECOUPLING_GATE_NOTES.md` (R0) →
   `docs/comite/comite_decision_003_*.md` (la decisión que gobierna). Continuar por **C1** (arriba).

> Nota: la **memoria** de Claude Code es local a cada máquina (`~/.claude/.../memory/`) y NO viaja
> con el repo. Esta hoja de ruta + las notas en `dev/` + las decisiones en `docs/comite/` son la
> continuidad portable y autoritativa entre PCs.
