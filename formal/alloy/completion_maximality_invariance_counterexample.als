module completion_maximality_invariance_counterexample

// Bounded counterexample for the claim:
// "Whether an observed element is maximal is invariant across completions
// that agree on the observed subposet."

sig Element {}

one sig Observation {
  elems: set Element
}

abstract sig Completion {
  elems: set Element,
  lt: Element -> Element
}

one sig A extends Completion {}
one sig B extends Completion {}

pred strictOrder[c: Completion] {
  c.lt in (c.elems -> c.elems)
  no (iden & c.lt)
  (c.lt).(c.lt) in c.lt
}

fact WellFormed {
  all c: Completion | strictOrder[c]

  // The observed fragment has exactly two elements.
  #Observation.elems = 2

  // Both completions extend the same observed fragment.
  Observation.elems in A.elems
  Observation.elems in B.elems

  // The completions share only the observed fragment.
  A.elems & B.elems = Observation.elems

  // Each completion adds exactly one different hidden element.
  #(A.elems - Observation.elems) = 1
  #(B.elems - Observation.elems) = 1

  // The induced observed order is identical in both completions.
  (A.lt & (Observation.elems -> Observation.elems))
    =
  (B.lt & (Observation.elems -> Observation.elems))
}

assert ObservedMaximalityIsCompletionInvariant {
  all e: Observation.elems |
    (
      no ((e -> Element) & A.lt)
      iff
      no ((e -> Element) & B.lt)
    )
}

check ObservedMaximalityIsCompletionInvariant for exactly 4 Element
