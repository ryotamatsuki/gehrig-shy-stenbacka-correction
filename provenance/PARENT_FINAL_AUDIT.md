> Frozen provenance snapshot imported from `ryotamatsuki/ozshypapers`, branch `final-cleanroom-theorem-audit-20260919`, path `audits/history_based_entry_welfare_2011_final.md` on 2026-09-20. The canonical correction analysis is in this repository's `audit/` and `code/` directories.\n\n# Final clean-room audit — Gehrig, Shy & Stenbacka (2011)

## 0. Final verdict

**Target:** Thomas Gehrig, Oz Shy, and Rune Stenbacka, “History-based Price
Discrimination and Entry in Markets with Switching Costs: A Welfare Analysis,”
*European Economic Review* 55(5), 732–739 (2011), DOI
`10.1016/j.euroecorev.2010.09.001`.

**Frozen mathematical source:** complete 14 December 2009 author working-paper
draft, `Draft = loyal50.tex`, 16 pages. The publisher VOR page was checked for
metadata and abstract but its full text was subscriber-restricted. The source
relationship is documented in
`sources/history_based_entry_welfare_2011_source_record.md`.

**Final audit status:** `FINAL_AUDITED_MATERIAL_ERROR`

**Error certification:**

1. `CERTIFIED_ERROR` — direct integration of the model gives
   `CS^u - CS^d = 3 theta(1-theta)sigma^2/(16 tau)`, whereas Eq. (9) reports
   the same expression without the factor 3. Combining the corrected consumer
   surplus loss with the paper's correct incumbent-profit difference gives
   `W^d - W^u = -theta(1-theta)sigma^2/(16 tau)`, reversing Eq. (14), Result 5,
   and the associated “profit gain exceeds consumer loss” headline.
2. `CERTIFIED_ERROR` — the displayed interior prices are not a global Nash
   equilibrium on the source's stated parameter domain. A regime-crossing
   deviation by the entrant is profitable even when both displayed market
   shares are strictly interior.
3. `CERTIFIED_ERROR` — the explanatory sentence after Result 1 says that a
   more efficient entrant corresponds to `Delta c < 0`, contradicting the
   paper's own definition `Delta c = c_A-c_B`, under which the entrant is more
   efficient when `Delta c > 0`.

The first two findings are correction-grade and material. Result 3's consumer
surplus ranking remains correct in sign in the interior regime, but its stated
magnitude is wrong. Result 4's entry-invariance identity remains correct
conditional on the interior equilibrium and the same entry-cost comparison.

---

## 1. Gate 1 — SOURCE FREEZE

The complete 2009 author draft was opened from the source URL and read through
the conclusion and references. It contains the full model, all displayed
equations, Results 1–5, footnotes, and no appendix or supplement. The 2011 VOR
metadata, DOI, PII, pages, and publication lineage were separately fixed. The
VOR PDF itself was not counted as opened; the working paper is the canonical
mathematical source for this audit.

The source record lists the exact VOR/working-paper links, access attempts,
version relationship, and prior-disclosure search.

---

## 2. Gate 2 — THEOREM LEDGER

Printed page references below refer to the complete 2009 draft. The source uses
“Result” rather than theorem/proposition numbering.

