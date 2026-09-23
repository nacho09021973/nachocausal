#!/usr/bin/env python3
"""Build a local vector index over biblioteca/*.pdf derived markdown.

Source of truth: the PDFs in biblioteca/ are canonical (see
biblioteca/derived-md-marker/FULL_LIBRARY_CONVERSION_REPORT.md and
nachocausal/CLAUDE.md). This script only indexes markdown that has already
been derived from them -- it does not re-run PDF extraction.

For each PDF it prefers biblioteca/derived-md-marker/<name>.md (higher math
and reading-order fidelity per biblioteca/derived-md-marker/MARKER_BENCHMARK_REPORT.md)
and falls back to biblioteca/derived-md/<name>.md (PyMuPDF4LLM baseline).
PDFs with neither are reported as uncovered, not silently skipped.

Chunks are grouped by <!-- PDF_PAGE: N --> markers so every chunk carries an
exact page citation back to the canonical PDF.

Requires a local Ollama server (http://localhost:11434) with the `bge-m3`
embedding model pulled (`ollama pull bge-m3`).

Output: biblioteca/rag_index/index.npz (vectors) + chunks.jsonl (metadata +
text). biblioteca/ is already git-ignored in this repo, so the index is not
committed, matching how biblioteca/derived-md* are already handled.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import numpy as np
import requests

BIBLIOTECA = Path(__file__).resolve().parents[2] / "biblioteca"
MARKER_DIR = BIBLIOTECA / "derived-md-marker"
BASE_DIR = BIBLIOTECA / "derived-md"
INDEX_DIR = BIBLIOTECA / "rag_index"

OLLAMA_URL = "http://localhost:11434"
EMBED_MODEL = "bge-m3"

PAGE_MARKER_RE = re.compile(r"<!--\s*PDF_PAGE:\s*(\d+)\s*-->")

CHUNK_TARGET_CHARS = 1200
CHUNK_MIN_CHARS = 200
# Ollama's default embedding batch size is 2048 tokens; scientific text with
# LaTeX-like symbols runs denser than ~4 chars/token, so keep a hard, well
# under that ceiling and split any oversized page block instead of just
# capping between pages.
CHUNK_HARD_MAX_CHARS = 2400


def find_markdown_source(pdf_stem: str) -> tuple[Path, str] | None:
    marker_path = MARKER_DIR / f"{pdf_stem}.md"
    if marker_path.exists():
        return marker_path, "marker"
    base_path = BASE_DIR / f"{pdf_stem}.md"
    if base_path.exists():
        return base_path, "pymupdf4llm"
    return None


def split_into_page_blocks(text: str) -> list[tuple[int | None, str]]:
    """Split markdown on PDF_PAGE markers. Returns [(page, block_text), ...]."""
    parts = PAGE_MARKER_RE.split(text)
    if len(parts) == 1:
        return [(None, text)]
    blocks: list[tuple[int | None, str]] = []
    if parts[0].strip():
        blocks.append((None, parts[0]))
    for i in range(1, len(parts), 2):
        page = int(parts[i])
        body = parts[i + 1] if i + 1 < len(parts) else ""
        blocks.append((page, body))
    return blocks


def chunk_pages(pages: list[tuple[int | None, str]]) -> list[dict]:
    """Merge consecutive page blocks into ~CHUNK_TARGET_CHARS chunks."""
    chunks: list[dict] = []
    buf_text: list[str] = []
    buf_pages: list[int] = []
    buf_len = 0

    def flush():
        nonlocal buf_text, buf_pages, buf_len
        if not buf_text:
            return
        text = "\n\n".join(buf_text).strip()
        if text:
            chunks.append({
                "text": text,
                "page_start": buf_pages[0] if buf_pages else None,
                "page_end": buf_pages[-1] if buf_pages else None,
            })
        buf_text, buf_pages, buf_len = [], [], 0

    def add_piece(page: int | None, piece: str):
        nonlocal buf_len
        if buf_len >= CHUNK_TARGET_CHARS:
            flush()
        buf_text.append(piece)
        if page is not None and page not in buf_pages:
            buf_pages.append(page)
        buf_len += len(piece)
        if buf_len >= CHUNK_HARD_MAX_CHARS:
            flush()

    for page, body in pages:
        body = body.strip()
        if not body:
            continue
        if len(body) <= CHUNK_HARD_MAX_CHARS:
            add_piece(page, body)
            continue
        # oversized single page: split on paragraph breaks, hard-cap fallback
        start = 0
        paras = body.split("\n\n")
        piece = ""
        for para in paras:
            if len(piece) + len(para) + 2 > CHUNK_HARD_MAX_CHARS and piece:
                add_piece(page, piece)
                piece = para
            else:
                piece = f"{piece}\n\n{para}" if piece else para
            while len(piece) > CHUNK_HARD_MAX_CHARS:
                add_piece(page, piece[:CHUNK_HARD_MAX_CHARS])
                piece = piece[CHUNK_HARD_MAX_CHARS:]
        if piece:
            add_piece(page, piece)
    flush()

    # merge trailing tiny chunk into the previous one
    if len(chunks) >= 2 and len(chunks[-1]["text"]) < CHUNK_MIN_CHARS:
        last = chunks.pop()
        prev = chunks[-1]
        prev["text"] = prev["text"] + "\n\n" + last["text"]
        prev["page_end"] = last["page_end"]

    return chunks


def embed_one(text: str) -> list[float]:
    r = requests.post(
        f"{OLLAMA_URL}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": text},
        timeout=120,
    )
    if r.status_code == 500 and len(text) > 400:
        # defensive fallback: still too many tokens for the server's batch
        # size (e.g. dense LaTeX/table text) -- split and average.
        mid = len(text) // 2
        a = embed_one(text[:mid])
        b = embed_one(text[mid:])
        return list((np.array(a) + np.array(b)) / 2)
    r.raise_for_status()
    return r.json()["embedding"]


def embed(texts: list[str]) -> np.ndarray:
    return np.array([embed_one(t) for t in texts], dtype=np.float32)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=None,
                     help="index only the first N PDFs (debugging)")
    args = ap.parse_args()

    try:
        requests.get(f"{OLLAMA_URL}/api/version", timeout=5).raise_for_status()
    except requests.RequestException as e:
        print(f"ERROR: cannot reach Ollama at {OLLAMA_URL} ({e}). "
              f"Start it with `ollama serve`.", file=sys.stderr)
        return 1

    pdf_stems = sorted(p.stem for p in BIBLIOTECA.glob("*.pdf"))
    if args.limit:
        pdf_stems = pdf_stems[: args.limit]

    covered: list[tuple[str, Path, str]] = []
    uncovered: list[str] = []
    for stem in pdf_stems:
        found = find_markdown_source(stem)
        if found is None:
            uncovered.append(stem)
        else:
            path, source = found
            covered.append((stem, path, source))

    print(f"PDFs in biblioteca/: {len(pdf_stems)}")
    print(f"With derived markdown: {len(covered)}")
    print(f"WITHOUT derived markdown (not indexed): {len(uncovered)}")

    all_chunks: list[dict] = []
    for stem, path, source in covered:
        text = path.read_text(encoding="utf-8", errors="replace")
        pages = split_into_page_blocks(text)
        for c in chunk_pages(pages):
            c["pdf_stem"] = stem
            c["md_source"] = source
            c["md_path"] = str(path.relative_to(BIBLIOTECA))
            all_chunks.append(c)

    print(f"Chunks to embed: {len(all_chunks)}")
    if not all_chunks:
        print("Nothing to index.", file=sys.stderr)
        return 1

    BATCH = 16
    vectors = []
    for i in range(0, len(all_chunks), BATCH):
        batch = all_chunks[i:i + BATCH]
        vectors.append(embed([c["text"] for c in batch]))
        done = min(i + BATCH, len(all_chunks))
        print(f"  embedded {done}/{len(all_chunks)}", end="\r", file=sys.stderr)
    print(file=sys.stderr)
    matrix = np.concatenate(vectors, axis=0)

    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(INDEX_DIR / "index.npz", vectors=matrix, model=EMBED_MODEL)
    with (INDEX_DIR / "chunks.jsonl").open("w", encoding="utf-8") as f:
        for c in all_chunks:
            f.write(json.dumps({
                "pdf_stem": c["pdf_stem"],
                "md_source": c["md_source"],
                "md_path": c["md_path"],
                "page_start": c["page_start"],
                "page_end": c["page_end"],
                "text": c["text"],
            }, ensure_ascii=False) + "\n")
    with (INDEX_DIR / "uncovered_pdfs.txt").open("w", encoding="utf-8") as f:
        f.write("\n".join(sorted(uncovered)) + "\n")

    print(f"Index written to {INDEX_DIR} "
          f"({matrix.shape[0]} vectors, dim {matrix.shape[1]}).")
    print(f"{len(uncovered)} PDFs have no derived markdown and are NOT in the "
          f"index -- see {INDEX_DIR / 'uncovered_pdfs.txt'}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
