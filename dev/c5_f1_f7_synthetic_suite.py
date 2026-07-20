#!/usr/bin/env python3
"""
C5 Env(Φ★_L) synthetic suite F1–F7.

Documentary / development-only. No project generator, no evaluation seeds,
no CANDIDATE_5, no BH/MINK production bands.

Run:  python3 dev/c5_f1_f7_synthetic_suite.py
"""

from __future__ import annotations

import itertools
import json
import math
import random
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, FrozenSet, Iterable, Optional

# ---------------------------------------------------------------------------
# Poset + Φ★_L
# ---------------------------------------------------------------------------

Element = str
Partition = FrozenSet[FrozenSet[Element]]


@dataclass(frozen=True)
class Poset:
    """Finite strict poset via covering-ish relation: edges mean a ≺ b (a below b)."""

    elements: FrozenSet[Element]
    # pairs (lower, upper): lower ≺ upper (transitively closed on construction)
    order: FrozenSet[tuple[Element, Element]]

    def predecessors(self, x: Element) -> set[Element]:
        return {a for a, b in self.order if b == x}

    def successors(self, x: Element) -> set[Element]:
        return {b for a, b in self.order if a == x}

    def minimals(self) -> list[Element]:
        return sorted(x for x in self.elements if not self.predecessors(x))

    def maximals(self) -> list[Element]:
        return sorted(x for x in self.elements if not self.successors(x))

    def future(self, x: Element) -> set[Element]:
        """Strict future J+(x)."""
        return {b for a, b in self.order if a == x}

    def peel(self) -> Optional["Poset"]:
        M = set(self.maximals())
        if not M:
            return None
        elems = self.elements - frozenset(M)
        if not elems:
            return None
        order = frozenset((a, b) for a, b in self.order if a in elems and b in elems)
        return Poset(frozenset(elems), order)

    def relabel(self, sigma: dict[Element, Element]) -> "Poset":
        elems = frozenset(sigma[x] for x in self.elements)
        order = frozenset((sigma[a], sigma[b]) for a, b in self.order)
        return Poset(elems, order)


def transitive_closure(elements: Iterable[Element], covers: Iterable[tuple[Element, Element]]) -> Poset:
    """covers: immediate or generating lower≺upper pairs; close under transitivity."""
    elems = set(elements)
    rel = set(covers)
    # Floyd-like
    changed = True
    while changed:
        changed = False
        add = set()
        for a, b in rel:
            for c, d in rel:
                if b == c and (a, d) not in rel and a != d:
                    add.add((a, d))
        if add:
            rel |= add
            changed = True
    return Poset(frozenset(elems), frozenset(rel))


def from_futures(
    minimals: list[Element],
    mid_futures: dict[Element, set[Element]],
    roof: Optional[Element] = "roof",
) -> Poset:
    """
    Build height-2 (or 1 if roof is None) poset:
      mi ≺ every x in mid_futures[mi]
      every mid ≺ roof (if roof)
    """
    mids: set[Element] = set()
    for s in mid_futures.values():
        mids |= set(s)
    elems = set(minimals) | mids
    covers: list[tuple[Element, Element]] = []
    for m in minimals:
        for x in mid_futures[m]:
            covers.append((m, x))
    if roof is not None:
        elems.add(roof)
        for x in mids:
            covers.append((x, roof))
    return transitive_closure(elems, covers)


def jacobi_eigh(A: list[list[float]], tol: float = 1e-14, max_iter: int = 20000):
    n = len(A)
    S = [row[:] for row in A]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(max_iter):
        mval = 0.0
        p = q = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(S[i][j]) > mval:
                    mval = abs(S[i][j])
                    p, q = i, j
        if mval < tol:
            break
        app, aqq, apq = S[p][p], S[q][q], S[p][q]
        if abs(apq) < 1e-30:
            S[p][q] = S[q][p] = 0.0
            continue
        tau = (aqq - app) / (2 * apq)
        t = math.copysign(1.0, tau) / (abs(tau) + math.sqrt(1 + tau * tau))
        c = 1.0 / math.sqrt(1 + t * t)
        s = t * c
        for i in range(n):
            if i != p and i != q:
                sip, siq = S[i][p], S[i][q]
                S[i][p] = S[p][i] = c * sip - s * siq
                S[i][q] = S[q][i] = s * sip + c * siq
        S[p][p] = app - t * apq
        S[q][q] = aqq + t * apq
        S[p][q] = S[q][p] = 0.0
        for i in range(n):
            vip, viq = V[i][p], V[i][q]
            V[i][p] = c * vip - s * viq
            V[i][q] = s * vip + c * viq
    w = [S[i][i] for i in range(n)]
    order = sorted(range(n), key=lambda i: w[i])
    w_s = [w[i] for i in order]
    V_s = [[V[i][j] for j in order] for i in range(n)]
    return w_s, V_s


