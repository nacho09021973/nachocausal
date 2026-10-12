Eres ASTRA, auditor independiente. No tienes acceso a ficheros, terminal, web ni herramientas: todo lo disponible está en este prompt. No escribas llamadas a herramientas. Etiqueta como [SOURCE] sólo lo que aparece abajo. Responde en español, como máximo 900 palabras.

### Tu intervención anterior (ronda 1)
[INFERENCE] El argumento analítico resiste los ataques de signos, normalización y rango. La concesión queda condicionada por una dependencia ejecutable ausente y por la distinción entre los intervalos internos y su serialización.

1. **§5.1 — Sustitución de `VN_FR`: `SE_SOSTIENE`.**

   [SOURCE] En el `run()` adjunto, `VN_FR` se consulta únicamente para obtener las velocidades normales. Las tablas, los pesos, `Z` y `B_hi` no dependen de ella. Las dos velocidades U de `e3` son positivas y las dos V son exactamente cero.

   [INFERENCE] La rama elegida para cero es válida **en este caso concreto**. Con `vn_lo = −ε`, multiplicar una cota superior no negativa de la integral de cara produce una contribución inferior a la contribución verdadera, que es cero. Para `Zprime`, el extremo inferior es negativo y el superior calculado con `vn_hi = +ε` es no negativo: ambos encierran cero.

   [INFERENCE] Esto no convierte esa rama en aritmética intervalar válida para cualquier velocidad cuyo intervalo cruce cero: usar `vn_hi` positivo con el peso inferior podría fallar para una velocidad verdadera positiva. Aquí salva el argumento conocer exactamente que la velocidad es cero.

   **Condición mínima de concesión:** [INFERENCE] que el objeto `gate` realmente ejecutado sea el adjunto, con esas velocidades exactas; véase el punto 6.

2. **§5.2 — Fórmula y signos de `dphi`: `SE_SOSTIENE`.**

   [SOURCE] El histórico define \(s(w)=1+W_0(-w/e)\), usa \(G(w)=s(w)e^{-s(w)}\) en las caras y las primitivas cúbicas indicadas para `fin` y `fout`.

   [INFERENCE] La equivalencia entre esas primitivas y las integrales de volumen se verifica algebraicamente:
   \[
   w=(1-s)e^s,\qquad dw=-s e^s\,ds,\qquad G(w)\,dw=-s^2\,ds.
   \]
   Por tanto, `fin` y `fout` son precisamente las integrales de ese \(G(UV)\) sobre las regiones interior y exterior. No falta un factor de normalización.

   [INFERENCE] En \(U=-u_{\rm out}\), desplazar el límite inferior con velocidad \(-du_{\rm out}\) aporta \(+du_{\rm out}J_{\rm uout}\). En \(U=u_{\rm in}\), el aporte es \(+du_{\rm in}J_{\rm uin}\). Los términos V llevan los signos superior positivo e inferior negativo. La interfaz \(U=0\) permanece fija, por lo que no aporta transporte. La regla del cociente da exactamente la fórmula implementada.

   **Condición mínima de concesión:** [INFERENCE] identidad del `G` importado con el usado en esta definición y aplicación de H4 a las operaciones intervalares nuevas. La coincidencia con valores flotantes históricos es un control, no su demostración.

3. **§5.3 — Cota burda de `|S(e2)|`: `SE_SOSTIENE`.**

   [SOURCE] H2 define el núcleo simétrico mediante \(p\), extendido por cero a pares incomparables, y H3 proporciona la fórmula de borde.

   [INFERENCE] Se tiene \(0\le h\le1\), luego
   \[
   0\le H(x)\le Z,\qquad
   0\le I_f=\int_f G H\le J_f Z.
   \]
   El núcleo simétrico no introduce aquí un factor 2: las orientaciones causales son excluyentes para pares estrictamente comparables.

   [INFERENCE] Como `e2` mueve una sola cara,
   \[
   S(e_2)=2v\left(I_f-\frac{J_fB}{Z}\right),
   \]
   y, usando positividad,
   \[
   |S(e_2)|\le2|v|J_f
   \left(Z_{\rm hi}+\frac{B_{\rm hi}}{Z_{\rm lo}}\right).
   \]
   Dividir por \(Z_{\rm lo}^2\) proporciona la cota implementada. La posible sobreestimación de `B_hi` sólo la debilita.

   **Condición mínima de concesión:** [INFERENCE] las envolventes heredadas, \(Z_{\rm lo}>0\) y la integral de cara superior certificada. No encuentro una hipótesis analítica adicional.

4. **§5.4 — Producto exterior e identificabilidad: `SE_SOSTIENE`.**

   [SOURCE] El código exige simultáneamente `d2.a > 0`, `drho3_lo.a > 0` y `W23_lo > 0`.

   [INFERENCE] Con esas positividades,
   \[
   W_{23}\ge
   \underline{\phi_2}\,\underline{\rho_3}
   -\overline{|\phi_3|}\,\overline{|\rho_2|}.
   \]
   No se emparejan indebidamente extremos ni se necesita conocer el signo de \(\rho_2\).

   [INFERENCE] Un testigo algebraico explícito es
   \[
   v=\rho_3\partial_{x_2}-\rho_2\partial_{x_3}.
   \]
   Entonces \(d\rho(v)=0\) y \(d\phi(v)=W_{23}>0\). El rango de la carta lo convierte en una dirección física. Además, la regularidad continua de las derivadas y \(d\rho\ne0\) permiten aplicar el teorema de la función implícita: hay una superficie local de nivel de \(\rho\) sobre la que \(\phi\) varía. Esto excluye reconstrucción local incluso sin presuponer una función reconstructora diferenciable.

   **Condición mínima de concesión:** [INFERENCE] las cotas anteriores y la regularidad heredada de H3.

