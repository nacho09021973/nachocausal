# Fase 1 · Paso 1.4 — Draft §4 (positive) + §5 (ledger)

> **STATUS: MANUSCRIPT_SECTION_DRAFT / NOT_FROZEN / NO_NEW_SCIENCE /
> DOES_NOT_TOUCH_SEAL / DOES_NOT_DISCHARGE_ITEM_5.**
>
> Pilares **P3** y **P2** del paper de límites. Material reutilizado de
> `docs/paper_outline_c1c6_plus_prereg002.md`, `docs/preregistration_002{,_result}.md`,
> y `docs/comite/comite_decision_042_…` (ampliado con C6 / 043–044).
>
> FECHA: 2026-07-28 · HEAD de referencia: `0bf0017`
> Gobernanza: R3 — ledger = `EMPIRICAL_FAILURE_OF_CLASS_L` only; never a substitute
> for Theorems 3.1–3.8 (`PROVED_NON_IDENTIFIABILITY`).

**Convenciones:** `[PROVED]`, `[BACKGROUND]`, `[VALIDATED]`, `[REMARK]`,
`EMPIRICAL_FAILURE_OF_CLASS_L`, `PROVED_NON_IDENTIFIABILITY`.

---

## §4 A sealed in-patch recoverability positive
<!-- Pillar P3 · manuscript body -->

Section 3 maps **limits**: targets that no order-only map can identify, or can identify
only above a rate floor. Those theorems would be empty of scientific interest if the
order-only channel were *vacuously* uninformative about every geometric score. This
section records that it is not. Under a frozen pre-registration, a single order-only
observable—future volume—passes a sealed blind validation contract in a finite
\(1{+}1\) Schwarzschild patch. The result is **recoverability of an in-patch geometric
signal**, not reconstruction of a global event horizon
(`NO_RECONSTRUCTION_CLAIM`).

### 4.1 Frozen contract (preregistration 002)

