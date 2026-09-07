#!/bin/bash
# PIPELINE_PROVENANCE=RECONSTRUCTED_BY_GOLDEN_REPLAY
set -u
cd /tmp/nachocausal_v4_replay
mkdir -p build
python3 pipeline/md2tex.py golden_v4_es.md replay_v4_es.tex || exit 1
cp replay_v4_es.tex build/
for pass in 1 2 3; do
  (cd build && lualatex -interaction=nonstopmode -halt-on-error \
      -file-line-error replay_v4_es.tex >/dev/null 2>&1)
done
(cd build && lualatex -interaction=nonstopmode -file-line-error replay_v4_es.tex > lastrun.log 2>&1)
if [ -f build/replay_v4_es.pdf ]; then cp build/replay_v4_es.pdf replay_v4_es.pdf; echo "BUILT"; else echo "FAILED"; fi
