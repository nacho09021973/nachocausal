# R-VAR — Closure as a Documented Negative Result

> Disposition-commit authorized by the PI, 2026-07-05, per the pre-committed criterion in
> `docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md` §11.3 ("if that object
> fails its own Gate 0 / calibration, R-VAR closes as a documented negative result") and
> `docs/comite/comite_decision_021_rvar-egs-truncation-object.md` §9 step 3 ("if step 1 fails
> [...] this step becomes a negative-result commit instead [...] never a redesign-and-retry on the
> same dev seeds").

## Status token

```
R_VAR_STATUS = CLOSED_NEGATIVE_RESULT [
  NO_NONDEGENERATE_MINK_NULL_FOUND_ON_FROZEN_GEOMETRY;
  TESTED_OBJECTS = {
    A_C_EMPTY_NONEMPTY_DICHOTOMY (REJECTED unanimously, comité 020 §8 —
      box-aspect-ratio artifact, corner-artifact argmax),
    LONGEST_CHAIN_FROM_MINIMAL + FUTURE_CARDINALITY_OF_MINIMAL (comité 021 candidate,
      falsification test FAILED on MINK non-degeneracy, dev/rvar_egs_falsification_test_result.json)
  };
  GEOMETRY_SPECIFIC (frozen tall box T_EDGE=6.0, R_EDGE=1.2, nachocausal/thresholds.py:36-38 —
    this closure is a statement about THIS box, not a universal claim about order-only
    horizon-truncation diagnostics);
  PRIMARY_TRACK_UNAFFECTED (prereg-002 / estimator-v2 PASS, seal intact, untouched throughout)
]
```

This is a **third explicit state**, following the same reporting discipline as
`PARTF_STATUS` (`docs/rvar_partF_disposition.md`): not a silent abandonment, not a claim that
"R-VAR failed to detect a real signal," but a documented closure with the specific reason
recorded and falsifiable.

## What happened, in order

1. **Part F (μ-calibration over the binary `𝒜(C)` EMPTY/nonempty object) was blocked by measured
   degeneracy**, never executed: `𝒜(C)=∅` certified 12/12 on production MINK, a consequence of the
   frozen tall-box aspect ratio (`R_EDGE=1.2 ≪ T_EDGE=6`), independent of compute
   (`docs/rvar_partF_disposition.md`, commit `896ec3e`).
2. **Comité 020** (commit `4a408a8`) unanimously rejected promoting the binary dichotomy itself as
   an object (post-hoc, box-artifact, corner-argmax) and signed a re-scope direction: an order-only
   graded observable with a non-degenerate MINK null, targeting Schwarzschild
   singularity-truncation, per the EGS future-cardinality/longest-chain bimodality mechanism — with
   an explicit PI-set criterion: *if that object also fails its own gates, R-VAR closes as a
   documented negative result.*
3. **Part E's over-claim was re-scoped** to a bounded polynomiality claim (`dev/PR003_R_VAR_SELECTOR_SPEC_V2_3.md`,
   commit `c92cb40`), independent of this closure and not affected by it.
4. **Comité 021** (commit `a15c1a3`) adjudicated the candidate object: PRIMARY = longest-chain
   height `L(i)` from each minimal element, SECONDARY = future-cardinality restricted to `Min(C)`,
   both order-only, no auxiliary sort key. The falsifier (corroborated independently by the
   literature verifier) flagged that EGS's cited MINK non-degeneracy evidence ("varies between n
   and √n already for Minkowski") is textually scoped to a **causal diamond**, not this project's
   frozen **tall box** — and predicted the same box-geometry mechanism that made `𝒜(C)=∅` could
   also collapse these graded statistics to near-degeneracy. The committee mandated a cheap,
   dev-seed-neutral falsification test (zero new seed consumption) as the required first move
   before treating any spec as more than a draft.
5. **The falsification test ran** (`dev/measure_pr003_rvar_egs_falsification_test.py` →
   `dev/rvar_egs_falsification_test_result.json`, report
   `dev/PR003_RVAR_EGS_FALSIFICATION_TEST_REPORT.md`), reusing the three already-consumed dev
   seeds (`20240617/13/101`) at all four frozen intensities. Result: the MINK coefficient of
   variation for both `L(i)` and `future_card(i)` across `Min(C)` was **0.006–0.024** at every
   intensity and every seed — versus **0.72–1.01** for the same statistics on BH draws (a
   40–100× gap). Every MINK minimal element has nearly identical longest-chain length and future
   cardinality: a near-delta-spike null, not the graded spread EGS's causal-diamond evidence
   predicted. The BH-side signal itself is genuine and strongly separated (Cohen's d ≈ 5.9–9.2,
   interior/exterior), and interior occupancy correctly **scales** with `n_min` across
   intensities (no corner-artifact relapse) — but a strongly-separated BH signal cannot be
   calibrated against a MINK null that has almost no spread to set a quantile against.
6. **PI decision, 2026-07-05:** given the falsification test's result — the second
   graded/order-only object attempted on this frozen geometry to show the same
   near-degenerate-MINK-null failure mode as the first (binary) object — R-VAR closes as a
   documented negative result, per the criterion pre-committed in step 2.

## What this closure means

The recurring mechanism across both attempted objects is geometric, not statistical bad luck:
this project's frozen tall box (`T_EDGE=6.0 ≫ R_EDGE=1.2`, chosen to sharpen the BH/MINK jump for
the *sealed* future-volume estimator, `docs/estimator_v2_freeze.md`) makes MINK causal structure
at these intensities close to "every minimal precedes (almost) every maximal" — light crosses the
box's spatial width in `Δt=R_EDGE=1.2`, far shorter than the box's temporal extent `T_EDGE=6.0`.
Any order-only statistic computed *per minimal element* on MINK draws in this geometry is likely
to inherit this near-homogeneity and collapse toward a single value, regardless of whether the
statistic is a binary membership flag (`𝒜(C)`) or a graded height/cardinality (`L`,
`future_card`). Two independently-designed objects hit the same wall.

