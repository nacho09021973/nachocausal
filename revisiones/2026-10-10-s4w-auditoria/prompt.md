# Encargo: revisión ciega de una auditoría matemática

---

Eres revisor externo de una **auditoría** matemática, no del trabajo original. El objeto que
revisas es `S4W_5LAYER_INDEPENDENT_AUDIT_2026-10-10.md` (rev. 2). Adjuntos van también el
documento auditado (`S4W_5LAYER_KRETSCHMANN_CANDIDATE.md`) y la fuente de la que depende el
cambio más importante de la rev. 2 (la tesis de máster de C.-D. Pfeiffer, 2022).

Contexto mínimo: en teoría de conjuntos causales, el operador de d'Alembert discreto `B` tiene
límite continuo `□ − R/2`. El documento auditado propone un operador de cinco capas dentro de
la familia GCD y, a partir de él, un estimador del escalar de Kretschmann `C_abcd C^abcd`. La
auditoría concluye `AUDIT_REQUIRES_MAJOR_FIX`.

## Objetivo

Decidir si la auditoría es correcta, y en particular si sus **dos pasos de juicio** se
sostienen. Son los dos únicos puntos donde la auditoría no se apoya en una cita literal sino en
una inferencia propia, y por eso se someten a otra familia de modelos.

**J1 — ¿rompe `U_y` el argumento de estructura covariante?** (§5 de la auditoría, pregunta D).
La afirmación auditada es: por covariancia, dimensiones y paridad, una corrección local escalar
de dimensión cuatro en vacío queda restringida a `C_abcd C^abcd`. La auditoría concede que eso
es cierto para escalares construidos covariantemente a partir de la métrica sola, pero sostiene
que es **falso** para el objeto que esta construcción produce, porque el desarrollo arrastra una
dirección temporal privilegiada `U_y` del intervalo causal, y `W = T_abcd U^a U^b U^c U^d`
(densidad de superenergía de Bel-Robinson) es un escalar de dimensión cuatro en vacío que no se
expresa mediante `C^2`. ¿Es correcto ese razonamiento, o hay una vía por la que la integral
sobre el cono devuelva algo invariante y la objeción se disuelva?

**J2 — ¿es legítima la hipótesis (h3)?** (§2.3 de la auditoría). Pfeiffer obtiene, aplicando el
operador `O_d = O_{2n}` a la región del cono, un factor `A_{λ,l}(n) = Π_{j=0}^{n} (d(l−λ)+2j+2)`
con `λ = l + (2/d)(l+1)`, y lo usa **siempre** con `n = ⌈d/2⌉`, que es el operador minimal de
cada dimensión. La auditoría lee esa misma `n` como el **número de raíces del operador**,
desacoplado de la dimensión, y concluye que el operador de cinco capas en `d=4` (cuatro raíces,
`n=3`) aniquila un término más y baja la contribución de la región del cono de `O(ρ^{−1/2})` a
`O(ρ^{−1})`. De ese paso cuelga la revocación de la objeción F2 y el que la línea pueda
reabrirse. ¿Es legítimo? ¿Depende la derivación de `A` de que `n` esté atado a `d` por alguna
vía que la auditoría no haya visto (la medida, el `λ`, la normalización, el rango de `l`, la
validez de la expansión (3.7) del volumen)?

## Qué más atacar si ves fallo

No te limites a J1 y J2. En particular, comprueba por tu cuenta:

- que `2032 E² + 360 H² = 82K + 1376W` con `K = 8(E² − B²)`, `W = E² + B²`, `B² = H²/2`;
- que con `λ = l + (2/d)(l+1)` se tiene `d(l−λ) = −2(l+1)` y por tanto `A = 0 ⟺ l ≤ n`;
- si la objeción F1 (que `ln(ρ)·ρ^{−1/2}` no es `o(ρ^{−1/2})`, y que por tanto la forma
  funcional reclamada es incompatible con el resto log-realzado de la región cercana) está bien
  planteada o si el mismo factor `A` también la limpia;
- si el veredicto global debería ser otro de los cuatro admisibles.

Si encuentras un error en la **auditoría**, dilo con el mismo detalle que si lo encontraras en el
documento auditado. Un `PASS` del auditor sostenido sobre un error es peor que un `FAIL`.

## Resultado esperado

Un informe en prosa seca, sin preámbulo, con esta forma al final:

```
J1_VEREDICTO = CORRECTA | INCORRECTA | NO_CONCLUYENTE   + por qué, en tres líneas
J2_VEREDICTO = LEGITIMA | ILEGITIMA | NO_CONCLUYENTE    + por qué, en tres líneas
VEREDICTO_GLOBAL_DE_LA_AUDITORIA = CONFIRMADA | CONFIRMADA_CON_CORRECCIONES | REFUTADA
DEFECTOS_ENCONTRADOS = lista, o NINGUNO
```

## Condiciones

- **Una sola ronda.** No hay réplica ni segunda vuelta.
- **Cierra el encargo** la emisión de los cuatro campos de arriba con sus razones. Si no puedes
  decidir J1 o J2 con lo adjunto, `NO_CONCLUYENTE` y di exactamente qué falta; eso también cierra.
- Sesión sellada: no tienes herramientas, ficheros ni web. Todo lo que puede contar como fuente
  está adjunto. **No cites nada que no esté adjunto**; si necesitas un resultado externo, dilo
  como laguna en vez de reconstruirlo de memoria.
- No reescribas la auditoría ni propongas redacción. Juzga.

---
