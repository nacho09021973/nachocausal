# Paper III — Resolución 002: reescopado de la Fase 1

```text
RESOLUTION_ID=PAPER_III_R002
STATUS=APPROVED
DATE=2026-09-10
SIGNED_BY=PI
RESOLVES=G0-10
DEPENDS_ON=PAPER_III_R001
PHASE_1_ROLE=NULL_CALIBRATION
PHASE_1_ROLE_NOT=ANOMALY_INVESTIGATION
```

Resuelve `G0-10`, abierto por la restitución de los artefactos bajo
[R001](paper_iii_resolucion_001_convencion_L.md).

## 1. Texto aprobado

> **RESOLVED — PHASE 1 RESCOPED.**
> The previously stated motivation "existing values show an effective slope near
> 0.29 rather than 0.25" is withdrawn. Under R001, the unrestricted observables
> are consistent, at the present design resolution, with the \(1/4\) asymptotic
> scaling. Phase 1 is retained only as a finite-size calibration /
> null-characterization stage for the unrestricted Minkowski 3+1 channel, prior
> to Phase 2. It is not a search for an already-observed anomalous exponent.

Pregunta revisada de la Fase 1:

> Una vez fijada R001 y certificada la procedencia, caracterizar cuánto pueden
> desviarse de la ley asintótica \(L \propto N^{1/4}\) los observables **no
> restringidos** en el rango finito de \(N\) que realmente usaremos, **sin
> asumir que existe una corrección detectable**.

## 2. Las tres consecuencias, como reglas operativas

### C1 — `1/4` es la línea base **nula**, no una expectativa

Deja de ser «el valor al que esperamos acercarnos». Cualquier resultado de la
Fase 1 se enuncia como *no se rechaza* o *se rechaza* la nula, con su resolución
declarada. Una desviación sólo cuenta si supera el suelo del propio diseño,
medido en el mismo diseño.

### C2 — `m₄` no se trata como conocido

Sólo existe la banda rigurosa `1.8555 ≤ m₄ ≤ 2.5296`. Por tanto `L/N^(1/4)` **no
identifica por sí solo** una corrección transitoria frente a una constante
desconocida: el modelo natural

```text
L / N^(1/4) = m_4 (1 + c N^(-alpha))
```

tiene tres parámetros libres y la pierna de precisión tiene cuatro puntos.
Verificado sobre los artefactos comprometidos, con el modelo de error agrupado
que exige R5: fijando `alpha` de antemano, la mejora sobre la constante es

| `alpha` fijado | `m₄` | `c` | χ² (dof 2) | Δχ² sobre la constante |
|---|---|---|---|---|
| 0.25 | 2.2586 | −0.354 | 3.77 | 1.14 |
| 0.50 | 2.2113 | −1.336 | 4.15 | 0.75 |
| 1.00 | 2.1911 | −28.37 | 4.65 | 0.26 |

Ninguna está preferida: la constante sola da χ² = 4.91 con 3 dof, y ningún
`alpha` compra más de 1.14 unidades de χ² a cambio de un parámetro. **`alpha` debe fijarse por argumento previo, no
ajustarse**, y el resultado debe reportarse condicionado a esa elección.

### C3 — las filas restringidas a minimales quedan **fuera** de la calibración principal

No pueden usarse como evidencia de desviación de `1/4` bajo la misma
parametrización que el canal `all`, porque su línea base no es la misma y no se
cumple: `⟨V⟩_min/ρ` deriva +18.2 % sobre el barrido mientras `⟨V⟩_all/ρ` es
plano. Quedan suspendidas hasta que tengan su propia línea base correcta, que es
trabajo separado y no de la Fase 1 reescopada. Es el bloqueo `G0-4`.

## 3. Estado de la nula sobre los datos existentes

Aritmética sobre artefactos comprometidos, bajo R001. Ninguna corrida nueva.
Verificado en `dev/verify_3p1_phase0_contract.py`, sección `[K]`.

### 3.1 La nula no se rechaza

| Pierna | modelo de error | χ²/dof contra constante | `m₄` ajustado |
|---|---|---|---|
| precisión, 8 semillas | `sem` individual por punto | 3.26 | 2.1572 ± 0.0144 |
| precisión, 8 semillas | **sd agrupada, 28 dof** | **1.64** | 2.1844 ± 0.0168 |
| base, 3 semillas | `sem` individual por punto | 0.95 | 2.0831 ± 0.0220 |

La tensión aparente de la primera fila **no sobrevive a un modelo de error
robusto**, y su origen es identificable:

