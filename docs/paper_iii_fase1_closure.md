# Paper III — Fase 1: cierre

```text
DOCUMENT_ID=PAPER_III_PHASE_1_CLOSURE
DATE=2026-09-10
DECIDED_BY=PI
PHASE_1_STATUS=CLOSED
PHASE_1_VERDICT=NULL_NOT_REJECTED
GATE_1=PASS
GATE_0=PASS
RESOLUTIONS=R001..R007 ALL SIGNED
NEW_RUNS=NONE
NEW_SEEDS=NONE
NEW_N=NONE
ARTIFACTS_MODIFIED=NONE
R_INTERPRETATION=DEFERRED
PHASE_2_STATUS=NOT_STARTED
PHASE_2_AUTHORIZED_NEXT=YES
```

Este documento **cierra la Fase 1 documentalmente**. No ejecuta nada, no modifica
ningún JSON científico y no inicia la Fase 2.

---

## 1. Cómo encaja `GATE_1 = PASS` en el mecanismo que el repo ya define

No se inventa semántica. `GATE_1` está definido, en la misma redacción, en
[la hoja de ruta](hoja_de_ruta_paper_iii.md) y en
[R002 §5](paper_iii_resolucion_002_reescopado_fase1.md):

```text
GATE_1=PASS  iff la resolución del diseño está caracterizada y declarada, la nula
             1/4 se contrasta contra ella, y el resultado -- se rechace o no --
             es reproducible y estable entre convenciones y semillas
GATE_1=NULL_NOT_REJECTED  iff la nula sobrevive a la resolución alcanzada.
             Es un resultado válido y suficiente para abrir la Fase 2 como control
GATE_1=FAIL  iff falla procedencia, implementación u orden causal
```

### 1.1 `PASS` y `NULL_NOT_REJECTED` no están en el mismo eje

Están escritos como un enum de tres valores, pero **no lo son**, y el propio
texto lo dice: la condición de `PASS` incluye la cláusula *«el resultado — **se
rechace o no** — es reproducible y estable»*. Si `PASS` fuese la rama «la nula se
rechaza», esa cláusula sería contradictoria consigo misma. La lectura que hace
coherente el texto congelado es la única disponible:

- **`PASS` califica el proceso**: resolución caracterizada, nula contrastada
  contra ella, resultado reproducible y estable. Es neutral respecto al desenlace.
- **`NULL_NOT_REJECTED` nombra el desenlace**: la nula sobrevivió. R002 lo llama
  «desenlace esperado» y lo declara suficiente para abrir la Fase 2 como control.

Por eso este cierre registra **los dos**, y no elige entre ellos:

```text
GATE_1          = PASS                 (el proceso cumple las tres condiciones)
PHASE_1_VERDICT = NULL_NOT_REJECTED    (el desenlace que ese proceso produjo)
```

`FAIL` no aplica: no falla procedencia, implementación ni orden causal — los dos
verificadores salen con código 0 y `GATE_0 = PASS` con cero bloqueos.

### 1.2 Las tres condiciones de `PASS`, contra evidencia

**(a) «la resolución del diseño está caracterizada y declarada».**

| magnitud | valor | dónde |
|---|---|---|
| suelo de resolución sobre una pendiente | `0.0179` | [R005](paper_iii_resolucion_005_incertidumbre.md) — el exponente exactamente conocido devuelve `1.0179` |
| incertidumbre relativa por punto | `0.97 %` | [replicación 17](paper_iii_fase1_replicacion_17.md) §6 |
| dof de la `sd` agrupada / su se relativa | `64` / `8.8 %` | idem |
| separación de extremos | `1.47 σ` | idem |
| error estadístico sobre `beta` | `0.0056` | idem §4.1 |
| amplitud mínima detectable de `c N^(−alpha)` | tabla por `alpha` | [R002 §3.3](paper_iii_resolucion_002_reescopado_fase1.md) |
| resolución del control interno sobre un exponente | `0.0030 … 0.0162` | [suelo interno](paper_iii_fase1_internal_floor.md) §5 |

