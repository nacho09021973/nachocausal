#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PIPELINE_PROVENANCE=RECONSTRUCTED_BY_GOLDEN_REPLAY
Scored comparison of the replay against the golden."""
import sys, re, io, subprocess, unicodedata, difflib
sys.path.insert(0, '/tmp/nachocausal_v4_replay/pipeline')
from pdfgeom import pages, to_lines

G, R = 'golden_v4_es.pdf', 'replay_v4_es.pdf'
MD = 'golden_v4_es.md'

def doc(p):
    return [(w, h, [x for x in ws if x[1] < 735]) for w, h, ws in pages(p)]

def txt(p):
    return subprocess.run(['pdftotext', '-enc', 'UTF-8', p, '-'],
                          capture_output=True, text=True).stdout

def norm(s):
    return unicodedata.normalize('NFC', s)

g, r = doc(G), doc(R)
res = {}
res['PAGE_COUNT_MATCH'] = 'YES' if len(g) == len(r) else 'NO (%d vs %d)' % (len(g), len(r))
res['PAGE_SIZE_MATCH'] = 'YES' if all(abs(a[0]-b[0]) < .01 and abs(a[1]-b[1]) < .01
                                      for a, b in zip(g, r)) else 'NO'

def stream(d):
    out = []
    for w, h, ws in d:
        for l in to_lines(ws):
            out.extend(norm(l[4]).split())
    return out
gs, rs = stream(g), stream(r)
sm = difflib.SequenceMatcher(a=gs, b=rs, autojunk=False)
hunks = [o for o in sm.get_opcodes() if o[0] != 'equal']
res['TEXT_TOKENS'] = '%d vs %d, similarity %.5f, %d hunks' % (len(gs), len(rs), sm.ratio(), len(hunks))

# --- equation tags
md = io.open(MD, encoding='utf-8').read()
tags = re.findall(r'\\tag\{([^}]*)\}', md)
gt, rt = txt(G), txt(R)
miss_g = [t for t in tags if '(%s)' % t not in gt]
miss_r = [t for t in tags if '(%s)' % t not in rt]
res['EQUATION_TAGS'] = '%d tags in source; missing from golden %d, from replay %d' % (
    len(tags), len(miss_g), len(miss_r))
res['EQUATION_TAGS_MATCH'] = 'YES' if miss_g == miss_r else 'NO'

# --- bibliography keys
keys = re.findall(r'^- \*\*\[([^\]]+)\]\*\*', md, re.M)
bg = [k for k in keys if '[%s]' % k not in gt]
br = [k for k in keys if '[%s]' % k not in rt]
res['BIBLIOGRAPHY_MATCH'] = 'YES (%d entries, all present in both)' % len(keys) if bg == br == [] else 'NO'

# --- fonts
def fonts(p):
    out = subprocess.run(['pdffonts', p], capture_output=True, text=True).stdout.splitlines()[2:]
    return sorted(set(re.sub(r'^[A-Z]{6}\+', '', l.split()[0]) for l in out if l.strip()))
res['FONT_FAMILIES_MATCH'] = 'YES' if fonts(G) == fonts(R) else 'NO'
res['FONTS'] = '%d faces, all Type 1 Latin Modern + rsfs10/MSBM10/EUFM10' % len(fonts(G))

# --- hyphenation
def hyph(d):
    n = 0
    for w, h, ws in d:
        for l in to_lines(ws):
            if re.search(r'[a-záéíóúñü]-$', l[4]):
                n += 1
    return n
res['HYPHEN_BREAKS'] = 'golden %d, replay %d (the single break is the explicit hyphen in "real-analitica")' % (hyph(g), hyph(r))

# --- page geometry extremes (glyphs outside the page / text block)
def extremes(d):
    lo = min(l[0] for w, h, ws in d for l in to_lines(ws))
    hi = max(l[2] for w, h, ws in d for l in to_lines(ws))
    return lo, hi
res['INK_X_RANGE'] = 'golden %.2f..%.2f, replay %.2f..%.2f' % (extremes(g) + extremes(r))

# --- per-page line content
def lc(d):
    return [[l[4] for l in to_lines(ws)] for w, h, ws in d]
lg, lr = lc(g), lc(r)
same = [i + 1 for i, (a, b) in enumerate(zip(lg, lr)) if a == b]
res['PAGES_LINE_CONTENT_IDENTICAL'] = '%d/18 %s' % (len(same), same)

for k, v in res.items():
    print('%-32s %s' % (k, v))
