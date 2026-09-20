"""Independent Stage-4A adversarial certification.

This file MUST NOT import or call code/stage04_global_validity.py.
It reconstructs payoffs directly from primitive clipped Hotelling demands,
enumerates all piecewise-quadratic branch candidates, and attacks the Stage-4
claims independently.

Canonical numerical normalization for attacks:
    tau = 1, c_B = 0, c_A = d, sigma = s.

Analytical identities remain mapped back to arbitrary tau > 0.
"""

from __future__ import annotations

import math
import random
import sympy as sp


TOL = 1e-9
SEED = 40420260920


def clip(x: float) -> float:
    return 0.0 if x < 0.0 else 1.0 if x > 1.0 else x


# ---------------------------------------------------------------------------
# Primitive payoff reconstruction
# ---------------------------------------------------------------------------

def hbp_payoffs(pa, qa, pb, theta, s, d):
    xo = clip(0.5 + (s + pb - pa) / 2.0)
    xn = clip(0.5 + (pb - qa) / 2.0)
    pia = (1.0 - theta) * (pa - d) * xo + theta * (qa - d) * xn
    pib = pb * ((1.0 - theta) * (1.0 - xo) + theta * (1.0 - xn))
    return pia, pib


def uniform_payoffs(pa, pb, theta, s, d):
    xo = clip(0.5 + (s + pb - pa) / 2.0)
    xn = clip(0.5 + (pb - pa) / 2.0)
    pia = (pa - d) * ((1.0 - theta) * xo + theta * xn)
    pib = pb * ((1.0 - theta) * (1.0 - xo) + theta * (1.0 - xn))
    return pia, pib


# ---------------------------------------------------------------------------
# Clean-room global maximizer for weighted clipped affine demand
# ---------------------------------------------------------------------------

def global_common_price_br(cost, effective_rivals, weights):
    """Return all global best-response prices by exhaustive branch enumeration.

    Demand in segment i is reconstructed as
        clip((1 + r_i - p)/2)
    after tau=1 normalization.

    Candidate maxima are obtained from every breakpoint and every feasible
    quadratic-branch vertex.  This implementation does not use any Stage-4
    threshold formula.
    """
    hs = [1.0 + r - cost for r in effective_rivals]
    bps = sorted(set([h - 2.0 for h in hs] + hs))
    edges = [-math.inf] + bps + [math.inf]
    candidates = set(bps)
    candidates.add(0.0)  # zero markup benchmark

    for lo, hi in zip(edges[:-1], edges[1:]):
        if math.isinf(lo):
            rep = hi - 1.0
        elif math.isinf(hi):
            rep = lo + 1.0
        else:
            rep = 0.5 * (lo + hi)

        intercept = 0.0
        slope = 0.0
        for h, w in zip(hs, weights):
            raw = 0.5 * (h - rep)
            if raw <= 0.0:
                continue
            if raw >= 1.0:
                intercept += w
            else:
                intercept += 0.5 * w * h
                slope += 0.5 * w

        # Profit is z*(intercept - slope*z).
        if slope > 0.0:
            z = intercept / (2.0 * slope)
            if (math.isinf(lo) or z >= lo - TOL) and (
                math.isinf(hi) or z <= hi + TOL
            ):
                candidates.add(z)

    def profit(z):
        q = sum(
            w * clip(0.5 * (h - z))
            for h, w in zip(hs, weights)
        )
        return z * q

    scored = [(profit(z), z) for z in candidates if math.isfinite(z)]
    best = max(v for v, _ in scored)
    zs = sorted(z for v, z in scored if abs(v - best) <= 2e-9)
    return [cost + z for z in zs], best


# ---------------------------------------------------------------------------
# Displayed candidates, reconstructed independently
# ---------------------------------------------------------------------------

def displayed_hbp(theta, s, d):
    pa = 1.0 + ((2.0 + theta) * s + 4.0 * d) / 6.0
    qa = 1.0 + (4.0 * d - (1.0 - theta) * s) / 6.0
    pb = 1.0 + (d - (1.0 - theta) * s) / 3.0
    return pa, qa, pb


