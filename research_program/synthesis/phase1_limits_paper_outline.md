# Fase 1 — Outline del paper de límites de recuperabilidad

> **STATUS: PHASE_1_OPEN / OUTLINE_AUTHORITATIVE_FOR_MANUSCRIPT /
> NOT_A_CLAIM / NOT_FROZEN / NO_NEW_SCIENCE / DOES_NOT_TOUCH_SEAL /
> DOES_NOT_DISCHARGE_ITEM_5.**
>
> Producto R2 de Fase 0 (`phase0_program_north_decision.md`). Este outline **gobierna**
> la redacción del manuscript de límites. Supersede el *norte* de
> `docs/paper_outline_c1c6_plus_prereg002.md` (ese archivo queda como **fuente de material**
> para §3–§5 y el ledger, no como tesis del paper).
>
> FECHA DE APERTURA: 2026-07-28 · HEAD de referencia: `6787260`
> Precedencia de programa: Fase 0 cerrada (R1–R3, N1–N5). Norte reconstructor horizonte
> SW 3+1 order-only = `ABANDONED_AS_PROGRAM_NORTH`.

**Guardarraíles (sin excepción en el manuscript):**

```text
NO_RECONSTRUCTION_CLAIM
NO_POST_HOC_TUNING
NO_THRESHOLD_LOOSENING
NO_GROUND_TRUTH_LEAKAGE
RESPECT_SEAL_FREEZE
R3: ledger = EMPIRICAL_FAILURE_OF_CLASS_L
    no-go = PROVED_NON_IDENTIFIABILITY only
```

---

## 0. Título, tesis, lo que el paper es y no es

### 0.1 Título de trabajo

**English (working):**  
*Finite order-only observation of Schwarzschild patches: exact scale blindness, localization floors, and a typed ledger of failed region-locators*

**Spanish (working):**  
*Observación order-only de parches de Schwarzschild: ceguera exacta de escala, suelos de localización y un ledger tipado de localizadores de región fallidos*

**Subtítulo obligatorio en abstract o nota al pie de título:**  
*A recoverability-limits paper — not a path to 3+1 event-horizon reconstruction from finite unlabeled order.*

### 0.2 Tesis (una frase)

En el canal **order-only** (poset no etiquetado; a menudo condicionado a \(N=n\)), sobre **parches finitos** de Schwarzschild, se demuestran **límites de identificabilidad** (escala absoluta; horizonte de eventos global; suelo de tasa en familias regulares 1+1) y se documenta un **ledger** de seis vías de localización de *región* agotadas en este banco; el único positivo sellado del banco es de **recoverability acotada** de una señal geométrica order-only, no de reconstrucción de horizonte.

### 0.3 Tres pilares (orden de aparición en el paper = orden de peso)

| Pilar | Etiqueta | ¿Es “contribución principal”? |
|---|---|---|
| **P1** No-identificabilidad demostrada (T1)–(T3) | `PROVED_NON_IDENTIFIABILITY` | **Sí** — el corazón del paper |
| **P2** Ledger C1–C6 | `EMPIRICAL_FAILURE_OF_CLASS_L` | **Sí** — como evidencia tipada de banco, no como no-go |
| **P3** Positivo prereg-002 (volumen de futuro) | `VALIDATED` / caveats de re-verificación | **Sí, acotado** — el canal no está vacío; el target fuerte sí está bloqueado |

### 0.4 Qué el abstract **debe** decir y **no** decir

**Debe:**

- recoverability benchmark / limits paper;
- order-only, finite patch, 1+1 primary arena; 3+1 only where TV=0 de masa está probado;
- exact scale/mass blindness at \(N=n\);
- localization floor in a regular 1+1 family;
- global event horizon is not a functional of finite-patch data;
- six-channel negative ledger (empirical failure of a named class);
- one sealed in-patch positive (future-volume), not horizon reconstruction.

**No debe:**

