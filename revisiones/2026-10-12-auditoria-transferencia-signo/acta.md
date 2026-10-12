# Acta — auditoría de la transferencia del signo de B2 al punto medio real

**Fecha:** 2026-10-12. **Convoca:** el PI. **Casas:** CIRO y ABNER. El PI ha pedido una
auditoría ligera a dos casas, no el sanedrín completo.

Se os pide **auditar**, no proponer trabajo nuevo. El objeto está congelado y subido **antes**
de esta auditoría (`7bcc087`). Vuestro trabajo es intentar **romperlo**: buscad una
desigualdad falsa, un caso que no esté cubierto o una constante que no acote lo que dice
acotar. Un acuerdo fácil no tiene valor.

No tenéis herramientas. Solo cuentan esta acta y los adjuntos:

1. `B2_sign_transfer.md` — la nota: qué cierra, la cota, el diagnóstico de radio y las
   hipótesis.
2. `verify_b2_sign_transfer.py` — el verificador completo (`mpmath.iv`).
3. `verification_b2_sign_transfer.json` — su salida.
4. `B2_path2_gate_certificate.md` — la nota de la compuerta, ya auditada y promocionada. Da el
   contexto: H1–H5, la parametrización de ASTRA en H3 y las cotas que se heredan.

## 1. Qué se afirma

La compuerta certificó `S(lambda*; d) >= S_lo = +0.0013679` en el binary64
`lambda* = path(0.5)`, a lo largo de la `d` exacta de los binary64. La nota afirma que, para
todo punto `m` a distancia sup `<= 1e-16` de `lambda*` y toda dirección `d'` a distancia sup
`<= 1e-16` de `d`:

```text
S(m; d') >= S_lo − DS_point − DS_dir >= +0.0013679131 > 0
```

Ese conjunto contiene el punto medio decimal y el punto medio exacto de los extremos binary64.

## 2. Lo que no se reabre

La auditoría de la compuerta (sanedrín 2026-10-11, pase condicional con la condición
verificada) cubre la cadena N1–N4, H3 como teorema, H4 como hipótesis de entorno y la capa
escalar de B1.5 (`s_encl`, `q_encl`, `G_encl`, `E_INV_HI`). Aquí solo se audita la cota
de continuidad nueva.

## 3. Lo que se os pide

Para cada punto, decid si se sostiene y, si no, cuál es la condición mínima para concederlo.

1. **El módulo `ω_h`.** La cota de `|h(x,y) − h(x',y)|` en los casos degenerados (un par
   comparable y el otro no, `A` o `B` nulos) y en las dos orientaciones. La desigualdad
   `|√s − √t| <= √|s−t|`. Que `w_f` no salga del rango donde valen `L_q` y `q_max`. Que usar
   **la misma** clase de `f` para los dos pares sea legítimo.
2. **`ΔI_f`.** Que `H_K <= Z` y que el término `|KΔK'|` cubra el cambio de `K` dentro de `H`.
   Que los extremos de cada cara estén bien contados.
3. **`q'` y `G'`.** Las fórmulas vía `ds/dw = −1/(s e^s)` y la monotonía en `s` de cada factor
   que se usa para acotarlas.
4. **`Δk` y el término de dirección.** La linealidad de `S` en la dirección. Que el término de
   dirección use `B/Z`, y no `k`, como coeficiente de `J_f`.
5. **El código frente a la nota.** Que cada fórmula del script sea la de la nota, que el
   redondeo vaya hacia afuera (`mpmath.iv`, `.a`/`.b`) y que no se use ningún valor en `m` como
   si fuera conocido.

**El diagnóstico de radio** (§3 de la nota) no entra en el terminal, pero afirma un radio de
`1e-7` en `γ`. Atacadlo también si veis un fallo.

**Veredictos posibles:** `AUDIT_PASS`, `AUDIT_PASS_CONDITIONAL_<COND>`,
`AUDIT_REQUIRES_MINOR_FIX`, `AUDIT_FAIL`.
