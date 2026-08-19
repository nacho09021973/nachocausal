# Foro Decision 002 — nc2fb-auditoria-adversarial

> Produced by `/foro`. The forum PROPOSES; the user AUTHORISES. No forum agent executed a one-way,
> outward-facing, or irreversible action. Claims are promoted only by an oracle outside the
> language layer — a command, a `path:line`, a verified citation. Agreement between agents is not
> evidence, and no verdict here was reached by majority.

## 1. Decision question

¿Pasa `NC-2F(B)` —el Teorema 1.1 `E[Delta_n^2] <= 4.2e4/n` para `n>=10^6`, incondicional, en
`emergencia/P1a_count_volume_rectangular_discrepancy_l2_d2.md` en el commit `ea732ff`— una
auditoría adversarial lo bastante fuerte como para que el PI declare CERRADA DE FORMA DEFINITIVA
toda la parte incondicional del programa y no vuelva a tocarla? Veredicto requerido:
PASA / PASA CON CORRECCIONES / NO PASA, con la lista literal de defectos y su gravedad.

## 2. Verified state

Facts checked **this session**, each with the command or `path:line` that produced it. Anything
unchecked is marked `[UNVERIFIED]`.

```text
$ git rev-parse HEAD
ea732ffb1a000d3df26e52c901bd7484d6c3514c

$ git status --porcelain
(sin salida: árbol limpio)

$ git log --oneline -4
ea732ff Record the PI's explicit ratification of NC-2F
9e5ac5c Lower the selected-variance exponent to 3/2 and bound L2 discrepancy
e0d17f6 Sync memory snapshot after NC-2E
fd71797 Reduce NC-2E to a relative discrepancy bound

$ ls FORO.md
ls: cannot access 'FORO.md': No such file or directory
```

Oráculo aritmético 1 del chair (`verify_nc2fb.py`, ejecutado en el scratchpad, **fuera del repo**;
no es un artefacto del repositorio):

```text
terms k=1..15: [1.118, 0.935, 0.75, 0.586, 0.451, 0.342, 0.258, 0.193, 0.143, 0.106, 0.078,
                0.057, 0.042, 0.031, 0.022]
sum_15 = 5.1131  tail k>=16 = 0.0594  total = 5.1725
sqrt(1.4) = 1.1832
niveles donde L_k > 1.4(k+1.5): [] count: 0
sqrt(6)*sqrt(1.4)*S = 14.9912 (coef de 1/sqrt(n))
n=1e6: K = 60  2^K/n^3 = 1.152921504606847  segunda parte exacta = 0.000896  1/sqrt(n) = 0.001
E[W] <= first+second+res = 0.015889424291505968  vs 17/sqrt(n) = 0.017
(17)^2+1 = 290 ; 144*290 = 41760 <= 4.2e4 -> True
C_Delta = 2*(65+4.2e4) = 84130.0 ; C_q = 4e4*C_Delta+1 = 3365200001.0
```

Oráculo 2 del chair, sobre el **literal publicado** en `:265` (motivado por el defecto D6 de la
ola 1, que detectó que el oráculo 1 había evaluado una expresión distinta de la commiteada):

```text
n=1e6:  K=60  exacto=896.0 <= 0.234K^2+0.93K=898.2 <= 4.4L^2+6L+2=924.7 | <=1/sqrt(n)? True margen=0.0753
n=1e7:  margen=0.6073 ; n=1e9: 0.9363 ; n=1e12: 0.9965 ; n=1e20: 1.0000 ; n=1e40: 1.0000
barrido n>=1e6 (200 puntos): 0 violaciones
razon exacta t_17/t_16 = 0.72703   (el texto :256 dice "<0.72": FALSO)
t_14 exacto = 0.03076              (el texto :253 tabula 0.030)
```

Oráculo 3 del chair, sobre las correcciones candidatas a la frase falsa:

```text
t_16 exacto = 0.016341 ; razon exacta = 0.7270292
  con r<=0.72,   t16<=0.0163:  cola <= 0.058214 -> <0.06? True
  con r<=0.728,  t16<=0.0163:  cola <= 0.059926 -> <0.06? True
  con r<=0.7271, t16<=0.01635: cola <= 0.059912 -> <0.06? True
  con r<=0.7271, t16<=0.0164:  cola <= 0.060095 -> <0.06? False
cola exacta k>=16 = 0.0593775
suma total usando cola 0.061: 5.17409 <= 5.2? True
```

Verificación de la correspondencia fichero↔token `NC-2D` (cerraba un `[UNVERIFIED]` de la ola 1):

```text
$ grep -n "NC-2D\|NC2D_TERMINAL" emergencia/P1a_count_volume_selected_second_moment_d2.md | head -5
1:# `NC-2D` — segundo momento de la forma seleccionada
496:NC2D_TERMINAL = NC2D_PARTIAL_RELATIVE_MOMENT_REDUCTION
$ grep -rn "selected_second_moment" docs/*.md
docs/program_reopening_note_2026-08-17_nc2d_selected_second_moment_DRAFT.md:157: (salida única de NC-2D)
```

**Corrección del chair a su propio DOSSIER, hecha tras la ola 1 y antes de la ola 2.** La premisa
inicial del expediente decía que «`NC-2F(a)` demuestra `Pr(S) -> 0`». Es **falsa**: `NC-2F(a)`
prueba una cota **inferior** que decae, y una cota inferior que decae no dice nada sobre el valor.
Esta corrección fue señalada por el rol de integración y confirmada después por el verificador de
fuentes. Queda registrada como claim `C10 / REFUTED` en §8 y como advertencia de método: el error
lo introdujo el chair, que es además el autor del documento auditado.

## 3. Dossier

Ficheros, comandos y referencias que el chair entregó al panel:

- `emergencia/P1a_count_volume_rectangular_discrepancy_l2_d2.md` — documento auditado (`NC-2F(B)`).
- `emergencia/P1a_count_volume_selected_variance_clt_scale_d2.md` — `NC-2E` (Teorema 8.1 `:607-653`,
  Corolario 8.2 `:654-660`, Lema 6.1 `:391`, Lema 6.3 `:437-449`).
- `emergencia/P1a_count_volume_selection_mass_sqrt_scaling_d2.md` — `NC-2F(a)`.
- `emergencia/P1a_count_volume_selected_interior_mass_d2.md` — `NC-2C`.
- `emergencia/P1a_count_volume_selected_second_moment_d2.md` — `NC-2D`.
- `emergencia/P1a_count_volume_lema_kl_d2.md` — modelo congelado (§1 experimento, §2.1
  independencia rango–magnitud).
- `docs/program_reopening_note_2026-08-18_nc2f_variance_exponent_reduction.md` — nota de alcance y
  refrendo de `NC-2F`.
- `docs/program_reopening_note_2026-08-18_nc2e_selected_clt_scale_DRAFT.md` — nota firmada de `NC-2E`.
- `docs/program_closure_note_2026-07-30.md` — cierre del programa.
- `memoria_claude/program-status-reentry-marker.md` — marcador de reentrada commiteado.
- `memoria_claude/numbers-must-come-from-committed-script.md` — regla sobre procedencia de números.
- `CLAUDE.md` — reglas fundacionales.
- Scratchpad autorizado para verificaciones de sólo lectura:
  `/tmp/claude-1000/-home-adnac-nachocausal/88e56500-527a-484d-862e-de41a6b8db26/scratchpad`.

Restricciones vinculantes entregadas al panel: `CLAUDE.md` (respaldo verificable o `[UNVERIFIED]`;
una barrera que no puede fallar es decoración; exploración y confirmación estrictamente separadas);
nota `NC-2F` §5 (prohibido afirmar que `NC2E-O3` queda cerrado; prohibido modificar tokens
publicados; prohibidos datos/simulaciones/semillas/código/artefactos nuevos **en el repo**; citas
externas con DOI verificable o prueba autocontenida); `NO_MODIFICA: PR #7`; `SELLO: intacto`.

## 4. Expert briefs (wave 1 — blind, parallel)

Pasted verbatim. The chair did not merge, smooth, or summarise these.