- “we reconstruct the black hole horizon”;
- “causal sets cannot see black holes” (demasiado amplio);
- “N2/N4/N5 are novel contributions”;
- “C1–C6 prove impossibility of all horizon proxies”;
- “3+1 horizon localization is solved / almost solved”.

### 0.5 Adjudicación N\* en el manuscript (Fase 0, vinculante)

| N\* | En el paper |
|---|---|
| N1 | Instanciación acotada del suelo (T3); técnica Le Cam/Hellinger = libro |
| N2 | **Lema** (T1); citas Order+Number / Zeeman / Madsen / Braun |
| N3 | Remark en diseño de familia (Kruskal) |
| N4 | Corolario dimensional / reparametrización; no teorema de novedad |
| N5 | **No** es contribución; 2–4 frases de disciplina DPI en notación |

**Ítem 5 Paso D:** si el manuscript afirma novedad de N1/T3, el ítem 5 debe estar descargado o el wording debe ser “to our knowledge / pending independent literature check” sin “first in the literature” absoluto.

---

## 1. Índice del manuscript (secciones)

### §1 Introduction and claim grammar

**Función:** fijar el experimento y matar la lectura reconstructor desde el primer párrafo.

| Bloque | Contenido | Anclas |
|---|---|---|
| 1.1 | Recoverability vs reconstruction | `docs/claim_grammar.md`; `CLAUDE.md` |
| 1.2 | Observation channel: unlabeled poset; `fixed_n` vs order+number | FWP; taxonomy |
| 1.3 | Hidden embedding scores only | prereg discipline |
| 1.4 | Three objects: global event horizon / singularity truncation / quasi-local proxy | claim_grammar §3 |
| 1.5 | Program north abandoned for 3+1 order-only horizon locators | Fase 0 R1 |
| 1.6 | Contributions list (P1–P3 only; N2/N5 not listed) | este outline §0.3 |

**Frase de cierre de §1 (plantilla):**

> We do not claim to reconstruct a Schwarzschild event horizon from a finite causal set. We map what the finite order-only channel can and cannot identify under frozen contracts.

### §2 Setup: geometry, sprinkling, targets

| Bloque | Contenido | Anclas |
|---|---|---|
| 2.1 | 1+1 Schwarzschild; EF corners; diamond family \(G_{\mathrm{diamond}}\) | `wp4_fisher_localization_floor.md` §4 |
| 2.2 | 3+1 only as needed for (T1): co-scaled patches, fixed shape \(\lambda\) | `op12_tv_zero_3p1.md` |
| 2.3 | Poisson sprinkling; laws \(P_{g,n}\), \(P_{g,\rho}\) | FWP; geometric_indeterminacy_decision |
| 2.4 | Targets \(T\): absolute mass/scale; continuous shape parameter \(\tau\); global horizon; in-patch score targets | claim_grammar lista 1–12 |
| 2.5 | Vocabulary: `EMPIRICAL_FAILURE_OF_CLASS_L` vs `PROVED_NON_IDENTIFIABILITY` | taxonomy §4.4; Fase 0 §3 |

### §3 Proved non-identifiability (Pilar P1)

Esta es la sección **matemática** principal. Tres subsecciones = (T1)(T2)(T3).

#### §3.1 (T1) Exact scale / mass blindness at \(N=n\)

| | |
|---|---|
| **Claim** | For fixed patch shape (and fixed temporal sector in 3+1), absolute \(M\) or \(r_s\) is non-identifiable from the unlabeled order conditioned on \(N=n\): \(\mathrm{TV}=0\) along the dilation/co-scaling orbit. |
| **Etiqueta** | `PROVED_NON_IDENTIFIABILITY` |
| **Proof sketch** | Constant conformal / metric co-scaling + volume normalization ⇒ identical normalized measures ⇒ identical poset laws (coupling lemma). |
| **1+1** | Teorema A — `first_witness_pair_candidates.md` §2 |
| **3+1** | `op12_tv_zero_3p1.md` §3 |
| **What it is not** | Not blindness to *relative* location in units of \(\ell\), patch size, or \(M\); not TV=0 in order+number with known \(\rho\). |
| **Background (lemma, not novelty)** | Dowker–Zalel arXiv:1703.07556; Madsen arXiv:2607.05840; Braun arXiv:2507.01907 §§3.3–3.4; HKMM 1976; Malament 1977; Zeeman via Bombelli 1987 PhD |
| **N\*** | Former N2 → **lemma** |

