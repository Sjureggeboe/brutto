# Scope review: REG (accounting and cost allocation) and RAP (reports and analytics)

> Working paper from the scope review of 29.10.2026. PLAN.md is the main plan and `docs/plan/scope.csv` holds the final tier per function; where this paper disagrees, they win.

Reviewer scope: all 64 functions in REG (30, `omr-K4.json`) and RAP (34, `omr-K6.json`), their entities and open questions. The per-function detail is in `docs/plan/scope.csv` (rows with area REG or RAP). Sources: S-avklaringer §6, natt/funn N02, N03, N11, N23, N24, N30, N32, N33, N40, natt/morgen.md item 7, R0-matrix-lonn §7, B-myndigheter §10, design.json B1, B6, B16, B19, B37, B41–B43.

## 1. Tier counts

| Area | Functions | M0 | M1 | M2 | LATER | CUT | Marked "MVP" today | MVP kept in M0/M1 |
|---|---|---|---|---|---|---|---|---|
| REG | 30 | 8 | 4 | 0 | 15 | 3 | 19 | 12 |
| RAP | 34 | 3 | 8 | 0 | 12 | 11 | 13 | 9 (+2 promoted) |
| **Total** | **64** | **11** | **12** | **0** | **27** | **14** | **32** | **21 (+2)** |

- **Demoted from MVP (11):** F-REG-03, F-REG-24, F-REG-27, F-REG-29, F-REG-30 (the old phase-1 A07-vs-ledger product), F-RAP-01 (report engine), F-RAP-07 (dashboards) → LATER; F-RAP-34 (liquidity calendar) → CUT. By the Plan v1 decision after review (dimension sync and cost reporting cut from M1), also F-REG-01 (chart-of-accounts and dimension sync), F-REG-08 (dimension inheritance) and F-RAP-28 (cost per department/project) → LATER.
- **Plan v1 decisions after review (29.10.2026):**
  - The M0 reports are the attestation summary (F-RAP-16, totals including withholding per payout date and AGA per zone), the payroll journal as PDF and CSV (F-RAP-09 = F-REG-06) and one run export as CSV (F-RAP-04). The payment list, withholding list and AGA overview (F-RAP-10, -12, -13) move to M1; in M0 their totals are in the attestation summary and the run export.
  - The holiday-pay list F-RAP-11 is M1, due for our own payroll at gate JUN27 (14.5.2027), not for the January go-live.
  - F-RAP-23 pay statistics is LATER, not CUT: the first pilot above 50 employees needs a pay export by gender and position for the pay-mapping duty (likestillings- og diskrimineringsloven § 26 a).
- **Promoted from "Etter MVP" (2):** F-RAP-16 attestation summary → M0 (it is the same function as F-KJO-22, which is MVP), F-RAP-21 cut-off / pay after end date → M1 (as controls inside F-RAP-14).
- **Duplicates to merge before planning.** The 23 M0/M1 rows shrink to about 12 work items (the dimension and chart-of-accounts pairs below are now LATER):
  - payroll journal: F-REG-06 = F-RAP-09 = F-KJO-45
  - attestation summary: F-RAP-16 = F-KJO-22
  - pre-approval controls: F-RAP-14 + F-RAP-21 = F-KJO-20
  - A07 comparison: F-REG-25 ≈ F-MYN-21 ≈ F-MIG-17, with F-RAP-15 as the report view
  - dimensions: F-REG-08 = F-ORG-18 = F-LON-06 (only F-LON-06 stays, M0, with one flat code in M1)
  - chart of accounts: F-REG-01 ≈ F-ORG-15 (both LATER)
  - OTP: F-REG-14 ≈ F-PEN-05/06
  - retroactive reallocation: F-REG-13 = F-ORG-19
  - liquidity: F-RAP-34 = F-BET-04

## 2. Narrative