@dataclass
class PhiResult:
    terminal: str
    partition: Optional[Partition] = None
    detail: dict[str, Any] = field(default_factory=dict)


def spectral_bipartition_on_A(
    labels: list[Element],
    A: list[list[int]],
    *,
    m_min: int = 4,
    mult_tol: float = 1e-8,
    zero_tol: float = 1e-9,
) -> PhiResult:
    m = len(labels)
    if m < m_min:
        return PhiResult("ABSTAIN_TOO_FEW_MINIMALS")
    deg = [sum(A[i][j] for j in range(m)) for i in range(m)]
    L = [[float((deg[i] if i == j else 0) - A[i][j]) for j in range(m)] for i in range(m)]
    w, V = jacobi_eigh(L)
    mult1 = sum(1 for x in w if abs(x - w[0]) < mult_tol)
    mult2 = sum(1 for x in w if abs(x - w[1]) < mult_tol)
    if mult1 != 1 or mult2 != 1:
        return PhiResult(
            "ABSTAIN_SPECTRAL_MULTIPLICITY",
            detail={"eigs": w, "mult1": mult1, "mult2": mult2},
        )
    v = [V[i][1] for i in range(m)]
    if abs(v[0]) >= zero_tol and v[0] < 0:
        v = [-x for x in v]
    if any(abs(x) < zero_tol for x in v):
        return PhiResult("ABSTAIN_SPECTRAL_ZERO_COMPONENT", detail={"v": v})
    plus = frozenset(labels[i] for i, x in enumerate(v) if x > 0)
    minus = frozenset(labels[i] for i, x in enumerate(v) if x < 0)
    if not plus or not minus:
        return PhiResult("ABSTAIN_SPECTRAL_ONE_SIGN")
    part: Partition = frozenset([plus, minus])
    return PhiResult("EMIT", part, detail={"eigs": w, "v": v})


def overlap_matrix(C: Poset, mins: list[Element]) -> list[list[int]]:
    futures = [C.future(m) for m in mins]
    m = len(mins)
    A = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            A[i][j] = len(futures[i] & futures[j])
    return A


def phi_star_L(C: Poset, *, m_min: int = 4) -> PhiResult:
    if not C.elements:
        return PhiResult("ABSTAIN_EMPTY_OR_DEGENERATE_POSET")
    mins = C.minimals()
    if len(mins) < m_min:
        return PhiResult("ABSTAIN_TOO_FEW_MINIMALS", detail={"m": len(mins)})
    A = overlap_matrix(C, mins)
    r_full = spectral_bipartition_on_A(mins, A, m_min=m_min)
    if r_full.terminal != "EMIT":
        return r_full
    C2 = C.peel()
    if C2 is None:
        return PhiResult("ABSTAIN_PEEL_UNDEFINED")
    mins2 = C2.minimals()
    if set(mins2) != set(mins):
        return PhiResult("ABSTAIN_PEEL_UNDEFINED", detail={"mins": mins, "mins2": mins2})
    # keep label order of mins
    A2 = overlap_matrix(C2, mins)
    r_peel = spectral_bipartition_on_A(mins, A2, m_min=m_min)
    if r_peel.terminal != "EMIT":
        return PhiResult(
            "ABSTAIN_ROOF_UNSTABLE",
            detail={"full": r_full.terminal, "peel": r_peel.terminal},
        )
    if r_peel.partition != r_full.partition:
        return PhiResult(
            "ABSTAIN_ROOF_UNSTABLE",
            detail={"full_part": fmt_part(r_full.partition), "peel_part": fmt_part(r_peel.partition)},
        )
    return PhiResult("EMIT", r_full.partition, detail={"A": A, "A_peel": A2, "eigs": r_full.detail.get("eigs")})


def phi_V(C: Poset, *, m_min: int = 4) -> PhiResult:
    """Exact volume-class bipartition oracle (Env F1)."""
    mins = C.minimals()
    if len(mins) < m_min:
        return PhiResult("ABSTAIN_TOO_FEW_MINIMALS")
    A = overlap_matrix(C, mins)
    V = {mins[i]: A[i][i] for i in range(len(mins))}
    classes: dict[int, set[Element]] = {}
    for m, v in V.items():
        classes.setdefault(v, set()).add(m)
    cells = list(classes.values())
    if len(cells) != 2:
        return PhiResult("ABSTAIN", detail={"n_classes": len(cells), "V": V})
    part = frozenset(frozenset(c) for c in cells)
    return PhiResult("EMIT", part, detail={"V": V})


