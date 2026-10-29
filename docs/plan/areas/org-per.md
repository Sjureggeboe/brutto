# Scope review: ORG (organisation and setup) and PER (persons and employments)

> Working paper from the scope review of 29.10.2026. PLAN.md is the main plan and `docs/plan/scope.csv` holds the final tier per function; where this paper disagrees, they win.

Source: `analyse/build/data/omr-K1.json` (all 65 functions in ORG and PER, 23 ORG/PER entities, 12 area questions), `design.json` (B6, B19, B21, B34, B35, B37, B41, B42), `fase1.json` (D08, D09, L03, P03, P05), `research/R0-matrix-lonn-omrader.md` (§ Agent K1). Per-function detail is in `docs/plan/scope.csv` (rows with area ORG or PER).

## 1. Tier counts

| Area | Functions | M0 | M1 | M2 | LATER | CUT | Currently "MVP" |
|---|---|---|---|---|---|---|---|
| ORG | 29 | 7 | 4 | 0 | 16 | 2 | 16 |
| PER | 36 | 11 | 11 | 0 | 11 | 3 | 24 |
| **Total** | **65** | **18** | **15** | **0** | **27** | **5** | **40** |

- 33 of the 40 MVP-marked functions stay in M0/M1, but almost all are cut down to a fraction of their written design (see the `simplest_lawful_version` column).
- 7 MVP functions move to LATER: F-ORG-28 (byrå/group templates), F-ORG-29 (setup wizard), F-PER-04 (address protection), F-PER-12 (history timeline and access export), and, by the Plan v1 decision after review, F-ORG-01 (Brreg lookup), F-ORG-15 (dimension sync with the accounting system) and F-ORG-18 (dimension inheritance).
- No "Etter MVP" (after-MVP) function has to move into M0/M1, but four of them create **conditions on which pilots we pick** (section 5).
- 16 functions weighted Må (must) end up in LATER/CUT. Each one has either a lawful manual route or a rule that keeps the case out of the pilot group.

