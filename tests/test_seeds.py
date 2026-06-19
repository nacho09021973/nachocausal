"""The frozen seed sets and threshold table must satisfy their invariants."""

from nachocausal import thresholds as T


def test_validation_seeds_disjoint_from_dev():
    assert set(T.VALIDATION_SEEDS).isdisjoint(T.DEV_SEEDS)


def test_ensemble_size():
    assert len(T.VALIDATION_SEEDS) == T.ENSEMBLE == 20
    assert len(set(T.VALIDATION_SEEDS)) == 20  # no duplicates


def test_thresholds_from_intensity_not_realized_N():
    # ell shrinks with intensity; theta_loc/theta_stab are finite positive
    # constants per frozen intensity (cmte C2: never realized N).
    prev = None
    for lam in T.INTENSITIES:
        e = T.ell(lam)
        assert e > 0 and T.theta_loc(lam) > 0 and T.theta_stab(lam) > 0
        if prev is not None:
            assert e < prev  # denser -> finer discreteness scale
        prev = e


def test_primary_endpoint_is_top_intensity():
    assert T.PRIMARY_INTENSITY == max(T.INTENSITIES)
