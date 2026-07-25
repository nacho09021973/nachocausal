# Ficha «SE BUSCA» — identificabilidad order-only en variación total (especificación de búsqueda bibliográfica)

**Estado:** `BORRADOR / EXPLORACION` (v4, 2026-07-25; v3 del 2026-07-24, v2 corregida tras
auditor_report_023, v1 sustituida). No es un documento congelado; no autoriza preregistros,
ejecuciones ni implementaciones. Su única función: especificar la búsqueda bibliográfica con
precisión suficiente para (a) dirigir cada disparo y (b) reconocer un acierto — o descartar un
falso positivo — con criterios escritos de antemano.

**v3 — dos disparos del coto 1 ya hechos (§2.1):** Janson 2011 (arXiv:0902.0306) y
Reitzner–Schulte 2013 (arXiv:1104.1039), ambos leídos íntegros, verificados localmente y
guardados en `biblioteca/`. Ninguno cierra el hueco central; Reitzner–Schulte lo reduce, para el
candidato 7.1, a una única desigualdad escalar por par (`p(theta) != p(theta')`), sin verificarla
para ningún par concreto — eso sería abrir cómputo/prueba nueva, no búsqueda bibliográfica.

**v4 — esa desigualdad ya está verificada (§2.2, nuevo).** El cálculo que la v3 dejaba pendiente
se hizo: `research_program/work_packages/wp4_comparable_pair_separation.md` (Anexo C de WP4) prueba
`p(tau) != p(tau')` para la familia diamante de WP4 §4, en forma cerrada al orden dominante en el
lapso nulo. **Esto cambia el estado de un ingrediente, no el de la ficha:** Forma L sigue `[OPEN]`,
y el obstáculo que queda no es esta desigualdad sino el **canal** (§2.2, punto 3). Auditado:
`docs/auditor/auditor_report_024_...md` (`AUDIT_FAIL`, un error de procedencia) y, tras corregirlo,
`docs/auditor/auditor_report_025_...md` (`AUDIT_PASS_WITH_WARNINGS`, 0 errores). Ninguna ejecución
del banco sellado; sello sin drift.

**Fuentes internas revisadas para esta versión** (las únicas que esta ficha cita):

- `research_program/work_packages/wp4_fisher_localization_floor.md` (WP4, íntegro);
- `research_program/models/first_witness_pair_candidates.md` (FWP, íntegro, esp. §4);
- `research_program/synthesis/op12_tv_zero_3p1.md` (OP-1.2, íntegro);
- `research_program/synthesis/pr012_tv_curve_scope.md` (PR012, íntegro; y PR011 vía lo que PR012
  reporta de él).

## 0. Pregunta científica

> Para sprinklings de Poisson cuyo dato observado es únicamente la clase de isomorfismo del poset
> inducido, ¿qué resultados permiten obtener cotas inferiores, cotas superiores uniformes o
> comparaciones de experimentos cuando `lambda -> infinito`, y cuánto se pierde al olvidar las
> etiquetas y la geometría continua?

## 1. Objetos, notación y régimen

### 1.1 Objetos

- **Parámetros geométricos `theta, theta'`.** Cada `theta` nombra una *completion*: un patch
  1+1D `(P_theta, g_theta)` con medida de volumen `vol(g_theta)` finita (FWP §1). Instancias
  internas de referencia: la familia diamante con esquinas EF fijas parametrizada por `tau`
  (WP4 §4) y los pares de Schwarzschild de FWP §2.
- **`X_{lambda,theta}` — experimento etiquetado.** Proceso de Poisson de intensidad
  `rho * vol(g_theta)` sobre `P_theta`, con media `lambda := rho * V_theta`,
  `V_theta := vol(g_theta)(P_theta)`; el observador ve la configuración **con posiciones**
  (coordenadas del continuo).
- **`Phi` — mapa olvidadizo.** Envía la configuración a la clase de isomorfismo del poset finito
  inducido por el orden causal. `Phi` borra etiquetas, posiciones y toda la estructura continua
  auxiliar.
- **`P_{lambda,theta}`** — ley de `X_{lambda,theta}`; **`Q_{lambda,theta} = Phi_# P_{lambda,theta}`**
  — ley order-only.
- **Canal `fixed_n`.** Ambos modelos condicionados a `N = n`; entonces los `n` puntos son iid de
  `vol(g_theta)/V_theta` (FWP Lemma 0). Notación `P^n_theta`, `Q^n_theta := Phi_# P^n_theta`.
  En patches que son cajas nulas, `Q^n_theta` depende de `theta` solo a través de la cópula
  `c_theta` (FWP Lemma 1).

### 1.2 La cardinalidad NO se olvida

`Phi` conserva `N` (el poset observado tiene `N` elementos). Consecuencia: en el canal Poisson
sin condicionar, `Q_{lambda,theta}` incluye la marginal `N ~ Poisson(rho * V_theta)`, y si
`V_theta != V_theta'` a `rho` conocida, esa marginal ya separa por sí sola (OP-1.2 §5; FWP
Remark A3). «Order-only» no significa «ciego a la cardinalidad». Todo enunciado buscado debe
declarar el canal: `fixed_n` (la carga recae íntegramente en el orden) o Poisson sin condicionar
(donde `N` es un confusor que puede fabricar separación trivial).

### 1.3 Tres modos de crecimiento de `lambda = rho * V`

1. **Alta densidad a volumen fijo** (`rho -> infinito`, patch fijo): el límite del continuo, el
   régimen relevante para el programa.
2. **Gran volumen a densidad fija** (`V -> infinito`, `rho` fijo): régimen termodinámico.
   **Excluido** salvo que la referencia traiga un paso de traducción explícito al modo 1.
3. **`fixed_n`, `n -> infinito`**: escalera de cardinalidad exacta; se conecta con el modo 1 vía
   el condicionamiento de FWP Lemma 0 y elimina el confusor de §1.2.

Una referencia solo cuenta como acierto en el régimen que declare; mezclar los tres modos sin
traducción es uno de los errores que esta ficha existe para evitar.

### 1.4 La información de Fisher no es un sustituto de TV

`I(theta)` entra solo así, y con estas hipótesis:

- Bajo QMD de la familia de cópulas (probada para la familia diamante: WP4 Prop 4),
  `H^2(c_theta, c_{theta+delta}) = (delta^2/4) I(theta) + o(delta^2)`, y de ahí **cotas
  superiores** de TV vía `TV <= H` y tensorización (WP4 §5). Nunca cotas inferiores del cociente.
