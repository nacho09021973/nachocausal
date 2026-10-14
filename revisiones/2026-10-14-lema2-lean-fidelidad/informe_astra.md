<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ c12c10eb4de36669f2048754d2df20a9747adf1f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 d4f0628a26b0e2ed64c6bd6312fb2b767a773037127a0384c8eea40872c47013; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.162.1)
inicio: 2026-10-14T08:29:13Z  fin: 2026-10-14T08:30:45Z
documento: /home/ignac/nachocausal/.worktrees/lean-b2-lema2/revisiones/2026-10-14-lema2-lean-fidelidad/extracto_certificado_B2.md ; último commit observado: 25a2a73 ; sha256 de la copia enviada 832452908377c5483383c02123b600cedf1f64117083f8a3272421a4ae4e8981
documento: /home/ignac/nachocausal/.worktrees/lean-b2-lema2/formal/TAREA_LEMA2_CODEX.md ; último commit observado: 9fd2c6d ; sha256 de la copia enviada 6f88a94143721c218f62c4c4b03e06c757670fd38d6347f0da8ec1b62cb3ffc6
documento: /home/ignac/nachocausal/.worktrees/lean-b2-lema2/formal/NachoFormal/Monotonicity.lean ; último commit observado: dc52599 ; sha256 de la copia enviada 77fdfa896761296aa612935b2d0e669fccf8f0aab7cd569b4a940d6486a2c121
entrada_astra.txt sha256 350c4cf8fc91fa8ec0c60df0b82308fcc1b4dcd856b8274969806443f6008f44
respuesta sha256 a2d02c2996fa307d3136de052e70c952c268994b87a9a876be62972b8bbc9997
-->

**1. Definiciones.**

- **`IsCausalCurve`: fiel con salvedad.** El orden producto corresponde exactamente a `dU ≥ 0`, `dV ≥ 0` de H1. La regularidad coincide con la parametrización Lipschitz que H1 utiliza, pero no incluye la restricción espacial `UV < 1`.
- **`L`: fiel con salvedad.** Para `q ≥ 0`, el elemento de longitud de la métrica escrita en el certificado es `q(UV)√(U'V')`. `integrable_of_causal` evita que la integral totalizada de Lean oculte una falta de integrabilidad bajo `Continuous q`.
- **`lengths`: fiel con salvedad.** Recoge exactamente las longitudes de las curvas definidas en el fichero. Su identificación con las gráficas absolutamente continuas de H1 queda pendiente del lema 3, expresamente excluido.
- **`tau`: fiel con salvedad.** Es la separación temporal finita cuando `lengths` está acotado. Para el conjunto vacío, el valor `0` es el convenio habitual adecuado; para un conjunto no acotado, el valor `0` **no** representa una separación infinita.

Precisiones:

La constante común de Lipschitz no restringe adicionalmente la clase: dadas dos constantes, sirve su máximo. Además, `K` depende de cada curva; no se impone una cota uniforme a todas.

El uso de `deriv`, aunque las funciones estén definidas arbitrariamente fuera de `[0,T]`, es correcto: en el interior las componentes son diferenciables casi por doquier; los extremos no afectan a la integral. Para `T = 0`, los extremos coinciden y la longitud es cero.

Bajo continuidad global de `q`, el caso no acotado no ocurre: toda curva queda en el rectángulo de sus extremos; allí `|q(UV)| ≤ M`, y Cauchy–Schwarz da
\[
L\le M\sqrt{\Delta U\,\Delta V}.
\]
Esto es una justificación matemática de la acotación, **no un resultado formalizado en este fichero**, y está expresamente fuera del encargo.

**2. Composición de los teoremas.**

Escribo `N(a,b)` para `(lengths q a b).Nonempty` y `B(a,b)` para su `BddAbove`. Todos los usos requieren `hq0` y `hqc`.

Supongamos las relaciones de esquinas
\[
P_{\rm bot}\le x\le P_{\rm top},\qquad
Q_{\rm bot}\le y\le Q_{\rm top}.
\]

Para la **cota inferior**, suponiendo además `P_top ≤ Q_bot`:
\[
\tau(P_{\rm top},Q_{\rm bot})
\underset{\texttt{tau\_mono\_left}}{\le}
\tau(x,Q_{\rm bot})
\underset{\texttt{tau\_mono\_right}}{\le}
\tau(x,y).
\]

- Primer uso: `a'=x`, `a=P_top`, `b=Q_bot`; exige `N(P_top,Q_bot)` y `B(x,Q_bot)`.
- Segundo uso: `a=x`, `b=Q_bot`, `b'=y`; exige `N(x,Q_bot)` y `B(x,y)`.

Las relaciones causales necesarias se deducen de la cadena
`x ≤ P_top ≤ Q_bot ≤ y`.

Para la **cota superior**, cuando `x ≤ y`:
\[
\tau(x,y)
\underset{\texttt{tau\_mono\_left}}{\le}
\tau(P_{\rm bot},y)
\underset{\texttt{tau\_mono\_right}}{\le}
\tau(P_{\rm bot},Q_{\rm top}).
\]

- Primer uso: `a'=P_bot`, `a=x`, `b=y`; exige `N(x,y)` y `B(P_bot,y)`.
- Segundo uso: `a=P_bot`, `b=y`, `b'=Q_top`; exige `N(P_bot,y)` y `B(P_bot,Q_top)`.