#### Expert brief — Combinatorista de la reducción discreta
- **Assessment:** Desde la lente §2–§3 el puente discreto→continuo es **correcto**: no encuentro ningún defecto matemático, ni deriva de definición entre `NC-2C`/`NC-2D`/`NC-2E`/`NC-2F-b`, ni pérdida/ganancia de factor. Los tres defectos que sí encuentro son **declarativos** (convención c.s. no declarada, puntero de sección impreciso, un paso elidido), no aritméticos: ninguno mueve `4`, `3`, `12`, `144` ni `41760`. Veredicto desde este rol: **PASA CON CORRECCIONES**, siendo las correcciones puramente textuales y confinadas a `P1a_count_volume_rectangular_discrepancy_l2_d2.md` §3.
- **Load-bearing facts:**
  - *Identidad del objeto entre documentos: exacta.* Las cuatro definiciones de `Delta_n` son literalmente la misma fórmula `max_{I,J}|N_{Pi_n}(I,J)/n - |I||J|/n^2|`: `emergencia/P1a_count_volume_rectangular_discrepancy_l2_d2.md:13-17`, `emergencia/P1a_count_volume_selected_variance_clt_scale_d2.md:136-140`, `emergencia/P1a_count_volume_selected_interior_mass_d2.md:431-439`, `emergencia/P1a_count_volume_selected_second_moment_d2.md:215-223`. No hay drift de definición.
  - *Convención abierto/cerrado: consistente.* `NC-2E` §2.5 usa **intervalos cerrados de rangos** con `|I|=K_h+1`, `|J|=L_h+1`, `M_h=N_{Pi_n}(I,J)` (`...selected_variance_clt_scale_d2.md:133-140`). Todo intervalo cerrado `{alpha..beta}` con `1<=alpha<=beta<=n` es exactamente `I={a_1+1..a_2}` con `a_1=alpha-1>=0`, `a_2=beta<=n`; la parametrización de `NC-2F` §2 (`:57`) es por tanto **biyectiva** sobre los intervalos no vacíos y cubre además los vacíos (`a_1=a_2`).
  - *El par del ganador del selector está dentro del máximo.* El selector restringe a cuádruplas con «los dos intervalos cerrados de cardinalidad al menos tres» (`emergencia/P1a_count_volume_lema_kl_d2.md:45`); el máximo de `Delta_n` recorre **todos** los pares, un superconjunto. La dirección necesaria es la correcta: `|theta_h| <= Delta_n` puntualmente en `S` (`...selected_variance_clt_scale_d2.md:149-150`) queda dominada. No hay sub-cobertura.
  - *Corroboración independiente del rango del máximo:* las tres notas previas cuentan «menos de `n^4` pares de intervalos» (`...selected_interior_mass_d2.md:441`, `...selected_second_moment_d2.md:225-232`, `...selected_variance_clt_scale_d2.md:430`). Con la parametrización de `NC-2F`, el número de pares es `[n(n+1)/2]^2 ~ n^4/4 < n^4`: consistente.
  - *Lema 2.1 correcto, incluyendo bordes.* `N(I,J)=F(a_2,b_2)-F(a_1,b_2)-F(a_2,b_1)+F(a_1,b_1)` con `F(a,b)=#{i<=a: Pi(i)<=b}` es inclusión–exclusión estándar sobre cuadrantes anidados; y `|I||J|=(a_2-a_1)(b_2-b_1)=a_2b_2-a_1b_2-a_2b_1+a_1b_1`, luego la línea `:63` es **correcta, no una errata**. Bordes: `a=0` o `b=0` → `F=0`, `D=0`, y `D^*` se define sobre `0<=a,b<=n` (`:47-51`) ✓; `I` o `J` vacío (`a_1=a_2`) → los cuatro términos se cancelan por pares ✓.
  - *Lema 3.1: la identificación NO se importa de fuera y NO es circular.* El hecho requerido —permutación de rangos de muestra iid continua es **uniforme** e independiente de los estadísticos de orden, con `Pi=R_V∘R_U^{-1}`— está en el modelo congelado, en `emergencia/P1a_count_volume_lema_kl_d2.md:95-105`. No hay circularidad con `NC-2C`/`NC-2E`: el Lema 3.1 de `NC-2C` (`...selected_interior_mass_d2.md:111-127`) es una desigualdad de Azuma sobre muestreo sin reemplazo, autocontenida y **no usada** en `NC-2F` §§2–7; recíprocamente `NC-2F` §3 no invoca ninguna cola de `NC-2C`. Las dos rutas son independientes.
  - *`F(a,b)=n P_n([0,U_(a)]x[0,V_(b)])` correcta.* `{i<=a}` en el índice de `U`-rangos ≡ `{U_i<=U_(a)}`; `{Pi(i)<=b}` ≡ `{V_i<=V_(b)}`.
  - *`|U_(a)-a/n|<=W` correcta y depende de la convención cerrada.* `Z(x,1)` está incluido en el sup de (3.1) (`:83-87`). Con rectángulos **cerrados** la FDE vale exactamente `a/n` (`:110-111`); con `[0,x)` valdría `(a-1)/n` y el argumento perdería `1/n`. El documento usa `[0,x]` de forma uniforme — coherente.
  - *Cadena final y factor 12: correctos, sin factor 2 perdido ni ganado.* `|U_(a)V_(b)-ab/n^2| <= W·1 + 1·W = 2W` ✓; `|D(a,b)| <= nW+2nW = 3nW` (`:121`); `Delta_n <= 4D^*/n <= 12W`, `E[Delta_n^2] <= 144 E[W^2]` (`:328-332`). Verifiqué `4·3=12` y `12^2=144`: exacto.
- **What would have to be true (ataquen esto):**
  1. Que `Delta_n` sea función medible **sólo de `Pi_n`** — lo que licencia transportar la cota puntual `Delta_n<=12W` (probada en el espacio acoplado iid) a `E[·]` bajo la ley uniforme de `Pi_n` del Teorema 1.1. Es inmediato de (1.1), pero el documento **no lo enuncia**.
  2. Que `Law(mapa de rangos de n puntos iid uniformes) = Uniform(S_n)`, que es exactamente `lema_kl:95-105`.
  3. Que el conjunto de empates sea nulo y que `Delta_n` esté acotado (`<=1`), de modo que un conjunto nulo no altere `E[Delta_n^2]`.
  4. Que el objeto **(B)** que `NC-2E` pide sea la esperanza bajo la ley **uniforme** — lo es literalmente: `...selected_variance_clt_scale_d2.md:658`.
- **Risks / failure modes from this lens:**
  - **D1 (menor, declarativo, el único con contenido real).** `grep -i "casi segur|c.s.|empate|probabilidad cero|continu"` devuelve **cero coincidencias**. Sin embargo §3 escribe el orden **estricto** (`:91`) y afirma que la FDE «vale exactamente `a/n`» (`:110-111`); ambas cosas son ciertas sólo en un evento de probabilidad 1. Inocuo para el enunciado `L^2`, pero **debe declararse**: es el tipo de convención tácita que, una vez congelada «para siempre», deja de ser corregible.
  - **D2 (menor, precisión de cita).** `:75` ancla la identificación en `lema_kl §1`; la **uniformidad** de `Pi` está en `lema_kl §2.1:95-105`.
  - **D3 (menor, paso elidido).** El salto de «cota puntual en el espacio acoplado» a «esperanza bajo la ley uniforme de `Pi_n`» no aparece escrito en ninguna línea de §3 ni de §8.
  - **D4 (cosmético, no defecto).** El `2W` de `:117-119` es holgado; el `12` es correcto pero no óptimo. Congelar «para siempre» fija esa holgura, y con ella el `144` y el umbral `n>=10^6`.
  - **Riesgo de encuadre:** `SELF_CONTAINED = YES_NO_EXTERNAL_CITATIONS` debe leerse «sin bibliografía externa», no «sin dependencias».
- **What you could not determine:** correspondencia fichero↔token `NC-2D` `[UNVERIFIED]`; no evalúa `E[W^2]<=290/n` (otro rol), su veredicto es **condicional** a esa cota; no evalúa la política de congelación.
- **Recommendation:** **PROCEED WITH CONDITIONS** — insertar en §3 tres frases sin efecto numérico (declaración «c.s., sin empates»; puntero `lema_kl §1 y §2.1`; «`Delta_n` es función de `Pi_n` sola, luego la cota puntual transporta a la ley uniforme»).

#### Expert brief — Teórico de procesos empíricos
- **Assessment:** Desde la maquinaria probabilística (§§4–6) **PASA CON CORRECCIONES**. No he encontrado ningún error estructural: la cota MGF de Bernstein en ambos signos, la maximal sub-gamma, el Corolario 5.2 y el encadenamiento diádico son todos correctos tal como están escritos, y el argumento cubre `x=1`/`y=1` sin agujero. Pero el texto contiene **una afirmación intermedia literalmente falsa** (el factor `0.72` de la cola) y **cuatro omisiones de rigor**. Ninguna de ellas cambia la constante `17/sqrt(n)` ni, por tanto, `4.2e4`.
- **Load-bearing facts:**
  - **Lema 4.1 correcto (ambos signos).** `:137-153`. El paso `j! >= 2·3^{j-2}` es correcto por inducción; la rama negativa usa `e^{-θ}-1+θ <= θ²/2`, correcta para `θ>=0`.
  - **Lema 5.1 correcto salvo el caso degenerado.** `:161-190`. Jensen no necesita independencia; `θ=t/(1+ct)` cumple `0<θ<1/c` **siempre**; el álgebra cierra en `sqrt(2vL)+cL`. **D1 (leve):** para `m=1`, `L=0`, `θ=0` queda fuera del rango y hace indefinido el `1/θ`; la conclusión sigue siendo cierta por paso al límite, pero la demostración escrita no la cubre. **No se usa nunca con `m=1`**: el Corolario 5.2 aplica a `2m>=2`.
  - **Corolario 5.2 correcto.** `v=np`, `c=1/3` casa con el rango `0<θ<3` del Lema 4.1.
  - **Encadenamiento: estructura correcta.** `x_{k-1}` **sí** queda determinado por `x_k`; la familia `(2^k+1)^2` **sobrecuenta** los pares realizables, lo cual es legítimo; `(2^k+1)^2<=4^{k+1}` ✓; `Q(x_{k-1},y_{k-1})⊆Q(x_k,y_k)` ✓; `λ(A) <= 2·2^{-k}+4^{-k} <= 3·2^{-k}` ✓; la cota vale **uniformemente en `(x,y)`**.
  - **`x=1` / `y=1` están cubiertos.** Para `x=y=1`, `Z(1,1)=0` **exactamente**.
  - **No se necesita continuidad/no-empates dentro de §6** (el grid es determinista, no adaptativo). **D4 (cosmético):** `Z(x,0)=0` es cierto **casi seguramente**, no de forma determinista, y el texto lo afirma sin el «c.s.».
  - **Término de resolución correcto.** `Q\Q_K ⊆ S_x ∪ S_y` ✓; `(N-1)^+ <= binom(N,2)` ✓; `E[Σ_j binom(N_j,2)] = 2^K·binom(n,2)·4^{-K}` es **exacto**; `sup_x P_n(S_x)=max_j N_j/n` **exacto**, no una aproximación.
  - **D2 (leve, pero enunciado literalmente FALSO).** `:255-256`: «sus términos decrecen por un factor menor que `0.72` a partir de `k=16`». El cociente exacto es `sqrt(18.5/35)=0.72703 > 0.72`. La **conclusión sobrevive** (cola `<= 0.05986 < 0.06`). Corrección de una tecla.
  - **D3 (cosmético).** `:253-254`: el término `k=14` se lista como `0.030` cuando vale `0.03076`; la suma se declara `5.111` frente a `5.1131`. Redondeo **a la baja** en una cadena de cotas superiores.
  - **D6 (procedimental, medio).** El oráculo del DOSSIER validó `(4.4(ln n)^2 + 6.1 ln n + 1.2)/n`, pero el texto commiteado en `:265` dice `(4.4(\ln n)^2+6\ln n+2)/n`. **El oráculo no comprobó la expresión literal publicada.** La he verificado a mano y **sí se sostiene**: la diferencia `0.0128L²-0.0533L+0.836` tiene discriminante negativo.
  - **D7 (cosmético).** El paso `0.23333K²+0.93333K <= 0.234K²+0.93K` sólo es cierto para `K>=5`; aquí `K>=60`, pero no se dice.
  - **D5 (leve, omisión).** No se argumenta la **medibilidad de `W`**. Es cierta (continuidad por la derecha ⇒ sup sobre conjunto numerable); sin esa frase, `E[W]` sólo está definida como esperanza exterior.
  - **D9 (cosmético).** El convenio de logaritmo nunca se declara; la aritmética **fuerza** logaritmo natural.
