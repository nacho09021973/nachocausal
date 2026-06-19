"""scoring — ISOLATED subpackage that reveals the hidden embedding (r).

Founding rule: the hidden embedding only SCORES; it never defines or guides the
observable. Nothing here is imported by nachocausal.estimator
(tests/test_leak.py enforces this). Callers must compute the blind boundary
threshold from O alone BEFORE invoking anything in this subpackage.
"""

from .scorer import blind_bracket  # noqa: F401

__all__ = ["blind_bracket"]
