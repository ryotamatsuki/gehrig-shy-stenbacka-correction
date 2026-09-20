# Stage 4 — Minimal Model Gate / Global-Equilibrium Scope

## Canonical verdict

`GO — SOLVED OBJECT READY FOR STAGE 4A`

All results in this file are **Candidate Propositions** until independently
certified at Stage 4A.

## 1. Frozen source model

Target: Gehrig, Shy & Stenbacka (2011), with the complete mathematical
reconstruction anchored to the 14 December 2009 author draft.

Players:

- incumbent `A` at 0;
- entrant `B` at 1.

Consumer cohorts:

- old consumers, mass `1-theta`;
- new consumers, mass `theta`;
- `0<theta<1` in the regular analysis.

Primitives:

- `tau>0`: Hotelling transportation parameter;
- `sigma>=0`: switching cost incurred by old consumers who buy from B;
- `c_A,c_B`: constant marginal costs;
- `Delta c=c_A-c_B`.

Full market coverage is maintained as in the source.

### HBP strategy profile

- A chooses `(p_A,q_A)`: old and new prices separately;
- B chooses one common price `p_B`.

### Uniform strategy profile

- A chooses one price `p_A=q_A`;
- B chooses one common price `p_B`.

The game is simultaneous.

## 2. Strategy-set ambiguity in the source

The frozen draft states that firms choose prices to maximize profits and then
reports a unique equilibrium, but it does not explicitly state a price strategy
set such as `R` or `R_+`, nor does it state a parameter domain ensuring all
reported cutoffs remain in `[0,1]`.

Canonical Stage-4 convention:

- solve the price game over real prices;
- state all equilibrium conditions in net-markup form;
- separately note robustness to nonnegative-price strategy sets.

Why the ambiguity does not drive the correction on the regular domain:
a price below own marginal cost yields nonpositive variable profit because
demand is nonnegative, whereas the displayed candidates in the strict certified
domain have positive markups and positive profits. Hence potentially profitable
deviations are weakly above cost. If prices are constrained to be nonnegative
and marginal costs/candidate prices are nonnegative, the same global-deviation
conditions apply.

The correction paper must not pretend that the original source explicitly
specified this domain.

## 3. Exact clipped demands

Define `clip(z)=min(1,max(0,z))`.

### HBP

A's shares are

`x_o = clip(1/2 + (sigma+p_B-p_A)/(2 tau))`

`x_n = clip(1/2 + (p_B-q_A)/(2 tau))`.

Profits:

`pi_A=(1-theta)(p_A-c_A)x_o + theta(q_A-c_A)x_n`

`pi_B=(p_B-c_B)[(1-theta)(1-x_o)+theta(1-x_n)]`.

### Uniform pricing

Set `p_A=q_A` in the same clipped allocation.

## 4. Normalization and canonical mathematical representation

Set

`s=sigma/tau`

`d=(c_A-c_B)/tau`

and recenter prices by `c_B`, then divide all price differences by `tau`.

For any firm charging a **common price** to two cohorts, let the net markup be
`z=(p-c)/tau`. Its normalized demand can be written

`D(z)=w clip((h_H-z)/2)+(1-w)clip((h_L-z)/2)`

with `h_H>=h_L`.

This is a one-dimensional piecewise-affine demand and hence a continuous
piecewise-quadratic profit `z D(z)`.

Application-neutral parent class:

> simultaneous Bertrand pricing with weighted clipped affine demand segments
> and a common-price coupling constraint.

The generic piecewise optimization is method, not a novelty claim.

## 5. Common-price global-best-response lemma

Let

`hbar = w h_H + (1-w)h_L`.

Suppose the displayed smooth candidate has both positive-mass segments
interior and solves the both-interior FOC. Then

`z* = hbar/2`

and its normalized profit is

`pi* = hbar^2/8`.

For prices below `z*`, any nonnegative-markup deviation cannot improve on the
candidate: clipped demand is nonincreasing with slope in `[-1/2,0]`, and
profit is nondecreasing up to the both-interior vertex. Negative-markup
deviations give nonpositive profit.

For prices above `z*`, the only possible second local maximum appears after
the lower-threshold segment has dropped to zero. The remaining high-threshold
segment has unconstrained vertex `z_H=h_H/2` and peak normalized profit

`w h_H^2/8`.

Therefore the both-interior common-price candidate is a global best response
if and only if

`hbar^2 >= w h_H^2`,

equivalently, on the positive-markup regular domain,

`hbar >= sqrt(w) h_H`.

