# Scope review – TRK (tax withholding and deductions) and PEN (pension and insurance)

> Working paper from the scope review of 29.10.2026. PLAN.md is the main plan and `docs/plan/scope.csv` holds the final tier per function; where this paper disagrees, they win.

Reviewer scope: all 46 functions in `omr-K2.json` areas TRK (28) and PEN (18), their entities and the open questions (`sporsmal`) in the K-files that concern them. Per-function detail: `docs/plan/scope.csv` (rows with area TRK or PEN).

## 1. Tier counts

| Area | Functions | Currently MVP | M0 | M1 | M2 | LATER | CUT |
|---|---|---|---|---|---|---|---|
| TRK | 28 | 22 | 10 | 12 | 0 | 4 | 2 |
| PEN | 18 | 7 | 4 | 4 | 0 | 4 | 6 |
| **Total** | **46** | **29** | **14** | **16** | **0** | **8** | **8** |

Movement against the current marking:
- **Promoted from "Etter MVP"** (after MVP): F-TRK-05 manual tax card → M0 (only the manual entry part), F-PEN-16 taxable insurance benefit → M1.
- **Demoted from MVP:** F-TRK-28 deduction balance/carry-forward → LATER.
- **Moved M1 → M0 (Plan v1 decision after review):** F-TRK-23 union dues. Skattebetalingsforskriften § 5-9-1 reduces the withholding base by the deductible dues, so the first live month needs it if any employee pays dues through payroll (PLAN §1.4).
- Everything else marked MVP stays in M0/M1. **The saving in TRK/PEN is mostly depth, not count**: forskuddstrekk (tax withholding), garnishment and pension rules are statutory, so functions cannot be cut. Instead the review cuts entity fields (76 of 161 kept in the TRK/PEN-owned entities, D-Forsikring dropped), API automation (garnishment API, early tax-card polling), configurability (deduction order, protected-amount calculator) and pension scheme breadth (OTP contribution only).

## 2. Narrative

