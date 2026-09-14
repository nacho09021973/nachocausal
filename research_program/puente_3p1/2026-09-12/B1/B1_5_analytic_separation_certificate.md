# B1.5 — Certificado analítico de separación para el par congelado

> **STATUS: `FROZEN_PAIR / ANALYTIC_INEQUALITY_CHAIN / NO_SEARCH / NO_SEEDS / NO_MONTE_CARLO`.**
> El par es exactamente el de B1.3 y no puede sustituirse. No se autoriza simulación,
> preregistro ni cambio de blanco. `PHASE_0_R1` intacto.
> **ADVANCES:** `L3`, sólo para el par congelado.

**Fecha:** 2026-09-14 · **Verificadores:** `verify_b1_5_analytic_separation.py` →
`verification_b1_5_analytic_separation.json`; `verify_b1_5_refinement_audit.py` →
`verification_b1_5_refinement_audit.json`.

---

## 1. Qué establece y qué no

B1.4 dejó las cotas angulares rigurosas punto a punto pero la integración global dependiendo
de la estabilidad de Gauss–Legendre, y por tanto `B1_FORMAL_CERTIFICATE = NOT_ESTABLISHED`.
B1.5 sustituye esa integración por una cadena de desigualdades.

La pregunta no es calcular `rho`. Es construir dos números con

```text
rho(lambda0) <= U0 < L1 <= rho(lambda1).
```

Resultado:

```text
U0 = 0.019908535921312993          (cota superior burda para lambda0)
L1 = 0.022826761203854212          (cota inferior burda para lambda1)
gap = 0.0029182252825412196        margen relativo = 14.66 %

TV(P_{lambda0,2}, P_{lambda1,2}) = |rho(lambda0) - rho(lambda1)| >= 0.00291822
```

```text
B1_FORMAL_CERTIFICATE = ESTABLISHED
B1_ARITHMETIC_STATUS  = DIRECTED_ROUNDING_ENCLOSURE
B1 = FORMAL_3P1_ORDER_NONDEGENERACY_ON_FROZEN_PAIR
P_{lambda0,2} != P_{lambda1,2}
```

Ninguna de las dos probabilidades queda calculada. Las cotas son deliberadamente burdas:
su distancia a las bandas numéricas de B1.4 es el precio de no usar cuadratura certificada.

Lo que **no** establece, y conviene no confundir:

- no es identificabilidad de `phi`: un par testigo da no-degeneración, no reconstrucción;
- no dice nada sobre puntos arbitrariamente próximos de la curva de B2 (`B2` sigue abierto);
- no establece la implicación general de `L3` (`phi(lambda) != phi(lambda') ⟹ TV>0`);
- no es un enunciado sobre localización de horizonte: el parámetro del bloque es `lambda`.

## 2. La reducción que hace el problema tratable

Con `p(a) = (1-cos min(a,pi))/2` y la medida normalizada del patch,

```text
rho(lambda) = (2/Z^2) int int_{Ux<=Uy, Vx<=Vy} G(Ux Vx) G(Uy Vy) p(Delta_max(x,y)) dx dy .
```

La dificultad es que el integrando vive en **cuatro** dimensiones. La clave del certificado es
que la integral de pares **nunca se discretiza**: se colapsa exactamente por Fubini, y sólo
quedan envolventes unidimensionales. Dos identidades hacen el trabajo:

```text
int_{v0}^{v1} int_{Vy>=Vx} int_{Vx}^{Vy} h(V) dV dVy dVx = int_{v0}^{v1} h(V)(V-v0)(v1-V) dV
int int_{Vx<=Vy} (Vy-Vx) dVx dVy = (v1-v0)^3/6 ,  int int (Vy-Vx)^2 = (v1-v0)^4/12
```

y en `U`, `int_{-uout}^{Uy}(Uy-Ux) dUx = (Uy+uout)^2/2`.

