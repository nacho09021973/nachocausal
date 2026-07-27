# WP4 — Diseño numérico para `Ibar` en el diamante de registro

**Estado:** `DESIGN_ONLY / NO_IMPLEMENTATION / NO_EXECUTION`.

Este documento congela el diseño previo a cualquier nueva cuadratura de Fisher. No modifica
`wp4_kappa_numeric_reference.py`, no crea un integrador alternativo, no consume semillas, no
ejecuta sprinklings ni el banco sellado, y no cambia umbrales ni etiquetas ya adoptadas.

## 1. Objeto y alcance exactos

Familia: diamantes causales EF de WP4 con esquinas fijas

```text
r_p = 3.0, r_q = 0.5, v_p = 0.0, v_q = 0.02,
tau in [1.0, 1.2].
```

El objeto puntual es

```text
I(tau) = integral_[0,1]^2 (partial_tau log c_tau(x,y))^2 c_tau(x,y) dx dy,
```

donde `c_tau` es la densidad de cópula de la medida de volumen normalizada del diamante
`D_tau`, expresada respecto de Lebesgue `dx dy` en el cuadrado unidad. La medida inicial en
coordenadas EF es `dv dr`, pues `sqrt(-det g_tau)=1`; el cambio a `(x,y)` se hace mediante las
marginales y sus mapas cuantiles, como en WP4-floor §4 y el integrador de referencia existente.

El objeto uniforme requerido por la Proposición 4 es

```text
Ibar_[1.0,1.2] = sup_{tau in [1.0,1.2]} I(tau).
```

Una evaluación puntual, ni siquiera en los extremos, no es `Ibar`. Una maximización sobre una
malla finita tampoco certifica el supremo sin una envolvente de error entre nodos.

## 2. Estado previo fijado

La prueba de refinación de 2026-07-27 observó deriva espacial fuerte en el valor puntual de
`I(1.0)` al variar conjuntamente la malla espacial y la cuadratura de cópula. Por tanto:

```text
IBAR_DIAMOND_INTERVAL = INCONCLUSIVE_NUMERICAL_NONCONVERGENCE
CONSTANT_LEVEL_DEFEATER = NOT_EVALUATED_IBAR_UNAVAILABLE
```

No son terminales científicos negativos. Prohíben solamente usar la implementación actual para:

- declarar `PASS` o `FAIL` de `zeta_1 * Ibar >= kappa^2 dv^2 / 54`;
- cuantificar la eficiencia constante de `S_n`;
- comparar `S_n` con la información completa del poset;
- publicar un `n*` derivado de `Ibar`.

No alteran `Delta_p != 0` en su régimen acotado, `zeta_1 > 0`, la identidad exacta de
`Var(S_n)`, la separación asintótica en `fixed_n` ni la optimalidad del exponente `n^(-1/2)`.

## 3. Riesgos numéricos que la implementación deberá tratar explícitamente

1. **Densidad y score.** La implementación debe identificar dónde `c_tau`, las marginales o sus
   interpolaciones se acercan a cero; no se permiten divisiones silenciosas, recortes, sustitución
   de ceros ni extrapolación PCHIP fuera del dominio.
2. **Cancelación en Fisher/Hellinger.** Si `partial_tau` sigue aproximándose por diferencias
   finitas de Hellinger, se debe documentar la escala del cociente y controlar cancelación entre
   densidades próximas. Un valor estable al variar sólo `delta` no acredita estabilidad espacial.
3. **Inversión de cuantiles y raíz.** Toda inversión de `W_tau` y de marginales debe permanecer
   dentro del intervalo geométrico declarado; un fallo de `brentq`, monotonicidad o normalización
   es un fallo del cálculo, no un dato descartable.
4. **Extremos y supremo.** El máximo de puntos calculados es como mucho diagnóstico. La envolvente
   debe controlar también los subintervalos entre nodos de `tau`.

## 4. Dos refinamientos independientes

La implementación debe variar por separado, no simultáneamente, los siguientes ejes:

1. **Resolución espacial:** malla del rectángulo `(Utilde,v)`, cuadratura sobre `(x,y)` y, si se
   usan, tolerancias de la inversión de raíces/cuantiles. Deben reportarse como parámetros
   distintos; una pareja opaca `(N,M)` no basta para atribuir la deriva.
2. **Derivada en `tau`:** secuencia explícita de pasos simétricos `delta_j -> 0`, con valores a
   ambos lados dentro de `[1.0,1.2]` o una fórmula unilateral de borde declarada y validada. La
   malla espacial se mantiene fija durante este estudio.

