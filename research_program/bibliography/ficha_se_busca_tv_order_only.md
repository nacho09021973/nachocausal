# Ficha «SE BUSCA» — identificabilidad order-only en variación total (especificación de búsqueda bibliográfica)

**Estado:** `BORRADOR / EXPLORACION` (v2, 2026-07-24; v1 del mismo día, sustituida). No es un
documento congelado; no autoriza preregistros, ejecuciones ni implementaciones. Su única función:
especificar la búsqueda bibliográfica con precisión suficiente para (a) dirigir cada disparo y
(b) reconocer un acierto — o descartar un falso positivo — con criterios escritos de antemano.

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
   ⟺ concordancia de rangos). Hace falta: (a) `p(theta) != p(theta')` para el par — **no
   probado; no se sigue de Prop 5** `[OPEN por par]`; (b) varianza de U-estadístico (clásico
   Hoeffding a `n` fijo; en Poisson, U-estadísticos de Poisson vía Malliavin–Stein). Si (a) vale,
   el cociente señal/ruido crece como `sqrt(n)*|Delta_p|` y §6.3 da Forma L fuerte.
4. *Confusores:* la media depende cuadráticamente de la cardinalidad (en Poisson sin condicionar,
   `N` domina — usar `fixed_n` o normalizar); forma del patch y borde entran vía la cópula; la
   escala NO es confusor (funcional de cópula ⟹ pasa el test §4 automáticamente).
5. *Puede dar:* Forma L (la ruta más corta si (a) se verifica); si `p(theta) = p(theta')`, el
   candidato es ciego para ese par y solo queda como evidencia auxiliar.

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
| Last–Penrose (*Lectures on the Poisson Process*) | funcionales de Poisson, Malliavin–Stein | funcional `F` bajo UNA ley | `lambda -> infinito` | `d_W/d_K/d_TV` **a la gaussiana límite** | aproximación, no comparación | momentos/diferencias de `F` | ingrediente 2–3 de §6 para 7.1/7.3 | no compara `theta` vs `theta'`; aplicabilidad a funcionales de orden por comprobar | `POSSIBLE_BRIDGE` / `UNVERIFIED` local |
| Reitzner–Schulte (U-estadísticos de Poisson, Malliavin–Stein) | U-estadísticos de procesos de Poisson | conteos tipo 7.1/7.3 | `lambda -> infinito` | CLT cuantitativo | fluctuaciones (ingrediente 2) | núcleos `L^2` | puente a L vía §6.3 | separación de medias (ingrediente 1) no incluida | `POSSIBLE_BRIDGE` / `UNVERIFIED` |
| Deuschel–Zeitouni 1995 (LIS de puntos iid no uniformes) | subsecuencia creciente más larga | permutación de rangos (order-only) | `n -> infinito` | LLN variacional de la media | medias (ingrediente 1 para 7.2) | densidad regular en el plano | puente a L vía 7.2 | fluctuaciones no uniformes; separación `c(theta)!=c(theta')` | `POSSIBLE_BRIDGE` / `UNVERIFIED` |
| Baik–Deift–Johansson 1999 | fluctuaciones LIS caso uniforme | permutación de rangos | `n -> infinito` | `n^{1/6}`, Tracy–Widom | fluctuaciones (ingrediente 2 para 7.2) | uniformidad | puente a L | extensión a densidades generales | `POSSIBLE_BRIDGE` / `UNVERIFIED` |
| Janson 2011 (arXiv:0902.0306, poset limits) | límites de posets intercambiables | posets no etiquetados | `n -> infinito` | convergencia de densidades de subposets | representación/límite, sin tasas | intercambiabilidad | herramienta para D (marco del experimento límite) | sin TV cuantitativa | `UNVERIFIED` (snapshot local sin verificar, OP-1.2 §9) |
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
