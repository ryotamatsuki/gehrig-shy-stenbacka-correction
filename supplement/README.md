# Research in Economics — supplementary verification package

This manifest defines the material intended for external submission with the
correction / reassessment manuscript. Internal editorial-strategy and workflow
memos are deliberately excluded from the submission supplement.

## Include in the submission supplement

### Economic reconstruction and global-deviation checks

- code/stage01_independent_recheck.py
  - independent reconstruction of the displayed prices, shares, profits,
    primitive consumer surplus, welfare, and CE1.

- code/stage04_global_validity.py
  - exact displayed-profile global-validity thresholds and CE1–CE3 regressions.

- code/stage04a_cleanroom_adversarial.py
  - independent primitive clipped-payoff reconstruction;
  - exhaustive piecewise-quadratic unilateral-deviation enumeration;
  - boundary / indifference-trigger audit.

- code/stage07_welfare_decomposition.py
  - transportation-cost and switching-cost decomposition.

- code/n3_independent_referee_recheck.py
  - independent manuscript-facing reconstruction that does not import the
    Stage-1/4/4A derivation modules.

### Formal verification

- formal/GSSCorrection.lean
- lean-toolchain
- lakefile.lean
- lake-manifest.json

The Lean development verifies proof-critical algebraic reductions, domain
containment, welfare accounting/sign, and the exact rational counterexamples.
It does not formalize the full economic game, branch exhaustiveness, full
equilibrium correspondence, or uniqueness.

### Python dependency provenance

requirements.txt pins sympy==1.14.0.

## Exact permanent regression cases

CE1 — HBP entrant:

- theta = 1/2
- tau = 1
- sigma = 23/10
- c_A = c_B = 0
- displayed prices: p_A = 47/24, q_A = 97/120, p_B = 37/60
- displayed shares: x_o = 47/48, x_n = 97/240
- deviation: p_B' = 217/240
- exact gain: 3281/230400 > 0

CE2 — uniform entrant:

- exact gain: 89/14400 > 0

CE3 — uniform incumbent:

- exact gain: 89/14400 > 0

## Minimal rerun commands

Python:

    python -m pip install -r requirements.txt
    python code/stage01_independent_recheck.py
    python code/stage04_global_validity.py
    python code/stage04a_cleanroom_adversarial.py
    python code/stage07_welfare_decomposition.py
    python code/n3_independent_referee_recheck.py

Lean:

    lake build

The repository CI additionally runs the independent Lean environment checker,
axiom audit, and placeholder rejection.

## Submission boundary

Do not include the full internal audit/ directory as reviewer supplementary
material. It contains workflow history, journal strategy, and referee-attack
records that are useful internally but unnecessary to reproduce the paper's
analytical results.

No publisher PDF or copyrighted Version-of-Record file is included in this
repository or submission supplement.
