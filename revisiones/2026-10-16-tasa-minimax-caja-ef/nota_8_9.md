# Afirmaciones a revisar: mezcla Poisson, cotas de Fisher y tasa minimax en una caja EF

## 1. Modelo y resultados aceptados (dados; no se pide revisarlos)

Caja B = [0,T] × [r_a, r_b] en coordenadas Eddington–Finkelstein ingoing (v, r) de
Schwarzschild 1+1D, con L = r_b − r_a. El parámetro es τ = 2M ∈ K, con K ⊂ (r_a, r_b)
un intervalo compacto. Coordenadas nulas: v y u_τ(v,r) = −e^{−v/(2τ)} W_τ(r), con
W_τ(r) = e^{r/τ}(r/τ − 1). El orden causal es el orden producto en (u, v). Dados n
puntos i.i.d. uniformes en B, Π_n ∈ S_n es la permutación entre el orden en u y el orden
en v, con probabilidades π_σ(τ) > 0 que son C¹ (y C²). El poset sin etiquetas es
imagen fija de Π_n. s_n = (√π_σ)_σ e I_n^Π = Σ π_σ'²/π_σ = 4‖ṡ_n‖².

Aceptados:
- (A) I_n^Π(τ) ≤ n J(τ), con J continua y finita en K.
- (B) sup_K ‖s̈_n‖ ≤ C_K n.
- (C) TV(L_τ(Π_n), L_{τ+δ}(Π_n)) ≤ (|δ|/2) √(n J̄), con J̄ = sup_K J, y lo mismo para
  el poset. De ahí una cota inferior de dos puntos de orden 1/√(n J̄) para todo
  estimador basado solo en el orden.

## 2. Afirmaciones nuevas

**D (mezcla de Poisson).** Sea N ~ Poisson(Λ), con Λ = λTL independiente de τ (√−g = 1 en
(v, r)), y dados N = n, los puntos como en §1. Se observa (N, Π_N). Con pesos
w_n = e^{−Λ}Λⁿ/n! y S = (√w_n s_n)_n se afirma:
(1) I^Pois = Σ w_n I_n^Π ≤ ΛJ;
(2) S es C¹ en ℓ² y ‖S(τ+h) − S(τ) − hṠ‖ ≤ (h²/2) C_K √(Λ+Λ²), luego la mezcla es QMD
    uniformemente en K;
(3) TV = Σ w_n TV_n ≤ (|δ|/2) √J̄ E√N ≤ (|δ|/2) √(J̄Λ).
Argumento: los bloques con distinto n tienen soportes disjuntos y el mismo peso para
todo τ. Las cotas Σ w_n sup‖ṡ_n‖² ≤ J̄Λ/4 y Σ w_n sup‖s̈_n‖² ≤ C_K²(Λ+Λ²) justifican derivar
término a término y aplicar el teorema fundamental del cálculo. Para (3) se usa Jensen.

**E (cota inferior lineal de Fisher).** Sea p(τ) la probabilidad de que dos puntos estén
relacionados (la identidad para n = 2), y sea U_n la fracción de pares relacionados, que
es un U-estadístico y función de Π_n. Se afirma: I_n^Π ≥ n p'(τ)²/(4p(1−p)).
Argumento: por Hoeffding, Var U_n = C(n,2)^{−1}[2(n−2)ζ_1 + ζ_2] ≤ 4p(1−p)/n, ya que
ζ_1 ≤ ζ_2 = p(1−p). Además d/dτ E U_n = Cov(U_n, score) ≤ √(Var U_n · I_n^Π).

**F (cota superior).** Si p es C¹ y estrictamente monótona en K con m = min_K |p'| > 0, el
estimador τ̂ = p^{−1}(clip_{p(K)} U_n) cumple sup_K E|τ̂ − τ| ≤ 2 sup_K √(p(1−p)) / (m√n).
Argumento: p^{−1} es 1/m-lipschitziana, el recorte no aleja, y se aplica Cauchy–Schwarz.

**G (monotonía).** Para cada par fijo de puntos de B, el indicador "relacionados" es no
creciente en τ. Además −p'(τ) ≥ c(τ) > 0, con
c(τ) = L^{−2} ∬_{τ<r_1<r_2<r_b} (2/T)(1 − Δφ/T)_+ (γ(r_2) − γ(r_1)) dr_1 dr_2,
φ_τ(r) = 2τ log|W_τ(r)| = 2r + 2τ log(|r−τ|/τ), Δφ = φ(r_2) − φ(r_1) y γ = ∂_τ φ. Como c es
semicontinua inferiormente, m ≥ min_K c > 0.
Argumento: con Δv = v_2 − v_1 > 0, la relación equivale a W(r_1) e^{Δv/(2τ)} > W(r_2).
- Exterior–exterior: equivale a Δv > Δφ. Si r_2 > r_1, ∂_τΔφ = γ(r_2) − γ(r_1) > 0,
  porque γ'(r) = 2/(r−τ) + 2τ/(r−τ)² > 0, así que el umbral sube. Si r_2 ≤ r_1, se
  cumple siempre.
- Interior–interior: equivale a Δv < φ(r_2) − φ(r_1) si r_2 < r_1, y no se da si
  r_2 ≥ r_1. Aquí γ_int'(r) = 2r/(τ−r)² > 0, así que el umbral baja.
- Exterior antes que interior: siempre relacionados.
- Interior antes que exterior: nunca relacionados.
- Cruces del horizonte (τ = r_k): φ → −∞ en el horizonte, y en cada cruce el indicador
  es continuo o pasa de 1 a 0.
La cota de c se obtiene de los pares exteriores con r_2 > r_1 > τ + h que dejan de estar
relacionados, dividiendo por h y aplicando Fatou; p es C¹ porque es π_id con n = 2.

**H (tasa minimax).** Por G, F se cumple sin condiciones; con C, la tasa minimax de
localización basada solo en el orden en K es n^{−1/2}:
c_1/√(n J̄) ≤ inf_τ̂ sup_K E|τ̂ − τ| ≤ 2 sup_K √(p(1−p)) / (m√n).
Lo mismo vale con Λ en el protocolo Poisson.

## 3. Comprobación numérica ya hecha (r_a = 0.1, r_b = 1.3, T = 6)

- p decrece en τ ∈ [0.15, 1.25], con p' ∈ [−0.73, −0.43] y |p'|/se > 300.
- En 2·10⁶ pares y 116 valores de τ, el indicador nunca pasa de 0 a 1.
- 0 < c(τ) ≤ −p'(τ) en los 23 puntos de la malla (c va de 0.70 a 0.017).
- p'²/(p(1−p)) en τ = 0.5 vale 1.425; el Monte Carlo independiente de I_2^Π da 1.421.
- Monte Carlo de I_n^Π (n ≤ 4): está entre la cota de E y nJ.
