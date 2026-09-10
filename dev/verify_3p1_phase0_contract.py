"""EXPLORATION (dev/) — Paper III, Phase 0: Gate-0 contract verifier.

Read-only audit of the four inputs listed in docs/hoja_de_ruta_paper_iii.md.
Runs NO sweep and produces NO new observable: it re-derives every stored
identity from the committed artifacts, exercises the three chain-length
implementations on an explicit 3-element poset, and audits the point process
of the interval generator against the exact Alexandrov density.

Complements dev/verify_3p1_notes_figures.py, which checks notes-vs-JSON only.
This one checks JSON-vs-itself, code-vs-code, and generator-vs-measure.

Run:  python3 dev/verify_3p1_phase0_contract.py
Exit: 0 iff every structural check passes. Findings are reported either way;
      an open finding is a Gate-0 blocker, not a script failure.
"""

from __future__ import annotations

import json
import sys
from math import e, gamma

import numpy as np

sys.path.insert(0, "dev")
sys.path.insert(0, ".")

PREC = "dev/explore_3p1_bg_reference_precision_results.json"
BASE = "dev/explore_3p1_bg_reference_results.json"
CAL = "dev/explore_3p1_scale_calibration_results.json"

# Declared audit seeds. Used ONLY by the generator-measure audit (G0-C), never
# by any leg that produces a reported figure.
AUDIT_SEEDS = (101, 102, 103)
AUDIT_ACCEPT_SEED = 999

failures: list[str] = []
findings: list[str] = []


def check(label: str, ok: bool) -> bool:
    print(f"  {'OK      ' if ok else 'FAIL    '}  {label}")
    if not ok:
        failures.append(label)
    return ok


def slope(x, y) -> float:
    return float(np.polyfit(np.log(x), np.log(y), 1)[0])


# ---------------------------------------------------------------------------
def audit_internal_consistency() -> None:
    print("\n[A] internal consistency: every stored aggregate re-derived from its raw Ls")
    prec, base, cal = (json.load(open(p)) for p in (PREC, BASE, CAL))

    for tag, obj in (("precision", prec), ("base", base)):
        ok = True
        for r in obj["rows"]:
            Ls = np.asarray(r["Ls"], dtype=float)
            ok &= abs(Ls.mean() - r["mean_L"]) < 1e-12
            ok &= abs(Ls.mean() / r["N"] ** 0.25 - r["L_over_N_quarter"]) < 1e-12
            if "sem_L" in r:
                ok &= abs(Ls.std(ddof=1) / np.sqrt(Ls.size) - r["sem_L"]) < 1e-12
            if "n_seeds" in r:
                ok &= r["n_seeds"] == Ls.size == len(obj["seeds"])
        check(f"{tag} leg: mean_L, sem_L, L/N^(1/4) reproduce the stored Ls", ok)

    Ns = [r["N"] for r in prec["rows"]]
    Lm = [r["mean_L"] for r in prec["rows"]]
    loc = [np.log(Lm[i + 1] / Lm[i]) / np.log(Ns[i + 1] / Ns[i]) for i in range(len(Ns) - 1)]
    check("precision leg: local_slopes reproduce the row means", np.allclose(loc, prec["local_slopes"]))
    check(
        "base leg: global_slope reproduces the row means",
        abs(slope([r["N"] for r in base["rows"]], [r["mean_L"] for r in base["rows"]]) - base["global_slope"]) < 1e-12,
    )

    rhos = cal["rho_sweep"]
    agg = {}
    for k in ("mean_V_all", "mean_L_all", "mean_V_min", "mean_L_min"):
        agg[k] = [float(np.mean([r[k] for r in cal["rows"] if r["rho"] == rho])) for rho in rhos]
    want = {
        "logV_all_vs_logrho": slope(rhos, agg["mean_V_all"]),
        "logL_all_vs_logrho": slope(rhos, agg["mean_L_all"]),
        "logL_vs_logV_all": slope(agg["mean_V_all"], agg["mean_L_all"]),
        "logV_min_vs_logrho": slope(rhos, agg["mean_V_min"]),
        "logL_min_vs_logrho": slope(rhos, agg["mean_L_min"]),
        "logL_vs_logV_min": slope(agg["mean_V_min"], agg["mean_L_min"]),
    }
    check("box leg: all six stored slopes reproduce the row means",
          all(abs(want[k] - cal["slopes"][k]) < 1e-9 for k in want))
    check("box leg: replica count is the declared seed list at every rho",
          all(len([r for r in cal["rows"] if r["rho"] == rho]) == len(cal["seeds"]) for rho in rhos))
    check("box leg: every realised N lies within 6 sigma of Poisson(rho * V_box)",
          all(abs(r["N"] - r["rho"]) < 6 * np.sqrt(r["rho"]) for r in cal["rows"]))


