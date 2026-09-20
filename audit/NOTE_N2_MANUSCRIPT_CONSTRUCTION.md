# Note N2 — Manuscript Construction

## Purpose

Construct a compact correction / reassessment note from the N1-frozen claim set.

## Manuscript artifacts

- `paper/manuscript.tex`
- `paper/references.bib`
- `paper/CLAIM_MAP.md`

## Architecture

1. Introduction / correction statement.
2. Model and displayed price profiles.
3. Global-validity correction.
4. Consumer-surplus and welfare correction.
5. Real-resource interpretation.
6. Scope and conclusion.
7. Technical appendices.

## Main-text theorem architecture

- Proposition 1: global validity of the displayed HBP and uniform profiles.
- Corollary 1: `D_U subseteq D_HBP` and common comparison domain.
- Example 1: exact HBP global-deviation counterexample.
- Proposition 2: corrected consumer-surplus, profit, and welfare identities.
- Resource decomposition: transportation-cost saving versus switching-cost loss.

## Scope discipline

The draft explicitly does not claim:

- full equilibrium uniqueness;
- absence of equilibria outside the displayed validity domains;
- selection-invariant boundary welfare;
- general welfare dominance of uniform pricing;
- an endogenous policy or regime-choice result;
- line-by-line VOR equation verification.

The equation-level source statement is restricted to the complete 14 December
2009 author draft.

## Reproducibility integration

The technical appendix links the manuscript logic to the layered verification:

1. primitive-demand reconstruction;
2. Stage-4A clean-room global-deviation audit;
3. targeted Lean 4 algebra/kernel certification.

## Literature positioning

The introduction treats the contribution as source-specific and distinguishes
the correction from:

- asymmetric no-discrimination models;
- settings where both firms discriminate;
- dynamic history-based pricing;
- richer information-design welfare results.

No generic piecewise-affine pricing theorem is claimed as a contribution.

## N2 compile gate

Workflow:

`.github/workflows/paper.yml`

Required:

- `paper/manuscript.tex` compiles successfully with bibliography;
- `paper/manuscript.pdf` is generated in CI.

Current state:

`PASS — MANUSCRIPT CONSTRUCTED`.

## Exit

After a green compile and final source/claim-map consistency check:

`PASS — MANUSCRIPT CONSTRUCTED -> N3 INDEPENDENT REFEREE ATTACK`.

## Compile closure evidence

Workflow run: `35500470176`.

Result: `success`.

The CI completed both the LaTeX compilation step and the explicit `paper/manuscript.pdf` existence check.

## N2 canonical verdict

`PASS — MANUSCRIPT CONSTRUCTED`.

Routing: `N3 — INDEPENDENT REFEREE ATTACK`.
