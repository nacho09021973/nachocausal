# WP6 — Outline del paper de visibilidad tangente de leyes causales finitas

> **STATUS: PAPER_SKELETON_DRAFT / INTERNAL_ONLY / NOT_FROZEN /
> PRIORITY_AUDIT_CLOSED_2026-09-02 (P1/P2/P3 = PRIORITY_NOT_REFUTED,
> see `wp6_s1_three_frozen_targets_priority_audit.md`) /
> NO_NOVELTY_CERTIFICATE / NO_NEW_MATHEMATICS.**
>
> Este documento organiza exclusivamente resultados S1 ya probados o
> corolarios inmediatos por ensamblaje. No abre la clasificación general de
> segundo orden, no estudia el mapa cuadrático `Q_N`, no transporta resultados
> a `2+1` o `3+1` y no modifica ningún instrumento sellado.

## 0. Decisión editorial

El paper se monta ya con tres blancos matemáticos estables:

\[
\boxed{V_N=\operatorname{Sym}^2P_{N-1}},
\qquad
\boxed{D\mathscr S_N=B_NP_N^{\rm vis}},
\qquad
\boxed{r_N(\gamma_\psi)=2\quad\forall N\ge2}.
\tag{0.1}
\]

Los dos primeros forman el núcleo all-\(N\) de primer orden. El tercero es un
corolario separado sobre una órbita exponencial antisimétrica explícita. La
clasificación de segundo orden general es opcional y no es una dependencia
lógica ni editorial del manuscrito.

```text
PAPER_FIRST = YES
FIRST_ORDER_ALL_N = CORE
SECOND_ORDER_EXPLICIT_ORBIT = SHORT_EXTENSION
GENERAL_Q_N_CLASSIFICATION = OPEN_OPTIONAL_NOT_IN_PAPER
```

## 1. Título — FIJADO (gate cerrado, 2026-09-02)

> **Exact tangent visibility of finite causal-order laws and Fisher
> resolution in the S1 model**

Subtítulo opcional:

**The S1 interaction model in a (1+1)-dimensional causal diamond**

