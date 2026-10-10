# S4W — auditoría matemática independiente del candidato de cinco capas

**Fecha:** 2026-10-10
**Objeto primario auditado:** `dev/S4W_5LAYER_KRETSCHMANN_CANDIDATE.md`, commit `15eb7a500f18abc401f3671edecc65a995ef3e89`
**Objeciones preliminares separadas:** `64aa326c1daa22000dbd21346c784c11a2a7d5cd`
**Brief cumplido:** `dev/S4W_5LAYER_INDEPENDENT_AUDIT_BRIEF.md`
**Documentos subsidiarios leídos:** `S4W_5LAYER_W2_COMPACT_PROOF.md`, `S4W_5LAYER_W1_SCHWARZSCHILD_C2_DERIVATION.md`, `S4W_5LAYER_W1_UNIFORM_REMAINDER_PROOF.md`, `S4W_5LAYER_AUDIT_PRECHECK_2026-09-15.md`

**Estado de esta auditoría:**

```text
INDEPENDENT_SESSION_AUDIT / WRITTEN_BY_CLAUDE
EXTERNALLY_BLIND_REVIEWED_BY_TWO_FAMILIES (deepseek-v4-pro, grok-4.6)  -> §11
PRIMARY_SOURCES_READ_DIRECTLY / NO_SIMULATION / NO_SEEDS / SEAL_UNTOUCHED
REV 2.1
```

Declaración de alcance de independencia, para que nadie la sobrelea: esta sesión **no**
escribió el candidato ni el precheck, y las fuentes primarias se leyeron directamente, no
por la narración del repo. La redactó **una sola casa** (Claude); por eso sus dos pasos de
juicio se mandaron después a dos familias distintas en revisión ciega sellada, que los
confirmaron y le encontraron cinco defectos, uno de ellos material (§11). **No** fue el
sanedrín: fueron dos encargos separados, por instrucción del PI. Donde un veredicto depende
de un juicio y no de una identidad verificable, se dice en el sitio.

