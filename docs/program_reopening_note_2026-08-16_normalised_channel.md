# Nota de reapertura acotada — `NC-0`, canal normalizado `sigma(M)`

```text
ESTADO: FIRMADA — NC-0 AUTORIZADO / NOT_YET_EXECUTED
FECHA: 2026-08-16
AMPLIA: docs/program_reopening_note_2026-07-31.md
NO_REVOCA: docs/program_closure_note_2026-07-30.md
NO_REABRE: EF-0--EF-8, EF-4/C1 ni reconstruccion de horizonte
SELLO: intacto — no se toca
SEMILLAS: ninguna
EJECUCION: AUTORIZADA SOLO DENTRO DE LA LISTA CERRADA DE §4
```

## 1. Por qué hace falta una nota nueva

La regla §6.1 de la reapertura del 31 de julio fija que nada entra sin una nueva
nota firmada. El cierre genealógico de EF-4 no autoriza otra línea: únicamente
establece que el barrido a `rho` pequeño no informa sobre la sucesión formal y que
`Q_{2,n}->0`, aun si quedase demostrado, es un error absoluto que puede colapsar a
la vez que la varianza total.

La línea acotada `NC-0` no intenta reconstruir ni localizar un horizonte. Estudia un
límite de información del canal ya congelado `sigma(M)` en `fixed-n`, `d=2`, con
el estimando lateral relativo existente. No introduce un selector, observable o
target nuevo. La duración `ell` se usa únicamente para puntuar el canal, nunca para
definir `M`, `S` ni una decisión observable.

## 2. Pregunta exacta

Para cada lado `h in {PAST,FUTURE}` y todo `n` para el que el denominador sea
positivo, defínase

\[
T_n^h=
\frac{
  E[\operatorname{Var}(\ell\mid M,n,h,S)\mid n,h,S]
}{
  \operatorname{Var}(\ell\mid n,h,S)
}
=1-(\rho_{\max,n}^h)^2.
\]

La igualdad es el Lema 3 de
`emergencia/P1a_count_volume_canal_sigma_m_d2.md`. La pregunta autorizada es:

\[
\text{¿vale }\liminf_{n\to\infty}T_n^h>0
\text{ para cada lado }h?
\]

Antes de atacar el límite debe demostrarse o tiparse la positividad eventual de
`Var(ell|n,h,S)`. Si el denominador se anula o su control asintótico no está
disponible, no se sustituye el cociente por el error absoluto.

El alcance es exclusivamente `sigma(M)`. Demostrar ese `liminf` positivo probaría
que, para cada lado, el mínimo del error cuadrático normalizado sobre todos los
predictores medibles respecto de `sigma(M)` queda acotado lejos de cero a lo largo
de la cola: ninguna función de `M` recupera `ell` con riesgo relativo tendente a
cero. Esto establece una obstrucción asintótica del canal `COUNT_VOLUME`/`M` solo
—pérdida de información, no defecto del estimador—, pero no demuestra recuperación
por ningún canal ni se transfiere a una cuádrupla enriquecida, al poset completo o
a reconstrucción de horizonte.

Un resultado negativo no sería un no-go para la cuádrupla ganadora, un canal
enriquecido ni el poset completo.

## 3. Estado previo que debe preservarse

```text
CHANNEL_REDUCTION_LEMMAS = PROVED
SEALED_SAMPLE_T_EMP = EXACT_FINITE_SAMPLE_IDENTITY
SEALED_SIZES = 64,96,128
SEALED_SIDES = PAST,FUTURE
T_EMP_RANGE = 0.6773_TO_0.7175
POPULATION_STATUS = STRONGLY_SUPPORTED_UNDER_IID_NOT_CLOSED_FORM_THEOREM
POPULATION_INTERVAL = NONE
ASYMPTOTIC_STATUS = OPEN
AUDIT_STATUS = PENDING_INDEPENDENT_RE_AUDIT_ROUND_4
```

Los seis valores de `T_emp` son identidades sobre la muestra sellada, no estimaciones
de `liminf T_n^h`. Tres tamaños no establecen una meseta asintótica. `T_xfit` tampoco
es una cota poblacional y los múltiplos de `SE_infl` no son intervalos demostrados.
Ningún texto de `NC-0` podrá elevar esos diagnósticos.

