/*
Exact finite gate for the first covtree witness case not covered by the
computational range reported in Gutzeit--Shaban--Yeats--Zalel (2026).

Frozen question
---------------
For n=6 and Gamma={A,B,C}, can a smallest witness have size 10 and height
at least 4?  Since n+3=9, such a witness would be the first possible finite
counterexample beyond the authors' reported search (all witnesses through
size 9, and size 10 at height at most 3).

Completeness reduction
----------------------
If a smallest witness Q has size 10, the shortest-path setup of Section 5
may be chosen so that Q=A union C for two distinct six-element anchor
downsets.  Then X=A intersection C is a two-element downset, A\X and C\X
have four elements each, and no element of A\X can be comparable with an
element of C\X (otherwise A or C would fail to be a downset).  Therefore Q
is exactly an amalgam of two six-element posets over a common pointed
two-element downset X.  The program enumerates all such pointed isomorphism
types and both identifications when X is an antichain.

Acceptance rule (existential aggregation)
----------------------------------------
A node Gamma is closed as soon as SOME size-10 representation of it contains a
proper downset whose six-downsets realise the same three types: that proper
downset is itself a witness of size <= 9.  One reducible representation is
therefore sufficient, and the only number that can indicate a counterexample is
a node with ZERO reducible representations.  Requiring every representation to
reduce -- as the first revision of this file did -- is strictly stronger than
the question being asked and reports spurious partial failures.  The program
exits 0 only when no node has zero reducible representations; otherwise it
prints the survivors and exits 4.

Dependency on Theorem 5.1 (external input, NOT established here)
----------------------------------------------------------------
The sweep enumerates only smallest witnesses of size exactly 10.  The step that
turns it into a statement about n=6 is Theorem 5.1 of the paper, which supplies
a witness of size at most floor((3/2)(6+1)) = 10 for every node.  Hence if no
witness of size <= 9 existed, one of size exactly 10 would have to exist, and it
would appear in this enumeration.  Without Theorem 5.1 a node whose smallest
witness had size 11 or 12 would fall outside the sweep entirely, since Theorem
4.1 alone permits n(k-1) = 12.

What is and is not established
------------------------------
ESTABLISHED (given Theorem 5.1): every node Gamma_6 with |Gamma_6| = 3 has a
witness of size at most 9 = n+3, at every height.

NOT established, and false as stated: that every MINIMAL witness has size <= 9.
Three nodes, reported below as ALLH_PARTIAL, carry size-10 representations with
no proper sub-witness -- witnesses minimal under inclusion that are not of
minimum cardinality.  They are precisely why Theorem 5.1 is existential.

This is a computational finite-case certificate for n=6, not a proof of the n+3
conjecture for arbitrary n.

Output is sorted so that a run is byte-reproducible and the artefact can be
sealed by hash; unordered_map iteration order is not otherwise guaranteed.
*/

#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using Code = std::uint64_t;

namespace {

constexpr int N = 6;

std::vector<std::array<int, N>> permutations6() {
    std::array<int, N> p{};
    for (int i = 0; i < N; ++i) p[i] = i;
    std::vector<std::array<int, N>> out;
    do {
        out.push_back(p);
    } while (std::next_permutation(p.begin(), p.end()));
    return out;
}

const std::vector<std::array<int, N>> PERMS6 = permutations6();

inline bool related(Code code, int i, int j, int n) {
    return (code >> (i * n + j)) & Code{1};
}

Code relabel6(Code code, const std::array<int, N>& old_to_new) {
    Code out = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (related(code, i, j, N)) {
                out |= Code{1} << (old_to_new[i] * N + old_to_new[j]);
            }
        }
    }
    return out;
}

Code canonical6(Code code) {
    Code best = ~Code{0};
    for (const auto& p : PERMS6) best = std::min(best, relabel6(code, p));
    return best;
}

bool is_transitive6(Code code) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (!related(code, i, j, N)) continue;
            for (int k = 0; k < N; ++k) {
                if (related(code, j, k, N) && !related(code, i, k, N)) return false;
            }
        }
    }
    return true;
}

