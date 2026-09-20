# Note N1 — Claim-Scope Ledger

## Purpose

Freeze the maximum defensible claim set for the compact correction /
reassessment note before manuscript construction.

This ledger is authoritative unless a later mathematical change explicitly
reopens N1 and the affected Stage-4A/Stage-7 certifications.

## C0 — Source relationship

### Allowed

- The complete mathematical reconstruction is anchored to the 14 December 2009
  author draft.
- The current publisher abstract preserves the disputed welfare headline.
- No correction addressing the certified errors was located in the searches
  recorded at Stages 2 and 6.

### Prohibited

- Do not say the 2011 Version-of-Record equations were checked line by line.
- Do not attribute a particular VOR equation number to the factor-three error
  until the VOR body itself is obtained and inspected.

## C1 — Displayed HBP equilibrium validity

### Formal claim

For `0<theta<1`, `tau>0`, `sigma>=0`, the displayed HBP price profile is
a global Nash equilibrium on the certified displayed-candidate domain

`-3 tau + [(4-theta+3 sqrt(theta))/4] sigma <= Delta c`

and

`Delta c <= 3 tau - [(1-theta)/2] sigma`.

### Evidence

- `audit/certificates/CERT_P1_HBP_VALIDITY.md`
- `code/stage04a_cleanroom_adversarial.py`

### Maximum prose

"The displayed HBP formulas constitute a Nash equilibrium on the stated
global-validity domain."

### Prohibited

- "The HBP game has a unique equilibrium."
- "No equilibrium exists outside the domain."
- "The displayed formulas are globally valid for all source parameters."

## C2 — Displayed uniform equilibrium validity

### Formal claim

For the displayed candidate construction, the uniform-price profile is a
global Nash equilibrium iff

`-3 tau + [(2+theta+3 sqrt(theta))/2] sigma <= Delta c`

and

`Delta c <= 3 tau - [(1-theta+3 sqrt(1-theta))/2] sigma`.

### Evidence

- `audit/certificates/CERT_P2_UNIFORM_VALIDITY.md`
- `code/stage04a_cleanroom_adversarial.py`

### Maximum prose

"The displayed uniform-pricing formulas are globally valid exactly on the
stated displayed-candidate domain."

### Prohibited

- game-wide uniqueness;
- a complete outside-branch equilibrium correspondence.

## C3 — Common comparison domain

### Formal claim

`D_U subseteq D_HBP`, hence the common displayed-equilibrium comparison domain
is

`D_compare=D_U`.

### Evidence

- `audit/certificates/CERT_P3_DOMAIN_CONTAINMENT.md`
- Lean theorem `p3_lower_containment`
- Lean theorem `p3_upper_containment`

### Maximum prose

"The uniform validity region is nested inside the HBP validity region."

## C4 — Consumer surplus correction

### Formal claim

On the displayed equilibria,

`CS^u-CS^d=3 theta(1-theta)sigma^2/(16 tau)`.

The complete 2009 draft reports the same expression without the factor 3.

### Evidence

- Stage 1 direct primitive integration;
- Stage 4A independent reconstruction;
- P4 certificate.

### Maximum prose

"Direct integration yields a factor three missing from the complete author
draft's reported consumer-surplus difference."

### Prohibited

- a VOR equation-number claim without VOR-body inspection.

## C5 — Welfare correction

### Formal claim

On `D_compare`,

`W^d-W^u=-theta(1-theta)sigma^2/(16 tau)`.

For `0<theta<1`, `sigma>0`, `tau>0`, the displayed uniform equilibrium
has strictly higher total welfare.

### Evidence

- `audit/certificates/CERT_P4_WELFARE.md`
- `code/stage07_welfare_decomposition.py`
- Lean theorems `p4_welfare_accounting` and `p4_welfare_negative`

### Maximum prose

"On the common certified domain, the paper's displayed-equilibrium welfare
ranking reverses."

### Prohibited

- "uniform pricing is generally welfare superior";
- welfare claims for every possible outside-branch or boundary equilibrium.

## C6 — Real-resource decomposition

### Formal claim

`TC^d-TC^u=-3 theta(1-theta)sigma^2/(16 tau)`

and

`SC^d-SC^u=4 theta(1-theta)sigma^2/(16 tau)`.

Thus HBP raises total real resource cost by

`theta(1-theta)sigma^2/(16 tau)`.

### Interpretation

HBP improves spatial matching but induces enough additional switching to more
than offset that gain.

### Scope condition

The switching-cost term must represent real utility/resource loss. A pure
monetary exit fee may be partly a transfer and does not map one-for-one to this
welfare interpretation.

## C7 — Profit / distributional result

### Formal claim

`pi_A^d-pi_A^u=theta(1-theta)sigma^2/(8 tau)`

`pi_B^d-pi_B^u=0`.

The incumbent recovers exactly two thirds of the consumer loss.

### Prohibited

Do not infer endogenous over-adoption of HBP. Regime choice is exogenous in the
source model.

## C8 — Counterexamples

Permanent exact regression cases:

1. HBP entrant global deviation gain:
   `3281/230400>0`.
2. Uniform entrant high-price/new-only deviation gain:
   `89/14400>0`.
3. Uniform incumbent high-price/old-only deviation gain:
   `89/14400>0`.

### Meaning

Strict candidate cohort interiority does not by itself certify global Nash.

### Formal evidence

Lean theorems `ce1_hbp_gain`, `ce2_uniform_entrant_gain`,
`ce3_uniform_incumbent_gain`.

## C9 — Boundary / multiplicity language

Weak validity boundaries can contain tied best responses that change the
opponent's best response.

Therefore:

- existence of the displayed equilibrium at a weak boundary is allowed;
- uniqueness and selection-invariant welfare at weak boundaries are not
  claimed.

## C10 — Strategy-set ambiguity

The frozen source does not explicitly specify `R` versus `R_+` for price
strategies.

Canonical analysis:

- real-price game;
- nonnegative-price interpretation only when displayed candidates and relevant
  deviations are feasible.

The note must state the ambiguity rather than silently impute a source
assumption.

## C11 — Novelty

### Allowed

- source-specific exact equilibrium-validity correction;
- source-specific consumer-surplus/welfare correction;
- economic resource-cost interpretation.

### Not claimed as novelty

- generic piecewise-affine global optimization;
- generic common-price segmented Bertrand theory;
- a general welfare theorem for personalized/history-based pricing.

## C12 — Institutional interpretation

Primary regulatory evidence supports the plausibility of:

- history/data-conditioned pricing;
- existing/new customer price differentiation;
- switching frictions.

It does not structurally validate the GSS model or its parameterization.

## Frozen note-level theorem architecture

Recommended main-text structure:

- Proposition 1: exact validity domains for the displayed HBP and uniform
  profiles;
- Corollary 1: `D_U subseteq D_HBP` and `D_compare=D_U`;
- Example 1: exact HBP global-deviation counterexample;
- Proposition 2: corrected consumer-surplus, profit and welfare identities;
- Corollary 2 / decomposition: transportation-cost gain versus switching-cost
  loss.

The generic common-price lemma belongs in the proof/appendix and is not a
contribution claim.

## Reopen rule

Reopen N1 and the earliest affected analytic gate if:

- a theorem/domain changes;
- VOR inspection changes source attribution materially;
- a new equilibrium correspondence is added;
- a new generality/policy claim is introduced;
- formal verification reveals a statement-fidelity defect.
