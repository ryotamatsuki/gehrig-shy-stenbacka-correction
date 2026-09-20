"""Stage-4 global-validity derivation and direct-payoff regression checks.

Target:
    Gehrig, Shy & Stenbacka (2011)

This script is intentionally separate from the Stage-1 welfare recheck.
It derives the normalized global-validity inequalities symbolically and then
uses a direct clipped-demand payoff evaluator to attack them numerically.

Normalization:
    tau = 1
    c_B = 0
    d = (c_A-c_B)/tau
    s = sigma/tau

The normalization is valid for the real-price game because only price-cost and
relative-price differences matter.  For nonnegative price strategy sets the
same profitable-deviation analysis applies whenever the displayed candidate
prices are feasible (in particular under nonnegative marginal costs).
"""

from __future__ import annotations

import math
import random
import sympy as sp


def clip(x: float) -> float:
    return max(0.0, min(1.0, x))


def displayed_candidates(theta: float, s: float, d: float):
    pa_d = 1 + ((2 + theta) * s + 4 * d) / 6
    qa_d = 1 + (4 * d - (1 - theta) * s) / 6
    pb = 1 + (d - (1 - theta) * s) / 3
    pa_u = 1 + (2 * d + (1 - theta) * s) / 3
    return pa_d, qa_d, pb, pa_u


def hbp_profit(pa: float, qa: float, pb: float, theta: float, s: float, d: float):
    xo = clip(0.5 + (s + pb - pa) / 2)
    xn = clip(0.5 + (pb - qa) / 2)
    pia = (1 - theta) * (pa - d) * xo + theta * (qa - d) * xn
    pib = pb * ((1 - theta) * (1 - xo) + theta * (1 - xn))
    return pia, pib


def uniform_profit(pa: float, pb: float, theta: float, s: float, d: float):
    xo = clip(0.5 + (s + pb - pa) / 2)
    xn = clip(0.5 + (pb - pa) / 2)
    pia = (pa - d) * ((1 - theta) * xo + theta * xn)
    pib = pb * ((1 - theta) * (1 - xo) + theta * (1 - xn))
    return pia, pib


def max_two_segment_common_price(cost: float, effective_rivals, weights):
    """Exact-by-branch candidate enumeration, evaluated in double precision.

    For a segment with effective rival price r, own demand is
        clip((1 + r - p)/2, 0, 1).
    In net markup z=p-cost, each branch is affine demand and profit is quadratic.
    Therefore a global maximizer must be a breakpoint or a branch vertex.
    """
    hs = [1 + r - cost for r in effective_rivals]  # zero-demand thresholds in z
    breakpoints = sorted(set([h - 2 for h in hs] + hs))

    candidates = {0.0}
    candidates.update(breakpoints)
    edges = [-math.inf] + breakpoints + [math.inf]

    for lo, hi in zip(edges[:-1], edges[1:]):
        if math.isinf(lo):
            rep = hi - 1.0
        elif math.isinf(hi):
            rep = lo + 1.0
        else:
            rep = (lo + hi) / 2.0

        A = 0.0
        B = 0.0
        for h, w in zip(hs, weights):
            raw = (h - rep) / 2.0
            if raw <= 0:
                continue
            if raw >= 1:
                A += w
            else:
                A += w * h / 2.0
                B += w / 2.0

        if B > 0:
            z = A / (2 * B)
            if (math.isinf(lo) or z >= lo - 1e-12) and (
                math.isinf(hi) or z <= hi + 1e-12
            ):
                candidates.add(z)

    def profit_z(z):
        demand = sum(w * clip((h - z) / 2.0) for h, w in zip(hs, weights))
        return z * demand

    return max((profit_z(z), z) for z in candidates if math.isfinite(z))


