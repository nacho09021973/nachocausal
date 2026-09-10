# Hoja de ruta de Paper III — calibración 3+1D antes de interpretar truncaciones

Fecha de decisión: 2026-09-10.

```text
PAPER_III_STATUS=PLANNING_ONLY
PAPER_III_ROUTE=1
PHASE_1=3P1_MINKOWSKI_ALEXANDROV_CALIBRATION
PHASE_2=STATIC_SPHERICAL_EXCISION
PHASE_3=SCHWARZSCHILD_3P1=DEFERRED
NEW_VALIDATION_RUNS=NOT_AUTHORIZED
NEW_OBSERVABLES=NOT_AUTHORIZED
HORIZON_CLAIM=NONE
```

Esta hoja ordena el trabajo preparatorio de Paper III. No es una
pre-registro, no congela semillas ni umbrales y no autoriza nuevos barridos.
Su función es impedir que una corrección de tamaño finito se interprete como
una señal geométrica.

## Pregunta de Paper III

La primera pregunta es deliberadamente estrecha:

> En sprinklings de Poisson sobre intervalos de Alexandrov de Minkowski
> \(3+1\), ¿cómo se aproxima \(L/N^{1/4}\) al régimen de gran \(N\), y qué
> parte de la desviación observable puede atribuirse únicamente a tamaño finito?

Aquí \(L\) es la longitud de la cadena máxima entre los extremos del intervalo
y \(N\) su cardinalidad interior. Esta fase no estudia horizontes, detectores,
localización, reconstrucción métrica ni Schwarzschild.

La razón del orden es que la ley de Brightwell–Gregory tiene como dominio
seguro los intervalos de Alexandrov. No se usará como una ley universal para
futuros truncados por una caja.

## Evidencia que ya existe

La nota exploratoria [PAPER3_3P1_SCALE_NOTES](../dev/PAPER3_3P1_SCALE_NOTES.md)
y sus artefactos contienen:

| Artefacto | Estado actual |
|---|---|
| `dev/explore_3p1_bg_reference_precision_results.json` | 8 semillas, \(N\le 32000\), intervalo de Alexandrov |
| `dev/explore_3p1_bg_reference_results.json` | pierna preliminar de 3 semillas |
| `dev/explore_3p1_scale_calibration_results.json` | caja truncada, \(\rho=500,\ldots,8000\), 3 semillas |
| `dev/verify_3p1_notes_figures.py` | verificador de procedencia; pasa con `ALL FIGURES MATCH` |

Los valores existentes muestran \(L/N^{1/4}\) creciente y una pendiente
efectiva cercana a \(0.29\), no \(0.25\), en el rango accesible. Eso es una
medida exploratoria de transitorio, no una refutación del límite. La deriva de
\(R=L^4/V\) impide usar \(R\) como calibrador antes de cerrar esta fase.

## Principios de alcance

1. Las coordenadas se usan para generar y puntuar el embedding; cualquier
   observable promovido debe definirse a partir del causet y su cardinalidad.
2. El intervalo de Alexandrov es la referencia matemática. Una caja o una
   región con interfaz no se trata como intervalo sin una prueba adicional.
3. Cada cifra nueva debe tener un generador permanente, un artefacto de salida,
   semillas declaradas y un verificador independiente.
4. La fase exploratoria no consume semillas confirmatorias ni toca instrumentos
   sellados del repositorio.
5. \(R=L^4/V\) queda aparcado. Puede reaparecer como funcional de forma solo
   después de una calibración de tamaño finito que permita separar ambos
   efectos.
6. La excisión esférica estática es una interfaz timelike de control. No es un
   horizonte nulo y cualquier resultado allí será necesario, pero no suficiente,
   para una afirmación sobre horizontes.

## Fase 0 — contrato matemático y auditoría de entrada

Objetivo: convertir los datos exploratorios en un contrato de calibración sin
afirmar más de lo que miden.

Entregables:

- definición exacta del intervalo de Alexandrov en Minkowski \(3+1\);
- convención de \(N\), tratamiento de los dos extremos y definición de \(L\);
- relación entre \(N\), intensidad \(\rho\), volumen y tiempo propio;
- tabla única de semillas, tamaños, número de réplicas y artefactos;
- auditoría de que la nube es Poisson homogénea respecto al volumen Minkowski;
- separación explícita entre el límite conocido y la corrección finita que se
  quiere medir.

