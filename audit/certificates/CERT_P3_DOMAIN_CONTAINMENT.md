# Certificate P3 — Common comparison domain

## Claim ID

`P3-DOMAIN-CONTAINMENT`

## Exact claim

For `0<theta<1` and `sigma>=0`,

`D_U subseteq D_HBP`.

The lower-bound difference is

`L_U-L_HBP = (3/4)[theta+sqrt(theta)] sigma >= 0`.

The upper-bound difference is

`U_HBP-U_U = (3/2)sqrt(1-theta) sigma >= 0`.

Therefore the displayed-equilibrium common comparison domain is

`D_compare=D_U`.

## Attack

- independently reconstructed all four bounds from primitive payoff
  comparisons;
- factorized both containment differences exactly;
- checked limiting case `sigma=0`, where the bounds coincide;
- checked the nonempty-domain threshold.

## Evidence

`code/stage04a_cleanroom_adversarial.py`.

## Scope limitation

This is containment of the validity domains of the **displayed candidates**.
It says nothing about whether other equilibria exist outside those domains.

## Certificate state

`PASS`
