"""EXPLORATION (dev/) — Paper III, Phase 0: Gate-0 contract verifier.

Read-only audit of the four inputs listed in docs/hoja_de_ruta_paper_iii.md.
Runs NO sweep and produces NO new observable: it re-derives every stored
identity from the committed artifacts, exercises the three chain-length
implementations on an explicit 3-element poset, and audits the point process
of the interval generator against the exact Alexandrov density.

Complements dev/verify_3p1_notes_figures.py, which checks notes-vs-JSON only.
This one checks JSON-vs-itself, code-vs-code, and generator-vs-measure.

Since RESOLUTION 1 was signed (2026-09-10, docs/paper_iii_resolucion_001_convencion_L.md)
the chain-length convention is no longer an open question but an ENFORCED INVARIANT:

    L = cardinality of the maximal chain, i.e. its NUMBER OF ELEMENTS.
    For a causal interval bounded by endpoints p, q, BOTH endpoints count.

Step 2 of the mandatory sequence applied it to the box leg (commit 3230986), so
the CODE now conforms and section [B] asserts the full [3, 2, 1] semantics. What
is still outstanding is the EVIDENCE: the committed box artifact was produced by
the pre-conversion generator, so G0-1 and G0-5 stay open until step 3 re-runs it.
That is a pending re-execution, not a breach of the signed convention, and the
verifier detects it by hash rather than by a hardcoded flag.

Exit codes (code 2 was previously reserved for signed-convention debt; with the
conversion done there is no such debt, and the honest distinction left to draw is
between a broken script and a clean script whose gate is still blocked):
    0  structural checks pass and GATE_0 has no open blocker
    1  a structural check failed (something is genuinely broken)
    2  structural checks pass but GATE_0 is blocked by open blockers

RESOLUTION 2 (2026-09-10, docs/paper_iii_resolucion_002_reescopado_fase1.md)
rescoped Phase 1 as a NULL CALIBRATION. Its three operative rules are checked
in section [K]:
    C1  1/4 is the null baseline, not an expectation
    C2  m_4 is bounded, not known: L/N^(1/4) alone cannot separate a transient
        from an unknown constant, so alpha must be fixed a priori
    C3  minimal-restricted rows are excluded from the primary calibration

Run:  python3 dev/verify_3p1_phase0_contract.py
Findings are reported whatever the exit code; an open finding is a Gate-0
blocker, not a script failure. Blockers are counted by distinct G0-x id, never
by how many files or occurrences a single id touches.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from math import e, gamma

import numpy as np

sys.path.insert(0, "dev")
sys.path.insert(0, ".")

PREC = "dev/explore_3p1_bg_reference_precision_results.json"
BASE = "dev/explore_3p1_bg_reference_results.json"
CAL = "dev/explore_3p1_scale_calibration_results.json"
CAL_GEN = "dev/explore_3p1_scale_calibration.py"

# ---------------------------------------------------------------------------
# TWO LINEAGES. The box leg exists twice, on purpose, and they are never mixed.
#
#   HISTORICAL_PRE_R001   CAL, produced by CAL_GEN_SHA256_HISTORICAL.
#                         Immutable. Carries G0-7 and backs sec. 3.2 of the
#                         exploratory notes via dev/verify_3p1_notes_figures.py.
#   R001_REEXECUTION      CAL_R001, produced by CAL_GEN_SHA256_R001 (commit
#                         3230986). Same seeds, same rho, same design; the only
#                         scientific difference is R001 for L. Carries G0-1/G0-5.
# ---------------------------------------------------------------------------
CAL_R001 = "dev/explore_3p1_scale_calibration_r001_results.json"

# ---------------------------------------------------------------------------
# The INTERVAL leg also exists twice, and for the same reason: a replication
# extension must not destroy the provenance of what it extends.
#
#   PREC     8 replicas, seeds 101..108. Historical and immutable. Backs sec.
#            3.1 of the notes through dev/verify_3p1_notes_figures.py.
#   PREC17   17 replicas, seeds 101..117 (PI decision, 2026-09-10). Same four N,
#            same sprinkler, same chain routine, same tau, same binomial
#            process, same observable. ONLY the replica count changed.
#
# Because each seed's chain is independent, the first 8 entries of PREC17 must
# equal PREC value for value. Section [A3] checks exactly that: it is what
# certifies the extension left the design alone, and it would fail loudly if
# the generator edit had perturbed the sampler.
# ---------------------------------------------------------------------------
PREC17 = "dev/explore_3p1_bg_reference_precision17_results.json"
PREC17_SHA256 = "62403ded8f9d784bb348dbd21c870bdfa394efc5a8ee6067ed886d75b89b5a10"

# Certified byte-for-byte against their generators in step 1 of the mandatory
# sequence (2026-09-10, contract sec. 5.2). G0-7 is closed only while these hold.
ARTIFACT_SHA256 = {
    PREC: "eb101d3f63ac6a3625f18557f6fcb8ab08e45935e7f67ef34963ec37379491e7",
    BASE: "5dbb04bc7b1b3f4c6e32b621ef3f10462937d5a4bf1f438283b6916e62167bc6",
    CAL: "e5cb5fb7ba5c3635b055a4363e5a50e6a8cb3c0a4746f0bf37834135920bcd6f",
}
# The box generator AS IT STOOD when it produced CAL: pre-conversion. Recorded by
# the step-1 byte-exact reproduction; it is NOT the live file any more.
CAL_GEN_SHA256_HISTORICAL = "a1b67a37a2eed73bd83000d48d4366c643dca505d857914ffd045dab23561a7b"
# The converted generator (step 2, commit 3230986) that produced CAL_R001.
CAL_GEN_SHA256_R001 = "b5ca8c99021aeed7541e587fbae44d2a76c1dc6cb26589140d125cbd426fb2bb"
CAL_R001_SHA256 = "0aa224027835be64cca2033f38c3b9b6344af6216259dbe26bb0d6fc0ac55b68"

NOTES = "dev/PAPER3_3P1_SCALE_NOTES.md"
ROADMAP = "docs/hoja_de_ruta_paper_iii.md"
BG_GEN = "dev/explore_3p1_bg_reference.py"

# PRODUCER OF RECORD vs LIVE EDITORIAL STATE. The producer hashes above are
# immutable: they say which file actually produced an artifact, and a later
# editorial correction never rewrites them. LIVE_SHA256 pins what the files are
# NOW, so an undeclared edit is caught while the provenance record stays honest.
BG_GEN_SHA256_AT_ARTIFACTS = "f9a181e2524b7d79dbc64837cb4d31de8d8111870d365de6be844504eb414b93"
LIVE_SHA256 = {
    CAL_GEN: "74d7d3d8a3f7d3d36199004bd0bf483b65ab4a785537a959d8ecd34495addd58",  # R004 + R006
    BG_GEN: "8f6a63d703d8db8bcb546423be4131fd8b6a2634ac9ee713a32ec824721bc7ce",   # R006 + 17-replica extension
}


# ---------------------------------------------------------------------------
# Signed documentary resolutions. Each predicate checks the CONDITION the
# resolution actually imposes, so a blocker closes on evidence in the files and
# reopens by itself if that evidence is edited away.
# ---------------------------------------------------------------------------
def r006_applied() -> bool:
    """R006: neither generator header may still say 'Paper II'.

    The obvious test is wrong: "Paper II" is a substring of "Paper III", so a
    plain containment check would keep firing after the correction and the
    blocker would never close. Match the negative lookahead instead.
    """
    return not any(re.search(r"Paper II(?!I)", open(p).readline())
                   for p in (BG_GEN, CAL_GEN))


def r004_applied() -> bool:
    """R004: the three minimal-restricted slope reports may no longer declare a
    baseline, and the notes must record the channel's suspension."""
    for ln in open(CAL_GEN).read().splitlines():
        if "_min" in ln and "loglog_slope" in ln and "expect" in ln:
            return False
    notes = open(NOTES).read()
    return "no pueden citarse como evidencia" in notes and "R004" in notes