**Accounting (REG): payroll needs a voucher, not an accounting integration platform.** M0 needs one balanced voucher (*bilag*) per run. It follows Sjur's standard posting (S #27), uses aggregated net pay on 2930, posts the holiday-pay (*feriepenger*) accrual 5020/2940 and AGA (employer's social security contribution) on the accrual 5405/2785, and has AGA lines per zone and rate. It is delivered as a CSV/JSON file together with the hashed payroll journal (*lønnsjournal*). That covers the law (bokføringsforskriften § 5-6 and § 3-1 (1) no. 9; NBS 2 pt 4.7 per N02/N30) and the parallel run. M0 also needs manual OTP (mandatory occupational pension) premium entry so that AGA on the premium reaches the a-melding (monthly employer report to the authorities). That is F-REG-14, aligned with F-PEN-05/06 in the TRK/PEN review.

M1 adds:
- one adapter, only if a signed pilot needs it (pilot-pulled, PLAN §6.1)
- transfer status with idempotent retry
- automatic reversal
- one flat department/project code per employment, carried to the voucher lines (no dimension sync or cost reporting; Plan v1)
- an A07 comparison of payroll vs the a-melding

Everything that reads the customer's ledger moves to LATER: F-REG-29, F-REG-24, F-REG-30, F-REG-27 and grouping codes F-REG-03.

**Generic file vs Tripletex adapter.** The generic file (F-REG-17) is the baseline in M0 and the permanent fallback. N33 shows that all nine ledgers accept a balanced voucher. N40 shows that Tripletex (T1 "competitive product", T2 "substitutes for … business logic", T11 30-day/at-will termination) and PowerOffice (P1, P2 "strategic and commercial interests") put any adapter at risk exactly where Brutto replaces their payroll modules. M1 should therefore build **one** adapter (F-REG-18), and only after written clearance. A human must send that request now. Pilots must not depend on the adapter. Choose the adapter by the pilots' actual ledgers. ReAi and Fiken have no idempotency key (N33), so they would need a lookup before every write.

**Tripletex posts differently (morgen.md item 7, N32).** Tripletex Lønn posts net pay per employee on 2910, with the employee on almost all lines, and 17 % of its payroll vouchers are reversals. Brutto's aggregated 2930 voucher is lawful and better for privacy (S #9). Customers who switch from Tripletex Lønn must:
- turn off Tripletex payroll posting
- have their accountant close the open 2910 items per employee
- expect Tripletex's own "Avstemming" module to show deviations for clients with an external payroll system (N33)

This last point is the main reason M1 still needs a small reconciliation report of its own (F-RAP-15 subset).

**A07-vs-ledger reconciliation (F-REG-27/29/30) is LATER, as a separate product line.** It was the narrow phase-1 product, and B37 merged it into the MVP. It is valuable for accounting firms (*byrå*) across *any* payroll system (N11), but it is not needed to run payroll, and it carries the heaviest baggage:
- ledger reads under restrictive API terms (N40 T1–T7)
- a balance engine that removes reversal pairs (N32)
- a 280-rule A07 mapping (N23)
- the kontrolloppstilling (payroll reconciliation statement), which is filed by year-end tools anyway (N24)

What stays core is **payroll vs a-melding vs A07** (F-REG-25 with F-MYN-21/F-MIG-17). It is the vendor-neutral source of truth for migration and parallel run (B16) and checks Brutto's own a-meldings. It needs no ledger access. **Recommendation:** revise B37 so that "A07 reconciliation" means A07 vs payroll in the MVP and A07 vs ledger later. PLAN §8 does this (B37 reworded, new B46).

**Holiday-pay accrual and AGA on it** is M0 and simple: always per run, at the sub-unit's zone, with a manual year-end true-up from the holiday-pay list. Drop the per-run/monthly/annual options and the automatic 2785 clearing.