Puerta de salida:

```text
GATE_0=PASS iff definitions, provenance, endpoint convention and scope are fixed
```

Si hay ambigüedad en el conteo de extremos, en la normalización o en la
procedencia de una cifra, la fase no avanza.

## Fase 1 — calibración de tamaño finito en Alexandrov (3+1)

Objetivo: describir empíricamente la aproximación a \(L/N^{1/4}\) sin convertir
la pendiente accesible en exponente asintótico.

Trabajo permitido después de `GATE_0`:

- reproducir primero los artefactos existentes;
- elegir una parametrización de corrección finita antes de mirar resultados
  nuevos;
- comparar tamaños y semillas mediante intervalos descriptivos, no mediante un
  umbral post hoc;
- comprobar sensibilidad a la convención de extremos y al algoritmo de cadena;
- verificar que el caso Minkowski intervalar reproduce la geometría continua
  usada para generar el intervalo.

El objeto primario es una curva de calibración de \(L/N^{1/4}\) frente a \(N\).
El objeto secundario es la estabilidad de esa curva entre semillas. No se
promueve todavía \(R\), \(L^4/V\), ni un exponente ajustado como ley universal.

Puerta de salida:

```text
GATE_1=PASS iff the finite-size description is reproducible,
         convention-stable, and clearly separated from the asymptotic claim
GATE_1=OPEN iff the accessible range cannot distinguish competing corrections
GATE_1=FAIL iff a provenance, implementation, or causal-order check fails
```

Un `OPEN` deja Paper III en calibración; no autoriza saltar a una geometría con
interfaz.

## Fase 2 — control de excisión esférica estática

Esta fase se abre solo con `GATE_1=PASS` o con una decisión explícita que
mantenga el resultado como estudio de control finito.

Modelo: Minkowski \(3+1\) con una bola espacial estática excindida. La
causalidad se define mediante

\[
p\prec q
\quad\Longleftrightarrow\quad
t_q-t_p\ge d_{\mathrm{obs}}(x_p,x_q),
\]

donde \(d_{\mathrm{obs}}\) es la distancia espacial mínima entre los puntos
evitando la bola. En los casos relevantes, \(d_{\mathrm{obs}}\) se obtiene por
tramos tangentes y arco de la esfera. Antes de cualquier simulación debe
probarse que es una métrica y que la relación causal resultante es transitiva.

Entregables:

- derivación geométrica de \(d_{\mathrm{obs}}\), incluidos tangencias y casos
  degenerados;
- verificador numérico de la fórmula contra una construcción independiente;
- definición previa de la región observada y del control Minkowski emparejado;
- comparación de \(L\), volumen futuro y, solo si la calibración lo permite,
  un funcional de forma;
- declaración explícita de que la frontera es timelike.

Puerta de salida:

```text
GATE_2=PASS iff causalidad, sprinkling, control emparejado and scope are verified
GATE_2=FAIL iff the excision creates non-transitive or implementation-dependent order
```

Un resultado positivo en esta fase significa que una interfaz timelike altera
la estadística de futuros de una forma controlable. No significa que exista un
horizonte ni que un poset lo localice.

## Fase 3 — decisión sobre funcionales de forma

Solo después de las dos calibraciones se decide si tiene sentido reabrir

\[
R(i)=\frac{L(i)^4}{V(i)}.
\]

La decisión debe responder, con datos ya calibrados:

- cuánto de la deriva de \(R\) queda explicado por la corrección finita de
  \(L\);
- si el control de excisión introduce una diferencia residual estable;
- si esa diferencia depende del tamaño de la región o de la densidad;
- si el funcional conserva significado al cambiar la forma del futuro.

Resultados posibles:

```text
R_SHAPE_OPEN       = evidencia compatible, teoría insuficiente
R_SHAPE_REJECTED   = la deriva queda explicada por tamaño finito
R_SHAPE_CANDIDATE  = diferencia residual reproducible, sin claim de horizonte
```

No se permite etiquetar `R` como calibrador universal ni como localizador de
horizonte.