**(b) «la nula 1/4 se contrasta contra ella».**

```text
M0 (constante)  chi2 = 4.6196 / 3 dof = 1.54   p = 0.202   m4 = 2.1762 +/- 0.0103, EN BANDA
beta - 1/4      = +0.0104   frente al suelo declarado 0.0179   ->  0.58x, NO lo supera
Dchi2(M0->M5)   = 3.517  ->  p = 0.0624 contra nula calibrada del propio diseno
control interno  no detecta sesgo de implementacion de signo positivo comparable
```

**(c) «el resultado — se rechace o no — es reproducible y estable entre
convenciones y semillas».**

- *Reproducible*: los tres artefactos históricos se reprodujeron **byte a byte**
  desde sus generadores (contrato §5.2); el artefacto de 17 réplicas está fijado
  por hash; las 8 réplicas compartidas entre la corrida de 8 y la de 17 son
  idénticas valor por valor (sección `[A3]` del verificador); las cifras de este
  cierre se re-derivan del JSON comprometido, no se copian.
- *Estable entre semillas*: tres conjuntos disjuntos (`21–23`, `101–108`,
  `109–117`); `chi2` conjunto base/precisión `1.24`; bootstrap sobre las 17
  réplicas; leave-one-out estable en las cuatro variantes.
- *Estable entre convenciones*: la sensibilidad al conteo de extremos se **midió**
  (`0.2835 → 0.2552`, [R001](paper_iii_resolucion_001_convencion_L.md) §3.1), se
  **resolvió por firma**, y se **impone en código**: la sección `[B]` del
  verificador comprueba que las tres implementaciones de longitud de cadena del
  repositorio cuentan vértices bajo la misma semántica. No se afirma que las
  cifras sean insensibles a la convención — lo eran, y por eso existe R001. Lo que
  es estable es el resultado bajo la convención firmada, aplicada de forma
  consistente y verificada.

---

## 2. BASELINE

```text
geometria    intervalo de Alexandrov de Minkowski 3+1, I(p,q) con tau = 1
             Vol_4 = (pi/24) tau^4 = 0.130899693899575
proceso      BINOMIAL: exactamente N puntos i.i.d. uniformes  (R003)
             = Poisson condicionado a N = n; NO es un sprinkling de Poisson
N            cardinalidad interior; rho * Vol = N exactamente
L            cardinalidad de la cadena maximal, extremos p y q INCLUIDOS  (R001)
             sobre las Ls guardadas, que son conteos interiores, eso es +2
canal        NO RESTRINGIDO. El canal de minimales sigue SUSPENDIDO por R004
observable   L / N^(1/4), y su ajuste descriptivo L = A N^beta
```

Diseño de la pierna de precisión: `N = 2000, 8000, 16000, 32000`, **17 réplicas**
por `N`, semillas `101..117`.

---

## 3. RESULTADOS PRINCIPALES

```text
m4        = 2.1762 +/- 0.0103        dentro de la banda rigurosa [1.8555, 2.5296]
M0 p      = 0.202                    chi2 = 4.6196 / 3 dof = 1.54
beta      = 0.2604                   (0.260427 sin redondear)
beta_shift= +0.0104                  (= beta - 1/4)
sd(beta)  = 0.0056
```

> **Nota de precisión.** Los informes de la replicación y del suelo interno citan
> `beta − 1/4 = +0.0105`. El valor con malla de exponente refinada es `+0.010427`,
> que redondea a `+0.0104`. La diferencia es `1·10⁻⁴`, muy por debajo de la `sd`
> del propio `beta` (`0.0056`) y del suelo del diseño (`0.0179`), y no altera
> ninguna conclusión. Este cierre registra el valor fino porque es el que el
> verificador re-deriva del artefacto.

