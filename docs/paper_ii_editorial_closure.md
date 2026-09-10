# Paper II — cierre editorial

Fecha: 2026-09-10.

```text
PAPER_II_SCIENTIFIC_CORE=CLOSED
PAPER_II_EDITORIAL_SOURCE=CLOSED
NOGO_B=CLOSED
PROBLEMA_A=OPEN_NOT_REQUIRED
FORMAT=MARKDOWN
SUBMISSION_OR_PUBLICATION=NOT_PERFORMED
```

## Documento de lectura

El manuscrito canónico en español es [Geometría local y horizontes globales en órdenes causales Schwarzschild 1+1](../manuscrito/paper_ii_es.md). Contiene título, autoría, resumen, introducción, definiciones, dos teoremas, sus demostraciones, apéndice técnico y referencias. La autoría y el contacto se conservan de los manuscritos existentes del mismo autor.

El contrato científico y la prueba congelada de B permanecen en [paperII_nogo_B_congelado.md](../paperII_nogo_B_congelado.md). Su cierre científico fue registrado en el commit `32a2698`. La versión editorial desarrolla la exposición y reúne las dependencias del resultado positivo; no introduce un nuevo frente de investigación.

## Arquitectura final

| Parte | Contenido | Ubicación |
|---|---|---|
| Modelo | Caja fija, volumen natural, entorno relativamente compacto y canal observado | §2 |
| Geometría común | Carta regular, factores conformes, isometrías y causalidad fuerte | §3 |
| Teorema positivo | Altura total y altura cruzada, límite uniforme y tiempo propio restringido a la caja | §4 |
| No-go B | Volumen, ausencia de relaciones nuevas, infinitos nulos futuros, ley exacta y minimax | §5 |
| Límites de interpretación | Clase de extensiones, papel del embedding, A abierto y ausencia de extrapolación dimensional | §6 |
| Transferencia compacta | Soportes con umbral, control de fronteras, rejillas y poissonización | Apéndice A |

La altura total es un observable del poset. La altura cruzada usa la partición Schwarzschild conocida. El manuscrito no presenta esta partición como reconstruida a partir del dato no etiquetado.

## Procedencia y estado de las notas anteriores

Las siguientes notas se conservan con sus fechas, advertencias y estados históricos. Sus etiquetas de revisión pendiente documentan su etapa de desarrollo; el estado de cierre adoptado para Paper II se registra en el contrato y en esta nota. No se reescriben ejecuciones ni auditorías anteriores.

| Fuente | Material trasladado |
|---|---|
| [Reducción double-null](../dev/PAPER2_DOUBLE_NULL_REDUCTION.md) | Métrica y coordenadas nulas por bloques |
| [Aproximación rectangular E2](../dev/PAPER2_E2_RECTANGULAR_APPROXIMATION.md) | Accesibilidad, reemplazo de huecos, recorte y control de fronteras |
| [Descomposición finita O4](../dev/PAPER2_HORIZON_O4_FINITE_DECOMPOSITION.md) | Separación de cadenas exteriores e interiores |
| [Umbral y carta regular](../dev/PAPER2_HORIZON_THRESHOLD_LIMIT.md) | Perfiles, banda del horizonte, malla monótona, máximo cruzado y transferencia compacta |
| [Auditoría de Deuschel–Zeitouni](../dev/PAPER2_DEUSCHEL_ZEITOUNI_APPLICABILITY.md) | Dominio preciso del teorema externo y obligaciones de transferencia |
| [Contrato corregido y prueba de B](../paperII_nogo_B_congelado.md) | Testigos y B.1–B.3, acoplamiento Poisson y minimax |

La identificación geométrica de los perfiles con tiempo propio se expone en §4.4 usando la accesibilidad de B.2. Se hace visible la concatenación dentro de la caja y la aproximación de los extremos del intervalo de umbrales; no se identifica la distancia restringida con una distancia ambiente.

## Decisiones editoriales fijadas

- Preservar exactamente todo el entorno relativamente compacto \(U_0\).
- Mantener la fórmula completa del rayo \(\gamma_p(\lambda)=(U_p,V_p+\lambda)\), \(\lambda\ge0\), y las igualdades completas de orden, volumen y leyes.
- Distinguir el límite asintótico del Teorema 1 de la identidad exacta para cada \(\rho>0\) del Teorema 2.
- Reservar la afirmación global de horizonte al par del No-go B.
- Mantener A abierto y fuera de las obligaciones del artículo.
- No incorporar material de Paper III al manuscrito de Paper II.

El cierre editorial corresponde al original Markdown. La restricción vigente sobre LaTeX y PDF se mantiene: no se generan ni modifican esos formatos. No se declara envío a revista, publicación, revisión externa ni formalización Lean completa. Los archivos vacíos `LaTeX` y `PDF` de la raíz son marcadores históricos y no entregables del artículo.

## Verificación del cierre

La revisión editorial comprueba la integridad de las fórmulas en la fuente, delimitadores matemáticos y entornos, referencias internas, enlaces locales y alcance del diff. No requiere simulaciones, nuevas semillas ni ejecución de pruebas científicas. Los límites y predicados globales se sostienen en las demostraciones escritas, no en estos controles de formato.

Paper II queda fuera de investigación activa. Una revisión independiente que encuentre un fallo matemático es motivo de reapertura; la elección del siguiente frente no lo es.
