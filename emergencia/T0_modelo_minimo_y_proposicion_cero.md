# T0 — Modelo mínimo y proposición cero

> **ESTADO: BORRADOR MATEMÁTICO v0.1 · PRUEBA INTERNA COMPLETA · NO AUDITADO
> INDEPENDIENTEMENTE.**
>
> Documento de arranque de la línea independiente **Identificabilidad del tiempo
> métrico desde orden causal finito**. No es una preregistración, no contiene
> evidencia numérica, no autoriza simulaciones y no reclama novedad para la
> maquinaria estadística utilizada.

## 0. Decisión de arranque

La primera familia será deliberadamente rígida: diamantes causales completos de
Minkowski cuya única cantidad desconocida es su duración propia. El objetivo no es
representar todavía una geometría general, sino aislar sin ambigüedad qué cambia al
pasar de cardinalidad condicionada a conteo Poisson con densidad conocida.

El orden de ataque inicial será:

1. **P2**, mediante una separación exacta entre escala invisible y escala calibrada;
2. **P1**, después de resolver cómo definir dos intervalos de manera intrínseca;
3. **P3**, comenzando por el error finito debido exclusivamente al conteo.

Este orden no altera las tres preguntas fundacionales. Solo escoge el caso en el que
puede obtenerse primero un resultado matemático controlado.

## 1. Pregunta exacta de esta nota

> En una familia de diamantes causales de Minkowski de dimensión y forma conocidas,
> ¿qué información sobre la duración absoluta `tau` contiene un poset finito cuando
> su cardinalidad está condicionada, y qué información reaparece cuando se conserva
> la ley Poisson de esa cardinalidad a densidad conocida?

La comparación se hará sobre la misma familia latente. No se enfrentará «orden sin
número» a «orden con número»: todo poset finito revela su cardinalidad. La diferencia
es si el valor observado de `N` fue fijado por diseño o si conserva su distribución de
muestreo y, con ella, información de volumen.

## 2. Familia geométrica mínima

### 2.1 Espacio-tiempo y diamante

Sea `d >= 2` conocido y sea `M^d` el espacio de Minkowski `d`-dimensional, con
coordenadas `(t,x)` y métrica de signatura `(-,+,...,+)`. Para `tau > 0`, definimos

```text
p_tau = (-tau/2, 0),
q_tau = ( tau/2, 0),
A_tau = I^+(p_tau) intersección I^-(q_tau).
```

La separación temporal entre los extremos latentes es

```text
tau(p_tau,q_tau) = tau.
```

Los extremos `p_tau` y `q_tau` delimitan la familia generativa, pero no se entregan
como eventos etiquetados en la observación. El target de esta nota es la duración del
diamante latente completo, no el tiempo propio entre dos elementos seleccionados a
posteriori dentro del causal set.

### 2.2 Volumen

Sea

```text
omega_(d-1) = pi^((d-1)/2) / Gamma((d+1)/2)
```

el volumen de la bola unidad en `R^(d-1)`. Una sección del diamante a tiempo `t`
es una bola espacial de radio `tau/2 - |t|`. Por integración directa,

```text
Vol_d(A_tau) = kappa_d tau^d,

kappa_d = omega_(d-1) / (d 2^(d-1))
        = pi^((d-1)/2) / (d 2^(d-1) Gamma((d+1)/2)).
```

Comprobaciones particulares:

```text
kappa_2 = 1/2,
kappa_4 = pi/24.
```

### 2.3 Parámetro, target y observación

Fijamos por comodidad un espacio paramétrico compacto

```text
Theta = [tau_min, tau_max],   0 < tau_min < tau_max < infinito.
```

El target es

```text
T(tau) = tau.
```

La observación es la clase de isomorfía de un poset finito `C`, de la que también se
conoce necesariamente

```text
N(C) = |C|.
```

Se olvidan coordenadas, etiquetas, embedding y posiciones de los extremos latentes.

## 3. Dos experimentos que no deben mezclarse

### 3.1 Experimento condicionado `E_fix(n)`

Se fija `n >= 0` por diseño y se toman

```text
X_1,...,X_n iid ~ mu_tau,

mu_tau = Vol_d|_(A_tau) / Vol_d(A_tau).
```

El orden entre puntos es el inducido por la causalidad de Minkowski y la observación
final es el poset no etiquetado. Denotamos su ley por

```text
Q_(n,tau) = Law([C_n] | N=n, tau).
```

Aquí conocemos la cardinalidad `n`, pero no es una variable aleatoria disponible para
distinguir valores de `tau`.

### 3.2 Experimento Poisson `E_Pois(rho)`

