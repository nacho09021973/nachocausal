#!/usr/bin/env python3
"""POST-HOC: autopsia exacta de los pares testigo no homogeneos de Xi^C en n=9.

    *** ESTO NO ES PREREGISTRADO Y NUNCA PODRA SERLO. ***

Los pares se identificaron DESPUES de ejecutar el paso 8
(`emergencia/resultados/p1a_qp_falsador_resumen.json`).  Cualquier regularidad que
aparezca aqui es exploracion post-hoc: describe los pares, no confirma ninguna
hipotesis, y no define ni propone ninguna coordenada nueva de Xi.  Si alguna vez se
quisiera convertir en un resumen, tendria que preregistrarse contra un target distinto
del que ya se ha observado.

BATERIA CONGELADA.  Las medidas son exactamente las que se aplicaron al primer par en
el commit c06a8c4, sin anadir ni una estadistica nueva:

 1. las tres vistas de Xi, para confirmar que el resumen no distingue el par;
 2. el paisaje de niveles completo, con orbitas y candidatos explicitos, y si Xi^C lo
    ve entero o truncado;
 3. los coeficientes exactos a_k y b_k, la divergencia de r_orb mascara a mascara y el
    detalle de las nueve supresiones simples que gobiernan a_8;
 4. que invariantes de orden separan los dos posets;
 5. donde vive la discrepancia en p: el supremo certificado y su argumento.

Seleccion de pares, mecanica y determinista, la misma regla que produjo el testigo
global del paso 8: para cada fibra no homogenea de Xi^C en n=9 se toma el
representante lexicograficamente menor de cada valor de alpha, y de entre ellos la
pareja que maximiza sup_p |q_p(sigma)-q_p(tau)|.

Fuentes: los artefactos ya congelados `p1a_paisaje_niveles_d2.csv` y
`p1a_qp_coeficientes_d2.csv`; no se recalcula nada que ya este publicado.

No se ejecuta ninguna simulacion Monte Carlo y no se escribe ningun artefacto.

    PYTHONDONTWRITEBYTECODE=1 python -m emergencia.p1a_autopsia_par_testigo_posthoc
"""

from __future__ import annotations

import csv
from fractions import Fraction
from itertools import combinations

from dev.r3_bridge_e_fibers import canonical_form, relation_matrix
from emergencia import p1a_enumeracion_simulacion as sealed
from emergencia import p1a_paisaje_niveles_d2 as landscape
from emergencia import p1a_qp_falsador_d2 as falsifier
from emergencia import p1a_sup_exacto as sup_exact
from emergencia import p1a_xi_familia_fibras_d2 as xi

N = 9
SUP_WIDTH = Fraction(1, 2**40)


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
        "n - altura": N - max(height),
        "minimales": minimals,
        "maximales": maximals,
        "perfil de grados (in,out) ordenado": sorted(zip(down, up)),
        "multiconjunto de cardinalidades de intervalo": interval_sizes,
    }


def supremum(alpha_a, alpha_b) -> tuple[float, float]:
    bernstein = [0] * (N + 1)
    for offset, (left, right) in enumerate(zip(alpha_a, alpha_b)):
        bernstein[falsifier.MIN_SUPPORT + offset] = left - right
    poly = sup_exact.bernstein_to_monomial(bernstein, N)
    low, high = sup_exact.supremum_on_unit_interval(poly, width=SUP_WIDTH)
    critical = sup_exact.isolate_roots(
        sup_exact.derivative(poly), Fraction(0), Fraction(1), width=SUP_WIDTH
    )
    argmax = 0.0
    best = Fraction(0)
    for left, right in critical:
        middle = (left + right) / 2
        value = abs(sup_exact.evaluate(poly, middle))
        if value > best:
            best, argmax = value, float(middle)
    return float(low), argmax