- **What would have to be true:**
  1. Que `X_1,...,X_n` sean **iid** uniformes (no sólo intercambiables): lo usan la factorización MGF y `E binom(N_j,2)`. Lo entrega §3 y **no es mío**: si el condicionamiento a `N=n` dejara dependencia, §§4 y 6 caen.
  2. Que `W` sea la misma variable en §6 y §7.
  3. Que el sup se tome sobre cuadrantes **cerrados** (`Q(x,y)` nunca se define formalmente en §6 — **D8**, notacional).
  4. Que `log` en §5–§6 sea natural (D9).
- **Risks / failure modes from this lens:** el riesgo real **no** es matemático sino de política: congelar «para siempre» un texto con una afirmación numérica falsa y un término mal redondeado. Un lector externo que rehaga la cola con `0.72` obtiene una desigualdad que no se sostiene y concluirá, con razón, que la prueba no fue auditada. Segundo: el oráculo del chair verificó una expresión que **no es la del repositorio**. Tercero: el Lema 5.1 no cubre `m=1` y podría reutilizarse en la parte selectiva con familia unitaria. Lo que **no** es un riesgo: `x=1`/`y=1`, empates, el recuento `m_k`, el sup sobre bandas.
- **What you could not determine:** si §2–§3 entrega genuinamente iid `[UNVERIFIED]`; si el `W` de §7 es medible/integrable bajo la misma construcción; por qué el oráculo usó `6.1/1.2` en vez de `6/2` (no tiene el fuente).
- **Recommendation:** **PROCEED WITH CONDITIONS** — corregir D2 (obligatorio: es falso), D3, y añadir tres frases para D1, D4 y D5, más la reconciliación del oráculo con el texto literal de `:265`.

#### Expert brief — Verificador aritmético y de constantes
- **Assessment: PASA CON CORRECCIONES.** Recalculé de forma independiente (script propio en el scratchpad, sin usar el oráculo del chair) las **veinte** constantes y desigualdades numéricas del documento. El Teorema 1.1 y la cifra publicada `4.2e4` **sobreviven con holgura** (la cadena óptima da `144·254.4 = 36 635`, un 13% por debajo), y el umbral `n>=10^6` **es suficiente para todas**, con monotonía verificada y sin rango de re-fallo. Pero hay **una desigualdad publicada que es literalmente FALSA** (`:255-256`) y cuatro redondeos en dirección insegura.
- **Load-bearing facts:**
  - **[D1 · GRAVE en el texto, INOCUO en el resultado]** `t_17/t_16 = sqrt(18.5/35) = 0.7270292` (ratios `k=16..24: [0.727029, 0.725966, 0.725011, ...]`). La *conclusión* sí se sostiene: `0.0163410/(1-0.727029) = 0.0598636 < 0.06` (margen **0.23%**), cola exacta `0.0593775`. El oráculo del chair **no testeó esta frase**. Corrección segura: `0.72`→`0.7271` **y** `0.0163`→`0.01635`, o declarar la cola `<0.061`.
  - **[D2 · MENOR, traza de auditoría]** `t_14` figura como `0.030`; el valor es `0.0307584`. La suma declarada `5.111` está **por debajo** de la verdadera `5.1130863`; 11 de 15 términos redondeados hacia abajo. Sin efecto: total exacto `5.1724638 <= 5.2`.
  - **[D3 · MENOR]** `1.183` es redondeo **a la baja** de `1.1832160`. Absorbido: `sqrt(6)·sqrt(1.4)·5.2 = 15.0710 <= 15.1`.
  - **[D4 · MENOR]** El paso `(1.4/3)[K(K+1)/2+1.5K] <= 0.234K^2+0.93K` usa `0.93` (**abajo, inseguro**) y **es falso para `K=1,2,3,4`** (`K=1: 1.16667 > 1.16400`); sólo vale `K>=5`. Irrelevante (`K=60`), pero escrito sin condición.
  - **[D5 · MENOR]** El desarrollo exacto es `4.38724L^2 + 6.05334L + 1.164`; se publica `4.4L^2+6L+2`, donde **`6` es redondeo a la baja de `6.05334`**. Válido porque la diferencia tiene **discriminante `-0.039816 < 0`** — pero el documento no da esa razón.
  - **[iii — umbral y monotonía · VERIFICADO OK]** En `n=10^6` el margen es **7.5%**, el más estrecho de la nota. Suficiencia: el primer `n` válido es `n* = 805 074`; `10^6` sobra por un factor **1.24** solamente. **No hay re-fallo**: cruce único, cociente estrictamente decreciente. Barrido de la cantidad **exacta** en ~1140 puntos de salto más 200 valores hasta `10^300`: **0 violaciones**, peor cociente `0.9035`.
  - **[iv — `L_k <= 1.4(k+1.5)` · OK PARA TODO `k`]** `log2+(k+1)log4 = 1.3862944k+2.0794415 <= 1.4k+2.1` para **todo `k>=0`**. Chequeo exacto `k=0..699`: `max[log(2m_k) - 1.4(k+1.5)] = -0.0205585`.
  - **[v — Corolario 8.1 · OK, redondeo SEGURO]** `2·(65+42000) = 84 130`; `4e4·84130 = 3.3652e9 <= 3.4e9` (holgura `3.48e7`). El `+1` se absorbe para `c<=1`. **`3.4e9` está redondeado hacia arriba = dirección segura.**
  - **[Resto · TODAS CORRECTAS]** `144·290 = 41 760 <= 4.2e4` ✓; `17^2+1 = 290` ✓; `16.1/sqrt n + 3/n <= 17/sqrt n ⟺ n >= 11.11` ✓; `2.2/n+3n^{-3} <= 3/n` ✓; `(1+1/(2n))/n <= 1.1/n ⟺ n>=5` ✓; `2^60/10^18 = 1.1529` ✓; `3/ln2 = 4.328085 <= 4.33` ✓; `9.3e-4` es redondeo **arriba** del verdadero `9.2471e-4` ✓; `p_k=3·2^{-k}` ⟺ `4^{-k}<=2^{-k}` ✓.
  - **[D6 · PROCEDIMENTAL, defecto del DOSSIER no del documento]** El oráculo del chair evaluó `6.1 ln n + 1.2`; **el literal publicado en `:265` es `6 ln n + 2`**. Mi recómputo confirma que la publicada también es válida, pero esto demuestra empíricamente que la verificación por el coautor **no basta**: no cubrió `:265` ni la frase falsa `D1`.
  - **[vi — `numbers-must-come-from-committed-script` · FUERA DE ÁMBITO POR PRECEDENTE]** La memoria describe un fallo con números *empíricos*; aquí las constantes son **deductivas**, re-derivables sin dato, semilla ni sello. Precedente uniforme: `grep -rln "2800\|26a_n\|NC-2C" --include=*.py .` → **sin resultados**; las quince notas de la familia llevan la cabecera «SIN DATOS, SIMULACIONES, SEMILLAS, CÓDIGO NI ARTEFACTOS NUMÉRICOS NUEVOS». Además `NC-2F §5` **prohíbe** crear el script que el remedio pediría. **No viola la regla.** Pero el *porqué* de la memoria sí obliga, y `D1` es exactamente su violación: un número publicado que no es correcto.
- **What would have to be true:** que `NC-2E` Cor. 8.2 y Thm 8.1 sean lógicamente válidos; que `m_k=(2^k+1)^2` sea el conteo correcto (**rol combinatorio**) — si estuviera mal por un factor `2^j`, `L_k` crecería `0.693j` y `1.4(k+1.5)` fallaría: el margen de `L_k` es sólo `0.0206` en `k=0`; que `W>=0`; que la serie se sume sobre **todo** `k>=1`.
- **Risks / failure modes from this lens:**
  - **El margen del 0.23% en la cola** (`D1`). Si alguien "corrige" `0.72` a `0.728`, la cota geométrica pasa a `0.060078 > 0.06` y **la frase vuelve a ser falsa**.
  - **Patrón sistemático de redondeo a la baja de cotas superiores**: seis instancias, cada una rescatada por holgura en *otro* término, **por accidente, no por diseño**.
  - **Estrangulamiento del umbral**: `n* = 805 074` frente a `10^6` publicado, factor `1.24`. Es la cifra más frágil de la nota, más que `4.2e4`.
  - **Verificación no independiente**: el oráculo lo produjo el coautor y —demostrablemente— evaluó una expresión distinta de la publicada.
- **What you could not determine:** si `m_k=(2^k+1)^2` es correcto (rol combinatorio); si `NC-2E` Cor. 8.2 requiere `c_1` para todo `n` grande o sólo `n>=n_2`; si algún otro documento del repo cita ya `4.2e4`, `290/n` o `17/sqrt n`.
- **Recommendation: PROCEED WITH CONDITIONS.** El Teorema 1.1 y la constante `4.2e4` son aritméticamente correctos y el umbral es suficiente y monótono, pero el PI **no debe declarar cerrada de forma definitiva** una nota que contiene una desigualdad publicada falsa más cinco redondeos en dirección insegura; condiciono la clausura a un parche mínimo y puramente textual de `D1`–`D5` y a que ese parche lo verifique **alguien que no sea coautor**.

