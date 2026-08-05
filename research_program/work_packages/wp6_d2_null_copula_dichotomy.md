# WP6 — La dicotomía de cópula nula en `d=2`: el orden ve exactamente la curvatura

```text
ESTADO: TEOREMA C [PROVED] / TEOREMA D [PROVED_MODULO_FUENTES_VERIFICADAS] / PUENTE E OPEN
ALCANCE: d=2, parches que son caja de coordenadas nulas
NATURALEZA: deductivo + bibliográfico. Cero semillas, cero simulación, sello intacto.
GOBERNANZA: requiere nota firmada — ver docs/program_reopening_note_2026-08-05_R3.md
FECHA: 2026-08-05
```

## 0. Qué afirma este documento en una frase

En `d=2`, y sobre un parche que es caja de coordenadas nulas, el orden causal de un
sprinkling condicionado a `N=n` ve **exactamente la cópula** de la medida de volumen en
coordenadas nulas; esa cópula es trivial **si y solo si el parche es plano**; luego todo
lo que el orden puede ver de la geometría es la curvatura, y la clase de invisibilidad
es exactamente la órbita del grupo infinito-dimensional de reparametrizaciones nulas.

Es la dimensión que HKMM (`d>2`), Braun (`d>=3`) y Madsen (`d>2`) excluyen, y la
exclusión de esos tres teoremas queda explicada estructuralmente por el mismo grupo.

## 1. Marco

Sea `B = [U_0,U_1] x [V_0,V_1]` una caja en coordenadas nulas globales y

```
g = -Omega(U,V) dU dV,     Omega > 0 continua sobre B.
```

Con `g_UV = g_VU = -Omega/2` se tiene `det g = -Omega^2/4`, luego

```
sqrt(-det g) = Omega/2,     dvol_g = (Omega/2) dU dV.
```

**La densidad de sprinkling en coordenadas nulas es proporcional a `Omega` misma.** Esa
coincidencia —que el factor conforme *es* la densidad, sin exponentes— es lo que hace que
el resultado de abajo sea exacto y no aproximado; en `d>2` no ocurre.

Sprinkling de Poisson de densidad `rho`, condicionado a `N=n`. Por el **Lema 2.1**
(`docs/manuscript_limits_draft.md:273`, `[PROVED]`) los `n` puntos son iid con ley

```
mu_Omega = Omega dU dV / integral_B Omega.
```

Orden causal en coordenadas nulas: `p <= q` si y solo si `U_p <= U_q` y `V_p <= V_q`. El
poset inducido es, por tanto, el orden producto — la estructura de dimensión 2.

Escribimos `P_n(Omega)` para la ley del **poset no etiquetado** de `n` elementos, y
`Q_n(Omega)` para la ley de la **permutación** inducida (rangos de `V` ordenados por `U`).
`P_n` es un engrosamiento de `Q_n`; la distinción es la §5, y es donde está el único hueco.

## 2. Lema A (invariancia por rangos) — reformulación del Lema 2.2

`[PROVED]`

Sean `F(u) = mu_Omega([U_0,u] x [V_0,V_1])` y `G(v) = mu_Omega([U_0,U_1] x [V_0,v])`.
Como `Omega > 0` es continua sobre la caja, `F` y `G` son continuas y **estrictamente
crecientes**. La transformación de rangos

```
T = (F,G) : B -> [0,1]^2
```

es un homeomorfismo creciente en cada coordenada por separado, luego **un isomorfismo de
orden** para el orden producto. Definimos la cópula `C_Omega := T_* mu_Omega`, medida de
probabilidad en `[0,1]^2` con marginales uniformes.

Como `T` preserva el orden punto a punto, la configuración de `n` puntos iid de
`mu_Omega` y su imagen por `T` inducen **el mismo poset etiquetado**. Por tanto

```
Q_n(Omega) = Q_n(C_Omega)   y   P_n(Omega) = P_n(C_Omega)   para todo n.
```

Esto es exactamente el Lema 2.2 del manuscrito (`:279`, `[PROVED]`), aquí con la
transformación explícita.

## 3. Proposición B (separable <=> plano)

`[PROVED]`

> `Omega(U,V) = a(U) b(V)` con `a,b > 0` continuas **si y solo si** `(B,g)` es plana.

**(⇐= de separable a plano.)** Sean `Ũ(U) = integral a` y `Ṽ(V) = integral b`, ambas
crecientes. Entonces `dŨ dṼ = a b dU dV = Omega dU dV`, luego `g = -dŨ dṼ`: es Minkowski
en coordenadas nulas. Plana.

**(=⇒ de plano a separable.)** Si `(B,g)` es plana y `B` simplemente conexa, existen
coordenadas nulas `(Ũ,Ṽ)` con `g = -dŨ dṼ`. Las foliaciones nulas son invariantes
geométricos del `g` conforme, y en `d=2` son exactamente `{U = cte}` y `{V = cte}`; luego
cualquier otro sistema de coordenadas nulas satisface `Ũ = Ũ(U)`, `Ṽ = Ṽ(V)` (o el mismo
par intercambiado), con ambas funciones crecientes. Entonces
`Omega dU dV = dŨ dṼ = Ũ'(U) Ṽ'(V) dU dV`, es decir `Omega = Ũ'(U) Ṽ'(V)`, separable.

