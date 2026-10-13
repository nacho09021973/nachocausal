"""scoring — ISOLATED subpackage that reveals the hidden radius r (2+1 bench).

The hidden embedding only SCORES; it never defines or guides the observable. Nothing here is
imported by nachocausal2p1.estimator or nachocausal2p1.gate (tests/test_2p1_package.py).
Callers must freeze the blind threshold from O alone BEFORE calling anything here.
"""

from .scorer import blind_bracket  # noqa: F401

__all__ = ["blind_bracket"]
