# Stage 6 — Novelty Re-Kill

## Canonical verdict

`GO — CORRECTION CONTRIBUTION SURVIVES; GENERIC-METHOD NOVELTY KILLED`

## Objective

Re-run the novelty/absorption test using the actual Stage-4A certified theorem
set rather than the pre-solution conjectures considered at Stage 2.

Certified objects entering Stage 6:

- L1: common-price global-best-response lemma for two weighted clipped affine
  demand segments;
- P1: exact global-validity domain for the displayed HBP candidate;
- P2: exact global-validity domain for the displayed uniform candidate;
- P3: `D_U subseteq D_HBP`, hence `D_compare=D_U`;
- P4: corrected consumer-surplus and welfare identities on `D_compare`.

## Search design

The search was re-run on 2026-09-20 through public web indexes and SciSpace.

### Application-labelled searches

Search language included:

- exact target title and DOI plus correction / erratum / consumer surplus /
  welfare / equilibrium;
- history-based / behavior-based price discrimination with switching costs;
- asymmetric no-discrimination constraints;
- incumbent/entrant common pricing;
- captive and contested consumers;
- uniform versus discriminatory pricing;
- later papers citing or positioning Gehrig–Shy–Stenbacka (2011).

### Application-neutral searches

The Stage-4 object was stripped to:

> simultaneous price competition in which a player's one-dimensional common
> price loads on a weighted sum of two clipped affine demand segments, while
> active-set changes may delete one segment.

Search language included:

- piecewise-affine price competition;
- regular extensions of affine demand;
- segmented-demand Bertrand competition;
- global best responses under clipped/piecewise-linear demand;
- FOC validity conditions in segmented price competition;
- common-price constraints across customer segments;
- captive-segment and market-capture deviations.

Exact square-root-threshold searches using `sqrt(theta)`,
`sqrt(1-theta)`, switching-cost, Hotelling, and price-discrimination language
did not return a matching prior result.

## Publication-level target check

The current ScienceDirect record exposes the 2011 article's published welfare
headline and section snippets. The abstract continues to state that the
incumbent's HBP profit gain exceeds the associated consumer loss.

Current public record:
https://www.sciencedirect.com/science/article/pii/S001429211000084X

The search did not locate a published erratum, corrigendum, or comment that
corrects the factor-three consumer-surplus identity, the resulting welfare
sign, or the global-validity scope derived here.

## Serious parent-theorem candidates and absorption maps

### A. Aksoy-Pierson, Allon & Federgruen (2013)

Paper:
*Price Competition Under Mixed Multinomial Logit Demand Functions*,
Management Science 59(8), 1817–1835.
DOI: `10.1287/mnsc.1120.1664`.

Prior theorem/object:
a general segmented-price-competition model with mixed multinomial-logit
demand. Under a stated market-share condition, pure Nash equilibrium exists
and Nash equilibria coincide with solutions to the FOC system; stronger
conditions deliver uniqueness.

Absorption map:

`prior segmented MNL theorem`
→ old/new market segments
→ firms A/B
→ would require replacing each GSS clipped Hotelling segment by an MNL share
and changing the demand functional class
→ P1/P2 exact square-root validity thresholds
→ **NOT ABSORBED**.

Reason:
GSS demand is clipped affine with finite active-set changes. Mixed-MNL demand is
smooth and does not become the GSS demand under a parameter restriction or
equivalence-preserving recentering. The prior theorem is conceptually relevant
to "when do FOCs certify equilibrium?" but is not a direct theorem from which
P1/P2 follow.

Classification:
`PARENT-CLASS ANALOGUE; NO DIRECT ABSORPTION`.

### B. Federgruen & Hu (2015; 2019; 2021)

Key papers:

- *Multi-Product Price and Assortment Competition*, Operations Research 63(3),
  572–584, DOI `10.1287/opre.2015.1380`;
- *Stability in a General Oligopoly Model*, Naval Research Logistics 66(1),
  90–102, DOI `10.1002/nav.21829`;
- *Global Robust Stability in a General Price and Assortment Competition
  Model*, Operations Research 69(1), 164–174,
  DOI `10.1287/opre.2020.2001`.