std::vector<Code> unlabeled_posets6() {
    std::array<std::pair<int, int>, 15> pairs{};
    int t = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) pairs[t++] = {i, j};
    }

    std::unordered_set<Code> seen;
    for (std::uint32_t mask = 0; mask < (1u << pairs.size()); ++mask) {
        Code code = 0;
        for (std::size_t b = 0; b < pairs.size(); ++b) {
            if ((mask >> b) & 1u) {
                const auto [i, j] = pairs[b];
                code |= Code{1} << (i * N + j);
            }
        }
        if (is_transitive6(code)) seen.insert(canonical6(code));
    }
    std::vector<Code> out(seen.begin(), seen.end());
    std::sort(out.begin(), out.end());
    return out;
}

bool is_downset6(Code code, int a, int b) {
    const unsigned subset = (1u << a) | (1u << b);
    for (int v : {a, b}) {
        for (int u = 0; u < N; ++u) {
            if (related(code, u, v, N) && !(subset & (1u << u))) return false;
        }
    }
    return true;
}

Code rooted_code(Code code, int x0, int x1) {
    std::array<int, 4> rest{};
    int t = 0;
    for (int v = 0; v < N; ++v) {
        if (v != x0 && v != x1) rest[t++] = v;
    }
    std::sort(rest.begin(), rest.end());

    Code best = ~Code{0};
    do {
        std::array<int, N> p{};
        p[x0] = 0;
        p[x1] = 1;
        for (int i = 0; i < 4; ++i) p[rest[i]] = i + 2;
        best = std::min(best, relabel6(code, p));
    } while (std::next_permutation(rest.begin(), rest.end()));
    return best;
}

struct RootedHalf {
    Code rooted{};
    Code unrooted{};
    bool chain_x{};
};

struct Poset10 {
    std::array<std::uint16_t, 10> successors{};
};

struct GammaHash {
    std::size_t operator()(const std::array<Code, 3>& x) const noexcept {
        std::size_t h = 0xcbf29ce484222325ULL;
        for (Code v : x) {
            h ^= std::hash<Code>{}(v) + 0x9e3779b97f4a7c15ULL + (h << 6) + (h >> 2);
        }
        return h;
    }
};

struct GammaStats {
    std::uint64_t representations{};
    std::uint64_t internally_reducible{};
    Poset10 representative{};
    int height{};
    int largest_smallest_internal{};
};

std::vector<RootedHalf> rooted_halves(const std::vector<Code>& posets) {
    std::unordered_map<Code, RootedHalf> by_root;
    for (Code p : posets) {
        for (int a = 0; a < N; ++a) {
            for (int b = a + 1; b < N; ++b) {
                if (!is_downset6(p, a, b)) continue;
                const bool ab = related(p, a, b, N);
                const bool ba = related(p, b, a, N);
                if (ab || ba) {
                    const int low = ab ? a : b;
                    const int high = ab ? b : a;
                    Code r = rooted_code(p, low, high);
                    by_root.emplace(r, RootedHalf{r, p, true});
                } else {
                    for (const auto& [x0, x1] : {std::pair{a, b}, std::pair{b, a}}) {
                        Code r = rooted_code(p, x0, x1);
                        by_root.emplace(r, RootedHalf{r, p, false});
                    }
                }
            }
        }
    }
    std::vector<RootedHalf> out;
    out.reserve(by_root.size());
    for (const auto& [_, h] : by_root) out.push_back(h);
    std::sort(out.begin(), out.end(), [](const auto& lhs, const auto& rhs) {
        return lhs.rooted < rhs.rooted;
    });
    return out;
}

Poset10 amalgamate(const RootedHalf& a, const RootedHalf& c) {
    Poset10 q;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (related(a.rooted, i, j, N)) q.successors[i] |= std::uint16_t{1} << j;
            if (!related(c.rooted, i, j, N)) continue;
            const int ii = i < 2 ? i : i + 4;
            const int jj = j < 2 ? j : j + 4;
            q.successors[ii] |= std::uint16_t{1} << jj;
        }
    }
    return q;
}

inline bool related10(const Poset10& q, int i, int j) {
    return (q.successors[i] >> j) & 1u;
}

