#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

constexpr double R_S = 0.5;
constexpr double TWO_M = 0.5;
constexpr double POOLED_SD_FLOOR = 0.5;
constexpr double EPS = 1e-12;

struct Point {
    double t;
    double r;
};

struct Split {
    double thr;
    double sep;
};

struct Bracket {
    bool valid;
    double r_lo;
    double r_hi;
    double width;
    double midpoint;
    bool covers;
    bool clean;
};

struct KindMetrics {
    int n_min;
    double improvement;
    double thr;
    double sep;
    Bracket bracket;
};

double mean(const std::vector<double>& v, int begin, int end) {
    if (end <= begin) {
        return std::numeric_limits<double>::quiet_NaN();
    }
    double s = 0.0;
    for (int i = begin; i < end; ++i) {
        s += v[i];
    }
    return s / static_cast<double>(end - begin);
}

double var_times_n(const std::vector<double>& v, int begin, int end) {
    if (end <= begin) {
        return 0.0;
    }
    const double m = mean(v, begin, end);
    double s = 0.0;
    for (int i = begin; i < end; ++i) {
        const double d = v[i] - m;
        s += d * d;
    }
    return s;
}

Split two_means_split(std::vector<double> values) {
    std::sort(values.begin(), values.end());
    const int n = static_cast<int>(values.size());
    if (n < 2) {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        return {nan, nan};
    }
    int best_i = 1;
    double best_sse = std::numeric_limits<double>::infinity();
    for (int i = 1; i < n; ++i) {
        const double sse = var_times_n(values, 0, i) + var_times_n(values, i, n);
        if (sse < best_sse) {
            best_sse = sse;
            best_i = i;
        }
    }
    const double mu_lo = mean(values, 0, best_i);
    const double mu_hi = mean(values, best_i, n);
    const double thr = 0.5 * (values[best_i - 1] + values[best_i]);
    double pooled = std::sqrt(best_sse / static_cast<double>(n));
    pooled = std::max(pooled, POOLED_SD_FLOOR);
    return {thr, std::abs(mu_hi - mu_lo) / pooled};
}

double improvement(std::vector<double> values) {
    std::sort(values.begin(), values.end());
    const int n = static_cast<int>(values.size());
    if (n < 2) {
        return 0.0;
    }
    const double total = var_times_n(values, 0, n);
    if (total <= 0.0) {
        return 0.0;
    }
    double best_sse = std::numeric_limits<double>::infinity();
    for (int i = 1; i < n; ++i) {
        const double sse = var_times_n(values, 0, i) + var_times_n(values, i, n);
        best_sse = std::min(best_sse, sse);
    }
    return 1.0 - best_sse / total;
}

bool causal_mink_past(const Point& earlier, const Point& later) {
    const double dt = later.t - earlier.t;
    return (dt > 0.0) && (dt >= std::abs(later.r - earlier.r) - EPS);
}

double bh_func(double r) {
    return r + 2.0 * R_S * std::log(std::abs(r - R_S) / R_S);
}

bool causal_bh_past(const Point& earlier, const Point& later, double f_earlier, double f_later) {
    if (!(earlier.t < later.t)) {
        return false;
    }
    const double dt = later.t - earlier.t;
    const double ri = later.r;
    const double rj = earlier.r;
    const double t_out = f_later - f_earlier;
    const double t_in = rj - ri;
    const bool b1 = (ri <= rj) && (rj <= R_S);
    const bool b2 = (rj >= R_S) && (rj >= ri);
    const bool b3 = (rj >= R_S) && (rj <= ri);
    if (b1) {
        return (t_out >= dt) && (dt >= t_in);
    }
    if (b2) {
        return dt >= t_in;
    }
    if (b3) {
        return dt >= t_out;
    }
    return false;
}

Bracket score_bracket(
    const std::vector<int>& minimal,
    const std::vector<int>& future_count,
    const std::vector<Point>& points,
    double thr
) {
    std::vector<double> lo_r;
    std::vector<double> hi_r;
    for (int idx : minimal) {
        if (static_cast<double>(future_count[idx]) < thr) {
            lo_r.push_back(points[idx].r);
        } else {
            hi_r.push_back(points[idx].r);
        }
    }
    const double nan = std::numeric_limits<double>::quiet_NaN();
    if (lo_r.empty() || hi_r.empty()) {
        return {false, nan, nan, nan, nan, false, false};
    }
    const double r_lo = *std::max_element(lo_r.begin(), lo_r.end());
    const double r_hi = *std::min_element(hi_r.begin(), hi_r.end());
    const double width = r_hi - r_lo;
    const bool covers = (r_lo <= R_S) && (R_S <= r_hi);
    return {true, r_lo, r_hi, width, 0.5 * (r_lo + r_hi), covers, width >= 0.0};
}

