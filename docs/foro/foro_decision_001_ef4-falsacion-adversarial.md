# Foro Decision 001 — ef4-falsacion-adversarial

> Produced by `/foro`. The forum PROPOSES; the user AUTHORISES. No forum agent executed a one-way,
> outward-facing, or irreversible action. Claims are promoted only by an oracle outside the
> language layer — a command, a `path:line`, a verified citation. Agreement between agents is not
> evidence, and no verdict here was reached by majority.

## 1. Decision question

¿Sobrevive el certificado EF-4 (§§EF-4.1–EF-4.5 de `docs/hoja_de_ruta_agosto_2026.md:1191-1528`) a
una falsación adversarial? En concreto: ¿es válida la inclusión `F_n ∩ G_n ⊆ S` (EF4.15, :1421) y
con ella el cierre `log(1/Pr_n(S)) = o(n)` (EF4.19) y `Q_{2,n} → 0` (EF4.20)?

Encargo explícito del PI: **intentar falsar primero (EF4.15)**. Prohibido en esta sesión ampliar
`n`, buscar otra construcción y editar ficheros.

## 2. Verified state

Hechos comprobados **esta sesión** por el presidente, cada uno con su comando. Lo no comprobado va
marcado `[UNVERIFIED]`.

- `git log -1 --format='%H %ad %s'` → `97b48dcdab2acd2a2f641d5cb30b2ab4e53c9c78 2026-08-15 20:06:53 +0200 Document complete EF-2 revalidation`
- `git status --short --branch` → `## research/f2-f3-chain-distance...origin/research/f2-f3-chain-distance` (árbol limpio)
- `.venv/bin/python -m pytest tests/test_p1a_entropia_fibras_ef3.py tests/test_p1a_entropia_fibras_ef4.py -q` → `16 passed in 1.28s`
- `make verify-seal` → `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
- No existe `FORO.md` en la raíz → se usan los defaults genéricos del protocolo.

Anclajes del BLOCK verificados por el presidente **después** de recibir la ola 2, por ser los que
deciden el veredicto:

- `docs/program_reopening_note_2026-07-31.md:83` → `1. Perímetro fijo: R1 y R2. Nada entra sin una nueva nota firmada.`
- `docs/program_reopening_note_2026-07-31.md:78` → `prórroga. R2 tiene además su propio tope: **dos semanas**; si no ha salido, se marca abierto y se`
- `grep -niE 'firmada_por|autorised_scope' docs/hoja_de_ruta_agosto_2026.md` → **sin resultados**. Las notas firmadas sí los llevan: `docs/program_reopening_note_2026-08-05_R3.md:96,98` y `docs/program_reopening_note_2026-08-09_P5_2.md:97,99` (`FIRMADA_POR: Ignacio (PI)`, `AUTORISED_SCOPE: ... (lista cerrada de §2)`).
- `docs/program_reopening_note_2026-08-09_P5_2.md:54` → `- El manuscript \`docs/manuscript_limits_draft.md\` no se toca.`; `:103` → `MANUSCRIPT_LIMITS: NO TOCAR`; `:58` → `horizonte, \`order-number-scale-limits\` ni dimensión superior.`
- `git show --stat --format='' 326fee3 -- docs/manuscript_limits_draft.md` → `1 file changed, 17 insertions(+), 3 deletions(-)` (commit del 2026-08-15).
- `grep -c 'EF-4\|EF4\|FIBER_CONCENTRATION' docs/manuscript_limits_draft.md` → `0`.
- `research_program/work_packages/wp7_f2_f3_product_order_contract.md:4` → `ESTADO: CONTRATO FORMAL v1.7 / P1--P4 PROBADAS / P5.2 PASS_WITH_SCOPE / EXTENSIÓN PROBADA PARA TODO d>=2 MÓDULO EL MISMO ALCANCE`, modificado en `8139092`, que además añade `research_program/work_packages/wp7_f2_f3_higher_dimensional_extension.md` (463 líneas) y siete ficheros nuevos en `research_program/posters/` (incluidos PDF y PNG).
- `docs/comite/comite_decision_050_...md:485` → `MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO` retained with a pointer to this brief.`
- `docs/comite/comite_decision_050_...md:325` → `Do not let my AM-GM repair enter the manuscript as \`PROVED\` on my say-so.`
- `grep -c 'MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED' docs/hoja_de_ruta_agosto_2026.md` → `0`, mientras `:1506` declara `EF4_CORRECTED_PRESCRIBED_FAMILY = PROVED`.

`[UNVERIFIED]` por el presidente: la ausencia de commits de R2 posteriores a `91a84ac` (aportada
por el guardián vía `git log dev/R2_lambda6_derivation_NOTES.md`); el contenido sustantivo de las
17 líneas añadidas al manuscrito.

## 3. Dossier

Ficheros y comandos entregados al panel:

- `docs/hoja_de_ruta_agosto_2026.md` (1753 líneas; EF-3 en 1022-1190, EF-4 en 1191-1528, EF-6/EF-7 en 1548-1625, §7-§11 en 1626-1753)
- `emergencia/p1a_entropia_fibras_ef3.py`, `emergencia/p1a_entropia_fibras_ef4.py`
- `tests/test_p1a_entropia_fibras_ef3.py`, `tests/test_p1a_entropia_fibras_ef4.py`
- `emergencia/P1a_count_volume_experimento_condicionado_d2.md`, `..._ley_condicionada_d2.md`, `..._lema_kl_d2.md`
- `emergencia/P1a_contrato_comparacion_selectores_balanceados_d2.md`, `emergencia/p1a_comparar_selectores_d2.py`, `emergencia/p1a_enumeracion_simulacion.py`
- `docs/comite/comite_decision_050_p1a-seccion-13-certificado-familia-prescrita.md`
- `docs/program_closure_note_2026-07-30.md`, `docs/program_reopening_note_2026-07-31.md`, `..._2026-08-05_R3.md`, `..._2026-08-09_P5_2.md`
- `CLAUDE.md`, `Makefile`
- Comandos de estado: `git log -1`, `git status`, `pytest`, `make verify-seal`

Restricciones vinculantes comunicadas al panel: alcance negativo §8 (:1652-1670); cierre del
programa 2026-07-30 no revocado; sello y banda virgen `[2.000.000-2.999.999]` intactos; cero
simulaciones y cero semillas en esta línea; prohibición del PI de ampliar `n`, buscar otra
construcción o editar.

## 4. Expert briefs (wave 1 — blind, parallel)

Pegados verbatim. El presidente no los fusionó, suavizó ni resumió.

#### Expert brief — Rival-classification prover

- **Assessment:** Yes — the trichotomy of EF-4.3 is exhaustive, and (EF4.9) holds at every floor and boundary I could construct, but the prose proof at `docs/hoja_de_ruta_agosto_2026.md:1315-1339` is *under-derived*: (EF4.9) is asserted with no computation and is true only by the razor-thin amount `(rho_n-1)/(4N_n)` when read literally, and the finite check at `tests/test_p1a_entropia_fibras_ef4.py:63` structurally cannot exercise the one configuration family the argument leans on hardest. I could not falsify exhaustiveness; I reconstructed a complete case split by hand and every branch lands in (1), (2) or (3).

- **Load-bearing facts:**
  - Rivals are *strict 4-chains*: `Q_3(C) = {(a,b,c,d) : a prec b prec c prec d, m_-,m_+>=3}` (`emergencia/P1a_count_volume_experimento_condicionado_d2.md:40-42`). Hence `row(a)<row(b)<row(c)<row(d)` and likewise for columns. This makes line 1334 (`el pasado nunca puede contener (n,n)`, `el futuro nunca puede contener (1,1)`) **forced, not assumed**: `(n,n)` in `[a,b]` forces `b=(n,n)`, contradicting `b prec c prec d`; `(1,1)` in `[c,d]` forces `c=(1,1)`, contradicting `a prec b prec c`. Verified, not an assumption.
  - Blocks are *closed* rectangles including endpoints (`emergencia/p1a_enumeracion_simulacion.py:173-198`, "closed-interval cardinalities … inclusive axis-aligned rectangle"), consistent with `p_0=rho_n+1` per planted side (`docs/hoja_de_ruta_agosto_2026.md:1246-1248`) and with the inclusive `inside()` in the test.
  - The band `{s-rho+1,…,s+rho}` is *entirely* prescribed — code: rows `{half-width+1,…,half-1} ∪ {half,half+1} ∪ {half+2,…,half+width}` (`emergencia/p1a_entropia_fibras_ef4.py:73-76`), matching :1216-1224. Therefore under `F_n`, if `row(b)` lies in the band, `b` *is* the prescribed point of that row and its column is determined. The row-only inspection at :1315 is legitimate **only because of this**; it is the hinge of the whole argument.
  - Rows `s-rho` and `s+rho+1` are **free** (band starts at `s-rho+1`). A rival with `b` on row `s-rho` and an arbitrary (possibly huge) free column still cannot contain a `B_-` point, because `B_-` rows are all `>= s-rho+1`. The row argument is airtight against the "column escapes the band" attack.
  - **(EF4.9) literal check.** With `R_n=2rho+2`, `N=n-R_n`: `LHS-RHS = (N/2)(n/4+rho)/N² - (1/8+rho/N) = (1-rho)/(4N)`. So it holds for every `rho>=1`, with equality at `rho=1` and slack exactly `(rho-1)/(4N)`. Command `/home/adnac/nachocausal/.venv/bin/python -c` (closed-form evaluation, no enumeration, no seeds) → at `n=1e9`: `tau=0.127761925`, `crudeEF4.9=0.127071444`, `slack=6.905e-04`, which equals `(rho-1)/(4N)=(2746751)/(4·994506494)` exactly. Generalising: the crude bound needs `R_n <= 4rho_n`; `R_n=2rho_n+2` clears it, but only by a factor <2.
  - **Exact-count versions are comfortable.** Same command, exact free-row/free-column counts against `tau_n`: at `n=1e6` (`rho=23996`, `N=952006`, `tau=0.150206`): `b∈B_-` → `0.131301`; past-crosses-upper-stair → `0.118699`; `c∈B_+` → `0.118699`; future-crosses-lower-stair → `0.131301`. All `<= tau`. Slack for the worst branch is `(6rho+2)/(8N) ≈ (3/4)(rho/N)`.
  - **The `rho_n/N_n` term in `tau_n` (EF4.8) is load-bearing, not decoration.** With `tau=1/8` alone the `b∈B_-` branch fails by `(rho-1)/(4N)` (same algebra). Any later step that tries to sharpen `tau` down to `1/8` breaks case (2).
  - **`rho_n<n/4` first holds at `n=396`** (same command: `smallest even n with rho_n < floor(n/4): 396, rho=98`). Below that the construction is undefined and the code refuses (`emergencia/p1a_entropia_fibras_ef4.py:67-68`, `width >= n//4 → ValueError`). At `n=396` the staircases are `B_-`: rows 101–197 / cols 100–196; `B_+`: rows 200–296 / cols 298–394 — no collision with `1,s,s+1,n`, and generally `q_1+rho-1<s` and `q_3+rho-1<n` follow from `rho<n/4`. **The two staircases do not collide anywhere in scope.**
  - What the `n=12` test certifies: it enumerates `C(12,4)^2 = 245025` pairs (4 rows × 4 columns) and zips them monotonically (`tests/…ef4.py:92-95`), i.e. **all abstract 4-chains** — a strict superset of realisable rivals, which makes the pass conservative and meaningful. It uses the same `tau` formula (`:72`) and the same three predicates as the doc, and asserts the disjunction at `:154`.
  - What it does **not** certify: (i) it runs at `rho=2`, not `rho_for_n(12)=8`, so each staircase has exactly `rho-1 = 1` point — **partial staircase containment is unreachable**; (ii) `tau = 1/8+2/6 = 0.4583` there, versus `tau → 1/8` asymptotically, so case (2) is far more permissive than in the real regime (indeed `tau > 1/4` makes (EF4.7) alone discharge most rivals); (iii) it never checks that a prescribed row forces its prescribed column (it enumerates abstract rows/columns), so the `F_n`-hinge above is untested; (iv) it validates only the *classification*, never the *margins* of EF-4.4.

- **What would have to be true (attack these):**
  1. `F_n` holds, so every band row carries its prescribed column. If any step later conditions on something weaker than `F_n`, the row-only inspection at :1315 collapses.
  2. Rivals are strict 4-chains of *permutation points* (not arbitrary rectangles). Both "≤3 specials" claims die if a "rival" could repeat a point or be a 3-chain.
  3. `u_±, v_±` are fractions of **free** rows/columns w.r.t. `N`, and bounding free columns by total columns is a legitimate over-count (it is; this is how the crude `n/4+rho_n` in :1318-1319 is licensed even though it counts prescribed columns as free).
  4. `R_n = 2rho_n+2` exactly. (EF4.9) needs `R_n <= 4rho_n`; the certificate is not robust to a redefinition of `R_n`.
  5. `rho_n >= 1` and `rho_n < n/4`, i.e. `n >= 396`.

- **Configurations the case analysis may not reach (I checked each by hand; all land in a case):**
  - `b` free on row `s-rho` with column `n-1`, `c=(?,n)` — past covers nearly all columns, `f_-≈1/2`, but `f_+≈0`. Not covered by (EF4.7) (which only gives `min<=1/4 > tau`). Resolved: past loses `B_-` row-wise, future's columns are `{n}` so no cross → case (3) with `past_prescribed<=1`, `future_prescribed<=1`.
  - `b=(s+1,s+1)` with `a` below the band and `c` above the band: past contains `(1,1)`, all of `B_-`, `(s,s)`, `(s+1,s+1)` = exactly `rho+2 = p_0+1`. **This saturates the case-(3) bound.** It is the tight configuration for the second branch of (EF4.10); any off-by-one in the count breaks EF-4.4, not EF-4.3.
  - `c=(s,s)` with `b` below the band (rival keeps *no* interior endpoint in the planted slot but reuses `(s,s)` as `c`): future = `[(s,s),d]` can hold `(s,s),(s+1,s+1),B_+,(n,n)` = `rho+2`; losing past has `<=1`. Case (3). ✓
  - `a ∈ B_-`, `b=(s,s)`, `c=(s+1,s+1)`, `d` arbitrary: case (1) — note case (1) constrains only `b,c`, so `a,d` roam freely. ✓
  - Both sides simultaneously crossing (`past ∋ B_+` and `future ∋ B_-`): **impossible**, since it forces `row(b)>=s+2` and `row(c)<=s-1<row(b)`. The doc never says this; it is a real (favourable) gap in the prose.
  - Empty/singleton blocks: excluded twice over — `a prec b` strictly, and `m_±>=3 = K0` (`emergencia/p1a_enumeracion_simulacion.py:32`).
  - Rivals straddling `q_1`/`q_3`: these are column indices only; no row-side claim depends on them, and the `B_-` column bound `col(b) <= q_1+rho-1` is what the argument actually uses.
  - **Partial staircase containment** (rectangle holds *some* `B_+` points but not all): handled correctly by the "at least one point" phrasing of *crosses/loses*, but **never exercised by any executed check** (see below).

- **Risks / failure modes from this lens:**
  1. `tests/…ef4.py:63` cannot be strengthened at `n=12`: `build_even_prescription` requires `rho < n//4 = 3` (`p1a_entropia_fibras_ef4.py:67-68`), so `rho<=2` and staircases are single points. **The only executed exhaustiveness oracle is structurally blind to multi-point staircases and to the asymptotic `tau→1/8` regime.** The trichotomy currently rests on prose plus my hand reconstruction, not on machine checking.
  2. (EF4.9) as printed at :1323-1327 mixes `n` in the numerator with `N` in the denominator and is presented as self-evident. It is not: `n/(8N) > 1/8`. A reader (or a future edit that changes `R_n`, or that removes the `rho_n/N` term from `tau_n`) can silently break it. Slack is `(rho_n-1)/(4N_n)`, i.e. *zero at `rho=1`*.
  3. `docs/…:1339` "el análisis para `b=(s+1,s+1)` es idéntico" is not identical: with `b=(s+1,s+1)` the case-(1) branch is unavailable (`c` cannot be `(s+1,s+1)`), and this is precisely the branch that saturates `p_0+1`. Sloppy prose over the tightest configuration.
  4. The classification is exact but *asymptotically tight in relative terms*: the worst case-(2) rival sits at `f_- = 1/8 + Θ(1/N)` against `tau_n = 1/8 + rho_n/N`. The entire case-(2) margin is `Θ(rho_n/N_n)` on the geometric side, and it is EF-4.4's `N/8-2rho_n-1` that turns it into a usable score gap. These two are coupled; a change to `tau_n` cannot be made locally.

