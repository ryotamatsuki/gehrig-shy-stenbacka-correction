# Note N3 — Independent Referee Attack

## Referee posture

This stage reviews the complete N2 manuscript adversarially as a skeptical
industrial-organization / theory referee. Earlier project conclusions are not
treated as dispositive.

The attack covers:

- mathematical correctness;
- global-equilibrium scope;
- boundary/multiplicity language;
- welfare accounting;
- source/version attribution;
- literature and bibliography accuracy;
- novelty positioning;
- overclaiming;
- whether the result is material enough for a standalone correction /
  reassessment note.

## Independent mathematical recheck

Independent artifact:

`code/n3_independent_referee_recheck.py`.

It does not import Stage-1, Stage-4, or Stage-4A derivation modules.

It reconstructs:

1. consumer surplus directly from primitive utility integrals;
2. incumbent and entrant profit differences;
3. total-welfare difference;
4. the HBP entrant common-price threshold reduction;
5. the uniform entrant lower threshold;
6. the uniform incumbent upper threshold.

Independent symbolic results:

`CS^u-CS^d = 3 theta(1-theta)sigma^2/(16 tau)`

`pi_A^d-pi_A^u = theta(1-theta)sigma^2/(8 tau)`

`pi_B^d-pi_B^u = 0`

`W^d-W^u = -theta(1-theta)sigma^2/(16 tau)`.

The independently reconstructed threshold gaps reduce to the same square-root
bounds used in Proposition 1.

Verdict on the frozen theorem core:

`NO MATHEMATICAL REOPEN TRIGGER FOUND`.

## Referee findings

### R1 — Strategy-set ambiguity missing from manuscript

Severity: `MATERIAL PRESENTATION / SCOPE`.

Problem:
N1 explicitly required the manuscript to disclose that the complete source
draft does not state whether prices are chosen from `R`, `R_+`, or another
strategy set. The N2 manuscript omitted this qualification.

Risk:
a referee could read the global-Nash theorem as attributing an unstated
strategy domain to the source or as silently switching between real and
nonnegative prices.

Resolution:
the model section now states:

- the canonical theorem is for the real-price game;
- for a nonnegative-price strategy set, the same deviation conditions apply
  when candidates and relevant deviations are feasible;
- the source ambiguity is not imputed away.

Status: `RESOLVED`.

### R2 — Central factor-three correction was asserted without showing the
primitive integral

Severity: `MATERIAL EXPOSITION`.

Problem:
the central consumer-surplus correction is the headline arithmetic result, but
the N2 draft jumped from the primitive model directly to the corrected
identity.

Risk:
a skeptical referee should be able to audit the factor-three correction from
the manuscript itself without relying on repository code.

Resolution:
the welfare section now displays the full old/new-cohort consumer-surplus
integral and explains that substitution of the displayed HBP and uniform
profiles yields Proposition 2.

Status: `RESOLVED`.

### R3 — Generic common-price lemma proof too compressed

Severity: `MATERIAL PROOF EXPOSITION`.

Problem:
the N2 proof asserted that lower-price branches cannot dominate and that the
high-only branch is the only competing upper local maximum, but the derivative
logic was compressed enough to invite a branch-exhaustiveness objection.

Resolution:
the proof now explicitly uses:

- continuity and piecewise-quadratic profit;
- positivity of the derivative below the both-interior vertex;
- the direction of derivative jumps at full-to-interior transitions;
- exclusion of negative-markup deviations;
- the zero-demand transition of the lower-threshold cohort;
- the high-only quadratic and its peak;
- branch-infeasible high-only vertex handling.

The repository's independent Stage-4A enumerator remains the machine-readable
exhaustiveness certificate.

Status: `RESOLVED`.

### R4 — Bibliography contained incorrect author metadata

Severity: `MATERIAL SOURCE ACCURACY`.

Two errors were found by independent bibliographic verification:

1. Shy, Stenbacka & Zhang (2016):
   the third author is **David Hao Zhang**, not Zhewei Zhang.
2. Chen, Shi & Zhang (2026):
   the authors are **Yanlin Chen, Xianwen Shi, and Jun Zhang**.

The 2026 paper is
*Welfare of Competitive Price Discrimination with Captive Consumers*,
American Economic Journal: Microeconomics 18(3), 203–243,
DOI `10.1257/mic.20230234`.

Resolution:
`paper/references.bib` corrected.

Status: `RESOLVED`.

### R5 — Draft-versus-published attribution needed sharper separation

Severity: `MATERIAL SOURCE ATTRIBUTION`.

Problem:
the equation-level factor-three finding is based on the complete 14 December
2009 author draft, whereas the project has not directly inspected the VOR
equations line by line.

