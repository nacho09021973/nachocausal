"""Exploration sandbox package marker — NOT on the sealed validation path.

The dev/ exploration SCRIPTS are committed as scoped exceptions so they sync
across machines (CLAUDE.md / README); only generated raw data + logs stay out of
git. This __init__ makes `dev` a package so GPU probes can run as
`python -m dev.<module>` via dev/run-gpu.sh (the WSL libcuda fix). Nothing here is
imported by the sealed `nachocausal/` package.
"""