- Sin QMD el vínculo se rompe: en la familia de caja EF fija el soporte se mueve, `H^2 >= c_1
  |delta|` (primer orden, WP4 Prop 2), `I` no está definida como forma cuadrática finita, y la
  escala natural de dos puntos es `1/n`, no `1/sqrt(n)` (WP4 Prop 3).
- `I > 0` tampoco es gratis: la familia de caja Kruskal fija tiene `I ≡ 0` exactamente
  (WP4 Prop 1) por ser la órbita de escala disfrazada.

Regla para la caza: una referencia que hable de Fisher solo es utilizable si declara (o permite
verificar) QMD u otra regularidad equivalente sobre nuestra clase de familias (§1.1), y aun
entonces solo aporta el lado superior.

### 1.5 Nota motivacional sobre `N_A` (delimitada; NO bibliográfica, NO antecedente del repo)

> En conversación se usó el número de Avogadro únicamente como ejemplo pintoresco de una media de
> Poisson macroscópica. `N_A` no tiene ningún papel fundamental conocido en causal set theory y
> no aparece en ningún documento del repo. El parámetro matemático relevante es `lambda = rho*V`,
> y lo científicamente importante que aquella conversación dejó es la obligación de distinguir
> los tres modos de §1.3 (gran volumen / alta densidad / cardinalidad exacta condicionada).
> Esta nota es motivación de la ficha, no una afirmación científica ni un resultado.

## 2. Estado interno: probado, numérico y abierto (qué no hay que buscar fuera)

Con etiquetas exactas de las fuentes; ninguna promoción de estatus se hace aquí.

- **[PROVED] Teorema A (FWP §2).** Par exacto `TV(Q^n_theta, Q^n_theta') = 0` para todo `n`:
  1+1D Schwarzschild `r_s` con patch `P` vs `s*r_s` con patch **co-escalado** `Phi_s(P)`
  (dilatación `Phi_s`, factor conforme constante, medida normalizada). El orden no lleva escala
  absoluta.
- **[PROSE-REMARK, promoción pendiente] Rigidez de cópulas (FWP §4).** En la clase de cajas
  nulas: misma cópula ⟹ isometría salvo constante global de escala; la clase `TV = 0` de una
  completion es exactamente su órbita de escala. Está enunciada y usada en prosa dentro del
  análisis del Attempt C; PR012 §2.1 la usa como hecho establecido y §9 pide promoverla a lema
  numerado con prueba propia. `[OPEN: promoción a lema]`
- **[PROVED] Cota superior fixed-`n` (WP4 §5).** Familia diamante:
  `TV(Q^n_tau, Q^n_{tau+delta}) <= (|delta|/2) * sqrt(n * Ibar)`, con QMD y `Ibar < infinito`
  probados (Lemma R, Prop 4) e inyectividad `tau -> c_tau` probada (Prop 5). Es una cota a `n`
  fijo condicionado `N = n`; **no** es un enunciado `lambda -> infinito`.
- **[PROVED (orden dominante)] Separación de la fracción de pares comparables (WP4 Anexo C, §2.2).**
  Familia diamante: `p(tau) = 1/2 + kappa(r_p,r_q)*tau*dv + O(dv^2)` con `kappa > 0`, luego
  `p(tau) != p(tau')`. Es el ingrediente 1 de §6 (separación de medias) para el candidato 7.1, no
  una cota de TV: `p` es un funcional de la cópula, y una separación de medias por sí sola **no**
  es una Forma L (§9.2, segundo guión). Incluye una reducción `[PROVED]` en forma cerrada de la
  integral cuádruple de concordancia a una doble, reutilizable para otros conteos.
- **[PROVED] Invariancia de forma (WP4 §5a, Prop 6).** `kappa = V * Ibar` es exactamente
  invariante por dilatación; el suelo `~ ell/sqrt(kappa)` depende solo de la forma del diamante.
  **[NUMERICAL, no probado]**: `kappa ~ 8e-4` para una forma de referencia (`delta_tau ~ 35 ell`)
  y degradación empírica `kappa ~ lambda_shape^6` al estrechar hacia el horizonte.
- **[PROVED] Canales separados (OP-1.2 §3, §5).** En 3+1D Schwarzschild, sector y forma de patch
  fijos: clase `TV = 0` a `fixed_n` = todo el intervalo de masas (co-escalado); en order+number
  con `rho` conocida, `TV = 0` iff `M = M'` (separa la marginal `N`); el canal identifica
  `rho*M^4`, no separa `rho` de `M`.
- **[PUBLICADO (PR011) / DRY-RUN PREVIEW (PR012)] Certificación numérica a `n` pequeño.** PR011
  publicó la cota naive `epsilon = 0.009223798457` a `n = 8`, `delta_tau = 0.1`. PR012 (borrador,
  no congelado; números de `--dry-run`, **no** certificación publicada, gate G2b abierto) prevé
  cotas tensorizadas `<= 0.0133` en los cuatro puntos certificados de la escalera
  (`delta_tau = 0.05` a `0.4`; los dos peldaños menores, `0.0125` y `0.025`, abstienen por
  resolución de grid, `GRID_RESOLUTION_ABSTAIN`, PR012 §4), es decir suelo minimax
  `~ 0.49–0.50` en esos puntos. Es evidencia numérica a `n = 8`; **no** es un
  teorema asintótico y no debe citarse como tal.
- **[OPEN — el hueco central] Distancias a nivel poset (WP4 §6.3; FWP Attempt C).** Todo el
  control de distancias está heredado del nivel puntual por data processing. No existe en el repo
  ninguna técnica para (a) acotar `TV(Q)` **por debajo**, ni (b) acotarla por arriba
  *estrictamente por debajo* de la cota puntual. Este hueco es exactamente lo que la búsqueda
  bibliográfica debe intentar cerrar.

## 2.1 Dos hallazgos externos verificados (2026-07-24, búsqueda bibliográfica, sin ejecución)

Ambos PDFs leídos íntegros y guardados en `biblioteca/` (`0902.0306v1.pdf`,
`1104.1039v3.pdf`). Ninguno de los dos cierra el hueco central por sí solo; cada uno recorta una
pieza concreta, con precisión sobre qué queda fuera.

**(A) Janson 2011, *Poset limits and exchangeable random posets* (arXiv:0902.0306, Teoremas 1.7,
1.8, 7.1; Lema 6.6; §6 "cut metric").** Da la **recíproca general** que OP-1.2 §7 marca
explícitamente como no usada («la recíproca general desde igualdad de todas las leyes finitas a
isomorfismo causal-medida») y que PR012 §9 pide para promover la rigidez de cópulas de FWP §4 a
lema citado:

- Teorema 7.1: para dos núcleos (`kernels`) `W_1` en `(S_1,mu_1,≺)` y `W_2` en `(S_2,mu_2,≺)`
  sobre espacios de Borel, son equivalentes: (i) los límites de poset coinciden,
  `Pi_{W_1} = Pi_{W_2}`; (ii) `t(Q,Pi_1) = t(Q,Pi_2)` para todo poset finito `Q` (igualdad de
  TODAS las densidades de subposet, para TODO tamaño); (iv) `P(n,W_1)` y `P(n,W_2)` tienen la
  misma ley **para todo `n` finito** (exactamente nuestra condición 2 de OP-1.2 §1: igualdad para
  todo `n`, no un `n` fijo); (vii) distancia de corte `delta_□(W_1,W_2) = 0`; y — solo bajo la
  hipótesis genérica adicional «`W_2` casi libre de gemelos» (ninguna condición de nuestros
  patches verificada contra esto todavía) — (ix) existe una biyección bimedible que preserva
  medida entre los dos espacios (módulo conjuntos nulos) tal que `W_1 = W_2` compuesto con ella.
  Esta última es la versión medida-teórica general, en cualquier espacio de Borel, del argumento
  diferencial-geométrico específico de Schwarzschild (isometría vía escalar de Ricci) que usa
  WP4 Prop 5 — **complementaria, no sustituta**: Janson no necesita estructura métrica ni
  ecuaciones de campo, pero exige la hipótesis de no-gemelos para la dirección (ix).
- Lema 6.6: `|t(Q,Pi_1) - t(Q,Pi_2)| <= m * delta_□(W_1,W_2)` (`m` = número de pares
  comparables en `Q`) — una cota **superior** explícita, misma familia que data processing;
  no da información nueva para el hueco central (Forma L).
- **Lo que NO da:** ni una tasa cuantitativa en TV a `n` fijo, ni un enunciado en el régimen
  `lambda -> infinito` de esta ficha — el teorema compara **el límite exacto sobre toda la
  escalera** (igualdad/desigualdad de leyes para todo `n` simultáneamente), un objeto distinto de
  `TV(Q^n)` a `n` fijo o de su asíntota en `n`. Útil para promover la rigidez de cópulas y para
  auditar el test de órbita (§4) con una herramienta general citada; no resuelve Forma L/U tal
  como se piden en esta ficha.
- Estado: `CONFIRMED_DIRECT` (verificado localmente, texto íntegro leído).

**(B) Reitzner–Schulte 2013, *Central limit theorems for U-statistics of Poisson point
processes* (Ann. Probab. 41(6), arXiv:1104.1039; Lema 3.5, Teoremas 4.7 y 5.2).** Da
exactamente el **ingrediente 2 de §6** (control de fluctuaciones) para el candidato 7.1 (número
de pares comparables), con una tasa explícita:

- Un `U`-estadístico de Poisson de orden `k=2`, `F = sum_{x!=y in eta} f(x,y)`, tiene fórmula
  exacta de varianza (Lema 3.5) y satisface (Teorema 4.7)
  `d_W((F - E F)/sqrt(Var F), N) <= 2*k^{7/2} * sum M_ij(f)/Var F`; si `f` es fijo,
  independiente de la intensidad `lambda` (Teorema 5.2), `d_W(...) <= C_f * lambda^{-1/2}` con
  `C_f` una constante que **no depende de lambda**.
- **Aplicación directa a 7.1:** tomando `X = [0,1]^2` en coordenadas de rango de la cópula,
  `mu_theta = lambda * c_theta` (intensidad de Poisson, `c_theta` la densidad normalizada de la
  cópula — nonatómica, hipótesis de Reitzner–Schulte §2.1 satisfecha) y `f(x,y) = 1[x prec y]`
  (el orden producto fijo en coordenadas de rango — **no depende de `theta` ni de `lambda`**),
  `S_lambda,theta := sum_{pares} f` (número de pares comparables observado, order-only: se lee
  del poset sin coordenadas) es un `U`-estadístico de orden 2 con kernel fijo. Teorema 5.2 da
  `d_W -> 0` a tasa `lambda^{-1/2}`, con la MISMA constante `C_f` para todo `theta` de la familia
  (el kernel no depende de `theta`).
- **Cálculo elemental restante (no en Reitzner–Schulte, aportado aquí, sin verificación por
  pares independiente):** por Mecke/primer-momento, `E_theta S = lambda^2 * p(theta)` con
  `p(theta) := int int f dc_theta dc_theta` (la `p(theta)` de §7.1, sin cambios); por Lema 3.5,
  `Var_theta S = Theta(lambda^3)` genéricamente (el término `i=1` domina). Cociente
  señal/ruido `~ lambda^{1/2} * (p(theta)-p(theta'))`, que diverge en el régimen 1.3-modo-1
  (`lambda -> infinito` a dominio fijo) **si y solo si** `p(theta) != p(theta')`.
- **Lo que esto cierra:** el ingrediente 2 de §6 para 7.1 completo, citado y con tasa explícita,
  uniforme en `theta`. **Lo que NO cerraba — el punto que faltaba:** `p(theta) != p(theta')`
  para el par concreto que se quiera usar (WP4 diamante, OP-1.1/1.2, u otro). Estaba
  `[OPEN por par]`; la inyectividad de `tau -> c_tau` (WP4 Prop 5) no implica la de
  `tau -> p(tau)`, y en la v3 no se había intentado ningún cálculo. **Resuelto en la v4 para la
  familia diamante — ver §2.2.** Para OP-1.1/1.2 y cualquier otra familia sigue `[OPEN por par]`:
  el cálculo del Anexo C es específico de la familia de WP4 §4.
- Estado: `CONFIRMED_DIRECT` (verificado localmente, texto íntegro leído; hipótesis §2.1 de
  Reitzner–Schulte — Borel, `mu` sigma-finita no atómica — comprobadas contra nuestra `c_theta`).

**Lectura conjunta.** (B) reduce el candidato 7.1 de «hace falta desarrollar máquinas de
momentos y CLT para conteos order-only» a «hace falta verificar una única desigualdad escalar,
`p(theta) != p(theta')`, para el par elegido» — el resto de la cadena (§6, pasos 2-4) queda
cubierto por un teorema citado con tasa explícita. Esa desigualdad era el siguiente paso natural,
y era un cálculo (no una ejecución ni una implementación de estimador). Se hizo: §2.2.

