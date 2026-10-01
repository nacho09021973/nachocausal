"""Check the dual distance formula at the already frozen degrees 1 through 4.

This verifies finite identities, not density, asymptotics, or uniqueness.
Run from the repository root with Python 3 and SymPy.
"""

import hashlib
import json
from pathlib import Path
import runpy

import sympy as s


ROOT = Path(__file__).resolve().parent


def verify_freeze():
    manifest = json.loads((ROOT / "FROZEN_JOINT_CRITERION.json").read_text())
    for item in manifest["files"]:
        path = ROOT / item["path"]
        if hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
            raise RuntimeError(f"Frozen input changed: {path}")


def main():
    verify_freeze()
    api = runpy.run_path(str(ROOT / "verify_joint_moments.py"))
    x, y, a = api["x"], api["y"], api["a"]
    poly, integ = api["poly"], api["integ"]
    integral_1, construct = api["integral_1"], api["construct"]
    expected = json.loads((ROOT / "verification_joint_moments.json").read_text())
    degree = expected["max_degree"]
    if degree != 4:
        raise RuntimeError("This verification is restricted to the frozen degree-4 evidence.")

    fs, rs, levels = [], [], []
    for n in range(degree + 1):
        for i in range(n // 2 + 1):
            j = n-i
            p = x**i*y**j if i == j else x**i*y**j+x**j*y**i
            f, r = construct(p)
            fs.append(f)
            rs.append(r)
        levels.append(len(fs))
    ds = [api["return_test"](j) for j in range(degree + 1)]
    phis = [a**2*x**j for j in range(degree + 1)]
    psis = [a**2*(2*x-1)**j for j in range(degree + 1)]

    def bstar(weighted):
        coefficients = s.Poly(s.cancel(weighted/a**2), x)
        assert coefficients.degree() <= degree
        return sum((coefficients.nth(j)*ds[j] for j in range(degree + 1)), poly(0))

    def pair_inner(first, second):
        return integral_1(first[0]*second[0]) + integ(first[1]*second[1])

    generators = ([(12*r, f) for r, f in zip(rs, fs)]
                  + [(-phi, d) for phi, d in zip(phis, ds)]
                  + [(psis[1], poly(0))])
    total = s.Matrix([[pair_inner(v, w) for w in generators] for v in generators])
    ys = [f+12*bstar(r) for f, r in zip(fs, rs)]
    d1 = bstar(psis[1])
    previous_scalar = s.Integer(1)
    records = []
    for n in range(1, degree + 1):
        size = levels[n]
        indices = list(range(size)) + list(range(len(fs), len(fs)+n+1)) + [len(generators)-1]
        active = [generators[j] for j in indices]
        gram = total.extract(indices, indices)
        _, diagonal = gram.LDLdecomposition(hermitian=False)
        assert all(diagonal[j, j] > 0 for j in range(gram.rows))
        inverse = gram.inv(method="DM")
        active_y = ys[:size] + [d1]
        gram_y = api["gram"](active_y, active_y)
        inverse_y = gram_y.inv(method="DM")
        record = {"degree": n, "pair_generators": len(active), "moments": {}}
        scalar = s.Rational(1, 2**(n+1))
        for k in range(n+1):
            target = (psis[k], poly(0))
            target_norm = integral_1(psis[k]**2)
            rhs = s.Matrix([pair_inner(target, v) for v in active])
            coefficients = inverse*rhs
            capacity = s.factor(target_norm-(rhs.T*coefficients)[0])
            frozen = s.Rational(expected["finite_sections"][n]["capacities"][str(k)]["exact"])
            assert capacity == frozen
            assert capacity == 0 if k == 1 else capacity > 0
            first = s.expand(sum(coefficients[j]*v[0] for j, v in enumerate(active)))
            second = sum((coefficients[j]*v[1] for j, v in enumerate(active)), poly(0))
            residual = s.expand(psis[k]-first)
            assert integral_1(residual**2)+integ(second*second) == capacity
            assert s.expand(first.subs(x, 1-x)-(-1)**k*first) == 0
            assert api["reflect"](second.as_expr()) == s.expand((-1)**(k+1)*second.as_expr())

            dk = bstar(psis[k])
            rhs_y = s.Matrix([integ(dk*v) for v in active_y])
            eta = s.factor(integ(dk*dk)-(rhs_y.T*inverse_y*rhs_y)[0])
            assert eta >= capacity
            cancelled = second-bstar(residual)
            expected_cancelled = (sum((coefficients[j]*ys[j] for j in range(size)), poly(0))
                                  - dk + coefficients[-1]*d1)
            assert cancelled == expected_cancelled
            assert integ(cancelled*cancelled) >= eta
            if k % 2 == 0:
                assert coefficients[-1] == 0
            scalar += s.Rational(1, 2**(k+1))*capacity/target_norm
            record["moments"][str(k)] = {
                "capacity_matches_frozen": True,
                "distance_squared_exact": str(capacity),
                "eta_exact": str(eta),
                "parity_and_first_component_cancellation": "passed",
            }
        scalar = s.factor(scalar)
        assert 0 < scalar <= previous_scalar <= 1
        previous_scalar = scalar
        record["aggregate_c_exact"] = str(scalar)
        records.append(record)
        print(f"N={n}: dual distances match every frozen capacity; parity and cancellation passed",
              flush=True)

    verify_freeze()
    result = {
        "status": "all_exact_checks_passed",
        "degrees": [1, 2, 3, 4],
        "sympy_version": s.__version__,
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "frozen_manifest_sha256": hashlib.sha256((ROOT/"FROZEN_JOINT_CRITERION.json").read_bytes()).hexdigest(),
        "frozen_inputs_verified_before_and_after": True,
        "checks": records,
        "claim_ceiling": "Finite dual identities only; density and zero limits remain unproved.",
    }
    (ROOT/"verification_capacity_distances.json").write_text(json.dumps(result, indent=2)+"\n")


if __name__ == "__main__":
    main()
