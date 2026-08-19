# Borrador — cierre acotado de la **capa incondicional**

```text
ESTADO: BORRADOR NO FIRMADO / NO EJECUTADO
FECHA_BORRADOR: 2026-08-19
FECHA_FIRMA: PENDIENTE
REQUIERE_FIRMA_NUEVA_DEL_PI: PENDIENTE
ORIGEN: docs/foro/foro_decision_002_nc2fb-auditoria-adversarial.md (FORO_VERDICT=REVISE_AND_RECONVENE)
NATURALEZA: DEONTICO_NO_ALETICO
REAPERTURA: ACOTADA — cláusula en §5
NO_REVOCA: docs/program_closure_note_2026-07-30.md
NO_MODIFICA: PR #7, sello, ni tokens publicados de NC-2A..NC-2F
SEMILLAS: ninguna
```

## 1. Por qué esta nota existe

El foro adversarial `foro-002` emitió **BLOCK** contra la propuesta de «declarar
cerrada de forma definitiva toda la parte incondicional del programa». Sus cuatro
motivos eran independientes y cada uno bastaba:

1. el objeto a congelar **no existe** como conjunto definido: `grep -rl "parte
   incondicional"` devuelve cero ficheros en el repositorio;
2. la nota `NC-2F` §9 acota el refrendo a dos terminales y declara que «no amplía el
   perímetro de §3»;
3. nunca se fijó por escrito un criterio de cierre, luego no hay nada que satisfacer
   (`CLAUDE.md` §«Founding rules»);
4. la práctica registrada del repositorio son **once** notas de reapertura acotada
   posteriores al cierre del 2026-07-30.

Esta nota responde a (1) enumerando el objeto, a (2) siendo una nota nueva y no una
extensión de `NC-2F`, a (3) declarando su naturaleza —un acto **deóntico**, que no
requiere criterio alético— y a (4) incorporando la cláusula de reapertura que el
repositorio ya usa.

## 2. Naturaleza del acto

Igual que `docs/program_closure_note_2026-07-30.md`, este cierre es **deóntico, no
alético**: retira la autorización para seguir invirtiendo esfuerzo en la capa
enumerada en §3. **No** afirma que esa capa esté libre de errores, ni que sus
constantes sean óptimas, ni que no exista trabajo legítimo que hacer en ella.

En particular, **no** convierte la auditoría `foro-002` en un certificado de
corrección. Lo que `foro-002` estableció es más modesto y está escrito en su brief:
el Teorema 1.1 de `NC-2F(B)` sobrevivió a un recómputo independiente y a la lectura
línea a línea de sus lemas, con tres defectos corregidos y tres puntos registrados
como no resueltos (el recuento `m_k`, la certificación cruzada de la exactitud iid,
y el estatuto de las constantes deductivas frente a
`numbers-must-come-from-committed-script`).

## 3. Enumeración literal de la capa que se cierra

Se cierra exactamente lo siguiente, entendido como **los enunciados cuya
formulación no condiciona por el suceso de selección `S`**:

```text
emergencia/P1a_count_volume_rectangular_discrepancy_l2_d2.md
    §§1-7 completos: Teorema 1.1; Lemas 2.1, 3.1, 4.1, 5.1, 7.1;
    Corolarios 5.2 y 7.2; Proposición 6.1.
    NO se cierran sus §8 (Corolarios 8.1 y 8.2): son puentes a la capa selectiva.

emergencia/P1a_count_volume_selected_variance_clt_scale_d2.md
    Lema 6.1 (E[R^2] <= 65/n) y Lema 6.2 (cola de Delta_n), ambos incondicionales.
    NO se cierra nada más de ese documento.

emergencia/P1a_count_volume_selected_interior_mass_d2.md
    §3: Lema 3.1 (Azuma para una biyección uniforme) y la unión (3.2).
    NO se cierran sus §§4-6 (masa de seleccion, interioridad), que son selectivos.

emergencia/P1a_count_volume_lema_kl_d2.md
    §§2-5: ley Beta-producto dada la forma, caso especial de Wendel, y la cota
    puntual Var(ell | k,l) <= (n+1/4)/(n+1)^2.
    NO se cierra su §7 (descomposición P_1/P_2), que vive en el canal condicionado.

emergencia/P1a_count_volume_beta_uniform_scaling_d2.md
    NC-2A completo: la cota de b_n(m) es una propiedad de la ley Beta, sin selector.
```

