# Nota de alcance `NC-2A` — escala uniforme de la cota Beta

```text
ESTADO: FIRMADA / NC2A_EXECUTED / NC2A_PROVED_UNIFORM_INTERIOR_N_INV
FECHA_BORRADOR: 2026-08-17
FECHA_FIRMA: 2026-08-17
REQUIERE_FIRMA_NUEVA_DEL_PI: CUMPLIDO
AMPLIARIA: docs/program_reopening_note_2026-08-17_nc1_asymptotic_conditions.md
NO_REVOCA: docs/program_closure_note_2026-07-30.md
NO_REABRE: EF-0--EF-8, EF-4/C1 ni reconstruccion de horizonte
SELLO: intacto — no se toca
SEMILLAS: ninguna
EJECUCION: COMPLETADA DENTRO DE LA LISTA CERRADA DE §4
```

## 1. Motivo

`NC-1` aisló como obligación `NC1-O2` encontrar una ventana de valores de `M`
donde la cota geométrica `b_n(m)` conserve la misma escala que la varianza total.
El presente borrador separa la parte puramente geométrica: determinar la escala de
`b_n(m)` uniformemente lejos de los bordes `m/n=0,1`, sin estudiar todavía la ley
seleccionada de `M`.

El nombre conserva `_DRAFT` por genealogía, pero la nota quedó firmada por el PI
en §8 y autoriza ejecutar exclusivamente el ataque descrito.

## 2. Objeto congelable

Para cada `m` factible,

\[
b_n(m)=\min_{(k,l)\in F_{\rm relax}(m,n)} v_n(k,l),
\]

donde

\[
v_n(k,l)=\operatorname{Var}(\sqrt{X_kY_l})
=\frac{kl}{(n+1)^2}\{1-R(k,n)R(l,n)\},
\]

`X_k~Beta(k,n+1-k)`, `Y_l~Beta(l,n+1-l)` son independientes y

```text
F_relax(m,n) = {
  (k,l) in Z^2:
  2<=k,l<=n-1,
  k,l>=m-1,
  k+l<=n+m-2
}.
```

La identidad de `v_n` y la cota global `v_n(k,l)<=1/n` ya están demostradas en
`emergencia/P1a_count_volume_lema_kl_d2.md`. No se vuelven a presentar como
resultado de `NC-2A`.

## 3. Pregunta primaria

Para cada `epsilon in (0,1/2)`, decidir si existen `c_epsilon>0` y
`n_0(epsilon)` tales que, para todo `n>=n_0(epsilon)` y todo entero `m` con

\[
\varepsilon n\le m\le(1-\varepsilon)n,
\]

se cumple

\[
\frac{c_\varepsilon}{n}\le b_n(m)\le\frac1n.
\tag{NC2A-U}
\]

Solo la cota inferior es nueva. El enunciado se fija para todo compacto interior;
no se elegirá una ventana mirando los valores sellados de `M/n`.

Si `NC2A-U` vale, `NC1-O2` se reduce a probar que, para algún `epsilon` fijo, la
ley seleccionada coloca masa no evanescente en
`[epsilon n,(1-epsilon)n]`. `NC-2A` no intenta probar esa masa.

## 4. Trabajo autorizado tras la firma

Orden cerrado:

1. partir de la identidad exacta
   `v_n(k,l)=kl(n+1)^{-2}(1-R(k,n)R(l,n))`;
2. obtener desigualdades de dos lados para los cocientes Gamma que controlen el
   primer orden de `1-R(k,n)R(l,n)` cuando `k,l` son proporcionales a `n`;
3. usar las restricciones de `F_relax` para mostrar que, si `m/n` permanece en un
   compacto interior, no pueden degenerar simultáneamente los factores que aportan
   varianza;
4. decidir `NC2A-U` con una prueba uniforme o con una sucesión analítica que la
   refute;
5. registrar exactamente un terminal de §5 en un único documento científico nuevo:

```text
emergencia/P1a_count_volume_beta_uniform_scaling_d2.md
```

Se permiten manipulaciones algebraicas y comprobaciones simbólicas deterministas
de identidades intermedias. No se autoriza un barrido numérico como evidencia del
enunciado uniforme.

