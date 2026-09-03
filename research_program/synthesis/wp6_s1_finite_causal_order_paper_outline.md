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

> Bombelli's statistical geometry of finite causal-set laws gives us the
> object we study here: the unlabeled causal-order channel of an explicit
> $1+1$-dimensional S1 interaction model, expanded at an independent
> reference geometry. For each fixed cardinality $N$, the score derivative
> factors through the orthogonal projection onto
> $V_N=\operatorname{Sym}^2P_{N-1}$, where $P_{N-1}$ is generated by the
> first $N-1$ centered shifted-Legendre modes, and this restriction to
> $V_N$ is injective, so its kernel is the orthogonal symmetric complement
> of $V_N$ together with the full antisymmetric sector. The spaces $V_N$
> have dimension $\binom N2$, are strictly nested, and their union is
> dense in the symmetric interaction Hilbert space. Visibility and
> statistical resolution turn out to be different questions: a
> positive-definite Fisher operator on $V_N$ governs the latter, is
> generally anisotropic, and need not be diagonal in the natural modal
> basis, so visible modes can mix before they are resolved. We also
> exhibit an antisymmetric exponential orbit whose finite-poset law is
> even in the perturbation parameter, yet whose first nonzero jet is
> exactly of order two for every $N\ge2$. This is a local differential
> resolution of Bombelli's finite-law construction in S1, not a claim of
> nonlinear reconstruction or universal causal determination, and it does
> not extend beyond this model.

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
> laws in which this construction sits. Surya [*Closeness function on
> coarse grained Lorentzian geometries*, Phys. Rev. D 113, 024034, 2026,
> arXiv:2510.19403] gives, via expected interval abundances, a closely
> related account of how
> increasing $N$ can lift degeneracies in this kind of causal compression.
> None of the three computes the differential of the finite-$N$ law at a
> reference geometry, its kernel, or its rank.
>
> We work in an explicit $1+1$-dimensional causal-diamond model (S1) with
> an independent-reference null geometry. The question we ask is narrow:
> to first order in a perturbation of the underlying Lorentzian geometry,
> what survives the map from a continuous perturbation to the finite
> unlabeled-poset law?
>
> Two pieces of an answer already exist, in adjacent literatures, without
> being combined. At the level of *labeled* permutations rather than
> *unlabeled two-dimensional posets*, the differential of a
> permutation-pattern statistic around the uniform reference is
> understood in some detail. Even-Zohar [*Patterns in Random
> Permutations*, Combinatorica 40, 2020, 775–804] decomposes the full
> space of pattern densities via the representation theory of $S_N$,
> isolating the standard-representation block $V_1^{\rm EZ}$ of dimension
> $(N-1)^2$, realized explicitly via $U^TA(\sigma)U$. Kurečka [*Lower
> bound on the size of a quasirandom forcing set of permutations*,
> Combin. Probab. Comput. 31, 2022] differentiates the pattern density
> directly, expressing the gradient in a Bernstein-type basis on
> $E_N=\mathbf1^\perp$ via compressed permutation matrices
> $A_\pi|_{E_N}$ and covering-matrix sums $\sum_\pi t_\pi A_\pi$.
>
> The abstract target module is not new either. Diaconis [*A
> generalization of spectral analysis with application to ranked data*,
> Ann. Statist. 17, 1989, 949–979] and the monograph [*Group
> Representations in Probability and Statistics*, IMS Lecture
> Notes-Monograph Series 11, 1988] give, for unordered-pair effects on
> rankings, the decomposition
> $M^{(N-2,2)}\simeq S^{(N)}\oplus S^{(N-1,1)}\oplus S^{(N-2,2)}$ — a
> module of dimension $\binom N2$ that is, up to naming, our target space
> $\operatorname{Sym}^2P_{N-1}$, illustrated already in 1988 with the
> Diallel Cross Design. And the many-to-one map from labeled permutations
> to unlabeled two-dimensional posets that we quotient by is itself
> classical combinatorics: Bayoumi, El-Zahar and Khamis [*Counting
> two-dimensional posets*, Discrete Math. 131, 1994] describe the fibers
> of this map explicitly, including their closure under $\sigma\mapsto
> \sigma^{-1}$ and the near-uniqueness of realizers for prime posets.
>
> None of these five results takes the one further step that connects
> them: sum the permutation-level differential over the fibers $\Gamma_C$
> of the permutation-to-unlabeled-poset map, and show that the resulting
> class-sum score representatives *span* the full symmetric target
> module,
> \[
> \operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}
> =\operatorname{Sym}^2P_{N-1}.
> \]
> This is Theorem C ($\S4$) below. The exact kernel, the identifiable
> quotient, and the Fisher-resolution statement all turn on it.
> Corollaries D and E and Theorem F follow from it directly; Theorem G
> and Corollary H are a separate, self-contained second-order statement
> about one explicit antisymmetric orbit. Fisher resolution and that
> second-order orbit are substantive results with their own content, not
> footnotes to the span theorem. In the compressed permutation-pattern
> language of §8, restricting each class sum to $E_N=\mathbf1^\perp$
> instead of working in $\operatorname{Sym}^2P_{N-1}$ directly, the same
> statement reads
> $\operatorname{span}\{A_C|_{E_N}:C\in\mathcal C_N\}=\operatorname{Sym}(E_N)$,
> the form compared there against Kurečka's covering-matrix technique.
>
> Put narrowly, this is the contribution:
> \[
> \boxed{\text{previous work identifies the ambient permutation-level
> structure;}\quad\text{we identify exactly what survives the quotient to
> unlabeled finite causal-order laws.}}
> \]
> We write "we identify" and "we prove," not "for the first time" or
> "novel." The individual ingredients above have substantial precedents,
> discussed in §8. We are not aware of this exact class-sum span theorem
> already stated in the literature, but that is not the same thing as a
> claim that none exists (§10).
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

**Estado: prosa de trabajo. Ancla:**
`wp6_finite_n_visible_span_pattern_preflight.md`, §§2–5. Ésta es la
definición normativa de \(R_\sigma^{(N)}\), \(R_C^{(N)}\) y
\(G_{[P]}^{(N)}\) para el manuscrito. La reducción matricial usa
\(\Lambda_N:E_N\to P_{N-1}\).

> For \(i=1,\ldots,N\), let
> \[
> d_i^{(N)}(t)
> :=N\binom{N-1}{i-1}t^{i-1}(1-t)^{N-i}
> \tag{3.1}
> \]
> be the density of the \(i\)-th order statistic in a sample of \(N\)
> independent uniform variables, and define its centered version
> \[
> b_i^{(N)}:=d_i^{(N)}-1.
> \tag{3.2}
> \]
> The normalized functions \(d_i^{(N)}/N\) form the Bernstein basis of
> degree \(N-1\). Since
> \[
> \sum_{i=1}^N d_i^{(N)}=N,
> \qquad
> \sum_{i=1}^N b_i^{(N)}=0,
> \]
> centering leaves exactly one linear relation and therefore
> \[
> \operatorname{span}\{b_1^{(N)},\ldots,b_N^{(N)}\}=P_{N-1}.
> \tag{3.3}
> \]
>
> Let \(f=\mathcal P\psi\in H\widehat\otimes H\) be an admissible S1
> interaction tangent, so the score of one observation of the copula at the
> reference model is \(2f\). If \(p_\varepsilon(\sigma)\) denotes the
> probability of the rank permutation \(\sigma\in S_N\), differentiation
> of its finite likelihood gives
> \[
> p_\sigma'(0;f)
> =\frac2{N!}\sum_{i=1}^N
> \left\langle f,
> d_i^{(N)}\otimes d_{\sigma(i)}^{(N)}\right\rangle.
> \tag{3.4}
> \]
> Both marginals of \(f\) vanish. Hence each \(d_i^{(N)}\) in (3.4) may be
> replaced by \(b_i^{(N)}\), and the permutation-level representative is
> defined by
> \[
> \boxed{
> R_\sigma^{(N)}
> :=\frac2{N!}\sum_{i=1}^N
> b_i^{(N)}\otimes b_{\sigma(i)}^{(N)},
> \qquad
> p_\sigma'(0;f)=\langle f,R_\sigma^{(N)}\rangle.}
> \tag{3.5}
> \]
> In particular,
> \(R_\sigma^{(N)}\in P_{N-1}\otimes P_{N-1}\). Formula (3.5), initially
> obtained for admissible continuous tangents, also defines a continuous
> linear functional of every \(f\in H\widehat\otimes H\); below we use this
> Hilbert-space extension without claiming that every such \(f\) is
> geometrically realizable.
>
> Recall from §2 that \(\mathcal C_N\) is the set of unlabeled
> two-dimensional poset classes generated at cardinality \(N\), and
> \(\Gamma_C=\{\sigma\in S_N:[P_\sigma]=C\}\) is the fiber of
> \(C\in\mathcal C_N\). The class representative is
> \[
> \boxed{
> R_C^{(N)}:=\sum_{\sigma\in\Gamma_C}R_\sigma^{(N)}.}
> \tag{3.6}
> \]
> Since \(\mu_{N,0}(C)=|\Gamma_C|/N!>0\), summing (3.5) over the fiber gives
> \[
> \left.\frac{d}{d\varepsilon}
> \mu_{N,\varepsilon}^{[P]}(C)\right|_{\varepsilon=0}
> =\langle f,R_C^{(N)}\rangle,
> \qquad
> (D\mathscr S_Nf)(C)
> =\frac{\langle f,R_C^{(N)}\rangle}{\mu_{N,0}(C)}.
> \tag{3.7}
> \]
> Thus \(D\mathscr S_Nf\) is exactly the score of the finite unlabeled-poset
> law. Its \(\mu_{N,0}\)-mean is zero because the derivatives in (3.7) sum
> to zero over \(C\).
>
> Each fiber is closed under inversion: if \(i<j\) then
> \(\sigma(i)<\sigma(j)\), so setting \(a=\sigma(i)\), \(b=\sigma(j)\)
> gives \(a<b\) and \(\sigma^{-1}(a)=i<j=\sigma^{-1}(b)\), i.e.
> \(i\mapsto\sigma(i)\) is a poset isomorphism \(P_{\sigma^{-1}}\cong
> P_\sigma\), so interchanging the two rank coordinates sends \(\sigma\)
> to \(\sigma^{-1}\) without changing the abstract poset. Consequently,
> \[
> \sigma\in\Gamma_C\Longleftrightarrow\sigma^{-1}\in\Gamma_C,
> \qquad
> \left(R_\sigma^{(N)}\right)^\top=R_{\sigma^{-1}}^{(N)},
> \]
> and hence
> \[
> \boxed{
> \left(R_C^{(N)}\right)^\top=R_C^{(N)},
> \qquad
> R_C^{(N)}\in\operatorname{Sym}^2P_{N-1}.}
> \tag{3.8}
> \]
>
> The Fisher bilinear form of the unlabeled-poset experiment is therefore
> defined by
> \[
> \boxed{
> G_{[P]}^{(N)}(f,g)
> :=\langle D\mathscr S_Nf,D\mathscr S_Ng\rangle_{L^2(\mu_{N,0})}
> =\sum_{C\in\mathcal C_N}
> \frac{\langle f,R_C^{(N)}\rangle
> \langle g,R_C^{(N)}\rangle}{\mu_{N,0}(C)}.}
> \tag{3.9}
> \]
> Because every reference mass is strictly positive,
> \[
> \ker D\mathscr S_N=\ker G_{[P]}^{(N)}
> =\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}^{\perp},
> \]
> and the visible space is equivalently
> \[
> \boxed{
> V_N
> :=(\ker D\mathscr S_N)^\perp
> =\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}
> \subseteq\operatorname{Sym}^2P_{N-1}.}
> \tag{3.10}
> \]
> This is the upper inclusion used in §4.
>
> To state the remaining finite reduction, put
> \[
> E_N:=\mathbf1^\perp\subset\mathbb R^N,
> \qquad
> \Lambda_N:E_N\longrightarrow P_{N-1},
> \qquad
> \Lambda_Nz:=\sum_{i=1}^Nz_i b_i^{(N)}.
> \tag{3.11}
> \]
> Equation (3.3) and the single relation \(\sum_i b_i^{(N)}=0\) show that
> \(\Lambda_N\) is an isomorphism. Fix the permutation-matrix convention
> \[
> P_\sigma:=\sum_{i=1}^Ne_i e_{\sigma(i)}^\top,
> \qquad
> A_C:=\sum_{\sigma\in\Gamma_C}P_\sigma.
> \tag{3.12}
> \]
> Closure of \(\Gamma_C\) under inversion makes \(A_C\) symmetric, and
> (3.5)–(3.6) give exactly
> \[
> R_C^{(N)}
> =\frac2{N!}\sum_{i,j=1}^N(A_C)_{ij}
> b_i^{(N)}\otimes b_j^{(N)}.
> \tag{3.13}
> \]
> Transporting by the isomorphism \(\Lambda_N\) therefore reduces the reverse
> inclusion in (3.10) to
> \[
> \boxed{
> V_N=\operatorname{Sym}^2P_{N-1}
> \quad\Longleftrightarrow\quad
> \operatorname{span}\{A_C|_{E_N}:C\in\mathcal C_N\}
> =\operatorname{Sym}(E_N).}
> \tag{3.14}
> \]
> Section 4 proves the right-hand statement constructively for every
> \(N\ge2\). The Bernstein and permutation-level differential machinery in
> this section is not claimed as new; the all-\(N\) contribution isolated in
> §4 is the span that survives after summing over the unlabeled-poset fibers.

### §4. Exact all-\(N\) visible subspaces

**Estado: prosa de trabajo. Ancla:** `wp6_full_class_sum_rank_theorem.md`,
§§1–5 y §6.1–6.3 (el kernel de §6.4 se difiere a §5, Corolario D — no se
incluye aquí). Notación \(n\to N\) respecto del archivo fuente, para casar
con el resto del manuscrito; fórmulas y numeración interna reproducidas sin
reconstrucción de memoria. Las definiciones de \(G_{[P]}^{(N)}\),
\(R_C^{(N)}\), \(E_N\), \(P_\sigma\) y \(A_C\), así como la reducción
matricial, son exclusivamente las de §3; §4 no introduce una segunda
convención.

