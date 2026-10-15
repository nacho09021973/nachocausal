#!/usr/bin/env bash
# Produce mecanica.txt (mechanical audit outputs) and delta.diff for the Gemini delta audit.
# Run from the repo root on HEAD 616c55d. Reversible inspection only: no C1/C2/C3, no virgin seed.
set -uo pipefail
D=revisiones/2026-10-15-prereg004-auditor-delta-gemini
PY=/home/ignac/nachocausal/.venv/bin/python
git diff 782d031..616c55d -- . ':(exclude)revisiones/*/entrada_gemini.txt' \
  ':(exclude)revisiones/*/*.json' ':(exclude)revisiones/*/*.log' > $D/delta.diff
{
  echo "# Salida capturada por Claude Opus 5.5 el $(date -u +%FT%TZ); el auditor no puede re-ejecutarla."
  echo "\$ git rev-parse HEAD; git status --porcelain | wc -l"; git rev-parse HEAD; git status --porcelain | wc -l
  echo "\$ git log --oneline 782d031..HEAD"; git log --oneline 782d031..HEAD
  echo "\$ git diff --stat 782d031..HEAD"; git diff --stat 782d031..HEAD
  echo "\$ bash .claude/skills/auditor/audit.sh"; bash .claude/skills/auditor/audit.sh; echo "exit=$?"
  echo "\$ make verify-seal verify-2p1 verify-seal-004"; make -s verify-seal verify-2p1 verify-seal-004 PY=$PY; echo "exit=$?"
  echo "\$ make test-004"; make -s test-004 PY=$PY 2>&1 | tail -3; echo "exit=${PIPESTATUS[0]}"
  echo "\$ make verify-comite verify-audit"; make -s verify-comite verify-audit PY=$PY 2>&1 | sort | uniq -c; echo "exit=${PIPESTATUS[0]}"
  echo "\$ git check-ignore -v results/validation_004.json"; git check-ignore -v results/validation_004.json
  echo "\$ ls docs/preregistration_004.md docs/validation_004_seeds.json results"; ls docs/preregistration_004.md docs/validation_004_seeds.json results 2>&1
} > $D/mecanica.txt 2>&1
