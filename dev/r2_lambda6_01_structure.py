import math
a, b = 0.3, 0.3
E = math.e

def W(rho, tau):
    return math.exp(rho/tau)*(rho/tau - 1.0)

def dU(lam, tau):
    """Delta Utilde = U(q) - U(p) for the reshaping scan, corners fixed."""
    rp, rq, vq = 1.0 + a*lam, 1.0 - a*lam, b*lam
    Up = -math.exp(-0.0/(2*tau))*W(rp, tau)
    Uq = -math.exp(-vq/(2*tau))*W(rq, tau)
    return Uq - Up

def Kfun(lam, tau):
    return dU(lam, tau)*(b*lam)/(E*tau)

# I from the script's scan, for comparison
I_num = {1.0:9.516742e-05, 0.5:7.372818e-06, 0.3:9.950784e-07,
         0.2:1.989860e-07, 0.1:1.252737e-08, 0.05:7.843762e-10}

print(f"{'lambda':>8} {'K(1)/l^2':>12} {'Kp(1)/l^2':>12} {'I_pred':>13} {'I_num':>13} {'ratio':>8}")
for lam in [1.0, 0.5, 0.3, 0.2, 0.1, 0.05]:
    h = 1e-6
    Kp = (Kfun(lam, 1.0+h) - Kfun(lam, 1.0-h))/(2*h)
    Ipred = Kp*Kp/144.0
    print(f"{lam:8.3f} {Kfun(lam,1.0)/lam**2:12.5f} {Kp/lam**2:12.5f} "
          f"{Ipred:13.5e} {I_num[lam]:13.5e} {I_num[lam]/Ipred:8.4f}")
