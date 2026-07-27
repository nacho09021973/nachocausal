# WP4 — Contrato ejecutable previo a implementación de `Ibar`

**Estado:** `CONTRACT_ONLY / IMPLEMENTATION_AUTHORIZATION = NOT_GRANTED /
EXECUTION_AUTHORIZATION = NOT_GRANTED`.

Este contrato hace ejecutable el diseño auditado
`wp4_ibar_interval_numerical_design.md`. Fija parámetros, decisiones y abstenciones **antes** de
editar `wp4_kappa_numeric_reference.py` o ejecutar cualquier cuadratura. No es autorización para
ninguna de las dos cosas, no modifica etiquetas científicas y no evalúa `I(tau)` ni `Ibar`.

## 1. Objeto congelado

```text
r_p = 3.0; r_q = 0.5; v_p = 0.0; v_q = 0.02
tau interval = [1.0, 1.2]
I(tau) = integral_[0,1]^2 (partial_tau log c_tau(x,y))^2 c_tau(x,y) dx dy
Ibar = sup_{tau in [1.0,1.2]} I(tau)
```

La medida es exactamente la cópula de la medida de volumen normalizada, respecto de `dx dy` en
`[0,1]^2`; el volumen EF original es `dv dr`. La definición, cambio de variables y razones para no
identificar un máximo de malla con `Ibar` son los del diseño auditado §§1 y 7.

Los únicos estados de partida son:

```text
IBAR_DIAMOND_INTERVAL = INCONCLUSIVE_NUMERICAL_NONCONVERGENCE
CONSTANT_LEVEL_DEFEATER = NOT_EVALUATED_IBAR_UNAVAILABLE
```

Ningún resultado de este contrato permite cambiar esos estados sin la autorización y auditoría
posteriores que correspondan.

## 2. Implementación que este contrato eventualmente permitirá

La ruta primaria será una sustitución explícita y versionada del integrador de referencia:

1. raíz `r_tau(Utilde,v)` con `brentq`, tolerancias `xtol=rtol=1e-12` y bracket geométrico
   comprobado en cada llamada;
2. malla uniforme separada en `Utilde` y `v`, integración trapezoidal de marginales y de masa;
3. cuantiles mediante PCHIP monótono dentro de soporte; sin extrapolación;
4. cuadratura de punto medio independiente sobre `[0,1]^2` para `H^2`;
5. `I` de interior por diferencia Hellinger simétrica y de borde por diferencia unilateral, según
   §4.

No se permite cambiar el algoritmo, los niveles, tolerancias, nodos, reglas de borde o criterios
de abajo sin un **nuevo** contrato y una nueva auditoría. Un parámetro no listado es un error de
contrato, no una libertad de implementación.

## 3. Mallas y tolerancias congeladas

Para cada `tau` que haya de ser aceptado, la ruta primaria ejecutará estos cuatro niveles
espaciales, completos y en este orden:

| Nivel | nodos `Utilde` | nodos `v` | nodos de Hellinger `x` | nodos `y` |
| --- | ---: | ---: | ---: | ---: |
| S1 | 160 | 160 | 32 | 32 |
| S2 | 240 | 240 | 48 | 48 |
| S3 | 360 | 360 | 72 | 72 |
| S4 | 540 | 540 | 108 | 108 |

Las dos direcciones espaciales y las dos de cópula se registrarán por separado aunque se usen los
valores simétricos de esta tabla. La inversión de cuantiles, la raíz, la normalización, las
marginales y la densidad se verifican en cada nivel. Se rechaza el nivel si ocurre `NaN`, `Inf`,
densidad negativa inferior a `-1e-13`, masa o CDF final fuera de `1` por más de `1e-10`,
monotonía no estricta donde se exige inversa, salida del bracket, o extrapolación.

Para dos aproximaciones finitas `a,b`, se define una diferencia aceptable si

```text
abs(a-b) <= A_POINT + R_POINT * max(abs(a), abs(b))
A_POINT = 1e-8
R_POINT = 1e-2
```

No se redondean valores antes de aplicar esta condición.

## 4. Escalera de derivada y bordes

La escalera completa e inalterable es

```text
D = (0.04, 0.02, 0.01, 0.005, 0.0025).
```

Para `tau` con ambos desplazamientos dentro del intervalo se emplea

```text
I_sym(tau; d) = 4 H^2(c_(tau-d/2), c_(tau+d/2)) / d^2.
```

En `tau=1.0` se emplea solamente

```text
I_plus(1.0; d) = 4 H^2(c_1.0, c_(1.0+d)) / d^2,
```

y en `tau=1.2` solamente

```text
I_minus(1.2; d) = 4 H^2(c_(1.2-d), c_1.2) / d^2.
```

La misma fórmula unilateral se usará para cualquier nodo que no admita la simétrica. No se mezcla
una estimación unilateral con una simétrica al verificar convergencia de un mismo nodo. La malla
espacial se mantiene en `S4` durante esta escalera; la escalera `D` no se modifica tras
inspeccionar resultados.

## 5. Regla de convergencia puntual y de parada

Un nodo `tau` obtiene `POINTWISE_NUMERICAL` sólo si se cumplen **todas** estas condiciones:

1. para `d=0.01`, los tres pares espaciales consecutivos `(S1,S2)`, `(S2,S3)` y `(S3,S4)` son
   aceptables bajo §3;
