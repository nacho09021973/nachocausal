# Auditoría de aplicabilidad: Deuschel–Zeitouni (1995) al Corolario 4

STATUS: AUDITORIA_BIBLIOGRAFICA / NOTAS_DE_EXPLORACION / NO_ES_PREREGISTRO / NO_SELLA_NADA
DATE: 2026-09-08
CAPA: dev/. No toca `nachocausal/`, contratos, seal ni `manuscrito/`.

Audita si el teorema externo invocado por el Corolario 4 de
`dev/PAPER2_DOUBLE_NULL_REDUCTION.md` cubre de hecho el caso que necesitamos.

**Resumen en una frase: no lo cubre directamente en ningún bloque.** El artículo
está enunciado para el **cuadrado unidad** con densidad **acotada inferiormente**
y para **`n` puntos i.i.d.**, no para un proceso de Poisson. Las tres cosas nos
afectan.

**Actualización E2 (2026-09-08).** El emparedado por área pequeña no basta:
el funcional del orden inducido permite puentes de peso cero fuera del soporte.
La [nota E2](PAPER2_E2_RECTANGULAR_APPROXIMATION.md) contiene una demostración
propuesta para la caja compacta en cada bloque, con aproximaciones explícitas,
control de las curvas en cada frontera y justificación del límite para pesos
constantes por rectángulos. Sigue pendiente la revisión independiente. Las
calificaciones de extensiones pendientes de este informe describen la auditoría
del artículo; la nota nueva aporta argumentos propios, no nuevas atribuciones
a DZ. Se retira la recomendación de sustituir ahora la caja por un diamante.

---

## 0. Procedencia y licencia

```text
Título     : Limiting Curves for I.I.D. Records
Autores    : Jean-Dominique Deuschel (ETH-Zentrum), Ofer Zeitouni (Technion)
Revista    : The Annals of Probability, 1995, Vol. 23, No. 2, 852-878
DOI        : 10.1214/aop/1176988293
Editor     : Institute of Mathematical Statistics
Acceso     : OPEN ACCESS en Project Euclid (verificado 2026-09-08)
Recibido   : noviembre 1993; revisado mayo 1994
AMS 1991   : Primary 60G70; secondary 60F10
PDF sha256 : 5b4622c2c99c237c07843ac6fb42eeca47cfe97c21d86a904bba5e457d3bd9bf
PDF bytes  : 1985581      PDF páginas: 27   (página PDF N  <->  página revista 851+N)
```

Artefactos añadidos (**ambos en `biblioteca/`, que está git-ignored en
`.gitignore:24`; por tanto NO entran en el commit y no se redistribuyen**):

- `biblioteca/Deuschel_Zeitouni_1995_AnnProb_23_852_Limiting_Curves_for_IID_Records.pdf`
- `biblioteca/derived-md/Deuschel_Zeitouni_1995_AnnProb_23_852_Limiting_Curves_for_IID_Records.md`

**Desviación de convención, declarada.** El resto de `derived-md/` se generó con
`marker`/`pypdfium2` y **OCR desactivado**, porque esos PDFs traen capa de texto.
Éste es un **escaneo de 1995 sin capa de texto**, así que hubo que usar OCR
(`ocrmypdf --force-ocr`, tesseract). La notación matemática del markdown derivado
está degradada y **no es citable**. Todas las fórmulas de este informe se leyeron
**de las imágenes de página del PDF**, no del OCR. `FULL_LIBRARY_CONVERSION_REPORT.md`
no se ha tocado: es un informe generado y añadirle una fila a mano lo falsearía.

---

## 1. Auditoría, punto por punto

### 1. Teorema de primer orden para la longitud máxima

**Teorema 2(i), p. 855, ec. (8).** Bajo (A1) y (A2):

```text
lim_{n->inf}  ell_max(n) / sqrt(n)  =  2 J_bar,
```

*el límite es en probabilidad.* `ell_max(n)` es la longitud de la subsucesión
creciente más larga de la muestra i.i.d. (p. 852, §1).

