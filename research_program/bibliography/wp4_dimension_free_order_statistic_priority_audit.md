# WP4 — auditoría de prioridad del teorema `dimension-free` por patrones de orden

> **STATUS: PRIORITY_AUDIT_COMPLETE / PRECURSOR_ONLY / STANDARD_COROLLARY /
> EXACT_SINGLE_SOURCE_NOT_LOCATED / NOVELTY_CERTIFIED=NO /
> NO_MANUSCRIPT_CHANGE / NO_CODE / NO_SIMULATION / NO_PR.**
>
> Auditoría bibliográfica específica de
> `wp4_dimension_free_order_statistic_separation.md`. La prueba interna permanece
> `INTERNAL_PROOF_AUDITED`. Este documento no reabre su validez matemática: fija
> únicamente el techo de prioridad que permiten las fuentes consultadas.

FECHA: 2026-07-30

RAMA: `agent/phase3-b2-decision-048`

HEAD auditado: `1359c0f4546553f6c89a2838bd9d6d89f5118b51`

## 1. Pregunta y veredicto

### Pregunta exacta

¿Existe un antecedente para la implicación
\[
Q_\theta^m\ne Q_{\theta'}^m
\quad\Longrightarrow\quad
\operatorname{TV}(Q_\theta^n,Q_{\theta'}^n)
\ge
\left[
1-2\exp\!\left(
-\frac{\lfloor n/m\rfloor\,
\operatorname{TV}(Q_\theta^m,Q_{\theta'}^m)^2}{2}
\right)
\right]_+
\longrightarrow1,
\]
donde \(Q_\theta^n\) y \(Q_{\theta'}^n\) son leyes de **posets no etiquetados**
inducidos por muestras `fixed_n`?

### Veredicto

```text
PRIORITY_GATE = PRECURSOR_ONLY
MATHEMATICAL_CLASSIFICATION = STANDARD_COROLLARY
EXACT_SINGLE_SOURCE_NOT_LOCATED = YES
NOVELTY_CERTIFIED = NO
```

No se localizó, en la búsqueda acotada descrita en §3, una fuente única que
enuncie la cota de TV con este mismo objeto cociente y estas constantes. Eso
**no** convierte el teorema en un resultado estadístico nuevo:

1. Hoeffding (1963), §4a, ecuaciones (4.4)–(4.7), da directamente la
   representación por bloques disjuntos y la cota
   \[
   \Pr\{U-\mathbb EU\ge t\}
   \le
   \exp\{-2\lfloor n/m\rfloor t^2\}
   \]
   para un U-estadístico con kernel indicador.
2. Janson (2011), en particular Ejemplo 1.5, Teoremas 1.7–1.8 y,
   con la numeración de `arXiv:0902.0306v1`, Teoremas 1.15–1.16, sitúa
   exactamente los posets inducidos por muestras
   i.i.d. dentro de los posets aleatorios intercambiables, identifica las leyes
   de las restricciones finitas con densidades de patrones inducidos y prueba
   convergencia casi segura al límite de poset correspondiente.
3. El test a punto medio y
   \(1-\operatorname{TV}\le\alpha+\beta\) son teoría elemental de tests
   bipuntuales.

Por tanto, la formulación de WP4 es una **especialización y empaquetado
explícito** de maquinaria estándar. Su valor legítimo es expositivo y de
transferencia al canal causal `fixed_n`; no se debe reclamar prioridad por el
teorema abstracto.

## 2. Descomposición del resultado auditado

| ID | Componente | Objeto |
|---|---|---|
| **DFO-A** | Consistencia proyectiva, equivarianza y restricciones disjuntas independientes | Poset aleatorio inducido por puntos i.i.d. |
| **DFO-B** | \(T_{n,m,A}\) es una densidad inducida y una función del poset no etiquetado | Cociente por isomorfismos |
| **DFO-C** | Concentración \(\exp\{-2\lfloor n/m\rfloor t^2\}\) | U-estadístico indicador acotado |
| **DFO-D** | Test a punto medio y cota inferior explícita de TV | Dos hipótesis simples |
| **DFO-E** | Cualquier diferencia en una ley finita implica TV \(\to1\) | Separación asintótica `fixed_n` |

Relaciones usadas en la matriz:

```text
SUBSUMES
DIRECT_PRECURSOR
TECHNICAL_BACKGROUND
ANALOGUE_OTHER_MODEL
NO_MATCH_AFTER_FULL_READ
```

## 3. Método y límites de la búsqueda

Se hizo una búsqueda dirigida por título, abstract y texto completo en la fuente
primaria accesible. Familias de consultas:

1. `"induced subposet" "total variation" random poset pattern density`
2. `"poset" "U-statistic" Hoeffding induced pattern`
3. `"exchangeable random posets" hypothesis testing total variation`
4. `"finite pattern" "total variation" exchangeable relational structures`
5. `"total variation" "poset limits"`
6. `"subposet density" Hoeffding`

También se contrastaron las anclas locales
`phase2_novelty_and_item5.md`,
`identifiability_bibliography_matrix.md` y
`ficha_se_busca_tv_order_only.md`.

Límites vinculantes:

- no es una revisión sistemática ni una búsqueda exhaustiva de citas;
- no se consultaron MathSciNet, zbMATH, Scopus o Web of Science con acceso de
  suscripción;
- `EXACT_SINGLE_SOURCE_NOT_LOCATED` describe el resultado de esta búsqueda, no
  prueba ausencia en la literatura;
- la adjudicación no depende de esa ausencia: las fuentes directas ya bastan
  para clasificar el resultado como corolario estándar.

## 4. Fuentes primarias y subsunción

### 4.1 Hoeffding (1963): la cota y sus constantes

W. Hoeffding, “Probability Inequalities for Sums of Bounded Random
Variables”, *Journal of the American Statistical Association* **58** (1963),
13–30, DOI
[10.1080/01621459.1963.10500830](https://doi.org/10.1080/01621459.1963.10500830);
[copia primaria del informe](https://repository.lib.ncsu.edu/items/3f47dae6-2e27-4a2c-9935-54aa9390ffaf).

Lectura relevante: §4a, “One-sample U statistics”, ecuaciones (4.3)–(4.7),
páginas internas 16–17 del informe.

- (4.4) forma la media de \(k=\lfloor n/m\rfloor\) bloques disjuntos;
- (4.5) expresa el U-estadístico como promedio sobre permutaciones de esas
  medias;
- (4.7) da
  \[
  \Pr\{U-\mathbb EU\ge t\}
  \le
  \exp\{-2kt^2/(b-a)^2\}.
  \]

Para \(g\in\{0,1\}\), \(b-a=1\), lo que reproduce exactamente DFO-C.
La cola inferior se obtiene aplicando la misma cota a \(-g\).

**Relación:** `SUBSUMES DFO-C`; `TECHNICAL_BACKGROUND DFO-D`.

**No contiene:** posets, cociente no etiquetado ni una cota de TV entre las
leyes de dos modelos.

**Corrección documental detectada:** la referencia de
`wp4_dimension_free_order_statistic_separation.md` remite actualmente a §5.
La sección correcta para U-estadísticos es **§4a**. §5 trata muestreo sin
reemplazo. La prueba reproducida en la nota y sus constantes no cambian.

### 4.2 Janson (2011): el antecedente directo para posets

S. Janson, “Poset limits and exchangeable random posets”,
*Combinatorica* **31** (2011), 529–563, DOI
[10.1007/s00493-011-2591-x](https://doi.org/10.1007/s00493-011-2591-x);
[arXiv:0902.0306](https://arxiv.org/abs/0902.0306).

Puntos verificados en el texto completo de `arXiv:0902.0306v1` (la numeración
puede diferir en la versión editorial):

- pp. 1–2: definición de subposet inducido y de \(t_{\rm ind}(Q,P)\);
- Ejemplo 1.5, pp. 3–4: el kernel estricto
  \(W(x,y)=\mathbf 1\{x\prec y\}\) genera, salvo etiquetas, el orden inducido
  por puntos i.i.d.;
- Teorema 1.7(i): \(P(n,W)\to\Pi_W\) casi seguramente;
- ecuaciones (1.5) y (1.7): las densidades inducidas determinan expectativas y
  leyes de restricciones finitas;
- Teorema 1.15(ii), ecuación (1.12): correspondencia entre límites de poset y
  leyes extremas de posets intercambiables, con
  \(t_{\rm ind}(Q,\Pi)=\Pr(R|_A=Q)\);
- Teorema 1.16: extremalidad equivalente a factorización sobre conjuntos
  disjuntos, el análogo exacto de la independencia de bloques usada en WP4.

Para una clase no etiquetada \([Q]\) de tamaño \(m\),
\[
\frac{\#\{I:[P|_I]=[Q]\}}{\binom nm}
=
\frac{m!}{|\operatorname{Aut}(Q)|}\,t_{\rm ind}(Q,P).
\]
Por tanto, \(T_{n,m,A}\) es una combinación finita de las densidades inducidas
de Janson y es intrínsecamente no etiquetada.

Además, si una ley finita difiere, alguna de estas densidades difiere y los dos
límites de poset son distintos. La convergencia casi segura de Janson permite
separar dos vecindades disjuntas de esos límites; esto ya implica
cualitativamente errores \(\to0\) y, por tanto, TV \(\to1\). Janson no formula
ese corolario en lenguaje de TV ni proporciona aquí la tasa exponencial.

**Relación:** `SUBSUMES DFO-A`; `DIRECT_PRECURSOR DFO-B`;
`DIRECT_PRECURSOR DFO-E` en forma cualitativa.

**No contiene:** DFO-C ni la cota encuadrada de DFO-D.

### 4.3 Coregliano–Malliaris (2024): marco relacional general

L. N. Coregliano y M. Malliaris, “High-arity PAC learning via
exchangeability”, [arXiv:2402.14294](https://arxiv.org/abs/2402.14294).

El trabajo formula explícitamente el muestreo de subestructuras inducidas en
grafos, hipergrafos y lenguajes relacionales finitos como distribuciones
intercambiables, con localidad/independencia en soportes disjuntos. Confirma
que DFO-A pertenece a un marco moderno mucho más general que los posets.

**Relación:** `TECHNICAL_BACKGROUND DFO-A`; no es un antecedente exacto de
DFO-D–E.

### 4.4 Antecedentes de grafos

P. Diaconis y S. Janson, “Graph limits and exchangeable random graphs”,
[arXiv:0712.2749](https://arxiv.org/abs/0712.2749), y la literatura de
frecuencias y testing de grafos densos son el análogo histórico. El propio
Janson desarrolla la teoría de posets como extensión de ese marco.

**Relación:** `ANALOGUE_OTHER_MODEL`. No hace falta transferir el resultado
desde grafos porque Janson ya proporciona la fuente poset-específica.

## 5. Matriz de prioridad

| Fuente | DFO-A | DFO-B | DFO-C | DFO-D | DFO-E |
|---|---|---|---|---|---|
| Hoeffding 1963, §4a | — | — | `SUBSUMES` | `TECHNICAL_BACKGROUND` | — |
| Janson 2011 | `SUBSUMES` | `DIRECT_PRECURSOR` | — | — | `DIRECT_PRECURSOR` cualitativo |
| Coregliano–Malliaris 2024 | `TECHNICAL_BACKGROUND` | — | — | — | — |
| Diaconis–Janson 2008 | `ANALOGUE_OTHER_MODEL` | `ANALOGUE_OTHER_MODEL` | — | — | `ANALOGUE_OTHER_MODEL` |

No se identificó una fuente que por sí sola subsuma DFO-A–E. Sí existe una
cadena corta de resultados directos que vuelve rutinaria la combinación:

\[
\text{Janson: patrón inducido no etiquetado}
\;+\;
\text{Hoeffding: concentración exponencial}
\;+\;
\text{test bipuntual: error--TV}.
\]

Esta cadena es suficiente para descartar un claim de novedad del teorema
abstracto.

## 6. Derivación exacta desde los antecedentes

Sea
\[
g_A(x_1,\ldots,x_m)
:=
\mathbf 1\{[\widetilde C(x_1,\ldots,x_m)]\in A\}.
\]
La equivarianza hace simétrico al kernel y la consistencia proyectiva identifica
\[
T_{n,m,A}
=
\binom nm^{-1}\sum_{|I|=m}g_A(X_I),
\]
un U-estadístico de un solo muestreo. Hoeffding (4.7), con
\(k=\lfloor n/m\rfloor\), da para ambas colas
\[
\Pr_\theta\{|T_{n,m,A}-q_\theta(A)|\ge t\}
\le 2e^{-2kt^2}.
\]

Para el test a punto medio no se necesita la cota bilateral: bajo cada
hipótesis se usa una sola cola con
\(t=\Delta_{m,A}/2\). Luego
\[
\alpha_n+\beta_n
\le
2e^{-k\Delta_{m,A}^2/2},
\]
y
\[
\operatorname{TV}(Q_\theta^n,Q_{\theta'}^n)
\ge 1-(\alpha_n+\beta_n).
\]
El estadístico es admisible para el dato observado por DFO-B. La truncación en
cero es puramente formal.

Si \(Q_\theta^m\ne Q_{\theta'}^m\), la finitud de \(\Omega_m\) permite escoger
un evento que alcanza \(\operatorname{TV}(Q_\theta^m,Q_{\theta'}^m)\). Esto
produce el corolario general sin ingrediente bibliográfico adicional.

## 7. Techo de claims

### Formulación permitida

> Aplicando la desigualdad de Hoeffding para U-estadísticos acotados a las
> densidades de subposets inducidos del marco de posets intercambiables de
> Janson, se obtiene una cota explícita de separación en variación total para
> las leyes no etiquetadas `fixed_n`. Registramos aquí esa especialización para
> el canal causal.

También es correcto afirmar:

- que la capa estadística es independiente de la dimensión;
- que el antecedente geométrico sigue siendo específico de cada familia;
- que la nota proporciona una formulación autosuficiente y constantes
  explícitas para su uso interno;
- que no se localizó una formulación idéntica en una sola fuente durante esta
  búsqueda acotada.

### Formulaciones prohibidas

- “nuevo teorema de separación”;
- “primera prueba” o “primer resultado”;
- “nueva desigualdad exponencial para posets”;
- cualquier inferencia de novedad a partir de
  `EXACT_SINGLE_SOURCE_NOT_LOCATED`;
- atribuir a Janson una tasa de TV que no enuncia;
- atribuir a Hoeffding la capa no etiquetada o la teoría de posets.

## 8. Condición antes de abrir PR

La puerta bibliográfica queda descargada con terminal `PRECURSOR_ONLY`, no con
un certificado de novedad. Antes de abrir un PR documental deben hacerse, en
un cambio separado y revisable:

1. corregir en la nota la localización de Hoeffding de “§5” a “§4a,
   ecuaciones (4.4)–(4.7)”;
2. añadir Janson 2011 como antecedente directo para densidades inducidas,
   intercambio de etiquetas, restricciones finitas y convergencia de posets;
3. mantener `NO_NOVELTY_CLAIM`;
4. presentar el teorema como especialización/corolario estándar con una
   derivación autosuficiente, no como prioridad matemática;
5. someter ese parche documental a revisión antes de abrir el PR.

No se ha ejecutado ninguna de esas acciones en esta auditoría. La hoja de ruta
preexistente, el manuscrito, el código, los experimentos y el historial Git
permanecen intactos.