Razón de la formulación exacta: `Exact` debe tipar únicamente la
clasificación all-\(N\) de visibilidad tangente (\(V_N\), kernel, cociente,
factorización — Teorema C, §4, y Corolario D, §5), no el espectro Fisher, que es
exacto sólo en \(N=2,3,4\) más leyes de retención asintótica sectorial
(Teorema F, §6). El título anterior ("Exact tangent visibility **and**
Fisher resolution...") dejaba ambiguo si "Exact" calificaba también a
Fisher para toda \(N\), lo cual el paper no prueba. La reformulación separa
los dos alcances mediante la sintaxis: *exact* modifica sólo *tangent
visibility*; *Fisher resolution* entra como una segunda cláusula sin
heredar ese calificador.

`causal compression` permanece exclusivamente como idea fuerte de la
Discussion (§9), no como término de título.

### Alternativas descartadas

1. **First-order compression by finite causal-order laws in the S1 model**
   — descartada: `compression` es demasiado interpretativo para encabezar
   el paper, aunque funciona bien en Discussion.
2. **Visible tangent spaces of finite unlabeled causal orders** —
   descartada: correcta pero esconde la contribución Fisher (Teorema F),
   que es sustantiva.
3. **Exact differential structure of finite causal-order laws** —
   descartada: segura pero demasiado genérica; pierde el rasgo memorable
   del resultado (el cociente por isomorfismo de poset y la resolución
   Fisher explícita).

`Causal compression` se reserva como interpretación de la Discussion. No se
usa por ahora como claim de título ni como nombre de una teoría general.

## 2. Tesis y claim principal

### 2.1. Tesis en una frase

Siguiendo la geometría estadística de leyes causales finitas de Bombelli, el
paper resuelve explícitamente el primer diferencial del canal a posets no
etiquetados en la clase S1: a cardinalidad \(N\), el canal ve exactamente
\(\operatorname{Sym}^2P_{N-1}\), codifica ese subespacio mediante una forma
Fisher positiva y anisótropa, y deja el sector antisimétrico invisible a
primer orden aunque una órbita antisimétrica concreta reaparece exactamente a
segundo orden para toda \(N\ge2\).

### 2.2. Teorema principal, versión compacta de trabajo

Sea

\[
H=L_0^2([0,1]),
\qquad
P_{N-1}=\operatorname{span}\{p_1,\ldots,p_{N-1}\},
\qquad
V_N=\operatorname{Sym}^2P_{N-1}.
\]

Bajo la identificación QMD de la derivada de la ley finita con su score,

\[
D\mathscr S_N=B_NP_N^{\rm vis},
\qquad
P_N^{\rm vis}=\Pi_{V_N}\Pi_{\rm sym},
\qquad
B_N=D\mathscr S_N|_{V_N}\quad\text{es inyectivo}.
\tag{2.1}
\]

En consecuencia,

\[
\ker D\mathscr S_N
=V_N^{\perp_{\rm sym}}\oplus\bigwedge\nolimits^2H,
\qquad
(H\widehat\otimes H)/\ker D\mathscr S_N\simeq V_N,
\tag{2.2}
\]

\[
\dim V_N=\binom N2,
\qquad
V_N\subsetneq V_{N+1},
\qquad
\overline{\bigcup_{N\ge2}V_N}
=H\widehat\otimes_{\rm sym}H.
\tag{2.3}
\]

La forma Fisher sobre el cociente visible viene dada por el operador positivo
definido

\[
F_N=B_N^*B_N:V_N\to V_N,
\qquad
D\mathscr S_N^*D\mathscr S_N
=P_N^{\rm vis}F_NP_N^{\rm vis}.
\tag{2.4}
\]

La contribución es la clasificación explícita y exacta de esta estructura en
S1, no la introducción de la geometría estadística de causal sets.

### 2.3. Extensión de segundo orden, separada del teorema principal

Para el generador antisimétrico polinómico ya construido y su senda
exponencial \(\gamma_\psi\), definir

\[
r_N(\gamma_\psi)
:=\inf\left\{k\ge1:
\left.\frac{d^k}{d\varepsilon^k}
\mu_{N,\varepsilon}^{[P]}\right|_{\varepsilon=0}\ne0\right\},
\]

con \(r_N=\infty\) si todos los jets se anulan. Entonces

\[
\boxed{r_N(\gamma_\psi)=2\qquad\forall N\ge2.}
\tag{2.5}
\]

La prueba que debe aparecer en el paper es exactamente:

\[
\text{paridad de }\mu_{N,\varepsilon}^{[P]}
\Longrightarrow r_N\ge2,
\]

\[
\mu_{2}''(0)\ne0,
\qquad
\mu_2''(0)=K_{N\to2}\mu_N''(0)
\Longrightarrow \mu_N''(0)\ne0
\Longrightarrow r_N=2.
\tag{2.6}
\]

Aquí \(K_{N\to2}\) es la composición de los kernels exactos de borrado
uniforme, independiente del parámetro.

## 3. Abstract provisional

> Building on Bombelli's statistical geometry of finite causal-set laws, we
> determine the exact first-order structure of the unlabeled causal-order
> channel in an explicit $1+1$-dimensional S1 interaction model. At the
> independent reference geometry and fixed cardinality $N$, the score
> derivative factors through the orthogonal projection onto
> $V_N=\operatorname{Sym}^2P_{N-1}$, where $P_{N-1}$ is generated by the
> first $N-1$ centered shifted-Legendre modes. The restriction of the
> differential to $V_N$ is injective; hence its kernel is the orthogonal
> symmetric complement of $V_N$, together with the full antisymmetric
> sector. The spaces $V_N$ have dimension $\binom N2$, are strictly nested,
> and have dense union in the symmetric interaction Hilbert space. We separate
> this visibility statement from statistical resolution: the latter is
> governed by a positive-definite Fisher operator on $V_N$, which is
> generally anisotropic and need not be diagonal in the natural modal basis.
> Finally, we exhibit an antisymmetric exponential orbit whose finite-poset
> law is even in the perturbation parameter and whose first nonzero jet is
> exactly of order two for every $N\ge2$. These results give a local
> differential resolution of Bombelli's finite-law construction in S1; they
> do not assert nonlinear reconstruction, a universal causal-determination
> theorem, or a classification beyond this model.

**Nota de freeze.** El abstract no usará `first`, `novel`, `for the first time`
ni equivalentes. Tras el cierre de la auditoría bibliográfica adversarial
(`bf09c54`, P1/P2/P3 = `PRIORITY_NOT_REFUTED`) esta restricción ya no es por
auditoría pendiente, sino permanente mientras `NO_NOVELTY_CERTIFICATE` siga
en pie (§10): la revisión de un especialista externo sigue siendo
obligatoria antes de cualquier afirmación de novedad.

## 4. Contribuciones declarables

| ID | Resultado | Papel en el paper | Techo de claim |
|---|---|---|---|
| C1 | \(V_N=\operatorname{Sym}^2P_{N-1}\), rango \(\binom N2\), nesting estricto y densidad simétrica | Contribución matemática principal | S1, primer orden, nulo independiente |
| C2 | Factorización \(D\mathscr S_N=B_NP_N^{\rm vis}\), kernel y cociente identificable; separación entre visibilidad y \(F_N\) | Formulación operatorial principal | Corolario funcional del span exacto; no llamar nueva teoría |
| C3 | Retención Fisher asintótica en el sector simétrico HS y espectros finitos ilustrativos | Resolución cuantitativa | Canal y normalización de referencia explícitos |
| C4 | \(r_N(\gamma_\psi)=2\) para toda \(N\ge2\) en una órbita antisimétrica explícita | Extensión corta, genuina y cerrada | Existencia estructural; no clasificación de \(\bigwedge^2H\) |

No presentar C2 como una contribución independiente de C1 si la auditoría
bibliográfica muestra que es una reformulación funcional estándar. Su valor
actual es aclarar exactamente qué proyecta el canal y qué mide Fisher.

## 5. Secuencia de resultados

### Resultado A — puente geométrico S1

Derivar desde la medida normalizada

\[
h_\psi=2\mathcal P\psi,
\qquad
\mathcal P=(I-M_u)(I-M_v),
\]

y separar generador geométrico, tangente de densidad, tangente de cópula y
score del experimento finito.

**Ancla:** `wp6_d2_geometric_tangent_classification.md`, §§3 y 9.

### Resultado B — representantes de score

Para cada clase no etiquetada \(C\),

\[
(D\mathscr S_Nf)(C)
=\frac{\langle f,R_C^{(N)}\rangle}{\mu_{N,0}(C)},
\]

y los representantes son simétricos y pertenecen a
\(\operatorname{Sym}^2P_{N-1}\).

**Ancla:** `wp6_finite_n_visible_span_pattern_preflight.md`, §§2–4.

### Teorema C — `FULL_CLASS_SUM_RANK_THEOREM`

Probar para todo \(N\ge2\)

\[
\operatorname{span}\{R_C^{(N)}\}=\operatorname{Sym}^2P_{N-1}
\]

mediante la familia de posets casi cadena, sumas de matrices de permutación y
triangularización por laplacianos de aristas.

**Ancla:** `wp6_full_class_sum_rank_theorem.md`, §§1–5.

### Corolario D — factorización exacta y cociente

Enunciar y probar (2.1)–(2.4). La prueba debe ser corta y explícita:

1. el score depende sólo de \(P_N^{\rm vis}f\);
2. el span exacto de los representantes hace inyectiva la restricción \(B_N\);
3. el complemento ortogonal del span da el kernel;
4. el cociente Hilbert se identifica isométricamente mediante
   \([f]\mapsto P_N^{\rm vis}f\).

### Corolario E — filtración de resolución

Registrar dimensión, nesting, witness universal
\(p_1\otimes p_N+p_N\otimes p_1\) y densidad de la unión visible.

**Ancla:** `wp6_full_class_sum_rank_theorem.md`, §6.

### Teorema F — resolución Fisher

Separar tres niveles:

1. soporte visible: \(P_N^{\rm vis}\);
2. métrica finita dentro del soporte: \(F_N=B_N^*B_N\);
3. retención asintótica en el sector simétrico HS.

La formulación no debe identificar \(F_N\) con la proyección. Los cálculos
\(N=2,3,4\) pueden ilustrar anisotropía y mezcla modal; no sustituyen la
prueba all-\(N\).

**Anclas:** `docs/hoja_de_ruta_septiembre_2026.md`, §§5.3–5.4;
`wp6_d2_geometric_tangent_classification.md`, §§13–15.

### Teorema G — paridad antisimétrica

Para el intercambio \(R(u,v)=(v,u)\) y un generador antisimétrico,

\[
R^*g_\varepsilon=g_{-\varepsilon},
\qquad
\mu_{N,\varepsilon}^{[P]}=\mu_{N,-\varepsilon}^{[P]}
\quad\forall N.
\]

Concluir invisibilidad exacta de primer orden sin llamarla pérdida de
información física.

**Ancla:** `docs/hoja_de_ruta_septiembre_2026.md`, §5.5.

### Corolario H — primer estrato de orden dos para toda cardinalidad

Presentar el cálculo racional exacto en \(N=2\),

\[
p_{\rm anticadena}''(0)=\frac85,
\qquad
p_{\rm cadena}''(0)=-\frac85,
\]

y propagar la no anulación a todo \(N\ge2\) por el kernel
\(K_{N\to2}\). Concluir (2.5).

**Anclas:** `docs/hoja_de_ruta_septiembre_2026.md`, §§5.6 y garbling por
borrado de §5.4.

## 6. Estructura de secciones del manuscrito

### §1. Introduction

**Estado: prosa de trabajo redactada tras el cierre de la auditoría de
prioridad (`bf09c54`, `wp6_s1_three_frozen_targets_priority_audit.md`,
`NOVELTY_CERTIFICATE = NO`). Integra los cinco precedentes; no altera
ningún teorema. El texto citable (bloque `>`) no debe contener nombres de
archivo del repo ni etiquetas internas de auditoría — esa trazabilidad
vive aquí, en la nota de estado, no en la prosa del paper.**

> Bombelli [*Statistical Lorentzian geometry and the closeness of
> Lorentzian manifolds*, arXiv:gr-qc/0002053, 2000] introduced the object
> this paper studies: the full law of an unlabeled causal poset at fixed
> cardinality $N$, sampled from a Lorentzian geometry, together with a
> statistical notion of closeness between two such laws. Janson [*Poset
> limits and exchangeable random posets*, arXiv:0902.0306, 2011] supplies
> the general limiting framework of poset kernels and consistent finite
> laws in which this construction sits, and Surya [*A Closeness Function on
> Coarse Grained Lorentzian Geometries*, arXiv:2510.19403, 2025] gives, via
> expected interval abundances, a closely related account of how increasing
> $N$ can lift degeneracies in this kind of causal compression. None of the
> three computes the differential of the finite-$N$ law at a reference
> geometry, its kernel, or its rank.
>
> We work in an explicit $1+1$-dimensional causal-diamond model (S1) with
> an independent-reference null geometry and ask the narrow question this
> leaves open: what, to first order in a perturbation of the underlying
> Lorentzian geometry, survives the map from a continuous perturbation to
> the finite unlabeled-poset law?
>
> Answering this requires two further steps that are already present,
> separately, in adjacent literatures, but not combined. First, at the
> level of *labeled* permutations rather than *unlabeled two-dimensional
> posets*, the differential of a permutation-pattern statistic around the
> uniform reference is understood in detail: Even-Zohar [*Patterns in
> Random Permutations*, Combinatorica 40, 2020, 775–804] decomposes the
> full space of pattern densities via the representation theory of $S_N$,
> isolating the standard-representation block $V_1^{\rm EZ}$ of dimension
> $(N-1)^2$, realized explicitly via $U^TA(\sigma)U$; Kurečka [*Lower bound
> on the size of a quasirandom forcing set of permutations*, Combin.
> Probab. Comput. 31, 2022] differentiates the pattern density directly,
> expressing the gradient in a Bernstein-type basis on $E_N=\mathbf1^\perp$
> via compressed permutation matrices $A_\pi|_{E_N}$ and covering-matrix
> sums $\sum_\pi t_\pi A_\pi$. Second, the abstract target module is also
> not new: Diaconis [*A generalization of spectral analysis with
> application to ranked data*, Ann. Statist. 17, 1989, 949–979] and the
> monograph [*Group Representations in Probability and Statistics*, IMS
> Lecture Notes-Monograph Series 11, 1988] give, for unordered-pair effects
> on rankings, the decomposition
> $M^{(N-2,2)}\simeq S^{(N)}\oplus S^{(N-1,1)}\oplus S^{(N-2,2)}$ — a
> module of dimension $\binom N2$ that is, up to naming, our target space
> $\operatorname{Sym}^2P_{N-1}$, illustrated already in 1988 with the
> Diallel Cross Design. And the many-to-one map from labeled permutations
> to unlabeled two-dimensional posets that we quotient by is itself
> classical combinatorics: Bayoumi, El-Zahar and Khamis [*Counting
> two-dimensional posets*, Discrete Math. 131, 1994] describe the fibers of
> this map explicitly, including their closure under $\sigma\mapsto
> \sigma^{-1}$ and the near-uniqueness of realizers for prime posets.
>
> What none of these five results does is the one step that connects them:
> sum the permutation-level differential over the fibers $\Gamma_C$ of the
> permutation-to-unlabeled-poset map, and show that the resulting
> class-sum score representatives *span* the full symmetric target module,
> \[
> \operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}
> =\operatorname{Sym}^2P_{N-1}.
> \]
> This is exactly Theorem C ($\S4$) below, and it is the hinge on which the
> rest of the paper — the exact kernel, the identifiable quotient, and the
> Fisher-resolution statement — turns. Everything else is either a direct
> corollary of this span theorem (Corollaries D, E; Theorem F) or a
> separate, self-contained second-order statement about one explicit
> antisymmetric orbit (Theorem G, Corollary H). In the compressed
> permutation-pattern language of §8 — restricting each class sum to
> $E_N=\mathbf1^\perp$ instead of working in $\operatorname{Sym}^2P_{N-1}$
> directly — the same statement reads
> $\operatorname{span}\{A_C|_{E_N}:C\in\mathcal C_N\}=\operatorname{Sym}(E_N)$,
> which is the form compared there against Kurečka's covering-matrix
> technique.
>
> We state the contribution as narrowly as the adversarial priority audit
> leaves it:
> \[
> \boxed{\text{previous work identifies the ambient permutation-level
> structure;}\quad\text{we identify exactly what survives the quotient to
> unlabeled finite causal-order laws.}}
> \]
> We write "we identify" and "we prove," not "for the first time" or
> "novel": a scoped literature search (§8) did not locate this exact
> class-sum span theorem, but the search was not an exhaustive systematic
> review — no full MathSciNet/zbMATH/Scopus/Web-of-Science coverage — and
> its absence does not certify novelty (§10).
>
> We make no claim of nonlinear reconstruction, geometric identifiability
> at finite distance, or any result about Schwarzschild, horizons, or
> higher dimensions.

