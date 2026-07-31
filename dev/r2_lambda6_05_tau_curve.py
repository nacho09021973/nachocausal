import sys, math, numpy as np
sys.path.insert(0, "research_program/work_packages")
import wp4_kappa_numeric_reference as ref
E = math.e
lam=0.1; a=b=0.3
rp,rq,vp,vq = 1+a*lam, 1-a*lam, 0.0, b*lam

def K_fit(tau, M=44, N=160):
    build, cdens = ref.make_builder(rp,rq,vp,vq)
    fam = build(tau, N=N)
    g=(np.arange(M)+0.5)/M; acc=0.0
    for x in g:
        for y in g: acc += math.log(cdens(fam,x,y))*(x-0.5)*(y-0.5)
    return 144.0*acc/M**2

def dU(tau):  return ref.Utilde(tau,vq,rq)-ref.Utilde(tau,vp,rp)
def K_an(tau): return dU(tau)*(vq-vp)/(E*tau)

print(f"{'tau':>8} {'K_fit':>13} {'K_an':>13} {'ratio':>8} {'dU':>12}")
for tau in [0.994,0.997,1.0,1.003,1.006]:
    kf,ka = K_fit(tau), K_an(tau)
    print(f"{tau:8.4f} {kf:13.6e} {ka:13.6e} {ka/kf:8.4f} {dU(tau):12.6f}")
