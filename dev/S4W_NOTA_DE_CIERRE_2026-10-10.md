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

**Un resultado local y positivo.** Sobre el acuerdo, dicho con precisión y no redondeado:
**dos casas de familias distintas lo confirmaron** (`grok-4.6`, `gpt-6-astra`) y la tercera
(`deepseek-v4-pro`) lo **refutó**, con una objeción que se verificó y falló (q2 §7.1). Esa
tercera casa no confirmó el resultado. Lo que lo sostiene no es un recuento de votos sino que
la objeción discrepante es comprobable y se comprueba falsa, y que el resultado se obtiene por
tres derivaciones independientes.

A orden de curvatura algebraico `R^2`, en vacío, el canal diagonal de orden `rho^{-1/2}` del
valor medio del operador de cinco capas tiene coeficiente

```
    -(73 sqrt6 / (1575 pi)) · C_abcd C^abcd
```

y la contribución **dependiente del observador es cero en ese canal**, no pequeña. El mecanismo
es algebraico: las dos formas cuárticas que intervienen reparten la densidad de superenergía de
Bel–Robinson con coeficiente **uniforme** sobre `u^4, u^3v, u^2v^2, uv^3, v^4`, y el factor
`(v-u)^{d-2}` de la medida tiene coeficientes `1, -2, 1` que suman cero. Lo único que sobrevive
es el exceso no uniforme, que es puro invariante. **Restricción obligada:** eso vale como
**proyección sobre el canal `rho^{-1/2}`**, no como «la contribución de `W` al valor medio es
cero». `(v-u)^2 S_4 = u^6 - u^5 v - u v^5 + v^6`: desaparecen los coeficientes interiores, no
el polinomio. Equivalentemente, con la identidad que aportó
Grok: `Q = T(y^4)/2 + K (y·y)^2/16`, y `(y·y)^2 = 4u^2v^2`.

**Es, exactamente, el número que el §7 del candidato había escrito con signo de interrogación.**
La auditoría lo tenía en `C_W1_COEFFICIENT = FAIL / NO DETERMINADO`. Estaba equivocada.

Verificado por tres vías independientes: contracción tensorial directa con `E`, `B` genéricas;
la identidad de Bel–Robinson; y la rederivación del `-1/180` de Wang (76) desde su ec. (6) que
aportó Astra —`(1/2)tr h_4 - (1/4)tr(h_2^2) = 1/45 - 1/36 = -1/180`—. El `73` sale de
`(105+41)/2`, con el `105` de la ec. (76) y el `41` de la ec. (79), calculadas por separado.

**El operador también es legítimo**, y eso lo estableció la auditoría §1: `b_* ` satisface las
condiciones (3a)–(3c) de Belenchia, luego su teorema de universalidad da límite local
`□ - R/2` **bajo las hipótesis con que él lo prueba**: soporte compacto del campo, de tamaño
menor que el radio de curvatura, y existencia del límite local —él mismo escribe que su prueba
*"strictly holds true"* sólo con esa hipótesis, y que por eso no considera `W2` ni `W3`. Recontrolado por una vía distinta en R6′ §3: los dos operadores dan la misma
contribución `4 sqrt6/9` en el canal `(2,2)`, porque el cociente de prefactores `b_0` (4)
cancela el de coeficientes de canal (1/4).

## 2. Lo que NO queda establecido, y es lo que cierra la línea

**No hay enunciado global.** El coeficiente local no es el valor medio completo, porque falta
el control del resto. Y falta por una razón concreta y ajena a este trabajo.

La región del cono (`W2`) está **acotada** en `O(rho^{-1/2})` sobre `B̄` —el mismo orden que la
señal—. Es una cota superior, no un orden efectivo: la contribución real podría ser menor, pero
no hay cómo probarlo. Y la cota no mejora, porque el operador de la cota no tiene raíces en
`s>0`.

La cota publicada que da eso es la de Belenchia–Benincasa–Dowker (arXiv:1510.04656), y es **válida**: su ec. (25)
—que está en su §II.B, el caso **plano**; el curvo es su §III.B, donde el mismo esquema deja
`W2` en `O(rho^{-1/2})` sobre `B̄`— acota primero el integrando, obteniendo el kernel de coeficientes positivos
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

