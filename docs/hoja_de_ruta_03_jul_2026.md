# Hoja de ruta — 03 jul 2026 · PR-003 tras cierre del registro de maximalidad

> **Plan REVISABLE, no congelado.** No es pre-registración, no fija umbrales, no autoriza commits ni
> push por sí mismo. Todo cambio sigue en fase local/dev salvo autorización explícita. Mantener
> `RESPECT_SEAL_FREEZE`, `NO_RECONSTRUCTION_CLAIM`, `NO_GROUND_TRUTH_LEAKAGE`,
> `NO_POST_HOC_TUNING` y `NO_THRESHOLD_LOOSENING`. Sucesora de `docs/hoja_de_ruta_27_jun_2026.md`.

## 0. Punto de partida (verificado, 03-jul-2026) — leer esto primero al retomar

- **Sello intacto.** `nachocausal/thresholds.py` sha256 = `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
  (`make verify-seal`). Nada de lo hecho desde el 27-jun toca el camino sellado.
- **`main` en GitHub al día**, `HEAD=aaba9e9`, working tree limpio.
- **prereg-002 `PASS`**; **prereg-003 FROZEN** (Fase #3 = cota operacional O(ℓ) del estimador
  sellado, no minimax universal — `docs/preregistration_003.md`).
- **Horizonte relacional (comité-006 + corrección posterior):** Def 9.1.1 corregida a orientación
  infalling `A_R→B_R` (la versión `B_R→A_R` es demostrablemente vacía ∀R; commit `110e4af`).
  Selector de `R` sigue **OPEN**, con la restricción de cierre `B̂` como único filtro adoptado;
  ningún candidato `R-a` está aprobado todavía.
- **BL-localization / L₁ (comité-007):** grado **OPEN–CONTINGENT**. L₁b sigue solo esbozado
  (falta el puente LPP/Johansson explícito, L₁b-(b)); L₁a sigue abierto. Congelado desde el pivote
  del PI (26-jun): no se toca `K_LOC`, `theta_loc`, `theta_stab`, `P_PERM_THRESHOLD`.
- **C1 / clase admisible 𝔄 / regla de referencia Q (comités 010→014):** el hilo más profundo y el
  que quedó más recientemente autorizado por escrito. Estado:
  - `𝔄` (clase de completación admisible C1): solo 3 obligaciones cerradas — preservación literal
    del subposet (`MANDATORY`), orden causal válido (`MANDATORY`), convexidad (`MANDATORY_FOR_C1`).
    Compatibilidad Schwarzschild y manifoldlikeness siguen `DEFERRED`; número de elementos ocultos
    `DEFERRED`. Cláusulas (b)/(c)/(e) de la definición C1 siguen `UNRESOLVED`
    (`docs/comite/comite_decision_012...md`).
  - Pista **Q** (regla de referencia lateral candidata): **`Q_REFERENCE_PATH_REMAINS_BLOCKED`**
    (comité 014). Caso `|A|=1` es solo diagnóstico, no operacional; selección de marcador general
    sin criterio de admisibilidad escrito; `MODULAR_PRIMALITY` disponible pero no selecciona `A`.
  - Único siguiente paso ya autorizado en ese hilo (comité 014, aún no ejecutado):
    `Q_A6_AGGREGATION_SPECIFICATION_ONLY` — **especificación escrita únicamente**, sin código, sin
    Alloy, sin Lean, sin simulaciones.
  - Alloy 002 permanece `INVALID_UNDER_CONVEXITY_REQUIREMENT` como testigo de interfaz;
    `boundary-bracket`/S3 permanece `FAILED_BASELINE...` (uso permitido: solo comparador
    diagnóstico). Ningún Alloy 003 ni Lean nuevo están autorizados hasta cerrar (b)/(c)/(e).
- **Registro de maximalidad — CERRADO esta sesión (03-jul):**
  `dev/PR003_INFINITE_MAXIMALITY_NONCERTIFIABILITY.md` (commit `aaba9e9`, pusheado) prueba, para
  todo `O` finito con `dim_DM(O)≤2`, `|O|≥2`, y todo `e∈Max(O)`, un par de completaciones (una
  infinita general + su truncación finita, Corolario 1) que voltean la maximalidad de `e`
  respetando convexidad/stem/dimensión — a diferencia del testigo Alloy 001 (no convexo, escala 4,
  puntual). `/comite` adjudicó `RETAIN_BOTH_WITH_NEW_STRONGER_COROLLARY`: Alloy 001 se conserva sin
  cambios (sigue siendo un testigo acotado verificado por herramienta, válido para su propia
  afirmación codificada); el Corolario 1 coexiste como resultado general. Esto cierra, con prueba
  general en vez de un contraejemplo puntual, la pregunta de si la maximalidad observada factoriza
  a través del stem finito — **respuesta: no**, para esta clase (Corolario 2).
  - Pendiente explícitamente diferido por ese mismo comité (no autorizado todavía): codificar
    `(Q_A^{(1)}, Q_B^{(1)})` como modelo Alloy comprometido para paridad de procedencia. Esto
    contaría como un nuevo modelo Alloy sobre el hilo de maximalidad — **antes de hacerlo, volver a
    comité**, porque comité 013/014 prohíben expresamente "Alloy 003 antes de que (c) esté
    `CLOSED`" en el hilo C1/Q, y conviene una decisión explícita sobre si esa prohibición aplica
    también al registro de maximalidad (un registro distinto) o si hace falta una autorización
    separada.

## 1. Los tres hilos vivos, sin mezclar

1. **C1 / Q-reference-rule** (comités 010-014): el hilo más avanzado en definición pero bloqueado
   en cierre; el siguiente paso ya está escrito por el propio comité 014.
2. **Horizonte relacional / selector `R`** (comité 006 + corrección 110e4af): el hilo que motivó el
   pivote estratégico del PI (26-jun) hacia una definición intrínseca; sigue sin un candidato
   `R-a` aprobado.
3. **BL-localization / L₁** (comité 007): congelado por decisión del PI; solo avanza si alguien
   escribe el puente L₁b-(b) explícito.

Regla de foco (la misma que ya rigió el 27-28 jun): elegir **uno** para la próxima sesión de
trabajo real, no repartir el esfuerzo entre los tres.

## 2. Recomendación para la próxima sesión

**Recomendación primaria: retomar el hilo C1/Q con `Q_A6_AGGREGATION_SPECIFICATION_ONLY`.**

Razones:
- Es la única acción ya autorizada por escrito por el comité vigente de ese hilo (014) — no
  requiere convocar nada nuevo para empezar a redactar.
- Es puramente de especificación (sin código, sin Alloy, sin Lean, sin datos) — riesgo cero sobre
  el camino sellado y sobre el freeze.
- Es la pieza que, si se cierra, desbloquea simultáneamente dos cosas: (a) la cláusula (c) de la
  clase C1 (regla de referencia no trivial), que es la que traba tanto el registro de interfaz
  (Alloy 002 / C1) como cualquier futuro Alloy 003; y (b) permite decidir si la pista Q se abandona
  formalmente (comité 014 ya dejó escritos los 4 criterios de abandono — conviene revisarlos
  explícitamente contra lo que salga de esta especificación, en vez de dejarlos indefinidos).
- Alcance acotado y ya escrito por el propio comité: (i) criterio de admisibilidad order-only para
  `𝔄(C)` basado en A5 excluyendo `O(i)`; (ii) formalización completa de A6.4 como única forma de
  agregación autorizada; (iii) evaluación conceptual de si `QG3` es formalizable.

**Alternativa igualmente legítima: cerrar el candidato `R-a` del selector relacional.**

Si el PI prefiere seguir el pivote estratégico del 26-jun (definición intrínseca del horizonte
antes que la maquinaria C1/Q), el siguiente paso natural es proponer un candidato concreto de `R`
que satisfaga la restricción de cierre `B̂` ya adoptada, y llevarlo a `/comite` para adjudicación —
igual que se hizo con la orientación de Def 9.1.1. Este hilo tiene más contenido físico pendiente
(qué cuenta como referencia relacional dinámica) que el hilo C1/Q, que es ahora mismo puramente
combinatorio/order-theoretic.

**Tercera opción, de bajo riesgo y en paralelo (no compite por foco):** el inventario de lemas
Lean-first de `docs/hoja_de_ruta_27_jun_2026.md` §2.C (ideal acotado ⇒ principal; ideal no
principal ⇒ cadena cofinal no acotada; funtorialidad de `Idl`; preservación de ideal ends bajo
embeddings) sigue sin escribirse. Es núcleo algebraico puro, no depende de qué hilo físico se elija,
y no compite con la regla de foco porque no es "trabajo de proyecto" sino infraestructura formal
reutilizable por cualquiera de los tres hilos.

**No recomendado ahora mismo:** tocar L₁/BL-localization. Sigue congelado por decisión explícita
del PI (26-jun) y nada ha cambiado esa decisión.

## 3. No hacer en la próxima sesión

- No commit/push automático de nada que no sea explícitamente autorizado.
- No tocar `nachocausal/thresholds.py` ni el camino sellado; no usar `RESERVED_002`.
- No crear un Alloy 003 ni tocar Lean bajo el hilo C1/Q — sigue `NOT_AUTHORIZED` hasta que (b)/(c)/(e)
  cierren.
- No codificar `(Q_A^{(1)}, Q_B^{(1)})` en Alloy sin pasar antes por `/comite` (ver nota de §0).
- No reclasificar `boundary-bracket`/S3 ni Alloy 002 ni Alloy 001 — ambos permanecen exactamente
  como están (`FAILED_BASELINE...` y `ALLOY_COUNTEREXAMPLE_FOUND` respectivamente).
- No mezclar los tres hilos en una sola sesión ni en un solo documento.
- No convertir ninguna nota conceptual en resultado sin pasar por `/comite`.

## 4. Checklist antes de cerrar la sesión

1. `git status --short` debe mostrar solo cambios documentales esperados.
2. Si se ejecuta cualquier script que dependa del entorno sellado: `make verify-seal` antes y
   después, esperando `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
3. Registrar explícitamente el estado (`OPEN`, `OPEN–CONTINGENT`, `DEFERRED`, `BLOCKED`) de
   cualquier pregunta tocada.
4. Si el hilo elegido produce una definición cerrada, convocar `/comite` antes de buscar testigos o
   tocar datos. Si solo produce una nota conceptual, dejarla en `dev/` sin promocionarla.
