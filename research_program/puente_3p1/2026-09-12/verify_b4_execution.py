"""B4 execution preflight: deterministic n=3 moment Jacobian at frozen point.

Fixed Gauss quadrature and fixed central chart steps only. No search or Monte Carlo. The script
reports INCONCLUSIVE unless a certified minor enclosure is available.
"""
import json, math, sys
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre, lambertw

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from verify_b2_2_shape_derivative import q  # noqa: E402

XSTAR = np.array((2.5714285714285716, .4666666666666666, .63))
V0 = .35

def lam(x):
    v1 = V0*x[0]; uin = x[2]/v1; uout = uin/x[1]
    return v1, uout, uin

def G(uv):
    s = 1 + lambertw(-np.asarray(uv)/math.e, 0).real
    return s*np.exp(-s)

def ap(b): return (1-np.cos(np.minimum(math.pi,np.maximum(0,b))))/2

def h_bounds(ux,vx,uy,vy):
    f=(ux<=uy)&(vx<=vy); b=(uy<=ux)&(vy<=vx); ok=f|b
    a,c=np.minimum(ux,uy),np.maximum(ux,uy); d,e=np.minimum(vx,vy),np.maximum(vx,vy)
    du,dv=np.maximum(c-a,0),np.maximum(e-d,0)
    ub=np.maximum.reduce([q(a*d),q(a*e),q(c*d),q(c*e)])*np.sqrt(du*dv)
    vm=(d+e)/2; um=a+(c-a)/2
    lo=q(um*vm)*np.sqrt((c-a)*(e-d))
    lo[~ok]=0; ub[~ok]=0
    return ap(lo),ap(ub)

def moments(x,n=10):
    v1,uo,ui=lam(x); lo,hi=-uo,ui
    z,w=roots_legendre(n); V0=V0_GLOBAL; U=(z+1)*(hi-lo)/2+lo; V=(z+1)*(v1-V0)/2+V0
    Wu=w*(hi-lo)/2; Wv=w*(v1-V0)/2
    ux,vx,uy,vy=np.meshgrid(U,V,U,V,indexing='ij')
    wt=np.meshgrid(Wu,Wv,Wu,Wv,indexing='ij'); W=wt[0]*wt[1]*wt[2]*wt[3]*G(ux*vx)*G(uy*vy)
    hl,hu=h_bounds(ux,vx,uy,vy); h=(hl+hu)/2
    # future/past masses for each radial x, with h directed by coordinate order.
    xxu,xxv=np.meshgrid(U,V,indexing='ij'); yu,yv=np.meshgrid(U,V,indexing='ij')
    yl,yh=h_bounds(xxu[...,None,None],xxv[...,None,None],yu[None,None,...],yv[None,None,...])
    ww=Wu[:,None]*Wv[None,:]*G(yu*yv)
    future=np.sum(ww[None,None,...]*yh,axis=(2,3)); past=np.sum(ww[None,None,...]*yl,axis=(2,3))
    Z=float(np.sum(Wu[:,None]*Wv[None,:]*G(xxu*xxv)))
    f=future/Z; p=past/Z; wx=Wu[:,None]*Wv[None,:]*G(xxu*xxv)
    rho=float(np.sum(wx*(f+p))/Z); f2=float(np.sum(wx*f*f)/Z); p2=float(np.sum(wx*p*p)/Z); pf=float(np.sum(wx*f*p)/Z)
    return np.array([rho,f2,p2,pf])

V0_GLOBAL = .35

def main():
    base=moments(XSTAR); J=np.zeros((4,3)); h=1e-3
    for j in range(3):
        xp=XSTAR.copy(); xm=XSTAR.copy(); xp[j]+=h; xm[j]-=h
        J[:,j]=(moments(xp)-moments(xm))/(2*h)
    minor=float(np.linalg.det(J[:3,:]))
    out={"unit":"PUENTE-3P1/B4","frozen_point":XSTAR.tolist(),"moments":base.tolist(),"Dm_central_deterministic":J.tolist(),"minor_rho_f2_p2":minor,"no_search":True,"no_seeds":True,"no_monte_carlo":True,"certified_minor":False,"terminal":"B4_INCONCLUSIVE_BY_BOUNDS"}
    print(json.dumps(out,indent=2)); json.dump(out,open(HERE/"verification_b4_execution.json","w"),indent=2)
if __name__=='__main__': main()
