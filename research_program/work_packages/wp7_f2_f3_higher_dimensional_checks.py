#!/usr/bin/env python3
"""Comprobaciones simbólicas para la extensión dimensional de WP7.

Este fichero no sustituye la prueba. Comprueba mecánicamente las integrales de volumen
en d=2,3,4, sus límites planos y el exponente logarítmico de la cota F2.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    y, s = sp.symbols("y s", positive=True, real=True)
    a = sp.exp(-s)
    b = sp.exp(s)
    midpoint = (a + b) / 2

    targets = {
        2: 2 * sp.log(sp.cosh(s)),
        3: 2 * (s - sp.tanh(s)),
        4: 2 * sp.log(sp.cosh(s)) - sp.tanh(s) ** 2,
    }
    unit_ball_volumes = {
        2: sp.Integer(2),
        3: sp.pi,
        4: 4 * sp.pi / 3,
    }

    for dimension, target in targets.items():
        first_half = sp.integrate(
            (y - a) ** (dimension - 1) / y**dimension,
            (y, a, midpoint),
        )
        second_half = sp.integrate(
            (b - y) ** (dimension - 1) / y**dimension,
            (y, midpoint, b),
        )
        computed = sp.simplify(sp.expand_log(first_half + second_half, force=True))
        difference = sp.simplify(sp.trigsimp(computed - target.rewrite(sp.exp)))
        assert difference == 0, (dimension, computed, target, difference)

        volume_ratio = unit_ball_volumes[dimension] * target / (2 * s) ** dimension
        minkowski_constant = unit_ball_volumes[dimension] / (
            dimension * 2 ** (dimension - 1)
        )
        flat_limit = sp.simplify(sp.limit(volume_ratio, s, 0, dir="+"))
        assert sp.simplify(flat_limit - minkowski_constant) == 0

        print(
            f"PASS volume d={dimension}: "
            f"I_{dimension}(s)={sp.sstr(target)}, "
            f"flat ratio={sp.sstr(flat_limit)}"
        )

    dimension = sp.symbols("d", positive=True)
    f2_log_exponent = sp.simplify(
        2 * (1 / dimension - sp.Rational(1, 2)) - sp.Rational(1, 2)
    )
    assert sp.simplify(
        f2_log_exponent - (2 / dimension - sp.Rational(3, 2))
    ) == 0

    expected = {
        2: -sp.Rational(1, 2),
        3: -sp.Rational(5, 6),
        4: -sp.Integer(1),
    }
    for value, exponent in expected.items():
        actual = sp.simplify(f2_log_exponent.subs(dimension, value))
        assert actual == exponent
        print(f"PASS F2 exponent d={value}: log(N)^({actual})")


if __name__ == "__main__":
    main()
