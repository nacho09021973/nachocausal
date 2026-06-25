#!/usr/bin/env bash
# Launch a dev/ exploration module in the GPU venv with the WSL CUDA driver dir
# FIRST on the library path. On this WSL2 box a stale native libcuda.so.535 in
# /lib/x86_64-linux-gnu shadows the WSL stub (driver 610) that matches the
# Windows driver -> cudaErrorNoDevice. Prepending /usr/lib/wsl/lib fixes it and
# is harmless on non-WSL / CPU-only machines (the dir just won't exist there).
#
# Default module is dev.explore_past_matrix; override with NACHO_MODULE, e.g.
#   NACHO_MODULE=dev.sweep_ensemble dev/run-gpu.sh --device auto --seeds dev
# A convenience wrapper dev/run-sweep.sh sets NACHO_MODULE for the sweep.
set -euo pipefail
cd "$(dirname "$0")/.."
[ -d /usr/lib/wsl/lib ] && export LD_LIBRARY_PATH="/usr/lib/wsl/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"
exec .venv-gpu/bin/python -m "${NACHO_MODULE:-dev.explore_past_matrix}" "$@"
