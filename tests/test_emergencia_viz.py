"""Pruebas de los guardarraíles de las figuras de `emergencia/viz/`.

Estas figuras no producen ciencia nueva: leen artefactos sellados. Su único valor de
integridad son los controles que abortan el dibujo, y un control que no se prueba es
decoración. Aquí se prueba que **saltan**, y en el caso del predicado de aparcamiento,
que salta en las **dos** direcciones: falso positivo (decir «aparcada» cuando el
contrato dice que no) y falso negativo (decir «no aparcada» cuando el contrato dice
que sí).

El falso negativo es el que motivó estas pruebas: hasta la auditoría 033 el código
usaba `max(sup IC95) < 0.50` sobre los seis estratos, que **implica** la regla del
contrato pero no es equivalente a ella. Sobre la muestra sellada ambas coinciden; el
caso `test_..._falso_negativo_del_atajo` es exactamente el que las separa.
"""

from __future__ import annotations

import pathlib
import sys

import pandas as pd
import pytest

_RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_RAIZ / "emergencia" / "viz"))

import datos  # noqa: E402


def _fila(n: int, side: str, sup_corr: float, inf_are: float,
          representacion: str = "X") -> dict:
    """Una fila de métricas con lo mínimo que mira el predicado del contrato."""
    return {
        "representation": representacion,
        "n": n,
        "side": side,
        "pearson_bootstrap95_high": sup_corr,
        "median_are_bootstrap95_low": inf_are,
    }


def _tabla(filas: list[dict]) -> pd.DataFrame:
    return pd.DataFrame(filas)


# --------------------------------------------------------------- contrato literal

def test_umbrales_no_se_han_movido() -> None:
    """Los umbrales son del contrato congelado; si cambian, es un cambio de ciencia."""
    assert datos.GATE == 0.80
    assert datos.APARCADO_FUERTE == 0.50
    assert datos.APARCADO_ERROR_RELATIVO == 0.50
    assert datos.UMBRAL_ERROR_RELATIVO == 0.30


def test_aparcada_por_el_primer_disyunto() -> None:
    """Todos los lados con `sup(IC95 rho) < 0.50`: aparcada."""
    filas = [_fila(n, lado, 0.40, 0.10)
             for n in (64, 96, 128) for lado in ("PAST", "FUTURE")]
    assert datos.aparcada_fuerte(_tabla(filas), "X") is True


def test_aparcada_por_el_segundo_disyunto() -> None:
    """Correlación alta en todos los lados, pero el error relativo la aparca igual.

    Este caso es invisible para el atajo `max(sup) < 0.50`, que diría «no aparcada».
    """
    filas = [_fila(n, lado, 0.95, 0.80)
             for n in (64, 96, 128) for lado in ("PAST", "FUTURE")]
    assert datos.aparcada_fuerte(_tabla(filas), "X") is True


def test_no_aparcada_si_algun_n_falla_en_los_dos_lados() -> None:
    """El cuantificador es «para todo `n`»: basta que un `n` no cumpla en ninguno."""
    filas = [_fila(n, lado, 0.40, 0.10)
             for n in (64, 96) for lado in ("PAST", "FUTURE")]
    filas += [_fila(128, "PAST", 0.70, 0.10), _fila(128, "FUTURE", 0.70, 0.10)]
    assert datos.aparcada_fuerte(_tabla(filas), "X") is False


def test_aparcada_con_un_solo_lado_por_n_es_suficiente() -> None:
    """«al menos un lado» — el otro puede incumplir sin deshacer el aparcamiento."""
    filas = []
    for n in (64, 96, 128):
        filas.append(_fila(n, "PAST", 0.40, 0.10))    # cumple
        filas.append(_fila(n, "FUTURE", 0.70, 0.10))  # no cumple
    assert datos.aparcada_fuerte(_tabla(filas), "X") is True


