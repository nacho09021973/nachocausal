# Paper III — Resolución 003: clase de proceso puntual

```text
RESOLUTION_ID=PAPER_III_R003
STATUS=APPROVED
DATE=2026-09-10
SIGNED_BY=PI
RESOLVES=G0-6
SCOPE=DOCUMENTATION_ONLY
NUMBERS_MOVED=NONE
```

Firma el bloque `APPROVED TEXT — R3` de
[Resoluciones pendientes](paper_iii_resoluciones_pendientes.md), sin
modificarlo.

## 1. Texto aprobado, literal

> La pierna intervalar de Paper III es un **proceso binomial**: extrae un número
> fijo de puntos i.i.d. uniformes en el intervalo de Alexandrov, es decir un
> proceso de Poisson condicionado a \(N = n\). La pierna de caja es un proceso de
> Poisson homogéneo de intensidad \(\rho\). Ambas son homogéneas respecto a la
> medida de Lebesgue, que en coordenadas inerciales coincide con el volumen de
> Minkowski. La elección de \(N\) fijo en la pierna intervalar es deliberada y
> legítima — es el canal \(N=n\) descrito en `CLAUDE.md` — y debe declararse en
> todo texto que reporte sus cifras. Queda prohibido describir ambas piernas
> como «sprinklings de Poisson» sin esta distinción.

## 2. Aplicación

Sólo texto. Ninguna cifra, semilla, tamaño ni artefacto se ha movido.

| Fichero | Cambio |
|---|---|
| `dev/PAPER3_3P1_SCALE_NOTES.md` | declaración de proceso en §3.1 y §3.2, junto a las cifras que reporta cada pierna |
| `docs/hoja_de_ruta_paper_iii.md` | la pregunta de Paper III decía «en sprinklings de Poisson sobre intervalos de Alexandrov»; corregida a la clase real |

Anclaje en el código, sin tocarlo:

```text
pierna intervalar  dev/explore_3p1_bg_reference.py:32-41   extrae exactamente n_target puntos  -> BINOMIAL
pierna de caja     dev/explore_3p1_scale_calibration.py:59 rng.poisson(rho * BOX_VOLUME)       -> POISSON
```

## 3. Cierre

`G0-6` cierra por evidencia documental, comprobada en
`dev/verify_3p1_phase0_contract.py`: ambos ficheros deben declarar la clase
binomial de la pierna intervalar, y ninguno puede describir las dos piernas como
«sprinklings de Poisson» sin la distinción.

```text
G0-6 = CLOSED
```
