# `NC-2B` — existencia eventual y bloqueo de la masa interior seleccionada

> **ESTADO: ATAQUE ANALÍTICO EJECUTADO EN ORDEN · `NC2B-O1` PROBADO ·
> `NC2B-O2` ABIERTO · `NC2B-O3` NO ABIERTO POR PRECEDENCIA · SIN DATOS,
> SIMULACIONES, BARRIDOS, CÓDIGO NI ARTEFACTOS NUMÉRICOS NUEVOS.**

Autorización firmada:
`docs/program_reopening_note_2026-08-17_nc2b_selected_law_DRAFT.md`.
El sufijo histórico `_DRAFT` no describe su estado actual; la firma consta en la
§9 de esa nota.

## 1. Precedencia y objeto

Se usa literalmente el selector congelado

```text
Q_3(C) = {(a,b,c,d): a prec b prec c prec d,
          |[a,b]|>=3, |[c,d]|>=3},

S_lex(q) = (min(m_-(q),m_+(q)), m_-(q)+m_+(q)),

S = {S_lex tiene un unico maximizador en Q_3(C)}.
```

En la representación `d=2`, el poset se obtiene de una permutación uniforme
`Pi_n`: `i prec j` si y solo si `i<j` y `Pi_n(i)<Pi_n(j)`. Los intervalos son
cerrados, como verifica literalmente
`emergencia/p1a_enumeracion_simulacion.py` en `interval_count_matrix`.

No se importa como teorema el certificado específico EF-4/EF-7 de masa
subexponencial: la genealogía vigente dejó esa aplicación `INCONCLUSIVE`. Los lemas
abstractos que no dependen de la familia prescrita siguen siendo contexto, pero no
deciden ninguna obligación de esta nota.

## 2. Lema para una cadena total par

**Lema 2.1.** Sea `C_N` una cadena total con `N=2r>=6` elementos. El selector
`MIN_COVERAGE_LEX` tiene un maximizador único, formado por los primeros `r` y los
últimos `r` elementos de la cadena, y

\[
m_-=m_+=r.
\]

**Demostración.** Para una cuádrupla `a<b<c<d` de la cadena, escríbanse

\[
x=|[a,b]|,
\qquad
y=|[c,d]|.
\]

Los dos intervalos cerrados son disjuntos, luego `x+y<=N`. Por tanto

\[
\min(x,y)\le\frac{x+y}{2}\le r.
\]

Alcanzar el valor primario `r` exige simultáneamente `x=y=r` y `x+y=N`.
La segunda igualdad no deja elementos antes, entre ni después de los intervalos;
así, los endpoints quedan forzados y la cuádrupla es única. Como `r>=3`, pertenece
a `Q_3(C_N)`. `QED`

## 3. `NC2B-O1` — existencia eventual

**Teorema 3.1.** Para todo `n>=6`,

\[
\Pr_n(S)\ge\frac1{n!}>0.
\tag{3.1}
\]

En particular, la ley condicionada por `(n,h,S)` existe para ambos lados y para
toda la cola `n>=6`.

**Demostración.**

### Caso par

Para `n=2r`, tómese la permutación identidad

\[
\pi_n=(1,2,\ldots,n).
\]

Su poset es la cadena total `C_n`. El Lema 2.1 da un ganador único.

### Caso impar

Para `n=2r+1>=7`, tómese

\[
\pi_n=(2,3,\ldots,n,1).
\]

Los primeros `n-1=2r` puntos forman una cadena total. El último punto tiene
índice mayor y rango menor que todos ellos, por lo que es incomparable con cada
punto de la cadena. No puede pertenecer a ninguna 4-cadena y tampoco cae dentro de
un intervalo cuyos endpoints están en la cadena. En consecuencia, `Q_3(C)` y sus
cardinalidades coinciden exactamente con los de `C_{n-1}`. El Lema 2.1 vuelve a dar
un ganador único.

Cada permutación concreta tiene probabilidad `1/n!` bajo la ley uniforme. En ambos
casos se ha exhibido una que pertenece a `S`, lo que prueba (3.1). `QED`

Esta prueba no afirma que `S` sea frecuente ni subexponencialmente raro. Solo
demuestra la positividad requerida para definir los condicionamientos en una cola
completa.

```text
NC2B_O1_EVENTUAL_SELECTION = PROVED_FOR_ALL_N_GE_6
NC2B_O1_PROBABILITY_LOWER_BOUND = 1/n!
```

## 4. La masa interior no es una consecuencia determinista de `S`

La construcción del Teorema 3.1 produce

\[
M_-=M_+=
\begin{cases}
n/2,&n\text{ par},\\
(n-1)/2,&n\text{ impar},
\end{cases}
\]

y por tanto demuestra que `S` contiene configuraciones interiores para todo
`n>=6`.

Sin embargo, `S` también contiene configuraciones de borde para todo `n>=6`.

**Lema 4.1.** Para cada `n>=6`, la permutación

\[
\tau_n=(n,n-1,\ldots,7,1,2,3,4,5,6),
\tag{4.1}
\]

con el prefijo vacío cuando `n=6`, pertenece a `S` y su ganador satisface

\[
M_-=M_+=3.
\tag{4.2}
\]

