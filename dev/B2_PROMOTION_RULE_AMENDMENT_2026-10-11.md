# B2 — enmienda de la regla de promoción

**Fecha:** 2026-10-11
**Estado:** `DRAFT_AWAITING_PI_SIGNATURE` — no se calcula ninguna envolvente certificada de `S`
hasta que esté firmada.

## Regla vigente

```text
B2_CORRECTED_POSITIVE  iff  formal_upper_bound(drho_dt) < 0
```

(`research_program/puente_3p1/2026-09-12/verify_b2_formal_sign_certificate.py`, 2026-09-13.)

## Por qué se enmienda

La dirección `< 0` se fijó sobre la evaluación numérica de B2.2, que daba una banda negativa por
un error de signo en las caras inferiores (`dev/B2_2_SIGN_BUG_2026-10-11.md`). Corregido, B2.2 es
inconcluso, y la evidencia independiente (B1.5 certificado, B2.1 monótono) apunta a `rho' > 0`.
Mantener `< 0` sería una compuerta que, con toda probabilidad, no puede abrirse nunca: no protege
contra nada, solo garantiza que el trabajo no emita.

El objetivo científico de B2 es identificabilidad local a lo largo de la curva —`rho'(t0) != 0`—,
para el que el signo es irrelevante.

## Regla propuesta

```text
B2_CORRECTED_POSITIVE  iff  0 not in formal_enclosure(drho_dt)
```

con `drho_dt = S / Z^2`, `S = B' - 2 (Z'/Z) B`, en el `t0 = 0.5` congelado.

## Declaración obligatoria

Esta enmienda **se hace sabiendo** que el signo esperado es positivo. En la práctica, «excluir
cero» equivale aquí a `inf > 0`. Se declara para que nadie lo lea como una regla bilateral
elegida a ciegas. Su justificación no es el resultado esperado sino un error documentado en el
número sobre el que se fijó la regla anterior. No es un umbral nuevo (ATTACK_04): no se toca
ningún valor numérico, solo la dirección de una desigualdad fijada contra una cifra errónea.

## Lo que no cambia

- `no_new_path`, `no_new_t0`, `no_new_points`, `no_search`, `no_adjustment`.
- Excluir cero en `t0` **no** emite un terminal positivo de B2.1: eso sigue exigiendo control en
  un vecindario (punto en el que coincidieron las cuatro casas del sanedrín).
- Un intervalo que contenga cero a resolución finita detiene la tentativa por presupuesto, sin
  agotar la representación (precedente: B1.5 §6, `K=L=6` frente a `K=L=8`).

## Firma

```text
PI: ______________________    fecha: __________
```
