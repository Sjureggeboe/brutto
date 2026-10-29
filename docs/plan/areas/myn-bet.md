# Scope review: MYN (authorities) and BET (payment and bank)

> Working paper from the scope review of 29.10.2026. PLAN.md is the main plan and `docs/plan/scope.csv` holds the final tier per function; where this paper disagrees, they win.

Reviewer: area agent MYN+BET, 29.10.2026. Source: `analyse/build/data/omr-K4.json` (all 64 functions, not only MVP-marked), entities in `omr-K1..K7.json`, `design.json`, `fase1.json`, research B, R2-myndighetsintegrasjoner, R3, natt/funn N06, N09, N13, N14, N15, N17, N25, N26, N27, N39. Per-function detail: `docs/plan/scope.csv` (rows with area MYN or BET).

## 1. Tier counts

| Area | Functions | M0 | M1 | M2 | LATER | CUT | Currently marked MVP |
|---|---|---|---|---|---|---|---|
| MYN Authorities | 42 | 7 | 18 | 2 | 13 | 2 | 26 |
| BET Payment and bank | 22 | 10 | 4 | 0 | 5 | 3 | 11 |
| **Total** | **64** | **17** | **22** | **2** | **18** | **5** | **37** |

Against the current MVP flag: 33 of 37 MVP functions stay in M0/M1, but almost all of them with a much thinner "simplification". Two MVP functions move to M2, accounting firms (F-MYN-04 agent system user, F-MYN-05 client linking), and two move to LATER (F-MYN-39 Brreg lookup, F-MYN-42 A07 controls). Six "Etter MVP" functions are in fact needed for M0/M1 (section 3).

**Plan v1 decisions after review (29.10.2026) that change this paper** (`scope.csv` wins):
- **F-MYN-20 a-melding 2.4 is M1 with a date**, not LATER: our own payroll must submit period 2028-01 in 2.4, so mapping is due 1.7.2027 and acceptance in test 1.12.2027 (PLAN §1.6, gates 24-S and 24-T).
- **F-MYN-34 K27 import is LATER.** The NAV refund receivable is entered by hand, with one AGA method ("deduct when received").
- **F-MYN-39 Brreg lookup is LATER.** Pilots enter the legal entity and sub-units by hand.
- **F-MYN-37 pay-equity basis is LATER** (same trigger as F-RAP-23), not CUT.
- **Forskuddstrekk KID in M0 comes from the a-melding feedback** (upload on payday, then pay). Brutto computes the KID itself only in M1, after it reproduces every KID the current system used in 2026 [verify KID positions 18–19] (PLAN §1.4).
- **The annual statement goes through Digipost** (bought) with print fallback, like payslips (PLAN §6.2).

M0 MYN: F-MYN-07, 08, 09, 10, 11, 14, 19. M0 BET: F-BET-01, 02, 06, 08, 09, 13, 17, 18, 20, 21. M2 MYN: F-MYN-04, 05.

## 2. Narrative

**M0 needs no government API at all.** The M0 authority path is: Brutto builds the a-melding aggregate (F-MYN-07) → serialises it to the same JSON the API takes → a person with the Altinn 3 access package "A-ordningen" (`a-ordning`) uploads it manually on skatteetaten.no (F-MYN-14) → the feedback is read in the Altinn inbox. The format for 2027 manual uploads (JSON or XML) is a [verify] item in the letter to Skatteetaten; an XML 2.3 serialiser of the same aggregate is the costed fallback (+1–2 weeks). Tax cards are keyed in by hand with four eyes, ordered through Skatteetaten's tax-card file service (RF-1211 via ID-porten, Altinn package "Lønn") or copied from the current system. The bank side is a pain.001 file with net pay (SALA), and forskuddstrekk (PAYE withholding) as its own payment order, not SALA, with the KID taken from the a-melding feedback (Plan v1; this paper first proposed a self-computed KID in M0). That's 17 functions, most of them reduced to a few hundred lines each.

**M1 is where the integrations land:** Maskinporten + a standard system user per direct customer (the accounting-firm agent system user and client linking are M2), REST submission, polled feedback, tax-card API (poll-only), A07 on demand, AGA payment info, union dues and samordnet utleggstrekk (coordinated garnishment) as payment lines, returns, first-payment control, and the annual statement. Everything NAV-API, trekkpålegg-API, bank-message import, open banking and batch firm features is LATER. Under Plan v1, K27 import (even as CSV) and Brreg lookup are LATER too, and the a-melding 2.4 serialiser is a dated M1 item.

