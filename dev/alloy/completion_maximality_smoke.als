module completion_maximality_smoke

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

// Las completaciones solo comparten el subposet observado.
A.elems & B.elems = Observation.elems

// Cada completación añade exactamente un elemento distinto.
#(A.elems - Observation.elems) = 1
#(B.elems - Observation.elems) = 1

// El orden inducido sobre C es idéntico.
(A.lt & (Observation.elems -> Observation.elems))
=
(B.lt & (Observation.elems -> Observation.elems))
}

pred CompletionChangesMaximality {
some e: Observation.elems |
no ((e -> Element) & A.lt)
and
some ((e -> Element) & B.lt)
}

run CompletionChangesMaximality for exactly 4 Element


