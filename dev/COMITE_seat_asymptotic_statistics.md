# Comité — especificación de asiento nuevo: "Estadístico asintótico de órdenes aleatorios" (dev, NO convoca)

> Charge document. Define el asiento que falta en el panel de 6 roles para poder deliberar el problema de
> identificabilidad de `dev/MEMO_random_orders_identifiability.md` (§5: clasificación de `P_n, Q_n`). **No
> lanza `/comite`, no congela, no commitea.** Es el paso "definir el asiento primero" antes de convocar.
> Procedencia: `make verify-seal` = `6e2c3888…` (sin código sellado tocado).

## Por qué un asiento nuevo

El panel actual tiene 6 asientos: reproducibility engineer, **mathematician (causal-sets)**, physicist,
falsifier, prereg warden, literature verifier (`docs/comite/comite_decision_004…md:56-141`). Ninguno cubre
la competencia central del problema: **estadística asintótica de la distinguibilidad de dos leyes de
órdenes aleatorios** (Le Cam: separación / contigüidad mutua / contigüidad unilateral; maquinaria de
likelihood-ratio sobre estructuras **transitivas y dependientes**, no aristas independientes). El asiento
de matemático de causal-sets está cerca del rol "formulación de las leyes sobre posets" (Brightwell), pero
no del rol "probar separación/contigüidad" (Kleijn/Rizzelli). Se añade el segundo y se re-mandata el
primero.

## Asiento A7 — "Estadístico asintótico de órdenes aleatorios" (rol Kleijn/Rizzelli)

- **Mandato (único):** dadas formalmente `P_n, Q_n` (leyes sobre clases de isomorfismo del suborden
  observable, memo §2), **clasificar su relación asintótica** en uno de los cuatro casos del memo §5
  (separación TV→1 / contigüidad mutua / contigüidad unilateral / complemento residual), con
  justificación verificable.
- **Salida (token de veredicto):** exactamente uno de
  `{SEPARABLE, MUTUAL_CONTIGUOUS, ONE_SIDED_CONTIGUOUS, RESIDUAL, UNDECIDED_NEEDS_<X>}`, donde `<X>` nombra
  la pieza analítica concreta que falta (cota de KL/Hellinger, segundo momento del LR, construcción de
  `A_n`, etc.). No puede devolver "parcialmente" sin nombrar `<X>`.
- **Herramientas admisibles:** método de dos puntos / Le Cam; Bretagnolle–Huber; segundo momento del
  likelihood-ratio; control tipo Lindeberg de log-LR; cotas TV / Hellinger / KL; para el caso compuesto,
  separación uniforme/minimax (`inf/sup` sobre la familia adversarial de bordes).
- **Límites de alcance (lo que NO hace):**
  - NO diseña estimadores ni scores nuevos (eso sería volver a OBS — el problema es de clasificación de
    leyes, no de construcción de instrumento).
  - NO toca el estimador sellado, NO puntúa contra `r`/`r_S`, NO mira `RESERVED_002`.
  - NO juzga buena-definición física de `H_trap`/`H_no-trap` (asiento físico, abajo).
  - Trabaja **analíticamente**: encaja en el protocolo blind de dos olas sin mirar datos.
- **Condiciones de ABSTENCIÓN explícitas:** si las leyes no están bien definidas; si no se ha fijado
  simple-vs-compuesto (memo §5 caveat); si la σ-álgebra observable no está especificada (suborden completo
  vs ventanas de radio acotado).

## Re-mandato del asiento de matemático (causal-sets) — rol "formulación" (Brightwell)

- **Encargo añadido:** fijar el **espacio muestral** (clases de iso de subórdenes no etiquetados vs
  vecindades locales), qué conserva una ventana local de un poset, y si el adversario de borde plano puede
  reproducir la **ley completa** del suborden Schwarzschild o solo marginales de bajo orden (memo §7 Q1-Q2).
  Provee a A7 la **estructura de dependencia** (transitividad) que reemplaza la independencia de aristas.

## Asiento físico (rol Dowker/Surya) — guardrail de "problema correcto"

- **Encargo (ya dentro del physicist seat, hecho explícito):** verificar que `H_trap`/`H_no-trap` no
  introducen de contrabando una geometría clásica; que una eventual separación detecte **enfocamiento nulo
  genuino** y no el borde, la singularidad impuesta o una condición de contorno artificial (memo §7 Q6).
  Poder de veto: convertir un `SEPARABLE` en "separable pero por el artefacto equivocado".

## Interacciones y orden de deliberación

```
mathematician(formulación) → fija P_n,Q_n y la dependencia
        ↓
A7(asintótica) → clasifica en los 4 casos  → token
        ↓
physicist(Dowker/Surya) ── veta si la separación es por artefacto
falsifier ── ataca: ¿A7 asumió independencia? ¿confundió output con suborden completo?
literature verifier ── ¿técnica conocida? (random orders, sprinkling indistinguishability)
warden ── nada que congelar aquí; vigila que NO se cuele un prereg encubierto
```

## Criterio de éxito de la sesión (qué decide convocar)

La sesión es útil sii produce **uno** de: (a) el token de clasificación con prueba/sketch verificable; o
(b) `UNDECIDED_NEEDS_<X>` con `<X>` lo bastante concreto como para ser una pregunta de dos líneas a un
experto externo real (Brightwell/Kleijn) — i.e. el memo §7 afinado. Cualquier otra salida (narrativa,
"prometedor", reabrir estimadores) es fallo de la sesión.

## Estado

Asiento **definido, NO convocado**. Siguiente paso reversible cuando lo decidas: lanzar `/comite` con este
charge + el memo como carga. Esta nota no congela nada y no toca el path sellado.