**Comprobación cruzada por curvatura.** Con `Omega = e^{2 rho}`, el escalar de Ricci en
`d=2` es `R = c * Omega^{-1} * d_U d_V log Omega` con `c` dependiente de convención
(signatura y factor de simetrización). El **prefactor es convencional; la condición de
anulación no lo es**: `R == 0` si y solo si `d_U d_V log Omega == 0`, si y solo si
`log Omega` se separa en `alpha(U) + beta(V)`, si y solo si `Omega` es separable. Coincide
con la demostración elemental de arriba, que no usa la fórmula.

## 4. Teorema C (invisibilidad exacta, a todo `n`)

`[PROVED]` · Etiqueta propuesta: `PROVED_EXACT_INVISIBILITY_CLASS_D2`

> Si `Omega` es separable, entonces para **todo** `n >= 1`
>
> ```
> TV( P_n(Omega), P_n(1) ) = 0     y     TV( Q_n(Omega), Q_n(1) ) = 0,
> ```
>
> y la permutación inducida es **uniforme sobre `S_n`**.

**Demostración.** `Omega = a(U)b(V)` implica que `mu_Omega` es una medida producto con
marginales continuas. Luego `U` y `V` son independientes bajo `mu_Omega`, luego
`C_Omega = Pi` (la cópula producto, es decir Lebesgue en `[0,1]^2`), que es también
`C_1`. Por el Lema A, `Q_n(Omega) = Q_n(Pi) = Q_n(1)` y otro tanto para `P_n`. Para una
medida producto con marginales continuas los rangos de `U` y de `V` son independientes y
uniformes, luego la permutación inducida es uniforme. ∎

**No necesita teoría de permutones.** Solo el Lema 2.1 y el Lema A.

**Corolario (la clase de invisibilidad es una órbita).** El grupo de reparametrizaciones
nulas `G = Diff^+(I) x Diff^+(I)` actúa por
`Omega |-> (Omega o (phi x psi)) * phi' * psi'`. La órbita de `Omega == 1` es exactamente
`{ phi'(U) psi'(V) }`, es decir **exactamente los factores separables**. Combinando con la
Proposición B: la clase de invisibilidad de Minkowski es su órbita bajo `G`, y es de
dimensión infinita.

Esta es la razón estructural de la hipótesis `d>2` de HKMM, escrita como enunciado y no
como excusa: en `d>2` el grupo análogo es finito-dimensional (Liouville), luego el orden
determina la clase conforme rígidamente; en `d=2` no.

## 5. Teorema D (completitud a nivel de permutación) y el puente E

### 5.1 Teorema D

`[PROVED_MODULO_FUENTES_VERIFICADAS]` — fuentes verificadas por el PI, 2026-08-05.

> Si `Q_n(Omega) = Q_n(Omega')` para todo `n`, entonces `C_Omega = C_Omega'` en casi todo
> punto. En particular, `Q_n(Omega) = Q_n(1)` para todo `n` implica `C_Omega = Pi`, luego
> `Omega` separable (Prop. B), luego `(B,g)` plana.

**Demostración.** Por el Lema A basta trabajar con la cópula. Para `n` puntos iid de
`C_Omega`, la ley de la permutación inducida es **exactamente el vector de densidades de
patrones de tamaño `n`** del permutón `C_Omega`. La igualdad para todo `n` da igualdad de
todas las densidades de patrones. Unicidad del permutón:

- Hoppen, Kohayakawa, Moreira, Ráth, Sampaio, *Limits of permutation sequences*,
  J. Combin. Theory Ser. B **103** (2013) 93–113, arXiv:1103.5844 — el objeto límite es
  único salvo igualdad c.t.p.
- Grübel, *Ranks, copulas, and permutons*, Metrika **87** (2024) 155–182 — identificación
  explícita permutón ↔ cópula, unicidad, y convergencia c.s. de la permutación de rangos
  de `n` puntos iid de `C` hacia `C`.

∎

**Nota de alcance.** Se necesita la sucesión **completa** en `n`. Un `n` fijo no basta: la
ley a tamaño `n` determina densidades de patrones de tamaño `<= n` solamente, y hay
métricas curvas que coinciden con la plana a `n` pequeño.

### 5.2 Puente E — el único hueco, y es un viejo conocido

`OPEN`

El observable físico es el **poset no etiquetado** `P_n`, no la permutación `Q_n`. La
aplicación `sigma |-> [P_sigma]` es un engrosamiento cuyas fibras contienen al menos
`{sigma, sigma^{-1}}` (intercambiar `U` y `V`). Para correr el Teorema D desde datos de
poset hace falta:

> **(E)** Las densidades de patrones de poset determinan las densidades de patrones de
> permutación, salvo transposición `U <-> V`.

