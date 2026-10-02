# S4W — brief para auditoría matemática independiente

**Objeto primario:** commit `15eb7a500f18abc401f3671edecc65a995ef3e89`  
**Objeciones preliminares separadas:** commit `64aa326c1daa22000dbd21346c784c11a2a7d5cd`  
**Base:** `relatividad @ 008918b65d4e800b05ce8fec6908d8022e350482`  
**Regla:** no ejecutar simulaciones; auditoría analítica y bibliográfica solamente.

## Mandato

Auditar desde cero el candidato `S4W_5LAYER_KRETSCHMANN_CANDIDATE.md`. No asumir correctas las conclusiones del candidato ni las del precheck. Las fuentes primarias, no la narración del repo, mandan.

Emitir uno y sólo uno de:

```text
AUDIT_PASS_FORMAL
AUDIT_PASS_CONDITIONAL
AUDIT_REQUIRES_MAJOR_FIX
AUDIT_REJECT
```

Un `PASS` debe especificar exactamente qué afirmaciones pasan. No promover un subresultado algebraico a estimador físico.

## Fuentes mínimas

1. Belenchia, arXiv:1510.04665 — definición GCD y restricciones de coeficientes.
2. Belenchia–Benincasa–Dowker, arXiv:1510.04656 — partición W1/W2/W3 y prueba del límite 4D.
3. Wang, arXiv:1904.01034 — volumen de ACD en vacío y definición de `E,H,D` respecto a la orientación temporal `U`.
4. Aslanbeigi–Saravani–Sorkin, arXiv:1403.1622 — familia GCB/prior art.
5. de Brito–Eichhorn–Pfeiffer, arXiv:2301.13525 — operadores de curvatura superior/prior art.

Cualquier claim de prioridad requiere búsqueda adicional; no inferir novedad de ausencia.

## Pregunta A — álgebra de cinco capas

Reproducir en D=4, sin usar números copiados del candidato:

- las restricciones de Belenchia para `a,b_n`;
- el núcleo de cinco capas;
- si `D5=(-1;3,-47,148,-168,64)` es realmente una dirección nula completa;
- si `lambda_*=2 sqrt(6)/3` anula el momento Gamma `n+2`;
- si el operador resultante es proporcional a

```text
(-1/2; 1,-14,41,-44,16)
```

- si

\[
\widehat O_* = \tfrac12(H+2)\widehat O_{BD}
\]

con las convenciones exactas de la fuente.

Un error de normalización/signo debe registrarse aunque no cambie la dirección nula.

## Pregunta B — región W2

No aceptar el razonamiento “hay raíz H=-2, por tanto mejora automáticamente un orden”.

Determinar si, bajo las hipótesis de Belenchia–Benincasa–Dowker, la integral previa a `O_*` admite una expansión uniforme suficientemente fuerte para concluir

\[
I_{2,*}=O(\rho^{-5/2}).
\]

Comprobar explícitamente:

- uniformidad en coordenadas longitudinales/angulares;
- regularidad requerida;
- términos `rho^-2 log rho` o análogos;
- efecto de los límites de integración;
- si el argumento necesita hipótesis adicionales no presentes en el candidato.

Si sólo puede probarse `o(rho^-2)` o una cota más débil, decirlo exactamente.

## Pregunta C0 — finitud antes de cualquier coeficiente de C²

El PI realizó una comprobación simbólica independiente, no incorporada como código al objeto congelado (`br.py` permanece local y no forma parte del repo). En Schwarzschild, usando la tétrada estática con `M=r=1`, boosts de rapidez `eta` en dirección arbitraria y `gamma=cosh(eta)`, obtuvo:

- `E^2-H^2 = 6` para cualquier boost, consistente con `K=8(E^2-H^2)=48 M^2/r^6`;
- para boost radial, `E^2+H^2=6` para todo `eta`;
- para boost tangencial,

\[
E^2+H^2=36\gamma^4-36\gamma^2+6;
\]

- promedio sobre direcciones a rapidez fija,

\[
\langle E^2+H^2\rangle
=\frac65\left(16\gamma^4-12\gamma^2+1\right).
\]

El control `gamma=1` devuelve `6`. Esta comprobación NO debe aceptarse por autoridad del repo: el auditor debe reproducirla o refutarla.

Suponiendo correctamente transcrita la ecuación (79) de Wang en `d=4`, la corrección de volumen relevante contiene

\[
2032E^2+360H^2
=836(E^2-H^2)+1196(E^2+H^2).
\]

Sólo el primer término es proporcional a `K`. El segundo es la densidad de Bel–Robinson `T(U_y,U_y,U_y,U_y)` y depende de la dirección temporal `U_y` del par `(x,y)`.

A rapidez grande, la parte no invariante crece como `gamma^4 ~ e^{4 eta}`. A tiempo propio fijo, la medida del hiperboloide temporal en 4D crece como `sinh^2(eta) d eta ~ e^{2 eta} d eta`; si el peso depende sólo del volumen propio del intervalo, el integrando angular/rapidez crece formalmente como `e^{6 eta}`.

