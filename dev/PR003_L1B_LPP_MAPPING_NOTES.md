# PR-003 — L₁b-(b): ¿hereda el observable causal el régimen LPP/KPZ de Johansson? (dev analítico, sin código)

Nota de sandbox, **analítica, sin código, ningún claim, nada congelado.** Único paso autorizado
(usuario, esta sesión): formular rigurosamente el puente L₁b-(b) —"orden producto 1+1D ⇒ las
hipótesis del modelo LPP de Johansson aplican al observable causal de enlaces"— ANTES de tocar los
términos `D²` de L₁a. Razón estructural: toda la ruta de tasa de L₁a presupone ese puente; si falla,
afinar Berry–Esseen sería trabajo correcto sobre el objeto equivocado. **L₁a queda congelado** hasta
el resultado de esta nota. Companion: `dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md` §8–§9.

Tres desenlaces posibles (todos útiles): **(1) mapeo exacto** → L₁b-(b) = importar una cota
publicada; **(2) mapeo por dominación/comparación** → hay que probar una desigualdad intermedia
propia; **(3) no hay mapeo suficiente** → se detiene limpiamente la ruta KPZ antes de invertir en L₁a.

---

## 1. El observable de enlaces, exactamente

`Φ(ℓ) = #{ (x,y) ∈ P² : x⋖y ,  s(x) ≤ ℓ < s(y) }`,
- `s(z)` = altura = longitud de la cadena máxima desde elementos minimales hasta `z`;
- `x⋖y` = enlace de cobertura: `x≺y` y `∄ z: x≺z≺y`.

**Lectura geométrica clave (en coordenadas de cono `u=t−r, v=t+r`):** `x≺y ⇔ u_x≤u_y ∧ v_x≤v_y`
(orden producto). Un enlace `x⋖y` ⇔ `y` domina a `x` y el **rectángulo abierto de Alexandrov**
`(u_x,u_y)×(v_x,v_y)` está **vacío** de puntos de `P`. Es decir: **un enlace = un rectángulo
axis-aligned vacío con los dos puntos en las esquinas inferior-izquierda / superior-derecha.** `Φ(ℓ)`
cuenta esos rectángulos vacíos que cruzan el nivel `ℓ` del campo de altura `s`. Todo orden-only.

## 2. La configuración de puntos que induce el orden producto

`P` = Poisson(ρ) **uniforme** en el parche `(t,r)` (caja `[0,T_edge]×[r_center±R_edge/2]`,
`nachocausal/thresholds.py`; `numpy_sprinkle` usa `rng.poisson(intensity)` ⇒ **N es Poisson,
NO condicionado**). El cambio `u=t−r, v=t+r` es lineal (Jacobiano 2) ⇒ `P` es **Poisson uniforme**
sobre la imagen `R_uv` = la caja `(t,r)` **rotada 45°** (un rectángulo inclinado / "diamante") en el
plano `(u,v)`. Orden = orden producto sobre `R_uv`.

Dos consecuencias que **disuelven** preocupaciones del informe para el NULL plano:
- **Condicionamiento: NINGUNO.** `N~Poisson` (no `N` fijo) ⇒ el cálculo de operadores diferencia de
  TY (Mecke/Slivnyak) aplica directo; no hay correlaciones espurias por condicionar a `|C|=N`.
- **Geometría no homogénea: NINGUNA en el null.** Poisson uniforme en `(u,v)` ⇒ homogeneidad
  **exacta** en el bulk. La no-homogeneidad es una preocupación del lado SEÑAL (Schwarzschild,
  densidad de relaciones variable), NO del null. L₁ es el null ⇒ no aplica.

## 3. El funcional de caminos crecientes correspondiente