If the high-only vertex lies outside its branch, this inequality is
automatically satisfied; hence the single inequality remains necessary and
sufficient.

This lemma is used only as a source-specific certification device.

## 6. Displayed HBP candidate

The source interior formulas become

`p_A^d = tau + [(2+theta)sigma+4c_A+2c_B]/6`

`q_A^d = tau + [4c_A+2c_B-(1-theta)sigma]/6`

`p_B^d = tau + [2c_B+c_A-(1-theta)sigma]/3`.

The two separate A-pricing problems are ordinary one-segment clipped Hotelling
problems. Their displayed interior vertices are global best responses whenever
the corresponding displayed shares lie in `[0,1]`.

The entrant is the nontrivial common-price player. Its high-threshold segment
is the new cohort, of weight `theta`.

### Candidate Proposition 1 — exact HBP validity domain

For `0<theta<1`, the displayed HBP candidate is a global Nash equilibrium on
the closed candidate-validity domain

`D_HBP:`

`-3 tau + [(4-theta+3 sqrt(theta))/4] sigma <= Delta c`

and

`Delta c <= 3 tau - [(1-theta)/2] sigma`.

The regular strict domain replaces the weak inequalities by strict ones and
excludes degenerate zero-share/equal-best-response boundaries as needed.

The HBP domain is nonempty exactly when

`sigma/tau <= 8/(2-theta+sqrt(theta))`.

At the lower boundary the entrant is indifferent between the displayed common
price and a higher new-only optimum. At the upper HBP boundary the displayed
new-customer allocation reaches a clipped boundary; the candidate remains a
best response but is no longer a strict interior solution.

## 7. Displayed uniform-pricing candidate

The source formulas are

`p_A^u = tau + [2c_A+c_B+(1-theta)sigma]/3`

`p_B^u = tau + [2c_B+c_A-(1-theta)sigma]/3`.

Both firms now face common-price coupling.

For A:

- high-threshold/captive segment: old consumers;
- weight: `1-theta`;
- possible profitable regime-crossing deviation: raise price and abandon new
  consumers.

For B:

- high-threshold segment: new consumers;
- weight: `theta`;
- possible profitable regime-crossing deviation: raise price and abandon old
  consumers.

### Candidate Proposition 2 — exact uniform validity domain

For `0<theta<1`, the displayed uniform candidate is a global Nash equilibrium
if and only if

`D_U:`

`-3 tau + [(2+theta+3 sqrt(theta))/2] sigma <= Delta c`

and

`Delta c <= 3 tau - [(1-theta+3 sqrt(1-theta))/2] sigma`.

The domain is nonempty exactly when

`sigma/tau <= 4/[1+sqrt(theta)+sqrt(1-theta)]`.

The lower inequality is B's no-profitable-new-only-deviation condition.
The upper inequality is A's no-profitable-old-only-deviation condition.

These bounds are strictly tighter than ordinary cohort-interiority conditions
when `sigma>0` and `0<theta<1`.

## 8. Common comparison domain

The uniform lower bound exceeds the HBP lower bound by

`[3/4][theta+sqrt(theta)] sigma > 0`

for the regular domain.

The uniform upper bound is below the HBP upper bound by

`[3/2]sqrt(1-theta) sigma > 0`.

### Candidate Proposition 3 — containment

For `0<theta<1` and `sigma>=0`,

`D_U subseteq D_HBP`.

Hence the exact common domain for the displayed candidate comparison is

`D_compare = D_U`.

This is useful because no additional HBP restriction is needed once the
uniform candidate has passed its two global common-price deviation tests.

## 9. Corrected welfare comparison on the certified common domain

On `D_compare`, the displayed HBP and uniform price profiles are both genuine
global Nash equilibria, so the Stage-1 accounting identities can be given an
equilibrium interpretation.

### Candidate Proposition 4 — corrected welfare identities

`CS^u-CS^d = 3 theta(1-theta)sigma^2/(16 tau)`

`pi_A^d-pi_A^u = theta(1-theta)sigma^2/(8 tau)`

`pi_B^d-pi_B^u = 0`

and therefore

`W^d-W^u = -theta(1-theta)sigma^2/(16 tau)`.

Thus, on the exact common certified domain and for
`0<theta<1, sigma>0`, total welfare is strictly **higher under uniform
pricing** for these equilibria.

The correction does not claim that this ranking has been established for every
possible outside-branch equilibrium or every equilibrium selection outside
`D_compare`.

## 10. Exact finite-deviation regression cases