Además `G` y `q` se encierran por envolventes que dependen de **una sola** variable:
como `w = UV` no cambia de signo a `U` fijo y `G` es unimodal en `w` con máximo en `w=0`,

```text
G(U v1) <= G(U V) <= G(U v0)          para todo V en [v0,v1],
```

y lo mismo por celda de `V`, lo que estrecha la envolvente a coste `O(1/L)` sin salir de 1D.

## 3. Cadena superior (se aplica a `lambda0`)

Para cualquier curva causal futura de `x` a `y`, la reparametrización monótona de B1.2 §2 da
`U(V) <= Uy`, luego `q(U(V)V) <= q(Uy V)` (`q` creciente en `w`, `V>0`), y Cauchy–Schwarz:

```text
Delta_max(x,y) <= a(x,y) := sqrt( dU * int_{Vx}^{Vy} q(Uy V)^2 dV ) .
```

Con `p(a) <= a^2/4` (válida para todo `a>=0`: para `a<=pi` es `1-cos a <= a^2/2`; para `a>pi`,
`p=1 <= a^2/4`), `G <= Gcheck(U)=G(U v0)` y las identidades de §2, todo colapsa a

```text
rho(lambda) <= (1/(2 Z_lo^2)) int_{-uout}^{uin} Gcheck(U) A1(U) C1(U) dU ,
A1(U) = e^{-1}(U+uout)^2/2 ,   C1(U) = int_{v0}^{v1} q(UV)^2 (V-v0)(v1-V) dV .
```

`A1` y `C1` son crecientes en `U` y `Gcheck` es unimodal con pico en `U=0`, que se fuerza a ser
punto de la malla: cada celda es monótona y sus extremos la acotan. El resultado es una suma de
Riemann superior sobre celdas 1D, no una cuadratura.

## 4. Cadena inferior (se aplica a `lambda1`)

Aquí la cota debe venir de una trayectoria causal **explícita**, y el problema es que la recta
de `x` a `y` depende de `Uy`, lo que rompe Fubini. La pieza que lo resuelve:

> **Anclaje.** Si `c <= Uy`, el segmento recto de `(Ux,Vx)` a `(c,Vy)` queda puntualmente por
> debajo del segmento a `(Uy,Vy)`. Como `q` crece en `w` y `V>0`, su perfil de `q` acota por
> debajo al de la recta verdadera, **sin** tocar la pendiente `sqrt(dU/dV)`.

Con `tau = (V-Vx)/(Vy-Vx)` el perfil anclado es `Ux + (c-Ux)tau`, **independiente de `Vx,Vy`**.
Acotando `q` por su peor `V` admisible en la celda,

```text
Delta_max(x,y) >= sqrt(dU*dV) * T ,      T = media de qtilde sobre [Ux, c_j] ,
qtilde_{l,m}(u) = q(u t_{m+1}) si u<0,   q(u t_l) si u>=0 .
```

Con `p(b) >= b^2/4 - b^4/48` (válida para todo `b>=0`: para `b<=pi` por la serie alternada; para
`b>pi` el polinomio no pasa de `3/4 < 1 = p`), y sumando sobre los bloques `(j,l,m)` —anclas de
`Uy`, celda de `Vx`, celda de `Vy`— cada bloque es un producto de integrales 1D por los momentos
cerrados de §2. Los pares con `Ux > c_j` se descartan: bajan la cota, no la invalidan.

## 5. Capa escalar: `s` sin Lambert W

`s(w)` se define por `f(s) = (1-s)e^s = w`, con `f'(s) = -s e^s < 0` en `s>0`. Por tanto

```text
s >= a  <=>  f(a) >= w ,        s <= b  <=>  f(b) <= w ,
```

y cada enclosure se certifica con **dos desigualdades escalares**, evaluadas en aritmética de
intervalos escalar (`mpmath.iv`, dps 25). No se llama a ninguna rutina de Lambert W en ningún
punto del certificado; la bisección en coma flotante sólo proporciona el punto de partida, que
después se verifica. `G` y `q` heredan el bracket por monotonía (`q` decrece en `s`; `G` es
unimodal con máximo `1/e`).

