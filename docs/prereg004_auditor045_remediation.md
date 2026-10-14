# Prereg-004 — correcciones del informe 045

Fecha: 2026-10-14. Base: `3cc152a` en `prereg004/step3-port`.
Autorización del PI: «adelante», tras la propuesta de corregir E1/E2 y W1/W2,
publicar y repetir la auditoría del delta en otra sesión. Este registro no es una auditoría.

## Cambios

- **E1, C1/C2:** `thresholds.py` conserva la receta y el estado, sin campos mutables de semillas.
  C1 congela ese instrumento. C2 añade solo `docs/validation_004_seeds.json`, producido por
  `nachocausal2p1/seed_manifest.py`, con `freeze_commit`, `draw_seed` y `seeds`.
  El lector exige el manifiesto comprometido en HEAD, árbol limpio, el commit único que
  introduce el documento congelado, diff nulo de los archivos sellados frente a C1 y
  coincidencia exacta de banda, cardinalidad y receta. C3 usa el commit C2 publicado como HEAD.
  El productor rechaza candidato no congelado, deriva del instrumento, árbol sucio y sobrescritura.
- **E2, INCONCLUSIVE:** `summarise_level` conserva los agregados descriptivos antes de fijar
  el estado. Una muestra vacía informa contadores cero y estadísticas NaN. La regla de
  menos de 18 válidas en cualquier nivel sigue dando INCONCLUSIVE.
- **W1:** el borrador y los comentarios atribuyen reproducibilidad al SHA, sin prometer
  impredecibilidad frente al autor de C1. No se cambia la receta del sorteo.
- **W2:** el ejemplo de cobertura tolera 10/20 no cubiertas con suelo 0.5.
- Se actualiza el borrador y se añade al comité 052 una nota posterior del PI, sin reescribir
  las deliberaciones ni firmar un nuevo veredicto. El informe histórico 045 queda intacto.

## Verificación realizada

Comando en el entorno sellado:

```sh
/home/ignac/nachocausal/.venv/bin/python -m pytest -q tests/test_004_seed_manifest.py tests/test_2p1_package.py tests/test_004_criteria_can_fail.py
```

Resultado: **61 passed in 13.10s**, exit 0. Los tests de manifiesto sustituyen el RNG/sorteo
por identificadores sintéticos. La prueba de integración crea un repo Git temporal con un
documento e instrumento sintéticos; no congela nada en nachocausal ni ejecuta realizaciones.
Las pruebas del nivel corto y del nivel vacío comprueban los agregados además del estado.

`make verify-seal verify-2p1 PY=/home/ignac/nachocausal/.venv/bin/python`, exit 0:

```text
thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4
nachocausal2p1/thresholds.py 2bf954fb1164f94b42b2e34512aac1d10d5e76e77915b15c14a640bf7186908e
nachocausal2p1/fixtures/tau_table_2p1.json 4bc4aec839257af7fed210030c0afa9041c265cacf43802bb735fb99df367a28
```

El verificador de estructura del comité 052 devuelve `BRIEF_CHECK=PASS`, exit 0.
`git diff --check` pasa. No se vuelve a ejecutar la suite global; el total histórico de
564 aprobados y 2 omitidos del informe 045 no se presenta como el total de este candidato.

## Estado y siguiente cierre

`STATUS` sigue siendo `CANDIDATE_NOT_FROZEN`. No existen el documento no-draft de prereg-004
ni el manifiesto real de C2. No se sortearon semillas reales ni se generó una realización virgen.
D11 permanece documental; no se implementa un manejador automático de abortos.

Siguiente paso: en otra sesión, aplicar `/auditor` al delta desde `3cc152a`, incluyendo
el nuevo productor/lector, los tests y los textos. Solo tras su veredicto favorable corresponde
el paso 7 de `/comite` en Claude Code y la decisión del PI. No se autoriza ni ejecuta C1-C3 aquí.
