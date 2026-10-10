# Auditoría de solapamiento: `poset_phase` y `nachocausal`

Fecha de revisión: 2026-09-11  
Fuente externa revisada: [Zenodo 10.5281/zenodo.19133012](https://zenodo.org/records/19133012) y [repositorio `unicome37/poset_phase`](https://github.com/unicome37/poset_phase).  
Código local revisado: `/home/adnac/poset_phase`, commit `4a284f1`.

## Veredicto corto

Hay solapamiento metodológico sustantivo y debe citarse como antecedente cercano. No hay identidad de objetivo demostrada: `poset_phase` estudia selección de fases geométricas en ensembles de posets mediante acciones, entropía y dinámica; `nachocausal` estudia la recuperabilidad order-only de una frontera asociada al horizonte en un parche Schwarzschild, con contratos de estimación, gates y validación ciega.

La novedad de `nachocausal` no puede sostenerse globalmente como «usar órdenes causales para recuperar estructura geométrica». Debe formularse, si sobrevive la auditoría, alrededor del canal, el objetivo, el observable, el protocolo y el resultado concreto de localización.

## Coincidencias verificadas

| Eje | `poset_phase` | `nachocausal` | Riesgo |
|---|---|---|---|
| Objeto | Posets finitos/causal orders | Causal sets finitos y posets observados | Bajo: objeto común amplio |
| Geometría | Familias Lorentzianas 2D/3D/4D frente a KR | Benchmark Schwarzschild 1+1D y objetivo 3+1D | Medio |
| Entropía | Extensiones lineales exactas y entropía combinatoria | Entropía/intervalos/coarse-graining en varias líneas | Medio-alto |
| Dimensión | Penalización de consistencia dimensional y recuperación de dimensión | Dimensión, canales order-only y límites de identificabilidad | Medio-alto |
| Selección estructural | Funcional de coste `F7`, ablation y Pareto | Selectores, gates y familias candidatas | Alto para C4/C5 y selectores |
| Robustez | Permutación, Monte Carlo, ablación, CV y nuevas semillas | Pre-registro, semillas selladas, controles y auditoría | Bajo: disciplina común, no mismo resultado |
| Dinámica | Metropolis, swaps y simulated annealing | No es el mecanismo central del benchmark vigente | Bajo |
| Espectro | Distancia Wasserstein y deriva de entropía espectral | Bloques espectrales/C5 aparecen como línea examinada | Alto si se presenta como nuevo sin comparación |

## Diferencias que preservan una frontera de novedad

1. `poset_phase` pregunta qué fase o familia gana bajo una acción/ensemble. `nachocausal` pregunta si un estimador calculado desde el orden y los conteos localiza una frontera física asociada a `r=2M`.

2. En `poset_phase`, el objeto central es la competencia entre estructuras generadas o muestreadas, con claims de transición/dominancia dentro de familias y tamaños finitos. En `nachocausal`, el resultado empírico principal está ligado a una comparación Schwarzschild–Minkowski, un objetivo de localización y un protocolo congelado.

3. El salto 4D de `poset_phase` es un resultado de selección/dominancia de posets Lorentzianos bajo acciones de consistencia. No equivale a localizar un horizonte Schwarzschild 3+1D sin coordenadas en la entrada del estimador.

4. La rama Fisher de `nachocausal` estudia retención de información en un canal de cociente/isomorfismo para scores separables. En la documentación examinada de `poset_phase` no aparece ese mismo teorema de retención Fisher como resultado central.

## Riesgos concretos para nuestras afirmaciones

- No usar «primero», «nuevo» o «sin precedente» para funcionales estructurales, entropía de posets, selección de dimensión, competencia Lorentziana–KR, coarse-graining o diagnósticos de robustez sin incorporar `poset_phase` y sus versiones previas.
- Revisar la línea C5/espectral: el repositorio externo usa Wasserstein, entropía espectral y selección estructural; cualquier claim nuestro debe especificar observable, entrada, target y null.
- Revisar la línea de entropía jerárquica: `poset_phase` declara una relación entre profundidad jerárquica y entropía combinatoria, incluso con intervenciones. No es automáticamente el mismo análisis que el nuestro, pero sí es un antecedente directo de la familia conceptual.
- Revisar el lenguaje sobre 3+1D: la existencia de experimentos 4D en `poset_phase` elimina la posibilidad de presentar «posets Lorentzianos 4D» como espacio inexplorado en general. La diferencia debe estar en el problema de horizonte y el canal order-only.

## Qué no se ha establecido todavía

Esta auditoría no demuestra prioridad ni equivalencia científica. Se ha comparado el registro Zenodo, el README y el árbol/código documentado del repositorio. Falta una lectura línea a línea de los tres manuscritos y de los scripts que implementan F7, Prediction A y Prediction C, además de comparar definiciones matemáticas y protocolos de datos.

## Acción recomendada

Antes de ampliar `nachocausal`:

1. Añadir `poset_phase` a la matriz de novedad de la bibliografía.
2. Construir una tabla de correspondencia formal para cada observable candidato: entrada permitida, ley de muestreo, variable objetivo, baseline, control y claim.
3. Reescribir cualquier claim de novedad amplio como claim de canal/objetivo/protocolo.
4. No importar ideas de `poset_phase` a una validación confirmatoria sin un contrato nuevo y sin separar exploración de confirmación.
5. Mantener abierta la posibilidad de que alguna línea propia —en particular la localización order-only de frontera Schwarzschild y el teorema Fisher del canal unlabeled-poset— siga siendo diferenciada, pero etiquetarla como «requiere auditoría de prioridad» hasta completar la comparación de manuscritos.

## Relación con el estado actual

El README de `nachocausal` ya limita el resultado a localización en un parche finito 1+1D y declara que no es reconstrucción métrica ni resultado 3+1D. Esa formulación es compatible con la evidencia comparada y debe conservarse. Véanse [README.md](../README.md), [la hoja de ruta de septiembre](hoja_de_ruta_septiembre_2026.md) y los documentos de `research_program/` sobre observables y auditoría de prioridad.