## 2.2 La desigualdad escalar, verificada (2026-07-25, cálculo propio, sin ejecución)

Fuente interna: `research_program/work_packages/wp4_comparable_pair_separation.md` (WP4 Anexo C),
con script de verificación `wp4_comparable_pair_separation_checks.py` (sympy + cuadratura
determinista + un cross-check Monte-Carlo con semilla fija; no importa nada de `nachocausal/`, no
toca umbrales, bandas de semillas ni artefactos de validación).

**Convención (una inconsistencia interna de esta ficha, ahora declarada).** §7.1 define `p(theta)`
como la probabilidad de que dos puntos iid sean **comparables**; §2.1(B) la define como
`int int 1[x prec y] dc dc`, que es **la mitad** (a.s. se cumple exactamente una de `x prec y`,
`y prec x`). El Anexo C calcula la de §7.1. El factor 2 es común a `theta` y `theta'`, luego no
afecta a la desigualdad; queda declarado para que las dos secciones no se lean como una
contradicción.

**Resultado.** Para la familia diamante de WP4 §4 (esquinas EF fijas `p=(v_p,r_p)`, `q=(v_q,r_q)`,
`0 < r_q < tau < r_p`, lapso nulo `dv := v_q - v_p`):

```text
p(tau) = 1/2 + kappa(r_p, r_q) * tau * dv + O(dv^2),
kappa(r_p, r_q) = [ (r_p^2 - r_q^2) - 2 r_p r_q log(r_p/r_q) ] / [ 12 r_p r_q (r_p - r_q)^2 ] > 0.
```

El término dominante es **estrictamente proporcional a `tau`**, luego `p(tau) != p(tau')` para
`tau != tau'` con `dv` pequeño. Positividad de `kappa` probada (con `x = r_p/r_q > 1`,
`phi(x) = (x-1/x)/2 - log x` cumple `phi(1)=0`, `phi' = (x-1)^2/(2x^2) > 0`). Verificado además
numéricamente en un par concreto (`r_p=3`, `r_q=0.5`, `tau=1.0` vs `tau'=1.2`).

**Pieza reutilizable (más allá de la desigualdad).** El Anexo C reduce en forma cerrada la integral
cuádruple de concordancia a una doble: el integral de un rayo nulo saliente vale
`rho(r_0,D)^2 - r_0^2 + tau*D`, de donde el volumen de cualquier sub-diamante
`J^+(x) ^ J^-(q)` es `rho(r_x,D)^2 + rho(r_q,-D)^2 - r_x^2 - r_q^2`. Esto sirve para cualquier
funcional de conteo de la familia, no sólo para `p`.

**Estados.** Reducción cerrada y lemas elementales: `[PROVED]` (identidades verificadas
simbólicamente; reducción corroborada por dos rutas numéricas independientes). Asintótica y
positividad: `[PROVED (orden dominante)]`, con dos pasos declarados como argumentados y no
escritos (analiticidad en `dv` en `0^+`; uniformidad en `tau` del resto `O(dv^2)`) y con `dv_0` no
efectivo. El par concreto: `[NUMERICAL]` a precisión de trabajo.

**Test de la órbita (§4), obligatorio, pasado.** `p` es exactamente un funcional de la cópula
(`p = (1 + tau_K(c_tau))/2`, con `tau_K` la tau de Kendall), luego es ciego a la órbita de escala
del Teorema A por construcción — verificado numéricamente a `< 1e-15` bajo la dilatación conjunta.
Un candidato a Forma L que separase un par del Teorema A sería inválido por §4; este no puede.

**Lo que NO cierra — y el obstáculo se ha desplazado al canal.** Forma L sigue `[OPEN]`. Cuatro
puntos (Anexo C §5, con detalle):

1. La CLT de Reitzner–Schulte vive en el canal **Poisson sin condicionar**, y esta familia tiene
   volumen dependiente de `tau` (`V(1.0) = 11.501608349297` vs `V(1.2) = 10.794261266781` a
   `dv = 4`). Con `rho` conocida la marginal `N` separa **por sí sola**: exactamente el mecanismo
   trivial que §1.2 y §9.2 prohíben contar.
2. El canal honesto es `fixed_n`, y allí la CLT importada no aplica tal cual: falta un paso de
   des-Poissonización que Reitzner–Schulte no da. `[OPEN]`
3. La no degeneración de la varianza a `fixed_n` (`Var S_n = Theta(n^3)`, i.e. proyección de
   Hoeffding `h_1` no constante) **no se calculó**, aunque es computable con la misma maquinaria
   del Anexo C §3. `[OPEN]`
4. El chequeo obligatorio de §6.4 pasa **sólo a nivel de tasas** (ambos umbrales en
   `delta ~ n^{-1/2}`, sin contradicción con la cota superior probada de WP4 §5, y — condicional
   al punto 3 — el conteo de pares sería óptimo en tasa frente a ese suelo). El chequeo a nivel de
   **constantes** no se hizo: compara `kappa*dv` con `sqrt(zeta_1 * Ibar)`, y no se dispone de
   `Ibar` para estas esquinas (WP4 §5a sólo tiene `V*Ibar` `[NUMERICAL]`, para una forma de
   referencia) ni de `zeta_1`. `[OPEN]`

## 3. Las tres formas de resultado buscadas

La búsqueda NO se reduce a la Forma L: una Forma U rigurosa resolvería una parte igual de central
de la pregunta. Las tres se registran por separado y un acierto se clasifica en una sola.

### Forma L — cota inferior / recuperabilidad

```text
TV( Q_{lambda,theta}, Q_{lambda,theta'} ) >= f_lambda(theta, theta')
```

con un régimen (§1.3, declarado) en el que `f_lambda -> 1`, o al menos `f_lambda >= f_0 > 0`
uniformemente. Interpretación: el orden no etiquetado conserva señal suficiente para distinguir
los parámetros (versión fuerte: test consistente; versión débil: separación no evanescente).

### Forma U — cota superior uniforme / barrera de identificabilidad

```text
sup_lambda TV( Q_{lambda,theta}, Q_{lambda,theta'} ) <= c < 1
```

para algún par `theta != theta'` **no** relacionado por la órbita de §4, o una cota que tienda a
cero. Interpretación: barrera permanente o no-identificabilidad asintótica en el canal order-only
— un no-go tan valioso como la Forma L, y el único desenlace que convertiría los suelos
numéricos de PR011/PR012 en fenómeno estructural.

### Forma D — comparación de experimentos