def displayed_uniform(theta, s, d):
    pa = 1.0 + (2.0 * d + (1.0 - theta) * s) / 3.0
    pb = 1.0 + (d - (1.0 - theta) * s) / 3.0
    return pa, pb


# ---------------------------------------------------------------------------
# Exact symbolic clean-room derivation
# ---------------------------------------------------------------------------

def exact_symbolic_attack():
    th = sp.symbols("theta", positive=True)
    s = sp.symbols("s", nonnegative=True)
    d = sp.symbols("d", real=True)
    one = sp.Integer(1)

    pa_d = one + ((2 + th) * s + 4 * d) / 6
    qa_d = one + (4 * d - (1 - th) * s) / 6
    pb = one + (d - (1 - th) * s) / 3
    pa_u = one + (2 * d + (1 - th) * s) / 3

    # HBP incumbent: two independent one-segment problems.
    h_A_old = sp.factor(one + pb + s - d)
    h_A_new = sp.factor(one + pb - d)

    # HBP entrant: direct primitive effective thresholds.
    h_B_old_d = sp.factor(one + pa_d - s)
    h_B_new_d = sp.factor(one + qa_d)
    H_B_d = sp.factor((1 - th) * h_B_old_d + th * h_B_new_d)

    # Uniform incumbent and entrant thresholds.
    h_A_old_u = sp.factor(one + pb + s - d)
    h_A_new_u = sp.factor(one + pb - d)
    H_A_u = sp.factor((1 - th) * h_A_old_u + th * h_A_new_u)

    h_B_old_u = sp.factor(one + pa_u - s)
    h_B_new_u = sp.factor(one + pa_u)
    H_B_u = sp.factor((1 - th) * h_B_old_u + th * h_B_new_u)

    # Verify that displayed net markups are the both-interior FOC vertices.
    assert sp.simplify(H_B_d / 2 - pb) == 0
    assert sp.simplify(H_A_u / 2 - (pa_u - d)) == 0
    assert sp.simplify(H_B_u / 2 - pb) == 0

    # Compare displayed common-price profit with the high-segment-only peak,
    # directly rather than importing the Stage-4 lemma.
    gap_HBP_B = sp.factor((H_B_d**2 - th * h_B_new_d**2) / 8)
    gap_U_B = sp.factor((H_B_u**2 - th * h_B_new_u**2) / 8)
    gap_U_A = sp.factor(
        (H_A_u**2 - (1 - th) * h_A_old_u**2) / 8
    )

    L_H = sp.factor(
        -3 + (4 - th + 3 * sp.sqrt(th)) * s / 4
    )
    U_H = sp.factor(3 - (1 - th) * s / 2)
    L_U = sp.factor(
        -3 + (2 + th + 3 * sp.sqrt(th)) * s / 2
    )
    U_U = sp.factor(
        3 - (1 - th + 3 * sp.sqrt(1 - th)) * s / 2
    )

    # Equality at the claimed global-deviation thresholds.
    assert sp.simplify(gap_HBP_B.subs(d, L_H)) == 0
    assert sp.simplify(gap_U_B.subs(d, L_U)) == 0
    assert sp.simplify(gap_U_A.subs(d, U_U)) == 0

    # Sign orientation: use linear factors after rationalization.
    # Equivalent no-deviation conditions on the positive regular branch.
    expr_H = sp.factor(H_B_d - sp.sqrt(th) * h_B_new_d)
    expr_UB = sp.factor(H_B_u - sp.sqrt(th) * h_B_new_u)
    expr_UA = sp.factor(
        H_A_u - sp.sqrt(1 - th) * h_A_old_u
    )
    assert sp.simplify(expr_H.subs(d, L_H)) == 0
    assert sp.simplify(expr_UB.subs(d, L_U)) == 0
    assert sp.simplify(expr_UA.subs(d, U_U)) == 0
    assert sp.simplify(sp.diff(expr_H, d)) > 0
    assert sp.simplify(sp.diff(expr_UB, d)) > 0
    assert sp.simplify(sp.diff(expr_UA, d)) < 0

    # HBP A's one-segment global-interior conditions:
    # 0 <= h <= 4.  Show that the B lower bound dominates the only material
    # lower A-bound, and U_H is the binding upper A-bound.
    A_old_lower = sp.factor(-3 + (2 + th) * s / 2)
    assert sp.factor(L_H - A_old_lower) == (
        3 * s * (sp.sqrt(th) - th) / 4
    )
    assert sp.simplify(h_A_new.subs(d, U_H)) == 0

    # Uniform globality strictly implies ordinary cohort interiority.
    uniform_interior_lower = sp.factor(-3 + (1 + 2 * th) * s)
    uniform_interior_upper = sp.factor(3 - 2 * (1 - th) * s)
    assert sp.factor(L_U - uniform_interior_lower) == (
        3 * s * (sp.sqrt(th) - th) / 2
    )
    assert sp.factor(uniform_interior_upper - U_U) == (
        3 * s * (sp.sqrt(1 - th) - (1 - th)) / 2
    )

    # Containment D_U subset D_HBP.
    assert sp.factor(L_U - L_H) == (
        3 * s * (th + sp.sqrt(th)) / 4
    )
    assert sp.factor(U_H - U_U) == (
        3 * s * sp.sqrt(1 - th) / 2
    )

    # Nonempty-domain thresholds.
    smax_H = sp.factor(8 / (2 - th + sp.sqrt(th)))
    smax_U = sp.factor(
        4 / (1 + sp.sqrt(th) + sp.sqrt(1 - th))
    )
    assert sp.simplify((L_H - U_H).subs(s, smax_H)) == 0
    assert sp.simplify((L_U - U_U).subs(s, smax_U)) == 0

    # Welfare identities reconstructed from primitive utility integrals.
    beta, x = sp.symbols("beta x", real=True)
    # Displayed shares.
    xo_d = sp.factor(sp.Rational(1, 2) + (s + pb - pa_d) / 2)
    xn_d = sp.factor(sp.Rational(1, 2) + (pb - qa_d) / 2)
    xo_u = sp.factor(sp.Rational(1, 2) + (s + pb - pa_u) / 2)
    xn_u = sp.factor(sp.Rational(1, 2) + (pb - pa_u) / 2)

    def cs(pa, qa, xo, xn):
        old = sp.integrate(beta - pa - x, (x, 0, xo))
        old += sp.integrate(beta - pb - (1 - x) - s, (x, xo, 1))
        new = sp.integrate(beta - qa - x, (x, 0, xn))
        new += sp.integrate(beta - pb - (1 - x), (x, xn, 1))
        return sp.factor((1 - th) * old + th * new)

    cs_d = cs(pa_d, qa_d, xo_d, xn_d)
    cs_u = cs(pa_u, pa_u, xo_u, xn_u)

    pia_d = sp.factor(
        (1 - th) * (pa_d - d) * xo_d
        + th * (qa_d - d) * xn_d
    )
    pib_d = sp.factor(
        pb * ((1 - th) * (1 - xo_d) + th * (1 - xn_d))
    )
    pia_u = sp.factor(
        (pa_u - d) * ((1 - th) * xo_u + th * xn_u)
    )
    pib_u = sp.factor(
        pb * ((1 - th) * (1 - xo_u) + th * (1 - xn_u))
    )

    assert sp.simplify(
        (cs_u - cs_d) - 3 * th * (1 - th) * s**2 / 16
    ) == 0
    assert sp.simplify(
        (pia_d - pia_u) - th * (1 - th) * s**2 / 8
    ) == 0
    assert sp.simplify(pib_d - pib_u) == 0
    assert sp.simplify(
        (cs_d + pia_d + pib_d) - (cs_u + pia_u + pib_u)
        + th * (1 - th) * s**2 / 16
    ) == 0

    print("CLEAN-ROOM SYMBOLIC ATTACK PASS")


