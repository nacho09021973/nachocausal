"""CV-4 item 2: techo analitico del factor que puede aportar apretar F_relax
por arriba (restriccion del lado opuesto).

Determinista, solo lectura sobre datos ya sellados. Contesta, sin evaluar ninguna
restriccion concreta, cual es el factor MAXIMO alcanzable por cualquier apriete que
solo baje las cotas superiores de (k,l).

Argumento (Seccion 2 del documento): la esquina inferior
  s_min(m) = (max(2,m-1), max(2,m-1))
es factible en F_relax siempre que m<=n (se cumple en todo el regimen publicado), y
NINGUN apriete que solo baje cotas superiores puede eliminarla. Luego para cualquier
F_tight obtenido asi,
  min_{F_tight} Var(ell|s) <= Var(ell|s_min(m)),
y por tanto
  B_n^tight <= E_m[Var(ell|s_min(m))] =: techo_esquina.
El cociente techo_esquina / B_n es el factor maximo alcanzable por esa via.
"""

import csv
import sys
from collections import defaultdict

sys.path.insert(0, "emergencia")

from p1a_count_volume_cota_resolucion_evaluacion_d2 import (  # noqa: E402
    bound_for_m,
    var_ell_given_shape,
)

INTERVALS_CSV = "emergencia/resultados/p1a_representaciones_intervalos_d2.csv"
K_NEEDED_MIN = 1.17  # excluiria el gate 0.80 en al menos un estrato
K_NEEDED_ALL = 1.36  # lo excluiria en los seis


def corner_bound(m, n):
    lo = max(2, m - 1)
    return var_ell_given_shape(lo, lo, n)


def opposite_side_bound(m, n):
    """Apriete concreto k,l <= n-3 (el lado opuesto necesita k_+,l_+>=1 y gamma>beta)."""
    lo = max(2, m - 1)
    hi = min(n - 3, n + m - 2 - lo)
    best = None
    for k in range(lo, hi + 1):
        for l in range(lo, min(hi, n + m - 2 - k) + 1):
            v = var_ell_given_shape(k, l, n)
            if best is None or v < best:
                best = v
    return best


def load_m_by_stratum(path):
    rows = defaultdict(list)
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            n = int(row["n"])
            if n in (64, 96, 128):
                rows[(n, row["side"])].append(int(row["interval_size"]))
    return rows


if __name__ == "__main__":
    strata = load_m_by_stratum(INTERVALS_CSV)
    cache = {}
    print(
        f"{'n':>4} {'side':>6} {'B_n':>10} {'B_n(k,l<=n-3)':>14} {'techo_esquina':>14} "
        f"{'factor_n-3':>11} {'factor_max':>11}"
    )
    factors_max = []
    factors_n3 = []
    for key in sorted(strata):
        n, side = key
        ms = strata[key]
        totals = [0.0, 0.0, 0.0]
        for m in ms:
            if (m, n) not in cache:
                cache[(m, n)] = (
                    bound_for_m(m, n),
                    opposite_side_bound(m, n),
                    corner_bound(m, n),
                )
            for i, v in enumerate(cache[(m, n)]):
                totals[i] += v
        base, n3, corner = (t / len(ms) for t in totals)
        factors_max.append(corner / base)
        factors_n3.append(n3 / base)
        print(
            f"{n:>4} {side:>6} {base:>10.6f} {n3:>14.6f} {corner:>14.6f} "
            f"{n3 / base:>11.6f} {corner / base:>11.6f}"
        )

    fmax = max(factors_max)
    print()
    print(f"CV4_ITEM2_FACTOR_OPPOSITE_SIDE_CONCRETE = {max(factors_n3):.6f}")
    print(f"CV4_ITEM2_FACTOR_CEILING_ANY_UPPER_TIGHTENING = {fmax:.6f}")
    print(f"CV4_ITEM2_CAN_REACH_{K_NEEDED_MIN} = {'YES' if fmax >= K_NEEDED_MIN else 'NO'}")
    print(f"CV4_ITEM2_CAN_REACH_{K_NEEDED_ALL} = {'YES' if fmax >= K_NEEDED_ALL else 'NO'}")
    print(
        "CV4_ITEM2_VERDICT = "
        + ("PURSUE" if fmax >= K_NEEDED_MIN else "ABANDON_ROUTE_WITHOUT_RESOLVING_W")
    )
