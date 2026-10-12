# Frente 2+1D ecuatorial — fase A: el generador funciona y está muy por debajo de la parada

**Fecha:** 2026-10-12 · **Acta:** `docs/acta_frente_2p1_ecuatorial_2026-10-12.md` (firmada; fase
A autorizada) · **Código:** `dev/gen2p1_equatorial.py` · **Ejecuciones:**
`dev/2p1_phaseA_runs_2026-10-12.jsonl`, generado con
`.venv/bin/python dev/gen2p1_equatorial.py N seed` para `(2000, 1)`, `(10000, 1)` y
`(20000, 2/3/4)`.

## Qué hace

- **Sembrado:** Poisson sobre el parche del puente, `U ∈ [−1.5, 0.7]`, `V ∈ [0.35, 0.9]` y
  `φ ∈ S¹`, con densidad `∝ e^{−s(UV)}` (E1 §3), por rechazo. Las coordenadas, es decir la
  verdad de referencia, se devuelven **aparte** del orden.
- **Orden:** la regla de E1 §3. Se decide en tres etapas:
  1. la recta por debajo y Cauchy–Schwarz por encima, en todos los pares ordenados (numba);
  2. la calibración por encima, sobre la rejilla de `c`, con tablas por punto;
  3. los pares que quedan ambiguos, en torno al 1–2 % de los ordenados, se resuelven con la
     **geodésica por disparo en `(U, V)`**. Para la métrica `F(UV) dU dV` las ecuaciones son
     `U' = p` y `p' = (F'/F)(UV)·p·(U − V p)`, con `F'/F = (1 + 3/s)/(s e^s)`. Cada par se
     parametriza con la coordenada que más avanza, gracias a la simetría `U ↔ V`. Se bisecciona
     la pendiente inicial hasta alcanzar el extremo con error `< 1e-9`.

**Lo que hubo que cambiar por el camino.**
- La geodésica de `c` constante de `dev/explore_b2_calibration_band.py` fallaba en unos 465 de
  2150 pares ambiguos con `N = 2000`, todos con los dos puntos fuera del horizonte (`U < 0`). La
  familia de `c` constante con la raíz menor solo cubre una rama, y las maximizadoras de la
  región exterior pueden tener un punto de retorno. El disparo en `(U, V)` no tiene ese
  problema.
- Con `V` como parámetro, un par casi nulo con `ΔV = 0.0016` y `ΔU = 0.80` hacía la ecuación
  rígida. Se resolvió parametrizando por la coordenada que más avanza.

## Resultados

| `N` medio | semilla | `n` | relaciones | pares en etapa 3 | a `< 1e-6` de la frontera | s/realización | violaciones de transitividad | auditoría: fallos / desacuerdos |
|---|---|---|---|---|---|---|---|---|
| 2000 | 1 | 2027 | 120 557 | 2 150 | 0 | 1.3 | 0 | 0 / 0 |
| 10000 | 1 | 10104 | 2 973 812 | 52 678 | 18 | 4.7 | 0 | 0 / 0 |
| 20000 | 2 | 20046 | 11 635 976 | 205 577 | 59 | 14.6 | 0 | 0 / 0 |
| 20000 | 3 | 19840 | 11 591 883 | 203 129 | 62 | 16.0 | 0 | 0 / 0 |
| 20000 | 4 | 20030 | 11 848 493 | 210 227 | 65 | 15.5 | 0 | 0 / 0 |

**Parada del acta:** «si con `N = 10⁴` el generador no baja de una hora por realización, se
informa y se para». Tarda **4.7 s**, así que no se activa.

## Controles

- **Transitividad:** un orden causal tiene que ser transitivo. Se comprueba con `A·A ⊆ A`, y da
  0 violaciones en todas las ejecuciones.
- **Auditoría de las etapas 1–2:** 20 000 pares ya decididos en cada ejecución se recalculan
  con el disparo exacto. No hay ningún fallo de extremo ni ningún desacuerdo.
- **Coherencia de la etapa 3:** en cada par, la longitud de la geodésica tiene que quedar entre
  la recta y la cota superior, y hay una aserción que lo exige. El disparo coincide con la
  geodésica antigua, donde aquella funcionaba, hasta `1.2e-8`.
- **Mutación:** con un generador que se fía de una cota un 3 % optimista, la transitividad lo
  detecta: 638 relaciones erróneas producen 76 violaciones.
- **Pares en el filo:** hay unos 60 pares por cada `2·10⁴` puntos con
  `|dist_φ − Delta_max| < 1e-6`. Los decide el valor de la geodésica, cuya precisión es de
  `~1e-8`. Se informan; son unos `5e-6` de las relaciones.

## Límites

- **Es un generador en flotante, no un certificado.** Es la verdad de referencia del banco: su
  exactitud se apoya en los controles de arriba, no en un redondeo dirigido.
- **Que la geodésica disparada sea la maximizadora** se apoya en que llega al extremo, en que
  queda dentro de `[recta, cota superior]` y en la transitividad. No hay prueba de unicidad.
- **El parche es el del puente, por omisión.** El del banco lo fija prereg-004.
- **Semillas usadas en la fase A:** `1, 2, 3, 4, 7, 99, 12345` (estas dos últimas en
  diagnósticos). Quedan **quemadas para validación**. La banda de exploración y la virgen se
  definen en la fase B, disjuntas de estas.

## Estado

```text
FASE A (generador)   = CUMPLIDA; parada no activada (4.7 s por realización con N = 1e4)
FASE B (estimador)   = pendiente de la firma del PI (acta §9.3)
```
