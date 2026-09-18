# Experimento Presente

## Idea

El workflow actual de ladders en este repo parte de un `start` de borde y avanza
hacia el futuro. Eso sesga la pregunta física hacia una estructura "sin pasado"
efectivo. Este experimento propone otra geometría:

- fijar un único evento `p` como `PRESENT_ANCHOR`;
- estudiar `C^-(p)` como cono pasado;
- estudiar `C^+(p)` como cono futuro;
- y medir si el entorno causal de `p` actúa como cuello, simetría rota, retorno
  o transición geométrica entre ambos conos.

La pregunta deja de ser solo "cuándo se despega una ladder sembrada en el
borde" y pasa a ser:

> Dado un punto-presente `p`, ¿la estructura causal alrededor de `p` muestra
> simetría, ruptura, retorno o límite geométrico al comparar el cono pasado y
> el cono futuro, sin privilegiar starts de frontera?

## Motivación

La motivación es distinguir entre:

1. un artefacto de borde:
   - el `start` nace en una zona con poco pasado disponible;
   - la ladder se prolonga solo en una dirección;
   - el peel-off puede estar condicionado por esa asimetría.

2. una estructura causal más intrínseca:
   - un presente con pasado y futuro disponibles;
   - continuidad causal bilateral;
   - confluencia de muchas historias compatibles en un mismo núcleo;
   - divergencia de muchos futuros compatibles desde ese mismo núcleo.

En lenguaje intuitivo: no mirar una rama que arranca "desde nada", sino un
evento donde "muchos pasados llegan" y "muchos futuros salen".

## Cambio de observable

Este experimento no es una pequeña variante del diagnóstico de `ladder
braiding`; define otro observable.

### Observable actual

- se elige una rung inicial `(sp, sq)` cerca de una frontera minimal;
- se construyen ladders hacia el futuro;
- se pregunta por adherencia, peel-off y branching futuro.

### Observable propuesto

- se elige un único `presente` `p`;
- se comparan `C^-(p)` y `C^+(p)`;
- se construyen extensiones compatibles hacia el pasado y hacia el futuro;
- se mide la asimetría, retorno, profundidad y estabilidad bilateral alrededor
  de `p`.

## Definición tentativa de presente

La definición primaria debe ser puntual, no espacial.

### Definición primaria — presente puntual

Elegir un evento `p` y estudiar:

- `C^-(p) = {x : x ≺ p}`
- `C^+(p) = {y : p ≺ y}`
- número de chains compatibles que llegan a `p`
- número de chains compatibles que salen de `p`

Ventaja:
- simple.
- evita introducir una foliación disfrazada.

Riesgo:
- demasiado sensible a ruido local de sprinkling.

Interpretación prohibida:

- no tratar el presente como slice espacial;
- no tratarlo como antichain engrosada;
- no tratarlo como banda;
- no tratarlo como hipersuperficie;
- salvo que eso se declare después como variante diagnóstica separada.

### Variante diagnóstica B — presente como rung

Elegir una rung `(p, q)` como núcleo presente, análoga a una seed rung, pero no
de borde:

- muchas estructuras pasadas deben poder extenderse hasta `(p, q)`;
- muchas estructuras futuras deben poder salir de `(p, q)`.

Ventaja:
- está más cerca del lenguaje actual de ladders.

Riesgo:
- sigue heredando parte de la gramática ladder.

### Variante diagnóstica C — presente como pequeño diamante / núcleo

Elegir un pequeño subposet `P` como presente:

- varios caminos causales llegan a `P`;
- varios caminos causales salen de `P`;
- la estructura se mide respecto a ese núcleo, no a un solo evento.

Ventaja:
- más robusto.

Riesgo:
- más costoso y más ambiguo de definir.

## Variables interesantes

Para un presente puntual `p`, medir:

- `past_crossing_fraction`;
- `future_crossing_fraction`;
- `past_return_fraction`;
- `future_return_fraction`;
- `past_future_asymmetry`;
- `cone_depth_dependence`;
- tamaño de `C^-(p)` y de `C^+(p)`;
- número de chains largas que llegan a `p`;
- número de chains largas que salen de `p`;
- anchura de branching al pasado y al futuro.

Cautela:

- comparación bilateral no significa esperar igualdad numérica exacta entre
  pasado y futuro;
