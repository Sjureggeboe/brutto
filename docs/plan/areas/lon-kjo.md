# Scope review: LON (pay agreements and pay types) and KJO (payroll run and calculation)

> Working paper from the scope review of 29.10.2026. PLAN.md is the main plan and `docs/plan/scope.csv` holds the final tier per function; where this paper disagrees, they win.

Reviewer: LON/KJO agent, 29.10.2026. Source: `analyse/build/data/omr-K2.json` (all 77 functions, 20 owned entities, 20 area questions), plus `design.json` (B5, B19, B37, B41–B43), `research/C-beregning.md` §0–2, `research/S-avklaringer-fra-sally.md` §6, `research/R0-matrix-lonn-omrader.md` (agent K2), `natt/funn/N13.md` (trekkrutine and rounding) and `N10.md` (approval).
Per-function detail: `docs/plan/scope.csv` (77 rows with area LON or KJO).

## 1. Tier counts

| Area | Functions | Marked MVP today | M0 | M1 | M2 | LATER | CUT |
|---|---|---|---|---|---|---|---|
| LON | 31 | 11 | 7 | 3 | 0 | 11 | 10 |
| KJO | 46 | 34 | 23 | 12 | 0 | 8 | 3 |
| **Total** | **77** | **45** | **30** | **15** | **0** | **19** | **13** |