# ---------------------------------------------------------------------------
# Direct global-deviation attacks
# ---------------------------------------------------------------------------

def candidate_is_global_hbp(theta, s, d):
    pa, qa, pb = displayed_hbp(theta, s, d)
    pia, pib = hbp_payoffs(pa, qa, pb, theta, s, d)

    # Independent A best responses by single-segment global enumeration.
    br_pa, _ = global_common_price_br(d, [pb + s], [1.0])
    br_qa, _ = global_common_price_br(d, [pb], [1.0])
    br_pb, best_b = global_common_price_br(
        0.0, [pa - s, qa], [1.0 - theta, theta]
    )

    ok = (
        min(abs(x - pa) for x in br_pa) <= 2e-7
        and min(abs(x - qa) for x in br_qa) <= 2e-7
        and min(abs(x - pb) for x in br_pb) <= 2e-7
        and best_b <= pib + 2e-8
    )
    return ok


def candidate_is_global_uniform(theta, s, d):
    pa, pb = displayed_uniform(theta, s, d)
    pia, pib = uniform_payoffs(pa, pb, theta, s, d)
    br_pa, best_a = global_common_price_br(
        d, [pb + s, pb], [1.0 - theta, theta]
    )
    br_pb, best_b = global_common_price_br(
        0.0, [pa - s, pa], [1.0 - theta, theta]
    )
    ok = (
        min(abs(x - pa) for x in br_pa) <= 2e-7
        and min(abs(x - pb) for x in br_pb) <= 2e-7
        and best_a <= pia + 2e-8
        and best_b <= pib + 2e-8
    )
    return ok


