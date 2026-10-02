"""Checks for the explicit edge singular sequence; no uniqueness claim.

Run: python3 verify_edge_sequence.py
Requires numpy, scipy, sympy. Integrates separated tensors through 1D Gram
matrices, with logarithmic quadrature to resolve exponentially small strips.
"""
import json
import math
from pathlib import Path

import numpy as np
import sympy as s
from scipy.special import roots_legendre
from scipy.linalg import solve_triangular


def symbolic_checks():
    x, y, t = s.symbols("x y t", positive=True)

    def op(f, z, kind):
        ft = f.subs(z, t)
        if kind == "L":
            return s.cancel(s.integrate((z-t)*ft, (t, 0, z))/z)
        if kind == "C":
            return s.cancel((1-z)*s.integrate(t*ft, (t, 0, z))/z**2)
        if kind == "R":
            return s.cancel(s.integrate((t-z)*ft, (t, z, 1))/(1-z))
        return s.cancel(z*s.integrate((1-t)*ft, (t, z, 1))/(1-z)**2)

    gt = (y-x)*(x+y-1)
    kg = (y-x)*gt
    # R here is the positive reflected L. Thus its wedge enters with a minus.
    for a, b, sign in [("L", "C", 1), ("C", "L", -1),
                       ("R", "E", -1), ("E", "R", 1)]:
        kg += 6*sign*op(op(gt, y, b), x, a)
    assert s.simplify(kg) == 0
    # Independently fix the reflected sign using the supplied Markov identity,
    # including its diagonal correction, on a non-kernel polynomial.
    u, v, z = s.symbols("u v z", positive=True)
    test = (y-x)*x*y
    ktest = (y-x)*test
    for aa, bb, sign in [("L", "C", 1), ("C", "L", -1),
                         ("R", "E", -1), ("E", "R", 1)]:
        ktest += 6*sign*op(op(test, y, bb), x, aa)
    X, Y = s.Rational(1, 4), s.Rational(3, 4)
    d = Y-X
    input_g = (v-u)*u*v
    qleft = 6*u*(X+Y-X*Y-v)/(X**2*Y**2)
    qmid = 6/d*((1-Y)/Y**2+X/(1-X)**2)*(v-u)
    qright = 6*(1-v)*(u-X*Y)/((1-X)**2*(1-Y)**2)
    qg = s.integrate(qleft*input_g, (u, 0, X), (v, X, Y))
    qg += s.integrate(qmid*input_g, (u, X, v), (v, X, Y))
    qg += s.integrate(qright*input_g, (u, X, Y), (v, Y, 1))
    Az = s.integrate((v-u)*input_g, (u, 0, v), (v, 0, z))
    Bz = s.integrate((v-u)*input_g, (v, u, 1), (u, z, 1))
    Dz = (1-z)*Az/z**2+z*Bz/(1-z)**2
    rhs = d*test.subs({x: X, y: Y})-d*qg+6*(Dz.subs(z, X)+Dz.subs(z, Y))
    assert s.simplify(ktest.subs({x: X, y: Y})-rhs) == 0
    beta = (s.sqrt(17)-3)/2
    assert s.simplify((beta+1)*(beta+2)-4) == 0

    # Exact correction of the zeroth and first moments on the small strip.
    q = s.symbols("q", positive=True)  # sqrt(epsilon)
    r0, r1 = 2*(1-q), s.Rational(2, 3)*(1-q**3)
    A, B = 4*r0-6*r1, -6*r0+12*r1
    assert s.expand(r0-A-B/2) == 0
    assert s.expand(r1-A/2-B/3) == 0

    # The corner correction identity A_c' = z^3 k/3.
    z = s.symbols("z", positive=True)
    bc, bcprime, source, sourceprime = s.symbols("bc bcprime source sourceprime")
    c = z**3/(1-z)**3
    k = -9*(source+bc)/(z*(1-z)**4)-3*(sourceprime+bcprime)/(1-z)**3
    assert s.simplify(z**3*k/3+s.diff(c, z)*(source+bc)+c*(sourceprime+bcprime)) == 0
    eps = s.Rational(1, 4)
    bound = eps**3*(s.sqrt(3)/(2*(1-eps)**4)+s.sqrt(s.Rational(3, 8))/(1-eps)**3)
    assert float(bound) < 0.066
    return {"K_gt": "exactly zero", "Markov_identity_non_kernel_polynomial": "exact at (1/4,3/4)", "beta": float(beta),
            "two_moments": "exactly zero", "corner_identity": "exact",
            "corner_Neumann_bound_epsilon_1_4": float(bound)}


