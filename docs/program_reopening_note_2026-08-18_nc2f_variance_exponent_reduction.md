# Nota de alcance `NC-2F` — reducción del exponente de varianza por vía técnica

```text
ESTADO: REFRENDADA / EJECUTADA / NC2F_A_PROVED_SQRT_SELECTION_MASS
        + NC2F_B_PROVED_L2_DISCREPANCY
FECHA: 2026-08-18
FECHA_REFRENDO: 2026-08-18
PREDECESOR: NC-2E / NC2E_PARTIAL_RELATIVE_VARIANCE_REDUCTION
AUTORIZACION_LITERAL: "vamos con 1, te autorizo a realizar las acciones que consideres"
                      Ignacio Martín (PI), 18/08/2026
REFRENDO_LITERAL: "refrenda la NC-2F con firma explícita y commitea"
                  Ignacio Martín (PI), 18/08/2026
ORDEN_DE_LOS_ACTOS: autorizacion general -> ejecucion -> refrendo explicito
                    (el refrendo es POSTERIOR a la ejecucion; no convierte esta
                     nota en una firma previa conforme a borrador)
ALCANCE_AUTORIZADO: opción 1 presentada al PI (piezas (a) y (b) de abajo)
USA: emergencia/P1a_count_volume_selected_interior_mass_d2.md
USA: emergencia/P1a_count_volume_selected_variance_clt_scale_d2.md
USA: emergencia/P1a_count_volume_selected_second_moment_d2.md
NO_MODIFICA: PR #7
NO_MODIFICA: los terminales publicados de NC-2C, NC-2D ni NC-2E
NO_REVOCA: docs/program_closure_note_2026-07-30.md
NO_REABRE: EF-0--EF-8, reconstruccion de horizonte ni d>=3
SELLO: intacto — no se toca
SEMILLAS: ninguna
```

## 1. Naturaleza de esta autorización

El PI eligió la opción 1 y autorizó ejecutarla sin exigir firma conforme a un
borrador previo. Esta nota **no es** una firma conforme a borrador: es el registro
del perímetro que la instrucción general cubre. Los terminales de §4 se
precomprometen antes de ejecutar; el PI la refrendó después (§9).

La diferencia con el resto de la cadena `NC` se declara aquí y no se disimula: en
`NC-2A`–`NC-2E` la firma precede a la ejecución y los terminales quedan
precomprometidos en una sesión anterior; en `NC-2F` la autorización fue general, y
los terminales de §4 se escribieron y la ejecución se realizó en la **misma**
sesión, con refrendo explícito posterior. El refrendo valida el trabajo y su
perímetro; **no** retrocede la fecha de la firma ni convierte el precompromiso en
uno anterior a la ejecución. Cualquier auditoría debe tratar `NC-2F` con ese
descuento procedimental, que no afecta a la corrección matemática de sus dos
documentos, verificable de forma independiente.

## 2. Motivo

`NC-2E` dejó el objetivo `NC2E-O3` (`Var_{nu_n}(q_{n,h})<=C_q n`) reducido a una
única obligación relativa y localizó dos objetos que faltan:

- **(A)** una cota inferior para `Pr_n(S)` mejor que la de `NC-2C`;
- **(B)** una cota **incondicional** por encadenamiento
  `E[Delta_n^2]=O(1/n)` para la discrepancia rectangular de una permutación
  uniforme, sin el factor de unión `n^4`.

Ninguna de las dos piezas de esta nota cierra `NC2E-O3`. Ambas son técnicas,
deductivas y auditables por separado.

## 3. Objetivos

**`NC2F-a` (masa de selección con exponente raíz).** Decidir si el parámetro libre
`rho` de la familia prescrita de `NC-2C` §4.1 puede tomarse de orden
`sqrt(n log n)` en vez de `n^{4/5}`, re-verificando **todas** las desigualdades de
margen del Lema 4.1 de `NC-2C`, y qué cota para `Pr_n(S)` resulta. Si resulta,
combinarla con el Teorema 7.1 de `NC-2E` y con la transferencia de `NC-2D` §2 para
obtener nuevas cotas de `Var(q_{n,h}|S)` y `Var(ell_h|S)`.

**`NC2F-b` (discrepancia en `L^2`, incondicional).** Decidir si
`E[Delta_n^2]<=C/n` con constante explícita, sin condicionar por `S` y sin usar el
selector. Si resulta, enunciar la consecuencia exacta vía el Corolario 8.2 de
`NC-2E`.

## 4. Terminales precomprometidos

Se emitirá exactamente uno por objetivo.

