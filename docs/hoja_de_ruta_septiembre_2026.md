# Hoja de ruta — septiembre de 2026 · de eficiencia combinatoria a tangentes geométricas

> **Plan REVISABLE, no congelado.** No es una pre-registración, no autoriza
> simulaciones, nuevos observables, consumo de semillas, cambios en instrumentos
> sellados ni extrapolaciones dimensionales. Su función es fijar el orden lógico
> de la nueva rama de información Fisher y evitar que vuelvan a abrirse frentes
> antes de cerrar el puente geométrico. Mantener `FAMILY_FROZEN`,
> `NO_UNIVERSALITY_CLAIM` y `PRIORITY = PROVISIONAL_NOT_SEALED`.

```text
GOBERNANZA: docs/program_reopening_note_2026-08-28_R4.md (firmada 2026-08-28)
G2: §2.2 enmendada a Convención B el 2026-08-28
    (lambda parametriza P psi, no el tangente de copula)
S2_NOT_OPENED
```

## 0. Punto de partida preservado

Rama de trabajo:

```text
emergencia/p1a-canal-sigma-m
```

Commits de preservación de entrada:

```text
236b1824d86ad3c169e574bf263ecde40310eb04
  prove asymptotic Fisher efficiency for unlabeled 2D posets

4bcbfc50a95ddb7af52bfa002974016b9eafbd43
  document unlabeled 2D poset Fisher theorem
```

Anclas obligatorias antes de trabajar:

1. `research_program/work_packages/wp6_d2_modular_fiber_score.md`;
2. `research_program/work_packages/wp6_d2_null_copula_dichotomy.md`;
3. `README.md`, sección “Current theory result — Fisher efficiency of
   unlabeled 2D posets”.

Estado científico de entrada:

```text
FAMILY_FROZEN
FINITE_N_POSET_LOSS_PROVED
TYPICAL_FIBER_ZERO_LOSS = PROVED
ASYMPTOTIC_POSET_FISHER_EFFICIENCY_FOR_BOUNDED_SEPARABLE_SCORES = PROVED
THEOREM_PROVED_PRIORITY_AUDIT_PASSED_PROVISIONALLY
POTENTIALLY_NOVEL_THEOREM_NOT_NOVEL_FRAMEWORK
NO_UNIVERSALITY_CLAIM
NEXT_TARGET = GEOMETRIC_TANGENT_CLASSIFICATION
TARGET_SUBCLASS = SYMMETRIC_RANK_ONE_COPULA_TANGENTS
GENERIC_BILINEAR_SEPARABLE_EXTENSION = OPEN_NOT_ASSUMED
RATE_IMPROVEMENT = DEFERRED
PRIORITY = PROVISIONAL_NOT_SEALED
```

El teorema autónomo ya demostrado usa una permutación uniforme `Pi_N`, el
canal exacto

\[
\Pi_N\longmapsto[P_{\Pi_N}],
\]

y scores simétricos separables

\[
S_N(\pi)=2\sum_{i=1}^N a_{i,N}a_{\pi(i)}.
\]

Si los perfiles son uniformemente acotados, centrados y tienen energía no
degenerada, entonces

\[
1-\frac{I_N^{[P]}}{I_N^\Pi}=O(N^{-1/2}),
\qquad
\frac{I_N^{[P]}}{I_N^\Pi}\longrightarrow1.
\]

Este resultado no se reabre en septiembre salvo contradicción matemática
explícita.

## 1. Norte único de septiembre

El único frente científico autorizado al comenzar el mes es

```text
GEOMETRIC_TANGENT_CLASSIFICATION
```

La pregunta es:

> ¿Qué perturbaciones conformes de un diamante causal (1+1) inducen, tras
> normalizar la medida y eliminar las marginales, un tangente de cópula
> simétrico rank-one cuyo score de rangos pertenece exactamente a la clase del
> teorema ya probado?

La secuencia vinculante es

\[
\boxed{
\text{teorema combinatorio ya probado}
\longrightarrow
\text{clasificación del tangente geométrico}
\longrightarrow
\text{teorema geometría }1+1\to\text{causet}
\longrightarrow
\text{auditoría final de prioridad}.
}
\]

