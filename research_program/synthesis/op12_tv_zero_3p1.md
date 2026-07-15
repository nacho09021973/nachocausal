# OP-1.2 — Clase TV=0 acotada en Schwarzschild 3+1D

**Estado:** `THEORY_DRAFT / SCOPED_CLASSIFICATION / NO_GENERAL_HAUPTVERMUTUNG`

**Revisiones autorizadas:**
`docs/comite/comite_decision_027_phase1-theory-package-first-review.md` §8-§11 y
`docs/comite/comite_decision_028_phase1-theory-package-second-review.md` §8-§11 y
`docs/comite/comite_decision_029_phase1-theory-package-third-review.md` §8-§11 y
`docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md` §8-§11;
sign-off Nacho / PI, 2026-07-15.

## 1. Pregunta exacta

Sea `P^K_{g,n}` la ley del poset no etiquetado en el canal `fixed_n`, y sea `P^K_{g,rho}`
la ley conjunta order+number en Poisson con `rho` conocida. Se distinguen:

1. `TV(P_{g,n},P_{g',n})=0` para un `n` concreto;
2. igualdad para todo `n>=0`;
3. contiguidad o equivalencia asintotica de dos secuencias de experimentos.

Este documento caracteriza solo una subfamilia candidata. No identifica la clase `TV=0` de todos
los espaciotiempos 3+1D ni deduce una Hauptvermutung discreta de HKMM.

## 2. Lema suficiente general

Sean `(K_g,prec_g,mu_g)` y `(K_{g'},prec_{g'},mu_{g'})` espacios causales de probabilidad, usando
las medidas positivas normalizadas. Si existen representantes conull y una biyeccion bimedible
`phi` entre ellos, con inversa medible modulo nulos, tal que

```text
phi_# mu_g = mu_{g'},
x prec_g y  <=>  phi(x) prec_{g'} phi(y)
para (mu_g tensor mu_g)-casi todo par ordenado (x,y),
```

entonces las leyes de posets etiquetados, y por data processing las no etiquetadas, son iguales
para todo `n`.

**Prueba.** Acoplar cada muestra `X_i~mu_g` con `phi(X_i)`. Para una muestra finita hay un numero
finito de pares; la union de sus conjuntos excepcionales sigue siendo nula. Todas las relaciones
de los dos posets coinciden casi seguramente. El cociente por relabeling preserva la igualdad. Fin.

La recíproca no se usa. La igualdad de todas las densidades finitas de subposets pertenece al
problema de kernels/poset limits y admite equivalencias debiles; HKMM parte de una biyeccion causal
continua dada, no de igualdad de leyes de muestras no etiquetadas.

## 3. Orbita de dilatacion Schwarzschild

Fijemos un sector `sigma in {+,-}` y una forma de patch `lambda` de OP-1.1. Para `a=M'/M`, la
identificacion en coordenadas Kruskal adimensionales

```text
phi_a(U,V,omega) = (U,V,omega)
```

cumple

```text
g_{M',lambda} = a^2 g_{M,lambda},
mu_{M',lambda} = a^4 phi_{a#} mu_{M,lambda},
mu_{M',lambda}(K_{M',lambda}) = a^4 mu_{M,lambda}(K_{M,lambda}).
```

Una multiplicacion conforme positiva conserva causalidad. Tras normalizar el volumen,

```text
mu_{M',lambda}/mu_{M',lambda}(K_{M',lambda})
  = phi_{a#}(mu_{M,lambda}/mu_{M,lambda}(K_{M,lambda})).
```

Por el lema suficiente,

```text
P^fixed_n_{M,sigma,lambda} = P^fixed_n_{M',sigma,lambda}
para todo n y todo M,M' en I_M.
```

Por tanto, dentro de cada sector y con `lambda` fijo, la clase `TV=0` a `fixed_n` es todo el
intervalo de masas. Esto no es una extrapolacion del Teorema A 1+1D: es una prueba 3+1D directa por
coescalado de la metrica y de la medida normalizada.

## 4. Que ocurre con el target

Los targets adimensionales de OP-1.1 son constantes sobre la orbita:

```text
h_M = r/(2M)-1,
y_M = sign(h_M),
H_M/M = {r/M=2}.
```

El campo `c_g` y el caracter sectorial `Chi(g)` tambien son constantes a lo largo de la orbita de
masa cuando el sector se mantiene fijo. La escala absoluta `M` y `r_h=2M` no son identificables en
`fixed_n`, pero la localizacion relativa en unidades de `M`, de tamano de patch o de

```text
ell_eff(n;g) = (mu_g(K_g)/n)^(1/4),  n>=1
```