Deficiencia o distancia de Le Cam entre el experimento etiquetado `E_lambda = (P_{lambda,theta})`
y el order-only `F_lambda = (Q_{lambda,theta})`. Precisión necesaria: como `Q = Phi_# P` con
`Phi` determinista, la dirección `E -> F` es gratis (`delta(E,F) = 0`); la cantidad informativa
es la **inversa**, `delta(F,E)`: cuánto pierde quien solo ve el poset.

**Puentes D → L/U, con sus hipótesis adicionales explícitas:**

- Si `delta(F_lambda, E_lambda) -> 0` (equivalencia asintótica) **y además** el experimento
  etiquetado separa (`TV(P_{lambda,theta}, P_{lambda,theta'}) -> 1`, cierto para pares fijos
  distintos con gap de cópula `h_0 > 0` por tensorización, FWP §4), entonces
  `TV(Q) >= TV(P) - 2*delta -> 1` (elemental desde la definición de deficiencia: el riesgo del
  test binario, `1 - TV`, se desplaza a lo sumo `2*delta` con pérdidas acotadas por 1): la
  Forma D fuerte ⟹ Forma L. Sin la segunda hipótesis no implica nada.
- `delta(F,E)` acotada inferiormente **no** implica Forma U: que el observador order-only no
  pueda simular el experimento etiquetado no impide que `TV(Q) -> 1` por otra vía. La Forma U
  exige una cota superior directa sobre `TV(Q)`.

## 4. Test obligatorio de la órbita (detector de errores)

**Principio.** Si dos modelos están relacionados por una biyección bimedible (módulo nulos) que
empuja la medida de muestreo normalizada de uno a la del otro y preserva la relación causal para
casi todo par, entonces las leyes de posets no etiquetados coinciden a todo `n` y la TV
order-only es exactamente cero (OP-1.2 §2, lema suficiente).

**El caso de escala, formulado con cuidado.** NO toda «transformación de escala» preserva el
experimento; las condiciones precisas, según la fuente interna que las prueba, son:

- dilatación `Phi_s` **con patch co-escalado** `P -> Phi_s(P)`, factor conforme constante (que no
  altera la causalidad) y medida **normalizada** (que cancela el `s^2` de volumen), en canal
  `fixed_n` o cociente equivalente — entonces `TV(Q^n) = 0` exacto (FWP Teorema A; versión 3+1D
  con co-escalado de masa y patch Kruskal: OP-1.2 §3);
- en el canal Poisson sin condicionar, el mismo par se separa a través de la marginal `N`
  (§1.2) — la órbita es `TV = 0` **solo** en el canal que quita o cociente la cardinalidad;
- «patch fijo + parámetro móvil» NO es la órbita, y equivocarse aquí tiene dos modos de fallo ya
  documentados: caja Kruskal fija = órbita disfrazada (`I ≡ 0`, WP4 Prop 1: cero señal donde se
  esperaba señal) y caja EF fija = familia no regular (`H^2` de primer orden, WP4 Prop 2: más
  señal de la que QMD permite). La pertenencia a la órbita se decide comparando cópulas /
  medidas normalizadas, nunca leyendo la descripción coordenada.

**Uso como detector, en ambas direcciones:**

- una supuesta cota inferior (Forma L) que sea estrictamente positiva sobre un par cuya ley
  order-only coincide (p. ej. un par de Teorema A) es **inválida**: o el resultado está mal, o
  sus hipótesis excluyen ese par y la incompatibilidad debe declararse por escrito al fichar la
  referencia;
- una supuesta barrera (Forma U) que se aplique también a pares fuera de la órbita con separación
  ya probada en algún canal más rico debe declarar el canal exacto, o es sospechosa de estar
  probando otra cosa.

## 5. La asimetría central: cuantificar la contracción de `Phi`

Por data processing (`Phi` determinista):

```text
TV( Q_{lambda,theta}, Q_{lambda,theta'} ) <= TV( P_{lambda,theta}, P_{lambda,theta'} ).
```

Las cotas superiores del experimento completo se heredan al order-only; **la dirección inferior
no se hereda**. El Teorema A es el ejemplo extremo interno: para `s != 1` los patches `P` y
`Phi_s(P)` difieren como conjuntos (elemental: un patch compacto con `r` acotado lejos de `0` no
puede ser `Phi_s`-invariante para `s != 1`), de modo que el experimento etiquetado los separa
(gap de Hellinger a una muestra `> 0` sobre la diferencia simétrica, que tensoriza:
`TV(P^n) -> 1` en `n`), mientras
`TV(Q^n) = 0` exactamente para todo `n`. La contracción puede ser **total**: de separación
perfecta a información cero.

El problema central de la ficha es, pues, el comportamiento del déficit

```text
D_Phi(theta, theta'; lambda) := TV(P_{lambda,theta}, P_{lambda,theta'})
                              - TV(Q_{lambda,theta}, Q_{lambda,theta'}) >= 0
```

en el régimen declarado. El único esquema general de cota inferior disponible es el de
estadísticos (§6): para todo funcional order-only `T` (invariante por isomorfismo, luego `T`
factoriza a través de `Phi`),

```text
TV( Q_{lambda,theta}, Q_{lambda,theta'} ) >= TV( L_theta(T), L_{theta'}(T) ),
```

data processing aplicado en la dirección correcta: `T` es función del poset, luego su ley es un
push-forward de `Q`. Toda la vía §6-§7 consiste en hacer computable el miembro derecho.

## 6. Auditoría de la vía Last–Penrose / Malliavin–Stein

**Qué dan realmente esos teoremas (delimitación).** La maquinaria Malliavin–Stein sobre el
espacio de Poisson (fórmulas de Mehler, desigualdades de Poincaré de segundo orden, cotas tipo
Berry–Esseen) produce **aproximación normal (o Poisson) cuantitativa para un funcional `F` bajo
UNA ley fija**: cotas sobre `d(F_lambda normalizado, N(0,1))` en Wasserstein/Kolmogorov/TV cuando
`lambda -> infinito`. NO produce por sí sola comparaciones entre las leyes de `F` bajo dos
parámetros `theta != theta'`, ni cotas inferiores de TV entre experimentos. Presentarla como
solución directa sería convertir una herramienta en un resultado. `[género herramienta, no
solución — estado por fuente en §8; la aplicabilidad a funcionales order-only causales es
justamente lo que hay que buscar]`

**La cadena completa que haría falta, escrita entera.** Para un estadístico order-only `T` y el
régimen declarado:

1. **Separación de medias:** asintótica de `Delta_mu(lambda) := E_theta T - E_theta' T`, con
   `Delta_mu != 0` verificado para el par concreto (no se sigue de inyectividad de la familia:
   que `c_theta` sea inyectiva (WP4 Prop 5) no implica que el funcional unidimensional
   `theta -> E_theta T` sea inyectivo). `[hueco por candidato, §7]`
2. **Control de fluctuaciones:** asintótica de `sigma^2_theta(lambda) = Var_theta T` (aquí sí:
   Poincaré / segundo orden, Last–Penrose).
3. **Conversión en cota TV, con honestidad sobre qué da cada nivel de control:**
   - *Solo dos momentos:* si `Delta_mu / max(sigma_theta, sigma_theta') -> infinito`, Chebyshev a
     ambos lados del punto medio da `TV(L_theta(T), L_theta'(T)) >= 1 - 8*sigma^2/Delta_mu^2 -> 1`
     (derivación de una línea: cada cola en el punto medio es `<= 4*sigma^2/Delta_mu^2`;
     desigualdades TV estándar, Tsybakov §2.4 `[UNVERIFIED, estándar]`) (Forma L fuerte). Si el cociente se queda acotado, **dos momentos no dan nada decisivo**:
     medias y varianzas distintas son compatibles con TV arbitrariamente pequeña sin control
     adicional de las distribuciones.
   - *Con aproximación normal (Malliavin–Stein):* si ambas leyes están a distancia `<= eps_lambda`
     de gaussianas explícitas, `TV(L_theta(T), L_theta'(T)) >= TV(N(mu_theta,sigma^2),
     N(mu_theta',sigma'^2)) - 2*eps_lambda` (desigualdad triangular de TV) — una Forma L débil (`f_0 > 0`) incluso con cociente
     señal/ruido acotado, siempre que `eps_lambda` sea de orden menor que el efecto.
   - *Anti-concentración:* para estadísticos de valores enteros (conteos) en regímenes sin CLT,
     haría falta control de átomos; sin él, ni siquiera el paso Chebyshev es citable con TV.
4. **Chequeo de consistencia interna:** el miembro derecho nunca puede superar las cotas
   superiores ya probadas. A `n` fijo en la familia diamante,
   `TV(L(T)) <= TV(Q^n) <= (|delta|/2)sqrt(n*Ibar)` (WP4 §5): un candidato cuyo cálculo de
   momentos «supere» esa cota está mal calculado. En Poisson sin condicionar, comprobar que la
   separación no viene solo de `N` (§1.2).

**Qué pedirle exactamente a la literatura en este coto:** teoremas de media/varianza/CLT para
funcionales **invariantes por isomorfismo de orden** de muestras Poisson o iid en dimensión 2
(conteos de pares comparables, cadenas, intervalos), con constantes o tasas dependientes de la
densidad subyacente — es decir, los ingredientes 1–3 para los candidatos de §7, no un teorema
genérico de normalidad.

## 7. Estadísticos candidatos order-only

Regla de la sección: no se añaden candidatos nuevos salvo justificación de que los existentes no
cubren la función; los cuatro de abajo cubren las tres escalas naturales (funcional promedio de
orden 2, extremal global, conteos locales de todo orden) y el agregado físico estándar.

### 7.1 Número de relaciones / fracción de pares comparables `S_n`

1. *Order-only:* sí — invariante por isomorfismo.
2. *Régimen:* definido en los tres modos de §1.3.
3. *Resultado necesario:* `E S_n = C(n,2) * p(theta)` con `p(theta)` = probabilidad de que dos
   puntos iid de `c_theta` sean comparables (funcional de la cópula; en cajas nulas, comparable
   ⟺ concordancia de rangos). **Ingrediente de varianza/CLT ahora `CONFIRMED_DIRECT`**: en el
   canal Poisson (`lambda -> infinito`, modo 1 de §1.3), Reitzner–Schulte 2013 (arXiv:1104.1039,
   Lema 3.5 + Teoremas 4.7/5.2 — ver §2.1(B)) da la fórmula exacta de varianza y
   `d_W((S-ES)/sqrt(Var S), N) <= C_f * lambda^{-1/2}`, con `C_f` uniforme en `theta` (el kernel
   comparabilidad `f = 1[x prec y]` no depende de `theta` ni de `lambda`). Con eso,
   `Var_theta S = Theta(lambda^3)` (elemental por Mecke, no en la fuente), luego el cociente
   señal/ruido `Delta_mu/sigma ~ sqrt(lambda)*(p(theta)-p(theta'))` diverge en `lambda`.
   **Ingrediente (a) — `p(theta) != p(theta')` — `CERRADO para la familia diamante de WP4 §4`**
   (§2.2; `[PROVED (orden dominante)]` vía `p = 1/2 + kappa*tau*dv + O(dv^2)` con `kappa > 0`, más
   verificación `[NUMERICAL]` en un par concreto). Para otras familias (OP-1.1/1.2, etc.) sigue
   `[OPEN por par]`. **Importante:** con (a) cerrado, §6.3 **no** da todavía Forma L fuerte — el
   obstáculo restante es el canal, no la separación de medias: ver §2.2, puntos 1-4 (marginal `N`
   como confusor en Poisson sin condicionar, des-Poissonización a `fixed_n`, varianza no
   calculada, chequeo de §6.4 sólo a nivel de tasas).
4. *Confusores:* la media depende cuadráticamente de la cardinalidad (en Poisson sin condicionar,
   `N` domina — usar `fixed_n` o normalizar); forma del patch y borde entran vía la cópula; la
   escala NO es confusor (funcional de cópula ⟹ pasa el test §4 automáticamente).
5. *Puede dar:* Forma L (sigue siendo la ruta más corta; con (B) de §2.1 y (a) cerrado por §2.2,
   los huecos restantes son de canal, no de señal). La rama «si `p(theta) = p(theta')` el candidato
   es ciego para ese par» queda **descartada para la familia diamante**: `kappa > 0` estrictamente,
   luego el estadístico nunca es ciego ahí.

### 7.2 Altura `H_n` (cadena más larga)

1. *Order-only:* sí.
2. *Régimen:* definido en los tres modos.
3. *Resultado necesario:* en cajas nulas, `H_n` = subsecuencia creciente más larga (LIS) de la
   permutación de rangos de la cópula. Se necesita: ley de grandes números
   `H_n / sqrt(n) -> c(theta)` para muestras de densidad no uniforme, separación
   `c(theta) != c(theta')`, y fluctuaciones `o(sqrt(n))` (en el caso uniforme, `n^{1/6}`
   Tracy–Widom `[UNVERIFIED]`). Con eso, §6.3 da Forma L fuerte.
