#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PIPELINE_PROVENANCE=RECONSTRUCTED_BY_GOLDEN_REPLAY
Geometric signature of a PDF page: exact baselines taken from the content
stream (Tm operators), rules from the path operators, text labels from
pdftotext -bbox.  Coordinates are reported from the TOP of the page."""
import sys, re, unicodedata
import pypdf
sys.path.insert(0, '/tmp/nachocausal_v4_replay/pipeline')
from pdfgeom import pages as _wordpages, to_lines

NUM = r'[-+]?[0-9]*\.?[0-9]+'
TM = re.compile((r'(%s) (%s) (%s) (%s) (%s) (%s) Tm' % ((NUM,) * 6)).encode())
TF = re.compile((r'/(\w+) (%s) Tf' % NUM).encode())
CM = re.compile((r'(%s) (%s) (%s) (%s) (%s) (%s) cm' % ((NUM,) * 6)).encode())
LINE = re.compile((r'(%s) (%s) m (%s) (%s) l S' % ((NUM,) * 4)).encode())
TJ = re.compile(rb'\]\s*TJ|\)\s*Tj')

def ops(pdf, pageno):
    """Yield ('text', x, ybase, size) and ('rule', x0, y, x1, y1, w)."""
    page = pypdf.PdfReader(pdf).pages[pageno - 1]
    H = float(page.mediabox.height)
    data = page.get_contents().get_data()
    out, size, cmx, cmy = [], 0.0, 0.0, 0.0
    pos = 0
    for m in re.finditer(rb'(?s).', data):  # cheap sequential scan below instead
        break
    # sequential scan over the interesting operators, in order
    pat = re.compile(TF.pattern + rb'|' + TM.pattern + rb'|' + CM.pattern + rb'|' + LINE.pattern)
    for m in pat.finditer(data):
        g = m.groups()
        if g[0] is not None:                      # Tf
            size = float(g[1])
        elif g[2] is not None:                    # Tm
            x, y = float(g[6]), float(g[7])
            # text follows this Tm up to the next operator
            tail = data[m.end():m.end() + 400]
            t = TJ.search(tail)
            if t:
                out.append(('text', x, H - y, size))
        elif g[8] is not None:                    # cm
            cmx, cmy = float(g[12]), float(g[13])
        elif g[14] is not None:                   # m ... l S
            x0, y0, x1, y1 = (float(v) for v in g[14:18])
            out.append(('rule', cmx + x0, H - (cmy + y0), cmx + x1, H - (cmy + y1)))
    return out, H

def rows(pdf, pageno, tol=0.6):
    o, H = ops(pdf, pageno)
    txt = [t for t in o if t[0] == 'text']
    rules = [t for t in o if t[0] == 'rule']
    groups = {}
    for _, x, y, s in txt:
        key = round(y / tol) * tol
        k = min(groups, key=lambda kk: abs(kk - key)) if groups else None
        if k is None or abs(k - key) > tol:
            k = key
        groups.setdefault(k, []).append((x, y, s))
    out = []
    for k in sorted(groups):
        g = groups[k]
        out.append(dict(base=min(v[1] for v in g), x0=min(v[0] for v in g),
                        x1=max(v[0] for v in g), size=max(v[2] for v in g),
                        n=len(g)))
    return out, rules, H

def label_map(pdf, pageno):
    for i, (w, h, ws) in enumerate(_wordpages(pdf), 1):
        if i == pageno:
            return [(l[1], l[3], l[0], l[2], l[4]) for l in to_lines([x for x in ws])]
    return []

def classify(text, x0, size):
    t = text.strip()
    if re.match(r'^(Teorema|Corolario|Lema|Proposici|Definici|Observaci)\s', t) and x0 < 75:
        return 'THEOREM_HEAD'
    if t.startswith('Demostraci') and x0 < 75:
        return 'PROOF_HEAD'
    if re.match(r'^\d+\s+\S', t) and size > 13 and x0 < 75:
        return 'SECTION_HEAD'
    if x0 < 75 or 86 < x0 < 92:
        return 'TEXT_LINE'
    return 'DISPLAY'

TAG = re.compile(r'\((\d+\.\d+)\)\s*$')

def signature(pdf, pageno):
    rws, rules, H = rows(pdf, pageno)
    labels = label_map(pdf, pageno)
    sig = []
    for r in rws:
        if r['base'] > 740:            # folio
            continue
        best, bd = '', 1e9
        for ytop, ybot, lx0, lx1, txt in labels:
            d = abs((ytop + ybot) / 2 - (r['base'] - r['size'] * 0.3))
            if d < bd and not (lx1 < r['x0'] - 2 or lx0 > r['x1'] + 2):
                bd, best = d, txt
        tag = TAG.search(best or '')
        sig.append(dict(base=round(r['base'], 3), x0=round(r['x0'], 2),
                        x1=round(r['x1'], 2), size=round(r['size'], 3),
                        type=classify(best or '', r['x0'], r['size']),
                        tag=tag.group(1) if tag else '',
                        text=unicodedata.normalize('NFC', (best or ''))[:50]))
    return sig, rules

if __name__ == '__main__':
    pdf = sys.argv[1]
    for p in [int(x) for x in sys.argv[2].split(',')]:
        sig, rules = signature(pdf, p)
        print('===== %s page %d =====' % (pdf, p))
        for s in sig:
            print('  base=%8.3f x=%6.2f..%-6.2f sz=%6.3f %-12s tag=%-5s %s'
                  % (s['base'], s['x0'], s['x1'], s['size'], s['type'], s['tag'], s['text']))
        for r in rules:
            print('  RULE  y=%8.3f x=%6.2f..%-6.2f' % (r[2], r[1], r[3]))