Contexto (p. 853): para el caso uniforme esto se reduce a Vershik–Kerov,
`ell_max(n)/sqrt(n) -> 2`. Extensión a `[0,1]^d` (Remark 2, p. 855):
`ell_max/n^{1/d} -> c_d J_bar`, con `c_d` **desconocido** — «an open and
challenging problem to compute `c_d`». Confirma independientemente por qué en
`d=2` estamos en el único caso con constante cerrada.

### 2. Clase precisa de dominios admitidos

**El cuadrado unidad `[0,1]^2`, y nada más.** (p. 852, §1: la ley `P(x,y)` está
«on `[0,1]^2`»). El espacio de curvas es

```text
B' = { phi: [0,1] -> [0,1] no decreciente, continua por la derecha }   (p. 854)
```

y los maximizadores resultan ir **de esquina a esquina**: `phi(0)=0`, `phi(1)=1`
(condiciones de contorno de la EDO (6), p. 854).

Única relajación disponible (**Remark 1, p. 863**): una **partición finita del
cuadrado en rectángulos** `S_ij = [a_i,a_{i+1}) x [b_j,b_{j+1})`, con

```text
(A2').  p es C_b^1 y acotada inferiormente EN CADA S_ij.
```

No hay ninguna clase de dominios curvos, ni regiones generales, ni soportes no
rectangulares en el artículo.

### 3. Hipótesis sobre la densidad

Textual, p. 853:

```text
(A1).  P(x,y) posee una densidad ACOTADA p(x,y) respecto de Lebesgue en [0,1]^2.
(A2).  p(x,y) es C_b^1 y ACOTADA INFERIORMENTE en [0,1]^2.
(A3).  K(J) es un conjunto finito {phi_1,...,phi_k}.
```

- continuidad / C1: **sí, `C_b^1`** (derivadas primeras continuas y acotadas);
- positividad estricta: **sí**, «bounded below» es exactamente eso;
- cota superior: **sí**, (A1);
- cota inferior: **sí**, (A2);
- normalización: `p` es una **densidad de probabilidad** (`∫ p = 1`), porque los
  `n` puntos son i.i.d. de ley `P`.

Hay además una **(A4)** (p. 860): separación uniforme de los maximizadores —
para todo `δ>0` existe `ε(δ)>0` tal que toda `phi` lineal a trozos no decreciente
con `||phi - phi_l|| > δ` para todo `l` cumple `J(phi) < J_bar - ε(δ)`. No es una
carga adicional: **Corolario 1, p. 869, prueba que (A1)–(A3) implican (A4)**.

`K(J)` es no vacío y compacto en `C_b^1` bajo (A1)–(A2) (**Remark 1, p. 854**);
los autores *creen* que (A3) se sigue de (A1)–(A2) pero **declaran que no saben
demostrarlo** («we do not know how to prove it», p. 854).

### 4. Modo de convergencia

**En probabilidad** (p. 855, texto bajo la ec. (8): «where the limit is in
probability»). No hay convergencia casi segura, ni tasa, ni cota no asintótica.
El artículo es de grandes desviaciones (secondary 60F10) pero el enunciado que
necesitamos es una ley débil.

### 5. Definición exacta del funcional variacional

**Ec. (3), p. 854:**

```text
J(phi) = ∫_0^1 sqrt( phi_dot(x) · p(x, phi(x)) ) dx,        phi ∈ B'
J_bar  = sup_{phi ∈ B'} J(phi)                                    (ec. (4))
```

Sólo cuenta la parte absolutamente continua: `phi(t) = ∫_0^t phi_dot + phi_s(t)`
con `phi_s` singular y derivada nula c.t.p. (p. 854).

**Forma paramétrica simétrica, Remark 3, p. 863** — ésta es la que usamos:

```text
J(psi) = ∫_0^1 ( p(psi(t)) · psi_dot_1(t) · psi_dot_2(t) )^{1/2} dt
```

**Teorema 3, p. 864:** bajo (A1)–(A2) el problema (23) tiene solución en `B'`.

### 6. ¿`n` i.i.d. o proceso de Poisson?

**`n` i.i.d.**, sin ambigüedad. p. 852, §1: «Let `z_α = (x_α,y_α)`, `α=1,...,n`,
be **n i.i.d.**, `R^2`-valued random variables». La demostración del Teorema 2
(§5, pp. 873-877) usa un argumento de acoplamiento con Vershik–Kerov sobre la
permutación de rangos, que es intrínsecamente de tamaño fijo.

