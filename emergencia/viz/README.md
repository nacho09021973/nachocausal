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
| 2 | `fig02_el_gate.py` | Tres representaciones, seis estratos, gate `0.80` y aparcamiento `0.50` | mejor `ρ = 0.566`; `HEIGHT_WIDTH` aparcada, `COUNT_VOLUME` no |
| 3 | `fig03_canal_sigma_m.py` | El canal observable es `σ(m)`; ANOVA de un factor | `SSW/SST = 0.68–0.72` ⟹ `ρ_max = 0.531–0.568` |
| 4 | `fig04_anatomia_del_error.py` | Se navegó con `ρ_max_ub(B_n) = 0.83–0.86` como si fuera el máximo | `0.83 > 0.80`: el gate parecía alcanzable |
| 5 | `fig05_seleccion_y_estabilidad.py` | Target estable, endpoints no; los scores no coinciden; pared de la caja | coincidencia entre selectores `= 0` a `n ≥ 96` |
| 6 | `fig06_mapa_del_fracaso.py` | El recorrido entero con el desvío marcado — 11 etapas, 7 fases y el ramal CV | `0.27 → 0.47 → 0.57`, nunca `0.80` |

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

Cinco controles corren **antes** de dibujar y abortan la figura si fallan:

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
4. **`fig02`** recomputa desde el CSV los terminales de aparcamiento y aborta si
   dejan de reproducir el registro sellado (`HEIGHT_WIDTH` aparcada, `COUNT_VOLUME`
   no). *Comprobado que salta.*
5. **`fig06`** cuenta etapas y fases sobre su propia lista y aborta si el recuento
   del título deja de describir el diagrama. *Comprobado que salta.*

`tests/test_emergencia_viz.py` (12 casos, `pytest`) prueba que los controles saltan
—y prueba el predicado de aparcamiento en las **dos** direcciones, incluido el caso
que separa la regla del contrato del atajo `max(sup) < 0.50` que se usaba antes.

Las constantes que **no** se recalculan están declaradas como constantes en
`datos.py` y `fig04`, con el ejecutable que las produjo escrito al lado: `B_n` por
estrato, el factor `1.000017` del Teorema CV-4.3, los umbrales del contrato congelado
de representaciones (`P1a_contrato_representaciones_alternativas_d2.md`) y el
retractado `ρ_max_ub(B_n) = 0.83–0.86`.

Los umbrales del contrato viven en **ejes distintos** y no son intercambiables — no
respetarlo fue el error 1 de la auditoría 032:

| Cantidad | Umbral | Sentido | Fuente |
|---|---|---|---|
| correlación de Pearson | `≥ 0.80` (IC95 inferior) | cualifica para preregistrar un cociente | `:146` |
| correlación de Pearson | `< 0.50` (IC95 superior) | aparcamiento fuerte | `:156` |
| mediana del error relativo | `≤ 0.30` (IC95 superior) | cualifica | `:145` |

La fig. 2 dibuja los dos primeros, que son los del eje que traza. El `0.30` **no** es
un umbral de correlación y no aparece en ella.

## Dos precisiones que hay que mantener

**`ρ_max` es una identidad, no una estimación.** Sobre la muestra sellada,
`ρ_max = sqrt(SSB/SST)` es exacta: no hay iid, ni bootstrap, ni modelo. Lo que **no**
está cerrado es el enunciado poblacional
(`CV4_POPULATION_STATUS = STRONGLY_SUPPORTED_UNDER_IID_NOT_CLOSED_FORM_THEOREM`).
Ninguna figura afirma más que lo primero.

**El hueco del panel A de la fig. 4, y de dónde sale el `0.0007`.** La figura dibuja
el hueco **finito-muestral exacto**

```text
Delta_A = rho_max - rho_obs = +0.0015 a +0.0026   (Bloque A, los seis estratos)
```

`P1a_count_volume_canal_sigma_m_d2.md` §6.2 da, para la misma comparación, `-0.0001`
a `+0.0007`. El documento **no dice** cómo se calculó esa cifra, así que aquí no se
afirma: se **deriva y se comprueba**. Tomando `T_corr` del Bloque B —el estimador con
corrección intrabin, impreso por el ejecutable auditado— y evaluando

```text
Delta_B = sqrt(1 - T_corr) - rho_obs
```

se obtiene `-0.000045` a `+0.000703` en **los seis estratos**, que reproduce el
intervalo del documento a la precisión con que está impreso.

Esos dos números son una **evaluación puntual a la precisión de la entrada**, no un
intervalo certificado: `T_corr` solo está disponible con cuatro decimales en la tabla
del Bloque B, y propagar ese redondeo (`±5e-5`) lleva `Delta_B` hasta `+0.000747` en
`(64, PAST)`. La cota que la entrada sí sostiene es por tanto

```text
|Delta_B| < 0.0008
```

y es la que se publica. (La cota `< 0.00071` que apareció en la primera versión de
este README no es sostenible con `T_corr` a cuatro decimales: auditoría 033,
hallazgo 1.)

Es decir: `Delta_A` es la identidad exacta sobre la muestra sellada y `Delta_B` es su
versión corregida, dependiente de iid. Son dos magnitudes distintas, no una
contradicción, y la fig. 4 dibuja la primera y lo dice. La comprobación es
reproducible con `T_corr` de
`PYTHONDONTWRITEBYTECODE=1 python3 emergencia/p1a_count_volume_canal_sigma_m_d2.py`
(Bloque B) y `rho_obs` de `datos.anova_sigma_m`.

## Idioma

Los rótulos están en español, como todo el corpus `emergencia/`. Si alguna vez van a
un manuscrito en inglés, el cambio es mecánico: todas las cadenas viven dentro de las
funciones `dibujar()`.