bool is_downset10(const Poset10& q, unsigned subset) {
    for (int v = 0; v < 10; ++v) {
        if (!(subset & (1u << v))) continue;
        for (int u = 0; u < 10; ++u) {
            if (related10(q, u, v) && !(subset & (1u << u))) return false;
        }
    }
    return true;
}

bool is_strict_poset10(const Poset10& q) {
    for (int i = 0; i < 10; ++i) {
        if (related10(q, i, i)) return false;
        for (int j = 0; j < 10; ++j) {
            if (!related10(q, i, j)) continue;
            if (related10(q, j, i)) return false;
            for (int k = 0; k < 10; ++k) {
                if (related10(q, j, k) && !related10(q, i, k)) return false;
            }
        }
    }
    return true;
}

Code induced6(const Poset10& q, unsigned subset) {
    std::array<int, N> verts{};
    int t = 0;
    for (int v = 0; v < 10; ++v) {
        if (subset & (1u << v)) verts[t++] = v;
    }
    Code out = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (related10(q, verts[i], verts[j])) out |= Code{1} << (i * N + j);
        }
    }
    return out;
}

int height10(const Poset10& q) {
    std::array<int, 10> memo{};
    auto dfs = [&](auto&& self, int v) -> int {
        if (memo[v]) return memo[v];
        int best = 1;
        for (int u = 0; u < 10; ++u) {
            if (related10(q, u, v)) best = std::max(best, self(self, u) + 1);
        }
        return memo[v] = best;
    };
    int best = 0;
    for (int v = 0; v < 10; ++v) best = std::max(best, dfs(dfs, v));
    return best;
}

}  // namespace


