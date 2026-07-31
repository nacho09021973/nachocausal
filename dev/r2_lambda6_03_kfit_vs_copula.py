import sys, math, numpy as np
sys.path.insert(0, "research_program/work_packages")
import wp4_kappa_numeric_reference as ref
E = math.e

def K_analytic(tau, rp, rq, vp, vq):
    Up = ref.Utilde(tau, vp, rp); Uq = ref.Utilde(tau, vq, rq)
    return (Uq-Up)*(vq-vp)/(E*tau)

print(f"{'lambda':>7} {'K_fit':>13} {'K_analytic':>13} {'K_an/K_fit':>11}")
for lam in [0.3, 0.2, 0.1, 0.05]:
    a=b=0.3
    rp, rq, vp, vq = 1+a*lam, 1-a*lam, 0.0, b*lam
    build, cdens = ref.make_builder(rp, rq, vp, vq)
    fam = build(1.0, N=140)
    M = 40
    g = (np.arange(M)+0.5)/M
    acc = 0.0
    for x in g:
        for y in g:
            acc += math.log(cdens(fam, x, y))*(x-0.5)*(y-0.5)
    proj = acc/M**2
    K_fit = 144.0*proj
    Ka = K_analytic(1.0, rp, rq, vp, vq)
    print(f"{lam:7.3f} {K_fit:13.6e} {Ka:13.6e} {Ka/K_fit:11.5f}")
