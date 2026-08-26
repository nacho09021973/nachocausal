#!/usr/bin/env python3
"""POST-HOC: autopsia exacta del par testigo de Xi^C en n=9.

    *** ESTO NO ES PREREGISTRADO Y NUNCA PODRA SERLO. ***

El par se identifico DESPUES de ejecutar el paso 8
(`emergencia/resultados/p1a_qp_falsador_resumen.json`).  Cualquier regularidad que
aparezca aqui es exploracion post-hoc: describe el par, no confirma ninguna hipotesis,
y no define ni propone ninguna coordenada nueva de Xi.  Si alguna vez se quisiera
convertir en un resumen, tendria que preregistrarse contra un target distinto del que
ya se ha observado.

Objeto: los dos elementos de la misma fibra de Xi^C (18 coordenadas identicas) cuyos
vectores de coeficientes libres difieren,

    sigma_a = 012583674   alpha = (2, 5, 2)
    sigma_b = 012573846   alpha = (2, 6, 6)

Se responde, exactamente y sin aproximar nada:

 1. que ve Xi^C y por tanto que es identico entre los dos;
 2. si el paisaje de niveles completo es identico o solo lo es hasta la profundidad 3;
 3. mascara por mascara, donde diverge r_orb, con el detalle de las 9 supresiones
    simples que gobiernan a_8;
 4. que invariantes de orden separan a los dos posets.

No se ejecuta ninguna simulacion Monte Carlo y no se escribe ningun artefacto.

    PYTHONDONTWRITEBYTECODE=1 python -m emergencia.p1a_autopsia_par_testigo_posthoc
"""

from __future__ import annotations

from itertools import combinations

from dev.r3_bridge_e_fibers import canonical_form, relation_matrix
from emergencia import p1a_enumeracion_simulacion as sealed
from emergencia import p1a_paisaje_niveles_d2 as landscape
from emergencia import p1a_qp_falsador_d2 as falsifier
from emergencia import p1a_tie_aut_diagnostic as tie_aut
from emergencia import p1a_xi_familia_fibras_d2 as xi


SIGMA_A = (0, 1, 2, 5, 8, 3, 6, 7, 4)
SIGMA_B = (0, 1, 2, 5, 7, 3, 8, 4, 6)
N = 9


def rule(title: str) -> None:
    print()
    print(title)
    print("-" * len(title))


def show_landscape(name: str, permutation: tuple[int, ...]) -> landscape.PermutationLandscape:
    result = landscape.score_landscape(permutation)
    print(
        f"{name} = {landscape.encode_permutation(permutation)}   "
        f"|Q|={result.n_candidates}  L={result.n_score_levels}  |Aut|={result.n_automorphisms}"
    )
    for index, level in enumerate(result.levels):
        print(
            f"    nivel {index}: S=({level.primary_score},{level.secondary_score})  "
            f"|A|={level.candidate_count}  orbitas={level.orbit_count}  "
            f"tamanos={level.orbit_sizes}"
        )
        for orbit in level.orbits:
            print(f"        orbita {orbit}")
    return result


def surviving_masks(permutation: tuple[int, ...], k: int) -> set[tuple[int, ...]]:
    survivors = set()
    for retained in combinations(range(N), k):
        r_orb, _ = falsifier.orbit_indicator(
            falsifier.induced_pattern(permutation, retained)
        )
        if r_orb:
            survivors.add(retained)
    return survivors


def order_invariants(permutation: tuple[int, ...]) -> dict[str, object]:
    relation = relation_matrix(permutation)
    counts, comparable = sealed.interval_count_matrix(permutation)
    relations = sum(1 for i in range(N) for j in range(N) if relation[i][j])
    down = [sum(1 for j in range(N) if relation[j][i]) for i in range(N)]
    up = [sum(1 for j in range(N) if relation[i][j]) for i in range(N)]
    minimals = sum(1 for i in range(N) if down[i] == 0)
    maximals = sum(1 for i in range(N) if up[i] == 0)
    # longest chain, by dynamic programming over the strict order
    height = [1] * N
    for j in range(N):
        for i in range(N):
            if relation[i][j]:
                height[j] = max(height[j], height[i] + 1)
    interval_sizes = sorted(
        int(counts[i, j]) for i in range(N) for j in range(N) if comparable[i, j]
    )
    return {
        "relaciones": relations,
        "altura (cadena maxima)": max(height),
        "anchura (anticadena via n - relaciones cubiertas)": N - max(height),
        "minimales": minimals,
        "maximales": maximals,
        "perfil de grados (in,out) ordenado": sorted(zip(down, up)),
        "multiconjunto de cardinalidades de intervalo": interval_sizes,
        "forma canonica": canonical_form(relation, N)[:0] or "ver hash",
        "hash canonico": None,
    }


