#!/usr/bin/env python3
"""PIPELINE_PROVENANCE=RECONSTRUCTED_BY_GOLDEN_REPLAY
Per-page raster comparison of golden vs replay at identical resolution."""
import sys, os
from PIL import Image, ImageChops

def run(gd, rd, out, thresh=64):
    os.makedirs(out, exist_ok=True)
    gs = sorted(os.listdir(gd)); rs = sorted(os.listdir(rd))
    tot = 0
    print("%-5s %-11s %-9s %-9s %s" % ("page", "size", "diffpx", "pct", "bbox of differing ink"))
    for i, (a, b) in enumerate(zip(gs, rs), 1):
        A = Image.open(os.path.join(gd, a)).convert('L')
        B = Image.open(os.path.join(rd, b)).convert('L')
        if A.size != B.size:
            print("%-5d SIZE MISMATCH %s vs %s" % (i, A.size, B.size)); continue
        d = ImageChops.difference(A, B).point(lambda p: 255 if p > thresh else 0)
        n = sum(d.histogram()[255:])
        px = A.size[0] * A.size[1]
        bb = d.getbbox()
        tot += n
        print("%-5d %-11s %-9d %-9.4f %s" % (i, "x".join(map(str, A.size)), n, 100.0*n/px, bb))
        if n:
            Image.merge('RGB', (A, B, A)).save(os.path.join(out, 'overlay_p%02d.png' % i))
    print("TOTAL_DIFF_PIXELS=%d" % tot)

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], sys.argv[3])
