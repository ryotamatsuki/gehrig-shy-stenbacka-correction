# Stage 1 — Source & Mathematical Audit

## Source freeze

Target VOR:

- Thomas Gehrig, Oz Shy, and Rune Stenbacka
- “History-based Price Discrimination and Entry in Markets with Switching Costs: A Welfare Analysis”
- *European Economic Review* 55(5), 732–739 (2011)
- DOI `10.1016/j.euroecorev.2010.09.001`

Complete mathematical source currently available:

- 14 December 2009 author working-paper draft
- header: `Draft = loyal50.tex`
- 16 pages
- Sections 1–5, Eqs. (1)–(14), Results 1–5, footnotes, conclusion, references

The publisher VOR metadata and abstract are verified, but the complete VOR body has not been opened in this environment. Equation-level claims below therefore refer to the complete author draft unless and until the VOR PDF is directly inspected.

## Canonical model

Incumbent `A` is at 0 and entrant `B` at 1 on a unit Hotelling line. A share `1-theta` are inherited consumers and a share `theta` are new consumers. Old consumers incur switching cost `sigma` when buying from `B`. Transportation parameter `tau>0`.

Old-consumer utilities:

`u_A^o(x)=beta-p_A-tau*x`

`u_B^o(x)=beta-p_B-tau*(1-x)-sigma`

New-consumer utilities:

`u_A^n(x)=beta-q_A-tau*x`

`u_B^n(x)=beta-p_B-tau*(1-x)`

Unclipped cutoffs:

`x_o = 1/2 + (sigma+p_B-p_A)/(2 tau)`

`x_n = 1/2 + (p_B-q_A)/(2 tau)`

Actual shares are `clip(x_o,0,1)` and `clip(x_n,0,1)`.

## Independently rederived interior HBP candidate

Let `Delta c = c_A-c_B`.

`p_A^d = tau + [(2+theta)sigma + 4c_A + 2c_B]/6`

`q_A^d = tau + [4c_A + 2c_B -(1-theta)sigma]/6`

`p_B^d = tau + [2c_B+c_A-(1-theta)sigma]/3`

`x_o^d = 1/2 + [(2+theta)sigma-2 Delta c]/(12 tau)`

`x_n^d = 1/2 - [(1-theta)sigma+2 Delta c]/(12 tau)`

`m_A^d = 1/2 + [(1-theta)sigma-Delta c]/(6 tau)`

These identities solve the interior FOCs. They are not by themselves a global-equilibrium certificate.

## Independently rederived uniform-pricing candidate

`p_A^u = tau + [2c_A+c_B+(1-theta)sigma]/3`

`p_B^u = tau + [2c_B+c_A-(1-theta)sigma]/3`

`x_o^u = 1/2 + [(2theta+1)sigma-Delta c]/(6 tau)`

`x_n^u = 1/2 - [Delta c+2(1-theta)sigma]/(6 tau)`

`m_A^u=m_A^d`

Thus the aggregate incumbent-share identity survives on the common interior branch.

## Consumer surplus and welfare

Direct integration of primitive utilities gives:

`CS^u-CS^d = 3 theta(1-theta)sigma^2/(16 tau)`.

The source draft's Eq. (9) reports the same expression without the factor 3.

Independent profit substitution gives:

`pi_A^d-pi_A^u = theta(1-theta)sigma^2/(8 tau)`

and

`pi_B^d-pi_B^u = 0`.

Therefore:

`W^d-W^u = -theta(1-theta)sigma^2/(16 tau)`

for `0<theta<1`, `sigma>0`, `tau>0`, conditional on the compared interior equilibria being valid.

This reverses the source draft's Eq. (14), Result 5, and the corresponding welfare headline.

## Exact global-deviation witness

Take:

`theta=1/2, tau=1, sigma=23/10, c_A=c_B=0`.

The published/interior candidate gives:

`p_A=47/24`

`q_A=97/120`

`p_B=37/60`

`x_o=47/48`

`x_n=97/240`

so both displayed shares are strictly interior.

Entrant candidate profit:

`1369/7200`.

The old-consumer zero-demand boundary for the entrant is:

`p_A-sigma+tau = 79/120`.

The new-only branch vertex is:

`p_B'=217/240`,

which lies above that boundary and yields:

`pi_B(p_B')=47089/230400`.

Exact gain:

`3281/230400 > 0`.

Hence the displayed interior HBP price triple is not a global Nash equilibrium on the unrestricted parameter domain of the source draft.

## Additional source-domain issue

The source defines `Delta c=c_A-c_B`. Under that definition, a more efficient entrant has `c_B<c_A`, hence `Delta c>0`. The prose sentence after Result 1 that associates entrant efficiency with `Delta c<0` reverses the sign.

## What survives Stage 1

- The HBP and uniform interior FOC algebra.
- Aggregate-share equality `m_A^u=m_A^d` on the interior branch.
- Result 3's sign `CS^u>CS^d` for positive interior parameters, but not its reported magnitude.
- Entrant-profit equality and the associated entry-invariance identity, conditional on the compared equilibria and entry-cost comparison being valid.

## Open mathematical work

Stage 1 does not certify a replacement global equilibrium correspondence. Stage 4/4A must derive exact active-set/global-best-response conditions, including old-only/new-only/full-capture/zero-capture branches and equality boundaries.

## Verification artifact

A separate exact-arithmetic Stage-1 recheck is stored at:

`code/stage01_independent_recheck.py`

The prior audit script remains an independent historical artifact rather than the sole basis for this Stage-1 verdict.

## Canonical verdict

`GO`

## Next-stage contract

Stage 2 must determine whether the welfare correction, equilibrium-domain correction, or a complete-correspondence result has already been disclosed or is directly absorbed by later history-based/behavior-based pricing literature.
