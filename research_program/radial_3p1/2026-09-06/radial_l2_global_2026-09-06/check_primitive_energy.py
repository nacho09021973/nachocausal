exec(open('/home/adnac/radial_l2_global_2026-09-06/explore_energy.py').read().split('basis=')[0])
a=x*(1-x);b=y*(1-y);A=a*b;d=y-x;m=x+y-1;q=1+m*m-d*d
bx=(1-x)**2*(1-y)+x*x*y;by=(1-x)*(1-y)**2+x*y*y
V=s.factor(-s.diff(A*(-bx)/d,x)-s.diff(A*by/d,y))
Vformula=(q*q+4*m*m)/8+A*(q+2*m*m)/(2*d*d)
assert s.factor(V-Vformula)==0
print('divergence identity exact',flush=True)
for g in [d,d*m,d*x*y,d*(x*x+y*y),d*x*x*y*y]:
 w=op(op(g,y,'S'),x,'S');W=s.cancel(w/A)
 p=-W.subs(x,0);r=-W.subs(x,1)
 ey=s.expand((1-y)*s.diff((1-y)*p,y)+y*s.diff(y*r,y))
 core=d*g+6*(-bx*s.diff(W,x)+by*s.diff(W,y)+ey+ey.subs(y,x))
 assert s.factor(core-K(g))==0
 F=s.cancel(W/d)
 energy=integ(s.diff(w,x,y)**2)+s.Rational(3,8)*integ((q*q+4*m*m)*W**2)+s.Rational(3,2)*integ(A*(q+2*m*m)*F**2)
 flux=6*integ((ey+ey.subs(y,x))*A*F)
 lhs=integ(K(g)*A*F)
 assert s.factor(lhs-energy-flux)==0
 print('g',g,'b',s.factor(ey),'energy',energy,'flux',flux,'lhs',lhs,flush=True)
