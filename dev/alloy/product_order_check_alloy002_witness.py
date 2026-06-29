"""
Minimal falsification test — comité 010 §9 step 1.

Check whether the Alloy 002 witness completions are:
  (a) valid strict partial orders
  (b) 2D-product-order realizable (order dimension ≤ 2)
  (c) physically admissible under the convexity constraint
      (no hidden element causally between two observed elements)

Alloy 002 source: docs/alloy/alloy_verification_002_completion-nonidentifiability-interface.md §4
Alloy model:     formal/alloy/completion_nonidentifiability_interface_counterexample.als
"""

from itertools import permutations

# ---------------------------------------------------------------------------
# Witness from Alloy 002 trace (§4)
# ---------------------------------------------------------------------------
# Notation: E0=Element$0, E1=Element$1, E2=Element$2, E3=Element$3

E0, E1, E2, E3 = "E0", "E1", "E2", "E3"

# Observation (shared subposet)
OBS_ELEMS = frozenset({E2, E3})
# Trace: Observation<:elems = {Observation$0->Element$2, Observation$0->Element$3}
# Induced lt on obs: A$0->Element$2->Element$3 (and same in B) -> E2 < E3

# Completion A: {E1, E2, E3}
# Trace: A$0->Element$2->Element$1, A$0->Element$2->Element$3, A$0->Element$3->Element$1
COMP_A = {
    "name": "A",
    "elems": frozenset({E1, E2, E3}),
    "lt": frozenset({(E2, E1), (E2, E3), (E3, E1)}),
}

