#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Align the geometric signatures of two PDFs page by page and report the
first vertical divergence."""
import sys
sys.path.insert(0, '/tmp/nachocausal_v4_replay/pipeline')
from pdfsig import signature

def blocks(pdf, p):
    sig, rules = signature(pdf, p)
    return sig

def key(s):
    return (s['type'], s['text'][:28], s['tag'])

if __name__ == '__main__':
    A, B = sys.argv[1], sys.argv[2]
    pgs = [int(x) for x in sys.argv[3].split(',')]
    prev_ok = None
    for p in pgs:
        ga, gb = blocks(A, p), blocks(B, p)
        print('===== page %d :  %s=%d rows   %s=%d rows'
              % (p, A.split('/')[-1], len(ga), B.split('/')[-1], len(gb)))
        n = min(len(ga), len(gb))
        first = None
        for i in range(n):
            same_txt = key(ga[i]) == key(gb[i])
            dy = gb[i]['base'] - ga[i]['base']
            if abs(dy) > 0.005 or not same_txt:
                first = i
                break
        if first is None and len(ga) == len(gb):
            print('   IDENTICAL (all %d rows, max |dy| < 0.005pt)' % n)
            prev_ok = (p, ga[-1] if ga else None)
            continue
        if first is None:
            first = n
        print('   first divergence at row %d' % first)
        for i in range(max(0, first - 2), min(n, first + 3)):
            mark = '>>' if i == first else '  '
            print('%s G base=%9.3f x=%6.2f sz=%6.3f %-12s %s'
                  % (mark, ga[i]['base'], ga[i]['x0'], ga[i]['size'], ga[i]['type'], ga[i]['text']))
            print('%s S base=%9.3f x=%6.2f sz=%6.3f %-12s %s'
                  % ('  ', gb[i]['base'], gb[i]['x0'], gb[i]['size'], gb[i]['type'], gb[i]['text']))
            print('     dy=%+.3f' % (gb[i]['base'] - ga[i]['base']))
        break
