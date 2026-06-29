# DeepMath consulting adapter

## Objetivo

Este repo puede preparar expedientes para consultar un DeepMath externo sin
instalar el modelo ni copiarlo dentro de `nachocausal`.

Ubicacion externa esperada:

```text
~/ai/deepmath/
```

La ruta puede cambiarse con `DEEPMATH_HOME` o `--deepmath-home`.

## Regla de este repo

En `nachocausal`, las consultas externas son **reversibles** y sus artefactos se
guardan por defecto en:

```text
dev/consultations/deepmath/
```

No cuentan como resultado sellado ni como evidencia del path de validacion.

## Principios

- DeepMath vive fuera del repo.
- `nachocausal` solo guarda expedientes, manifests y respuestas advisory-only.
- El adaptador no asume ningun CLI real de DeepMath.
- Si no hay comando configurado, falla cerrado con un error claro.
- No toca el path sellado ni la validacion.

## Comando

```bash
export DEEPMATH_CMD="$HOME/ai/deepmath/bin/deepmath-consult"
python scripts/consulting/deepmath_consult.py --check-only
```
