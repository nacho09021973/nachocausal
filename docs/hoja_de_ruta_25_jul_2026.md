# Hoja de ruta — 25 jul 2026 · paso 1 de la hoja del 24 jul ejecutado (`p(theta) != p(theta')`)

> **Plan REVISABLE, no congelado.** No es pre-registración, no fija umbrales, no autoriza
> ejecuciones ni implementaciones por sí mismo. Mantener `RESPECT_SEAL_FREEZE`,
> `NO_RECONSTRUCTION_CLAIM`, `NO_GROUND_TRUTH_LEAKAGE`, `NO_POST_HOC_TUNING` y
> `NO_THRESHOLD_LOOSENING`. Registro de sesión, una por fecha; no sustituye a las hojas anteriores
> (`docs/hoja_de_ruta_23_jun_2026.md` … `docs/hoja_de_ruta_24_jul_2026.md`, `docs/roadmap.md`) ni
> al marcador de pausa.

## 0. Relación con la pausa del programa

El programa sigue en `PROGRAMA_EN_PAUSA_LIMPIA` (`docs/marcador_reentrada_2026-07-19.md`, firmado
PI). El trabajo de hoy es **el paso 1 de `docs/hoja_de_ruta_24_jul_2026.md` §2**, que esa hoja
autorizaba explícitamente como cálculo: *"Es un cálculo simbólico/analítico — una integral doble
sobre una cópula ya definida en el repo — no una ejecución ni una implementación de estimador."*
No se ejecutó ningún script del banco sellado, no se tocó `nachocausal/thresholds.py`, no se
convocó `/comite`, no se reabrió C1–C7, no se abrió ningún candidato. Sello sin drift:
`6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
(= `docs/preregistration_002.md:8`).

## 1. Qué se hizo hoy

1. **WP4 Anexo C** — `research_program/work_packages/wp4_comparable_pair_separation.md` +
   `wp4_comparable_pair_separation_checks.py`. Contenido, en orden de dependencia:
   - **Reducción exacta `[PROVED]`.** La integral cuádruple de concordancia sobre `D_tau x D_tau`
     colapsa a una doble con integrando analítico. Piezas: el integral de un rayo nulo saliente vale
     `rho(r_0,D)^2 - r_0^2 + tau*D` (Lema C1), de donde
     `vol(J^+(x) ^ J^-(q)) = rho(r_x,D)^2 + rho(r_q,-D)^2 - r_x^2 - r_q^2` (Prop C2). Reutilizable
     para cualquier conteo de la familia, no sólo para `p`.
   - **Asintótica cerrada `[PROVED (orden dominante)]`.**
     `p(tau) = 1/2 + kappa(r_p,r_q)*tau*dv + O(dv^2)`, con
     `kappa = [(r_p^2-r_q^2) - 2 r_p r_q log(r_p/r_q)] / [12 r_p r_q (r_p-r_q)^2] > 0`
     (positividad probada). El término dominante es estrictamente proporcional a `tau`: de ahí
     `p(tau) != p(tau')`.
   - **Verificación numérica** en un par concreto (`r_p=3`, `r_q=0.5`, `tau=1.0` vs `1.2`),
     cuadratura estable a 15 dígitos, más cross-check Monte-Carlo con semilla fija.
   - **Test de la órbita (ficha §4) pasado**: `p = (1 + tau_K)/2` es funcional de la cópula, ciego
     a la órbita de escala del Teorema A — comprobado a `< 1e-15`. Un candidato que separase un par
     del Teorema A sería inválido; este no puede.
2. **Auditoría, dos pasadas.** `docs/auditor/auditor_report_024_...md` salió **`AUDIT_FAIL`**: un
   error real de procedencia (tres valores de `V(tau)` citados en la nota que **ningún script
   commiteado emitía**, provenientes de un comando ad-hoc, en la sección que sostiene el argumento
   central de honestidad) más cuatro warnings de etiquetado. Corregidos los cinco —nuevo check
   `[4b]` que emite y **asegura** esos volúmenes, recuento honesto de los pasos argumentados,
   cuantificador de `dv_0`, precisión `1.11e-15`, atribución del «78 sigma»— la re-auditoría
   `auditor_report_025_...md` da **`AUDIT_PASS_WITH_WARNINGS`** (0 errores; los 23 warnings son la
   línea base preexistente del repo, ajena a este objeto).
3. **Ficha actualizada a v4** (`research_program/bibliography/ficha_se_busca_tv_order_only.md`),
   sólo tras la auditoría en verde, como exigía la hoja del 24 jul §2.4: nueva §2.2, ingrediente (a)
   de §7.1 marcado cerrado **para la familia diamante** (y explícitamente `[OPEN por par]` para las
   demás), fila de Reitzner–Schulte de §8 con el obstáculo desplazado al canal, y declarada la
   inconsistencia de convención del factor 2 entre §7.1 y §2.1(B).

## 2. Lo que esto cambia — y lo que no

**Cambia:** el obstáculo del candidato 7.1 ya **no** es la desigualdad escalar. Los ingredientes 1
(separación de medias) y 2 (fluctuaciones, vía Reitzner–Schulte) de ficha §6 están ambos en mano
para una familia con nombre.

**No cambia:** **Forma L sigue `[OPEN]`**, y el hueco central de §2 (cotas inferiores a nivel poset)
sigue abierto. El obstáculo se ha **desplazado al canal**, que es un problema distinto y no
menor:

1. La CLT importada vive en Poisson **sin condicionar**, donde `V(tau)` dependiente de `tau`
   (`11.501608349297` vs `10.794261266781` a `dv=4`) hace que la marginal `N` separe sola — el
   mecanismo trivial que ficha §1.2/§9.2 prohíben contar.
2. A `fixed_n` falta un paso de des-Poissonización que Reitzner–Schulte no da.
3. La no degeneración de la varianza a `fixed_n` (`Var S_n = Theta(n^3)`) no se calculó.
4. El chequeo obligatorio de ficha §6.4 pasa **sólo a nivel de tasas**; a nivel de constantes falta
   `Ibar` para estas esquinas y `zeta_1`.

Una separación de medias sin cota de TV no es una Forma L: es literalmente el segundo guión de la
lista de descarte de ficha §9.2. Esta hoja lo deja escrito para que la v4 de la ficha no se lea
como más de lo que es.

## 3. Próximos pasos (ninguno ejecutado ni autorizado por este documento)

Orden de prioridad, uno cada vez. Los tres primeros son cálculos del mismo género que el de hoy
(compatibles con la pausa); el cuarto no lo es.

1. **`zeta_1` y la varianza a `fixed_n`** (punto 3 de §2). Es el paso más barato y el que más
   desbloquea: `h_1(x) = P(x comparable con Y)` es un cociente de volúmenes de sub-diamante ya en
   forma cerrada por Prop C2, luego `zeta_1 = Var(h_1(X))` es otra integral doble con la misma
   maquinaria. Cierra el ingrediente que falta para el paso Chebyshev de §6.3 y, con `Ibar`,
   permitiría el chequeo de §6.4 a nivel de constantes.
2. **Des-Poissonización a `fixed_n`** (punto 2). Buscar en la literatura (coto 1 sigue abierto) un
   teorema que transporte la CLT de U-estadísticos de Poisson al modelo binomial/`fixed_n` con tasa;
   es un hueco bibliográfico bien definido, no un cálculo.
3. **Promoción de la rigidez de cópulas a lema citado** — paso 2 pendiente de la hoja del 24 jul
   §2, no tocado hoy: evaluar si el Teorema 7.1 de Janson (Borel + no-gemelos) cubre nuestra clase,
   o si conviene mantener el argumento diferencial-geométrico propio (FWP §4) como razón
   independiente.
4. **Cotos 2-4 de la ficha** (LIS/récords; límites de posets y Bombelli; procesos parcialmente
   observados), en ese orden.

Regla que sigue en pie (hoja del 24 jul §2.4, ya ejercida hoy y con un `AUDIT_FAIL` real que lo
justifica): cualquier resultado que parezca cerrar una Forma L/U/D pasa por `/auditor` antes de
tocar estados `[PROVED]`/`[OPEN]`, y por `/comite` antes de convertirse en decisión de programa.

## 4. No hacer

- No presentar el candidato 7.1 como Forma L. Ni «casi». Los cuatro puntos de §2 son bloqueos, no
  detalles de redacción.
- No convertir el Anexo C en implementación de estimador, ni abrir un `CANDIDATE_7`: la
  recomendación viva del marcador de reentrada (consolidar, no observable nuevo) no ha cambiado, y
  nada de hoy la toca.
- No ejecutar `dev/pr011_tv_certification_enumeration.py` ni ningún script del banco sellado.
- No tocar `nachocausal/thresholds.py` ni ningún umbral congelado.
- No extrapolar el resultado a otras familias: `kappa > 0` es un enunciado sobre la familia diamante
  de WP4 §4. Para OP-1.1/1.2 el ingrediente (a) sigue `[OPEN por par]`.
- No leer la monotonía en `tau` como global: a `dv = 4` (fuera del régimen asintótico) `p`
  **decrece** en `tau`. El teorema es asintótico.

## 5. Checklist antes de cerrar la sesión

1. `make verify-seal` debe seguir dando
   `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`. ✔ (verificado)
2. El script del Anexo C debe salir con exit 0 y dos corridas byte-idénticas. ✔ (verificado)
3. Todo literal numérico de la nota debe aparecer verbatim en la salida del script. ✔ (17/17,
   verificado en `auditor_report_025` §4)
4. `git status --short` debe mostrar sólo: los dos ficheros del Anexo C, los dos reportes de
   auditoría, la ficha v4 y esta hoja.
