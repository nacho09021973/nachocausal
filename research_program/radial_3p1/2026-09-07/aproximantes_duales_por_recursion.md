# Un intento constructivo: recurrencia polinomica y estimacion que falta

Fecha: 2026-09-07. Trabajo posterior al criterio conjunto congelado.

**Resultado parcial.** Se fija exactamente la correccion temporal y se
construye una sucesion explicita de polinomios de prueba, sin resolver
problemas de minimizacion. Se demuestran identidades y cotas para todos los
pasos. La cota obtenida hace desaparecer \(\|\omega K r_n\|_2\), **no**
\(\|r_n\|_2\). Por tanto este intento no demuestra todavia el limite de
las capacidades. No se presenta la recurrencia como una solucion del
problema de densidad.

## 1. La correccion temporal no necesita elegirse en cada paso

Conservamos \(\psi_k=a^2(2z-1)^k\), \(d_k=B^*\psi_k\),
\(g_t=(y-x)(x+y-1)\) y
\[
b_t(z)=-\frac{(2z-1)(3z^2-3z+1)}{24}.
\]
Por dualidad, \(\langle d_k,g_t\rangle=v_k(b_t)\). La sustitucion
\(u=2z-1\) da, para \(k\) impar,
\[
v_k(b_t)=-\frac1{1536}
\left(\frac1{k+2}+\frac1{k+4}-\frac5{k+6}+\frac3{k+8}\right)
=-\frac{2k+7}{96(k+2)(k+4)(k+6)(k+8)}.
\tag{1}
\]
Para \(k\) par este momento es cero. En particular,
\(v_1(b_t)=-1/10080\). Definimos
\[
\lambda_k=
\begin{cases}
0,&k\text{ par},\\
\displaystyle\frac{105(2k+7)}{(k+2)(k+4)(k+6)(k+8)},&k\text{ impar},
\end{cases}
\qquad h_k=d_k-\lambda_k d_1.
\tag{2}
\]
Asi \(h_k\perp g_t\), \(h_1=0\), y, por ejemplo, \(\lambda_3=13/33\).

Esta eleccion es necesaria en el limite. Si
\[
e_n=K^*\theta_n-d_k+\lambda_n d_1\longrightarrow0,
\]
entonces, por \(Kg_t=0\),
\[
\langle e_n,g_t\rangle=(\lambda_n-\lambda_k)v_1(b_t),\qquad
|\lambda_n-\lambda_k|\le\frac{10080}{\sqrt{90}}\|e_n\|_2.
\tag{3}
\]
Sustituir \(\lambda_n\) por \(\lambda_k\) conserva la convergencia del
residuo a cero. Por tanto se puede fijar (2) desde el principio sin perder
ninguna posible construccion convergente. La correccion elimina la
obstruccion temporal conocida, no otros posibles elementos del nucleo.

## 2. Un operador positivo que genera polinomios

Sea \(\omega=x(1-x)y(1-y)\). Introducimos en \(H_{\rm alt}\)
\[
\mathcal A=K^*M_{\omega^2}K,\qquad R=I-4\mathcal A.
\tag{4}
\]
\(\mathcal A\) no es el operador \(\mathscr A=K-6UB\) del criterio
congelado. Tampoco es la energia auxiliar descartada: aqui la positividad
es la identidad elemental
\[
\langle\mathcal A f,f\rangle=\|\omega Kf\|_2^2\ge0.
\tag{5}
\]
Esta identidad no afirma coercividad ni clasifica su nucleo.