## 5. Terminales precomprometidos

```text
NC2A_PROVED_UNIFORM_INTERIOR_N_INV
  Se demuestra NC2A-U para todo epsilon fijo en (0,1/2), con constantes y
  cuantificadores explícitos. No demuestra masa seleccionada ni el teorema de NC-1.

NC2A_REFUTED_BY_ANALYTIC_SEQUENCE
  Se exhiben epsilon>0 y una sucesion exacta (n_j,m_j,k_j,l_j), con
  (k_j,l_j) in F_relax(m_j,n_j), m_j/n_j en el compacto interior y
  n_j v_{n_j}(k_j,l_j)->0. Un descenso numerico finito no basta.

NC2A_OPEN_BOUND_GAP
  No se obtiene ni la cota inferior uniforme ni una sucesion analitica que la
  refute; se localiza exactamente la desigualdad Gamma o la region del politopo
  donde queda el hueco.

NC2A_ALREADY_DECIDED_IN_EXISTING_RECORD
  Una prueba ya presente decide literalmente NC2A-U; se cita y no se duplica.
```

No se permite debilitar después de mirar el argumento el compacto interior, cambiar
`1/n` por una tasa ajustada o promover una malla finita a demostración.

## 6. Prohibiciones

- ninguna simulación, semilla, muestra o artefacto estocástico nuevo;
- ninguna lectura de los datos sellados para elegir `epsilon`;
- ningún cambio de `b_n`, `F_relax`, `M`, `S` o `MIN_COVERAGE_LEX`;
- ningún ataque a la ley seleccionada, `w`, `NC1-O1` o `NC1-O3`;
- ninguna afirmación sobre `T_n`, canales enriquecidos, poset completo, horizonte
  o `d>=3`;
- ninguna afirmación de novedad o prioridad;
- ningún commit ni push sin orden posterior del PI.

## 7. Test de terminado

El trabajo termina solo si el documento científico autorizado contiene:

1. definiciones y cuantificadores completos;
2. trazabilidad a las identidades Beta/Gamma ya demostradas;
3. una prueba uniforme completa o un falsificador analítico exacto;
4. límites de interpretación respecto de `NC1-O1`, `NC1-O2` y `NC1-O3`;
5. exactamente un terminal de §5.

## 8. Firma

```text
FIRMADO_POR: Ignacio Martín (PI)
FECHA_FIRMA: 2026-08-17
DECISION_NC2A: AUTORIZADO_CONFORME_AL_BORRADOR
AUTHORISED_SCOPE: lista cerrada de §4
LITERAL_SIGNOFF: "Firmo y autorizo NC-2A conforme al borrador. Ignacio Martín (PI), 17/08/2026."
```

## 9. Ejecución y cierre

El ataque autorizado se ejecutó en
`emergencia/P1a_count_volume_beta_uniform_scaling_d2.md` sin datos, simulaciones,
barridos numéricos ni código nuevo.

La prueba obtiene la identidad telescópica exacta

\[
R(k,n)=\prod_{j=k}^{n}\left(1-\frac1{(2j+1)^2}\right)
\]

y usa `k,l>=m-1` junto con `k+l<=n+m-2`. Para todo
`epsilon in (0,1/2)`, `n>=ceil(4/epsilon)` y
`epsilon n<=m<=(1-epsilon)n`, demuestra

\[
\frac{\varepsilon^3}{288n}\le b_n(m)\le\frac1n.
\]

El terminal vigente es:

```text
NC2A_TERMINAL = NC2A_PROVED_UNIFORM_INTERIOR_N_INV
NC2A_GEOMETRIC_SCALE = 1/n
NC2A_SELECTION_MASS = OPEN
NC2A_EVENTUAL_CONDITIONAL_LAW = OPEN
NC2A_TOTAL_VARIANCE_SCALE = OPEN
NC2A_LIMINF_T_N = NOT_PROVED
NC2A_NEW_DATA = NO
NC2A_NEW_CODE = NO
```

La autorización queda consumida con este terminal. Cualquier ataque posterior a la
masa seleccionada, la existencia eventual o la varianza total requiere una nueva
nota firmada.