def numerical_adversarial_attack():
    rng = random.Random(SEED)
    inside = outside = near = 0

    # 30,000 independent draws from strict D_compare.
    for _ in range(30000):
        th = rng.uniform(0.005, 0.995)
        smax = 4.0 / (
            1.0 + math.sqrt(th) + math.sqrt(1.0 - th)
        )
        s = rng.uniform(1e-5, 0.999 * smax)
        L = -3.0 + (2.0 + th + 3.0 * math.sqrt(th)) * s / 2.0
        U = 3.0 - (
            1.0 - th + 3.0 * math.sqrt(1.0 - th)
        ) * s / 2.0
        d = rng.uniform(L + 1e-6 * (U - L), U - 1e-6 * (U - L))
        assert candidate_is_global_uniform(th, s, d)
        assert candidate_is_global_hbp(th, s, d)
        inside += 1

    # Attack just outside each uniform bound while keeping ordinary displayed
    # cohort shares interior.  A global deviation must be found.
    for _ in range(10000):
        th = rng.uniform(0.02, 0.98)
        smax = 4.0 / (
            1.0 + math.sqrt(th) + math.sqrt(1.0 - th)
        )
        s = rng.uniform(0.01, 0.85 * smax)
        L = -3.0 + (2.0 + th + 3.0 * math.sqrt(th)) * s / 2.0
        U = 3.0 - (
            1.0 - th + 3.0 * math.sqrt(1.0 - th)
        ) * s / 2.0

        eps = min(1e-4, 0.01 * (U - L))
        assert not candidate_is_global_uniform(th, s, L - eps)
        assert not candidate_is_global_uniform(th, s, U + eps)
        outside += 2

    # Boundary and near-boundary sweeps.
    for th in [0.01, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99]:
        smax = 4.0 / (
            1.0 + math.sqrt(th) + math.sqrt(1.0 - th)
        )
        for frac in [0.01, 0.25, 0.5, 0.9, 0.999999]:
            s = frac * smax
            L = -3.0 + (2.0 + th + 3.0 * math.sqrt(th)) * s / 2.0
            U = 3.0 - (
                1.0 - th + 3.0 * math.sqrt(1.0 - th)
            ) * s / 2.0
            assert candidate_is_global_uniform(th, s, L)
            assert candidate_is_global_uniform(th, s, U)
            assert candidate_is_global_hbp(th, s, L)
            assert candidate_is_global_hbp(th, s, U)
            near += 2

    print(
        "DIRECT GLOBAL ATTACK PASS",
        {"inside": inside, "outside": outside, "boundary": near},
    )