def symbolic_derivation():
    theta, s, d = sp.symbols("theta s d", positive=True, real=True)
    r = sp.sqrt(theta)
    q = sp.sqrt(1 - theta)

    pa_d = 1 + ((2 + theta) * s + 4 * d) / 6
    qa_d = 1 + (4 * d - (1 - theta) * s) / 6
    pb = 1 + (d - (1 - theta) * s) / 3
    pa_u = 1 + (2 * d + (1 - theta) * s) / 3

    # HBP entrant: high-threshold segment is new consumers, weight theta.
    hbd_old = sp.factor(pa_d - s + 1)
    hbd_new = sp.factor(qa_d + 1)
    hbd_bar = sp.factor((1 - theta) * hbd_old + theta * hbd_new)
    assert sp.simplify(hbd_bar - 2 * pb) == 0
    assert sp.simplify(hbd_new - hbd_bar - (1 - theta) * s / 2) == 0

    # Uniform incumbent: high-threshold segment is old consumers, weight 1-theta.
    hua_old = sp.factor(pb + s + 1 - d)
    hua_new = sp.factor(pb + 1 - d)
    hua_bar = sp.factor((1 - theta) * hua_old + theta * hua_new)
    assert sp.simplify(hua_bar - 2 * (pa_u - d)) == 0
    assert sp.simplify(hua_old - hua_bar - theta * s) == 0

    # Uniform entrant: high-threshold segment is new consumers, weight theta.
    hub_old = sp.factor(pa_u - s + 1)
    hub_new = sp.factor(pa_u + 1)
    hub_bar = sp.factor((1 - theta) * hub_old + theta * hub_new)
    assert sp.simplify(hub_bar - 2 * pb) == 0
    assert sp.simplify(hub_new - hub_bar - (1 - theta) * s) == 0

    # Closed-form global-validity thresholds.
    L_hbp = sp.factor(-3 + (4 - theta + 3 * r) * s / 4)
    U_hbp = sp.factor(3 - (1 - theta) * s / 2)

    L_u = sp.factor(-3 + (2 + theta + 3 * r) * s / 2)
    U_u = sp.factor(3 - (1 - theta + 3 * q) * s / 2)

    # The common-price lemma condition is hbar >= sqrt(weight)*h_high.
    # Verify that its equality solves exactly at the proposed thresholds.
    assert sp.simplify(
        hbd_bar.subs(d, L_hbp) - r * hbd_new.subs(d, L_hbp)
    ) == 0
    assert sp.simplify(
        hub_bar.subs(d, L_u) - r * hub_new.subs(d, L_u)
    ) == 0
    assert sp.simplify(
        hua_bar.subs(d, U_u) - q * hua_old.subs(d, U_u)
    ) == 0

    # Uniform validity is strictly more restrictive than HBP for 0<theta<1,s>0.
    assert sp.factor(L_u - L_hbp) == 3 * s * (theta + r) / 4
    assert sp.factor(U_hbp - U_u) == 3 * s * q / 2

    # Nonempty-domain bounds.
    smax_hbp = sp.factor(8 / (2 - theta + r))
    smax_u = sp.factor(4 / (1 + r + q))
    assert sp.simplify((L_hbp - U_hbp).subs(s, smax_hbp)) == 0
    assert sp.simplify((L_u - U_u).subs(s, smax_u)) == 0

    print("SYMBOLIC PASS")
    print("D_HBP lower =", L_hbp)
    print("D_HBP upper =", U_hbp)
    print("D_U lower =", L_u)
    print("D_U upper =", U_u)
    print("smax_HBP =", smax_hbp)
    print("smax_U =", smax_u)


