"""Negative tests for the executed-IR fast-math guard of B2.1 / B3 (dev, 2026-10-12).
Each test must make the guard FAIL; the script exits non-zero if any is NOT caught:
 (1) a kernel loaded from a numba cache (the subprocess inherits this process's private
     NUMBA_CACHE_DIR, already filled by it, so its first call is a cache hit);
 (2) the inspected IR set with one prange body's definition removed (closure);
 (3) a required mangled name absent from the inspected set (a fictitious name);
 (4) a numeric body that calls through a function pointer.
Plus the positive case: guard_kernels over the kernels a small B2.1 box runs, ok = True."""
import re
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research_program" / "puente_3p1" / "2026-10-12"))
import verify_b2_1_box_certificate as b  # noqa: E402

T = b.tables()
b.run_box(F(45, 100), F(451, 1000), 16, T)
g = b.fastmath_guard()
print("positive: ok =", g["ok"], "| parfor bodies", g["parfor_bodies_defined"])

irs, defined = b.executed_ir(b.lb_rows_xy)
body = sorted(d for d in defined if d.startswith("_ZN")
              and "__numba_parfor_gufunc_0x" in d and not d.startswith("_ZN7cpython"))[0]
pat = re.compile(r'^define [^\n]*@"?' + re.escape(body) + r'"?\(.*?^}\n', re.M | re.S)
cut = [pat.sub("", ir) for ir in irs]
assert sum(len(c) for c in cut) < sum(len(i) for i in irs)
req = [b.lb_rows_xy.overloads[s].fndesc.mangled_name for s in b.lb_rows_xy.signatures]
failures = []
for label, irset, required in (("(2) body removed", cut, req),
                               ("(3) required absent", irs, req + ["_ZN3fooB3v1E"])):
    try:
        b.closure_check(irset, required)
        print(label, ": NOT CAUGHT"); failures.append(label)
    except RuntimeError as e:
        print(label, ": caught --", str(e)[:90])
fake = 'define void @"%s"() {\n  %%fp = load ptr, ptr null\n  call void %%fp()\n  ret void\n}\n' % body
if b.indirect_calls_in_numeric_bodies([fake]):
    print("(4) indirect call in numeric body : caught")
else:
    print("(4) indirect call in numeric body : NOT CAUGHT"); failures.append("(4)")

code = ("import sys; sys.path.insert(0, %r); sys.path.insert(0, %r)\n"
        "import numpy as np, verify_b2_path2_gate_certificate as gate\n"
        "gate.k_below(np.linspace(-1, 1, 9), 0.1)\n"
        "src = open(%r).read(); i = src.index('_SYM_DEF = '); j = src.index('def guard_kernels')\n"
        "import re; ns = {'re': re}; exec(src[i:j], ns)\n"
        "try:\n    ns['executed_ir'](gate.k_below); print('(1) cached kernel : NOT CAUGHT')\n"
        "except RuntimeError as e:\n    print('(1) cached kernel : caught --', e)\n") % (
    str(ROOT / "research_program/puente_3p1/2026-10-11"), str(ROOT / "research_program/puente_3p1/2026-10-12"),
    str(ROOT / "research_program/puente_3p1/2026-10-12/verify_b2_1_box_certificate.py"))
out1 = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True).stdout.strip()
print(out1)
if "caught" not in out1 or "NOT CAUGHT" in out1:
    failures.append("(1)")
if not g["ok"]:
    failures.append("positive")
print("ALL NEGATIVE TESTS CAUGHT, POSITIVE OK" if not failures else "FAILURES: %s" % failures)
sys.exit(1 if failures else 0)