4. *Confusores:* `c(theta)` es un funcional variacional grueso de la densidad — puede coincidir
   entre pares que la cópula distingue `[OPEN por par]`; sensible al borde del patch (la cadena
   maximal corre esquina a esquina); invariante de escala ⟹ pasa §4.
5. *Puede dar:* Forma L; obstáculo principal: la teoría de fluctuaciones para densidades no
   uniformes no es estándar `[UNVERIFIED]`.

### 7.3 Conteos de intervalos `N_k` (abundancias de `k`-intervalos)

1. *Order-only:* sí — son invariantes de isomorfismo.
2. *Régimen:* definidos en los tres modos.
3. *Resultado necesario:* medias y varianzas conjuntas de U-estadísticos de orden `k+2` bajo
   `c_theta`, con separación de medias para el par. Misma estructura que 7.1 con confusores
   añadidos por el orden del estadístico.
4. *Confusores:* fuerte dependencia en densidad/cardinalidad y en el borde; en el continuo los
   `N_k` son la entrada de la acción BD (7.4).
5. *Puede dar:* Forma L por la misma vía que 7.1; interés adicional: un vector `(N_0..N_k)` da
   más direcciones para lograr separación de medias cuando un solo escalar es ciego.

### 7.4 Acción de Benincasa–Dowker (combinación fija de `N_k`)

1. *Order-only:* sí (combinación lineal de 7.3 con coeficientes universales).
2. *Régimen:* definida; su interés físico está en `rho -> infinito`.
3. *Resultado necesario:* media (límite continuo: literatura CST sobre la acción discreta
   `[UNVERIFIED contra biblioteca/ — verificar antes de usar]`) y, crucialmente, varianza: la
   preocupación conocida en la comunidad es que las fluctuaciones de la acción BD **no** decaen
   sin suavizado (smearing `eps`) `[UNVERIFIED]`. Si `Var` no decae frente a `Delta_mu`, la vía
   §6.3-dos-momentos no cierra.
4. *Confusores:* términos de frontera pueden dominar la media; parámetro de no-localidad `eps`;
   dimensión.
5. *Puede dar:* en el mejor caso Forma L débil; hasta que la varianza esté controlada, solo
   evidencia auxiliar. No es la primera opción — 7.1 domina en tratabilidad.

## 8. Tabla de referencias externas

Estados usados (definición local de esta ficha):

- `CONFIRMED_DIRECT` — fuente primaria leída y verificada localmente (WP4 §9), y su enunciado
  toca directamente la pregunta de §0. **No** implica que la resuelva.
- `CONFIRMED_TOOL_ONLY` — leída/verificada localmente; aporta maquinaria, no un resultado sobre
  la pregunta.
- `POSSIBLE_BRIDGE` — ruta plausible declarada hacia L/U/D; hipótesis aún sin verificar.
- `NOT_APPLICABLE` — clasificada fuera de régimen/canal para §0; se conserva como contraste.
  Si la clasificación descansa en caracterización estándar no verificada localmente, se añade
  `UNVERIFIED`.
- `UNVERIFIED` — citada de memoria o como estándar; sin verificación local. Ninguna afirmación
  de esta ficha depende de ellas.