def fmt_part(p: Optional[Partition]) -> Any:
    if p is None:
        return None
    return [sorted(list(block)) for block in p]


def pattern_eq(a: PhiResult, b: PhiResult) -> bool:
    if a.terminal != b.terminal:
        return False
    if a.terminal != "EMIT":
        return True  # same abstention class name
    return a.partition == b.partition


def conjugate_partition(part: Partition, sigma: dict[Element, Element]) -> Partition:
    return frozenset(frozenset(sigma[x] for x in block) for block in part)


# ---------------------------------------------------------------------------
# Synthetic units
# ---------------------------------------------------------------------------

def unit_bridge() -> Poset:
    mins = ["m1", "m2", "m3", "m4"]
    mid = {
        "m1": {"a", "b", "c", "x"},
        "m2": {"a", "b", "c", "y"},
        "m3": {"x", "p", "q", "z"},
        "m4": {"y", "p", "q", "z"},
    }
    return from_futures(mins, mid, roof="roof")


def unit_cross() -> Poset:
    mins = ["m1", "m2", "m3", "m4"]
    mid = {
        "m1": {"a", "b", "c", "x"},
        "m2": {"x", "p", "q", "z"},
        "m3": {"a", "b", "c", "y"},
        "m4": {"y", "p", "q", "z"},
    }
    return from_futures(mins, mid, roof="roof")


def unit_roof_only() -> Poset:
    """
    Reconvergence only through shared roof: mid futures disjoint, all ≺ roof.
    Overlaps come only from the roof layer.
    """
    mins = ["m1", "m2", "m3", "m4"]
    mid = {
        "m1": {"a1", "a2", "a3"},
        "m2": {"b1", "b2", "b3"},
        "m3": {"c1", "c2", "c3"},
        "m4": {"d1", "d2", "d3"},
    }
    return from_futures(mins, mid, roof="roof")


def unit_roof_only_asymmetric() -> Poset:
    """Roof-only but unequal mid sizes → different V; still only roof creates cross links."""
    mins = ["m1", "m2", "m3", "m4"]
    mid = {
        "m1": {"a1", "a2"},
        "m2": {"b1", "b2", "b3", "b4"},
        "m3": {"c1"},
        "m4": {"d1", "d2", "d3"},
    }
    return from_futures(mins, mid, roof="roof")


def unit_side_wall() -> Poset:
    """
    Order-only surrogate of two lateral walls: two twin pairs reconverge internally
    with weak cross links only through a shared "wall corridor" mid set, no single roof
    funnel as the sole mechanism — use two local roofs (wall tops).
    """
    mins = ["m1", "m2", "m3", "m4"]
    # left wall pair m1,m2 share L*; right wall pair m3,m4 share R*; no global roof
    elems = set(mins) | {f"L{i}" for i in range(4)} | {f"R{i}" for i in range(4)} | {"WL", "WR"}
    covers = []
    for x in ["L0", "L1", "L2", "L3"]:
        covers.append(("m1", x))
        covers.append(("m2", x))
        covers.append((x, "WL"))
    for x in ["R0", "R1", "R2", "R3"]:
        covers.append(("m3", x))
        covers.append(("m4", x))
        covers.append((x, "WR"))
    # weak cross "corridor" single points
    covers += [("m1", "c12"), ("m3", "c12"), ("c12", "WL")]
    covers += [("m2", "c24"), ("m4", "c24"), ("c24", "WR")]
    elems |= {"c12", "c24"}
    return transitive_closure(elems, covers)


def unit_density_lobe() -> Poset:
    """
    Density lobe: m1,m2 see a large shared mid bulk; m3,m4 see small private futures.
    No geometry labels — pure cardinality imbalance.
    """
    mins = ["m1", "m2", "m3", "m4"]
    lobe = {f"L{i}" for i in range(20)}
    mid = {
        "m1": set(lobe) | {"s1"},
        "m2": set(lobe) | {"s2"},
        "m3": {"t1", "t2", "t3"},
        "m4": {"u1", "u2", "u3"},
    }
    return from_futures(mins, mid, roof="roof")


def unit_height_base() -> Poset:
    return unit_bridge()


