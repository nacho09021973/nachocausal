---
name: frente-2p1-ecuatorial
description: Frente 2+1D ecuatorial (abierto 2026-10-12): banco de estimador order-only del horizonte; lema E1; fase A (generador) cumplida; fase B pendiente de firma
metadata:
  type: project
---

**Abierto por el PI el 2026-10-12** (`docs/acta_frente_2p1_ecuatorial_2026-10-12.md`, firmado
§9.1 y §9.2), tras ver que el puente 3+1D no tiene estimador: B3 da negativo para `n=2` y B4/`n=3`
falla la compuerta de viabilidad. Es un banco **intermedio** hacia 3+1D, no un sustituto.

- **Lema E1** (`research_program/puente_3p1/2026-10-12/E1_equatorial_restriction_lemma.md`): el
  orden causal de Schwarzschild 3+1D restringido al ecuador es el de la métrica 2+1D inducida.
  Se hereda el núcleo `Delta_max`; cambian el peso (`e^{-s}`) y la ley angular (`b/π`).
  ASTRA dio pase condicional; la condición (degenerados y alcanzabilidad del `sup`, válido en
  parches rectangulares) está atendida.
- **Fase A cumplida** (`60a071c`). `dev/gen2p1_equatorial.py` genera en 4.7 s con `N = 1e4` y en
  ~15 s con `N = 2e4`. La etapa 3 es la geodésica por disparo en `(U, V)`, parametrizada por la
  coordenada que más avanza; la de `c` constante falla fuera del horizonte. Controles:
  transitividad, auditoría frente al disparo exacto y mutación.
- **Fase B en curso (2026-10-12):** generador sobre la caja EF alta (`6e19328`, coincide exactamente con la relación sellada de 1+1D en pares con el mismo ángulo). Estimador-v2 portado (`e1ea1f5`): con T=6 la horquilla queda sesgada hacia fuera (r≈0.53, horizonte efectivo por el corrimiento al rojo finito) y cubre 0/5; con T=12 cubre 3/3; Minkowski se abstiene siempre. T tiene que fijarse por una regla de principio en prereg-004. Bandas 2+1D: exploración 7_000_000..7_000_999 y virgen 8_000_000..8_999_999.
- **Semillas de la fase A, quemadas:** 1, 2, 3, 4, 7, 99 y 12345.

**Why:** «encontrar el horizonte» exige un estimador con `N` finito fuera de 1+1D, y el puente
3+1D no lo da.

**How to apply:**
- La siguiente fase es la B: el estimador en `dev`, partiendo del estimador-v2 de 1+1D, con una
  banda de semillas nueva y disjunta. Necesita la firma del PI (acta §9.3).
- Después vienen prereg-004 (umbrales y semillas vírgenes sellados, con `/comite` antes) y una
  sola ejecución ciega.
- No afirmar nada de 3+1D ni de Einstein en 2+1D.

Relacionado: [[puente-3p1-b2-gate]], [[prereg002-pass-artifact-gap]], [[gpu-exploration-backend]].
