"""Three preregistered static figures for the orbital-multiplicity profile."""

from __future__ import annotations

import csv
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from emergencia import p1a_large_n_orbital_baseline_d2 as baseline  # noqa: E402
from emergencia import p1a_orbital_multiplicity_d2 as multiplicity  # noqa: E402

import estilo  # noqa: E402


PHASE = multiplicity.PHASE
SUMMARY_PATH = multiplicity.RESULTS_DIR / multiplicity.SUMMARY_CSV_FILENAME
LONG_PATH = multiplicity.RESULTS_DIR / multiplicity.LONG_CSV_FILENAME
JSON_PATH = multiplicity.RESULTS_DIR / multiplicity.JSON_FILENAME
N_VALUES = multiplicity.N_VALUES
CCDF_THRESHOLDS = (2, 3, 4, 5, 6, 8, 10, 15, 20)
OUTPUT_NAMES = (
    "fig12_orbital_multiplicity_composition",
    "fig13_orbital_multiplicity_residual_entropy",
    "fig14_orbital_multiplicity_tie_ccdf",
)


def _inputs() -> tuple[list[dict[str, str]], dict[int, list[dict[str, str]]], dict]:
    for path in (SUMMARY_PATH, LONG_PATH, JSON_PATH):
        baseline._verify_sidecar(path)
    with SUMMARY_PATH.open(newline="", encoding="utf-8") as handle:
        summary = [
            row
            for row in csv.DictReader(handle)
            if row["method"] == "MONTE_CARLO_REPRODUCTION"
        ]
    with LONG_PATH.open(newline="", encoding="utf-8") as handle:
        long_rows = [
            row
            for row in csv.DictReader(handle)
            if row["method"] == "MONTE_CARLO_REPRODUCTION"
        ]
    payload = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    summary.sort(key=lambda row: int(row["n"]))
    by_n: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in long_rows:
        by_n[int(row["n"])].append(row)
    if tuple(int(row["n"]) for row in summary) != N_VALUES:
        raise RuntimeError("figure input does not contain the frozen scientific grid")
    if any(row["PHASE"] != PHASE for row in summary + long_rows):
        raise RuntimeError("figure input has wrong phase metadata")
    if payload.get("phase") != PHASE:
        raise RuntimeError("multiplicity summary has wrong phase metadata")
    if any(value != "PASS" for key, value in payload["controls"].items() if key != "BACKEND_FAILURES"):
        raise RuntimeError("multiplicity figure received a failed scientific control")
    if payload["controls"]["BACKEND_FAILURES"] != "0":
        raise RuntimeError("multiplicity figure received backend failures")
    for row in summary:
        total = (
            float(row["U_n_star"])
            + float(row["P_R_2_given_E"])
            + float(row["P_R_3_4_given_E"])
            + float(row["P_R_ge_5_given_E"])
        )
        if not math.isclose(total, 1.0, abs_tol=1e-12):
            raise RuntimeError("composition categories do not sum to one")
    return summary, by_n, payload


def _footer(fig, source: str) -> None:
    estilo.nota_al_pie(
        fig,
        f"PHASE={PHASE} · {source} (SHA-256 verificado) · 100 000 permutaciones por n · evidencia finita",
    )


