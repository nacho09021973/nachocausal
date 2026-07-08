# Matriz bibliográfica — identificabilidad geométrica desde orden causal

> **Documento de trabajo REVISABLE, no congelado.** Esta matriz reorganiza la bibliografía ya
> auditada en `docs/bibliography_claims.md` desde la pregunta del programa:
>
> > qué observable geométrico parece identificable desde orden causal, bajo qué hipótesis, y dónde
> > se rompe esa identificabilidad.

No sustituye al dossier de claims. Lo reordena para trabajo analítico.

## 0. Cómo leer esta matriz

Cada fila responde a cinco preguntas:

1. **Objeto geométrico**: qué se intenta recuperar.
2. **Canal informacional**: orden solo, orden+número, o input geométrico adicional.
3. **Régimen de validez**: continuum, ensemble, single-instance, dimensión, tipo de espaciotiempo.
4. **Qué licencia da**: qué afirmación permite sostener.
5. **Gap de identificabilidad**: dónde deja abierto el problema.

La columna decisiva para este programa es la última.

## 1. Matriz de alto nivel

| Línea | Objeto geométrico | Canal | Régimen | Qué licencia da | Gap de identificabilidad | Estado |
|---|---|---|---|---|---|---|
| HKMM | clase causal/conformal del espaciotiempo | orden + elemento de volumen | continuum, `d>2` | la causalidad transporta mucha geometría | no cubre `d=2`; no es resultado discreto; no fija el factor conforme desde orden solo | `PARTIAL` para este programa |
| Order + Number | geometría lorentziana hasta factor conforme | orden + cardinalidad/volumen | ensemble CST | justifica el slogan CST `Order + Number` | el paso `n ~ rho V` es en media; a realización finita hay fluctuación `sqrt(V)` | `PARTIAL` |
| Faithful embedding | manifold-likeness aproximada | orden + sprinkling Poisson | ensemble / embedding fiel | respalda que algunos posets aproximan geometrías | no prueba unicidad, convexidad necesaria ni identificabilidad single-instance | `PARTIAL` |
| Hauptvermutung / O-Hauptvermutung | unicidad aproximada del continuo subyacente | orden + número | general, pero incompleto | apoya una visión de reconstrucción por invariantes caso a caso | no hay teorema general; la mayoría de posets no son manifold-like | `PARTIAL` |
| Myrheim-Meyer | dimensión estadística de embedding | orden solo | ensemble, Minkowski o región pequeña curva | muestra que alguna cantidad de dimensión es order-recoverable | no vale como manifold-likeness; no conecta con order-dimension combinatoria; no es single-instance | `PARTIAL` |
| Homología espacial estable | topología de slice espacial | orden solo con antichain/collar | escala separada, hipótesis geométricas fuertes | prueba recuperación parcial de topología espacial | no recupera topología completa del espaciotiempo; la versión relevante para horizontes sigue abierta | `PARTIAL` |
| Links horizon-crossing (Dou-Sorkin) | área/entropía de horizonte | orden + partición de horizonte + cardinalidad | asintótico; 1+1D útil, `d>=3` problemático | benchmark geométrico externo de conteo | no localiza horizonte desde el causet; en `d>=3` el 1-link molecule diverge | `PARTIAL` / `CONTRADICTED` fuera de 1+1D |
| Horizon molecules (Barton et al.) | área de horizonte en esperanza | orden + horizonte/Σ dados + cardinalidad | expectation over sprinklings | observable geométrico covariante y fuerte para área | no identifica el horizonte intrínsecamente; gap single-instance explícito | `PARTIAL` |
| Causal horizon definition | horizonte como `∂I^-(γ_0)` | definición continuum | continuum | fija el objeto geométrico correcto | no da operacionalización intrínseca en causets finitos | `SUPPORTED` como definición |
| EGS longest-chain / future signal | frontera asociada al horizonte en 1+1D singular | orden solo | finite sprinklings, 1+1D Schwarzschild | precedente directo para recoverability order-only | depende de futures truncados por singularidad; no mostrado como convergencia general al horizonte | `PARTIAL` |
| EGS apparent-horizon ladders | signo de expansión interior/exterior | orden + baseline Minkowski + orientación práctica con embedding | 1+1D | precedente de clasificación física interior/exterior | no localiza finamente; implementación publicada usa embedding info | `PARTIAL` |
| EGS fuzzy ladders | porción discreta de horizonte | orden, pero con selección/orientación guiada por embedding | 1+1D proof-of-principle | target comparativo para una construcción futura | no es order-only en el sentido estricto del repo; exterior falla en signo; peel-off abierto | `PARTIAL` |

