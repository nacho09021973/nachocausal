# `UNIFORM_IN_N_REGULARITY` para la caja EF fija — cociente por lado del horizonte

```text
ESTADO: PROVED — READ_BY_PI 2026-10-16; PART_A_REVIEWED_DEEPSEEK; PART_B_REVIEWED_ASTRA (not independent)
FECHA: 2026-10-16
ENTRADA: research_program/work_packages/wp6_domain_bridge_fixed_ef_box.md §13–§19
NATURALEZA: prueba analítica; comprobación numérica en dev/ (sin semillas del track sellado)
UNIFORM_IN_N_FISHER_BOUND = PROVED_LINEAR            (I_n^Pi <= n J(tau))
UNIFORM_SQRT_SCORE_MODULUS = PROVED_LINEAR_WINDOW     (Omega_{n,K}(eta) <= C_K n eta)
UNIFORM_QMD_WINDOW = delta_n = o(1/n)
UNIFORM_QMD_AT_LAN_SCALE = NOT_IMPLIED (ver §6)
EF_BOX_ORDER_ONLY_TWO_POINT_FLOOR = PROVED  (orden 1/sqrt(n Jbar), Corolario C §7)
EF_BOX_ORDER_CHANNEL_ATTAINS_1_OVER_N = REFUTED (Corolario C)
EF_BOX_MINIMAX_RATE = N_POW_MINUS_HALF_PROVED (Teorema H §9; Lema G de monotonía)
REVIEW_OF_SECTIONS_8_9 = NONE_YET (escritas por Claude; sin revisión de otra familia ni lectura humana)
POISSON_MIXTURE_REGULARITY = PROVED (Corolario D §8)
FISHER_LOWER_BOUND = PROVED_LINEAR_WHERE_P_PRIME_NONZERO (Prop. E §9)
FISHER_TO_LOCALISATION_BRIDGE = NOT_OPENED
NO_PRIORITY_CLAIM
NEXT_RUN_AUTHORIZED = NO
```

## 0. Procedencia

La idea del §2 la propusieron por separado claude-opus-5-5 y gpt-6-astra en una
prueba de la herramienta CREATE (`~/herramientas`, commit `fbc5b3c`;
`~/herramientas/CREATE/runs/2026-10-16-fisher-uniforme-n/`). Se les dio como contexto
la lista de vías ya exploradas; esta no estaba en ella. Las pruebas de §3–§5 las
escribió Claude (Opus 5.5). Revisión ciega de la parte (a) por deepseek-v4-pro, con
veredicto "correcta con salvedades menores":
`revisiones/2026-10-16-cociente-horizonte-ciego/` (commit `278d536`). El PI leyó
§2–§5 el 2026-10-16 y los da por buenos. Revisión de la parte (b) (§5) por gpt-6-astra, con veredicto "correcta con
salvedades enumeradas" en el §6: `revisiones/2026-10-16-modulo-omega-astra/`. No es
independiente, porque Astra propuso la cota.

## 1. Modelo y notación

Se conserva el §1 de `wp6_domain_bridge_fixed_ef_box.md`: \(B=[0,T]\times[r_a,r_b]\),
\(L=r_b-r_a\), \(n\) puntos iid uniformes \((V_i,R_i)\in B\), y
\(K\Subset(r_a,r_b)\) un intervalo compacto de valores de \(\tau=2M\). Se usa

\[
u_\tau(v,r)=-e^{-v/(2\tau)}W_\tau(r),\qquad W_\tau(r)=e^{r/\tau}(r/\tau-1).
\]

