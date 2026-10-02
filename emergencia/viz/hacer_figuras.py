"""Genera las seis figuras e imprime los números que van dentro de ellas.

Punto de entrada único:

    PYTHONDONTWRITEBYTECODE=1 python3 emergencia/viz/hacer_figuras.py

Todo lo que se dibuja sale de artefactos sellados cuyo SHA-256 se verifica antes de
leerlos, o se recalcula desde ellos y se contrasta contra la salida de un ejecutable
ya auditado. No hay datos estocásticos nuevos, no se toca `resultados/`, no se
consume la banda de semillas reservada `[2 000 000 – 2 999 999]` y no se afirma
recuperabilidad en ninguna parte.

Los números que imprime son los que aparecen impresos en los paneles. Si cambian,
la figura y el texto que la cita han dejado de estar de acuerdo.
"""

from __future__ import annotations

import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))

import estilo                        # noqa: E402
import fig01_disponibilidad          # noqa: E402
import fig02_el_gate                 # noqa: E402
import fig03_canal_sigma_m           # noqa: E402
import fig04_anatomia_del_error      # noqa: E402
import fig05_seleccion_y_estabilidad  # noqa: E402
import fig06_mapa_del_fracaso        # noqa: E402

FIGURAS = [
    ("fig01_disponibilidad", fig01_disponibilidad),
    ("fig02_el_gate", fig02_el_gate),
    ("fig03_canal_sigma_m", fig03_canal_sigma_m),
    ("fig04_anatomia_del_error", fig04_anatomia_del_error),
    ("fig05_seleccion_y_estabilidad", fig05_seleccion_y_estabilidad),
    ("fig06_mapa_del_fracaso", fig06_mapa_del_fracaso),
]


def main() -> int:
    for nombre, modulo in FIGURAS:
        fig, numeros = modulo.dibujar()
        ruta = estilo.guardar(fig, nombre)
        print(f"\n{ruta}")
        for clave, valor in numeros.items():
            print(f"    {clave:46s} {valor}")
    print(f"\n{len(FIGURAS)} figuras en {estilo.SALIDA}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