**The plan's biggest hidden cost is the data model, not the functions.** The 24 MYN/BET-owned entities have 540 fields. M0+M1 need about 170 of them (section 4). Several entities should not exist as tables at all (D-KID, D-Frist in M0, D-Myndighetsabonnement, D-Kontoendring as separate from D-Personbankkonto).

**Recommended cutover (adopted in PLAN as D1 and the new B44):** run November and December 2026 as a shadow run in Brutto (compare to the øre, B16/B19) and keep the old system as the submitting system and system of record for 2026. Make **period 2027-01** (deadline Friday 5.2.2027) the first a-melding Brutto submits as a stretch (about 40 %); the planning date is period 2027-02 (deadline Friday 5.3.2027), and 2027-03 at the latest. Why:
- you don't need to build an XML v2.3 serialiser, because manual upload moves from XML to JSON after 2026 [verify by 27.11; asked in the letter to Skatteetaten; XML 2.3 stays a costed fallback]
- you don't need a split-year sammenstillingsoppgave (annual statement) for 2026 (R3 D-27)
- F532 applies from 2027-01, so you validate against the rule set you'll live with
- Maskinporten onboarding may be ready by then (7–10 weeks best case from ~2.11.2026)

B44 rules out submitting any 2026 period from Brutto. An XML v2.3 serialiser with XSD validation would only be needed if that ever changed, and Brutto produces no 2026 annual statement.

## 3. Verification of the hints

