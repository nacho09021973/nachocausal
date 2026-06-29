module poset_smoke

sig Element {
  lt: set Element
}

fact StrictPartialOrder {
  // Irreflexividad
  no e: Element | e->e in lt

  // Transitividad
  lt.lt in lt
}

pred NonTrivialExample {
  some lt
}

run NonTrivialExample for exactly 4 Element
