"""B4.3 certification gate.

Checks the available interval backend and refuses to promote quadrature convergence differences
to rigorous enclosures. The scientific terminal is intentionally a park, not a rank claim.
"""
import json
import mpmath as mp
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    # Pointwise interval arithmetic is available, but a certified remainder for the nested
    # boundary/cone integrals is not implemented in the repository yet.
    x = mp.iv.mpf(["0.35", "0.35"])
    pointwise_interval_backend = True
    out = {
        "unit": "PUENTE-3P1/B4.3",
        "same_point_chart_scaling": True,
        "interval_backend": "mpmath.iv",
        "pointwise_interval_backend_available": pointwise_interval_backend,
        "twelve_entry_enclosure": False,
        "quadrature_remainder_certificate": False,
        "shared_dependency_propagation_Z_F_P": False,
        "no_finite_difference": True,
        "no_rescaling": True,
        "no_new_point": True,
        "no_new_chart": True,
        "no_search": True,
        "no_seeds": True,
        "no_monte_carlo": True,
        "terminal": "B4.3_IMPLEMENTATION_FAILURE",
        "scientific_status": "N3_RANK_UNRESOLVED",
        "reason": (
            "Pointwise interval arithmetic exists, but no formal interval quadrature/remainder "
            "layer certifies the nested F/P shape-derivative integrals."
        ),
    }
    print(json.dumps(out, indent=2))
    with open(HERE / "verification_b4_3_certified_enclosure.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
