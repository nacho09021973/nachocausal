"""Independent numeric check of the Appendix C matrix chain formalized in Lean.

Mirrors, from the raw definitions, exactly the objects of `CycleLaplacian.lean` and
`SpanTheoremC.lean` (0-indexed, as in Lean):

    tau_{a,b}        b -> a ; k -> k+1 for a <= k < b ; identity elsewhere
    P_sigma[i][j]    = 1 iff sigma(i) = j                      (manuscript (3.12))
    S_{a,b}          = P_tau + P_tau^T                         (C.10)
    cproj            = I - J/N                                 (= I_{E_N})
    restr M          = cproj @ M @ cproj                       (= M|_{E_N})
    Qmat(x,y)        = 2*cproj - restr(S_{x,y})                (C.12)
    wInv(i,j)(x,y)   = [(x,y)=(i,j)] - (1/2)[y=x+1 and i<=x<j] (C.15)
    cCoef(p)         = (1/N) * sum_{i<j} wInv(i,j)(p)          (C.17)

and checks the identities the Lean theorems assert:

    (C.13)/(C.14)  Qmat(a,b) = L_{a,b} + sum_{k in [a,b)} L_{k,k+1}
    (C.15)         sum_{x,y} wInv(i,j)(x,y) * Qmat(x,y) = L_{i,j}
    (C.17)         sum_p cCoef(p) * Qmat(p) = cproj
    (C.18)         sum_p cCoef(p) = s_N = (N-1)(5-N)/12
    (C.19)         (1-2 s_N) * cproj = - sum_p cCoef(p) * S_p|_{E_N}
    (C.21)/final   span{A_C|_{E_N} : C in classes} = Sym(E_N), dimension N(N-1)/2

THIS SCRIPT PARTICIPATES IN NO LEAN PROOF. It is evidence that the formalized
*statements* say what Appendix C says; the proofs are the Lean terms, kernel-checked
for all N at once.
"""
from itertools import permutations

import numpy as np

TOL = 1e-9


def tau(a, b, N):
    return tuple(a if k == b else (k + 1 if a <= k < b else k) for k in range(N))


def permmat(s, N):
    P = np.zeros((N, N))
    for i in range(N):
        P[i, s[i]] = 1.0
    return P


def edgeL(i, j, N):
    e = np.zeros(N)
    e[i] += 1.0
    e[j] -= 1.0
    return np.outer(e, e)


def run(N):
    cproj = np.eye(N) - np.ones((N, N)) / N
    restr = lambda M: cproj @ M @ cproj
    pairs = [(x, y) for x in range(N) for y in range(N) if x < y]

    S = {(a, b): permmat(tau(a, b, N), N) + permmat(tau(a, b, N), N).T for a, b in pairs}
    Q = {p: 2 * cproj - restr(S[p]) for p in pairs}

    # (C.13)/(C.14)
    for a, b in pairs:
        cyc = edgeL(a, b, N) + sum(edgeL(k, k + 1, N) for k in range(a, b))
        assert np.allclose(Q[(a, b)], cyc, atol=TOL), ("C.14", N, a, b)
        if b == a + 1:
            assert np.allclose(Q[(a, b)], 2 * edgeL(a, b, N), atol=TOL), ("C.13", N, a, b)

    def wInv(i, j, p):
        x, y = p
        return (1.0 if (x, y) == (i, j) else 0.0) - (
            0.5 if (y == x + 1 and i <= x < j) else 0.0)

    # (C.15)
    for i, j in pairs:
        got = sum(wInv(i, j, p) * Q[p] for p in pairs)
        assert np.allclose(got, edgeL(i, j, N), atol=TOL), ("C.15", N, i, j)

    # (C.17), (C.18), (C.19)
    c = {p: sum(wInv(i, j, p) for i, j in pairs) / N for p in pairs}
    assert np.allclose(sum(c[p] * Q[p] for p in pairs), cproj, atol=TOL), ("C.17", N)
    sN = (N - 1) * (5 - N) / 12
    assert abs(sum(c.values()) - sN) < TOL, ("C.18", N, sum(c.values()), sN)
    lhs = (1 - 2 * sN) * cproj
    rhs = -sum(c[p] * restr(S[p]) for p in pairs)
    assert np.allclose(lhs, rhs, atol=TOL), ("C.19", N)
    assert abs(1 - 2 * sN) > TOL, ("C.20", N)

    # (C.21) and the final class-sum span, by rank over all realized poset classes
    def rel(s):
        return frozenset((i, j) for i in range(N) for j in range(N)
                         if i <= j and s[i] <= s[j])

    perms = list(permutations(range(N)))
    rels = {s: rel(s) for s in perms}

    def iso(rs, rt):
        return any(all(((i, j) in rs) == ((e[i], e[j]) in rt)
                       for i in range(N) for j in range(N)) for e in perms)

    classes = []
    for s in perms:
        if not any(iso(rels[s], rels[t]) for t in classes):
            classes.append(s)
    A = {t: sum(permmat(s, N) for s in perms if iso(rels[s], rels[t])) for t in classes}

    def vec(M):
        return np.array([M[i, j] for i in range(N) for j in range(i, N)])

    rk_S = np.linalg.matrix_rank(np.array([vec(restr(S[p])) for p in pairs]), tol=1e-8)
    rk_A = np.linalg.matrix_rank(np.array([vec(restr(A[t])) for t in classes]), tol=1e-8)
    target = N * (N - 1) // 2
    assert rk_S == target, ("C.21", N, rk_S, target)
    assert rk_A == target, ("final", N, rk_A, target)
    return len(classes), target


for N in range(2, 7):
    nclasses, dim = run(N)
    print(f"N={N}: (C.13),(C.14),(C.15),(C.17),(C.18),(C.19),(C.20),(C.21) OK; "
          f"{nclasses} poset classes, span dim = {dim} = C(N,2)")
print("PASS: numeric check agrees with the Lean statements for N = 2..6")
