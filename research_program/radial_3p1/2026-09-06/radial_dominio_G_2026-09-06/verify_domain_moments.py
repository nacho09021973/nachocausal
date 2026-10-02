"""Exact finite sections of a necessary and sufficient moment criterion for D(G).

No reconstructed W_b or numerical PDE solver is used.
Run: python3 verify_domain_moments.py --degree 4
Dependencies: SymPy.
"""
import argparse
import json
from pathlib import Path
import sympy as s

x, y, z = s.symbols('x y z', real=True)
a = x*(1-x)
omega = a*y*(1-y)
d = y-x
cx = (1-x)**2*(1-y)+x*x*y
cy = (1-x)*(1-y)**2+x*y*y


def poly(f):
    return s.Poly(f, x, y, domain=s.QQ)


def integ(f):
    f = f if isinstance(f, s.Poly) else poly(f)
    return sum(c/s.Integer((i+1)*(j+1)) for (i,j), c in f.terms())


def S(f, var):
    """Dirichlet inverse, acting on a polynomial in either variable."""
    ans = 0
    for (i,j), c in poly(f).terms():
        n = i if var == x else j
        other = y**j if var == x else x**i
        ans += c*other*(var**(n+2)-var)/s.Integer((n+1)*(n+2))
    return s.expand(ans)


def X(f):
    return -cx*s.diff(f,x)+cy*s.diff(f,y)


def construct(P):
    F = s.expand(d*omega**2*P-6*S(S(2*X(omega)*P+omega*X(P), y), x))
    r = s.expand(a*a*s.integrate(y*y*(1-y)**2*P,(y,0,1)))
    return poly(F), r


def bmoment(b, r):
    return s.integrate(b*r,(x,0,1))


def polynomial_K(g):
    def op(f, var, kind):
        t=s.Dummy('t')
        ft=f.subs(var,t)
        if kind=='L':
            out=s.integrate((var-t)*ft,(t,0,var))/var
        elif kind=='C':
            out=(1-var)*s.integrate(t*ft,(t,0,var))/var**2
        elif kind=='R':
            out=s.integrate((t-var)*ft,(t,var,1))/(1-var)
        else:
            out=var*s.integrate((1-t)*ft,(t,var,1))/(1-var)**2
        return s.cancel(out)
    result=d*g
    for left,right,sign in [('L','C',1),('C','L',-1),('R','E',-1),('E','R',1)]:
        result += 6*sign*op(op(g,y,right),x,left)
    return s.expand(result)


def main(degree):
    Ps=[]; Fs=[]; rs=[]; levels=[]
    for n in range(degree+1):
        for i in range(n//2+1):
            j=n-i
            P=x**i*y**j if i==j else x**i*y**j+x**j*y**i
            F,r=construct(P)
            Ps.append(P); Fs.append(F); rs.append(r)
        levels.append(len(Ps))
    M=s.Matrix([[integ(f*g) for g in Fs] for f in Fs])
    # An exact LDL decomposition verifies positivity at every finite section.
    _, diagonal=M.LDLdecomposition(hermitian=False)
    assert all(diagonal[i,i]>0 for i in range(M.rows))

    b_d=-(3*x*x-3*x+1)/12
    b_t=-(2*x-1)*(3*x*x-3*x+1)/24
    gd=d
    gt=d*(x+y-1)
    samples={'b_d':b_d, 'b_t':b_t, 'constant_1':s.Integer(1), 'linear_centered':2*x-1}
    full_c={name:s.Matrix([-12*bmoment(b,r) for r in rs]) for name,b in samples.items()}
    for name,g in [('b_d',gd),('b_t',gt)]:
        assert full_c[name] == s.Matrix([integ(poly(g)*f) for f in Fs])
        W=s.cancel(S(S(g,y),x)/omega)
        b=samples[name]
        assert s.cancel(d*g+6*X(W)+6*(b+b.subs(x,y))) == 0

    # Independently verify the adjoint test identity against the explicit core.
    for g in [gd,gt,d*x*y]:
        W=s.cancel(S(S(g,y),x)/omega)
        core=s.cancel(d*g+6*X(W))
        for i in range(min(4,len(Ps))):
            assert integ(core*omega**2*Ps[i]) == integ(poly(g)*Fs[i])

    assert polynomial_K(gd) == s.expand((a+y*(1-y))/2)
    assert polynomial_K(gt) == 0
    assert s.expand(Fs[0].as_expr()-omega*d*(1+2*(x+y-1)**2+11*omega)/10) == 0
    assert M[0,0] == s.Rational(23,12936000)

    # The normal reconstruction pencil maps y**beta to the constant 1.
    beta=s.symbols('beta',positive=True)
    kappa=(beta+1)*(beta+2)
    Syh=(y**(beta+2)-y)/kappa
    assert s.simplify(s.diff(Syh,y,2)-y**beta) == 0
    assert s.simplify(y*y**beta-kappa*Syh/y-1) == 0
    # At Re(sqrt(1+24/(3/2+i*tau)))=2, the positive tau**2
    # solves 16*tau**4-312*tau**2-351=0.
    critical=s.Rational(39,4)+3*s.sqrt(13)
    assert s.simplify(16*critical**2-312*critical-351) == 0

    records=[]; last={name:s.Integer(0) for name in samples}
    for n,size in enumerate(levels):
        block=M[:size,:size]
        inverse=block.inv(method='DM')
        record={'degree':n,'number_of_tests':size,'bounds':{}}
        for name,c in full_c.items():
            cn=c[:size,0]
            value=(cn.T*inverse*cn)[0]
            value=s.factor(value)
            assert value>=last[name]
            if name=='b_d': assert value<=s.Rational(1,6)
            if name=='b_t': assert value<=s.Rational(1,90)
            record['bounds'][name]={'exact':str(value),'decimal':float(value)}
            last[name]=value
        records.append(record)
        print(json.dumps(record),flush=True)

    # Compress each quadratic form to the first n+1 weighted moments of b.
    compressed=[]
    for n in range(min(degree,2)+1):
        size=levels[n]
        R=s.Matrix([[s.Poly(s.cancel(r/(a*a)),x).nth(k) for k in range(n+1)] for r in rs[:size]])
        H=144*R.T*M[:size,:size].inv()*R
        compressed.append({'degree':n,'H':[[str(v) for v in row] for row in H.tolist()]})

    result={'status':'all_exact_checks_passed','max_degree':degree,
            'first_test':str(s.factor(Fs[0].as_expr())),
            'first_test_norm_squared':str(M[0,0]),
            'first_boundary_polynomial':str(s.factor(rs[0])),
            'known_admissible_data':{'b_d':str(b_d),'b_t':str(b_t)},
            'finite_sections':records,'compressed_moment_matrices':compressed,
            'warning':'Finite bounds do not certify boundedness of the infinite sequence.'}
    Path(__file__).with_name('verification_domain_moments.json').write_text(json.dumps(result,indent=2)+'\n')
    print('All exact checks passed.',flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--degree',type=int,default=4)
    main(parser.parse_args().degree)