# ---------------------------------------------------------------------------
def audit_chain_conventions() -> None:
    print("\n[B] chain-length convention: three implementations on ONE explicit 3-chain")
    from explore_3p1_bg_reference import longest_chain_endpoint_to_endpoint
    from explore_3p1_scale_calibration import longest_future_chain
    from nachocausal.estimator import estimate_O

    # a < b < c, as a future matrix and as the sealed past matrix.
    fut = np.zeros((3, 3), dtype=bool)
    fut[0, 1] = fut[0, 2] = fut[1, 2] = True
    past = fut.T.copy()

    box_L = longest_future_chain(fut, np.array([0, 1, 2]))
    sealed_L = estimate_O(past)[2]
    # Three points on the t-axis inside the unit diamond: a genuine 3-chain.
    pts = np.array([[0.25, 0.0, 0.0, 0.0], [0.50, 0.0, 0.0, 0.0], [0.75, 0.0, 0.0, 0.0]])
    interval_L = longest_chain_endpoint_to_endpoint(pts, 1.0)

    print(f"      sealed   nachocausal/estimator.py       Lfut = {list(map(int, sealed_L))}  -> maximal element = 1  (VERTICES)")
    print(f"      interval dev/explore_3p1_bg_reference   L    = {interval_L}              -> 3-chain = 3          (VERTICES)")
    print(f"      box      dev/explore_3p1_scale_calib.   L    = {list(map(int, box_L))}  -> maximal element = 0  (EDGES)")

    check("sealed estimator uses the vertex convention (maximal element -> 1)", int(sealed_L[2]) == 1)
    check("interval leg agrees with the sealed vertex convention", interval_L == 3)
    ok = int(box_L[2]) == 0
    check("box leg DIVERGES from the sealed convention by exactly one", ok)
    if ok:
        findings.append(
            "G0-1 OPEN: dev/explore_3p1_scale_calibration.py:94 counts RELATIONS while "
            "nachocausal/estimator.py:47 and dev/explore_3p1_bg_reference.py:53 count ELEMENTS. "
            "dev/PAPER3_3P1_SCALE_NOTES.md sec.1 asserts a single frozen convention for both."
        )

    print("\n[C] the interval leg does not count the two Alexandrov endpoints p, q")
    prec = json.load(open(PREC))
    Ns = np.array([r["N"] for r in prec["rows"]], dtype=float)
    Lm = np.array([r["mean_L"] for r in prec["rows"]], dtype=float)
    print(f"      {'convention':<18}" + "".join(f"{int(n):>10d}" for n in Ns) + f"{'local slopes':>26}{'global':>9}")
    for off, name in ((0, "L   (as reported)"), (1, "L+1"), (2, "L+2 (with p, q)")):
        Q = (Lm + off) / Ns**0.25
        ls = [np.log((Lm + off)[i + 1] / (Lm + off)[i]) / np.log(Ns[i + 1] / Ns[i]) for i in range(len(Ns) - 1)]
        print(f"      {name:<18}" + "".join(f"{v:>10.4f}" for v in Q)
              + "  " + " ".join(f"{v:7.4f}" for v in ls) + f"{slope(Ns, Lm + off):9.4f}")
    g0, g2 = slope(Ns, Lm), slope(Ns, Lm + 2)
    check("endpoint convention shifts the global slope by more than 0.02", abs(g0 - g2) > 0.02)
    findings.append(
        f"G0-2 OPEN: the same artifact yields d log<L>/d log N = {g0:.4f} without the two Alexandrov "
        f"endpoints and {g2:.4f} with them. The reported departure from 1/4 is not "
        "convention-invariant at the N that were run."
    )