> By (3.10), the visible space
> $V_N=\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}$ satisfies
> $V_N\subseteq\operatorname{Sym}^2P_{N-1}$. Under the isomorphism
> $\Lambda_N$ of (3.11), equation (3.14) reduces the reverse inclusion to
> the following purely combinatorial statement about the class sums defined
> in (3.12):
> \[
> \operatorname{span}\{A_C|_{E_N}:C\in\mathcal C_N\}=\operatorname{Sym}(E_N).
> \tag{4.1}
> \]
>
> **A family of $\binom N2$ near-chain posets.** For integers
> $0\le a<b\le N-1$, define $C_{a,b}$ on a chain $c_1<\cdots<c_{N-1}$
> together with one extra element $z$ satisfying $c_i<z$ for $i\le a$,
> $z<c_i$ for $i>b$, and $z$ incomparable with $c_{a+1},\ldots,c_b$. Every
> linear extension inserts $z$ after exactly $k\in\{a,\ldots,b\}$ elements
> of the chain, and two extensions realize the same order relation exactly
> when $\{s,t\}=\{a,b\}$: the poset has exactly two linear-extension
> pairs, giving, once the chain is normalized to $1<\cdots<N$, a single
> cycle $\tau_{a,b}$ on the consecutive interval $I_{a,b}=\{a+1,\ldots,
> b+1\}$ and its inverse. Hence
> \[
> \Gamma_{C_{a,b}}=\{\tau_{a,b},\tau_{a,b}^{-1}\}
> \]
> (a single transposition, without multiplicity, when $b=a+1$). The
> multiset of strict-past cardinalities $\{|\mathrm{Past}(y)|:y\in
> C_{a,b}\}=\{0,\ldots,b-1,b+1,\ldots,N-1\}\uplus\{a\}$ is missing $b$ and
> repeats $a$, so it determines the pair $(a,b)$: the $\binom N2$ classes
> $C_{a,b}$ are pairwise distinct.
>
> **From interval cycles to edge Laplacians.** For $1\le i<j\le N$ let
> $L_{ij}:=(e_i-e_j)(e_i-e_j)^\top$ be the Laplacian of edge $\{i,j\}$ in
> the complete graph on $N$ vertices. Restricted to $E_N$, the $\binom N2$
> matrices $\{L_{ij}\}$ are linearly independent — a vanishing combination
> forces every off-diagonal coefficient, hence every $w_{ij}$, to vanish —
> so they form a basis of $\operatorname{Sym}(E_N)$; they also satisfy
> $\sum_{i<j}L_{ij}=NI_{E_N}$. Set
> $S_{a,b}:=P_{\tau_{a,b}}+P_{\tau_{a,b}}^\top$ — equal to $2A_{C_{a,b}}$
> when $b=a+1$ and to $A_{C_{a,b}}$ otherwise, a nonzero scalar either way
> — and $Q_{a,b}:=2I_{E_N}-S_{a,b}|_{E_N}$. Because $\tau_{a,b}$ is the
> consecutive cycle on $I_{a,b}$, $Q_{a,b}$ is exactly that cycle's graph
> Laplacian: $Q_{a,a+1}=2L_{a+1,a+2}$, and for $b>a+1$,
> $Q_{a,b}=L_{a+1,b+1}+\sum_{k=a+1}^bL_{k,k+1}$. These two identities
> triangularize by interval length and invert cleanly —
> $L_{i,i+1}=\tfrac12Q_{i-1,i}$, and for $j>i+1$,
> $L_{ij}=Q_{i-1,j-1}-\tfrac12\sum_{k=i}^{j-1}Q_{k-1,k}$ — so
> \[
> \operatorname{span}\{Q_{a,b}\}=\operatorname{span}\{L_{ij}:i<j\}
> =\operatorname{Sym}(E_N).
> \tag{4.2}
> \]
> This leaves exactly one gap: (4.2) uses the shared term $2I_{E_N}$
> subtracted out of every $Q_{a,b}$, so it does not by itself show that
> the class sums $S_{a,b}$ span the same space.
>
> **Closing the gap: the identity is itself a class-sum combination.**
> From $\sum_{i<j}L_{ij}=NI_{E_N}$ and the triangularized identities
> above, $I_{E_N}=\sum_{a<b}c_{a,b}Q_{a,b}$ for explicit coefficients
> $c_{a,b}$ whose sum depends only on how many edges sit at each distance
> $d=j-i$:
> \[
> s_N:=\sum_{a<b}c_{a,b}
> =\frac1N\sum_{d=1}^{N-1}(N-d)\Bigl(1-\frac d2\Bigr)
> =\frac{(N-1)(5-N)}{12}.
> \]
> Substituting $Q_{a,b}=2I_{E_N}-S_{a,b}|_{E_N}$ gives
> $(1-2s_N)I_{E_N}=-\sum_{a<b}c_{a,b}S_{a,b}|_{E_N}$, and the coefficient
> \[
> 1-2s_N=\frac{N^2-6N+11}6=\frac{(N-3)^2+2}6
> \]
> is strictly positive for every integer $N$ — it never vanishes, at
> $N=3$ or anywhere else — so
> $I_{E_N}\in\operatorname{span}\{S_{a,b}|_{E_N}\}$. Feeding this back
> into $Q_{a,b}=2I_{E_N}-S_{a,b}|_{E_N}$ shows every $Q_{a,b}$ is itself in
> that span, and with (4.2),
> \[
> \operatorname{span}\{S_{a,b}|_{E_N}:a<b\}=\operatorname{Sym}(E_N).
> \]
> Since each $S_{a,b}$ is $A_{C_{a,b}}$ up to a nonzero scalar, this is
> exactly (4.1). Combined with §3's reduction, this proves:
>
> **Theorem C.** *For every $N\ge2$,*
> \[
> \boxed{V_N=\operatorname{Sym}^2P_{N-1},\qquad
> \dim V_N=\operatorname{rank}G_{[P]}^{(N)}=\binom N2.}
> \]
> *The proof is constructive at every $N$: it exhibits, and does not
> merely count, an explicit family of $\binom N2$ poset classes whose
> score representatives span the target space, without enumerating posets
> or extrapolating from small $N$.*
>
> **Corollary E (filtration).** Since $P_{N-1}\subsetneq P_N$,
> \[
> V_N=\operatorname{Sym}^2P_{N-1}\subsetneq\operatorname{Sym}^2P_N=V_{N+1}
> \qquad(N\ge2),
> \]
> with rank sequence $1,3,6,10,15,\ldots,\binom N2,\ldots$ — a strict
> inclusion, not merely non-decreasing, at every step. A universal witness
> of each new degree is $p_1\otimes p_N+p_N\otimes p_1\in V_{N+1}\setminus
> V_N$: since the Fisher form is positive definite on $V_{N+1}$ and
> vanishes on $V_N^\perp$, $I_N^{[P]}(p_1\otimes p_N)=0$ while
> $I_{N+1}^{[P]}(p_1\otimes p_N)>0$ — the same witness recurs in the
> Fisher computations of §6. Because centered polynomials are dense in
> $H=L_0^2([0,1])$, Theorem C also gives, unconditionally,
> \[
> \overline{\bigcup_{N\ge2}V_N}=H\widehat\otimes_{\mathrm{sym}}H.
> \]
>
> The exact kernel of $D\mathscr S_N$ — the orthogonal complement of $V_N$
> together with the permanently invisible antisymmetric sector
> $\bigwedge^2H$ — is not derived here; it is Corollary D, §5, the direct
> functional consequence of Theorem C once the span is known.
>
> The finite reduction used in the argument is recorded in Appendix B,
> while Appendix C collects the almost-chain and Laplacian construction in
> full detail.

### §5. Operator factorization and the identifiable quotient

**Estado: prosa de trabajo. Anclas:** §2 para la identificación QMD del
diferencial con el score de la ley finita y §4, Teorema C, para la igualdad
exacta \(V_N=\operatorname{Sym}^2P_{N-1}\). Esta sección no usa todavía la
fórmula de representantes de §3 y no redefine ni \(R_C^{(N)}\) ni
\(G_{[P]}^{(N)}\).

> Let
> \[
> \mathcal X:=H\widehat\otimes H,
> \qquad
> \mathcal K_N:=L_0^2(\mathcal C_N,\mu_{N,0}),
> \]
> where \(\mathcal K_N\) is the Hilbert space of mean-zero scores of the
> finite unlabeled-poset law at the reference model. Under the QMD
> identification of §2, write
> \[
> D\mathscr S_N:\mathcal X\longrightarrow\mathcal K_N
> \]
> for its bounded score differential. The visible subspace is, by
> definition,
> \[
> V_N=(\ker D\mathscr S_N)^\perp.
> \tag{5.1}
> \]
> Theorem C identifies this abstract support exactly:
> \[
> V_N=\operatorname{Sym}^2P_{N-1}.
> \tag{5.2}
> \]
> Denote by \(\Pi_{\rm sym}\) the orthogonal projection of \(\mathcal X\)
> onto \(H\widehat\otimes_{\rm sym}H\), by \(\Pi_{V_N}\) the projection of
> the latter space onto \(V_N\), and set
> \[
> P_N^{\rm vis}:=\Pi_{V_N}\Pi_{\rm sym}.
> \tag{5.3}
> \]
> Thus
> \[
> \mathcal X
> =V_N\oplus V_N^{\perp_{\rm sym}}
> \oplus\bigwedge\nolimits^2H,
> \qquad
> \ker P_N^{\rm vis}
> =V_N^{\perp_{\rm sym}}\oplus\bigwedge\nolimits^2H.
> \tag{5.4}
> \]
>
> **Corollary D (exact factorization, kernel, and identifiable
> quotient).** *For every \(N\ge2\), let*
> \[
> B_N:=D\mathscr S_N|_{V_N}:V_N\longrightarrow\mathcal K_N.
> \]
> *Then \(B_N\) is injective and*
> \[
> \boxed{D\mathscr S_N=B_NP_N^{\rm vis}},
> \tag{5.5}
> \]
> \[
> \boxed{
> \ker D\mathscr S_N
> =V_N^{\perp_{\rm sym}}\oplus\bigwedge\nolimits^2H
> =\left(\operatorname{Sym}^2P_{N-1}\right)^{\perp_{\rm sym}}
> \oplus\bigwedge\nolimits^2H.}
> \tag{5.6}
> \]
> *If \(q_N:\mathcal X\to\mathcal X/\ker D\mathscr S_N\) is the quotient
> map, then*
> \[
> J_N:\mathcal X/\ker D\mathscr S_N\longrightarrow V_N,
> \qquad
> J_N([f])=P_N^{\rm vis}f,
> \tag{5.7}
> \]
> *is a canonical isometric isomorphism for the Hilbert quotient norm, and
> the differential has the unique induced factorization*
> \[
> \mathcal X\xrightarrow{\ q_N\ }
> \mathcal X/\ker D\mathscr S_N
> \xrightarrow{\ J_N\ }V_N
> \xrightarrow{\ B_N\ }\mathcal K_N,
> \qquad
> D\mathscr S_N=B_NJ_Nq_N.
> \tag{5.8}
> \]
> *In particular,*
> \[
> \boxed{
> \mathcal X/\ker D\mathscr S_N
> \simeq V_N=\operatorname{Sym}^2P_{N-1},
> \qquad
> \dim\bigl(\mathcal X/\ker D\mathscr S_N\bigr)=\binom N2.}
> \tag{5.9}
> \]
>
> *Proof.* The orthogonal decomposition
> \(\mathcal X=(\ker D\mathscr S_N)^\perp\oplus\ker D\mathscr S_N\)
> gives \(D\mathscr S_Nf=D\mathscr S_NP_N^{\rm vis}f\), which is (5.5).
> The restriction \(B_N\) is injective because its domain is
> \((\ker D\mathscr S_N)^\perp\). Equations (5.2) and (5.4) then give
> (5.6). Finally, (5.6) makes (5.7) well defined and bijective, while
> \[
> \|[f]\|_{\mathcal X/\ker D\mathscr S_N}
> =\inf_{k\in\ker D\mathscr S_N}\|f+k\|_{\mathcal X}
> =\|P_N^{\rm vis}f\|_{\mathcal X};
> \]
> hence \(J_N\) is isometric and (5.8) follows. \(\square\)
>
> In particular, for two interaction tangents \(f,g\in\mathcal X\),
> \[
> D\mathscr S_Nf=D\mathscr S_Ng
> \quad\Longleftrightarrow\quad
> [f]=[g]\text{ in }\mathcal X/\ker D\mathscr S_N
> \quad\Longleftrightarrow\quad
> P_N^{\rm vis}f=P_N^{\rm vis}g.
> \tag{5.10}
> \]
> This is the precise sense in which the finite law identifies the quotient:
> it is a statement about its first differential at the reference model,
> not nonlinear identifiability of geometries at finite distance.
>
> Appendix D collects the kernel, quotient, strict-nesting and density
> arguments used here.
>
> The projection \(P_N^{\rm vis}\) specifies **which** tangent directions
> survive; it does not specify how strongly the finite law encodes different
> surviving directions. That second datum is
> \[
> F_N:=B_N^*B_N:V_N\longrightarrow V_N,
> \qquad
> D\mathscr S_N^*D\mathscr S_N
> =P_N^{\rm vis}F_NP_N^{\rm vis}.
> \tag{5.11}
> \]
> Since \(B_N\) is injective and \(V_N\) is finite dimensional, \(F_N\) is
> positive definite on \(V_N\); it need not be the identity and must not be
> conflated with the support projection. Its spectrum and anisotropy belong
> to §6.

### §6. Fisher resolution inside the visible sector

**Estado: prosa de trabajo. Anclas:** §5 para \(P_N^{\rm vis}\), \(B_N\) y
\(F_N=B_N^*B_N\); `wp6_d2_geometric_tangent_classification.md`, §§13–15,
para los cálculos exactos \(N=2,3,4\); y
`docs/hoja_de_ruta_septiembre_2026.md`, §§5.3–5.4, para el teorema
Hilbert–Schmidt. Esta sección usa el aparato de §§3–5 y no redefine el
espacio visible, el diferencial ni su factorización.

> For \(f\in\mathcal X=H\widehat\otimes H\), the Fisher information in the
> finite unlabeled-poset law is
> \[
> I_N^{[P]}(f)
> :=G_{[P]}^{(N)}(f,f)
> =\|D\mathscr S_Nf\|_{L^2(\mu_{N,0})}^2
> =\big\langle P_N^{\rm vis}f,
> F_NP_N^{\rm vis}f\big\rangle.
> \tag{6.1}
> \]
> The continuous reference experiment consists of \(N\) independent copula
> observations, whose score is \(2\sum_{k=1}^Nf(U_k,V_k)\). Its Fisher form
> is therefore \(4N\langle f,g\rangle\). We use it only as an explicit
> normalization and set
> \[
> \widehat F_N
> :=\frac1{4N}P_N^{\rm vis}F_NP_N^{\rm vis}
> =\frac1{4N}D\mathscr S_N^*D\mathscr S_N
> \quad\text{on }\mathcal X.
> \tag{6.2}
> \]
> By data processing and Corollary D,
> \[
> 0\le\widehat F_N\le I_{\mathcal X},
> \qquad
> \operatorname{supp}\widehat F_N=V_N,
> \qquad
> \ker\widehat F_N=\ker D\mathscr S_N.
> \tag{6.3}
> \]
> Thus \(P_N^{\rm vis}\) fixes the support, whereas the nonzero eigenvalues
> of \(\widehat F_N\) quantify the resolution inside that support. In
> general
> \[
> \widehat F_N\ne P_N^{\rm vis}
> \qquad\text{and, equivalently,}\qquad
> F_N\ne4N I_{V_N}.
> \tag{6.4}
> \]
>
> **Exact low-cardinality spectra.** For compact rational formulas put
> \[
> x(t):=t-\frac12,qquad
> q(t):=\left(t-\frac12\right)^2-\frac1{12},qquad
> r(t):=\left(t-\frac12\right)^3
>       -\frac3{20}\left(t-\frac12\right).
> \tag{6.5}
> \]
> These are mutually orthogonal and span \(P_1,P_2,P_3\) successively.
> For \(N=2\), with \(e_{11}=x\otimes x\),
> \[
> G_{[P]}^{(2)}(f,g)
> =256\langle f,e_{11}\rangle\langle g,e_{11}\rangle,
> \qquad
> \operatorname{spec}_+(\widehat F_2)=\left\{\frac29\right\}.
> \tag{6.6}
> \]
> For \(N=3\), in the orthogonal basis
> \[
> e_{11}=x\otimes x,qquad
> e_{12}=x\otimes q+q\otimes x,qquad
> e_{22}=q\otimes q,
> \]
> the poset and continuous-reference forms are respectively
> \[
> [G_{[P]}^{(3)}]
> =\operatorname{diag}\left(\frac1{32},\frac1{1200},
> \frac1{180000}\right),
> \qquad
> [G_{\rm full}^{(3)}]
> =\operatorname{diag}\left(\frac1{12},\frac1{90},
> \frac1{2700}\right).
> \tag{6.7}
> \]
> Hence
> \[
> \boxed{
> \operatorname{spec}_+(\widehat F_3)
> =\left\{\frac38,\frac3{40},\frac3{200}\right\},}
> \tag{6.8}
> \]
> with eigenvectors \(e_{11},e_{12},e_{22}\), in that order. The visible
> space is already anisotropic: support membership alone does not determine
> retained Fisher strength.
>
> At \(N=4\), use
> \[
> \begin{aligned}
> e_{11}&:=x\otimes x,&
> e_{12}&:=x\otimes q+q\otimes x,&
> e_{13}&:=x\otimes r+r\otimes x,\\
> e_{22}&:=q\otimes q,&
> e_{23}&:=q\otimes r+r\otimes q,&
> e_{33}&:=r\otimes r.
> \end{aligned}
> \tag{6.9}
> \]
> Three generalized eigenvectors remain pure:
> \[
> \widehat F_4e_{11}=\frac{12}{25}e_{11},
> \qquad
> \widehat F_4e_{12}=\frac4{25}e_{12},
> \qquad
> \widehat F_4e_{23}=\frac4{525}e_{23}.
> \tag{6.10}
> \]
> The remaining invariant block is
> \(\operatorname{span}\{e_{13},e_{22},e_{33}\}\). In that ordered basis,
> the restrictions of the two bilinear forms are
> \[
> [G_{[P]}^{(4)}]_{\rm mix}
> =\begin{pmatrix}
> 1/55125&1/354375&1/38587500\\
> 1/354375&11/455625&-1/49612500\\
> 1/38587500&-1/49612500&11/5402250000
> \end{pmatrix},
> \]
> \[
> [G_{\rm full}^{(4)}]_{\rm mix}
> =\operatorname{diag}\left(\frac1{1050},\frac1{2025},
> \frac1{490000}\right).
> \tag{6.11}
> \]
> Its three generalized eigenvalues are the real positive roots of
> \[
> 144703125\lambda^3-9975000\lambda^2+142000\lambda-128=0,
> \tag{6.12}
> \]
> namely, for orientation only,
> \[
> 0.0494521212879\ldots,qquad
> 0.0185160720400\ldots,qquad
> 0.000966047034941\ldots.
> \]
> Therefore the exact spectrum is specified by (6.10) and (6.12), and its
> decreasing numerical order is
> \[
> \frac{12}{25}>\frac4{25}>0.0494521212879\ldots>
> 0.0185160720400\ldots>\frac4{525}>
> 0.000966047034941\ldots>0.
> \tag{6.13}
> \]
> The off-diagonal entries in (6.11) are the first explicit modal mixing:
> \(e_{13},e_{22},e_{33}\) are visible but are not individually Fisher
> eigenvectors.
>
> **Theorem F (Fisher resolution and asymptotic retention).** Let
> \(S_N^\Pi(f)\) be the score before the quotient, when the full rank
> permutation \(\Pi_N\) is observed, and put
> \[
> I_N^\Pi(f):=\mathbb E_0[S_N^\Pi(f)^2],
> \qquad
> \Delta_N(f):=I_N^\Pi(f)-I_N^{[P]}(f).
> \tag{6.14}
> \]
> Conditional expectation of scores along
> \(\Pi_N\mapsto[P_{\Pi_N}]\) gives
> \[
> \Delta_N(f)
> =\mathbb E_0\!\left[
> \operatorname{Var}_0\!\left(S_N^\Pi(f)\mid[P_{\Pi_N}]\right)
> \right]\ge0.
> \tag{6.15}
> \]
> For every \(f\in\mathcal X\),
> \[
> \frac{I_N^\Pi(f)}N\longrightarrow4\|f\|_{\mathcal X}^2.
> \tag{6.16}
> \]
> If in addition \(f\in H\widehat\otimes_{\rm sym}H\), then
> \[
> \frac{\Delta_N(f)}N\longrightarrow0,
> \qquad
> \frac{I_N^{[P]}(f)}N\longrightarrow4\|f\|_{\mathcal X}^2.
> \tag{6.17}
> \]
> For every nonzero symmetric \(f\), (6.16) gives a finite, generally
> nonuniform threshold \(N_0(f)\) such that \(I_N^\Pi(f)>0\) for all
> \(N\ge N_0(f)\). On that range define the two stages and their product by
> the following notation; \(\kappa_N\) is used for the second stage because
> \(q_N\) already denotes the quotient map in Corollary D:
> \[
> \rho_N(f):=\frac{I_N^\Pi(f)}{4N\|f\|^2},
> \qquad
> \kappa_N(f):=\frac{I_N^{[P]}(f)}{I_N^\Pi(f)},
> \qquad
> \eta_N^{\rm tot}(f):=\rho_N(f)\kappa_N(f)
> =\frac{I_N^{[P]}(f)}{4N\|f\|^2}.
> \tag{6.18}
> \]
> Then
> \[
> \boxed{
> \rho_N(f)\longrightarrow1,
> \qquad
> \kappa_N(f)\longrightarrow1,
> \qquad
> \eta_N^{\rm tot}(f)\longrightarrow1.}
> \tag{6.19}
> \]
> The first limit concerns continuous observations versus ranks; the second
> concerns ranks versus the unlabeled poset. They are distinct claims and
> neither is inferred from the strict inclusions \(V_N\subsetneq V_{N+1}\).
>
> Equivalently, on the full interaction Hilbert space,
> \[
> \boxed{
> \widehat F_N\xrightarrow{\rm SOT}\Pi_{\rm sym}.}
> \tag{6.20}
> \]
> More generally, if \(0\ne f=f_s+f_a\) is its orthogonal
> symmetric–antisymmetric decomposition, then
> \[
> \frac{I_N^{[P]}(f)}{4N\|f\|^2}
> \longrightarrow
> \frac{\|f_s\|^2}{\|f_s\|^2+\|f_a\|^2}.
> \tag{6.21}
> \]
> In particular, the antisymmetric sector contributes zero to the numerator
> at every \(N\), not merely asymptotically.
>
> *Proof.* Define
> \[
> H_{ij}^{(N)}(f)
> :=\iint f(s,t)d_i^{(N)}(s)d_j^{(N)}(t)\,ds\,dt.
> \tag{6.22}
> \]
> Its row and column sums vanish for \(f\in\mathcal X\), and the
> permutation score is
> \(S_N^\Pi(f)=2\sum_iH_{i,\Pi_N(i)}^{(N)}(f)\). Direct averaging over a
> uniform permutation gives the exact Gram identity
> \[
> I_N^\Pi(f)=\frac4{N-1}\|H^{(N)}(f)\|_F^2.
> \tag{6.23}
> \]
> The normalized order-statistic operator has the shifted-Legendre
> eigenvalues
> \[
> \lambda_{N-1,m}
> =\prod_{r=1}^m\frac{N-r}{N+r}\in[0,1],
> \qquad
> \lambda_{N-1,m}\longrightarrow1
> \quad(m\text{ fixed}).
> \tag{6.24}
> \]
> Expanding \(f\) in the tensor Legendre basis and applying dominated
> convergence to (6.23) proves (6.16). For symmetric finite-rank tensors,
> the fiber theorem gives \(\Delta_N(f)/N\to0\). The uniform bound
> \[
> 0\le\frac{\Delta_N(f)}N\le8\|f\|_{\mathcal X}^2
> \tag{6.25}
> \]
> extends this limit to the full symmetric Hilbert–Schmidt closure by a
> fixed-rank approximation followed by \(N\to\infty\), proving (6.17).
> Equations (6.18)–(6.19) follow by division only after the denominator is
> positive. Inversion symmetry annihilates the antisymmetric conditional
> score on every poset fiber, giving (6.21). Finally, (6.17), (6.21),
> polarization and \(0\le\widehat F_N\le I\) imply (6.20). \(\square\)
>
> The convergence in (6.20) is not convergence in operator norm. Indeed,
> for the unit vector
> \(h_N:=p_N\otimes p_N/\|p_N\|_{L^2}^2\), Theorem C gives
> \(h_N\perp V_N\), so
> \[
> \widehat F_Nh_N=0,
> \qquad
> \Pi_{\rm sym}h_N=h_N,
> \qquad
> \|\widehat F_N-\Pi_{\rm sym}\|\ge1
> \quad\text{for every }N.
> \tag{6.26}
> \]
> Nor does (6.20) make \(\widehat F_N\) a finite-\(N\) projection: already
> (6.6) gives its nonzero eigenvalue \(2/9\). The generic rate in
> (6.17)–(6.21) is only \(o_f(1)\), with no rate or threshold uniform over
> the Hilbert–Schmidt unit sphere. The available
> \(1-\kappa_N(f)=O(N^{-1/2})\) rate applies only to the bounded continuous
> finite-rank subclass.
>
> These statements concern the Hilbert completion of S1 interaction
> tangents. They transfer directly to the admissible geometric paths already
> constructed in that class, but they do not assert geometric realizability
> of an arbitrary Hilbert–Schmidt tensor. The finite spectra above compare
> the unlabeled-poset law with \(N\) continuous copula observations; they are
> not fractions of the full geometry, do not imply reconstruction, and do
> not establish monotonicity of individual Fisher eigenvalues with \(N\).
>
> Appendix E gives the estimates behind the asymptotic retention statement,
> and Appendix F records the exact matrices and generalized spectra for
> \(N=2,3,4\).