`s(x) = L_{R}(∂⁻ → x)` := nº máximo de puntos de `P` en una cadena creciente (en ambas coords) desde
la **frontera inferior-izquierda** `∂⁻` de `R_uv` hasta `x`. Esto es **exactamente** la percolación
de último paso (LPP) / subsecuencia creciente más larga con condición inicial sobre `∂⁻`.
**Identidad, no aproximación:** cadena máxima en orden producto = LIS = valor LPP (Surya LRR §4.3;
BDJ 1999). El flujo `Φ(ℓ)` es un **funcional del conjunto de nivel `{s=ℓ}`** del campo de altura LPP
**más** la estructura local de rectángulos vacíos (enlaces) que lo cruzan.

## 4. Qué hipótesis de Johansson 2000 se satisfacen literalmente

Johansson 2000, *Transversal fluctuations for increasing subsequences on the plane*: puntos de
Poisson en el plano/rectángulo, camino maximal de último paso, prueba el **exponente transversal
2/3** (el camino maximal de `(0,0)` a `(n,n)` se mantiene en `n^{2/3+o(1)}` del eje).

| Hipótesis de Johansson | ¿Aplica al observable causal? |
|---|---|
| Puntos de Poisson en el plano | **Sí, exacto** (Poisson uniforme en `(u,v)`, §2) |
| LPP / orden producto | **Sí, exacto** (identidad §3) |
| Fluctuación transversal del camino maximal ÚNICO a un extremo | **Sí, en el bulk** — da el radio de localidad `ℓ^{2/3}` para determinar `s(z)` (el insumo del §8) |
| Condición inicial punto-a-punto (narrow wedge, `(0,0)→(n,n)`) | **NO literal** — la nuestra es CI sobre la **frontera** `∂⁻` (tipo plana). El exponente 2/3 es universal en la CI, pero la **forma de la cola y las constantes** dependen de la CI (narrow-wedge→GUE; flat→GOE; stationary→Baik–Rains). |
| Régimen asintótico `n→∞` | **NO literal** — parche finito, correcciones `O(n^{−·})` |

## 5. Diferencias: parche finito, bordes, condicionamiento, geometría

- **Condicionamiento:** ninguno (§2). ✓ dissolved.
- **Geometría no homogénea:** ninguna en el null (§2). ✓ dissolved.
- **Parche finito + bordes [REAL, = C4]:**
  - `R_uv` es un **rectángulo inclinado**; en las **esquinas** el ancho transversal →0. La esquina
    inferior es un genuino narrow-wedge punto-a-punto; los bordes laterales imponen CI de frontera.
  - El corte bulk (`s` = mediana) está en el **interior** ⇒ el teorema de fluctuación transversal
    aplica AHÍ; pero la **membrana** `{s=ℓ}` corre de borde a borde y sus extremos cerca de las
    paredes laterales sienten efectos de tamaño finito / borde (la preocupación lenticular C4).
  - Asintótica de Johansson es `n→∞`; `N≤1620` del probe da correcciones no despreciables.

## 6. ¿Exacto / por comparación / heurístico? — el desenlace

| Pieza | Estatus del mapeo |
|---|---|
| `s(x)` ↔ valor LPP | **EXACTO** (identidad de orden, §3) |
| Localidad de un camino (insumo `ψ(r)` del §8 / L₁b integrabilidad) | **POR COMPARACIÓN** a Johansson 2000: escala 2/3 exacta en bulk; **forma de cola y CI-plana NO literales** |
| Estructura de correlación del flujo / **condición de 4-tuplas de TY Def. 2.3** (multi-punto, BL-loc) | **NO cubierto por Johansson 2000** — requiere correlaciones espaciales del campo de altura a lo largo del nivel (**proceso de Airy₂**: Prähofer–Spohn 2002; Corwin–Quastel–Remenik). Sólo **heurístico** vía universalidad KPZ por ahora. |

