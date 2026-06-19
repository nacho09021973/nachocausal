"""nachocausal — frozen 1+1D Schwarzschild horizon RECOVERABILITY benchmark.

A recoverability benchmark (not a reconstruction claim): recovering 1+1D
Schwarzschild event-horizon structure from causal-set order alone. See
docs/preregistration.md (frozen) and docs/preregistration_001_addendum.md
(frozen thresholds).

Package layout honours the founding rule that exploration (dev/) and
confirmation (validation) are strictly separated, and that the hidden embedding
only scores — it never defines or guides the observable:

  estimator   — order-only; sees ONLY the N x N boolean poset + |C|.
  generator   — produces (poset, hidden embedding) SEPARATELY.
  scoring/    — isolated subpackage that reveals r; estimator never imports it.
  thresholds  — every frozen constant, with provenance.
  validate    — the blind benchmark runner (step #5).
  dry_run     — dev-seed confirmation of the sealed pipeline (step #4).
"""

from . import estimator, generator, thresholds  # noqa: F401

__all__ = ["estimator", "generator", "thresholds"]
