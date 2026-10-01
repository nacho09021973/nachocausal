# Programa A de Relatividad — Gate M y taxonomía revisada

**Estado:** marco conceptual revisado tras `ATTACK_01`–`ATTACK_04`.

**Disciplina:** documento `dev/`; no es resultado confirmatorio, no ejecuta Gate M/S/U y no cambia
umbrales ni preregistraciones congeladas.

## 1. Alcance y ataques previos

La versión amplia anterior queda restringida por cuatro ataques analíticos:

- [ATTACK 01 — volumen normalizado](RELATIVIDAD_ATTACK_01_VOLUME_COUNTEREXAMPLE.md): las
  condiciones intrínseca + retardada + relabeling-invariant + sin embedding no fuerzan saturación;
  `chi=f(n/N_ref)` puede conservar profundidad timelike finita.
- [ATTACK 02 — trivialización lorentziana](RELATIVIDAD_ATTACK_02_LORENTZ_TRIVIALIZATION.md):
  `v_front -> c` puede ser la asintótica de una hipérbola timelike, sin universalidad dinámica.
- [ATTACK 03 — ambigüedad de escalado](RELATIVIDAD_ATTACK_03_SCALING_LIMIT_AMBIGUITY.md):
  `Delta -> 0` carece de interpretación sin camino de límite, escalas y normalización fijados.
- [ATTACK 04 — confusión frente/umbral](RELATIVIDAD_ATTACK_04_FRONT_THRESHOLD_CONFUSION.md):
  llegada a amplitud finita, soporte y frente no pueden identificarse sin un observable adicional
  que sobreviva a falsos positivos y negativos.

Consecuencia inmediata: no se permite usar “emergencia de la causalidad”, “hemos explicado `c`” ni
“velocidad universal” como lectura automática de una convergencia de pendientes o de umbrales.

## 2. Taxonomía canónica: cono cinemático y cono dinámico

### 2.1 Cono cinemático `K`

`K` es la estructura de lo permitido por la relación causal primitiva. En un causal set estándar,

```text
K = K_prec,
```

donde `prec` es input. `prec` no contiene metros ni segundos; tampoco fija por sí solo el número
`299792458 m/s`.

### 2.2 Cono dinámico `D`

`D` es la región o frontera alcanzada por una perturbación bajo una dinámica concreta. Las tres
relaciones posibles son:

```text
D ⊊ K    subsaturación;
D = K     saturación;
D ⊄ K     filtración/acausalidad.
```

Si la dinámica es estrictamente retardada respecto de `prec`, `D ⊄ K` queda excluida por
construcción. El problema no trivial es distinguir `D=K` de `D⊊K`.

Esto no debe llamarse “emergencia de la causalidad”: `K` ya estaba presente como primitiva.

## 3. Cuatro sentidos de emergencia

```text
E1  Emergencia del continuo:
    orden + número -> geometría u operador continuo aproximado.
    No es la tesis fuerte de este programa.

E2  Emergencia de un frente macroscópico:
    regla discreta -> frente o velocidad efectiva.
    Es débil y no implica geometría lorentziana emergente.

E3  Unicidad entre especies:
    microdinámicas genuinamente distintas -> una misma frontera macroscópica.
    Ocurre SOBRE un K dado y pertenece a la tesis de saturación.

E4  Emergencia de la estructura causal:
    K/prec no entra como primitiva; la relación causal se reconstruye después
    desde respuesta, susceptibilidad o soporte y se prueba que forma un orden
    localmente finito con límite lorentziano.
```

La expresión “emergencia de la causalidad” sólo está permitida para `E4`. `E4` es un proyecto
separado y queda bloqueado mientras `prec/K` sea input.

## 4. Tesis S — saturación

Dado `(C,prec)`, la pregunta admisible es si una clase amplia de dinámicas intrínsecas satisface,
en un camino de límite explícitamente fijado,

```text
partial D = partial K_prec.
```

La evidencia tendría que ser simultáneamente:

- no circular: la clase de dinámicas y el criterio se definen antes del resultado;
- isotrópica;
- robusta realización por realización, no sólo en promedio;
- válida para varias especies;
- obtenida de dinámicas no diseñadas para recuperar `Box`;
- evaluada con el camino de límite, escalas y normalizaciones preregistrados.

El claim máximo permitido bajo S es:

> Los campos no traen consigo su propio cono máximo; una clase de dinámicas satura un único borde
> perteneciente al orden.

No se permite elevarlo a:

```text
la causalidad emerge;
hemos explicado c.
```

