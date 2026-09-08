#!/usr/bin/env bash
# PIPELINE_PROVENANCE=RECONSTRUCTED_BY_GOLDEN_REPLAY
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: $0 manuscrito/manuscrito_v4_{en,es}.md" >&2
  exit 2
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/../.." && pwd)"
src="$1"

case "$src" in
  /*) md_path="$src" ;;
  *) md_path="$repo_root/$src" ;;
esac

if [ ! -f "$md_path" ]; then
  echo "missing markdown: $src" >&2
  exit 2
fi

base="$(basename "$md_path" .md)"
out_dir="$script_dir/out/$base"
tex_path="$out_dir/$base.tex"
pdf_path="${md_path%.md}.pdf"
tex_cache="$script_dir/out/texmf-cache"

mkdir -p "$out_dir" "$tex_cache"
python3 "$script_dir/md2tex.py" "$md_path" "$tex_path"

export TEXMFVAR="$tex_cache"
export TEXMFCACHE="$tex_cache"

for pass in 1 2 3; do
  (cd "$out_dir" && lualatex -interaction=nonstopmode -halt-on-error -file-line-error "$base.tex" >/dev/null 2>&1)
done

(cd "$out_dir" && lualatex -interaction=nonstopmode -file-line-error "$base.tex" > lastrun.log 2>&1)

if [ ! -f "$out_dir/$base.pdf" ]; then
  echo "FAILED" >&2
  exit 1
fi

cp "$out_dir/$base.pdf" "$pdf_path"
echo "BUILT $pdf_path"
