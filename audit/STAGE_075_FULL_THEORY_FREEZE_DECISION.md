# Stage 7.5 — Full-Theory Freeze Decision

## Canonical verdict

`NO-GO — FULL-THEORY ROUTE`

Classification:

`COMPACT CORRECTION / REASSESSMENT NOTE — WORTH PURSUING`

This is not a rejection of the project. It is a routing decision under
`research-paper-workflow v2.3`: the certified contribution is materially
valuable as a correction of Gehrig–Shy–Stenbacka (2011), but it does not yet
contain a sufficiently general mechanism to justify treatment as a new
full-theory paper.

Accordingly, the project must **not** be advanced to Stage 7.5A or Stage 8 under
the full-theory route by simply relabeling a narrow correction as a general
theorem.

## 1. Can the core result be stated without model-specific notation?

### Yes, but only at the mechanism level

Application-neutral statement:

> When one firm's single price jointly serves heterogeneous customer segments,
> an interior first-order-condition solution can fail globally because the firm
> may profitably raise price and abandon one segment. In the GSS environment,
> imposing the correct global-equilibrium scope also reveals that the published
> welfare comparison is reversed once consumer surplus is calculated correctly.

This is intelligible without GSS notation.

However, the **exact theorem content** remains model-specific:

- the square-root global-validity thresholds;
- `D_U subseteq D_HBP`;
- the exact factor-three consumer-surplus correction;
- the `-1/16` welfare coefficient.

Therefore the general prose mechanism exists, but the certified theorem is not
a general theorem over a broader demand/function class.

## 2. Minimal causal / strategic chain

The certified causal chain is:

1. two customer cohorts differ because old consumers face a switching cost;
2. one firm can discriminate across cohorts while its rival must set a common
   price;
3. a common price couples the firm's profits across the two clipped demand
   segments;
4. an interior FOC can be dominated by a finite deviation that abandons one
   cohort;
5. therefore the source's displayed formulas require explicit global-validity
   restrictions;
6. on the common certified domain, HBP reallocates old and new consumers while
   leaving aggregate firm shares unchanged;
7. HBP reduces transportation mismatch but induces additional switching;
8. the switching-cost increase exceeds the matching gain;
9. after correcting the source's consumer-surplus arithmetic, total welfare is
   lower under HBP at the displayed equilibria.

This is economically coherent and more than a numerical parameter exercise.

## 3. Essential assumptions versus normalization / tractability

### Essential for the current certified result

- two positive-mass consumer cohorts;
- one cohort incurs a one-sided switching cost;
- one firm can condition price on cohort;
- the rival must use a common price;
- Hotelling horizontal differentiation;
- clipped affine cohort demands;
- switching cost enters welfare as real utility/resource loss;
- simultaneous price competition;
- welfare comparison restricted to the displayed equilibria on the certified
  common domain.

### Normalization / tractability

- location endpoints normalized to 0 and 1;
- `tau` can be normalized for derivation and restored dimensionally;
- marginal-cost levels can be recentered, leaving `Delta c`;
- exact labels "incumbent", "entrant", "old", and "new" are interpretive.

### Material assumptions not yet generalized

- linear transportation cost;
- exactly two cohorts;
- exactly one common-price constraint;
- exogenous switching cost;
- no endogenous information acquisition;
- no dynamic customer acquisition;
- no endogenous choice of pricing regime;
- no full equilibrium correspondence outside the displayed branches.

These limitations are central to the Stage-7.5 decision.

## 4. Does the contribution survive a credible alternative formulation?

### Not yet as a theorem

The project has been stress-tested extensively **within the GSS model**:

- independent clean-room global-equilibrium certification;
- piecewise branch enumeration;
- exact counterexamples;
- boundary/indifference audit;
- welfare decomposition;
- literature absorption tests.

But no alternative economic formulation has been solved that changes a
structural assumption such as:

- nonlinear transportation costs;
- smooth non-Hotelling segmented demand;
- more than two cohorts;
- alternative real switching-cost technology.

Stage 6 also found that the generic piecewise-affine optimization method belongs
to an existing parent-class literature.

Therefore the result has not earned a claim of general mechanism robustness in
the workflow sense.

This is the decisive blocker for the **full-theory** route.

## 5. Is the welfare implication substantive?

`YES`.

The welfare reversal is not transfer accounting.

Certified resource decomposition:

`TC^d-TC^u = -3 theta(1-theta)sigma^2/(16 tau)`

`SC^d-SC^u = +4 theta(1-theta)sigma^2/(16 tau)`

so

`W^d-W^u = - theta(1-theta)sigma^2/(16 tau)`.

Thus HBP improves matching but induces more switching, and the latter dominates.

The private/social conflict is also substantive:

- incumbent operating profit favors HBP;
- consumers favor uniform pricing;
- total welfare favors uniform pricing;
- entrant displayed profit is unchanged.

This materially strengthens the correction note.

## 6. Would a skeptical field referee see more than a parameter exercise?

