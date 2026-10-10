# S4W — nota de cierre del apéndice

**Fecha:** 2026-10-10
**Objeto:** cerrar el apéndice `S4W` que quedaba colgando del programa `nachocausal`, cerrado por el comité 049 el 2026-07-30
**Cadena:** auditoría `1e03a54` → R6′ `e4d9365` → retirada del no-go `30f7fda` → R6″ q2 `0c3f07f` → tercera casa `38cfd39` → esta nota
**Autorizado por:** el PI

```text
ESTADO: APPENDIX_CLOSED / ONE_POSITIVE_LOCAL_RESULT / ONE_NAMED_GAP_IN_THE_LITERATURE
        NO_PHYSICAL_ESTIMATOR / NO_FURTHER_WORK_RECOMMENDED
NO_SIMULATION / NO_SEEDS / SEAL_UNTOUCHED (thresholds.py 6e2c3888…bfefd4)
```

---

## 1. Lo que queda establecido

**Un resultado local, positivo, confirmado por tres casas de familias distintas.**

A orden de curvatura algebraico `R^2`, en vacío, el canal diagonal de orden `rho^{-1/2}` del
valor medio del operador de cinco capas tiene coeficiente

```
    -(73 sqrt6 / (1575 pi)) · C_abcd C^abcd
```

y la contribución **dependiente del observador es cero en ese canal**, no pequeña. El mecanismo
es algebraico: las dos formas cuárticas que intervienen reparten la densidad de superenergía de
Bel–Robinson con coeficiente **uniforme** sobre `u^4, u^3v, u^2v^2, uv^3, v^4`, y el factor
`(v-u)^{d-2}` de la medida tiene coeficientes `1, -2, 1` que suman cero. Lo único que sobrevive
es el exceso no uniforme, que es puro invariante. Equivalentemente, con la identidad que aportó
Grok: `Q = T(y^4)/2 + K (y·y)^2/16`, y `(y·y)^2 = 4u^2v^2`.

**Es, exactamente, el número que el §7 del candidato había escrito con signo de interrogación.**
La auditoría lo tenía en `C_W1_COEFFICIENT = FAIL / NO DETERMINADO`. Estaba equivocada.

Verificado por tres vías independientes: contracción tensorial directa con `E`, `B` genéricas;
la identidad de Bel–Robinson; y la rederivación del `-1/180` de Wang (76) desde su ec. (6) que
aportó Astra —`(1/2)tr h_4 - (1/4)tr(h_2^2) = 1/45 - 1/36 = -1/180`—. El `73` sale de
`(105+41)/2`, con el `105` de la ec. (76) y el `41` de la ec. (79), calculadas por separado.

**El operador también es legítimo**, y eso lo estableció la auditoría §1: `b_* ` satisface las
condiciones (3a)–(3c) de Belenchia, luego su teorema de universalidad da límite local
`□ - R/2`. Recontrolado por una vía distinta en R6′ §3: los dos operadores dan la misma
contribución `4 sqrt6/9` en el canal `(2,2)`, porque el cociente de prefactores `b_0` (4)
cancela el de coeficientes de canal (1/4).

## 2. Lo que NO queda establecido, y es lo que cierra la línea

**No hay enunciado global.** El coeficiente local no es el valor medio completo, porque falta
el control del resto. Y falta por una razón concreta y ajena a este trabajo.

La región del cono (`W2`) contribuye a `B̄` en `O(rho^{-1/2})` —el mismo orden que la señal—.
La cota publicada que da eso es la de Benincasa–Dowker–Dowker, y es **válida**: su ec. (25)
acota primero el integrando, obteniendo el kernel de coeficientes positivos
`(1 + 9 sigma u^2v^2 + 8 sigma^2 u^4v^4 + (4/3) sigma^3 u^6v^6)`, y **luego** lo escribe como
identidad con el operador de signos invertidos `(1 - 9H_1 + 8H_2 - (4/3)H_3)` —que no es su
`Ô = (1 + 9H_1 + 8H_2 + (4/3)H_3)` de la ec. (15)—. Ninguna desigualdad pasa por `Ô`. Y su
`O(rho^{-2})` sale del **orden del desarrollo en `u`** (su `u^3`), no de raíces del operador.