#### Expert brief — Auditor de integración y techo de afirmación
- **Assessment:** **PASA CON CORRECCIONES** en la pieza que se me pide auditar (el objeto (B) sí queda cerrado: la cantidad acotada es literalmente la que `NC-2E` necesita, y `c_1` entra donde debe), y **NO PASA** la acción de una sola dirección que se propone encima de ella. La auditoría cubre *un* teorema; la decisión pretende congelar *toda* la parte incondicional del programa, que es un objeto estrictamente mayor (incluye `NC-2E` Lema 6.1, Lema 6.2, Lema 5.1, la identidad (2.7), y la cota incondicional de `Pr_n(S)` de `NC-2C`/`NC-2F(a)`), ninguno de los cuales ha sido auditado en esta sesión.
- **Load-bearing facts:**
  - **La cantidad es la misma.** `Delta_n` de `NC-2F(B)` (`:16-23`) es literal y simbólicamente idéntica a (2.6) de `NC-2E` (`:135-142`). La esperanza es bajo la ley uniforme, sin condicionar por `S`. Esto es exactamente **(B)** de `NC-2E` Cor. 8.2 (`:661-666`).
  - **`c_1` entra donde debe.** `C_\Delta = 2(65+c_1)/c`, con `65` del Lema 6.1 (`:391-401`); `C_q = 4·10^4 C_\Delta + 1` (`:625-630`). Oráculo: `3365200001.0 <= 3.4e9`. La sustitución es correcta.
  - **Append-only respetado.** `git diff 9e5ac5c^ ea732ff --stat`: sólo 3 ficheros nuevos + 15 líneas del marcador de memoria; ningún documento `NC-2C/2D/2E` tocado.
  - **DEFECTO 1 (GRAVE-MODERADO, integración).** `NC-2F(B)` Cor. 8.2 (`:349-362`) reescribe la obligación residual como `sum_{pi in S_n} Delta_n(pi)^2 <= (C/n)|S_n|`, **sin `R`**. La obligación real de `NC-2E` Teorema 8.1 es `sum_{pi in S_n}(R+Delta_n)^2 <= (C_\Delta/n)|S_n|` (`:610-618`). La frase «junto con la parte de anclaje, ya probada incondicional y libre de logaritmo en `NC-2E` Lema 6.1» (`:358-359`) es cierta pero engañosa en ese sitio: el Lema 6.1 es **incondicional**, no **relativo a `S_n`**; la única cota relativa disponible para `R` es el Lema 6.3, `E_{nu_n}[R^2]<=17L_n/n` (`:437-449`), que con `L_n` de `NC-2F(a)` **explota**. Tras `NC-2F(B)`, `R` y `Delta_n` están exactamente en la misma situación, y la «única obligación» está enunciada **de menos**.
  - **DEFECTO 2 (MODERADO, propagación).** El mismo error ya salió del documento: `memoria_claude/program-status-reentry-marker.md:113` dice «La única obligación que queda para cerrar O3 es selectiva: `sum_{pi in S_n} Delta_n^2 <= (C/n)|S_n|`», mientras el texto previo del mismo fichero lo enunciaba correctamente con `(R+Delta_n)^2`. Y en el mismo commit conviven dos nombres distintos para la obligación residual: `NC2F_REMAINING_OBLIGATION = LOWER_BOUND_ON_SELECTION_MASS` (nota §8) vs `NC2F_B_REMAINING_OBLIGATION = RELATIVE_DISCREPANCY_SUM_OVER_S_n` (`:399`).
  - **DEFECTO 3 (MODERADO, etiquetado).** `grep -ni "condicional"` devuelve **sólo** `:1`, `:3` y `:358`, todas dentro de «incondicional». El Corolario 8.1 nunca se etiqueta CONDICIONAL; su condicionalidad descansa entera en la cláusula «si además existiera `c>0`» (`:339`). Peor: el techo de afirmación §9 (`:366-367`) inventaría lo demostrado y **omite los Corolarios 8.1 y 8.2** (y el 7.2). Mitigación parcial: el token `NC2F_B_CONDITIONAL_CLOSURE` (`:396`) vive en §10, no junto al corolario.
  - **DEFECTO 4 (MENOR).** El documento nunca dice cuán lejos está (A). Un lector de `NC-2F(B)` en aislamiento no aprende la cota de `...selection_mass_sqrt_scaling_d2.md:186`.
  - **DEFECTO 5 (GRAVE si entra en el brief — corrección a la premisa del DOSSIER).** El DOSSIER afirma que «`NC-2F(a)` demuestra `Pr(S) -> 0`». **No lo demuestra.** `:186` es una **cota inferior**. `grep` no devuelve ninguna cota superior para `Pr_n(S)` en el repositorio. Registrar «(A) es falso» sería una sobreafirmación nueva creada por este propio foro.
  - **DEFECTO 6 (MENOR, dominio).** El Teorema 1.1 vale para `n>=10^6`; el Corolario 8.1 pasa por `NC-2E` Lema 6.3/Teorema 7.1, que exigen `n>=10^{40}`. Falta esa línea.
  - **Sobre `NC2F_B_SELF_CONTAINED`.** Textualmente lo sostengo: §§4–7 demuestran todo in situ. Dos matices: (i) el token es **más fuerte** que el terminal precomprometido, que decía «autocontenido salvo citas verificadas»; (ii) es una afirmación absoluta que una sola apelación no demostrada falsificaría.
  - **Sobre novedad.** No infringe la prohibición: es un **descargo**, reforzado por `NOVELTY_CERTIFIED = NO`. Único reparo: «el enunciado (1.2) es del tipo clásicamente asociado al proceso empírico bidimensional» es una aserción bibliográfica **sin ancla** y debería llevar `[UNVERIFIED]` o borrarse.
  - **Independencia y procedimiento.** La nota §1 declara que el refrendo es posterior a la ejecución; token `NC2F_SIGNATURE_PRECEDES_EXECUTION = NO`. El autor del documento es el PI que refrenda y el chair de este foro.
  - **Tasa base de «cierres definitivos».** `docs/program_closure_note_2026-07-30.md:153` declara el programa cerrado; `ls docs/ | grep reopening` devuelve **11 notas de reapertura** posteriores. La probabilidad empírica de que un cierre declarado se mantenga es baja, y el mecanismo barato ya existe: reapertura acotada con nota firmada.
- **What would have to be true:**
  1. Que §2-§7 sean correctos — no es mi remit; mi «PASA CON CORRECCIONES» es **condicional a los veredictos de los roles de probabilidad y aritmética**.
  2. Que el objeto (B) sea *exactamente* `E[\Delta_n^2]<=c_1/n` bajo la ley uniforme — verificado.
  3. Que «cerrar la parte incondicional» signifique sólo el Teorema 1.1. Si significa el conjunto entero, mi veredicto sobre la acción es NO PASA sin más discusión.
  4. Que el `+1` se absorba para todo `c` relevante — cierto para `c<=1`.
- **Risks / failure modes from this lens:**
  - **El riesgo dominante no es que el Teorema 1.1 sea falso, sino que el Corolario 8.2 mal enunciado se convierta en la definición operativa de «lo que falta».** Ya ocurrió: el marcador de memoria es la puerta de entrada de cualquier sesión futura. Congelado, el programa perseguiría una obligación estrictamente más débil que la real y podría un día declarar `NC2E-O3` cerrado con una prueba que no cubre `R`.
  - **Lectura futura del Corolario 8.1 como cierre conseguido.** A tres saltos de cita, la hipótesis `Pr_n(S)>=c` se evapora. Es el patrón exacto que la nota §5 prohíbe.
  - **Radio de explosión si aparece un error en seis meses (medido):** caería `NC-2F(B)` entero, el Corolario 8.1 y la línea `:113` del marcador. **No** caería `NC-2F(a)`; **no** caería `NC-2E` (es anterior y su terminal ya publica `NC2E_MISSING_OBJECT_B` como abierto). El daño es **reparable y localizado — siempre que el repositorio siga siendo reabrible**. Congelar convierte una reparación barata en una falsedad publicada e incorregible.
  - **Gobernanza.** La configuración propuesta es la más débil posible para el compromiso más fuerte posible.
