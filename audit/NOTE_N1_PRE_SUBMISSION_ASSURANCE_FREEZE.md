# Note N1 — Pre-submission Assurance / Theory Freeze

## Route

Project class:

`COMPACT CORRECTION / REASSESSMENT NOTE`.

This note-specific route follows the Stage-7.5 full-theory `NO-GO` decision.
It does not retroactively mark full-theory Stage 7.5A or Stage 8 as passed.

## N1 objectives

Before manuscript construction:

1. freeze the theorem/claim set;
2. preserve exact source/version limitations;
3. complete targeted formal verification of the proof-critical correction core;
4. retain independent Stage-4A global-deviation certification;
5. prohibit unsupported uniqueness, generality, and policy language;
6. define explicit reopen rules.

## Frozen mathematical core

The note is restricted to the certified GSS model and the following objects:

- P1: displayed HBP global-validity domain;
- P2: displayed uniform global-validity domain;
- P3: domain containment and common comparison domain;
- P4: corrected CS/profit/welfare identities;
- Stage-7 real-resource welfare decomposition;
- CE1–CE3 exact global-deviation counterexamples.

No complete outside-branch equilibrium atlas is part of the frozen note.

## Claim-scope authority

`audit/NOTE_N1_CLAIM_SCOPE_LEDGER.md`.

Any manuscript sentence stronger than that ledger is prohibited unless N1 is
reopened.

## Formal verification target

Formal source:

`formal/GSSCorrection.lean`.

Toolchain:

`leanprover/lean4:v4.35.0-rc2`.

Mathlib:

commit `b1007d8abfd0c776eb8a75e8f6bf26db5eae4a69`.

### Formally encoded

- algebraic reduction of the HBP entrant high-only comparison to the P1 lower
  threshold;
- algebraic reduction of the uniform entrant comparison to the P2 lower
  threshold;
- algebraic reduction of the uniform incumbent comparison to the P2 upper
  threshold;
- necessity/sufficiency of those threshold inequalities for the corresponding
  comparison gaps on the regular `sqrt(weight)<1` domain;
- P3 lower/upper domain containment;
- P4 welfare accounting identity;
- P4 resource decomposition identity;
- strict negativity of the P4 welfare gap for interior positive parameters;
- CE1–CE3 exact rational profit improvements.

### Explicitly outside the Lean model

- derivation of consumer demand from utility primitives;
- proof that the Stage-4A branch partition is exhaustive;
- full game-level Nash definition;
- full equilibrium correspondence;
- uniqueness;
- source/version/citation facts;
- institutional interpretation.

Those components remain certified by Stage 1/4A/6/7 evidence rather than being
misrepresented as Lean-certified.

## Independent economic certification retained

Lean does not replace:

`code/stage04a_cleanroom_adversarial.py`.

That artifact independently reconstructs primitive clipped payoffs, enumerates
all unilateral piecewise branches, attacks boundaries, and preserves exact
counterexamples.

The note's assurance architecture is deliberately layered:

`primitive economic reconstruction -> clean-room global-deviation audit -> Lean algebra/kernel checks`.

## CI formal-verification requirements

The repository workflow must require:

- Lean build success;
- axiom audit;
- independent Lean environment checking via nanoda;
- no `sorry` or `admit` placeholders;
- existing Python/SymPy and clean-room regressions.

## N1 exit rule

N1 may be marked `PASS — NOTE THEORY FROZEN` only after the Lean CI job is
green and its build/axiom evidence is recorded in a formal-verification
certificate.

Until then the state is:

`PASS — NOTE THEORY FROZEN`.

## Post-N1 route

After N1 PASS:

- N2 — Manuscript Construction
- N3 — Independent Referee Attack
- N4 — Journal Positioning
- N5 — Full-note Integration
- N6 — Submission QA
- N7 — Submission Freeze

## Formal-verification closure evidence

Certified workflow run: `35500192212`.

Certified commit: `044528e123a5058efc633e2e6241f24a2c6a4769`.

The run passed Lean build, `leanchecker` independent environment checking, axiom audit, no `sorry`/`admit` placeholders, and all Python/SymPy clean-room regressions through Stage 7.

Current `formal/GSSCorrection.lean` has the same Git blob SHA as the certified source: `fa5b8d1dba6a6b8f25bdb0916bfd8bca1b33fe82`.

## N1 canonical verdict

`PASS — NOTE THEORY FROZEN`.

Routing: `N2 — MANUSCRIPT CONSTRUCTION`.
