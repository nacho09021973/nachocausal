# Paper III — Resolución 006: atribución editorial

```text
RESOLUTION_ID=PAPER_III_R006
STATUS=APPROVED
DATE=2026-09-10
SIGNED_BY=PI
RESOLVES=G0-8
SCOPE=DOCSTRING_ONLY
NUMBERS_MOVED=NONE
GENERATOR_EXECUTED=NO
```

Firma el bloque `APPROVED TEXT — R6` de
[Resoluciones pendientes](paper_iii_resoluciones_pendientes.md), sin
modificarlo.

## 1. Texto aprobado, literal

> Todo material 3+1D del repositorio se atribuye a Paper III. Las cabeceras de
> `dev/explore_3p1_bg_reference.py` y `dev/explore_3p1_scale_calibration.py` se
> corrigen de «Paper II» a «Paper III». La corrección se aplica en el paso de
> conversión del orden obligatorio de R001 §5, nunca antes de la corrida de
> reproducción, para que la tabla de entradas siga siendo verificable.

## 2. Aplicación

Dos líneas de docstring. La condición temporal se cumple con holgura: la corrida
de reproducción del paso 1 está cerrada desde `ce30566`, de modo que la tabla de
entradas ya es verificable y la corrección llega después, no antes.

## 3. Procedencia — hashes que cambian y hashes que no

```text
                                    productor de registro        estado editorial vivo
explore_3p1_bg_reference.py         f9a181e2…14b93  (0338307)    3b91aa5d…131512a
explore_3p1_scale_calibration.py    a1b67a37…561a7b (0338307)    74d7d3d8…495addd58
                                    b5ca8c99…6fb2bb (3230986)
```

Los tres artefactos históricos y el artefacto R001 **no se han tocado** y
conservan su hash: nadie ha ejecutado nada. Los productores de registro
—quién produjo cada artefacto— siguen siendo los de la izquierda y **no se
reescriben** con los hashes posteriores a esta corrección editorial. El
contrato §5.1 distingue ahora explícitamente ambas columnas.

## 4. Una trampa que esta resolución obliga a arreglar

La comprobación previa de `G0-8` era `"Paper II" in head`. Como `"Paper II"` es
subcadena de `"Paper III"`, esa comprobación **habría seguido dando positivo
después de la corrección** y el bloqueo no habría cerrado nunca. El verificador
usa ahora `re.search(r"Paper II(?!I)", head)`.

## 5. Cierre

```text
G0-8 = CLOSED
```
