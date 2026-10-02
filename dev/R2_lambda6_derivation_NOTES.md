# R2 — derivación de `κ ~ λ⁶` y de su prefactor

```text
ESTADO: EXPONENTE Y PREFACTOR DERIVADOS / VERIFICACIÓN SIMBÓLICA Y NUMÉRICA INTERNA
FECHA_DE_CIERRE_ANALITICO: 2026-08-26
ALCANCE: R2 de docs/program_reopening_note_2026-07-31.md
NATURALEZA: dev/ — derivación interna; no es auditoría independiente ni afirmación de novedad
```

El ítem R2 partía del ajuste empírico `κ ~ λ⁶` de
`research_program/work_packages/wp4_fisher_localization_floor.md` §5a (exponentes 5.917 y
5.988). La expansión inicial identificó el mecanismo `V ~ λ²`, `I ~ λ⁴`, pero dejó el
prefactor abierto porque una expansión puntual en `τ=1` no era uniforme al derivar respecto de
`τ`. La expansión emparejada correcta, con `σ=(τ-1)/λ` fijo, cierra ese hueco.

## 1. Familia y resultado

Considérese la familia algo más general

```text
τ = 1 + λσ,
r_p = 1 + aλ,     r_q = 1 - aλ,
v_p = 0,          v_q = bλ,
```

con `a,b>0`, y evalúese Fisher en `τ=1` (`σ=0`) manteniendo las esquinas físicas fijas al variar
`τ`, exactamente como hace el barrido numérico. Entonces

```text
I_λ(1) = [b²(4a-b)²/576] λ⁴ + O(λ⁵),
V_λ(1) = 2ab λ² + O(λ³),
κ_λ(1) = V_λ(1) I_λ(1)
       = [a b³(4a-b)²/288] λ⁶ + O(λ⁷).
```

Para la forma realmente escaneada, `a=b=0.3`, esto se reduce a

```text
I_λ(1) = (a⁴/64) λ⁴ + O(λ⁵),
κ_λ(1) = (a⁶/32) λ⁶ + O(λ⁷)
       = 2.278125e-5 λ⁶ + O(λ⁷),
δ_τ/ell ~ sqrt(32)/a³ · λ⁻³ = 209.51… λ⁻³.
```

**Excepción que no debe borrarse.** Si `b=4a`, el prefactor mostrado se anula. La derivación no
autoriza `κ ~ λ⁶` para esa forma afinada: allí el primer término no nulo está a orden superior y
queda sin calcular. El resultado `λ⁶` es válido para la familia escaneada y, más generalmente,
para `b != 4a`; no es una ley universal sobre todo el espacio de formas.

## 2. Expansión uniforme

La coordenada nula saliente y su inversa exacta son

```text
Ũ_τ(v,r) = -exp[-v/(2τ)] exp(r/τ)(r/τ-1),
r_τ(Ũ,v) = τ {1 + W_0[-Ũ exp(v/(2τ)-1)]}.
```

Se fijan coordenadas en el cuadrado unidad

```text
y = v/(bλ),
z = (Ũ-Ũ_p)/(Ũ_q-Ũ_p),
x = (r-1)/λ.
```

La medida física es `dv dr`, de modo que su densidad normalizada en `(z,y)` es proporcional a
`-b λ² ∂_z x`. Expandiendo la inversa exacta a `σ` fijo,

```text
p_{λ,σ}(z,y) = 1 + λ p₁ + λ² p₂ + λ³ p₃ + O(λ⁴),
p₁ = 4a Z + (b/2)Y,
∂_σ p₂|₀ = -(2a+b)Z + (b/2)Y,
Z=z-1/2,  Y=y-1/2.
```

Los dos términos escritos son aditivos en `Z` e `Y`: solo deforman marginales y la cópula los
elimina. Como `∂_τ=λ⁻¹∂_σ`, el primer score conjunto relevante a orden `λ²` es

```text
B := ∂_σ p₃|₀ - p₁ ∂_σ p₂|₀.
```

