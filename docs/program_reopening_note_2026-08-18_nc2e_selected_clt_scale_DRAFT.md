# Nota de alcance `NC-2E` — escala de varianza seleccionada

```text
ESTADO: FIRMADA / EJECUTADA / NC2E_PARTIAL_RELATIVE_VARIANCE_REDUCTION
FECHA_BORRADOR: 2026-08-18
FECHA_FIRMA: 2026-08-18
REQUIERE_FIRMA_NUEVA_DEL_PI: CUMPLIDO
PREDECESOR: NC-2D / NC2D_PARTIAL_RELATIVE_MOMENT_REDUCTION
USA: emergencia/P1a_count_volume_selected_second_moment_d2.md
USA: emergencia/P1a_count_volume_selected_interior_mass_d2.md
USA: emergencia/P1a_count_volume_beta_uniform_scaling_d2.md
USA: emergencia/P1a_count_volume_lema_kl_d2.md
NO_MODIFICA: PR #7
NO_REVOCA: docs/program_closure_note_2026-07-30.md
NO_REABRE: EF-0--EF-8, reconstruccion de horizonte ni d>=3
SELLO: intacto — no se toca
SEMILLAS: ninguna
```

## 1. Motivo y precedencia

`NC-2D` probó, para ambos lados y todo `n>=10^40`,

\[
\mathbb E[(Z_{n,h}-1/2)^2\mid n,h,S]
\le700n^{-1/5}\log n,
\qquad
Z_{n,h}=\frac{q_{n,h}}{n+1},
\tag{1.1}
\]

y, mediante el reescalado exacto

\[
\operatorname{Var}(q_{n,h}\mid n,h,S)
=(n+1)^2\operatorname{Var}(Z_{n,h}\mid n,h,S),
\tag{1.2}
\]

obtuvo únicamente

\[
\operatorname{Var}(q_{n,h}\mid n,h,S)
\le2800n^{9/5}\log n.
\tag{1.3}
\]

La cota (1.3) no es una vía independiente respecto de (1.1). La brecha entre la
cota demostrada y la escala requerida por `NC2D-O3` es
`n^(4/5)log n`; esto no afirma que la varianza real tenga el orden de (1.3).

El cierre de `NC-2D` exige una nueva decisión del PI antes de atacar esa brecha. La
instrucción `"haz push y vamos por 2"` autoriza preparar este borrador, pero no
sustituye la firma específica de §9 ni inicia la ejecución de §5.

## 2. Objetos congelados y notación

No se cambia `MIN_COVERAGE_LEX`, `Q_3(C)`, el suceso de selección única `S`, el
lado `h`, los gaps `(K_h,L_h)`, el conteo `M_h` ni la duración relativa `ell_h`.
Se mantienen

\[
q_{n,h}=\sqrt{K_hL_h},
\qquad
Z_{n,h}=\frac{q_{n,h}}{n+1}.
\tag{2.1}
\]

El grupo simétrico se denota siempre por \(\mathfrak S_n\), el suceso de selección
por \(S\), y el subconjunto seleccionado por

\[
\mathcal S_n=\{\pi\in\mathfrak S_n:S(\pi)\}.
\tag{2.2}
\]

Para `n>=6`, `NC-2B` garantiza que \(\mathcal S_n\ne\varnothing\). Todas las
esperanzas y varianzas seleccionadas de esta nota se toman respecto de la medida
uniforme

\[
\nu_n(\pi)=\frac1{|\mathcal S_n|},
\qquad \pi\in\mathcal S_n.
\tag{2.3}
\]

La rotación de 180 grados probada en `NC-2C` preserva \(S\) e intercambia
PAST/FUTURE. Puede usarse para reducir el análisis a un lado, siempre que cada
estadístico nuevo introducido respete esa biyección.

## 3. Objetivo primario `NC2E-O3`

Decidir si existen constantes explícitas `C_q<infinity` y `n_0>=6`, comunes a
ambos lados, tales que

\[
\boxed{
\operatorname{Var}_{\nu_n}(q_{n,h})
\le C_q n
\quad\text{para todo }n\ge n_0
\text{ y }h\in\{\mathrm{PAST},\mathrm{FUTURE}\}.}
\tag{NC2E.1}
\]

Equivalentemente, si

\[
\bar q_{n,h}=\frac1{|\mathcal S_n|}
\sum_{\pi\in\mathcal S_n}q_{n,h}(\pi),
\tag{3.1}
\]

el objetivo es la desigualdad relativa