Contribuciones C1–C4 (tabla §4) siguen inmediatamente a este párrafo en el
manuscrito, sin reafirmar prioridad absoluta más allá de lo anterior.

### §2. The S1 model and finite causal-order experiments

**Estado: prosa de trabajo. Ancla:**
`wp6_d2_geometric_tangent_classification.md`, §§1, 3, 5 — reproduce sus
fórmulas exactas (factor, signo y constante ya probados allí); no se
reconstruye nada de memoria.

> We work in the flat $1+1$-dimensional causal diamond in null coordinates,
> reparametrized to $D=[0,1]^2$ with the product order
> $(u,v)\preceq(u',v')\iff u\le u',\,v\le v'$, and the uniform reference
> measure $\mu_0(du\,dv)=du\,dv$. A conformal generator $\psi\in C(D;\mathbb
> R)$ defines the normalized exponential family
> \[
> g_\varepsilon=\frac{e^{2\varepsilon\psi}}{Z(\varepsilon)}g_0,\qquad
> Z(\varepsilon)=\int_De^{2\varepsilon\psi}\,d\mu_0,
> \]
> which preserves total volume at every $\varepsilon$ — not only to first
> order — and induces the sampling density $q_\varepsilon=e^{2\varepsilon
> \psi}/Z(\varepsilon)$ for a Poisson sprinkling conditioned on $N$ points.
> Differentiating at $\varepsilon=0$ gives the metric tangent
> $\dot g_0=2(\psi-\bar\psi)g_0$, with $\bar\psi$ the mean of $\psi$ under
> $\mu_0$.
>
> Four distinct objects appear along the chain from geometry to statistic,
> and we keep them notationally separate throughout: the geometric
> generator $\psi$; the log-tangent of the normalized joint density
> $t_\psi=2(\psi-\bar\psi)$; the copula-density tangent $h_\psi$, obtained
> after uniformizing both marginals,
> \[
> h_\psi(u,v)=2\big[\psi(u,v)-\psi_U(u)-\psi_V(v)+\bar\psi\big]
> =2\mathcal P\psi,\qquad \mathcal P=(I-M_u)(I-M_v),
> \]
> with $\psi_U,\psi_V$ the two marginal means of $\psi$ and $\mathcal P$
> the double-centering projection used throughout §§4–6; and the score
> $S_{N,\psi}$ of the finite discrete experiment, defined below. The joint
> and copula densities both equal $1$ at $\varepsilon=0$, so $t_\psi$ and
> $h_\psi$ agree there in value but are not the same object — they differ
> by the two marginal terms, and only $h_\psi$ is what the finite
> experiment actually sees, since passing to ranks applies the marginal
> probability integral transform and removes marginal information.
>
> A sample of $N$ points generates three progressively coarser
> observations. At the finest level is the continuous sample
> $(U_k,V_k)_{k=1}^N$ itself, with score
> $T_{N,\psi}=\sum_kh_\psi(U_k,V_k)$. Ordering by $U$ and recording the
> induced rank in $V$ produces a *labeled* rank permutation $\Pi_N\in S_N$;
> its score is the conditional expectation
> \[
> S_{N,\psi}(\pi)=\mathbb E_0[T_{N,\psi}\mid\Pi_N=\pi],
> \]
> an identity that needs no independence assumption after conditioning and
> follows directly from the likelihood. Finally — and this is the level
> the finite causal-order law actually lives on — the *unlabeled*
> two-dimensional poset is the isomorphism class $[P_{\Pi_N}]$ of the
> permutation matrix: $\Pi_N$ depends on which linear realizer of $U$ and
> of $V$ is used, but the order-only datum a causal set exposes is exactly
> this isomorphism class, invariant under the realizer. The quotient from
> the labeled permutation $\Pi_N$ to the unlabeled poset $[P_{\Pi_N}]$ —
> and exactly what survives it — is the subject of §§4–5.
>
> Write $\mathcal C_N$ for the set of isomorphism classes of
> two-dimensional posets realized by some $\sigma\in S_N$, and for
> $C\in\mathcal C_N$ let $\Gamma_C:=\{\sigma\in S_N:[P_\sigma]=C\}$ be its
> fiber under $\sigma\mapsto[P_\sigma]$. The object this paper's tangent
> statement is about is the law of the unlabeled poset itself,
> \[
> \mu_{N,\varepsilon}^{[P]}(C)
> :=\mathbb P_\varepsilon\big([P_{\Pi_N}]=C\big)
> =\sum_{\sigma\in\Gamma_C}p_\varepsilon(\sigma),
> \qquad C\in\mathcal C_N,
> \]
> with reference value $\mu_{N,0}(C)=|\Gamma_C|/N!$. This closes the chain
> the rest of the paper works with:
> \[
> \psi\ \longrightarrow\ \dot g_0\ \longrightarrow\ t_\psi\ \longrightarrow\
> h_\psi\ \longrightarrow\ S_{N,\psi}\ \longrightarrow\
> \mu_{N,\varepsilon}^{[P]}.
> \]
>
> Throughout, $H=L_0^2([0,1])$ denotes the mean-zero $L^2$ space with the
> shifted-Legendre basis, $P_{N-1}=\operatorname{span}\{p_1,\ldots,
> p_{N-1}\}\subset H$ its first $N-1$ modes, and derivatives of finite-$N$
> laws at $\varepsilon=0$ are read as scores under the quadratic-mean-
> differentiability (QMD) identification, specializing Bombelli's finite-law
> construction to this S1 exponential family.

