# Auditor Report 001 — pr003-c1-freeze-foundation

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target
Backward-looking foundation for the forward `/comite` deliberation on the **PR-003 Fase #3 C1
freeze** — turning `docs/preregistration_003_draft.md` into a frozen `docs/preregistration_003.md`.
- Repo root `/home/ignac/nachocausal`, branch `main`, commit `bffa8a9` (`git rev-parse --short HEAD`).
- Working tree clean (`git status --short` empty); frozen `docs/preregistration_003.md` absent
  (only the draft exists — `ls docs/preregistration_003.md` → No such file).
- Trigger: pre-`/comite` foundation for a committing step (new pre-registration). A PROCEED may not
  be deliberated atop an `AUDIT_FAIL`.
- Audit focus per request: (1) seal integrity, (2) number provenance for `docs/preregistration_003_draft.md`
  §1/§3/§4, (3) dev/validation separation, (4) claim boundary (no minimax / no info-floor-over-C).

## 2. Mechanical audit
Verbatim output of `bash .claude/skills/auditor/audit.sh` (exit code `0`):

```
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/hoja_de_ruta_25_jun_2026.md,docs/preregistration_002.md,docs/preregistration_003_draft.md
----------------------------------------
Auditor: 0 error(s), 0 warning(s)
=== EXIT=0 ===
```
No CI-swallowing, no untested-code, no seal drift, no gitignored-but-tracked path, no ungenerated
`results/` data flagged.

## 3. Seal & freeze integrity
- Live seal: `make verify-seal` → `nachocausal/thresholds.py sha256:
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`; independently confirmed via
  `python3 -c "hashlib.sha256(...thresholds.py...)"` → identical.
- Recorded frozen SHA: `docs/preregistration_002_result.md:10` names seal `6e2c3888…` for the blind
  PASS run; the draft itself names the same SHA (`docs/preregistration_003_draft.md:14-15`). Live ==
  recorded. **No drift.**
- `git status --short` shows no `M nachocausal/` — the sealed instrument is byte-unchanged.
- The draft proposes **no** change to `thresholds.py` (anchor `K = K_LOC = 2` is the already-sealed
  value, `thresholds.py:98`); the freeze adds only a doc. **OK.**

## 4. Reproducibility of published numbers
All numeric anchors in `docs/preregistration_003_draft.md` resolve to committed sources:

**In-repo anchors (§1, §3 leg 1, §4) — verified literal, this CPU session:**
- `K_LOC = 2` — `nachocausal/thresholds.py:98`. **OK.**
- `POOLED_SD_FLOOR = 0.5` — `thresholds.py:78`. **OK.**
- `theta_loc = K_LOC·ℓ/(2M)`, `theta_stab = K_LOC·ℓ` — `thresholds.py:106-113` (`def theta_loc`,
  `def theta_stab`). **OK.**
- `BOX_AREA = T_EDGE·R_EDGE = 7.2`, `T_EDGE=6.0`, `R_EDGE=1.2`, `R_S=0.5`, `M=0.25` —
  `thresholds.py:36-43`. **OK.** (Draft cites `:36-43`; exact constants on `:37-41`.)

**Dev-measured figures (§3 leg 2 = O3, leg 4 = R2) — traced to committed deterministic scripts and
recorded in committed notes; NOT independently re-executed this session (see Finding W1):**
- O3 `r̂` scatter `≈ 0.40·ℓ`, density-invariant over ×8 density — `dev/measure_info_bound_o3.py`
  (git-tracked); recorded `dev/PR003_INFO_BOUND_NOTES.md:202` (intensity 12000 → `0.40`), `:204`
  ("density-invariant"), table `:199-202`.
- O3 resolvable separation `2s/ℓ ≈ 0.6` (TVg=0.5) — notes `:199-202` (`0.60–0.71`), `:287`, `:308`.
- O3 GPU≡CPU `maxdiff = 0` for this observable — notes `:191`.
- R2 top-1 `d⊥/ℓ@k=8 ≈ 5-7ℓ` for all K=1→64 — `dev/measure_kbeam_peeloff.py` (git-tracked);
  recorded `dev/PR003_KBEAM_PEELOFF_NOTES.md:54-55`, table `:41`.
- R2 head `k≤3 ≈ 2ℓ` — notes `:60` (and `:48` "adherent head ≈1.6-2.0ℓ for k=1-3").
- R2 `reach≥8 ≤ 23%` at K=64, t_edge=6 — notes `:41`, `:72-73`; label "PHYSICAL within box reach"
  `:76-77`.
Every figure in the draft has a committed generator and a recorded value; none is unbacked.

