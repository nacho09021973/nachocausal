# `UNIFORM_IN_N_REGULARITY` para la caja EF fija — cociente por lado del horizonte

```text
ESTADO: PROVED_MODEL_REVIEWED — NO_HUMAN_READ
FECHA: 2026-10-16
ENTRADA: research_program/work_packages/wp6_domain_bridge_fixed_ef_box.md §13–§19
NATURALEZA: prueba analítica; comprobación numérica en dev/ (sin semillas del track sellado)
UNIFORM_IN_N_FISHER_BOUND = PROVED_LINEAR            (I_n^Pi <= n J(tau))
UNIFORM_SQRT_SCORE_MODULUS = PROVED_LINEAR_WINDOW     (Omega_{n,K}(eta) <= C_K n eta)
UNIFORM_QMD_WINDOW = delta_n = o(1/n)
UNIFORM_QMD_AT_LAN_SCALE = NOT_IMPLIED (ver §6)
POISSON_MIXTURE_REGULARITY = OPEN_NOT_STARTED
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
`revisiones/2026-10-16-cociente-horizonte-ciego/` (commit `278d536`). La parte (b)
(§5) no ha tenido revisión de otra familia. **Ninguna persona ha leído este
documento.** El estado `PROVED_MODEL_REVIEWED` se fija por decisión del PI
(2026-10-16) y debe revisarse tras la lectura humana.

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

La ventana \(n\delta_n\to0\) es la natural de este argumento. En el experimento
gaussiano producto \(N(\tau,1)^{\otimes n}\), el módulo es del orden de \(n\delta\),
así que en la escala \(\delta_n=h/\sqrt n\) no tiende a 0 (cálculo propuesto por
la ruta 4 de Opus en la prueba CREATE; comprobado aquí solo en su escala).
Por tanto el Teorema B **no** implica QMD uniforme en la escala LAN. Si el
argumento posterior la necesita, el objeto correcto es un resto relativo, por
ejemplo \(\|s_n(\tau+h/\sqrt n)-s_n(\tau)-(h/\sqrt n)\dot s_n\|\to0\), y eso queda
abierto. Tampoco se abren la mezcla Poisson, el puente Fisher–localización ni
cotas inferiores de \(I_n^\Pi\).

## 7. Comprobación numérica (caja sellada \(r\in[0.1,1.3]\), \(v\in[0,6]\))

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

## 8. Pendiente

1. Lectura humana de §2–§5.
2. Revisión por otra familia de la parte (b) (§5) y de la dominación de segundo orden de §3.
3. Cita de un criterio de QMD comprobado en la fuente. Aquí no hace falta: la
   prueba usa derivación bajo la integral, no el criterio. El lema 7.6 de van der
   Vaart no está en `biblioteca/` [UNVERIFIED].