### §7. An antisymmetric orbit visible at second order

**Estado: prosa de trabajo. Anclas:**
`docs/hoja_de_ruta_septiembre_2026.md`, §§5.5–5.6, para la senda admisible,
la isotropía y el cálculo exacto en \(N=2\); §5.4bis del mismo documento para
el kernel de borrado uniforme; y
`wp6_s1_three_frozen_targets_priority_audit.md`, §5, para el ensamblaje
all-\(N\). Esta sección trata una única órbita explícita. No introduce un
segundo diferencial general ni un operador \(Q_N\).

> Let \(\ell_1,\ell_2\in H\) be the first two orthonormal shifted-Legendre
> modes,
> \[
> \ell_1(t)=\sqrt3(2t-1),
> \qquad
> \ell_2(t)=\sqrt5(6t^2-6t+1),
> \]
> and define the polynomial generator
> \[
> \boxed{
> \psi(u,v):=\ell_1(u)\ell_2(v)-\ell_2(u)\ell_1(v).}
> \tag{7.1}
> \]
> It is antisymmetric under coordinate exchange, has zero marginals, and
> satisfies
> \[
> \mathcal P\psi=\psi\ne0,
> \qquad
> h_\psi=2\psi\in\bigwedge\nolimits^2H,
> \qquad
> \|\psi\|_{L^2(D)}^2=2,
> \quad \|h_\psi\|_{L^2(D)}^2=8.
> \tag{7.2}
> \]
> In particular, \(\psi\notin\ker\mathcal P\): its first-order
> invisibility is not the marginal gauge of §2. Since \(\psi\) is bounded,
> the normalized exponential family
> \[
> \gamma_\psi:\varepsilon\longmapsto
> g_\varepsilon
> =\frac{e^{2\varepsilon\psi}}{Z(\varepsilon)}g_0,
> \qquad
> Z(\varepsilon)=\int_De^{2\varepsilon\psi}\,d\mu_0,
> \tag{7.3}
> \]
> is an admissible S1 path for every real \(\varepsilon\).
>
> Let \(\iota:D\to D\) exchange the two null coordinates,
> \(\iota(u,v)=(v,u)\). It preserves the product order, the reference
> measure and the flat metric, while \(\psi\circ\iota=-\psi\). A change of
> variables also gives \(Z(-\varepsilon)=Z(\varepsilon)\), and therefore
> \[
> \boxed{\iota^*g_\varepsilon=g_{-\varepsilon}}
> \qquad(\varepsilon\in\mathbb R).
> \tag{7.4}
> \]
> The two signs are thus identified by a discrete isometry of the S1 family.
> Because the finite observable records only the abstract causal
> order,
> \[
> \boxed{
> \mu_{N,\varepsilon}^{[P]}(C)
> =\mu_{N,-\varepsilon}^{[P]}(C)}
> \qquad(N\ge2,\ C\in\mathcal C_N).
> \tag{7.5}
> \]
>
> **Theorem G (exact parity of the antisymmetric orbit).** *For the path
> \(\gamma_\psi\) in (7.3), every finite unlabeled-poset law is a real-
> analytic even function of \(\varepsilon\). Consequently all its odd jets
> at the reference point vanish, in particular*
> \[
> \left.\frac d{d\varepsilon}
> \mu_{N,\varepsilon}^{[P]}\right|_{\varepsilon=0}=0
> \qquad\forall N\ge2.
> \tag{7.6}
> \]
>
> *Proof.* If \(p_\pi(\varepsilon)\) is the probability of the rank
> permutation \(\pi\in S_N\), then
> \[
> p_\pi(\varepsilon)
> =\frac{\left\langle e^{2\varepsilon T_\pi}\right\rangle_0}
>        {N!\,Z(\varepsilon)^N},
> \qquad
> T_\pi:=\sum_{i=1}^N
> \psi(U_{(i)},V_{(\pi(i))}),
> \tag{7.7}
> \]
> where the bracket is expectation over two independent vectors of uniform
> order statistics. Boundedness of \(\psi\) permits differentiation under
> the integral to every order, so \(p_\pi\) is real analytic. Coordinate
> exchange gives
> \(p_\pi(-\varepsilon)=p_{\pi^{-1}}(\varepsilon)\). Each fiber
> \(\Gamma_C\) is closed under inversion (§3); summing (7.7) over the fiber
> proves
> (7.5), hence the assertion. \(\square\)
>
> To measure the first nonvanishing response of the complete finite law,
> define the path invariant
> \[
> r_N(\gamma_\psi)
> :=\inf\left\{k\ge1:
> \left.\frac{d^k}{d\varepsilon^k}
> \mu_{N,\varepsilon}^{[P]}\right|_{\varepsilon=0}
> \ne0\ \text{as a vector on }\mathcal C_N\right\},
> \tag{7.8}
> \]
> with \(r_N(\gamma_\psi)=\infty\) if every jet vanishes. The notation
> refers to the full path, not merely to its zero first-order tangent.
>
> The same finite-likelihood formula gives
> \[
> p_\pi'(0)=\frac2{N!}\langle T_\pi\rangle_0,
> \qquad
> p_\pi''(0)=\frac4{N!}
> \left(\langle T_\pi^2\rangle_0-N\|\psi\|_{L^2(D)}^2\right).
> \tag{7.9}
> \]
> At \(N=2\), exact polynomial integration over the two order simplices
> yields
> \[
> \boxed{
> \left.\frac{d^2}{d\varepsilon^2}
> \mu_{2,\varepsilon}^{[P]}(\mathrm{antichain})\right|_{0}=\frac85,
> \qquad
> \left.\frac{d^2}{d\varepsilon^2}
> \mu_{2,\varepsilon}^{[P]}(\mathrm{chain})\right|_{0}=-\frac85.}
> \tag{7.10}
> \]
> Equivalently,
> \[
> \mu_{2,\varepsilon}^{[P]}(\mathrm{antichain})
> =\frac12+\frac45\varepsilon^2+O(\varepsilon^4),
> \qquad
> \mu_{2,\varepsilon}^{[P]}(\mathrm{chain})
> =\frac12-\frac45\varepsilon^2+O(\varepsilon^4).
> \tag{7.11}
> \]
> Thus the magnitude of the deformation is locally visible already at the
> smallest cardinality supporting two distinct causal orders, while its sign
> remains identified by (7.4).
>
> For \(m\ge3\), define the parameter-independent deletion kernel
> \[
> K_{m,m-1}(C,D)
> :=\frac1m\#\{v\in C:[C\setminus\{v\}]=D\},
> \tag{7.12}
> \]
> and let
> \[
> K_{N\to2}:=K_{3,2}\circ K_{4,3}\circ\cdots\circ K_{N,N-1},
> \qquad K_{2\to2}:=I.
> \tag{7.13}
> \]
> Uniformly deleting points from an iid sample leaves an iid subsample, so
> for every \(\varepsilon\),
> \[
> \mu_{2,\varepsilon}^{[P]}
> =K_{N\to2}\mu_{N,\varepsilon}^{[P]}.
> \tag{7.14}
> \]
> Since the kernel does not depend on \(\varepsilon\), differentiation gives
> \[
> \left(\mu_2^{[P]}\right)^{(k)}(0)
> =K_{N\to2}\left(\mu_N^{[P]}\right)^{(k)}(0)
> \qquad(k\ge1).
> \tag{7.15}
> \]
>
> **Corollary H (first nonzero jet at every cardinality).** *For the explicit
> path (7.3),*
> \[
> \boxed{r_N(\gamma_\psi)=2\qquad\forall N\ge2.}
> \tag{7.16}
> \]
>
> *Proof.* Theorem G gives \(r_N(\gamma_\psi)\ge2\). If
> \((\mu_N^{[P]})''(0)\) were zero, (7.15) with \(k=2\) would force
> \((\mu_2^{[P]})''(0)=0\), contradicting (7.10). Hence the second jet is
> nonzero for every \(N\ge2\), proving (7.16). \(\square\)
>
> Corollary H is an existence statement for one admissible orbit. It neither
> classifies the second differential on \(\bigwedge^2H\) nor asserts that
> every antisymmetric direction has order two. No general operator \(Q_N\),
> quadratic null cone, estimator, rate, or nonlinear reconstruction is
> introduced. The first-order zero is explained by the exact isometric fold
> \(\varepsilon\leftrightarrow-\varepsilon\); it must not be described as
> physical information loss.
>
> Appendix G gives the finite-likelihood derivatives, the exact \(N=2\)
> integration, and the deletion-kernel argument.

### §8. Relation to prior work

**Estado: prosa final citable, cerrada tras la auditoría de prioridad.
Ancla:** `wp6_s1_three_frozen_targets_priority_audit.md` §§2–6 (tabla
ejecutiva de §2, adjudicación de P1 en §3, de P2 en §4, de P3 en §5, claim
ceiling de §6). El texto citable (bloque `>`) no contiene nombres de
archivo del repo, commits ni terminología de auditoría/gate — esa
trazabilidad vive aquí, en la nota de estado.

> Bombelli (2000) already sets up the framework studied here: the
> complete law of an unlabeled causal poset at fixed cardinality, and a
> statistical comparison between two such laws obtained from different
> geometries. Janson (2011) supplies the general limiting framework of
> poset kernels and consistent finite laws in which this construction
> sits. Surya (2026) tells a related story: increasing resolution can
> lift degeneracies of a causal compression, though through a different
> observable — expected interval abundances rather than the full
> unlabeled-poset law used here. None of the three computes the
> differential of the finite-$N$ law at a reference geometry, its rank, or
> its kernel. That computation is what §§2–7 do.
>
> The many-to-one correspondence between permutations and two-dimensional
> posets that this differential must be summed over is itself classical.
> Bayoumi, El-Zahar and Khamis (1994) work explicitly with this
> correspondence, its realizers, the closure of a fiber under
> $\sigma\mapsto\sigma^{-1}$, and the near-uniqueness of realizers for
> prime posets. Recovering that correspondence is not the contribution
> here; we instead sum a differential score representative over the
> entire fiber,
> \[
> A_C=\sum_{\sigma\in\Gamma_C}P_\sigma,
> \]
> and ask what these class-sum representatives span once we pass to
> unlabeled poset classes.
>
> Before that quotient is taken, the relevant differential structure is
> close to two existing constructions. Even-Zohar (2020) decomposes the
> space of pattern densities via the representation theory of $S_N$ and
> isolates the standard-representation block of dimension $(N-1)^2$,
> realized through permutation matrices compressed to $\mathbf1^\perp$;
> his asymptotic regime concerns fluctuations of a random permutation's
> pattern profile as the host size grows, a scaling question distinct
> from the local $\varepsilon$-derivative used here. Kurečka (2022)
> differentiates a pattern density directly around the uniform permuton,
> expresses the resulting gradient in a Bernstein-type basis on
> $E_N=\mathbf1^\perp$ through compressed permutation matrices
> $A_\pi|_{E_N}$, and characterizes vanishing gradient combinations via
> covering-matrix sums $\sum_\pi t_\pi A_\pi$. Differentiating pattern
> densities, the appearance of a Bernstein-type basis at this level, the
> compression of permutation matrices to $E_N$, and the covering-matrix
> technique all belong to this line of work. What neither construction
> does is restrict those class sums to $E_N$ and show that they span the
> full symmetric target there:
> \[
> \operatorname{span}\{A_C|_{E_N}:C\in\mathcal C_N\}
> =\operatorname{Sym}(E_N).
> \]
> Chan, Král', Noel, Pehova, Sharifzadeh and Volec (2019/2020) and Garbe,
> Král', Malekshahian and Penaguiao (2025) are adjacent
> permuton-forcing and feasible-region results, on quasirandomness-forcing
> pattern sums and on the dimension of the feasible region of pattern
> densities respectively, and they do not give this fiber-indexed span
> statement either.
>
> The abstract target module and its dimension already appear in the
> representation-theory literature on rankings. Diaconis (1989) decomposes
> functions on rankings via $S_N$ representation theory and gives, for
> unordered-pair effects,
> $M^{(N-2,2)}\simeq S^{(N)}\oplus S^{(N-1,1)}\oplus S^{(N-2,2)}$, already
> the module, and the dimension $\binom N2$, behind a Johnson-scheme
> reformulation of $\operatorname{Sym}(E_N)$. The 1988 monograph makes this
> concrete with a worked instance on unordered pairs of experimental
> varieties, the Diallel Cross Design, and develops the associated model
> family. Neither work introduces unlabeled two-dimensional-poset fibers,
> their class sums, or a rank theorem for those specific sums. So
> $\operatorname{Sym}(E_N)$ and its dimension are not a new representation
> here; the narrower claim we are actually making is that sums over
> isomorphism fibers of unlabeled two-dimensional posets generate exactly
> that module.
>
> Fisher information after passing from continuous observations to ranks
> is not a new idea either. Hallin, Mellouk and Rifi (2001) already have
> Bernstein-type polynomials showing up in Hájek projections of rank
> statistics, though asymptotically rather than at our exact finite $N$.
> Hoff (2007) establishes the rank likelihood as a marginal-free
> semiparametric likelihood, and Hoff, Niu and Wellner (2014) together
> with Sei and Matsumoto (2020) develop the induced information and
> divergence of Gaussian-copula and rank models, including finite-sample
> identifiability loss. None of these reaches the further quotient from a
> full rank permutation to an unlabeled poset, $\Pi_N\to[P_{\Pi_N}]$, or
> classifies its S1 support the way §§3–6 do.
>
> The operator identity connecting these two levels is standard once its
> kernel is known. Pollard (2011/2012) shows, in the
> differentiability-in-quadratic-mean framework, that the score of a
> statistic is the conditional expectation of the original score; on a
> Hilbert space, any bounded linear operator factors tautologically
> through the orthogonal projection onto the complement of its kernel,
> with an injective restriction to that complement. So the factorization
> $D\mathscr S_N=B_NP_N^{\rm vis}$, used from §5 on, is not an independent
> operator construction. Theorem C is what pins the complement down
> exactly, $(\ker D\mathscr S_N)^\perp=\operatorname{Sym}^2P_{N-1}$, and
> the injectivity of $B_N$ follows immediately from that.
>
> §7 sits against several established mechanisms rather than introducing
> them. Rotnitzky, Cox, Bottai and Robins (2000) study likelihood models
> with singular information, relating the order of the first nonvanishing
> derivative to inferential behavior and noting the sign ambiguity that
> arises when that order is even; a law invisible at first order and
> visible only at a higher one, and the role parity plays in that, is not
> a general contribution of this paper. Within the permuton literature,
> forcing results go beyond the gradient: Chan (2021) and Crudele, Dukes
> and Noel (2023) compute Hessians of pattern-density combinations around
> the uniform permuton once the gradient vanishes, precedent for using a
> second differential of a permutation-pattern law to detect perturbations
> hidden at first order. That a size-two law is the uniform-deletion
> push-forward of a size-$N$ law is standard projective consistency of iid
> sampling, and differentiating an exact identity with a
> parameter-independent kernel is a formal consequence of it. None of
> these three pieces is new by itself. What is ours is the combination:
> the antisymmetric S1 orbit of §7, the exact parity it forces,
> $\mu_{N,\varepsilon}^{[P]}=\mu_{N,-\varepsilon}^{[P]}$, the nonvanishing
> second derivative $\mu_2''(0)\ne0$ computed for that orbit, and its
> propagation through the uniform-deletion kernel to $r_N(\gamma_\psi)=2$
> for every $N\ge2$ (Theorem G, Corollary H).
>
> Put together, the precedents above cover the permutation-level
> differential, the abstract representation-theoretic target, and the
> general mechanics of statistic-induced scores and singular first-order
> information. This paper determines what is left over: the exact effect
> of the additional quotient from labeled rank permutations to unlabeled
> finite causal-order laws, at every fixed cardinality $N$.