# ---------------------------------------------------------------------------
# Exact counterexamples and indifference-trigger audit
# ---------------------------------------------------------------------------

def exact_counterexamples():
    th = sp.Rational(1, 2)

    # Original HBP global-deviation witness.
    s = sp.Rational(23, 10)
    d = sp.Integer(0)
    pa = 1 + ((2 + th) * s + 4 * d) / 6
    qa = 1 + (4 * d - (1 - th) * s) / 6
    pb = 1 + (d - (1 - th) * s) / 3
    xo = sp.Rational(1, 2) + (s + pb - pa) / 2
    xn = sp.Rational(1, 2) + (pb - qa) / 2
    cand = sp.factor(pb * ((1 - th) * (1 - xo) + th * (1 - xn)))
    dev = sp.factor((qa + 1) / 2)
    dev_share = sp.factor((1 + qa - dev) / 2)
    gain = sp.factor(dev * th * dev_share - cand)
    assert gain == sp.Rational(3281, 230400)

    # Uniform entrant outside lower global bound.
    s = sp.Integer(1)
    d = -sp.Rational(4, 5)
    pa = 1 + (2 * d + (1 - th) * s) / 3
    pb = 1 + (d - (1 - th) * s) / 3
    xo = sp.Rational(1, 2) + (s + pb - pa) / 2
    xn = sp.Rational(1, 2) + (pb - pa) / 2
    cand = sp.factor(pb * ((1 - th) * (1 - xo) + th * (1 - xn)))
    dev = sp.factor((pa + 1) / 2)
    gain = sp.factor(dev * th * ((1 + pa - dev) / 2) - cand)
    assert gain == sp.Rational(89, 14400)

    # Uniform incumbent outside upper global bound.
    d = sp.Rational(9, 5)
    pa = 1 + (2 * d + (1 - th) * s) / 3
    pb = 1 + (d - (1 - th) * s) / 3
    xo = sp.Rational(1, 2) + (s + pb - pa) / 2
    xn = sp.Rational(1, 2) + (pb - pa) / 2
    cand = sp.factor((pa - d) * ((1 - th) * xo + th * xn))
    zdev = sp.factor((1 + pb + s - d) / 2)
    gain = sp.factor(zdev * (1 - th) * ((1 + pb + s - d - zdev) / 2) - cand)
    assert gain == sp.Rational(89, 14400)

    print("EXACT COUNTEREXAMPLES PASS")


def indifference_trigger_audit():
    """At equality bounds, the alternative tied action changes the opponent BR.

    This prevents silently treating the tied action as irrelevant.  It does not
    prove uniqueness and is not used as such.
    """
    th = 0.5
    s = 1.0
    L = -3.0 + (2.0 + th + 3.0 * math.sqrt(th)) * s / 2.0
    U = 3.0 - (
        1.0 - th + 3.0 * math.sqrt(1.0 - th)
    ) * s / 2.0

    # Lower boundary: B is tied with a higher new-only price.
    pa, pb = displayed_uniform(th, s, L)
    alt_b = (pa + 1.0) / 2.0
    br_a_alt, _ = global_common_price_br(
        L, [alt_b + s, alt_b], [1.0 - th, th]
    )
    assert all(abs(x - pa) > 1e-6 for x in br_a_alt)

    # Upper boundary: A is tied with a higher old-only price.
    pa, pb = displayed_uniform(th, s, U)
    h_old = 1.0 + pb + s - U
    alt_a = U + h_old / 2.0
    br_b_alt, _ = global_common_price_br(
        0.0, [alt_a - s, alt_a], [1.0 - th, th]
    )
    assert all(abs(x - pb) > 1e-6 for x in br_b_alt)

    print("INDIFFERENCE-TRIGGER AUDIT PASS")


# ---------------------------------------------------------------------------
# Diagnostic alternative-equilibrium search (not a uniqueness proof)
# ---------------------------------------------------------------------------