**La mejora a `O(rho^{-1})` no está probada.** Requeriría que las raíces del operador aniquilen
la cota, y el operador de la cota —el de kernel positivo— **no tiene ninguna raíz positiva**,
ni con cuatro capas ni con cinco: comprobado, `Q_{|b|}(s) > 0` para todo `s > 0`. La vía que
R6′ dio por buena era la de Pfeiffer (3.15)–(3.22), que aplica el operador **con sus raíces** a
una cantidad donde las funciones ya se han sustituido por sus normas supremas. Un operador
diferencial no preserva desigualdades. Ese paso es inválido, y lo encontró Astra.

Por tanto **el `F2` original de la auditoría está en pie**: `W2` vive en el orden de la señal,
también con cinco capas.

Lo que haría falta tiene nombre, y los propios autores lo declaran ausente:

> *"since we lack an explicit expression for the expansion of the volume of long skinny
> intervals 'down the light cone' in W2, the finite rho corrections to the limit from W2 can
> only be given in terms of integrals of unknown functions"* — BBD §III.D

Una expansión transversal del volumen de intervalos largos y finos en espacio curvo, con
regularidad suficiente y uniforme en `(V, theta, phi)`. Sin ella: no hay resto `o(rho^{-1/2})`,
`F1` y `C0` siguen abiertos, y no hay estimador.

Quedan además dos huecos menores de la misma familia, los dos señalados por Astra: la
uniformidad de los restos cerca de `u = 0` —el resto de Wang está formulado para diamantes
pequeños a orientación fija, y la rapidez **no** está acotada en `W1`, `tanh eta = (v-u)/(v+u)`—
y que `B_* 1` sobre un pasado no compacto no está definido, porque Pfeiffer presupone soporte
compacto.

## 3. Una corrección a la literatura

Independiente del operador de cinco capas, y de Astra, no de este repo:

**Los pasos (3.15)–(3.22) de Pfeiffer 2022 trasladan cotas de norma suprema a través de un
operador diferencial, que no preserva desigualdades.** Su identidad (3.17) no legitima esa
operación. En consecuencia su estimación de que la región del cono aporta correcciones de orden
`O(rho^{-2/d})` **no está probada** por ese argumento. Que el factor `A_{lambda,l}(n)` anule la
integral de un monomio es correcto; que anule una cota obtenida sustituyendo funciones por sus
normas supremas, no se sigue.

Ejemplo funcional de insuficiencia (Astra): una amplitud positiva y acotada que contenga
`U^3 log U`, con fase `V = U^2 f_0`, da
`int U^3 log U e^{-rho f_0 U^2} dU = -log(rho)/(4 f_0^2 rho^2) + cte/rho^2 + exp`, y la cuarta
raíz convierte ese logaritmo en orden `rho^{-1/2}`. No es un contraejemplo geométrico
Ricci-flat suave; demuestra que las hipótesis de mera acotación no bastan.

BBD, en cambio, está bien: su cota no pasa por el operador (§2).

## 4. Prioridad

El único fallo de la auditoría que sobrevive intacto, y es documental:

- `Ô_*` **es** el operador `O_6` de la ec. (13) de Dowker–Glaser (arXiv:1305.2588), evaluado con
  la relación de `d=4`, `H_DG = 4 rho ∂_rho`. Verificado: reproduce `(1,-14,41,-44,16)`, y de
  control las filas `d=4` y `d=6` de su Tabla 1. La quinta capa es un caso de una torre
  publicada, no un hallazgo.