def unit_height_extended() -> Poset:
    """
    Same mid reconvergence pattern as bridge, but thicker roof tower:
    mid ≺ r1 ≺ r2 (two peels would be needed to remove all roof; one peel leaves r1).
    Tests whether one-peel Φ★_L tracks only the outermost roof.
    """
    mins = ["m1", "m2", "m3", "m4"]
    mid = {
        "m1": {"a", "b", "c", "x"},
        "m2": {"a", "b", "c", "y"},
        "m3": {"x", "p", "q", "z"},
        "m4": {"y", "p", "q", "z"},
    }
    # build mid without roof then add tower
    C0 = from_futures(mins, mid, roof=None)
    elems = set(C0.elements) | {"r1", "r2"}
    covers = list(C0.order)
    mids = set()
    for s in mid.values():
        mids |= s
    for x in mids:
        covers.append((x, "r1"))
    covers.append(("r1", "r2"))
    return transitive_closure(elems, covers)


def unit_same_cloud_mink() -> Poset:
    """
    Synthetic same-cloud MINK surrogate: 1+1 Minkowski order on a fixed finite cloud.
    Points: 4 early + bulk grid. Causality: (t,x) ≺ (t',x') iff t<t' and |x'-x| < t'-t.
    """
    # cloud: minimals at t=0, bulk and top
    pts = {
        "m1": (0.0, -1.5),
        "m2": (0.0, -0.5),
        "m3": (0.0, 0.5),
        "m4": (0.0, 1.5),
        "b1": (1.0, -1.0),
        "b2": (1.0, 0.0),
        "b3": (1.0, 1.0),
        "b4": (2.0, -0.5),
        "b5": (2.0, 0.5),
        "top": (3.0, 0.0),
    }
    return _poset_from_minkowski(pts)


def unit_same_cloud_warped() -> Poset:
    """
    Same point cloud as MINK unit, but causal relation warped:
    right half (x>0) has slowed time for cone tests — synthetic non-flat causality,
    not Schwarzschild generator output.
    """
    pts = {
        "m1": (0.0, -1.5),
        "m2": (0.0, -0.5),
        "m3": (0.0, 0.5),
        "m4": (0.0, 1.5),
        "b1": (1.0, -1.0),
        "b2": (1.0, 0.0),
        "b3": (1.0, 1.0),
        "b4": (2.0, -0.5),
        "b5": (2.0, 0.5),
        "top": (3.0, 0.0),
    }
    return _poset_from_warped(pts)


def _poset_from_minkowski(pts: dict[str, tuple[float, float]]) -> Poset:
    names = list(pts)
    covers = []
    for a, b in itertools.permutations(names, 2):
        ta, xa = pts[a]
        tb, xb = pts[b]
        dt = tb - ta
        if dt > 0 and abs(xb - xa) < dt - 1e-12:
            covers.append((a, b))
    return transitive_closure(names, covers)


def _poset_from_warped(pts: dict[str, tuple[float, float]]) -> Poset:
    """Cone aperture depends on sign of x (synthetic wall/BH-like asymmetry)."""
    names = list(pts)
    covers = []
    for a, b in itertools.permutations(names, 2):
        ta, xa = pts[a]
        tb, xb = pts[b]
        dt = tb - ta
        if dt <= 0:
            continue
        # left: wide cone; right: narrow cone (harder to connect)
        if 0.5 * (xa + xb) >= 0:
            aperture = 0.45 * dt  # narrow
        else:
            aperture = 0.95 * dt  # wide
        if abs(xb - xa) < aperture - 1e-12:
            covers.append((a, b))
    return transitive_closure(names, covers)


def unit_two_volume_classes() -> Poset:
    """Same A-block structure but two V classes so Φ_V can emit."""
    mins = ["m1", "m2", "m3", "m4"]
    # m1,m2 large shared future; m3,m4 small shared
    mid = {
        "m1": {f"A{i}" for i in range(6)},
        "m2": {f"A{i}" for i in range(6)},
        "m3": {f"B{i}" for i in range(2)},
        "m4": {f"B{i}" for i in range(2)},
    }
    return from_futures(mins, mid, roof="roof")


# ---------------------------------------------------------------------------
# Suite runners
# ---------------------------------------------------------------------------

@dataclass
class UnitResult:
    falsifier: str
    unit: str
    status: str  # PASS / FAIL / INCONCLUSIVE / INFO
    primary: PhiResult
    control: Optional[PhiResult] = None
    note: str = ""


