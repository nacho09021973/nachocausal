# Nota de alcance `NC-2B` — paquete de ley seleccionada

```text
ESTADO: FIRMADA / EJECUTADA / NC2B_PARTIAL_EVENTUAL_SELECTION_ONLY
FECHA_BORRADOR: 2026-08-17
FECHA_FIRMA: 2026-08-17
REQUIERE_FIRMA_NUEVA_DEL_PI: CUMPLIDO
AMPLIARIA: docs/program_reopening_note_2026-08-17_nc1_asymptotic_conditions.md
USA: emergencia/P1a_count_volume_beta_uniform_scaling_d2.md
NO_REVOCA: docs/program_closure_note_2026-07-30.md
NO_REABRE: EF-0--EF-8, EF-4/C1 ni reconstruccion de horizonte
SELLO: intacto — no se toca
SEMILLAS: ninguna
```

## 1. Motivo y precedencia

`NC-2A` demostró que, en toda ventana interior fija,

\[
b_n(m)\ge\frac{\varepsilon^3}{288n}.
\]

Para convertir esa geometría en una cota normalizada quedan las tres obligaciones
seleccionadas de `NC-1`: existencia eventual del condicionamiento, masa interior de
`M` y escala superior de la varianza total.

Los textos históricos EF-4/EF-7 que presentan un certificado subexponencial para
`MIN_COVERAGE_LEX` no se importarán como teoremas: la genealogía vigente registró
roturas en la familia prescrita y dejó EF-4/C1 `INCONCLUSIVE`. `NC-2B` puede citar
sus lemas abstractos supervivientes, pero debe demostrar de nuevo cualquier hecho
específico del selector que utilice.

El nombre conserva `_DRAFT` por genealogía, pero la nota quedó firmada por el PI
en §9 y autoriza ejecutar exclusivamente el ataque descrito.

## 2. Experimento y objetos congelados

Sin cambiar el contrato existente:

```text
Pi_n = permutacion uniforme de {1,...,n};
MIN_COVERAGE_LEX = argmax unico de
  (min(m_-,m_+), m_-+m_+) sobre Q_3(C);
S = evento de que el argmax exista y sea unico;
M_h = cardinalidad del intervalo del lado h in {PAST,FUTURE};
ell_h = duracion relativa latente de ese intervalo.
```

Para `Pr_n(S)>0`,

\[
V_n^h=\operatorname{Var}(\ell_h\mid n,h,S),
\qquad
T_n^h=
\frac{\mathbb E[\operatorname{Var}(\ell_h\mid M_h,n,h,S)\mid n,h,S]}
{V_n^h}.
\]

No se modifica el selector, el evento de abstención, la observación marginal por
lado ni el target.

## 3. Objetivo primario `NC2B-P`

Decidir si existen constantes explícitas

\[
n_0\in\mathbb N,
\quad
\varepsilon\in(0,1/2),
\quad
p>0,
\quad
C<\infty,
\]

independientes de `n`, tales que para cada lado `h` y todo `n>=n_0`:

### `NC2B-O1` — existencia eventual

\[
\Pr_n(S)>0.
\tag{3.1}
\]

### `NC2B-O2` — masa interior seleccionada

\[
\Pr\{\varepsilon n\le M_h\le(1-\varepsilon)n\mid n,h,S\}
\ge p.
\tag{3.2}
\]

### `NC2B-O3` — escala de la varianza total

\[
\operatorname{Var}(\ell_h\mid n,h,S)\le\frac Cn.
\tag{3.3}
\]

Las constantes pueden ser conservadoras, pero deben quedar exhibidas por la prueba;
no se escogerán mirando los tres tamaños sellados.

## 4. Consecuencia precomprometida

Si `NC2B-O1`–`O3` se demuestran, `NC-2A` implica

\[
\mathbb E[b_n(M_h)\mid n,h,S]
\ge\frac{p\varepsilon^3}{288n}.
\]

Por la Proposición `NC1-P`,

\[
\liminf_{n\to\infty}T_n^h
\ge\frac{p\varepsilon^3}{288C}>0
\quad\text{para cada lado }h.
\tag{4.1}
\]

La conclusión solo alcanza el canal `sigma(M_h)` en `fixed-n`, `d=2`; no se
transfiere a canales enriquecidos ni al poset completo.

## 5. Trabajo autorizado tras la firma

Orden obligatorio y con parada tipada:

1. **auditoría de fuentes internas:** separar lemas abstractos válidos de los
   certificados EF-4/EF-7 degradados; ningún flag histórico sustituye una prueba;
2. **`O1` primero:** buscar una construcción exacta de permutaciones con ganador
   `MIN_COVERAGE_LEX` único para todo `n` suficientemente grande. No hace falta una
   cota subexponencial de `Pr(S)`;
3. **`O2` después:** controlar directamente el *pushforward* seleccionado de `M_h`,
   sin exigir una forma cerrada de toda `w(s|m,n,h,S)`;
4. **`O3` al final:** usar la independencia rango–magnitud y la descomposición
   \[
   V_n^h=
   \mathbb E[v_n(K_h,L_h)\mid S]
   +\operatorname{Var}\{\mu_n(K_h,L_h)\mid S\},
   \]
   distinguiendo el término Beta ya acotado por `1/n` del término entre formas;
5. combinar solo si las tres obligaciones pasan;
6. emitir exactamente un terminal de §6 en un único documento científico nuevo:

```text
emergencia/P1a_count_volume_selected_law_asymptotics_d2.md
```

