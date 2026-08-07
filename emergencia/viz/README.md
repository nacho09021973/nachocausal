# `emergencia/viz/` — las figuras del fracaso de la línea P1a

> **ESTADO: FIGURAS DE DIAGNÓSTICO · SOLO LECTURA SOBRE ARTEFACTOS YA SELLADOS ·
> SIN DATOS ESTOCÁSTICOS NUEVOS · NO TOCA EL SELLO · NO CONSUME SEMILLAS DE
> VALIDACIÓN · NO AFIRMA RECUPERABILIDAD.**
>
> Ningún número de estas figuras es nuevo. Todos salen de
> `emergencia/resultados/*.csv` con su `*.sha256` verificado, o se recalculan desde
> ellos y se contrastan contra la salida de un ejecutable ya auditado.

## Para qué existen

`HOJA_DE_RUTA.md` cuenta la línea en 47 000 caracteres y siete lecciones. Es correcto
y es ilegible de un vistazo. Estas seis figuras contestan, con los mismos datos, tres
preguntas que el texto sólo responde leído entero:

- **¿cuánto se falló?** (fig. 2)
- **¿por qué es imposible y no sólo difícil?** (fig. 3)
- **¿por qué se tardó meses en verlo?** (fig. 4)

El resto sitúa: la fig. 1 enseña la parte que sí salió bien y por qué engañaba, la
fig. 5 lo que la selección hace a espaldas de cualquier correlación, y la fig. 6
ordena el recorrido completo.

## Las figuras

| # | Fichero | Qué enseña | Número que la cierra |
|---|---|---|---|
| 1 | `fig01_disponibilidad.py` | El selector pasa de `1/720` a `0.697`: disponibilidad resuelta | y no medía nada de lo que hacía falta |
| 2 | `fig02_el_gate.py` | Tres representaciones, seis estratos, gate `0.80` | mejor `ρ = 0.566` |
| 3 | `fig03_canal_sigma_m.py` | El canal observable es `σ(m)`; ANOVA de un factor | `SSW/SST = 0.68–0.72` ⟹ `ρ_max = 0.531–0.568` |
| 4 | `fig04_anatomia_del_error.py` | Se navegó con `ρ_max_ub(B_n) = 0.83–0.86` como si fuera el máximo | `0.83 > 0.80`: el gate parecía alcanzable |
| 5 | `fig05_seleccion_y_estabilidad.py` | Target estable, endpoints no; los scores no coinciden; pared de la caja | coincidencia entre selectores `= 0` a `n ≥ 96` |
| 6 | `fig06_mapa_del_fracaso.py` | El recorrido entero, con el desvío marcado | `0.27 → 0.47 → 0.57`, nunca `0.80` |

Las figuras 2, 3 y 4 son una cadena y deben leerse en ese orden: **cuánto se falló**,
**por qué no había margen**, **por qué se creyó que lo había**.

## Uso

```bash
PYTHONDONTWRITEBYTECODE=1 python3 emergencia/viz/hacer_figuras.py
```

Escribe las seis en `emergencia/viz/output/` e imprime los números que van dentro de
los paneles. Dos ejecuciones dan ficheros **byte a byte idénticos** (verificado). Si
alguno de los números impresos cambia, la figura y el texto que la cita han dejado de
estar de acuerdo.

## Por qué esto no son ilustraciones

Tres controles corren **antes** de dibujar y abortan la figura si fallan:

1. **`datos._verificar`** comprueba el SHA-256 de cada CSV contra su sidecar. Un
   artefacto regenerado sin resellar no se dibuja. *Comprobado que salta*: alterando
   un byte de una copia, `leer()` lanza `ValueError` en vez de producir una figura.
2. **`datos.anova_sigma_m`** recalcula la descomposición `SST = SSB + SSW` sobre las
   observaciones —no la impone— y compara el `ρ_max` resultante con el valor impreso
   por `p1a_count_volume_canal_sigma_m_d2.py`. Discrepancia por encima de `1e-4`:
   aborta.
3. **`fig01`** contrasta enumeración exacta contra Monte Carlo en `n = 6..9`, que son
   dos implementaciones independientes del mismo estado (discrepancia máxima
   `0.0018`). **`fig06`** verifica que las tres representaciones siguen ordenadas de
   peor a mejor antes de contar esa historia.

Las constantes que **no** se recalculan están declaradas como constantes en
`datos.py` y `fig04`, con el ejecutable que las produjo escrito al lado: `B_n` por
estrato, el factor `1.000017` del Teorema CV-4.3, los umbrales `0.80` / `0.30` del
contrato congelado y el retractado `ρ_max_ub(B_n) = 0.83–0.86`.

## Dos precisiones que hay que mantener

**`ρ_max` es una identidad, no una estimación.** Sobre la muestra sellada,
`ρ_max = sqrt(SSB/SST)` es exacta: no hay iid, ni bootstrap, ni modelo. Lo que **no**
está cerrado es el enunciado poblacional
(`CV4_POPULATION_STATUS = STRONGLY_SUPPORTED_UNDER_IID_NOT_CLOSED_FORM_THEOREM`).
Ninguna figura afirma más que lo primero.

**El hueco del panel A de la fig. 4.** La figura dibuja el hueco finito-muestral
exacto `ρ_max − ρ_obs = 0.0015–0.0026`. La cifra `≤ 0.0007` que aparece en
`P1a_count_volume_canal_sigma_m_d2.md` es la misma comparación **con la corrección
intrabin del Bloque B**, y por tanto poblacional. No se contradicen; son dos
magnitudes distintas y la figura dice cuál dibuja.

## Idioma

Los rótulos están en español, como todo el corpus `emergencia/`. Si alguna vez van a
un manuscrito en inglés, el cambio es mecánico: todas las cadenas viven dentro de las
funciones `dibujar()`.