```text
N= 2000   Ls = [11,12,12,13,14,14,12,13]   sd = 1.0607
N= 8000   Ls = [19,18,18,18,17,18,18,18]   sd = 0.5345   <-- seis de ocho idénticos
N=16000   Ls = [23,22,22,23,23,25,21,22]   sd = 1.1877
N=32000   Ls = [27,27,29,27,28,26,29,28]   sd = 1.0607
```

Con `L` entero y dispersión del orden de la unidad, la `sd` muestral de ocho
extracciones muy empatadas subestima la dispersión real. Ese único punto domina
el χ². **Consecuencia operativa: la Fase 1 no puede usar la `sem` punto a punto
como modelo de error a este número de réplicas.**

### 3.2 Las dos piernas son consistentes

Mismo generador, semillas disjuntas, `N` solapados:

| `N` | precisión | base | diferencia | σ |
|---|---|---|---|---|
| 2 000 | 2.1869 ± 0.0561 | 2.0436 ± 0.0498 | 0.1433 | 1.91 |
| 8 000 | 2.1147 ± 0.0200 | 2.0795 ± 0.0352 | 0.0352 | 0.87 |
| 16 000 | 2.1895 ± 0.0373 | 2.1339 ± 0.0513 | 0.0556 | 0.88 |

χ² conjunto 5.17 / 3 dof = 1.72. Consistentes.

### 3.3 Resolución del diseño y qué la limita

Amplitud mínima detectable a 2σ de una corrección `c·N^(-alpha)`, usando la
palanca entre los extremos del rango corrido:

| `alpha` | \|c\| detectable | efecto en `N = 2 000` |
|---|---|---|
| 0.25 | ≥ 0.719 | +10.8 % |
| 0.50 | ≥ 3.205 | +7.2 % |
| 1.00 | ≥ 114.7 | +5.7 % |

Dispersión observada sobre el rango: +4.7 %. Es decir, **el diseño actual no
alcanza a detectar una corrección del tamaño de la que se observa**, para
ninguna de las tres `alpha`.

Réplicas necesarias, con `sd` agrupada y una incertidumbre relativa actual del
1.58 % por punto:

```text
separar los extremos a 2 sigma:  sem relativa <= 1.66 %  ->  ~ 8 semillas por punto
separar los extremos a 3 sigma:  sem relativa <= 1.11 %  ->  ~17 semillas por punto
```

**La limitación del diseño es el número de réplicas, no el rango de `N`.** El
coste de la cadena es `O(N²)` mientras que el de las réplicas es lineal y
paraleliza. Una Fase 1 que persiga `N` mayores antes que réplicas gasta el
presupuesto en el eje equivocado.

## 4. Qué NO autoriza esta resolución

- No autoriza barridos. La Fase 1 sigue cerrada hasta `GATE_0`.
- No fija `alpha`, ni la parametrización, ni el número de réplicas. Fija que
  esas elecciones deben hacerse **antes** de mirar resultados nuevos, y que
  `alpha` no se ajusta.
- No reabre las filas de minimales.
- No toca el orden obligatorio de R001 §5: **reproducir → convertir →
  reejecutar**.

## 5. Efecto sobre las puertas

`GATE_1` se reformula en coherencia con la nula. La redacción anterior
(«describir empíricamente la aproximación a `L/N^{1/4}`») presuponía una
aproximación observable:

```text
GATE_1=PASS  iff la resolución del diseño está caracterizada y declarada, la nula
             1/4 se contrasta contra ella, y el resultado -- se rechace o no --
             es reproducible y estable entre convenciones y semillas
GATE_1=NULL_NOT_REJECTED  iff la nula sobrevive a la resolución alcanzada.
             Es un resultado válido y suficiente para abrir la Fase 2 como control
GATE_1=FAIL  iff falla procedencia, implementación u orden causal
```

`NULL_NOT_REJECTED` sustituye al antiguo `OPEN` como desenlace esperado. Deja de
ser un no-resultado: es la calibración que la Fase 2 necesita para poder atribuir
a la excisión cualquier diferencia que aparezca.

## 6. Bloqueos

| id | Estado |
|---|---|
| G0-10 | **CERRADO** por esta resolución |
| G0-4 | abierto, y ahora además condición previa para reabrir el canal de minimales (C3) |
| G0-1, G0-5, G0-7 | abiertos, sujetos al orden obligatorio de R001 §5 |
| G0-3, G0-6, G0-8 | abiertos; redacción exacta propuesta en [Resoluciones pendientes](paper_iii_resoluciones_pendientes.md), sin firmar |

```text
GATE_0=BLOCKED   (7 bloqueos abiertos; 1 violación de convención firmada pendiente)
```
