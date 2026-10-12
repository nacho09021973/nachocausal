"""Controls for the B2.1 box certificate (dev; not part of the certificate).
(1) lb_rows_xy on lattice sources equals the gate's audited lb_rows bit for bit.
(2) negative control: one box over the whole [0.45, 0.55] must NOT certify at M=64."""
import sys
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[1] / "research_program" / "puente_3p1"
sys.path.insert(0, str(ROOT / "2026-10-12"))
import verify_b2_1_box_certificate as box  # noqa: E402
gate = box.gate

T = box.tables()
wt, qlo, glo, ghi, Flo, Fhi, bt, plo_p, phi_p = T
M = 32
Ug = np.linspace(-1.5, 0.7, M + 1); Vg = np.linspace(0.35, 0.9, M + 1)
n1 = M + 1
src = np.arange(0, n1 * n1, 7)
for fwd in (True, False):
    a = gate.lb_rows(src, fwd, Ug, Vg, M, wt, qlo, bt, plo_p, gate.N_TAU)
    b = box.lb_rows_xy(Ug[src // n1].copy(), Vg[src % n1].copy(), fwd, Ug, Vg, wt, qlo, bt, plo_p, gate.N_TAU)
    print("control 1, forward=%s: identical=%s  nonzero=%d" % (fwd, np.array_equal(a, b), int((a > 0).sum())))
r = box.run_box(box.T_LO, box.T_HI, 64, T)
print("control 2, single box [0.45,0.55], M=64: S_lo=%+.6f  (must be <= 0)" % r["S_lo"])
