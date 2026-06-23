#!/usr/bin/env bash
# Auditor — heuristic integrity audit for nachocausal (and any AI-assisted repo).
#
# Adapted from the standalone "Auditor Claude" guardrail toolkit. AI coding tools tend to *fake*
# success: they commit result files no script generates, leave CI green with no real tests, let a
# drifted instrument pass as frozen, or commit the exploration sandbox that the project swore was
# uncommitted. This script makes those patterns hard to slip past.
#
# Usage:  bash audit.sh [path-to-repo]      (defaults to the current repo)
#
# Exit codes: 0 = clean, 1 = errors found (gate CI), 2 = bad invocation.
# ERRORs are high-confidence and should gate. WARNs are heuristic (possible false positives) and
# do not fail the run. The decision/report verdict is written by the /auditor skill, not here.
set -uo pipefail

target="${1:-.}"
root="$(git -C "$target" rev-parse --show-toplevel 2>/dev/null || true)"
if [ -z "$root" ]; then
  echo "Auditor: '$target' is not inside a git repository." >&2
  exit 2
fi
cd "$root" || exit 2

echo "Auditor — auditing: $root"
echo "----------------------------------------"

errors=0
warnings=0

# 1. CI that swallows failures ------------------------------------------------
if ls .github/workflows/*.y*ml >/dev/null 2>&1; then
  hits="$(grep -nE '\|\|[[:space:]]*(true|echo)|continue-on-error:[[:space:]]*true' \
           .github/workflows/*.y*ml 2>/dev/null || true)"
  if [ -n "$hits" ]; then
    echo "ERROR: CI may be swallowing failures (|| true / || echo / continue-on-error):"
    echo "$hits" | sed 's/^/    /'
    errors=$((errors + 1))
  fi
fi

# 2. Are there any real test files? ------------------------------------------
# Only relevant if the repo actually contains application code.
appcode="$(git ls-files '*.py' '*.js' '*.jsx' '*.ts' '*.tsx' '*.go' '*.rs' \
            '*.rb' '*.java' '*.c' '*.cc' '*.cpp' '*.kt' '*.scala' 2>/dev/null | head -1)"
if [ -n "$appcode" ]; then
  testcount="$(git ls-files '*test_*.py' '*_test.py' 'tests/**' '*.test.*' '*_test.go' 2>/dev/null \
               | grep -cE '\.(py|js|ts|go|rs)$' || true)"
  if [ "${testcount:-0}" -eq 0 ]; then
    echo "ERROR: application code present but no test files found (e.g. tests/ or test_*.py)."
    errors=$((errors + 1))
  fi
else
  echo "note: no application code detected; skipping test-presence check."
fi

# 3. Seal integrity (nachocausal-specific) -----------------------------------
# The frozen instrument is the SHA256 of nachocausal/thresholds.py. The LIVE hash must appear
# verbatim in a docs/ freeze record (preregistration / seal doc). If it does not, the instrument
# has drifted from every recorded freeze — an unfrozen / tampered seal.
seal_file="nachocausal/thresholds.py"
if [ -f "$seal_file" ]; then
  live="$(python3 -c "import hashlib,pathlib;print(hashlib.sha256(pathlib.Path('$seal_file').read_bytes()).hexdigest())" 2>/dev/null || true)"
  if [ -n "$live" ]; then
    if git grep -q -- "$live" -- docs/ 2>/dev/null; then
      where="$(git grep -l -- "$live" -- docs/ 2>/dev/null | paste -sd, -)"
      echo "ok:   seal $seal_file SHA256 ${live:0:8}… is recorded in: $where"
    else
      echo "ERROR: live seal $seal_file SHA256 $live is recorded in NO docs/ freeze file —"
      echo "       the instrument has drifted from every frozen record (compare 'make verify-seal')."
      errors=$((errors + 1))
    fi
  fi
fi

# 4. gitignored-but-tracked contradiction ------------------------------------
# A path that is BOTH committed AND listed in .gitignore is an internal contradiction: the repo
# swears it is uncommitted (e.g. nachocausal's dev/ exploration sandbox, per CLAUDE.md) while
# carrying it in the tree. Generic: intersect tracked files with the ignore rules.
# --no-index: git normally refuses to call a tracked file "ignored"; this asks what the ignore
# rules say regardless of the index, which is exactly the contradiction we want to expose.
contra="$(git ls-files 2>/dev/null | git check-ignore --no-index --stdin 2>/dev/null || true)"
if [ -n "$contra" ]; then
  n="$(printf '%s\n' "$contra" | grep -c . || true)"
  echo "ERROR: $n tracked file(s) are also gitignored (committed despite being declared uncommitted):"
  printf '%s\n' "$contra" | head -20 | sed 's/^/    /'
  [ "$n" -gt 20 ] && echo "    … and $((n - 20)) more"
  errors=$((errors + 1))
fi

# 5. Committed result/data files with no generator reference -----------------
datafiles="$( { git ls-files '*.csv' '*.tsv' '*.out' '*.parquet' 2>/dev/null;
                git ls-files 'data/*' 'results/*' 'outputs/*' 2>/dev/null; } \
              | sort -u | grep -vE '\.(md|py|txt|gitkeep|json)$' || true)"
for f in $datafiles; do
  [ -z "$f" ] && continue
  base="$(basename "$f")"
  if ! git grep -q -- "$base" -- '*.py' '*.sh' '*.js' '*.ts' '*.ipynb' '*.go' '*.rs' 'Makefile' 2>/dev/null; then
    echo "WARN: committed data file with no generator reference: $f"
    warnings=$((warnings + 1))
  fi
done

echo "----------------------------------------"
echo "Auditor: ${errors} error(s), ${warnings} warning(s)"
[ "$errors" -gt 0 ] && exit 1
exit 0