Prior theorem/object:
general piecewise-affine demand generated as a regular extension of affine
demand, with equilibrium existence/assortment characterization and later
best-response/stability results.

Absorption map:

`regular piecewise-affine demand theorem`
→ represent old/new cohort demands as piecewise-affine objects
→ to obtain GSS uniform pricing, impose an equality constraint tying one
firm's segment prices to a single common price
→ also preserve internal cohort dropout kinks while the aggregate product
remains demanded
→ derive P1/P2 square-root bounds and P3 containment
→ **PARTIALLY ABSORBED AT THE METHOD/PARENT-CLASS LEVEL; HEADLINE NOT
ABSORBED**.

Reason:
the general regular-extension literature is the strongest application-neutral
parent found. It shows that piecewise-affine global price competition is not
new as a mathematical class. But the GSS correction contains a
source-specific cross-segment common-price coupling; the searched prior
statements do not supply the exact common-price constrained inequalities
certified in P1/P2, nor the GSS welfare correction.

Stage-6 consequence:
**L1 is not a novelty claim.** It is a proof device. P1/P2 remain
source-specific correction results.

### C. Bouckaert, Degryse & van Dijk (2013)

Paper:
*Bertrand Competition with an Asymmetric No-discrimination Constraint*,
Journal of Industrial Economics 61(1), 62–83.

Prior object:
one firm must commit to uniform pricing while the rival is unconstrained;
the model combines monopolistic and competitive segments and studies entry and
welfare consequences.

Absorption map:

`asymmetric no-discrimination constraint`
→ constrained firm ↔ common-price player
→ unconstrained firm ↔ discriminatory player
→ would require replacing the paper's exogenous monopolistic/competitive
segments with the GSS Hotelling old/new allocation, switching-cost wedge, and
endogenous cohort shares
→ P1/P2/P4
→ **NOT ABSORBED**.

Reason:
this is the closest regulatory architecture found, but there is no
equivalence-preserving variable/parameter mapping from its segment structure to
the GSS game that delivers the certified GSS thresholds or welfare identity.

Classification:
`STRUCTURALLY VERY CLOSE; DIFFERENT GAME`.

### D. Gnutzmann (2014)

Paper:
*Price Discrimination in Asymmetric Industries: Implications for Competition
and Welfare*, DISCE Working Paper 19 / SSRN 2490822.

Prior object:
history-based discrimination by asymmetric firms when the entrant can also
discriminate.

Absorption map:

`entrant also discriminates`
→ impose a restriction eliminating entrant discrimination
→ strategy set materially changes
→ GSS original strategy set and its P4 welfare correction
→ **NOT ABSORBED**.

Reason:
Gnutzmann obtains different welfare conclusions by changing the entrant's
instrument. It treats earlier models without entrant discrimination as
benchmarks; it does not identify the within-GSS factor-three error or the
P1/P2 global-deviation conditions.

### E. Gehrig, Shy & Stenbacka (2012)

Paper:
*A Welfare Evaluation of History-Based Price Discrimination*,
Journal of Industry, Competition and Trade 12, 373–393.
DOI `10.1007/s10842-011-0111-8`.

Mapping:
both firms can discriminate and inherited dominance is modeled differently.

Absorption result:
`NOT ABSORBED — DISTINCT SAME-AUTHOR GAME`.

### F. Shy, Stenbacka & Zhang (2016)

Paper:
*History-based versus Uniform Pricing in Growing and Declining Markets*,
International Journal of Industrial Organization 48, 88–117.
DOI `10.1016/j.ijindorg.2016.06.002`.

Mapping:
infinite-horizon OLG Markov game with entry/exit and lock-in.

Absorption result:
`NOT ABSORBED — DYNAMIC EXTENSION, DIFFERENT EQUILIBRIUM OBJECT`.

### G. Chen, Shi & Zhang (2026)

Paper:
*Welfare of Competitive Price Discrimination with Captive Consumers*,
American Economic Journal: Microeconomics 18(3), 203–243.
DOI `10.1257/mic.20230234`.

This is the most recent high-level welfare paper located in the search.

Prior object:
duopoly with captive and contested consumers; information-design approach to
best/worst market segmentation for producer, consumer, and social surplus.