# ---------------------------------------------------------------------------
def audit_baselines_and_uncertainty() -> None:
    print("\n[D] box leg: seed-to-seed spread of each slope (absent from the notes)")
    cal = json.load(open(CAL))
    rhos = cal["rho_sweep"]
    spec = {
        "logV_all_vs_logrho": ("mean_V_all", None, "1 (exact)"),
        "logL_all_vs_logrho": ("mean_L_all", None, "1/4"),
        "logL_vs_logV_all": ("mean_L_all", "mean_V_all", "1/4"),
        "logV_min_vs_logrho": ("mean_V_min", None, "1  <-- see [E]"),
        "logL_min_vs_logrho": ("mean_L_min", None, "1/4  <-- see [E]"),
        "logL_vs_logV_min": ("mean_L_min", "mean_V_min", "1/4  <-- see [E]"),
    }
    print(f"      {'quantity':<24}" + "".join(f"{'seed '+str(s):>9}" for s in cal["seeds"]) + f"{'pooled':>9}{'sd':>8}   annotated as")
    for key, (ykey, xkey, ann) in spec.items():
        per = []
        for s in cal["seeds"]:
            sub = sorted([r for r in cal["rows"] if r["seed"] == s], key=lambda r: r["rho"])
            per.append(slope([r["rho"] for r in sub] if xkey is None else [r[xkey] for r in sub],
                             [r[ykey] for r in sub]))
        print(f"      {key:<24}" + "".join(f"{v:>9.4f}" for v in per)
              + f"{cal['slopes'][key]:>9.4f}{np.std(per, ddof=1):>8.4f}   {ann}")
    v_all = cal["slopes"]["logV_all_vs_logrho"]
    check("the exactly-linear exponent 1 is recovered only to ~2% at 3 seeds", abs(v_all - 1.0) > 0.005)
    findings.append(
        f"G0-3 OPEN: no slope in sec.3.2 carries an uncertainty. The design's own noise floor is "
        f"visible in the exactly-known exponent, returned as {v_all:.4f} instead of 1."
    )

    print("\n[E] baseline audit: the minimal-restricted rows do not test the BG exponent")
    agg_vm = [float(np.mean([r["mean_V_min"] for r in cal["rows"] if r["rho"] == rho])) for rho in rhos]
    agg_va = [float(np.mean([r["mean_V_all"] for r in cal["rows"] if r["rho"] == rho])) for rho in rhos]
    print(f"      {'rho':>8}{'<V>_min / rho':>16}{'<V>_all / rho':>16}")
    for rho, vm, va in zip(rhos, agg_vm, agg_va):
        print(f"      {rho:8.0f}{vm/rho:16.5f}{va/rho:16.5f}")
    drift_min = agg_vm[-1] / rhos[-1] / (agg_vm[0] / rhos[0]) - 1
    drift_all = agg_va[-1] / rhos[-1] / (agg_va[0] / rhos[0]) - 1
    print(f"      drift over the sweep:  minimals {drift_min:+.1%}   all elements {drift_all:+.1%}")
    check("<V>_all/rho is flat, confirming the exactly-linear baseline for 'all'", abs(drift_all) < 0.06)
    check("<V>_min/rho is NOT flat, refuting the annotated baseline for 'minimals'", drift_min > 0.15)
    findings.append(
        "G0-4 OPEN: dev/explore_3p1_scale_calibration.py:184-186 annotates 'expect 1' and 'expect 1/4' "
        "for the minimal-restricted slopes. Min(C) is a rho-dependent selection that pushes minimal "
        f"elements toward the past corner, so <V>_min/rho drifts {drift_min:+.1%} across the sweep. "
        "Those three rows are measured against a baseline that does not hold."
    )

    print("\n[F] R = L^4 / V under the two candidate conventions (sensitivity, not a recomputation)")
    agg_lm = [float(np.mean([r["mean_L_min"] for r in cal["rows"] if r["rho"] == rho])) for rho in rhos]
    print(f"      {'rho':>8}{'<L>_min':>10}{'((L+1)/L)^4':>14}{'med R_min':>12}{'x factor':>12}")
    scaled = []
    for rho, lm in zip(rhos, agg_lm):
        mr = float(np.mean([r["median_R_min"] for r in cal["rows"] if r["rho"] == rho]))
        f = ((lm + 1) / lm) ** 4
        scaled.append(mr * f)
        print(f"      {rho:8.0f}{lm:10.3f}{f:14.3f}{mr:12.3f}{mr*f:12.3f}")
    r0 = float(np.mean([r["median_R_min"] for r in cal["rows"] if r["rho"] == rhos[0]]))
    r1 = float(np.mean([r["median_R_min"] for r in cal["rows"] if r["rho"] == rhos[-1]]))
    print(f"      reported drift  x{r1/r0:.2f}      first-order estimate under the vertex convention  x{scaled[-1]/scaled[0]:.2f}")
    check("the reported R drift is not convention-invariant", abs(r1 / r0 - scaled[-1] / scaled[0]) > 0.3)
    findings.append(
        f"G0-5 OPEN: R is quartic in L, so the off-by-one of G0-1 rescales it by up to "
        f"{((agg_lm[0]+1)/agg_lm[0])**4:.2f}x at the smallest rho. The headline 'R drifts by x{r1/r0:.2f}' "
        f"becomes roughly x{scaled[-1]/scaled[0]:.2f} once the sealed vertex convention is used. "
        "The exact curve requires re-running the box leg, which is Phase 1 work."
    )


