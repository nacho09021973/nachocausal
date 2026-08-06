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

int main(int argc, char** argv) {
    const bool run_pairs = argc == 2 && std::string(argv[1]) == "--run-pairs";
    const auto posets = unlabeled_posets6();
    const auto halves = rooted_halves(posets);
    std::size_t chain = 0;
    for (const auto& h : halves) chain += h.chain_x;

    std::cout << "UNLABELED_POSETS_N6=" << posets.size() << '\n';
    std::cout << "ROOTED_HALVES=" << halves.size() << '\n';
    std::cout << "ROOTED_CHAIN_X=" << chain << '\n';
    std::cout << "ROOTED_ANTICHAIN_X=" << halves.size() - chain << '\n';
    if (!run_pairs) return posets.size() == 318 ? 0 : 2;

    std::unordered_map<Code, Code> canon_cache;
    std::uint64_t pairs_tested = 0;
    std::uint64_t high_candidates = 0;
    std::uint64_t witness_pairs = 0;
    std::uint64_t witness_pairs_height4 = 0;
    std::array<std::uint64_t, 11> internal_reduction_sizes{};
    std::unordered_map<std::array<Code, 3>, GammaStats, GammaHash> all_gammas;
    std::unordered_map<std::array<Code, 3>, GammaStats, GammaHash> high_gammas;

    for (const auto& a : halves) {
        for (const auto& c : halves) {
            if (a.chain_x != c.chain_x) continue;
            if (a.unrooted == c.unrooted) continue;
            ++pairs_tested;
            const Poset10 q = amalgamate(a, c);
            if (!is_strict_poset10(q) || !is_downset10(q, 0b0000111111u)
                    || !is_downset10(q, 0b1111000011u)) {
                std::cerr << "AMALGAM_INVARIANT_FAILURE\n";
                return 3;
            }
            const int h = height10(q);
            if (h >= 4) ++high_candidates;

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
            std::array<Code, 3> gamma{};
            std::copy(types.begin(), types.end(), gamma.begin());
            int smallest_internal = 11;
            for (unsigned r = 0; r < (1u << 10); ++r) {
                const int size = __builtin_popcount(r);
                if (size < 6 || size >= smallest_internal || size >= 10
                        || !is_downset10(q, r)) continue;
                std::set<Code> subtypes;
                for (const auto& [s, type] : downsets6) {
                    if ((s & r) == s) subtypes.insert(type);
                }
                if (subtypes == types) smallest_internal = size;
            }
            const bool internally_reducible = smallest_internal <= 9;
            auto update_stats = [&](GammaStats& stats) {
                ++stats.representations;
                stats.internally_reducible += internally_reducible;
                stats.largest_smallest_internal = std::max(
                    stats.largest_smallest_internal, internally_reducible ? smallest_internal : 10);
                if (stats.representations == 1 || h < stats.height) {
                    stats.representative = q;
                    stats.height = h;
                }
            };
            update_stats(all_gammas[gamma]);
            if (h >= 4) {
                ++witness_pairs_height4;
                if (internally_reducible) ++internal_reduction_sizes[smallest_internal];
                update_stats(high_gammas[gamma]);
            }
        }
    }

    std::cout << "PAIRS_TESTED=" << pairs_tested << '\n';
    std::cout << "HEIGHT_GE_4_PAIRS=" << high_candidates << '\n';
    std::cout << "WITNESS_PAIRS=" << witness_pairs << '\n';
    std::cout << "WITNESS_PAIRS_HEIGHT_GE_4=" << witness_pairs_height4 << '\n';
    // Deterministic ordering: unordered_map iteration order is unspecified, so
    // every listing below is emitted from a sorted vector.
    auto sorted_by_gamma = [](const auto& table) {
        std::vector<std::pair<std::array<Code, 3>, GammaStats>> out(table.begin(), table.end());
        std::sort(out.begin(), out.end(), [](const auto& lhs, const auto& rhs) {
            return lhs.first < rhs.first;
        });
        return out;
    };
    const auto all_sorted = sorted_by_gamma(all_gammas);
    const auto high_sorted = sorted_by_gamma(high_gammas);

    auto print_node = [](const char* tag, const std::array<Code, 3>& gamma,
                         const GammaStats& stats) {
        std::cout << tag << " GAMMA=" << gamma[0] << ',' << gamma[1] << ',' << gamma[2]
                  << " REPRESENTATIONS=" << stats.representations
                  << " REDUCIBLE=" << stats.internally_reducible
                  << " MIN_HEIGHT=" << stats.height
                  << " LARGEST_SMALLEST_INTERNAL=" << stats.largest_smallest_internal
                  << " Q_ROWS=";
        for (int i = 0; i < 10; ++i) {
            if (i) std::cout << ',';
            std::cout << stats.representative.successors[i];
        }
        std::cout << '\n';
    };

    // Existential aggregation over ALL heights: this is the statement of record.
    std::uint64_t all_closed = 0;
    std::uint64_t all_zero_reducible = 0;
    std::uint64_t all_partial = 0;
    for (const auto& [_, stats] : all_sorted) {
        all_closed += stats.internally_reducible >= 1;
        all_zero_reducible += stats.internally_reducible == 0;
        all_partial += stats.internally_reducible >= 1
                    && stats.internally_reducible < stats.representations;
    }
    std::cout << "UNIQUE_GAMMAS_ALL_HEIGHTS=" << all_gammas.size() << '\n';
    std::cout << "ALL_HEIGHT_GAMMAS_CLOSED_EXISTENTIALLY=" << all_closed << '\n';
    std::cout << "ALL_HEIGHT_GAMMAS_WITH_ZERO_REDUCIBLE_REPRESENTATIONS="
              << all_zero_reducible << '\n';
    std::cout << "ALL_HEIGHT_GAMMAS_PARTIALLY_REDUCIBLE=" << all_partial << '\n';

    // Height >= 4 slice: the range left open by the authors' reported search.
    std::uint64_t high_closed = 0;
    std::uint64_t high_zero_reducible = 0;
    for (const auto& [_, stats] : high_sorted) {
        high_closed += stats.internally_reducible >= 1;
        high_zero_reducible += stats.internally_reducible == 0;
    }
    std::cout << "UNIQUE_GAMMAS_HEIGHT_GE_4=" << high_gammas.size() << '\n';
    std::cout << "HEIGHT_GE_4_GAMMAS_CLOSED_EXISTENTIALLY=" << high_closed << '\n';
    std::cout << "HEIGHT_GE_4_GAMMAS_WITH_ZERO_REDUCIBLE_REPRESENTATIONS="
              << high_zero_reducible << '\n';

    // Histogram is over height >= 4 representations only (see the accumulator).
    for (int size = 6; size <= 10; ++size) {
        std::cout << "HEIGHT_GE_4_REPRESENTATIONS_SMALLEST_INTERNAL_" << size << '='
                  << internal_reduction_sizes[size] << '\n';
    }

    // The three partially reducible nodes: closed, but carrying size-10
    // representations that are minimal under inclusion without being smallest.
    for (const auto& [gamma, stats] : all_sorted) {
        if (stats.internally_reducible == 0) continue;
        if (stats.internally_reducible == stats.representations) continue;
        print_node("ALLH_PARTIAL", gamma, stats);
    }

    // The only possible counterexamples: nodes with no reducible representation.
    for (const auto& [gamma, stats] : all_sorted) {
        if (stats.internally_reducible != 0) continue;
        print_node("SURVIVOR", gamma, stats);
    }

    const bool pass = all_zero_reducible == 0;
    std::cout << "N6_K3_N_PLUS_3="
              << (pass ? "PASS_EVERY_GAMMA6_HAS_WITNESS_LE_9" : "FAIL_SURVIVOR") << '\n';
    return pass ? 0 : 4;
}
