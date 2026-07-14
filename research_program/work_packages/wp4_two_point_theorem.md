# Nota técnica WP4/WP5 — Teorema de dos puntos para indeterminación order-only

> **Documento de trabajo REVISABLE, no congelado.** Esta nota da forma precisa y demostración al
> "teorema candidato" de indeterminación order-only (formalización del principio de
> identificabilidad de `research_program/models/canonical_counterexamples.md` §3, con el criterio
> WP3b). El núcleo matemático queda **PROBADO**; el contenido físico (la existencia de la pareja
> adversarial) queda explícitamente **ABIERTO**. Sin claim empírico, sin simulaciones, sin uso del
> estimador sellado, sin datos PR004. Síntesis transversal (módulo `\omega_\rho`, regímenes A/B/C,
> gobernanza PR010): `research_program/synthesis/geometric_indeterminacy_decision.md`.

## 0. Veredicto sobre el teorema candidato

El enunciado candidato mezcla tres afirmaciones de estatus distinto. Tras precisarlas:

- **(a) Cláusula de completaciones (`E_n`).** Con "plausible" = probabilidad positiva, es un
  teorema elemental y de hecho vale como **caracterización exacta** (si y solo si) de la
  identificabilidad con error cero. → **Teorema 1, PROBADO.**
- **(b) Cláusula estadística (`P_n(theta) ≈ P_n(theta')`).** Con "≈" = distancia en variación
  total y "fiable" = probabilidad de error acotada, es el **lema de dos puntos de Le Cam**,
  transportado al canal order-only sobre posets finitos. → **Teorema 2, PROBADO** (resultado
  estándar en estadística; la aportación aquí es solo la formalización en el marco causal-set).
- **(c) Cláusula de horizonte.** Es un corolario **condicional**: *si* existe la pareja
  `(theta_H, theta_notH)` con leyes próximas, *entonces* la existencia de horizonte no es
  identificable a ese `n`. → **Corolario 3, PROBADO como condicional.** La existencia de esa
  pareja **no está probada** y es exactamente el paso 1 del programa de instanciación
  (`canonical_counterexamples.md` §10). Esta nota no establece por sí misma ninguna
  indeterminación física.

## 1. Marco y definiciones

- `Omega_n`: el conjunto de clases de isomorfismo de posets finitos de `n` elementos. Es un
  conjunto **finito**, de modo que toda ley es una función de masa y no hay cuestiones de
  medibilidad.
- **Ley del modelo.** Para cada `theta in Theta`, `P_n(theta)` es una medida de probabilidad sobre
  `Omega_n`, con masa `p_theta(c)` para `c in Omega_n`. `Theta` puede contener completaciones
  geométricas o no geométricas (WP3 §2); nada en esta nota usa su estructura interna.
- **Estimador order-only.** Cualquier función `f : Omega_n -> T_space` (determinista; el caso
  aleatorizado se trata en la Observación 5.1). Que el dominio sean clases de isomorfismo captura
  exactamente el canal order-only: `f` no tiene acceso a etiquetas, coordenadas ni embedding.
- **Target.** `T : Theta -> T_space`, un funcional cualquiera (existencia de horizonte,
  localización, etiqueta singularidad/frontera, etc.).
- **Clase de completaciones compatibles (versión soporte).** Para `c in Omega_n`:

  `E_n(c) := { theta in Theta : p_theta(c) > 0 }`.

  Esta es la precisión "posibilista" de "plausible". La precisión estadística de "≈" es:
- **Variación total.** `TV(P,Q) := sup_{A ⊆ Omega_n} |P(A) − Q(A)| = (1/2) * sum_c |p(c) − q(c)|`.

Dos nociones de identificabilidad, que el teorema candidato usa sin distinguir y que hay que
separar:

- **Identificabilidad exacta sobre `Theta_0 ⊆ Theta`:** existe `f` tal que
  `P_theta( f(C_n) != T(theta) ) = 0` para todo `theta in Theta_0`.
- **Identificabilidad `epsilon`-fiable sobre `Theta_0`:** existe `f` tal que
  `P_theta( f(C_n) != T(theta) ) <= epsilon` para todo `theta in Theta_0`.

## 2. Teorema 1 (caracterización exacta — cláusula `E_n` del candidato)

**Teorema 1.** `T` es exactamente identificable sobre `Theta_0` **si y solo si** para todo
`c in Omega_n`, `T` es constante sobre `E_n(c) ∩ Theta_0`.

**Demostración.**

(*Necesidad.*) Sea `f` con error cero sobre `Theta_0`. Sean `theta, theta' in E_n(c) ∩ Theta_0`
para algún `c`. Error cero bajo `theta` exige `f(c') = T(theta)` para todo `c'` con
`p_theta(c') > 0`; en particular `f(c) = T(theta)`, porque `p_theta(c) > 0`. Análogamente
`f(c) = T(theta')`. Luego `T(theta) = T(theta')`.

