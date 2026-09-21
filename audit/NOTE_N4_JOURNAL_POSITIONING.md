# Note N4 — Journal Positioning

## Canonical verdict

`GO — EER PRE-SUBMISSION INQUIRY FIRST; IJIO PRIMARY FALLBACK`

Submission classification:

`INDEPENDENT COMMENT / CORRECTION / REASSESSMENT NOTE`

Do **not** label the manuscript a publisher "Corrigendum." It is an
independent scholarly correction of a published model, not an author/publisher
correction notice.

## Current manuscript fit

After N4 source hygiene, the manuscript is a single clean LaTeX document:

- approximately 2,900 words by a crude LaTeX-stripped count;
- 2 propositions;
- 1 corollary;
- 1 exact counterexample in the main text;
- 1 welfare-decomposition table;
- technical appendix with the common-price global-best-response calculation,
  additional exact deviations, and verification notes;
- one `\appendix`;
- one `\end{document}`.

N4 identified and removed dead duplicated source after the first
`\end{document}`. Because TeX stops at the first `\end{document}`, the
previously certified PDF already contained only the intended manuscript; the
cleanup removes source-file debris rather than changing any theorem or rendered
claim.

Clean-source commit:

`a11d8f193cc919350e3db85d45400c662515357b`.

Clean-source manuscript compile run:

`35505354250 — success`.

## 1. European Economic Review — first contact, inquiry before paid submission

### Fit

This is the journal that published the target article:

Gehrig, Shy & Stenbacka (2011),
*History-based Price Discrimination and Entry in Markets with Switching Costs:
A Welfare Analysis*,
European Economic Review 55(5), 732–739.

Current EER scope describes the journal as a general-interest outlet for
theoretical and empirical economics and states that it seeks work with high
relevance and impact across a wide range of topics.

Official journal page:
https://shop.elsevier.com/journals/european-economic-review/0014-2921

EER has a historical record of publishing articles explicitly titled
"comment" and recent issues also contain comments on previously published EER
work. Examples include:

- *Wall street QE vs. main street lending: A comment*,
  European Economic Review 161 (2024), 104569;
- *Comment on "Sectoral shocks, reallocation, and labor market policies"*,
  European Economic Review 157 (2023), 104523.

These examples establish that "comment" is a genuine EER publication form.
However, some recent examples arose from conference/discussant settings, and
the current public author material located in N4 does **not** clearly state
whether an unsolicited independent correction of a 2011 EER article should be
submitted as a Comment, a Research Article, or another article type.

### Submission-cost issue

The currently indexed EER Guide for Authors states that unsolicited
submissions carry a non-refundable EUR 100 submission fee (EUR 50 for a PhD
student contact author). A 2024 institutional invoice also confirms the EUR
100 submission-fee practice.

General submission-query address shown in the guide:

`eer@elsevier.com`.

### N4 decision

`FIRST CHOICE — INQUIRY BEFORE SUBMISSION`.

Do not pay the submission fee until the editorial office confirms that an
independent source-specific correction/reassessment of the 2011 EER article is
within current editorial scope and identifies the suitable article type.

The inquiry should state, very briefly:

1. the full citation/DOI of the 2011 EER article;
2. that the new manuscript is an independent correction/reassessment, not a
   corrigendum submitted by the original authors;
3. that it establishes two material points:
   - exact global-validity restrictions for the displayed equilibria;
   - a factor-three CS correction that reverses the published welfare headline
     on the common certified domain;
4. approximate manuscript length (~2,900 words plus technical appendix);
5. that the proofs and exact counterexamples have independent computational and
   Lean verification;
6. a direct question: whether EER would consider this as a Comment or other
   appropriate article type.

### Why not direct-submit immediately?

The relationship to the original EER article is uniquely strong, but the
general-interest scope creates a real desk-rejection risk for a deliberately
source-specific note. The article-type ambiguity plus the non-refundable
submission fee makes an inquiry the dominant first move.

## 2. International Journal of Industrial Organization — primary fallback

### Field fit

Current IJIO scope states that it aims at full coverage of theoretical and
empirical industrial-organization questions, including classic strategic
behavior and market structure, and explicitly encourages theoretical work.

Official journal page:
https://shop.elsevier.com/journals/international-journal-of-industrial-organization/0167-7187

This is a substantially tighter field fit than EER for the mathematical
content of the correction.

### Extremely close current Comment precedent

Izabela Jelovac (2026),
*Generic entry, price competition, and market segmentation in the prescription
drug market – a comment*,
International Journal of Industrial Organization 104, 103218,
DOI 10.1016/j.ijindorg.2025.103218.

