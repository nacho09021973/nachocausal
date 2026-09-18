# Hoja de ruta semanal — 21–27 de septiembre de 2026

> **PLAN OPERATIVO REVISABLE.** Este documento organiza una semana de trabajo; no es una
> pre-registración, no abre S2, no autoriza simulaciones ni consumo de semillas y no eleva ningún
> resultado a claim científico.

## Estado de partida

- La reorganización del repositorio está preparada en la rama
  `research/causal-fidelity-bridge`.
- `old/` conserva material auxiliar o sustituido; el mapa operativo es
  [`ESTADO_ACTIVO.md`](../ESTADO_ACTIVO.md).
- El contrato de fidelidad causal está en estado
  `NEW_FRONT / MINIMAL_CONTRACT / UNPROVED`:
  [`CAUSAL_FIDELITY_MINIMAL_CONTRACT.md`](../research_program/causal_fidelity/CAUSAL_FIDELITY_MINIMAL_CONTRACT.md).
- El frente de tangente geométrico permanece bloqueado por las obligaciones identificadas en el
  comité 051: gobernanza, consistencia de la convención de normalización y corrección de los
  tokens de estado. No se lee `PROVED` como puerta de apertura.
- El sello del benchmark y los instrumentos de validación no se tocan.

## Objetivo único de la semana

Dejar el repositorio gobernable y las dos fronteras abiertas expresadas con contratos mínimos,
sin confundir orden documental con evidencia matemática.

## Secuencia cerrada

### 1. Consolidación del repositorio

- Commit y push de la reorganización, el mapa operativo, las referencias corregidas y esta hoja.
- Excluir explícitamente del commit los WIP actuales: `research_program/puente_3p1/`, el contrato
  no preparado para promoción si no forma parte del commit de organización, y `.webui_secret_key`.
- Verificar igualdad entre `HEAD` local y la rama remota después del push.

### 2. Auditoría de gobernanza del frente geométrico

- Registrar como obligación abierta la brecha de perímetro señalada por el comité 051.
- No emitir `GEOMETRIC_TANGENT_CLASSIFICATION = PROVED` mientras no estén reparados el criterio
  literal, la normalización y los tokens admitidos.
- No abrir S2 aunque aparezca una condición técnica aislada.

### 3. Contrato de fidelidad causal

- Revisar definiciones y cuantificadores del contrato mínimo.
- Especificar, sin ejecutar confirmación, el primer caso mínimo y el control que cambia solo la
  dinámica.
- Mantener separados `PASS`, `FAIL` y `OPEN`; cualquier falta de definición o prueba conserva
  el estado `OPEN`.
- No reutilizar B1.6/B1.7 como evidencia del nuevo frente y no convertirlos en una afirmación
  dinámica general.

### 4. Cierre semanal

El domingo 27 se debe producir solo un informe de estado con:

```text
REPOSITORY_REORGANIZATION = COMMITTED_AND_PUSHED | OPEN
GEOMETRIC_TANGENT_GATE = BLOCKED | READY_FOR_REVIEW
CAUSAL_FIDELITY_CONTRACT = OPEN | PASS | FAIL
S2 = NOT_OPEN
NEW_RUNS = NOT_AUTHORIZED
SEALED_BENCHMARK = UNCHANGED
```

## Fuera de alcance

- simulaciones o ejecuciones confirmatorias;
- consumo de semillas reservadas;
- cambios de umbrales o instrumentos sellados;
- promoción de `puente_3p1`, B1.6/B1.7 o del contrato de fidelidad a resultado científico;
- auditoría bibliográfica de novedad;
- publicación o modificación del manuscrito editorial.

## Criterio de parada

Si una tarea exige ampliar el contrato, cambiar la convención, introducir un segundo observable,
abrir S2 o usar datos para redefinir el criterio, se detiene y se registra como decisión pendiente.
