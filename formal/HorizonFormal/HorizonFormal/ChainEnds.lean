import HorizonFormal.CofinalChains
import HorizonFormal.Ends

/-!
# Chain ends

Option 2 for the Lean-first end notion: an end is represented by a non-terminal
cofinal chain, modulo mutual cofinal domination.

This remains purely order-theoretic. It does not assert that such classes are
event horizons, escape ends, or asymptotic boundaries in a finite causal set.
-/

namespace HorizonFormal

variable {P : Type u} {Q : Type v} [Preorder P] [Preorder Q]

/-- Chain `c` is eventually dominated by chain `d` in the cofinal preorder sense. -/
def ChainEventuallyLe (c d : Nat → P) : Prop :=
  ∀ n : Nat, ∃ m : Nat, c n ≤ d m

/-- Cofinal-chain equivalence: mutual eventual domination. -/
def CofinalChainEquivalent (c d : Nat → P) : Prop :=
  ChainEventuallyLe c d ∧ ChainEventuallyLe d c

theorem chainEventuallyLe_refl (c : Nat → P) : ChainEventuallyLe c c := by
  intro n
  exact ⟨n, le_rfl⟩

theorem cofinalChainEquivalent_refl (c : Nat → P) :
    CofinalChainEquivalent c c :=
  ⟨chainEventuallyLe_refl c, chainEventuallyLe_refl c⟩

theorem chainEventuallyLe_trans {c d e : Nat → P}
    (hcd : ChainEventuallyLe c d) (hde : ChainEventuallyLe d e) :
    ChainEventuallyLe c e := by
  intro n
  obtain ⟨m, hcm⟩ := hcd n
  obtain ⟨k, hdk⟩ := hde m
  exact ⟨k, le_trans hcm hdk⟩

theorem cofinalChainEquivalent_symm {c d : Nat → P}
    (h : CofinalChainEquivalent c d) : CofinalChainEquivalent d c :=
  ⟨h.2, h.1⟩

theorem cofinalChainEquivalent_trans {c d e : Nat → P}
    (hcd : CofinalChainEquivalent c d) (hde : CofinalChainEquivalent d e) :
    CofinalChainEquivalent c e :=
  ⟨chainEventuallyLe_trans hcd.1 hde.1,
    chainEventuallyLe_trans hde.2 hcd.2⟩

/-- Setoid of chains modulo cofinal equivalence. -/
def cofinalChainSetoid (P : Type u) [Preorder P] : Setoid (Nat → P) where
  r := CofinalChainEquivalent
  iseqv := ⟨cofinalChainEquivalent_refl, cofinalChainEquivalent_symm,
    cofinalChainEquivalent_trans⟩

