import Mathlib.Algebra.Module.Submodule.Lattice

/-!
# Strict nesting, abstract witness form (Appendix D (D.10)–(D.12), Corollary E)

The paper's strict nesting `V_N \subsetneq V_{N+1}` is not proved by a dimension
comparison alone; it exhibits an explicit witness (`p_1 \odot p_N`, Appendix D (D.12))
lying in `V_{N+1}` but not in `V_N`. This module isolates exactly that
witness-based argument as an abstract fact about submodules of any module, which is
the actual logical content used once the witness is in hand.

Instantiating this against the real filtration `P_{N-1} \subset P_N` inside
`H = L^2_0([0,1])` — i.e. producing the witness itself — needs the shifted-Legendre
polynomial Hilbert space and is out of scope here (`OUT_OF_SCOPE_ANALYTIC`; see
`ClaimMap.md`). -/

namespace HorizonFormal.S1Paper

variable {R M : Type*} [Semiring R] [AddCommMonoid M] [Module R M]

/-- **Strict nesting from an explicit witness**: if `V ≤ W` and some `w ∈ W` is not in
`V`, then `V` is a *strict* submodule of `W`. This is exactly the logical shape of
Appendix D (D.10)–(D.12): a strict inclusion, not merely a dimension count. -/
theorem strict_nesting_of_witness {V W : Submodule R M} (hle : V ≤ W)
    {w : M} (hwW : w ∈ W) (hwV : w ∉ V) : V < W :=
  lt_of_le_of_ne hle (fun h => hwV (h ▸ hwW))

end HorizonFormal.S1Paper
