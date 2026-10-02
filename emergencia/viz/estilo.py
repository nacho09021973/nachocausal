"""Estilo compartido: se reutiliza el de `viz/style.py` sin duplicarlo.

Las figuras de la línea `emergencia` son diagnósticas, no pedagógicas, pero deben
verse como las del manuscrito: misma paleta Okabe–Ito, mismo tipo grande.
"""

from __future__ import annotations

import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "viz"))

from style import (  # noqa: E402,F401
    BLUE, ORANGE, GREEN, RED, PURPLE, SKY, YELLOW, GREY, use_style,
)

SALIDA = pathlib.Path(__file__).resolve().parent / "output"

# Colores con significado fijo en toda la serie: si cambian, cambian en un sitio.
COLOR_REPR = {"HEIGHT_ONLY": GREY, "COUNT_VOLUME": BLUE, "HEIGHT_WIDTH": ORANGE}
COLOR_SELECTOR = {"COVERAGE": ORANGE, "MIN_ONLY": PURPLE, "MIN_COVERAGE_LEX": GREEN}
COLOR_GATE = RED
COLOR_TECHO = "#7B1FA2"


def guardar(fig, nombre: str) -> pathlib.Path:
    SALIDA.mkdir(exist_ok=True)
    ruta = SALIDA / f"{nombre}.png"
    fig.savefig(ruta)
    return ruta


def nota_al_pie(fig, texto: str) -> None:
    """Línea de procedencia al pie: qué artefacto sellado produjo la figura."""
    fig.text(0.005, 0.005, texto, fontsize=7.2, color=GREY, va="bottom", ha="left")
