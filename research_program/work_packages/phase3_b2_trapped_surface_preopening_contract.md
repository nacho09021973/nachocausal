# Fase 3 B2 — contrato de preapertura v2: target sustituto \(Q_{\mathrm{trap}}\)

> **STATUS: PHASE_3_B2_PREOPENING_CONTRACT_V2_DRAFT / WORK_DATE_2026-07-29 /
> TARGET_NOT_ADOPTED / SCIENTIFIC_EXECUTION_NOT_OPENED / NO_CODE / NO_SIMULATION /
> NO_SEEDS / NO_THRESHOLD / NO_FREEZE / DOES_NOT_TOUCH_SEAL /
> ADJUDICATION_REQUIRED_IN_INDEPENDENT_SESSION.**
>
> Documento de trabajo revisable. Sucede al contrato v1
> (`phase3_b2_witness_pair_preopening_contract.md`, terminal
> `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL` registrado en su §12) tras la decisión
> `phase3_b2_qfmots_terminal_decision.md`. Prepara una única adjudicación científica
> futura por `/comite`, **que no puede ocurrir en la sesión que redactó este
> documento**; no presenta un teorema, no adopta un target y no autoriza construcción.

## 0. Por qué existe un v2

1. El target v1, \(Q_{\mathrm{FMOTS}}(g,U)\), recibió terminal tipado
   `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL`: se probó que el selector de coorientación
   "exterior" no queda fijado por \((g,U)\) en la clase local compacta (test falsificador
   \(S^3\), `phase3_b2_decision048_conditions_review.md`, Condición 1), y que la mejor
   reparación (extremo asintótico único) cambia la firma del target
   (`phase3_b2_asymptotic_end_restriction_review.md`, `REQUIRES_TARGET_CHANGE`).
2. Per contrato v1 §10, ese bloqueo cierra la instanciación, no la rama B2. Este v2 es la
   continuación de la rama con el único candidato identificado que **esquiva la obstrucción por
   construcción** en lugar de repararla con datos externos.
3. Los resultados reutilizables del expediente v1 se heredan explícitamente: Lema 1
   (irrelevancia de la normalización de \(\ell_\pm\)) y Lema 2 (covariancia por difeomorfismos),
   ambos probados en `phase3_b2_decision048_conditions_review.md`; y la Condición 2 (relación con
   Müller Thm 2) con su caveat permanente (§5 abajo).

## 1. Pregunta única de la adjudicación futura

> ¿Es admisible como target B2 sustituto el funcional binario intrínseco
> \(Q_{\mathrm{trap}}\), y existe una ruta no trivial —con regularidad y canal
> explícitos— para construir un par conforme estilo Müller que cambie
> \(Q_{\mathrm{trap}}\) mientras mantenga próximas las leyes de posets a
> cardinalidad fija?

El resultado de esa sesión debe ser una **ficha de target admitida para construcción
matemática** o un **bloqueo tipado** (§9). No se pasa a "buscar otro observable" durante
la misma sesión.

## 2. Target candidato

### 2.1 Definición provisional

Sea \(U\) un parche compacto, temporalmente orientado y causalmente convexo de una variedad
Lorentziana \(3{+}1\). Para una clase intrínseca y previamente cerrada
\(\mathcal S_{\mathrm{adm}}(g,U)\) de superficies espaciales compactas, cerradas, embebidas y
de codimensión dos, se propone

\[
Q_{\mathrm{trap}}(g,U)
=
\mathbf 1\!\left\{
\exists S\in\mathcal S_{\mathrm{adm}}(g,U):
\theta\bigl(\ell^{(1)}_S\bigr)<0\ \wedge\ \theta\bigl(\ell^{(2)}_S\bigr)<0
\right\},
\]

donde \(\ell^{(1)}_S,\ell^{(2)}_S\) son las dos direcciones nulas futuras normales a \(S\)
(existen exactamente dos para toda superficie espacial de codimensión 2), **sin designar
ninguna como exterior**, y las desigualdades se exigen puntualmente en todo \(S\).

**Lema 0 (inmunidad a la obstrucción v1 — enunciado y prueba de una línea).** La condición
definitoria es invariante bajo el intercambio \(\ell^{(1)}\leftrightarrow\ell^{(2)}\) (es una
conjunción simétrica) e invariante bajo reescalados positivos de cada dirección (Lema 1 del
expediente v1: \(\theta_{f\ell}=f\theta_\ell\), \(f>0\), preserva signos). Por tanto
\(Q_{\mathrm{trap}}\) no requiere ningún selector de coorientación, y el mecanismo del test
falsificador \(S^3\) — una isometría que permuta las dos presentaciones de \(S\) — deja la
condición invariante en lugar de hacerla inconsistente. La obstrucción que bloqueó el v1 no es
formulable contra este target. ∎

