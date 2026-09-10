# Paper III — Resolución 005: incertidumbre y modelo de error

```text
RESOLUTION_ID=PAPER_III_R005
STATUS=APPROVED
DATE=2026-09-10
SIGNED_BY=PI
RESOLVES=G0-3
SCOPE=REPORTING_RULE
NUMBERS_MOVED=NONE
NEW_STATISTICS=NONE
```

Firma el bloque `APPROVED TEXT — R5` de
[Resoluciones pendientes](paper_iii_resoluciones_pendientes.md), sin
modificarlo.

## 1. Texto aprobado, literal

> Toda pendiente, cociente o exponente reportado en Paper III va acompañado de su
> dispersión entre semillas y del número de réplicas que la produce. Toda
> desviación respecto de un valor esperado se compara explícitamente contra el
> suelo de resolución del propio diseño, estimado en el mismo diseño mediante una
> magnitud cuyo valor sea exactamente conocido.
> Además, mientras \(L\) sea un entero de dispersión del orden de la unidad, la
> desviación típica **no se estima punto a punto** sino de forma agrupada sobre
> el barrido, y el número de réplicas debe declararse suficiente para que esa
> estimación sea estable. Un contraste cuyo resultado dependa de la `sem` de un
> único punto no es admisible como evidencia.

## 2. Aplicación

Regla de reporte. No se ha ejecutado nada, no se ha introducido ninguna
estadística nueva y ninguna cifra se ha movido.

`dev/PAPER3_3P1_SCALE_NOTES.md` §3.2 reportaba seis pendientes sin dispersión.
Ahora cada una lleva su dispersión entre semillas y su número de réplicas. Las
dispersiones **no son nuevas**: son las ya reconstruidas y auditadas en
[el contrato §4.2](paper_iii_fase0_contrato.md), a partir de las filas por
semilla del propio artefacto histórico.

El suelo de resolución del diseño es el que devuelve la magnitud de valor
**exactamente conocido**: `d log⟨V⟩_all / d log rho` vale 1 por construcción y el
diseño lo devuelve como `1.0179`. Ésa es la referencia del diseño, y **no** una
incertidumbre teórica universal.

La regla del modelo de error agrupado se registra junto a las cifras que la
motivan: con `L` entero y ocho réplicas, en `N = 8000` seis de los ocho valores
coinciden y la `sd` sale la mitad que en los otros tres puntos, lo que por sí
solo genera un χ²/dof de 3.26 que baja a 1.64 con `sd` agrupada
([R002 §3.1](paper_iii_resolucion_002_reescopado_fase1.md)).

## 3. Cierre

`G0-3` cierra por evidencia documental, comprobada en
`dev/verify_3p1_phase0_contract.py`: cada una de las seis pendientes de §3.2 debe
aparecer acompañada de su dispersión, y la nota debe declarar la regla de `sd`
agrupada y el suelo del diseño.

```text
G0-3 = CLOSED
```
