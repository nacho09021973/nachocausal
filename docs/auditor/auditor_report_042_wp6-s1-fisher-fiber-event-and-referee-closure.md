# Auditor Report 042 — wp6-s1-fisher-fiber-event-and-referee-closure

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repository root `/home/adnac/nachocausal`, branch `emergencia/p1a-canal-sigma-m`, commit
`523883cc75c0518941bab2e706fe973c69d69509` ("Fix clean install dependencies for canonical tests"),
worktree clean.

This report continues the WP6/S1 audit from the single point report 039 left open and does not
re-adjudicate closed ground. Two things are in scope:

1. **The Fisher fiber-event question.** Whether the `O(N^{-1})` exceptional probability used in the
   Fisher-retention chain may be attributed to the event "the whole incomparability graph is
   prime", whether the primary source supports that attribution, and whether the internal
   fiber theorem sustains the retention as declared.
2. **The referee dependencies still open at HEAD**, above all the one report 039 named explicitly:
   `PDF_COMPILED=NO`.

Areas already adjudicated — the Kurečka positioning (039 §4.2), the deterministic
modular/Gallai fiber argument (039 §4.4), the Lean evidence (037, 038), and the provenance
remediation (040, 041) — were **not** reopened, with one deliberate exception: the
Bouvel–Chauve–Mishna–Rossin source was re-read, because a concrete contradiction between two
committed artifacts had to be resolved. No test suite was re-run.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh`, exit `0`:

```text
Auditor: 0 error(s), 0 warning(s)
```

`git status --short` is empty; the worktree is clean at `523883c`.

The regression suite was **not** re-executed under the standing instruction. The last recorded
state is report 041's `456 passed, 0 failed` at `db13f98`; three commits have landed since
(`3ca46fe`, `9a0c04b`, `523883c`), all touching tests/packaging only. `TESTS_RERUN=NO` is recorded
honestly rather than a green result being asserted.

## 3. Seal & freeze integrity

`sha256sum nachocausal/thresholds.py` →
`6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, and the mechanical audit
confirms that SHA is recorded across the freeze chain (`docs/preregistration_002.md`,
`docs/preregistration_003.md`, the auditor/comité series). This is the same `6e2c3888…` carried
since report 037: **no drift**. No commit in scope touches `nachocausal/thresholds.py`, a
preregistration, a threshold, or a seed band; this audit committed nothing at all (§5).

## 4. Reproducibility of published numbers

Two questions are in scope, and neither is a new data run: the Fisher fiber-event attribution
(§4.1) and the referee's remaining dependencies (§4.2).

### 4.1 The Fisher fiber-event question

#### 4.1.1 The contradiction

Two committed artifacts state the high-probability event differently.

**Manuscript (live, `f752bab`, unchanged at HEAD)** —
`research_program/synthesis/wp6_s1_finite_causal_order_manuscript.tex:330`:

> Let \(\mathcal G_N\) be the event that the strong interval tree of \(\Pi_N\) has a prime root and
> that every child of the root is either a leaf or a twin […] **This is not the event that the whole
> incomparability graph is prime: twins are allowed.**

**Outline (`PAPER_SKELETON_DRAFT / INTERNAL_ONLY / NOT_FROZEN`)** —
`research_program/synthesis/wp6_s1_finite_causal_order_paper_outline.md:2701-2708`:

> \(\mathcal G_N\) is taken to be **exactly this primality event** […] the complementary event —
> the incomparability graph **failing to be prime** […] has probability \(O(N^{-1})\) under the
> uniform reference law, by the average-case analysis of Bouvel, Chauve, Mishna and Rossin […]
> whose Theorem 2, via their Lemma 1, bounds exactly this exceptional probability.

The same file records `APPENDIX_E_EXTERNAL_FIBER_DEPENDENCY = CLOSED_WITH_EXPLICIT_CITATION`
(`:2712`), so the false version is carried under a closure token.

#### 4.1.2 Primary source, verbatim

Source re-fetched: M. Bouvel, C. Chauve, M. Mishna, D. Rossin, *Average-case analysis of perfect
sorting by reversals*, CPM 2009, <https://www.cecm.sfu.ca/~cchauve/Publications/CPM09.pdf>.
SHA256 `4b401a95588a1ccfc30697ab5f95626c8b79b226177563582493342deb576290` — **byte-identical to the
PDF report 039 checked**, so the two audits are reading the same document. Text extracted with
`pdftotext -layout`.