Las cuatro cifras se re-derivan del artefacto comprometido
`dev/explore_3p1_bg_reference_precision17_results.json` bajo R001 y el modelo de
error de R005. El verificador las recalcula; no son constantes copiadas.

---

## 4. RESIDUAL

```text
beta - 1/4 = +0.0104        OPEN_DIAGNOSTIC_RESIDUAL
```

**No interpretado.** Se registra, no se borra y no se promueve.

Lo que se sabe de él, y nada más:

- es **estable**: por encima de `1/4` en tres conjuntos de semillas disjuntos y en
  las cuatro variantes leave-one-out;
- es **marginal**: `1.89 σ`, `p = 0.062` contra la nula calibrada del propio
  diseño;
- **no supera el suelo** de resolución declarado (`0.58×` de `0.0179`);
- **no es artefacto de implementación**: el control interno reproduce leyes
  finitas exactas a `1.0–1.2 σ` sobre los mismos causal sets;
- **no está explicado**.

`OPEN_DIAGNOSTIC_RESIDUAL` significa exactamente eso: ni señal, ni bloqueo.

---

## 5. CALIBRACIÓN INTERNA

Registrada en [el informe del suelo interno](paper_iii_fase1_internal_floor.md).

- `C_k` (`k = 2,3,4`) **reproduce sus leyes finitas exactas**:
  `E[C_k] = chi_k · N(N−1)···(N−k+1)`, sin corrección de tamaño finito, con
  `g_k = 1.0017 ± 0.0017`, `1.0054 ± 0.0044`, `1.0095 ± 0.0078` — a `1.0–1.2 σ`.
- **No detecta fallo del pipeline.** Sobre tres cantidades cuyo exponente
  normalizado es exactamente `0`, el pipeline devuelve valores compatibles con `0`
  y, bajo la regla ponderada, de signo **contrario** al de `beta`.
- **No decide la corrección finita de la cadena más larga.** Su resolución se
  degrada con `k` (`0.0030`, `0.0087`, `0.0162`) justo en la dirección en que se
  parece más a una cadena, y por construcción carece de corrección de tamaño
  finito, que es la magnitud que decidiría `beta`.

```text
INTERNAL_CALIBRATION = INCONCLUSIVE
```

### 5.1 Decisión epistémica del PI

**No se exige un calibrador exacto de valor-extremo antes de la Fase 2.**

Razón, registrada literalmente: la ley finita de la cadena máxima es precisamente
la cantidad desconocida que se está calibrando. Resolverla no es una precondición
proporcionada para usar Minkowski como control.

```text
EXTREME_VALUE_CALIBRATOR_REQUIRED_BEFORE_PHASE2 = NO
```

---

## 6. CLAIM CEILING tras el cierre de la Fase 1

**Permitido:**

- la nula `1/4` **no se rechaza** a la resolución alcanzada;
- Minkowski 3+1 intervalar queda **suficientemente calibrado como control de
  referencia** para comenzar la Fase 2.

**No permitido — lo que `GATE_1 = PASS` NO significa:**

```text
NO  beta demostrado igual a 1/4
NO  regimen asintotico demostrado (ni alcanzado, ni no alcanzado)
NO  correccion de tamano finito igual a cero
NO  m4 conocido exactamente  (sigue solo ACOTADO: 1.8555 <= m4 <= 2.5296)
NO  cierre teorico del problema de finite-size scaling de la cadena mas larga
NO  beta != 1/4
NO  universalidad de R;  R_INTERPRETATION = DEFERRED
NO  reapertura del canal de minimales  (suspendido por R004)
```

Siguen fuera, como ya estaban: horizontes, localización, reconstrucción de
`r = 2M`, Schwarzschild 3+1, Kerr y transferencia automática desde Paper II.

---

## 7. Lo que este cierre NO recomienda

