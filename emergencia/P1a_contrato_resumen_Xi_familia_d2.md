# P1a — Contrato de la familia de resúmenes `Xi^A ⊂ Xi^B ⊂ Xi^C` en `d=2`

> **ESTADO: FAMILIA DE RESÚMENES CONGELADA v1.0 · DECLARADA ANTES DE OBSERVAR
> `q_p` · TRES IDENTIDADES DISTINTAS, LAS TRES SE REPORTAN · MÉTRICA = IGUALDAD
> EXACTA · REGLA DE PARES Y CRITERIO DE FALSACIÓN TODAVÍA ABIERTOS.**
>
> Fecha de congelación: 26 de agosto de 2026.

Este documento ejecuta los pasos 1–6 de la secuencia obligatoria del
`emergencia/P1a_contrato_admisibilidad_resumen_coarse_graining_d2.md`, §6. **No
completa la secuencia**: los pasos 7 (regla de selección de pares y criterio
cuantitativo de falsación) y 8 (materializar `q_p`) siguen sin autorizar. Congelar
`Xi` no abre `q_p`.

La base de datos estática de este contrato es
`emergencia/resultados/p1a_paisaje_niveles_d2.csv`
(sha256 `a02602fc8f08451c36324ae8818998be656a21a8a25929fd445a26c8a61529dd`), extraído
por `emergencia/p1a_paisaje_niveles_d2.py` sin ningún acceso al target.

## 0. Por qué una familia y no un resumen único

El §6 del contrato de admisibilidad permite explícitamente explorar varias
propuestas «declaradas de antemano como una familia finita» que «conserven
identidades distintas», y prohíbe presentar como preregistrado un resumen elegido
después de comparar sus resultados con `q_p`.

Se declaran aquí **tres** resúmenes anidados, con identidades distintas y fijas.
Las tres se evaluarán y las tres se reportarán, cualquiera que sea el resultado. No
se añadirá un cuarto miembro, no se retirará ninguno, y no se elegirá un «ganador»
después de ver `q_p`: el reporte final contendrá los tres.

## 1. Objeto sobre el que se define el resumen

Sea `C=C_sigma` el `2-order` estricto de una permutación de tamaño `n<=9`, y sea
`Q(C)` el conjunto de cuádruplas admisibles del selector congelado
`MIN_COVERAGE_LEX` con `K0=3`, tal como lo fija
`emergencia/P1a_contrato_estimando_qp_orbital_d2.md`, §1.

El score de un candidato `x=(a,b,c,d) in Q(C)` es el par

```text
S_C(x) = ( min(C_ab, C_cd),  C_ab + C_cd ),
```

ordenado lexicográficamente. Sean

```text
S_1 > S_2 > ... > S_L
```

los valores **distintos** de `S_C` sobre `Q(C)`, en orden lexicográfico
descendente, y

```text
A_j(C) = { x in Q(C) : S_C(x) = S_j },      j = 1..L.
```

Se escribe `S_j=(m_j,s_j)`, `c_j=|A_j(C)|` y `r_j=|A_j(C)/Aut(C)|`, donde `Aut(C)`
actúa componente a componente. Por construcción `A_1(C)=M(C)` y `r_1=rho(C)`.

Todos estos objetos son estáticos: se calculan sobre `C` y sólo sobre `C`.

## 2. Definición exacta de las tres coordenadas por nivel

Para cada profundidad `j` se definen cinco cantidades:

```text
avail_j = 1 si L >= j,  0 en otro caso        (indicador de disponibilidad)
m_j     = primera coordenada de S_j            NA si avail_j = 0
s_j     = segunda coordenada de S_j            NA si avail_j = 0
c_j     = |A_j(C)|                             NA si avail_j = 0
r_j     = |A_j(C)/Aut(C)|                      NA si avail_j = 0
```

`NA` nunca se convierte en cero. `avail_j` es el indicador de disponibilidad que
exige la condición 9 del contrato de admisibilidad.

Cuando `Q(C)=emptyset` se tiene `L=0`, luego `avail_j=0` para toda `j`, y todas las
coordenadas de nivel son `NA`. Esto no es un caso patológico raro: en `n=9`,
344 837 de las 362 880 permutaciones están en él.