def log_rule(lo, hi, order=24):
    nodes, weights = roots_legendre(order)
    out, wout = [], []
    for left in np.arange(lo, hi, 1.0):
        right = min(left+1.0, hi)
        out.append((left+right)/2+(right-left)*nodes/2)
        wout.append((right-left)*weights/2)
    return np.concatenate(out), np.concatenate(wout)


def numerical_sequence(n, order=24):
    eps = math.exp(-n)
    beta = (math.sqrt(17)-3)/2
    r0 = 2*(1-math.sqrt(eps))
    r1 = 2*(1-eps**1.5)/3
    A, B = 4*r0-6*r1, -6*r0+12*r1
    v, wv = log_rule(0, n, order)
    zn, zw = roots_legendre(order)
    zn, zw = (zn+1)/2, zw/2
    # Three disjoint intervals: (0,eps^2), (eps^2,eps), (eps,1).
    xs = [eps**2*zn, eps*np.exp(-v), np.exp(-v)]
    ws = [eps**2*zw, eps*np.exp(-v)*wv, np.exp(-v)*wv]
    gram = np.zeros((12, 12))
    for region, (x, w) in enumerate(zip(xs, ws)):
        u = x/eps
        if region < 2:
            p0 = np.zeros_like(x)
            p1 = np.zeros_like(x)
            bare = np.zeros_like(x)
            if region == 1:
                bare = u**-0.5
                p0 = 2*(np.sqrt(u)-math.sqrt(eps))
                p1 = 2*(u**1.5-eps**1.5)/3
            b = (bare-A-B*u)/math.sqrt(n)
            i0 = (p0-A*u-B*u**2/2)/math.sqrt(n)
            i1 = (p1-A*u**2/2-B*u**3/3)/math.sqrt(n)
            a = b/math.sqrt(eps)
            la = math.sqrt(eps)*(i0-i1/u)
            ca = (1-x)*i1/(math.sqrt(eps)*u**2)
            ra = x*la/(1-x)
            ea = -x*math.sqrt(eps)*(i0-eps*i1)/(1-x)**2
        else:
            a = la = ca = ra = ea = np.zeros_like(x)
        ma = x*a
        h = x**beta if region == 2 else np.zeros_like(x)
        if region == 2:
            h0 = (x**(beta+1)-eps**(beta+1))/(beta+1)
            h1 = (x**(beta+2)-eps**(beta+2))/(beta+2)
        else:
            h0 = h1 = np.zeros_like(x)
        lh = h0-h1/x
        ch = (1-x)*h1/x**2
        low = np.maximum(x, eps)
        j0 = -np.expm1((beta+1)*np.log(low))/(beta+1)
        j1 = -np.expm1((beta+2)*np.log(low))/(beta+2)
        rh = (j1-x*j0)/(1-x)
        eh = x*(j0-j1)/(1-x)**2
        f = np.array([a, ma, la, ca, ra, ea, h, x*h, lh, ch, rh, eh])
        fw = f*np.sqrt(w)
        gram += fw@fw.T
    matrix = np.zeros((12, 12))
    for i, j, coefficient in [(0, 7, 1), (1, 6, -1), (2, 9, 6),
                              (3, 8, -6), (4, 11, -6), (5, 10, 6)]:
        matrix[i, j] += coefficient
        matrix[j, i] += coefficient
    vals, vecs = np.linalg.eigh(gram)
    root = (vecs*np.sqrt(np.maximum(vals, 0)))@vecs.T
    residual = np.linalg.norm(root@matrix@root)
    norm_g = math.sqrt(2*(gram[0, 0]*gram[6, 6]-gram[0, 6]**2))
    norm_a_exact = 1-(r0*A+r1*B)/n
    assert abs(gram[0, 0]-norm_a_exact) < 1e-10
    return {"n": n, "epsilon": eps, "norm_a_squared": gram[0, 0],
            "norm_Kg_over_norm_g": residual/norm_g,
            "sqrt_n_times_ratio": math.sqrt(n)*residual/norm_g}


