# B2 — paso 2: la cadena de B1.5 no separa la malla

**Fecha:** 2026-10-11
**Autorizado por:** el PI
**Ejecutado:** `rho_upper` y `rho_lower` de `verify_b1_5_analytic_separation.py` evaluadas en
`lambda(0.45)` y `lambda(0.55)`. Sin escribir artefactos, sin sprinklings, sello intacto.

```text
RESULTADO = NEGATIVO
LA_RUTA_BARATA_QUE_PROPUSE = REFUTADA
PASO_1 = INTACTO (es estructural y no depende de esto)
```

---

## 1. Control de la invocación

La cadena reproduce exactamente los números publicados en B1.5 §1:

```text
rho_upper(lambda0) = 0.01990853592131315   publicado 0.01990853592131315
rho_lower(lambda1) = 0.02282676120387055   publicado 0.022826761203870553
```

Luego lo que sigue es un resultado sobre el método, no sobre mi forma de llamarlo.

## 2. El resultado

```text
t      lower         upper         ancho
0.45   0.016381084   0.032672079   0.016290995
0.55   0.017506106   0.035792517   0.018286411

criterio de B1.5:  upper(0.45) < lower(0.55)?
  0.032672079  vs  0.017506106   ->  gap = -0.015165973   NO SEPARA
  factor que faltaria: 8.6x
```

## 3. Por qué funcionó en los extremos y no aquí

La horquilla **se ensancha monótonamente a lo largo del camino**:

| t | horquilla | ancho |
|---|---|---:|
| 0.00 | `[0.011509, 0.019909]` | 0.008400 |
| 0.45 | `[0.016381, 0.032672]` | 0.016291 |
| 0.55 | `[0.017506, 0.035793]` | 0.018286 |
| 1.00 | `[0.022827, 0.050436]` | 0.027609 |

B1.5 separó `lambda0` de `lambda1` porque entre ellos `rho` **casi se duplica**, y porque la
horquilla en `lambda0` es la más estrecha de todo el camino (0.0084): las dos horquillas
simplemente no se cruzan, con un margen de `+0.002918`.

Entre `t=0.45` y `t=0.55`, `rho` cambia alrededor de un 2 %, mientras las horquillas miden
~0.017. No es que falte poco: falta un factor 8.6.

**El método es más débil justo donde B2 lo necesita**, porque la anchura crece con `t` y la
separación real entre puntos vecinos de la malla es diez veces menor que entre los extremos.

## 4. Lo peor del resultado

La cadena analítica no solo es insuficiente: en estos puntos es **más ancha que la cuadratura de
Gauss–Legendre que B2.1 ya tenía**.

| t | cadena B1.5 | B2.1 (GL regenerado) |
|---|---:|---:|
| 0.45 | 0.016291 | **0.014310** |
| 0.55 | 0.018286 | **0.015960** |

Es decir: aplicar B1.5 aquí no es un avance, es un retroceso de ~14 % en anchura. Su virtud es ser
una cota rigurosa sin depender de la estabilidad de la cuadratura, no ser estrecha.

## 5. Consecuencia para mi propia propuesta

`dev/B2_RECOST_PROPOSAL_2026-10-11.md` se apoyaba en que la cadena de B1.5, que no particiona,
haría barato lo que la partición en cajas hacía caro. **Esa premisa queda refutada** para los
puntos de la malla de B2. El «objetivo barato» de 6.9x no es alcanzable por esta vía: con esta
cadena faltan 8.6x, y partiendo de una horquilla peor que la que ya había.

Lo que **no** queda refutado:

- El paso 1 (`dev/B2_STEP1_PAPER_ANALYSIS_2026-10-11.md`): que `rho'` es Leibniz puro y que `G`
  nunca se deriva es estructural y sigue siendo cierto.
- Que `B'` pueda ser innecesario para *separar* dos `t`: sigue siendo cierto que separar no
  requiere la derivada. Lo que este paso muestra es que **ninguna de las dos herramientas
  existentes separa**, ni la cadena ni la cuadratura.

## 6. Estado

```text
B2 = SIGUE BLOQUEADO
B2.1 = INCONCLUSIVE_BY_BOUNDS   (sin cambio)
RUTA_B1.5_SOBRE_LA_MALLA = CERRADA_NEGATIVA
```

Cerrar esto costó una evaluación de funciones ya escritas. El paso 2 estaba secuenciado como
prueba precisamente para esto, y la prueba salió en contra.