### 7. ¿La poissonización se obtiene directamente o requiere un lema?

**Requiere un lema, y el artículo no lo contiene.** La palabra «Poisson» tiene
**cero apariciones** en el texto completo (`grep -i poisson` sobre el OCR de las
27 páginas: 0 hits). No hay proceso puntual en ninguna parte del artículo.

El lema que falta es elemental pero hay que escribirlo: `ell_max` es monótona
bajo adición de puntos; condicionado a `N=n` un Poisson da `n` i.i.d. con la
intensidad normalizada; `N/λ -> 1` en probabilidad; luego un emparedado monótono
entre tamaños `(1∓ε)λ` transfiere el límite. **Elemental, no citable.**

### 8. Casos que nos importan

| Caso | ¿Cubierto? | Referencia |
|---|---|---|
| Soportes **no rectangulares** | **NO.** El dominio es `[0,1]^2`; la única relajación es una partición **en rectángulos** | p. 852; Remark 1, p. 863 |
| Densidades que **se anulan** | **PARCIALMENTE, y no como la nuestra.** Remark 2, p. 863 admite `(A2'')`: en cada cuadrado `S_ij`, `p` es o bien `C_b^1` y acotada inferiormente, **o bien idénticamente 0**; hay que restringir el problema variacional a `S+`, los cuadrados con `p>0`. Es una anulación **por bloques, con salto**, no una densidad que **tiende a cero continuamente** como la nuestra en el horizonte | Remark 2, p. 863 |
| **Fronteras internas** | **PARCIALMENTE.** `(A2')`/`(A2'')` permiten discontinuidades sobre las líneas de una rejilla rectangular; bajo ellas dos soluciones distintas pueden intersecarse dentro de `[0,1]^2` o compartir un segmento (ejemplo del tablero de ajedrez, §4) | Remarks 1-2, p. 863 |
| **Regiones causales truncadas** | **NO.** No aparecen en el artículo | — |
| **Extremo del máximo en el borde** (extremo libre) | **NO.** El problema es de **esquina a esquina**: `phi(0)=0`, `phi(1)=1`. Nuestro `tau_max(x) = sup_{y ∈ F_x} d(x,y)` es un supremo con **extremo libre** sobre la frontera de truncación. Para un rectángulo coinciden (con `p>0` siempre conviene ir a la esquina lejana); para una región general, no | p. 854, contorno de (6) |

**Hallazgo que debilita todo lo anterior.** Los Remarks 1 y 2 (p. 863) están
escritos como relajaciones **del Teorema 1** — «an inspection of the proof
reveals that one could replace (A2) by…», y van inmediatamente después de
`PROOF OF THEOREM 1`. El **Teorema 2(i)**, que es el que necesitamos, se enuncia
bajo **(A1) y (A2)** sin relajar, y su demostración (§5) pasa por el Lema 7
(p. 874), que asume `(1-δ) < p(x,y) < (1+δ)`, y por los Lemas 8-9, que trocean la
curva en rectángulos y controlan cocientes `p(x,y)/p(iΔx,Y_i) ≤ 1+δ'`. Ese
control de **cocientes** es exactamente lo que revienta donde `p -> 0`.

