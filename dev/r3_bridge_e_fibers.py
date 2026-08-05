"""R3 / puente E — fibras de sigma |-> [P_sigma], por enumeracion exhaustiva.

Pregunta: para sigma en S_n, sea P_sigma el poset sobre [n] con i < j si y solo si
i < j (indice) y sigma(i) < sigma(j). Es el poset inducido por n puntos en posicion
general en un diamante nulo de d=2, leidos en coordenadas nulas.

El observable fisico es la CLASE DE ISOMORFISMO de P_sigma (poset no etiquetado).
La permutacion no lo es. Este script decide, para n pequeno, si la fibra

    fib([P]) = { sigma : P_sigma isomorfo a P }

coincide exactamente con la orbita por inversion { sigma, sigma^{-1} }, que es la
ambiguedad U <-> V ya conocida y que no rompe nada.

Determinista: sin aleatoriedad, sin semillas, sin remuestreo, no escribe ficheros.
Imprime a stdout. Referencia: research_program/work_packages/wp6_d2_null_copula_dichotomy.md §5.2
"""

from itertools import permutations
from collections import defaultdict


def relation_matrix(sigma):
    """Matriz de la relacion estricta del orden producto."""
    n = len(sigma)
    return tuple(
        tuple(i < j and sigma[i] < sigma[j] for j in range(n)) for i in range(n)
    )


def refine_colors(rel, n):
    """Refinamiento tipo 1-WL sobre el digrafo del poset. Determinista."""
    colors = [0] * n
    while True:
        sig = []
        for i in range(n):
            down = sorted(colors[j] for j in range(n) if rel[j][i])
            up = sorted(colors[j] for j in range(n) if rel[i][j])
            sig.append((colors[i], tuple(down), tuple(up)))
        order = {s: k for k, s in enumerate(sorted(set(sig)))}
        new = [order[s] for s in sig]
        if new == colors:
            return colors
        colors = new


def canonical_form(rel, n):
    """Forma canonica: minimo lexicografico de la cadena de adyacencia sobre
    todas las reetiquetaciones compatibles con el refinamiento de colores."""
    colors = refine_colors(rel, n)
    classes = defaultdict(list)
    for i, c in enumerate(colors):
        classes[c].append(i)
    blocks = [classes[c] for c in sorted(classes)]

    best = None
    def build(prefix, idx):
        nonlocal best
        if idx == len(blocks):
            perm = prefix
            s = tuple(
                rel[perm[a]][perm[b]] for a in range(n) for b in range(n)
            )
            if best is None or s < best:
                best = s
            return
        for p in permutations(blocks[idx]):
            build(prefix + list(p), idx + 1)

    build([], 0)
    return best


def inverse(sigma):
    n = len(sigma)
    inv = [0] * n
    for i, v in enumerate(sigma):
        inv[v] = i
    return tuple(inv)


def analyse(n):
    classes = defaultdict(list)
    for sigma in permutations(range(n)):
        cf = canonical_form(relation_matrix(sigma), n)
        classes[cf].append(sigma)

    total = 0
    bad = []
    size_hist = defaultdict(int)
    for cf, members in classes.items():
        ms = set(members)
        total += 1
        size_hist[len(members)] += 1
        for sigma in members:
            orbit = {sigma, inverse(sigma)}
            if orbit != ms:
                bad.append((cf, sorted(ms)))
                break
    return classes, total, size_hist, bad


def main():
    print("R3 / puente E — fibras de sigma |-> [P_sigma]")
    print("=" * 68)
    print(f"{'n':>2} {'|S_n|':>7} {'clases':>7} {'histograma de |fibra|':>28} "
          f"{'fibra == orbita inversa?':>26}")
    for n in range(1, 8):
        classes, total, size_hist, bad = analyse(n)
        hist = ", ".join(f"{k}:{v}" for k, v in sorted(size_hist.items()))
        verdict = "SI" if not bad else f"NO ({len(bad)} clases)"
        print(f"{n:>2} {len(list(permutations(range(n)))):>7} {total:>7} "
              f"{hist:>28} {verdict:>26}")

        if bad:
            print()
            print(f"  Primer contraejemplo en n={n}:")
            cf, members = bad[0]
            for sigma in members:
                one = "".join(str(v + 1) for v in sigma)
                inv = "".join(str(v + 1) for v in inverse(sigma))
                print(f"    sigma = {one}   sigma^-1 = {inv}")
            print()
            return n
    return None


if __name__ == "__main__":
    main()
