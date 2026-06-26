# PR-003 — BL-localización (Trauthwein–Yukich 2026) como ruta a la ley nula de C1 (dev, NOT a result)

Nota de sandbox. **Análisis teórico, nada medido, nada congelado, ningún claim.** Su valor es
re-evaluar un veredicto previo de la literatura de apoyo a la luz de un paper que el propio informe
citó pero aplicó bajo un marco más fuerte (y por tanto más restrictivo) del necesario.

## 0. Origen

El documento de apoyo `biblioteca/Horizontes En Conjuntos Causales.md` (git-ignored) audita el
candidato **C1** (altura intrínseca `s(x)`, foliación por ideales `Σ_ℓ`, flujo `Φ(ℓ)` normalizado
mediana/MAD, umbral `z*`) y emite dos veredictos:

- Entregable B (Dossier C1): `C1_IS_ONLY_AN_EMPIRICAL_DETECTOR`.
- §6 (global): `CREDIBLE_ONLY_AS_SEMICLASSICAL_PROGRAM`.

El Dossier B descansa en dos patas independientes:
1. **Pata semiclásica (Lema L₁):** "C1 carece de ley nula analítica porque `Φ` no estabiliza — el
   add-one cost de la altura no decae (un punto en el pasado profundo reordena toda la foliación),
   lo que bloquea Malliavin–Stein."
2. **Pata cuántica (Lema L₆):** "el min sobre cortes requiere el futuro asintótico → C1 es un
   *rogue set* no medible en la σ-álgebra de stems del covtree (Dowker–Zalel)."

Esta nota ataca **sólo la pata 1.** La pata 2 queda intacta (ver §5).

## 1. Qué prueba Trauthwein–Yukich (arXiv:2605.23292, "Second-order Poincaré inequalities and
   localization on the Poisson space", 22 May 2026; PDF en biblioteca)

- **Teorema 2.1 (p.5):** cota de 2º orden de Poincaré / Malliavin–Stein afilada para CUALQUIER
  funcional de Poisson `F` con `𝔼F=0` y momento finito de los operadores diferencia. Da
  `d_W(F,N), d_K(F,N) ≤ Σ_{i=0}^{6} γ̂_i`, con cada `γ̂_i` una integral de **cuartos momentos** de
  los operadores diferencia de 1er y 2º orden `D_xF`, `D²_{x,y}F` (def. p.4). **A este nivel NO se
  exige estabilización alguna** — sólo momentos cuartos finitos. Elimina los términos `γ₃,γ₄`
  (el `𝔼F⁴` problemático) de Last–Peccati–Schulte 2016 (p.6, punto 1).
- **Definición 2.3 (p.8) — BL-localización:** condición estructural sobre un funcional de tipo
  suma-de-scores `H = Σ_z ξ(z,P)` que hace colapsar los `γ̂_i` a `O(1/√Var H)`, dando la cota
  Berry–Esseen `d(H̃,N) = O(1/√Var H)` (eq. 1.3).

## 2. El punto clave: BL-localización es ESTRICTAMENTE más débil que estabilización

Cita textual (p.8):

> "BL-localization establishes closeness in the `d_BL` metric between the **laws** of the random
> variables ξ and their short-range versions ξ^[r], in contrast to 'stabilization', a notion
> comparing **specific realizations** of the scores — either exactly (via stopping sets) or
> approximately in L^q."

Y (p.6): "weaker and more flexible than the standard stopping set stabilization criterion … it
also **allows for interactions of scores at distant points**."

La objeción del informe (`D_{x'}s(x)` no decae) es una afirmación sobre **realizaciones
específicas** (estabilización L¹/stopping-set). BL-localización **no la usa**. Sólo pide que la
**distribución** del score local sea aproximable (en `d_BL`) por la de un score de rango corto,
uniformemente sobre cuádruplas y sobre configuraciones añadidas `𝒜` de tamaño ≤5 (eqs. 2.3–2.4).
**El informe descalificó C1 con el criterio antiguo; el criterio de 2026 no impone esa
descalificación.**

## 3. Mapeo sobre C1 — [PLAUSIBLE-TRANSFER], NO probado