/-- A non-terminal cofinal chain in a fixed ideal. -/
def NonterminalCofinalChainInIdeal (I : Order.Ideal P) : Type u :=
  {c : Nat → P // IsCofinalChainInIdeal I c ∧ ¬ IsTerminalCofinalChainInIdeal I c}

/-- Equivalence of non-terminal cofinal chains in the same ideal. -/
def NonterminalChainEquivalent {I : Order.Ideal P}
    (c d : NonterminalCofinalChainInIdeal I) : Prop :=
  CofinalChainEquivalent c.1 d.1

theorem nonterminalChainEquivalent_refl {I : Order.Ideal P}
    (c : NonterminalCofinalChainInIdeal I) :
    NonterminalChainEquivalent c c :=
  cofinalChainEquivalent_refl c.1

theorem nonterminalChainEquivalent_symm {I : Order.Ideal P}
    {c d : NonterminalCofinalChainInIdeal I}
    (h : NonterminalChainEquivalent c d) :
    NonterminalChainEquivalent d c :=
  cofinalChainEquivalent_symm h

theorem nonterminalChainEquivalent_trans {I : Order.Ideal P}
    {c d e : NonterminalCofinalChainInIdeal I}
    (hcd : NonterminalChainEquivalent c d)
    (hde : NonterminalChainEquivalent d e) :
    NonterminalChainEquivalent c e :=
  cofinalChainEquivalent_trans hcd hde

/-- Setoid of non-terminal cofinal chains inside a fixed ideal. -/
def nonterminalCofinalChainSetoid (I : Order.Ideal P) :
    Setoid (NonterminalCofinalChainInIdeal I) where
  r := NonterminalChainEquivalent
  iseqv := ⟨nonterminalChainEquivalent_refl, nonterminalChainEquivalent_symm,
    nonterminalChainEquivalent_trans⟩

/--
Chain-end classes inside a fixed ideal.

This is the option-2 replacement candidate for the broad provisional
`IdealEnd = non-principal ideal` definition.
-/
def ChainEndInIdeal (I : Order.Ideal P) : Type u :=
  Quotient (nonterminalCofinalChainSetoid I)

/-- Package an explicit non-terminal cofinal chain as a chain-end class. -/
def chainEndInIdealOfNonterminalChain {I : Order.Ideal P}
    (c : Nat → P) (hc : IsCofinalChainInIdeal I c)
    (hterm : ¬ IsTerminalCofinalChainInIdeal I c) : ChainEndInIdeal I :=
  Quotient.mk (nonterminalCofinalChainSetoid I) ⟨c, hc, hterm⟩

/-- Countable non-principal ideals have an inhabited chain-end quotient. -/
noncomputable def chainEndInIdealOfCountableNonprincipal (I : Order.Ideal P)
    (hcount : (I : Set P).Countable) (hnonprincipal : IsNonprincipalIdeal I) :
    ChainEndInIdeal I :=
  let witness := exists_nonterminal_cofinalChain_of_countable_nonprincipalIdeal
    I hcount hnonprincipal
  chainEndInIdealOfNonterminalChain (Classical.choose witness)
    (Classical.choose_spec witness).1
    (Classical.choose_spec witness).2

/--
An ambient chain end: a non-principal ideal together with a chain-end class in
that ideal.
-/
def ChainEnd (P : Type u) [Preorder P] : Type u :=
  Σ I : IdealEnd P, ChainEndInIdeal I.1

/-- Countable provisional ideal-ends have a chain-end representative. -/
noncomputable def chainEndOfCountableIdealEnd (I : IdealEnd P)
    (hcount : (I.1 : Set P).Countable) : ChainEnd P :=
  ⟨I, chainEndInIdealOfCountableNonprincipal I.1 hcount I.2⟩

/-- Transport a chain pointwise across an order isomorphism. -/
def mapChainOrderIso (e : P ≃o Q) (c : Nat → P) : Nat → Q :=
  fun n => e (c n)

theorem mapChainOrderIso_nondec (e : P ≃o Q) {c : Nat → P}
    (hc : IsNondecreasingSeq c) :
    IsNondecreasingSeq (mapChainOrderIso e c) := by
  intro n
  exact (OrderIsoClass.map_le_map_iff e).mpr (hc n)

theorem chainEventuallyLe_mapOrderIso (e : P ≃o Q) {c d : Nat → P}
    (h : ChainEventuallyLe c d) :
    ChainEventuallyLe (mapChainOrderIso e c) (mapChainOrderIso e d) := by
  intro n
  obtain ⟨m, hle⟩ := h n
  exact ⟨m, (OrderIsoClass.map_le_map_iff e).mpr hle⟩

theorem cofinalChainEquivalent_mapOrderIso (e : P ≃o Q) {c d : Nat → P}
    (h : CofinalChainEquivalent c d) :
    CofinalChainEquivalent (mapChainOrderIso e c) (mapChainOrderIso e d) :=
  ⟨chainEventuallyLe_mapOrderIso e h.1, chainEventuallyLe_mapOrderIso e h.2⟩

theorem mapChainOrderIso_cofinalSeqInIdeal (e : P ≃o Q)
    {I : Order.Ideal P} {c : Nat → P}
    (hc : IsCofinalSeqInIdeal I c) :
    IsCofinalSeqInIdeal (mapIdealOrderIso e I) (mapChainOrderIso e c) := by
  constructor
  · intro n
    exact ⟨c n, hc.1 n, rfl⟩
  · intro y hy
    obtain ⟨n, hn⟩ := hc.2 (e.symm y) (by simpa using hy)
    refine ⟨n, ?_⟩
    simpa [mapChainOrderIso] using (OrderIsoClass.map_le_map_iff e).mpr hn

theorem mapChainOrderIso_cofinalChainInIdeal (e : P ≃o Q)
    {I : Order.Ideal P} {c : Nat → P}
    (hc : IsCofinalChainInIdeal I c) :
    IsCofinalChainInIdeal (mapIdealOrderIso e I) (mapChainOrderIso e c) :=
  ⟨mapChainOrderIso_nondec e hc.1, mapChainOrderIso_cofinalSeqInIdeal e hc.2⟩

theorem mapChainOrderIso_not_terminal (e : P ≃o Q)
    {I : Order.Ideal P} {c : Nat → P}
    (hnot : ¬ IsTerminalCofinalChainInIdeal I c) :
    ¬ IsTerminalCofinalChainInIdeal (mapIdealOrderIso e I) (mapChainOrderIso e c) := by
  intro hterm
  obtain ⟨n, hn⟩ := hterm
  apply hnot
  refine ⟨n, ?_⟩
  intro x hx
  have hmap : e x ≤ e (c n) := hn (e x) ⟨x, hx, rfl⟩
  exact (OrderIsoClass.map_le_map_iff e).mp hmap

def mapNonterminalChainOrderIso (e : P ≃o Q) {I : Order.Ideal P} :
    NonterminalCofinalChainInIdeal I →
    NonterminalCofinalChainInIdeal (mapIdealOrderIso e I) :=
  fun c =>
    ⟨mapChainOrderIso e c.1,
      mapChainOrderIso_cofinalChainInIdeal e c.2.1,
      mapChainOrderIso_not_terminal e c.2.2⟩

theorem mapNonterminalChainOrderIso_respects_equiv (e : P ≃o Q)
    {I : Order.Ideal P} {c d : NonterminalCofinalChainInIdeal I}
    (h : NonterminalChainEquivalent c d) :
    NonterminalChainEquivalent
      (mapNonterminalChainOrderIso e c) (mapNonterminalChainOrderIso e d) :=
  cofinalChainEquivalent_mapOrderIso e h

def mapChainEndInIdealOrderIso (e : P ≃o Q) (I : Order.Ideal P) :
    ChainEndInIdeal I → ChainEndInIdeal (mapIdealOrderIso e I) :=
  Quotient.map (mapNonterminalChainOrderIso e)
    (fun _ _ h => mapNonterminalChainOrderIso_respects_equiv e h)

def mapChainEndOrderIso (e : P ≃o Q) : ChainEnd P → ChainEnd Q :=
  fun end_ =>
    ⟨mapIdealEndOrderIso e end_.1,
      mapChainEndInIdealOrderIso e end_.1.1 end_.2⟩

end HorizonFormal