def exact_regression_examples():
    # Stage-1 HBP counterexample.
    th = sp.Rational(1, 2)
    s = sp.Rational(23, 10)
    d = sp.Rational(0)
    pa = 1 + ((2 + th) * s + 4 * d) / 6
    qa = 1 + (4 * d - (1 - th) * s) / 6
    pb = 1 + (d - (1 - th) * s) / 3
    xo = sp.Rational(1, 2) + (s + pb - pa) / 2
    xn = sp.Rational(1, 2) + (pb - qa) / 2
    cand = sp.factor(pb * ((1 - th) * (1 - xo) + th * (1 - xn)))
    dev = sp.factor((qa + 1) / 2)
    yn_dev = sp.factor((1 + qa - dev) / 2)
    devpi = sp.factor(dev * th * yn_dev)
    assert sp.factor(devpi - cand) == sp.Rational(3281, 230400)

    # Uniform-pricing entrant failure: new-only high-price deviation.
    th = sp.Rational(1, 2)
    s = sp.Rational(1)
    d = sp.Rational(-4, 5)
    pa = 1 + (2 * d + (1 - th) * s) / 3
    pb = 1 + (d - (1 - th) * s) / 3
    xo = sp.Rational(1, 2) + ((2 * th + 1) * s - d) / 6
    xn = sp.Rational(1, 2) - (d + 2 * (1 - th) * s) / 6
    pib = sp.factor(pb * ((1 - th) * (1 - xo) + th * (1 - xn)))
    pb_dev = sp.factor((pa + 1) / 2)
    yn = sp.factor((1 + pa - pb_dev) / 2)
    pib_dev = sp.factor(pb_dev * th * yn)
    assert pib_dev - pib == sp.Rational(89, 14400)

    # Uniform-pricing incumbent failure: old-only high-price deviation.
    d = sp.Rational(9, 5)
    pa = 1 + (2 * d + (1 - th) * s) / 3
    pb = 1 + (d - (1 - th) * s) / 3
    xo = sp.Rational(1, 2) + ((2 * th + 1) * s - d) / 6
    xn = sp.Rational(1, 2) - (d + 2 * (1 - th) * s) / 6
    pia = sp.factor((pa - d) * ((1 - th) * xo + th * xn))
    z_dev = sp.factor((pb + s + 1 - d) / 2)
    pa_dev = sp.factor(d + z_dev)
    xo_dev = sp.factor((1 + s + pb - pa_dev) / 2)
    pia_dev = sp.factor(z_dev * (1 - th) * xo_dev)
    assert pia_dev - pia == sp.Rational(89, 14400)

    print("EXACT REGRESSION PASS")


def randomized_direct_attack():
    rng = random.Random(20260920)

    # Attack the claimed common domain from inside.
    for _ in range(20000):
        theta = rng.uniform(0.01, 0.99)
        s = rng.uniform(0.0, 2.0)
        L = -3 + (2 + theta + 3 * math.sqrt(theta)) * s / 2
        U = 3 - (1 - theta + 3 * math.sqrt(1 - theta)) * s / 2
        if L > U:
            continue
        d = rng.uniform(L, U)
        pa_d, qa_d, pb, pa_u = displayed_candidates(theta, s, d)

        pia_d, pib_d = hbp_profit(pa_d, qa_d, pb, theta, s, d)
        # HBP entrant: effective rival prices are pa_d-s (old) and qa_d (new).
        max_b_d = max_two_segment_common_price(
            0.0, [pa_d - s, qa_d], [1 - theta, theta]
        )
        assert max_b_d[0] <= pib_d + 1e-9

        pia_u, pib_u = uniform_profit(pa_u, pb, theta, s, d)
        # Uniform A: effective rival prices pb+s (old) and pb (new).
        max_a_u = max_two_segment_common_price(
            d, [pb + s, pb], [1 - theta, theta]
        )
        # Uniform B: effective rival prices pa_u-s (old) and pa_u (new).
        max_b_u = max_two_segment_common_price(
            0.0, [pa_u - s, pa_u], [1 - theta, theta]
        )
        assert max_a_u[0] <= pia_u + 1e-9
        assert max_b_u[0] <= pib_u + 1e-9

    # Necessity attack inside the ordinary uniform-interior region.
    for _ in range(20000):
        theta = rng.uniform(0.01, 0.99)
        s = rng.uniform(0.0, 1.99)
        Li = (1 + 2 * theta) * s - 3
        Ui = 3 - 2 * (1 - theta) * s
        if Li > Ui:
            continue
        d = rng.uniform(Li, Ui)

        pa_d, qa_d, pb, pa_u = displayed_candidates(theta, s, d)
        pia_u, pib_u = uniform_profit(pa_u, pb, theta, s, d)
        max_a_u = max_two_segment_common_price(
            d, [pb + s, pb], [1 - theta, theta]
        )
        max_b_u = max_two_segment_common_price(
            0.0, [pa_u - s, pa_u], [1 - theta, theta]
        )
        direct_valid = (
            max_a_u[0] <= pia_u + 1e-9 and max_b_u[0] <= pib_u + 1e-9
        )

        L = -3 + (2 + theta + 3 * math.sqrt(theta)) * s / 2
        U = 3 - (1 - theta + 3 * math.sqrt(1 - theta)) * s / 2
        formula_valid = L - 1e-10 <= d <= U + 1e-10
        assert direct_valid == formula_valid

    print("DIRECT-PAYOFF ATTACK PASS")


if __name__ == "__main__":
    symbolic_derivation()
    exact_regression_examples()
    randomized_direct_attack()
    print("STAGE 4 CHECKS PASS")