- `Φ(ℓ) = Σ_{(x,y): x≺y, s(x)≤ℓ<s(y)} 1 = Σ_{z∈P} ξ(z,P)` es un **funcional de score de Poisson
  con indexado de orden 2** (no una U-estadística: el indicador de cruce depende de `s(·)`, un
  funcional GLOBAL de `P`, no de un núcleo que dependa sólo del par `(x,y)`). Anclando cada par en
  su punto superior `z=y`, `ξ(z,P) = #{x≺z : s(x)≤ℓ<s(z)}` — exactamente la forma `H=Σ_z ξ(z,P̂)`
  para la que TY Setup p.7 está construido, y precisamente NO la maquinaria U-estadística / caos de
  Wiener finito. [Corrección C5, comité 007.] El montaje espacio-temporal `X×ℝ` con **horizonte
  temporal infinito** (Setup p.7) = sprinkling con futuro no acotado.
- Dos detalles que invierten la intuición del informe:
  - El add-one cost de la **altura misma** es `D_{x'}s(x) ∈ {0,1}` (añadir un punto sube la cadena
    más larga en a lo sumo 1). Lo NO acotado es el **número** de `x` afectados — y eso es justo lo
    que mata la estabilización clásica pero **no** la BL-localización (que mira leyes, no
    realizaciones). Un reordenamiento global *coherente* de la etiqueta de altura re-indexa el corte
    pero deja el perfil de flujo (como función de la posición geodésica) aprox. invariante.
  - La cadena más larga hasta `x` vive, con alta probabilidad, en un **tubo** de anchura
    transversal `~ℓ^{2/3}` alrededor de la geodésica (exponente transversal 2/3 de la percolación de
    último paso dirigida / Ulam; *estándar, no re-derivado aquí*). `s(x)` es por tanto localizable,
    aunque a una escala que CRECE con `ℓ`, no a radio fijo.
- Dos rasgos de TY hechos a medida:
  1. **Decaimiento integrable, NO exponencial:** sólo se exige `I_ψ(θ)<∞` (eq. 2.5) y `I_φ(θ')<∞`
     (eq. 2.6), "a mild integrability condition" (p.3). Un `ψ(r)` polinómico/estirado (cola KPZ)
     podría bastar. Estabilización exigía decaimiento exponencial; aquí no.
  2. **Radio dependiente de la geometría:** TY permite que `ξ^[r]` "be dependent on the geometry of
     the balls `B_r(·)`" (p.9) y formaliza **localización en tiempo** (Def. 2.3, eq. 2.2/2.4) para
     scores de soporte temporal creciente — exactamente el tubo `ℓ^{2/3}`.

## 4. Gaps honestos (lo que aún hay que probar para convertir esto en lema)

1. **Establecer `ψ(r)` para el score de flujo** vía el exponente transversal de la DLPP y verificar
   `I_ψ(θ)<∞`. Es acotar una cola conocida, no inventar una propiedad nueva. → siguiente paso
   analítico (bosquejo pendiente).
2. **`Φ` vs el estadístico real de C1.** TY da la ley nula **marginal/conjunta de un nº finito de
   cortes** `φ(ℓ)` (Gaussiana, tasa Berry–Esseen). El estadístico de C1 es `min_ℓ φ(ℓ)` sobre una
   familia *creciente* de cortes correlacionados → **scan/extreme-value statistic**, no un CLT de
   Poisson directo. Por tanto:
   - TY ataca el **Lema L₁** (ley nula de los cortes) — el que estaba marcado "impossible".
   - TY **alimenta** el **Lema L₂** (`z* ~ √(2 log N_eff)`) pero no lo prueba: hace falta EVT de
     máximos de Gaussianas dependientes ENCIMA del CLT marginal de TY. Ese `√(2 log N_eff)` es el
     que el informe ya marcó `[THEOREM-CONFIRMED]` y que toca el floor operacional de prereg-003.

## 5. Qué NO toca

TY es una CLT **cinemática** sobre sprinkling de Poisson. No dice nada sobre la σ-álgebra de stems
del covtree. El veredicto cuántico (C1 = *rogue set*, Lema L₆, §6 del informe) **permanece
intacto.** TY no rescata la aspiración de "observable cuántico relacional".

## 6. Re-graduación (adjudicada — comité 007, RECOMMEND_PROCEED_WITH_CAVEATS)