\(\Pi_n\) sigue la convención de wp6 §6: se ordenan los puntos por \(u\) y
\(\Pi_n(i)=j\) si el punto de rango \(i\) en \(u\) tiene rango \(j\) en \(v\). La
convención inversa da \(\Pi_n^{-1}\). Como la inversión es una biyección fija de
\(\mathfrak S_n\), las probabilidades se permutan y el Fisher no cambia.
\(I_n^\Pi(\tau)=\sum_\sigma\pi_\sigma'^2/\pi_\sigma\) y \(s_n=(\sqrt{\pi_\sigma})_\sigma\).

## 2. Representación por un canal independiente de \(\tau\)

Sean \(\varepsilon=+1\) y \(b=r_b\) si \(r>\tau\) (exterior), y \(\varepsilon=-1\) y
\(b=r_a\) si \(r<\tau\) (interior). Sean además \(t=|r-\tau|\) y \(t_b=|b-\tau|\).
Se define

\[
D=2\tau\log\frac{|W_\tau(b)|}{|W_\tau(r)|}=2\tau\log\frac{t_b}{t}+2\varepsilon(t_b-t)\ \ge 0.
\tag{2.1}
\]

**Lema 2.1.** (i) \(u<0\) si y solo si \(r>\tau\). (ii) Dentro de cada lado,
\(\log|u|=\log|W_\tau(b)|-(D+V)/(2\tau)\). Por tanto, en el exterior
\(u<u'\iff D+V<D'+V'\), y en el interior \(u<u'\iff D+V>D'+V'\).

*Prueba.* \(W_\tau(r)\) tiene el signo de \(r-\tau\); (ii) se obtiene tomando
logaritmos. \(\square\)

Por tanto existe un mapa \(\varphi\) **independiente de \(\tau\)** con
\(\Pi_n=\varphi((\varepsilon_i,D_i,V_i)_{i\le n})\): primero los exteriores ordenados
por \(D+V\) creciente, después los interiores ordenados por \(D+V\) decreciente, y
para cada uno se toma su rango en \(V\).

**Lema 2.2 (ley).** \(V\) es uniforme en \([0,T]\) e independiente de
\((\varepsilon,D)\). La densidad de \((\varepsilon,D)\) en
\(\{\pm1\}\times[0,\infty)\), que es un soporte fijo, es

\[
f_\tau(\varepsilon,d)=\frac{t}{2L(\tau+\varepsilon t)},\qquad
G(t,\tau,d):=\log t+\frac{\varepsilon t}{\tau}-\log t_b-\frac{\varepsilon t_b}{\tau}+\frac{d}{2\tau}=0.
\tag{2.2}
\]

*Prueba.* \(|dD/dr|=2r/|r-\tau|\) y \(R\) tiene densidad \(1/L\). Segunda vía
(revisor): \(P(\varepsilon,D>d)=t_d/L\); derivando \(G=0\) en \(d\) se obtiene la
misma densidad, que integra a \(t_b/L\) en cada lado. \(\square\)

**Observación (sobre wp6 §5).** El cambio de variables \((v,r)\mapsto(\varepsilon,D,V)\)
depende de \(\tau\), pero \(\varphi\) no. Esto refuta la lectura fuerte de la frase
de wp6 §5: "un mapa dependiente de τ puede fijar el soporte, pero entonces el canal
de orden también depende de τ". El teorema del §1–§5 de wp6 (no-QMD de la ley
puntual en \((u,v)\) y ausencia de un isomorfismo común) no queda afectado:
\((\varepsilon,D,V)\) no es función de \((u,v)\) por ningún mapa independiente de \(\tau\).

## 3. Cotas uniformes del modelo de un punto

Como \(\partial_tG=1/t+\varepsilon/\tau>0\) (en el interior \(t<\tau-r_a<\tau\)), el
teorema de la función implícita da \(t=t_\tau(d)\) de clase \(C^\infty\) en
\(\tau\). Además:

- **Cola.** Como \(\varepsilon(t_b-t)\ge0\), se tiene \(D\ge2\tau\log(t_b/t)\), luego
  \(t\le Le^{-d/(2\tau_{\max})}\). Con \(\tau+\varepsilon t=r\ge r_a\), resulta
  \(f_\tau\le Ce^{-d/(2\tau_{\max})}\) uniformemente en \(K\).
