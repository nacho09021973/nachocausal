# `viz/` — figuras pedagógicas del manuscrito de límites

> **ESTADO: FIGURAS_DE_APOYO / NO_TOCAN_EL_SELLO / SIN_SEMILLAS_DE_VALIDACIÓN /
> NO_AFIRMAN_RECONSTRUCCIÓN.**
>
> Estas figuras ilustran teoremas ya demostrados en `docs/manuscript_limits_draft.md`.
> No producen resultados nuevos, no consumen la banda de semillas reservada
> `[2.000.000–2.999.999]` y no tocan `thresholds.py`.

## Para qué existen

La relatividad general se explica sola con la malla elástica hundida. Los conjuntos
causales se dibujan siempre de dos maneras —diagramas de Hasse abstractos, o puntos
en Minkowski con conos encima— y **ninguna de las dos enseña qué deja de ver el
orden**, que es justamente de lo que vive este manuscrito.

Estas cinco figuras están pensadas para un estudiante, no para un especialista. Esa
elección **sube** el listón de exactitud, no lo baja: un experto lee el pie de figura
y perdona una imprecisión; un estudiante se cree el dibujo literalmente.

## Las figuras

| # | Fichero | Qué demuestra | Ancla |
|---|---|---|---|
| 1 | `fig01_diccionario.py` | Qué se tira a la basura al pasar del espaciotiempo al causet | — |
| 2 | `fig02_escala_invisible.py` | La escala absoluta es invisible al orden | Teorema 3.1 |
| 3 | `fig03_teleologia.py` | Lo que pasa fuera del parche no está en el parche | Teorema 3.2 |
| 4 | `fig04_pared_de_la_caja.py` | Por qué murieron los localizadores C1–C5 | acta 042 |
| 5 | `fig05_lo_recuperable.py` | Lo que el orden **sí** lee: `r/r_s` | pareja de la Fig. 2 |

Las figuras 2 y 5 son una pareja y deben ir juntas: la 2 dice que `r_s` es invisible,
la 5 dice que `r/r_s` no lo es. Juntas son la tesis del manuscrito en dos imágenes.

## Uso

```bash
python3 viz/hacer_figuras.py     # genera las cinco en viz/salida/ e imprime sus números
```

Cada figura fija su semilla: dos ejecuciones dan bytes idénticos. Los números que
imprime el runner son los que van impresos en los paneles; si cambian, el pie de
figura del manuscrito ha dejado de coincidir con la figura.

## Exactitud: por qué esto no es un dibujo bonito

Dos propiedades de Schwarzschild 1+1 hacen que todo el código sea exacto y auditable
de un vistazo (`causet_core.py` lo documenta línea a línea):

1. **`det g = −1`**, luego la forma de volumen es `dt dr` y el sprinkling es
   **uniforme en el rectángulo `(t, r)`**. Cualquier peso en el código sería un error.
2. Con la tortuga `r* = r + r_s ln|r/r_s − 1|` la métrica es conformemente plana,
   luego el orden causal es **exactamente** el orden producto en las nulas
   `(u, v) = (t − r*, t + r*)`. No se integran geodésicas ni se aproxima nada.

Comprobaciones que se ejecutan **antes** de dibujar, y que abortan la figura si fallan:

- `fig02` verifica que `Φ_s` preserva el orden **elemento a elemento** (0 discrepancias);
  si no, lanza `AssertionError` en vez de dibujar algo falso.
- `fig03` verifica que las dos continuaciones dejan el parche observado **idéntico**.

## Una trampa que la figura 2 evita, y hay que seguir evitando

El Teorema 3.1 es `TV = 0` entre **leyes**, no entre realizaciones. Dos sprinklings
*independientes* a masas distintas **no** dan el mismo poset. Lo que ocurre es que
`Φ_s` es un isomorfismo de orden, así que el mismo conjunto de puntos, transportado,
es un sprinkling legítimo del otro modelo con las mismas relaciones — y el teorema es
lo que convierte esa construcción en genérica en vez de en un caso escogido.

Si una versión futura de la figura sugiere «dos tiradas independientes salieron
iguales», está afirmando algo falso y hay que rechazarla.

## Pendiente

**Idioma.** Las etiquetas están en español; `docs/manuscript_limits_draft.md` está en
inglés. Antes de incorporarlas hay que decidir uno de los dos, y el cambio es
mecánico: todas las cadenas viven en las funciones `dibujar()`.