#### §3.2 (T2) Global event horizon is not a finite-patch functional

| | |
|---|---|
| **Claim** | The global event horizon of a complete spacetime is not determined by the causal set (or even the continuum geometry) restricted to a single finite patch: distinct extensions can agree on the patch and disagree on the horizon. |
| **Etiqueta** | `PROVED_NON_IDENTIFIABILITY` (definitional / teleological) |
| **Ancla** | `docs/claim_grammar.md` §3; geometric_indeterminacy notes on teleology |
| **What it is not** | Does **not** by itself kill quasi-local trapping / expansion proxies. |

#### §3.3 (T3) Localization floor in a regular 1+1 family

| | |
|---|---|
| **Claim** | For the EF-corner diamond family with proved QMD and finite \(\bar I\), in the order-only \(N=n\) channel, \(\mathrm{TV}(Q^n_\tau,Q^n_{\tau+\delta})\le C|\delta|\sqrt{n\bar I}\); hence no order-only estimator (randomized included) localizes \(\tau\) below the corresponding two-point threshold. |
| **Etiqueta** | `PROVED_NON_IDENTIFIABILITY` (rate / minimax lower bound via two-point) |
| **Ancla** | `wp4_fisher_localization_floor.md` §4–§5; symbolic checks script |
| **What it is not** | Bound may be loose for posets (data processing from points); \(\bar I\) finiteness proved, not necessarily numerically computed for reference corners; not a 3+1 theorem; not “horizon information”. |
| **Physics caveat (mandatory)** | In 1+1 Schwarzschild, \(\tau\) is simultaneously horizon radius and curvature amplitude; no threshold structure at \(r=\tau\). **Forbidden:** calling (T3) “horizon detection information”. |
| **N\*** | Former N1 → **bounded instantiation**; Le Cam/Hellinger = textbook |
| **Related optional paragraph** | Ordering-fraction / Chebyshev lower separation when \(\Delta_p\neq 0\) (material outline antiguo §6.1) — only if C3/C4 of comité 045 are closed; otherwise omit or mark `OPEN` |

#### §3.4 Design remark: sterile Kruskal-box mass family (ex-N3)

Short paragraph: fixed Kruskal box ⇒ mass dependence cancels after normalization ⇒ Fisher zero.  
**Not** a numbered contribution. Ancla: `wp4_fisher_localization_floor.md` Prop. 1 / §2.

#### §3.5 Dimensional corollary: \(\kappa=V\cdot I\) (ex-N4)

One paragraph: under dilation, \(V\cdot I\) is dimensionless; intrinsic floor \(\delta_n/\ell\sim 1/\sqrt{\bar\kappa}\).  
**Not** a novelty theorem. Present as reparametrization / units.

#### §3.6 Notational discipline (ex-N5, two–four sentences)

Upper bounds / data processing prove blindness regions; they do **not** prove visibility outside them. Label residual regions “candidate visible”, never “visible”.  
Cite DPI as textbook; optional analogy to information–computation gaps in other fields — **no** “blindness map contribution”.

### §4 Sealed in-patch positive (Pilar P3)

| Bloque | Contenido | Anclas |
|---|---|---|
| 4.1 | Pre-registration contract | `docs/preregistration_002.md` |
| 4.2 | Result and caveats | `docs/preregistration_002_result.md` — PASS with `PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY` |
| 4.3 | Supervised re-verification | comité 016; `prereg002_reverification_*` |
| 4.4 | What the positive **is** | Order-only future-volume localizes an in-patch geometric signal under frozen thresholds |
| 4.5 | What it **is not** | Not global horizon; not 3+1; not proof that region-locators work; embedding only scores |

