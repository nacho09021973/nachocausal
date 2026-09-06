exec(open('/home/adnac/radial_l2_global_2026-09-06/explore_energy.py').read().split('basis=')[0])
z=s.symbols('z')
def diag(f):
 A=s.integrate(s.integrate((y-x)*f,(x,0,y)),(y,0,z))
 B=s.integrate(s.integrate((y-x)*f,(y,x,1)),(x,z,1))
 return s.Poly(s.cancel((1-z)*A/z**2+z*B/(1-z)**2),z)
basis=[x**i*y**j-x**j*y**i for j in range(1,9) for i in range(j) if i+j<=8]
ds=[diag(f) for f in basis]
mat=s.Matrix([[p.nth(k) for p in ds] for k in range(max(p.degree() for p in ds)+1)])
vecs=mat.nullspace(); fs=[s.expand(sum(v*b for v,b in zip(vec,basis))) for vec in vecs]
print('dimensions',len(basis),len(fs),flush=True)
ks=[K(f) for f in fs];ws=[op(op(f,y,'S'),x,'S') for f in fs]
for typ in ['d_w','diff_w','d_wxy','d_g']:
 if typ=='d_w': tests=[(y-x)*w for w in ws]
 if typ=='diff_w': tests=[s.diff(w,y)-s.diff(w,x) for w in ws]
 if typ=='d_wxy': tests=[(y-x)*s.diff(w,x,y) for w in ws]
 if typ=='d_g': tests=[(y-x)*f for f in fs]
 mat=s.Matrix([[integ(k*tst) for tst in tests] for k in ks]);mat=(mat+mat.T)/2
 vals=np.linalg.eigvalsh(np.array(mat,dtype=float))
 print(typ,vals,flush=True)
 # Remove exact zero row/column for g_t when present; check principal minors.
 print('rank',mat.rank(),flush=True)
 if typ=='d_w':
  print('Q first rows',mat[:3,:3],flush=True)