`v_front -> v_prec` es, como máximo, evidencia auxiliar. La cantidad principal debe controlar una
profundidad causal/invariante y no sólo una pendiente coordenada. Además, “llegada al umbral” no se
identifica automáticamente con `partial D`; véase §6.

## 5. Tesis E — emergencia de `prec`

Es un proyecto separado y bloqueado. Esquemáticamente, una formulación futura podría estudiar

```text
x prec y  <=>  delta phi(y) / delta phi(x) != 0,
```

o una definición posterior más rigurosa basada en soporte o susceptibilidad. Sólo E permitiría
eventualmente afirmar que la estructura causal emerge de la respuesta.

## 6. Soporte, frente y llegada

Para una respuesta `chi(y,x)` hay que separar:

```text
soporte:                 chi(y,x) != 0;
frente:                  frontera física/matemática de propagación;
llegada a amplitud finita: T_dyn^(theta).
```

Los umbrales `theta={0.3,0.5,0.7}` pueden ser instrumentos de diagnóstico en Gate M, pero no son
por definición `partial D` en Tesis S. Un umbral puede:

- producir un falso negativo si una cola dominante alcanza `partial K` pero la amplitud principal
  está dentro;
- producir un falso positivo si una cola diminuta toca `partial K` mientras la respuesta relevante
  permanece dentro;
- cambiar de conclusión bajo reescalados monótonos de `chi` o normalizaciones equivalentes.

Por ello, antes de cualquier promoción, debe existir una definición de frente que sea intrínseca,
no idéntica al soporte retardado, independiente de un `theta` arbitrario, estable ante reescalado,
robusta ante sprinkling, realización por realización y compatible con los límites de ATTACK_02/03.
Si no aparece, la salida correcta es `STOPS_AS_FRONT_UNDEFINED`,
`STOPS_AS_THRESHOLD_DEPENDENT` o `STOPS_AS_SUPPORT_TAUTOLOGY`, según el fallo.

## 7. Jerarquía revisada de gates

### Gate M — MÉTODO

Pregunta única:

> ¿Existe un estimador intrínseco capaz de distinguir borde causal de interior causal y
> comportamiento anómalo?

Gate M valida una capacidad metodológica. Sus umbrales diagnósticos no constituyen por sí mismos
la Tesis S ni demuestran `partial D = partial K`.

### Tesis S — SATURACIÓN

Pregunta física adicional:

> ¿Una clase no trivial de dinámicas, no calibrada a `Box`, satura `K_prec` según un observable de
> frente no circular y un camino de límite especificado?

### E3 — UNICIDAD ENTRE ESPECIES

Pregunta dentro de S:

> ¿Es la misma frontera obtenida por especies o microdinámicas genuinamente diferentes?

E3 no crea `K`; estudia universalidad dinámica sobre el cono ya dado.

### E4 — EMERGENCIA CAUSAL

Proyecto independiente. Cerrado mientras `prec/K` sea una primitiva.

## 8. Taxonomía anterior: trazabilidad

La taxonomía A/B y el antiguo “Gate U” no se borran conceptualmente, pero quedan:

```text
STATUS = SUPERSEDED / DEPRECATED
```

La sustitución es semántica y explícita:

| Elemento antiguo | Destino revisado |
|---|---|
| Universalidad entre especies | `E3`, como subpregunta de `S`. |
| Gate U como nivel lógico independiente | Deprecated; no aparece en la jerarquía canónica. |
| Atractor RG | Posible mecanismo para explicar `S` o `E3`, no una tesis causal `E4`. |
| “Emergencia de causalidad” con `prec` dado | Claim inválido; sólo `E4` conserva ese nombre. |

Contenido histórico bajo A/B o U debe conservarse con sus referencias, pero no puede presentarse
como estado lógico vigente sin esta etiqueta.

## 9. Malentendido sobre `c`

No se identifica el valor escalar `c` con el resultado del programa. `prec` no contiene unidades
de metros ni segundos. Lo que podría resultar universal es una clase o frontera nula perteneciente
al orden; el número dimensional `299792458 m/s` requiere una convención física de unidades y no es
un output de S.

## 10. Regla de decisión actual

```text
GATE_M  = método; no equivale a saturación.
S       = saturación sobre K_prec; pendiente sola insuficiente.
E3      = unicidad entre especies dentro de S.
E4      = emergencia de prec; bloqueada.
```

Tras ATTACK_01–03, la versión amplia de S está falsada. ATTACK_04 debe decidir además si existe un
observable de frente no circular. Hasta entonces, no se autoriza cálculo caro ni se puede afirmar
saturación universal.

**No se ejecuta ningún gate en este documento.**