**M0 (first payroll, Brutto's own company):** F-ORG-02, -03, -22, -23, -24, -25, -27; F-PER-01, -02, -07, -14, -20, -22, -23, -24, -25, -27, -34.
**M1 (direct-customer pilots; firm clients are M2):** F-ORG-06, -13, -14, -16; F-PER-03, -06, -11, -13, -15, -18, -19, -21, -26, -35, -36.

**Plan v1 decision (after review, 29.10.2026):** Brreg lookup (F-ORG-01), dimension sync (F-ORG-15) and dimension inheritance (F-ORG-18) moved from M1 to LATER. Pilots enter the legal entity and sub-units by hand, and one flat department/project code on the employment is carried to the voucher lines (PLAN §6.2, §9).

## 2. Summary

For M0, ORG and PER only need to answer what the a-melding (monthly employer report) and the payment file ask about the employer and each employment. The employer side is the opplysningspliktig (reporting legal entity) and one sub-unit (virksomhet) with its AGA zone (arbeidsgiveravgift, employer's social-security contribution), plus a payday. Each employment needs an ID carried over from the old system, a type, start and end, position %, full-time hours, working-time arrangement, occupation code, form of employment and the two "last change" dates. Each person needs a national ID number and a bank account. Everything else in K1 is HR, analytics or breadth at SD Worx level.

M1 adds what direct-customer pilots actually hit (firm clients wait for M2; a firm's own payroll can be an M1 pilot as a direct customer):
- tax-exempt organisation rules
- one flat department and project code on the voucher
- foreign IDs
- on-call staff, terminations and corrections
- pay grade passed through to the a-melding
- the A07 comparison used to verify migration

The biggest saving is in the data model, not in the function count. Three changes do most of the work:
1. **Bitemporal → effective-dated + append-only.** F-PER-22, D-Underenhet and D-Kostnadsfordeling are designed as fully bitemporal, with valid time and recorded time on the stable employment as well. Use instead: `valid_from/valid_to` plus `recorded_at/superseded_at` on the rows that change over time, no "as known at" query layer, and an immutable snapshot of inputs per approved run. B6 and R3 D-38 already call a general "as known at" layer overbuilt. fase1 D08 proposes the same thing.
2. **Dimensions as two fixed fields.** Replace D-Dimensjonstype, D-Kostnadsfordeling (percentage split, profiles), D-Organisasjonsenhet (tree) and D-Prosjektdeltakelse with two optional references on the position period: `department` and `project`. Both point to one flat list (D-Dimensjonsverdi with type ∈ {department, project}). This answers the B35 hint: flat lists are enough for M1. B42 already says "flat lists for department and project".
3. **Don't store what payroll doesn't need.** Leave out home addresses, gender, citizenship, children, next of kin, probation and notice periods for now. This removes F-PER-04 and two open legal questions (gender, address protection), and it follows GDPR data minimisation.

## 3. Entities needed for M0/M1

Field counts are exact against `felt[]`. Overall, the 23 ORG/PER entities with **392 fields** become **11 entities with 126 fields: 90 for M0 and 36 more for M1**, plus 4 new columns (3 contact columns, 1 project reference).

| Entity | Now | M0 | +M1 | Notes / main cuts |
|---|---|---|---|---|
| D-Virksomhet (legal entity) | 29 | 8 | 7 | M0: org no., name, default AGA calculation code, pension provider org no. (`pensjonsordninger` reduced to one reference), full-time hours, feedback language, holiday-pay scheme default. Cut: Brreg roles (personal data), sector/NACE codes, register flags, konsern, fribeløp, § 23-2 exemption, tariffs, employee number series. |
| D-Underenhet (sub-unit) | 22 | 11 | 4 | Zone and municipality effective-dated, not bitemporal (`registrert_til` dropped). Cut: ambulating work, geography (Svalbard/continental shelf), Brreg headcount, location address. |
| D-Kommune (municipality → zone, reference data) | 8 | 5 | 0 | Yearly seed file. Mergers are handled by a new yearly version, not by `erstattet_av` chains. |
| D-Lonnskalender (payroll calendar) | 15 | 7 | 1 | One monthly calendar per legal entity. `gjelder_juridiske_enheter` becomes a single reference. Cut: deadline templates, selections, exceptions, run types. |
| D-Lonnsperiode (payroll period) | 14 | 9 | 2 | Variable-data window in M1. Cut: deadlines, bank-file date (derived). |
| D-Bankkonto (company account) | 16 | 7 | 2 | M1: second-person verification. Cut: IBAN/BIC/currency, bank-API channel. |
| D-Dimensjonsverdi (department or project) | 19 | 0 | 6 | Flat list. Cut: hierarchy, owner, funder model, hourly-rate caps, attributes. |
| D-Person | 25 | 9 | 4 | Takes over work e-mail, private e-mail and mobile from D-Kontaktinfo. Cut: gender, citizenship, language, address protection, death and estate, residence permit, custom fields. |
| D-Personbankkonto (personal bank account) | 21 | 8 | 4 | Norwegian account only. M1: verification by a second person. Cut: foreign IBAN fields, split pay, estate flag. |
| D-Arbeidsforhold (employment, stable part) | 34 | 10 | 2 | **Drop the bitemporal columns on the stable part.** Changes are rare; the audit log and replacement a-meldinger cover them. Cut: notice, probation, seniority, groups, leading role, `hovedarbeidsgiver` (redundant: tax is per person and opplysningspliktig), previous employment. `mottakerklasse`/`engasjement` are left to the ORL reviewer. |
| D-Stillingsperiode (position period) | 35 | 16 | 4 | M1: title, department (`organisasjonsenhet` re-pointed to a department value and made **optional**), pay grade and pay seniority as pass-through, plus a new `project` reference. Cut: position, location, tariff, per-employment zone override, maritime fields, cost/hourly price, control status, work schedule, shift length. |

**Dropped for M0/M1 (154 fields, 12 entities):** D-Konsern, D-Organisasjonsenhet, D-Lokasjon, D-Lederrelasjon, D-Dimensjonstype, D-Kostnadsfordeling, D-Prosjektdeltakelse, D-Kontaktinfo (folded into D-Person), D-Parorende, D-Barn, D-Skattetilknytning, D-Stilling. HR-owned D-Dokument, D-Arbeidsavtale, D-Sjekkliste and D-Utstyr are not used by any M0/M1 function in ORG/PER.

**Entities from other areas that the M0/M1 functions here depend on:**
- D-Lonnsavtale (LON)
- D-Skattekort (TRK)
- D-Pensjonsmedlemskap (PEN, M1)
- D-Akkumulator (KJO); **must be keyed on person + legal entity, not per employment** (see F-PER-16)
- D-Lonnskjoring and D-Avvik (KJO)
- D-Kontomapping (REG)
- D-AMelding, D-Avstemmingsrapport and D-Systembruker (MYN, the last two M1)
- D-Revisjonslogg and D-Tilgangslogg (SIK, the access log M1)
- D-Importjobb (MIG)

D-Personkobling and D-Kilderegister (PLA) can wait. Matching on fnr + arbeidsforholdId is enough for M1, and Brutto owns every field.

## 4. Top cuts (largest effort saved)

1. **Full bitemporality** in F-PER-22, F-ORG-03, F-ORG-16 and D-Arbeidsforhold. Replace with effective-dated append-only rows plus run snapshots.
2. **Dimension engine** (F-ORG-13/16/17/18/19/20/21): custom types, percentage split, six-level inheritance, hour-based allocation, retroactive reallocation, funder project payroll. M1 uses only department + project.
3. **Org structure and HR model**: org tree (F-ORG-09), reorganisation (F-ORG-10, CUT), locations (F-ORG-11), manager lines and delegation (F-ORG-12), positions (F-PER-30, CUT), equal-pay categories (F-PER-31).
4. **Group and structural events**: konsern (F-ORG-05), shared fribeløp (F-ORG-04), merger/bankruptcy wizard (F-ORG-08, CUT), change of legal entity (F-PER-17), change of sub-unit wizard (F-PER-16).
5. **Huma as HR master** (F-PER-32/33), duplicate merging (F-PER-10) and mass change (F-PER-29, CUT; agents can use the API in batch instead, B41).
6. **Setup machinery**: byrå templates and the generic settings resolver (F-ORG-28), setup wizard (F-ORG-29), nightly Brreg sync (F-ORG-07).
7. **Personal data payroll doesn't need**: address protection (F-PER-04), next of kin and children (F-PER-08), citizenship and social-security periods (F-PER-05), probation and notice (F-PER-27 beyond `formForAnsettelse`).

## 5. "Etter MVP" items that put conditions on the M1 pilots

None of these is needed if we choose pilots carefully. Write the conditions into the pilot criteria:
- **F-ORG-04 fribeløp:** no pilot in AGA zone 1a, and no sector-exempt or "economic difficulties" employer in zones 2–5. Otherwise pull in a single-entity counter.
- **F-PER-05 cross-border:** all employees tax-resident in Norway and in Norwegian National Insurance. No A1/posted workers, no Svalbard, no work abroad above 50 %.
- **F-ORG-26 / F-PER-26 tariffs:** no state, municipal or finance main-agreement employers. Pilots following Virke HUK fill in pay grade and seniority by hand (pass-through fields in M1).
- **F-PER-16 sub-unit moves:** a lawful manual route exists (end the employment with `endringIOrganisasjonsstrukturEllerByttetJobbInternt`, then create a new one). It only works if year-to-date and holiday-pay bases are keyed per person + legal entity. **This is an M0 design requirement for KJO/FRA.**
- **F-PER-08 children:** if FRA keeps counting care days (omsorgsdager) in M1, store an entitlement number, not child records.
- **F-PER-09 death:** handled by hand with dedicated pay types (K2) and an estate account entered by two people.

## 6. Legal must-haves for the M0/M1 profile

- **A-melding employer data:** opplysningspliktig org no.; sub-unit org no.; AGA zone and calculation code per sub-unit (the rate follows the sub-unit's municipality); pension provider for OTP-obligated employers (F-ORG-27). If the M0 employer (PLAN D2) is OTP-obligated, this belongs in M0.
- **A-melding employment data (F-PER-14/20/23/24/25/27):** arbeidsforholdId, type, start, end + reason, position %, full-time hours (never 0), working-time arrangement, 7-digit occupation code from the SSB list, `formForAnsettelse`, last pay-change date, last position-% change date. Pay grade where pay follows a step (F-PER-26). Check per-field obligation against XSD 2.3 guidance while building.
- **Recipient identity:** fnr or D-number, or an international ID + name + birth date (F-PER-03, M1).
- **Same arbeidsforholdId and start date on system switch** (F-PER-20). Otherwise a-ordningen sees duplicate employments. This is the key control in the November and December 2026 shadow runs and at the switch to Brutto from period 2027-01 (B19 as reworded, B44, B16).
- **Tax-exempt organisations** (F-ORG-06): the NOK 10,000 per-recipient threshold and `skattefriOrganisasjon` rule, if any pilot qualifies.
- **GDPR:** encrypted fnr and account number with read logging (founder's rule S §2 pt 6; art. 32), data minimisation (supports the cuts above), and art. 15 access requests (manual export is enough).
- **Control rather than law:** human confirmation of bank-account changes (B14). Not a statute, but the main fraud risk. Plan v1: re-authentication through the identity provider on bank-account change in M0, four eyes on bank-account changes in M1; changing a bank account is a human-only operation. The agent-confirmation flow F-PLA-37 is LATER.

## 7. Biggest risks

1. **Wrong arbeidsforholdId mapping on migration** creates duplicate employments in a-ordningen. Import IDs verbatim and check against A07 before the first a-melding sent from Brutto (period 2027-01). In M0 that means ordering A07 manually in Altinn.
2. **Accumulators keyed per employment** break year-to-date tax and holiday pay when someone changes sub-unit or employment. Decide the key before KJO is built.
3. **Over-modelling creeps back.** The JSON marks `organisasjonsenhet` as required on D-Stillingsperiode and puts bitemporal columns everywhere. Builders following the spec literally will rebuild SD Worx. Treat the field lists in section 3 as the M0/M1 schema.
4. **Zone table correctness:** municipality → zone has to be reseeded every 1 January, because municipality mergers take effect then. A wrong zone gives wrong AGA with no warning from Brutto.
5. **Flat department/project lists may not match pilots' accounting dimensions** (for example Tripletex `freeAccountingDimension1–3`; B35 is still open). Check the first pilots' charts of accounts before M1. Dimension sync (F-ORG-15) is LATER under Plan v1, so a mismatch is found by the accounting system on voucher import, not by Brutto.
6. **Encryption design** (per-tenant keys, blind index, fase1 D09) can stall M0. Use simple field encryption with a single key in M0 and per-tenant keys in M1.

## 8. Open questions: which ones block M0/M1

| Question (source) | Blocks? | Recommendation |
|---|---|---|
| arbeidsforholdId on sub-unit change: unique per what? (K1, PER) | **M0 schema, but the team can decide** | Use a permissive unique key (legal entity, sub-unit, person, ID) so imported IDs never fail. Asking Skatteetaten is not on the critical path. |
| Pay grade on the position period or on the salary agreement? (K1, PER) | **M1 schema** | Decide now: pass-through on the position period. The K2 salary agreement holds only the amount (no ladder in M1). |
| How much history now? (fase1 D08) | **M0 schema** | Effective dating + `recorded_at` + run snapshot, as in section 2. |
| Encryption of fnr and account number (fase1 D09) | M0 (light) | Single key in M0, per-tenant keys and blind index in M1. |
| Fribeløp: what counts as "one enterprise" in a group? (K1, ORG) | No, if pilots are gated | Gate pilots (section 5). |
| From which month does a new AGA zone apply after a move? (K1, ORG) | No | Rare. Enter the effective date manually. |
| Huma dates, end reasons and API terms (K1, PER) | Only if a pilot uses Huma (B21 downgraded to after M1; the Huma integration is LATER) | Ask pilots now. If yes, use a one-off CSV import. |
| Board fees to an employee: own employment? (K5, ORL) | M1 if pilots pay board fees to staff | Let the ORL reviewer resolve it. Affects F-PER-14/15. |
| AGA zone for freelance and fee employments (K5, ORL) | M1 if pilots have such recipients | ORL reviewer. |
| End reason when an employee dies (K1, PER) | No | LATER (F-PER-09). |
| Gender in the person register (K1, PER) | No | Don't store gender in M0/M1. |
| Address protection without the population register (K1, PER) | No | Don't store addresses in M0/M1. |
| Simplified a-melding for charities (K1, ORG) | No | Decide "not supported". Outside the 10–1000 segment. |
| Code-list changes in 2030 (K1, PER) | No | Maritime is CUT. |
| Whistleblowing/HMS outside Brutto (K1, HR) | No | HR, not in scope. |
| NFR and Horizon hourly rates (K1, ORG) | No | LATER (F-ORG-21). |
| Occupational health service fields on the legal entity (K7, HEL) | No | LATER (HR extension). |

Practical inputs M0 needs that are not in any question list:
- Is the M0 employer (PLAN D2) OTP-obligated, and with which pension provider?
- Which holiday-pay scheme does it use?
- What is the zone of its sub-unit?
- Can the current payroll system export arbeidsforholdId values?