no cambia a lo largo de la orbita. La restriccion `n>=1` aplica solo a esta escala: la igualdad de
leyes `fixed_n` de la seccion 3 sigue cuantificada para todo `n>=0`. `ell_eff` es una escala efectiva
de scoring condicional, no una densidad fisica observada en el experimento `fixed_n`. Un futuro
claim debe nombrar cual target y cual unidad puntua.

## 5. Canal order+number con rho conocida

En el canal Poisson,

```text
N_M ~ Poisson(rho mu_M(K_{M,lambda})),
mu_M(K_{M,lambda}) = M^4 mu_1(K_{1,lambda}).
```

Si `rho>0` y `M != M'`, las medias Poisson son distintas. Como la marginal de `N` ya difiere, las
leyes conjuntas no pueden tener `TV=0`. Dentro del sector y forma de patch fijados,

```text
TV(P^order+number_{M,sigma,lambda},
   P^order+number_{M',sigma,lambda}) = 0
iff M=M'.
```

Si `rho` no es conocida fisicamente, el canal identifica `rho M^4`, no separa `rho` de `M`.

## 6. Dualidad BH/WH

Para sectores emparejados,

```text
P^K_{M,-,lambda} = d_# P^K_{M,+,lambda},
d([P])=[P^op].
```

Esto no implica igualdad TV en el espacio de posets orientados. La igualdad requeriria que la ley
BH fuera dual-invariante, propiedad que aqui queda abierta. Para claims de localizacion modulo
dualidad puede usarse el canal cocientado que identifica `[P]` con `[P^op]`; en ese cociente los
dos sectores tienen la misma ley por construccion. Para claims de caracter no se permite ese
cociente: `Chi` cambia de signo y no desciende a el.

## 7. Alcance exacto de la clasificacion

La clasificacion queda cerrada solo para

```text
F_candidate = {
  Schwarzschild maximal 3+1D,
  lambda fijo,
  M in I_M,
  sector temporal fijo;
}
```

y, para localizacion modulo dualidad, para su cociente por `D`.

Quedan abiertos:

- variar la forma del patch `lambda`;
- patches no coescalados con `M`;
- perturbaciones no Schwarzschild o no esfericas;
- la recíproca general desde igualdad de todas las leyes finitas a isomorfismo causal-medida;
- igualdad o separacion BH/WH sin cocientar;
- contiguidad cuando `n`, patch o alternativa cambian conjuntamente.

No se autoriza usar HKMM para cerrar ninguno de esos puntos. HKMM fija la clase conforme cuando ya
existe una biyeccion causal entre continuos `d>2`; no convierte una ley de muestreo discreta en esa
biyeccion (`biblioteca/derived-md/The causal set approach to quantum gravity.md:340-352`).

## 8. Terminales que pueden fallar

- Si el futuro preregistro permanece dentro de `F_candidate`, usa `lambda` fijo y declara el canal:
  `TV_ZERO_CLASS_SCOPED_TO_CANDIDATE_FAMILY`.
- Si pretende variar patches o geometria sin un nuevo lema: `TV_ZERO_CHARACTERIZATION_OPEN`.
- Si puntua `M` absoluto en `fixed_n`: `TARGET_NONIDENTIFIABLE_TV_ZERO`.
- Si identifica BH/WH despues de cocientar por dualidad: `TARGET_NONIDENTIFIABLE_TV_ZERO`.

```text
OP_1_2_AUTHOR_TERMINAL = TV_ZERO_CLASS_SCOPED_TO_CANDIDATE_FAMILY
```

El terminal es condicional al alcance anterior; no es `TV_ZERO_CLASS_CHARACTERIZED` en sentido
general.

## 9. Fuentes

- Hawking, King y McCarthy, J. Math. Phys. 17 (1976), DOI 10.1063/1.522874.
  `[UNVERIFIED_PRIMARY_LOCAL_SNAPSHOT]`
- Malament, J. Math. Phys. 18 (1977), DOI 10.1063/1.523436.
  `[UNVERIFIED_PRIMARY_LOCAL_SNAPSHOT]`
- Surya, *The causal set approach to quantum gravity*, arXiv:1903.11544; lectura local
  `biblioteca/derived-md/The causal set approach to quantum gravity.md:340-481`.
- Janson, *Poset limits and exchangeable random posets*, arXiv:0902.0306: razon para no asumir una
  recíproca fuerte de igualdad de leyes finitas. `[UNVERIFIED_LOCAL_SNAPSHOT]`
- Familia dual y patch: `research_program/synthesis/op11_spherical_dual_target.md`.
