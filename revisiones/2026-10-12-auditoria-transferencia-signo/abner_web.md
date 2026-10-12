# ABNER (DeepSeek) — auditoría por la interfaz web, 2026-10-12

Consulta hecha por el PI en chat.deepseek.com con el prompt `abner_prompt_web.md` (mismo acta y
adjuntos que CIRO, sellado por instrucción). Por la API, los dos intentos agotaron el timeout de
900 s (`sanedrin.log.log`). **Procedencia:** no es la API, el modelo exacto no queda registrado y
el sellado solo se pidió por instrucción, sin que se pueda comprobar. Respuesta transcrita literalmente:

---

**Auditoría ABNER — transferencia del signo de B2 al punto medio real**

**1. Módulo `ω_h`.** La cota cubre los casos degenerados: si un par no es comparable, `T'=0` y el primer término `q_max sqrt(δ(A_max+B_max+δ))` acota `T` porque `|√s−√t| <= √|s−t|` y `A⁺B⁺` se anula. Las dos orientaciones se tratan por separado; `h = p(T_fut)+p(T_past)` con a lo sumo uno no nulo, y la comparación entre pares con distinta orientación se cubre porque cada `T` individual se acota contra cero. `w_f` permanece en `[−1.3500000000000005, 0.6300000000000002]`, donde valen `q_max` (en `w_cap`) y `L_q` (en `s_min`). Usar la misma clase de `f` para ambos pares es legítimo: el `sup` sobre una clase común permite comparar punto a punto y luego tomar supremo. **SE_SOSTIENE.**

**2. `ΔI_f`.** `H_K(x) = ∫_K g h <= ∫_K g = Z`, luego `H_K <= Z_max`. El término `g_max |KΔK'|` cubre el cambio de `K` dentro de `H`: al comparar `H_{K'}(x')` con `H_K(x)`, la diferencia por región es `∫_{KΔK'} g h <= g_max |KΔK'|`, y la diferencia por `x` es `Z_max ω_h`. Los extremos de cada cara se cuentan con `2δ g_max Z_max` por el cambio de límites. La fórmula de `dI` en el script separa correctamente límites, cambio de `g` (`L_G c_max δ Z_max`) y cambio de `H` (`g_max(g_max KD + Z_max ω_h)`). **SE_SOSTIENE.**

**3. `q'` y `G'`.** Con `ds/dw = −1/(s e^s)`, se obtiene `q'(w)=q(1/2+3/(2s))/(s e^s)` y `|G'(w)|=|1−s|e^{−2s}/s`. Todos los factores usados son decrecientes en `s` (o su máximo se toma en `s_min`), por lo que las cotas `L_q` en `s_min` y `L_G` con `e^{−2s_min}/s_min` son válidas. La monotonía de `q` en `w` (creciente) justifica `q_max = q_encl(w_cap)`. **SE_SOSTIENE.**

**4. `Δk` y término de dirección.** `S` es lineal en la dirección porque `v_f(e)` es lineal en `e`. El término de dirección usa `B/Z` como coeficiente de `Σ v_f J_f`: `S = 2Σ v I − 2(B/Z)Σ v J`, y en el código `dS_dir` emplea `Bmax/Zmin`, no `k`. La fórmula de `Δk` es correcta: `|Δk| <= 2(|ΔZ'|/Z_min + |Z'| |ΔZ|/(Z_min Z_lo))`, y la descomposición `|k_m B_m − k_* B_*| <= |Δk| B_max + k_* |ΔB|` es válida. **SE_SOSTIENE.**

**5. Código frente a nota.** Cada fórmula del script coincide con la nota. El redondeo es hacia afuera: `mpmath.iv` y uso de `.a`/`.b`; las constantes escalares se toman en la dirección conservadora (`q_max`, `L_q`, `L_G`, `g_max`). No se usa ningún valor en `m` como si fuera conocido: `Z_min`, `Z_max`, `B_max`, `k_*`, etc., se derivan de las cotas de `lambda*` más los incrementos `dZ`, `dB`, `dZp`. El script verifica el terminal y `M` del JSON de la compuerta y reproduce `S_lo`. **SE_SOSTIENE.**

**Diagnóstico de radio.** `max|d_i| = 1` (componente `u_out` de `L1−L0`), luego `γ(s) = lambda* + s d` está a distancia sup `|s|` de `lambda*`. Para `|s| <= 1e-7`, el punto cae en la bola de radio `1e-7`; la tabla diagnóstica da `S_lower = +0.0005620685 > 0` con dirección fija `d`. Por tanto `rho∘γ` es estrictamente creciente en `|s| <= 1e-7`. El método no alcanza B2.1 por el factor `sqrt(r)` del módulo de `h`, pero como diagnóstico es correcto. **SE_SOSTIENE.**

**Condición de concesión.** Ninguna condición adicional; las hipótesis de la compuerta (H1–H5) y la capa escalar auditada de B1.5 se heredan sin cambios.

**Veredicto: AUDIT_PASS**
