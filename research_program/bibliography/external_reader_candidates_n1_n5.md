# Candidatos a lector externo independiente — N1–N5

> **STATUS: WORKING_LIST / PHASE_2_RESPONSES_REGISTERED /
> NOT_A_NOVELTY_CERTIFICATE / ITEM_5_DISCHARGED_BOTH_TIERS.**
> Instrumento de trabajo para el ítem 5 de `wp5_paso_d_independent_novelty_review.md` §6. No ejecuta
> código, no consume semillas, no toca el sello, no congela nada y **no sostiene ningún claim
> científico**. Identificar candidatos por sí solo **no** descarga el ítem 5; en esta revisión,
> las respuestas efectivas de ambos tiers sí lo descargaron bajo la regla §4.1. Registro:
> `phase2_novelty_and_item5.md` §3.
>
> FECHA: 2026-07-28 · HEAD ref Fase 2 `66cec59` · Sello
> `thresholds.py sha256 = 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (intacto)

**Alcance deliberadamente limitado de este documento.** Contiene sólo datos bibliográficos públicos
y la correspondencia entre cada fuente y las afirmaciones N1–N5 que esa fuente está en posición de
refutar. **No contiene valoraciones personales de investigadores** —ni de disponibilidad, ni de
antigüedad, ni de motivación— por la razón obvia de que este repositorio es público y las personas
listadas no han consentido ser evaluadas en él. Las consideraciones tácticas de envío se mantienen
fuera del repositorio.

**Procedencia de los datos.** Nombres, títulos, identificadores y afiliaciones marcados
`VERIFICADO` se extrajeron de la **primera página del PDF primario** en `biblioteca/` (comando
`pdftotext -f 1 -l 1`, sesión 2026-07-28). Lo marcado `[UNVERIFIED]` no se comprobó y requiere
búsqueda antes de usarse. Este documento **no contiene direcciones de correo**.

---

## 1. Por qué la lista tiene dos tiers y no un ranking

`external_adversarial_review_package_n1_n5.md` §7 declara que el hueco principal **no peinado** de la
búsqueda es *inferencia geométrica / procesos puntuales en variedades*, y que ese hueco afecta a
**N1 y N4** — las dos afirmaciones que cargan la maquinaria estadística.

De ahí la consecuencia que organiza la lista:

> La literatura que podría contener antecedente de **N1/N4** no es la literatura de causal sets. Un
> lector de teoría de causal sets está en posición de refutar **N2, N3 y N5**, y de juzgar si la
> comparación de §5 con Müller 2025 es fiel. No está en posición de saber si un suelo de estimación
> tipo dos-puntos para un canal de orden ya está publicado en probabilidad o en estadística no
> paramétrica.

Por tanto la cobertura de N1–N5 **requiere dos comunidades**, y un envío restringido a una sola deja
afirmaciones sin examinar por quien sabe. Ver §4.

---

## 2. Tier A — causal sets / reconstrucción lorentziana

Cobertura: **N2, N3, N5**, y la fidelidad de §5.

| # | Fuente primaria | Verificación | Cubre | Anclaje del contraste en el repo |
|---|---|---|---|---|
| A1 | **M. Braun**, *Spacetime Reconstruction by Order and Number*, arXiv:2507.01907v1 [gr-qc], 2 Jul 2025 | `VERIFICADO` (`biblioteca/2507.01907v1.pdf`); afiliación no en portada `[UNVERIFIED]` | **N1, N2** | `wp4_fisher_localization_floor.md` §9 (:500–514) registra **tres separaciones** frente a su Teorema 1.4: (i) su hipótesis permanente es `d ≥ 3` y el régimen del proyecto es `d = 2` — la rigidez tipo HKMM es justo lo que falta en 2D; (ii) su observable son matrices **etiquetadas** para todo `k`, y su propio Rmk 3.10 declara que la versión **no etiquetada** (conjetura de Bombelli) **sigue abierta** — ése es el canal del proyecto; (iii) el par por dilatación del Teorema A **muestra la necesidad de su hipótesis de volúmenes iguales**. Las separaciones (i) y (iii) son afirmaciones *sobre su artículo* y su autor está en posición de adjudicarlas |
| A2 | **O. Müller**, *On the Hauptvermutung of Causal Set Theory*, arXiv:2503.01719v2 [math.DG], 29 Dec 2025 | `VERIFICADO` (`biblioteca/2503.01719v2.pdf`); afiliación no en portada `[UNVERIFIED]` | **N2**, marginalmente N1 | Su Teorema 2 es el **pariente publicado más cercano** reconocido por el repo (`wp4_fisher_localization_floor.md` §9, ficha TV §8 `CONFIRMED_DIRECT`). §5 del paquete y la pregunta 3 de §8.1 se dirigen a este resultado |
| A3 | **N. Madsen**, *On the Uniqueness of Embeddings of Causal Sets*, arXiv:2607.05840v1 [gr-qc], 7 Jul 2026 | `VERIFICADO`; afiliación `VERIFICADO`: Dept. of Physics **y** Dept. of Mathematics, University of California, Santa Barbara | **N2, N5** | Unicidad de embeddings = identificabilidad en otro vocabulario; fuente ya usada en el repo por su «order alone famously insufficient» |
| A4 | **A. Eichhorn, P. Gamito, N. Stokes**, *Towards black-hole horizons and geodesic focusing in causal sets*, arXiv:2605.06813v1 [gr-qc], 7 May 2026 | `VERIFICADO`; afiliación `VERIFICADO`: Institute for Theoretical Physics, Heidelberg University | **N5, N3** | Artículo directamente relevante (`CLAUDE.md`). El ledger del proyecto caracteriza sus *fuzzy ladders* como «no order-only en el sentido estricto del repo» (matriz biblio §1) — caracterización que estos autores están en posición de impugnar |
| A5 | **A. Eichhorn** *et al.*, dos frentes adicionales: arXiv:2301.13525v2 (con G. P. de Brito y C. Pfeiffer; CP3-Origins, University of Southern Denmark; Pfeiffer también Niels Bohr Institute, Copenhagen) y arXiv:2605.27514v1 (con H. Mack, K. T. Le, F. Wagner; ITP + Scientific Software Center, Heidelberg University) | `VERIFICADO` | contexto de curvatura | Ambos verificados en REV-1 del paso D; `2605.27514` corrobora la varianza prohibitiva de invariantes de curvatura (respaldo externo al terminal 046) |
| A6 | **S. Surya**, **F. Dowker** — presencia en `biblioteca/` vía arXiv:2209.00327 (Carlip–Carlip–Surya), arXiv:1309.3403 (Glaser–Surya), arXiv:2505.22217 (Benincasa–Dowker–Glaser) | presencia `VERIFICADO`; afiliaciones `[UNVERIFIED]` | control de **sobre-afirmación** transversal | No cubren prioridad técnica fina de N1; cubren la pregunta «¿el paquete afirma más de lo que sostiene?», que requiere conocer el corpus y su folclore |

---

## 3. Tier B — procesos puntuales de Poisson / geometría estocástica

Cobertura: **N1, N4** — el hueco declarado en §7 del paquete. **Sin un lector de este tier, N1 y N4
quedan sin examinar por el flanco que el propio paquete admite no haber peinado.**

| # | Fuente primaria | Verificación | Cubre | Anclaje |
|---|---|---|---|---|
| B1 | **T. Trauthwein, J. E. Yukich**, *Second-order Poincaré inequalities and localization on the Poisson space*, arXiv:2605.23292v1 [math.PR], 22 May 2026 | `VERIFICADO` (`biblioteca/2605.23292v1.pdf`); afiliaciones no en portada `[UNVERIFIED]` | **N1, N4** | **El proyecto ya depende de este resultado:** `comite_decision_007` re-calificó el Lema L1 de `IMPOSSIBLE` a `OPEN-CONTINGENT` apoyándose en su Teorema 2.1 (p.5) y su Def. 2.3 de BL-localización (p.8). Comunidad exacta del hueco: funcionales de medidas de Poisson en espacios métricos, Malliavin–Stein, tasas de aproximación normal |
| B2 | **M. Boguñá, D. Krioukov**, *Measuring spatial distances in causal sets via causal overlaps*, Phys. Rev. D **110**, 024008 (8 Jul 2024), DOI 10.1103/PhysRevD.110.024008 | `VERIFICADO` (`biblioteca/PhysRevD.110.024008-accepted.pdf`) | **N1** | Inferencia geométrica desde orden causal con tasa de error explícita `~1/√(ρV)`: **anverso positivo** del suelo inferior de N1 (acotan por arriba lo que N1 acota por abajo). Comunidad de ciencia de redes / física estadística, distinta de la de gravedad cuántica |

### 3.1 Hueco no cerrado + literaturas ampliadas (Fase 2)

La comunidad de **estadística minimax** —quien aplica el método de dos puntos de Le Cam/Tsybakov a
inferencia sobre variedades o procesos puntuales— es el centro del hueco de §7, y **esta lista no
contiene ningún candidato verificado de ella**. `biblioteca/Tsybakov_Nonparametric_Estimation.pdf` es
un libro de texto, no un interlocutor.

**Fase 2 (2026-07-28):** peinado abstract-level documentado en
`phase2_novelty_and_item5.md` §2 (`PHASE2_ST_PR_SWEEP = NO_N1_SINK_FOUND`). Vecinos de método
anotados allí (Ray–Schmidt-Hieber arXiv:1608.01824; Polyanskiy–Wu arXiv:1902.05616; Birgé Poisson
model selection; Trauthwein–Yukich ya es B1). **No** se rellenó la lista con nombres de
estadísticos sin ancla a PDF primario en `biblioteca/`.

**Subcampos y términos para peinado / para el revisor Tier B** (ampliación del diagnóstico
adversarial; no son autores contactados):

| Subcampo | Términos / referencias de entrada | Cubre |
|---|---|---|
| Minimax + PPP | `two-point method Poisson process`, `Hellinger affinity point process`, `minimax intensity estimation` | N1 |
| Geometric inference | `minimax manifold estimation`, `support estimation lower bound` | N1 |
| Random geometric graphs / latent space | Bubeck–Ding–Eldan–Rácz como pista de comunidad `READER_LEAD_UNVERIFIED`; `unlabeled geometric graph minimax lower bound`, `latent position DAG` | N1 |
| Shape theory | Kendall; Dryden–Mardia; `Procrustes Fisher information` | N2/N4 conceptual |
| Cópula / ranks | Joe; Nelsen; `semiparametric efficiency copula` | order-only ≈ rank |
| Info–computation gaps | Abbe; Decelle–Krzakala–Moore–Zdeborová | disciplina ex-N5 |

Vías de cierre del hueco de interlocutor minimax (ninguna es envío aún):

1. Localizar citas de Tsybakov cap. 2 en `math.PR`/`math.ST` reciente con PDF verificable y
   retener **un** B3 con fuente primaria en `biblioteca/`.
2. Preguntar a B1 (Trauthwein–Yukich línea) por un colega minimax — **fuera del repo**, sin
   almacenar correo aquí.
3. Ejecutar el protocolo de envío de `phase2_novelty_and_item5.md` §3.

---

## 4. Consecuencia de gobernanza: la letra del ítem 5

El ítem 5 de `wp5_paso_d_independent_novelty_review.md` §6 está redactado así:

> «identificar un lector competente en **causal set theory** sin implicación en el proyecto»

Los candidatos del **Tier B no son teóricos de causal sets**. Satisfacen el *espíritu* del ítem
—lector independiente y competente, capaz de examinar el hueco declarado— pero **no su letra**. La
combinación de ambos hechos produce una situación que conviene resolver **antes** de enviar, no
después:

- Un envío restringido al **Tier A** descargaría el ítem 5 *en su letra* dejando **N1 y N4** sin
  examinar por la comunidad que podría contener su antecedente.
- Un envío restringido al **Tier B** examinaría el hueco pero **no** descargaría el ítem en su letra.

Dos salidas admisibles, **decisión del PI, no de este documento**:

- **(a)** Exigir respuesta de **ambos tiers** para descargar el ítem 5. Es la lectura estricta.
- **(b)** Enmendar la letra del ítem 5 a «lector competente **en el canal de la afirmación**», con
  nota fechada, reconociendo que N1/N4 y N2/N3/N5 viven en comunidades distintas.

### 4.1 Resolución del PI (fechada)

```text
ITEM_5_DISCHARGE_RULE = SALIDA_(a)_AMBOS_TIERS
DECIDIDO_POR: PI
FECHA: 2026-07-28
ESTADO_EN_LA_FECHA: ningún envío realizado (decisión tomada antes de ver respuesta alguna)
```

**Contenido de la regla.** El ítem 5 **no** se marca descargado hasta que exista respuesta
registrada de **un lector Tier A y un lector Tier B**. Consecuencias:

- Una respuesta Tier A sola cierra la *letra* del ítem pero deja N1/N4 sin examinar por la
  comunidad que podría contener su antecedente → ítem 5 **abierto**.
- Una respuesta Tier B sola examina el hueco de §7 pero no satisface la letra → ítem 5 **abierto**.
- `DECLINED` o `NO_REPLY` en cualquiera de los dos tiers → ítem 5 **abierto**; el manuscript
  conserva el hedge de N1 y arXiv sigue bloqueado para lenguaje de primacía
  (`phase2_novelty_and_item5.md` §3.1, §5).

La decisión se toma **antes** de cualquier envío precisamente para que la lectura de la regla no
pueda elegirse después en función de lo que responda quien responda.

### 4.2 Ejecución de la regla

El 2026-07-28 quedaron registradas respuestas de ambos tiers en
`phase2_novelty_and_item5.md` §3.4–§3.6. Por tanto:

```text
ITEM_5_DISCHARGE_RULE = SALIDA_(a)_AMBOS_TIERS
ITEM_5_STATUS = DISCHARGED_BOTH_TIERS_2026-07-28
NOVELTY_CERTIFIED = NO
```

La descarga es procedimental. La adjudicación sustantiva es escenario (B): N1 queda como
instanciación acotada, con Müller Thm 3 reconocido como precursor cuantitativo y con la maquinaria
estadística declarada estándar.

**Salida explícitamente inadmisible:** obtener un `APPARENTLY_DISTINCT` del Tier A y marcar el ítem 5
como descargado. Eso dejaría el hueco de §7 intacto con un sello encima, que es la forma exacta de
guardarraíl-que-no-puede-fallar que la regla fundacional prohíbe.

---

## 5. Regla de uso de las respuestas

Aplicable a cualquier respuesta que se reciba, y fijada **antes** de recibir ninguna:

1. **Un `APPARENTLY_DISTINCT` no establece novedad.** El propio formulario (§8.2 del paquete) lo
   define como «no le consta antecedente». El estado de N1–N5 tras una respuesta favorable sigue
   siendo un claim **acotado y comparativo**, nunca novedad como hecho.
2. **Una respuesta de autor cuyo resultado el paquete compara en §5 no es evidencia de
   independencia.** Sirve —y sirve mucho— como intento de refutación por quien mejor conoce la
   frontera; no como certificación externa neutral. Las dos funciones no son intercambiables y no
   deben citarse la una por la otra.
3. **Una sola referencia que hunda un claim vale más que cualquier número de respuestas
   favorables.** Es la asimetría que el paquete pide explícitamente en su §1.
4. **Ninguna respuesta autoriza a redactar §6 del paper como sección definitiva** mientras el ítem 5
   siga abierto en la lectura elegida en §4.