Se fija una densidad física homogénea conocida `rho > 0` y se genera un proceso de
Poisson sobre `A_tau` con intensidad

```text
rho dVol_d.
```

La observación vuelve a ser el poset no etiquetado completo, ahora de tamaño aleatorio.
Su cardinalidad satisface

```text
N ~ Poisson(lambda_tau),
lambda_tau = rho kappa_d tau^d.
```

Denotamos la ley conjunta del poset y su cardinalidad por `P_(rho,tau)`.

## 4. Definición de identificabilidad

Para una familia de leyes `{P_theta : theta in Theta}`, un target `T(theta)` es
identificable si

```text
P_theta = P_theta'  implica  T(theta) = T(theta').
```

Esta es identificabilidad de la familia en ley. No significa que exista un estimador
preciso a tamaño finito ni que una sola realización determine el parámetro sin error.

## 5. Proposición cero — ceguera y recuperación de escala

### Enunciado

En la familia de las secciones 2–3:

1. **Ceguera exacta condicionada.** Para todo `n >= 0` y todo
   `tau,tau' in Theta`,

   ```text
   Q_(n,tau) = Q_(n,tau').
   ```

   Por tanto, la duración absoluta `T(tau)=tau` no es identificable en
   `E_fix(n)` y la distancia TV entre cualesquiera dos valores de `tau` es cero.

2. **Factorización Poisson.** Si `c` es un poset no etiquetado con `|c|=n`,

   ```text
   P_(rho,tau)(C=c)
     = Poisson(lambda_tau){n} Q_n(c),
   ```

   donde `Q_n` no depende de `tau`.

3. **Suficiencia del número.** Con `d`, `rho` y la forma del diamante conocidos,
   `N` es estadísticamente suficiente para `tau`; condicionado a `N=n`, el patrón
   de orden es ancilar respecto de `tau`.

4. **Identificabilidad Poisson.** Para `rho` conocida,

   ```text
   P_(rho,tau) = P_(rho,tau')  si y solo si  tau=tau'.
   ```

   Además, para dos duraciones,

   ```text
   TV(P_(rho,tau), P_(rho,tau'))
     = TV(Poisson(lambda_tau), Poisson(lambda_tau')).
   ```

   Toda la capacidad de distinguir la escala procede del conteo.

5. **Confusión densidad–escala.** Si `rho` también es desconocida, la ley depende de
   ambas cantidades únicamente mediante

   ```text
   eta = rho tau^d.
   ```

   En consecuencia, `rho` y `tau` no son identificables por separado.

### Demostración

Sea `a=tau'/tau` y considérese la dilatación

```text
D_a : (t,x) -> (a t, a x).
```

Esta aplicación lleva `A_tau` biyectivamente sobre `A_tau'`, preserva el orden causal
y multiplica el elemento de volumen por `a^d`. Al normalizar el volumen total, ese
factor se cancela:

```text
(D_a)_# mu_tau = mu_tau'.
```

Por ello, aplicar `D_a` a una muestra iid de `mu_tau` produce una muestra iid de
`mu_tau'` con exactamente la misma matriz de comparabilidades. La ley del poset
etiquetado es la misma y, después de olvidar las etiquetas, también lo es la ley del
poset no etiquetado. Esto prueba (1).

En un proceso de Poisson, condicionado al evento `N=n`, los puntos son iid con ley
de volumen normalizada `mu_tau`. Por (1), la ley condicional del poset es una misma
ley `Q_n` para todo `tau`. La regla de probabilidad total da (2).

La factorización separa toda dependencia en `tau` en el factor Poisson que solo usa
`N`; el criterio de factorización prueba (3). Como `tau -> rho kappa_d tau^d` es
inyectiva para `rho>0` y `tau>0`, dos leyes Poisson coinciden si y solo si coinciden
sus medias, lo cual prueba (4). La igualdad de TV se obtiene sumando, para cada
cardinalidad, sobre todos los posets de ese tamaño:

```text
(1/2) sum_n sum_(c:|c|=n)
  |p_lambda(n)Q_n(c) - p_lambda'(n)Q_n(c)|

= (1/2) sum_n |p_lambda(n)-p_lambda'(n)|.
```

Finalmente, si `rho` es desconocida, la media Poisson y por tanto toda la ley solo
dependen de `rho kappa_d tau^d`. La transformación

```text
(rho,tau) -> (rho a^(-d), a tau)
```

deja esa ley invariante siempre que ambos pares permanezcan en el espacio paramétrico.
Esto prueba (5). `QED`

## 6. Consecuencias de decisión y estimación

### 6.1 Cota exacta en el canal condicionado

