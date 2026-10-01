# Paquete de rederivación externa — `FULL_CLASS_SUM_RANK_THEOREM`

> **STATUS: EXTERNAL_REDERIVATION_PACKAGE_READY / NOT_SENT /
> FROM_SCRATCH_DERIVATION_REQUIRED / EIGHT_FAILURE_TARGETS /
> NOVELTY_CERTIFICATE_NO / FURTHER_MATHEMATICS_ON_HOLD.**

Fecha: 2026-08-29. Este paquete sustituye como gate matemático vigente al
paquete anterior, limitado a los cálculos `N=2,3`. Aquél se conserva como
registro histórico. Éste no abre `N=5`, no pide calcular nuevos espectros y no
solicita una revisión general del proyecto.

## 1. Instrucción al revisor

Estimado/a colega:

**Le pedimos una rederivación adversarial desde cero, no una comprobación línea
por línea de nuestra prueba.**

El resultado candidato afirma que, para todo `n >= 2`, el pullback Fisher de la
ley completa del poset causal no etiquetado sobre la clase tangente S1 tiene
espacio visible

\[
V_n=\operatorname{Sym}^2P_{n-1}
\tag{1.1}
\]

y rango

\[
\operatorname{rank}G_{[P]}^{(n)}=\binom n2.
\tag{1.2}
\]

Nuestra demostración usa una familia de posets casi cadena, sumas de matrices
de permutación y laplacianos de ciclos sobre intervalos. Para reducir el riesgo
de que el lector herede silenciosamente un error de esa ruta, le pedimos que
intente obtener o refutar (1.1)--(1.2) con su propia organización. Sólo después
compare con nuestro documento.

Una refutación parcial, un contraejemplo pequeño o una hipótesis omitida es más
útil que una aprobación general.

## 2. Alcance exacto del claim

Sea

\[
H=L_0^2([0,1])
\tag{2.1}
\]

y sea

\[
P_{n-1}=\operatorname{span}\{p_1,\ldots,p_{n-1}\}\subset H,
\tag{2.2}
\]

donde `p_k` es un polinomio ortogonal centrado de grado `k` para la medida
uniforme. El tangente S1 es

\[
f=\mathcal P\psi\in H\widehat\otimes H,
\tag{2.3}
\]

el score de una observación de la cópula en el nulo es `2f`, y el observable es
la clase de isomorfismo del poset producto inducido por `n` observaciones iid.

Se afirma:

\[
\boxed{
\begin{aligned}
V_n&=\operatorname{Sym}^2P_{n-1},\\
\dim V_n&=\binom n2,\\
V_n&\subsetneq V_{n+1},\\
I_n^{[P]}(p_1\otimes p_n)&=0<I_{n+1}^{[P]}(p_1\otimes p_n),\\
\overline{\bigcup_{n\ge2}V_n}
&=H\widehat\otimes_{\rm sym}H,\\
\bigwedge^2H&\subseteq\ker G_{[P]}^{(n)}\quad\forall n.
\end{aligned}}
\tag{2.4}
\]

No se afirma reconstrucción no lineal, identificabilidad global de geometrías,
resultado fuera de S1, ni novedad certificada.

## 3. Protocolo de independencia

Orden solicitado:

1. Lea únicamente §§1--2 de este paquete.
2. Fije sus propias convenciones para rankings, matrices de permutación y
   clases de posets.
3. Intente derivar el rango general sin consultar la prueba del proyecto.
4. Registre su derivación, incluso si queda incompleta.
5. Sólo entonces consulte
   `wp6_full_class_sum_rank_theorem.md` y complete los ocho ataques de §4.

Marque `INDEPENDENCE_COMPROMISED = YES` si ya había leído la prueba antes de
intentar la rederivación. Eso no invalida sus observaciones, pero impide llamar
al resultado una rederivación independiente.

No use los cálculos `N=2,3,4` como evidencia de que el teorema general debe ser
cierto. Pueden usarse únicamente como controles después de la derivación.

