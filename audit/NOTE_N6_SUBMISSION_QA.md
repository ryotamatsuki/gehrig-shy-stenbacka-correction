# Note N6 — Submission QA

## Canonical verdict

`PASS — SUBMISSION QA COMPLETE`

Routing:

`N7 — SUBMISSION FREEZE — NEXT`

Target submission route:

`Research in Economics (Elsevier)`.

Submission package commit audited:

`0532899eb320e7333d1751542ebedac1f0e41021`.

Formal source blob:

`fa5b8d1dba6a6b8f25bdb0916bfd8bca1b33fe82` — unchanged from the N1-certified source.

## 1. Gate prerequisites

- N1: PASS — NOTE THEORY FROZEN.
- N2: PASS — MANUSCRIPT CONSTRUCTED.
- N3: PASS — INDEPENDENT REFEREE ATTACK RESOLVED.
- N4: PASS — journal positioning re-certified.
- N5: PASS — FULL-NOTE INTEGRATION COMPLETE.
- N6 retargeted the submission package to Research in Economics by explicit author decision; no frozen mathematical statement was changed.

## 2. Mathematical QA

An independent N6 SymPy reconstruction, separate from the repository regression scripts, rechecked the manuscript formulas.

Confirmed:

- displayed HBP prices and cohort shares;
- displayed uniform prices and cohort shares;
- equality of the aggregate incumbent share on the displayed branch;
- HBP and uniform exact global-validity thresholds;
- containment differences: `3 sigma(theta+sqrt(theta))/4` at the lower bound and `3 sigma sqrt(1-theta)/2` at the upper bound;
- primitive consumer-surplus integration;
- `CS^u-CS^d = 3 theta(1-theta)sigma^2/(16 tau)`;
- `pi_A^d-pi_A^u = theta(1-theta)sigma^2/(8 tau)`;
- `pi_B^d-pi_B^u = 0`;
- `W^d-W^u = -theta(1-theta)sigma^2/(16 tau)`;
- `TC^d-TC^u = -3 theta(1-theta)sigma^2/(16 tau)`;
- `SC^d-SC^u = theta(1-theta)sigma^2/(4 tau)`;
- HBP real-resource-cost excess `theta(1-theta)sigma^2/(16 tau)` when sigma is a real switching disutility/resource loss.

Independent exact counterexample reconstruction:

- CE1: `p_A=47/24`, `q_A=97/120`, `p_B=37/60`, `x_o=47/48`, `x_n=97/240`, deviation `217/240`, gain `3281/230400 > 0`;
- CE2: uniform entrant deviation `49/60`, gain `89/14400 > 0`;
- CE3: uniform incumbent deviation `157/60`, gain `89/14400 > 0`.

No N1 reopen trigger was found.

## 3. Equilibrium-scope / wording QA

Full-text scan found none of the prohibited overclaims:

- `unique equilibrium`;
- `no equilibrium exists`;
- `globally valid for all parameters`;
- `uniform pricing is welfare superior`;
- `uniform pricing dominates HBP`;
- `optimal regulation`;
- `HBP should be banned`.

The only occurrence of the phrase `the equilibrium` is the sentence stating that equilibrium results are for the real-price game; it is not a uniqueness claim.

The manuscript expressly preserves:

- real-price game as the canonical strategy domain;
- nonnegative-price interpretation only when the displayed candidates and relevant deviations are feasible;
- weak-boundary multiplicity / tied-best-response caveat;
- no selection-invariant welfare claim for alternative boundary equilibria;
- displayed-equilibrium scope for the welfare comparison.

## 4. Source / version QA

Canonical relationship retained:

- equation-level reconstruction: complete 14 December 2009 author draft;
- published 2011 bibliographic metadata and published welfare headline: checked against the current ScienceDirect article record;
- factor-three expression error: attributed to the complete author draft;
- no claim of line-by-line Version-of-Record equation inspection;
- no correction/corrigendum addressing the certified factor-three, welfare-sign, or global-deviation issue was located in the targeted N6 searches.

Manuscript uses `draft`, `article`, and `Version of Record` only within this constrained attribution. It does not use `original paper` or `published paper` as ambiguous equation-level source labels.

Primary published record:

- https://www.sciencedirect.com/science/article/pii/S001429211000084X

## 5. Consumer-surplus correction QA

The main text displays the primitive consumer-surplus integral separately for old and new cohorts. Switching cost enters only the old consumers who buy from entrant B. Direct substitution into that integral reproduces the factor-three correction without reliance on the repository code.

Verdict: PASS.

## 6. Bibliography QA

Mechanical citation-key audit:

- cited keys: `bouckaert2013`, `chen2026`, `gehrig2011`, `gehrig2012`, `shy2016`;
- bibliography keys: exactly the same five;
- missing citations: none;
- uncited bibliography entries: none.

Metadata rechecked during N6:

- Gehrig, Shy & Stenbacka (2011), EER 55(5), 732–739, DOI `10.1016/j.euroecorev.2010.09.001`;
- Gehrig, Shy & Stenbacka (2012), JICT 12(4), 373–393, DOI `10.1007/s10842-011-0111-8`;
- Bouckaert, Degryse & van Dijk (2013), Journal of Industrial Economics 61(1), 62–83, DOI `10.1111/joie.12011`;
- Shy, Stenbacka & David Hao Zhang (2016), IJIO 48, 88–117, DOI `10.1016/j.ijindorg.2016.06.002`;
- Yanlin Chen, Xianwen Shi & Jun Zhang (2026), AEJ: Microeconomics 18(3), 203–243, DOI `10.1257/mic.20230234`.

Verdict: PASS.

## 7. Research in Economics positioning QA

Current RiE public journal description confirms that it publishes original theoretical and empirical economics articles and states an editorial sequence that first asks whether the results, if correct, are worth publishing, then emphasizes understandable/coherent exposition and correctness.

Official journal page:

- https://shop.elsevier.com/journals/research-in-economics/1090-9443

N6 changes therefore position the manuscript as a compact theoretical reassessment rather than a publisher corrigendum:

- title changed to `Equilibrium Scope and Welfare in History-Based Price Discrimination: A Reassessment of Gehrig, Shy, and Stenbacka (2011)`;
- abstract foregrounds the two corrections and explicit restricted scope;
- Lean/GitHub/CI remain supporting credibility, not the economic contribution;
- default submission classification is the standard research-article/full-length category unless the live RiE portal explicitly exposes a dedicated Comment/Reassessment category.

## 8. Title / abstract / keywords / JEL

- Title: source-specific reassessment, without claiming a general new theory.
- Abstract: equilibrium-scope correction, factor-three CS correction, welfare reversal, and scope limitation all explicit.
- Keywords: 5.
- JEL: D43 / L13 / D60.

Verdict: PASS.

## 9. Anonymity QA

No current public RiE-specific source located during N6 established a double-anonymized submission requirement. The canonical submission manuscript therefore carries the author identity rather than maintaining an unnecessary anonymous fork.

If the live submission portal explicitly requests double-anonymized files, producing an anonymous derivative from the frozen source is a formatting-only operation and does not reopen N1.

Verdict: PASS for the currently documented requirement set.

## 10. Submission metadata / declarations

Submission metadata is now populated:

- Ryota Matsuki;
- Independent Researcher, Matsuyama, Ehime, Japan 790-0853;
- corresponding email `ryota.matsuki@gmail.com`;
- ORCID `0009-0005-2329-531X`;
- no specific external grant funding;
- no competing interests;
- no acknowledgements;
- manuscript confirmed not to be under consideration elsewhere.

Elsevier's current generative-AI policy requires disclosure when AI assistance makes substantive changes to sentence structure or organization. The manuscript now contains a separate declaration naming OpenAI ChatGPT, describing its uses, and retaining full author responsibility.

Policy source:

- https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals

Files:

- `paper/SUBMISSION_METADATA.md`;
- `paper/title_page.md`;
- `paper/cover_letter.md`.

Verdict: PASS.

## 11. Supplement / reproducibility package

`supplement/README.md` now separates reviewer-facing reproducibility material from internal audit/editorial-strategy records.

External package includes:

- Stage 1 independent recheck;
- Stage 4 global-validity verifier;
- Stage 4A clean-room adversarial verifier;
- Stage 7 welfare decomposition;
- N3 independent recheck;
- Lean source;
- `lean-toolchain`;
- `lakefile.lean`;
- pinned `lake-manifest.json`;
- `requirements.txt` with `sympy==1.14.0`;
- CE1–CE3 exact regression data.

Internal audit files are not part of the intended reviewer supplement.

Repository tree contains no committed PDF/ZIP/image binary matching a publisher Version of Record.

Verdict: PASS.

## 12. Reproducibility CI

Submission-package commit:

`0532899eb320e7333d1751542ebedac1f0e41021`.

Mathematical/formal workflow:

- run `35550478704` — SUCCESS;
- Stage 1 exact recheck — success;
- Stage 4 global-validity checks — success;
- Stage 4A independent adversarial checks — success;
- Stage 7 welfare decomposition — success;
- N3 independent referee recheck — success;
- Lean build / kernel audit — success;
- independent `leanchecker` — success;
- axiom audit — success; 47 declarations within `[propext, Classical.choice, Quot.sound]`; 
- `sorry` / `admit` rejection — success.

