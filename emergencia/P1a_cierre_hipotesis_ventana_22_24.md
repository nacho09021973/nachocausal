# P1a — Cierre de la hipótesis de la ventana 22–24

ESTADO = CERRADO
FECHA = 2026-08-27
TERMINAL = `K_DEPENDENT_LOCATION`
CONTRATO = `P1a_contrato_robustez_en_K_d2.md`, sha `830e04791bc027425601842c6daa5bf507e060928ed5bce0c612a4e7d665a233`
(congelado antes de ejecutar; **no modificado** después)

---

## 1. Qué se falsó

La hipótesis bajo prueba era que el extremo de competencia observado en la
ventana 22–24 fuese una propiedad del objeto combinatorio y no la escala del
propio selector.

**Queda falsada.** La localización del máximo en `n` depende del suelo de
admisibilidad `K0`:

| K | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| `n*` = argmax de `p_n(K)` | 20 | **24** | 32 | 38 |

`p_n(K) = P(R≥5 | E)`, observable primario congelado. El desplazamiento es
**grande, monótono y ordenado**, no marginal. Tres de los cuatro brazos
`DESPLAZA`; solo el ancla `K=3` mantiene, como debía por construcción.

Los tres secundarios **concuerdan en cada brazo** (argmin de `U_n^\star`, argmax
de `Sbar_n_tie` y de `H_tie_n` caen en el mismo punto o en uno adyacente al del
primario). No decidieron el terminal, pero descartan un artefacto de un solo
observable.

**Conclusión precisa — no sobreleer.** No es que «todo fuera artefacto del
algoritmo». Es, exactamente:

> La localización del máximo en `n ≃ 22–24` depende de `K0`. Por tanto **no hay
> base para atribuir significado intrínseco a la ventana 22–24**.

---

## 2. Qué sobrevive, y con qué alcance

Dos resultados que deben conservarse **separados**:

**(a) La escala del pico es dependiente del selector.** Establecido por esta
campaña. Es el resultado negativo, y es sólido.

**(b) El régimen `R≥5` condicionado es estructuralmente distinguible y persiste
hasta `n=40`.** Establecido por la campaña de contraste mecanístico
(`P1a_interpretacion_paso7_contraste_r2_rge5_d2.md`, terminal
`SUPPORTED_PERSISTENT_SEPARATION_AT_N40`). Sigue siendo cierto **para este
selector**.

Lo que este cierre añade es la articulación entre ambos: **la frecuencia con la
que el algoritmo entra en el régimen `R≥5` está gobernada por su suelo de
admisibilidad**, mientras que la distinción cualitativa de ese régimen, cuando
ocurre, persiste.

**Ninguna de las dos es una afirmación universal sobre causal sets.** Ambas son
afirmaciones sobre `MIN_COVERAGE_LEX` en `d=2`, sobre la malla `n ∈ [20,40]` y
`K ∈ {2,3,4,5}`.

---

## 3. Compromiso de no parcheo (registrado antes del resultado)

Acordado antes de ver el terminal y cumplido literalmente:

- **ningún `K=6`**;
- **ningún score nuevo**;
- **ningún selector alternativo** para salvar el pico;
- ninguna redefinición de `R`.

Buscar una variante que devolviera el pico habría sido búsqueda de confirmación
con pasos adicionales, no robustez.

---

## 4. Alcance de lo observado (bordes)

- En `K=2` el argmax cae en `n=20`, **borde izquierdo de la malla**. La regla lo
  clasifica `DESPLAZA` correctamente (meseta `{20}`, disjunta de `W`), pero el
  máximo real podría estar por debajo de 20 y **no se ha observado**. Es un
  desplazamiento demostrado, no un pico localizado.
- En `K=5` el argmax en `n=38` sí es interior (`n=40` baja).
- El terminal no depende de ninguno de los dos casos.
- Ninguna celda fue censurada: las 44 son analizables.

---

## 5. Trazabilidad

Cadena auditada en orden, antes de mirar ningún valor científico:

```
44/44 COMPLETE → controles → artefactos → sidecars → read-back → tests
```

| control | valor |
|---|---|
| `SEALED_SELECTOR_UNTOUCHED` | `71594620005e2b83…f79bda2b` (intacto) |
| `K3_ARM_REPRODUCES_SEALED_CAMPAIGN` | PASS |
| `PAIRED_SAMPLE_IDENTITY` | PASS |
| `LONG_RECOMPOSITION` | PASS |
| `BACKEND_FAILURES` | 0 |

| artefacto | sha256 |
|---|---|
| `p1a_k_robustness_summary_d2.csv` | `10b054379e13c399…75f0346f` |
| `p1a_k_robustness_long_d2.csv` | `1743861cfb0b7f47…52384d6a` |
| `p1a_k_robustness_resumen.json` | `1953ee72b6d89023…8fe158694` |

Suite `tests/test_p1a_k_robustness_d2.py`: **13 passed, cero skipped** — el
read-back desde disco se ejecutó.

---

## 6. Lo que NO se abre aquí

La reformulación que sustituye a esta rama queda **planteada, no iniciada**:

> ¿Qué información intrínseca del causet puede extraerse del orden **sin exigir
> la elección canónica de un único elemento o candidato**?

Cambia el problema: ya no se busca vencer a los automorfismos con un selector
más ingenioso, sino preguntar qué objetos sobreviven al cociente por ellos.
Candidatos conceptuales mencionados —órbitas, conjuntos de candidatos,
distribuciones sobre órbitas, multiplicidades, invariantes relacionales— **no se
eligen aquí**.

El primer paso de esa línea no es un run ni un observable, sino algo que esta
rama nunca hizo: **escribir qué tendría que satisfacer una noción de
«información geométrica identificada por el orden» para ser físicamente
interesante y no simplemente otro observable arbitrario.**

Merece sesión y contrato propios.

---

## 7. Nota de método

La hipótesis salió mal; **el experimento salió bien**. Se diseñó un falsador con
capacidad real de destruir la interpretación vigente, se congeló antes de ver
datos, y destruyó exactamente lo que debía destruir. El valor de este registro
está en el cierre, no en el hallazgo.