## 5bis. Aritmética: redondeo dirigido de extremo a extremo

La capa escalar por sí sola no basta. En cuanto los extremos certificados se convierten a
`float`, toda operación posterior —sumas de Riemann, `cumsum`, productos, momentos,
normalización— puede redondear hacia el lado equivocado. Que el gap sea enorme frente al
epsilon de máquina **no demuestra** que el error de redondeo esté acotado; sólo lo hace
implausible. La versión certificada mantiene por tanto la dirección hacia afuera en cada paso:

| objeto | tratamiento |
|---|---|
| operaciones binarias (`*`, `/`, `-`) | cada resultado IEEE-754 está correctamente redondeado (error `<= 1/2 ulp`), y se desplaza **un ulp hacia afuera** |
| sumas | `math.fsum`, exactamente redondeada con cualquier signo y longitud, más un ulp hacia afuera |
| sumas acumuladas (`cumsum`) | `np.cumsum` más un término de error explícito `gamma_n` de Higham, `gamma_n = n u /(1-n u)`, aplicado a ambos extremos de la diferencia de prefijos |
| momentos de la partición (`V2`, `V4`, pesos de `C1`) | racionales **exactos** (`fractions.Fraction`) sobre los nodos, redondeados hacia afuera sólo al convertir |
| fronteras de la partición | son valores binary64, es decir racionales exactos; celdas consecutivas comparten extremo, de modo que su unión es exactamente el dominio, y las anchuras se redondean hacia afuera |
| productos de nodos (`U*t`) | el producto exacto no es el `float` calculado: la función se encierra sobre todo `[dn(U*t), up(U*t)]`, nunca en el punto redondeado |
| `1/e` | cota superior rigurosa tomada de `mpmath.iv`, no `math.exp(-1)` |
| `M1`, `M2` | reescritos sin cancelación, `(c1-u)^2-(c0-u)^2 = (c1-c0)((c1-u)+(c0-u))`, con todos los factores `>= 0` |
| divisiones finales | `U0` divide por `Z_lo` redondeado hacia abajo; `L1` por `Z_hi` hacia arriba |

No queda ninguna constante de holgura global: la comparación certificada es literalmente
`U0_hi < L1_lo`. El coste de esta capa resultó ser nulo en la práctica —el error de redondeo
real es de orden `1e-16` relativo— pero eso es ahora una **consecuencia medida**, no una
hipótesis.

## 6. Guardarraíles y su sensibilidad medida

Un guardarraíl que no puede fallar es decoración, así que se mide lo que detecta.

**Batería de mutación** (`pointwise_inequality_guards`). Sobre una retícula fija de 441 pares
ordenados por `lambda` se comprueban las dos desigualdades que sostienen todo:
`b_anchor <= b_line <= a`. Luego se rompe deliberadamente un paso:

| mutación | `max(b_anchor - b_line)` en `lambda1` | detectada |
|---|---|---|
| ninguna (cadena correcta) | `-0.003485` | — (no debe violar) |
| ancla tres bins por encima de `c_j` | `+0.073826` | sí |
| ancla en `u_in`, ignorando `Uy` | `+0.156831` | sí |
| `qtilde` con el extremo de `V` favorable | `+0.144791` | sí |

El margen de la cadena correcta (`-0.0035`) es del mismo orden que las violaciones detectadas:
el guardarraíl está efectivamente ajustado, no holgado.

**Auditoría de refinamiento** (`verify_b1_5_refinement_audit.py`). Toda elección de `(K,L,celdas)`
da cotas **válidas**; refinar sólo las aprieta. Lo que desacreditaría la cadena sería una
*reversión*: separar a una resolución y dejar de separar a otra más fina.