### §9. Discussion: causal compression

**Estado: prosa de trabajo. Ancla interpretativa:**
`wp6_full_class_sum_rank_theorem.md`, §7.1. Esta sección ensambla Theorem C,
Corollaries D–E, Theorem F y Theorem G/Corollary H. No introduce una nueva
definición, hipótesis o afirmación matemática.

> The phrase *causal compression* is a compact name for the exact S1
> factorization
> \[
> D\mathscr S_N=B_NP_N^{\rm vis},
> \qquad
> V_N=\operatorname{Sym}^2P_{N-1}.
> \tag{9.1}
> \]
> Read literally, at the level actually proved here: the first
> differential of an infinite-dimensional interaction tangent is compressed
> to the finite-dimensional component \(P_N^{\rm vis}f\), and that component
> is then encoded injectively as a score of the finite unlabeled-poset law.
> The projection selects what is visible, \(B_N\) performs the
> statistical encoding, and \(F_N=B_N^*B_N\) measures its directional
> strength. These are three different parts of one channel, not three
> names for the same operator.
>
> The word *causal* here is not decorative. In the \(1+1\)-dimensional
> diamond, the order relation is fixed by the joint pattern of the two
> null rankings. Passing from continuous coordinates to ranks throws away
> marginal information; passing from a rank permutation to an unlabeled
> poset throws away the choice of linear realizer. What survives both
> steps at first order is exactly the symmetric polynomial interaction
> sector in (9.1). In this restricted, model-specific sense the causal
> past and future compress the present: the finite order does not
> preserve a perturbation point by point, it records a finite collection
> of symmetric interaction modes through the relations among the sampled
> events.
>
> **Resolution grows, but not uniformly.** Theorem C and Corollary E turn this
> interpretation into an exact filtration,
> \[
> V_N\subsetneq V_{N+1},
> \qquad
> \dim V_N=\binom N2,
> \qquad
> \overline{\bigcup_{N\ge2}V_N}
> =H\widehat\otimes_{\rm sym}H.
> \tag{9.2}
> \]
> Each additional cardinality opens genuinely new polynomial directions, so
> no fixed nonzero symmetric tangent remains invisible at every sufficiently
> large resolution. This statement is nevertheless pointwise in the tangent.
> The moving direction \(p_N\otimes p_N\) lies beyond the resolution of the
> size-\(N\) experiment, and Theorem F correspondingly gives
> \[
> \widehat F_N\xrightarrow{\rm SOT}\Pi_{\rm sym},
> \qquad
> \|\widehat F_N-\Pi_{\rm sym}\|\ge1.
> \tag{9.3}
> \]
> Thus increasing \(N\) resolves every fixed symmetric interaction in the
> limit, but there is no uniform resolution over the Hilbert–Schmidt unit
> sphere and no operator-norm convergence.
>
> **Visibility is not sensitivity.** The exact spectra at \(N=2,3,4\) show
> that two directions can both belong to \(V_N\) and nevertheless be encoded
> with very different Fisher strengths. At \(N=4\), visible polynomial modes
> even mix before the Fisher eigenvectors emerge. Hence the binary question
> answered by Theorem C — whether a direction survives the differential — is
> logically prior to, but does not answer, the quantitative question treated
> by Theorem F. In particular, neither \(F_N\) nor its normalized ambient
> extension is a finite-\(N\) support projection.
>
> **A first-order kernel is not a nonlinear erasure theorem.** The full
> antisymmetric sector belongs to \(\ker D\mathscr S_N\) at every
> cardinality, but §7 shows why that fact must not be called physical
> information loss. For the explicit admissible odd path \(\gamma_\psi\),
> coordinate exchange is an isometry satisfying
> \(\iota^*g_\varepsilon=g_{-\varepsilon}\); the finite law therefore folds
> the two signs together. Its linear term vanishes by symmetry, while
> \[
> r_N(\gamma_\psi)=2\qquad\forall N\ge2.
> \tag{9.4}
> \]
> The magnitude of this deformation is detected at second order at every
> nontrivial finite resolution. This single orbit proves that membership in
> the first-order kernel does not imply invariance of the full nonlinear law;
> it does not classify higher-order behavior throughout
> \(\bigwedge^2H\).
>
> §§3–7 together describe the local anatomy of one channel. Score
> representatives give its finite linear functionals; the all-\(N\) span
> theorem pins down their exact support; the quotient marks off the
> equivalence class the differential identifies; the Fisher operator then
> resolves directions within that support, and the antisymmetric orbit of
> §7 shows that a symmetry-forced first-order zero can still carry a
> nonzero second jet. The result is a statement about tangent visibility
> and statistical resolution for the S1 finite-law experiment, not a
> reconstruction theorem.
>
> In particular, *the causal past and future compress the present* must not be
> read as saying that causal data universally determine a present geometry.
> The results do not reconstruct continuous coordinates or a Lorentzian
> metric from one causet, establish global injectivity, realize every
> Hilbert–Schmidt tangent geometrically, or extend beyond S1 and
> \(1+1\) dimensions. The phrase names the exact model-specific compression
> in (9.1), and nothing broader.

### §10. Limitations and open problems

**Estado: prosa de trabajo.** Registra el alcance de los resultados ya
demostrados y distingue limitaciones matemáticas, inferenciales y
bibliográficas. No abre extensiones nuevas.

> **Model scope.** Every theorem in this paper concerns the explicit S1
> interaction model in a (1+1)-dimensional causal diamond, expanded at the
> independent reference point. The arguments do not establish an analogue
> in (2+1) or (3+1) dimensions, for a general Lorentzian spacetime, or
> for an arbitrary causal-set sampling model. Such extensions would require
> new geometric and combinatorial input and are outside the present paper.
>
> **Ambient tangents versus geometric realizability.** The Hilbert space
> \(\mathcal X=H\widehat\otimes H\) is the analytic domain of the score
> operators. The exact identities for \(V_N\), \(\ker D\mathscr S_N\), and
> \(F_N\) therefore classify the finite channel on that ambient tangent
> space. They do not prove that every Hilbert–Schmidt direction is generated
> by an admissible curve of Lorentzian geometries. Geometric realizability of
> an arbitrary ambient tangent remains open and is not needed for the
> finite-channel classification.
>
> **Differential identification versus nonlinear reconstruction.**
> Corollary D identifies exactly the quotient seen by
> \(D\mathscr S_N\); it does not imply injectivity of the full map
> \(\mathscr S_N\) at finite distance, recovery of coordinates or a metric
> from one causet, or reconstruction from the family of finite laws. The
> antisymmetric orbit of §7 makes the distinction concrete: its first jet
> vanishes and its second jet does not. That calculation treats one explicit
> admissible orbit only. A general second-order operator \(Q_N\), the
> associated quadratic null cone, and a classification of the
> antisymmetric sector are not developed here.
>
> **Pointwise asymptotic retention.** The convergence
> \(\widehat F_N\to\Pi_{\rm sym}\) is strong-operator convergence. It gives
> asymptotic retention for each fixed symmetric Hilbert–Schmidt tangent, but
> no uniform rate over the unit sphere. Indeed, the moving unresolved
> directions in (6.26) give
> \(\|\widehat F_N-\Pi_{\rm sym}\|\ge1\) for every \(N\), and hence rule out
> operator-norm convergence. The exact Fisher spectra computed here are
> confined to
> \(N=2,3,4\); no all-\(N\) spectral formula, uniform conditioning bound, or
> nonlinear estimator is claimed.
>
> **Priority status.** The statistical comparison of finite causal-order
> laws, and the general expectation that larger samples can sharpen
> resolution, both have clear precedents; §8 reviews them, together with
> substantial partial precedents for the specific ingredients behind our
> results. We have not found an exact counterpart of the S1 all-\(N\)
> class-sum span theorem, or of the antisymmetric-orbit statement, in the
> literature considered there, but that absence is not itself a priority
> claim, and our search was not exhaustive. A broader specialist review
> would be needed before any affirmative claim of novelty.

### §11. Conclusion

**Estado: prosa de trabajo.** Ensambla únicamente C1–C4 y conserva el techo
de §§9–10. No introduce resultados ni problemas nuevos.

> The finite unlabeled causal-order law has, at the independent reference
> point of the \(1+1\)-dimensional S1 model, a local differential
> structure we can now state exactly. The score representatives of §3
> reduce the problem to class sums over the fibers of the
> permutation-to-poset map, and the constructive all-\(N\) argument of §4
> gives
> \[
> \operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}
> =V_N=\operatorname{Sym}^2P_{N-1},
> \qquad
> \dim V_N=\binom N2
> \quad(N\ge2).
> \tag{11.1}
> \]
> These are exactly the first-order interaction modes that survive the
> additional quotient from a rank permutation to an unlabeled causal
> order.
>
> The operator picture makes this precise. For every \(N\),
> \[
> D\mathscr S_N=B_NP_N^{\rm vis},
> \qquad
> \ker D\mathscr S_N
> =V_N^{\perp_{\rm sym}}\oplus\bigwedge\nolimits^2H,
> \qquad
> \mathcal X/\ker D\mathscr S_N\simeq V_N.
> \tag{11.2}
> \]
> The visible spaces are strictly nested, and their union is dense in the
> symmetric interaction Hilbert space: increasing cardinality keeps
> opening new first-order directions, while (11.2) itself states only
> differential identifiability at the reference model.
>
> Visibility is one thing, statistical sensitivity another. The positive
> operator \(F_N=B_N^*B_N\) resolves directions inside \(V_N\), and the
> exact spectra at \(N=2,3,4\) show both strong anisotropy and, at
> \(N=4\), modal mixing. Normalized by the Fisher information of \(N\)
> continuous copula observations, Theorem F gives
> \[
> \widehat F_N\xrightarrow{\rm SOT}\Pi_{\rm sym},
> \qquad
> \|\widehat F_N-\Pi_{\rm sym}\|\ge1
> \quad\text{for every }N.
> \tag{11.3}
> \]
> Every fixed symmetric Hilbert–Schmidt tangent is asymptotically
> retained, but not uniformly over the unit sphere; keeping the two
> stages, continuous observations \(\to\) ranks and ranks
> \(\to\) unlabeled posets, separate is what lets us locate the
> corresponding Fisher losses.
>
> The explicit antisymmetric orbit of §7 completes the picture.
> Coordinate exchange folds \(g_\varepsilon\) onto the isometric geometry
> \(g_{-\varepsilon}\), so the finite laws are even and their first
> derivatives vanish; the exact \(N=2\) second derivative and projective
> consistency under uniform deletion nonetheless give
> \[
> r_N(\gamma_\psi)=2
> \qquad\forall N\ge2.
> \tag{11.4}
> \]
> One admissible orbit, at every resolution, not a classification of the
> antisymmetric sector.
>
> Three layers make up the resulting picture:
> \[
> \boxed{
> \text{tangent visibility}=V_N,
> \qquad
> \text{statistical resolution}=F_N,
> \qquad
> \text{higher-order detectability}=r_N(\gamma_\psi)=2
> \text{ for the explicit witness}.}
> \tag{11.5}
> \]
> This is an exact, local account of what the finite causal-order channel
> retains in S1, not a reconstruction of geometry from a causet, a claim
> of global or nonlinear identifiability, or a result beyond the
> \(1+1\)-dimensional S1 model; §10 states the full limits. The
> statistical framework itself is inherited from prior work — what is
> isolated here is the explicit differential classification and its
> consequences within that fixed scope.

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

### Appendix A. QMD and score representatives

**Estado: prosa de trabajo.** Demuestra los pasos analíticos usados en
§§2–3 para cada \(N\) fijo. No modifica el dominio geométrico ni extiende
los representantes más allá de su continuación lineal hilbertiana.