def autopsy(sigma_a: tuple[int, ...], sigma_b: tuple[int, ...], label: str) -> dict:
    """The frozen battery, applied to one pair."""

    print()
    print("=" * 78)
    print(label)
    print("=" * 78)

    rule("1. Lo que Xi ve: identico en las 18 coordenadas")
    vectors_a = xi.xi_live(sigma_a)
    vectors_b = xi.xi_live(sigma_b)
    for member in xi.MEMBERS:
        same = vectors_a[member] == vectors_b[member]
        print(f"  {member}: {'IDENTICO' if same else 'DISTINTO'}  {vectors_a[member]}")
        if not same:
            print(f"        b: {vectors_b[member]}")

    rule("2. Paisaje completo de niveles")
    result_a = show_landscape("sigma_a", sigma_a)
    print()
    result_b = show_landscape("sigma_b", sigma_b)
    print()
    truncated = result_a.n_score_levels > 3 or result_b.n_score_levels > 3
    if not truncated:
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
    a_coeffs, b_counts = falsifier.coefficients(sigma_a)
    a_coeffs_b, b_counts_b = falsifier.coefficients(sigma_b)
    alpha_a = falsifier.alpha_of(a_coeffs, N)
    alpha_b = falsifier.alpha_of(a_coeffs_b, N)
    print(f"  a(sigma_a) = {a_coeffs}    b(sigma_a) = {b_counts}")
    print(f"  a(sigma_b) = {a_coeffs_b}    b(sigma_b) = {b_counts_b}")
    print(f"  alpha_a = {alpha_a}")
    print(f"  alpha_b = {alpha_b}")
    print(
        "  incrementos alpha_b - alpha_a = "
        f"{tuple(y - x for x, y in zip(alpha_a, alpha_b))}"
    )

    per_k: dict[int, tuple[int, int, int]] = {}
    for k in (6, 7, 8, 9):
        survivors_a = surviving_masks(sigma_a, k)
        survivors_b = surviving_masks(sigma_b, k)
        only_a = survivors_a - survivors_b
        only_b = survivors_b - survivors_a
        both = survivors_a & survivors_b
        per_k[k] = (len(both), len(only_a), len(only_b))
        print(
            f"\n  |A|={k}:  a_k(a)={len(survivors_a)}  a_k(b)={len(survivors_b)}  "
            f"comunes={len(both)}  solo_a={len(only_a)}  solo_b={len(only_b)}"
        )
        if k == 8:
            print("      (|A|=8 es 'borrar un elemento'; se listan los 9 casos)")
            for removed in range(N):
                retained = tuple(i for i in range(N) if i != removed)
                ra, _ = falsifier.orbit_indicator(
                    falsifier.induced_pattern(sigma_a, retained)
                )
                rb, _ = falsifier.orbit_indicator(
                    falsifier.induced_pattern(sigma_b, retained)
                )
                flag = "  <-- divergen" if ra != rb else ""
                print(
                    f"        borrar i={removed} (valor a={sigma_a[removed]}, "
                    f"b={sigma_b[removed]}):  r_orb_a={ra}  r_orb_b={rb}{flag}"
                )

    tie_nonaut_a = tuple(b_counts[k] - a_coeffs[k] for k in (6, 7, 8))
    tie_nonaut_b = tuple(b_counts_b[k] - a_coeffs_b[k] for k in (6, 7, 8))
    print(
        f"\n  perdida por NO unicidad orbital (b_k - a_k, k=6,7,8):  "
        f"a={tie_nonaut_a}   b={tie_nonaut_b}"
    )

    rule("4. Invariantes de orden que separan los dos posets")
    inv_a = order_invariants(sigma_a)
    inv_b = order_invariants(sigma_b)
    canonical_a = canonical_form(relation_matrix(sigma_a), N)
    canonical_b = canonical_form(relation_matrix(sigma_b), N)
    print(f"  no isomorfos (formas canonicas distintas): {canonical_a != canonical_b}")
    differing = []
    for key in inv_a:
        equal = inv_a[key] == inv_b[key]
        marker = "IGUAL   " if equal else "DISTINTO"
        print(f"  {marker} {key}")
        if not equal:
            differing.append(key)
            print(f"           a: {inv_a[key]}")
            print(f"           b: {inv_b[key]}")

    rule("5. Donde vive la discrepancia en p")
    sup_value, argmax = supremum(alpha_a, alpha_b)
    print(f"  sup_p |q_p(a) - q_p(b)| = {sup_value:.6f}   alcanzado en p ~ {argmax:.6f}")

    return {
        "label": label,
        "a": landscape.encode_permutation(sigma_a),
        "b": landscape.encode_permutation(sigma_b),
        "L": (result_a.n_score_levels, result_b.n_score_levels),
        "Q": (result_a.n_candidates, result_b.n_candidates),
        "aut": (result_a.n_automorphisms, result_b.n_automorphisms),
        "truncated": truncated,
        "same_candidates": same_candidates,
        "alpha_a": alpha_a,
        "alpha_b": alpha_b,
        "per_k": per_k,
        "tie_nonaut": (tie_nonaut_a, tie_nonaut_b),
        "differing_invariants": differing,
        "sup": sup_value,
        "argmax_p": argmax,
        "non_isomorphic": canonical_a != canonical_b,
    }


