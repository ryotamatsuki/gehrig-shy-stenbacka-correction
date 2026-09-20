# Frozen provenance snapshot imported from ryotamatsuki/ozshypapers, branch final-cleanroom-theorem-audit-20260919, path code/history_based_entry_welfare_2011_cleanroom.py on 2026-09-20.\n# Canonical correction verification lives in code/stage01_independent_recheck.py.\n\n"""Clean-room audit checks for Gehrig, Shy & Stenbacka (2011).

Target:
    "History-based Price Discrimination and Entry in Markets with Switching
    Costs: A Welfare Analysis"

The complete mathematical source used for the audit is the authors' dated
working-paper draft (14 December 2009), whose version relationship to the
2011 European Economic Review article is recorded in the source record.

This file derives the interior equilibrium, demand clipping, consumer surplus,
profits, and welfare directly from the primitives.  It also contains a global
deviation witness showing why the unqualified interior-price claim cannot be
treated as a global Nash equilibrium for all parameter values in the source.

Run:
    python code/history_based_entry_welfare_2011_cleanroom.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import sympy as sp


def clipped_share(raw: float) -> float:
    """Clip a Hotelling share to the unit interval."""
    return max(0.0, min(1.0, raw))


def discrimination_interior():
    """Solve the four interior FOCs under history-based pricing."""
    theta, sigma, tau, c_a, c_b = sp.symbols(
        "theta sigma tau c_a c_b", positive=True
    )
    delta_c = c_a - c_b

    p_a = tau + ((2 + theta) * sigma + 4 * c_a + 2 * c_b) / 6
    q_a = tau + (4 * c_a + 2 * c_b - (1 - theta) * sigma) / 6
    p_b = tau + (2 * c_b + c_a - (1 - theta) * sigma) / 3
    x_old = sp.Rational(1, 2) + ((2 + theta) * sigma - 2 * delta_c) / (
        12 * tau
    )
    x_new = sp.Rational(1, 2) - ((1 - theta) * sigma + 2 * delta_c) / (
        12 * tau
    )
    m_a = sp.factor(theta * x_new + (1 - theta) * x_old)
    return {
        "theta": theta,
        "sigma": sigma,
        "tau": tau,
        "c_a": c_a,
        "c_b": c_b,
        "p_a": sp.factor(p_a),
        "q_a": sp.factor(q_a),
        "p_b": sp.factor(p_b),
        "x_old": sp.factor(x_old),
        "x_new": sp.factor(x_new),
        "m_a": m_a,
    }


def uniform_interior():
    """Solve the interior FOCs when the incumbent uses one price."""
    theta, sigma, tau, c_a, c_b = sp.symbols(
        "theta sigma tau c_a c_b", positive=True
    )
    delta_c = c_a - c_b

    p_a = tau + (2 * c_a + c_b + (1 - theta) * sigma) / 3
    p_b = tau + (2 * c_b + c_a - (1 - theta) * sigma) / 3
    x_old = sp.Rational(1, 2) + ((2 * theta + 1) * sigma - delta_c) / (
        6 * tau
    )
    x_new = sp.Rational(1, 2) - (delta_c + 2 * (1 - theta) * sigma) / (
        6 * tau
    )
    m_a = sp.factor(theta * x_new + (1 - theta) * x_old)
    return {
        "theta": theta,
        "sigma": sigma,
        "tau": tau,
        "c_a": c_a,
        "c_b": c_b,
        "p_a": sp.factor(p_a),
        "p_b": sp.factor(p_b),
        "x_old": sp.factor(x_old),
        "x_new": sp.factor(x_new),
        "m_a": m_a,
    }


def consumer_surplus(
    theta, sigma, tau, beta, p_a, q_a, p_b, x_old, x_new
):
    """Integrate equilibrium utilities for old and new consumers."""
    z = sp.symbols("z")
    new_cs = sp.integrate(beta - q_a - tau * z, (z, 0, x_new))
    new_cs += sp.integrate(
        beta - p_b - tau * (1 - z), (z, x_new, 1)
    )
    old_cs = sp.integrate(beta - p_a - tau * z, (z, 0, x_old))
    old_cs += sp.integrate(
        beta - p_b - tau * (1 - z) - sigma, (z, x_old, 1)
    )
    return sp.factor(theta * new_cs + (1 - theta) * old_cs)