Para justificar un paso racional fijo en (4), basta una cota no optima.
El nucleo de \(L\) tiene norma de Hilbert--Schmidt \(1/\sqrt6\).
Ademas,
\[
C_0f(x)=\int_0^1 t f(tx)\,dt,\qquad
\|C_0\|\le\int_0^1 t^{1/2}\,dt=\frac23.
\]
Por reflexion y por los factores multiplicativos que definen \(C,E\),
\[
\|L\|,\|R_+\|\le\frac1{\sqrt6},\qquad
\|C\|,\|E\|\le\frac23.
\]
La formula de cuatro productos tensoriales de \(K\) implica
\[
\|K\|\le1+\frac{16}{\sqrt6}<8.
\]
Como \(\|\omega\|_\infty=1/16\),
\[
0\le\mathcal A\le\frac14 I,\qquad 0\le R\le I.
\tag{6}
\]
El operador \(R\) es, por tanto, una contraccion autoadjunta positiva.

La propiedad constructiva es que \(\mathcal A\) conserva polinomios:
\(K\) envia un polinomio antisimetrico a uno simetrico, y la identidad
congelada da
\[
Y_P=K^*(\omega^2P)=F_P+12B^*r_P,
\tag{7}
\]
que es polinomica. Todas estas operaciones conservan coeficientes
racionales. No hace falta aplicar el adjunto general a funciones con
logaritmos de borde.

## 3. Los candidatos explicitos

Para cada \(k\ne1\), ponemos
\[
r_{0,k}=h_k,\qquad P_{0,k}=0,
\]
\[
\boxed{
\begin{aligned}
P_{n+1,k}&=P_{n,k}+4Kr_{n,k},\\
r_{n+1,k}&=r_{n,k}-4Y_{Kr_{n,k}}.
\end{aligned}}
\tag{8}
\]
Equivale a \(r_{n,k}=R^nh_k\). La identidad telescopica es
\[
\boxed{K^*(\omega^2P_{n,k})-d_k+\lambda_k d_1=-r_{n,k}.}
\tag{9}
\]
En particular, se conocen las pruebas mismas, no solo sus valores
variacionales:
\[
P_{n,k}=4\sum_{j=0}^{n-1}K R^j h_k.
\]

Las paridades se conservan en todos los pasos: \(r_{n,k}\) tiene paridad
\((-1)^{k+1}\) bajo reflexion simultanea, y \(P_{n,k}\), paridad
\((-1)^k\). Ademas \(r_{n,k}\perp g_t\).

Se tiene \(\deg d_k\le k+5\), \(\deg Kf\le\deg f+1\) y
\(\deg Y_P\le\deg P+9\). La segunda desigualdad usa la cancelacion
de los terminos superiores de los pares reflejados, establecida en la
seccion 7.1 de la nota archivada del dominio. La primera y tercera se
leen directamente en las formulas polinomicas de \(D_k,F_P,r_P\).
Por induccion, para \(n\ge1\),
\[
\deg P_{n,k}\le N_{n,k}:=k+6+10(n-1).
\tag{10}
\]
La comparacion dual congelada proporciona la cota genuina
\[
\boxed{\kappa_{N_{n,k},k}\le\|r_{n,k}\|_2^2.}
\tag{11}
\]
La existencia de (8) no asegura que el miembro derecho tienda a cero.

## 4. Lo que se logra estimar para todos los pasos

Omitiendo \(k\), por (5)-(6),
\[
\begin{aligned}
\|r_n\|_2^2-\|r_{n+1}\|_2^2
&=8\|\omega Kr_n\|_2^2-16\|\mathcal A r_n\|_2^2\\
&\ge4\|\omega Kr_n\|_2^2\ge0.
\end{aligned}
\tag{12}
\]
La sucesion \(\|\omega Kr_n\|_2^2=\langle\mathcal A R^{2n}h,h\rangle\)
es decreciente, porque \(\mathcal A\) y \(R\) conmutan y son positivos.
Sumar (12) demuestra
\[
\boxed{\|\omega Kr_{n,k}\|_2\le
\frac{\|h_k\|_2}{2\sqrt{n+1}}.}
\tag{13}
\]
Esta es una cota analitica, no una extrapolacion del verificador.
Pero controla un operador aplicado al residuo, no el residuo de (9).

