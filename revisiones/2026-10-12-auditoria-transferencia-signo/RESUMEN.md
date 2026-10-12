# Auditoría ligera 2026-10-12 — transferencia del signo de B2 al punto medio real

**Objeto auditado:** `research_program/puente_3p1/2026-10-12/` en `7bcc087`. **Formato:** el PI
pidió dos casas en lugar del sanedrín completo, para ahorrar recursos. Las dos auditan **por
separado y a ciegas**, sin ver el turno de la otra, con el mismo `acta.md` y los mismos cuatro
adjuntos.

| casa | vía | veredicto | hallazgos |
|---|---|---|---|
| CIRO (`grok-4.6`) | CLI directo con las banderas selladas de sanedrín (`ciro_directo.md`, `grok_prompt.md`) | `AUDIT_PASS` | 1 MENOR documental |
| ABNER (DeepSeek) | interfaz web, consulta del PI (`abner_web.md`, `abner_prompt_web.md`) | `AUDIT_PASS` | ninguno |

**Lo que se sostiene, según las dos casas:**
- `ω_h`: los casos degenerados, las dos orientaciones, el rango de `w_f` y la misma clase de `f`;
- `ΔI_f`: `H_K <= Z`, `|KΔK'|` y los extremos;
- las fórmulas de `q'` y `G'`, con la monotonía en `s`;
- `Δk` y el término de dirección, con `B/Z` y no `k`;
- el código frente a la nota;
- el radio diagnóstico `1e-7`, que no alcanza B2.1.

CIRO añade dos holguras que no son agujeros: el `½` de `p` no se aprovecha, y `L_G` sale un 10 %
holgada.

**MENOR de CIRO, corregido** después de la auditoría, solo en el texto. La nota mostraba
`q_max` y `L_G` redondeadas **hacia abajo**, siendo cotas superiores. Ahora se muestran
redondeadas hacia arriba a 8 cifras. El cálculo usa los valores exactos del JSON, que no cambia.
La nota también dice ahora que su tabla diagnóstica muestra 6 de los 8 radios.

**Incidencias:**
- La sesión de sanedrín con `-m ciro,abner` perdió los dos turnos de ronda 1 por timeout
  (900 s × 2 por casa). El PI la abortó a las 08:34 UTC (`sanedrin.log`, `sanedrin.log.log`).
- Sanedrín exige al menos dos miembros, así que CIRO se llamó directamente con su mismo
  sellado y un timeout de 1800 s.

**Límites de esta auditoría frente a la de la compuerta:**
- son dos casas, no cinco, y no hubo rondas cruzadas ni veredicto arbitral;
- ninguna casa ejecutó el script; los números proceden de la ejecución del 2026-10-12;
- la respuesta de ABNER llegó por la web: no queda registrado el modelo exacto, y el sellado
  solo se pidió por instrucción, sin poder comprobarlo;
- la respuesta de ABNER confirma punto por punto, pero no aporta ningún ataque que no
  estuviera ya en el acta.
