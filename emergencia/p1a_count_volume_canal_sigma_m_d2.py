"""CV-4 — canal sigma(m): identidad finito-muestral exacta y sensibilidad poblacional.

PUNTO UNICO DE AUDITORIA. Determinista, solo lectura sobre la muestra ya sellada
`emergencia/resultados/p1a_representaciones_intervalos_d2.csv`. No genera
aleatoriedad, no remuestrea, no escribe en `resultados/`.

Reduccion (Lemas 1-3 de `P1a_count_volume_canal_sigma_m_d2.md`): dentro de un
estrato (n,side) condicionado a S, G = sigma(m,n,side,S) = sigma(m), y
COUNT_VOLUME = sqrt((m-2)/(n-2)) es biyeccion creciente de m, luego
sigma(COUNT_VOLUME) = G.

BLOQUE A (exacto, sin hipotesis): sobre la distribucion empirica sellada,
    T_emp        = SSW/SST
    rho_max_emp  = sqrt(SSB/SST)
son identidades finito-muestrales. Ninguna funcion de m -lineal o no- supera
rho_max_emp en la muestra sellada. No requiere iid, ni SE, ni bootstrap, ni w.

BLOQUE B (inferencia poblacional, SI requiere iid dentro del estrato): estimador
con correccion intrabin y error estandar analitico por funcion de influencia.
NO es un estimador insesgado de T: es un cociente de estimadores, no un
estimador del cociente. La funcion de influencia es la de PRIMER ORDEN del
cociente plug-in: no incorpora las correcciones (n_j-1) ni los bins omitidos, y
por tanto los multiplos de SE son distancias asintoticas bajo iid, NO exactas.

T_xfit (validacion cruzada determinista par/impar) es un DIAGNOSTICO DE
SOBREAJUSTE REALIZADO, no una cota. La desigualdad
    E_eval[(Y-mu_hat_M)^2 | mu_hat] = A + E[(mu_M-mu_hat_M)^2] >= A
es de esperanza condicional dado el predictor entrenado; una realizacion puede
quedar por encima o por debajo. Ademas su denominador usa la muestra completa,
luego no es una razon completamente out-of-sample.
"""

import csv
import math
import sys
from collections import defaultdict

sys.path.insert(0, "emergencia")

from p1a_count_volume_cota_resolucion_evaluacion_d2 import bound_for_m  # noqa: E402

CSV = "emergencia/resultados/p1a_representaciones_intervalos_d2.csv"
GATE = 0.80
THRESHOLD = 1.0 - GATE ** 2  # 0.36


def load():
    rows = defaultdict(list)
    with open(CSV, newline="") as f:
        for r in csv.DictReader(f):
            n = int(r["n"])
            if n in (64, 96, 128):
                rows[(n, r["side"])].append((
                    int(r["interval_size"]),
                    float(r["latent_duration"]),
                    float(r["estimate_count_volume"]),
                    r["replicate"],
                ))
    return rows


def pearson(xs, ys):
    N = len(xs)
    mx, my = sum(xs) / N, sum(ys) / N
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    return sxy / math.sqrt(sxx * syy)


rows = load()

# ---------------------------------------------------------------- BLOQUE A
print("=" * 104)
print("BLOQUE A — IDENTIDAD FINITO-MUESTRAL EXACTA sobre la muestra sellada")
print("  sin hipotesis de iid, sin SE, sin bootstrap, sin w")
print("=" * 104)
print(f"{'n':>4} {'side':>6} {'N':>6} {'K':>3} {'SSW':>10} {'SSB':>10} {'SST':>10} "
      f"{'T_emp':>7} {'>0.36':>6} {'rho_max_emp':>12} {'rho_obs':>8}")