| Topic | Finding | Consequence |
|---|---|---|
| Onboarding lead time | N06: Digdir terms, Altinn SBS terms, Skatteetaten scopes (via brukerstøtte). No certification for submission, A07 or tax cards. Free. **7–10 weeks from orgnr to first production call** [verify]. Overview says 3–5 months. Queues are likely long around the Altinn II shutdown (17.11 and 31.12.2026). The vendor orgnr is part of the system id (`<orgnr>_brutto`), so changing company later forces every customer to approve a new system user. | API submission is not realistic for the 7.12.2026 deadline. It's likely for period 2027-01 or 2027-02 at best, and Feb–Apr 2027 with buffer. **Pick the vendor company (M02) and owner (M01) this week.** |
| Manual a-melding upload (F-MYN-14) for 2026–2027 | It's in production since 04.06.2026 as a fallback for the "transition period", with no end date announced (B §2.2, R2 row 7). XML is planned "for the rest of 2026", then JSON (Skatteetaten Q&A 18.06.2026, N14) [verify]. It needs one of `a-ordning`, `regnskapsforer-lonn`, the accountant packages or the auditor packages (N25). The English SBS page says "in test" [verify]. A test version with TestID exists (ameldingfilopplasting.skatteetaten-test.no, N39). It's unknown whether it exists for 2.4. | Viable for M0, but it's a transition service and can't be the permanent plan. Build the JSON export, which is the API body anyway. Validate M0 output in the **test** upload during the shadow runs. Confirm that the uploader holds the Altinn 3 package "A-ordningen" for the M0 employer before the first live upload (period 2027-01 or 2027-02) [verify]. For Brutto the 17.11.2026 date only matters if it submits in 2026, which it doesn't (B44); but confirm this week that the current system's submission channel still works after 17.11.2026 (PLAN §1.1). |
| JSON vs XML (B16 note) | Confirmed. The a-melding API only accepts `application/json` per the OpenAPI schema (`AMLD_1047`). XML is only needed for the manual fallback (R2 §3.7 [V]). B-myndigheter §2.1 ("XML in JSON wrapper") is outdated. | One canonical serialiser: JSON 2.3. Drop `xml_eksport_ref` and other XML-centric fields. |
| 2.3 vs 2.4 | 2.4 is mandatory from period 2028-01. Final content 1.4.2027, spec by 1.5.2027, TT02 by 15.9.2027, IT ready by 1.12.2027, first 2.4 deadline 7.2.2028 (N14, B11). The precedent from 2.2→2.3 suggests 2027 periods can still be corrected in 2.3 after 1.1.2028 [verify]. | Keep the aggregate format-neutral from M0. **Plan v1:** the 2.4 serialiser (F-MYN-20) is a dated M1 item on the M0+ track: mapping by 1.7.2027, accepted in test by 1.12.2027, own company submits 2028-01 before any pilot. |
| F532 (from period 2027-01) | Sum forskuddstrekk per lønnsutbetalingsdato (payout date) can't be negative, severity "øyeblikkelig" (immediate). It's still open whether it applies per message or per month. | One message per entity and month, fully replaced (F-MYN-09), plus a trivial M0 check in F-MYN-10. With the 2027-01 cutover (B44), the check is needed from the first real submission. |
| A07 reconciliation (old phase 1) | Same scope as submission. No certification. Order → poll → KLAR. Not idempotent, and 429 on parallel orders (N03, N06). | M1: on-demand fetch for migration and parallel-run verification. The standalone control catalogue (F-MYN-42) is LATER. In M0, download from the portal if needed. |
| Tax-card API | Poll-only from 15.12.2026, with new values `registrertSomDoed` and `trekkEtterReglerOmKildeskattPaaPensjon15Prosent`. `dialogreferanse` becomes obsolete. Max 1 000 fnr per order. The fallback is an RF-1211 XML portal (max 1 MB). | M1, poll-only design from the start. M0 keys cards by hand (from the file service or the current system), including the 2027 cards in December 2026, and re-checks them before every run. |
| K27 (`ref-arbg`) | Since 15.6.2026 it's only available via the NAV Oppgjørsrapporter API or manual download. The CSV is ISO-8859-1 with 12 fields and contains fnr and ytelseskode (benefit code), which is GDPR art. 9 health data (B33, N15). | This paper proposed an M1 CSV upload that keeps only the refund sum per sub-unit and month. **Plan v1: K27 import is LATER** (F-MYN-34); M1 enters the refund receivable by hand. API and per-employee ledger are LATER. |
| Inntektsmelding (income report to NAV) | NAV says only sick pay can be sent from payroll systems (11.6.2026). It needs separate NAV onboarding and special-category access. | LATER. M1 is manual in NAV's portal (B42 already says this). |
| Trekkpålegg API | Strictest API: (1) Brutto must be integrated with Innrapportering A-melding API **and** the customer must have sent at least one a-melding through Brutto, (2) test scope by e-mail, (3) test data made by Skatteetaten, (4) a test summary is needed before production, (5) a signed agreement (R2 §3.5, N26). Orders also arrive as letters in Altinn. | LATER. M1 uses a manual register (TRK) from the letters. Apply once the first API a-meldinger are accepted. |
| Dialogporten feedback | Events need one subscription per client and resource. Polling via `dialogId` from `Leveransebekreftelse` is enough (N25, N27). Brutto must use the `consumerType: Api` URL. | M1 polls. Events are LATER. The `resourceFilter` open question is then not blocking. |
| Deadline calendar | A-melding is due on the 5th (next working day; 5.12.2026 is a Saturday, so 7.12). Forskuddstrekk is due the first working day after each payout. AGA is due the 15th of odd months (15.11.2026 is a Sunday, so 16.11). Skatteetaten's Frister API doesn't cover a-melding. | M0 computes the dates per run. M1 adds a list and reminders. No generic 23-type deadline entity. |
| pain.001 | Bits MIG 2.0 (pain.001.001.09) applies from 19.11.2023. Net pay uses SALA on `PmtInf`. Trekk goes in its own `PmtInf`, never SALA ("Lønn"), with KID as SCOR, otherwise the KID can be dropped (N17, B12). Nordea validates strictly from 9.9.2026. | M0: one bank profile (the team's bank). M1: 2–3 pilot banks. Ask the banks for test files now. |
| Open banking (B40) | No provider supports pure PSD2 bulk salary from all Norwegian banks. ZTL comes closest but uses its own client account, which carries bankruptcy and agent-status risk (N09, N17). | LATER. Keep the payment model channel-neutral. |
| Account-number shield | It's a founder rule that a human confirms account changes (B41, S #24). The quarantine length is still only a proposal. | M0: re-authentication through the identity provider on account change (PLAN §1.3), encryption and read logging, changes listed on the payment proposal. Four eyes on new accounts is listed under M1 in PLAN §6.2. Quarantine, notifications and reconfirmation are LATER. |
| Separate forskuddstrekk payment | The skattetrekkskonto (withholding account) was abolished from 1.1.2026. Withholding is paid by the first working day after each payout, with KID kravtype 05 and the month as term. **KID structure is now documented**: 19 digits, MOD11 check digit, buffer digit in position 18 (N17, Skatteetaten PDFs 2025-10). That mostly closes the K4 open question on the KID algorithm. | M0 must-have. **Simplest lawful rule: pay forskuddstrekk on the payout date itself**, in its own payment block. This avoids the 24.12/31.12 and Easter edge cases. **Plan v1:** the M0 KID comes from the a-melding feedback (upload on payday, then pay); Brutto's own KID only in M1 after it reproduces every 2026 KID [verify positions 18–19]. |

### Functions marked "Etter MVP" that M0/M1 actually need
- **F-MYN-14** manual-upload export → **M0**. It's the only M0 submission route.
- **F-MYN-34** K27: this paper proposed M1, as a CSV upload that stores sums only. **Plan v1: LATER**; the refund receivable is entered by hand, so it is not counted among the six.
- **F-MYN-36** sammenstillingsoppgave → **M1**. It's a legal statement; the first one from Brutto is for our own 2027 payroll, due 31.1.2028 (gate AS27: 14.1.2028).
- **F-MYN-41** contingency → **M1**, as a runbook only.
- **F-BET-03** AGA per term → **M1**, showing AGA from the feedback with an optional payment line.
- **F-BET-05** creditor, union and garnishment payments → **M1**.
- **F-BET-16** returned payments → **M1**, as manual re-issue.

### MVP-marked functions pushed down
- **F-MYN-04, F-MYN-05**: the agent system user and client linking are **M2** (accounting firms, B45). F-MYN-05 in M2 is portal linking, with no client-delegation API.
- **F-MYN-20**: this paper put the 2.4 serialiser in LATER with a hard date. **Plan v1: M1 with a date** (mapping 1.7.2027, test 1.12.2027). Format neutrality stays a design rule now.
- **F-MYN-39**: Brreg lookup at onboarding is **LATER** under Plan v1 (pilots enter the entity by hand).
- **F-MYN-42**: the A07 control catalogue is LATER.
- Within MVP functions, these parts are cut or postponed: the file-upload API (F-MYN-12), Altinn Events (F-MYN-15), the own avvik text catalogue (F-MYN-16), WORM hash chain and agent allowlist (F-MYN-23), SwaggerHub polling (F-MYN-24), and the nightly 9-service access matrix (F-MYN-06).

## 4. Entities for M0/M1 and over-engineering

### M0 (MYN/BET-owned): about 70 fields across 6 tables
| Entity | Fields now | Keep | Notes and over-engineered fields |
|---|---|---|---|
| D-AMelding | 35 | ~14 | Keep the payload JSON plus id, opplysningspliktig, kalendermaaned, versjon, meldingsId, erstatterMeldingsId, inkluderte_kjoringer, nyttelast_hash, status, godkjent_av/tid, and sums per date as an index. **Over:** `meldingsformat` and `regelpakke` (constants for now), `korrigeringstype` (5 values), `diff_mot_forrige`, `antall_*` and all `sum*`/`aga_*` columns that duplicate the payload, `xml_eksport_ref`, `migrert_fra_system`, `annenBagatellmessigStoette`, `sumFinansskattLoenn`, `utbetalingsdatoer_bekreftet` (belongs on the payment). |
| D-Innsending | 35 | ~10 (M0), ~16 (M1) | **Over:** polymorphic `objekt_ref` over 10 types (inntektsmelding, skattekort, systembruker …), the `forrige_hash` hash chain, WORM refs, `opplastingId` (file API cut), `nav_innsendingId`, `step_up_metode`, `utlost_av_type`. **Merge with D-Myndighetskall** into one authority-call log in M1. |
| D-Betalingsforslag | 26 | ~12 | **Over:** `kanal` (4 values), separate sums for AGA, finansskatt, kreditor and two utleggstrekk types (derive), `fullmakt_ref`, `avstemming_ref`, `nullstilt_arsak`. |
| D-Betalingsoppdrag (PmtInf) | 25 | ~12 | **Over:** `SvcLvl` and `ChrgBr` (bank-profile constants), `PmtInfSts` (pain.002 is LATER), `bekreftet_kilde` with 5 values (manual only), `DbtrAgt_BIC`. |
| D-Betalingslinje | 27 | ~12 | **Over:** `UETR`, `TxSts`, `StsRsnInf_Cd`, `BookgDt`, `AcctSvcrRef`, `retur_aarsak` (all from bank messages, LATER), `InstrId`, `CdtrAgt_BIC` (foreign is LATER). `erstatter_ref` comes in M1 (returns). |
| D-Betalingsfil | 19 | ~10 | **Over:** `kanal`, `GrpSts`, `InitgPty_Id`, `antall_nye_kontoer` (derive), `meldingsdefinisjon` and `bankguide` (one bank profile in M0). |
| D-KID | 14 | 0 | **Make it a value, not an entity.** Store the KID string and kravtype on the payment line, and compute and validate with a `kid::skatteetaten` function. Storing decomposed `inntektsaar`, `termin` and `kontrollsiffer` is over-engineering. |
| D-Frist | 16 | 0 in M0, ~8 in M1 | Compute deadlines from run dates in M0. The 23 type values include BYR/ORL types (honorarvedtak, verv) that are irrelevant here. |
| D-Kontoendring | 26 | merge | **Merge into D-Personbankkonto** (PER, 21 fields), which already has a status and verification fields. Two entities with parallel status machines for one bank account is over-engineering. **Over:** `karantene_til`, `varsel_gammel_kanal_*`, `naer_sluttdato`, `gjelder_daglig_leder`, `bankid_subject`, `bankid_navn_stemmer`, `forste_betaling_*` (already on the payment line). |

Cross-area entities M0 depends on: D-Virksomhet, D-Underenhet (zone), D-Lonnskjoring, D-Lonnslinje, D-Arbeidsforhold, D-Stillingsperiode, D-Person, D-Personbankkonto, D-Bankkonto, D-Pensjonsordning (only the pensjonsinnretning id), D-Skattekort (manual), D-Bruker, D-Avvik (local validation findings), D-Revisjonslogg, D-Lonnskalender.

Over-engineered cross-area fields:
- **D-Personbankkonto:** `andel_av_netto` (split pay), `gjelder_dodsbo`, `bank_navn_adresse`.
- **D-Bankkonto:** `formaal` list, `betalingskanal`, `bankavtale_id`.
- **D-Lonnskalender:** `fristmal`, `utvalg`, `variabel_forskyvning_mnd`, `unntak`. M0 needs only a payout date per run.

### M1 additions: about 100 fields (about 8 of them, D-Klienttilknytning, now belong to M2, and about 7, the K27 import, are LATER under Plan v1)
| Entity | Fields now | Keep | Notes |
|---|---|---|---|
| D-Systembruker | 25 | ~11 | **Over:** `tjenestestatus` JSON over 9 services, `changerequest_*`, `krevde_pakker`, `siste_mp303`, `dagl_navn`, `utvidet_modell`, `integrationTitle`. |
| D-Klienttilknytning | 16 | ~8 (M2) | M2, with client linking (F-MYN-05). Keep `skriftlig_fullmakt_ref` (GRFS 3.4). **Over:** `altinn_clientId`, `delegeringsmetode` (portal only), `tjenestestatus`, `instruks_sendt_tid`. |
| D-Myndighetskall | 23 | merge | Merge into D-Innsending to make one call log (about 16 fields in total). **Over:** `principal_type=agent`, `klassifisering` with 6 values. |
| D-Tilbakemelding | 28 | ~12 | Keep the raw JSON, ids, mottakstatus, KID for AGA and forskuddstrekk, forfallsdato, and the three received sums. **Over:** `hendelse_id` (no Events), the `mottatte_leveranser` list, `summer_stemmer_med_sendt` (derive). |
| D-Tilbakemeldingsavvik | 22 | ~10 | **Over:** `klartekst` and `rettforslag` catalogue, `forste_sett`/`sist_sett` auto-close. Consider storing these as D-Avvik rows with `kilde`. |
| D-Kontrollsak | 20 | merge | **Merge with D-Avvik** (open question in K4). **Over:** 6 severity levels, `lukkevilkar` JSON, the `varslet` list. |
| D-Avstemmingsrapport | 20 | ~8 | Keep order/status and the raw JSON. **Over:** columns that copy `innsendinger`, `betalingsinformasjon` and counters from the raw JSON. |
| D-Skattekortbestilling | 23 | ~11 | **Over:** `dialogreferanse` (obsolete after 15.12.2026), `antall_poll` and `siste_poll_tid` (job state, not domain), `varslingstype` (semantics unknown), and the `arbeidstakere` fnr list (reference persons instead). |
| D-Betalingsmottaker | 15 | ~8 | **Over:** `referanseformat`, `betalingshyppighet` (per run only), `samle_betalinger`, `kilde`. |
| D-Sammenstillingsoppgave | 17 | ~9 | Generate the PDF on demand from accumulators. Keep person, year, version, pdf_ref, published, and `kanal` (Plan v1 delivers through Digipost with print fallback). **Over:** stored copies of `ytelser_per_beskrivelse`, `fradrag` etc. |
| D-NavRapport + D-NavRapportlinje | 19 + 21 | 0 in M1 (~7 when built) | **Plan v1: LATER with K27 import.** When built, replace with a tiny `nav_refund_import`: orgnr, sub-unit, period, refund sum, file hash, imported by/at. **Never store fnr or ytelseskode lines** (art. 9). |

LATER entities: D-Myndighetsabonnement (whole entity: 9 services, webhooks, polling budgets), D-Inntektsmelding (35 fields), D-Bankmelding, D-NavRapportlinje.

Not needed by M0/M1 in this area: D-Lagringssted, D-Hendelse, D-Delegering, D-Fullmakt.

**Net: about 170 of 540 fields (−69%), and 24 MYN/BET entities reduced to 6 in M0 and about 15 in M1.** (Under Plan v1, about 160 fields and 14 entities, with K27 import LATER.)

## 5. Top cuts (biggest effort saved)
1. **All NAV APIs** (F-MYN-30, 31, 32, 33, 35 and the K27 API). Separate onboarding, art. 9 data, and a fragile NAV API status. M1 uses NAV's portal plus a hand-entered refund receivable (K27 CSV import is LATER under Plan v1).
2. **Trekkpålegg API** (F-MYN-28). It can't be obtained before API submissions anyway. Use a manual register.
3. **Bank-message import and channels** (F-BET-10, 11, 14, 15, 22). Manual payment confirmation, file only.
4. **A-melding 2.4** (F-MYN-20) until the spec exists. Only keep the aggregate format-neutral. (Plan v1 dates the build: mapping 1.7.2027, test 1.12.2027.)
5. **Firm batch features** (F-MYN-13, the client-delegation API, nightly multi-client polling budgets, Altinn Events).
6. **Gateway gold-plating** (WORM hash chain, agent allowlist service, SwaggerHub polling, in-app outage banner).
7. **Standalone A07 control catalogue** (F-MYN-42) and SSB data-quality checks (F-MYN-38).
8. **XML v2.3 serialiser**, because the first Brutto submission is a 2027 period (B44). It stays a costed fallback (+1–2 weeks) if Skatteetaten's answer is that 2027 manual uploads are still XML.
9. **Payment extras**: liquidity dashboard (F-BET-04), instant payments (F-BET-07), foreign accounts (F-BET-12), quarantine and notification machinery in the account shield.

## 6. Legal must-haves (cannot be cut for M0/M1)
- **Monthly a-melding by the 5th** (a-opplysningsloven; tvangsmulkt up to 1 000 rettsgebyr, § 10). It must include all incomes, forskuddstrekk per lønnsutbetalingsdato, AGA per zone, ongoing employments without pay, and `pensjonsinnretning` for OTP-liable employers. The lønnsutbetalingsdato must equal the actual payout (F-MYN-07, 08, F-BET-17). From 2027-01 the F532 and F530 rules apply. From 2028-01 format 2.4 is required.
- **Corrections** of earlier months as a full replacement (up to 3 years).
- **Forskuddstrekk paid separately after each payout** by the first working day after, with KID kravtype 05, never marked SALA ("Lønn"). Late payment is punishable for the customer (B §14 pkt. 6).
- **AGA paid by the 15th** of each two-month term, with the KID from the feedback.
- **Withholding by the current tax card**, 50% if there is none. The new year's card must be in use for January.
- **Samordnet utleggstrekk** honoured and paid to the order's account and KID the day after payout (M1, if any employee has an order). Not deducting can make the employer liable (N29).
- **Annual statement with feriepengegrunnlag** (ferieloven § 10). The full sammenstillingsoppgave and its 31.1 deadline still need legal confirmation [verify].
- **Vendor obligations** under the Digdir, Altinn and Skatteetaten terms: test in the test environment first, follow SBS news and the status page, keep a contact point, act as data processor with a DPA per customer, and respect the purpose limitation (public-task use only).
- **Accounting firms (M2)** need a written mandate from each client (GRFS 3.4) and REGN or delegation in Altinn.
- **Salary is paid through a bank.** Brutto never holds funds (B12), so the open-banking client-account model (N17) needs a lawyer before it's used.
- **Storage and retention**: receipts, feedback, tax-card responses and payment files are kept 5 years. Data and backups should stay in Norway (bokføringsforskriften § 7-5). Union-dues payment detail is special-category data (art. 9).

## 7. Biggest risks
1. **Onboarding lead time and vendor company.** Nothing starts until M02/M01 (PLAN D3) are decided. The best case is 7–10 weeks and the estimate is 3–5 months, with queues around the Altinn II shutdown. This gates every M1 pilot, not M0.
2. **The manual-upload fallback is a transition service.** The format changes from XML to JSON after 2026, the English page says "in test", and there's no end date or 2.4 support stated. M0, and M1's contingency, rest on it.
3. **Self-generated forskuddstrekk KID.** A wrong KID means the payment isn't registered, which can mean late withholding (criminal for the customer). The structure is documented (N17), but it must be tested against Skatteetaten's KID generator for all 12 months before the first real payment. Plan v1 mitigation: M0 uses the KID from the a-melding feedback, and Brutto's own KID comes only in M1, after it reproduces every 2026 KID [verify positions 18–19].
4. **Bank file acceptance.** Version, a separate non-SALA block in the same file, and several execution dates in one file are unconfirmed per bank. Nordea validates strictly.
5. **2.4 in 2027.** The spec arrives 1.5.2027 and the test environment 15.9.2027, while a team of three is also onboarding pilots.
6. **Garnishment chicken-and-egg.** The API needs Brutto API submissions first, so M1 relies on manual registration of orders from letters, which is error-prone.
7. **Accounting-firm access (M2).** It's unclear whether a firm gets the package without REGN, whether a private vendor gets an ID-porten client for client delegation, and whether the 5-concurrent-call quota is per firm or per client.
8. **Two systems in one income year.** Mixing systems complicates the annual statement and corrections. Mitigated by the 1.1.2027 cutover that PLAN adopts (B44).

## 8. Open questions (sporsmal) and whether they block M0/M1
| Question (file) | Blocks | Recommendation |
|---|---|---|
| KID check digit and AGA term code (K4) | M1 (own KID); not M0 | Largely answered by N17: MOD11 plus a buffer digit. AGA KID comes from the feedback, so the term code isn't needed. Plan v1: M0 takes the forskuddstrekk KID from the a-melding feedback too; own KID only after it reproduces every 2026 KID [verify positions 18–19] and passes the KID generator. |
| pain.001 version, SALA, several dates in one file (K4) | **M0** for the team's bank, M1 for pilot banks | Ask your own bank for the implementation guide and a test file now. |
| 24.12/31.12 as working days (K4) | Not blocking | Pay forskuddstrekk on the payout date. |
| F532 per message or per month (K4) | M1 (corrections) | The one-message-per-month replacement strategy is safe either way. |
| Correcting 2027 periods after 2.4 (K4) | LATER | – |
| Default AGA method for NAV refund (K4, design) | **M1** | Decide now: "deduct when received" as the only method in M1 (it can't double-deduct). With K27 import LATER, the receipt is entered by hand. |
| Sammenstillingsoppgave: legal basis, deadline, sender (K4, K6) | **M1** (Brutto submits no 2026 periods, B44) | Ask a lawyer and Skatteetaten (in the letter). The 1.1.2027 cutover avoids it for 2026. |
| Client delegation, REGN, quota (K4, design) | **M2** (firm clients) | Altinn portal linking. Fallback: a standard system user per client. Measure the quota in TT02 (M11). |
| Special-category package from start or at first NAV case (K4) | M1 decision | Don't request it in M1. NAV APIs are LATER. |
| Payout date when net pay is returned or moved (K4) | M1 | M0: the date is confirmed before the a-melding is generated (F-BET-17). |
| Account-shield quarantine (K4) | Not blocking | Cut the quarantine in M0/M1. Four-eyes is enough. |
| `resourceFilter` for Altinn Events (K4) | Not blocking | Poll by `dialogId` instead. |
| Multibank channel choice (K4) | Not blocking | LATER. |
| One case queue: D-Avvik + D-Kontrollsak (K4) | M1 data model | Merge. |
| Bidrag: channel and a-melding code (K2) | M1 only if a pilot has bidrag (child-support deductions) | Manual from the letter. |
| AGA of OTP premium (K2, design) | **M0/M1** AGA correctness (PEN/REG) | Needs an answer before the first real AGA term with OTP. |
| Use of Skatteetaten's trekkrutine (withholding routine, design / F-TRK-07) | **M0** (TRK) | Port it to Rust and test it 100% against the published table file (N13). |
| Proof that forskuddstrekk was paid, for firms (K5) | M1 | Manual confirmation with date. |
| fase1 **M01** owner and **M02** vendor company | **M0 (starts the clock)** | Decide this week. |
| fase1 M03 key, M05 first system-user type, M09 client linking, M10 A07 cadence, M11 TT02 plan | M1 (M09: M2) | Follow the proposals in fase1.json (replaced by `docs/plan/questions.md` §2). |
| fase1 B01–B09 open banking | Not blocking | LATER. B08 (keep the bank file) is the M0/M1 baseline. |

## 9. Minimal authority-integration sequence (manual first, API when ready)

| When | Manual / built | API |
|---|---|---|
| **Week of 2.11.2026** | Decide vendor company and owner (M01/M02). Ask your bank for the pain.001 guide and a test file. Ask Skatteetaten about the manual-upload format in 2027 and about KID testing. Check who holds the Altinn 3 package "A-ordningen" for the M0 employer (needed before the first live upload, period 2027-01). | Send the Digdir consumer form, sign the Maskinporten terms, delegate self-service, register a varslingspunkt (contact point). Apply for scopes `skatteetaten:innrapporteringamelding` and `skatteetaten:skattekorttilarbeidsgiver`. Accept the Altinn SBS terms and request the system-register scopes (N06 tracks A–D). |
| **Nov–Dec 2026 (M0 shadow)** | Brutto calculates November and December payroll in parallel. It generates the a-melding JSON and checks it in Skatteetaten's **test** manual upload with TestID. Compare with the old system to the øre. Tax cards (incl. 2027) are keyed by hand. The pain.001 is validated in the bank's test. **The old system submits 7.12.2026 and 5.1.2027.** | Set up the TT02 Maskinporten client, register in the TT02 system register, and create a system user for a Tenor test entity. |
| **First live period: 2027-01 (stretch, deadline Fri 5.2.2027) or 2027-02 (plan, deadline Fri 5.3.2027)** | First a-melding from Brutto by manual upload (JSON, or XML if Skatteetaten still requires it) [verify]. Forskuddstrekk is paid on payout day as its own payment order, with the KID from the a-melding feedback (upload on payday, then pay). Feedback is read in Altinn, and A07 downloaded from the portal for reconciliation. | Test in TT02: REST submission of synthetic a-meldinger, feedback polling by `dialogId`, A07 order and poll, poll-only tax-card orders. |
| **Feb–Apr 2027 (gate MP: Maskinporten live 29.1.2027 / 31.3.2027)** | Contingency runbook in place (F-MYN-41). | When production scopes are granted, the own company moves to REST plus system user. Then the tax-card API (order + HENT_KUN_ENDRING before each run), A07 on demand, and polled feedback with AGA KID. Pilot direct customers approve a standard system user before their parallel runs (October–November 2027 in the stretch case; spring 2028 in the plan, with pilots live 1.8.2028). K27 import is LATER under Plan v1. Firm clients (agent system user, clients linked in the portal) wait for M2, from 1.8.2028 at the earliest. |
| **~3 months after first API submissions** | Garnishment orders are still registered by hand from letters. | Apply for the trekkpålegg API (test summary and agreement required). |
| **Jun–Nov 2027** | – | Build the a-melding 2.4 serialiser after the spec (1.5.2027): mapping by 1.7.2027 (gate 24-S), test in TT02 from 15.9.2027, accepted in test by 1.12.2027 (gate 24-T). |
| **Dec 2027 – Jan 2028** | Sammenstillingsoppgave for 2027 by 14.1.2028 (gate AS27; legal deadline 31.1.2028). | Fetch 2028 tax cards via the API. First 2.4 a-melding for 2028-01 by 7.2.2028. |
| **2028+** | – | NAV APIs (inntektsmelding for sick pay, K27 API), Krav og betalinger, Altinn Events, pain.002/camt.054, open-banking partner (B40). |
