"""R3 / puente E — ¿sobrevive la dirección `b` a la consistencia por borrado?

Contexto. `dev/r3_bridge_e_fibers.py` mostró que en `n=4` las 16 clases de isomorfismo
de poset sobre 24 permutaciones dejan un núcleo de dimensión 8 (6 direcciones impares de
pares inversos, más 2 de la fibra triple {3421, 4231, 4312}, una impar y una PAR).

Pero un permutón no elige sus densidades de nivel 4 libremente: las de nivel `k` quedan
determinadas por las de nivel `k+1` mediante BORRADO,

    d_k(tau) = (1/(k+1)) * sum_{sigma in S_{k+1}} d_{k+1}(sigma) * #{i : del_i(sigma) = tau}

Este script impone simultáneamente, de forma exacta (aritmética racional):

  (A) las restricciones de fibra de poset en el nivel superior `n`,
  (B) que el empuje hacia abajo por borrado satisfaga las restricciones de fibra
      de poset en TODOS los niveles inferiores.

y descompone el espacio resultante en la parte PAR y la parte IMPAR bajo transposición
`sigma -> sigma^{-1}` (que es la ambigüedad U<->V, inevitable e inocua).

Si la parte par muere, la dicotomía de WP6 se cierra a nivel del observable físico hasta
ese orden. Determinista: sin aleatoriedad, sin semillas, no escribe ficheros.

Referencia: research_program/work_packages/wp6_d2_null_copula_dichotomy.md §5.4
"""

from itertools import permutations
from fractions import Fraction
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from r3_bridge_e_fibers import canonical_form, relation_matrix, inverse  # noqa: E402

from sympy import Matrix, Rational  # noqa: E402


def pattern(seq):
    """Patrón (permutación reducida) de una secuencia de valores distintos."""
    order = sorted(range(len(seq)), key=lambda i: seq[i])
    out = [0] * len(seq)
    for rank, i in enumerate(order):
        out[i] = rank
    return tuple(out)


def delete(sigma, i):
    return pattern(sigma[:i] + sigma[i + 1:])


def fiber_classes(n):
    """Lista de clases: cada una es la lista de permutaciones con el mismo poset."""
    classes = {}
    for sigma in permutations(range(n)):
        cf = canonical_form(relation_matrix(sigma), n)
        classes.setdefault(cf, []).append(sigma)
    return list(classes.values())


def build(n_top):
    """Devuelve (perms_top, filas_de_restriccion) imponiendo (A) y (B)."""
    perms = {k: list(permutations(range(k))) for k in range(2, n_top + 1)}
    index = {k: {p: i for i, p in enumerate(perms[k])} for k in perms}

    # Matriz de empuje hacia abajo: D[k] lleva un vector de nivel k+1 al nivel k.
    down = {}
    for k in range(2, n_top):
        M = [[Rational(0) for _ in perms[k + 1]] for _ in perms[k]]
        for sigma in perms[k + 1]:
            for i in range(k + 1):
                tau = delete(sigma, i)
                M[index[k][tau]][index[k + 1][sigma]] += Rational(1, k + 1)
        down[k] = Matrix(M)

    rows = []
    # (A) restricciones de fibra en el nivel superior.
    for cls in fiber_classes(n_top):
        row = [Rational(0)] * len(perms[n_top])
        for s in cls:
            row[index[n_top][s]] = Rational(1)
        rows.append(row)

    # (B) restricciones de fibra en cada nivel inferior, compuestas por borrado.
    proj = Matrix.eye(len(perms[n_top]))
    for k in range(n_top - 1, 1, -1):
        proj = down[k] * proj
        for cls in fiber_classes(k):
            row = [Rational(0)] * len(perms[n_top])
            for s in cls:
                r = proj.row(index[k][s])
                for j in range(len(perms[n_top])):
                    row[j] += r[j]
            rows.append(row)

    return perms[n_top], Matrix(rows)


def analyse(n_top):
    perms, C = build(n_top)
    ns = C.nullspace()
    dim = len(ns)

    # Descomposición par/impar bajo sigma -> sigma^{-1}.
    idx = {p: i for i, p in enumerate(perms)}
    T = Matrix([[Rational(1) if idx[inverse(p)] == j else Rational(0)
                 for j in range(len(perms))] for p in perms])

    if dim == 0:
        return dim, 0, 0, []

    B = Matrix.hstack(*ns)
    # Proyector par: (I+T)/2 restringido al núcleo.
    even = ((Matrix.eye(len(perms)) + T) / 2) * B
    odd = ((Matrix.eye(len(perms)) - T) / 2) * B
    return dim, even.rank(), odd.rank(), ns


def main():
    print("R3 / puente E — consistencia por borrado sobre el nucleo de fibras")
    print("=" * 72)
    print(f"{'n':>2} {'dim nucleo':>11} {'parte PAR':>10} {'parte IMPAR':>12}   veredicto")
    for n in range(3, 6):
        dim, ev, od, ns = analyse(n)
        verdict = ("dicotomia CERRADA a este orden" if ev == 0
                   else f"sobrevive obstruccion par de dim {ev}")
        print(f"{n:>2} {dim:>11} {ev:>10} {od:>12}   {verdict}")
    print()
    print("La parte IMPAR es la ambiguedad U<->V (C frente a C^T): inevitable e inocua.")
    print("Solo la parte PAR amenaza la dicotomia.")


if __name__ == "__main__":
    main()
