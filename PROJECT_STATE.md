# Project State

## Canonical identity

- Repository: `ryotamatsuki/gehrig-shy-stenbacka-correction`
- Canonical branch: `main`
- Workflow: `research-paper-workflow` v2.3
- Workflow commit: `9eb616bd31ea3a9ef3c29e288228ed962c44c9cf`
- Target: Thomas Gehrig, Oz Shy, and Rune Stenbacka (2011),
  “History-based Price Discrimination and Entry in Markets with Switching
  Costs: A Welfare Analysis,” *European Economic Review* 55(5), 732–739.
- DOI: `10.1016/j.euroecorev.2010.09.001`

## Provenance

Parent clean-room audit:

- Repository: `ryotamatsuki/ozshypapers`
- Branch: `final-cleanroom-theorem-audit-20260919`
- Historical correction workspace:
  `correction/history-based-entry-welfare-2011`

The parent audit classified the target as
`FINAL_AUDITED_MATERIAL_ERROR`. This repository does not rely on that label
as proof; Stage 1 independently rechecks the proof-critical mathematics.

## Current canonical state

| Stage | State |
|---|---|
| Stage 0 — Idea / Motivation Intake | **GO** |
| Stage 1 — Source & Mathematical Audit | **GO** |
| Stage 2 — Literature Frontier / Novelty Kill Gate | **GO** |
| Stage 3 — Candidate Mechanism Search | **GO — Architecture B selected** |
| Stage 4 — Minimal Model Gate | **GO** |
| Stage 4A — Independent Mathematical Adversarial Certification | **GO — PASS** |
| Stage 5 — Mechanism Hardening | **NOT TRIGGERED** |
| Stage 6 — Novelty Re-Kill | **GO** |
| Stage 7 — Welfare / Generality / Institutional Validation | **NOT STARTED — next** |
| Stage 7.5+ | **NOT STARTED** |

## Early-repository exception

This dedicated repository was initialized before Stage 8/9 by explicit project
decision to separate the correction paper from the omnibus Oz Shy audit.

This administrative initialization does **not** constitute Stage 9
Repository/Reproducibility certification. The canonical workflow gates remain
unchanged, and manuscript construction is not yet authorized.

## Surviving contribution set after Stage 2

1. Correct the consumer-surplus calculation and resulting welfare comparison.
2. Establish exact parameter restrictions under which the displayed interior
   pricing formulas are global Nash equilibria.
3. Derive additional active-set equilibrium correspondence only if needed for
   the correction and justified by Stage 3/4.
4. Treat the `Delta c` prose sign error as ancillary.

## Claims currently prohibited

- Do not claim equation-by-equation inspection of the 2011 VOR body until the
  VOR itself is directly verified.
- Do not claim that entry invariance is false; the interior entrant-profit
  identity survives the current audit.
- Do not claim a new general theory of history-based pricing.
- Do not state a global equilibrium theorem before Stage 4/4A certification.
- Do not extend welfare or policy claims beyond the exact certified model and
  parameter domain.


## Stage 3 architecture decision

Selected paper architecture: corrected welfare accounting plus exact
global-equilibrium validity conditions for the source's displayed HBP and
uniform-pricing interior candidates.

The full pure-price equilibrium correspondence is supporting work only unless
Stage 4 proves it is necessary for an exact validity characterization.


## Stage 4 solved object

The displayed uniform-pricing equilibrium has the exact global-validity domain

`-3 tau + [(2+theta+3 sqrt(theta))/2] sigma <= Delta c <= 3 tau - [(1-theta+3 sqrt(1-theta))/2] sigma`.

This domain is contained in the displayed HBP candidate's global-validity
domain, so it is also the common comparison domain.  The corrected welfare
identity on that domain is

`W^d-W^u = -theta(1-theta)sigma^2/(16 tau)`.

All Stage-4 propositions remain candidate theorems pending Stage 4A independent
adversarial certification.


## Stage 4A certification

Independent clean-room certification passed at commit
`a99e375e09a65fc0cfd0839876c4e13545a834cf`, workflow run
`35491396515`.

All headline Stage-4 candidate propositions have individual PASS certificates
under `audit/certificates/`.

Formal verification is `APPLICABLE`; the preliminary target map is recorded
at `audit/STAGE_04A_FORMALIZATION_TARGET_MAP.md`. Formal implementation is
still required before theory freeze.


## Stage 6 novelty re-kill

The generic piecewise-affine/common-price best-response machinery is not a
novelty claim.

Surviving contribution:
- source-specific P1/P2 global-validity domains;
- P3 common-domain containment;
- P4 factor-three consumer-surplus correction and welfare reversal.

No located parent theorem directly absorbs the correction as a short corollary.
The current frontier includes Chen, Shi & Zhang (2026), which reinforces that
P4 must be stated as a GSS-model correction rather than a general welfare
theorem about price discrimination.
