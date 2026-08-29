# Hoja de ruta — septiembre de 2026 · de eficiencia combinatoria a tangentes geométricas

> **Plan REVISABLE, no congelado.** No es una pre-registración, no autoriza
> simulaciones, nuevos observables, consumo de semillas, cambios en instrumentos
> sellados ni extrapolaciones dimensionales. Su función es fijar el orden lógico
> de la nueva rama de información Fisher y evitar que vuelvan a abrirse frentes
> antes de cerrar el puente geométrico. Mantener `FAMILY_FROZEN`,
> `NO_UNIVERSALITY_CLAIM` y `PRIORITY = PROVISIONAL_NOT_SEALED`.

## Checkpoint vigente — 2026-08-28

Las fases S1 y S2 que el plan inferior describía como futuras ya están
cerradas. La secuencia de §§0–14 se conserva como registro de planificación,
pero no constituye autorización para reabrir S3–S7. El estado operativo que
manda al reanudar desde otro clon es:

```text
GEOMETRIC_TANGENT_CLASSIFICATION = PROVED
S2_GEOMETRIC_FISHER_RETENTION = PROVED_BY_ASSEMBLY
STOP_AFTER_S2 = SI
S3_NOT_OPENED
S4_NOT_OPENED
NO_HORIZON_CLAIM
NO_PRIORITY_CLAIM
FISHER_BRANCH_ROLE = STRUCTURAL_TOOL

PHYSICAL_REENTRY = PARTIAL_TRANSPORT_WITH_POINT_QMD_OBSTRUCTION_PROVED
COMMON_POINT_ISOMORPHISM = REFUTED
MOVING_SUPPORT_QMD_STATUS = PROVED_NON_QMD_FOR_POINT_EXPERIMENT
FINITE_CHANNEL_REGULARITY = OPEN
DOMAIN_BRIDGE = OPEN_AT_FINITE_CHANNEL
NEXT_RUN_AUTHORIZED = NO
```

La auditoría autoritativa de reingreso es
`docs/physical_reentry_audit_001_2026-08-28.md`. La decisión acotada del PI y
la obstrucción negativa del puente puntual están registrados respectivamente en
`docs/program_domain_bridge_authorization_2026-08-28.md` y
`research_program/work_packages/wp6_domain_bridge_fixed_ef_box.md`. La prueba
completa la velocidad normal, la cota de área de la diferencia simétrica y la
cota inferior de densidad. No permite inferir no-QMD para la ley después del
canal finito; `FINITE_CHANNEL_REGULARITY` y el residuo de `DOMAIN_BRIDGE`
siguen abiertos y no autorizados.

```text
GOBERNANZA: docs/program_reopening_note_2026-08-28_R4.md (firmada 2026-08-28)
G2: §2.2 enmendada a Convención B el 2026-08-28
    (lambda parametriza P psi, no el tangente de copula)
PLAN_INFERIOR: REGISTRO_HISTORICO_DE_SECUENCIACION
```

## 0. Punto de partida preservado

Rama de trabajo:

```text
emergencia/p1a-canal-sigma-m
```

Commits de preservación de entrada:

```text
236b1824d86ad3c169e574bf263ecde40310eb04
  prove asymptotic Fisher efficiency for unlabeled 2D posets

4bcbfc50a95ddb7af52bfa002974016b9eafbd43
  document unlabeled 2D poset Fisher theorem
```

Anclas obligatorias antes de trabajar:

1. `research_program/work_packages/wp6_d2_modular_fiber_score.md`;
2. `research_program/work_packages/wp6_d2_null_copula_dichotomy.md`;
3. `README.md`, sección “Current theory result — Fisher efficiency of
   unlabeled 2D posets”.

Estado científico de entrada:

```text
FAMILY_FROZEN
FINITE_N_POSET_LOSS_PROVED
TYPICAL_FIBER_ZERO_LOSS = PROVED
ASYMPTOTIC_POSET_FISHER_EFFICIENCY_FOR_BOUNDED_SEPARABLE_SCORES = PROVED
THEOREM_PROVED_PRIORITY_AUDIT_PASSED_PROVISIONALLY
POTENTIALLY_NOVEL_THEOREM_NOT_NOVEL_FRAMEWORK
NO_UNIVERSALITY_CLAIM
NEXT_TARGET = GEOMETRIC_TANGENT_CLASSIFICATION
TARGET_SUBCLASS = SYMMETRIC_RANK_ONE_COPULA_TANGENTS
GENERIC_BILINEAR_SEPARABLE_EXTENSION = OPEN_NOT_ASSUMED
RATE_IMPROVEMENT = DEFERRED
PRIORITY = PROVISIONAL_NOT_SEALED
```