### §3. Score representatives of the finite law

- Densidades de estadísticos de orden y base de Bernstein centrada.
- Representantes \(R_\sigma^{(N)}\) y \(R_C^{(N)}\).
- Inversión de permutaciones, simetría y cota superior del span.

### §4. Exact all-\(N\) visible subspaces

- Teorema de sumas de clase.
- Posets casi cadena.
- Laplacianos de ciclos y aristas.
- Prueba de \(V_N=\operatorname{Sym}^2P_{N-1}\).
- Dimensión, nesting y densidad.

### §5. Operator factorization and the identifiable quotient

- Factorización \(D\mathscr S_N=B_NP_N^{\rm vis}\).
- Kernel exacto y cociente canónico.
- Diferencia entre soporte visible y codificación estadística.
- Diagrama funcional del canal.

### §6. Fisher resolution inside the visible sector

- \(F_N=B_N^*B_N\) y operador Fisher ambiente.
- Positividad definida, espectro y anisotropía.
- Ejemplos exactos \(N=2,3,4\); mezcla modal a \(N=4\).
- Retención asintótica en el sector simétrico y techo de interpretación.

### §7. An antisymmetric orbit visible at second order

- Generador polinómico explícito.
- Isotropía discreta y paridad exacta.
- Definición de \(r_N\).
- Cálculo de \(\mu_2''(0)\) y propagación por borrado uniforme.
- \(r_N=2\) para todo \(N\ge2\).
- No caracterización de \(Q_N\) ni de su cono cuadrático nulo.