- **Entregable B / Lema L₁:** de `IMPOSSIBLE` → **`OPEN–CONTINGENT`**. La imposibilidad (anclada a
  estabilización, una condición SUFICIENTE) se retira: TY Thm 2.1 no la asume y Def. 2.3 compara
  LEYES, no realizaciones. Se identifica una estrategia concreta, pero el grado es *contingente* de
  dos sub-lemas nombrados:
  - **L₁a (control del operador no acotado / invarianza de perfil):** acotar los momentos de
    `D_{x'}Φ` (UNbounded — el `{0,1}` es de `s`, no de `Φ`) en TY Thm 2.1; i.e. mostrar que el
    re-indexado global coherente de `s` deja la ley del flujo `d_BL`-cercana a su truncación de
    rango corto pese a `D_{x'}Φ` no acotado.
  - **L₁b (integrabilidad):** establecer `I_ψ(θ)<∞` para el score de flujo anclado en el dominio no
    acotado con sección de tubo `∝ ℓ^{2/3}`, vía la cola transversal DLPP. → bosquejada en §8.
- **Veredicto global §6:** SIN CAMBIO (`CREDIBLE_ONLY_AS_SEMICLASSICAL_PROGRAM`); la barrera
  cuántica L₆ es independiente y queda intacta.
- **Conexión prereg-003 [FIREWALL C1, vinculante]:** *condicional y NO autorizante.* SI L₁a+L₁b se
  cerraran, TY + EVT *sería* el backbone de un escalado `z* ~ √(2 log N_eff)`. Esta observación
  teórica **NO autoriza** modificar `z*`, `K_LOC=2`, `theta_loc`, `theta_stab` ni `P_PERM_THRESHOLD`
  donde están congelados/operativos. Cualquier cambio de un umbral congelado requiere una NUEVA
  pre-registración con nuevo sello, auditoría independiente y autorización explícita — idéntico al
  proceso que produjo `docs/preregistration_003.md`. L₁ ≠ L₂: TY da sólo el CLT marginal/conjunto;
  el escalado de `z*` necesita EVT de máximos de Gaussianas dependientes ENCIMA.
- **Gaps abiertos adicionales [comité 007]:** C3 (sin geometría encubierta en la prueba: el tubo y
  la escala de localidad deben caracterizarse orden-teóricamente; "geodésica"/"transversal" son
  descripciones del continuo usadas para *benchmark*, jamás para *definir* `Φ`); C4 (gap
  parche-finito vs montaje tiempo-infinito de TY: efectos lenticulares de borde no modelados).

## 8. Bosquejo de la cota ψ(r) desde el exponente transversal (L₁b) — dev analítico, NO probado

Siguiente paso analítico solicitado; coincide con la prueba de falsación mínima del comité 007
(`∫ ψ(r) dr < ∞` uniforme en ℓ). Esto es un BOSQUEJO: cierra L₁b a escala fija y aísla qué queda
abierto (L₁a). Todo paso del continuo es *benchmark*, no entra en la definición de `Φ` (C3).

### 8.1 La identidad estructural: orden causal 1+1D = orden producto 2D

En Minkowski 1+1D plano (la hipótesis nula), en coordenadas de cono de luz `u=t−x`, `v=t+x`:
`p ≺ q ⇔ u_p ≤ u_q ∧ v_p ≤ v_q`. **El orden causal ES el orden producto (coordenada a coordenada)
en el plano `(u,v)`.** Por tanto un causal set de Minkowski 1+1D = un **orden aleatorio 2D** de un
proceso de Poisson de intensidad ρ en el plano `(u,v)` (Surya LRR §4; el hecho 2D-order es estándar
en CST). Consecuencias inmediatas:

- `s(q)` = cadena máxima desde mínimos hasta `q` = **subsecuencia creciente más larga (LIS) /
  last-passage dirigido** hasta `q` — el problema de Ulam/Hammersley poissonizado.
- Entre dos puntos separados `(Δu, Δv)`, la cadena máxima tiene longitud
  `L ≈ 2√(ρ Δu Δv)` con fluctuaciones **Tracy–Widom** de orden `L^{1/3} ∝ (ρΔuΔv)^{1/6}` — la
  clase de universalidad KPZ. **Exponente longitudinal 1/3 + límite TW CONFIRMADOS**: Sasamoto–Spohn
  2010 (`biblioteca/1002.1879v2.pdf`) eq. (1.5) `h(0,t) ≅ −½(q−p)t + 2^{−1/3}((q−p)t)^{1/3} ξ_TW`
  con `ξ_TW` Tracy–Widom (eqs. 1.6–1.7, núcleo de Airy). La pertenencia de la cadena más larga del
  causal set 1+1D a esta clase es vía LIS poissonizada (BDJ 1999; Surya §4.3).