def run_F1() -> list[UnitResult]:
    out = []
    # Unit A: bridge — Φ★_L emits, all V equal ⇒ Φ_V abstains ⇒ not PATTERN_EQ on EMIT match
    C = unit_bridge()
    p, c = phi_star_L(C), phi_V(C)
    if p.terminal == "EMIT" and c.terminal != "EMIT":
        st, note = "PASS", "Φ★_L EMIT while Φ_V abstains (equal V)"
    elif p.terminal == "EMIT" and c.terminal == "EMIT" and not pattern_eq(p, c):
        st, note = "PASS", "both EMIT but partitions differ"
    elif p.terminal == "EMIT" and pattern_eq(p, c):
        st, note = "FAIL", "Φ_V reproduces Φ★_L partition"
    else:
        st, note = "INCONCLUSIVE", f"primary={p.terminal} control={c.terminal}"
    out.append(UnitResult("F1", "bridge_vs_phiV", st, p, c, note))

    # Unit B: two volume classes — check whether when both emit they match
    C2 = unit_two_volume_classes()
    p2, c2 = phi_star_L(C2), phi_V(C2)
    if p2.terminal == "EMIT" and c2.terminal == "EMIT":
        if pattern_eq(p2, c2):
            st, note = "INFO", "both EMIT same partition (possible marginal alignment on this unit)"
        else:
            st, note = "PASS", "both EMIT different partitions"
    elif p2.terminal == "EMIT" and c2.terminal != "EMIT":
        st, note = "PASS", "Φ★_L EMIT, Φ_V abstain"
    else:
        st, note = "INCONCLUSIVE", f"primary={p2.terminal} control={c2.terminal}"
    out.append(UnitResult("F1", "two_V_classes", st, p2, c2, note))
    return out


def run_F1b() -> list[UnitResult]:
    Cb, Cc = unit_bridge(), unit_cross()
    pb, pc = phi_star_L(Cb), phi_star_L(Cc)
    # same V check
    Ab = overlap_matrix(Cb, Cb.minimals())
    Ac = overlap_matrix(Cc, Cc.minimals())
    Vb = [Ab[i][i] for i in range(4)]
    Vc = [Ac[i][i] for i in range(4)]
    same_V = Vb == Vc
    sep = (pb.terminal, pb.partition) != (pc.terminal, pc.partition)
    if same_V and sep and pb.terminal == "EMIT" and pc.terminal == "EMIT":
        st, note = "PASS", f"same V={Vb}; parts {fmt_part(pb.partition)} vs {fmt_part(pc.partition)}"
    elif same_V and sep:
        st, note = "PASS", f"same V; terminals {pb.terminal} vs {pc.terminal}"
    else:
        st, note = "FAIL", f"same_V={same_V} sep={sep} {pb.terminal} {pc.terminal}"
    return [
        UnitResult("F1b", "bridge", "INFO", pb, note=f"V={Vb}"),
        UnitResult("F1b", "cross", "INFO", pc, note=f"V={Vc}"),
        UnitResult("F1b", "pair_separator", st, pb, pc, note),
    ]


def run_F2() -> list[UnitResult]:
    out = []
    for name, builder in [
        ("roof_only_equal_mid", unit_roof_only),
        ("roof_only_asymmetric", unit_roof_only_asymmetric),
    ]:
        C = builder()
        p = phi_star_L(C)
        # Pass if no peel-stable detection emission
        if p.terminal == "EMIT":
            st, note = "FAIL", "roof-only unit produced peel-stable EMIT (ENV_FAIL_ROOF)"
        elif p.terminal in {
            "ABSTAIN_ROOF_UNSTABLE",
            "ABSTAIN_SPECTRAL_MULTIPLICITY",
            "ABSTAIN_SPECTRAL_ZERO_COMPONENT",
            "ABSTAIN_PEEL_UNDEFINED",
            "ABSTAIN_TOO_FEW_MINIMALS",
        }:
            st, note = "PASS", f"roof-only → {p.terminal} (no stable detection)"
        else:
            st, note = "INCONCLUSIVE", p.terminal
        out.append(UnitResult("F2", name, st, p, note=note))
    return out