A = {}
for key in sorted(rows):
    n, side = key
    entries = rows[key]
    N = len(entries)
    g = defaultdict(list)
    for m, y, _, _ in entries:
        g[m].append(y)
    K = len(g)
    grand = sum(y for _, y, _, _ in entries) / N
    ssb = sum(len(ys) * (sum(ys) / len(ys) - grand) ** 2 for ys in g.values())
    ssw = sum(sum((y - sum(ys) / len(ys)) ** 2 for y in ys) for ys in g.values())
    # SST calculado DIRECTAMENTE sobre las observaciones, no como SSB+SSW.
    # La descomposicion ANOVA se verifica, no se impone.
    sst = sum((y - grand) ** 2 for _, y, _, _ in entries)
    anova_gap = abs(sst - (ssb + ssw)) / sst
    assert anova_gap < 1e-12, (key, anova_gap)
    t_emp = ssw / sst
    rho_max_emp = math.sqrt(ssb / sst)
    rho_obs = pearson([e[1] for e in entries], [e[2] for e in entries])
    A[key] = dict(N=N, K=K, ssb=ssb, ssw=ssw, sst=sst, t_emp=t_emp, anova_gap=anova_gap,
                  rho_max_emp=rho_max_emp, rho_obs=rho_obs, groups=g, grand=grand)
    print(f"{n:>4} {side:>6} {N:>6} {K:>3} {ssw:>10.6f} {ssb:>10.6f} {sst:>10.6f} "
          f"{t_emp:>7.4f} {'SI' if t_emp > THRESHOLD else 'NO':>6} "
          f"{rho_max_emp:>12.4f} {rho_obs:>8.4f}")

print()
print("CONTROLES DEL BLOQUE A (identidades; deben ser todos True):")
ok_a = True
for key in sorted(A):
    s = A[key]
    entries = rows[key]
    # (i) COUNT_VOLUME es biyeccion creciente de m dentro del estrato
    pares = sorted({(e[0], e[2]) for e in entries})
    biy = len({p[0] for p in pares}) == len({p[1] for p in pares}) == len(pares)
    mono = all(pares[i][1] < pares[i + 1][1] for i in range(len(pares) - 1))
    # (ii) la media por bin alcanza exactamente rho_max_emp
    pred = [sum(s["groups"][e[0]]) / len(s["groups"][e[0]]) for e in entries]
    rho_pred = pearson([e[1] for e in entries], pred)
    alcanza = abs(rho_pred - s["rho_max_emp"]) < 1e-12
    # (iii) ninguna funcion de m la supera: |rho_obs| <= rho_max_emp
    domina = abs(s["rho_obs"]) <= s["rho_max_emp"] + 1e-12
    # (iv) una fila por replica (estructura del panel sellado)
    unica = len({e[3] for e in entries}) == len(entries)
    # (v) la descomposicion ANOVA se cumple con SST calculado directamente
    descompone = s["anova_gap"] < 1e-12
    ok_a &= biy and mono and alcanza and domina and unica and descompone
    print(f"  n={key[0]:>3} {key[1]:>6}: biyectiva={biy} monotona={mono} "
          f"media_bin_alcanza_rho_max={alcanza} |rho_obs|<=rho_max={domina} "
          f"una_fila_por_replica={unica} SST=SSB+SSW={descompone}")
print(f"\nBLOQUE_A_CONSISTENCIA = {'PASS' if ok_a else 'FAIL'}")
print(f"CV4_SEALED_SAMPLE_STATUS = "
      f"{'GATE_EXCLUDED_EXACTLY' if all(A[k]['t_emp'] > THRESHOLD for k in A) else 'NOT_EXCLUDED'}")
print(f"RHO_MAX_EMP_RANGO = {min(A[k]['rho_max_emp'] for k in A):.4f} a "
      f"{max(A[k]['rho_max_emp'] for k in A):.4f}")

# ---------------------------------------------------------------- BLOQUE B
print()
print("=" * 104)
print("BLOQUE B — INFERENCIA POBLACIONAL (requiere filas iid dentro del estrato)")
print("  T_corr NO es insesgado para T: es un cociente de estimadores.")
print("=" * 104)
print(f"{'n':>4} {'side':>6} {'T_corr':>7} {'SE_infl':>8} {'T_corr-3SE':>11} "
      f"{'holgura/SE':>11} {'T_xfit':>7} {'T_bins>=30':>11} {'B_n/Var':>8} {'B_n<=EVar':>10}")