\[
\sum_{\pi\in\mathcal S_n}
\bigl(q_{n,h}(\pi)-\bar q_{n,h}\bigr)^2
\le C_q n|\mathcal S_n|.
\tag{NC2E.2}
\]

Una formulación exacta adicional, útil para comparar pares seleccionados, es

\[
\operatorname{Var}_{\nu_n}(q_{n,h})
=\frac1{2|\mathcal S_n|^2}
\sum_{\pi,\sigma\in\mathcal S_n}
\bigl(q_{n,h}(\pi)-q_{n,h}(\sigma)\bigr)^2.
\tag{3.2}
\]

No basta mejorar el exponente `9/5` sin llegar a `1`, demostrar una cota
incondicional, exhibir configuraciones seleccionadas aisladas ni obtener evidencia
en un conjunto finito de tamaños.

## 4. Consecuencia precomprometida y techo lógico

La descomposición rango–magnitud ya auditada en `NC-2D` implica que, si (NC2E.1)
vale, entonces

\[
\operatorname{Var}(\ell_h\mid n,h,S)
\le\frac{1+(\sqrt{C_q}+1/2)^2}{n}.
\tag{4.1}
\]

Combinada con la cota de numerador de `NC-2A` y `NC-2C`, esto permite promover

\[
\liminf_{n\to\infty}T_n^h
\ge
\frac{3}
{64\,000\,000\,[1+(\sqrt{C_q}+1/2)^2]}
>0
\tag{4.2}
\]

para cada lado, exclusivamente en el canal `sigma(M_h)`, `fixed-n`, `d=2`.

La tasa (NC2E.1) se denomina aquí *escala CLT* solo como descripción de orden. Su
prueba no demostraría convergencia normal, un teorema central del límite, una
constante asintótica de varianza ni colas subgaussianas.

## 5. Trabajo autorizado por la firma

Tras la firma, la ejecución seguirá este orden y no presupondrá que ninguna ruta
concreta tenga éxito:

1. **auditoría exacta de la medida seleccionada:** reconstruir únicamente desde
   resultados ya probados qué transformaciones de permutaciones preservan `S`, la
   unicidad del ganador y la dualidad PAST/FUTURE;
2. **sensibilidad del ganador:** determinar qué puede cambiar en
   `q_(n,h)(pi)` bajo transposiciones, inserciones, borrados o cirugías locales. Una
   oscilación determinista de orden `n` no se confundirá con una varianza de ese
   orden;
3. **descomposición relativa:** buscar una representación exacta de (3.2) o de
   (NC2E.2) mediante clases, fibras, niveles o pares de permutaciones seleccionadas.
   Toda descomposición de covarianzas deberá derivarse de una identidad declarada;
   no se asumirá aditividad informal de `q` ni del selector;
4. **rutas de comparación, por prioridad:** auditar una o varias de las siguientes:
   - una cadena de Markov o grafo de *switchings* sobre \(\mathcal S_n\), con medida
     uniforme reversible, conectividad, constante de Poincaré y energía de `q`
     demostradas en la misma escala;
   - pares intercambiables o resampling condicionado que permanezca dentro de
     \(\mathcal S_n\); no se aplicará Efron--Stein de coordenadas independientes
     después de condicionar por `S`;
   - una inyección o correspondencia de multiplicidad controlada que compare
     relativamente niveles extremos y centrales de `q` dentro de
     \(\mathcal S_n\);
   - una cola relativa integrable centrada en `bar q_(n,h)`, o la afirmación más
     fuerte centrada en `n/2`, siempre con denominador `|mathcal S_n|`;
   - como ruta auxiliar, una mejora de `Pr(S)` solo si alcanza por sí misma la
     escala necesaria; no se la tratará como condición necesaria;
5. **adjudicación:** probar (NC2E.1), probar su negación mediante una subsucesión
   exacta, obtener una reducción material nueva o identificar literalmente el lema
   relativo ausente;
6. **salida única:** emitir exactamente un terminal de §6 en un único documento
   científico nuevo:

```text
emergencia/P1a_count_volume_selected_variance_clt_scale_d2.md
```

Se permiten cálculos simbólicos deterministas y verificaciones exactas de
identidades intermedias. No se autorizan simulaciones, Monte Carlo, muestras,
semillas, consulta de tamaños sellados para escoger constantes, ni inferencias
asintóticas desde tamaños finitos. No se autoriza crear código o artefactos
numéricos nuevos.

## 6. Terminales precomprometidos

La ejecución emitirá exactamente uno:

```text
NC2E_PROVED_SELECTED_CLT_SCALE
  Se prueba NC2E.1 con C_q y n_0 explicitos para ambos lados. Se promueven (4.1) y
  (4.2), sin afirmar un CLT ni normalidad asintotica.

NC2E_REFUTED_SELECTED_CLT_SCALE
  Se prueba mediante una subsucesion exacta que Var(q_{n,h}|n,h,S)/n no esta
  acotada. Evidencia finita o el fallo de una tecnica no bastan.

NC2E_PARTIAL_RELATIVE_VARIANCE_REDUCTION
  Se obtiene una identidad, desigualdad relativa o estructura nueva y material,
  pero no se prueba ni refuta NC2E.1; se identifica literalmente la obligacion
  restante.

NC2E_BLOCKED_RELATIVE_SELECTED_MEASURE
  Las rutas auditadas no producen una comparacion relativa mejor que NC-2D. Se
  documentan los obstaculos exactos sin presentar el bloqueo como refutacion.
```

Una refutación de (NC2E.1) refuta `NC2E-O3`, pero no implica por sí sola que
`liminf T_n^h=0`: numerador y denominador del cociente podrían requerir un análisis
conjunto distinto.

## 7. Prohibiciones y techo de afirmación

- no presentar (1.3) como información independiente de (1.1)--(1.2);
- no confundir la brecha entre cotas con el orden de la varianza real;
- no usar Efron--Stein, diferencias acotadas o martingalas de exposición bajo la
  ley condicionada sin construir y justificar el kernel o filtrado correspondiente;
- no suponer que una modificación local de la permutación cambia localmente al
  ganador de `MIN_COVERAGE_LEX`;
- no sustituir una comparación relativa dentro de \(S\) por una cola
  incondicional dividida sin controlar explícitamente `Pr(S)`;
- no inferir (NC2E.1) de una cota de soporte, ejemplos aislados o enumeraciones
  finitas;
- no afirmar un CLT, normalidad, optimalidad de tasa ni constante asintótica a
  partir de una cota `O(n)`;
- no cambiar el selector, `Q_3`, `S`, `M_h`, `(K_h,L_h)`, `ell_h` ni la abstención;
- no usar los tamaños sellados `n in {64,96,128}` para elegir constantes o una ruta
  de prueba;
- no transferir resultados a canales enriquecidos, poset completo, horizontes,
  escala absoluta o `d>=3`;
- no formular afirmaciones de novedad o prioridad bibliográfica;
- no modificar, cerrar, comentar, fusionar ni marcar como lista la PR #7;
- no hacer commit ni push sin una orden posterior expresa del PI.

## 8. Test de terminado

El documento científico deberá contener:

1. el dominio condicionado, la notación y la medida uniforme \(\nu_n\);
2. la identidad exacta que fundamente cualquier descomposición de varianza o
   covarianza utilizada;
3. tratamiento de ambos lados o reducción por una dualidad demostrada;
4. una desigualdad relativa con denominador `|mathcal S_n|`, o una explicación
   exacta de por qué la ruta auditada no la produce;
5. todas las obligaciones de conectividad, reversibilidad, gap, multiplicidad o
   sensibilidad exigidas por la técnica elegida;
6. constantes explícitas si el terminal es positivo;
7. una subsucesión exacta si el terminal es de refutación;
8. separación explícita entre cota demostrada, escala requerida y varianza real;
9. separación explícita entre escala `O(n)` y un CLT;
10. exactamente un terminal de §6.

## 9. Firma

```text
FIRMADO_POR: Ignacio Martín (PI)
FECHA_FIRMA: 2026-08-18
DECISION_NC2E: AUTORIZADO_CONFORME_AL_BORRADOR
AUTHORISED_SCOPE: lista cerrada de §5
LITERAL_SIGNOFF: "Firmo y autorizo NC-2E conforme al borrador. Ignacio Martín (PI), 18/08/2026."
```

El sufijo `_DRAFT` del nombre del fichero conserva la genealogía del documento; no
describe el estado de la autorización.

## 10. Ejecución y cierre

La autorización se ejecutó en
`emergencia/P1a_count_volume_selected_variance_clt_scale_d2.md`, siguiendo el orden
de §5, sin consultar los tamaños sellados para elegir constantes ni ruta, y sin
datos, simulaciones, semillas, código ni artefactos numéricos nuevos.

**Auditoría de la medida seleccionada (§5.1).** Las dos transformaciones probadas
—la rotación de 180 grados de `NC-2C` §2 y la inversión de la permutación de
`P1a_count_volume_lema_kl_d2.md` §7.1.1— son involuciones que conmutan y preservan
\(\mathcal S_n\); generan un grupo de Klein de biyecciones que preservan
\(\nu_n\). Como `q_{n,h}` es invariante por la inversión y la rotación intercambia
los lados, se obtiene la igualdad exacta

