"""Gate 0 Tier 1 -- automated silent-corruption falsification check for R-VAR v2.2 (D.2.3).

Authorized scope: PI authorization 2026-07-04 (chat, scoped block id "f4ljlu"), conditioned on
v2.2 being committed first (verified: commit 6687357, dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md).
Controlling spec: dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md, D.2.1-D.2.3.

Scope (frozen by the authorization, do not exceed):
  - Gate 0 Tier 1 ONLY. No S2-S5, no mu computation, no calibration tables, no production/
    BH-patch scoring tracks.
  - >=100 finite posets, N<=14, generated from EXPLORE_POOL sub-seeds only (never
    VALIDATION_SEEDS). Both MINK and BH kind per accepted embedding.
  - For every poset: compare the D.2.1 min-cut / maximum-weight-closure argmax (imported
    UNCHANGED from the Tier 0 script, measure_pr003_rvar_gate0.py) against an independent
    brute-force enumeration of A(C), at every Dinkelbach step, with exact rational arithmetic.
  - Zero-discrepancy acceptance rule (frozen, D.2.3): any single mismatch is GATE0_TIER1_FAIL
    and blocks mu-table freeze / Tier 2+ unconditionally. Not adjusted post-hoc.
  - Degenerate D=empty / D=C ties at the raw (unfiltered) optimum are reported separately,
    confirming the A(C) membership filter gates the argmax (D.2.1 normative warning).

Methodology note (disclosed scope limitation, matching Tier 0's own precedent -- not a silent
gap): T(C)/E(C)/U(C) are reported via the frozen D.2.2 formula (brute_force_TEU, evaluated at
the mincut-cross-checked lambda*), exactly as Tier 0 did. Tier 0 did not independently
re-derive T/E/U via a second forced-membership flow computation, and this script does not
either -- inventing a new forced-mincut construction not already vetted by comite 017 would be
scope creep beyond the authorization. What IS independently cross-checked, per poset and at
every Dinkelbach step, is the D.2.1 argmax: brute-force enumeration over the family vs. the
maximum-weight-closure/min-cut flow computation.

Interpretation of ">=100 posets" (disclosed): the binding target is >=100 posets whose A(C) is
NON-empty -- only those can exercise (and therefore falsify) the D.2.1/D.2.2 machinery; an
EMPTY_FAMILY poset has nothing for either implementation to disagree about. Total posets
generated (including EMPTY_FAMILY and out-of-range-N skips) is reported alongside for
transparency.

Seeds: roots are EXPLORE_POOL (dev/explore_seeds.py, 1000000..1000039, in order). Per root,
child seeds are drawn via `numpy.random.SeedSequence(root).spawn(K)`, consumed in order, capped
at MAX_CHILDREN_PER_ROOT per root as a safety valve. VALIDATION_SEEDS are never referenced by
this script (no import of that name). The sprinkle intensity (TOY_INTENSITY=9.0, Poisson mean)
is a toy-scale choice made ONLY to land N in [0,14] with reasonable probability -- it is NOT one
of the sealed thresholds.INTENSITIES values and carries no statistical/calibration meaning.

Does NOT: touch VALIDATION_SEEDS, run sealed-intensity sprinklings, compute mu, produce
calibration tables, touch production/BH-patch scoring tracks, or proceed to S2-S5.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from fractions import Fraction

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal.generator import numpy_sprinkle, past_matrix_fast  # noqa: E402
from nachocausal import thresholds  # noqa: E402
from dev.explore_seeds import EXPLORE_POOL  # noqa: E402
from dev.measure_pr003_rvar_gate0 import (  # noqa: E402
    minimal_elements,
    maximal_elements,
    is_cover,
    family_A,
    brute_force_argmax,
    brute_force_TEU,
    maxflow_mincut_closure,
    mincut_argmax_in_family,
)

RESULT_PATH = os.path.join(os.path.dirname(__file__), "gate0_tier1_result.json")

TOY_INTENSITY = 9.0          # Poisson mean; toy-scale choice, NOT thresholds.INTENSITIES.
N_MAX = 14
TARGET_NONEMPTY = 100        # binding target -- see module docstring interpretation note.
MAX_CHILDREN_PER_ROOT = 400  # safety cap; EXPLORE_POOL has 40 roots, this is far more capacity
                              # than needed to reach TARGET_NONEMPTY.
KINDS = ("MINK", "BH")


def build_leq(C: np.ndarray):
    """past_matrix_fast convention: C[i,j] True iff j precedes i (j causally in i's past)."""
    def leq(a, b):
        return a == b or bool(C[b, a])
    return leq


def assert_partial_order(elems, leq) -> None:
    """Integrity check on the generator's output (not a Tier 1 comparison target, but a
    guardrail that CAN fail per the founding rules): antisymmetry + transitivity."""
    for a in elems:
        for b in elems:
            if a != b and leq(a, b) and leq(b, a):
                raise ValueError(f"generator relation not antisymmetric: {a}<={b}<={a}")
    for a in elems:
        for b in elems:
            if not leq(a, b):
                continue
            for c in elems:
                if leq(b, c) and not leq(a, c):
                    raise ValueError(f"generator relation not transitive: {a}<={b}<={c} but not {a}<={c}")


def run_single_poset_check(elems, leq, tag):
    Min = minimal_elements(elems, leq)
    Max = maximal_elements(elems, leq)
    covers = [(x, y) for x in elems for y in elems if is_cover(elems, leq, x, y)]
    dplus = {x: sum(1 for (a, b) in covers if a == x) for x in elems}
    fam = family_A(elems, leq, covers, dplus, Min, Max)

    record = dict(
        tag=tag, N=len(elems), n_covers=len(covers), n_min=len(Min), n_max=len(Max),
        family_size=len(fam),
    )

    if not fam:
        record.update(status="EMPTY_FAMILY", PASS=True)
        return record

    Dstar_bf, (Astar, Bstar) = brute_force_argmax(fam)
    T_bf, E_bf, U_bf = brute_force_TEU(elems, fam, Astar, Bstar)

    # D.2.1 degenerate-tie check: raw (UNFILTERED over all down-sets) mincut optimum at lambda*.
    c_at_star, D_raw = maxflow_mincut_closure(elems, covers, dplus, Astar, Bstar)
    degenerate_raw_tie = D_raw in (frozenset(), frozenset(elems))

    tied_in_fam, _ = mincut_argmax_in_family(elems, leq, Max, fam, c_at_star)
    # Compare against the FULL brute-force tie set, not a single max()-picked representative:
    # multiple down-sets can legitimately tie at the same optimal ratio (observed in practice
    # at this automated scale, unlike the hand-built Tier 0 poset which happened not to tie).
    lam_star_frac = Fraction(Astar, Bstar)
    full_tie_set_bf = {D for D, (a, b) in fam.items() if Fraction(a, b) == lam_star_frac}
    optimum_matches = set(tied_in_fam) == full_tie_set_bf

    def bf_argmax_at(p, q):
        return max(fam.items(), key=lambda kv: q * kv[1][0] - p * kv[1][1])[0]

    def mincut_argmax_at(p, q):
        c, _ = maxflow_mincut_closure(elems, covers, dplus, p, q)
        tied, _ = mincut_argmax_in_family(elems, leq, Max, fam, c)
        return tied[0] if tied else bf_argmax_at(p, q)

    lam_num, lam_den = 0, 1
    trace = []
    for it in range(40):
        D_bf = bf_argmax_at(lam_num, lam_den)
        D_mc = mincut_argmax_at(lam_num, lam_den)
        agree = D_bf == D_mc
        trace.append(dict(it=it, lam=str(Fraction(lam_num, lam_den)), agree=agree))
        A_bf, B_bf = fam[D_bf]
        if Fraction(A_bf, B_bf) == Fraction(lam_num, lam_den) and it > 0:
            break
        lam_num, lam_den = A_bf, B_bf
    else:
        record.update(status="DINKELBACH_DID_NOT_CONVERGE", PASS=False)
        record["dinkelbach_trace"] = trace
        return record

    all_agree = all(t["agree"] for t in trace)
    converged_matches = Fraction(trace[-1]["lam"]) == Fraction(Astar, Bstar)

    passed = optimum_matches and all_agree and converged_matches
    record.update(
        status="TESTED",
        lambda_star=[Astar, Bstar],
        degenerate_raw_tie=degenerate_raw_tie,
        mincut_optimum_matches_brute_force=optimum_matches,
        dinkelbach_steps=len(trace),
        all_dinkelbach_steps_agree=all_agree,
        converged_lambda_matches=converged_matches,
        T_bf=T_bf, E_bf=E_bf, U_bf=U_bf,
        PASS=passed,
    )
    return record


def generate_and_test():
    tested = []
    nonempty_count = 0
    skipped_out_of_range = 0
    for root in EXPLORE_POOL:
        if nonempty_count >= TARGET_NONEMPTY:
            break
        children = np.random.SeedSequence(root).spawn(MAX_CHILDREN_PER_ROOT)
        for child_idx, child_seedseq in enumerate(children):
            if nonempty_count >= TARGET_NONEMPTY:
                break
            embedding, edges, center = numpy_sprinkle(child_seedseq, TOY_INTENSITY)
            N = embedding.shape[0]
            if N > N_MAX:
                skipped_out_of_range += 1
                continue
            elems = list(range(N))
            for kind in KINDS:
                if nonempty_count >= TARGET_NONEMPTY:
                    break
                C = past_matrix_fast(embedding, kind, thresholds.R_S)
                leq = build_leq(C)
                assert_partial_order(elems, leq)
                tag = f"root={root},child={child_idx},kind={kind},N={N}"
                rec = run_single_poset_check(elems, leq, tag)
                rec["root_seed"] = root
                rec["child_index"] = child_idx
                rec["kind"] = kind
                tested.append(rec)
                if rec["status"] != "EMPTY_FAMILY":
                    nonempty_count += 1
    return tested, skipped_out_of_range


if __name__ == "__main__":
    commit_hash = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        capture_output=True, text=True, check=True,
    ).stdout.strip()

    tested, skipped_out_of_range = generate_and_test()

    nonempty = [r for r in tested if r["status"] != "EMPTY_FAMILY"]
    empty_family = [r for r in tested if r["status"] == "EMPTY_FAMILY"]
    mismatches = [r for r in nonempty if not r["PASS"]]
    degenerate_ties = [r for r in nonempty if r.get("degenerate_raw_tie")]

    overall_status = "GATE0_TIER1_PASS" if (len(nonempty) >= TARGET_NONEMPTY and not mismatches) else "GATE0_TIER1_FAIL"

    result = dict(
        gate="Gate 0 Tier 1",
        spec="dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md",
        commit_at_run=commit_hash,
        toy_intensity=TOY_INTENSITY,
        n_max=N_MAX,
        target_nonempty=TARGET_NONEMPTY,
        seed_pool="EXPLORE_POOL (dev/explore_seeds.py, 1000000..1000039)",
        seed_recipe="numpy.random.SeedSequence(root).spawn(K) per EXPLORE_POOL root, "
                    "roots and children consumed in order, K<=MAX_CHILDREN_PER_ROOT="
                    f"{MAX_CHILDREN_PER_ROOT}",
        total_posets_generated=len(tested),
        total_skipped_N_out_of_range=skipped_out_of_range,
        n_empty_family=len(empty_family),
        n_nonempty_family_tested=len(nonempty),
        n_mismatches=len(mismatches),
        n_degenerate_raw_ties=len(degenerate_ties),
        degenerate_raw_tie_examples=[r["tag"] for r in degenerate_ties[:10]],
        mismatch_records=mismatches,
        size_range_N=[min(r["N"] for r in tested), max(r["N"] for r in tested)] if tested else None,
        OVERALL_STATUS=overall_status,
        all_records=tested,
    )
    with open(RESULT_PATH, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Generated: {len(tested)} posets total ({skipped_out_of_range} skipped N>{N_MAX})")
    print(f"  EMPTY_FAMILY: {len(empty_family)}   non-empty tested: {len(nonempty)}")
    print(f"  degenerate raw ties (D=empty or D=C at unfiltered optimum): {len(degenerate_ties)}")
    print(f"  mismatches: {len(mismatches)}")
    print(f"OVERALL Gate 0 Tier 1 STATUS: {overall_status}")
    print(f"Full result written to {RESULT_PATH}")
