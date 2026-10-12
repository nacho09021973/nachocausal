# El control de fast-math de la compuerta pasa en vacío con la caché de numba

**Fecha:** 2026-10-12 · **Encontrado:** al construir el certificado por cajas de B2.1 ·
**Script:** `dev/explore_gate_fastmath_fresh_ir.py`

## Qué pasa

Los kernels de `verify_b2_path2_gate_certificate.py` se declaran con `@njit(cache=True)`. Si en
una ejecución se cargan desde la caché en disco, `inspect_llvm` devuelve un módulo **vacío**,
de unos 200 caracteres y sin ninguna `define`. Numba avisa con «Inspection disabled for cached
code. Invalid result is returned». El control `fastmath_guard` no encuentra flags en ese módulo
vacío y da `ok = True`. La prueba por mutación no lo detecta, porque el mutante se compila sin
caché.

**Consecuencia.** El control solo es real en una ejecución que compile desde cero. Cualquier
`fastmath_guard.ok = True` de una reejecución con la caché caliente es vacío. En concreto:
- la reejecución bit a bit de la compuerta del 2026-10-12 (`a671493`);
- con toda probabilidad, la condición (v) del sanedrín del 2026-10-11, «reejecutado a `M=128`
  … `fastmath_guard.ok = True`», hecha después de la ejecución original.

La ejecución original que congeló el JSON (`7909c0e`) pudo compilar desde cero, pero no queda
constancia.

## Comprobación

`dev/explore_gate_fastmath_fresh_ir.py` ejecuta la compuerta con `M=16`, para que los 19
kernels tengan firma. Después recompila cada uno **sin caché**, con las mismas opciones y
firmas, e inspecciona ese IR:

```text
cached_ir_chars : 193 – 214      (módulos vacíos)
fresh_ir_chars  : 4 556 – 255 547
flags           : ninguno en los 19
ALL 19 GATE KERNELS CLEAN ON FRESH IR: True
```

**El certificado de la compuerta no cambia.** Ninguno de sus kernels contiene
`fast`/`contract`/`reassoc`/`fma`. Lo que cambia es la **evidencia**: hasta hoy, en las
reejecuciones, esa garantía descansaba en un control que no podía fallar.

## Corrección

El verificador de cajas de B2.1 (`research_program/puente_3p1/2026-10-12/verify_b2_1_box_certificate.py`)
usa `fresh_ir`. Esta función recompila sin caché e **intenta fallar** si el IR no contiene la
definición de la función. Además, el mutante se detecta también por esa misma vía. El verificador
de la compuerta está congelado y no se edita. Su control se sustituye por esta comprobación, que
se puede repetir con el script de arriba.
