# Encargo: revisión ciega de un resultado POSITIVO que confirma al autor original

---

Revisas `S4W_R6PP_Q2_WEYL_COEFFICIENT_2026-10-10.md`. Van adjuntos los documentos previos
(el no-go retirado, el resultado parcial R6′, la auditoría), la tesis de Pfeiffer 2022 y
**el artículo de Wang (arXiv:1904.01034) completo, en extracción de texto**, de modo que puedes verificar sus ecuaciones
(2), (6), (7)–(8), (11), (76)–(77) y (79) directamente en el original en vez de fiarte de la
transcripción del documento.

Contexto: se auditó un candidato que proponía extraer el Kretschmann `C_abcd C^abcd` de un
operador de cinco capas en conjuntos causales. La auditoría dejó el coeficiente en
`FAIL / NO DETERMINADO` y señaló que el objeto integrado parecía ser `82K + 1376W`, con `W` la
densidad de Bel-Robinson dependiente del observador. Este documento afirma ahora que la pieza
`W` **se cancela exactamente** y que el coeficiente sale `-73 sqrt6/(1575 pi)`, que es
**exactamente** el número que el candidato original había escrito con signo de interrogación.

**Aviso que condiciona el encargo.** En las tres rondas anteriores las revisiones externas
encontraron errores materiales, incluido uno que obligó a retirar un no-go entero. Un
resultado que reproduce al dígito el número que el autor del documento auditado quería obtener
es el caso donde más cabe sospechar de un sesgo de confirmación o de un ajuste inadvertido.
Atácalo con eso en mente.

## Objetivo

Decidir si el resultado es correcto. Cuatro afirmaciones lo sostienen:

**P1 — las dos formas cuárticas.** Con `E`, `B` genéricas (no Schwarzschild):
`int dOmega C^{ga}_{mn}C_{gras}y^m y^n y^r y^s = (8pi/5)W(u^4+u^3v+u^2v^2+uv^3+v^4) + pi K u^2v^2`
y `int dOmega T_{abcd}y^a y^b y^c y^d = (16pi/5)W(u^4+u^3v+u^2v^2+uv^3+v^4)`.
¿Correctas? En particular, ¿es cierto que la parte `W` entra con coeficiente **uniforme** en
los cinco monomios, y que el único exceso no uniforme es `pi K u^2v^2`?

**P2 — el mecanismo de cancelación.** Que `(v-u)^{d-2} = (v-u)^2` tiene coeficientes
`1, -2, 1` que suman cero, luego aniquila cualquier reparto uniforme, y que por eso la parte
dependiente del observador desaparece del canal diagonal. ¿Es legítimo el argumento, o hay
contribuciones al canal `u^3v^3` (o `u^5v^5`) que el documento no haya contado?

**P3 — los dos coeficientes de canal.** `+pi K/180` para la vía (i) y `41 pi^2 K/226800` para
la vía (ii′), con `eps_2` obtenida de la ec. (79) de Wang vía `l_W = sqrt(uv/2)`.

**P4 — el ensamblado.** Que con el `rho^l` dentro del operador, la simetrización `1/2` de
Pfeiffer (3.36) y el jacobiano `1/4`, la suma da `-(105+41)sqrt6/(3150 pi) = -73 sqrt6/(1575 pi)`.

**P0 — la estructura de índices de la ec. (76) de Wang.** El documento interpreta
`C^{ga}_{mn} C_{gras} y^m y^n y^r y^s` como `C_{gamma mu alpha nu} C_{gamma rho alpha sigma}`
contrayendo `gamma` y `alpha`, es decir con las `y` en el **segundo** slot de cada par
antisimétrico. Alega que eso es lo mismo que la estructura de su ec. (6),
`R^gamma_{mu alpha nu} R_{gamma rho beta sigma} x^mu x^nu x^rho x^sigma`, contrayendo
`alpha` con `beta`. **Verifícalo en el original adjunto.** Si la contracción correcta fuera
dentro de un par antisimétrico, la forma sería idénticamente nula y el resultado caería
entero; dilo si es el caso.

## Qué más atacar

- ¿Hay otras combinaciones `(l, alpha+beta)` a orden de curvatura `R^2` que caigan en
  `rho^{-1/2}` y que falten? El documento admite en §6 que ese recuento es suyo.
- ¿Está bien la identificación de `eps_2` como la ec. (79) completa, o Wang mide un volumen
  (ACD entre dos vértices) que no es el `V(x,y)` de Pfeiffer (intervalo causal entre `x` e `y`)?
  Esto es la juntura más delicada del cálculo.
- La rapidez no está acotada en `W1` (`tanh eta = (v-u)/(v+u)`, `gamma -> inf` cuando `u -> 0`).
  ¿Convergen las integrales? ¿Puede el régimen de boost grande estropear la cancelación de §1,
  que es algebraica monomio a monomio pero se aplica bajo una integral?
- ¿Se afirma de más? El §5 declara que siguen prohibidas las afirmaciones sobre varianza,
  convergencia realización-por-realización y horizonte. Dime si el resto del texto lo respeta.

## Resultado esperado

Prosa seca, sin preámbulo, y al final:

```
P0_INDICES_WANG76  = CORRECTA | INCORRECTA | NO_CONCLUYENTE  + por qué
P1_FORMAS_CUARTICAS = CORRECTA | INCORRECTA | NO_CONCLUYENTE  + por qué
P2_CANCELACION      = CORRECTA | INCORRECTA | NO_CONCLUYENTE  + por qué
P3_COEFICIENTES     = CORRECTA | INCORRECTA | NO_CONCLUYENTE  + por qué
P4_ENSAMBLADO       = CORRECTA | INCORRECTA | NO_CONCLUYENTE  + por qué
VEREDICTO_Q2 = CONFIRMADO | CONFIRMADO_CON_CORRECCIONES | REFUTADO
DEFECTOS_ENCONTRADOS = lista, o NINGUNO
```

## Condiciones

- **Una sola ronda.** Sesión sellada: sin herramientas, ficheros ni web. No cites nada que no
  esté adjunto. Si te falta algo, dilo como laguna.
- No reescribas el documento. Juzga.

---