(*Suficiencia.*) Supóngase `T` constante sobre cada `E_n(c) ∩ Theta_0`. Defínase `f(c)` como ese
valor común cuando `E_n(c) ∩ Theta_0 != ∅` (y arbitrario en otro caso); está bien definida por la
hipótesis de constancia. Para todo `theta in Theta_0` y todo `c` con `p_theta(c) > 0` se tiene
`theta in E_n(c) ∩ Theta_0`, luego `f(c) = T(theta)`. Por tanto
`P_theta( f(C_n) != T(theta) ) = 0`. ∎

Esto prueba (y refuerza a "si y solo si") la primera cláusula del candidato: la constancia de `T`
sobre las completaciones compatibles no es solo necesaria, es también suficiente **para la noción
de error cero**. Para la noción fiable (`epsilon > 0`) la versión soporte es demasiado débil (un
solape de probabilidad ínfima ya rompe la constancia sin impedir inferencia fiable); ahí el
instrumento correcto es el Teorema 2.

## 3. Teorema 2 (cota de dos puntos — cláusula `≈` del candidato)

**Teorema 2.** Sean `theta, theta' in Theta` con `T(theta) != T(theta')`. Entonces para **todo**
estimador order-only `f`:

`P_theta( f(C_n) != T(theta) ) + P_theta'( f(C_n) != T(theta') ) >= 1 − TV( P_n(theta), P_n(theta') )`.

Además la cota es **exacta**: existe `f` que la alcanza con igualdad.

**Demostración.**

(*Cota.*) Sea `A := { c in Omega_n : f(c) = T(theta) }`. Entonces:

- `P_theta( f != T(theta) ) = 1 − P_n(theta)(A)`.
- Sobre `A` se tiene `f = T(theta) != T(theta')`, luego `{ f = T(theta') } ⊆ A^c`, y por tanto
  `P_theta'( f != T(theta') ) >= P_n(theta')(A)`.

Sumando:

`suma de errores >= 1 − P_n(theta)(A) + P_n(theta')(A) = 1 − [ P_n(theta)(A) − P_n(theta')(A) ] >= 1 − TV`,

usando en el último paso la definición de `TV` como supremo sobre eventos. ∎

(*Exactitud.*) Tómese el test de razón de verosimilitud
`f*(c) := T(theta)` si `p_theta(c) >= p_theta'(c)`, y `f*(c) := T(theta')` en caso contrario.
Su suma de errores es

`1 − sum_c ( p_theta(c) − p_theta'(c) )_+ = 1 − TV`,

por la identidad estándar `TV = sum_c (p − q)_+` en espacios finitos. ∎

**Consecuencias inmediatas.**

1. `max` de los dos errores `>= (1 − TV)/2`: si `TV -> 0`, algún error tiende al menos a `1/2`,
   es decir, no mejor que adivinar.
2. Si `TV( P_n(theta), P_n(theta') ) < 1 − 2*epsilon`, entonces **ningún** estimador order-only es
   `epsilon`-fiable sobre ningún `Theta_0` que contenga a ambos. La desigualdad debe ser
   **estricta**: con `TV = 1 − 2*epsilon` un test equilibrado puede tener error exactamente
   `epsilon` bajo ambos modelos y ser por tanto `epsilon`-fiable según la definición de §1. Esta es
   la forma cuantitativa exacta de "ningún estimador order-only puede identificar `T` de forma
   fiable a ese `n`".
3. La cuantificación es sobre *todas* las funciones del orden observado, no sobre una clase de
   pipelines: es evidencia de nivel intrínseco (taxonomía §3.3/§4.3), condicionada a exhibir la
   pareja.

## 4. Corolario 3 (existencia de horizonte — cláusula final del candidato)

**Corolario 3.** Sea `T_space = {0,1}` y `T(theta) = 1` si y solo si `theta` contiene estructura
tipo horizonte. Si existen `theta_H` (Familia A) y `theta_notH` (Familia B) con

`TV( P_n(theta_H), P_n(theta_notH) ) <= 1 − 2*epsilon`,

entonces todo estimador order-only de existencia de horizonte tiene error `>= epsilon` bajo al
menos una de las dos completaciones a ese `n`. En particular, si la `TV` es pequeña, la existencia
de horizonte **no es identificable desde un único causal set finito order-only a ese `n`**.

**Demostración.** Instancia directa del Teorema 2 con ese `T` binario. ∎

**Lo que el corolario NO dice:** no afirma que tal pareja exista. Exhibirla — con la `TV` acotada
de verdad, a un `n` físicamente relevante — es el problema abierto central (§6).

## 5. Observaciones

### 5.1 Estimadores aleatorizados

