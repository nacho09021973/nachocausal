# Acta — frente 2+1D ecuatorial: banco de localización del horizonte a partir del orden

> **STATUS: `DRAFT_FOR_PI_SIGNATURE`.** Propone abrir un frente. **No** fija umbrales, semillas
> ni estimador: eso lo hará un preregistro (prereg-004) después de la exploración en `dev`, como
> en 1+1D. Nada de §4 en adelante se ejecuta sin la firma de §9.

**Fecha:** 2026-10-12 · **Propuesto por:** el PI («creo que habría que ir a 1+2D») ·
**Base técnica:** el lema E1
(`research_program/puente_3p1/2026-10-12/E1_equatorial_restriction_lemma.md`).

---

## 1. Por qué

- **El objetivo es 3+1D** (README, objetivo 1). El puente 3+1D se ha quedado en la pregunta de
  identificabilidad, sin ningún estimador:
  - `n=2` es ciega a una dirección en la que el horizonte se mueve (B3, promocionado);
  - `n=3` sigue sin resolver por falta de resolución (B4-R, `8fb3b17`).
- **Lo que falta para «encontrar el horizonte» es un estimador con `N` finito** que funcione
  fuera de 1+1D. En 1+1D existe (prereg-002, `PASS`) y en 3+1D no. Simular conjuntos causales
  en 3+1D con densidad suficiente es caro.
- **2+1D ecuatorial es el paso intermedio natural.** Por E1, su orden causal es el de
  Schwarzschild 3+1D en el ecuador, con el mismo núcleo `Delta_max` ya certificado. Simular es
  mucho más barato que en 3+1D, y lo que funcione aquí se puede llevar a 3+1D cambiando solo la
  medida y la ley angular.

**No es un sustituto de 3+1D.** El frente se justifica solo como banco intermedio
(README, objetivo 3: cerrar unidades verificables antes de ampliar).

## 2. Objeto

- **Variedad:** el ecuador de Schwarzschild, `(E, g_E)` con `g_E = −C(UV) dU dV + r² dφ²`
  (E1 §1). **No** es una solución de Einstein en 2+1D. Es un banco de geometría causal cuyo
  orden coincide con el de 3+1D en el ecuador (E1 §4).
- **Región sembrada:** un parche `K × S¹` que cruza el horizonte `U = 0`, de la familia del
  puente. Qué parche o parches, su tamaño y la escala se fijan en la exploración y se congelan
  en prereg-004.
- **Sembrado:** Poisson con densidad proporcional a la medida `∝ r C dU dV dφ`, es decir, con
  peso `e^{−s}` (E1 §3).
- **Orden:** la regla de E1 §3 para parches rectangulares. Cuando `ΔU, ΔV > 0`,
  `x ≺ y ⟺ dist_φ(x, y) <= Delta_max(x, y)`, con el `Delta_max` de B1.2. Si `ΔU = 0` o
  `ΔV = 0`, `x ≺ y` solo cuando `dist_φ = 0`. Sale del generador, nunca del estimador.
- **Verdad de referencia:** el horizonte `r = 2M`, que en el parche es `U = 0`. Solo puntúa; no
  define ni guía el observable (regla fundacional del CLAUDE.md).

## 3. Lo que se quiere poder afirmar al final (forma, no umbrales)

Lo mismo que prereg-002, pero en 2+1D. Un estimador **ciego a la inmersión**, que ve solo la
clase de isomorfismo del poset y sus cardinalidades (Order + Number, CLAUDE.md), localiza el
horizonte dentro de un umbral de principio, con criterios de:
- significación;
- localización;
- estabilidad;
- falsos positivos;
- un guardia «order-only».

Los evalúa una sola ejecución ciega con semillas vírgenes. El alcance es la localización en un
parche finito en 2+1D ecuatorial: no hay horizonte global, ni 3+1D, ni reconstrucción.

## 4. Fases

**Fase A — generador (dev).** Sembrado más cálculo del orden.
- El riesgo principal es el coste: `Delta_max` exige un `sup` por cada par, y hay del orden de
  `N²/2` pares.
- Opciones a explorar: disparo de geodésicas nulas, la calibración de la compuerta como cota
  superior y la recta como inferior para decidir pronto los pares claros, y GPU (solo en `dev`,
  regla del 2026-06-20).
- **Control obligatorio:** en los pares que el generador decide, su orden coincide con el de
  las cotas certificadas.
- **Parada:** si con `N = 10⁴` el generador no baja de una hora por realización, se informa y
  se para.

**Fase B — estimador (dev).**
- Se parte del estimador-v2 de 1+1D (observable VOLUME `|future(i)|`, puerta `τ(n)` de
  abstención y puerta de dominio) y se adapta a 2+1D.
- Solo se usan semillas de exploración de una banda nueva reservada para 2+1D, disjunta de
  todas las anteriores.
- Las cardinalidades son observables legítimas. Lo que se vigila es la dependencia inducida por
  la selección, no el hecho de contar (CLAUDE.md).

**Fase C — preregistro (prereg-004).** Se congelan:
- la geometría y los parches;
- las intensidades;
- el estimador sellado;
- los umbrales anclados a bases de principio, como `θ_loc = 2ℓ_λ/(2M)` en 1+1D;
- las semillas vírgenes, sorteadas una sola vez.

El sello se hace por SHA256, como en prereg-002.

**Fase D — una sola ejecución ciega**, con autorización explícita. Su resultado se publica sea
cual sea: `PASS`, `FAIL`, `INCONCLUSIVE` u `OUT_OF_DOMAIN`.

## 5. Separación dev / validación

- Bandas de semillas nuevas y disjuntas: exploración en una, validación virgen en otra. Se
  definen en la fase B y se protegen con un guardia que se puede ejecutar, como en
  `thresholds.py`.
- La exploración no toca los umbrales sellados ni ve las semillas de validación.
- La GPU solo se usa en `dev`. La ejecución ciega es en CPU y reproducible bit a bit.

## 6. Guardarraíles

```text
order_only_estimator (ve solo el poset + cardinalidades), ground_truth_only_scores,
no_threshold_tuning_after_seal, single_blind_run, report_alike,
no_3p1_claim_from_2p1, no_einstein_2p1_claim, gpu_dev_only
```

## 7. Lo que el frente NO hace

- No reabre B4 ni cambia ningún resultado del puente 3+1D.
- No afirma nada de 3+1D a partir de 2+1D. Trasladar un estimador a 3+1D sería otro frente.
- No usa BTZ. Si se quisiera un agujero negro 2+1D auténtico, iría en un acta aparte.

## 8. Coste y presupuesto

- **Fase A:** de una a dos jornadas, con la parada de §4.
- **Fase B:** abierta, y es la fase de riesgo científico.
- **Fases C y D:** como prereg-002.

Antes de cerrar la fase C conviene un `/comite`, como se hizo con prereg-002.

## 9. Firma del PI

1. Abrir el frente 2+1D ecuatorial con el alcance de §1–§3. `[SÍ / NO]`
2. Fase A (generador) autorizada, con su parada. `[SÍ / NO]`
3. Las fases B, C y D se firman cuando lleguen. `[se firma después]`

```text
PI: ____________________          fecha: __________
```
