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
provenance_registry="provenance/committed_artifact_generators.tsv"
provenance_header=$'artifact_path\tgenerator_path\tcommand_or_template\tprovenance_anchor'
registry_usable=1
if [ -e "$provenance_registry" ]; then
  registry_first_line="$(head -n 1 "$provenance_registry" 2>/dev/null || true)"
  if [ "$registry_first_line" != "$provenance_header" ]; then
    echo "ERROR: provenance registry has an invalid header: $provenance_registry"
    errors=$((errors + 1))
    registry_usable=0
  fi
fi

datafiles="$( { git ls-files '*.csv' '*.tsv' '*.out' '*.parquet' 2>/dev/null;
                git ls-files 'data/*' 'results/*' 'outputs/*' 2>/dev/null; } \
              | sort -u | grep -vE '\.(md|py|txt|gitkeep|json)$' || true)"
# A path may satisfy the historical literal-reference fallback only if it can
# plausibly BE a generator. Documentation, audit tooling, provenance metadata and
# tests are not generators: a filename mentioned only there is no evidence that
# anything produces the artifact. Auditor report 040 recorded the concrete failure
# this guard closes — a test file listing the 23 historical basenames silenced all
# 23 provenance warnings without the registry ever being consulted.
is_generator_candidate() {
  case "$1" in
    tests/*|*/tests/*) return 1 ;;
    test/*|*/test/*) return 1 ;;
    mytests/*|*/mytests/*) return 1 ;;
    .claude/*|*/.claude/*) return 1 ;;
    docs/*|*/docs/*) return 1 ;;
    provenance/*|*/provenance/*) return 1 ;;
  esac
  case "$(basename "$1")" in
    conftest.py|test_*|*_test|*_test.*) return 1 ;;
  esac
  return 0
}

for f in $datafiles; do
  [ -z "$f" ] && continue
  # This TSV is audit metadata, not a generated result/data artifact.
  [ "$f" = "$provenance_registry" ] && continue
  base="$(basename "$f")"

  # (A) Registry first. A declared provenance row is authoritative and is never
  #     eclipsed by a literal filename match: if a row exists it must fully
  #     validate, or the artifact is an ERROR.
  registry_rows=""
  registry_count=0
  if [ -e "$provenance_registry" ] && [ "$registry_usable" -eq 1 ]; then
    registry_rows="$(awk -F '\t' -v artifact="$f" 'NR > 1 && $1 == artifact { print }' \
                      "$provenance_registry" 2>/dev/null || true)"
    registry_count="$(printf '%s\n' "$registry_rows" | grep -c . || true)"
    registry_count="${registry_count:-0}"
  fi

  if [ "$registry_count" -gt 1 ]; then
    echo "ERROR: provenance inconsistency for $f: expected exactly one registry row, found $registry_count"
    errors=$((errors + 1))
    continue
  fi

  if [ "$registry_count" -eq 1 ]; then
    registry_field_count="$(printf '%s\n' "$registry_rows" | awk -F '\t' '{ print NF }')"
    IFS=$'\t' read -r registry_artifact generator_path command_or_template provenance_anchor \
      <<< "$registry_rows"
    if [ "$registry_field_count" -ne 4 ] || [ -z "$registry_artifact" ] || \
       [ -z "$generator_path" ] || [ -z "$command_or_template" ] || \
       [ -z "$provenance_anchor" ]; then
      echo "ERROR: provenance inconsistency for $f: registry row must contain four non-empty tab-separated fields"
      errors=$((errors + 1))
      continue
    fi
    if [ ! -f "$generator_path" ] || \
       ! git ls-files --error-unmatch -- "$generator_path" >/dev/null 2>&1; then
      echo "ERROR: provenance inconsistency for $f: generator is missing or untracked: $generator_path"
      errors=$((errors + 1))
      continue
    fi

    case "$provenance_anchor" in
      git:*)
        anchor_commit="${provenance_anchor#git:}"
        if ! printf '%s\n' "$anchor_commit" | grep -Eq '^[0-9a-fA-F]{40}$' || \
           ! git cat-file -e "${anchor_commit}^{commit}" 2>/dev/null; then
          echo "ERROR: provenance inconsistency for $f: invalid git commit anchor: $provenance_anchor"
          errors=$((errors + 1))
          continue
        fi
        if ! git diff-tree --root --no-commit-id --name-only -r "$anchor_commit" -- "$f" \
             2>/dev/null | grep -Fxq -- "$f"; then
          echo "ERROR: provenance inconsistency for $f: anchor commit does not introduce or modify the artifact: $provenance_anchor"
          errors=$((errors + 1))
          continue
        fi
        ;;
      *)
        echo "ERROR: provenance inconsistency for $f: unsupported provenance anchor: $provenance_anchor"
        errors=$((errors + 1))
        continue
        ;;
    esac

    # Registry row present and fully validated: provenance is established.
    continue
  fi

  # (B) No registry row for this artifact: fall back to the historical literal
  #     reference, but only when the reference lives in genuine generator code.
  candidates="$(git grep -l -- "$base" \
                  -- '*.py' '*.sh' '*.js' '*.ts' '*.ipynb' '*.go' '*.rs' 'Makefile' \
                  2>/dev/null || true)"
  resolved=0
  if [ -n "$candidates" ]; then
    while IFS= read -r cand; do
      [ -z "$cand" ] && continue
      if is_generator_candidate "$cand"; then
        resolved=1
        break
      fi
    done <<< "$candidates"
  fi
  [ "$resolved" -eq 1 ] && continue

  echo "WARN: committed data file with no generator reference: $f"
  warnings=$((warnings + 1))
done

echo "----------------------------------------"
echo "Auditor: ${errors} error(s), ${warnings} warning(s)"
[ "$errors" -gt 0 ] && exit 1
exit 0