def check_corner_correction():
    """Independent finite-scale check using a degree-2 shifted Legendre a.

    This tests the correction construction, not the asymptotic sequence.
    Its two moments vanish exactly, and epsilon=0.1 keeps the correction
    resolvable rather than exponentially below floating-point resolution.
    """
    beta, eps = (math.sqrt(17)-3)/2, 0.1
    H0 = (1-eps**(beta+1))/(beta+1)
    H1 = (1-eps**(beta+2))/(beta+2)

    def source(z):
        u = z/eps
        a = eps**-0.5*(6*u*u-6*u+1)
        a0 = eps**0.5*(2*u**3-3*u*u+u)
        a1 = eps**1.5*(1.5*u**4-2*u**3+0.5*u*u)
        B = -H1*a0+H0*a1
        Bd = -(H1-z*H0)*a
        F = -9*B/(z*(1-z)**4)-3*Bd/(1-z)**3
        return B, F

    def kernel(z, t):
        delta = np.maximum(t-z, 0)
        return (-3*z**0.5*delta**3*t**-1.5/(1-z)**4
                +3*z**1.5*delta**2*t**-1.5/(1-z)**3)

    results = []
    for N in [80, 160, 320]:
        x, w = roots_legendre(N)
        z, w = eps*(x+1)/2, eps*w/2
        _, F = source(z)
        mat = kernel(z[:, None], z[None, :])*w
        v = solve_triangular(np.eye(N)-mat, z**1.5*F)
        k = v/z**1.5
        moment = float(np.sum(w*z**3*k)/3)
        residual = []
        qx, qw = roots_legendre(100)
        for zz in np.linspace(0.01, 0.09, 9):
            q, ww = zz*(qx+1)/2, zz*qw/2
            _, ff = source(q)
            kk = ff+(kernel(q[:, None], z[None, :])@(w*v))/q**1.5
            Ac = np.sum(ww*q**3*kk)/3
            Bc = np.sum(w*np.maximum(z-zz, 0)**3*k)/3
            Bcross, _ = source(np.array([zz]))
            residual.append(float((1-zz)*Ac/zz**2+zz*(Bcross[0]+Bc)/(1-zz)**2))
        max_defect = max(abs(np.array(residual)))
        assert max_defect < 1e-11 and abs(moment) < 1e-13
        results.append({"nodes": N, "total_weighted_moment": moment,
                        "max_diagonal_defect_at_nine_points": max_defect})
    return results


if __name__ == "__main__":
    result = {"symbolic": symbolic_checks(),
              "sequence_before_corner_correction": [numerical_sequence(n) for n in [16, 32, 64, 128]]}
    # Independent quadrature refinement on the most strongly separated scales.
    refined = numerical_sequence(128, order=40)
    assert abs(refined["norm_Kg_over_norm_g"]-result["sequence_before_corner_correction"][-1]["norm_Kg_over_norm_g"]) < 1e-9
    result["quadrature_refinement"] = "24 versus 40 nodes per logarithmic interval: passed"
    result["corner_correction_independent_finite_scale_check"] = check_corner_correction()
    Path(__file__).with_name("verification.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
