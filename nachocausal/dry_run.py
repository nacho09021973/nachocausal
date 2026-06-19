"""dry_run — block #4 confirmation that the SEALED pipeline runs end-to-end.

Runs the full frozen validate.run() PASS/FAIL code path on DEV_SEEDS ONLY
(numpy 1.26.4, no Minz). The dev verdict is DISCARDED — its purpose is to prove
the analysis code is runnable and the frozen thresholds are computable BEFORE
any validation seed exists. It imports the frozen thresholds.py constants and
asserts NOTHING bespoke (cmte adversarial M3/m4): a regression here is a finding,
not a licence to retune.

Run: python -m nachocausal.dry_run   (or: make dry-run)
"""

from __future__ import annotations

from . import thresholds, validate


def main() -> None:
    thresholds.assert_environment()
    print("=" * 78)
    print("nachocausal SEALED-PIPELINE DRY RUN (dev seeds only; verdict DISCARDED)")
    print(f"  numpy pinned = {thresholds.PINNED_NUMPY}")
    print(f"  dev seeds = {thresholds.DEV_SEEDS}")
    print(f"  intensities = {thresholds.INTENSITIES}  ensemble would be "
          f"{thresholds.ENSEMBLE} at validation (dev uses {len(thresholds.DEV_SEEDS)})")
    print("=" * 78)

    # MIN_VALID_SEEDS (18) is a validation-ensemble gate; dev has only 8 seeds,
    # so we exercise the SAME code path with a dev-sized validity floor. This is
    # purely to run the machinery; no threshold value is changed.
    saved = thresholds.MIN_VALID_SEEDS
    thresholds.MIN_VALID_SEEDS = max(3, len(thresholds.DEV_SEEDS) - 2)
    try:
        verdict = validate.run(
            seeds=thresholds.DEV_SEEDS, label="dev_dryrun", guard=True, write=True
        )
    finally:
        thresholds.MIN_VALID_SEEDS = saved

    hdr = (f"{'intensity':>9} {'N':>6} {'n_ok':>4} {'p_perm':>9} {'sig':>4} "
           f"{'med|dr|/2M':>10} {'θ_loc':>6} {'loc':>4} {'cov':>4} "
           f"{'r_std':>6} {'θ_stab':>6} {'stab':>4} {'fp':>5} {'fp_ok':>5}")
    print(hdr)
    for lam in thresholds.INTENSITIES:
        L = verdict["levels"][lam]
        if L.get("status") != "scored":
            print(f"{lam:>9.0f} {L['N_mean']:>6.0f} {L['n_valid']:>4} "
                  f"{'INCONCLUSIVE':>50}")
            continue
        print(f"{lam:>9.0f} {L['N_mean']:>6.0f} {L['n_valid']:>4} "
              f"{L['p_perm']:>9.2e} {str(L['significant']):>4} "
              f"{L['median_width_over_2M']:>10.3f} {L['theta_loc']:>6.3f} "
              f"{str(L['loc_pass']):>4} {L['coverage_frac']:>4.2f} "
              f"{L['boundary_r_std']:>6.3f} {L['theta_stab']:>6.3f} "
              f"{str(L['stab_pass']):>4} {L['fp_fraction']:>5.2f} "
              f"{str(L['fp_pass']):>5}")
    print("-" * len(hdr))
    print(f"  dev verdict (DISCARDED): {verdict.get('verdict')}  "
          f"checks={verdict.get('checks', verdict.get('reason'))}")
    print("  Purpose: prove the sealed PASS/FAIL path RUNS and the frozen "
          "thresholds COMPUTE. Not a result.")
    print("  Guard-v raised on no causet -> O is order-only on every dev causet.")


if __name__ == "__main__":
    main()