## 2. Lectura por tipo de observable

### 2.1 Clase causal / conformal

**Resultado central:** HKMM.

Qué respalda:

- la estructura causal sí transporta geometría no trivial;
- el orden no es una compresión absurda del continuo;
- la parte naturalmente accesible desde orden es de tipo causal/conformal.

Qué no cierra:

- el régimen del proyecto es `d=2`, justo fuera del teorema citado;
- HKMM no es un teorema de causal sets finitos;
- no responde identificabilidad a resolución finita.

Lectura programática:
esta línea justifica perseguir geometría desde orden, pero no autoriza ningún claim fino sobre
localización de horizonte en el régimen actual.

### 2.2 Volumen / cardinalidad

**Resultado central:** `Order + Number ~ Geometry`.

Qué respalda:

- para observables dependientes de volumen, el orden solo no basta;
- el número de elementos es parte constitutiva de la información geométrica.

Gap de identificabilidad:

- la correspondencia `n ~ rho V` es ensemble-level;
- para un causet finito concreto hay fluctuación Poisson de orden `sqrt(V)`;
- esto ya introduce una fuente estructural de incertidumbre volumétrica.

Lectura programática:
si el observable geométrico de interés mezcla causalidad y escala métrica, cualquier discusión de
"indeterminación" debe distinguir orden puro de orden+cardinalidad.

### 2.3 Dimensión

**Resultado central:** Myrheim-Meyer.

Qué respalda:

- hay cantidades order-only recuperables en sentido estadístico;
- la dimensión es un banco de pruebas positivo para el programa general.

Gap de identificabilidad:

- es resultado de ensemble, no de una realización aislada;
- no prueba manifold-likeness;
- no conecta con la `dim_DM` combinatoria usada en algunos hilos internos del repo.

Lectura programática:
la dimensión muestra que "order-only recoverability" existe, pero también que puede vivir en un
régimen estadístico mucho más débil que una localización geométrica fina.

### 2.4 Topología

**Resultado central:** homología espacial estable.

Qué respalda:

- parte de la topología espacial puede recuperarse desde orden, con maquinaria extra adecuada.

Gap de identificabilidad:

- la topología total del espaciotiempo no es recuperable de esa manera;
- el caso de estructuras de trapping/boundary sigue mucho menos cerrado;
- se necesita separación de escalas fuerte.

Lectura programática:
la topología es ejemplo de recoverability parcial bajo hipótesis fuertes, no de reconstrucción
general.

### 2.5 Horizonte como área / conteo

**Resultados centrales:** Dou-Sorkin, Dhital, horizon molecules.

Qué respaldan:

- existen observables causal-set bien motivados ligados a la geometría del horizonte;
- el área del horizonte puede emerger como expectativa de un conteo order-theoretic bien elegido.

Gap de identificabilidad:

- esos observables suelen necesitar el horizonte ya dado como input continuum;
- dan área/entropía o conteos, no localización intrínseca;
- el gap single-instance sigue explícito;
- en `d>=3` la versión más naive fracasa.

Lectura programática:
esta línea es fuerte para **benchmark geométrico**, pero débil para **horizon identification from
order alone**.

### 2.6 Horizonte como frontera detectable en causets finitos

**Resultado central:** EGS longest-chain / future-cardinality.

Qué respalda:

- en 1+1D Schwarzschild singular, un observable order-only computable en causets finitos puede
  separar interior/exterior y localizar una transición sharp cerca del horizonte.

Gap de identificabilidad:

- el mecanismo depende de futuros truncados por singularidad;
- no está cerrado como resultado de horizonte genérico;
- no está demostrado como identificación arbitrariamente refinable;
- el observable complementario de future-cardinality es sensible al borde de caja.

Lectura programática:
esta línea es el precedente más cercano a `prereg-002`, pero también el recordatorio más fuerte
de que recoverability aquí puede estar capturando un **singularity imprint** más que una noción
genérica de horizonte.

### 2.7 Horizonte como expansión / ladders

**Resultados centrales:** rigid ladders, fuzzy ladders.

Qué respaldan:

- hay otra familia física distinta del longest-chain signal;
- la sustracción por baseline Minkowski no es capricho interno del repo, sino necesidad física
  observada externamente;
