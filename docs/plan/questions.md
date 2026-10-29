# Brutto – open questions and pending proposals, triaged for payroll-first (29.10.2026)

> **Status:** Working paper from the scope review of 29.10.2026. [`PLAN.md`](../../PLAN.md) is the main plan; where this paper and PLAN.md disagree, PLAN.md wins.
>
> **What it is for:** the list of questions Sjur, Peter and Sander still have to answer before M0 and M1, the replacement for `fase1.json`, and the review of decisions B1–B46 behind PLAN.md §8 (decisions) and §10 (open questions).

Scope of this triage: every open question and pending proposal in
- `analyse/build/data/design.json` `sporsmal` (36, numbered DQ01–DQ36 in file order) and the status of B1–B43,
- `analyse/build/data/omr-K1.json` … `omr-K7.json` `sporsmal` (105, numbered K1-01 … K7-08 in file order),
- `analyse/build/data/fase1.json` `fase1.sporsmal` (105, ids P/T/A/J/D/M/K/R/G/B/U/I/H/X/L as in the file),
- `analyse/natt/forslag.md` (N01–N40, triaged per item: its proposed mapping changes plus its questions), `analyse/natt/backlog.md` (N22 is the only open item), `analyse/natt/morgen.md` (8 decisions for Sjur = MS1–MS8, 8 questions for Peter and Sander = MP1–MP8, and the "recommended mapping changes").