- Como `Δu Δv = τ²` (tiempo propio al cuadrado, salvo constante), `s ≈ 2√ρ · τ` → **la altura es
  proporcional al tiempo propio.** El nivel `ℓ` corresponde a `τ_ℓ = ℓ/(2√ρ)`.

### 8.2 La cola transversal (el insumo KPZ)

La cadena maximizante entre extremos separados tiempo propio `T` se concentra en un **tubo** en
torno a la recta geodésica del continuo. **La ESCALA transversal 2/3 está anclada** por dos vías:
Sasamoto–Spohn 2010 (`biblioteca/1002.1879v2.pdf`, Introducción p.2) — "the height fluctuations will
grow as `t^{1/3}`, while the **transverse correlation length increases as `t^{2/3}`**" — y, como
teorema directo para el modelo poissoniano de subsecuencias crecientes, Johansson 2000,
*Transversal fluctuations for increasing subsequences on the plane* (NO en biblioteca; fuente
primaria leída externamente). A nivel `ℓ`, `T ∝ ℓ`, luego la escala transversal del tubo es
`∝ ℓ^{2/3}`.

**La FORMA de la cola es donde hay que ser preciso [corrección de fuente primaria].** La cola
cúbica `P(W>r) ≤ C exp(−c (r/ℓ^{2/3})³) = C exp(−c r³/ℓ²)` que usé en una primera versión **NO está
literalmente probada por Johansson 2000**: su prueba usa colas longitudinales tipo Tracy–Widom y
obtiene, para excluir desviaciones `r=N^γ`, una estimación `~exp(−c N^{6γ−4})`, que reescrita en `r`
da `~exp(−c r⁶/N⁴)` (cola **sextica**, no cúbica). Esto no refuta la cola cúbica; muestra que esa
atribución concreta a Johansson **no está sustentada** → la forma cúbica queda **[UNVERIFIED]**.

**Lo que sí es robusto:** ambas colas (la cúbica `exp(−c r³/ℓ²)` y la sextica de Johansson
`exp(−c r⁶/ℓ⁴)`, ya que su escala `N^{2/3}` ↔ `ℓ^{2/3}`) **cruzan en `r ~ ℓ^{2/3}`** y dan el MISMO
`∫ r ψ dr ~ ℓ^{4/3}` (§8.4). La convergencia depende de la **escala 2/3** (anclada), NO de la forma
de la cola. La forma cúbica es ilustrativa; el insumo crítico es la escala.

### 8.3 ψ(r) para el score de flujo

Truncación de rango corto `ξ^[r](z,P)`: calcular `s(z)` y los socios de cruce `x≺z` usando sólo
puntos dentro de radio `r` de `z` (en la métrica del plano `(u,v)`). `ξ ≠ ξ^[r]` exige que la cadena
máxima que fija `s(z)` (o el cruce de un socio por el corte) use un punto fuera del tubo de radio
`r`. Por §8.2, a nivel `ℓ`:

  **ψ(r) ≲ C exp(−c r³ / ℓ²).**

Decaimiento estirado/cúbico-exponencial — más fuerte que la integrabilidad *suave* que TY exige
(eq. 2.5), pero con **escala fijada por ℓ** (no radio fijo). Esto es exactamente lo que la
estabilización clásica (radio fijo, decaimiento exponencial) no captaba y BL-localización sí admite.

### 8.4 La integral de localización a escala fija (cierra L₁b a ℓ fijo)

`ν` = Lebesgue 2D (`ρ du dv`); en coordenadas polares el elemento de volumen es **`r dr`**
(explícito, no `dr`). La integral relevante de TY eq. 2.5, **condicional** a una cota uniforme
`ψ_ℓ(r) ≤ C exp(−c r³/ℓ²)`:

  `∫₀^∞ r ψ_ℓ(r) dr ≤ C ∫₀^∞ r exp(−c r³/ℓ²) dr`.

Sustituyendo `r = ℓ^{2/3} s` (⇒ `r dr = ℓ^{4/3} s ds`), con `∫₀^∞ s e^{−c s³} ds = (1/3) c^{−2/3} Γ(2/3)`:

  `= (C/3) c^{−2/3} Γ(2/3) · ℓ^{4/3} < ∞.`