- una construcción tipo "porción discreta de horizonte" existe como proof-of-principle.

Gap de identificabilidad:

- los resultados fuertes son de signo/clasificación, no de localización fina;
- la implementación publicada usa información de embedding para orientar o seleccionar ladders;
- la extensión exterior puede fallar incluso cuando el interior funciona;
- el peel-off de ladders largos deja abierto si la frontera es infinitamente localizable.

Lectura programática:
esta línea es especialmente valiosa para el programa de indeterminación, porque pone sobre la mesa
una posibilidad concreta:

> recuperación global/coarse de frontera, pero fallo de localización geométrica fina estable.

## 3. Lectura por tipo de canal informacional

### 3.1 Orden solo

Ejemplos con apoyo real:

- dimensión estadística tipo Myrheim-Meyer;
- longest-chain/proper-time proxies;
- señal de horizonte en EGS 1+1D singular.

Patrón:

- sí hay recoverability parcial;
- suele ser estadística, coarse o dependiente de un régimen muy específico;
- la localización fina y genérica sigue abierta.

### 3.2 Orden + número / volumen

Ejemplos:

- slogan CST `Order + Number`;
- area-law en horizon molecules;
- link-counting de horizonte.

Patrón:

- la geometría métrica más rica parece requerir cardinalidad/medida;
- incluso entonces, gran parte de la literatura vive en expectativas de ensemble, no en
  realización finita única.

### 3.3 Orden + input geométrico externo

Ejemplos:

- horizonte dado como partición outside/inside;
- superficie `Σ` y curva `γ_0` dadas;
- selección/orientación de ladder usando embedding.

Patrón:

- estos trabajos pueden ser geométricamente muy informativos;
- pero no resuelven el problema order-only de identificabilidad intrínseca.

## 4. Huecos bibliográficos que importan al programa

### 4.1 Gap A — `d=2`

El soporte tipo HKMM que justifica "orden transporta geometría" no cierra el caso `d=2`.

Importancia:
el banco de pruebas central del repo vive precisamente en `1+1D`.

### 4.2 Gap B — single-instance vs ensemble

Muchos resultados fuertes de CST son en esperanza o por promedio de ensemble.

Importancia:
el proyecto experimental trabaja con realizaciones finitas concretas y scoring por seed.

### 4.3 Gap C — horizonte genérico vs imprint singular

La línea más cercana al repo (EGS longest-chain) depende de truncación por singularidad.

Importancia:
sin separar ese mecanismo, no se puede promover recoverability local a claim de horizonte
genérico.

### 4.4 Gap D — localización fina vs clasificación gruesa

Parte de la literatura logra:

- clasificación interior/exterior,
- sign change,
- área en esperanza,
- porciones discretas proof-of-principle.

Pero no cierra:

- localización fina arbitrariamente refinable;
- convergencia single-instance fuerte;
- no-identificabilidad intrínseca.

### 4.5 Gap E — lower bounds intrínsecos

La matriz bibliográfica revisada aquí no aporta todavía un lower bound general del tipo:

> ninguna regla order-only puede localizar mejor que escala `a_n`.

Importancia:
ese es exactamente el hueco donde entra el programa de identificabilidad/minimax/contigüidad.

## 5. Conclusión operativa para el programa

La literatura disponible sugiere este cuadro:

1. **Sí** hay evidencia seria de que el orden causal contiene geometría recuperable.
2. **No** hay base para pasar directamente de ahí a reconstrucción geométrica general.
3. **Sí** hay recoverability parcial y física relevante para ciertos observables order-only.
4. **No** está cerrado cuándo esa recoverability se convierte en localización arbitrariamente fina.
5. **No** tenemos aún un lower bound intrínseco del orden para el observable horizonte.
6. **Sí** existe ya una tensión bibliográfica real entre:
   - recoverability coarse,
   - sensibilidad a borde/caja,
   - dependencia de singularidad,
   - y fallos o peel-off en construcciones finas.

Esa tensión es precisamente el hueco científico donde vive el programa de
**indeterminación order/geometría**.

## 6. Siguientes documentos que esta matriz habilita

Con esta base, los siguientes artefactos útiles son:

1. `research_program/models/canonical_counterexamples.md`
2. una nota sobre familias `P_n(theta)` y testing/contigüidad
3. un primer work package de lower bounds sobre una clase concreta de observables

La matriz bibliográfica ya deja claro por qué ese siguiente paso no debe ser "otro observable más"
sin marco de identificabilidad.
