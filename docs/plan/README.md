# Plan working papers

These papers back [PLAN.md](../../PLAN.md). They come from the scope review of 29.10.2026, where fifteen review agents each took one area group or one cross-cutting question across the whole mapping in `analyse/`. They were then edited to agree with PLAN.md. **Where a paper and PLAN.md disagree, PLAN.md wins.** For a single function, [scope.csv](scope.csv) is the source of truth.

| File | Question it answers |
|---|---|
| [scope.csv](scope.csv) | Which tier does each of the 676 mapped functions belong to (M0, M1, M2, LATER, CUT), what is its simplest lawful version, and why? Columns: `id, area, name_en, name_no, old_mvp, weight, tier, simplest_lawful_version, reason` |
| [ready-to-build.md](ready-to-build.md) | What must be in place before any code, before M0 goes live, and before M1 pilots: owner, lead time and who to ask |
| [timeline.md](timeline.md) | How much the team can deliver, how big M0 and M1 are, which decisions conflict, and the milestone plan with go/no-go criteria |
| [questions.md](questions.md) | Which open questions block M0 or M1, the new question set for Peter and Sander (replaces `fase1.json`), triage of all ~300 open items, and a recommendation for each of B1–B43 |
| [data-model.md](data-model.md) | The minimal core data model (25 tables for M0, 12 more for M1, 1 for M2), history policy, merges, sensitive fields and an ER diagram |
| [api-mcp.md](api-mcp.md) | What "API first" means for a three-person team, what must be right from day one, and the first operations and MCP tools |
| [prototype-stack.md](prototype-stack.md) | Which stack Sjur's prototype uses, how it keeps the Rust rewrite cheap, and how it runs on localhost (B47, B48, D13) |
| [testing.md](testing.md) | How we prove payroll is correct: golden cases, withholding conformance, a-melding validation, parallel-run protocol, release diff |
| [competitors.md](competitors.md) | Table stakes against SD Worx breadth, cheap differentiators, and what the cheapest competitors charge |
| [areas/](areas/) | One scope review per area group: org-per, lon-kjo, trk-pen, fra-tid-utl, myn-bet, reg-rap, byr-por-orl, pla-sik-mig |

Tier definitions:
- **M0 – First payroll:** our own company's payroll. It is shadow-run in November and December 2026 and goes live from period 2027-02 (planning date; 2027-01 is a stretch).
- **M1 – MVP:** 3–5 direct customers with 20–150 employees run a normal month end to end.
- **M2 – Accounting firms:** firms run payroll for many clients.
- **LATER:** on the roadmap after the MVP, with a trigger.
- **CUT:** off the roadmap until a paying customer asks.

The Norwegian source material stays in `analyse/`: research reports, night-work findings and the mapping data in `analyse/build/data`.