Theorem 2, verbatim:

```text
Theorem 2. Asymptotically, with probability 1, a random permutation σ of size
n has a strong interval tree such that the root is a prime vertex and every child
of the root is either a leaf or a twin. Moreover the probability that TS(σ) has
such a shape with exactly k twins is 2^k/(e^2 k!).
```

Proof of Theorem 2, verbatim:

```text
Lemma 1 with c = 1 gives that the proportion of non-simple permutations with
common intervals of size greater than or equal to 3 is O(n^-1). But permutations
whose common intervals are only of size 1, 2 or n are exactly permutations whose
strong interval tree has a prime root and every child is either a leaf or a twin.
```

And, decisively, the **same paper's Equation (1)**, quoting Albert–Atkinson–Klazar:

```text
sn = n!/e^2 (1 - 4/n + 2/(n(n-1)) + O(1/n^3))   when n → ∞.            (1)
```

Three consequences, all from the source itself:

- The event whose complement is `O(n^{-1})` is **prime root with leaf-or-twin children**, i.e.
  "all common intervals have size 1, 2 or n". Twins are permitted.
- "The whole incomparability graph is prime" is the same thing as "σ is simple", which is the
  `k = 0` case of Theorem 2's own twin count. Its limiting probability is `2^0/(e^2 0!) = e^{-2}`.
- Equation (1) states it directly: `s_n/n! → e^{-2} = 0.1353353`.

Therefore the complement of the primality event has probability `→ 1 - e^{-2} = 0.8646647`. That is
`Θ(1)`, **not** `O(N^{-1})`.

#### 4.1.3 The repository's own numbers refute the outline

`research_program/work_packages/wp6_d2_modular_fiber_score.md:1457` carries the committed
brute-force enumeration up to `N = 9`. Its `k`-twin columns are exactly Bouvel's counting formula
`s_{N-k} · C(N-k, k) · 2^k`; summing them reproduces `|A_N|` with no residue:

| `N` | `Σ_k s_{N-k} C(N-k,k) 2^k` | `\|A_N\|` in the table | match |
|---:|---:|---:|:--|
| 4 | 2 | 2 | yes |
| 5 | 22 | 22 | yes |
| 6 | 154 | 154 | yes |
| 7 | 1194 | 1194 | yes |
| 8 | 10930 | 10930 | yes |
| 9 | 111194 | 111194 | yes |

Its `k = 0` column is `2, 6, 46, 338, 2926, 28146` — the simple-permutation sequence, i.e. exactly
the permutations whose whole incomparability graph is prime. So the repository already holds the
refuting numbers:

| `N` | `P(graph prime)` | AAK Eq. (1) prediction | `P(A_N)` | `P(A_N^c)` |
|---:|---:|---:|---:|---:|
| 4 | 0.08333 | 0.02256 | 0.08333 | 0.91667 |
| 5 | 0.05000 | 0.04060 | 0.18333 | 0.81667 |
| 6 | 0.06389 | 0.05413 | 0.21389 | 0.78611 |
| 7 | 0.06706 | 0.06445 | 0.23690 | 0.76310 |
| 8 | 0.07257 | 0.07250 | 0.27108 | 0.72892 |
| 9 | 0.07756 | 0.07895 | 0.30642 | 0.69358 |

`P(graph prime)` is heading to `e^{-2} = 0.1353`, not to 1, and tracks Equation (1) to within the
stated `O(n^{-3})` from `N = 7` on. `P(A_N)` rises monotonically toward 1, as Theorem 2 requires.
No new enumeration was run; only arithmetic on committed table entries and the published
asymptotic.

#### 4.1.4 The internal theorem that carries the load

`research_program/work_packages/wp6_d2_modular_fiber_score.md:1326` defines

```text
A_N(π):  the root of the strong interval tree is prime, and
         every child of the root has size one or two.
```

which is Bouvel's Theorem 2 event verbatim (a size-two child is a twin — the bridge to modules is
made explicitly at `:1290-1340` via Habib–Paul, *A survey of the algorithmic aspects of modular
decomposition*, CSR 4 (2010), Lemma 20, and not by decree). Then, at `:1347`:

> **Teorema 4 (fibra de raíz prima con hojas y twins).** Si `A_N(π)`, entonces
> `F_N([P_π]) = {π, π^{-1}}`.

This is strictly stronger than the primality version: it delivers the two-element fiber on the
**whole** typical event, twins included, which is exactly the event the source's `O(N^{-1})` bound
covers. Its proof (`:1347-1440`) transports the isomorphism to canonical maximal strong modules,
contracts, applies Gallai's two-orientation uniqueness on the prime quotient, and closes the
internal patterns `{1, 12, 21}` — `12` induces a chain and `21` an antichain, so an isomorphism
cannot exchange them, and all three are involutions so the inverse-of-an-inflation identity returns
`π^{-1}`. The independent falsifier at `:1440-1456` reports `violaciones = 0` across all `62003`
classes for `4 ≤ N ≤ 9`, and explicitly refutes the tempting "independent twin flips" fiber
(`INDEPENDENT_TWIN_FLIPS_IN_ORIENTED_FIBER = REFUTED`, `:1612`).

The retention chain needs only *conditional variance zero*, which needs the score constant on the
fiber. For symmetric `f`, `H^{(N)}(f)` is symmetric, so `S_N^Π(f)(σ) = S_N^Π(f)(σ^{-1})`
(manuscript `(E.2)`, `(E.3)`); a fiber contained in `{π, π^{-1}}` is therefore sufficient. Teorema 4
supplies it on all of `A_N = 𝒢_N`, and `(E.16)`–`(E.19)` then run unchanged.

#### 4.1.5 Adjudication

Against the three options put to this audit:

- **The Fisher retention claim itself — option 1, fully saved.** `(E.15)`–`(E.19)`, Theorem 4 of the
  manuscript, `q_N → 1` in the WP, and Theorem 8 of `wp6_d2_geometric_fisher_retention.md` all rest
  on the wider event `𝒢_N = A_N`, which is the source's event, and on internal Teorema 4, which
  proves the two-element fiber on that whole event. Nothing needs weakening, and the constants
  `C_fib`, `N_fib` are correctly declared as unspecified existentials inherited from the source.
- **The outline's Appendix E draft sentence — option 3, it fails mathematically.** It is not a
  citation slip that a corrected attribution would repair. As written, `𝒢_N` is the primality
  event, and the assertion that its complement is `O(N^{-1})` is **false**: that complement has
  probability `→ 1 - e^{-2} ≈ 0.865`. The refutation comes from the cited paper's own Equation (1)
  and from the repository's own committed enumeration table.
- **The retention is saved only through the internal theorem, not through the narrower event.** If
  one insisted on the primality event, the deterministic half would still hold but the
  probabilistic half would collapse, and `Δ_N(f,f) = o(N)` would not follow. Teorema 4 is load-
  bearing, not decorative.

The live manuscript is unaffected: it already carries the correct event, the correct
non-identification ("This is not the event that the whole incomparability graph is prime"), and the
correct proof over twins. The defect is confined to a committed **internal, not-frozen draft** that
the manuscript superseded at `f752bab` and that was never brought into line — and which still
carries `APPENDIX_E_EXTERNAL_FIBER_DEPENDENCY = CLOSED_WITH_EXPLICIT_CITATION` over the false text.

```text
E15_PRIMARY_SOURCE_EVENT          = PRIME_ROOT_WITH_LEAF_OR_TWIN_CHILDREN
E15_PRIMALITY_EVENT_PROBABILITY   = e^-2 (NOT 1 - O(N^-1))
E15_MANUSCRIPT_EVENT_MATCH        = PASS
E15_OUTLINE_EVENT_MATCH           = FAIL_MATHEMATICALLY
INTERNAL_THEOREM_SUSTAINS_RETENTION = YES (Teorema 4, wp6_d2_modular_fiber_score.md:1347)
FISHER_RETENTION_CLAIM            = FULLY_SAVED
```

### 4.2 Remaining referee dependencies

No referee dossier is committed anywhere in the history
(`git log --all --name-only | grep -i referee` returns only report 039 itself), so the dependency
list below is reconstructed from the explicit open items in the committed record, not from the
referee's own wording. That reconstruction is stated as such and not presented as a recovered list.

