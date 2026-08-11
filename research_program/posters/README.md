# Póster WP7

Artefactos:

- `wp7_f2_f3_poster.tex`: fuente editable A0 horizontal;
- `wp7_f2_f3_poster.pdf`: PDF vectorial listo para impresión;
- `wp7_f2_f3_poster_preview.png`: previsualización raster para revisión rápida.
- `wp7_question_for_meyer.tex`: fuente del póster-pregunta dirigido a David A. Meyer;
- `wp7_question_for_meyer.pdf`: PDF vectorial de la pregunta experta;
- `wp7_question_for_meyer_preview.png`: previsualización del póster para Meyer.

Compilación reproducible:

```bash
cd research_program/posters
xelatex -interaction=nonstopmode -halt-on-error wp7_f2_f3_poster.tex
xelatex -interaction=nonstopmode -halt-on-error wp7_question_for_meyer.tex
```

Fuentes de verdad del contenido:

- `../work_packages/wp7_f2_f3_product_order_contract.md`;
- `../work_packages/wp7_f2_f3_higher_dimensional_extension.md`;
- `../bibliography/wp7_f2_f3_primary_novelty_audit.md`.

Formato verificado: una página A0 apaisada, `3370.39 × 2383.94 pt`. El póster conserva
literalmente los calificadores de alcance de de Sitter y prohíbe cualquier afirmación de prioridad
absoluta. La versión para Meyer incorpora la extensión probada a toda dimensión fija `d>=2`,
incluidos `2+1` y `3+1`.