No se abre el siguiente eslabón hasta cerrar o refutar el anterior.

## 2. Fase S1 — cerrar el puente geométrico

### 2.1 Objeto congelado

Partir de una perturbación conforme

\[
g_\varepsilon
=\frac{e^{2\varepsilon\psi(u,v)}}{Z(\varepsilon)}g_0
\]

en un diamante (1+1), con dominio, medida de referencia y condicionamiento en
`N` fijados antes de cualquier generalización.

Debe derivarse desde la medida normalizada, no postularse, el tangente de
cópula obtenido al retirar las dos marginales:

\[
\boxed{
h_\psi(u,v)
=2\,[\psi(u,v)-\psi_U(u)-\psi_V(v)+\bar\psi].
}
\]

Aquí deben definirse explícitamente `psi_U`, `psi_V`, `bar psi`, la constante
`Z(epsilon)` y el sentido de la derivada. No se permite esconder términos de
normalización dentro de una proporcionalidad informal.

### 2.2 Subclase objetivo

Caracterizar exactamente cuándo

\[
\psi(u,v)-\psi_U(u)-\psi_V(v)+\bar\psi
=\lambda f(u)f(v),
\qquad\text{equivalentemente}\qquad
h_\psi(u,v)=2\lambda f(u)f(v),
\]

con

\[
f\ \text{suave},
\qquad
\int_0^1 f(u)\,du=0,
\qquad
\int_0^1 f(u)^2\,du>0,
\]

y con las condiciones de acotación necesarias para aplicar el teorema de
scores separables.

**Convención B (G2, 2026-08-28).** El símbolo `lambda` parametriza la
proyección geométrica `P psi`, no el tangente de cópula. El factor `2` de
`h_psi=2 P psi` queda explícito, y el score de §2.3 usa el mismo `lambda`
en todas las etapas. (La Convención A, `h_psi=lambda f f`, queda
retirada de este §2.2.)

El objetivo no es clasificar todas las perturbaciones conformes. Es identificar
una subclase geométrica explícita, no vacía y estable bajo las equivalencias
marginales pertinentes.

### 2.3 Obligaciones de prueba

1. Derivar el score de la muestra condicionada a `N`.
2. Derivar el score condicionado a la permutación de rangos.
3. Probar que, en la subclase rank-one simétrica,
   \[
   S_N(\pi)=2\lambda\sum_i a_{i,N}a_{\pi(i)},
   \qquad
   a_{i,N}=\mathbb E[f(U_{(i)})],
   \]
   con cualquier convención de escala registrada de forma consistente.
4. Verificar, sin simulación:
   \[
   \sup_{N,i}|a_{i,N}|<\infty,
   \qquad
   \sum_i a_{i,N}=0,
   \qquad
   \frac1N\sum_i a_{i,N}^2\longrightarrow\int_0^1 f(u)^2\,du>0.
   \]
5. Distinguir el tangente geométrico, el tangente de densidad, el tangente de
   cópula y el score de rangos. No identificarlos mediante notación ambigua.

### 2.4 Falsificadores obligatorios

- Una perturbación puramente marginal
  `psi(u,v)=alpha(u)+beta(v)+const` debe desaparecer tras la proyección de
  marginales.
- Debe verificarse el factor `2`, el signo y el término `bar psi` mediante una
  diferenciación independiente.
- Debe exhibirse al menos una `psi` no sinusoidal dentro de la clase o demostrar
  que la clase geométrica se reduce más de lo previsto.
- Si un producto genérico `f(u)g(v)` con `f != g` aparece, no se promoverá al
  teorema simétrico: quedará fuera de alcance.

### 2.5 Veredictos permitidos

```text
GEOMETRIC_TANGENT_CLASSIFICATION = PROVED
GEOMETRIC_TANGENT_CLASSIFICATION = REFUTED
GEOMETRIC_TANGENT_CLASSIFICATION = OPEN_WITH_EXACT_OBLIGATION
```

`OPEN` sólo es admisible con una proposición concreta pendiente. Un ejemplo
numérico o una expansión formal sin control del resto no cierra la fase.

## 3. Fase S2 — primer teorema completo geometría a causet

Esta fase sólo se abre si S1 termina `PROVED`.

