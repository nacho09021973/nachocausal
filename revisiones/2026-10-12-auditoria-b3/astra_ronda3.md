[INFERENCE] La corrección cierra los cuatro huecos **para dependencias representadas por referencias simbólicas reconocidas por el control**. No demuestra por sí sola que todo cuerpo ejecutado pertenezca a ese grafo. Mantengo una concesión condicionada, sin afirmar que el ejecutable congelado haya omitido cuerpos.

1. **Clausura y cobertura**

[SOURCE] B3 utiliza ahora `guard_kernels`, que exige cuerpos paralelos para cada kernel marcado como paralelo. El recorrido accede directamente a `_linking_libraries`. `closure_check` exige los nombres exactos de `ov.fndesc.mangled_name` y busca referencias en todo el texto, no solamente en declaraciones.

[INFERENCE] Esto resuelve la ausencia del requisito paralelo en B3, el silencio ante un atributo inexistente y la identificación aproximada de las especializaciones. También corrige la pérdida de un cuerpo simbólicamente referenciado: encontrar otro cuerpo ya no basta para compensar su ausencia.

[INFERENCE] Sin embargo, **clausura de símbolos reconocidos no equivale necesariamente a clausura del código ejecutado**. Un contraejemplo al alcance general del control sería:

- Una especialización inspeccionada contiene su definición exacta y un cuerpo paralelo reconocido.
- Esa especialización llama además a una función compilada por Numba mediante un puntero obtenido de una dirección numérica o de datos suministrados externamente.
- El cuerpo correspondiente a ese puntero queda fuera del conjunto inspeccionado.

[INFERENCE] La llamada indirecta puede aparecer como `call ... %fp(...)`, sin ninguna referencia `@nombre` al destino. Si los símbolos restantes están definidos, no hay flags detectados y se cumplen las demás condiciones, el control puede aprobar aunque ese destino externo contenga aritmética prohibida. No hace falta ocultar una referencia simbólica: el destino nunca estuvo representado por ella.

[UNVERIFIED] Los adjuntos no demuestran que esto suceda en los kernels congelados. Tampoco contienen su IR completo para descartar ese caso. Es un contraejemplo a la garantía general del control, no un hallazgo de ejecución incorrecta.

[SOURCE] Además, `executed_ir` reúne los módulos de todas las firmas antes de comprobar la clausura; el recuento de cuerpos también se realiza sobre esa unión.

[INFERENCE] Por tanto, no hay una acreditación separada por especialización. La unión puede ocultar diferencias de cobertura si existen definiciones homónimas en bibliotecas distintas; la pertenencia de un nombre al conjunto no acredita qué definición resolvió el enlazador. No afirmo que tales colisiones existan aquí.

[INFERENCE] Para conceder la cobertura del ejecutable congelado basta aportar evidencia de que sus dependencias relevantes quedan representadas por los símbolos reconocidos, que cualquier destino indirecto está cubierto o pertenece a los auxiliares heredados, y que las definiciones inspeccionadas corresponden a las enlazadas. Comprobar cada sobrecarga separadamente fortalecería esa vinculación.

2. **Exclusiones y «cuerpo real»**

[SOURCE] `_numba_code_symbol` excluye expresamente `_ZN08NumbaEnv*`. Los nombres `.const*` quedan fuera porque no tienen ninguno de los prefijos admitidos. El recorrido de referencias sigue examinando todo el texto.

[INFERENCE] Las exclusiones son razonables bajo la convención declarada de que esos símbolos designan datos. Excluir el nombre de una constante no elimina una referencia `@funcion` que aparezca en su inicializador: esa referencia se examina igualmente. En cambio, una dirección codificada numéricamente conserva la limitación anterior.

[INFERENCE] El control clasifica por nombres, no por tipos LLVM. Por ello, la corrección de esa clasificación depende de las convenciones del compilador utilizado; no constituye una comprobación independiente de que todos los símbolos excluidos sean datos.

[SOURCE] El recuento paralelo exige una `define` cuyo nombre empiece por `_ZN`, contenga `__numba_parfor_gufunc_0x` y no empiece por `_ZN7cpython`.

[INFERENCE] Es una mejora concreta: cuenta definiciones, no declaraciones ni referencias a entornos. Bajo esas convenciones identifica cuerpos nativos paralelos. No demuestra, por sí solo, que cada cuerpo contado sea alcanzable desde la especialización examinada, ni que todos sus destinos estén cubiertos.

3. **Qué prueban las pruebas negativas**

[SOURCE] Las salidas aportadas declaran tres rechazos.

[INFERENCE] **(2)** acredita que eliminar las definiciones del cuerpo seleccionado, conservando referencias reconocibles, provoca un fallo de clausura. No prueba la pérdida de cualquier biblioteca ni cubre llamadas indirectas.

[INFERENCE] **(3)** acredita que se rechaza un nombre obligatorio inexistente. Añade un nombre ficticio; no elimina realmente la definición de una sobrecarga ejecutada. Es una prueba válida de esa condición, con alcance limitado.

[SOURCE] **(1)** informa de un acierto de caché. El subproceso no sustituye su entorno, mientras que importar B2.1 establece `NUMBA_CACHE_DIR`.

[INFERENCE] Acredita el rechazo por caché informado, pero la descripción «caché predeterminada» no concuerda con el entorno heredado.

[SOURCE] Los casos no detectados imprimen `NOT CAUGHT`; no fuerzan un fallo del script. Tampoco se comprueba el código de salida del subproceso.

[INFERENCE] Son evidencias diagnósticas aportadas, todavía no una batería que falle automáticamente ante esas regresiones. Mantengo las concesiones anteriores sobre vinculación y aritmética bajo sus condiciones heredadas.

Veredicto final B3: AUDIT_PASS_CONDITIONAL_IR_COMPLETENESS  
Control IR (también para B2.1): REQUIERE_CORRECCIÓN_O_EVIDENCIA_DE_COBERTURA_COMPLETA