KindMetrics compute_kind(const std::vector<Point>& points, const std::string& kind) {
    const int n = static_cast<int>(points.size());
    std::vector<char> has_past(n, 0);
    std::vector<int> future_count(n, 0);
    std::vector<double> f;
    if (kind == "BH") {
        f.resize(n);
        for (int i = 0; i < n; ++i) {
            f[i] = bh_func(points[i].r);
        }
    }

    std::vector<int> by_t(n);
    std::iota(by_t.begin(), by_t.end(), 0);
    std::sort(by_t.begin(), by_t.end(), [&](int a, int b) {
        return points[a].t < points[b].t;
    });

    for (int aa = 0; aa < n; ++aa) {
        const int earlier = by_t[aa];
        for (int bb = aa + 1; bb < n; ++bb) {
            const int later = by_t[bb];
            bool related = false;
            if (kind == "MINK") {
                related = causal_mink_past(points[earlier], points[later]);
            } else if (kind == "BH") {
                related = causal_bh_past(points[earlier], points[later], f[earlier], f[later]);
            } else {
                throw std::runtime_error("unknown kind");
            }
            if (related) {
                has_past[later] = 1;
                future_count[earlier] += 1;
            }
        }
    }

    std::vector<int> minimal;
    std::vector<double> values;
    for (int i = 0; i < n; ++i) {
        if (!has_past[i]) {
            minimal.push_back(i);
            values.push_back(static_cast<double>(future_count[i]));
        }
    }

    const Split split = two_means_split(values);
    const double imp = improvement(values);
    Bracket br = {false,
                  std::numeric_limits<double>::quiet_NaN(),
                  std::numeric_limits<double>::quiet_NaN(),
                  std::numeric_limits<double>::quiet_NaN(),
                  std::numeric_limits<double>::quiet_NaN(),
                  false,
                  false};
    if (kind == "BH") {
        br = score_bracket(minimal, future_count, points, split.thr);
    }
    return {static_cast<int>(minimal.size()), imp, split.thr, split.sep, br};
}

void print_json_number(double x) {
    if (std::isfinite(x)) {
        std::cout << std::setprecision(17) << x;
    } else {
        std::cout << "null";
    }
}

void print_kind(const std::string& name, const KindMetrics& m, bool with_bracket) {
    std::cout << "\"" << name << "\":{";
    std::cout << "\"n_min\":" << m.n_min << ",";
    std::cout << "\"improvement\":";
    print_json_number(m.improvement);
    std::cout << ",\"thr\":";
    print_json_number(m.thr);
    std::cout << ",\"sep\":";
    print_json_number(m.sep);
    if (with_bracket) {
        std::cout << ",\"bracket\":{";
        std::cout << "\"valid\":" << (m.bracket.valid ? "true" : "false") << ",";
        std::cout << "\"r_lo\":";
        print_json_number(m.bracket.r_lo);
        std::cout << ",\"r_hi\":";
        print_json_number(m.bracket.r_hi);
        std::cout << ",\"width\":";
        print_json_number(m.bracket.width);
        std::cout << ",\"midpoint\":";
        print_json_number(m.bracket.midpoint);
        std::cout << ",\"covers\":" << (m.bracket.covers ? "true" : "false") << ",";
        std::cout << "\"clean\":" << (m.bracket.clean ? "true" : "false") << "}";
    }
    std::cout << "}";
}

}  // namespace

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n = 0;
    if (!(std::cin >> n)) {
        std::cerr << "expected N followed by N lines of t r\n";
        return 2;
    }
    std::vector<Point> points(n);
    for (int i = 0; i < n; ++i) {
        if (!(std::cin >> points[i].t >> points[i].r)) {
            std::cerr << "expected coordinate line " << i << "\n";
            return 2;
        }
    }

    try {
        const KindMetrics bh = compute_kind(points, "BH");
        const KindMetrics mk = compute_kind(points, "MINK");
        std::cout << "{\"N\":" << n << ",";
        print_kind("BH", bh, true);
        std::cout << ",";
        print_kind("MINK", mk, false);
        std::cout << "}\n";
    } catch (const std::exception& exc) {
        std::cerr << exc.what() << "\n";
        return 1;
    }
    return 0;
}
