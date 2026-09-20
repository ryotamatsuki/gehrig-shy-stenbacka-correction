# Stage 4A Formal Verification Applicability and Target Map

## Applicability decision

`FORMALIZATION APPLICABLE`

Reason: the correction depends materially on piecewise/clipped demand,
global-deviation inequalities, square-root threshold ordering, boundary cases,
exact counterexamples, and a welfare identity whose failure reverses the
published headline. These are precisely the proof-critical objects for which a
small formal core can add assurance.

This Stage-4A decision is **not** a formal-verification pass. Implementation is
deferred to the workflow's formal-verification gate before theory freeze.

## Preliminary target map

| Claim ID | Paper claim | Proof-critical component | Formalization target | Explicitly excluded at first pass | Assurance gain |
|---|---|---|---|---|---|
| L1 | common-price global BR | exhaustive piecewise cases and comparison with high-only branch | prove branch-exhaustive maximizer condition for weighted two-segment clipped affine demand | full economic interpretation | closes fragile globality step |
| P1 | HBP displayed-profile validity | entrant global-deviation threshold + incumbent one-segment bounds | derive equivalence between P1 inequalities and all unilateral-BR conditions | full outside equilibrium correspondence | certifies exact domain |
| P2 | uniform displayed-profile validity | B new-only and A old-only deviation thresholds | prove both necessary/sufficient inequalities | uniqueness of the full game | certifies exact common-price globality |
| P3 | domain containment | ordering of lower/upper bounds | exact real-inequality proof of `D_U subseteq D_HBP` | none material | low-cost high-value scope check |
| P4 | welfare correction | CS factor 3 and welfare cancellation | exact algebra/integration-equivalent identities from displayed formulas | welfare of alternative equilibria | protects headline sign |
| CE1–CE3 | exact counterexamples | rational/real arithmetic profit improvement | formally evaluate candidate and deviation profits and prove positive gain | numerical search | permanent falsification certificates |

## Model boundary for intended formalization

Planned to formalize:
- normalized displayed price formulas;
- clipped two-segment demand algebra or an equivalent exhaustive piecewise
  representation;
- global-BR inequalities for the displayed candidates;
- containment and threshold ordering;
- exact counterexamples;
- welfare identities.

Not initially claimed as formally certified:
- a complete equilibrium correspondence outside the displayed branches;
- game-wide uniqueness;
- citation/literature claims;
- Version-of-Record textual identity;
- economic interpretation of every boundary selection.

## Recommended tool

Lean 4 + mathlib, with toolchain pinned when implementation begins.

## Rollback rule

If formalization exposes a missing branch, missing assumption, wrong inequality
direction, or theorem/domain mismatch, reopen Stage 4/4A. Do not weaken the
formal theorem merely to make it compile.
