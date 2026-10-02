# nachocausal — sealed-instrument targets (block #4).
# Sealed numeric core is pure numpy (numpy==1.26.4). The canonical test suite also
# imports support packages pinned in requirements.txt. `gate` additionally needs
# the external Minz clone via NACHOCAUSAL_MINZ_PATH.

PY ?= python

.PHONY: test dry-run gate verify-seal audit verify-comite verify-audit op21-bench op21-terminal

test:                ## bit-exact regression + leak + seed-invariant tests
	$(PY) -m pytest -q tests/

dry-run:             ## run the sealed PASS/FAIL path on DEV seeds (verdict discarded)
	$(PY) -m nachocausal.dry_run

verify-seal:         ## print the SHA256 of the frozen thresholds (compare to addendum)
	@$(PY) -c "import hashlib,pathlib; p=pathlib.Path('nachocausal/thresholds.py'); \
print('thresholds.py sha256:', hashlib.sha256(p.read_bytes()).hexdigest())"

gate:                ## re-run the Minz admissibility cross-check (needs Minz venv)
	$(PY) -c "from nachocausal import generator as g; \
print('BH gate N=', g.gate('BH')); print('MINK gate N=', g.gate('MINK')); \
print('accelerator == Minz bit-for-bit at the gated N')"

# --- OP-2.1 reference certifier (decision 034; dev prereg OP21) --------------
# Deliberately OUTSIDE `make test`: the canonical suite's semantics/runtime must
# not change (decision 034 §9 R3). MC-based tests are gated on the frozen prereg.

op21-bench:          ## OP-2.1 dev-loop suite (guards + gated MC smoke; not a terminal run)
	$(PY) -m pytest -q certifier/tests

op21-terminal:       ## the SINGLE authorized terminal-issuing bench run (dev prereg OP21 §7)
	$(PY) -m certifier.bench --terminal --out results/op21_reference_certifier_report.json

# --- integrity tooling (.claude/skills/auditor + comite) ---------------------
# No `|| true` here on purpose: a swallowed failure is exactly what `audit`
# flags, so these targets must propagate non-zero and gate.

audit:               ## heuristic integrity audit (seal drift, gitignored-but-tracked, faked results)
	bash .claude/skills/auditor/audit.sh

verify-comite:       ## validate every committee brief in docs/comite/ against the brief gate
	@found=0; fail=0; \
	for f in docs/comite/comite_decision_*.md; do \
	  [ -e "$$f" ] || continue; found=1; \
	  $(PY) .claude/skills/comite/check_comite_brief.py "$$f" || fail=1; \
	done; \
	[ "$$found" = 1 ] || echo "no committee briefs in docs/comite/ yet — nothing to verify"; \
	exit $$fail

verify-audit:        ## validate every auditor report in docs/auditor/ against the report gate
	@found=0; fail=0; \
	for f in docs/auditor/auditor_report_*.md; do \
	  [ -e "$$f" ] || continue; found=1; \
	  $(PY) .claude/skills/auditor/check_audit_report.py "$$f" || fail=1; \
	done; \
	[ "$$found" = 1 ] || echo "no auditor reports in docs/auditor/ yet — nothing to verify"; \
	exit $$fail