**OTP from invoice:** payroll posts nothing (S #29). The only lawful requirement is that the premium per termin enters the AGA base and the a-melding. That is one number per termin, entered by hand. This is M0, because the M0 employer (PLAN D2) very likely has a mandatory OTP scheme; verify this. It is M1 at the latest.

**Reports (RAP): use fixed reports, not a report engine.** Matrix ships "fixed reports, no builder" (R0 §7.2). Build each legally needed or safety-critical report as an API endpoint returning CSV/PDF behind the normal role check. Defer the generic engine (F-RAP-01, D-Rapportdefinisjon with 34 fields), report snapshots/signing (F-RAP-03) and suppression (F-RAP-02). Cut the builder, BI feed, scheduling, budget, forecast, cost-of-hire calculator, settlement simulation, ESG and pay-transparency features until a paying customer asks.

## 3. Entities needed for M0/M1 (and what to trim)

The REG- and RAP-owned entities have 15 entities and about 305 fields. The proposal keeps 7 entities with about 70 fields. All RAP-owned entities drop out of M0/M1.

| Entity | Owner | Tier | Keep (M0/M1) | Trim / over-engineering |
|---|---|---|---|---|
| D-Bilag (27 fields) | REG | M0 | id, ekstern_referanse, juridisk_enhet, type (only `loenn`/`korreksjon`/`reversering`), lonnskjoring_ref, revisjon, bilagsdato, periode, periodeaar, beskrivelse, sum_debet, sum_kredit, vedlegg_ref, vedlegg_hash, status; M1 adds regnskap_bilagsnummer/-id, overfoert_tid, feilmelding, reverserer_ref/reversert_av_ref | 8 of 11 `type` values (avsetning, periodisering, omfordeling, betaling, aga_termin, refusjon_nav, otp_aga, aarsslutt); utlost_av_fordeling_ref; foreslaatt_periode; valuta (always NOK) |
| D-Postering (18) | REG | M0 | bilag_ref, linjenr, konto, debet_kredit, beloep, beskrivelse, dimensjoner (M1), lonnsart, kilde, sone, sats | grupperingskode snapshot, ansatt_ref (no sub-ledger), linjekontering_refs, mengde, skjermet (true by construction), ekstern_ref |
| D-Kontomapping (18) | REG | M0 | objekt_type (6 values: lønnsart, trekk, aga, aga_feriepenger, avsetning_feriepenger, netto), objekt_ref, juridisk_enhet, debetkonto, kreditkonto, gyldig_fra, endret_av, endret_tid | 4-level `nivaa` inheritance (brutto_mal/kjede/byraa/kunde) → only default + customer; laast_av_mal, malversjon, eier_ref, 5-value dimensjonsregel (M1: inherit or none), fast_dimensjon, skjermet |
| D-Regnskapskonto (20) | REG | M0 (seeded) / M1 (entered per customer; import with F-REG-01 is LATER under Plan v1) | juridisk_enhet, kontonummer, navn, aktiv, ekstern_id, sist_synket; M1 krever_avdeling/krever_prosjekt if the adapter returns them | standardkonto, grupperingskategori, grupperingskode(+_kilde), saldo, saldo_dato, reskontro, krever_fri_dimensjon, sensitiv, sensitivitetsgrunn (all serve LATER reconciliation or are true by construction) |
| D-Regnskapsoppsett (18) | REG | M1 (M0 hard-coded) | juridisk_enhet, integrasjon_ref (adapter or file), bilagsserie, loennsjournal_vedlegg (full/none), gyldig_fra | 11 option fields become fixed defaults: bilagsdato_regel, aggregering, avsetning_feriepenger, aga_av_feriepenger, periodisering_paa, betalingsbilag_i_brutto, omklassifiser_forskudd, feriepenger_kontering, standard_dimensjoner, sensitive_kontoer; aga_refusjonsmetode duplicates D-Lonnsinnstillinger (MYN) |
| D-Avstemming (28) | REG | M1 (simplified) | opplysningspliktig, periode, avstemmingsrapport_ref, sum_loenn_system, sum_amelding, status (open/reconciled), avstemt_av, avstemt_tid | hovedbok/bank/Skatteetaten sums, saldo_2600/2610/2770/2930/2940, aga_frigitt(+tid), overstyrt_begrunnelse, kontrollert_av/tid (four-eyes), pakke_pdf/csv, gjenaapnet_aarsak |
| D-Avstemmingslinje (17) | REG | M1 (simplified) | avstemming_ref, kontrollpunkt, dimensjon_type/verdi, person_ref, verdi_loenn, verdi_amelding, differanse, forklaring, forklart_av/tid | verdi_hovedbok, verdi_bank, verdi_skatteetaten, 6-value differansetype taxonomy, kontrollsak_ref |
| D-Linjekontering (16) | REG | **CUT for M0/M1** | Put konto + 1–2 dimension columns on D-Lonnslinje. The approved run is immutable (B6), so the posting is frozen anyway | Whole entity: segment split, percentage shares, largest-remainder, regelkilde, validation flags (keep the design note for LATER) |
| D-Periodisering (17) | REG | LATER | – | – |
| D-Rapportdefinisjon (34) | RAP | **CUT for M0/M1** | Reports as code | dataklasser, minste_gruppestorrelse, sekundaer_undertrykking, planlegging, abonnenter, dashbord_roller, eier_type/arvet_fra, versjon… |
| D-Rapportkjoring (26) | RAP | LATER | M0/M1 stores generated documents (journal, payslips, voucher file) as files with SHA-256 on the run | Snapshot/signing/as-of reproduction |
| D-Budsjettlinje (19), D-Prognosescenario (17), D-Verdigruppe (13) | RAP | CUT | – | – |
| D-Tilskuddsprofil (17) | RAP | LATER | – | – |

**Other areas' entities consumed by REG/RAP M0/M1:**
- D-Lonnskjoring, D-Lonnslinje (+ account/dimension columns), D-Lonnsart, D-Lonnsslipp, D-Skattekort, D-Akkumulator / D-Feriesaldo (holiday-pay basis incl. migrated year-to-date), D-AMelding, D-Underenhet, D-Virksomhet
- D-Betalingsoppdrag / D-Betalingslinje / D-KID (payment list, trekk)
- M1: D-Avstemmingsrapport (A07), D-Integrasjon (one adapter, pilot-pulled), D-Dimensjonsverdi / D-Dimensjonstype (flat lists), D-Kostnadsfordeling (single value per employment), D-Pensjonspremie (premium amount per termin), D-Trekkpalegg, D-Avvik (one deviation list; merge D-Kontrollsak into it)
- D-Sammenstillingsoppgave (MYN, 17 fields): M1 needs only data + PDF. Keep `maaneder_annet_system`, because systems change mid-year. Keep `kanal`: Plan v1 delivers the statement through Digipost (bought), with print fallback.

## 4. Top cuts (biggest effort saved)

1. **A07-vs-ledger product line out of the MVP** (F-REG-29, F-REG-30, F-REG-24, F-REG-27, F-REG-03 → LATER). This removes ledger reads, the balance engine with reversal pairs, the 280-rule mapping and the four-eyes package with AGA lock, and it takes the Tripletex/PowerOffice terms off the critical path. Revise B37.
2. **No report engine** (F-RAP-01 LATER, D-Rapportdefinisjon cut). Use fixed reports as API endpoints instead.
3. **Builder, BI feed, scheduling, dashboards** (F-RAP-06, F-RAP-08, F-RAP-05 cut; F-RAP-07 later).
4. **Budget, forecast and simulation** (F-RAP-30–34 cut). These also remove D-Budsjettlinje and D-Prognosescenario.
5. **Only one accounting adapter**, and only if a signed pilot pulls it (PLAN §6.1; second in the M1 cut order, §6.3). PowerOffice and Xledger come later; Visma and Fiken are cut (F-REG-19–22). The generic file is the fallback.
6. **Allocation engine** (D-Linjekontering cut; F-REG-13 later). This paper reduced F-REG-08 to one dimension value per employment; under Plan v1 F-REG-08 is LATER and the one flat code rides on F-LON-06.
7. **Option sprawl in D-Regnskapsoppsett.** 11 settings become fixed defaults.
8. **HR, ESG and transparency analytics** (F-RAP-22–27 later or cut; D-Verdigruppe cut).
9. **Payment vouchers and the AGA lock** (F-REG-09 cut; AGA hard lock replaced by a warning).

## 5. Legal must-haves (cannot be cut for the M0/M1 profile)

| Requirement | Source | Function(s) | Tier |
|---|---|---|---|
| Payroll documentation per recipient and period, issued no later than payout: fødselsnummer (national ID number), name, table number or percentage, gross, benefits in kind, deductions, trekk basis, trekk; utleggstrekk (enforcement deduction) details; hours per day for hourly paid staff | bokføringsforskriften § 5-6 (B §10.2) | F-REG-06 / F-RAP-09 | M0 |
| A short description of how the payroll system is built and works | bokføringsforskriften § 5-6 (B §10.2, R3 D-30) | Static document per release (F-SIK-29) | M0, from the first live month (Plan v1, PLAN §1.4 item 8); this paper first put it in M1 |
| Booked voucher with a two-way audit trail to the journal; payroll-reportable benefits specified per period by account; AGA-liable benefits per sats and sone | bokføringsloven; bokføringsforskriften § 3-1 (1) no. 9; NBS 2 pt 4.7 (N02, N30) | F-REG-05, F-REG-17; AGA per zone and rate in the M0 attestation summary (F-RAP-16) and run export; the F-RAP-13 overview is M1 | M0 |
| Retain journal, vouchers and payment documentation 5 years after year-end, in Norway or with notice; never delete | bokføringsloven § 13; bokføringsforskriften § 7-5/§ 7-7 (open) | F-REG-06, storage (SIK) | M0 (real accounting material from the first run) |
| Holiday-pay liability accrued; basis per employee tracked | Accrual principle (AS); ferieloven § 10 | F-REG-11 (M0); holiday-pay list F-RAP-11 (M1, gate JUN27 for own payroll) | M0 accrual; list by 14.5.2027 |
| AGA on OTP premium included in the a-melding | Folketrygdloven ch. 23; S #29; R3 D-01 | F-REG-14 (+F-PEN-06) | M0 (manual premium entry) |
| Payslip: written statement of pay calculation, holiday-pay basis and deductions | arbeidsmiljøloven § 14-15 (6th paragraph per B §10.1) | KJO/POR (not REG/RAP) | M0 |
| Trekk paid in full and on time; first business day after payout from 2026 | Skattebetalingsloven; B §12 | Withholding per payout date in the attestation summary (F-RAP-16) in M0; the F-RAP-12 list is M1 (payment in BET) | M0 |
| Sammenstillingsoppgave (annual statement) by 31 January (legal basis unverified; treat as legal) | R3 D-36, open question | F-RAP-17 / F-MYN-36 | M1; the first one from Brutto is for our own 2027 payroll, by 31.1.2028 (gate AS27: 14.1.2028; 2026 comes from the current system, B44) |
| No health or union data exposed in the ledger | GDPR art. 9; S #7–8 | F-REG-28 (by construction) | M0 |
| Firm clients: skyldig skattetrekk (withheld tax owed) and AGA reconciled each period | GRFS (E-byra §2.2), the firm's duty | F-RAP-15 subset | M2 for firm clients (the F-RAP-15 subset itself is M1) |

**Not legally required from Brutto, so these can be deferred:**
- dashboards
- liquidity calendar
- basis for notes (the accountant's year-end job)
- kontrolloppstilling (filed in the næringsspesifikasjon, the tax-return business specification, via year-end tools; N24)
- ARP pay mapping (an employer duty; a CSV export suffices)
- auditor package
- budget, forecast, BI, ESG, pay transparency

## 6. Biggest risks

1. **Accounting API terms (N40).** Tripletex T1/T2/T11 and PowerOffice P1/P2 can block or end the M1 adapter at 30 days' notice. *Mitigation:* the file is the baseline; a human sends the written request now; no pilot depends on the adapter; lawyer review.
2. **Unverified posting convention.** The 2930 credit for gross and debit for trekk, and 1580 for refunds, come from C §11.3, not from Sjur's A07 mapping. If wrong, every voucher is wrong. Sjur can settle this in an hour, and it blocks M0.
3. **System switch for our own staff.** PLAN D1/B44 avoids a mid-year switch: the current system submits all of 2026 and issues the 2026 sammenstillingsoppgave, and Brutto starts at period 2027-01 (stretch) or 2027-02 (plan), so no 2026 year-to-date import is needed (with a 2027-02 start, the 2027 months run in the old system are imported and checked against A07). The 2026 holiday-pay basis must still be imported per employee (F-MIG-22), or the 2940 accrual and the June 2027 payout will be wrong (gate JUN27, 14.5.2027).
4. **Cross-area tier gaps that hit M0.**
   - F-MYN-14 (manual-upload a-melding export) was marked "Etter MVP", but it is M0's only filing route. `scope.csv` now has it in M0 (JSON for manual upload).
   - F-BET-03 (AGA per termin) was "Etter MVP"; it is M1 in `scope.csv`. The Nov–Dec 2026 termin is paid from the current system (B44). Brutto's first own termin is Jan–Feb 2027 (only its February part if go-live is 2027-02), due 15.3.2027; until F-BET-03 lands, AGA is paid by hand from the feedback KID and the AGA per zone in the M0 attestation summary (F-RAP-16) and run export (F-RAP-04).
   - F-MYN-36 is "Etter MVP" while F-POR-16 is "MVP".
   - `scope.csv` has F-MYN-14 in M0 and F-BET-03 and F-MYN-36 in M1, which is consistent with this review.
5. **Scope creep through B37.** Keeping "A07 reconciliation + controls + graphs" in the MVP pulls in ledger reads, the balance engine and dashboarding, which is exactly the costly part above.
6. **Tripletex migrations.** Old 2910 per-employee balances and the loss of Tripletex's reconciliation module for clients with an external payroll system (N33) need an onboarding note for accountants.
7. **Hourly staff.** § 5-6 needs hours per day. The input must carry daily hours, or the approved timesheet must be attached to the run.
8. **Storage location (B9 / § 7-5 vs § 7-7).** It must be decided before M0 production, because the M0 journals are retained accounting material.

## 7. Open questions (sporsmal) in K4/K6 that touch REG/RAP

| Question (file, owner) | Blocks? | Recommended answer |
|---|---|---|
| Counter-accounts in Sjur's posting: 2930 for gross and 1580 for refund (K4, Gründer) | **Blocks M0** (2930 part) | Sjur confirms against his A07 mapping. 1580 is not blocking (F-REG-15 is LATER) |
| Grouping codes: two assumed codes and SAF-T relation (K4, Gründer) | No (F-REG-03 LATER) | Park with the A07-vs-ledger line |
| Should the AGA lock be absolute? (K4, Gründer) | No, if cut | Cut the lock; warn 5 business days before the 15th |
| Is the union account (2650) sensitive? (K4, Jurist) | No (aggregated voucher, no employee on lines) | Answer before union dues go through Brutto: M0 if own staff pay dues via payroll (F-TRK-23 is M0 under Plan v1), otherwise M1 |
| Standard AGA method for NAV refund (K4, Gründer; touches F-REG-15, D-Regnskapsoppsett) | **Blocks M1** (sick-leave basics affect the AGA base) | "Deduct when received", as proposed; the receipt is entered by hand (K27 import is LATER) |
| Legal basis, deadline and sender of the sammenstillingsoppgave (K4, Jurist) | **Blocks M1** (Brutto's first statement is for 2027, due 31.1.2028; 2026 comes from the current system, B44) | Treat as legal with deadline 31.1 until answered |
| Annual statement after a mid-year switch (K6, Skatteetaten) | **Blocks M1** for pilots that switch mid-year (window 1.3 or 1.8); not our own payroll (B44) | Full-year statement from A07 + imported YTD |
| One case queue for calculation deviations and authority errors (K4, Teknisk; D-Avvik vs D-Kontrollsak) | M1 design only | Yes, one queue (D-Avvik) |
| Payout date when net is returned or moved (K4, Skatteetaten) | No (voucher date = planned payout date; correct later) | – |
| Minimum group size in statistics (K6, Jurist) | No (statistics LATER) | – |
| Where the report builder ends (K6, Gründer) | No | Resolved by this review: no builder, no OData; the public API covers BI |
| ESG and pay transparency: how much now (K6, Gründer) | No | Only gender and pay-component flags; cut D-Verdigruppe |
| Auditor access: duration and scope (K6, Revisor; F-RAP-19) | No for M0; M1 needs only read-only export access | – |
| Backup in Norway, § 7-5 or § 7-7 (K6, Jurist) | **Blocks M0 production storage choice** | Primary data and backup both in Norway (B9) |

**Related questions outside the area files:**
- fase1.json R01 (which ledger first) blocks the M1 adapter choice. Decide by the pilots' ledgers once written terms are in.
- N40 backlog #1 (written clarification with Tripletex/PowerOffice) blocks F-REG-18 in production.
- P01–P03 are moot under the new direction.

## 8. Minimal report set

All reports are fixed endpoints in the API (B41) returning CSV and/or PDF. There is no report engine.

**M0 (own payroll: shadow runs, then live from period 2027-01 as a stretch, 2027-02 as the planning date).** Plan v1 narrows the M0 set to the attestation summary, the payroll journal and one run export; the separate lists this paper proposed move to M1 (see section 1):
1. Payslip PDF (KJO/POR; arbeidsmiljøloven § 14-15)
2. Payroll journal per run, PDF + CSV, hashed at approval (F-REG-06 / F-RAP-09 / F-KJO-45)
3. Payroll voucher file, CSV/JSON, including AGA per zone and rate and the holiday-pay accrual (F-REG-05 / F-REG-17)
4. Attestation summary: totals vs last month and vs the old system, including withholding per payout date, AGA per zone and the holiday-pay accrual (F-RAP-16 = F-KJO-22)
5. One run export as CSV (F-RAP-04), which carries the payment, withholding and AGA totals in M0
6. Parallel-run diff per employee and pay type vs the old system (MIG; cross-area)
7. Static system description (§ 5-6; F-SIK-29), from the first live month

**M0+ track (own payroll, gate JUN27, 14.5.2027):** holiday-pay list with basis incl. the imported 2026 base, accrual vs 2940/2785 (F-RAP-11).

**M1 adds:**

8. Payment list: net per recipient, masked account, count and sum = pain.001 (F-RAP-10)
9. Withholding list per creditor: forskuddstrekk with KID and due date, utleggstrekk with KID, union dues per union, pension deduction (F-RAP-12)
10. AGA per sub-unit, zone and rate, per month and termin (F-RAP-13)
11. About ten pre-approval controls, including pay after end date, new account numbers and missing tax card (F-RAP-14 + F-RAP-21 = F-KJO-20)
12. Payroll ↔ a-melding ↔ A07 reconciliation per month, with explanation and reviewer (F-REG-25 / F-RAP-15 subset)
13. Annual statement per employee, the basis for the sammenstillingsoppgave (F-RAP-17 / F-MYN-36)
14. Journal/voucher exports for the auditor (through the F-RAP-04 exports; the auditor package F-RAP-19 is LATER)

Payroll cost per department/project (F-RAP-28) was on this paper's M1 list; Plan v1 moves it to LATER with dimension sync.

**Explicitly not in M0/M1:**
- dashboards
- liquidity calendar
- notes basis
- budget, forecast and simulations
- report builder and OData
- HR, sick-leave and ARP statistics (pay statistics F-RAP-23 is LATER, triggered by the first pilot above 50 employees)
- ESG
- signed auditor package
- A07-vs-ledger and bank reconciliation
