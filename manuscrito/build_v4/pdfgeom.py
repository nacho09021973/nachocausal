#!/usr/bin/env python3
"""Group pdftotext -bbox words into lines. Shared by golden/replay analysis."""
import subprocess, re, sys, html

WORD = re.compile(
    r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>')
PAGE = re.compile(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', re.S)

def pages(pdf):
    out = subprocess.run(['pdftotext', '-bbox', '-enc', 'UTF-8', pdf, '-'],
                         capture_output=True, text=True).stdout
    for pm in PAGE.finditer(out):
        w, h = float(pm.group(1)), float(pm.group(2))
        words = [(float(a), float(b), float(c), float(d), html.unescape(t))
                 for a, b, c, d, t in WORD.findall(pm.group(3))]
        yield w, h, words

def to_lines(words, tol=1.5):
    lines, cur, cury = [], [], None
    for w in sorted(words, key=lambda w: (round(w[1], 1), w[0])):
        if cury is None or abs(w[1] - cury) <= tol:
            cur.append(w); cury = w[1] if cury is None else cury
        else:
            lines.append(cur); cur = [w]; cury = w[1]
    if cur: lines.append(cur)
    out = []
    for ln in lines:
        ln = sorted(ln, key=lambda w: w[0])
        out.append((min(w[0] for w in ln), min(w[1] for w in ln),
                    max(w[2] for w in ln), max(w[3] for w in ln),
                    ' '.join(w[4] for w in ln)))
    return out

if __name__ == '__main__':
    pdf = sys.argv[1]
    want = set(int(x) for x in sys.argv[2].split(',')) if len(sys.argv) > 2 else None
    for i, (w, h, words) in enumerate(pages(pdf), 1):
        if want and i not in want: continue
        print(f"===== page {i}  ({w:.0f}x{h:.0f}) =====")
        for x0, y0, x1, y1, t in to_lines(words):
            print(f"x0={x0:6.1f} x1={x1:6.1f} y={y0:6.1f} h={y1-y0:5.2f} | {t[:76]}")
