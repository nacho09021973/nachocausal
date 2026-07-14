# PR009 Ladder-Ensemble Effective-Expansion Closure Decision

STATUS: CLOSED
TERMINAL_LABEL: FAILED_DATA_CONTRACT
SCOPE: CONTRACT_CLOSURE / NO_SCIENTIFIC_TERMINAL / NO_RERUN
SEALED_IMPLEMENTATION_SHA: 489f560f2cbe0cc92671b06574dc48b04d432968

## Decision

Close PR009 at the reference data-contract gate.

```text
PR009 terminated before publication because reference-MINK coverage at
depth 7 was below the preregistered minimum. No scientific terminal result
was produced and no inference about horizon sensitivity is permitted.
```

PR009 is neither a dead observable nor a surviving observable. The frozen run did not
reach evaluation or scoring, so none of the preregistered scientific terminal labels
applies.

## Execution Record

The implementation commit was sealed and pushed at:

```text
489f560f2cbe0cc92671b06574dc48b04d432968
```

The authorized production sequence stopped during the first command:

```text
python3 dev/run_pr009_effective_expansion.py --block REFERENCE
```

The runner raised:

```text
DataContractError: insufficient reference-MINK rows at depth 7
```

The failure occurred before atomic publication. No PR009 reference, evaluation,
canonical, truth, scored, report, sidecar, or temporary production artifact exists.
The evaluation command and scorer were not executed.

## Scientific Boundary

The only admissible conclusion is that the frozen PR009 design did not supply the
preregistered reference-MINK coverage needed to define its depth baseline through the
required range.

This closure does not establish:

- absence or presence of horizon sensitivity;
- failure or survival of the effective-expansion observable;
- a null or negative physical result;
- any contrast, permutation result, coverage terminal, or scorer label.

No internal, unpublished PR009 values may be inspected, summarized, reused, or used to
choose a successor design.

## Forbidden Repairs Inside PR009

PR009 is closed without amendment. It is forbidden to:

- reduce the minimum of 12 reference-MINK rows;
- remove depth 7 or change the scored depth range;
- add or replace seeds;
- change `MAX_DEPTH`;
- repeat the reference block;
- publish the report reserved to the scorer;
- tune any parameter or threshold in response to the failed run.

Any such action would be post-run adaptation of the frozen protocol.

## Operational Interpretation

The enclosing-diamond separation optimization resolved the computational bottleneck.
PR009 nevertheless failed at a distinct statistical-design boundary: evaluable
reference-MINK transition coverage at depth.

Future work must redesign coverage under a new phase and new data. It must not reopen
PR009 or reinterpret this contract failure as scientific evidence.

## Next Phase

Open PR010 as a separate coverage-design phase under
`dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md`.
