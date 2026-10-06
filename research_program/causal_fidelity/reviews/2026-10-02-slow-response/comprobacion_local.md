# Comprobación local previa a la revisión externa

Fecha: 2026-10-02. Documentos objetivo: commit 71a5adf.
Estado: comprobación del autor; no revisión independiente.
Herramienta de preparación: ~/herramientas @ 0137a63.

Se releen las reglas y se comprueban algebraicamente estos pasos:

- Dos cadenas con 2n-1 y 3n-1 interiores y dos extremos dan N_n=5n;
  las únicas rutas saturadas tienen longitudes 2n y 3n.
- Una ruta de ln coberturas multiplica exp(-gamma/n) ln veces y produce
  exp(-l gamma). Subdividir una cobertura en r mantiene su peso total.
- La integral de |sqrt(n) f(k)|^2 en una celda de longitud 1/n es |f(k)|^2;
  esto comprueba la isometría. Los retardos enteros 2 y 3 transportan
  exactamente celdas en celdas, sin interpolación del retardo.
- Un modo coseno macroscópico fijo está finalmente bajo el corte discreto.
  La aproximación por valores en centros de celda converge para ese modo;
  densidad y norma de proyector <=1 extienden el argumento a cada función
  fija de L2. No hay aquí una prueba uniforme para fuentes variables con n.
- El perfil constante pertenece al sector y tiene norma uno. Las fracciones
  de ventana observables son 1/2 y 1/4. La primera lectura es 3/4=192/256;
  la segunda es 9/32+27/256=99/256; la diferencia es 93/256. La integral
  sobre los dos tramos retardados reproduce esos factores.
- La primera amplitud de la segunda dinámica es 9/16>1/2: ambas primeras
  llegadas son 2n. La igualdad de llegada no compara amplitudes ni lecturas.

No se identifica un error nuevo en estos pasos dentro del alcance declarado.
Esto no constituye una certificación independiente. Los puntos para atacar
se fijan en prompt.md; no se envía esta comprobación al revisor para evitar
orientarlo hacia el juicio del autor.

Preparación del envío: sólo contrato histórico, nota de protocolos lentos y
nota de familia creciente, junto con el bloque delimitado de prompt.md.
REVISION_SOLO_ENTRADA=1 impide llamar a la API. La entrada exacta resultante
queda en entrada_deepseek.txt. No se adjuntan credenciales, memoria, historial
de conversación ni otros ficheros del checkout.
