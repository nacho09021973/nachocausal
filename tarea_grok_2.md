# Hoja de ruta del programa — post N1–N5 y cierre del camino reconstructor

> **STATUS: PROGRAM_ROADMAP / PHASE_0_CLOSED / FASE_1_NEXT /
> NOT_A_PREREGISTRATION / NOT_A_NOVELTY_CERTIFICATE / DOES_NOT_TOUCH_SEAL /
> DOES_NOT_DISCHARGE_ITEM_5.**
>
> Documento de síntesis operativa. Integra: (i) el filtro de la respuesta adversarial
> bibliográfica sobre N1–N5; (ii) el veredicto de que la vía “otro observable order-only
> → horizonte SW 3+1” no es el camino; (iii) la distinción entre **imposibilidad demostrada**
> y **fracaso al construir**. No congela umbrales, no ejecuta código, no descarga el ítem 5
> del Paso D (lector humano independiente).
>
> FECHA: 2026-07-28 · HEAD de referencia al abrir: `e9744d8`
> **Fase 0 cerrada** con `PI_SIGN_OFF` en
> `research_program/synthesis/phase0_program_north_decision.md` §7.
> Anclas de repo: `research_program/bibliography/*`, `research_program/synthesis/*`,
> `docs/claim_grammar.md`, `docs/paper_outline_c1c6_plus_prereg002.md`

---

## 0. Veredicto en una página

### 0.1 Qué se cierra

| Decisión | Contenido | Tipo de justificación |
|---|---|---|
| **R1** | Abandonar como norte del programa la **reconstrucción / localización de horizonte SW 3+1 order-only** mediante “otro candidato” de la matriz post-PR008 | Estratégica + evidencia de ledger C1–C6 + matriz de supervivencia + OP-1.2 |
| **R2** | El producto defendible del ciclo actual es un **paper de límites de recuperabilidad** (cegueras demostradas + ledger de negativos + positivo acotado 1+1), no un reconstructor | Editorial / de claim grammar |
| **R3** | Imposibilidad se enuncia **solo** donde hay igualdad de leyes o no-funcionalidad del target; el ledger C1–C6 **no** es prueba de no-go | Epistémica (vinculante) |

### 0.2 Qué se demuestra matemáticamente (y qué no)

```text
SÍ teorema (canal + target fijos):
  (T1) Masa / escala absoluta a N=n  →  TV ≡ 0  (1+1 Teorema A; 3+1 OP-1.2)
  (T2) Horizonte de eventos GLOBAL desde un patch finito  →  no es funcional de los datos del patch
  (T3) Suelo de localización ~ n^{-1/2} en familia regular QMD  →  1+1 diamantes EF (N1);
       plantilla lista; 3+1 requiere familia regular probada

NO teorema (hoy):
  (X1) “Ningún proxy de trapping / codim-2 order-only funciona en 3+1”
  (X2) “Schwarzschild no es recoverable desde causal sets”
  (X3) “Order+number tampoco basta para la masa”
  (X4) “C1–C6 demuestran imposibilidad”

Regla de oro:
  ∀f en lista L: falla(f)   ≠   ∀f medible: riesgo(f) ≥ c
  Lo segundo exige TV / Hellinger / Fisher / par testigo, no historial de intentos.
```

### 0.3 Qué se hace con N1–N5 (propuesta de adjudicación)

| Claim | Propuesta | Motivo (post-filtro adversarial) |
|---|---|---|
| **N1** | **Mantener acotado** como instanciación (técnica de libro) | No hundido; hueco residual math.ST/PR sin peinar |
| **N2** | **Degradar a lema** (ya lo pedía el paquete §4.2) | Folclore con anclas: Dowker–Zalel, Madsen, Braun, HKMM, Malament, Zeeman/Bombelli |
| **N3** | **Remark de diseño**, no N-número | Hecho GR de libro; diagnóstico estadístico sin prior hallado |
| **N4** | **Debilitar** a corolario dimensional de N2 + reparametrización | `κ = V·I` adimensional por análisis dimensional; no medalla de novedad |
| **N5** | **Retirar** como contribución | DPI de libro + disciplina de redacción; analogía: information–computation gaps |

**Ítem 5 del Paso D sigue pendiente:** ninguna salida de LLM lo descarga. Solo un lector humano independiente.

---