def welfare_identities():
    """Compare both regimes using the primitives, not displayed formulas."""
    d = discrimination_interior()
    u = uniform_interior()
    theta, sigma, tau, c_a, c_b = (
        d["theta"],
        d["sigma"],
        d["tau"],
        d["c_a"],
        d["c_b"],
    )
    beta = sp.symbols("beta", real=True)

    cs_d = consumer_surplus(
        theta,
        sigma,
        tau,
        beta,
        d["p_a"],
        d["q_a"],
        d["p_b"],
        d["x_old"],
        d["x_new"],
    )
    cs_u = consumer_surplus(
        theta,
        sigma,
        tau,
        beta,
        u["p_a"],
        u["p_a"],
        u["p_b"],
        u["x_old"],
        u["x_new"],
    )

    pi_a_d = sp.factor(
        theta * d["x_new"] * (d["q_a"] - c_a)
        + (1 - theta) * d["x_old"] * (d["p_a"] - c_a)
    )
    pi_b_d = sp.factor(
        (1 - d["m_a"]) * (d["p_b"] - c_b)
    )
    pi_a_u = sp.factor(u["m_a"] * (u["p_a"] - c_a))
    pi_b_u = sp.factor((1 - u["m_a"]) * (u["p_b"] - c_b))

    cs_gap = sp.factor(cs_u - cs_d)
    incumbent_profit_gap = sp.factor(pi_a_d - pi_a_u)
    entrant_profit_gap = sp.factor(pi_b_d - pi_b_u)
    welfare_gap = sp.factor(
        (cs_d + pi_a_d + pi_b_d) - (cs_u + pi_a_u + pi_b_u)
    )

    return {
        "cs_d": cs_d,
        "cs_u": cs_u,
        "cs_u_minus_cs_d": cs_gap,
        "pi_a_d": pi_a_d,
        "pi_a_u": pi_a_u,
        "pi_a_d_minus_pi_a_u": incumbent_profit_gap,
        "pi_b_d": pi_b_d,
        "pi_b_u": pi_b_u,
        "pi_b_d_minus_pi_b_u": entrant_profit_gap,
        "wd_minus_wu": welfare_gap,
    }


def a_segment_best_response(
    competitor_price: float,
    switching_shift: float,
    cost: float,
    tau: float,
):
    """Global best response for one incumbent segment.

    The effective rival price is competitor_price + switching_shift.  The
    return value is (regime, price, share), with zero-demand and full-demand
    branches included explicitly.
    """
    effective = competitor_price + switching_shift
    if effective < cost - tau:
        return "zero-demand", effective + tau, 0.0
    if effective > cost + 3 * tau:
        return "full-demand", effective - tau, 1.0
    price = (effective + cost + tau) / 2
    share = clipped_share(0.5 + (effective - price) / (2 * tau))
    return "interior", price, share


def b_profit(
    price: float,
    p_a: float,
    q_a: float,
    theta: float,
    sigma: float,
    tau: float,
    c_b: float,
) -> float:
    """Entrant profit with clipped old/new demand."""
    old_a = clipped_share(0.5 + (sigma + price - p_a) / (2 * tau))
    new_a = clipped_share(0.5 + (price - q_a) / (2 * tau))
    demand_b = theta * (1 - new_a) + (1 - theta) * (1 - old_a)
    return (price - c_b) * demand_b


def grid_maximum(values: Iterable[float], objective):
    """Simple adversarial cross-check over an explicit deviation grid."""
    candidates = list(values)
    scored = [(objective(value), value) for value in candidates]
    return max(scored)


def global_deviation_witness():
    """Show a profitable regime-crossing deviation at an interior candidate."""
    theta, sigma, tau, c_a, c_b = 0.5, 2.3, 1.0, 0.0, 0.0
    d = discrimination_interior()
    subs = {
        d["theta"]: theta,
        d["sigma"]: sigma,
        d["tau"]: tau,
        d["c_a"]: c_a,
        d["c_b"]: c_b,
    }
    p_a = float(d["p_a"].subs(subs))
    q_a = float(d["q_a"].subs(subs))
    p_b = float(d["p_b"].subs(subs))
    x_old = float(d["x_old"].subs(subs))
    x_new = float(d["x_new"].subs(subs))

    # Once old consumers are fully captured by A, B can optimize against new
    # consumers alone.  The branch starts at p_a-sigma+tau.
    old_zero_boundary = p_a - sigma + tau
    new_only_vertex = (q_a + c_b + tau) / 2
    candidate_profit = b_profit(
        p_b, p_a, q_a, theta, sigma, tau, c_b
    )
    deviation_profit = b_profit(
        new_only_vertex, p_a, q_a, theta, sigma, tau, c_b
    )

    assert 0 < x_old < 1 and 0 < x_new < 1
    assert new_only_vertex > old_zero_boundary
    assert deviation_profit > candidate_profit
    return {
        "p_a": p_a,
        "q_a": q_a,
        "p_b_candidate": p_b,
        "x_old": x_old,
        "x_new": x_new,
        "old_zero_boundary": old_zero_boundary,
        "new_only_vertex": new_only_vertex,
        "candidate_profit": candidate_profit,
        "deviation_profit": deviation_profit,
    }


