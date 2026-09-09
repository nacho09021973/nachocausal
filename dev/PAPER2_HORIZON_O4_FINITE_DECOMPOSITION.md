# Cruce del horizonte: descomposición finita por O4

Este documento fija la primera identidad de tamaño finito para cadenas que
cruzan `r = r_S`. No contiene todavía un resultado asintótico ni una
reformulación intrínseca del poset.

## Partición finita

Sea `P_ρ` el conjunto finito de puntos del sprinkling y supongamos que ningún
punto cae exactamente en el horizonte. Escribimos

```text
P_ρ = P_ρ^ext ⊔ P_ρ^int.
```

Por O4, para `e ∈ P_ρ^ext` e `i ∈ P_ρ^int`,

```text
e ≺ i  ↔  v(e) ≤ v(i),
```

y no existe una relación futura `i ≺ e`. Por tanto, toda cadena que contiene
puntos de ambos bloques tiene una única forma

```text
e₁ ≺ ⋯ ≺ e_m ≺ i₁ ≺ ⋯ ≺ i_n,
```

con `e_m ≺ i₁` decidido únicamente por `v(e_m) ≤ v(i₁)`.

## Longitudes ancladas

Definimos

```text
ℓ_ext(e) = max {|C| : C ⊆ P_ρ^ext es cadena y max C = e},
ℓ_int(i) = max {|C| : C ⊆ P_ρ^int es cadena y min C = i}.
```

La altura del conjunto vacío y todos los máximos sobre conjuntos vacíos se
interpretan como `0`, incluido el caso de dos bloques no vacíos sin par cruzado.

La longitud máxima de cadena en `P_ρ` satisface exactamente

```text
L_ρ(P_ρ) = max {
  L_ρ^ext,
  L_ρ^int,
  max { ℓ_ext(e) + ℓ_int(i) :
        e ∈ P_ρ^ext, i ∈ P_ρ^int, v(e) ≤ v(i) }
}.
```

La suma no cuenta dos veces ningún punto: los tramos exterior e interior son
disjuntos. La igualdad se obtiene en ambas direcciones: una cadena cruzada se
separa en su último punto exterior y su primer punto interior; recíprocamente,
dos cadenas ancladas en `e` e `i` se concatenan cuando `v(e) ≤ v(i)`.

## Alcance

O4 se usa aquí como caracterización exacta en el embedding, no como un
invariante definido únicamente a partir del poset. La identidad es finita y
determinista. No justifica aún el intercambio de

```text
lim_{ρ→∞} max   y   max lim_{ρ→∞}.
```

**Continuación (2026-09-09):**
[umbral finito, carta regular y control del horizonte](PAPER2_HORIZON_THRESHOLD_LIMIT.md).
Allí se demuestra la identidad por umbral, distinguiendo cadenas cruzadas de
cadenas puras cuando un lado está vacío. La monotonía de los perfiles permite
pasar de convergencia puntual a uniforme si el límite es continuo.

La misma nota exhibe una carta nula regular `(v,Z)` que representa el orden
de ambos bloques y prueba una cota uniforme para borrar una banda del
horizonte. Incluye una demostración propuesta de los límites compactos con
umbral y del paso al máximo. Su revisión matemática sigue pendiente; esta
identidad finita no se convierte por sí sola en un teorema de detección.
