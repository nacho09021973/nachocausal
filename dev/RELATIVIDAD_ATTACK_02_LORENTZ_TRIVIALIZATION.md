# Relatividad — ATTACK 02: trivialización lorentziana

**Objetivo:** determinar si `v_front -> v_prec` puede ser una consecuencia cinemática de la
invariancia lorentziana, sin universalidad de la dinámica.

**Estado:** ataque analítico; sin simulación, sin búsqueda, sin ajuste y sin cambio de Gate.

## 1. Claim atacado

La interpretación fuerte bajo ataque es:

```text
v_front -> v_prec
    ==> la dinámica relacional universaliza o satura la propagación causal.
```

El ataque pregunta si la misma observación puede aparecer para respuestas dinámicamente distintas
por la forma asintótica de una órbita timelike lorentziana.

## 2. Familia mínima

Consideremos cualquier respuesta escalar retardada cuyo límite continuo tenga la forma

```text
chi_lambda(y,x) = F_lambda(tau(x,y)),
```

donde `tau` es el intervalo propio y `F_lambda` puede depender de la especie o de parámetros
dinámicos `lambda`. No se supone que la respuesta sea KG, BD, solución de una ecuación concreta ni
que comparta la misma escala con otra especie.

Para un umbral `theta`, supóngase que existe una solución regular

```text
F_lambda(tau_lambda,theta) = theta,
0 < tau_lambda,theta < infinity.
```

La superficie de nivel es entonces

```text
t^2-r^2 = tau_lambda,theta^2.
```

## 3. Velocidad coordenada

Parametrizando la superficie por `r`,

```text
t(r) = sqrt(r^2 + tau_lambda,theta^2),
dr/dt = r/t = r/sqrt(r^2+tau_lambda,theta^2).
```

Por tanto,

```text
dr/dt -> 1  as r -> infinity
```

para todo `0<tau_lambda,theta<infinity`. En particular, dos especies pueden satisfacer

```text
tau_phi,theta != tau_psi,theta,
v_front^phi -> c,
v_front^psi -> c,
```

sin que sus respuestas dinámicas se aproximen entre sí ni que exista un atractor dinámico común.

La diferencia finita queda visible en la profundidad invariante, aunque desaparece de la pendiente
coordenada:

```text
Delta_tau = |tau_phi,theta - tau_psi,theta| > 0,
lim_(r->infinity) (v_phi(r)-v_psi(r)) = 0.
```

Más precisamente,

```text
1 - v_front(r) = tau_lambda,theta^2/(2 r^2) + O(r^-4),
```

de modo que la velocidad sólo conserva la profundidad en términos subdominantes.

## 4. La órbita de un solo vector ya basta

Un vector timelike de norma propia `tau` tiene órbita lorentziana

```text
(t,r) = (tau cosh(zeta), tau sinh(zeta)).
```

Su rapidez coordenada es

```text
r/t = tanh(zeta) -> 1  as zeta -> infinity.
```

Así, una medición basada únicamente en “la máxima velocidad observada a grandes distancias” puede
recuperar `c` por simetría lorentziana, incluso si la escala propia `tau` permanece estrictamente
positiva y depende de la especie.

## 5. Resultado adversarial

El argumento rompe la inferencia dinámica:

```text
ADVERSARIAL_RESULT = PASS
CLAIM_UNDER_ATTACK  = FAIL
```

en el sentido siguiente:

```text
v_front -> v_prec
```

no es evidencia suficiente de universalidad dinámica ni de saturación causal. Puede ser sólo la
asintoticidad de una hipérbola timelike al cono nulo en coordenadas de un observador.

El resultado no demuestra que toda respuesta lorentziana tenga `tau>0`, ni que el causal set
realice exactamente esta familia a cardinalidad finita. Basta una familia continua admisible para
invalidar la interpretación universal de la observación de velocidad.

## 6. Reparación mínima de Gate S

El observable primario no debe ser sólo una pendiente. Debe incluir una cantidad de profundidad
causal invariante, por ejemplo una escala propia del nivel:

```text
tau_front(lambda,theta;L),
```

o una versión adimensional fijada por una escala de referencia independiente. La condición fuerte
que no queda trivializada por este ataque es del tipo

```text
tau_front(lambda,theta;L) -> 0
```

en el límite declarado, junto con una especificación de qué se mantiene fijo. La convergencia de
`v_front` a `v_prec` puede mantenerse como observable auxiliar, pero no como criterio de
saturación.

Una prueba futura debe reportar conjuntamente:

```text
coordinate-slope convergence,
invariant-depth convergence,
species dependence,
limit path.
```

Si sólo se observa el primer renglón, el resultado debe clasificarse como compatible con
`LORENTZIAN_KINEMATIC_TRIVIALIZATION`.

## 7. Decisión

Gate S no puede sostener la afirmación “velocidad universal” a partir de `v_front -> v_prec` sola.
Debe reformularse, como mínimo, en términos de colapso de profundidad causal invariante y superar
el ataque de escalado de `ATTACK_03`.

**No se ejecutan Gate M, Gate S ni Gate U en este documento.**