El teorema autónomo ya demostrado usa una permutación uniforme `Pi_N`, el
canal exacto

\[
\Pi_N\longmapsto[P_{\Pi_N}],
\]

y scores simétricos separables

\[
S_N(\pi)=2\sum_{i=1}^N a_{i,N}a_{\pi(i)}.
\]

Si los perfiles son uniformemente acotados, centrados y tienen energía no
degenerada, entonces

\[
1-\frac{I_N^{[P]}}{I_N^\Pi}=O(N^{-1/2}),
\qquad
\frac{I_N^{[P]}}{I_N^\Pi}\longrightarrow1.
\]

Este resultado no se reabre en septiembre salvo contradicción matemática
explícita.

## 1. Norte único de septiembre

El único frente científico autorizado al comenzar el mes es

```text
GEOMETRIC_TANGENT_CLASSIFICATION
```

La pregunta es:

> ¿Qué perturbaciones conformes de un diamante causal (1+1) inducen, tras
> normalizar la medida y eliminar las marginales, un tangente de cópula
> simétrico rank-one cuyo score de rangos pertenece exactamente a la clase del
> teorema ya probado?

La secuencia vinculante es

\[
\boxed{
\text{teorema combinatorio ya probado}
\longrightarrow
\text{clasificación del tangente geométrico}
\longrightarrow
\text{teorema geometría }1+1\to\text{causet}
\longrightarrow
\text{auditoría final de prioridad}.
}
\]

No se abre el siguiente eslabón hasta cerrar o refutar el anterior.

## 2. Fase S1 — cerrar el puente geométrico

### 2.1 Objeto congelado

Partir de una perturbación conforme

\[
g_\varepsilon
=\frac{e^{2\varepsilon\psi(u,v)}}{Z(\varepsilon)}g_0
\]

en un diamante (1+1), con dominio, medida de referencia y condicionamiento en
`N` fijados antes de cualquier generalización.

Debe derivarse desde la medida normalizada, no postularse, el tangente de
cópula obtenido al retirar las dos marginales:

\[
\boxed{
h_\psi(u,v)
=2\,[\psi(u,v)-\psi_U(u)-\psi_V(v)+\bar\psi].
}
\]

Aquí deben definirse explícitamente `psi_U`, `psi_V`, `bar psi`, la constante
`Z(epsilon)` y el sentido de la derivada. No se permite esconder términos de
normalización dentro de una proporcionalidad informal.

### 2.2 Subclase objetivo

Caracterizar exactamente cuándo

\[
\psi(u,v)-\psi_U(u)-\psi_V(v)+\bar\psi
=\lambda f(u)f(v),
\qquad\text{equivalentemente}\qquad
h_\psi(u,v)=2\lambda f(u)f(v),
\]

con

\[
f\ \text{suave},
\qquad
\int_0^1 f(u)\,du=0,
\qquad
\int_0^1 f(u)^2\,du>0,
\]

y con las condiciones de acotación necesarias para aplicar el teorema de
scores separables.

**Convención B (G2, 2026-08-28).** El símbolo `lambda` parametriza la
proyección geométrica `P psi`, no el tangente de cópula. El factor `2` de
`h_psi=2 P psi` queda explícito, y el score de §2.3 usa el mismo `lambda`
en todas las etapas. (La Convención A, `h_psi=lambda f f`, queda
retirada de este §2.2.)

El objetivo no es clasificar todas las perturbaciones conformes. Es identificar
una subclase geométrica explícita, no vacía y estable bajo las equivalencias
marginales pertinentes.

### 2.3 Obligaciones de prueba

1. Derivar el score de la muestra condicionada a `N`.
2. Derivar el score condicionado a la permutación de rangos.
3. Probar que, en la subclase rank-one simétrica,
   \[
   S_N(\pi)=2\lambda\sum_i a_{i,N}a_{\pi(i)},
   \qquad
   a_{i,N}=\mathbb E[f(U_{(i)})],
   \]
   con cualquier convención de escala registrada de forma consistente.
4. Verificar, sin simulación:
   \[
   \sup_{N,i}|a_{i,N}|<\infty,
   \qquad
   \sum_i a_{i,N}=0,
   \qquad
   \frac1N\sum_i a_{i,N}^2\longrightarrow\int_0^1 f(u)^2\,du>0.
   \]
5. Distinguir el tangente geométrico, el tangente de densidad, el tangente de
   cópula y el score de rangos. No identificarlos mediante notación ambigua.