```text
K=6  L=6   U0=0.020159  L1=0.019940   no separa
K=8  L=8   U0=0.020039  L1=0.021158   SEPARA
K=12 L=12  U0=0.019968  L1=0.022259   SEPARA
K=16 L=16  U0=0.019909  L1=0.022827   SEPARA   <- ajuste reportado
K=20 L=20  U0=0.019883  L1=0.023148   SEPARA

U0 decreciente, L1 creciente, sin reversión.
TERMINAL = B1.5_REFINEMENT_MONOTONE_NO_REVERSAL
```

Que `K=L=6` no separe no es una contradicción: esa cota es válida y simplemente demasiado
débil. La separación exige una partición al menos tan fina como `K=L=8`.

**Consistencia con B1.4.** Los intervalos rigurosos contienen estrictamente las bandas
numéricas: `[0.01151, 0.01991] ⊃ [0.01276, 0.01879]` para `lambda0` y
`[0.02283, 0.05044] ⊃ [0.02793, 0.04384]` para `lambda1`. Si el certificado y la cuadratura de
B1.4 se contradijeran, uno de los dos estaría mal; no se contradicen.

## 7. De qué depende el certificado

Es un certificado **condicional**, y sus hipótesis son explícitas:

- **H1.** De B1.2 §2 se usan **sólo dos consecuencias**, y el certificado no se apoya en la
  equivalencia variacional completa `Delta_max = min(pi, sup_U L[U])`:
  **(H1a)** el desplazamiento angular de toda curva causal futura de `x` a `y` está acotado por
  la cota de Cauchy–Schwarz de §3; **(H1b)** la recta explícita de `x` a `y` es una curva causal
  admisible, luego su presupuesto acota `Delta_max` por debajo. Ambas quedan establecidas en
  B1.2 (marcado `DERIVED`); aquí no se vuelven a derivar.
- **H2.** La identidad a `n=2`: `TV(P_{lambda,2}, P_{lambda',2}) = |rho(lambda)-rho(lambda')|`
  (`B1_par_testigo_lambda.md` §5), que depende de que a `n=2` sólo haya dos clases de poset.
- **H3.** La carta, el patch y la medida congelados (B0, `op11` §2).
- **H4.** Modelo aritmético: aritmética IEEE-754 binary64 con las operaciones básicas
  correctamente redondeadas —la garantía del estándar— y `mpmath.iv` para la capa escalar. Con
  eso, §5bis propaga la dirección hacia afuera en cada paso y la conclusión ya **no** descansa
  en que un error de redondeo sea pequeño frente al gap. H4 queda reducida al modelo aritmético
  de la máquina; no incluye ninguna holgura asumida.

## 8. Cumplimiento de la regla de parada de B1.5

La regla era declarar `TOO_COSTLY` si hacía falta aritmética intervalar multidimensional
general, cuadratura certificada en dimensión alta, infraestructura formal para Lambert W o una
partición enorme. Lo realmente usado:

```text
integral de pares 4D          : nunca discretizada (colapsada exacta por Fubini)
dimensión de toda cuadratura  : 1
aritmética intervalar         : escalar, sólo para encerrar s, G, q en puntos
redondeo                      : dirigido hacia afuera en todo paso posterior (§5bis)
Lambert W                     : no se usa
partición                     : K=16 anclas, L=16 celdas, <=480 celdas 1D
enclosures escalares certificados : 149424 (s), 149424 (q), 29165 (G)
tiempo de ejecución           : ~18 s las cotas, ~43 s con los guardarraíles
```

El recuento de enclosures es alto porque `C1(U)` se acota en 480 puntos de `U` con 160 celdas
de `V` cada uno; pero eso es un producto de mallas **unidimensionales** para acotar una integral
1D, no una malla en dimensión 4. El criterio que decide la regla de parada —no discretizar la
integral de pares, no usar aritmética intervalar multidimensional— se cumple; el coste bruto es
de segundos.

