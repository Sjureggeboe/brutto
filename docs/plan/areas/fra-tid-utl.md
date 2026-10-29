# Scope review: FRA (holiday and absence), TID (time and working hours), UTL (expenses and travel)

> Working paper from the scope review of 29.10.2026. PLAN.md is the main plan and `docs/plan/scope.csv` holds the final tier per function; where this paper disagrees, they win.

Reviewer: area agent FRA/TID/UTL, 29.10.2026. Source: `analyse/build/data/omr-K3.json` (all 95 functions, 22 entities, 14 area questions), `design.json` (B12, B19, B20, B32, B33, B42, open questions), `R3-kritikk-domene.md` (D-07, D-08, D-11, D-12, b.2.1), `R0-matrix-lonn-omrader.md` (agent K3). One row per function is in `docs/plan/scope.csv` (area FRA, TID or UTL). Its `old_mvp` column keeps the old marking ("MVP"/"Etter MVP" = post-MVP) and `weight` the need weight (Must/Should/Could).

## 1. Tier counts

| Area | Functions | Marked MVP today | M0 | M1 | M2 | LATER | CUT |
|---|---|---|---|---|---|---|---|
| FRA – holiday and absence | 43 | 17 | 0 | 16 | 0 | 24 | 3 |
| TID – time and working hours | 27 | 8 | 3 | 5 | 0 | 12 | 7 |
| UTL – expenses and travel | 25 | 15 | 0 | 7 | 0 | 16 | 2 |
| **Total** | **95** | **40** | **3** | **28** | **0** | **52** | **12** |

M0+M1 is 31 functions against 40 marked MVP today. The 28 M1 functions become about **10 build items**, and the area's data model goes from **22 entities / 539 fields to about 6 stored entities / ~100 fields** (section 5). Ten functions marked MVP move out: F-FRA-36 (permittering counters) from this review, and by the Plan v1 decision after review F-FRA-09 (holiday-days ledger) and the travel-allowance calculation F-UTL-03, -06, -09 to -13 and -17. One function marked "Etter MVP" (post-MVP) moves into M1: F-FRA-23, the printable inntektsmelding basis (Plan v1 review fix). Section 3 lists the post-MVP ones whose *outcome* M1 still needs, done manually or by another function.

