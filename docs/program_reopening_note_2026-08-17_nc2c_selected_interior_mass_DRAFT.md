# Nota de alcance `NC-2C` — masa interior de la ley seleccionada

```text
ESTADO: FIRMADA / EJECUTADA / NC2C_PROVED_UNIFORM_INTERIOR_MASS
FECHA_BORRADOR: 2026-08-17
FECHA_FIRMA: 2026-08-17
REQUIERE_FIRMA_NUEVA_DEL_PI: CUMPLIDO
PREDECESOR: NC-2B / NC2B_PARTIAL_EVENTUAL_SELECTION_ONLY
USA: emergencia/P1a_count_volume_selected_law_asymptotics_d2.md
USA: emergencia/P1a_count_volume_beta_uniform_scaling_d2.md
NO_REVOCA: docs/program_closure_note_2026-07-30.md
NO_REABRE: NC2B-O3, EF-0--EF-8, EF-4/C1 ni reconstruccion de horizonte
SELLO: intacto — no se toca
SEMILLAS: ninguna
```

## 1. Motivo y precedencia

`NC-2B` demostró para todo `n>=6` que

\[
\Pr_n(S)\ge \frac1{n!}>0.
\]

Por tanto, para cada lado `h in {PAST,FUTURE}`,

\[
D_h=\{n\ge6\},
\]

y la ley condicionada por `(n,h,S)`, su varianza positiva y `T_n^h` están
definidos en toda la cola relevante. La cota `1/n!` no controla la composición
interna de `S` y no implica masa seleccionada útil.

`NC-2A` demostró, para toda ventana interior fija y para
`n>=ceil(4/epsilon)`,

\[
\inf_{\varepsilon n\le m\le(1-\varepsilon)n}b_n(m)
\ge \frac{\varepsilon^3}{288n}.
\tag{1.1}
\]

La única pregunta autorizable en esta nota es si la ley seleccionada de `M_h`
conserva una masa uniforme dentro de alguna de esas ventanas. `NC2B-O3` permanece
cerrado aunque la respuesta sea positiva.

La instrucción del PI `"vamos con O2"` autorizó preparar el borrador. La firma
específica exigida por el cierre de `NC-2B` consta en §9 y abre exclusivamente el
trabajo de §5.

## 2. Objetos congelados

Sin alterar el contrato vigente:

```text
Pi_n = permutacion uniforme de {1,...,n};
Q_3(C) = {(a,b,c,d): a prec b prec c prec d,
          |[a,b]|>=3, |[c,d]|>=3};
MIN_COVERAGE_LEX = argmax unico de
  (min(m_-,m_+), m_-+m_+) sobre Q_3(C);
S = evento de que ese argmax exista y sea unico;
M_PAST = |[a,b]| y M_FUTURE = |[c,d]| para el ganador unico.
```

Para `n>=6`, sea

\[
\mathcal S_n=\{\pi\in\mathfrak S_n:S(\pi)\},
\]

y, para `epsilon in (0,1/2)`,

\[
\mathcal I_{n,h}(\varepsilon)
=\{\pi\in\mathcal S_n:
\varepsilon n\le M_h(\pi)\le(1-\varepsilon)n\}.
\]

Como la ley de `Pi_n` es uniforme y \(\mathcal S_n\) no es vacío,

\[
R_{n,h}(\varepsilon)
:=\Pr\{\varepsilon n\le M_h\le(1-\varepsilon)n\mid n,h,S\}
=\frac{|\mathcal I_{n,h}(\varepsilon)|}{|\mathcal S_n|}.
\tag{2.1}
\]

## 3. Objetivo primario `NC2C-O2`

Decidir si existen constantes explícitas

\[
\varepsilon\in(0,1/2),\qquad p>0,\qquad n_0\ge6,
\]

independientes de `n` y comunes a ambos lados, tales que

\[
R_{n,h}(\varepsilon)\ge p
\quad\text{para todo }n\ge n_0
\text{ y }h\in\{PAST,FUTURE\}.
\tag{NC2C.1}
\]

Equivalente y puramente combinatoriamente,

\[
|\mathcal I_{n,h}(\varepsilon)|
\ge p|\mathcal S_n|.
\tag{NC2C.2}
\]

No basta demostrar que \(\mathcal I_{n,h}\) es no vacío, que `Pr(S)` es positiva o
subexponencial, ni que (NC2C.1) se cumple para un conjunto finito de tamaños.