### 2.4 Falsificadores obligatorios

- Una perturbación puramente marginal
  `psi(u,v)=alpha(u)+beta(v)+const` debe desaparecer tras la proyección de
  marginales.
- Debe verificarse el factor `2`, el signo y el término `bar psi` mediante una
  diferenciación independiente.
- Debe exhibirse al menos una `psi` no sinusoidal dentro de la clase o demostrar
  que la clase geométrica se reduce más de lo previsto.
- Si un producto genérico `f(u)g(v)` con `f != g` aparece, no se promoverá al
  teorema simétrico: quedará fuera de alcance.

### 2.5 Veredictos permitidos

```text
GEOMETRIC_TANGENT_CLASSIFICATION = PROVED
GEOMETRIC_TANGENT_CLASSIFICATION = REFUTED
GEOMETRIC_TANGENT_CLASSIFICATION = OPEN_WITH_EXACT_OBLIGATION
```

`OPEN` sólo es admisible con una proposición concreta pendiente. Un ejemplo
numérico o una expansión formal sin control del resto no cierra la fase.

## 3. Fase S2 — primer teorema completo geometría a causet

Esta fase sólo se abre si S1 termina `PROVED`.

### 3.1 Enunciado objetivo

Para la clase explícita de deformaciones conformes rank-one simétricas obtenida
en S1, demostrar

\[
\boxed{
\frac{I_N^{[P]}(g_\varepsilon)}
     {I_N^\Pi(g_\varepsilon)}
\longrightarrow1.
}
\]

La notación debe especificar:

- familia geométrica y parámetro local;
- diamante (1+1) y coordenadas normalizadas;
- condicionamiento a cardinalidad fija `N`;
- representación observada antes del cociente;
- poset orientado no etiquetado observado después del cociente;
- score y punto nulo donde se calcula Fisher;
- clase exacta de `psi` o de `f`.

### 3.2 Claim ceiling

El resultado permitido será:

> En una clase explícita de deformaciones conformes simétricas rank-one de un
> diamante (1+1), el poset no etiquetado retiene asintóticamente toda la
> información Fisher relativa disponible en la permutación de rangos.

No estará permitido inferir:

- suficiencia respecto de las coordenadas continuas completas;
- reconstrucción de la métrica;
- universalidad para todo tangente geométrico;
- una afirmación sobre horizontes;
- una afirmación en (2+1) o (3+1);
- suficiencia absoluta sin especificar el experimento comparado.

### 3.3 Entregable

Un teorema autónomo con prueba modular en cuatro pasos:

1. geometría `->` tangente de cópula;
2. tangente de cópula `->` score de rangos simétrico;
3. score simétrico `->` teorema combinatorio ya probado;
4. conclusión Fisher para el canal `Pi_N -> [P_Pi_N]`.

No duplicar en esta fase las pruebas del cuarto momento ni de la fibra típica;
citarlas con hipótesis verificadas una por una.

## 4. Fase S3 — auditoría final de prioridad geométrica

Esta fase sólo se abre cuando exista un enunciado geométrico completo y estable.
La auditoría provisional del teorema combinatorio no sustituye esta revisión.

### 4.1 Pregunta adversarial exacta

> ¿Existe una fuente previa que demuestre suficiencia asintótica (L^2) o
> Fisher del poset bidimensional no etiquetado respecto de la permutación de
> rangos para tangentes procedentes de deformaciones geométricas conformes de
> la clase S1?

No basta encontrar antecedentes sobre:

- suficiencia asintótica de cuantizaciones en general;
- estadística clásica de rangos;
- cópulas, permutons o frecuencias de patrones antes del cociente;
- rigidez o unicidad de órdenes aleatorios bidimensionales;
- pérdida de etiquetas en grafos mediante entropía o mutual information.

### 4.2 Salidas permitidas

```text
DIRECT_PRIOR_FOUND
PRECURSOR_ONLY
SURVIVES_NARROWLY
INCONCLUSIVE_ACCESS_OR_SCOPE
```

Aunque el resultado sobreviva, el wording máximo seguirá siendo:

> We are not aware of previous results establishing the stated asymptotic
> Fisher-retention theorem for this exact geometric-to-unlabeled-poset channel.

No usar `first`, `novelty certified`, `breakthrough` ni equivalentes.

## 5. Fase S4 — generalización simétrica controlada en (1+1)

Esta fase no pertenece al objetivo inicial de septiembre. Sólo puede diseñarse
si S1–S3 están cerradas y documentadas.

La observación estructural de partida es que la fibra típica es

\[
\{\pi,\pi^{-1}\}.
\]

