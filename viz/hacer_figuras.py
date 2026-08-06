"""Genera todas las figuras y vuelca los números que aparecen en ellas.

Punto de entrada único y reproducible:

    python3 viz/hacer_figuras.py

Cada figura fija su propia semilla, así que dos ejecuciones dan bytes idénticos.
Los números que se imprimen son los mismos que van impresos en los paneles: si
alguno cambia, la figura y el pie de figura del manuscrito han dejado de coincidir.
"""

from __future__ import annotations

import pathlib
import sys

AQUI = pathlib.Path(__file__).parent
sys.path.insert(0, str(AQUI))

import fig01_diccionario          # noqa: E402
import fig02_escala_invisible     # noqa: E402
import fig03_teleologia           # noqa: E402
import fig04_pared_de_la_caja     # noqa: E402
import fig05_lo_recuperable       # noqa: E402

SALIDA = AQUI / "salida"


def main():
    SALIDA.mkdir(exist_ok=True)
    print("=" * 72)

    fig01_diccionario.dibujar(SALIDA / "fig01_diccionario.png")
    print("fig01  diccionario continuum ↔ orden")

    _, discrepancias = fig02_escala_invisible.dibujar(SALIDA / "fig02_escala_invisible.png")
    print(f"fig02  escala invisible          discrepancias de orden = {discrepancias}"
          "   (debe ser 0)")

    fig03_teleologia.dibujar(SALIDA / "fig03_teleologia.png")
    print("fig03  teleología                 parche idéntico verificado en ambas continuaciones")

    _, c_t, c_r, c_banda = fig04_pared_de_la_caja.dibujar(SALIDA / "fig04_pared_de_la_caja.png")
    print(f"fig04  pared de la caja           corr(|J+|,t) = {c_t:+.3f}   "
          f"corr(|J+|,r) = {c_r:+.3f}   corr en banda = {c_banda:+.3f}")

    _, brecha, sd = fig05_lo_recuperable.dibujar(SALIDA / "fig05_lo_recuperable.png")
    print(f"fig05  lo recuperable             |rs=1 − rs=7| máx = {brecha:.4f}   "
          f"sd típica = {sd:.4f}   (la brecha debe quedar por debajo de la sd)")

    print("=" * 72)
    print(f"figuras en {SALIDA}")


if __name__ == "__main__":
    main()
