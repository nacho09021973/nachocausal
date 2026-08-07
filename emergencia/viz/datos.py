"""Carga verificada de los artefactos sellados de la línea `emergencia`.

Regla de la casa: una figura que dibuja sin comprobar de dónde salen los números es
decoración. Aquí **todo** lector de datos verifica el sidecar `*.sha256` antes de
devolver una sola fila, y aborta si no coincide. Si alguien regenera un CSV sin
regenerar su sidecar, las figuras dejan de producirse — que es lo que se quiere.

Ninguna función de este módulo genera aleatoriedad, escribe en `resultados/` ni
consume la banda de semillas reservada `[2 000 000 – 2 999 999]`.
"""

from __future__ import annotations

import hashlib
import pathlib

import numpy as np
import pandas as pd

RESULTADOS = pathlib.Path(__file__).resolve().parents[1] / "resultados"

# Umbrales congelados antes de ver datos. No se recalculan aquí: se citan.
#
# El contrato que gobierna el experimento de representaciones —que es el que se
# dibuja en fig02— es `emergencia/P1a_contrato_representaciones_alternativas_d2.md`,
# NO el del gate de altura. Ambos coinciden en el `0.80`, y por eso la confusión
# pasó desapercibida (auditoría 032, hallazgos 1 y 2).
#
# Los dos umbrales viven en EJES DISTINTOS y no son intercambiables:
#   correlación de Pearson       -> cualifica si bootstrap95_lower >= 0.80  (§ :146)
#                                -> aparcada FUERTE si bootstrap95_upper < 0.50 (§ :156)
#   mediana del error relativo   -> cualifica si bootstrap95_upper <= 0.30  (§ :145)
# El `0.30` NO es un umbral de correlación y no debe dibujarse sobre ese eje.
GATE = 0.80             # correlación exigida para preregistrar un cociente
APARCADO_FUERTE = 0.50  # correlación por debajo de la cual la representación se aparca
UMBRAL_ERROR_RELATIVO = 0.30  # eje distinto: mediana del error relativo absoluto

# Valores impresos por los ejecutables deterministas ya auditados. Se usan SOLO
# como control: las figuras los recalculan desde el CSV sellado y abortan si no
# los reproducen. Fuente: emergencia/p1a_count_volume_canal_sigma_m_d2.py.
RHO_MAX_SELLADO = {
    (64, "FUTURE"): 0.5680, (64, "PAST"): 0.5681,
    (96, "FUTURE"): 0.5315, (96, "PAST"): 0.5439,
    (128, "FUTURE"): 0.5482, (128, "PAST"): 0.5349,
}
# emergencia/p1a_count_volume_techo_apriete_d2.py
FACTOR_MAX_APRIETE = 1.000017   # techo de cualquier apriete de F_relax por arriba
FACTOR_NECESARIO = 1.17         # factor mínimo que se necesitaba para servir de algo
# emergencia/P1a_count_volume_canal_sigma_m_d2.md §6 (retractación)
RHO_MAX_UB_BN = (0.83, 0.86)    # el "techo" en el que se creyó durante meses


def _verificar(nombre: str) -> pathlib.Path:
    """Devuelve la ruta del artefacto tras comprobar su SHA-256 contra el sidecar."""
    ruta = RESULTADOS / nombre
    sidecar = RESULTADOS / (nombre + ".sha256")
    if not ruta.exists():
        raise FileNotFoundError(f"falta el artefacto sellado: {ruta}")
    if not sidecar.exists():
        raise FileNotFoundError(f"falta el sidecar: {sidecar}")
    esperado = sidecar.read_text().split()[0]
    obtenido = hashlib.sha256(ruta.read_bytes()).hexdigest()
    if esperado != obtenido:
        raise ValueError(
            f"SHA-256 no coincide para {nombre}:\n"
            f"  sidecar  {esperado}\n"
            f"  fichero  {obtenido}\n"
            "El artefacto ha cambiado sin resellarse. No se dibuja."
        )
    return ruta


def leer(nombre: str) -> pd.DataFrame:
    return pd.read_csv(_verificar(nombre))


def disponibilidad() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Estados del selector de cobertura: enumeración exacta y Monte Carlo."""
    return leer("p1a_enumeracion_exacta_d2.csv"), leer("p1a_monte_carlo_d2.csv")


def representaciones() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Métricas agregadas y las 46 532 filas de intervalo de la cuarta muestra."""
    return (leer("p1a_representaciones_metricas_d2.csv"),
            leer("p1a_representaciones_intervalos_d2.csv"))


def anova_sigma_m(intervalos: pd.DataFrame, n: int, side: str) -> dict:
    """Descomposición ANOVA de un factor de la duración latente sobre `m`.

    Ésta es la figura entera del canal, en cuatro líneas. Dentro de un estrato
    `(n, side)` condicionado a la selección, el canal observable es `sigma(m)`
    (Lemas 1–3 de `P1a_count_volume_canal_sigma_m_d2.md`), y `COUNT_VOLUME` es una
    biyección creciente de `m`. Luego la mejor correlación alcanzable por
    *cualquier* función de la observación es exactamente

        rho_max = sqrt(SSB / SST),

    una identidad finito-muestral: no hay iid, ni bootstrap, ni modelo detrás.

    `SST` se calcula directamente sobre las observaciones y la descomposición se
    **verifica**, no se impone — igual que en el ejecutable auditado.
    """
    d = intervalos[(intervalos["n"] == n) & (intervalos["side"] == side)]
    y = d["latent_duration"].to_numpy()
    m = d["interval_size"].to_numpy()
    grand = y.mean()
    sst = float(((y - grand) ** 2).sum())
    ssb = ssw = 0.0
    medias = {}
    for valor in np.unique(m):
        ys = y[m == valor]
        medias[int(valor)] = float(ys.mean())
        ssb += len(ys) * (ys.mean() - grand) ** 2
        ssw += float(((ys - ys.mean()) ** 2).sum())
    hueco = abs(sst - (ssb + ssw)) / sst
    if hueco >= 1e-12:
        raise ValueError(f"la descomposición ANOVA no cierra en {(n, side)}: {hueco}")

    rho_max = float(np.sqrt(ssb / sst))
    control = RHO_MAX_SELLADO[(n, side)]
    # Tolerancia 1e-4: los valores de control están redondeados a cuatro
    # decimales en la salida del ejecutable, luego no se puede exigir más.
    if abs(rho_max - control) > 1e-4:
        raise ValueError(
            f"rho_max recalculado {rho_max:.6f} no reproduce el valor sellado "
            f"{control:.4f} en {(n, side)}. No se dibuja."
        )

    rho_obs = float(np.corrcoef(y, d["estimate_count_volume"].to_numpy())[0, 1])
    return dict(datos=d, y=y, m=m, medias=medias, K=len(medias), N=len(y),
                sst=sst, ssb=ssb, ssw=ssw, t_emp=ssw / sst,
                rho_max=rho_max, rho_obs=rho_obs)


def estratos() -> list[tuple[int, str]]:
    return [(n, s) for n in (64, 96, 128) for s in ("PAST", "FUTURE")]