El ataque es analítico. Se permiten comprobaciones simbólicas deterministas de
identidades intermedias. No se autorizan simulaciones, Monte Carlo ni nuevos
tamaños empíricos.

## 6. Terminales precomprometidos

Precedencia: contraejemplo exacto; bloqueo en `O1`; bloqueo en `O2`; bloqueo en
`O3`; paquete completo.

```text
NC2B_REFUTED_BY_EXACT_SUBSEQUENCE
  Se demuestra que alguna de (3.1)--(3.3) falla en una subsucesion infinita. Una
  tendencia numerica no basta.

NC2B_BLOCKED_BY_EVENTUAL_SELECTION
  No se prueba ni se refuta que Pr_n(S)>0 en una cola completa; se localiza la
  obstruccion combinatoria exacta y no se usan condicionales fuera de su dominio.

NC2B_PARTIAL_EVENTUAL_SELECTION_ONLY
  Se prueba O1, pero no O2; O3 no se promueve aunque admita avances auxiliares.

NC2B_PARTIAL_EVENTUAL_SELECTION_AND_INTERIOR_MASS
  Se prueban O1 y O2, pero O3 queda abierto.

NC2B_BLOCKED_BY_TOTAL_VARIANCE_SCALE
  O1 y O2 pasan, pero no se obtiene V_n^h<=C/n ni una refutacion exacta.

NC2B_PROVED_SELECTED_LAW_PACKAGE
  Se prueban O1--O3 con constantes explicitas y, mediante NC-2A/NC-1, (4.1).
```

Un terminal parcial conserva literalmente lo probado y no autoriza citar (4.1).

## 7. Prohibiciones

- ninguna simulación, semilla, muestra o artefacto estocástico nuevo;
- ninguna lectura de datos sellados para escoger `epsilon`, `p` o `C`;
- ningún cambio de `MIN_COVERAGE_LEX`, `Q_3`, `M_h`, `S` o la abstención;
- ninguna rehabilitación del certificado EF-4/EF-7 sin volver a demostrar sus
  pasos específicos;
- ninguna sustitución de riesgo relativo por error absoluto;
- ninguna afirmación sobre canales enriquecidos, poset completo, horizontes,
  escala absoluta o `d>=3`;
- ninguna afirmación de novedad o prioridad;
- ningún commit ni push sin orden posterior del PI.

## 8. Test de terminado

El documento científico autorizado debe contener:

1. definiciones y dominio condicional exactos;
2. trazabilidad y precedencia de toda fuente interna usada;
3. prueba o bloqueo tipado de `O1`, seguido en orden por `O2` y `O3`;
4. constantes explícitas para toda obligación promovida;
5. combinación con `NC-2A` solo si pasan `O1`–`O3`;
6. exactamente un terminal de §6.

## 9. Firma

```text
FIRMADO_POR: Ignacio Martín (PI)
FECHA_FIRMA: 2026-08-17
DECISION_NC2B: AUTORIZADO_CONFORME_AL_BORRADOR
AUTHORISED_SCOPE: lista cerrada de §5
LITERAL_SIGNOFF: "Firmo y autorizo NC-2B conforme al borrador. Ignacio Martín (PI), 17/08/2026."
```

## 10. Ejecución y cierre

La autorización se ejecutó en
`emergencia/P1a_count_volume_selected_law_asymptotics_d2.md`, sin datos,
simulaciones, barridos ni código nuevo.

`NC2B-O1` queda demostrado para todo `n>=6`. Para `n` par, la permutación
identidad induce una cadena total y tiene un ganador único con dos intervalos de
tamaño `n/2`. Para `n` impar, la permutación `(2,3,...,n,1)` induce una cadena
total de tamaño par `n-1` y un punto aislado, sin alterar el conjunto de
cuádruplas admisibles de la cadena. En ambos casos se exhibe una permutación de
`S`, de modo que

\[
\Pr_n(S)\ge \frac1{n!}>0.
\]

`NC2B-O2` queda abierto en el cociente exacto

\[
\frac{|\{\pi\in\mathcal S_n:
\varepsilon n\le M_h(\pi)\le(1-\varepsilon)n\}|}{|\mathcal S_n|}.
\]

La familia exacta `(n,n-1,...,7,1,2,3,4,5,6)` pertenece a `S` y tiene
`M_-=M_+=3`, por lo que la interioridad no se deduce determinísticamente de `S`.
Esto no refuta una cota probabilística uniforme; localiza la obligación restante
como un problema de conteo relativo. Al no pasar `O2`, `NC2B-O3` no se abrió,
conforme a la precedencia de §5.

El terminal único de la ejecución es:

```text
NC2B_TERMINAL = NC2B_PARTIAL_EVENTUAL_SELECTION_ONLY
NC2B_EVENTUAL_SELECTION = PROVED_FOR_ALL_N_GE_6
NC2B_SELECTION_PROBABILITY_LOWER_BOUND = 1/n!
NC2B_INTERIOR_MASS = OPEN_RELATIVE_COUNTING_PROBLEM
NC2B_TOTAL_VARIANCE_SCALE = NOT_OPENED_BY_PRECEDENCE
NC2B_SELECTED_LAW_PACKAGE = NOT_PROVED
NC2B_LIMINF_T_N = NOT_PROVED
NC2B_NEW_DATA = NO
NC2B_NEW_CODE = NO
```

La autorización `NC-2B` queda consumida y cerrada con ese terminal. Cualquier
ataque posterior al cociente relativo de `O2` requiere una nota de alcance y una
firma nuevas del PI.