Absorption map:

`optimal information/segmentation design with captive/contested consumers`
→ would require replacing the fixed GSS old/new information structure and
switching-cost Hotelling allocation by endogenous information segmentation
→ P4 source-specific corrected welfare identity
→ **NOT ABSORBED**.

Stage-6 positioning consequence:
the correction must not be sold as a general theorem that uniform pricing is
welfare-superior to competitive price discrimination. The 2026 literature
makes clear that welfare depends on the segmentation/information environment.
P4 is a correction **inside the GSS model**.

### H. New spatial/captive-buyer equilibrium literature

Recent work such as Kawai & Nakagawa (2025),
*Price Equilibria in a Spatial Competition with Captive Buyers*, explicitly
classifies pure/mixed equilibrium regions in a spatial captive-buyer model.

Absorption result:
`NOT ABSORBED`.

The captive-buyer information structure and mixed-strategy regions differ from
the GSS switching-cost/cohort common-price game. This literature reinforces the
need to check global/corner equilibria but does not deliver P1–P4.

## Component vs whole-game novelty ledger

| Certified object | Stage-6 novelty status |
|---|---|
| L1 common-price piecewise global-BR lemma | **KILLED AS CONTRIBUTION** — generic proof device / parent-class mathematics |
| P1 exact HBP displayed-profile validity domain | **SURVIVES AS SOURCE-SPECIFIC CORRECTION** |
| P2 exact uniform displayed-profile validity domain | **SURVIVES AS SOURCE-SPECIFIC CORRECTION** |
| P3 `D_U subseteq D_HBP` / common comparison domain | **SURVIVES AS SUPPORTING CORRECTION RESULT** |
| P4 factor-three CS correction and welfare sign reversal | **SURVIVES AS HEADLINE CORRECTION** |
| complete clipped-demand equilibrium correspondence | **NOT A CONTRIBUTION CLAIM / NOT NEEDED** |
| broad welfare theorem for price discrimination | **KILLED** |
| broad theory of segmented piecewise-affine Bertrand pricing | **KILLED** |
| `Delta c` prose sign error | **ANCILLARY ERRATUM ONLY** |

## Whole-game absorption result

No searched paper provides a theorem that, under an equivalence-preserving
mapping, simultaneously gives:

1. the GSS asymmetric HBP/uniform strategy sets;
2. the old/new switching-cost Hotelling allocation;
3. the exact P1/P2 global-validity inequalities for the source's displayed
   formulas; and
4. the P4 corrected welfare identity.

Accordingly the correction is not absorbed as a whole game or as a short
application of a located parent theorem.

The strongest parent-class overlap is Federgruen–Hu's piecewise-affine price
competition framework, but the common-price cross-segment coupling and the
source-specific welfare correction remain outside the directly located
theorems.

## Exact contribution statement authorized after Stage 6

The project may claim:

> Re-evaluating Gehrig, Shy & Stenbacka (2011) with globally clipped demand
> yields two corrections. First, the displayed interior price formulas are
> Nash equilibria only on explicitly characterized parameter domains, with the
> uniform-pricing domain forming the common comparison domain. Second, on that
> domain, correcting consumer surplus reverses the paper's total-welfare
> ranking.

The project may **not** claim:

- a new general theorem for piecewise-affine Bertrand games;
- a complete equilibrium correspondence for all source parameters;
- uniqueness of the GSS game;
- uniform pricing is generally welfare superior to price discrimination;
- later literature's different welfare results are mathematically erroneous.

## Stage-2 ledger update

Stage 2 survives after theorem-aware re-kill, with two refinements:

1. the global-validity contribution is explicitly **source-specific**, not
   generic methodological novelty;
2. current 2026 captive-consumer welfare literature is added to the frontier
   and narrows the permissible welfare interpretation.

No surviving headline correction is killed.

## Canonical decision

`GO -> STAGE 7`

Stage 7 should treat welfare as a **corrected source-model comparison**, audit
the institutional/policy interpretation inherited from GSS, and determine the
appropriate exposition vehicle. It must not attempt to generalize P4 beyond the
certified model without additional theory.
