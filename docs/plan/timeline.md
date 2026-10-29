# Timeline and feasibility review – Brutto (as of 29.10.2026)

> **Status:** Working paper from the scope review of 29.10.2026. [`PLAN.md`](../../PLAN.md) is the main plan; where this paper and `PLAN.md` disagree, `PLAN.md` wins. Where they differ, this paper keeps its own analysis and states what `PLAN.md` decided.
>
> **What this paper is for:** the capacity and effort estimates, the feasibility of each possible go-live month, the conflicts between decisions B1–B43, and the milestone plan that `PLAN.md` §1, §3, §6.4 and §11 are built on.

Reviewer role: timeline and feasibility critic. Sources: `analyse/build/data/design.json` (B11, B16, B19, B22–B28, B37, B38, B41, B42, `oversikt.datoer`), `analyse/research/R3-kritikk-strategi.md` §2, §3.2, §4.5, §7, `analyse/research/R3-kritikk-domene.md` (c), `analyse/research/R0-matrix-lonn.md` §7, `analyse/natt/morgen.md`, `analyse/natt/funn/N06.md`, `N13.md`, `N14.md`, `N39.md`, `analyse/build/data/fase1.json` (J13, M01, M02, P09), and the function list (`analyse/build/data/omr-K*.json`).

Estimates are mine unless a source is cited. "Dev-month" means one unassisted senior developer-month, the unit R3 used. That keeps the numbers comparable with R3's ~61 dev-months for its MVP.

---

## 0. Verdict

1. **B19 as written cannot be delivered.** It says "own payroll in Brutto for November 2026, whole system finished during November". The November payday is about 3–4 weeks away. Two developers have about 1.5–3 dev-month-equivalents of capacity in that window. The B42 MVP needs roughly 65–95 dev-months, and even M0 needs 6–9 in this paper's first estimate (`PLAN.md` §1.3: 20–31 dev-weeks, about 5–8 dev-months, after the M0 cuts). Going live for November would also break B16, which requires two parallel periods equal to the øre (Norwegian cent) before production. It would also split income year 2026 across two systems.
2. **What November can realistically give is a shadow run.** Brutto calculates November after the fact, before Christmas. The result is compared to the øre with the existing system. Brutto also generates a November a-melding file (the monthly employer report to the tax authority, NAV and SSB) and validates it, but does not submit it. The old system keeps paying and submitting. **A shadow run has no deadline tied to payday**, so it can finish by 18.12.2026.
3. **December 2026 is the worst possible first live month.** It is the best month to shadow, because it exercises halvt trekk (half withholding).
4. **January 2027 (period 2027-01) is the earliest sensible first live month for M0**, if two shadow months (November and December) match to the øre by 15.1.2027. Starting in January avoids a split year and starts on the 2027 rule set. My probability is about 40% for January, about 65% for February and about 80% for March 2027. February or March only needs a one- or two-month year-to-date import. **`PLAN.md` §0 and §3 turn this into the plan: 2027-02 is the planning date (≈65 %), 2027-01 the stretch (≈40 %) and 2027-03 the latest. If shadow #1 slips past 31.12.2026, go-live moves to 2027-02 automatically.**
5. **External pilots should go live on a-melding 2.4 in 2028, not on 2.3 in 2027.** With **two developers only**, even a slimmed M1 is unlikely to be ready for parallel runs in autumn 2027. The realistic pilot date is then **1.8.2028**, with 1.3.2028 as the optimistic case. Pilots with period 2028-01, after parallel runs in October and November 2027, need about 2 more developers starting by 1.4.2027 and a payroll specialist from Q2 2027. M1 must also be held to about 36–42 dev-months, and even then January 2028 is roughly 50/50 at base agent productivity. **Decided in `PLAN.md` (§0, §3, §6.4, D12):** pilots live 1.8.2028 is the plan date. Period 2028-01 is a stretch, under 50 %, that needs two developers signed by **18.12.2026** (gate HIRE) so they can start by 1.4.2027 after three months' notice. G2 (29.1.2027) calibrates and re-forecasts M1, but no longer decides the hiring.
6. B19, B42 and B41 should be reworded and B22, B25 and B26 re-dated (§5). B23's capital figures assume a 14-FTE company and do not describe this team. **Decided in `PLAN.md` §8:** drop B42 (and B31); reword B19, B37, B41 and B23; activate B22; tighten B25; re-date B26; and add B44 (the current system submits all of income year 2026), B45 (accounting firms are M2; consequence: no firm-client revenue before 2029 in the base case) and B46 (A07-vs-ledger is a separate product line).

---

## 1. Assumptions

