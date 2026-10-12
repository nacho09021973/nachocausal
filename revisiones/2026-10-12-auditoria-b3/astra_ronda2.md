1. **Vinculación de la compuerta: `SE_SOSTIENE`.**

[SOURCE] B2.1 importa `verify_b2_path2_gate_certificate as gate`, toma `b15 = gate.b15` y crea alias locales de sus funciones de redondeo. Los tres núcleos nuevos son funciones del módulo B2.1; `GATE_UNUSED` selecciona exclusiones del control, sin sustituir funciones de `gate`. En los adjuntos, la única asignación explícita a un atributo de `gate` es `gate.VN_FR = ...`, realizada por B3.

[INFERENCE] No encuentro un parche, sustitución o reasignación adicional de funciones de la compuerta. Llamar a `gate._compile_helpers()` para compilar especializaciones no constituye, por sí mismo, una sustitución de funciones.

[SOURCE] Se declara un único commit del fichero de la compuerta, coincidente con el objeto auditado.

[UNVERIFIED] Esa declaración no es una comprobación independiente del fichero efectivamente importado; un registro de commits tampoco acredita por sí solo la ausencia de modificaciones locales.

**Condición de concesión:** [INFERENCE] aceptar la identidad declarada del módulo importado con la compuerta congelada y las garantías heredadas de sus auxiliares. Bajo esa condición, queda resuelta la duda sobre modificaciones introducidas por B2.1.

2. **Inspección del IR ejecutado: `REQUIERE_CORRECCIÓN`.**

[SOURCE] `executed_ir` rechaza los aciertos de caché, recorre todas las firmas registradas y exige una definición cuyo nombre concuerde con su expresión regular. Ambos controles impiden aprobar si algún núcleo seleccionado carece de firmas. Ambos incluyen un mutante con `fastmath=True`.

[INFERENCE] Estas comprobaciones eliminan varios pases en vacío: una lista vacía de firmas no permite aprobar los controles completos, y un módulo sin la definición buscada provoca una excepción.

[SOURCE] La prueba negativa declarada obtiene el rechazo de `k_below` cargado desde caché.

[INFERENCE] Esa prueba respalda la barrera de caché; no demuestra la exhaustividad de la inspección de los cuerpos paralelos. Persisten estos huecos:

- **B3 no exige cuerpos `prange`.** [SOURCE] `guard_all_gate_kernels` no comprueba `parfor_bodies` ni `parallel_ok`. [INFERENCE] Puede aprobar inspeccionando un módulo con la función principal, sin acreditar que haya incluido los cuerpos paralelos externos.
- **El recorrido tolera silenciosamente perder enlaces.** [SOURCE] Se utiliza `getattr(cur, "_linking_libraries", ())`. [INFERENCE] Si ese atributo no está disponible y el módulo principal conserva la definición exigida pero no los cuerpos externos, B3 puede aprobar. El mutante escalar no detecta esta pérdida. No afirmo que ocurra en la versión utilizada; afirmo que el control no la excluye.
- **B2.1 comprueba presencia, no exhaustividad.** [SOURCE] Basta encontrar algún cuerpo con nombre `__numba_parfor_gufunc_...` en el conjunto recorrido para cada núcleo paralelo. [INFERENCE] Si hay varios cuerpos y falta uno, encontrar otro puede satisfacer `parallel_ok`. Tampoco se establece esa cobertura por especialización.
- **La identidad de la definición es aproximada.** [SOURCE] La expresión regular usa el nombre Python, sin contrastarlo con el nombre LLVM exacto de cada especialización. [INFERENCE] Esto es más débil que acreditar la definición concreta asociada a cada resultado de compilación.

**Condición de concesión:** [INFERENCE] exigir y validar el mecanismo de enlaces de la versión utilizada, contrastar la definición exacta de cada especialización y acreditar la cobertura de todos sus cuerpos paralelos, también en B3. Una prueba negativa que retire u oculte un cuerpo enlazado debe impedir aprobar. Puede concederse igualmente mediante evidencia concreta que demuestre esa cobertura completa para el ejecutable congelado.

[INFERENCE] Son insuficiencias del control, no evidencia de que los cálculos hayan usado efectivamente código incorrecto.

3. **Serialización y producto exterior: `CORREGIDO`, bajo H4 heredada.**

[SOURCE] B3 serializa los extremos nuevos mediante `b15.iv_lo` y `b15.iv_hi`. Calcula el producto y la resta de `W23` en `mpmath.iv`, y decide positividad usando `W23.a`, junto con las positividades de los dos factores inferiores.

[INFERENCE] Esto corrige tanto la conversión final sin dirección explícita como el redondeo escalar del producto exterior. `W23` encierra la expresión conservadora usada para obtener una cota inferior; no necesita encerrar el valor completo del producto exterior verdadero.

**Condición de concesión:** [INFERENCE] conservar las garantías heredadas de redondeo exterior de `iv_lo`/`iv_hi` y H4. Sus cuerpos no aparecen aquí; no los doy por nuevamente auditados ni reabro B1.5.

Veredicto final B3: AUDIT_PASS_CONDITIONAL_IR_COMPLETENESS  
Control IR (también para B2.1): REQUIERE_CORRECCIÓN_DE_COBERTURA_COMPLETA