(Con la cola sextica de Johansson `exp(−c r⁶/ℓ⁴)`: `r = ℓ^{2/3} s`, `∫ s e^{−c s⁶} ds` constante ⇒
**mismo `ℓ^{4/3}`**. La forma de la cola sólo cambia la constante, no el exponente.)

**Conclusión L₁b — CONDICIONAL, no teorema:** *si* se prueba la cota uniforme de cola con escala
`ℓ^{2/3}` (cualquier forma que decaiga), *entonces* `I_ψ(θ) ~ ℓ^{4/3} < ∞` a cada escala `ℓ`. La
cuenta es correcta; **la localización existe donde la estabilización fallaba**. Pero L₁b NO está
cerrado como teorema: queda condicional a (a) la cota de cola con su escala 2/3, y (b) **el paso
"orden producto 1+1D ⇒ las hipótesis exactas del modelo LPP de Johansson aplican al observable
causal concreto"**, que debe FORMULARSE, no asumirse por analogía KPZ. [gap L₁b-(b), nuevo]

> **Corroboración independiente del 4/3:** el exponente `ℓ^{4/3}` que sale aquí coincide con el
> exponente KPZ conocido `t^{4/3}` de la varianza de la función de dos puntos estacionaria
> (Sasamoto–Spohn 2010 p.2, citando bounds de Balázs–Quastel–Seppäläinen [ref. 2]). No es
> coincidencia: ambos integran la escala transversal 2/3 sobre la estructura 2D. Esto da confianza
> en que la sustitución `r = ℓ^{2/3}s` y el resultado `ℓ^{4/3}` son la física KPZ correcta, no un
> artefacto del bosquejo.

### 8.5 Lo que NO cierra el bosquejo (queda en L₁a)

El que `I_ψ < ∞` a `ℓ` fija da BL-localización; la **tasa Berry–Esseen** de TY escala como
`~ I_ψ^a / √Var Φ(ℓ)`. Con `I_ψ ~ ℓ^{4/3}` creciendo con la escala, el CLT con tasa **no trivial**
exige `Var Φ(ℓ)` creciendo lo bastante rápido para dominar. Calcular `Var Φ(ℓ)` (cuántos cruces y
su covarianza a nivel `ℓ` en el orden 2D) es la tarea analítica genuina restante = **L₁a**, ligada
al operador no acotado `D_{x'}Φ`. El bosquejo NO la resuelve; la deja como el cuello real.

**Veredicto del bosquejo:** L₁b cierra **CONDICIONALMENTE** (integral convergente exhibida, dado
(a) la cota de cola con escala 2/3 y (b) la aplicabilidad del modelo LPP al observable causal); L₁a
sigue abierto (interacción I_ψ-vs-Var en dominio creciente). Coherente con `OPEN–CONTINGENT`, **no
hay base para volver a IMPOSSIBLE, ni para elevar a `OPEN` pleno**. La integral `∫ r ψ dr` da
**finito a ℓ fija pero creciente como ℓ^{4/3}** — exactamente la frontera que L₁a debe domar.

## 9. L₁a — Var Φ(ℓ) en el orden 2D y control de `D_{x'}Φ` (dev analítico, HEURÍSTICO, NO probado)

Escalas del parche (cuadrado de lado `U` en `(u,v)`, intensidad `ρ`): `N = ρU²` puntos; altura
máxima `L_max ≈ 2√(ρU²) = 2√N` (Ulam/LIS, §8.1); número de niveles `~2√N`; **antichain por nivel
`|Σ_ℓ| ~ √N`** (`= √ρ U`). Todo "geodésica/transversal" es benchmark del continuo, NO entra en la
definición de `Φ` (C3).

### 9.1 Resultado forzado: el flujo DEBE ser de *enlaces* (covering-links), no de relaciones

El conteo de **relaciones transitivas** que cruzan el corte, `Φ_rel(ℓ)=#{x≺y : s(x)≤ℓ<s(y)}`, es
**no local**: un único `y` profundo en el futuro es comparable con `~ρ·u_y v_y` puntos pasados, casi
todos bajo el corte ⇒ `D_{x'}Φ_rel` crece con el **área** del parche, sin cola integrable. **BL-loc
FALLA para `Φ_rel`.** El objeto correcto es el **flujo de enlaces** (relaciones de cobertura,
intervalo vacío) que cruzan el corte:

  `Φ(ℓ) := #{ x⋖y : s(x)≤ℓ<s(y) }`,

