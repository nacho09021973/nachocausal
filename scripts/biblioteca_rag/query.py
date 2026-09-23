#!/usr/bin/env python3
"""Query the local biblioteca/ RAG index built by build_index.py.

Retrieval-only by default: prints the top-k matching chunks with their
source PDF and page range, so you can jump straight to the canonical PDF.
Pass --answer to additionally ask a local Ollama chat model to synthesize
an answer grounded in those chunks (slower; still local, no API cost).

The derived markdown is non-authoritative for formulas and order/precedence
symbols (see biblioteca/derived-md-marker/MARKER_BENCHMARK_REPORT.md) --
any claim about a specific equation or causal-order relation must be
checked against the cited PDF page before it is used for anything.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import requests

BIBLIOTECA = Path(__file__).resolve().parents[2] / "biblioteca"
INDEX_DIR = BIBLIOTECA / "rag_index"

OLLAMA_URL = "http://localhost:11434"
EMBED_MODEL = "bge-m3"
DEFAULT_ANSWER_MODEL = "qwen2.5:7b-instruct"

DISCLAIMER = (
    "Fuente derivada, no autoritativa para formulas/orden causal: "
    "comprueba en el PDF citado antes de usarlo."
)


def embed_query(text: str) -> np.ndarray:
    r = requests.post(
        f"{OLLAMA_URL}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": text},
        timeout=60,
    )
    r.raise_for_status()
    return np.array(r.json()["embedding"], dtype=np.float32)


def load_index():
    data = np.load(INDEX_DIR / "index.npz")
    vectors = data["vectors"]
    chunks = []
    with (INDEX_DIR / "chunks.jsonl").open(encoding="utf-8") as f:
        for line in f:
            chunks.append(json.loads(line))
    if len(chunks) != vectors.shape[0]:
        print("WARNING: chunks.jsonl and index.npz are out of sync; "
              "rerun build_index.py.", file=sys.stderr)
    return vectors, chunks


def top_k(query_vec: np.ndarray, vectors: np.ndarray, k: int) -> list[int]:
    qn = query_vec / (np.linalg.norm(query_vec) + 1e-9)
    vn = vectors / (np.linalg.norm(vectors, axis=1, keepdims=True) + 1e-9)
    sims = vn @ qn
    return list(np.argsort(-sims)[:k]), sims


def cite(chunk: dict) -> str:
    pages = chunk["page_start"]
    if chunk["page_start"] != chunk["page_end"]:
        pages = f"{chunk['page_start']}-{chunk['page_end']}"
    return f"{chunk['pdf_stem']}.pdf p.{pages} (via {chunk['md_path']})"


def call_ollama_chat(model: str, question: str, context_blocks: list[str]) -> str:
    context = "\n\n---\n\n".join(context_blocks)
    system = (
        "Respondes solo con lo que aparece en el CONTEXTO. Si el contexto no "
        "alcanza para responder, dilo explicitamente. Cita siempre el "
        "identificador de fuente entre corchetes tal como aparece en el "
        "contexto, p.ej. [Bombelli_1987_PhD.pdf p.12]. No inventes numeros de "
        "ecuacion ni relaciones de orden causal que no esten literalmente en "
        "el contexto: son texto derivado de PDF, no la transcripcion "
        "autoritativa."
    )
    prompt = f"CONTEXTO:\n{context}\n\nPREGUNTA: {question}"
    r = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            "stream": False,
        },
        timeout=600,
    )
    r.raise_for_status()
    return r.json()["message"]["content"]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("question", help="query, any language")
    ap.add_argument("-k", type=int, default=6, help="number of chunks to retrieve")
    ap.add_argument("--answer", action="store_true",
                     help="also synthesize an answer with a local Ollama chat model")
    ap.add_argument("--model", default=DEFAULT_ANSWER_MODEL,
                     help=f"Ollama chat model for --answer (default {DEFAULT_ANSWER_MODEL})")
    args = ap.parse_args()

    if not (INDEX_DIR / "index.npz").exists():
        print(f"No index at {INDEX_DIR}. Run build_index.py first.", file=sys.stderr)
        return 1

    vectors, chunks = load_index()
    qvec = embed_query(args.question)
    idxs, sims = top_k(qvec, vectors, args.k)

    print(f"# {len(idxs)} resultados para: {args.question}\n")
    context_blocks = []
    for i in idxs:
        c = chunks[i]
        label = cite(c)
        print(f"## [{label}]  (sim={sims[i]:.3f})")
        snippet = c["text"][:600].strip()
        print(snippet + ("..." if len(c["text"]) > 600 else ""))
        print()
        context_blocks.append(f"[{label}]\n{c['text']}")

    print(f"--\n{DISCLAIMER}")

    if args.answer:
        print(f"\n# Respuesta ({args.model}, local, sin coste de API)\n")
        try:
            answer = call_ollama_chat(args.model, args.question, context_blocks)
        except requests.RequestException as e:
            print(f"ERROR llamando a Ollama ({e}). "
                  f"Prueba `ollama pull {args.model}` primero.", file=sys.stderr)
            return 1
        print(answer)
        print(f"\n--\n{DISCLAIMER}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