### 3.1 Enunciado objetivo

Para la clase explícita de deformaciones conformes rank-one simétricas obtenida
en S1, demostrar

\[
\boxed{
\frac{I_N^{[P]}(g_\varepsilon)}
     {I_N^\Pi(g_\varepsilon)}
\longrightarrow1.
}
\]

La notación debe especificar:

- familia geométrica y parámetro local;
- diamante (1+1) y coordenadas normalizadas;
- condicionamiento a cardinalidad fija `N`;
- representación observada antes del cociente;
- poset orientado no etiquetado observado después del cociente;
- score y punto nulo donde se calcula Fisher;
- clase exacta de `psi` o de `f`.

### 3.2 Claim ceiling

El resultado permitido será:

> En una clase explícita de deformaciones conformes simétricas rank-one de un
> diamante (1+1), el poset no etiquetado retiene asintóticamente toda la
> información Fisher relativa disponible en la permutación de rangos.

No estará permitido inferir:

- suficiencia respecto de las coordenadas continuas completas;
- reconstrucción de la métrica;
- universalidad para todo tangente geométrico;
- una afirmación sobre horizontes;
- una afirmación en (2+1) o (3+1);
- suficiencia absoluta sin especificar el experimento comparado.

### 3.3 Entregable

Un teorema autónomo con prueba modular en cuatro pasos:

1. geometría `->` tangente de cópula;
2. tangente de cópula `->` score de rangos simétrico;
3. score simétrico `->` teorema combinatorio ya probado;
4. conclusión Fisher para el canal `Pi_N -> [P_Pi_N]`.

No duplicar en esta fase las pruebas del cuarto momento ni de la fibra típica;
citarlas con hipótesis verificadas una por una.

## 4. Fase S3 — auditoría final de prioridad geométrica

Esta fase sólo se abre cuando exista un enunciado geométrico completo y estable.
La auditoría provisional del teorema combinatorio no sustituye esta revisión.

### 4.1 Pregunta adversarial exacta

> ¿Existe una fuente previa que demuestre suficiencia asintótica (L^2) o
> Fisher del poset bidimensional no etiquetado respecto de la permutación de
> rangos para tangentes procedentes de deformaciones geométricas conformes de
> la clase S1?

No basta encontrar antecedentes sobre:

- suficiencia asintótica de cuantizaciones en general;
- estadística clásica de rangos;
- cópulas, permutons o frecuencias de patrones antes del cociente;
- rigidez o unicidad de órdenes aleatorios bidimensionales;
- pérdida de etiquetas en grafos mediante entropía o mutual information.

### 4.2 Salidas permitidas

```text
DIRECT_PRIOR_FOUND
PRECURSOR_ONLY
SURVIVES_NARROWLY
INCONCLUSIVE_ACCESS_OR_SCOPE
```

Aunque el resultado sobreviva, el wording máximo seguirá siendo:

> We are not aware of previous results establishing the stated asymptotic
> Fisher-retention theorem for this exact geometric-to-unlabeled-poset channel.

No usar `first`, `novelty certified`, `breakthrough` ni equivalentes.

## 5. Fase S4 — generalización simétrica controlada en (1+1)

Esta fase no pertenece al objetivo inicial de septiembre. Sólo puede diseñarse
si S1–S3 están cerradas y documentadas.

La observación estructural de partida es que la fibra típica es

\[
\{\pi,\pi^{-1}\}.
\]

Por ello, para

\[
S_H(\pi)=\sum_i H_{i,\pi(i)},
\]

la condición

\[
H=H^{\mathsf T}
\]

hace al score invariante bajo inversión. El primer candidato de extensión es
una clase de rango finito

\[
H_N=\sum_{r=1}^R
\lambda_r a^{(r)}a^{(r)\mathsf T}.
\]

Esto es una **ruta candidata**, no un corolario ya demostrado. Antes de
promoverla habrá que cerrar de nuevo:

1. escala no degenerada de `I_N^Pi`;
2. cota de cuarto momento uniforme para el score matricial;
3. dependencia admisible de `R`, `lambda_r` y las normas de los perfiles;
4. clase geométrica que produce esos kernels simétricos.

