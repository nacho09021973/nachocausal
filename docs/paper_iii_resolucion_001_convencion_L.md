# Paper III — Resolución 001: convención de longitud de cadena

```text
RESOLUTION_ID=PAPER_III_R001
STATUS=APPROVED
DATE=2026-09-10
SIGNED_BY=PI
SUPERSEDES=ALL_PRIOR_L_CONVENTIONS_IN_PAPER_III
SCOPE=PAPER_III_3P1_LINE
```

Resuelve el bloqueo `G0-2` y adjudica `G0-9` de
[la auditoría de entrada](paper_iii_fase0_contrato.md) §8, resolución 1.

## 1. Texto aprobado

> En Paper III, \(L\) se define como la cardinalidad de la cadena maximal, es
> decir, el número de elementos que contiene.
>
> Para intervalos causales acotados por extremos \(p,q\), ambos extremos se
> incluyen en \(L\).
>
> Esta convención sustituye cualquier conteo previo basado en número de
> relaciones/enlaces o en la exclusión de los extremos.
>
> Los resultados históricos calculados bajo otra convención se conservan
> únicamente como artefactos de procedencia y no como evidencia física vigente.

## 2. Qué queda fijado

```text
L(cadena)      = |cadena|                      (elementos, no relaciones)
L(elem. maximal) = 1                            (no 0)
L(intervalo p,q) = 2 + #{elementos interiores}  (extremos incluidos)
N              = cardinalidad interior          (sin cambio; los extremos no son puntos sembrados)
```

La convención coincide con la del estimador sellado
(`nachocausal/estimator.py:47`, `Lfut[e] = 1 + max(...)`), con la de la pierna
intervalar (`dev/explore_3p1_bg_reference.py:53`) y con la del enunciado de
Brightwell–Gregory tal como lo fija la fuente local: *«An n-chain is a chain
with n elements […] The length of a path is its number of elements»*
(`biblioteca/derived-md/Dynamics_of_Causal_Sets_arXiv_gr-qc0212064.md:178`),
medida sobre *«the longest chain connecting x and y»* (idem `:249`).

Mantener `N` como cardinalidad interior conserva la identidad
`rho · Vol = N` exactamente, de modo que la normalización de Brightwell–Gregory
`L/(rho V)^{1/4}` y la `L/N^{1/4}` que reportan las notas siguen coincidiendo
sin aproximación.

## 3. Efecto sobre los artefactos existentes

La resolución **no genera datos**. Sobre lo ya comprometido se separa en dos:

### 3.1 Restatable por aritmética de procedencia

La pierna intervalar guarda las `Ls` crudas por semilla, luego aplicar la
convención firmada es un desplazamiento de `+2` sobre enteros ya comprometidos.
Verificado en `dev/verify_3p1_phase0_contract.py`, sección `[J]`:

| Pierna | pendiente global, convención derogada | pendiente global, **firmada** | dispersión de `L/N^(1/4)` |
|---|---|---|---|
| precisión, 8 semillas | 0.2835 | **0.2552** | +9.4 % → **+4.7 %** |
| base, 3 semillas | 0.2902 | **0.2516** | +17.9 % → **+8.4 %** |

Las diez filas de ambas piernas quedan **dentro** de la banda rigurosa
`1.8555 ≤ m₄ ≤ 2.5296`. Bajo la convención derogada, tres caían fuera de la
cota inferior — que es lo que decidió la cuestión.

En la pierna de caja `⟨L⟩` es lineal, luego `⟨L⟩` firmado `= ⟨L⟩` previo `+ 1`
es aritmética exacta sobre el agregado guardado:

| Pendiente | derogada | **firmada** | esperado |
|---|---|---|---|
| `d log⟨L⟩_all / d log ρ` | 0.3161 | **0.2450** | 1/4 |
| `d log⟨L⟩_all / d log⟨V⟩_all` | 0.3106 | **0.2407** | 1/4 |
| `d log⟨L⟩_min / d log ρ` | 0.3195 | **0.2788** | 1/4 — línea base no válida, `G0-4` |
| `d log⟨L⟩_min / d log⟨V⟩_min` | 0.3005 | **0.2622** | 1/4 — línea base no válida, `G0-4` |

### 3.2 No restatable