## 5. dev/validation separation & ground-truth leakage
- Both evidence scripts enforce the separation **at runtime**: they refuse any seed outside
  `EXPLORE_POOL` and any seed in the `RESERVED_002` band —
  `dev/measure_info_bound_o3.py:114-116` and `dev/measure_kbeam_peeloff.py:94-96`
  (`raise SystemExit(... refusing ...)`). Both print "no seed in RESERVED_002 touched"
  (`measure_info_bound_o3.py:323`, `measure_kbeam_peeloff.py:327`).
- Ground truth used only to **score**, never to guide: `measure_info_bound_o3.py:36`
  "the estimator/observable never sees r. No RESERVED_002 seed is touched."
- No-new-constant / leakage gate #5: the draft reports the measured constant `O(1) < 2` as a
  *consistency* statement about the existing sealed `K_LOC = 2`, and forbids re-tuning `K` on the
  EXPLORE_POOL measurement (`docs/preregistration_003_draft.md:86-92`). No score feeds back into a
  threshold. **OK — separation intact.**

## 6. Claim-boundary check
The draft does **not** over-claim. Every occurrence of `minimax` / `universal` / `information floor`
/ `no estimator` / `reconstruction` / `3+1D` / `Kerr` / `asymptotic` in the draft appears under a
**NOT** or **OPEN** heading, never as an established result:
- `docs/preregistration_003_draft.md:40-47` — "**NOT** a Le Cam minimax lower bound over all
  functions of `C`"; states the data-processing direction (output KL bounds full-data KL **from
  below**) and leaves the minimax-over-`C` bound "explicitly OPEN".
- `:49-51` — "**NOT** a universal / asymptotic no-go." `:55` — "**NOT** 3+1D, **NOT** Kerr, **NOT**
  metric reconstruction." `:78` — O1 "explicitly NOT a minimax statement."
- `:108-110` — a built-in freeze self-check requiring `/auditor` to confirm the frozen text never
  reintroduces "no estimator of `C` can do better".
- `:117-119` — minimax floor over `C` listed under "Open items … explicitly NOT closed."
The registered claim stays inside the prereg-002 frozen language: order-only localisation of the
horizon-associated boundary within a finite patch (operational, estimator-induced). **OK — no
over-claim; the requested boundary (no minimax / no info-floor over C) is honored.**

## 7. Findings
| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | Mechanical audit clean: 0 errors / 0 warnings | `bash audit.sh` → exit 0 |
| 2 | OK | Live seal `6e2c3888…` == recorded prereg-002 seal; no `M nachocausal/`; draft re-seals nothing | `make verify-seal`; `docs/preregistration_002_result.md:10`; `thresholds.py:98` |
| 3 | OK | All in-repo anchors (K_LOC, POOLED_SD_FLOOR, theta_loc/stab, BOX_AREA) resolve literally | `thresholds.py:78,98,106-113,36-43` |
| 4 | OK | O3 / R2 figures backed by committed scripts + recorded in committed notes | `dev/measure_info_bound_o3.py`, `dev/measure_kbeam_peeloff.py`; `PR003_INFO_BOUND_NOTES.md:191,199-204`; `PR003_KBEAM_PEELOFF_NOTES.md:41,54-60,72-77` |
| 5 | OK | dev/validation separation enforced at runtime (EXPLORE_POOL only; RESERVED_002 refused); no score→threshold feedback | `measure_info_bound_o3.py:114-116,36`; `measure_kbeam_peeloff.py:94-96`; draft `:86-92` |
| 6 | OK | Claim boundary respected: minimax/universal/3+1D/Kerr/reconstruction only under NOT/OPEN | `docs/preregistration_003_draft.md:40-55,78,108-119` |
| W1 | WARN | O3 (`measure_info_bound_o3.py`) and R2 (`measure_kbeam_peeloff.py`) are GPU-produced (numpy 2.4.6 dev venv); this CPU audit session traced them to committed scripts + recorded notes but did **not** independently re-execute them to confirm bit-level reproduction. The freeze step should re-run both generators in a GPU session and confirm the recorded figures before `docs/preregistration_003.md` is created. | `dev/PR003_KBEAM_PEELOFF_NOTES.md:9` (HEAD `5081f4e`, numpy 2.4.6, GPU venv); raw logs git-ignored/regenerable |

AUDIT_ERRORS=0
AUDIT_WARNINGS=1

## 8. Verdict
One of: `AUDIT_PASS` (no errors, no warnings), `AUDIT_PASS_WITH_WARNINGS` (no errors, ≥1 warning),
`AUDIT_FAIL` (≥1 error). Must match the counts in §7.
AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
