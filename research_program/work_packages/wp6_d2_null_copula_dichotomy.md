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

**Lo que NO toca el hueco.** El Teorema C (invisibilidad) es inmune: un engrosamiento
preserva la igualdad de leyes. La mitad no-go de la dicotomía está cerrada sin (E).

### 5.2bis (E) es FALSA — contraejemplo exhaustivo en `n=4`

`[PROVED — enumeración exhaustiva determinista]`
Ejecutable: `dev/r3_bridge_e_fibers.py` (sin aleatoriedad, sin semillas, no escribe).

Enumerando `S_n` y clasificando `P_sigma` por isomorfismo:

```
 n   |S_n|  clases   histograma de |fibra|   fibra == órbita inversa?
 1       1       1   1:1                     SI
 2       2       2   1:2                     SI
 3       6       5   1:4, 2:1                SI
 4      24      16   1:9, 2:6, 3:1           NO  (1 clase)
```

El contraejemplo mínimo es la clase del poset **«una 2-cadena más dos puntos aislados»**,
cuya fibra tiene **tres** elementos:

```
3421,  4231 (auto-inversa),  4312 = 3421^{-1}
```

Comprobación directa: `P_3421` tiene la única relación `1<2`; `P_4231` la única relación
`2<3`; `P_4312` la única relación `3<4`. Los tres posets son isomorfos, y `4231` no es la
inversa de ninguno de los otros dos.

**Consecuencia bibliográfica.** Esto refuta la unicidad del realizador salvo intercambio
para posets de dimensión 2, y con ello el ítem `docs/bibliography_claims.md` §5.3 deja de
ser una cita pendiente: el enunciado era falso.

**Y no es una contribución.** Casi con certeza es folclore: la estructura de las
orientaciones transitivas de un grafo de comparabilidad está caracterizada por la
**descomposición modular de Gallai (1967)**, y el grafo de incomparabilidad del testigo es
`K_4` menos una arista, el caso descomponible de manual. El valor de la enumeración fue
**interno** —evitar que este WP persiguiera un lema falso— y así debe presentarse.
`[UNVERIFIED: Gallai 1967 y Golumbic no leídos en primaria; que esto sea clásico es él
mismo una conjetura bibliográfica.]`

### 5.4 Reformulación correcta de (E), y la reducción que deja

(E) como unicidad del realizador era **suficiente pero no necesaria**. Lo que la dicotomía
necesita es mucho más débil: no injectividad en todas partes, sino **injectividad en un
único punto**.

