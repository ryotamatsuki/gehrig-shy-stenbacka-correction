# Certificate P2 — Uniform displayed-candidate validity

## Claim ID

`P2-UNIFORM-DISPLAYED-GLOBAL-NASH`

## Exact claim

For `0<theta<1`, `tau>0`, `sigma>=0`, the displayed uniform-pricing
candidate is a global Nash equilibrium iff

`-3 tau + [(2+theta+3 sqrt(theta))/2] sigma <= Delta c`

and

`Delta c <= 3 tau - [(1-theta+3 sqrt(1-theta))/2] sigma`,

for the displayed candidate construction.

The lower bound is B's no-profitable-new-only-deviation condition.
The upper bound is A's no-profitable-old-only-deviation condition.

## Claim type

Necessary-and-sufficient global-validity characterization for the
**displayed candidate**, not uniqueness of the full equilibrium correspondence.

## Independent attacks

1. Reconstructed both firms' clipped demands directly.
2. Globally enumerated all common-price branch maxima for each unilateral
   deviation.
3. Tested 30,000 draws strictly inside the claimed domain.
4. Tested 20,000 just-outside-bound deviations across the lower and upper
   sides combined.
5. Tested boundary and near-boundary parameter configurations.
6. Preserved exact entrant and incumbent counterexamples with profit gains
   `89/14400`.

## Evidence

`code/stage04a_cleanroom_adversarial.py`.

Exact counterexamples:
- lower-side entrant failure:
  `theta=1/2,tau=sigma=1,c_B=0,c_A=-4/5`;
- upper-side incumbent failure:
  `theta=1/2,tau=sigma=1,c_B=0,c_A=9/5`.

Both have strictly interior displayed cohort shares.

## Indifference audit

At the lower equality boundary, B is indifferent between the displayed common
price and a higher new-only price. At the upper equality boundary, A is
indifferent between the displayed price and a higher old-only price.

The independent audit changes the indifferent action and recomputes the other
firm's global best response. In the audited boundary benchmark the opponent's
best response changes, so the tied action is not dismissed as strategically
irrelevant.

This is why no uniqueness or selection-invariance statement is attached to the
weak boundaries.

## Alternative-equilibrium audit

A deterministic global-best-response multi-start diagnostic is run on strict
interior draws. It found no alternative equilibrium in the audited sample, but
this is explicitly **not** elevated to a uniqueness proof.

P2 requires only that the displayed profile is a global Nash equilibrium.
Downstream welfare language is restricted to that displayed profile, so full
equilibrium uniqueness is not required for P2's stated scope.

## Certificate state

`PASS`
