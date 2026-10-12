---
name: display-bounds-round-outward
description: "Al mostrar una cota certificada con menos cifras, redondear HACIA AFUERA (inferior hacia abajo, superior hacia arriba); nunca al más cercano"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 9bbca683-ada3-4de3-a0b2-353599e0546a
  modified: 2026-10-12T09:27:36.384Z
---

Toda cota certificada que se muestre abreviada en una nota, una tabla, un commit, un acta o un
chat se redondea **hacia afuera**: una cota inferior hacia abajo (truncar) y una superior hacia
arriba. El redondeo al más cercano publica una desigualdad más fuerte que la certificada.

**Why:** el 2026-10-12 ASTRA cazó `drho/dt >= 0.0066481` cuando lo certificado era
`0.006648095…`. Al buscar casos parecidos aparecieron más: `+0.00705` para la compuerta
(certificado `0.0070474…`), `S_lo +0.0012175` (certificado `0.00121747…`), cuatro valores de la
tabla diagnóstica de la transferencia, y una cota **superior** mostrada hacia abajo
(`2.5435e-08` frente a `2.54351…e-08`). Algunos quedaron en mensajes de commit, que no se pueden
corregir.

**How to apply:** formatear desde el script con `Decimal.quantize(..., ROUND_FLOOR)` para las
inferiores y `ROUND_CEILING` para las superiores, nunca con `%.7f`. Antes de commitear, buscar
con grep cada cifra abreviada y compararla con el JSON. Lo mismo vale al resumir en el chat.
Relacionado: [[numbers-must-come-from-committed-script]], [[puente-3p1-b2-gate]].