A favor del traslado: los autores dicen que «the proof of both parts of Theorem 2
follows from Lemmas 8 and 9 **in exactly the same way** that Theorem 1 followed
from Lemmas 1 and 4» (p. 877). El paralelo estructural es explícito. Pero
**el artículo no afirma que (A2')/(A2'') basten para el Teorema 2(i)**, y
nosotros no podemos citarlo como si lo hiciera.

### 9. ¿Hay localización/concentración de las curvas maximizantes?

**Sí, es el resultado principal del artículo.**

- **Teorema 1, p. 854, ec. (5):** bajo (A1)–(A3), condicionado a que la muestra
  forme un *record*, todos los puntos se concentran a distancia `< δ` de alguna
  `phi_l ∈ K(J)`, con probabilidad `-> 1`.
- **Teorema 2(ii), p. 855, ec. (9):** bajo (A1)–(A3), **toda** subsucesión
  creciente de longitud máxima se concentra a distancia `< δ` de alguna
  `phi_j ∈ K(J)`, con probabilidad `-> 1`.
- Versión reforzada (Remark 4, p. 864, ec. (22)) con la función constante a
  trozos `g` que reordena la muestra.

Precio: **la localización necesita (A3)**, la hipótesis que los propios autores
no saben demostrar. Sin (A3) queda sólo la ley de primer orden, Teorema 2(i).

Esto es exactamente lo que haría falta para pasar de «`L` mide `tau_max`» a
«la cadena máxima *traza* la geodésica». No es gratis.

---

## 2. Punto 10 — verificación algebraica de `2 J_bar = sqrt(2) tau_D`

### 2.1 Normalizaciones exactas del repositorio

De `dev/PAPER2_DOUBLE_NULL_REDUCTION.md`, Teorema 2, dentro de un bloque:

```text
ds^2      = |f| dv dw,                f = 1 - r_S/r
dt* dr    = (|f|/2) dv dw             (jacobiano, |J| = 2/|f|)
intensidad respecto de dvol = dt* dr  :  rho          (constante; det g = -1)
intensidad respecto de dv dw          :  mu = rho·|f|/2
```

### 2.2 Paso de la forma DZ (densidad de probabilidad, `n` fijo) a la forma de intensidad

DZ: `ell_max ≈ 2 sqrt(n) J_bar_DZ` con `J_bar_DZ = sup ∫ (p psi_1' psi_2')^{1/2} dt`
y `p` **densidad de probabilidad**. Con `n = ∫_D mu dv dw` y `p = mu/n`:

```text
2 sqrt(n) J_bar_DZ = 2 sup ∫ ( n·p · psi_1' psi_2' )^{1/2} dt
                   = 2 sup ∫ ( mu   · psi_1' psi_2' )^{1/2} dt  =:  2 J_bar
```

Es decir, `J_bar := sqrt(n) J_bar_DZ` es la misma funcional escrita con la
**intensidad** en lugar de la densidad normalizada. (El cambio de variables afín
al cuadrado unidad se cancela: si `v = a s_1 + v_0`, `w = b s_2 + w_0`, entonces
`p = mu·ab/n` y `psi_i' -> a psi_1'`, `b psi_2'`, y los factores `a b` se
compensan dentro de la raíz.)

### 2.3 La identidad

Sustituyendo `mu = rho·|f|/2`:

```text
2 J_bar = 2 sup ∫ ( (rho|f|/2) psi_1' psi_2' )^{1/2} dt
        = 2 sqrt(rho/2) · sup ∫ ( |f| psi_1' psi_2' )^{1/2} dt
        = sqrt(2 rho)   · sup ∫ dtau                    [ds^2 = |f| dv dw]
        = sqrt(2 rho)   · tau_D
```

y en particular, **con la normalización `rho = 1`**:

```text
  2 J_bar = sqrt(2) · tau_D                                      VERIFICADO
```

`tau_D := sup_{gamma} ∫ dtau` sobre curvas causales futuras dentro de `D` = la
distancia lorentziana máxima alcanzable. La identidad es exacta y sale de dos
factores: `sqrt(1/2)` del jacobiano y el factor conforme `|f|` que convierte
`(|f| psi_1' psi_2')^{1/2} dt` en `dtau`.

### 2.4 Contraste con Vershik–Kerov (cierre del bucle)

Intervalo de Alexandrov plano de tiempo propio `tau`: en `(u,v)` es el cuadrado
`[0,tau]^2`, `vol = tau^2/2`, `n = rho tau^2/2`, `p ≡ 1` tras reescalar al
cuadrado unidad, y el óptimo es la diagonal, `J_bar_DZ = 1`. Entonces
`ell_max -> 2 sqrt(n) = tau sqrt(2 rho)`. La ruta del repositorio da
`L -> sqrt(2 rho) tau_max = sqrt(2 rho) tau`. **Idénticas**, y `m_2 = 2` se
recupera. Las dos normalizaciones son consistentes.

---

## 3. Veredicto por bloque

### A. Bloque exterior (`r > r_S`)

```text
DEUSCHEL_ZEITOUNI_APPLIES = AFTER_ELEMENTARY_EXTENSION
CONDICION: clausura(F_x) contenida en {r >= r_S + eps}, eps > 0
SIN ESA CONDICION: NOT_ESTABLISHED
```

*Qué sí encaja.* El orden es exactamente el componente a componente en `(v,U)`
(Teorema 1 del documento anterior). La densidad `mu = rho f(r)/2` con
`r = psi^{-1}(v-U)` es suave (`psi' = 2r/(r-r_S) != 0` fuera del horizonte),
acotada superiormente por `rho/2`, y **acotada inferiormente por
`rho f(r_S+eps)/2 > 0`** en cualquier compacto alejado del horizonte. `C_b^1` y
acotada por ambos lados: (A1) y (A2) se cumplen.

*Qué falta.* Cuatro extensiones, ninguna en el artículo:

| | Extensión | Dificultad |
|---|---|---|
| E1 | Poissonización (§1.7) | elemental: monotonía + emparedado |
| E2 | Dominio no rectangular. `F_x = J^+(x) ∩ D` es un cuadrante intersecado con la caja; en `(v,U)` la caja **no es un rectángulo** (`r = const` es una recta a 45°, `t* = const` tampoco es paralela a los ejes) | elemental *en esquema* — emparedado monótono entre uniones de rectángulos vía `(A2'')` — **pero exige un lema de continuidad de `J_bar` bajo refinamiento del dominio que DZ no demuestra** |
| E3 | Extremo libre en vez de esquina a esquina (§1.8) | elemental |
| E4 | Traslado de `(A2')`/`(A2'')` del Teorema 1 al Teorema 2(i) (§1.8, hallazgo) | inspección de demostración; los autores declaran el paralelo estructural (p. 877) pero no lo enuncian |

Si un árbitro rechaza que E2 sea elemental, **A degrada a `NOT_ESTABLISHED`**.

### B. Bloque interior (`0 < r < r_S`)

```text
DEUSCHEL_ZEITOUNI_APPLIES = AFTER_ELEMENTARY_EXTENSION
CONDICION: clausura(F_x) contenida en {eps_0 <= r <= r_S - eps}
SIN ESA CONDICION: NOT_ESTABLISHED
```

Mismo cuadro que A (E1–E4 idénticas), con **una hipótesis adicional que hay que
declarar**: en el interior `|f| = r_S/r - 1`, que **diverge cuando `r -> 0`**.
La densidad `mu = rho|f|/2` no es acotada cerca de la singularidad, y (A1) —
densidad acotada — fallaría. En la geometría congelada del repositorio no se
rompe **sólo porque la caja trunca en `r = 0.1`**: con `r_S = 0.5`,
`|f| <= 4` y `mu <= 2 rho`. Es decir, (A1) se sostiene aquí **por una elección
de caja, no por la física**. Eso debe quedar escrito en cualquier enunciado.

### C. Futuro que cruza el horizonte

**Actualización (2026-09-09).** Las objeciones que siguen describen la antigua
carta `(v,w)`, auditada aquí. La [nueva nota](PAPER2_HORIZON_THRESHOLD_LIMIT.md)
construye `(v,Z)`, regular y con orden producto también entre bloques; O4 no
impide tal representación. Incluye una prueba propuesta del límite por
recortes compactos y control de la banda del horizonte. Sigue sin ser una
aplicación directa de DZ al indicador de la caja; la revisión de la extensión
propia queda pendiente. Se conserva debajo el diagnóstico de la ruta original.

```text
DEUSCHEL_ZEITOUNI_APPLIES = NOT_ESTABLISHED
```

Cuatro razones independientes, cada una suficiente:

1. **No hay un único plano `(v,w)`** sobre el que plantear el problema: la
   lectura de `r` cambia de fórmula al cruzar y los rangos se solapan (O1). DZ
   necesita *un* dominio con *un* orden componente a componente.
2. **El dominio no sería acotado**: `R -> -inf` a ambos lados, el horizonte está
   en la frontera al infinito de la carta (O2). DZ trabaja en `[0,1]^2`.
3. **`mu -> 0` continuamente en el horizonte** (O3). `(A2'')` sólo admite que la
   densidad se anule **idénticamente sobre rectángulos enteros de una rejilla**,
   con salto — no una anulación continua sobre una curva interior. Y el
   mecanismo de la demostración del Teorema 2 (Lemas 7-9) controla **cocientes**
   de densidades, que divergen justo ahí.
4. **La relación cruzada la decide `v` sola** (O4): la estructura de dos
   coordenadas que DZ asume no existe a través del horizonte.

Conforme a la instrucción, no se intenta resolver este caso aquí.

---

## 4. Consecuencia para el Corolario 4 (corrección pendiente)

`dev/PAPER2_DOUBLE_NULL_REDUCTION.md`, Corolario 4 y §8, dice que la ley de
altura está «condicionada a **un único insumo externo**». **Esa frase es ahora
inexacta y debe corregirse**: son un insumo externo (DZ, Teorema 2(i)) **más
cuatro extensiones** E1–E4 que el artículo no contiene, y la validez es
condicional a que `F_x` esté a distancia positiva del horizonte (y, en el
interior, de `r = 0`).

No he aplicado la corrección porque la lista de artefactos de esta tarea es
explícita (PDF, markdown derivado, **un único** informe). Queda registrada aquí
como pendiente.

## 4.1 Referencia posterior: el diamante no sustituye la caja

En un problema distinto, E2 **desaparece** si el parche continuo
`D` se elige como un **intervalo de Alexandrov** del bloque en vez de una caja
coordenada: entonces `D` es un rectángulo en `(v,w)`, `F_x = J^+(x) ∩ D` es
también un rectángulo, y el reescalado al cuadrado unidad es afín. Quedarían
sólo las otras dependencias aplicables; el extremo libre es trivial en un
rectángulo porque la esquina lejana es el óptimo. Esto no resuelve E2 para la
caja y no es una propuesta de cambiar el dominio ni abrir otro contrato.
Primero debe revisarse la demostración de la nota E2. Además, un intervalo
curvo no satisface en general `A = tau^2/2`: la rectangularidad nula no elimina
la variación de la densidad conforme ni garantiza `R_2 -> 4`.

Esto coincide con lo que la propia literatura del repositorio ya había marcado:
el enunciado de EGS sobre cardinalidad-de-futuro está textualmente acotado a un
**causal diamond**, no a una caja (verificado por el asiento de verificación
bibliográfica en `docs/comite/comite_decision_021_rvar-egs-truncation-object.md`
§7). Es la misma frontera, encontrada por dos caminos.

---

## 5. Verificabilidad de las referencias

Las 9 referencias del artículo (p. 878) se transcribieron de la imagen de página:
Cesari (1983); Dembo & Zeitouni (1993); Ekeland (1990); Goldie & Resnick (1989),
*Ann. Probab.* **17** 678-699; Goldie & Resnick (1993); Ioffe & Tichomirov (1979);
Pollard (1984); Logan & Shepp (1977), *Adv. in Math.* **26** 206-222;
Vershik & Kerov (1977), *Dokl. Akad. Nauk* **233** 1024-1028.

**Advertencias, según lo pedido:**

1. **[5] Goldie & Resnick (1993), «Multivariate records and ordered random
   scattering», está listado como *Preprint*.** No he podido verificar si llegó a
   publicarse ni dónde. Es además la referencia que motiva todo el problema de
   *records* del artículo (p. 852). `[UNVERIFIED]`.
2. Las otras ocho son ítems publicados estándar, pero **sólo las he transcrito
   de la página; no he verificado cada una contra su fuente**. No las marco como
   verificadas.
3. La única que sí importa para nuestro uso es **[9] Vershik–Kerov (1977)**, de
   la que dependen el Lema 7 y toda la constante 2. Tampoco está en
   `biblioteca/`. `[UNVERIFIED]` como fuente primaria; su enunciado está,
   eso sí, citado dentro de DZ (pp. 853, 855, 873).
4. **Licencia/distribución:** el artículo es Open Access en Project Euclid, con
   copyright del Institute of Mathematical Statistics. El PDF se ha guardado en
   `biblioteca/`, que **está git-ignored**, de modo que este commit **no lo
   redistribuye**. Sólo se comitea este informe.
