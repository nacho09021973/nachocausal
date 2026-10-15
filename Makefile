# nachocausal — sealed-instrument targets (block #4).
# Sealed numeric core is pure numpy (numpy==1.26.4). The canonical test suite also
# imports support packages pinned in requirements.txt. `gate` additionally needs
# the external Minz clone via NACHOCAUSAL_MINZ_PATH.

PY ?= python

.PHONY: test dry-run gate verify-seal verify-2p1 test-004 dry-run-004 verify-seal-004 audit verify-comite verify-audit op21-bench op21-terminal

test:                ## bit-exact regression + leak + seed-invariant tests
	$(PY) -m pytest -q tests/

dry-run:             ## run the sealed PASS/FAIL path on DEV seeds (verdict discarded)
	$(PY) -m nachocausal.dry_run

verify-seal:         ## print the SHA256 of the frozen thresholds (compare to addendum)
	@$(PY) -c "import hashlib,pathlib; p=pathlib.Path('nachocausal/thresholds.py'); \
print('thresholds.py sha256:', hashlib.sha256(p.read_bytes()).hexdigest())"

verify-2p1:          ## SHA256 of the 2+1 CANDIDATE thresholds and tau fixture (not a seal yet)
	@$(PY) -c "import hashlib,pathlib; [print(p, hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()) \
for p in ('nachocausal2p1/thresholds.py','nachocausal2p1/fixtures/tau_table_2p1.json')]"

# --- prereg-004 (2+1) pre-flight targets (comité 052 §9, comité 053 §8 item 6) ----------
test-004:            ## the three prereg-004 test files (seed manifest, package, can-fail)
	$(PY) -m pytest -q tests/test_004_seed_manifest.py tests/test_2p1_package.py tests/test_004_criteria_can_fail.py

dry-run-004:         ## 2+1 MECHANICS-ONLY dry run: off-grid rho, burned seeds, no widths, not a result
	$(PY) -m nachocausal2p1.dry_run

verify-seal-004:     ## SHA256 of every file sealed at C1 for prereg-004 (2+1 package + imported 1+1 files)
	@sha256sum nachocausal/thresholds.py nachocausal/__init__.py nachocausal/estimator.py \
	  nachocausal/generator.py nachocausal2p1/*.py nachocausal2p1/scoring/*.py \
	  nachocausal2p1/fixtures/tau_table_2p1.json

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
