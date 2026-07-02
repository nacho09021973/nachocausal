import HorizonFormal.Accessibility

/-!
# Horizon

Pregeometric relational horizon vocabulary, kept at the order-theoretic level.

This file intentionally avoids any event-horizon, Schwarzschild, GKP, or sprinkling
claim. It only records the finite-poset relational shape needed by the notes.

## Orientation correction (2026-07-02)

The original definition took horizon pairs `(x, y)` with `x ∈ B_R` (black-region
candidate) and `y ∈ A_R` (relational past of escape). That set is provably empty
for every `R` in every preorder: `A_R = ↓R` is a lower set, so `x < y ≤ r ∈ R`
forces `x ∈ A_R`, contradicting `x ∈ B_R`. The vacuous version is kept below as
`RelationalHorizonOld` with the tombstone theorem `relationalHorizonOld_eq_empty`,
so the correction is itself a checkable statement rather than silent history; a
non-emptiness witness for the corrected orientation (`VPoset`, at the end of this
file) exists so the formalisation can fail.

The corrected orientation takes crossing links from the relational past of escape
*into* the black-region candidate — infalling links, matching the Dou–Sorkin
orientation (lower element outside the horizon, upper element inside;
arXiv:gr-qc/0302009).

What is and is not automatic: because `B_R` is an upper set, *no* causal relation
leaves `B_R` into `A_R` (`relationalBlackRegion_no_escape`). This is only the
one-way prohibition. It does not by itself establish exterior-future development,
wall/inhomogeneity discrimination, persistence, or any physical horizon claim;
all of that burden lies with the (still open) selection rule for `R`.
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

/--
Boundary interface between `A_R` and `B_R`, expressed only with the order:
infalling crossing links, from the relational past of escape into the
black-region candidate (corrected orientation, 2026-07-02).
-/
def RelationalHorizon (R : RelationalReference P) : Set (P × P) :=
  {p : P × P |
    p.1 ∈ RelationalPast R ∧
    p.2 ∈ RelationalBlackRegion R ∧
    IsCover p.1 p.2}

/--
Tombstone: the pre-correction orientation (black region below, relational past
above). Kept only as the subject of `relationalHorizonOld_eq_empty`; do not use.
-/
def RelationalHorizonOld (R : RelationalReference P) : Set (P × P) :=
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

/--
One-way prohibition (the only automatic component of any asymmetry condition):
no causal relation leaves the black-region candidate into the relational past.
-/
theorem relationalBlackRegion_no_escape {R : RelationalReference P} {x y : P}
    (hx : x ∈ RelationalBlackRegion R) (hy : y ∈ RelationalPast R) :
    ¬ x ≤ y :=
  fun hxy => hx (relationalPast_lower hxy hy)

/--
Tombstone theorem: the pre-correction orientation is empty for every reference
`R`, in every preorder — no finitude, antisymmetry, or sprinkling hypothesis.
This is why the orientation had to be corrected.
-/
theorem relationalHorizonOld_eq_empty (R : RelationalReference P) :
    RelationalHorizonOld R = ∅ := by
  ext p
  simp only [Set.mem_empty_iff_false, iff_false]
  rintro ⟨hblack, hpast, hlt, -⟩
  exact hblack (relationalPast_lower hlt.le hpast)

theorem mem_relationalHorizon_pair {R : RelationalReference P} {x y : P}
    (hx : x ∈ RelationalPast R) (hy : y ∈ RelationalBlackRegion R)
    (hcover : IsCover x y) : (x, y) ∈ RelationalHorizon R :=
  ⟨hx, hy, hcover⟩

theorem relationalHorizon_fst_mem_past {R : RelationalReference P} {p : P × P}
    (hp : p ∈ RelationalHorizon R) : p.1 ∈ RelationalPast R :=
  hp.1

theorem relationalHorizon_snd_mem_black {R : RelationalReference P} {p : P × P}
    (hp : p ∈ RelationalHorizon R) : p.2 ∈ RelationalBlackRegion R :=
  hp.2.1

theorem relationalHorizon_isCover {R : RelationalReference P} {p : P × P}
    (hp : p ∈ RelationalHorizon R) : IsCover p.1 p.2 :=
  hp.2.2

theorem relationalHorizon_lt {R : RelationalReference P} {p : P × P}
    (hp : p ∈ RelationalHorizon R) : p.1 < p.2 :=
  (relationalHorizon_isCover hp).1

theorem relationalHorizon_ne {R : RelationalReference P} {p : P × P}
    (hp : p ∈ RelationalHorizon R) : p.1 ≠ p.2 :=
  ne_of_lt (relationalHorizon_lt hp)

theorem relationalHorizon_fst_not_mem_black {R : RelationalReference P} {p : P × P}
    (hp : p ∈ RelationalHorizon R) : p.1 ∉ RelationalBlackRegion R := by
  intro hblack
  exact hblack (relationalHorizon_fst_mem_past hp)

theorem relationalHorizon_snd_not_mem_past {R : RelationalReference P} {p : P × P}
    (hp : p ∈ RelationalHorizon R) : p.2 ∉ RelationalPast R :=
  relationalHorizon_snd_mem_black hp

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

/-!
## Non-emptiness witness

The corrected interface is non-vacuous: in the three-element V-shaped poset
`a < b`, `a < c`, `b ∥ c`, with escape reference `R = {b}` (a subset of the
maximal elements `{b, c}`), the infalling link `(a, c)` lies in
`RelationalHorizon R`. The old orientation admits no such example
(`relationalHorizonOld_eq_empty`), so this witness is what lets the
formalisation fail.
-/

/-- Three-element V-shaped witness poset: `a < b`, `a < c`, `b ∥ c`. -/
inductive VPoset : Type
  | a | b | c

namespace VPoset

/-- `a` below both `b` and `c`; `b` and `c` incomparable. -/
protected def le : VPoset → VPoset → Prop
  | .a, _ => True
  | .b, .b => True
  | .c, .c => True
  | _, _ => False

instance : Preorder VPoset where
  le := VPoset.le
  le_refl x := by cases x <;> trivial
  le_trans x y z hxy hyz := by
    cases x <;> cases y <;> cases z <;> trivial

theorem a_mem_relationalPast :
    VPoset.a ∈ RelationalPast ({VPoset.b} : RelationalReference VPoset) :=
  ⟨VPoset.b, rfl, trivial⟩

theorem c_mem_relationalBlackRegion :
    VPoset.c ∈ RelationalBlackRegion ({VPoset.b} : RelationalReference VPoset) := by
  rintro ⟨y, rfl, hcy⟩
  exact hcy

theorem lt_a_c : VPoset.a < VPoset.c :=
  ⟨trivial, fun h => h⟩

theorem isCover_a_c : IsCover VPoset.a VPoset.c := by
  refine ⟨lt_a_c, ?_⟩
  rintro ⟨z, hz1, hz2⟩
  cases z
  · exact hz1.2 trivial
  · exact hz2.1
  · exact hz2.2 trivial

/-- The corrected interface is non-empty on the V-poset with `R = {b} ⊆ max`. -/
theorem relationalHorizon_nonempty_witness :
    (VPoset.a, VPoset.c) ∈
      RelationalHorizon ({VPoset.b} : RelationalReference VPoset) :=
  ⟨a_mem_relationalPast, c_mem_relationalBlackRegion, isCover_a_c⟩

end VPoset

end HorizonFormal