`median_R_min`. El artefacto guarda la mediana de `L⁴/V`, no las `L` por
elemento, y la mediana de `(L+1)⁴/V` no es función de la mediana de `L⁴/V`.
Exige reejecución. Toda cifra de `R` queda, por la última cláusula del texto
firmado, como artefacto de procedencia sin estatus de evidencia.

## 4. Consecuencia de alcance — `G0-10`, nuevo

Bajo la convención firmada, **todas las pendientes del canal no restringido
caen sobre 1/4 dentro del suelo de ruido del propio diseño**:

```text
pierna intervalar   0.2552   y   0.2516
pierna de caja      0.2450   (|0.2450 - 0.25| = 0.0050)
suelo de ruido      0.0179   (el exponente exactamente conocido sale 1.0179 en vez de 1)
```

La premisa sobre la que la hoja de ruta formula la pregunta de la Fase 1 — «los
valores existentes muestran `L/N^{1/4}` creciente y una pendiente efectiva
cercana a 0.29, no 0.25» — **deja de estar sostenida** en el canal no
restringido. No es que la corrección de tamaño finito se haya medido y salga
nula: es que la desviación que motivaba medirla era el desfase de convención.

Lo que sigue vivo:

- la dispersión residual de `+4.7 %` en la pierna de precisión, que podría ser
  corrección de tamaño finito genuina y no está caracterizada;
- `m₄` sigue **acotado, no conocido**, luego una curva de `L/N^{1/4}` frente a
  `N` no puede separar constante de transitorio sin parametrización previa;
- las pendientes restringidas a minimales, que siguen desviadas (0.2788,
  0.2622) y que son exactamente las que `G0-4` muestra medidas contra una línea
  base que no se cumple.

**Esto obliga a re-escopar la pregunta de la Fase 1, y eso es decisión del PI,
no del auditor.** La resolución 1 no la re-escopa por sí sola.

## 5. Restricción de secuenciación — obligatoria

`G0-7` («nada certifica los JSON contra sus generadores») sólo puede cerrarse
reejecutando los generadores **tal como están** y comprobando que reproducen los
JSON comprometidos. Editar un generador para aplicar esta resolución antes de
esa corrida destruye la comprobación de forma permanente.

```text
ORDEN OBLIGATORIO:
  1. reproducir   — correr los generadores actuales, verificar contra los JSON  -> cierra G0-7
  2. convertir    — aplicar R001 a dev/explore_3p1_scale_calibration.py:94
  3. reejecutar   — nueva corrida bajo la convención firmada                    -> cierra G0-1, G0-5
```

Por eso los generadores **no se han tocado** en esta iteración. El verificador
detecta la violación y la reporta como deuda firmada pendiente, no como
regresión:

```text
python3 dev/verify_3p1_phase0_contract.py
  STRUCTURAL CHECKS:  ALL PASS
  SIGNED-CONVENTION:  1 violation(s) of Resolution 1
  EXPECTED_UNTIL=PHASE_1_BOX_LEG_REEXECUTION
  exit 2
```

Códigos de salida del verificador: `0` limpio, `1` fallo estructural real,
`2` deuda de convención firmada pendiente.

## 6. Estado de los bloqueos tras esta firma

| id | Antes | Ahora |
|---|---|---|
| G0-1 | abierto | **decidido**, violación registrada, pendiente de los pasos 1–3 de §5 |
| G0-2 | abierto | **CERRADO** por esta resolución |
| G0-9 | abierto | **ADJUDICADO**: decidió G0-2 y la firma ratificó su conclusión |
| G0-5 | abierto | cifras de `R` **derogadas** a procedencia; medición pendiente de reejecución |
| G0-3, G0-4, G0-6, G0-8 | abiertos | abiertos — requieren las resoluciones 3–6, sin firmar |
| G0-7 | abierto | abierto, y ahora con orden de ejecución obligatorio (§5) |
| G0-10 | — | **nuevo**: la pregunta de la Fase 1 necesita re-escopado |

```text
GATE_0=BLOCKED   (8 bloqueos abiertos; 1 violación de convención firmada pendiente)
```

La resolución 1 no abre la Fase 1. Cierra un bloqueo, adjudica otro, deroga las
cifras de `R`, y abre uno nuevo de alcance.
