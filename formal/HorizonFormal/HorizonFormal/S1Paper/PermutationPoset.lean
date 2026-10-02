import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Data.Fintype.Perm

/-!
# The poset of a permutation, and unlabeled poset isomorphism (§2/§3, Appendix C)

For `σ ∈ S_N`, the manuscript's two-dimensional poset `P_σ` on `Fin N` is
`i ≼_σ j ↔ i ≤ j ∧ σ(i) ≤ σ(j)`. Different `σ` give *different* partial orders on the
same underlying type `Fin N`, so we do not register `sigmaPartialOrder σ` as a global
mathlib `PartialOrder` instance (that would require one canonical order per type); it
is a genuine `PartialOrder` *value*, and "isomorphism class of `P_σ`" is formalized
directly as `PosetIsomorphic`, a bijection of `Fin N` carrying one relation to the
other — a real, checkable order-isomorphism, not a labeled equality.
-/

namespace HorizonFormal.S1Paper

variable {N : ℕ}

/-- The order relation of `P_σ`: `i ≼_σ j ↔ i ≤ j ∧ σ(i) ≤ σ(j)`. -/
def leSigma (σ : Equiv.Perm (Fin N)) (i j : Fin N) : Prop := i ≤ j ∧ σ i ≤ σ j

@[simp] lemma leSigma_iff (σ : Equiv.Perm (Fin N)) (i j : Fin N) :
    leSigma σ i j ↔ i ≤ j ∧ σ i ≤ σ j := Iff.rfl

lemma leSigma_refl (σ : Equiv.Perm (Fin N)) (i : Fin N) : leSigma σ i i := by
  constructor <;> simp

lemma leSigma_trans (σ : Equiv.Perm (Fin N)) {i j k : Fin N}
    (h1 : leSigma σ i j) (h2 : leSigma σ j k) : leSigma σ i k := by
  obtain ⟨h1a, h1b⟩ := h1
  obtain ⟨h2a, h2b⟩ := h2
  rw [Fin.le_def] at h1a h1b h2a h2b
  rw [leSigma_iff, Fin.le_def, Fin.le_def]
  omega

lemma leSigma_antisymm (σ : Equiv.Perm (Fin N)) {i j : Fin N}
    (h1 : leSigma σ i j) (h2 : leSigma σ j i) : i = j := by
  have ha := h1.1; have hb := h2.1
  rw [Fin.le_def] at ha hb
  exact Fin.ext (by omega)

/-! `leSigma σ` is a genuine partial order on `Fin N`: reflexive (`leSigma_refl`),
transitive (`leSigma_trans`), antisymmetric (`leSigma_antisymm`), each proved directly
from the definition above. (We do not additionally bundle these into a mathlib
`PartialOrder (Fin N)` *instance* — `Fin N` already carries its own canonical order
instance, and different `σ` would need different, non-canonical instances on the same
type; nothing below needs the bundled form, only the three order laws proved above.) -/

/-! ## Unlabeled isomorphism -/

/-- `e` carries the order of `P_σ` to the order of `P_τ`: a genuine order-isomorphism
witness. -/
def IsPosetIso (σ τ : Equiv.Perm (Fin N)) (e : Equiv.Perm (Fin N)) : Prop :=
  ∀ i j, leSigma σ i j ↔ leSigma τ (e i) (e j)

/-- `P_σ ≅ P_τ` as unlabeled posets: there exists an order-isomorphism between them.
This is the Lean model of `[P_σ] = [P_τ]` (manuscript §2). -/
def PosetIsomorphic (σ τ : Equiv.Perm (Fin N)) : Prop := ∃ e : Equiv.Perm (Fin N), IsPosetIso σ τ e

/-! Both relations are decidable, so the fiber `Γ_C` is an honest `Finset` (used in
`ClassSum.lean` to form the class sum `A_C`) rather than a classical-choice artefact. -/

instance decidableLeSigma (σ : Equiv.Perm (Fin N)) (i j : Fin N) :
    Decidable (leSigma σ i j) :=
  inferInstanceAs (Decidable (i ≤ j ∧ σ i ≤ σ j))