# Completion B: {E0, E2, E3}
# Trace: B$0->Element$0->Element$3, B$0->Element$2->Element$0, B$0->Element$2->Element$3
COMP_B = {
    "name": "B",
    "elems": frozenset({E0, E2, E3}),
    "lt": frozenset({(E0, E3), (E2, E0), (E2, E3)}),
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def transitive_closure(elems, lt):
    tc = set(lt)
    changed = True
    while changed:
        changed = False
        for (x, y) in list(tc):
            for (y2, z) in list(tc):
                if y == y2 and (x, z) not in tc:
                    tc.add((x, z))
                    changed = True
    return frozenset(tc)


def is_valid_spo(elems, lt):
    for e in elems:
        if (e, e) in lt:
            return False, f"irreflexivity violated: ({e},{e})"
    tc = transitive_closure(elems, lt)
    if tc != lt:
        return False, f"not transitively closed; TC has {tc - lt} extra pairs"
    return True, "ok"


def all_linear_extensions(elems, lt):
    result = []
    for perm in permutations(elems):
        pos = {e: i for i, e in enumerate(perm)}
        if all(pos[x] < pos[y] for (x, y) in lt):
            result.append(perm)
    return result


def order_dimension_le_2(elems, lt):
    """
    Brute-force check: does there exist a pair of linear extensions (L1, L2)
    such that x <_P y iff x <_L1 y AND x <_L2 y?
    Returns (bool, witness_pair_or_None).
    """
    elems = list(elems)
    exts = all_linear_extensions(elems, lt)

    for L1 in exts:
        pos1 = {e: i for i, e in enumerate(L1)}
        for L2 in exts:
            pos2 = {e: i for i, e in enumerate(L2)}
            ok = True
            for x in elems:
                for y in elems:
                    if x == y:
                        continue
                    in_P = (x, y) in lt
                    in_L1 = pos1[x] < pos1[y]
                    in_L2 = pos2[x] < pos2[y]
                    # x < y in P iff x < y in BOTH L1 and L2
                    if in_P != (in_L1 and in_L2):
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return True, (L1, L2)
    return False, None


def convexity_check(obs_elems, comp_elems, comp_lt):
    """
    Check that obs_elems is a convex subset of the completion:
    for all x, y in obs_elems with x < y in comp_lt,
    no hidden element h satisfies x < h < y in comp_lt.
    """
    hidden = comp_elems - obs_elems
    violations = []
    for x in obs_elems:
        for y in obs_elems:
            if x == y:
                continue
            if (x, y) not in comp_lt:
                continue
            for h in hidden:
                if (x, h) in comp_lt and (h, y) in comp_lt:
                    violations.append((x, h, y))
    return violations


# ---------------------------------------------------------------------------
# Run checks
# ---------------------------------------------------------------------------

def check_completion(comp, obs_elems):
    name = comp["name"]
    elems = comp["elems"]
    lt_direct = comp["lt"]

    print(f"\n{'='*62}")
    print(f"  Completion {name}")
    print(f"  Elements : {sorted(elems)}")
    print(f"  lt       : {sorted(lt_direct)}")
    print(f"  hidden   : {sorted(elems - obs_elems)}")
    print()

    # 1. Transitive closure
    lt_tc = transitive_closure(elems, lt_direct)
    if lt_tc != lt_direct:
        print(f"  [NOTE] lt extended by TC: added {sorted(lt_tc - lt_direct)}")
    else:
        print(f"  [1] TC check: lt is already transitively closed ✓")
    lt = lt_tc

    # 2. Valid strict partial order
    valid, msg = is_valid_spo(elems, lt)
    print(f"  [2] Valid strict partial order: {'YES ✓' if valid else 'NO ✗'} ({msg})")

    # 3. 2D product-order realizable
    dim_ok, witness = order_dimension_le_2(elems, lt)
    if dim_ok:
        L1, L2 = witness
        print(f"  [3] 2D product-order realizable: YES ✓")
        print(f"        L1 = {L1}")
        print(f"        L2 = {L2}")
    else:
        print(f"  [3] 2D product-order realizable: NO ✗")

    # 4. Convexity of observation
    violations = convexity_check(obs_elems, elems, lt)
    if not violations:
        print(f"  [4] Observation {sorted(obs_elems)} convex in completion: YES ✓")
        convex = True
    else:
        print(f"  [4] Observation {sorted(obs_elems)} convex in completion: NO ✗")
        for (x, h, y) in violations:
            print(f"        Violation: {x} < {h} < {y}  (hidden {h} between observed {x} and {y})")
        convex = False

    # 5. Interface decision
    maximal = {e for e in elems if not any(e == x for (x, _) in lt)}
    interface = maximal & obs_elems
    print(f"  [5] Maximal elements in completion: {sorted(maximal)}")
    print(f"       Interface (maximal ∩ observed): {sorted(interface)}")

    admissible = valid and dim_ok and convex
    print()
    print(f"  ADMISSIBILITY: {'ADMISSIBLE ✓' if admissible else 'NOT ADMISSIBLE ✗'}")
    print(f"    (valid SPO={valid}, dim≤2={dim_ok}, convex={convex})")

    return {
        "valid_spo": valid,
        "dim_le_2": dim_ok,
        "convex": convex,
        "admissible": admissible,
        "interface": interface,
    }


print("=" * 62)
print("  Alloy 002 Witness — Physical Admissibility Check")
print("  comité 010 §9 step 1 (minimal falsification test)")
print("=" * 62)
print(f"\n  Observed subposet : {sorted(OBS_ELEMS)}")
print(f"  Shared lt on obs  : {{(E2, E3)}}")
print(f"  Skolem witness    : Element$3 (E3)")
print(f"  Claim: isInterface[B, E3] ∧ ¬isInterface[A, E3]")

result_A = check_completion(COMP_A, OBS_ELEMS)
result_B = check_completion(COMP_B, OBS_ELEMS)

print(f"\n{'='*62}")
print("  SUMMARY")
print(f"{'='*62}")
print(f"  Completion A — admissible: {result_A['admissible']}")
print(f"  Completion B — admissible: {result_B['admissible']}")
print()

# The counterexample uses B for the positive interface decision (E3 interface in B)
# and A for the negative (E3 not interface in A)
if not result_B["admissible"] and result_A["admissible"]:
    print("  VERDICT: PHYSICAL_LAYER_EMPTY_EVIDENCE")
    print()
    print("  The Alloy 002 counterexample achieves a different interface decision")
    print("  for E3 (interface in B, not in A) only by using Completion B, which")
    print("  fails the convexity constraint: the hidden element E0 lies causally")
    print("  BETWEEN the two observed elements E2 and E3.")
    print()
    print("  A physically admissible completion (convex region of a 2D product")
    print("  order) cannot hide an element inside the observed subposet's interior.")
    print("  Therefore the Alloy witness does NOT demonstrate physical")
    print("  non-identifiability.")
    print()
    print("  Update to Alloy 002 summary:")
    print("    PHYSICAL_LAYER_OPEN  →  PHYSICAL_LAYER_EMPTY_EVIDENCE")
elif result_A["admissible"] and result_B["admissible"]:
    print("  VERDICT: PHYSICAL_LAYER_OPEN")
    print()
    print("  Both completions are physically admissible. The counterexample")
    print("  stands at the physical layer — genuine non-identifiability.")
else:
    print("  VERDICT: INCONCLUSIVE (unexpected admissibility pattern)")
    print(f"    A admissible: {result_A['admissible']}, B admissible: {result_B['admissible']}")