Por ello, para

\[
S_H(\pi)=\sum_i H_{i,\pi(i)},
\]

la condición

\[
H=H^{\mathsf T}
\]

hace al score invariante bajo inversión. El primer candidato de extensión es
una clase de rango finito

\[
H_N=\sum_{r=1}^R
\lambda_r a^{(r)}a^{(r)\mathsf T}.
\]

Esto es una **ruta candidata**, no un corolario ya demostrado. Antes de
promoverla habrá que cerrar de nuevo:

1. escala no degenerada de `I_N^Pi`;
2. cota de cuarto momento uniforme para el score matricial;
3. dependencia admisible de `R`, `lambda_r` y las normas de los perfiles;
4. clase geométrica que produce esos kernels simétricos.

```text
FINITE_RANK_BOUNDED_CONTINUOUS_SYMMETRIC_RETENTION = PROVED_BY_ASSEMBLY
FINITE_RANK_SYMMETRIC_RETENTION = PROVED
```

### 5.1 Preflight autorizado — rango finito simétrico (2026-08-29)

Este preflight no depende del `PASS` externo de Bombelli ni modifica el estado
bibliográfico. Tampoco abre kernels de rango infinito. Reconstruye literalmente
S2 desde el Teorema 5 de `wp6_d2_modular_fiber_score.md`, los Teoremas 6--7 y
los Lemas 11.1--11.2 de
`wp6_d2_geometric_tangent_classification.md`, y el Teorema 8 de
`wp6_d2_geometric_fisher_retention.md`.

#### Datos de S2 reconstruidos

Para un perfil `a in C[0,1]`, centrado y no nulo, escribiendo

\[
a_{i,N}:=\mathbb E[a(U_{(i)})],
\qquad
X_N(a):=\sum_i a_{i,N}a_{\Pi_N(i),N},
\tag{5.1}
\]

el score geométrico rank-one, con la Convención B, es

\[
S_N(a)=2\lambda X_N(a).
\tag{5.2}
\]

S2 prueba, para `lambda != 0`,

\[
0\le 1-\frac{I_N^{[P]}(a)}{I_N^\Pi(a)}
\le
\left(
\frac{\sqrt{240C_A}\,\|a\|_\infty^4}
{4\left(\int_0^1a^2\right)^2}+o(1)
\right)N^{-1/2}.
\tag{5.3}
\]

Aquí `C_A,N_A` proceden de `Pr(B_N)<=C_A/N`; la constante no depende de
`lambda`. Las hipótesis reales sobre el perfil son continuidad, centrado
exacto, norma `L2` positiva y, por compacidad, acotación uniforme. La
normalización es `P psi=lambda a tensor a`, tangente de cópula
`h_psi=2 lambda a tensor a` y score (5.2).

#### Forma de pérdida

Para scores producidos por tangentes admisibles definimos

\[
\Delta_N(f,g):=G_N^\Pi(f,g)-G_N^{[P]}(f,g).
\tag{5.4}
\]

La identidad de score condicionado y polarización dan exactamente

\[
\Delta_N(f,g)
=\mathbb E\!\left[
\operatorname{Cov}(S_N(f),S_N(g)\mid[P])
\right].
\tag{5.5}
\]

Por tanto `Delta_N` es una forma bilineal semidefinida positiva,

\[
\Delta_N(f,f)
=\mathbb E[\operatorname{Var}(S_N(f)\mid[P])]\ge0,
\tag{5.6}
\]

y Cauchy--Schwarz para formas semidefinidas positivas implica

\[
|\Delta_N(f,g)|
\le\sqrt{\Delta_N(f,f)\Delta_N(g,g)}.
\tag{5.7}
\]

#### Ensamblaje finito dentro de la clase acotada de S2

Sea

\[
f=\sum_{r=1}^R\lambda_r a_r\otimes a_r,
\qquad R<\infty,
\tag{5.8}
\]

con cada `a_r in C[0,1]` centrado. El score es la suma de los scores
rank-one. De (5.7), o equivalentemente de la desigualdad triangular para la
seminorma inducida por `Delta_N`, se obtiene

\[
\Delta_N(f,f)
\le
\left(\sum_{r=1}^R|\lambda_r|
\sqrt{\Delta_N(a_r\otimes a_r,a_r\otimes a_r)}\right)^2.
\tag{5.9}
\]

La cota absoluta (7.6) del WP6 modular, antes de dividir por el Fisher, da la
versión explícita

\[
\boxed{
\Delta_N(f,f)
\le
\sqrt{240C_A}\,\sqrt N
\left(\sum_{r=1}^R|\lambda_r|\|a_r\|_\infty^2\right)^2
}
\qquad(N\ge N_A).
\tag{5.10}
\]