> Fix an admissible generator \(\psi\in C([0,1]^2)\), put
> \(f=\mathcal P\psi\), and let \(c_\varepsilon\) be the copula density
> obtained from the normalized S1 density by the two marginal probability
> integral transforms of §2. The calculation there gives, uniformly on the
> unit square,
> \[
> c_\varepsilon(u,v)
> =1+2\varepsilon f(u,v)+o(\varepsilon),
> \qquad
> \int_0^1f(u,v)\,du=
> \int_0^1f(u,v)\,dv=0.
> \tag{A.1}
> \]
> Positivity of the exponential S1 density and continuity on the compact
> domain give a common positive lower bound for \(c_\varepsilon\) when
> \(|\varepsilon|\) is small. Taylor expansion of the square root, with the
> uniform remainder in (A.1), therefore yields
> \[
> \int_{[0,1]^2}
> \left(
> \sqrt{c_\varepsilon}-1-\varepsilon f
> \right)^2du\,dv=o(\varepsilon^2).
> \tag{A.2}
> \]
> So the one-observation copula experiment is QMD at zero with score
> \(2f=h_\psi\).
>
> For a fixed \(N\), write
> \(L_{N,\varepsilon}=\prod_{k=1}^Nc_\varepsilon(U_k,V_k)\) for the density
> of the iid copula sample with respect to Lebesgue measure on
> \(([0,1]^2)^N\). Taking the finite product in (A.2) gives
> \[
> \int
> \left(
> \sqrt{L_{N,\varepsilon}}-1
> -\varepsilon\sum_{k=1}^Nf(U_k,V_k)
> \right)^2=o(\varepsilon^2).
> \tag{A.3}
> \]
> Hence the full-sample score is
> \[
> T_{N,\psi}
> =2\sum_{k=1}^Nf(U_k,V_k)
> =\sum_{k=1}^Nh_\psi(U_k,V_k).
> \tag{A.4}
> \]
>
> Let \(\mathcal A_\sigma\) be the set of samples whose relative rank
> permutation is \(\sigma\in S_N\). This event is defined entirely by strict
> coordinate inequalities and is independent of \(\varepsilon\); ties have
> probability zero. Since \(c_\varepsilon\) and its parameter derivative are
> uniformly bounded in a neighborhood of zero, differentiation under the
> integral over \(\mathcal A_\sigma\) is valid. With
> \(p_\varepsilon(\sigma)=\int_{\mathcal A_\sigma}L_{N,\varepsilon}\) and
> \(p_0(\sigma)=1/N!\),
> \[
> \begin{aligned}
> p_\sigma'(0;f)
> &=\mathbb E_0\!\left[
> \mathbf1_{\{\Pi_N=\sigma\}}T_{N,\psi}
> \right],\\
> S_N^\Pi(f)(\sigma)
> &:=\left.\partial_\varepsilon
> \log p_\varepsilon(\sigma)\right|_0
> =\mathbb E_0[T_{N,\psi}\mid\Pi_N=\sigma].
> \end{aligned}
> \tag{A.5}
> \]
> This is the conditional-score identity used in §2; it follows from the
> likelihood and does not assume that the ordered observations remain
> independent after conditioning.
>
> Under the uniform reference law, the two vectors of order statistics are
> independent, and conditional on \(\Pi_N=\sigma\) the point of \(U\)-rank
> \(i\) is paired with the point of \(V\)-rank \(\sigma(i)\). If
> \(d_i^{(N)}\) is the order-statistic density from (3.1), (A.4)–(A.5) give
> \[
> S_N^\Pi(f)(\sigma)
> =2\sum_{i=1}^N
> \left\langle f,
> d_i^{(N)}\otimes d_{\sigma(i)}^{(N)}\right\rangle,
> \tag{A.6}
> \]
> and consequently
> \[
> p_\sigma'(0;f)
> =\frac2{N!}\sum_{i=1}^N
> \left\langle f,
> d_i^{(N)}\otimes d_{\sigma(i)}^{(N)}\right\rangle.
> \tag{A.7}
> \]
> Because both marginals of \(f\) vanish, writing
> \(d_i^{(N)}=1+b_i^{(N)}\) removes the constant and one-coordinate terms:
> \[
> \left\langle f,d_i^{(N)}\otimes d_j^{(N)}\right\rangle
> =\left\langle f,b_i^{(N)}\otimes b_j^{(N)}\right\rangle.
> \tag{A.8}
> \]
> Combining (A.7)–(A.8) proves the representative formula
> \[
> R_\sigma^{(N)}
> =\frac2{N!}\sum_{i=1}^N
> b_i^{(N)}\otimes b_{\sigma(i)}^{(N)},
> \qquad
> p_\sigma'(0;f)=\langle f,R_\sigma^{(N)}\rangle.
> \tag{A.9}
> \]
>
> The last step is to pass from labeled ranks to the observable unlabeled
> poset. For \(C\in\mathcal C_N\), the fiber \(\Gamma_C\) is finite and fixed, so
> direct summation of (A.9) gives
> \[
> \begin{aligned}
> \mu_{N,0}^{[P]}(C)&=\frac{|\Gamma_C|}{N!},\\
> \left.\partial_\varepsilon
> \mu_{N,\varepsilon}^{[P]}(C)\right|_0
> &=\left\langle f,R_C^{(N)}\right\rangle,
> \qquad
> R_C^{(N)}:=\sum_{\sigma\in\Gamma_C}R_\sigma^{(N)}.
> \end{aligned}
> \tag{A.10}
> \]
> Every reference mass in (A.10) is positive. Since \(\mathcal C_N\) is
> finite, coordinatewise differentiability of its probabilities is
> equivalent here to the discrete QMD expansion
> \[
> \sum_{C\in\mathcal C_N}
> \left[
> \sqrt{\mu_{N,\varepsilon}^{[P]}(C)}
> -\sqrt{\mu_{N,0}^{[P]}(C)}
> -\frac{\varepsilon}{2}
> (D\mathscr S_Nf)(C)
> \sqrt{\mu_{N,0}^{[P]}(C)}
> \right]^2
> =o(\varepsilon^2),
> \tag{A.11}
> \]
> with score
> \[
> (D\mathscr S_Nf)(C)
> =\frac{\langle f,R_C^{(N)}\rangle}
> {\mu_{N,0}^{[P]}(C)}.
> \tag{A.12}
> \]
> Also,
> \(\sum_{C\in\mathcal C_N}R_C^{(N)}=0\): after summing (A.9) over
> \(\sigma\), each \(b_j^{(N)}\) occurs \((N-1)!\) times at every fixed
> position and \(\sum_jb_j^{(N)}=0\). So (A.12) has zero mean, as a score
> must; polarization gives
> \[
> G_{[P]}^{(N)}(f,g)
> =\sum_{C\in\mathcal C_N}
> \frac{\langle f,R_C^{(N)}\rangle
> \langle g,R_C^{(N)}\rangle}
> {\mu_{N,0}^{[P]}(C)}.
> \tag{A.13}
> \]
>
> Equations (A.9)–(A.13) were derived for continuous S1 tangents. Since
> every \(R_C^{(N)}\) is a finite sum of polynomial tensors, the right-hand
> sides define bounded linear functionals on
> \(\mathcal X=H\widehat\otimes H\). This is the Hilbert-space
> extension used in §§3–6; it is not a claim that every element of
> \(\mathcal X\) is geometrically realizable.

### Appendix B. Finite reduction to \(\operatorname{Sym}(E_N)\)

**Estado: prosa de trabajo.** Justifica (3.11)–(3.14), incluidos el
isomorfismo de Bernstein, la restricción de las sumas de clase y el factor
exacto \(2/N!\). \(B_N\) sigue reservado para el operador de codificación de
§5.

> Let
> \[
> E_N=\mathbf1^\perp\subset\mathbb R^N,
> \qquad
> P_{N-1}=\operatorname{span}\{p_1,\ldots,p_{N-1}\}
> \subset H.
> \tag{B.1}
> \]
> The functions \(d_i^{(N)}/N\) form the Bernstein basis of the
> polynomials of degree at most \(N-1\). Since
> \(1=N^{-1}\sum_i d_i^{(N)}\), their centered versions satisfy
> \[
> b_i^{(N)}
> =d_i^{(N)}-\frac1N\sum_{j=1}^Nd_j^{(N)},
> \qquad
> \sum_{i=1}^Nb_i^{(N)}=0.
> \tag{B.2}
> \]
> This is their only linear relation. Indeed, every coefficient vector
> \(a\in\mathbb R^N\) decomposes as \(a=\bar a\mathbf1+z\) with
> \(z\in E_N\); the constant part gives the relation in (B.2), whereas
> \[
> \sum_{i=1}^Nz_i b_i^{(N)}
> =\sum_{i=1}^Nz_i d_i^{(N)},
> \tag{B.3}
> \]
> and linear independence of the Bernstein basis makes the right-hand side
> zero only when \(z=0\). Consequently,
> \[
> \Lambda_N:E_N\longrightarrow P_{N-1},
> \qquad
> \Lambda_Nz=\sum_{i=1}^Nz_i b_i^{(N)},
> \tag{B.4}
> \]
> is injective and, since both spaces have dimension \(N-1\), is an
> isomorphism.
>
> We use the Euclidean inner product to identify
> \(\operatorname{Sym}(E_N)\), the self-adjoint endomorphisms of \(E_N\),
> with \(\operatorname{Sym}^2E_N\). For
> \(M\in\operatorname{Sym}(E_N)\), let \(\widetilde M\) be its self-adjoint
> extension to \(\mathbb R^N\) that vanishes on
> \(\operatorname{span}\{\mathbf1\}\). The tensor transport induced by
> (B.4) is
> \[
> \begin{aligned}
> \mathfrak T_N:\operatorname{Sym}(E_N)
> &\longrightarrow\operatorname{Sym}^2P_{N-1},\\
> M&\longmapsto
> \sum_{i,j=1}^N
> \widetilde M_{ij}
> b_i^{(N)}\otimes b_j^{(N)},
> \end{aligned}
> \tag{B.5}
> \]
> Equivalently, \(\mathfrak T_N\) is
> \(\Lambda_N\otimes\Lambda_N\) restricted to the
> symmetric tensor square. It is therefore a linear isomorphism. It need not
> be an isometry; only spans and ranks, not Fisher eigenvalues, are preserved
> by this reduction.
>
> With the convention of (3.12),
> \[
> P_\sigma=\sum_{i=1}^Ne_i e_{\sigma(i)}^\top,
> \qquad
> A_C=\sum_{\sigma\in\Gamma_C}P_\sigma.
> \tag{B.6}
> \]
> Every permutation matrix has unit row and column sums. Hence
> \[
> A_C\mathbf1=|\Gamma_C|\mathbf1,
> \qquad
> \mathbf1^\top A_C=|\Gamma_C|\mathbf1^\top,
> \tag{B.7}
> \]
> so \(E_N\) is invariant under \(A_C\). Also,
> \(P_\sigma^\top=P_{\sigma^{-1}}\), and the fiber \(\Gamma_C\) is closed
> under inversion (§3). So
> \[
> A_C^\top=A_C,
> \qquad
> A_C|_{E_N}\in\operatorname{Sym}(E_N).
> \tag{B.8}
> \]
>
> Because \(\sum_i b_i^{(N)}=0\), projecting onto \(E_N\) on either matrix
> index does not change the transported tensor. Equations (3.13) and (B.5)
> therefore give the exact
> identity
> \[
> R_C^{(N)}
> =\frac2{N!}\,
> \mathfrak T_N\!\left(A_C|_{E_N}\right).
> \tag{B.9}
> \]
> The scalar \(2/N!\) is nonzero for every \(N\). Since
> \(\mathfrak T_N\) is an isomorphism, (B.9) proves
> \[
> \operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}
> =\operatorname{Sym}^2P_{N-1}
> \quad\Longleftrightarrow\quad
> \operatorname{span}\{A_C|_{E_N}:C\in\mathcal C_N\}
> =\operatorname{Sym}(E_N).
> \tag{B.10}
> \]
> In particular, after choosing any basis of \(E_N\), the right-hand side is
> equivalent to the finite rank condition
> \[
> \operatorname{rank}
> \left(
> \operatorname{vec}_{\rm sym}(A_C|_{E_N})
> \right)_{C\in\mathcal C_N}
> =\frac{N(N-1)}2.
> \tag{B.11}
> \]
> Appendix C proves this rank structurally from the almost-chain family; no
> finite-cardinality enumeration is part of the reduction above.

### Appendix C. Almost-chain classes and Laplacian triangularization

**Estado: prosa de trabajo.** Desarrolla la prueba constructiva all-\(N\) de
(4.1). Usa exclusivamente la reducción del Apéndice B y no enumera clases de
posets a cardinalidad fija.