Sean `tau_0 != tau_1`. Como ambos parámetros producen la misma ley, para cualquier
estimador —determinista o aleatorizado— `tau_hat(C_n)` se cumple

```text
max_i E_(tau_i)|tau_hat-tau_i| >= |tau_1-tau_0|/2,

max_i E_(tau_i)(tau_hat-tau_i)^2 >= |tau_1-tau_0|^2/4.
```

Si `Theta=[tau_min,tau_max]`, los estimadores constantes en el punto medio alcanzan
esas cotas para las pérdidas absoluta y cuadrática. Por tanto,

```text
minimax absoluto = (tau_max-tau_min)/2,
minimax cuadrático = (tau_max-tau_min)^2/4.
```

Aumentar `n` no reduce este riesgo: se ha eliminado la escala del experimento al
condicionar la cardinalidad.

### 6.2 Estimación en el canal Poisson

Sin imponer todavía los extremos de `Theta`, el estimador de máxima verosimilitud es

```text
tau_hat_raw = (N/(rho kappa_d))^(1/d).
```

En el espacio compacto fijado en §2.3, el MLE restringido es la proyección de
`tau_hat_raw` sobre `[tau_min,tau_max]`. Para `d>1` no debe describirse automáticamente
como insesgado; cuando `N=0`, el MLE restringido cae en `tau_min`. Los intervalos exactos
deben construirse primero para la media Poisson `lambda` y transformarse después mediante

```text
tau = (lambda/(rho kappa_d))^(1/d).
```

La información de Fisher de una observación es

```text
I_tau = d^2 lambda_tau / tau^2
      = rho kappa_d d^2 tau^(d-2).
```

Así, en el interior del espacio paramétrico y para estimadores insesgados regulares,
la cota de Cramér–Rao implica

```text
Var(tau_hat)/tau^2 >= 1/(d^2 lambda_tau).
```

La escala relativa de fluctuación `1/(d sqrt(lambda_tau))` es un límite local del
modelo Poisson, no un principio universal de incertidumbre temporal.

La afinidad de Bhattacharyya entre las dos marginales de conteo es

```text
BC(Poisson(lambda),Poisson(lambda'))
  = exp(-(sqrt(lambda)-sqrt(lambda'))^2/2),
```

lo que hace explícita una resolución relativa de orden `lambda^(-1/2)` para cambios
locales de escala. Cualquier claim minimax concreto requerirá fijar pérdida y espacio
paramétrico.

## 7. Qué resuelve y qué no resuelve

### 7.1 Efecto sobre P2

La proposición proporciona una respuesta completa solo dentro de la familia mínima:

- a cardinalidad fija, la escala absoluta es estructuralmente invisible;
- con conteo Poisson y `rho` conocida, la escala es identificable;
- con `rho` desconocida, sobrevive una órbita exacta de confusión.

No demuestra que `orden + número` reconstruya tiempo métrico en una familia
lorentziana general. La conclusión positiva usa de manera esencial que se conocen
dimensión, forma del diamante, homogeneidad y relación volumen–duración.

### 7.2 Efecto sobre P1

La proposición no resuelve si razones de tiempos propios son identificables. Una razón
es invariante bajo la dilatación global utilizada en la prueba y, por ello, no queda
destruida por este contraejemplo.

El próximo obstáculo es definir dos intervalos o pares de eventos mediante una regla
intrínseca del poset. Introducir extremos elegidos desde el embedding oculto cambiaría
el canal de observación.

### 7.3 Efecto sobre P3

El canal condicionado presenta un límite exacto que no disminuye con `n`. El canal
Poisson ofrece, en cambio, una referencia finita de conteo con escala relativa
`lambda^(-1/2)`. Este será el control más simple antes de añadir:

- error de cadenas máximas;
- inferencia de dimensión;
- curvatura;
- efectos de borde;
- desviaciones respecto de un diamante completo;
- e incertidumbre o inhomogeneidad en `rho`.

## 8. Hipótesis externas y techo de afirmación

### Hipótesis necesarias

1. espacio de Minkowski exacto;
2. dimensión `d` conocida y fija;
3. región latente exactamente igual a un diamante causal completo;
4. muestreo uniforme o proceso de Poisson homogéneo;
5. densidad `rho` conocida para la conclusión positiva;
6. target restringido a la duración total del diamante.

### Afirmaciones autorizadas por esta nota

- `exact scale blindness after conditioning on N=n in the minimal family`;
- `scale identifiability from Poisson count at known density in the minimal family`;
- `N is sufficient for tau and conditional order is ancillary in this family`;
- `rho and tau are confounded when rho is unknown`.