// ---------------------------------------------------------------------------
// Regularity of U -- finite corroboration of the GENERAL statements.
//
// Every statement below is quantified over all n and all m >= 3 in the write-up;
// this bench only instantiates n = 6, m = 4, k = 3 and counts violations.
//
//   F1  X = A cap C is a downset of Q.
//   F2  no element of A\X is comparable with an element of C\X.
//   LA  (Lemma A)  Max(A\X) is non-empty and contained in Max(Q); same for C\X.
//   L52 (imported Lemma 5.2, m >= 3)  every n-downset D with tau(D) != tau_B
//       satisfies A\X subset D or C\X subset D.
//   TR  (Theorem R)  every n-downset D with tau(D) != tau_B meets Max(Q).
//   F3  multiplicity of tau_B is at least m - 1 = 3.
//   CU  (Corollary U) a multiplicity-one type is never tau_B, and its unique
//       copy U satisfies Max(Q) cap U != empty.
//
// L52, TR, F3 and CU are claimed only inside the Section 5 configuration; the
// bench reports inside and outside separately.  F1, F2 and LA are claimed for
// every admissible amalgam, inside or outside.
// ---------------------------------------------------------------------------
int main() {
    const auto posets = unlabeled_posets6();
    const auto halves = rooted_halves(posets);

    constexpr unsigned A_SET = 0b0000111111u;
    constexpr unsigned C_SET = 0b1111000011u;
    constexpr unsigned AX    = 0b0000111100u;
    constexpr unsigned CX    = 0b1111000000u;

    std::unordered_map<Code, Code> canon_cache;
    std::uint64_t witness_pairs = 0, s5_pairs = 0;
    std::uint64_t f1_viol = 0, f2_viol = 0, la_viol = 0, la_empty = 0;
    std::uint64_t l52_viol_in = 0, l52_viol_out = 0;
    std::uint64_t tr_viol_in = 0, tr_viol_out = 0;
    std::uint64_t f3_viol_in = 0, f3_viol_out = 0;
    std::uint64_t mult1_is_b_in = 0, mult1_is_b_out = 0;
    std::uint64_t cu_viol_in = 0, cu_viol_out = 0;
    std::uint64_t mult1_copies_in = 0, mult1_copies_out = 0;
    std::array<std::uint64_t, 11> u_hist_in{}, u_hist_out{};
    std::array<std::uint64_t, 11> multb_hist_in{}, multb_hist_out{};
    // Does the stronger side-form hold: U contains Max(A\X) or Max(C\X)?
    std::uint64_t cu_side_viol_in = 0;

    for (const auto& a : halves) {
        for (const auto& c : halves) {
            if (a.chain_x != c.chain_x) continue;
            if (a.unrooted == c.unrooted) continue;
            const Poset10 q = amalgamate(a, c);
            if (!is_strict_poset10(q) || !is_downset10(q, A_SET) || !is_downset10(q, C_SET)) {
                std::cerr << "AMALGAM_INVARIANT_FAILURE\n";
                return 3;
            }

            std::set<Code> types;
            std::vector<std::pair<unsigned, Code>> downsets6;
            for (unsigned s = 0; s < (1u << 10); ++s) {
                if (__builtin_popcount(s) != 6 || !is_downset10(q, s)) continue;
                const Code raw = induced6(q, s);
                auto it = canon_cache.find(raw);
                const Code canonical = it == canon_cache.end()
                    ? canon_cache.emplace(raw, canonical6(raw)).first->second
                    : it->second;
                types.insert(canonical);
                downsets6.push_back({s, canonical});
                if (types.size() > 3) break;
            }
            if (types.size() != 3 || !types.contains(a.unrooted) || !types.contains(c.unrooted)) continue;
            ++witness_pairs;

            const Code b_type = [&] {
                for (Code t : types) {
                    if (t != a.unrooted && t != c.unrooted) return t;
                }
                return Code{0};
            }();

            unsigned maxmask = 0;
            for (int v = 0; v < 10; ++v) {
                bool above = false;
                for (int u = 0; u < 10; ++u) {
                    if (related10(q, v, u)) { above = true; break; }
                }
                if (!above) maxmask |= (1u << v);
            }

            // F1: X = {0,1} is a downset of Q.
            if (!is_downset10(q, 0b0000000011u)) ++f1_viol;
            // F2: A\X and C\X are mutually incomparable.
            for (int i = 2; i < 6; ++i) {
                for (int j = 6; j < 10; ++j) {
                    if (related10(q, i, j) || related10(q, j, i)) ++f2_viol;
                }
            }
            // LA: Max of each half, computed INSIDE the half, lands in Max(Q).
            auto side_max = [&](unsigned side) {
                unsigned mx = 0;
                for (int v = 0; v < 10; ++v) {
                    if (!(side & (1u << v))) continue;
                    bool above = false;
                    for (int u = 0; u < 10; ++u) {
                        if ((side & (1u << u)) && related10(q, v, u)) { above = true; break; }
                    }
                    if (!above) mx |= (1u << v);
                }
                return mx;
            };
            const unsigned max_ax = side_max(AX), max_cx = side_max(CX);
            if (!max_ax || !max_cx) ++la_empty;
            if ((max_ax & ~maxmask) || (max_cx & ~maxmask)) ++la_viol;

            // Section 5 configuration: a shortest A - B - B - B - C path exists.
            auto adj = [](unsigned p1, unsigned p2) { return __builtin_popcount(p1 & ~p2) == 1; };
            bool s5 = false;
            for (const auto& [s1, t1] : downsets6) {
                if (t1 != b_type || !adj(A_SET, s1)) continue;
                for (const auto& [s2, t2] : downsets6) {
                    if (t2 != b_type || !adj(s1, s2)) continue;
                    for (const auto& [s3, t3] : downsets6) {
                        if (t3 == b_type && adj(s2, s3) && adj(s3, C_SET)) s5 = true;
                    }
                }
            }
            if (s5) ++s5_pairs;

            std::unordered_map<Code, int> mult;
            for (const auto& [s, t] : downsets6) ++mult[t];

            // F3: multiplicity of tau_B is at least m - 1 = 3.
            const int mb = mult[b_type];
            (s5 ? multb_hist_in : multb_hist_out)[std::min(mb, 10)]++;
            if (mb < 3) { if (s5) ++f3_viol_in; else ++f3_viol_out; }

            for (const auto& [s, t] : downsets6) {
                if (t == b_type) continue;
                // L52: D contains A\X or C\X.
                const bool side = ((s & AX) == AX) || ((s & CX) == CX);
                if (!side) { if (s5) ++l52_viol_in; else ++l52_viol_out; }
                // TR: D meets Max(Q).
                if (!(s & maxmask)) { if (s5) ++tr_viol_in; else ++tr_viol_out; }
            }

            // CU: multiplicity-one types.
            for (const auto& [t, count] : mult) {
                if (count != 1) continue;
                (s5 ? mult1_copies_in : mult1_copies_out)++;
                if (t == b_type) { if (s5) ++mult1_is_b_in; else ++mult1_is_b_out; }
                for (const auto& [s, tt] : downsets6) {
                    if (tt != t) continue;
                    const int hit = __builtin_popcount(s & maxmask);
                    (s5 ? u_hist_in : u_hist_out)[std::min(hit, 10)]++;
                    if (hit == 0) { if (s5) ++cu_viol_in; else ++cu_viol_out; }
                    if (s5 && ((s & max_ax) != max_ax) && ((s & max_cx) != max_cx)) {
                        ++cu_side_viol_in;
                    }
                }
            }
        }
    }

    std::cout << "WITNESS_PAIRS=" << witness_pairs << '\n';
    std::cout << "S5_PAIRS=" << s5_pairs << '\n';
    std::cout << "NON_S5_PAIRS=" << witness_pairs - s5_pairs << '\n';
    std::cout << "F1_X_NOT_DOWNSET=" << f1_viol << '\n';
    std::cout << "F2_CROSS_COMPARABILITIES=" << f2_viol << '\n';
    std::cout << "LA_EMPTY_SIDE_MAX=" << la_empty << '\n';
    std::cout << "LA_SIDEMAX_NOT_GLOBAL_MAX=" << la_viol << '\n';
    std::cout << "L52_VIOLATIONS_INSIDE_S5=" << l52_viol_in << '\n';
    std::cout << "L52_VIOLATIONS_OUTSIDE_S5=" << l52_viol_out << '\n';
    std::cout << "TR_VIOLATIONS_INSIDE_S5=" << tr_viol_in << '\n';
    std::cout << "TR_VIOLATIONS_OUTSIDE_S5=" << tr_viol_out << '\n';
    std::cout << "F3_MULTB_LT_3_INSIDE_S5=" << f3_viol_in << '\n';
    std::cout << "F3_MULTB_LT_3_OUTSIDE_S5=" << f3_viol_out << '\n';
    for (int i = 0; i <= 10; ++i) {
        if (multb_hist_in[i]) std::cout << "MULTB_INSIDE_S5_" << i << '=' << multb_hist_in[i] << '\n';
    }
    for (int i = 0; i <= 10; ++i) {
        if (multb_hist_out[i]) std::cout << "MULTB_OUTSIDE_S5_" << i << '=' << multb_hist_out[i] << '\n';
    }
    std::cout << "MULT1_COPIES_INSIDE_S5=" << mult1_copies_in << '\n';
    std::cout << "MULT1_COPIES_OUTSIDE_S5=" << mult1_copies_out << '\n';
    std::cout << "MULT1_TYPE_IS_B_INSIDE_S5=" << mult1_is_b_in << '\n';
    std::cout << "MULT1_TYPE_IS_B_OUTSIDE_S5=" << mult1_is_b_out << '\n';
    std::cout << "CU_VIOLATIONS_INSIDE_S5=" << cu_viol_in << '\n';
    std::cout << "CU_VIOLATIONS_OUTSIDE_S5=" << cu_viol_out << '\n';
    std::cout << "CU_SIDE_FORM_VIOLATIONS_INSIDE_S5=" << cu_side_viol_in << '\n';
    for (int i = 0; i <= 10; ++i) {
        if (u_hist_in[i]) std::cout << "U_MAXHITS_INSIDE_S5_" << i << '=' << u_hist_in[i] << '\n';
    }
    for (int i = 0; i <= 10; ++i) {
        if (u_hist_out[i]) std::cout << "U_MAXHITS_OUTSIDE_S5_" << i << '=' << u_hist_out[i] << '\n';
    }
    const bool pass = f1_viol == 0 && f2_viol == 0 && la_empty == 0 && la_viol == 0
                   && l52_viol_in == 0 && tr_viol_in == 0 && f3_viol_in == 0
                   && mult1_is_b_in == 0 && cu_viol_in == 0;
    std::cout << "REGULARITY_U=" << (pass ? "NO_VIOLATION_INSIDE_S5" : "VIOLATED") << '\n';
    return pass ? 0 : 4;
}