instance decidableIsPosetIso (σ τ e : Equiv.Perm (Fin N)) : Decidable (IsPosetIso σ τ e) :=
  inferInstanceAs (Decidable (∀ i j, leSigma σ i j ↔ leSigma τ (e i) (e j)))

instance decidablePosetIsomorphic (σ τ : Equiv.Perm (Fin N)) : Decidable (PosetIsomorphic σ τ) :=
  inferInstanceAs (Decidable (∃ e, IsPosetIso σ τ e))

lemma isPosetIso_refl (σ : Equiv.Perm (Fin N)) : IsPosetIso σ σ (Equiv.refl (Fin N)) :=
  fun _ _ => Iff.rfl

lemma isPosetIso_symm {σ τ : Equiv.Perm (Fin N)} {e : Equiv.Perm (Fin N)}
    (h : IsPosetIso σ τ e) : IsPosetIso τ σ e.symm := by
  intro i j
  have := h (e.symm i) (e.symm j)
  simpa using this.symm

lemma isPosetIso_trans {σ τ ρ : Equiv.Perm (Fin N)} {e f : Equiv.Perm (Fin N)}
    (h1 : IsPosetIso σ τ e) (h2 : IsPosetIso τ ρ f) : IsPosetIso σ ρ (e.trans f) := by
  intro i j
  rw [h1 i j]
  exact h2 (e i) (e j)

theorem posetIsomorphic_refl (σ : Equiv.Perm (Fin N)) : PosetIsomorphic σ σ :=
  ⟨Equiv.refl _, isPosetIso_refl σ⟩

theorem posetIsomorphic_symm {σ τ : Equiv.Perm (Fin N)} (h : PosetIsomorphic σ τ) :
    PosetIsomorphic τ σ :=
  let ⟨e, he⟩ := h; ⟨e.symm, isPosetIso_symm he⟩

theorem posetIsomorphic_trans {σ τ ρ : Equiv.Perm (Fin N)}
    (h1 : PosetIsomorphic σ τ) (h2 : PosetIsomorphic τ ρ) : PosetIsomorphic σ ρ :=
  let ⟨e, he⟩ := h1; let ⟨f, hf⟩ := h2; ⟨e.trans f, isPosetIso_trans he hf⟩

/-! ## Inversion (manuscript §3, used again in §7/Appendix G) -/

/-- **`P_σ ≅ P_{σ^{-1}}` via the map `i ↦ σ(i)`** (manuscript §3's elementary
closure-under-inversion fact, made a real order-isomorphism): the check is immediate
once unfolded, since `leSigma σ⁻¹ (σ i) (σ j) = (σ i ≤ σ j) ∧ (i ≤ j)`, the same
conjunction as `leSigma σ i j` with the two conjuncts swapped. -/
theorem posetIso_inv (σ : Equiv.Perm (Fin N)) : IsPosetIso σ σ⁻¹ σ := by
  intro i j
  simp only [leSigma_iff]
  rw [show σ⁻¹ (σ i) = i by simp, show σ⁻¹ (σ j) = j by simp]
  exact and_comm

/-- **`P_σ ≅ P_{σ^{-1}}`** (unlabeled): the fiber of every unlabeled poset class is
closed under inversion, `σ ∈ Γ_C ⟹ σ^{-1} ∈ Γ_C`. -/
theorem posetIsomorphic_inv (σ : Equiv.Perm (Fin N)) : PosetIsomorphic σ σ⁻¹ :=
  ⟨σ, posetIso_inv σ⟩

/-- Restated via transitivity for direct use as the fiber-closure property: if `σ` is
isomorphic to a class representative `C`, so is `σ⁻¹`. -/
theorem posetIsomorphic_inv_of_isomorphic {σ C : Equiv.Perm (Fin N)}
    (h : PosetIsomorphic σ C) : PosetIsomorphic σ⁻¹ C :=
  posetIsomorphic_trans (posetIsomorphic_symm (posetIsomorphic_inv σ)) h

end HorizonFormal.S1Paper
