# N6 Amendment — Elsevier Generative-AI Policy Re-audit

Date: 2026-09-21
Target: Research in Economics
Parent N6 closure commit: `834e7442bd83930210dd141589445865c494928a`

## Trigger

The current Elsevier "Generative AI policies for journals" were re-read against the actual project workflow before N7 submission freeze.

## Finding

The existing manuscript-preparation declaration correctly disclosed ChatGPT use, but it described the use too narrowly. The project also used ChatGPT supportively in the research/verification process, including mathematical consistency checking and drafting/review of verification code/workflow material. Elsevier distinguishes manuscript-preparation disclosure from AI use in research methods and specifically calls for detailed disclosure of AI-assisted code development in the methodology.

## Amendment

The manuscript now:

1. renames the verification section to `Verification methodology and reproducibility`;
2. adds a detailed research-process disclosure identifying OpenAI ChatGPT/OpenAI, the scope of mathematical and code/workflow assistance, human oversight, and the evidentiary boundary;
3. states that AI output was not treated as evidence;
4. states that the reported results remain reproducible from archived Python/SymPy and Lean artifacts without ChatGPT;
5. revises the separate pre-references declaration so it covers manuscript-preparation uses and points to the methodology disclosure for research-process uses.

A separate `audit/AI_USE_RECORD.md` records tool scope, oversight, reproducibility, documentation, and the remaining account-level terms/privacy check.

## Theory-freeze effect

None. No theorem, equilibrium domain, counterexample, welfare identity, resource decomposition, source-version claim, or formal proof artifact changed. N1 is not reopened.

## Remaining external check

Elsevier also requires the author to check the AI tool's terms/privacy conditions, including rights over unpublished manuscript inputs. Repository automation cannot verify account-level data-control settings or retrospectively certify every project session.

Therefore:

`CONDITIONAL PASS — MANUSCRIPT AI DISCLOSURE RECERTIFIED`

N7 submission freeze remains blocked only until the author confirms the applicable AI-tool terms/account settings satisfy the Elsevier privacy/confidentiality/intellectual-property/no-unrelated-training requirement.
