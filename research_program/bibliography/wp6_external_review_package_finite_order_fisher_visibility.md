# Paquete de revisión externa — visibilidad Fisher a orden finito, (N=2,3)

> **STATUS: EXTERNAL_REVIEW_PACKAGE_READY / NOT_SENT /
> EXACTLY_THREE_ADVERSARIAL_QUESTIONS / NO_NOVELTY_CERTIFICATE /
> N4_ON_HOLD.**

> **SUPERSEDED AS CURRENT MATHEMATICAL GATE.** Después de preparar este paquete
> se demostró internamente `FULL_CLASS_SUM_RANK_THEOREM` para todo `n >= 2`.
> El gate vigente es
> `wp6_external_rederivation_package_full_class_sum_rank_theorem.md`. Este
> documento se conserva como registro histórico de los ataques a `N=2,3` y no
> debe enviarse como si describiera el estado actual.

Fecha: 2026-08-29. Este paquete no solicita una revisión general del proyecto.
No abre `N=4`, no propone una teoría general en `N` y no pide confirmar una
conclusión. Pide intentar refutar tres puntos concretos.

## 1. Carta breve al lector

Estimado/a colega:

**No le pedimos que avale este trabajo. Le pedimos que intente romperlo en tres
lugares precisos: atribución, precedencia y cálculo.**

Partimos del marco de Bombelli para comparar geometrías lorentzianas mediante
las probabilidades de posets causales finitos. En una clase tangente explícita
en 1+1 dimensiones calculamos el pullback Fisher de la ley completa del poset
no etiquetado para cardinalidades dos y tres. La búsqueda interna y la cadena
de citantes no han localizado el mismo cálculo. Sabemos que esto no prueba
novedad, y por eso solicitamos una lectura externa estrecha.

Una referencia previa, una equivalencia que hayamos omitido o un error en una
fracción exacta es un resultado útil. No es necesario revisar ninguna otra
rama del repositorio.

## 2. Resultado sometido a revisión

Sean

\[
x(t)=t-\frac12,
\qquad
q(t)=\left(t-\frac12\right)^2-\frac1{12}.
\tag{2.1}
\]

El claim interno, acotado al modelo S1 y a `N=2,3`, es

\[
\boxed{
\begin{aligned}
V_2&=\operatorname{span}\{x\otimes x\},\\
V_3&=\operatorname{span}\{x\otimes x,
x\otimes q+q\otimes x,q\otimes q\},\\
\operatorname{rank}G_{[P]}^{(2)}&=1,
\qquad \operatorname{rank}G_{[P]}^{(3)}=3,\\
I_2^{[P]}(x\otimes q)&=0,
\qquad I_3^{[P]}(x\otimes q)=\frac1{4800},\\
\ker G_{[P]}^{(3)}&\subsetneq\ker G_{[P]}^{(2)}.
\end{aligned}}
\tag{2.2}
\]

Respecto del Fisher de tres observaciones iid de la cópula continua, el
problema generalizado sobre `V_3` tiene

\[
\boxed{
\lambda(x\otimes x)=\frac38,
\quad
\lambda(x\otimes q+q\otimes x)=\frac3{40},
\quad
\lambda(q\otimes q)=\frac3{200}.
}
\tag{2.3}
\]

No se afirma monotonía en `N`, reconstrucción geométrica ni resultado fuera de
S1.

## 3. Ataque A — Bombelli: atribución y expansión infinitesimal

### Pregunta

¿Es correcta nuestra identificación del objeto de Bombelli con el precursor
directo del pullback Fisher, y le estamos concediendo suficiente prioridad?

Bombelli define para cada `N` el vector de probabilidades

\[
G\mapsto\{P^{(N)}(C\mid G)\}_{C\in\mathcal P_N}
\tag{3.1}
\]

y usa la distancia de Wootters

