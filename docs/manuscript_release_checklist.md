# Manuscript release checklist

Status date: 2026-08-16

Code-and-manuscript commit tested by the 2026-08-07 release gate: `ab038a88836083276f17406e2537463189e79967`

This checklist separates the scientific gate for taking the manuscript PR out of
draft from the administrative work needed for an eventual arXiv submission.

## Scientific release gate

- [x] **Complete the audited 64-realization bit-exact regression.**
  - Fixture: `nachocausal/fixtures/o_samples.json` (`64` records).
  - Command:
    ```text
    .venv/bin/python -m pytest -vv -s \
      tests/test_regression.py::test_o_multisets_bit_exact
    ```
  - Result: `PASSED` — `1 passed in 254.79s`; process exit status `0`.
  - Environment: Python `3.12.3`, NumPy `1.26.4`, pytest `8.4.2`.
  - Wall time measured by `/usr/bin/time -v`: `4:25.38`; maximum resident set
    size: `556424` KiB.
- [x] **Recheck the frozen threshold seal.**
  - Command: `make verify-seal`.
  - Result:
    `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.

The scientific/technical blocker tracked by the 2026-08-07 gate is closed. This
checklist is documentation-only and does not modify the tested code, fixture,
estimator, or seal.

## R1 reopening gate — 2026-08-16

This section implements the completion test in
`docs/program_reopening_note_2026-07-31.md` for R1. It does not reopen EF-0--EF-8
and does not promote any R2 result.

- [x] **Return the reviewed manuscript to the authorized R1 branch without importing
  the later research history wholesale.**
  - R1 branch: `reopen/r1-r2-limits-writeup`.
  - Integration commit: `f26b8d75c69826b95173452515e9474079b4d14b`.
  - The commit contains only `docs/manuscript_limits_draft.md`, this checklist, and
    the manuscript `viz/` suite. No EF, C1, forum, August-roadmap, or new-test path
    is imported by that commit.
- [x] **Priority wording remains bounded.**
  - The reviewed manuscript explicitly disclaims novelty for textbook statistical
    machinery and avoids absolute priority language.
- [x] **Recheck the deterministic WP4 numerical reference used by the R1 contract.**
  - Committed reference implementation:
    `research_program/work_packages/wp4_kappa_numeric_reference.py`.
  - Re-execution of the committed calculation for the moderate reference diamond
    gives
    `V = 1.4717204319`,
    `I = 5.4152614727e-4`,
    `V*I = 7.9697509534e-4`, and
    `delta_tau/ell = 35.42237079`.
  - The small-patch log-log fits reproduce exponents `5.91684` (all points) and
    `5.98794` (smallest four). These are deterministic quadrature/discretization
    outputs, not exact values or certified error enclosures.
- [ ] **Make R2's unresolved part explicit in the manuscript itself.**
  - Current scientific state to state, without promotion:
    exponent `lambda^6` derived and numerically cross-checked within its documented
    shrinking-family scope; prefactor `OPEN / [UNVERIFIED]`.
  - R2's expired time box is not a scientific verdict and must not be presented as
    `FAILED` or `PROVED`.
- [ ] **Compile the exact current R1 manuscript to a self-contained PDF and inspect
  it.**
  - The compilation must use the current R1 commit, embed all six figures, and
    leave no repository-internal reference that an external reader must resolve in
    order to understand a claim.

Until the last two boxes are closed, R1 remains open. Neither box authorizes new
scientific calculations, new estimators, EF-4 work, or a change to the frozen seal.

## PR state

- [x] Scientific gate required before changing the manuscript PR from draft to
  ready: satisfied under the 2026-08-07 gate.
- [ ] Change the PR state only as an explicit maintainer action after the final
  R1 diff and remote commit are checked.

## arXiv preparation (editorial, non-blocking for the PR)

- [x] Proposed primary category: `gr-qc`. Its official scope includes quantum
  gravity, so it matches the manuscript's causal-set and gravitational focus.
- [ ] Decide whether the statistical content merits one cross-list to
  `math.ST`/`stat.TH`. The arXiv taxonomy states that `stat.TH` is an alias for
  `math.ST`; they are not two independent cross-list choices.
- [ ] Check the submitting author's account for `gr-qc` endorsement before the
  intended submission day. arXiv may require endorsement for a first submission
  or for a new category; the account/submission workflow determines whether it
  is needed.
- [ ] Build and compile the arXiv source bundle. The repository currently tracks
  the manuscript as Markdown plus PNG figures, not as a submission-ready TeX
  source package.
- [ ] Inspect the arXiv-generated PDF, metadata, author spelling, abstract,
  license, figure inclusion, and references before final submission.

Official references checked on 2026-08-07:

- [arXiv category taxonomy](https://arxiv.org/category_taxonomy)
- [Category cross-listing guidance](https://info.arxiv.org/help/cross.html)
- [Endorsement guidance](https://info.arxiv.org/help/endorsement.html)
- [Submission guidelines](https://info.arxiv.org/help/submit/index.html)

## ORCID (editorial, non-blocking)

- [ ] If José Ignacio Martín-Gandul has an ORCID iD, link it to the submitting
  arXiv account and add it to the manuscript metadata where appropriate.
- [x] Do not block scientific closure or PR readiness on ORCID. arXiv encourages
  authors to link an ORCID iD but does not list it as a submission requirement.

Official reference checked on 2026-08-07:
[arXiv ORCID guidance](https://info.arxiv.org/help/orcid.html).