**M0 (Brutto's own payroll: shadow runs for November and December 2026, live from period 2027-01, B44)** needs a small but exact withholding core:
1. A tax card register (F-TRK-01) filled by **manual entry with four eyes** (F-TRK-05). Cards are ordered through Skatteetaten's tax-card file service (RF-1211 format via ID-porten; needs the Altinn package "Lønn"), or copied from the current payroll system for as long as it keeps fetching. Re-checked before every run and for every new hire (PLAN §1.4). No API.
2. Table withholding via an own Rust port of the trekkrutine (Skatteetaten's withholding routine; F-TRK-07), plus percentage withholding by pay-type method (F-TRK-08).
3. The 50 % rule when there is no card, and the January–February fallback to last year's card (F-TRK-03).
4. **Half withholding in December or November** (F-TRK-12). M0's very first (shadow) runs fall in that window.
5. Cap at the cash amount (F-TRK-15) and totals per payout date (F-TRK-16).
6. **Union dues** (F-TRK-23, M0 under Plan v1) if any employee pays dues through payroll: the withholding base is reduced by the deductible dues, rounded up to whole kroner (skattebetalingsforskriften § 5-9-1, within the annual cap [verify the 2027 cap]), and the dues are then taken from net pay.
7. On the pension side (if the M0 employer is OTP-obliged, which is likely with ≥2 people at ≥75 %), a minimal scheme record (F-PEN-01), the pensjonsinnretning (pension provider) org.no. in the a-melding (F-PEN-10), and manual entry of the OTP premium per term (F-PEN-05). That entry drives **AGA (employer's social security contribution) on the premium** (F-PEN-06).

**M1 (pilots)** adds:
- The tax-card API (F-TRK-02/04) with result codes, frikort (F-TRK-10), June rules (F-TRK-11; for own payroll on the M0+ track, gate JUN27 14.5.2027), and per-person aggregation with percent for extra runs (F-TRK-09).
- A **single manual garnishment register** covering samordnet (coordinated), old, and child-support orders, with calculation, reporting and payment (F-TRK-18/19/20/22). The Trekkpålegg API stays LATER because Skatteetaten only opens it after the customer has sent an a-melding through Brutto's API (N26).
- Agreed deductions with a written agreement (F-TRK-24), a fixed legal deduction order (F-TRK-26) and one protected amount per employee (F-TRK-27).
- OTP employee share (F-PEN-03/04/09) and the taxable insurance benefit as a plain pay type (F-PEN-16).

## 3. Recommendation: table withholding for M0 given the licence uncertainty

**Do not wait for, or depend on, the licence.** Implement from the rule and verify against the public tables:

1. **Own crate `brutto-trekkrutine`** (about 150 lines), written from the published rule and constants as described in N13 §1.2. Constants live per income year in D-Regelpakke/D-Sats. Use `f64` with Java's operation order (no `mul_add`, no fast-math). Exact decimal arithmetic misses Skatteetaten by 1 kr in 60 rows (N13 §1.4). `f64` is allowed only in this crate.
2. **Oracle = Skatteetaten's "all tables in one file" text file.** Skatteetaten publishes it for testing payroll systems. The tables are fixed by the Tax Directorate (skattebetalingsloven § 5-1), so they are an authority decision without copyright (åndsverkloven § 14). Store the file with its SHA-256 and gate CI on 100 % row match. Add the N13 §1.5 vectors, including amounts above 200 000 kr, which the file does not cover.
3. **M0 gate:** 100 % match for the monthly period on tables 8000–8400, 9010–9400 and 7150–7170. The full gate (all periods and tables) must pass before M1. The port computes every period anyway. **Plan v1 decision:** the M0 gate is stricter: 100 % match on all rows of the 2026 table file by M0-α (27.11.2026), and of the 2027 file before go-live, as a CI gate (PLAN §3, §5).
4. **M0 fallback** if the port is not green before the November shadow run: look up the text file directly for the monthly period. This is licence-clean and correct up to 200 000 kr per month, which is enough for Brutto's own staff. Percentage cards do not need the routine at all.
5. **Never run the Java code in production.** It has no licence file and no Maven artifact. Without a licence, even using it as a CI oracle is a grey zone, and the text file is enough.
6. **Still send the written licence request** (a human must send it; N13 backlog). It is not blocking.
7. **Year change is the real M0 risk.** The 2027 branch and constants are expected in early December 2026, after the budget agreement. Build regelpakke 2027, re-run the full gate, and only then approve the January 2027 run. Note the difference between tax cards and tables:
   - **Tax cards:** the January–February fallback to last year's *card* is lawful (§§ 5-5-1/5-5-2).
   - **Tables:** there is no such fallback for *tables*. January must use the 2027 rules.
8. **Shadow runs:** compare withholding per employee to the krone against the current system for November and December 2026 (half withholding). The first live period is 2027-01 as a stretch (the planning date is 2027-02); it must pass the 100 % gate on the 2027 table file first (M0-L).

## 4. Entities needed by M0/M1 (and over-engineering)

### TRK/PEN-owned entities

| Entity | Fields now | Keep (M0/M1) | Keep these | Cut or defer (why) |
|---|---|---|---|---|
| D-Skattekort | 24 | 17 | id, person, employer, income year, result (M1), skattekortidentifikator (M1), issued date, received time, deduction code, form, table no., percent, months, free-card amount, tilleggsopplysninger (M1, only to block kildeskatt/Svalbard), source, registered_by | `hovedarbeidsgiver` (**duplicate** of D-Arbeidsforhold.hovedarbeidsgiver; two sources of truth), `bestillingsreferanse` (belongs in D-Skattekortbestilling/D-Innsending), `manuell_prosent`, `manuell_begrunnelse`, `frivillig_tilleggstrekk` (LATER with F-TRK-05 override), `kontrollert_av` (LATER), `gjeldende` (derive; do not store) |
| D-Trekkpalegg | 29 | 17 | id, regime, person, issuer, case no., status, start, end, amount, percent, KID, account, received date, letter document, registered_by, checked_by, end reason | API fields `trekkid`, `trekkversjon`, `sekvensnummer`, `opprettet` (LATER with F-TRK-17), `skyldner_fnr` (**second copy of the national ID number**: privacy risk, use person_id), `trekkpliktig_orgnr`, `betalingsmottaker_orgnr`, `amelding_beskrivelse`, `regnskapskonto`, `prioritet` (all derivable from regime and received date), `saldo_kjent`, `kilde` (manual only in M1). N28's D-Trekkperiode child table: defer until the API |
| D-Trekk | 30 | 17 | id, employment, type, description, agreement document, agreement ref., amount per period, percent, percent base, cap per period, creditor account, creditor KID, priority, individual protected amount, contra account, valid from, valid to | `hovedstol`, `saldo` (F-TRK-28 LATER), `rente` (loan benefit belongs to LON, LATER), `hjemmel` and `amelding_fradrag` (derive from type), `fagforening_navn` (special category; reference a creditor/payee instead), `kreditor_navn`, `avtaledato` (in the document), `vernet_belop_regel`, `fremforing`, `trekk_i_sluttoppgjor` (fixed rules), `aktiv` (derive from dates), `registrert_tid` (system column) |
| D-Pensjonsordning | 22 | 9 | id, employer, provider name, pensjonsinnretning org.no., agreement no., type (one value: otp_innskudd), employee share %, valid from, valid to | `satstrinn`, `lonnsbegrep`, `valgte_kan_lonnsarter`, `arslonnsmetode`, `g_basis`, `tak_g` (constant 12G in the rule package), `minstealder`, `medlemsvilkar`, `premieform` (always invoice), `rapporteringsform`, `rapporteringsfrekvens`, `kostnadskonto`/`egenandelskonto` (belong in REG account mapping). The 8-value type enum (KLP, SPK, hybrid, defined benefit, AFP…) is over-engineering for M1 |
| D-Pensjonsmedlemskap | 15 | 5 | id, employment, scheme, enrolled date, left date (M1; or fold into the employment as an "excluded from" date) | KLP/SPK fields (`stillingskode`, `pensjonsgrunnlag_arlig`, `permisjonskode`, `siste_rapportert_*`), `medlemsnummer_leverandor`, `utmeldingsarsak`, `status` (derive), `egenandel_prosent_overstyring`, `registrert_tid` |
| D-Pensjonspremie | 24 | 11 | id, scheme, term from, term to, payment date, AGA-liable employer premium, employee share, AGA reporting month, zone split (derived, M1), registered_by, a-melding ref. | invoice no./date and voucher refs (accounting adapter, LATER), `reguleringspremie`, `premiefond_bruk`, `administrasjonskostnad` (enter one AGA-liable figure, with the split decided by the accountant), `avstemming_status` (F-PEN-08 LATER), `juridisk_enhet`, `leverandoer_orgnr` (derive), `aga_bilag_ref`, `status` enum |
| D-Forsikring | 17 | 0 | – | **Entity cut.** F-PEN-16 is a benefit pay type plus a recurring fixed line |
| **Total** | **161** | **76** | | |

Cross-cutting over-engineering: every field on these entities, including ids and foreign keys, is marked **bitemporal**. For M0/M1, use append-only versions with `valid_from` and `recorded_at` per row (tax card, garnishment order). Use plain validity for schemes and deductions.

### Shared entities (owned elsewhere) that TRK/PEN M0/M1 depend on
- **D-Person, D-Arbeidsforhold:** the `hovedarbeidsgiver` flag lives here only. M1 adds an optional "excluded from pension" date.
- **D-Virksomhet, D-Underenhet:** AGA zone. M1 needs a zone split for the premium.
- **D-Lonnsart (pay type):**
  - M0: `trekkpliktig`, `trekkmetode`, `halvt_trekk`, and the union-dues deductible flag if dues go through payroll (PLAN D6).
  - M1: `trekkfritak_juni`, `pensjonsgrunnlag` reduced to a boolean, and the new flag `inngar_i_utleggstrekkgrunnlag` (N28).
  - `afp_grunnlag` is LATER.
- **D-Lonnslinje / D-Beregningsspor:** the tax card version used, the effective withholding method, and the deduction-object reference.
- **D-Akkumulator (year-to-date totals):**
  - M0: withholding-liable gross, and withholding per payout date.
  - M1: free card used, pensionable salary.
  - LATER: deduction balance, AFP base.
- **D-Regelpakke / D-Sats (rule package, rates):** table constants per year, the 50 % rate, the free-card limit, the subsistence rate and G.
- **D-Lonnsinnstillinger (payroll settings):** `halvt_trekk_maned` (M0) and `vernet_belop_standard` (M1). **`trekkrekkefolge` is CUT.**
- **D-Lonnsslipp:** must show the table or percent used (M0).
- **D-Avvik (run deviations):** M0 warnings `SKATTEKORT_MANGLER` and `OTP_UTEN_PREMIE`.
- **D-Dokument:** M1, for agreements and garnishment letters.
- **D-KID, D-Betalingsoppdrag, D-Betalingslinje** (owned by BET/MYN): withholding payment in M0, garnishment payments in M1.

## 5. Top cuts (and what replaces them)

1. **Trekkpålegg API** (F-TRK-17) → LATER. A manual register covers every regime. The API cannot be used before the customer's first a-melding through Brutto anyway (N26).
2. **D-Forsikring and the insurance module** (F-PEN-15, F-PEN-17, F-PEN-18) → CUT. The taxable part becomes one benefit pay type.
3. **Pension breadth** → LATER or CUT: KLP file, SPK, provider files, AFP, calculated contribution and premium reconciliation (F-PEN-07, F-PEN-08, F-PEN-11 to F-PEN-14). M1 is OTP contribution only, premium from the invoice, entered manually.
4. **Configurability:** customer-defined deduction order, the family-based protected-amount calculator, per-scheme "maybe pensionable" pay-type lists, and the 8 scheme types.
5. **Deduction balances and carry-forward** (F-TRK-28) → LATER. Fixed amount plus end date is enough.
6. **Special regimes:** Svalbard, Jan Mayen and seafarers (F-TRK-14) and damage deductions (F-TRK-25) → CUT. PAYE/kildeskatt (F-TRK-13) → LATER, with M1 blocking such cards.
7. **Optional legal niceties:** minimum withholding thresholds (F-TRK-15) are optional for the employer under § 5-4-3 → CUT. Per-run withholding override and voluntary extra withholding → LATER.
8. **Table accumulation across several payouts in a month** (F-TRK-09) → LATER. Extra runs use the percentage rate, which § 5-10-1 (3)–(4) allows.

## 6. Legal must-haves

**M0 (cannot be cut):**
- **Withholding follows the tax card:** table, percent or frikort; 50 % without a card; last year's card in January–February (skattebetalingsforskriften §§ 5-5-1, 5-5-2).
- **Half withholding in November or December** for monthly paid employees on 10.5-month table cards (§ 5-7-2).
- **Withholding never exceeds cash pay.**
- **Rounding:** percent withholding and derived table amounts round down to whole kroner (§§ 5-5-4, 5-10-4).
- **Union dues** deducted in pay reduce the withholding base, rounded up to whole kroner (§ 5-9-1), if any employee pays dues through payroll (F-TRK-23).
- **Documentation:** table number or percent is documented per employee and payout (bokføringsforskriften § 5-6) and shown on the payslip (§ 5-10-20).
- **A-melding content:** withholding per income recipient as a negative integer, `sumForskuddstrekkPerLoennsutbetalingsdato`, pensjonsinnretning for OTP-obliged private employers, and `tilskuddOgPremieTilPensjon` (the AGA base for employer-paid pension premium).
- **Payment:** withholding is paid by the **first working day after the payout**. The skattetrekkskonto (separate withholding account) was abolished on 1.1.2026 (B-myndigheter §3). Payment uses KID kravtype 05 with month as the period, as its own payment order to Skatteetaten, not marked SALA. The check-digit algorithm is still open (MYN). For M0, take the KID from the a-melding feedback (upload on payday, then pay); Brutto computes its own KID only in M1, after it reproduces every 2026 KID [verify positions 18–19] (PLAN §1.4).
- **Employee pension share** is deducted before tax and reported as fradrag (deduction), if the own scheme has a share.

**M1 (in addition):**
- **Tax card source:** cards obtained from Skatteetaten (API or portal) for every employee.
- **Frikort and the June exemption** (§ 5-7-1).
- **Garnishments are withheld, reported and paid.** The employer is liable for orders not withheld or not paid (innkrevingsloven § 31; N29). A samordnet order ends old orders (F-TRK-18).
- **Union dues** only with a tariff basis (aml § 14-15 (3) d). They are a special category under GDPR art. 9: restricted access, and a DPIA before pilots go live. (For own payroll the dues rule is already M0, see above.)
- **Agreed deductions** only with a prior written agreement for that specific deduction (HR-2021-2532-A), and only above the protected amount (aml § 14-15 (4)).
- **Taxable insurance premiums** are reported as a natural benefit with withholding and AGA, unless treated as a gift within the 5 000 kr limit.

## 7. Biggest risks

1. **Year change and December in the first two months.** M0 hits half withholding (December shadow run), new tables (January 2027) and the new F532 rule (period 2027-01: the per-date sum cannot be negative) within three runs, and the first live run carries both of the last two. Most systemic withholding errors happen in exactly these months.
2. **Withholding method per pay type is wrong.** A bonus that gets table withholding and is halved in December is the classic error (R3 D-02). It needs the pay-type flags approved by Sjur (blocking question below).
3. **AGA on the OTP premium is missing or mistimed,** so AGA is under-reported every term (R3 D-01). The timing (payment month or invoice period) and whether admin fees are included are still unanswered.
4. **Garnishment liability.** A missed or unpaid order makes the customer liable, with interest from 1.1.2027 (N29). Pilots' first runs must rely on the manual register, which means discipline and four-eyes control.
5. **Data inconsistencies that would produce wrong withholding if built as written:**
   - **Union dues:** C #48 treats them as post-tax, while N13 cites skattebetalingsforskriften § 5-9-1, which suggests a deduction in the withholding base, rounded up. **Resolved in Plan v1:** § 5-9-1 applies; the dues reduce the base (rounded up) and are deducted from net. C #48 is wrong (PLAN §1.4, §7.4).
   - **Pension share placement:** F-TRK-26 puts the employee pension share in the post-tax queue, but it is pre-tax (C §198).
   - **December supplements:** F-TRK-12 says supplements are always withheld in full in December, while N13 reads § 5-7-2 (4) as covering supplements paid with the salary [verify].
   - **Main-employer flag** exists on both D-Skattekort and D-Arbeidsforhold.
   - **D-Trekkpalegg** stores a second copy of the national ID number.
   - The issuer enum value `namsmann` should be `namsfogd` (N28).
6. **API onboarding slip.** If Maskinporten/system user is late, M1 tax cards fall back to manual portal orders for 20–150 employees. That is feasible but laborious, so plan it explicitly.
7. **Pilot selection.** A pilot with KLP/HUK pension, AFP, PAYE workers or seafarers pulls LATER functions into M1. Screen pilots for these.

## 8. Open questions (from the K-files and design.json) and whether they block

| Question (file, owner) | Functions | Blocks? | Recommended handling |
|---|---|---|---|
| Extended pay-type model must be approved (K2, founder; marked "Stopper" in design.json) | F-TRK-08/11/12, F-PEN-03 | **Blocks M0** | Sjur approves the minimum before the November shadow run (M0 scope freeze 13.11.2026): `trekkmetode` and `halvt_trekk` (M0), then `trekkfritak_juni` and boolean `pensjonsgrunnlag` (M1) |
| How the OTP premium comes in, and AGA on it (K2 PEN, auditor; also design.json) | F-PEN-05/06 | **Blocks M0** (if the M0 employer has OTP) | Channel: decide manual entry now. Timing and admin-fee inclusion: ask the accountant/auditor this week; in M0 replicate current practice and compare in the parallel run |
| Licence for Skatteetaten's trekkrutine (K2 TRK; "Stopper" in design.json) | F-TRK-07 | **No**, given §3 | Own port plus text-file oracle; still send the letter |
| Table vs percent, half withholding and June in special cases (K2 TRK) | F-TRK-08/11/12 | M0: no, monthly pay is clear. **Blocks M1 June** (answer needed by May 2027) | Ask Skatteetaten together with the other withholding questions |
| Frikort above the limit (K2 TRK) | F-TRK-10 | No | Use 50 % (Skatteetaten's guidance); verify the legal basis |
| Garnishment that cannot be taken in full (K2 TRK) | F-TRK-20/21 | No | N28: no carry-forward for samordnet; old orders follow the letter |
| Child-support channel and a-melding code (K2 TRK) | F-TRK-19/22 | **Blocks M1 only if a pilot has child-support deductions** | Fetch the utleggstrekk description code list; ask fremtidensinnkreving@skatteetaten.no |
| Protected amount standard (K2 TRK, lawyer) | F-TRK-27 | No | Customer-set amount, default single-person subsistence rate |
| Which G for pension (K2 KJO) | F-PEN-03/09 | No | G at payout; the 12G cap rarely binds for pilots |
| Rounding of percent withholding (K2 KJO) | F-TRK-08 | No, answered | Round down (§§ 5-5-4, 5-10-4; N13 §2) |
| Taxable behandlingsforsikring and group-life threshold (K2 PEN) | F-PEN-16 | No, answered | Taxable from the first krone, can be covered by the 5 000 kr gift limit (N13 §3.2) |
| OTP rates 2026–27 (K2 PEN) | F-PEN-02/09 | No | Validation only: share ≤ 4 % and ≤ employer share |
| KLP/SPK file format and approval (K2 PEN) | F-PEN-11/12 | No (LATER/CUT) | Avoid KLP pilots |
| Net pay agreements and PAYE in the a-melding (K2 TRK) | F-TRK-13 | No | M1 blocks PAYE cards |
| KID check digit and AGA term code (K4 MYN) | F-TRK-16, F-TRK-22 | M0: no, KID from the a-melding feedback. **Blocks automated payment in M1** | Reproduce every 2026 KID first [verify positions 18–19]; test against Skatteetaten's KID generator |
| Are 24.12 and 31.12 working days for the withholding due date? (K4 BET) | F-TRK-16 | Matters for Brutto's first live December (2027) if payday is 23.12 or 30.12; December 2026 is a shadow run (B44). Asked in the letter to Skatteetaten (PLAN §2.3) | Choose a December payday before 23.12 |
| Is the union-dues account 2650 sensitive? (K4 REG); DPIA for union data (design.json) | F-TRK-23 | **Blocks M0 only if own staff pay dues through payroll** (access control on the lines); **blocks M1 union dues for pilots** (DPIA) | Privacy adviser before pilots |
| Test data for garnishment orders (K6 SIK) | F-TRK-17/19/20 | Long lead time for M1 tests | Order now |

## 9. Dependencies on other areas
- **MYN:** the a-melding aggregate (serialised to JSON for manual upload in M0) must carry withholding per date, utleggstrekk (garnishment entries), fradrag (deductions), pensjonsinnretning and the pension AGA base. MYN also owns KID generation.
- **BET:** withholding and garnishment payments as separate payment blocks without SALA (the salary payment code).
- **KJO:** draft recalculation, plus the run control showing the effective withholding method per line.
- **LON:** the pay-type flags listed above.
- **MIG:** opening YTD values for frikort used and withholding, plus open garnishment and deduction orders.
