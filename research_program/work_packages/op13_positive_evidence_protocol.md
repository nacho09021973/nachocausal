# OP-1.3 — Protocolo de evidencia positiva por testigo acotado

**Estado:** `THEORY_DRAFT / FIXED_SAMPLE_DEFAULT / NO_EXECUTION_AUTHORIZED`

**Revisiones autorizadas:**
`docs/comite/comite_decision_027_phase1-theory-package-first-review.md` §8-§11 y
`docs/comite/comite_decision_028_phase1-theory-package-second-review.md` §8-§11 y
`docs/comite/comite_decision_029_phase1-theory-package-third-review.md` §8-§11 y
`docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md` §8-§11;
sign-off Nacho / PI, 2026-07-15.

## 1. Objeto certificado

Para dos leyes `P,Q` sobre el mismo espacio de posets observados y un testigo preespecificado
`f:Omega->[0,1]`,

```text
TV(P,Q) >= |E_P f - E_Q f|.
```

La desigualdad certifica separacion estadistica en la direccion positiva. No certifica por si sola
que `f` localice el target fisico ni que un poset individual determine una geometria.

## 2. Prueba de la desigualdad testigo

Para `0<=f<=1`, la representacion por capas da

```text
E_P f - E_Q f = integral_0^1 [P(f>t)-Q(f>t)] dt.
```

Cada diferencia absoluta esta acotada por `TV(P,Q)`; integrar sobre un intervalo de longitud uno
prueba el resultado. La misma prueba muestra que un error TV `epsilon` en una ley generadora cambia
la esperanza de cualquier testigo `[0,1]` como maximo en `epsilon`.

## 3. Certificado confirmatorio de muestra fija

Para cada celda confirmatoria `j=1,...,J`, se congelan:

- leyes pretendidas `P_j,Q_j`, canal, `n`, masa, patch y alternativa;
- leyes realmente generadas `tilde_P_j,tilde_Q_j`;
- testigo `f_j` y su hash;
- numeros independientes de replicas `m_Pj,m_Qj`;
- presupuesto `alpha_j>0`, con `sum_j alpha_j <= alpha_total`;
- cotas deterministas certificadas
  `TV(P_j,tilde_P_j)<=epsilon_Pj` y `TV(Q_j,tilde_Q_j)<=epsilon_Qj`.

Se muestrean IID

```text
X^P_{j,1},...,X^P_{j,m_Pj} ~ tilde_P_j,
X^Q_{j,1},...,X^Q_{j,m_Qj} ~ tilde_Q_j,
```

con streams independientes salvo dependencia declarada y cubierta por otra prueba. Las medias
Monte Carlo `mu_hat_tilde_Pj,mu_hat_tilde_Qj` estiman las esperanzas bajo las leyes generadas.
Hoeffding para variables `[0,1]` da radios

```text
r_Pj = sqrt(log(4/alpha_j)/(2 m_Pj)),
r_Qj = sqrt(log(4/alpha_j)/(2 m_Qj)).
```

La union de las dos colas de cada media falla con probabilidad a lo sumo `alpha_j`; la union sobre
todas las celdas falla con probabilidad a lo sumo `alpha_total`. Por tanto,

```text
TV_lower_j = max(
  0,
  |mu_hat_tilde_Pj-mu_hat_tilde_Qj|
    - r_Pj - r_Qj
    - epsilon_Pj - epsilon_Qj
)
```

es simultaneamente una cota inferior para `TV(P_j,Q_j)` con cobertura al menos `1-alpha_total`.
La derivacion usa primero los intervalos para las esperanzas bajo `tilde_P_j,tilde_Q_j` y despues
`|E_P f-E_tilde_P f|<=epsilon_Pj` y su analogo para `Q`.

Este certificado es conservador pero auditable, no requiere enumerar posets y no tiene el techo
`n<=8` de la suma exhaustiva.

## 4. Seleccion del testigo

Se permiten exactamente dos rutas:

### Ruta A — testigo congelado

