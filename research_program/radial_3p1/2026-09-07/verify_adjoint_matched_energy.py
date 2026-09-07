"""Exact test of the energy multiplier suggested by the adjoint null mode.

Tests one proposed inequality, without extending the capacity table.
A negative rational witness refutes that inequality, not radial uniqueness.
"""

import argparse
import hashlib
import json
from pathlib import Path
import runpy

import sympy as s


ROOT = Path(__file__).resolve().parent


def negative_witness(matrix):
    current = matrix
    vectors = s.eye(matrix.rows)
    while current.rows:
        pivot = next((i for i in range(current.rows) if current[i, i] != 0), None)
        if pivot is None:
            edge = next(((i, j) for i in range(current.rows)
                         for j in range(i+1, current.rows) if current[i, j] != 0), None)
            if edge is None:
                return None
            i, j = edge
            v = s.zeros(current.rows, 1)
            v[i], v[j] = 1, -s.sign(current[i, j])
            return vectors*v
        if current[pivot, pivot] < 0:
            return vectors[:, pivot]
        rest = [j for j in range(current.rows) if j != pivot]
        transform = s.zeros(current.rows, len(rest))
        for k, j in enumerate(rest):
            transform[j, k] = 1
            transform[pivot, k] = -current[pivot, j]/current[pivot, pivot]
        vectors = vectors*transform
        current = transform.T*current*transform
    return None


def simplify_witness(matrix, witness):
    """Round only coordinates in the exact constraint nullspace."""
    normalized = witness / max(abs(c) for c in witness)
    for scale in (1, 10, 100, 1000, 10000):
        candidate = normalized.applyfunc(lambda c: s.floor(scale*c+s.Rational(1, 2)))
        if (candidate.T*matrix*candidate)[0] < 0:
            return candidate
    return witness


def centered_integral(expression, m, d):
    """Integrate over |m|+|d|<1, including the Jacobian 1/2."""
    value = s.S.Zero
    for (i, j), coefficient in s.Poly(expression, m, d).terms():
        if i % 2 == 0 and j % 2 == 0:
            value += 2*coefficient*s.factorial(i)*s.factorial(j)/s.factorial(i+j+2)
    return value


def main(degree):
    api = runpy.run_path(str(ROOT / "verify_joint_moments.py"))
    verify = runpy.run_path(str(ROOT / "verify_capacity_distances.py"))["verify_freeze"]
    verify()
    x, y = api["x"], api["y"]
    poly, integ = api["poly"], api["integ"]
    kernel, primitive = api["legacy"]["polynomial_K"], api["legacy"]["S"]
    omega = x*(1-x)*y*(1-y)
    chi = 2*((1-x)*(1-y)+x*y)
    gt = (y-x)*(x+y-1)
    records = []
    for parity in (0, 1):
        basis = []
        for n in range(1, degree+1):
            if n % 2 != parity:
                continue
            for i in range((n+1)//2):
                j = n-i
                basis.append(s.expand((2*x-1)**i*(2*y-1)**j-(2*x-1)**j*(2*y-1)**i))
        images = [kernel(g) for g in basis]
        ws = [s.cancel(primitive(primitive(g, y), x)/omega) for g in basis]
        tests = [s.cancel(chi*w/(y-x)) for w in ws]
        raw = s.Matrix([[integ(poly(image*test)) for test in tests] for image in images])
        symmetric = (raw+raw.T)/2
        diagonal = [s.Poly(image.subs(y, x), x) for image in images]
        constraint = s.Matrix([[p.nth(k) for p in diagonal] for k in range(degree+2)])
        nullspace = constraint.nullspace()
        restriction = s.Matrix.hstack(*nullspace) if nullspace else s.zeros(len(basis), 0)
        for scope, change in [("all_polynomials", s.eye(len(basis))),
                              ("exact_diagonal_constraint", restriction)]:
            form = change.T*symmetric*change
            witness = negative_witness(form)
            record = {"g_reflection_parity": parity, "boundary_parity": "odd" if parity == 0 else "even",
                      "scope": scope, "dimension": form.rows, "rank": form.rank(),
                      "positive_semidefinite_on_finite_space": witness is None}
            if witness is not None:
                witness = simplify_witness(form, witness)
                coefficients = change*witness
                g = s.expand(sum(c*f for c, f in zip(coefficients, basis)))
                kg = kernel(g)
                wg = s.cancel(primitive(primitive(g, y), x)/omega)
                value = integ(poly(s.cancel(kg*chi*wg/(y-x))))
                assert value == (witness.T*form*witness)[0] < 0
                if scope == "exact_diagonal_constraint":
                    assert s.expand(kg.subs(y, x)) == 0
                assert s.expand(api["reflect"](g)-(-1)**parity*g) == 0
                record["witness_g"] = str(s.factor(g))
                record["energy_exact"] = str(value)
                record["diagonal_Kg"] = str(s.factor(kg.subs(y, x)))
                if scope == "exact_diagonal_constraint":
                    m, d = s.symbols("m d")
                    centered = s.expand(g.subs({x: (1+m-d)/2, y: (1+m+d)/2},
                                               simultaneous=True))
                    integrand = s.cancel(kg*chi*wg/(y-x))
                    transformed = s.expand(integrand.subs(
                        {x: (1+m-d)/2, y: (1+m+d)/2}, simultaneous=True))
                    assert centered_integral(transformed, m, d) == value
                    record["witness_in_m_d"] = str(s.factor(centered))
                    record["restricted_coordinates"] = [str(c) for c in witness]
                    # Impose the same temporal gauge as the capacities, not
                    # merely L2 orthogonality to the temporal polynomial.
                    psi1 = x**2*(1-x)**2*(2*x-1)
                    gauge = api["integral_1"](api["boundary"](g)*psi1)
                    correction = gauge / (-s.Rational(1, 10080))
                    gauged = s.expand(g-correction*gt)
                    assert api["integral_1"](api["boundary"](gauged)*psi1) == 0
                    assert s.expand(kernel(gauged)-kg) == 0
                    gauged_w = s.cancel(primitive(primitive(gauged, y), x)/omega)
                    assert integ(poly(s.cancel(kg*chi*gauged_w/(y-x)))) == value
                    record["temporal_gauge_correction"] = str(correction)
                    record["centered_integral_crosscheck"] = True
            records.append(record)
            print(json.dumps(record), flush=True)
        if parity == 0:
            test_gt = chi*(x+y-1)/24
            assert all(integ(poly(kg*test_gt)) == 0 for kg in images)

    verify()
    result = {"status": "exact_checks_completed", "max_polynomial_degree": degree,
              "test_multiplier": "chi * (J tensor J)g / (y-x)", "records": records,
              "sympy_version": s.__version__,
              "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "claim_ceiling": "Finite inequality test only; no capacity limit or uniqueness claim."}
    name = "verification_adjoint_matched_energy"
    if degree != 6:
        name += f"_degree_{degree}"
    (ROOT/f"{name}.json").write_text(json.dumps(result, indent=2)+"\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--degree", type=int, default=6)
    args = parser.parse_args()
    if args.degree < 2:
        parser.error("degree must be at least 2")
    main(args.degree)
