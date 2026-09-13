"""B2 formal-sign gate.

This is a deliberately conservative stop-rule artifact.  It checks whether
the repository has the two ingredients needed for a finite-box proof:
pointwise outward-rounded interval evaluation and a validated outward-rounded
box-summation/quadrature layer for Z, Z', B and B'.  Pointwise interval support
alone is not promoted to an integral enclosure.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    try:
        import mpmath as mp  # noqa: F401
        pointwise_backend = hasattr(mp, "iv")
    except ImportError:
        pointwise_backend = False

    quantities = ["Z", "Z_prime", "B", "B_prime"]
    box_domain = {"U": [-1.5, 0.7], "V": [0.35, 0.9], "UV": [-1.35, 0.63]}
    box_partition = {
        "method": "finite_boxes_with_monotone_endpoint_bounds",
        "quantities": quantities,
        "implemented": False,
        "monotonicity": {
            "q_true_in_UV": "increasing on UV in [-1.35,0.63]",
            "G_in_UV": "increasing on [-1.35,0], decreasing on [0,0.63]",
            "angular_prob": "increasing in nonnegative budget",
        },
        "candidate_partition_M": 16,
        "candidate_box_counts": {
            "Z": 16 ** 2, "Z_prime": 4 * 16,
            "B": 16 ** 4, "B_prime": 4 * 16 ** 3,
        },
        "reason": (
            "The repository has pointwise interval arithmetic but mpmath.iv does "
            "not implement LambertW for this use, and there is no validated "
            "outward-rounded box summation layer. Implementing both would be "
            "infrastructure comparable to the parked B4 quadrature work."
        ),
    }
    out = {
        "unit": "PUENTE-3P1/B2_CORRECTED_FORMAL_SIGN_CERTIFICATE",
        "path": "lambda(t)=(1-t)*lambda0+t*lambda1",
        "t0": 0.5,
        "kernel": "q(uv)=2*exp(-s(uv)/2)/s(uv)^(3/2)",
        "formula": "rho_prime = B_prime/Z^2 - 2*(B/Z^2)*Z_prime/Z",
        "box_domain": box_domain,
        "frozen_inputs": True,
        "pointwise_interval_backend_available": pointwise_backend,
        "box_partition_enclosure": box_partition,
        "formal_drho_dt_enclosure": None,
        "formal_upper_bound_drho_dt": None,
        "stop_rule_triggered": True,
        "terminal": "B2_CORRECTED_CERTIFICATION_ROUTE_TOO_COSTLY",
        "promotion_rule": "B2_CORRECTED_POSITIVE iff formal_upper_bound(drho_dt) < 0",
        "no_new_path": True,
        "no_new_t0": True,
        "no_new_points": True,
        "no_search": True,
        "no_adjustment": True,
        "b3_executed": False,
        "b4_reopened": False,
    }
    print(json.dumps(out, indent=2))
    with open(HERE / "verification_b2_formal_sign_certificate.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
