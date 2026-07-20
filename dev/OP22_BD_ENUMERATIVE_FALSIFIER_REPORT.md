# OP-2.2 BD enumerative falsifier report

STATUS: DEV_REPORT / CLAIM_INERT / NO_OP22_TERMINAL
DATE: 2026-07-19
SCOPE: Read-only execution of the frozen PR011 enumerator for the OP-2.2 BD-action support question.

## 1. Authorization and boundary

This note records the single read-only OP-2.2 falsifier run identified in
`docs/marcador_reentrada_2026-07-19.md`.

It does not:

- open OP-2.2;
- draft or freeze a preregistration;
- execute Monte Carlo;
- consume seeds;
- write `data/reports/` artifacts;
- touch the sealed validation path;
- emit an OP-2.2 terminal.

The only code path used was the frozen PR011 enumerator:
`dev/pr011_tv_certification_enumeration.py`.

## 2. Environment and seal

Interpreter and numeric environment:

```text
.venv/bin/python
Python 3.12.3
numpy 1.26.4
```

Post-run seal check:

```text
thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4
```

Post-run working-tree check:

```text
## main...origin/main
?? nachocausal-program.local-before-pull.html
```

After this report is added, this report itself is the only intended new tracked candidate. The
pre-existing untracked `nachocausal-program.local-before-pull.html` was not touched.

## 3. Frozen falsifier output

Command:

```text
.venv/bin/python dev/pr011_tv_certification_enumeration.py falsifier
```

Output:

```text
PR011_ENUM_FALSIFIER=OK
n=4 grid_m=20
tau_pair=(0.95, 1.05)
raw_mass_sum=(0.527706552060, 0.527925458372)
mass_sum=(1.000000000000, 1.000000000000)
n_poset_classes=24
TV=0.001330364764505
TV_certified_upper=0.001330364765
falsifier_verdict=PAIR_DISTINGUISHABLE_TV_POSITIVE
```

Interpretation: under the frozen enumerator at `n=4`, `grid_m=20`, the two PR011 laws are not
identical. This is a read-only falsifier/probe result, not a new PR011 certification artifact.

## 4. BD action convention checked on the enumerated support

Formula:

```text
S(C) = N - 2*N1 + 4*N2 - 2*N3
```

where `N=4` and `Ni` counts inclusive order intervals of cardinality `i+1`.

On the support returned by the frozen enumerator:

```text
support_classes=24
S_min=-6
S_max=6
S_values=[-6, -4, -2, 0, 2, 4, 6]
```

Thus the support-level normalization convention for this run is:

```text
f(C) = (S(C) + 6) / 12
```

No clipping is needed for this enumerated support.

## 5. Support-restricted non-collapse versus relation count

The support-restricted map `S(C)` does not collapse to a function of `|relations(C)|` under the
frozen enumerator.

Observed support mapping:

```text
rel=0: [4]
rel=1: [2]
rel=2: [0]
rel=3: [-2, 4]
rel=4: [-4, 2]
rel=5: [-6, 6]
rel=6: [4]
support_restricted_collapse_to_relation_count=False
```

Non-collapse witnesses exist at relation counts 3, 4, and 5. This discharges the enumerative
support-restricted version of the dossier's V2 question for the frozen `grid_m=20` support: the
BD action is not merely `f_bench = |relations|/6` in disguise on that support.

Boundary: this is an enumerator-support statement, not an analytic theorem about the exact
continuum law.

## 6. Normalized BD gap and algebraic residual

Using `f(C)=(S(C)+6)/12` on the same normalized enumerated laws:

```text
E_tau0_f=0.582761108990414
E_tau1_f=0.582790373614537
g_abs_mean_gap=0.000029264624123
global_tv=0.001330364764505
```

The mean witness gap is positive but small: `g ≈ 2.93e-5`.

Conditioning by relation count gives:

```text
rel=0 mass_tau0=0.034990381698 mass_tau1=0.034826684860 cond_tv_S=0.000000000000000
rel=1 mass_tau0=0.108461415086 mass_tau1=0.108014219092 cond_tv_S=0.000000000000000
rel=2 mass_tau0=0.191743912351 mass_tau1=0.191235343301 cond_tv_S=0.000000000000000
rel=3 mass_tau0=0.248476428126 mass_tau1=0.248347916294 cond_tv_S=0.000255262256856
rel=4 mass_tau0=0.223719483655 mass_tau1=0.224118380471 cond_tv_S=0.000090417675602
rel=5 mass_tau0=0.143062135652 mass_tau1=0.143637838090 cond_tv_S=0.000084855933871
rel=6 mass_tau0=0.049546243432 mass_tau1=0.049819617891 cond_tv_S=0.000000000000000
weighted_conditional_residual_tv_lower_component=0.000095761716420
```

Interpretation:

- `V2-support`: positive — support-restricted non-collapse is observed.
- `V4a ALGEBRAIC_NONREDUNDANCY`: positive but tiny under this enumerated proxy.
- `V4b HORIZON_FIDELITY`: unchanged from the dossier — structurally not constructible inside
  PR011 because the family hard-freezes straddling placement and exposes no exterior-only /
  horizon-placement axis.

## 7. Disposition

This run resolves the small finite enumerative question that was left open in the reentry marker:
the frozen enumerator does not collapse the BD action to relation count on its `n=4` support.

The result is not strong enough to promote BD into a horizon witness. The admissible ceiling
remains:

```text
REFERENCE_WITNESS_SEPARATION_ONLY
```

The practical cost implication is severe if one uses the empirical mean-gap route: substituting
`g ≈ 2.93e-5` into the OP-2.1 Hoeffding radius formula would require orders of magnitude more
samples than the dossier's already-large best-case table. Exact enumeration remains the only
reasonable way to use this bench.
