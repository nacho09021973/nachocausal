import sys, math, numpy as np
sys.path.insert(0, "research_program/work_packages")
import wp4_kappa_numeric_reference as ref
E = math.e

def K_fit(tau, rp, rq, vp, vq, M=40, N=140):
    build, cdens = ref.make_builder(rp, rq, vp, vq)
    fam = build(tau, N=N)
    g = (np.arange(M)+0.5)/M
    acc = 0.0
    for x in g:
        for y in g:
            acc += math.log(cdens(fam, x, y))*(x-0.5)*(y-0.5)
    return 144.0*acc/M**2

def K_an(tau, rp, rq, vp, vq):
    return (ref.Utilde(tau,vq,rq)-ref.Utilde(tau,vp,rp))*(vq-vp)/(E*tau)

I_num = {0.2:1.989860e-07, 0.1:1.252737e-08, 0.05:7.843762e-10}
print(f"{'lam':>6} {'dKfit/dtau':>13} {'dKan/dtau':>13} {'ratio':>8} "
      f"{'I from Kfit':>13} {'I_num':>13} {'ratio':>8}")
for lam in [0.2, 0.1, 0.05]:
    a=b=0.3; rp,rq,vp,vq = 1+a*lam, 1-a*lam, 0.0, b*lam
    h = 0.004*lam
    dKf = (K_fit(1+h,rp,rq,vp,vq)-K_fit(1-h,rp,rq,vp,vq))/(2*h)
    dKa = (K_an(1+h,rp,rq,vp,vq)-K_an(1-h,rp,rq,vp,vq))/(2*h)
    Ipred = dKf*dKf/144.0
    print(f"{lam:6.3f} {dKf:13.6f} {dKa:13.6f} {dKa/dKf:8.4f} "
          f"{Ipred:13.5e} {I_num[lam]:13.5e} {I_num[lam]/Ipred:8.4f}")
