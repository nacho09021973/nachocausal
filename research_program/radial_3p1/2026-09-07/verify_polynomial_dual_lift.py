"""Exact polynomial adjoint ansatz for the first even dual target.

This tests exact algebraic preimages, not numerical capacity asymptotics.
No frozen file is modified. A failed finite ansatz is not a density obstruction.
"""

import argparse
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import runpy

import sympy as s


ROOT = Path(__file__).resolve().parent
api = runpy.run_path(str(ROOT / "verify_joint_moments.py"))
x, y = api["x"], api["y"]
lx, ly, rx, ry = s.symbols("log_x log_y log_1mx log_1my")
variables = (x, y, lx, ly, rx, ry)


@lru_cache(None)
def lower(n, kind):
    if n == 0:
        return 1-x+x*lx
    if kind == "L":
        return s.Rational(1, n+1)-x/n+x**(n+1)/s.Integer(n*(n+1))
    if n == 1:
        return -x*lx-x+x*x
    return x/s.Integer(n*(n-1))-x**n/(n-1)+x**(n+1)/n


@lru_cache(None)
def op(n, kind):
    if kind in ("L", "C"):
        return lower(n, kind)
    reflected = sum(s.binomial(n, j)*(-1)**j*lower(j, "L" if kind == "R" else "C")
                    for j in range(n+1))
    return s.expand(reflected.subs({x: 1-x, lx: rx}, simultaneous=True))


@lru_cache(None)
def monomial_adjoint(i, j):
    out = (y-x)*x**i*y**j
    for left, right, sign in [("L", "C", 1), ("C", "L", -1),
                              ("R", "E", -1), ("E", "R", 1)]:
        out += 6*sign*op(i, left)*op(j, right).subs({x: y, lx: ly, rx: ry}, simultaneous=True)
    return s.Poly(out, *variables, domain=s.QQ)


def adjoint(theta):
    return sum((c*monomial_adjoint(i, j) for (i, j), c in api["poly"](theta).terms()),
               s.Poly(0, *variables, domain=s.QQ))


def boundary_conditions(theta):
    lower_edge = s.expand(s.diff(theta, x).subs(x, 0)
                          -(1-y)*s.diff(theta.subs(x, 0), y))
    upper_edge = s.expand(s.diff(theta, x).subs(x, 1)
                          -y*s.diff(theta.subs(x, 1), y))
    return lower_edge, upper_edge


def interior_equation(theta):
    omega = x*(1-x)*y*(1-y)
    cx = (1-x)**2*(1-y)+x*x*y
    cy = (1-x)*(1-y)**2+x*y*y
    transport = -cx*s.diff(theta, x)+cy*s.diff(theta, y)
    return s.expand(omega*s.diff((y-x)*theta, x, 2, y, 2)-6*transport)


def main(degree):
    verify = runpy.run_path(str(ROOT / "verify_capacity_distances.py"))["verify_freeze"]
    verify()
    left_mode = 2*((x*y)**2-((1-x)*(1-y))**2)
    assert adjoint(s.Integer(1)).as_expr() == y-x
    assert adjoint(left_mode).is_zero
    common_image = s.Poly((y-x)*((x*y)**2+((1-x)*(1-y))**2), *variables, domain=s.QQ)
    assert adjoint((x*y)**2) == common_image
    assert adjoint(((1-x)*(1-y))**2) == common_image
    assert interior_equation(left_mode) == 0
    assert interior_equation(s.Integer(1)) == 0
    ii, jj = s.symbols("i j", integer=True, nonnegative=True)
    # For i >= 2, the recurrence pivot is bounded below by 2*(j-1)**2+22.
    pivot = ii*(ii-1)*jj*(jj+1)+6*(2*ii-jj)
    assert s.expand(pivot.subs(ii, 2) - (2*(jj-1)**2+22)) == 0
    assert s.expand(pivot.subs(ii, 1) - 6*(2-jj)) == 0
    for n in range(1, 9):
        for i in range(n+1):
            j = n-i
            expression = s.Poly(interior_equation(x**i*y**j), x, y)
            assert expression.coeff_monomial(x**(i+1)*y**j) == -i*(i+1)*j*(j-1)+6*(i-2*j)
            assert expression.coeff_monomial(x**i*y**(j+1)) == i*(i-1)*j*(j+1)+6*(2*i-j)
    # Establish signs through duality against the independent forward formula.
    for theta in [s.Integer(1), ((1-x)*(1-y))**2, (x*y)**2,
                  (x*(1-x)*y*(1-y))**2]:
        image = adjoint(theta)
        assert all(not any(index[2:]) for index, _ in image.terms())
        expression = image.as_expr()
        assert boundary_conditions(theta) == (0, 0)
        for g in [y-x, (y-x)*(x+y-1), (y-x)*x*y]:
            assert api["integ"](api["poly"](g*expression)) == api["integ"](
                api["poly"](api["legacy"]["polynomial_K"](g)*theta))

    basis = []
    images = []
    for n in range(0, degree+1, 2):
        for i in range(n//2+1):
            j = n-i
            theta = ((2*x-1)**i*(2*y-1)**j if i == j else
                     (2*x-1)**i*(2*y-1)**j+(2*x-1)**j*(2*y-1)**i)
            basis.append(s.expand(theta))
            images.append(adjoint(theta))
    target = s.Poly(api["return_test"](0).as_expr(), *variables)
    terms = sorted(set(target.monoms()).union(*(set(image.monoms()) for image in images)))
    dictionaries = [image.as_dict() for image in images]
    target_dict = target.as_dict()
    matrix = s.Matrix([[d.get(term, 0) for d in dictionaries] for term in terms])
    rhs = s.Matrix([target_dict.get(term, 0) for term in terms])
    reduced, pivots = matrix.row_join(rhs).rref()
    consistent = matrix.cols not in pivots
    result = {"degree": degree, "parity": "even", "target": "B_star_a_squared",
              "left_polynomial_null_mode": str(s.factor(left_mode)),
              "K_star_1": "y - x", "K_star_left_mode": "0",
              "K_star_I_squared_equals_K_star_J_squared": str(s.factor(common_image.as_expr())),
              "interior_recurrence_checks": "passed",
              "ansatz_dimension": len(basis), "equations": len(terms),
              "matrix_rank": len([p for p in pivots if p < matrix.cols]),
              "augmented_rank": len(pivots), "exact_polynomial_lift_exists": consistent}
    if consistent:
        coefficients = s.zeros(matrix.cols, 1)
        for row, col in enumerate(pivots):
            coefficients[col] = reduced[row, -1]
        theta = s.expand(sum(c*p for c, p in zip(coefficients, basis)))
        assert adjoint(theta) == target
        assert boundary_conditions(theta) == (0, 0)
        result["theta_exact"] = str(s.factor(theta))
    else:
        result["claim_ceiling"] = "No exact symmetric even polynomial preimage up to this degree; approximation remains undecided."
    verify()
    result["verifier_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (ROOT/"verification_polynomial_dual_lift.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--degree", type=int, default=8)
    args = parser.parse_args()
    if args.degree < 0 or args.degree % 2:
        parser.error("degree must be a nonnegative even integer")
    main(args.degree)
