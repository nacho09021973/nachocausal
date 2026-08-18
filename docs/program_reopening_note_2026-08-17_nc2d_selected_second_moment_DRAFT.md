# Nota de alcance `NC-2D` — segundo momento seleccionado

```text
ESTADO: FIRMADA / EJECUTADA / NC2D_PARTIAL_RELATIVE_MOMENT_REDUCTION
FECHA_BORRADOR: 2026-08-17
FECHA_FIRMA: 2026-08-17
REQUIERE_FIRMA_NUEVA_DEL_PI: CUMPLIDO
PREDECESOR: NC-2C / NC2C_PROVED_UNIFORM_INTERIOR_MASS
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

`NC-2B` demostró que la ley condicionada por selección existe para todo `n>=6`.
`NC-2C` demostró, para ambos lados y todo `n>=10^40`, masa seleccionada al menos
`1/2` en la ventana `0.03n<=M_h<=0.97n`. Junto con `NC-2A`, esto da

\[
\mathbb E[b_n(M_h)\mid n,h,S]
\ge \frac{3}{64\,000\,000}\frac1n.
\tag{1.1}
\]

La única obligación analítica restante en la ruta suficiente de `NC-1` es

\[
\operatorname{Var}(\ell_h\mid n,h,S)=O(1/n).
\tag{1.2}
\]

El preflight de solo lectura de `NC-2D` aisló una formulación agregada que no exige
resolver la ley completa de formas seleccionadas.

## 2. Objetos congelados y reducción objetivo

No se cambia `MIN_COVERAGE_LEX`, `Q_3(C)`, el evento de selección única `S`, el
conteo lateral `M_h`, la forma de rangos `(K_h,L_h)` ni la duración relativa
`ell_h`. Se define

\[
q_{n,h}=\sqrt{K_hL_h},
\qquad
Z_{n,h}=\frac{q_{n,h}}{n+1}.
\]

La descomposición rango–magnitud ya probada es

\[
\operatorname{Var}(\ell_h\mid n,h,S)
=\mathbb E[v_n(K_h,L_h)\mid n,h,S]
+\operatorname{Var}(\mu_n(K_h,L_h)\mid n,h,S),
\tag{2.1}
\]

con

\[
\mathbb E[v_n(K_h,L_h)\mid n,h,S]\le\frac1n,
\qquad
|\mu_n(K_h,L_h)-Z_{n,h}|\le\frac1{2\sqrt n}.
\tag{2.2}
\]

Por contracción de la proyección sobre constantes, (1.2) es equivalente, salvo
constantes explícitas en ambos sentidos, a

\[
\operatorname{Var}(q_{n,h}\mid n,h,S)=O(n).
\tag{2.3}
\]

## 3. Objetivo primario `NC2D-O3`

Decidir si existen constantes explícitas `C_q<infinity` y `n_0` tales que, para
todo `n>=n_0` y ambos lados `h in {PAST,FUTURE}`,

\[
\operatorname{Var}(q_{n,h}\mid n,h,S)\le C_q n.
\tag{NC2D.1}
\]

Si

\[
\mathcal S_n=\{\pi\in\mathfrak S_n:S(\pi)\},
\qquad
\bar q_{n,h}=\frac1{|\mathcal S_n|}
\sum_{\pi\in\mathcal S_n}q_{n,h}(\pi),
\]

entonces la forma combinatoria exacta de (NC2D.1) es

\[
\sum_{\pi\in\mathcal S_n}
\bigl(q_{n,h}(\pi)-\bar q_{n,h}\bigr)^2
\le C_q n|\mathcal S_n|.
\tag{NC2D.2}
\]

Esta desigualdad relativa de segundo momento es el objetivo mínimo. Una ley cerrada
de `w`, una cota uniforme positiva para `Pr(S)` o una concentración subgaussiana
condicionada serían suficientes, pero son afirmaciones más fuertes y no constituyen
el objetivo primario.

## 4. Consecuencia precomprometida

Si (NC2D.1) vale, entonces

\[
\operatorname{Var}(Z_{n,h}\mid n,h,S)
\le\frac{C_q}{n}.
\]

Usando (2.1)--(2.2),

\[
\operatorname{Var}(\ell_h\mid n,h,S)
\le
\frac{1+(\sqrt{C_q}+1/2)^2}{n}.
\tag{4.1}
\]

Por (1.1), para cada lado,

\[
\liminf_{n\to\infty}T_n^h
\ge
\frac{3}
{64\,000\,000\,[1+(\sqrt{C_q}+1/2)^2]}
>0.
\tag{4.2}
\]

La conclusión solo alcanza el canal `sigma(M_h)` en `fixed-n`, `d=2`.

## 5. Trabajo autorizado por la firma

La ejecución seguirá este orden:

1. auditar la descomposición (2.1), la aproximación (2.2) y la dualidad exacta
   PAST/FUTURE;
2. reducir el ataque a un lado y a la desigualdad relativa (NC2D.2);
3. atacar directamente ese segundo momento mediante conteos, inyecciones, cirugía
   combinatoria, identidades de momentos o desigualdades deterministas;
4. caracterizar toda `w` solo si la ruta agregada resulta insuficiente;
5. combinar con `NC-2A` y `NC-2C` únicamente si (NC2D.1) queda demostrada;
6. emitir exactamente un terminal de §6 en un único documento científico nuevo:

```text
emergencia/P1a_count_volume_selected_second_moment_d2.md
```

Se permiten comprobaciones simbólicas deterministas de identidades intermedias. No
se autorizan datos, simulaciones, Monte Carlo, nuevas semillas, código ni artefactos
numéricos.

## 6. Terminales precomprometidos

```text
NC2D_PROVED_SELECTED_SECOND_MOMENT
  Se demuestra (NC2D.1) con constantes explicitas. Se promueven (4.1) y (4.2).