> Fix \(N\ge2\). For each pair of integers
> \(0\le a<b\le N-1\), let \(C_{a,b}\) be the poset consisting of a chain
> \[
> c_1<\cdots<c_{N-1}
> \tag{C.1}
> \]
> and one further element \(z\), with
> \[
> c_i<z\quad(i\le a),
> \qquad
> z<c_i\quad(i>b),
> \qquad
> z\parallel c_i\quad(a<i\le b).
> \tag{C.2}
> \]
> Every linear extension of \(C_{a,b}\) is obtained by inserting \(z\)
> after exactly \(k\in\{a,\ldots,b\}\) elements of the chain; denote this
> extension by \(L_k\). For two such extensions, their intersection places
> \(c_1,\ldots,c_{\min(s,t)}\) below \(z\) and
> \(c_{\max(s,t)+1},\ldots,c_{N-1}\) above it. Therefore
> \[
> L_s\cap L_t=C_{a,b}
> \quad\Longleftrightarrow\quad
> \{s,t\}=\{a,b\}.
> \tag{C.3}
> \]
> Any \(\sigma\) with \(P_\sigma\cong C_{a,b}\) pulls the natural order and
> the \(\sigma\)-order back to an ordered realizer pair of \(C_{a,b}\).
> Conversely, enumerating the elements in the first order of any ordered
> realizer pair and recording their ranks in the second produces one such
> \(\sigma\). Applying an automorphism or a simultaneous relabeling to both
> orders does not change this relative-rank permutation, so no additional
> permutations arise from the choice of an isomorphism.
>
> So the only ordered realizer pairs are \((L_a,L_b)\) and
> \((L_b,L_a)\). After normalizing the first extension to the natural order,
> the relative permutation is a cycle \(\tau_{a,b}\) on the consecutive
> interval
> \[
> I_{a,b}=\{a+1,a+2,\ldots,b+1\},
> \tag{C.4}
> \]
> and reversing the ordered pair gives its inverse. Hence
> \[
> \Gamma_{C_{a,b}}
> =\{\tau_{a,b},\tau_{a,b}^{-1}\},
> \tag{C.5}
> \]
> as a set without multiplicity. When \(b=a+1\), the cycle is a
> transposition and the two displayed permutations coincide.
>
> These \(\binom N2\) classes are pairwise distinct. Indeed, the multiset of
> strict-past cardinalities is
> \[
> \bigl\{|\operatorname{Past}(y)|:y\in C_{a,b}\bigr\}
> =\{0,1,\ldots,b-1,b+1,\ldots,N-1\}\uplus\{a\}.
> \tag{C.6}
> \]
> It omits \(b\) and contains \(a\) twice, so it determines \((a,b)\).
> This means the construction supplies exactly one distinct class for
> each of the \(\binom N2\) pairs \(a<b\).
>
> For \(1\le i<j\le N\), define the edge Laplacian
> \[
> L_{ij}:=(e_i-e_j)(e_i-e_j)^\top.
> \tag{C.7}
> \]
> Each \(L_{ij}\) annihilates \(\mathbf1\) and preserves \(E_N\). If a
> linear combination of their restrictions vanishes on \(E_N\), it also
> vanishes on \(\operatorname{span}\{\mathbf1\}\), hence on all of
> \(\mathbb R^N\); its \((i,j)\) entry is \(-w_{ij}\), so every coefficient
> is zero. There are
> \(\binom N2=\dim\operatorname{Sym}(E_N)\) such matrices, and therefore
> \[
> \{L_{ij}|_{E_N}:1\le i<j\le N\}
> \quad\text{is a basis of }\operatorname{Sym}(E_N).
> \tag{C.8}
> Summing all edges gives the complete-graph Laplacian
> \[
> \sum_{1\le i<j\le N}L_{ij}
> =NI-\mathbf1\mathbf1^\top,
> \qquad
> \sum_{i<j}L_{ij}|_{E_N}=NI_{E_N}.
> \tag{C.9}
> \]
>
> Symmetrize the interval cycle by setting
> \[
> S_{a,b}:=P_{\tau_{a,b}}+P_{\tau_{a,b}}^\top.
> \tag{C.10}
> \]
> Equation (C.5) implies
> \[
> S_{a,b}
> =\begin{cases}
> 2A_{C_{a,b}},&b=a+1,\\
> A_{C_{a,b}},&b>a+1.
> \end{cases}
> \tag{C.11}
> \]
> The scalar relating \(S_{a,b}\) to the class sum is nonzero in both cases.
> On \(E_N\), put
> \[
> Q_{a,b}:=2I_{E_N}-S_{a,b}|_{E_N}.
> \tag{C.12}
> \]
> The matrix \(Q_{a,b}\) is the graph Laplacian of the consecutive cycle on
> \(I_{a,b}\), with the unique edge counted twice when the interval has
> length two. In the formulas below, each \(L_{ij}\) is understood as its
> restriction to \(E_N\). Thus
> \[
> Q_{a,a+1}=2L_{a+1,a+2},
> \tag{C.13}
> \]
> whereas, when \(b>a+1\),
> \[
> Q_{a,b}
> =L_{a+1,b+1}+\sum_{k=a+1}^{b}L_{k,k+1}.
> \tag{C.14}
> \]
> These identities are triangular in the interval length. They invert as
> \[
> L_{i,i+1}=\frac12Q_{i-1,i},
> \qquad
> L_{ij}=Q_{i-1,j-1}
> -\frac12\sum_{k=i}^{j-1}Q_{k-1,k}
> \quad(j>i+1).
> \tag{C.15}
> \]
> By (C.8),
> \[
> \operatorname{span}\{Q_{a,b}:0\le a<b\le N-1\}
> =\operatorname{Sym}(E_N).
> \tag{C.16}
> \]
>
> The common identity term in (C.12) still has to be removed. From (C.9)
> and (C.15), there are coefficients \(c_{a,b}\) such that
> \[
> I_{E_N}=\sum_{a<b}c_{a,b}Q_{a,b}.
> \tag{C.17}
> \]
> Their individual values are unnecessary, but their sum is not. An edge
> \(L_{ij}\) at distance \(d=j-i\) contributes total coefficient
> \(1-d/2\) in its expression through the \(Q\)'s: this is \(1/2\) for
> \(d=1\), and for \(d>1\) it is one long-interval term minus \(d\)
> adjacent terms of coefficient \(1/2\). Since there are \(N-d\) edges at
> distance \(d\), (C.9) gives
> \[
> \begin{aligned}
> s_N:=\sum_{a<b}c_{a,b}
> &=\frac1N\sum_{d=1}^{N-1}(N-d)\left(1-\frac d2\right)\\
> &=\frac{(N-1)(5-N)}{12}.
> \end{aligned}
> \tag{C.18}
> \]
> Substituting \(Q_{a,b}=2I_{E_N}-S_{a,b}|_{E_N}\) into (C.17) yields
> \[
> (1-2s_N)I_{E_N}
> =-\sum_{a<b}c_{a,b}S_{a,b}|_{E_N}.
> \tag{C.19}
> \]
> The coefficient of the identity never vanishes:
> \[
> 1-2s_N
> =\frac{N^2-6N+11}{6}
> =\frac{(N-3)^2+2}{6}>0.
> \tag{C.20}
> \]
> So \(I_{E_N}\) lies in the span of the
> \(S_{a,b}|_{E_N}\). Equation (C.12) then puts every \(Q_{a,b}\) in that
> same span, and (C.16) gives
> \[
> \operatorname{span}\{S_{a,b}|_{E_N}:a<b\}
> =\operatorname{Sym}(E_N).
> \tag{C.21}
> \]
> The remaining step, (C.11), shows that the selected class sums themselves
> span \(\operatorname{Sym}(E_N)\). Appendix B then transports (C.21) to
> \(V_N=\operatorname{Sym}^2P_{N-1}\), completing the constructive proof of
> Theorem C for every \(N\ge2\).

### Appendix D. Kernel, strict nesting, and density

**Estado: prosa de trabajo.** Demuestra las consecuencias funcionales de
Theorem C usadas en §§4–5 y §9. Todas las clausuras son en norma
Hilbert–Schmidt; ninguna afirmación de densidad se interpreta como
realizabilidad geométrica de cada tangente.

> Let
> \[
> \mathcal X=H\widehat\otimes H,
> \qquad
> \mathcal X_{\rm sym}=H\widehat\otimes_{\rm sym}H,
> \qquad
> \mathcal X_{\rm alt}=\bigwedge\nolimits^2H.
> \tag{D.1}
> \]
> The coordinate-swap involution
> \((\mathfrak s f)(u,v)=f(v,u)\) is unitary and self-adjoint. Its two
> eigenspaces are orthogonal, with projections
> \[
> \Pi_{\rm sym}=\frac{I+\mathfrak s}{2},
> \qquad
> \Pi_{\rm alt}=\frac{I-\mathfrak s}{2},
> \qquad
> \mathcal X=\mathcal X_{\rm sym}\oplus\mathcal X_{\rm alt}.
> \tag{D.2}
> \]
>
> By (B.8)–(B.9), every class representative \(R_C^{(N)}\) belongs to
> \(\mathcal X_{\rm sym}\). Appendix A gives
> \[
> (D\mathscr S_Nf)(C)
> =\frac{\langle f,R_C^{(N)}\rangle}{\mu_{N,0}^{[P]}(C)},
> \qquad
> \mu_{N,0}^{[P]}(C)>0.
> \tag{D.3}
> \]
> Hence
> \[
> \ker D\mathscr S_N
> =\ker G_{[P]}^{(N)}
> =\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}^{\perp_{\mathcal X}}.
> \tag{D.4}
> \]
> The first equality uses
> \(G_{[P]}^{(N)}(f,f)=\|D\mathscr S_Nf\|_{\mathcal K_N}^2\).
> Theorem C identifies the span in (D.4) with
> \(V_N=\operatorname{Sym}^2P_{N-1}\subset\mathcal X_{\rm sym}\). Splitting
> the ambient orthogonal complement according to (D.2) proves
> \[
> \boxed{
> \ker D\mathscr S_N
> =V_N^{\perp_{\rm sym}}\oplus\mathcal X_{\rm alt}
> =\left(\operatorname{Sym}^2P_{N-1}\right)^{\perp_{\rm sym}}
> \oplus\bigwedge\nolimits^2H.}
> \tag{D.5}
> \]
> Here \(\perp_{\rm sym}\) denotes the orthogonal complement inside
> \(\mathcal X_{\rm sym}\), not inside the full tensor product.
>
> Let \(P_N^{\rm vis}=\Pi_{V_N}\Pi_{\rm sym}\). Since
> \(V_N\subset\mathcal X_{\rm sym}\), this is the ambient orthogonal
> projection onto \(V_N\), and (D.5) gives
> \[
> \ker P_N^{\rm vis}=\ker D\mathscr S_N.
> \tag{D.6}
> \]
> If \(B_N=D\mathscr S_N|_{V_N}\), then \(B_N\) is injective: a vector in
> its kernel belongs simultaneously to \(V_N\) and \(V_N^\perp\). For every
> \(f\in\mathcal X\), (D.6) also gives
> \[
> D\mathscr S_Nf
> =D\mathscr S_NP_N^{\rm vis}f
> =B_NP_N^{\rm vis}f.
> \tag{D.7}
> \]
> This proves the exact factorization without identifying \(B_N\) with the
> support projection.
>
> For completeness, let
> \(q_N:\mathcal X\to\mathcal X/\ker D\mathscr S_N\) be the quotient map.
> The map
> \[
> J_N:\mathcal X/\ker D\mathscr S_N\longrightarrow V_N,
> \qquad
> J_N([f])=P_N^{\rm vis}f,
> \tag{D.8}
> \]
> is well defined by (D.6), is onto, and is injective for the same reason.
> The orthogonal decomposition
> \(\mathcal X=V_N\oplus\ker D\mathscr S_N\) gives
> \[
> \|[f]\|_{\mathcal X/\ker D\mathscr S_N}
> =\inf_{k\in\ker D\mathscr S_N}\|f+k\|_{\mathcal X}
> =\|P_N^{\rm vis}f\|_{\mathcal X}.
> \tag{D.9}
> \]
> Thus \(J_N\) is a canonical isometric isomorphism and
> \(D\mathscr S_N=B_NJ_Nq_N\). This is an identification of the differential
> quotient only.
>
> We next prove strict nesting. Orthogonality of the shifted-Legendre basis
> gives
> \[
> P_N=P_{N-1}\oplus\operatorname{span}\{p_N\}.
> \tag{D.10}
> \]
> Write \(x\odot y=x\otimes y+y\otimes x\). Taking symmetric tensor squares
> and using Theorem C,
> \[
> \begin{aligned}
> V_{N+1}=\operatorname{Sym}^2P_N
> &=\operatorname{Sym}^2P_{N-1}
> \oplus\{x\odot p_N:x\in P_{N-1}\}
> \oplus\operatorname{span}\{p_N\otimes p_N\}\\
> &=V_N\oplus\{x\odot p_N:x\in P_{N-1}\}
> \oplus\operatorname{span}\{p_N\otimes p_N\},
> \end{aligned}
> \tag{D.11}
> \]
> and the summands are orthogonal.
> In particular,
> \[
> p_1\odot p_N\in V_{N+1}\setminus V_N,
> \qquad
> V_N\subsetneq V_{N+1}
> \quad(N\ge2).
> \tag{D.12}
> \]
> The same witness gives the Fisher statement in Corollary E. For the
> nonsymmetrized tangent \(p_1\otimes p_N\), its symmetric component is
> \((p_1\odot p_N)/2\). Equation (D.5) annihilates it at size \(N\), whereas
> injectivity of \(B_{N+1}\) on \(V_{N+1}\) gives
> \[
> I_N^{[P]}(p_1\otimes p_N)=0,
> \qquad
> I_{N+1}^{[P]}(p_1\otimes p_N)>0.
> \tag{D.13}
> \]
>
> Finally, centered polynomials are dense in \(H=L_0^2([0,1])\). Indeed,
> if ordinary polynomials \(q_m\) converge in \(L^2\) to \(h\in H\), then
> \[
> \left\|q_m-\int_0^1q_m-h\right\|_{L^2}
> \le2\|q_m-h\|_{L^2}\longrightarrow0.
> \tag{D.14}
> \]
> Finite sums of elementary tensors from a dense subspace are dense in the
> Hilbert tensor product. Applying the continuous projection
> \(\Pi_{\rm sym}\), every symmetric Hilbert–Schmidt tensor can therefore be
> approximated by finite sums of symmetrized polynomial tensors. Each such
> finite sum belongs to \(\operatorname{Sym}^2P_m=V_{m+1}\) for some \(m\).
> So
> \[
> \boxed{
> \overline{\bigcup_{N\ge2}V_N}^{\,\|\cdot\|_{\mathcal X}}
> =\mathcal X_{\rm sym}.}
> \tag{D.15}
> \]
> Combining (D.5), strict nesting, and (D.15) also gives
> \[
> \bigcap_{N\ge2}\ker D\mathscr S_N
> =\bigwedge\nolimits^2H.
> \tag{D.16}
> \]
> Equation (D.16) concerns simultaneous first-order invisibility across all
> finite resolutions. It does not say that antisymmetric geometric paths are
> invisible to the nonlinear law: the explicit path of §7 has a nonzero
> second jet. Likewise, the Hilbert-space density in (D.15) does not assert
> that every element of \(\mathcal X_{\rm sym}\) is generated by an
> admissible geometric curve.

### Appendix E. Hilbert–Schmidt bounds and Fisher retention

**Estado: prosa de trabajo.** Demuestra Theorem F separando el paso
observaciones continuas \(\to\) rangos del paso rangos \(\to\) poset no
etiquetado. Todas las convergencias son para tangentes fijos; no se obtiene
una tasa uniforme ni convergencia en norma de operadores. La dependencia
bibliográfica externa de (E.15) queda cerrada con cita explícita: el paso
determinista transporta el teorema de Gallai vía el puente primo probado en
`research_program/work_packages/wp6_d2_modular_fiber_score.md` §§6.4–6.5
(Theorem 3), y el paso probabilístico externo es
`wp6_d2_modular_fiber_score.md` §7.5, que aplica el Theorem 2/Lemma 1 de
Bouvel–Chauve–Mishna–Rossin. Estos nombres de archivo son sólo trazabilidad
editorial; el texto citable dentro del blockquote usa referencias
bibliográficas normales.

> For \(a\in H\), define the order-statistic transform
> \[
> \mathcal O_Na
> :=\bigl(\langle a,d_1^{(N)}\rangle,\ldots,
> \langle a,d_N^{(N)}\rangle\bigr)\in\mathbb R^N,
> \tag{E.1}
> \]
> and, for \(f\in\mathcal X\), define
> \[
> H_{ij}^{(N)}(f)
> :=\langle f,d_i^{(N)}\otimes d_j^{(N)}\rangle.
> \tag{E.2}
> \]
> So \(H^{(N)}(f)=(\mathcal O_N\otimes\mathcal O_N)f\). Since
> \(\sum_i d_i^{(N)}=N\) and both marginals of \(f\) vanish, this matrix has
> zero row and column sums. Appendix A gives the rank-permutation score as
> \[
> S_N^\Pi(f)(\sigma)=2\sum_{i=1}^NH_{i,\sigma(i)}^{(N)}(f).
> \tag{E.3}
> \]
>
> If \(H\) and \(K\) have zero row and column sums and \(\Pi_N\) is uniform
> on \(S_N\), splitting the average according to \(i=j\) and \(i\ne j\)
> gives
> \[
> \mathbb E_0\!\left[
> \sum_iH_{i,\Pi_N(i)}\sum_jK_{j,\Pi_N(j)}
> \right]
> =\frac1{N-1}\langle H,K\rangle_F.
> \tag{E.4}
> \]
> Indeed, the diagonal contribution is \(N^{-1}\langle H,K\rangle_F\),
> while the zero-sum identities reduce the off-diagonal numerator to
> \(\langle H,K\rangle_F\), with probability factor
> \(1/[N(N-1)]\). Consequently,
> \[
> G_N^\Pi(f,g)
> =\frac4{N-1}
> \left\langle H^{(N)}(f),H^{(N)}(g)\right\rangle_F,
> \qquad
> I_N^\Pi(f)=\frac4{N-1}\|H^{(N)}(f)\|_F^2.
> \tag{E.5}
> \]
>
> Jensen's inequality and \(\sum_i d_i^{(N)}=N\) imply
> \(\|\mathcal O_Na\|_{\ell^2}\le\sqrt N\|a\|_{L^2}\). Hence
> \[
> \|H^{(N)}(f)\|_F\le N\|f\|_{\mathcal X},
> \qquad
> 0\le\frac{I_N^\Pi(f)}N
> \le\frac{4N}{N-1}\|f\|_{\mathcal X}^2
> \le8\|f\|_{\mathcal X}^2.
> \tag{E.6}
> \]
> This is the uniform Hilbert–Schmidt bound used below.
>
> The limit of the rank Fisher form is more precise. Let
> \((\ell_m)_{m\ge1}\) be an orthonormal shifted-Legendre basis of \(H\) and
> put \(\widetilde{\mathcal O}_N=N^{-1/2}\mathcal O_N\). The positive
> operator \(\widetilde{\mathcal O}_N^*\widetilde{\mathcal O}_N\) is the
> Bernstein–Durrmeyer operator of degree \(N-1\). It is triangular on the
> nested polynomial spaces: the beta-integral formula applied to a monomial
> of degree \(m\le N-1\) gives diagonal coefficient
> \[
> \frac{N!(N-1)!}{(N+m)!(N-1-m)!}
> =\prod_{r=1}^m\frac{N-r}{N+r}.
> \]
> Self-adjointness then makes the orthogonal differences between successive
> polynomial spaces invariant, so the \(\ell_m\) are eigenfunctions, with
> \[
> \lambda_{N-1,m}
> =\prod_{r=1}^m\frac{N-r}{N+r}
> \quad(1\le m\le N-1),
> \qquad
> \lambda_{N-1,m}=0\quad(m\ge N).
> \tag{E.7}
> \]
> For each fixed \(m\), these eigenvalues lie in \([0,1]\) and converge to
> one. If
> \(f=\sum_{j,k\ge1}c_{jk}\ell_j\otimes\ell_k\), then
> \[
> \frac{I_N^\Pi(f)}N
> =\frac{4N}{N-1}
> \sum_{j,k\ge1}
> \lambda_{N-1,j}\lambda_{N-1,k}|c_{jk}|^2.
> \tag{E.8}
> \]
> Dominated convergence in the square-summable coefficient array yields
> \[
> \boxed{
> \frac{I_N^\Pi(f)}N\longrightarrow4\|f\|_{\mathcal X}^2
> \qquad(f\in\mathcal X).}
> \tag{E.9}
> \]
>
> We now isolate the second channel. Conditional expectation of scores under
> \(\Pi_N\mapsto[P_{\Pi_N}]\) and the law of total variance give
> \[
> \Delta_N(f,g):=G_N^\Pi(f,g)-G_{[P]}^{(N)}(f,g)
> =\mathbb E_0\!\left[
> \operatorname{Cov}_0(S_N^\Pi(f),S_N^\Pi(g)\mid[P_{\Pi_N}])
> \right].
> \tag{E.10}
> \]
> Thus \(\Delta_N\) is positive semidefinite and
> \(0\le\Delta_N(f,f)\le I_N^\Pi(f)\).
>
> First suppose that \(f\in\mathcal X_{\rm sym}\) has finite rank. Its
> spectral decomposition has the form
> \(f=\sum_{r=1}^R\alpha_r a_r\otimes a_r\), with centered orthonormal
> \(a_r\in H\). Put \(x_i=(\mathcal O_Na)_i\) for one fixed profile. The
> spectral convergence above and a bounded-function approximation give
> \[
> \frac1N\sum_{i=1}^Nx_i^2\longrightarrow\|a\|_2^2,
> \qquad
> \max_i|x_i|=o(\sqrt N),
> \qquad
> \sum_i x_i=0.
> \tag{E.11}
> \]
> For the second assertion, choose bounded \(b\) close to \(a\) in
> \(L^2\). Since \(0\le d_i^{(N)}\le N\) and
> \(\int d_i^{(N)}=1\), uniformly in \(i\),
> \[
> \frac{|(\mathcal O_Na)_i|}{\sqrt N}
> \le\frac{\|b\|_\infty}{\sqrt N}+\|a-b\|_2.
> \tag{E.12}
> \]
> Taking \(N\to\infty\) and then \(b\to a\) proves (E.11).
>
> Let \(X_N(a)=\sum_i x_i x_{\Pi_N(i)}\),
> \(S_2=\sum_i x_i^2\), \(S_4=\sum_i x_i^4\), and
> \((N)_r=N(N-1)\cdots(N-r+1)\). Directly grouping the four indices by
> coincidence pattern gives, for \(N\ge4\),
> \[
> \begin{aligned}
> \mathbb E_0[X_N(a)^4]
> ={}&\frac{S_4^2}{N}
> +\frac{4S_4^2}{(N)_2}
> +\frac{3(S_2^2-S_4)^2}{(N)_2}\\
> &+\frac{6(2S_4-S_2^2)^2}{(N)_3}
> +\frac{9(S_2^2-2S_4)^2}{(N)_4}.
> \end{aligned}
> \tag{E.13}
> \]
> Equation (E.11) gives \(S_2=O(N)\) and
> \(S_4\le(\max_i|x_i|)^2S_2=o(N^2)\). Substitution in (E.13) yields
> \(\mathbb E_0[X_N(a)^4]=o(N^3)\). Since
> \(S_N^\Pi(f)=2\sum_{r=1}^R\alpha_rX_N(a_r)\), Minkowski's inequality in
> \(L^4\) gives
> \[
> \mathbb E_0[S_N^\Pi(f)^4]=o(N^3)
> \qquad(f\text{ symmetric and of fixed finite rank}).
> \tag{E.14}
> \]
>
> Two independent facts combine to supply a
> \([P_{\Pi_N}]\)-measurable event \(\mathcal G_N\) and constants
> \(C_{\rm fib},N_{\rm fib}<\infty\) such that
> \[
> \mathbb P_0(\mathcal G_N^c)\le\frac{C_{\rm fib}}N
> \quad(N\ge N_{\rm fib}),
> \qquad
> \Gamma_{[P_{\Pi_N}]}=\{\Pi_N,\Pi_N^{-1}\}
> \quad\text{on }\mathcal G_N,
> \tag{E.15}
> \]
> with the set understood without multiplicity for involutions. The first
> fact is deterministic: on the event that the incomparability graph
> \(G_{\Pi_N}^{\rm inc}\) is prime, the fiber of the unlabeled poset over
> \(\Pi_N\) collapses exactly to \(\{\Pi_N,\Pi_N^{-1}\}\). This is proved
> structurally, not merely cited, by transporting Gallai's uniqueness
> theorem for the two transitive orientations of a prime comparability
> graph — Gallai [*Transitiv orientierbare Graphen*, Acta Mathematica
> Academiae Scientiarum Hungaricae **18**, 1967, 25–66,
> DOI 10.1007/BF02020961] — to the two competing linear extensions of the
> finite poset. \(\mathcal G_N\) is taken to be exactly this primality
> event, which is \([P_{\Pi_N}]\)-measurable since the incomparability
> graph is determined up to isomorphism by the unlabeled poset. The second
> fact is probabilistic and external to this paper: the complementary event
> — the incomparability graph failing to be prime, i.e. the atypical shape
> of the associated strong interval tree — has probability \(O(N^{-1})\)
> under the uniform reference law, by the average-case analysis of Bouvel,
> Chauve, Mishna and Rossin [*Average-Case Analysis of Perfect Sorting by
> Reversals*, Combinatorial Pattern Matching (CPM 2009), LNCS 5577,
> 314–325, DOI 10.1007/978-3-642-02441-2_28], whose Theorem 2, via their
> Lemma 1, bounds exactly this exceptional probability. Combining the two
> gives (E.15), with \(C_{\rm fib}\) and \(N_{\rm fib}\) existential
> constants inherited from that source and not otherwise specified: this
> paper does not reprove, and does not sharpen, the \(O(N^{-1})\) estimate.
> For symmetric
> \(f\), (E.2) gives \(H^{(N)}(f)^\top=H^{(N)}(f)\), and hence
> \(S_N^\Pi(f)(\sigma^{-1})=S_N^\Pi(f)(\sigma)\). The conditional variance
> in (E.10) therefore vanishes on \(\mathcal G_N\). Cauchy–Schwarz and
> (E.14)–(E.15) imply
> \[
> \begin{aligned}
> 0\le\Delta_N(f,f)
> &\le\mathbb E_0\!\left[S_N^\Pi(f)^2
> \mathbf1_{\mathcal G_N^c}\right]\\
> &\le\mathbb P_0(\mathcal G_N^c)^{1/2}
> \mathbb E_0[S_N^\Pi(f)^4]^{1/2}
> =o(N).
> \end{aligned}
> \tag{E.16}
> \]
>
> To remove the finite-rank restriction, set
> \(\mathcal L_N(f,g)=\Delta_N(f,g)/N\) on
> \(\mathcal X_{\rm sym}\). Equations (E.6) and (E.10) give the uniform
> bound
> \[
> 0\le\mathcal L_N(f,f)\le8\|f\|_{\mathcal X}^2.
> \tag{E.17}
> \]
> Choose symmetric finite-rank \(f_R\to f\) in Hilbert–Schmidt norm before
> taking \(N\to\infty\). The triangle inequality for the seminorm induced by
> the positive form \(\mathcal L_N\) gives
> \[
> \sqrt{\mathcal L_N(f,f)}
> \le\sqrt{\mathcal L_N(f_R,f_R)}
> +\sqrt8\,\|f-f_R\|_{\mathcal X}.
> \tag{E.18}
> \]
> With \(R\) fixed, (E.16) makes the first term vanish as
> \(N\to\infty\); only afterwards is \(R\to\infty\) taken. Therefore
> \[
> \boxed{
> \frac{\Delta_N(f,f)}N\longrightarrow0,
> \qquad
> \frac{I_N^{[P]}(f)}N\longrightarrow4\|f\|_{\mathcal X}^2
> \quad(f\in\mathcal X_{\rm sym}).}
> \tag{E.19}
> \]
>
> For \(0\ne f\in\mathcal X_{\rm sym}\), (E.9) provides a finite threshold
> \(N_0(f)\) such that \(I_N^\Pi(f)>0\) for every \(N\ge N_0(f)\). On that
> range the three ratios in (6.18) are well defined, and (E.9) and (E.19)
> give
> \[
> \rho_N(f)\longrightarrow1,
> \qquad
> \kappa_N(f)\longrightarrow1,
> \qquad
> \eta_N^{\rm tot}(f)\longrightarrow1.
> \tag{E.20}
> \]
> The threshold depends on \(f\); no ratio is assigned when its denominator
> is zero.
>
> For the full tensor space, write \(f=f_s+f_a\) according to (D.2).
> The transform in (E.2) intertwines coordinate swap with matrix transpose,
> so \(H^{(N)}(f_s)\) is symmetric and \(H^{(N)}(f_a)\) is skew-symmetric.
> Frobenius orthogonality in (E.5), together with the exact antisymmetric
> kernel in (D.5), gives
> \[
> I_N^\Pi(f)=I_N^\Pi(f_s)+I_N^\Pi(f_a),
> \qquad
> I_N^{[P]}(f)=I_N^{[P]}(f_s).
> \tag{E.21}
> \]
> Combining (E.9), (E.19), and (E.21),
> \[
> \frac{I_N^{[P]}(f)}{4N\|f\|_{\mathcal X}^2}
> \longrightarrow
> \frac{\|f_s\|_{\mathcal X}^2}
> {\|f_s\|_{\mathcal X}^2+\|f_a\|_{\mathcal X}^2}
> \qquad(f\ne0).
> \tag{E.22}
> \]
>
> Finally, by the definition in (6.2),
> \[
> \langle f,\widehat F_Nf\rangle
> =\frac{I_N^{[P]}(f)}{4N}
> \longrightarrow\|\Pi_{\rm sym}f\|_{\mathcal X}^2.
> \tag{E.23}
> \]
> Polarization gives weak-operator convergence to \(\Pi_{\rm sym}\). Since
> \(0\le\widehat F_N\le I\), also
> \(\widehat F_N^2\le\widehat F_N\); using this inequality in the squared
> norm gives
> \[
> \begin{aligned}
> \|\widehat F_Nf-\Pi_{\rm sym}f\|^2
> &\le\langle f,\widehat F_Nf\rangle
> +\|\Pi_{\rm sym}f\|^2
> -2\operatorname{Re}
> \langle\widehat F_Nf,\Pi_{\rm sym}f\rangle
> \longrightarrow0.
> \end{aligned}
> \]
> This upgrades the weak convergence to
> \[
> \boxed{\widehat F_N\xrightarrow{\rm SOT}\Pi_{\rm sym}.}
> \tag{E.24}
> \]
> This convergence is not uniform. For
> \(h_N=p_N\otimes p_N/\|p_N\|_{L^2}^2\), one has \(\|h_N\|=1\),
> \(h_N\perp V_N\), and therefore
> \[
> \widehat F_Nh_N=0,
> \qquad
> \Pi_{\rm sym}h_N=h_N,
> \qquad
> \|\widehat F_N-\Pi_{\rm sym}\|\ge1
> \quad\text{for every }N.
> \tag{E.25}
> \]
> The result is an ambient Hilbert-space retention theorem. Its application
> to geometry is restricted to tangents already known to arise from
> admissible S1 paths.