`f_j` se define sin mirar ninguna replica confirmatoria. Codigo, parametros y transformaciones se
sellan antes del run.

### Ruta B — desarrollo/confirmacion separados

El testigo puede elegirse adaptativamente con seeds y replicas de desarrollo. Despues se congela su
hash y se evalua una sola vez sobre replicas confirmatorias independientes. Condicionalmente al
testigo congelado, la cobertura anterior sigue siendo valida.

Durante desarrollo, la regla de seleccion solo puede consumir identidad de generador y estadisticas
order-only producidas por candidatos definidos sin embedding. `h_M`, expansiones, coordenadas,
etiquetas por elemento y perdidas geometricas pueden aparecer en un diagnostico separado, pero no
decidir promocion, features, orientacion, frontera o abstencion. Antes de promocionar `f` se
registran seeds de desarrollo, espacio de busqueda, informacion disponible, regla de seleccion,
dependencias, criterio de promocion y hash de todas las transformaciones. Omitir uno activa
`FAILED_DEVELOPMENT_PROVENANCE`.

Usar las mismas replicas para seleccionar y certificar activa
`ADAPTIVE_SELECTION_UNCONTROLLED`, salvo que exista una cota uniforme demostrada sobre toda la
clase de testigos.

## 5. Multiplicidad

Una celda `j` es la tupla completa

```text
(f, n, geometria P, geometria Q, patch, canal, alternativa, target auxiliar).
```

Cambiar cualquiera de esos campos crea otra celda y consume presupuesto `alpha_j`. Se permite
Bonferroni ponderado preespecificado. No se permite informar solo la mejor masa, el mejor `n` o el
mejor patch sin incluir esa busqueda en `J`.

## 6. Error del generador

El contrato exige una de estas salidas:

1. `EXACT_GENERATOR`: `tilde_P_j=P_j`, `tilde_Q_j=Q_j` y predicado causal exacto;
2. `BOUNDED_GENERATOR_ERROR(epsilon)`: prueba externa de las dos cotas TV deterministas de §3;
3. `GENERATOR_ERROR_NOT_BOUNDED`: abstencion obligatoria.

Con punto flotante, declarar que los errores son pequenos no es una cota. Debe existir aritmetica
certificada, margen causal que haga imposible cambiar una relacion, o auditoria que produzca
`epsilon`. Comparar dos implementaciones sin una referencia certificada es un diagnostico, no una
cota TV.

Antes de cualquier confirmacion, un manifest completo registra como minimo: hashes de codigo,
generador, testigo y transformaciones; lista exhaustiva de celdas `J`; versiones de entorno y RNG;
derivacion de seeds y bandas disjuntas; `m_Pj,m_Qj,alpha_j,epsilon_Pj,epsilon_Qj`; `N_grid`,
`Delta_alt`, `eta`; reglas de abstencion; y tiempos de inicio/fin. Ausencia de cualquier campo emite
`INCOMPLETE_CONFIRMATORY_MANIFEST` antes de consumir seeds.

## 7. Parada y ley de encendido

La opcion por defecto es muestra fija. No se mira `TV_lower` para decidir cuando parar.

Una parada secuencial requiere reemplazar Hoeffding fijo por una confidence sequence valida en todo
tiempo, con regla y presupuesto congelados. La referencia primaria candidata es Howard, Ramdas,
McAuliffe y Sekhon, arXiv:1810.08240. Hasta instanciar y probar esa frontera en el protocolo:

```text
SEQUENTIAL_STOPPING = FORBIDDEN
```

Para una rejilla finita preespecificada `N_grid`, y cotas simultaneas sobre toda la rejilla,

```text
n_star(Delta_alt;eta) = min {n in N_grid: TV_lower_f(n,Delta_alt) >= eta}.
```

Si no existe cruce se emite `NO_CROSSING_IN_GRID`; no se extrapola. Como las cotas finitas pueden
no ser monotonas, cualquier requisito de persistencia en `n` debe congelarse como otra regla antes
de datos.