### For a correction/reassessment note: YES

The project identifies:

1. a published welfare-sign error;
2. a factor-three consumer-surplus arithmetic error;
3. a separate global-equilibrium-domain defect;
4. exact necessary/sufficient global-validity conditions for the displayed
   uniform candidate;
5. exact containment of the comparison domains;
6. a real-resource explanation of the welfare reversal;
7. exact counterexamples showing why interiority is insufficient.

That is substantially more than a routine comparative-static exercise.

### For a new general theory paper: NOT YET

A skeptical theory referee could reasonably say that:

- the parent mathematical class is already known;
- the new thresholds are source-specific;
- no broader functional-class theorem is established;
- no alternative structural formulation has been solved;
- no endogenous regime-choice or broader organizational theorem is present.

Hence the project should not be inflated into a general theory paper.

## 7. Generalization / unification test

No generalization or unification claim survives Stage 6.

The project does not nest and extend multiple important prior models in a way
that generates a new theorem unavailable in the benchmarks.

Therefore this criterion does not support a full-theory `GO`.

## 8. Why the project should continue as a correction note

The note has four independent reasons for publication value:

### A. Headline correction

The source welfare conclusion reverses under its own displayed model formulas.

### B. Equilibrium-scope correction

The source interior formulas are not globally valid over the unrestricted
parameter space; the correction supplies exact validity domains.

### C. Methodological relevance

The exact counterexamples demonstrate a specific failure mode:
cohort interiority does not imply global optimality when a common price spans
multiple clipped segments.

This is useful as a caution, even though the generic method is not claimed as
new theory.

### D. Economic interpretation

The corrected welfare sign has a transparent resource mechanism rather than
being a bare algebraic sign flip.

These features justify a self-contained correction/reassessment manuscript.

## 9. Recommended manuscript class

Preferred classification:

`SHORT THEORY NOTE / CORRECTION / REASSESSMENT`

Expected structure should be compact:

1. introduction and exact correction statement;
2. source model and displayed formulas;
3. global-validity correction;
4. consumer-surplus/welfare correction;
5. resource-cost interpretation;
6. short literature positioning;
7. appendices with global-BR proof and exact counterexamples.

The manuscript should not be expanded merely to resemble a full-length theory
paper.

## 10. What would be required to reopen the full-theory route?

A genuine Stage-7.5 reconsideration would require at least one **structural**
extension, not additional algebra inside the same model.

Examples:

- prove an analogous global-BR/welfare theorem for a non-Hotelling segmented
  demand class;
- characterize a broader class of common-price constraints with a theorem that
  nests GSS as one case;
- endogenize the pricing-regime choice and derive a new private/social adoption
  wedge;
- show the welfare mechanism survives a materially different switching-cost or
  demand formulation.

Any such extension must return to Stage 3/4/4A and then repeat Stage 6–7.5.
It must not be bolted onto the present correction note without re-certification.

## 11. Formal verification despite full-theory NO-GO

Stage 4A concluded `FORMALIZATION APPLICABLE`.

The full-theory pipeline would normally implement this at Stage 7.5A.
Because Stage 7.5 is `NO-GO` for that route, the project must not falsely mark
Stage 7.5A as passed.

Nevertheless, targeted Lean verification remains strongly recommended before
submission because this is a mathematical correction of a published result.

Recommended note-specific pre-submission assurance:

- formalize P1/P2 threshold implications;
- formalize P3 containment;
- formalize P4 welfare identities;
- formalize the three exact counterexamples;
- retain the Stage-4A clean-room global-deviation audit as the economic-model
  certification.

This should be recorded as a **note-specific formal verification task**, not as
a retroactive Stage-7.5A `GO`.

## 12. Claims authorized for the note

Allowed:

> We correct two issues in Gehrig, Shy & Stenbacka (2011). The displayed
> pricing formulas are Nash equilibria only on explicit parameter domains, and
> on their common validity domain the paper's welfare ranking reverses after
> correcting consumer surplus. The welfare reversal reflects a real-resource
> tradeoff: improved spatial matching is outweighed by additional switching.

Not allowed:

> We develop a new general theory of history-based price discrimination.

Not allowed:

> Uniform pricing is generally welfare superior to history-based pricing.

Not allowed:

> The complete GSS game has a unique equilibrium on the full parameter space.

## 13. Canonical routing decision

`NO-GO — FULL-THEORY ROUTE`

`PROJECT CLASSIFICATION — COMPACT CORRECTION / REASSESSMENT NOTE`

The current theory is strong enough to justify manuscript investment **as a
correction note**, but not to justify passing the workflow's full-theory freeze
gate.

Therefore:

- Stage 7.5A is **NOT ENTERED** under the full-theory workflow;
- Stage 8 is **BLOCKED** under the full-theory workflow;
- the next productive task is to define and execute a note-specific
  pre-submission assurance/freeze protocol, including targeted formal
  verification, before manuscript construction.
