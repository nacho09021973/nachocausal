"""Exact checks of a polynomial dual recursion, not a capacity-limit proof.

Only two steps for the first nontrivial target in each parity are checked.
The all-step identities and the missing residual estimate are in the note.
"""

from functools import lru_cache
import hashlib
import json
from pathlib import Path
import runpy

import sympy as s


ROOT = Path(__file__).resolve().parent
api = runpy.run_path(str(ROOT / "verify_joint_moments.py"))
x, y = api["x"], api["y"]
poly, integ = api["poly"], api["integ"]
omega = x*(1-x)*y*(1-y)
forward = api["legacy"]["polynomial_K"]
freeze = runpy.run_path(str(ROOT / "verify_capacity_distances.py"))["verify_freeze"]


@lru_cache(None)
def return_test(k):
    return api["return_test"](k)


def target(k):
    return sum((s.binomial(k, j)*2**j*(-1)**(k-j)*return_test(j)
                for j in range(k+1)), poly(0))


def weighted_adjoint(p):
    """K* (omega^2 p), through the frozen core/return decomposition."""
    f, r = api["construct"](p.as_expr())
    quotient = s.Poly(s.cancel(r/(x*(1-x))**2), x)
    returned = sum((c*return_test(j) for (j,), c in quotient.terms()), poly(0))
    return f+12*returned


def norm2(p):
    return integ(p*p)


def temporal_ratio(k):
    if k % 2 == 0:
        return s.S.Zero
    return s.Rational(105*(2*k+7), (k+2)*(k+4)*(k+6)*(k+8))


def main():
    freeze()
    gt = poly((y-x)*(x+y-1))
    bt = -(2*x-1)*(3*x*x-3*x+1)/24
    d1 = target(1)
    q = s.symbols("q", positive=True)
    rational_moment = -s.Rational(1, 1536)*(1/(q+2)+1/(q+4)-5/(q+6)+3/(q+8))
    assert s.cancel(rational_moment + (2*q+7)/(96*(q+2)*(q+4)*(q+6)*(q+8))) == 0
    for k in range(10):
        moment = api["integral_1"](bt*x**2*(1-x)**2*(2*x-1)**k)
        assert moment == -temporal_ratio(k)/10080
        assert integ(target(k)*gt) == moment
    assert norm2(gt) == s.Rational(1, 90)

    records = []
    for k in (0, 3):
        lam = temporal_ratio(k)
        h = target(k)-lam*d1
        assert integ(h*gt) == 0
        residual, p = h, poly(0)
        record = {"moment": k, "lambda": str(lam), "initial_norm_squared": str(norm2(h)),
                  "steps": []}
        for n in range(1, 3):
            kr = poly(forward(residual.as_expr()))
            ar = weighted_adjoint(kr)
            weighted_forward_norm = norm2(poly(omega)*kr)
            assert integ(residual*ar) == weighted_forward_norm
            updated = residual-4*ar
            p += 4*kr
            assert h-weighted_adjoint(p) == updated
            assert s.expand(api["reflect"](p.as_expr())-(-1)**k*p.as_expr()) == 0
            assert s.expand(api["reflect"](updated.as_expr())-(-1)**(k+1)*updated.as_expr()) == 0
            assert integ(updated*gt) == 0
            drop = norm2(residual)-norm2(updated)
            assert drop == 8*weighted_forward_norm-16*norm2(ar)
            assert drop >= 4*weighted_forward_norm >= 0
            degree_bound = k+6+10*(n-1)
            assert p.total_degree() <= degree_bound
            record["steps"].append({"step": n, "test_degree": p.total_degree(),
                                    "degree_bound": degree_bound,
                                    "residual_degree": updated.total_degree(),
                                    "residual_norm_squared": str(norm2(updated)),
                                    "weighted_forward_norm_squared_before_step": str(weighted_forward_norm),
                                    "exact_energy_identity": True})
            if n == 1:
                record["first_test_polynomial"] = str(s.factor(p.as_expr()))
            residual = updated
            print(f"k={k}, step={n}: exact recursion, parity and energy checks passed", flush=True)
        records.append(record)

    freeze()
    output = {"status": "explicit_recursion_verified_limit_open", "sympy_version": s.__version__,
              "records": records,
              "claim_ceiling": "No assertion that the residual norms tend to zero. No capacity table extended.",
              "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT / "verification_dual_recursion.json").write_text(json.dumps(output, indent=2)+"\n")


if __name__ == "__main__":
    main()
