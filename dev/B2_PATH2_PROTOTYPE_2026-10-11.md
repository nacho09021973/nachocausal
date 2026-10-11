# B2 — camino 2, prototipo en coma flotante: `S_lo > 0` desde `M = 64`

**Fecha:** 2026-10-11
**Autorizado por:** el PI (elige el camino 2 de cinco).
**Sonda:** `dev/explore_b2_path2_prototype.py`. Coma flotante, **no certificado**. Guardarraíles
intactos.

```text
S_lo(M) = S_inf − a/M,   S_inf = +0.002411,  a = 0.1167
M = 16    S_lo = −0.005061
M = 32    S_lo = −0.001261
M = 64    S_lo = +0.000587      primer M positivo
M = 96    S_lo = +0.001195
M = 128   S_lo = +0.001499      (predicho por el ajuste 64/96: +0.001499)
S_inf coincide con el intervalo ideal [recta, calibración]: +0.002419
```

---

## 1. El esquema que se prototipa

Es el esquema de cotas que usaría el certificado, a nivel de celda y no de punto:

- **Separación temporal ⇒ desigualdad triangular inversa.** Si `x ∈ P` e `y ∈ Q`:
  `P_top <= Q_bot ⇒ Delta(x,y) >= Delta(P_top, Q_bot)` y
  `P_bot <= Q_top ⇒ Delta(x,y) <= Delta(P_bot, Q_top)`.
  Basta concatenar curvas causales futuras. Cada par de celdas queda acotado por **un** par de
  esquinas de la retícula, sin argumentos de monotonía sobre `q` ni `G`.
- **Cota inferior entre esquinas:** el presupuesto de la recta.
- **Cota superior entre esquinas:** `min(inf_c calibración, Cauchy–Schwarz)`.
- **Solo `S_lo`**: `B'_lo` con la cota inferior de `H` en `U=-u_out`, `U=u_in`, `V=v0`
  (`v_n > 0`) y la superior en `V=v1`; `B_hi` con la superior.

**Desviación respecto a lo propuesto, declarada:** el camino 2 decía «colapsar `B` por Fubini».
No hace falta. Gracias a la desigualdad triangular, `B` por pares de celdas cuesta `M^4` consultas
a una tabla `(M+1)^2 × (M+1)^2` de cotas de esquina: 9 s a `M = 128`. Es más simple de auditar
que un colapso analítico y no pierde nada por `p <= a²/4`, porque usa `p` exacta.

## 2. Resultados (`M` celdas por lado, uniformes)

| `M` | `B_hi` | `B'_lo` | `S_lo` |
|---|---|---|---|
| 16 | 0.005840 | 0.004437 | −0.005061 |
| 32 | 0.004855 | 0.006635 | −0.001261 |
| 64 | 0.004412 | 0.007763 | +0.000587 |
| 96 | 0.004271 | 0.008142 | +0.001195 |
| 128 | 0.004202 | 0.008334 | +0.001499 |

`Z = 0.440556`, `Z' = +0.358274` en todas. La pérdida es `O(1/M)`, la de las celdas próximas a
la diagonal, donde la cota de esquinas degenera. El ajuste `S_inf − a/M` sobre `M = 64` y `96`
predice `M = 128` a 1e-6, y su límite (`+0.002411`) es el intervalo ideal medido por otra vía
(`+0.002419`, `dev/B2_NEW_REPRESENTATION_2026-10-11.md` §6). Esa concordancia es el control
principal: dos cálculos independientes del mismo límite.

## 3. Lo que queda para el certificado

Con `M = 128` hay un margen de `+0.0015` para absorber las pérdidas de la capa certificada:

1. **Cotas de esquina con redondeo dirigido.** Recta: cota inferior de una integral 1D de `q` a lo
   largo de un segmento (sumas de Riemann sobre tramos monótonos de `w(tau)`, cuadrático en
   `tau`). Calibración: cota superior de `Phi_c(w_b) − Phi_c(w_a)`, integral 1D. Ambas usan solo
   el enclosure de `s(w)` de B1.5, sin Lambert W. **Para cada `c` la cota es válida, así que la
   rejilla de `c` no necesita certificarse.**
2. **Pesos `W_P`, `Z`, `Z'`** con envolventes de `G`, como `z_bracket` de B1.5.
3. **Sumas** con árbol dirigido.
4. **Memoria:** las tablas densas limitan a `M ≈ 128` (6.9 GB). Para ir más allá: calcular las
   esquinas sobre la marcha o refinar solo cerca de la diagonal, que es de donde viene la pérdida.

Aún no se ha medido cuánto pierde la capa 1 frente al flotante. Ese es el siguiente número.
