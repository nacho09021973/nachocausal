import sympy as s
import numpy as np
x,y,t=s.symbols('x y t')
def op(f,z,k):
 ft=f.subs(z,t)
 if k=='L': return s.cancel(s.integrate((z-t)*ft,(t,0,z))/z)
 if k=='C': return s.cancel((1-z)*s.integrate(t*ft,(t,0,z))/z**2)
 if k=='R': return s.cancel(s.integrate((t-z)*ft,(t,z,1))/(1-z))
 if k=='E': return s.cancel(z*s.integrate((1-t)*ft,(t,z,1))/(1-z)**2)
 return s.expand(s.integrate((z-t)*ft,(t,0,z))-z*s.integrate((1-t)*ft,(t,0,1)))
def K(f):
 out=(y-x)*f
 for a,b,sgn in [('L','C',1),('C','L',-1),('R','E',-1),('E','R',1)]:
  out+=6*sgn*op(op(f,y,b),x,a)
 return s.expand(out)
def integ(f):
 p=s.Poly(s.expand(f),x,y)
 return sum(c/s.Rational((i+1)*(j+1)) for (i,j),c in p.terms())
basis=[x**i*y**j-x**j*y**i for j in range(1,6) for i in range(j) if i+j<=6]
ks=[K(f) for f in basis]
ws=[op(op(f,y,'S'),x,'S') for f in basis]
for typ in ['d_w','diff_w','d_wxy','d_g']:
 if typ=='d_w': tests=[(y-x)*w for w in ws]
 if typ=='diff_w': tests=[s.diff(w,y)-s.diff(w,x) for w in ws]
 if typ=='d_wxy': tests=[(y-x)*s.diff(w,x,y) for w in ws]
 if typ=='d_g': tests=[(y-x)*f for f in basis]
 mat=s.Matrix([[integ(k*tst) for tst in tests] for k in ks]); mat=(mat+mat.T)/2
 vals=np.linalg.eigvalsh(np.array(mat,dtype=float))
 print(typ,vals,flush=True)
 print('principal minors 1-5',[s.factor(mat[:n,:n].det()) for n in range(1,6)],flush=True)
