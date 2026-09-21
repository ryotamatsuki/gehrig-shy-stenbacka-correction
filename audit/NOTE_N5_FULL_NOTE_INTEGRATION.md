# Note N5 — Full-Note Integration

## Purpose

Integrate the N3-refereed manuscript for the N4 re-certified
`Review of Industrial Organization` first-submission route without changing
the N1-frozen theorem scope.

## Target-journal requirements checked

Current RIO author guidance was checked directly at the Springer journal site.

Relevant requirements:

- RIO publishes industrial-organization research and explicitly welcomes
  shorter notes and commentaries.
- Abstract: 150–250 words.
- Keywords: 4–6.
- JEL classification: required.
- Mathematical manuscripts may be submitted in LaTeX.
- Editable source files are required.
- Reference list: published or accepted works only; unpublished works should be
  mentioned in text rather than included in the reference list.
- Data Availability Statement required for original research.
- Author/contribution and competing-interest metadata are handled through the
  submission interface.

Official pages:

- https://link.springer.com/journal/11151/aims-and-scope
- https://link.springer.com/journal/11151/submission-guidelines

## Manuscript integration

### Title

N2/N3 title:

`History-Based Price Discrimination with Switching Costs: Equilibrium Scope and a Welfare Correction`

N5 RIO-facing title:

`A Comment on Gehrig, Shy, and Stenbacka (2011): Equilibrium Scope and Welfare`

Rationale:

- identifies the paper unambiguously as a source-specific comment;
- avoids suggesting a general new theory;
- communicates the two substantive objects: equilibrium scope and welfare.

### Abstract

The abstract was rewritten to be self-contained and to satisfy the RIO
150–250-word requirement.

Approximate plain-text count:

`173 words`.

It contains no citation commands and preserves exactly the N1-authorized claims:

- global-validity correction;
- domain containment;
- factor-three CS correction;
- incumbent-profit and entrant-profit identities;
- welfare reversal;
- switching-cost versus spatial-matching interpretation.

### Keywords / JEL

Keywords: 5.

JEL codes added:

- D43 — Oligopoly and Other Forms of Market Imperfection;
- L11 — Production, Pricing, and Market Structure;
- L13 — Oligopoly and Other Imperfect Markets.

### Introduction / conclusion alignment

The manuscript now consistently calls itself a `comment`.

The source-specific limitation remains explicit.

No new claims were added about:

- uniqueness;
- outside-domain equilibrium correspondence;
- general welfare dominance;
- policy;
- endogenous regime choice.

The conclusion continues to preserve the entrant-profit / entry-invariance
qualification.

## Source and bibliography integration

RIO guidance states that unpublished works should not appear in the reference
list.

Accordingly:

- the complete 14 December 2009 author draft remains described in the
  source-version paragraph but was removed from the bibliography;
- the unpublished Gnutzmann (2014) working paper was removed from the
  bibliography and from the related-literature citation list;
- all remaining bibliography entries are cited in the manuscript;
- no citation key is missing;
- no bibliography entry is uncited;
- the bibliography contains no `@unpublished` entry;
- DOI metadata was added for Bouckaert, Degryse & van Dijk (2013);
- DOI metadata was preserved in BibTeX. The attempted `spbasic` style was reverted because the current TeX CI image does not provide `spbasic.bst`; RIO permits LaTeX submissions and recommends, rather than requires, the Springer template. Final publisher-template styling is therefore an N6 submission-QA task.

The remaining cited articles and DOI metadata were independently checked
against current publisher / AEA / RePEc records during N5.

## Data availability / reproducibility

A Data Availability section was added:

- no empirical dataset is analyzed;
- the computational and formal-verification files supporting the analytical
  checks are identified as an accompanying replication package.

A package manifest was created at:

`supplement/README.md`.

It maps:

- Stage-4A clean-room economic verification;
- Stage-7 welfare decomposition;
- N3 independent manuscript recheck;
- Lean source/toolchain/dependencies;
- audit certificates.

The manuscript does **not** claim that the whole economic game is Lean
formalized.

## Table / equation consistency

No new figure was introduced.

The existing welfare-decomposition table is unchanged and remains covered by
the certified Stage-7 algebraic check and N3 independent recheck.

Theorem architecture is unchanged:

- Proposition 1 — displayed-profile global validity;
- Corollary 1 — domain containment;
- Example 1 — exact HBP deviation;
- Proposition 2 — corrected CS/profit/welfare.

## Deliberately deferred to N6

N5 does not fabricate submission metadata.

N6 must finalize:

- author name;
- affiliation;
- corresponding-author email;
- ORCID, if used;
- competing-interest declaration;
- funding declaration;
- final submission-system article type;
- final replication-package URL or supplementary archive;
- any anonymity choice required by the live submission interface.

## N1 reopen audit

No N1 reopen trigger occurred.

N5 changes are journal-facing integration only:

- title/framing;
- abstract;
- JEL;
- bibliography/source-format compliance;
- data-availability / replication presentation.

No mathematical theorem, parameter domain, quantifier, counterexample, or
welfare identity changed.

## N5 closure gate

Required before PASS:

1. RIO-integrated manuscript compiles to PDF.
2. Stage-1/4/4A/7/N3 regression suite passes.
3. Lean formal-verification workflow passes.
4. No missing citation keys / uncited bibliography entries.
5. N1 claim scope remains unchanged.

Current verdict:

`CONDITIONAL PASS — INTEGRATION COMPLETE; CI CONFIRMATION PENDING`.