**Demostración.** El prefijo formado por los valores `n,n-1,...,7` es decreciente,
así que sus puntos son mutuamente incomparables. Todos sus índices preceden a los
seis puntos finales, pero sus valores son mayores que `1,...,6`; por tanto también
son incomparables con cada punto final. Los seis puntos finales forman una cadena
total `C_6` y contienen todas las comparabilidades del poset. El Lema 2.1, con
`N=6`, da un ganador único con dos intervalos de tamaño tres. `QED`

Para cualquier `epsilon>0`, (4.2) queda fuera de
`[epsilon n,(1-epsilon)n]` cuando `n>3/epsilon`. Así, ninguna implicación
determinista `S => M_h interior` puede probar `NC2B-O2`.

## 5. Reducción exacta de `NC2B-O2` a un problema de conteo

Sea

\[
\mathcal S_n=\{\pi\in\mathfrak S_n:S(\pi)\},
\]

y, para un lado `h` y `epsilon in (0,1/2)`,

\[
\mathcal I_{n,h}(\varepsilon)
=\{\pi\in\mathcal S_n:
\varepsilon n\le M_h(\pi)\le(1-\varepsilon)n\}.
\]

Como `Pi_n` es uniforme,

\[
\Pr\{\varepsilon n\le M_h\le(1-\varepsilon)n\mid S\}
=\frac{|\mathcal I_{n,h}(\varepsilon)|}{|\mathcal S_n|}.
\tag{5.1}
\]

Por tanto `NC2B-O2` exige una cota de conteo relativa, uniforme en la cola:

\[
|\mathcal I_{n,h}(\varepsilon)|\ge p|\mathcal S_n|.
\tag{5.2}
\]

Las construcciones de §§3–4 prueban que tanto el numerador como su complemento
son no vacíos, pero aportan solo una permutación a cada clase. En particular,
la cota `Pr(S)>=1/n!` de `O1` no implica ningún `p>0` en (5.2).

Tampoco basta una cota marginal sobre `Pr(S)`: incluso si se demostrase de nuevo
`-log Pr(S)=o(n)`, aún habría que controlar qué fracción de `S` tiene `M_h`
interior. El certificado EF-4/EF-7 degradado no contiene (5.2), y no puede
rehabilitarse como sustituto de esa obligación.

Una prueba de (5.2) necesitaría al menos uno de los siguientes objetos, ninguno de
los cuales está disponible en el registro vigente:

1. una inyección de multiplicidad uniformemente acotada desde las permutaciones
   únicas de borde hacia las únicas interiores;
2. una recurrencia o función generadora conjunta para `(|S_n|,M_h)`;
3. una cota de probabilidad para `S cap {M_h fuera de la ventana}` comparada con
   una cota inferior de la misma escala para `S`.

Los lemas de discrepancia uniforme existentes dan colas incondicionales para
rectángulos de rangos, pero dividirlas por `Pr(S)` vuelve a requerir un control de
la masa de selección y no produce por sí solo el cociente relativo (5.1).

En consecuencia, el ataque se detiene en `O2` con el hueco tipado por (5.2). No se
afirma que (5.2) sea falsa.

```text
NC2B_O2_INTERIOR_MASS = OPEN
NC2B_O2_EXACT_MISSING_OBJECT = RELATIVE_COUNT_I_N_H_OVER_S_N
NC2B_O2_DETERMINISTIC_ROUTE = REFUTED_BY_TAU_N_WITH_M_EQ_3
```

## 6. `NC2B-O3` no se abre por precedencia

El contrato ordena atacar la escala de la varianza total solo si `O2` pasa. Se
preserva la descomposición conocida

\[
\operatorname{Var}(\ell_h\mid n,h,S)
=\mathbb E[v_n(K_h,L_h)\mid n,h,S]
+\operatorname{Var}\{\mu_n(K_h,L_h)\mid n,h,S\}.
\]

El primer término está acotado por `1/n`; el segundo, entre formas seleccionadas,
no tiene una cota `O(1/n)` en el repositorio. No se promueve ningún resultado
auxiliar sobre `O3` en esta ejecución.

## 7. Techo de afirmación

Queda demostrado exclusivamente que el condicionamiento existe para todo `n>=6`.
No queda demostrado:

- masa no evanescente de `M_h` en una ventana interior;
- `Var(ell_h|n,h,S)=O(1/n)`;
- la hipótesis conjunta `C_h` de `NC-1`;
- `liminf T_n^h>0`;
- ningún resultado para canales enriquecidos, poset completo, horizonte, escala
  absoluta o `d>=3`.

No se usaron datos sellados, simulaciones, barridos ni código nuevo.

## 8. Terminal

`NC2B-O1` está probado, `O2` queda abierto en el cociente de conteos (5.1) y `O3`
no se abre por precedencia. El terminal único es:

```text
NC2B_TERMINAL = NC2B_PARTIAL_EVENTUAL_SELECTION_ONLY
NC2B_EVENTUAL_SELECTION = PROVED_FOR_ALL_N_GE_6
NC2B_SELECTION_PROBABILITY_LOWER_BOUND = 1/n!
NC2B_INTERIOR_MASS = OPEN_RELATIVE_COUNTING_PROBLEM
NC2B_TOTAL_VARIANCE_SCALE = NOT_OPENED_BY_PRECEDENCE
NC2B_SELECTED_LAW_PACKAGE = NOT_PROVED
NC2B_LIMINF_T_N = NOT_PROVED
NC2B_NEW_DATA = NO
NC2B_NEW_CODE = NO
```
