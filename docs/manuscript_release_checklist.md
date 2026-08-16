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
- [x] **Make R2's unresolved part explicit in the manuscript itself.**
  - Verified manuscript commit:
    `265a9538d16171b0403fdd63a7e6f3a530d3878e`.
  - §7.2 now states, without promotion, that the `lambda^6` exponent is derived and
    numerically cross-checked within its documented shrinking-family scope, while
    the multiplicative prefactor remains `OPEN / [UNVERIFIED]`.
  - The text also states explicitly that expiry of the R2 time box is an
    administrative handoff to R1, not a scientific verdict and not `FAILED` or
    `PROVED`.
- [x] **Compile the exact current R1 manuscript to a self-contained PDF and inspect
  it.**
  - Source commit compiled:
    `265a9538d16171b0403fdd63a7e6f3a530d3878e`.
  - GitHub Actions run: `31950827078`; inspection artifact: `9264605989`.
  - PDF SHA256:
    `0c5038b36f5f9735032978e3cd34f3a8a20f800419ebc4aafafdc5ba24a2ba14`.
  - Output: 30 A4 pages, PDF 1.5, unencrypted; Poppler reports six embedded RGB
    figure images (plus their transparency masks).
  - Visual render inspection covered the complete 30-page contact sheet and the
    six figure pages plus §7.2. No clipped text, overlaps, broken glyphs, or missing
    figures were found.
  - Text extraction confirms the R2 `OPEN / [UNVERIFIED]` statement in the PDF.
  - The repository-token scan finds only the optional historical archive labels
    `COM-*`, `X0-Qn`, and `TF-*` in §5. Their outcomes and lessons are stated in the
    manuscript itself, so an external reader does not need to resolve those labels
    to understand any scientific claim.

**R1 completion status:** `CLOSED / COMPLETION_TEST_PASSED_2026-08-16`.
The two final reopening-gate obligations are satisfied. This closure does not
promote R2, reopen EF-0--EF-8, authorize EF-4 work, alter the frozen seal, or
change the scientific scope of the manuscript.

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
