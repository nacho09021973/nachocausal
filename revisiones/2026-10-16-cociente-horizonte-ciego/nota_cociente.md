# Afirmación a revisar: cota lineal del Fisher del canal de permutaciones en una caja EF

## 1. Modelo (dado; no se pide revisarlo)

Caja B = [0,T] × [r_a, r_b], 0 < r_a < r_b, L = r_b − r_a. n puntos i.i.d. (V_i, R_i)
uniformes en B, en coordenadas Eddington–Finkelstein ingoing (v, r) de
Schwarzschild 1+1D. El parámetro es τ = 2M, en un compacto K ⊂ (r_a, r_b).
Coordenadas nulas: v y

    u_τ(v, r) = −e^{−v/(2τ)} W_τ(r),    W_τ(r) = e^{r/τ}(r/τ − 1).

El orden causal es el orden producto en (u, v). Π_n ∈ S_n es la permutación que
lleva el orden de los puntos en v a su orden en u_τ, con probabilidades π_σ(τ).
I_n^Π(τ) = Σ_σ π_σ'(τ)² / π_σ(τ).

Hechos ya probados (no se piden): la ley de un punto en (u, v) tiene soporte móvil
S_τ y no es QMD, con H²(p_τ, p_{τ+δ}) ≥ c|δ|; a cada n fijo, π_σ es C¹ y tiene
soporte total en S_n. La cota disponible es factorial, I_n^Π ≲ n!/a_K^n · poly(n).
Un documento previo afirma: "Un mapa dependiente de τ puede fijar el soporte, pero
entonces el canal de orden también depende de τ".

## 2. Afirmación

Para τ ∈ int K, I_n^Π(τ) ≤ n · J(τ), con J(τ) < ∞ continua en K.

## 3. Argumento propuesto

**L1 (lado).** W_τ(r) tiene el signo de r − τ. Por tanto u < 0 si y solo si r > τ:
todo punto exterior precede en u a todo punto interior.

**L2 (orden dentro de cada lado).** Sea J = ext si r > τ e int si r < τ; b_ext = r_b,
b_int = r_a; ε = +1 (ext) o −1 (int); t = |r − τ|, t_b = |b_J − τ|. Se define

    D = 2τ log(|W_τ(b_J)| / |W_τ(r)|) = 2τ log(t_b / t) + 2ε(t_b − t) ≥ 0.

Entonces log|u| = log|W_τ(b_J)| − (D + V)/(2τ). En el exterior (u = −|u|),
u < u' si y solo si D+V < D'+V'. En el interior (u = |u|), u < u' si y solo si
D+V > D'+V'. Con S = D + V:

    φ: orden en u = exteriores por S creciente, después interiores por S decreciente;
       orden en v = orden de V.

φ no depende de τ y Π_n = φ((J_i, D_i, V_i)_{i ≤ n}).

**L3 (ley).** V es uniforme en [0,T] e independiente de (J, D). Como
|dD/dr| = 2r/|r − τ|, la densidad de (J, D) respecto de (conteo × Lebesgue) en
{int, ext} × [0, ∞) es

    f_τ(j, d) = t / (2L (τ + ε t)),   donde t = t_τ(j, d) resuelve
    t e^{ε t/τ} = t_b e^{ε t_b/τ} e^{−d/(2τ)}.

El soporte es fijo. La cola en d → ∞ (horizonte) es exponencial, t ≈ C(τ) e^{−d/(2τ)}.

**L4 (regularidad).** G(t, τ, d) = log t + εt/τ − log t_b − ε t_b/τ + d/(2τ) = 0, con
∂G/∂t = 1/t + ε/τ > 0 (en el interior t < τ − r_a < τ). Por el teorema de la
función implícita, t_τ(d) es C^∞ en τ. El score ∂_τ log f_τ(j, d) es O(1 + d)
uniformemente en K, así que J(τ) = E[(∂_τ log f)²] < ∞ y es continua. Con √f C¹
en τ y J continua, la familia de un punto (J, D, V) es QMD (resultado estándar,
p. ej. van der Vaart, *Asymptotic Statistics*, lema 7.6, por comprobar).

**L5 (data processing).** π_σ(τ) = E_τ[1{φ(X) = σ}] con X = (J_i, D_i, V_i)_i i.i.d.
Derivando bajo la integral (dominación uniforme en K por L3 y L4),
π_σ' = E[A_n 1{φ(X) = σ}] con A_n = Σ_i ∂_τ log f(J_i, D_i). Por Cauchy–Schwarz,
π_σ'²/π_σ ≤ E[A_n² 1{φ(X) = σ}]. Sumando en σ, I_n^Π ≤ E[A_n²] = n J(τ).

**Compatibilidad con el no-QMD de un punto.** (J, D, V) es una función de (v, r)
que depende de τ y no es función de (u, v) por un mapa independiente de τ. La
ley de (u, v) puede ser no regular y la de (J, D, V) regular. Π_n es función fija
de la segunda.

## 4. Comprobación numérica ya hecha (sobre r ∈ [0.1, 1.3], v ∈ [0, 6])

- φ reproduce Π_n en 600 000 muestras con n = 6 y τ ∈ {0.4, 0.5, 0.7}, con 0 discrepancias.
- J(0.4, 0.5, 0.7) = 5.52, 4.38, 3.49 por cuadratura. E[score] ≈ 5·10⁻⁹. El score
  implícito coincide con el de diferencias finitas hasta 5·10⁻⁸.
- Monte Carlo (2·10⁷ conjuntos) de I_n^Π para n = 2, 3, 4: entre 0.15 y 0.31 veces n·J.