## 4. Ocho blancos obligatorios de fallo

### A1. Clases casi cadena y suma de clase

Para cada `0 <= a < b <= n-1`, la prueba construye una cadena

\[
c_1<\cdots<c_{n-1}
\tag{4.1}
\]

y un elemento `z` incomparable exactamente con
`c_(a+1),...,c_b`. Afirma que los únicos pares ordenados de extensiones
lineales cuya intersección recupera ese poset son los dos extremos de
inserción `(L_a,L_b)` y `(L_b,L_a)`. De ahí obtiene una permutación cíclica
`tau_(a,b)` sobre el intervalo consecutivo y su inversa.

Compruebe independientemente:

- que no falta ningún realizador;
- que normalizar el primer orden produce realmente el ciclo alegado;
- que automorfismos o relabelings no añaden permutaciones a la clase;
- que las `binom(n,2)` clases construidas son abstractamente distintas;
- el factor de multiplicidad cuando el ciclo es una transposición.

`A1 = FAIL` si cualquier suma de clase contiene más o menos términos que los
usados en la prueba.

### A2. Identidad de laplacianos y triangularización

La prueba define

\[
S_{a,b}=P_{\tau_{a,b}}+P_{\tau_{a,b}}^\top,
\qquad
Q_{a,b}=2I-S_{a,b},
\tag{4.2}
\]

restringidos a `E_n = 1^perp`, y afirma

\[
Q_{a,a+1}=2L_{a+1,a+2},
\tag{4.3}
\]

\[
Q_{a,b}=L_{a+1,b+1}+\sum_{k=a+1}^{b}L_{k,k+1}
\quad(b>a+1),
\tag{4.4}
\]

con

\[
L_{ij}=(e_i-e_j)(e_i-e_j)^\top.
\tag{4.5}
\]

Redérive (4.3)--(4.4) con una convención explícita para `P_tau`. Verifique que
la fórmula de inversión

\[
L_{ij}=Q_{i-1,j-1}
-\frac12\sum_{k=i}^{j-1}Q_{k-1,k}
\tag{4.6}
\]

tiene índices y factores correctos.

`A2 = FAIL` ante cualquier arista omitida, duplicada o con signo incorrecto.

### A3. Base de \(\operatorname{Sym}(\mathbf1^\perp)\)

Compruebe que las `binom(n,2)` restricciones `L_ij|E_n` son linealmente
independientes y generan todo `Sym(E_n)`, no sólo el subespacio de matrices
laplacianas visto en coordenadas ambientales.

Debe justificarse el paso entre:

- matrices simétricas `n x n` con sumas de filas cero;
- operadores autoadjuntos sobre el espacio `(n-1)`-dimensional `E_n`;
- formas bilineales simétricas sobre `E_n`.

`A3 = FAIL` si la restricción identifica combinaciones no triviales o si hay
una discrepancia de dimensión.

### A4. Eliminación del término identidad

La triangularización produce los `Q_(a,b)`, pero las sumas de clase son los
`S_(a,b)`. La prueba usa

\[
I_{E_n}=\frac1n\sum_{i<j}L_{ij}
\tag{4.7}
\]

y calcula que, en una expresión

\[
I_{E_n}=\sum_{a<b}c_{a,b}Q_{a,b},
\tag{4.8}
\]

la suma de coeficientes es

\[
s_n=\sum_{a<b}c_{a,b}=\frac{(n-1)(5-n)}{12}.
\tag{4.9}
\]

De ahí

\[
1-2s_n=\frac{(n-3)^2+2}{6}>0
\tag{4.10}
\]

y `I_E` pertenece al span de los `S_(a,b)`.

Redérive (4.7)--(4.10), preferiblemente obteniendo los coeficientes
`c_(a,b)` explícitos. Éste es un punto de fallo independiente de la
triangularización.

`A4 = FAIL` si el coeficiente puede anularse, si depende de una igualdad sólo
válida en dimensión pequeña o si no se recupera `I_E` de las sumas de clase.