- **What you could not determine:** si §2-§7 son correctos; **qué se entiende exactamente por «toda la parte incondicional del programa»** — sin una lista literal, la decisión es inauditable, y **esto solo ya bloquea el cierre**; si algún consumidor externo (PR #7, manuscrito) cita ya `c_1=4.2·10^4`; si `Pr_n(S)` está acotado inferiormente o no.
- **Recommendation:** **PROCEED WITH CONDITIONS** — cerrar el objeto (B) como resultado, sí; declarar cerrada para siempre «toda la parte incondicional», no. Condiciones mínimas: (1) corregir el Corolario 8.2 y la línea `:113` del marcador para restituir `(R+Delta_n)^2`; (2) etiquetar el Corolario 8.1 como CONDICIONAL, darle dominio `n>=10^{40}` e incluirlo en el inventario de §9; (3) añadir la referencia cruzada a `NC-2F(a):186` y **no** registrar que (A) sea falsa; (4) sustituir el cierre irreversible por el mecanismo que este repositorio ya usa once veces — cierre con cláusula de reapertura acotada.

## 5. Falsifier attack

### Falsifier attack

- **Concrete failure modes:**
  1. **False intermediate claim, rescued only by luck.** `:255-256` states the terms decay "por un factor menor que `0.72`" from `k=16`. Independent recomputation (`t_k=sqrt((k+1.5)*2^-k)`) gives `t_17/t_16 = 0.7270291800`, i.e. **> 0.72**, so the sentence as literally written is false — confirmed independently, not just by the chair's Oráculo 2/3. The numeric conclusion survives only because plugging the document's own false factor into the geometric bound gives `0.05836 < 0.06` (margin **2.7%**), and the chair's own Oráculo 3 shows the margin flips to failure (`0.060095>0.06`) under a nearby "correction" (`r<=0.7271, t16<=0.0164`). A document about to be declared closed forever contains a disprovable statement whose truth-preserving rescue is a coincidence of slack, not a valid proof step.
  2. **Corolario 8.2 of the audited document silently drops a term that NC-2E's own Theorem 8.1 requires.** Direct read of both files: NC-2E `:610-618` boxes `(8.1)` as `sum_{pi} (R(pi)+Delta_n(pi))^2 <= (C_Delta/n)|S_n|`. The audited document's own `Corolario 8.2` (`:349-362`) restates the "única obligación" as `sum_{pi} Delta_n(pi)^2 <= (C/n)|S_n|` — **no `R` term**. This is not cosmetic: Lemma 6.3 (`:437-449`) gives `E_{nu_n}[R^2] <= 17 L_n/n` with `L_n = log(1/p_n)+log n`, and NC-2F(a) Theorem 5.1 (`:186`) only bounds `log(1/p_n) <= 41*sqrt(n)*(log n)^{3/2}` — i.e. `R`'s relative bound is *not* `O(1/n)`, it can dominate. Dropping `R` from the "one remaining obligation" mischaracterizes what is actually left to prove `NC2E-O3`.
  3. **That exact error has already propagated into the memory gateway file.** `memoria_claude/program-status-reentry-marker.md:113` reads: *"La única obligación que queda para cerrar O3 es selectiva: `sum_{pi in S_n} Delta_n^2 <= (C/n)|S_n|`"* — same omission, verbatim, in the file every future session reads first.
  4. **Three different, non-matching labels for the same "one remaining obligation"** across three files: `NC-2E:610-618` = `(R+Delta_n)^2`; reopening note `:183` = `NC2F_REMAINING_OBLIGATION = LOWER_BOUND_ON_SELECTION_MASS`; audited doc terminal = `NC2F_B_REMAINING_OBLIGATION = RELATIVE_DISCREPANCY_SUM_OVER_S_n`. None of the three is the literal boxed statement in NC-2E. A "close forever" action would freeze this inconsistency permanently.
  5. **The decision's own object is undefined.** `grep -rl "parte incondicional"` across the whole repo returns **zero files**, while `emergencia/` contains 30 `P1a_*` files. The DOSSIER asks to close "toda la parte incondicional" but no manifest enumerates what that set is — the integration auditor's objection is not speculative, it is confirmed by an empty grep.

- **Unanchored claims:**
  - Combinatorist: "no encuentro ningún defecto matemático" in §2-3, while their own "what would have to be true" (1) states "`Delta_n` medible sólo de `Pi_n`... EL DOCUMENTO NO LO ENUNCIA" — an admitted gap dressed as a PASA verdict.
  - Empirical-processes theorist: "(2^k+1)^2 SOBRECUENTA los pares realizables, lo cual es legítimo" — asserted, no oracle recomputation of `m_k`; the same author later lists `m_k` correctness under "what would have to be true," i.e. certifies and doubts the same fact in one brief.
  - Integration auditor: "el daño es reparable SIEMPRE QUE el repositorio siga siendo reabrible" — directly contradicted by the decision question itself, which is precisely a proposal to make the repository *not* reabrible for this part.
  - DOSSIER's own "Corrección 2" (chair-authored, post-wave-1): declares the NC-2D file↔token correspondence "CONFIRMED" with no command/output shown, upgrading it from the combinatorist's explicit `[UNVERIFIED]`.

- **Assumption attacks:**
  - The combinatorist's necessary condition "`Delta_n` is a measurable function of `Pi_n` alone" is flagged by the same brief as unstated in the document, yet still counted toward PASA CON CORRECCIONES as a "purely textual" fix — an unproven mathematical precondition is not a textual fix.
  - The empirical-processes theorist assumes iid-exactness is "delivered by §3, and NOT its own" role; the combinatorist (who owns §2-3) never certifies iid-exactness against conditioning on `N=n`, only cites `Law(rangos)=Uniform(S_n)`. Each brief assumes the other closed this loop; neither did.
  - Integration auditor's "what would have to be true": *"que 'cerrar la parte incondicional' signifique sólo el Thm 1.1"* — confirmed above (empty grep) that this scope is nowhere defined in-repo, so this assumption is neither true nor false, it's unresolved, and the decision as posed cannot be answered PASA without resolving it.
  - Cross-brief inconsistency on `m_k=(2^k+1)^2`: arithmetic verifier marks it `[UNVERIFIED]` from their role and flags it as the tightest margin in the whole proof (`k=0` margin `0.0206`); no role actually re-derives it from the chaining construction.

- **Constraint violations:**
  - `NC2F_B_UNCONDITIONAL = YES` and the decision's own framing demand permanent, uncorrected closure, yet the operative verdict from all four wave-1 experts is "PASA CON CORRECCIONES" — corrections that, as of `ea732ff` (current `HEAD`, tree clean per `git status --porcelain`), are **not in the committed file** (`:255-256` still reads "menor que `0.72`"). A "correction" that exists only as a brief recommendation, not as a diff, is a barrier that can fail silently — the exact "decoración" CLAUDE.md prohibits.
  - Oracle-provenance failure: two independent expert briefs report that the chair's own Oráculo 2 validated `(4.4L^2+6.1L+1.2)/n`, a **different expression** from the one actually committed at `:265`. The chair's own verification apparatus tested the wrong literal text and this was caught only by independent reading, not by the oracle itself.
  - Scope creep by the chair post-wave-1: "Corrección 1" unilaterally forbids any role from recording `(A)` as false, and "Corrección 2" converts an `[UNVERIFIED]` into `CONFIRMED` — both edits made by the same person who authored and ratified the audited document, after seeing the wave-1 briefs, with no independent second check shown.

- **Irreversibility / blast radius:** The decision is explicitly one-way ("congela para siempre... no se vuelve a auditar"). The R-omission (failure mode 2 above) is already inside `memoria_claude/program-status-reentry-marker.md:113`, the file every future session reads first. If frozen, any future attempt to discharge "the one remaining obligation to close NC2E-O3" will target `Delta_n` alone and never address `R`, which per Lemma 6.3 + NC-2F(a) Thm 5.1 can be relatively unbounded — risking either wasted future effort or a downstream false "closure" of `NC2E-O3`, with no permitted mechanism to reopen and catch it. Absorbed by: any future contributor/session that trusts the marker file and the frozen terminal, silently and indefinitely.

- **Independent-verification gate:** Failed by construction. The reopening note shows the same person, Ignacio Martín, as `AUTORIZACION` and `REFRENDO` (PI), and per the DOSSIER's own framing this person is also the chair convening this forum. The three "oráculos del chair" that anchor the DOSSIER's headline numbers were produced by this same person outside the repo, not committed — and one of them (Oráculo 2) was shown by two independent briefs to have checked a non-literal expression. The author of the audited document, the PI who ratifies it, and the chair who curated the DOSSIER are one and the same actor.

- **Correlated-error check:** All four wave-1 briefs converge on "PASA CON CORRECCIONES" and on the identical pair of defects (the `0.72` ratio, the `t_14`/sum rounding) — both of which were already surfaced verbatim in the DOSSIER's own "Oráculo 2/3" section *before* the briefs were written. This is agreement anchored to a shared, chair-supplied error list, not four independently-derived defect sets; it raises the risk that experts stopped searching once they'd confirmed the pre-flagged items, and explains why deeper items (the `m_k` recount, the `(R+Delta_n)^2` vs `Delta_n^2` mismatch) were found by just one role each rather than cross-checked by all.

- **Minimal falsification test:** Already executed, read-only, in the scratchpad: `python3` recomputation of `t_k=sqrt((k+1.5)*2^-k)` for `k=16,17` gives ratio `0.7270291800` (document's `:255-256` claim of `<0.72` is false) and geometric-tail-with-false-factor `= 0.05836077 < 0.06` (margin 2.7%, not robust). Second executed check: `sed -n` diff of NC-2E `:607-618` boxed `(8.1)` against the audited document's `Corolario 8.2` `:349-362` shows the `R` term is dropped — a direct textual, not inferred, mismatch. Third executed check: `grep -rln "parte incondicional" .` returns zero files, confirming the decision's scope object is undefined in-repo. All three checks are reproducible by any future auditor with no repo modification.

- **Attacks I could not make executable:**
  - Whether §2-3's iid/measurability gap actually breaks §4/§6 — would require re-deriving the probability construction from scratch; not done here. INCONCLUSIVE.
  - Whether `m_k=(2^k+1)^2` is the exact correct dyadic pair count for the chaining argument — would require rebuilding the §6 chaining combinatorics independently; not done. INCONCLUSIVE.
  - Whether `n*=805074` and the reported 1140+200-point sweep are correct — I only reproduced the `k=16` tail piece. INCONCLUSIVE.
  - Whether any downstream/external consumer already cites `c_1=4.2e4` or `290/n` — not searched outside this repo. INCONCLUSIVE.

## 6. Commitment warden verdict

### Commitment warden verdict
- Verdict: **BLOCK**

- Commitments on record:
  - `FORO.md` — verified absent (`ls FORO.md` → "No such file or directory"). No forum-specific domain layer exists, so the only binding record is the `NC-*` note chain and `CLAUDE.md`.
  - `docs/program_closure_note_2026-07-30.md:5` — closure is explicitly `CLOSURE_IS_DEONTIC_NOT_ALETHIC`.
  - `docs/program_closure_note_2026-07-30.md:29-34` — "Naturaleza del acto... Este cierre es un acto **deóntico**... No es, y no debe leerse como, un acto **alético**: no afirma que esté probado que no existe ningún camino científico legítimo." A revisable, non-final closure is the repo's own definition of "closed."
  - `docs/program_reopening_note_2026-08-18_nc2f_variance_exponent_reduction.md:16` — `ALCANCE_AUTORIZADO: opción 1 presentada al PI (piezas (a) y (b) de abajo)`, a closed list (§3).
  - `...nc2f_variance_exponent_reduction.md:103` — §5 prohibition: "no afirmar que `NC2E-O3` queda cerrado ni que `liminf T_n^h>0`."
  - `...nc2f_variance_exponent_reduction.md:205-209` — §9: the ratification covers only "los dos terminales emitidos, los dos documentos científicos de §7 y el commit de todo ello. No amplía el perímetro de §3, no levanta ninguna prohibición de §5... La cadena vuelve al procedimiento normal —firma previa conforme a borrador— en la siguiente autorización."
  - `emergencia/P1a_count_volume_rectangular_discrepancy_l2_d2.md:369` (§9) — `NC2E.1` ni `NC2E-O3`, que siguen abiertos.
  - `emergencia/P1a_count_volume_rectangular_discrepancy_l2_d2.md:399` — token `NC2F_B_NC2E_O3 = OPEN`.
  - `CLAUDE.md:37-39` — founding rule: thresholds/criteria are "anchored to principled bases and frozen before any validation data is seen."
  - Precedent of bounded, not definitive, closure: 11 `docs/program_reopening_note_*` files postdate the 2026-07-30 closure (verified by `ls docs/ | grep -i reopening`), all operating under an append-only, scope-limited reopening mechanism, never a "never touch again" declaration.

- Pre-commitment status: **Not met, on two independent grounds.**
  1. For `NC-2F` itself: the note self-declares that the terminals of §4 and the execution happened "en la **misma** sesión" with ratification only "posterior" (`...nc2f_variance_exponent_reduction.md:32-43`, tokens `NC2F_RATIFIED_BY_PI = YES_AFTER_EXECUTION`, `NC2F_SIGNATURE_PRECEDES_EXECUTION = NO` at lines 190-191). This is an admitted deviation from the chain's own norm and from `CLAUDE.md:37-39`.
  2. For the decision actually on the table — declaring "cerrada de forma definitiva toda la parte incondicional del programa" — there is **no criterion for this step anywhere in the record**. No note defines "la parte incondicional del programa" as a governed object, no note sets a threshold or test for declaring it definitively closed, and `NC-2F` §9 explicitly disclaims doing so (line 206). A criterion invented after seeing the audit result fails pre-commitment by definition.

- Reversibility classification: The proposed action is explicitly framed by the DOSSIER itself as "Decisión de UNA SOLA DIRECCIÓN: congelar para siempre". This is one-way. Everything on record that this decision would supersede is instead built as **reversible/bounded**: `docs/program_closure_note_2026-07-30.md:29-34` (deontic, revisable by design) and 11 subsequent bounded reopenings. No note on record authorizes converting that revisable mechanism into a permanent, alethic, never-to-reopen state. The closest is the `NC-2F` refrendo, which §9 confines to the two terminals and explicitly returns the chain to normal procedure for "la siguiente autorización" (line 209), i.e., anticipates further notes, not a freeze.

- Scope: **Widens it, silently.** `NC-2F` §3 authorized exactly two narrow technical objectives and §5 forbids claiming `NC2E-O3` is closed. The note's own terminal states `NC2E-O3` remains `OPEN` (`:399`) and piece (A) is actually unproven. Declaring the entire "parte incondicional del programa" definitively closed is a strictly larger claim than anything `NC-2F(B)` proves or than anything its authorizing note permits asserting.

- Reporting symmetry: **Fails as proposed.** The document itself reports negatives correctly in its own §9. But the *decision being asked* would bury, at forum-summary altitude, several negative findings carrying equal evidentiary weight: `NC2E-O3` still open (`:399`), the false sentence at `:255-256`, the propagated Cor 8.2 defect now sitting in a committed memory file (`memoria_claude/program-status-reentry-marker.md:113-114`), and piece (A)'s missing upper bound. None of these disqualifies the theorem locally, but all of them disqualify the proposed *global, irreversible* action.

- Forbidden moves present?
  - **Author verifying their own claim: YES.** The DOSSIER states it: the author of the audited document is also the forum chair and the ratifying PI. Wave 1's arithmetic verifier made independent verification an explicit precondition for any remedy — a condition unmet by a chair-author-PI closing the loop alone.
  - **Silent scope widening: YES** (see Scope above).
  - **Post-hoc relaxation of a fixed criterion: YES** for the meta-decision (no criterion for "definitive incondicional closure" existed before this question was posed).
  - Re-run after peeking / outcome coercion: not directly evidenced in the record reviewed; `[UNVERIFIED]`.

- Reasons:
  - `docs/program_closure_note_2026-07-30.md:29-34` defines this repository's closure mechanism as deliberately non-final; the proposed action contradicts that design.
  - `...nc2f_variance_exponent_reduction.md:205-209` (§9) is the PI's own ratification, and it explicitly bounds itself to the two `NC-2F` terminals.
  - `emergencia/P1a_count_volume_rectangular_discrepancy_l2_d2.md:369,399` — the audited document itself says `NC2E-O3` is open.
  - Chair = author = ratifying PI is a self-verification pattern the record's own procedural expectations treat as insufficient for a step of this consequence.
  - 11 reopening notes postdating the closure are the repository's *revealed* practice: closures here get reopened when warranted, not frozen.
  - `CLAUDE.md:37-39` — no criterion for "definitive incondicional closure" was ever frozen, so none exists to be satisfied here.

## 7. Source verdict

### Source verdict

| Source | Claimed by | Claim it was cited for | Status |
| --- | --- | --- | --- |
| `...rectangular_discrepancy_l2_d2.md:14-17`, `...selected_variance_clt_scale_d2.md:136-139`, `...selected_interior_mass_d2.md:432-439`, `...selected_second_moment_d2.md:216-223` | Combinatorista | "The four definitions of `Delta_n` are literally the same formula; no definitional drift" | CONFIRMED — all four give `Delta_n = max_{I,J} \|N_{Pi_n}(I,J)/n - \|I\|\|J\|/n^2\|` verbatim |
| `...lema_kl_d2.md:95-107` (§2.1) | Combinatorista | Rank permutation of iid continuous sample is uniform and independent of order statistics | CONFIRMED — verbatim at 95-107 (2-line drift); this is what makes the reduction non-circular |
| `...selected_interior_mass_d2.md:111-127` | Combinatorista | NC-2C's Lemma 3.1 is a self-contained Azuma bound, **not used** in NC-2F(b) §§2-7 | CONFIRMED, with caveat: NC-2F(b) has its **own** differently-proved "Lema 3.1"; the label collision is a real risk for a careless reader |
| `...rectangular_discrepancy_l2_d2.md:75` vs `lema_kl` §1/§2.1 | Combinatorista | Doc anchors the identification in §1, but the supporting fact is in §2.1 | CONFIRMED on close reading — §1 only *defines* `Pi`; that it is **uniform** is proved only in §2.1 |
| `...rectangular_discrepancy_l2_d2.md:255-256` | Procesos empíricos | Text claims factor <0.72 from k=16; marked FALSE | CONFIRMED — ratio 0.7270291799…; the bound only becomes true for k≥26 |
| `...rectangular_discrepancy_l2_d2.md:253-254` | Procesos empíricos | k=14 tabulated 0.030, sum declared 5.111 | CONFIRMED — true term 0.030758, true sum 5.11309 |
| `...rectangular_discrepancy_l2_d2.md:265` | Procesos empíricos | Published literal is `(4.4(ln n)^2+6 ln n+2)/n` | CONFIRMED — verbatim match |
| `...rectangular_discrepancy_l2_d2.md:235-236` | Procesos empíricos | `m_k=(2^k+1)^2<=4^{k+1}` and `L_k<=1.4(k+1.5)` | CONFIRMED — verbatim |
| `...selected_variance_clt_scale_d2.md:391-396`, `:620-627`, `:654-660` | Aritmético | `E[R^2]<=65/n`; `C_q=4·10^4 C_Delta+1`; `C_Delta=2(65+c_1)/c` | CONFIRMED — all three present, minor line drift |
| `memoria_claude/numbers-must-come-from-committed-script.md` | Aritmético | Memory describes an EMPIRICAL-number failure; remedy = emit from committed script | CONFIRMED for literal content. The inference "therefore deductive constants are exempt" is the role's own extrapolation, **not stated in the source** |
| `...rectangular_discrepancy_l2_d2.md:349-362` vs `...variance_clt_scale_d2.md:609-618,663-678` | Integración | Cor 8.2 states the residual obligation WITHOUT `R`, contradicting NC-2E's explicit "obligación literal que falta" | CONFIRMED verbatim on both sides — the gravest, best-supported finding in the dossier |
| `memoria_claude/program-status-reentry-marker.md:113-114` | Integración | Committed marker already propagates the version without `R` | CONFIRMED — while the same file's NC-2E summary two lines above (102-104) correctly carries `(R+Delta_n)^2`. The marker documents the drift in the act of committing it |
| `...rectangular_discrepancy_l2_d2.md:366-367` (§9) | Integración | §9 omits Corolarios 8.1, 8.2, 7.2 from the list of proved results | CONFIRMED — Cor 7.2 (proved at 319, used in the QED at 328) and Cor 8.1/8.2 (337/349) are absent |
| `:339` and `:396-397` | Integración | Cor 8.1's conditionality rests entirely on "si además existiera c>0"; the token lives in §10 | CONFIRMED — token at 397, inside §10, while Cor 8.1 is at 337 |
| `...selection_mass_sqrt_scaling_d2.md:186,193`; repo-wide search | Integración | The `Pr_n(S)` bounds; and no upper bound exists, so (A) is open | CONFIRMED for both formulas. Repo-wide grep found **no unconditional** upper bound. One *conditional* bound exists (`docs/backlog_hallazgos.md:1209`, EF3.11: `p_n<=(4/q)n^4 exp(-nq^2/8)`), explicitly contingent on an unproven hypothesis — it does not refute (A) |
| `...selected_variance_clt_scale_d2.md:437-449` (Lema 6.3) | Integración | `E_nu[R^2]<=17 L_n/n` is the only relative bound for `R`, and it explodes | CONFIRMED — no other `E_{nu_n}[R^2]` bound in the repo; combined with NC-2F(a), `E_nu[R^2]=O((log n)^{1.5}/√n)`, far worse than the `O(1/n)` needed |
| `docs/program_closure_note_2026-07-30.md:153`; `ls docs/ \| grep reopening` | Integración | Closure declared; eleven later reopening notes | CONFIRMED — line 153 verbatim; the grep returns exactly 11 files |
| `docs/program_reopening_note_2026-08-18_nc2f...md` §1, §8/§9 | Integración | Ratification posterior to execution; tokens `NC2F_SIGNATURE_PRECEDES_EXECUTION=NO`, `NC2F_RATIFIED_BY_PI=YES_AFTER_EXECUTION` | CONFIRMED — §1 (28-42) states it explicitly; tokens verbatim at 190-191 |
| `...rectangular_discrepancy_l2_d2.md:375-378` | Integración | "(1.2) is of the type classically associated with the 2-D empirical process" is unanchored | CONFIRMED — verbatim; no citation accompanies the sentence |
| `git diff 9e5ac5c^ ea732ff --stat` | Integración | Append-only respected: 3 new files + 15 lines of the marker | CONFIRMED on re-run — no NC-2C/2D/2E file appears |

- Unsupported claims: none of the 20 citations point to a source that fails to exist or says something contradictory to what was claimed. The one soft spot is citation 10: the further conclusion "therefore deductive constants fall outside the rule" is the Aritmético's own inference, not text in the source — treat that inference as argued-but-uncited, not as a misquote.

- Uncited substantive claims: (a) the Combinatorista's claim rests on two objects both labelled "Lema 3.1" in different documents with unrelated proofs; no brief flags this naming collision itself as a risk. (b) The claim that Corolario 8.2 is "wrong" (as opposed to "an alternative, unproved weaker sufficient route" per NC-2E's own §8 remark 3 that (8.1)-with-R is not claimed necessary) is not directly asserted in any single sourced line — it follows from cross-reading NC-2E lines 674-678 against NC-2F(b) 349-362, which I did and which holds up, but no brief cites NC-2E's own caveat ("Lo que el Teorema 8.1 no dice… no se ha probado ninguna implicación recíproca," lines 684-685) that would complicate a claim of outright falsity rather than omission/mislabeling.

- Notes: (1) Several citations show 1-2 line drift; all within tolerance and noted per-row. (2) Citation 15's "no upper bound anywhere" is correct but there is a *conditional* upper bound at `docs/backlog_hallazgos.md:1209` that a future audit could mistake for an unconditional refutation of (A) — it is not. (3) The single most load-bearing finding — the R-dropping in Corolario 8.2 — is fully CONFIRMED by direct side-by-side text comparison and independently corroborated by the memory marker. This is a real, verified defect in the closure argument's own accounting of what remains open, not a citation error by the auditing roles.

## 8. Claim ledger

Every substantive claim, its status, and the argument or artefact that set it. Status is exactly
one of `PROPOSED`, `VERIFIED`, `REFUTED`, `INCONCLUSIVE`. `VERIFIED` requires evidence outside the
language layer; concurring agents never suffice.

| ID | Claim | Status | Evidence | What set the status |
| --- | --- | --- | --- | --- |
| C1 | `Delta_n` es el mismo objeto en `NC-2C`, `NC-2D`, `NC-2E` y `NC-2F(B)`: no hay deriva de definición | VERIFIED | Cuatro ficheros abiertos línea a línea por el verificador de fuentes; fórmula verbatim idéntica | El verificador de fuentes abrió las cuatro definiciones, no la concordancia entre roles |
| C2 | La reducción al proceso empírico iid (Lema 3.1 de `NC-2F(B)`) no es circular respecto de `NC-2C`/`NC-2E` | VERIFIED | `emergencia/P1a_count_volume_lema_kl_d2.md:95-107`; `...selected_interior_mass_d2.md:111-127` | Lectura directa: el Azuma de `NC-2C` no se usa en §§2-7; la uniformidad del mapa de rangos es del modelo congelado |
| C3 | La aritmética publicada sostiene `4.2e4` y el umbral `n>=10^6` es suficiente y monótono, sin rango de re-fallo | VERIFIED | Recómputo independiente del rol aritmético (~1340 puntos, 0 violaciones, peor cociente `0.9035`); oráculos 1–2 del chair | Recómputo independiente que **no** usó el oráculo del chair |
| C4 | La frase de `:255-256` («factor menor que `0.72`») es **literalmente falsa** | VERIFIED | Razón exacta `t_17/t_16 = 0.7270291800`; tres recómputos independientes (procesos empíricos, aritmético, falsador) más oráculos 2–3 del chair | Cálculo exacto, no lectura |
| C5 | El parche `0.72 -> 0.728` propuesto inicialmente por el chair es **inseguro**: con el `t_16` exacto la frase vuelve a ser falsa | VERIFIED | Oráculo 3: `0.016341/(1-0.728) = 0.060077 > 0.06`; el rol aritmético lo señaló antes | El rol aritmético lo detectó; el chair lo confirmó por cálculo |
| C6 | El Corolario 8.2 de `NC-2F(B)` enuncia la obligación residual **sin `R`**, contabilizando de menos lo que falta para `NC2E-O3` | VERIFIED | `...rectangular_discrepancy_l2_d2.md:349-362` frente a `...selected_variance_clt_scale_d2.md:609-618, 663-678` | Comparación textual lado a lado por el auditor de integración, reproducida por falsador y verificador de fuentes |
| C7 | Esa misma omisión ya está commiteada en el marcador de memoria, la puerta de entrada de toda sesión futura | VERIFIED | `memoria_claude/program-status-reentry-marker.md:113-114`, frente a `:102-104` del mismo fichero, que sí lleva `(R+Delta_n)^2` | Lectura directa del fichero commiteado |
| C8 | «Toda la parte incondicional del programa» no está definida en ninguna parte del repositorio | VERIFIED | `grep -rl "parte incondicional"` → cero ficheros; `emergencia/` contiene 30 ficheros `P1a_*` | Grep vacío ejecutado por el falsador |
| C9 | No existe cota superior **incondicional** para `Pr_n(S)`: la hipótesis (A) `Pr(S)>=c>0` está abierta, no refutada | VERIFIED | Búsqueda repo-wide del verificador de fuentes; única cota superior hallada, `docs/backlog_hallazgos.md:1209` (EF3.11), es **condicional** a una hipótesis no probada | Búsqueda exhaustiva independiente |
| C10 | Premisa original del DOSSIER: «`NC-2F(a)` demuestra `Pr(S) -> 0`» | REFUTED | `...selection_mass_sqrt_scaling_d2.md:186` es una cota **inferior**; no hay cota superior incondicional (C9) | Detectado por el auditor de integración, confirmado por el verificador de fuentes; el error era del chair |
| C11 | El Teorema 1.1 cierra el objeto **(B)** tal como `NC-2E` Corolario 8.2 lo define, y `c_1` entra donde debe | VERIFIED | `...selected_variance_clt_scale_d2.md:654-660`; `:391-396`; `:620-627`; aritmética `3.3652e9 <= 3.4e9` | Sustitución verificada término a término |
| C12 | El Corolario 8.1 nunca se etiqueta CONDICIONAL en el cuerpo del documento, y §9 omite los Corolarios 7.2, 8.1 y 8.2 del inventario de lo demostrado | VERIFIED | `grep -ni "condicional"` devuelve sólo `:1`, `:3`, `:358` (todas dentro de «incondicional»); `:366-367` | Grep y lectura del inventario |
| C13 | El recuento `m_k=(2^k+1)^2` del encadenamiento es el correcto | INCONCLUSIVE | Ningún rol lo re-derivó desde la construcción; el margen de `L_k` es `0.0206` en `k=0` | El falsador lo registró explícitamente como ataque no ejecutable |
| C14 | §§2-3 entregan puntos **iid exactos** bajo el condicionamiento a `N=n`, como §§4-6 requieren | INCONCLUSIVE | Cada rol asumió que el otro había cerrado el punto; ninguno lo certificó | Detectado por el falsador como hueco cruzado entre briefs |
| C15 | Las constantes deductivas quedan fuera de la regla `numbers-must-come-from-committed-script` | INCONCLUSIVE | La memoria sólo documenta un fallo con números **empíricos**; la extrapolación es inferencia del rol, no texto de la fuente | El verificador de fuentes rebajó la afirmación |
| C16 | La ola 1 sufre correlación de errores: los cuatro briefs convergen en los dos defectos que el chair había puesto en el DOSSIER | VERIFIED | Los defectos `0.72` y `t_14`/suma aparecen en los oráculos 2–3 del DOSSIER, escritos **antes** que los briefs | Comparación del DOSSIER con los briefs |
| C17 | El refrendo de `NC-2F` es posterior a la ejecución y los terminales se precomprometieron en la misma sesión | VERIFIED | `docs/program_reopening_note_2026-08-18_nc2f_variance_exponent_reduction.md:28-43, 190-191` | La nota lo declara ella misma |
| C18 | Declarar «cerrada de forma definitiva toda la parte incondicional» excede el perímetro que cualquier nota del registro autoriza | VERIFIED | Nota `NC-2F` §9 `:205-209` («No amplía el perímetro de §3»); §5 `:103`; terminal `:399` `NC2E_O3 = OPEN`; `CLAUDE.md:37-39` | Guardián de compromisos, con `doc:line` |
| C19 | Radio de explosión de un error futuro: caerían `NC-2F(B)`, el Corolario 8.1 y `:113` del marcador; **no** caerían `NC-2E` ni `NC-2F(a)` | VERIFIED | `NC-2E` es anterior y su terminal ya publica `NC2E_MISSING_OBJECT_B` como abierto; `NC-2F(a)` depende de `NC-2C` §4.1 y `NC-2E` Thm 7.1 | Trazado de dependencias por el auditor de integración |
| C20 | El repositorio cierra en la práctica mediante reapertura acotada, no mediante congelación: 11 notas de reapertura posteriores al cierre de 2026-07-30 | VERIFIED | `docs/program_closure_note_2026-07-30.md:153`; `ls docs/ \| grep -i reopening` → 11 ficheros | Recuento reproducido por el verificador de fuentes |
| C21 | Ninguna de las correcciones recomendadas existe todavía como diff: en `ea732ff` el `:255-256` sigue diciendo `0.72` | VERIFIED | `git status --porcelain` vacío; lectura del fichero en `HEAD` | El falsador |

## 9. Synthesis

**Dirección recomendada: separar las dos preguntas que el encargo mezclaba.** El Teorema 1.1 es
correcto y su constante sobrevive; la acción irreversible que se propone encima de él no está
autorizada por ningún compromiso del registro y su objeto ni siquiera está definido.

Sobre el **teorema** (`C1`–`C4`, `C11`): los cuatro roles de la ola 1 coinciden en PASA CON
CORRECCIONES, pero —y esto lo señala el falsador con razón (`C16`)— esa coincidencia está
parcialmente inducida por la lista de defectos que el chair había puesto en el expediente antes de
que escribieran. Lo que sostiene el veredicto no es la concordancia sino el recómputo independiente
del rol aritmético (`C3`), que no usó el oráculo del chair, y la verificación línea a línea de las
20 citas (`C1`, `C11`). Defectos que deben corregirse antes de publicar nada encima:

- **Grave textual (`C4`)**: la frase de `:255-256` es falsa. El parche debe usar `r <= 0.7271`
  **y** `t_16 <= 0.01635`, o declarar la cola `< 0.061` (opción robusta: deja la suma en
  `5.174 <= 5.2` sin tocar `5.2`, `15.1`, `17`, `290` ni `4.2e4`). El parche `0.728` es **inseguro**
  (`C5`).
- **Grave de integración (`C6`, `C7`)**: el Corolario 8.2 y la línea `:113` del marcador deben
  restituir `(R+Delta_n)^2`.
- **Moderados (`C12`)**: etiquetar el Corolario 8.1 como CONDICIONAL en su encabezado, declarar su
  dominio `n>=10^{40}`, e incluir los Corolarios 7.2/8.1/8.2 en el inventario del §9.
- **Menores**: «c.s./sin empates»; puntero `lema_kl §1 y §2.1`; frase de transporte; caso `m=1` del
  Lema 5.1; medibilidad de `W`; convenio de logaritmo; `K>=5` en el paso `0.234K^2+0.93K`;
  redondeos a la baja (`t_14`, suma `5.111`, `1.183`); marcar `[UNVERIFIED]` o borrar la aserción
  bibliográfica de `:375`.

Sobre la **acción irreversible** (`C8`, `C18`, `C20`): el guardián de compromisos devuelve **BLOCK**,
y por la regla 4 del protocolo un BLOCK no puede convivir con un veredicto PROCEED. Los motivos son
independientes entre sí y cada uno bastaría: el objeto a congelar no existe como conjunto definido
(`C8`); el perímetro autorizado por la nota `NC-2F` §9 excluye explícitamente ampliaciones (`C18`);
no se fijó nunca un criterio para «cierre definitivo incondicional», luego no hay nada que
satisfacer (`CLAUDE.md:37-39`); y la práctica revelada del repositorio son once reaperturas acotadas
tras un cierre declarado (`C20`).

**Desacuerdos entre roles, con quién lleva la evidencia:**

1. *«No hay ningún defecto matemático» (combinatorista) frente a «hay un hueco no enunciado»
   (falsador).* Lleva la evidencia el falsador en la forma, no en el fondo: el propio brief
   combinatorista admite que la medibilidad de `Delta_n` respecto de `Pi_n` **no está escrita** en el
   documento, y llamar a eso «corrección textual» es una decisión de clasificación, no un hecho. El
   contenido matemático sí es correcto; la etiqueta «puramente textual» es la que no se sostiene.
2. *Gravedad de la omisión de `R`.* El auditor de integración lo trata como error de contabilidad;
   el verificador de fuentes matiza que `NC-2E:684-685` dice que (8.1) es **suficiente, no
   necesaria**, y que no se probó recíproco. Lleva la evidencia el verificador en la formulación
   exacta: el Corolario 8.2 no afirma una desigualdad falsa, **omite** un término al describir lo que
   queda abierto. El efecto práctico —perseguir una obligación más débil que la real— es el mismo, y
   ambos coinciden en que debe corregirse.
3. *Regla `numbers-must-come-from-committed-script` (`C15`).* El rol aritmético concluye que no
   aplica por precedente; el verificador de fuentes rebaja eso a inferencia propia del rol, no
   sostenida por el texto de la memoria. Queda INCONCLUSIVE: la regla no se ha violado según el
   precedente uniforme de quince notas, pero nadie ha fijado por escrito que las constantes
   deductivas estén exentas.
4. *Independencia de la verificación.* Ningún rol discute el hecho (`C17`); discrepan en su efecto.
   El guardián lo cuenta como movimiento prohibido para una decisión de esta consecuencia; los roles
   técnicos lo tratan como circunstancia atenuada por el recómputo independiente. Lleva la evidencia
   el guardián para la **decisión**, y los roles técnicos para el **teorema**: son dos objetos
   distintos, y ésa es exactamente la separación que recomienda este brief.

**Alternativas ordenadas:**

1. *(Recomendada)* Aplicar el parche de correcciones, verificarlo con un recómputo que no proceda
   del autor, y cerrar la parte incondicional **con cláusula de reapertura acotada** — el mecanismo
   que el repositorio ya usa once veces. Entrega el 100% del beneficio (dejar de trabajar en ello)
   con 0% del coste (perder la capacidad de corregir).
2. Aplicar el parche y no declarar ningún cierre: seguir a la parte selectiva dejando la
   incondicional simplemente inactiva. Más barato, menos explícito.
3. Declarar el cierre definitivo tal como se pidió. **Bloqueada** por el guardián; requeriría antes
   enumerar por escrito qué compone «la parte incondicional» y fijar un criterio de cierre, es
   decir, exactamente el trabajo que la opción 1 hace de forma reversible.

## 10. Next-step spec

**Pasos reversibles (ejecutables ahora si el usuario lo pide):**

1. Parche textual de `emergencia/P1a_count_volume_rectangular_discrepancy_l2_d2.md`:
   - `:255-256` → cola `< 0.061` (o `r <= 0.7271` **y** `t_16 <= 0.01635`); `:253` `0.030` → `0.031`;
     suma `5.111` → `5.114`. **Regla vinculante precomprometida:** ninguna de estas ediciones puede
     cambiar `5.2`, `15.1`, `17`, `290` ni `4.2e4`; si alguna lo hiciera, el parche se detiene y se
     reconvoca.
   - Corolario 8.2 → restituir `sum_{pi in S_n}(R+Delta_n)^2 <= (C/n)|S_n|`.
   - Corolario 8.1 → encabezado «(CONDICIONAL)», dominio `n>=10^{40}`, referencia cruzada a
     `NC-2F(a):186`, e inclusión en el inventario del §9 junto con 7.2 y 8.2.
   - Frases de rigor: «c.s., sin empates»; puntero `lema_kl §1 y §2.1`; transporte de la cota puntual
     a la ley uniforme; caso `m=1` del Lema 5.1; medibilidad de `W`; convenio de logaritmo natural;
     `K>=5` en `:260-261`; `[UNVERIFIED]` o borrado en `:375`.
2. Corrección de `memoria_claude/program-status-reentry-marker.md:113` para restituir
   `(R+Delta_n)^2`, y unificación de los dos nombres del token de obligación residual.
3. Registro en el brief de la cota superior **condicional** de `docs/backlog_hallazgos.md:1209`
   (EF3.11), para que una auditoría futura no la confunda con una refutación de (A).
4. **Test mínimo de falsación del falsador, ya ejecutado y reproducible por cualquiera:**
   recómputo de `t_k = sqrt((k+1.5)2^{-k})` para `k=16,17` (razón `0.7270291800`); diff lado a lado
   de `NC-2E:607-618` contra `NC-2F(B):349-362` (el término `R` desaparece);
   `grep -rln "parte incondicional" .` (cero ficheros). Los tres son de sólo lectura y no modifican
   el repositorio.

**Pasos que comprometen (sólo con autorización explícita del usuario):**

5. Commit del parche. Debe ir acompañado de una nota que declare que las correcciones proceden de
   una auditoría adversarial y que enumere los defectos corregidos, con reporte simétrico: los
   hallazgos negativos (`C4`, `C6`, `C7`, `C16`) con la misma prominencia que la confirmación del
   teorema.
6. Verificación del parche por un recómputo que **no** proceda del autor del documento —condición
   explícita del rol aritmético— antes de considerar cerrada la corrección.
7. Cualquier declaración de cierre. Si el PI la quiere, requiere previamente: (a) enumerar por
   escrito qué ficheros y qué resultados componen «la parte incondicional»; (b) fijar el criterio de
   cierre **antes** de evaluarlo; (c) redactarlo como cierre con cláusula de reapertura acotada, no
   como congelación. Nada de esto puede hacerse dentro del perímetro de `NC-2F` §3: exige nota nueva
   firmada.

## 11. Verdict

FORO_VERDICT=REVISE_AND_RECONVENE

## 12. User sign-off

_(left blank for the user — decision, date, and any overriding notes)_