- 44 of the 45 MVP-marked functions stay in M0/M1. One moves out: F-LON-05 (customer's own pay types with quarantine) goes to LATER.
- One "Etter MVP" function moves in: **F-KJO-41 year-end → M0, due 15.1.2027.** It was deferred because the first year-end was assumed to be December 2028. This paper first put it in M1 for the first live December (2027). **Plan v1 decision:** with own payroll going live in January 2027, the go-live is itself the first year switch (2027 rule pack and table file, 2027 tax cards, 2026 holiday-pay basis closed and carried as opening state), so F-KJO-41 is M0 (PLAN §1.6, §7.4). The first live December is still gate DEC27 (15.11.2027), with the 2028 rule pack by 22.12.2027.
- 14 "Må" (must) functions are LATER or CUT. They are all tariff, pay-settlement, retro, cut-off, death or June/December checklist features. Each has a lawful manual path for the M1 customer profile (see CSV).
- Entity fields owned by LON/KJO: **499 in total → 177 in M0 → 291 in M1.** Four entities (88 fields) are not needed before LATER at all: D-Tariffavtale, D-Lonnstabell, D-Lonnsoppgjor and D-Lonnsforslag.

## 2. Narrative

LON and KJO are the product. The MVP marking here was already mostly the true core, so cutting by function count saves little. **The savings are in depth.** The current design builds SD Worx-grade machinery into every core function:
- bitemporal versioning of pay types, pay agreements, fixed lines and settings
- a 20-node calculation graph with fixed-point iteration
- signed rule packs with a status workflow
- quarantine and four-eyes release for pay types and mappings
- inheritance chains (chain → byrå → client)
- materialised accumulators with year locks
- a separate trace table
- 8 run types and a 10-state linear run status

M0 needs none of this. M1 needs very little of it.

What must be right from the first line of code, because it is expensive to retrofit:
1. A **pure, deterministic calculation function**: inputs + rule pack + engine version → lines.
2. **Frozen input snapshot + hash** and **approval bound to the result hash** (F-KJO-07, F-KJO-23, F-KJO-24, F-KJO-25).
3. **Flag snapshot per line** (F-LON-04).
4. **A JSON trace per line** (F-KJO-16).
5. **Money as decimal with an explicit rounding policy** (F-KJO-17).
6. **Idempotent input API** (F-KJO-03), because the CLI, retries and later agents call it (B41 narrowed: no MCP in M0; MCP draft tools for pay inputs in M1).

Everything else can start as the simplest lawful version.

The pay-type model (B5) has to be extended before M0. Sjur's model (number, a-melding code, four flags, two accounts) cannot produce a correct a-melding or correct withholding. The minimum additions are:
- withholding method (table, percent or none)
- half-tax eligibility
- `fordel` (cash, natural benefit or expense allowance)
- report object and quantity requirement
- AGA type and sign

Pension basis, sick-pay basis, June exemption and car tilleggsinformasjon (extra fields reported in the a-melding) can wait for M1. Retro, AFP, hourly-rate basis, holiday-deduction basis, extra accumulators, languages and quarantine status can wait longer.

### Recommendation on the shape of M0
**Run November and December 2026 as shadow runs.** The existing payroll system stays the system of record and sends the a-melding for all of income year 2026. Brutto becomes the system of record from period 2027-01 as a stretch (about 40 %); the planning date is 2027-02, and 2027-03 at the latest. PLAN adopts this as D1 and the new B44. Reasons:
- If Brutto sends the November or December 2026 a-melding, it also has to produce the 2026 annual statement to employees (sammenstillingsoppgave) with imported Jan–Oct figures (D-27). It would also take on mid-year migration risk.
- Starting at 1.1.2027 means year-to-date (YTD) opening balances are needed only for comparison, plus the 2026 holiday-pay basis for the June 2027 payout.
- The 2027 rule pack and trekkrutine (Skatteetaten's withholding routine) are needed anyway. The 2027 routine is normally published in early December.
- B19 already recommends sending from Brutto only once everything matches to the øre. This makes the switch date explicit.

December 2026 in shadow mode exercises half-tax withholding (F-TRK-12) and January 2027 exercises the year boundary (2027 rule pack and tax cards; F-KJO-41, M0). The first live December in Brutto is December 2027 (gate DEC27). All are good tests before real customers.

## 3. Changes against the current MVP marking

- **Pulled in:** F-KJO-41 (M0 under Plan v1; the year switch for the January 2027 go-live, due 15.1.2027).
- **Pushed out:** F-LON-05 (LATER). In M1, Brutto's payroll expert adds pay types to the shared catalogue on request. Customers override text and accounts only.
- **MVP functions that are M1, not M0:**
  - LON: F-LON-08, F-LON-15, F-LON-17
  - KJO: F-KJO-04, F-KJO-05, F-KJO-08, F-KJO-10, F-KJO-12, F-KJO-20, F-KJO-22, F-KJO-28, F-KJO-29, F-KJO-34, F-KJO-38, F-KJO-39
- **Date-critical items for own payroll:**
  - F-TRK-12 half-tax withholding (TRK area) is M0 in `scope.csv`: the December 2026 shadow run needs it.
  - F-KJO-38/39 and F-TRK-11 (holiday-pay payout, ferietrekk and June exemption; the F-KJO-37 accrual is M0): gate 14.5.2027.
  - F-KJO-41 year switch 2026→2027: 15.1.2027 (M0). First live December: gate DEC27, 15.11.2027; 2028 rule pack by 22.12.2027.

## 4. Proposed minimal calculation pipeline

### M0: own payroll (one legal entity, one sub-unit, ≤10 employees, fixed monthly salary, maybe one hourly employee)
1. **Create the run** (F-KJO-01). ORDINARY run for one opplysningspliktig (reporting entity). The payout date sets the reporting month, the income year and the AGA rate (cash principle, C §0 pt 2).
2. **Freeze inputs** (F-KJO-07). Take the active employments and stillingsprosent (position %), the pay agreements (F-LON-11) and the manual variable lines received via API (F-KJO-03). Add manually entered tax cards with version (TRK), settings (F-KJO-46) and the rule pack for the payout year (F-KJO-18). Store a canonical JSON snapshot with a SHA-256 hash.
3. **Fixed pay.** Monthly salary at 100 % × stillingsprosent, for a full month. A mid-month change becomes a manual line in M0.
4. **Variable pay** (F-LON-10, F-KJO-09). Hourly pay = hours × hourly rate, with a work date per line. Other manual lines are quantity × rate or a fixed amount.
5. **Cash gross.** Sum of the cash lines.
6. **Natural benefits** (F-KJO-11), for example EK (elektronisk kommunikasjon: employer-paid phone and internet) entered as a manual line. They are added to the withholding and AGA bases, not to net.
7. **Withholding base per person**, split into the table base and the percentage base using the pay-type flags (F-LON-02). If any employee pays union dues through payroll, the base is reduced by the deductible dues, rounded up to whole kroner (skattebetalingsforskriften § 5-9-1; F-TRK-23, M0).
8. **Forskuddstrekk** (tax withholding; F-TRK-07/08/03):
   - Table withholding uses Brutto's own Rust port of the trekkrutine. It must match Skatteetaten's table file 100 % (N13).
   - For percentage withholding, base and amount are rounded down to whole kroner (§§ 5-10-4, 5-5-4; PLAN §1.4).
   - A missing tax card gives 50 %.
   - Withholding is capped at the available cash amount.
9. **Net** = cash gross + tax-free reimbursements − withholding − union dues and agreed deductions. Net must be ≥ 0, otherwise approval is blocked (F-KJO-32).
10. **AGA** (arbeidsgiveravgift, employer's social security contribution; F-KJO-13). Sum the AGA-liable lines per sub-unit and multiply by the zone rate. Add a manually entered OTP premium base if a premium is paid this month (PEN). Track the fribeløp (exemption amount) only if the zone has one.
11. **Holiday pay** (F-KJO-14, F-KJO-37). Basis for this run × rate gives the accrual, plus AGA on the accrual. YTD basis = imported opening state + approved lines.
12. **YTD** (F-KJO-15). Computed from the lines and the opening balances. Nothing is materialised.
13. **Rounding and trace** (F-KJO-17, F-KJO-16). Lines in øre, withholding in whole kroner, AGA on the monthly sum. One JSON trace per line.
14. **Draft outputs.** Journal and totals (F-KJO-45) and a voucher preview. The draft can be recalculated any number of times as numbered versions (F-KJO-19).
15. **Øre comparison with the old system.** Compare per employee: gross, withholding, net, AGA basis and holiday-pay basis. This is done outside the engine.
16. **Approve** (F-KJO-23). One named human who did not prepare the run approves the result hash. Log the SoD (separation of duties) exception, because everyone is paid in the run, and send the totals to the board chair. After approval the run is immutable (F-KJO-25).
17. **After approval only** (F-KJO-24; B43 tracks):
    - payslip PDFs, archived (F-KJO-42, F-KJO-44)
    - pain.001 for net pay as SALA, plus forskuddstrekk as its own payment order to Skatteetaten, not SALA, due the first working day after payout, with the KID from the a-melding feedback (BET; PLAN §1.4)
    - voucher CSV (REG)
    - the a-melding aggregate, serialised to the JSON the API takes, for manual upload (MYN; F-MYN-14, now M0 in `scope.csv`)

### M1: direct-customer pilots (20–150 employees, monthly and hourly pay, OTP, few sub-units; a firm's own payroll can be one, firm clients are M2)
0. **Create and freeze.** Run types are ORDINARY, EXTRA, CORRECTION and MIGRATION (F-KJO-01, F-KJO-28, F-KJO-29), with an employee selection. Tax cards are fetched by API and fetched again before approval (F-KJO-24).
1. **Fixed pay.** Proportional segments for start, end, %-change and unpaid leave, with one method per entity (F-KJO-08). Fixed lines (F-LON-15) and benefits: company car and EK (F-LON-17).
2. **Variable pay:**
   - hours, and overtime at a fixed % per pay type (F-KJO-09)
   - lines paid in arrears with work date and earning period (F-KJO-04)
   - sick pay and unpaid leave (F-KJO-10)
   - in June: holiday-pay payout and ferietrekk (holiday deduction from monthly salary) (F-KJO-38, F-KJO-39)
3. **Retro.** No automatic retro. Back pay is a manual line with the original description, an earning period and percentage withholding.
4. **Cash gross.**
5. **Natural benefits.** These include bilOgBaat tilleggsinformasjon (company-car fields in the a-melding).
6. **Allowances.** Pre-split lines from CSV (F-KJO-12), pilot-pulled (PLAN §6.1). The Utleggsappen integration and travel-rate calculation are LATER (PLAN §6.2).
7. **Employee pension contribution**, deducted before tax (F-PEN-09).
8. **Withholding base per person and payout date**, summed over employments, minus withholding already taken earlier in the month (F-TRK-09), and reduced by deductible union dues (§ 5-9-1, rounded up). Includes the June exemption (F-TRK-11), half tax in December (F-TRK-12) and frikort YTD (frikort: tax-free card up to an income limit) (F-TRK-10).
9. **Forskuddstrekk**, capped at cash, with minimum limits (F-TRK-15). Totals per payout date (F-TRK-16).
10. **Net before deductions.**
11. **After-tax deductions in a fixed order:**
    - utleggstrekk (attachment of earnings) and bidrag (child-support deduction) from a manual register (F-TRK-19/20)
    - union dues (F-TRK-23; taken from net here, after they have reduced the withholding base in step 8)
    - agreed deductions with a protected amount (F-TRK-24/27)
    - carry-forward of what could not be taken (F-TRK-28)
12. **Net ≥ 0.** Limit the holiday deduction and carry the rest forward. Any remaining negative net becomes a receivable on account 1570 (F-KJO-32).
13. **AGA.** Per sub-unit and zone, including the pension-premium base (F-PEN-06), minus NAV refunds with one method ("deduct when received"; the refund receivable is entered by hand, since K27 import is LATER under Plan v1), and the fribeløp where a zone has one (F-KJO-13; zone Ia is outside the M1 profile).
14. **Holiday-pay accrual**, including the 60+ supplement, plus AGA on the accrual (F-KJO-14, F-KJO-37).
15. **Employer pension.** Nothing is calculated; the premium comes from the supplier invoice (PEN, S §6 pt 29).
16. **YTD, rounding and trace.**
17. **Voucher.** One flat department/project code is taken from the employment and allocated by largest remainder (F-LON-06). Dimension sync with the accounting system is LATER.
18. **Controls.** About 10 controls with acknowledgement, plus a-melding pre-validation (F-KJO-20), and the attestation summary against last month (F-KJO-22).
19. **Approval.** One or two levels with BankID step-up and SoD rules. Recording a byrå client's approval with channel and attachment (F-KJO-23) waits for M2. Hard block on outputs until approval, an immutable run (F-KJO-24/25) and the B43 tracks.

## 5. Entities needed for M0/M1

### Owned by LON/KJO: fields kept per tier
Field names below are copied from the JSON (`felt[].navn`).

| Entity | Fields today | M0 | M1 (cumulative) | Dropped for M0/M1 (over-engineering or later) |
|---|---|---|---|---|
| D-Lonnsart | 48 | 23 | 34 | beskrivelse, retro_relevant, inngar_i_timesatsgrunnlag, inngar_i_ferietrekkgrunnlag, afp_grunnlag, akkumulatorer, sats_kilde, vis_i_timeliste, opprinnelse, arvet_fra_lonnsart_id, status, godkjent_av, gyldig_til, registrert_tid |
| D-Lonnsavtale | 34 | 14 | 18 | valuta, tariffavtale_id, lonnstabell_id, lonnstrinn, ansiennitetsdato, garantilonn_aktiv, effektiv_arslonn_100, lonnsfrekvens, forholdsmessig_metode, ferietrekk_metode, ferietrekk_tidspunkt, overtidsregelsett, nettolonn_avtalt, netto_malbelop, oppgrossingstabellnummer, lonnsoppgjor_id |
| D-Fastlinje | 22 | 0 | 14 | type, prosent, stopp_ved_ulonnet_permisjon, stopp_ved_permittering, gjelder_kjoringstyper, dimensjoner_overstyring, slipptekst_tillegg, aktiv |
| D-Fordelsavtale | 21 | 0 | 15 | motortype, yrkesbil_km_privat, markedsverdi, trekk_id, forsikring_id, registrert_tid |
| D-Lonnsgrunnlag | 34 | 16 | 30 | fra_tid, til_tid, vedlegg_ref, onsket_periode |
| D-Lonnskjoring | 37 | 21 | 27 | lonnsfrekvens, slipp_tilgjengelig_dato, lonnskalender_id, antall_mottakere, sum_brutto, sum_netto, sum_forskuddstrekk, sum_utleggstrekk, sum_aga (derive the sums from lines), simulering_utloper |
| D-Lonnslinje | 36 | 22 | 35 | spesifikasjon |
| D-Lonnsslipp | 34 | 23 | 29 | saldoer, forklaring, avdeling, sprak, apnet_tid |
| D-Lonnsinnstillinger | 28 | 8 | 17 | lonnsfrekvenser, feriepenger_av_forskuttering, helligdag_er_arbeidsdag, ferietrekk_tidspunkt, retro_ferietrekk, retrohorisont_maneder, boutgiftstillegg, trekkrekkefolge (fixed in code), kontrollterskler (fixed in code), slipp_publiseres_dager_for, arvet_fra_mal |
| D-Akkumulator | 19 | 8 | 8 | Reduce to **opening balances only**; compute current values. Drop underenhet_id, aga_sone, pensjonsordning_id, trekkobjekt_id, botte_type, verdi_belop, verdi_antall, siste_kjoring_id, avstemt_mot_amelding, last, oppdatert_tid. Add a "through date". |
| D-Feriepengegrunnlag | 21 | 7 | 13 | rest_overfort_ferie, nav_dager_refundert, forskuttering_ordning, feriepengerefusjon_forventet, avsetning_regnskap, aga_avsetning, korreksjoner, last |
| D-Beregningsspor | 17 | 7 (JSON keys) | 7 | Make it a JSON column on D-Lonnslinje instead of a table. Drop spor_id, kjoring_id, beregningsversjon, lonnslinje_id, arbeidsforhold_id, node, regel_versjon, regelpakke_id, avrunding, forklaringsmal (redundant with line/run). |
| D-Avvik | 16 | 0 | 12 | lonnsart_id, terskel, automatisk_forklaring, myndighetssak_ref. M0 uses engine invariants as errors instead. |
| D-Kjoringsgodkjenning | 18 | 13 | 17 | rolle (derive from the role assignment) |
| D-Regelpakke | 15 | 8 | 8 | Keep as a **data file in the repo**, not a DB-managed workflow. Drop arver_fra, status, regelimplementasjoner, valideringsmatrise_versjon, signert_lonnsfaglig, signert_utvikler, publisert_tid (Git review replaces signing). |
| D-Sats | 11 | 7 | 7 | sats_id, dimensjon (put zone into the key), gyldig_til, kommentar |
| D-Tariffavtale | 29 | 0 | 0 | Entire entity is LATER |
| D-Lonnstabell | 15 | 0 | 0 | Entire entity is LATER |
| D-Lonnsoppgjor | 23 | 0 | 0 | Entire entity is CUT |
| D-Lonnsforslag | 21 | 0 | 0 | Entire entity is CUT |
| **Total** | **499** | **177** | **291** | |

Design-level over-engineering to drop for M0/M1:
- **Bitemporality.** A `registrert_tid` audit timestamp plus valid-from is enough; R3 D-38 agrees. This applies to D-Lonnsart, D-Lonnsavtale, D-Fastlinje, D-Fordelsavtale and D-Lonnsinnstillinger.
- **The 10-value linear `D-Lonnskjoring.status`.** Stop at APPROVED/DISCARDED and use the B43 tracks after that.
- **Run types** RETRO, FORSKUDD and SIMULERING.
- **D-Lonnsgrunnlag lifecycle** statuses RECEIVED, VALIDATED, DEFERRED, PAID and REPORTED. Keep ACCEPTED, LOCKED and REJECTED; paid and reported are run-level tracks.
- **Byrå/group template inheritance** (`opprinnelse`, `arvet_fra_*`).
- **Quarantine status and four-eyes release** on pay types.

Fields to add:
- a "through date" on opening balances (prevents double counting, R0 §3 no. 7)
- `trace` (JSON) on D-Lonnslinje
- `trekkmetode_effektiv` (effective withholding method) on D-Lonnslinje in M1, as R0 proposes
- a catalogue version instead of per-pay-type versions

### Borrowed from other areas (owners review the fields)
- **M0:**
  - D-Virksomhet and D-Underenhet with AGA zone (ORG)
  - D-Person, D-Arbeidsforhold and D-Stillingsperiode for stillingsprosent, start and end (PER)
  - D-Skattekort, entered manually (TRK)
  - D-Bilag as CSV (REG)
  - D-AMelding (MYN)
  - D-Betalingsforslag, D-Betalingsoppdrag and D-Betalingsfil (BET)
  - D-Dokument or plain object storage for PDFs (HR)
  - D-Rolletildeling, minimal (LED/SIK)
- **M1:**
  - D-Trekk and D-Trekkpalegg (TRK)
  - D-Kontomapping (REG)
  - D-Kostnadsfordeling, single department/project (ORG)
  - D-Mappingregel and D-Kildeprofil (PLA)
  - D-Pensjonspremie and D-Pensjonsmedlemskap (PEN)
  - D-Fravaer, D-Permisjon and D-Sykefravaerstilfelle, basics only (FRA)
  - D-Refusjonskrav, manual (FRA)
  - holiday days entered by hand for ferietrekk (FRA); the holiday-days ledger D-Feriesaldo / F-FRA-09 is LATER under Plan v1
- **Not needed in M0/M1 for LON/KJO:**
  - D-Lonnskalender: the payout date is a field on the run.
  - D-Stilling: only used by pay settlement.
  - D-Utleggslinje as a separate store: M1 can post pre-split lines straight into D-Lonnsgrunnlag.
  - D-Integrasjon beyond the source id.

## 6. Top cuts
1. **The whole pay-settlement module** F-LON-22 to F-LON-31 (10 functions, D-Lonnsoppgjor and D-Lonnsforslag). It is HR scope (B34). F-LON-24, F-LON-28 and F-LON-29 stay LATER with the tariff epic.
2. **Tariffs, ladders, seniority and guaranteed wage** (F-LON-12, F-LON-19, F-LON-20, F-LON-21) go to LATER, together with D-Tariffavtale and D-Lonnstabell. The M1 profile has no tariff ladders. Virke HUK will likely be the first tariff, because of the organisation segment.
3. **Automatic retro with knock-on effects** (F-KJO-26, F-KJO-27) goes to LATER, with a manual back-pay line as the workaround.
4. **Net-pay agreements and gross-up** (F-LON-13, F-KJO-33), plus bankruptcy (F-KJO-36), advances (F-KJO-31), employee loans (F-LON-18) and mass change (F-LON-16): CUT.
5. **Formula/expression language** (part of F-LON-10): CUT. Declarative rule types only (B5).
6. **Pay-type quarantine, self-service own pay types, templates, flag validation as a product feature, translations** (F-LON-03, F-LON-05, F-LON-07, F-LON-09): LATER.
7. **Cut-off with deferral, June/December run plans, explanations in plain language, run reversal** (F-KJO-02, F-KJO-40, F-KJO-21, F-KJO-43, F-KJO-30): LATER.
8. **Design depth** inside kept functions: bitemporality, graph engine with fixed-point iteration, signed rule-pack workflow, materialised accumulators, inheritance chains, scenarios and simulations. This saves the most effort.

## 7. Legal must-haves for M0/M1 (cannot be cut)
- **Cash principle.** The payout date decides the income year, the a-melding month, the AGA rate and zone, and the holiday-pay earning year (C §0 pt 2).
- **Payslip.** The employee gets a written statement of how pay was calculated, the holiday-pay basis and the deductions (aml. § 14-15). Bokføringsforskriften § 5-6 also requires, per employee and period:
  - pay and benefits, gross, natural benefits and deductions
  - withholding basis, table number or percentage, and forskuddstrekk
  - utleggstrekk and the payout date
  - hours for hourly staff (per day, according to B §10.2)

  This applies to F-KJO-42 and F-KJO-45.
- **Deductions need a legal basis** (aml. § 14-15 (3) a–f).
  - Agreed deductions respect a protected amount (§ 14-15 (4)).
  - A negative correction without a written agreement becomes a receivable, not a deduction (HR-2021-2532-A).
  - This applies to F-KJO-05, F-KJO-32 and TRK.
- **Forskuddstrekk (skattebetalingsloven ch. 5 and the forskrift):**
  - follows the tax card, table or percentage, with half tax in December and the June exemption
  - 50 % when the tax card is missing
  - capped at the cash amount
  - summed per payout date and paid on the first working day after payout (2026 rule)
  - whole kroner in the a-melding
  - Over-withheld tax may only reduce later withholding in the same year, or must be repaid before 31 January (C §2.4).
- **AGA:**
  - per sub-unit zone and month, including natural benefits and the pension premium, minus NAV refunds with one method
  - fribeløp in zone 1a
  - must be specifiable per rate and zone (bokføringsforskriften § 3-1 nr. 9)
  - AGA on the OTP premium must be in the a-melding when the customer has OTP (R3 D-01)
- **Holiday pay (ferieloven § 10 and § 11):**
  - 10.2 % by law, or 12 % by agreement
  - the basis is pay paid in the earning year
  - the 60+ supplement is 2.3 percentage points, and the 6G cap applies only to the supplement
  - paid out before the holiday, and at termination
  - always reported as trekkpliktig (subject to withholding)
  - ferietrekk is reported as negative trekkILoennForFerie, together with an unreduced fixed salary
- **Net ≥ 0** for every person in every run (C §2.4).
- **A-melding fields that LON/KJO supply:**
  - `inngaarIGrunnlagForTrekk`, `utloeserArbeidsgiveravgift` and `fordel` on every income line
  - `sisteLoennsendringsdato` (F-LON-14)
  - bilOgBaat for company cars
  - corrections sent as a replacement message for the affected month (F-KJO-28)
- **Documentation integrity:**
  - approved runs and payslips are never altered; corrections are new lines (F-KJO-25)
  - 5-year retention, stored in Norway (B9; F-KJO-44)
- **Overtime** is at least 40 % (aml. § 10-6 (11)), if the pay type is used for overtime.
- **Special categories (GDPR art. 9).** Sick-pay and union-dues lines must be masked for roles without access (`sarlig_kategori`) from the first pilot (M1).

## 8. Open questions (`sporsmal`) touching LON/KJO, and whether they block

| Question (omr-K2/K3) | Owner | Blocks | Proposed default to unblock |
|---|---|---|---|
| Extended pay-type model must be approved (F-LON-02) | Founder | **M0** | Approve the M0 flag set in §2 now; M1 flags later |
| Meaning of ten standard pay types 1001, 1002, 2001, 2002, 2028, 3008, 3009, 3016, 6002, 6011 (F-LON-01) | Founder | **M0** only for those used in own payroll; **M1** for the rest | Sjur fills them in from his A07 mapping |
| How the OTP premium comes in, and AGA on it (F-PEN-05/06) | Auditor/Skatteetaten | **M0** if the M0 employer pays OTP premium; **M1** | Manual premium per month, AGA in the payment month (night-work proposal for F-PEN-06/GC-17 in `natt/morgen.md`) |
| Licence for Skatteetaten's trekkrutine (F-TRK-07) | Skatteetaten | Does not block if we decide on an **own Rust port** verified 100 % against the table file (N13). Send the licence request anyway | Decide "own port" now |
| Rounding of percentage withholding and net pay (F-KJO-17) | Skatteetaten | **M0**, for øre equality | Base and amount rounded down to whole kroner (§§ 5-10-4, 5-5-4), union dues in the base rounded up, AGA rounded down once per opplysningspliktig and month (§ 10-4-4), as in PLAN §1.4; confirm in the letter to Skatteetaten and verify the F185 tolerance in test (N13) |
| Table or percent, half tax and June for special cases (F-TRK-08/11/12) | Skatteetaten | **M1** (secondary employment, part-year staff) | Monthly frequency only in M1 |
| Frikort above the limit (F-TRK-10) | Skatteetaten | **M1** | 50 % above the limit, flagged |
| Utleggstrekk that cannot be taken in full; bidrag channel and code; standard protected amount | Skatteetaten/lawyer | **M1** (TRK) | Carry forward with deviation; manual register; living-cost rate + housing allowance |
| What the "4/26" holiday-deduction method means (F-KJO-39) | Founder | **M1** | One method per entity: 12/260 per working day or 1/26 per weekday |
| Which G applies to the 6G cap, wage guarantee and pension (F-KJO-37) | Payroll | **M0+ track** (60+ cap, gate JUN27); not blocking | For the 60+ supplement: the G in force on 31 December of the earning year (ferieloven § 10 (3)); for June 2027 that is the G of 31.12.2026 (PLAN JUN27). This paper first proposed "G at payout date"; Plan v1 replaces it |
| Default for retro of ferietrekk (F-KJO-26) | Payroll | Does not block (LATER) | – |
| Reporting of salary advances (F-KJO-31) | Payroll | Does not block (CUT) | – |
| Pay settlement as core or HR module (F-LON-22–31) | Founder | Does not block | Answer: HR module, CUT for now |
| Ownership of D-Tariffavtale and of the AGA calculation | Technical | Does not block, but **decide for M0 module boundaries** | KJO computes AGA, ORG owns zone per sub-unit, MYN reports |
| Net pay and PAYE in the a-melding (F-KJO-33) | Skatteetaten | Does not block (CUT) | – |
| Which tariffs to support first (K3/TID) | Founder | Does not block M0/M1 | Pilots decide; likely Virke HUK |
| Holiday for part-time and turnus staff: days or hours (K3/FRA) | Payroll | **M1** partly (part-time ferietrekk); turnus is out of scope | Days for part-time staff with a fixed weekly pattern |
| design.json: who are payroll experts no. 1 and 2? | Founder | **M0/M1** golden cases and rule-pack review | Sjur signs M0 fasit (reference answers); buy external hours for M1 |

New questions this review raises:
- **Will Brutto send the Nov/Dec 2026 a-meldinger, or shadow-run until 1.1.2027?** This decides whether the 2026 sammenstillingsoppgave (D-27) and mid-year migration belong in M0. **Answered by PLAN D1/B44:** shadow runs; the current system submits all of 2026.
- **Does the M0 employer have OTP with an employee contribution, any EK or car benefit, or an hourly employee?** This decides which pay types and steps M0 needs. **Blocks M0 scope.**
- **SoD conflict.** "Nobody approves their own pay" (R3 D-47) cannot be met by a three-person team that is all paid in the same run. Confirm the logged exception plus the board-chair report. **Blocks M0 approval design.**

## 9. Biggest risks
1. **Calendar.** November payday is about 3–4 weeks away, and the a-melding is due 7.12.2026. A correct engine, withholding port, AGA, holiday accrual, payslip, pain.001, voucher and a-melding is only realistic as a shadow run. PLAN D1/B44 settles it: Brutto submits no 2026 period, and the first live period is 2027-01 (§2).
2. **Table withholding.** The licence is unresolved. A Rust port must reproduce Java's `f64` evaluation order, otherwise it is 1 kr off in 60 of 1.09 M rows (N13). The 2027 routine arrives in early December, so a new port check is needed before the January 2027 run.
3. **Pay-type flags and catalogue.** B5 is not approved, and 10 of the 26 standard pay types are undefined. Wrong flags give wrong withholding, AGA and a-melding on every line.
4. **Rebuilding the full design inside the "simple" version.** Bitemporality, graph engine, rule-pack workflow and inheritance quietly come back. Mitigation: build a linear pipeline with clear seams and keep the data model to the M0 field lists in §5.
5. **OTP premium and AGA on it.** The question is open. If the M0 employer pays OTP, the M0 AGA is wrong without a manual premium input.
6. **Manual retro and corrections in M1.** Back pay entered by hand can miss the overtime and holiday-basis consequences (R3 D-03). Mitigation: a control that flags pay changes effective before the last approved run, plus a written procedure.
7. **June 2027** is the first real test of holiday pay. It brings ferietrekk, the June exemption, 60+, negative net for new hires and holiday pay at termination, for both own payroll and pilots. F-KJO-37/38/39 and F-TRK-11 must be ready and golden-tested by gate JUN27 (14.5.2027), together with the holiday-pay list F-RAP-11 and the 2026 base import F-MIG-22.
8. **Rounding.** AGA rounding (F185 tolerance) and percentage-withholding rounding are unverified. Øre comparison will expose them, so allow a TT02 test early (N13).
