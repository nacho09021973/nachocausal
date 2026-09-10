# Paper III — Resoluciones pendientes: redacción exacta para firma

```text
STATUS=DRAFT_FOR_SIGNATURE
DATE=2026-09-10
SIGNED=R001 (convención de L), R002 (reescopado de la Fase 1)
PENDING=R2, R3, R4, R5, R6, R7
BLOCKERS_COVERED=G0-3, G0-4, G0-6, G0-8
```

Redacción literal de las resoluciones que quedan sin firmar, en la numeración de
[§8 del contrato](paper_iii_fase0_contrato.md). Cada bloque `APPROVED TEXT` está
escrito para firmarse tal cual, o para devolverse corregido. Ninguna se ha
aplicado.

Ninguna de estas resoluciones genera datos ni autoriza barridos. Todas son de
definición, anotación o redacción, salvo donde se indique lo contrario.

---

## R2 — convención de `N` · bloqueo: ninguno abierto, pero R001 depende de ella

**Por qué existe.** El texto firmado de R001 fija `L` y guarda silencio sobre
`N`. Toda la restitución numérica de R001 §3 y de R002 §3 asume `N` =
cardinalidad interior. Es lo que los artefactos ya hacen, pero conviene que sea
una decisión y no una herencia: si `N` incluyera los extremos, todas las cifras
`L/N^(1/4)` se moverían.

**Qué cambia si se firma.** Nada en el código ni en los artefactos. Fija la
lectura de las cifras ya publicadas.

> **APPROVED TEXT — R2.**
> En Paper III, \(N\) denota la cardinalidad del **interior** de la región
> sembrada. Los extremos \(p,q\) de un intervalo de Alexandrov no son puntos del
> sprinkling y no cuentan en \(N\), aunque sí cuenten en \(L\) por R001. Con esta
> convención se conserva la identidad exacta \(\rho \cdot \mathrm{Vol} = N\), y
> por tanto la normalización de Brightwell–Gregory \(L/(\rho V)^{1/4}\) coincide
> literalmente con \(L/N^{1/4}\), sin aproximación.

**Alternativa si se rechaza.** Declarar `N` inclusivo de extremos y volver a
restituir R001 §3 y R002 §3 con `N + 2`. La banda rigurosa seguiría
cumpliéndose, pero las pendientes cambiarían.

---

## R3 — clase de proceso puntual · bloqueo `G0-6`

**Por qué existe.** `dev/PAPER3_3P1_SCALE_NOTES.md` y
`docs/hoja_de_ruta_paper_iii.md` llaman «sprinklings de Poisson» a las dos
piernas. La pierna de caja lo es
(`dev/explore_3p1_scale_calibration.py:59`, `rng.poisson(rho * Vol)`). La
pierna intervalar **no**: extrae exactamente `n_target` puntos
(`dev/explore_3p1_bg_reference.py:32-41`), lo cual es un proceso binomial.

**Qué cambia si se firma.** Sólo texto: una línea en las notas y una en la hoja
de ruta. Ningún número se mueve.

> **APPROVED TEXT — R3.**
> La pierna intervalar de Paper III es un **proceso binomial**: extrae un número
> fijo de puntos i.i.d. uniformes en el intervalo de Alexandrov, es decir un
> proceso de Poisson condicionado a \(N = n\). La pierna de caja es un proceso de
> Poisson homogéneo de intensidad \(\rho\). Ambas son homogéneas respecto a la
> medida de Lebesgue, que en coordenadas inerciales coincide con el volumen de
> Minkowski. La elección de \(N\) fijo en la pierna intervalar es deliberada y
> legítima — es el canal \(N=n\) descrito en `CLAUDE.md` — y debe declararse en
> todo texto que reporte sus cifras. Queda prohibido describir ambas piernas
> como «sprinklings de Poisson» sin esta distinción.

---

## R4 — líneas base de las magnitudes restringidas a minimales · bloqueo `G0-4`

**Por qué existe.** `dev/explore_3p1_scale_calibration.py:184-186` anota
«expect 1» y «expect 1/4» para `⟨V⟩_min` y `⟨L⟩_min`. `Min(C)` es una selección
dependiente de `ρ`: al crecer la densidad los minimales se concentran contra la
esquina pasada de la caja y su volumen futuro medio crece con ellos. Medido
sobre los artefactos: `⟨V⟩_min/ρ` deriva +18.2 % mientras `⟨V⟩_all/ρ` es plano.

**Qué cambia si se firma.** Tres líneas de anotación en el script, y la
suspensión del canal de minimales como evidencia de escala. Ningún número se
mueve; lo que cambia es contra qué se compara.

> **APPROVED TEXT — R4.**
> Las magnitudes restringidas al conjunto de elementos minimales no tienen como
> línea base los exponentes 1 y 1/4. \(\mathrm{Min}(C)\) es una selección
> dependiente de \(\rho\), de modo que la esperanza condicionada a ser minimal no
> es lineal en \(\rho\). Las anotaciones «expect 1» y «expect 1/4» quedan
> retiradas de esas filas. Hasta que el canal de minimales disponga de una línea
> base derivada y verificada propia, **sus pendientes no pueden citarse como
> evidencia de desviación respecto de la ley asintótica**, ni compararse con el
> canal no restringido bajo la misma parametrización. Esta prohibición es la
> condición C3 de R002.