**Label.** Pre-registration: `docs/preregistration_002.md` (status FROZEN).  
**Instrument.** Estimator-v2 under the sealed package
(`docs/estimator_v2_freeze.md`, `docs/estimator_v2_seal.md`).  
**Seal.** `nachocausal/thresholds.py` SHA256
`6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
(`make verify-seal`). Thresholds and seeds were frozen **before** the blind
validation run.

**Observable (order-only).** For each sprinkled element \(i\),
\[
O(i) \;=\; \bigl|\mathrm{future}(i)\bigr|
\]
(cardinality of the causal future inside the patch). The point estimate of the
horizon-associated boundary uses a bracket midpoint under a frozen analysis plan
inherited from the prereg-001 addendum and modified only by the three sealed
estimator-v2 changes: VOLUME observable; \(\tau(n)\) abstention gate; domain gate
\(T_{\mathrm{EDGE\_MIN}}=6\).

**Channel.** Order-only selection and scoring: no continuum coordinates are available
to the estimator. The hidden embedding is used **only** to score localization error
after the estimate is produced (§1.3).

**Held-out seeds.** Twenty validation seeds drawn once, blind, from the virgin band
\([2\,000\,000,\,2\,999\,999]\) by a deterministic `numpy` draw
(`VALIDATION_DRAW_SEED=20260622`), disjoint from all exploration seeds
(prereg-002 text; guard in `thresholds.py`).

**Primary endpoint.** Intensity \(\lambda=12000\) (mean \(N\) of order \(1.2\times 10^4\)),
\(t_{\mathrm{edge}}=6\) (in-domain). **PASS** if and only if all six frozen checks hold
at that endpoint (significance, localization, convergence slack, stability, false
positive, order-only guard); otherwise FAIL / INCONCLUSIVE / OUT_OF_DOMAIN as
specified—**report alike**, no post-hoc retuning.

### 4.2 Blind outcome

**Verdict.** `[VALIDATED]` with documented artifact caveats (next subsection):

```text
PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY]
```

At the primary endpoint, all six frozen checks evaluated true
(`docs/preregistration_002_result.md`). Headline primary numbers (transcribed from
the original validation table; same values MATCH under supervised re-verification):

| Check | Primary (\(\lambda=12000\)) |
|---|---|
| Sign-flip \(p_{\mathrm{perm}}\) | \(9.54\times 10^{-7}\le 10^{-4}\) |
| Median \(\lvert dr\rvert/(2M)\) vs \(\theta_{\mathrm{loc}}\) | \(0.064\le 0.098\) |
| Coverage | \(0.95\ge 0.5\) |
| Boundary \(r\)-std vs \(\theta_{\mathrm{stab}}\) | \(0.008\le 0.049\) |
| LOO false-positive fraction | \(0.00\le 0.05\) |
| Order-only guard | no raise |

The \(\tau(n)\) abstention gate behaves as designed: Schwarzschild abstention \(0.00\)
at every intensity level; Minkowski control abstention \(0.90\)–\(1.00\) (suppresses
structureless false structure). A transparent non-primary caveat is recorded: at
\(\lambda=6000\), false-positive fraction \(0.10\) misses \(\theta_{\mathrm{fp}}\); the
frozen rule evaluates false positives **only** at the primary endpoint, where the
check passes.

**Run provenance (historical).** Blind `validate.run()` on the sealed package at
commit `573cfcb`, seal as above, numpy 1.26.4; chain
decision → freeze → estimator seal → prereg-002 seal → single blind run
(prereg-002 result §Provenance).

### 4.3 Artifact integrity and supervised re-verification

Honesty about the raw artifact is part of the positive, not a footnote to hide.

1. The **primary raw** `results/validation.json` of the original 2026-06-22 blind run
   was later found unrecoverable (`auditor_report_005`, `AUDIT_FAIL`; second machine
   unavailable per PI determination).
2. A **supervised re-verification** was authorized
   (`comite_decision_016`, `prereg002_reverification_declaration.md`): deterministic
   replay on the same sealed instrument, commit lineage, and frozen seeds—not a
   second blind discovery, not a retuning loop.
3. Outcome: **MATCH** on every frozen field
   (`prereg002_reverification_result.md`).

Therefore the scientific claim remains the frozen PASS under the pre-registered
contract, with the epistemic status explicitly weakened to
`PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY`. We do
not claim recovery of the original raw bytes.

### 4.4 What the PASS means

**Means (bounded, frozen claim).** In a finite \(1{+}1\) Schwarzschild patch at the
sealed domain edge, the causal order alone—under this observable and this
protocol—carries enough information to localize a horizon-*associated* boundary
score **significantly and stably** relative to frozen thresholds, with bracket width
contracting toward the discreteness floor as density grows, while a box-matched
flat control does not produce the same separation
(prereg-002 result, “What this PASS does and does NOT mean”).

**Units.** Localization is scored in units of \(2M\) and compared to thresholds built
from the discreteness scale \(\ell\). This is compatible with Theorem 3.1: absolute
\(r_s\) is non-identifiable at fixed \(n\); the PASS does not claim absolute scale.

**Role relative to Section 3.** The channel is not empty. Non-identifiability of
absolute mass, of the global event horizon, and the rate floor for a continuous
family parameter coexist with recoverability of a **different**, carefully
contracted in-patch score.

### 4.5 What the PASS does not mean

| Forbidden reading | Why |
|---|---|
| Global event horizon reconstructed | Theorem 3.2; claim grammar §3 |
| Full metric reconstruction | Outside contract |
| \(3{+}1\) Schwarzschild / Kerr | Outside bank and dimension |
| Region-locators C1–C6 work | They do not; see §5 |
| Every order-only map succeeds at something | Only this sealed instrument under this protocol |
| Primary raw artifact still on disk | §4.3 |

### 4.6 Methodological note (optional short paragraph)

Dev/validation separation, pre-frozen thresholds, and one-way blind evaluation are
part of the positive’s credibility. A guardrail that cannot fail is decoration: every
number above is either the literal output of a sealed run / MATCH re-verification or
is marked as transcription. No threshold was loosened after seeing validation
outcomes (`NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`).

---

## §5 Typed negative ledger: six exhausted region-localization channels
<!-- Pillar P2 · manuscript body -->

### 5.1 Why a ledger is a result

Section 3 answers questions of the form: *no estimator in the whole measurable class
can identify \(T\).* This section answers a different question:

> Within a **named** class \(L\) of order-only constructions aimed at localizing a
> *region* of horizon-like structure in this finite \(1{+}1\) bank, what happened to
> each construction under project adjudication?

Documenting typed failures with terminals, anchors, and lessons is a scientific
deliverable of a recoverability benchmark (“documented failure \(>\) almost-PASS”;
committee decision 042). The program label for the entire section is:

```text
EMPIRICAL_FAILURE_OF_CLASS_L
L = {C3-early, C1, C2, C3-third, C4, C5, C6}
      (region-localization constructions in this bank)
