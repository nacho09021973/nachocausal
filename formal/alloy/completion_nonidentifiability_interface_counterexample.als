module completion_nonidentifiability_interface_counterexample

// Minimal bounded model for the dev proposition:
// the same observed finite order can admit two completions that induce
// incompatible interface decisions on the shared observed copy.

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

pred isInterface[c: Completion, e: Element] {
  e in Observation.elems
  no ((e -> Element) & c.lt)
}

fact WellFormed {
  all c: Completion | strictOrder[c]

  #Observation.elems = 2

  Observation.elems in A.elems
  Observation.elems in B.elems

  A.elems & B.elems = Observation.elems

  #(A.elems - Observation.elems) = 1
  #(B.elems - Observation.elems) = 1

  (A.lt & (Observation.elems -> Observation.elems))
    =
  (B.lt & (Observation.elems -> Observation.elems))
}

pred CompletionNonIdentifiabilityWitness {
  some e: Observation.elems | isInterface[A, e] and not isInterface[B, e]
}

assert SameObservationForcesSameInterfaceDecision {
  no e: Observation.elems | isInterface[A, e] and not isInterface[B, e]
}

check SameObservationForcesSameInterfaceDecision for exactly 4 Element
