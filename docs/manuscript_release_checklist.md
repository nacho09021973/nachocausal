# Manuscript release checklist

Status date: 2026-08-07

Code-and-manuscript commit tested: `ab038a88836083276f17406e2537463189e79967`

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

The only scientific/technical blocker among the three exit items is therefore
closed. This checklist is documentation-only and does not modify the tested
code, fixture, estimator, or seal.

## PR state

- [x] Scientific gate required before changing the manuscript PR from draft to
  ready: satisfied.
- [ ] Change the PR state only as an explicit maintainer action after the final
  diff and remote commit are checked.

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
