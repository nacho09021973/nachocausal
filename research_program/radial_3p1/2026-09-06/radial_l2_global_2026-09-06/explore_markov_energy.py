exec(open('/home/adnac/radial_l2_global_2026-09-06/explore_energy.py').read().split('basis=')[0])
z=s.symbols('z')
basis=[x**i*y**j-x**j*y**i for j in range(1,10) for i in range(j) if i+j<=9]
As=[s.Poly(s.integrate(s.integrate((y-x)*f,(x,0,y)),(y,0,z)),z) for f in basis]
Bs=[s.Poly(s.integrate(s.integrate((y-x)*f,(y,x,1)),(x,z,1)),z) for f in basis]
for mode in ['D','AB']:
 ds=[s.Poly(s.cancel((1-z)*a.as_expr()/z**2+z*b.as_expr()/(1-z)**2),z) for a,b in zip(As,Bs)] if mode=='D' else As+Bs
 if mode=='D': mat=s.Matrix([[p.nth(k) for p in ds] for k in range(max(p.degree() for p in ds)+1)])
 else: mat=s.Matrix([[p.nth(k) for p in As] for k in range(13)]+[[p.nth(k) for p in Bs] for k in range(13)])
 vecs=mat.nullspace(); fs=[s.expand(sum(v*b for v,b in zip(vec,basis))) for vec in vecs]
 print(mode,'dimensions',len(basis),len(fs),flush=True)
 ks=[K(f) for f in fs];tests=[s.cancel(f/(y-x)) for f in fs]
 Q=s.Matrix([[integ(k*tst) for tst in tests] for k in ks]);Q=(Q+Q.T)/2
 G=s.Matrix([[integ(a*b) for a in fs] for b in fs])
 from scipy.linalg import eigvalsh
 vals=eigvalsh(np.array(Q,dtype=float),np.array(G,dtype=float))
 print('generalized energy eigenvalues',vals,flush=True)
 print('Q first rows',Q[:3,:3],flush=True)