| # | Assumption | If wrong |
|---|---|---|
| A1 | Peter and Sander are full-time on Brutto from November 2026, both experienced in Rust, and the team has no other developers or contractors. | Every capacity figure scales with it. |
| A2 | Sjur can give 15–20 h/week to payroll-domain work (golden cases, mapping, sign-off, shadow diffs). The rest goes to CEO work, sales, interviews, fundraising and authority contact. That is about 180–250 h per quarter. R3 assumes one full-time payroll specialist gives 1,400–1,500 productive hours a year [R3 §2.3]. | If it is less, the domain work, not the coding, sets the dates. |
| A3 | The team's employer entity already runs payroll in a commercial system. That system can export 2026 payslips, the submitted a-meldinger, year-to-date (YTD) values and the holiday-pay base (feriepengegrunnlag), and it stays licensed for at least 12 months. | Without a reference there can be no shadow run. Go-live then means going live blind. `PLAN.md` §2.4 item 2: check this week that the export is at line level, not only PDFs. |
| A4 | Own payroll matches the M0 profile used in the review (now `PLAN.md` §1.1): ≤10 employees, fixed monthly salary, one entity with one sub-unit, tabelltrekk or prosenttrekk (table-based or percentage tax withholding), AGA (arbeidsgiveravgift, employer's social security contribution) in one zone. If the company has OTP (obligatory occupational pension), AGA on the premium must also be in M0 (D-01, `PLAN.md` D10). | OTP is a small addition but needed for equality to the øre. |
| A5 | Coding-agent productivity is uncertain. I use three multipliers on effective developer time: ×1.3 (R3's own: ×1.5 on the ~60% that is pure coding), ×1.8 (base) and ×2.5 (optimistic). B38 requires human review of all code touching money, access and the authorities, and that caps the gain. | **Measure it on M0** (§2.4). |
| A6 | Overhead is 30% of raw developer time: meetings, review of agent output, infrastructure, authority onboarding (3–5 admin days per N06), running own payroll and fixing bugs. From Q2 2027, a further 15% is reserved for regulatory change: 2.4, the 2028 rule year and F532 (B22 domain note). | |

---

## 2. Capacity and effort

### 2.1 Developer capacity (unassisted-equivalent dev-months)

| Period | Devs | Raw | Effective (−30%) | ×1.3 | ×1.8 (base) | ×2.5 |
|---|---|---|---|---|---|---|
| Nov–Dec 2026 | 2 | 4 | 2.8 | 3.6 | 5.0 | 7.0 |
| Q1 2027 | 2 | 6 | 4.2 | 5.5 | 7.6 | 10.5 |
| Q2 2027 | 2 | 6 | 4.2 → 3.6 after 15% reg. reserve | 4.6 | 6.4 | 8.9 |
| Q3 2027 | 2 | 6 | 3.6 | 4.6 | 6.4 | 8.9 |
| **Cumulative to 30.9.2027, 2 devs** | | **22** | | **18** | **25** | **35** |
| Q4 2027 | 2 | 6 | 3.6 | 4.6 | 6.4 | 8.9 |
| **Cumulative to 31.12.2027, 2 devs** | | **28** | | **23** | **32** | **44** |
| *Variant: +2 devs from 1.4.2027* (signed by 18.12.2026, `PLAN.md` D12 and gate HIRE; this paper first said 29.1.2027. 3 months' notice per R3 §2.1, 1 dev-month onboarding each) | 4 | Q2: 10, Q3: 12, Q4: 12 | Q2: 7.0→6.0, Q3/Q4: 8.4→7.1 | | | |
| **Cumulative to 30.9.2027, +2 devs** | | **34** | | **~26** | **~36** | **~50** |
| **Cumulative to 31.12.2027, +2 devs** | | **46** | | **~35** | **~49** | **~68** |

Rule of thumb: **each full-time developer gives about 3.2–3.8 unassisted dev-months per quarter in the base case**, after overhead and the regulatory reserve.

### 2.2 Payroll-domain hours

| Need | Hours (estimate) | Window |
|---|---|---|
| M0: pay-type catalogue for own company, 30 golden cases (first estimated here at ~40), a-melding mapping check, 2 shadow diffs, 2027 rule pack check, manual tax cards with four eyes, go-live sign-off | **100–200** | Nov 2026–Jan 2027 (Sjur: ~200–250 available, so it fits) |
| Own payroll in production, 2027 (monthly checks, June, December, annual statement) | 80–120 | 2027 |
| M1 for 3–5 direct customers and 1–2 accounting firms (byrå): R3's 2,400 h [§2.3] scaled down. ~200 golden cases (400), rule packs 2027/2028 and trekkrutine (200), review of results (300), catalogue (100), migration of ~6–8 entities at ~40 h (280), 2 parallel periods (110), help texts and support (150), 2.4 spec (120) | **1,400–2,000** | Nov 2026–Dec 2027 |
| **Sjur's supply in 2027** | **~700–1,000** | |
| **Gap** | **~500–1,200 h** | Covered by a payroll specialist at 0.5–1 FTE from Q2 2027 plus bought external fasit (signed golden-case answers): 150–250 h in B27; `PLAN.md` D4 contracts an external expert from November 2026 for 20–30 h in M0 and 100–150 h before M1 |

**`PLAN.md` uses narrower figures:** about 200 h for M0 and about 1,000–1,200 h for M1 (+120 h for 2.4), of which 350–450 h can be bought (`PLAN.md` §1.1, §6.4). The M1 row above is wider because it still included 1–2 byrå and ~200 golden cases. In `PLAN.md`, firm clients are M2, and M1 has about 150 golden cases in a coverage matrix, 20 % countersigned externally (§5).

B28 (payroll veto on releases) needs a named deputy. With Sjur as the only payroll person, releases stop whenever he is away. This paper recommended naming an external deputy before M1. **Decided in `PLAN.md` (D4):** contract the external payroll expert now, from November 2026; the expert is also the B28 deputy.

### 2.3 Effort estimates

**M0 – first payroll (own company)**, unassisted dev-weeks. The right-hand column is what `PLAN.md` §1.3 adopted after the M0 cuts.

| Block | Dev-weeks (this paper) | `PLAN.md` §1.3 (after the M0 cuts) |
|---|---|---|
| Rust workspace, CI, Postgres, migrations, deploy in Norway, secrets | 2–3 | Foundations 2–3, also covering `tenant_id` on every row, the append-only audit log and the operation catalogue (E8) |
| Internal login and roles, basic audit log, field encryption of national ID number (fødselsnummer) and bank account number | 2–3 | Login and roles 0.5–1: managed OIDC login (e.g. Entra ID) with MFA and a CLI device flow, re-authentication through the identity provider on approval and bank-account change, two roles as code, no BankID. The audit log sits in Foundations and field encryption in master data |
| Entity and sub-unit with AGA zone, person, employment (a-melding fields), 26 standard pay types with flags including withholding method, tax card (manual), bank accounts. API CRUD | 3–4 | Master data, pay types and tax cards 3–4. Only the 8–12 signed pay types are seeded (D7). Employment and leave IDs kept from the current system |
| Engine: clean-room Rust port of the trekkrutine (Skatteetaten's withholding routine) with 100% match against the published 2026 and 2027 table files (N13), prosenttrekk, frikort (tax-free card), **halvt trekk**, AGA by zone, holiday-pay accrual 10.2/12% (+60+), YTD accumulators, one hourly line, AGA on OTP premium (if relevant) | 4–6 | Engine 4–6, with union dues reducing the withholding base (§ 5-9-1, rounded up). The 60+ supplement moves to the M0+ track (gate JUN27) |
| Run lifecycle: draft, calculate, approve with hash, immutable runs, correction as a new run | 2–3 | 2–3, with an attestation summary before approval and a status per output after it |
| Payslip PDF (showing YTD holiday-pay base, D-31), pain.001 (bank payment file) for net pay, accounting voucher CSV | 3–5 | Outputs 3–4, adding the payroll journal (PDF and CSV) and one run export (CSV). Forskuddstrekk is its own payment order with the KID from the a-melding feedback |
| Format-neutral a-melding aggregate, serialised to the **JSON** the API takes, for manual upload of 2027 periods (N14 [verify]; asked in the letter to Skatteetaten), schema validation | 3–5 | 3–5: JSON per Skatteetaten's Q&A of 18.06.2026 **[verify by 27.11]**. An XML 2.3 serialiser of the same aggregate is a costed fallback (+1–2 weeks) |
| YTD/opening-balance import and comparison harness against the old system (øre diff report) | 2–3 | Shadow and cutover tooling 2–3, including ongoing leave and permittering with their old leave IDs |
| `brutto` CLI over the public REST API (OpenAPI); no web UI in M0. Optional MCP over stdio in the CLI, test data only | 2–4 | Interface 1–2: the CLI only. **No MCP in M0** while real payroll data is in the system |
| **Total** | **23–36 dev-weeks ≈ 6–9 dev-months** (central ~7) | **≈ 20–31 dev-weeks ≈ 5–8 dev-months** |

With two developers at base productivity (~7.6 per quarter), **M0 is feature-complete around late January 2027**. The calculation core alone, which is enough for the shadow runs, should be done by mid-December 2026. `PLAN.md` §1.2 is tighter: the shadow core (engine, master data, run lifecycle, a-melding JSON and the diff harness) is 17–26 dev-weeks against about 17 available from 2.11 to 18.12, so it needs coding from Monday 2.11 and the low end of every estimate.

**M1 – MVP for first pilots** (includes M0), unassisted dev-months. The right-hand column is the slim M1 that `PLAN.md` §6.2 adopted.

| Block | Full M1 (this paper) | Slim M1 (`PLAN.md` §6.2) |
|---|---|---|
| Foundations and security: tenant isolation with RLS (row-level security), encryption, audit log, roles, BankID via broker with step-up, backup in Norway, monitoring | 5–7 | 5–6, plus a read log for sensitive fields, backups in two Norwegian locations, break-glass access and the pentest |
| Master data: entity, sub-units and zones, person, employment with history, pay types with local copies, flat departments and projects | 4–5 | 3–4 |
| Calculation: full withholding (table, percentage, frikort, 50% without tax card, half withholding, June), AGA zones and fribeløp (tax-free allowance), holiday pay including ferietrekk (holiday-pay deduction) and payout on termination, OTP with AGA on premium, union dues, deductions by agreement, manual utleggstrekk (enforced deduction) with KID (payment reference), sick-leave basics (employer-period counter, sick-pay advance, refund report or light ledger), leave and layoff in the a-melding, pro-rata pay, termination settlement, explanation trace | 10–13 | 9–10, absence legal core included: the NAV refund receivable entered by hand, one AGA method ("deduct when received"), and a list of sick cases near the 3-month refund deadline. K27 import is LATER. Fribeløp zones are out of the M1 profile |
| Run lifecycle and controls: calendar, cut-off, controls against last month, BankID approval with hash, extra and correction runs, light post-approval tracks (B43) | 3–4 | 3–3.5 |
| CSV/Excel import with mapping and idempotency | 1.5–2 | Input 1–1.5 |
| Authorities: Maskinporten, standard system user, a-melding via REST with feedback (A03) and replacement, F532 strategy, tax-card API (polling), A07 fetch and reconciliation (A07 = Skatteetaten's a-melding reconciliation report), manual-upload export as fallback | 6–8 | 6–7 |
| Outputs: payslip delivery, pain.001 with KID and withholding as a separate payment, one accounting adapter plus CSV, standard reports | 3–4 | 2–2.5: payslips and the annual statement through Digipost (bought) with print fallback and manual delivery; the voucher file always, one adapter only if a pilot pulls it at G4 |
| Migration and parallel run: YTD and holiday-pay base, keeping employment IDs, A07 diff 0, parallel diff report | 3–4 | 3–3.5, keeping leave IDs too |
| Byrå basics: client list and status, tenant switch, agent system user, bulk tax-card fetch | 2–3 | – (M2, B45) |
| API-first public API, admin UI good enough for pilot payroll staff, thin MCP | 4–6 | 3: admin web UI as a client of the public API; remote MCP with read and draft tools, where actions with legal effect are human-only |
| Ops: pentest fixes, runbooks, on-call, DPA (data processing agreement) and DPIA (data protection impact assessment) support | 1–2 | Ops and support 1 |
| **M1 total** | **≈ 43–58 (central ~50)** | **≈ 36–42** |
| Separate, regulatory: a-melding 2.4 (spec 1.5.2027, test 15.9.2027) | 2–4 | +2–4 (F-MYN-20, now an M1 item on the M0+ track) |
| For comparison, **B42 as written** (~305 functions, Matrix-level, full MCP parity, phase-1 reconciliation, controls and graphs) | **≈ 65–95** | – (B42 dropped) |

This paper's slim-M1 sketch moved byrå clients to M2, used a slim payslip channel (PDF by e-mail or Digipost), a minimal admin UI and MCP read and draft only. `PLAN.md` §6.2 lands on the same 36–42 and chooses Digipost (F-POR-12, M1) with print or manual fallback; the employee portal and login are LATER (F-POR-01, -27, -28).

### 2.4 What this means

| Scope | 2 devs, base ×1.8 | +2 devs from 1.4.2027, base | Comment |
|---|---|---|---|
| M0 (~7 here; 5–8 in `PLAN.md` §1.3) | late Jan 2027 | same | The calculation core for the shadow runs comes by mid-Dec 2026 |
| Slim M1 (~39) | **~Q2 2028** | **~Sep–Oct 2027** | +2 devs makes 2028-01 pilots about a 50/50 bet at base productivity (it needs a multiplier ≥ ~2 or the low end of slim M1). 2 devs points to 1.8.2028. `PLAN.md` §6.4: M1-FC about 31.3.2028 and pilots live 1.8.2028 (plan); M1-FC about 1.9.2027 and pilots 2028-01 with hires (stretch, under 50 %) |
| Full M1 (~50) | ~Q3 2028 | ~Dec 2027 (too late for Oct–Nov parallel runs) | Full M1 for 2028-01 only works if the ×2.5 multiplier holds |
| B42 (~80) | mid-2029 | ~Q2–Q3 2028 | Not an MVP for this team |

**Calibrate on M0.** Track M0 in dev-weeks against the table in §2.3. At the 29.1.2027 gate (G2), compute the observed multiplier and re-forecast M1. This paper let that number decide the hiring. **`PLAN.md` cannot wait for it:** two developers must sign by 18.12.2026 to start by 1.4.2027 (D12, gate HIRE). G2 writes the measured gain and the runway at actual burn into the gate ADR, and M1 dates then move by rule, not by drift.

---

## 3. Concrete answers

### 3.1 What is realistic for the November 2026 payroll?

| Option | Feasible? | Assessment |
|---|---|---|
| **Live**: Brutto calculates, the bank pays from Brutto's pain.001, the a-melding is uploaded manually by 7.12.2026 | Technically possible: manual XML upload is a production fallback with no stated end date (N14, R3 §4.4). **Not advisable.** | About 3 weeks of build before payday, no parallel period (breaks B16), no golden-case coverage, tax tables untested at scale. 2026 would be split across two systems, so Brutto must produce the **2026 annual statement (sammenstillingsoppgave) with imported YTD by 31.1.2027** (D-27, D-36). December, the hardest month, would follow at once. F-MYN-14 (manual export) is still marked "Etter MVP" (after MVP) in the source data (M0 in `docs/plan/scope.csv`). My probability of being right to the øre with no fallback: under 20%. |
| **Shadow, calculation only** (gross, withholding, AGA base and amount by zone, holiday-pay base, net) after the old system has run November | **Yes, target 18.12.2026** (~65%) | No payday deadline. Real data stays in Brutto's own production environment, never in TT02 (the test environment), which allows only synthetic data. |
| **Shadow plus the a-melding**: the November a-melding generated from the aggregate, schema-validated and compared with the submitted message (field by field, via A07 or the old system's export) | **Likely by 18.12.2026, certainly by 15.1.2027** (~50% / ~80%) | The file is not submitted. |
| **Shadow plus pain.001 and voucher CSV** | By 15.1.2027 | A human can validate the pain.001 in the bank's upload check without signing. The voucher should balance and match the old system's postings per account. |

**Recommendation:** shadow November and December. The old system pays and submits both months. Never pay from Brutto's output during a shadow month.

**Decided in `PLAN.md` (D1, new B44):** the current system submits all of income year 2026. Brutto is system of record from period 2027-01 if both shadows are clean by 15.1.2027 (stretch), otherwise 2027-02 (planning date) or 2027-03.

### 3.2 December 2026 as first live month: **bad**

- Half withholding on ordinary table-based pay only, not on bonus, percentage cards or 12-month cards (D-05). A new and wrong flag halves the wrong lines.
- The calendar is compressed: early payday, Christmas bonuses and gifts (tax rules in N13), team holidays.
- The 2027 trekkrutine and tables arrive in early December (the 2026 version was merged 8.12.2025, N13). Tax cards for 2027 must be fetched in December, and from 15.12.2026 by polling only.
- Altinn II roles end 31.12.2026 (for the a-melding, one Skatteetaten page says 17.11.2026; see `docs/plan/ready-to-build.md` §0 item 6). The person who uploads must hold the Altinn 3 package A-ordningen for the company. `PLAN.md` §2.4 item 3: confirm this week that the current system can still submit 2026-11 and 2026-12 after 17.11.2026.
- The December a-melding is due 5.1.2027. Whether F532/F530 apply to submissions made after 1.1.2027 is unverified.
- AGA for November–December is due 15.1.2027. Forskuddstrekk is due no later than the first working day after each payout (`PLAN.md` §1.4 item 3).
- Going live in December splits 2026 across two systems, the same problem as November.

**December is ideal as shadow month #2** because it tests half withholding without risk.

### 3.3 January 2027 as first live month: **sensible, and the best option**

| Factor | Effect |
|---|---|
| New income year | No split year. The old system produces the 2026 annual statement, and YTD in Brutto starts at zero. The payslip's YTD holiday-pay base (D-31) also starts clean. |
| New tables and tax cards | Implemented once. The 2027 table file arrives about a month before the January payday, enough to reach a 100% match. Tax cards for ≤10 people are ordered by hand through Skatteetaten's tax-card file service (RF-1211 via ID-porten, which needs the Altinn package "Lønn") or copied from the current system, and entered with four eyes (`PLAN.md` §1.4 item 4). The API comes later (gate MP). |
| F532/F530 from 1.1.2027 | Built in from the first message. One strategy: one message per entity and month, replaced on every change (B11, D-16). |
| Altinn II ends 31.12.2026 | Brutto never depended on it. Manual upload uses personal Altinn 3 access; the uploader's A-ordningen package must be confirmed before the first live upload (period 2027-01, deadline 5.2.2027). In 2027 the manual channel takes **JSON** per Skatteetaten's Q&A of 18.06.2026 (N14) **[verify by 27.11]**, the same format as the REST API. That means one serializer. `PLAN.md` §1.3 costs an XML 2.3 serializer of the same aggregate as the fallback (+1–2 weeks). |
| Deadlines | The 2027-01 a-melding is due Friday 5.2.2027. Forskuddstrekk is due the first working day after payday, as its own payment order with the KID from the a-melding feedback, so the a-melding is uploaded on payday (`PLAN.md` §1.4 item 3). AGA for January–February is due 15.3.2027. |
| Holiday pay | The 2026 holiday-pay base sits in the old system. Import it per employee before 14.5.2027 and verify it to the øre (gate JUN27). |
| Risk | January is high season for byrås and for authority queues. That does not matter for own payroll. |

If the 15.1.2027 gate fails, shadow January and go live in **February** (YTD import of one month), or shadow February and go live in **March**. `PLAN.md` §1.2 adds: if shadow #1 slips past 31.12.2026, go-live moves to period 2027-02 automatically. **Do not go live in May or June**, and none from mid-November to December.

### 3.4 Maskinporten and external pilots

- **Onboarding:** N06 estimates **7–10 weeks from a ready org number** to the first production call. The same scope (`skatteetaten:innrapporteringamelding`) covers A07, a-melding submission and feedback. Apply for the tax-card scope on the same form.
  - There are no published processing times, and November–December queues are probably long because of the Altinn II shutdown (N06 §5).
  - The overview's 3–5 months is the pessimistic case; `PLAN.md` §2.3 plans on about 3 months.
  - **The vendor company (M02) is not chosen.** Nothing can start until it is, and changing it later forces every customer to re-approve the system user (N06 §9). `PLAN.md` D3 puts it in this week's decisions.
  - Targets: **production system user and first A07 fetch for own company by 31.3.2027, 29.1.2027 in the best case** (`PLAN.md` gate MP). First a-melding via API for period 2027-02 (due 5.3.2027) or 2027-03 (due 5.4.2027). Until then, M0 uses manual upload, which **is why F-MYN-14 must move into M0**.
- **Maskinporten does not set the pilot date. The size of M1 and the domain capacity do.** One authority constraint matters: the **trekkpålegg** (deduction-order) API requires Brutto to already submit in production *and* the customer to have reported once through Brutto (N06, F-MYN-28). Pilots therefore start with a manual deduction-order register.
- **A-melding 2.4:** final content 1.4.2027, spec 1.5.2027, guidance 1.9.2027, test environment 15.9.2027, Skatteetaten's IT done 1.12.2027, mandatory from 2028-01, first deadline **7.2.2028** (N14). That leaves 3.5 months of test environment and no real-data test before production (D-19).
- **Should pilots go live on 2.3 in 2027 or wait for 2028? Wait.**
  - A pilot live in Q3–Q4 2027 would hit four risk events in its first months: a split 2027 year (Brutto makes the annual statement with imported YTD, D-27), December with half withholding, the 2028 rule year, and the 2.3 → 2.4 switch.
  - M1 cannot be ready before autumn 2027 with this team anyway.
  - The fastest path: run each pilot **in parallel in October and November 2027** (calculate in 2.3/2.4 aggregate form and compare with A07, never submit), add a **historic shadow of June 2027** and, where possible, a **December 2027 shadow** (domain gate M). Then go live with **period 2028-01 on 2.4**. **`PLAN.md` §6.4 keeps this as the stretch** (two developers signed by 18.12.2026, under 50 %). The plan date is **1.8.2028**, with M1 feature-complete about 31.3.2028 and the parallel runs in spring 2028.
  - **Brutto's own company is the only 2.3 production user in 2027.** It gets a year of real API, feedback and KID experience. It should submit the a-melding for the pilots' first period at least 5 working days before any pilot (gate P-L).
  - Customer go-live windows are 1.1, 1.3 and 1.8 (`PLAN.md` §3). **No external customer should face June 2028 as their first or second live month without a June simulation on migrated data by 2.5.2028** (gate JUN28, stretch case only).
- **Byrå sequencing:** byrås are busy from November to February (Altinn II shutdown, year-end). Recommended: the byrå's *own* payroll goes live with the direct pilots if gates pass, and byrå *clients* follow in M2 (new B45 in `PLAN.md`): **1.8.2028 if the pilots go live 2028-01, otherwise about 8.2029**, using YTD import. `PLAN.md` §8 states the consequence (no firm-client revenue before 2029 in the base case) and an option to cost: a firm runs a client as a direct-customer tenant in M1, the client approves a standard system user, and the firm's staff are users in that tenant.

### 3.5 Dangerous months in the plan

| Month | Own company | Pilots |
|---|---|---|
| December 2026 | Shadow only (half withholding) | – |
| June 2027 | **First live holiday-pay payout.** Gate JUN27, 14.5.2027: holiday-pay payout and ferietrekk built, historic shadow of June 2026 equal to the øre, 2026 holiday-pay base imported and equal per person, the whole payout reported as feriepenger with the June exemption (§ 5-7-1), and the 60+ supplement capped at 6 G using the G in force on 31.12.2026 (ferieloven § 10 (3)). Fallback: manual lines in Brutto signed by Sjur, never a second system (`PLAN.md` §3). This paper first assumed the G adjusted from 1.5.2027 and the old system as fallback. | Historic shadow of June 2027 during migration |
| December 2027 | First live December, a full rehearsal for pilots. Gate DEC27, 15.11.2027: half withholding correct, including the hourly-pay rule (two weeks exempt, § 5-7-2). 2028 rule pack and table file by 22.12.2027. On-call staffed 27.12.2027–14.1.2028 | Shadow if possible |
| January 2028 | First 2.4 message, submitted early. Brutto's own 2027 annual statement by 14.1.2028 (gate AS27; legal deadline 31.1.2028) | Go-live in the stretch case, deadline 7.2.2028 |
| June 2028 | Second June | **First June on migrated data in the stretch case, the most likely failure month (domain critic).** Gate JUN28, 2.5.2028 |

---

## 4. Conflicts between decisions

| # | Conflict | Recommendation |
|---|---|---|
| C1 | **B19 vs B42 vs B38.** "Whole system finished during November" and ~305 functions (≈65–95 dev-months) against a 3-person team with ≈1.5–3 dev-month-equivalents in November. | **Reword B19:** "Own payroll in Brutto. Shadow runs for November and December 2026 compared to the øre. Live from the first month after two consecutive matching shadow months, target period 2027-01, fallback February or March 2027. M0 scope only." Delete "whole system finished during November". `PLAN.md` §8 holds the wording that applies. |
| C2 | **B19 vs B16.** Going live in November means zero parallel periods; B16 requires two equal to the øre. | **B16 governs**, for Brutto's own payroll too (domain critic: "same gates as for customers"). |
| C3 | **B42 vs B22.** B42 grew scope after B22 (freeze, one in, one out) was proposed, and B22 is not yet in force. | **Drop B42** (`PLAN.md` §8; this review first proposed a downgrade): Matrix Lønn stays the long-term reference for breadth, not the MVP. **Activate B22 now:** freeze M0 on 13.11.2026 (G1). `PLAN.md` freezes the M1 lawful core on 1.2.2027 (G3) and the pilot-pulled items at G4 (31.3.2027), after the letters of intent. Measure changes in dev-weeks, not function counts. Sjur signs. Regulatory changes are exempt but come out of the 15% reserve. |
| C4 | **B41 vs B19/B38 capacity.** Full UI↔API↔MCP parity in CI, server-side OAuth (rmcp has client-side OAuth only, R6 §2), URL-elicitation BankID confirmation, an agent that sends the a-melding, all from day one. About 3–6 dev-months, and the customer-agent part is blocked by the open DPIA/DPA and J10. | **Keep the core, downgrade the rest.** Keep: API-first, and the UI is a client of the public OpenAPI. Parity comes from the operation catalogue and one `dispatch`, so the CI parity test is cut (`PLAN.md` §4, §8). This review proposed an optional MCP over stdio in the M0 CLI on test data, and agent-started actions confirmed by a human with BankID in M1. **`PLAN.md` §4 decides narrower:** no MCP at all in M0 while real payroll data is in the system. In M1, remote MCP has read tools, draft tools (pay inputs and run drafts) and two generic tools. Actions with legal effect (approve, submit, pay, change a bank account or a role) are human-only operations that agent tokens cannot call. Agent tokens are issued by a human; there is no OAuth server. MCP is off by default per tenant. The human-confirmation flow for agent-started actions (F-PLA-37) and agent submission for customers are LATER, after the DPIA. This review also suggested trying agent submission for our own company once the API is live; `PLAN.md` rules that out, since production payroll data never goes to AI tools (§5, §11). |
| C5 | **B37 vs M0 timing.** Phase 1 merged into the MVP brings A07 reconciliation, controls and graphs, which need Maskinporten (≥7–10 weeks) and would delay M0. | **Keep B37's "calculate payroll from the first release".** In M0, A07 is a manual download from Altinn used as truth for the shadow diff. A07 via API comes in M1 as migration and parallel-run truth (B16). Graphs and most controls are LATER. This review proposed keeping the AGA bridge (F-REG-30) as an M1 control; `docs/plan/scope.csv` puts F-REG-30 (A07 vs general ledger) in LATER, as part of the separate product line (new B46). |
| C6 | **B19 vs F-MYN-14.** B19's fallback is manual upload, but F-MYN-14 is marked after MVP. | **Move F-MYN-14 into M0** (done in `docs/plan/scope.csv`). It exports the JSON the API takes, for 2027 periods. `PLAN.md` §1.3: JSON per Skatteetaten's Q&A of 18.06.2026 [verify by 27.11, gate M0-α]; an XML 2.3 serialiser of the same aggregate is a costed fallback (+1–2 weeks). Brutto never needs XML for a 2026 period, since D1/B44 leaves 2026 with the current system. |
| C7 | **B19 vs F-TRK-07 (licence).** The licence was presented as a blocker. | **Not a blocker:** a clean-room Rust port of about 150 lines, verified 100% against Skatteetaten's published table file (N13). Keep asking for a licence (a human sends the request, `PLAN.md` §2.4 item 4). |
| C8 | **B19 ("customers into production as soon as the MVP is ready") vs B25 and B16.** Ad-hoc go-lives clash with the cohort limit, parallel runs and year-end switching. | **Reword:** customers go live only in dated windows (1.1, 1.3, 1.8) after a per-customer go/no-go. |
| C9 | **B25 cohort limit (12 customers, 1,500 recipients) vs a 3-person team.** The limit was sized for 14 FTE with 2 support staff. With Sjur as the only payroll person, payday support is the binding constraint. | **Keep, tighten for wave 1:** ≤5 direct customers (a byrå's own payroll counts as one), ≤~600 recipients (adopted in `PLAN.md` §6.4 and §8). No new starts in the first 2 months after go-live, in May–June, or from mid-November to January (except the 1.1 window). Byrå clients in M2. |
| C10 | **B26 dated gates vs B19.** B26's dates (31.3.2027, 1.6, 1.9, 1.12.2027, 5.2.2028) assume R3's 1.1.2028 plan with 5–7 developers. B19 replaced the first-production date, but B26 was not re-dated. | **Keep B26 and re-date it** to the milestones in §6 (now `PLAN.md` §3). `PLAN.md` adds the hiring gate HIRE (18.12.2026) and the June and December gates: JUN27 (14.5.2027), DEC27 (15.11.2027, with the 2028 rule pack by 22.12.2027), AS27 (14.1.2028) and JUN28 (2.5.2028). |
| C11 | **B23 capital vs the real team.** "24 months before first pilot", "60–70 MNOK" and "1.7–1.8 MNOK per month" assume a 14-FTE organisation [R3 §9]. They do not fit 3 people, and the plan now needs hires. | **Reword:** "Fund the actual plan: current team plus 2 developers and 1 payroll specialist from Q2 2027, until at least 6 months after pilot go-live. Raise the next round on own payroll through June and December 2027 plus pilots live in 2028." Recompute runway at actual burn; the figures are not in the repo. `PLAN.md` §8 adopts this, writes the runway at actual burn into the G2 ADR, and D12 needs a runway figure before 6.11. |
| C12 | **B28 payroll veto vs one payroll person.** There is no deputy, and the "two payroll specialists by 1.2.2027" requirement (R3) is unmet. | **Keep.** **Decided in `PLAN.md` (D4):** contract an external payroll expert now, from November 2026, for 20–30 h in M0 and 100–150 h before M1; the expert is the B28 deputy. This paper first put the external hours and the deputy before M1 only. A payroll specialist at 0.5–1 FTE from Q2 2027 (`PLAN.md` §6.4, §12). |
| C13 | **B39/B40 "designed now" vs capacity.** Customer-defined approval flows and open banking both pull Peter, who also owns infrastructure. | **Keep "design later".** M0/M1 use one or two approval levels and pain.001 with manual confirmation. Open banking is LATER. Only reserve the data-model hooks. |

---

## 5. Recommended wording (for `design.json`, if Sjur approves)

`PLAN.md` §8 holds the wording that applies. The drafts below are kept as the review's input.

- **B19 (reworded):** "Brutto runs the team's own payroll. November and December 2026 are shadow runs: Brutto calculates after the existing system has run, and the results are compared to the øre. Brutto goes live from the first month after two consecutive matching shadow months, target period 2027-01, fallback 2027-02 or 2027-03. The existing system stays as fallback for at least 12 months. Scope is M0." `PLAN.md` §8 words it as: system of record from period 2027-01 if both shadows are clean by 15.1.2027, otherwise 2027-02 or 2027-03, with manual upload until Maskinporten is live. It adds B44: the existing system submits all of income year 2026.
- **B42 (the review's draft; `PLAN.md` §8 drops B42 instead):** "Matrix Lønn is the long-term reference for breadth. The MVP for pilots is M1, sized for the actual team (slim M1 ≈ 36–42 dev-months). Function counts are not a scope measure."
- **B41 (narrowed; the review's draft):** "API-first from day one, with the UI as a client of the public API. MCP: read and draft in M1. Actions with legal effect are started via MCP and confirmed by a human with BankID. Agent submission for customers comes after DPIA/DPA." `PLAN.md` §8 narrows further: actions with legal effect are human-only operations, and agent-started actions and agent submission both come after the DPIA.
- **B22 (activated):** "M0 frozen 13.11.2026, M1 frozen 1.2.2027. Changes are one in, one out, measured in dev-weeks. 15% of capacity is reserved for regulatory change from Q2 2027." `PLAN.md` §8 freezes the M1 lawful core on 1.2.2027 and the pilot-pulled items at G4 (31.3.2027).
- **B25, B26, B23:** as C9–C11.

---

## 6. Milestone plan with go/no-go criteria

The gate ids, names and dates follow `PLAN.md` §3. The criteria keep this review's extra detail where it does not conflict.

| ID | Milestone | Date (target / latest) | Go/no-go criteria (all measurable) | If no-go |
|---|---|---|---|---|
| **G0** | Ready to build | 6.11.2026 | E1–E10 adopted on Monday 2.11 (`PLAN.md` §2.1). D1–D5 and D12 taken (§2.2), including the vendor company and orgnr (D3, M02) and the onboarding owner and deputy (M01). The 2026 export received and checked at line level: payslips, submitted a-meldinger, YTD, the 2025 and 2026 holiday-pay bases, employment and leave IDs, and the 2026 forskuddstrekk KIDs. Onboarding forms sent: Samarbeidsportalen information form (N06 A1), TT02 org-number read-in (B3), Skatteetaten scope form with **a-melding and tax card** (C3). Licence request for the trekkrutine sent by a human. | Every later date slips week for week |
| **G1** | M0 scope frozen (B22) | 13.11.2026 | M0 list signed by Sjur; D6–D11 taken. Everything else tagged M1, M2, LATER or CUT. | – |
| **M0-α** | Engine spike | 27.11.2026 | Rust trekkrutine **100% match against the 2026 table file**, all tables, periods and steps (about 1.06–1.09 million rows [verify]). The first 20 of the 30 M0 golden cases (`docs/plan/testing.md` §4.1) pass, signed by Sjur. Money type with rounding rules per `PLAN.md` §1.4 item 2. Upload format confirmed, or the XML 2.3 fallback started. | Shadow #1 moves to January |
| **M0-S1** | Shadow #1: November 2026 | 18.12.2026 / 31.12.2026 | Every employee: gross, withholding, AGA base and amount by zone, holiday-pay base and net **diff 0.00 kr**, or every diff explained and signed. November a-melding schema-valid and field-by-field equal to the submitted message on mapped fields. | Go-live moves to 2027-02 |
| **M0-S2** | Shadow #2: December 2026 (half withholding) | 15.1.2027 | As S1, plus half withholding correct per line type (D-05). pain.001 passes the bank's validation (human, no signing). Voucher CSV balances and matches the old system per account. | Go-live moves to 2027-02 or 2027-03 |
| **M0-L** | **M0 live (own payroll)** | Decision 15.1.2027 for period 2027-01 (stretch, ≈40 %); otherwise 2027-02 (planning date, ≈65 %) or 2027-03 | Exit criteria in `PLAN.md` §1.7: S1 and S2 clean; withholding port 100 % on the 2026 and 2027 table files; the 30 M0 golden cases signed and green (plus a union-dues case if dues go through payroll); a synthetic twin accepted in Skatteetaten's test upload, with the uploader's A-ordningen package confirmed before the 5.2.2027 deadline; pain.001 accepted by the bank's validation; the forskuddstrekk KID routine written and rehearsed; ongoing leave, sick cases and garnishments absent or imported and signed; system description signed; rollback runbook ready; the current system's records archived; Sjur's B28 sign-off. The 2027 rule pack and table file loaded and 2027 tax cards registered with four eyes (F-KJO-41). | Shadow one more month |
| **HIRE** | Hiring for the stretch date | 18.12.2026 | Two developers signed, starting by 1.4.2027, and funding confirmed (`PLAN.md` D12). | Pilot plan date stays 1.8.2028 |
| **G2** | Calibration | 29.1.2027 | Observed agent multiplier from M0 actuals (dev-weeks vs §2.3). M1 re-forecast. Runway at actual burn written in the gate ADR. A payroll specialist (0.5–1 FTE from Q2 2027) lined up. This review first made G2 the hiring gate; `PLAN.md` moves hiring to HIRE. | M1 dates move by rule, not by drift |
| **G3** | M1 lawful core frozen | 1.2.2027 | Core list in `PLAN.md` §6.2 signed. | – |
| **MP** | Maskinporten live (own company) | 31.3.2027 (best case 29.1.2027) | Production Maskinporten client and system registration. Standard system user approved for own company. First production A07 fetch. N22 test plan passed in TT02. Synthetic test a-meldinger with 0 rejections. Tax-card API working in production (polling). | Stay on manual upload; it is not on the critical path for own payroll |
| **M0-API** | Own a-melding via API (follows MP; not a separate gate in `PLAN.md`) | Period 2027-02 or 2027-03 (deadlines 5.3 / 5.4.2027) | 0 rejections. A03 feedback read. KID for withholding equals A03 (`kidForForskuddstrekk`). A07 diff 0 against Brutto's own message. | Manual upload continues |
| **G4** | Pilot commitments; pilot-pulled items frozen | 31.3.2027 | ≥3 direct customers (a byrå's own payroll can be one) with a signed letter of intent or pilot agreement, willing to share their a-melding history. DPA template ready. Pilot-pulled items (`PLAN.md` §6.1) chosen from their needs. | Pilot date slips. Recruit a second candidate pool. |
| **JUN27** | Own payroll: first June | Gate 14.5.2027; payout June 2027 | Holiday-pay payout and ferietrekk built. Historic shadow of June 2026 equal to the øre. 2026 holiday-pay base imported and equal per person. The whole payout reported as feriepenger, with the June exemption (§ 5-7-1). 60+ supplement for employees turning 60 in 2027, capped at 6 G using the G in force on 31.12.2026 (ferieloven § 10 (3)). A signed 60+ golden case. | Pay June holiday pay in Brutto as manual lines signed by Sjur, never in a second system |
| **24-S** | a-melding 2.4 mapped | Spec by 1.5.2027 → mapping 1.7.2027 | 2.4 types generated. The aggregate serializes to both 2.3 and 2.4. Semantic diff 0 on shared fields for all scenarios (B11, D-19). | Draw on the 15% regulatory reserve |
| **M1-FC** | M1 (slim) feature complete | 31.3.2028 (plan) / 1.9.2027 (stretch) | About 150 signed golden cases on a coverage matrix (pay form × absence × zone × June/Dec × deduction), 100% green, 20% countersigned externally (this review first proposed ≥200). A-melding 2.3 accepted in TT02 for ≥5 test companies with 0 rejections. Full month for two synthetic customers (AS ~100, organisation ~40) end to end in under 1 working day. BankID login. pain.001 accepted by ≥2 banks. The accounting adapter, if a pilot pulled it, posts balanced vouchers. Pentest: no high or critical findings. | Pilots move to the next window |
| **24-T** | 2.4 in test | 15.9.2027 → 1.12.2027 | Our own company and synthetic twins of every pilot accepted in the 2.4 test environment with 0 rejections. | Manual upload as fallback [verify that it supports 2.4] |
| **DEC27** | Own payroll: first live December | Gate 15.11.2027; 2028 rule pack by 22.12.2027 | Half withholding correct, including the hourly-pay rule (two weeks exempt, § 5-7-2), with a signed hourly-December golden case. 2028 rule pack and table file loaded within 5 working days of publication. On-call staffed 27.12.2027–14.1.2028. | – |
| **AS27** | Own annual statement 2027 | 14.1.2028 (legal deadline 31.1.2028) | Produced by Brutto for the whole year (F-MYN-36). YTD diff 0 against A07 for 2027. | Manual from A07 |
| **P-PAR** | Pilot parallel runs | Two periods before go-live (stretch: October and November 2027) | Per customer: two consecutive periods equal to the øre. YTD diff 0 against A07. Employment and leave IDs 100% kept. Holiday-pay base equal against the old system's list and the 2940 balance. Historic June shadow with no unexplained diffs. Signed acceptance protocol. | The customer moves to the next window |
| **P-GO** | Per-pilot go/no-go (this review; not a separate gate in `PLAN.md`) | About one month before each pilot's go-live (1.12.2027 in the stretch case) | P-PAR and 24-T passed. Old system kept for at least 3 months (contract). | Next go-live window |
| **P-L** | **Pilots live** | 1.8.2028 (plan) / period 2028-01 (stretch) | Brutto's own a-melding for the same period submitted ≥5 working days before the pilots. **All pilots submit with 0 rejections or "immediate" errors caused by Brutto** (in the stretch case, 2028-01 by 7.2.2028). | Affected customers move to the next window |
| **JUN28** | Pilots: first June | Gate 2.5.2028 (stretch case only) | June 2028 simulated for all pilots on migrated data. 10% of employees checked by hand by the payroll specialist with 0 unexplained diffs. | That pilot pays June holiday pay in its old system |
| **M2** | Accounting firms: byrå clients (called "wave 2" in the first draft) | 1.8.2028 if the pilots go live 2028-01, otherwise about 8.2029 (`PLAN.md` §9) | Trigger: M1 stable through the pilots' first June. Byrå's own payroll stable ≥3 months. Agent system user tested in TT02 and production for ≥3 clients. Each client passes P-PAR rules (one period plus historic June shadow is acceptable for green clients, per the domain critic). | Next window |

---

## 7. Top 10 schedule risks

| # | Risk | Likelihood | Impact | Early signal | Mitigation |
|---|---|---|---|---|---|
| 1 | **Scope creep**: B42 and full B41 parity stay in, or new founder requirements arrive, so M0 drifts into M1 | High | Critical | M0 not frozen by 13.11.2026. Work starts on non-M0 items before M0-L. | Activate B22 now. Weekly burn-up in dev-weeks. One in, one out, signed. M1 cut order agreed now (`PLAN.md` §6.3). |
| 2 | **Only two developers.** One sick, departing or pulled into open banking or infrastructure loses ~50% of capacity. | Medium–high | Critical | No signed hires at HIRE (18.12.2026). Peter's time on B40. | Decide D12 now and sign two developers by 18.12.2026. Defer open banking. Pair on trekk, AGA and a-melding. Written runbooks. |
| 3 | **Payroll-domain bottleneck.** Sjur is the only fasit and is also CEO, sales and support. | High | Critical | <10 h/week domain work in November–December. Golden cases written by developers. | Protect 15–20 h/week. External payroll expert from November 2026 (`PLAN.md` D4: 20–30 h for M0, 100–150 h before M1), who is also the B28 deputy. Payroll specialist from Q2 2027. |
| 4 | **Authority onboarding delays**: no published SLAs, Altinn II shutdown queues in November and December, vendor company still unchosen, org number must be read into TT02. | Medium | Medium for own payroll (manual fallback); high for M1 | Applications not sent by 6.11.2026. No scopes by 15.1.2027. | Choose M02 this week (D3). Send all N06 forms in week 1. F-MYN-14 into M0. Log every application and reply date. |
| 5 | **Format and rule changes at the year boundary**: the 2027 manual-upload format (JSON per Skatteetaten's Q&A of 18.06.2026 [verify]), Altinn II roles stopping 17.11.2026, F532/F530 from 1.1.2027, null fields omitted in A07 since 12.10.2026. | Medium | High | Upload rejected in a shadow dry run. Unclear format guidance. Format not confirmed by 27.11. | JSON as primary serializer; a costed XML 2.3 fallback (+1–2 weeks) of the same aggregate, started at M0-α if the format is not confirmed. Check the Altinn packages this week. Nightly contract test in TT02 (N39). Ask Skatteetaten in writing. |
| 6 | **Withholding errors**: the Rust port is off by 1 kr (f64 order, N13), the 2027 tables arrive late, or bonuses get half withholding. | Medium | High | Under 100% match against the table file. Diff in S2. | 100% match on all ~1.06 million rows as a CI gate. Half-withholding flag per pay type (D-02, D-05). Load the 2027 file the day it is published. |
| 7 | **Missing reference data** from the old system (payslip detail, submitted messages, YTD, holiday-pay base, employment and leave IDs, KIDs), so øre equality cannot be proved. | Medium | High | Export incomplete or PDF-only by 6.11.2026. | Export everything now and check it is at line level (`PLAN.md` §2.4 item 2); budget extra shadow-tooling time if not. Download A07 manually from Altinn. Archive the old system's records before its licence ends; they are kept 5 years after each year-end (2026 records until 31.12.2031). |
| 8 | **A-melding 2.4 is late or changes**: spec 1.5.2027, test 15.9.2027, no real-data test before 2028-01. | Medium | High | Content not final on 1.4.2027. Test environment unstable. | Version-independent aggregate (B11). One generator for both formats (N39). Synthetic twins. Own company submits 2028-01 first. 15% reserve. |
| 9 | **Pilot commitment and timing**: no named pilots, byrås busy November–February, customers needed for the parallel runs. | Medium–high | High | No LOIs by 31.3.2027. Customers unwilling to share a-melding history. | Two tracks (direct and byrå). Flat-fee pilot. Go-live windows 1.1, 1.3 and 1.8. |
| 10 | **Dangerous months**: June (holiday pay on migrated base, 60+ and 6G, NAV days) and December (half withholding, new year, tax cards). | Medium | Critical (reputation) | Gates JUN27, DEC27, AS27 or JUN28 not green 4–6 weeks ahead. | Dated gates 14.5.2027, 15.11.2027 (2028 rule pack 22.12.2027), 14.1.2028 and 2.5.2028. Historic June shadows. No go-lives in May–June or mid-November to January. On-call rota. |

Just outside the top 10:
- Review bottleneck for agent-written code in money and authority paths (B38). Mitigation: property-based and mutation tests on trekk, AGA and holiday pay as CI gates.
- Wrong forskuddstrekk KID or late payment (`PLAN.md` risk 7). Mitigation: in M0 the KID comes from the a-melding feedback (upload on payday, then pay); Brutto computes its own KID only after it reproduces every 2026 KID [verify positions 18–19].
- Founder time pulled into fundraising (B23).
- API terms at Tripletex and PowerOffice may block the accounting adapter (N40). Mitigation: voucher file first; the adapter is pilot-pulled and comes after legal review.

---

## 8. One-paragraph summary for the plan

Brutto cannot go live for November 2026, but it can shadow November and December 2026 and go live with its own payroll in early 2027: `PLAN.md` plans on period 2027-02 (about 65 %), with 2027-01 as the stretch (about 40 %) and 2027-03 at the latest. After the M0 cuts, M0 is about 20–31 dev-weeks (this paper first estimated about 7 dev-months), and it should be used to measure real agent productivity. The A07, a-melding and tax-card APIs should be live for the team's own company by 31.3.2027 (29.1.2027 at best). Until then M0 uses manual upload and tax cards from Skatteetaten's file service. In the plan, external pilots go live 1.8.2028. The stretch is pilots live with period 2028-01 on a-melding 2.4, after parallel runs in October–November 2027. It holds only if M1 stays slim (≈36–42 dev-months) and two more developers sign by 18.12.2026, and even then it is under 50 %. `PLAN.md` §8 settles the decisions: drop B42 and B31; reword B19, B37, B41 and B23; activate B22; tighten B25; re-date B26; and add B44–B46.