def figure_composition(summary: list[dict[str, str]]):
    estilo.use_style()
    fig, ax = plt.subplots(figsize=(11.4, 6.4))
    n_values = [int(row["n"]) for row in summary]
    series = (
        (r"$R=1$", "U_n_star", estilo.BLUE, ""),
        (r"$R=2$", "P_R_2_given_E", estilo.ORANGE, "//"),
        (r"$R=3$–$4$", "P_R_3_4_given_E", estilo.PURPLE, ".."),
        (r"$R\geq5$", "P_R_ge_5_given_E", estilo.GREEN, "xx"),
    )
    bottom = np.zeros(len(summary), dtype=float)
    for label, field, color, hatch in series:
        values = np.asarray([float(row[field]) for row in summary])
        ax.bar(
            n_values,
            values,
            bottom=bottom,
            width=1.55,
            color=color,
            edgecolor="white",
            linewidth=0.7,
            hatch=hatch,
            label=label,
        )
        bottom += values
    ax.annotate(
        r"$n=22$ · mínimo observado de $U_n^\star$ en la malla",
        xy=(22, 0.995),
        xytext=(24.0, 0.955),
        ha="left",
        va="top",
        fontsize=8.2,
        color=estilo.GREY,
        bbox={"boxstyle": "round,pad=0.22", "fc": "white", "ec": estilo.GREY, "alpha": 0.94},
        arrowprops={"arrowstyle": "-|>", "color": estilo.GREY, "lw": 1.0},
    )
    ax.set_xlabel("tamaño del poset $n$")
    ax.set_ylabel(r"probabilidad condicionada a $M\ne\varnothing$")
    ax.set_xticks(n_values)
    ax.set_ylim(0, 1)
    ax.set_title("Composición de la multiplicidad orbital del máximo", loc="left", pad=24)
    ax.text(
        0,
        1.015,
        "Categorías exhaustivas de $p_n(r)$; EMPTY queda fuera del denominador",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=9,
        color=estilo.GREY,
    )
    ax.legend(ncol=4, loc="upper center", bbox_to_anchor=(0.5, -0.13))
    _footer(fig, multiplicity.SUMMARY_CSV_FILENAME)
    fig.subplots_adjust(left=0.09, right=0.985, top=0.90, bottom=0.22)
    return fig


def _errorbar(ax, summary, *, field, color, marker, label, fill):
    x = np.asarray([int(row["n"]) for row in summary])
    y = np.asarray([float(row[field]) for row in summary])
    low = np.asarray([float(row[f"{field}_ci95_low"]) for row in summary])
    high = np.asarray([float(row[f"{field}_ci95_high"]) for row in summary])
    ax.errorbar(
        x,
        y,
        yerr=np.vstack((y - low, high - y)),
        color=color,
        marker=marker,
        mfc=color if fill else "white",
        mec=color,
        mew=1.2,
        ms=6,
        lw=1.8,
        capsize=2.5,
        label=label,
    )


def figure_entropy(summary: list[dict[str, str]]):
    estilo.use_style()
    fig, ax = plt.subplots(figsize=(10.6, 6.2))
    _errorbar(
        ax,
        summary,
        field="Sbar_n",
        color=estilo.BLUE,
        marker="o",
        label=r"$\bar S_n=E[\ln R\mid M\ne\varnothing]$",
        fill=True,
    )
    _errorbar(
        ax,
        summary,
        field="Sbar_n_tie",
        color=estilo.ORANGE,
        marker="s",
        label=r"$\bar S_{n,\mathrm{tie}}=E[\ln R\mid R\geq2]$",
        fill=False,
    )
    ax.axvline(22, color=estilo.GREY, ls="--", lw=1.3)
    ax.text(
        22.25,
        0.985,
        r"mínimo observado de $U_n^\star$ en la malla",
        rotation=90,
        ha="left",
        va="top",
        fontsize=8.2,
        color=estilo.GREY,
        transform=ax.get_xaxis_transform(),
    )
    ax.set_xlabel("tamaño del poset $n$")
    ax.set_ylabel(r"media de $\ln R$  (log natural)")
    ax.set_xticks([int(row["n"]) for row in summary])
    ax.set_title("Entropía residual operacional de la multiplicidad", loc="left", pad=24)
    ax.text(
        0,
        1.015,
        "Barras: bootstrap percentil 95% · definición operacional, no entropía física",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=9,
        color=estilo.GREY,
    )
    ax.legend(loc="upper right")
    _footer(fig, multiplicity.SUMMARY_CSV_FILENAME)
    fig.subplots_adjust(left=0.10, right=0.985, top=0.90, bottom=0.13)
    return fig


