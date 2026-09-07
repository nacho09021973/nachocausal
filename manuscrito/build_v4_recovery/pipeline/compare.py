#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PIPELINE_PROVENANCE=RECONSTRUCTED_BY_GOLDEN_REPLAY
Compare golden vs replay PDFs: content stream, page breaks, geometry."""
import sys, re, difflib, unicodedata
sys.path.insert(0, '/tmp/nachocausal_v4_replay/pipeline')
from pdfgeom import pages, to_lines

FOOT = 735.0   # folio band: y below this is body

def doc(pdf):
    out = []
    for w, h, words in pages(pdf):
        body = [x for x in words if x[1] < FOOT]
        foot = [x for x in words if x[1] >= FOOT]
        out.append({'w': w, 'h': h, 'words': body,
                    'lines': to_lines(body),
                    'folio': ' '.join(x[4] for x in sorted(foot, key=lambda x: x[0]))})
    return out

def stream(d):
    toks = []
    for p in d:
        for ln in p['lines']:
            toks.extend(ln[4].split())
    return toks

def norm(t):
    t = unicodedata.normalize('NFC', t)
    return t

if __name__ == '__main__':
    g, r = doc(sys.argv[1]), doc(sys.argv[2])
    print("PAGES  golden=%d replay=%d" % (len(g), len(r)))
    print("SIZE   golden=%.0fx%.0f replay=%.0fx%.0f" % (g[0]['w'], g[0]['h'], r[0]['w'], r[0]['h']))
    print("FOLIOS golden=%s" % ','.join(p['folio'] for p in g))
    print("FOLIOS replay=%s" % ','.join(p['folio'] for p in r))
    gs, rs = [norm(x) for x in stream(g)], [norm(x) for x in stream(r)]
    print("TOKENS golden=%d replay=%d" % (len(gs), len(rs)))
    sm = difflib.SequenceMatcher(a=gs, b=rs, autojunk=False)
    ndiff = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        ndiff += 1
        if ndiff <= 40:
            print("  %-7s g[%d:%d]=%s | r[%d:%d]=%s"
                  % (tag, i1, i2, ' '.join(gs[i1:i2])[:90],
                     j1, j2, ' '.join(rs[j1:j2])[:90]))
    print("DIFF_HUNKS=%d  ratio=%.5f" % (ndiff, sm.ratio()))
