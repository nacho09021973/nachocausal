# `DOMAIN_BRIDGE` para la caja EF fija — obstrucción QMD del experimento puntual

```text
ESTADO: PROVED
FECHA: 2026-08-28
GOBERNANZA: docs/program_domain_bridge_authorization_2026-08-28.md
ENTRADA: docs/physical_reentry_audit_001_2026-08-28.md §12
NATURALEZA: prueba analítica; cero simulación, cero semillas
```

## 1. Enunciado y techo

Fijemos

\[
B=[0,T]\times[r_a,r_b],\qquad 0<r_a<r_b,
\]

y un intervalo compacto de parámetros \(K\Subset(0,\infty)\). En coordenadas
EF ingoing la medida puntual normalizada es uniforme en \(B\). En coordenadas
nulas globales

\[
v=v,\qquad
u_\tau(v,r)=-e^{-v/(2\tau)}W_\tau(r),\qquad
W_\tau(r)=e^{r/\tau}(r/\tau-1),
\]

el orden es el orden producto y la ley tiene soporte móvil \(S_\tau\).

**Teorema (obstrucción de dominio).** Para cada
\(\tau\in\operatorname{int}K\),

\[
H^2(p_\tau,p_{\tau+\delta})\ge c_\tau|\delta|
\]

para \(|\delta|\) suficientemente pequeño y alguna \(c_\tau>0\). Por tanto la
familia puntual \(\{p_\tau\}\) no es QMD. No existe un isomorfismo estadístico
común, independiente de \(\tau\), que la transforme en una familia QMD de
soporte fijo. En particular, el transporte de coordenadas requerido en la
auditoría física §12 no existe dentro de esa clase natural.

El teorema no afirma que la ley finita de `Pi_n` o `[P_{Pi_n}]` sea no-QMD:
un canal puede regularizar una familia no regular. Tampoco identifica Fisher
con el localizador `O=|future|`.

## 2. Densidad y cotas uniformes locales

Como

\[
\partial_r W_\tau(r)=\frac{r}{\tau^2}e^{r/\tau}>0,
\]

el mapa \(r\mapsto u_\tau(v,r)\) es estrictamente decreciente. Es un
difeomorfismo sobre cada fibra y

\[
S_\tau=\left\{(u,v):0\le v\le T,\quad
-e^{-v/(2\tau)}W_\tau(r_b)\le u\le
-e^{-v/(2\tau)}W_\tau(r_a)\right\}.
\]

El cambio de variables desde la densidad \(1/[T(r_b-r_a)]\) da

\[
p_\tau(u,v)=
\frac{\tau^2 e^{v/(2\tau)-r/\tau}}
     {T(r_b-r_a)r},
\qquad r=r_\tau(u,v),
\]

en \(S_\tau\), y cero fuera. En cualquier vecindad compacta de un
\(\tau\in\operatorname{int}K\), continuidad y \(r\in[r_a,r_b]\) proporcionan
constantes \(0<m\le p_\sigma\le M<\infty\), uniformes en \(\sigma\).

## 3. Velocidad de los bordes

Para un borde generado por \(r=r_j\), \(j\in\{a,b\}\), escribamos

\[
b_{j,\tau}(v)=-e^{(r_j-v/2)/\tau}(r_j/\tau-1).
\]

La derivación directa da

\[
\partial_\tau b_{j,\tau}(v)
=\frac{e^{(r_j-v/2)/\tau}}{\tau^2}
\left[(r_j-v/2)(r_j/\tau-1)+r_j\right].
\]

El corchete es afín en \(v\). Si \(r_j\ne\tau\), tiene a lo sumo un cero;
si \(r_j=\tau\), vale \(r_j>0\). Por tanto

\[
A_\tau:=\sum_{j\in\{a,b\}}\int_0^T
|\partial_\tau b_{j,\tau}(v)|\,dv>0.
\]

La diferenciabilidad uniforme de los bordes y el hecho de que la anchura de
cada fibra es positiva implican, para \(\delta\to0\),

\[
|S_\tau\triangle S_{\tau+\delta}|
=A_\tau|\delta|+o(|\delta|).
\]

En particular, existe \(d_\tau>0\) tal que la diferencia simétrica tiene área
al menos \(d_\tau|\delta|\). Al menos una de las dos diferencias orientadas
tiene la mitad de esa área.

## 4. Cota Hellinger y fallo QMD

Con la convención

\[
H^2(p,q)=\int(\sqrt p-\sqrt q)^2,
\]

en \(S_\tau\setminus S_{\tau+\delta}\) el integrando es \(p_\tau\), y en la
diferencia opuesta es \(p_{\tau+\delta}\). La cota inferior uniforme de §2
produce

\[
H^2(p_\tau,p_{\tau+\delta})
\ge m\max\{|S_\tau\setminus S_{\tau+\delta}|,
|S_{\tau+\delta}\setminus S_\tau|\}
\ge \frac{m d_\tau}{2}|\delta|.
\]

Una familia QMD tendría

\[
H^2(p_\tau,p_{\tau+\delta})=O(\delta^2).
\]

La cota lineal lo contradice. Queda probado

```text
MOVING_SUPPORT_QMD_STATUS = PROVED_NON_QMD_FOR_POINT_EXPERIMENT
```

## 5. Invariancia y cierre del candidato de transporte

Sea \(T\) un isomorfismo medible común, independiente de \(\tau\), y sean
\(q_\tau=T_\#p_\tau\). La afinidad de Hellinger, y por tanto \(H^2\), se
preserva exactamente bajo \(T\). Si \(\{q_\tau\}\) fuera QMD, su distancia
Hellinger sería \(O(\delta^2)\), en contradicción con §4. Por consiguiente no
hay un cambio de coordenadas paramétricamente común que convierta el
experimento puntual de la caja EF en el experimento regular de S1/S2.

Un mapa dependiente de \(\tau\) puede fijar el soporte, pero entonces el
canal de orden también depende de \(\tau\); no es el transporte común exigido
por `DOMAIN_BRIDGE`.

## 6. Veredicto y siguiente frontera

```text
COMMON_POINT_ISOMORPHISM = REFUTED
MOVING_SUPPORT_QMD_STATUS = PROVED_NON_QMD_FOR_POINT_EXPERIMENT
FINITE_CHANNEL_REGULARITY = OPEN
DOMAIN_BRIDGE = OPEN_AT_FINITE_CHANNEL
FISHER_TO_LOCALISATION_BRIDGE = NOT_OPENED
NEXT_RUN_AUTHORIZED = NO
```

El esqueleto finito `Pi_n -> [P_{Pi_n}]` continúa siendo exacto. El siguiente
objeto matemático posible sería la regularidad de la ley inducida después del
canal. Esa cuestión es justamente el residuo de `DOMAIN_BRIDGE`, requiere una
decisión separada y no queda autorizada por este resultado.