Las estimaciones se etiquetarán `POINTWISE_NUMERICAL` hasta que ambos ejes satisfagan el criterio
predefinido de §5. No se permitirá compensar un eje inestable refinando el otro.

## 5. Criterio de convergencia predefinido

Antes de inspeccionar un resultado final, la implementación deberá declarar en su propio contrato:

- una escalera estrictamente creciente de resoluciones espaciales;
- una escalera estrictamente decreciente de pasos `delta`;
- una tolerancia relativa y una tolerancia absoluta para diferencias entre los dos últimos niveles
  de cada escalera;
- un mínimo de dos niveles de confirmación posteriores al primer nivel aparentemente estable;
- reglas fail-closed para `NaN`, `Inf`, densidad negativa, masa no unitaria, inversión fuera de
  dominio, pérdida de monotonía o error de raíz.

Las tolerancias numéricas concretas no quedan fijadas por este documento: deberán ser propuestas
antes de la primera ejecución, auditadas contra la precisión/tolerancias del método y congeladas
en el contrato ejecutable. No se eligen tras observar qué valor favorece el defeater.

## 6. Validación independiente mínima

Para al menos dos valores de `tau` —uno interior y uno extremo— se requiere una segunda ruta que
no reutilice simultáneamente la misma discretización y la misma interpolación de cuantiles. Puede
ser, por ejemplo, una parametrización alternativa de la integral de Fisher, diferenciación
automática/analítica del score si se deriva, o una cuadratura adaptativa independiente.

La concordancia se evalúa con las tolerancias congeladas de §5. Desacuerdo no se promedia ni se
resuelve escogiendo la ruta más favorable: activa un terminal de no convergencia.

## 7. Construcción de la envolvente de intervalo

La implementación deberá separar tres objetos:

```text
I_point(tau)              = estimación puntual convergida, si la hay
Ibar_mesh                 = max de los I_point en nodos
Ibar_envelope             = cota superior numérica/controlada sobre todo [1.0,1.2]
```

Sólo `Ibar_envelope` puede respaldar el lado uniforme de la Proposición 4. La envolvente deberá
incluir una cota explícita de variación entre nodos (por regularidad certificada del score, una
cota de derivada, o subdivisión adaptativa con criterio de intervalo); una malla uniforme sin tal
control termina en `POINTWISE_CONVERGED_ENVELOPE_UNRESOLVED`.

Para el defeater, una cota inferior puntual puede servir únicamente para demostrar que el lado
izquierdo es al menos el umbral; nunca para declarar una violación a partir de un máximo observado
insuficiente. Todo uso de este hecho deberá etiquetarse `NUMERICAL`, no `PROVED`.

## 8. Terminales fail-closed

La ejecución futura debe emitir exactamente uno:

```text
CONVERGED_POINTWISE_AND_ENVELOPE
POINTWISE_CONVERGED_ENVELOPE_UNRESOLVED
NUMERICAL_NONCONVERGENCE
DOMAIN_OR_SCORE_SINGULARITY
```

- `CONVERGED_POINTWISE_AND_ENVELOPE`: ambos refinamientos y la validación independiente pasan, y
  existe `Ibar_envelope` sobre el intervalo completo.
- `POINTWISE_CONVERGED_ENVELOPE_UNRESOLVED`: las evaluaciones puntuales pasan, pero falta control
  entre nodos; no permite declarar el defeater `PASS` ni `FAIL`.
- `NUMERICAL_NONCONVERGENCE`: cualquier deriva por encima del contrato, desacuerdo independiente o
  sensibilidad no decreciente; mantiene ambos estados de §2.
- `DOMAIN_OR_SCORE_SINGULARITY`: la geometría, densidad, score o inversión sale del dominio
  declarado; no se intenta reparación silenciosa.

## 9. Secuencia y frontera de autorización

```text
especificación de convergencia -> auditoría del diseño -> implementación -> ejecución acotada
```

Este documento sólo completa la primera fase. La auditoría del diseño debe comprobar, antes de
editar código, que las salidas, terminales, ausencia de artefactos de validación y separación entre
`I_point` e `Ibar_envelope` coinciden literalmente con este contrato. Implementación y ejecución
requieren autorizaciones posteriores y separadas del PI.

## 10. No hacer

- No añadir más mallas al integrador actual como sustituto del contrato.
- No usar el máximo de una cuadrícula como `Ibar`.
- No ajustar tolerancias, nodos o pasos tras ver el resultado para obtener `PASS` o `FAIL`.
- No abrir observables, `CANDIDATE_7`, estimadores, banco sellado, semillas ni umbrales.
- No elevar resultados numéricos a una cota probada ni a una conclusión sobre curvatura,
  localización, reconstrucción o 3+1D.