Tambien se obtiene
\[
\|r_n-r_{n+1}\|_2\le\frac{\|h\|_2}{n+1}.
\tag{14}
\]
En efecto, como \(0\le R\le I\),
\[
0\le(n+1)R^n(I-R)\le\sum_{j=0}^nR^j(I-R)=I-R^{n+1}\le I.
\]
La cota (14) no es sumable y no demuestra que el limite sea cero.

## 5. El limite exacto de la recurrencia y la brecha

Por (5), y porque \(\omega>0\) casi por doquier,
\[
\ker\mathcal A=\ker K.
\]
Las potencias de \(R\) convergen fuertemente a la proyeccion sobre ese
nucleo. Puede probarse aqui sin invocar un resultado adicional: en
\(\operatorname{Ran}(I-R)\), la desigualdad usada para (14) da
\(R^n(I-R)v\to0\). La autoadjuncion implica
\[
\overline{\operatorname{Ran}(I-R)}=(\ker(I-R))^\perp.
\]
La cota uniforme \(\|R^n\|\le1\) extiende esa convergencia al cierre;
en \(\ker(I-R)\), las potencias son la identidad. Luego
\[
\boxed{r_{n,k}\longrightarrow\Pi_{\ker K}h_k\quad\hbox{en }L^2.}
\tag{15}
\]
Por tanto, conocer \(h_k\perp g_t\) solo elimina la parte temporal de
este limite. No elimina una posible componente sobre otros vectores
de \(\ker K\). Usar la unicidad para anular (15) seria circular.

Una forma concreta de cerrar el intento seria exhibir, para cada \(k\),
un vector \(v_k\) con
\[
h_k=\mathcal A v_k.
\tag{16}
\]
Entonces (14), aplicada a \(v_k\), daria la cota requerida
\[
\|r_{n,k}\|_2\le\frac{\|v_k\|_2}{4(n+1)}.
\tag{17}
\]
Pero **(16) no se ha demostrado** y es mas fuerte que lo necesario.
Ademas \(v_k\) no puede ser un polinomio: de serlo,
\(\theta=\omega^2Kv_k\) seria un levantamiento polinomico exacto de
\(d_k-\lambda_kd_1\), excluido para \(k\ne1\) por la
[obstruccion polinomica dual](levantamiento_polinomico_dual.md).
No se deduce de ello que un \(v_k\) no polinomico sea imposible.

Asi, la recurrencia aporta candidatos racionales explicitos y una
estimacion all-step mas debil, pero no ha permitido probar el limite
de (11). No se introduce una nueva capacidad ni se modifica el objetivo.

## 6. Verificacion y limites de la evidencia

[verify_dual_recursion.py](verify_dual_recursion.py) comprueba la identidad
racional general de (1), los momentos temporales para \(k=0,\ldots,9\),
y dos pasos exactos de (8) para \(k=0,3\), uno por cada sector no trivial.
Comprueba dualidad, telescopado, paridad, normalizacion, grados e identidad
de descenso. Los dos pasos no son evidencia del limite cero.

```text
python3 research_program/radial_3p1/2026-09-07/verify_dual_recursion.py
```

Salida: [verification_dual_recursion.json](verification_dual_recursion.json).
El verificador comprueba los hashes congelados antes y despues. No se
amplia la tabla de capacidades. Las pruebas analiticas anteriores son de
trabajo con verificacion interna; no hay adjudicacion independiente.

## 7. Cierre del intento: el residuo se reduce exactamente al nucleo

Esta seccion registra el estado terminal de esta via. No se buscara una
cota mejor de \(\|r_{n,k}\|_2\) por esta ruta.