# ---------------------------------------------------------------------------
def audit_point_process() -> None:
    print("\n[G] point process of the interval generator vs the exact Alexandrov measure")
    from explore_3p1_bg_reference import sprinkle_interval_4d, DIAMOND_VOL_COEFF

    rng = np.random.default_rng(AUDIT_ACCEPT_SEED)
    m = 2_000_000
    t = rng.random(m)
    x = rng.random((m, 3)) - 0.5
    rad = np.linalg.norm(x, axis=1)
    keep = (rad <= t) & (rad <= 1 - t)
    acc = float(keep.mean())
    print(f"      proposal box x ~ U[-1/2, 1/2]^3 inscribes the ball of radius 1/2: the diamond is never clipped")
    print(f"      acceptance rate {acc:.6f}   exact vol(diamond)/vol(box) = pi/24 = {DIAMOND_VOL_COEFF:.6f}")
    check("rejection sampler acceptance rate matches pi/24 to 1%", abs(acc / DIAMOND_VOL_COEFF - 1) < 0.01)
    check("no accepted point exceeds the diamond's maximal radius tau/2", rad[keep].max() < 0.5)

    def bin_mass(a: float, b: float) -> float:
        f = lambda u: u**4 / 4.0
        m_ = 0.0
        lo = min(b, 0.5)
        if a < lo:
            m_ += f(lo) - f(max(a, 0.0))
        hi = max(a, 0.5)
        if b > hi:
            m_ += f(1 - hi) - f(1 - b)
        return m_

    n = 200_000
    for seed in AUDIT_SEEDS:
        pts = sprinkle_interval_4d(seed, n, 1.0)
        e = np.linspace(0.0, 1.0, 21)
        h, _ = np.histogram(pts[:, 0], bins=e)
        w = np.array([bin_mass(e[i], e[i + 1]) for i in range(20)])
        chi2 = float((((h - w / w.sum() * n) ** 2) / (w / w.sum() * n)).sum())
        r = np.linalg.norm(pts[:, 1:], axis=1)
        u = (r / np.minimum(pts[:, 0], 1 - pts[:, 0])) ** 3  # exactly U[0,1] iff uniform in the diamond
        ks = float(np.max(np.abs(np.sort(u) - (np.arange(1, n + 1) - 0.5) / n)))
        crit = 1.36 / np.sqrt(n)
        print(f"      seed {seed}: t-marginal chi2 = {chi2:7.2f} (dof 19, 1% crit 36.19)   radial KS = {ks:.5f} (5% crit {crit:.5f})")
        check(f"seed {seed}: t-marginal consistent with min(t, tau-t)^3", chi2 < 36.19)
        check(f"seed {seed}: radial marginal consistent with uniform-in-diamond", ks < crit)

    print("      process class: interval leg draws EXACTLY n_target points -> BINOMIAL (Poisson conditioned on N=n).")
    print("                     box leg draws rng.poisson(rho * V_box)     -> POISSON.")
    print("      Both are homogeneous w.r.t. Lebesgue = Minkowski volume (sqrt(-g) = 1 in inertial coordinates).")
    findings.append(
        "G0-6 OPEN (documentation): dev/PAPER3_3P1_SCALE_NOTES.md and docs/hoja_de_ruta_paper_iii.md "
        "call both legs Poisson sprinklings. The interval leg is binomial. The two agree in the "
        "large-N limit and the fixed-N choice is legitimate, but the roadmap requires it be declared."
    )


