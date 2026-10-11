# B2 — propuesta de reevaluación de coste

**Fecha:** 2026-10-11
**Estado:** `SUPERSEDED_NEGATIVE` — ejecutada y **refutada** el mismo dia.

> **Resultado.** Paso 1 positivo (`dev/B2_STEP1_PAPER_ANALYSIS_2026-10-11.md`), paso 2
> **negativo** (`dev/B2_STEP2_RESULT_2026-10-11.md`): la cadena de B1.5 no separa `lambda(0.45)`
> de `lambda(0.55)` —faltan 8.6x— y ademas es ~14 % mas ancha que la cuadratura que B2.1 ya tenia.
> Los factores de esta nota, corregidos a 27.3x / 6.9x tras regenerar los artefactos obsoletos,
> **no son alcanzables por esta via**. Leer esta nota solo como registro de la hipotesis.
**Alcance:** reevaluar si la ruta de certificación de B2 sigue siendo demasiado cara.
No propone curva nueva, ni `t0` nuevo, ni puntos nuevos.

---

## 1. El hallazgo: una cronología

B2 está parado por dos terminales, ambos del 2026-09-13:

```text
B2.1  = INCONCLUSIVE_BY_BOUNDS                       (envolventes solapadas)
B2    = CORRECTED_CERTIFICATION_ROUTE_TOO_COSTLY     (implemented = false)
```

La ruta descartada por coste es una **partición en cajas**,
`finite_boxes_with_monotone_endpoint_bounds`, con `M = 16` sobre el dominio 4D:

| cantidad | cajas |
|---|---:|
| `Z` | 256 |
| `Z'` | 64 |
| `B` | 65 536 |
| `B'` | 16 384 |

**Catorce horas después**, el 2026-09-14, B1.5 resolvió el problema hermano por una vía que
**no particiona**: sustituyó la integración por una cadena de desigualdades en forma cerrada
—unimodalidad de `G` en `w`, las identidades
`int int_{Vx<=Vy}(Vy-Vx) = (v1-v0)^3/6` y `(Vy-Vx)^2 -> (v1-v0)^4/12`, Cauchy–Schwarz, y cotas
sup con redondeo dirigido de extremo a extremo—. Eso llevó B1 de `NOT_ESTABLISHED` a
`B1_FORMAL_CERTIFICATE = ESTABLISHED`.

```text
6f866a2  09-13 19:58   B2 -> TOO_COSTLY  e  INCONCLUSIVE_BY_BOUNDS
5d029c7  09-14 09:29   nace la cadena analitica de B1.5
f4b5846  09-14 10:37   B1.5 -> AUDIT_PASS_FORMAL
```

**B2 no se ha tocado desde el 09-13.** Su veredicto de coste se emitió contra una maquinaria
que fue superada a la mañana siguiente, y nadie volvió a costearlo.

## 2. Cuánto habría que estrechar

De las envolventes registradas en `verification_b2_1_local_injectivity.json`:

| t | envolvente | ancho | centro |
|---|---|---:|---:|
| 0.450 | `[0.00516753, 0.00697562]` | 0.00180809 | 0.00607158 |
| 0.475 | `[0.00527167, 0.00713325]` | 0.00186158 | 0.00620246 |
| 0.500 | `[0.00537664, 0.00729216]` | 0.00191552 | 0.00633440 |
| 0.525 | `[0.00548242, 0.00745234]` | 0.00196992 | 0.00646738 |
| 0.550 | `[0.00558905, 0.00761378]` | 0.00202473 | 0.00660141 |

```text
separar puntos ADYACENTES  -> factor 15.1x   (monotonicidad local: el terminal positivo de B2.1)
separar los EXTREMOS       -> factor  3.8x   (no-constancia de rho en [0.45, 0.55])
```

Esto da **dos objetivos, no uno**, y el barato no estaba identificado:

- **3.8x** separa `t=0.45` de `t=0.55` y establece que `rho` **no es constante** en el intervalo.
  Es menos que monotonicidad local, pero es un resultado positivo y cuesta cuatro veces menos.
- **15.1x** es lo que pide el terminal `B2.1_POSITIVE_LOCAL_MONOTONICITY`.

## 3. Lo que NO se afirma

- **No se afirma que la cadena de B1.5 transfiera.** B1.5 acota `rho`; B2 necesita acotar
  `rho' = B'/Z^2 - 2(B/Z^2)(Z'/Z)`. La derivada puede romper justo la estructura que el colapso
  explota. Esto es una hipótesis a comprobar en papel **antes** de escribir código.
- **No se afirma que 15.1x sea alcanzable.** El margen de B1.5 fue 14.66 % sobre cotas que su
  propio texto llama «deliberadamente burdas», lo que sugiere holgura; pero son integrales
  distintas y esa holgura no se hereda.
- **No se afirma que B2.1 esté mal.** Su terminal es correcto para la maquinaria que usó.

## 4. Lo que haría falta, en orden

1. **En papel, sin código:** ¿sobrevive la unimodalidad de `G` y el colapso de §2 de B1.5 al pasar
   a `B'`? El propio JSON de B2 ya registra las monotonías relevantes
   (`q` creciente en `UV` sobre `[-1.35, 0.63]`; `G` creciente en `[-1.35,0]` y decreciente en
   `[0,0.63]`; probabilidad angular creciente en presupuesto no negativo). Si la respuesta es no,
   la propuesta muere aquí y no cuesta nada.
2. Si sobrevive: aplicar la cadena al objetivo **3.8x** primero, que es el barato.
3. Solo entonces evaluar si 15.1x está al alcance.

## 5. Guardarraíles respetados

El certificado de B2 fija `no_new_path`, `no_new_t0`, `no_new_points`, `no_search`,
`no_adjustment`, todos `true`. **Esta propuesta no toca ninguno:** misma curva
`lambda(t)=(1-t)lambda0 + t·lambda1`, mismo `t0 = 0.5`, misma malla de cinco puntos. Lo único
que cambia es el **método de acotación**, no el objeto acotado.

Tampoco es ATTACK_04 con otra parametrización: no se introduce umbral, gradiente, máximo ni
percentil nuevo. Y no reabre `relatividad` en el sentido de la nota de parada del 2026-09-13
—no hay `Char_C[G]` aquí, ni se pretende—; B2 es la línea del puente 3+1D, no el programa de
saturación.

## 6. Qué decide el PI

Autorizar o no **el paso 1**, que es análisis en papel y no gasta presupuesto, no genera
sprinklings y no toca el sello.
