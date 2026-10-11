# B2 — paso 1: ¿transfiere el colapso de B1.5 a `rho'`?

**Fecha:** 2026-10-11
**Autorizado por:** el PI (paso 1 de `dev/B2_RECOST_PROPOSAL_2026-10-11.md`)
**Ejecutado:** análisis en papel. **Sin código nuevo, sin sprinklings, sello intacto.**

```text
RESPUESTA = SI_TRANSFIERE / POR_UNA_RAZON_MAS_FUERTE_DE_LA_PREVISTA
OBJETO_CARO = POSIBLEMENTE_INNECESARIO
ANOMALIA_DETECTADA = SI -> §4, requiere comprobacion aparte
```

---

## 1. El hecho estructural

Temía que `rho'` rompiera la unimodalidad de `G`, que es lo que explota la envolvente de B1.5.
**No puede romperla, porque `partial_t G` no existe en este problema.**

En `verify_certified_rho_frozen_pair.py`:

```python
def G(uv):  s = s_of_uv(uv); return s * np.exp(-s)
def q(uv):  s = s_of_uv(uv); return 2.0*np.exp(-0.5*s)/s**1.5
```

`G` y `q` toman **solo el producto `uv`**. No reciben `lambda`. Y en
`verify_b2_1_local_injectivity.py`:

```python
def path(t): return (1.0 - t)*L0 + t*L1
def enclosure(lam, ...):  v0, v1, uout, uin, _ = lam
```

`lambda` son **los límites del dominio**: `V in [v0,v1]`, `U in [-uout,uin]`. (La quinta
componente se descarta y además vale `0.1` en los dos extremos.)

**Toda la dependencia en `t` está en el dominio de integración, ninguna en el integrando.**

## 2. Consecuencia: `rho'` es Leibniz puro

Con `rho(t) = (2/Z^2) B`, y `v0' = -0.3`, `v1' = -0.2`, `uout' = +1.0`, `uin' = +0.4`
(constantes, el camino es afín):

```text
Z'(t) = int_{v0}^{v1} [ G(uin V) uin' + G(-uout V) uout' ] dV
      + int_{-uout}^{uin} [ G(U v1) v1' - G(U v0) v0' ] dU
```

Cuatro integrales **1D de `G`** — exactamente los objetos que B1.5 ya encierra, con la misma
unimodalidad y el mismo redondeo dirigido.

`B'(t)` es la suma de las **integrales de cara** del mismo integrando
`G(Ux Vx) G(Uy Vy) p(Delta_max)`, una dimensión menos (3D en vez de 4D). Las identidades de
colapso de B1.5 §2 son hechos geométricos sobre el dominio ordenado `{Ux<=Uy, Vx<=Vy}` y
sobreviven intactas; sobre cada cara, además, parte de la restricción de orden se vuelve
automática (p.ej. en la cara `Uy = uin`, la condición `Ux <= Uy` no restringe nada).

Nada de esto deriva `G`. La unimodalidad se conserva **exactamente**.

## 3. El resultado que importa: puede que `rho'` no haga falta

La regla de promoción de B2 es

```text
B2_CORRECTED_POSITIVE  iff  formal_upper_bound(drho_dt) < 0
```

y **es esa regla, no el problema, la que obliga a construir `B'`** — el objeto que costaba
16 384 cajas, con `B` a 65 536.

Pero separar `rho` en dos valores de `t` **no necesita la derivada**. Necesita una cota superior
en un `lambda` y una inferior en otro, que es **literalmente lo que B1.5 ya hace** para el par
congelado: su §3 es la cadena superior para `lambda0` y su §4 la inferior para `lambda1`,
y produjo `U0 < L1` con margen del 14.66 %.

Aplicar la cadena superior en `lambda(0.45)` y la inferior en `lambda(0.55)` es **uso directo de
maquinaria existente, sin partición y sin `B'`**.

Reserva honesta: esa ruta establece `rho(t_i) < rho(t_j)` —no-constancia y orden sobre la malla—,
**no** el signo de `drho/dt`. Si el terminal `B2.1_POSITIVE_LOCAL_MONOTONICITY` exige la derivada
en sentido estricto, esta ruta no lo emite; emite un resultado más débil y mucho más barato.
Decidir si eso basta es del PI, no mío.

## 4. Anomalía detectada — no resuelta

Comparando lo que ya está registrado en el repo:

| fuente | `t` | envolvente de `rho` |
|---|---|---|
| `verification_certified_rho_frozen_pair.json` (B1.4) | 0 (`lambda0`) | `[0.012756, 0.018794]` |
| `verification_b2_1_local_injectivity.json` | 0.45 – 0.55 | `[0.005168, 0.007614]` |
| `verification_certified_rho_frozen_pair.json` (B1.4) | 1 (`lambda1`) | `[0.027931, 0.043835]` |

**El punto medio queda por debajo de los dos extremos, con un factor de 2 a 3.** Verifiqué que la
normalización es la misma (`2*sum(weight*angular_prob)/z**2` en ambos) y que el par congelado es
el mismo (`LAMBDA0/LAMBDA1` = `L0/L1`).

Si las tres envolventes son válidas, `rho` **no es monótona en `[0,1]`**: baja desde `t=0`, tiene
un mínimo antes de `0.45`, y sube hasta `t=1`. Es posible, pero ningún documento lo dice, y un
lector asumiría que `rho` interpola entre las bandas de B1.4.

La alternativa es que una de las envolventes no sea válida.

**No lo he resuelto porque resolverlo es código**, y lo autorizado era papel. La comprobación es
barata: evaluar la función `enclosure` de B2.1 —ya escrita— en `t=0` y `t=1` y contrastar con las
bandas de B1.4. Segundos de cálculo. No es búsqueda de un punto favorable: es un control de
consistencia entre dos artefactos del repo, y `no_new_points` protege contra lo primero, no
contra lo segundo.

Hasta que eso se aclare, **el objetivo «3.8x» que propuse para separar los extremos de la malla
no debe darse por bueno**: está calculado sobre las envolventes de B2.1, y si esas envolventes
discrepan de B1.4 el factor cambia.

## 5. Estado

```text
PASO_1 = COMPLETADO / POSITIVO
PASO_2 = NO_AUTORIZADO  (aplicar la cadena de B1.5 en lambda(0.45) y lambda(0.55))
BLOQUEO_PREVIO_A_PASO_2 = resolver la anomalia de §4
```
