"""Estimator-v2 contract tests — one per frozen clause of
docs/estimator_v2_freeze.md (A observable, C gate, D domain, H order).

Provenance/poset-integrity (the height oracle) stays covered by
tests/test_regression.py and test_poset_checksum.py.
"""

import numpy as np
import pytest

from nachocausal import estimator, gate, generator, thresholds, validate

pinned = pytest.mark.skipif(
    np.__version__ != thresholds.PINNED_NUMPY,
    reason=f"sealed under numpy=={thresholds.PINNED_NUMPY}",
)


# --- (A) VOLUME observable ----------------------------------------------------
def test_volume_observable_on_hand_poset():
    # Elements 0,1 minimal; 0<2, 0<3, 1<3.  C[i,j] True iff j precedes i.
    C = np.zeros((4, 4), dtype=bool)
    C[2, 0] = True            # past(2) = {0}
    C[3, 0] = C[3, 1] = True  # past(3) = {0,1}
    O, mins = estimator.estimate_O_volume(C)
    assert mins == [0, 1]
    assert O == {0: 2, 1: 1}  # |future(0)|={2,3}=2 ; |future(1)|={3}=1


def test_volume_observable_is_relabel_invariant():
    emb, _, _ = generator.numpy_sprinkle(seed=42, intensity=600.0)
    C = generator.past_matrix_fast(emb, "BH")
    estimator.verify_order_only(C, seed=3)  # default observable = volume; must not raise


# --- improvement (feeds the gate): vectorised == brute ------------------------
def test_improvement_matches_brute():
    def brute(o):
        o = np.sort(np.asarray(o, float)); n = o.size
        if n < 2:
            return 0.0
        tot = o.var() * n
        if tot <= 0:
            return 0.0
        best = min(o[:i].var() * i + o[i:].var() * (n - i) for i in range(1, n))
        return 1.0 - best / tot

    rng = np.random.default_rng(0)
    for n in range(2, 40):
        x = rng.random(n)
        assert np.isclose(estimator.improvement(x), brute(x), rtol=0, atol=1e-12)
    assert estimator.improvement([5.0]) == 0.0          # n<2
    assert estimator.improvement([3.0, 3.0, 3.0]) == 0.0  # zero variance


# --- (C) tau(n) gate semantics ------------------------------------------------
@pinned
def test_gate_tau_in_table_and_params_match():
    assert thresholds.GATE_TAU_N_MAX == 128
    assert 0.0 < gate.tau(71) < 1.0
    assert gate.tau(2) == pytest.approx(1.0, abs=1e-9)  # 2 points always "separable"


def test_gate_abstains_semantics():
    t16 = gate.tau(16)
    assert gate.abstains(t16 - 1e-6, 16) is True     # below tau -> abstain
    assert gate.abstains(t16 + 1e-6, 16) is False    # above tau -> claim
    assert gate.abstains(0.99, 1) is True            # n<2 -> abstain
    with pytest.raises(ValueError):
        gate.tau(thresholds.GATE_TAU_N_MAX + 1)      # outside frozen table


# --- (D) domain gate: t_edge < T_EDGE_MIN is OUT-OF-DOMAIN, not FAIL ----------
def test_domain_gate_out_of_domain_below_t_min():
    v = validate.run(seeds=(13,), label="t_domain", guard=False, write=False,
                     t_edge=4.0)
    assert v["verdict"] == "OUT_OF_DOMAIN"
    assert v["verdict"] != "FAIL"
    assert "levels" not in v          # no scoring happened below the domain


def test_t_edge_min_is_sealed_value():
    assert thresholds.T_EDGE_MIN == thresholds.T_EDGE == 6.0  # area/theta_loc unchanged


# --- (H) per-seed path runs volume->gate->score and is well-formed ------------
@pinned
def test_per_seed_path_well_formed():
    out = validate._per_seed(seed=13, intensity=600.0, t_edge=thresholds.T_EDGE,
                             guard=True)
    for k in ("sep_BH", "sep_MINK", "d", "valid", "covers",
              "abstained_BH", "abstained_MINK"):
        assert k in out
    assert np.isfinite(out["sep_BH"]) and np.isfinite(out["sep_MINK"])
