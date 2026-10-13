Eres ASTRA. No tienes acceso a ficheros, terminal, web ni herramientas: todo lo disponible está en este prompt. No escribas llamadas a herramientas; escribe tu respuesta directamente.

# Encargo ciego — anclaje de θ_loc y θ_stab para el banco 2+1D (prereg-004)

**Fecha:** 2026-10-13 · **Encarga:** el PI (decisión del comité 052, opción c1) · **Destinatario:**
ASTRA, sellado: una sola intervención, sin herramientas.

**Regla de ceguera (vinculante).** Este encargo **no contiene ningún resultado numérico de
exploración**: ni anchuras de horquilla, ni coberturas, ni sesgos, ni recuentos medidos. Tu
derivación tiene que salir solo de la geometría, de la regla de 1+1D y de argumentos de
estructura. No intentes adivinar ni ajustarte a valores medidos que no conoces. Si la derivación
necesita una constante que no se puede fijar analíticamente, dilo y propón cómo fijarla **sin**
datos de la verdad de referencia (por ejemplo, con un Montecarlo sobre la geometría continua, sin
semillas del proyecto).

## 1. El banco

- **Variedad.** El ecuador de Schwarzschild, `θ = π/2`. En coordenadas de Eddington–Finkelstein
  entrantes, la métrica es `−(1 − 2M/r) dv² + 2 dv dr + r² dφ²`, con `v = t* + r`. Se usa
  `2M = 0.5`.
- **Caja.** `t* ∈ [0, T]` con `T = 16` (congelado), `r ∈ [0.1, 1.3]` y `φ ∈ S¹`.
- **Medida.** `√(−g) = r`, así que el volumen es `T · π (1.3² − 0.1²)` y un sembrado de Poisson es
  uniforme en `(t*, φ)` con densidad `∝ r`.
- **Densidad.** `ρ` se define como puntos por unidad de volumen 2+1D. Se congela a partir de la
  intensidad nominal y nunca del `N` realizado. La rejilla congelada es `ρ ∈ {32, 63, 126}`, con
  `ρ = 126` como principal.
- **Orden causal.** El orden causal del ambiente, que en el ecuador coincide con el de
  Schwarzschild 3+1D, restringido a los puntos sembrados.

## 2. El estimador (solo usa el orden)

- **Observable.** Los elementos mínimos son los que no tienen pasado dentro del conjunto. Para
  cada uno se toma `O(i) = |futuro(i)|`, el número de elementos de su futuro.
- **Partición.** Una partición en dos grupos (2-medias) de los valores `O` de los mínimos. Los de
  `O` bajo deberían ser los de dentro del horizonte, porque su futuro queda cortado por el borde
  interior `r = 0.1`. Los de `O` alto serían los de fuera.
- **Puntuación.** Solo al puntuar se revela `r`. Se forma la horquilla
  `[máx r de los mínimos con O bajo, mín r de los mínimos con O alto]`. Su anchura `|dr|` es el
  objeto del criterio de localización (ii), que se mide en unidades de `2M`. Su punto medio, a
  través de las semillas, es el objeto del criterio de estabilidad (iii).

## 3. La regla sellada de 1+1D que hay que trasladar

En 1+1D (caja `t ∈ [0, 6]`, `r ∈ [0.1, 1.3]`, área `7.2`, densidad uniforme), el código sellado
dice (`nachocausal/thresholds.py`):

```text
# --- Localisation / stability (frozen; anchored to the DISCRETENESS scale) ----
# ell is computed from the FROZEN INTENSITY and the FIXED box area, NEVER from
# the realized Poisson N (cmte C2), so the thresholds are literal constants.
K_LOC = 2                      # user decision; cannot localise finer than ~ell
ell(intensity)   = (intensity / BOX_AREA) ** -0.5        # 2D discreteness scale rho^(-1/2)
theta_loc        = K_LOC * ell / (2M)                     # bound on bracket width |dr|/(2M)
theta_stab       = K_LOC * ell                            # bound on std of boundary r-location across seeds
```

El principio declarado es: **«no se puede localizar más fino que ~ℓ»**.

## 4. Lo que te pido

1. **Traslada el principio de §3 al banco 2+1D**, con `K_LOC = 2` **sin cambiar**. Decide qué
   escala de discretitud es la que gobierna la anchura de la horquilla, que es una separación en
   `r` entre elementos mínimos, y justifícalo. Algunas candidatas, sin preferencia por ninguna:
   - el traslado dimensional `ρ^{-1/3}`;
   - una separación radial entre elementos mínimos;
   - cualquier otra que derives.

   Tu argumento tiene que reducirse exactamente a la regla sellada `ℓ = ρ^{-1/2}` cuando se aplica
   a 1+1D. Si no se reduce, explica por qué 1+1D es un caso distinto.
2. Si tu escala depende de un **punto de evaluación**, por ejemplo un perímetro `2πr` en algún `r`,
   **elígelo sin usar la verdad de referencia**: `2M` está oculto para el estimador. Justifica la
   elección. Si usas `2M` solo como unidad de puntuación, como hace 1+1D, dilo.
3. Fija cualquier **constante O(1)**:
   - analíticamente si se puede;
   - si no, con un procedimiento libre de datos que dejes especificado;
   - o, si no, declárala absorbida en `K_LOC = 2`, como en 1+1D, y dilo.
4. Haz lo mismo para `θ_stab`, de forma coherente con `θ_loc`.
5. Da la **fórmula final** de `θ_loc(ρ)` y `θ_stab(ρ)`, y sus **valores numéricos** en
   `ρ = 32, 63, 126` con `T = 16`.
6. Señala cualquier riesgo de que el criterio resultante **no pueda fallar** (decorativo) o
   **falle siempre**, razonando solo desde la estructura, sin datos.

**Formato:** en español, de 700 a 1000 palabras. Etiqueta como `[DERIVACIÓN]` lo que deduces y
como `[SUPUESTO]` lo que asumes. Termina con un bloque `FÓRMULA_FINAL` que contenga las fórmulas y
los seis números.
