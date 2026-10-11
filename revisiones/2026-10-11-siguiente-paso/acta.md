# Acta — ¿cuál es el siguiente paso de la línea viva de `nachocausal`?

**Fecha:** 2026-10-11. **Convoca:** el PI.

Se os pide decidir **un** siguiente paso, no revisar trabajo hecho. No tenéis
herramientas: sólo cuenta lo que está en esta acta y en los ficheros adjuntos.

---

## 1. Estado, en hechos

`nachocausal` busca recuperar estructura de horizonte de agujero negro a partir
de **orden + recuento** de un causal set, como *benchmark de recuperabilidad*,
no como reconstrucción.

**El repo está vivo.** Hay piezas cerradas, pero el proyecto no lo está.

**Cerrado y firmado:**
- El programa del comité 049, el 2026-07-30.
- El apéndice `S4W`, el 2026-10-10, con `NO_FURTHER_WORK_RECOMMENDED`. Dejó un
  coeficiente local positivo y un hueco nombrado en la literatura.
- El programa de *saturación* de `relatividad`, parado el 2026-09-13:
  `TESIS_S = BLOCKED_UNDER_CURRENT_PRIMITIVES`, bloqueo **definicional**. Sólo
  reabre con un objeto `Char_C[G]` que cumpla siete requisitos (adjunto). Un
  umbral o percentil nuevo **no** sirve: sería `ATTACK_04` otra vez.

**La línea viva es el puente 3+1D.** Estado exacto:

- `B1` **ESTABLECIDO**: certificado formal de separación para el par congelado
  `lambda0 = (0.5,1.0,1.0,0.5,0.1)`, `lambda1 = (0.2,0.8,2.0,0.9,0.1)`, con
  redondeo dirigido de extremo a extremo. `TV >= 0.00291822`, margen 14.66 %.
  **No** es identificabilidad de `phi`, **no** es la implicación general `L3`.

- `B2` **BLOQUEADO**, con dos terminales:
  - `B2.1 = INCONCLUSIVE_BY_BOUNDS`: sobre la malla
    `t = {0.45, 0.475, 0.5, 0.525, 0.55}` del camino
    `lambda(t) = (1-t)lambda0 + t lambda1`, las envolventes de `rho` solapan
    entre puntos adyacentes.
  - `B2 = CORRECTED_CERTIFICATION_ROUTE_TOO_COSTLY`, `implemented = false`:
    la ruta formal era una partición en cajas, `M=16` sobre 4D, 65 536 cajas
    para `B` y 16 384 para `B'`.

## 2. Lo que se hizo hoy, 2026-10-11

**(a) Hallazgo de integridad.** El commit que corrigió el kernel angular el
2026-09-13 (`q`: de `exp(-s/2)/sqrt(s)` a `2exp(-s/2)/s^1.5`) no regeneró
**siete** artefactos de verificación de B2, B3 y B4. Regenerados hoy: entre el
40 % y el 80 % de las cifras cambiaron y **ningún terminal se movió**. Las
conclusiones eran correctas; las cifras bajo ellas, no. Queda instalado un
control permanente que lo detecta por grafo de imports y fechas de commit.

**(b) Paso 1, positivo y estructural.** `G(uv)` y `q(uv)` **no reciben nunca**
`lambda`; `lambda = (v0, v1, uout, uin, ·)` son los **límites del dominio** de
integración. Luego toda la dependencia en `t` está en el dominio y `rho'` es una
derivada de **Leibniz**: el integrando nunca se deriva y la unimodalidad de `G`
se conserva exacta. `Z'` son cuatro integrales 1D de `G`; `B'` son integrales de
cara. Corolario: **`B'` puede ser innecesario para separar dos `t`** — es la
regla de promoción de B2, formulada como signo de `drho/dt`, la que obliga al
objeto caro.

**(c) Paso 2, NEGATIVO.** Se aplicó la cadena analítica de B1.5 — la que no
particiona — en `lambda(0.45)` y `lambda(0.55)`:

```
t      lower         upper         ancho
0.45   0.016381084   0.032672079   0.016290995
0.55   0.017506106   0.035792517   0.018286411
criterio:  upper(0.45) = 0.032672  >  lower(0.55) = 0.017506   NO SEPARA
falta un factor 8.6x
```

Diagnóstico: la horquilla **se ensancha monótonamente** a lo largo del camino
(0.0084 en `t=0`, 0.0276 en `t=1`). B1.5 separó los extremos porque entre ellos
`rho` casi se duplica y `lambda0` tiene la horquilla más estrecha. Entre 0.45 y
0.55 `rho` se mueve ~2 % y las horquillas miden ~0.017.

Y lo peor: en esos puntos la cadena es **~14 % más ancha** que la cuadratura de
Gauss–Legendre que B2.1 ya tenía. No es un avance, es un retroceso.

Factores de estrechamiento necesarios, sobre los números oficiales regenerados:
**27.3x** para separar puntos adyacentes, **6.9x** para separar los extremos de
la malla (`0.45` vs `0.55`, que daría no-constancia de `rho` en el intervalo).

## 3. Guardarraíles vinculantes

Cualquier propuesta debe respetarlos o declarar explícitamente que pide
levantarlos y por qué:

```
no_new_path   no_new_t0   no_new_points   no_search   no_adjustment
```

Más: sin simulaciones nuevas, sin semillas, sin tocar el sello
(`thresholds.py`, sha256 `6e2c3888…bfefd4`). Y la frontera de claims sigue
prohibiendo afirmar convergencia realización-por-realización, varianza
controlada, detector práctico de horizonte, Page–Shoom discreto, reconstrucción
de Schwarzschild, emergencia del cono causal, y prioridad sin auditoría
bibliográfica separada.

## 4. La pregunta

**¿Cuál debe ser el siguiente paso?** Elegid **uno** y defendedlo. Opciones que
el PI ya tiene sobre la mesa, no exhaustivas — proponer otra es legítimo:

- **(A)** Atacar los **6.9x** de los extremos de la malla con una cota mejor que
  las dos ya probadas. ¿Cuál, concretamente?
- **(B)** Volver a la **partición en cajas** y recostearla: el veredicto
  `TOO_COSTLY` es del 2026-09-13 y nadie lo ha reevaluado con hardware ni
  aritmética de intervalos actuales.
- **(C)** Abandonar la **separación** y atacar directamente el signo de
  `drho/dt` por la vía Leibniz del paso 1, que nadie ha intentado.
- **(D)** Declarar `B2` cerrado-negativo y mover el esfuerzo a `L3` o a
  identificabilidad de `phi`, que B1 explícitamente no establece.
- **(E)** Parar la línea y documentar la frontera, como se hizo con saturación.

## 5. Qué se os pide

1. **Un** siguiente paso, nombrado y justificado.
2. **El coste**, en el orden de magnitud que podáis: ¿papel, cómputo, semanas?
3. **Qué lo falsaría barato**: el test más pequeño que mataría la propuesta
   antes de gastar en ella. El PI valora esto por encima del optimismo.
4. **Qué guardarraíl tocáis**, si tocáis alguno.

Advertencia que el PI quiere explícita: en la ronda de ayer, de once errores
suyos, diez los encontró otra familia de modelos y ninguno él releyendo; y la
casa que quedó en minoría 1–2 tenía razón en lo factual. **Un acuerdo de dos
sobre tres no es una verificación.** Si disentís, disentid.
