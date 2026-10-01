# Archivo de trabajo: unicidad radial 3+1, 6 de septiembre de 2026

Este directorio preserva los 19 archivos científicos de la jornada, copiados
sin cambios de contenido. Incluye demostraciones, notas, exploraciones,
scripts de verificación y resultados guardados. La unicidad global original
continúa abierta según las notas archivadas.

## Contenido y procedencia

| Archivo o directorio archivado | Procedencia original | Archivos |
|---|---|---:|
| [analisis_kernel_conforme_2026-09-06.md](analisis_kernel_conforme_2026-09-06.md) | `/home/adnac/analisis_kernel_conforme_2026-09-06.md` | 1 |
| [radial_l2_2026-09-06/](radial_l2_2026-09-06/) | `/home/adnac/radial_l2_2026-09-06/` | 3 |
| [radial_l2_global_2026-09-06/](radial_l2_global_2026-09-06/) | `/home/adnac/radial_l2_global_2026-09-06/` | 11 |
| [radial_dominio_G_2026-09-06/](radial_dominio_G_2026-09-06/) | `/home/adnac/radial_dominio_G_2026-09-06/` | 3 |
| [Estudio compass_artifact.md](<bibliografia/Estudio compass_artifact.md>) | `/home/adnac/nachocausal/biblioteca/Estudio compass_artifact.md` | 1 |

El [manifiesto PROVENANCE.json](PROVENANCE.json) registra para cada archivo
su ruta original, ruta archivada, tamaño y SHA-256. También identifica el
commit previo al archivo y las tres cachés de Python excluidas.
Los originales se conservan en sus ubicaciones de partida.

El estudio bibliográfico de Claude estaba bajo la regla general que ignora
`biblioteca/`. Se conserva aquí como documento de investigación, sin modificar
esa regla ni incorporar la biblioteca completa. Sus afirmaciones se preservan
tal como fueron recibidas: este archivo no constituye una nueva validación
de sus referencias o conclusiones.

## Lectura

1. La nota inicial contiene el análisis conforme y del modelo de vértice.
2. [Obstrucción lateral y sucesión singular](radial_l2_2026-09-06/obstruccion_normal_y_sucesion_singular.md).
3. [Energía positiva y reconstrucción desde el dato de borde](radial_l2_global_2026-09-06/energia_positiva_y_reduccion_de_borde.md).
4. [Dominio de G por momentos](radial_dominio_G_2026-09-06/dominio_G_por_momentos.md).

Los scripts `explore_*` y `fixed_boundary_exploration.json` son exploraciones.
Las notas distinguen estas exploraciones de las demostraciones y de las
verificaciones simbólicas exactas. Se han preservado también los intentos
que no produjeron una prueba de unicidad.

## Verificar la copia en otro ordenador

Desde este directorio, con Python 3:

```bash
python3 archive_tools.py verify
```

No se necesitan paquetes adicionales para comprobar los hashes. En el
ordenador original se puede verificar además que no falta ningún archivo
científico de los directorios fuente y que sus bytes coinciden:

```bash
python3 archive_tools.py verify --sources
```

## Ejecutar las verificaciones sin modificar el archivo

El entorno observado al preservar la jornada era Python 3.12.3,
NumPy 1.26.4, SciPy 1.17.1 y SymPy 1.14.0. Son versiones registradas
para reproducibilidad; no se exige alterar el entorno general del repositorio.
Los dos verificadores simbólicos necesitan SymPy; el verificador lateral
y algunas exploraciones también necesitan NumPy y SciPy.

```bash
python3 archive_tools.py run radial_l2_2026-09-06/verify_edge_sequence.py
python3 archive_tools.py run radial_l2_global_2026-09-06/verify_global_energy.py
python3 archive_tools.py run radial_dominio_G_2026-09-06/verify_domain_moments.py --degree 4
```

La herramienta trabaja sobre una copia temporal, muestra los resultados y
comprueba si los JSON resultantes coinciden con los archivados. Los resultados
temporales se descartan y las evidencias originales permanecen intactas.
Un cambio de versiones o plataforma puede afectar resultados numéricos.

Cuatro exploraciones conservan una lectura histórica de
`/home/adnac/radial_l2_global_2026-09-06/explore_energy.py`.
Para ejecutarlas en otro ordenador, la misma herramienta redirige esa lectura
a la copia temporal, sin editar el código científico:

```bash
python3 archive_tools.py run radial_l2_global_2026-09-06/check_primitive_energy.py
```

Las rutas absolutas citadas dentro de las notas también se conservan por
procedencia; la tabla y el manifiesto permiten localizar sus copias en Git.

## Exclusiones

Se excluyeron únicamente tres archivos `.pyc` de `__pycache__`, regenerables
a partir de los scripts incluidos. No se excluyó ningún archivo científico
de las cuatro ubicaciones de trabajo ni el estudio bibliográfico identificado.
