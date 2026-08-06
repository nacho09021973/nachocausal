import csv
import math
from collections import defaultdict

INTERVALS_CSV = "emergencia/resultados/p1a_representaciones_intervalos_d2.csv"


def e_sqrt_beta(a, b):
    return math.exp(
        math.lgamma(a + 0.5) + math.lgamma(a + b) - math.lgamma(a) - math.lgamma(a + b + 0.5)
    )


def var_ell_given_shape(k, l, n):
    e_x = k / (n + 1)
    e_y = l / (n + 1)
    e_sqrt_x = e_sqrt_beta(k, n + 1 - k)
    e_sqrt_y = e_sqrt_beta(l, n + 1 - l)
    return e_x * e_y - (e_sqrt_x * e_sqrt_y) ** 2


def bound_for_m(m, n):
    lo = max(2, m - 1)
    hi = n - 1
    best = None
    for k in range(lo, hi + 1):
        k_l_cap = n + m - 2 - k
        l_hi = min(hi, k_l_cap)
        for l in range(lo, l_hi + 1):
            v = var_ell_given_shape(k, l, n)
            if best is None or v < best:
                best = v
    return best


def check_hand_example():
    v = bound_for_m(3, 4)
    assert abs(v - 0.021974) < 1e-5, v
    return v


def load_rows(path):
    rows = defaultdict(list)
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            n = int(row["n"])
            if n not in (64, 96, 128):
                continue
            m = int(row["interval_size"])
            side = row["side"]
            signed_error = float(row["signed_error_count_volume"])
            rows[(n, side)].append((m, signed_error))
    return rows


def summarize(rows):
    cache = {}
    out = {}
    for (n, side), entries in sorted(rows.items()):
        bound_sum = 0.0
        mse_sum = 0.0
        m_values = []
        for m, signed_error in entries:
            key = (m, n)
            if key not in cache:
                cache[key] = bound_for_m(m, n)
            bound_sum += cache[key]
            mse_sum += signed_error ** 2
            m_values.append(m)
        count = len(entries)
        out[(n, side)] = {
            "count": count,
            "mean_m": sum(m_values) / count,
            "median_m": sorted(m_values)[count // 2],
            "bound_avg": bound_sum / count,
            "mse_observed": mse_sum / count,
        }
    return out


if __name__ == "__main__":
    hand_check = check_hand_example()
    print(f"HAND_EXAMPLE_CHECK n=4,m=3 bound={hand_check:.6f} (expected 0.021974)")
    rows = load_rows(INTERVALS_CSV)
    summary = summarize(rows)
    print(f"{'n':>4} {'side':>6} {'count':>6} {'mean_m':>8} {'median_m':>9} "
          f"{'bound_avg':>11} {'mse_observed':>13} {'bound/mse':>10}")
    for (n, side), s in summary.items():
        ratio = s["bound_avg"] / s["mse_observed"]
        print(f"{n:>4} {side:>6} {s['count']:>6} {s['mean_m']:>8.2f} {s['median_m']:>9} "
              f"{s['bound_avg']:>11.6f} {s['mse_observed']:>13.6f} {ratio:>10.4f}")
