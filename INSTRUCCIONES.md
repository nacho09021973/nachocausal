# INSTRUCCIONES.md

Guía operativa para cualquier IA o agente que se conecte a `nachocausal`.

Este documento no sustituye a `CLAUDE.md`, `README.md` ni a la pre-registración
congelada. Su función es explicar, de forma directa, **qué maquinaria existe en
el repo** y **cuál es el flujo correcto de uso**.

## 1. Qué es este repo

`nachocausal` es un **benchmark de recoverability**, no una reclamación libre de
reconstrucción. El proyecto trabaja con una disciplina estricta:

- exploración (`dev/`) y confirmación (`results/`, docs congeladas) están separadas;
- los umbrales congelados no se tocan sin nueva pre-registración;
- la embedding oculta solo puntúa, no define el observable;
- ninguna IA debe sobredeclarar resultados.

Antes de actuar, lee como mínimo:

1. `CLAUDE.md`
2. `README.md`
3. `docs/preregistration.md`
4. este `INSTRUCCIONES.md`

## 2. Maquinaria disponible

### A. `/comite` — deliberación científica

Uso correcto:

- decisiones de frontera;
- pasos científicamente comprometidos;
- promoción de una idea a claim, spec o plan de trabajo serio;
- preguntas del tipo "¿debemos proceder?".

Qué hace:

- convoca un comité con varios roles y subagentes;
- produce un brief en `docs/comite/`;
- propone, pero no ejecuta pasos irreversibles.

No usar para:

- tareas triviales;
- comprobar si un número ya publicado es real;
- ejecutar código o cambiar umbrales.

### B. `/auditor` — auditoría de integridad

Uso correcto:

- antes de construir sobre resultados ya reclamados;
- para verificar que números, sellos y separación dev/validation son reales;
- para revisar si una afirmación ya escrita está respaldada.

Qué hace:

- ejecuta comprobaciones mecánicas;
- revisa sellos y claims;
- escribe un informe en `docs/auditor/`.

No usar para:

- decidir una línea científica futura;
- arreglar el repo por su cuenta.

### C. Deep externo — consultor advisory-only

Contrato:

- vive **fuera** del repo;
- ubicación esperada: `~/ai/deepmath/`;
- adaptador del repo: `scripts/consulting/deepmath_consult.py`;
- documentación: `docs/DEEPMATH_CONSULTING.md`;
- artefactos: `dev/consultations/deepmath/`.

Uso correcto:

- consulta externa no vinculante;
- apoyo conceptual o matemático;
- preparación de dossier con trazabilidad.

Límite:

- no cuenta como evidencia científica;
- no toca el path sellado;
- si falta el comando, debe fallar cerrado.

### D. NVIDIA externo — consultor advisory-only

Contrato:

- vive **fuera** del repo;
- ubicación esperada: `~/ai/nvidia-consult/`;
- adaptador del repo: `scripts/consulting/nvidia_consult.py`;
- documentación: `docs/NVIDIA_CONSULTING.md`;
- artefactos: `dev/consultations/nvidia/`.

Uso correcto:

- consulta externa no vinculante;
- apoyo de razonamiento o redacción técnica;
- mismo patrón de dossier + manifest + response.

Límite:

- no cuenta como evidencia;
- no guarda claves dentro del repo;
- si falta `NVIDIA_API_KEY` o el comando, debe fallar cerrado.

### E. `/alloy-verifier` — verificación formal acotada

Uso correcto:

- solo cuando una afirmación ya se ha traducido a un **modelo finito y relacional verificable**;
- para buscar contraejemplos o comprobar un `check`/`run` a alcance finito.

Contrato:

- modelos canónicos: `formal/alloy/`
- modelos exploratorios: `dev/alloy/`
- informes: `docs/alloy/`
- skill global: `~/.claude/skills/alloy_verifier/`
- documentación: `docs/ALLOY_VERIFICATION.md`

Límite:

- Alloy **no prueba** el claim físico general;
- Alloy solo da evidencia sobre el modelo codificado y el alcance finito;
- si no hay comando Alloy verificado, debe fallar cerrado.

## 3. Qué es canónico y qué no

