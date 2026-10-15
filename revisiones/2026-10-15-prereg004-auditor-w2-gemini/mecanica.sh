#!/usr/bin/env bash
# Produce mecanica.txt for the Gemini audit of the comments-only delta 6f76d21..e6b5bfe.
set -uo pipefail
D=revisiones/2026-10-15-prereg004-auditor-w2-gemini
PY=/home/ignac/nachocausal/.venv/bin/python
{
  echo "# Salida capturada por Claude Opus 5.5 el $(date -u +%FT%TZ); el auditor no puede re-ejecutarla."
  echo "\$ git rev-parse HEAD"; git rev-parse HEAD
  echo "\$ git diff --stat 6f76d21..e6b5bfe"; git diff --stat 6f76d21..e6b5bfe
  echo "\$ make verify-seal verify-seal-004"; make -s verify-seal verify-seal-004 PY=$PY; echo "exit=$?"
  echo "\$ make test-004"; make -s test-004 PY=$PY 2>&1 | tail -1; echo "exit=${PIPESTATUS[0]}"
  echo "\$ AST of validate.py at 6f76d21 vs e6b5bfe, docstrings blanked (comments are not in the AST)"
  $PY - <<'PYEOF'
import ast, subprocess
def src(rev): return subprocess.run(["git","show",f"{rev}:nachocausal2p1/validate.py"],capture_output=True,text=True,check=True).stdout
def norm(s):
    t=ast.parse(s)
    for n in ast.walk(t):
        if isinstance(n,(ast.Module,ast.FunctionDef,ast.ClassDef)) and n.body and isinstance(n.body[0],ast.Expr) \
           and isinstance(getattr(n.body[0],"value",None),ast.Constant) and isinstance(n.body[0].value.value,str):
            n.body[0].value.value=""
    return ast.dump(t)
print("ast_equal", norm(src("6f76d21"))==norm(src("e6b5bfe")))
PYEOF
} > $D/mecanica.txt 2>&1
