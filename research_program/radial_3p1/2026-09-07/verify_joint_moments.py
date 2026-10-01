"""Exact finite checks for the joint admissibility/return moment criterion.

Run: python3 research_program/radial_3p1/2026-09-07/verify_joint_moments.py
Requires SymPy. Finite sections do not decide the asymptotic uniqueness question.
"""

import argparse
import hashlib
import json
from pathlib import Path
import runpy

import sympy as s


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "2026-09-06/radial_dominio_G_2026-09-06/verify_domain_moments.py"
legacy = runpy.run_path(str(SOURCE))
x, y = legacy["x"], legacy["y"]
poly, integ, construct = legacy["poly"], legacy["integ"], legacy["construct"]
a = x * (1 - x)


def integral_1(f):
    return sum(c / s.Integer(i + 1) for (i,), c in s.Poly(f, x).terms())


def swap(f):
    return f.subs({x: y, y: x}, simultaneous=True)


def reflect(f):
    return s.expand(f.subs({x: 1 - x, y: 1 - y}, simultaneous=True))


def boundary(g):
    """Canonical B, evaluated independently through its two marginals."""
    t = s.Dummy("t")
    mg = s.integrate((1 - x) * g, (x, 0, 1)).subs(y, t)
    ng = s.integrate(x * g, (x, 0, 1)).subs(y, t)
    return s.cancel(
        (1 - x) * s.integrate(t * mg, (t, 0, x)) / x**2
        - x * s.integrate((1 - t) * ng, (t, x, 1)) / (1 - x)**2
    )


def return_test(k):
    t = s.Dummy("t")
    cstar = x * s.integrate(t**k * (1 - t)**3, (t, x, 1))
    estar = (1 - x) * x**(k + 4) / s.Integer(k + 4)
    raw = (1 - x) * cstar.subs(x, y) - x * estar.subs(x, y)
    return poly((raw - swap(raw)) / 2)


def gram(left, right):
    return s.Matrix([[integ(f * g) for g in right] for f in left])


def centered_row(k, size):
    return s.Matrix(1, size, [s.binomial(k, j) * 2**j * (-1)**(k - j)
                             if j <= k else 0 for j in range(size)])


def rational_record(value):
    value = s.factor(value)
    return {"exact": str(value), "decimal": float(value)}