El falsificador EF-4, sus familias prescritas y su cap no son evidencia para esta
pregunta. Los runs existentes deben revisarse antes de proponer datos, scripts o
dependencias nuevas.

## 4. Único trabajo autorizado

`NC-0` es un preflight documental y matemático, no un run científico. Orden
obligatorio:

1. completar la re-auditoría independiente de ronda 4 de
   `emergencia/P1a_count_volume_canal_sigma_m_d2.md`, incluidos la definición
   literal de `S`, el ANOVA empírico exacto y la función de influencia;
2. reejecutar, si la auditoría lo necesita, únicamente el script determinista y de
   solo lectura ya existente
   `emergencia/p1a_count_volume_canal_sigma_m_d2.py` sobre los artefactos sellados;
3. fijar sin ambigüedad la relación entre `T_emp`, el objeto poblacional `T_n^h` y
   la condición de positividad del denominador;
4. inventariar los runs y artefactos existentes y declarar qué información falta;
5. formular una condición matemática correcta de masa y separación, o una cota
   equivalente, que sería suficiente para `liminf T_n^h>0`, sin afirmar que dicha
   condición se cumple;
6. emitir exactamente uno de los terminales de §5.

**Superficie científica autorizada:** únicamente
`emergencia/P1a_count_volume_canal_sigma_m_d2.md`. La nota de reapertura solo puede
actualizarse para registrar firma y terminal. No se crea código, tabla, figura ni
artefacto nuevo.

## 5. Terminales precomprometidos de `NC-0`

```text
NC0_READY_FOR_ANALYTIC_ATTACK
  La auditoría pasa; T_n^h y su denominador quedan bien definidos; se aísla una
  obligación analítica no vacua. No demuestra el liminf y cualquier ataque posterior
  requiere otra nota.

NC0_BLOCKED_BY_AUDIT
  Aparece una incidencia material en la identidad, los datos sellados o su lectura.

NC0_BLOCKED_BY_DENOMINATOR_ASYMPTOTICS
  El numerador puede estudiarse, pero no existe control suficiente de
  Var(ell|n,h,S) para formular el cociente asintótico.

NC0_BLOCKED_BY_SELECTION_CONDITIONING
  La ley condicionada por S impide obtener la masa/separación necesaria y el hueco
  queda tipado exactamente.

NC0_ALREADY_DECIDED_IN_EXISTING_RECORD
  Una prueba ya presente decide la pregunta; se cita y no se duplica trabajo.
```

La precedencia es: incidencia material de auditoría; objeto mal definido por el
denominador; bloqueo por selección; resultado ya existente; preparación para ataque.

## 6. Prohibiciones expresas

- ninguna simulación, muestreo, semilla o dato nuevo;
- ningún script, dependencia, selector, observable o estimando nuevo;
- ningún cambio de `MIN_COVERAGE_LEX`, `M`, `S` o del gate `0.80`;
- ninguna reapertura de EF-4/C1, histogramas, caps o puentes desde `rho` fijo;
- ningún resultado sobre horizontes, escala absoluta, `d>=3` o el poset completo;
- ninguna modificación de manuscritos, resultados sellados o `thresholds.py`;
- ninguna afirmación de consistencia, no-go, prioridad o novedad a partir de tres
  tamaños.

## 7. Test de terminado

`NC-0` termina solo si el único fichero científico autorizado contiene:

1. auditoría de ronda 4 con comandos y anclajes verificables;
2. definición poblacional exacta de `T_n^h` y condición del denominador;
3. inventario de evidencia existente, separando muestra sellada y población;
4. una obligación analítica explícita o un bloqueo tipado;
5. exactamente un terminal de §5 y ningún lenguaje más fuerte.

## 8. Firma

```text
FIRMADA_POR: Ignacio (PI)
FECHA: 2026-08-16
DECISION_NC0: AUTORIZADO
AUTORISED_SCOPE: lista cerrada de §4; un solo fichero científico
NOT_AUTHORISED: todo lo listado en §6; cualquier ataque posterior al preflight
BRANCH: agent/close-ef4-open-normalised-channel
```

La autorización queda activa en esta rama. `NC-0` está abierto exclusivamente para
el preflight de §4; no se ha ejecutado todavía ninguna de sus obligaciones.
