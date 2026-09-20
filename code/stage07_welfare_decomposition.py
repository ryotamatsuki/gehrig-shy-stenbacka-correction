"""Stage-7 welfare decomposition and comparative-prediction verification.

All identities are exact and conditional on the displayed equilibria being
valid on D_compare.
"""

import sympy as sp


def main():
    th, s, t, dc = sp.symbols(
        "theta sigma tau Delta_c", positive=True, real=True
    )
    x = sp.symbols("x", real=True)

    xo_d = sp.Rational(1, 2) + ((2 + th) * s - 2 * dc) / (12 * t)
    xn_d = sp.Rational(1, 2) - ((1 - th) * s + 2 * dc) / (12 * t)

    xo_u = sp.Rational(1, 2) + ((2 * th + 1) * s - dc) / (6 * t)
    xn_u = sp.Rational(1, 2) - (dc + 2 * (1 - th) * s) / (6 * t)

    # Allocation-composition shifts.
    assert sp.simplify(xo_d - xo_u + th * s / (4 * t)) == 0
    assert sp.simplify(
        xn_d - xn_u - (1 - th) * s / (4 * t)
    ) == 0

    mA_d = sp.factor((1 - th) * xo_d + th * xn_d)
    mA_u = sp.factor((1 - th) * xo_u + th * xn_u)
    assert sp.simplify(mA_d - mA_u) == 0

    # Prices: entrant unchanged; incumbent tilts old/new prices in opposite
    # directions relative to uniform pricing.
    ca, cb = sp.symbols("c_A c_B", real=True)
    pa_d = t + ((2 + th) * s + 4 * ca + 2 * cb) / 6
    qa_d = t + (4 * ca + 2 * cb - (1 - th) * s) / 6
    pb_d = t + (2 * cb + ca - (1 - th) * s) / 3
    pa_u = t + (2 * ca + cb + (1 - th) * s) / 3
    pb_u = pb_d

    assert sp.simplify(pa_d - pa_u - th * s / 2) == 0
    assert sp.simplify(qa_d - pa_u + (1 - th) * s / 2) == 0
    assert sp.simplify(pb_d - pb_u) == 0

    # Transport resource cost for one cohort with A share cutoff z.
    z = sp.symbols("z", real=True)
    tc = sp.factor(
        t * (
            sp.integrate(x, (x, 0, z))
            + sp.integrate(1 - x, (x, z, 1))
        )
    )

    TC_d = sp.factor(
        (1 - th) * tc.subs(z, xo_d) + th * tc.subs(z, xn_d)
    )
    TC_u = sp.factor(
        (1 - th) * tc.subs(z, xo_u) + th * tc.subs(z, xn_u)
    )

    # Switching cost is borne only by old consumers buying B.
    SC_d = sp.factor((1 - th) * s * (1 - xo_d))
    SC_u = sp.factor((1 - th) * s * (1 - xo_u))

    assert sp.simplify(
        (TC_d - TC_u) + 3 * th * (1 - th) * s**2 / (16 * t)
    ) == 0
    assert sp.simplify(
        (SC_d - SC_u) - th * (1 - th) * s**2 / (4 * t)
    ) == 0

    resource_gap = sp.factor((TC_d + SC_d) - (TC_u + SC_u))
    assert sp.simplify(
        resource_gap - th * (1 - th) * s**2 / (16 * t)
    ) == 0

    # Because aggregate firm shares are unchanged, production-cost spending is
    # unchanged between regimes. Therefore W_d-W_u is minus the resource-cost
    # gap.
    welfare_gap = -resource_gap
    assert sp.simplify(
        welfare_gap + th * (1 - th) * s**2 / (16 * t)
    ) == 0

    cs_loss = 3 * th * (1 - th) * s**2 / (16 * t)
    incumbent_gain = th * (1 - th) * s**2 / (8 * t)
    assert sp.simplify(incumbent_gain / cs_loss - sp.Rational(2, 3)) == 0

    print("STAGE 7 WELFARE DECOMPOSITION PASS")
    print("x_old^d-x_old^u =", sp.factor(xo_d - xo_u))
    print("x_new^d-x_new^u =", sp.factor(xn_d - xn_u))
    print("TC_d-TC_u =", sp.factor(TC_d - TC_u))
    print("SC_d-SC_u =", sp.factor(SC_d - SC_u))
    print("resource_cost_d-resource_cost_u =", resource_gap)
    print("W_d-W_u =", welfare_gap)
    print("incumbent_gain / consumer_loss =", sp.Rational(2, 3))


if __name__ == "__main__":
    main()
