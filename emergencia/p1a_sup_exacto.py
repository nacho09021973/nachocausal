#!/usr/bin/env python3
"""Certified supremum of an integer polynomial on the open interval (0,1).

Used only for the DESCRIPTIVE magnitude D_X of
``emergencia/P1a_contrato_falsador_paso7_d2.md`` §5.  It never adjudicates a verdict.

The method is exact where exactness matters and certified where it cannot be exact:

1. the polynomial is carried in the monomial basis with ``Fraction`` coefficients,
   built exactly from the integer Bernstein coefficients;
2. its critical points are isolated by a Sturm sequence of the squarefree part of the
   derivative, evaluated in exact rational arithmetic, so the ROOT COUNT in every
   interval is certified, never estimated;
3. each isolated root is bisected in exact rational arithmetic to a width below a
   requested bound, and the supremum is returned as a certified enclosure
   ``[low, high]`` whose width accounts for the residual bracket via an exact
   Lipschitz bound on the derivative.

No floating point enters any decision; floats appear only in the reported value.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb
from typing import Sequence

Poly = tuple[Fraction, ...]  # coefficient i multiplies x**i


def _trim(coefficients: Sequence[Fraction]) -> Poly:
    values = list(coefficients)
    while values and values[-1] == 0:
        values.pop()
    return tuple(values)


def is_zero(poly: Poly) -> bool:
    return not poly


def degree(poly: Poly) -> int:
    return len(poly) - 1


def evaluate(poly: Poly, x: Fraction) -> Fraction:
    total = Fraction(0)
    for coefficient in reversed(poly):
        total = total * x + coefficient
    return total


def derivative(poly: Poly) -> Poly:
    return _trim([coefficient * index for index, coefficient in enumerate(poly)][1:])


def _sub(left: Poly, right: Poly) -> Poly:
    size = max(len(left), len(right))
    return _trim(
        [
            (left[i] if i < len(left) else Fraction(0))
            - (right[i] if i < len(right) else Fraction(0))
            for i in range(size)
        ]
    )


def _shift_scale(poly: Poly, shift: int, factor: Fraction) -> Poly:
    return _trim([Fraction(0)] * shift + [coefficient * factor for coefficient in poly])


def _remainder(numerator: Poly, denominator: Poly) -> Poly:
    if is_zero(denominator):
        raise ZeroDivisionError("polynomial division by zero")
    remainder = numerator
    while not is_zero(remainder) and degree(remainder) >= degree(denominator):
        factor = remainder[-1] / denominator[-1]
        shift = degree(remainder) - degree(denominator)
        remainder = _sub(remainder, _shift_scale(denominator, shift, factor))
    return remainder


def _gcd(left: Poly, right: Poly) -> Poly:
    a, b = left, right
    while not is_zero(b):
        a, b = b, _remainder(a, b)
    if is_zero(a):
        return a
    return _trim([coefficient / a[-1] for coefficient in a])


def _quotient(numerator: Poly, denominator: Poly) -> Poly:
    quotient = [Fraction(0)] * max(degree(numerator) - degree(denominator) + 1, 1)
    remainder = numerator
    while not is_zero(remainder) and degree(remainder) >= degree(denominator):
        factor = remainder[-1] / denominator[-1]
        shift = degree(remainder) - degree(denominator)
        quotient[shift] = factor
        remainder = _sub(remainder, _shift_scale(denominator, shift, factor))
    return _trim(quotient)


def squarefree(poly: Poly) -> Poly:
    if degree(poly) < 1:
        return poly
    common = _gcd(poly, derivative(poly))
    if degree(common) < 1:
        return poly
    return _quotient(poly, common)


def sturm_sequence(poly: Poly) -> list[Poly]:
    base = squarefree(poly)
    if degree(base) < 1:
        return [base]
    sequence = [base, derivative(base)]
    while degree(sequence[-1]) > 0:
        remainder = _remainder(sequence[-2], sequence[-1])
        if is_zero(remainder):
            break
        sequence.append(_trim([-coefficient for coefficient in remainder]))
    return sequence


def _sign_changes(sequence: Sequence[Poly], x: Fraction) -> int:
    signs = []
    for poly in sequence:
        value = evaluate(poly, x)
        if value != 0:
            signs.append(1 if value > 0 else -1)
    return sum(1 for i in range(len(signs) - 1) if signs[i] != signs[i + 1])


def count_roots(sequence: Sequence[Poly], low: Fraction, high: Fraction) -> int:
    """Number of distinct real roots in the half-open interval (low, high]."""

    return _sign_changes(sequence, low) - _sign_changes(sequence, high)


def isolate_roots(
    poly: Poly, low: Fraction, high: Fraction, *, width: Fraction
) -> list[tuple[Fraction, Fraction]]:
    """Brackets of width <= `width`, each containing exactly one distinct root."""

    if degree(poly) < 1:
        return []
    sequence = sturm_sequence(poly)
    if degree(sequence[0]) < 1:
        return []
    if count_roots(sequence, low, high) == 0:
        return []

    pending = [(low, high)]
    isolated: list[tuple[Fraction, Fraction]] = []
    while pending:
        left, right = pending.pop()
        total = count_roots(sequence, left, right)
        if total == 0:
            continue
        if total == 1 and right - left <= width:
            isolated.append((left, right))
            continue
        middle = (left + right) / 2
        if middle == left or middle == right:
            isolated.append((left, right))
            continue
        pending.append((left, middle))
        pending.append((middle, right))
    return sorted(isolated)


def bernstein_to_monomial(coefficients: Sequence[int], n: int) -> Poly:
    """Exact expansion of sum_k c_k p^k (1-p)^(n-k) into the monomial basis."""

    if len(coefficients) != n + 1:
        raise ValueError("expected one Bernstein coefficient per degree 0..n")
    monomial = [Fraction(0)] * (n + 1)
    for k, coefficient in enumerate(coefficients):
        if coefficient == 0:
            continue
        # p^k (1-p)^(n-k) = sum_j C(n-k, j) (-1)^j p^(k+j)
        for j in range(n - k + 1):
            monomial[k + j] += Fraction(coefficient * comb(n - k, j) * (-1) ** j)
    return _trim(monomial)


def supremum_on_unit_interval(
    poly: Poly, *, width: Fraction = Fraction(1, 2**40)
) -> tuple[Fraction, Fraction]:
    """Certified enclosure [low, high] of sup_{p in (0,1)} |poly(p)|.

    The enclosure is valid for the OPEN interval: the endpoint values are included
    because sup over (0,1) of a continuous function is at least its limit at either
    endpoint, so including them can only be conservative on the upper side, and the
    lower bound is always attained at an interior sample.
    """

    if is_zero(poly):
        return Fraction(0), Fraction(0)

    critical = isolate_roots(derivative(poly), Fraction(0), Fraction(1), width=width)
    samples = [Fraction(0), Fraction(1)]
    for left, right in critical:
        samples.extend((left, right))

    low = max(abs(evaluate(poly, x)) for x in samples)

    # Exact Lipschitz bound for |poly'| on [0,1]: the sum of the absolute values of
    # its monomial coefficients.  Each residual bracket can hide at most that much
    # variation over its width.
    slope = sum(abs(coefficient) for coefficient in derivative(poly))
    residual = max((right - left for left, right in critical), default=Fraction(0))
    return low, low + slope * residual


__all__ = [
    "bernstein_to_monomial",
    "count_roots",
    "derivative",
    "evaluate",
    "isolate_roots",
    "squarefree",
    "sturm_sequence",
    "supremum_on_unit_interval",
]
