# nachocausal

Research repository for causal-set recoverability, order-and-counting observables, and the current normalized-channel / physical-reentry program.

> **PORTABLE HANDOFF — 2026-08-28**
>
> This branch is a migration snapshot for resuming work from another computer. It is **not** a scientific seal, preregistration, novelty certificate, or merge decision.
>
> Branch: `handoff/portable-2026-08-28`
>
> Verified remote base: `d99f153b1ffe4e88e89ccb58852335bc2a1fe5a4` (`agent/nc2fb-lemma-2-1-lean`, 2026-08-21).
>
> The default branch `main` is older (`256d9e76fbed186463770af666602f8e592debcc`, 2026-08-16). Do **not** infer current scientific state from `main` alone.

## Start here on a new computer

```bash
git clone https://github.com/nacho09021973/nachocausal.git
cd nachocausal
git fetch --all --tags --prune
git switch handoff/portable-2026-08-28
```

Then read, in this order:

1. `INSTRUCCIONES.md` — repository workflow and governance.
2. `docs/hoja_de_ruta_agosto_2026.md` — current operational roadmap.
3. `docs/handoff_2026-08-28_remote_migration.md` — exact migration status and what is / is not yet on GitHub.
4. `docs/status_note_2026-08-21_normalized_theorem_ledger.md` — latest theorem ledger present in the verified remote base.
5. `docs/program_reopening_note_2026-08-18_nc2f_variance_exponent_reduction.md` and `emergencia/P1a_count_volume_rectangular_discrepancy_l2_d2.md` — NC-2F reduction and audited discrepancy layer.
6. `formal/HorizonFormal/` — Lean formalization already present in the remote snapshot.

## Scientific status represented by the verified remote base

The remote snapshot contains the normalized-channel reopening through NC-2F, the audited rectangular-discrepancy layer, the associated Lean formalization, and the selection-mass stress-test machinery. In particular, `main` is not the right reference point for this work; the relevant remote history is on the later `agent/*` and `ci/*` branches.

The repository distinguishes strictly between:

- **proved / audited statements** backed by committed files,
- **exploratory or stress-test evidence**,
- **working-state conclusions reported during later local sessions but not yet backed by a remote commit**.

That distinction is especially important during this migration.

## Migration caveat: later local work

Work performed after the verified remote base exists on the old workstation and is **not certified as uploaded merely by this handoff branch**. The later working state includes the completed selection-mass continuation and the physical-reentry audit in which:

```text
MOVING_SUPPORT_QMD_STATUS = OPEN
FIRST_PHYSICAL_OBSTACLE = DOMAIN_BRIDGE
PHYSICAL_REENTRY = PARTIAL_TRANSPORT_WITH_EXACT_FIRST_OBLIGATION
```

These tokens are recorded here only as a **working-session handoff**. They become repository evidence only when the corresponding local commits/files are pushed and can be inspected on GitHub.

Do not recreate missing files from memory if the old workstation still has them. Push the original commits/files instead.

## Current program discipline

- Physical consistency and exact domain statements take priority over better-looking metrics.
- Exploration and confirmation remain distinct.
- Do not promote a local-session conclusion to `PROVED` without the committed proof/audit trail.
- Reuse existing scripts, runs, and formal files before creating new machinery.
- The immediate technical bottleneck is the **domain bridge** for physical reentry; moving-support QMD remains open, not established.

## Historical material

Older program material remains in the repository and in Git history. Important historical entry points include:

- `docs/manuscript_limits_draft.md`
- `tarea_grok_2.md`
- `docs/backlog_hallazgos.md`
- `research_program/`
- `emergencia/`

Those files remain valuable provenance, but some of their operational handoffs have been superseded by the August 2026 normalized-channel reopening and by the migration roadmap above.