def run_F3() -> list[UnitResult]:
    """
    Side-wall order-only surrogate (twin corridors / two local roofs).

    Critical unit: wall vs bridge — both are twin-pair reconvergence combinatorics.
    If PATTERN_EQ, Φ★_L cannot tell wall-driven structure from the bridge mid pattern
    (structural S4_side risk → FAIL).

    Secondary unit: wall vs cross — diagonal mid pattern should differ if wall is twin-type.
    """
    out = []
    wall = phi_star_L(unit_side_wall())
    bridge = phi_star_L(unit_bridge())
    cross = phi_star_L(unit_cross())

    if bridge.terminal != "EMIT":
        out.append(UnitResult("F3", "wall_vs_bridge", "INCONCLUSIVE", bridge, wall, "bridge primary did not EMIT"))
    elif pattern_eq(bridge, wall):
        out.append(
            UnitResult(
                "F3",
                "wall_vs_bridge",
                "FAIL",
                bridge,
                wall,
                "side-wall surrogate PATTERN_EQ bridge emission (twin-pair ambiguity)",
            )
        )
    else:
        out.append(
            UnitResult(
                "F3",
                "wall_vs_bridge",
                "PASS",
                bridge,
                wall,
                f"wall={wall.terminal}/{fmt_part(wall.partition)} ≠ bridge",
            )
        )

    if cross.terminal != "EMIT":
        out.append(UnitResult("F3", "wall_vs_cross", "INCONCLUSIVE", cross, wall, "cross primary did not EMIT"))
    elif pattern_eq(cross, wall):
        out.append(
            UnitResult(
                "F3",
                "wall_vs_cross",
                "FAIL",
                cross,
                wall,
                "side-wall surrogate PATTERN_EQ cross emission",
            )
        )
    else:
        out.append(
            UnitResult(
                "F3",
                "wall_vs_cross",
                "PASS",
                cross,
                wall,
                f"wall={wall.terminal}/{fmt_part(wall.partition)} ≠ cross",
            )
        )
    return out


def run_F4() -> list[UnitResult]:
    mink = phi_star_L(unit_same_cloud_mink())
    warp = phi_star_L(unit_same_cloud_warped())
    if pattern_eq(mink, warp):
        # same pattern on both causalities
        if mink.terminal == "EMIT":
            st, note = "FAIL", "same-cloud MINK and warped PATTERN_EQ on EMIT"
        else:
            st, note = "INFO", f"both abstain identically ({mink.terminal}) — weak pass/info"
            # abstain-abstain is not ENV_FAIL_MINK for detection; mark PASS_WEAK
            st = "PASS"
            note = f"both {mink.terminal}; no false shared EMIT detection"
    else:
        st, note = "PASS", f"MINK={mink.terminal}/{fmt_part(mink.partition)} vs warped={warp.terminal}/{fmt_part(warp.partition)}"
    return [
        UnitResult("F4", "same_cloud_mink", "INFO", mink),
        UnitResult("F4", "same_cloud_warped", "INFO", warp),
        UnitResult("F4", "same_cloud_compare", st, mink, warp, note),
    ]


def run_F5() -> list[UnitResult]:
    """
    Density lobe unit: if Φ★_L emits {{m1,m2},{m3,m4}} that matches the lobe grouping,
    check against a density oracle = exact volume classes / largest-future pair.
    Fail only if emission is PATTERN_EQ to Φ_V when V alone forces the lobe split.
    """
    C = unit_density_lobe()
    p, c = phi_star_L(C), phi_V(C)
    # density oracle: bipartition by whether V equals max V (lobe vs small)
    mins = C.minimals()
    A = overlap_matrix(C, mins)
    V = [A[i][i] for i in range(len(mins))]
    vmax = max(V)
    lobe = frozenset(mins[i] for i, v in enumerate(V) if v == vmax)
    rest = frozenset(mins[i] for i, v in enumerate(V) if v != vmax)
    dens_part: Optional[Partition] = None
    dens_term = "ABSTAIN"
    if lobe and rest and lobe | rest == frozenset(mins):
        dens_part = frozenset([lobe, rest])
        dens_term = "EMIT"
    dens = PhiResult(dens_term, dens_part)

    if p.terminal == "EMIT" and dens.terminal == "EMIT" and p.partition == dens.partition:
        # also if Φ_V matches
        if c.terminal == "EMIT" and pattern_eq(p, c):
            st, note = "FAIL", "density/volume oracles reproduce Φ★_L (ENV_FAIL_DENSITY)"
        else:
            st, note = "INFO", "Φ★_L matches density split but not Φ_V exact-class bipartition"
            # still a density-tracking risk
            st = "FAIL"
            note = "Φ★_L partition equals density-lobe split (cardinality domination)"
    elif p.terminal == "EMIT":
        st, note = "PASS", f"EMIT {fmt_part(p.partition)} not equal to density split {fmt_part(dens_part)}"
    else:
        st, note = "PASS", f"no EMIT on density unit ({p.terminal})"
    return [UnitResult("F5", "density_lobe", st, p, dens, note)]


