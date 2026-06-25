#!/usr/bin/env bash
# Convenience wrapper: run the full-ensemble exploration sweep on the GPU venv.
#   dev/run-sweep.sh --device auto --seeds dev
#   dev/run-sweep.sh --device auto --seeds validation
exec env NACHO_MODULE=dev.sweep_ensemble "$(dirname "$0")/run-gpu.sh" "$@"