No se ha absorbido en `O(.)` ninguna dependencia en `R`, los eigenvalores o
las normas de los perfiles.

Para arrays centrados `x,y` y permutación uniforme, el mismo cálculo de pares
usado en §7.1 del WP6 modular, ahora polarizado, da

\[
\mathbb E[(x^TP_{\Pi_N}x)(y^TP_{\Pi_N}y)]
=\frac{(x^Ty)^2}{N-1}.
\tag{5.11}
\]

En consecuencia el denominador de (5.8) es exactamente

\[
\boxed{
I_N^\Pi(f)
=\frac4{N-1}\sum_{r,s=1}^R
\lambda_r\lambda_s
\left(\sum_{i=1}^Na_{r,i,N}a_{s,i,N}\right)^2.
}
\tag{5.12}
\]

La demostración de H3 del Teorema 7 se polariza, de modo que

\[
\frac1N\sum_i a_{r,i,N}a_{s,i,N}
\longrightarrow\langle a_r,a_s\rangle_{L^2}.
\tag{5.13}
\]

Por tanto, para `f != 0`,

\[
I_N^\Pi(f)=4N\|f\|_{HS}^2+o(N).
\tag{5.14}
\]

Combinando (5.10) y (5.14), queda probado por ensamblaje, sin uniformidad en
`R`, que para todo kernel simétrico de rango finito que admita una
descomposición (5.8) con perfiles continuos centrados,

\[
0\le1-\eta_N(f)
\le
\left[
\frac{\sqrt{240C_A}
(\sum_r|\lambda_r|\|a_r\|_\infty^2)^2}
{4\|f\|_{HS}^2}+o(1)
\right]N^{-1/2},
\qquad
\eta_N(f)\to1.
\tag{5.15}
\]

En una descomposición espectral ortonormal, la dependencia del numerador es
de tipo norma de traza ponderada por `\|a_r\|_infty^2`; no es una cota de tipo
Hilbert--Schmidt ni uniforme en `R`.

#### Único lema ausente para el enunciado literal en (L^2)

Un operador simétrico de rango finito en
`L_0^2 widehat tensor_sym L_0^2` puede tener eigenfunciones no acotadas. S2 y
(5.10) no se le aplican, porque dependen de `\|a_r\|_infty`. El denominador
no es el obstáculo: (5.12)--(5.14) siguen siendo la estructura requerida una
vez justificada la aproximación de perfiles.

El único lema nuevo suficiente es un control de cuarto momento para cada
perfil fijo `a in L_0^2`, o directamente para cada suma finita fija, que
implique

\[
\mathbb E[S_N(f)^4]=o(N^3).
\tag{5.16}
\]

Como `Pr(B_N)=O(N^{-1})`, (5.16) daría por Cauchy--Schwarz
`Delta_N(f,f)=o(N)` y, junto con (5.14), retención relativa. Una formulación
elemental candidata para probar (5.16) a partir de la expansión exacta (7.1)
es

\[
\max_i|\mathbb E[a(U_{(i)})]|=o(\sqrt N)
\qquad(a\in L^2[0,1]),
\tag{5.17}
\]

combinada con `N^{-1}\sum_i a_{i,N}^2 -> \|a\|_2^2`. Este lema no está
demostrado en los artefactos anteriores al preflight.

### 5.2 `L2_ORDER_STATISTIC_FOURTH_MOMENT_LEMMA` (2026-08-29)

El lema se cierra sin hipótesis `L-infinity`. Sea

\[
\rho_{i,N}(t)
:=N\binom{N-1}{i-1}t^{i-1}(1-t)^{N-i}
\tag{5.18}
\]

la densidad de `U_(i)` y defínase

\[
(T_Na)_i:=\int_0^1a(t)\rho_{i,N}(t)\,dt.
\tag{5.19}
\]

Como `sum_i rho_(i,N)(t)=N`, Jensen y Tonelli dan, para todo `a in L2`,

\[
\frac1N\sum_{i=1}^N|(T_Na)_i|^2
\le\frac1N\sum_i\int|a|^2\rho_{i,N}
=\|a\|_2^2.
\tag{5.20}
\]

Por tanto `T_N:L2 -> ell_N^2`, con la norma normalizada del lado discreto, es
una contracción uniforme. Para `b in C[0,1]` centrada, el Teorema 7 ya prueba
`N^(-1)||T_Nb||_2^2 -> ||b||_2^2`. Dado `a in L2`, elija `b` continuo con
`||a-b||_2<epsilon`. De (5.20),