La negación que permitiría refutar el objetivo completo es

\[
\forall\varepsilon\in(0,1/2),\ \forall p>0,\ \forall n_0,
\ \exists n\ge n_0,\ \exists h:
R_{n,h}(\varepsilon)<p.
\tag{NC2C.3}
\]

Por tanto, el fallo de una sola ventana o de una sola técnica de conteo no refuta
`NC2C-O2`.

## 4. Consecuencia suficiente, no necesaria

Si (NC2C.1) pasa, entonces, para
`n>=max(n_0,ceil(4/epsilon))`, (1.1) implica

\[
\mathbb E[b_n(M_h)\mid n,h,S]
\ge \frac{p\varepsilon^3}{288n}.
\tag{4.1}
\]

Esto cierra una ruta suficiente para la escala inferior del numerador. No es una
condición necesaria: una cota agregada directa sobre
`E[b_n(M_h)|n,h,S]` podría existir sin (NC2C.1). Un hallazgo de ese tipo podrá
registrarse como observación, pero no contará como prueba de `NC2C-O2` dentro de
esta ejecución.

Incluso si (NC2C.1) pasa, no se podrá afirmar `liminf T_n^h>0`: seguirá faltando la
cota de varianza total `NC2B-O3`.

## 5. Trabajo autorizado por la firma

La ejecución seguirá este orden:

1. **auditoría de fuentes:** identificar qué identidades exactas del selector y
   qué simetrías de permutaciones están probadas; no importar el certificado
   selector-específico EF-4/EF-7 degradado;
2. **dualidad por lado:** decidir deductivamente si una biyección preserva `S` e
   intercambia `M_PAST` y `M_FUTURE`; si pasa, reducir sin pérdida a un lado;
3. **descomposición exacta del conteo:** expresar el borde seleccionado y el
   interior mediante clases combinatorias que conserven la unicidad del ganador;
4. **comparación relativa:** intentar una o varias de estas rutas, sin suponer que
   alguna funcione:
   - inyección o cirugía de multiplicidad controlada entre clases de borde e
     interior;
   - recurrencia o función generadora conjunta para selección y `M_h`;
   - cotas superior e inferior de la misma escala para los conteos relevantes;
   - desigualdad probabilística directa que controle
     `Pr(S cap {M_h fuera})/Pr(S)`;
5. **adjudicación:** probar (NC2C.1), probar su negación completa (NC2C.3), o
   localizar el lema de conteo todavía ausente;
6. emitir exactamente un terminal de §6 en un único documento científico nuevo:

```text
emergencia/P1a_count_volume_selected_interior_mass_d2.md
```

Se permiten comprobaciones deterministas y exactas de identidades intermedias,
pero no inferencias asintóticas desde tamaños finitos. No se autoriza crear código,
simulaciones, Monte Carlo, muestras, semillas ni artefactos numéricos nuevos.

## 6. Terminales precomprometidos

La ejecución emitirá exactamente uno:

```text
NC2C_PROVED_UNIFORM_INTERIOR_MASS
  Se prueba NC2C.1 con epsilon, p y n_0 explicitos para ambos lados. Se promueve
  (4.1), pero O3 y liminf T_n^h permanecen abiertos.

NC2C_REFUTED_UNIFORM_INTERIOR_MASS
  Se prueba la negacion completa NC2C.3 mediante una subsucesion o argumento
  equivalente. El fallo de una ventana concreta no basta.

NC2C_PARTIAL_COMBINATORIAL_REDUCTION
  Se obtiene una reduccion, simetria o cota nueva y exacta, pero no se prueba ni
  refuta NC2C.1; se identifica literalmente la obligacion restante.

NC2C_BLOCKED_RELATIVE_COUNTING
  No se mejora materialmente la reduccion (2.1)--(2.2); se documenta por que las
  rutas auditadas no comparan numerador y denominador en la misma escala.
```

Ningún terminal autoriza abrir `O3` automáticamente.

## 7. Prohibiciones y techo de afirmación

- no abrir, estimar ni acotar `Var(ell_h|n,h,S)`;
- no afirmar `liminf T_n^h>0`;
- no cambiar `MIN_COVERAGE_LEX`, `Q_3`, `S`, `M_h` ni la abstención;
- no usar los tamaños sellados para elegir `epsilon`, `p` o una ruta de prueba;
- no rehabilitar EF-4/EF-7 sin volver a demostrar cada paso específico usado;
- no sustituir el cociente condicionado por una probabilidad incondicional;
- no presentar no-vacuidad o una familia explícita como masa proporcional;
- no transferir resultados a canales enriquecidos, poset completo, horizontes,
  escala absoluta o `d>=3`;