```text
FINITE_RANK_SYMMETRIC_SCORE_EXTENSION = DEFERRED_NOT_PROVED
```

## 6. Fase S5 — clasificar la información que sí se pierde

Después del sector simétrico se estudiará su contraparte. Para

\[
S_{x,y}(\pi)=x^{\mathsf T}P_\pi y,
\qquad x\ne y,
\]

la inversión global produce

\[
S_{x,y}(\pi^{-1})=y^{\mathsf T}P_\pi x,
\]

que no tiene por qué coincidir con el score original. Por tanto, incluso el
sector típico puede conservar pérdida.

La pregunta futura será si existe una descomposición rigurosa entre:

\[
\text{sector simétrico: eficiencia relativa }\to1,
\]

y

\[
\text{sector asimétrico: pérdida posiblemente persistente}.
\]

No se preregistra esa dicotomía como verdadera. Debe falsarse primero en
tamaños finitos y demostrarse después a nivel de la ley condicional.

```text
GENERIC_BILINEAR_SEPARABLE_EXTENSION = OPEN_NOT_ASSUMED
```

## 7. Fase S6 — salto a (2+1)

El paso dimensional sólo se abre después de una teoría (1+1) geométrica y
simétrica estabilizada. En (2+1) ya no existe la cadena especial

\[
\text{cópula}\leftrightarrow
\text{permutación}\leftrightarrow
\text{poset 2D}.
\]

La pregunta transportable será:

\[
\boxed{
\text{¿qué fracción de la información Fisher de una representación geométrica}
\atop
\text{sobrevive al olvidar el embedding y observar sólo }[C]\text{?}
}
\]

El primer trabajo en (2+1) deberá definir el experimento antes y después del
cociente. No empezará con reconstrucción métrica, simulaciones masivas ni un
observable elegido por conveniencia.

```text
DIMENSION_2P1_EXTENSION = DEFERRED
```

## 8. Fase S7 — programa de `information retention`

El objeto a largo plazo es clasificar tangentes geométricos mediante

\[
\eta_N(h)
=\frac{I_N^{\mathrm{intrinsic}}(h)}
       {I_N^{\mathrm{representation}}(h)}.
\]

Los tres regímenes conceptuales que deberán distinguirse, sin asumir que todos
ocurren, son

\[
\eta_N(h)\to1,
\qquad
\eta_N(h)\to\eta_\infty\in(0,1),
\qquad
\eta_N(h)\to0.
\]

El programa preguntará qué información geométrica es preservada, parcialmente
perdida o destruida por el paso desde una representación enriquecida al causet
intrínseco. Éste es un horizonte de investigación, no una afirmación vigente.

## 9. Secuencia operativa de septiembre

### Semana 1 — derivación geométrica

1. fijar dominio, normalización y convenciones;
2. derivar `h_psi` por dos rutas independientes;
3. ejecutar los falsificadores marginales y de signo/factor;
4. registrar la obligación exacta si la fórmula no cierra.

### Semana 2 — clasificación rank-one y score de rangos

1. caracterizar la preimagen geométrica de `lambda f tensor f`;
2. derivar el score condicionado a rangos;
3. verificar acotación, centrado y energía;
4. emitir el veredicto S1.

### Semana 3 — teorema geometría a causet

Sólo si S1 es `PROVED`:

1. escribir el enunciado autónomo;
2. encadenar las cuatro piezas de §3.3;
3. auditar cuantificadores, canales y denominadores Fisher;
4. preparar una versión legible independiente del work package.

### Semana 4 — prioridad y decisión de continuación

1. ejecutar la auditoría adversarial S3;
2. fijar el claim ceiling final;
3. decidir si la rama continúa hacia S4;
4. no comenzar S4 dentro del mismo acto de decisión.

Si S1 queda `REFUTED` u `OPEN`, las semanas restantes se dedican a documentar
el bloqueo y preservar el resultado combinatorio. No se compensa abriendo S4,
S5 o (2+1).

## 10. Entregables de septiembre

Obligatorios, en orden:

1. derivación exacta del tangente geométrico y de cópula;
2. clasificación o refutación de la subclase simétrica rank-one;
3. verificación de las hipótesis del teorema de eficiencia;
4. teorema completo geometría (1+1) `->` causet, si procede;
5. auditoría final de prioridad del teorema geométrico, si procede;
6. actualización mínima de README e inventario de teoremas sólo después de
   cerrar los resultados correspondientes.

Cada entregable debe incluir:

- hipótesis completas;
- canal exacto;
- prueba o bloqueo preciso;
- falsificador finito/simbólico proporcionado al riesgo;
- fuentes primarias cuando se importe un teorema;
- claim permitido y claim prohibido;
- tests deterministas y `git diff --check` antes de preservarlo.

## 11. No hacer en septiembre

- No pasar todavía a (2+1) ni (3+1).
- No mejorar la tasa `O(N^{-1/2})`.
- No abrir scores bilineales genéricos.
- No promover automáticamente kernels simétricos de rango finito.
- No hacer simulaciones asintóticas.
- No introducir observables nuevos.
- No mezclar este frente con horizontes o reconstrucción métrica.
- No generalizar de rank-one simétrico a `f tensor g` con `f != g`.
- No declarar prioridad sellada a partir de ausencia de resultados en una
  búsqueda.
- No llamar universal al teorema combinatorio ni al eventual teorema
  geométrico.
- No tocar instrumentos, umbrales, semillas ni artefactos congelados de otros
  frentes de NACHOCAUSAL.

```text
RATE_IMPROVEMENT = DEFERRED
GENERIC_BILINEAR_SEPARABLE_EXTENSION = OPEN_NOT_ASSUMED
DIMENSION_2P1_EXTENSION = DEFERRED
NO_SIMULATION_AUTHORIZATION
NO_UNIVERSALITY_CLAIM
```

## 12. Gates de cierre del mes

### Gate A — `GEOMETRIC_CAUSALSET_THEOREM_PROVED`

S1 y S2 están demostradas, S3 está auditada y el wording no excede la
evidencia. Septiembre cierra con un teorema geométrico (1+1) y una decisión
separada sobre S4.

### Gate B — `COMBINATORIAL_THEOREM_PRESERVED_GEOMETRIC_BRIDGE_OPEN`

El teorema combinatorio permanece intacto, pero S1 deja una obligación concreta
no resuelta. No se abre ninguna generalización para compensarlo.

### Gate C — `GEOMETRIC_RANK_ONE_ROUTE_REFUTED`

La fórmula marginal o la clasificación muestran que la ruta rank-one propuesta
no describe la clase geométrica esperada. Se entrega el contraejemplo o la
caracterización correcta, sin reparar retrospectivamente el contrato.

### Gate D — `PRIORITY_SCOPE_REVISED`

El teorema geométrico cierra matemáticamente, pero la auditoría encuentra un
antecedente directo o una limitación de prioridad. Se ajusta el framing sin
debilitar ni inflar el contenido matemático.

## 13. Criterio de éxito y visión de continuidad

La visión de la rama es

\[
\boxed{
\text{teorema combinatorio}
\longrightarrow
\text{teorema geométrico }1+1
\longrightarrow
\text{clase simétrica más amplia}
\longrightarrow
2+1.
}
\]

Septiembre tiene éxito si convierte el primer arco en el segundo o identifica
con precisión por qué no puede hacerlo. No requiere mejorar tasas, ampliar
dimensión ni producir numerics.

Si el puente geométrico falla, la rama conserva un teorema combinatorio
autónomo. Si el puente cierra y la generalización simétrica empieza después a
sobrevivir, habrá una línea propia de investigación sobre retención de
información geométrica en causal sets. Esa posibilidad no se promociona como
resultado antes de demostrar sus gates.

## 14. Checklist de reentrada

1. Confirmar rama, `HEAD`, upstream y worktree limpio.
2. Leer las tres anclas de §0 antes de derivar nada.
3. Verificar que no existe otro objetivo `in_progress`.
4. Copiar literalmente las definiciones de canal y score ya probadas; no
   reconstruirlas de memoria.
5. Abrir sólo S1.
6. Antes de cada cambio de fase, emitir el veredicto permitido y preservar el
   diff correspondiente.
7. Si aparece una contradicción con el teorema combinatorio, detener la hoja y
   auditarla antes de continuar.
