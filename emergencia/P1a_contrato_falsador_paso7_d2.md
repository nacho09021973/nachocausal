# P1a — Contrato del falsador (paso 7) para la familia `Xi^A ⊂ Xi^B ⊂ Xi^C` en `d=2`

> **ESTADO: CRITERIO DE FALSACIÓN Y POBLACIÓN CONGELADOS v1.0 · DECLARADO ANTES DE
> OBSERVAR `q_p` · SIN UMBRAL, SIN `p`, SIN BANDA NULA · COMPLETA EL PASO 7 DE LA
> SECUENCIA §6.**
>
> Fecha de congelación: 26 de agosto de 2026.

Este documento cierra el paso 7 de la secuencia obligatoria del
`emergencia/P1a_contrato_admisibilidad_resumen_coarse_graining_d2.md`, §6. Con los
pasos 1–6 ya cerrados por `emergencia/P1a_contrato_resumen_Xi_familia_d2.md`, la
precondición del paso 8 queda satisfecha. Este contrato **no** ejecuta el paso 8.

Base congelada previa:

- estimando y `a_k`: `P1a_contrato_estimando_qp_orbital_d2.md`;
- familia y métrica: `P1a_contrato_resumen_Xi_familia_d2.md`;
- paisaje estático: `resultados/p1a_paisaje_niveles_d2.csv`
  (sha256 `a02602fc8f08451c36324ae8818998be656a21a8a25929fd445a26c8a61529dd`);
- fibras: `resultados/p1a_xi_familia_fibras_resumen.json`
  (sha256 `35b6c8200860537c3d7c63b4c28f48a6ecab59b2229501163c661e66fbbf86fa`).

## 1. Hechos previos, demostrados sin observar `q_p`

Estos cuatro hechos se derivan de las definiciones ya congeladas. No son mediciones y
no consumen acceso al target. Se registran aquí porque determinan el diseño.

**H1. `q_p ≡ 0` en toda la fibra no disponible.** Si `Q(C)=emptyset` entonces
`Q(C[A])=emptyset` para todo `A ⊆ [n]`: los endpoints de una cuádrupla admisible de
`C[A]` forman la misma cadena `a≺b≺c≺d` en `C`, y `|[a,b]_{C[A]}| <= |[a,b]_C|`
porque restringir sólo puede quitar elementos del intervalo; luego la cuádrupla sería
admisible en `C`. Por tanto `r_orb(R_p(sigma))=0` para toda máscara y
`Delta_p = 0` exactamente sobre esa fibra, para todo `p`. La fibra no disponible pasa
el test **por teorema**, no por evidencia.

**H2. `a_k = 0` para `k<6`, y `a_n = r_orb(C)` es función de `Xi^A`.** Lo primero es
el §3 del contrato del estimando. Lo segundo, porque
`r_orb(C) = 1{avail_1=1 y r_1=1}` y ambas son coordenadas de `Xi^A`. Luego `a_n` es
**constante dentro de cualquier fibra** de los tres miembros, y los coeficientes
libres dentro de una fibra son exactamente `a_6,...,a_{n-1}`:

```text
n=6: ninguno  -> el test no puede fallar; n=6 es VACÍO y se declara así de antemano
n=7: a_6                       (1 grado de libertad)
n=8: a_6, a_7                  (2)
n=9: a_6, a_7, a_8             (3;  |Delta a_6|<=84, |Delta a_7|<=36, |Delta a_8|<=9)
```

**H3. `d(p) := q_p(sigma)-q_p(tau)` se anula en ambos extremos** para `sigma,tau` en
una misma fibra: `d(0)=0` porque `q_0=0` siempre, y `d(1)=0` por H2. El supremo se
alcanza en el interior. Por eso el intervalo `I=(0,1)` **no es una elección**: es el
único que no descarta información, y no hace falta preregistrar ningún `p`, rejilla
ni subintervalo.

**H4. `D_C <= D_B <= D_A` es una identidad matemática.** `Xi^B` es prefijo de `Xi^C`,
luego toda fibra de `C` está contenida en una de `B`, y un máximo sobre un conjunto
menor no puede ser mayor. Se declara igual que `q_1=r_orb`:

```text
La DIRECCIÓN de la monotonía en profundidad es TAUTOLÓGICA, no evidencia.
Sólo la MAGNITUD del descenso informa.
```

## 2. Población congelada

Para cada `n in {6,7,8,9}` y cada miembro `X in {A,B,C}`, la población es

```text
P_X(n) = { fibras F de Xi^X : avail_1(F) = 1  y  |F| >= 2 }.
```

Se excluyen por construcción, no por resultado, los dos conjuntos cuyo
`Delta_p` es cero forzado:

- la fibra no disponible (`avail_1=0`), por H1;
- las fibras disponibles con un solo elemento, donde no hay par que comparar.

Ambas exclusiones se reportarán con su recuento y su razón. Tamaños de `P_X(n)`, ya
fijados por el estudio de fibras y por tanto no elegibles a posteriori:

```text
n=6   Xi^A: 0    Xi^B: 0    Xi^C: 0     (población vacía; coincide con H2)
n=7   Xi^A: 3    Xi^B: 3    Xi^C: 3
n=8   Xi^A: 12   Xi^B: 16   Xi^C: 16
n=9   Xi^A: 33   Xi^B: 73   Xi^C: 92
```

## 3. Criterio de falsación congelado

Para una fibra `F` y `sigma,tau in F`, escríbase el vector entero de coeficientes
libres

```text
alpha(sigma) = ( a_6(sigma), ..., a_{n-1}(sigma) ).
```

Como `{p^k(1-p)^{n-k}}_{k=0..n}` es base del espacio de polinomios de grado `<=n`, y
`a_k=0` para `k<6` y `a_n` es constante en la fibra, se tiene la equivalencia exacta

```text
q_p(sigma) = q_p(tau) para TODO p    <=>    alpha(sigma) = alpha(tau).
```

Se define entonces

```text
F es HOMOGÉNEA   sii   alpha es constante sobre F.
```

y el veredicto por miembro y por `n`:

```text
Xi^X es SUFICIENTE en n     sii   toda fibra de P_X(n) es homogénea.
Xi^X es NO SUFICIENTE en n  sii   existe al menos una fibra no homogénea.
```

No hay umbral, no hay `p`, no hay banda nula, no hay `p`-valor y no hay corrección
por multiplicidad: el veredicto es una igualdad combinatoria exacta, no un contraste
estadístico. El par adversarial no requiere ninguna regla de selección: está definido
como cualquier par que testifique la no homogeneidad de su fibra.

## 4. Estadístico graduado, también sin umbral

Junto al veredicto binario se reportará siempre, por miembro y por `n`:

```text
h_X(n) = |{F in P_X(n) : F homogénea}| / |P_X(n)|
w_X(n) = (permutaciones en fibras homogéneas de P_X(n)) / (permutaciones en P_X(n))
```

`h_X` y `w_X` toman valores en `[0,1]`, no requieren umbral y admiten cualquier
resultado. Por H4, su dirección en `X` está forzada; su magnitud no.

> **ERRATUM v1.0-e1, 26 de agosto de 2026, POSTERIOR A LA EJECUCIÓN.**
> La última frase de este §4 es incorrecta y se deja intacta arriba para preservar
> el registro. H4 fuerza la dirección de `D_X`, y sólo de `D_X`: el máximo sobre un
> conjunto menor no puede crecer. **No** fuerza la de `h_X` ni la de `w_X`.
> Contraejemplo: al refinar, una fibra homogénea de tamaño 2 puede partirse en dos
> singletons, que la población del §2 excluye; el numerador pierde una fibra
> homogénea y `h` puede **bajar**. Por tanto cualquier monotonía observada en
> `h_X` o `w_X` es un dato, no una identidad, y así debe reportarse.
> Este erratum no toca el criterio del §3, ni la población del §2, ni `D_X`, ni
> ningún veredicto: `h` y `w` nunca adjudicaron nada.

## 5. Magnitud descriptiva, que NUNCA adjudica

Se reportará además

```text
D_X(n) = max_{F in P_X(n)}  max_{sigma,tau in F}  sup_{p in (0,1)} |q_p(sigma)-q_p(tau)|,
```