def main(degree):
    fs, rs, levels = [], [], []
    for n in range(degree + 1):
        for i in range(n // 2 + 1):
            j = n - i
            p = x**i * y**j if i == j else x**i * y**j + x**j * y**i
            f, r = construct(p)
            fs.append(f)
            rs.append(r)
        levels.append(len(fs))

    ds = [return_test(k) for k in range(degree + 1)]
    assert all(f.as_expr().subs(x, 0) == 0 for f in fs)
    for k, dk in enumerate(ds):
        trace = dk.as_expr().subs(x, 0)
        assert s.cancel(s.diff(2*trace/y, y) + (1-y)**3*y**k) == 0
    mass = gram(fs, fs)
    cross = gram(fs, ds)
    returned = gram(ds, ds)
    gd, gt = y - x, (y - x) * (x + y - 1)
    bd = -(3*x*x - 3*x + 1) / 12
    bt = -(2*x - 1) * (3*x*x - 3*x + 1) / 24
    assert s.expand(boundary(gt) - bt) == 0
    assert s.expand(boundary(gd) - bd - a/12) == 0
    assert integral_1((bd - boundary(gd)) * a**2) == -s.Rational(1, 1680)
    temporal_gauge = integral_1(bt * a**2 * (2*x - 1))
    assert temporal_gauge == -s.Rational(1, 10080)

    for g in [gd, gt, (y-x)*x*y, (y-x)*(x*x+y*y)]:
        bg = boundary(g)
        for k, dk in enumerate(ds):
            assert integ(poly(g) * dk) == integral_1(bg * a**2 * x**k)
        assert s.expand(boundary(reflect(g)) + bg.subs(x, 1-x)) == 0

    records, previous = [], {}
    previous_h = None
    previous_sigma00 = None
    previous_capacity = {}
    for n, size in enumerate(levels):
        m = mass[:size, :size]
        mi = m.inv(method="DM")
        l = cross[:size, :n+1]
        z = returned[:n+1, :n+1]
        sigma = z - l.T * mi * l
        _, diagonal = sigma.LDLdecomposition(hermitian=False)
        # Positivity is checked only for the requested finite levels.
        assert all(diagonal[i, i] > 0 for i in range(n+1))
        si = sigma.inv(method="DM")
        r = s.Matrix([[s.Poly(s.cancel(p/a**2), x).nth(k) for k in range(n+1)]
                      for p in rs[:size]])
        h = 144 * r.T * mi * r
        jmat = s.eye(n+1) + 12 * l.T * mi * r
        joint_h = h + jmat.T * si * jmat

        # Independent check against the full Gram system, without Schur inversion.
        full_gram = m.row_join(l).col_join(l.T.row_join(z))
        rhs = (-12*r).col_join(s.eye(n+1))
        assert joint_h == rhs.T * full_gram.inv(method="DM") * rhs
        if previous_h is not None:
            padded = s.zeros(n+1)
            padded[:n, :n] = previous_h
            assert (joint_h - padded).is_positive_semidefinite is True
        previous_h = joint_h

        # Centered moment coordinates split both energy forms into parity blocks.
        change = s.Matrix.vstack(*(centered_row(k, n+1) for k in range(n+1)))
        ci = change.inv()
        for matrix in [h, joint_h]:
            centered = ci.T * matrix * ci
            assert all(centered[i, k] == 0 for i in range(n+1)
                       for k in range(n+1) if (i+k) % 2)

        record = {"degree": n, "reconstruction_tests": size,
                  "return_tests": n+1, "schur_rank": n+1, "samples": {}}
        for name, b in [("b_t", bt), ("b_d", bd), ("constant_1", s.Integer(1))]:
            u = s.Matrix([integral_1(b*a**2*x**k) for k in range(n+1)])
            q = (u.T*h*u)[0]
            qjoint = s.factor((u.T*joint_h*u)[0])
            assert qjoint >= q
            assert qjoint >= previous.get(name, 0)
            previous[name] = qjoint
            if name == "b_t":
                assert qjoint <= s.Rational(1, 90)
                assert rhs*u == s.Matrix(
                    [integ(poly(gt)*f) for f in fs[:size]+ds[:n+1]])
            if name == "b_d" and n >= 2:
                assert qjoint > s.Rational(1, 6)
            defect = u - l.T*mi*(-12*r*u)
            assert qjoint >= q + defect[0]**2 / sigma[0, 0]
            record["samples"][name] = {
                "Q": rational_record(q), "joint_Q": rational_record(qjoint),
                "return_defect_moment_0": rational_record(defect[0]),
            }
        if previous_sigma00 is not None:
            assert sigma[0, 0] <= previous_sigma00
        previous_sigma00 = sigma[0, 0]
        record["schur_00"] = rational_record(sigma[0, 0])

        # Include the minimum L2 norm realizing the prescribed weighted moments.
        weight = s.Matrix(n+1, n+1, lambda i, k: integral_1(a**4*x**(i+k)))
        energy = weight.inv(method="DM") + joint_h
        if n >= 1:
            inverse = energy.inv(method="DM")
            gauge = centered_row(1, n+1)
            restricted = inverse - (inverse*gauge.T*gauge*inverse)/(gauge*inverse*gauge.T)[0]
            assert gauge*restricted == s.zeros(1, n+1)
            capacities = {}
            for k in range(n+1):
                row = centered_row(k, n+1)
                capacity = s.factor((row*restricted*row.T)[0])
                assert capacity >= 0
                if k in previous_capacity:
                    assert capacity <= previous_capacity[k]
                previous_capacity[k] = capacity
                if k == 1:
                    assert capacity == 0
                elif capacity:
                    optimizer = restricted*row.T
                    assert (optimizer.T*energy*optimizer)[0] == capacity
                    assert (row*optimizer)[0] == capacity
                capacities[str(k)] = rational_record(capacity)
            record["capacities"] = capacities
        if n <= 2:
            record["joint_H"] = [[str(v) for v in line] for line in joint_h.tolist()]
        records.append(record)
        print(f"degree={n}: {size} reconstruction tests, {n+1} return tests; exact checks passed",
              flush=True)

    result = {
        "status": "all_exact_checks_passed", "max_degree": degree,
        "sympy_version": s.__version__,
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "temporal_centered_moment_1": str(temporal_gauge),
        "finite_sections": records,
        "claim_ceiling": "Finite identities and inequalities only; no asymptotic rate or uniqueness proof.",
    }
    target = ROOT / "verification_joint_moments.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Saved {target}", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--degree", type=int, default=4)
    args = parser.parse_args()
    if args.degree < 1:
        parser.error("--degree must be at least 1")
    main(args.degree)
