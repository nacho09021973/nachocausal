"""Independent brute-force check of the Lean theorem `fiber_eq` (manuscript C.5).

Model, mirroring the Lean file exactly:
  leSigma s i j  <->  i <= j and s[i] <= s[j]
  PosetIsomorphic s t <-> exists bijection e with
        leSigma s i j <-> leSigma t (e i) (e j)  for all i,j
  tau_{a,b}: b -> a ; i -> i+1 for a<=i<b ; identity elsewhere
Checks, for every N and every 0<=a<b<N, that
  {s : PosetIsomorphic s tau} == {tau, tau^{-1}}
"""
from itertools import permutations


def tau(a, b, N):
    t = []
    for k in range(N):
        if k == b:
            t.append(a)
        elif a <= k < b:
            t.append(k + 1)
        else:
            t.append(k)
    return tuple(t)


def inv(s):
    r = [0] * len(s)
    for i, v in enumerate(s):
        r[v] = i
    return tuple(r)


def rel(s, N):
    return frozenset((i, j) for i in range(N) for j in range(N)
                     if i <= j and s[i] <= s[j])


def iso(rs, rt, N, bijs):
    for e in bijs:
        if all(((i, j) in rs) == ((e[i], e[j]) in rt)
               for i in range(N) for j in range(N)):
            return True
    return False


for N in range(2, 7):
    perms = list(permutations(range(N)))
    bijs = perms
    rels = {s: rel(s, N) for s in perms}
    for a in range(N):
        for b in range(a + 1, N):
            t = tau(a, b, N)
            rt = rels[t]
            fiber = {s for s in perms if iso(rels[s], rt, N, bijs)}
            expected = {t, inv(t)}
            assert fiber == expected, (N, a, b, sorted(fiber), sorted(expected))
            # cross-check the adjacency dichotomy proved in Lean
            assert (t == inv(t)) == (b == a + 1), (N, a, b)
            assert len(fiber) == (1 if b == a + 1 else 2)
    print(f"N={N}: all {N*(N-1)//2} pairs (a,b) OK  "
          f"[fiber == {{tau, tau^-1}}, |fiber| = 1 iff b=a+1]")
print("PASS: brute force agrees with the Lean theorem fiber_eq for N = 2..6")