\[
d_N(G,G')=\frac2\pi\arccos
\sum_C\sqrt{P^{(N)}(C\mid G)P^{(N)}(C\mid G')}.
\tag{3.2}
\]

Para una familia regular `p_C(epsilon)`, usamos

\[
\sum_C\sqrt{p_C(0)p_C(\varepsilon)}
=1-\frac{\varepsilon^2}{8}
\sum_C\frac{p_C'(0)^2}{p_C(0)}+o(\varepsilon^2).
\tag{3.3}
\]

De aquí concluimos que la forma cuadrática local es Fisher, salvo la
normalización global de `d_N`.

### El ataque tiene éxito si

- (3.3) no corresponde al objeto de Bombelli bajo sus convenciones;
- una hipótesis de soporte/regularidad falla en nuestro modelo;
- Bombelli ya calcula el diferencial, su rango/kernel o algo equivalente;
- el lenguaje “building on Bombelli” sigue atribuyéndonos demasiado.

### Material mínimo

- Bombelli 2000: [arXiv:gr-qc/0002053](https://arxiv.org/abs/gr-qc/0002053).
- Derivación y deflación interna:
  `wp6_finite_causal_order_fisher_spectrum_priority_audit.md`, §§3--4.

## 4. Ataque B — Surya: posible equivalencia oculta

### Pregunta

¿Algún resultado de Surya, o alguna referencia que ella use, implica ya —quizá
con otro lenguaje— una misma perturbación `v` tal que

\[
I_N^{[P]}(v)=0<I_{N+1}^{[P]}(v)
\tag{4.1}
\]

para la **ley completa** de posets?

Nuestra lectura es que Surya usa abundancias esperadas de intervalos como una
compresión, define distancias `L^r` entre esos espectros y muestra que algunas
degeneraciones se levantan al aumentar `N`. Esto precede la narrativa genérica
“más `N`, más resolución”, pero no (4.1) como afirmación tangente/Fisher sobre
la ley completa.

### El ataque tiene éxito si

- su espectro de intervalos es suficiente para la ley completa en el caso
  pertinente;
- una degeneración levantada en su trabajo equivale realmente al kernel de
  nuestro diferencial;
- sus referencias contienen el diferencial, un witness `N -> N+1` o un
  cociente de información equivalente;
- nuestra distinción “compresión versus ley completa” es artificial.

### Material mínimo

- Surya 2025/2026:
  [arXiv:2510.19403](https://arxiv.org/abs/2510.19403).
- Cribado de citantes:
  `wp6_bombelli_citation_chain_adversarial_audit.md`, §§4--5.

## 5. Ataque C — WP6: rederivación matemática independiente

### Pregunta

¿Son correctos el rango `1 -> 3`, el witness `1/4800` y los tres autovalores
generalizados, y corresponden a la forma Fisher afirmada?

Pedimos una rederivación, no sólo una lectura de consistencia. Los puntos que
deben comprobarse independientemente son:

1. la identidad de derivada para cada permutación de tres elementos;
2. el cociente correcto de las seis permutaciones en cinco clases de poset;
3. las probabilidades nulas `(1/6,1/6,1/6,1/3,1/6)`;
4. la tabla de derivadas en la base
   `(x tensor x, q tensor q, x tensor q+q tensor x)`;
5. que esos representantes agotan el rango sobre `Ran P`, no sólo la
   restricción a un subespacio elegido;
6. la anulación del sector mixto antisimétrico;
7. las matrices

\[
G_{[P]}^{(3)}=
\operatorname{diag}\left(\frac1{32},\frac1{180000},\frac1{1200}\right),
\quad
G_{\mathrm{full}}^{(3)}=
\operatorname{diag}\left(\frac1{12},\frac1{2700},\frac1{90}\right);
\tag{5.1}
\]

8. el factor de normalización del score geométrico `h_psi=2 P psi` y del
   experimento iid continuo.

### El ataque tiene éxito si

cualquier igualdad exacta es falsa, si el push-forward usa clases equivocadas,
si el rango tres sólo vale en el span ensayado, si el witness contiene una
componente no admisible o si el denominador Fisher de referencia no es el
experimento que el texto declara.

### Material mínimo

- Cálculo `N=2`: `wp6_d2_geometric_tangent_classification.md`, §13.
- Cálculo `N=3`: el mismo documento, §14; en particular (14.3), (14.7),
  (14.10) y (14.12)--(14.16).
- Contexto del bridge geométrico a cópula: §§3, 9--11 del mismo documento.

## 6. Techo de reivindicación congelado

```text
FRAMEWORK_NOVELTY = NO
MORE_N_MORE_RESOLUTION_NOVELTY = NO
EXACT_FINITE_N_FISHER_TANGENT_CLASSIFICATION = POTENTIALLY_NOVEL
NOVELTY_CERTIFICATE = NO
N4 = HOLD
```

Título de trabajo permitido, no definitivo:

> **Finite-order Fisher visibility of geometric perturbations in a causal-set
> model**

Bombelli debe aparecer como antecedente del marco. Surya debe aparecer como el
vecino de resolución mediante espectros de abundancias de intervalos.

## 7. Formulario de respuesta

Para cada ataque, marque una opción y añada la evidencia mínima:

```text
ATTACK_A_BOMBELLI = PASS / FAIL / INCONCLUSIVE
Reason:
Primary-source locator or correction:

ATTACK_B_SURYA = PASS / FAIL / INCONCLUSIVE
Reason:
Primary-source locator or correction:

ATTACK_C_WP6_MATHEMATICS = PASS / FAIL / INCONCLUSIVE
Reason:
First equation or step that fails, if any:
Independent derivation attached: YES / NO

PRIOR_ART_FOUND = YES / NO / UNCERTAIN
Citation and exact overlap:

RECOMMENDED_CLAIM = KEEP / NARROW / WITHDRAW / INCONCLUSIVE
Recommended wording:
```

`PASS` significa únicamente que el ataque concreto no encontró un fallo. No
significa certificado de novedad, corrección global del proyecto ni aval para
abrir `N=4`.

## 8. Regla de decisión posterior

- Cualquier `FAIL` bloquea una nota hasta corregir o retirar el claim afectado.
- Cualquier `INCONCLUSIVE` conserva `NOVELTY_CERTIFICATE = NO` y `N4 = HOLD`.
- Tres `PASS` permiten **evaluar** una nota corta `N=2,3`; no obligan a
  escribirla ni certifican prioridad absoluta.
- `N=4` sólo se reconsidera mediante una decisión posterior separada.

Este paquete está preparado para revisión, pero `NOT_SENT`: cualquier envío o
contacto externo requiere una acción explícita posterior del responsable del
proyecto.