**Rol retórico:** el canal order-only **no es vacíamente ciego** a toda geometría; por eso los no-gos de §3 son interesantes y el ledger de §5 no es “no hay información en el orden”.

### §5 Typed negative ledger C1–C6 (Pilar P2)

| Bloque | Contenido | Anclas |
|---|---|---|
| 5.1 | Method: documenting failures with terminals is a result | decision 042 §5.7 |
| 5.2 | Master table (C3-early … C6) | outline antiguo §4; decisiones 039–044 |
| 5.3 | Cross-cutting structural lessons | ceiling/wall; no lateral pairing; scale↔depth; no stable codim-2 screen |
| 5.4 | Case study C6 (optional depth) | antichain waist; comité 043→044 self-correction vignette |
| 5.5 | **Mandatory label** | Entire section = `EMPIRICAL_FAILURE_OF_CLASS_L` for the named locator class in this bank — **not** (T1)–(T3) |

**Frase prohibida en §5:** “therefore it is impossible to localize a horizon order-only.”  
**Frase permitida:** “within this bank and this named class of constructions, every channel terminated as listed; this does not replace the measure-theoretic limits of §3.”

Material reutilizable: `docs/paper_outline_c1c6_plus_prereg002.md` §§4–6.

### §6 Relation to literature

| Tema | Fuentes | Mensaje |
|---|---|---|
| Order + Number | Dowker–Zalel; Braun; Madsen; Bombelli/Zeeman | Background for (T1) as formalized folklore |
| Continuum causal determination | HKMM; Malament | Order → conformal; scale missing |
| Indistinguishability constructions | Müller arXiv:2503.01719 | Closest published relative for *qualitative* order indistinguishability; no Fisher rates |
| Constructive distances | Boguñá–Krioukov PRD 110, 024008 | Upper rates from causal overlaps; opposite direction to (T3) |
| Horizon phenomenology in CST | Eichhorn–Gamito–Stokes arXiv:2605.06813 | Motivates quasi-local ideas; does not supply order-only codim-2 in our sense |
| Curvature / observables | BD, BDG, Eichhorn et al. graph observables | Classification / curvature, not our abandoned north |
| Methods | Tsybakov / Le Cam textbook | Technique for (T3) |

### §7 What remains open (and what is abandoned)

| Item | Status |
|---|---|
| New order-only SW 3+1 horizon region-locators (matrix A–C, etc.) | **`ABANDONED_AS_PROGRAM_NORTH`** (Fase 0 R1) |
| Absolute mass at \(N=n\) | **Closed** by (T1) — non-identifiable |
| Global event horizon from finite patch | **Closed** by (T2) |
| Rate-optimal constants / \(\bar I\) numerics for (T3) | `OPEN` / numerical reference only where marked |
| 3+1 regular family + Fisher floor | `OPEN` (template only) |
| Order+number with known \(\rho\): mass separation | Open as **new program** (Fase 3 option B1); OP-1.2 §5 already notes Poisson means differ |
| Witness-pair no-gos for named quasi-local \(Q\) | Open as Fase 3 **B2** (preferred after manuscript) |
| Independent novelty check for N1/T3 (ítem 5) | Pending; wording discipline in §0.5 |

### §8 Conclusions

- Restate P1–P3 in one paragraph each with correct labels.  
- One sentence: this is not a reconstruction pathway for 3+1 horizons from finite order-only data.  
- Optional: next scientific step is B2 (adversarial pairs), not another estimator of the abandoned north.

### Appendices (as needed)

| App | Content |
|---|---|
| A | Full proof of (T1) 1+1 + 3+1 co-scaling |
| B | Full proof of (T3) / QMD regularity sketch + symbolic check pointer |
| C | Antichain theorem for C6 (if §5.4 kept long) |
| D | Prereg-002 contract summary + seal hash pointer (no seal change) |