| Referencia | Objeto probabilístico | Dato observado | Régimen | Distancia controlada | Dirección | Hipótesis clave | Aplicación L/U/D | Obstáculo pendiente | Estado |
|---|---|---|---|---|---|---|---|---|---|
| Braun 2025 (arXiv:2507.01907; local, WP4 §9) | leyes de matrices de adyacencia `C^k`, todo `k` | **etiquetado**, order+number | volumen igual, `d >= 3` | igualdad exacta de leyes | identificabilidad exacta (sabor L, nivel etiquetado) | causal continuity, chronocompleteness, `d>=3` | L (etiquetado); su Rmk 3.10: el caso no etiquetado = conjetura de Bombelli, **abierta** — nuestra pregunta con nombre propio | quitar etiquetas; `d=2` excluida (la rigidez HKMM falla, FWP Lemma 1) | `CONFIRMED_DIRECT` |
| Müller 2025 (arXiv:2503.01719; local, WP4 §9) | leyes `K`-punto del orden, invariantes por permutación | no etiquetado (fixed `K`) | pares dependientes de `K` (`v ~ log(1/eps)/K`) | `L^1` entre leyes `K`-punto vs `d^-` geométrica | sabor U: leyes cercanas, geometría lejana | slabs de volumen unidad; bump conforme | U (técnica de bump = candidata a barrera por construcción) | no uniforme en `lambda` para par fijo; target = diámetro, no horizonte | `CONFIRMED_DIRECT` |
| Madsen 2026 (arXiv:2607.05840; local, WP4 §9) | embeddings de causal sets | order + volumen + cadenas | alta densidad | isometría aproximada (`eps -> 0`) | sabor D: qué compra el dato extra | embedding «well-conditioned», glob. hiperbólico | D (cuantifica la brecha entre order-only y order+volumen+cadenas) | canal más rico que el nuestro; no da `delta(F,E)` | `CONFIRMED_DIRECT` |
| Boguñá–Krioukov 2024 (PRD 110, 024008; local, WP4 §9) | estimador de distancias espaciales por solapes causales | order + cardinalidad | `rho -> infinito`, Minkowski | error relativo `~1/sqrt(rho V)` | lado alcanzabilidad (upper-bound-side) | flatness local | auxiliar (contraste de canales) | sin cotas inferiores; canal y target distintos | `NOT_APPLICABLE` (leída local) |
| Höpfner 2014 (biblioteca local, WP4 §8) | familias QMD, contigüidad | genérico iid | asintótica local | `H^2`, contigüidad | superior (vía `TV <= H`) | QMD | herramienta para L/D | nada sobre no etiquetado | `CONFIRMED_TOOL_ONLY` |
| van der Vaart 1998, Lemma 7.6; Tsybakov 2009 §2.4 | criterio QMD; método de dos puntos | genérico | asintótica local / `n` fijo | `H`, TV | superior | estándar | herramienta | sin copia local verificada | `UNVERIFIED` (estándar) |
| Last–Penrose (*Lectures on the Poisson Process*; maquinaria general detrás de Reitzner–Schulte) | funcionales de Poisson, expansión de Wiener–Itô | funcional `F` bajo UNA ley | `lambda -> infinito` | `d_W` a la gaussiana límite | aproximación, no comparación | momentos/diferencias de `F` | ingrediente de fondo de Reitzner–Schulte (fila siguiente) | no compara `theta` vs `theta'` directamente | `CONFIRMED_TOOL_ONLY` (citado dentro de Reitzner–Schulte §2.3, no leído aparte) |
| **Reitzner–Schulte 2013** (Ann. Probab. 41(6); arXiv:1104.1039, local `biblioteca/1104.1039v3.pdf`; Lema 3.5, Teoremas 4.7/5.2) | U-estadísticos de orden `k=2` de procesos de Poisson | conteo order-only de pares comparables (candidato 7.1) | `lambda -> infinito`, dominio fijo (modo 1 de §1.3) | `d_W` a `N(0,1)`, tasa explícita `<= C_f*lambda^{-1/2}` | fluctuaciones (ingrediente 2 de §6), **con tasa citada** | `mu` Borel no atómica (✓ para `c_theta`); `f` fijo, independiente de `lambda`/`theta` (✓ para `f=1[x prec y]`) | puente a Forma L vía §6.3, ver §2.1(B) | `p(theta) != p(theta')` ya **no** es el obstáculo: cerrado para la familia diamante (§2.2). Lo pendiente es el canal — su CLT es Poisson sin condicionar, donde la marginal `N` separa sola (§2.2 punto 1); a `fixed_n` falta des-Poissonización (punto 2) | `CONFIRMED_DIRECT` (verificado localmente 2026-07-24) |
| Deuschel–Zeitouni 1995 (LIS de puntos iid no uniformes) | subsecuencia creciente más larga | permutación de rangos (order-only) | `n -> infinito` | LLN variacional de la media | medias (ingrediente 1 para 7.2) | densidad regular en el plano | puente a L vía 7.2 | fluctuaciones no uniformes; separación `c(theta)!=c(theta')` | `POSSIBLE_BRIDGE` / `UNVERIFIED` |
| Baik–Deift–Johansson 1999 | fluctuaciones LIS caso uniforme | permutación de rangos | `n -> infinito` | `n^{1/6}`, Tracy–Widom | fluctuaciones (ingrediente 2 para 7.2) | uniformidad | puente a L | extensión a densidades generales | `POSSIBLE_BRIDGE` / `UNVERIFIED` |
| **Janson 2011** (arXiv:0902.0306, local `biblioteca/0902.0306v1.pdf`; Teoremas 1.7, 1.8, 7.1, Lema 6.6) | límites de posets intercambiables, núcleos (`kernels`) | igualdad de leyes de poset **para todo `n`** (no `n` fijo) | régimen «toda la escalera» (no `lambda`/`n` fijo de esta ficha) | distancia de corte `delta_□`; cota `\|t(Q,·)-t(Q,·)\| <= m*delta_□` | recíproca general (Teo. 7.1) + cota superior (Lema 6.6, misma familia que data processing) | espacios de Borel; hipótesis extra «casi libre de gemelos» solo para la dirección de isomorfismo (ix), no verificada contra nuestros patches | promueve la rigidez de cópulas (FWP §4) a lema citado, ver §2.1(A); no da Forma L/U en el régimen de esta ficha | régimen «todo `n`» distinto de `n` fijo o `lambda->infinito`; hipótesis de no-gemelos sin chequear | `CONFIRMED_DIRECT` (verificado localmente 2026-07-24; supera el `UNVERIFIED` de la v2, snapshot no leído entonces) |
| Kleitman–Rothschild | poset uniforme aleatorio | posets no etiquetados | conteo asintótico | estructura típica (3 niveles) `[UNVERIFIED]` | — | uniformidad sobre TODOS los posets | ninguna: clase de universalidad equivocada (nuestros posets son órdenes 2D de medidas) | — | `NOT_APPLICABLE` (contraste) / `UNVERIFIED` local |

## 9. Criterios de cierre de la búsqueda

### 9.1 Una referencia cuenta como ACIERTO solo si

- trabaja directamente con órdenes aleatorios, clases de isomorfismo, observaciones cociente o
  pérdida de etiquetas — o proporciona un teorema transferible con TODAS las hipótesis
  verificables contra §1.1–§1.3;
- produce una cota cuantitativa en TV, Hellinger, KL, riesgo de test o deficiencia que se
  conecte rigurosamente con TV (con las desigualdades estándar declaradas);
- declara (o permite identificar) su régimen en los términos de §1.3;
- pasa el test de la órbita (§4);
- no depende de ground truth geométrico inaccesible al observador order-only (posiciones,
  marginales, emparejamientos, volumen absoluto con `rho` desconocida).

### 9.2 NO basta (lista de descarte rápido)

- convergencia de un único observable sin control de separación entre los dos parámetros
  (ingrediente 1 de §6 ausente);
- diferencia de medias aislada, sin varianzas ni aproximación distribucional (§6.3);
- información de Fisher sin regularidad QMD verificable (§1.4);
- cotas del experimento etiquetado usadas como si fueran cotas inferiores del cociente (§5:
  la dirección inferior no se hereda — el error simétrico al legítimo `TV(Q) <= TV(P)`);
- evidencia numérica tipo PR011/PR012 (n pequeño, dry-run) presentada como teorema asintótico;
- el fracaso de varios observables concretos interpretado como no-go universal (la Forma U exige
  una cota sobre TODO el canal, no sobre una lista de estadísticos).

## 10. Cotos de caza (uno cada vez, en este orden)

El orden prioriza la ruta con la cadena §6 más corta. Nota: WP4 §9 ya contiene una primera
pasada verificada (Braun/Müller/Madsen/Boguñá-Krioukov, filas 1–4 de §8); no repetirla.

1. **Malliavin–Stein sobre el espacio de Poisson** (Last–Penrose como puerta; Reitzner–Schulte
   para U-estadísticos): busca los ingredientes 2–3 de §6 para los candidatos 7.1/7.3. Primer
   objetivo concreto: ¿hay tratamiento publicado de conteos de pares comparables / intervalos
   para muestras de densidad no uniforme en 2D?
2. **Línea LIS / récords** (Deuschel–Zeitouni; Baik–Deift–Johansson y sucesores): ingredientes
   1–2 para el candidato 7.2 con densidades no uniformes.
3. **Límites de posets y la conjetura de Bombelli** (Janson; literatura que cite Braun 2025
   Rmk 3.10): el marco de la Forma D y el estado del problema no etiquetado con nombre propio.
4. **Estadística de procesos puntuales parcialmente observados / datos unlabeled**: por si la
   comunidad estadística ya cuantificó la pérdida por olvido de etiquetas en otro vestido.

Contraste permanente (no coto): Kleitman–Rothschild, solo para reconocer la clase de
universalidad equivocada.
