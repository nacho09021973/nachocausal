# Relatividad — Programa A / Gate M

**Estado:** EXPLORATORIO — GATE M ONLY  
**Rama:** `relatividad`  
**Objeto actual:** validar un estimador intrínseco de posición respecto de la frontera causal.  
**No autorizado por este documento:** claims de universalidad, emergencia de Lorentz, emergencia de `c`, Gate S, Gate U o Programa B.

---

## 1. Separación de programas

Este frente distingue dos programas conceptualmente diferentes y no los mezcla.

### Programa A — universalidad de saturación del cono causal

Se parte de un causal set

\[
\mathcal C=(C,\prec)
\]

con `\prec` fundamental. La dinámica no genera el orden: solo determina qué parte del futuro causal permitido recibe respuesta efectiva.

La pregunta fuerte de este programa, todavía **no abierta**, sería si una clase amplia de dinámicas intrínsecas y no calibradas campo por campo satura universalmente la frontera causal en el régimen macroscópico.

### Programa B — emergencia del propio orden causal

No se introduce `\prec` como primitivo; se intentaría derivarlo posteriormente a partir de una estructura de respuesta.

Este programa queda **fuera de alcance y bloqueado**. Ningún resultado de Gate M o Gate S del Programa A autoriza lenguaje de emergencia del propio orden causal.

---

## 2. Jerarquía de gates

### Gate M — método

Pregunta única:

> ¿Existe un estimador intrínseco que, sobre causal sets manifoldlike, distinga de forma estable la piel causal del interior timelike sin consultar la métrica ni las coordenadas del embedding?

Resultado máximo permitido tras un PASS:

> El estimador discrimina borde causal e interior causal en causal sets manifoldlike.

Nada más.

### Gate S — saturación

**BLOQUEADO hasta PASS de Gate M.**

Requeriría una clase `\mathcal D` de dinámicas genuinas, retardadas, intrínsecas y no seleccionadas por recuperar `\Box`, para estudiar si

\[
\lim_{L\to\infty}\Delta_\lambda(L)=0
\qquad \forall\lambda\in\mathcal D,
\]

con control de fluctuaciones, simetría izquierda/derecha en `1+1` y al menos dos tipos de excitación.

### Gate U — universalidad / cuenca

**BLOQUEADO hasta PASS de Gate S.**

Requeriría una familia parametrizada de dinámicas y una transformación de coarse-graining intrínseca

\[
\mathcal R:\mathcal D\to\mathcal D
\]

que no use `\Delta`, el embedding ni la proximidad al cono como criterio de bloqueo. Solo entonces tendría sentido hablar de cuenca o atractor.

---

## 3. Regla de no circularidad

El primer experimento es una **calibración falsable del instrumento**, no una prueba embrionaria de universalidad.

Dos advertencias quedan congeladas:

\[
\text{“el instrumento ve el borde de }\prec\text{”}
\not\Rightarrow
\text{“el borde es emergente”.}
\]

\[
\text{“vemos un frente cercano al borde causal”}
\not\Rightarrow
\text{“hemos explicado }c\text{”.}
\]

El valor numérico de `c` en unidades macroscópicas no es el objeto de este programa. Como máximo, fases posteriores podrían estudiar la **unicidad y saturación de una estructura nula común**.

---

## 4. Alcance exacto de Gate M

Se usa:

- el mismo sprinkling para todos los kernels;
- la misma fuente `x=\gamma_0`;
- la misma cadena-observador `\gamma`;
- coordenadas radar construidas solo a partir de `(C,\prec)` y de `\gamma`;
- el embedding únicamente para generar el poset y para figuras de control no utilizadas por el observable.

Queda prohibido durante Gate M:

- Sorkin / Benincasa–Dowker;
- el d’Alembertiano local de Boguñá–Krioukov;
- ajustar coeficientes para reproducir `\Box` o clavar el cono;
- declarar llegada por `\chi\neq0`;
- elegir ventanas, umbrales o escalas después de inspeccionar el observable final;
- interpretar un resultado de Gate M como evidencia de Gate S o Gate U.