def witness_pairs() -> list[tuple[tuple[int, ...], tuple[int, ...], tuple]]:
    """The inhomogeneous Xi^C fibres of n=9, from the already frozen artifacts."""

    rows = xi._read_landscape_csv(xi.LANDSCAPE_CSV, (N,))
    alpha_of: dict[str, tuple[int, ...]] = {}
    with (falsifier.DEFAULT_OUTPUT_DIR / falsifier.COEFFICIENT_FILENAME).open(
        newline="", encoding="utf-8"
    ) as handle:
        for row in csv.DictReader(handle):
            if int(row["n"]) == N:
                alpha_of[row["permutation"]] = tuple(
                    int(value) for value in row["alpha"].split("-")
                )

    fibres: dict[tuple, list[str]] = {}
    for encoded in sorted(alpha_of):
        vector = xi.xi_from_csv_rows(rows[(N, encoded)])["XI_C"]
        fibres.setdefault(vector, []).append(encoded)

    pairs = []
    for key in sorted(fibres, key=str):
        members = fibres[key]
        if len(members) < 2:
            continue
        representative: dict[tuple[int, ...], str] = {}
        for encoded in members:  # members are already in lexicographic order
            representative.setdefault(alpha_of[encoded], encoded)
        if len(representative) < 2:
            continue
        best = None
        for left, right in combinations(sorted(representative), 2):
            value, _ = supremum(left, right)
            if best is None or value > best[0]:
                best = (value, left, right)
        assert best is not None
        pairs.append(
            (
                tuple(int(digit) for digit in representative[best[1]]),
                tuple(int(digit) for digit in representative[best[2]]),
                key,
            )
        )
    pairs.sort(key=lambda item: -supremum(
        alpha_of[landscape.encode_permutation(item[0])],
        alpha_of[landscape.encode_permutation(item[1])],
    )[0])
    return pairs


def main() -> int:
    print(__doc__.split("\n\n")[1].strip())
    pairs = witness_pairs()
    print(f"\nFibras no homogeneas de Xi^C en n=9: {len(pairs)}")

    records = []
    for index, (sigma_a, sigma_b, _key) in enumerate(pairs, start=1):
        records.append(autopsy(sigma_a, sigma_b, f"TESTIGO {index} de {len(pairs)}"))

    rule(f"COMPARACION DE MECANISMOS SOBRE LOS {len(records)} TESTIGOS")
    header = (
        f"{'#':>2} {'sigma_a':>10} {'sigma_b':>10} {'L':>5} {'|Q|':>7} {'trunc':>5} "
        f"{'mismos':>6} {'k=8 div':>7} {'TIE_NA':>12} {'sup':>7} {'argmax p':>8}"
    )
    print(header)
    print("-" * len(header))
    for index, record in enumerate(records, start=1):
        divergences = record["per_k"][8][1] + record["per_k"][8][2]
        print(
            f"{index:>2} {record['a']:>10} {record['b']:>10} "
            f"{str(record['L']):>5} {str(record['Q']):>7} "
            f"{'SI' if record['truncated'] else 'no':>5} "
            f"{'SI' if record['same_candidates'] else 'no':>6} "
            f"{divergences:>7} "
            f"{str(record['tie_nonaut'][0]) + '/' + str(record['tie_nonaut'][1]):>12} "
            f"{record['sup']:>7.4f} {record['argmax_p']:>8.4f}"
        )

    print()
    truncated = sum(1 for record in records if record["truncated"])
    same = sum(1 for record in records if record["same_candidates"])
    concentrated = sum(
        1
        for record in records
        if record["per_k"][8][1] + record["per_k"][8][2]
        >= record["per_k"][6][1] + record["per_k"][6][2]
    )
    tie_differential = sum(
        1 for record in records if record["tie_nonaut"][0] != record["tie_nonaut"][1]
    )
    non_isomorphic = sum(1 for record in records if record["non_isomorphic"])
    print(f"  Xi^C truncaba el paisaje de niveles:            {truncated}/{len(records)}")
    print(f"  mismo conjunto de candidatos:                   {same}/{len(records)}")
    print(f"  divergencia en k=8 >= divergencia en k=6:       {concentrated}/{len(records)}")
    print(f"  perdida TIE_NONAUT diferencial entre el par:    {tie_differential}/{len(records)}")
    print(f"  pares no isomorfos:                             {non_isomorphic}/{len(records)}")

    counts: dict[str, int] = {}
    for record in records:
        for key in record["differing_invariants"]:
            counts[key] = counts.get(key, 0) + 1
    print("\n  invariantes de orden que difieren, por numero de testigos:")
    for key in sorted(counts, key=lambda name: -counts[name]):
        print(f"    {counts[key]:>2}/{len(records)}  {key}")

    rule("Etiqueta cientifica")
    print(
        "  EXPLORACION POST-HOC. Describe pares ya observados. No confirma nada, no\n"
        "  propone ninguna coordenada y no puede presentarse como preregistrada."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
