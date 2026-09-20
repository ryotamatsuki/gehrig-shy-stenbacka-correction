# Stage 3 — Candidate Mechanism Search

## Canonical verdict

`GO — SELECT ARCHITECTURE B`

## Objective

Choose the smallest correction-paper architecture that carries the certified
Stage-1 mathematical errors and the Stage-2 surviving contribution without
turning a source-specific correction into an unnecessarily broad new theory
paper.

This is a correction project, so "mechanism search" is interpreted as a search
over **correction architectures and strategic objects that must be solved**,
not as permission to add new economic ingredients to the Gehrig–Shy–Stenbacka
(2011) model.

## Strategic core that must be preserved

The source game contains one strategically important asymmetry:

- incumbent A can set cohort-specific prices under HBP;
- entrant B must set one common price across old and new consumers;
- old consumers face switching cost `sigma`, while new consumers do not;
- each cohort's Hotelling demand is clipped to `[0,1]`.

The feedback loop is therefore:

> A's segment prices shift the entrant's two cohort-specific demand schedules;
> B's one common price jointly loads on both schedules; a sufficiently large
> deviation can optimally abandon one cohort and move to a different active
> set, so the smooth interior FOC need not be B's global best response.

This coupling is exactly what the Stage-1 counterexample exploits. It is not a
new mechanism added by the correction paper; it is a strategic feature already
present in the source model that must be handled correctly.

A second, logically separate object is the welfare accounting identity: direct
integration of primitive utilities produces a factor three in
`CS^u-CS^d`, which reverses the source welfare headline on the common valid
interior branch.

## Candidate architectures

### Architecture A — arithmetic-only corrigendum

Content:

1. rederive consumer surplus;
2. correct the missing factor three;
3. reverse the welfare comparison;
4. mention the local `Delta c` prose sign error.

Smallest model: exactly the source interior formulas, taken as given.

Strategic feedback handled: none beyond the interior FOCs.

Candidate result:

`W^d-W^u=-theta(1-theta)sigma^2/(16 tau)`

conditional on valid interior equilibria.

#### Kill test

**REJECT.**

Stage 1 has already certified that the displayed HBP price triple can fail to
be a global Nash equilibrium even when the candidate cohort shares are strictly
interior. Publishing only the accounting correction would knowingly leave a
second material source error unresolved and would make the scope of the welfare
comparison ambiguous.

---

### Architecture B — welfare correction plus exact global-validity domain

Content:

1. independently reproduce the source interior candidates;
2. derive the exact global-best-response conditions under clipped demand;
3. state necessary and sufficient parameter conditions under which the
   displayed HBP interior candidate is a global Nash equilibrium;
4. perform the corresponding global-validity audit for the uniform-pricing
   candidate, because the welfare comparison requires both regimes to be valid;
5. define the common certified domain on which the two equilibria can be
   compared;
6. on that domain, give the corrected consumer-surplus and total-welfare
   identities;
7. preserve a compact exact counterexample showing why interior shares/FOCs
   alone do not certify equilibrium.

Smallest model: the source game itself. No new player, state, information
structure, cost, or timing margin is added.

Strategic feedback handled: the entrant's common price couples two clipped
cohort demands, and under uniform pricing each firm's common price must likewise
be tested against all active-set changes.

Candidate results unavailable from the source's interior analysis alone:

- an exact global-validity characterization for the displayed price formulas;
- a common parameter domain on which the published regime comparison is
  legitimate;
- a corrected welfare ranking on that certified domain;
- an exact demonstration that "strictly interior candidate shares" is not
  sufficient for global Nash under HBP.

#### Verdict

**SELECT.**

This is the smallest architecture that repairs both material defects already
known to exist.

---

### Architecture C — complete pure-price equilibrium correspondence

Content:

Architecture B plus a complete classification of every pure-strategy
equilibrium outside the displayed interior branch, including old-only,
new-only, zero-capture, full-capture, boundary, multiplicity, and possible
nonexistence regions for both HBP and uniform pricing.

Smallest model: still the source game, but the theorem object is much larger.

Strategic feedback handled: all active-set combinations globally.

Candidate result: a full equilibrium atlas over the complete parameter space.

#### Kill / downgrade test

**DOWNGRADE TO OPTIONAL.**

Stage 2 found no reason to market the active-set machinery as a new general
theorem. A complete correspondence may be useful if it is the cleanest route
to exact validity conditions or if economically important behavior outside the
published branch changes a headline conclusion. It is not justified merely to
make the correction more technical.

Stage 4 may derive pieces of the outside correspondence as lemmas or
certificates, but Architecture C does not become the paper architecture unless
Architecture B cannot be stated rigorously without it.

---

### Architecture D — expand the economic model

Examples would include entrant recognition, additional consumer histories,
endogenous information acquisition, dynamic switching, or an additional
discrimination instrument.

#### Kill test

**REJECT.**

These are distinct research questions and collide with the Stage-2 decision
that this project is a correction of GSS (2011), not a new general theory of
history-based pricing.