## 9. Ruta muerta documentada, para no repetirla

La ruta sugerida de acotar `lambda1` por debajo con un **subdominio rectangular** de pares
`A x B` está muerta por volumen, no por el presupuesto angular. Como `p <= 1`, cualquier región
producto contribuye a lo sumo `2 Gmax^2 |A||B| / Z^2`, luego alcanzar `L1 = 0.02283` exige

```text
|A||B| >= L1 * Z1^2 / (2 Gmax^2) = 0.02283 * 0.40017 / 0.27067 = 0.0337 ,
```

es decir el **4.46 %** del 4-volumen de pares ordenados (`area^2/4 = 0.7569`), y eso suponiendo
`p == 1` en todo `A x B`. Las elecciones naturales (dos rectángulos bien separados en `U` y `V`,
que es lo que da presupuesto angular garantizado) rondan el 1 %. Por eso la cota inferior de
este certificado usa **todo** el dominio y ancla el perfil de `q`, en vez de recortar el dominio.

## 10. Siguiente paso, y lo que no lo es

Lo que este resultado habilita es una pregunta, no un programa: si la no-degeneración a `n=2`
sobrevive cuando los dos `lambda` se acercan (`B2`), que es donde la derivada y las
cancelaciones reaparecen y donde B1.5 no dice nada. Este documento no autoriza abrir `B2`,
ni `B3`, ni `n=3`, ni otro par testigo, ni ejecución alguna.

## 11. Historial de auditoría

El objeto se congeló y se pusheó **antes** de auditarlo, para que el control fuera independiente
de quien escribió la prueba.

```text
commit auditado : 5d029c7edbc43c788c055f0f53d7fbc003b3047c
base            : origin/emergencia/p1a-canal-sigma-m (6f866a2)
veredicto       : AUDIT_PASS_CONDITIONAL_H4
```

La auditoría no halló fallo en la normalización, el factor `2/Z^2`, el anclaje, el colapso por
Fubini, las desigualdades trigonométricas ni la dirección de las cotas, y confirmó que el código
**no** sustituye la pendiente por `sqrt((c_j-U_x)/dV)`: conserva `sqrt(dU dV)` y sólo rebaja el
perfil de `q`. El defecto señalado fue exactamente uno, y era aritmético: la cadena abandonaba
la aritmética intervalar al convertir a `float`, y sólo aplicaba una holgura global `1e-9` al
final, de modo que

```text
"el gap es enorme comparado con 1e-9"   NO demuestra   |error float| < 1e-9 * |resultado| .
```

Clasificación entonces: `ROBUST_FLOAT_CERTIFICATE`, no enclosure con redondeo exterior. El
parche de §5bis propaga la dirección hacia afuera desde la capa escalar hasta la comparación
final y elimina la constante de holgura; la matemática de §3–§4 no se tocó. Los valores se
movieron sólo en el dígito 11, que es justo lo que la holgura `1e-9` había estado inflando:

```text
antes (holgura 1e-9) : U0 = 0.019908535941221436   L1 = 0.022826761181048354
ahora (dirigido)     : U0 = 0.019908535921312993   L1 = 0.022826761203854212
```

La recomendación de reformular H1 en términos de las dos consecuencias usadas, sin cargar B1.5
con la equivalencia variacional completa, está aplicada en §7.

## 12. Fuentes

- Criterio causal angular y cotas LB/UB: `B1_2_angular_causal_reach.md` §2, §3
- Par congelado e identidad a `n=2`: `B1_3_frozen_pair_and_rho.md` §2; `B1_par_testigo_lambda.md` §5
- Bandas numéricas que este certificado sustituye: `B1_4_exact_or_certified_rho.md` §3
- Carta, patch, medida y gauge de dilatación: `docs/puente_schwarzschild_3p1_2026-09-12.md` §3, §5
- Requisitos de claim y dirección de garantía: `docs/claim_grammar.md` §1