cache = {}
for key in sorted(A):
    n, side = key
    entries = rows[key]
    s = A[key]
    N, g, grand = s["N"], s["groups"], s["grand"]

    num = sum((len(ys) / N) * (sum((y - sum(ys) / len(ys)) ** 2 for y in ys) / (len(ys) - 1))
              for ys in g.values() if len(ys) >= 2)
    den = s["sst"] / (N - 1)
    t_corr = num / den

    # Funcion de influencia de PRIMER ORDEN del cociente plug-in, CENTRADA
    # explicitamente antes de tomar el segundo momento.
    binmean = {m: sum(ys) / len(ys) for m, ys in g.items()}
    infl = [(((y - binmean[m]) ** 2 - num) - t_corr * ((y - grand) ** 2 - den)) / den
            for m, y, _, _ in entries]
    infl_mean = sum(infl) / N
    se = math.sqrt(sum((v - infl_mean) ** 2 for v in infl) / N ** 2)

    # DIAGNOSTICO de sobreajuste (validacion cruzada determinista par/impar).
    # NO es una cota: la desigualdad E_eval[...|mu_hat] >= A es de esperanza
    # condicional, no vale para una realizacion. Denominador = muestra completa,
    # luego tampoco es una razon completamente out-of-sample.
    tot = cnt = 0
    idx = list(range(N))
    for fit, ev in ((idx[0::2], idx[1::2]), (idx[1::2], idx[0::2])):
        gm = defaultdict(list)
        for i in fit:
            gm[entries[i][0]].append(entries[i][1])
        mu = {k2: sum(v) / len(v) for k2, v in gm.items()}
        gmean = sum(entries[i][1] for i in fit) / len(fit)
        for i in ev:
            tot += (entries[i][1] - mu.get(entries[i][0], gmean)) ** 2
            cnt += 1
    t_xfit = tot / cnt / den

    # peor caso: bins pequenos predichos perfectamente
    num_big = sum((len(ys) / N) * (sum((y - sum(ys) / len(ys)) ** 2 for y in ys) / (len(ys) - 1))
                  for ys in g.values() if len(ys) >= 30)
    t_big = num_big / den

    bsum = 0.0
    for m, _, _, _ in entries:
        if (m, n) not in cache:
            cache[(m, n)] = bound_for_m(m, n)
        bsum += cache[(m, n)]
    b_n = bsum / N

    print(f"{n:>4} {side:>6} {t_corr:>7.4f} {se:>8.5f} {t_corr - 3 * se:>11.4f} "
          f"{(t_corr - THRESHOLD) / se:>11.1f} {t_xfit:>7.4f} {t_big:>11.4f} "
          f"{b_n / den:>8.4f} {'OK' if b_n <= num else 'VIOLADO':>10}")

print()
print("Lectura del Bloque B — limites que NO deben rebasarse:")
print("  * 'holgura/SE' son distancias ASINTOTICAS bajo iid con influencia de primer")
print("    orden; no son exactas ni dan un intervalo demostrado.")
print("  * T_xfit es un diagnostico de sobreajuste REALIZADO, no una cota superior:")
print("    no se deriva de el ningun intervalo poblacional.")
print("  * los bins con n_j<2 se omiten de T_corr; los n_j<30 se anulan en el control")
print("    de sensibilidad. Ambas cosas refuerzan el techo NOT_CLOSED_FORM_THEOREM.")
print()
print("CV4_POPULATION_STATUS = STRONGLY_SUPPORTED_UNDER_IID_NOT_CLOSED_FORM_THEOREM")
print("CV4_POPULATION_INTERVAL_CLAIMED = NO")
print("OLD_BN_RHO_MAX_LABEL = RETRACTED_AND_RENAMED_rho_max_ub_Bn")
print("W_STATUS = UNNECESSARY_FOR_SEALED_G_CHANNEL")
print("CV4_RICHER_CHANNEL_STATUS = OUT_OF_SCOPE_ONLY_LINEAR_FAMILY_TESTED")