## Candidate comparison

Scores are diagnostic only: 5 = strongest on the stated dimension.

| Dimension | A: arithmetic only | B: welfare + validity domain | C: full correspondence | D: expanded model |
|---|---:|---:|---:|---:|
| Novelty / correction value | 4 | 5 | 4 | 2 |
| Mechanism clarity | 3 | 5 | 3 | 2 |
| Whole-game prior-art survival | 4 | 5 | 4 | 2 |
| Tractability | 5 | 4 | 2 | 1 |
| Welfare content | 5 | 5 | 5 | 3 |
| Institutional/source relevance | 4 | 5 | 4 | 2 |
| Correction-paper fit | 4 | 5 | 2 | 1 |

Architecture B dominates the feasible correction choices because it resolves
both certified material errors without requiring a parameter-space atlas that
is not itself the contribution.

## Closest-literature delta

Relative to GSS (2011), Architecture B changes **no primitive economic
assumption**. It changes the analysis:

- demand is treated as clipped globally rather than as an everywhere-interior
  affine expression;
- global best responses replace interior FOCs as the equilibrium certificate;
- consumer surplus is recomputed directly from primitive utilities;
- the welfare comparison is stated only on a domain where both compared
  equilibria have been globally certified.

Relative to later HBP papers identified at Stage 2, the project does not import
their additional pricing/information structures. Its contribution remains
source-specific.

## Benchmark / limiting cases

This is not a generalization/unification project, so the workflow's
joint-endogeneity benchmark requirement is not applicable as a novelty test.
Nevertheless Stage 4 must recover the following diagnostic limits:

- `sigma=0`: the history-based wedge disappears, so the corrected welfare
  difference must vanish;
- `theta=0` or `theta=1`: the cross-cohort welfare wedge
  `theta(1-theta)` vanishes;
- symmetric marginal costs `Delta c=0`: useful benchmark for isolating the
  switching-cost/segmentation mechanism;
- active-set boundaries: candidate formulas must connect continuously where
  the relevant clipped-demand branch permits it.

These are verification benchmarks, not claimed contributions.

## Stage-4 model contract

Stage 4 is authorized to solve **Architecture B only**, with Architecture C as
a contingent supporting derivation.

### Required Stage-4 outputs

1. Freeze the exact source strategy sets, including whether prices are
   unrestricted, nonnegative, or otherwise constrained. If the source is
   silent, record the adopted strategy domain explicitly and show which
   conclusions are invariant to the ambiguity.
2. Normalize where useful by `tau>0`, e.g.
   `s=sigma/tau` and `d=(c_A-c_B)/tau`, while preserving a transparent map
   back to source notation.
3. Write the exact clipped old/new demands under HBP and uniform pricing.
4. Derive global best-response correspondences branch by branch.
5. For the **displayed HBP interior candidate**, derive necessary and
   sufficient inequalities for every firm's displayed price to be a global
   best response, including comparisons with regime-crossing finite
   deviations.
6. Repeat the global-validity test for the **displayed uniform-pricing
   candidate**. Do not assume that interior cohort shares imply global Nash.
7. Define the common certified domain
   `D_compare = D_HBP ∩ D_uniform`.
8. On `D_compare`, independently certify:
   - `CS^u-CS^d = 3 theta(1-theta)sigma^2/(16 tau)`;
   - `pi_A^d-pi_A^u = theta(1-theta)sigma^2/(8 tau)`;
   - `pi_B^d-pi_B^u = 0`;
   - `W^d-W^u = -theta(1-theta)sigma^2/(16 tau)`.
9. Preserve the exact Stage-1 HBP deviation witness as a permanent regression
   test and search analytically first for analogous failures of the
   uniform-pricing candidate.
10. Derive outside-branch equilibria only to the extent needed to prove the
    validity conditions, boundary behavior, existence, or a correction
    statement. Do **not** expand automatically to the full Architecture-C
    atlas.
11. State all Stage-4 conclusions as Candidate Propositions and explicitly
    distinguish local/interior identities from global equilibrium claims.
12. Produce a direct-payoff evaluator independent of symbolic FOC derivations
    for global-deviation checks.

## Stage-3 kill tests

- No additional player/channel/parameter is introduced.
- The selected object creates a real strategic problem: global optimization
  over coupled piecewise demands rather than another comparative-static
  parameter.
- The paper does not claim novelty for generic clipping or piecewise quadratic
  optimization.
- The full correspondence is not authorized as headline scope without a
  Stage-4 necessity finding.

## Canonical decision

`GO — ARCHITECTURE B SELECTED`

**Paper architecture:** corrected welfare accounting + exact global-equilibrium
scope of the source's displayed interior formulas.

**Stage-4 headline target:** characterize the exact common parameter domain on
which the HBP and uniform interior candidates are genuine global Nash
equilibria, then state the corrected welfare comparison on that domain.

**Optional extension:** only the portion of the complete equilibrium
correspondence required to make that characterization exact.