| Source | Formal result or claim | Assumptions/domain recorded | Audit status |
|---|---|---|---|
| p. 4, Eqs. (1)–(3) | Old/new consumer utilities and Hotelling cutoffs `x` and `x^n` | `x in [0,1]`, `tau>0`, `sigma>=0`; full coverage; incumbent can identify old consumers | Correct algebraically; clipping/parameter restrictions omitted |
| p. 6, Eqs. (4)–(5) | History-based prices, cohort shares, and incumbent share `m_A^d` | Interior old/new shares; `theta in (0,1)` | Correct FOC solution only; not globally certified |
| p. 6, Result 1 | Dominance with HBP if `sigma > Delta c/(1-theta)` | Same interior regime and `1-theta>0` | Threshold identity correct; narrative cost-sign sentence wrong |
| p. 7, Eq. (6) | Uniform prices, cohort shares, and `m_A^u=m_A^d` | Interior shares | Correct FOC solution only; not globally certified |
| p. 8, Result 2 | Persistence of dominance invariant across HBP and uniform pricing | Compare Eq. (5) and Eq. (6) in common admissible region | Conditional identity correct |
| pp. 9–10, Eqs. (7)–(9) | Consumer surplus under HBP and uniform pricing; `CS^u-CS^d` | Interior cutoffs and utility integrals | Eq. (9) misses factor 3 |
| p. 11, Eq. (10) | Entrant profit is identical under both pricing regimes | Interior entry equilibrium | Algebraically correct conditional on valid equilibrium |
| p. 11, Result 4 | Entry decision invariant to pricing regime | No sunk/fixed entry cost in formal model; same entrant profit | Conditional result correct |
| p. 12, Eqs. (11)–(13) | Incumbent profits and profit gain from HBP | Interior equilibrium | Incumbent difference correct |
| p. 13, Eq. (14) | Social-welfare difference | `W=CS+pi_A+pi_B` | Sign/magnitude wrong because Eq. (9) is wrong |
| p. 13, Result 5 | HBP promotes social welfare | Same model | False; corrected sign favors uniform pricing |
| pp. 13–15, conclusion | HBP profit gain exceeds consumer loss; exploitation not exclusion | Same interior claims | Profit/loss headline is reversed; entry statement remains conditional |

No additional formal lemma, theorem, corollary, appendix result, or figure-based
relationship appears in the complete source.

---

## 3. Gate 3 — MODEL CANONICALIZATION

### 3.1 Players and timing

- Incumbent firm `A` is at the left endpoint of a unit Hotelling line; entrant
  `B` is at the right endpoint.
- A proportion `1-theta` of consumers are inherited/old and a proportion
  `theta` are new, with `0<theta<1` in the nondegenerate model.
- Consumers are uniformly distributed on `[0,1]` and buy one unit under the
  paper's full-coverage assumption.
- Under HBP, `A` chooses two prices: `p_A` to old consumers and `q_A` to new
  consumers. `B` chooses one price `p_B` because it has no purchase-history
  information.
- Under uniform pricing, `A` is constrained to `p_A=q_A` and `B` still chooses
  `p_B`.

The source does not specify a simultaneous-game notation or formal tie-breaking
rule. The audit interprets prices as simultaneous strategic choices and uses
weak utility inequalities only when testing boundary correspondences.

### 3.2 Primitives and payoffs

For an old consumer at `x`:

`u_A^o(x)=beta-p_A-tau*x`,

`u_B^o(x)=beta-p_B-tau*(1-x)-sigma`.

For a new consumer:

`u_A^n(x)=beta-q_A-tau*x`,

`u_B^n(x)=beta-p_B-tau*(1-x)`.

Here `tau>0` is the horizontal differentiation parameter and `sigma>=0` is the
old-consumer switching cost. Marginal costs are `c_A,c_B`; the source does not
state an explicit nonnegative-cost restriction. The source assumes no fixed or
entry costs in the formal entry comparison.

The un-clipped cutoffs are

`x = 1/2 + (sigma+p_B-p_A)/(2*tau)`,

`x^n = 1/2 + (p_B-q_A)/(2*tau)`.

Actual shares must be `clip(x,0,1)` and `clip(x^n,0,1)`. The source's displayed
FOCs silently use the interior values.

Strategy bounds are not explicitly stated. The audit checks the result even
under the standard nonnegative-price restriction; the counterexample uses only
positive prices and therefore does not rely on negative-price deviations.

### 3.3 Equilibrium and welfare objects

Under HBP:

`pi_A=(1-theta)(p_A-c_A)x + theta(q_A-c_A)x^n`,

`pi_B=(p_B-c_B)[(1-theta)(1-x)+theta(1-x^n)]`.

Under uniform pricing, set `q_A=p_A`. Consumer surplus is the population-weighted
integral of the four utility expressions, including `-sigma` for old consumers
who switch. Total welfare is defined by the source as

`W=CS+pi_A+pi_B`.

---

## 4. Gate 4 — CLEAN-ROOM PROOF

### 4.1 HBP interior FOCs

Holding `p_B` fixed, the incumbent's old and new problems separate. For an
interior share, `dx/dp_A=dx^n/dq_A=-1/(2*tau)`, so

