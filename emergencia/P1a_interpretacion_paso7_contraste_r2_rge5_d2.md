# P1a — Paso 7: interpretación del contraste R=2 vs R≥5 y enlace con la descomposición orbital

ESTADO = INTERPRETACIÓN_POST_HOC (lectura de artefactos; ningún cálculo nuevo)
FECHA = 2026-08-27
CAMPAÑA = `POST_HOC_EXPLORATORY_R2_VS_RGE5_MECHANISTIC_CONTRAST`
TERMINAL DEL INSTRUMENTO = `R2_RGE5_COMBINATORIAL_CONTRAST_COMPLETED`
INCIDENTE PREVIO = `P1a_incidente_implementacion_recomposicion_layout_d2.md`

Artefactos usados, con sidecars auditados (cadena 1–6 PASS, suite `11 passed`,
cero skipped):

| artefacto | sha256 |
|---|---|
| `p1a_r2_vs_rge5_mechanistic_contrast_summary_d2.csv` | `fafa7a1be958362d…3566dc80` |
| `p1a_r2_vs_rge5_mechanistic_contrast_long_d2.csv` | `62cb93c8265f19db…4d9c178b` |
| `p1a_r2_vs_rge5_mechanistic_contrast_resumen.json` | `95ec8cc471a85977…bc06e983` |
| `p1a_orbital_multiplicity_summary_d2.csv` (campaña previa) | `a9e8a76d1329cc93…dac6f641` |

---

## 1. Veredicto

Etiqueta emitida bajo la trinaria forzada del protocolo:

```
SUPPORTED_CONTINUING_TREND
```

**Traducción al registro — es la lectura que gobierna, no la etiqueta:**

> **`SUPPORTED_PERSISTENT_SEPARATION_AT_N40`** — separación persistente en el
> control `n=40`. **No** hay evidencia de tendencia asintótica ni de
> monotonía en `n`.

La etiqueta disponible más cercana importaba una monotonía que los datos **no**
sostienen. Se separan por tanto dos afirmaciones distintas:

- **no respaldada:** localización/atenuación del rasgo al llegar a `n=40`;
- **tampoco demostrada:** continuación monotónica con `n`.

Lo observado es **persistencia**, y sobre la forma en `n` del fenómeno
—creciente, saturante, no monótona o con estructura adicional en 22–24— estos
tres puntos no deciden.

---

## 2. Lo que refuta y lo que **no** refuta

**Queda refutada** la hipótesis fuerte: que *la separación misma* entre R=2 y
R≥5 sea un fenómeno localizado en la ventana 22–24 que se desvanezca al crecer
`n`. En 4 de 6 observables el efecto adimensional en `n=40` es igual o mayor.

**No queda refutada** la existencia de una **estructura especial en 22–24
superpuesta a un fondo persistente**. `secondary_score` tiene precisamente su
extremo en `n=24` ($d=-0.970$) y vuelve en `n=40` al nivel de `n=22`
($-0.888$ frente a $-0.882$, IC95 solapados). Que el extremo caiga en 24 es
compatible con estructura local; no es evidencia en contra.

*(Corrección explícita: en una lectura anterior este extremo en 24 se usó como
evidencia contra la localización. Era incorrecto — descarta un rasgo centrado
en 22, no un rasgo en la ventana.)*

---

## 3. Persistencia, no tendencia — los números

Cohen $d$, adimensional (los `delta` crudos están confundidos con la escala:
`mu_R2` de `primary_score` va de 3.71 a **6.58** entre `n=22` y `n=40`):

| observable | $d$(22) | $d$(24) | $d$(40) | forma |
|---|---|---|---|---|
| `n_maximizers` | +2.94 | +2.84 | **+3.84** | mayor en 40, IC disjunto |
| `n_automorphisms` | −0.069 | −0.045 | −0.006 | decae; IC de 40 cruza 0 |
| `primary_score` | −0.745 | −0.815 | −0.814 | **se estabiliza** 24→40 |
| `secondary_score` | −0.882 | **−0.970** | −0.888 | extremo en 24, vuelve |
| `mean_orbit_size` | −0.005 | +0.004 | −0.005 | nulo en los tres |
| `max_orbit_size` | +0.224 | **+0.240** | +0.194 | baja en 40; IC solapan |

Solo `n_maximizers` es monótonamente mayor en el control. `primary_score` se
estabiliza, `secondary_score` y `max_orbit_size` **bajan** en 40. Eso es
persistencia con forma no monótona, no una tendencia.

Solapamientos declarados: `mean_orbit_size` contiene 0 en los tres tamaños;
`n_automorphisms` en `n=40` contiene 0 ($d$ IC95 `[−0.031,+0.023]`);
`max_orbit_size` solapa en los tres; `primary_score` 24 y 40 indistinguibles;
`secondary_score` 22 y 40 indistinguibles.

