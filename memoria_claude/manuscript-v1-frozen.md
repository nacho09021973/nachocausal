---
name: manuscript-v1-frozen
description: "manuscrito/manuscrito_v1_{en,es}.{md,pdf} congelados en 046b377 (2026-09-05) — nunca sobrescribir; todo cambio científico posterior va a manuscrito_v2_*"
metadata: 
  node_type: memory
  type: project
  originSessionId: 5434765d-d5a6-429e-b5fd-ca7aec093126
  modified: 2026-09-05T12:49:11.396Z
---

**Los cuatro archivos de `manuscrito/` están congelados por decisión del PI el 2026-09-05**, en
`046b37739e5339fca5976b334485d7b230ba7bab` (rama `emergencia/p1a-canal-sigma-m`). Son una
fotografía exacta de la V1 del paper WP6/S1, no un artefacto vivo.

```text
manuscrito_v1_en.md   sha256 6e3907c34760fcf756cade32bb498005de9efb848abe4c73f325e5a633c640fc
manuscrito_v1_en.pdf  sha256 802751e5ba07a71507ad80871e51b82b099c765ae054104de8b293b06a7f40a8   35 páginas
manuscrito_v1_es.md   sha256 e0b0a8d49307d35968f16961056789022167b7596793196db1b76f7188fa3e53
manuscrito_v1_es.pdf  sha256 4706540b4f904e9286ba301f4f1b7da12bf54e9db22588fff4a90ce8dbb41ff9   36 páginas
```

Fuente canónica: `research_program/synthesis/wp6_s1_finite_causal_order_manuscript.tex`,
sha256 `91f8262b1b744b2800a3319c539e41f99ecb2f54bb5a350e4a1fffd379c2e544`. El PDF inglés es esa
fuente compilada con la cadena `lualatex` + `bibtex` validada por el referee — no una
recomposición desde Markdown.

**Why:** el PI quiere que la V1 quede como registro inmutable del estado en que se cerró la
auditoría 042 y su remediación, para poder citarla y compararla contra cualquier revisión futura.
Sobrescribirla destruiría esa referencia sin dejar rastro, porque los cuatro archivos son
artefactos generados y un diff sobre ellos no es legible.

**How to apply:**
- Si el artículo cambia científicamente, crear `manuscrito_v2_en.*` y `manuscrito_v2_es.*`.
  **Nunca** regenerar sobre los `_v1_`.
- El español se produjo con un pipeline de marcadores (tokenizar la matemática del `.tex`,
  traducir sólo la prosa, reinsertar la matemática) — reconstruirlo si hace falta una V2, no
  traducir a mano. El round-trip del inglés por ese pipeline reproduce la fuente byte a byte.
- Métrica de validación, con su redacción exacta acordada — no volver a etiquetarla como
  «segmentos matemáticos idénticos» a secas:
  `MATH_SEGMENTS_STRICTLY_IDENTICAL=NO`, `MATH_SEGMENTS_TOTAL=1047`,
  `MATH_TEXT_PAYLOAD_TRANSLATED=14`, `MATH_SYMBOLIC_CONTENT_IDENTICAL=YES`,
  `EQUATION_TAGS_IDENTICAL=YES`. Los 14 segmentos son exactamente los que llevan `\text{...}`,
  cuya prosa **sí** se traduce (decisión aprobada: dejarla en inglés mutilaba la (11.4) española).
  Los identificadores `\mathrm{}` (`chain`, `antichain`, `id`, `swap`, `Past`, `sym`) no se tocan.
- El `.es.tex` lleva `\setlength{\emergencystretch}{3em}` y `babel` cargado como
  `[provide=*,spanish]` (no existe `spanish.ldf` en este TeX Live); sin eso hay 1 `Overfull` y
  errores de babel respectivamente.
- Verificar «0 contenido cortado» **geométricamente**, no por el log: `pdftotext -bbox-layout` y
  comprobar que ningún glifo pasa del ancho de página (612 pt). El log de `Overfull` sólo avisa
  por encima de `\hfuzz`. Ambos PDFs dan máximo 544,01 pt.

Relacionado: [[numbers-must-come-from-committed-script]], [[program-status-reentry-marker]].
