# Nota de autorización acotada — remediación `NC-0` y preflight `NC-1`

```text
ESTADO: FIRMADA — REMEDIACIÓN NC-0 Y PREFLIGHT NC-1 AUTORIZADOS
FECHA: 2026-08-17
AMPLIA: docs/program_reopening_note_2026-08-16_normalised_channel.md
NO_REVOCA: docs/program_closure_note_2026-07-30.md
NO_REABRE: EF-0--EF-8, EF-4/C1 ni reconstrucción de horizonte
SELLO: intacto — no se toca
SEMILLAS: ninguna
DATOS_NUEVOS: ninguno
```

## 1. Autorización del PI

El PI ordena y firma, con fecha 17 de agosto de 2026:

> «Subsana esta incidencia, cierra la reauditoría. Además firmo y autorizo un
> preflight separado para estas condiciones asintóticas.»

La autorización se interpreta de forma estrecha conforme a las reglas del
repositorio. No autoriza simulaciones, datos nuevos, cambios del selector, ataques
de fuerza bruta ni una demostración asintótica completa.

## 2. Bloque A — remediación y cierre de `NC-0`

Se autoriza exactamente:

1. corregir las cuatro expresiones localizadas por la ronda 4 en las tres
   superficies siguientes:
   - `emergencia/HOJA_DE_RUTA.md` §19.1(4) y su flag de §19.4;
   - `emergencia/P1a_puerta_teorica_en_Minkowski.md` §13.9;
   - `docs/comite/comite_decision_050_p1a-seccion-13-certificado-familia-prescrita.md`
     §11;
2. sustituir la atribución incorrecta de evidencia de `T_emp` hasta `n=16000` por
   el soporte real `n in {64,96,128}`; las apariciones de `n=16000` que describen
   el falsificador de la familia prescrita permanecen intactas;
3. reejecutar solo el verificador determinista ya existente y los sidecars de los
   artefactos sellados;
4. registrar una ronda 5 de reauditoría y cerrar `NC-0` con uno de sus terminales
   precomprometidos en el fichero científico auditado, la nota de reapertura de
   2026-08-16 y los dos libros mayores
   `emergencia/HOJA_DE_RUTA.md` y `docs/hoja_de_ruta_agosto_2026.md`.

No se autoriza modificar los CSV/JSON sellados, sus sidecars, el script auditado,
los manuscritos ni `thresholds.py`.

## 3. Bloque B — preflight separado `NC-1`

Se autoriza crear un único documento científico nuevo:

```text
emergencia/P1a_count_volume_preflight_asintotico_d2.md
```

Su cometido cerrado es:

1. escribir la desigualdad poblacional que se obtiene de la cota geométrica Beta
   `b_n(m)` ya demostrada;
2. formular condiciones suficientes de existencia eventual, masa/concentración
   de `M` y escala de `Var(ell|n,h,S)` para implicar
   `liminf T_n^h>0`;
3. probar solo la implicación condicional;
4. identificar qué consecuencias agregadas de la selección bastarían sin resolver
   toda `w`;
5. separar los valores finitos ya existentes de cualquier afirmación asintótica;
6. emitir exactamente un terminal de §4.

El preflight no puede afirmar que sus hipótesis se cumplen en el modelo. Tampoco
puede abrir por sí mismo el ataque posterior.

## 4. Terminales de `NC-1`

```text
NC1_READY_FOR_ANALYTIC_ATTACK
  La cota Beta produce una implicación suficiente correcta, las obligaciones
  asintóticas quedan separadas y tienen ancla finita refutable. No demuestra las
  obligaciones ni el liminf.

NC1_BLOCKED_BY_INVALID_LOWER_BOUND
  La desigualdad Beta no soporta el paso poblacional requerido.

NC1_BLOCKED_BY_VACUOUS_CONDITION
  Solo se obtiene una reformulación circular o una condición no refutable.

NC1_ALREADY_DECIDED_IN_EXISTING_RECORD
  El repositorio ya contiene una prueba o refutación asintótica aplicable.
```

`NC1_READY_FOR_ANALYTIC_ATTACK` es un terminal de preparación, no un resultado
científico sobre el límite. Cualquier ataque a las obligaciones aisladas exige una
nueva autorización firmada.

## 5. Prohibiciones

- ninguna simulación, semilla, tabla o artefacto nuevo;
- ningún cambio de `M`, `S`, `MIN_COVERAGE_LEX` ni del gate `0.80`;
- ninguna modificación de resultados sellados;
- ninguna inferencia desde los tres tamaños hacia una cola asintótica;
- ninguna afirmación sobre canales enriquecidos, poset completo, horizonte o
  `d>=3`;
- ninguna afirmación de novedad o prioridad;
- ningún commit ni push sin orden posterior del PI.

## 6. Firma

```text
FIRMADO_POR: Ignacio Martín (PI)
FECHA_FIRMA: 2026-08-17
DECISION_NC0_REMEDIATION: AUTORIZADA
DECISION_NC1_PREFLIGHT: AUTORIZADO
AUTHORISED_SCOPE: listas cerradas de §2 y §3
ANALYTIC_ATTACK_AFTER_PREFLIGHT: NO_AUTORIZADO
```