def test_el_atajo_daba_un_falso_negativo_y_el_predicado_no() -> None:
    """El caso exacto que separa el atajo del contrato (auditoría 033, hallazgo 2).

    `max(sup) = 0.70 > 0.50`, luego el atajo diría «no aparcada»; pero cada `n` tiene
    un lado por debajo de `0.50`, luego el contrato dice «aparcada».
    """
    filas = []
    for n in (64, 96, 128):
        filas.append(_fila(n, "PAST", 0.45, 0.10))
        filas.append(_fila(n, "FUTURE", 0.70, 0.10))
    tabla = _tabla(filas)

    atajo = tabla["pearson_bootstrap95_high"].max() < datos.APARCADO_FUERTE
    assert not bool(atajo)                                 # lo que decía el atajo
    assert datos.aparcada_fuerte(tabla, "X") is True       # lo que dice el contrato


def test_representacion_ausente_es_error_no_falso() -> None:
    """Una representación que no está no puede devolver «no aparcada» en silencio."""
    with pytest.raises(ValueError):
        datos.aparcada_fuerte(_tabla([_fila(64, "PAST", 0.4, 0.1)]), "NO_EXISTE")


# --------------------------------------------- terminales sellados y guardarraíles

def test_los_terminales_sellados_se_reproducen() -> None:
    """`HEIGHT_WIDTH` aparcada, `COUNT_VOLUME` no — el registro sellado."""
    metricas, _ = datos.representaciones()
    assert datos.aparcada_fuerte(metricas, "HEIGHT_WIDTH") is True
    assert datos.aparcada_fuerte(metricas, "COUNT_VOLUME") is False


def test_el_guardarrail_de_fig02_salta_con_terminales_falsos() -> None:
    """Falso positivo: si el umbral se moviera, la figura debe negarse a dibujar."""
    import fig02_el_gate

    original = datos.APARCADO_FUERTE
    try:
        datos.APARCADO_FUERTE = 0.60   # ahora COUNT_VOLUME saldría «aparcada»
        with pytest.raises(ValueError, match="terminales de aparcamiento"):
            fig02_el_gate.dibujar()
    finally:
        datos.APARCADO_FUERTE = original


def test_el_guardarrail_sha256_salta(tmp_path: pathlib.Path) -> None:
    """Un artefacto regenerado sin resellar no se dibuja."""
    nombre = "p1a_representaciones_metricas_d2.csv"
    (tmp_path / nombre).write_bytes(
        (datos.RESULTADOS / nombre).read_bytes() + b" ")
    (tmp_path / f"{nombre}.sha256").write_bytes(
        (datos.RESULTADOS / f"{nombre}.sha256").read_bytes())

    original = datos.RESULTADOS
    try:
        datos.RESULTADOS = tmp_path
        with pytest.raises(ValueError, match="SHA-256 no coincide"):
            datos.leer(nombre)
    finally:
        datos.RESULTADOS = original


def test_anova_reproduce_el_ejecutable_auditado() -> None:
    """`rho_max` recalculado debe reproducir el valor sellado en los seis estratos."""
    _, intervalos = datos.representaciones()
    for estrato in datos.estratos():
        a = datos.anova_sigma_m(intervalos, *estrato)
        assert abs(a["rho_max"] - datos.RHO_MAX_SELLADO[estrato]) <= 1e-4
        assert a["rho_obs"] <= a["rho_max"]


def test_el_recuento_del_titulo_de_fig06_se_verifica() -> None:
    """11 etapas, 7 fases, 3 del ramal; y el control salta si deja de ser cierto."""
    import fig06_mapa_del_fracaso

    _, numeros = fig06_mapa_del_fracaso.dibujar()
    assert numeros["etapas dibujadas"] == 11

    fuente = (_RAIZ / "emergencia" / "viz" / "fig06_mapa_del_fracaso.py").read_text()
    inyectada = fuente.replace(
        '        ("§18", "El canal es',
        '        ("Fase 7", "etapa fantasma", "x", CERRADO, ""),\n'
        '        ("§18", "El canal es', 1)
    assert inyectada != fuente, "la inyección de prueba ya no encaja con el fichero"

    espacio: dict = {"__file__": str(_RAIZ / "emergencia" / "viz" /
                                     "fig06_mapa_del_fracaso.py")}
    exec(compile(inyectada, "fig06_inyectada", "exec"), espacio)
    with pytest.raises(ValueError, match="no describe el diagrama"):
        espacio["dibujar"]()