## What this closure does NOT claim

- **Does not claim no order-only Schwarzschild-horizon diagnostic can ever work.** This is a
  closure specific to (i) this project's frozen box geometry and (ii) the two specific objects
  tested. A differently-shaped patch (e.g. closer to EGS's own causal-diamond geometry) or a
  geometry-normalized statistic might behave differently — but exploring that would be a **new**
  committee question with its own pre-registration and Gate 0, not a reopening or "fix" of this
  closed line (`NO_POST_HOC_TUNING`: redesigning on the same already-inspected dev seeds is
  exactly what is prohibited).
- **Does not touch the project's primary result.** `prereg-002` / estimator-v2 (future-volume
  observable `O_min`) remains `PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED;
  BLINDNESS_DOCUMENTARY_ONLY]`, sealed, unaffected. `make verify-seal` confirmed MATCH
  (`6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` =
  `docs/preregistration_002.md:8`) both before and after every step of this closure.
- **Does not retroactively invalidate Part E's computability finding.** The bounded polynomiality
  claim in `dev/PR003_R_VAR_SELECTOR_SPEC_V2_3.md` (v2.3, commit `c92cb40`) is a true statement
  about the algorithmic structure of the `𝒜(C)`-restricted selector, independent of whether R-VAR
  as a whole is pursued further.
- **Does not claim the falsification test constitutes a formal Gate 0.** No numeric
  accept/reject threshold was pre-frozen for MINK non-degeneracy (freezing one after seeing the
  data would itself be `NO_POST_HOC_TUNING`); the 40–100× CV gap is reported as the empirical
  basis for the PI's closure decision, not as a certified statistical test result.

## Anchors

| Fact | Source |
| --- | --- |
| Part F blocked by measured degeneracy, never executed | `docs/rvar_partF_disposition.md`, commit `896ec3e` |
| Comité 020: binary dichotomy rejected, graded-object re-scope signed, negative-closure criterion set | `docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md` §8, §11.3, commit `4a408a8` |
| Part E re-scope (independent of this closure) | `dev/PR003_R_VAR_SELECTOR_SPEC_V2_3.md`, commit `c92cb40` |
| Comité 021: candidate object adjudicated, falsification test mandated | `docs/comite/comite_decision_021_rvar-egs-truncation-object.md`, commit `a15c1a3` |
| Falsification test: MINK CV 0.006–0.024 vs BH CV 0.72–1.01; BH Cohen's d 5.9–9.2; BH interior occupancy scales with `n_min` | `dev/rvar_egs_falsification_test_result.json`, `dev/PR003_RVAR_EGS_FALSIFICATION_TEST_REPORT.md` |
| EGS's non-degeneracy evidence is scoped to a causal diamond, not a box | comité 021 §7 literature verdict, `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:247` |
| Seal unaffected throughout | `make verify-seal` → matches `docs/preregistration_002.md:8` |
| Primary result unaffected | `docs/prereg002_reverification_result.md` |

## Next steps (not authorized by this record)

None on this line. A future order-only horizon/truncation diagnostic, if pursued, requires a new
`/comite` question defining a new object under a new pre-registration — not a continuation of
R-VAR.
