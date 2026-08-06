"""R3 / puente E — ¿es la dirección `b` realizable a primer orden alrededor de `Pi`?

La consistencia por borrado (`dev/r3_bridge_e_deletion.py`) NO mata la dirección par `b`,
y la obstrucción par crece con `n` (1 en n=4, 10 en n=5). Luego el puente E' no se cierra
por álgebra lineal: la pregunta es de REALIZABILIDAD por un permutón de verdad.

Este script decide la versión infinitesimal. Perturbamos el permutón uniforme,

    dC_eps = (1 + eps*h(x,y)) dx dy,     con marginales nulas: int h dx = int h dy = 0,

y usamos que, para 4 puntos iid,

    d_sigma(eps) = 1/24 + 4*eps*E[ h(X_1,Y_1) * 1{patron = sigma} ] + O(eps^2)
                 = 1/24 + 4*eps*<h, G_sigma> + O(eps^2),

donde `G_sigma(x,y)` es la probabilidad de que un punto FIJO en `(x,y)` más 3 uniformes
formen el patrón `sigma`. `G_sigma` es polinomio de grado <= 3 en cada variable, luego el
emparejamiento solo ve la proyección de `h` sobre `span{p_i(x) p_j(y) : 1<=i,j<=3}` con
`p_i` los polinomios de Legendre desplazados (media nula ⇒ marginales nulas). El problema
es por tanto EXACTAMENTE 9-dimensional y se resuelve en aritmética racional.

Preguntamos: ¿existe `h` con `<h, G_sigma> = 0` para las 21 permutaciones cuya densidad
está forzada a `1/24`, y con efecto NO nulo sobre la fibra triple {3421, 4231, 4312} en la
proporción par `(+1, -2, +1)`?

  - Si SÍ: hay un permutón curvo indistinguible del plano a orden 4, a primer orden, y el
    teorema de la función implícita hace muy verosímil una construcción exacta. Sería un
    parche curvo ciego al orden: la rama espectacular.
  - Si NO: `b` no es realizable infinitesimalmente y la dicotomía gana terreno.

`G_sigma` se calcula EXACTAMENTE, sin integración numérica: los 3 puntos uniformes se
reparten entre las 4 regiones que `(x,y)` induce en el cuadrado; dentro de cada región
X e Y son independientes y uniformes, luego el orden en X dentro de cada mitad vertical y
el orden en Y dentro de cada mitad horizontal son uniformes e independientes.

Determinista: sin aleatoriedad, sin semillas, no escribe ficheros.
Referencia: research_program/work_packages/wp6_d2_null_copula_dichotomy.md §5.4
"""

from itertools import permutations, product
from collections import defaultdict

from sympy import Rational, symbols, integrate, expand, legendre, sqrt, Matrix, simplify

x, y = symbols("x y", positive=True)

TRIPLE = [(2, 3, 1, 0), (3, 1, 2, 0), (3, 2, 0, 1)]   # 3421, 4231, 4312 en base 0
TRIPLE_WEIGHTS = {(2, 3, 1, 0): 1, (3, 2, 0, 1): 1, (3, 1, 2, 0): -2}


def pattern_from_orders(xorder, yorder):
    """De un orden en X y un orden en Y de las mismas 4 etiquetas al patrón."""
    xrank = {lab: i for i, lab in enumerate(xorder)}
    yrank = {lab: i for i, lab in enumerate(yorder)}
    return tuple(yrank[lab] for lab in sorted(xrank, key=lambda l: xrank[l]))