`p_A-c_A=2*tau*x`,

`q_A-c_A=2*tau*x^n`.

The entrant has total interior demand `1-m_A`, with derivative `-1/(2*tau)`,
so

`p_B-c_B=2*tau(1-m_A)`.

Solving these three identities gives exactly the source's Eq. (4):

`p_A^d=tau+[(2+theta)sigma+4c_A+2c_B]/6`,

`q_A^d=tau+[4c_A+2c_B-(1-theta)sigma]/6`,

`p_B^d=tau+[2c_B+c_A-(1-theta)sigma]/3`.

Substitution gives Eq. (5):

`x^d=1/2+[(2+theta)sigma-2 Delta c]/(12 tau)`,

`x^{n,d}=1/2-[(1-theta)sigma+2 Delta c]/(12 tau)`,

`m_A^d=1/2+[(1-theta)sigma-Delta c]/(6 tau)`,

where `Delta c=c_A-c_B`.

### 4.2 Uniform interior FOCs

When `p_A=q_A`, the incumbent's total share has derivative `-1/(2*tau)`
with respect to its common price. Therefore

`p_A-c_A=2*tau*m_A`,

and the entrant FOC remains `p_B-c_B=2*tau(1-m_A)`. Solving yields Eq. (6):

`p_A^u=tau+[2c_A+c_B+(1-theta)sigma]/3`,

`p_B^u=tau+[2c_B+c_A-(1-theta)sigma]/3`,

`x^u=1/2+[(2theta+1)sigma-Delta c]/(6 tau)`,

`x^{n,u}=1/2-[Delta c+2(1-theta)sigma]/(6 tau)`,

and

`m_A^u=m_A^d`.

Thus Results 1 and 2's share-comparison algebra is correct where both regimes'
interior equilibria are actually admissible.

### 4.3 Consumer surplus and profit recomputation

Directly integrating the four primitive utility functions at the two interior
solutions gives

`CS^u-CS^d = 3 theta(1-theta)sigma^2/(16 tau)`.

The source reports the same expression without the factor 3 in Eq. (9). The
incumbent and entrant profit differences from independent substitution are

`pi_A^d-pi_A^u = theta(1-theta)sigma^2/(8 tau)`,

`pi_B^d-pi_B^u = 0`.

Consequently,

`W^d-W^u`
`= (pi_A^d-pi_A^u) - (CS^u-CS^d)`
`= -theta(1-theta)sigma^2/(16 tau) < 0`

for `0<theta<1`, `sigma>0`, and `tau>0`.

The source's Eq. (14), Result 5, and the headline statement that the incumbent's
profit gain exceeds the consumer loss are therefore false under the source's
own welfare definition. The direct integrals also reproduce the factor-3
discrepancy in the expanded consumer-surplus expressions preceding Eq. (9).

### 4.4 Concrete interior numerical witness

Take `theta=1/2`, `tau=1`, `sigma=1`, and `c_A=c_B=0`. The displayed interior
prices and shares are:

`p_A^d=17/12`, `q_A^d=11/12`, `p_B^d=5/6`,

`x^d=17/24`, `x^{n,d}=11/24`;

`p_A^u=7/6`, `p_B^u=5/6`,

`x^u=5/6`, `x^{n,u}=1/3`.

All shares are strictly interior. Direct integration gives

`CS^u-CS^d=3/64`,

`pi_A^d-pi_A^u=1/32`, and

`W^d-W^u=-1/64`.

The source's Eq. (9)/(14) would instead report `1/64` for both the consumer
surplus gap and the positive welfare gap.

---

## 5. Gate 5 — CORNER / BOUNDARY AUDIT

### 5.1 Interior-share domains omitted by the source

For HBP, the displayed shares require

`-6tau < (2+theta)sigma-2 Delta c < 6tau`,

`-6tau < (1-theta)sigma+2 Delta c < 6tau`.

For uniform pricing they require

`-3tau < (2theta+1)sigma-Delta c < 3tau`,

`-3tau < Delta c+2(1-theta)sigma < 3tau`.

