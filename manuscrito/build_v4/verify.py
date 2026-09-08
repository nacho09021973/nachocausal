#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PIPELINE_PROVENANCE=RECONSTRUCTED_BY_GOLDEN_REPLAY
Objective final checks for the reconstructed V4 build output."""
import io
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

from pdfgeom import pages

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]

TARGETS = {
    "en": REPO_ROOT / "manuscrito" / "manuscrito_v4_en",
    "es": REPO_ROOT / "manuscrito" / "manuscrito_v4_es",
}

REQUIRED_TEXT = {
    "en": {
        "marginal_definitions": ["marginal means", "marginal-mean operators", "Mu", "Mv"],
        "g_full_definition": ["Gfull", "4N"],
        "anchors": [
            "Visible Directions in Finite Causal Orders",
            "Jose Ignacio Martin Gandul",
            "jmartin596@alumno.uned.es",
            "Theorem 1",
            "Corollary 2",
            "Corollary 3",
            "Theorem 4",
            "witness",
            "antichain) 0 = 85",
            "chain) 0 = - 85",
            "For Karim",
            "What is forgotten is not always gone",
            "References",
        ],
    },
    "es": {
        "marginal_definitions": ["medias marginales", "operadores de media marginal", "Mu", "Mv"],
        "g_full_definition": ["Gfull", "4N"],
        "anchors": [
            "Direcciones visibles en ordenes causales finitos",
            "Jose Ignacio Martin Gandul",
            "jmartin596@alumno.uned.es",
            "Teorema 1",
            "Corolario 2",
            "Corolario 3",
            "Teorema 4",
            "testigo",
            "antichain) 0 = 85",
            "chain) 0 = - 85",
            "For Karim",
            "What is forgotten is not always gone",
            "Referencias",
        ],
    },
}


def run(args):
    return subprocess.run(args, capture_output=True, text=True, check=False)


def normalize(s):
    s = s.replace("−", "-")
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")


def pdf_text(pdf):
    return normalize(run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"]).stdout)


def source_counts(md):
    src = io.open(md, encoding="utf-8").read()
    return (
        len(re.findall(r"\\tag\{[^}]*\}", src)),
        len(re.findall(r"^- \*\*\[[^\]]+\]\*\*", src, re.M)),
    )


def log_counts(log):
    s = log.read_text(encoding="utf-8", errors="replace") if log.exists() else ""
    return {
        "overfull": len(re.findall(r"Overfull \\\\hbox", s)),
        "undefined_refs": len(re.findall(r"LaTeX Warning: Reference .* undefined|There were undefined references", s)),
        "undefined_citations": len(re.findall(r"Citation .* undefined|There were undefined citations", s)),
        "missing_glyphs": len(re.findall(r"Missing character:", s)),
    }


def glyphs_outside(pdf):
    bad = 0
    for w, h, words in pages(pdf):
        for x0, y0, x1, y1, _ in words:
            if x0 < -0.01 or y0 < -0.01 or x1 > w + 0.01 or y1 > h + 0.01:
                bad += 1
    return bad


def page_size_and_count(pdf):
    pg = list(pages(pdf))
    ok = all(abs(w - 612.0) < 0.01 and abs(h - 792.0) < 0.01 for w, h, _ in pg)
    return len(pg), ok


def contains_all(haystack, needles):
    flat = haystack.replace("\n", " ")
    return all(n in flat for n in needles)


def main():
    status = 0
    for lang, stem in TARGETS.items():
        md = stem.with_suffix(".md")
        pdf = stem.with_suffix(".pdf")
        log = SCRIPT_DIR / "out" / stem.name / "lastrun.log"
        txt = pdf_text(pdf) if pdf.exists() else ""
        pages_n, page_size_ok = page_size_and_count(pdf) if pdf.exists() else (0, False)
        eq_tags, bib_entries = source_counts(md)
        lc = log_counts(log)
        outside = glyphs_outside(pdf) if pdf.exists() else -1
        marginal = contains_all(txt, REQUIRED_TEXT[lang]["marginal_definitions"])
        gfull = contains_all(txt, REQUIRED_TEXT[lang]["g_full_definition"])
        anchors = contains_all(txt, REQUIRED_TEXT[lang]["anchors"])
        built = pdf.exists() and pdf.stat().st_size > 0
        passed = (
            built
            and page_size_ok
            and eq_tags == 70
            and bib_entries == 20
            and lc["overfull"] == 0
            and lc["undefined_refs"] == 0
            and lc["undefined_citations"] == 0
            and lc["missing_glyphs"] == 0
            and outside == 0
            and marginal
            and gfull
            and anchors
        )
        if not passed:
            status = 1
        up = lang.upper()
        print(f"{up}_PDF={'PASS' if passed else 'FAIL'}")
        print(f"{up}_PAGES={pages_n}")
        print(f"PAGE_SIZE_{up}={'PASS' if page_size_ok else 'FAIL'}")
        print(f"EQUATION_TAGS_{up}={eq_tags}")
        print(f"BIBLIOGRAPHY_ENTRIES_{up}={bib_entries}")
        print(f"OVERFULL_{up}={lc['overfull']}")
        print(f"UNDEFINED_REFS_{up}={lc['undefined_refs']}")
        print(f"UNDEFINED_CITATIONS_{up}={lc['undefined_citations']}")
        print(f"MISSING_GLYPHS_{up}={lc['missing_glyphs']}")
        print(f"GLYPHS_OUTSIDE_PAGE_{up}={outside}")
        print(f"MARGINAL_DEFINITIONS_{up}={'PASS' if marginal else 'FAIL'}")
        print(f"G_FULL_DEFINITION_{up}={'PASS' if gfull else 'FAIL'}")
        print(f"ANCHORS_{up}={'PASS' if anchors else 'FAIL'}")
    return status


if __name__ == "__main__":
    sys.exit(main())