5. **§5.5 — Carta y H5: `SE_SOSTIENE`.**

   [SOURCE] La reconstrucción es \(v_1=v_0x_1\), \(u_{\rm in}=x_3/v_1\), \(u_{\rm out}=u_{\rm in}/x_2\).

   [INFERENCE] Su diferenciación reproduce las columnas suministradas y da
   \[
   \det=-\frac{v_0u_{\rm out}}{x_2v_1}
   =-\frac{10133099161583616}{8106479329266893}\ne0.
   \]
   Los racionales exactos representan la carta matemática en el punto binary64. No deben confundirse con derivadas de un algoritmo de reconstrucción redondeado.

   [SOURCE] El histórico usa los mismos literales de `LSTAR`; H5 fija expresamente `path(0.5)` binary64.

   **Condición mínima de concesión:** [INFERENCE] mantener ese objeto y la quinta componente fija. No se concede transferencia al punto medio real.

6. **Pieza adicional — dependencia ejecutada y salida numérica.**

   **`REQUIERE_CORRECCIÓN` de trazabilidad.** [SOURCE] B3 obtiene `gate`, `b15` y `executed_ir` de `verify_b2_1_box_certificate`, cuyo cuerpo no está adjunto.

   [UNVERIFIED] No puede comprobarse aquí que ese módulo exporte exactamente la compuerta mostrada, preserve sus funciones o imponga efectivamente la caché vacía y la inspección del IR ejecutado. Una discrepancia permitiría que el código certificase otro integrando u otro ejecutable. El JSON declara el éxito, pero no cierra esa conexión.

   **Condición mínima de concesión:** [INFERENCE] acreditar esas identidades y las garantías efectivas del control B2.1, sin reabrir B1.5.

   **`MENOR` en la serialización.** [SOURCE] Los extremos intervalares se convierten mediante `float(...)`, sin conversión dirigida explícita.

   [INFERENCE] H4 no garantiza que esa conversión conserve el sentido de cada cota. Esto afecta a los últimos dígitos del JSON; no al test interno de positividad. Las cifras abreviadas de la nota tienen margen suficiente para absorber ese redondeo.

   **Condición mínima de concesión:** [INFERENCE] conceder las cifras exteriores abreviadas; no atribuir certificación dirigida a todos los dígitos serializados.

Veredicto: AUDIT_PASS_CONDITIONAL_B21_BINDING_AND_EXECUTED_IR
# Acta, ronda 2 — vinculación con B2.1 e IR ejecutado

**Casa:** ASTRA. Es la continuación de tu auditoría de B3. Allí diste
`AUDIT_PASS_CONDITIONAL_B21_BINDING_AND_EXECUTED_IR`: los puntos 1–5 se sostenían y quedaban dos
pendientes.

**Pendiente 6a (trazabilidad).** No veías el módulo `verify_b2_1_box_certificate.py`, del que
B3 importa `gate`, `b15` y `executed_ir`. Ahora va adjunto completo. El `executed_ir` que
contiene **no lo ha auditado nadie**: se escribió después de tu auditoría de B2.1, para atender
tu condición «IR ejecutado» de entonces. Esta ronda cubre también esa deuda de B2.1.

Evidencia que no puedes ver tú mismo y que se declara aquí:

```text
$ git log --oneline -- research_program/puente_3p1/2026-10-11/verify_b2_path2_gate_certificate.py
7909c0e B2 gate certificate: drho/dt(t0) >= +0.00705 with directed rounding, frozen pending audit
    (único commit: el verificador de la compuerta no ha cambiado desde el objeto auditado)

prueba negativa (ejecutada el 2026-10-12): se carga la compuerta desde la caché por defecto de
numba y se aplica executed_ir a gate.k_below
    -> RuntimeError: k_below was loaded from a numba cache (1 hits)
```

**Pendiente 6b (MENOR, serialización).** Ya está corregida en el verificador de B3 adjunto: los
extremos se escriben con `b15.iv_lo`/`b15.iv_hi`, que convierten hacia afuera. Además, el
producto final `W23` se calcula ahora en `mpmath.iv`; antes se hacía con escalares `mpf`.

## Lo que se te pide

1. ¿Vincula el módulo B2.1 la compuerta mostrada **sin alterarla**? Comprueba si hay alguna
   sustitución, parche o reasignación de funciones de `gate` además de `VN_FR`, que hace B3.
2. ¿Cumple `executed_ir`, junto con `fastmath_guard` / `guard_all_gate_kernels`, lo que
   exigiste: inspeccionar el código ejecutado, cubrir los cuerpos `prange` y no poder pasar en
   vacío? Busca cualquier manera de que pase sin haber inspeccionado el código real.
3. ¿Queda bien la corrección de 6b?

Para cada punto, da una clasificación y la condición de concesión. Termina con una línea
`Veredicto final B3: …` y otra `Control IR (también para B2.1): …`.