No corresponding restriction is stated in the complete source. For example,
`theta=1/2`, `tau=1`, `sigma=10`, and `c_A=c_B=0` gives the HBP displayed old
share `x=31/12>1`. In the actual clipped-demand problem, old consumers are
already fully captured by `A`, so increasing `p_A` up to the old full-capture
boundary is profitable. The displayed FOC price is not an equilibrium.

### 5.2 Exact equality and tie cases

- `m_A=1/2` is equality, not market dominance; Result 1 uses a strict inequality.
- `sigma=0` makes the consumer-surplus and profit differences zero.
- `theta=0` or `theta=1` collapses one cohort and makes the strict welfare
  inequalities weak.
- `x=0,1` or `x^n=0,1` creates a kink and requires clipping.
- `p_A-c_A=2tau*x`, `q_A-c_A=2tau*x^n`, or `p_B-c_B=2tau(1-m_A)` at a boundary
  is not sufficient for global optimality.
- Full capture, zero capture, and the old-only/new-only entrant branches all
  require separate active-set comparisons.
- The source does not specify consumer tie-breaking at an indifference cutoff.

---

## 6. Gate 6 — GLOBAL DEVIATION AUDIT

### 6.1 Incumbent segment best responses

For one HBP segment with effective rival price `r` (where `r=p_B` for new
consumers and `r=p_B+sigma` for old consumers), the globally optimal incumbent
price is piecewise:

- zero incumbent demand if `r<c_A-tau`;
- interior price `(r+c_A+tau)/2` if `c_A-tau <= r <= c_A+3tau`;
- full incumbent demand at `r-tau` if `r>c_A+3tau`.

The source uses only the middle branch. Thus the incumbent FOCs are globally
valid only after these active-set conditions are checked.

### 6.2 Entrant regime-crossing deviation

The entrant's demand is a weighted sum of two clipped linear segments. At a price
above `p_A-sigma+tau`, old consumers all remain with `A`, while the entrant can
still sell to new consumers. A new-only local optimum is

`p_B^{new-only}=(q_A+c_B+tau)/2`.

The following all-positive-price witness is inside the source's displayed
interior-share formulas:

`theta=1/2`, `tau=1`, `sigma=23/10`, `c_A=c_B=0`.

The source prices and shares become

`p_A=47/24`, `q_A=97/120`, `p_B=37/60`,

`x=47/48`, `x^n=97/240`.

The candidate entrant profit is

`pi_B(p_B)=1369/7200 ≈ 0.190139`.

At the new-only deviation `p_B=217/240`, which lies above the old full-capture
boundary `p_A-sigma+tau=79/120`, the entrant earns

`pi_B(217/240)=47089/230400 ≈ 0.204379`.

The deviation gain is `3281/230400>0`. Therefore the displayed price triple is
not a Nash equilibrium even though both displayed cohort shares are strictly
between zero and one. This is a certified global-deviation failure, not merely
an out-of-domain corner.

### 6.3 Other deviations

The audit explicitly checked low-price/full-capture, high-price/no-demand,
old-only, new-only, and regime-crossing branches. The source's single interior
FOC system does not compare all of them. The code retains the piecewise demand
function and the exact new-only witness for reproducibility.

---

## 7. Gate 7 — EXISTENCE / UNIQUENESS / COMPLETE CORRESPONDENCE

The source calls the Eq. (4) prices “uniquely-determined equilibrium prices,”
but it neither states the active-set restrictions needed for the interior system
nor constructs the full best-response correspondence. The certified deviation
above disproves that unqualified uniqueness claim.

The complete correspondence is parameter-dependent and must include at least:

- the all-interior branch;
- old-only and new-only entrant-demand branches;
- full-capture and zero-capture boundaries for each cohort;
- equality/tie branches at clipped cutoffs; and
- possible no-entry/zero-profit outcomes when entry is an optional action.

No asymmetric price triple, boundary branch, or continuum is certified here as
a universal replacement. The audit therefore does not certify the paper's global
uniqueness or a complete equilibrium correspondence. It certifies the narrower
failure: the stated interior triple is not globally valid on the paper's
unrestricted parameter set.

---

## 8. Gate 8 — COMPARATIVE STATICS

Within the interior algebra, the source's price/share signs are as follows:

| Object | Derivative with respect to `sigma` | Domain qualification |
|---|---:|---|
| `p_A^d` | `(2+theta)/6>0` | interior HBP |
| `q_A^d` | `-(1-theta)/6<0` | `0<theta<1` |
| `p_B^d` | `-(1-theta)/3<0` | `0<theta<1` |
| `x^d` | `(2+theta)/(12tau)>0` | before clipping |
| `x^{n,d}` | `-(1-theta)/(12tau)<0` | before clipping |
| `p_A^u` | `(1-theta)/3>0` | interior uniform |
| `p_B^u` | `-(1-theta)/3<0` | interior uniform |
| `x^u` | `(2theta+1)/(6tau)>0` | before clipping |
| `x^{n,u}` | `-(1-theta)/(3tau)<0` | before clipping |
| `m_A^d=m_A^u` | `(1-theta)/(6tau)>0` | before clipping |

The entrant-profit formula is

`pi_B=[Delta c-(1-theta)sigma+3tau]^2/(18tau)`.

Its sign claims require the interior positive-bracket region
`Delta c-(1-theta)sigma+3tau>0`; at the zero-bracket boundary the derivative
signs become weak or change after clipping. The source does not state this
qualification.

The corrected welfare comparative static is

`d(W^d-W^u)/d sigma = -theta(1-theta)sigma/(8tau)<0`

for positive `sigma`. This is the opposite of the source's Eq. (14) implication.

---

## 9. Gate 9 — WELFARE / CONCLUSION AUDIT

The consumer-surplus integrals include the switching-cost disutility exactly as
the source writes it. Prices are transfers and cancel against firm profits in
total welfare, while transport and switching costs remain real losses. The
correct interior comparison is:

| Quantity | Clean-room result | Source claim |
|---|---:|---:|
| `CS^u-CS^d` | `3 theta(1-theta)sigma^2/(16tau)` | `theta(1-theta)sigma^2/(16tau)` |
| `pi_A^d-pi_A^u` | `theta(1-theta)sigma^2/(8tau)` | same |
| `pi_B^d-pi_B^u` | `0` | same |
| `W^d-W^u` | `-theta(1-theta)sigma^2/(16tau)` | positive `theta(1-theta)sigma^2/(16tau)` |

This propagates from Eq. (9) to Eq. (14), Result 5, the abstract's “profit gain
exceeds” sentence, and the conclusion. The error is therefore a headline
conclusion reversal, not a harmless local typo.

The source's consumer-surplus ranking (`CS^u>CS^d`) remains true for positive
interior parameters, and the corrected welfare result also favors uniform
pricing, but for the opposite accounting reason from the source's Result 5.

---

## 10. Gate 10 — PRIOR DISCLOSURE AUDIT

The following were searched using exact title, DOI/PII, author names, and Result/
welfare phrases:

- ScienceDirect, RePEc/IDEAS, EconPapers, Hanken's institutional record,
  ResearchGate, and Oz Shy's publication list;
- erratum, corrigendum, comment, reply, and correction searches;
- later papers by the same authors; and
- the 2012 same-author *A Welfare Evaluation of History-Based Price
  Discrimination*.

No correction or comment addressing the factor 3, the welfare sign, or the
regime-crossing deviation was located. The 2012 paper is a distinct model with
both firms able to price discriminate and is not a disclosure of these findings.
The accessible VOR abstract continues to state the disputed profit-versus-loss
headline, but the VOR body was not accessible for equation-level verification.

---

## 11. Gate 11 — FINAL VERDICT + REPRODUCIBILITY

`FINAL_AUDITED_MATERIAL_ERROR`

Certified findings:

- missing factor 3 in the consumer-surplus difference;
- reversed social-welfare sign and false Result 5/headline conclusion;
- unqualified global-equilibrium/uniqueness claim fails under an explicit
  positive-price deviation; and
- a local sign error in the interpretation of `Delta c`.

The source remains useful for the conditional interior FOC algebra and the
entry-invariance identity, but those identities are not a complete global
equilibrium audit.

Reproduce with:

```text
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  code/history_based_entry_welfare_2011_cleanroom.py
```

The script checks the FOCs, share equality, direct welfare integrals, equality/
boundary cases, clipping, and the exact profitable regime-crossing deviation.