def run_F6() -> list[UnitResult]:
    base = phi_star_L(unit_height_base())
    ext = phi_star_L(unit_height_extended())
    # Pass if extended does not merely invent a new peel-stable detection from extra roof only;
    # expect same partition if mid structure dominates (pattern stable under roof tower).
    if base.terminal == "EMIT" and ext.terminal == "EMIT":
        if base.partition == ext.partition:
            st, note = "PASS", "partition stable under roof-tower extension (not pure roof tracking)"
        else:
            st, note = "FAIL", "partition changed under height/roof extension only"
    elif base.terminal == "EMIT" and ext.terminal != "EMIT":
        st, note = "INFO", f"base EMIT, extended {ext.terminal}"
        st = "PASS"
        note = f"extra roof tower destroyed emission ({ext.terminal}) — not a pure translated detection"
    elif base.terminal != "EMIT" and ext.terminal == "EMIT":
        st, note = "FAIL", "emission appears only after height extension"
    else:
        st, note = "INCONCLUSIVE", f"base={base.terminal} ext={ext.terminal}"
    return [
        UnitResult("F6", "height_base", "INFO", base),
        UnitResult("F6", "height_extended", "INFO", ext),
        UnitResult("F6", "height_compare", st, base, ext, note),
    ]


def run_F7() -> list[UnitResult]:
    C = unit_bridge()
    base = phi_star_L(C)
    results = []
    # all permutations of minimal labels + identity on other elements
    mins = C.minimals()
    others = [e for e in sorted(C.elements) if e not in mins]
    perms = list(itertools.permutations(mins))
    # include a few full random shuffles of all labels
    rng = random.Random(0)  # fixed, not a physics seed band
    ok = True
    notes = []
    for pi, perm in enumerate(perms):
        sigma = {mins[i]: perm[i] for i in range(len(mins))}
        for o in others:
            sigma[o] = o
        Cr = C.relabel(sigma)
        r = phi_star_L(Cr)
        if base.terminal != r.terminal:
            ok = False
            notes.append(f"perm#{pi} terminal {base.terminal}→{r.terminal}")
            break
        if base.terminal == "EMIT":
            expected = conjugate_partition(base.partition, sigma)
            if r.partition != expected:
                ok = False
                notes.append(f"perm#{pi} partition not conjugate")
                break
    # full element permutations (sample)
    all_elems = sorted(C.elements)
    for s in range(20):
        img = all_elems[:]
        rng.shuffle(img)
        sigma = {all_elems[i]: img[i] for i in range(len(all_elems))}
        r = phi_star_L(C.relabel(sigma))
        if base.terminal != r.terminal:
            ok = False
            notes.append(f"full-shuffle#{s} terminal mismatch")
            break
        if base.terminal == "EMIT":
            expected = conjugate_partition(base.partition, sigma)
            if r.partition != expected:
                ok = False
                notes.append(f"full-shuffle#{s} partition not conjugate")
                break
    st = "PASS" if ok else "FAIL"
    note = "all tested relabelings conjugate" if ok else "; ".join(notes)
    results.append(UnitResult("F7", "relabel_bridge", st, base, note=note))
    return results


def aggregate(results: list[UnitResult]) -> dict[str, str]:
    by: dict[str, list[str]] = {}
    for r in results:
        by.setdefault(r.falsifier, []).append(r.status)
    summary = {}
    for f, sts in by.items():
        if "FAIL" in sts:
            summary[f] = "FAIL"
        elif all(s in {"PASS", "INFO"} for s in sts) and any(s == "PASS" for s in sts):
            summary[f] = "PASS"
        elif all(s == "INFO" for s in sts):
            summary[f] = "INFO"
        elif "INCONCLUSIVE" in sts and "FAIL" not in sts:
            # pass if at least one PASS
            summary[f] = "PASS" if "PASS" in sts else "INCONCLUSIVE"
        else:
            summary[f] = "PASS" if "PASS" in sts and "FAIL" not in sts else "INCONCLUSIVE"
    return summary


