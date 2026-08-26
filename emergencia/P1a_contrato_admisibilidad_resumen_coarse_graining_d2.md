# P1a — Contrato de admisibilidad para un resumen de coarse-graining en `d=2`

> **ESTADO: CONTRATO DE ADMISIBILIDAD CONGELADO v1.0 · SOLO DOCUMENTO ·
> COORDENADAS DEL RESUMEN NO ELEGIDAS · SIN EJECUCIÓN AUTORIZADA.**
>
> Fecha de congelación: 26 de agosto de 2026.

Este documento fija qué condiciones debe satisfacer cualquier resumen pequeño
candidato antes de estudiar si conserva información suficiente para anticipar el
estimando orbital bajo thinning. No define todavía `Xi_n`, no valida las cinco
coordenadas sugeridas en una discusión exploratoria y no autoriza calcular
`q_p`, escoger una métrica ni buscar pares adversariales.

`Xi_n=(B_n,Delta mu_n,Delta Sigma_n,m_n(delta),O_n)` no es un objeto heredado de
`nachocausal`: es una propuesta nueva y sus nombres no constituyen definiciones.

## 1. Objeto que se quiere resumir

Sea `C=C_sigma` el `2-order` estricto asociado a una permutación de tamaño `n`.
Se conserva el selector `MIN_COVERAGE_LEX`, con `K0=3`, del contrato
`P1a_contrato_estimando_qp_orbital_d2.md`.

Se denota por `Q(C)` el conjunto de todas las cuádruplas admisibles y por

\[
L_C(x)=\bigl(\min(C_{ab},C_{cd}),\ C_{ab}+C_{cd}\bigr),
\qquad x=(a,b,c,d)\in Q(C),
\]

su score lexicográfico. Si `Q(C)` no es vacío,

\[
L^\star(C)=\max_{x\in Q(C)}L_C(x),
\qquad
M(C)=\{x\in Q(C):L_C(x)=L^\star(C)\}.
\]

`Aut(C)` actúa tanto sobre `Q(C)` como sobre cada nivel del score y, en
particular, sobre `M(C)`. El paisaje estático de candidatos de `C` comprende
`Q(C)`, sus scores, sus relaciones de solapamiento y la acción de `Aut(C)`.

Un resumen candidato se denotará provisionalmente por

\[
\Psi_n(C)\in\mathcal X_n.
\]

Esta notación evita presuponer que el vector exploratorio de cinco nombres sea el
resumen correcto.

## 2. Objetivo y techo de afirmación

El futuro experimento solo podrá preguntar si configuraciones próximas o iguales
según `Psi_n` tienen valores próximos de

\[
q_p(C)=\Pr\{r_{\rm orb}(R_p(C))=1\mid C\}.
\]

Que un resumen supere pruebas finitas no lo convierte en variable suficiente, no
demuestra una dinámica de renormalización y no establece `WALL` ni `NO-WALL`.
Una discrepancia exacta dentro de una fibra de `Psi_n` sí puede refutar la
suficiencia exacta de ese resumen en el tamaño y régimen examinados.

## 3. Condiciones obligatorias de admisibilidad

Una propuesta de `Psi_n` será admisible solo si satisface simultáneamente:

1. **Definición previa.** Cada coordenada tiene fórmula, dominio, codominio,
   convención de borde y justificación informativa antes de materializar valores
   de `q_p`.
2. **Intrinsicidad.** Si `C` y `C'` son isomorfos, entonces
   `Psi_n(C)=Psi_n(C')`. No puede depender de etiquetas, de la representación
   concreta por permutación ni de coordenadas latentes del sprinkling.
3. **Estado original solamente.** Se calcula usando únicamente `C`, su paisaje
   estático de candidatos y sus invariantes. No evalúa configuraciones obtenidas
   al borrar, intercambiar, perturbar o reordenar elementos.
4. **Independencia del thinning.** No usa máscaras, `R_p`, subposets propios
   inducidos, tasas de retención ni resultados de aplicar `r_orb` después de una
   eliminación.
5. **Ausencia de fuga del objetivo.** No usa `q_p`, `q_p^star`, `e_p`, los
   coeficientes exactos `a_k,b_k`, estimaciones Monte Carlo ni sustitutos
   construidos a partir de esos objetos.
6. **Independencia de `p`.** Una misma definición de `Psi_n` debe servir para la
   función de retención que se decida estudiar; no se rediseñan coordenadas para
   cada valor de `p`.
7. **Baja dimensión real.** El número de coordenadas queda acotado
   independientemente de `n`. Se excluyen listas de longitud creciente,
   histogramas sin binning previamente acotado y codificaciones encubiertas de
   la relación completa.