```text
mas replicas                                    NO  (el error estadistico ya esta
                                                     por debajo del suelo del diseno)
N mayores                                       NO  (no es la limitacion)
ajustar alpha                                   NO
buscar una familia de correccion                NO  (indistinguibles; bateria de modelos)
perseguir el calibrador de valor-extremo
  antes de la Fase 2                            NO  (decision epistemica, sec. 5.1)
```

---

## 7bis. El gate puede fallar — comprobado, no afirmado

«Un guardarraíl que no puede fallar es decoración.» La sección `[L]` del
verificador se sometió a ocho mutaciones deliberadas, cada una revertida a
continuación (restauración byte a byte comprobada por hash):

| mutación | resultado |
|---|---|
| borrar este documento | `GATE_1 = BLOCKED` |
| contradecir `m4` en el bloque de resultados | `GATE_1 = BLOCKED` |
| contradecir `beta` en el bloque de resultados | `GATE_1 = BLOCKED` |
| borrar el bloque de resultados entero | `GATE_1 = BLOCKED` |
| suprimir una cláusula del claim ceiling | `GATE_1 = BLOCKED` |
| degradar el residuo de `OPEN_DIAGNOSTIC_RESIDUAL` a `SIGNAL` | `GATE_1 = BLOCKED` |
| revertir el cierre en la hoja de ruta | `GATE_1 = BLOCKED` |
| borrar el informe del suelo interno | `GATE_1 = BLOCKED` |

Las ocho salen con código `2` (puerta bloqueada), no `1` (script roto), que es la
distinción que el verificador documenta.

La primera versión de `[L]` **no** detectaba la segunda mutación: comprobaba que
la cifra apareciese *en alguna parte* del documento, y `m4 = 2.1762 +/- 0.0103`
también aparece en §1.2(b), de modo que corromper §3 dejaba pasar el gate. Se
corrigió a **leer las cifras del bloque de resultados y compararlas
numéricamente** con lo que devuelve el artefacto. Se registra porque el fallo lo
encontró el test negativo, no la lectura del código.

## 8. Cadena documental

| documento | papel |
|---|---|
| [contrato Fase 0](paper_iii_fase0_contrato.md) | `GATE_0 = PASS`, R001–R007 firmadas |
| [R002](paper_iii_resolucion_002_reescopado_fase1.md) | define `GATE_1` y reescopa la Fase 1 como calibración nula |
| [R005](paper_iii_resolucion_005_incertidumbre.md) | modelo de error y suelo del diseño |
| [R007](paper_iii_resolucion_007_estatus_R.md) | estatus de `R`; `R_INTERPRETATION = DEFERRED` |
| [batería de modelos](paper_iii_fase1_model_battery.md) | `CONSTANT_MODEL_SUFFICIENT_AT_CURRENT_RESOLUTION` |
| [replicación 17](paper_iii_fase1_replicacion_17.md) | `NULL_CALIBRATION_STABLE`; `m4`, `p`, `beta` |
| [suelo interno](paper_iii_fase1_internal_floor.md) | `INTERNAL_CALIBRATION_INCONCLUSIVE` |
| **este documento** | cierre: `PHASE_1_STATUS = CLOSED`, `GATE_1 = PASS` |

## 9. Estado tras el cierre

```text
Fase 0   CLOSED   GATE_0 = PASS
Fase 1   CLOSED   PHASE_1_VERDICT = NULL_NOT_REJECTED   GATE_1 = PASS
Fase 2   NEXT, NOT STARTED
```

La Fase 2 queda **autorizada como siguiente paso**, no iniciada. Su apertura
requiere su propio trabajo previo, tal como lo fija la hoja de ruta: derivación
geométrica de `d_obs`, prueba de que es una métrica y de que la relación causal
resultante es transitiva, verificador numérico independiente, y definición previa
de la región observada y del control Minkowski emparejado. **Nada de eso se hace
en este documento.**