Independent public-record check:
the published article record and publisher abstract continue to state that the
incumbent's HBP profit gain exceeds the associated consumer loss.

Resolution:
the source-version paragraph now distinguishes:

- exact missing-factor attribution: complete author draft;
- disputed welfare headline: also present in the published article record;
- no claim of line-by-line VOR-equation inspection.

Status: `RESOLVED`.

### R6 — Entry-invariance implication could be misread as attacked

Severity: `MINOR BUT IMPORTANT SCOPE`.

Problem:
because the manuscript corrects welfare and global-equilibrium scope, a reader
might infer that it also disproves the source's entry-invariance result.

Resolution:
the conclusion now states explicitly that the entrant-profit equality survives
on the common displayed branch. The note does not claim the entry result false;
entry conclusions remain conditional on the validity of the compared
equilibria and the source's entry-cost comparison.

Status: `RESOLVED`.

### R7 — Welfare table duplicated identical information

Severity: `MINOR PRESENTATION`.

Problem:
the N2 table contained two numerical columns carrying the same coefficient.

Resolution:
reduced to one coefficient column in units of
`theta(1-theta)sigma^2/tau`.

Status: `RESOLVED`.

### R8 — Internal formal-checker record mismatch

Severity: `AUDIT-HYGIENE`.

Problem:
the early N1 text still named `nanoda` even though the certified successful
formal run used `leanchecker` plus Lean build, axiom audit, and placeholder
rejection.

Resolution:
N1 audit text aligned with the successful certified run. No theorem or claim
scope changed.

Status: `RESOLVED`.

## Boundary and multiplicity attack

The revised manuscript does not say:

- "unique equilibrium";
- "no equilibrium exists outside the domain";
- "the welfare ranking holds under every equilibrium selection".

It states that weak-boundary ties may occur and that the displayed candidate
remains the object being certified.

This is consistent with the Stage-4A indifference-trigger audit.

Verdict:

`PASS`.

## Welfare attack

Independent primitive integration reproduces the factor-three consumer-surplus
difference.

Independent substitution reproduces:

- incumbent gain: `+2/16`;
- consumer change under HBP relative to uniform: `-3/16`;
- entrant change: `0`;
- total welfare: `-1/16`;

all in units of `theta(1-theta)sigma^2/tau`.

The resource decomposition is internally coherent:

- transportation cost: `-3/16`;
- switching cost: `+4/16`;
- resource cost: `+1/16`.

The manuscript appropriately conditions the resource interpretation on
`sigma` representing real switching disutility/resource loss rather than a
pure transfer.

Verdict:

`PASS`.

## Novelty / absorption attack

The manuscript does not claim generic novelty for piecewise-affine pricing.

It positions itself against distinct neighboring literatures:

- asymmetric no-discrimination constraints;
- both-firms-discriminate HBP models;
- dynamic HBP;
- richer information-design welfare models.

No located prior result directly supplies both the source-specific
global-validity domains and the within-GSS welfare correction.

The contribution is therefore defensible only as:

`SOURCE-SPECIFIC CORRECTION / REASSESSMENT`.

That is exactly how the revised manuscript is framed.

Verdict:

`PASS WITH NARROW POSITIONING`.

## Materiality attack

A standalone note would be weak if it merely corrected one coefficient with no
effect on a substantive conclusion.

That is not the case here.

The note contains two independent corrections:

1. a welfare accounting error that reverses the published welfare headline on
   the certified common domain;
2. a global-equilibrium-scope defect showing that strict interiority of the
   displayed cohort shares is not enough for Nash equilibrium, together with
   exact validity domains and exact finite deviations.

The real-resource decomposition further explains why the sign reversal is
economic rather than cosmetic.

Referee assessment:

`SUFFICIENTLY MATERIAL FOR A COMPACT CORRECTION / REASSESSMENT NOTE`.

This does not imply acceptance at any particular journal; venue fit is deferred
to N4.

## Remaining non-blocking limitations

These are not N3 failures, but must remain visible:

- VOR equations have not been inspected line by line;
- no full outside-branch equilibrium correspondence is supplied;
- no game-wide uniqueness theorem is supplied;
- no endogenous regime-choice or policy theorem is supplied;
- the current note is source-specific rather than a general theory paper.

## CI closure requirement

N3 may close only after the revised manuscript passes:

- manuscript LaTeX/PDF CI;
- existing Stage 1 / Stage 4 / Stage 4A / Stage 7 regressions;
- the new independent N3 symbolic recheck;
- Lean build / independent checker / axiom audit / placeholder rejection.

Current verdict pending final revised-source CI:

`CONDITIONAL PASS — REVISIONS COMPLETE, CI CONFIRMATION PENDING`.
