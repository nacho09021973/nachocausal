# NVIDIA consulting adapter

## Objetivo

Este repo puede preparar expedientes para consultar un wrapper externo apoyado
en modelos servidos por NVIDIA Build / NIM, sin copiar modelos ni claves dentro
de `nachocausal`.

Ubicacion externa esperada:

```text
~/ai/nvidia-consult/
```

La ruta puede cambiarse con `NVIDIA_CONSULT_HOME` o `--nvidia-home`.

## Regla de este repo

En `nachocausal`, las consultas externas son **reversibles** y sus artefactos se
guardan por defecto en:

```text
dev/consultations/nvidia/
```

No cuentan como resultado sellado ni como evidencia del path de validacion.

## Principios

- El wrapper NVIDIA vive fuera del repo.
- `nachocausal` solo guarda expedientes, manifests y respuestas advisory-only.
- El adaptador de `nachocausal` no contiene `NVIDIA_API_KEY`.
- No toca el path sellado ni la validacion.

## Comando

```bash
export NVIDIA_CONSULT_HOME="$HOME/ai/nvidia-consult"
export NVIDIA_CONSULT_CMD="$HOME/ai/nvidia-consult/bin/nvidia-consult"
python scripts/consulting/nvidia_consult.py --check-only
```
