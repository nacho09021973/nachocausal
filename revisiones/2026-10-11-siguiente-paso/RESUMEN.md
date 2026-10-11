# Sanedrín 2026-10-11 — siguiente paso de la línea viva

**Estado del protocolo: `DEGRADED_NO_CONSENSUS`.** El asiento `opus` falló las dos
rondas (`API Error 400`: Claude Code 2.1.234 no soporta `claude-opus-5-5`, exige
2.1.280+) y el disyuntor lo desactivó. Deliberaron **cuatro** casas, ninguna de
ellas Claude: ASTRA (GPT), CIRO (Grok), ABNER (DeepSeek), GEMINI (Google).
El propio sanedrín advierte: *un veredicto en estado degradado es material de
análisis, no consenso validado*. Se arregla con `claude update` y se puede repetir.

## Acuerdo de las cuatro — un solo paso

Transferir las cadenas de B1.5 a las **cuatro caras** de `B'` en el `t0 = 0.5`
congelado, acotar las **cuatro integrales 1D** de `Z'`, y formar el intervalo con
redondeo dirigido de

```
S = B' - 2 (Z'/Z) B
```

Guardarraíles intactos, sello intacto. **No** es ninguna de las cinco opciones del
acta tal cual: es la (C) concretada, y se apoya exactamente en el resultado
estructural del paso 1 — que `rho'` es Leibniz y las caras son el objeto natural.

## Lo que las cuatro niegan que esto consiga

- **Ninguna** ha establecido que las cotas de cara sean lo bastante estrechas para
  certificar el signo.
- **Excluir cero en un punto NO emite terminal positivo de B2.1**: eso exige
  control en un **vecindario**, no en `t0`.
- Una jornada es **un presupuesto, no un coste demostrado**.

## Desacuerdo vivo — y es una decisión del PI, previa al gasto

**¿Qué cuenta como éxito en la compuerta?**

- **ASTRA**: exige `sup I_S < 0`, conforme a la regla de promoción transcrita.
- **CIRO y ABNER**: excluir cero **con cualquier signo** habilita extender el
  control a la malla, sin emitir terminal.

No discrepan sobre la necesidad del vecindario, sino sobre si un signo **positivo**
permite continuar. El PI debe fijar ese criterio **antes**, o el trabajo puede
terminar sin poder emitir nada.

Segundo desacuerdo: qué hacer si el intervalo contiene cero. **GEMINI** exige
bifurcar estrictamente entre recostear `M=16` (opción B) o documentar la frontera
(opción E). **CIRO y ABNER** quieren mantener viva una vía analítica acoplada;
GEMINI pide que la formulen antes.

## Concesión convergente, con precedente en el propio repo

Un intervalo que contenga cero **a resolución finita detiene la tentativa por
presupuesto, pero no agota la representación**: solo lo haría si su intervalo
**ideal**, sin error de integración, contuviera cero.

ASTRA y CIRO citan el precedente: **B1.5 §6 documenta que `K=L=6` no separaba y
`K=L=8` sí, con la misma cadena.** Fallar a una resolución no prueba imposibilidad.

## Posiciones retiradas en la deliberación

- CIRO, ABNER y GEMINI retiraron el ascenso de «extremos crecientes» a «derivada
  local necesariamente positiva».
- **GEMINI retiró que B2 sea un bloqueo definicional, y la extrapolación a `10^12`
  cajas como justificación para descartar el recosteo.** La opción (B) sigue viva
  y sigue sin hacerse.
- CIRO retiró su filtro de variación total como atajo demostrado.
- ABNER y CIRO abandonaron el colapso de una sola cara como test de muerte.
- ASTRA cedió la prioridad de su representación por medidas firmadas, reconociendo
  que no había demostrado ventaja computacional.

## Pendiente, según el propio veredicto

No existen envolventes certificadas de `B'`, `Z'` ni `S` en `t0`, ni una medición
del coste de la compuerta. Falta obtener las expresiones de cara con sus
coeficientes y signos, evaluar sus cotas, y **distinguir holgura angular de error
de integración**.

**Registro completo:** `sanedrin.log` (101 KB), bitácora en `sanedrin.log.log`.
