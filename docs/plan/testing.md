# Correctness and verification strategy for M0 and M1

> **Status:** Working paper from the scope review of 29.10.2026. [PLAN.md](../../PLAN.md) is the main plan; where this paper and PLAN.md disagree, PLAN.md wins.
> **What it is for:** how we prove that Brutto's payroll is correct: the golden-case lists, withholding-table conformance, a-melding validation, the shadow and parallel-run protocols, and the test gates for M0 and M1.

Reviewer: correctness and verification. Date: 29.10.2026. Tiers follow PLAN.md and [`docs/plan/scope.csv`](scope.csv) (M0, M1, M2, LATER, CUT). Gate names and dates follow PLAN.md §3.

**Inputs read:** `analyse/research/C-beregning.md` (§0, §2–5, §10–13), `analyse/research/R3-kritikk-domene.md` (all), `analyse/research/F-arkitektur.md` (§1.10, §6.4–6.5, §7), `analyse/research/R3-kritikk-strategi.md` §2.3–2.4, `analyse/research/B-myndigheter.md` §2, §10, `analyse/research/S-avklaringer-fra-sally.md` §6 pkt. 27, `analyse/build/data/design.json` (B6, B12, B16, B19, B24, B26, B28, B37, B41–B43), `analyse/build/data/fase1.json` (D05, L01–L03), `analyse/natt/funn/N08.md` (§3, §7, §8, §14), `N13.md` (all), `N14.md` (all), `N39.md` (§6–7), plus the functions F-TRK-07–12, F-KJO-13/14/17/18/42, F-MYN-10/12/14/21, F-REG-30, F-SIK-35/36, F-MIG-16/21/31/32.

**N22 does not exist.** N39 refers to "N22" as the TT02 test plan, but there is no `analyse/natt/funn/N22.md`. Section 3.3 below is the TT02 plan, built on N39 §6.

**Markers:** [U] means unverified. The rule must be confirmed (by Skatteetaten, NAV, a lawyer or an external payroll expert) before a golden case that depends on it can be signed. Norwegian terms get a gloss the first time they appear.

---

## 0. Summary

1. **Errors come from transitions and inputs, not from the table.** The test effort is aimed there: migrated balances, tax cards and pay types entered by hand, December and June, and the year boundary. In M0, the parallel run in November and December plus the opening-balance check against A07 (the reconciliation report from the a-ordning, the national payroll reporting scheme) carry more weight than any number of unit tests.
2. **The oracle matters more than the language.** Expected values come from four sources, and none of them is Brutto's own code:
   - Skatteetaten's withholding table file and trekkrutine (the withholding algorithm)
   - hand calculations signed by the payroll-domain owner
   - the old payroll system's output during the parallel run
   - A07 and the a-melding feedback (A03)

   Coding agents may never change an expected value (D-48). CODEOWNERS on `golden/**`, `rules/**` and the a-melding mapping enforces this.
3. **Every money type uses `rust_decimal`, with one exception.** The `brutto-trekkrutine` crate must compute in `f64`, in the same operation order as Skatteetaten's Java. Exact decimal arithmetic gives 1 kr errors on 60 of 1.09 million table rows (N13 §1.4). The text-file test guards that crate.
4. **"Table 7100", used in earlier drafts, no longer exists.** The 71xx numbering ended in 2024. From 2025 the tables are 8000–8400 (deduction tables) and 9010–9400 (addition tables). The golden cases below use 8000.
5. **M0 needs 30 golden cases (M0-01–30), about 200 payroll-domain hours and about 3 developer-weeks of test harness.** The first 20 cases are signed and green at the engine spike (M0-α, 27.11.2026), and all 30 at M0 exit. Three more cases are dated (§4.1): M0-31, union dues, needed at M0 exit only if dues go through payroll; M0-32, the 60+ holiday-pay supplement, before gate JUN27 (14.5.2027); and M0-33, an hourly employee in December, before gate DEC27 (15.11.2027). The gate before Brutto becomes system of record (M0-L): two shadow periods (November and December 2026) with zero unexplained differences, and 100 % conformance with both the 2026 and the 2027 withholding-table files. The decision on 15.1.2027 is for period 2027-01, which is a stretch (about 40 %). The planning date is 2027-02 (about 65 %), and 2027-03 is the latest.
6. **M1 adds about 34 named cases and fills a coverage matrix to about 150 signed cases** (§3.7), 20 % countersigned externally, and about 1,000 payroll-domain hours. It also adds:
   - migration verified against A07 per customer
   - a release diff run in production as a shadow job
   - a B28 sign-off on every release
   - TT02 end-to-end tests with Tenor twins
   - property-based and mutation tests

   About 350–450 of those hours can be bought externally.
7. **Decided in PLAN.md (D1, new B44):** the current system submits all of income year 2026. Brutto shadow-runs November and December 2026 and is system of record from period 2027-01 (stretch) or 2027-02 (planning date), and 2027-03 at the latest, see §1.2. So Brutto needs no 2026 year-to-date import and produces no 2026 sammenstillingsoppgave (annual statement of pay and tax per employee, D-27). The a-melding is one format-neutral aggregate. It is serialised to JSON, per Skatteetaten's Q&A of 18.06.2026, and uploaded manually (F-MYN-14) [verify the format by 27.11.2026]. An XML 2.3 serialiser of the same aggregate is a costed fallback (+1–2 developer-weeks) in case 2027 manual upload takes XML (N14 §3).

---

## 1. Principles and M0 timeline

### 1.1 Where each known error source is caught

