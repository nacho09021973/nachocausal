"""Single audited figure for the post-hoc orbital curve refinement through n=40."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from emergencia import p1a_large_n_orbital_baseline_d2 as baseline  # noqa: E402
from emergencia import p1a_orbital_curve_refinement_d2 as refinement  # noqa: E402

import estilo  # noqa: E402


PHASE = refinement.PHASE
CSV_PATH = refinement.RESULTS_DIR / refinement.CSV_FILENAME
JSON_PATH = refinement.RESULTS_DIR / refinement.JSON_FILENAME
OUTPUT_NAME = "fig11_orbital_curve_refinement"


def _inputs() -> tuple[list[dict[str, str]], dict]:
    baseline._verify_sidecar(CSV_PATH)
    baseline._verify_sidecar(JSON_PATH)
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    with JSON_PATH.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if not rows or any(row["PHASE"] != PHASE for row in rows):
        raise RuntimeError("refinement figure received missing or wrong phase metadata")
    if payload.get("phase") != PHASE:
        raise RuntimeError("refinement summary has wrong phase metadata")
    return sorted(rows, key=lambda row: int(row["n"])), payload


def _errorbar(ax, rows, *, key, low, high, color, marker, label, linestyle="-"):
    x = [int(row["n"]) for row in rows]
    y = [float(row[key]) for row in rows]
    yerr = [
        [float(row[key]) - float(row[low]) for row in rows],
        [float(row[high]) - float(row[key]) for row in rows],
    ]
    ax.errorbar(
        x,
        y,
        yerr=yerr,
        fmt=marker,
        linestyle=linestyle,
        color=color,
        mfc="white" if marker == "s" else color,
        mec=color,
        mew=1.2,
        ms=5.5,
        capsize=2.5,
        lw=1.6,
        label=label,
        zorder=3,
    )


def draw():
    rows, payload = _inputs()
    anchors = payload["independent_anchor_comparison"]

    estilo.use_style()
    fig, (ax, zoom) = plt.subplots(
        2,
        1,
        figsize=(10.2, 8.0),
        sharex=True,
        gridspec_kw={"height_ratios": [1.15, 1], "hspace": 0.16},
    )

    series = (
        ("$E_n$ — disponibilidad", "E_hat", "E_ci95_low", "E_ci95_high", estilo.ORANGE, "^", "--"),
        ("$U_n$ — unicidad absoluta", "U_hat", "U_ci95_low", "U_ci95_high", estilo.BLUE, "o", "-"),
        ("$U_n^\\star$ — unicidad si disponible", "U_star_hat", "U_star_ci95_low", "U_star_ci95_high", estilo.PURPLE, "s", "-."),
    )
    for label, key, low, high, color, marker, linestyle in series:
        _errorbar(
            ax,
            rows,
            key=key,
            low=low,
            high=high,
            color=color,
            marker=marker,
            label=label,
            linestyle=linestyle,
        )

    _errorbar(
        zoom,
        rows,
        key="U_star_hat",
        low="U_star_ci95_low",
        high="U_star_ci95_high",
        color=estilo.PURPLE,
        marker="s",
        label="campaña de refinamiento",
    )
    zoom.scatter(
        [int(anchor["n"]) for anchor in anchors],
        [float(anchor["prior_U_star_hat"]) for anchor in anchors],
        marker="D",
        s=58,
        facecolors="white",
        edgecolors=estilo.GREY,
        linewidths=1.5,
        label="baseline anterior independiente",
        zorder=5,
    )

    ax.set_ylabel("probabilidad")
    ax.set_ylim(0.39, 1.025)
    ax.set_title(
        "Curva orbital post-hoc: refinamiento entre n=20 y n=40",
        loc="left",
        pad=26,
    )
    ax.text(
        0.0,
        1.005,
        "100 000 permutaciones uniformes independientes por tamaño · barras: Wilson 95%",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=9,
        color=estilo.GREY,
    )
    ax.legend(loc="center right")

    zoom.set_xlabel("tamaño del poset $n$")
    zoom.set_ylabel("$U_n^\\star$")
    zoom.set_xticks([int(row["n"]) for row in rows])
    zoom.set_ylim(0.455, 0.565)
    zoom.set_title("Detalle de la unicidad orbital condicionada", loc="left", fontsize=11)
    zoom.legend(loc="upper left")
    zoom.text(
        0.99,
        0.03,
        "anclas n=24,32: muestras nuevas y previas no combinadas",
        transform=zoom.transAxes,
        ha="right",
        va="bottom",
        fontsize=8.2,
        color=estilo.GREY,
    )

    estilo.nota_al_pie(
        fig,
        f"PHASE={PHASE} · {refinement.CSV_FILENAME} (SHA-256 verificado) · evidencia finita; sin ajuste asintótico",
    )
    fig.subplots_adjust(left=0.10, right=0.98, top=0.90, bottom=0.12, hspace=0.25)
    return fig


def main() -> int:
    output = estilo.SALIDA / f"{OUTPUT_NAME}.png"
    if output.exists():
        raise FileExistsError(f"refusing to overwrite {output}")
    fig = draw()
    fig.savefig(output, metadata={"Phase": PHASE, "Claim": "finite-n descriptive only"})
    plt.close(fig)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
