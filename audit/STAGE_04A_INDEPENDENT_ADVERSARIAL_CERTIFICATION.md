# Stage 4A — Independent Mathematical Adversarial Certification

## Canonical verdict

`GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`

Routing: **Stage 6**. Stage 5 is not triggered because no single economic
deficiency requiring model repair was found.

## Independent implementation

The clean-room verifier is:

`code/stage04a_cleanroom_adversarial.py`

It does **not** import or call `code/stage04_global_validity.py`.

It reconstructs primitive clipped Hotelling payoffs, enumerates every
piecewise-quadratic unilateral-deviation branch, and independently rederives
the proof-critical threshold and welfare identities.

Certified CI evidence:

- successful commit:
  `a99e375e09a65fc0cfd0839876c4e13545a834cf`
- workflow run:
  `35491396515`
- job:
  `106026840293`

Final clean-room output:

- `CLEAN-ROOM SYMBOLIC ATTACK PASS`
- `EXACT COUNTEREXAMPLES PASS`
- `DIRECT GLOBAL ATTACK PASS {'inside': 30000, 'outside': 20000, 'boundary': 70}`
- `INDIFFERENCE-TRIGGER AUDIT PASS`
- alternative-equilibrium diagnostic:
  120 parameter draws × 21 starts,
  zero alternative equilibria found in either regime;
- `STAGE 4A CLEAN-ROOM ADVERSARIAL CHECKS PASS`.

The alternative-equilibrium diagnostic is explicitly not promoted to a
uniqueness theorem.

## Headline claims certified

### L1 — common-price global best response

For the source's two weighted clipped affine demand segments, the
both-interior FOC candidate is globally optimal exactly when the possible
high-segment-only deviation cannot dominate it.

Certificate:

`audit/certificates/CERT_L1_COMMON_PRICE_GLOBAL_BR.md`

State: `PASS`.

### P1 — HBP displayed-profile validity

For `0<theta<1` the displayed HBP profile is a global Nash equilibrium on

`-3 tau + [(4-theta+3 sqrt(theta))/4] sigma <= Delta c`

and

`Delta c <= 3 tau - [(1-theta)/2] sigma`.

Certificate:

`audit/certificates/CERT_P1_HBP_VALIDITY.md`

State: `PASS`.

### P2 — uniform displayed-profile validity

The displayed uniform profile is a global Nash equilibrium iff

`-3 tau + [(2+theta+3 sqrt(theta))/2] sigma <= Delta c`

and

`Delta c <= 3 tau - [(1-theta+3 sqrt(1-theta))/2] sigma`

for the displayed candidate construction.

Certificate:

`audit/certificates/CERT_P2_UNIFORM_VALIDITY.md`

State: `PASS`.

### P3 — comparison-domain containment

`D_U subseteq D_HBP`, hence

`D_compare=D_U`.

Certificate:

`audit/certificates/CERT_P3_DOMAIN_CONTAINMENT.md`

State: `PASS`.

### P4 — corrected welfare

For the displayed equilibria on `D_compare`,

`CS^u-CS^d = 3 theta(1-theta)sigma^2/(16 tau)`

`pi_A^d-pi_A^u = theta(1-theta)sigma^2/(8 tau)`

`pi_B^d-pi_B^u = 0`

and

`W^d-W^u = -theta(1-theta)sigma^2/(16 tau)`.

Certificate:

`audit/certificates/CERT_P4_WELFARE.md`

State: `PASS`.

## Quantifier and scope audit

Certified:

- global unilateral best-response validity of the displayed profiles on the
  stated domains;
- necessary/sufficient global-validity conditions for the displayed uniform
  candidate;
- exact containment of the displayed-candidate domains;
- welfare accounting for the displayed equilibria.

Not certified and not claimed:

- uniqueness of the full pure-strategy equilibrium correspondence;
- nonexistence or classification of every outside-branch equilibrium;
- selection-invariant welfare at all equality-boundary equilibria;
- welfare ranking for arbitrary equilibria outside `D_compare`.

This distinction is mandatory in the eventual manuscript.

## Boundary / indifference audit

The weak domain boundaries can create tied best responses.