2. con `S4`, los cuatro pares consecutivos de la escalera `D` son aceptables bajo §3;
3. las dos últimas confirmaciones espaciales `(S2,S3)` y `(S3,S4)` y las dos últimas de derivada
   `(0.01,0.005)` y `(0.005,0.0025)` son aceptables; y
4. no ocurre ninguna condición fail-closed de §3 ni desacuerdo de §6.

La estimación reportable del nodo es la de `S4,d=0.0025`; los niveles previos y sus diferencias
se conservan como trazabilidad. Si un nodo falla, no se aumenta S4, no se inserta un paso menor y
no se ajusta una tolerancia: se emite el terminal que corresponda en §8 y se detiene la ejecución
acotada.

## 6. Validación independiente congelada

La segunda ruta se aplicará obligatoriamente a `tau=1.0` y `tau=1.1`:

- integración adaptativa de Gauss--Kronrod anidada en `(x,y)` para la integral Hellinger, con
  tolerancias absolutas y relativas de integración `1e-10` y `1e-8` respectivamente;
- inversión de cuantiles por resolución de la CDF acumulada mediante bracket y raíz en cada
  abscisa adaptativa, sin PCHIP ni reutilización de la malla uniforme primaria;
- misma definición Hellinger y misma escalera `D`, incluida la fórmula unilateral en `tau=1.0`.

Cada valor independiente debe satisfacer internamente las condiciones de §5 sustituyendo su error
de cuadratura certificado por la diferencia espacial. Después, su valor final y el de la ruta
primaria `S4,d=0.0025` deben satisfacer

```text
abs(I_primary - I_independent)
  <= 2*A_POINT + 2*R_POINT*max(abs(I_primary), abs(I_independent)).
```

No se promedian rutas. Desacuerdo, integración no certificada o pérdida de bracket dispara
`NUMERICAL_NONCONVERGENCE` o `DOMAIN_OR_SCORE_SINGULARITY`, según §8.

## 7. Certificación de `Ibar`: envolvente, no máximo de malla

La malla de cobertura de `tau` queda fijada en 161 nodos

```text
T = {1.0 + j/800 : j=0,...,160},
```

es decir, 160 celdas cerradas de anchura `h_tau=0.00125`. Se exige `POINTWISE_NUMERICAL` en todos
los nodos de `T`; un único nodo no convergido impide toda envolvente.

Para cada celda `J_j=[tau_j,tau_(j+1)]`, un módulo separado de aritmética de intervalos con
redondeo dirigido debe devolver una cota superior verificable `U_j` de la integral Fisher en toda
la celda. Debe encerrar conjuntamente el intervalo de `tau`, las raíces, marginales, cuantiles,
score e integración; no puede reutilizar como certificación valores puntuales, PCHIP ni derivadas
muestreadas. Si el enclosure no logra demostrar una raíz única, positividad/normalización o cota
finita, falla cerrado.

Se fija

```text
Ibar_envelope = max_j U_j.
E_ENVELOPE_ABS = 1e-7
E_ENVELOPE_REL = 1e-2
```

La envolvente se acepta sólo si también se obtiene una cota inferior certificada `L=max_j L_j` y

```text
Ibar_envelope - L <= E_ENVELOPE_ABS + E_ENVELOPE_REL * max(abs(Ibar_envelope), abs(L)).
```

`Ibar_mesh=max_{tau in T} I_point(tau)` queda siempre separado y no puede sustituir
`Ibar_envelope`. Una cota inferior puntual nunca puede declarar una violación del defeater.

## 8. Terminales y abstenciones

La futura ejecución emite exactamente uno de estos terminales:

```text
CONVERGED_POINTWISE_AND_ENVELOPE
POINTWISE_CONVERGED_ENVELOPE_UNRESOLVED
NUMERICAL_NONCONVERGENCE
DOMAIN_OR_SCORE_SINGULARITY
```

- `CONVERGED_POINTWISE_AND_ENVELOPE`: §5 pasa en los 161 nodos, §6 concuerda y §7 produce el
  enclosure superior e inferior requerido.
- `POINTWISE_CONVERGED_ENVELOPE_UNRESOLVED`: §5 y §6 pasan donde aplican, pero §7 no produce una
  envolvente certificada. Prohíbe `PASS` y `FAIL` del defeater.
- `NUMERICAL_NONCONVERGENCE`: falla una comparación de §5, la validación independiente discrepa o
  el error/enclosure no alcanza sus tolerancias sin una singularidad de dominio identificada.
- `DOMAIN_OR_SCORE_SINGULARITY`: falla cualquier condición geométrica, de raíz, masa, CDF,
  positividad, cuantiles o finitud de score exigida por §§2--3 o §7.

En los últimos tres terminales permanecen literalmente:

```text
IBAR_DIAMOND_INTERVAL = INCONCLUSIVE_NUMERICAL_NONCONVERGENCE
CONSTANT_LEVEL_DEFEATER = NOT_EVALUATED_IBAR_UNAVAILABLE
```

Incluso el primer terminal no autoriza por sí solo cambiar etiquetas científicas, publicar `n*`, ni
declarar el defeater: requiere auditoría de la ejecución y una instrucción posterior del PI.

## 9. Frontera de este documento

Antes de editar código, este contrato requiere una auditoría precommit propia que compruebe su
literalidad, las tolerancias, la independencia efectiva de §6, la corrección de las fórmulas de
borde y el carácter certificador de §7. Sólo después de un resultado documental aceptado podrá el
PI decidir separadamente si concede `IMPLEMENTATION_AUTHORIZATION`. Ninguna frase de este contrato
concede `EXECUTION_AUTHORIZATION`.
