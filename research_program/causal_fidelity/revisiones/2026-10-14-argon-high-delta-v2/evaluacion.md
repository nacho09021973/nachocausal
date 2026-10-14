# Evaluación de la revisión del delta v1→v2 (gemini-4-argon, thinkingLevel=high)

Fecha: 2026-10-14. Evaluador: Claude Opus 5.5, que redactó la v2 (no es evaluación independiente).
Herramienta: revision-ciega @ ~/herramientas c12c10e. Documentos enviados: v2 en 505ac49 y el diff
a77d9d8..505ac49 (31bc7b5). Una ronda.

## Contra la expectativa previa

| | Detectado | Comprobación |
|---|---|---|
| F1 inclusión T_IR ⊆ T_caus automática | no explícito | — |
| F2 límites constantes excluyen casos legítimos | sí (T3.3) | argumento correcto: límite aleatorio común (no ergódico) queda fuera |
| F3 τ_caus^IR = 0 en posets densos, pérdida estricta gratis | sí (T3.2) | plausible; afirmado como "demostrado" sin prueba para sprinkling `[UNVERIFIED]` |
| F4 NT3 no ata la diferencia al observable | sí, más fuerte (T2.2.1) | **comprobada a mano**: Q^{D1}=Q^{D2}=2 para todo N, NT1–NT5 se cumplen; el IR no hace trabajo |
| F5 modo "esperanza" mal definido | sí (T2.1) | correcto; además c.s. exige acoplamiento entre N |

## Objeciones no previstas, válidas al leer la v2

- §2.3: D recibe (c,s) pero no d, aunque se dice que comparte el detector.
- σ_N equivariante y determinista no existe si c tiene automorfismos que no fijan ningún par s≺d.
- "Sin par" deja Q fuera de dominio; con modo esperanza y τ=∞ asignado, E[Q]=∞ y NT1 imposible.
- A no se exige equivariante ni sin bloqueos, ni que conecte s con d.
- Incumplir NT4 / NT1 por A degenerado da `FAIL` según §1; debería ser inadmisible (`OPEN`), no `FAIL`.
- §5 llama semirrecta a [∞,∞)=∅; la equivalencia de §6 sólo vale bajo NT1 (falta decirlo).
- λ: falta declarar codominio (≥1 si s≺d y λ es longitud de cadena, pero el contrato no lo fija);
  τ_caus sin la convención min ∅ = ∞.

## Lo que no se adopta sin comprobar

- T4: que en el control de contrato los Q finitos difieren en Θ(N^{-1/2}) para θ≠1/2 (TCL para el
  tiempo de alcance con varianzas asintóticas distintas). Plausible, `[UNVERIFIED]`. Si es cierto,
  el control de contrato sobrevive a NT3' con θ≠1/2; con θ=1/2 la diferencia sería de orden menor.
- NT3' tal como lo propone (Ω(N^{-α}), "no atribuible a un retraso de O(1) pasos") es vago; la idea
  útil es exigir la diferencia en Q a N finito y no sólo en la curva Δ.

## Lectura

La v2 cierra 10 de 15 filas de §10; 4 parciales, 1 no cerrada (NT4 clasificado como FAIL). Hay un
PASS trivial nuevo y correcto (F4) y un PASS barato plausible en posets densos (F3). La v2 no puede
congelarse así: hace falta una v2.1.
