# Certificate L1 — Common-price global best response

## Claim ID

`L1-COMMON-PRICE-GLOBAL-BR`

## Exact claim

For a player with nonnegative demand

`D(z)=w clip((h_H-z)/2)+(1-w)clip((h_L-z)/2)`

where `0<w<1`, `h_H>=h_L`, and a displayed candidate has both segments
interior and solves the smooth FOC, the displayed markup
`z*=hbar/2`, with `hbar=w h_H+(1-w)h_L`, is a global best response iff the
high-only branch cannot beat it. On the positive regular branch this is

`hbar >= sqrt(w) h_H`.

## Classification

- equilibrium ingredient: global best-response characterization;
- baseline functional form: two weighted clipped affine segments;
- global, not merely local, conditional on the stated two-segment structure;
- no uniqueness claim for the entire game.

## Quantifiers / domain

- `0<w<1`;
- displayed candidate has both positive-mass segments interior;
- actual demand is clipped to `[0,1]`;
- price is represented by real net markup `z`;
- negative markup cannot improve on a positive-profit regular candidate.

## Adversarial attacks

1. Reconstructed the payoff independently from primitives.
2. Enumerated every clipping breakpoint and every feasible quadratic-branch
   vertex in `code/stage04a_cleanroom_adversarial.py`.
3. Checked low-price branches rather than assuming concavity globally.
4. Checked the high-only branch explicitly.
5. Ran direct global maximization over all enumerated candidates in the
   independent randomized attack.

## Evidence

- `code/stage04a_cleanroom_adversarial.py`
- Stage-4A CI run for the certified commit.
- Production derivation is deliberately not imported by the independent code.

## Alternative-equilibrium / indifference scope

This lemma is a one-player best-response statement, not a game-level uniqueness
claim. Equality creates multiple best responses and therefore triggers the
separate indifference audit in the Stage-4A main record.

## Surviving limitation

The lemma is not claimed as a new general theorem. It certifies the exact
piecewise-linear demand object used by the source model.

## Certificate state

`PASS`
