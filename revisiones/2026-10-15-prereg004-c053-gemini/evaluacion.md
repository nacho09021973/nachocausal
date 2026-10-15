# Evaluación de la revisión cruzada del prereg-004 tras el comité 053 (gemini-4-argon, thinkingLevel=high)

Fecha: 2026-10-15. Evaluador: Claude Opus 5.5, que escribió el paquete, el borrador y su revisión
(no es evaluación independiente). Herramienta: revision-ciega @ ~/herramientas c12c10e. Documentos
en 007947e (los nueve de `documentos.txt`). Una ronda.

**Veredicto del revisor:** «listo con cambios menores enumerados». Tras comprobarlo contra el
código, las objeciones se sostienen; una de ellas (G8) es un resquicio real del código, no solo
del texto, y es la más importante. El informe ocupa unas 3000 palabras, por encima del máximo de
2000 pedido; no afecta al contenido.

## Objeciones comprobadas

| # | objeción | estado | comprobación |
|---|---|---|---|
| G1 | En el bloque de procedencia, `env \| grep NUMBA_` no registra `NUMBA_NUM_THREADS=20`, que solo se pone como prefijo de la línea de lanzamiento | **comprobado** (lectura del bloque, §9) | hay que exportarlo antes del bloque |
| G2 | El bloque usa `<(...)`, sintaxis de bash, en un bloque marcado `sh`; con `dash` falla | **comprobado** | `/bin/sh` es dash en Ubuntu; marcar `bash` |
| G3 | `grep -v '^#'` conserva líneas vacías del lockfile | **parcial** | `grep -c '^$' requirements-lock.txt` → 0 hoy; se endurece igual (`grep -vE '^(#\|$)'`) |
| G4 | «una sola horquilla limpia ⇒ la corrida no puede PASS» solo vale en ρ\*; en ρ = 32 o 63 el IQR y (iii) no se consultan | **comprobado** | `verdict_from_levels`: IQR y `stab_pass` solo de `prim` (`validate.py` l. 248-252). Error de alcance del texto |
| G5 | Con 0 semillas válidas del generador, `escape_pass` (`0 ≤ 1`) y `n_abstain_BH < 3` dan True en vacío | **comprobado** | `validate.py:171,193`. No afecta al veredicto (es INCONCLUSIVE), pero sí a los valores *non-verdict* que el §7 promete informar |
| G6 | Los valores *non-verdict* bajo INCONCLUSIVE no los produce el código: `verdict_from_levels` retorna antes de `checks`; hay que calcularlos en el documento de resultado a partir de `levels`. La guarda `status != "scored"` del bucle de F es inalcanzable | **comprobado** | `validate.py` l. 226-245. Inofensivo; se aclara en el texto |
| G7 | La reducción de (i) a `p = 2^-m` exige que no escape ninguna semilla plana en ese nivel; (iv) no limita los escapes en ρ = 63 y en ρ\* permite 1 | **comprobado** | `verdict_from_levels` usa `escape_pass` solo de `prim`; el §7 ya lo condiciona («with the flat control abstaining»), pero no dice lo de ρ = 63 |
| G8 | `_check_freeze` usa `git log --diff-filter=A` **sin `--full-history`**: un commit alternativo C1_alt desde `C1^`, con `git merge -s ours C1`, hace que `git log` devuelva solo `[C1_alt]` y el manifiesto acepte otro sorteo | **comprobado ejecutando** en un repo temporal (scratchpad, sin artefacto): por defecto devuelve solo C1_alt; con `--full-history` devuelve los dos y la comprobación de unicidad falla | `seed_manifest.py:40`. Resquicio de código; deja rastro en el grafo y contradice el SHA anotado, pero el código no lo detecta. Se cierra con `--full-history` |
| G9 | «bracket-valid» no está definido en §4 | **comprobado** | `scorer.blind_bracket`: válida si ambas clases del corte son no vacías; además la semilla debe ser válida y el BH no abstenerse (`validate.per_seed`) |
| G10 | `check_seed` admite la banda de exploración aunque `STATUS == "FROZEN"`; el §6 la llama «quemada» | **comprobado**, por diseño | `validate.py:93-94`. La corrida C3 exige las semillas del manifiesto (`run`), así que «quemada» significa «nunca semilla de validación»; se aclara el texto |
| G11 | `ABORTED_GUARD_V` / `ABORTED_TAU_RANGE` no existen en el código; son etiquetas de procedimiento | **comprobado** | `grep ABORTED nachocausal2p1/` → nada. El §9 ya dice que se informan así; se aclara que son etiquetas del documento de resultado |

## Confirmado sin objeción

Precedencia (salvo G11), semántica NaN de (i)-(iv) en ρ\*, (v) como precondición, tabla de θ, la
aritmética de potencia (0,53; 0,945; 0,975, coincide con mi comprobación con scipy) y la simetría
de su redacción.

## Contra la expectativa previa

H1 (OUT_OF_DOMAIN y abortos en `run`): detectado. H2 (minado del SHA): detectado y separado de G8.
H3 (unicidad dependiente de un fichero ignorado): detectado. H4 (bash, `/tmp`, diff del lockfile):
detectado y ampliado (G1). H5 (aritmética): confirmada. H6 (reducción de (i)): detectado y
precisado (G7). Objeción válida no prevista: **G8**, la más grave; también G4, G5, G9, G10.
Afirmaciones falsas sobre el código: ninguna encontrada.

## Qué se cambia

- **Código (sellado en C1, requiere `/auditor` sobre el delta):** `--full-history` en
  `seed_manifest._check_freeze`, con un test que reproduce el merge `-s ours`.
- **Texto (borrador):** G1-G7, G9-G11.
- **No se cambia** ningún umbral, semilla ni criterio.
