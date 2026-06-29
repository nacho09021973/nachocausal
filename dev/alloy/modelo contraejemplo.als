module completion_maximality_check

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

assert ObservedMaximalityIsCompletionInvariant {
all e: Observation.elems |
(
no ((e -> Element) & A.lt)
iff
no ((e -> Element) & B.lt)
)
}

check ObservedMaximalityIsCompletionInvariant for exactly 4 Element