def deterministic_br_price(cost, rivals, weights):
    prices, _ = global_common_price_br(cost, rivals, weights)
    return min(prices)


def alternative_equilibrium_diagnostic():
    rng = random.Random(SEED + 1)
    parameter_draws = 120
    starts_per_draw = 21
    alternative_uniform = 0
    alternative_hbp = 0

    for _ in range(parameter_draws):
        th = rng.uniform(0.05, 0.95)
        smax = 4.0 / (
            1.0 + math.sqrt(th) + math.sqrt(1.0 - th)
        )
        s = rng.uniform(0.02, 0.9 * smax)
        L = -3.0 + (2.0 + th + 3.0 * math.sqrt(th)) * s / 2.0
        U = 3.0 - (
            1.0 - th + 3.0 * math.sqrt(1.0 - th)
        ) * s / 2.0
        d = rng.uniform(L + 0.05 * (U - L), U - 0.05 * (U - L))

        pa_star, pb_star = displayed_uniform(th, s, d)
        hpa_star, hqa_star, hpb_star = displayed_hbp(th, s, d)

        starts = [
            -4.0 + 12.0 * k / (starts_per_draw - 1)
            for k in range(starts_per_draw)
        ]

        found_u = []
        found_h = []

        for start in starts:
            # Uniform Gauss-Seidel global-BR dynamics.
            pb = start
            for _it in range(200):
                pa = deterministic_br_price(
                    d, [pb + s, pb], [1.0 - th, th]
                )
                new_pb = deterministic_br_price(
                    0.0, [pa - s, pa], [1.0 - th, th]
                )
                if abs(new_pb - pb) < 1e-11:
                    pb = new_pb
                    break
                pb = new_pb
            pa = deterministic_br_price(
                d, [pb + s, pb], [1.0 - th, th]
            )
            brb = deterministic_br_price(
                0.0, [pa - s, pa], [1.0 - th, th]
            )
            if abs(brb - pb) < 1e-8:
                found_u.append((pa, pb))

            # HBP reduces to the entrant price after A's two separable BRs.
            pb = start
            for _it in range(200):
                pa = deterministic_br_price(d, [pb + s], [1.0])
                qa = deterministic_br_price(d, [pb], [1.0])
                new_pb = deterministic_br_price(
                    0.0, [pa - s, qa], [1.0 - th, th]
                )
                if abs(new_pb - pb) < 1e-11:
                    pb = new_pb
                    break
                pb = new_pb
            pa = deterministic_br_price(d, [pb + s], [1.0])
            qa = deterministic_br_price(d, [pb], [1.0])
            brb = deterministic_br_price(
                0.0, [pa - s, qa], [1.0 - th, th]
            )
            if abs(brb - pb) < 1e-8:
                found_h.append((pa, qa, pb))

        def distinct(points, target):
            for p in points:
                if max(abs(a - b) for a, b in zip(p, target)) > 1e-6:
                    return True
            return False

        if distinct(found_u, (pa_star, pb_star)):
            alternative_uniform += 1
        if distinct(found_h, (hpa_star, hqa_star, hpb_star)):
            alternative_hbp += 1

    # This is diagnostic only.  The candidate propositions do not claim
    # uniqueness, so zero findings are not promoted to an analytic theorem.
    assert alternative_uniform == 0
    assert alternative_hbp == 0
    print(
        "ALTERNATIVE-EQUILIBRIUM DIAGNOSTIC",
        {
            "parameter_draws": parameter_draws,
            "starts_per_draw": starts_per_draw,
            "uniform_alternatives_found": alternative_uniform,
            "hbp_alternatives_found": alternative_hbp,
            "status": "DIAGNOSTIC_ONLY_NOT_A_UNIQUENESS_PROOF",
        },
    )


if __name__ == "__main__":
    exact_symbolic_attack()
    exact_counterexamples()
    numerical_adversarial_attack()
    indifference_trigger_audit()
    alternative_equilibrium_diagnostic()
    print("STAGE 4A CLEAN-ROOM ADVERSARIAL CHECKS PASS")