Canónico:

- skills bajo `.claude/skills/`;
- documentación en `docs/`;
- modelos Alloy serios en `formal/alloy/`;
- notas de trabajo en `dev/`;
- consultorías externas archivadas en `dev/consultations/`.

No canónico por defecto:

- archivos `.als` sueltos en la raíz;
- pruebas rápidas;
- material temporal;
- cualquier salida no enlazada por docs o por una nota de verificación.

Si un modelo Alloy importa de verdad, promuévelo a `formal/alloy/` y crea su
nota en `docs/alloy/`.

## 4. Flujo correcto de uso

### Flujo 1 — decisión científica seria

1. leer contexto y reglas;
2. si la decisión construye sobre resultados ya reclamados, pasar primero por `/auditor`;
3. convocar `/comite`;
4. ejecutar solo pasos reversibles si el usuario lo pide;
5. no commit, no push, no validación sellada sin autorización explícita.

### Flujo 2 — consulta externa de apoyo

1. redactar la pregunta con alcance estrecho;
2. adjuntar contexto relevante;
3. usar Deep o NVIDIA a través de `scripts/consulting/`;
4. guardar dossier, manifest y response en `dev/consultations/...`;
5. tratar la respuesta como **advisory-only**;
6. si afecta a una decisión científica, llevarla luego a una nota `dev/` o al `/comite`.

### Flujo 3 — verificación Alloy

1. comprobar que el claim ya está traducido a un modelo finito;
2. verificar el comando Alloy local;
3. ejecutar `/alloy-verifier` o el comando equivalente;
4. guardar el informe en `docs/alloy/`;
5. explicitar siempre:
   - modelo;
   - comando;
   - alcance;
   - resultado;
   - límites de interpretación.

### Flujo 4 — desarrollo normal en `dev/`

1. trabajar en `dev/` cuando la idea aún no está cerrada;
2. no tocar umbrales congelados;
3. no reetiquetar exploración como evidencia;
4. si aparece una objeción lógica seria, se puede:
   - formalizar en Alloy;
   - elevar al comité;
   - o convertir en nota de trabajo explícita.

## 5. Orden recomendado entre herramientas

Regla simple:

- **¿es una decisión?** -> `/comite`
- **¿es una verificación de algo ya afirmado?** -> `/auditor`
- **¿es una consulta externa no vinculante?** -> Deep o NVIDIA
- **¿es una afirmación ya formalizada en un modelo finito?** -> `/alloy-verifier`

Orden típico sano:

1. nota `dev/`
2. Deep/NVIDIA si hace falta apoyo externo
3. Alloy si ya hay traducción formal
4. `/comite` para decidir
5. `/auditor` si se va a construir sobre claims ya publicados o a consolidar

No todo paso necesita todas las herramientas. Lo importante es **no saltarse la
disciplina**.

## 6. Reglas negativas

No hacer:

- commits o push sin autorización explícita del usuario;
- cambios de umbrales congelados;
- uso de resultados de validación como si fueran datos de exploración;
- presentar Deep, NVIDIA o Alloy como prueba física concluyente;
- confundir un contraejemplo lógico con un no-go físico completo;
- meter modelos, wrappers o claves dentro del repo si deben vivir fuera.

## 7. Estado conceptual actual de Alloy

En este momento, Alloy sirve como capa formal **lógica/combinatoria**.

Lectura correcta:

```text
logical counterexample != physical no-go
```

pero también:

```text
logical counterexample => the obstruction is not empty rhetoric
```

Así que Alloy puede apoyar una objeción formal acotada, pero no certificar por
sí solo embedding fiel, manifold-likeness, Poisson típico, curvatura, ni
convergencia al continuo.

## 8. Si eres una IA nueva en este repo

Haz esto primero:

1. lee `CLAUDE.md`;
2. lee `README.md`;
3. lee este archivo;
4. identifica si tu tarea es:
   - deliberación,
   - auditoría,
   - consulta externa,
   - verificación Alloy,
   - o trabajo exploratorio normal;
5. usa la herramienta mínima correcta;
6. deja trazabilidad;
7. no sobredeclares.
