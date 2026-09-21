# Replication package manifest

This directory-level manifest defines the supplementary verification material
for the compact correction / reassessment note.

## Economic reconstruction and global-deviation checks

- `code/stage04a_cleanroom_adversarial.py`
  - independent primitive clipped-payoff reconstruction;
  - piecewise-quadratic unilateral-deviation enumeration;
  - exact validity thresholds and counterexamples.

- `code/stage07_welfare_decomposition.py`
  - transportation-cost and switching-cost decomposition;
  - welfare accounting checks.

- `code/n3_independent_referee_recheck.py`
  - independent manuscript-facing re-derivation of consumer surplus, profits,
    welfare, and threshold reductions;
  - does not import the Stage-1/4/4A derivation modules.

## Formal verification

- `formal/GSSCorrection.lean`
- `lean-toolchain`
- `lakefile.lean`
- `lake-manifest.json`

The Lean development verifies the proof-critical algebraic reductions, domain
containment, welfare identities/sign, and exact rational counterexamples. It
does not claim to formalize the entire economic game, branch exhaustiveness,
full equilibrium correspondence, or uniqueness.

## Audit certificates

Supporting human-readable certificates are in:

- `audit/certificates/`
- `audit/STAGE_04A_INDEPENDENT_ADVERSARIAL_CERTIFICATION.md`
- `audit/NOTE_N3_INDEPENDENT_REFEREE_ATTACK.md`

## Reproducibility boundary

The manuscript's replication statement is intentionally narrower than
"fully formalized paper":

`primitive economic reconstruction -> clean-room global-deviation audit -> targeted Lean verification`.

The source/version and literature claims remain documentary rather than
Lean-certified.
