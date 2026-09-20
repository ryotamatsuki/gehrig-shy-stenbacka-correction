# Gehrig–Shy–Stenbacka (2011) Correction

Independent correction project for:

Thomas Gehrig, Oz Shy, and Rune Stenbacka (2011),
“History-based Price Discrimination and Entry in Markets with Switching Costs:
A Welfare Analysis,” *European Economic Review* 55(5), 732–739.
DOI: `10.1016/j.euroecorev.2010.09.001`.

## Current workflow state

This project follows `research-paper-workflow` v2.3 at commit
`9eb616bd31ea3a9ef3c29e288228ed962c44c9cf`.

- Stage 0 — GO
- Stage 1 — GO
- Stage 2 — GO
- Stage 3 — GO — Architecture B selected
- Stage 4 — GO
- Stage 4A — GO — independent certification PASS
- Stage 5 — NOT TRIGGERED
- Stage 6 — NOT STARTED — next
- Stage 7+ — NOT STARTED

The repository has been initialized early as a dedicated research workspace by
explicit project decision. This does **not** mark workflow Stage 9 complete and
does not authorize manuscript construction before the theory-freeze gates.

## Certified starting findings

Stage 1 independently rederived three issues from the source model:

1. Consumer surplus:
   `CS^u-CS^d = 3 theta(1-theta) sigma^2/(16 tau)`.
2. Hence:
   `W^d-W^u = -theta(1-theta) sigma^2/(16 tau)`
   on the common valid interior branch.
3. The displayed interior HBP prices need not be a global Nash equilibrium on
   the unrestricted parameter domain because the entrant can profitably cross
   an active-set boundary.

The project also records an ancillary prose sign error involving
`Delta c=c_A-c_B`.

## Repository layout

- `PROJECT_STATE.md` — canonical workflow state and claim restrictions.
- `audit/` — stage-gate records and search logs.
- `code/` — independent symbolic/exact verification.
- `sources/` — source lineage and provenance only; no copyrighted VOR is
  committed without permission.
- `paper/` — reserved for manuscript construction after the applicable
  workflow gates.
- `.github/workflows/` — reproducibility checks.

## Parent audit provenance

The discovery audit remains preserved in
`ryotamatsuki/ozshypapers`, branch
`final-cleanroom-theorem-audit-20260919`.

This correction repository treats that audit as provenance, not as proof:
proof-critical identities are independently rechecked here.