que coincide con la `β` de covering-links del comité 006 (`docs/comite/comite_decision_006_*`).
**Primera conclusión de L₁a: el programa de localización OBLIGA a usar el flujo de enlaces; la
variante transitiva está muerta para Malliavin–Stein.** (Esto refina C5 y la definición de C1.)

### 9.2 `Var Φ(ℓ)` — escala [HEURÍSTICO]

Los enlaces que cruzan están anclados en la membrana ≈ hiperbola `uv = ℓ²/4ρ` (tiempo propio
constante). El nº de enlaces por elemento en un orden 2D de Poisson `~ log N` (la integral de
intervalo-vacío `ρ∫∫e^{−ρab}da db` es log-divergente, cortada por la caja). Enlaces que cruzan
`~ |Σ_ℓ| × O(1)` por celda de corte ⇒ `E[Φ(ℓ)] ~ √N` (salvo factores log). Si las contribuciones a
lo largo de la membrana (sistema efectivamente 1D de longitud `~U`) son **localmente dependientes**
con correlación que decae en la escala KPZ, entonces

  **`Var Φ(ℓ) ~ E[Φ(ℓ)] ~ √N`** (polylog) — [HEURÍSTICO, fluctuación tipo-Poisson de suma de
  términos locales sobre una membrana 1D].

### 9.3 `D_{x'}Φ` — no acotado, pero ¿con momentos controlados?

Añadir `x'` cambia `Φ` por dos vías: (i) **enlaces incidentes a `x'`** (creados/destruidos: `x'`
puede caer en un intervalo antes vacío y romper un enlace) — número `K_{x'}` con media `~log N` y
cola integrable; (ii) **re-clasificación por el desplazamiento de altura** `Δs∈{0,1}` que `x'`
propaga en su tubo futuro. El **soporte** del tubo en el corte tiene anchura transversal `~ℓ^{2/3}`
(§8.2), que intersecta `~√ρ·ℓ^{2/3}` puntos de `Σ_ℓ`. **AQUÍ está el cuello:**

- **Lectura A (localidad-absoluta, pesimista):** si una *fracción constante* de esos `~ℓ^{2/3}`
  puntos cambia de altura ⇒ `D_{x'}Φ ~ ℓ^{2/3} ~ N^{1/3}` para CADA uno de los `~N` puntos
  interiores ⇒ `∫ E[|D_{x'}Φ|⁴] ν ~ N·N^{4/3} = N^{7/3}`. Con `Var~√N`, la tasa de TY **diverge**.
  → L₁ revertiría hacia IMPOSSIBLE.
- **Lectura B (localidad-condicional, optimista):** el nº de `z` cuya altura *realmente* cambia al
  añadir `x'` = los `z` cuya **cadena máxima pasa por `x'`**, que es `O(1)` genérico (la cadena
  óptima a casi todo `z` NO atraviesa un `x'` dado; unicidad a.s. de la geodésica de last-passage).
  El `ℓ^{2/3}` es el **soporte** (quién *podría* afectarse), no el desplazamiento *realizado*, que es
  **disperso**. ⇒ `E[|D_{x'}Φ|⁴]` uniformemente `O(polylog)`, cola integrable. Entonces `∫ E|DΦ|⁴ ν
  ~ N·polylog` y la tasa de TY → 0 (escala `~ N^{−1/4}` polylog, suma de `~√N` celdas casi-indep).
  → L₁ cierra (OPEN → hacia CONFIRMED).

### 9.4 L₁a reducido a UNA conjetura nítida con regla de decisión

> **Conjetura de localidad-condicional (L₁a):** el flujo de enlaces, expresado *relativo a su propia
> foliación por altura*, tiene radio de localización efectivo por-score = la escala LOCAL inter-nivel
> `O(1)` (en altura), NO el `ℓ^{2/3}` global que necesita la altura *absoluta* `s`. Equivale a la
> versión rigurosa de "el re-indexado coherente deja el perfil de flujo invariante" (§3, §6).

- Si **VERDADERA** ⇒ `I_ψ` acotado por la escala local (no `ℓ^{4/3}`), `Var~√N`, tasa `~N^{−1/4}→0`
  ⇒ **L₁ graduaría OPEN-CONTINGENT → (camino a) CONFIRMED.**
