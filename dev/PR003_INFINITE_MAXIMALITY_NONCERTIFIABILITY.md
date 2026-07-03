# PR-003 — No-certificabilidad de la maximalidad futura en historias infinitas 2D (teorema combinatorio)

Status: **dev, nota matemática, sin código en el path sellado, sin freeze, sin claim físico.**
Extiende al caso infinito la ambigüedad de maximalidad ya registrada en capa finita/acotada
(Alloy 001, `docs/alloy/alloy_verification_001_completion-maximality-counterexample.md`;
`dev/PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md`). Es un **teorema combinatorio sobre
2-órdenes**, no un no-go físico: no involucra sprinkling, manifoldlikeness ni Schwarzschild
(la cadena "combinatorial counterexample does NOT imply physical no-go" de
`PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md` sigue vigente).

Por qué un documento nuevo: ningún documento existente trata extensiones infinitas; el anfitrión
natural (`PR003_COMPLETION_TRUNCATION_NONIDENTIFIABILITY.md`) está delimitado a la proposición
finita sobre decisiones de interfaz y su registro Alloy, y anexarle un teorema autocontenido con
prueba desbordaría su rol de nota-insumo de comité.

---

## 1. Veredicto

```text
VERDICT = PROVED
```

Probado en la formulación uniforme (∀ e ∈ Max(O)), con extensiones contables, localmente
finitas, de dimensión Dushnik–Miller ≤ 2, con `O` como partial stem, y bajo la lectura **más
fuerte** razonable de "extensión futura" (todo elemento nuevo estrictamente por encima de algún
elemento de `O`). Prueba explícita por realizadores de dos órdenes lineales en §4–§5.

## 2. Enunciado definitivo

> **Teorema (ambigüedad infinita de la maximalidad futura, clase 2D).**
> Sea `O` un poset finito con `dim_DM(O) ≤ 2` y `|O| ≥ 2`, y sea `e ∈ Max(O)` **arbitrario**.
> Existen posets `Q_A`, `Q_B`, ambos contables e infinitos, tales que:
>
> 1. `O` es subposet inducido de cada uno (ninguna relación nueva entre elementos de `O`);
> 2. cada uno es extensión futura de `O` en el sentido fuerte: ningún elemento nuevo está por
>    debajo de un elemento de `O` (⇒ `O` es partial stem de cada uno), y además todo elemento
>    nuevo está estrictamente por encima de algún elemento de `O`;
> 3. `dim_DM(Q_A) ≤ 2` y `dim_DM(Q_B) ≤ 2`;
> 4. ambos son localmente finitos (de hecho, past-finitos: todo pasado es finito);
> 5. `e ∉ Max(Q_A)` y `e ∈ Max(Q_B)`;
> 6. ambos admiten un etiquetado natural (crecimiento secuencial en el que cada elemento es
>    maximal al nacer).

Aclaraciones exigidas por el encargo:

- **Vale para cada maximal:** sí — la construcción toma `e ∈ Max(O)` arbitrario. La hipótesis
  `|O| ≥ 2` se usa en el Lema 1 para excluir que `e` sea simultáneamente menor global y maximal
  en un poset no unitario. La hipótesis `e ∈ Max(O)` se usa dos veces: (1) en el Lema 1, en esa
  misma contradicción; y (2) en la Rama `Q_B` (caso 6), para concluir que, al no haber elementos
  nuevos por encima de `e` (caso 5) ni viejos por encima de `e` (por ser `e` maximal en `O`),
  ningún elemento — viejo ni nuevo — puede destruir su maximalidad.
- **Contables:** sí — `|Q_α| = |O| + ℵ₀`.
- **Localmente finitas:** sí — past-finitas, luego todo intervalo `I[x,y]` es finito (definición
  BLMS, dossier `docs/bibliography_claims.md` §2.3).
- **`O` es stem:** sí, *partial stem* en el sentido de Rideout (gr-qc/0212064): "a finite
  subcauset S which contains its own past"
  (`biblioteca/derived-md/Dynamics_of_Causal_Sets_arXiv_gr-qc0212064.md:353`). En `Q_A` es además
  *full stem*; en `Q_B` en general **no** lo es (contraejemplo: `O` = 3-cadena, §5 observación).
- **Dimensión:** Dushnik–Miller (realizador = intersección de órdenes lineales; primaria leída,
  dossier §5.1). La definición vale para posets infinitos sin cambio (DM 1941 es transfinito).
