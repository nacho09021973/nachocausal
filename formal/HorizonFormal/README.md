# HorizonFormal

Lean-first formalisation track for the order-theoretic core of NACHOCAUSAL.

This project deliberately starts below the Schwarzschild/GKP/sprinkling layer:
posets, ideals, non-principal ideal ends, accessibility, and the relational
horizon interface. It is a small Lean 4 + mathlib library intended to formalise
the algebraic lemmas before they are used as physical scaffolding.

## Dependencies

- Lean toolchain: pinned in `lean-toolchain`.
- mathlib revision: pinned in `lakefile.toml` and `lake-manifest.json`.
- Build system: Lake, installed with Lean through `elan`.

Install Lean/elan once if needed:

```bash
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | \
  sh -s -- -y --default-toolchain leanprover/lean4:v4.31.0
. "$HOME/.elan/env"
```

Build from this directory:

```bash
lake update
lake build
```

The `.lake/` directory is a local build cache and is not committed.

## Module Order

- `HorizonFormal.Posets`
- `HorizonFormal.Ideals`
- `HorizonFormal.CofinalChains`
- `HorizonFormal.Ends`
- `HorizonFormal.ChainEnds`
- `HorizonFormal.Accessibility`
- `HorizonFormal.Horizon`