### HBP entrant failure — inherited from Stage 1

`theta=1/2, tau=1, sigma=23/10, c_A=c_B=0`.

Both displayed cohort shares are strictly interior, yet a new-only entrant
price gives exact profit gain

`3281/230400 > 0`.

This permanently rejects "interior shares imply global Nash."

### Uniform entrant failure

Take

`theta=1/2, tau=1, sigma=1, c_B=0, c_A=-4/5`.

The displayed uniform candidate has

`p_A=19/30, p_B=17/30`,

with strictly interior displayed shares

`x_o=29/30, x_n=7/15`.

The entrant can move to the new-only branch at

`p_B'=49/60`

and gains exactly

`89/14400 > 0`.

### Uniform incumbent failure

Take

`theta=1/2, tau=1, sigma=1, c_B=0, c_A=9/5`.

The displayed uniform candidate has

`p_A=71/30, p_B=43/30`,

with strictly interior displayed shares

`x_o=8/15, x_n=1/30`.

The incumbent can move to the old-only branch at

`p_A'=157/60`

and gains exactly

`89/14400 > 0`.

These examples show why both sides of `D_U` are economically substantive.

## 11. Verification artifacts

Production derivation / regression script:

`code/stage04_global_validity.py`.

It contains:

- symbolic derivation of all three global-validity thresholds;
- exact verification of containment;
- exact nonempty-domain thresholds;
- the Stage-1 HBP counterexample;
- exact uniform-A and uniform-B counterexamples;
- an independently coded direct clipped-payoff evaluator that enumerates all
  breakpoints and quadratic branch vertices;
- deterministic randomized attacks from inside and outside the claimed domain.

The CI workflow runs both the Stage-1 welfare recheck and Stage-4 global-validity
checks.

## 12. Limiting cases

### `sigma=0`

The two cohorts become strategically identical with respect to switching.
Both validity domains reduce to the standard displayed Hotelling condition

`-3 tau <= Delta c <= 3 tau`.

The welfare wedge vanishes.

### `theta -> 0` or `theta -> 1`

The two-positive-mass-segment lemma degenerates because one cohort disappears.
The welfare wedge vanishes as `theta(1-theta)`. Endpoint cohort cases should
be stated separately rather than inferred by dividing expressions involving
`1-sqrt(theta)` or `1-sqrt(1-theta)`.

### symmetric costs

At `Delta c=0`, the common-domain condition reduces to an upper bound on
`sigma/tau` determined by the tighter of the two uniform global-deviation
conditions.

## 13. Existence, uniqueness, and scope

Existence of the **displayed** equilibrium is established on the validity
domains above.

Stage 4 does **not** claim a full uniqueness theorem for all pure-strategy
equilibria of the clipped game. Such a theorem would amount to part of the
Architecture-C correspondence that Stage 3 explicitly made optional.

Accordingly:

- the source's unrestricted phrase "uniquely-determined equilibrium prices" is
  not recertified here;
- the correction paper can state exactly when the displayed formulas are Nash;
- claims about uniqueness, multiplicity, or welfare of other outside-branch
  equilibria remain outside the Stage-4 headline unless Stage 4A finds them
  material to the correction.

This is a scope choice, not an inference that alternative equilibria exist.

## 14. Candidate theorem certificate pre-map for Stage 4A

Stage 4A must independently attack:

1. the common-price global-best-response lemma, especially low-price branches
   and branch-feasibility logic;
2. `D_HBP`, including the clipped upper boundary;
3. both inequalities defining `D_U`;
4. the containment `D_U subseteq D_HBP`;
5. the claim that nonnegative-price restrictions do not alter profitable
   deviations when candidate feasibility/nonnegative costs hold;
6. the corrected welfare identities on `D_compare`;
7. the exact three finite-deviation regression examples;
8. whether failure to prove full equilibrium uniqueness is material to any
   wording intended for the eventual paper.

Formal verification is prima facie applicable to the proof-critical
piecewise/case logic, threshold inequalities, exact counterexamples, and welfare
identities. The formalization target map must be finalized at Stage 4A and
implemented/revisited at Stage 7.5A according to workflow v2.3.

## Canonical Stage-4 decision

`GO -> STAGE 4A`

The solved object is the smallest Architecture-B correction:

> exact global-validity scope for the source's displayed HBP and uniform price
> formulas, plus the corrected welfare ranking on their common certified
> domain.

The complete outside-branch equilibrium atlas remains unauthorized as a
headline extension unless Stage 4A demonstrates that it is necessary.