### A5. Del rango combinatorio al espacio Fisher visible

Compruebe desde la ley iid que las densidades de order statistics

\[
d_i^{(n)}(t)=n\binom{n-1}{i-1}t^{i-1}(1-t)^{n-i}
\tag{4.11}
\]

al centrarse generan exactamente `P_(n-1)`, y que

\[
p'_\sigma(0;f)=\frac2{n!}
\sum_i\langle f,b_i^{(n)}\otimes b_{\sigma(i)}^{(n)}\rangle.
\tag{4.12}
\]

Debe verificarse:

- el factor `2/n!`;
- que las marginales nulas permiten centrar ambos factores;
- que el mapa `E_n -> P_(n-1)` es un isomorfismo;
- que sumar por clase de isomorfismo corresponde exactamente a `A_C`;
- que todas las probabilidades de las clases usadas son positivas;
- que el span de representantes de score coincide con el complemento del
  kernel de la forma Fisher.

`A5 = FAIL` si el rango matricial no se transporta fielmente a
`V_n = Sym^2 P_(n-1)`.

### A6. Inclusión estricta y witness universal

Suponiendo A1--A5, compruebe que

\[
P_{n-1}\subsetneq P_n
\tag{4.13}
\]

implica realmente

\[
V_n\subsetneq V_{n+1}.
\tag{4.14}
\]

Para el tangente no simetrizado `p_1 tensor p_n`, compruebe por separado que

\[
I_n^{[P]}(p_1\otimes p_n)=0
\tag{4.15}
\]

y

\[
I_{n+1}^{[P]}(p_1\otimes p_n)>0.
\tag{4.16}
\]

Debe declararse el papel de sus componentes simétrica y antisimétrica. No
basta con afirmar erróneamente que el tensor no simetrizado pertenece a
`V_(n+1)`.

`A6 = FAIL` si el witness no es admisible en S1, su componente simétrica se
anula o la positividad Fisher no sigue del teorema de rango.

### A7. Conclusión de densidad

Compruebe la cadena funcional-analítica

\[
\overline{\bigcup_mP_m}=H
\tag{4.17}
\]

\[
\Longrightarrow
\quad
\overline{\bigcup_m\operatorname{Sym}^2P_m}
=H\widehat\otimes_{\rm sym}H.
\tag{4.18}
\]

Especifique la topología, el producto tensorial de Hilbert y la convención de
`Sym^2`. Compruebe que la unión es creciente y que no se está sustituyendo
densidad de tensores de rango finito por una afirmación de reconstrucción no
lineal.

`A7 = FAIL` si cambia la topología, falta completitud o la conclusión excede el
sector tangente simétrico.

### A8. Kernel antisimétrico y cociente no etiquetado

Redérive que intercambiar las coordenadas nulas envía una permutación
`sigma` a `sigma^(-1)` y produce un poset abstractamente isomorfo. Compruebe
que cada clase está cerrada bajo inversión y que su representante de score es
simétrico.

Debe distinguirse entre:

- una simetría del nulo o de la base polinómica;
- una simetría accidental de `N=2,3,4`;
- la invariancia estructural introducida por observar sólo la clase de
  isomorfismo del poset.

`A8 = FAIL` si el argumento requiere simetría de la perturbación, si deja de
valer fuera de la base elegida o si observar el poset no etiquetado conserva
algún score antisimétrico.

## 5. Controles pequeños permitidos

Después de la rederivación general pueden usarse como controles:

\[
\operatorname{rank}G_{[P]}^{(2)}=1,
\qquad
\operatorname{rank}G_{[P]}^{(3)}=3,
\qquad
\operatorname{rank}G_{[P]}^{(4)}=6.
\tag{5.1}
\]

Y los witnesses

\[
I_2(x\otimes q)=0<I_3(x\otimes q),
\qquad
I_3(x\otimes r)=0<I_4(x\otimes r).
\tag{5.2}
\]

No se solicita ni autoriza usar `N=5` como sustituto de la prueba general.