### Appendix F. Exact matrices and spectra for \(N=2,3,4\)

**Estado: prosa de trabajo.** Documenta los cálculos racionales de
(6.5)–(6.13) en las bases modales allí fijadas. No extiende esos cálculos a
cardinalidad general ni modifica la interpretación de Theorem F.

> Put
> \[
> x(t):=t-\frac12,\qquad
> q(t):=\left(t-\frac12\right)^2-\frac1{12},\qquad
> r(t):=\left(t-\frac12\right)^3
>       -\frac3{20}\left(t-\frac12\right).
> \tag{F.1}
> \]
> Direct integration gives the mutually orthogonal modal norms
> \[
> \|x\|^2=\frac1{12},\qquad
> \|q\|^2=\frac1{180},\qquad
> \|r\|^2=\frac1{2800}.
> \tag{F.2}
> \]
> For cardinality \(N\), the continuous reference experiment consists of
> \(N\) iid copula observations. By (A.4), its score is
> \(2\sum_{k=1}^N f(U_k,V_k)\), and therefore
> \[
> G_{\rm full}^{(N)}(f,g)=4N\langle f,g\rangle.
> \tag{F.3}
> \]
> In any basis of \(V_N\), the nonzero eigenvalues of
> \(\widehat F_N\) are the generalized eigenvalues of
> \[
> G_{[P]}^{(N)}v=\lambda\,G_{\rm full}^{(N)}v.
> \tag{F.4}
> \]
> So the matrix of the Fisher form in a non-normalized basis is not the
> matrix of the operator \(\widehat F_N\); the continuous Gram matrix in
> (F.4) supplies the metric with respect to which the operator is
> represented.
>
> **Cardinality \(N=2\).** Let \(e_{11}=x\otimes x\). Formula (6.6),
> equivalently (A.13) specialized to the two poset classes, gives
> \[
> G_{[P]}^{(2)}(f,g)
> =256\langle f,e_{11}\rangle\langle g,e_{11}\rangle.
> \tag{F.5}
> \]
> Since \(\|e_{11}\|^2=\|x\|^4=1/144\), evaluation of (F.5) on
> \(e_{11}\), together with (F.3), yields
> \[
> [G_{[P]}^{(2)}]=\left(\frac1{81}\right),
> \qquad
> [G_{\rm full}^{(2)}]=\left(\frac1{18}\right).
> \tag{F.6}
> \]
> Their generalized quotient is therefore
> \[
> \operatorname{spec}_+(\widehat F_2)
> =\left\{\frac{1/81}{1/18}\right\}
> =\left\{\frac29\right\}.
> \tag{F.7}
> \]
>
> **Cardinality \(N=3\).** Use the orthogonal ordered basis
> \[
> e_{11}=x\otimes x,\qquad
> e_{12}=x\otimes q+q\otimes x,\qquad
> e_{22}=q\otimes q.
> \tag{F.8}
> \]
> Substitution of the five class derivatives in the Fisher formula (A.13)
> gives the first matrix below. For the second, (F.2)–(F.3) give
> \(12\|e_{11}\|^2=1/12\),
> \(12\|e_{12}\|^2=12\cdot2\|x\|^2\|q\|^2=1/90\), and
> \(12\|e_{22}\|^2=1/2700\). Hence
> \[
> [G_{[P]}^{(3)}]
> =\operatorname{diag}\left(
> \frac1{32},\frac1{1200},\frac1{180000}
> \right),
> \qquad
> [G_{\rm full}^{(3)}]
> =\operatorname{diag}\left(
> \frac1{12},\frac1{90},\frac1{2700}
> \right).
> \tag{F.9}
> \]
> Both matrices are diagonal in the same basis, so their entrywise
> generalized quotients give
> \[
> \operatorname{spec}_+(\widehat F_3)
> =\left\{\frac38,\frac3{40},\frac3{200}\right\},
> \tag{F.10}
> \]
> with eigenvectors \(e_{11},e_{12},e_{22}\), respectively. This records
> only Fisher anisotropy inside the three-dimensional visible support fixed
> in §4.
>
> **Cardinality \(N=4\).** In exactly the order used in (6.9), set
> \[
> \begin{aligned}
> e_{11}&=x\otimes x,&
> e_{12}&=x\otimes q+q\otimes x,&
> e_{13}&=x\otimes r+r\otimes x,\\
> e_{22}&=q\otimes q,&
> e_{23}&=q\otimes r+r\otimes q,&
> e_{33}&=r\otimes r.
> \end{aligned}
> \tag{F.11}
> \]
> The exact class-score calculation from (A.13) gives
> \[
> [G_{[P]}^{(4)}]
> =
> \begin{pmatrix}
> 4/75&0&0&0&0&0\\
> 0&8/3375&0&0&0&0\\
> 0&0&1/55125&1/354375&0&1/38587500\\
> 0&0&1/354375&11/455625&0&-1/49612500\\
> 0&0&0&0&2/4134375&0\\
> 0&0&1/38587500&-1/49612500&0&11/5402250000
> \end{pmatrix}.
> \tag{F.12}
> \]
> Orthogonality and (F.2)–(F.3) give the corresponding continuous Gram
> matrix
> \[
> [G_{\rm full}^{(4)}]
> =\operatorname{diag}\left(
> \frac19,\frac2{135},\frac1{1050},
> \frac1{2025},\frac1{15750},\frac1{490000}
> \right).
> \tag{F.13}
> \]
> The isolated diagonal entries of (F.12)–(F.13) immediately produce the
> three pure channels
> \[
> \lambda_{11}=\frac{4/75}{1/9}=\frac{12}{25},\qquad
> \lambda_{12}=\frac{8/3375}{2/135}=\frac4{25},\qquad
> \lambda_{23}=\frac{2/4134375}{1/15750}=\frac4{525}.
> \tag{F.14}
> \]
> On the remaining invariant block
> \(\operatorname{span}\{e_{13},e_{22},e_{33}\}\), taking
> \(\det(G_{[P],\rm mix}^{(4)}-\lambda
> G_{\rm full,\rm mix}^{(4)})\) gives, up to a nonzero rational factor,
> \[
> 144703125\lambda^3
> -9975000\lambda^2
> +142000\lambda
> -128.
> \tag{F.15}
> \]
> Its three roots are positive because the Fisher operator \(F_4\) is
> positive definite on its support \(V_4\). For orientation only, as in
> §6, they are
> \[
> 0.0494521212879\ldots,\qquad
> 0.0185160720400\ldots,\qquad
> 0.000966047034941\ldots.
> \tag{F.16}
> \]
> Combining the three pure factors with the mixed block gives the full
> generalized characteristic determinant, again up to a nonzero rational
> factor:
> \[
> (25\lambda-12)(25\lambda-4)(525\lambda-4)
> \left(
> 144703125\lambda^3
> -9975000\lambda^2
> +142000\lambda
> -128
> \right).
> \tag{F.17}
> \]
>
> This appendix only documents the exact fixed-\(N\) calculations used in
> §6. It provides no all-\(N\) spectral formula, proves no monotonicity of
> eigenvalues with \(N\), and does not identify \(F_N\) with
> \(P_N^{\rm vis}\). The generalized quotients compare the unlabeled-poset
> law with \(N\) continuous observations of the reference copula. They are
> not fractions of geometry and are not reconstruction results. No new
> claim is added here.

### Appendix G. Second-order derivatives and uniform-deletion kernel

**Estado: prosa de trabajo, cierre de apéndice — el último previsto.**
Cierra en detalle el cálculo explícito de §7 ((7.1)–(7.16)), con anclas en
`docs/hoja_de_ruta_septiembre_2026.md` §§5.5–5.6 para la senda admisible y el
cálculo exacto en \(N=2\), y §5.4bis del mismo documento para el kernel de
borrado uniforme. `dev/wp6_second_order_antisymmetric_witness.py` se usa
exclusivamente como backend exacto de verificación de las fracciones que
siguen, no como fuente de la prueba. La convención de likelihood/score es la
de Appendix A. Esta sección trata una única senda antisimétrica explícita.
No clasifica el segundo diferencial general, no define un operador \(Q_N\)
ni un cono cuadrático nulo, y no amplía Corollary H con un resultado
distinto del ya enunciado en §7.