- puede haber asimetría física o artefactual por horizonte, borde finito,
  orientación temporal o ventana de sprinkling;
- por eso `past_future_asymmetry` debe medirse, no suponerse nula.

## Hipótesis cualitativas

### Hipótesis H1 — artefacto de borde

Si el fenómeno actual depende mucho del hecho de partir de borde, entonces al
anclar un punto presente con conos pasado/futuro disponibles debería cambiar la
dinámica:

- puede disminuir el peel-off aparente;
- puede aparecer más coherencia de ladders;
- puede cambiar la profundidad típica del despegue;
- puede emerger estructura bilateral que el experimento actual no puede ver.

### Hipótesis H2 — estructura intrínseca

Si el causal set contiene verdaderos "cuellos" estructurales, deberían aparecer
eventos `p` donde:

- muchas historias pasadas compatibles convergen;
- muchos futuros compatibles divergen;
- el presente actúa como pivote causal;
- y esa centralidad no depende solo de estar cerca de una frontera.

### Hipótesis H3 — no hay presente especial

También es posible que no aparezca nada especial:

- los candidatos a presente no muestren más coherencia que un nodo típico;
- la estructura bilateral sea tan ruidosa como la unilateral;
- y el comportamiento observado hasta ahora siga siendo una propiedad general
  del orden, no de un presente privilegiado.

## Qué cambiaría respecto al experimento actual

No basta con cambiar un parámetro. Habría que cambiar al menos:

1. la selección del ancla:
   - de `start` de frontera a evento `p` interior;

2. la dirección de exploración:
   - de solo futuro a `C^-(p)` + `C^+(p)`;

3. el criterio de interés:
   - de adherencia/peel-off unilateral
   - a confluencia/divergencia bilateral.

## Riesgos conceptuales

### Riesgo 1 — redefinir demasiado

El "presente" puede volver a inflarse desde evento a pseudo-superficie y perder
falsabilidad.

### Riesgo 2 — confundir centralidad con física

Un nodo con gran conectividad o gran número de chains no implica por sí mismo un
observable físico profundo.

### Riesgo 3 — sobrecontar combinatoria

En causal sets, el número de extensiones puede crecer muy rápido. Habría que
distinguir:

- multiplicidad puramente combinatoria;
- frente a concentración estructural genuina.

### Riesgo 4 — volver a introducir información de embedding sin querer

Si el presente se define usando coordenadas ocultas, el experimento pierde valor
order-only.

La distinción correcta es:

- `GEOMETRY_ASSISTED`: `p` elegido con ayuda de embedding/coordenadas;
- `ORDER_ONLY`: `p` elegido solo con criterios internos del orden.

La primera opción puede servir como control exploratorio. La segunda es la que
empieza a tocar la tesis fuerte de recuperabilidad intrínseca.

## Diseño mínimo razonable

Un diseño sobrio sería:

1. elegir candidatos `p` solo con información causal;
2. medir para cada candidato:
   - número de extensiones en `C^-(p)`,
   - número de extensiones en `C^+(p)`,
   - asimetría pasado/futuro,
   - estabilidad de las familias que atraviesan `p`;
3. comparar esos candidatos con starts de borde;
4. decidir si el comportamiento bilateral cambia de forma cualitativa.

## Qué podría significar un resultado positivo

Un resultado exploratorio positivo sería:

- existe una familia de presentes con fuerte confluencia pasada y fuerte
  divergencia futura;
- esa familia no es reducible a mero artefacto de borde;
- y la estructura bilateral es más estable que la unilateral actual.

Eso no probaría un horizonte, ni 3+1D, ni una afirmación física fuerte. Pero sí
justificaría abrir una nueva línea experimental dentro del repo.

## Qué NO significaría

No significaría automáticamente:

- reconstrucción de horizonte;
- observable público listo para Paper I;
- prueba de defecto físico;
- prueba de un presente objetivo en sentido fuerte;
- claim de relatividad o cosmología emergente.

## Veredicto provisional

La idea es físicamente interesante porque ataca una limitación real del workflow
actual: partir desde un borde sin pasado efectivo. En términos de causal set,
puede revelar una estructura bilateral que ahora está oculta.

La interpretación prudente es:

- no es una extensión menor de `ladder braiding`;
- es un experimento nuevo;
- y su primera misión sería discriminar artefacto de borde frente a estructura
  causal más intrínseca.
