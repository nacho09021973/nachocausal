# P1a — Techo del apriete de `F_relax` por el lado opuesto (CV-4, ítem 2)

> **ESTADO: BORRADOR v1.0 · CV-4 ÍTEM 2 · EVALUACIÓN DETERMINISTA DE LECTURA SOBRE
> DATOS YA SELLADOS · SIN DATOS ESTOCÁSTICOS NUEVOS · VEREDICTO: VÍA DESCARTADA.**
>
> Responde a la pregunta previa exigida antes de invertir en el ítem 2: ¿cuál es el
> factor **máximo** que puede aportar la restricción del lado opuesto? Se contesta
> sin evaluar ninguna restricción concreta, con un argumento de una línea.

## 1. Criterio de decisión fijado antes de mirar el número

De `emergencia/P1a_count_volume_cota_correlacion_d2.md` §6:

```text
factor >= 1.36  -> exclusion del gate 0.80 en los seis estratos
1.17 - 1.36     -> exclusion parcial
factor < 1.17   -> abandonar esta via sin resolver w
```

## 2. Teorema CV-4.3 — techo del apriete por arriba

La restricción del lado opuesto es, estructuralmente, una cota **superior**: de
`alpha<beta<gamma<delta` (§1 de `P1a_count_volume_ley_condicionada_d2.md`) y
`k_+ = delta-gamma >= 1`, `gamma > beta`, se obtiene

```text
k_- + k_+ <= delta - alpha <= n-1,   con gamma-beta>=1  =>  k_- <= n-3,
```

y análogamente `l_- <= n-3`. Baja el techo `k,l <= n-1` a `k,l <= n-3`. No toca las
cotas inferiores `k,l >= m-1`.

**Teorema.** Sea `F_tight` cualquier subconjunto de `F_relax(m,n)` obtenido bajando
únicamente cotas superiores sobre `(k,l)`. Entonces

```text
min_{F_tight} Var(ell|s) <= Var(ell | s_min(m)),   s_min(m) = (max(2,m-1), max(2,m-1)),
```

y por tanto `B_n^tight <= E_m[ Var(ell|s_min(m)) ] =: techo_esquina`.

**Demostración.** `s_min(m)` satisface `k,l >= m-1` con igualdad y
`k+l = 2m-2 <= n+m-2` siempre que `m<=n` — cierto en todo el régimen publicado
(`m <= 43`, `n >= 64`). Luego `s_min(m) in F_relax(m,n)`, y como `F_tight` solo
elimina puntos por *exceder* cotas superiores, `s_min(m)` sobrevive a cualquier
apriete de ese tipo. El mínimo sobre un conjunto que contiene `s_min(m)` no supera
`Var(ell|s_min(m))`. `QED`

El techo es por tanto **independiente de cuán agresiva sea la restricción del lado
opuesto**: acota incluso el caso límite en que el apriete eliminara todo salvo la
esquina inferior.

## 3. Evaluación

```text
PYTHONDONTWRITEBYTECODE=1 python3 emergencia/p1a_count_volume_techo_apriete_d2.py
```

| `n` | lado | `B_n` | `B_n` con `k,l<=n-3` | `techo_esquina` | factor `n-3` | **factor máx** |
|---:|---|---:|---:|---:|---:|---:|
| 64 | futuro | 0.001102 | 0.001102 | 0.001102 | 1.000000 | 1.000004 |
| 64 | pasado | 0.001100 | 0.001100 | 0.001100 | 1.000000 | 1.000017 |
| 96 | futuro | 0.000771 | 0.000771 | 0.000771 | 1.000000 | 1.000000 |
| 96 | pasado | 0.000771 | 0.000771 | 0.000771 | 1.000000 | 1.000000 |
| 128 | futuro | 0.000598 | 0.000598 | 0.000598 | 1.000000 | 1.000000 |
| 128 | pasado | 0.000597 | 0.000597 | 0.000597 | 1.000000 | 1.000000 |

**Factor máximo alcanzable: `1.000017`.** Frente a `1.17` necesario.

## 4. Por qué el techo es exactamente `1`

