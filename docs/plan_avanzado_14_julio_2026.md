# Plan avanzado — 14 julio 2026

Documento de situación local: dónde está el programa **nachocausal**, qué está cerrado con respaldo verificable, y qué falta en la cadena hacia **Schwarzschild 3+1D order-only**. No es preregistro ni autorización de ejecución.

**Commit de referencia al redactar:** `9a5e3df` (certificación PR011 en `n=5`).

---

## Destino del programa

El objetivo estratégico prioritario (ver `README.md`) es **localización/recuperación del horizonte Schwarzschild en 3+1D** usando solo información causal (orden + cardinalidad donde corresponda). Las coordenadas del embedding sirven para simulación, validación y ground truth, **nunca** como entrada del estimador order-only.

El trabajo 1+1D actual es **cimiento estructural**, no el resultado final. No implica que lo demostrado en 1+1D se transfiera automáticamente a 3+1D.

---

## Dónde estamos

Dos frentes que no deben mezclarse:

### A. Recoverability empírica — parche 1+1D, estimador sellado

| Hito | Estado | Notas |
|------|--------|-------|
| **prereg-002** | **PASS** | Localización order-only del horizonte en parche finito 1+1D Schwarzschild (`docs/preregistration_002_result.md`) |
| **prereg-003** | Sellado | Cota operacional O(ℓ) del estimador v2; **no** es minimax sobre toda estadística order-only |
| **PR008** | Cerrado | Terminal `BASELINE_DOMINATED` |
| **PR009** | Cerrado sin ciencia | `FAILED_DATA_CONTRACT`; sin artefacto ni scorer publicado |
| **PR010** | Cerrado diseño | `PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`; artefacto `data/reports/pr010_reference_depth_coverage_development.csv` |

**Límite de interpretación:** el observable de prereg-002 depende del mecanismo de **futuros truncados por singularidad** en 1+1D. No es un resultado de horizonte genérico ni de 3+1D (`research_program/README.md` §1.2, matriz bibliográfica).

### B. Identificabilidad teórica — WP4 / PR011

| Hito | Estado | Notas |
|------|--------|-------|
| Teorema dos puntos, Teorema A (TV=0 por escala), piso Fisher diamante | Matemática en repo | `research_program/work_packages/wp4_two_point_theorem.md`, etc. |
| **PR011** spec | `FROZEN_VIABILITY_SPEC` | `research_program/synthesis/pr011_mass_distinguishability_viability.md` |
| **G0b / G2b** | Descargados | `auditor_report_008`, `auditor_report_009` |
| **Viabilidad certificada** | `n=4`, `n=5` | Terminal `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` |
| Método | `HELLINGER_FALLBACK` (§6.1) | Cuadratura primaria en rejilla no cierra tier-1 a M tractable |
| Artefactos | Publicados | `data/reports/pr011_tv_certification_n4.csv`, `pr011_tv_certification_n5.csv` (+ `.sha256`) |
| Escalera `n ∈ {6,7,8}` | **Abierta** | |
| Estimación de masa / prerreg ciego | **No abierto** | |

**ε certificado (cota superior, ambos &lt; 1):**

| `n` | `epsilon_certified_upper` | Generador |
|-----|---------------------------|-----------|
| 4 | `0.004611899229` | `python3 dev/pr011_tv_certification_enumeration.py certify --n 4` |
| 5 | `0.005764874036` | `python3 dev/pr011_tv_certification_enumeration.py certify --n 5` |

PR011 responde: *¿el orden solo, condicionado a `N=n`, distingue dos masas en la familia diamante EF 1+1D?* No es un protocolo de recuperación de horizonte ni un claim 3+1D.

---

## Tres capas de claim (recordatorio)

Del `research_program/README.md` §2:

1. **Límite del estimador** — el pipeline concreto falla o satura (parcialmente cerrado en 1+1D).
2. **Límite de una familia de observables** — abierto en general.
3. **Límite intrínseco del orden** — objetivo fuerte del programa; **no cerrado**.

No confundir recoverability empírica (capa 1) con indeterminación intrínseca (capa 3).

---

## Qué falta en la cadena 1+1D (antes de subir dimensión)

Orden lógico según `geometric_indeterminacy_decision.md` §15 y PR011 §11:

1. **Cerrar escalera PR011** — certificar `n=6, 7, 8` (misma ruta Hellinger o enumeración si algún día cierra tier-1).
2. **PR012 (escalado)** — curva TV vs `Δτ`, posiblemente escalera en `ρ` y `n`, con prerregistro propio.
3. **Prerregistro de estimación de masa** — solo tras viabilidad + curva TV; bandas dev/confirmación nuevas; sin inputs PR009/PR010.
4. **Separar mecanismos** — singularity-imprint vs horizonte genérico (tabla §3 del programa de investigación).
5. **Observable / cobertura** — PR010 cerró infeasible; retomar expansión efectiva exige nuevo diseño o canal distinto.

Todo lo anterior permanece en **1+1D, familia `G_◊` controlada, parche finito**.

---

## Pasos hacia Schwarzschild 3+1D order-only

La síntesis WP4 fija: **ningún claim 3+1D hasta que la viabilidad escalar cierre en la familia 1+1D controlada** (`geometric_indeterminacy_decision.md` §15).

```
prereg-002 (localización 1+1D)          ✓ hecho
        ↓
PR011 viabilidad masa τ en G_◊          → en curso (n=4,5 ✓; n=6–8 pendiente)
        ↓
PR012 / estimación τ certificada        → no abierto
        ↓
Puente dimensional explícito           → no especificado en repo
  · familia 3+1D Schwarzschild (biblioteca: He–Rideout, Homšak–Veroni)
  · canal order-only + cardinalidad en 3+1D
  · observable que no replique solo el mecanismo 1+1D singular
        ↓
Recoverability o indeterminación en 3+1D  → claim aparte; capa (3) abierta
```

**Lo que 3+1D exigiría además** (todo **OPEN** en el repositorio):

- Definir **familia estadística 3+1D** y canal de observación.
- Elegir **observable** transferible (no el longest-chain 1+1D tal cual).
- **Prerregistro + auditoría** independientes del sellado 1+1D.
- Demostrar recoverability o acotar indeterminación en ese régimen — **sin inferir desde 1+1D**.

---

## En una frase

Hay **localización empírica 1+1D** (prereg-002) y **viabilidad teórica de distinguir masa** en diamante 1+1D (PR011, `n=4`–`5`). El camino a **SW 3+1D** pasa por cerrar identificabilidad escalar en 1+1D, abrir estimación certificada, y solo entonces un **puente dimensional** con familia, observable y protocolo propios — sin saltar dimensiones ni mezclar recoverability con reconstrucción métrica global.

---

## Referencias rápidas

| Tema | Ruta |
|------|------|
| Programa de investigación | `research_program/README.md` |
| PR011 spec y §13 estado | `research_program/synthesis/pr011_mass_distinguishability_viability.md` |
| Síntesis WP4 / puente PR011 | `research_program/synthesis/geometric_indeterminacy_decision.md` |
| Certificación TV | `dev/pr011_tv_certification_enumeration.py` |
| Auditoría G2b | `docs/auditor/auditor_report_008_*.md`, `auditor_report_009_*.md` |
| PR010 cierre | `dev/PR010_REFERENCE_DEPTH_COVERAGE_DECISION.md` |
| Objetivo 3+1D | `README.md` (Strategic objectives §1) |