\[
\left|N^{-1/2}\|T_Na\|_2-N^{-1/2}\|T_Nb\|_2\right|
\le\|a-b\|_2.
\tag{5.21}
\]

Pasando primero `N -> infinity` y después `epsilon -> 0`, se obtiene

\[
\boxed{
\frac1N\sum_i|\mathbb E[a(U_{(i)})]|^2\longrightarrow\|a\|_2^2.
}
\tag{5.22}
\]

Para el máximo, la expresión binomial en (5.18) implica puntualmente
`0<=rho_(i,N)<=N`; como su integral es uno,

\[
\|\rho_{i,N}\|_2^2\le\|\rho_{i,N}\|_\infty\le N.
\tag{5.23}
\]

Fijados `a in L2` y `epsilon>0`, tome una función acotada `b` con
`||a-b||_2<epsilon`. Entonces, uniformemente en `i`,

\[
\frac{|(T_Na)_i|}{\sqrt N}
\le\frac{\|b\|_\infty}{\sqrt N}
+\|a-b\|_2\frac{\|\rho_{i,N}\|_2}{\sqrt N}
\le\frac{\|b\|_\infty}{\sqrt N}+\epsilon.
\tag{5.24}
\]

Tomando `limsup_N` y luego `epsilon -> 0`, queda

\[
\boxed{
\max_i|\mathbb E[a(U_{(i)})]|=o(\sqrt N).
}
\tag{5.25}
\]

Además `sum_i(T_Na)_i=N int a=0` exactamente. Si `x_i=(T_Na)_i`, escribamos
`S_2=sum_i x_i^2`, `S_4=sum_i x_i^4` y
`M_N=max_i|x_i|`. Por (5.22), `S_2=O(N)`, mientras (5.25) da

\[
S_4\le M_N^2S_2=o(N^2).
\tag{5.26}
\]

Al sustituir estas dos estimaciones en la expansión combinatoria exacta (7.1)
del WP6 modular, sus cinco términos son respectivamente

\[
o(N^3),\qquad o(N^2),\qquad O(N^2),\qquad O(N),\qquad O(1).
\tag{5.27}
\]

En particular,

\[
\boxed{\mathbb E[X_N(a)^4]=o(N^3).}
\tag{5.28}
\]

Para una suma fija de `R` scores, Minkowski en `L4` y (5.28) implican

\[
\mathbb E[S_N(f)^4]=o(N^3),
\qquad
f=\sum_{r=1}^R\lambda_ra_r\otimes a_r,
\quad a_r\in L_0^2.
\tag{5.29}
\]

En el evento típico `A_N`, la fibra es exactamente `{Pi_N,Pi_N^(-1)}` y cada
forma cuadrática simétrica, y por tanto su suma, es invariante. Usando
`Pr(B_N)<=C_A/N`, Cauchy--Schwarz y (5.29),

\[
0\le\Delta_N(f,f)
\le\mathbb E[S_N(f)^2\mathbf1_{B_N}]
\le\Pr(B_N)^{1/2}\mathbb E[S_N(f)^4]^{1/2}
=o(N).
\tag{5.30}
\]

La polarización de (5.22) extiende (5.13) a perfiles `L2`. Por ello la fórmula
exacta (5.12) sigue dando, para todo `f != 0` simétrico de rango finito,

\[
I_N^\Pi(f)=4N\|f\|_{HS}^2+o(N).
\tag{5.31}
\]

Dividiendo (5.30) por (5.31), queda probado el teorema de rango finito en el
espacio natural:

\[
\boxed{
f\in L_0^2\widehat\otimes_{\rm sym}L_0^2,
\quad 0<\operatorname{rank}f<\infty
\quad\Longrightarrow\quad
\eta_N(f)\longrightarrow1.
}
\tag{5.32}
\]

La tasa disponible para perfiles `L2` generales es sólo `o_f(1)`: (5.25) no
proporciona una velocidad universal. La tasa `O_f(N^(-1/2))` permanece para
la subclase continua/acotada de §5.1. Este cierre es tangente/Fisher en el
espacio de Hilbert; no afirma que todo vector `L2` sea realizado por una senda
positiva continua de densidades con la regularidad geométrica original.

Para el sector mixto, el cociente no etiquetado mata exactamente la componente
antisimétrica, pero no se promueve aquí ninguna fórmula para el cociente con
denominador de referencia. Permanece:

```text
FINITE_RANK_BOUNDED_CONTINUOUS_SYMMETRIC_RETENTION = PROVED_BY_ASSEMBLY
L2_ORDER_STATISTIC_FOURTH_MOMENT_LEMMA = PROVED
FINITE_RANK_SYMMETRIC_RETENTION = PROVED
R_CONTROL = TRACE_NORM_TYPE_WEIGHTED_BY_PROFILE_SUP_NORMS
L2_FINITE_RANK_RATE = o_f(1)_WITHOUT_UNIVERSAL_RATE
FULL_SYMMETRIC_S1_FISHER_RETENTION_PREFLIGHT = PASS_FINITE_RANK_NEW_LEMMA_IDENTIFIED
FIRST_MISSING_LEMMA = NONE_AT_FINITE_RANK
INFINITE_RANK_EXTENSION_STATUS = NOT_OPENED
MIXED_SECTOR_LIMIT = CONJECTURE
NEXT_RUN_AUTHORIZED = NO
```

## 6. Fase S5 — clasificar la información que sí se pierde

Después del sector simétrico se estudiará su contraparte. Para

\[
S_{x,y}(\pi)=x^{\mathsf T}P_\pi y,
\qquad x\ne y,
\]

la inversión global produce

\[
S_{x,y}(\pi^{-1})=y^{\mathsf T}P_\pi x,
\]

que no tiene por qué coincidir con el score original. Por tanto, incluso el
sector típico puede conservar pérdida.

La pregunta futura será si existe una descomposición rigurosa entre:

\[
\text{sector simétrico: eficiencia relativa }\to1,
\]

y

\[
\text{sector asimétrico: pérdida posiblemente persistente}.
\]

No se preregistra esa dicotomía como verdadera. Debe falsarse primero en
tamaños finitos y demostrarse después a nivel de la ley condicional.

```text
GENERIC_BILINEAR_SEPARABLE_EXTENSION = OPEN_NOT_ASSUMED
```

## 7. Fase S6 — salto a (2+1)

El paso dimensional sólo se abre después de una teoría (1+1) geométrica y
simétrica estabilizada. En (2+1) ya no existe la cadena especial

\[
\text{cópula}\leftrightarrow
\text{permutación}\leftrightarrow
\text{poset 2D}.
\]

La pregunta transportable será:

\[
\boxed{
\text{¿qué fracción de la información Fisher de una representación geométrica}
\atop
\text{sobrevive al olvidar el embedding y observar sólo }[C]\text{?}
}
\]

El primer trabajo en (2+1) deberá definir el experimento antes y después del
cociente. No empezará con reconstrucción métrica, simulaciones masivas ni un
observable elegido por conveniencia.

```text
DIMENSION_2P1_EXTENSION = DEFERRED
```

## 8. Fase S7 — programa de `information retention`

El objeto a largo plazo es clasificar tangentes geométricos mediante

\[
\eta_N(h)
=\frac{I_N^{\mathrm{intrinsic}}(h)}
       {I_N^{\mathrm{representation}}(h)}.
\]

Los tres regímenes conceptuales que deberán distinguirse, sin asumir que todos
ocurren, son

\[
\eta_N(h)\to1,
\qquad
\eta_N(h)\to\eta_\infty\in(0,1),
\qquad
\eta_N(h)\to0.
\]

El programa preguntará qué información geométrica es preservada, parcialmente
perdida o destruida por el paso desde una representación enriquecida al causet
intrínseco. Éste es un horizonte de investigación, no una afirmación vigente.

## 9. Secuencia operativa de septiembre

### Semana 1 — derivación geométrica

1. fijar dominio, normalización y convenciones;
2. derivar `h_psi` por dos rutas independientes;
3. ejecutar los falsificadores marginales y de signo/factor;
4. registrar la obligación exacta si la fórmula no cierra.

### Semana 2 — clasificación rank-one y score de rangos

1. caracterizar la preimagen geométrica de `lambda f tensor f`;
2. derivar el score condicionado a rangos;
3. verificar acotación, centrado y energía;
4. emitir el veredicto S1.

### Semana 3 — teorema geometría a causet

Sólo si S1 es `PROVED`:

1. escribir el enunciado autónomo;
2. encadenar las cuatro piezas de §3.3;
3. auditar cuantificadores, canales y denominadores Fisher;
4. preparar una versión legible independiente del work package.

### Semana 4 — prioridad y decisión de continuación

1. ejecutar la auditoría adversarial S3;
2. fijar el claim ceiling final;
3. decidir si la rama continúa hacia S4;
4. no comenzar S4 dentro del mismo acto de decisión.

Si S1 queda `REFUTED` u `OPEN`, las semanas restantes se dedican a documentar
el bloqueo y preservar el resultado combinatorio. No se compensa abriendo S4,
S5 o (2+1).