**Desenlace: (2) mapeo por dominación/comparación, con frontera nítida.** La ruta KPZ **NO se
detiene** (desenlace 3 evitado): la pieza de un-camino del §8/L₁b tiene backbone real (Johansson
2000, por comparación, bulk, con caveat CI-plana). PERO se identifica con precisión la pieza que
Johansson NO da: **TY Def. 2.3 exige cercanía `d_BL` de 4-TUPLAS de scores — un enunciado
multi-punto — que la fluctuación de un solo camino de Johansson no provee.** Eso necesita la
**decorrelación espacial del campo de altura a lo largo del conjunto de nivel (proceso de Airy₂)**,
una cita/desigualdad DISTINTA, aún no anclada.

## 7. Consecuencias para el programa L₁ (qué cambia, qué no)

- **L₁b integrabilidad (un-camino, `ψ(r)`):** queda **condicional a Johansson 2000 por comparación**
  (escala 2/3) + el caveat de CI-plana (forma de cola). Ya no es "analogía KPZ" desnuda; tiene un
  teorema detrás para la ESCALA. Sigue sin ser teorema cerrado por la forma de cola (ver
  `..._NULL_LAW_NOTES.md` §8.2, [UNVERIFIED]) y la CI.
- **L₁b-(b) propiamente (aplicabilidad del modelo):** **resuelto como desenlace (2)** — mapeo por
  comparación, NO exacto. La pieza de un-camino mapea; la pieza **multi-punto (Def. 2.3) NO**, y se
  nombra el insumo faltante: proceso de Airy₂ / correlaciones espaciales del nivel.
- **L₁a (tasa, `D²`):** **permanece congelado**, pero ahora con un objetivo más claro: la tasa
  Berry–Esseen no depende sólo de Johansson (un-camino) sino de la decorrelación multi-punto. Antes
  de los `D²` hay que **anclar/comparar las correlaciones de Airy₂** o probar una desigualdad de
  decorrelación propia para el flujo de rectángulos vacíos a lo largo del nivel.
- **Posible atajo [especulativo]:** el flujo de enlaces = rectángulos vacíos cruzando el nivel
  (§1) es un objeto Poisson explícito; quizá la decorrelación a 1er orden (Var) y la condición de
  4-tuplas puedan acotarse DIRECTAMENTE por vaciedad de rectángulos + dominación, sin invocar todo el
  aparato de Airy₂. A explorar sólo si se decide continuar.

**Re-grado:** sin cambio. **OPEN–CONTINGENT** sigue bien puesto: el desenlace (2) ni cierra L₁b como
teorema ni lo devuelve a IMPOSSIBLE. No hay base para elevar a `OPEN` pleno.

## 8. Backing

- Observable, orden producto, link=rectángulo vacío: `dev/PR003_BL_LOCALIZATION_NULL_LAW_NOTES.md`
  §8.1, §9.1; Surya LRR §4 (orden 2D); `nachocausal/generator.py` (`numpy_sprinkle` N~Poisson,
  `past_matrix_fast` MINK cono).
- Identidad cadena-máxima = LPP/LIS: Surya §4.3; BDJ 1999 (*Shape Fluctuations and Random Matrices*).
- Escala transversal 2/3: Johansson 2000, *Transversal fluctuations for increasing subsequences on
  the plane* (NO en biblioteca; primaria leída externamente) — escala exacta, forma de cola NO la
  cúbica usada en §8 (su estimación ~`exp(−c r⁶/N⁴)`, ver `..._NULL_LAW_NOTES.md` §8.2 [UNVERIFIED]).
- Multi-punto / nivel: proceso de Airy₂ — Prähofer–Spohn 2002; Corwin–Quastel–Remenik (NO en
  biblioteca; **[UNVERIFIED]**, citados como el insumo faltante, no como respaldo).
- TY Def. 2.3 (condición de 4-tuplas, `d_BL`): `biblioteca/2605.23292v1.pdf` p.8.
- Decisión de scope (L₁b-(b) primero, L₁a congelado): instrucción del usuario, esta sesión.
