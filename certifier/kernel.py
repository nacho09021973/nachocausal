"""Fixed-sample Hoeffding kernel for the OP-2.1 reference positive certifier.

Not part of the prereg-002 evaluation path.

Implements op13 §3 (research_program/work_packages/op13_positive_evidence_protocol.md:36-81):

    r      = sqrt(log(4/alpha) / (2*m))
    TV_low = max(0, |mu_p - mu_q| - r_p - r_q - eps_p - eps_q)

The input type is the firewall (dev prereg OP21 §2): two 1-D float streams with every
value finite and in [0,1], plus scalars. No poset, no past_matrix, no coordinates, no
labels, no callables. Per decision 034 D1 this proves *module-level* geometry-blindness
only — never end-to-end stream provenance.

The kernel is pure and stateless: it cannot own multiplicity or stopping discipline.
Those live in `certifier.ledger` (a stateless guard here would be decoration).
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


class DomainError(ValueError):
    """Raised when an input violates the [0,1]-stream / scalar contract."""


STATE_BOUND_POSITIVE = "BOUND_POSITIVE"
STATE_ZERO_BOUND = "ZERO_BOUND"
STATE_ABSTAIN_PRECISION = "ABSTAIN_PRECISION"
STATE_ABSTAIN_GENERATOR_ERROR = "ABSTAIN_GENERATOR_ERROR"


@dataclass(frozen=True)
class Certificate:
    state: str
    tv_lower: float | None  # None on any abstention — an abstention reports no bound
    r_p: float
    r_q: float
    mu_p: float
    mu_q: float
    m_p: int
    m_q: int
    alpha: float
    eps_p: float | None
    eps_q: float | None


def hoeffding_radius(m: int, alpha: float) -> float:
    """Two-sided Hoeffding radius for a [0,1] mean of m IID samples (op13:59-62)."""
    if isinstance(m, bool) or not isinstance(m, (int, np.integer)) or m < 1:
        raise DomainError(f"m must be a positive integer, got {m!r}")
    if not isinstance(alpha, (int, float)) or isinstance(alpha, bool):
        raise DomainError(f"alpha must be a float in (0,1), got {alpha!r}")
    if not (0.0 < alpha < 1.0):
        raise DomainError(f"alpha must lie in (0,1), got {alpha!r}")
    return math.sqrt(math.log(4.0 / alpha) / (2.0 * m))


def _validated_stream(stream: object, name: str) -> np.ndarray:
    arr = np.asarray(stream, dtype=float)
    if arr.ndim != 1 or arr.size == 0:
        raise DomainError(f"{name} must be a non-empty 1-D array")
    if not np.all(np.isfinite(arr)):
        raise DomainError(f"{name} contains non-finite values")
    if float(arr.min()) < 0.0 or float(arr.max()) > 1.0:
        raise DomainError(f"{name} leaves [0,1]")
    return arr


def _is_certified_eps(eps: object) -> bool:
    """A generator-error bound must be an explicit finite float >= 0 (op13:122-133).

    None / NaN / negative / non-numeric means the caller holds no certified bound:
    mandatory abstention, never a silent eps=0.
    """
    if isinstance(eps, bool) or not isinstance(eps, (int, float, np.floating, np.integer)):
        return False
    return math.isfinite(float(eps)) and float(eps) >= 0.0


def _eps_term(eps_p: float, eps_q: float) -> float:
    """Designated mutation point MUT-B (dev prereg OP21 §5 C4)."""
    return eps_p + eps_q


def certify_tv_lower(
    stream_p: object,
    stream_q: object,
    alpha: float,
    eps_p: float | None,
    eps_q: float | None,
    precision_budget: float | None = None,
) -> Certificate:
    """One fixed-sample, one-sided TV lower-bound certificate (op13 §3).

    Coverage (>= 1 - alpha for this single cell) holds only under the ledger's
    multiplicity budget and with certified eps bounds; this function alone certifies
    nothing about a set of calls.
    """
    p = _validated_stream(stream_p, "stream_p")
    q = _validated_stream(stream_q, "stream_q")
    m_p, m_q = int(p.size), int(q.size)
    r_p = hoeffding_radius(m_p, alpha)
    r_q = hoeffding_radius(m_q, alpha)
    mu_p = float(p.mean())
    mu_q = float(q.mean())

    if not (_is_certified_eps(eps_p) and _is_certified_eps(eps_q)):
        return Certificate(
            STATE_ABSTAIN_GENERATOR_ERROR, None, r_p, r_q, mu_p, mu_q,
            m_p, m_q, alpha, None, None,
        )

    eps_p_f, eps_q_f = float(eps_p), float(eps_q)
    total_slack = r_p + r_q + _eps_term(eps_p_f, eps_q_f)

    if precision_budget is not None:
        if not isinstance(precision_budget, (int, float)) or isinstance(precision_budget, bool) \
                or not math.isfinite(precision_budget) or precision_budget <= 0.0:
            raise DomainError(f"precision_budget must be a finite float > 0, got {precision_budget!r}")
        if total_slack > precision_budget:
            return Certificate(
                STATE_ABSTAIN_PRECISION, None, r_p, r_q, mu_p, mu_q,
                m_p, m_q, alpha, eps_p_f, eps_q_f,
            )

    tv_lower = max(0.0, abs(mu_p - mu_q) - total_slack)
    state = STATE_BOUND_POSITIVE if tv_lower > 0.0 else STATE_ZERO_BOUND
    return Certificate(
        state, tv_lower, r_p, r_q, mu_p, mu_q, m_p, m_q, alpha, eps_p_f, eps_q_f,
    )