## 10. Entregables de septiembre

Obligatorios, en orden:

1. derivación exacta del tangente geométrico y de cópula;
2. clasificación o refutación de la subclase simétrica rank-one;
3. verificación de las hipótesis del teorema de eficiencia;
4. teorema completo geometría (1+1) `->` causet, si procede;
5. auditoría final de prioridad del teorema geométrico, si procede;
6. actualización mínima de README e inventario de teoremas sólo después de
   cerrar los resultados correspondientes.

Cada entregable debe incluir:

- hipótesis completas;
- canal exacto;
- prueba o bloqueo preciso;
- falsificador finito/simbólico proporcionado al riesgo;
- fuentes primarias cuando se importe un teorema;
- claim permitido y claim prohibido;
- tests deterministas y `git diff --check` antes de preservarlo.

## 11. No hacer en septiembre

- No pasar todavía a (2+1) ni (3+1).
- No mejorar la tasa `O(N^{-1/2})`.
- No abrir scores bilineales genéricos.
- No promover automáticamente kernels simétricos de rango finito.
- No hacer simulaciones asintóticas.
- No introducir observables nuevos.
- No mezclar este frente con horizontes o reconstrucción métrica.
- No generalizar de rank-one simétrico a `f tensor g` con `f != g`.
- No declarar prioridad sellada a partir de ausencia de resultados en una
  búsqueda.
- No llamar universal al teorema combinatorio ni al eventual teorema
  geométrico.
- No tocar instrumentos, umbrales, semillas ni artefactos congelados de otros
  frentes de NACHOCAUSAL.

```text
RATE_IMPROVEMENT = DEFERRED
GENERIC_BILINEAR_SEPARABLE_EXTENSION = OPEN_NOT_ASSUMED
DIMENSION_2P1_EXTENSION = DEFERRED
NO_SIMULATION_AUTHORIZATION
NO_UNIVERSALITY_CLAIM
```

## 12. Gates de cierre del mes

### Gate A — `GEOMETRIC_CAUSALSET_THEOREM_PROVED`

S1 y S2 están demostradas, S3 está auditada y el wording no excede la
evidencia. Septiembre cierra con un teorema geométrico (1+1) y una decisión
separada sobre S4.

### Gate B — `COMBINATORIAL_THEOREM_PRESERVED_GEOMETRIC_BRIDGE_OPEN`

El teorema combinatorio permanece intacto, pero S1 deja una obligación concreta
no resuelta. No se abre ninguna generalización para compensarlo.

### Gate C — `GEOMETRIC_RANK_ONE_ROUTE_REFUTED`

La fórmula marginal o la clasificación muestran que la ruta rank-one propuesta
no describe la clase geométrica esperada. Se entrega el contraejemplo o la
caracterización correcta, sin reparar retrospectivamente el contrato.

### Gate D — `PRIORITY_SCOPE_REVISED`

El teorema geométrico cierra matemáticamente, pero la auditoría encuentra un
antecedente directo o una limitación de prioridad. Se ajusta el framing sin
debilitar ni inflar el contenido matemático.

## 13. Criterio de éxito y visión de continuidad

La visión de la rama es

\[
\boxed{
\text{teorema combinatorio}
\longrightarrow
\text{teorema geométrico }1+1
\longrightarrow
\text{clase simétrica más amplia}
\longrightarrow
2+1.
}
\]

Septiembre tiene éxito si convierte el primer arco en el segundo o identifica
con precisión por qué no puede hacerlo. No requiere mejorar tasas, ampliar
dimensión ni producir numerics.

Si el puente geométrico falla, la rama conserva un teorema combinatorio
autónomo. Si el puente cierra y la generalización simétrica empieza después a
sobrevivir, habrá una línea propia de investigación sobre retención de
información geométrica en causal sets. Esa posibilidad no se promociona como
resultado antes de demostrar sus gates.

## 14. Checklist de reentrada

1. Confirmar rama, `HEAD`, upstream y worktree limpio.
2. Leer las tres anclas de §0 antes de derivar nada.
3. Verificar que no existe otro objetivo `in_progress`.
4. Copiar literalmente las definiciones de canal y score ya probadas; no
   reconstruirlas de memoria.
5. No abrir ninguna fase nueva: aplicar el checkpoint vigente de cabecera.
6. Antes de cada cambio de fase, emitir el veredicto permitido y preservar el
   diff correspondiente.
7. Si aparece una contradicción con el teorema combinatorio, detener la hoja y
   auditarla antes de continuar.