def numerical_boundary_checks():
    """Check equality cases, invalid shares, and the exact deviation witness."""
    d = discrimination_interior()
    u = uniform_interior()
    tau = d["tau"]

    # The two regimes generate the same aggregate incumbent share in the
    # interior algebra.
    assert sp.simplify(d["m_a"] - u["m_a"]) == 0

    # A large switching-cost witness makes the displayed old share exceed one.
    bad_old_share = d["x_old"].subs(
        {d["theta"]: sp.Rational(1, 2), d["sigma"]: 10,
         d["tau"]: 1, d["c_a"]: 0, d["c_b"]: 0}
    )
    assert bad_old_share > 1

    witness = global_deviation_witness()
    assert witness["deviation_profit"] > witness["candidate_profit"]
    return witness


def main() -> None:
    d = discrimination_interior()
    u = uniform_interior()
    checks = welfare_identities()

    theta, sigma, tau, c_a, c_b = (
        d["theta"],
        d["sigma"],
        d["tau"],
        d["c_a"],
        d["c_b"],
    )
    delta_c = c_a - c_b

    # Clean-room FOCs for the discrimination regime.
    assert sp.simplify(
        d["p_a"] - c_a - 2 * tau * d["x_old"]
    ) == 0
    assert sp.simplify(
        d["q_a"] - c_a - 2 * tau * d["x_new"]
    ) == 0
    assert sp.simplify(
        d["p_b"] - c_b - 2 * tau * (1 - d["m_a"])
    ) == 0

    # Clean-room FOCs for the uniform regime.
    assert sp.simplify(u["p_a"] - c_a - 2 * tau * u["m_a"]) == 0
    assert sp.simplify(
        u["p_b"] - c_b - 2 * tau * (1 - u["m_a"])
    ) == 0
    assert sp.simplify(d["m_a"] - u["m_a"]) == 0

    # The paper reports 1/16 for the CS gap.  Direct integration gives 3/16.
    claimed_cs_gap = theta * (1 - theta) * sigma**2 / (16 * tau)
    corrected_cs_gap = 3 * theta * (1 - theta) * sigma**2 / (16 * tau)
    assert sp.simplify(checks["cs_u_minus_cs_d"] - corrected_cs_gap) == 0
    assert sp.simplify(checks["cs_u_minus_cs_d"] - claimed_cs_gap) != 0

    # The incumbent profit gap is 1/8, so the corrected welfare gap is -1/16.
    assert sp.simplify(
        checks["pi_a_d_minus_pi_a_u"]
        - theta * (1 - theta) * sigma**2 / (8 * tau)
    ) == 0
    assert checks["pi_b_d_minus_pi_b_u"] == 0
    assert sp.simplify(
        checks["wd_minus_wu"]
        + theta * (1 - theta) * sigma**2 / (16 * tau)
    ) == 0

    # The source's dominance threshold is algebraically correct wherever the
    # interior shares are admissible; the narrative's cost-sign sentence is not
    # checked here because it is a text-level sign error, not an FOC identity.
    assert sp.simplify(
        d["m_a"] - (sp.Rational(1, 2)
                     + ((1 - theta) * sigma - delta_c) / (6 * tau))
    ) == 0

    witness = numerical_boundary_checks()

    print("PASS: clean-room FOCs, corrected welfare algebra, and boundary checks")
    print("CS_u - CS_d (correct):", checks["cs_u_minus_cs_d"])
    print("W_d - W_u (correct):", checks["wd_minus_wu"])
    print("interior deviation witness:", witness)


if __name__ == "__main__":
    main()
