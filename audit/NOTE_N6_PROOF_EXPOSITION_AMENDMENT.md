# N6 Amendment — Proof Exposition and Human Readability

Date: 2026-09-21
Target: Research in Economics
Parent manuscript commit: `ddd69d53727105af4bb72a060cf9b247f261366e`

## Trigger

A full manuscript read-through found that the certified mathematics was stronger than the proof exposition visible to a human referee.  The generic common-price lemma had a formal `proof` environment, but Proposition 1, its containment corollary, and the welfare proposition did not all have an explicit paper-level proof closure.

## Changes

The manuscript now:

1. displays the interior first-order conditions before presenting the candidate prices;
2. adds a proof roadmap for the global-validity result;
3. gives an explicit Appendix proof of Proposition 1, including the three factorized square-root threshold gaps;
4. explains why the HBP weak upper boundary is included;
5. gives the domain-containment corollary an explicit proof and QED;
6. gives the welfare proposition an explicit proof from the primitive consumer-surplus integrals;
7. derives the factor-three consumer-surplus correction through cutoff identities and differences of squares rather than an opaque full expansion;
8. derives the incumbent-profit gap through the weighted-variance identity;
9. explains entrant-profit invariance from equal entrant price and aggregate quantity;
10. states why production-cost expenditure cancels in the resource decomposition;
11. identifies each numerical deviation as the vertex of the relevant one-cohort quadratic branch;
12. clarifies the branch-infeasible-vertex step in the generic common-price lemma.

## Theory-freeze effect

None.  The change is proof exposition only.

No equilibrium domain, theorem scope, counterexample, welfare identity, resource decomposition, source-version claim, bibliography item, Lean source, or verification script was changed.  All newly displayed intermediate identities were independently rechecked algebraically before insertion.

N1 remains frozen.  N6 retains its separate conditional status arising from the outstanding author-controlled Elsevier AI-tool terms/privacy confirmation.
