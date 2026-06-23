# Hoja de ruta — 23 jun 2026 · PR-003: de *localizar* a *construir*

> **Plan REVISABLE, no congelado.** Este documento no es una pre-registración y no fija ningún
> umbral vinculante. Las reglas y los criterios de éxito que aquí se nombran se congelan
> formalmente, cada uno en su documento sellado, **antes** de cualquier paso *committing* (reglas
> fundacionales en `CLAUDE.md` y `docs/preregistration.md`). Sucesor de `docs/roadmap.md`.

## Punto de partida (verificado)

- **prereg-002 `PASS`** (`docs/preregistration_002_result.md`, sello `6e2c3888…`): localización
  *order-only* del borde asociado al horizonte en un parche finito 1+1D, a ciegas y bajo protocolo
  congelado.
- **Claim acotada:** localización — **no** reconstrucción de métrica, **no** horizonte global,
  **no** 3+1D, **no** Kerr.
- **Objetivo de PR-003:** cambiar *qué devuelve el estimador* — de «el borde está entre X e Y» a
  un **subconjunto ordenado de elementos** del causal set (curva causal discreta) que *es* un trozo
  reconstruido del horizonte, **order-only y a ciegas**.
- **Avance frente a Eichhorn–Gamito–Stokes** (arXiv:2605.06813 §V): ellos *sembraron y
  seleccionaron* la escalera del horizonte usando el embedding; lo nuestro debe ser order-only y
  ciego, sembrado desde el bracket order-only de v2.
- **Semáforo de la exploración (dev, no congelado):** factibilidad 🟢 (fuzzy ladders ≥8
  abundantes); dirección #2 🟡 (AUC 0.72–0.95, muestras minúsculas, banda cerca del horizonte sin
  testear); semillado-bracket #3 🟡 (concentra cerca del horizonte pero rinde poco, `d_⊥` mediana
  ≈3–4 ℓ frente al objetivo O(ℓ)); kernel iterativo ya en su sitio (el recursivo hacía SIGSEGV).

## Los cuatro puntos

### 1. La disciplina anti-fuga es lo primero — *empezamos aquí*
El único valor de PR-003 sobre EGS es **ser ciego**. El modo de fallo dominante es que la verdad
oculta (embedding) entre a **sembrar** o **seleccionar** la escalera, no solo a **puntuar**. El día
que eso pase, deja de ser reconstrucción ciega y queda una prueba de principio asistida — lo que
EGS ya hizo.
- **Entregable:** un *leakage gate* escrito — la lista de criterios que **toda** regla nueva
  (dirección, selección) debe pasar antes de medirse o congelarse. Cada regla declara
  explícitamente sus entradas y aporta la prueba de que el embedding **solo puntúa**, nunca define
  ni guía el observable ni el borde.
- **Hecho cuando:** existe el checklist y el observable + la semilla de PR-003 están descritos
  únicamente en términos del orden causal.

### 2. Congelar las dos reglas order-only **antes** de cualquier paso *committing*
Mientras no estén escritas y selladas, no hay reconstrucción ciega que valga.
- **Regla de dirección (#2):** saliente vs entrante, solo con orden (candidata: el campo de
  exterioridad `φ = L_fut`, diagnóstico interior/exterior de EGS).
- **Regla *fija* de selección de escalera (#3):** qué escalera se elige, determinista y order-only,
  sembrada desde el bracket boundary de v2.
- **Hecho cuando:** ambas reglas pasan el *leakage gate* del punto 1 y quedan congeladas en su
  documento sellado, con su SHA, antes de tocar datos *committing*.

### 3. Resolver el bloqueo experimental real
Hoy #2/#3 están medidos donde es fácil, no donde importa.
- Medir #2/#3 **en la banda cerca del horizonte** con muestra suficiente (la dirección AUC donde
  manda; el rendimiento real del semillado).
- Empujar `d_⊥` hacia **O(ℓ)** seleccionando la escalera saliente más larga sembrada desde el
  bracket.
- **Hecho cuando:** hay medidas estables y reproducibles en la banda cercana, suficientes para
  *justificar* (no ajustar a posteriori) la forma de las reglas del punto 2.

### 4. Redactar el plan PR-003 con criterios de éxito en forma **congelable**
- Criterios: `d_⊥ ≲ k·ℓ`, persistencia temporal, continuidad discreta, convergencia transversal
  con densidad, estabilidad en hold-out, **control plano** (sin curva persistente) y **controles
  desplazados** (variar M ⇒ la reconstrucción se mueve sola, sin reajustar nada), y salida
  geométrica (conjunto de elementos).
- **Hecho cuando:** el plan está escrito en forma sellable, con semillas dev/validación disjuntas y
  banda virgen reservada, listo para convocar al comité y, tras su visto bueno, congelar.

## Secuencia real de ejecución

El punto **1 gobierna todo**. El orden no es estrictamente 1→2→3→4: es **1 → 3** (medir donde
importa) **→ 2** (congelar las reglas con lo ya medido, nunca al revés) **→ 4** (sellar el plan).
**Nada *committing*** —ni quemar semillas vírgenes, ni sellar reglas— hasta tener 1, 3 y el plan 4
con el visto bueno del comité.

## Disciplina (cómo se vigila)

- **`/comite`** antes de sellar las reglas (#2) y el plan (#4): el falsador y el *pre-registration
  warden* existen justo para cazar la fuga del embedding y el «congelaste *después* de mirar».
- **`/auditor`** (`make audit`) antes de construir sobre cualquier número ya medido: todo número
  publicado debe ser salida literal de un script determinista commiteado; el sello no debe haber
  derivado.
- Toda exploración vive en `dev/` (scripts commiteados, datos crudos no); la confirmación vive en
  la ruta sellada. La separación es de **rutas de código y semillas**, no de git.

## Roadmap global

**localización del borde ✅ → construcción de un trozo de horizonte (PR-003) → convergencia bajo
extensión del parche → 3+1D.**