def _ccdf_matrix(by_n: dict[int, list[dict[str, str]]]) -> np.ndarray:
    matrix = np.zeros((len(N_VALUES), len(CCDF_THRESHOLDS) + 1), dtype=float)
    for i, n in enumerate(N_VALUES):
        q = {
            int(row["r"]): float(row["q_given_tie"])
            for row in by_n[n]
            if row["q_given_tie"] != "NA"
        }
        for j, threshold in enumerate(CCDF_THRESHOLDS):
            matrix[i, j] = sum(value for r, value in q.items() if r >= threshold)
        matrix[i, -1] = sum(value for r, value in q.items() if r > 20)
    if not np.allclose(matrix[:, 0], 1.0, atol=1e-12):
        raise RuntimeError("tie CCDF does not start at one")
    if np.any(np.diff(matrix[:, :-1], axis=1) > 1e-12):
        raise RuntimeError("tie CCDF is not nonincreasing")
    return matrix


def figure_tie_ccdf(by_n: dict[int, list[dict[str, str]]], payload: dict):
    estilo.use_style()
    matrix = _ccdf_matrix(by_n)
    fig, ax = plt.subplots(figsize=(12.0, 6.8))
    image = ax.imshow(matrix, aspect="auto", cmap="Blues", vmin=0, vmax=1)
    labels = [rf"$R\geq{threshold}$" for threshold in CCDF_THRESHOLDS] + [r"$R>20$"]
    ax.set_xticks(range(len(labels)), labels=labels, rotation=38, ha="right")
    ax.set_yticks(range(len(N_VALUES)), labels=[str(n) for n in N_VALUES])
    ax.set_xlabel("umbral de multiplicidad entre casos competitivos")
    ax.set_ylabel("tamaño del poset $n$")
    ax.set_title("CCDF de órbitas ganadoras condicionada a rivalidad", loc="left", pad=24)
    ax.text(
        0,
        1.015,
        r"Cada celda es $P(R\geq t\mid R\geq2)$; la última conserva explícitamente la cola $R>20$",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=9,
        color=estilo.GREY,
    )
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            value = matrix[i, j]
            color = "white" if value >= 0.55 else "black"
            label = f"{value:.3f}" if value >= 0.001 else "<.001" if value > 0 else "0"
            ax.text(j, i, label, ha="center", va="center", fontsize=7.2, color=color)
    colorbar = fig.colorbar(image, ax=ax, pad=0.015)
    colorbar.set_label("probabilidad de cola")
    maximum = payload["observed_extrema"]["maximum_R_observed"]
    ax.text(
        0.995,
        -0.20,
        f"máximo observado en la malla: R={maximum}",
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=8.2,
        color=estilo.GREY,
    )
    _footer(fig, multiplicity.LONG_CSV_FILENAME)
    fig.subplots_adjust(left=0.09, right=0.94, top=0.90, bottom=0.25)
    return fig


def _save_new(fig, name: str) -> Path:
    estilo.SALIDA.mkdir(exist_ok=True)
    path = estilo.SALIDA / f"{name}.png"
    if path.exists():
        raise FileExistsError(f"refusing to overwrite {path}")
    fig.savefig(
        path,
        metadata={"Phase": PHASE, "Claim": "finite-n post-hoc descriptive only"},
    )
    plt.close(fig)
    return path


def main() -> int:
    paths = [estilo.SALIDA / f"{name}.png" for name in OUTPUT_NAMES]
    if any(path.exists() for path in paths):
        raise FileExistsError("refusing to overwrite an orbital-multiplicity figure")
    summary, by_n, payload = _inputs()
    outputs = (
        _save_new(figure_composition(summary), OUTPUT_NAMES[0]),
        _save_new(figure_entropy(summary), OUTPUT_NAMES[1]),
        _save_new(figure_tie_ccdf(by_n, payload), OUTPUT_NAMES[2]),
    )
    for output in outputs:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