- **What I could not determine:**
  - Whether the trichotomy survives machine enumeration with **multi-point staircases** at the correct `tau`. The decisive experiment is one deterministic, seedless, write-free run of the `:63` enumeration at e.g. `(n=20, rho=4)` and `(n=24, rho=5)` (staircases of 3–4 points, `tau=0.125+rho/N`). **I did not run it**, because it requires enlarging `n` beyond the committed test and the PI forbade enlarging `n` this session. My hand proof covers those configurations, but a hand proof is not an oracle.
  - Whether case (1)'s "cualquier cambio reduce estrictamente el mínimo al menos en una unidad" (`:1387-1391`) is airtight — that is EF-4.4's margin arithmetic and belongs to another role, but note EF-4.3 dumps into case (1) every rival with `b=(s,s), c=(s+1,s+1)` and arbitrary `a,d`, including `a` inside `B_-` and `d` inside `B_+`. Whoever owns EF-4.4 must confirm the "elimina `(1,1)`/`(n,n)`" argument covers `a ∈ B_-` (where the past loses `(1,1)` *and* part of `B_-`, so the deficit is `>=1`) — favourable, but it is asserted for the wrong reason if only `(1,1)` is invoked.
  - Nothing in the repo re-derives (EF4.9); `p1a_entropia_fibras_ef4.py` computes `small_product_threshold` (`:138`) but never checks the geometric inequality that justifies it.

- **Recommendation:** **PROCEED WITH CONDITIONS** — the trichotomy is exhaustive and (EF4.9) holds at every floor and boundary I could reach (slack exactly `(rho_n-1)/(4N_n)`, and `≈(3/4)rho_n/N_n` with exact counts), but before EF-4.3 is treated as `PROVED` the document should (i) print the two-line derivation of (EF4.9) making the `n/N>1` deficit and the `R_n<=4rho_n` condition explicit, (ii) record that `b=(s+1,s+1)` is the `p_0+1`-saturating case rather than "idéntico", and (iii) log that the `n=12` finite check cannot exercise multi-point staircases, so its pass is weaker than it reads.

#### Expert brief — Margin and envelope analyst

- **Assessment**: Yes — subject to inputs I do not own, the margin arithmetic of EF-4.4 does control all rivals **simultaneously**, and it does so correctly. The simultaneity is not manufactured by the margin argument at all: it is bought once, up front, by `G_n`'s union over the ≤ n⁴ *deterministic* index-interval pairs (`:1268-1280`), after which the per-rival comparison is a deterministic inequality on the event `F_n ∩ G_n`. No second union over rivals is needed and none is silently omitted. I found **no arithmetic defect** in (EF4.7), (EF4.9), (EF4.10)→(EF4.11), (EF4.12), (EF4.13) or the η-budget of (EF4.14): I re-derived all six by hand and they are exact. The four attack vectors I was given (discrete-lattice envelope, Cauchy–Schwarz direction, hidden 4η, unit-gap vs η) all **fail to land**. The two real findings are (a) an undisclosed numerical threshold n₀ ≈ 1.475×10⁶ with non-monotone jitter, and (b) an extreme first-order sensitivity of γ^loss to EF-4.3's cap `p₀+1` on the winning block — a cap that is *not* mine to certify and whose failure would drive γ^loss negative, not merely smaller.

- **Load-bearing facts**:
  - Envelope crossing, re-derived: `3+Nx² = p₀+1+N(1−x)²` ⟹ `x = 1/2 + (p₀−2)/(2N)`; value `= N/4 + p₀/2 + 2 + (p₀−2)²/(4N)`. Matches (EF4.11) exactly (`docs/hoja_de_ruta_agosto_2026.md:1360-1370`). Deficit `N/4+p₀ − (EF4.11) = p₀/2 − 2 − (p₀−2)²/(4N)` matches (EF4.12) exactly (`:1372-1376`).
  - `(p₀−2)²/(4N) ~ ρ²/(4N) ~ n^{1/3}(log n)^{2/3}/4 = o(ρ)`, so `γ^loss = (1/2+o(1))ρ_n`. Measured: `loss_gap/ρ` = 0.4979 / 0.4997 / 0.4999 at n = 10⁸/10¹⁰/10¹² (command below), consistent with `tests/test_p1a_entropia_fibras_ef4.py:190` asserting `0.45 < ratio < 0.51`.
  - `γ^small`, re-derived: `N/4 + p₀ − (2p₀ + N(1/8 + ρ/N)) = N/8 − p₀ − ρ = N/8 − 2ρ − 1`. Matches (EF4.13) exactly (`:1384-1389`). Positivity ⟺ `n > 18ρ_n + 10`; measured negative through n = 50 000 (`small_gap = −505.8`) and positive at n = 10⁵ (`+1552.5`).
  - (EF4.9) re-derived: `(N/2)(n/4+ρ)/N² ≤ 1/8 + ρ/N` ⟺ `n ≤ N + 4ρ = n + 2ρ − 2`, true for all ρ ≥ 1. **Valid** (`:1319-1325`).
  - (EF4.7) re-derived: `√(u₋v₋)+√(u₊v₊) ≤ √((u₋+u₊)(v₋+v₊))` is Cauchy–Schwarz on `(√u₋,√u₊)·(√v₋,√v₊)`. Direction is correct. `u₋+u₊ ≤ 1` and `v₋+v₊ ≤ 1` are forced because the past and future rectangles of a 4-chain have **strictly** ordered row and column endpoints (in a permutation each row carries one point, so row(q₂) < row(q₃)), hence the two row-intervals are disjoint and their *free*-row sets are disjoint. Overlap with the prescribed band is irrelevant: `u` counts only free rows. Then `f₊ ≤ (1−√f₋)²` follows since `1−√f₋ ≥ 0`. **Holds as stated** (`:1326-1339`).
  - η-budget, counted on both sides. Rival: `S ≤ min(3+Nf+η, p₀+1+Nf'+η) = η + min(...) ≤ η + (EF4.11)` — one η, because `min(m₁+e₁, m₂+e₂) ≤ min(m₁,m₂)+η`. Planted: `S₀ ≥ N/4+p₀−η` — one η, because `G_n` is two-sided and covers both planted rectangles at once. Strict domination ⟺ `γ > 2η`. **Exactly (EF4.14); no third or fourth η is needed and none is missing** (`:1413-1416`).
  - `η_n = √(3N log n)` with `N = N_n = n − R_n < n`, so `η_n < √(3n log n) = O(√(n log n))`; `ρ_n = Θ(n^{2/3}(log n)^{1/3})`; ratio `η/ρ ~ n^{−1/6}(log n)^{1/6} → 0`. `η_n = o(ρ_n)` ✓ (`:1399-1403`). The union arithmetic is exact: `2n⁴exp(−2·3N log n/N) = 2n⁴n^{−6} = 2n^{−2}` (`:1271-1275`).
  - `N` is the correct denominator everywhere: EF-3's tail is `2exp(−2u²/|I|) ≤ 2exp(−2u²/n)` (`:1044-1047`); EF-4 uses `2exp(−2η²/N)` with `|I_free| ≤ N`, which is the **weaker, conservative** direction. Safe.
  - Measured thresholds (command: `.venv/bin/python -c "from emergencia import p1a_entropia_fibras_ef4 as ef4; ..."`, evaluating committed code only):
    ```
    n=1e5   loss/2η=0.6698  small/2η=0.4396  PRE
    n=1e6   loss/2η=0.9429  small/2η=5.6521  PRE
    n=2e6   loss/2η=1.0474  small/2η=8.9030  PASS
    n=1e7   loss/2η=1.3408  small/2η=22.69   PASS
    n=1e12  loss/2η=8.3026  small/2η=6829    PASS
    ```
    Fine scan: first even n with both margins > 2η is **n = 1 474 934**; last failing even n in [1.46e6, 1.50e6] is **n = 1 475 204** (`loss/2η = 1.000000`). The predicate is *not* monotone across that window — the `ceil` in `ρ_n` produces jitter of ~270 in n.
  - Which constraint binds flips with n: `γ^small` is binding below ≈10⁶ (0.44 vs 0.67 at n=10⁵), `γ^loss` is binding above (0.94 vs 5.65 at n=10⁶). The doc discloses the pre-asymptotic status qualitatively at `:1499-1502` ("preasintótico en n=10⁵,10⁶ … satisface (EF4.14) en n=10⁷") but never states n₀.

- **What the three named tests certify, exactly**:
  - `tests/test_p1a_entropia_fibras_ef4.py:157` `test_loss_case_exact_envelope_dominates_a_dense_grid`: at the single size n = 10⁶, over 100 001 grid values of `f ∈ [0,1]`, `min{3+Nf, p₀+1+N(1−√f)²} ≤ (EF4.11) + 1e-7`. It certifies **only that the closed form (EF4.11) was transcribed correctly into `loss_case_mean_upper`** — a typo-catcher. It does **not** certify Cauchy–Schwarz (that step is *baked into* `loss_case_objective:118` as `other_product=(1-√f)²`, i.e. assumed, not tested), does not certify the caps 3 and `p₀+1`, does not certify that any real rival attains such an `f`, and cannot in principle fail, since (EF4.11) is a provable upper bound for every real `f`. Note also the grid step 1e-5 in `f` is ≈9.5 units in `Nf` at n=10⁶ — coarse relative to the peak, but harmless in the "≤" direction.
  - `:162` `test_fixed_margins_enter_the_proved_asymptotic_regime`: certifies `uniqueness_margin_positive` is **False at n=10⁵** and **True at n=10⁷**, with both gaps > 2η at 10⁷. It **pins the pre-asymptotic failure as intended behaviour**. It certifies nothing for 10⁵ < n < 10⁷ (where the real threshold and its jitter live) and nothing above 10⁷.
  - `:185` `test_loss_gap_has_the_declared_rho_over_two_scale`: certifies `γ^loss/ρ ∈ (0.45, 0.51)` and increasing at n = 10⁸, 10¹⁰, 10¹² — i.e. the `1/2` factor that committee 050 demanded. It does **not** compare γ^loss to η at all, and says nothing about cases (1) or (2).
  - No test anywhere exercises the case-(1) one-unit deterministic deficit, nor the exact `X₋ = X₊` flux identity (only its precondition, half-balance, at `:27-32`).

- **What would have to be true** (for another role to attack):
  1. EF-4.3's cap of **`p₀+1`** prescribed points on the *non-losing* block in case (3). This is the single most load-bearing input to my whole lane. Sensitivity: for a generic envelope `min{a+Nf, b+N(1−√f)²}`, the max is `a + (b−a+N)²/(4N)`, so the deficit from `N/4+p₀` is `p₀ − a + 1 − (b−a)/2 − (b−a)²/(4N)`. With `a=3, b=p₀+1` this is `p₀/2 − 2 − …` (EF4.12) ✓. With `b = 2p₀` (a rival holding *both* staircases in one block) the deficit becomes `−3/2 − (2p₀−3)²/(4N) < 0` — **the loss margin does not shrink, it inverts**. EF-4.3 excludes this by routing "cruces" into case (2) via (EF4.9); that exclusion is correct arithmetic (I checked (EF4.9)) but whether it is *exhaustive* is not mine.
  2. `X₋ = X₊` **pathwise** (not in mean), which needs exactly `N/2` free rows and `N/2` free columns per half. Verified as a precondition by `validate_even_balance` (`emergencia/p1a_entropia_fibras_ef4.py:86-94`) and tested at `:27-32`; the flux step itself I re-derived by hand: free-lower-rows mapped up = `N/2 − X₋` = free-upper-rows mapped down, so `X₊ = X₋`.
  3. The score of a block is `#prescribed + #free` with `p₀ = ρ+1` per planted side, and the primary component is `min(past, future)` — selector semantics, not mine.
  4. EF-3's hypergeometric tail (`:1036-1047`) is sound; EF-4 uses it in the conservative direction.

- **Arithmetic defects found**: none that break the argument. Specifically, the four attacks I was assigned all fail:
  1. **Lattice/discreteness of `f` (attack 1) — does not land.** The bound `min{g₁(f), g₂(f)} ≤ V*` holds for **every** `f ∈ [0,1]`, attainable or not: for `f ≤ f*`, `min ≤ g₁(f) ≤ g₁(f*) = V*`; for `f ≥ f*`, `min ≤ g₂(f) ≤ g₂(f*) = V*`. It never asks that the crossing be attained. Discreteness of `f = u·v` (a ratio of integer counts over `N²`) can only *shrink* the admissible set, and no neighbouring lattice value can exceed the pointwise envelope. Also both branches are valid bounds for *all* admissible `f` simultaneously (branch 1 bounds the losing block, branch 2 the other; neither has a restricted domain), so there is no "outside the range where both are valid" region. And `√f* = 1/2 + (ρ−1)/(2N) → 1/2 ∈ [0,1]`, so the crossing is interior. **Cost to repair: zero — nothing to repair.**
  2. **Cauchy–Schwarz (attack 2) — holds as stated**, direction correct, and `u₋+u₊ ≤ 1`, `v₋+v₊ ≤ 1` are genuinely forced by strict endpoint ordering in a permutation, including for rivals whose intervals straddle the prescribed band (the fractions count free rows/columns only). **Cost: zero.**
  3. **Hidden 4η (attack 3) — not present.** The budget closes at exactly 2η, one on each side, because `min` absorbs the two per-rectangle errors into a single η on each side and `G_n` covers all rectangles simultaneously. It closes **tightly**: (EF4.14) is `γ > 2η` with no spare, so any future correction that adds even one more η per side (e.g. if a score ever needed `max` rather than `min` over rectangles, or if the secondary lexicographic component needed its own concentration) would require `γ > 4η` — still asymptotically fine, but it would roughly quadruple n₀ (γ^loss/2η grows like n^{1/6}, so doubling the required ratio pushes n₀ from ≈1.5×10⁶ to ≈9×10⁷).
  4. **Unit gap vs η in case (1) (attack 5) — does not land, and the reason is precise.** Case (1) is not a comparison of *means* at all; it is a **pathwise** comparison on the same realisation ω. Both rival rectangles are set-theoretic **subsets** of the planted ones (interior endpoints are pinned at `(s,s)`/`(s+1,s+1)`; the past exterior can only move up from `(1,1)`, the future exterior only down from `(n,n)`), so the rival's block counts are `A₋−k₁`, `A₊−k₂` with `kᵢ ≥ 0`, `max(k₁,k₂) ≥ 1` because at least one of `(1,1)`, `(n,n)` is dropped and row n ↦ column n forces the drop to be genuine. Since `A₋ = A₊ = A` **exactly** (flux), `min(A−k₁, A−k₂) ≤ A−1 < A`. The η's cancel identically because they are the *same* η on the *same* ω. This is the correct argument and it is robust to the endpoint-inclusion convention (open intervals lose the new endpoint instead). **Cost: zero, but see risk 1.**