### Adjunto: verify_b2_1_box_certificate.py
```
"""PUENTE-3P1 / B2.1 -- drho/dt > 0 on the whole frozen mesh hull t in [0.45, 0.55].

B2.1 (research_program/puente_3p1/2026-09-12/B2_1_local_order_law_injectivity.md) asks for local
injectivity of t -> rho(lambda(t)) near t0 = 0.5 on the frozen mesh {0.45, ..., 0.55}, by "an
envelope of the derivative that excludes zero".  The gate certificate (2026-10-11, promoted) gives
the sign only AT t0; its continuity transfer (2026-10-12) reaches a radius of 1e-7 only, because h
has a sqrt modulus.  This file instead bounds S directly over BOXES of lambda.

Box.  [0.45, 0.55] is cut into N equal t-intervals T_k.  On T_k every coordinate of lambda(t) is
affine and monotone, for the binary64-endpoint curve and for the decimal curve alike; c_lo / c_hi
are the outward-rounded min / max over both curves and both ends.  For every lambda in that box:
    K_in  = [-uo_lo, ui_lo] x [v0_hi, v1_lo]   subset of  K(lambda)  subset of
    K_out = [-uo_hi, ui_hi] x [v0_lo, v1_hi].
Each face of K(lambda) lies in a thin STRIP (e.g. U = u_in(lambda) in [ui_lo, ui_hi]).  The
direction d enters only through the face velocities v_n, enclosed for both curves' d.

Bounds (g, h >= 0, so integrals are monotone in the domain):
  Z      in [Z(K_in)_lo, Z(K_out)_hi];          B <= B(K_out)_hi   (gate's b_hi_sum on K_out)
  I_f = int_face g H_K, faces with v_n > 0 (U=-u_out, U=u_in, V=v0):
         I_f >= sum over strip cells of the INNER face extent of len_lo * g_lo(cell) * H_lo(cell),
         H_lo(cell) = sum_Q W_lo(Q) [p_lo(LB(c_top, Q_bot)) + p_lo(LB(Q_top, c_bot))],  Q in K_in,
         by monotonicity of the sup in the endpoints (gate note section 2.2): every x of the cell
         lies above c_bot and below c_top, and H_K >= H_{K_in};
  face V=v1 (v_n < 0): I_f <= sum over strip cells of the OUTER extent of len_hi * g_hi * H_hi,
         H_hi(cell) = sum_Q W_hi(Q) [p_hi(UB(c_bot, Q_top)) + p_hi(UB(Q_bot, c_top))],  Q in K_out,
         whose lattice has v1_lo as its second-to-last V node, so both cell corners are lattice
         points and the gate's ub_table applies unchanged;
  J_f = int_face g: upper over the outer extent for v_n > 0, lower over the inner extent for v1;
  S_lo = B'_lo - (2 Z'_hi / Z_lo) B_hi,   B'_lo = 2 sum_f (v_n lo) * (I_f lower or upper).

Arithmetic: the gate's (section 3 of its note): one ulp outward after every binary64 operation,
certified monotone tables from B1.5's scalar layer, B1.5's directed pairwise sums, fast-math guard
over the gate's kernels AND the three new ones.  M (lattice) and N (boxes) are proof parameters:
any values give valid bounds.

Determinism: no seeds, no Monte Carlo, no search over lambda, t0 or points; the curve and the
interval [0.45, 0.55] are the frozen B2.1 ones.
Usage: .venv/bin/python research_program/puente_3p1/2026-10-12/verify_b2_1_box_certificate.py
       [M N [k0 k1]]     (a partial range k0..k1-1 prints and does not write the JSON)
"""
import json
import math
import os
import re
import sys
import tempfile
import time

# Every kernel is compiled IN THIS PROCESS: an empty, private numba cache directory, set before
# numba is imported.  A dispatcher loaded from a cache returns an EMPTY module from inspect_llvm,
# so the fast-math guard must inspect code that was compiled here (dev/B2_FASTMATH_GUARD_CACHE_
# FINDING_2026-10-12.md).  The guard also checks stats.cache_hits == 0 for every kernel.
os.environ["NUMBA_CACHE_DIR"] = tempfile.mkdtemp(prefix="b2_1_numba_cache_")
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
from numba import njit, prange

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "2026-10-11"))
import verify_b2_path2_gate_certificate as gate  # noqa: E402

b15 = gate.b15
up, dn, _up, _dn = gate.up, gate.dn, gate._up, gate._dn

# --- frozen inputs ---------------------------------------------------------------------------
L0, L1 = gate.L0, gate.L1                                  # binary64, as every frozen B2 script
DEC0 = ("0.5", "1.0", "1.0", "0.5", "0.1")
DEC1 = ("0.2", "0.8", "2.0", "0.9", "0.1")
T_LO, T_HI = Fr(45, 100), Fr(55, 100)                      # hull of the frozen B2.1 mesh
CURVES = [([Fr(float(x)) for x in L0], [Fr(float(x)) for x in L1]),
          ([Fr(x) for x in DEC0], [Fr(x) for x in DEC1])]

# --- proof parameters (any values give a valid bound) -----------------------------------------
M_DEFAULT = 128
N_DEFAULT = 100
R_SUB, N_TAU = gate.R_SUB, gate.N_TAU


def coord_range(i, ta, tb):
    """Outward binary64 (lo, hi) of coordinate i over t in [ta, tb], both curves."""
    vals = [a[i] + t * (b[i] - a[i]) for a, b in CURVES for t in (ta, tb)]
    return float(dn(float(min(vals)))), float(up(float(max(vals))))


def vn_range(name):
    """Outward (lo, hi) of the outward normal velocity of a face, both curves' directions."""
    idx, sgn = {"U=-u_out": (2, 1), "U=u_in": (3, 1), "V=v0": (0, -1), "V=v1": (1, 1)}[name]
    vals = [sgn * (b[idx] - a[idx]) for a, b in CURVES]
    return float(dn(float(min(vals)))), float(up(float(max(vals))))


def w_table_global():
    """One certified w table for every box: the range of K_out over the whole interval."""
    uo = coord_range(2, T_LO, T_HI)[1]
    ui = coord_range(3, T_LO, T_HI)[1]
    v1 = coord_range(1, T_LO, T_HI)[1]
    wlo = float(dn(-uo * v1)) - 1e-3
    whi = float(up(ui * v1)) + 1e-3
    assert whi < 1.0
    left = np.linspace(wlo, 0.0, gate.NT_HALF + 1)
    right = np.linspace(0.0, whi, gate.NT_HALF + 1)[1:]
    wt = np.concatenate([left, right])
    assert np.all(np.diff(wt) > 0) and wt[gate.NT_HALF] == 0.0
    return wt


# ---------------------------------------------------------------------------------------------
# New kernels (the rest are the gate's, imported unchanged).
# ---------------------------------------------------------------------------------------------
@njit(parallel=True, cache=True)
def lb_rows_xy(srcU, srcV, forward, Ug, Vg, wt, qlo, bt, plo_p, ntau):
    """p_lo(LB) between arbitrary source points and every lattice point.  Same arithmetic as the
    gate's lb_rows; forward: the source is the past end, else the future end."""
    n1 = Ug.size
    npt = n1 * n1
    out = np.zeros((srcU.size, npt))
    inv = 1.0 / ntau
    for r in prange(srcU.size):
        for x in range(npt):
            ix, jx = x // n1, x % n1
            if forward:
                Ua, Va, Ub, Vb = srcU[r], srcV[r], Ug[ix], Vg[jx]
            else:
                Ua, Va, Ub, Vb = Ug[ix], Vg[jx], srcU[r], srcV[r]
            if not (Ub > Ua and Vb > Va):
                continue
            du_lo, du_hi = _dn(Ub - Ua), _up(Ub - Ua)
            dv_lo, dv_hi = _dn(Vb - Va), _up(Vb - Va)
            acc = 0.0
            for k in range(ntau):
                t0, t1 = k * inv, (k + 1) * inv
                U_lo = _dn(Ua + _dn(du_lo * t0))
                U_hi = _up(Ua + _up(du_hi * t1))
                V_lo = _dn(Va + _dn(dv_lo * t0))
                V_hi = _up(Va + _up(dv_hi * t1))
                w_lo = _dn(U_lo * V_lo) if U_lo >= 0.0 else _dn(U_lo * V_hi)
                kq = gate.k_below(wt, w_lo)
                if kq >= 0:
                    acc = _dn(acc + qlo[kq])
            line = _dn(_dn(math.sqrt(_dn(du_lo * dv_lo))) * _dn(acc * inv))
            out[r, x] = gate.p_lo_of(line, bt, plo_p)
    return out


@njit(cache=True)
def strip_weights(u_face, a0, a1, grid, r, wt, glo, ghi, e_inv_hi):
    """Per segment of `grid` along a face: (lo, hi) of len * G over the strip cell.
    u_face: the face is U = const in [a0, a1] and the grid runs along V; else V = const."""
    n = grid.size - 1
    lo = np.zeros(n); hi = np.zeros(n)
    for i in range(n):
        xs = gate.tiling(grid[i], grid[i + 1], r)
        alo = 0.0; ahi = 0.0
        for a in range(r):
            if u_face:
                wl, wh = gate.rect_w(a0, a1, xs[a], xs[a + 1])
            else:
                wl, wh = gate.rect_w(xs[a], xs[a + 1], a0, a1)
            gl, gh = gate.g_range(wl, wh, wt, glo, ghi, e_inv_hi)
            alo = _dn(alo + _dn(_dn(xs[a + 1] - xs[a]) * gl))
            ahi = _up(ahi + _up(_up(xs[a + 1] - xs[a]) * gh))
        lo[i] = alo; hi[i] = ahi
    return lo, hi


@njit(cache=True)
def face_h_cells(M, W, fwd, bwd, lower):
    """H per strip cell from per-cell rows over the lattice of an M x M cell grid.
    lower: fwd[i] = p_lo(c_top -> .), bwd[i] = p_lo(. -> c_bot): uses Q_bot / Q_top.
    upper: fwd[i] = p_hi(c_bot -> .), bwd[i] = p_hi(. -> c_top): uses Q_top / Q_bot."""
    n1 = M + 1
    ncell = fwd.shape[0]
    H = np.zeros(ncell)
    for i in range(ncell):
        acc = 0.0
        for Q in range(M * M):
            iQ, jQ = Q // M, Q % M
            bot = iQ * n1 + jQ
            top = (iQ + 1) * n1 + (jQ + 1)
            if lower:
                v = fwd[i, bot] + bwd[i, top]
                acc = _dn(acc + _dn(W[Q] * _dn(v)))
            else:
                v = fwd[i, top] + bwd[i, bot]
                acc = _up(acc + _up(W[Q] * _up(v)))
        H[i] = acc
    return H


NEW_KERNELS = (lb_rows_xy, strip_weights, face_h_cells)
# Gate kernels this file never calls: replaced by the three new ones above.  They are excluded
# BY NAME, so the guard still demands a compiled signature for every kernel that runs here.
GATE_UNUSED = ("lb_rows", "face_h", "segment_weights")


def executed_ir(fn):
    """LLVM IR of every overload of `fn` that ran in this process, with every library it links
    (the prange bodies, __numba_parfor_gufunc_*, live in linked libraries).  Fails if any
    overload came from a cache, or if a module lacks the definition of fn's own mangled name."""
    hits = sum(fn.stats.cache_hits.values())
    if hits:
        raise RuntimeError("%s was loaded from a numba cache (%d hits)" % (fn.py_func.__name__, hits))
    name = fn.py_func.__name__
    own = re.compile(r"^define [^\n]*@_ZN\d+\w*?%d%sB" % (len(name), re.escape(name)), re.M)
    out = []
    for sig in fn.signatures:
        lib = fn.overloads[sig].library
        seen, stack = {}, [lib]
        while stack:
            cur = stack.pop()
            if id(cur) in seen:
                continue
            seen[id(cur)] = cur
            stack.extend(getattr(cur, "_linking_libraries", ()))
        top = lib.get_llvm_str()
        if not own.search(top):
            raise RuntimeError("no definition of %s in its own module" % name)
        out.extend(c.get_llvm_str() for c in seen.values())
    return out


def fastmath_guard():
    gate._compile_helpers()
    used = tuple(fn for fn in gate.KERNELS if fn.py_func.__name__ not in GATE_UNUSED) + NEW_KERNELS
    assert len(used) == len(gate.KERNELS) - len(GATE_UNUSED) + len(NEW_KERNELS)
    uncompiled = [fn.py_func.__name__ for fn in used if not fn.signatures]
    flags, ir_chars, parfor_bodies = {}, {}, {}
    for fn in used:
        irs = executed_ir(fn)
        name = fn.py_func.__name__
        flags[name] = sorted({m.group(0) for ir in irs for m in gate._FAST.finditer(ir)})
        ir_chars[name] = sum(len(ir) for ir in irs)
        parfor_bodies[name] = len({m.group(0) for ir in irs for m in re.finditer(
            r"^define [^\n]*@_ZN\w*?__numba_parfor_gufunc_0x[0-9a-f]+", ir, re.M)})
    parallel_ok = all(parfor_bodies[fn.py_func.__name__] > 0 for fn in used
                      if fn.targetoptions.get("parallel"))

    @njit(fastmath=True)
    def _mutant(a, b, c):
        return a * b + c
    _mutant(1.0, 2.0, 3.0)
    mutant_caught = bool(gate._FAST.search("".join(executed_ir(_mutant))))
    clean = all(not v for v in flags.values())
    return {"kernels_checked": len(flags),
            "inspection": "executed overloads, compiled in-process (private empty numba cache, "
                          "cache_hits == 0), own mangled definition required, linked libraries "
                          "included",
            "min_ir_chars": min(ir_chars.values()),
            "parfor_bodies_found": {k: v for k, v in parfor_bodies.items() if v},
            "parallel_kernels_have_bodies": parallel_ok,
            "gate_kernels_excluded_as_unused": list(GATE_UNUSED),
            "kernels_without_compiled_signature": uncompiled,
            "flags_found": {k: v for k, v in flags.items() if v}, "all_clean": clean,
            "mutation_fastmath_detected": mutant_caught,
            "ok": bool(clean and mutant_caught and parallel_ok and not uncompiled)}


# ---------------------------------------------------------------------------------------------
# One box.
# ---------------------------------------------------------------------------------------------
def run_box(ta, tb, M, T):
    wt, qlo, glo, ghi, Flo, Fhi, bt, plo_p, phi_p = T
    e_inv = b15.E_INV_HI
    v0_lo, v0_hi = coord_range(0, ta, tb)
    v1_lo, v1_hi = coord_range(1, ta, tb)
    uo_lo, uo_hi = coord_range(2, ta, tb)
    ui_lo, ui_hi = coord_range(3, ta, tb)
    assert 0 < v0_lo < v0_hi < v1_lo < v1_hi and 0 < ui_lo < ui_hi and 0 < uo_lo < uo_hi
    n1 = M + 1

    # ---- inner lattice: Z_lo and lower H ----
    Ug_i = np.linspace(-uo_lo, ui_lo, n1)
    Vg_i = np.linspace(v0_hi, v1_lo, n1)
    assert Ug_i[0] == -uo_lo and Ug_i[-1] == ui_lo and Vg_i[0] == v0_hi and Vg_i[-1] == v1_lo
    assert np.all(np.diff(Ug_i) > 0) and np.all(np.diff(Vg_i) > 0)
    Wi_lo, _ = gate.cell_weights(Ug_i, Vg_i, R_SUB, wt, glo, ghi, e_inv)
    Z_lo = b15.sum_dn(Wi_lo)

    # ---- outer lattice: Z_hi, B_hi, upper H; v1_lo is its second-to-last V node ----
    Ug_o = np.linspace(-uo_hi, ui_hi, n1)
    Vg_o = np.concatenate([np.linspace(v0_lo, v1_lo, M), [v1_hi]])
    assert Ug_o[0] == -uo_hi and Ug_o[-1] == ui_hi and Vg_o[0] == v0_lo
    assert Vg_o[M - 1] == v1_lo and Vg_o[M] == v1_hi
    assert np.all(np.diff(Ug_o) > 0) and np.all(np.diff(Vg_o) > 0)
    _, Wo_hi = gate.cell_weights(Ug_o, Vg_o, R_SUB, wt, glo, ghi, e_inv)
    Z_hi = b15.sum_up(Wo_hi)
    nulo, nuhi = gate.nu_enclosures(Vg_o)
    iu, jv = np.divmod(np.arange(n1 * n1), n1)
    PU, PV = Ug_o[iu], Vg_o[jv]
    wlo_pt, whi_pt = dn(PU * PV), up(PU * PV)
    cs = np.concatenate([gate.C_POS, gate.C_NEG])
    AU_lo, AU_hi, AL_lo, AL_hi, thr = gate.calibration_point_tables(
        cs, wt, Flo, Fhi, wlo_pt, whi_pt, nulo[jv], nuhi[jv])
    Pcs_lo, Pcs_hi = gate.cs_prefix(Ug_o, Vg_o, R_SUB, wt, Fhi)
    pub = gate.ub_table(M, Ug_o, Vg_o, wlo_pt, whi_pt, AU_lo, AU_hi, AL_lo, AL_hi, thr,
                        Pcs_lo, Pcs_hi, bt, phi_p)
    del AU_lo, AU_hi, AL_lo, AL_hi
    B_hi = gate.b_hi_sum(M, Wo_hi, pub)

    # ---- faces ----
    lower_faces = {   # name: (u_face, strip a0, a1, inner grid along the face, outer grid)
        "U=-u_out": (True, -uo_hi, -uo_lo, Vg_i, Vg_o),
        "U=u_in": (True, ui_lo, ui_hi, Vg_i, Vg_o),
        "V=v0": (False, v0_lo, v0_hi, Ug_i, Ug_o),
    }
    Bp_terms, Zp_hi_terms, Zp_lo_terms, face_out = [], [], [], {}
    for name, (u_face, a0, a1, g_in, g_out) in lower_faces.items():
        vn_lo, vn_hi = vn_range(name)
        assert vn_lo > 0
        seg_lo, _ = strip_weights(u_face, a0, a1, g_in, R_SUB, wt, glo, ghi, e_inv)
        if u_face:     # cell j: c_bot = (a0, V_j), c_top = (a1, V_j+1)
            bU, bV, tU, tV = np.full(M, a0), g_in[:-1], np.full(M, a1), g_in[1:]
        else:          # cell i: c_bot = (U_i, a0), c_top = (U_i+1, a1)
            bU, bV, tU, tV = g_in[:-1], np.full(M, a0), g_in[1:], np.full(M, a1)
        fwd = lb_rows_xy(tU.copy(), tV.copy(), True, Ug_i, Vg_i, wt, qlo, bt, plo_p, N_TAU)
        bwd = lb_rows_xy(bU.copy(), bV.copy(), False, Ug_i, Vg_i, wt, qlo, bt, plo_p, N_TAU)
        H = face_h_cells(M, Wi_lo, fwd, bwd, True)
        inner = b15.sum_dn(dn(seg_lo * H))
        term = float(dn(2.0 * dn(vn_lo * inner)))
        Jo_lo, Jo_hi = strip_weights(u_face, a0, a1, g_out, R_SUB, wt, glo, ghi, e_inv)
        Ji_lo, _ = strip_weights(u_face, a0, a1, g_in, R_SUB, wt, glo, ghi, e_inv)
        Zp_hi_terms.append(float(up(vn_hi * b15.sum_up(Jo_hi))))
        Zp_lo_terms.append(float(dn(vn_lo * b15.sum_dn(Ji_lo))))
        Bp_terms.append(term)
        face_out[name] = term

    # face V = v1 (v_n < 0): upper I over the outer extent, strip cells on the outer lattice
    vn_lo, vn_hi = vn_range("V=v1")
    assert vn_hi < 0
    _, seg_hi = strip_weights(False, v1_lo, v1_hi, Ug_o, R_SUB, wt, glo, ghi, e_inv)
    cbot = np.arange(M) * n1 + (M - 1)            # (U_i, v1_lo)
    ctop = (np.arange(M) + 1) * n1 + M            # (U_i+1, v1_hi)
    H = face_h_cells(M, Wo_hi, pub[cbot, :], pub[:, ctop].T.copy(), False)
    inner = b15.sum_up(up(seg_hi * H))
    term = float(dn(2.0 * dn(vn_lo * inner)))
    Ji_lo, _ = strip_weights(False, v1_lo, v1_hi, Ug_i, R_SUB, wt, glo, ghi, e_inv)
    Zp_hi_terms.append(float(up(vn_hi * b15.sum_dn(Ji_lo))))
    Zp_lo_terms.append(float(dn(vn_lo * b15.sum_up(seg_hi))))
    Bp_terms.append(term)
    face_out["V=v1"] = term
    del pub

    Bp_lo = b15.sum_dn(Bp_terms)
    Zp_lo, Zp_hi = b15.sum_dn(Zp_lo_terms), b15.sum_up(Zp_hi_terms)
    assert Zp_hi > 0
    k_hi = float(up(2.0 * up(Zp_hi / Z_lo)))
    S_lo = float(dn(Bp_lo - up(k_hi * B_hi)))
    drho_lo = float(dn(S_lo / up(Z_hi * Z_hi))) if S_lo > 0 else None
    return {"t": [str(ta), str(tb)],
            "box": {"v0": [v0_lo, v0_hi], "v1": [v1_lo, v1_hi], "u_out": [uo_lo, uo_hi],
                    "u_in": [ui_lo, ui_hi]},
            "Z": [Z_lo, Z_hi], "Zprime": [Zp_lo, Zp_hi], "two_Zp_over_Z_hi": k_hi,
            "B_hi": B_hi, "Bprime_lo": Bp_lo, "faces_Bprime_lower": face_out,
            "S_lo": S_lo, "drho_dt_lower_bound": drho_lo}


def tables():
    wt = w_table_global()
    qlo, qhi, glo, ghi, Flo, Fhi = gate.certified_tables(wt)
    bt, plo_p, phi_p = gate.p_table()
    return wt, qlo, glo, ghi, Flo, Fhi, bt, plo_p, phi_p


def main():
    args = sys.argv[1:]
    M = int(args[0]) if args else M_DEFAULT
    N = int(args[1]) if len(args) > 1 else N_DEFAULT
    k0, k1 = (int(args[2]), int(args[3])) if len(args) > 3 else (0, N)
    full = (k0, k1) == (0, N) and M == M_DEFAULT and N == N_DEFAULT
    t_start = time.time()
    T = tables()
    t_tab = time.time() - t_start
    width = (T_HI - T_LO) / N
    boxes = []
    for k in range(k0, k1):
        ta, tb = T_LO + k * width, T_LO + (k + 1) * width
        t1 = time.time()
        res = run_box(ta, tb, M, T)
        res["seconds"] = round(time.time() - t1, 1)
        boxes.append(res)
        print(f"box {k:3d} t=[{float(ta):.4f},{float(tb):.4f}]  S_lo={res['S_lo']:+.6f}  "
              f"B'_lo={res['Bprime_lo']:.6f}  B_hi={res['B_hi']:.6f}  ({res['seconds']} s)",
              flush=True)
    guard = fastmath_guard()
    worst = min(boxes, key=lambda b: b["S_lo"])
    all_pos = all(b["S_lo"] > 0 for b in boxes)
    terminal = ("B2.1_POSITIVE_DERIVATIVE" if (all_pos and guard["ok"] and full)
                else "B2.1_INCONCLUSIVE_BY_BOUNDS" if full else "PARTIAL_RUN_NO_TERMINAL")
    out = {
        "unit": "PUENTE-3P1/B2.1_BOX_CERTIFICATE",
        "interval_t": [str(T_LO), str(T_HI)], "curves": "binary64 endpoints and decimal, both",
        "M": M, "N": N, "boxes_run": [k0, k1], "R_sub": R_SUB, "N_tau": N_TAU,
        "w_table_nodes": int(T[0].size), "seconds_tables": round(t_tab, 1),
        "min_S_lo": worst["S_lo"], "min_S_lo_box_t": worst["t"],
        "min_drho_dt_lower_bound": min((b["drho_dt_lower_bound"] or -1.0) for b in boxes),
        "fastmath_guard": guard, "boxes": boxes,
        "no_new_path": True, "no_new_t0": True, "no_new_points": True, "no_search": True,
        "no_adjustment": True, "no_seeds": True, "no_monte_carlo": True,
        "terminal": terminal,
    }
    print(json.dumps({k: v for k, v in out.items() if k != "boxes"}, indent=2))
    if full:
        (HERE / "verification_b2_1_box_certificate.json").write_text(json.dumps(out, indent=2) + "\n")


if __name__ == "__main__":
    main()
```