#### 4.2.1 `PDF_COMPILED` — was open, now CLOSED with findings

Report 039 §4.7 recorded `PDF_COMPILED=NO` because no TeX engine was installed, and §8 named a real
TeX build and PDF inspection as "the remaining technical publication control". Engines are now
present: `pdflatex`, `lualatex`, `xelatex` (no `latexmk`, no `tectonic`).

The build was performed in a disposable scratchpad directory from copies; **the project tree was
not modified and no build artifact was written into the repository**.

- `pdflatex` **fails**: `! pdfTeX error (font expansion): auto expansion is only possible with
  scalable fonts.` This is an environment defect — `microtype` expansion against non-scalable
  Type 1 bitmap fonts under `T1` encoding (`cm-super` absent) — **not** a manuscript error.
- `lualatex` → `bibtex` → `lualatex` → `lualatex` **succeeds**: exit `0`, `ms.pdf` produced,
  **35 numbered pages**, **zero** LaTeX errors, **zero** undefined references, **zero** undefined
  citations, `20` `\bibitem`s rendered (matching the 20 cited keys report 039 counted).
- `bibtex` emits two field warnings, both cosmetic: `there's a number but no volume in
  CrudeleDukesNoel2024`; `empty publisher in Pollard2013`.
- **Three `Overfull \hbox` warnings, and all three truncate visible content at the page edge.**
  Confirmed by rendering the pages to images and reading them, not inferred from the log:

  | `.tex` line | Overfull | PDF page | What is cut off |
  | --- | ---: | ---: | --- |
  | `:61` | 260.1 pt | 2 | The boxed one-line statement of the paper's contribution ends mid-word: "…we identify exactly what survives the quotien" |
  | `:258` | 133.0 pt | 18 | Equation (11.4), the Conclusion's three-layer summary box: "…higher-order detectability = r_N(γ_ψ) = 2 for the expl" |
  | `:377` | 97.4 pt | 32 | An Appendix G display loses a term: "…= M_1(11)M_2(22) − 2M_1(12)M_2(12) + M_1(22)M_2" |

  The third is the most serious: **mathematical content, not just prose, is lost off the right
  margin.** All three are single-line `\[ … \]` displays too wide for the `1in`-margin `article`
  text block; none is a mathematical error, and none affects any theorem. They are publication
  blockers, not scientific ones.

```text
PDF_COMPILED              = YES (lualatex; pdflatex blocked by a missing scalable-font package)
PDF_PAGES                 = 35
PDF_LATEX_ERRORS          = 0
PDF_UNDEFINED_REFS        = 0
PDF_UNDEFINED_CITATIONS   = 0
PDF_BIBITEMS              = 20
PDF_CONTENT_TRUNCATIONS   = 3   (tex :61, :258, :377 → pages 2, 18, 32)
```

#### 4.2.2 Dependencies closed since report 039, verified not reopened

- **W-17, unclean worktree** — CLOSED. `git status --short` is empty at HEAD.
- **23 provenance warnings** — CLOSED at `b5f93b4`/`db13f98`; the mechanical audit at HEAD is
  `0 error(s), 0 warning(s)` and report 041 §4 proved by execution that the registry, not a
  literal fallback, produces it.
- **Report 041's three residual WARNs** (`*_test.ipynb`, `conftest.py`, `test/`, `mytests/`
  escaping the fallback deny-list, and no test pinning the list) — CLOSED at `9a0c04b`.
  `.claude/skills/auditor/audit.sh:112-124` now denies `tests/`, `test/`, `mytests/`, `.claude/`,
  `docs/`, `provenance/` as path prefixes and `conftest.py`, `test_*`, `*_test`, `*_test.*` as
  basenames; `*_test.ipynb` is covered by `*_test.*`.
- **W-16, Lean ledger token breadth** — CLOSED at `33d712d`, verified in report 038 and unchanged:
  `FORMALIZATION_STATUS.md:268-291` now splits the token and retires the over-broad one.

#### 4.2.3 Dependencies that remain open at HEAD

