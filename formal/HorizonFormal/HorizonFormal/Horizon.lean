import HorizonFormal.Accessibility

/-!
# Horizon

Pregeometric relational horizon vocabulary, kept at the order-theoretic level.

This file intentionally avoids any event-horizon, Schwarzschild, GKP, or sprinkling
claim. It only records the finite-poset relational shape needed by the notes.
-/

namespace HorizonFormal

variable {P : Type u} [Preorder P]

/-- A reference subset representing escape/asymptotic future in a purely relational formulation. -/
abbrev RelationalReference (P : Type u) := Set P

/-- Relational past of a reference subset `R`: all points below some point in `R`. -/
def RelationalPast (R : RelationalReference P) : Set P :=
  {x : P | ∃ y : P, y ∈ R ∧ x ≤ y}

/-- Relational black-hole-region candidate: complement of the relational past of escape. -/
def RelationalBlackRegion (R : RelationalReference P) : Set P :=
  {x : P | x ∉ RelationalPast R}

/--
Cover/link relation placeholder.

For partial orders this is the immediate-cover relation: `x < y` and no strict
intermediate point. We keep it as a definition rather than relying on notation so
the causal-set use is explicit.
-/
def IsCover (x y : P) : Prop :=
  x < y ∧ ¬ ∃ z : P, x < z ∧ z < y

/-- Boundary interface between `B_R` and `A_R`, expressed only with the order. -/
def RelationalHorizon (R : RelationalReference P) : Set (P × P) :=
  {p : P × P |
    p.1 ∈ RelationalBlackRegion R ∧
    p.2 ∈ RelationalPast R ∧
    IsCover p.1 p.2}

theorem mem_relationalPast_of_mem {R : RelationalReference P} {x : P}
    (hx : x ∈ R) : x ∈ RelationalPast R :=
  ⟨x, hx, le_rfl⟩

theorem relationalPast_lower {R : RelationalReference P} {x y : P}
    (hxy : x ≤ y) (hy : y ∈ RelationalPast R) : x ∈ RelationalPast R := by
  obtain ⟨z, hzR, hyz⟩ := hy
  exact ⟨z, hzR, le_trans hxy hyz⟩

theorem relationalPast_mono {R S : RelationalReference P}
    (hRS : R ⊆ S) : RelationalPast R ⊆ RelationalPast S := by
  intro x hx
  obtain ⟨y, hyR, hxy⟩ := hx
  exact ⟨y, hRS hyR, hxy⟩

theorem relationalBlackRegion_antitone {R S : RelationalReference P}
    (hRS : R ⊆ S) : RelationalBlackRegion S ⊆ RelationalBlackRegion R := by
  intro x hxS hxR
  exact hxS (relationalPast_mono hRS hxR)

theorem relationalBlackRegion_upper {R : RelationalReference P} {x y : P}
    (hxy : x ≤ y) (hx : x ∈ RelationalBlackRegion R) :
    y ∈ RelationalBlackRegion R := by
  intro hy
  exact hx (relationalPast_lower hxy hy)

theorem relationalHorizon_fst_mem_black {R : RelationalReference P} {p : P × P}
    (hp : p ∈ RelationalHorizon R) : p.1 ∈ RelationalBlackRegion R :=
  hp.1

theorem relationalHorizon_snd_mem_past {R : RelationalReference P} {p : P × P}
    (hp : p ∈ RelationalHorizon R) : p.2 ∈ RelationalPast R :=
  hp.2.1

theorem relationalHorizon_isCover {R : RelationalReference P} {p : P × P}
    (hp : p ∈ RelationalHorizon R) : IsCover p.1 p.2 :=
  hp.2.2

@[simp]
theorem relationalPast_empty :
    RelationalPast (P := P) (∅ : RelationalReference P) = ∅ := by
  ext x
  simp [RelationalPast]

@[simp]
theorem relationalHorizon_empty :
    RelationalHorizon (P := P) (∅ : RelationalReference P) = ∅ := by
  ext p
  simp [RelationalHorizon]

@[simp]
theorem relationalPast_univ :
    RelationalPast (P := P) (Set.univ : RelationalReference P) = Set.univ := by
  ext x
  constructor
  · intro _
    exact Set.mem_univ x
  · intro _
    exact ⟨x, Set.mem_univ x, le_rfl⟩

@[simp]
theorem relationalBlackRegion_univ :
    RelationalBlackRegion (P := P) (Set.univ : RelationalReference P) = ∅ := by
  ext x
  simp [RelationalBlackRegion]

@[simp]
theorem relationalHorizon_univ :
    RelationalHorizon (P := P) (Set.univ : RelationalReference P) = ∅ := by
  ext p
  simp [RelationalHorizon]

end HorizonFormal