### Adjunto: verify_b3_certificate.py
```
"""PUENTE-3P1 / B3 -- n=2 versus phi at the frozen point, with the gate's certified machinery.

B3 (research_program/puente_3p1/2026-09-12/B3_transverse_n2_audit.md) asks whether dphi is
parallel to drho in the gauge-quotiented chart x = (v1/v0, u_in/u_out, u_in v1), v0 fixed, at the
frozen point lambda* (the binary64 path(0.5), the gate's H5).  One wedge component excluding
zero gives B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY: there is a direction v with
drho(v) = 0 and dphi(v) != 0.  Since 2026-10-11 B3 is INCONCLUSIVE_BY_BOUNDS.

This file certifies the (x2, x3) component,
    W23 = dphi_2 drho_3 - dphi_3 drho_2  >  0,
from four enclosures:
  * drho_3 >= S_lo(e3)/Z_hi^2.  Along e3 = d lambda/d x3 only the two U faces move, both with
    v_n > 0 -- exactly the gate's case.  The gate's audited run() is called UNCHANGED, with its
    face-velocity table VN_FR set to e3's exact rationals (V faces: exactly 0).
  * dphi_2, dphi_3 from phi = Z_in/(Z_in + Z_out) (U > 0 and U < 0 parts of K):
        dphi = (Z_out dZ_in - Z_in dZ_out)/(Z_in + Z_out)^2,
    dZ by face integrals of G, all from the gate's cell_weights / segment_weights, combined in
    mpmath.iv.
  * |drho_2| crudely: along e2 only U = -u_out moves, and H <= Z, so
        |S(e2)| <= 2 |v| J (Z_hi + B_hi/Z_lo),  J = int_face G.
Chart rank 3 is an exact rational determinant.  The fast-math guard is B2.1's (executed IR,
private empty numba cache), over all 19 gate kernels.

Determinism: no seeds, no Monte Carlo, no search; frozen point and chart as in B3.
Usage: .venv/bin/python research_program/puente_3p1/2026-10-12/verify_b3_certificate.py [M]
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_b2_1_box_certificate as b21  # noqa: E402  (sets the private numba cache first)

import json  # noqa: E402
import re  # noqa: E402
from fractions import Fraction as Fr  # noqa: E402

import numpy as np  # noqa: E402
from mpmath import iv  # noqa: E402
from numba import njit  # noqa: E402

gate, b15 = b21.gate, b21.b15
iv.dps = 30

LAM = [Fr(float(x)) for x in gate.LAM[:4]]        # (v0, v1, u_out, u_in), binary64, exact
V0, V1, UO, UI = LAM
X = (V1 / V0, UI / UO, UI * V1)                     # chart coordinates at lambda*


def chart_jacobian():
    """Columns d lambda / d x_j, exact rationals; gauge v0 fixed (research B3 note)."""
    x1, x2, x3 = X
    return [  # rows v0, v1, u_out, u_in
        [Fr(0), Fr(0), Fr(0)],
        [V0, Fr(0), Fr(0)],
        [-UO / x1, -UO / x2, UO / x3],
        [-UI / x1, Fr(0), 1 / V1],
    ]


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def I(x):
    x = Fr(x)
    return iv.mpf(x.numerator) / iv.mpf(x.denominator)


def F(lo, hi):
    return iv.mpf([lo, hi])


def guard_all_gate_kernels():
    gate._compile_helpers()
    flags, chars = {}, {}
    uncompiled = [fn.py_func.__name__ for fn in gate.KERNELS if not fn.signatures]
    for fn in gate.KERNELS:
        irs = b21.executed_ir(fn)
        flags[fn.py_func.__name__] = sorted({m.group(0) for ir in irs for m in gate._FAST.finditer(ir)})
        chars[fn.py_func.__name__] = sum(len(i) for i in irs)

    @njit(fastmath=True)
    def _mutant(a, b, c):
        return a * b + c
    _mutant(1.0, 2.0, 3.0)
    mutant = bool(gate._FAST.search("".join(b21.executed_ir(_mutant))))
    clean = all(not v for v in flags.values())
    return {"kernels_checked": len(flags), "inspection": "executed overloads, private empty cache",
            "min_ir_chars": min(chars.values()), "kernels_without_compiled_signature": uncompiled,
            "flags_found": {k: v for k, v in flags.items() if v}, "all_clean": clean,
            "mutation_fastmath_detected": mutant, "ok": bool(clean and mutant and not uncompiled)}


def phi_pieces(M):
    """Enclosures of Z_in, Z_out and the face integrals of G that dphi needs."""
    wt = gate.w_table()
    _, _, glo, ghi, _, _ = gate.certified_tables(wt)
    e = b15.E_INV_HI
    v0, v1, uo, ui = (float(x) for x in LAM)
    Vg = np.linspace(v0, v1, M + 1)
    Ui = np.linspace(0.0, ui, M + 1)
    Uo = np.linspace(-uo, 0.0, M + 1)
    assert Vg[0] == v0 and Vg[-1] == v1 and Ui[-1] == ui and Uo[0] == -uo
    assert Ui[0] == 0.0 and Uo[-1] == 0.0
    out = {}
    lo, hi = gate.cell_weights(Ui, Vg, gate.R_SUB, wt, glo, ghi, e)
    out["Z_in"] = F(b15.sum_dn(lo), b15.sum_up(hi))
    lo, hi = gate.cell_weights(Uo, Vg, gate.R_SUB, wt, glo, ghi, e)
    out["Z_out"] = F(b15.sum_dn(lo), b15.sum_up(hi))
    for key, fixed, grid in (("J_uin", ui, Vg), ("J_uout", -uo, Vg),      # U faces, along V
                             ("J_v1_in", v1, Ui), ("J_v1_out", v1, Uo),    # V = v1, split at U = 0
                             ("J_v0_in", v0, Ui), ("J_v0_out", v0, Uo)):   # V = v0
        lo, hi = gate.segment_weights(fixed, grid, gate.R_SUB, wt, glo, ghi, e)
        out[key] = F(b15.sum_dn(lo), b15.sum_up(hi))
    return out


def dphi(pc, col):
    dv0, dv1, duo, dui = (I(c) for c in col)
    dZin = dui * pc["J_uin"] + dv1 * pc["J_v1_in"] - dv0 * pc["J_v0_in"]
    dZout = duo * pc["J_uout"] + dv1 * pc["J_v1_out"] - dv0 * pc["J_v0_out"]
    Zs = pc["Z_in"] + pc["Z_out"]
    return (pc["Z_out"] * dZin - pc["Z_in"] * dZout) / Zs ** 2


def main():
    M = int(sys.argv[1]) if len(sys.argv) > 1 else gate.M_DEFAULT
    J = chart_jacobian()
    cols = [[J[r][c] for r in range(4)] for c in range(3)]
    det = det3([J[1], J[2], J[3]])
    chart_rank3 = det != 0

    # drho_3 lower bound: the gate's run() with e3's face velocities
    e3 = cols[2]
    assert e3[0] == 0 and e3[1] == 0 and e3[2] > 0 and e3[3] > 0
    gate.VN_FR = {"U=-u_out": e3[2], "U=u_in": e3[3], "V=v0": -e3[0], "V=v1": e3[1]}
    r3 = gate.run(M)
    Z = F(*r3["Z"])
    # S_lo > 0 divides by Z_hi^2; otherwise by Z_lo^2 (still a valid lower bound)
    drho3_lo = I(r3["S_lo"]) / (iv.mpf(r3["Z"][1]) ** 2 if r3["S_lo"] > 0 else iv.mpf(r3["Z"][0]) ** 2)

    # |drho_2| crude upper bound; e2 moves only U = -u_out
    pc = phi_pieces(M)
    e2 = cols[1]
    assert e2[0] == 0 and e2[1] == 0 and e2[3] == 0
    S2_abs = 2 * abs(I(e2[2])) * pc["J_uout"].b * (Z.b + iv.mpf(r3["B_hi"]) / Z.a)
    drho2_abs = S2_abs / Z.a ** 2

    dphis = [dphi(pc, c) for c in cols]
    d2, d3 = dphis[1], dphis[2]
    # every factor is positive here: W23 >= lo(dphi_2) lo(drho_3) - hi|dphi_3| hi|drho_2|, in iv
    abs3 = iv.mpf(max(abs(d3.a), abs(d3.b)))
    W23 = iv.mpf(d2.a) * iv.mpf(drho3_lo.a) - abs3 * iv.mpf(drho2_abs.b)
    W23_lo = W23.a
    wedge_nonzero = bool(d2.a > 0 and drho3_lo.a > 0 and W23_lo > 0)
    guard = guard_all_gate_kernels()
    terminal = ("B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY"
                if (wedge_nonzero and chart_rank3 and guard["ok"]) else "B3_INCONCLUSIVE_BY_BOUNDS")
    f = lambda x: [b15.iv_lo(x), b15.iv_hi(x)]  # noqa: E731   outward into binary64
    out = {
        "unit": "PUENTE-3P1/B3_CERTIFICATE", "M": M,
        "frozen_lambda_binary64": [float(x) for x in gate.LAM],
        "chart_x": [str(x) for x in X], "chart_jacobian_columns": [[str(v) for v in c] for c in cols],
        "chart_det_rows_v1_uout_uin": str(det), "chart_rank_three": chart_rank3,
        "drho_dx3": {"S_lo_e3": r3["S_lo"], "Z": r3["Z"], "B_hi": r3["B_hi"],
                     "Bprime_lo_e3": r3["Bprime_lo"], "lower_bound": b15.iv_lo(drho3_lo)},
        "drho_dx2_abs_upper": b15.iv_hi(drho2_abs),
        "phi_pieces": {k: f(v) for k, v in pc.items()},
        "dphi_dx": [f(x) for x in dphis],
        "wedge_x2x3_lower_bound": b15.iv_lo(W23),
        "dphi_wedge_drho_certified_nonzero": wedge_nonzero,
        "fastmath_guard": guard,
        "no_new_path": True, "no_new_point": True, "no_search": True, "no_seeds": True,
        "no_monte_carlo": True, "terminal": terminal,
    }
    print(json.dumps(out, indent=2))
    if len(sys.argv) <= 1:
        (HERE / "verification_b3_certificate.json").write_text(json.dumps(out, indent=2) + "\n")


if __name__ == "__main__":
    main()
```