| # | Item | State | Note |
| --- | --- | --- | --- |
| D1 | Outline Appendix E draft carries a false probabilistic statement under a closure token | **OPEN — this report's only substantive finding** | `…paper_outline.md:2701-2712`; internal, `NOT_FROZEN`; live manuscript already correct |
| D2 | Three PDF content truncations | **OPEN** | §4.2.1; publication blocker, one loses a formula term |
| D3 | `pdflatex` cannot build the manuscript in this environment | **OPEN (environmental)** | `cm-super` / scalable-font package absent; `lualatex` unaffected |
| D4 | `THEOREM_C_GRAM_RANK = NOT_FORMALIZED`, `BERNSTEIN_TRANSPORT_TO_VN = NOT_FORMALIZED` | **OPEN BY DESIGN** | Correctly declared in the ledger; not a mismatch, and the manuscript makes no Lean claim |
| D5 | `EXACT_COMMANDS_DOCUMENTED = 21/23` | **OPEN BY DESIGN** | Two rows `NOT_DOCUMENTED`; no command was invented; distinct from `PROVENANCE_CONFIRMED = 23/23` |
| D6 | Two `bibtex` field warnings | **OPEN (cosmetic)** | `CrudeleDukesNoel2024` number-without-volume; `Pollard2013` empty publisher |
| D7 | Regression suite not re-run at HEAD | **NOT VERIFIED THIS PASS** | Standing instruction; last recorded green is 041's `456 passed` at `db13f98` |

## 5. dev/validation separation & ground-truth leakage

Nothing was committed, no threshold or seed band was touched, and the TeX build ran entirely on
copies in the session scratchpad. `dev/` was read only as documentary provenance. No embedding or
ground-truth access was created. **No separation or leakage defect found.**

## 6. Claim-boundary check

No claim text was changed by this audit. The manuscript's ceiling is unchanged from report 039
§6 and was not re-derived. One boundary observation belongs here: this report's finding D1 is a
defect in an **internal draft**, and the internal-draft status must not be used to soften it —
`APPENDIX_E_EXTERNAL_FIBER_DEPENDENCY = CLOSED_WITH_EXPLICIT_CITATION` asserts a closure over text
that is mathematically false, which is precisely the shape of claim the founding rules forbid.
Equally, the defect must not be inflated: it does not touch the manuscript, any theorem, or any
published number.

## 7. Findings

| # | Severity | Finding | Anchor |
| --- | --- | --- | --- |
| 1 | **WARN** | **Outline Appendix E identifies `𝒢_N` with the primality event and attributes `O(N^{-1})` to its complement. This is mathematically false, not a mis-citation**: the primality event is "σ simple", whose probability tends to `e^{-2} ≈ 0.135`, so its complement tends to `≈ 0.865`. Refuted by the cited paper's own Equation (1) and by the repository's own enumeration. Carried under `APPENDIX_E_EXTERNAL_FIBER_DEPENDENCY = CLOSED_WITH_EXPLICIT_CITATION`. Internal, `NOT_FROZEN`, superseded by the manuscript — hence WARN, not ERROR. | `…paper_outline.md:2701-2712`; CPM09 Eq. (1); `wp6_d2_modular_fiber_score.md:1457` |
| 2 | **WARN** | **Three overfull displays truncate content off the right page edge in the compiled PDF** — the contribution statement (p. 2), Conclusion Eq. (11.4) (p. 18), and an Appendix G display that loses a term of an equation (p. 32). Confirmed by reading the rendered pages. | manuscript `:61`, `:258`, `:377`; `lualatex` log; pages 2, 18, 32 |
| 3 | OK | **Primary source verified verbatim and byte-identical to report 039's copy.** Theorem 2's event is prime root with leaf-or-twin children; its proof derives `O(n^{-1})` from Lemma 1 with `c=1`; twins are explicitly permitted. | CPM09 SHA256 `4b401a95…`; Theorem 2 and its proof, quoted §4.1.2 |
| 4 | OK | **The manuscript states the event correctly and explicitly disowns the primality reading.** No repair needed in the live artifact. | manuscript `:330` |
| 5 | OK | **Internal Teorema 4 sustains the declared retention**, delivering `F_N([P_π]) = {π, π^{-1}}` on the whole event `A_N` including twins — strictly stronger than the primality version and exactly matched to the source's bound. | `wp6_d2_modular_fiber_score.md:1326`, `:1347` |
| 6 | OK | **The committed enumeration reproduces Bouvel's counting formula exactly** — `Σ_k s_{N-k}C(N-k,k)2^k = \|A_N\|` for `N = 4..9`, with `violaciones = 0` across `62003` classes. Independent corroboration of both the source bridge and Teorema 4. | `wp6_d2_modular_fiber_score.md:1440-1456`; §4.1.3 |
| 7 | OK | **Fisher retention chain intact.** Symmetric `f` gives `S_N^Π(f)(σ) = S_N^Π(f)(σ^{-1})`, so a fiber inside `{π,π^{-1}}` forces conditional variance zero; `(E.16)`–`(E.19)` and Theorem 8 follow unchanged. | manuscript `(E.2)`, `(E.3)`, `(E.15)`–`(E.19)`; `wp6_d2_geometric_fisher_retention.md` §3.3 |
| 8 | OK | **PDF now compiles**: `lualatex` + `bibtex`, exit `0`, 35 pages, 0 errors, 0 undefined refs, 0 undefined citations, 20 bibitems. Report 039's `PDF_COMPILED=NO` is closed. | §4.2.1 |
| 9 | OK | **Report 041's three residual WARNs are closed** at `9a0c04b`; the deny-list now covers `test/`, `mytests/`, `conftest.py`, and `*_test.*` (hence `.ipynb`). | `audit.sh:112-124`; `git show --stat 9a0c04b` |
| 10 | OK | Seal intact (`6e2c3888…`), mechanical audit `0/0` at HEAD, worktree clean, W-17 and W-16 remain closed, Lean ledger unchanged and correctly bounded. | §2–§3, §4.2.2 |
| 11 | OK | Nothing was committed, no test re-run, no threshold or seed touched; the TeX build ran on scratchpad copies only. | §5 |