---

## 5. Coordenadas radar intrínsecas

Para un elemento `y`, se identifican sobre la cadena-observador

\[
\gamma_-(y)=\max\{z\in\gamma:z\prec y\},
\]

\[
\gamma_+(y)=\min\{z\in\gamma:y\prec z\}.
\]

A partir de una distancia temporal intrínseca sobre `\gamma`, denotada `\tau_C`, se construyen

\[
t_C(y)=\frac{
\tau_C(\gamma_0,\gamma_+(y))+
\tau_C(\gamma_0,\gamma_-(y))}{2},
\]

\[
r_C(y)=\frac{
\tau_C(\gamma_-(y),\gamma_+(y))}{2}.
\]

La implementación concreta de `\tau_C` debe quedar fijada en el código/protocolo antes del run confirmatorio de Gate M y no puede usar coordenadas del embedding.

---

## 6. Frontera causal estimada

Para cada celda intrínseca `(t,r)`, se define

\[
F_{\rm caus}(t,r)
=
\frac{\#\{y\in S_{t,r}:x\prec y\}}
{\#S_{t,r}}.
\]

El nivel primario queda fijado en

\[
q=0.5.
\]

El tiempo de llegada causal es

\[
T_{\rm caus}(r)
=
\inf\{t:F_{\rm caus}(t,r)\ge 0.5\}.
\]

No se optimiza `q` después de ver resultados.

---

## 7. Kernels de validación

Estos objetos son **kernels de respuesta para validar el estimador**, no microdinámicas físicas completas ni funciones de Green derivadas de una ecuación de movimiento.

### `\lambda_1` — kernel de Hasse

\[
\chi_1(y,x)
=
\exp[-d_H(x,y)/d_*]
\qquad (x\prec y).
\]

`d_H` es la distancia en el diagrama de recubrimiento. El kernel está diseñado como caso de respuesta próxima al borde causal.

La regla que fija `d_*` debe congelarse antes del barrido en `N`. Si se usa un cuantil de la muestra, el cuantil `p_H` debe quedar preregistrado y la sucesión debe nombrarse explícitamente como `\lambda_1(N;p_H)`.

### `\lambda_2` — kernel de volumen de intervalo

Con intervalo abierto

\[
n^\circ(x,y)
=
\left|\{z:x\prec z\prec y\}\right|,
\]

se usa

\[
\chi_2(y,x)
=
\frac{n^\circ(x,y)}{n^\circ(x,y)+n_*}.
\]

Este kernel debe actuar como control de interior timelike: cerca del borde causal los intervalos son flacos; más al interior, `\chi_2` crece.

`n_*` no puede elegirse libremente en cada `N`. La ley de escala debe quedar congelada antes del run principal. Una opción admisible es fijarlo respecto de un intervalo de referencia intrínseco,

\[
n_*=\alpha_V N_{\rm ref},
\]

con `\alpha_V` preregistrado y `N_ref` definido solo mediante el poset y la cadena-observador. Si la implementación existente usa otra regla, debe documentarse y congelarse antes de ejecutar Gate M.

### `\lambda_-` — control difusivo

Control negativo basado en una construcción difusiva intrínseca que utilice `d_H` y una noción de altura `h` derivada de cadenas.

La fórmula exacta y sus parámetros deben estar fijados en el código/protocolo antes del run principal. Si no lo están, **Gate M permanece bloqueado**: no se improvisan después de inspeccionar `\lambda_1` o `\lambda_2`.

---

## 8. De respuesta a tiempo de llegada

En cada celda `(t,r)` se agrega la amplitud mediante mediana:

\[
A_\lambda(t,r)
=
\operatorname{median}_{y\in S_{t,r}}
|\chi_\lambda(y,x)|.
\]

Se normaliza por radio:

\[
\widehat A_\lambda(t,r)
=
\frac{A_\lambda(t,r)}{\max_{t'}A_\lambda(t',r)}.
\]

Los umbrales quedan fijados en

\[
\theta\in\{0.3,0.5,0.7\}.
\]

El tiempo de llegada dinámica es

\[
T_{\rm dyn}^{\lambda,\theta}(r)
=
\inf\left\{t:\widehat A_\lambda(t,r)\ge\theta\right\}.
\]

No se usa `\chi\neq0` como criterio de llegada.

---

## 9. Observable primario: profundidad causal excedente

El observable primario de Gate M no es una velocidad ni una pendiente.

En cada celda causalmente accesible se calcula

\[
M(t,r)
=
\operatorname{median}_{y\in S_{t,r},\,x\prec y}
 n^\circ(x,y).
\]

Después,

\[
M_{\rm caus}(r)
=
M(T_{\rm caus}(r),r),
\]

\[
M_{\lambda,\theta}(r)
=
M(T_{\rm dyn}^{\lambda,\theta}(r),r).
\]

En dimensión `d`, se define

\[
\Delta_{\lambda,\theta}(r)
=
[M_{\lambda,\theta}(r)+1]^{1/d}
-
[M_{\rm caus}(r)+1]^{1/d}.
\]

Para el run actual en `1+1`, `d=2`:

\[
\boxed{
\Delta_{\lambda,\theta}(r)
=
\sqrt{M_{\lambda,\theta}(r)+1}
-
\sqrt{M_{\rm caus}(r)+1}
}.
\]

Interpretación operacional de Gate M:

- `\Delta\approx0`: llegada próxima a la piel causal estimada;
- `\Delta>0`: llegada en el interior timelike;
- valores persistentemente incompatibles con la causalidad estimada obligan a auditar binning/reconstrucción antes de cualquier interpretación física.

---

## 10. Diagnósticos secundarios

Se conserva el retraso

\[
u_{\lambda,\theta}(r)
=
T_{\rm dyn}^{\lambda,\theta}(r)-T_{\rm caus}(r),
\]

pero **no se usa como observable primario**, porque una superficie timelike

\[
T(r)=\sqrt{r^2+a^2}
\]

satisface

\[
T(r)-r\to0
\]

cuando `r\to\infty` sin convertirse por ello en una superficie nula.

La antigua razón de pendientes `\eta` queda, como máximo, como diagnóstico histórico. No autoriza claims de velocidad porque superficies timelike asintóticas al cono pueden producir `\eta\to1` geométricamente.

---

## 11. Ventanas y agregación

Las ventanas radiales deben fijarse por percentiles de `r_C` **antes de calcular pendientes o inspeccionar diferencias entre kernels**.

Para cada ventana de escala `L`, se registra

\[
\bar\Delta_{\lambda,\theta}(L)
=
\operatorname{median}_{r\in W_L}
\Delta_{\lambda,\theta}(r),
\]

junto con dispersión entre sprinklings.

El protocolo debe conservar resultados por realización. Un efecto que exista solo después de promediar sprinklings no demuestra que el instrumento funcione en una realización típica.

En `1+1`, además se debe controlar la simetría izquierda/derecha cuando la reconstrucción permita separar ambas orientaciones:

\[
\Delta_\lambda^{(+)}(L)-\Delta_\lambda^{(-)}(L)
\to0
\]

dentro de las fluctuaciones esperables. Una asimetría persistente invalida la interpretación de un frente isotrópico.

---

## 12. Escala de la primera batería

El prototipo `N=2200` se considera **andamio diagnóstico**, no evidencia de Gate M.

El run principal de validación deberá usar, como objetivo inicial:

- `N\sim10^4` por sprinkling;
- aproximadamente `20` sprinklings independientes;
- mismas reglas preregistradas para celdas, ventanas, `q`, `\theta`, `d_*`, `n_*` y control difusivo.

Estas cifras son objetivo de validación inicial, no garantía automática de potencia suficiente. Si la resolución sigue siendo insuficiente, el resultado correcto es `INCONCLUSIVE`, no reajustar el observable mirando las respuestas.

---

## 13. Gate M — criterios de decisión

### PASS

Gate M puede declararse `PASS` solo si, a resolución suficiente, se obtiene de forma estable:

\[
\bar\Delta_1
<
\bar\Delta_2,
\qquad
\bar\Delta_1
<
\bar\Delta_-,
\]

con:

- separación reproducible entre sprinklings;
- estabilidad cualitativa para `\theta=0.3,0.5,0.7`;
- ausencia de dependencia violenta del binning;
- control razonable de simetría izquierda/derecha en `1+1`;
- sin consultar el embedding para decidir el resultado.

Claim máximo autorizado tras PASS:

> El estimador intrínseco distingue una respuesta próxima a la frontera causal de respuestas situadas más profundamente en el interior causal en causal sets manifoldlike `1+1` bajo esta batería de validación.

### FAIL

Gate M es `FAIL` si ocurre de forma robusta cualquiera de los siguientes:

- volumen o difusión colapsan sobre Hasse en `\Delta`;
- la ordenación cambia cualitativamente entre los umbrales preregistrados;
- el estimador no separa borde e interior con mayor resolución;
- la simetría izquierda/derecha falla persistentemente sin explicación de muestreo;
- la conclusión depende de usar información del embedding.

### INCONCLUSIVE

Se usa `INCONCLUSIVE` cuando el muestreo, ocupación de celdas o fluctuaciones no permiten decidir sin cambiar el protocolo.

No se transforma un `INCONCLUSIVE` en `PASS` retocando a posteriori ventanas, umbrales o escalas.

---

## 14. Criterios de parada del programa

Durante Gate M se deja de escalar la batería y se vuelve a diseño si:

1. el estimador no distingue de forma estable Hasse de los controles de interior;
2. `\Delta(\theta)` depende violentamente de `\theta\in[0.3,0.7]`;
3. la reconstrucción intrínseca produce falsos adelantamientos sistemáticos que no desaparecen al aumentar resolución;
4. la separación solo existe en el promedio y no en realizaciones típicas;
5. cualquier parte necesaria del protocolo termina usando la métrica o coordenadas ocultas del embedding para decidir.

Gate S y Gate U permanecen bloqueados aunque Gate M pase. Se requiere una decisión científica separada antes de abrirlos.

---

## 15. Pruebas adversariales reservadas para Gate S

Si Gate M pasa, la fase siguiente no empieza intentando confirmar saturación. Empieza intentando destruirla.

Antes de hablar de universalidad deben buscarse dinámicas intrínsecas admisibles que produzcan deliberadamente:

- un frente persistentemente subcausal;
- diferencias entre especies;
- asimetría izquierda/derecha en `1+1` o anisotropía en dimensiones superiores;
- dependencia de escala/energía que no tienda a una única característica.

Si esos contraejemplos son fáciles y estables dentro de la clase admisible, no existe evidencia de una cuenca universal.

Si resultan imposibles bajo restricciones independientes y bien motivadas, el objeto interesante sería un posible **resultado de rigidez causal**, no una simulación particular con `\eta\to1`.

---

## 16. Disciplina de claims

Estado actual del programa:

\[
\boxed{\text{PROGRAMA A / GATE M — EXPLORATORY METHOD VALIDATION}}
\]

No usar en informes, commits o discusión externa expresiones como:

- “hemos explicado `c`”;
- “`c` emerge”;
- “la invariancia de Lorentz emerge”;
- “el cono causal emerge”;
- “hemos demostrado universalidad”.

Antes de Gate U, la formulación fuerte máxima que podría llegar a ser evaluada en Programa A es:

\[
\boxed{
\text{un único cono de respuesta puede ser un fenómeno de saturación colectiva,}
\text{ no una propiedad independiente de cada campo.}
}
\]

Hoy esa frase es una **hipótesis de trabajo**, no un resultado.
