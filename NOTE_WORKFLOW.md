# Correction-Note Workflow

This repository follows a note-specific route after the Stage-7.5 decision:

`NO-GO — FULL-THEORY ROUTE`

`COMPACT CORRECTION / REASSESSMENT NOTE — WORTH PURSUING`.

This workflow does not relabel the full-theory Stage 7.5A/8 gates as passed.

## N1 — Pre-submission Assurance / Theory Freeze

Required:

- final claim-scope ledger;
- exact source/version limitations;
- independent Stage-4A global-deviation certification retained;
- targeted Lean formal verification;
- build + axiom audit + independent checker + no placeholders;
- explicit model boundary;
- reopen rules.

Exit:

`PASS — NOTE THEORY FROZEN`.

## N2 — Manuscript Construction

Build a compact theory correction/reassessment note from the frozen N1 claim
set.

Required sections:

1. Introduction / correction statement.
2. Source model and notation.
3. Global-validity correction.
4. Consumer-surplus and welfare correction.
5. Real-resource interpretation.
6. Conclusion / scope.
7. Technical appendix.

No theorem or claim may exceed N1 without reopening the relevant gate.

## N3 — Independent Referee Attack

Adversarially review the complete manuscript as if by a skeptical IO/theory
referee.

Attack:

- correctness;
- source attribution;
- novelty positioning;
- equilibrium globality;
- boundary/multiplicity wording;
- welfare accounting;
- overclaiming;
- whether the note is sufficiently material to publish.

Every material criticism must be resolved or explicitly scoped.

## N4 — Journal Positioning

Choose the best target for the actual note, not the imagined full theory paper.

Compare:

- fit with corrections/comments/short notes;
- article type and length;
- relation to the original journal;
- open manuscript / simultaneous submission restrictions;
- fees;
- expected audience.

Do not select a venue by prestige alone.

## N5 — Full-Note Integration

Integrate referee fixes and journal-specific framing.

Required:

- theorem numbering frozen;
- abstract/introduction/conclusion consistent with N1;
- appendix and formal-verification references aligned;
- figures/tables regenerated from certified code;
- bibliography and source-version statements checked.

## N6 — Submission QA

Final submission audit:

- anonymous/manuscript variants as required;
- title/abstract/keywords/JEL;
- source and DOI accuracy;
- all equations compile;
- all figures/tables reproducible;
- no forbidden claims;
- formal artifacts match certified commit;
- cover letter and disclosure statements.

## N7 — Submission Freeze

Freeze:

- manuscript PDF/source;
- supplementary verification package;
- code;
- Lean source/toolchain/dependency provenance;
- audit trail;
- submission metadata.

Any post-freeze theorem or scope change reopens N1 and downstream note gates as
appropriate.


## Current project checkpoint

Current certified state:

- N1 — `PASS — NOTE THEORY FROZEN`
- N2 — `PASS — MANUSCRIPT CONSTRUCTED`
- N3 — `PASS — INDEPENDENT REFEREE ATTACK RESOLVED`
- N4 — `PASS — JOURNAL POSITIONING RE-CERTIFIED`
- N5 — `PASS — FULL-NOTE INTEGRATION COMPLETE`
- N6 — `CONDITIONAL PASS — AI-POLICY MANUSCRIPT AMENDMENT COMPLETE; AUTHOR TERMS/PRIVACY CONFIRMATION OUTSTANDING`
- N7 — `BLOCKED — AWAIT AUTHOR AI-TOOL TERMS/PRIVACY CONFIRMATION`

Current formal submission target:

`Research in Economics`.

Fallback ladder after RiE: `RIO -> JICT -> Economics Bulletin`; IJIO remains optional stretch and EER optional inquiry.

IJIO is optional stretch; EER is optional inquiry only.

The full-theory route remains unchanged:

- Stage 7.5 — `NO-GO — FULL-THEORY ROUTE`
- Stage 7.5A — not entered
- Stage 8 — blocked under the full-theory workflow.


## N5 closure checkpoint

N5 is closed:

`PASS — FULL-NOTE INTEGRATION COMPLETE`.

RIO-facing manuscript integration is complete and CI-certified.

Next:

`N6 — SUBMISSION QA`.

## N6 closure checkpoint

N6 was re-opened narrowly for the 2026-09-21 Elsevier generative-AI policy check and is now conditionally re-certified:

`CONDITIONAL PASS — MANUSCRIPT AI DISCLOSURE RECERTIFIED`.

The change is disclosure/methodology-only and does not reopen N1 or alter any theorem, domain, counterexample, welfare identity, or formal artifact.

Target-specific package: Research in Economics.

Audited submission-package commit: `0532899eb320e7333d1751542ebedac1f0e41021`.

CI evidence:

- verify run `35550478704` — success;
- paper run `35550478697` — success;
- PDF artifact `10618029564` — visually inspected, 9 pages.

Outstanding before N7: author confirmation of applicable AI-tool terms and account/data-control settings for Elsevier privacy/confidentiality/no-unrelated-training compliance.

Next:

`N7 — SUBMISSION FREEZE — BLOCKED PENDING AUTHOR CONFIRMATION`.
