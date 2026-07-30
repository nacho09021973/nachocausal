# Fase 3 B2 — revisión acotada de las cinco condiciones de la Decisión 048

> **STATUS: BOUNDED_CONDITIONS_REVIEW / WORK_DATE_2026-07-29 / NOT_A_COMITE_ACTA /
> DOES_NOT_MODIFY_DECISION_048 / DOES_NOT_MODIFY_PREOPENING_CONTRACT / TARGET_NOT_ADOPTED /
> WITNESS_PAIR_NOT_CONSTRUCTED / NO_CODE / NO_SIMULATION / NO_SEEDS / PR_1_UNTOUCHED /
> COMITE_NOT_RECONVENED.**
>
> Este documento es una revisión de trabajo del chair, no un acta de `/comite`. Evalúa el estado de
> las cinco condiciones registradas en
> `docs/comite/comite_decision_048_q-fmots-target-adjudication.md` §9 ("Pendiente antes de poder
> re-adjudicar `ADOPT`"), en su redacción exacta y su orden de precedencia. No modifica la
> Decisión 048 ni `research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md`.
> No construye el par testigo, no escribe código, no ejecuta simulaciones ni reserva semillas. Las
> formulaciones matemáticas candidatas que aparecen abajo son eso — candidatas — y no quedan
> adoptadas normativamente por este documento.

## 0. Las cinco condiciones (texto exacto de la Decisión 048 §9)

1. Cerrar \(S_{\rm adm}(g,U)\) con una única definición intrínseca y verificada — o bien
   derivar/anclar a fuente primaria la ley de transformación conforme correcta de \(\theta_\pm\) y
   elegir **una** convención (no dos conflictivas), o adoptar explícitamente la forma libre de
   orientación ("trapped surface", \(\theta_+&lt;0\) y \(\theta_-&lt;0\)) como una **sustitución de
   target** reconocida como tal, con su propio recorrido de G1–G9.
2. Re-argumentar G8 específicamente contra el mecanismo del Teorema 2 de Müller (perturbación
   conforme sobre slab de Cauchy arbitrario), no contra el Teorema 3; declarar honestamente si B2
   sobrevive como instanciación acotada o si dispara `B2_REDUNDANT_WITH_MULLER`.
3. Pre-declarar la degradación de regularidad (\(\rho\to0\), amplitud \(O(1)\), curvatura
   \(\sim\sqrt n\)) explícitamente en el techo de reclamo (G4/G9), en vez de descubrirla después de
   construir un testigo.
4. No tratar G2 como cerrado hasta que \(S_{\rm adm}\) esté cerrado (es condicional, colapsa en
   G1).
5. Exhibir — o justificar explícitamente por qué se difiere — un ejemplo con \(Q=1\) y otro con
   \(Q=0\), siguiendo el propio estándar de no-vacuidad de la pista Lean del repositorio, antes de
   tratar la clase como utilizable.

Fuente primaria consultada esta sesión, además de lo ya citado en la Decisión 048: el PDF completo
de Müller leído íntegro (`pdftotext -layout biblioteca/2503.01719v2.pdf`, 7 páginas, texto
verificado línea por línea), y una búsqueda exhaustiva de "trap|horizon|MOTS|expansion|marginal"
sobre ese texto completo (cero coincidencias — ver condición 2). No se encontró en `biblioteca/`
ningún libro de texto o artículo de referencia sobre superficies atrapadas / MOTS más allá de
Eichhorn–Gamito–Stokes (que a su vez, en su propio montaje 1+1D, no puede computar \(\theta_\pm\)
directamente — `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal
sets.md:227`). Esto se registra explícitamente en cada condición donde es relevante.

---

## Condición 1 — Cerrar \(S_{\rm adm}(g,U)\) intrínsecamente

**Status: OPEN**

### Evidencia primaria

- El contrato mismo (`phase3_b2_witness_pair_preopening_contract.md:71-77`, §2.2) ya reconoce que
  \(S_{\rm adm}\) no puede ser "la superficie que nosotros marcamos" y exige una especificación
  difeomorfismo-invariante con orientación exterior y condiciones de borde cerradas.
- No existe en `biblioteca/` ninguna fuente primaria de geometría de superficies atrapadas /
  transformación conforme de expansiones nulas: se buscó explícitamente (`grep` sobre
  `biblioteca/derived-md/` y lista de PDFs en `biblioteca/`) y el único documento con contenido de
  MOTS es Eichhorn–Gamito–Stokes, que no calcula \(\theta_\pm\) en absoluto en su propio montaje
  (`…geodesic focusing….md:227`). Esto confirma lo que la Decisión 048 ya registraba: cualquier ley
  de transformación conforme de \(\theta_\pm\) permanece `[UNVERIFIED]` a nivel de fuente primaria
  local.

Esta sesión ataca cuatro preguntas por separado, tal como las planteó el PI: (a) uso exclusivo de
\((g,U)\), (b) cuantificadores cerrados, (c) invariancia por difeomorfismos, (d) respaldo primario.
Dos de ellas se cierran esta sesión con demostraciones completas y autocontenidas (no ancladas a
`biblioteca/`, pero verificables paso a paso dentro de este documento — lo cual, per la regla
fundacional del proyecto, es una forma legítima de respaldo verificable junto a la cita: "file:line,
comando, commit **o cita**"; una demostración reproducible es análoga a un comando cuya salida
cualquiera puede recomprobar). Las otras dos quedan genuinamente abiertas, y una de ellas resulta
más difícil de lo que la Decisión 048 sugería.

### Lema 1 (PROBADO) — la normalización de \(\ell_\pm\) es irrelevante: el signo de \(\theta\) es una propiedad del rayo nulo, no del representante

**Enunciado.** Sea \(S\) una superficie espacial de codimensión 2 y \(\ell\) un campo normal nulo
futuro a \(S\). Para cualquier función escalar suave \(f>0\) sobre \(S\), \(\theta_{f\ell} =
f\,\theta_\ell\) puntualmente (igualdad exacta, no aproximada).

**Demostración.** Por definición \(\theta_\ell = q^{ab}\nabla_a\ell_b\), donde \(q^{ab}\) es la
métrica inversa inducida en \(S\), extendida por cero en las direcciones normales (es la
convención estándar del proyector tangente a \(S\)). Entonces
\(\nabla_a(f\ell_b) = f\nabla_a\ell_b + \ell_b\nabla_a f\), y al contraer con \(q^{ab}\):
\(q^{ab}\nabla_a(f\ell_b) = f\,q^{ab}\nabla_a\ell_b + (q^{ab}\ell_b)\nabla_a f\). El segundo término
se anula **exactamente**, no solo a primer orden: \(q^{ab}\) proyecta sobre direcciones tangentes a
\(S\), mientras que \(\ell_b\) es puramente normal a \(S\) por definición (es un normal nulo), así
que \(q^{ab}\ell_b=0\) idénticamente. Queda \(\theta_{f\ell}=f\,\theta_\ell\). ∎

**Consecuencia inmediata:** para \(f>0\), \(\operatorname{sign}(\theta_{f\ell}) =
\operatorname{sign}(\theta_\ell)\) y \(\theta_{f\ell}=0 \iff \theta_\ell=0\). El signo y el
conjunto de anulación de la expansión son propiedades de la **dirección** nula (el rayo, no el
vector concreto), independientes de cómo se normalice \(\ell_\pm\). Esto es más fuerte que lo
registrado en la Decisión 048: allí se observó que las dos leyes de Wave 1
(\(\tilde\theta_\pm=e^{-\omega}(\cdots)\) vs. \(e^{-2\omega}(\cdots)\)) compartían el mismo término
entre paréntesis "por construcción"; aquí se prueba, desde la definición de \(\theta\), que **todo**
prefactor positivo es irrelevante, sin necesidad de comparar las dos fórmulas candidatas ni de
apelar a ninguna de ellas. La obligación del contrato §2.1
(`phase3_b2_witness_pair_preopening_contract.md:59-62`) de "no heredar la normalización
implícitamente" queda satisfecha de forma definitiva: \(Q_{\mathrm{FMOTS}}\) nunca depende de la
normalización, así que no hace falta "elegir una convención" en absoluto para esta parte del
problema. **Esto cierra por completo la sub-cuestión de normalización que la condición 1 planteaba
como una de sus dos rutas** ("derivar/anclar la ley de transformación conforme… y elegir una
convención, no dos conflictivas") — pero, como se ve abajo, esa no era la parte difícil del
problema.

### Lema 2 (PROBADO) — la clase de superficies candidatas y la expansión son covariantes por difeomorfismos

**Enunciado.** Sea \(\varphi:U\to U'\) un difeomorfismo y \(g'=\varphi_*g\). Si \(S\subset U\) es
suave, compacta, embebida, espacial y de codimensión 2, entonces \(\varphi(S)\subset U'\) tiene las
mismas cuatro propiedades respecto de \(g'\). Si \(\ell\) es un normal nulo futuro a \(S\) respecto
de \(g\), entonces \(\varphi_*\ell\) es un normal nulo futuro a \(\varphi(S)\) respecto de \(g'\), y
\(\theta_{\varphi_*\ell}^{g'}(\varphi(p)) = \theta_\ell^{g}(p)\) para todo \(p\in S\).

**Demostración (bosquejo).** "Suave", "compacta", "embebida" y "codimensión 2" son propiedades de
la topología diferencial de la inclusión \(S\hookrightarrow U\), preservadas por cualquier
difeomorfismo. "Espacial" es una propiedad del carácter causal del espacio tangente respecto de la
métrica, y el pushforward de una métrica preserva el carácter causal de cualquier vector por
construcción (\(g'(\varphi_*v,\varphi_*v)=g(v,v)\)). Igual para "nulo" y "futuro". La expansión
\(\theta_\ell=q^{ab}\nabla_a\ell_b\) se construye enteramente a partir de tensores naturales
(métrica inducida, conexión de Levi-Civita, segunda forma fundamental) que se transportan
covariantemente bajo pushforward; por naturalidad, \(\theta\) evaluada en el punto transportado
coincide con el valor original. ∎

**Consecuencia:** cualquiera de las formulaciones candidatas de \(S_{\rm adm}\) consideradas en esta
sección (la de "borde de región compacta" de la sesión anterior, o la "libre de orientación" de
abajo) es automáticamente difeomorfismo-invariante **como clase**, sin necesidad de verificarlo caso
por caso — es una consecuencia estructural de que sus condiciones definitorias (suave, compacta,
embebida, espacial, codimensión 2, y las nulas asociadas) son todas naturales. Esto cierra la
sub-cuestión de invariancia por difeomorfismos **en general**, para cualquier candidato que se
construya a partir de estas propiedades — lo que queda por decidir no es si la clase será
covariante, sino qué contenido adicional (más allá de estas propiedades naturales) hace falta para
fijar "exterior".

### Hallazgo (intento fallido, mantenido por su valor negativo) — una definición libre de orientación NO evita el problema, solo lo reubica

Dado el Lema 1, cabe preguntar si se puede evitar toda noción de "exterior" definiendo, de forma
totalmente simétrica:

\[
Q_{\mathrm{FMOTS}}^{\rm sym}(g,U) := \mathbf 1\Bigl\{\exists S\subset U\text{ (suave, compacta,
embebida, espacial, codim-2)},\ \exists\{i,j\}=\{1,2\}:\ \theta(\ell^{(i)}_S)\equiv0,\
\theta(\ell^{(j)}_S)&lt;0\Bigr\},
\]

donde \(\ell^{(1)},\ell^{(2)}\) son las dos direcciones nulas futuras normales a \(S\) (siempre
existen exactamente dos, sin elegir cuál es "exterior"). Por el Lema 1, esta expresión no depende
de cómo se normalicen \(\ell^{(1)},\ell^{(2)}\), y por el Lema 2 es automáticamente
difeomorfismo-invariante. **Parece cerrar la condición 1 de un plumazo, sin loncha, sin borde, sin
infinito.**

**Se comprobó que esto es incorrecto, y por qué importa:** esta definición simétrica no distingue
entre una superficie marginalmente-atrapada-exterior genuina (\(\theta_+=0,\theta_-&lt;0\) en la
convención estándar — el horizonte de Schwarzschild) y una superficie marginalmente-atrapada
"interior" con los papeles cambiados (\(\theta_-=0,\theta_+&lt;0\)) — una configuración distinta,
asociada en la literatura de relatividad a horizontes internos/de Cauchy, no al horizonte de
sucesos exterior que \(Q_{\mathrm{FMOTS}}\) pretende detectar. **Verificación en el caso de
referencia:** en Schwarzschild, \(\Theta_{\rm in}=-2/r\) (`biblioteca/derived-md/Towards black-hole
horizons and geodesic focusing in causal sets.md:221-225`) nunca se anula para \(r&gt;0\) finito, así
que sobre esferas redondas la definición simétrica coincide exactamente con la orientada — pero esto
es una coincidencia del caso de referencia esféricamente simétrico, no una prueba general. Para una
superficie no esférica, o para una \(S\) generada dentro de una protuberancia conforme pequeña
(el mecanismo que B2 necesitaría), no hay ninguna razón estructural para que \(\theta_-\) no pueda
anularse en vez de \(\theta_+\) — y la definición simétrica no podría distinguir ese caso de un
verdadero MOTS exterior.

**La razón de fondo, verificada aquí:** para fijar CUÁL de las dos direcciones nulas es "exterior"
exactamente en la superficie marginal misma (donde por definición una de las dos expansiones es
cero), hace falta información que no vive en \((g,S)\) puntualmente — típicamente, una familia
continua de superficies de comparación cercanas a \(S\) (una foliación local o transversal) respecto
de la cual una de las dos expansiones sea positiva justo "afuera" y la otra negativa justo "adentro"
en el sentido de esa familia. Esto es, estructuralmente, el mismo tipo de dato que la formulación
"borde de región compacta \(\Omega\) dentro de una loncha \(\Sigma\)" de la sesión anterior ya
proponía — **no es una alternativa más simple, es la misma necesidad estructural vista desde otro
ángulo.** Este es un resultado negativo genuino y verificado en esta sesión, no solo una sospecha:
**cualquier definición intrínseca correcta de "exterior" para una superficie marginal, en un parche
compacto sin infinito, necesita datos locales transversales a \(S\) (una loncha, una foliación, o
equivalente) — no puede depender solo de \((g,S)\) puntualmente.**

### Estado de la vía \(\Sigma,\Omega\) (borde de región compacta) tras este hallazgo — reformulación correcta del bloqueo

La formulación candidata de la sesión anterior —

\[
S_{\rm adm}(g,U) := \bigl\{\, S=\partial\Omega \mid \Sigma\subset U\text{ loncha espacial compacta
causalmente convexa},\ \Omega\Subset\Sigma\text{ región compacta con borde suave} \,\bigr\},
\]

con "exterior" = normal que apunta fuera de \(\Omega\) — sigue siendo la **única** vía candidata
identificada hasta ahora que provee correctamente el dato transversal necesario. La sesión anterior
había enmarcado el hueco pendiente como "orden de cuantificadores sobre \(\Sigma\)"; esa
formulación era imprecisa y esta sesión la corrige: **cambiar de loncha \(\Sigma\) a otra que
induzca la misma coorientación de \(S\) (el mismo lado llamado \(\Omega\)) solo reescala
positivamente \(\ell_\pm\)** — es un boost en el 2-plano normal a \(S\), y por el Lema 1 el signo y
la anulación de \(\theta_\pm\) son invariantes bajo cualquier reescalado positivo. **El único hueco
real es discreto, no continuo:** si dos presentaciones admisibles de la misma \(S\) —posiblemente
con \(\Sigma\) distintas, posiblemente con la misma \(\Sigma\)— pueden inducir coorientaciones
**opuestas** (\(\Omega\) vs. su complemento), la elección de "exterior" no queda fijada por
\((g,U)\) sola.

### Test falsificador — ¿puede la misma \(S\) (misma \(\Sigma\)) bordear dos regiones compactas de lados opuestos?

**Candidato de prueba:** \(\Sigma\cong S^3\) (loncha espacial compacta sin borde, topológicamente
una 3-esfera — realizable, p.ej., como la loncha espacial de un universo FRW cerrado o de Einstein
estático, \(ds^2=-dt^2+a(t)^2\bigl(d\chi^2+\sin^2\chi\,d\Omega_2^2\bigr)\), \(\chi\in[0,\pi]\)), y
\(S=\{\chi=\pi/2\}\) la 2-esfera ecuatorial. Se toma
\(U=[t_0-\varepsilon,t_0+\varepsilon]\times S^3\) (compacto, causalmente convexo para cualquier
\(\varepsilon\), pues \(t\) es una función temporal global monótona a lo largo de curvas causales
futuras — hecho estándar de FRW).

**Verificación explícita:**

1. \(\Omega_+:=\{\chi&lt;\pi/2\}\) y \(\Omega_-:=\{\chi&gt;\pi/2\}\) son ambas compactas (cada una
   \(\cong D^3\), un casquete cerrado de la 3-esfera), con \(\partial\Omega_+=\partial\Omega_-=S\).
   **\(S\) pertenece a la clase declarada bajo ambas presentaciones** — nada en la definición actual
   de \(S_{\rm adm}\) excluye lonchas con topología \(S^3\) ni exige que el complemento de \(S\) en
   \(\Sigma\) tenga una componente "no acotada" privilegiada (a diferencia de \(\mathbb R^3\), donde
   una esfera separa un interior acotado de un exterior no acotado y la asimetría topológica
   resolvería la elección sola).
2. **Corrección de orientación.** La reflexión inicialmente considerada,
   \(\varphi:\chi\mapsto\pi-\chi\), corresponde en la incrustación estándar \(S^3\subset\mathbb R^4\)
   (con \(x_4=\cos\chi\), \((x_1,x_2,x_3)=\sin\chi\cdot(\text{vector unitario en }\theta,\phi)\)) a
   la reflexión lineal \((x_1,x_2,x_3,x_4)\mapsto(x_1,x_2,x_3,-x_4)\), de determinante \(-1\): **invierte
   la orientación espacial de \(S^3\)**. Si la clase de difeomorfismos admisibles para argumentar
   naturalidad debe preservar también la orientación espacio-temporal, \(\varphi\) queda descartada
   como testigo y el argumento original no se sostiene sin modificación. Se sustituye por
   \[
   \psi:(x_1,x_2,x_3,x_4)\longmapsto(-x_1,x_2,x_3,-x_4),
   \]
   extendida trivialmente en \(t\). \(\det\psi=(-1)(1)(1)(-1)=+1\): **preserva orientación**
   (y, al no tocar \(t\), preserva trivialmente la orientación temporal). Verificación directa:
   \(\psi\) es una isometría de la métrica \(S^3\) estándar (restricción de una isometría lineal de
   \(\mathbb R^4\)), \(\psi_*g=g\) exactamente, \(\psi(U)=U\). Sobre \(S=\{x_4=0\}\), \(\psi\) actúa
   como \((x_1,x_2,x_3)\mapsto(-x_1,x_2,x_3)\): **deja \(S\) invariante como conjunto** (\(\psi(S)=S\))
   pero **no punto a punto** — solo fija el círculo máximo \(\{x_1=0\}\subset S\). Sí intercambia los
   hemisferios: \(\psi(\Omega_+)=\Omega_-\) (pues \(x_4\to-x_4\)).
3. **La covariancia no necesita puntos fijos.** Sean \(\ell_A\) = dirección nula futura que apunta
   fuera de \(\Omega_+\) (hacia \(x_4\) decreciente) y \(\ell_B\) = fuera de \(\Omega_-\) (hacia
   \(x_4\) creciente), como campos sobre \(S\) (hasta reescalado positivo, irrelevante por el Lema
   1). Como \(\psi\) intercambia \(\Omega_+\leftrightarrow\Omega_-\), transporta \(\ell_A\) en
   \(p\) a (un múltiplo positivo de) \(\ell_B\) en \(\psi(p)\) — **no** a \(\ell_B\) en el mismo
   punto \(p\), porque \(\psi(p)\neq p\) en general. Por el Lema 2 (isometría exacta) y el Lema 1
   (irrelevancia del reescalado positivo):
   \[
   \theta_B(\psi(p)) \;=\; \theta_{\psi_*\ell_A}(\psi(p)) \;=\; \theta_A(p)
   \qquad\forall\,p\in S,
   \]
   es decir \(\theta_B\circ\psi=\theta_A\) como identidad de **perfiles** (funciones sobre \(S\)),
   no de valores en el mismo punto. Esto ya basta: si \(S\) fuera FMOTS bajo la presentación
   \(\Omega_+\) (\(\theta_A\equiv0\) y \(\theta_B&lt;0\) en todo \(S\)), entonces
   \(\theta_B(\psi(p))=\theta_A(p)=0\) para todo \(p\), y como \(\psi|_S\) es una biyección de \(S\)
   sobre sí mismo, \(\theta_B\equiv0\) en todo \(S\) — **contradiciendo** \(\theta_B&lt;0\)
   estrictamente. El mismo argumento, con los papeles cambiados, descarta la presentación
   \(\Omega_-\). **No hace falta que \(\psi\) fije \(S\) punto a punto para que la covariancia
   impida que una expansión sea idénticamente cero mientras la otra es estrictamente negativa.**
4. **Conclusión del test.** \(\psi\) es una isometría propia, ortócrona, que preserva \((g,U)\),
   deja \(S\) invariante como conjunto e intercambia sus dos presentaciones admisibles como borde de
   región compacta. **La propuesta "\(S=\partial\Omega\) con \(\Omega\) compacta determina un
   exterior" queda `REFUTED` en la clase actualmente declarada** — no por un artefacto de
   orientación del testigo, sino con un testigo que preserva orientación espacial y temporal. Como
   antes, esta \(S\) particular no puede ser un FMOTS genuino bajo ninguna presentación (mismo tipo
   de protección que en el intento anterior, ahora derivada sin puntos fijos); eso acota el riesgo
   concreto de este ejemplo sin decir nada sobre superficies asimétricas, que no se han
   construido ni se construyen en esta sesión.

**Respaldo primario:** la construcción es autocontenida (incrustación estándar \(S^3\subset\mathbb
R^4\), cálculo explícito de \(\psi\) y de su determinante) y verificable línea por línea en este
documento; no requiere ni se buscó cita de `biblioteca/` — es geometría diferencial elemental
aplicada a una métrica escrita explícitamente, no un resultado especializado de relatividad
matemática.

### Veredicto de la condición

`OPEN`, **sin que esto constituya un no-go universal**. El test falsificador se ejecutó con un
testigo que preserva orientación espacial y temporal (corrigiendo el testigo inicial, que no lo
hacía), y su resultado es concluyente en la rama que importa: **\(S\) pertenece a la clase
actualmente declarada**, y \(\psi\) —isometría propia y ortócrona de \((g,U)\) que deja \(S\)
invariante como conjunto e intercambia las dos regiones compactas que puede bordear— basta, por
covariancia de perfiles (sin necesidad de puntos fijos), para impedir que \(S\) satisfaga el
criterio FMOTS bajo ninguna presentación consistentemente. **La propuesta concreta "borde de
región compacta \(\Omega\)" como selector de exterior queda `REFUTED` para la clase actual** — no
fija la coorientación cuando la topología de \(\Sigma\) no privilegia un lado. Esto refuta *esa*
propuesta específica, no la posibilidad de cualquier cierre intrínseco: no se ha exhibido, ni se
buscó, un argumento de que **ninguna** definición intrínseca de "exterior" pueda existir — solo que
esta no basta. La condición 1 permanece `OPEN`: el progreso de los Lemas 1–2 sigue siendo válido y
reutilizable en cualquier reparación futura, pero el problema de fondo ya no es "elegir un orden de
cuantificadores sobre \(\Sigma\)" (formulación anterior, corregida) — es que la clase, tal como está
escrita, **no fija la coorientación de \(S\)** cuando la topología de \(\Sigma\) no privilegia un
lado, y la vía de borde-de-región-compacta, tal como se propuso, ya no es candidata viable sin
modificación. No se construyó ningún ejemplo asimétrico adicional en esta sesión.

---

## Condición 2 — Re-argumentar G8 contra el Teorema 2 de Müller

**Status: CLOSED**

### Evidencia primaria (lectura completa del PDF esta sesión)

Texto íntegro de la prueba del Teorema 2 (`biblioteca/2503.01719v2.pdf`, p. 3, vía
`pdftotext -layout`):

> "Let \(X\) be any Cauchy slab. There is \(x\in X\) with \(\operatorname{vol}(J^+(x))<v/2\) with
> \((1-v)K>\varepsilon\). Let \(q\in(X\setminus J^+(x))^K\), then \(C_K(X)(q)>\varepsilon\). Let
> \(c\) be a maximizer from \(x\) to the future boundary of \(X\) of length \(r\). We modify the
> Lorentzian metric in a sufficiently thin neighborhood of \(c\) by a **conformal factor** \(u\) in
> a way that the volume of \((J^+(x),ug)\) is smaller than \(v\) and the length of \(c\) w.r.t.
> \(ug\) is greater than \(r+D\). We call the resulting Cauchy slab \(Y\). Consequently,
> \(C_K(Y)(q)>\varepsilon\), and \(d^-(X,Y)>\operatorname{tdiam}(J^+(x),ug)-
> \operatorname{tdiam}(J^+(x),g)=D\)."

Hechos verificados directamente del texto primario:

1. **\(X\) es "any Cauchy slab"** — enteramente arbitrario, no plano. Esto confirma y refuerza el
   hallazgo del verificador de literatura de la Decisión 048 §7 (la premisa de planitud del
   matemático de Wave 1 es válida solo para el Teorema 3, no el Teorema 2).
2. **El mecanismo es literalmente el mismo que propone B2**: una perturbación conforme de soporte
   pequeño (un "sufficiently thin neighborhood" de una curva) sobre un slab de Cauchy arbitrario,
   con datos de frontera compartidos: el enunciado del Teorema 2 exige \(\partial^\pm X=\partial^\pm
   Y\) (línea 133 del texto extraído) — **esto coincide exactamente** con la fila "Bordes: mismos
   datos de borde o diferencia declarada" del contrato §3
   (`phase3_b2_witness_pair_preopening_contract.md:106`).
3. **El canal es literalmente el mismo que propone B2**: \(C_K(X)\) es la medida de probabilidad
   sobre relaciones de orden en \(K\) puntos i.i.d. de la medida de volumen normalizada, invariante
   bajo permutación (definición en p. 3 del PDF) — esto es exactamente
   \(P_{i,n}\) del contrato §4.1 con \(K=n\).
4. **Búsqueda exhaustiva confirma que Müller nunca menciona superficies atrapadas.** Se ejecutó
   `grep -in "trap|horizon|MOTS|expansion|marginal"` sobre el texto completo extraído del PDF
   (292 líneas, artículo completo incluidas referencias): **cero coincidencias**. El artículo de
   Müller no prueba, ni niega, ni siquiera formula nada sobre existencia de MOTS, superficies
   atrapadas ni expansiones nulas. Su target es la distancia de Lorentz / diámetro temporal
   \(d^-\), un invariante completamente distinto de \(Q_{\mathrm{FMOTS}}\).

### Argumento y disposición

La pregunta de la condición 2 tiene dos partes, y deben responderse por separado:

- **¿El resultado de Müller ya establece (o refuta) lo que B2 querría probar?** No. El Teorema 2
  de Müller no dice nada sobre superficies atrapadas — es lógicamente mudo respecto de
  \(Q_{\mathrm{FMOTS}}\). No hay ningún resultado publicado que anticipe si la perturbación
  conforme construida por Müller cambia o no el estado de MOTS del slab. **Por tanto
  `B2_REDUNDANT_WITH_MULLER` no se dispara**: no existe redundancia de *resultado*, porque el
  resultado de B2 (si se probara) sería sobre un objeto que Müller nunca toca.
- **¿La técnica es la misma?** Sí, casi exactamente: perturbación conforme de soporte pequeño sobre
  un slab arbitrario con datos de frontera compartidos, medida vía ley de orden invariante a
  cardinalidad fija. La única diferencia real de mecanismo es que Müller perturba un entorno
  tubular delgado de una curva 1-dimensional (una geodésica maximizante), mientras que el contrato
  B2 (§3) permite un soporte más general \(\omega\in C_c^k(U)\) — pero un entorno tubular delgado
  de una curva **es un caso particular** de esa familia general, así que la construcción de Müller
  cabe dentro de la familia que B2 propone, no al revés.

### Veredicto de la condición

`CLOSED` — pero **solo respecto a la redundancia lógica**, y no más que eso. Lo que queda cerrado
es exactamente esta proposición: *Müller no implica, ni contradice, la separación de
\(Q_{\mathrm{FMOTS}}\)* — es lógicamente mudo sobre superficies atrapadas, así que
`B2_REDUNDANT_WITH_MULLER` no se dispara por *resultado*. Esto **no** cierra, y no debe leerse como
si cerrara, la cuestión de si B2 aporta un método nuevo: el mecanismo (perturbación conforme de
soporte pequeño sobre un slab arbitrario, con \(\partial^\pm X=\partial^\pm Y\) compartido) y el
canal (ley de orden invariante a cardinalidad fija) son, hecho por hecho, los mismos que el
Teorema 2 de Müller. Esta cautela **no es un caveat temporal para retirar más adelante**: es una
condición permanente de cómo debe describirse B2 si algún día se completa —
instanciación/adaptación acotada de la técnica de Müller sobre un target que su artículo no aborda,
nunca como método nuevo — exactamente la disposición que el contrato ya anticipaba en su propia
cláusula de gobernanza (`phase3_b2_witness_pair_preopening_contract.md:184-186`, "Una técnica
conocida con target nuevo se describirá como instanciación/adaptación acotada, no como método
nuevo"). Cualquier "Ledger de fuentes" futuro (§8.5 del contrato) debe citar la prueba del Teorema 2
verbatim (arriba), no la del Teorema 3, y debe conservar esta cautela en cualquier redacción
posterior — incluida la propia adjudicación de admisión, si algún día se reconvoca.

---

## Condición 3 — Pre-declarar la degradación de regularidad

**Status: OPEN**

### Evidencia y re-examen del argumento de Wave 1

El matemático y el físico derivaron independientemente, en la Decisión 048, que forzar el cambio de
signo de \(\theta_+\) exige amplitud \(\|\omega\|_\infty=O(1)\) y por tanto curvatura
\(\|\partial^2\omega\|\sim\rho^{-2}\sim\sqrt{n}\) al encoger el soporte \(\rho\to0\) para mantener
\(\mathrm{TV}(\mu_0,\mu_1)=O(1/n)\). Ambos lo marcaron `[UNVERIFIED heuristic]`.

Al re-derivar este argumento para este dossier, se encontró que descansa en un supuesto no escrito
en ninguna parte: que la superficie testigo \(S\) debe tener **escala macroscópica**, comparable al
tamaño de \(U\) (por ejemplo, un horizonte tipo Schwarzschild de radio \(\sim L=\operatorname{diam}
(U)\)), de modo que igualar la corrección \(2\ell_+(\omega)\sim\|\omega\|_\infty/\rho\) con el valor
típico de \(\theta_+\sim2/L\) fuerce \(\|\omega\|_\infty\sim\rho/L\to0\) — es decir, **si \(S\) es
macroscópica, la amplitud SÍ puede encogerse junto con \(\rho\)**, contradiciendo la conclusión de
amplitud \(O(1)\).

La conclusión de Wave 1 (\(\|\omega\|_\infty=O(1)\)) solo se sostiene bajo un supuesto distinto y
más restrictivo: que \(S\) está **confinada a la escala del propio soporte** \(\rho\) (por ejemplo,
una superficie pequeña generada enteramente dentro de la protuberancia conforme, no anclada a
ninguna característica macroscópica de \(U\)). En ese caso \(\theta_+\) de fondo en esa región es
\(O(1/\rho)\) también (una superficie pequeña en un espacio casi-plano tiene expansión \(\sim2/\rho\)),
y entonces sí se necesita \(\|\omega\|_\infty/\rho\sim1/\rho\Rightarrow\|\omega\|_\infty=O(1)\) para
cancelar el término de fondo — coincidiendo con la heurística de Wave 1.

**Cuál de los dos escenarios es el relevante depende enteramente de qué superficies admite
\(S_{\rm adm}\)** — en particular, de si la clase permite superficies de escala arbitrariamente
pequeña o exige alguna cota inferior de tamaño / anclaje a una característica de \(U\). Esa
pregunta es exactamente la condición 1, todavía abierta.

### Veredicto de la condición

`OPEN`, y depende explícitamente de la condición 1. La heurística de degradación de Wave 1 sigue
siendo una advertencia legítima y no descartada (es correcta bajo el supuesto de superficie
confinada al soporte), pero no puede pre-declararse como techo de reclamo (G4/G9) sin primero
decidir la escala admisible en \(S_{\rm adm}\) — declararla ahora, sin esa decisión, sería fijar
un techo de reclamo sobre una premisa no verificada, exactamente el tipo de afirmación prematura
que la Decisión 048 ya advirtió evitar. Ningún cálculo de esta sesión usó par testigo, código,
simulación ni semillas — es análisis dimensional de lápiz y papel únicamente.

---

## Condición 4 — No tratar G2 como cerrado hasta que \(S_{\rm adm}\) esté cerrado

**Status: OPEN** (estado derivado directamente del de la condición 1; no es una tarea matemática
independiente sino una disciplina de gobernanza que se sigue de la condición 1 por construcción)

### Verificación

La Decisión 048 (Wave 1, brief del lógico) ya estableció que \(Q\neq T_{EH}\) (G2) es demostrable
*condicionalmente*: si \(S_{\rm adm}(g,U)\) depende únicamente de \(g|_U\), entonces \(Q\) es un
funcional de \(g|_U\) mientras que \(T_{EH}\) no lo es (por el Teorema 3.2 probado en
`docs/manuscript_limits_draft.md:455-483`), y ese teorema suministraría el testigo de separación
directamente. Esta sesión no ha cerrado \(S_{\rm adm}\) (condición 1 sigue `OPEN`), así que la
premisa de localidad de \(S_{\rm adm}\) sigue sin verificarse formalmente — aunque las dos
formulaciones candidatas de la condición 1 (borde de región compacta dentro de una loncha
\(\Sigma\subset U\); orientación libre tipo trapped-surface) **sí parecen depender solo de
\(g|_U\)** en su forma actual, lo cual es una señal positiva pero no una prueba.

### Veredicto de la condición

`OPEN`, por diseño: esta condición no puede marcarse `CLOSED` mientras la condición 1 no lo esté,
y no debe forzarse. Se registra aquí, siguiendo la instrucción del PI, que la disciplina se está
respetando correctamente — G2 no se trata como cerrado en ningún documento de este expediente.

---

## Condición 5 — Exhibir (o diferir explícitamente) ejemplos con \(Q=1\) y \(Q=0\)

**Status: PARTIAL**

### Candidatos identificados (no construidos como testigo — son hechos de GR estándar, no un par
comparativo con cota TV)

- **Candidato \(Q=1\):** un parche \(U\) compacto causalmente convexo de Schwarzschild que contenga
  la esfera \(r=2M\) en algún corte temporal. Es un hecho estándar de GR, ya confirmado por el
  verificador de literatura de la Decisión 048 contra `biblioteca/derived-md/Towards black-hole
  horizons and geodesic focusing in causal sets.md:221-225`: \(\Theta_{\rm out}(r=2M)=0\),
  \(\Theta_{\rm in}=-2/r&lt;0\) en todo \(r\). Esa esfera es, por definición, una MOTS exacta.
- **Candidato \(Q=0\):** cualquier parche \(U\) compacto de Minkowski (plano). Es un hecho estándar
  de relatividad general que el espacio de Minkowski no admite superficies cerradas atrapadas ni
  marginalmente atrapadas — toda esfera redonda tiene \(\theta_{\rm out}=2/r&gt;0\) en todas
  partes, y esto se extiende a toda superficie cerrada embebida en una loncha plana por argumentos
  estándar de positividad. **`[UNVERIFIED against biblioteca — no hay libro de GR local; este es
  conocimiento de fondo estándar, no una cita verificable localmente]`.**

### Por qué esto es `PARTIAL` y no `CLOSED`

- Ambos candidatos son plausibles y de altísima probabilidad de ser correctos, pero su admisibilidad
  formal depende de que la esfera en cuestión efectivamente pertenezca a \(S_{\rm adm}(g,U)\) bajo
  cualquiera de las dos formulaciones candidatas de la condición 1 — y esa condición sigue `OPEN`.
- Ninguno de los dos hechos de GR está anclado a una fuente primaria disponible en `biblioteca/`
  (la biblioteca del proyecto es de teoría de conjuntos causales, no de relatividad general
  estándar) — deben marcarse `[UNVERIFIED against biblioteca]` aunque sean estándar.
- No se ha construido explícitamente el parche compacto causalmente convexo \(U\) con datos de
  frontera para ninguno de los dos casos (eso empezaría a acercarse a construcción, fuera del
  alcance de este dossier).

### Veredicto de la condición

`PARTIAL`. El estándar de no-vacuidad de la pista Lean del repositorio (exhibir tanto \(Q=1\) como
\(Q=0\) antes de usar la clase, cf. `formal/HorizonFormal/HorizonFormal/Horizon.lean:120-125,
195-249`) parece satisfacible con ejemplos estándar de GR una vez cerrada la condición 1, pero no
está formalmente cerrado hoy.

---

## Síntesis y estado para reconvocatoria

| # | Condición | Status | Depende de |
|---|---|---|---|
| 1 | Cerrar \(S_{\rm adm}\)/orientación | `OPEN` | — (raíz) |
| 2 | Re-argumentar G8 vs. Thm 2 de Müller | `CLOSED` *(solo redundancia lógica — ver caveat permanente arriba)* | independiente |
| 3 | Pre-declarar degradación de regularidad | `OPEN` | condición 1 (escala admisible en \(S_{\rm adm}\)) |
| 4 | No cerrar G2 prematuramente | `OPEN` | condición 1 (por diseño) |
| 5 | Exhibir ejemplos \(Q=1\)/\(Q=0\) | `PARTIAL` | condición 1 |

Ninguna condición resultó fatal en el sentido de "provablemente imposible de cerrar" — no se marca
ninguna `NOT_REACHED`. La condición 1 (cierre intrínseco de \(S_{\rm adm}\)) es la única raíz
genuinamente abierta y es el **siguiente bloqueo a atacar** — no "lo único que falta" en general:
resolverla no cierra automáticamente las condiciones 3, 4 y 5, solo determina la forma que su
trabajo pendiente debe tomar. Esta sesión avanzó la condición 1 con dos demostraciones completas
(Lema 1: la normalización de \(\ell_\pm\) es irrelevante; Lema 2: cualquier candidato construido a
partir de propiedades naturales es automáticamente difeomorfismo-invariante), un resultado negativo
verificado (el atajo "libre de orientación" no evita el problema, lo reubica), y un **test
falsificador ejecutado y concluyente**: una 2-esfera ecuatorial en una loncha \(\Sigma\cong S^3\)
(p.ej. FRW cerrado) pertenece a la clase declarada y admite dos presentaciones \(S=\partial\Omega_+
=\partial\Omega_-\) de coorientación opuesta, relacionadas por \(\psi:(x_1,x_2,x_3,x_4)\mapsto
(-x_1,x_2,x_3,-x_4)\) — una isometría **propia y ortócrona** de \((g,U)\) (determinante \(+1\),
preserva orientación espacial y temporal; el testigo inicial, una reflexión que invertía
orientación, fue descartado y corregido por esta razón) que deja \(S\) invariante como conjunto
(sin fijarla punto a punto) y permuta los lados. La covariancia de perfiles bajo \(\psi\) —sin
necesidad de puntos fijos— ya basta para impedir que una expansión sea idénticamente cero mientras
la otra es estrictamente negativa. **La propuesta concreta "\(S=\partial\Omega\) con \(\Omega\)
compacta" como selector de exterior queda `REFUTED` para la clase actualmente declarada** —no fija
la coorientación cuando la topología de \(\Sigma\) no privilegia un lado (a diferencia de
\(\mathbb R^3\) o de un espaciotiempo asintóticamente plano). Esto refuta esa propuesta específica,
**no constituye un no-go universal**: no se ha mostrado, ni se intentó mostrar, que ninguna
definición intrínseca de "exterior" pueda existir — solo que esta no basta. El bloqueo real, gracias
a esta sesión, ya **no** es "elegir un orden de cuantificadores sobre \(\Sigma\)" (formulación de la
sesión anterior, ahora corregida): cambiar de loncha sin cambiar de lado solo produce un boost,
inocuo por el Lema 1; lo que falta es fijar la **coorientación** misma, y el test falsificador
muestra que \((g,U)\) solo, sin hipótesis adicional sobre la topología de \(U\) o sin datos
auxiliares (una foliación elegida), no basta para hacerlo con esta propuesta. No se construyó
ningún ejemplo asimétrico adicional en esta sesión — el resultado se apoya enteramente en el
testigo simétrico corregido. Las condiciones 3, 4 y 5 heredan esa apertura exactamente como antes,
sin cambios de sustancia por este avance: la 3 necesita, además, decidir la escala admisible en
\(S_{\rm adm}\) una vez fijada la definición; la 5 necesita construir (o justificar diferir) los
parches compactos concretos; y la 4 simplemente deja de estar bloqueada, pero su cierre efectivo
(aplicar el argumento del Teorema 3.2) sigue pendiente de ejecutarse.

**Precisión sobre las rutas de la condición 1 — no son intercambiables.** El propio texto de la
condición 1 ofrece dos caminos, y son categóricamente distintos, no dos variantes de lo mismo:

- **Reparar \(S_{\rm adm}\) dentro de \(Q_{\mathrm{FMOTS}}\)** (cerrar la definición de "exterior"
  intrínsecamente) — esto sí **cerraría la condición 1** tal como está planteada, sin tocar el
  target. Dentro de esta ruta, esta sesión descartó dos candidatas por no funcionar: la definición
  simétrica/libre de orientación (no evita el problema, lo reubica), y la formulación de borde de
  región compacta dentro de una loncha \(\Sigma\) (`REFUTED` por el test falsificador — no fija la
  coorientación cuando la topología de \(\Sigma\) no privilegia un lado). Ninguna candidata viable
  queda identificada todavía; la ruta sigue abierta, no descartada en general.
- **Sustituir \(Q_{\mathrm{FMOTS}}\) por un indicador libre de orientación** ("trapped surface",
  \(\theta_+&lt;0\) y \(\theta_-&lt;0\) simétricos) — esto **no es una reparación de \(S_{\rm
  adm}\)**, es **cambiar el target**, y además esta sesión mostró que ni siquiera evita el problema
  que pretendería resolver (ver hallazgo negativo arriba): también necesitaría datos transversales
  para distinguir un MOTS exterior genuino de una configuración "interior" con los papeles
  cambiados. Cambiaría qué se está adjudicando (de "existencia de MOTS orientada" a "existencia de
  región marginal sin orientar"), y el propio contrato exige que una sustitución así recorra G1–G9
  **desde cero, como un acto de adopción nuevo** — no puede colarse como si fuera el cierre de esta
  condición. Este dossier no recomienda ni descarta esa sustitución; solo constata que es un fork
  distinto, no una casilla intercambiable con la reparación, y que tampoco es un atajo matemático
  más fácil de lo que parecía.

**READY_TO_RECONVENE: NO → `NOT_READY_TO_RECONVENE`**

Justificación de los bloqueos residuales: la condición 1 es la raíz y el siguiente paso de trabajo,
pero no el único pendiente — las condiciones 3 y 5 seguirán teniendo trabajo propio incluso después
de que la 1 se resuelva, y la 4 solo deja de estar bloqueada, no se cierra automáticamente. La
condición 2, en cambio, queda cerrada en su alcance limitado (no-redundancia lógica) y no debe
reabrirse salvo que aparezca nueva evidencia primaria — pero su cautela de "instanciación acotada,
no método nuevo" permanece vigente indefinidamente, no es un caveat de paso.

Este documento no ha sido comiteado, no se ha versionado (sin commit, sin push), no modifica la
Decisión 048 ni el contrato de preapertura, no toca el PR #1, no adopta \(Q_{\mathrm{FMOTS}}\) y no
reconvoca al comité.
