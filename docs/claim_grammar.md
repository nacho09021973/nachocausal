# Gramática de claims

**Unidad:** `OP-0.2`

**Estado:** `REVISION_1 / COMMITTEE_RECONVENE_PENDING / DOCUMENT_ONLY / NO_NEW_RESULT`

**Fuentes de programa:** snapshot `726c8c1` y matriz OP-0.1 auditada por
`docs/auditor/auditor_report_013_op01-survival-matrix.md`.

**Revisión autorizada:** `docs/comite/comite_decision_024_op02-claim-grammar-adoption.md` §9;
sign-off Nacho / PI, 2026-07-15. Hash del borrador bloqueado:
`08a34ea4bc699ba58717718c3ff621a4de740fb0ff4b66c1939360b4affa9c91`.

## 1. Función normativa

Este documento fija el vocabulario admisible para textos futuros de `nachocausal`. No añade un
teorema, una medición ni una propiedad a ningún estimador. Una frase escrita como objetivo,
requisito o plantilla sigue siendo un objetivo, requisito o plantilla hasta que exista evidencia
con el nivel declarado.

Todo claim científico nuevo debe identificar, en la misma sección:

1. dimensión, familia geométrica o clase generativa y clase física relevante;
2. carta, patch físico, truncaciones y regla de extensión;
3. canal (`fixed_n`, `order+number` u otro) y secuencia de experimentos;
4. target continuo, mecanismo físico y salida discreta;
5. pérdida y contrato `embedding-only-scores`;
6. orientación temporal o acción de dualidad;
7. dirección de la garantía (`TV <=`, `TV >=`, riesgo, cobertura u otra);
8. régimen de probabilidad y unidad de muestreo;
9. nulas, alternativas y controles de especificidad;
10. gate de dominio generativo;
11. condiciones de abstención del estimador o del método numérico;
12. terminal negativo y su precedencia.

Si falta uno, la frase debe marcarse `OPEN`, `TARGET` o `[UNVERIFIED]`; no puede aparecer como
resultado.

## 2. Etiquetas de evidencia

| Etiqueta | Uso permitido |
|---|---|
| `TARGET` | Objeto que se pretende construir o recuperar; ninguna existencia está establecida |
| `OPEN` | Problema especificado pero no resuelto |
| `[UNVERIFIED]` | Afirmación aún sin anclaje comprobado |
| `PROVED` | Teorema con hipótesis, prueba y alcance identificables |
| `CERTIFIED` | Cota o propiedad respaldada por método certificado y artefacto auditable |
| `EMPIRICAL` | Resultado de ensemble con protocolo, incertidumbre y población declarados |
| `VALIDATED` | Resultado confirmatorio bajo preregistro y scoring ciego |

`DRAFT`, `DRY_RUN`, `PLAUSIBLE`, `ADVISORY_ONLY` y `PREVIEW` nunca se convierten implícitamente en
`CERTIFIED`, `EMPIRICAL` o `VALIDATED`. Toda promoción exige un artefacto versionado, hash,
fecha, población o familia aplicable, evidencia requerida por la etiqueta y gate independiente.
Una elección hecha después de observar datos no puede registrarse retrospectivamente como
preespecificada.

## 3. Teleología y patch finito

### Regla

El horizonte de eventos global depende de la continuación futura del espacio-tiempo. Dos
continuaciones que coinciden dentro del patch observado pueden tener horizontes globales distintos;
por ello, el orden finito del patch no identifica por sí solo ese objeto global
(`research_program/synthesis/geometric_indeterminacy_decision.md:355-367`). Las alternativas
cuasi-locales se formulan mediante expansión/trapping y requieren su propio target
(`research_program/bibliography/next_observable_theory_review.md:23-44`).

### Forma permitida

```text
En la familia congelada G, dimensión d, carta X y patch P_L, el estimador order-only f
[PROVED|CERTIFIED|EMPIRICAL|VALIDATED: verbo y garantía] el proxy cuasi-local Q con
pérdida L_Q, bajo el canal K y el régimen probabilístico E.
Esto no identifica el horizonte de eventos global.
NO_RECONSTRUCTION_CLAIM.
```

