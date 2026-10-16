# Relevo del frente 3+1D, 2026-10-16 (para continuar desde otro ordenador)

## Estado

- **Hecho y subido.**
  - Lema M1: comparación de conos en cualquier dimensión.
  - Teorema M2: cota superior \(n^{-1/2}\), condicional a M3.
  - Comprobaciones MONOTONE_2P1_CONSISTENT y MONOTONE_3P1_CONSISTENT.
  - Ver `M1_metric_comparison_and_upper_rate.md`.
- **Pregunta abierta central.** ¿La tasa basada solo en el orden en 3+1D es \(n^{-1/2}\), o
  más rápida? En 3+1D solo hay automorfismos conformes (Zeeman, Levichev); en 2D, en
  cambio, hay grandes grupos de reparametrización.
- **Experimentos de información** (cota inferior variacional \(\tilde I_n\) sobre estadísticos
  del orden):
  - `dev/explore_information_growth_3p1_toy.py`: UNDECIDED. Control de 1+1D con
    pendiente 1.07; juguete de Minkowski 3+1D con pendiente 1.10 [1.03, 1.22].
  - `dev/explore_information_growth_degeneracy.py`: UNDECIDED (fallo de diseño anotado).
    \(\tilde I\) del juguete saltó a 41 065 en \(n=4000\), con solo 100 réplicas, por la
    combinación de la fracción de pares con \(n_{\max}\) y \(n_{\min}\).
  - **En curso al irse el PI:** `dev/explore_information_growth_boundary_cv.py`
    (\(n\) hasta 8000, 300 réplicas, regla fijada en el docstring). Si no llegó a
    terminar, **no hay fichero de resultados**: hay que relanzarlo.

## Cómo relanzar el experimento en curso

```bash
cd ~/nachocausal
git pull
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt   # si no existe .venv
.venv/bin/python dev/explore_information_growth_boundary_cv.py
```

- Tarda unos 70 minutos en un portátil de 4 núcleos y necesita unos 2 GB de RAM.
- Escribe `dev/explore_information_growth_boundary_cv_results.json` y no lo sobrescribe
  si ya existe.
- Es determinista (semillas `[7_000_923, dim, n, rep]`): da el mismo resultado en
  cualquier máquina con las mismas versiones de numpy.
- Para que la salida se vea mientras avanza, no lo pases por `tail`.

## Cómo leer el veredicto

- **METHOD_INVALID:** el control de 1+1D no sale lineal; no se interpreta el juguete.
- **SUPERLINEAR:** en el juguete 3+1D la información crece más rápido que \(n\). La tasa
  sería mejor que \(n^{-1/2}\), y el estimador combinaría la fracción de pares con
  \(n_{\max}\) y \(n_{\min}\). Siguiente: repetirlo en Schwarzschild 3+1D con
  `dev/explore_metric_comparison_3p1.py:order_3p1`; es pesado y conviene Claude cloud.
- **LINEAR_CONSISTENT:** el salto de \(n=4000\) era ruido. Siguiente: probar
  \(I_n\le Cn\) por la identidad de flujo (CREATE prueba 3, ruta Opus 1).
- **UNDECIDED:** subir las réplicas o el rango de \(n\) en un script nuevo, con su regla
  fijada antes.

## Otros pendientes

- M3 con rigor: primera variación del alcance angular (bosquejo en la nota M1, §4).
- Paper 1 (manuscrito con la §3.5):
  - auditoría de prioridad provisional en
    `research_program/bibliography/priority_audit_manuscript_s3_5_2026-10-16.md`;
  - faltan Hájek–Šidák y Lehmann–Romano (libros con derechos de autor);
  - falta la frase de reducción por invariante maximal en la §3.5;
  - falta citar Minguzzi–Sánchez, p. 36.
- Catálogo: `scripts/biblioteca_catalog/curated.csv` solo existe en la rama
  `research/causal-fidelity-bridge`. Hay que decidir si se lleva a `main` antes de
  regenerar `biblioteca/INDICE.md`.
- CREATE prueba 3 (tasa en 3+1D): `~/herramientas/CREATE/runs/2026-10-16-tasa-3p1/`.