```

**Rule R3 (binding, restated).** Nothing in §5 is a proof of
`PROVED_NON_IDENTIFIABILITY`. In particular, §5 does **not** prove that every
conceivable order-only map fails to localize every conceivable quasi-local proxy.
It proves only that the listed constructions, under the listed adjudications,
terminated as stated.

### 5.2 Master table

Anchors: `docs/comite/comite_decision_042_c1-c5-localizer-line-closure.md` §3–§4
(C1–C5); C6 via decisions 043–044 and the consolidation outline
`docs/paper_outline_c1c6_plus_prereg002.md` §4–§5. Label on every row:
`EMPIRICAL_FAILURE_OF_CLASS_L`.

| ID | Construction (one line) | Terminal | Lesson (one line) | Program label |
|---|---|---|---|---|
| **C3-early** | Future-width / funnel collapse as horizon proxy | `REJECTED_HAYWARD` | Funnel tracks singularity truncation, not trapping (fails regular Hayward control) | `EMPIRICAL_FAILURE_OF_CLASS_L` |
| **C1** | Bottleneck / ideal / flow through `Max` | `BLOCKED_UNCLOSED` + `MAX_TRIVIAL` | Finite `Max` trivializes; definition never closed as frozen localizer | `EMPIRICAL_FAILURE_OF_CLASS_L` |
| **C2** | Common-future overlap / \(\kappa\) on a wavefront | `BLOCKED_E_INDEP` + `TRUNCATION` | Without null structure + ceiling control, confounds with box truncation | `EMPIRICAL_FAILURE_OF_CLASS_L` |
| **C3-third** | Truncated-future selectors \((L,V)\) on minimals | `INCONCLUSIVE_EDGE_MARGINAL` | Edge-dominated marginal channel; insufficient pair synergy | `EMPIRICAL_FAILURE_OF_CLASS_L` |
| **C4** | Common-future convergence conditioned on neighbors | `REJECTED_NO_E_M` | No order-only, relabel-invariant neighbor graph \(E_M\) (decision 039) | `EMPIRICAL_FAILURE_OF_CLASS_L` |
| **C5** | Global common-future matrix → spectral block / partition | `EXHAUSTED` (F3) | Wall \(\neq\) `Max`; twin/bridge ambiguity; no lateral dual (040–041) | `EMPIRICAL_FAILURE_OF_CLASS_L` |
| **C6** | Antichain waist \(W(p,q)\) of an Alexandrov interval | `BLOCKED_NO_STABLE_CODIM2` | Antichain exists as order object; stable codim-2 screen and transport do not | `EMPIRICAL_FAILURE_OF_CLASS_L` |

**Line status.** C1–C5: `EXHAUSTED_FOR_LOCALIZATION` as a localizer line for
horizon/edge structure in this bank (decision 042). C6: closed at the conservative
terminal after committee red-team (043→044), not promoted to a frozen localizer.

### 5.3 Channel notes (short)

**C3-early.** Width collapse looked like a trapping diagnostic until a regular
(non-singular) black-hole control removed the funnel: the signal was singularity
geometry, not apparent horizon. Terminal: reject for horizon localization.

**C1.** Ideal-theoretic bottleneck formalisms never closed in the finite unlabeled
setting; maximality notions that work in the continuum idealize badly when `Max` is
trivial or unclosed. Never promoted to a frozen localizer.

**C2.** Common-future overlap statistics confound physical near-horizon structure with
the computational ceiling of the patch. Independence and truncation controls blocked
promotion.

**C3-third.** Clean developmental channel on truncated futures of minimals; remains
inconclusive and edge-dominated—a marginal channel rather than a region partitioner.

**C4.** Any “neighbor-conditioned” construction requires an edge set \(E_M\) on
minimals. No order-only, permutation-invariant, non-circular, tie-closed definition of
\(E_M\) was available; continuum references (Rideout–Wallden, Boguñá–Krioukov) do not
supply that \(E_M\) in the C4 domain (decision 039). Concept blocked before
pre-registration.

**C5.** Global matrix methods can be mathematically live as linear algebra on the
poset; as a *localization channel* they exhaust on wall/bridge/twin ambiguity and the
absence of a lateral dual peel that would turn a spectral block into a horizon
region (decisions 040–041).

**C6 (detail).** For \(p\prec^* q\), the waist
\[
W(p,q)
\;=\;
\{\,x : p\prec^* x \land x\prec^* q\,\}
\]
is an antichain in the order (order-only theorem; full proof in project appendix
material). Existence of an antichain is not existence of a **stable codimension-two
screen** with order-only transport and sign. Committee 043 initially overstated
abundance/stability; red-team 044 lowered the terminal to the conservative
`BLOCKED_NO_STABLE_CODIM2`. The self-correction is part of the method: the ledger
records the lower claim, not the withdrawn higher one.

### 5.4 Cross-cutting structural reading

Across C1–C6, the recurring obstructions in this bank are:

1. **Ceiling / wall / truncation** of the finite patch mistaken for physical boundary;
2. **No lateral pairing** or neighbor structure that is purely order-only;
3. **Scale \(\leftrightarrow\) depth** confounds when absolute scale is invisible
   (Theorem 3.1) but patch depth is visible;
4. **No stable order-only codimension-two object** with transport (C6), in a dimension
   where continuum codim-2 screens are already subtle.

These are lessons about *this construction class in this bank*, not a theorem that
the order contains no geometric information (contradicted by §4) and not a theorem
that every quasi-local continuum proxy is non-identifiable (that would require
witness pairs or Fisher analysis for each named \(T\), i.e.\ Section 3 methodology).

### 5.5 What §5 does not authorize

| Forbidden | Correct substitute |
|---|---|
| “Therefore horizon localization is impossible order-only” | Theorems 3.1–3.2 for absolute scale and global EH; open/abandoned for other \(T\) under R1 |
| “C1–C6 prove minimax lower bounds” | Only Thm 3.8-style arguments prove minimax floors |
| Reopening A–C matrix candidates as the program north | `ABANDONED_AS_PROGRAM_NORTH` (Fase 0 R1) |
| Renaming singularity funnel as trapping | claim grammar trichotomy §1.4 |

### 5.6 Relation to the abandoned north and to Section 3

The ledger **motivates** the program decision not to spend further cycles on the same
region-localizer line (§1.5). The **proofs** that absolute mass and the global event
horizon are out of reach are Section 3, not Section 5. A future no-go for a named
quasi-local proxy \(Q\) would require a new witness pair or rate bound for that \(Q\)
(Fase 3 option B2), not another row of the same ledger style without measure-theoretic
content.

---

## Stitching note (full manuscript order so far)

```text
phase1_section1_2_abstract_draft.md     →  title, abstract, §1, §2
phase1_section3_nonidentifiability_draft.md →  §3  (P1)
phase1_section4_5_positive_ledger_draft.md  →  §4 (P3), §5 (P2)
(pending 1.5)  §6 literature, §7 open/abandoned, §8 conclusions
```

Pillar order in the **outline** was P1–P2–P3 by weight; in the **manuscript** we place
P3 before P2 so that the reader sees “channel not empty” before “these constructions
failed.” The abstract already lists non-identifiability first (scientific weight), then
positive, then ledger—consistent with both.

---

## Repo anchors (auditor table)

| Block | Primary anchors |
|---|---|
| §4.1 contract | `docs/preregistration_002.md`; estimator-v2 freeze/seal docs |
| §4.2 PASS table | `docs/preregistration_002_result.md` |
| §4.3 re-verification | `comite_decision_016`; `prereg002_reverification_{declaration,result}.md`; `auditor_report_005` |
| §5.2 C1–C5 | `comite_decision_042_c1-c5-localizer-line-closure.md` |
| §5.2–5.3 C4 | `comite_decision_039_…` |
| §5.2–5.3 C5 | `comite_decision_040/041_…` |
| §5.2–5.3 C6 | `comite_decision_043/044_…`; outline C1–C6 §5 |
| Seal hash | `thresholds.py` SHA256 `6e2c3888…bfefd4` (do not change seal) |

## Numbers policy

All numeric entries in §4 are **transcriptions** of
`preregistration_002_result.md` (MATCH under re-verification). No new ensemble was
run for this draft. If any figure is later disputed, re-run sealed validation under
auditor rules; do not edit numbers by hand without a generator commit.

---

## Checklist paso 1.4

```text
[x] §4.1 frozen contract (observable, seal, seeds, PASS rule)
[x] §4.2 blind outcome + primary table
[x] §4.3 artifact lost + supervised MATCH
[x] §4.4 means / role vs §3
[x] §4.5 does not mean (table)
[x] §5.1 ledger as result + R3
[x] §5.2 master table with EMPIRICAL_FAILURE_OF_CLASS_L every row
[x] §5.3 short channel notes + C6 self-correction
[x] §5.4 cross-cutting lessons
[x] §5.5 forbidden readings
[x] §5.6 link to abandoned north vs Thm 3.1–3.2
[ ] PI review of §4 caveats wording and §5 R3 discipline
[ ] Paso 1.5 — §6 literature + §7 open/abandoned + §8 conclusions
```

## Next (1.5)

Draft §6 (literature: Order+Number, Müller, Boguñá–Krioukov, EGS, textbook methods),
§7 (open vs abandoned; Fase 3 B2 pointer), §8 (conclusions restating P1–P3 labels).
Optional: merge §1–§5 into a single `docs/manuscript_limits_draft.md` after 1.5.
