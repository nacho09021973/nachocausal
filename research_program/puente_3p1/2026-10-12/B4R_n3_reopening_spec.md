# B4-R — Reapertura de `n=3`: especificación

> **STATUS: `CLOSED — GATE_FAILED`.** Firmada (§8.1 y §8.2, 2026-10-12). La fase 0 se ejecutó y la
> compuerta de §5 **falló**: `σ_pred(128) ≈ −7.84`. B4 vuelve a `PARKED` con
> `N3_RANK_UNRESOLVED_BY_RESOLUTION`, y la fase 1 no procede
> (`dev/B4R_PHASE0_RESULT_2026-10-12.md`). Además, el control del paso 1 destapó que los números
> antiguos de B4 no corresponden a la ley `n=3` (`dev/B4_EXECUTION_WRONG_MOMENTS_2026-10-12.md`).
> Es la
> especificación de la **reapertura** de B4, que está aparcado
> (`research_program/puente_3p1/2026-09-12/B4_n3_local_identifiability_spec.md`). **No** es una
> especificación nueva de `n=3`: el objeto, el punto, la carta, el escalado, el criterio y los
> terminales son los de B4, B4.0, B4.1 y B4.3, y aquí no se cambian. Lo nuevo es la maquinaria de
> cálculo, una compuerta de viabilidad fijada **antes** de calcular nada y las reglas de parada.

**Fecha:** 2026-10-12 · **Motivo:** B3 es `B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY`
(promocionado, `5540097`), lo que según su especificación **justifica proponer** `n=3`.

---

## 1. La pregunta, sin cambios

En el punto congelado `lambda*`, el binary64 `path(0.5)`, y en la carta de B3,
`x = (v1/v0, u_in/u_out, u_in·v1)` con `v0` fijo, ¿determina la ley `n=3` la geometría
localmente?

Según B4.0, la ley `n=3` equivale exactamente a cuatro momentos:

```text
m = (rho, E[f²], E[p²], E[p f]),   f(x) = nu(J+(x) ∩ K),  p(x) = nu(J-(x) ∩ K),
q = (P_E, P_V, P_Lambda, P_C) = T m,   det T = 162   =>   rowspan Dq = rowspan Dm.
```

`Dm(x*)` es una matriz `4 × 3`. Las derivadas de forma directas de los momentos están en B4.3 §3,
y la de `rho` es la de H3.

## 2. Terminales: los de B4, sin cambios

```text
B4_STRONG_POSITIVE          rank Dm = 3: algún menor 3×3 certificado excluye cero,
                            o sigma_min(R Dm) tiene una cota inferior positiva certificada
                            => identificabilidad local completa de la familia física 3D
                            => phi reconstruible localmente
B4_PHI_FIRST_ORDER_POSITIVE rank Dm < 3 y dphi ∈ rowspan(Dm)
B4_NEGATIVE_FOR_PHI         existe v con Dm v = 0 y dphi(v) ≠ 0
B4_INCONCLUSIVE_BY_BOUNDS   la envolvente no decide
```

Con el escalado fijo de B4.1, `R = diag(1, 10⁴, 10⁴, 10⁴)` y `C = I_3`, que no se reajusta.

**Límite estructural, declarado ahora.** Con envolventes solo se puede alcanzar
`B4_STRONG_POSITIVE`. Los dos terminales que dependen de `rank Dm < 3` exigen una dependencia
**exacta**, que una envolvente no puede demostrar (B4.1: «un determinante numéricamente pequeño
no es evidencia de rango menor»). Por tanto, en esta reapertura el resultado es `STRONG_POSITIVE`
o `INCONCLUSIVE`.

## 3. Por qué reabrir: la condición de B4

B4 se aparcó con `B4_REOPEN_ONLY_IF = certified quadrature with formal remainder`, porque B4.3 no
tenía cómo encerrar las integrales anidadas de `F`, `P` y sus derivadas. Desde entonces existe
una maquinaria que **encierra** esas integrales con redondeo dirigido, auditada y usada en tres
certificados promocionados (compuerta, B2.1 y B3):
- cotas de `h` por pares de celdas, mediante la monotonía del `sup` respecto a los extremos;
- la cota de la recta por debajo, y `min(calibración, Cauchy–Schwarz)` por encima;
- pesos con envolventes de `G`;
- la capa escalar de B1.5.

**No es un resto de cuadratura en sentido estricto, sino una envolvente.** El PI tiene que
decidir (§8.1) si eso cumple la condición de reapertura. Esta especificación sostiene que sí,
porque la condición pedía cotas rigurosas de esas integrales, y eso es lo que da.

## 4. Lo que hace falta, y lo nuevo que exige

Para cada dirección de la carta `e_j` y cada momento hay que dar envolventes de las doce
entradas de `Dm`, con cota **inferior y superior**, porque los signos son mixtos. Respecto a lo
ya auditado, es nuevo:
- **`F(x)` y `P(x)` en puntos interiores, con orientación.** B2 solo necesitaba
  `H = F + P` en las caras. La retícula da las dos orientaciones por separado: `plb`/`pub`
  hacia el futuro y hacia el pasado.
- **Productos `f²`, `p²` y `f p`, integrados sobre `K`.** Para `F, P >= 0` basta con encerrar
  cada factor.
