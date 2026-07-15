"""Manifest/ledger layer for the OP-2.1 reference positive certifier.

Not part of the prereg-002 evaluation path.

Owns what a stateless kernel call cannot (decision 034 §8, falsifier modes 1-2):
the frozen cell list, the alpha-budget ledger (op13:44,110-120), the one-shot
certification per cell, and the structural rejection of sequential use
(op13:141-151, SEQUENTIAL_STOPPING=FORBIDDEN — there is no append/update/incremental
entry point; streams arrive complete or not at all).
"""

from __future__ import annotations

import hashlib
import math
import time
from dataclasses import dataclass, field

import numpy as np

from certifier.kernel import Certificate, DomainError, certify_tv_lower


class LedgerError(RuntimeError):
    """Cell registration / freeze protocol violated."""


class LedgerOverdraft(LedgerError):
    """sum(alpha_j) would exceed alpha_total (op13:44)."""


class SequentialUseError(LedgerError):
    """A cell was certified more than once, or with a stream length differing from
    its registration — the sequential/peeking path is structurally rejected."""


@dataclass(frozen=True)
class CellSpec:
    cell_id: str
    m_p: int
    m_q: int
    alpha_j: float
    eps_p: float | None
    eps_q: float | None
    precision_budget: float | None = None


@dataclass
class _CellRecord:
    spec: CellSpec
    certificate: Certificate | None = None
    stream_p_sha256: str | None = None
    stream_q_sha256: str | None = None
    certified_at_unix: float | None = None


def _stream_sha256(arr: np.ndarray) -> str:
    return hashlib.sha256(np.ascontiguousarray(arr, dtype=float).tobytes()).hexdigest()


@dataclass
class CertificationLedger:
    alpha_total: float
    _cells: dict[str, _CellRecord] = field(default_factory=dict)
    _spent: float = 0.0
    _frozen: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.alpha_total, float) or not math.isfinite(self.alpha_total) \
                or not (0.0 < self.alpha_total < 1.0):
            raise LedgerError(f"alpha_total must be a float in (0,1), got {self.alpha_total!r}")

    def register_cell(
        self,
        cell_id: str,
        m_p: int,
        m_q: int,
        alpha_j: float,
        eps_p: float | None,
        eps_q: float | None,
        precision_budget: float | None = None,
    ) -> CellSpec:
        if self._frozen:
            raise LedgerError("ledger is frozen; the cell list is closed (dev prereg OP21 §3)")
        if cell_id in self._cells:
            raise LedgerError(f"cell {cell_id!r} already registered — a changed tuple is a NEW cell (op13:113-120)")
        if not (isinstance(alpha_j, float) and math.isfinite(alpha_j) and 0.0 < alpha_j < 1.0):
            raise LedgerError(f"alpha_j must be a float in (0,1), got {alpha_j!r}")
        if self._spent + alpha_j > self.alpha_total * (1.0 + 1e-12):
            raise LedgerOverdraft(
                f"registering {cell_id!r} (alpha_j={alpha_j}) overdraws the budget: "
                f"spent={self._spent}, alpha_total={self.alpha_total}"
            )
        spec = CellSpec(cell_id, int(m_p), int(m_q), alpha_j, eps_p, eps_q, precision_budget)
        self._cells[cell_id] = _CellRecord(spec=spec)
        self._spent += alpha_j
        return spec

    def freeze(self) -> None:
        if not self._cells:
            raise LedgerError("cannot freeze an empty cell list")
        self._frozen = True

    def certify_cell(self, cell_id: str, stream_p: object, stream_q: object) -> Certificate:
        if not self._frozen:
            raise LedgerError("freeze() the cell list before certifying (declare-then-run)")
        record = self._cells.get(cell_id)
        if record is None:
            raise LedgerError(f"unknown cell {cell_id!r}")
        if record.certificate is not None:
            raise SequentialUseError(
                f"cell {cell_id!r} already certified once — no second look (op13:141-151)"
            )
        p = np.asarray(stream_p, dtype=float)
        q = np.asarray(stream_q, dtype=float)
        spec = record.spec
        if p.ndim != 1 or q.ndim != 1 or p.size != spec.m_p or q.size != spec.m_q:
            raise SequentialUseError(
                f"cell {cell_id!r} expects complete streams of exactly "
                f"({spec.m_p}, {spec.m_q}) values, got ({p.size}, {q.size}) — "
                "growing or shrinking a stream is the forbidden sequential path"
            )
        certificate = certify_tv_lower(
            p, q, spec.alpha_j, spec.eps_p, spec.eps_q, spec.precision_budget
        )
        record.certificate = certificate
        record.stream_p_sha256 = _stream_sha256(p)
        record.stream_q_sha256 = _stream_sha256(q)
        record.certified_at_unix = time.time()
        return certificate

    def manifest(self) -> dict:
        """op13:135-139 ledger-side fields; the bench adds env/commit/timestamps."""
        cells = {}
        for cell_id, record in sorted(self._cells.items()):
            spec = record.spec
            cert = record.certificate
            cells[cell_id] = {
                "m_p": spec.m_p,
                "m_q": spec.m_q,
                "alpha_j": spec.alpha_j,
                "eps_p": spec.eps_p,
                "eps_q": spec.eps_q,
                "precision_budget": spec.precision_budget,
                "stream_p_sha256": record.stream_p_sha256,
                "stream_q_sha256": record.stream_q_sha256,
                "certified_at_unix": record.certified_at_unix,
                "certificate": None if cert is None else {
                    "state": cert.state,
                    "tv_lower": cert.tv_lower,
                    "r_p": cert.r_p,
                    "r_q": cert.r_q,
                    "mu_p": cert.mu_p,
                    "mu_q": cert.mu_q,
                },
            }
        return {
            "alpha_total": self.alpha_total,
            "alpha_spent": self._spent,
            "frozen": self._frozen,
            "cells": cells,
        }
