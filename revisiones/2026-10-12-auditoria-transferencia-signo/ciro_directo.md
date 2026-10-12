# CIRO (grok-4.6) — auditoría sellada directa, 2026-10-12

Llamada directa al CLI con las banderas selladas de sanedrin (sanedrin exige >= 2 miembros). Prompt: acta.md + los 4 adjuntos (grok_prompt.md). timeout 1800 s, rc=0.

**Auditoría CIRO — transferencia del signo B2 (`7bcc087`).** Solo se audita la cota de continuidad nueva; H1–H5, H3 como teorema, H4 y la capa B1.5 no se reabren [SOURCE].

**1. Módulo `ω_h`.** Clasificación: **SE_SOSTIENE**. Condición: parametrización ASTRA ya aceptada en H3 (misma clase de `f`, `∫√f' ≤ 1`).

`|√s−√t| ≤ √|s−t|` vale en `s,t ≥ 0` porque `√s+√t ≥ √|s−t|`. Con `|A−A'|≤δ` y `|B−B'|≤δ`, `|AB−A'B'| ≤ δ(A_max+B_max+δ)` y el primer término acota el cambio del prefactor `√(AB)` por `q_max`. El segundo es la regla de producto con `|w_f−w'_f| ≤ (U_max+V_max+δ)δ` (un extremo se mueve `≤δ` por coordenada; el `+δ` sobra y es holgura). Casos degenerados: si el par deja de ser comparable, algún `A⁺` o `B⁺` cruza cero, luego `min(A,B)≤δ` y `A⁺B⁺ ≤ δ(A_max+B_max+δ)`; el mismo término cubre `T=0` en el cono. Cambio de orientación (futuro↔pasado) exige ambos signos `≤δ`, aún más chico. `min(π,·)` es 1-Lipschitz y `p` es ½-Lipschitz; `h=p(T_fut)+p(T_past)` tiene a lo sumo un sumando no nulo, de modo `|Δh| ≤ |ΔT| ≤ ω_h` (el ½ no se gasta: holgura, no agujero). `w_f` vive en el rectángulo agrandado: `V>0`, extremos de `UV` en las esquinas, rango `[−(u_out+δ)(v1+δ),(u_in+δ)(v1+δ)] ⊂ (−1.351,0.631)` donde valen `s_encl`/`q_encl` (`w_max<1` se afirma). Misma clase de `f` para los dos pares: la clase `{f AC, 0→1}` no depende de los extremos, y `|sup L[f]−sup L'[f]| ≤ sup|L−L'|`.

**2. `ΔI_f`.** Clasificación: **SE_SOSTIENE**. Condición: `h≤1` (definición de `p`).

`H_K(x)=∫_K g h ≤ ∫_K g = Z`. Cambio de dominio de `H`: simétrica `KΔK'` cubierta por las cuatro franjas `2δ(L_v+2δ)+2δ(L_u+2δ)` (esquinas dobles: cota por exceso). Cambio de núcleo con `y` fijo: `Z_max ω_h`. Juntos dan `|ΔH| ≤ g_max|KΔK'| + Z_max ω_h`; el `|KΔK'|` es exactamente el cambio de `K` dentro de `H`. Caras: intersección de segmentos 1D tiene longitud `≤ L` (la original) y simétrica `≤ 2δ`; extremos bien contados. A lo largo de la intersección, `|ΔG| ≤ L_G c_max δ` con `c_max=V_max` en caras `U=const` (`dw=V dU`) y `c_max=U_max` en caras `V=const` (`dw=U dV`). Piezas de `ΔJ_f` análogas sin `H`. `B` solo cambia por dominio (`h` no depende de `K`): `|ΔB| ≤ 2 g_max² |K∪K'| |KΔK'|` cierra.

**3. `q'` y `G'`.** Clasificación: **SE_SOSTIENE**. Condición: capa escalar B1.5 (`s_encl`, `q_encl`, `E_INV_HI`).

De `(1−s)e^s=w` sale `ds/dw=−1/(s e^s)` [SOURCE]. Entonces `G=s e^{−s}` da `G'=−(1−s)e^{−2s}/s`, y `q=2 e^{−s/2}s^{−3/2}` da `q'=q(1/2+3/(2s))/(s e^s)`. Factores de `q'` (q, `1/2+3/(2s)`, `1/(s e^s)`) positivos y decrecientes en `s`; máximo en `s_min=s_encl(w_cap)_lo`. `e^{−2s}/s` decrece para `s>0`; `L_G` toma `max|1−s|·e^{−2 s_min}/s_min` (producto de máximos: válido, ~10 % holgado). `q` creciente en `w` ⇒ `q_max=q_encl(w_cap)_hi`. Constantes del JSON coinciden con la tabla de la nota.

**4. `Δk` y dirección.** Clasificación: **SE_SOSTIENE**. Condición: ninguna nueva.

`I_f,J_f,B,Z` no dependen de `e`; `v_f(e)` es una componente ⇒ `S` lineal en la dirección. Identidad `S(m;d')=S(λ*;d)−[S(λ*;d)−S(m;d)]+S(m;d'−d)` y `k=2Z'/Z` dan `|Δk|≤2(|ΔZ'|/Z_min+|Z'_*| |ΔZ|/(Z_min Z_lo))` y `|Δ(kB)|≤|Δk|B_max+k_*|ΔB|`. El término de dirección usa `2(B/Z)`, con `|I_f|≤L_f g_max Z_max`, `|J_f|≤L_f g_max`, `|v_f|≤EPS` y `L_f` agrandada; **no** usa `k` como coeficiente de `J_f`. Velocidades del término de punto: `|d|` exacto de los binary64, misma `d`.

**5. Código frente a la nota.** Clasificación: **SE_SOSTIENE**, con **MENOR** documental. Condición: el JSON de la compuerta leído es el congelado `7909c0e` (el script afirma `terminal`, `M`, `S_lo` y `lambda_star`; no reescribe `Z`/`B`/`k`).

Fórmulas de `KD`, `KU`, `omega`, `dI`/`dJ`, `dk`, `dS_point` y `dS_dir` son las de la nota. `mpmath.iv` con `.b` en cotas superiores y `S_m.a` / `drho.a` en inferiores; `I()` vía racional exacto. No hay evaluación de `S,Z,B` en `m`. Objetivos: `1/22517998136852480` y `1/18014398509481984`, ambos `≤ 1e-16` [SOURCE]. MENOR: `L_q`/`L_G` de la nota van redondeados al último dígito; la tabla diagnóstica de la nota es subconjunto de `DIAG_RADII` (los valores publicados coinciden); `float(w_max)`+`up` queda cubierto por el `assert Fr(w_cap)≥w_max`.

**Diagnóstico de radio.** Clasificación: **SE_SOSTIENE** como diagnóstico; **no entra en el terminal**. Condición: dirección fija `d`, misma cota.

`max|d_i|=1` (`u_out`: `2.0−1.0`) ⇒ `|s|≤1e-7` cae en la bola sup de radio `1e-7`. Tabla [SOURCE]: `S≥+0.0005621>0` a `r=1e-7`, negativo a `1e-6`. Luego `ρ∘γ` es estrictamente creciente en `|s|≤1e-7`. El `√r` impide B2.1 (`|s|≤0.05`): la nota no lo pretende.

Veredicto: AUDIT_PASS
