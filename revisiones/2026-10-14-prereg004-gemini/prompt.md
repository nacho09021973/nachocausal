Encargo: revisión ciega independiente (O8) del borrador de pre-registro 004 y del paquete 2+1 candidato `nachocausal2p1` (gemini-4-argon, thinkingLevel=high), en el commit 5afb33d de la rama prereg004/step3-port. Objetivo: buscar, antes de congelar (C1), criterios que no puedan fallar, fugas de información hacia el estimador, incoherencias entre texto y código y resquicios en la corrida ciega única. Resultado esperado: informe con veredicto por tarea y una lista de defectos por gravedad. Una sola ronda; lo cierra el informe; no hay segunda ronda salvo decisión del usuario.
---
Eres un revisor adversarial de diseño experimental y de código científico. Te adjunto el borrador de un pre-registro (todavía no congelado) y el código que lo ejecutará. El proyecto prueba si el orden causal de un conjunto causal sembrado (sin coordenadas) basta para localizar el horizonte de Schwarzschild en un banco 2+1D ecuatorial. Un estimador ve solo el orden; después, un módulo aislado de puntuación compara su frontera con la verdad (`r`). Habrá una única corrida ciega sobre 20 semillas vírgenes, sin repetición.

No se adjunta el paquete 1+1 sellado del que se reutilizan algunas primitivas (`two_means_split`, la regla de abstención por `τ(n)`, la prueba de permutación con cambio de signo); trátalo como auditado y di cuándo una conclusión tuya depende de él.

Tareas, en este orden:

1. **Criterios que no pueden fallar.** Para cada criterio del veredicto (`i_significant_every_rho_ge_min`, `ii_localisation_primary`, `ii_convergence_slack`, `iii_stability_primary`, `iv_flat_escapes_primary`, `v_order_only`), ¿puede pasar de forma vacía o casi garantizada por construcción, o fallar de forma trivial? Si sí, da el mecanismo concreto (fichero y función) y la cláusula que lo evitaría.
2. **Fugas.** ¿Puede llegar al estimador, o a una decisión humana durante la corrida, alguna información de la verdad (`r`, la horquilla, las anchuras, la cobertura) antes de que el umbral quede fijado o antes del veredicto? Revisa en particular el registro de progreso por semilla (`progress_line`, `PROGRESS_FIELDS`) y la regla de caídas y relanzamiento.
3. **Texto frente a código.** ¿Coinciden los valores y reglas del borrador (§6-§10) con `thresholds.py` y `validate.py`? Enumera cada discrepancia.
4. **Diseño estadístico.** Evalúa: `p_perm` sobre las semillas válidas del generador con `sep = 0` para un agujero negro que se abstiene; la regla «≥ 3 abstenciones = FAIL de (i)» en cada ρ exigido; la cobertura sobre las horquillas válidas; la holgura de convergencia entre niveles de ρ que comparten las mismas 20 semillas; la mediana de anchuras sobre las horquillas «limpias». ¿Hay algún sesgo de selección o de dependencia que el texto no declare?
5. **Corrida única y reproducibilidad.** ¿Hay algún resquicio por el que la corrida ciega pueda repetirse, elegirse entre varias o depender del entorno (hilos, versiones, caché)? Ten en cuenta que no se ha comprobado el determinismo entre distintos números de hilos y que el número de hilos se fija en 20.
6. **Veredicto global:** «listo para congelar», «listo con cambios menores enumerados» o «no listo», con los defectos ordenados por gravedad.

Reglas: distingue lo que demuestras con el código adjunto de lo que conjeturas. Cita fichero y función. No cites literatura que no puedas identificar con precisión. Sé conciso: máximo 2000 palabras.
---
