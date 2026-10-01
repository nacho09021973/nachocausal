"""PUENTE-3P1 / B4.0 — exact symbolic check of the n=3 moment reduction."""
import json
import sympy as sp

rho, f2, p2, pf = sp.symbols("rho f2 p2 pf")
pc = 6 * pf
pv = 3 * f2 - pc
pl = 3 * p2 - pc
pe = 3 * rho - 6 * f2 - 6 * p2 + 6 * pf
pa = 1 - 3 * rho + 3 * f2 + 3 * p2

T = sp.Matrix([[3, -6, -6, 6], [0, 3, 0, -6],
               [0, 0, 3, -6], [0, 0, 0, 6]])
m = sp.Matrix([rho, f2, p2, pf])
q = sp.Matrix([pe, pv, pl, pc])

out = {
    "unit": "PUENTE-3P1/B4.0",
    "q_equals_Tm": bool(q == T * m),
    "det_T": int(T.det()),
    "T_invertible": bool(T.det() != 0),
    "sum_probabilities": sp.simplify(pa + pe + pv + pl + pc),
    "comparable_pair_identity": sp.simplify(pe + 2 * pv + 2 * pl + 3 * pc - 3 * rho),
    "n3_independent_moments": ["rho", "E[f^2]", "E[p^2]", "E[p*f]"],
    "B4_execution_authorized": False,
}
assert out["q_equals_Tm"]
assert out["det_T"] == 162
assert out["sum_probabilities"] == 1
assert out["comparable_pair_identity"] == 0
print(json.dumps(out, indent=2, default=str))
with open(__file__.rsplit("/", 1)[0] + "/verification_b4_0_moment_reduction.json", "w") as fh:
    json.dump(out, fh, indent=2, default=str)
