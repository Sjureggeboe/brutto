# Scope review: BYR, POR, LED, ORL, KOM, HR, UTV, HEL

> Working paper from the scope review of 29.10.2026. PLAN.md is the main plan and `docs/plan/scope.csv` holds the final tier per function; where this paper disagrees, they win.

Reviewer: area agent (accounting firms, employee portal, manager approvals, organisational life, notifications, HR extension).
Source: `analyse/build/data/omr-K1/K5/K7.json`, `design.json` (B12, B18, B19, B34, B37, B39, B41–B43), `fase1.json` (P02, D04, G01–G07, M09–M13, J05), `research/R0-matrix-lonn-omrader.md`, `research/R3-kritikk-strategi.md`.
Detail per function: `docs/plan/scope.csv` (157 rows in these eight areas, one per function).

## 1. Tier counts

| Area | Functions | Marked MVP today | M0 | M1 | M2 | LATER | CUT |
|---|---|---|---|---|---|---|---|
| BYR Accounting firms | 36 | 18 | 0 | 0 | 10 | 18 | 8 |
| POR Employee portal/app | 29 | 4 | 1 | 3 | 0 | 20 | 5 |
| LED Manager and approval | 19 | 2 | 0 | 2 | 0 | 15 | 2 |
| ORL Organisational life | 33 | 2 | 0 | 2 | 0 | 26 | 5 |
| KOM Notifications/start page | 9 | 4 | 0 | 3 | 0 | 3 | 3 |
| HR | 8 | 1 | 1 | 0 | 0 | 5 | 2 |
| UTV Competence | 11 | 0 | 0 | 0 | 0 | 4 | 7 |
| HEL Health follow-up | 12 | 0 | 0 | 0 | 0 | 10 | 2 |
| **Total** | **157** | **31** | **2** | **10** | **10** | **101** | **34** |

- 31 functions are marked MVP today. 11 end in M0/M1. 10 move to M2, accounting firms: the byrå-lite slice in section 3 (F-BYR-01, -02, -03, -10, -12, -19, -26, -27) plus F-BYR-07 (agent system user) and F-BYR-08 (client linking and diagnostics). 10 MVP-marked functions move to LATER: F-BYR-04, -14, -15, -17, -18, -30, -32, -33, F-POR-27 and F-KOM-06.
- One "After MVP" function is needed for M1, in simplified form: F-POR-04 (Digipost print or manual delivery for staff without a digital mailbox). This review also pulled in F-POR-01 (BankID login for employees) and F-POR-28 (leavers keep access); Plan v1 moves both to LATER.
- **Plan v1 decision after review (29.10.2026): payslips and the annual statement go through Digipost** (bought, F-POR-12, M1), with Digipost print and manual delivery as fallback (F-POR-04). The employee login, the "My payslips" page and payroll notifications to employees (F-POR-01, -27, -28) are LATER. F-BYR-07/-08 are M2 with the rest of the firm features (B45). This paper's BankID-page proposal below is kept as the reasoning and as the fallback if Digipost is cut (sixth in the M1 cut order, PLAN §6.3: then manual secure delivery).
- All M0/M1/M2 rows in these eight areas carry a simplification. None is built as specified.
- Entities: these areas own 51 entities with 844 fields. M0/M1 needs 4 of them with about 38 fields; M2 adds 2 more (D-Byra, D-Klient) with about 16, so about 54 fields instead of 138 in all. The rest is either folded in as a few fields on entities owned by other areas, or not needed (section 6).

## 2. Narrative per area

**M0 (own payroll: shadow runs November and December 2026, live from period 2027-01 as a stretch, 2027-02 as the planning date).** Only two functions come from these areas:
- F-POR-08: the payslip PDF/A is generated per payment.
- F-HR-01: the PDF goes into an immutable archive with SHA-256 and a retention of 5 years after year-end, alongside the a-melding upload file and the voucher file.

During the shadow runs the current system's payslip and a-melding are the legal ones (B44). So M0 needs no delivery channel, no notifications and no portal. From the first live period, when Brutto is system of record, the team (3 people) gets its PDFs by hand until M1 delivery through Digipost exists. That is lawful. There is no byrå, manager or org-life content in M0. F-ORL-15 (M1) is needed earlier only if the M0 employer pays board fees after go-live.