Formal source blob remains exactly the N1-certified blob:

`fa5b8d1dba6a6b8f25bdb0916bfd8bca1b33fe82`.

Verdict: PASS.

## 13. LaTeX / PDF QA

Paper workflow:

- run `35550478697` — SUCCESS;
- artifact `10618029564` — `manuscript-pdf`;
- final PDF: 9 pages;
- PDF preflight: openable, unencrypted, non-scanned;
- final log: no undefined citations/references, multiply-defined labels, missing glyphs, LaTeX/fatal errors, or overfull boxes;
- source has one `\\appendix` and one `\\end{document}`.

All nine rendered pages were visually inspected at N6. No table/equation overflow, clipped text, malformed equations, corrupted bibliography, accidental duplicate section, heading orphan, or anomalous blank page was found.

Verdict: PASS.

## 14. Publication ethics

- no simultaneous submission;
- no publisher PDF stored in the repository;
- source draft and published record are distinguished;
- no excessive verbatim source quotation;
- independent authorship is not represented as an original-author corrigendum;
- no citation-manipulation language;
- verification dependencies are pinned and no external proprietary dataset is redistributed.

Absence of a repository-wide open-source license does not prevent submission of the supplementary files; third-party Lean/mathlib dependencies retain their own licensing. A public-release license can be added later without changing the paper.

Verdict: PASS.

## 15. Final adversarial referee simulation

| Objection | Classification | N6 disposition |
|---|---|---|
| This is merely an arithmetic correction. | manuscript already resolves | The equilibrium-scope defect and exact profitable deviations are logically independent of the factor-three correction. |
| The paper is too source-specific. | genuine limitation but non-blocking | Scope is explicit; RiE fit is argued on correctness/materiality rather than general-theory novelty. |
| The equilibrium failure is an artifact of the price strategy set. | manuscript already resolves | Real-price theorem plus explicit nonnegative-price feasibility caveat. |
| The authors have not inspected every VOR equation. | genuine limitation but non-blocking | Exact formula attribution is limited to the complete author draft; the published headline is separately verified. |
| Welfare is not selection robust on weak boundaries. | manuscript already resolves | No selection-invariant boundary claim; result is for displayed equilibria. |
| The common-price lemma is not novel. | manuscript already resolves | It is proof machinery, not a novelty claim. |
| Why should RiE publish a reassessment of an EER article? | genuine limitation but non-blocking | RiE's public editorial policy expressly centers whether a correct result is worth publishing; the note changes a substantive welfare conclusion and equilibrium domain. |
| The entry result is unchanged. | genuine limitation but non-blocking | Manuscript expressly says entrant-profit equality survives and does not overstate the correction. |
| Policy relevance is limited. | genuine limitation but non-blocking | No policy theorem is claimed; economic content is the equilibrium and welfare correction. |
| Lean adds no economics. | manuscript already resolves | Formal verification is presented only as credibility support. |
| The title may imply a dedicated Comment article type. | needs wording fix — resolved | RiE title changed from `A Comment` to `A Reassessment`; default article category is standard research article unless portal says otherwise. |
| The negative `c_A` in CE2 is economically artificial. | manuscript already resolves | Appendix explains common additive cost/price translation leaves demand and markups unchanged. |
| AI-assisted preparation is undisclosed. | needs wording fix — resolved | Elsevier-style AI declaration added immediately before references. |

No blocking referee objection remains.

## 16. Unresolved limitations

Non-blocking and intentionally preserved:

- no full outside-domain equilibrium correspondence;
- no game-wide uniqueness theorem;
- no selection-invariant welfare theorem at weak-boundary multiplicities;
- no general HBP/personalized-pricing welfare theorem;
- no line-by-line certification of every Version-of-Record equation;
- live RiE portal wording for article-type/anonymity may require a purely formatting-level upload adjustment.

None requires N1 reopening.

## N6 exit criteria

1. N5 formally complete — PASS.
2. No N1 claim-scope drift — PASS.
3. Source/version attribution exact — PASS.
4. Equations/theorems/counterexamples match certified artifacts — PASS.
5. Bibliography audited — PASS.
6. PDF clean compile and visual QA — PASS.
7. Mathematical/Lean CI green — PASS.
8. Submission files aligned to documented RiE/Elsevier requirements — PASS.
9. Submission metadata/declarations complete — PASS.
10. No unresolved blocking referee objection — PASS.

## Final N6 decision

`PASS — SUBMISSION QA COMPLETE`

`N7 — SUBMISSION FREEZE — NEXT`