**Límite lógico de esta observación:** para `eta` grande, `y` está lejos de `x` en coordenadas aunque el tiempo propio sea fijo, de modo que la expansión RNC local usada para obtener la corrección de Wang deja de ser válida. La divergencia formal NO demuestra que la integral exacta diverja. Sí demuestra que no se puede extender uniformemente la aproximación local sobre todo el hiperboloide sin un argumento adicional.

Antes de calcular ningún número para `C^2`, el auditor debe responder:

1. ¿Es finita la integral del término `E^2+H^2` sobre `J^-(x)` bajo las hipótesis exactas del esquema Belenchia–Benincasa–Dowker?
2. Si no lo es sin regulación/soporte compacto, ¿qué región geométrica domina el problema: `W1`, `W2`, frontera de soporte u otra?
3. ¿Existe en Belenchia–Benincasa–Dowker un argumento publicado que justifique cortar, regular o tratar localmente esa región a la precisión subdominante `O(rho^-1/2)` requerida aquí?
4. Si la finitud sólo se obtiene imponiendo soporte compacto, parche finito o taper, ¿se demuestra que la contribución dependiente de esa prescripción es `o(rho^-1/2)` para `O_*`?

Si la integral global para `phi=1` no está definida y ninguna prescripción publicada controla la dependencia del cutoff por debajo del orden objetivo, el estado debe promoverse a

```text
S4W_KRETSCHMANN_ESTIMATOR = NOT_DEFINED_WITHOUT_EXTRA_PRESCRIPTION
```

no meramente `NOT_ESTABLISHED`.

## Pregunta C — término local W1 y Weyl²

Éste es el punto decisivo si C0 no mata antes el estimador.

Rehacer la expansión a orden curvatura-cuadrada sin fijar prematuramente el frame estático de Schwarzschild.

Wang define `E,H,D` respecto a un vector temporal `U`; en un ACD, `U` está ligado a la geodésica entre sus extremos. En la integral del operador, `y` varía por el cono temporal. Determinar si la orientación relevante es `U_y` y, en ese caso, mantenerla dentro de la integral.

Comprobar si es legítimo o ilegítimo usar globalmente

\[
H=0,\qquad D^2=4E^2,\qquad K=8E^2
\]

con `E` evaluado en el tetrad estático.

Después combinar de forma consistente:

- expansión de `sqrt(-g(y))` en RNC a orden `C^2 y^4`;
- expansión del volumen `V(x,y)` del intervalo;
- acción de `O_*`;
- integrales angulares y nulas.

Sólo si se reproduce de forma independiente puede aceptarse

\[
\mathbb E[B_*1]
=-\frac{73\sqrt6}{1575\pi}C^2\rho^{-1/2}+o(\rho^{-1/2}).
\]

Si el coeficiente cambia o no queda determinado, el estimador normalizado del candidato falla aunque el operador de cinco capas sobreviva.

## Pregunta D — estructura del término permitido

Separar dos afirmaciones:

1. por covariancia/dimensiones/paridad, una corrección local escalar de dimensión cuatro en vacío puede quedar restringida a `C_{abcd}C^{abcd}` (más posibles términos que deban excluirse explícitamente);
2. el coeficiente de ese escalar es distinto de cero y tiene un valor concreto.

La primera no prueba la segunda.

## Pregunta E — prior art

Buscar específicamente:

- operadores GCD no mínimos con cinco capas;
- el vector relativo `(1,-14,41,-44,16)` o equivalentes por reescala;
- uso de raíces adicionales del operador `H` para cancelar correcciones finitas;
- extracción de `C^2`, Weyl² o Kretschmann de conteos de capas/intervalos causales.

Clasificar cualquier antecedente como exacto, estructural o sólo vecino.

## Frontera de claims

Incluso un `AUDIT_PASS_FORMAL` para el coeficiente medio NO autoriza afirmar:

- convergencia realización-por-realización;
- varianza finita/controlada;
- detector práctico de horizonte;
- Page–Shoom discreto;
- reconstrucción de Schwarzschild;
- emergencia del cono causal;
- prioridad/novedad sin auditoría bibliográfica separada.

## Formato de salida exigido

```text
VERDICT = ...

A_ALGEBRA = PASS/FAIL + derivación mínima
B_W2 = PASS/FAIL/CONDITIONAL + hipótesis
C0_GLOBAL_FINITUDE = PASS/FAIL/REGULATED_ONLY + prescripción exacta
C_W1_COEFFICIENT = PASS/FAIL/UNRESOLVED + valor si existe
D_COVARIANT_STRUCTURE = PASS/FAIL/CONDITIONAL
E_PRIOR_ART = EXACT_FOUND / STRUCTURAL_ONLY / NONE_FOUND_IN_SCOPED_SEARCH

MAXIMUM_SURVIVING_CLAIM = ...
FATAL_ISSUES = ...
REQUIRED_FIXES = ...
```

**No merge y no simulación hasta veredicto independiente.**