`Aut(C)` no se enumera cuando `Q(C)=emptyset`, exactamente como hace el instrumento
congelado `p1a_tie_aut_diagnostic.py`. El orden del grupo **no** es una coordenada
de ningún miembro de esta familia.

## 3. Los tres miembros

```text
Xi^A  (dimensión  5) = ( avail_1, m_1, s_1, c_1, r_1 )

Xi^B  (dimensión 10) = Xi^A  ++  ( avail_2, m_2, s_2, c_2, r_2 )

Xi^C  (dimensión 18) = Xi^B  ++  ( avail_3, m_3, s_3, c_3, r_3 )
                             ++  ( L, |Q(C)|, R )
```

con

```text
R = suma_{j=1..L} r_j     (número total de órbitas de candidatos, todos los niveles)
  = 0 cuando L = 0.
```

`L`, `|Q(C)|` y `R` son totales sobre el paisaje completo, no requieren `NA` y valen
`0` cuando `Q(C)=emptyset`; ese cero es un conteo genuino, no un `NA` encubierto.

Las dimensiones 5, 10 y 18 son constantes: no dependen de `n`. El rango de cada
coordenada crece con `n`, lo que la condición 7 permite; lo que prohíbe es que crezca
el **número** de coordenadas, y aquí no crece.

`Xi^A ⊂ Xi^B ⊂ Xi^C` como listas de coordenadas: cada miembro es un prefijo del
siguiente. La fibra de `Xi^C` refina la de `Xi^B`, que refina la de `Xi^A`.

## 4. Pérdida de información que cada bloque pretende controlar

Requisito 1 del §6 del contrato de admisibilidad. Se declara la intención, no un
resultado:

- `avail_1` controla la desaparición total del paisaje de candidatos.
- `(m_1,s_1)` controla la escala del óptimo: cuán grandes son los dos intervalos que
  el selector consigue emparejar.
- `c_1` controla la multiplicidad bruta del argmax, es decir el tamaño del empate.
- `r_1=rho(C)` controla la parte del empate que **no** explica el cociente por
  automorfismos. Es la cantidad que define `r_orb`.
- El bloque de profundidad 2 controla la existencia y el tamaño del primer nivel
  rival, y — al llevar `(m_2,s_2)` junto a `(m_1,s_1)` — deja el salto de score
  disponible como par ordenado **sin definir ninguna distancia escalar**.
- El bloque de profundidad 3 controla la continuación inmediata del paisaje.
- `(L,|Q(C)|,R)` controla el tamaño global del paisaje y su masa orbital total, sin
  describir su forma.

Ninguna de estas frases es una hipótesis contrastada. Son la justificación
informativa previa que la condición 1 exige, y quedan sujetas a falsación.

## 5. Verificación de las diez condiciones de admisibilidad

1. **Definición previa.** Este documento se congela antes de calcular un solo valor
   de `q_p`, `q_p^star`, `e_p`, `a_k` o `b_k`. Ninguno de esos objetos existe todavía
   en el repositorio: `grep -rn "r_orb" --include=*.py .` no devuelve nada.
2. **Intrinsicidad.** Toda coordenada es un invariante de orden. `C_ab` es la
   cardinalidad del intervalo `{z : a <= z <= b}` de `C`; la admisibilidad y la
   cadena `a prec b prec c prec d` son intrínsecas; luego `S_C` es
   `Aut(C)`-invariante, cada `A_j` es `Aut(C)`-cerrado, y `c_j`, `r_j`, `L`, `|Q|`,
   `R` son invariantes por isomorfismo. Se verifica además numéricamente en §6.
3. **Estado original solamente.** Sólo se usa `C` y su paisaje estático de
   candidatos. No se borra, intercambia, perturba ni reordena ningún elemento.
4. **Independencia del thinning.** No intervienen máscaras, `R_p`, subposets propios
   inducidos ni tasas de retención. El módulo generador no importa
   `p1a_estabilidad_d2` y no llama a `induced_permutation`.
5. **Ausencia de fuga del objetivo.** Ninguna coordenada usa `q_p`, `q_p^star`,
   `e_p`, `a_k`, `b_k`, estimaciones Monte Carlo ni sustitutos de ellos.