Es un target:

- **binario y adimensional**;
- **cuasi-local en sentido estricto**: funcional de \((g,U)\) solo, sin extensión ambiente,
  sin extremo, sin componente distinguida de \(\partial U\);
- de **existencia/clasificación**, no de localización de una región;
- definido sobre la completación geométrica latente, no sobre un estimador;
- **libre de orientación por construcción** (Lema 0).

### 2.2 Puntos que deben cerrarse antes de adoptarlo

1. **Escala admisible en \(\mathcal S_{\mathrm{adm}}\).** El expediente v1 (Condición 3) mostró
   que la degradación de regularidad de la ruta conforme depende de si la clase admite
   superficies de escala arbitrariamente pequeña (amplitud \(O(1)\), curvatura \(\sim\sqrt n\))
   o solo superficies de escala macroscópica (amplitud \(\sim\rho/L\to0\)). La clase debe fijar
   esta decisión **antes** de la adjudicación, y el escenario de escala resultante debe
   pre-declararse en el techo de reclamo (G4/G9).
2. **Anclaje primario de la noción.** "Superficie atrapada cerrada" (\(\theta\) de ambas familias
   nulas futuras estrictamente negativa) es la hipótesis clásica de los teoremas de singularidad,
   definida sin referencia a infinito ni a orientación exterior.
   `[UNVERIFIED against biblioteca — no hay texto de relatividad matemática en biblioteca/; la
   adjudicación debe anclar la definición a fuente primaria (p. ej. Penrose 1965, o un texto
   estándar tipo Hawking–Ellis / Wald) o marcarla como definición autocontenida del contrato.]`
