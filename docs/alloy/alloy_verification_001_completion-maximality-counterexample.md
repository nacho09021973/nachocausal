# Alloy verification 001 — Completion Maximality Counterexample

> Produced by `/alloy-verifier`. Bounded model checking over an explicit Alloy translation of a
> claim. This is evidence about the encoded model at the checked finite scope, not a general proof
> of the underlying scientific statement.

## 1. Question

Check whether the claim "observed maximality is invariant across completions that agree on the
observed subposet" survives bounded Alloy verification once the claim is translated into an
explicit finite relational model.

## 2. Model under test

- Model file(s): `formal/alloy/completion_maximality_invariance_counterexample.als`
- Assertion / predicate / command: `check ObservedMaximalityIsCompletionInvariant`
- Requested scope: `for exactly 4 Element`
- Translation status: committed model

## 3. Tooling status

- Verified Alloy command: `/home/adnac/.local/bin/alloy exec`
- Command found locally: yes
- Execution status: executed successfully; Alloy produced a bounded counterexample trace

## 4. Exact run record

```text
/home/adnac/.local/bin/alloy exec -o - -t text /home/adnac/nachocausal/formal/alloy/completion_maximality_invariance_counterexample.als
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
skolem $ObservedMaximalityIsCompletionInvariant_e={Element$3}
```

### stderr

```text

```

## 5. Findings

- A bounded counterexample exists at scope `exactly 4 Element`.
- In the returned witness, the observed fragment is the same in completions `A` and `B`, but the
  observed element skolemized as `Element$3` does not preserve maximality across the two
  completions.
- Therefore the encoded assertion `ObservedMaximalityIsCompletionInvariant` is false in this model.

## 6. Scope limits

- This result is bounded to the encoded finite model and the checked scope `exactly 4 Element`.
- It does not prove the strongest possible general impossibility statement; it only shows that the
  encoded invariance claim already fails in one small finite witness.
- It does not by itself certify that the model is the right translation of any larger scientific
  claim; translation fidelity still needs human review.

## 7. Verdict

ALLOY_VERDICT=ALLOY_COUNTEREXAMPLE_FOUND

## 8. Next step

Decide whether this bounded counterexample should become a supporting formal objection in a dev note
or committee dossier, keeping the claim boundary explicitly tied to the encoded model.