6. **Independencia de `p`.** `p` no aparece en ninguna definición.
7. **Baja dimensión real.** 5, 10 y 18 coordenadas, constantes en `n`. No hay listas
   de longitud creciente ni histogramas.
8. **Compresión no trivial.** No hay hashes, formas canónicas, expansiones digitales
   ni reales de precisión arbitraria. La distribución de tamaños de fibra y la
   existencia de colisiones entre clases **no isomorfas** se documentan en el
   artefacto de §6, antes de mirar `q_p`.
9. **Totalidad y tipado explícito.** Los tres miembros están definidos también
   cuando `Q(C)` o `M(C)` son vacíos, mediante `avail_j` y `NA`.
10. **Reproducibilidad exacta.** Cada coordenada se calcula por dos caminos
    independientes en `n<=9`: recomputación en vivo desde la permutación, y lectura
    del artefacto CSV del paisaje. Ninguna implementación es su propia referencia.

## 6. Declaración obligatoria sobre `rho`

`r_1=rho(C)` es coordenada de los tres miembros. Por tanto, conforme al §4 del
contrato de admisibilidad, se declara expresamente:

```text
q_1(C) = r_orb(C) es un control TAUTOLÓGICO, no evidencia predictiva.
Cualquier prueba no trivial de esta familia deberá usar 0 < p < 1.
```

## 7. Paso 6 del §6: métrica en espacio-`Xi`

Se congela como regla de igualdad la **igualdad exacta del vector completo**, con
`NA` igual a `NA` en la misma coordenada:

```text
Xi^X(C) ~ Xi^X(C')   sii   coinciden las X coordenadas una a una.
```

Dos configuraciones son comparables por esta familia exactamente cuando caen en la
misma fibra. No se introduce distancia, umbral, `delta`, normalización ni peso entre
coordenadas: la igualdad exacta es la única regla que no exige ninguna elección
adicional, y es la que el propio §3.8 presupone al hablar de fibras.

## 8. Lo que este contrato NO congela

- la regla de selección de pares `(sigma,tau)` dentro de una fibra;
- el criterio cuantitativo de falsación;
- los valores de `p` que se estudiarán;
- la corrección por multiplicidad si se examinan muchos pares;
- cualquier campaña Monte Carlo para `n>9`;
- cualquier conclusión `WALL` o `NO-WALL`.

`q_p` sigue sin autorizar. La secuencia del §6 del contrato de admisibilidad se
reanudará en su paso 7.

## 9. Techo de afirmación

Este documento define tres resúmenes estáticos del paisaje de score del selector
`MIN_COVERAGE_LEX` y una regla de igualdad entre ellos. No demuestra que ninguno sea
variable suficiente, no establece estabilidad, coarse-graining físico, dinámica de
renormalización, metastabilidad ni relevancia asintótica.

```text
P1A_XI_FAMILY_VERSION = 1.0
P1A_XI_FAMILY_MEMBERS = XI_A,XI_B,XI_C
P1A_XI_FAMILY_DIMENSIONS = 5,10,18
P1A_XI_FAMILY_NESTED = YES
P1A_XI_FAMILY_ALL_MEMBERS_REPORTED = REQUIRED
P1A_XI_FAMILY_SELECTOR = MIN_COVERAGE_LEX
P1A_XI_FAMILY_K0 = 3
P1A_XI_FAMILY_EMPTY_POLICY = AVAIL_FLAG_AND_NA_NEVER_ZERO
P1A_XI_FAMILY_METRIC = EXACT_VECTOR_EQUALITY
P1A_XI_FAMILY_RHO_INCLUDED = YES
P1A_XI_FAMILY_Q1_IS_TAUTOLOGICAL = DECLARED
P1A_XI_FAMILY_FROZEN_BEFORE_TARGET = YES
P1A_COARSE_SUMMARY_SEQUENCE_STEPS_DONE = 1,2,3,4,5,6
P1A_COARSE_SUMMARY_SEQUENCE_STEPS_PENDING = 7,8
P1A_PAIR_SELECTION_RULE_STATUS = NOT_FROZEN
P1A_FALSIFICATION_CRITERION_STATUS = NOT_FROZEN
P1A_QP_EXECUTION_AUTHORIZED = NO
```
