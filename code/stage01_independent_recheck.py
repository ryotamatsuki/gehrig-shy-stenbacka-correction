"""Independent Stage-1 recheck for Gehrig-Shy-Stenbacka (2011).

This script is intentionally separate from the parent audit implementation.
It derives the interior candidates and welfare identities directly with SymPy
and verifies the exact regime-crossing counterexample.

Run:
    python code/stage01_independent_recheck.py
"""

import sympy as sp


def main():
    th, s, t, ca, cb, beta = sp.symbols(
        "theta sigma tau c_A c_B beta", positive=True
    )
    z = sp.symbols("z", real=True)
    dc = ca - cb

    # HBP interior candidate.
    pa_d = t + ((2 + th) * s + 4 * ca + 2 * cb) / 6
    qa_d = t + (4 * ca + 2 * cb - (1 - th) * s) / 6
    pb_d = t + (2 * cb + ca - (1 - th) * s) / 3
    xo_d = sp.Rational(1, 2) + ((2 + th) * s - 2 * dc) / (12 * t)
    xn_d = sp.Rational(1, 2) - ((1 - th) * s + 2 * dc) / (12 * t)
    ma_d = sp.factor((1 - th) * xo_d + th * xn_d)

    # Uniform-pricing interior candidate.
    pa_u = t + (2 * ca + cb + (1 - th) * s) / 3
    pb_u = t + (2 * cb + ca - (1 - th) * s) / 3
    xo_u = sp.Rational(1, 2) + ((2 * th + 1) * s - dc) / (6 * t)
    xn_u = sp.Rational(1, 2) - (dc + 2 * (1 - th) * s) / (6 * t)
    ma_u = sp.factor((1 - th) * xo_u + th * xn_u)

    assert sp.simplify(ma_d - ma_u) == 0

    def cs(pa, qa, pb, xo, xn):
        old = sp.integrate(beta - pa - t * z, (z, 0, xo))
        old += sp.integrate(beta - pb - t * (1 - z) - s, (z, xo, 1))
        new = sp.integrate(beta - qa - t * z, (z, 0, xn))
        new += sp.integrate(beta - pb - t * (1 - z), (z, xn, 1))
        return sp.factor((1 - th) * old + th * new)

    cs_d = cs(pa_d, qa_d, pb_d, xo_d, xn_d)
    cs_u = cs(pa_u, pa_u, pb_u, xo_u, xn_u)

    pia_d = sp.factor(
        (1 - th) * (pa_d - ca) * xo_d + th * (qa_d - ca) * xn_d
    )
    pib_d = sp.factor((pb_d - cb) * (1 - ma_d))
    pia_u = sp.factor((pa_u - ca) * ma_u)
    pib_u = sp.factor((pb_u - cb) * (1 - ma_u))

    expected_cs = 3 * th * (1 - th) * s**2 / (16 * t)
    expected_pia = th * (1 - th) * s**2 / (8 * t)
    expected_w = -th * (1 - th) * s**2 / (16 * t)

    assert sp.simplify((cs_u - cs_d) - expected_cs) == 0
    assert sp.simplify((pia_d - pia_u) - expected_pia) == 0
    assert sp.simplify(pib_d - pib_u) == 0
    wd_minus_wu = sp.factor((cs_d + pia_d + pib_d) - (cs_u + pia_u + pib_u))
    assert sp.simplify(wd_minus_wu - expected_w) == 0

    # Exact all-positive-price global-deviation witness.
    sub = {
        th: sp.Rational(1, 2),
        t: 1,
        s: sp.Rational(23, 10),
        ca: 0,
        cb: 0,
    }
    PA = sp.factor(pa_d.subs(sub))
    QA = sp.factor(qa_d.subs(sub))
    PB = sp.factor(pb_d.subs(sub))
    XO = sp.factor(xo_d.subs(sub))
    XN = sp.factor(xn_d.subs(sub))

    boundary = sp.factor(PA - sub[s] + sub[t])
    dev = sp.factor((QA + sub[cb] + sub[t]) / 2)

    def clip(q):
        return sp.Max(0, sp.Min(1, q))

    # Evaluate exact shares by branch, avoiding Max/Min simplification.
    assert PA == sp.Rational(47, 24)
    assert QA == sp.Rational(97, 120)
    assert PB == sp.Rational(37, 60)
    assert XO == sp.Rational(47, 48)
    assert XN == sp.Rational(97, 240)
    assert boundary == sp.Rational(79, 120)
    assert dev == sp.Rational(217, 240)
    assert dev > boundary

    cand_profit = sp.factor(
        (PB - sub[cb]) *
        ((1 - sub[th]) * (1 - XO) + sub[th] * (1 - XN))
    )

    # At dev > boundary, old demand for B is zero; new demand is interior.
    xn_dev = sp.Rational(1, 2) + (dev - QA) / (2 * sub[t])
    dev_profit = sp.factor((dev - sub[cb]) * sub[th] * (1 - xn_dev))
    gain = sp.factor(dev_profit - cand_profit)

    assert cand_profit == sp.Rational(1369, 7200)
    assert dev_profit == sp.Rational(47089, 230400)
    assert gain == sp.Rational(3281, 230400)
    assert gain > 0

    print("PASS")
    print("CS_u-CS_d =", sp.factor(cs_u - cs_d))
    print("pi_A^d-pi_A^u =", sp.factor(pia_d - pia_u))
    print("pi_B^d-pi_B^u =", sp.factor(pib_d - pib_u))
    print("W_d-W_u =", wd_minus_wu)
    print("counterexample gain =", gain)


if __name__ == "__main__":
    main()