---

## 2. Abstract skeleton (English, ≤200 words)

```text
We study what can and cannot be recovered from the isomorphism class of a finite
causal set obtained by Poisson sprinkling into a Schwarzschild region, when only
the unlabeled order (often conditioned on cardinality N=n) is observed. We prove
three non-identifiability statements: (i) absolute mass (horizon radius in absolute
units) is exactly non-identifiable at fixed n under patch-shape-preserving
dilations/co-scalings in 1+1 and 3+1; (ii) the global event horizon is not a
functional of any single finite-patch observation; (iii) in a regular one-parameter
1+1 diamond family with finite Fisher information, no order-only procedure can
localize the parameter below a two-point rate ~ n^{-1/2}. These are measure-theoretic
and definitional limits, not failures of particular estimators. Separately, we
report a sealed in-patch recoverability PASS for a future-volume observable under
a frozen pre-registration, and a typed ledger of six exhausted region-localization
channels in the same 1+1 bank, labeled as empirical failure of a named construction
class rather than as a universal no-go. The paper is a recoverability-limits
benchmark: it is not a claim that black-hole horizons have been reconstructed from
causal sets, nor a pathway to 3+1 event-horizon reconstruction from finite
order-only data alone.
```

---

## 3. Plan de redacción (Fase 1 — pasos)

| Paso | Entrega | Gate |
|---|---|---|
| **1.1** | Este outline (hecho al abrir Fase 1) | PI no objeta estructura |
| **1.2** | §3 draft (T1)–(T3) — **HECHO** `phase1_section3_nonidentifiability_draft.md` (2026-07-28) | Cada claim con etiqueta + ancla file |
| **1.3** | §1–§2 + abstract — **HECHO** `phase1_section1_2_abstract_draft.md` (2026-07-28) | claim_grammar; abandoned north; setup |
| **1.4** | §4–§5 — **HECHO** `phase1_section4_5_positive_ledger_draft.md` (2026-07-28) | P3 prereg-002; P2 ledger R3 labels |
| **1.5** | §6–§8 — **HECHO** `phase1_section6_7_8_draft.md` (2026-07-28) | literature; open/abandoned; conclusions |
| **1.6** | Full merge — **HECHO** `docs/manuscript_limits_draft.md` (ensamblado; polish pendiente) | Internal only; no arXiv until ítem 5 policy applied |
| **1.7** | Self-audit pass: every number has generator or `[UNVERIFIED]` | Auditor optional |

**Paralelo (Fase 2, no bloquea 1.2–1.5):** anclas biblio en paquete adversarial; plan ítem 5.

**No en Fase 1:** código de estimadores, kill tests de matriz A–C, reabrir norte R1, tocar sello.

---

## 4. Claim cards (una por resultado principal)

### Card T1 — Scale blindness

```text
DIMENSION: 1+1 and 3+1 Schwarzschild (stated separately)
FAMILY: fixed patch shape λ; fixed sector in 3+1
CHANNEL: order-only, N=n
TARGET: absolute M or r_s
LOSS: any metric on absolute mass
GUARANTEE: TV=0 ⇒ minimax risk ≥ half-separation on mass interval
LABEL: PROVED_NON_IDENTIFIABILITY
ANCHORS: first_witness_pair_candidates.md §2; op12_tv_zero_3p1.md §3
NOT: relative location; order+number with known ρ
```

### Card T2 — Global horizon

```text
DIMENSION: any (definitional)
FAMILY: spacetimes with a finite observed patch P
CHANNEL: any data determined by P alone
TARGET: global event horizon of the completion
GUARANTEE: not a functional of data on P
LABEL: PROVED_NON_IDENTIFIABILITY
ANCHOR: docs/claim_grammar.md §3
NOT: quasi-local proxies
```

### Card T3 — Localization floor

