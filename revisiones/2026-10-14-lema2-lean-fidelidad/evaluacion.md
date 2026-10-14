# Evaluación de la revisión ciega del lema 2 en Lean (gpt-6-astra, esfuerzo high)

Fecha: 2026-10-14. Evaluador: Claude Opus 5.5, que escribió `Monotonicity.lean` y el encargo (no es
evaluación independiente). Herramienta: revision-ciega @ ~/herramientas c12c10e. Documentos
enviados: extracto del certificado (25a2a73), `formal/TAREA_LEMA2_CODEX.md` (9fd2c6d) y
`formal/NachoFormal/Monotonicity.lean` (dc52599). Una ronda.

**Veredicto del revisor:** fiel con salvedades enumeradas. No encuentra ninguna hipótesis que deje
vacíos los teoremas en sus usos causales.

## Contra la expectativa previa

| | Detectado | Comprobación |
|---|---|---|
| E1 pares sin relación causal: `τ = 0` por convenio, la cota superior no está enunciada | sí (§3) | correcto; el ejemplo `x=(0,1)`, `y=(1,0)` lo ilustra |
| E2 `BddAbove` como hipótesis; no vacío redundante | sí (§1, §2) | correcto; además nota que con `q` continua el caso no acotado no ocurre (Cauchy–Schwarz en el rectángulo), sin formalizar |
| E3 composición en dos pasos con hipótesis en el punto intermedio | sí (§2) | composición escrita explícitamente para las dos cotas; comprobada a mano contra los enunciados de `tau_mono_left/right` |
| E4 dominio `UV < 1` frente a `q` global | sí (§3) | correcto, y da el argumento: `UV` es bilineal, sus extremos en el rectángulo están en las esquinas, y las esquinas mixtas con producto positivo quedan por debajo de una de las de `a` o `b`. Comprobado a mano |
| E5 clase de curvas de H1, no gráficas `U(V)`; sin lema 3 no dice nada de `Delta_max` | sí (§1, §4) | correcto |
| E6 `capped_mono` en `[0,∞)`; falta `tau_nonneg` | sí (§2) | correcto; añade que el tope `min(π,·)` no necesita no negatividad |
| E7 la triangular inversa no se formaliza | sí, y más (§4) | ver abajo |

## Objeción no prevista, válida: el paso 2 del certificado es falso tal como está escrito

El certificado (`B2_path2_gate_certificate.md`, líneas 54-55) dice: «si `z` está en el futuro causal
de `x`, la concatenación da `τ(x,y) >= τ(x,z) + τ(z,y) >= τ(z,y)`». Falta la hipótesis `z ≤ y`.
Contraejemplo del revisor con `q ≡ 1`: `x=(0,0)`, `y=(1/4,1/4)`, `z=(1/2,1/2)`. Con `q ≡ 1`,
`τ(a,b) = sqrt(ΔU ΔV)` para `a ≤ b` (Cauchy–Schwarz, alcanzada por el segmento), así que
`τ(x,y) = 1/4`, `τ(x,z) = 1/2`, y `τ(z,y) = 0` porque `z ≰ y` (convenio habitual `τ = 0` fuera del
futuro causal; es también el de Lean). La desigualdad diría `1/4 >= 1/2`. **Comprobado a mano.**

Alcance: es una errata de enunciado, no del número. Los dos usos del paso 2 (cotas por esquinas)
tienen siempre el punto intermedio entre los extremos (`x ≤ P_top ≤ Q_bot ≤ y` para la inferior;
para la superior, `P_bot ≤ x ≤ y ≤ Q_top`, o el par no causal con `τ(x,y) = 0`), y el fichero Lean
no enuncia la versión aditiva. Corregir el texto del certificado (añadir «y `z ≤ y`») toca un
objeto promocionado: lo decide el PI.

## Otras observaciones del revisor, correctas

- La constante Lipschitz común no restringe la clase (sirve el máximo), y `K` depende de cada
  curva (`IsCausalCurve.lip` es un `∃ K` por curva).
- `_hab` es redundante con `hne`: una curva testigo monótona fuerza `a ≤ b`.
- `q ≡ 0` está admitida (generalización degenerada); la positividad estricta del `q` físico queda
  por comprobar fuera del fichero.

## Lectura

Detecta E1-E7, con argumentos correctos al comprobarlos, y una errata real del certificado que la
expectativa no previó. No hay errores matemáticos ni literatura citada.

Los enunciados en Lean son fieles al encargo. Para cerrar la distancia con el paso 2 del
certificado faltan, fuera de este fichero: (1) la rama de pares no causales de la cota superior;
(2) `tau_nonneg` y las cotas `BddAbove` (Cauchy–Schwarz); (3) la extensión de `q` desde `UV < 1`;
(4) el lema 3 (`Delta_max = τ`). Ninguno impide fusionar el PR #12 si el README sigue diciendo lo
que formaliza y lo que no.