def main() -> int:
    print(__doc__.split("\n\n")[1].strip())

    rule("1. Lo que Xi ve: identico en las 18 coordenadas")
    vectors_a = xi.xi_live(SIGMA_A)
    vectors_b = xi.xi_live(SIGMA_B)
    for member in xi.MEMBERS:
        same = vectors_a[member] == vectors_b[member]
        print(f"  {member}: {'IDENTICO' if same else 'DISTINTO'}  {vectors_a[member]}")
        if not same:
            print(f"        b: {vectors_b[member]}")

    rule("2. Paisaje completo de niveles")
    result_a = show_landscape("sigma_a", SIGMA_A)
    print()
    result_b = show_landscape("sigma_b", SIGMA_B)
    print()
    if result_a.n_score_levels <= 3 and result_b.n_score_levels <= 3:
        print(
            "  L <= 3 en ambos: Xi^C captura el paisaje de niveles ENTERO, no una "
            "truncacion.\n  La informacion que falta NO esta en niveles mas profundos."
        )
    else:
        print(
            f"  L_a={result_a.n_score_levels}, L_b={result_b.n_score_levels}: hay "
            "niveles por debajo de la profundidad 3 que Xi^C no describe."
        )
    same_candidates = set(result_a.candidates) == set(result_b.candidates)
    print(f"  ?mismos candidatos como conjunto de cuadruplas?  {same_candidates}")

    rule("3. Coeficientes exactos y divergencia mascara a mascara")
    a_coeffs, b_counts = falsifier.coefficients(SIGMA_A)
    a_coeffs_b, b_counts_b = falsifier.coefficients(SIGMA_B)
    print(f"  a(sigma_a) = {a_coeffs}    b(sigma_a) = {b_counts}")
    print(f"  a(sigma_b) = {a_coeffs_b}    b(sigma_b) = {b_counts_b}")
    print(f"  alpha_a = {falsifier.alpha_of(a_coeffs, N)}")
    print(f"  alpha_b = {falsifier.alpha_of(a_coeffs_b, N)}")
    print(
        "  incrementos alpha_b - alpha_a = "
        f"{tuple(y - x for x, y in zip(falsifier.alpha_of(a_coeffs, N), falsifier.alpha_of(a_coeffs_b, N)))}"
    )

    for k in (6, 7, 8, 9):
        survivors_a = surviving_masks(SIGMA_A, k)
        survivors_b = surviving_masks(SIGMA_B, k)
        only_a = survivors_a - survivors_b
        only_b = survivors_b - survivors_a
        both = survivors_a & survivors_b
        print(
            f"\n  |A|={k}:  a_k(a)={len(survivors_a)}  a_k(b)={len(survivors_b)}  "
            f"comunes={len(both)}  solo_a={len(only_a)}  solo_b={len(only_b)}"
        )
        if k == 8:
            print("      (|A|=8 es 'borrar un elemento'; se listan los 9 casos)")
            for removed in range(N):
                retained = tuple(i for i in range(N) if i != removed)
                ra, _ = falsifier.orbit_indicator(
                    falsifier.induced_pattern(SIGMA_A, retained)
                )
                rb, _ = falsifier.orbit_indicator(
                    falsifier.induced_pattern(SIGMA_B, retained)
                )
                flag = "  <-- divergen" if ra != rb else ""
                print(
                    f"        borrar i={removed} (valor a={SIGMA_A[removed]}, "
                    f"b={SIGMA_B[removed]}):  r_orb_a={ra}  r_orb_b={rb}{flag}"
                )

    rule("4. Invariantes de orden que separan los dos posets")
    inv_a = order_invariants(SIGMA_A)
    inv_b = order_invariants(SIGMA_B)
    canonical_a = canonical_form(relation_matrix(SIGMA_A), N)
    canonical_b = canonical_form(relation_matrix(SIGMA_B), N)
    print(f"  no isomorfos (formas canonicas distintas): {canonical_a != canonical_b}")
    for key in inv_a:
        if key in ("forma canonica", "hash canonico"):
            continue
        equal = inv_a[key] == inv_b[key]
        marker = "IGUAL   " if equal else "DISTINTO"
        print(f"  {marker} {key}")
        if not equal:
            print(f"           a: {inv_a[key]}")
            print(f"           b: {inv_b[key]}")

    rule("Etiqueta cientifica")
    print(
        "  EXPLORACION POST-HOC. Describe un par ya observado. No confirma nada, no\n"
        "  propone ninguna coordenada y no puede presentarse como preregistrada."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
