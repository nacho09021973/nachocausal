# nachocausal — sealed-instrument targets (block #4).
# Validation path is pure numpy (numpy==1.26.4). `gate` additionally needs the
# external Minz clone via NACHOCAUSAL_MINZ_PATH.

PY ?= python

.PHONY: test dry-run gate verify-seal audit verify-comite verify-audit

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