## Fase 4 — preflight Schwarzschild (3+1)

Esta fase no se abre automáticamente al pasar las anteriores. Requiere un
contrato nuevo y separado.

Obligaciones previas:

- especificar la medida de sprinkling, incluyendo el factor
  \(r^2\sin\theta\);
- definir una relación causal verificable en Schwarzschild \(3+1\);
- resolver el problema de llegada nula más temprana, con control cerca de
  \(r=3M\);
- fijar el canal observado y separar embedding de entrada order-only;
- construir controles Minkowski con la misma geometría observada;
- decidir si el objetivo es una ley de escala, una propiedad de forma o una
  pregunta de recoverability.

Hasta que estas obligaciones estén satisfechas,

```text
SCHWARZSCHILD_3P1_EXECUTION=BLOCKED
```

El bloqueo es de contrato y verificabilidad, no una conclusión científica
negativa.

## Calendario lógico

El orden de trabajo es secuencial, no temporal:

```text
Fase 0: contrato y auditoría de entrada
    -> Gate 0
Fase 1: Alexandrov 3+1 finito
    -> Gate 1
Fase 2: excisión esférica timelike
    -> Gate 2
Fase 3: decisión sobre R como forma
    -> claim ceiling
Fase 4: preflight Schwarzschild 3+1
    -> contrato independiente, no ejecución automática
```

No se abre una fase por haber consumido una fecha o un presupuesto. Se abre
solo por pasar su puerta lógica y conservar el alcance.

## Primera iteración de trabajo

La primera iteración queda limitada a la Fase 0:

1. leer la nota de escala y los cuatro artefactos listados arriba;
2. reconciliar tamaños, semillas, réplicas, conteo de extremos y normalizaciones;
3. ejecutar únicamente el verificador ya existente para confirmar procedencia;
4. redactar el contrato de calibración y registrar cualquier ambigüedad como
   bloqueo de `GATE_0`.

El resultado de esta iteración será un contrato revisable y una tabla de
entradas. No generará nuevos datos, no elegirá un ajuste a posteriori y no
abrirá la excisión esférica.

## Claim ceiling de Paper III

Hasta el cierre de la Fase 1, el claim máximo permitido es:

> En el rango explorado, la longitud de cadena en intervalos de Alexandrov
> Minkowski \(3+1\) muestra una corrección de tamaño finito que debe
> caracterizarse antes de interpretar funcionales de futuros truncados.

Después de la Fase 2 puede añadirse:

> Una excisión esférica estática proporciona un control timelike para estudiar
> cómo una interfaz modifica futuros truncados en Minkowski \(3+1\).

Quedan fuera de este claim ceiling: horizontes, localización, reconstrucción
de \(r=2M\), Schwarzschild \(3+1\), Kerr, universalidad de \(R\) y transferencia
automática desde Paper II.

## Ejecución de la Fase 0

La primera iteración está ejecutada y registrada en
[el contrato de calibración de la Fase 0](paper_iii_fase0_contrato.md), con
verificador permanente en `dev/verify_3p1_phase0_contract.py`. Resultado:

```text
GATE_0=BLOCKED   (9 bloqueos abiertos; ningún barrido ejecutado)
```

## Inventario de dependencias

- [Contrato de calibración de la Fase 0](paper_iii_fase0_contrato.md).
- [Notas exploratorias de escala](../dev/PAPER3_3P1_SCALE_NOTES.md).
- [Pierna intervalar](../dev/explore_3p1_bg_reference.py).
- [Calibración exploratoria de caja](../dev/explore_3p1_scale_calibration.py).
- [Verificador de cifras](../dev/verify_3p1_notes_figures.py).
- [Brightwell–Gregory, referencia bibliográfica local](../biblioteca/derived-md/Dynamics_of_Causal_Sets_arXiv_gr-qc0212064.md).
- [Notas de causalidad Schwarzschild (3+1)](../biblioteca/Investigación Causalidad Schwarzschild R19M.md).

Los dos últimos recursos son dependencias de lectura y no autorizan por sí
solos un resultado nuevo. Toda promoción a resultado confirmatorio requerirá
un contrato, artefactos reproducibles, auditoría independiente y una decisión
de alcance separada.