La palabra `recupera` solo es admisible si una garantía positiva ya está establecida, anclada y
etiquetada como `PROVED`, `CERTIFIED`, `EMPIRICAL` o `VALIDATED`, y si el mismo claim declara
target, pérdida, familia, canal, régimen y alternativas. Declarar una garantía futura no basta.
Antes de satisfacer esas condiciones se usa `TARGET`, `candidato`, `proxy` o `evalúa`.

Se distinguen siempre tres objetos:

1. el horizonte de eventos global;
2. el corte de truncación por singularidad dentro de la familia Schwarzschild singular congelada;
3. un proxy cuasi-local de expansión/trapping definido por separado.

El segundo no se renombra como el tercero. El observable longest-chain/future-cardinality actual
responde a truncación por singularidad y borde finito, y se espera que no transfiera sin más a
agujeros negros regulares (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-201`).

En el toy 1+1D no existen las superficies espaciales bidimensionales que portan la expansión nula
de una esfera de simetría en 3+1D. La construcción EGS no calcula una expansión nula verdadera ni
una superficie marginal codimensión dos 3+1D: usa la distancia espacial unidimensional entre
geodésicas vecinas como proxy de expansión
(`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:214-230`).

### Convergencia

Los dos límites se escriben y evalúan por separado:

```text
density_limit, Poisson: rho_k -> infinity, N_k ~ Poisson(rho_k V_k), con P_L fijo
density_limit, fixed_n: n_k -> infinity bajo leyes condicionadas P_{n_k}; rho no es parámetro observable
patch_limit: L_k -> infinity con rho_k o ell_k y geometría de extensión declaradas
```

Una escalera en `rho` a patch fijo no prueba convergencia al horizonte global. Una escalera de
patch sin control de resolución tampoco. El benchmark congelado existente renuncia expresamente a
un claim asintótico de horizonte de eventos a caja fija
(`docs/preregistration_001_addendum.md:75-84`).

### Formas prohibidas

- "el causal set contiene el horizonte de eventos";
- "el horizonte fue reconstruido" a partir de un patch finito;
- "convergencia" sin nombrar qué límite varía y qué permanece fijo;
- cambiar silenciosamente entre horizonte global, región atrapada, superficie marginal y proxy.

**Terminal:** `TELEOLOGY_CLAIM_FAIL`.

## 4. Orientación temporal y dualidad

### Regla

Un representante etiquetado `P=(S,prec)` porta una relación orientada; su dual es
`P^op=(S,prec^op)`, con `x prec^op y` si y solo si `y prec x`. Son estructuras distintas, no un
cociente automático. Se separan dos niveles:

```text
Rep_K:   representantes etiquetados admisibles del canal K
Omega_K: clases de isomorfismo observadas
q:       Rep_K -> Omega_K,  q(P)=[P]
```

La dualización `d_rep(P)=P^op` actúa en `Rep_K` y desciende a la involución bien definida
`d([P])=[P^op]` en `Omega_K`. Una salida set-valued se formula en representantes y debe ser
equivariante bajo relabeling; una salida escalar invariante desciende a `Omega_K`.

Antes de formular dualidad se congelan:

1. una familia de modelos temporo-orientados `G_dual` y una involución `D:G_dual->G_dual`;
2. un único canal, `Rep_K`, `Omega_K`, `q`, `d_rep` y `d`, todos estables bajo dualidad;
3. la ley observada `Law_K(g)` sobre `Omega_K` para cada `g in G_dual`, con el contrato de
   pushforward `Law_K(Dg) = d_# Law_K(g)`;
4. para cada representante `P`, la biyección de soporte
   `iota_P:S(P)->S(P^op)`, con `iota_{P^op} o iota_P = id`;
5. compatibilidad con relabeling: para toda biyección `sigma`, la salida set-valued satisface
   `H_hat(sigma.P)=sigma(H_hat(P))` y `chi_hat(sigma.P)=chi_hat(P)`;
6. si el estimador es aleatorio, el acoplamiento de su aleatoriedad bajo dualidad y si la igualdad
   requerida es casi segura o en ley.

Para salidas deterministas `H_hat(P) subset S(P)` y `chi_hat(P) in {-1,0,+1}`, el contrato
candidato completo es:

```text
para todo P en Rep_K con [P] en Omega_K y [P^op]=d([P]):
  H_hat(P^op)   = iota_P(H_hat(P))
  chi_hat(P^op) = -chi_hat(P)
```

Estas ecuaciones son `TARGET` hasta que se demuestren o validen sobre `G_dual`; escribirlas aquí
no afirma que un estimador actual las satisfaga. Si una clase observada es autodual, la
anti-equivariancia y la invariancia por isomorfismo fuerzan `chi_hat=0`; ese valor significa
`CHARACTER_ABSTAIN_SELF_DUAL`, nunca BH o WH.

Si la familia no se cierra bajo dualidad, debe congelarse una convención temporal externa y el
claim se limita a esa orientación. No se permite inferir carácter BH/WH a partir de localización
sola. La experiencia del repo muestra que cambiar la orientación de una interfaz puede volverla
estructuralmente vacía (`dev/PR003_C1_RELATIONAL_SPEC.md:18-28`) y que el score asimétrico actual
sigue abierto (`dev/PR003_C1_RELATIONAL_SPEC.md:120-141`).

### Formas permitidas

- "localización módulo dualidad sobre `G_dual`", si se verifica la primera ecuación;
- "carácter condicionado a la convención temporal C", si C fue congelada antes de datos;
- "orientación estadísticamente identificable" solo después de un lema o test específico con su
  error y alternativas.

### Formas prohibidas

- "el poset no tiene orientación";
- "BH y WH son indistinguibles" sin especificar familia, canal y acción dual;
- reclamar equivariancia probándola solo dentro de una familia que no contiene sus duales;
- interpretar el signo de una salida que solo localiza.

**Terminal:** `ORIENTATION_CLAIM_FAIL`.

## 5. Escala, número y canal

### Regla

Siempre se distingue entre:

```text
fixed_n:      ley del poset condicionada a N=n
order+number: ley conjunta donde N es observable
```

En un sprinkling Poisson, `N ~ Poisson(rho V)` informa sobre el producto `rho V`; por sí solo no
separa `rho` y `V`. Si `rho` es conocida externamente, el número informa sobre volumen. Si no lo
es, identificarla con una escala física es una hipótesis adicional
(`research_program/work_packages/wp4_two_point_theorem.md:149-157`;
`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:102-115`).

La escala de discreción en dimensión espacio-temporal `d` es

```text
ell = rho^(-1/d).
```

En 3+1D, `ell = rho^(-1/4)`. Un resultado intrínseco puede expresarse como `r_h/ell`, pérdida en
unidades de `ell` o una razón con el tamaño del patch. Convertirlo a metros o unidades de Planck
requiere declarar la identificación física de `rho`.

La degeneración exacta de escala a `fixed_n` está probada para el par de dilatación 1+1D
(`research_program/models/first_witness_pair_candidates.md:62-105`). El canal `order+number` con
`rho` conocida reabre información mediante `N`
(`research_program/models/first_witness_pair_candidates.md:107-112`). Ninguna de esas frases
caracteriza por sí sola la clase `TV=0` completa en 3+1D.

### Formas prohibidas

- "N determina la escala física" sin `rho` conocida o hipótesis equivalente;
- trasladar el Teorema A 1+1D como caracterización completa de `TV=0` en 3+1D;
- mezclar leyes condicionadas a distintos `n` como si vivieran en el mismo experimento;
- escribir `rho -> infinity` dentro de un único experimento `fixed_n` sin una secuencia `n_k`;
- omitir las unidades relativas del target.

**Terminal:** `SCALE_CHANNEL_CLAIM_FAIL`.

## 6. Ensemble, instancia y límites probabilísticos

### Regla

Toda performance empírica se expresa sobre una ley de sprinklings o ensembles declarada:

```text
Pr_{C ~ P_theta,rho,L}( loss(f(C), T(theta)) <= delta ) >= 1 - alpha
```

o mediante riesgo esperado, con `theta`, `rho`, patch, número de réplicas, dependencia y cobertura
especificados. Un output correcto sobre un poset individual no demuestra unicidad geométrica de
ese poset.

También se separan:

- `single_instance`: una realización finita `C`;
- `ensemble_replicates`: varias realizaciones independientes al mismo `n`;
- `density_asymptotic`: una secuencia de experimentos con `n` o `rho` creciente;
- `patch_asymptotic`: una secuencia con dominio observado creciente.

Cada secuencia declara qué índice crece, cómo cambia la ley, qué parámetros permanecen fijos y si
las realizaciones son independientes. En `fixed_n`, condicionar elimina `rho` de la ley puntual
normalizada; el límite de densidad se formula mediante `n_k -> infinity`, no mediante variar un
`rho` invisible (`research_program/models/first_witness_pair_candidates.md:23-31`).

La tensorización demuestra que ensemble e instancia pueden tener distinguibilidad distinta, y
declara abierto el asintótico en `n`
(`research_program/work_packages/wp4_two_point_theorem.md:170-181`). Por tanto, "con alta
probabilidad" siempre nombra la fuente de aleatoriedad y el límite correspondiente.

### Formas prohibidas

- "el poset codifica unívocamente la geometría" a partir de una sola salida;
- extrapolar cobertura ensemble a unicidad single-instance;
- llamar convergencia a mejorar al añadir réplicas sin aumentar densidad;
- informar solo medias sin incertidumbre, población y unidad de muestreo.

**Terminal:** `ENSEMBLE_INSTANCE_CLAIM_FAIL`.

## 7. Nulas, alternativas y dirección de garantía

### Regla

Se declaran por separado:

1. error bajo la familia objetivo o nula;
2. separación frente a alternativas nombradas;
3. robustez frente a alternativas adversariales diseñadas;
4. especificidad del target frente a artefactos de patch, escala o densidad.

Sean `P_theta` y `P_theta_prime` dos leyes sobre el mismo espacio muestral del canal. Para pérdida
0-1 de recuperación exacta y targets distintos, una cota superior
`TV(P_theta,P_theta_prime) <= epsilon` activa directamente el suelo del teorema de dos puntos; no
es evidencia positiva de recuperación
(`research_program/work_packages/wp4_two_point_theorem.md:81-124`).

Para una pérdida genérica `L` y umbral aceptable `delta`, se congelan antes de datos las regiones
de decisión

```text
A_theta(delta)       = {a : L(a,T(theta))       <= delta}
A_theta_prime(delta) = {a : L(a,T(theta_prime)) <= delta}.
```

El transporte del suelo TV solo está permitido si estas regiones son disjuntas o si se aporta otra
reducción demostrada a un test binario. Targets distintos no bastan: regiones aceptables pueden
solaparse. Para pérdida métrica, una reducción admisible usa separación
`Delta_T=d(T(theta),T(theta_prime))` y umbral menor que `Delta_T/2`, o el clasificador de target más
cercano, produciendo la cota de cola/riesgo correspondiente
(`research_program/synthesis/geometric_indeterminacy_decision.md:214-234`). Sin una de estas
hipótesis, una cota TV no licencia un suelo de pérdida genérica.

Una cota inferior puede obtenerse con un estadístico testigo acotado:

```text
TV(P,Q) >= | E_P f - E_Q f |,
con P,Q sobre el mismo espacio medible y f: Omega -> [0,1].
```

Demostración: por la representación por capas,
`E_P f - E_Q f = integral_0^1 [P(f>t)-Q(f>t)] dt`; el valor absoluto de cada integrando está
acotado por `TV(P,Q)`, y el intervalo tiene longitud uno.

Para uso `CERTIFIED`, sean `[L_P,U_P]` y `[L_Q,U_Q]` intervalos simultáneos para las dos esperanzas
con cobertura al menos `1-alpha`. Entonces

```text
L_gap = max(0, L_P-U_Q, L_Q-U_P)
```

es una cota inferior de confianza para TV con la misma cobertura. Solo `L_gap>0`, bajo un método
y presupuesto Monte Carlo preespecificados, licencia un claim de separación. Deben declararse el
testigo, cobertura simultánea, dependencia, error Monte Carlo, alternativas y terminal si el
intervalo no resuelve el signo. Una cota inferior no convierte automáticamente `f` en un
reconstructor geométrico: además debe cerrarse el contrato target/salida/pérdida.

### Formas prohibidas

- llamar "distinguible" a `TV <= epsilon < 1` sin su consecuencia numérica;
- presentar una cota superior como señal positiva;
- reclamar especificidad usando solo controles fáciles;
- elegir el testigo después de mirar las alternativas confirmatorias;
- identificar "existe un test" con "existe un localizador" sin pérdida geométrica.

**Terminal:** `ADVERSARIAL_GUARANTEE_CLAIM_FAIL`.

## 8. Sprinkling cinemático y dinámica

### Regla

Sprinklear una geometría continua conocida produce un causal set manifold-like por construcción;
evalúa cinemática y recoverability condicionadas a esa familia. No demuestra que una dinámica de
causal sets genere, seleccione o haga dominante esa geometría. La construcción de sprinkling e
inducción del orden se describe en
`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:102-119`.

La mayoría combinatoria de los órdenes finitos es altamente no manifold-like y está dominada
asintóticamente por órdenes de Kleitman-Rothschild. La supresión de esa dominación es un problema
dinámico separado (`biblioteca/derived-md/Chevalier_2023_Discrete_Causal_Action_and_Holes_in_Spacetime.md:191-213`).

### Formas permitidas

- "recoverability cinemática condicionada a sprinklings de G";
- "benchmark sobre una geometría conocida";
- "candidato para una futura prueba bajo una medida dinámica".

### Formas prohibidas

- "emergencia del espacio-tiempo" a partir de sprinklings sobre un fondo fijado;
- "resultado de gravedad cuántica" sin medida, dinámica y clase de órdenes declaradas;
- asumir que reconocer Schwarzschild resuelve la supresión entrópica;
- presentar manifoldlikeness de los inputs como conclusión del algoritmo.

**Terminal:** `DYNAMICS_CLAIM_FAIL`.

## 9. Plantilla mínima para resultados futuros

### Precedencia de gates y abstenciones

```text
FAILED_DATA_CONTRACT
  > OUT_OF_DOMAIN
  > NUMERICAL_ABSTAIN
  > ESTIMATOR_ABSTAIN
  > SCIENTIFIC_PASS_OR_FAIL
```

Un terminal de mayor precedencia impide emitir cualquiera inferior. `OUT_OF_DOMAIN` no es FAIL
físico; una abstención numérica no es evidencia de indistinguibilidad; una abstención del
estimador no se coerciona a PASS o FAIL. Cada protocolo puede refinar los nombres, pero no alterar
esta precedencia sin una nueva gramática adoptada.

```text
RESULTADO [PROVED|CERTIFIED|EMPIRICAL|VALIDATED]
Dimensión / familia / clase física: ...
Carta / patch / truncaciones / extensión: ...
Canal / escala conocida / secuencia de experimentos: ...
Target / mecanismo físico / salida / pérdida: ...
Embedding: SOLO scoring; evidencia de que no define construcción, selección, abstención o frontera.
Orientación o acción dual: ...
Garantía y dirección: ...
Régimen probabilístico: ...
Nulas y alternativas: ...
Gate de dominio: ...
Abstención numérica / del estimador: ...
Terminal negativo y precedencia: ...
Límites no reclamados: ...
NO_RECONSTRUCTION_CLAIM.
Anclajes: file:line, comando, commit y artefacto.
```

Una frase que no cabe honestamente en esta plantilla no se publica como resultado.

## 10. Gate OP-0.2

```text
OP_0_2_AUTHOR_TERMINAL = CLAIM_GRAMMAR_DRAFT_READY_REVISION_1
OP_0_2_COMMITTEE_GATE = RECONVENE_PENDING
OP_0_2_AUDIT_GATE = PENDING
```

Máquina de estados:

```text
DRAFT_READY
  -> COMMITTEE_ADOPTED_AUDIT_PENDING
  -> ADOPTED

cualquier estado -> CLAIM_GRAMMAR_INCOMPLETE | CLAIM_GRAMMAR_OVERCLAIM |
                    CLAIM_GRAMMAR_ANCHOR_FAIL
```

El comité registra el hash exacto del blob que adopta. `/auditor` audita ese mismo hash y emite el
terminal final en su informe; no se hace una edición de estado posterior que cambie el blob
auditado. Precedencia fail-closed:

```text
CLAIM_GRAMMAR_ANCHOR_FAIL
  > CLAIM_GRAMMAR_OVERCLAIM
  > CLAIM_GRAMMAR_INCOMPLETE
  > CLAIM_GRAMMAR_ADOPTED
```

Terminal efectivo:

- `CLAIM_GRAMMAR_ADOPTED` si `/comite` adopta y `/auditor` confirma anclajes y claim boundary;
- `CLAIM_GRAMMAR_INCOMPLETE` si falta un campo, tipo, cuantificador, gate o precedencia exigidos;
- `CLAIM_GRAMMAR_OVERCLAIM` si alguna forma permitida excede la evidencia disponible;
- `CLAIM_GRAMMAR_ANCHOR_FAIL` si un fundamento no es trazable o está mal representado.