```text
NC2F_A_PROVED_SQRT_SELECTION_MASS
  Se prueba Pr_n(S) >= (1/2) n^(-(C*sqrt(n log n)+c)) con C,c explicitos, para todo
  n >= n_0, re-verificando cada desigualdad de margen. Se publican las cotas de
  varianza resultantes.

NC2F_A_REFUTED_AT_SQRT_SCALE
  Se exhibe una desigualdad de margen del Lema 4.1 de NC-2C que falla para todo
  rho de orden sqrt(n log n), con el calculo exacto.

NC2F_A_BLOCKED
  No se decide: alguna desigualdad no se puede verificar sin rehacer partes de
  NC-2C que esta nota no autoriza a rehacer.

NC2F_B_PROVED_L2_DISCREPANCY
  Se prueba E[Delta_n^2] <= C/n con C explicito, autocontenido salvo citas
  verificadas.

NC2F_B_PARTIAL
  Se prueba una cota estrictamente mejor que el factor de union n^4 pero no O(1/n).

NC2F_B_BLOCKED
  No se obtiene mejora sobre la union del Lema 6.2 de NC-2E.
```

## 5. Prohibiciones y techo de afirmación

- no afirmar que `NC2E-O3` queda cerrado ni que `liminf T_n^h>0`;
- no modificar, degradar ni promover ningún token ya publicado de `NC-2C`,
  `NC-2D` o `NC-2E`; el registro es append-only y las cotas nuevas se publican
  como resultados adicionales, no como correcciones;
- no cambiar el selector, `Q_3`, `S`, `M_h`, `(K_h,L_h)`, `ell_h` ni la abstención;
- no usar los tamaños sellados `n in {64,96,128}` para elegir constantes ni ruta;
- no generar datos, simulaciones, semillas, código ni artefactos numéricos;
- no transferir resultados a canales enriquecidos, poset completo, horizontes,
  escala absoluta o `d>=3`;
- no formular afirmaciones de novedad o prioridad bibliográfica;
- no modificar, cerrar, comentar, fusionar ni marcar como lista la PR #7;
- toda cita externa debe llevar autor, fuente y DOI verificable, o sustituirse por
  una prueba autocontenida.

## 6. Test de terminado

Cada documento científico debe contener: el objeto exacto y su dominio; la lista
completa de desigualdades verificadas con sus valores en el umbral; constantes
explícitas; la separación entre lo probado y lo que sigue abierto; y exactamente
un terminal de §4.

## 7. Salida

```text
emergencia/P1a_count_volume_selection_mass_sqrt_scaling_d2.md      (NC2F-a)
emergencia/P1a_count_volume_rectangular_discrepancy_l2_d2.md       (NC2F-b)
```

## 8. Ejecución y cierre

Ambos objetivos se ejecutaron el 2026-08-18, sin datos, simulaciones, semillas,
código ni artefactos numéricos, sin consultar los tamaños sellados y sin tocar el
sello ni la PR #7.

**`NC2F-a`.** Con `rho=ceil(20 sqrt(n log n))` se re-verificaron las cinco
desigualdades de margen del Lema 4.1 de `NC-2C` (casos 2 y 3, `rho<n/4`,
`N>=0.99n`, cociente de columnas `<1/3`), todas con margen amplio en
`n>=10^{40}`. Resulta

\[
\Pr_n(S)\ \ge\ \tfrac12\,n^{-(40\sqrt{n\log n}+5)}
\qquad(n\ge10^{40}),
\]

estrictamente mejor que `NC-2C` (4.14), que queda intacta. Por el Teorema 7.1 de
`NC-2E` y la transferencia de `NC-2D` §2,

\[
\operatorname{Var}_{\nu_n}(q_{n,h})\le4.2\cdot10^{7}\,n^{3/2}(\log n)^{3/2},
\qquad
\operatorname{Var}(\ell_h\mid n,h,S)\le4.3\cdot10^{7}\,\frac{(\log n)^{3/2}}{\sqrt n}.
\]

El exponente de varianza baja de `9/5` a `3/2`; ambas cotas son estrictamente
mejores que las de `NC-2D` en todo el dominio probado `n>=10^{40}`.

**`NC2F-b`.** Se probó, de forma autocontenida salvo la desigualdad exponencial
elemental de Chernoff–Bernstein (demostrada en el propio documento),

\[
\mathbb E[\Delta_n^2]\ \le\ \frac{4.2\cdot10^{4}}n
\qquad(n\ge10^{6}),
\]

sin condicionar por `S`. Esto cierra el objeto **(B)** de `NC-2E` §8 y deja la
implicación limpia: si `Pr_n(S)>=c>0`, entonces `NC2E.1` vale con
`C_q<=3.4\cdot10^{9}/c`.

**Estado del objetivo.** `NC2E-O3` sigue abierto. Tras `NC-2F` la única obligación
que resta para cerrarlo es de naturaleza puramente selectiva: una cota inferior
relativa para la masa de `S` (o, más débilmente, que la selección no infle el
segundo momento de la discrepancia).