3. **No-vacuidad en ambos sentidos (estándar Lean del repositorio,
   `formal/HorizonFormal/HorizonFormal/Horizon.lean:120-125`).** Deben exhibirse, con parche
   compacto causalmente convexo explícito:
   - **\(Q_{\mathrm{trap}}=1\):** un parche de Schwarzschild que contenga una esfera redonda con
     \(r<2M\) en algún corte: allí \(\Theta_{\rm out}=r^{-1}(1-2M/r)<0\) y
     \(\Theta_{\rm in}=-2/r<0\)
     (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:221-225`
     da las expresiones; el signo para \(r<2M\) es lectura directa de la fórmula). Nótese que este
     candidato está **mejor anclado localmente** que su análogo v1.
   - **\(Q_{\mathrm{trap}}=0\):** un parche de Minkowski. Hecho estándar (no hay superficies
     cerradas atrapadas en Minkowski) `[UNVERIFIED against biblioteca — mismo déficit de fuente
     que el punto 2; la adjudicación debe anclarlo o derivarlo]`.
4. **Medibilidad del mapa muestra→poset** como hipótesis explícita de la clase de regularidad
   (señalado por el matemático en la Decisión 048 §4 y nunca descargado).

### 2.3 Lo que este target no es — y el precio que paga

- no es \(T_{\mathrm{EH}}\) ni ningún objeto teleológico;
- no es \(Q_{\mathrm{FMOTS}}\): **no detecta "el horizonte exterior"** ni distingue
  configuraciones interiores de exteriores — detecta presencia de región atrapada en el parche.
  Esta pérdida semántica es el precio declarado del cierre intrínseco, y **no debe re-narrarse**
  como si el target siguiera siendo un detector de horizonte orientado;
- no es la pantalla `W(p,q)` de C6, ni un mapa `Min(C) -> región`, ni una reedición de C1–C6;
- no presupone que una superficie atrapada sea reconstruible desde el poset;
- no convierte una obstrucción finita en no-go asintótico;
- en el caso de referencia (Schwarzschild) su conjunto \(\{Q=1\}\) co-localiza con parches que
  penetran \(r<2M\), pero esa co-localización **no es parte de la definición ni del claim**.

## 3. Familia candidata para el par testigo

Idéntica a v1 §3 (familia conforme \(g_\omega=e^{2\omega}g_0\), \(\omega\in C_c^k(U)\), mismo
\(U\), orientación temporal y datos de borde), con las mismas obligaciones de tabla, y además:

- la ley de transformación conforme de \(\theta_\pm\) sigue siendo obligación de anclaje primario
  (las dos fórmulas de Wave 1 de la Decisión 048 eran mutuamente inconsistentes y ambas
  `[UNVERIFIED]`; ese estado no ha cambiado);
- la ventaja técnica específica de \(Q_{\mathrm{trap}}\) debe explotarse honestamente: la
  condición es **abierta** (desigualdades estrictas), así que la construcción no necesita
  producir una igualdad exacta \(\theta\equiv0\), solo cruzar un umbral de signo en un abierto —
  pero esto no exime de probar la **no existencia** en el lado \(Q=0\) sobre toda la clase
  \(\mathcal S_{\mathrm{adm}}\), que sigue siendo la mitad difícil (ataque 5 de v1, heredado
  íntegro).

## 4. Canal y régimen estadístico

Idénticos a v1 §4, sin cambio alguno: canal `ORDER_ONLY_CONDITIONED_ON_N` (poset no etiquetado de
\(n\) puntos i.i.d. de la medida de volumen normalizada en \(U\)), cadena TV §4.2 con las mismas
tres desigualdades a probar o citar con alcance exacto, y régimen permitido
`FIXED_n_OR_ANNOUNCED_FINITE_n_RANGE / TWO_POINT_MINIMAX_LOWER_BOUND /
POSSIBLY_n_DEPENDENT_WITNESS_PAIR`. La conclusión alcanzable es un **suelo de testeo**
(risk \(\ge(1-\mathrm{TV})/2\)), nunca una tasa de localización.

## 5. Relación obligatoria con Müller (caveat permanente heredado)

La Condición 2 del expediente v1 queda incorporada aquí con rango de cláusula permanente:

- El mecanismo (perturbación conforme de soporte pequeño sobre slab arbitrario, bordes
  compartidos) y el canal (ley de orden invariante a cardinalidad fija) son, hecho por hecho, los
  del Teorema 2 de Müller (arXiv:2503.01719v2, prueba en p. 3-4, leída íntegra y citada verbatim
  en `phase3_b2_decision048_conditions_review.md`, Condición 2).
- Müller es lógicamente mudo sobre superficies atrapadas: `grep -in
  "trap|horizon|MOTS|expansion|marginal"` sobre el texto completo extraído → cero coincidencias.
  `B2_REDUNDANT_WITH_MULLER` no se dispara por *resultado*; la comparación de G8 debe hacerse
  contra el **Teorema 2** (no el Teorema 3) y citar su frase de prueba verbatim.
- Si B2 se completa bajo este target, se describirá **siempre** como instanciación/adaptación
  acotada de la técnica de Müller sobre un target que su artículo no aborda — nunca como método
  nuevo. Esta cláusula no caduca.

## 6. Ataques falsadores que deben intentarse primero

Los ocho de v1 §6 se heredan (con "MOTS" leído como "superficie atrapada"), y se añaden dos
específicos de este target:

9. **Dilución semántica / falso positivo cosmológico.** \(Q_{\mathrm{trap}}=1\) puede darse en
   parches sin ningún agujero negro (p. ej. regiones cosmológicas en recolapso; superficies
   atrapadas de origen cosmológico). Si el par testigo separa \(Q\) mediante una configuración
   cosmológica, el resultado sigue siendo válido como separación del funcional, pero **no puede
   narrarse como "el orden recuerda el horizonte"** — solo como "el orden recuerda la presencia
   de región atrapada". El claim ceiling (G9) debe fijar esta redacción antes de construir.
10. **Pasado vs. futuro.** La definición usa direcciones nulas **futuras** (superficie
    futuro-atrapada). Un parche de universo en expansión contiene esferas **anti-atrapadas**
    (atrapadas hacia el pasado); la adjudicación debe verificar que la orientación temporal
    global de \(U\) (que sí es dato declarado del parche, a diferencia de "exterior") basta para
    distinguir futuro de pasado, y que ninguna construcción testigo explota una ambigüedad ahí.

## 7. Gates de admisión del target

Acumulativos, como en v1:

| ID | Gate | Evidencia mínima |
|---|---|---|
| G1 | Target intrínseco y difeomorfismo-invariante | definición cerrada de \(\mathcal S_{\mathrm{adm}}\) **incluida la decisión de escala**; Lemas 0–2 |
| G2 | No global / no teleológico | prueba de que \(Q\neq T_{\mathrm{EH}}\) por localidad de \(\mathcal S_{\mathrm{adm}}\) (vía Teorema 3.2, `docs/manuscript_limits_draft.md:455-483`) — condicional a G1, no antes |
| G3 | No localizador | output binario, sin mapa a región; salvaguarda explícita contra extracción de la superficie testigo (ataque 8) |
| G4 | Familia cerrada | \(U\), regularidad **con escenario de escala pre-declarado**, bordes, equivalencias, sampling |
| G5 | Separación real | argumento \(Q(g_0,U)\neq Q(g_1,U)\), con la mitad de no-existencia tratada como la carga principal |
| G6 | Cercanía estadística | cadena TV con constantes y régimen |
| G7 | No trivialidad | diferencia no introducida por etiqueta externa (Lema 0 cubre el modo de fallo v1; verificar que no entre por otra vía) |
| G8 | Prior art | comparación literal con Müller **Thm 2** (cita verbatim) y vecinos; incluye la órbita de dilatación exacta propia (Teorema 3.1) señalada por el lógico en 048 |
| G9 | Claim ceiling | fixed-\(n\); redacción anti-dilución del ataque 9 fijada por escrito; sin herencia de credibilidad del positivo 1+1 sellado |

Fallar cualquier gate impide abrir la construcción matemática bajo este target.

## 8. Entregables exactos de la sesión de adjudicación

Como v1 §8 (ficha Q de una página; proposición candidata ≤10 líneas; tabla del par; cadena TV;
ledger de fuentes — ahora obligatoriamente con el anclaje primario de "trapped surface" y la cita
verbatim del Thm 2 de Müller; ataque falsador contra G1, G3, G5, G7 **y el ataque 9**; terminal
único de §9). No se escribe código, no se construyen datos, no se reserva banda de seeds.

## 9. Terminales de la sesión de adjudicación

En orden de precedencia (idénticos a v1; se aplican a \(Q_{\mathrm{trap}}\) y este contrato):

```text
B2_BLOCKED_TARGET_NOT_INTRINSIC
B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL
B2_BLOCKED_NO_MATCHED_COMPLETION_FAMILY
B2_BLOCKED_REGULARITY_DEGENERATES
B2_BLOCKED_TARGET_SEPARATION_NOT_PROVED
B2_BLOCKED_NO_SMALL_TV_ROUTE
B2_REDUNDANT_WITH_MULLER
B2_TARGET_ADMISSIBLE_FOR_WITNESS_CONSTRUCTION
```

`B2_TARGET_ADMISSIBLE_FOR_WITNESS_CONSTRUCTION` autoriza únicamente completar la prueba
matemática del par. No autoriza simulación, código, estimador, prerregistro empírico, claim de
novedad ni publicación.

## 10. Criterio de éxito y parada de B2 (v2)

Como v1 §10, con una adición a la lista de parada limpia:

- se aparca también si el único par separador disponible depende del falso positivo cosmológico
  (ataque 9) **y** el PI juzga que el claim resultante ("el orden recuerda la región atrapada")
  ya no sirve al objetivo 3+1D del programa (`docs/plan_operativo_15_julio_2026.md`) — este
  juicio es del PI, no de la sesión de adjudicación.

Un bloqueo documentado de este target no refuta B2 en general. Si \(Q_{\mathrm{trap}}\) también
se bloquea, la rama B2 queda con dos instanciaciones cerradas y una coherente-no-perseguida
(\(Q_{\mathrm{end}}\)); la decisión de cerrar B2 entera sería entonces un acto separado del PI.

## 11. Estado de autorización

```text
PHASE_3_BRANCH = B2
PREOPENING_CONTRACT_V2 = DRAFT_AWAITING_INDEPENDENT_ADJUDICATION
PRIMARY_TARGET_CANDIDATE = Q_trap
PREDECESSOR = Q_FMOTS (terminal B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL, contrato v1 §12)
TARGET_ADOPTION = PENDING_SCIENTIFIC_ADJUDICATION
ADJUDICATION_SESSION = MUST_BE_INDEPENDENT_OF_DRAFTING_SESSION
WITNESS_CONSTRUCTION = NOT_AUTHORIZED_YET
CODE = NOT_AUTHORIZED
SIMULATION = NOT_AUTHORIZED
SEEDS = NOT_AUTHORIZED
THRESHOLDS = NOT_APPLICABLE
SEALED_PATH = UNTOUCHED
COMMIT_OF_THIS_DRAFT = AUTHORIZED_BY_PI_DELEGATION_2026_07_29
```