> **(E')** Si las densidades de patrones de poset de `C` coinciden con las de `Pi` a todo
> `n`, ¿es `C = Pi`?

La enumeración da la estructura fina de la obstrucción a nivel `n=4`. Las 16 ecuaciones de
clase sobre 24 incógnitas dejan un núcleo de dimensión 8, y ese núcleo se descompone:

- **9 fibras unitarias** — todas de permutaciones auto-inversas: sus densidades quedan
  **forzadas** a `1/24`. Sin libertad.
- **6 fibras de tamaño 2** — todas pares inversos exactos `{sigma, sigma^{-1}}`. Su
  dirección libre es `d(sigma) - d(sigma^{-1})`, **impar bajo transposición**: es
  exactamente la ambigüedad `U <-> V`, que ya sabíamos inevitable y que no rompe nada,
  porque `C` y `C^T` tienen idénticas leyes de poset por construcción.
- **1 fibra de tamaño 3** — aporta 2 dimensiones, de las cuales una es impar y **una es
  par**: `d(3421) = d(4312) = 1/24 + b`, `d(4231) = 1/24 - 2b`.

**Toda la obstrucción par a nivel de 4 puntos es, por tanto, exactamente unidimensional: el
parámetro `b`.** Restringido a permutones simétricos (`C = C^T`), que anulan todas las
direcciones impares, `b` es la **única** libertad.

**Palanca disponible.** Si se cita que un permutón con todas las densidades de tamaño 4
iguales a `1/24` es necesariamente `Pi` —resultado de cuasialeatoriedad de permutaciones
caracterizada por densidades de 4 puntos, atribuido a Král'–Pikhurko (2013)
`[UNVERIFIED: citado de memoria, requiere verificación en primaria como se hizo con
HKMMRS y Grübel]`— entonces (E') se reduce a una pregunta finita y concreta:

> ¿Existe un permutón, no uniforme, con `b != 0` y todas las demás densidades de tamaño 4
> iguales a `1/24`, que además siga coincidiendo con `Pi` a todo `n > 4`?

Si **no existe**, la dicotomía queda completa a nivel del observable físico. Si **existe**,
el resultado es igual de publicable y más llamativo: sería un parche **curvo exactamente
indistinguible del plano por orden a todo `n`**, es decir una ceguera de curvatura del
canal, y el Teorema C dejaría de ser el límite máximo de invisibilidad.

En ambas ramas hay resultado. Eso es lo que hace que (E') merezca el ataque.

### 5.5 Rutas

- **(a) Directa.** Decidir (E') por álgebra de banderas / construcción explícita sobre la
  única dirección par `b`. Es finita y no depende de nada geométrico.
- **(b) Bibliográfica.** Verificar Král'–Pikhurko en primaria; y leer Janson, *Poset limits
  and exchangeable random posets*, Combinatorica **31** (2011) 529–563, que es la teoría de
  límites del objeto exacto de este WP —posets aleatorios intercambiables— y probablemente
  ya contiene el enunciado de unicidad que (E') necesita. `[UNVERIFIED: no leído]`.
  **Kelly–Trotter / Trotter dejan de ser la ruta**: preguntaban por la unicidad del
  realizador, que §5.2bis acaba de refutar.

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
5. **Novedad no certificada, y el riesgo es alto pieza por pieza.** Triaje honesto, de
   mayor a menor probabilidad de que ya exista:

   | Pieza | Riesgo de ser previo | Por qué |
   | --- | --- | --- |
   | Lema A (invariancia por rangos) | **Casi seguro previo** | Teoría de cópulas estándar |
   | Prop. B (separable ⟺ plano) | **Seguro previo** | Relatividad 2D de manual |
   | Causal set 2D ⟷ permutación; plano ⟷ uniforme | **Seguro previo** | Folclore CST (Myrheim; BDJ) |
   | §5.2bis, testigo `n=4` | **Casi seguro previo** | Descomposición modular de Gallai |
   | Teorema C (invisibilidad exacta a todo `n`) | **Alto** | Sale en dos líneas de lo anterior |
   | Clase de invisibilidad = órbita de `Diff+ x Diff+` | Medio | En el continuo es clásico; en el canal discreto, menos claro |
   | Teorema D (completitud vía permutones) | Medio-bajo | El permutón es de 2013; aplicarlo aquí es el paso plausiblemente nuevo |
   | §5.4, reducción de (E') a una dirección par | Bajo | Específico de este cálculo |

   **Objetivo prioritario de la auditoría de novedad, que el repositorio aún no tiene
   fichado:** la literatura de **órdenes aleatorios de dimensión 2** — Winkler, *Random
   orders*; Brightwell, *Models of random partial orders*; Bollobás–Brightwell. Si alguien
   estudió órdenes 2-dimensionales aleatorios con densidad no uniforme, es ahí donde el
   Teorema C ya puede estar escrito. Es un objetivo mucho más afilado que el coto genérico
   «graphon/poset-kernel» de `docs/hoja_de_ruta_30_jul_2026.md:131`.
   `[UNVERIFIED: ninguno leído; no están en biblioteca/.]`

   `NOVELTY_CERTIFIED = NO`. Y por la regla fundacional del repositorio, esto **no lo puede
   firmar ni un comité interno ni esta sesión**: exige búsqueda en primaria.

## 8. Estado

```text
LEMA_A_RANK_INVARIANCE          = PROVED (= Lema 2.2 del manuscrito)
PROP_B_SEPARABLE_IFF_FLAT       = PROVED (elemental + control por curvatura)
TEOREMA_C_INVISIBILIDAD_EXACTA  = PROVED (no usa permutones)
COROLARIO_ORBITA_G              = PROVED
TEOREMA_D_COMPLETITUD           = PROVED_MODULO_HKMMRS_2013_Y_GRUBEL_2024
PUENTE_E_UNICIDAD_REALIZADOR    = FALSE_WITH_EXPLICIT_WITNESS_N4
BIBLIOGRAPHY_CLAIMS_5_3         = ANSWERED_NEGATIVELY_NO_LONGER_AN_OPEN_CITATION
PUENTE_E_PRIMA_INYECTIVIDAD_EN_PI = OPEN_REDUCED_TO_ONE_EVEN_DIRECTION_AT_N4
KRAL_PIKHURKO_2013              = UNVERIFIED_CITED_FROM_MEMORY
JANSON_POSET_LIMITS_2011        = UNVERIFIED_NOT_READ_LIKELY_RIGHT_SOURCE
TESTIGO_COMPARABLES             = PROVED_SUFFICIENT_NOT_NECESSARY
CONSISTENCIA_CON_R2             = CORROBORADA_EN_AMBOS_SENTIDOS
NOVELTY_CERTIFIED               = NO
SEMILLAS = 0 · SIMULACION = NINGUNA · SELLO = INTACTO
```

**Próximo paso único.** Decidir (E') sobre su única dirección par `b`, por §5.5(a) o (b).
Las dos ramas del resultado son publicables: si `b` no es realizable, la dicotomía se
completa a nivel del observable físico; si lo es, existe un parche curvo exactamente
invisible al orden a todo `n`, que es un enunciado más fuerte que el propio Teorema C.
