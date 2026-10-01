"""Exact symbolic checks accompanying the analytic proof (not replacing it).

Run: python3 verify_global_energy.py
Requires SymPy. Writes verification_global_energy.json next to this file.
"""
import json
from pathlib import Path
import sympy as s

x, y, t = s.symbols('x y t', real=True)
d = y-x
m = x+y-1
omega = x*(1-x)*y*(1-y)
chi = 1+m*m-d*d
cx = (1-x)**2*(1-y)+x*x*y
cy = (1-x)*(1-y)**2+x*y*y


def zero(expr):
    assert s.cancel(expr) == 0, s.factor(expr)


def op(f, z, kind):
    ft = f.subs(z, t)
    if kind == 'L':
        ans = s.integrate((z-t)*ft, (t, 0, z))/z
    elif kind == 'C':
        ans = (1-z)*s.integrate(t*ft, (t, 0, z))/z**2
    elif kind == 'R':
        ans = s.integrate((t-z)*ft, (t, z, 1))/(1-z)
    elif kind == 'E':
        ans = z*s.integrate((1-t)*ft, (t, z, 1))/(1-z)**2
    else:
        ans = s.integrate((z-t)*ft, (t, 0, z))-z*s.integrate((1-t)*ft, (t, 0, 1))
    return s.cancel(ans)


def K(f):
    ans = d*f
    for left, right, sign in [('L','C',1), ('C','L',-1), ('R','E',-1), ('E','R',1)]:
        ans += 6*sign*op(op(f, y, right), x, left)
    return s.expand(ans)


def integrate(f):
    poly = s.Poly(s.cancel(f), x, y)
    return sum(coef/s.Integer((i+1)*(j+1)) for (i,j), coef in poly.terms())


def X(f):
    return -cx*s.diff(f, x)+cy*s.diff(f, y)


def primitive(g):
    w = op(op(g, y, 'S'), x, 'S')
    return w, s.cancel(w/omega)


def boundary(g):
    mg = s.integrate((1-x)*g, (x, 0, 1))
    ng = s.integrate(x*g, (x, 0, 1))
    return s.factor(op(mg, y, 'C')-op(ng, y, 'E'))


def energy_pair(W, V):
    w, v = omega*W, omega*V
    return (integrate(s.diff(w,x,y)*s.diff(v,x,y))
            +s.Rational(3,8)*integrate((chi**2+4*m*m)*W*V)
            +s.Rational(3,2)*integrate(omega*(chi+2*m*m)*s.cancel(W/d)*s.cancel(V/d)))


def form(W, V):
    return (integrate(s.diff(omega*W,x,y)*s.diff(omega*V,x,y))
            +6*integrate(omega*X(W)*s.cancel(V/d)))


if __name__ == '__main__':
    zero(s.diff(-cx,x)+s.diff(cy,y))
    zero(X(m)-m*d)
    zero(X(chi)+d*chi)
    zero(X(omega)+d*(chi**2+4*m*m)/8)
    zero(-s.diff(-omega*cx/d,x)-s.diff(omega*cy/d,y)
         -(chi**2+4*m*m)/8-omega*(chi+2*m*m)/(2*d*d))

    # Exact piecewise integral for <j_x,j_y>, on 0<x<y<1.
    inner = (s.integrate(t*t/(x*y), (t,0,x))
             +s.integrate(t*(1-t)/((1-x)*y), (t,x,y))
             +s.integrate((1-t)**2/((1-x)*(1-y)), (t,y,1)))
    zero(inner-s.Rational(1,3)+d*d/(6*y*(1-x)))

    rows = []
    polys = [d, d*m, d*x*y, d*(x*x+y*y), d*x*x*y*y]
    for g in polys:
        w, W = primitive(g)
        b = boundary(g)
        p, q = -W.subs(x,0), -W.subs(x,1)
        zero(b-(1-y)*s.diff((1-y)*p,y)-y*s.diff(y*q,y))
        zero(K(g)-d*g-6*X(W)-6*(b+b.subs(y,x)))
        en = energy_pair(W,W)
        flux = 6*integrate((b+b.subs(y,x))*s.cancel(w/d))
        lhs = integrate(K(g)*s.cancel(w/d))
        zero(lhs-en-flux)
        rows.append({'g':str(g), 'b':str(b), 'energy':str(en),
                     'boundary_flux':str(flux), 'left_hand_side':str(lhs)})
    wt, Wt = primitive(d*m)
    zero(K(d*m))
    zero(Wt-d*m/24)
    zero(boundary(d*m)+(2*y-1)*(3*y*y-3*y+1)/24)
    zero(energy_pair(Wt,Wt)-s.Rational(1,30240))

    # Cross terms independently check the polarized integration by parts.
    U = primitive(polys[0])[1]
    V = primitive(polys[3])[1]
    zero((form(U,V)+form(V,U))/2-energy_pair(U,V))

    # A nonzero antisymmetric example with both marginals exactly zero.
    p2 = s.legendre(2,2*x-1)
    p3 = s.legendre(3,2*x-1)
    g0 = s.expand(p2*p3.subs(x,y)-p3*p2.subs(x,y))
    zero(boundary(g0))
    w0, W0 = primitive(g0)
    e0 = energy_pair(W0,W0)
    assert e0 > 0
    zero(integrate(K(g0)*s.cancel(w0/d))-e0)

    result = {'status':'all_exact_checks_passed', 'examples':rows,
              'zero_marginal_example_energy':str(e0),
              'note':'The L2 extension and variational reconstruction are proved analytically in the companion note.'}
    Path(__file__).with_name('verification_global_energy.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