Stage 4A explicitly changed the indifferent player's action to the tied
high-only price and recomputed the opponent's global best response.

At the audited lower uniform boundary, B's tied new-only action changes A's
best response.

At the audited upper uniform boundary, A's tied old-only action changes B's
best response.

Therefore tied actions are not dismissed as irrelevant. This blocks any
unqualified uniqueness or selection-invariance claim at weak boundaries.

The displayed candidate itself remains a Nash equilibrium at the certified weak
bounds.

## Alternative-equilibrium audit

Because the headline result is an **existence/validity statement for the
displayed profile**, not a uniqueness statement, a full equilibrium
correspondence is not required for certification.

Nevertheless Stage 4A conducted a diagnostic search:

- 120 strict-domain parameter draws;
- 21 dispersed initial prices per draw;
- deterministic global-best-response dynamics;
- both HBP and uniform regimes;
- zero alternative fixed points found.

This is supporting evidence only. It is not an analytic proof of uniqueness.

If a later manuscript draft uses words such as "unique equilibrium" or makes a
selection-free welfare claim, this certificate becomes insufficient and the
project must reopen Stage 4/4A.

## Strategy-domain audit

The frozen source does not explicitly define whether price strategies are
`R`, `R_+`, or another set.

Canonical theorem interpretation remains the real-price game.

For nonnegative-price strategy sets, the same certification applies when
candidate prices and the relevant deviations are feasible; in particular,
nonnegative marginal costs together with the certified positive-markup regular
domain provide the economically standard case.

The eventual paper must state this source ambiguity rather than attribute an
unstated price domain to GSS (2011).

## Counterexample certificate

Permanent exact regression cases:

1. HBP entrant global-deviation failure:
   gain `3281/230400>0`.
2. Uniform entrant new-only deviation:
   gain `89/14400>0`.
3. Uniform incumbent old-only deviation:
   gain `89/14400>0`.

All remain in CI.

These establish that strict candidate cohort interiority alone is not a global
Nash certificate.

## Numerical audit

Purpose:
global-deviation falsification and boundary stress testing after symbolic
derivation.

Seed:
`40420260920`.

Final direct global attack:

- strict inside-domain draws: 30,000;
- just-outside uniform-bound attacks: 20,000;
- exact/near boundary checks: 70;
- unresolved solver calls: 0;
- numerical failures: 0.

The direct evaluator enumerates breakpoints and feasible quadratic vertices; it
does not interpret branch failure as an unprofitable deviation.

Numerical evidence is not used as the analytic proof of P1–P4.

## Formal-verification applicability

Decision:

`FORMALIZATION APPLICABLE`.

Preliminary target map:

`audit/STAGE_04A_FORMALIZATION_TARGET_MAP.md`.

High-value formal targets include:

- exhaustive common-price piecewise globality;
- P1/P2 threshold equivalences;
- P3 domain containment;
- P4 welfare identity;
- exact counterexamples.

No formal-verification `PASS` is claimed at Stage 4A. Implementation remains
required before theory freeze under the workflow's Stage 7.5A formal gate.

## Failed-run record

Two intermediate CI runs failed while building the independent verifier.

Both failures were implementation-level SymPy assertion issues:

1. attempting to coerce a symbolic relational expression into a Python
   Boolean;
2. using structural equality for two algebraically equivalent derivative
   expressions.

Neither exposed a counterexample or changed a theorem statement.

The final implementation replaces those assertions with exact algebraic
identity checks and passes the complete clean-room suite.

The failed runs are intentionally not hidden because they are part of the
audit trail.

## Maximum defensible paper scope after Stage 4A

Allowed:

> The displayed HBP and uniform-pricing formulas are global Nash equilibria on
> explicitly characterized domains; the uniform domain is the common
> comparison domain; on that domain the source welfare ranking reverses after
> correcting consumer surplus.

Not allowed:

> The complete game has a unique equilibrium everywhere.

Not allowed:

> Uniform pricing is welfare-superior under every possible equilibrium
> selection for all source parameters.

## Canonical decision

`GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS -> STAGE 6`

No Stage-5 model hardening is authorized or necessary on the current evidence.