Si `f` usa aleatoriedad auxiliar `U` independiente de `C_n`, ambos teoremas se conservan: para
cada valor `u` fijo el argumento determinista da la cota, y promediar sobre `u` la preserva.

### 5.2 Fuga por cardinalidad

Aquí ambas leyes viven sobre `Omega_n` con el **mismo** `n`, de modo que la cardinalidad no
discrimina. Pero en mecanismos generativos reales (sprinkling de Poisson) `N` es aleatorio, con
ley `Poisson(rho * V(theta))`: si `V(theta) != V(theta')`, la sola cardinalidad ya separa las
leyes completas. Consecuencia práctica para la instanciación: toda pareja adversarial debe
**emparejar la ley de `N`** (mismo volumen efectivo / misma intensidad) o formularse condicionada
a `N = n`. Esto conecta con la disciplina de canales de WP3 §2: la distinción order-only vs
order+cardinality se vuelve activa exactamente cuando las leyes de `N` difieren.

### 5.3 Certificación de "≈" por KL o Hellinger

La `TV` de leyes de sprinkling sobre posets no etiquetados es difícil de calcular directamente.
Cotas estándar permiten certificarla por divergencias más manejables (convención
`H^2(P,Q) := sum_c ( sqrt(p) − sqrt(q) )^2 in [0,2]`):

- Pinsker: `TV <= sqrt( KL(P||Q) / 2 )`;
- Le Cam: `H^2/2 <= TV <= H * sqrt( 1 − H^2/4 )`.

Ambas son de libro de texto (véase §7); basta acotar `KL` o `H^2` para activar el Teorema 2.

### 5.4 Ensemble vs single-instance (tensorización)

Con `m` muestras independientes, el coeficiente de Bhattacharyya `rho := 1 − H^2/2` tensoriza:
`rho( P^{⊗m}, Q^{⊗m} ) = rho(P,Q)^m`, luego `H^2_m = 2 (1 − rho^m) -> 2` siempre que `H > 0`, y
la `TV` del producto tiende a 1. Es decir: **una pareja con `TV` pequeña pero no nula a `m = 1` es
no identificable single-instance y a la vez identificable en ensemble**. Esto convierte el
mecanismo de la plantilla §5.4 de `canonical_counterexamples.md` (ambigüedad single-instance pese
a separación de ensemble) en un hecho a nivel de teorema — condicionado, de nuevo, a exhibir la
pareja geométrica. Distinto de ambos regímenes es el **asintótico en `n`** (densidad creciente):
esta nota trabaja a `n` fijo; la distinguibilidad asintótica al crecer `n` requeriría una
*secuencia* de parejas de modelos y herramientas como contigüidad (taxonomía §6, WP3b §5.2), y no
se prueba aquí.

## 6. Lo que esta nota establece y lo que deja abierto

**Establecido (evidencia tier 1, teorema/prueba, WP3b §7):**

- el criterio de identificabilidad de `canonical_counterexamples.md` §3 sube de "principio" a
  proposición demostrada, en sus dos versiones (exacta: Teorema 1; fiable: Teorema 2);
- la cota es exacta y cuantifica sobre todos los estimadores order-only, no sobre una clase;
- el mecanismo ensemble/single-instance (Obs. 5.4) queda probado como matemática condicional.

**Abierto (el contenido físico entero):**

1. La existencia de una pareja concreta `(theta_H, theta_notH)` — o de la pareja de localización
   fina `(theta_0, theta_1)` con desplazamiento `O(ell)` — con `TV` (o `KL`, `H^2`) acotada
   pequeña a `n` finito relevante. Es el paso 1-4 de `canonical_counterexamples.md` §10.
2. Cualquier técnica para acotar esas distancias sobre marginales de posets no etiquetados
   inducidos por sprinklings. Sin eso, el Teorema 2 es un arma sin munición.
3. Honestidad de prioridad: el núcleo matemático es estadística estándar (dos puntos de Le Cam);
   la aportación de esta nota es únicamente su transporte cuidadoso al canal order-only sobre
   causal sets finitos y su encaje en el programa (canales WP3, targets §4, plantillas §5).

Ninguna consecuencia de gobernanza para PR004 (§6 de `canonical_counterexamples.md`) se activa con
esta nota: el antecedente del Corolario 3 no está exhibido.

## 7. Referencias estándar

- L. Le Cam, *Convergence of Estimates Under Dimensionality Restrictions*, Ann. Statist. 1 (1973)
  — lema de dos puntos. `[estándar, no verificado contra biblioteca/ local]`
- A. B. Tsybakov, *Introduction to Nonparametric Estimation*, Springer (2009), §2.4 y Lemma 2.3 —
  desigualdades TV/Hellinger/KL y método de dos puntos. `[estándar, no verificado contra
  biblioteca/ local]`