Sea `P_c B := B-E(B|Z)-E(B|Y)+E(B)` la proyección que quita ambas marginales. La expansión
algebraica da

```text
P_c B = [b(4a-b)/2] ZY,
∂_τ log c_τ|_{τ=1}
      = λ² [b(4a-b)/2] ZY + O(λ³).
```

El movimiento de los cuantiles marginales no altera este término: sus velocidades son `O(λ)`,
mientras que, por la aditividad de `p₁`, los gradientes condicionales empiezan en `O(λ²)`; su
producto entra en `O(λ³)`. Finalmente, con la medida límite uniforme y
`E[Z²]=E[Y²]=1/12`,

```text
I_λ(1)/λ⁴ -> [b²(4a-b)²/4] (1/12)²
           = b²(4a-b)²/576.
```

Multiplicar por `V_λ(1)/λ² -> 2ab` produce el prefactor de `κ` de §1.

## 3. Comprobaciones

`dev/r2_lambda6_06_prefactor.py` verifica simbólicamente la proyección marginal, la integral de
Fisher y las especializaciones. No usa datos aleatorios. Salida principal:

```text
copula score / lambda^2 = b*(4*a - b)*(2*y - 1)*(2*z - 1)/8
I(1) / lambda^4        = b**2*(4*a - b)**2/576
V(1) / lambda^2        = 2*a*b
kappa(1) / lambda^6    = a*b**3*(4*a - b)**2/288
a=b specialization      = a**6/32
```

Contra los valores deterministas ya producidos por
`research_program/work_packages/wp4_kappa_numeric_reference.py`, para `a=b=0.3`:

| `λ` | `I` numérico | asintótica `1.265625e-4 λ⁴` | ratio num./asint. |
|---:|---:|---:|---:|
| 0.20 | `1.989860e-7` | `2.025000e-7` | 0.98265 |
| 0.10 | `1.252737e-8` | `1.265625e-8` | 0.98982 |
| 0.05 | `7.843762e-10` | `7.910156e-10` | 0.99161 |

Una comprobación adicional sobre la cópula numérica a `λ=0.1` da, para
`dK/dτ ~ b(4a-b)λ²/2`, ratios 0.99864, 0.99740 y 0.99608 en `b=0.15,0.30,0.45`. En la forma
afinada `b=4a=1.2`, el valor cae de escala `10^-3` a `-8.98e-6`, coherente con la cancelación del
término dominante; no se usa ese residuo para inferir el orden siguiente.

## 4. Por qué falló el primer prefactor

La aproximación anterior `K_an=ΔŨ Δv/(eτ)` reproduce `K(1)` pero no su derivada. Coincidía
puntualmente al bajar `λ`, mientras `dK_an/dτ` tenía signo opuesto y difería por un factor que
tendía a `-4sqrt(2)` en la forma `a=b=0.3`. No era una convención de Fisher ni un error de
centrado: las esquinas están a distancia `O(λ)` del horizonte, por lo que la escala natural de
variación es `τ-1=O(λ)`. Derivar una expansión puntual no uniforme pierde precisamente los
términos de tercer orden que sobreviven después de quitar las marginales. La variable
`σ=(τ-1)/λ` corrige el orden de límites.

## 5. Etiquetas

```text
EXPONENTE_LAMBDA6      = DERIVED_IN_THIS_PROJECT / NUMERICALLY_CROSS_CHECKED
PREFACTOR_GENERAL      = a*b^3*(4*a-b)^2/288
PREFACTOR_A_EQ_B       = a^6/32
FAMILIA_ESCANEADA      = a=b=0.3 / COEFFICIENT=2.278125e-5
TUNED_SHAPE_B_EQ_4A    = LEADING_TERM_CANCELS / NEXT_ORDER_OPEN
INDEPENDENT_AUDIT      = NOT_DONE
SEMILLAS               = 0
SIMULACION             = NINGUNA
SELLO                   = INTACTO
```

El cierre es analítico para la familia nominada de R2 y está contrastado internamente. No prueba
una ley universal para cualquier estrechamiento de diamantes, no calibra el estimador sellado y
no establece una afirmación de novedad.
