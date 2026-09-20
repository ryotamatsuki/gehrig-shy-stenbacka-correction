# Certificate P4 — Corrected welfare identity

## Claim ID

`P4-CORRECTED-WELFARE`

## Exact claim

For the displayed HBP and uniform equilibria on their certified common domain,

`CS^u-CS^d = 3 theta(1-theta)sigma^2/(16 tau)`,

`pi_A^d-pi_A^u = theta(1-theta)sigma^2/(8 tau)`,

`pi_B^d-pi_B^u = 0`,

and hence

`W^d-W^u = -theta(1-theta)sigma^2/(16 tau)`.

For `0<theta<1`, `sigma>0`, `tau>0`, this displayed-equilibrium welfare
difference is strictly negative.

## Independent reconstruction

Stage 4A re-integrates consumer utility from primitives and independently
recomputes both firms' profits. It does not import the Stage-1 or Stage-4
symbolic objects.

The normalization `tau=1` is used internally for the clean-room symbolic
attack; dimensional restoration gives the stated `1/tau` factor.

## Welfare benchmark certificate

- population: the same old/new consumers as in the source;
- welfare: consumer surplus plus both firms' operating profits;
- switching and transportation costs enter through consumer utilities;
- there is no claim of a planner first-best;
- the comparison concerns the two displayed equilibria, not every equilibrium
  selection outside or on knife-edge multiplicity boundaries.

## Boundary/selection discipline

The algebraic identities hold for the displayed formulas on the closed common
domain. If equality boundaries admit additional equilibria, P4 does not assert
that every such equilibrium has the same welfare.

Maximum defensible prose:

"At the displayed equilibria, on the domain where both displayed price
profiles are global Nash equilibria, uniform pricing yields higher total
welfare by `theta(1-theta)sigma^2/(16 tau)`."

Prohibited:

"Uniform pricing is welfare-superior in every equilibrium for all parameters."

## Evidence

- `code/stage04a_cleanroom_adversarial.py`
- `code/stage01_independent_recheck.py`

The Stage-4A file is the independent certificate; the Stage-1 file is
corroborating provenance.

## Certificate state

`PASS`