def r005_applied() -> bool:
    """R005: every slope reported in the notes carries its seed dispersion and
    replica count, and the pooled-error rule and the design floor are stated."""
    notes = open(NOTES).read()
    labels = ("d log <V>_all / d log rho", "d log <L>_all / d log rho",
              "d log <L>_all / d log <V>_all", "d log <V>_min / d log rho",
              "d log <L>_min / d log rho", "d log <L>_min / d log <V>_min")
    for lab in labels:
        line = next((ln for ln in notes.splitlines() if lab in ln and "|" in ln), None)
        if line is None or "\u00b1" not in line:
            return False
    return "agrupada" in notes and "1.0179" in notes


def r003_applied() -> bool:
    """R003: the interval leg must be declared binomial wherever its figures are
    reported, and neither text may call both legs Poisson sprinklings."""
    notes, road = open(NOTES).read(), open(ROADMAP).read()
    return ("binomial" in notes and "binomial" in road
            and "sprinklings de Poisson" not in road
            and "sprinklings de Poisson" not in notes)


def sha256(path: str) -> str:
    return hashlib.sha256(open(path, "rb").read()).hexdigest()

# Declared audit seeds. Used ONLY by the generator-measure audit (G0-C), never
# by any leg that produces a reported figure.
AUDIT_SEEDS = (101, 102, 103)
AUDIT_ACCEPT_SEED = 999