**POR.** (**Plan v1 decision:** M1 buys delivery through Digipost (F-POR-12) instead of the page below; the login, notifications and leaver access are LATER. The analysis is kept as the reasoning.) This review found the cheapest lawful M1 delivery to be a read-only "My payslips" web page:
- The employee logs in with BankID through the same broker that payroll approval needs anyway (B41).
- The login is matched to the employee's own records by a fødselsnummer (national ID) hash, so no invitations, passkeys or app are needed.
- An e-mail without amounts says "payslip available" (F-POR-27).
- Staff without BankID get the PDF from payroll by hand (F-POR-04).
- Leavers keep access while the data is retained (F-POR-28). This is how the final-settlement slip reaches people who have already left.
- The annual sammenstillingsoppgave (annual statement to each recipient) is one PDF per year, published the same way (F-POR-16).
- Everything else waits for the app and the modules: explained payslip, Digipost, self-service account change and profile, absence/time/expense tabs, WCAG audit and languages.

Comparison of channels:
- *Plain PDF by e-mail:* rejected. Payslips show union dues and sick pay, which are GDPR art. 9 data, so this is an art. 32 risk.
- *Digipost:* lawful and convenient. It adds a Posten contract, a per-letter cost and another integration, and staff who are not Digipost users still need a fallback. This review rated it LATER; **Plan v1 chooses it for M1** (F-POR-12, bought, B27), with Digipost print and manual delivery as the fallback (F-POR-04), because it removes the employee portal and its login from M1.
- *BankID page:* the cheapest to build, because BankID is already in M1 for approvals. Under Plan v1 it is LATER (F-POR-01, -27, -28).

**LED.** Customer-configurable approval flows (B39), the manager inbox, deputies, escalation, team calendar and manager visibility profiles are all LATER. In M1, approval happens upstream in the source systems, and facts arrive approved via CSV (as R0 already says). The Huma and Utleggsappen integrations are LATER. M1 keeps two things:
- F-LED-04 segregation of duties, limited to the payroll run and the first payment to a new bank account.
- F-LED-13 role end dates and automatic revocation.

F-LED-04 must be built **once**, in F-SIK-12/F-KJO-23. Today the same rule appears in F-LED-04, F-BYR-19, F-KJO-23, F-SIK-12 and F-BET-19.

**Minimum approval in M1:**
1. One approval step on the payroll run, with BankID step-up and hash lock (B41). A recalculation invalidates the approval.
2. The preparer cannot approve the run.
3. Whoever registered or verified a new bank account cannot approve the first payment to it. Account changes are made by payroll with four eyes.
4. A customer with only one payroll person gets a logged exception, plus a post-run report to the daglig leder (managing director) or styreleder (board chair).

A second approval step (G01–G03) and per-customer templates are LATER.