- Si **FALSA** (el rango de nivel-absoluto `ℓ^{2/3}` es irreducible) ⇒ tasa diverge ⇒ **L₁ revierte
  hacia IMPOSSIBLE.**

El cálculo de escala por sí solo NO decide entre A y B: depende de la **dispersión del
desplazamiento de altura realizado** (¿cuántos `z` reenrutan su cadena máxima por un `x'` dado?). Esa
es la cantidad decisiva y es **directamente medible**.

### 9.5 Prueba decisiva (dev, reversible — propuesta, NO ejecutada)

`dev/measure_*.py` (venv sellado numpy 1.26.4, DEV_SEEDS, jamás VALIDATION_SEEDS; no toca umbrales
sellados; seal `6e2c3888…` pre+post). Medir en sprinklings de Minkowski plano, para `N` creciente:
1. `Var Φ_link(ℓ)` vs `N` en el corte bulk → confirmar/refutar el exponente `√N` (§9.2).
2. La **distribución de `D_{x'}Φ_link`** (add-one cost empírico: re-sprinkle quitando/poniendo `x'`)
   → media, cola, y sobre todo el **nº de `z` con altura cambiada por `x'`** (Lectura A vs B, §9.3).
3. El **rango de correlación** del flujo de enlaces a lo largo de la membrana → ¿escala local `O(1)`
   o global `ℓ^{2/3}`? (decide la conjetura §9.4).
Decisión: A ⇒ documentar reversión de L₁; B ⇒ documentar camino a cierre. Resultado reportado igual
sea cual sea (regla de reporte simétrica).

### 9.6 Resultado del probe (EJECUTADO — dev, EMPÍRICO, tasa heurística)

`dev/measure_bl_localization_l1a.py`, log `dev/bl_localization_l1a.log`; venv sellado numpy 1.26.4;
8 DEV_SEEDS; Minkowski plano; corte bulk = mediana de altura; `N ∈ {207, 410, 814, 1620}`; seal
`6e2c3888…` verificado pre y post. **Corrección importante que los datos imponen al §9.3/§9.4:** el
operador decisivo NO es `#shifted` (re-indexado de alturas) sino **`D_{x'}Φ` (cambio de flujo)**.

| N | E[Φ] | Var[Φ] | Var/√N | #shifted | mean\|DΦ\| | max\|DΦ\| | frac(DΦ≠0) | #contrib/√N |
|---|---|---|---|---|---|---|---|---|
| 207 | 41.5 | 196.6 | 13.7 | 8.0 | 0.76 | 12 | 0.241 | 3.46 |
| 410 | 77.8 | 321.9 | 15.9 | 11.8 | 0.38 | 9 | 0.178 | 3.61 |
| 814 | 158.8 | 452.5 | 15.9 | 18.0 | 0.50 | 12 | 0.175 | 4.99 |
| 1620 | 323.6 | 560.0 | 13.9 | 35.2 | — | — | — | — |

Tres hallazgos:
1. **`Var Φ(ℓ) ~ √N`** — `Var/√N` PLANO (13.7→15.9→15.9→13.9) sobre 8× en N. Confirma §9.2. ✓
2. **El re-indexado de alturas NO es disperso** — `#shifted ~ N^{0.7}` (8→35), incluso más rápido
   que el N^{1/3} de la Lectura A. Las etiquetas de `s` se mueven masivamente al quitar `x'`.
3. **PERO el operador de flujo `D_{x'}Φ` está CONTROLADO** — `mean|DΦ|` y `max|DΦ|` acotados
   (~0.5, ~12) sin tendencia con N, y la **fracción de `x'` con `DΦ≠0` DECRECE** (0.24→0.175) ⇒
   `#contrib` crece **sub-linealmente** (~N^{0.65}, frac↓). Esto es literalmente "el re-indexado
   coherente deja el perfil de flujo invariante" (§3, §6) — **medido**.

**Veredicto del probe (Lectura B favorecida, NO prueba):** con `|DΦ|` acotado por contribuyente,
`#contrib` sub-lineal y `Var ~ √N`, la tasa de Berry–Esseen **heurística** de TY
`d_W ~ (∫E|DΦ|⁴ ν)^{1/2}/Var ~ (N^{0.65})^{1/2}/N^{1/2} = N^{−0.18} → 0`. Robusto mientras
`#contrib` sea sub-lineal (cualquier α<1 da tasa→0; los datos dan frac↓ ⇒ α<1 claramente). **Esto
descarta la Lectura A (tasa divergente) EN EL RÉGIMEN NUMÉRICO EXPLORADO (`N≤1620`)** — el experimento
falsa esa lectura *operativa* concreta, NO es una refutación de un enunciado asintótico aún no
formalizado.