# ---------------------------------------------------------------------------
def audit_m4_band() -> None:
    """The one check that discriminates between the two endpoint conventions.

    Rideout, Dynamics of Causal Sets (gr-qc/0212064) eq. (1.3), quoted verbatim
    at biblioteca/derived-md/Dynamics_of_Causal_Sets_arXiv_gr-qc0212064.md:283:

        1.77 <= 2^(1-1/d)/Gamma(1+1/d) <= m_d <= 2^(1-1/d) e Gamma(d+1)^(1/d)/d <= 2.62

    Those are RIGOROUS bounds, so any admissible normalisation of L must land
    inside them. The same source, line 178, defines chain length as its NUMBER
    OF ELEMENTS, and line 249 measures it as the longest chain CONNECTING the
    two endpoints x and y of the Alexandrov set.
    """
    print("\n[I] rigorous m_4 band: does the reported normalisation land inside it?")
    d = 4
    lo = 2 ** (1 - 1 / d) / gamma(1 + 1 / d)
    hi = 2 ** (1 - 1 / d) * e * gamma(d + 1) ** (1 / d) / d
    print(f"      d = 4:  {lo:.4f} <= m_4 <= {hi:.4f}   (source band for d >= 3: 1.77 .. 2.62)")
    print(f"      {'leg':<12}{'N':>7}{'<L>':>9}{'L/N^(1/4)':>12}{'in band':>9}{'(L+2)/N^(1/4)':>16}{'in band':>9}")
    out_reported, out_endpoint = 0, 0
    for tag, path in (("precision", PREC), ("base 3-seed", BASE)):
        for r in json.load(open(path))["rows"]:
            q0 = r["L_over_N_quarter"]
            q2 = (r["mean_L"] + 2) / r["N"] ** 0.25
            in0, in2 = lo <= q0 <= hi, lo <= q2 <= hi
            out_reported += not in0
            out_endpoint += not in2
            print(f"      {tag:<12}{r['N']:7d}{r['mean_L']:9.3f}{q0:12.4f}{'yes' if in0 else 'NO':>9}"
                  f"{q2:16.4f}{'yes' if in2 else 'NO':>9}")
    print(f"      outside the rigorous band:  as reported {out_reported}/10 rows   with endpoints {out_endpoint}/10 rows")
    check("the reported normalisation violates the rigorous m_4 lower bound somewhere", out_reported > 0)
    check("the endpoint-inclusive normalisation violates it nowhere", out_endpoint == 0)

    prec = json.load(open(PREC))
    q0 = np.array([r["L_over_N_quarter"] for r in prec["rows"]])
    q2 = np.array([(r["mean_L"] + 2) / r["N"] ** 0.25 for r in prec["rows"]])
    print(f"      precision leg spread over the N range:  as reported {q0.min():.4f}..{q0.max():.4f} "
          f"({q0.max()/q0.min()-1:+.1%}, monotone)   with endpoints {q2.min():.4f}..{q2.max():.4f} ({q2.max()/q2.min()-1:+.1%})")
    findings.append(
        f"G0-9 OPEN, and it decides G0-2: under the reported interior-only count {out_reported} of 10 rows "
        f"fall OUTSIDE the rigorous band {lo:.4f} <= m_4 <= {hi:.4f}, which no admissible normalisation may do. "
        f"Counting the two Alexandrov endpoints puts all 10 inside and turns the headline of sec.3.1 "
        f"({q0.max()/q0.min()-1:+.1%} monotone rise) into a {q2.max()/q2.min()-1:+.1%} spread. "
        "The claim that the asymptotic regime has not been reached rests on the convention, not on the data."
    )


