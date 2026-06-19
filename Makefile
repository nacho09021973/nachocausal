# nachocausal — sealed-instrument targets (block #4).
# Validation path is pure numpy (numpy==1.26.4). `gate` additionally needs the
# external Minz clone via NACHOCAUSAL_MINZ_PATH.

PY ?= python

.PHONY: test dry-run gate verify-seal

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
