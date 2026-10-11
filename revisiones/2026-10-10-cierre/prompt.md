# Encargo: revisión ciega de una nota de cierre

---

Revisas `S4W_NOTA_DE_CIERRE_2026-10-10.md`. Es el documento que va a quedar como **registro
final** de una línea de investigación que se cierra, así que lo que importa no es si es
brillante sino si es **fiel**: si lo que declara establecido lo está, si lo que declara no
establecido no lo está, y si no se cuela ninguna afirmación por encima de su soporte.

Van adjuntos el candidato auditado (ya enmendado), la auditoría, R6′, el no-go retirado, el
resultado del coeficiente, y las fuentes primarias: Wang (arXiv:1904.01034),
Belenchia–Benincasa–Dowker (1510.04656), Belenchia (1510.04665), Dowker–Glaser (1305.2588) y la
tesis de Pfeiffer 2022. **Esta vez están todas**, de modo que cada cita es comprobable en el
original.

## Objetivo

Cuatro comprobaciones, y la tercera es la que más pesa.

**N1 — ¿está bien lo que declara ESTABLECIDO?** El coeficiente local
`-73 sqrt6/(1575 pi)` por `C_abcd C^abcd` a orden algebraico `R^2` en el canal `rho^{-1/2}`, con
la pieza dependiente del observador exactamente cero **en ese canal**. ¿Está el alcance bien
acotado, o se desliza hacia un enunciado más fuerte?

**N2 — ¿está bien lo que declara NO ESTABLECIDO?** Que no hay enunciado global porque falta el
control del resto; que `W2` vive en `O(rho^{-1/2})`; que `F1` y `C0` siguen abiertos.

**N3 — la distinción BBD válido / Pfeiffer inválido.** La nota sostiene que la cota de BBD ec.
(25) es legítima porque acota **primero** el integrando —obteniendo el kernel de coeficientes
positivos— y sólo después lo escribe como identidad con el operador de signos invertidos
`(1 - 9H_1 + 8H_2 - (4/3)H_3)`, que no es su `Ô` de la ec. (15); y que su `O(rho^{-2})` sale del
orden del desarrollo en `u`, no de raíces. Y que Pfeiffer (3.15)–(3.22), en cambio, aplica el
operador **con sus raíces** a una cantidad ya acotada por normas supremas, lo que no vale.
**Compruébalo en los dos originales adjuntos.** Es la afirmación más fuerte de la nota —imputa
un paso inválido a un trabajo ajeno— y la que más conviene que no sea un malentendido de
lectura.

**N4 — la prioridad.** Que `Ô_*` es el `O_6` de la ec. (13) de Dowker–Glaser con
`H_DG = 4 rho ∂_rho`, que eso reproduce `(1,-14,41,-44,16)`, y que no hay antecedente exacto del
coeficiente.

## Qué más atacar

- ¿Hay en la nota alguna afirmación sin respaldo en lo adjunto, o alguna cita que no diga lo
  que se le atribuye?
- ¿El §6 («qué reabriría esto») describe bien el hueco, o lo pinta más pequeño o más grande de
  lo que es?
- ¿El §7, la tabla de errores, omite alguno relevante o se atribuye hallazgos ajenos?
- ¿Está bien cerrada la frontera de claims del §5, o queda algún resquicio?

## Resultado esperado

Prosa seca, sin preámbulo, y al final:

```
N1_ESTABLECIDO     = FIEL | SOBREAFIRMA | SUBAFIRMA | NO_CONCLUYENTE  + por qué
N2_NO_ESTABLECIDO  = FIEL | SOBREAFIRMA | SUBAFIRMA | NO_CONCLUYENTE  + por qué
N3_BBD_VS_PFEIFFER = CORRECTA | INCORRECTA | NO_CONCLUYENTE           + por qué
N4_PRIORIDAD       = CORRECTA | INCORRECTA | NO_CONCLUYENTE           + por qué
VEREDICTO_CIERRE = APTA_COMO_REGISTRO | APTA_CON_CORRECCIONES | NO_APTA
DEFECTOS_ENCONTRADOS = lista, o NINGUNO
```

## Condiciones

- **Una sola ronda.** Sesión sellada: sin herramientas, ficheros ni web. No cites nada que no
  esté adjunto.
- No reescribas la nota. Juzga si es fiel.

---