```text
NC2F_A_TERMINAL = NC2F_A_PROVED_SQRT_SELECTION_MASS
NC2F_B_TERMINAL = NC2F_B_PROVED_L2_DISCREPANCY
NC2F_SELECTION_MASS_BOUND = (1/2)*n^(-(40*sqrt(n*log n)+5))
NC2F_VARIANCE_EXPONENT = 3/2
NC2F_UNCONDITIONAL_L2_DISCREPANCY = 4.2*10^4/n
NC2F_NC2E_O3 = OPEN
NC2F_REMAINING_OBLIGATION = LOWER_BOUND_ON_SELECTION_MASS
NC2F_LIMINF_T_N = NOT_PROVED
NC2F_NEW_DATA = NO
NC2F_NEW_CODE = NO
NC2F_SEAL_TOUCHED = NO
NC2F_PR7_MODIFIED = NO
NC2F_PRIOR_TOKENS_MODIFIED = NO
NC2F_RATIFIED_BY_PI = YES_AFTER_EXECUTION
NC2F_SIGNATURE_PRECEDES_EXECUTION = NO
```

## 9. Refrendo del PI

```text
REFRENDADO_POR: Ignacio Martín (PI)
FECHA_REFRENDO: 2026-08-18
DECISION_NC2F: REFRENDADA_A_POSTERIORI_CONFORME_A_LO_EJECUTADO
AUTHORISED_SCOPE: opción 1 (piezas (a) y (b) de §3), lista cerrada
LITERAL_SIGNOFF: "refrenda la NC-2F con firma explícita y commitea"
                 Ignacio Martín (PI), 18/08/2026
```

El refrendo cubre: los dos terminales emitidos, los dos documentos científicos de
§7 y el commit de todo ello. No amplía el perímetro de §3, no levanta ninguna
prohibición de §5, no toca el sello ni la PR #7, y no altera ningún token publicado
de `NC-2C`, `NC-2D` o `NC-2E`. La cadena vuelve al procedimiento normal —firma
previa conforme a borrador— en la siguiente autorización.

La autorización `NC-2F` queda consumida y cerrada.

## 10. Corrección posterior por auditoría adversarial (foro-002, 2026-08-19)

El brief `docs/foro/foro_decision_002_nc2fb-auditoria-adversarial.md`
(`FORO_VERDICT=REVISE_AND_RECONVENE`) confirmó el Teorema 1.1 de `NC-2F(B)` con
recómputo independiente y localizó defectos que se han corregido en el documento
científico. Esta sección se añade en modo append-only: **no reescribe** el bloque de
tokens de §8, que queda como registro histórico de lo que se afirmó el 2026-08-18.

Token de §8 que resultó **mal nombrado** y su valor correcto:

```text
NC2F_REMAINING_OBLIGATION = LOWER_BOUND_ON_SELECTION_MASS        [SUPERSEDED]
NC2F_REMAINING_OBLIGATION = RELATIVE_SUM_OF_(R+Delta_n)^2_OVER_S_n   [VIGENTE]
```

El nombre antiguo describía una **ruta suficiente** (mejorar `Pr(S)`), no la
obligación. La obligación vigente es la del Teorema 8.1 de `NC-2E`, con sus dos
términos, y `NC-2F(B)` aporta sólo la mitad correspondiente a `\Delta_n`, y sólo
incondicionalmente.

Se corrigió además el marcador de reentrada, que propagaba la versión sin `R`. La
corrección se hizo primero sobre el fichero de memoria vivo, que está **fuera del
repositorio**, y la copia commiteada
`memoria_claude/program-status-reentry-marker.md` se sincroniza en el mismo commit
que esta nota. Se deja constancia del matiz porque una verificación independiente
del parche detectó que la redacción anterior de este párrafo describía como hecho un
cambio que en ese momento aún no existía como diff en el repositorio — exactamente
el patrón «corrección que existe como texto pero no como diff» que el propio foro
había señalado (claim `C21` del brief).

El foro emitió **BLOCK** contra la acción de declarar «cerrada de forma definitiva
toda la parte incondicional del programa»: ese objeto no está definido en ninguna
parte del repositorio, ningún criterio de cierre se fijó por escrito antes de
evaluarlo, la nota `NC-2F` §9 excluye ampliaciones de perímetro, y la práctica
registrada del repositorio son once reaperturas acotadas posteriores a un cierre
declarado. Cualquier cierre de esa parte exige nota nueva firmada, con enumeración
literal de su contenido y cláusula de reapertura acotada.

```text
NC2F_ADVERSARIAL_AUDIT = FORO_002
NC2F_AUDIT_VERDICT = REVISE_AND_RECONVENE
NC2F_THEOREM_B_STATUS = CONFIRMED_WITH_CORRECTIONS_APPLIED
NC2F_DEFINITIVE_CLOSURE = BLOCKED_BY_COMMITMENT_WARDEN
```