- **Historia completa vs prolongación abstracta:** cada `Q_α` es un poset infinito completo de la
  clase (contable, localmente finito, `dim ≤ 2`) — no un paso único. Que esa clase agote las
  "historias físicas" NO se afirma: eso requeriría manifoldlikeness/sprinkling, fuera de alcance
  (§7).
- **`|O| = 1`:** excluido del teorema. Bajo la lectura débil de "futura" (solo "nada nuevo por
  debajo de `O`"), `Q_B = {e} ⊔ ω` (cadena disjunta) da el resultado también para `|O| = 1`; bajo
  la lectura fuerte adoptada no hay testigo `w ≠ e` disponible y la rama `Q_B` no se construye.

## 3. Definiciones

Sea `P = (X, <)` un poset (orden estricto). Notación: `Max(P) = {x : ∄y, x < y}`.

- **Extensión lineal** de `P`: orden total `L` sobre `X` con `< ⊆ L`. **Realizador** de tamaño 2:
  par `(L1, L2)` de extensiones lineales con `< = L1 ∩ L2`. **`dim_DM(P) ≤ 2`** ⟺ existe tal par
  (Dushnik–Miller 1941, §2.1–2.2; leído en primaria, `docs/bibliography_claims.md` §5.1; vale
  para cardinalidad arbitraria).
- **Localmente finito**: `|I[x,y]| < ∞` para todo `x,y`, con `I[x,y] = {z : x ≤ z ≤ y}` (BLMS
  vía Surya 2019, dossier §2.3). **Past-finito**: `|{z : z < x}| < ∞` ∀x. Past-finito ⇒
  localmente finito.
- **Extensión futura** de `O` (lectura débil): `Q ⊇ O` con `O` subposet inducido y ningún
  `q ∈ Q∖O` con `q < x` para algún `x ∈ O` — equivalentemente, `O` es down-set de `Q`, i.e.
  *partial stem* (Rideout, cita arriba) al ser finito. (Lectura fuerte, adoptada): además todo
  `q ∈ Q∖O` satisface `x < q` para algún `x ∈ O`. La definición del repo de completación
  admisible (comité 010/012; `dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md` §3–4) no fija la
  versión infinita; ambas construcciones satisfacen la fuerte, así que la elección no afecta el
  veredicto.
- **Etiquetado natural**: biyección `X → {0,1,2,…}` con `x < y ⇒ label(x) < label(y)` — i.e. una
  extensión lineal de tipo ω; equivale a una historia de crecimiento donde cada elemento es
  maximal al nacer (Rideout–Sorkin 1999,
  `biblioteca/derived-md/Rideout_Sorkin_1999_...md:60,64,146`).
- Distinción estricta usada en todo el documento: *minimal* (nada debajo) ≠ *menor global*
  (debajo de todos) ≠ *maximal* (nada encima) ≠ *mayor global* (encima de todos).

## 4. Lema de posición en el realizador (el punto lógico)

> **Lema 1.** Sea `O` finito, `|O| ≥ 2`, `dim_DM(O) ≤ 2`, `e ∈ Max(O)`, y `(L1, L2)` cualquier
> realizador. Entonces existe `i ∈ {1,2}` y `w ∈ O`, `w ≠ e`, con `w <_{Li} e`.

*Prueba.* Supóngase lo contrario: `e` es el primer elemento de `L1` **y** de `L2`. Entonces para
todo `x ≠ e`: `e <_{L1} x` y `e <_{L2} x`, luego `e < x` en `O = L1 ∩ L2` — es decir, `e` es el
**menor elemento global** de `O`. Como `|O| ≥ 2`, existe `x ≠ e` con `e < x`, contradiciendo
`e ∈ Max(O)`. ∎

(Nota de rigor: el paso intermedio es "menor global", no "no minimal" — un elemento puede ser
minimal y maximal a la vez; lo imposible para `|O| ≥ 2` es ser *menor global* y maximal.)

## 5. Prueba

Fijar un realizador `(L1, L2)` de `O` (existe por `dim_DM(O) ≤ 2`). Sea `H = {h_1, h_2, …}` un
conjunto contable nuevo.

### Rama `Q_A` (e pierde la maximalidad)

Defínase `Q_A := O ⊕ ω` (suma lineal): `x < h_n` para todo `x ∈ O` y todo `n`; `h_m < h_n` para
`m < n`; sin relaciones nuevas dentro de `O`.

- **`dim ≤ 2`:** `(L1 ⊕ ω, L2 ⊕ ω)` es realizador — pares viejos-viejos: intersección
  `L1 ∩ L2 = O`; viejo-nuevo: `x` antes de `h_n` en ambos ⟺ `x < h_n` en `Q_A` ✓; nuevo-nuevo:
  ω en ambos ✓. La intersección es exactamente `Q_A`.
- **Inducido / futura fuerte / stem:** sin relaciones nuevas en `O`; ningún `h_n` debajo de
  ningún viejo; todo `h_n` encima de todo `O` (en particular encima de algún elemento). `O` es
  partial stem, y de hecho **full stem** (todo `h_n` sucede a un maximal de `O`).
- **`e ∉ Max(Q_A)`:** `e < h_1`. ✓
- **Past-finito:** `past(h_n) = O ∪ {h_1,…,h_{n−1}}` finito; `past(x ∈ O) ⊆ O`. ✓
- **Etiquetado natural:** `L1`-orden sobre `O` seguido de `h_1, h_2, …` es una extensión lineal
  de tipo ω; cada elemento es maximal al nacer (todo lo que lo domina nace después). ✓

### Rama `Q_B` (e sigue maximal)

Por el Lema 1, renombrando los dos órdenes si hace falta, existe `w ≠ e` con `w <_{L2} e`.
Defínanse dos órdenes lineales sobre `O ∪ H`:

- `M1 := L1 ⊕ (h_1 < h_2 < ⋯)` — todos los nuevos después de todos los viejos;
- `M2 :=` `L2` con la cadena insertada inmediatamente después de `w`: tipo de orden
  `(segmento inicial de L2 hasta w) ⊕ ω ⊕ (resto de L2)`. Nótese que `e` está en el resto
  (porque `w <_{L2} e`), es decir, **después** de toda la cadena en `M2`.

Defínase `Q_B := M1 ∩ M2`. Verificación por casos de pares:

1. **Viejos-viejos:** la inserción no altera el orden relativo de los viejos en ninguno de los
   dos, luego la intersección restringida a `O` es `L1 ∩ L2 = O` — subposet inducido, sin
   relaciones nuevas. ✓
2. **Nuevos-nuevos:** `h_m < h_n ⟺ m < n` en ambos — cadena. ✓
3. **Nuevo debajo de viejo:** `h_n <_{M1} x` es falso para todo `x ∈ O` (nuevos después de
   viejos en `M1`) ⇒ ningún nuevo debajo de ningún viejo. `O` es down-set ⇒ **partial stem**. ✓
4. **Viejo debajo de nuevo:** `x < h_n ⟺ x <_{M2} h_n ⟺ x ≤_{L2} w`. En particular
   `w < h_n` para todo `n` (**testigo**: futura fuerte ✓), y el `O`-pasado de cada `h_n` es el
   segmento inicial `I_w = {x : x ≤_{L2} w}`, que es down-set de `O` (todo segmento inicial de
   una extensión lineal lo es).
5. **`h_n` incomparable con `e`:** `e ∉ I_w` (pues `w <_{L2} e` y `e ≠ w`) ⇒ `¬(e < h_n)`;
   `¬(h_n < e)` por el caso 3. ✓
6. **`e ∈ Max(Q_B)`:** nada viejo encima de `e` (caso 1 + `e ∈ Max(O)`); nada nuevo encima de
   `e` (caso 5). ✓
7. **`dim ≤ 2`:** `(M1, M2)` es por construcción un realizador de `Q_B`. ✓
8. **Past-finito:** `past(h_n) = I_w ∪ {h_1,…,h_{n−1}}` finito; `past(x ∈ O) ⊆ O`. ✓
9. **Etiquetado natural:** (`L1`-orden de `O`) seguido de `h_1, h_2, …` — extensión lineal de
   `Q_B` de tipo ω (viejos antes que nuevos es compatible por el caso 3); cada elemento maximal
   al nacer. ✓

*Observación (full stem):* `Q_B` no hace de `O` un full stem en general: con `O` = cadena
`a<b<c`, `e=c`, `L2=(a,b,c)`, `w=b`, el pasado-en-`O` de los `h_n` es `{a,b}`, que no contiene
ningún maximal de `O`. El teorema pide partial stem y eso sí se cumple. ∎

### Corolario 1 (testigo finito admisible — resultado general para el registro de maximalidad)

Las truncaciones `Q_A^{(1)}, Q_B^{(1)}` (un solo `h_1`) son completaciones **finitas** de un
elemento que voltean la maximalidad de `e`, probando directamente — no por herencia de ninguna
clase de admisibilidad externa — que cada rama satisface: `O` queda como subposet inducido;
ningún elemento nuevo queda por debajo de un elemento observado; el elemento nuevo tiene pasado
observado no vacío (`Q_A^{(1)}`: todo `O`; `Q_B^{(1)}`: `w`); `O` es partial stem de la
completación; la inclusión `O ⊆ Q_α^{(1)}` es convexa (ningún elemento nuevo entre dos
observados — inmediato del caso 3: nada nuevo debajo de nada viejo); `dim_DM(Q_α^{(1)}) ≤ 2`
(realizador explícito en cada rama); y el elemento nuevo es maximal al ser añadido — con `e`
perdiendo la maximalidad en `Q_A^{(1)}` y conservándola en `Q_B^{(1)}`. Estas propiedades están
ancladas en las definiciones de §3 (partial/full stem — Rideout gr-qc/0212064; `dim_DM` —
Dushnik–Miller 1941) y en la prueba explícita de §4–§5; no se afirma que las truncaciones
satisfagan la clase de completación admisible C1 (𝔄) adjudicada por comité 012 para el registro
de interfaz (Alloy 002) — ese es un registro distinto, y esta prueba es autónoma de él.

Contraste: el testigo Alloy 001 lograba el flip solo con una completación que **violaba
convexidad** (su completación B interpone `E0` entre los observados `E2 < E3`;
`dev/alloy/product_order_check_alloy002_witness_note.md` §4 documenta el mismo defecto en el
testigo 002, con traza idéntica). Este corolario da el flip dentro de la clase convexa/stem, para
todo `O` finito con `dim_DM(O) ≤ 2` y todo `e ∈ Max(O)` — no solo para la instancia puntual de 4
elementos de Alloy 001.

### Corolario 2 (no-certificabilidad desde observación finita)

No existe ninguna función `F(O, e)` del stem finito observado (ni de ningún dato derivable solo
de su orden) tal que `F(O,e) = 1 ⟺ e ∈ Max(Q)` para toda historia `Q` contable, localmente
finita, `dim_DM ≤ 2`, con `O` como partial stem: para cada `(O, e)` con `|O| ≥ 2`,
`dim_DM(O) ≤ 2`, `e ∈ Max(O)`, ambas respuestas se realizan (`Q_A`, `Q_B`). La maximalidad en la
historia completa **no factoriza a través del stem** en esta clase.

## 6. Tabla de obligaciones

| Propiedad | `Q_A` | `Q_B` | Garantizada por |
|---|---|---|---|
| Restricción inducida = `O` | ✓ | ✓ | §5 caso viejos-viejos (intersección = `L1 ∩ L2`) |
| Extensión futura (débil: nada nuevo bajo `O`) | ✓ | ✓ | `M1` pone nuevos tras viejos (caso 3) |
| Extensión futura (fuerte: nuevo ⇒ sobre algún viejo) | ✓ (sobre todo `O`) | ✓ (sobre `w`) | construcción / caso 4 |
| `O` partial stem | ✓ (y full stem) | ✓ (full stem NO en general) | caso 3; observación §5 |
| Infinitud | ✓ | ✓ | `H ≅ ω` |
| Contabilidad | ✓ | ✓ | `|O| + ℵ₀` |
| Localidad finita | ✓ | ✓ | past-finitud (§5, punto 8 / rama A) |
| `dim_DM ≤ 2` | ✓ | ✓ | realizadores explícitos `(L1⊕ω, L2⊕ω)` / `(M1, M2)` |
| Estado de `e` | NO maximal (`e < h_1`) | maximal (caso 6) | §5 |
| Incomparabilidad `h_n ∥ e` (solo `Q_B`) | n/a | ✓ | caso 5 (`e ∉ I_w`) |
| Crecimiento con nacimientos maximales | ✓ | ✓ | etiquetado natural explícito (punto 9) |
| Convexidad del observado (obligación repo §4) | ✓ | ✓ | caso 3 (nada nuevo debajo de viejo ⇒ nada interpuesto) |
| Uniformidad ∀`e ∈ Max(O)` | ✓ | ✓ | Lema 1 solo usa `|O| ≥ 2` y `e` maximal |

## 7. Alcance causal-set (qué es y qué NO es este resultado)

- **Invariancia bajo isomorfismos:** el enunciado y la construcción son invariantes por
  isomorfismo de órdenes (dependen solo de `(O, <)` y de la elección de un realizador; testigos
  distintos dan `Q_B` isomorfos o no, pero la *existencia* afirmada es invariante).
- **Teorema combinatorio sobre 2-orders:** eso es exactamente lo probado — nada más.
- **No-certificabilidad desde observación finita:** Corolario 2, probado, con la cuantificación
  exacta sobre la clase (contable + localmente finito + `dim ≤ 2` + partial stem).
- **Observable covariante en una dinámica causal-set:** NO establecido. Que "e es maximal para
  siempre" sea un evento medible en la σ-álgebra de stems del covtree, y qué medida le asigne
  una dinámica CSG, no se toca aquí (misma frontera que el registro L₆/rogue-sets,
  `dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md`). Este teorema solo muestra que ambos resultados
  son *cinemáticamente* realizables.
- **Embebibilidad / aproximación a Minkowski 1+1:** NO afirmada ni usada. `dim_DM ≤ 2` no está
  probado equivalente a manifoldlikeness 1+1D en este proyecto (la Prop. 7.3 de
  `dev/PR003_RELATIONAL_HORIZON_DEFINITION_NOTES.md` es unidireccional y condicional; el dossier
  §2.6 prohíbe además confundir dimensión Myrheim–Meyer con dimensión de orden). `Q_A`, `Q_B`
  son 2-órdenes; nadie afirma que sean sprinklings.
- **Relación con la capa física del proyecto:** las obligaciones `UNDEFINED` de la clase 𝔄
  (compatibilidad Schwarzschild, manifoldlikeness/sprinkling) no pueden evaluarse sobre `Q_A`,
  `Q_B` porque siguen sin definición ejecutable. `PHYSICAL_LAYER_OPEN` se mantiene sin cambios.

## 8. Registro de validación

- Chequeo de sanidad ejecutable (NO es prueba; ayuda de auditoría): script en scratchpad de
  sesión (`check_infinite_maximality_construction.py`) construyó `Q_A^{(N)}, Q_B^{(N)}`,
  `N ∈ {1,2,3}`, para 6 posets base (2-anticadena, 2-cadena, V, 3-cadena, N-poset, diamante) y
  cada `e ∈ Max(O)`, verificando exhaustivamente: SPO, `O` inducido, partial stem, convexidad,
  `dim_DM ≤ 2` (búsqueda exhaustiva de realizadores), estado de `e`, incomparabilidad `h ∥ e`,
  testigo `w < h`, y etiquetado natural. Resultado: **54/54 OK, 0 fallos**. El teorema general
  se sostiene en la prueba de §4–§5, no en este experimento finito.
- Trabajo previo verificado: la versión infinita no aparece en ningún documento del repo
  (barridos `Q_A|Q_B|stem`, `maximalidad|certificab`, `dim_DM|Dushnik` sobre `dev/`, `docs/`,
  `formal/`); el registro finito existente es Alloy 001/002 con testigos no convexos.
- Referencias usadas y su alcance comprobado: Dushnik–Miller 1941 (dimensión/realizador —
  primaria leída, dossier §5.1); BLMS/Surya (localidad finita — dossier §2.3); Rideout
  gr-qc/0212064 (partial/full stem — derived-md:353); Rideout–Sorkin gr-qc/9904062 (etiquetado
  natural — derived-md:60,64,146). Ninguna otra atribución de literatura.

## 9. Estado tras comité (registro de coexistencia)

`/comite` adjudicó `RETAIN_BOTH_WITH_NEW_STRONGER_COROLLARY` sobre si el par finito admisible
`(Q_A^{(1)}, Q_B^{(1)})` debía sustituir al testigo Alloy 001 como registro vigente de la capa
lógica de no-identificabilidad de maximalidad. Alloy 001 conserva su veredicto
(`ALLOY_COUNTEREXAMPLE_FOUND`) y su valor como testigo acotado verificado por herramienta
(`alloy exec`, scope `exactly 4 Element`); este documento no lo retracta ni lo sustituye
silenciosamente. El Corolario 1 se añade como resultado general, uniforme para todo
`e ∈ Max(O)`, y compatible con convexidad/stem. La capa física sigue `OPEN` y este documento no
la toca. Sin sprinklings, sin dinámica probabilística, sin promoción de selector.
