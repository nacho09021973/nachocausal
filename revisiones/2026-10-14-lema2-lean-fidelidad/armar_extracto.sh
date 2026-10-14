#!/usr/bin/env bash
# Arma extracto_certificado_B2.md: los pasajes del certificado de B2 que el lema 2 en Lean
# pretende formalizar (§2 pasos 1-2, la fila de `p` de §3 y la hipótesis H1 de §6).
# Fija la versión del certificado por su SHA-256 y aborta si ha cambiado.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
F=research_program/puente_3p1/2026-10-11/B2_path2_gate_certificate.md
ESPERADO=04b48eba1ba21f7e64da27060edbb00212da6ba296782c72b268a27b43c6af7e
REAL=$(sha256sum "$F" | cut -d' ' -f1)
[ "$REAL" = "$ESPERADO" ] || { echo "el certificado cambió: $REAL" >&2; exit 1; }
OUT=revisiones/2026-10-14-lema2-lean-fidelidad/extracto_certificado_B2.md
{
  echo "# Extracto del certificado de la compuerta de B2"
  echo
  echo "Pasajes literales, sin editar, de \`B2_path2_gate_certificate.md\` (líneas indicadas)."
  echo
  echo "## Líneas 50-61 (§2, pasos 1 y 2)"
  echo
  sed -n 50,61p "$F"
  echo
  echo "## Líneas 106-107 y 110 (§3, cabecera de la tabla y fila de \`p\`)"
  echo
  sed -n 106,107p "$F"
  sed -n 110p "$F"
  echo
  echo "## Líneas 162-183 (§6, hipótesis H1)"
  echo
  sed -n 162,183p "$F"
} > "$OUT"
echo "certificado sha256 $REAL"