| Error source (R3 b.0 and the domain critic) | When it strikes | M0 control | M1 control |
|---|---|---|---|
| Migrated balances (year-to-date figures, feriepengegrunnlag (holiday-pay basis), withholding) | First run, June, January | M0-27: the employment fields equal the current system, diff 0. No general 2026 year-to-date import (D1). Year-to-date figures only if go-live is after January (the 2027 months run in the old system, checked against A07). The 2026 holiday-pay basis is imported on the M0+ track by gate JUN27 (F-MIG-22, M0-20) | Port M per customer (§3.1), M1-31 |
| Union dues treated as purely after tax (research report C #48 is wrong) | Every run, if dues go through payroll | M0-31: the withholding base is reduced by the dues deducted, rounded up to whole kroner (skattebetalingsforskriften § 5-9-1), and the dues are taken from net | M1-21 adds the annual cap and carry-forward |
| Pay-type flags and mapping from the old system | First run | Pay-type set signed by Sjur, M0-30 blocks unsigned flags | Quarantine (M1-34, GC-21), flag combinations validated against the a-melding code list |
| Variable pay in arrears across the switch | First month after the switch | Not in M0: the switch is at the year boundary (D1) with fixed pay only | M1-32 (GC-02) |
| Ongoing sick leave across the switch | First month | Not in M0. The M0 employer (D2) records no AGP (arbeidsgiverperiode, the 16-day employer-paid sick period) in Brutto during M0 | M1-19 (GC-01) |
| Garnishments registered by hand | Every run | None expected in M0 | Four-eyes entry check, M1-23 |
| December (half withholding) | December | Second shadow period (M0-S2), M0-10. M0-33 (hourly employee) before gate DEC27, 15.11.2027 | Historical December shadow per customer |
| June (holiday pay, trekkfritak) | June | Historical shadow of June 2026 and M0-32 (60+ supplement) by gate JUN27, 14.5.2027 (§2.9) | June gate per customer (§3.6), M1-11–14 |
| Year switch (new tax card, new trekkrutine, F532 from 2027-01) | January | M0-28–30, conformance run on the 2027 file | Same, every year |
| Tax card entered by hand | Every run while there is no tax-card API | Cards ordered through Skatteetaten's tax-card file service (RF-1211 via ID-porten; needs the Altinn package "Lønn") or copied from the current system while it still fetches them. Entered with four eyes and re-checked before every run and for every new hire (PLAN.md §1.4) | Tax-card API with all result codes (§3.3) |

### 1.2 M0 timeline, and who is master

Fixed dates:
- 17.11.2026: Altinn II roles stop working for a-melding and tax cards. Brutto submits no 2026 period (D1), but the current system submits 2026-11 and 2026-12. Confirm this week that its submission channel still works after this date (PLAN.md §1.1).
- 7.12.2026: deadline for the November a-melding (submitted by the current system).
- 15.12.2026: tax cards can then only be fetched by polling.
- Early December 2026: trekkrutine 2027 is expected (N13 §1.11).
- 2027-01: F532 and F530 take effect. Manual a-melding upload goes from XML to JSON after 2026 (Skatteetaten's Q&A of 18.06.2026, N14). The format for 2027 periods is a [verify] item in the letter to Skatteetaten, to be settled by 27.11.2026 (M0-α). The XML 2.3 serialiser is the costed fallback.
- 5.2.2027: deadline for period 2027-01, Brutto's first live a-melding if the stretch date holds. At the planning date (2027-02) the first deadline is 5.3.2027. The uploader must hold the Altinn 3 package "A-ordningen" before then.

| Option | What Brutto submits | Extra correctness burden |
|---|---|---|
| **A (adopted in PLAN.md as D1, new B44): the current system submits all of 2026. Brutto shadow-runs November and December 2026 and is system of record from 2027-01 (stretch) or 2027-02 (planning date)** | Nothing in 2026. The first real a-melding is January 2027 if the stretch holds (deadline Fri 5.2.2027). At the planning date it is February (deadline Fri 5.3.2027), and March at the latest | 2027 rule pack and conformance on the 2027 file before the first live run. The manual-upload format for 2027 is confirmed by 27.11.2026 (letter to Skatteetaten; otherwise the XML 2.3 fallback), and a synthetic twin is accepted in the test upload before M0-L |
| B (not pursued): Brutto is master from November 2026 if the parallel run is equal to the øre | November (XML) and maybe December | Opening balances for Jan–Oct 2026 must be exact for the sammenstillingsoppgave 2026 (D-27). The December upload in January may need JSON. A mistake in a submitted month needs a full replacement message |

PLAN.md §8 rewords B19 to match Option A. Brutto computes each shadow month in full, and the comparison with the current system proves it. Option B is kept here only to show what D1 avoids: a 2026 year-to-date import, a 2026 sammenstillingsoppgave from Brutto, and two systems in one income year.

---

## 2. M0 – test strategy for the first payroll (own company, ≤ 10 employees)

### 2.1 Golden-case suite

**Format.** One TOML file per case under `golden/<income-year>/`.

Inputs:
- the company: opplysningspliktig (the reporting legal entity) and its sub-unit with AGA zone (AGA = arbeidsgiveravgift, the employer's social-security contribution)
- persons with synthetic IDs
- employment versions with valid-from dates
- salary agreement and tax card
- variable lines
- pay period and payout date
- rule-pack id

Expected outputs:
- payslip lines (pay type, quantity, rate, amount)
- trekkgrunnlag (withholding basis) for table and for percentage
- forskuddstrekk (PAYE withholding) per payout date
- AGA basis per zone and type, and AGA amount
- holiday-pay accrual
- net pay
- voucher lines per account and dimension
- payment-file totals
- a-melding fragment as normalised JSON (inntekt, fradrag, forskuddstrekk, arbeidsgiveravgift)

Each case also carries metadata: `source` (C §12 #n, GC-n, N13 vector, Skatteetaten, external), `signed_by`, `signed_at`, `countersigned_by` and `uncertain` (list of [U] items).

**Rules:**
1. Expected money values are written by hand from the rule, or taken from an external oracle, **before** the code exists. Approval snapshots (`insta`) are allowed only for layout fields, never for amounts.
2. CODEOWNERS: `golden/**`, `rules/**` and `amelding/mapping/**` need approval from the payroll-domain owner. Commits from agents are labelled (D-48).
3. CI runs every case for every income year on every PR. A red case blocks the merge. A case for a closed year is never edited. A later fix becomes a new correction case (F §7.1).
4. In the parallel run, every B-category deviation (a Brutto bug) becomes a new golden case before the fix is merged (F-MIG-31).
5. Golden files contain only synthetic data, with identity guards (N39 §7): fnr-shaped numbers fail the build (F-SIK-36).
6. **Second derivation in M0:** a developer recomputes the 10 highest-risk cases independently in a spreadsheet. This catches arithmetic slips but is not domain sign-off. The cases are M0-04, 05, 08, 10, 15, 16, 18, 20, 24 and 29.

### 2.2 Withholding-table conformance (F-TRK-07, L01, N13)

| Check | Pass criterion | Tier |
|---|---|---|
| Own Rust port of the 2026 algorithm in the isolated crate `brutto-trekkrutine`, in `f64` with the Java operation order. No `mul_add`, no fast-math | – | M0 |
| **Full text file 2026** ("alle tabellene i en fil", about 1.06 million rows, all 96 tables, all 7 periods). A human downloads it, and it is stored with its SHA-256 | **100 %** of rows equal. Runs in CI on every change to the crate and nightly | M0 |
| Vectors above table max (N13 §1.5, for example 8000, month, 250 000 → 120 593) | 100 % | M0 |
| Property tests from Skatteetaten's `TrekkrutineTest`: withholding ≤ basis, more deduction gives less withholding, at most one 0-row per table, no trygdeavgift (national-insurance contribution) for "Ingen" tables, thresholds 125 188 and 143 175 | 0 violations | M0 |
| Basis handling: truncate øre (`ToZero`) before the call, negative basis becomes 0, interval 100/50/20 and midpoint | Unit tests at the boundaries (M0-02) | M0 |
| **2027 file and algorithm** when the 2027 branch is published (expected early December 2026). The year is chosen from the payout date | 100 % before the January 2027 run | M0 (gate M0-L) |
| Watch the GitHub branch, the file's `Last-Modified` and SHA-256 (F-MYN-24). A new file triggers a re-run | Alert | M0, manual weekly check in December |
| Spot checks against Skatteetaten's search service | 5 values per table family, by hand | M0 |
| Licence | Own implementation from the rule. Java is used only as a reference. The text file is published "for testing payroll systems". A human asks Skatteetaten for a written licence. This does not block M0 | M0 action |

The licence question (F-TRK-07) does not block M0 as long as Brutto writes its own port and tests it against the text file.

### 2.3 A-melding validation (the monthly payroll report to the a-ordning)

| Layer | What | Pass criterion | Tier |
|---|---|---|---|
| 1. Schema | Brutto's JSON (the payload the a-melding API takes, also used for manual upload, F-MYN-14) validated against the OpenAPI/JSON schema in CI (N14 §3). An XML 2.3 serialiser of the same aggregate, with XSD validation by `xmllint` in CI (N08 §7), is the costed fallback (+1–2 developer-weeks) if 2027 manual upload takes XML. The format is settled by 27.11.2026 (M0-α) | 0 errors | M0 |
| 2. Local business rules (F-MYN-10, M0 subset) | Sum of forskuddstrekk per lønnsutbetalingsdato (payout date) as an integer (F173-2/F277-2). AGA sum = Σ basis × rate (F185). Required fields (yrke (occupation code) F503, stillingsprosent (position %), dates). Valid inntektsbeskrivelse/fordel combinations from the code list. `pensjonsinnretning` (pension provider) present when the employer has OTP (B §8.2). F529. From 2027-01: F532, a negative sum per date is blocked | 0 rejections, 0 "øyeblikkelig" (findings that must be fixed at once). Guideline findings acknowledged | M0 (rules imported as data from Skatteetaten's rule spreadsheet, N36) |
| 3. Test portal | A **synthetic twin** of the M0 a-melding, in the format confirmed for 2027 periods: the same structure, with a Tenor company and Tenor persons (N39 TV-7). A human uploads it with TestID at `ameldingfilopplasting.skatteetaten-test.no` and reads the tilbakemelding (A03, the feedback on a submitted a-melding). **Real data never goes to test** | Accepted, 0 rejections, 0 "øyeblikkelig" | M0 (by M0-L, 15.1.2027) |
| 4. Parallel diff | Semantic diff between Brutto's message and the old system's message for the same month, per arbeidsforhold (employment) and inntektsbeskrivelse (income description). `kildesystem` and message ids are ignored | 0 differences (M0-26) | M0 |
| 5. Hash lock | The file that is uploaded has the hash recorded at approval (B41; re-authentication through the identity provider in M0, BankID from M1). Changing anything after approval needs a new approval | Test: an edit after approval is refused | M0 |
| 6. After a real submission (only from the first live period, when Brutto is system of record) | Upload on payday. A03 read in Altinn by hand, and the forskuddstrekk KID taken from it for the separate withholding payment (PLAN.md §1.4 item 3). A07 for the month downloaded by hand ("Avstemmingsinformasjon" portal) until the API exists | 0 rejections. The withholding payment uses the KID from A03. A07 equals Brutto's aggregate, diff 0 | M0 |

**Operational check:** the person who uploads needs the Altinn 3 access package "A-ordningen" for the M0 employer. Confirm it before the first live upload (period 2027-01, deadline 5.2.2027, or 2027-02, deadline 5.3.2027). Ordering tax cards through the file service needs the package "Lønn"; "A-ordningen" does not cover tax cards. The 17.11.2026 stop for Altinn II roles matters for the current system, which submits 2026-11 and 2026-12 (§1.2).

### 2.4 Parallel-run protocol, "equal to the øre" (F-MIG-31, F-MIG-32, F §6.4–6.5, B16)

PLAN.md calls the M0 parallel periods shadow runs: shadow #1 (November 2026, gate M0-S1, 18.12.2026, latest 31.12.2026; if it slips past that, go-live moves to 2027-02 automatically) and shadow #2 (December 2026, gate M0-S2, 15.1.2027). Under D1 the current system pays, posts and submits both months. The P-relative timings below apply where the shadow runs ahead of pay day; a shadow computed after pay day uses the same frozen inputs.

| Step | When | Content | Signs |
|---|---|---|---|
| 1. Opening balances | Before shadow #1 | Import master data, employment IDs with all a-melding fields and change dates, ongoing leave and permittering with their leave IDs, fixed lines and pension setup from the current system (PLAN.md §1.3). The 2026 feriepengegrunnlag (paid out in June 2027) and the 2025 basis for the June 2026 historic shadow are exported now and imported on the M0+ track by gate JUN27 (F-MIG-22, M0-20). No general 2026 year-to-date import (D1): the exported 2026 year-to-date figures and A07 for 2026-01..10, downloaded by hand, are reference data only (M0-27) | Sjur, plus 1 developer |
| 2. Tax cards | Before cut-off | Ordered through Skatteetaten's tax-card file service (RF-1211 via ID-porten, package "Lønn") or copied from the current system. Person 1 enters them. Person 2 checks against the source and the old system's card data: table, %, number of withholding months, frikort (tax-free card) amount. Re-checked before every run and for every new hire | Two persons |
| 3. Historical shadow | Before shadow #1 | Recompute **October 2026** (and September if time allows) from the old system's inputs. Compare line by line | Sjur |
| 4. Input freeze | P−3 working days | The same input list goes into both systems. Brutto records the input-snapshot hash (B6, D-38) | Developer |
| 5. Compute and compare | P−2 | The comparison tool produces a diff per employee × checkpoint (table below) | Tool |
| 6. Classify | P−2 to P−1 | Every deviation gets a class: A migration error (fix the data), B Brutto bug (fix plus a new golden case plus re-run), C error in the old system (document it), D accepted convention from a list signed **in advance** (for example the AGA rounding rule) | Sjur |
| 7. Single payer, single report, single posting | P | Only the master system's pain.001 file goes to the bank, only one voucher is posted, and only one a-melding is submitted. Brutto's file is clearly marked PARALLEL and is never uploaded while the old system is master | Sjur |
| 8. Protocol | P+1 to P+5 | Signed acceptance protocol: checkpoints and deviations by class. It is input to the M0-L decision (under D1 the current system submits both months) | Sjur, plus 1 developer |
| 9. Repeat for December | December P | Second parallel period. Covers half withholding and holiday due dates | As above |

**Checkpoints:** 100 % of employees, no samples. The tolerance is 0.00 unless a class-D convention is documented.

| Checkpoint | Tolerance |
|---|---|
| Net paid per employee | 0.00 |
| Forskuddstrekk per employee and per payout date | 0 kr |
| Trekkgrunnlag (table and percentage) per employee | 0.00 |
| AGA basis per zone and type (salary, pension premium) | 0.00 |
| AGA amount per opplysningspliktig | 0 kr, or class D if the old system rounds to the nearest krone |
| Feriepengegrunnlag and accrual per employee | 0.00 |
| OTP basis per employee | 0.00 |
| Sum per mapped pay type | 0.00 |
| A-melding per arbeidsforhold and inntektsbeskrivelse, including arbeidsforholdId and the dates of the last salary change and last change in position % | Identical |
| Voucher: debit = credit, sum per account and dimension | 0.00 (a mapping difference is class D) |
| Payment file: sum and number of recipients | 0.00 / identical |
| Holiday-pay basis year-to-date against the current system (year-to-date against A07 applies from 2027-01, §2.3 layer 6) | 0.00 |

**Privacy:** the parallel run uses real data. It runs only in the production environment. The diff report stays there and is never pasted into the repo, issues or agent prompts (D-48, F-SIK-36).

### 2.5 Payslip legal-content check (F-KJO-42)

The payslip is rendered from a structured `PayslipDoc`. An automated test checks every element below on every M0 golden case. Sjur reviews a rendered sample (an `insta` text snapshot) each time the template changes.

| Element | Legal source |
|---|---|
| How the pay was computed: each line with pay type, quantity, rate and amount | aml. § 14-15 sixth paragraph |
| Basis for holiday pay, **feriepengegrunnlag year-to-date** | aml. § 14-15 sixth paragraph, D-31 |
| Deductions made: forskuddstrekk, utleggstrekk (garnishment), other deductions | aml. § 14-15 sixth paragraph |
| Table number or withholding %, trekkperiode (withholding period), bruttolønn (gross pay), withholding basis with deductions itemised | skattebetalingsforskriften § 5-10-20 (N13), bokføringsforskriften § 5-6 |
| Payout date, gross, benefits in kind, deductions, withholding basis, withholding | bokføringsforskriften § 5-6 (per period) |
| For hourly employees: hours per day and total (payslip appendix or payroll journal) | bokføringsforskriften § 5-6 |
| Year-to-date figures, masked account number, employer name and orgnr | F-KJO-42 |
| A correction gives a new payslip showing what changed. The old one is kept | F-KJO-42 |

PDF/A validation with veraPDF is M1. In M0 a plain PDF is enough.

### 2.6 Money arithmetic and rounding (D05, N08 §3, N13 §2, F §1.10, F-KJO-17)

**Types and bans:**
- `Money` = `rust_decimal::Decimal`, scale 2, in the domain. `NUMERIC(14,2)` in Postgres (sqlx `rust_decimal`). In the API JSON, amounts are **strings** (`rust_decimal::serde::str`), because JSON numbers pass through f64 (N08 §3).
- `WholeKroner(i64)` for every `BeloepSomHeltall` field: forskuddstrekk, utleggstrekk, AGA payable. Its constructor rejects fractions.
- `Rate` = `Decimal` for percentages, which may have decimals (§ 5-2-2). Hourly rates and pro-rata fractions are **not rounded**. Only the resulting line amount is rounded.
- `clippy.toml` bans `Decimal::round`, `Decimal::round_dp` (banker's rounding) and `from_f64_retain`. `clippy::float_arithmetic` is denied in every crate **except** `brutto-trekkrutine`.
- External amounts are parsed with `Decimal::from_str_exact`. Too many decimals is an error, never silent rounding.
- Rounding happens only through `brutto_penger::round(value, rule)`, with the rule taken from the rule pack (key, strategy, level, direction for negatives, legal source, valid-from). A run stores the hash of its rule pack.

**Rounding per element** (default policy until verified):

| Element | Rule | Source |
|---|---|---|
| Payslip line amounts (pro rata, hourly, overtime, allowances) | Øre, `MidpointAwayFromZero`. Net = Σ rounded lines | F §1.10, F-KJO-17 |
| Basis into the trekkrutine | Truncate to whole kroner (`ToZero`), then interval and midpoint inside the crate | N13 §2 |
| Table withholding | Nearest krone, half up, in `f64` (Java `Math.round`). Sea tables round down (later) | N13 §1.2 |
| Derived table withholding (half, ×2, ×3, ×n) | Down to whole kroner (`ToZero`) after the operation. Half withholding = ⌊t/2⌋ | § 5-5-4, N13 §1.8 |
| Percentage withholding | ⌊⌊basis⌋ × p / 100⌋ | §§ 5-10-4, 5-5-4 |
| Union dues used as a deduction in the basis | Up to whole kroner (`AwayFromZero`) | § 5-9-1 |
| Forskuddstrekk in the a-melding | Integer per recipient, sum per payout date | XSD 2.3, F173-2/F277-2 |
| AGA basis | Not rounded (decimal) | XSD 2.3 |
| AGA payable | Σ(basis × rate) exact per opplysningspliktig and month, rounded **once**. Default `ToZero` (§ 10-4-4) until a TT02 test shows what F185 accepts [U] | N13 §2, backlog 2 |
| Holiday pay | Øre per employee and payout, `MidpointAwayFromZero`. Partial payouts are computed cumulatively (paid so far is subtracted) | F §1.10, N13 §2 [U] |
| Utleggstrekk | Down to whole kroner [U] | N13 §2, N28 |
| `inntekt.beloep` and `fradrag.beloep` | 2 decimals (F280) | N13 §2 |
| Allocation to dimensions and accounts (AGA, holiday pay, OTP) | Largest remainder. Invariant: Σ parts = total | F §1.10, F-KJO-13 |
| Negative amounts (reversals) | Round the magnitude, then put the sign back, so a reversal is exactly −original [U] | N13 §2 |
| Payment file | Exact øre, no øre rounding | F §1.10 |

### 2.7 Minimal invariants and controls in M0

Five `proptest` invariants with 10,000 generated cases each. They are cheap and catch most agent-written regressions:
1. **Determinism:** the same input snapshot and rule pack give byte-identical output, also with input lists shuffled (L02: the engine is a pure function).
2. **Net balances:** net = Σ earnings + tax-free allowances − pension contribution − withholding − deductions, and net ≥ 0.
3. **Withholding cap:** withholding ≤ the cash available at each payout date.
4. **Voucher balances:** Σ debit = Σ credit, and Σ allocated parts = total.
5. **Report equals payslip:** Σ a-melding amounts per inntektsbeskrivelse = Σ mapped payslip lines.

Controls:
- No deployment between approval of a run and the a-melding upload. If one is unavoidable, the approved run is recomputed in shadow and must give diff 0 (an early form of the release diff).

### 2.8 Test harness cost (developers, rough)

| Item | Days |
|---|---|
| Golden runner and TOML format, with diff output | 3–4 |
| Trekkrutine port and full-file CI test | 3–5 |
| Schema validation in CI (JSON schema; XSD only if an XML serialiser is built) | 1 |
| Parallel-run comparison tool (old system's CSV/XML against Brutto) | 2–3 |
| Property tests | 2 |
| Payslip element check | 1 |
| **Total** | **≈ 12–16 days** |

### 2.9 M0 gates and the M0+ track (PLAN.md §3, §1.6; B26 re-dated)

| Gate | Date | Thresholds |
|---|---|---|
| M0-α engine spike | 27.11.2026 | 100 % on the 2026 text file. The first 20 of the 30 M0 cases signed by Sjur and green in CI, including AGA by zone and holiday-pay accrual, drawn from M0-01–19 and M0-21–25. A case with an open [U] item can only be signed once the item is resolved: 17 of those 24 cases have none, so resolve [U] items early or add M0-20, M0-27 or M0-30. If union dues go through payroll, M0-31 is among the first 20 (union dues in the base are built in weeks 3–4). Schema validation in CI. Upload format confirmed, or the XML 2.3 fallback started |
| M0-S1 shadow #1 (November 2026) | 18.12.2026 / latest 31.12.2026 | Steps 1–8 of §2.4 complete, 0 unexplained deviations, protocol signed. The a-melding validates and matches the submitted message on mapped fields (M0-26). If S1 slips past 31.12.2026, go-live moves to 2027-02 automatically |
| M0-S2 shadow #2 (December 2026) | 15.1.2027 | As S1, plus half withholding correct per line (M0-10). pain.001 passes the bank's validation, without signing (M0-23). Voucher file balances and matches the current system per account (M0-22) |
| **M0-L Brutto live (system of record)** | Decision 15.1.2027 for period 2027-01 (stretch, about 40 %). Planning date 2027-02 (about 65 %); 2027-03 at the latest | S1 and S2 clean. 100 % on the 2027 text file. 2027 rule pack signed by Sjur and a developer (F-KJO-18). 2027 tax cards registered with four eyes. All 30 M0 cases signed and green (incl. M0-28–30), plus M0-31 if dues go through payroll. A synthetic twin of the M0 a-melding (Tenor company, TestID) accepted in Skatteetaten's test upload, in the format confirmed for 2027 periods; real data never goes to test. The forskuddstrekk KID routine (KID from the a-melding feedback) written and rehearsed. Uploader holds "A-ordningen". System description signed (F-SIK-29). Rollback runbook ready. The current system's records archived (5 years after each year-end); it stays licensed for at least 12 months |
| MP Maskinporten live (own company) | 31.3.2027 (best case 29.1.2027) | Synthetic test a-meldinger in TT02 with 0 rejections. First production A07 fetch. Tax-card API works. Otherwise stay on manual upload |
| **JUN27** own payroll: first June | Gate 14.5.2027 | Holiday-pay payout and ferietrekk built. Shadow of **June 2026** in Brutto with the 2025 basis from the current system: equal to the øre, or each difference explained and signed. 2026 holiday-pay basis imported (F-MIG-22) and equal per person. The whole payout reported as feriepenger, with the June exemption (§ 5-7-1). **M0-32 green:** the 60+ supplement for employees turning 60 in 2027, with the base capped at 6 G using the G in force on 31.12.2026 (ferieloven § 10 (3)). June 2027 is the first June the M0 employer pays from Brutto. If no-go: pay June holiday pay in Brutto as manual lines signed by Sjur, never in a second system |
| 24-S a-melding 2.4 mapped | Spec by 1.5.2027, mapping by 1.7.2027 | The aggregate serialises to both 2.3 and 2.4. Semantic diff 0 on shared fields |
| 24-T 2.4 in test | 15.9.2027 → 1.12.2027 | Our own company, and synthetic twins of every pilot, accepted in the 2.4 test environment |
| **DEC27** own payroll: first live December | Gate 15.11.2027; 2028 rule pack and table file by 22.12.2027 | Half withholding correct per line, including **M0-33** (hourly employee: two weeks exempt, § 5-7-2). On-call staffed 27.12.2027–14.1.2028 |
| **AS27** own annual statement 2027 | 14.1.2028 (legal deadline 31.1.2028) | The 2027 sammenstillingsoppgave (F-MYN-36), including the holiday-pay base, produced by Brutto for the whole year. Year-to-date diff 0 against A07 per employee. If no-go: produce it by hand from A07 |

---

## 3. M1 additions (first external pilots)

### 3.1 Migration verified against A07 (Port M per customer; F-MIG-16, F-MIG-21; D-17, D-18)

| Check | Criterion |
|---|---|
| Year-to-date per employee × inntektsbeskrivelse × month, against A07 for every month before cut-over (A07 via API by then) | Diff 0. A difference **blocks** the first ordinary run (C §4.2) |
| arbeidsforholdId, permisjonsId (leave id), start date, type, dates of the last salary change and the last change in position % | 100 % preserved. The number of employments per employee and sub-unit is unchanged. The first message contains every active employment and leave |
| Previous year's feriepengegrunnlag per employee (A07 has no basis field) | Equal to the old system, diff 0. Plausibility check: Σ holiday-pay-qualifying A07 lines for the previous year ≈ the basis, with differences explained |
| AGA basis per zone so far this year, and the fribeløp (exemption amount) used in zone Ia | Equal to A07 (pilots in Ia are excluded) |
| Open garnishments: KID, balance, code (samordnet or skatt) | Entered and checked by two persons (D-23) |
| Ongoing AGP, self-certified sick days in the last 12 months, income for the last 3 months for hourly staff | Imported, and checked against GC-01/GC-20 |
| Parallel periods | Direct customers: 2 periods equal to the øre (gate P-PAR). Byrå clients (**M2**): 1 period plus a historical June shadow (EM.9). Signed protocol per customer (in M2, also the byrå) |
| Old system | Kept for at least 3 months for corrections of earlier periods (D-20, written into the pilot agreement) |

### 3.2 Release diff and payroll-domain sign-off (F-SIK-35, B28, D-51)

- **Every release that touches calculation, reporting or mapping:**
  1. All golden cases for all years are green.
  2. A **shadow recompute in production** runs as an approved job. It takes the stored input snapshot of every run in the previous month, for all tenants, plus a year-wheel set (the latest June and the latest December). It uses **the rule pack each run used**, so any difference can only come from code.
  3. The job compares payslip lines, the a-melding contribution and voucher lines. It logs counts and run ids only.
  4. An unexplained difference stops the rollout. Explained differences are listed in the release notes and signed.
- **"Anonymised snapshots" are not M1.** Copying production data into test, even anonymised, conflicts with F-SIK-36 and S §2 pkt. 10 and would need a DPIA (data protection impact assessment). The in-production shadow over stored snapshots gives the same coverage without data leaving production. Anonymised sandbox copies are LATER, with a DPIA.
- **B28 sign-off:** a named payroll-domain owner (Sjur) and a named **deputy** approve:
  - the PR (CODEOWNERS)
  - the release-diff report
  - every rule-pack release (two-person rule with a developer, F-KJO-18)

  The signed release record is stored as future ISAE evidence. Without a deputy, no release that changes calculation goes out while the owner is away.
- **B24 calculation guarantee** (downgraded to after M1, PLAN.md §8): do not offer it to pilots until the M1 gate is met. Its credibility rests on this evidence: signed golden cases, release-diff logs and parallel-run protocols. Wording: "we cover", not "we correct" (D-35).

### 3.3 TT02 end-to-end tests (TT02 = the Altinn and Skatteetaten test environment; replaces the missing N22)

Test layers (N39 §7):
- **L1:** every PR, no network. Replays recorded TT02 responses.
- **L2:** nightly. Contract smoke test against TT02. Never blocks a release.
- **L3:** weekly, and before each pilot.

| Scenario (N39 S-ids) | Criterion |
|---|---|
| Maskinporten token, system user, tax-card fetch for test persons, every `resultatForSkattekort` value incl. `registrertSomDoed` | All handled |
| a-melding REST submission with `idempotencyKey`, retry, `AMLD_019` | Accepted. A resend gives the same receipt |
| S01–S03, S05, S07–S09, S11, S12 (fixed pay, joiner, leaver with holiday pay, leave, zones, benefits, holiday pay, union dues, replacement) | 0 rejections, 0 "øyeblikkelig". A03 read |
| Closed loop: Brutto run → submit → A07 → diff | Diff 0 for every scenario |
| Two payout dates, extra run, F532 stopped locally (M1-05–07) | As in the cases |
| Manual-upload fallback (JSON in 2027 [U], to be confirmed in the letter to Skatteetaten) in the test portal | Accepted |
| Garnishment (S10): order test data from Skatteetaten now (long lead time, D-52), even though garnishments are entered by hand in MVP | Test KID works |

### 3.4 Tenor synthetic persons and test data (F-SIK-36, N39)

- A **synthetic twin** of each pilot customer: Tenor company (orgnr starting 2 or 3), the same number of sub-units and zones, the same pay-type set, persons with test tax cards. Used in L3 and as the pilot's pre-go-live rehearsal.
- Identity guards: test tenants accept only Tenor patterns. CI fails on any fnr-shaped number with a valid checksum.
- Tenor-API is never called from L1 or L2. Selected data is frozen in `testdata/tenor/`.
- NAV (Dolly) is used only when the NAV integration starts. K27 import (NAV's refund settlement report, F-MYN-34) is LATER: in M1 the refund is entered by hand, so there are no K27 fixtures. When the import comes, it is tested with CSV fixtures (ISO-8859-1).

### 3.5 Property-based and mutation tests

**Ten invariants, 10,000 cases each, 0 violations.** The five from M0, plus:
6. Monotonicity within a table: higher basis never gives lower withholding.
7. Deduction queue: net after deductions under § 14-15 (c), (e) and (f) is ≥ the protected amount, and no deduction is ever negative.
8. Correction equivalence: original + correction gives the same economic end result as a recompute with the corrected facts.
9. Split month: two runs in a month give the same monthly table withholding as one run (accumulated basis minus withholding already taken).
10. Registration time: changing the registration time without changing the validity gives an identical result. (Tenant invariance, where the same case run in a byrå tenant gives identical output, moves to **M2**.)

**Mutation testing** (`cargo-mutants`) runs on four modules: withholding, AGA, holiday pay and the deduction queue. Score ≥ 80 %, with surviving mutants reviewed by Sjur. This is the main defence against code from agents that looks right but is wrong in payroll terms.

### 3.6 Gates for the dangerous months

| Month | M1 gate |
|---|---|
| December | Historical shadow of the customer's last December before go-live, or the live December parallel run |
| January | 100 % on the next year's text file. New rule pack signed. Time-travel run of every synthetic twin from December into January |
| June | Gate JUN28 for pilots, 2.5.2028 (stretch case only, when pilots go live 2028-01): shadow of last June with the migrated basis. Sjur checks 10 % of employees by hand, 0 unexplained deviations. M1-11–14 green |

### 3.7 Coverage matrix (replaces the "300 cases" count)

Axes:
- pay form: monthly, hourly, honorarium
- tax card: table 10.5 months, table 12 months, percentage, frikort, none
- month: normal, June, November/December, January
- absence: none, sick within AGP, sick with refund, parental leave
- deduction: none, union dues, utleggstrekk, agreed deduction
- event: none, joiner, leaver
- zones in use

Not a full Cartesian product. Every cell relevant to the pilot profile needs ≥ 2 cases, and ≥ 5 for cells that touch withholding, AGA or holiday pay. Cells for pilot-pulled items (honorarium and board fees, travel allowances as pre-split lines, small association fees, PAYE cards, a department and project code; PLAN.md §6.1) are filled only for items pulled at G4 (31.3.2027). Target at the M1 gate: **about 150 signed cases**. These are the named cases below plus parametrised variants. 20 % are countersigned by an external payroll expert.

### 3.8 M1 gate (summary; M1-FC in PLAN.md §3: 31.3.2028 plan / 1.9.2027 stretch, which needs two more developers signed by 18.12.2026)

| Area | Threshold |
|---|---|
| Golden cases | All green, about 150 in the coverage matrix, 20 % countersigned externally |
| End to end | A full month for two synthetic customers. BankID login. Pentest with no high or critical findings (PLAN.md §3) |
| Trekkrutine | 100 % for the current year and for the next year (once published) |
| Property and mutation tests | 10 invariants with 0 violations. Mutation score ≥ 80 % on the four modules |
| TT02 | a-melding accepted for at least 5 test companies (synthetic twins) with 0 rejections and 0 "øyeblikkelig". A07 closed loop diff 0. 2.4 follows at gate 24-T |
| Process | B28 owner and deputy named, release diff live |
| Per customer | Port M (§3.1) signed |

---

## 4. Golden cases

**Who signs:**
- **S** = Sjur, the payroll-domain owner (B28).
- **X** = external payroll expert countersigns. Mandatory for every [U] case.
- **O** = machine oracle: Skatteetaten's file or trekkrutine. Sjur signs the oracle version and hash, not each value.
- **P** = old-system or A07 reference from the parallel run or migration. Sjur signs the classification.
- **C** = the customer's payroll lead (M1 migration and parallel cases).
- **SKE** = needs a written answer from Skatteetaten first.

Unless stated otherwise: November 2026, sub-unit in zone I (14.1 %), holiday pay 12 %, table 8000 with 10.5 months.

### 4.1 M0 – 30 cases plus three dated cases (own payroll)

M0-01–30 are signed and green by M0-L (the first 20 by M0-α). M0-31 is required at M0-L only if an employee pays union dues through payroll. M0-32 is required by gate JUN27 (14.5.2027) and M0-33 by gate DEC27 (15.11.2027), on the M0+ track (PLAN.md §1.6).

| Id | Case | Expected logic (one line) | Source | Signs |
|---|---|---|---|---|
| M0-01 | Monthly salary, table 8000, monthly period, zone I, no absence | 50 000 → withholding 14 184. Net, AGA and accrual follow | N13 §1.5 | O + S |
| M0-02 | Table interval boundaries and øre in the basis | 50 000 / 50 099 / 50 100 → 14 184 / 14 184 / 14 222. 50 099.99 is truncated to 50 099 | N13 §1.5, §2 | O + S |
| M0-03 | Addition table (9xxx), monthly | Equals the oracle. Proves that table families are selected correctly | N13 §1.3 | O + S |
| M0-04 | Percentage card 30 % with OTP | Withholding 15 000, net 35 000, holiday-pay accrual 6 000, AGA 14.1 % × 51 000 = 7 191.00 | C #1 | S |
| M0-05 | Percentage with decimals and øre in the basis | 43 210.75 at 27.5 % → ⌊43 210 × 0.275⌋ = 11 882 | §§ 5-10-4, 5-5-4 | S + X |
| M0-06 | Salary above table max | 250 000 on 8000 → 120 593, computed rather than looked up | N13 §1.5 | O |
| M0-07 | No tax card | 50 % of cash pay, logged, warning on the payslip, no December halving | C §2.2, N13 §1.10 | S + X [U legal basis] |
| M0-08 | Frikort exceeded | Limit 100 000, 95 000 used, 10 000 paid → 5 000 free, 2 500 withheld. Holiday pay counts against the limit | C #3, F-TRK-10 | S + X [U 50 %] |
| M0-09 | Bonus paid together with the monthly salary on a table card | Salary withheld by table, bonus by the card's percentage (trekkmetode flag per pay type) | § 5-10-1 fourth para., D-02 | S |
| M0-10 | **December half withholding** | 50 000 on 8000 → ⌊14 184/2⌋ = 7 092. Bonus at full percentage. 12-month card and percentage card not halved | C #24, N13 §1.8 | S + X [U percentage card, § 5-7-2 fourth para.] |
| M0-11 | Withholding capped at the cash amount | Taxable benefit with low cash pay: withholding ≤ cash, "missing withholding" warning, AGA on the full basis | C #19 (no car) | S |
| M0-12 | Hourly employee | Daily hour lines × rate. Table on the periodic hourly pay. Hours per day stored. Hours reported in the a-melding [U antall rule] | C §2.2, bokføringsforskriften § 5-6 | S |
| M0-13 | Fixed allowance plus monthly salary | Both in the table basis, holiday-pay basis and AGA. Separate payslip lines | C §1 | S |
| M0-14 | Taxable benefit (health insurance or EK, if the M0 employer has one) | In the withholding and AGA basis. Not in net or holiday-pay basis. Benefit line in the a-melding, posted 5280 against 5290 | N13 §3.2, S §6 pkt. 27 | S |
| M0-15 | AGA in the company's own zone, and its rounding | Σ(basis × rate) exact, rounded once. 100 003.55 × 14.1 % = 14 100.50055 → 14 100 (`ToZero`) or 14 101 (nearest). The chosen rule is documented | N13 §2, F-KJO-13 | S + X [U F185] |
| M0-16 | AGA on the OTP premium from the invoice | The monthly premium entered becomes the `tilskuddOgPremieTilPensjon` basis, separate from salary. `pensjonsinnretning` is reported | D-01, GC-17, B §8.2 | S + X [U timing, admin cost] |
| M0-17 | Zone-rate table | Parametrised zones I, II, III, IV, IVa, V give the C §0.1 rates (Ia excluded) | C §0.1 | O (rule pack) + S |
| M0-18 | Monthly holiday-pay accrual | 12 % × 50 000 = 6 000.00 (5020/2940). AGA 846.00 (5405/2785). Not in net or the a-melding | C #1, F-KJO-14 | S |
| M0-19 | What goes into feriepengegrunnlag | In: salary, hourly pay, allowance, bonus. Out: benefits (except kost), expense allowances, styrehonorar (board fee), holiday pay. Year-to-date on the payslip | C §3.1, D-31 | S |
| M0-20 | Holiday-pay basis per employee and earning year | Brutto builds the basis from approved lines, keyed by payout date (ferieloven § 10 (1)): in each shadow month it equals the current system per employee to the øre, and the 2027 basis opens at 0 (or at the imported year-to-date if go-live is after January). December 2026 work paid in January 2027 counts in the 2027 basis. Importing the full 2026 basis for the June 2027 payout, and the 2025 basis for the June 2026 historic shadow, is checked again at gate JUN27 (F-MIG-22) | C §4.2, PLAN.md §1.4 item 5 | P + S |
| M0-21 | Payslip legal content | Every element in §2.5 is present for every M0 case | aml. § 14-15, bokføringsforskriften § 5-6, skattebetalingsforskriften § 5-10-20 | S |
| M0-22 | Voucher | Balances. Accounts per S §6 pkt. 27 (5000, 2600, 5400/2770, 5020/2940, 5405/2785, 2930/1920). Net as one sum on 2930. Equal to the old system per account (mapping differences are class D) | C §11.3, S §6 pkt. 27 | S |
| M0-23 | pain.001 payment file | Sum = Σ net (exact øre). Count = recipients with net > 0. Valid mod-11 account numbers. Withholding is **not** in the salary file: it is a separate order to Skatteetaten, not marked SALA, due the first working day after payout. In M0 its KID is taken from the a-melding feedback (upload on payday, then pay). Brutto computes the KID itself only in M1, after it reproduces every KID the current system used in 2026 [verify KID positions 18–19] | D-24, D-46, PLAN.md §1.4 item 3 | S |
| M0-24 | Withholding due dates | Fri 20.11.2026 → Mon 23.11.2026. Fri 18.12.2026 → Mon 21.12.2026. Wed 23.12.2026 → Thu 24.12 or Mon 28.12 | D-24, GC-12 | S + SKE [U is 24.12 a working day] |
| M0-25 | November a-melding (shadow) | The aggregate is serialised to the JSON the API takes and is valid against its schema (XML 2.3 only as the costed fallback, if 2027 manual upload takes XML). Withholding as an integer per payout date. AGA per sub-unit and zone. Description and benefit code per pay type. arbeidsforholdId equal to earlier submissions | F-MYN-10, F-MYN-14 | S |
| M0-26 | A-melding diff against the old system | 0 differences per employment and inntektsbeskrivelse | B16, F §6.5 | P + S |
| M0-27 | Opening year-to-date and employment fields | No 2026 year-to-date import (D1): 2027 year-to-date opens at 0. Employment fields and arbeidsforholdId come from the source and equal the current system's submissions, never the import date. Jan–Oct 2026 per employee against A07 for 2026-01..10 is reference data for the shadow comparison only | F-MIG-16, F-MIG-21 | P (A07) + S |
| M0-28 | Year switch to 2027 | 2027 card. Trekkrutine 2027 selected by the payout-date year. Year-to-date reset. 2026 holiday-pay basis closed on payout dates up to 31.12.2026 and kept for payout in 2027 | F-KJO-41, F-KJO-18, C §3.5 | S |
| M0-29 | January 2027 without a new tax card | The 2026 card is used and corrected by the end of February. Not 50 % | §§ 5-5-1, 5-5-2 (N13 §1.10) | S + X |
| M0-30 | Pre-approval controls | Blocks: missing account, net < 0, pay after the end date, unsigned pay-type flags, F532 (negative sum per date, 2027-01). Warns: missing tax card | F-MYN-10, D-16 | S |
| M0-31 | **Union dues in the withholding base** (only if dues go through payroll) | Salary 50 000 on 8000, dues 450.40 kr. The withholding base is reduced by 451 kr (the dues deducted, rounded **up** to whole kroner), so the table is looked up on 49 549. Net = 50 000 − withholding − 450.40. Within the annual cap [verify the 2027 cap]. The dues line is special category (GDPR art. 9). Not "after tax": research report C #48 is wrong | skattebetalingsforskriften § 5-9-1, PLAN.md §1.4 item 1, F-TRK-23 | O + S + X [U 2027 cap] |
| M0-32 | **60+ holiday-pay supplement: accrual and June payout** (before JUN27) | Accrual: for an employee entitled to the 60+ supplement (2.3 % of the basis), the supplement is accrued with AGA on it. June payout: the supplement on a basis above 6 G is computed on 6 G only, using the G in force on 31.12 of the earning year (for June 2027: the G on 31.12.2026, from the 2026 rule pack), not the G from 1.5 of the payout year. Example: basis 900 000 → 2.3 % × 6 G. The payout is reported as feriepenger | ferieloven § 10 (3), C #9, GC-04, PLAN.md §3 JUN27 | S + X |
| M0-33 | **Hourly employee in December** (before DEC27) | Pay for hours in December follows the hourly-pay rule in § 5-7-2: two weeks exempt, not ⌊t/2⌋ on the monthly table. Fixed-salary staff in the same run are halved as in M0-10. Bonus at full percentage | skattebetalingsforskriften § 5-7-2, PLAN.md §3 DEC27 | S + X [U how the two-week rule applies when hours are paid monthly] |

### 4.2 M1 – 34 more cases (pilots: direct customers with 20–150 employees; byrå clients are M2)

Cases for pilot-pulled items (PLAN.md §6.1) are written only if the item is pulled at G4 (31.3.2027): M1-26 (board fee), M1-27 (small association fees), M1-28 (travel allowances as pre-split lines) and M1-30 (department and project code). A PAYE card case is added the same way if a pilot pulls PAYE cards.

| Id | Case | Expected logic (one line) | Source | Signs |
|---|---|---|---|---|
| M1-01 | Overtime 50 % and 100 % | Rate 624 000 / 1 950 = 320.00. 10 hours → 4 800.00, 4 hours → 2 560.00. In the holiday-pay basis. Hours reported | C #5 | S |
| M1-02 | Joiner mid-month | 50 000 from 16.3: 25 806.45 (calendar days) or 27 272.73 (working days), method set per company | C #6 | S |
| M1-03 | Position % changed mid-month | 25 000 + 15 000 = 40 000. A-melding date of position % change 16.4 | C #7 | S |
| M1-04 | Back pay as a manual line (no retro in MVP, B42) | Percentage withholding. Reported in the payout month with opptjeningsperiode (earning period). Holiday-pay basis of the payout year | C §5.2–5.3 | S |
| M1-05 | Two payout dates in one month | 10.11 salary (table) and 20.11 bonus 20 000 at 40 % → two sums, due 11.11 and 23.11.2026. One message with two sum lines | C #23 | S |
| M1-06 | Extra run after the a-melding is submitted | Replacement message with the full month's content | GC-11 | S |
| M1-07 | F532 | A correction that reduces withholding for an earlier date goes as a replacement. Local validation stops a negative add-on | GC-10, D-16 | S + X + SKE [U per message or per month] |
| M1-08 | Overpaid bonus, net method | Correction run for March with bonus −10 000 and withholding −4 000. Replacement message. 6 000 recovered by the agreed deduction | C #22 | S + X |
| M1-09 | Two employments in the same legal entity | Withholding = oracle(40 000), not oracle(30 000) + oracle(10 000). Reported once per recipient | C #2 | O + S |
| M1-10 | **Leaver mid-month with holiday-pay settlement** | Pro-rata last salary. Last year's remainder tax-free. This year's 54 000 withheld by percentage (35 % → 18 900). Holiday taken but not deducted is deducted. End date and reason reported. Holiday pay after the end month is allowed | C #10, C §10.1, N39 S03 | S |
| M1-11 | June payout with holiday deduction and trekkfritak (June withholding exemption) | Holiday pay 72 000, deduction −57 692.31, withholding 0, AGA 9 067.38, three a-melding lines | C #8 | S + X |
| M1-12 | June variants | (a) Part-year employee: holiday pay tax-free, June salary not exempt. (b) 12-month card: full withholding | GC-05 | S + X [U (a)] |
| M1-13 | June 60+ supplement with the 6G cap (pilot variant of M0-32) | 2.3 % × min(900 000; 6G) = 18 843.76 withheld. 108 000 tax-free. G is the G in force on 31.12 of the earning year (ferieloven § 10 (3)); recompute the amount with that G from the rule pack | C #9, GC-04 | S + X |
| M1-14 | New employee whose holiday deduction exceeds pay | Capped at −25 000. 3 846.15 carried to July. No negative net or negative sum | C #11 | S |
| M1-15 | Half withholding moved to November | Company setting. Ordinary pay only | GC-06, D-05 | S |
| M1-16 | Sick leave: AGP and full pay above 6G | AGP 2.–17.3. Refund receivable 24 032, entered by hand. AGA base reduced only when the refund is received (one method, "deduct when received", F-FRA-26). Accumulator for the 48 holiday-pay days | C #12 | S + X [U NAV rounding] |
| M1-17 | NAV refund lower than the receivable | The receivable is entered by hand from NAV's payment information (K27 import is LATER). The AGA base is reduced by the 23 500 received, in the month it is received, not by the computed 24 032. The "in advance" method is not offered in M1. The case appears on the list of cases near the 3-month refund deadline until it is closed | GC-18, D-08, F-FRA-25, F-FRA-26 | S + X |
| M1-18 | Graded sick leave, hourly employee | AGP pay per planned day from the 3-month average (ftrl. § 8-28). Correct AGP count | GC-20 | S + X |
| M1-19 | Sick leave across the system switch | AGP days 13–16 paid in Brutto from the imported days. Inntektsmelding (income report to NAV) basis from imported income | GC-01, D-07 | S |
| M1-20 | Parental leave with ID continuity | The same arbeidsforholdId and permisjonsId after migration. No end and restart | GC-03 (without permittering) | S |
| M1-21 | Union dues at pilot breadth (extends M0-31) | The dues actually deducted reduce the withholding base, rounded up to whole kroner (§ 5-9-1), as long as the year's total stays within the annual cap [verify the cap]. The dues themselves are always taken from net. Special category. Never beyond the available net; the rest is carried forward, and only the amount deducted reduces the base | § 5-9-1, PLAN.md §1.4 item 1 (C §2.3 and C #48 are wrong to treat dues as after tax) | S + X [U cap] |
| M1-22 | Deduction priority and protected amount | Net 11 388 (rent 4 742, 3 258 and the loan carried forward). Protected amount from the 1.7 rule pack | C #14, D-06 | S + X |
| M1-23 | Samordnet utleggstrekk (coordinated garnishment) | 4 500 of 6 000. Employee KID. Due Mon 23.11.2026. `utleggstrekkSamordnet` dated 20.11. Entered with four eyes | C #15, D-23 | S + X [U carry or lapse] |
| M1-24 | Agreed deduction without a written agreement | `REQUIRES_WRITTEN_AGREEMENT`. No deduction. Receivable on 1570 | GC-09 | S |
| M1-25 | OTP contribution, employee share and two zones | Employee share before tax. 12G cap. AGA on the premium 21 000 × 14.1 % + 9 000 × 6.4 % = 3 537 | GC-17, C §9 | S + X [U] |
| M1-26 | Board fee without a tax card | 40 000 → 20 000 withheld, AGA 5 640. No holiday pay or OTP. Honorarium employment reported only in the payout month | C #4, GC-13a | S |
| M1-27 | 10 000-krone rule in a tax-exempt organisation | 3 × 4 000: everything is reported in October, withholding from the limit. Keep such customers out of M1 until Skatteetaten has answered | GC-14, D-09 | S + SKE [U] |
| M1-28 | Mileage and per diem split | 1 800 and 638 taxable (AGA 253.80 and 89.96). `reiseregningKomplett` = false makes everything taxable | C #20, D-12 | S + X [rates from secondary source] |
| M1-29 | Benefit in kind with low cash pay | Withholding capped at 2 000, warning, AGA on 15 085.83 (2026 car rules; the 2027 model only if a pilot has company cars) | C #19, D-10 | S + X |
| M1-30 | Department changed mid-month (pilot-pulled flat code; no percentage split) | 28 000 / 20 400 / 13 600. AGA, holiday pay and OTP allocated proportionally by largest remainder. Exact to the øre | GC-16, D-39 | S |
| M1-31 | Migration year-to-date equals A07, IDs preserved | Per employee × description × month diff 0. IDs 100 %. All active employments and leaves in the first message | §3.1, D-18 | P (A07) + C + S |
| M1-32 | Variable pay in arrears across the switch | Paid once, in Brutto, under Brutto's year rules. The old system does not pay | GC-02 | S + C |
| M1-33 | Missing tax card, and a new card arrives after approval | 50 % at computation. Choice between recompute and next run. No fetch for `registrertSomDoed` | GC-22, D-22 | S |
| M1-34 | Imported pay type with wrong flags, and Easter due dates | (a) Quarantine until signed. (b) Payout Wed 24.3.2027 → withholding due Tue 30.3.2027 | GC-21, GC-12 (moved to 2027) | S |

### 4.3 Not in M1 (LATER or CUT), so no golden case now

| Case | Tier | Why |
|---|---|---|
| Permittering (temporary layoff) 50 % (C #13) | LATER | Rare in the pilot profile. Manual fallback |
| Death and post-death pay (C #25) | LATER | Rare. Handled manually with Sjur |
| AGA fribeløp in zone Ia (C #17), ambulating AGA (C #18) | CUT until a customer asks | Excluded from the pilot profile (B3). PAYE (kildeskatt på lønn) cards are pilot-pulled instead (PLAN.md §6.1): percent path only, without June/December relief [verify] |
| Net-pay agreement (C #16) | CUT | Excluded (B3) |
| Omsorgsdager (care days, GC-19) | LATER | Absence module |
| Company car under the 2027 model | M1 only if a pilot has one, otherwise LATER | D-10 |

a-melding 2.4 (F-MYN-20) is no longer in this list: it is M1, first in the M1 queue for our own payroll, with dated gates 24-S (mapping by 1.7.2027) and 24-T (accepted in the 2.4 test environment by 1.12.2027). Its test is a semantic diff of 0 against 2.3 on shared fields, and twins accepted in the 2.4 test environment (§2.9, §6; D-19, N14).

---

## 5. Payroll-domain hours and what can be bought

### 5.1 M0 (from now until gate JUN27, roughly November 2026 to mid-May 2027; most of it before mid-January)

| Activity | Hours |
|---|---|
| Pay-type set for the company's own payroll (about 10 pay types): flags, a-melding mapping, accounts | 15 |
| 2026 rule pack and rounding-policy table, signed | 10 |
| 2027 rule pack and trekkrutine 2027 conformance sign-off (December) | 10 |
| 30 M0 golden cases: hand-calculated expected values and signature | 60 |
| A-melding mapping review, test-portal upload, diff against the old system | 15 |
| Payslip content checklist and template review | 5 |
| Opening balances against A07, tax cards with four eyes | 10 |
| Historical shadow of September and October 2026 | 10 |
| Shadow runs in November and December: diff review, classification, protocol | 20 |
| Reviewing results and triaging defects during the build | 30 |
| June 2026 shadow and M0-32 (JUN27) | 8 |
| Drafting questions to Skatteetaten (licence, AGA rounding, half withholding, 24.12, upload format, KID positions, union-dues cap) | 5 |
| **Total** | **≈ 200 h (range 170–240)** |

About 200 hours over roughly 11 weeks is about 18 h/week from Sjur on top of his founder role. **Buy 20–30 h** from an external payroll expert (a byrå's payroll lead or a payroll auditor). They countersign M0-05, 07, 08, 10, 15, 16 and 29 and review the a-melding mapping: before M0-α (27.11.2026) for cases among the first 20, and before M0-L for the rest.

### 5.2 M1 (pilot build-out, about 9–12 months)

| Activity | Hours |
|---|---|
| 34 named M1 cases (about 3 h each including [U] research) | 100 |
| About 90 coverage-matrix variants to reach about 150 cases (about 1 h each) | 90 |
| Pay-type catalogue (26 standard types and customer copies), flags, mapping | 60 |
| Rule packs: G on 1.5.2027, protected-amount rates on 1.7.2027, the 2028 pack and trekkrutine 2028 | 40 |
| Reviewing results, triaging defects, reviewing surviving mutants | 150 |
| Migration and mapping, about 6 customers × 30 h | 180 |
| Parallel runs (direct customers 2 periods; byrå clients are M2), about 6 × 16 h | 100 |
| Historical June and December shadows per customer | 40 |
| TT02 scenario specification and acceptance | 40 |
| B28 release sign-off (about 2–3 h × about 20 releases) | 50 |
| Clarifications with Skatteetaten, NAV, a lawyer or an auditor | 30 |
| Help texts, support routines, pilot onboarding (onboarding a byrå is M2) | 100 |
| Payroll-day on-call (domain), first 3 months | 60 |
| **Total** | **≈ 1 040 h** |
| Later but mandatory before 2028: a-melding 2.4 specification and acceptance | +120 h |

### 5.3 What can be bought or delegated

| What | From whom | Hours saved | Limit |
|---|---|---|---|
| Writing and countersigning [U]-heavy golden cases (June, sick leave and refunds, deductions, organisation niche) and the 20 % countersign | Payroll lead at a byrå, or a payroll auditor | 120–150 | Sjur still owns the rule pack and the veto |
| Migration mapping per customer | An implementation partner who knows the customers (in M2, the pilot byrå for its clients) | 100–150 | Brutto runs the A07 checks. The customer (in M2, the byrå) signs |
| Classes C and D in the parallel run | The customer's payroll lead (they sign these anyway, F-MIG-31) | 40–60 | – |
| Help texts and first-line support | Pilot byrå (partner agreement) | 40–60 | Never approves or submits for the customer (D-35) |
| B28 deputy | Contracted external payroll expert on call, about 2 h per release | – | Must be named in writing |
| Free oracles | Skatteetaten's text file, trekkrutine and search service. NAV's `helse-spleis` as a reference for sick pay. Each old system during migration (a differential test) | – | Skatteetaten answers that need [U] resolved: send questions now |
| **Cannot be bought** | Rule-pack sign-off, the release veto, the final classification of B-category defects | – | – |

Bought and delegated work comes to about 350–450 h. That leaves about 600–700 h in-house over the M1 period, which is more than a founder can give. **M1 needs a second payroll-domain person at about 0.5 FTE, or the contracted deputy with a larger share.** R3-strategi reached the same conclusion with a wider scope (about 2,400 h, two specialists).

---

## 6. Test items by tier

| Item | Tier | Note |
|---|---|---|
| Golden-case harness with CODEOWNERS, 30 M0 cases (20 signed at M0-α, all 30 at M0-L), plus M0-31 at M0-L if dues go through payroll | **M0** | §2.1, §4.1 |
| M0-32 (60+ supplement) by JUN27 and M0-33 (hourly December) by DEC27 | **M0+ track** (first in the M1 queue) | §2.9, §4.1 |
| Trekkrutine port, 100 % against the full 2026 and 2027 files | **M0** | §2.2 |
| Schema validation (JSON; XSD only if XML is ever built) and the local rule subset, test-portal upload of the synthetic twin | **M0** | §2.3 |
| Shadow-run protocol, two periods, single payer, report and posting | **M0** | §2.4 |
| Payslip element check | **M0** | §2.5 |
| Money types, clippy bans, rounding table in the rule pack | **M0** | §2.6 |
| Five invariants, deploy freeze from approval to upload | **M0** | §2.7 |
| June 2026 shadow by 14.5.2027 | **M0+ track** (gate JUN27) | §2.9 |
| First live December and the own 2027 annual statement | **M0+ track** (gates DEC27, 15.11.2027, and AS27, 14.1.2028) | §2.9 |
| Migration against A07 per customer (Port M) | **M1** | §3.1 |
| Release diff as an in-production shadow job, B28 owner and deputy | **M1** | §3.2 |
| TT02 end-to-end (L1, L2, L3) and Tenor twins | **M1** | §3.3, §3.4 |
| Ten invariants and mutation testing on four modules | **M1** | §3.5 |
| About 150 cases in the coverage matrix, 20 % countersigned externally | **M1** | §3.7 |
| PDF/A with veraPDF | **M1** | – |
| Byrå-client parallel run (1 period plus a June shadow), tenant invariance in a byrå tenant | **M2** | §3.1, §3.5 |
| a-melding 2.4 dual serialisation, semantic diff, 2.4 test environment | **M1** (M0+ track; gates 24-S, mapping by 1.7.2027, and 24-T, accepted in test by 1.12.2027) | D-19, F-MYN-20 |
| Time-travel environment across the year end | **LATER** (before December 2027). A manual year-switch run is enough for M0 | F §7.5 |
| Anonymised production sandbox | **LATER**, with a DPIA | F-SIK-36 |
| ISAE evidence packaging | **LATER** | – |
| Load test with 400+ employees | **LATER** (trivial at 150 employees) | – |
| "300 cases" as a count target, and "10 000 random withholding combinations" | **CUT**. Replaced by the coverage matrix and the full-file test | R3 port 1 |
| Nightly Playwright UI end-to-end | **CUT** for M0/M1. Test the API (B41). UI smoke only | F §7.1 |
| Regular shadowing of byrå clients against competitors | **CUT** until asked | F §7.3 |
| 500,000-payslip load test | **CUT** until there are large customers | F §7.1 |

---

## 7. Open items that block signing specific cases

| # | Question | Blocks | Who | By |
|---|---|---|---|---|
| 1 | AGA rounding: does F185 accept rounding down, to the nearest krone, or both? (test in TT02 with x.30, x.50 and x.99) | M0-15 | Developer and Sjur | Before M0-α (default `ToZero`) |
| 2 | Half withholding: percentage card, and supplements paid with the period's salary up to average earnings (§ 5-7-2 fourth paragraph) | M0-10 | Sjur and X | Before the December run |
| 3 | Is 24.12 a working day for withholding due dates? | M0-24 | Skatteetaten | Before the December run |
| 4 | AGA on the OTP premium: timing, admin costs, zone split | M0-16, M1-25 | Auditor and Skatteetaten | Before M0-α |
| 5 | Manual-upload format for 2027 periods (JSON per the Q&A of 18.06.2026, or XML). 2026 periods do not arise: the current system submits all of 2026 (D1) | M0-25, M0-L | [verify] item in the letter to Skatteetaten; developer rehearses with a synthetic twin in the test upload. If XML, start the costed XML 2.3 fallback | By 27.11.2026 (M0-α) |
| 6 | Written licence for the trekkrutine and the text file (does not block M0) | – | Sjur (a human sends it) | Now |
| 7 | F532: does it apply per message or per month? | M1-07 | Skatteetaten | Before M1 |
| 8 | 50 % rule for frikort and for a missing tax card (legal basis) | M0-07, M0-08 | X or Skatteetaten | Before M0-α |
| 9 | Board fee to an employee, zone for freelancers, the 10,000 limit (D-09) | M1-26, M1-27 | Skatteetaten | Before M1 pilots in organisations |
| 10 | Is `antall` (hours) required for hourly pay in the a-melding? | M0-12 | Developer, rule spreadsheet | Before M0-α |
| 11 | The 2027 annual cap for deductible union dues | M0-31, M1-21 | Letter to Skatteetaten | Before M0-L, if dues go through payroll |
| 12 | KID positions 18–19 for the forskuddstrekk payment | Brutto's own KID (M1); M0 takes the KID from the feedback | Letter to Skatteetaten; check against the 2026 KIDs from the export | Before M1 |
| 13 | How the hourly-pay rule in § 5-7-2 (two weeks exempt) applies when hours are paid monthly | M0-33 | X or Skatteetaten | Before DEC27 (15.11.2027) |

---

## 8. Sources

- `analyse/research/C-beregning.md`: §0.1, §2.1–2.4, §3, §4.2, §5.2–5.3, §10.1, §11.2–11.3, §12 (cases #1–25), §13
- `analyse/research/R3-kritikk-domene.md`: b.0, D-01–D-55, port table (c), golden cases GC-01–GC-22, (g)
- `analyse/research/R3-kritikk-strategi.md`: §2.3 (≈ 2,400 h table), §2.4 (buy 150–250 h external oracle)
- `analyse/research/F-arkitektur.md`: §1.10, §6.4–6.5, §7.1–7.6
- `analyse/research/B-myndigheter.md`: §2 (a-melding channels, manual upload), §10.1–10.2 (payslip and § 5-6), pension provider
- `analyse/research/S-avklaringer-fra-sally.md`: §6 pkt. 27 (standard accounts)
- `analyse/build/data/design.json`: B6, B12, B16, B19, B24, B26, B28, B37, B41, B42, B43, `oversikt.datoer`
- `analyse/build/data/fase1.json`: D05, L01, L02, L03
- `analyse/build/data/omr-K*.json`: F-TRK-07–12, F-KJO-13/14/17/18/42, F-MYN-10/12/14/21, F-REG-30, F-SIK-35/36, F-MIG-16/21/31/32
- `analyse/natt/funn/N08.md` §3, §7, §8, §14. `N13.md` (trekkrutine, f64, rounding table, vectors). `N14.md` (2.4, manual upload goes to JSON). `N39.md` §6–7 (TT02 scenarios, layers, identity guards). N22 does not exist.