Labels: **BLOCKS-M0** = must be answered before building the first payroll (own company, shadow run). **BLOCKS-M1** = before external pilots (direct customers only). **LATER** = roadmap after M1; "LATER (M2)" marks items for the accounting-firm milestone M2 (B45). **MOOT** = irrelevant under payroll-first narrow scope, or cut (reason given). A dagger (†) means "needed, but adopt the existing proposal unless someone objects – no meeting time needed". **Decided in PLAN.md (D#/E#/§)** means PLAN.md gives the answer; it is listed for traceability. D1–D12 are Sjur's decisions with PLAN.md's recommended answer, taken by the dates in PLAN.md §2.2 (D1–D5 and D12 by 6.11, D6 by 9.11, D7–D11 by 13.11). E1–E10 are engineering defaults, adopted at the Monday 2.11 meeting unless someone objects.

Norwegian terms used: a-melding (monthly employer report to the a-ordning), AGA (arbeidsgiveravgift, employer's social-security contribution, by zone), forskuddstrekk (PAYE withholding), skattekort (tax card), feriepenger (holiday pay), ferietrekk (holiday deduction), halvt trekk (half withholding in December), arbeidsgiverperiode/AGP (employer-paid first 16 days of sick leave), opplysningspliktig (reporting legal entity), virksomhet (sub-unit/establishment), trekkpålegg (garnishment order), sammenstillingsoppgave (annual earnings statement), byrå (accounting firm), K27 (NAV refund settlement report), OTP (mandatory occupational pension).

## Key findings

1. **The M0 critical path is not Maskinporten.** It is Sjur's payroll-domain decisions (pay-type list, flags, accounts, rounding, OTP input), the withholding implementation (own port, checked against the published table file), the manual a-melding upload channel, and the team's own bank file format. After deduplication, 21 questions block M0. PLAN.md answers 16 of them through D1–D12, E1–E10 and §1, which leaves 5 open: the M0 employer and vendor company (Q19), the upload format and the Altinn packages (Q10), the bank's pain.001 version (Q12), the letter to Skatteetaten (Q24) and recruiting (Q30).
2. **Shadow run in November–December 2026; Brutto is system of record from period 2027-02 (planning date) or 2027-01 (stretch)**, 2027-03 at the latest (decided in PLAN.md D1, new B44). The current system keeps filing all of income year 2026. This removes the 2026 sammenstillingsoppgave and the 2026 year-to-date import from M0 (DQ12, DQ26, D-27). The December shadow run still exercises halvt trekk. Brutto then files by manual upload until Maskinporten is live (gate MP, 31.3.2027, best case 29.1.2027).
3. **Two M0 blockers were not in any existing list** (Q10, Q11): which manual a-melding channel and format work after Altinn II roles stop, with the Altinn 3 packages confirmed ("A-ordningen" for the a-melding, "Lønn" for tax cards), and where M0 tax cards come from. PLAN.md §1.4 item 4 now answers the second: Skatteetaten's tax-card file service (RF-1211) or a copy from the current system. Also, **F-MYN-14 (manual-upload export) is tagged "Etter MVP" but M0 depends on it** – moved to M0 in `scope.csv`.
4. **41 of the 105 `fase1.json` questions are moot or later** (4 of them M2), mostly because they were written for the read-only A07/general-ledger reconciliation tool (P01–P03, P06–P07, G-series flexibility, open banking, assistant, agent OAuth and SDKs). The same goes for the night-work items N04, N05, N11, N25, N26, N32, N37 and N38. The other 64 collapse into 25 replacement questions (section 2), and 7 of those are engineering defaults to adopt as proposed (†).
5. **Of the 105 area questions, 25 block M0 (9) or M1 (16).** Most of the rest belong to organisation life (ORL), HR (K7), tariffs, expenses or time, which are all outside M1.
6. **B42 (MVP at Matrix level) and B31 (map before building) should be dropped.** B13, B15, B17, B18, B20, B21, B24, B39 and B40 should be downgraded to later. PLAN.md adds B44, B45 and B46; B45 has a stated consequence, no firm-client revenue before 2029 in the base case. See section 4.

---

## 1. Questions that block M0 or M1 (30)

PLAN.md §2.1 (E1–E10) and §2.2 (D1–D12) carry the answers. Mapping: D1 = Q1; D2 and D3 = Q19; D4 = Q21; D5 = Q2 and Q13; D6 = Q4; D7 = Q5; D8 = Q7; D9 = Q9; D10 = Q8; D11 = Q16; D12 = Q30. E1 = Q13; E4 = Q14; E5 = Q6 and Q15; E6 and E7 = Q15; E10 = Q18 (E2, E3, E8 and E9 are engineering-only, in section 2).

Of the 30, 17 are decided in PLAN.md. 5 are open and block M0 (Q10, Q12, Q19, Q24, Q30), 7 are open and block M1 (Q20, Q21, Q22, Q23, Q26, Q28, Q29), and Q27 moves to M2 (B45). This matches PLAN.md §10.

| # | Question | Tier | Owner | Recommended answer (one line) | Sources |
|---|---|---|---|---|---|
| Q1 | Is Brutto the system of record for income year 2026, or does it shadow-run Nov–Dec and take over in 2027? | Decided in PLAN.md (D1, B44) | Sjur | The current system submits all of income year 2026. Brutto shadow-runs November and December 2026, compared to the øre, and is system of record from period 2027-01 if both shadows are clean by 15.1.2027 (stretch, ≈40 %), otherwise 2027-02 (planning date, ≈65 %) or 2027-03. No 2026 year-to-date import and no 2026 sammenstillingsoppgave from Brutto. Import each employee's 2026 holiday-pay base before the June 2027 payout (gate JUN27, 14.5.2027). | B19, B44, DQ12, DQ26, D-27 |
| Q2 | When something has to give, what goes first: date, scope or quality? | Decided in PLAN.md (D5, §3, §6.3) | Sjur | Quality, then date, then scope. M0 slips by rule rather than files an a-melding that has not been verified: a failed shadow moves go-live to 2027-02 or 2027-03. Scope is frozen (M0 13.11.2026, M1 lawful core 1.2.2027, pilot-pulled items 31.3.2027) and changes are one in, one out, in developer-weeks. If M1-FC is at risk, the agreed cut order applies: (1) MCP draft tools, (2) the accounting adapter, (3) dimensions beyond one department, (4) travel allowances, (5) board and fee recipient classes, (6) Digipost, replaced by manual secure delivery, (7) automated termination settlement. Never cut: engine correctness, the a-melding API with feedback, A07 as answer key, migration checks, BankID approval, row-level security, the pentest. | DQ03, B22, B26 |
| Q3 | What is the M0 exit criterion? | Decided in PLAN.md (§1.7) | All three | Gate M0-L: two consecutive shadow months where payslip lines, withholding, AGA base and amount, holiday-pay base, net pay, the payment-file sum and the a-melding content match the current system to the øre, with every remaining difference explained and signed. The withholding port matches 100 % of the 2026 and 2027 table files; the 30 M0 golden cases (plus a union-dues case if dues go through payroll) are signed and green; a synthetic twin is accepted in Skatteetaten's test upload; the bank validates the pain.001 file; the forskuddstrekk KID routine is written and rehearsed; ongoing leave, sick cases and garnishments are absent or imported and signed; the system description is signed; the rollback runbook is ready; the current system's records are archived; and Sjur signs off. | P04, B16, B26 |
| Q4 | What is the minimal pay-type (lønnsart) model? | Decided in PLAN.md (D6) | Sjur | Number, name, a-melding code (description and benefit), withholding method (table, percent, none), half-withholding flag, flags for tax, AGA, holiday pay, sick pay and pension base, a union-dues deductible flag, unit, and debit and credit accounts. No customer formulas. Retro, the expression language and June-specific flags come later. Needed by 9.11. | DQ06, K2-01, B5, D-02 |
| Q5 | Which pay types does M0 need, with codes, flags and accounts? | Decided in PLAN.md (D7) | Sjur | 8–12 of the 26 standard types, and only these are seeded: fixed salary, hourly (if any), one-off addition, holiday pay, ferietrekk and deduction after tax, plus union dues and benefits if the M0 employer (D2) has them. Sjur fills codes, flags and accounts from his A07 mapping, with one signed golden case per type, by 13.11. | K2-02, S #25, N23 |
| Q6 | How is forskuddstrekk computed in M0? | Decided in PLAN.md (E5, Appendix A item 4) | Sjur approves; Sander builds | Our own Rust port of Skatteetaten's published withholding rules, in `f64` with the Java order of operations, isolated in its own crate, plus percentage cards. CI requires a 100 % match against every row of the published table file (about 1.06 million rows). Still open as actions (PLAN.md Start here, §2.4 item 4): approve the 5.6 MB table-file download at the Monday 2.11 meeting, and send the licence question for the trekkrutine without waiting for the answer. | DQ09, K2-04, L01, N13, MS5 |
| Q7 | What are the rounding rules for withholding, union dues and AGA? | Decided in PLAN.md (D8, §1.4 item 2) | Sjur (Skatteetaten confirms) | Base and amount for percentage withholding rounded down (§§ 5-10-4, 5-5-4). Half and other derived table amounts rounded down. Union dues in the withholding base rounded up (§ 5-9-1). AGA computed exactly per virksomhet and zone, then rounded down once per opplysningspliktig and month (§ 10-4-4) [verify the F185 tolerance in test]. Lines kept to the øre, never banker's rounding. Prove it by matching the current system to the øre, and confirm it in the letter to Skatteetaten (Q24). | K2-13, fase1 K03, N13 Q5–Q6 |
| Q8 | Does the M0 employer have OTP, and how do the premium and AGA on the premium get in? | Decided in PLAN.md (D10) | Sjur | If there is OTP: the premium is entered by hand for the month it is paid. Brutto computes AGA on it (payment month, F-PEN-06/GC-17) and reports the pension provider in the a-melding. The premium itself is booked from the invoice (S #29). Ask the auditor about admin cost later. Needed by 13.11. | DQ19, K2-03, N16 |
| Q9 | What is the standard posting for the payroll voucher? | Decided in PLAN.md (D9) | Sjur | One aggregated voucher per run. Net pay as one line on 2930 (S #9). AGA per zone and rate. Holiday-pay accrual and AGA on it every run. Still to settle: the OTP account (S #29) and the grouping of 5390 (S #28 says 5000, assumed). Sjur confirms the accounts from his A07 mapping (S #27). Needed for the voucher file, about 14.12. The NAV refund receivable in M1 is entered by hand (PLAN.md §6.2); its account (1579 per the N-finding; F-REG-15 is LATER in `scope.csv`) is settled before M1. | K4-12, R02, N02, N30, MS4 |
| Q10 | **NEW:** Which manual a-melding channel and format work for the M0 employer after Altinn II roles stop, and who holds the access? | BLOCKS-M0 (format by 27.11; packages this week) | Sjur (packages); Peter and Sander (format) | Upload manually on skatteetaten.no with ID-porten (F-MYN-14, R2 §3.18), using the JSON the API takes. PLAN.md §1.3 relies on Skatteetaten's Q&A of 18.06.2026 **[verify by 27.11]**, with an XML 2.3 serialiser of the same aggregate as a costed fallback (+1–2 weeks), started at M0-α if the format is not confirmed. Check this week which people hold the Altinn 3 packages "A-ordningen" (a-melding and A07 download) and "Lønn" (tax cards) for the M0 employer (PLAN.md §2.4 item 3). The uploader must hold A-ordningen before the first live upload (period 2027-01, deadline 5.2.2027). Also confirm that the current system can still submit 2026-11 and 2026-12 after Altinn II roles stop on 17.11.2026. Rehearse in the test upload with a synthetic twin. | B19, B44, F-MYN-14, design dates, N14 |
| Q11 | **NEW:** Where do M0 tax cards come from? | Decided in PLAN.md (§1.4 item 4) | Sjur | Order them by hand through Skatteetaten's tax-card file service (RF-1211 format via ID-porten), which needs the Altinn package "Lønn" (A-ordningen does not cover tax cards), or copy them from the current system for as long as it keeps fetching. Enter them append-only with source and date and four eyes. Re-check before every run and every new hire. In January without a 2027 card, use the 2026 card and correct by the end of February (§§ 5-5-1, 5-5-2); otherwise 50 %. Switch to the API at gate MP. | B19, R2 §3.18, F-TRK-05 |
| Q12 | Does the team's own bank accept pain.001 upload, in which version, and with SALA? | BLOCKS-M0 | Peter | Get the bank's implementation guide and build only the version it requires (PLAN.md §2.4 item 7). Net pay as a SALA batch without employee addresses. Forskuddstrekk is its own payment order to Skatteetaten, not SALA, due the first working day after payout, with the KID from the a-melding feedback (upload on payday, then pay; PLAN.md §1.4 item 3). AGA is paid manually with KID by the 15th every other month. | DQ33, K4-04, B05, B07, N17 |
| Q13 | Who is tech lead, and what are the rules for coding agents? | Decided in PLAN.md (D5, E1) | Sjur, Peter, Sander | Name one tech lead at the Monday 2.11 meeting. Agents never edit golden cases, rate tables or expected values, and never touch production data. A human reads all code that touches money, access, authorities or crypto (B38), enforced with CODEOWNERS (E2). Golden cases gate CI. | DQ34, T02, B28, D-48 |
| Q14 | Which hosting region, and where do backups go? | Decided in PLAN.md (E4) | Peter, Sander | Azure Norway East (Postgres Flexible, General Purpose, and Key Vault) with backups in Norway. Test a restore before the first real run. No payroll data in telemetry outside Norway. Request Norway West for geo-backup this week (PLAN.md §2.4 item 10). | H01, DQ35, B9, MP1 |
| Q15 | How are money, history and tenants modelled? | Decided in PLAN.md (E5–E7) | Peter, Sander | rust_decimal and NUMERIC, with one named rounding function per legal rule and `f64` only inside the isolated withholding crate. Append-only versions with valid-from and recorded-at on data that drives calculation, plus an immutable input snapshot with input and result hashes per calculation. tenant_id on every row, with row-level security switched on before the first external customer. | D05, D08, D03, B6, B7 |
| Q16 | Which actions need a human, and what gets locked? | Decided in PLAN.md (D11, §1.3, §4) | All three | A named human who is not the preparer approves the run, with re-authentication through the identity provider in M0 and BankID step-up in M1. The approval hashes the result, the a-melding payload and the payment file, and any change voids it. A human also confirms bank-account changes, roles and "paid"; these are human-only operations that agent tokens cannot call. Everyone is in the same pay run, so someone approves their own pay: the exception is logged and reported to the board chair (D11). | J05, G04, G06, B41, B43 |
| Q17 | What is the a-melding aggregate strategy? | Decided in PLAN.md (§1.3, §4) | Peter, Sander | One message per opplysningspliktig per month, replaced on every change, built from a format-neutral aggregate. M0 serialises to the JSON the API takes, for manual upload (format: Q10); M1 sends it via the API, so F532 (from 2027-01) cannot trigger. XML 2.3 is only the costed fallback for the manual upload. 2.4 mapped by 1.7.2027 and accepted in test by 1.12.2027 (gates 24-S, 24-T). This makes Skatteetaten's F532 answer non-blocking. | DQ15, K4-02, B11, N14 |
| Q18 | Which language do API names use? | Decided in PLAN.md (E10) | Peter, Sander | English names in code, API and docs. Norwegian only for legal code values as Skatteetaten publishes them (`a_melding`, `a07`, `aga`). | J08 |
| Q19 | Which legal entity is the M0 employer, which company is the vendor, and who owns onboarding with Digdir, Skatteetaten and Altinn? | BLOCKS-M0 (D2, D3; by 6.11) | Sjur | Decide both this week (PLAN.md Start here, §2.4 item 1). The M0 employer comes with the D2 facts: current system and export formats, payday, bank and accounting system, holiday-pay rate, OTP and employee pension contribution, union dues through payroll, employees aged 59 or over, ongoing leave or garnishments, and who holds the Altinn packages. The vendor's orgnr is part of the Altinn system id, and changing it later means re-approval at every customer; if the vendor differs from the employer, check the regnskapsførerloven question and sign a DPA. Owner decided in D3: Sander, with Peter as deputy. Email the Altinn servicedesk to load the orgnr into TT02. Plan on about 3 months for onboarding; 7–10 weeks is the best case. | M01, M02, N06, N39, MS1 |
| Q20 | Who are the pilots? | BLOCKS-M1 | Sjur | Keep 2 byråer and 5–7 direct customers in the funnel to end with 3–5 direct customers (at most 5 and about 600 recipients, B25). A byrå can join M1 only with its own payroll, as a direct customer; its clients wait for M2 (B45). Screen out the profile exclusions (PLAN.md §6.1). Ask about their ledger, bank, Huma, pay types and OTP provider. Signed letters of intent by 31.3.2027 (gate G4), when the pilot-pulled items are chosen from their needs. Pilot conversations replace the 25-interview programme. | DQ04, DQ07, DQ08, DQ14, MS8 |
| Q21 | Who holds the payroll-domain veto, who is deputy, and who provides external answer keys? | BLOCKS-M1 (approach decided in PLAN.md D4) | Sjur | Sjur holds the veto. Contract an external payroll expert now, from November 2026 (PLAN.md §2.4 item 8): 20–30 hours for M0 and 100–150 before M1. The expert is also the B28 deputy and countersigns 20 % of the about 150 M1 golden cases. Naming the person blocks M1 (PLAN.md §10). | DQ02, DQ25, B28 |
| Q22 | What legal work is needed before signing pilots? | BLOCKS-M1 (order this week) | Sjur and a lawyer | One review (PLAN.md §2.3) covering the pilot agreement (software-only role, liability cap, support never approves or submits), the data processing agreement (DPA) on the EU standard clauses, a reference DPIA with art. 9(2)(b) as legal basis (covering the M1 MCP read and draft tools), the migration role and the regnskapsførerloven boundary, the Tripletex and PowerOffice API terms, and the copyright position of the withholding port. Huma, ZTL, "approve and sign" and the MCP addendum to the DPA (needed before agent submission) come later. | DQ25, DQ28, K6-04, H08, MS2, N19, N40 |
| Q23 | What is the default AGA method for NAV sick-pay refunds? | BLOCKS-M1 | Sjur | Deduct when the refund is received and documented (PLAN.md §6.2; to be confirmed, §10). In M1 the refund receivable is entered by hand, with a list of sick cases near the 3-month refund deadline; K27 import is LATER. One method per customer per year, locked. The full refund ledger comes later. | DQ13, K4-06, B33, N15 |
| Q24 | Which tax questions go to Skatteetaten now, in one letter? | BLOCKS-M0 (send this week) | Sjur | PLAN.md §2.3: the trekkrutine licence (we don't wait for the answer); rounding and the F185 tolerance; half withholding on percentage cards; June for part-year staff; KID positions 18–19; whether 24.12 and 31.12 are working days; the manual-upload format for 2027 periods (JSON or XML); and the 2027 annual cap for union dues. The rounding, upload-format, half-withholding, KID and union-dues answers serve M0 (PLAN.md §10). If there is room: frikort above the limit, the AGA term code, F532, the legal basis for the sammenstillingsoppgave, and income descriptions allowed after an end date. Organisation-life and garnishment details go in a later letter. | DQ09, DQ15, DQ17, DQ18, DQ26, K2-05/06/13, MS3, MS7 |
| Q25 | Which Altinn access packages do direct customers grant? | Decided in PLAN.md (§6.2) | Peter, Sander | A standard system user with `a-ordning` and `lonn`, which covers a-melding, tax cards and A07. The special-category package only when NAV APIs are built. In M0 the M0 employer's own people hold "A-ordningen" and "Lønn" (Q10, Q11). | K4-10, N06, N01, B10 |
| Q26 | Which ledger gets the one API adapter? | BLOCKS-M1 (pilot-pulled at G4) | Sjur, Peter, Sander | Only if a signed pilot needs it, chosen at G4 (31.3.2027); it is second in the M1 cut order. Then the ledger most pilots use, built only after written OK on its API terms (competition clause, N40). Post as a draft voucher. The voucher file always works for every ledger. | R01, N40, N02, N33 |
| Q27 | How does the first byrå connect its clients (M2)? | LATER (M2, B45) | Peter, Sander | Not an M1 question: M1 is direct customers only, and a byrå's own payroll can be an M1 pilot as a direct customer. For M2 (1.8.2028 if the pilots go live 2028-01, otherwise about 8.2029): the byrå must hold the REGN (authorised accountant) role and use an agent (client-system) system user with `regnskapsforer-lonn`. Clients are linked in the Altinn portal with a Brutto checklist, and byrå users get grants per client. Test in TT02 and in production for at least 3 clients first (gate M2). Option to cost now (B45): a firm runs a client as a direct-customer tenant in M1, the client approves a standard system user, and the firm's staff are users in that tenant. | DQ20, DQ21, K4-09, M09, M11, D04 |
| Q28 | How are pilots migrated? | BLOCKS-M1 | Sjur | Start pilots in a go-live window (1.1, 1.3 or 1.8), on 1 January where possible. Otherwise import year-to-date figures from an Excel template and check them against A07 (diff 0), and check the holiday-pay base against the old system's list and the 2940 balance. Keep arbeidsforhold-ID, start date and leave IDs (method 1), and bring ongoing sick cases and leave. The customer signs each import, Brutto issues the full-year sammenstillingsoppgave, and every pilot runs two parallel periods (gate P-PAR). | B16, K6-04, K6-06, K4-07, N35, DQ26 |
| Q29 | Which BankID broker? | BLOCKS-M1 | Peter, Sander | One broker (Criipto/Idura or Signicat), chosen on price. BankID for customer users and approvers, with step-up on approval and on account-number changes. M0 uses managed OIDC login (e.g. Entra ID) with MFA and a CLI device flow instead. Employees don't log in in M1: payslips go through Digipost, and the employee portal is LATER. | DQ36, I01, B14 |
| Q30 | Do we recruit two developers now, and does the runway match the pilot date? | BLOCKS-M0 (D12, by 6.11); the runway check BLOCKS-M1 | Sjur | D12: pilots live 1.8.2028 is the plan date. The stretch, pilots live 2028-01, needs two developers starting by 1.4.2027, so with three months' notice they must sign by 18.12.2026 (gate HIRE), and even then it is under 50 %. The decision needs a runway figure. Do not sign pilots unless the runway covers support through their first June and December (B23: at least 6 months after the pilots go live); recompute runway at actual burn in the G2 ADR (29.1.2027). | DQ01, B23, B25, B26 |

---

## 2. Questions for Peter and Sander (replaces `fase1.json`)

Payroll-first, grouped, 25 questions. Each has a proposal so it can be answered in the artefact the same way as today. "Replaces" lists the old ids it supersedes. Old ids not listed anywhere here are moot or later (see 3.3). PLAN.md §2.1 condenses the M0 proposals into the defaults E1–E10, adopted at the Monday 2.11 meeting unless someone objects: E1 = PS-01/PS-02, E2 = PS-03, E3 = PS-04, E4 = PS-05, E5 = PS-08/PS-09, E6 = PS-12, E7 = PS-06, E8 = PS-07, E9 = PS-14/PS-15, E10 = PS-07. PLAN.md also settles most of the rest. Per PLAN.md §10, the only open M0 questions for Peter and Sander are the bank's pain.001 version (PS-17) and the manual-upload format, by 27.11 (PS-16).

### A. Working agreement
- **PS-01 Who owns what in M0?** *Status:* Decided in PLAN.md (E1). *Why:* three people must cover calculation, outputs, infrastructure and authorities. *Proposal:* Sander owns the calculation engine (withholding, AGA, holiday pay), the a-melding aggregate and serializer, and authority onboarding. Peter owns hosting, security, login, the payment file, voucher export and payslip PDF, and is deputy for onboarding. Sjur owns pay types, golden cases and the comparison with the current system. One named tech lead. *Tier:* M0. *Replaces:* T01.
- **PS-02 Who is tech lead, and what are the rules for coding agents?** *Status:* Decided in PLAN.md (E1, D5). *Proposal:* One tech lead, named on 2.11, merges to the core. Agents never edit golden cases, rate tables or expected values, and never touch production data. A human reviews every change to money, access, authority and crypto code. *Tier:* M0. *Replaces:* T02 (with DQ34).
- **PS-03 What are the repo layout and CI gates?** *Status:* Decided in PLAN.md (E2). *Proposal:* A Cargo-workspace monorepo (`crates/`, `apps/api`, `apps/cli`; `web/` from M1). CI runs fmt, clippy `-D warnings`, tests including golden cases, the sqlx offline check, and cargo-deny/audit. Short ADRs in the repo. CODEOWNERS on money, access and authority code. *Tier:* M0†. *Replaces:* T03, T04, T05, H07.

### B. Architecture
- **PS-04 Confirm the base stack.** *Status:* Decided in PLAN.md (E3). *Proposal:* A modular monolith with one binary, axum, REST with OpenAPI generated from code (utoipa) and the spec committed, and Postgres with sqlx. No web UI and no MCP in M0: the interface is the `brutto` CLI over the REST API, with personal tokens and managed OIDC login (PS-22). M1 adds a minimal TypeScript + React admin UI for pilot payroll staff, using the generated client, with server-side session cookies. No job queue in M0; a Postgres queue arrives with M1. *Tier:* M0† (web UI M1). *Replaces:* A01–A05, J02, D01, D02, I03, U01.
- **PS-05 Which hosting, keys and backups?** *Status:* Decided in PLAN.md (E4). *Proposal:* Azure Norway East (Postgres Flexible, General Purpose, and Key Vault), daily backups in Norway, a restore test before the first real run, and no payroll data in telemetry outside Norway. Request Norway West for geo-backup now; backups in two Norwegian locations before M1. Local and production environments in M0; add a TT02-facing test environment in M1. IaC (OpenTofu) before the second environment. *Tier:* M0. *Replaces:* H01–H04, H06, A06.
- **PS-06 How are tenants separated?** *Status:* Decided in PLAN.md (E7). *Proposal:* tenant_id on every row from the first migration, with Postgres row-level security switched on before the first external tenant. A tenant is one customer with one or more opplysningspliktige. A byrå user is a user with grants to many tenants (M2, B45). One policy module checks all access. *Tier:* M0 (byrå part M2). *Replaces:* D03, D04, I04.
- **PS-07 Which API conventions are cheap now and expensive later?** *Status:* Decided in PLAN.md (E8, E10). *Proposal:* Every action is one named operation (stable id; read, write or human-only) in one catalogue, behind one `dispatch` with policy, idempotency, audit and masking, and actor context (person or agent, injected clock) on every call. English names, with Norwegian only for published legal code values. Idempotency keys on writes, problem+json errors with stable codes, cursor pagination, `/v1`, and money as decimal strings. Dry-run, SDKs and webhooks come later. *Tier:* M0†. *Replaces:* J07, J08, J09, A05.

### C. Money and calculation engine
- **PS-08 How are money and rounding handled?** *Status:* Decided in PLAN.md (E5). *Proposal:* `rust_decimal` in the domain and NUMERIC in the database, with `f64` only inside the isolated withholding crate (PS-09). Rounding happens only in named functions, one per legal rule (withholding, union dues in the base, AGA, holiday pay), and clippy bans ad-hoc `round`. Sjur supplies the rules (Q7, D8). *Tier:* M0. *Replaces:* D05, K03, MP2.
- **PS-09 How do we compute forskuddstrekk?** *Status:* Decided in PLAN.md (E5, Appendix A item 4). *Proposal:* Our own Rust port of Skatteetaten's published withholding rules, in `f64` with the Java order of operations, in an isolated crate, plus percentage cards. CI requires a 100 % match on every row of the published table file for 2026 and 2027. Nothing waits for the licence answer. *Tier:* M0. *Replaces:* L01.
- **PS-10 What shape does the engine have?** *Status:* Decided in PLAN.md (§1.3). *Proposal:* A pure function: inputs, rule pack and engine version give the result plus an explanation trace per line. Rates (AGA per zone, holiday-pay %, G, tables) are versioned data with valid-from dates. *Tier:* M0†. *Replaces:* L02.
- **PS-11 What exactly does the M0 engine cover?** *Status:* Decided in PLAN.md (§1.1, §1.5). *Proposal:* Fixed monthly salary (pro rata on start or end mid-month), hourly (quantity × rate), one-off additions and deductions, table and percentage withholding (frikort, halvt trekk in December on flagged lines, 50 % without a card, capped at cash pay), AGA per virksomhet and zone (including AGA on an OTP premium in the month it is paid), holiday-pay base and accrual (10.2 % or 12 %), and union dues. Union dues reduce the withholding base (skattebetalingsforskriften § 5-9-1, rounded up, within the annual cap [verify the 2027 cap]) and are then deducted from net pay; research report C (#48, "after tax") is wrong on this (PLAN.md §1.4, §7.4). Not in M0: the 60+ supplement and holiday-pay payout (M0+ track, gate JUN27), sick pay and refunds, garnishment and the OTP employee contribution (M1); retro and tariffs (later). *Tier:* M0. *Replaces:* new (was P05/P08 territory).

### D. Data model and history
- **PS-12 Which data carries history, and how are approved runs frozen?** *Status:* Decided in PLAN.md (E6). *Proposal:* Append-only versions with `valid_from` and `recorded_at` for employment (position %, salary, department), tax card, pay types, virksomhet (zone) and rates. Each calculation stores an immutable input snapshot plus input and result hashes, and corrections are new runs. No general bitemporal query layer. *Tier:* M0. *Replaces:* D08.
- **PS-13 What are the person/employment model and ids?** *Status:* Decided in PLAN.md (§1.3, §4). *Proposal:* UUIDv7 internally. The arbeidsforhold-ID and the leave ID (permisjons-ID) are short, stable strings per opplysningspliktig, and imported ids are kept unchanged. All fields the a-melding requires are mandatory: occupation code, employment type, working-hours arrangement, position %, start and end with reason. *Tier:* M0†. *Replaces:* D06, L03, N35 Q3.
- **PS-14 How is personal data protected in M0 and in M1?** *Status:* Decided in PLAN.md (E9). *Proposal:* M0: disk encryption, field encryption with one key and a blind index for national id and account numbers from the first migration, masking by default in the API and CLI, no personal data in logs or telemetry (filtered in code), and payroll data only for the payroll roles. Before M1: one key per tenant (envelope), logged reads of sensitive fields, and masking in list responses and in MCP. *Tier:* M0 (per-tenant keys, read log and MCP masking M1). *Replaces:* D09, H05, J10 (API part).
- **PS-15 What does the audit log look like?** *Status:* Decided in PLAN.md (E9). *Proposal:* An append-only table from the first migration for every write, approval, export and authority call: who (person or agent, and on whose behalf), what, when, why, channel, and a before/after hash. The hash chain comes later, before ISAE. From M2, byrå person and client are on every authority call. *Tier:* M0†. *Replaces:* D10, M08, M12.

### E. Outputs of a payroll run
- **PS-16 How is the a-melding built and checked?** *Status:* Open: the upload format, by 27.11 (PLAN.md §10); the rest decided in PLAN.md (§1.3). *Proposal:* A format-neutral aggregate per opplysningspliktig and month, replaced on change. The M0 serializer is the JSON the API takes, uploaded manually (F-MYN-14); M1 sends the same JSON via the API. JSON for 2027 periods rests on Skatteetaten's Q&A of 18.06.2026 [verify by 27.11; also asked in the letter]. An XML 2.3 serializer of the same aggregate is a costed fallback (+1–2 weeks), started at M0-α if the format is not confirmed. CI validates against JSON Schema and Brutto's own copy of the key business rules (about 10 hard checks in M0). Rehearse with a synthetic twin in Skatteetaten's test upload, and compare with the current system's submitted a-melding. Version 2.4: spec by 1.5.2027, mapping by 1.7.2027, in test by 1.12.2027 (gates 24-S, 24-T). *Tier:* M0. *Replaces:* new (B11, N14 Q1–Q3).
- **PS-17 How is the payment file built?** *Status:* Open: our bank's pain.001 version (PLAN.md §10); the rest decided in PLAN.md (§1.4 item 3). *Proposal:* pain.001 in the version our bank requires. Net pay as a SALA batch without employee addresses. The file shows count, sum and hash to the approver. Forskuddstrekk is its own payment order to Skatteetaten, not SALA, due the first working day after payout, with the KID from the a-melding feedback (upload on payday, then pay). Brutto computes the KID itself only in M1, after it reproduces every 2026 KID [verify positions 18–19]. AGA is paid manually in M0. M1 adds deductions to creditors as separate payments, and returned payments. "Paid" is confirmed manually. *Tier:* M0. *Replaces:* B05–B08.
- **PS-18 How is the accounting voucher built?** *Status:* Decided in PLAN.md (D9, §1.3). *Proposal:* One aggregated voucher per run, with net pay on 2930 collectively and a run reference of 20 characters or fewer. M0 delivers CSV in the import format of our own ledger. The payroll journal comes as PDF and CSV and is archived with a hash, plus one run export (CSV). M1 adds one API adapter that posts a draft voucher, only if a pilot pulls it at G4 and after written OK on its API terms; customer tokens are kept in Key Vault. *Tier:* M0 (adapter M1, pilot-pulled). *Replaces:* R01–R03, N02, N30, N33.
- **PS-19 How is the payslip produced and delivered?** *Status:* Decided in PLAN.md (§1.3, §6.2). *Proposal:* A Typst template producing PDF/A, archived with hash in Norway for 5 years after the end of the accounting year. In M0 it is delivered by download or by the admin. M1 sends payslips and the annual statement through Digipost (bought, F-POR-12), with Digipost print as fallback and manual secure delivery for employees without a digital mailbox (F-POR-04). The employee portal, employee login and e-mail notices are LATER (F-POR-01, -27, -28). Digipost is sixth in the M1 cut order; if it goes, manual secure delivery replaces it. *Tier:* M0† (Digipost M1). *Replaces:* new (N08 spike 6).

### F. Approval and control
- **PS-20 How does approval work?** *Status:* Decided in PLAN.md (§1.3, D11). *Proposal:* One approval step by a named human who is not the preparer, with re-authentication through the identity provider in M0 and BankID step-up in M1. In M0 someone approves their own pay (D11): the exception is logged and reported to the board chair. Approval hashes the result, the a-melding payload and the payment file, and any change voids it. After approval, each output has its own status (payslip, payment, voucher, a-melding). Configurable multi-step flows come later. *Tier:* M0. *Replaces:* J05, G04, G06 (G01–G03, G05, G07 → later).
- **PS-21 Which checks run before approval in M0?** *Status:* Decided in PLAN.md (§1.3). *Proposal:* An attestation summary before approval (F-RAP-16): totals including withholding per payout date, AGA per zone and holiday-pay accrual. Difference against last month and against the current system (parallel run). Withholding against the table, AGA as base × rate per zone, gross − withholding − deductions = net = payment-file sum, no zero or negative net, and a-melding validation with about 10 hard checks. Checks are code with id and version, and tolerances are data. *Tier:* M0. *Replaces:* P05, K01, K02, K04, K05.

### G. Identity and access
- **PS-22 How do users log in, and which roles exist?** *Status:* Decided in PLAN.md (§1.3). *Proposal:* M0: managed OIDC login (e.g. Entra ID) with MFA and a CLI device flow for the three of us, personal accounts only, re-authentication through the identity provider on approval and bank-account change, and two roles as code: payroll admin and approver. No BankID in M0. M1: BankID via a broker for customer users and approvers, with step-up on approval; roles per tenant. Employees don't log in in M1 (payslips via Digipost); employee login is LATER. A byrå role with client grants comes in M2. *Tier:* M0 (BankID M1, byrå M2). *Replaces:* I01, I02.

### H. Authorities (the M1 critical path)
- **PS-23 How do we connect to Maskinporten and system users?** *Status:* Decided in PLAN.md (D3, §6.2). *Proposal:* Our own JWK in Key Vault, signed by the key vault, and a small Rust client of our own. A standard system user per direct customer (`a-ordning` + `lonn`); our own company uses it as soon as gate MP passes (31.3.2027, best case 29.1.2027). The agent (client-system) system user for byråer, with clients linked in the Altinn portal, comes in M2. Registration starts this week, owned by Sander with Peter as deputy. *Tier:* M1 (agent system user M2). *Replaces:* M01, M03, M04, M05, M09, M13.
- **PS-24 What do we use from Skatteetaten in M1, and in what order?** *Status:* Decided in PLAN.md (§6.2). *Proposal:* (1) a-melding submission with feedback polling, (2) tax-card fetch (polling only from 15.12.2026), (3) A07 on demand as the answer key for migration and parallel runs, never nightly. Raw responses are stored encrypted. TT02 with Tenor test persons, running the N22 test plan. Manual upload stays as fallback. Trekkpålegg, K27 (import and API; M1 enters the NAV refund receivable by hand), inntektsmelding (filed in NAV's portal), Dialogporten and Altinn Events come later. *Tier:* M1. *Replaces:* M06, M07, M10, M11, D07, J06.

### I. API and MCP scope
- **PS-25 What remains of B41 in M0 and M1?** *Status:* Decided in PLAN.md (§4, §8 B41). *Proposal:* B41 narrowed. The API is the application layer: one operation catalogue behind one `dispatch` (PS-07). REST, the `brutto` CLI, MCP and the M1 web UI are thin clients, so parity comes from the structure and the CI parity test is cut. **M0: no MCP at all** while real payroll data is in the system; the `brutto` CLI over REST is the interface. **M1:** remote MCP with read tools, draft tools (pay inputs and run drafts) and two generic tools. Actions with legal effect (approve, submit, pay, change a bank account or a role) are human-only operations in Brutto; agent tokens cannot call them. Agent tokens are issued by a named human, and there is no OAuth server in M1. National id, bank account, protected address, health and union data never leave via MCP, and MCP is off by default per tenant. MCP draft tools are first in the M1 cut order; read-only MCP stays. **LATER:** agent-started actions with a human BankID confirmation (F-PLA-37), agent submission for customers (after the DPIA and an MCP addendum to the DPA), the OAuth server, webhooks, a developer portal beyond the generated API reference, and SDKs beyond the generated TypeScript client. Agent evals and the assistant also wait. *Tier:* M0 (CLI, catalogue); MCP read and draft tools M1. *Replaces:* J01, J03, J04, J10 (MCP part), J11–J13, X01–X05.

---

## 3. Full triage list

### 3.0 Counts

| Source | Items | BLOCKS-M0 | BLOCKS-M1 | LATER | MOOT |
|---|---|---|---|---|---|
| design.json `sporsmal` | 36 | 8 | 11 | 14 | 3 |
| omr-K1..K7 `sporsmal` | 105 | 9 | 16 | 55 | 25 |
| fase1.json | 105 | 42 | 22 | 27 | 14 |
| natt N-items (N01–N40, incl. deferred N22) | 40 | 8 | 9 | 14 | 9 |
| morgen.md (MS1–8, MP1–8) | 16 | 5 | 6 | 1 | 4 |
| morgen.md recommended mapping changes | 18 | 2 | 7 | 7 | 2 |

(The dagger variants count in their base tier. "LATER (M2)" counts as LATER: DQ20, K4-09, D04, M09, M11 and M12. Many M0/M1 items are duplicates of each other; section 1 deduplicates them into 30. Counts updated 29.10.2026 to agree with PLAN.md: no web UI and no MCP in M0, field encryption and the withholding KID payment in M0, MCP read and draft tools in M1, payslips via Digipost in M1 (K5-07 to LATER), F-REG-15 LATER as in `scope.csv`, byrå items to M2.)

### 3.1 design.json `sporsmal` (DQ01–DQ36)

| Id | Question (short) | Tier | Note / recommended answer |
|---|---|---|---|
| DQ01 | Capital secured and runway | BLOCKS-M1 | Q30. Pilots live 1.8.2028 in the plan; 2028-01 needs two developers signed by 18.12.2026 (D12, gate HIRE). The runway must cover support through the pilots' first June and December (B23). |
| DQ02 | Payroll experts no. 1 and 2; how much can Sjur be the answer key | BLOCKS-M0 | Sjur is the answer key for M0, using the last 3 months from the current system as golden cases. The external payroll expert is contracted from November 2026: 20–30 h for M0, 100–150 h before M1, and the B28 deputy (D4, Q21). |
| DQ03 | What gives first: date, scope, quality | BLOCKS-M0 | Q2: quality, date, scope. |
| DQ04 | Which byråer and direct customers become pilots | BLOCKS-M1 | Q20. |
| DQ05 | When do the vacation/absence and time modules come | LATER | After M1. M1 keeps the legal core inside payroll (AGP, sick-pay lines, leave codes, holiday pay and ferietrekk), with hours via CSV. |
| DQ06 | Extended pay-type model; OTP premium input | BLOCKS-M0 | Q4 and Q8. |
| DQ07 | Interview 15 byråer and 10 organisations | LATER | Fold the pilot-relevant part into Q20. The full programme is not needed to build. |
| DQ08 | How many OrgLab customers have ≥10 employees | LATER | Only for segment sequencing after M1. Ask during pilot screening. |
| DQ09 | May Brutto use Skatteetaten's trekkrutine | BLOCKS-M0 | Q6 (decided in PLAN.md): our own Rust port of the published rules, checked 100 % against the table file; licence asked in parallel, not waited for. The Kotlin/JVM argument is moot since Rust is decided. |
| DQ10 | Fees: lost earnings, board fee to an employee, zone for freelancers, 10 000 limit | LATER | Organisation life. Screen these cases out of the pilots, and ask in the second Skatteetaten letter. |
| DQ11 | Keep the Huma-replacement goal internal; what triggers HR | MOOT | HR comes after payroll (B34). Keep the goal internal and decide the trigger after M1. |
| DQ12 | First customers in early live use; own company first | MOOT | Answered by B19 (reworded) and B44: shadow run Nov–Dec 2026, Brutto system of record from period 2027-02 (planning date) or 2027-01 (stretch) (Q1). |
| DQ13 | Default AGA method for NAV refunds | BLOCKS-M1 | Q23: deduct when received. |
| DQ14 | How many pilots use Huma | LATER | Ask during pilot screening. No Huma connector unless a signed pilot needs it. |
| DQ15 | F532 per message or per month | BLOCKS-M0 | Design default (Q17). Skatteetaten's answer is not needed. |
| DQ16 | Correcting 2027 periods after 2.4 | LATER | Needed by Q3 2027. Brutto holds all of its own 2027 periods anyway. |
| DQ17 | KID algorithm, AGA term code, 24.12/31.12 | BLOCKS-M1 | M0 takes the forskuddstrekk KID from the a-melding feedback (upload on payday, then pay; PLAN.md §1.4 item 3). Brutto computes its own KID only in M1, after it reproduces every 2026 KID [verify positions 18–19; asked in the letter, Q24]. 24.12/31.12 is needed before the first December payout made in Brutto (December 2027). |
| DQ18 | Halvt trekk and tax-free June in special cases | BLOCKS-M1 | Before the first June or December run of a pilot. Send in the letter (Q24). |
| DQ19 | AGA on OTP premium: timing, admin cost, zone | BLOCKS-M0 | Q8 (only if the M0 employer has OTP). One zone, so only timing matters, and the payment month is the default. |
| DQ20 | Byrå client system without REGN; 5-call quota | LATER (M2) | Q27 (M2): require REGN for the first byrå. The quota is irrelevant at that volume. |
| DQ21 | ID-porten client for client delegation | LATER | Use the Altinn portal as standard and apply in parallel. |
| DQ22 | Which inntektsmeldinger (income reports to NAV) can be sent from a payroll system | LATER | Inntektsmelding in NAV's portal in M1 (PLAN.md §6.2). Not relevant for M0. |
| DQ23 | Bidragstrekk (child-support deduction) in the trekkpålegg API | LATER | Registered manually from letters in M1. |
| DQ24 | Fixed work plan with registered deviations, aml. § 10-7 | LATER | Time module. |
| DQ25 | Calculation guarantee and veto | BLOCKS-M1 | Q21 and Q22. A capped commitment in the pilot agreement. |
| DQ26 | Legal basis and deadline for the sammenstillingsoppgave | BLOCKS-M1 | Avoided for 2026 by D1/B44. Needed for Brutto's own 2027 statement by 14.1.2028 (gate AS27; legal deadline 31.1.2028) and for mid-year pilot starts (Q28). |
| DQ27 | Bokføringsforskriften § 7-5 or § 7-7; must backup be elsewhere | MOOT | Moot if both primary data and backup stay in Norway (Q14). Revisit only if that changes. |
| DQ28 | Legal basis and DPIA for health and union data | BLOCKS-M1 | Q22: art. 9(2)(b), same protection as payroll data (S §2 pkt 7), reference DPIA. |
| DQ29 | Privacy when the customer's agent reads and writes via MCP | BLOCKS-M1 | M1 has remote MCP with read and draft tools, off by default per tenant; national id, bank account, protected address, health and union data never leave via MCP, and actions with legal effect are human-only operations that agent tokens cannot call (PS-25). No MCP in M0. Cover it in the reference DPIA (Q22). Agent-started actions and agent submission wait for the DPIA and an MCP addendum to the DPA. |
| DQ30 | Who owns Utleggsappen, OrgLab, Tikket; what they were promised | LATER | Integrations come after M1. |
| DQ31 | Receipt archive and VAT for expenses | LATER | Expenses via integration come after M1. |
| DQ32 | Huma API access, retries, document export | LATER | |
| DQ33 | Which pain.001 version the pilot banks need | BLOCKS-M0 | Q12 for the team's own bank. Pilot banks at M1. |
| DQ34 | Tech lead and quality of agent-written code | BLOCKS-M0 | Q13. |
| DQ35 | Backup in Azure Norway West or with a Norwegian provider | BLOCKS-M1 | M0: zone-redundant Norway East backups. A geo-separated Norwegian backup before M1. |
| DQ36 | BankID broker and price | BLOCKS-M1 | Q29. |

### 3.2 Area questions (`omr-K*.json`)

| Id | Area | Question (short) | Tier | Note / recommended answer |
|---|---|---|---|---|
| K1-01 | PER | Arbeidsforhold-ID when moving between sub-units: unique per what | LATER | One sub-unit per employee in M0/M1. Brutto issues new ids and keeps imported ids (method 1). |
| K1-02 | PER | End reason on death | LATER | Rare. Handle manually and include in the second letter. |
| K1-03 | PER | Gender in the personnel register | LATER | Not in the a-melding. Only for equality reporting (ARP) and pay-gap reports. |
| K1-04 | PER | Protected addresses without Folkeregisteret | LATER | M1 simplification: no employee addresses in bank files or reports, plus a manual "protected" flag. |
| K1-05 | ORG | Fribeløp (AGA allowance) per enterprise and other de minimis aid in groups | LATER | Groups that share fribeløp are excluded (B3). A single-entity counter only if a pilot is in a fribeløp zone. |
| K1-06 | ORG | From which month a new AGA zone applies after a move | LATER | Rare. Zone is a dated field set manually. |
| K1-07 | PER | Huma dates, end reason, API terms | LATER | |
| K1-08 | HR | Whistleblowing and HSE deviations outside Brutto | MOOT | HR expansion (B34). Keep outside and use a partner. |
| K1-09 | PER | a-melding code-list changes from 2030 | LATER | Revisit in 2029. |
| K1-10 | ORG | Simplified a-melding for charitable organisations | MOOT | Below the segment. Local branches are excluded (B3). |
| K1-11 | PER | Pay step (lønnstrinn) on position period or pay agreement | MOOT | No pay scales before tariffs, which come after M1. |
| K1-12 | ORG | Hourly rates for Forskningsrådet/Horizon | MOOT | CUT. Project-cost reporting is not core payroll. |
| K2-01 | LON | Extended pay-type model must be approved | BLOCKS-M0 | Q4. |
| K2-02 | LON | Meaning of the ten standard pay types | BLOCKS-M0 | Q5. |
| K2-03 | PEN | How the OTP premium comes in, and AGA on it | BLOCKS-M0 | Q8 (if OTP). |
| K2-04 | TRK | Licence for the trekkrutine | BLOCKS-M0 | Q6. |
| K2-05 | TRK | Table vs percentage, halvt trekk, June, special cases, `antallMaanederForTrekk` | BLOCKS-M1 | M0: regular monthly pay uses the table, everything else the percentage, 10.5 months standard. Special cases before the first June or December. |
| K2-06 | TRK | Frikort (exemption card) above the limit | BLOCKS-M1 | Hourly staff with frikort are likely among pilots. Ask (Q24) and flag cases for manual check meanwhile. |
| K2-07 | TRK | Garnishment that cannot be fully deducted | LATER | M1 manual register. Carry-forward decided case by case. |
| K2-08 | TRK | Bidragstrekk channel and code | LATER | Manual from letters. |
| K2-09 | TRK | Protected amount for agreed deductions | LATER | M1: warn when net pay falls below a threshold set per customer. |
| K2-10 | KJO | Which G for the 6G cap, wage guarantee, pension | LATER | The provider computes OTP and NAV computes refunds. The 60+ holiday-pay cap is needed before the first June payout: gate JUN27 uses the G in force on 31.12.2026 for the 6 G cap (ferieloven § 10 (3)). |
| K2-11 | KJO | Default for retro of ferietrekk | LATER | Retro is excluded. |
| K2-12 | KJO | The "4/26" ferietrekk method | LATER | M1 has one default method, the one the current system uses. |
| K2-13 | KJO | Rounding of percentage withholding and net pay | BLOCKS-M0 | Q7. |
| K2-14 | KJO | Reporting salary advances | LATER | Manual. |
| K2-15 | PEN | Tax status of treatment insurance; group-life limit | LATER | Enter as a manual taxable-benefit line if a pilot needs it. |
| K2-16 | PEN | OTP rates 2026–2027 | LATER | Brutto does not compute premiums (S #29). Only for a later minimum-rate control. |
| K2-17 | PEN | KLP/SPK file format and approval | MOOT | Public-sector pension is excluded (B3). |
| K2-18 | LON | Pay settlement (lønnsoppgjør) as core or HR module | MOOT | CUT until a paying customer asks. |
| K2-19 | KJO | Ownership of D-Tariffavtale and the AGA calculation | BLOCKS-M0 | AGA part only: computed in KJO per virksomhet and zone, reported by MYN. Tariff part later. |
| K2-20 | TRK | Net-salary agreements and PAYE in the a-melding | MOOT | Excluded (B3). |
| K3-01 | FRA | New permittering (temporary layoff) fields in the a-melding | LATER | Permittering is not in M1. |
| K3-02 | UTL | Passenger name in a-melding or travel claim | MOOT | Expenses via integration later. |
| K3-03 | UTL | Mileage allowance code and km field | BLOCKS-M1 | Only if mileage is a pilot pay type. Sjur decides from Skatteetaten guidance. |
| K3-04 | TID | Fixed plan with deviations (§ 10-7) | LATER | Duplicate of DQ24. |
| K3-05 | UTL | Who owns VAT and the receipt archive | LATER | Duplicate of DQ31. |
| K3-06 | FRA | Is the core always the answer key for holiday balance | LATER | M1 tracks holiday pay (money) and days taken for ferietrekk only. |
| K3-07 | FRA | Holiday for part-time and shift workers: days or hours | LATER | Shift rosters are excluded. |
| K3-08 | UTL | State rates for passenger and night allowance | LATER | |
| K3-09 | UTL | Utleggsappen contract | LATER | |
| K3-10 | FRA | Counting rules for partial layoff | LATER | |
| K3-11 | FRA | Retention of sick notes | LATER | M1 stores no sick-note documents, only period, degree and AGP days. |
| K3-12 | TID | Start/stop in an app | MOOT | CUT: no punch clock. |
| K3-13 | TID | Which tariffs first | LATER | No tariffs before M1+. |
| K3-14 | FRA | Self-certified sick leave "4 per 12 months" | LATER | Warn, never block. |
| K4-01 | MYN | KID check digit and AGA term code | BLOCKS-M1 | Duplicate of DQ17. M0 takes the KID from the a-melding feedback. |
| K4-02 | MYN | F532 per message or per month | BLOCKS-M0 | Duplicate of DQ15. Design default. |
| K4-03 | MYN | Correcting 2027 periods after 2.4 | LATER | Duplicate of DQ16. |
| K4-04 | BET | pain.001 version, SALA, several execution dates | BLOCKS-M0 | Q12 for the own bank. Pilot banks in M1. |
| K4-05 | BET | Are 24.12 and 31.12 working days for withholding due dates | BLOCKS-M1 | Before the first December payout made in Brutto. |
| K4-06 | MYN | Default AGA method for NAV refunds | BLOCKS-M1 | Duplicate of DQ13 (Q23). |
| K4-07 | MYN | Sammenstillingsoppgave: legal basis, deadline, sender | BLOCKS-M1 | Duplicate of DQ26. Avoided in M0 by the January cutover. |
| K4-08 | MYN | Inntektsmelding beyond sick pay | LATER | Duplicate of DQ22. |
| K4-09 | MYN | Client delegation, REGN role, quota | LATER (M2) | Byråer only (Q27, B45). |
| K4-10 | MYN | Special-category package from start or at the first NAV case | BLOCKS-M1 | Q25: `a-ordning` + `lonn`. Special category later. |
| K4-11 | REG | Grouping codes and SAF-T | LATER | Needed for ledger reconciliation, not for payroll vouchers. |
| K4-12 | REG | Contra accounts 2930 (gross) and 1580 (refund) | BLOCKS-M0 | Q9: 2930 collectively. The M1 refund receivable is entered by hand; its account is settled before M1 (F-REG-15 is LATER in `scope.csv`). |
| K4-13 | REG | Should the AGA lock be absolute | LATER | M0/M1: a warning 5 working days before the 15th, never a lock. |
| K4-14 | BET | Payout date when net pay is returned or moved | LATER | Handled by a manual correction run. |
| K4-15 | BET | Quarantine in the account-number shield | BLOCKS-M1 | Four-eyes approval plus notice to the employee, no quarantine. BankID self-service later. |
| K4-16 | REG | Is the union-dues account (2650) sensitive | BLOCKS-M1 | Post collectively without employee dimension or name. Detail only in Brutto, behind payroll access. |
| K4-17 | MYN | resourceFilter for a-melding feedback in Altinn Events | LATER | M1 polls for feedback. |
| K4-18 | BET | Multibank channel and order of bank APIs | LATER | B40. |
| K4-19 | MYN | One case queue for calculation and authority errors | LATER | M1 uses one simple deviation list. |
| K5-01 | ORL | Lost earnings (tapt arbeidsfortjeneste) | LATER | Duplicate of DQ10. |
| K5-02 | ORL | Board fee to someone who is also an employee | LATER | Screen pilots for employee board members. Ask Skatteetaten. |
| K5-03 | ORL | AGA zone for freelance relationships | LATER | |
| K5-04 | ORL | The 10 000 limit | LATER | |
| K5-05 | ORL | Artist tax and the a-melding | MOOT | Artists are excluded (Tikket comes later). |
| K5-06 | ORL | Altinn access when a central body runs local branches' payroll | MOOT | Local branches are excluded (B3). |
| K5-07 | POR | How long leavers keep access | LATER | Employees don't log in in M1: payslips go to their Digipost mailbox (F-POR-12). BankID access for former employees comes with the employee portal (F-POR-28, LATER). |
| K5-08 | POR | Fallback for employees without BankID or Digipost | BLOCKS-M1 | Digipost print, or manual secure delivery (in person or as an encrypted PDF) in M1 (F-POR-04). |
| K5-09 | BYR | Controller role for byrå engagement documentation | LATER | |
| K5-10 | BYR | Time measurement in the byrå as a control measure | MOOT | CUT (time-suggestion feature). |
| K5-11 | BYR | Is e-mail approval enough under GRFS 8.6 | LATER | M1 stores the client-approval attachment with a hash. The byrå's own routine applies. |
| K5-12 | BYR | Proof that withholding was paid | LATER | |
| K5-13 | LED | Boundary between the approval entities | LATER | M1 approves payroll runs only. |
| K5-14 | ORL | Union, party or church positions as special category | MOOT | Organisation life later. |
| K5-15 | BYR | AI interpretation of unstructured input | MOOT | CUT. |
| K5-16 | ORL | Does Brutto own RF-1301 reporting | MOOT | CUT: sole-trader (ENK) payments are not payroll. |
| K5-17 | ORL | Frikjøp (buy-out of working time) model A without reporting duty | MOOT | Organisation life later. |
| K6-01 | SIK | Backup in Norway; § 7-5 or § 7-7 | BLOCKS-M1 | Moot if everything is in Norway. A geo-separated Norwegian backup before M1. |
| K6-02 | RAP | Minimum group size in statistics | LATER | |
| K6-03 | SIK | Separate "Payroll: health" role | BLOCKS-M1 | Same protection as payroll data in M1. A separate role later. |
| K6-04 | MIG | Who enters data at migration without becoming the accountant | BLOCKS-M1 | The customer signs each import job (a byrå from M2). Brutto staff prepare only. Lawyer confirms (Q22). |
| K6-05 | MIG | Format for correcting pre-transition periods | LATER | |
| K6-06 | MIG | Sammenstilling when switching mid-year | BLOCKS-M1 | Q28. Prefer 1 January starts. |
| K6-07 | MIG | End-reason code under method 3 | LATER | M1 uses method 1 only. |
| K6-08 | MIG | API access to Visma.net Payroll, PowerOffice, SD Worx | LATER | Excel-template import. |
| K6-09 | PLA | Huma API terms | LATER | |
| K6-10 | RAP | Limits of the report builder | MOOT | CUT. Fixed reports plus the API. |
| K6-11 | PLA | Price unit and usage metering | LATER | Flat pilot fee. |
| K6-12 | PLA | Payroll data via MCP (B41) | BLOCKS-M1 | Duplicate of DQ29 (PS-25). |
| K6-13 | RAP | ESG and pay transparency | LATER | VSME is cut. Pay transparency when Norwegian law requires it. |
| K6-14 | SIK | Auditor access | LATER | M1 provides exports. |
| K6-15 | SIK | Test data for trekkpålegg and NAV | LATER | |
| K7-01 | KOM | Boundary between KOM and LED/POR for inbox and notices | MOOT | HR expansion (B34). |
| K7-02 | HEL | New entities D-Oppfolgingssak, D-Oppgave, D-Varselregel | MOOT | HR expansion. |
| K7-03 | HEL | Follow-up case vs sick-leave case | MOOT | HR expansion. AGP counting stays in the payroll core. |
| K7-04 | HEL | NAV sick-leave follow-up APIs | MOOT | HR expansion. |
| K7-05 | HEL | Retention and legal basis for HR data | MOOT | HR expansion. |
| K7-06 | HEL | One health role or three | MOOT | M1 uses payroll-level protection. |
| K7-07 | UTV | Build or partner for employee development | MOOT | HR expansion. Partner recommended. |
| K7-08 | HEL | Occupational health service provider on the virksomhet | MOOT | HR expansion. |

### 3.3 `fase1.json` (105)

| Id | Question (short) | Tier | Note → new id |
|---|---|---|---|
| P01 | What to reconcile A07 against | MOOT | Written for the read-only tool. In M1, A07 is checked against Brutto's own a-melding. Ledger reconciliation later. |
| P02 | Who is the first user | MOOT | Answered: our own company (M0), then 3–5 direct customers (M1), then byråer (M2, B45). |
| P03 | Where the employee overview comes from | MOOT | Answered: Brutto is master. A07/Excel only for migration. |
| P04 | When phase 1 is done | BLOCKS-M0 | Q3 (M0 exit criterion). |
| P05 | Which controls first | BLOCKS-M0 | PS-21. Pre-approval checks replace the ledger controls. |
| P06 | Which graphs | LATER | Cut from M1. The numbers are available in the API. |
| P07 | How far back to fetch data | MOOT | No A07 fetch in M0. M1 fetches the current and previous year for migration. |
| P08 | Approval flow and payment in phase 1 | MOOT | Answered: one approval step plus pain.001 (PS-20, PS-17). |
| P09 | When Brutto runs payroll | MOOT | Answered (B19 reworded, B44, Q1). |
| T01 | Who owns what | BLOCKS-M0 | PS-01. |
| T02 | Rust experience; how much agents write | BLOCKS-M0 | PS-02. |
| T03 | Repo layout | BLOCKS-M0† | PS-03. |
| T04 | CI gates | BLOCKS-M0† | PS-03. |
| T05 | ADRs | LATER† | PS-03: adopt. |
| A01 | Monolith or services | BLOCKS-M0† | PS-04. |
| A02 | Web framework | BLOCKS-M0† | PS-04. |
| A03 | API style | BLOCKS-M0† | PS-04. |
| A04 | Background jobs | BLOCKS-M1† | PS-04: none in M0. |
| A05 | Error handling | BLOCKS-M0† | PS-07. |
| A06 | Config and secrets | BLOCKS-M0† | PS-05. |
| J01 | UI/API/MCP parity in CI | MOOT | Cut (B41 narrowed): parity comes from the operation catalogue (PS-25). |
| J02 | Contract-first or code-first | BLOCKS-M0† | PS-04. |
| J03 | MCP server design | BLOCKS-M1 | PS-25: remote MCP with read tools, draft tools and two generic tools in M1; actions with legal effect are human-only. No MCP in M0. |
| J04 | Agent login (OAuth 2.1) | LATER | PS-25: OAuth server later. |
| J05 | Which actions a human confirms | BLOCKS-M0 | PS-20, Q16. |
| J06 | Long-running jobs via API/MCP | LATER | PS-24: simple 202 plus status in M1. |
| J07 | Endpoint requirements | BLOCKS-M0† | PS-07. |
| J08 | Norwegian or English names | BLOCKS-M0 | PS-07, Q18. |
| J09 | API versioning | BLOCKS-M1† | PS-07. |
| J10 | Limiting personal data via MCP | BLOCKS-M1 | PS-25: national id, bank account, protected address, health and union data never leave via MCP; MCP off by default per tenant. Masking for external users in M1 (PS-14). |
| J11 | SDK and CLI | BLOCKS-M0 | PS-25: the `brutto` CLI over REST is the M0 interface. SDKs beyond the generated TypeScript client later. |
| J12 | Agent evals | LATER | |
| J13 | What to cut to make room for API/MCP | MOOT | Superseded by PLAN.md (B41 narrowed). |
| D01 | Database | BLOCKS-M0† | PS-04. |
| D02 | Database library | BLOCKS-M0† | PS-04. |
| D03 | Tenant separation | BLOCKS-M0 | PS-06. |
| D04 | Byrå and client model | LATER (M2) | PS-06, Q27: keep tenant and grants generic so M2 fits. |
| D05 | Money storage | BLOCKS-M0 | PS-08. |
| D06 | Ids | BLOCKS-M0† | PS-13. |
| D07 | Store raw Skatteetaten data | BLOCKS-M1 | PS-24. |
| D08 | How much history now | BLOCKS-M0 | PS-12. |
| D09 | Encrypt national id and account numbers | BLOCKS-M0 | PS-14 (PLAN.md E9): field encryption and blind index from the first migration. Per-tenant keys in M1. |
| D10 | Audit log | BLOCKS-M0† | PS-15. |
| D11 | Retention and deletion | LATER | 5-year retention. Nothing is deleted before 2032. |
| M01 | Who owns Digdir/Skatteetaten onboarding | BLOCKS-M1 | Start now (Q19, PS-23). |
| M02 | Which company is the vendor | BLOCKS-M1 | Start now (Q19). |
| M03 | Maskinporten key type | BLOCKS-M1† | PS-23. |
| M04 | Own Maskinporten client in Rust | BLOCKS-M1† | PS-23. |
| M05 | Which system-user type first | BLOCKS-M1 | PS-23: standard system user in M1; agent (client-system) system user in M2. |
| M06 | How to fetch the A07 report | BLOCKS-M1 | PS-24: on demand, not nightly. |
| M07 | Test environment and test data | BLOCKS-M1 | PS-24. |
| M08 | Logging calls to authorities | BLOCKS-M1† | PS-15. |
| M09 | How the byrå links clients | LATER (M2) | PS-23, Q27: Altinn portal. |
| M10 | When and how often to fetch A07; quota | BLOCKS-M1 | PS-24. |
| M11 | What to test in TT02 for the byrå flow | LATER (M2) | Q27: TT02 and production for at least 3 clients (gate M2). |
| M12 | Logging who in the byrå did what | LATER (M2)† | PS-15. |
| M13 | Byråer with their own payroll; local branches | LATER | The model allows several system users per customer. Local branches are moot. |
| K01 | Controls as code or configuration | BLOCKS-M0† | PS-21. |
| K02 | What a deviation contains | BLOCKS-M1† | PS-21. |
| K03 | Tolerances and rounding | BLOCKS-M0 | PS-08, Q7. |
| K04 | When controls run | LATER | PS-21. |
| K05 | Who may mark a deviation as explained | BLOCKS-M1† | PS-21. |
| R01 | Which ledgers first | BLOCKS-M1 | Q26, PS-18. |
| R02 | Accounts per customer | BLOCKS-M0 | Q9, PS-18. |
| R03 | Storing ledger tokens | BLOCKS-M1† | PS-18. |
| G01 | How flexible the approval flow is | LATER | A fixed template in M0/M1 (B39 downgraded). |
| G02 | What decides who approves a step | LATER | |
| G03 | Sequential or parallel steps | LATER | |
| G04 | Segregation of duties | BLOCKS-M1 | PS-20, Q16. |
| G05 | Delegation and substitutes | LATER | |
| G06 | What happens on change after approval | BLOCKS-M0 | PS-20: hash, and a change voids the approval. |
| G07 | One approval engine for all areas | LATER | Payroll runs only. |
| B01 | Which open-banking providers | LATER | B40. |
| B02 | Bulk salary from a corporate account | LATER | |
| B03 | Who signs payments, and how | MOOT | Answered (B12). |
| B04 | Can the accountant start and sign | LATER | |
| B05 | KID and a separate withholding payment | BLOCKS-M0 | PS-17: forskuddstrekk as its own non-SALA payment order, with the KID from the a-melding feedback in M0. |
| B06 | Status back from the bank | LATER | Manual "paid" confirmation. |
| B07 | Hiding salaries in the bank | BLOCKS-M0† | PS-17: SALA. |
| B08 | Bank file as fallback | MOOT | pain.001 is the primary channel. |
| B09 | Licence and liability for payment initiation | LATER | |
| U01 | Frontend framework | BLOCKS-M1† | PS-04: no web UI in M0; minimal TypeScript + React admin UI in M1. |
| U02 | Components and design system | LATER | |
| U03 | Charting library | MOOT | No graphs in M0/M1. |
| U04 | WCAG requirements | LATER | Use accessible components. Formal requirement comes with the employee portal. |
| I01 | Login in phase 1 | BLOCKS-M0 | PS-22. |
| I02 | Roles in phase 1 | BLOCKS-M0 | PS-22. |
| I03 | Sessions | BLOCKS-M0† | PS-04, PS-22: managed OIDC login with a CLI device flow and personal tokens in M0; session cookies with the M1 web UI. |
| I04 | Where access is checked | BLOCKS-M0† | PS-06. |
| H01 | Cloud and region | BLOCKS-M0 | PS-05, Q14. |
| H02 | Runtime | BLOCKS-M0† | PS-05. |
| H03 | Infrastructure as code | BLOCKS-M1† | PS-05. |
| H04 | Environments | BLOCKS-M0† | PS-05. |
| H05 | Logging and monitoring | BLOCKS-M0† | PS-14. |
| H06 | Backup and restore | BLOCKS-M0† | PS-05. |
| H07 | Dependency security | BLOCKS-M0† | PS-03. |
| H08 | Pentest and DPA before the first customer | BLOCKS-M1 | Q22. Threat model now. |
| X01 | Assistant uses the same API | LATER | |
| X02 | Which data the language model sees | MOOT | No LLM features before M1. |
| X03 | Model provider and region | LATER | |
| X04 | First assistant tasks | LATER | |
| X05 | Assistant boundaries | MOOT | Already decided in B13. Enforced in the access model when built. |
| L01 | How to compute withholding | BLOCKS-M0 | PS-09, Q6. |
| L02 | Engine as a pure function | BLOCKS-M0† | PS-10. |
| L03 | Same employee model in phase 1 and 2 | MOOT | There is one model, built for payroll. |

### 3.4 Night work (`natt/`)

**N-items (forslag.md; proposals plus questions), and backlog N22**

| N | Topic | Tier | What survives / note |
|---|---|---|---|
| N01 | Garnishment, child support and other deductions | LATER | M1: a manual trekk register (D-Trekkpalegg with `innhentet_fra`). Agree to move F-BYR-15/F-MYN-28. Dialogporten letter sensor later. Q1 (`lonn` package) → yes, in Q25. |
| N02 | Accounting for the payroll run | BLOCKS-M0 | Aggregate per account and dimension, net pay on 2930, short run reference (PS-18). Draft-voucher posting at M1. |
| N03 | The A07 report | BLOCKS-M1 | On-demand fetch as answer key for migration and parallel runs. Hand-written types for the subset needed, raw data encrypted (PS-24). |
| N04 | Reading from ledgers | MOOT | Read-only ledger reconciliation. Cut from M1. |
| N05 | Employee overview from the a-ordning | MOOT | Brutto is master. A07 import only for migration. |
| N06 | Becoming a vendor with Digdir/Skatteetaten/Altinn | BLOCKS-M1 | Start now (Q19, PS-23). Direct customers grant `a-ordning` + `lonn`. |
| N07 | Control catalogue for byrå and auditor reconciliation | LATER | A later add-on product with A07-vs-ledger (B46). The AGA bridge per zone goes with it. |
| N08 | Rust ecosystem | BLOCKS-M0 | Decimal policy and PDF tooling (PS-08, PS-19). JWS, job queue and OpenAPI client generation at M1. |
| N09 | Open banking | LATER | B40. |
| N10 | Approval flow | BLOCKS-M0 | Only the simple version: one step, hash, per-output status (PS-20). Byrå interviews fold into Q20. Configurable flows later. |
| N11 | Competitors' A07 reconciliation | MOOT | Market research for the read-only tool. Keep as input for a later add-on. |
| N12 | Assistant, Claude in the EU, cloud and KMS | BLOCKS-M0 | Cloud and key-vault part only (Q14, PS-05). AI and data-class parts later or moot. |
| N13 | Trekkrutine, rounding, tax liability | BLOCKS-M0 | Q6, Q7, PS-08, PS-09. Approve the table-file download. Sjur's questions (group life, halvt trekk with supplements) are M1, before December. |
| N14 | a-melding 2.4 and notices | BLOCKS-M0 | Aggregate design only (Q17, PS-16). The 2.4 serializer: spec by 1.5.2027, mapping by 1.7.2027, in test by 1.12.2027. The fine (tvangsmulkt) sensor later. |
| N15 | NAV refund and K27 | BLOCKS-M1 | Refund receivable entered by hand, one AGA method and a list of sick cases near the 3-month deadline (Q23). K27 import and API, matching and the full refund ledger later. |
| N16 | Pension providers and OTP | BLOCKS-M1 | OTP fields in the a-melding and premium input (M0 if the M0 employer has OTP). Provider files later. |
| N17 | Salary payment in the bank | BLOCKS-M0 | pain.001 with net pay as SALA and forskuddstrekk as a separate payment with KID (PS-17). Deductions to creditors at M1. ZTL later. |
| N18 | Huma API | LATER | |
| N19 | Privacy, DPIA, DPA | BLOCKS-M1 | Q22. In M0, only "no payroll data in telemetry" (PS-14). |
| N20 | Tariff data and the AGA zone table | LATER | Zone is set manually per virksomhet in M0/M1. Split-municipality lookup and tariffs are cut until asked for. |
| N21 | ReAi and Vinderen (test tenant) | LATER | Relevant only if ReAi becomes the M0 employer's ledger or the M1 adapter. |
| N22 | TT02 test of A07 (deferred) | BLOCKS-M1 | Once the Maskinporten client exists (PS-24). |
| N23 | A07 mapping as a data file | LATER | Ledger reconciliation. The pay-type → a-melding code part feeds Q5 now. |
| N24 | Kontrolloppstilling (year-end payroll reconciliation statement) | LATER | Year-end 2027 at the earliest. |
| N25 | Access in the MVP (Krav og betalinger, "Brutto submits for others") | MOOT | Strike "Brutto submits for others" (agree). Krav og betalinger later. |
| N26 | Trekkpålegg API without submitting | MOOT | The premise (no submission) is gone. The API comes later. |
| N27 | Dialogporten in phase 1 | LATER | M1 polls feedback through the a-melding API. |
| N28 | Coordinated garnishment in detail | LATER | |
| N29 | Liability for wrong deductions | LATER | The contract clause folds into Q22. |
| N30 | Documentation model for payroll | BLOCKS-M0 | Aggregated voucher plus an archived, hashed payroll journal (PS-18). The legal questions come later. |
| N31 | Expenses via integration | LATER | |
| N32 | How integrated payroll modules post in practice | MOOT | Ledger reconciliation. Later. |
| N33 | Vouchers to other ledgers | LATER | One adapter in M1. A run reference of ≤20 characters already in M0. |
| N34 | Funder requirements | MOOT | Cut. |
| N35 | Arbeidsforhold-ID in Tripletex and ReAi | BLOCKS-M1 | Migration keeps the ids (Q28). The id format for Brutto's own ids is M0 (PS-13). |
| N36 | Control catalogue ANS-01–19 | LATER | Reuse a few a-melding rules in the M0 pre-checks. Sjur's questions are organisation life, later. |
| N37 | Employee APIs in other systems | MOOT | Migration uses the Excel template. |
| N38 | Name-list import and privacy for A07 | MOOT | Names come from Brutto. § 7-31 note questions later. |
| N39 | Test data for A07 in TT02 and Tenor | BLOCKS-M1 | Email the Altinn servicedesk now. Brutto's own serializer is the "generator". |
| N40 | Terms and access in edge cases | BLOCKS-M1 | Written OK from the one ledger vendor before building its adapter (Q26). The dashboard and aggregation concerns are moot. |

**morgen.md – decisions for Sjur (MS) and questions for Peter and Sander (MP)**

| Id | Item | Tier | Note |
|---|---|---|---|
| MS1 | Choose the vendor company and technical owner | BLOCKS-M1 | Q19. Start this week. |
| MS2 | One combined legal review | BLOCKS-M1 | Narrow it to Q22. Huma, ZTL and "approve and sign" later. |
| MS3 | Approve sending the inquiries | BLOCKS-M1 | Send now: Skatteetaten (Q24), Altinn servicedesk (TT02 orgnr), own bank (Q12), and the one ledger vendor (Q26). Later: ZTL, NAV, Huma, Finans Norge, Brreg, Utleggsappen, ReAi. |
| MS4 | OTP account (5420 vs 5950) and 5390 → 5300 | BLOCKS-M0 | Part of the standard posting (Q9, PLAN.md D9): settle the OTP account (S #29) and the grouping of 5390 (S #28 says 5000, assumed). Brutto does not post the premium itself. Grouping codes matter only for ledger reconciliation (later). |
| MS5 | Approve the downloads (table file, Visma PDF) | BLOCKS-M0 | Approve the table file (Q6). The Visma PDF is moot. |
| MS6 | ReAi voucher test in tenant 2915 | MOOT | Only if ReAi is the M0 employer's ledger. |
| MS7 | Payroll-domain questions (descriptions after end date, support contacts, FTE in notes, deputy board members, withholding paid from voucher) | BLOCKS-M1 | Only "which descriptions may follow an end date" (termination settlement, Q24). The rest later. |
| MS8 | Interview 2–3 byråer and 2–3 auditors | BLOCKS-M1 | Fold into pilot recruitment (Q20). |
| MP1 | Azure Norway East, Key Vault, Postgres 18; own JWS | BLOCKS-M0 | Q14, PS-05. JWS at M1. |
| MP2 | Money in Rust, no `round()`, f64 isolated | BLOCKS-M0 | PS-08, PS-09 (PLAN.md E5): `f64` only inside the isolated withholding crate. |
| MP3 | Job queue for 500 clients per night | MOOT | Not in scope. A simple Postgres queue in M1. |
| MP4 | Three data layers with a source per field | MOOT | That was for multi-source reconciliation. Cut. |
| MP5 | Balance engine with reversal pairs | MOOT | Ledger reconciliation. |
| MP6 | Approval engine with hash and three tracks | BLOCKS-M0 | Simple version (PS-20). |
| MP7 | Dialogporten sensor; shared accounting/employee-source trait | LATER | |
| MP8 | MVP launch date; 2.4; who runs N22 | BLOCKS-M1 | M0 shadow run Nov–Dec 2026; Brutto files from 2027-02 (planning date) or 2027-01 (stretch) (B44). Pilots live 1.8.2028 (plan); 2028-01 is a stretch that needs two developers signed by 18.12.2026 (D12, gate HIRE). 2.4 mapped by 1.7.2027 and in test by 1.12.2027. N22 run by the Maskinporten owner. |

**morgen.md – recommended mapping changes (pending proposals)**

| Proposal | Tier | Note |
|---|---|---|
| F-REG-30/02/03: account rules with balance type | LATER | Ledger reconciliation (B46). The AGA bridge per zone goes with it. |
| F-REG-29: SAF-T as the first source | MOOT | Read-only tool. |
| F-BYR-15/F-MYN-28: trekkpålegg to MVP, manual register | BLOCKS-M1 | Accept: a manual register in M1. |
| F-MYN-02: direct customers grant `a-ordning` + `lonn` | BLOCKS-M1 | Accept (Q25). |
| F-PER-24: validate the occupation code against the published list | BLOCKS-M0 | The occupation code is mandatory in the a-melding. Validate against the list Skatteetaten publishes for the a-melding. |
| F-TRK-12: halvt trekk covers supplements paid with salary | BLOCKS-M1 | Before the first December. |
| F-REG-15: refund receivable on 1579 | LATER | LATER in `scope.csv`. M1 enters the NAV refund receivable by hand (PLAN.md §6.2), and the account is settled before M1 (Q9). |
| F-PEN-06/GC-17: AGA on premium follows the payment month | BLOCKS-M0 | Accept (Q8). |
| F-LON-19: the state A-table is gone from 2024 | LATER | Data correction. Accept. |
| F-UTL-18: only pure refunds outside payroll; tax-free km and diet go in the a-melding | BLOCKS-M1 | A legal correction. Accept if mileage or diet is a pilot pay type. |
| New functions: kontrolloppstilling, Dialogporten sensor, vendor agreements, name list via link, data class per field, audit-trail description, F-TRK-29 diligence log | LATER | The name list via link is cut. |
| New function: synthetic a-melding generator | BLOCKS-M1 | Brutto's serializer plus Tenor test persons. |
| New entities: D-Regnskapssaldo, D-Hovedbokslinje, D-Feltkilde, D-Feltkonflikt | MOOT | Read-only and multi-source tool. Cut. |
| New entities: D-Arbeidsforholdkobling | BLOCKS-M1 | Migration id mapping. |
| New entities: D-Banksignering, D-Banksamtykke, D-Partnerkunde, D-Skattekrav, D-Skatteinnbetaling, D-NavRapport, D-Trekkperiode, D-Rolleinnehaver, D-Tariffpakke, D-Kontrolloppsett | LATER | |
| New entity: D-Sonedel (split-municipality zones) | LATER | Zone set manually. |
| Voucher contract: reference ≤20 characters; net, VAT and gross per line; look up before write; no "Lønnsbilag" type in Tripletex | BLOCKS-M1 | The ≤20-character reference already in M0. |
| Retention: locked report 5 years, raw A07 13 months, project data 10 years | LATER | Nothing is deleted before 2032. |

---

## 4. Decisions B1–B46 under the new direction

"Keep" means unchanged. "Reword" gives the new wording in short form. "Downgrade" means it moves to after M1. "Drop" means it is superseded. "Narrow", "Activate now", "Tighten" and "Re-date" follow PLAN.md §8, which wins where this table differs. "New" marks decisions added by PLAN.md.

| B | Title | Status now | Recommendation | Reason / new wording |
|---|---|---|---|---|
| B1 | Standalone payroll for 10–1000 employees and byråer | Decided | Keep, reword | Long-term target. Path: M0 own company → M1 3–5 direct customers (20–150 employees; a byrå's own payroll can be one) → M2 byråer with their clients (B45) → 150–300 → 300–1000. |
| B2 | Open integrations on equal terms | Decided | Keep, reword | Keep the principle and phase the mechanisms. M0/M1: one public API used by our own `brutto` CLI (M0) and admin UI (M1), plus CSV import. Developer portal, webhooks, source registry and partner contracts later. |
| B3 | Segment order | Proposal | Keep, reword (adopt as decided) | Adopt the critic's cohort as the M1 profile, with explicit exclusions: tariffs/KLP/shift rosters, ambulatory AGA, posted workers, seafarers, Svalbard, net-salary agreements, groups sharing fribeløp, local branches, lost-earnings cases. |
| B4 | Software only, no payroll service | Proposal | Keep | Needed for pilot contracts. Lawyer review before M1 (Q22). |
| B5 | Pure engine and Sjur's pay-type model | Partly decided | Keep, reword | Approve the minimal extension now (Q4). Expression language cut; retro later. |
| B6 | History and immutable runs | Proposal | Keep, reword | Limit to data that affects calculation: append-only valid-from/recorded-at versions, an immutable input snapshot per approved run, corrections as new runs, no general bitemporal query layer (PS-12). |
| B7 | Customer owns data; shared DB with RLS | Proposal | Keep, reword | tenant_id from M0, RLS before the first external tenant, byrå access grants in M2. Cells cut until a customer over 300 employees. |
| B8 | Rust, modular monolith, Postgres | Partly decided | Keep (mark decided) | Rust is decided. The rest is settled by PS-04/PS-05. Remove the Kotlin/JVM discussion. |
| B9 | Data and backup in Norway | Proposal | Keep | The simplest lawful option: no § 7-5 notice for customers. M0 single region in Norway; geo-separated Norwegian backup before M1. |
| B10 | Authorities via Maskinporten and system user | Partly decided | Keep, reword | M0 uses manual upload and tax cards from Skatteetaten's tax-card file service (RF-1211, Altinn package "Lønn") or copied from the current system. M1 standard system user with `a-ordning` + `lonn`; agent (client-system) system user for byråer in M2. Special-category package later. Change "trekkrutine is the answer key" to "the published table file is the answer key" (our own port must match it 100 %). |
| B11 | a-melding as its own aggregate; 2.4 from 2028 | Proposal | Keep, reword | One format-neutral aggregate per opplysningspliktig and month, replaced on change. Serialised to the JSON the API takes: uploaded manually in M0, sent via the API in M1. JSON for 2027 manual uploads per Skatteetaten's Q&A of 18.06.2026 [verify by 27.11], with a costed XML 2.3 fallback (+1–2 weeks). 2.4 mapped by 1.7.2027, in test by 1.12.2027. |
| B12 | Brutto never moves money | Decided | Keep | pain.001 through M1. |
| B13 | AI prepares, explains and flags | Partly decided | Downgrade | No AI features in M0/M1. Keep the boundaries as policy for when they come. |
| B14 | BankID, passkeys, SSO, account-number shield | Proposal | Keep, reword | M0: managed OIDC login (e.g. Entra ID) with MFA and a CLI device flow, re-authentication through the identity provider; no BankID. M1: BankID via broker for customer users and approvers, with step-up on approval; account change with four-eyes and a notice. SSO/SCIM, quarantine and the employee BankID portal later. |
| B15 | ISAE 3402 and ISO 27001 | Proposal | Downgrade | After about 6 months with external customers. M1: DPA, pentest, a light information-security management system, and controls that produce evidence (golden cases, release diff). |
| B16 | Migration with authority data as answer key, parallel run | Proposal | Keep, reword | M0: two shadow months to the øre, Brutto system of record from period 2027-02 (planning date) or 2027-01 (stretch) (B44). M1: Excel-template year-to-date import checked against A07, method 1, prefer 1 January starts. Adapters for other systems cut until there is volume. |
| B17 | Pricing | Proposal | Downgrade | Flat pilot fee in M1. Metering and price unit later. |
| B18 | Recipients without ordinary employment | Partly decided | Downgrade | Organisation-life epic after M1. Board fees and simple fees (recipient classes board/office and fee) are in M1 only if a signed pilot needs them (pilot-pulled at G4, fifth in the M1 cut order). |
| B19 | Own payroll in November 2026 | Decided | Reword | PLAN.md §8: "Brutto runs the team's own payroll. November and December 2026 are shadow runs, compared to the øre with the current system, which keeps submitting income year 2026. Brutto is system of record from period 2027-01 if both shadows are clean by 15.1.2027, otherwise 2027-02 or 2027-03. Manual upload until Maskinporten is live." Drop "the whole system finished in November". 2027-02 is the planning date; 2027-01 is the stretch. |
| B20 | Own modules for vacation/absence and time | Decided | Downgrade | Modules after M1. M1 keeps the legal core in payroll (AGP, sick pay, leave codes, holiday pay); hours via CSV. |
| B21 | Integrate Huma now, replace later | Decided | Downgrade | Huma connector only when a signed pilot needs it. The replacement goal stays internal. |
| B22 | Scope rule | Proposal | Activate now | M0 frozen 13.11.2026, M1 lawful core frozen 1.2.2027 (G3), pilot-pulled items frozen at G4 (31.3.2027). One in, one out, measured in developer-weeks; Sjur signs. Regulatory changes are exempt but come out of a 15 % reserve. |
| B23 | Capital and runway | Proposal | Reword | Fund the actual plan (current team, plus 2 developers and a payroll specialist from Q2 2027) through at least 6 months after pilot go-live. Recompute runway at actual burn and write it into the G2 ADR; D12 needs a runway figure before 6.11 (Q30). |
| B24 | Calculation guarantee with cap | Proposal | Downgrade | M1 pilots get a simple capped commitment in the agreement ("we cover documented interest and fees up to the cap"). Full guarantee and insurance later. |
| B25 | Cohort limit | Proposal | Tighten | Wave 1 is at most 5 direct customers and about 600 recipients. Firm clients in M2. "12 customers / 1,500 payees" applies to a later cohort. |
| B26 | Gates with dates, go/no-go | Proposal | Re-date | Use the gates in PLAN.md §3: G0 6.11.2026; G1 (M0 freeze) 13.11.2026; M0-α engine spike 27.11.2026; M0-S1 shadow #1 18.12.2026 (latest 31.12.2026); M0-S2 shadow #2 and the go/no-go for 2027-01 15.1.2027 (M0 live 2027-01 stretch, 2027-02 plan, 2027-03 latest); HIRE two developers signed 18.12.2026; G2 calibration 29.1.2027; G3 (M1 lawful core frozen) 1.2.2027; MP Maskinporten live 31.3.2027 (best case 29.1.2027); G4 pilot letters of intent and pilot-pulled items 31.3.2027; JUN27 14.5.2027; 24-S mapping 1.7.2027; M1-FC 31.3.2028 (plan) / 1.9.2027 (stretch); 24-T 1.12.2027; DEC27 15.11.2027 with the 2028 rule pack by 22.12.2027; AS27 14.1.2028; P-PAR two periods before go-live; P-L pilots live 1.8.2028 (plan) / period 2028-01 (stretch); JUN28 2.5.2028 (stretch only); M2 1.8.2028 if the pilots go live 2028-01, otherwise about 8.2029. |
| B27 | Buy everything around the engine | Proposal | Keep | BankID broker, PDF, hosting, pentest, Digipost, external payroll-expert hours (from November 2026, D4). Build the engine (including our own withholding port, checked against the published table file), the a-melding aggregate and the explanation trace ourselves. |
| B28 | Payroll-domain veto | Proposal | Keep | Sjur now; the external payroll expert, contracted from November 2026, is the deputy (D4, Q21). |
| B29 | Integration before a new module | Proposal | Keep | Supports the narrow scope. It also governs the module user interfaces in B20. |
| B30 | External positioning | Proposal | Keep | Costs nothing and protects the API dependencies. |
| B31 | Map before building | Decided | Drop | Superseded by B37 and by PLAN.md. Building starts. |
| B32 | Expenses only via integrations | Decided | Keep, reword | No integration in M1. Mileage and per-diem are entered as pre-split pay lines or CSV with the state-rate split, only if a signed pilot needs them (pilot-pulled). Travel-rate calculation and the Utleggsappen integration later. |
| B33 | K27 and NAV refund in the core | Partly decided | Keep, reword | M1: AGP tracking, sick-pay lines, the refund receivable entered by hand, a list of sick cases near the 3-month deadline, inntektsmelding in NAV's portal, and one AGA method, "deduct when received" (Q23). K27 import and API, matching and the full refund ledger later. |
| B34 | Payroll first, HR later | Decided | Keep, reword | Stop further mapping of HR, UTV, HEL and KOM. "Employee portal for payroll" is reduced to payslip delivery through Digipost in M1; the portal and employee login come later. |
| B35 | Departments, projects, dimensions | Partly decided | Keep, reword | M0: one department, no dimensions. M1: a flat department and project on the employment, carried to voucher lines. Percentage splits and hierarchy later. |
| B36 | Sally is a separate product | Decided | Keep | |
| B37 | Straight to MVP, phase 1 merged | Decided | Reword | Brutto calculates payroll from the first release (kept), in the M0/M1 tiers. A07 stays only as the answer key for migration and parallel runs. Graphs and broad controls are LATER, and A07-vs-ledger is a separate product line (B46). |
| B38 | Team of three | Decided | Keep | |
| B39 | Approval flow configured per customer | Decided | Downgrade | M0/M1: a fixed flow (preparer → approver, optional second approver) with a hash lock. Configurable flows later. |
| B40 | Payout via an open-banking provider | Partly decided | Downgrade | pain.001 and manual "paid" confirmation through M1. |
| B41 | API-first; everything via MCP | Partly decided | Narrow | PLAN.md §8: the API is the application layer (one operation catalogue, one `dispatch`), and the UI and MCP are thin clients; OpenAPI is generated from code. M0: `brutto` CLI over REST, no MCP. M1: MCP with read tools, draft tools and two generic tools; actions with legal effect (approve, submit, pay, bank account, roles) are human-only, and the human approval hash-locks the a-melding. Agent-started actions and agent submission come after the DPIA (and an MCP addendum to the DPA); OAuth server, webhooks and developer portal later. CI parity test cut (PS-25). |
| B42 | MVP at Matrix level | Partly decided | Drop | Replaced by M0 and M1 in PLAN.md. About 305 functions is far beyond M1. Matrix Lønn stays a long-term reference for breadth. |
| B43 | Tracks after approval | Proposal | Keep, reword | M0: a simple status per output (payslip, payment file, voucher, a-melding). M1: withholding per payout date and AGA per term. Bank-status integration later. |
| B44 | Sender of record for income year 2026 | New (PLAN.md D1) | Add | The current system submits all of income year 2026. Brutto shadow-runs November and December 2026, compared to the øre, and is system of record from period 2027-01 if both shadows are clean by 15.1.2027, otherwise 2027-02 (planning date) or 2027-03. No 2026 year-to-date import and no 2026 sammenstillingsoppgave from Brutto (Q1). |
| B45 | Accounting firms are M2 | New (PLAN.md) | Add | PLAN.md §8: a firm's own payroll can be an M1 pilot; firm clients wait for M2 (1.8.2028 if the pilots go live 2028-01, otherwise about 8.2029), together with the agent system user and client linking (Q27). **Consequence:** no firm-client revenue before 2029 in the base case. **Option to cost:** a firm runs a client as a direct-customer tenant in M1; the client approves a standard system user, and the firm's staff are users in that tenant. |
| B46 | A07-vs-ledger is a separate product line | New (PLAN.md) | Add | LATER, and only with written API clearance from the accounting vendors. A07 in M1 is the answer key for migration and parallel runs only. |