---

## R5 — incertidumbre y modelo de error · bloqueo `G0-3`

**Por qué existe.** Ninguna pendiente de §3.2 de las notas lleva dispersión. El
exponente **exactamente conocido** vale 1 y el diseño lo devuelve como
`1.0179`: ése es el suelo empírico. Y R002 §3.1 muestra algo más fino: con `L`
entero y ocho réplicas, la `sem` punto a punto es ella misma poco fiable — en
`N = 8000` seis de ocho valores son idénticos y la `sd` sale la mitad que en los
otros tres puntos, lo que por sí solo genera un χ²/dof de 3.26 que desaparece
(1.64) con un modelo de error agrupado.

**Qué cambia si se firma.** Obliga a reportar dispersión, y fija el modelo de
error de la Fase 1. Afecta a la redacción de todo resultado futuro.

> **APPROVED TEXT — R5.**
> Toda pendiente, cociente o exponente reportado en Paper III va acompañado de su
> dispersión entre semillas y del número de réplicas que la produce. Toda
> desviación respecto de un valor esperado se compara explícitamente contra el
> suelo de resolución del propio diseño, estimado en el mismo diseño mediante una
> magnitud cuyo valor sea exactamente conocido.
> Además, mientras \(L\) sea un entero de dispersión del orden de la unidad, la
> desviación típica **no se estima punto a punto** sino de forma agrupada sobre
> el barrido, y el número de réplicas debe declararse suficiente para que esa
> estimación sea estable. Un contraste cuyo resultado dependa de la `sem` de un
> único punto no es admisible como evidencia.

---

## R6 — atribución editorial · bloqueo `G0-8`

**Por qué existe.** `dev/PAPER3_3P1_SCALE_NOTES.md` §0 prohíbe explícitamente
que material 3+1D se atribuya a Paper II. Las cabeceras de los dos generadores
siguen diciendo «Paper II»:

```text
dev/explore_3p1_bg_reference.py:1      """EXPLORATION (dev/) — Paper II, Phase I reference leg.
dev/explore_3p1_scale_calibration.py:1 """EXPLORATION (dev/) — Paper II, Phase I: 3+1 discrete scale calibration.
```

**Qué cambia si se firma.** Dos líneas de docstring.

**Atención — colisión con el orden obligatorio.** Editar cualquiera de los dos
generadores antes de la corrida de reproducción no invalida `G0-7`
(un docstring no cambia la salida), pero sí cambia el hash del fichero registrado
en la tabla de entradas. Recomendación: aplicar R6 **en el mismo commit** que la
conversión de R001, es decir en el paso 2 del orden `reproducir → convertir →
reejecutar`, no antes.

> **APPROVED TEXT — R6.**
> Todo material 3+1D del repositorio se atribuye a Paper III. Las cabeceras de
> `dev/explore_3p1_bg_reference.py` y `dev/explore_3p1_scale_calibration.py` se
> corrigen de «Paper II» a «Paper III». La corrección se aplica en el paso de
> conversión del orden obligatorio de R001 §5, nunca antes de la corrida de
> reproducción, para que la tabla de entradas siga siendo verificable.

---

## R7 — estatus de `R = L⁴/V` · bloqueo `G0-5`

**Por qué existe.** Propuesta original: «`R` no se interpreta hasta que 1 y 5
estén aplicados y la pierna de caja reejecutada». La última cláusula de R001 ya
deroga toda cifra de `R` a artefacto de procedencia, de modo que R7 es en buena
parte **redundante**. Lo que añade es el estatus futuro, no el pasado.

> **APPROVED TEXT — R7.**
> `R = L⁴/V` no se interpreta, ni se cita como evidencia, ni se describe como
> calibrador, hasta que se cumplan las tres condiciones: R001 aplicada al
> generador de la pierna de caja, R5 aplicada al reporte, y la pierna reejecutada
> bajo la convención firmada. La afirmación «`R` deriva monótonamente y no
> estabiliza» queda retirada. `median_R_min` no es restituible por aritmética:
> el artefacto guarda la mediana de \(L^4/V\), no las \(L\) por elemento, y la
> mediana de \((L+1)^4/V\) no es función de ella.

---

## Resumen para decisión

| Res. | Bloqueo | Naturaleza | Mueve cifras | Toca código |
|---|---|---|---|---|
| R2 | — | convención de `N` | no, fija su lectura | no |
| R3 | G0-6 | declaración de proceso | no | no |
| R4 | G0-4 | línea base + suspensión de canal | no, cambia el contraste | 3 líneas de anotación |
| R5 | G0-3 | modelo de error y reporte | no | no |
| R6 | G0-8 | atribución editorial | no | 2 docstrings, **en el paso 2** |
| R7 | G0-5 | estatus de `R` | ya derogadas por R001 | no |

Firmadas R2–R7, quedan abiertos `G0-1`, `G0-5` y `G0-7`, que sólo cierran con la
secuencia **reproducir → convertir → reejecutar** de R001 §5. Ése es el único
trabajo restante de `GATE_0` que requiere ejecutar algo.