**ORL.** M1 needs the minimum for board fees and fees, which are common in AS (employee board members are mandatory on request when there are more than 30 employees, aksjeloven § 6-4) and in organisations:
- F-ORL-01, reduced to three recipient classes stored as an enum on the employment relation: EMPLOYEE, BOARD/OFFICE (verv) and FEE (honorar).
- F-ORL-15: manual board-fee lines with arbeidsforholdstype `frilanserOppdragstakerHonorarPersonerMm`, lønnsbeskrivelse (income description) `styrehonorarOgGodtgjoerelseVerv`, percentage withholding (50 % without a tax card), AGA (employer's NI contribution) and no holiday pay or OTP (occupational pension).

Under Plan v1 both are pilot-pulled: in M1 only if a signed pilot needs them (chosen at G4, PLAN §6.1), and fifth in the M1 cut order (§6.3). Everything else in ORL waits for the organisation segment and the OrgLab/Tikket integrations: the wizard, engagements, invitations, decisions, the 10,000 rule, the § 23-2 exemption, lost earnings, events, artist tax and shifts. Choose pilots so that the 10,000 rule, the AGA exemption and foreign artists do not occur in M1. Otherwise handle them by hand (see risks).

**KOM.** M1 keeps three things:
- F-KOM-01: e-mail plus an in-app list, with neutral content.
- F-KOM-02: about seven hard-coded payroll events.
- F-KOM-03: a "needs action" list derived from state. This is the Matrix pattern where the state creates the task, so no task table and no workflow engine are needed.

The start page (F-KOM-06) becomes that list plus the run tracks (B43). The workflow engine, announcements, carousel and messages are LATER or CUT.

**HR / UTV / HEL.** These are confirmed LATER or CUT as an HR extension (B34). HR-01 is the exception, kept as the payroll document archive. Leaving HEL out is lawful: the employer's sick-leave follow-up duty (aml. § 4-6) can be met in NAV's "Dine sykmeldte" or Huma. Masking of sick-pay and union-dues pay types is a SIK concern and is needed in M1 there. Following the area's own question (K7 #6), the HR extension would build appraisals and certificates with expiry first. Competence search, job profiles, gap analysis, courses, goals, salary-review input and talent planning are CUT.

**BYR.** See section 4.

## 3. The byrå slice ("byrå-lite", 8 functions), now M2

This review first proposed these 8 functions as an optional M1 slice. PLAN (B45) and `scope.csv` put them in **M2**, together with F-BYR-07 (agent system user) and F-BYR-08 (client linking and diagnostics), so `scope.csv` has 10 BYR rows in M2. In M1, a firm's own payroll can be a pilot as a direct customer; firm clients wait for M2.

| Id | Simplest version (M2) |
|---|---|
| F-BYR-01 | One flat firm entity linked to client tenants. No chain, office or team levels. |
| F-BYR-02 | Client created from orgnr via Brreg. Fields: oppdragsansvarlig (responsible accountant), who approves pay, and a reference to the engagement-letter document. |
| F-BYR-03 | Three roles per client with an end date and personal BankID login (regnskapsførerloven § 4-2, GRFS 8.1). |
| F-BYR-10 | Per-person logging of submissions. Comes for free from the generic audit log. |
| F-BYR-12 | Client list with status per client and month: run tracks and next deadline. |
| F-BYR-19 | Four eyes through the shared segregation-of-duties rule, signed with name and date. |
| F-BYR-26 | Recorded customer approval: original e-mail plus SHA-256 bound to the run hash (GRFS 8.6). |
| F-BYR-27 | Default "customer pays": pain.001 download is logged, and count/sum/hash are shown. |

This review proposed that byrå-lite use each client's **standard system user**, approved by the client in Altinn, or the manual upload (F-MYN-14), and not the agent system user (`regnskapsforer-lonn`). PLAN §9 puts the agent system user with `regnskapsforer-lonn` and client linking in the Altinn portal (F-MYN-04/05, F-BYR-07/08) in M2, with a standard system user per client as the fallback.

## 4. Recommendation: byrå in M1 or a separate M2?

**Recommendation (adopted in PLAN as B45): make the byrå a separate milestone, M2, after M1 (from 1.8.2028 at the earliest). Keep the data model byrå-ready from M0. Firm clients wait for M2; a firm's own payroll can be an M1 pilot as a direct customer.**

Why:
1. **The founder's direction.** Lock payroll first. BYR has 36 functions, 18 of them MVP-marked, which is the largest MVP block in these areas. Almost all of them add surface around payroll and do not change payroll correctness.
2. **External dependencies sit on the byrå path.** The agent system user, client delegation and bulk fetching depend on open Altinn/Digdir questions (K4 #8; fase1 M09, M11): an ID-porten client for the client-delegation API, `regnskapsforer-lonn` without the REGN role, and the 5-concurrent-call quota. These need TT02 tests and possibly a Digdir approval. Putting them on the M1 critical path adds months of lead time the team does not control.
3. **The legal minimum for a firm is small and mostly generic.** It covers personal login, access limited to assigned clients, per-person logging of submissions, recorded customer approval, preparer ≠ approver, and data kept 5 years. All of it falls out of the generic audit log, role grants and run approval. So a firm can pilot its own payroll in M1 as a direct customer without byrå machinery, and the byrå-lite slice in M2 stays small.
4. **What makes Brutto attractive to firms is M2 material.** That is the agent system user, bulk tax-card/A07 fetching, the queue across clients, copied templates, the GRFS documentation package, the exit package, usage counts and the licence model. It only pays off at tens of clients, and it is better built on a payroll core that has been through real months.
5. **Make these decisions in M0, because they are cheap now and expensive later** (D04, M13):
   - The tenant is the customer's opplysningspliktig (reporting entity), and the customer owns the data.
   - Users get access through role grants with context TENANT or CLIENT and an end date.
   - Several system users per tenant are allowed (standard now, agent in M2).
   - Every authority call and every submission is logged with person, tenant, payload hash and receipt, and kept for ≥ 5 years.

PLAN takes the pure direct-customer route: the 8 byrå-lite rows and F-BYR-07/08 are M2 in `scope.csv`, with no effect on direct customers. PLAN B45 adds an option to cost: a firm runs a client as a direct-customer tenant in M1, with the client approving a standard system user and the firm's staff as users in that tenant.

**M2 "Byrå" content.** `scope.csv` tags the 8 byrå-lite rows (section 3), F-BYR-07/08 (agent system user, client linking and diagnostics) and F-MYN-04/05 as M2. The list below is tagged LATER in `scope.csv`; it matches "later in M2" in PLAN §9:
- F-BYR-14, -15: bulk tax cards and A07/feedback.
- F-BYR-04: deputies.
- F-BYR-17: deadline alerts.
- F-BYR-18: template copy, without inheritance.
- F-BYR-29: GRFS package generated from the audit log.
- F-BYR-30: exit package.
- F-BYR-32, -33: usage and licence.
- Later in M2 or after: F-BYR-22, -24 (customer portal and mobile approval), F-BYR-16 (gated "send all") and F-BYR-34 (practice-system webhooks).

## 5. Top cuts (remove until a paying customer asks)

1. **AI and analytics extras:** F-POR-13 (ask-your-payslip AI), F-BYR-23 (AI input parsing; both blocked by S §3 pkt 11), F-BYR-20 (quality KPIs), F-BYR-36 (AML signals), F-BYR-35 (time measurement of firm staff; aml. chapter 9 issues).
2. **SD Worx-level HR breadth:** F-UTV-03, -04, -05, -06, -09, -10, -11 (competence search, job profiles, gap analysis, courses, goals, salary-review input, talent) and F-HEL-10, -12.
3. **Intranet features:** F-KOM-07, -08, -09 (announcements, carousel, messages), F-POR-07, F-POR-11, F-HR-06, F-HR-07.
4. **Firm-scale features:** F-BYR-05, -09, -21, -25. F-BYR-25 is the only "Must" that is cut. GRFS 7.2 requires discussing unreasonable input with the customer, but e-mail plus the deviation acknowledgement in the run already meets that.
5. **Organisation niceties:** F-ORL-19, -22, -28, -32, -33 (fixed fee runs, congress mode, fast payout, RF-1301, annual cycle). Extra runs and the generic deadline engine cover them, and the RF-1301 data lives in the accounting system.
6. **Duplicates:** F-LED-06 (Teams/Slack approval), F-LED-12 (delegation per type), F-POR-18, F-POR-29.

Biggest **deferrals** by effort:
- Manager approvals: all of LED except -04 and -13.
- The full app: POR-02, -03, -05, -09, -10, -12, -14…-26.
- The OrgLab/Tikket engagement model: ORL-02…-31.
- HEL follow-up: 10 functions.
- Byrå automation: 18 functions LATER (on top of the 10 BYR functions in M2).

## 6. Entities for M0/M1

**Owned by these areas and needed (4 of 51 for M0/M1 with about 38 fields, plus 2 for M2 with about 16; about 54 of 138 fields in all):**

| Entity | Tier | Keep (approx.) | Drop or defer (over-engineering for M0/M1) |
|---|---|---|---|
| D-Dokument (17) | M0 | ~9: id, owner, type (payslip, a-melding upload file, voucher file, deduction agreement, engagement letter, annual statement), file, sha256, source, delete-not-before, visible-to-employee, created | versions/previous version, signatories, signature proof, legal hold, access level per type (derive from type), retention-rule reference (constant: 5 years after year-end) |
| D-Bruker (26) | M0 for payroll users (PLAN's User table); BankID fields M1 | ~8: id, type (PERSON/AGENT/SERVICE), display name, identity-key hash (HMAC of fnr), e-mail, status, created, last login | passkey and SSO fields, Digipost flags, payslip channel, language, accessibility prefs, no-BankID/ID-control refs, leaver read-until date, bankid_sub |
| D-Rolletildeling (21) | M1 | ~10: id, user, role (about 7 of 20 values), context type (TENANT/CLIENT), context id, valid from/to, granted by/at, revoked at/reason, optional approved-by | visibility level, personnel responsibility, sub-unit inheritance, sensitive access packages, confidential group, amount limit, source (SCIM/HR), periodic re-confirmation |
| D-Klient (36) | M2 (byrå-lite) | ~11: id, firm, tenant, orgnr, name, from/to, responsible accountant, who approves pay, who submits, engagement-letter doc, status | all Altinn/REGN diagnostics (M2), risk level/control requirement, invoice recipient, template, bank cut-off, accounting system, practice-system ref, instructions, contact list, end reason, retention date, and `kanalbeskyttelse_til` (a commercial clause that does not belong in the product data model) |
| D-Byra (22) | M2 (byrå-lite) | ~5: id, name, orgnr, quality responsible, status | hierarchy level/parent, pricing model, volume tiers, annual cap, partner agreement, central billing, branding, SSO/SCIM, time-measurement consent date, locked template fields, agent system user (M2) |
| D-Varsel (16) | M1 | ~11: id, type key, recipient, channel (EMAIL/APP), text parameters, link, tenant/client, status, sent, error, dedup key (keep address hash for old-channel account notices) | quiet-hours planning, read receipts, SMS/Teams/Slack channels |

**Folded into entities owned by other areas instead of separate entities:**

| Entity | Instead in M0/M1 |
|---|---|
| D-Kundegodkjenning (22) | M2: about 7 "external approval evidence" fields on KJO's run approval: channel, approver name, time, attachment doc, attachment sha256, registered by, authorisation doc. The summary copies, second approver and strong-auth flag are dropped. |
| D-Mottakerklasse (20) and D-Engasjement (31) | One enum `recipient_class` on D-Arbeidsforhold, plus a static consequence table in the rule pack. |
| D-Varselregel (11) | Constants in code. |
| D-Oppgave (16) | A derived query. Nothing is persisted. |
| D-Fullmakt (20) | M2: a document reference on D-Klient. |

**Fields that other areas' entities need for these M0/M1 functions** (for the owning reviewers):
- **D-Lonnsslipp (KJO):** delivery status per channel (published, delivered, failed, opened, delivered manually). This is Matrix finding #9.
- **D-Lonnskjoring (KJO):** tracks after approval (B43), and the approval hash with the evidence fields above.
- **D-Arbeidsforhold (PER):** arbeidsforholdstype (ordinary or frilans) and `recipient_class`.
- **D-Lonnsart (LON):** a board-fee pay type with its lønnsbeskrivelse and flags: no holiday pay, no OTP basis, AGA, percentage withholding.
- **D-Person (PER):** encrypted fnr with an HMAC index for BankID matching.
- **D-Revisjonslogg (SIK) and D-Innsending (MYN):** acting person, tenant, payload hash and receipt, retained ≥ 5 years.
- **D-Frist (MYN):** deadlines for a-melding, forskuddstrekk (tax withholding) and AGA.
- **D-Systembruker (MYN):** several per tenant.

**Not needed as entities in M0/M1 (45 entities including the folded ones above, about 700 fields):**
- POR and LED: D-Innloggingsmetode (16), D-Invitasjon (23), D-Lonnsslippforklaring (14), D-Delegering (20), D-Godkjenningsregel (20).
- BYR: D-Byramal (16), D-Malunntak (12), D-Grunnlagsinnsending (21), D-Oppdragsdokumentasjon (29; generate from the audit log in M2), D-Fakturagrunnlag (21; a query, not an entity), D-Timeforslag (11), D-Eksportpakke (15).
- ORL: D-Honorarvedtak, D-Honorarsats, D-Organisasjonsprofil, D-Moteoppmote, D-TaptArbeidsfortjeneste, D-Frikjopsavtale, D-Arrangement, D-Utoveroppdrag.
- HR extension: all 8 UTV and 4 HEL entities, D-Arbeidsavtale, D-Sjekkliste, D-Utstyr, D-Melding, D-Kunngjoring, D-Arbeidsflytmal and D-Arbeidsflyt.

B34 only requires the *canonical person and employment model* to tolerate the HR extension. It does not require these tables to exist now.

## 7. Legal must-haves (M0/M1 customer profile)

| Requirement | Source | Where it lands |
|---|---|---|
| Written payslip at each payment showing the calculation, holiday-pay basis and deductions. It must reach every recipient, including board-fee recipients, staff without BankID and leavers (final settlement). | aml. § 14-15 sixth paragraph; GRFS 7.7 | F-KJO-42 content; F-POR-08 (M0); delivery in M1 through Digipost (F-POR-12) with Digipost print or manual delivery as fallback (F-POR-04). Leavers get the final-settlement slip in their Digipost mailbox or by hand |
| Payroll documentation retained 5 years after year-end | bokføringsloven/-forskriften; S §1 pkt 1 | F-HR-01 (M0) |
| Annual statement to each recipient by 31 January, including holiday-pay basis | ferieloven § 10; 31.1 deadline [verify hjemmel, K4 #6] | F-POR-16 + F-MYN-36 (M1), delivered through Digipost. Brutto submits no 2026 period (B44), so the first hard date is 31.1.2028, for our own 2027 payroll (gate AS27: 14.1.2028). |
| Written prior agreement for deductions by agreement (paper or PDF is enough) | aml. § 14-15 (2) c; HR-2021-2532-A | F-HR-01/-02 (upload in M1) |
| Secure handling of payslips, which contain art. 9 data (union dues, sick pay): no unencrypted PDF e-mails, neutral notifications | GDPR art. 9, art. 32 | F-POR-12 (Digipost), F-KOM-01; employee notifications F-POR-27 are LATER |
| Access ends when people leave or engagements end | GDPR art. 32 | F-LED-13 |
| Correct a-melding coding of board fees (frilans type, `styrehonorarOgGodtgjoerelseVerv`, percentage withholding or 50 %, AGA, no holiday pay or OTP) | a-melding rules; Skatteetaten | F-ORL-01/-15 |
| *Byrå (M2):* personal login and access only to assigned clients; responsible accountant and written engagement; per-person logging of submissions; customer approval of pay unless agreed otherwise; segregation of duties with a small-firm exception; documentation kept 5 years | regnskapsførerloven §§ 4-2, 5-1, 5-2, 5-3; GRFS 2.3, 3.4, 8.1, 8.6 | F-BYR-02/-03/-10/-19/-26; audit-log retention from day one |
| *Byrå (M2):* data processing agreement chain (customer as controller, firm as processor, Brutto as sub-processor) and DPIA | GDPR art. 28, 35; J10 | Contract, not a function, but needed before the first byrå client |

The following are **not** legal requirements for this profile (Plan v1 buys Digipost anyway as the M1 channel): Digipost, the explained payslip, multiple languages, self-service account change, manager approvals and HEL in Brutto. Whether WCAG applies to a private internal portal is [verify]. It is needed for public-sector customers.

## 8. Biggest risks

1. **Annual statement deadline.** Settled by B44: the current system submits all of 2026 and issues the 2026 sammenstillingsoppgave. Brutto's first is for our own 2027 payroll, due 31.1.2028. F-MYN-36 was marked "After MVP", inconsistent with F-POR-16 (MVP); `scope.csv` now has both in M1.
2. **Payslip channel.** Without a decision (BankID page or Digipost), M1 pilots end up with e-mailed PDFs. That is an art. 32 risk because of union dues and sick pay. PLAN §6.2 adopts Digipost (bought) with print and manual fallback; sign the Digipost contract early. The BankID broker (Signicat/Criipto/Idura; pricing unknown) is still needed for payroll approval in M1.
3. **Byrå scope creep and Altinn lead time.** The agent system user path has unresolved Digdir/Altinn questions. PLAN moves it to M2 (B45), which keeps that external lead time off the M1 critical path.
4. **Board fees to employees.** Employee board members are common in AS with more than 30 employees. The a-melding treatment (ordinary relation or separate frilans relation, K5 #1) and the AGA zone for frilans (K5 #2) are unanswered. Get an answer or a documented conservative default before the first M1 pilot. Until then, hold such lines for manual handling.
5. **Organisation pilots hitting special rules.** These are § 2-32 tax-exempt organisations (the 10,000 rule), § 23-2 AGA exemption, foreign artists and lost earnings. Wrong tax or AGA here hits the recipient. Screen pilots, or use the manual workaround.
6. **The same rule built several times.** Segregation of duties appears in five functions (LED-04, BYR-19, KJO-23, SIK-12, BET-19), and notifications/tasks in six (POR-27, LED-08, BYR-17, KOM-01/02/03, PLA-30). Assign one owner each (SIK/KJO for segregation of duties, KOM for notifications), or the three-person team builds them two or three times.
7. **Single-person customers.** Many 20–50 employee customers have one payroll person. If segregation of duties is enforced without the logged-exception path, they cannot run payroll at all.

## 9. Open questions and which block M0/M1

| Question | Owner | Blocks? |
|---|---|---|
| K4 #6 Hjemmel, deadline and sender for the sammenstillingsoppgave | Jurist | **M1** (Brutto submits no 2026 period, B44; first statement due 31.1.2028). Build it as required anyway, so it does not block the build. |
| K5 #1 Board fee to an employee: ordinary or separate frilans relation | Skatteetaten | **M1** for AS pilots with employee board members. Not M0. |
| K5 #2 AGA zone for frilans relations | Skatteetaten | M1 only for multi-zone pilots. Screen pilots to zone I or one zone. |
| K5 #10 Is a recorded e-mail approval enough under GRFS 8.6? | Revisor | **M2** (byrå-lite is M2), because it is the only approval path there. Ask the first firm's quality control. |
| K4 #8 / fase1 M09, M11 Client delegation, REGN role, quota | Teknisk/Digdir | **M2** (agent system user). Not blocking: M1 direct customers use standard system users. |
| K5 #7 Fallback for staff without BankID or Digipost | Gründer | M1. Decide now: Digipost print, or manual delivery by payroll (F-POR-04). |
| K5 #6 How long leavers keep access, and on what legal basis | Jurist | Not blocking: leaver access (F-POR-28) is LATER under Plan v1, and Digipost delivers the final-settlement slip to the leaver's own mailbox. |
| K7 #0 Boundary between KOM and LED/POR for inbox and notifications | Teknisk | Not blocking. Decide now: KOM owns e-mail notifications and the derived list. |
| K5 #11 Proof that forskuddstrekk is paid | Partner | Not blocking. Manual "paid on date" confirmation in M1. |
| fase1 D04, M13 Byrå/tenant model, several system users per customer | Peter/Sander | **M0 design decision.** Cheap now, expensive to retrofit. |
| fase1 G04, G06 Segregation of duties; re-approval after change | Peter/Sander | M1. Answer together with KJO-23/SIK-12. G01–G03, G05 and G07 are LATER (B39). |
| fase1 P02 "Who is the first user?" (suggests byrå first) | All three | Superseded by the founder's direction, B19 and PLAN (B45). Answer: own company, then direct customers, then firms (M2). |
| K5 #0, #3, #4, #5, #8, #9, #13–#16; K6 #1; K7 #1–#7; K1 #6, #7 | various | Not blocking: they concern LATER or CUT functions. K1 #7: confirm that whistleblowing and HSE stay outside Brutto (CUT). |

## 10. Cross-area flags

- **F-MYN-36** (annual statement) was "After MVP" but is required for M1; `scope.csv` now has it in M1. Brutto's first one is due 31.1.2028 (B44).
- **F-MYN-14** (manual upload) was "After MVP" but is the M0 submission path; `scope.csv` now has it in M0 (JSON for manual upload).
- **F-KJO-42** (payslip content) owns what the slip says. POR only owns storage, access and delivery.
- **Segregation of duties** should have one owner (F-SIK-12 / F-KJO-23). F-LED-04 and F-BYR-19 then become thin references.
- **BankID broker** for approvals (F-SIK-01) is M1. Employee login (F-POR-01) and the agent-confirmation flow (F-PLA-37) are LATER under Plan v1, but should reuse the same integration and contract when they come.
