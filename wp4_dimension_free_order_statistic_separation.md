# Nota técnica WP4 — separación `fixed_n` dimension-free por patrones de orden

> **STATUS: INTERNAL_PROOF_AUDITED / EXPLORATORY_GENERALIZATION / COMMIT_READY_DOC_ONLY /
> NO_NOVELTY_CLAIM / NO_MANUSCRIPT_CHANGE / NO_CODE / NO_SIMULATION.**
>
> Esta nota extrae la capa estadística abstracta que ya aparece, para pares comparables, en
> `research_program/work_packages/wp4_comparable_pair_separation.md` y en el Teorema 3.9 de
> `docs/manuscript_limits_draft.md`. La nueva formulación no
> prueba que una geometría concreta en dimensión superior cambie ninguna frecuencia de orden:
> prueba únicamente que **si** existe un patrón finito cuya probabilidad cambia, **entonces** las
> leyes `fixed_n` de los posets no etiquetados se separan en variación total cuando `n -> infinity`.
> El caso geométrico \(1+1\) cerrado por el Corolario C6 del Anexo C suministra un antecedente
> explícito con \(m=2\).

## 0. Pregunta exacta y respuesta

**Pregunta.** ¿Qué parte del mecanismo
\[
\text{hueco en la fracción de pares comparables}
\quad\Longrightarrow\quad
\operatorname{TV}(Q_\theta^n,Q_{\theta'}^n)\longrightarrow1
\]
depende de la dimensión del espacio-tiempo?

**Respuesta.** Ninguna parte estadística. El argumento solo necesita:

1. muestreo i.i.d. condicionado a \(N=n\);
2. que el dato observado sea el poset no etiquetado completo;
3. un patrón de orden de tamaño fijo \(m\) cuya probabilidad difiera entre los dos modelos.

La dimensión, la métrica y la forma de los conos causales intervienen únicamente al demostrar el
antecedente geométrico: que tal diferencia de probabilidades existe. La fracción de pares
comparables es el caso \(m=2\), pero el resultado vale para cualquier patrón finito.

## 1. Marco

Sea \(\Theta\) una familia de modelos. Para cada \(\theta\in\Theta\), sean
\(X_1,X_2,\ldots\) puntos i.i.d. en un espacio de probabilidad que puede depender de \(\theta\).
Una regla causal medible induce, casi seguramente, un poset sobre cada muestra finita. Se exige
que los mapas muestra-a-poset sean equivariantes bajo permutaciones de los índices y
proyectivamente consistentes: para todo \(n\ge m\) y todo
\(I=\{i_1<\cdots<i_m\}\subseteq[n]\), el poset
\(\widetilde C_{\theta,n}|_I\), reetiquetado mediante \(j\mapsto i_j\), coincide casi seguramente
con el resultado de aplicar la misma regla a
\((X_{i_1},\ldots,X_{i_m})\). En particular,
\[
[\widetilde C_{\theta,n}|_I]\sim Q_\theta^m,
\]
donde \(Q_\theta^m\) se define a continuación, y la restricción es una función medible únicamente
de \((X_i)_{i\in I}\).

Por tanto, subposets soportados por conjuntos de índices disjuntos son independientes y todos los
subposets inducidos sobre \(m\) índices tienen la misma ley \(Q_\theta^m\). Estas hipótesis se
satisfacen al condicionar una aspersión de Poisson a \(N=n\): los \(n\) puntos son i.i.d. según el
volumen normalizado de la región, y una única relación causal sobre el espacio subyacente determina
de manera compatible todas las restricciones finitas.

Notación:

- \(\Omega_n\): conjunto finito de clases de isomorfismo de posets de \(n\) elementos;
- \(\widetilde C_{\theta,n}\): poset etiquetado inducido sobre los índices \([n]\);
- \(C_{\theta,n}:=[\widetilde C_{\theta,n}]\in\Omega_n\): su clase de isomorfismo, que es el
  dato no etiquetado observado;
- \(Q_\theta^n:=\mathcal L(C_{\theta,n})\);
- \(m\ge2\): tamaño fijo de patrón;
- \(A\subseteq\Omega_m\): cualquier clase o colección de clases de patrones;
- \(q_\theta(A):=Q_\theta^m(A)\): probabilidad de observar \(A\) en \(m\) puntos.

Para \(n\ge m\), defínase la frecuencia inducida
\[
T_{n,m,A}(C)
:=
\binom nm^{-1}
\sum_{\substack{I\subseteq[n]\\ |I|=m}}
\mathbf 1\{[\widetilde C|_I]\in A\},
\]
donde \(\widetilde C\) es cualquier representante etiquetado de \(C\). El valor no depende del
representante: una permutación de las etiquetas solo permuta los subconjuntos \(I\). Por tanto
\(T_{n,m,A}\) es un estadístico legítimo del **poset no etiquetado**.

## 2. Teorema general

### Teorema 1 (amplificación `fixed_n` por un patrón finito)

Bajo el marco de §1, fije \(m\ge2\), \(A\subseteq\Omega_m\) y
\(\theta,\theta'\in\Theta\). Ponga
\[
\Delta_{m,A}(\theta,\theta')
:=
\bigl|q_\theta(A)-q_{\theta'}(A)\bigr|,
\qquad
k_n:=\left\lfloor\frac{n}{m}\right\rfloor.
\]
Entonces, para todo \(n\ge m\),
\[
\boxed{
\operatorname{TV}(Q_\theta^n,Q_{\theta'}^n)
\ge
\left[
1-2\exp\!\left(
-\frac{k_n\,\Delta_{m,A}(\theta,\theta')^2}{2}
\right)
\right]_+ ,
}
\]
donde \([x]_+:=\max\{x,0\}\).

En particular, si \(\Delta_{m,A}(\theta,\theta')>0\) para un \(m\) fijo, entonces
\[
\operatorname{TV}(Q_\theta^n,Q_{\theta'}^n)\longrightarrow1
\qquad (n\to\infty).
\]

#### Demostración

**Paso 1: media de la frecuencia.** Por intercambiabilidad,
cada subposet inducido sobre \(m\) índices tiene ley \(Q_\theta^m\). Luego
\[
\mathbb E_\theta T_{n,m,A}=q_\theta(A).
\]

**Paso 2: concentración mediante bloques disjuntos.** Sea \(\Pi\) una permutación uniforme de
\([n]\), independiente de la muestra, y agrupe los primeros \(m k_n\) índices en los bloques
\[
B_{\Pi,j}
:=
\{\Pi((j-1)m+1),\ldots,\Pi(jm)\},
\qquad 1\le j\le k_n.
\]
Defina
\[
Z_\Pi
:=
\frac1{k_n}
\sum_{j=1}^{k_n}
\mathbf 1\{[\widetilde C_{\theta,n}|_{B_{\Pi,j}}]\in A\}.
\]
Condicionado al poset etiquetado, cada subconjunto de \(m\) índices tiene la misma probabilidad de
aparecer como uno de esos bloques. En concreto, para cada \(I\subseteq[n]\) con \(|I|=m\),
\[
\mathbb P_\Pi\{I=B_{\Pi,j}\text{ para algún }j\}
=
\frac{k_n}{\binom nm}.
\]
Al sustituir esta probabilidad en la suma y cancelar \(k_n\), se obtiene
\[
\mathbb E_\Pi[Z_\Pi\mid X_1,\ldots,X_n]=T_{n,m,A}.
\]

Para una permutación fija, los \(k_n\) sumandos de \(Z_\Pi\) dependen de bloques disjuntos de
puntos i.i.d.; son por ello independientes, toman valores en \([0,1]\) y tienen media
\(q_\theta(A)\). Si esos indicadores se denotan por \(Y_1,\ldots,Y_{k_n}\), el lema elemental de
Hoeffding aplicado a cada
\((\lambda/k_n)(Y_j-q_\theta(A))\), seguido del producto por independencia, da el factor
\(\exp(\lambda^2/(8k_n))\). Por tanto, para todo \(\lambda>0\), Jensen da
\[
\begin{aligned}
\mathbb E_\theta
\exp\{\lambda(T_{n,m,A}-q_\theta(A))\}
&\le
\mathbb E_{\theta,\Pi}
\exp\{\lambda(Z_\Pi-q_\theta(A))\}\\
&\le
\exp\!\left(\frac{\lambda^2}{8k_n}\right).
\end{aligned}
\]
La cota de Chernoff, optimizada en \(\lambda=4k_nt\), produce
\[
\mathbb P_\theta\!\left(
T_{n,m,A}-q_\theta(A)\ge t
\right)
\le e^{-2k_nt^2}.
\]
Aplicada a \(-T_{n,m,A}\), da la misma cota para la cola inferior.

**Paso 3: test a punto medio.** Suponga, sin pérdida de generalidad,
\(q_\theta(A)<q_{\theta'}(A)\), y decida \(\theta'\) cuando
\[
T_{n,m,A}>
\frac{q_\theta(A)+q_{\theta'}(A)}2.
\]
Bajo cada hipótesis, el error es una cola a distancia
\(\Delta_{m,A}(\theta,\theta')/2\) de su media. Así,
\[
\alpha_n+\beta_n
\le
2\exp\!\left(
-\frac{k_n\,\Delta_{m,A}(\theta,\theta')^2}{2}
\right).
\]
Para cualquier test entre dos leyes, \(1-\operatorname{TV}\) no excede su suma de errores.
Además, el test anterior usa solo \(T_{n,m,A}\), que es función de la clase de isomorfismo
observada. Se obtiene la cota encuadrada; truncarla en cero solo hace explícita la no negatividad
de la variación total. ∎

### Corolario 2 (cualquier diferencia finita se amplifica)

Si \(Q_\theta^m\ne Q_{\theta'}^m\) para algún \(m\) fijo, entonces
\[
\operatorname{TV}(Q_\theta^n,Q_{\theta'}^n)\longrightarrow1.
\]
Más precisamente, como \(\Omega_m\) es finito, existe un evento
\(A_*\subseteq\Omega_m\) que alcanza la variación total en tamaño \(m\):
\[
\Delta_{m,A_*}(\theta,\theta')
=
\operatorname{TV}(Q_\theta^m,Q_{\theta'}^m).
\]
El Teorema 1 da
\[
\operatorname{TV}(Q_\theta^n,Q_{\theta'}^n)
\ge
\left[
1-2\exp\!\left(
-\frac{\lfloor n/m\rfloor\,
\operatorname{TV}(Q_\theta^m,Q_{\theta'}^m)^2}{2}
\right)
\right]_+.
\]

Este corolario no construye el testigo \(m\). Dice que, una vez encontrada **cualquier**
diferencia en una ley de subposets de tamaño finito, la separación asintótica del poset completo
es automática.

## 3. Pares comparables: el caso \(m=2\)

Tómese \(m=2\) y sea \(A_{\rm chain}\subset\Omega_2\) la clase del orden total de dos elementos.
Entonces
\[
q_\theta(A_{\rm chain})
=
p(\theta)
:=
\mathbb P_\theta(X_1\text{ y }X_2\text{ son comparables}),
\]
y \(T_{n,2,A_{\rm chain}}=S_n/\binom n2\), donde \(S_n\) es el número de pares comparables.
El Teorema 1 se especializa a
\[
\boxed{
\operatorname{TV}(Q_\theta^n,Q_{\theta'}^n)
\ge
\left[
1-2\exp\!\left(
-\frac{\lfloor n/2\rfloor\,|p(\theta)-p(\theta')|^2}{2}
\right)
\right]_+ .
}
\]

Consecuencias:

1. **Par fijo.** Si \(p(\theta)\ne p(\theta')\), entonces
   \(\operatorname{TV}(Q_\theta^n,Q_{\theta'}^n)\to1\), con una cota exponencial en \(n\).
2. **Uniformidad separada.** Si una clase de pares satisface
   \(|p(\theta)-p(\theta')|\ge\gamma>0\), la cota de TV y el error de los tests bipuntuales
   correspondientes son uniformes sobre esa clase.
3. **Alternativas móviles.** Para sucesiones \(\theta_n,\theta_n'\), el mismo test es consistente
   siempre que
   \[
   \sqrt n\,|p(\theta_n)-p(\theta_n')|\longrightarrow\infty.
   \]
4. **Sin uniformidad automática.** La inyectividad de \(p\) por sí sola no da un único \(n_0\)
   sobre todos los pares distintos: el hueco puede tender a cero.

Esta cota ofrece decaimiento exponencial del error para un hueco fijo, frente al decaimiento
polinómico de la cota de Chebyshev del Teorema 3.9. Ambas prueban el mismo exponente de frontera
\(n^{-1/2}\) en el sentido \(o/\omega\). La nueva cota no resuelve la constante crítica cuando el
hueco es exactamente de orden \(n^{-1/2}\).

## 4. Corolario para regiones lorentzianas en dimensión arbitraria

Considérese una familia de regiones lorentzianas de volumen finito
\[
\{(D_\theta,g_\theta):\theta\in\Theta\}
\]
en cualquier dimensión espacio-temporal \(d\), con
\(0<\operatorname{Vol}_{g_\theta}(D_\theta)<\infty\), muestreo según el volumen normalizado y
condicionado a \(N=n\). Supóngase únicamente que la relación causal es medible y que induce un
poset casi seguramente. Sea
\[
\mu_\theta(B)
:=
\frac{\operatorname{Vol}_{g_\theta}(B)}
     {\operatorname{Vol}_{g_\theta}(D_\theta)}
\qquad (B\subseteq D_\theta\ \text{medible})
\]
la medida de probabilidad de muestreo, y defina
\[
p_d(\theta)
:=
\iint_{D_\theta\times D_\theta}
\mathbf 1\{x,y\text{ causalmente comparables en }g_\theta\}\,
d\mu_\theta(x)\,d\mu_\theta(y).
\]

### Corolario 3 (transferencia dimension-free por fracción de orden)

Para cualesquiera \(\theta,\theta'\) tales que
\(p_d(\theta)\ne p_d(\theta')\),
\[
\operatorname{TV}(Q_{\theta,d}^n,Q_{\theta',d}^n)
\longrightarrow1.
\]
La cota explícita es la de §3 con \(p\) sustituido por \(p_d\).

Si, sobre un espacio paramétrico métrico, se prueba además un módulo inferior
\[
\lvert p_d(\theta)-p_d(\theta')\rvert
\ge
\omega\!\left(d_\Theta(\theta,\theta')\right),
\]
entonces la garantía de los tests bipuntuales es uniforme donde \(\omega\ge\gamma>0\), y esos
tests separan alternativas móviles siempre que
\[
\sqrt n\,
\omega\!\left(d_\Theta(\theta_n,\theta_n')\right)
\longrightarrow\infty.
\]
Aquí “uniforme” significa que la misma **cota de error** vale para todos los pares del conjunto;
el punto medio y, por tanto, el test simple-vs-simple pueden depender del par. No se construye un
único test para una hipótesis compuesta.

**Contenido exacto.** Este corolario ya es válido en \(2+1\), \(3+1\) y dimensión general porque
su prueba no usa \(d\). Lo que **no** está probado es que una familia superior concreta cumpla
\(p_d(\theta)\ne p_d(\theta')\), ni mucho menos una cota inferior uniforme. Esa es la carga
geométrica nueva: recalcular o controlar la fracción de orden con los conos causales de la
dimensión correspondiente.

Si \(p_d\) resulta ciega, el Corolario 2 conserva una segunda vía: basta encontrar algún
\(m>2\) y algún patrón \(A\subseteq\Omega_m\) cuya probabilidad cambie.

## 5. Recuperación y fortalecimiento del Corolario C6 del Anexo C

En la familia diamante \(1+1\) de
`research_program/work_packages/wp4_comparable_pair_separation.md`, el Corolario C6 prueba que existe
\(dv_0=dv_0(r_p,r_q,\tau_0,\tau_1)>0\) tal que, para todo
\(0<dv<dv_0\) fijo y todos \(\tau,\tau'\in K=[\tau_0,\tau_1]\),
\[
|p(\tau)-p(\tau')|
\ge
\frac{\kappa(r_p,r_q)\,dv}{2}\,|\tau-\tau'|.
\]
El Teorema 1 da entonces
\[
\boxed{
\operatorname{TV}(Q_\tau^n,Q_{\tau'}^n)
\ge
\left[
1-2\exp\!\left(
-\frac{\lfloor n/2\rfloor\,
\kappa(r_p,r_q)^2\,dv^2\,|\tau-\tau'|^2}{8}
\right)
\right]_+ .
}
\]

Por tanto:

- para cada par fijo \(\tau\ne\tau'\), la TV converge a uno;
- bajo \(|\tau-\tau'|\ge\eta>0\), la convergencia es uniforme;
- para alternativas móviles, basta
  \(\sqrt n\,|\tau_n-\tau_n'|\to\infty\);
- el mismo \(dv_0\) del Corolario C6 sirve: esta nota no modifica ni evalúa numéricamente ese
  umbral.

Esta sección **no reemplaza** la parte geométrica del Corolario C6. La usa como antecedente y mejora
únicamente la cota estadística de Chebyshev a una cota exponencial estándar de U-estadísticos.

## 6. Libro de cuantificadores

1. \(m\) y el evento \(A\) se fijan antes de hacer \(n\to\infty\).
2. En el Corolario 2, el evento maximizador \(A_*\) puede depender de
   \((\theta,\theta')\); no se afirma que exista un único patrón testigo para toda \(\Theta\).
3. Para cada par fijo con \(\Delta_{m,A}>0\), la TV converge a uno.
4. No existe uniformidad sobre pares cuyo hueco \(\Delta_{m,A}\) pueda aproximarse a cero.
5. La uniformidad se recupera imponiendo \(\Delta_{m,A}\ge\gamma>0\), o mediante un módulo
   inferior cuantitativo.
   Esto uniformiza la garantía bipuntual, no produce un único test para una hipótesis compuesta.
6. En el Corolario C6, \(dv_0\) es uniforme sobre \(K\), pero \(dv\) queda fijo al hacer
   \(n\to\infty\).
7. Toda la nota trabaja en el canal condicionado `fixed_n`. No afirma nada sobre el canal Poisson
   no condicionado, donde el marginal de \(N\) puede separar por volumen.
8. La dimensión \(d\) es arbitraria en el teorema condicional; la verificación del antecedente
   geométrico sigue siendo específica de cada familia y dimensión.

## 7. Alcance, novedad y criterio de cierre

**Lo probado en esta nota, tras revisión adversarial interna:**

- un teorema abstracto sobre leyes de posets no etiquetados inducidas por muestras i.i.d.;
- una cota explícita exponencial a partir de cualquier diferencia de patrón finito;
- el teorema dimension-free de pares comparables como caso \(m=2\);
- el fortalecimiento cuantitativo de la conclusión estadística del Corolario C6.

**Comprobación de consistencia con la ceguera de escala.** En la órbita de dilatación del
Teorema 3.1 se tiene \(Q_\theta^m=Q_{\theta'}^m\) para todo \(m\). Por tanto
\(\Delta_{m,A}=0\) para todo patrón y el antecedente del Teorema 1 no se activa. El nuevo resultado
no contradice la TV exactamente nula de esa órbita: distingue solo grados de libertad que cambian
alguna ley de orden finita.

**Lo no probado:**

- que \(p_d(\theta)\) sea inyectiva, monótona o siquiera no constante en una familia concreta de
  dimensión \(2+1\) o \(3+1\);
- reconstrucción de métrica, horizonte, localización o parámetro a partir del poset;
- separación en el canal no condicionado;
- constante óptima a escala crítica \(n^{-1/2}\);
- prioridad o novedad frente a la literatura de U-estadísticos, estructuras intercambiables,
  límites de posets o modelos geométricos latentes.

La concentración usada es matemática estándar; no se reclama novedad por Hoeffding ni por el
test a punto medio. El valor potencial de la nota es estructural: separa con precisión una capa
estadística completamente general de la carga geométrica específica de dimensión.

**Cierre de auditoría interna (2026-07-30):**

1. **PASS — identidad de randomización.** Para cada bloque \(j\),
   \(B_{\Pi,j}\) es uniforme sobre los \(\binom nm\) subconjuntos de tamaño \(m\); por tanto
   \[
   \mathbb E_\Pi[Z_\Pi\mid X_1,\ldots,X_n]
   =
   \frac1{k_n}\sum_{j=1}^{k_n}
   \frac1{\binom nm}\sum_{|I|=m}
   \mathbf 1\{[\widetilde C_{\theta,n}|_I]\in A\}
   =
   T_{n,m,A}.
   \]
2. **PASS — constantes.** El lema exponencial de Hoeffding da
   \(\exp(\lambda^2/(8k_n))\); Chernoff se optimiza en \(\lambda=4k_nt\) y produce
   \(e^{-2k_nt^2}\). Con \(t=\Delta_{m,A}/2\), la suma de errores queda acotada por
   \(2e^{-k_n\Delta_{m,A}^2/2}\).
3. **PASS — dato no etiquetado.** Todo isomorfismo permuta biyectivamente los subconjuntos de
   tamaño \(m\) y preserva el tipo de cada subposet inducido; por ello \(T_{n,m,A}\) depende solo
   de la clase de isomorfismo.
4. **PASS — compatibilidad con el Anexo C.** El \(dv_0\) sigue siendo el mismo umbral uniforme
   sobre \(K\), \(dv\) queda fijo cuando \(n\to\infty\), y no se añade ninguna conclusión
   geométrica, Poisson, reconstructiva o de dimensión superior.
5. **SEPARATE_GATE — prioridad.** La auditoría bibliográfica sigue siendo obligatoria antes de
   cualquier claim de novedad. No condiciona la corrección matemática de esta nota y no se
   satisface mediante la referencia estándar de §8.

El cierre anterior elimina los bloqueos matemáticos internos detectados y deja la nota preparada
para un eventual commit documental separado. No autoriza por sí mismo ese commit, un cambio en el
manuscrito ni lenguaje de prioridad.

## 8. Fuente estándar consultada

- W. Hoeffding, “Probability Inequalities for Sums of Bounded Random Variables,”
  *Journal of the American Statistical Association* **58** (1963), 13–30, §4a,
  especialmente ecuaciones (4.4)–(4.7),
  [doi:10.1080/01621459.1963.10500830](https://doi.org/10.1080/01621459.1963.10500830).
  Es la fuente primaria de la desigualdad clásica para U-estadísticos acotados. La demostración
  necesaria está reproducida en §2 para que la cota y sus constantes puedan auditarse sin
  depender de una referencia externa. Esta cita no constituye una auditoría de prioridad del
  teorema de transferencia a leyes de posets.
