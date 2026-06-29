# Alloy verification 002 — Completion Nonidentifiability Interface Counterexample

> Produced by `/alloy-verifier`. Bounded model checking over an explicit Alloy translation of a
> claim. This is evidence about the encoded model at the checked finite scope, not a general proof
> of the underlying scientific statement.

## 1. Question

Stress-test a minimal formal version of the dev proposition in
`dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md`: can the same observed finite order admit
two completions that induce incompatible interface decisions on the shared observed subposet?

## 2. Model under test

- Model file(s): `formal/alloy/completion_nonidentifiability_interface_counterexample.als`
- Assertion / predicate / command: `check SameObservationForcesSameInterfaceDecision`
- Requested scope: `for exactly 4 Element`
- Translation status: committed model

## 3. Tooling status

- Verified Alloy command: `/home/adnac/.local/bin/alloy exec`
- Command found locally: yes
- Execution status: executed successfully; Alloy produced a bounded counterexample trace

## 4. Exact run record

```text
/home/adnac/.local/bin/alloy exec -o - -t text /home/adnac/nachocausal/formal/alloy/completion_nonidentifiability_interface_counterexample.als
```

Exit code: `0`

### stdout

```text
---Trace---
------State 0 (loop)-------
univ={Element$0, Element$1, Element$2, Element$3, Observation$0, A$0, B$0, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7}
Int={-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7}
seq/Int={0, 1, 2, 3}
String={}
none={}
this/Element={Element$0, Element$1, Element$2, Element$3}
this/Observation={Observation$0}
this/Observation<:elems={Observation$0->Element$2, Observation$0->Element$3}
this/A={A$0}
this/B={B$0}
this/Completion={A$0, B$0}
this/Completion<:elems={A$0->Element$1, A$0->Element$2, A$0->Element$3, B$0->Element$0, B$0->Element$2, B$0->Element$3}
this/Completion<:lt={A$0->Element$2->Element$1, A$0->Element$2->Element$3, A$0->Element$3->Element$1, B$0->Element$0->Element$3, B$0->Element$2->Element$0, B$0->Element$2->Element$3}
skolem $SameObservationForcesSameInterfaceDecision_e={Element$3}
```

### stderr

```text

```

## 5. Findings

- A bounded counterexample exists at scope `exactly 4 Element`.
- The two completions agree on the observed subposet and differ only by one hidden element each.
- In the returned witness, the observed element skolemized as `Element$3` is an interface element in
  completion `A` but not in completion `B`.
- Therefore the encoded implication "same observed finite order forces the same interface decision"
  is false in this bounded model.

## 6. Scope limits

- This is a minimal logical witness, not a full formalization of the physical completion class in
  PR-003.
- The model does not yet encode Schwarzschild, Hayward, matched flat controls, or a geometric
  notion of admissibility.
- So the result supports only the narrow claim that completion-based incompatibility is consistent
  with a small explicit finite model; it does not settle the full committee question by itself.

## 7. Verdict

ALLOY_VERDICT=ALLOY_COUNTEREXAMPLE_FOUND

## 8. Next step

Refine the completion class explicitly if you want the next Alloy model to distinguish merely
logical completions from the physically admissible completions relevant to PR-003.
