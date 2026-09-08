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

Si un bloque no contiene puntos, su longitud y los máximos correspondientes
se interpretan como `0`.

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

El paso al límite requiere control uniforme de las longitudes ancladas y de
la maximización sobre pares de cruce, además de un tratamiento de la pérdida
de compacidad de la carta nula al aproximarse a `r = r_S`.

La siguiente tarea acotada es reorganizar el término cruzado por un umbral de
`v`, y demostrar el control uniforme necesario antes de invocar cualquier
límite variacional.