---

## 4. Enlace con la descomposición orbital previa

La campaña previa (`E_n`, `U_n^\star`, `H_n`, `H_tie_n`, `Sbar_n_tie`) **sí
exhibe un rasgo localizado en 22–24**, en los observables que su propio contrato
designa como portadores de la información no trivial:

| n | `U_n^star` | `Sbar_n_tie` | IC95 `Sbar_tie` | `H_tie_n` | `P(R≥5\|E)` |
|---|---|---|---|---|---|
| 20 | 0.4819 | 1.0106 | [1.0069,1.0147] | 1.3721 | 0.0655 |
| 22 | **0.4742** ← mín | 1.0318 | [1.0278,1.0359] | 1.4354 | 0.0734 |
| 24 | 0.4800 | **1.0398** ← máx | [1.0359,1.0438] | **1.4604** | **0.0761** |
| 26 | 0.4884 | 1.0312 | [1.0272,1.0352] | 1.4400 | 0.0726 |
| 30 | 0.5058 | 1.0156 | [1.0112,1.0198] | 1.3989 | 0.0656 |
| 40 | 0.5505 | 0.9622 | [0.9585,0.9661] | 1.2404 | 0.0438 |

`U_n^\star` alcanza su **mínimo observado en la malla** en `n=22`
(IC95 `[0.4710,0.4774]`, disjunto del de `n=20`), y `Sbar_n_tie` su **máximo
observado** en `n=24`, con IC95 disjunto del de `n=26` y apenas tangente al de
`n=22`. Después, decaimiento monótono hasta caer por debajo del nivel de `n=20`
ya en `n=34`.

**Consistencia verificable entre campañas.** Los tamaños de grupo de la campaña
nueva se recuperan exactamente de la previa vía `P(R≥5|E)·E_n·N`:

```
n=22:  0.0734 × 0.9286 × 100000 = 6 816   ✓
n=24:  0.0761 × 0.9662 × 100000 = 7 351   ✓
n=40:  0.0438 × 1.0000 × 100000 = 4 383   ✓
```

Es el control `PRIOR_COUNTS_REPRODUCED = PASS` de la campaña nueva. Las dos
campañas operan sobre la **misma partición exacta**.

### La misma historia combinatoria desde dos observables

Las dos campañas **no se contradicen: miden cosas distintas y encajan**.

- La previa mide **cómo se reparte la masa de probabilidad** entre valores de
  `R`. Ahí el rasgo **sí es local**: la competencia entre candidatos es máxima
  en 22–24 (mínimo de unicidad, máxima entropía residual, máxima fracción R≥5)
  y se relaja después.
- La nueva mide, **condicionado a caer en R=2 o en R≥5**, cuán distintos son los
  descriptores. Ahí la separación **no es local**: sobrevive a `n=40`.

Lectura conjunta: **`n=22` no es la escala donde nace y muere el obstáculo. Es
un punto donde cambia la competencia relativa dentro de un obstáculo que
sobrevive a tamaños bastante mayores.** Lo localizado es la *asignación de masa*;
lo persistente es la *distinción cualitativa* del régimen R≥5 cuando ocurre.

**Caveat honesto.** La campaña nueva **no reproduce por sí sola** el extremo de
22–24: `secondary_score` y `max_orbit_size` alcanzan su máximo $|d|$ en 24, pero
`n_maximizers` alcanza ahí su **mínimo**. Los tres no apuntan en la misma
dirección. La evidencia de localización proviene de la campaña previa; la nueva
es en gran medida **muda** sobre la localización, y decisiva solo sobre la
persistencia.

---

## 5. Lo que estos datos **no** permiten concluir

- Nada sobre `n<20`, `n>40`, ni sobre los tamaños no muestreados.
- `n=22` es **mínimo observado de `U_n^\star` en la malla**, y `n=24` **máximo
  observado de `Sbar_n_tie` en la malla** — nunca escalas críticas continuas.
- La no-monotonía del conteo R≥5 (6 816 → 7 351 → 4 383) **no** se lee como pico
  en la campaña nueva: es composición, no uno de los seis observables congelados,
  y no lleva IC en ese artefacto. Su respaldo con IC está en la campaña previa.
- El colapso de `EMPTY` (7 140 → 3 384 → **1**) marca un cambio de régimen de
  composición entre 22 y 40 que **no está caracterizado** por este diseño.
- `n_automorphisms` se observa compatible con cero **en `n=40`**; no se concluye
  anulación asintótica.
- «Entropía residual» es el nombre operacional de `E[ln R]`. **No** se identifica
  con entropía termodinámica ni causal.