- El **programa** está publicado: de Brito–Eichhorn–Pfeiffer (arXiv:2301.13525) enuncia en sus
  conclusiones *"definitions of new discrete operators, based on expressions inspired by Eq.(8),
  but with, for instance, different coefficients and different number of layers"*.
- **No hay antecedente exacto** del coeficiente ni del vector: la tesis de Pfeiffer, leída
  completa, no contiene Weyl ni Kretschmann ni la familia GCD no mínima.

Las cinco fuentes del brief están ya en `biblioteca/` (git-ignored), con sus sha256.

## 5. Frontera de claims — intacta

Nada de lo anterior la toca. Sigue prohibido afirmar:

```
convergencia realizacion-por-realizacion; varianza finita o controlada; detector practico
de horizonte; Page-Shoom discreto; reconstruccion de Schwarzschild; emergencia del cono
causal; prioridad sin auditoria bibliografica separada.
```

Lo calculado es un **coeficiente local del valor medio sobre sprinklings**. Dowker–Glaser
advierten que las fluctuaciones del operador minimal **crecen** con la densidad; nada aquí dice
que las del de cinco capas no lo hagan. Las fluctuaciones no se han tocado en absoluto.

## 6. Qué reabriría esto

Una sola cosa, y no es una elección de capas:

```
Una expansion transversal del volumen de intervalos largos y finos en espacio curvo
—la f_0(V,theta,phi) de BBD y los dos ordenes siguientes— con control UNIFORME en
(V,theta,phi), suficiente para separar O(rho^{-1/2}) de O(log(rho) rho^{-1/2}).

NO sirve: mas capas, otra raiz, un taper, ni la via de Pfeiffer (3.15)-(3.22).
```

Es un problema abierto declarado en la literatura. No se recomienda abordarlo desde aquí.

## 7. Historia de los errores, porque es parte del resultado

Cuatro rondas de revisión ciega a tres casas (`deepseek-v4-pro`, `grok-4.6`, `gpt-6-astra`),
con `revision-ciega` del PATH. En las cuatro me corrigieron algo. Lo que cayó:

| # | error mío | quién | dónde |
|---|---|---|---|
| 1 | la auditoría no examinó la cara `W1` de `(h3)`: el canal `k=3` lo comparten el resto log y el `y^4` de `C^2` | Grok | auditoría rev.2.1 §2.4 |
| 2 | clasifiqué las vías a `C^2` sin imponer Ricci-flat; dos de las tres se anulan en vacío | ambas | R6″ §4 |
| 3 | apliqué `Ô_*` a `G_nu` en vez de a `rho^l G_nu`: el no-go entero era falso y hubo que retirarlo | ambas | `30f7fda` |
| 4 | la auditoría §3.3 afirmaba que la rapidez está acotada en `W1`. No lo está | propio, al calcular | R6″ q2 |
| 5 | el `32` del control de §7.1 era el coeficiente de la forma reducida, no de `E^2` | Astra | q2 rev.2 |
| 6 | el argumento de paridad: la integración angular mata componentes **espaciales** impares, no grado total impar | Astra | R6′ rev.4 |
| 7 | la truncación `∇∇Riem` mal justificada: aparece al mismo grado cuártico en Wang (6) | Astra | q2 §8.2 |
| 8 | promoví un coeficiente local a enunciado global sobre la media | Astra | q2 rev.2 |

Y una vez rechacé una corrección: la objeción de antisimetría de DeepSeek sobre la ec. (76) de
Wang, que falla al verificarla —en `u=v` el vector `y` es puramente temporal, luego
`Q = E^2 (y^0)^4 != 0`, y el polinomio reproduce la evaluación directa—. Hizo falta una tercera
casa **con el artículo original en el lote** para zanjarlo. Las dos primeras rondas se habían
hecho heredando la transcripción, que era la laguna que Grok declaró.

La lección operativa, que vale más que el coeficiente: de mis ocho errores, siete los encontró
otra familia de modelos y uno lo encontré yo al calcular. Ninguno lo encontré releyendo lo que
había escrito.