Porque el `argmin` de `Var(ell|k,l)` sobre `F_relax(m,n)` **ya está en la esquina
inferior** `s_min(m)` en 72 de los 74 pares `(m,n)` que ocurren en la muestra. Las
dos excepciones (`n=64`, `m=24` y `m=25`) caen en la frontera superior
`k+l = n+m-2` y admiten un factor puntual de `1.016` y `1.047` respectivamente —
pero son `m` de cola: ponderadas por su frecuencia real en el estrato, el techo
agregado sube solo a `1.000017`.

La razón estructural: `Var(ell|k,l) = kl/(n+1)^2 - (E[sqrt(X_k)]E[sqrt(Y_l)])^2` es
pequeña en **ambos** extremos del rango de `k` — con `k` pequeño porque la escala
misma es pequeña, y con `k` cerca de `n` porque `Beta(k,n+1-k)` se concentra. El
mínimo vive en el extremo inferior, que es justo el que las cotas superiores no
tocan.

```text
CV4_ARGMIN_LIVES_AT_LOWER_CORNER = YES (con 2 excepciones numericamente irrelevantes)
```

## 5. Consecuencia: qué queda vivo y qué no

**Muerto:** apretar `F_relax` por arriba, en cualquier variante. No es que la
restricción del lado opuesto sea débil; es que **ninguna** restricción de ese tipo
puede aportar más de un factor `1.00002`. El ítem 2 queda cerrado por un argumento,
no por una evaluación cara.

**Vivo, y es el único:** subir la cota **inferior** sobre `(k,l)` — demostrar que
las formas con `k` o `l` cerca de `m-1` no pueden ganar el argmax del selector. Eso
es exactamente un argumento de selección, es decir, `w(s|m,n,side,S)` (Ruta 1,
`P1a_count_volume_ley_condicionada_d2.md` §11), o al menos una cota inferior parcial
sobre su soporte.

La decisión pendiente queda por tanto limpia: **la exclusión estructural del gate
`0.80` por esta vía pasa íntegramente por `w`, o no pasa.** No hay atajo intermedio.

## 6. Techo de afirmación

No se establece:

- que el gate `0.80` sea inalcanzable **por esta vía** (la cota superior inducida por
  `B_n` es `rho_max_ub_Bn = 0.83-0.86`, que **no** es la correlación máxima real y no
  basta para excluirlo). *Nota posterior:* el gate sí queda excluido exactamente
  sobre la muestra sellada por el cálculo directo del canal
  (`emergencia/P1a_count_volume_canal_sigma_m_d2.md`, `rho_max = 0.532-0.568`), que
  no pasa por `F_relax` ni por `B_n`. Nada de este documento queda contradicho;
- que `w` vaya a dar el factor `1.17`+ (no se ha intentado; podría no darlo);
- nada asintótico: el argumento del §2 es exacto para todo `(m,n)` con `m<=n`, pero
  la evaluación numérica cubre solo `n=64,96,128`.

## 7. Estado de control

```text
CV4_TIGHTER_FEASIBLE_SET = DONE_AND_CLOSED
CV4_ITEM2_THEOREM = PROVED (Seccion 2)
CV4_ITEM2_FACTOR_OPPOSITE_SIDE_CONCRETE = 1.000000
CV4_ITEM2_FACTOR_CEILING_ANY_UPPER_TIGHTENING = 1.000017
CV4_ITEM2_VERDICT = ABANDON_ROUTE_WITHOUT_RESOLVING_W
CV4_GATE_0.80_STRUCTURALLY_EXCLUDED_BY_BOUND = NO (sin cambio)
CV4_ONLY_REMAINING_ROUTE = LOWER_BOUND_ON_(k,l) == w
CV4_W_RESOLVED = NO (sigue aparcado)
CV4_NEW_STOCHASTIC_DATA_GENERATED = NO
NOVELTY_CERTIFIED = NO
```

## 8. Artefactos

```text
emergencia/p1a_count_volume_techo_apriete_d2.py
```

Determinista, solo lectura. Reutiliza `bound_for_m` y `var_ell_given_shape` del
script ya auditado `p1a_count_volume_cota_resolucion_evaluacion_d2.py`. No escribe en
`resultados/`, no genera aleatoriedad.