## 8. Separacion no equivale a recoverability

Para conectar el testigo con un reconstructor se exige ademas:

1. target continuo y salida discreta de OP-1.1;
2. perdida congelada, computable solo en scoring;
3. prueba o validacion de que `f` es funcion de esa salida/perdida, no solo un clasificador de dos
   generadores;
4. controles que separen horizonte de patch, volumen, sector temporal y artefactos numericos.

Un `TV_lower>0` con un estadistico de cardinalidad puede distinguir masas en `order+number` y seguir
sin localizar ninguna frontera. Ese caso es `TARGET_WITNESS_MISMATCH`, no recovery.

## 9. Terminales y condiciones FAIL

```text
POSITIVE_EVIDENCE_PROTOCOL_PROVED
ADAPTIVE_SELECTION_UNCONTROLLED
FAILED_DEVELOPMENT_PROVENANCE
GENERATOR_ERROR_NOT_BOUNDED
INCOMPLETE_CONFIRMATORY_MANIFEST
INTERRUPTED_CONFIRMATORY_RUN
NO_VALID_POSITIVE_CERTIFICATE
TARGET_WITNESS_MISMATCH
NO_CROSSING_IN_GRID
```

Para cualquier futura instancia, los terminales de reporte tienen la siguiente precedencia total
y determinista cuando varias condiciones se cumplen simultaneamente:

```text
INCOMPLETE_CONFIRMATORY_MANIFEST
  > FAILED_DEVELOPMENT_PROVENANCE
  > ADAPTIVE_SELECTION_UNCONTROLLED
  > GENERATOR_ERROR_NOT_BOUNDED
  > INTERRUPTED_CONFIRMATORY_RUN
  > TARGET_WITNESS_MISMATCH
  > NO_VALID_POSITIVE_CERTIFICATE
  > NO_CROSSING_IN_GRID
  > POSITIVE_EVIDENCE_PROTOCOL_PROVED
```

El primer terminal aplicable en esta cadena es el unico terminal principal publicado; las demas
condiciones verdaderas se conservan como diagnosticos secundarios. El terminal de autor
`POSITIVE_EVIDENCE_PROTOCOL_PROVED` certifica solo el esquema matematico y no convierte una futura
corrida en PASS cientifico.

El terminal positivo requiere simultaneamente:

- prueba de la cota;
- independencia o control uniforme de seleccion;
- presupuesto de multiplicidad completo;
- muestreo fijo, o confidence sequence ya instanciada;
- error generador exacto o acotado;
- abstenciones no coercionadas.

La cadena anterior sustituye cualquier precedencia parcial: en particular, resuelve sin discrecion
los fallos simultaneos de adaptacion, provenance y error de generador. Ningun terminal contractual
consume el significado de una no separacion.

La matematica del certificado fijo queda cerrada como esquema condicional en este documento. La
satisfaccion de esos campos por un generador y testigo concretos pertenece a una futura spec; no
queda autorizada ninguna eleccion concreta ni puede heredarse retrospectivamente de exploraciones.

```text
OP_1_3_AUTHOR_TERMINAL = POSITIVE_EVIDENCE_PROTOCOL_PROVED
IMPLEMENTATION_READINESS = PENDING_GENERATOR_AND_WITNESS_SPEC
```

## 10. Fuentes y anclajes

- Hoeffding, *Probability inequalities for sums of bounded random variables*, JASA 58 (1963),
  DOI 10.1080/01621459.1963.10500830. `[UNVERIFIED_LOCAL_SNAPSHOT]`
- Howard et al., *Time-uniform, nonparametric, nonasymptotic confidence sequences*,
  arXiv:1810.08240; solo para una futura extension secuencial. `[UNVERIFIED_LOCAL_SNAPSHOT]`
- Cota inferior y limites de claim: `docs/claim_grammar.md:273-338`.
- Teorema de dos puntos, direccion negativa:
  `research_program/work_packages/wp4_two_point_theorem.md:81-124`.