**Plan v1 decisions after review (29.10.2026) that change this paper** (PLAN §6.2, §9; `scope.csv` wins):
- **K27 import is LATER.** The NAV refund receivable is entered by hand per sick case, with one AGA method ("deduct when received") and a list of cases near the 3-month deadline (F-FRA-25/26).
- **The holiday-days ledger F-FRA-09 is LATER.** Ferietrekk needs only the method setting.
- **Travel-allowance calculation is LATER.** M1 takes pre-split lines (taxable, tax-free, a-melding code, completeness flag) through the pay-input API, and only if a signed pilot needs them (pilot-pulled, PLAN §6.1). The thin allowance engine below is kept as the design for when it returns.
- **F-FRA-23 inntektsmelding basis is M1** (printable basis for NAV's portal).

## 2. Narrative: the minimal kernel

**Principle.** B20 still holds: the kernel owns the rules with legal effect. For M1, though, the kernel only has to apply them to **facts that arrive already approved** (CSV; the Huma integration is LATER, triggered only when a signed customer needs it, PLAN §9). Self-service, approval flows, counters with no pay effect and NAV automation wait for the modules.

**M0 (own payroll: shadow runs November and December 2026, live from period 2027-01 as a stretch, 2027-02 as the planning date).** FRA and UTL add **nothing** to M0. TID adds three things: the two a-melding working-time fields on the employment (F-TID-01), plus day-level hourly CSV (F-TID-05) and pricing (F-TID-19), but only if the M0 employer has an hourly employee. Before the first shadow run, and again before going live, check these preconditions against A07 and the current system (B19 shadow runs):
1. **Ferietrekk** (holiday deduction from monthly salary) is taken in June, not when the holiday is taken. Otherwise, add one manual negative line.
2. No ongoing **permisjon** (leave) or **permittering** (temporary layoff) is open for own employees in A07. If one is, F-FRA-37 is needed in M0, because ongoing leave must be repeated in every a-melding.
3. No sick pay after the **arbeidsgiverperiode** (AGP, the employer-paid 16 days) and no NAV refund received in a month Brutto runs. If there is one, use a manual pay line and a manual AGA-base adjustment (KJO/MYN). The current system submits all of 2026 (B44), so this matters from the first live period.
4. Mileage or per diem: manual lines on pre-coded pay types, split by hand (in 2026 they are paid from the current system).

**Employer period (F-FRA-21/22).** M1 does **not** need the full state machine with NAV overlap clipping. It needs a *sick case* with AGP start and end, either entered by payroll from NAV's request or confirmed from a simple suggestion (16 calendar days, merge gaps under 16 days). The case shows the first refund day and the claim deadline. Monthly-paid staff keep their salary, so there is no calculation. For hourly-paid staff, Brutto shows the ftrl. § 8-28 average of the last 3 calendar months, and payroll enters the AGP pay line. That is lawful and needs 3 months of income history, which comes from the YTD migration.

**NAV refund and K27: is the domain critic right?** Partly. (Plan v1 narrows the answer below further: K27 import is LATER, see the bullets.) R3 b.2.1 asks for four things: AGP state, a refund ledger with a deadline warning, K27 import and the 48-day holiday-pay accumulator. The law requires two things. AGA (employer's social security contribution) must be reduced by the refund **exactly once**, and AGP must be paid correctly. Losing a refund is a money risk for the customer, not a legal breach. For a pilot with 20–150 employees and a handful of open sick cases, this simpler set is safe:
- **One AGA method for all M1 customers: deduct in the month the refund is received, documented by the K27 import** (F-FRA-26). The deduction then comes only from NAV's own settlement report, so double deduction cannot happen by construction. **Plan v1 decision:** the method stays, but the received refund is entered by hand from NAV's payment information, not imported from K27. Migration guard (as first designed, with K27 import): K27 lines for periods the old system already deducted are marked "excluded"; under Plan v1 the migration checklist lists those refunds instead. This needs the founder's sign-off (open question "Which AGA method is standard?").
- **K27 CSV import** with dedup on report id. Brutto suggests exact matches to open sick cases, and payroll matches the rest by hand (F-FRA-25). **Plan v1 decision: LATER** (trigger: volume in the pilots). M1 has a refund receivable per sick case entered by hand.
- **A deadline list** of sick cases near or past the 3-month refund deadline. This is the cheap part of the critic's ledger and the part that prevents lost refunds.
- **Inntektsmelding (NAV income report) in NAV's portal**, using a printable basis per case (F-FRA-23, M1 under Plan v1; this paper first put it in LATER).
- **Holiday pay on advanced salary: FULL only.** Then no 48-day accumulator is needed (F-FRA-27 → LATER).

What goes: forecast refunds (6G, divisor 260), aging, tolerance auto-matching, partial-payment allocation, June holiday-pay matching, the "advance month" AGA method, and the omsorgspenger (care-day benefit) refund object.

**Holiday.** (**Plan v1 decision:** the holiday-days ledger F-FRA-09 is LATER; ferietrekk needs only the method setting, and holiday days come from the customer's absence source or are entered by payroll. The ledger design below is kept for the absence module.) M1 needs a **holiday-days ledger only**: append-only transactions for entitlement, taken (from imported absence), deducted (by payroll), carried over and manual adjustment. The balance is computed from them, and days are used in a fixed order (Matrix finding). It also needs ferietrekk with one method per employer, collected in June plus at termination, and the holiday part of the termination settlement with written-agreement guards. The year-end job (F-FRA-13) can be manual transactions until December 2027. The egenmelding (self-certified sick leave) counter, care-day quotas, time bank and flex are not payroll and move LATER.

**Leave and permittering in the a-melding (F-FRA-37) is M1 and cannot be cut.** It covers leave over 14 days and all permittering, every month while they last, with the full ID lifecycle and IDs carried over from the previous system. Permittering is entered by hand (notice date, start, %, end of wage obligation, reason). The permittering counters (F-FRA-36), letters and NAV checklist are LATER. Unpaid leave, "stop salary after AGP" and permittering share one deduction function (F-FRA-34).

**Absence via CSV.** One generic CSV template, one source per customer, approved facts only, a fixed list of ~10 types, and corrections after locking as delta lines guarded by aml. § 14-15 (no deduction from pay without written agreement). Huma webhooks are added, together with the pre-cut-off reconciliation (F-FRA-41), only if a signed pilot needs Huma (the LATER trigger in PLAN §9; open question FL11).

**TID: hours for hourly-paid staff.** CSV with one row per employee per work date. Brutto stores the day lines (bokføringsforskriften § 5-6 as cited in R3 D-11) and sums them to pay lines. Source codes map directly to lønnsart (pay type); the hour-type catalogue, schedules, overtime counters, § 10-7 overview, rest-period checks and supplements belong to the time source or the later time module. The open conflict: Matrix/Tidsbanken send **month totals per pay type**. If a pilot's time system can only do that, M1 is blocked until a revisor confirms that day-level records kept in the source, referenced from the pay line, meet § 5-6 (B42 risk). Until then, reject month-only files.

**UTL: is a CSV of already-classified lines enough for M1?** (**Plan v1 decision:** yes. Travel-allowance calculation is LATER, and M1 takes pre-split lines with the a-melding code and the completeness flag, pilot-pulled. The analysis below is kept as the design for the LATER engine and as the reason the completeness flag and code stay mandatory.) Legally yes, with three conditions. The employer is liable for correct withholding no matter which software splits the amount. A source-classified line is therefore acceptable only if Brutto:
1. checks the tax-free (trekkfri) part against Skatteetaten's ceiling × quantity, and moves any excess to taxable with AGA;
2. requires a per-line `reiseregningKomplett` attestation, and holds the line or makes the whole amount taxable when it is missing (skattebetalingsforskriften § 5-6-12);
3. sets the a-melding code and antall (quantity).

That ceiling check is the same arithmetic as doing the split in Brutto. The recommendation is therefore a **thin allowance engine**: domestic tax-free rates only, mileage (car + passenger), domestic per diem with meal deductions, night allowance, private-benefit flag and domestic codes. It accepts gross lines or pre-split lines; for pre-split lines, Brutto checks the split and warns rather than rejects. Only reportable lines enter Brutto. Pure receipt refunds stay with the expense app or accounting (route B), which keeps VAT and receipt archiving out of payroll. The following are LATER: the state-agreement rate tables (the paid amount comes from the source), foreign trips/FX, the 28-day and commuter rules, the travel-claim header entity (D-Reise), receipt hashes, status push, travel advances and VAT.

Plan v1 (PLAN §6.1, §6.2, §9) goes further than this recommendation: no allowance engine and no ceiling check in M1. Pre-split lines (taxable, tax-free, a-melding code, completeness flag) come in through the pay-input API, only for a pilot that needs them, and travel allowances are fourth in the M1 cut order (PLAN §6.3). The employer is still liable for the split, so the pilot agreement must say the source system owns it. The Utleggsappen integration and the thin engine are LATER.

## 3. Post-MVP functions M1 depends on indirectly
- F-FRA-13 year-end job: manual transactions until Dec 2027 (the 2026 holiday year is closed in the current system, B44); it must exist before 31.12.2027.
- F-FRA-24 / F-FRA-33 / F-FRA-28: covered in M1 by F-FRA-34 (deduction), F-FRA-37 (a-melding) and manual NAV portal work, using the F-FRA-23 basis (M1 under Plan v1).
- F-FRA-41: becomes M1 if a pilot uses Huma as absence source.
- F-UTL-21: becomes M1 if a pilot organisation pays volunteers' or board members' travel via payroll (ORL decision).
- **Outside these areas, but blocking M0:** F-MYN-14 (manual-upload a-melding export) was marked "Etter MVP"; `scope.csv` now has it in M0, serialised to the JSON the API takes. F-MYN-35 (K27 vs refund ledger) is "Etter MVP" while F-FRA-25 is "MVP": the same thing marked two ways (`scope.csv`: F-MYN-35 LATER, F-FRA-25 M1 as a hand-entered refund receivable; K27 import LATER).

## 4. M1 build items (what the 31 M0/M1 functions become)
1. Absence import and register, fixed type list, delta corrections (F-FRA-01/02/03/06)
2. Health-data role and masking (F-FRA-05, shared with F-SIK-08)
3. Holiday settings, ferietrekk, holiday in termination (F-FRA-08/14/15; merge with F-KJO-39/34). The holiday-days ledger F-FRA-09 is LATER under Plan v1
4. Sick case with AGP dates, hourly AGP pay helper, printable inntektsmelding basis (F-FRA-21/22/23)
5. Refund receivable entered by hand, AGA "deduct when received", deadline list (F-FRA-25/26). K27 import is LATER under Plan v1
6. Unpaid-leave deduction (F-FRA-34)
7. Leave/permittering in the a-melding (F-FRA-37)
8. Opening balances for FRA (F-FRA-07, inside the MIG framework)
9. Working-time fields on employment (F-TID-01) — M0
10. Hours CSV: day lines, mapping, pricing, lock, delta correction, 100%-absence check (F-TID-05/08/19/20/21/22/23; merge F-TID-19 with F-KJO-09)
11. Pre-split allowance lines, pilot-pulled: intake contract, idempotency, held lines, CSV, a-melding codes, payment route, posting (F-UTL-01/02/04/05/14/18/24; reuse F-KJO-03 idempotency, merge with F-KJO-12). Customer setup, late-change handling and the thin allowance engine (F-UTL-03/06/09–13/17) are LATER under Plan v1

## 5. Entities for M0/M1 and over-engineering

### Area entities (K3): current → proposed

| Entity | Fields now | M0/M1 proposal | Approx. fields | Over-engineering flagged |
|---|---|---|---|---|
| D-Fravaer (absence) | 30 | M1, keep, slim | 15 | Full bitemporal `transaksjonstidFra`, self-service statuses (ONSKET/SOKT), `erHovedferie`, `varsletDato`, `barnRef`, `sykmeldingId`, `arbeidsrelatert` (occupational injury → HEL), `dokumentasjonstype`, `saldokonto`/`ferieAar` (derivable), `godkjenningId` (use batch approval facts) |
| D-Fravaerstype | 24 | M1 as code enum, not a table | ~7 constants | Customer-configurable catalogue: `maksDagerPerAar`, `kreverDokumentasjonFraDag`, `synligForLeder`, `saerligKategoriGrunn`, `rapporteringsgrenseDager`, `navYtelse` |
| D-Feriesaldo (balance ledger) | 27 | LATER with F-FRA-09 (Plan v1); first proposed as an M1 computed view | 0 stored | 27 materialised totals mixing holiday, egenmelding, care days, time bank and flex; `antallBarnIKvote`, `aleneomsorg`, `ekstradagerKroniskSyk` are special-category data with no payroll use |
| D-Saldotransaksjon | 18 | LATER with F-FRA-09 (Plan v1); first proposed as M1, holiday accounts only | 0 (12 when built) | `timeregistreringId`, `godkjenningId` (four eyes) and `importjobbId` can wait; keep `reversererTransaksjonId` |
| D-Ferieprofil | 21 | M1 as 3 settings (employer + employment override) | 3 | Statutory constants stored as config (`hovedferieFra/Til/Dager`, `varselMaanederFor`, `maksOverforing`, `maksForskudd`, `nyansattFristFullFerie`); tariff level |
| D-Sykefravaerstilfelle (sick case) | 32 | M1, slim | 11 | NAV request fields (`navReferanseId`, `forespoerselStatus`, `inntektPaakrevd`…), `naturalytelserBortfall`, `refusjonsendringer`, `redusertLoennIAgp*`, `maksdato`, `endringsaarsaker` → LATER with the inntektsmelding API |
| D-Permisjon (leave/permittering) | 24 | M1, keep a-melding fields | 16 | `lonnspliktDagerBrukt`, `ukerUtenLonnspliktSiste18Mnd`, `forventetSluttdato`, `navMeldingSendtDato`, `varselbrevDokumentId`, first/last reported month (derivable) |
| D-Refusjonskrav + D-Refusjonsavstemming | 28 + 22 | M1 as one refund receivable per sick case, entered by hand (Plan v1; K27 import LATER) | ~10 | Two entities plus D-NavRapportlinje (K4) model the same K27 row. `omsorgspengerFravaer` object, `kanal`, `harUtbetaltPliktigeDager`, aging statuses, `agaMetode` per claim |
| D-Timeregistrering (hour line) | 32 | M0/M1, slim | 14 | Overtime fields (`overtidPaalagtAv`, `overtidBegrunnelse`, `forhaandsgodkjent`, `frivilligUtoverRamme`, `kompensasjonsvalg`), `kostprisSnapshot`, `registrertMedStempling`, separate `aktivitet`/`finansior` refs (use the generic dimension list) |
| D-Timetype | 20 | CUT; map to D-Lonnsart | 0 | Tariff time windows, weekdays, holiday flags duplicate lønnsart |
| D-Arbeidstidsordning | 32 | M0 as 2 fields on D-Stillingsperiode | 2 | Overtime limit profiles, rest periods, night window, averaging, flex core time |
| D-Arbeidsplan (work schedule) | 21 | LATER | 0 | Rotation, publication, shortened days |
| D-Utleggslinje (expense line) | 39 | M1, slim | 20 | Currency trio, `foreslatt`, `kvitteringer` hashes, `mvaKode`, `engasjementId`, `betalingsstatus`/`rapporteringsstatus` (derive from run), JSON-schema `fakta` |
| D-Reise (travel-claim header) | 33 | LATER; 4 facts move onto the line | 0 | Stores third-party names (`passasjerer`, `deltakere`) in payroll — data minimisation issue; `pendlerPersontype`, `oppholdOver28Dogn`, trailer/forest-road km, travel advance |
| D-Godtgjorelsessats (rates) | 23 | LATER with travel-allowance calculation (Plan v1); first proposed as M1, slim | 0 (10 when built) | State-agreement and customer-policy series, per-country rates, separate meal-deduction fields |
| D-Utleggskategori | 13 | CUT for M1 | 0 | VAT rules and accounts per category belong to the expense app/accounting |
| D-Utleggsoppsett | 15 | 1 setting on employer | 1 | Run frequency, amount limits, receipt copy, notification recipients |
| D-Godkjenning (approval) | 25 | LATER (design now) | 3 on import batch | `signaturHash`, `beloepEstimat`, `avviksflagg`, `dyplenke`, levels and delegation |
| D-Egenmeldingspolicy, D-Sykmelding, D-Sykepengesoknad | 20 + 25 + 15 | LATER | 0 | D-Sykmelding would store doctor name/phone and free-text prognosis — minimise even when built |
| **Total K3** | **539 fields, 22 entities** | | **~100 fields, 6 stored entities + enums/settings** (first proposal ~120 fields, 8 entities; Plan v1 moves D-Saldotransaksjon and D-Godtgjorelsessats to LATER) | |

### Entities from other areas that M0/M1 here depends on
D-Arbeidsforhold, D-Stillingsperiode (+2 working-time fields), D-Lonnsart (pay types with a-melding code and flags, including allowance pay types), D-Lonnsgrunnlag, D-Lonnslinje, D-Lonnskjoring, D-Akkumulator (3-month income for § 8-28; YTD), D-Importjobb, D-Mappingregel (**one** mapping entity with source context and version; Matrix found three overlapping ones), D-NavRapport (K27 file; LATER with K27 import under Plan v1), D-AMelding, D-Virksomhet (holiday and AGA-method settings), D-Kostnadsfordeling/D-Dimensjonsverdi, D-Avvik (held lines). D-Kilderegister can be a single setting per customer in M1.

## 6. Top cuts (and LATER items that save the most)
1. **Self-service and approval layer** (F-FRA-10/11/32/38/39/42/43, F-TID-04/09/16/20 UI): everything arrives approved; D-Godkjenning is designed now and built later.
2. **NAV automation**: sykmelding API, inntektsmelding API, refund forecasts, omsorgspenger refunds, the 48-day accumulator (F-FRA-20/24/27/30; F-FRA-23 keeps only the printable basis, M1). M1 uses NAV's portal, a hand-entered refund receivable and a deadline list (K27 import is LATER under Plan v1).
3. **Working-time law engine** (F-TID-02/06/10–13/18, D-Arbeidstidsordning, D-Timetype, D-Arbeidsplan): it belongs in the customer's time or shift system until the own time module ships. Rest periods, averaging, supplements and staffing are cut outright.
4. **Generic balance ledger**: egenmelding counters/policies, care-day quotas, time bank, flex (F-FRA-17/18/19/29, F-TID-14–17). The ledger is for holiday days only, and under Plan v1 that ledger (F-FRA-09) is LATER as well.
5. **Full allowance engine**: D-Reise, state-agreement and foreign rates, 28-day/commuter rules, receipt hashes, VAT, travel advance, status push (F-UTL-07/15/16/20/22/23). This paper proposed a thin engine for M1; under Plan v1 the whole calculation is LATER and M1 takes pre-split lines only.
6. **Source switching with shadow periods** (F-FRA-04, F-TID-24, F-UTL-08): one source per data type in M1.
7. **Research/project niche** (F-TID-26/27 cut; F-TID-25 LATER).

## 7. Legal must-haves for the M0/M1 profile (cannot be cut)
- **A-melding arbeidsforhold fields**: `arbeidstidsordning` and `antallTimerPerUkeSomEnFullStillingTilsvarer` on every employment (F-TID-01) — M0.
- **Leave and permittering in the a-melding**: leave over 14 days and all permittering, repeated each month while ongoing, correct ID lifecycle, IDs carried over from the previous system (F-FRA-37). Store the new permittering fields (`varslingsdato`, `sluttdatoLoennsplikt`, `permitteringsaarsak`) from day one.
- **Hourly-paid documentation**: hours per day and total per period (bokføringsforskriften § 5-6 as cited in R3 D-11) (F-TID-05). Day lines are kept 5 years (bokføringsloven § 13).
- **AGP pay**: 16 calendar days paid by the employer; hourly-paid paid from the § 8-28 average (ftrl. §§ 8-19, 8-28) (F-FRA-21/22).
- **AGA**: a NAV refund reduces the AGA base once, never twice (F-FRA-26).
- **Holiday**: ferieloven § 5 entitlement incl. 60+; ferietrekk for monthly-paid; holiday pay settled at termination; deduction for advance holiday only with written agreement (ferieloven § 7, aml. § 14-15) (F-FRA-08/14/15; with F-FRA-09 LATER, holiday days come from the customer's source or are entered by payroll).
- **No set-off or negative correction from net pay without written agreement** (aml. § 14-15 second paragraph letter c, HR-2021-2532-A) for absence, hours and expenses (F-FRA-06, F-TID-21, F-UTL-06).
- **Unpaid leave**: no holiday-pay accrual on the deducted salary (F-FRA-34).
- **Travel allowances**: tax-free part has no withholding or AGA and is reported with code and quantity; the excess is taxable with AGA; an incomplete travel claim makes the whole amount taxable (skattebetalingsforskriften § 5-6-12); employer-covered private cost is a taxable benefit (F-UTL-09–14/17). Under Plan v1 the split comes pre-made from the source; Brutto requires the code, quantity and completeness flag on each line (F-UTL-01/14), and the employer stays liable for the split.
- **GDPR art. 9**: absence type, sick pay, K27 lines and parental leave are health data. They need a restricted role and masking, a DPIA, and no diagnoses or health free text (F-FRA-05).

## 8. Biggest risks
1. **Double or missed AGA deduction at migration.** The pilot's old system used the "advance month" method and the refund arrives after go-live. Mitigation: one method ("deduct when received"), and the migration checklist lists the refunds the old system already deducted so they are not entered again (with K27 import LATER, there is no K27 "excluded" flag in M1).
2. **Hourly AGP pay wrong** if fewer than 3 months of income history are migrated. The migration must include the last 3 calendar months per employment, not only YTD totals.
3. **Time systems that send month totals** (Tidsbanken, as seen in Matrix) conflict with § 5-6 day-level documentation, which can block pilots. Get a revisor's answer before choosing pilots.
4. **Utleggsappen has no public API or contract.** Mitigation: CSV is the first client; Utleggsappen later uses the same contract.
5. **Holiday year-end without a job.** Dec 2027 (own company; 2026 is closed in the current system) and the pilots' first December in Brutto need manual carry-over until F-FRA-13 exists; the risk is forgotten forfeits or carry-overs.
6. **Huma as absence source** without webhook retry gives silently missing absences and wrong pay. Mitigation: CSV only in M1, or (once the LATER Huma integration is triggered) Huma plus mandatory F-FRA-41 reconciliation.
7. **Health data in production before the DPIA and role exist.** This is a legal exposure from the first pilot sick leave.
8. **Parental leave paid as salary without a refund claim**: NAV then pays the employee directly, so the employee is paid twice. A manual checklist in M1; the automatic warning comes later.
9. **Lost refunds** (3-month rule) if the deadline list is ignored. The customer loses money, but no law is broken.

## 9. Open questions and whether they block M0/M1

| Question (source) | Blocks? | Recommended answer to unblock |
|---|---|---|
| Which AGA method is standard for NAV refunds? (design #13, B33) | **Blocks M1** | "Deduct when received" as the only M1 method, with the receipt entered by hand (PLAN §10; K27 import LATER) |
| When do the FRA/TID modules come? (design #5) | **Blocks scope** | Kernel rules on imported facts in M1; modules and self-service LATER (this review) |
| How many pilots use Huma? (design #14, FL11) | **Blocks M1 scope of F-FRA-03/41** | Ask in pilot interviews; default CSV only |
| Behandlingsgrunnlag and DPIA for health/union data (design #28) | **Blocks M1 go-live** (not the build) | Advisor sign-off before the first pilot runs |
| Month totals vs day-level hours (B42 risk, Matrix TID) | **Blocks M1** if a pilot's time system sends totals | Revisor: day records in the source + reference on the pay line? Until then require day lines |
| km allowance code and km field in a-melding (K3 UTL) | **Blocks M1** a-melding with mileage (and M0 if the team claims km) | Ask Skatteetaten / test in TT02; default `antall` = km |
| Utleggsappen contract (K3 UTL) | Blocks the Utleggsappen integration only; CSV path not blocked | Publish the CSV/API line format as the contract |
| New permittering fields: from which version? (K3 FRA) | No — store fields regardless | Ask in Skatteetaten's SBS channel |
| Kvitteringsarkiv and VAT owner (K3 UTL, design #31, FL8) | No, if pure refunds stay outside payroll | Brutto never posts VAT; source keeps receipts |
| Kernel as truth for holiday balance (K3 FRA) | No | Yes, Brutto's ledger is payroll truth |
| Holiday for part-time/turnus: days or hours (K3 FRA) | No (no turnus in target) | Virkedager in M1 |
| State rates for passenger/night (K3 UTL) | No (M1 uses only tax-free rates) | — |
| Lønnsplikt counting for partial permittering (K3 FRA) | No (F-FRA-36 LATER) | — |
| Retention for sick notes/applications (K3 FRA) | No (not fetched in M1); fold into DPIA | — |
| § 10-7 fixed plan + deviations (K3 TID, design #24) | No (time module LATER) | — |
| Start/stop in app (K3 TID) | No (cut) | — |
| Which tariffs first (K3 TID) | No (no tariff in M1) | — |
| "4 egenmeldinger per 12 months" (K3 FRA) | No (LATER) | — |
| Which inntektsmeldinger from a payroll system (design #22) | No (portal in M1) | — |
| fase1 G07/G02 (one approval engine; who approves) | No for these areas | Design now, build with modules |

## 10. Cross-area notes
- Duplicates to merge: F-FRA-14 ↔ F-KJO-39 (ferietrekk); F-FRA-15 ↔ F-KJO-34 (termination); F-FRA-25 ↔ F-MYN-35 (K27, marked differently); F-TID-19 ↔ F-KJO-09 (hour pricing); F-UTL-01 ↔ F-PLA-24 ↔ F-KJO-12 (expense intake); F-FRA-03/F-TID-22 ↔ F-PLA-23; F-FRA-20 ↔ F-MYN-33; D-Refusjonsavstemming ↔ D-NavRapportlinje (K4); three mapping entities → one.
- F-MYN-14 (manual-upload a-melding export) was marked "Etter MVP" but is the only M0 submission route. `scope.csv` now has it in M0 (JSON for manual upload).
- M0 needs a manual AGA-base adjustment per zone (KJO/MYN) for the rare refund case, and a manual pay line for any absence effect.