### Afirmaciones no autorizadas

- que todo tiempo métrico emerge de cualquier causal set;
- que el orden no contiene información temporal adimensional;
- que el número basta sin conocer dimensión, forma o densidad;
- que una realización finita reconstruye una geometría general;
- que la cota Poisson es un principio fundamental de incertidumbre temporal;
- que el resultado es novedoso dentro de causal set theory.

## 9. Relación con resultados existentes de `nachocausal`

La prueba es una especialización elemental a Minkowski del mecanismo de órbitas de
escala que ya aparece en el programa general:

- `research_program/models/first_witness_pair_candidates.md`, Teorema A, prueba
  ceguera exacta de escala en una familia Schwarzschild `1+1` condicionada a `N=n`;
- `research_program/synthesis/op12_tv_zero_3p1.md` extiende una órbita acotada de
  dilatación a Schwarzschild `3+1` y separa expresamente el canal Poisson;
- `research_program/work_packages/wp4_two_point_theorem.md` proporciona el lema de
  dos puntos y explica la fuga por cardinalidad.

Por tanto, la aportación de esta nota no es un nuevo no-go general. Su función es fijar
el banco de pruebas más transparente para la nueva línea temporal y derivar en él la
factorización, suficiencia y riesgo exactos que se usarán como controles posteriores.

## 10. Anclas bibliográficas locales

1. **Surya (2019), pp. 12–17.** Formula `Order + Number ~ Lorentzian Geometry`,
   presenta el número como volumen y da la ley Poisson con media `rho V`.
   Archivo: `biblioteca/emergencia/1903.11544v2_Surya_Causal_Set_Approach_to_Quantum_Gravity.pdf`.
2. **Kambor–X (2020), pp. 2–5.** Explicita `N=rho V`, el muestreo Poisson y la
   dependencia de los estimadores temporales respecto de la densidad.
   Archivo: `biblioteca/emergencia/2007.03835v3_Kambor_X_Manifold_Properties_Using_Chains.pdf`.
3. **Braun (2025), pp. 3–4.** Separa el componente de orden del componente de número
   y formula la reconstrucción probabilística mediante todas las leyes de muestras
   condicionadas, bajo hipótesis globales fuertes.
   Archivo: `biblioteca/emergencia/2507.01907v1_Braun_Spacetime_Reconstruction_Order_Number.pdf`.
4. **Madsen (2026), pp. 1–2.** Añade embeddings bien condicionados, densidad común y
   correspondencia cadenas–proper time; sirve como advertencia de que la unicidad a
   alta densidad requiere más estructura que una realización finita desnuda.
   Archivo: `biblioteca/emergencia/2607.05840v1_Madsen_Uniqueness_Embeddings_Causal_Sets.pdf`.

Braun y Madsen son preprints recientes. No se usan como premisas necesarias para la
demostración de la proposición cero.

## 11. Siguiente problema matemático

La siguiente unidad no debe ampliar todavía la geometría. Debe intentar construir el
primer target de P1:

> una razón de dos duraciones definida mediante dos subestructuras que puedan
> seleccionarse de forma equivariante desde el poset no etiquetado, sin coordenadas,
> extremos suministrados ni desempate dependiente de etiquetas.

Antes de proponer un estimador habrá que decidir si el target es:

1. una cantidad puntual, definida solo cuando la selección es única;
2. una clase de equivalencia bajo automorfismos;
3. una distribución o multiconjunto de razones;
4. o un funcional promedio sobre todos los pares admisibles.

Ese problema de definición es parte de la identificabilidad, no un detalle técnico.

Su primera capa se abre en:

```text
emergencia/P1a_seleccion_intrinseca_y_automorfismos.md
```

P1a separa la posibilidad de selección equivariante de la posterior validez métrica
del cociente y adopta una política explícita de `UNIQUE_ORDERED_PAIR_OR_ABSTAIN`.
El primer selector concreto queda congelado en
`emergencia/P1a_primer_selector_de_cobertura.md`: dos intervalos causalmente
ordenados y disjuntos, soporte mínimo tres y cobertura total máxima, sin desempate
secundario.
Su puerta teórica en Minkowski se encuentra en
`emergencia/P1a_puerta_teorica_en_Minkowski.md`: el vacío queda cerrado mediante la
altura y solo se habilita el diseño de una enumeración exacta en `d=2`.
La enumeración y el Monte Carlo posteriormente autorizados se completaron bajo
contrato en `emergencia/P1a_resultados_enumeracion_y_monte_carlo_d2.md`, con terminal
de disponibilidad operacional positivo y sin claim métrico.
