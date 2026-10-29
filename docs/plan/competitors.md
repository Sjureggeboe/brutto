# Table stakes vs SD Worx-level breadth: what Brutto must have, and what it should skip

> **Status:** Working paper from the scope review of 29.10.2026. [PLAN.md](../../PLAN.md) is the main plan; where this paper and PLAN.md disagree, PLAN.md wins.
> **What it is for:** what the cheapest Norwegian payroll products force Brutto to have (table stakes), which SD Worx-level breadth to skip, which cheap differentiators to keep, and what the market's price level means for a narrow MVP.

Reviewer: competitor lens. Date: 29.10.2026.
Inputs: `analyse/research/A-marked-konkurrenter.md` (A), `analyse/research/R0-matrix-lonn.md` (R0), `analyse/research/R0-sdworx-meny.md`, `analyse/build/data/meny.json` (SD Worx mapping), `analyse/research/D-praksis.md` (D), `analyse/research/E-byra.md` (E), `analyse/research/R2-virksomhet.md` (R2V), `analyse/research/R3-kritikk-strategi.md` (R3), `analyse/build/data/design.json` (B-decisions), `analyse/build/data/omr-K*.json` (function ids), and public price and feature pages fetched on 29.10.2026.

Markers: **[V]** verified on a primary source (a vendor price page or a register). **[L]** the vendor's own marketing claim. **[T]** third-party source. **[A]** my assessment.

Tier labels follow PLAN.md: **M0** first payroll (own company), **M1** MVP for direct customers, **M2** accounting firms, **LATER**, **CUT**. The tiers in this paper are its recommendations; [`docs/plan/scope.csv`](scope.csv) holds the decided tier per function, and where the two differ, scope.csv wins.

---

## 0. Summary