## 1. Parte A — Registro del filtro bibliográfico (tarea_grok_1 → verificación)

> Esta sección archiva el resultado del filtro humano sobre la respuesta adversarial.
> Procedencia: pista vía LLM (Grok), citas re-verificadas a fuente primaria por el operador /
> revisor del paquete. Cumple la nota de procedencia tipo §6.6 del paquete adversarial.

### 1.1 Citas verificadas (cero inventadas en el lote filtrado)

| Cita | Verificación |
|---|---|
| Dowker & Zalel, arXiv:1703.07556 | «lacking only information about local physical scale»; «Number plus Order equals Geometry, in R. Sorkin's slogan» — verbatim |
| Madsen, arXiv:2607.05840 | «the causal order alone is famously insufficient (this is essentially the content of Müller's negative result)» — verbatim |
| Braun, arXiv:2507.01907 | §1.1; §3.3 «Order». Conformal isometry…; §3.4 «Number». Isometry by volume-preservation — títulos exactos |
| HKMM 1976 | J. Math. Phys. **17**, 174–181 — vía ref. de Braun |
| Malament 1977 | J. Math. Phys. **18**, 1399–1404 — vía ref. de Braun |
| Bombelli 1987 PhD | Zeeman: isomorfismos causales Minkowski = Poincaré + dilataciones; métrica «up to a global scale factor» — `biblioteca/derived-md/` |
| Boguñá–Krioukov PRD 110, 024008 | Escala de discreción \(\rho^{-1/(d+1)}\) con \(d\) espacial — literal en fuente |

**Artefacto irrelevante del LLM:** la frase «genovesa de rank statistics» en una tabla de literaturas no peinadas es ruido; ignorar.

### 1.2 Qué cambia de verdad respecto al paquete

1. **N2/N5 frágiles:** el paquete ya lo declaraba. Grok no lo descubrió; **coincidió**.
2. **Ganancia real N2:** anclas publicadas (sobre todo Zeeman en Bombelli 1987) donde antes había “patrimonio de la disciplina”. La vía de refutación §4.2(7) del paquete queda parcialmente satisfecha en el **continuo**; el TV=0 discreto del Teorema A sigue siendo formalización exacta del canal \(N=n\), no descubrimiento físico.
3. **Golpe técnico sobre N4:** invariancia de \(\kappa = V\cdot I\) bajo dilatación es, en lo esencial, **análisis dimensional** + el hecho de que \(\Phi_s\) preserva cocientes adimensionales (hermano de N2). Re-evaluar §4.4 del paquete: no vender como teorema de novedad.
4. **N1 intacto como claim de instanciación**; riesgo residual: paper math.ST/PR 1990–2015 con dos puntos sobre funcional de PPP + parámetro de posición. **Hueco de lectura humana Tier B sigue abierto.**
5. **Literaturas a añadir al peinado:** shape theory (Kendall, Dryden–Mardia); cópulas/rangos (Joe, Nelsen); information–computation gaps (para la *disciplina* de N5, no como prior del mapa CST).

### 1.3 Acciones bibliográficas pendientes (operativas)

| # | Acción | Quién | Descarga ítem 5? |
|---|---|---|---|
| B1 | Incorporar las 6+ anclas a §7 del paquete adversarial con nota «pista LLM, verificada a mano» | Operador | No |
| B2 | Ampliar §3.1 candidatos externos con shape / cópulas / minimax PPP + términos de búsqueda | Operador | No |
| B3 | Adjudicación formal de estatus N2/N4/N5 (esta hoja propone; el PI confirma) | PI | No |
| B4 | Lectura humana independiente (Tier A causal sets + Tier B estadística) | Externo | **Sí** |
| B5 | Archivar respuesta cruda LLM fuera del árbol git (o en anexo no normativo) | Operador | No |

---

## 2. Parte B — Diagnóstico del camino que se abandona

### 2.1 El paquete fallido (tres ambiciones a la vez)

```text
Target:   horizonte / región atrapada / codim-2 / evento
Canal:    order-only (poset no etiquetado; a menudo N=n)
Ambición: transferir a Schwarzschild 3+1
```

No ha fallado “causal sets”. Ha fallado **esta conjunción**.

### 2.2 Evidencia que motiva el abandono (sin confundirla con teorema)

| Fuente | Qué dice | Qué NO dice |
|---|---|---|
| Ledger C1–C6 | Seis vías de localización de *región* cerradas en este banco | Imposibilidad de todo proxy futuro |
| Matriz 1+1→3+1 | `tau` como localizador `DOES_NOT_TRANSFER` | Que 3+1 sea inaccesible en todo canal |
| OP-1.2 | Clase TV=0 de masas a `fixed_n` en SW 3+1 | Que order+number también sea ciego a M |
| N2 / Teorema A | Escala absoluta ciega a N=n | Ceguera a localización relativa en unidades de ℓ o del patch |
| Físico del comité (1+1) | `τ` es radio **y** curvatura; no hay umbral en el horizonte | No-go 3+1 de trapping |
| claim_grammar §3 | Horizonte global no es objeto de un patch finito | Que no exista proxy cuasi-local legítimo |

### 2.3 Prohibición operativa (R1)

```text
NO abrir nuevos candidatos de la forma:
  "observable order-only X que localiza horizonte / trapping / codim-2 en SW 3+1"

NO interpretar almost-PASS o retuning de H_hat / ladders / cuts como reapertura del norte.

SÍ permitir trabajo teórico de no-go (pares testigo, TV, Fisher) sobre targets bien nombrados.
SÍ permitir cambio de canal (Order+Number) o de target (no-horizonte) como programa NUEVO
  con nombre y claim grammar propios — no como "continuación" del reconstructor.
```

---

## 3. Parte C — Principio de no-identificabilidad (forma matemática, no Heisenberg)

### 3.1 Forma canónica (la única que se puede demostrar)

Sea \(K\) un canal de observación, \(P\) un patch, \(G\) una familia de geometrías, \(T:G\to\Theta\) un target.

**Lema maestro (data processing + igualdad de leyes).**  
Si \(g_0,g_1\in G\) cumplen \(T(g_0)\neq T(g_1)\) y \(\mathrm{Law}_K(g_0)=\mathrm{Law}_K(g_1)\), entonces para todo estimador (aleatorizado) \(\widehat T\) medible respecto de \(K\),

\[
\max\bigl\{\mathbb{E}_{g_0} d(\widehat T,T(g_0)),\;
           \mathbb{E}_{g_1} d(\widehat T,T(g_1))\bigr\}
\ge \tfrac12\, d\bigl(T(g_0),T(g_1)\bigr)
\]

(en la métrica de decisión usual; el factor exacto depende de la pérdida, pero el mensaje es: **riesgo no puede anularse en ambos extremos**).

**Corolario de contigüidad / Hellinger:** si \(\mathrm{TV}\le\varepsilon\), el riesgo minimax está acotado por debajo en función de \(\varepsilon\) y de la separación de targets (Le Cam / dos puntos).

Esto **no** usa la existencia o no de un estimador construido por el proyecto.

### 3.2 Tres teoremas del programa (capas del “principio”)

#### (T1) Ceguera exacta de escala / masa — PROVED (formalizar y unificar en el paper)

| | |
|---|---|
| **Canal** | Order-only, \(N=n\) (medida de volumen normalizada) |
| **Familia** | Schwarzschild, forma de patch \(\lambda\) fija, sector fijo |
| **Target** | \(M\) o \(r_s\) en unidades absolutas |
| **Conclusión** | \(\mathrm{TV}=0\) en la órbita de dilatación/coescalado ⇒ no-identificabilidad exacta |
| **Anclas** | `first_witness_pair_candidates.md` Teorema A (1+1); `op12_tv_zero_3p1.md` (3+1) |
| **Background** | Dowker–Zalel; Madsen; Braun Order vs Number; HKMM/Malament; Zeeman/Bombelli |

**Enunciado para paper (sin medalla de novedad física):** formalización exacta del folclore Order+Number en el canal \(N=n\), con prueba de tres líneas / coescalado.

#### (T2) Horizonte de eventos global no es funcional del patch — PROVED (definición + claim_grammar)

| | |
|---|---|
| **Datos** | Cualquier estructura inducida solo en un patch finito \(P\) |
| **Target** | Horizonte de eventos de la spacetime completa |
| **Conclusión** | Existen extensiones que coinciden en \(P\) y difieren en el horizonte global ⇒ no hay mapa datos\(_P\) → horizonte global |
| **Ancla** | `docs/claim_grammar.md` §3; teleología en `geometric_indeterminacy_decision.md` |

**Enunciado para paper:** cierra el *paquete reconstructor fuerte*, no los proxies cuasi-locales.

#### (T3) Suelo de resolución en familias regulares — PROVED en 1+1 (N1); OPEN en 3+1

| | |
|---|---|
| **Canal** | Order-only, \(N=n\) |
| **Hipótesis** | Familia uniparamétrica QMD con \(\bar I<\infty\) |
| **Conclusión** | Ningún procedimiento order-only localiza por debajo de \(\sim 1/\sqrt{n\bar I}\) |
| **Ancla** | `wp4_fisher_localization_floor.md` |
| **Límite de claim** | No afirma que la cota sea ajustada para posets (data processing desde puntos); no afirma 3+1 |

### 3.3 Corolario de programa (no es un teorema único numerado)

```text
El paquete
  (reconstruir SW 3+1 con horizonte + order-only + patch finito + a menudo N=n)
está bloqueado por (T1)+(T2) en el target fuerte, y acotado por (T3) en parámetros
continuos de forma en las familias donde aplica.

Eso NO implica un no-go de "causal sets no ven agujeros negros".
Eso SÍ implica: dejar de buscar el observable X del mismo paquete.
```

### 3.4 Cómo se atacaría un no-go **más fuerte** (opcional, no prioritario)

Para “imposible localizar proxy \(Q\) order-only en familia 3+1 \(G\)”:

1. Congelar \(G, P, K, Q\).  
2. Exhibir \(g_0,g_1\) con \(Q(g_0)\neq Q(g_1)\).  
3. Probar \(\mathrm{TV}(P_{g_0},P_{g_1})=0\) o \(\le\varepsilon\).  
4. Aplicar el lema maestro.

Método: **construcción de adversarios** (estilo Müller), no más estimadores.  
Si no existe tal par, \(Q\) podría ser identificable y el ledger solo habría fallado al construirlo — y entonces **no hay teorema**.

---

## 4. Parte D — Hoja de ruta secuenciada

### Fase 0 — Gobernanza (esta semana documental)

| Paso | Entrega | Criterio de hecho |
|---|---|---|
| 0.1 | PI confirma o enmienda **R1–R3** y la tabla N1–N5 de §0.3 | Acta breve o commit de esta hoja con `PI_SIGN_OFF` |
| 0.2 | Marcar en matriz de candidatos / plan operativo: norte reconstructor horizonte 3+1 = `ABANDONED_AS_PROGRAM_NORTH` | Un párrafo en `next_observable_candidate_matrix` o plan operativo: no autoriza kill tests de nuevos localizadores de horizonte |
| 0.3 | Separar vocabulario: `EMPIRICAL_FAILURE_OF_CLASS_L` vs `PROVED_NON_IDENTIFIABILITY` | Usar en paper outline y comités |

**No hacer en Fase 0:** código nuevo, semillas, tocar sello, abrir PR de estimador.

### Fase 1 — Paper de límites (producto principal del ciclo)

**Título de trabajo (ejemplo):**  
*Finite order-only observation of Schwarzschild patches: exact scale blindness, localization floors, and a ledger of failed region-locators — not a reconstruction claim.*

| Sección del paper | Material del repo | Claim permitido |
|---|---|---|
| 1. Claim grammar | `docs/claim_grammar.md` | Qué no se afirma |
| 2. Positivo acotado 1+1 | PR002 / future volume | Recoverability de *señal geométrica*, no horizonte |
| 3. Ledger C1–C6 | outline + decisiones 039–044 | Negativos tipados; método |
| 4. (T1) Ceguera de escala | Teorema A + OP-1.2 + citas folclore | Lema; Order+Number |
| 5. (T3) Suelo Fisher/dos puntos | WP4 floor | Instanciación; técnica de libro |
| 6. (T2) Horizonte global | claim_grammar | No-funcionalidad |
| 7. Mapa de ceguera (sin N5-medalla) | WP5 definición, 2–4 frases de disciplina DPI | Organización, no novedad |
| 8. Qué queda abierto | order+number; targets no-horizonte; alta densidad | Explicitamente fuera de alcance |

**Condiciones de escritura:**

- N2 y N4 no van en la lista de “contribuciones principales”.  
- N5 no es contribución.  
- N1 solo como instanciación acotada.  
- C1–C6 en sección empírica/metodológica, **no** como demostración de (T1)–(T3).  
- Una frase en abstract: *this is not a path to 3+1 event-horizon reconstruction from finite order-only data*.

**Gate de Fase 1:** outline congelado + adjudicación N1–N5 + anclas file:line en cada teorema.  
Aún **sin** ítem 5 cumplido no hay claim público de *novedad* de N1; el paper puede escribirse como límites con citas de background.

### Fase 2 — Cerrar bibliografía de novedad (paralelo a Fase 1, no bloquea redactar límites)

| Paso | Entrega |
|---|---|
| 2.1 | Meter anclas §1.1 en paquete adversarial §7 |
| 2.2 | Lista de búsqueda math.ST/PR (términos de la respuesta adversarial) ejecutada por humano o con API, con log |
| 2.3 | Envío ítem 5: al menos un lector Tier A y, si se puede, uno Tier B |
| 2.4 | Si Tier B hunde N1: retirar o reescribir N1 antes de cualquier abstract “first lower bound…” |

### Fase 3 — Bifurcaciones **después** del paper de límites (elegir como máximo una)

Solo se abre si Fase 1 tiene manuscript interno estable y R1 sigue en vigor.

| Opción | Pregunta nueva | Canal | Target | Primer teorema/experimento |
|---|---|---|---|---|
| **B1** | ¿Qué de SW es recuperable con **Order+Number** (\(\rho\) conocida)? | Poisson + orden | Masa relativa, distancias, no horizonte global | Separación de \(M\) vía \(N\sim\mathrm{Poisson}(\rho V(M))\); contrastar OP-1.2 §5 |
| **B2** | Mapa de identificabilidad **puro** (más pares testigo) | Order-only o mixto | Parámetros adimensionales / forma | Par testigo estilo Müller para un proxy \(Q\) nombrado, o prueba de que no existe |
| **B3** | Clasificación / curvatura / manifoldlikeness (línea EGS, BD) | Order-only o grafo de Hasse | Clase, no localización de horizonte | Banco de clases (Eichhorn et al.), no SW-horizon |
| **B4** | Parar investigación empírica; solo mantenimiento del banco | — | — | Repo como artefacto de recuperabilidad |

**Prohibido como “Fase 3 disfrazada”:** reabrir matriz A/B/C de localizadores de horizonte order-only.

### Fase 4 — Explicitamente fuera de ruta hasta nuevo PI sign-off

- Reconstrucción métrica completa 3+1 desde poset finito.  
- Horizonte de eventos global desde patch.  
- Claims de convergencia al horizonte a caja fija sin `density_limit` / `patch_limit` separados.  
- Mezclar order-only con embedding en el scoring y seguir llamándolo order-only.

---

## 5. Parte E — Criterios de éxito y de parada

### 5.1 Éxito del programa en el horizonte de este documento

1. Existe un manuscript (aunque sea pre-arXiv) cuyo **claim principal** es límites de recuperabilidad, anclado a (T1)–(T3) + ledger.  
2. Ningún documento activo del repo presenta “localizar horizonte SW 3+1 order-only” como objetivo abierto sin etiqueta `ABANDONED`.  
3. Toda imposibilidad citada en el manuscript es de tipo (T1)/(T2)/(T3) o par testigo nuevo; **ninguna** cita el ledger como prueba de no-go.  
4. N2/N4/N5 no se cuentan como novedades independientes.  
5. Ítem 5: o bien descargado con lectura externa, o bien el manuscript **no** afirma novedad de N1.

### 5.2 Señales de que se está reincidiendo (parar y releer §2)

- Nuevo `dev/explore_*.py` cuyo target es “horizonte” / trapping sin cambio de canal ni de claim grammar.  
- Comité convocado para “un candidato más” de la matriz post-PR008 sin matar R1.  
- Abstract que diga “towards reconstructing black hole horizons from causal sets” sin la negación explícita del paquete finito order-only.  
- Usar “principio de indeterminación” sin fijar \(G,T,K,P\).

### 5.3 Qué contaría como *falso* el abandono R1

Solo evidencia **positiva** de identificabilidad del target fuerte bajo el canal fuerte, p.ej.:

- par de geometrías SW 3+1 con horizontes (proxies \(Q\)) distintos y leyes order-only **separables** a tasa controlada, **más** un estimador que alcanza esa tasa bajo pre-registro;

no: un almost-PASS en un proxy 1+1 ya conocido.

---

## 6. Parte F — Mapa de anclas (file → rol en la ruta)

| Archivo | Rol |
|---|---|
| `research_program/models/first_witness_pair_candidates.md` | (T1) 1+1 |
| `research_program/synthesis/op12_tv_zero_3p1.md` | (T1) 3+1 |
| `research_program/work_packages/wp4_fisher_localization_floor.md` | (T3) |
| `research_program/synthesis/geometric_indeterminacy_decision.md` | Framing minimax; exclusiones Heisenberg |
| `research_program/taxonomy/identifiability_taxonomy.md` | Capas recoverability / minimax / no-go |
| `docs/claim_grammar.md` | (T2) + formas prohibidas |
| `docs/paper_outline_c1c6_plus_prereg002.md` | Esqueleto paper límites + ledger |
| `research_program/synthesis/survival_matrix_1p1_to_3p1.md` | Por qué `tau` no financia 3+1 |
| `research_program/bibliography/external_adversarial_review_package_n1_n5.md` | N1–N5 + vía de refutación |
| `research_program/bibliography/external_reader_candidates_n1_n5.md` | Tier A/B; hueco math.ST |
| `research_program/bibliography/wp5_paso_d_independent_novelty_review.md` | Paso D; ítem 5 |
| `research_program/work_packages/next_observable_candidate_matrix.md` | Matriz a marcar abandoned-as-north |
| `tarea_grok_1.md` | Prompt adversarial original |
| `instruccion_grok.md` | Protocolo anti-invención LLM |
| **este archivo** | Hoja de ruta unificada |

---

## 7. Checklist de adjudicación PI (rellenar)

> **Fase 0 cerrada 2026-07-28.** Checklist firmado en
> `research_program/synthesis/phase0_program_north_decision.md` §7.
> Siguiente: **Fase 1** (paper de límites). Ítem 5 sigue pendiente.

```text
[x] R1 — Abandonar norte reconstructor horizonte SW 3+1 order-only
[x] R2 — Producto del ciclo = paper de límites
[x] R3 — Ledger ≠ prueba de no-go
[x] N1 — mantener acotado / enmienda: ninguna
[x] N2 — degradar a lema / enmienda: ninguna
[x] N3 — remark de diseño / enmienda: ninguna
[x] N4 — debilitar a corolario dimensional / enmienda: ninguna
[x] N5 — retirar como contribución / enmienda: ninguna
[x] Fase 3 preferida: B2 (default)
[ ] Ítem 5: plan de envío a lector(es): ________  (pendiente; no bloquea Fase 1 sin claim de novedad N1)
[x] 0.2 — banner en next_observable_candidate_matrix (2026-07-28)
[x] 0.3 — vocabulario en phase0 §3 + taxonomy §4.4 (2026-07-28)

PI_SIGN_OFF: Ignacio (PI / Nacho) — sesión 2026-07-28
FECHA: 2026-07-28
HEAD al firmar: e9744d8 (lote Fase 0 commiteado a continuación)
```

---

## 8. Resumen ejecutivo final

1. **Bibliografía:** el lote adversarial filtrado es usable; ancla N2 al folclore con localizadores; deflacta N4; no hunde N1; no descarga el ítem 5.  
2. **Estrategia:** dejar de buscar el observable que reconstruya SW 3+1 order-only; ese no es el camino.  
3. **Matemática:** sí hay no-gos demostrables — **igualdad de leyes** (masa a \(N=n\)) y **no-funcionalidad** (horizonte global) y **suelos de tasa** (familia regular) — **sin** basarse en “no supimos construirlo”.  
4. **Producto:** paper de límites de recuperabilidad con claim grammar estricto.  
5. **Después (opcional):** Order+Number, otros targets, o más teoría de pares testigo — cada uno como programa nuevo, no como reincidencia.

> **Una frase de gobierno:**  
> *El orden finito no etiquetado, en un patch y a cardinalidad fija, no es el canal con el que se reconstruye un horizonte de Schwarzschild 3+1; es el canal con el que se demuestran, con pruebas de igualdad de medidas y de definición de objetos, los límites de lo que ese experimento puede ver.*
