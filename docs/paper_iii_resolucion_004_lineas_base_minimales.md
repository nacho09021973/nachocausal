# Paper III — Resolución 004: líneas base del canal de minimales

```text
RESOLUTION_ID=PAPER_III_R004
STATUS=APPROVED
DATE=2026-09-10
SIGNED_BY=PI
RESOLVES=G0-4
SCOPE=ANNOTATION_AND_SUSPENSION
NUMBERS_MOVED=NONE
GENERATOR_EXECUTED=NO
```

Firma el bloque `APPROVED TEXT — R4` de
[Resoluciones pendientes](paper_iii_resoluciones_pendientes.md), sin
modificarlo.

## 1. Texto aprobado, literal

> Las magnitudes restringidas al conjunto de elementos minimales no tienen como
> línea base los exponentes 1 y 1/4. \(\mathrm{Min}(C)\) es una selección
> dependiente de \(\rho\), de modo que la esperanza condicionada a ser minimal no
> es lineal en \(\rho\). Las anotaciones «expect 1» y «expect 1/4» quedan
> retiradas de esas filas. Hasta que el canal de minimales disponga de una línea
> base derivada y verificada propia, **sus pendientes no pueden citarse como
> evidencia de desviación respecto de la ley asintótica**, ni compararse con el
> canal no restringido bajo la misma parametrización. Esta prohibición es la
> condición C3 de R002.

## 2. Aplicación

Tres etiquetas de impresión en `dev/explore_3p1_scale_calibration.py` y la
declaración de suspensión en la nota. **Ninguna cifra se mueve y el generador no
se ha ejecutado**: las etiquetas no aparecen en el JSON, de modo que ningún
artefacto cambia.

La evidencia que motiva la retirada ya está auditada y no se recalcula aquí:
`⟨V⟩_min/ρ` deriva `+18.2 %` sobre el barrido mientras `⟨V⟩_all/ρ` se mantiene
plano en el mismo diseño.

## 3. Procedencia — el punto delicado

Editar el generador cambia su hash, y ese generador es el **productor de
registro** del artefacto R001. La corrección editorial **no** reescribe esa
procedencia:

```text
productor de registro del artefacto R001   b5ca8c99…26fb2bb   commit 3230986   INMUTABLE
estado editorial vivo tras R004            1f4ff927…0c29d467                    declarado
```

El artefacto `dev/explore_3p1_scale_calibration_r001_results.json` lo produjo el
fichero de `3230986`, y así se sigue registrando. Lo que el verificador exige del
fichero vivo es otra cosa: que sea exactamente el estado editorial declarado, que
conserve la semántica `[3,2,1]` de R001 y que el diseño científico —barrido de
`rho`, semillas, aristas de la caja— siga intacto. Nunca se sustituye el hash
productor por el posterior.

## 4. Cierre

`G0-4` cierra por evidencia, comprobada en
`dev/verify_3p1_phase0_contract.py`: ninguna de las tres líneas de pendiente
restringida a minimales puede seguir declarando una línea base, y la nota debe
registrar la suspensión del canal.

```text
G0-4 = CLOSED
```

El canal de minimales queda **suspendido como evidencia de escala**, no
reabierto. Esa suspensión es permanente hasta que disponga de línea base propia
derivada y verificada.