\[
\operatorname{Var}_{\nu_n}(q_{n,\rm PAST})
=\operatorname{Var}_{\nu_n}(q_{n,\rm FUTURE}),
\]

que cierra la obligación de ambos lados por biyección, no por repetición del
argumento.

**Sensibilidad del ganador (§5.2).** Los dos testigos de `NC-2D` §3 se volvieron a
demostrar aquí de forma autocontenida. Su consecuencia se enunció como no-go de
soporte: existe una medida sobre \(\mathcal S_n\) con varianza
`Theta(n^2)`, luego ninguna prueba puede apoyarse sólo en el soporte de
\(\nu_n\) o en una cota inferior de `|mathcal S_n|`. La oscilación determinista de
orden `n` no se presentó como varianza de ese orden, y no se supuso que una
modificación local cambie localmente al ganador.

**Descomposición y comparación (§5.3–§5.4).** Se probó la identidad determinista

\[
q_{n,h}^2=n\,M_h+n^2\theta_h-(K_h+L_h+1),
\qquad|\theta_h|\le\Delta_n,
\]

válida punto a punto en `S`, y la cota puntual
`|Z_(n,h)-1/2| <= 50(R+Delta_n)+10/n` en todo \(\mathcal S_n\), con `R` el radio de
anclaje aleatorio. De ahí, con división controlada por `Pr(S)`, la desigualdad
relativa

\[
\sum_{\pi\in\mathcal S_n}
\bigl(q_{n,h}(\pi)-\bar q_{n,h}\bigr)^2
\le10^6\,n
\left[\log\frac{n!}{|\mathcal S_n|}+4\log n\right]|\mathcal S_n|,
\qquad n\ge10^{40}.
\]

Con la cota de `Pr(S)` hoy disponible esto reproduce el **orden** `n^(9/5) log n` de
`NC-2D` con constante peor; no es una mejora numérica y no sustituye la constante
`2800`. Su contenido es la dependencia explícita en `|mathcal S_n|`.

**Adjudicación (§5.5).** No se probó ni se refutó `NC2E.1`. Se obtuvo:

1. el óptimo exacto de la familia auditada,
   `Theta(n[log(1/Pr(S))+log n])`, cuyo suelo es de orden `n log n` incluso con
   `Pr(S)=1`; por tanto una mejora de `Pr(S)` **no alcanza por sí sola** la escala
   requerida, y conforme a §5 no se desarrolló ninguna mejora de esa cota;
2. la reducción suficiente: si
   `sum_{pi in mathcal S_n}(R+Delta_n)^2 <= (C_Delta/n)|mathcal S_n|`, entonces
   `NC2E.1` vale con `C_q=4*10^4 C_Delta+1`, y se promueven (4.1) y (4.2);
3. la obligación restante, literal: esa desigualdad relativa de discrepancia media
   cuadrática bajo \(\nu_n\); implicada, como caso particular más fuerte, por la
   conjunción de `Pr(S)>=c>0` y una cota **incondicional** por encadenamiento
   `E[Delta_n^2]=O(1/n)`;
4. la formalización exacta de la ruta de switchings: reversibilidad probada,
   conectividad, gap y energía abiertos; y la constatación de que Efron–Stein no es
   aplicable bajo \(\nu_n\) por ausencia de estructura producto.

No se afirmó ningún teorema central del límite ni normalidad: `NC2E.1` es un
enunciado de orden de varianza.

```text
NC2E_TERMINAL = NC2E_PARTIAL_RELATIVE_VARIANCE_REDUCTION
NC2E_RELATIVE_VARIANCE_BOUND = 10^6*n*(log(n!/|S_n|)+4*log(n))
NC2E_SUFFICIENT_REDUCTION = RELATIVE_MEAN_SQUARE_DISCREPANCY_SUM_(R+Delta)^2 <= C*|S_n|/n
NC2E_PR_S_ROUTE_CEILING = INSUFFICIENT_ALONE
NC2E_O3 = OPEN
NC2E_LIMINF_T_N = NOT_PROVED
NC2E_SEAL_TOUCHED = NO
NC2E_PR7_MODIFIED = NO
NC2E_COMMITTED = NO
```

La autorización `NC-2E` queda consumida y cerrada. Cualquier ataque posterior a la
obligación relativa restante —incluida cualquier mejora de la cota de `Pr(S)` de
`NC-2C` o cualquier trabajo sobre la cota incondicional de discrepancia— requiere
una nueva decisión del PI.