junto con la fibra y el par que lo realizan. Por H3 el supremo es interior; por H2 el
polinomio `d` tiene a lo sumo tres coeficientes libres en `n<=9`, luego el supremo es
calculable exactamente en aritmética racional (el máximo sobre `p` de un polinomio de
grado `<=9` con coeficientes enteros, vía sus puntos críticos certificados).

`D_X` es **descriptiva**. No define el veredicto, no se le asocia umbral, y ningún
resultado suyo puede reclasificar un veredicto ya emitido por el §3.

Nota de implementación, no de definición: `max` sobre un conjunto finito conmuta con
`sup_p`, y `alpha` toma pocos valores distintos dentro de una fibra, de modo que basta
deduplicar por `alpha` antes de recorrer pares. Eso no altera el valor de `D_X`.

## 6. Obligaciones de reporte

- Se reportan **los tres miembros**, siempre, cualquiera que sea el resultado. No se
  elige un ganador después de ver `q_p`.
- Se reporta `n=6` como VACÍO por H2, no como PASS.
- Se reportan los recuentos de las dos exclusiones del §2 con su razón.
- Se reporta H4 junto a cualquier comparación entre miembros.
- Se reporta `q_1 = r_orb` como control tautológico, y la verificación
  `q_0 = 0`, `q_1 = r_orb(C_sigma)` exigida por el §7 del contrato del estimando.
- Se contrasta la suma directa sobre máscaras con los polinomios `a_k`, `b_k`.
- `q_p^star` se reporta con `e_p`, y vale `NA` cuando `e_p=0`, nunca cero.

## 7. Lo que este contrato NO autoriza

- ningún `n>9`;
- ninguna campaña Monte Carlo;
- ningún cuarto miembro de la familia;
- ninguna reponderación de la población tras ver `q_p`;
- ninguna conclusión `WALL` o `NO-WALL`.

## 8. Techo de afirmación

Un veredicto NO SUFICIENTE refuta la suficiencia exacta de ese resumen en el tamaño y
régimen examinados. Un veredicto SUFICIENTE no demuestra suficiencia asintótica, ni
estabilidad, ni coarse-graining físico, ni dinámica de renormalización. En `n<=9` el
poder discriminante está acotado por H2 a tres enteros, y esa limitación se declara
antes de mirar el resultado.

```text
P1A_FALSIFIER_VERSION = 1.0
P1A_FALSIFIER_ERRATA = e1_h_and_w_monotonicity_not_forced_by_H4
P1A_FALSIFIER_CRITERION = EXACT_COEFFICIENT_VECTOR_EQUALITY
P1A_FALSIFIER_FREE_COEFFICIENTS = a_6..a_{n-1}
P1A_FALSIFIER_THRESHOLD = NONE
P1A_FALSIFIER_P_CHOICE = NONE_VERDICT_IS_P_FREE
P1A_FALSIFIER_MAGNITUDE_INTERVAL = OPEN_0_1_FORCED_BY_H3
P1A_FALSIFIER_MAGNITUDE_ADJUDICATES = NO
P1A_FALSIFIER_POPULATION = AVAILABLE_FIBRES_WITH_AT_LEAST_TWO_MEMBERS
P1A_FALSIFIER_PAIR_RULE = NOT_NEEDED_ANY_WITNESS_OF_INHOMOGENEITY
P1A_FALSIFIER_MULTIPLICITY_CORRECTION = NOT_APPLICABLE_EXACT_EQUALITY
P1A_FALSIFIER_NULL_BAND = NONE
P1A_FALSIFIER_N6_STATUS = VACUOUS_BY_H2
P1A_FALSIFIER_ALL_MEMBERS_REPORTED = REQUIRED
P1A_COARSE_SUMMARY_SEQUENCE_STEPS_DONE = 1,2,3,4,5,6,7
P1A_COARSE_SUMMARY_SEQUENCE_STEPS_PENDING = 8
P1A_QP_EXECUTION_AUTHORIZED = YES
P1A_QP_EXECUTION_SIGNOFF = PI, 26 de agosto de 2026, sobre este contrato v1.0
P1A_DESIGN_PHASE = CLOSED_ON_SIGNOFF
```