### §8. Relation to prior work

**Estado: prosa de trabajo redactada tras el cierre de la auditoría de
prioridad (`bf09c54`). Reproduce las adjudicaciones de
`wp6_s1_three_frozen_targets_priority_audit.md` §§3.1–3.7; no reabre nada.**

**Causal-set framework.** Bombelli (2000) precedes the framework in full:
the full unlabeled-poset law at fixed cardinality, its compression to a
finite probability list, and the question of small geometric variations.
Janson (2011) supplies the global poset-limit framework these finite laws
sit inside. Surya (2025) precedes the general narrative that increasing
$N$ can lift degeneracies of a causal compression, via expected interval
abundances — a distinct compressed object from ours. None of the three
computes the S1 differential, its rank, or its kernel.

**Permutation-to-poset fibers.** Bayoumi, El-Zahar and Khamis (1994) work
explicitly with the many-to-one correspondence between permutations and
two-dimensional posets, and record its closure under
$\sigma\mapsto\sigma^{-1}$ and the near-uniqueness of realizers for prime
posets. They do not sum a matrix-valued statistic over a fiber, differ­
entiate a sampling law, or prove a span theorem on $E_N$.

**Pre-quotient permutation differential.** Even-Zohar (2020) is the
closest neighbor to the pre-quotient side of our construction: the
standard-representation block $V_1^{\rm EZ}$, dimension $(N-1)^2$, realized
via $U^TA(\sigma)U$. His scaling regime ($n\to\infty$ fluctuations of a
random permutation's pattern profile) must not be identified without proof
with our first jet in the local S1 parameter $\varepsilon$, and he does not
sum over unlabeled-poset isomorphism fibers. Kurečka (2022) is the
mandatory differential precursor at the labeled-permutation level: he
differentiates the pattern density $d(\pi,\mu)$ exactly around the uniform
permuton, defines the gradient polynomial $P_\pi(\alpha,\beta)$ with
coefficients $c_{ij}(P_\pi)=K_{ij,N}(\mathbf b_{i+2}^N)^TA_\pi\mathbf
b_{j+2}^N$, and characterizes vanishing combinations via the covering
matrix $\sum_\pi t_\pi A_\pi$. This precedes, substantially, the finite
polynomials, the Bernstein-type basis, the compression of permutation
matrices to $E_N$, and the covering-matrix technique used in §§3–4 below;
none of these should be presented as new. What Kurečka does not do is our
additional quotient — summing $A_\sigma$ over the fiber $\Gamma_C$ of
permutations mapping to a fixed unlabeled poset $C$, and proving that the
resulting $\{A_C|_{E_N}\}$ span all of $\operatorname{Sym}(E_N)$. Chan,
Král', Noel, Pehova, Sharifzadeh and Volec (2019/2020) and Garbe, Král',
Malekshahian and Penaguiao (2023/2025) are adjacent permuton-forcing and
feasible-region results that likewise do not supply this span theorem and
rule out generic phrases like "first classification of the degrees of
freedom of pattern densities."

**Abstract target module.** Diaconis (1989) decomposes functions on
rankings via $S_N$ representation theory and gives, for unordered-pair
effects, $M^{(N-2,2)}\simeq S^{(N)}\oplus S^{(N-1,1)}\oplus S^{(N-2,2)}$ —
already the module and the $\binom N2$ dimension behind a Johnson-scheme
reformulation of $\operatorname{Sym}(E_N)$. The 1988 monograph makes this
concrete and precedes it further: Ch. 8 (Diallel Cross Design, p. 155)
instantiates the same module on unordered pairs of $n$ varieties with the
identical decomposition, and Ch. 9 develops the associated model family.
Neither work introduces unlabeled two-dimensional-poset fibers, their
class sums, or a proof that those class sums span the full module. Chapter
5 of the monograph (verified in full, `bf09c54`) is a purely motivational
examples chapter with no theorems at all, and the full index (pp. 193–198)
contains no entry for "poset" or "partially ordered set" anywhere in the
book. So the symmetric representation and its decomposition are not new;
the class-sum span theorem over poset-isomorphism fibers is the piece not
located.

**Rank statistics and copulas.** Hallin, Mellouk and Rifi (2001) precede
Bernstein-polynomial appearances in rank-statistic projections (Hájek
projections, asymptotic approximation, not our exact finite-$N$ score
span). Hoff (2007) establishes the rank likelihood as a marginal-free
semiparametric likelihood; Sei and Matsumoto (2020) and Hoff, Niu and
Wellner (2014) develop the induced divergence and efficient geometry of
Gaussian-copula/rank models, including finite-$n$ identifiability loss.
None of these adds the additional quotient from a full permutation to an
unlabeled poset, or the equality $V_N=\operatorname{Sym}^2P_{N-1}$ for a
nonparametric S1 tangent.

**What §§3–7 must therefore not claim.** The full pre-quotient standard
block, the differential/Bernstein/covering-matrix technique at the
permutation level, and the abstract unordered-pair symmetric module are
all preceded and must be cited as such, not presented as contributions.
The single package that should go to an external permuton/rank-statistics
specialist is the implication chain of §6.3 of the priority audit: pattern
gradient $\to A_\sigma|_{E_N}$ (near Kurečka) $\to$ poset-isomorphism class
sum $A_C=\sum_{\sigma\in\Gamma_C}A_\sigma$ $\to$
$\operatorname{span}\{A_C|_{E_N}\}=\operatorname{Sym}(E_N)$ $\to$
$V_N=\operatorname{Sym}^2P_{N-1}$ and $D\mathscr S_N=B_NP_N^{\rm vis}$.
Distinguish, throughout, the Fisher spectrum on $V_N$ from the spectrum of
any operator defined on a single realized causet.

### §9. Discussion: causal compression

Recuperar la interpretación de que **el pasado y el futuro causales comprimen
el presente**, anclada exclusivamente a

\[
D\mathscr S_N=B_NP_N^{\rm vis},
\qquad
V_N=\operatorname{Sym}^2P_{N-1}.
\]

La ley finita no retiene una perturbación continua punto a punto: retiene sólo
su componente visible a primer orden. Aumentar \(N\) amplía estrictamente esa
resolución. El sector antisimétrico permanece invisible a primer orden y el
testigo de §7 muestra que puede reaparecer a orden superior.

**Prohibido:** convertir esta lectura en un teorema universal según el cual el
pasado y el futuro determinan el presente.

### §10. Limitations and open problems

- Prioridad bibliográfica all-\(N\) pendiente.
- Realizabilidad geométrica de un tangente HS arbitrario abierta.
- Sector antisimétrico general a segundo orden abierto.
- No clasificación de \(Q_N\) ni de su cono cuadrático nulo.
- No convergencia en norma del operador Fisher relativo.
- No resultados fuera de S1 o en dimensiones superiores.

### §11. Conclusion

Repetir sólo C1–C4 y cerrar con la distinción:

\[
\text{visibilidad}=V_N,
\qquad
\text{resolución estadística}=F_N,
\qquad
\text{orden superior}=r_N(\gamma_\psi)=2\text{ para un testigo}.
\]

## 7. Apéndices previstos

| Apéndice | Contenido |
|---|---|
| A | Derivación QMD y fórmula de representantes de score |
| B | Reducción finita a \(\operatorname{Sym}(E_N)\) |
| C | Familia casi cadena y triangularización por laplacianos |
| D | Pruebas de kernel, nesting y densidad |
| E | Cotas Hilbert–Schmidt y retención Fisher |
| F | Matrices y espectros exactos en \(N=2,3,4\) |
| G | Derivadas de segundo orden y kernel de borrado uniforme |

## 8. Figuras y tablas mínimas

1. **Diagrama del diferencial:**
   \(H\widehat\otimes H\xrightarrow{P_N^{\rm vis}}V_N
   \xrightarrow{B_N}L_0^2(\mu_{N,0})\), con el kernel separado en sector
   simétrico invisible y sector antisimétrico.
2. **Filtración visible:** dimensiones
   \(1,3,6,10,\ldots,\binom N2\) y witness de cada inclusión estricta.
3. **Órbita plegada:** \(\varepsilon\leftrightarrow-\varepsilon\) identificados
   por la reflexión, con coordenada observable local
   \(\theta=\varepsilon^2\).
4. **Tabla de claims:** resultado, hipótesis, canal y afirmaciones prohibidas.

No se propone ninguna figura numérica nueva ni se autoriza simulación.

## 9. Auditoría bibliográfica adversarial posterior al skeleton

### Blanco P1 — espacio visible all-\(N\)

Buscar equivalentes de

\[
\operatorname{span}\{R_C^{(N)}\}
=\operatorname{Sym}^2P_{N-1}
\]

en causal sets, posets de permutación, clases cerradas bajo inversión,
estadística de rangos, cópulas, permutones, álgebras de clases y
representación de \(S_N\).

### Blanco P2 — diferencial y cociente

Buscar una identificación equivalente del kernel/rango del diferencial de la
ley completa, aunque no use lenguaje Fisher. Distinguir un antecedente
matemático sustantivo de la consecuencia funcional estándar
`span exacto -> proyección + restricción inyectiva`.

### Blanco P3 — segundo jet de la órbita

Buscar antecedentes de paridad por inversión/reflexión, identificabilidad en
\(|\varepsilon|\) o \(\theta=\varepsilon^2\), y propagación all-\(N\) de un
segundo jet no nulo mediante consistencia proyectiva o borrado uniforme.

### Salidas permitidas

```text
PRECEDED
KNOWN_THEOREM_SPECIALIZATION
PRIORITY_NOT_REFUTED
NO_EXACT_PRECEDENT_FOUND_IN_SCOPED_SEARCH
```

Ninguna salida equivale por sí sola a `NOVELTY_CERTIFIED = YES`.

## 10. Claim ceiling vinculante

```text
FRAMEWORK_NOVELTY = NO                         # Bombelli
GENERIC_MORE_N_MORE_RESOLUTION_NOVELTY = NO    # Surya y literatura previa
EXACT_S1_ALL_N_DIFFERENTIAL_CLASSIFICATION = PRIORITY_AUDIT_PENDING
SECOND_ORDER_GENERAL_CLASSIFICATION = OPEN_NOT_REQUIRED
GEOMETRIC_REALIZABILITY_OF_ARBITRARY_HS = OPEN
NONLINEAR_RECONSTRUCTION = NOT_CLAIMED
UNIVERSAL_PAST_FUTURE_DETERMINES_PRESENT = NOT_CLAIMED
HORIZON_OR_SCHWARZSCHILD_RESULT = NO
DIMENSION_2PLUS1_OR_HIGHER = NOT_OPENED
RELATIVE_OPERATOR_NORM_CONVERGENCE = REFUTED
NOVELTY_CERTIFICATE = NO
```

El teorema abstracto de Hoeffding causal actualmente en `dev/` queda fuera de
este paper: está marcado `DEV_EXPLORATION / NOT_COMMITTEE_REVIEWED`, responde a
otro problema dimensional y ampliaría el claim sin ser necesario para la
historia S1.

## 11. Anclas documentales

1. `research_program/work_packages/wp6_d2_geometric_tangent_classification.md`
2. `research_program/work_packages/wp6_finite_n_visible_span_pattern_preflight.md`
3. `research_program/work_packages/wp6_full_class_sum_rank_theorem.md`
4. `research_program/work_packages/wp6_d2_geometric_fisher_retention.md`
5. `research_program/work_packages/wp6_d2_modular_fiber_score.md`
6. `docs/hoja_de_ruta_septiembre_2026.md`, §§5.3–5.6
7. `research_program/bibliography/wp6_finite_causal_order_fisher_spectrum_priority_audit.md`
8. `research_program/bibliography/wp6_bombelli_citation_chain_adversarial_audit.md`
9. `research_program/bibliography/wp6_external_rederivation_package_full_class_sum_rank_theorem.md`

## 12. Gate antes de redactar el cuerpo completo

1. Confirmar que el PI acepta el título y la tesis de §§1–2. **HECHO**
   (`d3011f7`) — título fijado, tesis de §2.1 sin cambios, alineada.
2. Ejecutar la auditoría de prioridad contra P1–P3 sin mover los blancos.
   **HECHO** — `wp6_s1_three_frozen_targets_priority_audit.md`, `bf09c54`.
3. Clasificar cada pieza como `PRECEDED`, `KNOWN_THEOREM_SPECIALIZATION` o
   `PRIORITY_NOT_REFUTED`. **HECHO** — ver tabla ejecutiva de la auditoría.
4. Ajustar Introduction, Related Work y abstract sin alterar los teoremas.
   **BORRADOR HECHO** (este commit, §§1 y 8) — pendiente de aceptación del
   PI, no de auditoría adicional.
5. Redactar el cuerpo desde las anclas de §11; no reconstruir pruebas de
   memoria. **EN CURSO**: §2 (dominio S1, cuatro objetos, tres niveles
   observacionales) redactado, ancla `wp6_d2_geometric_tangent_
   classification.md` §§1,3,5. Pendientes en orden: §4 (Teorema all-\(N\)),
   §6 (Fisher \(N=2,3,4\) + asintótica), §7 (senda antisimétrica,
   \(r_N=2\)), §9 (Discussion / causal compression), §11 (Conclusion +
   claim ceiling). §3, §5, §10 y apéndices después del cuerpo continuo.
6. Mantener fuera \(Q_N\) general salvo que el manuscrito revele una laguna
   lógica real y se emita una autorización separada.
