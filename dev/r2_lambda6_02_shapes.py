import math
E = math.e
def W(rho, tau): return math.exp(rho/tau)*(rho/tau - 1.0)

def K(tau, rp, rq, vp, vq):
    Up = -math.exp(-vp/(2*tau))*W(rp, tau)
    Uq = -math.exp(-vq/(2*tau))*W(rq, tau)
    return (Uq - Up)*(vq - vp)/(E*tau)

shapes = {
 "A moderate":      (2.0, 0.5, 0.0, 1.0,  5.415261e-04),
 "B thin":          (1.3, 0.7, 0.0, 0.3,  9.516742e-05),
 "C very thin":     (1.1, 0.9, 0.0, 0.1,  1.508730e-06),
 "scan l=0.2":      (1.06,0.94,0.0, 0.06, 1.989860e-07),
 "scan l=0.05":     (1.015,0.985,0.0,0.015,7.843762e-10),
}
print(f"{'shape':>14} {'K(1)':>12} {'Kp(1)':>12} {'I_pred':>13} {'I_num':>13} {'I_num/I_pred':>13}")
for name,(rp,rq,vp,vq,Inum) in shapes.items():
    h=1e-7
    Kp=(K(1+h,rp,rq,vp,vq)-K(1-h,rp,rq,vp,vq))/(2*h)
    Ip=Kp*Kp/144.0
    print(f"{name:>14} {K(1,rp,rq,vp,vq):12.6f} {Kp:12.6f} {Ip:13.5e} {Inum:13.5e} {Inum/Ip:13.5f}")
