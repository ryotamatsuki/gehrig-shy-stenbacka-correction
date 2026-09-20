"""Independent N3 referee recheck.

This script intentionally does not import project derivation/audit modules.
It reconstructs the central manuscript identities from primitive utilities
and displayed candidates, and independently checks the global-deviation
threshold reductions used in Proposition 1.
"""

import sympy as sp


def main():
    th, sig, tau = sp.symbols("theta sigma tau", positive=True, real=True)
    cA, cB, beta = sp.symbols("c_A c_B beta", real=True)
    x = sp.symbols("x", real=True)
    dc = cA - cB

    pAd = tau + ((2 + th) * sig + 4*cA + 2*cB) / 6
    qAd = tau + (4*cA + 2*cB - (1-th)*sig) / 6
    pBd = tau + (2*cB + cA - (1-th)*sig) / 3

    pAu = tau + (2*cA + cB + (1-th)*sig) / 3
    pBu = pBd

    xod = sp.Rational(1, 2) + ((2+th)*sig - 2*dc) / (12*tau)
    xnd = sp.Rational(1, 2) - ((1-th)*sig + 2*dc) / (12*tau)
    xou = sp.Rational(1, 2) + ((2*th+1)*sig - dc) / (6*tau)
    xnu = sp.Rational(1, 2) - (dc + 2*(1-th)*sig) / (6*tau)

    def cs_old(cut, pA, pB):
        return (
            sp.integrate(beta-pA-tau*x, (x, 0, cut))
            + sp.integrate(beta-pB-tau*(1-x)-sig, (x, cut, 1))
        )

    def cs_new(cut, qA, pB):
        return (
            sp.integrate(beta-qA-tau*x, (x, 0, cut))
            + sp.integrate(beta-pB-tau*(1-x), (x, cut, 1))
        )

    CSd = sp.expand((1-th)*cs_old(xod, pAd, pBd) + th*cs_new(xnd, qAd, pBd))
    CSu = sp.expand((1-th)*cs_old(xou, pAu, pBu) + th*cs_new(xnu, pAu, pBu))

    cs_gap = sp.factor(CSu-CSd)
    assert sp.simplify(cs_gap - 3*th*(1-th)*sig**2/(16*tau)) == 0

    piAd = sp.expand((1-th)*(pAd-cA)*xod + th*(qAd-cA)*xnd)
    piAu = sp.expand((pAu-cA)*((1-th)*xou + th*xnu))
    piBd = sp.expand((pBd-cB)*((1-th)*(1-xod) + th*(1-xnd)))
    piBu = sp.expand((pBu-cB)*((1-th)*(1-xou) + th*(1-xnu)))

    assert sp.simplify(
        (piAd-piAu) - th*(1-th)*sig**2/(8*tau)
    ) == 0
    assert sp.simplify(piBd-piBu) == 0

    w_gap = sp.factor((piAd-piAu) + (piBd-piBu) - (CSu-CSd))
    assert sp.simplify(
        w_gap + th*(1-th)*sig**2/(16*tau)
    ) == 0

    # Independent normalized threshold reductions.
    r, s, d = sp.symbols("r s d", real=True)
    theta = r**2

    pAd_n = 1 + ((2+theta)*s + 4*d)/6
    qAd_n = 1 + (4*d - (1-theta)*s)/6
    h_old_Bd = 1 + pAd_n - s
    h_new_Bd = 1 + qAd_n
    hbar_Bd = (1-theta)*h_old_Bd + theta*h_new_Bd
    gap_Bd = sp.factor(hbar_Bd-r*h_new_Bd)
    target_Bd = sp.Rational(2, 3)*(1-r)*(
        d - (-3 + (4-r**2+3*r)*s/4)
    )
    assert sp.simplify(gap_Bd-target_Bd) == 0

    pAu_n = 1 + (2*d + (1-theta)*s)/3
    h_old_Bu = 1 + pAu_n - s
    h_new_Bu = 1 + pAu_n
    hbar_Bu = (1-theta)*h_old_Bu + theta*h_new_Bu
    gap_Bu = sp.factor(hbar_Bu-r*h_new_Bu)
    target_Bu = sp.Rational(2, 3)*(1-r)*(
        d - (-3 + (2+r**2+3*r)*s/2)
    )
    assert sp.simplify(gap_Bu-target_Bu) == 0

    q = sp.symbols("q", real=True)
    pBu_q = 1 + (d-q**2*s)/3
    h_old_Au = 1 + s + pBu_q - d
    h_new_Au = 1 + pBu_q - d
    hbar_Au = q**2*h_old_Au + (1-q**2)*h_new_Au
    gap_Au = sp.factor(hbar_Au-q*h_old_Au)
    target_Au = sp.Rational(2, 3)*(1-q)*(
        (3-(q**2+3*q)*s/2)-d
    )
    assert sp.simplify(gap_Au-target_Au) == 0

    print("N3 INDEPENDENT REFEREE RECHECK PASS")
    print("CSu-CSd =", cs_gap)
    print("piA_d-piA_u =", sp.factor(piAd-piAu))
    print("piB_d-piB_u =", sp.factor(piBd-piBu))
    print("Wd-Wu =", w_gap)
    print("HBP threshold gap =", gap_Bd)
    print("Uniform B threshold gap =", gap_Bu)
    print("Uniform A threshold gap =", gap_Au)


if __name__ == "__main__":
    main()
