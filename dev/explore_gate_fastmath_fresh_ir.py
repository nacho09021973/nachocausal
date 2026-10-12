"""Re-check the B2 gate's fast-math guard with FRESH (non-cached) IR (dev, 2026-10-12).

Finding: with numba cache=True, a dispatcher loaded from the on-disk cache returns an EMPTY
LLVM module from inspect_llvm ("Inspection disabled for cached code"), so the gate's guard
(verify_b2_path2_gate_certificate.fastmath_guard) passes vacuously on any cached rerun.  This
script runs the gate at a small M so all 19 kernels get signatures, then inspects each one
recompiled without cache, through the same fresh_ir the B2.1 box verifier uses."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1] / "research_program" / "puente_3p1"
sys.path.insert(0, str(ROOT / "2026-10-12"))
import verify_b2_1_box_certificate as box  # noqa: E402
gate = box.gate

cached = {fn.py_func.__name__: None for fn in gate.KERNELS}
gate.run(16)
gate._compile_helpers()
rows = []
for fn in gate.KERNELS:
    cached_len = min(len(fn.inspect_llvm(s)) for s in fn.signatures)
    irs = box.fresh_ir(fn)
    flags = sorted({m.group(0) for ir in irs for m in gate._FAST.finditer(ir)})
    rows.append((fn.py_func.__name__, cached_len, min(len(i) for i in irs), flags))
for r in rows:
    print("%-26s cached_ir_chars=%6d  fresh_ir_chars=%7d  flags=%s" % r)
print("ALL 19 GATE KERNELS CLEAN ON FRESH IR:", all(not r[3] for r in rows) and len(rows) == 19)