```text
DIMENSION: 1+1
FAMILY: EF diamond family with proved QMD, Ībar < ∞
CHANNEL: order-only, N=n
TARGET: continuous parameter τ (shape/location in family — NOT “horizon” as physics name)
GUARANTEE: two-point TV bound ⇒ rate lower bound ~ n^{-1/2}
LABEL: PROVED_NON_IDENTIFIABILITY (rate)
ANCHOR: wp4_fisher_localization_floor.md §4–§5
NOT: tight constant; 3+1; horizon-threshold physics
NOVELTY WORDING: bounded instantiation; technique textbook; ítem 5 if “first”
```

### Card P3 — Prereg-002 positive

```text
DIMENSION: 1+1 bank
CHANNEL: order-only future-volume observable under frozen prereg
TARGET: in-patch geometric localization score (as defined in prereg-002)
LABEL: VALIDATED with documented caveats on primary artifact
ANCHORS: preregistration_002.md; preregistration_002_result.md; comité 016
NOT: global horizon; 3+1 reconstruction
```

### Card L — Ledger C1–C6

```text
CLASS L: named localization constructions C1–C6 in this bank
LABEL: EMPIRICAL_FAILURE_OF_CLASS_L
ANCHORS: comite decisions 039–044; paper_outline_c1c6… table
NOT: proof that every possible order-only map fails
```

---

## 5. Relación con documentos previos

| Documento | Rol tras apertura Fase 1 |
|---|---|
| `phase0_program_north_decision.md` | Gobierna norte y N\*; cerrado |
| `tarea_grok_2.md` | Hoja de ruta Fases 0–4 |
| `docs/paper_outline_c1c6_plus_prereg002.md` | **Material** para §4–§5; tesis antigua (“un positivo + seis negativos como mensaje principal”) **reordenada**: P1 matemático primero |
| `docs/claim_grammar.md` | Normativo para wording |
| `geometric_indeterminacy_decision.md` | Framing minimax; exclusiones Heisenberg |
| Paquete adversarial N1–N5 | Biblio; ítem 5 pendiente |

---

## 6. Checklist de apertura Fase 1

```text
[x] Outline escrito con tesis de límites (no reconstructor)
[x] P1–P3 ordenados; N2/N5 degradados en el plan de redacción
[x] Claim cards T1–T3, P3, L
[x] Abstract skeleton
[x] Plan de pasos 1.2–1.7
[x] Precedencia sobre outline C1–C6 antiguo declarada
[x] Paso 1.2 — draft §3 (T1)–(T3): phase1_section3_nonidentifiability_draft.md
[x] Paso 1.3 — abstract + §1 + §2: phase1_section1_2_abstract_draft.md
[x] Paso 1.4 — §4 positivo + §5 ledger: phase1_section4_5_positive_ledger_draft.md
[x] Paso 1.5 — §6–§8: phase1_section6_7_8_draft.md
[x] Paso 1.6 (merge) — docs/manuscript_limits_draft.md ensamblado
[ ] PI / red-team de wording (manuscript completo)
[ ] Paso 1.6b polish: dedupe Lemma 0 / channel text entre §2 y §3
[ ] Paso 1.7 — number audit / `[UNVERIFIED]` sweep

PHASE_1_OPENED: 2026-07-28
HEAD al abrir outline: 6787260
PASO_1_2 … 1.5: 2026-07-28 (section drafts + merge)
NEXT: PI review; optional polish 1.6b; number audit 1.7; Fase 2 (biblio/ítem 5) en paralelo
```

---

## 7. Frase de gobierno (repetir en intro del manuscript)

> *The finite unlabeled order, on a patch and at fixed cardinality, is not the channel with which one reconstructs a 3+1 Schwarzschild event horizon; it is the channel with which one proves, by equality of laws and by definition of global objects, the limits of what that experiment can see — and with which one can still validate bounded in-patch recoverability of a carefully contracted geometric score.*
