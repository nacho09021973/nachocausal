# Hoja de ruta — fin de semana 27-28 jun 2026 · PR-003 giro relacional/formal

> **Plan REVISABLE, no congelado.** No es pre-registración, no fija umbrales, no autoriza commits ni
> push por sí mismo. Todo cambio sigue en fase local/dev salvo autorización explícita. Mantener
> `RESPECT_SEAL_FREEZE`, `NO_RECONSTRUCTION_CLAIM`, `NO_GROUND_TRUTH_LEAKAGE`,
> `NO_POST_HOC_TUNING` y `NO_THRESHOLD_LOOSENING`.

## 0. Estado de partida

- `main` está actualizado desde GitHub a `5973df0` por fast-forward.
- `docs/preregistration_003.md` ya está congelado: PR-003 Fase #3 = **operational
  resolution floor** del estimador sellado, no minimax universal sobre todos los estimadores.
- Comité-006 dejó `REFINE_CANDIDATES_BEFORE_PROMOTION`: C1 es el eje primario a cerrar, C2 queda
  como validador/replanteo secundario; no se promueve nada sin definición cerrada e independiente.
- Comité-007 dejó L₁ en estado **OPEN–CONTINGENT**: BL-localization retira el bloqueo por
  estabilización, pero exige cerrar L₁a/L₁b y mantener el firewall de prereg-003.
- Cambios locales ya hechos este sábado:
  - `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md`: nueva §9 sobre horizontes relacionales
    pregeométricos, referencia dinámica `R`, test Minkowski y evento covariante.
  - `dev/X0_Qn_wellposedness_NOTES.md`: nueva §13 con flujo Lean-first para formalizar el núcleo de
    teoría de órdenes.
  - `dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md`: lenguaje corregido para que geodésicas/tubos
    sean benchmarks semiclasicos, no definiciones order-only.

## 1. Objetivo del fin de semana

Consolidar el giro conceptual sin tocar el instrumento sellado:

1. Definir el horizonte como propiedad relacional/pregeométrica de un poset finito más una referencia
   interna `R`, no como detector de una métrica preexistente.
2. Separar tres capas que no deben mezclarse:
   - núcleo algebraico/order-theoretic formalizable;
   - candidatos semiclásicos C1/C2 y su ley nula;
   - interpretación física y correspondencia Schwarzschild/GKP, todavía abierta.
3. Dejar una ruta concreta para Lean 4 antes de volver a simulaciones o preregistraciones.

## 2. Sábado 27 jun — trabajo local recomendado

### A. Cierre documental del giro relacional

- Revisar la nueva §9 en `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` contra comité-006:
  asegurar que `R` se presenta como referencia relacional dinámica y que `H[C;R]` no reclama evento
  horizon clásico en un causet finito.
- Añadir, si hace falta tras lectura, una nota corta que conecte §9 con la cautela existente:
  persistencia + asimetría + controles adversariales, no sólo frontera de `down(R)`.
- No convertir §9 en resultado. Etiqueta: `CONCEPTUAL_FORMULATION`, no `PROVED` salvo la
  trivialidad finita 9.2.1.

### B. BL-localization / L₁

- Mantener el grado `OPEN–CONTINGENT`.
- No usar TY 2026 para tocar `K_LOC`, `theta_loc`, `theta_stab`, `P_PERM_THRESHOLD` ni ningún
  umbral congelado.
- Próximo entregable analítico, si se trabaja en esto: formular explícitamente L₁b-(b), el puente
  "orden producto 1+1D ⇒ hipótesis exactas del LPP/Johansson aplican al observable causal".
- No ejecutar nuevo probe hasta que el objetivo sea una pregunta falsable con salida simétrica.

### C. Formalización Lean-first

- Preparar inventario de lemas pequeños antes de crear código Lean:
  1. ideal acotado + directed/lower-set ⇒ principal, con hipótesis exactas;
  2. ideal no principal en poset numerable localmente finito ⇒ cadena cofinal no acotada;
  3. functorialidad de `Idl` bajo mapas monótonos;
  4. preservación de ideal ends bajo embeddings, una vez fijada la noción de end.
- No formalizar todavía Schwarzschild, GKP, sprinklings ni fuzzy ladders.

## 3. Domingo 28 jun — decisión de bifurcación

Elegir una de estas tres ramas, no todas:

1. **Rama formal:** crear un microproyecto Lean separado o una nota `dev/LEAN_FORMALIZATION_NOTES.md`
   con definiciones Lean candidatas y dependencias mathlib. Sin prometer que compile aún.
2. **Rama C1:** cerrar en escritura la definición C1 según comité-006: flujo forward por ideales,
   clase de búsqueda cerrada, comparator cuantitativo, y Guard-v sobre la selección.
3. **Rama L₁:** escribir el puente LPP/KPZ faltante y decidir si L₁b sigue `OPEN–CONTINGENT` o se
   degrada por falta de hipótesis exactas.

Regla de foco: si una rama produce una definición cerrada, convocar comité/auditor antes de
probarla con datos. Si sólo produce una nota conceptual, dejarla en `dev/` y no promocionarla.

## 4. No hacer este fin de semana

- No commit/push automático.
- No tocar `nachocausal/thresholds.py` ni el camino sellado.
- No usar `RESERVED_002` ni lanzar `validate.run()`.
- No mezclar la nueva definición relacional con afirmaciones de reconstrucción.
- No entrenar modelos ni abrir una línea de autoformalización masiva antes del inventario de lemas.

## 5. Checklist antes de cerrar la sesión

1. `git status --short` debe mostrar sólo cambios documentales esperados.
2. Si se ejecuta cualquier script o prueba que pueda depender del entorno sellado: `make verify-seal`
   antes y después, esperando `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
3. Registrar explícitamente si queda una pregunta en estado `OPEN`, `OPEN–CONTINGENT` o `DEFERRED`.
4. No dejar una decisión conceptual escrita como si fuera un resultado empírico.