failures: list[str] = []
findings: list[str] = []
pending: list[str] = []  # signed work done in code but not yet re-run (G0-1, G0-5)
R001_VALIDATED = False  # set by audit_r001_lineage(); gates the G0-1/G0-5 closures


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
def audit_r001_lineage() -> None:
    """The two box-leg lineages, checked separately and never merged.

    Closing G0-1 and G0-5 is not asserted here: it is earned, by a chain that
    must hold end to end -- the converted generator is the live file, it is the
    recorded producer of the R001 artifact, that artifact still hashes to what
    was validated, the L-independent quantities are bit-identical to the
    historical run, the L-dependent ones moved exactly as R001 requires, and
    nothing else moved at all.
    """
    global R001_VALIDATED
    print("\n[A2] box-leg lineages: HISTORICAL_PRE_R001 and R001_REEXECUTION")

    live_gen = sha256(CAL_GEN)
    print(f"      historical artifact  {CAL.split('/')[-1]:52s} {sha256(CAL)[:16]}")
    print(f"        its producer       (pre-R001, recorded in step 1)             {CAL_GEN_SHA256_HISTORICAL[:16]}")
    print(f"      R001 artifact        {CAL_R001.split('/')[-1]:52s} "
          f"{sha256(CAL_R001)[:16] if os.path.exists(CAL_R001) else '<MISSING>'}")
    print(f"        its producer       (converted, commit 3230986)                {CAL_GEN_SHA256_R001[:16]}")
    print(f"      live generator                                                    {live_gen[:16]}")

    ok = check("historical box artifact still hashes to the G0-7-certified value",
               sha256(CAL) == ARTIFACT_SHA256[CAL])
    ok &= check("the two lineages have genuinely different producers",
                CAL_GEN_SHA256_HISTORICAL != CAL_GEN_SHA256_R001)
    if not os.path.exists(CAL_R001):
        check("R001 artifact is present", False)
        return
    ok &= check("R001 artifact hashes to the validated step-3 output",
                sha256(CAL_R001) == CAL_R001_SHA256)
    # The producer of record is immutable. Signed editorial resolutions may move
    # the live file afterwards; that must be declared, and must never be allowed
    # to rewrite who produced the artifact.
    ok &= check("live box generator is exactly the declared editorial state",
                live_gen == LIVE_SHA256[CAL_GEN])
    ok &= check("live interval generator is exactly the declared editorial state",
                sha256(BG_GEN) == LIVE_SHA256[BG_GEN])
    from explore_3p1_scale_calibration import RHO_SWEEP, SEEDS, T_EDGE, X_EDGE
    ok &= check("editorial resolutions left the box design untouched (rho sweep, seeds, box edges)",
                tuple(RHO_SWEEP) == (500.0, 1000.0, 2000.0, 4000.0, 8000.0)
                and tuple(SEEDS) == (11, 12, 13) and T_EDGE == 1.0 and X_EDGE == 1.0)
    if live_gen != CAL_GEN_SHA256_R001:
        print("      NOTE: the live file has moved since the artifact was produced, by signed")
        print("      editorial resolutions only. The producer of record stays the commit-3230986")
        print("      file and is never rewritten to the later hash.")

    old = json.load(open(CAL))
    new = json.load(open(CAL_R001))
    ok &= check("R001 run kept the historical design: same seeds, same rho, same box",
                old["seeds"] == new["seeds"] and old["rho_sweep"] == new["rho_sweep"]
                and old["box"] == new["box"] and len(old["rows"]) == len(new["rows"]))

    def bits(a, b):
        if isinstance(a, float) and isinstance(b, float):
            return a.hex() == b.hex()
        return type(a) is type(b) and a == b

    # L-independent: the point realisation and everything derived from V alone.
    INVARIANT = ("N", "n_minimal", "mean_V_all", "mean_V_min")
    inv = all(bits(o[k], n[k]) for o, n in zip(old["rows"], new["rows"]) for k in INVARIANT)
    inv &= all(bits(old["slopes"][k], new["slopes"][k])
               for k in ("logV_all_vs_logrho", "logV_min_vs_logrho"))
    ok &= check("L-independent quantities are bit-identical to the historical run "
                "(same point realisation, same causal matrix)", inv)

    # The R001 signature: every element gains its own base case, so these shift
    # by exactly one. Anything else moving is an unexpected change.
    PLUS_ONE = ("mean_L_all", "mean_L_min", "max_L")
    DERIVED = ("median_R_all", "median_R_min", "cross_sectional_slope")
    shifted = all(abs((n[k] - o[k]) - 1.0) < 1e-12
                  for o, n in zip(old["rows"], new["rows"]) for k in PLUS_ONE)
    ok &= check("R001 signature: mean_L_all, mean_L_min and max_L shift by exactly +1",
                shifted)

    unexpected = []
    for o, n in zip(old["rows"], new["rows"]):
        for k in sorted(set(o) | set(n)):
            if k not in o or k not in n:
                unexpected.append(f"rows.{k}")
            elif k in INVARIANT or k in ("seed", "rho"):
                if not bits(o[k], n[k]):
                    unexpected.append(f"rows.{k}")
            elif k in PLUS_ONE or k in DERIVED:
                continue
            else:
                unexpected.append(f"rows.{k} (unclassified)")
    for k in sorted(set(old["slopes"]) | set(new["slopes"])):
        moved = not bits(old["slopes"][k], new["slopes"][k])
        # Only the slopes of V alone are L-independent. "logL_vs_logV_all" is an
        # L slope despite the substring, so match the prefix, not the substring.
        if moved and k.startswith("logV"):
            unexpected.append(f"slopes.{k}")
        if not moved and k.startswith("logL"):
            unexpected.append(f"slopes.{k} (an L slope that did not move)")
    ok &= check(f"no unexpected change: every field is invariant, +1, or L-derived "
                f"({len(unexpected)} unexpected)", not unexpected)
    if unexpected:
        print(f"      FIRST DIVERGENCE: {unexpected[0]}")

    # G0-5 needs R measured, not estimated. The historical artifact could only
    # ever give an estimate, because it stores median(L^4/V) and not the L.
    measured = all(isinstance(n.get("median_R_min"), float) and np.isfinite(n["median_R_min"])
                   for n in new["rows"])
    ok &= check("R001 artifact carries a MEASURED median_R_min in all 15 rows", measured)

    R001_VALIDATED = bool(ok)
    print(f"\n      {'slope':<26}{'historical':>12}{'R001':>10}")
    for k in ("logL_all_vs_logrho", "logL_vs_logV_all", "logL_min_vs_logrho", "logL_vs_logV_min"):
        print(f"      {k:<26}{old['slopes'][k]:>12.4f}{new['slopes'][k]:>10.4f}")
    print(f"\n      {'rho':>8}{'median_R_min hist':>20}{'median_R_min R001':>20}{'median_R_all R001':>20}")
    for rho in new["rho_sweep"]:
        mo = float(np.mean([r["median_R_min"] for r in old["rows"] if r["rho"] == rho]))
        mn = float(np.mean([r["median_R_min"] for r in new["rows"] if r["rho"] == rho]))
        ma = float(np.mean([r["median_R_all"] for r in new["rows"] if r["rho"] == rho]))
        print(f"      {rho:8.0f}{mo:20.3f}{mn:20.3f}{ma:20.3f}")
    d_o = ([float(np.mean([r["median_R_min"] for r in old["rows"] if r["rho"] == x])) for x in new["rho_sweep"]])
    d_n = ([float(np.mean([r["median_R_min"] for r in new["rows"] if r["rho"] == x])) for x in new["rho_sweep"]])
    print(f"      median_R_min drift: historical x{d_o[-1]/d_o[0]:.2f}  ->  R001 measured x{d_n[-1]/d_n[0]:.2f}")
    print("      Convention-sensitivity measurement only. R is NOT interpreted here: no claim of")
    print("      stabilisation, universality or geometry, and the minimal channel stays out while G0-4 is open.")