Herramienta: álgebra simbólica (`sympy` 1.14.0 del `.venv` del repo, uso de solo lectura).
No se ejecutó `make dry-run`, `make gate`, `make op21-terminal`, ninguna simulación,
ninguna semilla. `nachocausal/thresholds.py` no se tocó (sha256 verificado post-auditoría:
`6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, idéntico al de
`docs/preregistration_002.md`).

---

## REVISIÓN 2 — 2026-10-10, mismo día, tras leer Pfeiffer 2022

La rev. 1 de este documento dejó `E_PRIOR_ART` abierto por no haber leído la tesis de
Christopher-Dustin Pfeiffer, *Higher curvature terms for Causal Sets: Extended proof and
generalization for the Causal Set d'Alembertian* (Master thesis, Univ. de Copenhague, NBI,
20 mayo 2022; supervisor Emil Bjerrum-Bohr, co-supervisora Astrid Eichhorn). Leída
completa. Cambia **dos** cosas, en direcciones opuestas:

1. **Prioridad: despejada.** No contiene antecedente exacto. Ver §6.3.
2. **`B_W2`: mi veredicto de la rev. 1 queda REVOCADO.** Pasa de `FAIL` a
   `PASS_CONDITIONAL`, y con ello cae `F2`. La tesis contiene la maquinaria que el §6 del
   candidato necesitaba y que yo di por inexistente. Ver §2 y §6.4.

El token global no cambia —el coeficiente sigue mal—, pero **la razón se encoge**: de "dos
problemas abiertos en la literatura" a "un cálculo que nadie ha hecho, con el bloqueo
retirado". Las secciones afectadas van marcadas `(rev.2)`. Lo que la rev. 1 decía se
conserva tachado en su sitio, no se borra.

---

## 0. Veredicto

```text
VERDICT = AUDIT_REQUIRES_MAJOR_FIX

A_ALGEBRA             = PASS
B_W2                  = PASS_CONDITIONAL          (rev.2; era FAIL en rev.1)
C0_GLOBAL_FINITUDE    = REGULATED_ONLY  (y la dependencia del corte NO es o(rho^-1/2))
C_W1_COEFFICIENT      = FAIL  (coeficiente NO determinado)
D_COVARIANT_STRUCTURE = FAIL  (en la afirmación 1: el integrando de Wang arrastra U_y)
E_PRIOR_ART           = STRUCTURAL_ONLY  (cerrado en rev.2: Pfeiffer 2022 leída y despejada)
```

No es `AUDIT_REJECT`: el operador existe, el álgebra es exacta y es un miembro legítimo de
la familia GCD con límite local `□ − R/2` por un teorema publicado. Lo que no sobrevive es
el **estimador físico**.

No es `AUDIT_PASS_CONDITIONAL`: el coeficiente reclamado no está determinado y el objeto que
la expansión produce no es `C^2` (§4).

> **Actualizado en rev.2 / rev.2.1.** La rev. 1 justificaba este punto diciendo que lo que
> faltaba eran *"dos problemas abiertos en la literatura citada — control uniforme de `W2` en
> espacio curvo al orden `rho^-1/2`, y la expansión `W1` a orden curvatura-cuadrada"*. El
> primero **ya no es un problema abierto**: cae con Pfeiffer (§2.3). El segundo tampoco es
> exactamente un problema abierto, sino un cálculo con la maquinaria ya publicada (§2.4,
> `R6'`). Lo que sostiene el token hoy es `F3`/`F4`: un error de modelado, no una laguna de
> la literatura.

Promoción de estado exigida por el propio brief (§C0), cuya condición se cumple:

```text
S4W_KRETSCHMANN_ESTIMATOR = NOT_DEFINED_WITHOUT_EXTRA_PRESCRIPTION
```

---

## 1. Pregunta A — álgebra de cinco capas: `PASS`

Reproducida desde cero, sin usar los números del candidato, y contrastada contra **tres**
fuentes primarias independientes. Todo cuadra, incluidas normalización y signos.

### 1.1 Marco, tomado de la fuente y no del repo

Belenchia (arXiv:1510.04665) ec. (1): `(B_rho^(D) phi)(x) = rho^(2/D) [a phi(x) + sum_n b_n sum_{y in I_n(x)} phi(y)]`
— la misma forma que usa el candidato. Su ec. (6) define `Ô = sum_n (b_n/n!) (-1)^n H_n`
con `H_n = rho^n ∂^n/∂rho^n`. Actuando sobre `rho^-s`:

```
H_n rho^-s = (-1)^n (s)_n rho^-s   =>   Ô rho^-s = Q_b(s) rho^-s ,
Q_b(s) := sum_n b_n (s)_n / n!  =  M_s(b)/Gamma(s) ,   M_s(b) := sum_n b_n Gamma(n+s)/n!
```

que coincide con la ec. (20) de Belenchia. Para `D = 2N+2` con `N = 1`, sus condiciones son:

- **(3a)** `sum_n (b_n/n!) Gamma(n + (k+1)/(N+1)) = 0`, `k = 0,1,...,N+1` → en D=4, los tres
  momentos en `s = 1/2, 1, 3/2`. **Tres** condiciones homogéneas.
- **(3b)** `a + [2(-1)^(N+1) pi^N / (N! D^2 C_D)] sum_n b_n psi(n+1) = 0`. Con
  `C_D = (pi/4)^((D-1)/2) / (D Gamma((D+1)/2))`, en D=4 sale `C_4 = pi/24` y el corchete vale
  exactamente **3**: `a + 3 sum_n b_n psi(n+1) = 0`. Es literalmente la ecuación de `a` del
  candidato, factor 3 incluido.
- **(3c)** `sum_n (b_n/n!) Gamma(n+3/2) psi(n+3/2) = ` constante no nula. Es una
  **normalización**, no una condición homogénea: es la que fija que el límite sea `□` y no
  otro operador.

### 1.2 Lo verificado

Con `b_BD = (4/sqrt6)(1,-9,16,-8,0)`, `a_BD = -4/sqrt6`:

```
M_{1/2} = M_1 = M_{3/2} = 0                           (exacto)
N_psi(3/2) := sum b_n Gamma(n+3/2)psi(n+3/2)/n! = -2 sqrt6 sqrt(pi)/9   (no nulo: es la normalización)
a_BD + 3 sum b_n psi(n+1) = 0                          (exacto)
```

Ese `(a_BD, b_BD)` es el publicado, en dos sitios: Belenchia–Benincasa–Dowker
(arXiv:1510.04656) ec. (5) da `B̄phi = (4 sqrt(rho)/sqrt6)[-phi(x) + rho ∫ ... e^-xi (1 - 9xi + 8xi^2 - (4/3)xi^3)]`,
y Dowker–Glaser (arXiv:1305.2588) Tabla 1 fila 4d da `C^(4) = (1,-9,16,-8)` con
`alpha_4 = -4/sqrt6`. Coinciden con el candidato componente a componente.

Para la dirección añadida por la quinta capa:

```
delta b = (3,-47,148,-168,64):
  M_{1/2} = M_1 = M_{3/2} = 0        (exacto)
  N_psi(3/2) = 0                     (exacto)  <- preserva la normalización (3c)
  sum delta b_n = 0                  (exacto)  <- necesario: cancela gamma_E
  sum delta b_n psi(n+1) = 1/3       (exacto)  =>  delta a = -1
```

El espacio de soluciones de las cuatro condiciones lineales homogéneas sobre cinco
incógnitas es unidimensional, y `delta b` lo genera (y es primitivo: `gcd = 1`). Las cuatro
condiciones se preservan **para todo** `lambda`, luego `B_lambda = B_BD + lambda D_5` sigue
dentro de la familia GCD. Por el teorema de universalidad de Belenchia (§3.5, su ec. 45:
*"all GCD in even dimensions reduce to (□ − R/2)phi in the local limit"*), el límite local
es `□ − R/2` para todo `lambda`. **La afirmación del §4 del candidato es correcta y está
respaldada por un teorema publicado**, no solo por su propio cálculo.

Momento segundo y el valor de `lambda`:

```
M_2(b) = sum_n b_n Gamma(n+2)/n! = sum_n (n+1) b_n
M_2(b_BD) = -2 sqrt6/3 ,   M_2(delta b) = 1   =>   lambda_* = 2 sqrt6/3     (único)

b_* = b_BD + lambda_* delta b = (8 sqrt6/3)(1,-14,41,-44,16)
a_* = a_BD + lambda_*(-1)     = -4 sqrt6/3 = (8 sqrt6/3)(-1/2)
```

luego el operador del recuadro del §5 del candidato es exacto, prefactor `8 sqrt6/3`
incluido. Y la factorización:

```
Q_{b_*}(s)/(8 sqrt6/3) = (s-2)(s-1)(2s-3)(2s-1)/6
```

que bajo `H = rho d/drho` (es decir `H -> -s` sobre `rho^-s`) es **idéntica** a
`(2/3)(H+1/2)(H+1)(H+3/2)(H+2)`; y `Ô_BD` sale `(4/3)(H+1/2)(H+1)(H+3/2)`, de modo que
`Ô_* = (1/2)(H+2) Ô_BD` es exacto. El kernel `P_*(z) = 1 - 14z + (41/2)z^2 - (22/3)z^3 + (2/3)z^4`
también.

### 1.3 Comprobación de convención, que es donde el brief pedía buscar

Dowker–Glaser usan `H_DG = -l ∂/∂l` y su ec. (13) `O_{2n} = (H+2)(H+4)...(H+2n+2)/[2^{n+1}(n+1)!]`.
En `d` dimensiones `rho = l^-d`, luego `H_DG = d · (rho d/drho)`. Traduciendo:

```
O_4 con H_DG = 4 theta  ->  (4/3)(theta+1/2)(theta+1)(theta+3/2)   == Ô_BD del candidato
```

y aplicando `O_4` y `O_6` a `e^-w` por su propia ec. (12) se recuperan **las dos filas**
de su Tabla 1, `C^(4) = (1,-9,16,-8)` y `C^(6) = (1,-34,141,-189,81)`. Esto valida la
traducción de convención contra dos puntos publicados, no uno. **No hay error de
normalización ni de signo en el candidato.**

De paso aparece el hallazgo de prioridad del §5 de esta auditoría.

---

## 2. Pregunta B — región W2: `PASS_CONDITIONAL` (rev.2)

> **rev.2 — lo que sigue en §2.1–§2.2 era el razonamiento de la rev. 1, que concluía `FAIL`.
> Sigue siendo una descripción correcta de lo que BBD prueban y no prueban, pero
> **ya no sostiene el veredicto**: Pfeiffer 2022 §3.3 va más fino que BBD en exactamente
> este punto. El veredicto vivo es el de §2.3.**

El §6 del candidato propone: *"bajo regularidad suficiente para una expansión uniforme de
Laplace en el coordenado transversal U de W2, la raíz adicional H=-2 debe eliminar también
el término rho^-2"*, dejando `I_{2,*} = O(rho^-5/2)`.

La premisa es exactamente la que BBD enuncian **en espacio plano** y declaran no tener en
espacio curvo.

**Plano (BBD §II.B).** Ahí la heurística es legítima y está escrita: *"If the function of
rho on which Ô acts is well-behaved enough as rho → ∞ to be equal to a power series
expansion in rho^-1/2, then application of Ô will eliminate all the terms that would not —
after multiplication by rho^3/2 — tend to zero."* En plano, añadir el factor `(H+2)` sí
mata la potencia `rho^-2`.

**Curvo (BBD §III.B).** La cota de `W2` **no** proviene de una serie de potencias. Proviene
de acotar integrales de funciones continuas desconocidas: sus ecs. (63)–(66) introducen
`f_0, f_1, f_2, F` en `V(y) = U^2 f_0 + U^3 f_1 + U^4 f_2 + U^5 F`, más `h_0,h_1,h_2,H` en
`sqrt(-g)` y `Phi` en `phi`; y su ec. (75) acota `I_23` con
`|sum_{k>=3} (-rho)^k U^{3k} G^k / k!| <= (rho^3/6) U^9 |G|^3 e^{rho U^3 |G|}`, integrando
luego `U^9 e^{-rho U^2 f_0 / 2}`. Y añaden: *"The terms arising from the action of each H_i,
i = 1,2,3 on the integrand can be bounded similarly and are also of order rho^-1/2."*

Dos consecuencias, y las dos son fatales para el §6:

1. **Un cero del operador aniquila una potencia, no una cota.** Los términos que fijan el
   orden de `W2` en curvo no son de la forma `rho^-s` con `s ∈ {1/2,1,3/2,2}`; son cotas
   sobre integrales de `f_0,f_1,f_2,F,H,Phi,G`. Añadir el factor `(H+2)` no actúa sobre
   ellas. La mejora que el candidato espera no está disponible en el marco publicado.

2. **El orden que BBD consiguen en curvo es ya el orden del supuesto resultado.** Tras el
   prefactor `rho^3/2`, la contribución de `W2` en espacio curvo queda acotada en
   `O(rho^-1/2)` — precisamente el orden en el que el candidato quiere leer su coeficiente
   `C^2`. `W2` no es despreciable al orden objetivo: vive **en** el orden objetivo.

Y BBD cierran la puerta explícitamente en su §III.D: *"since we lack an explicit expression
for the expansion of the volume of long skinny intervals 'down the light cone' in W2, the
finite rho corrections to the limit from W2 can only be given in terms of integrals of
unknown functions, such as f_0(V,theta,phi) ... and are not very enlightening."*

`S4W_5LAYER_W2_COMPACT_PROOF.md` declara su propio alcance como *"analytic lemma only; no
simulation; no global phi=1 claim"* y trabaja sobre `J(rho) = ∫_D dz ∫_0^{U_*(z)} A(U,z) e^{-rho V(U,z)} dU`
con `A` y `V` suficientemente regulares. Dentro de ese enunciado el lema puede ser correcto
—no he encontrado fallo en él—, pero **no es el objeto que hace falta**: su hipótesis de
regularidad sobre `A` y `V` es justamente la que BBD dicen no poder establecer para
intervalos largos y finos en curvo. El lema prueba lo que haría falta *si* se tuviera la
expansión; no la proporciona.

Respuestas puntuales a lo que el brief pedía comprobar: uniformidad en las coordenadas
longitudinal/angulares — **no establecida** en curvo (depende de `f_0(V,theta,phi)`
desconocida); regularidad requerida — es la de las ecs. (63)–(65) de BBD, que ellos
**suponen** (*"we now assume enough differentiability of the metric"*) y no derivan;
términos `rho^-2 log rho` — ver §3, hay términos logarítmicos y están **por encima** del
orden objetivo; límites de integración — el corte `U <= b/(2 sqrt(f_0))` y la
desalineación `a' != a` entre `W1` y `W2` (BBD Fig. 2) introducen dependencia de
prescripción no controlada al orden requerido; hipótesis adicionales — sí, las dos del
párrafo anterior.

### 2.3 (rev.2) Pfeiffer 2022 §3.3: la mejora existe, y el candidato acertó el resultado

Pfeiffer extiende la prueba de BBD a dimensión arbitraria y, en la región del cono, **no
acota término a término**: rastrea la acción del operador de forma exacta a través de una
gamma incompleta. Su ec. (3.7) es `V(x,y) = U^{d/2} f_0(V,θ) + U^{d/2+1} f_1(U,V,θ)`;
desarrollando la exponencial en potencias `l` de `f_1`, sustituyendo `x = U^{d/2}` y
aplicando `O_d`, obtiene su ec. (3.27):

```
O_d [ gamma(lambda, b rho) / rho^{lambda-l} ]
   = A_{lambda,l}(n) gamma(lambda,b rho)/rho^{lambda-l}
     + sum_k (-1)^k B_{lambda,l}(k+1,n) d^{1+k} b^{lambda+k} rho^{l+k} e^{-b rho}
```

con **(3.28)** `A_{lambda,l}(n) := prod_{j=0}^{n} ( d(l - lambda) + 2j + 2 )`, y
`lambda = l + (2/d)(l+1)` (que he vuelto a deducir de su propia sustitución, no copiado).
Los términos con `B` llevan `e^{-b rho}`: suprimidos exponencialmente, irrelevantes.

Lo decisivo, verificado simbólicamente: `d(l - lambda) = -2(l+1)` **en cualquier
dimensión**, luego el factor `j`-ésimo es `2(j-l)` y

```
A_{lambda,l}(n) = prod_{j=0}^{n} 2(j-l) = 0   <=>   l <= n
```

`A` tiene `n+1` factores, que son **exactamente las raíces de `O_{2n}`** (su recursión del
apéndice, `A(n+1) = A(n)·(d(l-lambda)+2(n+1)+2)`, añade un factor por raíz y no sabe nada
de `d` salvo por `lambda`). Es decir: **las raíces del operador sí aniquilan términos de
`W2`** — el mecanismo que el §6 del candidato postulaba y que la rev. 1 de este informe
declaró inexistente. Contando órdenes con su ec. (3.31), la contribución de `W2` a `B̄` es
`rho^{1-2l/d}` para el primer `l` que sobrevive:

| operador en `d=4` | `n` | `A=0` para | primer `l` vivo | `W2` en `B̄` |
|---|---|---|---|---|
| `O_4`, minimal (el de Pfeiffer, `n=⌊d/2⌋=2`) | 2 | `l=0,1,2` | 3 | `O(rho^{-1/2})` |
| `O_6` = el `Ô_*` **del candidato** | 3 | `l=0,1,2,3` | 4 | **`O(rho^{-1})`** |

La fila de arriba reproduce el resultado publicado de Pfeiffer, `O(rho^{-2/d})`, y concuerda
con BBD. La fila de abajo es el §6 del candidato: él predijo
`I_{2,*}=O(rho^{-5/2})`, es decir `rho^{3/2} I_{2,*} = O(rho^{-1})`. **Coincide exacto.**

Luego: **la conclusión del §6 es correcta; su justificación no.** El candidato la apoyaba
en que la función de `rho` admite serie de potencias en `rho^{-1/2}` —que es justo lo que
BBD declaran no tener en curvo, §2.1—. El mecanismo real es otro y está publicado: el
factor `A` de Pfeiffer. Esto es una **reparación, no una refutación**, y es lo que convierte
el §6 de obligación de prueba en resultado con fuente.

```text
B_W2 = PASS_CONDITIONAL
hipótesis exactas bajo las que pasa:
  (h1) ec.(3.7) de Pfeiffer: V = U^{d/2} f_0 + U^{d/2+1} f_1, con f_0(V,θ) > 0 para V > 0
       y f_0 creciente en V;
  (h2) ||f_1||_inf finita sobre W2 y sqrt(-g) no divergente en W2  (sus hipótesis literales);
  (h3) leer su n como el número de raíces del operador y no como floor(d/2).
```

`(h3)` es el único paso que **no está en la tesis**: ella solo usa `n = ⌊d/2⌋`, porque solo
le interesa el operador minimal de cada dimensión. La generalización es una lectura directa
de su propia (3.28) y de la recursión del apéndice —y es legítima porque en `d=4` el
candidato conserva la medida y el `lambda` de `d=4` y solo cambia el número de factores—,
pero **es mi inferencia, no una cita**.

`(h3)` fue sometida a revisión ciega de dos familias (§11) y las dos la declaran **legítima**,
aportando lo que yo no había citado: la inducción del **apéndice A** construye `A_{λ,l}(n)`
factor a factor sobre las raíces de `O_{2n}` sin usar `n=⌊d/2⌋` en ningún paso.

### 2.4 (rev.2.1) El hueco de `(h3)` por el lado de `W1`, señalado por Grok

Lo que esta auditoría **no** examinó, y es el defecto más serio que encontró la revisión
externa: el mismo mecanismo aniquilador existe también en la región **cercana**. Pfeiffer
§3.4, ecs. (3.50)–(3.52):

```
A_{kappa+1,l}(n) = prod_{zeta=0}^{n} ( d(l-(kappa+1)) + 2 zeta + 2 ) = prod_{zeta=0}^{n} 2(zeta - k)
        =>  A_{kappa+1,l} = 0  para  k <= n = floor(d/2)
```

verificado en el texto de la tesis. Es decir: la cuarta raíz no solo limpia `W2`; también
mueve qué términos de `W1` sobreviven, y mueve la condición que él traduce (vía su ec. 3.41,
`m >= ceil((alpha+beta+d-2)/2)`) en `alpha + beta <= 2` para el operador minimal, donde
`alpha, beta` son los órdenes del desarrollo en `y`.

**El canal `k=3` lo comparten el resto logarítmico y el término `y^4` donde vive `C^2`.** De
modo que la cuarta raíz puede, o bien limpiar los logaritmos y abrir el canal de curvatura
cuadrada, o bien aniquilar también la señal. **No lo sé, y no se decide desde aquí.**

Consecuencia sobre lo que afirma la rev. 2: la "separación de un orden entero" entre la región
del cono y el orden `rho^{-1/2}` local es correcta por el lado de `W2`, pero queda
**condicionada a que el canal local sobreviva**. No es una separación establecida; es una
separación establecida en `W2` y pendiente en `W1`. Eso reescribe `R6'` (§9).

Nota de consistencia que vale la pena: que `Ô_*` sea `O_6` (§6.1) y que mate una capa más de
`W2` son **la misma observación vista dos veces**. En la contabilidad del cono, el operador
del candidato se comporta como el de `d=6`, y por eso aniquila un término más.

---

## 3. Pregunta C0 — finitud global antes de cualquier coeficiente: `REGULATED_ONLY`

### 3.1 La comprobación simbólica del PI: **reproducida, no refutada**

El brief ordena reproducirla o refutarla y prohíbe aceptarla por autoridad del repo. Lo he
rehecho desde el tensor de Weyl, no desde `br.py` (que no está en el repo).

Construcción: Schwarzschild es tipo D y puramente eléctrico en el tétrada estático, con
`E_ij = (M/r^3) diag(-2,1,1)`. Reconstruyo el Weyl completo en frame ortonormal mediante
`C_{0i0j} = E_ij`, `C_{0ijk} = H_ijk`, `C_{ijkl} = -eps_{ijm} eps_{kln} E_mn` (esta última
verificada contra la ec. 11b de Wang, `D^k_{ikj} = E_ij`, y contra `D^2 = 4E^2` en d=4),
y aplico un boost de Lorentz a los cuatro índices. Con `M = r = 1`:

| magnitud | resultado | claim del PI |
|---|---|---|
| control sin boost | `E^2 = 6`, `H^2 = 0`, Kretschmann `= 48` | — |
| `8(E^2 - B^2)` | `48` `= 48 M^2/r^6` | ✓ |
| `E^2 - B^2`, boost arbitrario | `6` (invariante) | ✓ |
| boost **radial**, `W = E^2 + B^2` | `6` para todo `eta` | ✓ |
| boost **tangencial** | `36 gamma^4 - 36 gamma^2 + 6` | ✓ exacto |
| promedio angular a rapidez fija | `(96/5)gamma^4 - (72/5)gamma^2 + 6/5` | ✓ `= (6/5)(16 gamma^4 - 12 gamma^2 + 1)` |
| control `gamma = 1` | `6` | ✓ |

Las cuatro fórmulas del PI son correctas. Aviso de notación que importa más abajo: su `H`
es la parte magnética de **dos** índices (`B_ij`), no la `H_ijk` de Wang; se ve en que
impone `K = 8(E^2 - H^2)`. La relación es `B^2 = H^2_{Wang}/2`.

### 3.2 Wang ec. (79) en d=4: transcripción correcta, interpretación del brief con un error

Wang (arXiv:1904.01034) ec. (79) da el `d`-volumen total del ACD en vacío. Sustituyendo
`d = 4`: numerador `2068 E^2 + 360 H^2 - 9 D^2`, denominador `453600`, `Omega_2 = 4 pi`.
Con `D^2 = 4 E^2` (válido en d=4, su ec. 5):

```
2032 E^2 + 360 H^2          <- la transcripción del brief es CORRECTA
```

Pero reexpresado en los invariantes correctos, con `K = 8(E^2 - B^2)` y `W = E^2 + B^2`,
`B^2 = H^2/2`:

```
2032 E^2 + 360 H^2  =  82 K  +  1376 W         ratio  1376/82 = 688/41 ≈ 16.78
```

El split que propone el brief, `836(E^2-H^2) + 1196(E^2+H^2)`, es **álgebra válida** pero
su **etiquetado es falso**: con la `H` de Wang, `E^2 - H^2 = 3K/16 - W/2`, que no es
proporcional a `K`; y `E^2 + H^2` no es `W`. Ninguno de los dos trozos del split es el
término invariante. La descomposición correcta es la de arriba. Esto corrige al brief, no
al candidato; se registra como hallazgo porque el brief es documento del proyecto.

Lo que sobrevive, y es el punto: la corrección de volumen **no** es proporcional a `K`.
Lleva una mezcla con la densidad de superenergía de Bel–Robinson
`W = T_abcd U^a U^b U^c U^d`, que depende de la dirección temporal `U` del diamante, **con
un coeficiente casi 17 veces mayor que el del término invariante**.

### 3.3 Las cuatro preguntas del brief

1. **¿Es finita la integral del término `E^2+H^2` sobre `J^-(x)` bajo las hipótesis exactas
   del esquema BBD?** La pregunta no se plantea en ese esquema: BBD nunca forman esa
   integral. Parten `J^-(x) = W_1 ∪ W_2 ∪ W_3` (sus ecs. 56–58) y la expansión RNC solo se
   usa en `W_1`, de tamaño `a` fijo. Dentro de `W_1` la rapidez está acotada, así que la
   divergencia formal `e^{6 eta}` que teme el brief **no aparece**. La observación del
   brief sobre el límite lógico de su propio argumento es correcta y aquí queda zanjada: no
   hay divergencia, pero tampoco hay integral global.
2. **¿Qué región domina?** `W_2`, la de pegada al cono nulo. Es la única cuya cota en curvo
   (§2) está en `O(rho^-1/2)`, el orden objetivo.
3. **¿Existe en BBD un argumento publicado que justifique cortar, regular o tratar
   localmente esa región a la precisión subdominante `O(rho^-1/2)`?** **No.** Belenchia es
   taxativo: *"Regions W_2 and W_3 ... are not considered in this work"*, y su prueba
   *"strictly holds true when the assumption that the compact support of the field is much
   smaller than the curvature scale is fulfilled"*. BBD sí tratan las tres regiones, pero
   solo a la precisión que exige el límite `□ − R/2`.
4. **Si la finitud solo se obtiene con soporte compacto / parche finito / taper, ¿se
   demuestra que la contribución dependiente de esa prescripción es `o(rho^-1/2)`?**
   **No, y además es falso que lo sea.** BBD §III.C, sobre la propia región `W_1` en curvo:
   *"these terms, after multiplication by rho^3/2, vanish in the limit and the leading
   correction to the limit is O(ln(rho)/sqrt(rho))"*.

El punto 4 tiene una consecuencia que va más allá de "no probado", y es el hallazgo más
duro de esta auditoría: **la forma funcional que el candidato afirma es estructuralmente
incompatible con el resto publicado.** El candidato escribe

```
E[B_* 1] = -(73 sqrt6 / 1575 pi) C^2 rho^-1/2 + o(rho^-1/2)
```

pero `ln(rho) · rho^-1/2` **no es** `o(rho^-1/2)`. Con `phi = 1` los restos del campo (`Psi`)
se anulan, pero los de la métrica y del volumen no: son `T_{mu nu rho}(y)` en su ec. (78) y
`S_{mu nu rho}(y)` en su ec. (80), funciones `C^3` **sin expandir** que absorben
precisamente el orden `y^4` del que tendría que salir el `C^2`.

> **Corrección de rev.2.1, defecto señalado por Grok.** La rev. 1 decía aquí que la forma
> funcional del candidato es *"estructuralmente incompatible con el resto publicado"* y que
> los restos log-realzados *"dominan la señal reclamada"*. Eso es afirmar demasiado: el resto
> `O(ln(rho)/sqrt(rho))` que BBD §III.C declaran es **el del operador de tres raíces**. Con
> cuatro raíces no está calculado, y por §2.4 el factor análogo de `W1` puede cambiarlo.
> Obsérvese además que `(H+s)(ln(rho) rho^{-s}) = rho^{-s}`: una raíz extra **no borra
> logaritmos como borra potencias**, los convierte. El enunciado correcto es el de `F1` en
> §8: la objeción está **bien planteada contra la forma `o(rho^{-1/2})` tal como está
> escrita**, y es una **comprobación abierta**, no una incompatibilidad establecida.

Se cumple por tanto la condición de promoción que el propio brief fijó:
`S4W_KRETSCHMANN_ESTIMATOR = NOT_DEFINED_WITHOUT_EXTRA_PRESCRIPTION`.

---

## 4. Pregunta C — término local W1 y Weyl²: `FAIL`, coeficiente no determinado

Tres razones independientes. La primera basta.

**(i) `H = 0` se usa globalmente y solo vale en un frame.** Especializando Wang a `H = 0`
y `K = 8 E^2`:

```
delta V = 4 pi l^8 (2032 E^2)/453600 = (127 pi/56700) K l^8
```

que es **exactamente** la fórmula del §7 del candidato. Su transcripción de Wang es
correcta. Pero `H = 0` es la condición de que el Weyl sea puramente eléctrico, y eso solo
ocurre en el tétrada estático de Schwarzschild (y bajo boosts radiales, como confirma la
tabla de §3.1: `W = 6` invariante en radial). Para cualquier otra orientación `B != 0` y
`W = E^2 + B^2` crece como `gamma^4`. Por §3.2, el término descartado entra con coeficiente
`1376` frente a `82`: **fijar `H = 0` no comete un error pequeño, descarta el término
dominante.** Respuesta directa a la pregunta del brief: usar globalmente `H=0, D^2=4E^2,
K=8E^2` con `E` en el tétrada estático es **ilegítimo**.

**(ii) La orientación relevante es `U_y` y debe quedar dentro de la integral.** Wang define
`E,H,D` respecto a un `U^a` que en el ACD es la tangente a la geodésica entre sus vértices
(su §III, "ACD"). En la integral del operador, `V(x,y)` es el volumen del intervalo entre
`x` e `y`, de modo que `U = U_y` **varía** sobre la región de integración, barriendo
rapideces respecto al tétrada estático. El candidato la congela. La sospecha del brief es
correcta y ahora es cuantitativa: con el promedio angular de §3.1,
`<W> = (6/5)(16 gamma^4 - 12 gamma^2 + 1)`, la parte no invariante no solo no se cancela al
promediar sobre direcciones: crece.

**(iii) Aun arreglando (i) y (ii), el orden requerido no está disponible en las fuentes
citadas.** Wang sí aporta el ingrediente que falta por un lado — su ec. (76)–(77) da
`sqrt(g)` en RNC a orden curvatura-cuadrada, `sqrt(g) = 1 - (1/180) C^{gamma alpha}_{mu nu} C_{gamma rho alpha sigma} x^mu x^nu x^rho x^sigma`,
y su ec. (6) la métrica RNC al mismo orden. Pero hay que casarlo con un control de `W2` que
no existe (§2) y con restos `W1` que están sin expandir a ese orden (§3.3). `S4W_5LAYER_W1_SCHWARZSCHILD_C2_DERIVATION.md`
se declara a sí mismo `DERIVATION_CANDIDATE_FROZEN / INDEPENDENT_AUDIT_REQUIRED / NO_GLOBAL_PHI1_CLAIM`
y usa la especialización de Schwarzschild desde el principio, con lo que hereda (i).

```
C_W1_COEFFICIENT = FAIL
valor: NO DETERMINADO.  El -73 sqrt6/(1575 pi) no se reproduce y no es validable hoy.
```

El precheck interno ya había puesto `LOCAL_C2_COEFFICIENT = FAIL_AS_DERIVED`. Coincido en
el token; la razón que doy es más fuerte y distinta: no es que la derivación tenga un hueco,
es que el objeto que pretende calcular no es `C^2` sino una combinación `82K + 1376W`
dependiente del observador.

---

## 5. Pregunta D — estructura del término permitido: `FAIL` en la afirmación 1

El brief separa bien dos cosas. Mi veredicto difiere en la primera.

**Afirmación 1** (por covariancia/dimensiones/paridad, una corrección local escalar de
dimensión cuatro en vacío queda restringida a `C_abcd C^abcd`): **es cierta para escalares
construidos covariantemente a partir de la métrica sola** — en vacío `R = 0`,
`R_ab R^ab = 0`, `□R = 0`, y Gauss–Bonnet reduce la base a `C^2`; de Brito–Eichhorn–Pfeiffer
lo enumeran igual en su ec. (2). **Pero es falsa para el objeto que esta construcción
produce**, porque el desarrollo arrastra una dirección temporal privilegiada `U_y` del
intervalo causal. `W = T_abcd U^a U^b U^c U^d` es un escalar de dimensión cuatro en vacío
que **no** se expresa mediante `C^2`, y la ec. (79) de Wang muestra que aparece con
coeficiente ~17 veces mayor. El argumento de estructura falla precisamente porque el objeto
al que se le aplica **no es `U`-libre**.

> **Precisión de rev.2.1, defecto señalado por Grok.** La rev. 1 decía "la construcción no es
> `U`-libre", lo que atribuye al **operador discreto** algo que no le pasa: `B_*` está definido
> por orden y recuento, sin marco preferido ni espacio tangente. Quien lleva la dirección
> temporal es el **integrando**: la corrección de volumen de Wang para un diamante de
> Alexandrov con eje `U`. La objeción es la misma, pero el sujeto correcto es el integrando,
> no el operador. Esto además es lo que mantiene viva la vía de `R6''`: un funcional local
> Lorentz-invariante del jet métrico en `x` tendría que ser múltiplo de `C^2`, así que la
> integral angular sobre `U_y` **podría** colapsar a un invariante. Una posibilidad no
> calculada no autoriza el atajo de unicidad ni a congelar `U`, pero tampoco está cerrada.

De Brito–Eichhorn–Pfeiffer apuntan al mismo obstáculo desde el otro lado: *"the definition
of objects with 'open indices' from causal sets is a challenging task, because it requires
the notion of a tangent space"*.

**Afirmación 2** (el coeficiente es no nulo y vale tal cosa): no establecida, §4.

```
D_COVARIANT_STRUCTURE = FAIL
```

---

## 6. Pregunta E — prior art: `STRUCTURAL_ONLY`

### 6.1 Antecedente estructural fuerte, y no estaba citado como tal: Dowker–Glaser 2013

Su ec. (13) define, para dimensión par `d = 2n`:

```
O_{2n} = (H+2)(H+4)...(H+2n+2) / [2^{n+1} (n+1)!] ,     H = -l ∂/∂l
```

Verificado simbólicamente: `Ô_*` del candidato **es exactamente `O_6`** —esa misma ec. (13)
con `n = 3`— evaluada con la relación de `d = 4`, `H_DG = 4 rho ∂_rho`:

```
O_6|_{H_DG = 4 theta} = (theta+1)(theta+2)(2 theta+1)(2 theta+3)/6
                      = (2/3)(theta+1/2)(theta+1)(theta+3/2)(theta+2)     == Ô_*
y aplicado a e^-w devuelve   C_i = (1,-14,41,-44,16)
```

Es decir: "añadir una quinta capa y ajustar `lambda_*` para anular `M_2`" es, término a
término, **lo mismo que usar el siguiente operador de la torre de Dowker–Glaser**. La raíz
extra `H = -2` (en convención del candidato) es su `H_DG = -8`, el cuarto factor de la
torre. El vector `(1,-14,41,-44,16)` no aparece en su Tabla 1 —que empareja cada operador
con su dimensión propia, y para `d=6` da `(1,-34,141,-189,81)`— así que el vector en sí
parece nuevo; la construcción no lo es. Esto no invalida nada matemáticamente, pero cambia
por completo cómo puede presentarse: el candidato debe citar la ec. (13) de Dowker–Glaser
como la forma general de la que su operador es un caso, no derivar la quinta capa como
hallazgo propio.

### 6.2 El programa ya está publicado: de Brito–Eichhorn–Pfeiffer 2023

arXiv:2301.13525 construye invariantes de curvatura de orden superior en causal sets
(prueba que `R^2 - 2□R` surge de `B^2`) y **enuncia la idea del candidato como dirección
abierta**, en sus conclusiones: *"the construction of new operators that converge to
curvature-invariants beyond the Ricci-scalar, e.g. `R_mu nu R^mu nu` and
`R_mu nu alpha beta R^mu nu alpha beta`. ... we expect that definitions of new discrete
operators, based on expressions inspired by Eq. (8), but with, for instance, **different
coefficients and different number of layers**, can give us information about other
curvature-invariants in a causal set."*

Eso es exactamente el método del candidato, publicado como conjetura/programa en enero de
2023. No es antecedente exacto del coeficiente, pero **elimina cualquier reclamación de
novedad conceptual**.

### 6.3 (rev.2) Pfeiffer 2022: leída, y **no** hay antecedente exacto

La referencia [57] de de Brito–Eichhorn–Pfeiffer es la tesis de máster de
**Christopher-Dustin Pfeiffer**, *Higher curvature terms for Causal Sets: Extended proof and
generalization for the Causal Set d'Alembertian*, Univ. de Copenhague / NBI, 20 mayo 2022
(defensa 1 junio 2022; supervisor Emil Bjerrum-Bohr, co-supervisora Astrid Eichhorn).
Descargada del repositorio del NBI y leída completa.

Barrido sobre el texto completo:

| término | apariciones | lectura |
|---|---|---|
| `Weyl` | **1** | y no es extracción: dice que *comparando* las construcciones de bola geodésica y de intervalo de Alexandrov *"it would also already be possible to get some information about the Weyl tensor in flat space-times"* (su ref. [62]). Otra ruta, no ésta. |
| `Kretschmann` | **0** | — |
| `non-minimal` / `nonminimal` / `generalized causal set` | **0** | la familia GCD no mínima **no aparece** |
| `Aslanbeigi` | 1 | solo Saravani–Aslanbeigi, *On the causal set–continuum correspondence* (2014). **No** cita arXiv:1403.1622, el paper de los GCD |
| `W2` / `light cone region` | 14 / 3 | sí trata las tres regiones, en dimensión arbitraria → §2.3 |

Su generalización es `B^2 = B ∘ B`, **composición** del operador minimal consigo mismo, que
da `R^2` y `□R` — la misma ruta que luego publicaron en arXiv:2301.13525. **No varía el
número de capas ni usa coeficientes libres en ningún punto.**

Conclusión: **no hay antecedente exacto** del operador de cinco capas, ni del vector
`(1,-14,41,-44,16)`, ni de ningún estimador de `C^2`/Kretschmann. El antecedente estructural
sigue siendo la ec. (13) de Dowker–Glaser (§6.1), y el del programa, 2301.13525 (§6.2).
`E_PRIOR_ART` queda **cerrado** en `STRUCTURAL_ONLY`.

### 6.4 (rev.2) Y además la tesis nombra el obstáculo que el candidato retira

En su sección final de perspectivas, Pfeiffer escribe:

> *"Extensions towards other components of the Ricci-tensor are not possible within the
> framework of the Causal Set d'Alembertian alone. Such components could come from higher
> orders in the metric expansion in Riemann Normal Coordinates, but such terms of the
> corrections to the Causal Set d'Alembertian **would be of at least the same order in rho
> as the corrections from the light-cone region**. There an expansion of volume V(x,y),
> needed to calculate the contributions from this region, is not yet as easily possible."*

Eso es, palabra por palabra, el obstáculo que esta auditoría había identificado por su
cuenta como `F2`/`R6`: los órdenes superiores de la expansión RNC de la métrica —donde vive
`C^2`— entran al **mismo orden** que las correcciones de la región del cono, y no se las
puede separar.

Pero por §2.3, **el operador del candidato rompe precisamente ese empate**: con la raíz
extra, la región del cono baja a `O(rho^{-1})` mientras el término buscado sigue en
`O(rho^{-1/2})`. Hay un orden entero de separación donde la tesis dice que no hay ninguno.

Esto es lo más valioso que sale de la auditoría, y no estaba en el candidato: la línea tiene
ahora un **obstáculo publicado con nombre y autor al que responde**, en lugar de una
esperanza. No prueba el coeficiente —§4 sigue en pie— pero convierte la pregunta en una bien
planteada.

### 6.4 Resto del barrido

- Uso de raíces adicionales de `H`: estructuralmente presente en la torre de §6.1, y la
  familia no mínima con parámetros libres es de Aslanbeigi–Saravani–Sorkin (arXiv:1403.1622),
  que es de donde Belenchia toma los GCD.
- Extracción de curvatura de recuentos de capas/intervalos: Benincasa–Dowker (1001.2725),
  Roy–Sinha–Surya (arXiv:1212.0631, *The Discrete Geometry of a Small Causal Diamond*, que
  **sí está en `biblioteca/`** bajo el nombre `Discrete geometry of a small causal diamond.pdf`
  y obtiene correcciones de curvatura de primer orden a `<C_k>` en RNC).

```
E_PRIOR_ART = STRUCTURAL_ONLY  (CERRADO en rev.2)
  - antecedente estructural del operador:  Dowker-Glaser 1305.2588 ec.(13) con n=3   -> §6.1
  - antecedente del programa:               de Brito-Eichhorn-Pfeiffer 2301.13525     -> §6.2
  - Pfeiffer 2022 (tesis):                  LEIDA Y DESPEJADA, sin antecedente exacto -> §6.3
  - antecedente exacto del operador de cinco capas, del vector (1,-14,41,-44,16)
    o de cualquier estimador de C^2/Kretschmann:  NINGUNO ENCONTRADO
```

> Corrección de rev.2.1: esta caja decía *"y Pfeiffer 2022 SIN COMPROBAR"*, resto de la rev. 1
> que contradecía al propio §6.3. Defecto señalado por la revisión ciega de DeepSeek
> (`revisiones/2026-10-10-s4w-auditoria/informe_deepseek.md`). Inconsistencia documental, sin
> efecto sobre ningún veredicto.

### 6.5 Higiene bibliográfica: ninguna de las cinco fuentes del brief está en `biblioteca/`

Comprobado: de los cinco arXiv que el brief declara "fuentes mínimas" —1510.04665,
1510.04656, 1904.01034, 1403.1622, 2301.13525— **no hay ninguno** en `biblioteca/` (125
PDFs). Sí están 1001.2725 (Benincasa–Dowker) y, no citados por el brief pero pertinentes,
1305.2588 (Dowker–Glaser, con conversión a markdown) y 1212.0631. Es la misma clase de
doble estándar que el comité 051 registró como T21.

---

## 7. Claim máximo que sobrevive

```
MAXIMUM_SURVIVING_CLAIM:
Un enunciado puramente algebraico, exacto y verificado:

En D=4 y con L_max=4, la familia GCD definida por las ecs. (3a)-(3c) de Belenchia admite
una dirección nula unidimensional delta b = (3,-47,148,-168,64) con delta a = -1 que
preserva las tres condiciones homogéneas y la normalización; lambda_* = 2 sqrt6/3 es el
único valor que anula M_2(b); el operador resultante es

  B_* = (8 sqrt6/3) rho^{1/2} [ -1/2 + L_1 - 14 L_2 + 41 L_3 - 44 L_4 + 16 L_5 ] ,
  Ô_* = (2/3)(H+1/2)(H+1)(H+3/2)(H+2) = (1/2)(H+2) Ô_BD ,

sigue siendo miembro de la familia GCD y por tanto, por el teorema de universalidad de
Belenchia (1510.04665 §3.5), conserva el límite local □ - R/2; y coincide exactamente con
el operador O_6 de la ec. (13) de Dowker-Glaser (1305.2588) evaluado con H_DG = 4 rho ∂_rho.

AÑADIDO EN rev.2 — un enunciado asintotico, condicional pero con fuente:

Bajo las hipotesis (h1)-(h3) de §2.3, la contribucion de la region del cono W2 al valor
medio del operador de cinco capas en d=4 es O(rho^{-1}), frente a O(rho^{-1/2}) para el
operador minimal.  Es decir: la quinta capa compra un orden entero de separacion entre la
region del cono y el orden rho^{-1/2} donde viviria un termino local de curvatura
cuadrada — la separacion que Pfeiffer 2022, en sus perspectivas, declara no disponible.

Nada físico todavía. Ni estimador, ni coeficiente, ni sensibilidad a Weyl. Pero esto ya no
es solo algebra: es una propiedad asintotica del operador, y es lo unico de todo el
candidato que apunta a por que la linea podria merecer otra ronda.
```

Permanece prohibido todo lo del §8 del candidato y de la "frontera de claims" del brief, y
se añade: **no afirmar que el operador de cinco capas sea nuevo** sin despachar antes §6.1
y leer Pfeiffer 2022.

---

## 8. Cuestiones fatales

```
FATAL_ISSUES:

F1. ABIERTA, NI RESUELTA NI REFUTADA (rev.2).  ln(rho) rho^{-1/2} no es o(rho^{-1/2}).  La
    forma funcional del §7 del candidato choca con el resto log-realzado que BBD §III.C
    declaran para W1 en curvo.  rev.2: NO se sabe si el factor A de Pfeiffer limpia tambien
    estos terminos.  Es la comprobacion R6' de abajo, y es ahora el verdadero cuello.

F2. *** CAE EN rev.2. ***  Decia: "W2 vive en el orden objetivo y la raiz extra no puede
    mejorarlo".  Es falso.  Por Pfeiffer (3.27)-(3.32), leyendo su n como el numero de
    raices del operador, W2 baja de O(rho^{-1/2}) a O(rho^{-1}) con la quinta capa, y la
    prediccion del §6 del candidato se confirma exacta.  Del F2 original solo queda que la
    *justificacion* escrita en el §6 es la equivocada (serie de potencias vs factor A).

F3. EN PIE.  H=0 descarta el termino dominante.  Wang ec.(79) en d=4 es 82K + 1376W; el
    candidato conserva solo la parte proporcional a K, cuyo coeficiente es ~17 veces menor
    que el del termino de Bel-Robinson que tira.

F4. EN PIE.  El integrando no es U-libre (el operador discreto si lo es: orden y recuento),
    luego el argumento de estructura covariante no cierra tal como se uso.  W = T_abcd U^a U^b
    U^c U^d es un escalar de dimension cuatro en vacio que no se reduce a C^2, y U = U_y varia
    dentro de la integral.  Que la integral angular colapse a un invariante sigue siendo
    posible y es el calculo R6''.

F5. CERRADA EN LO EXACTO, ABIERTA EN LO DOCUMENTAL (rev.2).  No hay antecedente exacto:
    Pfeiffer 2022 leida y despejada (§6.3).  Pero Ô_* es la ec.(13) de Dowker-Glaser con
    n=3 y hay que citarlo (R2); y el programa esta publicado en 2301.13525.
```

Ninguna afecta al §1 (álgebra). El cambio que trae rev.2 es de **naturaleza**, no solo de
recuento: antes el estimador estaba bloqueado por dos cosas que los propios autores de la
literatura declaran abiertas. Ahora lo bloquean `F3` y `F4`, que no son problemas abiertos
sino **un error de modelado y un cálculo que nadie ha hecho**, más `F1`, que es una
comprobación concreta. Eso es reabrible; lo anterior no lo era.

---

## 9. Reparaciones exigidas

```
REQUIRED_FIXES:

R1 (documental, inmediato).  Reescribir el §7 del candidato: el objeto que la expansion
   produce es 82K + 1376W con W dependiente de U_y, no C^2.  Retirar las tres formulas con
   signo de interrogacion, no "dejarlas pendientes": su forma funcional esta refutada por
   F1, no solo sin verificar.

R2 (documental, inmediato).  Anadir al §3 del candidato la cita de la ec.(13) de
   Dowker-Glaser 1305.2588 y declarar que Ô_* = O_6|_{H_DG = 4 rho ∂_rho}.  Rebajar la
   quinta capa de hallazgo a caso particular de una torre publicada.

R2' (documental, rev.2).  Reescribir el §6 del candidato: la conclusion I_{2,*}=O(rho^{-5/2})
   es CORRECTA, pero su justificacion no.  Sustituir el argumento de "expansion uniforme de
   Laplace / serie de potencias en rho^{-1/2}" por el factor A_{lambda,l}(n) de Pfeiffer
   (3.28), citando la tesis, y declarar las hipotesis (h1)-(h3) de §2.3 — incluida la (h3),
   que es inferencia de esta auditoria y no cita.

R3 (documental).  Corregir el split del brief: 2032 E^2 + 360 H^2 = 82K + 1376W.  El
   836(E^2-H^2) + 1196(E^2+H^2) es algebra valida con etiquetas falsas.

R4 (estado, actualizado en rev.2).  Emitir:
     S4W_5LAYER_OPERATOR_ALGEBRA   = PASS_EXACT_AND_INDEPENDENTLY_REPRODUCED
     S4W_W2_EXTRA_ROOT             = PASS_EXACT
     S4W_W2_ASYMPTOTIC_IMPROVEMENT = PASS_CONDITIONAL_ON_PFEIFFER_2022_(h1)-(h3)
     S4W_W1_LOG_REMAINDER          = OPEN / DECISIVE          <- nuevo, era F1
     S4W_LOCAL_C2_COEFFICIENT      = FAIL_AS_DERIVED / COEFFICIENT_NOT_DETERMINED
     S4W_KRETSCHMANN_ESTIMATOR     = NOT_DEFINED_WITHOUT_EXTRA_PRESCRIPTION
     S4W_PRIOR_ART                 = STRUCTURAL_ANTECEDENT_FOUND / NO_EXACT_ANTECEDENT /
                                     PFEIFFER_2022_CHECKED_AND_CLEARED
     MERGE_TO_RELATIVIDAD          = NOT_AUTHORIZED
     SIMULATION                    = NOT_AUTHORIZED

R5 (bibliografico, barato).  Incorporar a biblioteca/ los cinco arXiv del brief, que no
   estan, mas Dowker-Glaser 1305.2588 (ya esta) y la tesis de Pfeiffer 2022 (descargada
   del repositorio del NBI; conviene archivarla con su sha256).

R6 *** SUPERSEDIDA POR rev.2. ***  Decia que habia que construir la expansion del volumen
   de intervalos largos y finos en curvo, y que sin ella ninguna eleccion de capas cambiaba
   nada.  Lo segundo es falso: la quinta capa SI cambia el orden de W2 (§2.3).  La
   expansion sigue sin existir, pero ya no hace falta para separar los ordenes.

R6' (rev.2, REESCRITA EN rev.2.1 tras el defecto 5 de Grok — la comprobacion que decide la
   linea, y es barata).  La version de rev.2 preguntaba solo por los logaritmos.  Estaba
   incompleta: hay que preguntar por el canal entero, porque la cuarta raiz actua en W1 igual
   que en W2.

   Maquinaria: Pfeiffer §3.4, ecs.(3.41) y (3.50)-(3.52), donde
       A_{kappa+1,l}(n) = prod_{zeta=0}^{n} 2(zeta - k) = 0  para k <= n,
   y la condicion de contribuir se traduce via m >= ceil((alpha+beta+d-2)/2) en alpha+beta <= 2
   para el operador minimal (n=2).  Rehacerlo con n=3 y responder las DOS preguntas a la vez:

     (a) ¿aniquila la cuarta raiz los restos log-realzados del W1 curvo (BBD §III.C
         ecs.(48)-(52), que con phi=1 son los de la metrica T_{mu nu rho} y del volumen
         S_{mu nu rho})?   Ojo: (H+s)(ln(rho) rho^{-s}) = rho^{-s}, asi que una raiz extra NO
         borra logaritmos como borra potencias; los convierte.  No dar por hecho el signo del
         resultado.
     (b) ¿SOBREVIVE el canal y^4 donde vive C^2, o lo aniquila el mismo factor?  k=3 lo
         comparten el resto log y el termino de curvatura cuadrada.  Con n=3 la condicion
         alpha+beta <= 2 se mueve; hay que calcular a donde.

   Cuatro salidas, y las cuatro son resultado publicable dentro del repo:
     - (a) si y (b) sobrevive  -> el orden rho^{-1/2} queda limpio y el canal abierto: pasar a R6''.
                                  Es el unico escenario en que la linea revive de verdad.
     - (a) si y (b) aniquilado -> la quinta capa limpia la region del cono Y mata la senal.
                                  Autoderrota elegante; cierra la linea con un no-go nitido.
     - (a) no                  -> el estimador muere por F1 de forma definitiva.
     - no concluyente          -> decir exactamente que falta; sigue siendo mas de lo que habia.
   Es analitico, no necesita simulacion ni semillas.

R6'' (solo si R6' sale bien).  Recalcular el termino local de W1 al orden rho^{-1/2}
   manteniendo U_y DENTRO de la integral, con la metrica RNC a orden curvatura-cuadrada de
   Wang ec.(6) y su sqrt(g) ec.(76)-(77), y con la descomposicion E/H referida a U_y y no al
   tetrad estatico.  Lo que salga sera una combinacion de K y de la integral angular de W
   sobre el cono: la pregunta fisica real es si esa integral angular colapsa a algo
   invariante.  Nadie la ha hecho.  Y OJO: aunque salga un coeficiente, sigue prohibido todo
   lo de la frontera de claims (realizacion-por-realizacion, varianza, horizonte, Page-Shoom).
```

---

## 10. Lo que esta auditoría no cubre

- **Los dos pasos de juicio ya NO están sin revisar** (rev.2.1): se sometieron a dos familias
  distintas en revisión ciega sellada y las dos los confirman. Ver §11. Lo escrito en §1
  (`PASS`) es verificación simbólica; §3 y §4 son lecturas ancladas en cita literal.
- **Pfeiffer 2022: leída completa** (§6.3–§6.4). `E_PRIOR_ART` queda cerrado.
- **No he auditado** `S4W_5LAYER_W1_UNIFORM_REMAINDER_PROOF.md` línea a línea. En rev.1 dije
  que un `PASS` suyo no movería el veredicto, porque el fallo estaba en `F2`. **Con `F2`
  caído eso ya no vale**: su alcance (`fixed compact W1`) está justo donde ahora se decide
  todo, así que **pasa a ser pieza central** y debe auditarse junto con `R6'`.
- **No se ejecutó nada.** Ni simulación, ni semillas, ni `make dry-run/gate/op21-terminal`.
  `thresholds.py` intacto.

---

## 11. (rev.2.1) Revisión ciega externa de esta auditoría — dos familias

Por instrucción del PI (2026-10-10), **no** se convocó al sanedrín: se mandó la auditoría a
dos casas por separado, en revisión ciega sellada, con `revision-ciega` del PATH
(`~/herramientas` @ `783f078`). Encargo, entradas exactas y respuestas sin editar en
`revisiones/2026-10-10-s4w-auditoria/`.

**Qué se envió, idéntico a las dos casas** (`entrada_*.txt` sha256
`49cbb423966c7071ea5cc93119810e848188373b5128fbadabbacd2c2e8982e9`, 256 KB): esta auditoría
(rev. 2), el candidato (`15eb7a5`) y la tesis de Pfeiffer en PDF (sha256 `39beffd1…b7eba`).
Nada más del repo. Sesión sellada: sin herramientas, ficheros ni web.

**Qué se preguntó:** los dos únicos pasos donde esta auditoría no cita sino que infiere —`J1`
(si `U_y` rompe el argumento de estructura) y `J2` (si `(h3)` es legítima)— más tres
recomputaciones de control y la invitación explícita a tumbar el token.

| casa | modelo | `J1` | `J2` | veredicto global |
|---|---|---|---|---|
| DeepSeek | `deepseek-v4-pro` | `CORRECTA` | `LEGITIMA` | `CONFIRMADA_CON_CORRECCIONES` |
| Grok (xAI) | `grok-4.6` | `CORRECTA` | `LEGITIMA` | `CONFIRMADA_CON_CORRECCIONES` |

Las dos, de familias distintas y sin verse, confirman los dos juicios y el token
`AUDIT_REQUIRES_MAJOR_FIX`. Las dos recomputaron y confirmaron `2032E²+360H² = 82K+1376W`,
`d(l−λ) = −2(l+1)` con `A = 0 ⟺ l ≤ n`, y que `F1` está bien planteada contra la forma
`o(ρ^{−1/2})` del §7 del candidato. Las dos aportaron lo mismo en apoyo de `(h3)`, y es algo
que esta auditoría no había citado: **la inducción del apéndice A construye `A_{λ,l}(n)`
factor a factor sobre las raíces de `O_{2n}` sin usar `n=⌊d/2⌋` en ningún paso.**

**Defectos que encontraron, todos incorporados:**

| # | casa | defecto | dónde se corrigió |
|---|---|---|---|
| 1 | ambas | caja de §6 con `Pfeiffer 2022 SIN COMPROBAR`, resto de rev. 1 que contradecía a §6.3 | §6, caja de `E_PRIOR_ART` |
| 2 | Grok | `n=⌈d/2⌉` escrito donde Pfeiffer usa `⌊d/2⌋` (inocuo en `d=4`) | §2.3, §10 |
| 3 | Grok | §3.3 declaraba `F1` "estructuralmente incompatible" mientras §8 la deja abierta | §3.3, nota de rev.2.1 |
| 4 | Grok | "la construcción no es `U`-libre" atribuye al operador discreto lo que es del integrando | §0, §5, `F4` |
| 5 | **Grok** | **no se examinó la cara `W1` de `(h3)`**: `A_{κ+1,l}(n=3)` puede aniquilar el canal `k=3`, compartido por el resto log y por el `y^4` de `C^2` | **§2.4 nueva, y `R6'` reescrita** |

El **defecto 5 es material** y es la aportación real de la revisión externa. Obligó a: añadir
§2.4; condicionar la "separación de un orden entero" de la rev. 2 a que el canal local
sobreviva; y reescribir `R6'`, que preguntaba solo por los logaritmos, para que pregunte
también si la cuarta raíz mata la señal. Sin ese defecto, la auditoría habría dejado como
"vía de reapertura" algo que puede ser autoderrotante.

Lectura honesta del resultado: las dos casas confirman que la auditoría acierta en lo que
afirma, y una de las dos muestra que **no afirmaba bastante** — el alcance de `(h3)` era más
ancho de lo que esta auditoría vio, y en la dirección que puede decidir la línea en cualquiera
de los dos sentidos.
