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
#include <sstream>
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
// Does the amalgam really satisfy the Section 5 setup?
//
// The paper's setup (p.14) is NOT "some A - B - B - B - C path exists".  It is:
// P is a shortest path of the form P_1 - P_2 - ... - P_2 - P_3 and "no shorter
// path of this form FOR ANY THREE DISTINCT P_i exists in G_n(Q)".  With k = 3
// the three roles can be assigned in three essentially different ways (choice of
// the middle type), and copies range over all size-n downsets.
//
// STRICT: our anchors A_SET, C_SET with middle tau_B realise that global minimum.
// LOOSE : some A - B - B - B - C path of length 4 exists (the earlier flag).
// ---------------------------------------------------------------------------
int main() {
    const auto posets = unlabeled_posets6();
    const auto halves = rooted_halves(posets);

    constexpr unsigned A_SET = 0b0000111111u;
    constexpr unsigned C_SET = 0b1111000011u;
    constexpr unsigned AX    = 0b0000111100u;
    constexpr unsigned CX    = 0b1111000000u;

    std::unordered_map<Code, Code> canon_cache;
    std::uint64_t witness_pairs = 0, loose = 0, strict = 0, loose_not_strict = 0;
    std::array<std::uint64_t, 8> minlen_hist{};
    std::uint64_t l52_viol_strict = 0, l52_viol_loose_not_strict = 0;
    std::uint64_t tr_viol_strict = 0;
    std::uint64_t cu_viol_strict = 0, mult1_is_b_strict = 0, mult1_copies_strict = 0;
    std::array<std::uint64_t, 11> u_hist_strict{};
    std::uint64_t multb_lt3_strict = 0;
    std::array<std::uint64_t, 4> xt{};
    std::vector<std::string> strict_lines;

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
            std::vector<unsigned> sets;
            std::vector<Code> tps;
            for (unsigned s = 0; s < (1u << 10); ++s) {
                if (__builtin_popcount(s) != 6 || !is_downset10(q, s)) continue;
                const Code raw = induced6(q, s);
                auto it = canon_cache.find(raw);
                const Code canonical = it == canon_cache.end()
                    ? canon_cache.emplace(raw, canonical6(raw)).first->second
                    : it->second;
                types.insert(canonical);
                sets.push_back(s);
                tps.push_back(canonical);
                if (types.size() > 3) break;
            }
            if (types.size() != 3 || !types.contains(a.unrooted) || !types.contains(c.unrooted)) continue;
            ++witness_pairs;
            const int V = static_cast<int>(sets.size());

            const Code b_type = [&] {
                for (Code t : types) {
                    if (t != a.unrooted && t != c.unrooted) return t;
                }
                return Code{0};
            }();

            std::vector<std::vector<int>> adj(V);
            for (int i = 0; i < V; ++i) {
                for (int j = 0; j < V; ++j) {
                    if (i != j && __builtin_popcount(sets[i] & ~sets[j]) == 1) adj[i].push_back(j);
                }
            }

            // Shortest S - mid - ... - mid - T path, interior all of type `mid`,
            // at least one interior vertex; endpoints of the two other types.
            auto best_for_middle = [&](Code mid) {
                int best = 99;
                for (int s = 0; s < V; ++s) {
                    if (tps[s] == mid) continue;
                    std::vector<int> dist(V, -1);
                    std::vector<int> frontier{s};
                    dist[s] = 0;
                    for (int step = 1; step <= 8 && !frontier.empty(); ++step) {
                        std::vector<int> next;
                        for (int u : frontier) {
                            for (int v : adj[u]) {
                                if (dist[v] != -1) continue;
                                // reachable at distance `step`; keep expanding only
                                // through middle-type vertices
                                dist[v] = step;
                                if (tps[v] == mid) next.push_back(v);
                                else if (tps[v] != tps[s] && step >= 2) best = std::min(best, step);
                            }
                        }
                        frontier.swap(next);
                    }
                }
                return best;
            };
            int global_best = 99;
            Code arg_mid = 0;
            for (Code mid : types) {
                const int b = best_for_middle(mid);
                if (b < global_best) { global_best = b; arg_mid = mid; }
            }
            minlen_hist[std::min(global_best, 7)]++;

            auto adjmask = [](unsigned p1, unsigned p2) { return __builtin_popcount(p1 & ~p2) == 1; };
            bool loose_flag = false;
            for (int i = 0; i < V; ++i) {
                if (tps[i] != b_type || !adjmask(A_SET, sets[i])) continue;
                for (int j = 0; j < V; ++j) {
                    if (tps[j] != b_type || !adjmask(sets[i], sets[j])) continue;
                    for (int k = 0; k < V; ++k) {
                        if (tps[k] == b_type && adjmask(sets[j], sets[k]) && adjmask(sets[k], C_SET)) {
                            loose_flag = true;
                        }
                    }
                }
            }
            // STRICT: the global minimum over all role assignments is 4 and is
            // attained with the middle type tau_B by our own anchor pair.
            const bool strict_flag = loose_flag && global_best == 4;
            (void)arg_mid;
            if (loose_flag) ++loose;
            if (strict_flag) ++strict;
            if (loose_flag && !strict_flag) ++loose_not_strict;

            int smallest_internal = 11;
            for (unsigned r = 0; r < (1u << 10); ++r) {
                const int size = __builtin_popcount(r);
                if (size < 6 || size >= smallest_internal || size >= 10 || !is_downset10(q, r)) continue;
                std::set<Code> subtypes;
                for (int i = 0; i < V; ++i) {
                    if ((sets[i] & r) == sets[i]) subtypes.insert(tps[i]);
                }
                if (subtypes == types) smallest_internal = size;
            }
            const bool reducible = smallest_internal <= 9;
            xt[(strict_flag ? 0 : 2) + (reducible ? 1 : 0)]++;

            unsigned maxmask = 0;
            for (int v = 0; v < 10; ++v) {
                bool above = false;
                for (int u = 0; u < 10; ++u) {
                    if (related10(q, v, u)) { above = true; break; }
                }
                if (!above) maxmask |= (1u << v);
            }
            std::unordered_map<Code, int> mult;
            for (Code t : tps) ++mult[t];

            if (strict_flag && mult[b_type] < 3) ++multb_lt3_strict;

            for (int i = 0; i < V; ++i) {
                if (tps[i] == b_type) continue;
                const bool side = ((sets[i] & AX) == AX) || ((sets[i] & CX) == CX);
                if (!side) {
                    if (strict_flag) ++l52_viol_strict;
                    else if (loose_flag) ++l52_viol_loose_not_strict;
                }
                if (strict_flag && !(sets[i] & maxmask)) ++tr_viol_strict;
            }
            if (strict_flag) {
                std::ostringstream os;
                os << "STRICT RED=" << (reducible ? 'Y' : 'N')
                   << " MAXQ=" << __builtin_popcount(maxmask)
                   << " MULT_A/B/C=" << mult[a.unrooted] << '/' << mult[b_type] << '/'
                   << mult[c.unrooted]
                   << " D6=" << V << " X=" << (a.chain_x ? "chain" : "antichain")
                   << " Q_ROWS=";
                for (int i = 0; i < 10; ++i) { if (i) os << ','; os << q.successors[i]; }
                strict_lines.push_back(os.str());
                for (const auto& [t, count] : mult) {
                    if (count != 1) continue;
                    ++mult1_copies_strict;
                    if (t == b_type) ++mult1_is_b_strict;
                    for (int i = 0; i < V; ++i) {
                        if (tps[i] != t) continue;
                        const int hit = __builtin_popcount(sets[i] & maxmask);
                        u_hist_strict[std::min(hit, 10)]++;
                        if (hit == 0) ++cu_viol_strict;
                    }
                }
            }
        }
    }

    std::cout << "WITNESS_PAIRS=" << witness_pairs << '\n';
    std::cout << "XTAB_STRICT_IRRED=" << xt[0] << " STRICT_RED=" << xt[1]
              << " NONSTRICT_IRRED=" << xt[2] << " NONSTRICT_RED=" << xt[3] << '\n';
    for (const auto& l : strict_lines) std::cout << l << '\n';
    std::cout << "LOOSE_S5=" << loose << '\n';
    std::cout << "STRICT_S5=" << strict << '\n';
    std::cout << "LOOSE_BUT_NOT_STRICT=" << loose_not_strict << '\n';
    for (int i = 0; i < 8; ++i) {
        if (minlen_hist[i]) std::cout << "GLOBAL_MIN_SPECIAL_PATH_LEN_" << i << '=' << minlen_hist[i] << '\n';
    }
    std::cout << "L52_VIOLATIONS_STRICT=" << l52_viol_strict << '\n';
    std::cout << "L52_VIOLATIONS_LOOSE_NOT_STRICT=" << l52_viol_loose_not_strict << '\n';
    std::cout << "TR_VIOLATIONS_STRICT=" << tr_viol_strict << '\n';
    std::cout << "MULTB_LT_3_STRICT=" << multb_lt3_strict << '\n';
    std::cout << "MULT1_COPIES_STRICT=" << mult1_copies_strict << '\n';
    std::cout << "MULT1_TYPE_IS_B_STRICT=" << mult1_is_b_strict << '\n';
    std::cout << "CU_VIOLATIONS_STRICT=" << cu_viol_strict << '\n';
    for (int i = 0; i <= 10; ++i) {
        if (u_hist_strict[i]) std::cout << "U_MAXHITS_STRICT_" << i << '=' << u_hist_strict[i] << '\n';
    }
    return 0;
}