**Caveats honestos (por qué sigue OPEN-CONTINGENT, no CONFIRMED):**
- La fórmula de tasa es una **reducción dimensional heurística** de los γ̂ de TY (Thm 2.1); NO se
  computaron los términos de 2º orden `D²Φ`. [HEURÍSTICO]
- Sólo 3–4 N (207–1620) y 40 remociones/seed: el **exponente α de #contrib** (≈0.65) y la **cola del
  4º momento** de `|DΦ|` (vía `max` proxy) están poco constreñidos; un `x'` raro tipo "vértice de
  corte" del DAG de cadenas máximas podría engrosar la cola a N grande. [dev, muestreo limitado]
- **C4 no aislado:** el corte = mediana en una caja fija; los efectos lenticulares de borde no se
  separaron de bulk. Pendiente: corte bulk explícito lejos de bordes temporales.
- Falta el cierre **analítico** de la sub-linealidad de #contrib (unicidad a.s. de geodésica de
  last-passage ⇒ dispersión del desplazamiento *realizado*).

**Estado L₁a:** evidencia empírica **a favor de la localidad-condicional (cierre de L₁)**, con la
tasa→0 plausible; pero el grado se mantiene **OPEN-CONTINGENT** hasta (i) γ̂ completos de TY con
`D²`, (ii) prueba analítica de #contrib sub-lineal, (iii) cola del 4º momento a N grande, (iv)
aislamiento C4. El probe **descartó la Lectura A en el régimen numérico explorado**, no **probó** la B.
**L₁a queda CONGELADO** hasta resolver el mapeo L₁b-(b) (ver `dev/PR003_L1B_LPP_MAPPING_NOTES.md`):
afinar tasas Berry–Esseen sería correcto sobre el objeto equivocado si el puente LPP/KPZ falla.

## 7. Backing

- arXiv:2605.23292 (PDF en `biblioteca/2605.23292v1.pdf`): Teorema 2.1 (p.5), Def. 2.3 (p.8),
  eqs. 1.3/2.1–2.6, discusión "weaker than stabilization" (intro p.3 + §2.2 p.6; corrección de
  página del verif. de literatura, comité 007), montaje espacio-temporal (p.7), radio geométrico
  (p.9; eq. 2.4 está en p.8).
- `biblioteca/Horizontes En Conjuntos Causales.md` Entregables B/C/§6 (documento de apoyo,
  git-ignored).
- Orden causal 1+1D = orden producto 2D / LIS: Surya LRR §4 (estándar CST).
- **Escalas KPZ — ANCLADAS:** longitudinal 1/3 + límite Tracy–Widom + varianza 4/3 de la función de
  dos puntos vía Sasamoto–Spohn 2010 (`biblioteca/1002.1879v2.pdf`, eqs. 1.5–1.7 e Introducción p.2);
  **transversal 2/3** como teorema del modelo poissoniano de subsecuencias crecientes vía
  **Johansson 2000, *Transversal fluctuations for increasing subsequences on the plane*** (NO en
  biblioteca; primaria leída externamente). Pertenencia de la cadena más larga a la clase: LIS
  poissonizada (BDJ 1999 *Shape Fluctuations…*; Surya §4.3).
- **[UNVERIFIED] — la FORMA de la cola transversal.** La cúbica `exp(−c r³/ℓ²)` NO está probada por
  Johansson 2000: su estimación se reescribe como `~exp(−c r⁶/N⁴)` (sextica). La atribución cúbica
  no está sustentada. **No es crítica**: ambas colas cruzan en `r~ℓ^{2/3}` y dan el mismo `ℓ^{4/3}`;
  la convergencia de §8.4 sólo usa la escala 2/3 (anclada), no la forma.
- **[gap L₁b-(b)]** El paso "orden producto 1+1D ⇒ hipótesis exactas del modelo LPP de Johansson
  aplican al observable causal" debe formularse, no asumirse por analogía KPZ.
- Adjudicación: `docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md`
  (RECOMMEND_PROCEED_WITH_CAVEATS; caveats C1–C5).