- **Risks / failure modes from this lens**:
  1. **Case (1) has literally one unit of slack and it is not tested.** It survives η only because `X₋ = X₊` holds *exactly*. If the half-balance ever failed by one — a different `ρ` parity, an odd `N`, a change to `build_even_prescription` — then `A₋ = A₊ ± 1` and the one-unit deterministic deficit is exactly cancelled, producing a **tie** (`min` equal), which destroys uniqueness and hence (EF4.15). `certificate_bounds` never checks `free_count % 2 == 0` or the balance; only the test at `:27-32` does, and only at three hard-coded n. This is the most brittle single hinge in EF-4.4 and it is not the one committee 050 broke.
  2. **The `1/2` factor is not a comfort margin, it is the whole margin.** γ^loss = `p₀/2 − 2 − …` is a *first-order* residue of `p₀ − p₀/2`. Any O(ρ) leakage in the cap on the winning block (EF-4.3's `p₀+1`) flips the sign outright, as computed above. Committee 050's refutation was exactly this class of error, one rung up.
  3. **Undisclosed, non-monotone threshold.** n₀ ≈ 1.475×10⁶ with the predicate failing again as late as n = 1 475 204. The doc's asymptotic claim is unaffected (only ratios are used, `:1501-1502`), but any reader who tries to instantiate EF-4 at a finite n will get a silently false certificate for all n < 1.47×10⁶, and `certificate_bounds` reports this only through `uniqueness_margin_positive`, which no non-test caller consults except `main()`'s final assertion at n=10⁷.
  4. **`validate_loss_optimization` is near-tautological** and could give false assurance in a review: it grids a function against its own provable supremum. It cannot fail unless the closed form was mistyped. It is not evidence that the envelope is the right envelope.
  5. The margins are compared against `2η` with `η = √(3N log n)` derived from a union over `n⁴` rectangles. That constant `3` is tuned so that `2n⁴·n^{−6} = 2n^{−2}`. If the rectangle count were ever recounted as, say, `n⁵` (e.g. if a triple of intervals were needed), η would grow only by `√(7/3)` and n₀ by ≈5×, so this is not fragile. Noted as *not* a risk.

- **What you could not determine**:
  - Whether EF-4.3's case-(3) caps (`≤3` on the losing block, `≤ p₀+1` on the other) are exhaustively justified. My sensitivity computation shows this is the make-or-break input, but the trichotomy is another role's. `[UNVERIFIED here]`
  - Whether the frozen `MIN_COVERAGE_LEX` primary score is in fact `#prescribed + #free` over the closed rectangle and `min` over the two blocks. All of EF-4.4's arithmetic presumes this. `emergencia/p1a_comparar_selectores_d2.py` is imported by the tests but I did not audit its scoring convention; `tests/test_p1a_entropia_fibras_ef4.py:41-60` only checks that appending an incomparable point preserves the selector, not the score's definition. `[UNVERIFIED]`
  - Whether the trichotomy test at `:63-154` (n=12, ρ=2) is in the regime where the caps it asserts (`≤3`, `≤ρ+2`) coincide with the asymptotic ones; at n=12, N=6 and `γ^small = 6/8−4−1 < 0`, so that test exercises exhaustiveness only, never the margins. Closing this would need the same brute force at an n where γ^small > 0, i.e. n ≳ 10⁵ — combinatorially out of reach, and enlarging n is forbidden this session.
  - Whether `Pr(G_n^c | F_n) ≤ 2n^{-2}` is compatible with EF-4.5's `(1 − 2n^{-2})/(n)_{R_n}` — that is EF-4.5's lane, not mine.

- **Recommendation**: **PROCEED WITH CONDITIONS.** The quantitative margin argument of EF-4.4 is arithmetically correct, closes at exactly 2η, and does control all rivals simultaneously via `G_n`'s deterministic union — but conditional on EF-4.3's `p₀+1` cap (whose failure inverts γ^loss rather than shrinking it) and on the exact `X₋ = X₊` balance (whose failure by one unit collapses case (1) into a tie); I would ask the chair to record the measured threshold n₀ = 1 474 934 with jitter to 1 475 204 in the brief, and to note that `test_loss_case_exact_envelope_dominates_a_dense_grid` is not independent evidence for the envelope.

#### Expert brief — Selector-semantics analyst

- **Assessment:** Yes on both counts, with one wording defect and one provenance gap. The object EF-4 maximises **is** the frozen `MIN_COVERAGE_LEX` score: the frozen score has exactly two integer components, `(min(m_-,m_+), m_-+m_+)`, both raw closed-interval cardinalities, with a constant eligibility threshold `K0 = 3`; the first component *is* the `MIN_ONLY` score, so a strict win on it is genuinely sufficient for uniqueness of the lexicographic argmax. The event `S` is "the argmax of `S_lex` over `Q_3(C)` exists and is unique" — the same event at every site I checked (EF3.9, EF4.15, EF4.16, EF4.18), never silently narrowed to "returns `q_0`". The parity transfer preserves candidates, ties and winner because **nothing in the frozen selector is normalised by `n`**: I verified this against the definition, not the prose. The residual defects are (a) `[UNVERIFIED-by-seal]` provenance — `make verify-seal` does not cover the module where the selector lives — and (b) a misleading sentence at :1417 that routes the argument through `MIN_ONLY`, which the frozen contract explicitly forbids treating as a stage of `MIN_COVERAGE_LEX`.

- **Load-bearing facts:**
  - Frozen score, authoritative: `emergencia/P1a_contrato_comparacion_selectores_balanceados_d2.md:18-24` — `S_min(q)=min(m_minus,m_plus)`, `S_lex(q)=(min(m_minus,m_plus), m_minus+m_plus)`, maximised lexicographically. Two components, both raw counts. Domain `Q_3(C)` at `:36-44`: `a≺b≺c≺d`, `|[a,b]|>=3`, `|[c,d]|>=3`. Names frozen at `:51-52`: `MIN_ONLY = maximiza S_min; MIN_COVERAGE_LEX = maximiza S_lex`.
  - Same definition, verbatim, in the count-volume contract: `emergencia/P1a_count_volume_experimento_condicionado_d2.md:47-62`, including `MIN_COVERAGE_LEX(C) = q* = argmax S_lex si el argmax es unico; UNDEFINED si Q_3(C)=vacio o hay empate`.
  - Explicit warning that lex is **not** a tiebreak on top of `MIN_ONLY`: `emergencia/P1a_contrato_comparacion_selectores_balanceados_d2.md:56-58` — "`MIN_COVERAGE_LEX` es un selector distinto, no un desempate aplicado después de ejecutar `MIN_ONLY`."
  - Implementation matches: `emergencia/p1a_comparar_selectores_d2.py:246` `eligible = counts >= sealed.K0`; `:305-306` `MIN_ONLY` outcome carries `minimum_best`; `:361-366` `MIN_COVERAGE_LEX` outcome carries `(minimum_best, lex_secondary_best)` — i.e. the lex **primary component is literally the `MIN_ONLY` optimum value**. `emergencia/p1a_enumeracion_simulacion.py:32` `K0 = 3`; `:173-199` `interval_count_matrix` returns *closed*-interval cardinalities with strict comparability (`comparable = (i<j) & (v_i<v_j)`).
  - No `n`-dependence anywhere in the selector: the eligibility threshold is the constant `3`, both score components are unnormalised counts, and the only `n`-normalised object in the program (`Z_n`, `(K+1)(L+1)/n^2`, `docs/hoja_de_ruta_agosto_2026.md:1060-1072`) is an *observable* computed after `S`, not an input to `S`. Hence "no altera scores" at :1450-1451 is true for the frozen score, not merely for interval cardinalities. This is the conjunct most likely to have been false and it survives.
  - Strict first-component dominance ⇒ unique lex argmax: valid, because lexicographic comparison is decided by component 1 whenever it differs; ties on component 2 are then unreachable. Formally: if `S_lex(q_0)_1 > S_lex(q)_1` for all `q ∈ Q_3\{q_0}`, then `q_0` is the strict lex maximum. No second-component analysis is needed, and the roadmap correctly performs none.
  - Uniqueness must be at the level of **quadruples**, not `(b,c)` bridges — the code counts quadruple multiplicity (`left_mult`/`right_mult`/`left_equal`/`right_equal`, `:246-249`, `:307-320`), so rivals differing only in `a` or `d` are genuine tie sources. EF-4 covers them: case (1) at `docs/hoja_de_ruta_agosto_2026.md:1336-1339` ("cambiar el endpoint exterior pasado elimina `(1,1)` … cualquier cambio reduce estrictamente el mínimo al menos en una unidad, sin usar discrepancia"). This is sound only because the two planted sides are *exactly* equal, which is asserted and which I checked independently: `docs/hoja_de_ruta_agosto_2026.md:1246-1250` (`X_-=X_+` by flow conservation). Recomputed: with `k` free lower-half rows mapped to upper-half columns, lower-half free columns give `N/2 = (N/2-k)+k'` so `k'=k` and `X_+=N/2-k'=X_-`. Exact, deterministic per completion. Also checked the half-balance premise: prescribed rows/columns split `rho+1` per half (from `:1214-1222`), so free rows = free columns = `N/2 = s-rho-1` per half. Both hold.
  - Injectivity and the `1/n`: `sigma ↦ pi` with `pi(i)=sigma(i)+1 (i<n), pi(n)=1` is a bijection `S_{n-1} → {pi ∈ S_n : pi(n)=1}`, image size `(n-1)!`. Hence `Pr_n(S) >= (n-1)!·Pr_{n-1}(S)/n! = Pr_{n-1}(S)/n`. The counting at :1452-1455 is right, and the constant is exact, not lossy-by-more.
  - Incomparability of `(n,1)`: for `i<n`, `i<n` but `pi(i)=sigma(i)+1 >= 2 > 1 = pi(n)`, so `i ⊀ n`; and `n ⊀ i` since `n>i`. Therefore no chain `a≺b≺c≺d` can use it, `Q_3` is unchanged as a set, and no closed interval `[x,y]` gains a point (an interval requires `x ≼ z ≼ y`). Both score components and eligibility are therefore literally invariant. Code agrees: `emergencia/p1a_entropia_fibras_ef4.py:52-58` `append_incomparable` shifts values up and appends `0` at the last position.
  - Certification by test: `tests/test_p1a_entropia_fibras_ef4.py:41-60` iterates **all 720 permutations of size 6**, embeds each to size 7, and asserts equality of `state` (EMPTY/UNIQUE/TIE), `n_maximizers`, `primary_score`, `secondary_score`, the winning `quadruple` (same indices), and `past_size`/`future_size`. That is an exhaustive, exact certification of the (EF4.17) invariance — but **only at `n=6 → 7`**. It is not a proof at general `n`; the proof is the incomparability argument above, which does hold at general `n`.
  - Seal scope: `Makefile:15-17` — `verify-seal` hashes `nachocausal/thresholds.py` only. `K0`, `interval_count_matrix` and the `MIN_COVERAGE_LEX` implementation live in `emergencia/p1a_enumeracion_simulacion.py` and `emergencia/p1a_comparar_selectores_d2.py`, which the seal does not cover. Provenance instead: `git log --oneline -3 -- emergencia/p1a_comparar_selectores_d2.py emergencia/p1a_enumeracion_simulacion.py emergencia/P1a_contrato_comparacion_selectores_balanceados_d2.md` → single commit `0992277`; `git log -S"K0 = 3" --oneline -- emergencia/p1a_enumeracion_simulacion.py` → `0992277` only. So the selector and `K0=3` have never been edited since introduction. Adequate, but by git archaeology, not by the seal.

- **Definition of `S` as actually used at each site:** Identical at all four.
  - Master definition: `docs/hoja_de_ruta_agosto_2026.md:207` — "`S(pi)` es el evento de que ese maximizador exista y sea único", over the selector defined at `:199-206` (the frozen lex pair with `|I|>=3`). Matches `emergencia/P1a_count_volume_experimento_condicionado_d2.md:61` — "`S = { MIN_COVERAGE_LEX(C) esta definido } = { el argmax de S_lex es unico }`", plus `:63-64` "`S` es un evento sobre la realización completa del poset … depende de todo `Q_3(C)`".
  - (EF3.9) at `:1099`, via `p_n = Pr_n(S)` introduced at `:1081`: the same `S`, EXISTENCE + UNIQUENESS, no reference to any particular quadruple. Good.
  - (EF4.15) at `:1421`: proves the strictly stronger statement "on `F_n∩G_n` the unique maximiser is `q_0`", which implies `S`. This is the safe direction — proving more than needed does not break the composition.
  - (EF4.16) at `:1431` and (EF4.18) at `:1455`: `Pr_n(S)` with the same `S`; (EF4.18) transfers unique-argmax-exists between sizes, which is exactly what the invariance argument gives.
  - No site conditions `S` on `q* = q_0`, on admissibility separately, or on the side `h`. The side `h` is fixed before conditioning (`:210-212`) and does not enter `S`. **Verdict: no semantic drift of `S` between EF-3 and EF-4.**

- **What would have to be true (assumptions my clearance rests on, for other roles to attack):**
  1. The trichotomy at `:1310-1315` really exhausts *all* of `Q_3(C)\{q_0}` (not just quadruples of a nice shape). I grant this; if it leaks a rival class, my strict-dominance conclusion fails immediately, because uniqueness is a universally quantified statement over `Q_3`.
  2. The margins (EF4.12)/(EF4.13) really exceed `2*eta_n` for all large even `n`, so that every case-(2)/(3) rival is strictly below on component 1. I grant this.
  3. `X_- = X_+` exactly (`:1246-1250`). I checked this one myself and it holds; but note it is load-bearing *for me*, not just for the margin role: if the two planted sides were unequal, a case-(1) rival that shaves the larger side would **tie on component 1** and the sentence at :1417 ("único maximizador de `MIN_ONLY`") would be false. The lex selector would still pick `q_0` via component 2, but the roadmap's stated route would be broken.
  4. `eta_n = o(N_n)` so that the planted's per-side cardinality `>= N/4+p_0-eta_n` exceeds `3` for large `n` (admissibility). Holds with `eta_n = O(sqrt(n log n))`, `N_n = n - o(n)`.

- **Semantic gaps found:**
  1. **:1417 routes uniqueness through `MIN_ONLY`, which the frozen contract forbids as a reading of the lex selector** (`P1a_contrato_comparacion_selectores_balanceados_d2.md:56-58`). Substantively the inference used is "strict win on component 1 ⇒ unique lex argmax", which is valid and does *not* treat lex as `MIN_ONLY`+tiebreak. But the sentence as written invites exactly the forbidden reading, and it makes the certificate needlessly depend on assumption (3) above. A reader auditing §8 compliance (`:1657-1658`, no changes to `MIN_COVERAGE_LEX`) will stumble here. Wording defect, not a mathematical defect.
  2. **"Admisible" is never defined in EF-4, and "sus cardinalidades tienden a infinito" is a proxy, not the condition.** The actual condition is `min(|[a,b]|,|[c,d]|) >= K0 = 3`, a *constant* threshold (`p1a_enumeracion_simulacion.py:32`, roadmap `:204`). Divergence to infinity is a sufficient but strictly stronger asymptotic statement, and phrasing it as a limit obscures that what is needed is a per-`n`, on-event bound: on `F_n∩G_n`, `N/4+p_0-eta_n >= 3` for `n >= n_0`. That is true, so the gap is expositional. It would be a real gap if `K0` grew with `n` — it does not.
  3. **`F_n ∩ G_n ⊆ S` is only established for `n >= n_0`** ("para todo `n` par suficientemente grande", `:1400-1409`), never for all even `n`. (EF4.16) correctly says "para tamaños pares grandes" and the conclusion is asymptotic, so this is harmless — but (EF4.18) applied to odd `n` implicitly needs the even predecessor to be past `n_0` and `>= 8` (`p1a_entropia_fibras_ef4.py:64-65`), which is nowhere stated. Harmless asymptotically; incomplete as written.
  4. **Provenance gap.** The dossier line "sello intacto" (`make verify-seal` → `thresholds.py sha256: …`) is **not** evidence that `MIN_COVERAGE_LEX` or `K0` is unchanged: the seal covers `nachocausal/thresholds.py` only (`Makefile:15-17`), and the selector lives elsewhere. I closed this by git (`0992277`, never touched), but the forum should not treat the seal as covering the selector.

- **Risks / failure modes from this lens:**
  - If the trichotomy role finds a rival class that ties `q_0` on component 1 (e.g. a quadruple whose losing side happens to hit exactly `p_0 + X_-`), the certificate does **not** automatically die: `MIN_COVERAGE_LEX` could still be unique via `m_-+m_+`. But EF-4 gives **no** second-component analysis at all, so in that scenario the roadmap has nothing to fall back on and (EF4.15) fails as written. The certificate is single-component-fragile by construction.
  - Symmetrically: any future edit that added a normalisation by `n` to either component, or made `K0` grow with `n`, would silently invalidate the (EF4.17)-(EF4.18) transfer while leaving the prose "no altera scores" unchanged. The `n=6` test would catch a normalisation change but not an `n`-dependent threshold (at `n=6→7` a threshold like `ceil(n/2)` changes from 3 to 4 and the test *would* catch it; a threshold like `ceil(log n)` would not). The invariance is currently protected by a single 720-permutation test at one size.
  - The `1/n` factor is applied once per odd size and never compounded; if anyone later chained it across several sizes, the cost would become `log(n!) = Θ(n log n)` and break `o(n)`. Nothing in the text forbids that misuse.

- **What you could not determine:**
  - Whether the trichotomy at `:1310-1315` is exhaustive over `Q_3` (explicitly another role's; I granted it, and my whole clearance is conditional on it).
  - Whether the margin arithmetic (EF4.10)-(EF4.14) is correct, including whether the closed-interval endpoint convention (`interval_count_matrix` counts both endpoints) is the one used in the `3 + Nf` and `p_0+1+N(1-sqrt f)^2` envelopes at `:1350-1356`. A ±2 endpoint convention mismatch would move `gamma_n^loss` by O(1) only, so it does not threaten the `Θ(rho_n)` margin — but I did not verify it, `[UNVERIFIED]`. Closing it requires the margin role to state which points the envelope counts.
  - Whether `test_incomparable_embedding_preserves_the_frozen_selector` holding at `n=6→7` generalises — it does by the incomparability argument, which I verified analytically; no larger-`n` test exists and the PI forbids enlarging `n`, so this stays proof-backed rather than test-backed.

- **Recommendation:** PROCEED WITH CONDITIONS — the maximised object is genuinely the frozen `MIN_COVERAGE_LEX`, `S` means the same thing at every site, and the even-to-odd transfer is exactly invariant (raw counts, constant `K0=3`, `Q_3` unchanged, injective map, exact `1/n`); condition on (i) rewording :1417 to state the inference as "strictly dominates every rival on the first lexicographic component" instead of routing through `MIN_ONLY`, (ii) replacing "sus cardinalidades tienden a infinito" with the actual on-event bound `>= 3`, and (iii) not citing `make verify-seal` as provenance for the selector, which it does not cover.

#### Expert brief — Inference-chain and evidence engineer

- **Assessment:** The **composition is sound** — I found no mishandled conditioning anywhere in the chain (EF4.3)→(EF4.6)→(EF4.15)→(EF4.16)→(EF4.18)→(EF4.19)→(EF3.9)→(EF4.20). Every arithmetic step I could re-derive checks out, and the one conditional probability in the chain is multiplied by the event it is conditioned on, which is the only legitimate use. The **evidence does not match the declared tokens**: three of the four `PROVED`-class tokens rest entirely on prose. Worse, the executable verifier *certifies that the certificate is false* at n=10⁵ and n=10⁶, and the one test that targets the load-bearing structural claim (the trichotomy underlying EF4.15) is **provably vacuous**.

- **Load-bearing facts:**
  - `(n)_{R_n}` factor count is correct. `docs/hoja_de_ruta_agosto_2026.md:1215-1224` prescribes 4 special points + two staircases of `rho_n-1` points; `4 + 2(rho_n-1) = 2rho_n+2 = R_n` (:1206). Confirmed in code: `emergencia/p1a_entropia_fibras_ef4.py:73-78` builds a 4-entry dict plus `range(1,width)` twice and asserts `expected = 2*width+2`; `:79-80` asserts no row/column collision. No double-counting.
  - The band is fully prescribed. Rows `s-rho+1..s-1` (lower stair), `s`, `s+1`, `s+2..s+rho` (upper stair) = exactly the `2rho_n` rows of `{s-rho_n+1,...,s+rho_n}` (:1226-1228). This is load-bearing for the trichotomy ("Dentro de la banda toda fila está prescrita", :1319).
  - `p_0 = rho_n+1` per side is correct: past rectangle `[1,s]×[1,s]` contains `(1,1)`, `(s,s)` and all `rho_n-1` lower-stair points (their columns `q_1+1..q_1+rho_n-1 < s` since `rho_n < n/4`). Symmetric for the future. Matches :1244-1250.
  - `X_- = X_+` exactly (:1246-1250) is a genuine deterministic identity, not a mean statement: prescribed rows ≤ s number `2 + (rho-1) = rho+1` and prescribed columns ≤ s likewise, so each half has exactly `N/2` free rows and `N/2` free columns; flow conservation then forces `X_+ = N/2 - (N/2 - X_-) = X_-`. `validate_even_balance` (`emergencia/p1a_entropia_fibras_ef4.py:86-94`) tests exactly this hypothesis.
  - (EF4.6) arithmetic: `2n^4 exp(-2·3N log n/N) = 2n^4 n^{-6} = 2n^{-2}` (:1268-1276). Correct. The union is over ≤ n⁴ *deterministic* index pairs, taken before the selector acts (:1277-1280) — conservative (n > N), so safe.
  - (EF4.11)/(EF4.12) re-derived by hand: at `√f = 1/2 + (p_0-2)/(2N)`, `3 + Nf = N/4 + p_0/2 + 2 + (p_0-2)²/(4N)`. Exactly :1362-1370. `gamma^loss = p_0/2 - 2 - (p_0-2)²/(4N)`; since `(p_0-2)²/(4N) / rho ≈ rho/(4N) → 0`, this is `(1/2 - o(1))rho_n`. (:1374 writes `(1/2+o(1))`; sign of the `o(1)` is cosmetic.)
  - `log((n)_{R_n}) = Σ_{k<R_n} log(n-k) <= R_n log n`; `-log(1-2n^{-2}) = O(n^{-2}) = o(1)`. (EF4.16) at :1430-1438 is correct.
  - Asymptotics of (EF4.14) are genuinely true: `gamma^loss/2eta ~ (rho/2)/(2√(3n log n)) = Θ(n^{1/6}(log n)^{-1/6}) → ∞`, and `gamma^small ~ n/8` vs `2eta = O(√(n log n))`. The inequality (:1404-1410) is not in doubt asymptotically; only its threshold is.
  - `docs/manuscript_limits_draft.md` contains **zero** references to EF-4: `grep -rn 'EF-4\|EF4\|FIBER_CONCENTRATION\|SELECTOR_CLASS_THEOREM\|entropia_fibras' docs/manuscript_limits_draft.md` → no output. The manuscript is **not** contaminated, contrary to the dossier's downstream list.
  - `gh pr view 4` → `Update fiber entropy program and EF-8 preflights`, state `OPEN` (draft), body: "closes and documents the fiber-entropy roadmap through EF-7, including the EF-3/EF-4 verification machinery". EF-4 is unmerged and unpublished.

- **Conditioning defects found:** *none that break the chain.* Enumerated, with why each holds:
  1. **(EF4.3)×(EF4.6) product — HOLDS.** `Pr(S) >= Pr(F_n ∩ G_n) = Pr(F_n)·(1 - Pr(G_n^c|F_n)) >= (1-2n^{-2})/(n)_{R_n}`. This is the definition of conditional probability, not a multiplication of two differently-conditioned probabilities. The chain is designed so that the *only* conditional event (`G_n`) is conditioned on the *only* unconditional event (`F_n`) it is multiplied against. No defect.
  2. **Trichotomy is deterministic given `F_n` — HOLDS.** `f_-, f_+` (:1291-1294) are functions of the rival's rectangles and the free row/column sets, and the free sets are *determined* by `F_n`. So the case classification is not a random event and cannot be mis-conditioned. Randomness enters only through `G_n` converting fractions into counts.
  3. **The factor 2 on `eta_n` — HOLDS and is necessary.** Planted is bounded below by `N/4 + p_0 - eta_n`, rival above by `(bound) + eta_n`; the gap needs `gamma > 2eta_n`. `emergencia/p1a_entropia_fibras_ef4.py:38-39` uses `2.0 * discrepancy_radius` for both gaps. Consistent.
  4. **Case (1) covers the endpoint-multiplicity trap — HOLDS.** The frozen selector counts *quadruples*, not bridges: `minimum_nmax = Σ left_ge[b]*right_ge[c] - left_gt[b]*right_gt[c]` (`emergencia/p1a_comparar_selectores_d2.py:284-289`). Uniqueness therefore requires a unique outer `a` and `d`, not just a unique bridge. Case (1) (:1387-1391) handles exactly this, and it works *only because* `X_-=X_+` makes both planted sides exactly equal, so any strict shrink of either side strictly lowers the min. If the balance identity were only "in mean", case (1) would fail. It is exact.
  5. **`MIN_ONLY` → lex uniqueness — HOLDS.** Strict maximality in the first lexicographic component implies uniqueness regardless of the second (:1417-1419), and cases (1)–(3) all deliver a strictly smaller first component.
  6. **Admissibility (`K0`) — HOLDS.** `sealed.K0 = 3` (`emergencia/p1a_enumeracion_simulacion.py:32`); on `F_n∩G_n` the planted has `>= N/4 - eta_n + p_0 → ∞` per side. The clause at :1415-1416 is not decoration; it is required by `eligible = counts >= sealed.K0`.
  7. **(EF4.17)/(EF4.18) parity transfer — HOLDS.** `(n,1)` vs `(i, sigma(i)+1)`: `i<n` but `sigma(i)+1 >= 2 > 1`, so genuinely incomparable; it lies in no order interval, so no count changes and no 4-chain uses it. Injectivity gives `Pr_n >= (1/n)Pr_{n-1}` from `|S_n| = n|S_{n-1}|`.
  8. **o(n) preservation across parity — HOLDS, no boundary gap.** For odd `n`: `log(1/Pr_n) <= log n + R_{n-1}log(n-1) + o(1) = O(n^{2/3}(log n)^{4/3})`. Adding `log n` to that leaves the order unchanged, a fortiori `o(n)`. The "para tamaños pares grandes" quantifier (`∃n_0 ∀ even n>=n_0`) transfers to `∀ odd n >= n_0+1`; the finitely many `n < n_0` are irrelevant because `o(n)` constrains only the tail. There is no boundary gap here.
  9. **(EF4.19) into (EF3.9) — HOLDS, quantifier order is correct.** (EF3.9) at `:1094-1100` is a *finite-sample* inequality holding for every `n` and every `epsilon>0` simultaneously; the `o(n)` bound on `log(1/p_n)` does not involve `epsilon` at all. So `log(2n^4 e^{-2n eps²}/p_n) = -2n eps² + o(n) → -∞` for each fixed `eps`, giving `limsup Q_{2,n} <= eps`, then `eps ↓ 0`. The "for each fixed epsilon then arbitrary" order at :1470-1477 is legitimate precisely because the hypothesis is uniform in `epsilon`. `Q_{2,n} >= 0` (conditional MSE) closes it. No defect.
  - The only interface I could not fully audit is (EF3.9)'s own derivation from (EF3.5)/(EF3.8), which needs `Delta_n <= 1` — true since `N_pi(I,J)/n ∈ [0,1]` — and the martingale tail at `:1039-1049`, which is **prose only** with no executable check of the Azuma step.

- **What the tests actually certify:**
  - `test_even_prescription_is_an_injective_partial_permutation` (:14) → the dict at n=10⁵ has `2rho+2` distinct rows and distinct columns and the four special fixed points. Certifies (EF4.2) injectivity **at n=10⁵ only**.
  - `test_prescription_leaves_exactly_half_the_residual_on_each_side` (:27) → the `rho+1` per-half balance (hypothesis of `X_-=X_+`) at n ∈ {10⁵,10⁶,10⁷}. This is the most load-bearing thing the suite actually checks.
  - `test_invalid_or_colliding_prescriptions_are_refused` (:34) → input validation only. Certifies nothing mathematical.
  - `test_incomparable_embedding_preserves_the_frozen_selector` (:41) → over all 720 permutations of `S_6`, the map (EF4.17) preserves state, `n_maximizers`, both scores and the selected quadruple, against the **frozen selector module**. This is the strongest test in the suite and it certifies (EF4.17) exactly — **at n=6→7 only**.
  - `test_geometric_trichotomy_exhausts_all_abstract_n12_chains` (:63) → **vacuous.** See next bullet.
  - `test_loss_case_exact_envelope_dominates_a_dense_grid` (:157) → the closed form (EF4.11) dominates `min{3+Nf, p_0+1+N(1-√f)²}` on a 100 001-point grid, at n=10⁶. Certifies the 1-D optimisation (EF4.10)→(EF4.11).
  - `test_fixed_margins_enter_the_proved_asymptotic_regime` (:162) → asserts `not early.uniqueness_margin_positive` at n=10⁵ and `late.uniqueness_margin_positive` at n=10⁷. **The test formally certifies that (EF4.14) is FALSE at n=10⁵.**
  - `test_prescription_cost_is_subexponential_on_log_scale` (:171) → `R_n log n / n` decreasing and `R_n log n / (n^{2/3}(log n)^{4/3}) ∈ (1.9,2.1)` at n ∈ {10⁸,10¹⁰,10¹²}. Certifies the *arithmetic* of (EF4.16) but not (EF4.16) itself — `Pr_n(S)` never appears.
  - `test_loss_gap_has_the_declared_rho_over_two_scale` (:185) → `gamma^loss/rho ∈ (0.45,0.51)`, increasing, at n ∈ {10⁸,10¹⁰,10¹²}. Certifies (EF4.12)'s constant.
  - `.venv/bin/python emergencia/p1a_entropia_fibras_ef4.py` → `LOSS_GAP_OVER_2ETA = 0.669836 (n=10⁵), 0.942871 (10⁶), 1.34077 (10⁷)`; `CERTIFICATE=PREASYMPTOTIC, PREASYMPTOTIC, PASS`. The verifier confirms the certificate **fails** for all n ≤ 10⁶ with these constants and holds at exactly one checkpoint.

- **The trichotomy test is provably vacuous (new finding).** `tests/test_p1a_entropia_fibras_ef4.py:63-154` runs `n=12, rho=2`, giving `N=6` and `threshold = 1/8 + rho/N = 1/8 + 2/6 = 0.458333` (`:72`). But by (EF4.7) with disjoint row and column intervals, `min(f_-,f_+) <= 1/4` for *every* rival. Since `0.25 < 0.4583`, the `small_product` disjunct at `:120-122` is **unconditionally true**, so the assertion at `:154` (`fixed_inner or small_product or loss_case`) can never fail. Diagnostic over the test's own loop confirms: `tuples= 245025 small_product_true= 245025 max_min_free_product= 0.25`. The test therefore certifies **nothing** about case (1), case (3), or the exhaustiveness of the trichotomy — which is exactly the geometric content that (EF4.15) rests on. Non-vacuity would require `tau_n <= 1/4`, i.e. `n >= 10*rho + 2` (n ≥ 22 at rho=2); the constraint `rho < n//4` at `emergencia/p1a_entropia_fibras_ef4.py:68` forces `rho=2` at `n=12`, so this specific size can never be non-vacuous.

- **Declared-token vs evidence gap:**
  - `EF4_CORRECTED_PRESCRIBED_FAMILY = PROVED` (:1505) — **partially backed.** The integer construction, injectivity and half-balance are executably verified at n ∈ {10⁵,10⁶,10⁷}. The geometric trichotomy (EF-4.3) that makes the family *work* is **prose only**; its one test is vacuous.
  - `EF4_UNIQUE_SELECTION_ENTROPY = SUBEXPONENTIAL_PROVED_FULL_SEQUENCE` (:1506) — **no executable backing for the claim itself.** No test evaluates `Pr_n(S)`. `entropy_log_upper_bound` (`emergencia/p1a_entropia_fibras_ef4.py:180-184`) computes `R_n log n`, i.e. the *right-hand side*, and never touches the left. The link to `Pr_n(S)` is (EF4.15), which is unverified. `test_incomparable_embedding...` backs the `FULL_SEQUENCE` half (parity transfer) at n=6 only.
  - `EF4_Q2_ASYMPTOTIC = Q2_TO_ZERO_PROVED` (:1507) — **zero executable backing.** Pure prose deduction from (EF4.19) + (EF3.9). The only executable `Q_{2,n}` values anywhere are the four exact ones at n=6..9 (:1140-1148), which the roadmap itself says "no se extrapola" (:1152).
  - `EF4_TERMINAL = FIBER_CONCENTRATION` (:1508) — downstream of the above; no independent backing.
  - `EF4_MONTE_CARLO = NOT_RUN` and `EF4_GAUSS_KUZMIN = NOT_USED` (:1511-1512) — honest and confirmed by the script's own output.
  - **How much comfort can finite tests give?** Essentially none for the asymptotic claim. The verifier's honest concession at :1499-1503 understates the situation: the finite evidence is not merely "preasintótico", it is a **confirmed failure** of (EF4.14) at every checkpoint below 10⁷. The claim is asymptotic and its finite evidence is one data point at n=10⁷ plus three ratio checks. That is consistent with the proof but cannot corroborate it: any error in the trichotomy would leave every one of these numbers unchanged, because none of them evaluates a permutation. **No test in the suite ever computes `Pr_n(S)` or exhibits a single permutation in `F_n ∩ G_n`.** The whole certificate's contact with the frozen selector is the 720 permutations of `S_6` in `test_incomparable_embedding_preserves_the_frozen_selector`.

- **Blast radius if (EF4.15) fails:**
  - Immediate: (EF4.16), (EF4.19), (EF4.20) all fall; tokens at :1505-1508 must revert; gate EF-4 `PASS` (:1514) must revert to the EF-3 state `EF3_TERMINAL = OPEN_AFTER_FIBER_AUDIT` (:1180) and obligation (EF3.12) at :1162 reopens.
  - `EF3_SUBEXPONENTIAL_SELECTION_IMPLIES_FIBER_CONCENTRATION = PROVED` (:1176) **survives** — it is the conditional implication (EF3.10), independent of EF-4. EF-3 is cleanly insulated; the rollback is well-defined.
  - Header `ESTADO: CIERRE FUERTE EN FIBER_CONCENTRATION` (:5), §9 "cierre fuerte" (:1671-1681), §10 summary (:1711-1714), and §11 `LINE_STATUS_2026_08_12` / `EF4_STATUS: COMPLETE_ASYMPTOTIC` / `EF4_TERMINAL` (:1733,:1740-1741) all become false and must be retracted.
  - EF-7: `EF7_SELECTOR_CLASS_THEOREM = PROVED` (:1607) fails **partially**. Layers 1 and 2 (abstract change-of-measure lemma; class theorem for adaptive rank-rectangle selectors) are conditional on `-log Pr(S_n)=o(n)` and survive; layer 3 — "el certificado específico de pertenencia de `MIN_COVERAGE_LEX`, formado por la familia prescrita, el margen de unicidad y la transferencia par–impar de EF-4" (:1620-1622) — is exactly EF-4 and dies. `EF7_MIN_COVERAGE_LEX_ROLE = NONTRIVIAL_MEMBERSHIP_CERTIFICATE` (:1610) must be retracted; `SELECTOR_CLASS_THEOREM` degrades to a theorem with no verified member.
  - EF-6: `EF6_RESULT_CLASS = FAMILY_SPECIFIC_RESULT` classifies "el puente condicionado de EF-3 más el certificado prescrito de unicidad de EF-4", which would become a classification of a refuted object. Exposure is limited: `EF6_PRIORITY_STATUS = PRIORITY_NOT_CERTIFIED` and `EF6_DESTINATION = STANDALONE_TECHNICAL_NOTE_BEFORE_MANUSCRIPT_INTEGRATION` were already set, so nothing was externalised.
  - **`docs/manuscript_limits_draft.md` is NOT contaminated** (grep returns nothing for EF-4/EF4/FIBER_CONCENTRATION/SELECTOR_CLASS_THEOREM). PR #4 is still `DRAFT`. PR #3 (`integrate/manuscript-v2`) is independent. **Nothing has left the repository.** The cost of being wrong today is a documented retraction inside one roadmap file plus one draft PR — cheap. It becomes expensive only after PR #4 merges or the standalone note is issued.
  - The seal, the reserved seed band and P5.2/WP7 are untouched by any EF-4 outcome (:1751-1753); no simulation or seed is involved in this line.

- **What would have to be true:** (i) that `interval_count_matrix` counts the *closed* rank rectangle, consistent with (EF3.6) at `:1071` — I read the surrounding prose but did not read the function body; (ii) that the event `S` in EF-3's (EF3.9) is literally `STATE_UNIQUE` for `MIN_COVERAGE_LEX`, the same `S` as in EF-4 — the two sections use the same symbol and the same frozen selector, and `tests/test_p1a_entropia_fibras_ef3.py:63` uses `comparison.STATE_UNIQUE`, which is consistent; (iii) that the EF-3 Azuma/hypergeometric tail at `:1039-1049` is correct, since (EF4.6) reuses it verbatim with `N` in place of `n`; (iv) that the geometric trichotomy at `:1296-1339` really is exhaustive — this is the single point on which my whole "composition holds" verdict is contingent, and it is owned by another role.

- **What you could not determine:** (a) whether the trichotomy is exhaustive at parameters in the asymptotic regime — the only test that touches it is vacuous, and closing this would need the same exhaustive sweep at `n >= 10*rho+2` (e.g. `n=24, rho=2`, or `n=44, rho=4`), which is combinatorially cheap and would be **decisive**, but is forbidden here (no file edits, no new construction); (b) whether case (3)'s claim that the losing block has at most three prescribed points is tight, since it is prose-only; (c) whether `Pr_n(S) > 0` for the finitely many `n < n_0` — irrelevant to `o(n)` but relevant if anyone quotes (EF4.19) as a finite-`n` statement; (d) the exact `n_0` above which (EF4.14) holds — the verifier brackets it in `(10^6, 10^7]` but the proof never exhibits it, and :1501-1503 correctly declines to lean on the threshold.

- **Recommendation:** **PROCEED WITH CONDITIONS.** The inference chain composes correctly — I could not break the conditioning at any of the eight junctions, and the (EF4.16), (EF4.11)/(EF4.12), (EF4.6) and (EF3.9)-insertion arithmetic all re-derive — but the token `EF4_Q2_ASYMPTOTIC = Q2_TO_ZERO_PROVED` currently has **zero** executable backing and the sole test guarding (EF4.15)'s geometric core is vacuously satisfied, so the tokens should be qualified (e.g. `PROVED_DEDUCTIVE_NO_EXECUTABLE_BACKING`) and the vacuity of `test_geometric_trichotomy_exhausts_all_abstract_n12_chains` recorded in the roadmap before PR #4 leaves draft.

## 5. Falsifier attack

### Falsifier attack

**Concrete failure modes**

1. **Test `tests/test_p1a_entropia_fibras_ef4.py:63` is vacuous — confirmed independently, and worse than wave 1 reported.** I re-derived the bound from scratch rather than trusting either blind role. For any two disjoint free-row intervals with `a+b<=m` free rows and disjoint free-column intervals with `c+d<=m` free columns (`m=free_count`), `max(min(ac,bd))=(m/2)^2` — proved by the substitution `a=m/2+x,b=m/2-x,c=m/2+y,d=m/2-y`, which forces `ac=bd` only at `x=-y`, giving `ac=bd=(m/2)^2-x^2<=(m/2)^2`. Hence `min(f_-,f_+)<=1/4` **for every rival, for every `free_count`**, not just at `n=12`. Verified numerically:
```
n=12 rho=2: free_count=6  threshold=0.458333  max_min_ratio=0.25  vacuous=True
n=22 rho=2: free_count=16 threshold=0.25       max_min_ratio=0.25  vacuous=True (tie via <=)
n=24 rho=2: free_count=18 threshold=0.236111   max_min_ratio=0.25  vacuous=False (first size where it could bite)
```
So the engineer's `n>=22` estimate is off by one usable step — `n=22` is *still* fully vacuous because the threshold exactly equals the structural cap (`<=` in the code, `tests/test_p1a_entropia_fibras_ef4.py:121`), and `n=24` is the earliest size that could be informative. **Stronger finding than either blind role stated**: because `small_product` is *unconditionally* true whenever the threshold `>=1/4`, and the assert at `:154` is a bare `or`, the other two disjuncts (`fixed_inner`, `loss_case`, `p1a_entropia_fibras_ef4.py`-mirrored logic at `:116-153`) are **never evaluated for truth-relevance** — a bug in `loss_case`'s `<=3` / `<=rho+2` caps, in `past_crosses`/`future_crosses`, or in the stair-range definitions would not be caught by this test at any n where it currently runs. The test certifies literally nothing about EF-4.3's case logic; it only certifies that the threshold formula was transcribed correctly.

2. **The claimed threshold `n0≈1,474,934` is not the asymptotic `n0` the doc's own claim (EF4.14) requires — it's just "first crossing found."** I reproduced it exactly by calling `certificate_bounds` directly:
```
first pass in window: n=1474934, uniqueness_margin_positive=True, loss_gap/2eta=1.0000031
last fail in window:  n=1475204, loss_gap/2eta=0.9999998
60 failing even n occur strictly after the first pass, within a 300-wide window
```
This confirms the margin analyst's number to the digit. But note the margin at the *reported* n0 is `1.0000031` — indistinguishable from exactly 1 at float precision. `EF4.14` as stated in the doc (`docs/hoja_de_ruta_agosto_2026.md:1403-1411`, "para todo `n` par suficientemente grande") is compatible with jitter continuing arbitrarily far out; it does not assert monotonicity, and nowhere in the doc is `n0` recorded or a monotonicity claim made. I spot-checked (not exhaustively) `1,475,206`–`1,600,000` (dense, step 2) and found zero further failures, but this is a sample, not a proof — the `ceil()` in `rho_for_n` produces jumps roughly every `O(n^{1/3})` scale change, and nothing in the repo proves no later jump recreates a tie. **The "first n0" the margin analyst reports is not the quantity EF4.14 needs; the true eventual-monotone threshold has never been established by anyone, including me.**

3. **The repair of committee 050's Prop. 13.12 Case-2 bug is real, but its epistemic labeling directly violates comité 050's explicit condition.** I reconstructed comité 050's counterexample (`n=4000, rho=320, b=(1680,3999)`) against the *current* `EF4.10`–`EF4.12` machinery: the losing (past) block's true free product is `f_-≈0.5`, and via `EF4.7`'s Cauchy–Schwarz the complementary block is correctly capped at `(1-√0.5)^2≈0.086`, giving a rival bound `≈610` against a planted mean `≈1160.5` — correctly dominated. The old bug (assigning `u·v<=1/4` to the *staircase-losing* block instead of the *minimising* block) is genuinely gone; `EF4.7`'s envelope optimum matches a brute-force grid search to 4 decimal places (`1009.575611` vs `1009.576013`). **But**: committee 050's explicit ruling (`docs/comite/comite_decision_050_...md:496-497`) was "**Must not be labelled `PROVED`** — the falsifier is the author of the repair and explicitly declines to have it entered on its say-so," and R1 (`:485`) mandated `MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO` be **retained** with a pointer to that brief. The current doc has:
```
docs/hoja_de_ruta_agosto_2026.md:1506  EF4_CORRECTED_PRESCRIBED_FAMILY = PROVED
```
and `MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED` does not appear anywhere in `docs/hoja_de_ruta_agosto_2026.md` (`grep` returned nothing) — the token was not carried forward and downgraded/annotated as ordered, it was **silently dropped**, while the underlying claim was promoted straight to `PROVED`. There is no committee after 050 (`docs/comite/` ends at `comite_decision_050`) that re-authorizes this upgrade. This is not a math bug — it is the exact procedural failure mode comité 050 pre-empted, recurring verbatim: **the same reasoning lineage both wrote the repair and declared it proved**, with the prior committee's guardrail against exactly that removed rather than satisfied.

4. **Numerical divergence between comité 050's own falsifier-verified repair and the currently committed one, unchecked by any wave-1 role.** Comité 050's minimal falsification test (`:512-518`) reports, for its repaired formula, `gap/(2η_n) = 0.152 → 0.186` at `n=2000,4000,8000,16000`. Running the *current* committed `certificate_bounds` at the same `n`:
```
n=2000  loss_gap/2eta=0.388  n=4000  loss_gap/2eta=0.427
n=8000  loss_gap/2eta=0.469  n=16000 loss_gap/2eta=0.516
```
Same qualitative shape (rising, `<1`), but **not numerically the same repair** — roughly 2-2.5x higher at each `n`. Either `rho_n`, the `eta_n` constant (the "3" in `discrepancy_radius=sqrt(3·free_count·log n)`), or some other parameter differs between comité 050's falsifier-verified sketch and what's now embedded in EF-4, and no wave-1 brief checked this cross-session consistency. This is a new finding, not previously raised.

**Unanchored claims**

- Rival-classification prover's "I reconstructed a complete case split by hand and every branch lands in (1), (2) or (3)" — self-declared as hand reconstruction, explicitly not an oracle; the prover itself flags this. Not independently machine-checked by me either (the only oracle, `:63`, is vacuous, confirmed above).
- Margin analyst's implicit framing of `n=1,474,934` as "the" threshold — my own reproduction shows it is only the *first* crossing in a non-monotone region, not a proven permanent one (see failure mode 2).
- Engineer's `n>=10*rho+2` (i.e. `n>=22`) as the non-vacuity boundary — corrected above to `n=24` by direct computation; `n=22` remains exactly vacuous due to the tie at threshold `=1/4`.

**Assumption attacks**

- "What would have to be true" #1 shared by rival-classification prover and selector analyst — "the trichotomy really exhausts all of `Q_3\{q_0}`" — is the single point every other brief's clearance is conditioned on, and it rests on prose (`:1307-1339`) plus one vacuous test. This is the load-bearing unchecked assumption across the whole dossier.
- Selector analyst's own admission (#3): "`X_-=X_+` exactly — load-bearing FOR ME too... if the planted sides were unequal, a case-(1) rival shaving the larger side would TIE." I did not find a flaw in `X_-=X_+` (it is an integer-arithmetic identity of `build_even_prescription`, `test_prescription_leaves_exactly_half_the_residual_on_each_side` passes at 3 checkpoints), but note it is checked at only 3 hardcoded `n` (`:27-32`), not proved as an identity in code for all valid `n`, mirroring exactly the class of gap ("deterministic identity checked only at finitely many points, then treated as universal") that comité 050 found broken in the *old* Lemma 13.4.
- Margin analyst's "no hidden 4η" claim assumes the current `EF4.7`/`EF4.14` formulation is final; given the unexplained numeric divergence from comité 050's own repair (finding 4 above), this assumption is unverified — a different `eta_n` constant elsewhere in the lineage already moved the crossing by 2-2.5x once.

**Constraint violations**

- **The clearest one**: `EF4_CORRECTED_PRESCRIBED_FAMILY = PROVED` (`docs/hoja_de_ruta_agosto_2026.md:1506`) directly contradicts committee 050's explicit, binding instruction that this exact repair "must not be labelled PROVED" and that `MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO` be retained (`docs/comite/comite_decision_050_...md:485,496-497`). No later committee lifts this condition. This is a silent conversion of an explicitly-conditional SKETCH into an unconditioned PROVED — the sharpest instance of "post-hoc relaxation" the dossier asked me to look for.
- Wave-1's four briefs each independently found sub-issues (vacuity, threshold, wording, prose-only steps) but none cross-checked the current doc against comité 050's own R1 label table — a real, anchored gap in the wave-1 process itself, not a re-hash of any single brief's finding.

**Irreversibility / blast radius**

Matches the engineer's brief: nothing has left the repository (`git status` clean, PR #4 still DRAFT, `manuscript_limits_draft.md` uncontaminated — I did not re-verify the grep but have no reason to doubt it, not independently re-run this session). The cost of being wrong today is a documented retraction inside one roadmap file. The cost of *not* fixing the `PROVED` label before PR #4 merges is that a claim explicitly forbidden from carrying that label by the most recent adjudicating committee on this exact certificate ships as PROVED — that is the concrete, near-term, avoidable irreversibility. Who absorbs it: whoever reads EF4_CORRECTED_PRESCRIBED_FAMILY=PROVED downstream (EF-7 layer 3, SELECTOR_CLASS_THEOREM) without re-reading comité 050.

**Independent-verification gate**

Yes, on the sharpest finding: the author of the EF-4.4 repair (same reasoning lineage that wrote comité 050's falsifier repair sketch) is also the author of the `PROVED` label now attached to it, exactly the configuration comité 050 pre-emptively forbade ("the falsifier is the author of the repair and explicitly declines to have it entered on its say-so"). No independent audit of the promotion is on record.

**Correlated-error check**

All four wave-1 briefs converge on "PROCEED WITH CONDITIONS" and each independently flags real issues (vacuity, threshold, wording, prose-only steps) — but none of them consulted committee 050's explicit label instructions as a binding constraint on the *current* document; they treated 050 only as "prior art to compare margins against," not as a standing procedural order still in force. That is a shared blind spot inherited from the framing given to all four ("attack the math"), not evidence that the labeling violation doesn't matter.

**Minimal falsification test**

For the vacuity of `:63` (worst uncontrolled failure mode): run the identical trichotomy-exhaustiveness enumeration at `n=24, rho=2` (smallest size where `threshold=0.2361<0.25=max_min_ratio`, so `small_product` can be false and `fixed_inner`/`loss_case` are finally exercised). Concrete predicate: if any of the `C(24,4)^2≈1.13e8` tuples trips `small_product=False` and also fails both `fixed_inner` and `loss_case`, the trichotomy is falsified at finite n. **This requires enlarging `n` in the test, which the PI has forbidden this session — I specify it, I do not run it.**

For the labeling violation (no test needed): already executed — `grep -n "EF4_CORRECTED_PRESCRIBED_FAMILY" docs/hoja_de_ruta_agosto_2026.md` → `PROVED`, and `grep -n "MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED" docs/hoja_de_ruta_agosto_2026.md` → no output. This alone is decisive against the *label*, independent of whether the underlying math is correct.

**Attacks I could not make executable**

- Whether `EF-4.3`'s case (1) "`b=(s+1,s+1)` es idéntico" (`:1338-1339`) genuinely mirrors the `b=(s,s)` analysis, as the rival-classification prover disputes — I could not construct an executable discriminator without enumerating rivals at the forbidden larger `n`. INCONCLUSIVE.
- Whether the numeric divergence between comité 050's falsifier margins (`0.152→0.186`) and the current code's margins (`0.388→0.516`) at the same `n` reflects an intentional, documented re-parametrization or an unlogged drift — I found no doc text explaining the discrepancy; settling it requires locating the exact `C, L` (or equivalent) comité 050's falsifier used, which is not in `docs/hoja_de_ruta_agosto_2026.md`. INCONCLUSIVE, logged as an open provenance gap rather than a refutation.
- Whether further jitter recurs beyond `n=1.6e6` (the doc's asymptotic claim is compatible with it) — my scan was a spot check, not exhaustive; I cannot rule it out without a much wider dense sweep, which is expensive but not forbidden (it doesn't enlarge the vacuous combinatorial test's n) — time did not permit it here. INCONCLUSIVE.

## 6. Commitment warden verdict

### Commitment warden verdict

- **Verdict: BLOCK**

- **Commitments on record:**
  - `docs/program_reopening_note_2026-07-31.md:83` (§6.1): "Perímetro fijo: R1 y R2. Nada entra sin una nueva nota firmada."
  - `docs/program_reopening_note_2026-07-31.md:77-79` (§5): R2 has its own two-week cap; unresolved → "se marca abierto y se pasa a R1 sin discusión."
  - `docs/program_reopening_note_2026-08-05_R3.md:14-18`: reaffirms §6.1 is binding — anything outside R1/R2/R3 "queda como hallazgo fuera de perímetro," destined to `docs/backlog_hallazgos.md`, absent a new signed note.
  - `docs/program_reopening_note_2026-08-09_P5_2.md:53-58` (§3) + `:103` (firma): "El manuscript `docs/manuscript_limits_draft.md` no se toca" / `MANUSCRIPT_LIMITS: NO TOCAR`; "no se trabaja en paralelo sobre... dimensión superior"; "Un solo fichero científico modificado durante P5.2"; publication/integration decisions require a later, separate authorization (`:89-90`).
  - `docs/hoja_de_ruta_agosto_2026.md:1652-1670` (§8, self-declared negative scope): excludes `d>=3`, "modificaciones de WP7, del manuscrito de límites o de resultados sellados," new selectors/observables chosen after seeing results, absolute-novelty/priority language.
  - `docs/program_closure_note_2026-07-30.md:122-137` (§Alcance, still in force in every later note): "reconstrucción de horizonte en cualquier reformulación" stays closed; clause 2 bans absolute-novelty claims.

- **Perimeter authorisation for EF-0..EF-8: NONE.** I read all three signed notes in full (`program_reopening_note_2026-07-31.md`, `_2026-08-05_R3.md`, `_2026-08-09_P5_2.md`). Each names a closed list of authorised items (R1+R2; R3; P5.2 respectively) and each carries an explicit `## Firma` block with `FIRMADA_POR: Ignacio (PI)` and `AUTORISED_SCOPE`. `docs/hoja_de_ruta_agosto_2026.md` — the document that opens EF-0..EF-8 — has **no such block anywhere in its 1753 lines** (`grep -n "FIRMA\|SIGNED\|PI:"` returns nothing). It asserts its own legitimacy in prose (`:16-19`, "amplía de forma acotada el perímetro... no revoca... no reabre reconstrucción") but this is exactly the self-certifying move that R3's own note (`:14-18`) says is insufficient: "Sin esta nota firmada, ese work package queda como hallazgo fuera de perímetro." Nothing in the fiber-entropy line — a new, independent target (`Z_n`, `COUNT_VOLUME` identifiability in `emergencia/`) that is none of R1, R2, R3 or P5.2's closed lists — is covered by any signed authorisation on record.

- **R2 box status: expired, unresolved, and not honoured as specified.** Cap = 2026-08-14 (`program_reopening_note_2026-07-31.md:78`, reaffirmed unchanged in `_R3.md:104`). Today = 2026-08-15. Last substantive R2 work is `git log dev/R2_lambda6_derivation_NOTES.md` → single commit `91a84ac`, 2026-07-31 ("R2 day 1"), file itself: `PREFACTOR = OPEN / [UNVERIFIED]`. No later commits. The required consequence of the box lapsing — "se marca abierto y se pasa a R1 sin discusión" — has not happened: `grep -n "R2" docs/manuscript_limits_draft.md` returns **nothing**; R1 does not even mention R2 as open. Meanwhile all visible effort since 2026-08-11 went into the unauthorised EF line. This is silent lapse, not honoured closure.

- **Pre-commitment status: honoured for §9, but irrelevant given §1 fails.** `git log -p docs/hoja_de_ruta_agosto_2026.md` shows §9 ("cierre fuerte"/"cierre honesto") was written verbatim in the first commit `adc391d` (2026-08-11 21:52:59), when the file contained only EF-0 through EF-2 — EF-4 did not exist yet (it first appears in `326fee3`, 2026-08-15 19:54). `git diff` across all three commits shows §9's text is byte-identical throughout — the criterion was not adjusted to fit EF-4's later result. Good discipline internally, but it cannot rescue a criterion operating inside an unauthorised perimeter (finding 1).

- **Reversibility classification:**
  - Reversible / not yet happened: `gh pr view 4` → `OPEN, DRAFT`; `main` is 59 commits behind (`e42fbc6`) and untouched; `make verify-seal` matches the recorded hash `6e2c38...bfefd4`; no evidence of virgin-seed-band `[2,000,000–2,999,999]` extraction; the EF-6 "standalone technical note" (`emergencia/P1a_entropia_fibras_ef6_auditoria_bibliografica.md`) exists only as an in-repo draft file, not issued externally.
  - **Already one-way / already happened on the working branch:** commit `326fee3d` (2026-08-15 19:54:28, `research/f2-f3-chain-distance`) edits `docs/manuscript_limits_draft.md` — verified by `git diff`, a substantive new paragraph on Madsen/Braun/F2-F3 comparison — directly against P5.2's "no se toca" / `MANUSCRIPT_LIMITS: NO TOCAR`. Commit `8139092` (2026-08-11 11:49:18) edits `research_program/work_packages/wp7_f2_f3_product_order_contract.md` itself, changing `ESTADO` to "EXTENSIÓN PROBADA PARA TODO d>=2" and adding a d=3/d=4 (2+1, 3+1) counterexample theorem — directly against P5.2's "ni dimensión superior" and the roadmap's own §8 `d>=3` exclusion. Both are committed history now, even though unmerged into `main`; reverting them is possible but the breach of the "no touch" commitment has already occurred, which is the discipline this role guards.

- **Scope: fails on two concrete §8 items.**
  1. `d>=3` — violated by commit `8139092`, which modifies the WP7 terminal file to cover d≥2 generally, including 2+1 and 3+1.
  2. "modificaciones de WP7... del manuscrito de límites" — violated by commits `8139092` and `326fee3` respectively, both against the roadmap's own text.
  3. `MIN_COVERAGE_LEX` — EF-4's uniqueness step (`docs/hoja_de_ruta_agosto_2026.md:1417`) proves uniqueness under `MIN_ONLY` and infers lex-uniqueness from a strict first-component gap; `emergencia/P1a_contrato_comparacion_selectores_balanceados_d2.md:56-58` freezes `MIN_COVERAGE_LEX` as "un selector distinto, no un desempate aplicado después de ejecutar MIN_ONLY." Whether the logical inference is valid is a mathematical question outside my role, but routing the uniqueness argument through `MIN_ONLY` at all is a scope-adjacent move flagged by wave 1 that I could not clear; `[PLAUSIBLE, not adjudicated]`.
  4. Absolute-priority language: not violated — `EF6_PRIORITY_STATUS: PRIORITY_NOT_CERTIFIED` is held consistently at `:1573` and `:1745`.

- **Reporting symmetry: fails.** I independently ran the suite (`.venv/bin/python -m pytest`) and re-executed the trichotomy tuple loop by hand. Confirmed: `test_fixed_margins_enter_the_proved_asymptotic_regime` (`tests/test_p1a_entropia_fibras_ef4.py:162-167`) literally asserts `not early.uniqueness_margin_positive` at n=100,000 and `late.uniqueness_margin_positive` only at n=10,000,000 — a machine-certified failure at n=1e5. In the text, this is reported as a downgraded "control no vinculante" aside (`docs/hoja_de_ruta_agosto_2026.md:1498-1502`) immediately before the bolded headline `Gate EF-4: PASS` at `:1514`. I also reran the trichotomy exhaustiveness check myself (n=12, ρ=2): `total=245025, small_product_true=245025` — the disjunct `small_product` is true for every single tuple, so the assertion can never exercise `loss_case` or `fixed_inner`; it certifies nothing about exhaustiveness, yet nowhere in the surrounding prose is this vacuity disclosed with anything like the prominence of `PASS`.

- **Forbidden moves present?**
  - **Silent scope widening — CONFIRMED**, twice (manuscript touch, WP7 dimensional extension), both against explicit written "no toca" clauses.
  - **Entry without signed note — CONFIRMED** for the entire EF-0..EF-8 line.
  - **Outcome coercion via prominence asymmetry — CONFIRMED** (PASS headline vs. buried/downgraded finite-n failure and vacuous trichotomy test, independently reproduced above).
  - **Author verifying own claim — PLAUSIBLE, not fully adjudicated** (git commit author `adnacho@gmail.com` matches the PI's own signing identity across the whole EF branch; no independent party signs off the EF-4 `PASS` gate the way a comité would).
  - **Post-hoc relaxation of the done-criterion — not found** (§9 text is unchanged since before EF-4 existed).
  - **Seal / seed tampering — not found** (seal hash matches; no seed-band evidence).

- **Reasons:**
  - `docs/program_reopening_note_2026-07-31.md:83` binds "nada entra sin nueva nota firmada"; `docs/hoja_de_ruta_agosto_2026.md` has no `FIRMA`/`FIRMADA_POR` block anywhere (`grep` empty), unlike all three genuine reopening notes, which invalidates its self-declared authority to open EF-0..EF-8.
  - `docs/program_reopening_note_2026-07-31.md:78` sets R2's cap at 2026-08-14; today is 2026-08-15 and R2 remains unresolved, unmarked-open in R1, with all effort diverted to the unauthorised EF line instead.
  - `docs/program_reopening_note_2026-08-09_P5_2.md:54,103` ("no se toca" / `NO TOCAR`) is contradicted by commit `326fee3d` editing `docs/manuscript_limits_draft.md` on 2026-08-15.
  - `docs/program_reopening_note_2026-08-09_P5_2.md:57` ("ni dimensión superior") and `docs/hoja_de_ruta_agosto_2026.md:1656` (`d>=3` excluded) are both contradicted by commit `8139092` extending the WP7 counterexample to d≥2 including 3+1.
  - `docs/hoja_de_ruta_agosto_2026.md:1514` (`PASS`) is not accompanied by reporting of equal prominence for the machine-verified finite-n failure I reproduced (`tests/test_p1a_entropia_fibras_ef4.py:162-167`) or the vacuous trichotomy test I reproduced (245025/245025).

Given an entire uninitialed research line, two concrete breaches of explicit "do not touch" clauses already committed to the working branch, and an expired, unresolved R2 box while attention was diverted to that unauthorised line, EF-4's `PASS` gate cannot be certified as sitting inside the commitments on record.

## 7. Source verdict

### Source verdict

| Source | Claimed by | Claim it was cited for | Status |
|---|---|---|---|
| `tests/test_p1a_entropia_fibras_ef4.py:63-154` + diagnostic numbers | Chain engineer | n=12 trichotomy test is vacuous: `tuples=245025 small_product_true=245025 max_min_free_product=0.25` vs `threshold=0.458333` | **CONFIRMED** — reproduced exactly (see below) |
| `tests/test_p1a_entropia_fibras_ef4.py:72` | Chain engineer | `threshold = 1/8 + rho/free_count = 0.458333` at n=12 | **CONFIRMED** |
| `tests/test_p1a_entropia_fibras_ef4.py:120-122` | Chain engineer | the `small_product` disjunct | **CONFIRMED** — exact line match |
| `tests/test_p1a_entropia_fibras_ef4.py:154` | Chain engineer | final `assert fixed_inner or small_product or loss_case` | **CONFIRMED** |
| `emergencia/p1a_entropia_fibras_ef4.py::certificate_bounds`, n=1474934 | Margin analyst | certificate first holds (`uniqueness_margin_positive`) at n=1474934 | **CONFIRMED** — False at 1474932, True at 1474934, monotonic from n=100000 up to there |
| same, n=1475204 in [1.46e6,1.50e6] | Margin analyst | last failing even n in that window | **CONFIRMED** — exact match; also reveals non-monotonic flicker between 1474934 and 1475204 not mentioned in the brief |
| `emergencia/p1a_entropia_fibras_ef4.py` main() output | Chain engineer / margin analyst | `LOSS_GAP_OVER_2ETA=0.669836/0.942871/1.34077`, `CERTIFICATE=PREASYMPTOTIC,PREASYMPTOTIC,PASS` | **CONFIRMED** — byte-for-byte on live re-run |
| `emergencia/P1a_contrato_comparacion_selectores_balanceados_d2.md:18-24` | Selector analyst | two-component score `S_lex` | **CONFIRMED** |
| same, `:36-44` | Selector analyst | `Q_3` domain definition | **CONFIRMED** |
| same, `:51-52` | Selector analyst | frozen names `MIN_ONLY`/`MIN_COVERAGE_LEX` | **CONFIRMED** (line drift: `COVERAGE` itself sits at :50, just outside the cited range — minor imprecision, not wrong) |
| same, `:56-58` | Selector analyst | "MIN_COVERAGE_LEX is a distinct selector, not a tiebreak after MIN_ONLY" | **CONFIRMED** — verbatim |
| `emergencia/p1a_enumeracion_simulacion.py:32` | Selector analyst | `K0 = 3` | **CONFIRMED** |
| `emergencia/p1a_comparar_selectores_d2.py:246` | Selector analyst | `eligible = counts >= sealed.K0` | **CONFIRMED** |
| same, `:284-289` | Selector analyst / chain engineer | quadruple-multiplicity count (`minimum_nmax`) | **CONFIRMED** |
| same, `:305-306` | Selector analyst | `outcomes[MIN_ONLY] = ScoreOutcome(...)` | **CONFIRMED** |
| same, `:361-366` | Selector analyst | `outcomes[MIN_COVERAGE_LEX] = ScoreOutcome(...)` | **CONFIRMED** |
| `Makefile:15-17` | Selector analyst | `verify-seal` hashes only `nachocausal/thresholds.py` | **CONFIRMED** |
| — (grep on `nachocausal/thresholds.py`) | Selector analyst | `K0`/`MIN_COVERAGE_LEX` are NOT in the sealed file | **CONFIRMED** — zero matches |
| `git log --oneline -3` on the three selector files | Selector analyst | single commit `0992277` | **CONFIRMED** |
| `git log -S"K0 = 3" --oneline` | Selector analyst | `0992277` only | **CONFIRMED** |
| `grep ... docs/manuscript_limits_draft.md` | Chain engineer | zero EF-4/entropia_fibras hits (no contamination) | **CONFIRMED** — empty, exit 1 |
| `gh pr view 4` | Chain engineer | state OPEN/DRAFT | **CONFIRMED** — `{"state":"OPEN","isDraft":true}` |
| `docs/hoja_de_ruta_agosto_2026.md:1323-1327` | Chain engineer | (EF4.9) tag location | **CONFIRMED** |
| same, `:1362-1370`/`:1372-1376`/`:1384-1389` | Chain engineer | (EF4.11)/(EF4.12)/(EF4.13) tags | **CONFIRMED** (tags at 1365/1374/1388, inside ranges) |
| same, `:1420-1423` | Chain engineer | (EF4.15) tag, `F_n∩G_n⊆S` | **CONFIRMED** |
| same, `:1094-1100`/`:1099` | Chain engineer | (EF3.9) tag | **CONFIRMED** — tag at line 1099 |
| Rival prover "`LHS-RHS=(1-rho)/(4N)`" vs margin analyst "(EF4.9)⟺n≤N+4rho=n+2rho-2" | Rival prover / margin analyst | claimed contradictory forms of (EF4.9) | **CONFIRMED, NOT contradictory** — symbolically re-derived; both are the same relation (with `N=n-2rho-2`) written two ways |
| `docs/comite/comite_decision_050_...md` | Margin analyst / roadmap `:1377-1379` | earlier certificate refuted by committee 050 over margin `rho` vs `rho/2` | **CONFIRMED** — §8/§9: "the true margin is `ρ/2`, not `ρ−1`"; verdict `RECOMMEND_REVISE_AND_RECONVENE` |
| `emergencia/p1a_entropia_fibras_ef4.py:73-80` | Chain engineer | `expected=2*width+2`, collision guard | **CONFIRMED** |
| same, `:52-58` | Chain engineer / selector analyst | `append_incomparable` | **CONFIRMED** |
| same, `:180-184` | Chain engineer | `entropy_log_upper_bound` = `R_n log n` | **CONFIRMED** |
| roadmap `:1140-1148`, `:1152` | Chain engineer | exact `Q_{2,n}` table, "no se extrapola" | **CONFIRMED** ("no se extrapola" actually at line 1151, off by one — trivial drift) |
| roadmap `:1176`, `:1180` | Chain engineer | `EF3_SUBEXPONENTIAL...=PROVED`, `EF3_TERMINAL=OPEN_AFTER_FIBER_AUDIT` | **CONFIRMED** |
| roadmap `:1607`, `:1610` | Chain engineer | `EF7_SELECTOR_CLASS_THEOREM=PROVED`, `EF7_TERMINAL=SELECTOR_CLASS_THEOREM` | **CONFIRMED** |
| roadmap `:1620-1622` | Chain engineer | "layer 3" of the EF-7 three-layer decomposition | **UNCONFIRMED** — layer 3 ("el certificado específico de pertenencia de `MIN_COVERAGE_LEX`...") is actually at `:1596-1597`; `:1620-1622` is the unrelated WP7 motivational analogy |
| roadmap `:5` | Chain engineer | `ESTADO` header | **CONFIRMED** |
| roadmap `:1733`, `:1740-1741` | Chain engineer | §11 status tokens | **CONFIRMED** |
| roadmap `:1039-1049` | Chain engineer | Azuma/Doob-martingale hypergeometric tail | **CONFIRMED** |
| `emergencia/P1a_count_volume_experimento_condicionado_d2.md:40-42` | Rival prover | "rivals are strict 4-chains" | **UNCONFIRMED** — `:40-42` is the Poisson sprinkling law (`(u_i,v_i) iid Uniform`); the 4-chain condition `a≺b≺c≺d` is at `:50`, not `:40-42` |
| `emergencia/p1a_enumeracion_simulacion.py:173-198` | Rival prover | "blocks are closed rectangles" | **CONFIRMED** — docstring: "closed-interval cardinalities … inclusive axis-aligned rectangle" |
| `emergencia/p1a_entropia_fibras_ef4.py:73-76` | Rival prover | "the band is entirely prescribed" | **CONFIRMED** |
| `emergencia/p1a_entropia_fibras_ef4.py:67-68` + "`rho_n<n/4` first holds at n=396" | Rival prover | `ValueError` on `width>=n//4`; first-success n | **CONFIRMED** exactly under the code's own semantics (even n, integer `n//4`); real-division/odd-n scan gives a different (wrong) answer of 385 — the brief's own framing survives only because it matches the code, not casual arithmetic. Also: `build_even_prescription` succeeds at 396, **fails again at 398**, succeeds permanently from 400 — this flicker is not mentioned |
| `tests/test_p1a_entropia_fibras_ef4.py:92-95`, `:154` | Rival prover | `C(12,4)^2=245025` pairs, zip, assertion | **CONFIRMED** |
| n=1e6 four branches `0.131301/0.118699/0.118699/0.131301` vs `tau=0.150206` | Rival prover | exact-count branch values | **No path:line given** — but independently reproduced: `tau` = `small_product_threshold` at n=1e6 exactly; the two branch values equal `1/8 ± rho/(4·free_count)` exactly. Numerically genuine, citation absent |
| `emergencia/p1a_entropia_fibras_ef4.py:118` | Margin analyst | `other_product=(1-sqrt(free_product))**2` bakes in Cauchy–Schwarz | **CONFIRMED** |
| same, `:38-39` | Margin analyst | `2.0 * discrepancy_radius` in both margin checks | **CONFIRMED** |
| same, `:86-94` | Margin analyst | `validate_even_balance` | **CONFIRMED** |
| same, `:138` | Margin analyst | `small_product_threshold` | **CONFIRMED** |
| — | Margin analyst | `certificate_bounds` never checks `free_count%2==0` | **CONFIRMED** — that check lives only in the test (`:31`), not the function |
| — | Margin analyst | `small_product_gap` negative through n=50000, positive at n=1e5 | **CONFIRMED** (−505.75 / +1552.5; claimed −505.8/+1552.5, rounding-level match) |
| — | Margin analyst | `loss_gap/rho = 0.4979/0.4997/0.4999` at n=1e8/1e10/1e12 | **UNCONFIRMED at n=1e8** — computed 0.49856 (rounds to 0.4986), not 0.4979; n=1e10 (0.49967→0.4997) and n=1e12 (0.49992→0.4999) match |
| `tests/test_p1a_entropia_fibras_ef4.py:190` | Margin analyst | `assert 0.45 < ratio < 0.51` | **CONFIRMED** |
| `tests/test_p1a_entropia_fibras_ef4.py:41-60` | Selector analyst | 720 permutations of size 6, all fields checked | **CONFIRMED** |
| `docs/hoja_de_ruta_agosto_2026.md:207` + `P1a_count_volume_experimento_condicionado_d2.md:61` | Selector analyst | master definition of `S` | **CONFIRMED** both |
| roadmap `:1081` | Selector analyst | `p_n=Pr_n(S)` introduced | **CONFIRMED** |
| President's session facts (HEAD, `git status`, `pytest -q`, `make verify-seal`) | President | reproducibility of the session state | **CONFIRMED** — all four re-run bit-for-bit |

- **Reproduced numbers:**
  - Vacuity diagnostic: claimed `tuples=245025 small_product_true=245025 max_min_free_product=0.25 threshold=0.458333` → got exactly the same, plus `none_true=0` and `only_small_product=28339` (small_product is the sole surviving disjunct 28339/245025 times, but never the only *possible* true one is required — it is true in **100%** of cases, which is what makes the assert vacuous). **Match, fully confirmed.**
  - Margin threshold: claimed n=1474934 first holds, n=1475204 last failing in [1.46e6,1.50e6] → both exact. `loss/2eta` = 0.6698/0.9429/1.3408 at 1e5/1e6/1e7 → exact (0.669836/0.942871/1.34077). **Match.**
  - `small_product_gap`: claimed −505.8 / +1552.5 at n=50000/1e5 → got −505.75 / +1552.5. **Match** (rounding).
  - `loss_gap/rho`: claimed 0.4979/0.4997/0.4999 at 1e8/1e10/1e12 → got 0.49856/0.49967/0.49992. **Mismatch at n=1e8** (0.4979 vs 0.4986); 1e10 and 1e12 match.
  - Four-branch numbers at n=1e6: claimed 0.131301/0.118699/0.118699/0.131301, tau=0.150206 → got tau (=small_product_threshold) = 0.150205723…, and `1/8 ± rho/(4·free_count) = 0.1313014/0.1186986`. **Match**, though uncited.
  - `rho_n<n/4` first-success n: claimed 396 → confirmed 396 exactly under the code's real constraints (even n, `n//4`), but the construction flickers (398 fails again) before permanently stabilizing at 400 — not disclosed in the brief.
  - EF4.9 algebra: `LHS−RHS=(n−4ρ−N)/(8N)`; substituting `N=n−2ρ−2` gives both `(1−ρ)/(4N)` (rival prover) and the equivalent inequality `n≤N+4ρ=n+2ρ−2` (margin analyst) — **symbolically identical, not a contradiction.**

- **Unsupported claims:**
  - Chain engineer's "layer 3 described at `:1620-1622`" — that span is the WP7 motivational analogy, unrelated to the three-layer EF-7 decomposition (actually at `:1589-1597`).
  - Rival prover's "rivals are strict 4-chains per `:40-42`" — those lines define the sprinkling law, not the chain condition (which is at `:50`).
  - Margin analyst's `loss_gap/rho=0.4979` at n=1e8 does not match the live computation (0.4986); the other two values in the same triple do match, so this looks like an isolated slip rather than a systematic error, but it is a real numeric discrepancy in a brief whose entire value proposition is "trust these ratios."

- **Uncited substantive claims:**
  - Rival prover's n=1e6 four-branch numbers (0.131301/0.118699/0.118699/0.131301, tau=0.150206) carry no `path:line` at all in the brief summary, despite being load-bearing evidence for "the trichotomy is not close" at large n. They are numerically genuine (independently reproduced), but as delivered they are unverifiable without reverse-engineering the formula.

- **Notes:**
  - No sources were unlocatable; all cited files/paths exist. The only line drift found (aside from the layer-3 and the 4-chain miscitations above) is trivial (±1 line on "no se extrapola" and on the EF4.11/12/13 tag ranges, which include a line or two of surrounding prose but still contain the cited tag).
  - The most consequential finding for the decision question: the n=12 finite-n "trichotomy" test (`tests/test_p1a_entropia_fibras_ef4.py:63-154`) is genuinely vacuous — `small_product` is true for all 245025 tuples because `max_min_free_product (0.25) < threshold (0.458333)` by a wide margin, so the test never actually exercises `fixed_inner` or `loss_case`. This does not touch the deductive asymptotic proof of (EF4.15) in `docs/hoja_de_ruta_agosto_2026.md` (which is presented as a proof, not a computed check), but it means the codebase currently offers **no non-vacuous finite-n corroboration** of the trichotomy structure underlying EF4.15, which is precisely the kind of gap committee 050 flagged in the sibling §13 certificate (a `PROVED` label resting on an untested case split). The EF-4 chain does explicitly incorporate the `ρ/2` correction that committee 050 forced onto the earlier certificate (roadmap `:1377-1379`, EF4.12), so that specific historical failure mode has been addressed — but the vacuous test means the current combinatorial case-split (Lemma-13.11-analogue) is unverified computationally, only asserted deductively.

## 8. Claim ledger

Estado exactamente uno de `PROPOSED`, `VERIFIED`, `REFUTED`, `INCONCLUSIVE`. `VERIFIED` exige
oráculo fuera de la capa de lenguaje; el acuerdo entre agentes nunca basta.

| ID | Claim | Status | Evidence | What set the status |
| --- | --- | --- | --- | --- |
| C1 | La tricotomía de EF-4.3 es exhaustiva sobre todo `Q_3\{q_0}` | INCONCLUSIVE | prosa `:1307-1339`; única prueba ejecutable vacía | Prover la reconstruyó a mano y no pudo falsarla, pero declara que una reconstrucción a mano no es oráculo; el falsificador tampoco la rompió ni pudo hacerlo ejecutable |
| C2 | El test `tests/test_p1a_entropia_fibras_ef4.py:63-154` es vacuo: no certifica nada sobre la tricotomía | VERIFIED | `tuples=245025 small_product_true=245025 max_min_free_product=0.25` vs `threshold=0.458333` | Reproducido de forma independiente por cuatro roles (chain engineer, falsificador, verificador de fuentes, guardián); el falsificador además probó `min(f_-,f_+)<=1/4` para todo `free_count`, generalizando la vacuidad |
| C3 | El primer tamaño donde ese test podría morder es `n=24`, no `n=22` | VERIFIED | `n=22: threshold=0.25 = max_min_ratio → vacuo por el `<=` en `:121`; n=24: threshold=0.236111` | El falsificador corrigió la estimación del chain engineer por cómputo directo |
| C4 | La aritmética de márgenes de EF-4.4 es correcta y cierra a exactamente `2η` sin holgura | VERIFIED | envolvente vs búsqueda bruta `1009.575611` vs `1009.576013`; ratios reproducidos por el verificador byte a byte | Margin analyst re-derivó las seis identidades; el falsificador reprodujo la envolvente por fuerza bruta; el verificador confirmó los números |
| C5 | El objeto maximizado es el `MIN_COVERAGE_LEX` congelado y `S` significa lo mismo en EF3.9/EF4.15/EF4.16/EF4.18 | VERIFIED | `P1a_contrato_...:18-24,:36-44,:51-52,:56-58`; `p1a_comparar_selectores_d2.py:246,:284-289,:305-306,:361-366`; `p1a_enumeracion_simulacion.py:32` | Selector analyst lo ancló sitio por sitio; el verificador abrió cada cita y las confirmó todas |
| C6 | La transferencia par→impar (EF4.17)-(EF4.18) preserva candidatos, empates y ganador | VERIFIED | argumento de incomparabilidad + `tests/...ef4.py:41-60` sobre las 720 permutaciones de `S_6` | Selector analyst lo probó analíticamente; el verificador confirmó el test |
| C7 | La composición condicional (EF4.3)→(EF4.6)→(EF4.15)→(EF4.16)→(EF4.18)→(EF4.19)→(EF3.9)→(EF4.20) es sólida | VERIFIED | ocho junturas re-derivadas; `2n^4 n^-6 = 2n^-2`; `log((n)_{R_n}) <= R_n log n` | Chain engineer no pudo romper ninguna juntura; nadie en la ola 2 la atacó con éxito |
| C8 | (EF4.15) `F_n ∩ G_n ⊆ S` es válida | INCONCLUSIVE | depende enteramente de C1 | Todo el clearance de C4, C5 y C7 está condicionado a C1, que sigue sin oráculo |
| C9 | `Q_{2,n} → 0` (EF4.20) está probado | INCONCLUSIVE | depende de C8; `EF4_Q2_ASYMPTOTIC = Q2_TO_ZERO_PROVED` tiene **cero** respaldo ejecutable | Chain engineer: ningún test evalúa `Pr_n(S)` ni exhibe una sola permutación en `F_n ∩ G_n` |
| C10 | El certificado falla en `n=1e5` y `n=1e6` y sólo pasa en `n=1e7`; el primer cruce está en `n=1474934` con jitter hasta `n=1475204` | VERIFIED | `LOSS_GAP_OVER_2ETA = 0.669836 / 0.942871 / 1.34077`; `CERTIFICATE=PREASYMPTOTIC,PREASYMPTOTIC,PASS` | Margin analyst lo midió; verificador y falsificador lo reprodujeron exactamente; el propio `tests/...ef4.py:162` lo asserta |
| C11 | El `n0` que (EF4.14) necesita (monotonía eventual) no lo ha establecido nadie | VERIFIED | margen en el primer cruce = `1.0000031`; 60 `n` pares fallan *después* del primer cruce | Falsificador: el "primer cruce" no es la cantidad que el enunciado requiere |
| C12 | `EF4_CORRECTED_PRESCRIBED_FAMILY = PROVED` viola una orden vigente del comité 050 | VERIFIED | `comite_050:485` ("`MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO` retained"), `:325` ("Do not let my AM-GM repair enter the manuscript as `PROVED` on my say-so"); `grep -c` del token en la hoja → `0`; `:1506` → `PROVED` | Falsificador lo encontró; **el presidente lo verificó de primera mano** |
| C13 | La reparación material que el comité 050 exigió (margen `ρ/2`, no `ρ`) sí está incorporada | VERIFIED | `:1377-1379`, (EF4.12); contraejemplo de 050 (`n=4000, ρ=320`) reconstruido y correctamente dominado | Falsificador lo reconstruyó; verificador confirmó qué refutó 050 |
| C14 | La línea EF-0..EF-8 no está autorizada por ninguna nota firmada | VERIFIED | `grep -niE 'firmada_por\|autorised_scope' docs/hoja_de_ruta_agosto_2026.md` → sin resultados; las tres notas sí los llevan (`_R3.md:96,98`; `_P5_2.md:97,99`); `nota 07-31:83` "Nada entra sin una nueva nota firmada" | Guardián lo dictaminó; **el presidente lo verificó de primera mano** |
| C15 | `docs/manuscript_limits_draft.md` fue modificado contra `MANUSCRIPT_LIMITS: NO TOCAR` | VERIFIED | `git show --stat 326fee3 -- docs/manuscript_limits_draft.md` → `17 insertions(+), 3 deletions(-)`; `_P5_2.md:54,:103` | Guardián lo dictaminó; **el presidente lo verificó de primera mano** |
| C16 | Ese mismo manuscrito NO está contaminado por EF-4 | VERIFIED | `grep -c 'EF-4\|EF4\|FIBER_CONCENTRATION' docs/manuscript_limits_draft.md` → `0` | Chain engineer lo afirmó, verificador lo confirmó, presidente lo re-ejecutó. **No contradice C15**: el manuscrito fue tocado, pero no por EF-4 |
| C17 | WP7 fue extendido a `d>=2` contra §8 y contra P5.2 | VERIFIED | `wp7_f2_f3_product_order_contract.md:4` → `EXTENSIÓN PROBADA PARA TODO d>=2`; commit `8139092` añade `wp7_f2_f3_higher_dimensional_extension.md` (463 líneas) y siete ficheros en `posters/`; `_P5_2.md:58`, roadmap `:1656` | Guardián lo dictaminó; **el presidente lo verificó de primera mano** |
| C18 | La caja dura de R2 venció el 2026-08-14 sin resolverse y sin ejecutar §4.4 | VERIFIED | `nota 07-31:78`; `git log dev/R2_lambda6_derivation_NOTES.md` → único commit `91a84ac` (2026-07-31), `PREFACTOR = OPEN` | Guardián lo verificó por comando; el presidente confirmó `:78` |
| C19 | El sello no cubre el selector (`K0`, `MIN_COVERAGE_LEX`) | VERIFIED | `Makefile:15-17` hashea sólo `nachocausal/thresholds.py`; grep del token en el fichero sellado → 0 coincidencias | Selector analyst lo detectó; verificador lo confirmó |
| C20 | El criterio de terminado §9 se fijó antes de que EF-4 existiera | VERIFIED | `git log -p`: §9 escrito en `adc391d` (2026-08-11), EF-4 aparece en `326fee3` (2026-08-15); texto byte-idéntico | Guardián lo verificó; es el único punto de disciplina que la hoja sí honra |
| C21 | `loss_gap/rho = 0.4979` en `n=1e8` | REFUTED | valor real `0.49856` | Verificador de fuentes re-ejecutó el cómputo; los otros dos valores del mismo triple sí coinciden |
| C22 | La "layer 3" de EF-7 está descrita en `:1620-1622` | REFUTED | está en `:1589-1597`; `:1620-1622` es la analogía motivacional de WP7 | Verificador de fuentes abrió el rango citado |
| C23 | La condición de 4-cadena estricta está en `P1a_count_volume_experimento_condicionado_d2.md:40-42` | REFUTED | está en `:50`; `:40-42` es la ley de sprinkling de Poisson | Verificador de fuentes abrió el rango citado |
| C24 | Los márgenes del comité 050 (`0.152→0.186`) y los del código actual (`0.388→0.516`) a igual `n` divergen 2-2.5× sin explicación documentada | INCONCLUSIVE | comparación ejecutada por el falsificador; ningún texto explica la diferencia | El falsificador no pudo determinar si es reparametrización intencional o deriva no registrada |

## 9. Synthesis

**Dirección recomendada: `REVISE_AND_RECONVENE`.** El veredicto no puede ser un PROCEED: el
guardián de compromisos emitió `BLOCK` y el foro no resuelve por mayoría.

Hay que separar dos capas que el documento actual mezcla, porque el resultado del foro es distinto
en cada una.

**La matemática sobrevivió el ataque.** Nadie —cuatro expertos ciegos más un falsificador con
mandato explícito de romperla— consiguió falsar (EF4.15). Más aún, tres piezas quedaron
*verificadas* con oráculo, no sólo sin refutar: la aritmética de márgenes de EF-4.4 (C4), la
identidad del selector y del evento `S` (C5, C6) y la composición condicional completa de ocho
junturas (C7). La reparación material que el comité 050 exigió está genuinamente incorporada
(C13). Los cuatro ataques asignados al analista de márgenes fallaron por razones precisas, y el
falsificador reconstruyó el contraejemplo de 050 contra la maquinaria actual y lo vio correctamente
dominado.

**Pero el certificado no está probado, y la etiqueta que lleva está prohibida.** Dos cosas
distintas:

1. *Epistémico.* (EF4.15) descansa en C1 —la exhaustividad de la tricotomía— que sigue
   `INCONCLUSIVE`: prosa más una reconstrucción a mano que su propio autor declara que no es un
   oráculo. Y el único guardián ejecutable de esa prosa es **vacuo** (C2), reproducido de forma
   independiente por cuatro roles. De ahí que C8 y C9 sean `INCONCLUSIVE`: `Q2_TO_ZERO_PROVED`
   tiene cero respaldo ejecutable y ningún test evalúa jamás `Pr_n(S)`.
2. *Procedimental.* El comité 050 dictó que esta reparación **no puede llevar `PROVED`** y que
   `MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO` debía conservarse. El token desapareció
   del documento y la afirmación subió a `PROVED` (C12, verificado por el presidente). Es
   exactamente el modo de fallo que 050 anticipó: el mismo linaje de razonamiento escribe la
   reparación y la declara probada.

**Desacuerdos abiertos, con quién carga la evidencia:**

- *Los cuatro expertos dicen `PROCEED WITH CONDITIONS`; el guardián dice `BLOCK`.* La evidencia
  está del lado del guardián, y el presidente verificó personalmente sus tres anclajes decisivos
  (C14, C15, C17). Los expertos no se equivocaron: se les encargó atacar la matemática, y ninguno
  tenía mandato sobre el perímetro. El falsificador identificó esto explícitamente como punto ciego
  compartido heredado del encuadre del presidente — **es un fallo del presidente, no de los roles**.
- *"El manuscrito está contaminado" vs "el manuscrito está limpio".* No es contradicción: fue
  modificado contra una cláusula `NO TOCAR` (C15) pero no contiene ninguna referencia a EF-4 (C16).
  Ambas verificadas. La consecuencia práctica es que el radio de daño *científico* de EF-4 sigue
  siendo barato, mientras que la brecha *de compromiso* ya ocurrió.
- *`n>=22` vs `n=24` como primer tamaño no vacuo.* El falsificador corrigió al chain engineer por
  cómputo directo (C3). Carga la evidencia el falsificador.
- *El "umbral" `n0 = 1474934`.* El analista de márgenes lo presentó como el umbral; el falsificador
  mostró que es sólo el primer cruce dentro de una región no monótona, con 60 fallos posteriores
  (C11). Carga la evidencia el falsificador.
- *Tres citas de la ola 1 resultaron mal ancladas* (C21, C22, C23), detectadas por el verificador
  de fuentes. Ninguna es load-bearing para el veredicto, pero las tres eran presentadas con la misma
  confianza que las correctas — que es precisamente el argumento a favor de tener el rol.

## 10. Next-step spec

**Reversibles (ejecutables ya si el PI lo pide):**

R-1. **Test mínimo de falsación del falsificador.** Ejecutar la misma enumeración de
exhaustividad de la tricotomía en `n=24, rho=2` — el primer tamaño donde `threshold=0.236 < 0.25`
y por tanto `small_product` puede ser falso y los disyuntos `fixed_inner` / `loss_case` se
ejercitan por fin. Predicado: si alguna de las `C(24,4)^2 ≈ 1.13e8` tuplas falla los tres
disyuntos, C1 queda **refutada** en `n` finito. Determinista, sin semillas, sin escritura.
*Requiere levantar la prohibición de ampliar `n`* — es la única forma de convertir C1 de
`INCONCLUSIVE` en `VERIFIED` o `REFUTED`.

R-2. Registrar en la hoja la vacuidad de `test_geometric_trichotomy_exhausts_all_abstract_n12_chains`
con el diagnóstico literal (`245025/245025`) y la razón estructural (`min(f_-,f_+)<=1/4` siempre).

R-3. Registrar el umbral medido `n0 = 1474934` con su jitter hasta `1475204`, y decir explícitamente
que **no** es el `n0` de monotonía eventual que (EF4.14) requiere.

R-4. Corregir las tres citas mal ancladas (C21, C22, C23) donde se hayan propagado.

**Comprometedores (sólo con autorización explícita del PI):**

C-1. **Degradar los tokens.** `EF4_CORRECTED_PRESCRIBED_FAMILY` no puede llevar `PROVED` mientras
la orden del comité 050 siga vigente. Restituir
`MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO` con puntero a 050, y cualificar
`EF4_Q2_ASYMPTOTIC` (p. ej. `PROVED_DEDUCTIVE_NO_EXECUTABLE_BACKING`). Reglas precomprometidas: no
se sube ningún token sin auditoría independiente registrada; el autor de una reparación no firma su
propia promoción.

C-2. **Resolver el perímetro.** O bien el PI firma una nota que autorice retroactivamente la línea
EF-0..EF-8 con lista cerrada, o la línea entera pasa a `docs/backlog_hallazgos.md` como hallazgo
fuera de perímetro, según `_R3.md:14-18`. No hay tercera opción compatible con `nota 07-31:83`.

C-3. **Ejecutar §4.4 de la nota del 31-jul sobre R2**: marcarlo abierto por escrito y consignar el
paso a R1. La caja venció el 2026-08-14.

C-4. **Adjudicar las dos brechas ya cometidas** (manuscrito tocado, WP7 extendido a `d>=2`):
revertir, o regularizar con nota firmada. Los commits `326fee3` y `8139092` ya están en la rama.

C-5. **No sacar PR #4 de draft** hasta que C-1 esté hecho. Hoy nada ha salido del repositorio y el
coste de la retractación es una nota en un fichero; después del merge deja de serlo.

**Precondición de orden:** ningún PROCEED sobre EF-4 mientras el `BLOCK` del guardián siga en pie.
Y una nota sobre este mismo foro: no ejecutó una auditoría retrospectiva antes de deliberar, que es
lo que habría anclado el terreno; el hallazgo C12 llegó por el falsificador, no por diseño.

## 11. Verdict

FORO_VERDICT=REVISE_AND_RECONVENE

## 12. User sign-off

```text
FIRMADA_POR: Ignacio (PI)
FECHA: 2026-08-15
DECISION_C2: MOVER_EF0_EF8_A_BACKLOG
DESTINO: docs/backlog_hallazgos.md
AUTORISED_SCOPE: resolver exclusivamente C-2 mediante el traslado íntegro de EF-0..EF-8
NOT_AUTORISED: C-1, C-3, C-4; ampliación de n; test n=24; commit; push
OVERRIDING_NOTES: ninguna
```

## 13. Addendum 2026-08-16 — qué se hizo después de esta firma

El bloque §12 se conserva íntegro. Sus `NOT_AUTORISED` fueron levantados uno a uno, por notas
firmadas posteriores, no por interpretación:

| Ítem | Estado | Respaldo |
|---|---|---|
| C-4 | `CLOSED_BY_REVERT` | commit `a7b6623` |
| C-3 | `CLOSED` — R2 abierto, prefactor `OPEN / [UNVERIFIED]`, pasa a R1 | commit `44b0d75` |
| `ampliación de n` / `test n=24` | autorizados **sólo** para R-1, renombrado `FORO001-F1` | `docs/scope_note_2026-08-16_foro001_falsification_test.md` |
| R-1 (`FORO001-F1`) | EJECUTADO — tricotomía falsa en el dominio **abstracto**, **no refutada sobre `F_n`** | `dev/EF4_TRICHOTOMY_N24_RESULT.md`, commits `7b5deec` + corrección |
| C-1 | `ADJUDICATED`, corregido en parte el mismo día | `docs/c1_adjudication_2026-08-16_ef4_token_degradation.md` + `docs/c1_correction_2026-08-16_realizability.md` |
| C-5 | **sigue en pie** — PR #4 no sale de draft | — |

Sobre el ledger de §9: la fila **C1** se mantiene en **`INCONCLUSIVE`**. Se emitió `REFUTED` el
2026-08-16 y **se retractó el mismo día**: los 560 fallos de `n=24` emparejan filas y columnas que
la prescripción `F_n` prohíbe (el testigo usa `(11,11)` cuando `F_n` fija `11 -> 7`), de modo que
no son permutaciones de `F_n` y no refutan la familia. De las `40` configuraciones realizables
donde `small_product` no basta, las `40` caen en `loss_case`:
`dev/ef4_trichotomy_prescription_compatibility_n24.py` → `COMPATIBLE_FAILURES=0`.

La fila **C3** (`n=24` es el primer tamaño donde el test podría morder, `VERIFIED`) se confirma
por ejecución: `n=12` da `245025/245025` vacuas y `n=24` da `1504` tuplas no vacuas.

**Lección para el próximo falsificador.** El test mínimo especificado en §10 —y el predicado que
esta casa firmó a partir de él— cuantificaba sobre `C(24,4)^2` cuádruplas **abstractas**. Ese es
el dominio equivocado: el certificado sólo tiene que cubrir cadenas realizables bajo `F_n`
(`11.639.124` en `n=24`, no `112.911.876`). Un predicado precomprometido sobre el dominio
equivocado produce un veredicto limpio, reproducible y falso.
