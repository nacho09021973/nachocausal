"""Núcleo geométrico y de orden para las figuras pedagógicas del manuscrito de límites.

Sin dibujo: aquí sólo vive la geometría de Schwarzschild 1+1, el sprinkling y el
orden causal.  Los ficheros `figNN_*.py` importan de aquí y sólo dibujan.

Convenios y por qué son exactos
-------------------------------
Métrica de Schwarzschild 1+1 en coordenadas `(t, r)`, exterior `r > rs`:

    g = -(1 - rs/r) dt^2 + (1 - rs/r)^{-1} dr^2

Dos hechos que hacen que todo lo de abajo sea exacto y no aproximado:

1. `det g = -1`, luego la forma de volumen es `dt dr`.  El sprinkling de Poisson
   condicionado a `N = n` es, por tanto, **n puntos iid uniformes en el rectángulo
   `(t, r)`** — sin jacobiano ni pesos.  Cualquier peso en el código sería un error.

2. Con la coordenada tortuga `r* = r + rs·ln|r/rs - 1|`, la métrica es
   `(1 - rs/r)·(-dt^2 + dr*^2)`: conformemente plana.  Un factor conforme no cambia
   el orden causal, luego el orden es **exactamente** el orden de Minkowski en
   `(t, r*)`, es decir el orden producto en las coordenadas nulas `u = t - r*`,
   `v = t + r*`.  No hay que integrar geodésicas.

Dilatación (Teorema 3.1)
------------------------
`Phi_s(t, r) = (s·t, s·r)` lleva el modelo de radio de horizonte `rs` al de `s·rs`.
En tortuga:

    r*(s·r ; s·rs) = s·r + s·rs·ln|s·r/(s·rs) - 1| = s·(r + rs·ln|r/rs - 1|)
                   = s · r*(r ; rs)

luego `(u, v) -> (s·u, s·v)`: una dilatación de las nulas, que preserva el orden
producto **elemento a elemento**.  Ésta es la razón de que el Teorema 3.1 sea una
igualdad exacta y no una aproximación, y `check_dilation_identity` la verifica.
"""

from __future__ import annotations

import numpy as np

__all__ = [
    "tortoise",
    "null_coords",
    "sprinkle_exterior",
    "causal_matrix",
    "dilate",
    "check_dilation_identity",
    "hasse_edges",
    "layer_of",
    "future_volume",
    "comparable_fraction",
]


# --------------------------------------------------------------------------- #
# Geometría
# --------------------------------------------------------------------------- #

def tortoise(r, rs):
    """Coordenada tortuga `r* = r + rs·ln|r/rs - 1|`.  Exterior: `r > rs`."""
    r = np.asarray(r, dtype=float)
    if np.any(r <= rs):
        raise ValueError("tortoise() sólo está definida aquí en el exterior r > rs")
    return r + rs * np.log(r / rs - 1.0)


def null_coords(t, r, rs):
    """Nulas `(u, v) = (t - r*, t + r*)`.  El orden causal es el orden producto."""
    rstar = tortoise(r, rs)
    return t - rstar, t + rstar


def sprinkle_exterior(rs, t_range, r_range, n, rng):
    """`n` puntos iid según la forma de volumen en el rectángulo `(t, r)`.

    Como `det g = -1`, la forma de volumen es `dt dr` y el muestreo es uniforme.
    Devuelve `(t, r)`, cada uno de forma `(n,)`.
    """
    if r_range[0] <= rs:
        raise ValueError("el parche debe vivir en el exterior: r_lo > rs")
    t = rng.uniform(t_range[0], t_range[1], size=n)
    r = rng.uniform(r_range[0], r_range[1], size=n)
    return t, r


# --------------------------------------------------------------------------- #
# Orden causal
# --------------------------------------------------------------------------- #

def causal_matrix(t, r, rs):
    """Matriz booleana `rel[i, j] = (i precede estrictamente a j)`.

    `i < j` sii `u_i <= u_j` y `v_i <= v_j` y `i != j` (orden producto en nulas).
    """
    u, v = null_coords(t, r, rs)
    le = (u[:, None] <= u[None, :]) & (v[:, None] <= v[None, :])
    np.fill_diagonal(le, False)
    return le


def dilate(t, r, rs, s):
    """`Phi_s`: devuelve `(s·t, s·r, s·rs)` — el mismo conjunto en el modelo dilatado."""
    return s * np.asarray(t, float), s * np.asarray(r, float), s * rs


def check_dilation_identity(t, r, rs, s):
    """Verifica que `Phi_s` preserva el orden **elemento a elemento**.

    Devuelve `(identicas, n_discrepancias)`.  Es la comprobación numérica del
    mecanismo del Teorema 3.1: no comprueba el teorema (que es sobre leyes), sino
    que esta realización concreta induce literalmente el mismo poset etiquetado.
    """
    rel_a = causal_matrix(t, r, rs)
    t_b, r_b, rs_b = dilate(t, r, rs, s)
    rel_b = causal_matrix(t_b, r_b, rs_b)
    diff = int(np.sum(rel_a != rel_b))
    return diff == 0, diff


# --------------------------------------------------------------------------- #
# Utilidades de poset
# --------------------------------------------------------------------------- #

def hasse_edges(rel):
    """Aristas de cobertura (reducción transitiva) de una relación de orden estricta."""
    n = rel.shape[0]
    cover = rel.copy()
    for i in range(n):
        for j in range(n):
            if not rel[i, j]:
                continue
            # i < j deja de ser cobertura si existe k con i < k < j
            if np.any(rel[i] & rel[:, j]):
                cover[i, j] = False
    return [(i, j) for i in range(n) for j in range(n) if cover[i, j]]


def layer_of(rel):
    """Altura de cada elemento: longitud de la cadena más larga que termina en él."""
    n = rel.shape[0]
    layer = np.zeros(n, dtype=int)
    order = np.argsort(rel.sum(axis=0))  # menos predecesores primero
    for _ in range(n):
        changed = False
        for j in order:
            preds = np.nonzero(rel[:, j])[0]
            new = 0 if preds.size == 0 else int(layer[preds].max()) + 1
            if new != layer[j]:
                layer[j] = new
                changed = True
        if not changed:
            break
    return layer


def future_volume(rel):
    """`|future(i)|` — cardinal del futuro estricto de cada elemento."""
    return rel.sum(axis=1)


def comparable_fraction(rel):
    """Fracción de pares no ordenados que son comparables."""
    n = rel.shape[0]
    total = n * (n - 1) // 2
    return float(rel.sum()) / total if total else 0.0
