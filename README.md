# Gehrig–Shy–Stenbacka (2011) correction / reassessment

Independent reassessment project for:

Thomas Gehrig, Oz Shy, and Rune Stenbacka (2011),
“History-based Price Discrimination and Entry in Markets with Switching Costs:
A Welfare Analysis,” European Economic Review 55(5), 732–739.
DOI: 10.1016/j.euroecorev.2010.09.001.

## Current route

The full-theory route was stopped at Stage 7.5. The project follows the
compact correction / reassessment-note workflow.

Current certified note stages:

- N1 — PASS — NOTE THEORY FROZEN
- N2 — PASS — MANUSCRIPT CONSTRUCTED
- N3 — PASS — INDEPENDENT REFEREE ATTACK RESOLVED
- N4 — PASS — JOURNAL POSITIONING RE-CERTIFIED
- N5 — PASS — FULL-NOTE INTEGRATION COMPLETE
- N6 — Research in Economics submission QA in progress
- N7 — not started

The current formal submission target is Research in Economics by explicit
author decision at N6.

## Frozen headline results

For the displayed HBP profile:

    -3 tau + [(4-theta+3 sqrt(theta))/4] sigma <= Delta c
    <= 3 tau - [(1-theta)/2] sigma

For the displayed uniform-pricing profile:

    -3 tau + [(2+theta+3 sqrt(theta))/2] sigma <= Delta c
    <= 3 tau - [(1-theta+3 sqrt(1-theta))/2] sigma

The uniform displayed-profile domain is contained in the HBP domain. On the
common displayed-equilibrium domain:

- CS^u-CS^d = 3 theta(1-theta) sigma^2/(16 tau)
- pi_A^d-pi_A^u = theta(1-theta) sigma^2/(8 tau)
- pi_B^d-pi_B^u = 0
- W^d-W^u = -theta(1-theta) sigma^2/(16 tau)

The project does not claim game-wide uniqueness, nonexistence outside the
displayed validity domains, a full equilibrium correspondence, or a general
welfare theorem for history-based pricing.

## Source boundary

Equation-level reconstruction is anchored to the complete 14 December 2009
author draft. Published 2011 metadata and the welfare headline in the published
record have been separately checked. The repository does not claim a
line-by-line audit of every Version-of-Record equation.

No publisher PDF is committed.

## Reproducibility

Python/SymPy checks:

    python -m pip install -r requirements.txt
    python code/stage01_independent_recheck.py
    python code/stage04_global_validity.py
    python code/stage04a_cleanroom_adversarial.py
    python code/stage07_welfare_decomposition.py
    python code/n3_independent_referee_recheck.py

Lean:

    lake build

CI additionally performs independent Lean environment checking, an axiom
audit, placeholder rejection, and manuscript PDF QA.

See supplement/README.md for the reviewer-facing verification package.