- **Derivadas.** \(\partial_\tau t=-\partial_\tau G/\partial_tG\), con
  \(\partial_\tau G=O(1+d)\) y \(\partial_tG\ge1/t\cdot c_K\). Por tanto
  \(\partial_\tau t/t=O(1+d)\). Derivando otra vez (con \(\partial_t^2G=-1/t^2\) y
  \(\partial_\tau^2G=O(1+d)\)) se obtiene \(\partial_\tau^2t/t=O((1+d)^2)\).
- En consecuencia \(s:=\partial_\tau\log f_\tau=O(1+d)\) y
  \(b:=\partial_\tau^2\log f_\tau=O((1+d)^2)\), uniformemente en \(K\).

Así, \(J(\tau)=E_\tau s^2\), \(m_4(\tau)=E_\tau s^4\) y \(E_\tau b^2\) son finitos,
continuos y uniformemente acotados en \(K\). Se cumplen \(E s=0\) y \(Eb=-J\). La
dominación \(|\partial_\tau^k f_\tau|\le C(1+d)^{2}e^{-d/(2\tau_{\max})}\), para
\(k\le2\) y uniforme en \(K\), permite derivar dos veces bajo la integral.

## 4. Teorema A: cota lineal de Fisher

**Teorema A.** Para todo \(n\ge1\) y todo \(\tau\in K\),
\(I_n^{[P]}(\tau)\le I_n^\Pi(\tau)\le nJ(\tau)\).

