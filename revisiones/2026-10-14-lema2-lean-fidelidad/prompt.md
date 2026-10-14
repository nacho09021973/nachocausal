Encargo: revisión ciega de la fidelidad de los enunciados de `formal/NachoFormal/Monotonicity.lean` (lema 2 de B2, PR #12) frente al §2.2 del certificado de B2 (astra, gpt-6-astra, esfuerzo high). Objetivo: decidir si lo que el fichero Lean demuestra es lo que el certificado usa, antes de fusionar el PR. Resultado esperado: informe con veredicto por tarea y un veredicto global. Una sola ronda; lo cierra el informe; no hay segunda ronda salvo decisión del usuario.
---
Eres un revisor matemático adversarial con experiencia en Lean 4 y Mathlib. No puedes compilar nada: la compilación ya se hizo (`lake build` sin errores, sin `sorry`, y `#print axioms` de cada teorema muestra solo `propext`, `Classical.choice` y `Quot.sound`). No te pido que revises las demostraciones, sino los **enunciados**: si lo que el fichero demuestra es lo que el certificado necesita.

Te adjunto tres documentos:
1. un extracto literal del certificado de una cota numérica (§2 pasos 1-2, una fila de su §3 y su hipótesis H1). El paso 2 es la afirmación que se quiere formalizar;
2. el encargo con el que se escribió el fichero Lean, que fija su alcance y lo que deja fuera;
3. el fichero Lean, `Monotonicity.lean`.

Tareas, en este orden:

1. **Definiciones.** ¿`IsCausalCurve`, `L`, `lengths` y `tau` capturan la separación temporal `τ` de la métrica `q(UV)² dU dV` tal como la usan el paso 2 y H1? Revisa en particular la orientación temporal (orden producto en `ℝ × ℝ`), el integrando, el uso de `deriv`, la clase de regularidad (monótona y Lipschitz por componentes, con constante común) y el convenio de Lean `sSup ∅ = 0` y `sSup` de un conjunto no acotado `= 0`. Para cada una: "fiel", "fiel con salvedad" o "no fiel", con una línea de justificación.
2. **Teoremas.** Para `tau_mono_left`, `tau_mono_right`, `capped_mono`, `capped_tau_mono_left` y `capped_tau_mono_right`: ¿basta su enunciado, con las hipótesis que lleva, para obtener las dos desigualdades del paso 2, `τ(P_top, Q_bot) <= τ(x,y)` y `τ(x,y) <= τ(P_bot, Q_top)`, y su paso a `min(pi, ·)` y a `p`? Escribe la composición explícita e indica qué hipótesis (no vacío, `BddAbove`, `0 <= τ`, relación causal entre `x` e `y`) quedan por descargar en cada uso y si el certificado las asegura.
3. **Huecos.** ¿Hay algún caso que el certificado usa y que los enunciados no cubren (por ejemplo `x` e `y` sin relación causal, extremos con `ΔU = 0` o `ΔV = 0`, el dominio `UV < 1` frente a `q` definida en todo `ℝ`)? ¿Hay alguna hipótesis que haga un teorema vacío o trivialmente cierto? Si la hay, da el contraejemplo mínimo o la construcción.
4. **Alcance.** El encargo deja fuera la equivalencia con la clase de gráficas `U(V)` de H1 (lema 3) y la cota de Cauchy–Schwarz. ¿Hay algo más que el certificado atribuya al paso 2 y que no esté ni en el fichero ni en lo que se declara fuera?
5. **Veredicto global:** "fiel", "fiel con salvedades enumeradas" o "no fiel". Lista las salvedades por orden de gravedad.

Reglas: distingue lo que demuestras de lo que conjeturas. Cita el nombre de la declaración Lean o la línea del extracto en que te apoyas. No cites literatura que no puedas identificar con precisión. Sé conciso: máximo 1500 palabras.
---