**Lema (reduccion exacta al nucleo).** Para cada \(k\ne1\),
\[
\boxed{
\lim_{n\to\infty}\|r_{n,k}\|_2=0
\iff
\Pi_{\ker K}h_k=0
\iff
h_k\perp\ker K,}
\]
donde \(\ker K\) se entiende dentro de \(H_{\rm alt}\), que es donde vive
\(h_k\) y donde actua la recurrencia.

*Prueba.* Es (15) mas \(\ker\mathcal A=\ker K\) de la seccion 5. \(\square\)

El obstaculo restante es **espectral, no cuantitativo**. La cota (13)
hace desaparecer \(\|\omega Kr_n\|_2\), es decir, exactamente la parte de
\(r_n\) visible por \(K\); toda componente de \(h_k\) en \(\ker K\) es
invisible para la iteracion y sobrevive intacta. Ningun argumento
construido solo con \(K^*M_{\omega^2}K\) puede eliminarla, porque esa
componente esta en el nucleo del propio operador que genera la
iteracion. Refinar (13) o (14) no cambia esto.

La correccion (2) garantiza unicamente \(h_k\perp g_t\). Si se supiera
\(\ker K=\operatorname{span}\{g_t\}\), el lema daria \(r_{n,k}\to0\) de
inmediato; invocarlo ahora seria asumir la unicidad radial pendiente, que
es lo que se quiere demostrar. La nota archivada del 2026-09-06 la deja
explicitamente sin demostrar.

**Valor que se conserva.** El lema convierte esta construccion en un
*certificado condicional*: en cuanto se cierre \(\ker K=\operatorname{span}\{g_t\}\),
se obtienen aproximantes polinomicos **explicitos** \(P_{n,k}\) con
coeficientes racionales, no minimizadores abstractos, y con (11) la
consecuencia \(\kappa_{N_{n,k},k}\to0\) a lo largo de
\(N_{n,k}=k+6+10(n-1)\).

**Direccion del certificado.** La implicacion util es una sola:
\(r_{n,k}\to0\Rightarrow\kappa_{N,k}\to0\). El reciproco es falso como
argumento: que las capacidades tiendan a cero no exige que *esta*
recurrencia converja. Por tanto el lema **no** afirma que el problema de
densidad sea equivalente a la unicidad radial; afirma que la convergencia
de esta recurrencia lo es.

**Evidencia numerica y su limite.** En `verification_dual_recursion.json`,
el cociente \(\|r_{n+1}\|_2^2/\|r_n\|_2^2\) es 0.99848, 0.99849 para
\(k=0\) y 0.99782, 0.99782 para \(k=3\): la masa espectral de \(h_k\)
esta concentrada cerca de \(\lambda=1\) para \(R\). Como
\(\|r_n\|_2^2=\int\lambda^{2n}d\mu_{h_k}\) y el limite buscado es
\(\mu_{h_k}(\{1\})\), unos pocos pasos no pueden separar decaimiento
subgeometrico de limite positivo, y cada paso adicional cuesta grado
\(+10\). No se propone extender la tabla: la recurrencia tampoco sirve
como diagnostico numerico de la unicidad.

**Siguiente paso (fuera de esta via).** Demostrar que no hay componentes
\(L^2\) de \(\ker K\) aparte de \(g_t\). El asidero mas fuerte disponible
no es otra energia iterativa sino la equivalencia exacta ya establecida
en la seccion 3 de la nota del 2026-09-06,
\[
Kg=0\iff Pf=f\ \hbox{y}\ \mathcal D=0,
\qquad f=g/(y-x),
\]
con \(P\) el nucleo de Markov explicito (9), no negativo y con
\(P1=1\). Eso reduce la unicidad a una propiedad de tipo Liouville para
\(P\) restringida por \(\mathcal D=0\): \(f=1\) y \(f=x+y-1\) son puntos
fijos, y solo el segundo satisface \(\mathcal D=0\). Queda por decidir si
hay mas funciones armonicas admisibles. Esta reduccion es una
observacion sobre donde mirar, no un resultado nuevo.