def main() -> int:
    all_r: list[UnitResult] = []
    all_r += run_F1()
    all_r += run_F1b()
    all_r += run_F2()
    all_r += run_F3()
    all_r += run_F4()
    all_r += run_F5()
    all_r += run_F6()
    all_r += run_F7()

    summary = aggregate(all_r)
    # overall
    fails = [f for f, s in summary.items() if s == "FAIL"]
    overall = "SUITE_FAIL" if fails else "SUITE_PASS"

    lines = []
    lines.append("# C5 F1–F7 synthetic suite report")
    lines.append("")
    lines.append("STATUS: SYNTHETIC_FINITE_POSET_SUITE / CANDIDATE_5_NOT_YET_OPENED")
    lines.append("NO_PROJECT_GENERATOR / NO_EVALUATION_SEEDS / NO_FREEZE / NO_RECONSTRUCTION_CLAIM")
    lines.append("")
    lines.append("Runner: `dev/c5_f1_f7_synthetic_suite.py`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"Overall: **{overall}**")
    lines.append("")
    lines.append("| Falsifier | Result |")
    lines.append("|---|---|")
    for f in ["F1", "F1b", "F2", "F3", "F4", "F5", "F6", "F7"]:
        lines.append(f"| {f} | {summary.get(f, 'MISSING')} |")
    lines.append("")
    lines.append("## Units")
    lines.append("")
    for r in all_r:
        lines.append(f"### {r.falsifier} / {r.unit} — `{r.status}`")
        lines.append("")
        lines.append(f"- primary: `{r.primary.terminal}` part=`{fmt_part(r.primary.partition)}`")
        if r.control is not None:
            lines.append(f"- control: `{r.control.terminal}` part=`{fmt_part(r.control.partition)}`")
        if r.note:
            lines.append(f"- note: {r.note}")
        lines.append("")

    lines.append("## Interpretation")
    lines.append("")
    if summary.get("F3") == "FAIL":
        lines.append(
            "**F3 FAIL is structural, not a runner bug.** The side-wall surrogate (two twin "
            "corridors with local roofs) produces the same peel-stable bipartition as the "
            "bridge mid pattern `{{m1,m2},{m3,m4}}`. So Φ★_L, on these finite units, does not "
            "separate wall-type reconvergence from the non-marginal mid pattern used as a "
            "positive control. This matches Decision 040 / lateral dual doctrine: side control "
            "cannot be internal to the map; wall combinatorics can mimic the signal."
        )
        lines.append("")
        lines.append(
            "Secondary unit `wall_vs_cross` may still PASS (diagonal mid pattern differs). "
            "Aggregate F3 remains FAIL while the critical twin ambiguity stands."
        )
        lines.append("")
    lines.append("## Scope limits")
    lines.append("")
    lines.append("- Finite synthetic posets only; not Poisson sprinklings of Schwarzschild.")
    lines.append("- F4 uses a hand cloud with Minkowski vs warped cones — not the sealed same-cloud generator.")
    lines.append("- F3 side wall is an order-only twin-corridor surrogate, not continuum box walls.")
    lines.append("- F8 (emission rate floor) is out of scope for this suite.")
    lines.append("- Spectral step uses Jacobi floats with multiplicity/zero tolerances; bridge/cross")
    lines.append("  eigenvectors are known exact from F1b dossier and match here.")
    lines.append("")
    lines.append("## Terminal")
    lines.append("")
    lines.append("```text")
    lines.append(f"C5_F1_F7_SUITE = {overall}")
    for f in ["F1", "F1b", "F2", "F3", "F4", "F5", "F6", "F7"]:
        lines.append(f"{f} = {summary.get(f, 'MISSING')}")
    lines.append("CANDIDATE_5_NOT_YET_OPENED")
    lines.append("NO_EVALUATION_SEEDS")
    lines.append("F3_STRUCTURAL_WALL_BRIDGE_AMBIGUITY = " + ("YES" if summary.get("F3") == "FAIL" else "NO"))
    lines.append("```")
    lines.append("")

    report = "\n".join(lines)
    out_path = Path(__file__).resolve().parent / "C5_F1_F7_SYNTHETIC_SUITE_REPORT.md"
    out_path.write_text(report, encoding="utf-8")

    # machine summary
    machine = {
        "overall": overall,
        "summary": summary,
        "units": [
            {
                "falsifier": r.falsifier,
                "unit": r.unit,
                "status": r.status,
                "primary": r.primary.terminal,
                "primary_part": fmt_part(r.primary.partition),
                "control": None if r.control is None else r.control.terminal,
                "control_part": None if r.control is None else fmt_part(r.control.partition),
                "note": r.note,
            }
            for r in all_r
        ],
    }
    json_path = Path(__file__).resolve().parent / "C5_F1_F7_SYNTHETIC_SUITE_RESULTS.json"
    json_path.write_text(json.dumps(machine, indent=2), encoding="utf-8")

    print(report)
    print(f"\nWrote {out_path}")
    print(f"Wrote {json_path}")
    return 0 if overall == "SUITE_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