- **`DF[a]` y `DP[a]`** (B4.3 §2), que combinan pares interior–cara y llevan los signos de `a_n`.
- **Cotas inferiores de `B`, `F` y `P`.** Necesitan la tabla completa de cotas inferiores por
  pares (`plb`), que la compuerta no construía. Con `M = 128` ocupa unos 2.2 GB, igual que
  `pub`.

Cada pieza nueva lleva un kernel nuevo y se audita como tal.

## 5. Fase 0 — exploración de viabilidad (dev, sin terminal)

Antes de escribir el certificado, una exploración en flotante en `dev/`, que se puede acelerar
con la GPU según la regla del 2026-06-20. Usa **las mismas cotas por celdas que usaría el
certificado**, con el redondeo al más cercano.

1. **Valores centrales.** Las doce entradas de `Dm` con la representación nueva, en
   `M ∈ {32, 64, 128}`, junto con los valores singulares de `R·Dm` y los cuatro menores.
   Control: compararlos con `verification_b4_1_rank_certification.json`, regenerado el
   2026-10-11, cuyos valores singulares reescalados son `(147.88, 2.605, 0.03825)`. Si difieren
   por encima de la anchura de las envolventes, se para y se explica antes de seguir.
2. **Anchura.** Para cada `M`, la semianchura `E_M` de la envolvente de `R·Dm` entrada a entrada,
   y la cota predicha `σ_pred(M) = σ_min(R·Dm_centro) − ‖E_M‖_F` (Weyl).

**Compuerta de viabilidad, congelada aquí:**

```text
si  σ_pred(128) > 0               ->  Fase 1 permitida (con firma del PI, §8.3)
si  σ_pred(128) <= 0              ->  B4 vuelve a PARKED con N3_RANK_UNRESOLVED_BY_RESOLUTION
```

`M = 128` es el techo, **por memoria**, no por elección. `plb` y `pub` con `M = 128` ocupan unos
4.4 GB; con `M = 192` ocuparían unos 22 GB, más que los 15 GB de esta máquina. No se extrapola
en `M` para sortear la compuerta, ni se busca otro escalado, menor o fila.

**Expectativa, declarada antes de calcular.** Los valores regenerados dan
`σ_min(R·Dm) ≈ 0.038` frente a `σ_max ≈ 148`. Para pasar la compuerta, las filas de momentos
tendrían que estar encerradas con un error relativo de `~1e-3`–`1e-2`. La maquinaria actual
tiene, con `M = 128`, un error relativo de `~40 %` en `S` (`S_lo = 0.00137` frente al ideal
`0.0024`). **Lo más probable es que la compuerta falle.** *(Anotación posterior: los valores regenerados de
B4 resultaron no ser la ley `n=3`, como explica `dev/B4_EXECUTION_WRONG_MOMENTS_2026-10-12.md`. La
fase 0 midió `σ_min(R·Dm_centro) ≈ 7e-4`, y la compuerta falló igualmente.)* La fase 0 sirve para medirlo con
coste bajo, no para forzarlo.

## 6. Fase 1 — certificado (solo si la fase 0 pasa y el PI firma)

- Un verificador nuevo en `research_program/puente_3p1/<fecha>/`, con:
  - los kernels de la compuerta, importados sin cambios;
  - kernels nuevos para `F`/`P` orientados, `plb` completo y los términos de B4.3;
  - el control de fast-math `guard_kernels` (IR ejecutado, clausura por sobrecarga);
  - pruebas negativas.
- Una envolvente con intervalos dirigidos de las doce entradas, y después de `R·Dm`. El
  terminal es `B4_STRONG_POSITIVE` si se cumple
  `σ_min(R·Dm_centro) − ‖radio‖_F > 0` en aritmética dirigida, o si algún menor encerrado
  excluye cero. En caso contrario es `B4_INCONCLUSIVE_BY_BOUNDS`.
- Se congela y se sube **antes** de auditarlo. Se audita como los anteriores.

## 7. Guardarraíles (todos heredados de B4; ninguno se relaja)

```text
no_new_point, no_new_chart, no_new_scaling (R fijo), no_row_dropping, no_search,
no_seeds, no_monte_carlo (N3_MONTE_CARLO = NOT_AUTHORIZED), no_finite_differences,
no_n4, no_general_interval_quadrature_library
```

La fase 0 no emite ningún terminal de B4. Una fase 0 favorable **no** es evidencia de rango 3.

## 8. Firma del PI

1. **Condición de reapertura.** ¿Cumple la maquinaria de envolventes de la compuerta
   `B4_REOPEN_ONLY_IF`? **SÍ** (PI, 2026-10-12)
2. **Fase 0** autorizada, con la compuerta de §5 tal como está escrita. **SÍ** (PI, 2026-10-12)
3. **Fase 1** solo si la fase 0 pasa la compuerta, y con una firma nueva en ese momento.
   `[se firma después]`

```text
PI: Nacho Martín                  fecha: 2026-10-12   (§8.1 y §8.2)
```

## 9. Nota sobre B4.1

El texto de B4.1 cita menores (`~1e-13`) anteriores a la regeneración del 2026-10-11. Su JSON
actual da `−1.47e-11`, `7.00e-10`, `−3.42e-9` y `−3.51e-9`. Las cifras válidas son las del
JSON. Se anotará en B4.1 si se reabre.
