import numpy as np
from scipy.special import eval_legendre, roots_legendre
from scipy.linalg import solve, eigvals
import json

def calc(N):
 M=N+7
 q,w=roots_legendre(M);x=(q+1)/2;w=w/2
 ps=np.array([np.sqrt(2*n+1)*eval_legendre(n,q) for n in range(N+2)])
 ds=np.zeros_like(ps)
 for n in range(1,N+2): ds[n]=np.sqrt(2*n+1)*2*n*(eval_legendre(n-1,q)-q*eval_legendre(n,q))/(1-q*q)
 e0=np.sqrt(2*np.arange(N+2)+1)*(-1.)**np.arange(N+2)
 e1=np.sqrt(2*np.arange(N+2)+1)
 a=x*(1-x); da=1-2*x
 X=x[:,None];Y=x[None,:];d=Y-X;omega=a[:,None]*a[None,:]
 bx=(1-X)**2*(1-Y)+X*X*Y;by=(1-X)*(1-Y)**2+X*Y*Y
 pairs=[(i,j) for j in range(1,N+1) for i in range(j)]
 F=[];D=[];T=[];BB=[]
 for i,j in pairs:
  f=(ps[i,:,None]*ps[j,None,:]-ps[j,:,None]*ps[i,None,:])/np.sqrt(2)
  fx=(ds[i,:,None]*ps[j,None,:]-ds[j,:,None]*ps[i,None,:])/np.sqrt(2)
  fy=(ps[i,:,None]*ds[j,None,:]-ps[j,:,None]*ds[i,None,:])/np.sqrt(2)
  div=np.divide(f,d,out=np.zeros_like(f),where=d!=0)
  np.fill_diagonal(div,(ps[i]*ds[j]-ps[j]*ds[i])/np.sqrt(2))
  vi=da*ps[i]+a*ds[i];vj=da*ps[j]+a*ds[j]
  mixed=(vi[:,None]*vj[None,:]-vj[:,None]*vi[None,:])/np.sqrt(2)
  F.append(div);D.append(mixed);T.append(6*omega*(-bx*fx+by*fy))
  p=-(e0[i]*ps[j]-e0[j]*ps[i])/np.sqrt(2)
  pd=-(e0[i]*ds[j]-e0[j]*ds[i])/np.sqrt(2)
  r=-(e1[i]*ps[j]-e1[j]*ps[i])/np.sqrt(2)
  rd=-(e1[i]*ds[j]-e1[j]*ds[i])/np.sqrt(2)
  BB.append((1-x)**2*pd-(1-x)*p+x*x*rd+x*r)
 F=np.array(F);D=np.array(D);T=np.array(T);BB=np.array(BB)
 ww=np.sqrt(w[:,None]*w[None,:]).ravel()
 ff=F.reshape(len(pairs),-1)*ww;dd=D.reshape(len(pairs),-1)*ww;tt=T.reshape(len(pairs),-1)*ww
 amat=dd@dd.T+tt@ff.T
 rmap=np.einsum('ixy,xy,y->ix',F,omega,w)
 rhs=-12*(rmap*w)@ps.T
 coeff=solve(amat.T,rhs)
 bmat=(BB*w)@ps.T
 feedback=bmat.T@coeff
 vals=eigvals(feedback)
 vals=vals[np.argsort(abs(vals-1))]
 return {'N':N,'eigenvalues_near_one':[[float(z.real),float(z.imag)] for z in vals[:8]],'core_min_symmetric_eig':float(np.linalg.eigvalsh((amat+amat.T)/2)[0])}
if __name__=='__main__':
 for n in [4,8,12,18,26]: print(json.dumps(calc(n)),flush=True)