Its abstract states that it revises a theoretical condition from Regan (2008):
the condition was obtained from an interior solution while excluding the
existence of that interior solution, creating an internal inconsistency.

That is unusually close to the present note's equilibrium-scope issue:

`interior FOC / interior allocation != global equilibrium validity`.

The current note additionally contains a welfare-sign correction and exact
global-validity domains.

### Caveat

Jelovac corrects an article originally published in IJIO, whereas the present
target article was published in EER. Therefore this precedent proves that IJIO
actively publishes mathematically substantive Comments, but not that IJIO will
automatically accept comments on papers from another journal.

### N4 decision

`PRIMARY FALLBACK / BEST DIRECT FIELD SUBMISSION AFTER EER`.

If EER says the note is outside its current Comment/article scope, position the
paper for IJIO as a short source-specific theoretical reassessment with a
general methodological warning about common-price coupling and global
deviations, without inflating the generic lemma into a novelty claim.

## 3. Research in Economics — second fallback

Current publisher description identifies Research in Economics as a
general-interest theoretical/empirical journal. Its editorial policy is
unusually compatible with a correction note: editors first ask whether the
result, **if correct**, is worth publishing, then ask whether the paper is
understandable/coherent and whether the results are correct within reasonable
bounds. It states a goal of a definitive answer within one month.

Official journal page:
https://shop.elsevier.com/journals/research-in-economics/1090-9443

### Strengths

- exact-correction/reassessment work fits the "if correct, worth publishing"
  editorial logic;
- theory is within scope;
- compact manuscript is not structurally problematic;
- fast-decision policy is attractive for a rigorously pre-certified note.

### Weakness

The audience is less specifically industrial-organization focused than IJIO,
and the link to the original EER publication is weaker than an EER submission.

### N4 decision

`SECOND FALLBACK`.

## 4. Journal of Industry, Competition and Trade — explicit Comment format but
scope tension

Current Springer submission guidelines explicitly state:

- papers are typically under 20 double-spaced pages and cannot exceed 40;
- comments or replies to previously published articles are accepted in the
  manuscript format;
- the journal uses double-blind review;
- mathematical manuscripts may be submitted in LaTeX;
- simultaneous consideration elsewhere is prohibited.

Official submission guidelines:
https://link.springer.com/journal/10842/submission-guidelines

The journal is hybrid. The current Springer page states that the subscription
route has no APC, while optional open access currently costs EUR 2,390
(also GBP 2,090 / USD 2,990).

Official publishing-options page:
https://link.springer.com/journal/10842/how-to-publish-with-us

### Scope tension

The current aims and scope state that applied theoretical papers must clearly
highlight implications for empirical analysis and economic policy.

The present note intentionally does **not** derive an optimal policy theorem,
and N1 prohibits inflating the correction into a regulatory recommendation.
That makes JICT's explicit Comment format attractive but its substantive
positioning less clean than IJIO.

### N4 decision

`THIRD FALLBACK`.

Do not add artificial policy claims merely to improve JICT fit.

## 5. Economics Bulletin — preservation fallback

The current submission portal explicitly accepts peer-reviewed:

- Note;
- Comment;
- Preliminary Result.

It limits these submissions to seven printed pages or fewer, excluding tables,
figures, and references.

Submission portal:
https://www.accessecon.com/pubs/eb/default.aspx?page=Newsubmission

### N4 decision

`FINAL FORMAT-COMPATIBLE FALLBACK`.

The present manuscript would require a significant compression/reallocation to
fit the seven-page main-text format, but the journal is explicitly designed to
carry Comments.

## 6. Economics Letters — killed

Current Economics Letters description states:

- contributions are usually limited to about 2,000 words excluding references;
- comments or pedagogical notes are **not suitable** for the Letters format.

Official journal page:
https://shop.elsevier.com/journals/economics-letters/0165-1765

The clean manuscript is approximately 2,900 words even before treating the
technical appendix separately, and its scholarly purpose is precisely a
correction/reassessment of prior work.

### N4 decision

`KILL — DO NOT SUBMIT`.

This is a scope mismatch, not merely a length problem.

## Canonical submission sequence

1. **EER — pre-submission suitability inquiry only.**
2. If EER explicitly invites submission:
   - N5 becomes EER-specific integration;
   - submit under the article type instructed by EER.
3. If EER says unsuitable or does not consider this type of independent
   correction:
   - **IJIO** becomes the direct submission target.
4. If IJIO rejects on fit/contribution rather than a correctable manuscript
   defect:
   - **Research in Economics**.
5. Then **Journal of Industry, Competition and Trade**.
6. **Economics Bulletin** only as a compact-preservation fallback.

Economics Letters is excluded.