1. **Customers judge Brutto against the cheapest dedicated payroll products, not against SD Worx.** For a buyer with 20–150 employees, the floor is set by NettLønn, PowerOffice Go, Finago Payday and Tripletex, which charge 35–49 kr per paid recipient [V]. Every one of them sends the a-melding (the monthly employer report to the tax authorities) directly, delivers payslips digitally, integrates with accounting, and handles absence, holiday pay and departments or projects. The buyer assumes all of this, so it earns no credit and missing any of it loses the deal.
2. **SD Worx's breadth is mostly HR, not payroll.** In the HR Specialist role, its menu has 15 top areas: competence, performance, salary review, health and back-to-work, team planning, announcements and others. The payroll run does not appear in that role at all (`R0-sdworx-meny.md`). SD Worx's real payroll edge is its tariff engine, its import templates and its BPO (payroll outsourcing) service. The pilot customer profile (B3, R3 §4.1) needs none of these in year 1.
3. **The floor is 38 table-stakes items** (§2), covering 203 function ids. Of these, 197 are already marked MVP. **Six are not. This paper recommended moving five of them in and merging the sixth. PLAN.md and scope.csv decided:**
   - **F-MYN-14**, the manual-upload fallback for the a-melding: **M0**. It is the only M0 submission route. It exports the JSON the API takes (per Skatteetaten's Q&A of 18.06.2026 [verify by 27.11.2026]); an XML 2.3 serialiser of the same aggregate is a costed fallback (PLAN.md §1.3).
   - **F-KJO-41**, the year-end rollover in payroll: **M0**. With our own payroll live from 2027, the January 2027 go-live is itself the first year switch: 2027 rule pack, table file and tax cards by 15.1.2027 (PLAN.md §1.6, §7.4 item 3). The first December in Brutto is December 2027 (gate DEC27).
   - **F-FRA-13**, the year-end job for holiday: **LATER**. Manual carry-over transactions the first time (scope.csv).
   - **F-REG-19**, the PowerOffice Go adapter: **LATER**. The one M1 accounting adapter (F-REG-18) is pilot-pulled: chosen at G4 (31.3.2027) from the pilots' ledgers, and built only after a written OK on its API terms (PLAN.md §6.1). The voucher file always works.
   - **F-FRA-23**, as a basis report only (the input to the inntektsmelding, the employer's sick-pay income report to NAV): **M1** in scope.csv (PLAN.md §7.3). Brutto prints the basis per sick case, and the inntektsmelding is entered in NAV's portal. No NAV API.
   - **F-MYN-36**, the annual statement: **M1** (PLAN.md §6.2). For our own payroll the first one is for 2027, by gate AS27 (14.1.2028). F-POR-16 is also M1 and publishes it; scope.csv keeps the two as separate rows.
4. **108 of the 305 MVP functions are not table stakes.** Of these, 22 are invisible engine enablers, 13 are the differentiators, and 14 are legal or security hygiene that must stay. **59 are SD Worx-style breadth or over-engineering and are candidates to defer or simplify** (Appendix A).
5. **Six cheap differentiators are worth keeping** (§4). Most cost 1–4 developer-weeks each **if they are built into the engine from day one**. The trace and the explained deviation list cost more, but nearly all of that is the trace itself:
   - an explanation trace per payslip line
   - approved runs that can never change, with a hash and corrections as new runs
   - A07 (the a-ordningen reconciliation report) used as the truth for checking and migration
   - an API-first design with an MCP for reading and drafts (PLAN.md §4: actions with legal effect are human-only operations that agents cannot call)
   - a deviation list that explains itself
   - separate status tracks after approval

   The expensive parts are full UI↔API↔MCP parity enforced in CI, agent-started actions with legal effect (F-PLA-37), and a generic "as-of" query layer. Postpone those.
6. **Pricing:** a narrow MVP competes at the NettLønn and PowerOffice price point (35–49 kr per paid recipient) and should not expect the 69 kr in B17 until it has tariff, retro and modules. Price removes an objection but does not win the switch. Trust, migration and minutes per payslip win it (A §6.2, E §5.3). PLAN.md §6.4: pilots pay a flat fee, and 39–49 kr per recipient for direct customers is tested in pilot conversations (estimate).

---

## 1. Where the floor is: what the cheapest competitors publicly claim

| Product | Price (ex. VAT), 29.10.2026 | Payroll features they advertise | Source |
|---|---|---|---|
| **NettLønn** (Adato/ECIT) | 39 kr per payslip, billed only for employees paid that month. NettLønn People (travel and expenses) 35 kr per active user. Accounting-firm price on request | 160 ready-made pay types, "always updated rates", employments synchronised via A07, Altinn integration, payslip in an app, absence registration, mass registration and update, department, project and dimension, pension data export, reports for reconciling against accounting, accountant access, multiple companies with settings copied between them (for accounting firms), integrations with "a range of" accounting systems | [V] nettlonn.com/priser-nettlonn, /funksjoner-i-nettlonn |
| **PowerOffice Go** (Visma) | 195 kr/month + 35 kr per paid recipient. Payroll can be bought standalone. Add-ons: time 100 + 50 per user, travel 100 + 50 per user, holiday and absence 35 per user | Payroll "with a few keystrokes", payslips in the mobile app | [V] poweroffice.no/no/priser |
| **Finago Payday** | 49 kr per payslip, 49 kr per sammenstillingsoppgave (the employee's annual summary), travel and expenses 29 kr per user. No minimum | Payroll runs, holiday and absence, multi-client, API integrations, phone and chat support 09–15 | [V] finago.no/priser |
| **Tripletex** (Visma) | Payroll is included in Pro (from 479 kr/month), Komplett and others with 1 user. "Lønn og reiseregning" 65 kr per extra user, time registration against payroll 39 kr per employee | Automatic a-melding creation and submission, company car, allowances and deductions, travel expenses in the app, hourly time, approval | [V] tripletex.no/priser |
| **Fiken** | 69 kr per user per month ("Lønn og ansatte") | Pay out salary, send the a-melding from Fiken | [V] fiken.no/priser |
| **Visma Payroll** | Start, Pluss and Smart, per active employee. The amounts are hidden ("Sjekk pris"). Third-party list prices: 57, 67 and 100 kr | Start: **no integrations**, the payroll officer registers holiday and absence. Pluss: integrations. Smart: adds time, expenses and app self-service | [V] for the packages (vismasoftware.no), [T] for the prices (hr.software, June 2026) |
| **Intect** (DK, Norwegian version since 2025) | 39 DKK per payslip (Scandinavian page, not confirmed for Norway) | Multi-company, employee app, open API, templates | [V] intect.io, A §3 |
| **Uni Micro (accounting-firm licence)** | Payroll 12 kr per active employee (0–49) and 9 kr (50+) as the firm's cost price. Recommended resale price 20 and 15 kr | Accounting-firm package | [V] via E §5.1 |
| **SD Worx** | Not published. Roughly 60 kr per payslip *including services*, derived from revenue | Flexible engine, tariffs, import templates, absence and NAV refunds, portals, BPO, ISAE report | A §1.2, §2.1 [A] |

**Reading [A].** Across the cheap tier, the floor is:
- direct a-melding submission
- tax cards (skattekort)
- holiday pay
- absence that affects pay
- digital payslips
- accounting integration with dimensions
- multi-client for accounting firms (M2 in PLAN.md)
- intake of travel and expenses
- rates and rules updated by the vendor

**What the cheap tier is criticised for** (Regnskap Norge 2025 via D §8.1, A §5.3):
- only one import per run (Tripletex)
- many clicks (PowerOffice)
- bugs in forskuddstrekk (tax withholding) and in holiday pay for employees over 60 (PowerOffice, Finago)
- payroll that cannot be finished without also going into accounting and the bank (Finago)
- poor control reports (all of them)

**Getting the core right is therefore a selling point in this tier.** Breadth is not.

**What SD Worx sells on top** (A §2.1, `R0-sdworx-meny.md`, meny.json `sdworx`):
- **HR:** People processes, Competence, Perform, SalaryReview, Health/Back2Work, Dashboard Management
- **Workforce management:** time, team planning, work schedules
- **Engine depth:** tariffs and regulations, automatic runs, many import templates, a report universe
- **Service and assurance:** portals for client, manager and employee, BPO, and ISAE assurance

None of this is required by the pilot profile (B3, R3 §4.1):
- 20–150 employees
- monthly and hourly pay
- OTP (mandatory occupational pension) on a contribution basis
- no tariff
- no turnus (rotating shifts)
- one legal entity

---

## 2. Table stakes: what a 20–150-employee organisation or AS and a small accounting firm will not buy without

"Table stakes" here means **the buyer walks away, or cannot run a lawful month, without it**. Each item gives the **simplest lawful version** that passes. Ids are from `analyse/build/data/omr-K*.json`. Items marked ⚠ were "Etter MVP", and this paper recommended moving them in; each such row says what PLAN.md and scope.csv decided. A few other ids listed here are LATER in scope.csv in their full form: F-ORG-01 and F-MYN-39 (Brreg lookup; facts entered by hand), F-LON-05 (customer's own pay types; M1 overrides text and accounts on standard types), F-FRA-36 (permittering counters; M1 enters the fields by hand), F-UTL-17 (private cost as a benefit), F-REG-08, F-ORG-18 and F-RAP-28 (dimension inheritance and cost per dimension), F-REG-24 (payroll against the ledger), F-SIK-09 (auditor access) and F-BYR-30 (exit package).

Some M1 ids are **pilot-pulled** (PLAN.md §6.1): in M1 only if a signed pilot needs them, chosen at G4 (31.3.2027). They are the accounting adapter (F-REG-18), board and fee recipient classes (F-ORL-01, F-ORL-15), travel allowances as pre-split lines (F-UTL-01, F-UTL-04, F-UTL-05, F-UTL-14, F-KJO-12), small association fees (F-ORG-06), PAYE cards, and the flat department and project code (F-ORG-13, F-ORG-14, F-ORG-16).

### 2.1 Legal payroll core (compliance; nothing here can be cut)

| # | Table stake (simplest version that passes) | Tier | Function ids | Why it is the floor |
|---|---|---|---|---|
| TS-01 | Employer set up with the facts from the Enhetsregisteret (the business register): legal entity, sub-units (underenheter), AGA (employer's social security contribution) zone and calculation code per sub-unit | M0 (entered by hand) | F-ORG-02, F-ORG-03; F-ORG-01 and F-MYN-39 (Brreg lookup and sync) are **LATER**: the facts are entered by hand for our own company and 3–5 pilots | The a-melding is per opplysningspliktig (reporting employer) and sub-unit. A wrong zone gives wrong AGA (D §6.2) |
| TS-02 | Person and employment register with every field the a-melding requires: fødselsnummer or D-number (national ID numbers), employment type, start and end dates, position percentage, hours, yrkeskode (occupation code), working-time arrangement, ansettelsesform (employment form), date of last salary change. Several employments per person. **Keep arbeidsforholdId (employment id) on a system switch** | M0 / M1 | F-PER-01, F-PER-02, F-PER-13 (one simple form), F-PER-14, F-PER-15, F-PER-19, F-PER-20, F-PER-22 (valid-time only, no bitemporal UI), F-PER-23, F-PER-24, F-PER-25, F-PER-27 (ansettelsesform only), F-TID-01 (a-melding code only) | Required a-melding fields. Skatteetaten's rules for switching systems require continuity (A §7.1) |
| TS-03 | Personal bank account with change control: log every change, flag new accounts in the control list | M0 | F-PER-07, F-BET-18 | Fraud risk and a revisor (auditor) expectation (D §1.3) |
| TS-04 | The 26 standard pay types plus the customer's own, with flags for tax, AGA, holiday pay, pension and sick-pay base, the a-melding code, the **trekkmetode** (table or percentage withholding), and one debit and one credit account | M0 | F-LON-01, F-LON-02, F-LON-05 (quarantine = "test before first use", no workflow), F-LON-06 | All competitors ship a catalogue (NettLønn has 160). Without trekkmetode, a bonus gets table withholding and is halved in December (B5 critic) |
| TS-05 | Pay agreement (monthly or hourly), fixed lines with dates, proration when someone starts, stops or changes position percentage | M0 (pay agreement) / M1 (fixed lines with dates F-LON-15, proration F-KJO-08) | F-LON-11 (monthly and hourly only, no ladders), F-LON-15, F-KJO-08 | Basic mechanics |
| TS-06 | Hourly pay and variable additions (quantity × rate, overtime, one-off), each line with an opptjeningsperiode (earning period) for pay made a month in arrears | M0 (hourly) / M1 | F-KJO-09, F-KJO-04, F-TID-05 (simplify: accept period sums per pay type with a source reference, pending R0 §7.5 pt 4), F-TID-08, F-TID-19 | Monthly plus hourly is the pilot profile. Variable pay is usually paid a month in arrears (D §1.2) |
| TS-07 | Import of variable data (CSV/Excel and API) with mapping that can be **re-run** (idempotent), a preview, and an unknown code that stops the line | M1 (idempotent pay input via the API, F-KJO-03, is M0) | F-KJO-03, F-LON-08, F-PLA-15, F-MIG-10 | "Only one import per run" is a documented Tripletex complaint (D §5.2). Bad mapping caused the Kristiansand error (D §4.4) |
| TS-08 | Tax cards: fetched via API at setup and per run, with daily changes, 50 % withholding when there is no card, frikort (tax-free card), and cards for the new income year | M0 entered by hand with four eyes, from Skatteetaten's tax-card file service or the current system (PLAN.md §1.4) / M1 API | F-TRK-01, F-TRK-02, F-TRK-03, F-TRK-10, F-MYN-25, F-MYN-26, F-MYN-27 | Every competitor fetches them. GRFS 7.4 (the accounting firms' standard) requires withholding to be based on fetched cards (E §1.1) |
| TS-09 | Forskuddstrekk (tax withholding): table via Skatteetaten's trekkrutine, percentage, method per pay type, summed basis when there are several payouts, no table withholding in June, half withholding in November or December, cap at the cash amount, main or secondary employer. Union dues paid through payroll reduce the withholding base (TS-14) | M0 / M1 (summed basis F-TRK-09; June F-TRK-11, for our own payroll by gate JUN27) | F-TRK-07 (own port tested 100 % against Skatteetaten's table file; the licence is asked for but does not block, PLAN.md Appendix A item 4), F-TRK-08, F-TRK-09, F-TRK-11, F-TRK-12, F-TRK-15, F-TRK-06 (simplified) | Law. Bugs here are what users hold against PowerOffice and Finago (D §8.1). **Note:** the half-withholding month (November or December) must be known before the shadow runs; PLAN.md checks December half withholding in shadow #2 (M0-S2) |
| TS-10 | AGA per sub-unit and zone, including AGA on the holiday-pay accrual and on the pension premium | M0 (one zone) / M1 (all zones) | F-KJO-13, F-KJO-14, F-PEN-06 | Law |
| TS-11 | Feriepenger (holiday pay): 10.2 % or 12 %, the extra for employees over 60, a basis per earning year, holiday profile, payout in June with ferietrekk (the deduction for holiday taken), payout on termination, accrual posting | M0 accrual / M1 June payout; for our own payroll on the M0+ track by gate JUN27 (14.5.2027), including the 60+ supplement with the 6 G cap at the G in force on 31.12 of the earning year (ferieloven § 10 (3)) | F-KJO-37, F-KJO-38, F-KJO-39, F-FRA-08, F-FRA-14, F-FRA-15, F-REG-11 | Law. Holiday pay for over-60s is where Finago failed in 2025 (D §8.1) |
| TS-12 | OTP contribution: the scheme for the employer, pension base per pay type, simple membership, employee share deducted before tax, premium entered per term (for AGA and the a-melding), pension provider (pensjonsinnretning) in the a-melding | M0 / M1 | F-ORG-27, F-PEN-01, F-PEN-03, F-PEN-04, F-PEN-05, F-PEN-09, F-PEN-10, F-MYN-08, F-REG-14 | OTP is mandatory, and the premium is AGA-liable (R3 §4.2) |
| TS-13 | Absence that affects pay: egenmelding (self-certified sick leave) and sykmelding (doctor's sick note), counting the 16-day arbeidsgiverperiode (the period the employer pays sick pay), pay during that period, an advance after it with a refund receivable and the AGA effect, unpaid leave, permittering (temporary layoff), and leave in the a-melding. **A basis report for the inntektsmelding, sent manually in NAV's portal** | M1 | F-KJO-10, F-FRA-01, F-FRA-02, F-FRA-21, F-FRA-22, F-FRA-25 (receivable entered by hand; K27 import F-MYN-34 is LATER), F-FRA-26 (one AGA method: deduct when received), F-FRA-34, F-FRA-36, F-FRA-37, ⚠ F-FRA-23 (basis printout only; **M1** in scope.csv; the inntektsmelding is entered in NAV's portal) | "Sykepenger and NAV refund" is on every must-list (A §6.2). PowerOffice charges extra for holiday and absence, but registering absence is assumed. The API is LATER (R3 §4.4) |
| TS-14 | Deductions: union dues, agreed deductions, utleggstrekk (wage garnishment) and old-style deductions registered manually with KID, each with its own a-melding line and payment. A samordnet (coordinated) deduction ends the old ones. **Union dues are not purely after tax:** the dues deducted reduce the withholding base, rounded up to whole kroner (skattebetalingsforskriften § 5-9-1), and are then taken from net (research report C #48 is wrong) | M0 (union dues, only if dues go through payroll) / M1 | F-TRK-23 (**M0**), F-TRK-24, F-TRK-19, F-TRK-20 (simple), F-TRK-22, F-TRK-18 | Union dues are on the must-list (A §6.2). The 2026 garnishment rules apply to everyone (D §0 pt 5). The API is LATER (R3 §4.4: 5 minutes per order manually) |
| TS-15 | Taxable benefits in kind as non-cash pay types (ekom (electronic communication), insurance, company car entered as a monthly amount) | M1 | F-LON-17 (amount entry; car calculator LATER), F-KJO-11 | Common for AS customers. Tripletex advertises company cars |
| TS-16 | Travel and expense lines from the expense tool or CSV, **pre-split** into tax-free and taxable with the right a-melding codes. **No own allowance calculator**: travel-rate tables and the allowance calculation are LATER (F-UTL-09–11) | M1, pilot-pulled (PLAN.md §6.1); fourth on the M1 cut order (§6.3) | F-UTL-01, F-UTL-04, F-UTL-05, F-UTL-14, F-UTL-17 (**LATER**), F-KJO-12 | Every competitor takes travel into payroll. Expenses only via integrations (B32) |
| TS-17 | Non-employee recipients: board fees (styrehonorar) and honoraria, with three recipient classes (employee, fee or office holder, expenses only). Board fees stay out of the holiday-pay and OTP base | M1, pilot-pulled (PLAN.md §6.1) | F-ORL-01 (3 classes, not 7), F-ORL-15 | Organisations and most AS pay board fees. Organisations are the second-sharpest segment (R3 §6.4) |
| TS-18 | Sluttoppgjør (termination settlement): final pay, holiday pay paid out, sluttårsak (end reason) in the a-melding | M1 | F-KJO-34, F-PER-19, F-FRA-15 | Happens every month at 20–150 employees |
| TS-19 | **Year-end rollover:** lock last year's holiday-pay basis and accumulators, apply the new rule pack and tax cards, carry balances forward | **M0** (F-KJO-41: for our own payroll the January 2027 go-live is the first year switch, PLAN.md §1.6, §7.4 item 3) | ⚠ F-KJO-41 (**M0**), ⚠ F-FRA-13 (**LATER** in scope.csv: manual carry-over the first time) | Any customer live in December needs it. Both functions were "Etter MVP". Because the current system submits all of 2026 (D1), Brutto's first year switch is January 2027 (by 15.1.2027) and its first December is 2027 (gate DEC27). The 2026 holiday-pay basis is imported by gate JUN27 (F-MIG-22) |
| TS-20 | Sammenstillingsoppgave (annual summary per recipient) by 31 January, including year-to-date figures from the old system after a mid-year switch | M1 (by 31.1 after go-live, delivered through Digipost; for our own payroll first for 2027, by gate AS27, 14.1.2028) | F-POR-16 (M1), F-MIG-20 (M1 in scope.csv, for pilots that start mid-year; not in M0, because the current system submits all of 2026), ⚠ F-MYN-36 (**M1**; this paper proposed merging it with F-POR-16, scope.csv keeps both rows. The legal basis is flagged "verifiseres", but market practice makes it table stakes either way) | Accounting firms bill it (70–200 kr, E §5.2). Finago charges 49 kr. GRFS 7.7 requires it of firms |

### 2.2 Running the month

| # | Table stake | Tier | Function ids | Why |
|---|---|---|---|---|
| TS-21 | Payroll run: ordinary and extra runs, several per month, free simulation and recalculation until approval, fixed calculation order | M0 / M1 (extra runs, F-KJO-29) | F-KJO-01 (ordinary, extra, correction, termination only), F-KJO-06, F-KJO-19, F-KJO-29 | Test runs are standard above about 50 employees (D §0 pt 3) |
| TS-22 | Control list before approval: totals compared with last month, per-employee changes over a threshold, zero or negative net, missing tax card, pay after the end date, new bank account, AGA zone changes | M0 basic / M1 | F-KJO-20, F-KJO-22, F-KJO-32, F-RAP-14 | Control is where 25–35 % of the time goes, and every system is criticised for weak control reports (D §1.3–1.4, §8.1) |
| TS-23 | Approval and lock: the person who prepares is not the person who approves (four-eyes when there are two or more users; an automatic notice as compensating control when there is only one person), BankID step-up, a locked run cannot change | M1 (M0: one step by a named approver who is not the preparer, re-authentication through the identity provider, no BankID) | F-KJO-23 (one or two steps only), F-KJO-24, F-KJO-25, F-SIK-03, F-SIK-12, F-SIK-13 | GRFS 8.1 and 8.6 for accounting firms. Auditor expectation (D §3.2) |
| TS-24 | Corrections after approval: a correction run for an earlier period with a replacement a-melding; back pay (etterbetaling) as a manual line with its period | M1 | F-KJO-28, F-MYN-18 | Corrections happen every month. **Full retro with knock-on effects is LATER** (§3) |
| TS-25 | Payslip with the legally required content as PDF, delivered digitally (Digipost), archived and available later | M0 PDF archive / M1 delivery through Digipost (bought, F-POR-12), with Digipost print or manual secure delivery for employees without it (F-POR-04). The employee portal and login are LATER (F-POR-01, F-POR-27, F-POR-28). Sixth on the M1 cut order: Digipost → manual secure delivery (PLAN.md §6.3) | F-KJO-42, F-KJO-44, F-POR-08 (M0: archived PDF/A, downloadable via the API), F-POR-12 (**M1**), F-POR-04 | Everyone has digital payslips (NettLønn, PowerOffice, Visma and Tripletex apps) |

### 2.3 Outputs to the authorities, money and the ledger

| # | Table stake | Tier | Function ids | Why |
|---|---|---|---|---|
| TS-26 | A-melding per opplysningspliktig and month: pre-validated, submitted via API with a systembruker (Altinn system user), feedback in plain language, replacement messages, **and a file for manual upload as fallback** | M0 = ⚠ F-MYN-14 file / M1 = API | F-MYN-01, F-MYN-02, F-MYN-07, F-MYN-09, F-MYN-10, F-MYN-11, F-MYN-12, F-MYN-15, F-MYN-16, F-MYN-20, ⚠ **F-MYN-14** | Every competitor down to Fiken submits directly. From 17.11.2026 Altinn II roles can no longer be used, so a systembruker is hygiene (E §0 pt 4). **F-MYN-14 was "Etter MVP"; scope.csv now has it in M0.** It exports the JSON the API takes; XML 2.3 is the costed fallback (PLAN.md §1.3). F-MYN-20 (a-melding 2.4) is M1 with gates 24-S and 24-T |
| TS-27 | Payment file (pain.001) for net pay. Forskuddstrekk payment with KID due the first business day after payout (M0: the KID comes from the a-melding feedback; Brutto's own KID only in M1, after it reproduces the 2026 KIDs, PLAN.md §1.4). AGA amount and KID per term. Garnishment payments. Employer's own bank accounts | M0 / M1 (payment information from the feedback, F-MYN-17) | F-ORG-25, F-BET-01, F-BET-02, F-BET-08, F-BET-09, F-BET-20, F-TRK-16, F-MYN-17 (M1), F-BYR-27 (M2) | New 2026 payment rules carry a penalty risk (R2V §7 #2). The bank file is the floor everywhere. Brutto never moves money (B12) |
| TS-28 | Accounting voucher per run with standard postings, net pay on 2930, and department and project dimensions. **Pushed to Tripletex and PowerOffice Go**, plus a generic file for every other system | M0 CSV with one flat department / M1: one adapter and the flat department and project code, both pilot-pulled (PLAN.md §6.1) | F-REG-02, F-REG-05, F-REG-07, F-REG-08 (**LATER**), F-REG-17, F-REG-18, ⚠ **F-REG-19**, F-ORG-13, F-ORG-14, F-ORG-16, F-ORG-18 (**LATER**; dimension sync and cost reports are LATER) | The pilots use Tripletex or PowerOffice Go (R3 §4.1). Visma Payroll Start is criticised for having no integrations. PowerOffice Go is the #4 system among payroll users (A §1.1). **This paper recommended moving F-REG-19 in. PLAN.md: the one M1 adapter (F-REG-18) is pilot-pulled at G4 and built only after a written OK on its API terms; F-REG-19 is LATER; the voucher file always works** |
| TS-29 | Standard reports: payroll journal, payroll list, holiday-pay list, deduction list, AGA per sub-unit and zone, all exportable to Excel, CSV and PDF. Cost per department and project (F-RAP-28) is **LATER** | M0 (attestation summary, payroll journal as PDF and CSV, one run export) / M1 (holiday-pay list for our own payroll by gate JUN27) | F-KJO-45, F-REG-06, F-RAP-04, F-RAP-09, F-RAP-10, F-RAP-11, F-RAP-12, F-RAP-13, F-RAP-28 | Revisor and accountant expectations (D §4.2). Matrix has 12 reports (R0 §1) |
| TS-30 | Monthly reconciliation of payroll against the a-melding, and payroll against the general ledger for the payroll accounts | M1 | F-REG-25, F-REG-24 (simple; **LATER** in scope.csv: Brutto shows its own voucher totals and the accountant compares), F-RAP-15 | NettLønn advertises reconciliation against accounting. A typical audit finding (R2V §7 #8) |
| TS-31 | Deadline calendar: payout date, withholding due date, a-melding due on the 5th, AGA term, shown as statuses or tasks | M0 (deadlines computed per run) / M1 (statuses and tasks) | F-ORG-22, F-ORG-23, F-ORG-24, F-MYN-19 | The 2026 rules made the dates denser (D §0 pt 4) |

### 2.4 Switching and trust

| # | Table stake | Tier | Function ids | Why |
|---|---|---|---|---|
| TS-32 | Migration: an Excel template, validation, arbeidsforholdId kept, year-to-date per a-melding description, holiday-pay basis for last and this year, open deductions, leaves and ongoing absence (including an arbeidsgiverperiode in progress), pension and fixed lines, **two parallel periods equal to the øre with a deviation report** (gate P-PAR) and a reconciliation against the A07 report before the first a-melding | M0 (cutover for our own payroll: F-MIG-16, -17, -27, -28, -31) / M1 | F-MIG-15, F-MIG-16, F-MIG-17, F-MIG-21, F-MIG-22, F-MIG-25, F-MIG-26, F-MIG-27, F-MIG-28, F-MIG-31, F-FRA-07 | "Migration without risk" is the main switching barrier (A §6.2, §7). Free migration is the market norm (E §0 pt 6) |
| TS-33 | Login and access: managed OIDC login with MFA in M0 and BankID in M1, roles (payroll, approver, accountant, read-only auditor), tenant isolation, audit log, encryption of fødselsnummer and account numbers, backup, data processing agreement (DPA), data in Norway or the EEA | M1 (M0 minimal) | F-SIK-01, F-SIK-05, F-SIK-09, F-SIK-11, F-SIK-15, F-SIK-19, F-SIK-25, F-SIK-27 | Payroll data includes GDPR art. 9 special categories. Accounting firms ask for a DPA and data location (E §4 #20) |
| TS-34 | Rates and rules maintained by the vendor (G (the national insurance base amount), AGA rates, trekk tables; tax-free allowance rates are LATER with the travel-rate tables), plus payroll-competent support and on-call cover in payroll week | M0 / M1 (payday contingency, F-SIK-34) | F-KJO-18 (simple versioned rule pack), F-SIK-34 | NettLønn advertises "always updated rates". Support is SD Worx's biggest weakness and cheap to win on (A §6.1 pt 5) |

### 2.5 The small accounting firm (byrå) adds (M2)

PLAN.md moves all byrå features to **M2** (from 1.8.2028 at the earliest, new B45). A firm's *own* payroll can still be an M1 pilot as a direct customer. The tier column below shows the decided tier; ids that scope.csv puts in LATER are marked.

| # | Table stake | Tier | Function ids | Why |
|---|---|---|---|---|
| TS-35 | Multi-client: one login, quick switching between clients, roles per client, a client list with **status per client and month** (run approved, a-melding sent and accepted, payments confirmed) | M2 | F-BYR-01, F-BYR-02, F-BYR-03, F-BYR-12 (simple status list, no cross-client queue engine) | E §4 #1–3 and #8. NettLønn and Finago include multi-client |
| TS-36 | The firm's client system user (agent systembruker) in Altinn, a per-client access check, and a log of which person submitted what | M2 | F-MYN-04, F-MYN-05, F-BYR-07, F-BYR-08, F-BYR-10 | Mandatory with Altinn 3 (E §3.4). The supplier must log at person level |
| TS-37 | Bulk actions and copying: fetch tax cards and feedback for all clients, copy pay types and account setup from one client to another | M2 (all three ids LATER in scope.csv; PLAN.md §9: later in M2) | F-BYR-14, F-BYR-15 (feedback and A07 only; garnishment orders LATER), F-BYR-18 (copy or template, no live inheritance) | E §4 #4–5. NettLønn copies settings between companies |
| TS-38 | Evidence that the client approved the payroll (GRFS 8.6), and a full export per client (documentation for 5 years, and exit) | M2 | F-BYR-26, F-BYR-30 (LATER; PLAN.md §9: exit package later in M2) | GRFS 8.6 and 12.3. Firms will not risk lock-in (E §4 #14) |

**Count:** 38 items, 203 function ids. 197 are already MVP. The six that are not, with the tier PLAN.md and scope.csv decided:
- F-MYN-14: M0
- F-KJO-41: M0
- F-FRA-13: LATER
- F-REG-19: LATER
- F-FRA-23: M1
- F-MYN-36: M1

### 2.6 What is deliberately *not* in the table stakes (but the market has it)

These items are common in the market but no pilot buyer will walk away without them:
- **An employee app or portal beyond payslips** (holiday applications, egenmelding, changing your own account number). PowerOffice charges extra for holiday and absence. Visma has it only in Smart.
- **Holiday-day balances.** Feriepenger is table stakes, but day balances are not (the holiday-days ledger, F-FRA-09, is LATER). The payroll officer registers holiday taken (as in Visma Start).
- **A manager approval inbox.**
- **Bank status (pain.002/camt.054).** The file plus a manual "paid" confirmation is enough (R3 §4.4).
- **The NAV inntektsmelding API and the garnishment-order API.** The manual portal works at 20–150 volumes (R3 §4.4).

---

## 3. Do not chase in year 1: SD Worx and enterprise features to exclude explicitly

"Do not chase" applies to the breadth. scope.csv keeps the simplest version of some ids in these rows in M0 or M1, for example: CSV import, locking and correction of hours (F-TID-20–23), handling of received, pre-split expense lines (F-UTL-18, -24; pilot-pulled), the fixed-order deduction queue (F-TRK-26), returned payments (F-BET-16), the BankID broker (F-PLA-29), e-mail notices and a derived task list (F-KOM-01–03), tenant status flags (F-PLA-34), manual pay-type mapping (F-MIG-13), search in the person register (F-PER-11), pay grade as a pass-through field (F-PER-26), the taxable insurance benefit (F-PEN-16), the 10,000-kr rule for tax-exempt organisations (F-ORG-06, pilot-pulled), a reference page for the API (F-PLA-05), two manager functions (F-LED-04, F-LED-13) and an immutable payroll document store (F-HR-01, M0). K27 import (F-MYN-34) and the travel-rate tables (F-UTL-09) are LATER. Check scope.csv before cutting an id.

### 3.1 From SD Worx's HR menu (`analyse/research/R0-sdworx-meny.md` → `analyse/build/data/meny.json` mapping)

| SD Worx area | Brutto ids | Tier | One-line reason |
|---|---|---|---|
| Competence (overview, search, GAP analysis, job profiles) | F-UTV-01–06 | **CUT** (F-UTV-03–06) / **LATER** (F-UTV-01, -02) | A talent/HR market (Huma, Simployer). No pilot buys payroll for it (B34) |
| Perform (talks, targets, statistics), talent | F-UTV-07–09, F-UTV-11 | **CUT** (F-UTV-09, -11) / **LATER** (F-UTV-07, -08) | Same as above. Not payroll |
| SalaryReview (pots, manager proposals, negotiation protocol) | F-LON-22–30, F-UTV-10 | **LATER** (F-LON-24, -28, -29; before the pilots' first wage settlement, about May 2028) / **CUT** (the rest) | For non-tariff customers with 20–150 employees, importing new salaries with an effective date plus a back-pay line covers it (R3 §4.4: 2–4 h manually) |
| Health / Back2Work (follow-up plan, dialogue meetings, health search) | F-HEL-01–12 | **LATER** (F-HEL-01–09, -11) / **CUT** (F-HEL-10, -12) | NAV and the HR system own the process. Payroll only needs the pay effect of sick leave (R2V §9) |
| Dashboard Management (announcements, links, slideshow) | F-KOM-07, F-KOM-08 | **CUT** | An intranet feature with no payroll value |
| Process Overview, Messages, workflow engine | F-KOM-04, F-KOM-05, F-KOM-09 | **LATER** (F-KOM-04, -05) / **CUT** (F-KOM-09) | E-mail plus tasks derived from state (R0 §3 #5) is enough for 3–5 pilots |
| Organization Chart, organisation tree with history, re-organisation | F-HR-07, F-ORG-09, F-ORG-10 | **LATER** (F-ORG-09) / **CUT** (F-HR-07, F-ORG-10) | Flat departments and projects are enough (R0 §7.2) |
| Time: Calendar, Team Planning, Work Time Schedule, turnus, clocking, time bank, flexitime | F-TID-02–04, F-TID-06, F-TID-07, F-TID-09–18, F-TID-20–23, F-TID-25–27 | **CUT** (M1) / **LATER** (B20 module) | Quinyx, Planday, Tamigo and GAT own scheduling. Brutto takes CSV with pay type × quantity (R2V §9) |
| Expense › Voucher Handling (own expense module and rate engine) | F-UTL-03, F-UTL-06, F-UTL-09–13, F-UTL-18, F-UTL-24 | **LATER** in core (B32; F-UTL-03, -06, -09–13). F-UTL-18 and -24 stay M1 for pre-split lines, pilot-pulled | The expense tool calculates allowances. Brutto only classifies the lines it receives (TS-16) |
| Delegate, manager portal, approval chains from the hierarchy | F-LED-01–19, F-ORG-12 | **LATER** (B39); F-LED-06 and -12 CUT; F-LED-04 and -13 stay M1 in their simplest form | Pilots need one or two approval steps, not a chain |
| Advanced Search, Analytics dashboards, report builder, BI/OData | F-PER-11, F-RAP-06, F-RAP-07, F-RAP-08 | **LATER** (F-RAP-07) / **CUT** (F-RAP-06, -08); simple search F-PER-11 is M1 | Fixed reports, CSV and the API are enough. Big customers want raw data, not our charts (R2V §9) |
| Admin Modules › Connector (app catalogue, installations, webhooks, sandbox) | F-PLA-05–12, F-PLA-19 | **LATER** (2028); F-PLA-07 CUT; F-PLA-05 is M1 as a generated reference page only | For 3–5 pilots and 1–2 firms, adapters operated by Brutto are enough |
| Payslip portal as a native mobile app | F-POR-03 (as an app), F-POR-05, F-POR-06 | **LATER** (portal and app) | Digipost (F-POR-12, M1) is enough. The employee portal and login are LATER (F-POR-01, F-POR-27, F-POR-28) |

### 3.2 From SD Worx and Visma's payroll and enterprise depth

| Feature | Brutto ids | Tier | One-line reason |
|---|---|---|---|
| Tariff libraries, salary ladders, automatic step-up by seniority | F-ORG-26, F-LON-19–21, F-PER-26 | **LATER** (2028–29); F-PER-26 stays M1 as pass-through pay grade and seniority | The pilot profile has no tariff. Tariff brings KLP and turnus with it (B3 critic) |
| Retro with knock-on effects (hourly-dependent additions, corrected inntektsmelding, pension) | F-KJO-26, F-KJO-27, F-ORG-19, F-REG-13 | **LATER** (Q3 2028, R3) | Valuable and durable, but heavy. **Design the data for it now** (immutable runs, valid-time, §4 D2) and build the feature later |
| KLP/SPK (public-sector pension schemes), AFP (contractual early retirement), insurance register | F-PEN-11–18 | **LATER** / **CUT** (F-PEN-12, -13, -15, -17, -18); the taxable insurance benefit F-PEN-16 is M1 | Out of the pilot profile (B3, R3 §4.1) |
| Group with several legal entities, structural changes, moves between entities | F-ORG-05, F-ORG-08, F-PER-16, F-PER-17 | **LATER** / **CUT** (F-ORG-08) | One legal entity in the pilots |
| Automatic run plans, cut-off engine, June and December as separate plans | F-KJO-02, F-KJO-40, F-PLA-21 | **LATER** | Manual runs with a calendar are enough (TS-31) |
| NAV automation (sick note and claim, inntektsmelding API, K27 import) | F-FRA-20, F-MYN-30–35 | **LATER** (Q2 2028), including K27 import (F-MYN-34): M1 enters the refund by hand, uses one AGA method and lists cases near the 3-month deadline (PLAN.md §6.2). F-MYN-32 and -33 are CUT | Manual NAV portal plus a refund receivable. About 15 minutes per case (R3 §4.4) |
| Garnishment-order API, a full deduction queue with protected amounts and carry-forward | F-TRK-17, F-MYN-28, F-MYN-29, F-TRK-26 | **LATER**; F-TRK-26 stays M1 as a fixed-order queue | Register orders manually with KID. Use a fixed order and stop when net goes below zero (manual decision) |
| Open banking, pain.002/camt.054, bank reconciliation, foreign accounts | F-BET-11, F-BET-12, F-BET-14–16, F-BET-22, F-REG-26 | **LATER** (B12, B40) / **CUT** (F-BET-11); returned payments F-BET-16 are M1 | The file plus a manual "paid" confirmation |
| More accounting adapters (Xledger, Visma, Fiken), practice systems | F-REG-20–22, F-BYR-34, F-PLA-31 | **LATER** (F-REG-20, F-BYR-34) / **CUT** (F-REG-21, -22, F-PLA-31) | The generic file covers them until a paying customer asks |
| ISAE 3402, ISO 27001, SSO/SCIM | B15, F-PLA-29 (the SSO part), F-SIK-04 | **LATER** (ISAE plan in 2028) | Required from about 250 employees (D §4.3). Send a security package plus DPA now |
| Weekly or fortnightly pay, gross-from-net, net pay agreements, maritime, Svalbard, special withholding rules | F-KJO-33, F-LON-13, F-PER-28, F-TRK-13, F-TRK-14 | **CUT** until asked (F-TRK-13 is LATER) | Rare in the segment. Stop and warn |
| Organisation-life breadth (OrgLab/Tikket inflows, local branches, conference mode, artist tax, meeting allowances, rapid event payouts) | F-ORL-02–14, F-ORL-16–33 | **LATER** (except TS-17); some F-ORL ids CUT. The 10,000-kr rule (F-ORG-06) is M1, pilot-pulled: **only if a pilot is a tax-exempt organisation**. F-ORL-11 is LATER | Three recipient classes plus board fees cover the pilots (R0 §7.3) |
| Multi-channel notification engine (push, SMS, Teams) and a shared task inbox | F-KOM-01–03, F-KOM-06 | **LATER** (F-KOM-06); F-KOM-01–03 stay M1 as e-mail plus a derived task list | E-mail plus a list derived from state |
| Accounting-firm extras: chains, mass reassignment, quality KPIs, powered-by, billing basis, licence switching | F-BYR-04, F-BYR-20, F-BYR-28, F-BYR-32, F-BYR-33, F-PLA-34, F-PLA-35 | **LATER** / **CUT** (F-BYR-20); tenant status flags F-PLA-34 are M1 | Invoice 1–2 firms manually |
| AI features (AI mapping, "ask the payslip", assistant, reading unstructured input) | F-MIG-13, F-POR-13, F-PLA-36, F-BYR-23 | **LATER** (B13) / **CUT** (F-POR-13, F-BYR-23); F-MIG-13 is M1 as manual mapping | Rule-based explanations first. An LLM only phrases the text later |
| ARP/equal-pay reporting, ESG, budgets, forecasts, simulations | F-RAP-24, F-RAP-27, F-RAP-30–33, F-MYN-37 | **LATER** (F-RAP-24, F-MYN-37) / **CUT** (F-RAP-27, -30–33) | A CSV export covers the biennial pay survey required above 50 employees |
| Personnel file and document archive, contract templates, on- and offboarding | F-HR-01, F-HR-02–08 | **LATER** / **CUT** (F-HR-06, -07); F-HR-01 stays M0 as the immutable payroll document store | The payslip archive is enough. Huma owns personnel files (B21, B34) |

---

## 4. Cheap differentiators worth keeping in the MVP

Rule of thumb from R3 §10.2: whatever is a UI feature gets copied within six months, while what lives in the architecture lasts. The six below are kept because each is **cheap when built in from the start and expensive to add later**, or nearly free once table stakes exist. All developer-week estimates are **[A]**, for a team using coding agents, and assume the engine is designed with them in mind.

| # | Differentiator | Ids | Build cost if designed in from day 1 | What makes it expensive (avoid in M1) | Durable? | Verdict |
|---|---|---|---|---|---|---|
| D1 | **Explanation trace per payslip line:** every calculation step stores the rule, rule-pack version, inputs, rate and result. The line shows "why 12 %?" and where the value was inherited from | F-KJO-16, F-KJO-07, F-LON-04 | **2–4 dev-weeks** on top of a non-tracing engine, plus some storage per payslip. **High cost to retrofit** | A generic "as-of" query layer (B6 critic, D-38). LLM phrasing. Explaining non-calculation data | Yes. Old engines must be rebuilt to match it | **M0** |
| D2 | **Approved runs never change:** a hash lock, corrections as new runs, frozen values shown on the calculation | F-KJO-24, F-KJO-25, F-MYN-11, B6, B43 | **1–2 dev-weeks** if storage is append-only from the start | Bitemporal history on every field (limit it to data that affects calculation, B6 critic) | Yes. It is the basis for retro later, which is Visma's biggest weakness (D §8.1) | **M0** |
| D3 | **A07 reconciliation as the truth:** compare Brutto's own a-melding with the A07 per employee and month. A "diff 0" proof for migration and the parallel run. An employee overview from the a-ordningen | F-MYN-21, F-MYN-42 (LATER in scope.csv; its one essential check folds into F-MYN-21), F-PER-35, (F-REG-30 LATER) | **2–3 dev-weeks** once Maskinporten and the systembruker exist (A07 uses the same access and scope as a-melding submission, R0 §7.4) | The Digdir onboarding lead time (3–5 months; shared anyway). A07 lacks the holiday-pay basis (N03). A07 against the general ledger needs adapters that read the ledger, so that is LATER | Partly. **NettLønn already advertises "employments synchronised via A07"**, so the edge is using A07 as a *control*, not merely having it | **M1** |
| D4 | **API-first plus an MCP for reading and drafts:** the UI is a client of the public API, and an agent can read the payroll, prepare the month (import the basis, create a draft run) and explain it | F-PLA-01, F-PLA-03, F-PLA-33 | Near zero for the API if it is an architecture rule. **1–2 dev-weeks** for MCP read tools generated from OpenAPI | CI-enforced parity for every function (B41). Agent-started actions with approval and preview (F-PLA-37, LATER). Developer portal, versioning and sunset machinery (F-PLA-02, F-PLA-05). Webhooks | No. **Intect already has an open API** (A §3). The edge is that "an agent prepares and explains the month", not the API itself | **M1**, scoped: read and draft tools only; approving, sending and paying are human-only operations that agents cannot call |
| D5 | **A deviation list that explains itself:** each change against last month gets a rule-based reason from the trace (new pay type, rate change, tax card, absence, proration, back pay) | F-KJO-20 (+ D1), later F-KJO-21 | **2–3 dev-weeks** once D1 exists | AI explanations in free text, configurable threshold engines | Yes (it needs D1) | **M1.** This is what accounting firms pay for: minutes per payslip (E §5.3) |
| D6 | **Separate status tracks after approval:** payslip, payment, withholding, voucher and a-melding each have their own status, and tasks exist as long as the state calls for them | B43, R0 §3 #1 and #5 | **1–2 dev-weeks** (state machines instead of one linear status) | A generic workflow engine (F-KOM-04) | Partly (Matrix has it) | **M1.** It gives the firm's client status list (TS-35) almost for free |

**Also free:** a transparent price with everything included (§5). It is a decision, not a build, and it is copyable (Intect already publishes its price).

**Honest note:** the differentiators do not win a single deal if a table stake is missing. Put D1 and D2 into the engine in M0 because they are architecture. D3–D6 come after TS-26 (the API) is in place.

---

## 5. What the cheapest competitors charge, and what it means for a narrow MVP

### 5.1 Monthly software cost (ex. VAT) for a customer with N paid recipients

| Product | Pricing rule | N = 30 | N = 100 | N = 150 |
|---|---|---|---|---|
| NettLønn [V] | 39 kr per payslip | 1,170 | 3,900 | 5,850 |
| PowerOffice Go payroll [V] | 195 + 35 per recipient | 1,245 | 3,695 | 5,445 |
| Finago Payday [V] | 49 per payslip (+ 49 per annual summary per year) | 1,470 | 4,900 | 7,350 |
| Tripletex [V] / [A] | Payroll is in Pro (479 kr incl. 1 payroll user). +65 per extra payroll or travel user, +39 per employee for time | ≈ 0–200 marginal on top of the accounting subscription | same | same |
| Fiken [V] | 69 kr per user | ≈ 69 | not a realistic fit above about 10 employees | – |
| Uni Micro, accounting-firm cost price [V] | 12 / 9 kr per active employee (resale price 20 / 15) | 360 | 900 | 1,350 |
| Visma Payroll Start / Smart [T] | 57 / 100 kr per active employee | 1,710 / 3,000 | 5,700 / 10,000 | 8,550 / 15,000 |
| Intect [V] | 39 DKK per payslip (≈ 60 NOK [A]) | ≈ 1,800 | ≈ 6,000 | ≈ 9,000 |
| **Brutto B17 proposal** [A] | 69 per recipient, minimum 1,490 per legal entity | 2,070 | 6,900 | 10,350 |

### 5.2 Implications for positioning a narrow MVP [A]

1. **The narrow MVP is a NettLønn/PowerOffice/Finago-class product, not a Visma Payroll Smart or SD Worx one.** M1 has no tariff, no full retro, no modules and no app. Feature for feature, buyers will compare it with the 35–49 kr tier. The 69 kr in B17 sits at the level of Visma Payroll Pluss and Smart, and cannot be defended on breadth in year 1. Two things can justify it: measured minutes saved per payslip (accounting firms) and fewer errors (direct customers), both proven in the pilots.
2. **Suggested pilot and list price** (to test in interviews, as B17 says; PLAN.md §8 downgrades B17 to after M1):
   - **Pilots:** a flat fee during the pilot (PLAN.md §6.4), then a price guarantee, as in R3 §6.5. The B24 calculation guarantee is downgraded to after M1 (PLAN.md §8).
   - **Direct customers:** a list price in the 39–49 kr band per paid recipient, to be tested in pilot conversations (PLAN.md §6.4, estimate), with a minimum fee per legal entity to cover the fixed cost of the a-melding and support. All inclusive: annual summary, A07 reconciliation, API/MCP and digital payslip through Digipost. Finago charges extra per annual summary, and Visma Start has no integrations.
   - **Accounting firms (M2):** 20–30 kr net per payslip. That is above the Uni Micro cost price and below NettLønn's list price, and it is justified only if it saves 3–5 minutes per payslip (E §5.3).
   - **Later:** raise the price toward B17 when tariff, retro and modules arrive.
3. **Price does not trigger a switch.** It only removes an objection (A §6.2 pt 4). The triggers are:
   - a forced migration: Visma Lønn closed in 2024, and Altinn 3 and the systembruker from 17.11.2026 (E §0 pt 4)
   - outgrowing Tripletex or PowerOffice payroll
   - a change of accounting firm
   - dissatisfaction: NettLønn scores 2.9 out of 6

   Sell **risk removal**: migration with diff 0 against the A07 (D3), a parallel month, a named onboarding contact, and payroll-week support.
4. **NettLønn's dissatisfied customers are mostly too small to sell to directly.** NettLønn claims 3,000+ customers and 30,000+ payslips a month, which is about 10 payslips per customer (A §2.3). They are below the M1 floor of 20 employees, so reach them through accounting firms, not direct sales.
5. **The bundling threat is real.** For a Tripletex or PowerOffice customer, payroll is almost free inside a subscription they already pay for. A standalone Brutto adds a line item, so:
   - (a) the integration with their ERP must be flawless (TS-28; this paper wanted F-REG-19 in M1, but PLAN.md makes the one M1 adapter pilot-pulled and builds it only after a written OK on its API terms; F-REG-19 is LATER, and the voucher file is the fallback)
   - (b) the case has to be control, auditability and time, not features
   - (c) Brutto should avoid customers that Visma is already moving up to Payroll (R3 §10.1)
6. **The revenue is a proof vehicle, not a business, in year 1:**
   - **Direct:** 5 pilots × 80 recipients × 45 kr × 12 ≈ 0.2 MNOK annual recurring revenue (ARR), at list price after the flat-fee pilot period.
   - **Accounting firm (M2):** one firm with 30 clients × 12 payslips × 25 kr × 12 ≈ 0.1 MNOK.

   **Do not spend MVP capacity on monetisation machinery** (F-BYR-32, F-BYR-33, F-PLA-34, F-PLA-35). Invoice by hand.
7. **One-line position for the MVP** (accounting-firm clients from M2): "Safe, explainable payroll for organisations and accounting-firm clients with 20–150 employees who keep their Tripletex or PowerOffice ledger. Every number on the payslip is explained, every month is reconciled against the a-ordningen, and an agent can prepare the month." It must **not** be pitched as "SD Worx for less".

---

## Appendix A: MVP functions (305) that are not table stakes (108)

These are the 305 MVP functions minus the 197 table-stakes ids that are already MVP, sorted by role: 22 enablers, 13 differentiators, 14 hygiene and 59 candidates to defer. This is a lens for the other reviewers, not a final cut; scope.csv holds the decided tier of each id, and several candidates below stay in M0 or M1 in their simplest version (for example F-TRK-26 and F-TRK-27). Legal requirements in the column "Legal or security hygiene" stay in.

| Category | Ids | Comment |
|---|---|---|
| **Engine and data enablers** (invisible, needed for correctness) | F-KJO-05, F-KJO-15, F-KJO-17, F-KJO-46, F-LON-14, F-PER-18, F-PER-36, F-TRK-04, F-TRK-28, F-FRA-06, F-MIG-04, F-MIG-14, F-MIG-18, F-PLA-18, F-UTL-02, F-REG-03, F-REG-10, F-REG-23, F-MYN-23 (simple: log raw requests and responses), F-PLA-26, F-PLA-27, F-PLA-29 (umbrella entries) | Keep, in their simplest form. F-TRK-28 and F-REG-03 are LATER in scope.csv |
| **Differentiators** (§4) | F-KJO-07, F-KJO-16, F-LON-04, F-MYN-21, F-MYN-42, F-PER-35, F-PLA-01, F-PLA-03, F-PLA-33, F-PLA-37 (LATER in scope.csv: agents cannot start legal-effect actions in M1), F-BET-17, F-MIG-30, F-MIG-32 (lightweight) | Keep D1/D2 in M0 and the rest in M1, except F-MYN-42 and F-PLA-37 (LATER) |
| **Legal or security hygiene** (not buyer-driven, but required) | F-PER-04, F-PER-12 (data subject access as a manual export), F-FRA-05, F-SIK-08, F-SIK-16, F-SIK-28, F-SIK-33, F-SIK-36, F-REG-28, F-BET-21, F-LED-04, F-SIK-35 (as golden-case regression tests), F-ORG-06 (only if a pilot is a tax-exempt organisation) | Keep, simplified. F-SIK-20: per-tenant keys yes, crypto-shredding LATER. F-PER-04 and F-PER-12 are LATER in scope.csv |
| **SD Worx-style breadth or over-engineering** (candidates to defer) | F-HR-01, F-ORG-15, F-ORG-28, F-ORG-29, F-PER-03, F-PER-06 (minimal fields only), F-PER-11, F-PER-21, F-PER-26, F-PER-34, F-LON-10 (only quantity × rate, fixed amount and percentage), F-TRK-26, F-TRK-27, F-FRA-03 (CSV only), F-FRA-09, F-TID-20, F-TID-21, F-TID-22, F-TID-23, F-UTL-03, F-UTL-06, F-UTL-09, F-UTL-10, F-UTL-11, F-UTL-12, F-UTL-13, F-UTL-18, F-UTL-24, F-MYN-06, F-MYN-22, F-MYN-24, F-BET-06, F-BET-13, F-BET-19, F-REG-01, F-REG-27, F-REG-29, F-REG-30, F-POR-27, F-LED-13, F-BYR-04, F-BYR-17, F-BYR-19, F-BYR-32, F-BYR-33, F-RAP-01, F-RAP-07, F-RAP-17, F-RAP-34, F-PLA-02, F-PLA-05, F-PLA-17, F-PLA-34, F-SIK-06, F-MIG-13, F-KOM-01, F-KOM-02, F-KOM-03, F-KOM-06 | Defer or simplify:<br>• **F-TRK-27:** the protected amount (vernet beløp) for agreed deductions must still be respected. Check it manually in M1.<br>• **F-BET-06 and F-BET-19:** keep "no payment file before approval" as a simple rule.<br>• **F-BYR-19:** the approval signature is the GRFS quality check |

---

## Sources

- NettLønn prices: https://nettlonn.com/priser-nettlonn. Features: https://nettlonn.com/funksjoner-i-nettlonn. Home page: https://nettlonn.com (fetched 29.10.2026)
- PowerOffice prices: https://poweroffice.no/no/priser (fetched 29.10.2026)
- Tripletex prices: https://www.tripletex.no/priser/ (fetched 29.10.2026)
- Finago prices: https://finago.no/priser (fetched 29.10.2026)
- Fiken prices: https://fiken.no/priser (fetched 29.10.2026)
- Visma Payroll packages: https://www.vismasoftware.no/lonn-hr/pakker-priser (fetched 29.10.2026). Third-party prices: https://www.hr.software/reviews/visma-net-payroll (via A §2.2)
- Intect: https://intect.io/en/scandinavian-payroll-system/ (fetched 29.10.2026)
- Uni Micro accounting-firm prices, accounting-firm invoicing levels and GRFS: `analyse/research/E-byra.md` §1, §4, §5
- Regnskap Norge "Lønnssystemer 2025" satisfaction scores and complaints: `analyse/research/A-marked-konkurrenter.md` §1.1, `analyse/research/D-praksis.md` §8.1
- SD Worx menu: `analyse/research/R0-sdworx-meny.md`, `analyse/build/data/meny.json` (`meny.sdworx`)
- Matrix Lønn: `analyse/research/R0-matrix-lonn.md`
- Strategy critic (MVP list, manual fallbacks, durable advantages): `analyse/research/R3-kritikk-strategi.md` §4, §6, §10
- Decided tiers: `PLAN.md` and `docs/plan/scope.csv`