## 6. Material que sólo debe abrirse después del intento independiente

1. Prueba principal:
   `research_program/work_packages/wp6_full_class_sum_rank_theorem.md`.
2. Reducción analítica previa:
   `research_program/work_packages/wp6_finite_n_visible_span_pattern_preflight.md`.
3. Casos ilustrativos:
   `research_program/work_packages/wp6_d2_geometric_tangent_classification.md`,
   §§13--15.
4. Auditoría de prioridad:
   `research_program/bibliography/wp6_finite_causal_order_fisher_spectrum_priority_audit.md`.
5. Cadena Bombelli--Surya:
   `research_program/bibliography/wp6_bombelli_citation_chain_adversarial_audit.md`.

## 7. Formulario de veredicto

```text
INDEPENDENCE_COMPROMISED = YES / NO
INDEPENDENT_DERIVATION_ATTACHED = YES / NO / PARTIAL

A1_CLASS_SUMS = PASS / FAIL / INCONCLUSIVE
A2_INTERVAL_LAPLACIANS = PASS / FAIL / INCONCLUSIVE
A3_EDGE_LAPLACIAN_BASIS = PASS / FAIL / INCONCLUSIVE
A4_IDENTITY_IN_CLASS_SUM_SPAN = PASS / FAIL / INCONCLUSIVE
A5_COMBINATORICS_TO_FISHER = PASS / FAIL / INCONCLUSIVE
A6_STRICT_NESTING_AND_WITNESS = PASS / FAIL / INCONCLUSIVE
A7_DENSITY = PASS / FAIL / INCONCLUSIVE
A8_ANTISYMMETRIC_KERNEL = PASS / FAIL / INCONCLUSIVE

FIRST_FAILED_EQUATION_OR_STEP:
COUNTEREXAMPLE_OR_CORRECTION:
OMITTED_HYPOTHESIS:

OVERALL_MATHEMATICAL_VERDICT = PASS / FAIL / INCONCLUSIVE
PRIOR_ART_FOUND = YES / NO / UNCERTAIN
RECOMMENDED_CLAIM = KEEP / NARROW / WITHDRAW / INCONCLUSIVE
```

Cada `PASS` requiere una derivación o localizador, no una impresión de
plausibilidad. `OVERALL_MATHEMATICAL_VERDICT = PASS` exige ocho `PASS` y una
derivación adjunta al menos suficientemente completa para reconstruir el
argumento.

## 8. Regla de decisión

- Un solo `FAIL` bloquea cualquier promoción del teorema hasta corregirlo o
  retirarlo.
- Un solo `INCONCLUSIVE` mantiene el resultado como
  `INTERNALLY_PROVED / EXTERNALLY_UNVERIFIED`.
- Ocho `PASS` con independencia no comprometida permiten etiquetar
  `EXTERNALLY_REDERIVED`, nunca `NOVELTY_CERTIFIED`.
- La prioridad bibliográfica se decide por separado; corrección matemática no
  implica novedad.
- No se abre nueva matemática, `N=5`, espectros o asintótica mientras este gate
  esté pendiente, salvo decisión explícita posterior del responsable.

## 9. Techo de reivindicación durante el gate

Texto permitido:

> Para la familia tangente S1, demostramos internamente que el pullback Fisher
> de las leyes de posets no etiquetados tiene rango exactamente `binom(n,2)`;
> sus espacios visibles forman una filtración estricta cuya unión es densa en
> el sector simétrico, mientras el sector antisimétrico permanece en el kernel.
> La demostración general está pendiente de rederivación externa.

```text
FRAMEWORK_NOVELTY = NO
MORE_N_MORE_RESOLUTION_NOVELTY = NO
FULL_CLASS_SUM_RANK_THEOREM = INTERNALLY_PROVED
EXTERNAL_REDERIVATION = PENDING
NOVELTY_CERTIFICATE = NO
FURTHER_MATHEMATICS = HOLD
PACKAGE_SENT = NO
```