- no formular afirmaciones de novedad o prioridad;
- no hacer commit ni push sin una orden posterior expresa del PI.

## 8. Test de terminado

El documento científico debe contener:

1. definiciones exactas de \(\mathcal S_n\), \(\mathcal I_{n,h}\) y `R_{n,h}`;
2. trazabilidad de cada lema importado;
3. tratamiento explícito de ambos lados o una biyección que los intercambie;
4. una comparación relativa con denominador `|mathcal S_n|`, no solo un conteo
   absoluto del interior;
5. constantes y cola explícitas si el terminal es positivo;
6. la negación completa (NC2C.3) si el terminal es de refutación;
7. confirmación expresa de que `O3` no se abrió;
8. exactamente un terminal de §6.

## 9. Firma

```text
FIRMADO_POR: Ignacio Martín (PI)
FECHA_FIRMA: 2026-08-17
DECISION_NC2C: AUTORIZADO_CONFORME_AL_BORRADOR
AUTHORISED_SCOPE: lista cerrada de §5
LITERAL_SIGNOFF: "Firmo y autorizo NC-2C conforme al borrador. Ignacio Martín (PI), 17/08/2026."
```

El nombre conserva `_DRAFT` por genealogía; no describe el estado vigente de la
nota.

## 10. Ejecución y cierre

La autorización se ejecutó en
`emergencia/P1a_count_volume_selected_interior_mass_d2.md`, sin datos,
simulaciones, semillas, código ni artefactos numéricos nuevos.

Se demostró primero la dualidad exacta PAST/FUTURE mediante la rotación de 180
grados de la matriz de permutación. Después se construyó, para tamaños pares, una
familia prescrita nueva de anchura

\[
\rho_n=\lfloor n^{4/5}\rfloor
\]

que fuerza un ganador único con probabilidad `e^{-o(n)}`. La demostración no
importa el certificado EF-4/EF-7 degradado: prueba de nuevo la uniformidad de la
biyección residual, una cota de discrepancia por martingalas y la unicidad del
ganador. El caso geométrico de pérdida de una escalera se cierra mediante la
optimización explícita

\[
\max_f\min\{Nf+2,N(1-\sqrt f)^2+\rho+2\}
=\frac N4+\frac\rho2+\frac{\rho^2}{4N}+2,
\]

con margen asintótico `rho/2`. Una inyección que añade un punto aislado transfiere
la cota a tamaños impares.

Separadamente, una partición determinista en diez bloques prueba que, salvo un
evento de discrepancia exponencialmente pequeño, todo ganador seleccionado tiene
ambos intervalos entre `0.03n` y `0.97n`. La cola exponencial sobrevive al
condicionamiento por la masa subexponencial de `S`.

En consecuencia, para

\[
\varepsilon=\frac3{100},
\qquad p=\frac12,
\qquad n_0=10^{40},
\]

todo `n>=n_0` y ambos lados satisfacen

\[
\Pr\{\varepsilon n\le M_h\le(1-\varepsilon)n\mid n,h,S\}\ge p.
\]

Por `NC-2A`, queda promovida exclusivamente la consecuencia

\[
\mathbb E[b_n(M_h)\mid n,h,S]
\ge\frac{3}{64\,000\,000}\frac1n.
\]

El terminal único es:

```text
NC2C_TERMINAL = NC2C_PROVED_UNIFORM_INTERIOR_MASS
NC2C_EPSILON = 3/100
NC2C_P = 1/2
NC2C_N0 = 10^40
NC2C_SIDE_DUALITY = PROVED_EXACT
NC2C_SUBEXPONENTIAL_SELECTION_MASS = PROVED_WITH_NEW_ARGUMENT
NC2C_INTERIOR_NUMERATOR_SCALE = PROVED_ORDER_1_OVER_N
NC2C_O3 = NOT_OPENED
NC2C_LIMINF_T_N = NOT_PROVED
NC2C_NEW_DATA = NO
NC2C_NEW_CODE = NO
```

La autorización `NC-2C` queda consumida y cerrada. `NC2B-O3` no se abrió; cualquier
ataque a la varianza total requiere una nota de alcance y una firma nuevas del PI.