Quedan además **dos huecos lógicamente independientes**, que no se cierran resolviendo `W2` y
que la rev.1 llamaba «menores» sin justificación (Astra, Grok): la
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
- **No se encontró antecedente exacto** del coeficiente ni del vector en las fuentes
  examinadas. Precisión obligada: la tesis de Pfeiffer **sí menciona Weyl**, una vez, en su
  cap. 6 —obtener información del tensor de Weyl comparando las construcciones de bola
  geodésica e intervalo de Alexandrov, en espacio plano—, tal como la auditoría §6.3 había
  registrado correctamente. Lo que no contiene es Kretschmann, ni la familia GCD no mínima, ni
  antecedente del coeficiente; su generalización es `B^2 = B∘B`.

> **Corregido en rev.2 (Astra).** La rev.1 de esta nota decía que la tesis «no contiene Weyl».
> **Es falso**, y además contradecía a mi propia auditoría §6.3, que lo tenía bien. Una regresión
> al resumir. Y «no hay antecedente exacto» se degrada a «no se encontró en las fuentes
> examinadas»: la ausencia en una tesis no certifica ausencia bibliográfica.

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

**Tres** cosas, no una, y ninguna es una elección de capas:

```
(a) Justificar la regularidad y la UNIFORMIDAD que permitan separar O(rho^{-1/2}) de
    O(log(rho) rho^{-1/2}) en la region del cono.
(b) La uniformidad de los restos de Wang cerca de u=0, donde la rapidez no esta acotada.
(c) La definicion de B_*1 sobre un pasado no compacto.

(b) y (c) NO se siguen de (a): son independientes.
NO sirve, y es lo unico que esta descartado: la via de Pfeiffer (3.15)-(3.22).
```

> **Corregido en rev.2 (Astra, corroborado por Grok).** La rev.1 decía «una sola cosa» y
> «**no sirve** más capas, otra raíz, un taper, ni la vía de Pfeiffer». **Excedía lo
> demostrado por dos lados.**
>
> Primero, recortaba el hueco a uno cuando el propio §2 enumera tres, y (b) y (c) son
> independientes de (a).
>
> Segundo —y es la objeción que más importa—: **se ha descartado un argumento, no todas las
> reparaciones posibles.** BBD (63) ya introduce `V = U^2 f_0 + U^3 f_1 + U^4 f_2 + U^5 F` bajo
> hipótesis de diferenciabilidad; su declaración de §III.D se refiere a las **expresiones
> explícitas** de esos coeficientes y a la interpretación de las correcciones, **no** a que
> ninguna separación asintótica sea posible sin calcularlos. Astra esboza una ruta concreta: si
> se justificara uniformemente el cambio `w = sqrt(V(y))` y la amplitud transformada admitiera
> `A~(w,z) = a_0(z) + a_1(z)w + a_2(z)w^2 + a_3(z)w^3 + O(w^4)`, las cuatro raíces eliminarían
> las cuatro potencias integradas y el resto daría `O(rho^{-5/2})` antes del prefactor —**sin
> necesidad de conocer los `a_j`**. Lo pendiente es justificar las hipótesis y la uniformidad.
>
> Por tanto el fundamento de no continuar **no es un no-go**: es una **obligación de prueba
> pendiente**, y la decisión de no asumirla desde aquí es de oportunidad, no de imposibilidad.

No se recomienda abordarlo desde aquí, por coste y porque el programa está cerrado desde el
2026-07-30. Pero que no se lea como «no tiene arreglo».

## 7. Historia de los errores, porque es parte del resultado

**Cinco** rondas de revisión ciega a tres casas (`deepseek-v4-pro`, `grok-4.6`, `gpt-6-astra`),
con `revision-ciega` del PATH. En las cinco me corrigieron algo —esta nota incluida. Lo que cayó:

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
| 9 | **acepté sin comprobar la prueba de `W2` de Pfeiffer**, que pasa cotas por un operador. Es el error que habilitó la revocación de `F2` y las promociones posteriores; el 8 es su consecuencia | Astra | esta nota §2–§3 |
| 10 | leí el resto `O(log rho/sqrt rho)` como incompatibilidad **establecida**, cuando era comprobación abierta | Grok | auditoría rev.2.1 §3.3 |
| 11 | formulé la cancelación de `W` para **toda** la contribución en vez de para el canal | Astra | esta nota §1 |