Cada `N(a,b)` se obtiene de `a ≤ b` mediante `segment_is_causal` y la definición de `lengths`. Recíprocamente, la monotonía de cualquier curva testigo implica `a ≤ b`. Por tanto, las hipótesis `_hab` son redundantes con `hne`, pero inocuas.

Las hipótesis `B` requieren la cota externa. El encargo lo declara explícitamente; H1 menciona continuidad en compactos y Cauchy–Schwarz aparte. **El extracto no verifica por sí solo esas obligaciones para el `q` concreto y todos los pares utilizados**: esa descarga permanece `[UNVERIFIED]`.

Para el tope, cada desigualdad `u ≤ v` implica directamente
`min π u ≤ min π v`, por monotonía de `min`; no hace falta no negatividad.

Para `p`, `capped_mono` exige `0 ≤ u` y `0 ≤ v`; basta `0 ≤ u`, pues `u ≤ v`. Los corolarios `capped_tau_mono_left/right` permiten repetir exactamente las composiciones anteriores. Sus hipótesis adicionales son:

- cota inferior: no negatividad de `τ(P_top,Q_bot)` y de `τ(x,Q_bot)`;
- cota superior: no negatividad de `τ(x,y)` y de `τ(P_bot,y)`.

La segunda de cada pareja puede heredarse del primer paso. La inicial se obtiene de una longitud testigo, `length_nonneg` y la acotación correspondiente. Falta un lema explícito `tau_nonneg`, pero no falta el argumento.

**3. Casos y posibles vacuidades.**

**Puntos sin relación causal.** Si `¬ x ≤ y`, no existe curva admisible, luego `lengths q x y = ∅` y `τ(x,y)=0`. Los teoremas de monotonía no se aplican: fallan sus hipótesis causales y de no vacío. La cota superior del certificado sigue siendo cierta por `τ(P_bot,Q_top) ≥ 0`, pero necesita esta rama adicional, ausente del fichero.

Ejemplo: celdas puntuales con `x=(0,1)` e `y=(1,0)`. La desigualdad superior es `0 ≤ 0`; ninguno de los dos teoremas permite demostrarla directamente. La condición de la cota inferior, en cambio, garantiza `x ≤ y`.

**Enlaces nulos.** No hay exclusión de `ΔU=0` ni de `ΔV=0`. La componente correspondiente es constante en el intervalo; su derivada es cero en el interior y `L=0`. Así se admiten los enlaces horizontales y verticales de H1. No aparece un teorema separado que declare su longitud cero, pero los teoremas de concatenación y monotonía ya los cubren.

**Dominio.** Falta conectar el `q` físico con una función continua y no negativa en todo `ℝ`. Esto es reparable localmente: para extremos comparables pertenecientes a `UV<1`, todo su rectángulo está en ese dominio. En efecto, los productos positivos se controlan por el extremo superior si ambas coordenadas son positivas y por el inferior si ambas son negativas; los restantes son no positivos. El conjunto de productos es compacto y está separado de `1`; puede extenderse `q` desde ese intervalo mediante truncamiento del argumento. Esa construcción no está formalizada.

**Vacuidad.** No hay hipótesis imposibles en los teoremas generales: `q≡1` proporciona ejemplos no triviales. `q≡0` también está permitido y produce todas las longitudes nulas: es una generalización degenerada, no una métrica lorentziana no degenerada. La positividad estricta del `q` físico queda por comprobar.

**4. Alcance adicional y error del certificado.**

La frase del paso 2, líneas 50–61, es **falsa literalmente**: `x ≤ z` no basta para
\[
\tau(x,y)\ge\tau(x,z)+\tau(z,y).
\]
Falta `z ≤ y`.

Contraejemplo con `q≡1`, dentro de `UV<1`:
\[
x=(0,0),\quad y=(1/4,1/4),\quad z=(1/2,1/2).
\]
Entonces `τ(x,y)=1/4`, `τ(x,z)=1/2` y `τ(z,y)=0`. Los valores se verifican por el segmento diagonal y la cota de Cauchy–Schwarz. La desigualdad afirmaría `1/4 ≥ 1/2`.

El fichero no demuestra esa afirmación incorrecta. Con `x ≤ z ≤ y` y acotación, la versión correcta se deriva de `concat_length` tomando supremos, aunque no está enunciada. Las dos cotas por esquinas no necesitan la versión aditiva.

Además del lema 3 y Cauchy–Schwarz, quedan pendientes la conexión con el dominio físico, la rama no causal y la identificación formal con `h`, cuya definición no aparece en el extracto.

**5. Veredicto global: fiel con salvedades enumeradas.**

Respecto del encargo acotado, los enunciados son adecuados. No constituyen por sí solos una formalización completa del paso 2 literal:

1. El certificado debe corregir la desigualdad aditiva añadiendo `z ≤ y`.
2. Falta conectar el dominio y el `q` físico con los datos globales del fichero.
3. Falta cubrir explícitamente la cota superior para pares no causales.
4. Deben descargarse acotación y no negatividad del supremo, y completar las identificaciones externas con `Delta_max` y `h`.

No detecto una hipótesis que vuelva vacíos los teoremas en sus aplicaciones causales previstas.