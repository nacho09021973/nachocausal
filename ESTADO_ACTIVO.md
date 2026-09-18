# Mapa activo del repositorio

Este archivo es un mapa operativo de rutas. No sustituye a `README.md`,
`CLAUDE.md`, `INSTRUCCIONES.md` ni a los contratos y estados científicos de
`docs/`.

## Núcleo activo

- `nachocausal/`: paquete principal y observables sellados.
- `tests/`: pruebas del paquete.
- `dev/`: exploración y desarrollo reversible.
- `docs/`: contratos, preregistros, auditorías, decisiones y estados.
- `research_program/`: programa de investigación, síntesis y work packages.
- `formal/`: formalizaciones reproducibles; `formal/HorizonFormal/.lake/` es
  caché local regenerable y no debe versionarse.
- `scripts/`: utilidades operativas.
- `certifier/`: código de certificación.
- `provenance/`: registros de procedencia.

## Evidencia y entregables

- `data/`: datos y tablas versionados.
- `evidence/`: evidencia archivada y diagnósticos.
- `emergencia/`: línea de investigación separada con sus resultados y
  verificadores; no mezclar automáticamente con el paquete principal.
- `manuscrito/`: fuentes y entregables editoriales.
- `web/` y `viz/`: sitio y figuras reproducibles.

## Solo local o regenerable

- `biblioteca/`: biblioteca bibliográfica local, ignorada por Git.
- `results/`, `dev_ensemble_raw/`, `email/` y salidas de compilación: no son
  rutas canónicas por defecto.
- Cachés como `__pycache__/`, `.pytest_cache/` y `.lake/` pueden eliminarse y
  regenerarse cuando sea necesario.

## Histórico

`old/` conserva material auxiliar o sustituido para trazabilidad. Sus archivos
no son contratos, resultados vigentes ni fuentes de claims sin revalidación.

## Regla de mantenimiento

Antes de crear una nueva carpeta en la raíz, comprobar si el contenido encaja
en una de estas rutas. Antes de archivar algo, buscar sus referencias y
preservar los enlaces mediante `git mv`.