Eso es **exactamente** la unicidad del realizador salvo intercambio para posets de
dimensión 2 — es decir, `docs/bibliography_claims.md` §5.3, que lleva registrado como
`UNSUPPORTED_GAP` con la instrucción explícita de *no adoptarlo como respaldado por la
literatura*. Dushnik–Miller 1941 (§5.1, leído en primaria, `SUPPORTED`) prueba la
**existencia** del conjugado, y el propio dossier registra que "says nothing about
uniqueness of the realizer/conjugate up to swapping the two orders".

Dos rutas, ninguna cara:

- **(a) Bibliográfica.** OCR de Kelly–Trotter 1982 / Trotter 1995, ya presentes físicamente
  en `biblioteca/` pero no extraíbles con las herramientas de la sesión que los archivó
  (§5.2).
- **(b) Directa.** Es un enunciado combinatorio finito. No depende de nada geométrico.

**Lo que NO toca el hueco.** El Teorema C (invisibilidad) es inmune: un engrosamiento
preserva la igualdad de leyes. La mitad no-go de la dicotomía está cerrada sin (E).

### 5.3 Testigo suficiente que esquiva el hueco

A nivel de poset no etiquetado, la **densidad de pares comparables** es observable. Bajo
`Pi`, dos puntos iid son comparables con probabilidad exactamente `1/2`
(`1/4 + 1/4`). En general la densidad de comparables es `(1 + tau)/2` con `tau` la tau de
Kendall de `C_Omega`, y `tau(Pi) = 0`.

Luego: **densidad de comparables distinta de `1/2` certifica no-planitud, solo con orden,
sin (E) y sin permutones.** Es exactamente el estadístico del Teorema 3.9 del manuscrito.
Es suficiente, no necesario: `tau = 0` no implica `C = Pi`, y para esos casos hacen falta
patrones de orden superior — es decir, (E).

## 6. Consistencia con R2

R2 (`dev/R2_lambda6_derivation_NOTES.md`, 31 jul) obtuvo, cerca del horizonte,

```
log h = const(tau) + eps + Phi(s + eps),
eta_bilineal = -2 u eps = O(lambda^2)   =>   Fisher O(lambda^4)   =>   kappa ~ lambda^6,
```

con la frase «la cópula es ciega al espacio plano; lo primero que ve cerca del horizonte es
curvatura × área del parche».

**Esa frase es la versión infinitesimal del Teorema C.** La parte separable de `log h` es
la que el Teorema C anula exactamente a todo `n`; por eso el score no arranca en orden `0`
ni en orden `1` sino en la primera contribución **no separable**, que es `O(lambda^2)`. El
exponente `lambda^6 = 2 + 2*2` deja de ser una coincidencia numérica: el `2` es el área y
el `4` es el cuadrado de la primera curvatura visible.

Ni WP6 modifica R2 ni R2 modifica WP6. Se corroboran, y esa corroboración es un control
independiente de ambos.

## 7. Alcance — lo que este resultado NO dice

1. **Solo cajas nulas.** Fuera de parches rectangulares en `(U,V)`, la forma del dominio
   entra en la cópula y **se mezcla con la curvatura**: el orden ve también la forma. Es
   coherente con el confundido masa-vs-forma ya registrado en este repositorio, y es la
   hipótesis literal del Lema 2.2.
2. **Planitud del parche, no del espaciotiempo.** No contradice el Teorema 3.2
   (el horizonte global no es funcional de un parche finito): la dicotomía es local.
3. **Solo `d=2`, deliberadamente.** No se afirma transferencia a `3+1`. El valor del
   resultado es precisamente que `d=2` es lo que la literatura de reconstrucción excluye.
4. **No es reconstrucción de horizonte.** Es identificabilidad de la clase conforme módulo
   reparametrización nula. Dirección opuesta al objetivo clausurado.
5. **Novedad no certificada.** La conexión causal set 2D ↔ permutación es folclore
   (Myrheim; BDJ, en `biblioteca/`). Lo que se propone como nuevo es la formulación por
   permutones y la dicotomía exacta. `NOVELTY_CERTIFIED = NO` hasta auditoría.

## 8. Estado

```text
LEMA_A_RANK_INVARIANCE          = PROVED (= Lema 2.2 del manuscrito)
PROP_B_SEPARABLE_IFF_FLAT       = PROVED (elemental + control por curvatura)
TEOREMA_C_INVISIBILIDAD_EXACTA  = PROVED (no usa permutones)
COROLARIO_ORBITA_G              = PROVED
TEOREMA_D_COMPLETITUD           = PROVED_MODULO_HKMMRS_2013_Y_GRUBEL_2024
PUENTE_E_POSET_VS_PERMUTACION   = OPEN (= bibliography_claims.md §5.3 UNSUPPORTED_GAP)
TESTIGO_COMPARABLES             = PROVED_SUFFICIENT_NOT_NECESSARY
CONSISTENCIA_CON_R2             = CORROBORADA_EN_AMBOS_SENTIDOS
NOVELTY_CERTIFIED               = NO
SEMILLAS = 0 · SIMULACION = NINGUNA · SELLO = INTACTO
```

**Próximo paso único.** Cerrar el puente E por la ruta (b) o la (a). Es lo único que
separa la dicotomía de estar completa a nivel del observable físico.