def g_polynomials():
    """G_sigma(x,y) exacto para cada sigma en S_4, como polinomio racional."""
    # Regiones para cada uno de los 3 puntos uniformes: (izq/der de x, abajo/arriba de y)
    weight = {
        (0, 0): x * y,
        (0, 1): x * (1 - y),
        (1, 0): (1 - x) * y,
        (1, 1): (1 - x) * (1 - y),
    }
    G = defaultdict(lambda: 0)
    F = "F"                       # el punto fijo
    labels = [0, 1, 2]

    for assign in product(weight, repeat=3):
        prob = weight[assign[0]] * weight[assign[1]] * weight[assign[2]]

        left = [i for i in labels if assign[i][0] == 0]
        right = [i for i in labels if assign[i][0] == 1]
        down = [i for i in labels if assign[i][1] == 0]
        up = [i for i in labels if assign[i][1] == 1]

        xperms = [list(a) + [F] + list(b)
                  for a in permutations(left) for b in permutations(right)]
        yperms = [list(a) + [F] + list(b)
                  for a in permutations(down) for b in permutations(up)]
        norm = Rational(1, len(xperms) * len(yperms))

        for xo in xperms:
            for yo in yperms:
                G[pattern_from_orders(xo, yo)] += prob * norm

    return {s: expand(g) for s, g in G.items()}


def legendre_basis():
    """p_1, p_2, p_3 de Legendre desplazados a [0,1]: media nula, ortogonales."""
    return [expand(legendre(k, 2 * x - 1)) for k in (1, 2, 3)]


def main():
    print("R3 / puente E — realizabilidad de `b` a primer orden alrededor de Pi")
    print("=" * 74)

    G = g_polynomials()
    perms = sorted(G)
    assert len(perms) == 24
    # Control: sum_sigma G_sigma = 1 y int G_sigma = 1/24.
    tot = expand(sum(G.values()))
    assert simplify(tot - 1) == 0, tot
    for s in perms:
        m = integrate(integrate(G[s], (x, 0, 1)), (y, 0, 1))
        assert m == Rational(1, 24), (s, m)
    print("controles: sum_sigma G_sigma = 1  y  int G_sigma = 1/24 para las 24   [OK]")

    P = legendre_basis()
    basis = [(i, j) for i in range(3) for j in range(3)]        # 9 funciones h
    def pair(hpoly, s):
        f = expand(hpoly * G[s])
        return integrate(integrate(f, (x, 0, 1)), (y, 0, 1))

    L = {}
    for (i, j) in basis:
        h = expand(P[i] * P[j].subs(x, y))
        for s in perms:
            L[(i, j, s)] = 4 * pair(h, s)

    forced = [s for s in perms if s not in TRIPLE_WEIGHTS]
    assert len(forced) == 21

    # Sistema: <h, G_s> = 0 para las 21 forzadas.
    A = Matrix([[L[(i, j, s)] for (i, j) in basis] for s in forced])
    ns = A.nullspace()
    print(f"h vive en dimension {len(basis)}; restricciones forzadas: {len(forced)}")
    print(f"nucleo de las 21 restricciones: dimension {len(ns)}")

    if not ns:
        print()
        print("VEREDICTO: ninguna perturbacion de primer orden mantiene las 21 densidades")
        print("forzadas en 1/24 salvo h=0. La direccion `b` NO es realizable a primer orden.")
        return

    print()
    print("Efecto de cada vector del nucleo sobre la fibra triple:")
    any_b = False
    for k, v in enumerate(ns):
        eff = {}
        for s in TRIPLE_WEIGHTS:
            eff[s] = sum(v[m] * L[(basis[m][0], basis[m][1], s)] for m in range(len(basis)))
            eff[s] = simplify(eff[s])
        lab = {(2, 3, 1, 0): "3421", (3, 1, 2, 0): "4231", (3, 2, 0, 1): "4312"}
        print(f"  vector {k}: " + ", ".join(f"{lab[s]}={eff[s]}" for s in TRIPLE_WEIGHTS))
        if any(e != 0 for e in eff.values()):
            any_b = True

    print()
    if any_b:
        print("VEREDICTO: la direccion `b` SI es alcanzable a primer orden.")
    else:
        print("VEREDICTO: todo el nucleo actua trivialmente sobre la fibra triple:")
        print("`b` NO es realizable a primer orden.")


if __name__ == "__main__":
    main()