# ---------------------------------------------------------------------------
def audit_provenance() -> None:
    print("\n[H] provenance scope of the existing verifier")
    src = open("dev/verify_3p1_notes_figures.py").read()
    check("dev/verify_3p1_notes_figures.py runs no sweep (it only reads the JSONs)",
          "sprinkle" not in src and "import explore" not in src)
    print("      It certifies notes-vs-JSON. Nothing in the repository certifies JSON-vs-GENERATOR:")
    print("      the committed results are not re-executed and their producing commit is not recorded.")
    findings.append(
        "G0-7 OPEN: no artifact records that the committed JSONs are the output of the committed "
        "generators. Closing it requires one deterministic re-execution, which the roadmap assigns "
        "to Phase 1 ('reproducir primero los artefactos existentes')."
    )
    for path in ("dev/explore_3p1_bg_reference.py", "dev/explore_3p1_scale_calibration.py"):
        head = open(path).readline()
        if "Paper II" in head:
            findings.append(f"G0-8 OPEN (documentation): {path}:1 still reads 'Paper II', which "
                            "dev/PAPER3_3P1_SCALE_NOTES.md sec.0 explicitly forbids for 3+1D material.")
    check("both generator headers were checked for the Paper II/III mis-assignment", True)


def main() -> int:
    print("=" * 92)
    print("PAPER III — PHASE 0 GATE CONTRACT VERIFIER (read-only; no sweep, no new observable)")
    print("=" * 92)
    audit_internal_consistency()
    audit_chain_conventions()
    audit_baselines_and_uncertainty()
    audit_point_process()
    audit_m4_band()
    audit_provenance()

    print("\n" + "=" * 92)
    print(f"STRUCTURAL CHECKS: {'ALL PASS' if not failures else 'FAILURES: ' + str(failures)}")
    print(f"GATE_0 FINDINGS:   {len(findings)} open")
    for f in findings:
        print("\n  - " + f.replace(". ", ".\n    ", 2))
    print("\n" + "=" * 92)
    print("GATE_0 = " + ("BLOCKED" if findings else "PASS")
          + "   (roadmap: 'Si hay ambiguedad en el conteo de extremos, en la normalizacion")
    print("                    o en la procedencia de una cifra, la fase no avanza.')")
    print("=" * 92)
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