## Positioning language by venue

### EER

Lead with scientific-record correction:

> This note revisits a 2011 European Economic Review article and establishes
> two material corrections: exact global-equilibrium validity conditions for
> its displayed pricing profiles and a consumer-surplus correction that
> reverses its published welfare headline on the common certified domain.

Do not lead with Lean or generic methodology. Verification is supporting
credibility, not the contribution.

### IJIO

Lead with the equilibrium issue and then welfare:

> In a canonical history-based-pricing model, interior first-order conditions
> need not characterize a global equilibrium when a common price spans clipped
> customer segments. We derive the exact validity regions and show that the
> corrected welfare accounting reverses the source-model ranking.

This connects naturally to the active IJIO Comment precedent without claiming
generic theory novelty.

### Research in Economics

Lead with correctness/materiality:

> The note supplies an exact reassessment of a published welfare result and
> identifies the global-equilibrium domain needed for the comparison to be
> well-defined.

## Pre-submission rules frozen at N4

- Never submit simultaneously to multiple journals.
- Never call the manuscript a `Corrigendum` unless a publisher/editor
  specifically instructs that classification.
- Do not add empirical or policy claims to manufacture journal fit.
- Do not weaken the source-version caveat for the sake of a stronger cover
  letter.
- EER submission fee should not be paid before the suitability inquiry is
  resolved.
- Any journal-requested theorem or scope expansion that exceeds N1 reopens N1
  and all affected downstream stages.

## N4 canonical verdict

`PASS — JOURNAL POSITIONING FROZEN`

Primary route:

`EER INQUIRY FIRST -> IF INVITED, EER SUBMISSION`

Primary fallback:

`IJIO`

Second fallback:

`RESEARCH IN ECONOMICS`

Next:

`N5 — FULL-NOTE INTEGRATION`

N5 should first produce an EER-facing integrated package: journal-neutral
manuscript cleanup plus an EER suitability-inquiry draft. It should not change
the frozen theorem scope.


---

## N4 Re-certification Addendum — post-positioning review

### Trigger

After the initial N4 freeze, the journal ladder was stress-tested against a
more precise objective:

> avoid spending long review cycles on a venue whose contribution threshold is
> materially above this source-specific correction, while also avoiding an
> unnecessarily low placement.

The manuscript itself and all N1 mathematical claims are unchanged.

### Reassessment

The initial ordering over-weighted the existence of an IJIO Comment precedent.
That precedent shows that IJIO publishes mathematically substantive Comments,
but it corrected an IJIO article. The present note corrects an EER article and
does not claim a new general IO theorem. IJIO therefore remains a defensible
stretch submission, but not the default time-efficient first target.

Research in Economics was also re-examined. Its editorial model is unusually
compatible with a correctness-driven reassessment: the initial editorial
question is whether the result, if correct, is worth publishing, followed by a
focused correctness/coherence evaluation. It is therefore a credible direct
target rather than merely a low fallback.

Review of Industrial Organization provides the best compromise between
specialist audience and attainable contribution threshold. It has a direct IO
readership and published precedent for short comments that revise consumer-
surplus/social-welfare comparisons in prior IO models.

### Re-certified canonical ladder

1. **Review of Industrial Organization (RIO)** — first formal submission.
2. **Research in Economics (RiE)** — second submission; strongest
   time-efficiency / correctness-fit alternative.
3. **Journal of Industry, Competition and Trade (JICT)**.
4. **Economics Bulletin** — preservation fallback.

Optional:

- **IJIO** may be inserted before RIO only as a deliberate stretch attempt.
- **EER** may receive a brief suitability/scientific-record inquiry, but this
  is not a formal submission and should not delay the main ladder.

Excluded:

- **Economics Letters**.

### Rationale

The note is stronger than a one-line corrigendum because it contains:

- exact global-validity domains for both displayed pricing regimes;
- exact finite-deviation counterexamples;
- a factor-three consumer-surplus correction;
- reversal of the displayed-equilibrium welfare ranking;
- a real-resource decomposition;
- independent clean-room and Lean-backed verification.

At the same time, Stage 7.5 correctly determined that the contribution remains
source-specific rather than a new general theory of history-based pricing.
That combination argues against both extremes: neither a high-risk IJIO-first
strategy nor an immediate Economics Bulletin placement is the default.

### N4 re-certified verdict

`PASS — JOURNAL POSITIONING RE-CERTIFIED`

Canonical first formal target:

`REVIEW OF INDUSTRIAL ORGANIZATION`

Canonical second target:

`RESEARCH IN ECONOMICS`

Next workflow gate remains:

`N5 — FULL-NOTE INTEGRATION`.