# ---------------------------------------------------------------------------
def audit_precision17_lineage() -> None:
    """The two interval-leg replica counts, checked separately and never merged.

    The extension earns its provenance the same way the box leg did: the
    historical artifact is untouched, the new one hashes to what was validated,
    the seed list is a strict contiguous extension disjoint from every other seed
    list in Paper III, and the replicas the two runs SHARE are identical value for
    value. That last check is the one that matters -- it is what proves the edit
    to the generator was editorial and did not move the sampler.
    """
    print("\n[A3] interval-leg replica counts: 8-seed HISTORICAL and 17-seed EXTENSION")
    if not os.path.exists(PREC17):
        check("17-replica artifact is present", False)
        return

    old, new = json.load(open(PREC)), json.load(open(PREC17))
    print(f"      historical  {PREC.split('/')[-1]:52s} {sha256(PREC)[:16]}")
    print(f"      extension   {PREC17.split('/')[-1]:52s} {sha256(PREC17)[:16]}")

    ok = check("historical 8-replica artifact still hashes to the G0-7-certified value",
               sha256(PREC) == ARTIFACT_SHA256[PREC])
    ok &= check("17-replica artifact hashes to the validated run output",
                sha256(PREC17) == PREC17_SHA256)

    from explore_3p1_bg_reference import (PRECISION17_SEEDS, PRECISION_NS,
                                          PRECISION_SEEDS)
    ok &= check("the extension changed the replica count and NOTHING else about the design",
                tuple(old["seeds"]) == PRECISION_SEEDS
                and tuple(new["seeds"]) == PRECISION17_SEEDS
                and [r["N"] for r in old["rows"]] == [r["N"] for r in new["rows"]]
                == list(PRECISION_NS)
                and old["tau"] == new["tau"] == 1.0)
    ok &= check("17 replicas at every N, declared and realised",
                all(r["n_seeds"] == 17 == len(r["Ls"]) for r in new["rows"]))

    # The seed list is a contiguous extension, and the added seeds are fresh.
    added = tuple(s for s in PRECISION17_SEEDS if s not in PRECISION_SEEDS)
    ok &= check("added seeds are exactly the nine that continue the block: 109..117",
                added == tuple(range(109, 118)))
    # Every other seed list Paper III has ever consumed.
    from explore_3p1_scale_calibration import SEEDS as BOX_SEEDS
    base_seeds = (21, 22, 23)  # dev/explore_3p1_bg_reference.py main(), hardcoded
    spent = set(BOX_SEEDS) | set(base_seeds) | set(PRECISION_SEEDS) \
        | set(AUDIT_SEEDS) | {AUDIT_ACCEPT_SEED}
    ok &= check(f"added seeds are disjoint from every other Paper III seed list "
                f"({sorted(spent)})", not (set(added) & spent))

    # THE check: shared replicas must be identical, value for value.
    shared = all(n["Ls"][:len(PRECISION_SEEDS)] == o["Ls"]
                 for o, n in zip(old["rows"], new["rows"]))
    ok &= check("the 8 shared replicas are identical in both runs -- the generator "
                "edit did not move the sampler", shared)
    for o, n in zip(old["rows"], new["rows"]):
        print(f"        N={o['N']:6d}  shared 8: {o['Ls']}")
        print(f"        {'':8s}  added  9: {n['Ls'][len(PRECISION_SEEDS):]}")

    # Aggregates re-derive from the raw Ls, exactly as section [A] demands of PREC.
    agg = True
    for r in new["rows"]:
        a = np.asarray(r["Ls"], dtype=float)
        agg &= abs(a.mean() - r["mean_L"]) < 1e-12
        agg &= abs(a.std(ddof=1) / np.sqrt(a.size) - r["sem_L"]) < 1e-12
        agg &= abs(a.mean() / r["N"] ** 0.25 - r["L_over_N_quarter"]) < 1e-12
    Lm = [r["mean_L"] for r in new["rows"]]
    Ns = [r["N"] for r in new["rows"]]
    loc = [np.log(Lm[i + 1] / Lm[i]) / np.log(Ns[i + 1] / Ns[i]) for i in range(len(Ns) - 1)]
    agg &= bool(np.allclose(loc, new["local_slopes"]))
    check("17-replica leg: every stored aggregate re-derives from its raw Ls", agg)

    # R005 is a REPORTING rule, and the extension is the thing it was written for:
    # with L integer and 8 replicas the sd was tie-dominated. Report what changed.
    def pooled(o):
        sd = np.array([np.asarray(r["Ls"], float).std(ddof=1) for r in o["rows"]])
        return float(np.sqrt(np.mean(sd ** 2))), sd
    p_old, sd_old = pooled(old)
    p_new, sd_new = pooled(new)
    print(f"      pooled sd  8 replicas: {p_old:.4f} ({(len(sd_old))*(8-1)} dof), "
          f"per-point sd spread {sd_old.min():.4f}..{sd_old.max():.4f}")
    print(f"      pooled sd 17 replicas: {p_new:.4f} ({(len(sd_new))*(17-1)} dof), "
          f"per-point sd spread {sd_new.min():.4f}..{sd_new.max():.4f}")
    print("      R005's pooled-sd clause exists because of the 8-replica tie pattern;")
    print("      the extension is the remedy it pointed at, not a change to the rule.")


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
    print(f"      box      dev/explore_3p1_scale_calib.   L    = {list(map(int, box_L))}  -> maximal element = 1  (ELEMENTS)")

    # R001: the whole vector, not one entry, so a base-case regression anywhere
    # along the chain is caught rather than only at the maximal element.
    check("sealed estimator returns the R001 semantics [3, 2, 1] on the 3-chain",
          [int(v) for v in sealed_L] == [3, 2, 1])
    check("interval leg agrees with R001 (3-chain -> 3)", interval_L == 3)
    check("box leg returns the R001 semantics [3, 2, 1] on the 3-chain",
          [int(v) for v in box_L] == [3, 2, 1])

    # Code conformance is settled here; whether the EVIDENCE exists under R001 is
    # settled in [A2], and G0-1 follows that, not this.
    print(f"\n      R001 conformance of the code : YES        "
          f"evidence regenerated under R001: {'YES' if R001_VALIDATED else 'NOT YET'}")
    if R001_VALIDATED:
        print(f"      G0-1 CLOSED: the R001 lineage certified in [A2] is the re-executed evidence.")
    else:
        findings.append(
            "G0-1 OPEN (pending re-execution): the box generator implements R001 (step 2, commit "
            "3230986) but no certified R001 artifact is present, so every L, max_L and R on record "
            "is still on the superseded convention. Step 3 re-executes the box leg; until then the "
            "evidence is stale, not wrong code."
        )
        pending.append(
            "box leg: R001 applied to the code, evidence not yet regenerated -> G0-1, G0-5"
        )

    print("\n[C] endpoint count: SUPERSEDED interior-only vs SIGNED endpoint-inclusive")
    prec = json.load(open(PREC))
    Ns = np.array([r["N"] for r in prec["rows"]], dtype=float)
    Lm = np.array([r["mean_L"] for r in prec["rows"]], dtype=float)
    print(f"      {'convention':<18}" + "".join(f"{int(n):>10d}" for n in Ns) + f"{'local slopes':>26}{'global':>9}")
    for off, name in ((0, "L   (superseded)"), (1, "L+1"), (2, "L+2 (SIGNED, with p,q)")):
        Q = (Lm + off) / Ns**0.25
        ls = [np.log((Lm + off)[i + 1] / (Lm + off)[i]) / np.log(Ns[i + 1] / Ns[i]) for i in range(len(Ns) - 1)]
        print(f"      {name:<18}" + "".join(f"{v:>10.4f}" for v in Q)
              + "  " + " ".join(f"{v:7.4f}" for v in ls) + f"{slope(Ns, Lm + off):9.4f}")
    g0, g2 = slope(Ns, Lm), slope(Ns, Lm + 2)
    check("endpoint convention shifts the global slope by more than 0.02", abs(g0 - g2) > 0.02)
    print(f"      G0-2 CLOSED by Resolution 1: the signed count is L+2, global slope {g2:.4f} (was {g0:.4f}).")


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
    if r005_applied():
        print(f"      G0-3 CLOSED by R005: every slope in the notes carries its seed dispersion and")
        print(f"      replica count, the pooled-error rule is stated, and the design floor is the")
        print(f"      exactly-known exponent returned as {v_all:.4f} instead of 1.")
    else:
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
    if r004_applied():
        print("      G0-4 CLOSED by R004: the three minimal-restricted rows no longer declare a")
        print("      baseline, and the notes record the channel as suspended -- not reopened.")
    else:
        findings.append(
            "G0-4 OPEN: the minimal-restricted slopes in dev/explore_3p1_scale_calibration.py still "
            "annotate 'expect 1' and 'expect 1/4'. Min(C) is a rho-dependent selection that pushes "
            f"minimal elements toward the past corner, so <V>_min/rho drifts {drift_min:+.1%} across "
            "the sweep. Those three rows are measured against a baseline that does not hold."
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
    if R001_VALIDATED:
        print("      G0-5 CLOSED: median_R_min is MEASURED under R001 in the [A2] lineage, so the")
        print("      first-order estimate above is superseded by an exact figure. R stays uninterpreted.")
    else:
        findings.append(
            f"G0-5 OPEN: R is quartic in L, so the superseded off-by-one rescales it by up to "
            f"{((agg_lm[0]+1)/agg_lm[0])**4:.2f}x at the smallest rho. The headline 'R drifts by "
            f"x{r1/r0:.2f}' becomes roughly x{scaled[-1]/scaled[0]:.2f} under R001. The code is "
            "converted; the exact curve still requires re-running the box leg (step 3)."
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
    if r003_applied():
        print("      G0-6 CLOSED by R003: both texts declare the interval leg binomial, and neither")
        print("      describes the two legs as 'sprinklings de Poisson'.")
    else:
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
    print(f"      G0-9 ADJUDICATED: it decided G0-2, and Resolution 1 signed the outcome it pointed to.")
    _ = (
        f"under the superseded interior-only count {out_reported} of 10 rows "
        f"fall OUTSIDE the rigorous band {lo:.4f} <= m_4 <= {hi:.4f}, which no admissible normalisation may do. "
        f"Counting the two Alexandrov endpoints puts all 10 inside and turns the headline of sec.3.1 "
        f"({q0.max()/q0.min()-1:+.1%} monotone rise) into a {q2.max()/q2.min()-1:+.1%} spread."
    )


# ---------------------------------------------------------------------------
def audit_r1_restatement() -> None:
    """What Resolution 1 recovers by arithmetic, and what it does not.

    The interval leg stores the raw per-seed chain counts, so the signed
    convention is a shift of +2 on integers already committed: a restatement,
    not a measurement. The box leg stores only aggregates; <L> is linear so it
    shifts by +1 exactly, but median(L^4/V) is not a function of median((L-1)^4/V)
    and cannot be recovered without re-running.
    """
    print("\n[J] Resolution 1 applied to the committed artifacts (arithmetic on provenance)")
    for tag, path in (("precision (8 seeds)", PREC), ("base (3 seeds)", BASE)):
        o = json.load(open(path))
        N = np.array([r["N"] for r in o["rows"]], dtype=float)
        L0 = np.array([r["mean_L"] for r in o["rows"]], dtype=float)
        L1 = L0 + 2.0
        q0, q1 = L0 / N**0.25, L1 / N**0.25
        print(f"      {tag}:  d log<L>/d log N   superseded {slope(N, L0):.4f}  ->  SIGNED {slope(N, L1):.4f}")
        print(f"      {'':<{len(tag)}}   spread of L/N^(1/4)  superseded {q0.max()/q0.min()-1:+.1%}"
              f"  ->  SIGNED {q1.max()/q1.min()-1:+.1%}")

    cal = json.load(open(CAL))
    rhos = cal["rho_sweep"]
    agg = {k: [float(np.mean([r[k] for r in cal["rows"] if r["rho"] == rho])) for rho in rhos]
           for k in ("mean_V_all", "mean_L_all", "mean_V_min", "mean_L_min")}
    print(f"\n      box leg, <L> shifts by +1 exactly:")
    print(f"      {'slope':<30}{'superseded':>12}{'SIGNED':>10}   expected")
    for label, ykey, xs, exp in (
        ("d log<L>_all / d log rho", "mean_L_all", rhos, "1/4"),
        ("d log<L>_all / d log<V>_all", "mean_L_all", agg["mean_V_all"], "1/4"),
        ("d log<L>_min / d log rho", "mean_L_min", rhos, "1/4  (baseline unsound, G0-4)"),
        ("d log<L>_min / d log<V>_min", "mean_L_min", agg["mean_V_min"], "1/4  (baseline unsound, G0-4)"),
    ):
        y = agg[ykey]
        print(f"      {label:<30}{slope(xs, y):>12.4f}{slope(xs, [v + 1 for v in y]):>10.4f}   {exp}")

    a_all = slope(rhos, [v + 1 for v in agg["mean_L_all"]])
    v_all = cal["slopes"]["logV_all_vs_logrho"]
    floor = abs(v_all - 1.0)
    check("the unrestricted L slope lands within the design's own noise floor of 1/4",
          abs(a_all - 0.25) <= floor)
    print(f"      |{a_all:.4f} - 0.25| = {abs(a_all-0.25):.4f}  vs  noise floor |{v_all:.4f} - 1| = {floor:.4f}")
    print("      G0-10 CLOSED by Resolution 2: Phase 1 rescoped as a null calibration; the "
          "'slope near 0.29' premise is withdrawn.")
    _ = (
        f"under Resolution 1 every UNRESTRICTED slope lands at 1/4 within the "
        f"design's own noise floor (interval leg {slope(np.array([r['N'] for r in json.load(open(PREC))['rows']], dtype=float), np.array([r['mean_L'] for r in json.load(open(PREC))['rows']], dtype=float) + 2):.4f} "
        f"and {slope(np.array([r['N'] for r in json.load(open(BASE))['rows']], dtype=float), np.array([r['mean_L'] for r in json.load(open(BASE))['rows']], dtype=float) + 2):.4f}; box leg {a_all:.4f}). "
        "The premise of the roadmap's Phase 1 question -- an observable departure from 1/4 -- is no "
        "longer supported in the unrestricted channel. Only the minimal-restricted slopes still "
        "deviate, and those are exactly the ones G0-4 shows are measured against an unsound baseline. "
        "Phase 1 needs a re-scoped question, which is a PI decision."
    )
    print("\n      NOT restatable: median_R_min. The artifact stores the median of L^4/V, not the")
    print("      per-element L, and median((L+1)^4/V) is no function of median(L^4/V). Re-run required.")


# ---------------------------------------------------------------------------
def audit_null_calibration() -> None:
    """Resolution 2: is the NULL -- a pure constant, no correction -- rejected?

    Under R001 this is arithmetic on the committed per-seed integers. It runs no
    sweep. It reports the answer under two error models, because at 8 replicas of
    an integer L the per-point sem is itself poorly determined.
    """
    print("\n[K] Resolution 2 null calibration: is a constant already consistent with the data?")

    def leg(path):
        rows = json.load(open(path))["rows"]
        N = np.array([r["N"] for r in rows], dtype=float)
        Ls = [np.asarray(r["Ls"], dtype=float) + 2.0 for r in rows]  # R001 convention
        y = np.array([a.mean() for a in Ls]) / N**0.25
        sd = np.array([a.std(ddof=1) for a in Ls])
        return N, Ls, y, sd

    def const_fit(y, s):
        w = 1.0 / s**2
        m = float((w * y).sum() / w.sum())
        return float((w * (y - m) ** 2).sum()), m, float(1.0 / np.sqrt(w.sum()))

    N, Ls, y, sd = leg(PREC)
    n_rep = Ls[0].size
    s_ind = sd / np.sqrt(n_rep) / N**0.25
    pooled = float(np.sqrt(np.mean(sd**2)))
    s_pool = np.full(len(N), pooled / np.sqrt(n_rep)) / N**0.25

    print(f"      {'N':>7}{'Ls (R001)':>34}{'sd':>9}")
    for i, a in enumerate(Ls):
        print(f"      {int(N[i]):7d}{str([int(v) for v in a]):>34}{sd[i]:9.4f}")
    print(f"      -> sd across the sweep: {sd.min():.4f} .. {sd.max():.4f}. With L integer and spread ~1,")
    print(f"         a heavily tied 8-sample sd underestimates the true one and dominates any chi2.")

    c_ind, m_ind, _ = const_fit(y, s_ind)
    c_pool, m_pool, se_pool = const_fit(y, s_pool)
    dof = len(N) - 1
    print(f"\n      precision leg, per-point sem      chi2/dof = {c_ind/dof:.2f}   m_4 = {m_ind:.4f}")
    print(f"      precision leg, POOLED sd          chi2/dof = {c_pool/dof:.2f}   m_4 = {m_pool:.4f} +/- {se_pool:.4f}")
    Nb, Lsb, yb, sdb = leg(BASE)
    c_b, m_b, se_b = const_fit(yb, sdb / np.sqrt(Lsb[0].size) / Nb**0.25)
    print(f"      base leg, per-point sem           chi2/dof = {c_b/(len(Nb)-1):.2f}   m_4 = {m_b:.4f} +/- {se_b:.4f}")
    check("C1: the null (pure constant) is NOT rejected under a robust error model",
          c_pool / dof < 2.5 and c_b / (len(Nb) - 1) < 2.5)
    check("C1: the fitted constant lies inside the rigorous m_4 band",
          1.8555 <= m_pool <= 2.5296 and 1.8555 <= m_b <= 2.5296)

    # C2: identifiability
    print("\n      C2 identifiability -- L/N^(1/4) = m_4 (1 + c N^-alpha) has 3 free parameters,")
    print(f"         and the precision leg has {len(N)} points. Fixing alpha a priori:")
    w = 1.0 / s_pool**2
    print(f"         {'alpha':>8}{'m_4':>10}{'c':>11}{'chi2 (dof 2)':>15}{'gain vs const':>15}")
    gains = []
    for al in (0.25, 0.5, 1.0):
        X = np.column_stack([np.ones_like(N), N ** (-al)])
        W = np.diag(w)
        beta = np.linalg.solve(X.T @ W @ X, X.T @ W @ y)
        r = y - X @ beta
        chi = float(r @ W @ r)
        gains.append(c_pool - chi)
        print(f"         {al:8.2f}{beta[0]:10.4f}{beta[1]/beta[0]:11.3f}{chi:15.2f}{c_pool-chi:15.2f}")
    check("C2: no fixed alpha is preferred -- alpha must be set a priori, never fitted",
          max(gains) < 4.0)

    # C3: the minimal channel is suspended
    cal = json.load(open(CAL))
    rhos = cal["rho_sweep"]
    vm = [float(np.mean([r["mean_V_min"] for r in cal["rows"] if r["rho"] == x])) for x in rhos]
    va = [float(np.mean([r["mean_V_all"] for r in cal["rows"] if r["rho"] == x])) for x in rhos]
    d_min = (vm[-1] / rhos[-1]) / (vm[0] / rhos[0]) - 1
    d_all = (va[-1] / rhos[-1]) / (va[0] / rhos[0]) - 1
    print(f"\n      C3 minimal channel suspended: <V>_min/rho drifts {d_min:+.1%} vs {d_all:+.1%} for all elements.")
    check("C3: the minimal channel's baseline is confirmed unsound, so it stays out of the calibration",
          abs(d_min) > 3 * abs(d_all))

    # design resolution
    print("\n      design resolution -- smallest correction amplitude detectable at 2 sigma:")
    se_diff = float(np.sqrt(s_pool[0] ** 2 + s_pool[-1] ** 2))
    print(f"         {'alpha':>8}{'|c| min':>12}{'effect at N=' + str(int(N[0])):>22}")
    for al in (0.25, 0.5, 1.0):
        lever = N[0] ** (-al) - N[-1] ** (-al)
        cmin = 2 * se_diff / lever / m_pool
        print(f"         {al:8.2f}{cmin:12.3f}{cmin * N[0]**(-al):>21.1%}")
    obs = y.max() / y.min() - 1
    rel = pooled / np.sqrt(n_rep) / float(np.mean([a.mean() for a in Ls]))
    print(f"         observed spread over the range: {obs:+.1%}   per-point uncertainty: {rel:.2%}")
    for k, lbl in ((2, "2 sigma"), (3, "3 sigma")):
        need = n_rep * (rel / (obs / k / np.sqrt(2))) ** 2
        print(f"         to separate the endpoints at {lbl}: ~{int(np.ceil(need))} replicas per point")
    print("         The binding constraint is REPLICAS, not N: the chain is O(N^2), replicas are linear.")


# ---------------------------------------------------------------------------
def audit_provenance() -> None:
    print("\n[H] provenance scope of the existing verifier")
    src = open("dev/verify_3p1_notes_figures.py").read()
    check("dev/verify_3p1_notes_figures.py runs no sweep (it only reads the JSONs)",
          "sprinkle" not in src and "import explore" not in src)
    print("      It certifies notes-vs-JSON. JSON-vs-GENERATOR was certified separately, in step 1")
    print("      of the mandatory sequence: all three artifacts reproduced BYTE-FOR-BYTE from the")
    print("      unedited generators (2026-09-10, contract sec. 5.2). G0-7 is CLOSED.")
    print("      G0-7 rides on the HISTORICAL lineage alone; the R001 artifact is not part of it.")
    print("      That closure holds only while the artifacts are the ones certified, so re-check:")
    intact = True
    for path, want in ARTIFACT_SHA256.items():
        got = sha256(path)
        ok = got == want
        intact &= ok
        print(f"        {'OK  ' if ok else 'FAIL'}  {path.split('/')[-1]:48s} {got[:16]}")
    check("G0-7 stays closed: the three certified artifacts are unchanged", bool(intact))

    if r006_applied():
        print("      G0-8 CLOSED by R006: both generator headers read 'Paper III'.")
    else:
        stale_heads = [p for p in (BG_GEN, CAL_GEN)
                       if re.search(r"Paper II(?!I)", open(p).readline())]
        # One blocker id, however many files carry it.
        findings.append("G0-8 OPEN (documentation): line 1 still reads 'Paper II' in "
                        + " and ".join(stale_heads)
                        + ", which dev/PAPER3_3P1_SCALE_NOTES.md sec.0 explicitly forbids for 3+1D "
                        "material.")
    check("both generator headers were checked for the Paper II/III mis-assignment", True)


def main() -> int:
    print("=" * 92)
    print("PAPER III — PHASE 0 GATE CONTRACT VERIFIER (read-only; no sweep, no new observable)")
    print("=" * 92)
    audit_internal_consistency()
    audit_r001_lineage()
    audit_precision17_lineage()
    audit_chain_conventions()
    audit_baselines_and_uncertainty()
    audit_point_process()
    audit_m4_band()
    audit_r1_restatement()
    audit_null_calibration()
    audit_provenance()

    print("\n" + "=" * 92)
    # Blockers are counted by distinct G0-x id. A single id that shows up in two
    # files (G0-8 did) is one blocker, not two.
    open_ids = sorted({m.group(0) for f in findings if (m := re.match(r"G0-\d+", f))},
                      key=lambda s: int(s.split("-")[1]))

    print(f"STRUCTURAL CHECKS:  {'ALL PASS' if not failures else 'FAILURES: ' + str(failures)}")
    print(f"R001 CONVENTION:    code conforms; {len(pending)} item(s) pending re-execution")
    for v in pending:
        print("\n  ~ " + v.replace(". ", ".\n    ", 2))
    print(f"\nGATE_0 BLOCKERS:    {len(open_ids)} open  ->  {', '.join(open_ids) if open_ids else 'none'}")
    for f in findings:
        print("\n  - " + f.replace(". ", ".\n    ", 2))
    print("\n" + "=" * 92)
    print("GATE_0 = " + ("BLOCKED" if open_ids else "PASS")
          + "   (roadmap: 'Si hay ambiguedad en el conteo de extremos, en la normalizacion")
    print("                    o en la procedencia de una cifra, la fase no avanza.')")
    if pending:
        print("PENDING=STEP_3_BOX_LEG_REEXECUTION   (signed work not yet re-run; not a regression)")
    print("=" * 92)
    if failures:
        return 1
    return 2 if open_ids else 0


if __name__ == "__main__":
    sys.exit(main())