*Prueba.* Sea \(X=(\varepsilon_i,D_i,V_i)_{i\le n}\) y \(A_n=\sum_is(\varepsilon_i,D_i)\).
Por §3, \(\pi_\sigma'=E[A_n1\{\varphi(X)=\sigma\}]\). Por Cauchy–Schwarz,
\(\pi_\sigma'^2/\pi_\sigma\le E[A_n^21\{\varphi(X)=\sigma\}]\). Sumando en \(\sigma\)
queda \(I_n^\Pi\le E A_n^2=nJ\). La primera desigualdad es wp6 (15.3). \(\square\)

Este resultado sustituye, para la escala de Fisher, la cadena condicional
§16–§19 de wp6 y su cota factorial (16.1). No hace falta ni la cola de slices
delgados ni el falsificador de celdas raras.

## 5. Teorema B: módulo de la raíz-score

**Teorema B.** Sea \(c(\tau)^2=\tfrac98(m_4+3J^2)+E b^2\). Para todo \(n\ge1\),
\(\sup_{\tau\in K}\|\ddot s_n(\tau)\|_2\le n\sup_Kc\). En consecuencia,

\[
\Omega_{n,K}(\eta)\le C_K\,n\,\eta,\qquad C_K=\sup_Kc,
\]

y \(\Omega_{n,K}(|\delta_n|)\to0\) para toda ventana con \(n\delta_n\to0\). Por
(15.11) de wp6, el resto QMD es uniforme a lo largo de esas ventanas.

*Prueba.* Sea \(B_n=\sum_ib(\varepsilon_i,D_i)\). Por §3,
\(\pi_\sigma''=E[(A_n^2+B_n)1_\sigma]\), y \(\pi_\sigma>0\) (soporte total, wp6 §6). Se
tiene \(\ddot s_\sigma=\pi_\sigma''/(2\sqrt{\pi_\sigma})-\pi_\sigma'^2/(4\pi_\sigma^{3/2})\),
luego

\[
\|\ddot s_n\|^2\le\tfrac12\sum_\sigma\frac{\pi_\sigma''^2}{\pi_\sigma}
+\tfrac18\sum_\sigma\frac{\pi_\sigma'^4}{\pi_\sigma^3}.
\]

Por Cauchy–Schwarz, \(\pi_\sigma''^2/\pi_\sigma\le E[(A_n^2+B_n)^21_\sigma]\) y
\(\pi_\sigma'^4/\pi_\sigma^3\le(E[A_n^21_\sigma])^2/\pi_\sigma\le E[A_n^41_\sigma]\).
Sumando,
\(\|\ddot s_n\|^2\le\tfrac98E A_n^4+E B_n^2\). Para sumas iid,
\(EA_n^4=nm_4+3n(n-1)J^2\le n^2(m_4+3J^2)\) y
\(EB_n^2=n\operatorname{Var}b+n^2J^2\le n^2Eb^2\). Para \(\tau,\tau+h\in K\),
\(\|\dot s_n(\tau+h)-\dot s_n(\tau)\|\le|h|\sup_K\|\ddot s_n\|\). \(\square\)

## 6. Techo: la escala LAN

En el experimento gaussiano producto \(N(\tau,1)^{\otimes n}\) (cálculo de la ruta 4
de Opus, rehecho por Astra en la revisión de §5),
\(\|\ddot\psi\|^2=3n^2/16\) y
\(\|\dot\psi_{\tau+h}-\dot\psi_\tau\|=(\sqrt3/4)\,n|h|\,[1+O(nh^2)]\) **solo en el
régimen** \(\sqrt n|h|\to0\), porque el módulo está acotado por \(\sqrt n\). Por tanto:

- La cota del Teorema B no da QMD uniforme en la escala \(\delta_n=h/\sqrt n\): el resto
  \((\delta^2/2)\sup\|\ddot s_n\|\) es \(O(h^2)\), no \(o(1)\). Esto es una **limitación de
  esta cota**, no una imposibilidad. No excluye LAN para \(\Pi_n\) por otro argumento.
- La optimalidad de la escala \(n\eta\) para \(\Pi_n\) **no está demostrada**. Para
  cualquier canal, \(\langle s_n,\ddot s_n\rangle=-I_n^\Pi/4\), luego
  \(\|\ddot s_n\|\ge I_n^\Pi/4\) (Astra). Una cota inferior \(I_n^\Pi\gtrsim n\) probaría
  que el coeficiente de Lipschitz local es de orden \(n\). Esa cota inferior está
  abierta. La simulación da \(I_n^\Pi\) creciente para \(n\le4\), pero no la prueba.

`[CORRECCIÓN 2026-10-16, tras la encuesta]` Una versión anterior proponía como objeto
el resto lineal \(\|s_n(\tau+h/\sqrt n)-s_n(\tau)-(h/\sqrt n)\dot s_n\|\to0\). Está **mal
planteado**: tampoco tiende a 0 en el modelo iid regular, que sí es LAN. Con
\(s_n=s^{\otimes n}\) y \(a=h^2I/8\), su cuadrado tiende a
\(2(1-e^{-a})+2a-4ae^{-a}=3a^2+O(a^3)\) (Opus y Astra por separado; rehecho por Claude).
LAN es un enunciado sobre la log-verosimilitud:
\(\log dP_{\tau+h/\sqrt n}/dP_\tau=h\Delta_n-\tfrac12h^2I^\Pi+o_P(1)\) con
\(\Delta_n\Rightarrow N(0,I^\Pi)\). Para \(\Pi_n\) está abierta y, según la encuesta
(`revisiones/2026-10-16-encuesta-escala-lan/sintesis.md`), **no hace falta** para las
cotas inferiores sobre el orden de la tasa. Solo haría falta para constantes óptimas
o para eficiencia.
Tampoco se abren la mezcla Poisson ni el puente Fisher–localización.

## 7. Corolario C: cota inferior de dos puntos en la caja EF

Lo propusieron por separado los cuatro modelos de la encuesta
(`revisiones/2026-10-16-encuesta-escala-lan/sintesis.md`). Es la contrapartida, en la
caja EF, del Teorema 3.8 de `docs/manuscript_limits_draft.md`.

**Corolario C.** Sea \(\bar J=\sup_KJ\). Para todo \(n\ge1\), todo
\(\tau,\tau+\delta\in K\) y todo estimador \(\widehat\tau\), posiblemente aleatorizado,
que sea función de \(\Pi_n\) o del poset sin etiquetas \([P_{\Pi_n}]\):

1. \(\mathrm{TV}(\mathcal L_\tau,\mathcal L_{\tau+\delta})\le\tfrac{|\delta|}{2}\sqrt{n\bar J}\),
   tanto para la ley de \(\Pi_n\) como para la del poset.
2. \(\mathbb P_\tau(|\widehat\tau-\tau|\ge|\delta|/2)+
   \mathbb P_{\tau+\delta}(|\widehat\tau-\tau-\delta|\ge|\delta|/2)\ge
   1-\tfrac{|\delta|}{2}\sqrt{n\bar J}\).
3. Ningún procedimiento basado solo en el orden localiza \(\tau\) con precisión
   \(|\delta|/2\) y confianza \(1-\epsilon\) en ambos extremos si
   \(|\delta|<2(1-2\epsilon)/\sqrt{n\bar J}\).

*Prueba.* A \(n\) fijo, \(s_n\) es \(C^1\) en \(K\) (Teorema B) y
\(\|\dot s_n\|^2=\sum_\sigma\pi_\sigma'^2/(4\pi_\sigma)=I_n^\Pi/4\) (\(\pi_\sigma>0\), wp6 §6).
Como \(K\) es un intervalo, por el teorema fundamental del cálculo y el Teorema A,
\(\|s_n(\tau+\delta)-s_n(\tau)\|\le\int\|\dot s_n\|\le\tfrac{|\delta|}{2}\sqrt{n\bar J}\). Además,
\(\mathrm{TV}=\tfrac12\sum|\sqrt p-\sqrt q|(\sqrt p+\sqrt q)\le\|\sqrt p-\sqrt q\|_2\) por
Cauchy–Schwarz, ya que \(\|\sqrt p+\sqrt q\|_2\le2\). El poset es imagen de \(\Pi_n\) por un
mapa fijo (wp6 (15.3)), así que la TV se contrae. El punto 2 es el lema de dos
puntos aplicado al test \(1\{\widehat\tau>\tau+\delta/2\}\); el punto 3 se sigue de 2. \(\square\)

**Consecuencias.**

- Cierra en negativo el hueco 4 de `wp4_fisher_localization_floor.md` §6, que preguntaba
  si el canal de orden alcanza la tasa \(1/n\) de la ley de un punto en la caja EF
  (Proposición 3 de wp4). **No la alcanza**: ningún estimador basado solo en el orden
  baja del orden \(1/\sqrt{n\bar J}\). La ventaja del soporte móvil (estadísticos
  extremos) se pierde al quedarse solo con el orden.
- **No** establece la tasa minimax \(n^{-1/2}\) en la caja EF: falta una cota superior
  basada en el orden, que es el puente Fisher–localización, abierto.
- Solo vale a \(N=n\) fijo. Opus sugiere que con \(N\) de Poisson la cota se extendería
  con \(E[N]\), porque en una caja rectangular en \((v,r)\) la ley de \(N\) no depende de
  \(\tau\) [UNVERIFIED].
- La constante es la de la cota de TV, no la del riesgo gaussiano.

## 8. Corolario D: mezcla de Poisson

En el protocolo Poisson, \(N\sim\mathrm{Poisson}(\Lambda)\) con \(\Lambda=\lambda T L\). En la caja
EF, \(\sqrt{-g}=1\) en \((v,r)\) (`nachocausal/generator.py:9-12`), así que la ley de \(N\) no
depende de \(\tau\). Dado \(N=n\), los puntos son iid uniformes y \(\Pi_n\) es el de §1. Se
observa \((N,\Pi_N)\), o el poset sin etiquetas, que determina \(N\) y es imagen fija de
\((N,\Pi_N)\). Con pesos \(w_n=e^{-\Lambda}\Lambda^n/n!\), el vector de raíces es
\(S(\tau)=(\sqrt{w_n}\,s_n(\tau))_{n\ge0}\).

**Corolario D.** En \(K\):
1. \(I^{\mathrm{Pois}}(\tau)=\sum_nw_nI_n^\Pi(\tau)\le\Lambda J(\tau)\).
2. \(S\) es \(C^1\) con valores en \(\ell^2\), con \(\dot S=(\sqrt{w_n}\dot s_n)\), y
   \(\|S(\tau+h)-S(\tau)-h\dot S(\tau)\|\le\tfrac{h^2}{2}C_K\sqrt{\Lambda+\Lambda^2}\). La mezcla es
   QMD, uniformemente en \(K\).
3. \(\mathrm{TV}(P_\tau,P_{\tau+\delta})=\sum_nw_n\mathrm{TV}_n\le\tfrac{|\delta|}{2}\sqrt{\bar J}\,E\sqrt N
   \le\tfrac{|\delta|}{2}\sqrt{\bar J\Lambda}\). Así, la cota inferior del Corolario C vale con
   \(\Lambda\) en lugar de \(n\).

*Prueba.* Los bloques con distinto \(n\) tienen soportes disjuntos y el mismo peso
\(w_n\) para todo \(\tau\); de ahí la igualdad de 3 y la suma de 1. Por los Teoremas A y B,
\(\sum_nw_n\sup_K\|\dot s_n\|^2\le\bar J\Lambda/4\) y
\(\sum_nw_n\sup_K\|\ddot s_n\|^2\le C_K^2E N^2=C_K^2(\Lambda+\Lambda^2)\). Estas son las cotas
dominantes uniformes en \(n\) que pedía `docs/physical_channel_observable_bridge_2026-09.md`
§4 (líneas 177–181). Con ellas, la derivación término a término en \(\ell^2\) y el teorema
fundamental del cálculo valen componente a componente y se suman. Para 3 se usa
Jensen, \(E\sqrt N\le\sqrt\Lambda\). \(\square\)

## 9. Cota inferior lineal de Fisher y cota superior condicional

Sea \(p(\tau)=P_\tau(\text{dos puntos están relacionados causalmente})\), es decir, la
probabilidad de la permutación identidad para \(n=2\). Sea
\(U_n=\binom n2^{-1}\#\{\text{pares relacionados}\}\). \(U_n\) es función de \(\Pi_n\) (los pares
que no forman inversión) y del poset sin etiquetas (su número de relaciones).

**Proposición E (cota inferior lineal).** Para \(n\ge2\) y \(\tau\in K\),

\[
I_n^\Pi(\tau)\ \ge\ \frac{n\,p'(\tau)^2}{4\,p(\tau)(1-p(\tau))}.
\]

*Prueba.* \(U_n\) es un U-estadístico de núcleo \(h\in\{0,1\}\). Por la fórmula de Hoeffding,
\(\operatorname{Var}U_n=\binom n2^{-1}[2(n-2)\zeta_1+\zeta_2]\) con \(\zeta_1\le\zeta_2=p(1-p)\), luego
\(\operatorname{Var}U_n\le4p(1-p)/n\). Como \(S_n\) es finito,
\(\tfrac{d}{d\tau}E_\tau U_n=\sum_\sigma U(\sigma)\pi_\sigma'=\operatorname{Cov}(U_n,\text{score})\le
\sqrt{\operatorname{Var}U_n\,I_n^\Pi}\), y \(E_\tau U_n=p(\tau)\). \(\square\)

Con el Teorema A, \(I_n^\Pi\asymp n\) en todo \(\tau\) con \(p'(\tau)\ne0\). Por la cota de
Astra (§6), \(\|\ddot s_n\|\ge I_n^\Pi/4\), así que en esos puntos la escala \(n\eta\) del
Teorema B es la correcta en orden.

**Proposición F (cota superior, condicional).** Supóngase que \(p\) es \(C^1\) y
estrictamente monótona en \(K\), con \(m=\min_K|p'|>0\). Sea
\(\widehat\tau=p^{-1}(\mathrm{clip}_{p(K)}U_n)\), un estimador basado solo en el orden. Entonces

\[
\sup_{\tau\in K}E_\tau|\widehat\tau-\tau|\ \le\ \frac{2\sup_K\sqrt{p(1-p)}}{m\sqrt n}.
\]

*Prueba.* \(p^{-1}\) es \(1/m\)-lipschitziana en \(p(K)\), y recortar a \(p(K)\) no aleja de
\(p(\tau)\). Por tanto \(|\widehat\tau-\tau|\le|U_n-p(\tau)|/m\). Se concluye con Cauchy–Schwarz
y la cota de la varianza. \(\square\)

**Lema G (monotonía de \(p\)).** Para cada par fijo de puntos de \(B\), el suceso "están
relacionados" es no creciente en \(\tau\). Además, \(-p'(\tau)\ge c(\tau)\), con

\[
c(\tau)=\frac1{L^2}\iint_{\tau<r_1<r_2<r_b}\frac2T\Bigl(1-\frac{\Delta\varphi}{T}\Bigr)_+
\bigl(\gamma(r_2)-\gamma(r_1)\bigr)\,dr_1dr_2>0,
\]

donde \(\varphi_\tau(r)=2\tau\log|W_\tau(r)|=2r+2\tau\log(|r-\tau|/\tau)\),
\(\Delta\varphi=\varphi(r_2)-\varphi(r_1)\) y \(\gamma=\partial_\tau\varphi\). La función \(c\) es
semicontinua inferiormente, así que \(m:=\min_K|p'|\ge\min_Kc>0\).

*Prueba.* Sea \(\Delta v=v_2-v_1>0\). La relación equivale a
\(W(r_1)e^{\Delta v/(2\tau)}>W(r_2)\). Hay cuatro casos.

1. **Exterior y exterior.** La relación equivale a \(\Delta v>\Delta\varphi\). Si
   \(r_2\le r_1\), se cumple siempre. Si \(r_2>r_1\),
   \(\partial_\tau\Delta\varphi=\gamma(r_2)-\gamma(r_1)>0\), porque
   \(\gamma'(r)=2/(r-\tau)+2\tau/(r-\tau)^2>0\): el umbral sube.
2. **Interior y interior.** La relación equivale a \(\Delta v<\varphi(r_2)-\varphi(r_1)\) si
   \(r_2<r_1\), y no se da si \(r_2\ge r_1\). Aquí
   \(\gamma_{\rm int}'(r)=2r/(\tau-r)^2>0\), así que el umbral baja.
3. **Exterior antes que interior.** Siempre relacionados.
4. **Interior antes que exterior.** Nunca relacionados.

Cuando \(\tau\) cruza el radio de uno de los puntos, \(\varphi\to-\infty\) en el horizonte.
Revisando los cruces, el indicador es continuo o pasa de 1 a 0. Por ejemplo, con
\(r_2<r_1\) y \(r_1\) cruzando, se pasa del caso 3 al caso 2 con un umbral que tiende a
\(+\infty\). Por tanto el indicador es no creciente, y \(p(\tau)-p(\tau+h)\) es la
probabilidad de dejar de estar relacionados. Restringiendo al caso 1 con
\(r_2>r_1>\tau+h\), dividiendo por \(h\) y aplicando Fatou, se obtiene
\(-p'(\tau)\ge c(\tau)\). Aquí \(p\) es \(C^1\) porque es \(\pi_{\rm id}\) con \(n=2\) (wp6
§11). El integrando de \(c\) es positivo en un conjunto de medida positiva (\(r_2\)
cercano a \(r_1\), \(\Delta\varphi<T\)), y el factor \(1\{r_1>\tau\}\) es semicontinuo
inferiormente, de modo que \(c\) es semicontinua inferiormente y positiva. Por ser
\(K\) compacto, alcanza un mínimo positivo. \(\square\)

**Teorema H (tasa minimax en la caja EF).** Por el Lema G, la Proposición F se cumple
sin condiciones. Con el Corolario C, la tasa minimax de localización de \(\tau\) en
\(K\) por un procedimiento basado solo en el orden (\(\Pi_n\) o el poset sin etiquetas) es
\(n^{-1/2}\):

\[
\frac{c_1}{\sqrt{n\bar J}}\ \le\ \inf_{\widehat\tau}\sup_{\tau\in K}E_\tau|\widehat\tau-\tau|\ \le\
\frac{2\sup_K\sqrt{p(1-p)}}{m\sqrt n}.
\]

La cota superior la alcanza \(\widehat\tau=p^{-1}(\mathrm{clip}\,U_n)\), que solo usa el número
de relaciones del poset. En el protocolo Poisson vale lo mismo con \(\Lambda\) (Corolario
D; para la cota superior, condicionando a \(N\)). Es la contrapartida, en la caja EF, del
Corolario 3.10 del manuscrito para el diamante.

Comprobación numérica (criterios fijados antes de ejecutar):
- `dev/explore_ef_box_comparable_pair_monotonicity.py`: MONOTONE_ON_GRID; en la caja
  sellada, \(p'\in[-0.73,-0.43]\) en \(\tau\in[0.15,1.25]\).
- `dev/explore_ef_box_pairwise_relation_monotonicity.py`: LEMMA_CONSISTENT. En 2·10⁶
  pares y 116 valores de \(\tau\), el indicador nunca pasa de 0 a 1. Además
  \(0<c(\tau)\le-p'(\tau)\) en los 23 puntos (\(c\) va de 0.70 a 0.017; la cota es floja
  cerca de \(r_b\)).
- Otra vía: \(p'^2/(p(1-p))\) en \(\tau=0.5\) vale 1.425, frente a 1.421 del Monte Carlo
  independiente de \(I_2^\Pi\).

## 10. Comprobación numérica (caja sellada \(r\in[0.1,1.3]\), \(v\in[0,6]\))

Criterios fijados en el docstring antes de ejecutar:

- `dev/explore_create_fisher_quotient_check.py` (commit `dccc54b`):
  BOUND_CONSISTENT. \(\varphi\) reproduce \(\Pi_n\) en 600 000 muestras sin
  ninguna discrepancia. \(J(0.4,0.5,0.7)=5.52,\,4.38,\,3.49\). El Monte Carlo da
  \(I_n^\Pi/(nJ)\in[0.15,0.31]\) para \(n\le4\).
- `dev/explore_create_omega_modulus_check.py`: MODULUS_BOUND_CONSISTENT.
  \(|Eb+J|/J<10^{-7}\). El Monte Carlo de \(\|\ddot s_n\|\) queda entre 0.02 y 0.06
  veces la cota para \(n\le4\), y la cota dividida por \(n\) es casi constante.

Las comprobaciones numéricas cubren solo \(n\) pequeño. Para todo \(n\), el
resultado descansa en las pruebas de §4–§5.

## 11. Pendiente

1. ~~Lectura humana de §2–§5.~~ Hecha por el PI, 2026-10-16.
2. ~~Revisión por otra familia de la parte (b).~~ Hecha por Astra (no independiente); una revisión independiente de §5 sigue siendo deseable.
3. Cita de un criterio de QMD comprobado en la fuente. Aquí no hace falta: la
   prueba usa derivación bajo la integral, no el criterio. El lema 7.6 de van der
   Vaart no está en `biblioteca/` [UNVERIFIED].
4. ~~Cota inferior \(I_n^\Pi\gtrsim n\).~~ Probada donde \(p'\ne0\) (Prop. E).
5. ~~Monotonía de \(p\).~~ Lema G, §9.
6. Revisión ciega de §8–§9 (Corolario D, Proposiciones E y F, Lema G, Teorema H) por otra familia, y lectura del PI.