> **The witness and the finite likelihood.** With \(\ell_1,\ell_2\) as in
> (7.1) and the generator \(\psi\) of (7.1)–(7.2),
> \[
> \bar\psi=0,
> \qquad
> \|\psi\|_{L^2(D)}^2=2,
> \]
> already established in §7; realizability is not reopened here. For exact
> polynomial integration it is convenient to use the equivalent factored
> form, obtained from (7.1) by direct expansion in \(u,v\):
> \[
> \psi(u,v)
> =-2\sqrt{15}\,(u-v)\bigl(6uv-3u-3v+2\bigr).
> \tag{G.1}
> \]
> For \(\pi\in S_N\) and two independent families of uniform order
> statistics \(U_{(1)}<\dots<U_{(N)}\), \(V_{(1)}<\dots<V_{(N)}\), set
> \[
> T_\pi:=\sum_{i=1}^N\psi\bigl(U_{(i)},V_{(\pi(i))}\bigr).
> \tag{G.2}
> \]
> Since \(\psi\) is bounded on the compact \(D\), the integrand
> \(e^{2\varepsilon T_\pi}\) defining the numerator and the integrand
> \(e^{2\varepsilon\psi}\) defining \(Z(\varepsilon)\), together with their
> \(\varepsilon\)-derivatives of every order, are uniformly dominated on
> every compact interval of \(\varepsilon\); differentiation under the
> integral is therefore valid to every order, so both the numerator and
> \(Z(\varepsilon)\) are real analytic, and \(Z(\varepsilon)>0\) for every
> \(\varepsilon\in\mathbb R\) because the integrand is strictly positive.
> So, exactly as in (7.7),
> \[
> \boxed{
> p_\pi(\varepsilon)
> =\frac{\bigl\langle e^{2\varepsilon T_\pi}\bigr\rangle_0}
>        {N!\,Z(\varepsilon)^N},
> }
> \qquad
> Z(\varepsilon)=\int_De^{2\varepsilon\psi}\,d\mu_0,
> \tag{G.3}
> \]
> where \(\langle\cdot\rangle_0\) is expectation, at \(\varepsilon=0\),
> under the two independent order-statistic vectors, and \(p_\pi\) is real
> analytic on all of \(\mathbb R\).
>
> **First and second derivatives.** Since \(\bar\psi=0\),
> \(Z'(0)=2\int_D\psi\,d\mu_0=0\) and
> \[
> Z''(0)=4\int_D\psi^2\,d\mu_0=4\|\psi\|_{L^2(D)}^2.
> \]
> Expanding \(\langle e^{2\varepsilon T_\pi}\rangle_0
> =1+2\varepsilon\langle T_\pi\rangle_0
> +2\varepsilon^2\langle T_\pi^2\rangle_0+O(\varepsilon^3)\) and
> \(Z(\varepsilon)^{-N}=1-2N\|\psi\|_{L^2(D)}^2\varepsilon^2+O(\varepsilon^4)\)
> in (G.3) and matching coefficients gives
> \[
> \boxed{
> p_\pi'(0)=\frac2{N!}\langle T_\pi\rangle_0,
> }
> \qquad
> \boxed{
> p_\pi''(0)=\frac4{N!}
> \left(\langle T_\pi^2\rangle_0-N\|\psi\|_{L^2(D)}^2\right).
> }
> \tag{G.4}
> \]
> This reproduces (7.9); it is a scalar identity attached to the single
> path (G.3), not the definition of an operator on \(\bigwedge^2H\).
>
> **Parity.** Since \(\psi(v,u)=-\psi(u,v)\), relabeling the dummy
> variables in (G.2)–(G.3) — the \(U\)- and \(V\)-order-statistic families
> are independent and identically distributed, so exchanging their roles is
> a valid change of variables — turns \(T_\pi\) into \(-T_{\pi^{-1}}\)
> after reindexing \(j=\pi(i)\), and turns \(Z(\varepsilon)\) into
> \(Z(-\varepsilon)\) with \(Z(-\varepsilon)=Z(\varepsilon)\). Hence
> \[
> p_\pi(-\varepsilon)=p_{\pi^{-1}}(\varepsilon),
> \tag{G.5}
> \]
> which is (7.7). Each fiber \(\Gamma_C\) is closed under inversion (§3),
> so summing (G.5) over \(\Gamma_C\) gives
> \[
> \boxed{
> \mu_{N,\varepsilon}^{[P]}(C)=\mu_{N,-\varepsilon}^{[P]}(C)
> }
> \qquad(N\ge2,\ C\in\mathcal C_N),
> \tag{G.6}
> \]
> which is (7.5). Every odd derivative of every class probability vanishes
> at \(\varepsilon=0\); this documents the computation of §7 and is not a
> new parity theorem.
>
> **Self-contained computation at \(N=2\).** The two permutations of
> \(S_2\) are the identity, whose fiber is the chain, and the transposition,
> whose fiber is the antichain:
> \[
> T_{\rm chain}=\psi(U_{(1)},V_{(1)})+\psi(U_{(2)},V_{(2)}),
> \qquad
> T_{\rm antichain}=\psi(U_{(1)},V_{(2)})+\psi(U_{(2)},V_{(1)}),
> \]
> with \((U_{(1)},U_{(2)})\) and \((V_{(1)},V_{(2)})\) two independent
> pairs of order statistics of two uniforms on \([0,1]\), jointly
> distributed with density \(2\) on each simplex \(0<t_1<t_2<1\).
>
> Both permutations of \(S_2\) are involutions
> (\(\mathrm{id}^{-1}=\mathrm{id}\), \(\mathrm{swap}^{-1}=\mathrm{swap}\)),
> so (G.5) gives \(p_\pi(-\varepsilon)=p_\pi(\varepsilon)\) for each
> individually, and in particular
> \[
> \langle T_{\rm chain}\rangle_0=\langle T_{\rm antichain}\rangle_0=0,
> \tag{G.7}
> \]
> already at the level of a single permutation, not only of its class —
> reproducing exactly the vanishing recorded for \(N=2\) in (7.9).
>
> For the second moments, expand \(\psi=\ell_1\otimes\ell_2-\ell_2\otimes
> \ell_1\) inside each square. Because the \(U\)-process is independent of
> the \(V\)-process, every cross term factors into a product of a
> two-point \(U\)-moment and a two-point \(V\)-moment (identically
> distributed to the \(U\)-moments). Write, for \(j,k\in\{1,2\}\) and
> \(i\in\{1,2\}\),
> \[
> A_{jk}:=\mathbb E\bigl[\ell_j(U_{(1)})\,\ell_k(U_{(2)})\bigr],
> \qquad
> M_i(jk):=\mathbb E\bigl[\ell_j(U_{(i)})\,\ell_k(U_{(i)})\bigr].
> \tag{G.8}
> \]
> Direct integration against the pair density \(2\) on \(0<t_1<t_2<1\)
> and the marginal order-statistic densities \(2(1-t)\) (\(i=1\)) and
> \(2t\) (\(i=2\)) gives the elementary values
> \[
> A_{11}=A_{22}=0,
> \qquad
> A_{12}=-A_{21}=\frac1{\sqrt{15}},
> \tag{G.9}
> \]
> \[
> M_1(11)=M_1(22)=M_2(11)=M_2(22)=1,
> \qquad
> M_1(12)=-\frac2{\sqrt{15}}=-M_2(12).
> \tag{G.10}
> \]
> Expanding \(\psi(x,y)^2=\ell_1(x)^2\ell_2(y)^2
> -2\ell_1(x)\ell_2(x)\ell_1(y)\ell_2(y)+\ell_2(x)^2\ell_1(y)^2\) and using
> independence of same- or different-index order statistics from the two
> processes,
> \[
> \bigl\langle\psi(U_{(i)},V_{(i)})^2\bigr\rangle_0
> =2M_i(11)M_i(22)-2M_i(12)^2,
> \qquad
> \bigl\langle\psi(U_{(1)},V_{(2)})^2\bigr\rangle_0
> =M_1(11)M_2(22)-2M_1(12)M_2(12)+M_1(22)M_2(11),
> \]
> and, expanding the cross products
> \(\psi(U_{(1)},V_{(1)})\psi(U_{(2)},V_{(2)})\) and
> \(\psi(U_{(1)},V_{(2)})\psi(U_{(2)},V_{(1)})\) into four terms each and
> grouping \(U\)-factors against \(V\)-factors,
> \[
> \bigl\langle\psi(U_{(1)},V_{(1)})\psi(U_{(2)},V_{(2)})\bigr\rangle_0
> =2A_{11}A_{22}-2A_{12}A_{21},
> \qquad
> \bigl\langle\psi(U_{(1)},V_{(2)})\psi(U_{(2)},V_{(1)})\bigr\rangle_0
> =-\bigl(A_{12}^2+A_{21}^2\bigr).
> \]
> Substituting (G.9)–(G.10): each diagonal term of \(T_{\rm chain}^2\)
> equals \(2(1)(1)-2(2/\sqrt{15})^2=22/15\), and the cross term equals
> \(2(0)(0)-2(1/\sqrt{15})(-1/\sqrt{15})=2/15\); each diagonal term of
> \(T_{\rm antichain}^2\) equals
> \(1-2(-2/\sqrt{15})(2/\sqrt{15})+1=38/15\), and the cross term equals
> \(-(1/15+1/15)=-2/15\). Summing,
> \[
> \boxed{
> \langle T_{\rm chain}^2\rangle_0
> =2\cdot\frac{22}{15}+2\cdot\frac2{15}=\frac{16}5,
> \qquad
> \langle T_{\rm antichain}^2\rangle_0
> =2\cdot\frac{38}{15}+2\left(-\frac2{15}\right)=\frac{24}5.
> }
> \tag{G.11}
> \]
> With \(N\|\psi\|_{L^2(D)}^2=2\cdot2=4\), (G.4) and (G.11) give
> \[
> \boxed{
> \mu_2''(\mathrm{antichain})=\frac45\left(\frac{24}5-4\right)=\frac85,
> \qquad
> \mu_2''(\mathrm{chain})=\frac45\left(\frac{16}5-4\right)=-\frac85,
> }
> \tag{G.12}
> \]
> together with \(\mu_{2,0}(\mathrm{antichain})=\mu_{2,0}(\mathrm{chain})
> =\tfrac12\) from the uniform reference law on \(S_2\), and the exact
> check \(\sum_C\mu_2''(C)=\tfrac85-\tfrac85=0\), consistent with (G.6)
> summed over \(\varepsilon\)-independent total mass. These fractions
> reproduce (7.10); the derivation above is self-contained.
>
> **The uniform-deletion kernel.** For \(m\ge3\) and unlabeled classes
> \(C\in\mathcal C_m\), \(D\in\mathcal C_{m-1}\), define
> \[
> K_{m,m-1}(C,D)
> :=\frac1m\#\{v\in C:[C\setminus\{v\}]=D\}.
> \tag{G.13}
> \]
> *Well-defined on classes.* Fix a labeled representative of \(C\); if
> \(\phi:C\to C'\) is a poset isomorphism onto another representative, then
> for every \(v\in C\) the restriction \(\phi|_{C\setminus\{v\}}\) is an
> isomorphism \(C\setminus\{v\}\to C'\setminus\{\phi(v)\}\), so \(\phi\)
> carries \(\{v\in C:[C\setminus v]=D\}\) bijectively onto
> \(\{v'\in C':[C'\setminus v']=D\}\). The count in (G.13), hence
> \(K_{m,m-1}(C,D)\), does not depend on the labeled representative chosen
> for \(C\).
>
> *Markov kernel.* Each summand is a nonnegative count, so
> \(K_{m,m-1}(C,D)\ge0\). Every \(v\in C\) deletes to a poset lying in
> exactly one class \(D\in\mathcal C_{m-1}\), so summing the count over all
> \(D\) counts each of the \(m\) elements of \(C\) exactly once:
> \[
> \sum_{D\in\mathcal C_{m-1}}K_{m,m-1}(C,D)=\frac1m\sum_{v\in C}1=1.
> \tag{G.14}
> \]
>
> *Parameter-independence.* (G.13) is a purely combinatorial count on
> unlabeled finite posets; it makes no reference to \(\varepsilon\) or to
> \(\mu_{m,\varepsilon}^{[P]}\).
>
> *Deletion of an iid point.* Let \(X_1,\dots,X_m\) be iid from
> \(q_\varepsilon\), and let \(V\) be uniform on \(\{1,\dots,m\}\),
> independent of the sample. For every fixed \(j\), \((X_i)_{i\ne j}\) is
> an iid sample of size \(m-1\) from \(q_\varepsilon\), being a fixed
> subvector of an iid vector; averaging over the uniform, independent
> choice of the deleted index leaves this law unchanged, so the joint law
> of \((X_i)_{i\ne V}\) is exactly the \((m-1)\)-fold product of
> \(q_\varepsilon\). Passing to ranks and then to the unlabeled poset gives,
> coordinatewise,
> \[
> \boxed{
> \mu_{m-1,\varepsilon}^{[P]}(D)
> =\sum_{C\in\mathcal C_m}
> \mu_{m,\varepsilon}^{[P]}(C)\,K_{m,m-1}(C,D)
> }
> \qquad(D\in\mathcal C_{m-1},\ m\ge3).
> \tag{G.15}
> \]
>
> **Composition to \(N=2\).** As in (7.13), define
> \[
> K_{N\to2}:=K_{3,2}\circ K_{4,3}\circ\cdots\circ K_{N,N-1},
> \qquad K_{2\to2}:=I.
> \tag{G.16}
> \]
> Iterating (G.15) from \(m=N\) down to \(m=3\) gives, for every
> \(\varepsilon\) and every \(N\ge2\),
> \[
> \mu_{2,\varepsilon}^{[P]}=K_{N\to2}\,\mu_{N,\varepsilon}^{[P]}.
> \tag{G.17}
> \]
>
> **Commutation with the jets.** For fixed \(N\), both sides of (G.17)
> are functions of \(\varepsilon\) valued in the finite-dimensional spaces
> \(\mathbb R^{\mathcal C_2}\) and \(\mathbb R^{\mathcal C_N}\), and
> \(K_{N\to2}\) is a fixed linear map between them, independent of
> \(\varepsilon\) by the third property of (G.13). Differentiating (G.17)
> \(k\) times therefore commutes termwise with this linear map — a matter
> of linearity on a finite-dimensional space, with no limit or asymptotic
> argument:
> \[
> \boxed{
> \bigl(\mu_2^{[P]}\bigr)^{(k)}(0)
> =K_{N\to2}\bigl(\mu_N^{[P]}\bigr)^{(k)}(0)
> }
> \qquad(k\ge1).
> \tag{G.18}
> \]
>
> **Closure of Corollary H.** Assembling the pieces above: parity (G.6)
> gives \(r_N(\gamma_\psi)\ge2\) for every \(N\ge2\), by definition (7.8).
> If \((\mu_N^{[P]})''(0)\) vanished for some \(N\ge2\), (G.18) with
> \(k=2\) would force \(K_{N\to2}(\mu_N^{[P]})''(0)=0\), i.e.
> \((\mu_2^{[P]})''(0)=0\) — contradicting the exact values \((8/5,-8/5)\)
> of (G.12). Hence, exactly as in Corollary H of §7,
> \[
> \boxed{
> r_N(\gamma_\psi)=2\qquad\forall N\ge2.
> }
> \tag{G.19}
> \]
> This closes Corollary H; it is not presented as a result distinct from
> it.
>
> This appendix treats a single explicit antisymmetric path, (G.1)–(G.3);
> it does not classify the general second differential on
> \(\bigwedge^2H\), does not define an operator \(Q_N\), and does not
> define a quadratic null cone. It does not assert that every element of
> \(\bigwedge^2H\) has \(r_N=2\): (G.19) is an existence and
> non-vanishing statement for the single witness \(\psi\) of (7.1),
> propagated to every \(N\ge2\) by the parameter-independent deletion
> kernel of (G.13)–(G.18), not a classification result. No estimator,
> consistency statement, or rate is introduced, and no nonlinear
> reconstruction is claimed. The vanishing of the first-order jet in (G.6)
> is the exact isometric fold \(\varepsilon\leftrightarrow-\varepsilon\)
> of Theorem G and (7.4)–(7.6); it must not be described as physical
> information loss. What (G.19) detects is the local magnitude of this
> deformation at second order, not its sign, which remains identified by
> the fold.

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
EXACT_S1_ALL_N_DIFFERENTIAL_CLASSIFICATION = PRIORITY_NOT_REFUTED_INTERNAL_AUDIT_CLOSED
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
   memoria. **CUERPO REDACTADO**: §2 (dominio S1, cuatro objetos, tres niveles
   observacionales, cadena \(\psi\to\mu_N^{[P]}\) cerrada), §3
   (representantes de score, forma Fisher y reducción matricial normativa),
   §4 (Teorema C: familia casi cadena, laplacianos de aristas, identidad en
   el span, Corolario E de filtración — kernel diferido a §5) y §5
   (Corolario D:
   factorización, kernel exacto, cociente canónico y separación entre
   soporte visible y codificación Fisher) y §6 (operador Fisher normalizado,
   espectros exactos \(N=2,3,4\), mezcla modal, retención simétrica HS y
   límite SOT), y §7 (órbita antisimétrica explícita, paridad exacta,
   segundo jet en \(N=2\) y propagación \(r_N=2\) all-\(N\)), §9
   (Discussion: ensamblaje de compresión, filtración, sensibilidad Fisher y
   pliegue de segundo orden), §10 (Limitations: alcance matemático,
   inferencial, dimensional y bibliográfico) y §11 (Conclusion: síntesis
   C1–C4 y techo S1 local/diferencial, sin reconstrucción no lineal)
   redactados; anclas
   `wp6_d2_geometric_tangent_classification.md` §§1,3,5 y
   `wp6_full_class_sum_rank_theorem.md` §§1–5,6.1–6.3 +
   `wp6_finite_n_visible_span_pattern_preflight.md` §§2–5. La dependencia
   de §4 hacia §3 queda cerrada mediante referencias a (3.10)–(3.14), sin
   definición autónoma duplicada; \(B_N\) permanece reservado para §5 y el
   isomorfismo finito se denota \(\Lambda_N\). Para §6, las anclas son
   `wp6_d2_geometric_tangent_classification.md` §§13–15 y
   `docs/hoja_de_ruta_septiembre_2026.md` §§5.3–5.4. Para §7, las anclas son
   la misma hoja de ruta §§5.5–5.6 y la consistencia por borrado de §5.4bis.
   Para §9, el ancla interpretativa es
   `wp6_full_class_sum_rank_theorem.md` §7.1.
   El cuerpo continuo queda completo. Appendices A (QMD y representantes de
   score), B (reducción finita a \(\operatorname{Sym}(E_N)\)), C (familia
   casi cadena y triangularización por laplacianos), D (kernel, nesting
   estricto y densidad simétrica HS), E (cotas HS y retención Fisher), F
   (matrices y espectros exactos para \(N=2,3,4\)) y G (derivadas de
   segundo orden en la senda antisimétrica explícita, cálculo autosuficiente
   en \(N=2\) y kernel de borrado uniforme, cerrando Corollary H para todo
   \(N\ge2\)) cerrados.

   ```text
   SECTION8_RELATED_WORK_FINAL_PROSE = CLOSED
   ALL_PLANNED_APPENDICES_DRAFTED
   APPENDIX_E_EXTERNAL_FIBER_DEPENDENCY = CLOSED_WITH_EXPLICIT_CITATION
   SECTION8_HUMAN_STYLE_PASS = CLOSED
   APPENDICES_A_G_HUMAN_STYLE_PASS = CLOSED
   INTRO_DISCUSSION_CONCLUSION_HUMAN_STYLE_PASS = CLOSED
   ABSTRACT_LIMITATIONS_HUMAN_STYLE_PASS = CLOSED
   GLOBAL_INTERNAL_CONSISTENCY_FIXES = CLOSED
   ```

   La dependencia bibliográfica de (E.15) queda cerrada con cita explícita
   (Gallai para la unicidad de orientaciones transitivas del cociente
   primo; Bouvel–Chauve–Mishna–Rossin para la cota \(O(N^{-1})\) del evento
   excepcional), sin reabrir el argumento matemático ya cerrado. §8 se
   convirtió de guía editorial a prosa final citable, cubriendo P1–P3 de la
   auditoría de prioridad (§§2–6 de la misma) sin elevar ningún veredicto.
   No se declara `PAPER_FINAL`: quedan pendientes la bibliografía final,
   la auditoría global de notación/labels/cross-references y el ensamblaje
   final del manuscrito.
6. Mantener fuera \(Q_N\) general salvo que el manuscrito revele una laguna
   lógica real y se emita una autorización separada.