AUDIT_ERRORS=0
AUDIT_WARNINGS=2

## 8. Verdict

The Fisher question is settled, and it splits.

**The retention claim is fully saved.** The event the manuscript uses is the event the primary
source actually bounds — prime root with leaf-or-twin children — and the internal Teorema 4 proves
the two-element fiber on all of it, twins included. The repository's own enumeration reproduces
Bouvel's counting formula exactly to `N = 9` with zero violations, so the deterministic half is
corroborated as well as proved. `(E.16)`–`(E.19)`, manuscript Theorem 4, and Theorem 8 of the
geometric retention WP stand without any weakening, and the unspecified constants `C_fib`, `N_fib`
are correctly declared as inherited existentials.

**The outline's version of the same appendix does not survive, and it is not rescued by fixing the
attribution.** Identifying `𝒢_N` with "the whole incomparability graph is prime" makes the
`O(N^{-1})` statement false, by a factor that does not vanish: that event has limiting probability
`e^{-2} ≈ 0.135`, not `1 - O(N^{-1})`. The cited paper refutes it in its own Equation (1), and the
repository refutes it in its own committed table. The correct reading is that Teorema 4 is
load-bearing: it is what lets the argument use the wide event the source can actually bound. The
live manuscript already says all of this; the internal draft was simply never brought into line and
still carries a closure token over the false text.

On the referee's remaining dependencies, the one report 039 named explicitly is now closed: the
manuscript compiles under `lualatex` to a 35-page PDF with zero errors, zero undefined references
or citations, and a complete 20-entry bibliography. The inspection that closure enables immediately
earned its keep — three displays run off the right page edge, and one of them drops a term from an
equation in Appendix G. That is a publication blocker, found by looking at the pages rather than at
the log.

Two warnings, no errors. Neither touches a theorem, a published number, the seal, or the claim
ceiling. Remediation of both is the user's call; this auditor applied none.

```text
FISHER_RETENTION_CLAIM              = FULLY_SAVED
E15_MANUSCRIPT_EVENT_MATCH          = PASS
E15_OUTLINE_EVENT_MATCH             = FAIL_MATHEMATICALLY
INTERNAL_THEOREM_SUSTAINS_RETENTION = YES
PDF_COMPILED                        = YES
PDF_CONTENT_TRUNCATIONS             = 3
TESTS_RERUN                         = NO
SEAL_DRIFT                          = NONE
AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
AUDIT_ERRORS=0
AUDIT_WARNINGS=2
```
