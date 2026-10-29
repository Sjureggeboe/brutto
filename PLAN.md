# Brutto – Plan v1: payroll first

**Date:** 29.10.2026 · **Owner:** Sjur · **Status:** proposal. Sjur signs the decisions in §8 before it is binding.

This plan replaces two earlier decisions: the MVP definition in B42 ("MVP at Matrix level") and the November go-live in B19.

**How the plan was made:**
- It reviews everything mapped so far: 676 functions, 189 entities, 43 decisions, about 300 open questions, the research reports and the night-work findings.
- Fifteen review agents each took one area or one cross-cutting question.
- Two more agents then reviewed this plan, one for payroll law and one for strategy and feasibility.
- Their working papers are in [`docs/plan/`](docs/plan/README.md). Where a working paper and this plan disagree, this plan wins. For a single function, [`docs/plan/scope.csv`](docs/plan/scope.csv) is the source of truth.

**Names used in this plan:**
- **M0 – First payroll:** what you called "phase 1". Brutto runs our own payroll.
- **M1 – MVP:** the first external customers.
- **M2 – Accounting firms.**
- **LATER:** on the roadmap, with a trigger.
- **CUT:** off the roadmap until a paying customer asks.

**Language:** everything in the project is now written in English. Norwegian legal terms stay where they are precise:
- a-melding (the monthly employer report);
- AGA (employer's social security contribution);
- forskuddstrekk (tax withholding);
- feriepenger (holiday pay);
- opplysningspliktig (reporting entity);
- virksomhet (sub-unit).

---

## Start here

**The next ten weeks:**
- Brutto calculates our own November and December 2026 payroll after the fact. We compare it with the current system to the øre.
- The current system keeps paying and submitting all of 2026.
- Brutto becomes our payroll system from period 2027-01 if both months are clean by 15.1.2027. That is a stretch, about 40 %. The planning date is 2027-02, about 65 %.

**Not now:**
- web UI, BankID, Maskinporten and authority APIs;
- sick pay, garnishments and accounting firms;
- dashboards, MCP and the A07-vs-ledger product.

**Monday 2.11, one hour, all three:**
- Adopt the engineering defaults E1–E10 (§2.1) as written.
- Name the tech lead.
- Sjur approves downloading Skatteetaten's withholding table file.
- Coding starts the same day, on work that needs no other decision.

**Weeks 1–4:**
- **Sander:** the withholding crate with the full table-file test, the rule pack and the engine. Gate on 27.11.
- **Peter:** workspace, CI, database, operation catalogue, master data and run lifecycle.
- **Sjur:** decisions D1–D12, the 2026 export, and the first 20 golden cases.

**Sjur this week.** Only these block code; the rest in §2.4 may slip a week.
1. Choose the M0 employer and the vendor company.
2. Export the current system's 2026 data, and check that it is at line level, not only PDFs.
3. Check which Altinn 3 packages the M0 employer's people hold ("A-ordningen" and "Lønn").
4. Settle the pay-type model.
5. Decide whether to recruit two developers now (D12).

**Dates:**
- 13.11: M0 frozen
- 27.11: engine spike
- 18.12: November shadow
- 15.1: December shadow, and go/no-go for 2027-01
- 29.1: calibration

**Rules:**
- Agents never touch golden cases, rate tables or expected values.
- A human reviews all code for money, access and authorities.
- New scope comes in only if something of the same size goes out, counted in developer-weeks.

**Read next:** §1 (M0), §2 (ready to build), §4 (architecture) and §5 (correctness).

---

## 0. The short version

**Why the plan changes**
- **The current plan cannot be delivered.**
  - B42 (MVP at Matrix level, about 305 functions) is about 65–95 developer-months.
  - B19 (own payroll live in November 2026, "the whole system finished in November") leaves about three weeks until payday, with no parallel period.
  - Two developers and coding agents deliver about 7 developer-months a quarter (estimate).
  - You decided B19, B37, B41 and B42 today. We propose to change them because of these numbers (§8).
- **Payroll is the product.** The breadth we mapped belongs to later phases: HR, an employee portal, our own absence and time modules, a partner platform, dashboards, A07-vs-ledger reconciliation and firm tooling.
- **Who we compete with.** In year 1 we are compared with NettLønn, PowerOffice Go, Tripletex and Finago at 35–49 kr per paid recipient, not with SD Worx. A customer buys correct payroll for its profile, not breadth.

**What we build, in order**

| Step | What it is | Date |
|---|---|---|
| Ready to build | Defaults adopted, Sjur's decisions, accounts and exports (§2) | Coding from 2.11. Decisions by 6.11. M0 frozen 13.11.2026 |
| **M0 – First payroll** | Our own payroll in Brutto: shadow runs for November and December 2026, then live (§1) | Live from 2027-01 (stretch) or 2027-02 (plan); 2027-03 at the latest |
| **M1 – MVP** | 3–5 direct customers with 20–150 employees run a normal month end to end (§6) | Pilots live 1.8.2028 (plan). Stretch: 2028-01, which needs two developers signed by 18.12.2026 and is still under 50 % |
| **M2 – Accounting firms** | Firms run payroll for many clients (§9) | 1.8.2028 if the pilots go live 2028-01, otherwise about 8.2029 |
| LATER | Modules, portal and app, tariffs, organisation life, open banking, platform, HR | Each with a trigger (§9) |

**What we cut** (details in §7 and [`scope.csv`](docs/plan/scope.csv))

| | Functions | Tables / entities | Fields |
|---|---|---|---|
| Mapped today | 676 (305 marked MVP) | 189 entities | 3,837 |
| M0 – First payroll | 119 | 25 tables | ≈ 360 |
| M1 – MVP (adds) | 152 | +12 tables | ≈ +175 |
| M2 – Accounting firms (adds) | 13 | +1 table | ≈ +10 |
| LATER | 294 | 67 entities deferred | – |
| CUT | 98 | 44 entities cut | – |

- **M0 + M1 is 271 functions, against 305 marked MVP before.** The count drops only a little, because the mapping splits the legal core of payroll into many small functions that the law requires.
- **The real cut is in depth.** Every function gets its simplest lawful version, and the data model shrinks from 3,837 fields to about 545.
- **M1 is also narrower than the old MVP.** Out go accounting firms, K27 import, travel-allowance calculation, dimension sync, the employee portal and agent-started actions.
- **From now on we measure scope in developer-weeks, not functions.**

---

## 1. M0 – First payroll

### 1.1 Goal and profile

**Goal:** Brutto calculates our own company's payroll correctly. We prove it against the current system to the øre for November and December 2026. Brutto then becomes system of record for income year 2027.

**Profile:**
- one legal entity with one sub-unit;
- at most 10 employees;
- fixed monthly salary, possibly one hourly employee;
- 8–12 standard pay types;
- table or percentage withholding;
- AGA in one zone, and holiday-pay accrual;
- OTP and union dues only if our company has them.

**Effort:**
- About 20–31 developer-weeks (5–8 developer-months; §1.3).
- About 200 payroll-domain hours, mostly Sjur's (about 18 hours a week until mid-January).
- 20–30 hours of external countersigning.

**The current system stays the oracle and the fallback.**
- It submits a-meldinger for 2026-11 (due 7.12.2026) and 2026-12 (due 5.1.2027).
- Confirm this week that its submission channel still works after Altinn II roles stop on 17.11.2026.

### 1.2 Build order

The shadow core must be ready by 18.12: engine, master data, run lifecycle, a-melding JSON and the diff harness. That is 17–26 developer-weeks of work, against about 17 available from 2.11. It needs coding from Monday and the low end of every estimate.

| Weeks | Sander | Peter | Sjur | Gate |
|---|---|---|---|---|
| 1 (2.–6.11) | Withholding crate: own port plus the full table-file test in CI | Workspace, CI, Postgres/sqlx, `tenant_id`, audit table, operation catalogue and `dispatch` skeleton, Azure subscription | D1–D5 and the D2 facts; 2026 export and format check; D6 | Mon: E1–E10 adopted |
| 2 (9.–13.11) | Rule pack as data (2026 AGA zones, holiday-pay rates, G). Engine for monthly pay: table and percent withholding, AGA, accrual. Golden-case runner | Master data (legal entity, sub-unit, person, employment, tax card) and the CLI skeleton | D7–D11; first 10 golden cases; sign the M0 freeze | G1, 13.11 |
| 3–4 (16.–27.11) | Half withholding, cap at cash pay, frikort, hourly line, union dues in the base; first 20 cases green | Run lifecycle (draft → calculate → approve with hash → immutable); import the real employees and their opening state | Remaining golden cases; download A07 from Altinn | M0-α, 27.11 |
| 5–7 (30.11–18.12) | a-melding aggregate and JSON for upload, about 10 hard checks; historic shadow of September and October 2026 | Diff harness against the current system; November import | Classify and sign the differences | S1, 18.12 |
| 8–11 (21.12–15.1) | 2027 rule pack and 2027 table file (published early December); half withholding checked on December | pain.001 for net pay, voucher file, payslip PDF, payroll journal, managed login | S2 protocol; 2027 tax cards with four eyes; system description | S2 and go/no-go, 15.1 |

If S1 slips past 31.12.2026, go-live moves to period 2027-02 automatically.

### 1.3 What M0 contains

Function ids are in [`scope.csv`](docs/plan/scope.csv) (tier `M0`). Each block is the simplest lawful version.

| Block | Contents | Dev-weeks (est.) |
|---|---|---|
| Foundations | Workspace, CI, Postgres, migrations, deploy in Norway, secrets, `tenant_id` on every row, append-only audit log, operation catalogue (E8) | 2–3 |
| Login and roles | Managed OIDC login (e.g. Entra ID) with MFA and a CLI device flow. Re-authentication through the identity provider on approval and on bank-account change. Two roles as code: payroll admin and approver. No BankID | 0.5–1 |
| Master data, pay types and tax cards | Legal entity and sub-unit with AGA zone (municipality → zone table per year). Person with national ID and bank account encrypted at field level. Employment with all fields the a-melding requires. Employment IDs and leave IDs kept from the current system. Effective-dated position periods. One flat department. Only the 8–12 signed pay types are seeded. Rule pack per year as data. Tax cards entered by hand with four eyes, with source and date (§1.4) | 3–4 |
| Engine | Pure function: inputs + rule pack + engine version → lines with an explanation trace. Pipeline in §1.5 | 4–6 |
| Run lifecycle | Draft → calculate (numbered versions) → approve (one named human who is not the preparer, hash of the result) → immutable. Corrections as new runs. Attestation summary before approval. After approval, payslip, payment file, voucher and a-melding each have their own status | 2–3 |
| Outputs | Payslip PDF with the content arbeidsmiljøloven § 14-15 (6) requires, including the year-to-date holiday-pay base, archived with hash in Norway for 5 years after the end of the accounting year. pain.001 with net pay as SALA (forskuddstrekk: §1.4). Voucher as CSV/JSON in our accounting system's import format. Payroll journal (lønnsjournal) as PDF and CSV. One run export (CSV). The attestation summary carries the totals: withholding per payout date, AGA per zone, holiday-pay accrual | 3–4 |
| a-melding | One format-neutral aggregate per opplysningspliktig and month, replaced on every change. Serialised for Skatteetaten's manual upload. Schema validation plus about 10 hard checks. Format: JSON, per Skatteetaten's Q&A of 18.06.2026 **[verify by 27.11]**. An XML 2.3 serialiser of the same aggregate is a costed fallback (+1–2 weeks) | 3–5 |
| Shadow and cutover tooling | Opening state import: employment IDs with all a-melding fields and change dates, ongoing leave and permittering with their leave IDs, fixed lines, pension setup. If go-live is after January, also year-to-date figures for the 2027 months run in the old system, checked against A07. Diff report per employee and field. Signed "equal to the øre" protocol | 2–3 |
| Interface | `brutto` CLI over the REST API. No web UI and no MCP | 1–2 |
| **Total** | | **≈ 20–31** |

### 1.4 Legal details M0 must get right

These came out of the legal review and are easy to get wrong.

1. **Union dues reduce the withholding base.**
   - Skattebetalingsforskriften § 5-9-1: the base is reduced by the deductible dues deducted in pay, rounded up to whole kroner.
   - The dues are then taken from net pay.
   - Research report C (#48, "after tax") is wrong on this.
2. **Rounding:**
   - base and amount for percentage withholding are rounded down (§§ 5-10-4, 5-5-4);
   - half and other derived table amounts are rounded down;
   - union dues in the base are rounded up;
   - AGA is computed exactly per virksomhet and zone, then rounded down once per opplysningspliktig and month (§ 10-4-4) [verify the F185 tolerance in test];
   - lines are kept to the øre, never with banker's rounding.
3. **Forskuddstrekk:**
   - It is due no later than the first working day after payout, as its own payment order to Skatteetaten, not marked SALA.
   - In M0 the KID comes from the a-melding feedback: upload on payday, then pay.
   - Brutto computes the KID itself only after it reproduces every KID the current system used in 2026 [verify KID positions 18–19].
   - AGA is due on the 15th every other month.
4. **Tax cards:**
   - Order them by hand through Skatteetaten's tax-card file service (RF-1211 format via ID-porten). This needs the Altinn package **Lønn**; "A-ordningen" does not cover tax cards.
   - Or copy them from the current system for as long as it keeps fetching.
   - Re-check before every run and for every new hire.
   - In January without a 2027 card: use the 2026 card and correct by the end of February (§§ 5-5-1, 5-5-2); otherwise 50 %.
5. **Holiday-pay base:**
   - The base is pay paid out in the earning year (ferieloven § 10 (1)), so the 2026 base closes on payout dates up to 31.12.2026.
   - December 2026 work paid in January 2027 belongs to the 2027 base.
6. **Leave:**
   - Ongoing leave or permittering at cutover continues in Brutto's first a-melding with the old leave ID.
   - Every active employment is reported, even without pay (F108).
   - A missing leave that was reported last month triggers F231 and a daily fine.
7. **Records of the current system:**
   - Payroll documentation is kept in Norway for 5 years after each year-end, so 2026 records until 31.12.2031. That covers the payroll journal, payslips, a-meldinger, vouchers and tax-card data.
   - Export and archive them before the old licence ends.
   - Then revoke the old vendor's Altinn system user.
8. **System description:** bokføringsforskriften § 5-6 requires a short description of the payroll system from the first live month.

### 1.5 Calculation pipeline

1. **Freeze the inputs** for the period: employments, pay agreements, fixed lines, variable lines, tax-card versions, rule pack.
2. **Gross lines:** monthly salary (a start or end mid-month as a manual adjustment line in M0; automatic pro rata in M1), hours × rate, one-off lines.
3. **Bases per line** from the pay-type flags: tax, AGA, holiday pay, pension.
4. **Withholding per payout date:**
   - Base = taxable lines − deductible union dues (rounded up, § 5-9-1, within the annual cap [verify the 2027 cap]).
   - Table via our own port, or percent.
   - Half in December on flagged lines.
   - 50 % without a card.
   - Capped at cash pay.
5. **Deductions from net pay:** union dues and agreed deductions.
6. **Net pay.** Negative net blocks approval.
7. **AGA** per sub-unit and zone, including AGA on the OTP premium in the month it is paid.
8. **Holiday-pay base and accrual,** with AGA on the accrual.
9. **Year to date**, computed from approved lines plus opening balances, and the explanation trace.
10. **Outputs after approval:** payslip, payment proposal, voucher and a-melding aggregate.

### 1.6 Our own payroll in 2027 (the M0+ track)

Once Brutto is live, our own payroll needs some M1 items before M1 is finished. They come first in the M1 queue. They sit inside the M1 estimate, except a-melding 2.4, which adds 2–4 developer-months.

| Item | Function ids | Due |
|---|---|---|
| Year switch 2026 → 2027: rule pack, table file, tax cards | F-KJO-41 (M0) | 15.1.2027 |
| Manual in-year tax-card changes and new hires | F-TRK-05 | From January 2027 |
| Maskinporten, a-melding API with feedback, tax-card API | MP gate | 31.3.2027 (best case 29.1) |
| Holiday-pay payout, ferietrekk, June rules, holiday-pay list, 2026 base imported | F-KJO-38, F-KJO-39, F-FRA-14, F-TRK-11, F-RAP-11, F-MIG-22 | 14.5.2027 (gate JUN27) |
| a-melding 2.4 serialiser from the same aggregate | F-MYN-20 | Mapping by 1.7.2027; accepted in test by 1.12.2027 |
| 2028 rule pack and table file | – | 22.12.2027 |
| 2027 sammenstillingsoppgave (annual statement to employees), including the holiday-pay base | F-MYN-36 | 14.1.2028 (legal deadline 31.1.2028) |

**When something happens to an employee:**
- **Leave or layoff:** report it in the a-melding with a stable leave ID from the first month.
- **Sickness:** for monthly staff, sick pay in the employer period changes nothing in the calculation. The NAV refund and the inntektsmelding are handled in NAV's portal.
- **Leaving:** termination settlement as manual lines, calculated and signed by Sjur.
- **A garnishment order (trekkpålegg) arrives:** deduct from the next payout, report utleggstrekk in the a-melding, and pay by the first working day after payout. 1–2 developer-weeks, triggered by the order.

### 1.7 Exit criteria (M0 live)

1. **Shadow months:** two in a row match the current system to the øre, with every remaining difference explained and signed. That covers:
   - payslip lines and withholding;
   - AGA base and amount;
   - holiday-pay base and net pay;
   - payment-file sum and a-melding content.
2. **Withholding port:** matches 100 % of the 2026 and 2027 table files.
3. **Golden cases:** all 30 M0 cases in [`testing.md`](docs/plan/testing.md) §4.1 are signed by Sjur and green in CI, plus a union-dues case if dues go through payroll.
4. **a-melding test upload:** a synthetic twin of the M0 a-melding (Tenor company, TestID) is accepted in Skatteetaten's test upload. Real data never goes to test.
5. **Payment file:** the bank's validation accepts the pain.001 file.
6. **KID:** the routine for the forskuddstrekk KID (§1.4) is written and rehearsed.
7. **Cutover:** ongoing leave, open sick cases and garnishment orders are either absent or imported and signed.
8. **System description:** signed.
9. **Rollback runbook:**
   - It says which system runs a month if Brutto fails.
   - It says how 2027 year-to-date and the holiday-pay base move between systems.
   - It says which system issues the 2027 annual statement.
   - Never run a 2027 period in a second system without importing it back.
10. **Old records:** the current system's records are archived (§1.4 item 7).
11. **Sign-off:** Sjur signs.

---

## 2. Ready to build: what must be in place, and by when

The full checklist, with owner, lead time and who to ask, is in [`ready-to-build.md`](docs/plan/ready-to-build.md).

### 2.1 Monday 2.11: engineering defaults (Peter and Sander)

Adopt each default unless someone objects in the Monday meeting. The full question set that replaces `fase1.json` is in [`questions.md`](docs/plan/questions.md) §2.

| # | Topic | Default |
|---|---|---|
| E1 | Who owns what | Sander: engine, withholding, AGA, holiday pay, a-melding aggregate, authority onboarding. Peter: hosting, security, login, payment file, voucher, payslip. Sjur: pay types, golden cases, shadow comparison. One named tech lead |
| E2 | Repo and CI | Cargo-workspace monorepo. CI runs fmt, clippy `-D warnings`, tests including golden cases, the sqlx offline check and cargo-deny. Short ADRs in the repo. CODEOWNERS on money, access and authority code |
| E3 | Base stack | Modular monolith, one binary. axum, REST, OpenAPI generated from code (utoipa) and committed. Postgres with sqlx. No job queue in M0 |
| E4 | Hosting | Azure Norway East: Postgres Flexible (General Purpose) and Key Vault. Backups in Norway. Restore tested before the first real run. No payroll data in telemetry outside Norway |
| E5 | Money and rounding | `rust_decimal` and `NUMERIC`. No ad-hoc `round()`; one named rounding function per legal rule (§1.4). `f64` only inside the isolated withholding crate, in the Java order of operations |
| E6 | History | Append-only versions with `valid_from` and `recorded_at` on data that drives calculation. Each calculation stores an immutable input snapshot plus input and result hashes. Corrections are new runs. No general "as known at" query layer |
| E7 | Tenants | `tenant_id` on every row from the first migration. Row-level security on before the first external customer. One policy module that every operation goes through |
| E8 | Operation catalogue | Every action is one named operation (stable id; read, write or human-only) behind one `dispatch`. Actor context on every call (person or agent, injected clock). Idempotency keys on writes. Stable error codes (problem+json). `/v1`. Money as decimal strings |
| E9 | Audit and personal data | Append-only audit log from the first migration; hash chain later, before ISAE. Field encryption with one key, and a blind index for national ID and bank account numbers. No personal data in application logs |
| E10 | Naming | English names in code, API and docs. Norwegian only for legal code values as Skatteetaten publishes them (`a_melding`, `a07`, `aga`) |

### 2.2 Sjur's decisions

| # | Decision | Recommendation | Needed before |
|---|---|---|---|
| D1 | Who submits November and December 2026? | **The current system.** Brutto shadow-runs both months and becomes system of record for income year 2027. This means no 2026 year-to-date import, no 2026 sammenstillingsoppgave from Brutto, and no two systems in one income year | 6.11 |
| D2 | Which legal entity is the M0 employer, and its facts | Current payroll system and its export formats; payday, bank and accounting system; holiday-pay rate (10.2 % or 12 %). OTP, employee pension contribution, union dues through payroll, employees aged 59 or over, ongoing leave or garnishments. Who holds the Altinn packages "A-ordningen" and "Lønn". Whether the vendor company differs from the employer: if so, check the regnskapsførerloven question and sign a DPA between them | 6.11 |
| D3 | Vendor company and orgnr (M02); onboarding owner (M01) | Decide now. The orgnr goes into Brutto's Altinn system ID, and changing it later means every customer approves again. Sander owns authority onboarding; Peter is deputy | 6.11 |
| D4 | Payroll authority (B28) | Sjur signs golden cases, rule packs, a-melding mapping and every release that changes calculation or reporting. Contract an external payroll expert now: 20–30 hours for M0 and 100–150 before M1; the expert is also B28 deputy | 6.11 |
| D5 | Scope freeze and working agreements (B22, B38) | M0 list frozen 13.11.2026. A human reads all code that touches money, access, authorities or crypto. Agents never edit golden cases, rate tables or expected values, and never touch production data | 6.11 |
| D6 | Minimal pay-type model (B5) | Number, name, a-melding code (description and benefit), withholding method (table, percent, none), half-withholding flag, flags for tax, AGA, holiday pay, sick pay and pension base, union-dues deductible flag, unit, debit and credit account. No customer formulas | Pay-type layer, 9.11 |
| D7 | The 8–12 pay types M0 uses | From Sjur's 26 standard types and his A07 mapping: fixed salary, hourly (if any), one-off addition, holiday pay, ferietrekk, deduction after tax. Also union dues and benefits, if our company has them. One signed golden case per type | 13.11 |
| D8 | Rounding rules | As in §1.4 item 2, confirmed in the letter to Skatteetaten | 13.11 |
| D9 | Standard posting | One aggregated voucher per run. Net pay as one line on 2930. AGA per zone and rate. Holiday-pay accrual and AGA on it every run. Settle the OTP account (S #29 in the founder's domain decisions) and the grouping of 5390 (S #28 says 5000, assumed) | Voucher file, about 14.12 |
| D10 | OTP (if our company has it) | The premium is entered by hand for the month it is paid. Brutto computes AGA on it and reports the pension provider in the a-melding. The premium itself is booked from the invoice | 13.11 |
| D11 | Separation of duties in a team of three | Everyone is in the same pay run, so someone approves their own pay. Allow a logged exception, reported to the board chair | 13.11 |
| D12 | Recruit two developers now? | Pilots in 2028-01 need two developers starting by 1.4.2027. With three months' notice they must sign by **18.12.2026**. Without them, the plan date for pilots is 1.8.2028. This needs a runway figure | 6.11 |

### 2.3 Long lead time: start now, needed for M1

- **Digdir, Altinn and Skatteetaten onboarding:**
  - Digdir consumer form and terms;
  - Altinn SBS terms and scopes;
  - Skatteetaten scopes `skatteetaten:innrapporteringamelding` and `skatteetaten:skattekorttilarbeidsgiver`;
  - ask Altinn to read our orgnr into TT02.

  Plan on about 3 months. The best case is 7–10 weeks from the orgnr [verify].
- **One letter to Skatteetaten:**
  - the trekkrutine licence (we don't wait for the answer);
  - rounding and the F185 tolerance;
  - half withholding on percentage cards;
  - June for part-year staff;
  - KID positions 18–19;
  - whether 24.12 and 31.12 are working days;
  - the manual-upload format for 2027 periods (JSON or XML);
  - the 2027 annual cap for union dues.
- **One legal review:**
  - pilot agreement: software-only role (B4) and liability cap;
  - DPA on the EU standard clauses, and a reference DPIA;
  - the regnskapsførerloven boundary;
  - Tripletex and PowerOffice API terms;
  - the copyright position of our withholding port.
- **Pilot recruitment:** 2 firms and 5–7 direct customers in the funnel, to end with 3–5 direct customers.

### 2.4 This week

1. Decide the M0 employer, the vendor company and the onboarding owner (D2, D3).
2. Export the current system's data:
   - payslips at line level and submitted a-meldinger;
   - year-to-date figures and the 2025 and 2026 holiday-pay bases;
   - employment and leave IDs, and the 2026 forskuddstrekk KIDs.
3. Check the Altinn 3 packages: "A-ordningen" for the a-melding and the A07 download, and "Lønn" for tax cards. Confirm that the current system can still submit 2026-11 and 2026-12 after 17.11.2026.
4. Approve downloading Skatteetaten's withholding table file (5.6 MB). Send the licence question, written by a human.
5. Decide on recruiting (D12). If yes, write the job ad. Sjur owns recruiting; Peter and Sander interview at most 4 hours a week each until 15.1.
6. Send the Digdir consumer form, the Altinn scope registration and the Skatteetaten scope form. E-mail the Altinn servicedesk to read our orgnr into TT02.
7. Ask the M0 employer's bank about pain.001 upload: version, salary agreement, SALA.
8. Contract the external payroll expert (D4).
9. Order the legal review and send the letter to Skatteetaten.
10. Set up the Azure Norway East subscription, and request access to Norway West for geo-backup.

---

## 3. Gates and dates

| ID | Milestone | Date (target / latest) | Go criteria (all measurable) | If no-go |
|---|---|---|---|---|
| **G0** | Ready to build | 6.11.2026 | E1–E10 adopted on 2.11. D1–D5 and D12 taken. 2026 export received and checked. Onboarding forms sent | Later dates slip week for week |
| **G1** | M0 scope frozen | 13.11.2026 | M0 list signed by Sjur; D6–D11 taken | – |
| **M0-α** | Engine spike | 27.11.2026 | Withholding port matches 100 % of the 2026 table file (about 1.06–1.09 million rows [verify]). The first 20 of the 30 M0 golden cases pass. Upload format confirmed, or the XML fallback started | Shadow #1 moves to January |
| **M0-S1** | Shadow #1: November 2026 | 18.12.2026 / 31.12.2026 | Per employee, these differ by 0.00 kr, or each difference is explained and signed: gross, withholding, AGA base and amount, holiday-pay base, net. The a-melding validates and matches the submitted message on mapped fields | Go-live moves to 2027-02 |
| **M0-S2** | Shadow #2: December 2026 (half withholding) | 15.1.2027 | As S1, plus half withholding correct per line. pain.001 passes the bank's validation (no signing). The voucher file balances and matches the current system per account | Go-live moves to 2027-02 or 2027-03 |
| **M0-L** | **M0 live** | Decision 15.1.2027 for period 2027-01; otherwise 2027-02 or 2027-03 | Exit criteria in §1.7 | Shadow one more month |
| **HIRE** | Hiring for the stretch date | 18.12.2026 | Two developers signed, starting by 1.4.2027, and funding confirmed | Pilot plan date stays 1.8.2028 |
| **G2** | Calibration | 29.1.2027 | Real agent gain measured from M0 actuals. M1 re-forecast. Runway at actual burn written in the gate ADR | M1 dates move by rule, not by drift |
| **G3** | M1 lawful core frozen | 1.2.2027 | Core list in §6.2 signed | – |
| **MP** | Maskinporten live (own company) | 31.3.2027 (best case 29.1) | Production client and system registration. Standard system user approved. First production A07 fetch. Synthetic test a-meldinger in TT02 with 0 rejections. Tax-card API works | Stay on manual upload |
| **G4** | Pilot commitments; pilot-pulled items frozen | 31.3.2027 | ≥ 3 direct customers with a signed letter of intent, willing to share their a-melding history. DPA template ready. Pilot-pulled items (§6.1) chosen from their needs | Pilot date slips |
| **JUN27** | Own payroll: first June | Gate 14.5.2027 | Holiday-pay payout and ferietrekk built. June 2026 historic shadow equal to the øre. 2026 holiday-pay base imported and equal per person. The whole payout reported as feriepenger, with the June exemption (§ 5-7-1). 60+ supplement for employees turning 60 in 2027, capped at 6 G using the G in force on 31.12.2026 (ferieloven § 10 (3)) | Pay June holiday pay in Brutto as manual lines signed by Sjur, never in a second system |
| **24-S** | a-melding 2.4 mapped | Spec by 1.5.2027 → mapping 1.7.2027 | The aggregate serialises to both a-melding versions, 2.3 and 2.4. Semantic diff 0 on shared fields | Draw on the 15 % regulatory reserve |
| **M1-FC** | M1 feature complete | 31.3.2028 (plan) / 1.9.2027 (stretch) | About 150 signed golden cases in a coverage matrix, 100 % green, 20 % countersigned externally. a-melding accepted in TT02 for ≥ 5 test companies. A full month for two synthetic customers end to end. BankID login. Pentest with no high or critical findings | Pilots move to the next window |
| **24-T** | 2.4 in test | 15.9.2027 → 1.12.2027 | Our own company and synthetic twins of every pilot accepted in the 2.4 test environment | Manual upload as fallback [verify that it supports 2.4] |
| **DEC27** | Own payroll: first live December | Gate 15.11.2027; 2028 rule pack by 22.12.2027 | Half withholding correct, including the hourly-pay rule (two weeks exempt, § 5-7-2). On-call staffed 27.12.2027–14.1.2028 | – |
| **AS27** | Own annual statement 2027 | 14.1.2028 (legal deadline 31.1.2028) | Produced by Brutto for the whole year. Year-to-date diff 0 against A07 | Manual from A07 |
| **P-PAR** | Pilot parallel runs | Two periods before go-live (stretch: October and November 2027) | Per customer: two consecutive periods equal to the øre. Year-to-date diff 0 against A07. Employment and leave IDs kept 100 % | The customer moves to the next window |
| **P-L** | **Pilots live** | 1.8.2028 (plan) / period 2028-01 (stretch) | Our own a-melding for the same period submitted at least 5 working days before the pilots. All pilots submit with 0 rejections caused by Brutto | Affected customers move to the next window |
| **JUN28** | Pilots: first June | Gate 2.5.2028 (stretch case only) | June simulated for every pilot on migrated data. 10 % of employees checked by hand | That pilot pays June in its old system |

**Customer go-live windows** are 1.1, 1.3 and 1.8. There are no new starts in May–June, nor from mid-November to January, except the 1.1 window.

---

## 4. Architecture minimum

**Principles we keep.** These are the ten principles for the payroll core:
- determinism and reproducibility;
- versioned rules;
- history on data that drives calculation;
- immutable approved runs;
- idempotent side effects;
- an explanation trace per line;
- an audit trail;
- simulation with the same engine;
- tenant isolation.

What changes is how much of each we build now.

**Must be right from the first migration** (expensive to retrofit):
- the operation catalogue and `dispatch` (E8);
- `tenant_id` everywhere (E7);
- money and rounding (E5);
- history policy and the calculation snapshot (E6);
- the append-only audit log and field encryption (E9);
- the format-neutral a-melding aggregate;
- OpenAPI generated from code;
- employment and leave IDs kept from the previous system;
- year-to-date and holiday-pay totals computed per person and legal entity, not per employment.

**Data model.**

| | Tables |
|---|---|
| Platform (M0) | Tenant, User, Document, AuditEvent |
| Organisation (M0) | LegalEntity, LegalEntitySettings, SubUnit |
| People (M0) | Person, Employment, EmploymentTerms, EmployeeBankAccount, TaxCard |
| Pay setup (M0) | PayType, RulePackage, PayInput |
| Run (M0) | PayRun, PayLine, Payslip, OpeningBalance, Finding |
| Outputs (M0) | AMelding, PaymentBatch, PaymentLine, Voucher, VoucherLine |
| M1 adds 12 | RoleAssignment, PayRunApproval, RecurringItem, Garnishment, PensionScheme, Absence, MappingRule, ImportJob, AuthorityExchange, SystemUserConnection, DimensionValue, Integration |
| M2 adds 1 | ClientEngagement |

The run status stops at approved or discarded. After that, payslip, payment, voucher and a-melding each have their own status (B43). Details are in [`data-model.md`](docs/plan/data-model.md).

**API and MCP** (B41 narrowed):
- **M0:** REST with OpenAPI, the `brutto` CLI as the interface, personal tokens. No MCP while real payroll data is in the system.
- **M1:**
  - Remote MCP with read tools, draft tools (pay inputs and run drafts) and two generic tools.
  - Actions with legal effect are human-only operations in Brutto: approve, submit, pay, and change a bank account or a role. Agent tokens cannot call them.
  - National ID, bank account, protected address, health and union data never leave via MCP.
  - MCP is off by default per tenant.
- **LATER:**
  - agent-started actions with BankID confirmation;
  - agent submission for customers, after the DPIA and an MCP addendum to the DPA;
  - an OAuth server, webhooks, and a developer portal beyond the generated API reference.

See [`api-mcp.md`](docs/plan/api-mcp.md).

---

## 5. Correctness: how we know payroll is right

**Where errors come from.** Payroll errors come more from inputs and transitions than from table lookups: migrated balances, pay in arrears across a system switch, ongoing sick leave, manual garnishments and pay-type flags. June and December are the dangerous months.

**What our own shadow runs prove.** They test the plumbing on a handful of employees on fixed salary. The golden cases carry the breadth.

| Check | M0 | M1 |
|---|---|---|
| Golden cases | 30 signed by Sjur ([`testing.md`](docs/plan/testing.md) §4.1), as a gate in CI. Add a union-dues case (if used), a 60+ case before JUN27 and an hourly December case before DEC27. Cases with an open rule question may be signed as an agreed convention, with the current system as oracle | About 150 in a coverage matrix (pay form × absence × zone × June/December × deduction), 20 % countersigned externally |
| Withholding | 100 % match on all rows of the 2026 and 2027 table files, as a CI gate | The same, every year on the day the file is published |
| a-melding | Schema validation and hard checks. A synthetic twin accepted in Skatteetaten's test upload. Field-by-field comparison with the submitted message | TT02 end to end on Tenor twins of each pilot, 0 rejections |
| Parallel run | Historic shadow of September and October 2026, then November and December equal to the øre. Signed protocol, zero tolerance | Two periods per customer. Year-to-date diff 0 against A07. Holiday-pay base checked against the old system's list and the 2940 balance, since A07 does not carry it |
| Release | Recompute previous months in CI. Sjur signs changes to calculation or reporting | Release diff over stored run snapshots, signed by Sjur or the named deputy (B28) |
| Code | Property tests on withholding, AGA and holiday pay | Plus mutation testing (≥ 80 %) on the rule modules |

**Two hard rules:**
- Agents never change golden files, rule packs or a-melding mapping without the payroll authority's signature.
- Production data never goes to test or to AI tools.

---

## 6. M1 – MVP for direct customers

### 6.1 Customer profile

| In | Pilot-pulled (in only if a signed pilot needs it; chosen at G4) | Out until a later phase |
|---|---|---|
| Organisations, foundations, associations and AS with 20–150 employees | Accounting adapter for Tripletex or PowerOffice Go (the voucher file always works) | Tariff ladders, pay settlements, KLP and SPK |
| One legal entity, few sub-units | Board fees and simple fees (recipient classes board/office and fee) | Shift and roster work, and supplements calculated from time systems |
| AGA for general industries in zones I, II, III, IV, IVa and V | Travel allowances as pre-split lines | Zone Ia and other fribeløp cases (sector-exempt enterprises, enterprises in difficulty), and groups sharing fribeløp |
| Monthly and hourly pay, standard pay types | Small fees in associations under the reporting thresholds [verify amounts and legal basis] | Posted workers, seafarers, Svalbard, ambulatory AGA |
| Contribution-based OTP | PAYE (kildeskatt på lønn) cards: percent path without June/December relief [verify] | Net-pay agreements, advances, employee loans |
| A firm's own payroll, as a direct customer | One flat department and project code to the voucher | Firm clients (M2), local branches with their own orgnr, lost-earnings cases |

### 6.2 What M1 adds to M0

| Block | Contents | Dev-months incl. M0 (est.) |
|---|---|---|
| Foundations and security | Row-level security on. Field encryption per tenant. Read log for sensitive fields. BankID via a broker for customer users, with step-up on approval. Backups in two Norwegian locations. Break-glass support access. Pentest | 5–6 |
| Master data | Several sub-units, roles per tenant, effective-dated history on everything that drives calculation, flat department and project | 3–4 |
| Calculation | Overtime and supplements; June rules; frikort above the limit; union dues and agreed deductions; garnishments in a manual register with KID; OTP with employee share; taxable insurance benefit; pro-rata pay; termination settlement with holiday pay and ferietrekk; holiday-pay payout; year-end | 9–10 |
| Absence (legal core only) | Absence register via CSV or manual entry. Employer period (arbeidsgiverperiode) with a simple suggestion. Sick pay in the employer period. NAV refund receivable entered by hand, with one AGA method ("deduct when received") and a list of sick cases near the 3-month refund deadline. Basis printout for the inntektsmelding in NAV's portal. Leave and permittering in the a-melding | incl. above |
| Run and control | Payroll calendar and cut-off. Controls against last month, and pay after end date. Preparer ≠ approver, with a logged exception for single-person payroll. Four eyes on bank-account changes. Extra and correction runs. Withholding per payout date and AGA per term as separate payment statuses | 3–3.5 |
| Input | CSV import with a mapping per source profile; an unknown code stops the line. Hours as day lines for hourly staff | 1–1.5 |
| Authorities | Maskinporten and a standard system user per customer (`a-ordning` + `lonn`). a-melding via the API with feedback and replacement messages. One message per opplysningspliktig and month, replaced on every change, so F532 (negative withholding sum per payout date, from 2027-01) cannot trigger. Tax-card API (polling). A07 on demand, as answer key for migration and parallel runs. Manual upload stays as fallback | 6–7 |
| Outputs | Payslips and the annual statement through Digipost (bought), with print fallback and manual delivery for employees without it. pain.001 with withholding and deductions as separate payments, returned payments, and our own KID after verification. Voucher file, plus one adapter if pilot-pulled and only after written OK on its API terms. Annual statement (sammenstillingsoppgave). System description per customer | 2–2.5 |
| Migration | Excel template for year-to-date figures, checked against A07 (diff 0). Holiday-pay base checked against the old system's list and the 2940 balance. Employment and leave IDs kept. Ongoing sick cases and leave. Two parallel periods per customer | 3–3.5 |
| API, UI and MCP | Admin web UI for pilot payroll staff, as a client of the public API. Remote MCP with read and draft tools, agent identity and agent limits. Generated API reference | 3 |
| Ops and support | Alerting, runbooks, on-call on paydays. A support process for payday: who answers while Sjur is the only payroll person. DPA, reference DPIA and security pack | 1 |
| **Total** | Slim M1, including M0 | **≈ 36–42**, plus 2–4 for a-melding 2.4 |

**Explicitly not in M1:**
- firm features (M2);
- our own absence and time modules, an employee portal or app, and manager flows;
- tariffs and automatic retro;
- open banking;
- Huma, Utleggsappen and OrgLab integrations;
- K27 import, a holiday-days ledger, travel-rate calculation, dimension sync and Brreg lookup;
- report builder and dashboards;
- A07-vs-ledger reconciliation;
- agent-started actions with legal effect;
- ISAE 3402 and ISO 27001.

### 6.3 Cut order if M1-FC is at risk

Agreed now, before the pressure arrives. First out first:
1. MCP draft tools. Read-only MCP stays.
2. The accounting adapter. The voucher file stays.
3. Dimensions beyond one department.
4. Travel allowances, which are then excluded from the pilot profile.
5. Board and fee recipient classes, unless an organisation pilot has signed.
6. Digipost, replaced by manual secure delivery.
7. Automated termination settlement, replaced by a checklist and manual lines.

**Never cut:**
- engine correctness;
- the a-melding API with feedback;
- A07 as answer key;
- migration checks;
- BankID approval;
- row-level security;
- the pentest.

### 6.4 Effort, staffing and date

- **Effort:** slim M1 is about 36–42 developer-months including M0, plus 2–4 for a-melding 2.4.
- **Payroll-domain work:** about 1,000–1,200 hours, plus 120 for 2.4. Of that, 350–450 hours can be bought.
- **Plan, current team** (two developers): M1 is feature-complete about 31.3.2028, the pilots run in parallel in spring 2028, and **the pilots go live 1.8.2028**.
- **Stretch:** two more developers start by 1.4.2027 (signed by 18.12.2026), and a payroll specialist at 0.5–1 FTE starts in Q2 2027. Then M1 is feature-complete about 1.9.2027, the pilots run in parallel in October–November 2027, and **the pilots go live 2028-01** on a-melding 2.4. Even then it is under 50 %.
- **Calibration:** at G2 (29.1.2027) we measure the real agent gain on M0 and re-forecast.
- **Wave 1:** at most 5 direct customers and about 600 recipients (B25 tightened).
- **Pricing:** pilots pay a flat fee. Test 39–49 kr per paid recipient in the pilot conversations.

### 6.5 Exit criteria (pilots live)

- Gates M1-FC, 24-T and P-PAR passed.
- Every pilot has run two parallel periods equal to the øre.
- Year-to-date diff 0 against A07, and employment and leave IDs kept 100 %.
- A signed acceptance protocol per customer.
- Our own a-melding for the same period submitted at least 5 working days before the pilots.

---

## 7. What we cut

The function-level detail is in [`scope.csv`](docs/plan/scope.csv): 676 rows, each with tier, simplest lawful version and reason. The per-area reviews are in [`docs/plan/areas/`](docs/plan/areas/).

### 7.1 Tiers by area

| Area | M0 | M1 | M2 | LATER | CUT | Marked MVP before |
|---|---|---|---|---|---|---|
| ORG Organisation | 7 | 4 | – | 16 | 2 | 16 |
| PER Persons and employment | 11 | 11 | – | 11 | 3 | 24 |
| LON Pay types | 7 | 3 | – | 11 | 10 | 11 |
| KJO Payroll run | 23 | 12 | – | 8 | 3 | 34 |
| TRK Tax and deductions | 10 | 12 | – | 4 | 2 | 22 |
| PEN Pension | 4 | 4 | – | 4 | 6 | 7 |
| FRA Holiday and absence | 0 | 16 | – | 24 | 3 | 17 |
| TID Time | 3 | 5 | – | 12 | 7 | 8 |
| UTL Expenses and travel | 0 | 7 | – | 16 | 2 | 15 |
| MYN Authorities | 7 | 18 | 2 | 13 | 2 | 26 |
| BET Payment | 10 | 4 | – | 5 | 3 | 11 |
| REG Accounting | 8 | 4 | – | 15 | 3 | 19 |
| POR Employee portal | 1 | 3 | – | 20 | 5 | 4 |
| LED Manager | 0 | 2 | – | 15 | 2 | 2 |
| BYR Accounting firms | 0 | 0 | 10 | 18 | 8 | 18 |
| ORL Organisation life | 0 | 2 | – | 26 | 5 | 2 |
| RAP Reports | 3 | 8 | – | 12 | 11 | 13 |
| PLA Platform | 3 | 10 | – | 22 | 2 | 13 |
| SIK Security | 11 | 11 | 1 | 12 | 1 | 20 |
| MIG Migration | 10 | 13 | – | 8 | 4 | 18 |
| HR, UTV, HEL, KOM | 1 | 3 | – | 22 | 14 | 5 |
| **Total** | **119** | **152** | **13** | **294** | **98** | **305** |

### 7.2 The big cuts, by theme

| Theme | What goes | Where it lands |
|---|---|---|
| Depth of the data model | 189 entities and 3,837 fields become 38 tables and about 545 fields. Bitemporal history everywhere becomes effective dating on calculation data plus a calculation snapshot. Merged: three mapping entities, four approval models, five finding queues, the four-level payment chain | The biggest single saving |
| Accounting firms | Templates with inheritance, mass reassignment, bulk operations, billing, licences, exit pack, AI input, AML signals, and the client model itself | M2 (13), LATER, 8 CUT |
| The old phase-1 product | A07-vs-ledger reconciliation, ledger reads, grouping codes, the A07 control catalogue, the reconciliation package | LATER, as its own product line |
| Absence, time and expenses | Holiday planning, holiday-days ledger, clock-in, rest periods, averaging, timesheet signing, supplements engine, travel-rate calculation, K27 import | Legal core only in M1; the rest LATER (B20, B32) |
| Pay settlement and tariffs | Pay-settlement module (F-LON-22–31), tariff agreements, pay tables and ladders, net-pay agreements, mass change, employee loans, advances, bankruptcy | LATER or CUT |
| Reports and analytics | Report engine and builder, dashboards, BI feed, budget, forecast, ESG, liquidity calendar | Fixed reports only. The rest is CUT or LATER; pay statistics stay LATER for the pay-mapping duty |
| Employee portal | Login, notifications, start page | Payslips through Digipost (bought) |
| Dimensions and Brreg | Dimension sync, dimension inheritance, cost reports, Brreg lookup and nightly sync | One flat code and manual entry; LATER |
| Partner platform | App registry, consent, source registry, webhooks, sandbox, certification, metering, unified API | LATER or CUT |
| Pension and insurance breadth | KLP, SPK, AFP, supplier files, insurance register and enrolment | Contribution-based OTP only |
| Organisation life | Congress mode, fixed fee runs, fast event payout, annual cycle, RF-1301 | Three recipient classes, pilot-pulled |
| HR extension | Competence, goals, talent, health search, HSE, org chart, equipment | LATER or CUT (B34) |
| Migration adapters | PowerOffice, Visma and SD Worx adapters, the Huma source switch, AI mapping | Excel template plus A07 check |
| API and MCP extras | CI parity test, the human-confirmation flow for agent actions, OAuth server with DCR, MCP Apps, SDKs beyond TypeScript, paid rate tiers | LATER or CUT |

### 7.3 Moved against the old MVP marking

**57 functions that were marked MVP are now outside M0 and M1:**
- 43 move to LATER, 13 move to M2 (accounting firms), and 1 is cut (the liquidity calendar).
- The largest groups:
  - firm features;
  - A07-vs-ledger;
  - travel-rate calculation;
  - dimension sync and Brreg;
  - the report engine and dashboards;
  - the setup wizard;
  - customer-made pay types;
  - the holiday-days ledger;
  - permittering counting;
  - auditor access;
  - the agent-confirmation flow.

**23 functions that were not marked MVP are needed earlier:**
- **M0:**
  - year switch (F-KJO-41);
  - manual tax card (F-TRK-05);
  - manual-upload export (F-MYN-14);
  - attestation summary (F-RAP-16);
  - system description (F-SIK-29);
  - migration cutover items (F-MIG-01, -03, -33, -35).
- **M1:**
  - annual statement (F-MYN-36);
  - inntektsmelding basis (F-FRA-23);
  - taxable insurance benefit (F-PEN-16);
  - contingency when an authority is down (F-MYN-41);
  - AGA per term (F-BET-03);
  - deductions to creditors (F-BET-05);
  - returned payments (F-BET-16);
  - staff without a digital mailbox (F-POR-04);
  - pay after end date (F-RAP-21);
  - agent identity and agent limits (F-PLA-32, F-SIK-31);
  - break-glass support (F-SIK-10);
  - security pack (F-SIK-32);
  - ongoing sick cases at migration (F-MIG-24).

**a-melding 2.4 (F-MYN-20)** was marked "after MVP". It is now an M1 item with a date, because our own payroll must submit period 2028-01 in 2.4.

### 7.4 Errors found in the mapping

1. **Union dues.** Research report C (#48) treats them as after tax, but skattebetalingsforskriften § 5-9-1 reduces the withholding base (§1.4). F-TRK-23 is fixed in `scope.csv`.
2. **F-MYN-14 (manual-upload export)** was marked "after MVP", but M0 depends on it.
3. **F-KJO-41 (year-end)** was deferred on the assumption that the first year-end is December 2028. With own payroll, the January 2027 go-live is itself the first year switch.
4. **F-TRK-26** puts the employee pension share in the after-tax deduction queue, but it is deducted before tax.
5. **Table numbering.** The 7100–7133 series ended with 2024. From 2025 the tables are 8000–8400 and 9010–9400, and the special tables 7150–7700 and 6300–6700 remain. Golden cases use these.
6. **Data model.** It had four separate approval models, five queues for findings, three overlapping mapping entities, and no tenant entity.
7. **Deferred entities still in use.** 24 entities deferred by the data-model review are referenced by MVP-marked functions. `scope.csv` resolves most of them. One M1 gap remains open in [`data-model.md`](docs/plan/data-model.md) §10: storing sick cases, with a proposed fix of five fields on Absence.
8. **Pricing.** The 69 kr per recipient in B17 is at Visma Payroll level and can't be defended on features in year 1.

---

## 8. Decisions to sign

You decided B19, B37, B41 and B42 today (29.10.2026). We propose to change them because of the capacity numbers in §0. Everything below is a proposal until Sjur signs. The full table for B1–B46 is in [`questions.md`](docs/plan/questions.md) §4.

| Decision | Change |
|---|---|
| **B19** Own payroll in November 2026 | **Reword:** "Brutto runs the team's own payroll. November and December 2026 are shadow runs, compared to the øre with the current system, which keeps submitting income year 2026. Brutto is system of record from period 2027-01 if both shadows are clean by 15.1.2027, otherwise 2027-02 or 2027-03. Manual upload until Maskinporten is live." Drop "the whole system finished in November". |
| **B42** MVP at Matrix level | **Drop.** Replaced by M0 and M1 in this plan. Matrix Lønn stays a long-term reference for breadth. |
| **B37** Straight to MVP, phase 1 merged | **Reword:** Brutto calculates payroll from the first release (kept). A07 is the answer key for migration and parallel runs. Graphs, broad controls and A07-vs-ledger are LATER. |
| **B41** API first, everything via MCP | **Narrow:** the API is the application layer, and the UI and MCP are thin clients. M1 has MCP with read and draft tools; actions with legal effect are human-only. Agent-started actions and agent submission come after the DPIA. The CI parity test is cut. |
| **B1, B3** Target and segments | **Reword:** the long-term target stays 10–1000 employees and firms. The path is: own company → 3–5 direct customers with 20–150 employees (§6.1) → firm clients (M2) → 150–300 employees → 300–1000. |
| **B22** Scope rule | **Activate now.** M0 frozen 13.11.2026. M1 lawful core frozen 1.2.2027, and pilot-pulled items at G4 (31.3.2027). One in, one out, in developer-weeks. 15 % regulatory reserve. |
| **B25** Cohort limit | **Tighten:** wave 1 is at most 5 direct customers and about 600 recipients. |
| **B26** Gates | **Re-date** to §3. |
| **B23** Capital | **Reword:** fund the actual plan through at least 6 months after the pilots go live. Recompute runway at actual burn and write it into the G2 ADR. |
| **B31** Map before building | **Drop.** Superseded: building starts. |
| **B13, B15, B17, B18, B20, B21, B24, B39, B40** | **Downgrade to after M1:** AI, certification, the pricing model, organisation life beyond three classes, our own modules, Huma, the guarantee, configurable approval, open banking. The principles stay; the work waits. |
| **B5, B6, B7, B10, B11, B14, B16, B32, B33, B34, B35, B43** | **Keep, with the narrowed wording** in `questions.md` §4:<br>- the minimal pay-type model;<br>- history only on calculation data;<br>- row-level security before the first external tenant;<br>- a manual authority path in M0;<br>- one a-melding aggregate;<br>- login with MFA in M0 and BankID in M1;<br>- the M0/M1 migration path;<br>- pre-split allowances;<br>- the manual NAV-refund path;<br>- payslips without a portal;<br>- flat dimensions;<br>- status per output. |
| **New B44** Sender of record for 2026 | The current system submits all of income year 2026 (D1). |
| **New B45** Accounting firms are M2 | A firm's own payroll can be an M1 pilot; firm clients wait for M2.<br>**Consequence:** no firm-client revenue before 2029 in the base case.<br>**Option to cost:** a firm runs a client as a direct-customer tenant in M1. The client approves a standard system user, and the firm's staff are users in that tenant. |
| **New B46** A07-vs-ledger is a separate product line | LATER, and only with written API clearance from the accounting vendors. |

---

## 9. M2 – Accounting firms, and the later roadmap

**M2 – Accounting firms:**
- **When:** 1.8.2028 if the pilots go live 2028-01, otherwise about August 2029. Trigger: M1 stable through the pilots' first June.
- **First:**
  - firm entity and clients;
  - firm roles per client;
  - a client list with status per client and month;
  - an agent system user with `regnskapsforer-lonn`, and client linking in the Altinn portal;
  - four-eyes quality control and recorded customer approval;
  - who presses pay.
- **Later in M2:** bulk tax-card fetch, templates, work queues, billing basis, exit package.

**LATER, with triggers:**

| Theme | Trigger |
|---|---|
| Tariff, pay ladders, pay settlement, automatic retro | First paying customer on a tariff agreement |
| Our own absence and time modules, employee portal and app, manager approval (B20, B39) | Five paying customers without an external alternative (B29) |
| Integrations: Utleggsappen, Huma, OrgLab, Tikket, a second accounting adapter | A signed customer needs it |
| K27 import, travel-rate calculation, dimension sync, Brreg lookup | Volume in the pilots |
| Organisation life beyond three recipient classes (B18) | Organisation segment after M1 |
| A07-vs-ledger reconciliation for firms | After M2, and only with written API clearance |
| Open banking (B40), direct bank API | Customer demand after M1 |
| Agent-started actions, agent submission, OAuth server, webhooks, developer portal, sandbox, SDKs | Partner or customer demand, and the DPIA done |
| KLP, SPK, AFP, insurance register | Tariff segment |
| Pay statistics by gender and position (pay-mapping duty) | The first pilot above 50 employees asks |
| Dashboards, report builder, analytics, AI assistant | After the pilots are stable |
| ISAE 3402 type 1, then type 2 and ISO 27001 (B15) | About 6 months after the first external customers |
| HR, competence, health follow-up, start page (B34) | After payroll is stable at scale |

---

## 10. Open questions

**Blocking M0, Sjur:**
- D1–D12 (§2.2);
- the vendor company;
- the Altinn packages, and the current system's submission channel after 17.11.2026;
- the letter to Skatteetaten, which carries the M0 questions: rounding, the upload format, half withholding, KID and the union-dues cap.

**Blocking M0, Peter and Sander:**
- E1–E10 (§2.1);
- which pain.001 version our bank requires;
- the manual-upload format (JSON or XML), by 27.11.

**Blocking M1:**
- the pilots and the payroll deputy;
- the legal review;
- confirming the default AGA method for NAV refunds ("deduct when received");
- which accounting system gets the adapter, if a pilot pulls it;
- how the pilots are migrated;
- the BankID broker;
- whether the runway covers support through the pilots' first June and December.

The 30 blocking questions with recommended answers are in [`questions.md`](docs/plan/questions.md), together with the 25 questions for Peter and Sander that replace `fase1.json`. Peter and Sander have not yet answered `fase1.json` in the artifact; they should answer the new set instead.

---

## 11. Top risks

| # | Risk | Mitigation |
|---|---|---|
| 1 | Scope creep: B42 breadth or full B41 parity creeps back | B22 active now. Weekly burn-up in developer-weeks. One in, one out. Cut order agreed (§6.3) |
| 2 | Only two developers; one is ill or pulled into infrastructure or open banking | Decide D12 now. Defer open banking. Pair on withholding, AGA and a-melding |
| 3 | Payroll-domain bottleneck: Sjur is the only answer key and also CEO, sales and support | Protect 15–20 hours a week. External expert from November. Payroll specialist from Q2 2027. Named deputy |
| 4 | The current system's export is PDF only, so the shadow diff can't be automated | Check the export format this week. Budget extra shadow-tooling time if needed |
| 5 | The upload format or Altinn access after 17.11.2026 is not as expected | Verify by 27.11. Costed XML fallback. Check the packages this week |
| 6 | Withholding off by 1 kr (`f64` order), late 2027 tables, wrong half withholding | 100 % table-file gate in CI. Half-withholding flag per pay type. Load the 2027 file the day it is published |
| 7 | Wrong forskuddstrekk KID, or late payment | KID from the feedback in M0. Our own KID only after it reproduces 2026 |
| 8 | a-melding 2.4 late or changed; no real-data test before 2028-01 | Version-independent aggregate. Synthetic twins. Own company submits 2028-01 first. 15 % reserve |
| 9 | No pilot commitments in time | Two funnels (direct and firm). Flat-fee pilot. Go-live windows 1.1, 1.3 and 1.8 |
| 10 | Dangerous months: June (holiday pay on a migrated base) and December (half withholding, new year) | Dated gates JUN27, DEC27, AS27 and JUN28. Historic June shadows. On-call rota |

**Also:**
- Agent-written code in money and authority paths needs review capacity, so property and mutation tests run as CI gates.
- The accounting vendors' API terms may block an adapter; the voucher file is always the fallback.
- Real payroll data must not reach AI models in M0.

---

## 12. Team, roles and cadence

| Who | Role |
|---|---|
| Sjur | Product owner, payroll authority (B28), owner of the scope list (B22), customer and authority contact, pilots, legal, recruiting |
| Sander | Engine, withholding, AGA, holiday pay, a-melding aggregate; owner of authority onboarding |
| Peter | Hosting, security, login, payment file, voucher, payslip; deputy for authority onboarding |
| External payroll expert (from November 2026) | Countersigns golden cases (20–30 hours for M0, 100–150 before M1), reviews M1 rules, B28 deputy |
| To hire (D12) | Two developers (signed by 18.12.2026 for the stretch date), and a payroll specialist at 0.5–1 FTE from Q2 2027 |

**Cadence:**
- **Weekly:** 30 minutes on the burn-up in developer-weeks and on blockers.
- **At each gate in §3:** go or no-go, written down as a short ADR.
- **Monthly:** Sjur reviews the scope list.

---

## Appendix A: What the review found

1. **Scope and team do not match.**
   - **Capacity:** about 3.2–3.8 developer-months per developer per quarter. That is after 30 % overhead, a 15 % reserve for regulatory change from Q2 2027, and an assumed ×1.8 gain from coding agents. All of these are estimates.
   - **With two developers:** about 25 developer-months by 30.9.2027.
   - **Effort:** M0 5–8 developer-months; slim M1 including M0 36–42; full M1 43–58; B42 as written 65–95.
   - **Payroll-domain work** is the second bottleneck: about 200 hours for M0 and about 1,000–1,200 for M1.
2. **The decisions contradict each other.**
   - B19 (live in November) breaks B16 (two parallel periods equal to the øre).
   - B42 grew the scope after B22 (scope freeze) was proposed, and B22 was never activated.
   - B41's full parity test, server-side OAuth and agent submission from day one cost 3–6 developer-months, before the privacy work is done.
   - B26 and B23 assume a company of 5–14 people.
3. **M0 needs no authority API.** The a-melding can be uploaded manually, tax cards can be ordered through Skatteetaten's file service, and the bank takes a pain.001 file. The M0 critical path is Sjur's payroll decisions, our own withholding port and the shadow comparison.
4. **The withholding licence does not block us.**
   - We write our own Rust port of the published rules, in `f64` with the Java order of operations.
   - We require a 100 % match against the published table file.
   - We still ask for the licence, but we don't wait for it.
5. **The old phase 1 (A07 against the general ledger) is a separate product line.** It needs read access to Tripletex and PowerOffice, whose API terms ban competing products and "dashboarding" (N40). It is not needed to run payroll.
6. **Accounting firms are a separate milestone.** The agent system user depends on Altinn/Digdir questions that need TT02 testing. Firm features are breadth, not payroll.
7. **Legal details** that the earlier material got wrong or left out are listed in §1.4 and §7.4.

## Appendix B: Files

| File | What it is |
|---|---|
| [`docs/plan/README.md`](docs/plan/README.md) | Index of the working papers |
| [`docs/plan/scope.csv`](docs/plan/scope.csv) | All 676 functions with tier (M0, M1, M2, LATER, CUT), simplest lawful version and reason |
| [`docs/plan/ready-to-build.md`](docs/plan/ready-to-build.md) | Full checklist: before code, before M0 live, before M1 |
| [`docs/plan/timeline.md`](docs/plan/timeline.md) | Capacity, effort estimates, milestone plan, conflicts between decisions |
| [`docs/plan/data-model.md`](docs/plan/data-model.md) | The core model, history policy, merges, deferred entities, ER diagram |
| [`docs/plan/testing.md`](docs/plan/testing.md) | Correctness strategy and golden-case lists |
| [`docs/plan/api-mcp.md`](docs/plan/api-mcp.md) | Minimal API and MCP scope, first operations and tools |
| [`docs/plan/questions.md`](docs/plan/questions.md) | Blocking questions, new questions for Peter and Sander, triage of all open items, B1–B46 |
| [`docs/plan/competitors.md`](docs/plan/competitors.md) | Table stakes against SD Worx breadth, cheap differentiators, pricing |
| [`docs/plan/areas/`](docs/plan/areas/) | One scope review per area group |

The Norwegian analysis in `analyse/` stays as background. This plan has not changed the data in `analyse/build/data` or the artifact. Updating them to the new tiers is a separate step, once Sjur has signed.