8. **Compresión no trivial.** No se admiten hashes, etiquetas canónicas,
   expansiones digitales ni reales de precisión arbitraria que permitan
   reconstruir `C`. Antes de mirar `q_p` se documentará la distribución de
   tamaños de las fibras de `Psi_n` y se verificará que contiene colisiones entre
   clases no isomorfas en el dominio del falsador.
9. **Totalidad y tipado explícito.** `Psi_n` debe estar definido también cuando
   `Q(C)` o `M(C)` sean vacíos. Una cantidad inexistente será `NA` acompañada de
   un indicador de disponibilidad; no se convertirá silenciosamente en cero.
10. **Reproducibilidad exacta.** Toda coordenada debe poder contrastarse con una
    especificación independiente en el piloto `n<=9`. La eventual
    implementación optimizada no será su propia referencia.

## 4. Información permitida, sin elegir todavía coordenadas

Las condiciones anteriores permiten que una coordenada inspeccione, dentro de la
configuración original:

- invariantes intrínsecos de `C`;
- el número y los scores de los candidatos de `Q(C)`;
- el score óptimo y déficits respecto de él;
- la partición en órbitas de candidatos situados en niveles de score previamente
  definidos;
- cardinalidades de órbitas y estabilizadores;
- relaciones combinatorias de incidencia o solapamiento entre candidatos,
  intervalos y endpoints.

Esta lista delimita fuentes de información; no selecciona una coordenada ni una
normalización. En particular, expresiones como «margen», «rival», «solapamiento»
u `O_n` siguen siendo nombres informales hasta que se especifique su fórmula.

El número orbital original

\[
\rho(C)=|M(C)/Aut(C)|
\]

es información estática admisible. Si una propuesta lo incluye, deberá declarar
que `q_1(C)=r_orb(C)` es entonces un control tautológico, no evidencia predictiva.
La prueba no trivial tendrá que usar `0<p<1`.

## 5. Información excluida por este contrato

No son admisibles como coordenadas:

- cualquier función de los resultados sobre las `2^n` máscaras;
- la respuesta de `r_orb` en subposets propios inducidos;
- una estimación directa o suavizada de `q_p`;
- el grado de reparación obtenido evaluando transposiciones vecinas, salvo que
  un contrato posterior cambie expresamente la regla de «estado original»;
- una coordenada escogida por su correlación observada con `q_p`;
- la identidad de `sigma`, una forma canónica completa o cualquier codificación
  inyectiva equivalente;
- una estadística cuya convención para `EMPTY`, empates o automorfismos quede
  implícita.

La exclusión del grado de reparación no afirma que sea irrelevante. Separa la
dinámica por transposiciones del thinning independiente que define `q_p`.

## 6. Secuencia obligatoria para proponer el resumen

Antes de ejecutar el falsador se deberá completar, en este orden:

1. formular la pérdida de información que cada coordenada pretende controlar;
2. dar su definición exacta y sus convenciones `EMPTY/NA`;
3. demostrar o comprobar su invariancia por isomorfismo;
4. fijar cualquier normalización dependiente de `n` y cualquier parámetro como
   `delta` sin observar `q_p`;
5. fijar la dimensión y verificar que el resumen no es una codificación
   inyectiva;
6. congelar la métrica o regla de igualdad en espacio-`Psi`;
7. congelar la regla de selección de pares y el criterio de falsación;
8. solo entonces materializar `q_p` mediante el piloto exacto.

Si se exploran varias propuestas, deberán declararse de antemano como una familia
finita y conservar identidades distintas. No se podrá presentar como
prerregistrado un resumen seleccionado después de comparar sus resultados con
`q_p`.

## 7. Objetos que permanecen abiertos

Este contrato no fija:

- el número final de coordenadas;
- ninguna de las cinco coordenadas sugeridas para `Xi_n`;
- una definición de margen, rival cercano, solapamiento u orbit count agregado;
- normalizaciones, umbrales o el parámetro `delta`;
- la métrica `d_Xi`;
- valores concretos de `p`;
- la búsqueda adversarial;
- el criterio cuantitativo de falsación;
- una banda nula Monte Carlo para tamaños mayores;
- ninguna ejecución.

```text
P1A_COARSE_SUMMARY_ADMISSIBILITY_VERSION = 1.0
P1A_COARSE_SUMMARY_STATUS = COORDINATES_OPEN
P1A_COARSE_SUMMARY_TARGET = q_p
P1A_COARSE_SUMMARY_TARGET_ACCESS = FORBIDDEN_DURING_DESIGN
P1A_COARSE_SUMMARY_THINNING_FEATURES = FORBIDDEN
P1A_COARSE_SUMMARY_NEIGHBOR_EVALUATION = FORBIDDEN
P1A_COARSE_SUMMARY_FIXED_DIMENSION = REQUIRED
P1A_COARSE_SUMMARY_NONTRIVIAL_FIBERS = REQUIRED
P1A_COARSE_SUMMARY_RUN_AUTHORIZATION = 0
```