NC2D_REFUTED_BY_EXACT_SUBSEQUENCE
  Se demuestra que Var(q_{n,h}|S)/n no esta acotada en una subsucesion infinita.
  Una tendencia numerica no basta.

NC2D_PARTIAL_RELATIVE_MOMENT_REDUCTION
  Se obtiene una cota nueva y exacta o una reduccion material, pero no se prueba ni
  refuta (NC2D.1). Se identifica literalmente la obligacion restante.

NC2D_BLOCKED_SELECTED_SECOND_MOMENT
  No se mejora materialmente (NC2D.2); se localiza por que las rutas auditadas no
  controlan el segundo momento relativo.
```

El fallo o bloqueo de esta condición suficiente no refuta por sí solo
`liminf T_n^h>0`.

## 7. Prohibiciones y techo de afirmación

- no elegir constantes a partir de los tamaños sellados `n in {64,96,128}`;
- no generar simulaciones, datos, semillas, código ni artefactos numéricos;
- no cambiar el selector, `Q_3`, `S`, `M_h`, `(K_h,L_h)` ni el target;
- no interpretar `O1+O2` como prueba del teorema final;
- no transferir resultados a canales enriquecidos, poset completo, horizontes,
  escala absoluta o `d>=3`;
- no formular afirmaciones de novedad o prioridad;
- no modificar, cerrar, comentar, fusionar ni marcar como lista la PR #7;
- no hacer commit ni push sin una orden posterior expresa del PI.

## 8. Test de terminado

El documento científico debe contener:

1. dominio condicionado y objetos exactos;
2. prueba de la equivalencia entre O3 y (NC2D.1), con constantes;
3. tratamiento de ambos lados o dualidad exacta;
4. una cota relativa con denominador `|mathcal S_n|`, no solo una cota
   incondicional;
5. constantes explícitas si el terminal es positivo;
6. una subsucesión exacta si el terminal es de refutación;
7. separación explícita entre bloqueo de la ruta y refutación del objetivo final;
8. exactamente un terminal de §6.

## 9. Firma

```text
FIRMADO_POR: Ignacio Martín (PI)
FECHA_FIRMA: 2026-08-17
DECISION_NC2D: AUTORIZADO_CONFORME_AL_BORRADOR
AUTHORISED_SCOPE: lista cerrada de §5
LITERAL_SIGNOFF: "Firmo y autorizo NC-2D conforme al borrador. Ignacio Martín (PI), 17/08/2026."
```

El sufijo `_DRAFT` conserva la genealogía del documento; no describe el estado de
la autorización.

## 10. Ejecución y cierre

La autorización se ejecutó en
`emergencia/P1a_count_volume_selected_second_moment_d2.md`, sin consultar los
tamaños sellados para elegir constantes y sin datos, simulaciones, semillas, código
ni artefactos numéricos nuevos.

La equivalencia entre `NC2D-O3` y

\[
\operatorname{Var}(\sqrt{K_hL_h}\mid n,h,S)=O(n)
\]

quedó probada con constantes explícitas en ambos sentidos. La selección única no
produce una cota determinista de anchura `sqrt(n)`: la cadena total y la cadena
aislada de seis puntos dan testigos exactos dentro de `S` separados a escala `n`.

Usando la cota subexponencial de `Pr(S)` de `NC-2C`, cuatro cajas ancla y la
discrepancia rectangular uniforme, se obtuvo para ambos lados y todo `n>=10^40`

\[
\mathbb E\!\left[\left(
\frac{\sqrt{K_hL_h}}{n+1}-\frac12
\right)^2\mathrel{\Big|}n,h,S\right]
\le700n^{-1/5}\log n,
\]

y, en consecuencia,

\[
\begin{aligned}
\operatorname{Var}(\sqrt{K_hL_h}\mid n,h,S)
&=(n+1)^2\operatorname{Var}\!\left(
\frac{\sqrt{K_hL_h}}{n+1}\mathrel{\Big|}n,h,S
\right)\\
&\le700(n+1)^2n^{-1/5}\log n\\
&\le2800n^{9/5}\log n.
\end{aligned}
\]

mientras que

\[
\operatorname{Var}(\ell_h\mid n,h,S)
\le730n^{-1/5}\log n.
\]

La cota para `sqrt(K_h L_h)` no es un resultado independiente: es exactamente el
reescalado de la cota de varianza normalizada, con la última relajación obtenida de
`(n+1)^2<=4n^2`. Además, como `n^(-1/5)log n` decrece en este dominio y

\[
700(10^{40})^{-1/5}\log(10^{40})
<6.45\times10^{-4}<\frac14,
\]

la estimación mejora desde el umbral explícito `n>=10^40` las cotas triviales

\[
\operatorname{Var}(Z_{n,h}\mid n,h,S)\le\frac14,
\qquad
\operatorname{Var}(q_{n,h}\mid n,h,S)\le\frac{(n+1)^2}{4}.
\]

Esto prueba concentración `L2` seleccionada y `Var(ell_h|n,h,S)->0`, pero pierde un
factor `n^(4/5)log n` entre la cota demostrada y la escala requerida por O3. Esto no
afirma que la varianza real tenga ese orden. El objeto exacto todavía ausente es una
cota de segundo momento relativa de orden `n` sobre la medida uniforme en
\(\mathcal S_n=\{\pi\in\mathfrak S_n:S(\pi)\}\). Aquí \(S\) queda reservado al
suceso de selección y \(\mathfrak S_n\) al grupo simétrico, que no se abrevia. No
se probó ni refutó O3 y no se promovió `liminf T_n^h>0`.

```text
NC2D_TERMINAL = NC2D_PARTIAL_RELATIVE_MOMENT_REDUCTION
NC2D_SELECTED_Q_BOUND_STATUS = EXACT_RESCALE_OF_Z_VARIANCE_BOUND
NC2D_NONTRIVIAL_FROM_N = 10^40
NC2D_O3 = OPEN
NC2D_LIMINF_T_N = NOT_PROVED
NC2D_PR7_MODIFIED = NO
```

La autorización `NC-2D` queda consumida y cerrada. Cualquier ataque posterior al
factor relativo restante requiere una nueva decisión del PI.
