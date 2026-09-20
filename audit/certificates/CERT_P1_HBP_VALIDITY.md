# Certificate P1 — HBP displayed-candidate validity

## Claim ID

`P1-HBP-DISPLAYED-GLOBAL-NASH`

## Exact claim

For `0<theta<1`, `tau>0`, `sigma>=0`, the displayed HBP candidate is a
global Nash equilibrium whenever

`-3 tau + [(4-theta+3 sqrt(theta))/4] sigma <= Delta c`

and

`Delta c <= 3 tau - [(1-theta)/2] sigma`.

Conversely, within the displayed candidate's regular/interior construction,
violation of the lower global-deviation condition or the binding incumbent
segment condition invalidates the displayed profile as a global Nash
equilibrium.

## Claim type

Existence/validity characterization of the **displayed price profile**.
It is not a uniqueness theorem for all pure-strategy equilibria.

## Assumptions

Economic:
- source Hotelling model;
- full market coverage;
- old/new masses `1-theta`, `theta`;
- switching cost applies only to old consumers buying from B;
- simultaneous pricing;
- A discriminates by cohort, B sets one common price.

Analytical:
- clipped demands are used globally;
- real-price strategy domain for canonical analysis;
- nonnegative-price robustness only when candidate feasibility and cost
  conditions make the relevant actions feasible.

## Globality audit

- A's two segment prices were independently reconstructed as separate
  one-segment clipped-demand optimization problems.
- B's common price was globally optimized by exhaustive enumeration of all
  breakpoints and branch vertices.
- The exact Stage-1 regime-crossing counterexample is retained as a permanent
  falsification of the broader unrestricted claim.
- Boundary and near-boundary draws were attacked independently.

## Evidence ledger

| attack | artifact | result | limitation |
|---|---|---|---|
| symbolic threshold reconstruction | `code/stage04a_cleanroom_adversarial.py` | passes exact equality/sign checks | relies on source primitives |
| finite/global deviation enumeration | same | no profitable deviation inside claimed domain | certifies displayed profile only |
| outside-domain counterexample | same + Stage-1 witness | profitable new-only deviation exists | not a full outside correspondence |
| boundary audit | same | displayed profile remains a best-response profile at weak boundaries | ties may create other best responses |
| alternative-equilibrium diagnostic | same | no alternatives found in deterministic multi-start sample | not uniqueness proof |

## Indifference trigger

At equality boundaries a player can have a tied alternative best response.
Stage 4A does not discard this fact. The paper must not convert P1 into a
selection-free uniqueness statement.

## Maximum defensible prose

"The displayed HBP formulas constitute a Nash equilibrium exactly on the
certified displayed-candidate validity domain stated in P1."

Prohibited:
"the HBP game has a unique equilibrium on the entire source parameter space."

## Certificate state

`PASS`