**Queda explícitamente fuera** —es decir, sigue vivo y autorizado— todo lo que
condiciona por `S`: `NC-2B`; `NC-2C` §§4-6, incluida la cota de `Pr_n(S)`;
`NC-2D`; `NC-2E` §§2-5 y §§7-9; `NC-2F(a)` completo; y los Corolarios 8.1 y 8.2 de
`NC-2F(B)`. La obligación abierta que hereda el programa es la de `NC-2E`
Teorema 8.1, con **sus dos términos**:

\[
\sum_{\pi\in\mathcal S_n}\bigl(R(\pi)+\Delta_n(\pi)\bigr)^2
\ \le\ \frac Cn\,|\mathcal S_n| .
\]

## 4. Lo que el cierre significa en la práctica

- No se abren nuevas notas de alcance para mejorar constantes, umbrales ni
  exponentes de la capa de §3.
- Sus resultados pueden **citarse** libremente desde la capa selectiva, con su
  estatuto exacto: `E[\Delta_n^2]\le4.2\cdot10^4/n` es incondicional; `E[R^2]\le65/n`
  es incondicional; ninguno de los dos es una cota **relativa** sobre
  \(\mathcal S_n\), y confundir ambas cosas es el error que `foro-002` cazó.
- El esfuerzo del programa se dirige a la capa selectiva.

## 5. Cláusula de reapertura acotada

La capa de §3 se reabre, sin necesidad de deliberación previa, cuando concurran las
dos condiciones siguientes:

1. alguien exhibe un **error demostrado** —no una sospecha, no una mejora posible—
   con `path:line` y una comprobación reproducible que cualquiera pueda repetir; y
2. se firma una nota nueva que acote la reapertura a reparar ese error.

No son motivo de reapertura: mejorar una constante, bajar un umbral, acortar una
prueba, ni sustituirla por otra más elegante. Sí lo es un error que afecte a un
enunciado del que dependa la capa selectiva.

Los tres puntos que `foro-002` dejó **no resueltos** quedan registrados aquí como
deuda conocida, no como error: el recuento `m_k=(2^k+1)^2`; la certificación cruzada
de la exactitud iid bajo el condicionamiento a `N=n`; y el estatuto de las
constantes deductivas frente a `numbers-must-come-from-committed-script`. Si alguno
se convierte en error demostrado, la cláusula 1 aplica.

## 6. Prohibiciones

- no leer este cierre como certificado de corrección de la capa de §3;
- no afirmar que `NC2E-O3` queda cerrado ni que `liminf T_n^h>0`;
- no presentar el Corolario 8.1 de `NC-2F(B)` como cierre conseguido: su hipótesis
  `Pr_n(S)\ge c>0` está **abierta en ambos sentidos**;
- no contabilizar la obligación restante usando sólo `\Delta_n`;
- no modificar tokens publicados; el registro es append-only;
- no tocar el sello, las semillas ni la PR #7.

## 7. Firma pendiente

```text
FIRMADO_POR: Ignacio Martín (PI)
FECHA_FIRMA: PENDIENTE
DECISION: CIERRE_ACOTADO_DE_LA_CAPA_INCONDICIONAL
ALCANCE: la enumeración literal de §3, y nada más
CLAUSULA_DE_REAPERTURA: §5
LITERAL_SIGNOFF: PENDIENTE
```

Hasta esa firma, el estado permanece `BORRADOR NO FIRMADO / NO EJECUTADO` y la capa
de §3 sigue formalmente abierta.