Y una vez rechacé una corrección: la objeción de antisimetría de DeepSeek sobre la ec. (76) de
Wang, que falla al verificarla —en `u=v` el vector `y` es puramente temporal, luego
`Q = E^2 (y^0)^4 != 0`, y el polinomio reproduce la evaluación directa—. Hizo falta una tercera
casa **con el artículo original en el lote** para zanjarlo. Las dos primeras rondas se habían
hecho heredando la transcripción, que era la laguna que Grok declaró.

**Procedencia del lote de esta ronda**, que también es un defecto señalado por las tres: el
original de de Brito–Eichhorn–Pfeiffer (arXiv:2301.13525) **no** iba entre las fuentes
enviadas, de modo que su cita del §4 sólo es cotejable a través de los documentos internos; y el
recontrol del `4 sqrt6/9` que el §1 atribuye a R6′ §3 tampoco es comprobable con el lote, porque
R6′ no se adjuntó. Las dos lagunas son de la misma clase que la de Wang en las rondas 2 y 3, y
la repetí después de haberla señalado.

La lección operativa, que vale más que el coeficiente: de mis **once** errores, diez los
encontró otra familia de modelos y uno lo encontré yo al calcular. **Ninguno lo encontré
releyendo lo que había escrito.** Y en la ronda de hoy, el único que estaba en minoría —una casa
contra dos— tenía razón: que la tesis «no contiene Weyl» es falso, y ni el voto de las otras dos
ni mi propia relectura lo detectaron. Un acuerdo de dos sobre tres no es una verificación.

---

## 8. Revisión ciega de esta nota — las tres casas

`revisiones/2026-10-10-cierre/`. Entrada idéntica para las tres (535 KB): esta nota, el
candidato enmendado, la auditoría, el resultado de q2, y como primarias Wang (1904.01034),
BBD (1510.04656), Belenchia (1510.04665), Dowker–Glaser (1305.2588) y la tesis de Pfeiffer.
No iba 2301.13525, y eso es un defecto que las tres señalaron (§7).

| casa | `N1` establecido | `N2` no establecido | `N3` BBD/Pfeiffer | `N4` prioridad | veredicto |
|---|---|---|---|---|---|
| `grok-4.6` | FIEL | FIEL | CORRECTA | CORRECTA | `APTA_CON_CORRECCIONES` |
| `deepseek-v4-pro` | FIEL | FIEL | CORRECTA | CORRECTA | `APTA_CON_CORRECCIONES` |
| `gpt-6-astra` | SOBREAFIRMA | SOBREAFIRMA | CORRECTA | INCORRECTA | `APTA_CON_CORRECCIONES` |

**Las tres coinciden en `N3`**, que era lo que más importaba porque imputa un paso inválido a
trabajo ajeno: las tres lo verificaron en los originales. Grok lo detalla hasta la identidad
(3.17) —`∂|f|/∂x = sgn(f) ∂f/∂x`, que no autoriza pasar desigualdades por un operador en `rho`—
y señala que (3.18)–(3.22) sustituyen `sqrt(-g)` y `phi` por normas supremas y **recién entonces**
aplican `O_d`, de modo que `A_{lambda,l}(n)` anula la comparación, no el integrando original.

**Y Astra, en minoría 1–2, tenía razón en lo factual.** Su `N4 = INCORRECTA` se apoyaba en que
la tesis sí menciona Weyl. Lo es: Grok lo escribe en su propio informe —*"en la tesis de
Pfeiffer, Weyl aparece una vez"*— y mi auditoría §6.3 lo tenía bien registrado. Las otras dos
casas dieron el `N4` por correcto en la sustancia y pasaron por encima del dato. Un voto no
arregla un hecho: corregido en §4.

Las once correcciones están aplicadas en el sitio donde tocaba, cada una con su marca y su
atribución. Las de más alcance son las de Astra sobre el §6 —que el fundamento de no continuar
es una obligación de prueba pendiente y no un no-go— y la fila 9 de la tabla de errores, que
registra el error que habilitó toda la cadena y que yo había omitido.

**Estado final de esta nota:** `APTA_CON_CORRECCIONES` por las tres casas, correcciones
aplicadas. Queda como registro del cierre.
