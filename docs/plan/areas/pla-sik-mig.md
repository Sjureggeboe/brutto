# Scope review: PLA, SIK, MIG (29.10.2026)

> Working paper from the scope review of 29.10.2026. PLAN.md is the main plan and `docs/plan/scope.csv` holds the final tier per function; where this paper disagrees, they win.

Reviewer: platform and integrations (PLA), security, access and privacy (SIK), and migration and import (MIG).
Source: every function in `omr-K6.json` for the three areas (108 functions), their entities, the K6 questions (`sporsmal`), design decisions B4–B43, `fase1.json` (D, H, I, J, X) and `research/R0-matrix-lonn-omrader.md` (agent K6).
Detail per function: `docs/plan/scope.csv` (rows with area PLA, SIK or MIG).

**Tier rule used.** Each function gets the *earliest* tier in which its simplest lawful version is needed. "NO CODE" in `scope.csv` means a document, checklist or procedure covers that tier.

## 1. Tier counts

| Area | Functions | M0 | M1 | M2 | LATER | CUT | Marked MVP today |
|---|---|---|---|---|---|---|---|
| PLA Platform and integrations | 37 | 3 | 10 | 0 | 22 | 2 | 13 |
| SIK Security, access and privacy | 36 | 11 | 11 | 1 | 12 | 1 | 20 |
| MIG Migration and import | 35 | 10 | 13 | 0 | 8 | 4 | 18 |
| **Total** | **108** | **24** | **34** | **1** | **42** | **7** | **51** |

- **M0 is mostly documents and checklists.** 10 of the 24 M0 items are NO CODE, a document or manual entry through the existing API (F-SIK-29, F-SIK-33, F-SIK-36, F-MIG-03, F-MIG-17, F-MIG-27, F-MIG-28, F-MIG-32, F-MIG-33, F-MIG-35). New M0 code in these areas is limited to:
  - managed OIDC login with MFA, a CLI device flow and re-authentication through the identity provider
  - fixed roles
  - `tenant_id` on every row and one policy module (PLAN E7 turns RLS on before the first external customer)
  - field encryption of national ID and bank account with one key and a blind index (F-SIK-19, PLAN E9)
  - an append-only audit log
  - backup
  - CI regression
  - API/OpenAPI
  - voucher CSV and pain.001 (owned by REG/BET)
- The opening-balance input for the 2026 holiday-pay basis (F-MIG-22) is M1 with a date: our own payroll needs it by gate JUN27 (14.5.2027), not for the January go-live. There is no 2026 YTD import: Brutto reports no 2026 period (B44).
- **The cut is in depth, not in count.** All MVP-marked functions in these areas except F-SIK-09, F-PLA-37 and F-SIK-06 stay in M0 or M1, but almost every one gets a much smaller version (the `simplest_lawful_version` column). Most of the weight is in the 42 LATER and 7 CUT functions: the partner-platform machinery, named adapters, generic ABAC and compliance registers.
- **10 functions marked "Etter MVP" (after MVP) are needed earlier:**
  - M0: F-MIG-01 (as cutover fields), F-MIG-03 (manual A07 + exports), F-MIG-33 (cutover checklist), F-MIG-35 (keep migration evidence), F-SIK-29 (system description, a legal duty from the first live month; this paper first put it in M1)
  - M1: F-SIK-10 (break-glass as procedure), F-SIK-31 (agent limits; M1 has remote MCP with read and draft tools), F-SIK-32 (security pack), F-MIG-24 (open sick-leave cases), F-PLA-32 (agent identity for the M1 remote MCP)
  - F-PLA-30 (digital post and notifications) stays LATER. **Plan v1:** payslips and the annual statement go through Digipost, bought, as F-POR-12 (M1); the employee login and BankID payslip page this paper assumed are LATER.
- **Three MVP-marked functions move later:** F-SIK-09 (auditor access, LATER; the first audit season is spring 2028, and until then the customer exports reports for its auditor), F-PLA-37 (human confirmation of agent-started actions, LATER under Plan v1) and F-SIK-06 (the byrå→client relation, M2 under B45).
- **Plan v1 decisions after review (29.10.2026):** no MCP at all in M0; in M1 actions with legal effect are human-only operations that agent tokens cannot call, and the confirmation flow F-PLA-37 is LATER; field encryption (F-SIK-19) and the system description (F-SIK-29) are M0; the 2026 holiday-pay base import and the annual summary/YTD for mid-year switches (F-MIG-20, -21, -22) are M1.

## 2. Narrative

**PLA.** PLA is designed as a full partner platform:
- app registration, consent and installations (F-PLA-08–12)
- source-of-truth registry and source switching (13–14)
- webhooks (19), sandbox with time machine (06), certification (07)
- an integration catalogue with ~40 named systems (22–31)

None of this is needed while Brutto is the only source and there are no partners (R3 D-41, Matrix analysis).

What stays:
- **M0:** the API itself (F-PLA-01, because B41 makes the UI a client of the API), the voucher file (26) and pain.001 (27).
- **M1:** a generic pay-input CSV/endpoint with few states (15), deterministic matching on employee number (17), mapping per source profile (18), idempotency and problem+json (03), minimal docs (05), `/v1` convention (02), BankID through a broker (29), feature flags (34), and the MCP block (32, 33), as B41 is narrowed in PLAN §4. The confirmation flow (37) and general digital post (30) are LATER; payslips go through Digipost as F-POR-12.

The MCP block is the single largest optional item in M1, and its draft tools are first in the M1 cut order (PLAN §6.3). PLAN §4 settles its scope: remote MCP with read tools, draft tools (pay inputs and run drafts) and two generic tools, off by default per tenant. Actions with legal effect (approve, submit, pay, change a bank account or a role) are human-only operations; agent tokens, issued by a named human, cannot call them. National ID, bank account, protected address, health and union data never leave via MCP. Agent-started actions with BankID confirmation (F-PLA-37), agent submission for customers, an OAuth server, webhooks and a developer portal are LATER (after the DPIA and an MCP addendum to the DPA). In M0 the interface is the `brutto` CLI, and there is no MCP at all while real payroll data is in the system (this paper first allowed an optional stdio MCP on test data). Time, expense, Huma, OrgLab/Tikket and pension integrations are all replaced by the generic CSV in M1.

**SIK.** Norwegian law and GDPR set a *risk-based* baseline, not a feature list. The legal core is short:
- personal accounts with MFA
- need-to-know access, including GDPR art. 9 special categories (health, union membership)
- integrity and traceability (audit log)
- availability and restore (backup)
- records of processing, a DPA and breach handling
- the bookkeeping system description

Field encryption, the access log, hash chains, ABAC, SCIM, SIEM, ISAE 3402 and ISO 27001 are *not* legal requirements. Some are founder rules (S §2 pkt. 6: encrypt fødselsnummer (national ID) and account number, and log reads). Under Plan v1, field encryption with one key and a blind index is M0 (E9, F-SIK-19), with per-tenant keys and the read log in M1; the rest is LATER. Retention, deletion, storage register, data-subject requests and export become documents or manual procedures until volume or the first deletion date (~2032) requires code.

**MIG.** The design (D-Migreringsprosjekt has 35 fields) is a byrå-scale migration factory. For M0 the team migrates ≤10 people, which needs IDs, a few balances, a parallel comparison and a checklist (section 7). For M1 the minimum is one Excel/CSV template that uses official a-melding code values, one signed import pipeline, an automated diff against A07 and one parallel month. Source adapters are replaced by the template:
- CUT: PowerOffice, Visma/H&L, SD Worx
- LATER: Tripletex, ReAi, Huma

The AI part of F-MIG-13 is CUT.

## 3. Entities for M0/M1

### 3a. Owned by PLA/SIK/MIG: 27 entities, 557 fields → about 130 fields needed in M1

| Entity (fields today) | Tier | Proposed shape | Over-engineering to drop now |
|---|---|---|---|
| D-Revisjonslogg (29) | M0 | ~18 fields: seq, id, tenant, time, actor_type, actor_id, on_behalf_of, channel, action, resource_type/id, person_id, field, before/after (masked), reason, correlation_id, auth_method, step_up | `hash_forrige`/`hash` and daily seal (LATER, ISAE); `break_glass_id`; `ip_adresse`/`land` (personal data with little value now) |
| D-Programversjon (18) | M0 | ~6: version/git sha, engine version, rule-package version, deployed_at, payroll approver; stamped on every pay run | `release_diff_*` json, `andel_agentcommits`, `sbom_ref`, change-freeze fields |
| D-Migreringsprosjekt (35) | M0 | **No entity.** 4 fields on the opplysningspliktig (reporting entity): `previous_system`, `previous_system_last_period`, `brutto_first_period`, `old_system_readable_until` | Phase state machine, complexity, counts, go/no-go, plan-B, consent document, etc. (LATER, byrå factory) |
| D-Rolledefinisjon (21) | M0 | **No table.** Roles as a code enum with fixed permissions | `eier_type`, `arvet_fra_id`, `versjon`, `tildelbar_av`, per-role MFA/step-up lists, scope types |
| D-Tilgangslogg (21) | M1 | **Merge** into the audit log: add `data_class`, `count`, `file_hash` | Separate hash chain, `tjenstlig_behov`, `break_glass_id` |
| D-Arbeidsdelingsregel (16) | M1 | Rules in code; ~7-field record only for a tenant exception (rule, reason, control recipient, approved_by/at, valid_to) | `handling_a/b`, `felles_objekt`, `handhevelse` as data |
| D-Krypteringsnokkel (16) | M1 | ~6: tenant, data class, KMS ref, version, status, created (or a wrapped DEK column on the tenant) | Blind-index/webhook/signing key types, shredding fields |
| D-Abonnement (18) | M1 | ~6: tenant, status, feature flags, MCP/AI opt-in, contract start, after-termination choice | Price plan, price unit, unit/minimum price, invoice recipient, `celle_id`, `aktive_moduler` |
| D-Mappingregel (25) | M1 | ~12: tenant, source profile, domain, source value/description, target value (null = unknown), status, approved_by/at, version, valid_from | `ki_konfidens`, `ki_begrunnelse`, `arvet_fra_id`, `transformasjon`, `faktor`, `flaggavvik_ved_migrering`, test-calc reference |
| D-Kildeprofil (9) | M1 | Keep ~6 | `installasjon_id` |
| D-Integrasjon (27) | M1 | ~8 as an **API token / agent grant**: user, tenant, scopes (read/write), agent flag, created, expires, revoked | Shadow mode, amount limits, byrå assignment, orgnr check, IP allowlist, partner terms |
| D-App (28) | LATER (needed only if Brutto runs its own OAuth server for MCP; PLAN §4 puts that in LATER) | ~6 as an OAuth client: client_id, name, redirect URIs, tenant, status, created | Catalogue, certification, partner terms, key prefixes, "same owner" |
| D-Importjobb (34) | M1 | ~15: id, tenant, type, source system, file name/hash, format, mode, status, row/ok/error counts, control totals (source and imported), signed_by/at, imported_at, used_in_approved_run, rolled_back_at | `kildebytte_id`, `installasjon_id`, `tegnsett`, `mal_versjon`, quarantine count, separate idempotency key (the file hash is enough) |
| D-Importrad (18) | M1 | ~12 | `ekstern_versjon`, `manuelt_rettet_av` |
| D-Parallellkjoring (28) | M1 (M0 = spreadsheet) | ~8: period, type, Brutto run, old-result import, status, approved_by/at | Eight separate `diff_*` columns (derive from D-Migreringsavvik), byrå approval, coverage % |
| D-Migreringsavvik (24) | M1 (M0 = spreadsheet) | ~12: run/import, person/arbeidsforhold, control point, period, old/new/diff, category A–D, status, customer_approved_by | `ny_gylden_case`, `rettet_i_importjobb_id` |

LATER or CUT as entities, about 190 fields replaced by documents:
- D-Kilderegister, D-Kildebytte, D-Hendelse, D-Webhookabonnement, D-Personkobling
- D-Lagringssted, D-Oppbevaringsregel, D-Underleverandor (a list in the DPA annex)
- D-Personvernforesporsel (manual), D-Sikkerhetshendelse (ticket/doc)
- D-Lagringsmelding (CUT with F-SIK-24)

### 3b. Entities owned elsewhere that M0/M1 functions in these areas use

- **M0:**
  - D-Virksomhet, D-Underenhet, D-Person, D-Personbankkonto, D-Arbeidsforhold, D-Stillingsperiode
  - D-Akkumulator: holds the YTD and holiday-pay opening values. `apningsverdi` and `apningsverdi_kilde` already fit. It needs a key per a-melding *inntektsbeskrivelse* (income description) for the annual summary.
  - D-Fastlinje, D-Pensjonsordning, D-Pensjonsmedlemskap, D-Lonnsart, D-Lonnskjoring, D-Lonnslinje, D-Lonnsslipp
  - D-Bilag, D-Postering, D-Kontomapping, D-Betalingsoppdrag, D-Betalingslinje, D-Bankkonto, D-AMelding, D-Bruker, D-Rolletildeling
- **M1 adds:**
  - D-Lonnsgrunnlag (pay input)
  - D-Permisjon, D-Sykefravaerstilfelle, D-Trekkpalegg, D-Trekk, D-KID
  - D-Systembruker, D-Godkjenning (D-Klient comes with M2)
  - D-Avvik and D-Beregningsspor (MCP tools)

Over-engineering noticed in borrowed entities (for their owners):
- **D-Rolletildeling (LED, 21 fields, a 20-value role enum).** M1 needs ~8 fields (user, role, context type/id, valid_from/to, granted_by, revoked_at). Drop for now:
  - `innsynsniva`, `personalansvar`, `inkluderer_underenheter`
  - `konfidensiell_gruppe_id`, `beloepsgrense`, `sist_bekreftet`, `kilde` (SCIM)
- **D-Bruker (POR, 26 fields).** M1 needs ~10. Drop:
  - `tilgjengelighetsvalg`, the multi-language enum
  - `uten_bankid`/`id_kontroll_ref` (go with F-SIK-02, LATER)
  - the Digipost fields (Digipost delivery under F-POR-12 is addressed by national ID on D-Person, not by user fields)
- **D-Feriesaldo (FRA, 27 fields).** Not needed for MIG in M0/M1. Holiday-pay *basis* lives in D-Akkumulator; holiday *days* are LATER (F-MIG-23).

## 4. Top cuts

1. **Partner-platform machinery → LATER:**
   - app registration, installation, consent, byrå install, overview (F-PLA-08–11), shadow mode (12)
   - source registry and switching (13–14), webhooks (19), monitor/status page (20), pay-calendar events (21)
   - sandbox with time machine (06), rate-limit policy (04), metering (35)
   - CUT: certification (07) and unified API/practice systems (31)
2. **Named integrations → LATER, replaced by one generic pay-input CSV (F-PLA-15):** Huma (22), time/shift (23), expenses (24), OrgLab/Tikket (25), pension files (28). The built-in assistant (36) is LATER (B13).
3. **Migration adapters and factory:**
   - CUT: PowerOffice (F-MIG-07), Visma/H&L (08), SD Worx (09), Huma source switch (34), and the AI part of F-MIG-13
   - LATER: Tripletex (05; also N40 API-terms risk), ReAi (06), Huma import (12), byrå factory (02), a-melding history import (11), historical payslips (29), holiday-day balances (23), pre-cutover corrections (19, handled by contract)
4. **Compliance registers as products → documents:**
   - storage register (F-SIK-23), retention rules (21), deletion/legal hold (22), export/archive (26), data-subject requests (30), SoD report (14)
   - CUT: § 7-5 notification generator (24), which is moot with all data in Norway (B9)
5. **Identity breadth → LATER:** SCIM (F-SIK-04), SSO/SAML, the no-BankID fallback (02), ABAC/confidential groups (07), auditor role (09), SIEM/monitoring (17–18). The byrå→client relation (06) is M2.
6. **Entity slimming:** about 557 → 130 fields in M1. The biggest items:
   - D-Migreringsprosjekt becomes 4 fields
   - D-Rolledefinisjon and D-Tilgangslogg become code or a merged log
   - D-Parallellkjoring drops its 8 diff columns

## 5. Legal must-haves (cannot be cut for the M0/M1 profile)

| Requirement | Source | Smallest compliant version | Tier |
|---|---|---|---|
| Keep arbeidsforhold-ID (employment ID), start date and change dates across a system switch | Skatteetaten guidance on changing payroll system; A-marked §7.1; R2 F5 | Manual entry or template, checked against A07 | M0 (F-MIG-16/17) |
| Never report one period from two systems | A-marked §7.1 | Cutover fields on the opplysningspliktig + checklist | M0 (F-MIG-01/33) |
| Holiday-pay basis carried over; holiday-pay basis shown in a summary to the employee | Ferieloven; ferieloven § 10 (B-myndigheter §2.7, verified) | Import the 2026 basis per employee, closed on payout dates up to 31.12.2026 and checked against 2940 | M0+ track: by 14.5.2027, gate JUN27 (F-MIG-22 is M1 with a date under Plan v1) |
| Annual summary (sammenstilling) when Brutto reports part of a year | Treated as a legal duty until a lawyer answers (D-36) | Generate from imported YTD + Brutto runs by 31.1 | M1, for pilots that switch mid-year (F-MIG-20/21, both M1 in `scope.csv`). Not needed for our own payroll: Brutto reports no 2026 period (B44) |
| Payslip at payment; deductions only with a legal basis or prior written agreement | aml. § 14-15 | PDF payslip; hold net deductions without an agreement (F-PLA-15); agreement reference on agreed deductions (F-MIG-25) | M0 (payslip, KJO) / M1 |
| Payroll documentation incl. hours per day for hourly staff, and an easy-to-read system description | bokføringsforskriften § 5-6 | Per-day lines in the pay-input CSV; one versioned system-description document | M0: short system description signed before the first live run (F-SIK-29, M0 under Plan v1); M1: per-day CSV lines (F-PLA-15) and the description extended per customer |
| Retain payroll accounting material 5 years, stored in Norway (or notify), protected against loss | bokføringsloven § 13 ff.; forskriften ch. 7 (S §1) | Norwegian region + second Norwegian backup location; no deletion before 5 years | M0 (F-SIK-25) |
| Security appropriate to risk: personal login + MFA, need-to-know, integrity, restore, testing | GDPR art. 5(1)(f), 25, 32 | Section 6 | M0/M1 |
| Fødselsnummer (national ID) only where secure identification is needed; no FNR as key or in logs | personopplysningsloven § 12 | Internal person ID; masked by default; log filter | M0 |
| Special categories (sick pay, absence reasons, union dues) need a legal basis and need-to-know | GDPR art. 9(2)(b), personopplysningsloven § 6; B-myndigheter §11 | Separate "health & union" permission; never via MCP; external advisor review | M1 (F-SIK-08) |
| Records of processing (no <250-employee exemption: payroll is not occasional and includes art. 9 data) | GDPR art. 30(1), (2), (5) | Spreadsheet/document | M0 (own company), M1 (as processor) |
| DPA with every customer; sub-processor list; byrå chain | GDPR art. 28; B-myndigheter §11 | Standard DPA; the byrå variant comes with M2 | M1 (F-SIK-27); byrå chain M2 |
| Breach handling: processor tells the controller without undue delay; controller tells Datatilsynet within 72 h | GDPR art. 33/34 | One-page procedure | M0 (F-SIK-33) |
| DPIA where processing is high-risk | GDPR art. 35 | Likely not required for 3 employees; a reference DPIA for customers, especially with agent/MCP access | M1 (F-SIK-28) |
| Synthetic data only in Skatteetaten/NAV test environments | B-myndigheter §11 | Rule + Tenor/Dolly | M0 (F-SIK-36) |
| Honour trekkpålegg (garnishments) from day one | Employer liability (D-23) | Manual 4-eyes entry with KID before the first run | M1 (F-MIG-25); M0 = confirm none |
| Running leaves keep their permisjons-ID | a-melding rules (D-42) | Template/manual | M1 (F-MIG-26) |
| Open sick-leave cases keep the correct arbeidsgiverperiode (employer period) and refund status | folketrygdloven ch. 8 | Manual entry | M1 (F-MIG-24) |

**Not legally required (keep out of M0/M1 unless decided otherwise):**
- ISAE 3402 / ISO 27001: B15 puts type 1 about 6 months after the first customer is live
- SSO/SCIM
- generic ReBAC/ABAC
- a hash-chained audit log
- SIEM
- crypto-shredding
- § 7-5 notification (moot if all data stays in Norway)
- field-level encryption and the read-access log: founder rules (S §2 pkt. 6), kept in M1 in their smallest form

GRFS (good accounting practice, which applies to byrå clients from M2) adds personal login + MFA and a vendor control/contingency description. Both are covered by F-SIK-01 and F-SIK-32 in M1.

## 6. Minimal security baseline

### M0: own payroll, ≤10 employees, Brutto's own company as data controller, no external customers
Must be in place **before the first real fødselsnummer or account number lands in production** (before the first shadow run on real data, November–December 2026):
1. **Hosting in Norway:** managed Postgres in a Norwegian region, encrypted at rest (provider default), TLS everywhere, secrets in a managed vault.
2. **Login:** personal accounts through managed OIDC (e.g. Entra ID) with MFA and a CLI device flow; no BankID in M0 (PLAN §1.3). The interface is the `brutto` CLI over the REST API; there is no web UI in M0. No shared accounts. Forced re-authentication through the identity provider on pay-run approval and bank-account change (F-SIK-01/03).
3. **Roles:** two fixed roles in code: payroll admin and approver (F-SIK-05).
4. **Multi-tenant from the first migration:** `tenant_id` on every row + one policy module; a CI test for cross-tenant reads (F-SIK-11). Postgres RLS: `scope.csv` F-SIK-11 says from the first migration; PLAN E7 requires it on before the first external customer. Turning it on in M0 is allowed and cheap.
5. **Audit log:** append-only, for every write, with channel (ui/api/import/job) and masked before/after (F-SIK-15). Stamp each pay run with program/rule version.
6. **Encryption and masking:** FNR/D-number and account number encrypted at field level with one key (KEK in Key Vault in Norway) and an HMAC blind index (F-SIK-19, PLAN E9); masked in API and CLI responses by default; never used as keys; a log filter strips 11-digit IDs and account numbers from application logs and error tracking.
7. **Backup:** PITR + a nightly encrypted dump to a second Norwegian location/provider; one restore test before the first shadow run on real data (F-SIK-25).
8. **CI:** golden cases + regression on the previous month, cargo-audit/deny, secret scanning; a human reviews all money/access/authority code; Sjur signs calculation changes (F-SIK-35, fase1 T02).
9. **No production data outside production.** Do not connect the production tenant to any LLM or MCP client (including the team's coding agents). M0 has no MCP at all (PLAN §4). Sending the team's own payroll data to a model provider would be a new transfer and purpose for Brutto's company as controller (F-SIK-31, F-SIK-36).
10. **Paperwork (NO CODE):**
    - art. 30 record for the team's employee data
    - 1–2-page risk assessment
    - one-page breach procedure
    - a note on who has production access

**Not needed in M0:**
- a DPA, as long as the team's employer is the same company that operates Brutto; if not, a simple DPA is required
- a DPIA
- per-tenant keys (one-key field encryption is M0)
- the access log
- ReBAC, BankID, SoD enforcement
- a pentest
- the security pack

### M1: 3–5 direct pilots (a firm's own payroll can be one; firm clients are M2)
Adds to M0:
1. **Contracts:**
   - DPA for direct customers + public sub-processor list (the byrå variant, with Brutto as sub-processor, comes with M2)
   - art. 30(2) processor record
   - reference DPIA + external review of art. 9 handling and MCP agent access before the first pilot
   - 3–5-page security and contingency description (F-SIK-27/28/32)
2. **Authentication:** BankID through a broker for login and step-up: approval, account change, role change, personal-data export, signing balance imports (F-PLA-29, F-SIK-03).
3. **Access:**
   - ~6 fixed roles + a "health & union" unmask permission
   - (the byrå→client relationship comes with M2)
   - SoD blocks (preparer ≠ approver; no change to own salary or account) + the small-customer exception with a post-run report (F-SIK-05/08/12/13)
4. **Encryption:** the M0 field encryption moves to one data key per tenant (DEK) under a KEK in a Norwegian-region KMS, with documented rotation; masked in MCP (F-SIK-19/20). RLS on (PLAN E7).
5. **Read log:** unmask, export and bulk reads go into the same log store (F-SIK-16).
6. **Agent policy (remote MCP with read and draft tools is in M1, PLAN §4):**
   - off by default per tenant
   - agents can never approve or confirm
   - national ID, bank account, protected address, health and union data never via MCP
   - agent actions logged on behalf of the user, with agent tokens issued by a named human (no OAuth server in M1)
   - actions with legal effect (approve, submit, pay, change a bank account or a role) are human-only operations that agent tokens cannot call (F-SIK-31, F-PLA-32)
   - agent-started actions with BankID confirmation (F-PLA-37) and agent submission for customers are LATER (after the DPIA and an MCP addendum to the DPA)
7. **Testing:** external pentest focused on tenant isolation/IDOR before the first external customer (fase1 H08).
8. **Operations:**
   - break-glass as a procedure, with no standing production access
   - incident procedure with 24 h processor notice
   - payday contingency: payment file and payslips downloadable offline (F-SIK-10/33/34)
9. **Documentation:** the system description extended per customer and release (F-SIK-29; the M0 version exists from the first live month).

**LATER:**
- ISAE 3402 type 1 and then type 2 (start control evidence on the first production day, per B15 domain critic)
- ISO 27001
- SSO/SCIM, SIEM, hash chain/daily seal
- crypto-shredding, retention automation
- self-service data-subject requests
- confidential groups/ABAC
- sandbox

## 7. Minimal migration path

### M0: the team's own payroll (current system not stated in the repo: PLAN D2 asks Sjur to confirm it)

For table withholding (*tabelltrekk*) and percentage withholding, YTD is **not** needed, and December half tax needs no YTD either. YTD **is** needed for:
- the annual summary, if Brutto reports any 2026 period (it does not, B44)
- zone 1a *fribeløp* (AGA allowance), only if the team's sub-unit is in zone 1a
- *frikort* (tax-exemption card) limits, unlikely for this team

Holiday-pay basis is always needed: it drives June 2027 holiday pay and any termination settlement.

**Option A (recommended, smallest; adopted by PLAN as D1/B44).** Shadow November and December 2026; cut over on **1.1.2027** as a stretch (about 40 %). The planning date is period 2027-02, and 2027-03 at the latest; then the year-to-date figures for the 2027 months run in the old system are imported and checked against A07 (PLAN §1.3).
- The old system remains the reporting and paying master for all of 2026, including both a-meldinger and the 2026 annual summary.
- Brutto runs November and December in parallel. Per-employee results and the generated a-melding content are compared to the old system to the øre (F-MIG-31/32).
- Data to load, via scripted API calls, no import framework:
  1. persons, bank accounts and tax cards (entered by hand with four eyes, from Skatteetaten's tax-card file service or copied from the current system)
  2. arbeidsforhold with **arbeidsforhold-ID**, start date, type, %, STYRK, working-time arrangement, last salary-change date and last %-change date, taken from A07 for October (F-MIG-16/17)
  3. fixed pay lines and benefits (F-MIG-28)
  4. OTP scheme and membership (F-MIG-27)
  5. ongoing leave and permittering with their old leave IDs (PLAN §1.4 item 6)
  6. by 14.5.2027 (gate JUN27): each employee's final **2026 holiday-pay basis** from the old system, closed on payout dates up to 31.12.2026, with an "up to and including 2026-12" marker, plus confirmation that the 2025 basis was paid out (F-MIG-22). This paper first put this in January 2027; Plan v1 dates it to JUN27.
- Checklist items: confirm that trekkpålegg and open sick leave are absent, or imported and signed (PLAN §1.7 item 7); set the cutover fields (old system last period 2026-12 or 2027-01, Brutto first period 2027-01 or 2027-02; F-MIG-01/33); archive exports, A07, diff sheet and signed protocol (F-MIG-35); archive the old system's records for 5 years after each year-end (2026 → 31.12.2031) and then revoke the old vendor's Altinn system user (PLAN §1.4 item 7).
- The first real submission is the January 2027 a-melding (deadline 5.2.2027) in the stretch case, or February 2027 (deadline 5.3.2027) in the plan. This keeps the unverified annual-summary rule (D-36) and YTD import off the critical path.

**Option B (B19 read literally; not adopted, B44 rules it out).** Brutto submits November (and December) 2026. This needs everything in A, plus:
- YTD January–October per employee per *inntektsbeskrivelse* + forskuddstrekk (F-MIG-21)
- the 2026 holiday-pay basis January–October immediately (F-MIG-22)
- Brutto generating the **2026 annual summary by 31.1.2027** (F-MIG-20)
- the old system must *not* send November and must stay usable ≥3 months for corrections of January–October (F-MIG-19)

Option B gives an earlier real submission, which is useful given the Altinn II role change on 17.11.2026. It costs two extra deliverables and puts an open legal question on the December/January critical path.

### M1: pilot customers (go-live windows 1.1, 1.3 and 1.8; pilots live 1.8.2028 in the plan, or from period 2028-01 in the stretch case)
1. **Inputs:** the customer fills one Excel/CSV template from old-system reports (F-MIG-10) and grants a system user so Brutto can fetch A07 (MYN API; manual upload as fallback; F-MIG-03).
2. **Import:** Brutto's implementer prepares and the **customer signs** each import with step-up (F-MIG-04, D-35). The pipeline:
   - validation (F-MIG-15)
   - official a-melding codes, where unknown blocks (F-MIG-14)
   - manual pay-type mapping (F-MIG-13)
3. **Data loaded:**
   - persons and arbeidsforhold with IDs and change dates (16); leaves with permisjons-ID (26)
   - YTD per inntektsbeskrivelse + forskuddstrekk + AGA basis per sub-unit/zone + fribeløp and frikort used (21)
   - holiday-pay basis: prior year (unpaid part) and current year (22)
   - fixed lines and benefits (28); OTP (27)
   - **trekkpålegg entered manually with KID, 4 eyes** (25); open sick-leave cases entered manually (24)
4. **Verification:**
   - diff against A07 = 0 (17)
   - one historical shadow month, or a second live parallel month (30)
   - one live parallel month (31)
   - signed "equal to the øre" protocol (32)
   - cutover checklist (33); evidence kept for 5 years (35)
5. **Timing and contract:** cut over in the go-live windows 1.1, 1.3 or 1.8 (PLAN §3); no new starts in May–June or from mid-November to January, except the 1.1 window (F-MIG-01). The pilot contract requires the old system to stay usable ≥3 months (F-MIG-19) and that the customer signs imports.

## 8. Open questions: which block M0/M1

| Question | Source | Blocks | Default if unanswered |
|---|---|---|---|
| **Does Brutto submit any 2026 a-melding (Option A vs B)?** New; derived from B19 | – | **M0** scope (F-MIG-20/21) | Answered by PLAN D1/B44: Option A, cut over 1.1.2027 (stretch) or to period 2027-02 (plan) |
| Hosting and a second backup location in Norway (Azure Norway West restricted vs a Norwegian provider); § 7-5 vs § 7-7 | K6 Q0; design "Kan backup ligge …", "§ 7-5 eller § 7-7"; fase1 H01/H06 | **M0** (hosting must be chosen before real data; the paragraph question is moot if all data stays in Norway) | Norwegian region + Norwegian backup provider; document an exit plan given Datatilsynet's 1.7.2026 warning on US cloud |
| Architecture defaults: RLS (D03), audit log (D10), login (I01), policy module (I04) | fase1 | **M0** | Adopt the engineering defaults E1–E10 on 2.11.2026 (PLAN §2.1), which replace these fase1 questions |
| Tech lead, and QA of code written by coding agents | design "Teknisk" | **M0** (F-SIK-35 process) | Sjur signs calculation changes; human review of money/access code |
| Legal basis and deadline of the annual summary | K6 Q5; design "Hvilken hjemmel …" | **M1** for mid-year pilots (Option B is not adopted) | Treat as a legal duty, deadline 31.1 |
| Separate "Lønn: helse" role vs the same protection as payroll data | K6 Q2 | **M1** | Same protection + a separate unmask permission (F-SIK-08) |
| Art. 9 legal basis and DPIA for health/union data | design "Juridisk" | **M1** | External advisor before the first pilot |
| Privacy when the customer's agent reads and writes payroll data via MCP (J10) | K6 Q11; design "Juridisk"; fase1 J04/J10 | **M1** (remote MCP with read and draft tools); agent submission LATER | Off by default, masked IDs, no special categories, customer DPIA |
| Who enters migration data without Brutto becoming a regnskapsfører (accountant) | K6 Q3; B4; design "beregningsgaranti" | **M1** (pilot contracts) | Brutto prepares, the customer signs each import; break-glass as procedure |
| BankID broker and price | design "Teknisk"; B14 | **M1** | Get quotes from two brokers now |
| Test data for trekkpålegg and NAV (long lead time) | K6 Q14 | **M1** test readiness | Order now |
| Format for correcting pre-cutover periods (2.3 vs 2.4) | K6 Q4 | No (LATER) | Contract: keep the old system ≥3 months |
| Sluttårsak (end reason) code for method 3 | K6 Q6 | No | Use method 1 |
| API access to Visma, PowerOffice and SD Worx | K6 Q7 | No | Excel template |
| Huma terms, export and retry | K6 Q8 | No, unless a pilot uses Huma | CSV/PAXml |
| Pricing unit and metering | K6 Q10 | No | Invoice pilots manually |
| Auditor access duration | K6 Q13 | No (LATER) | 90 days when built |

Outside these areas but on the M0 critical path: the manual a-melding upload and A07 ordering route in Altinn after Altinn II roles stop on 17.11.2026. Confirm that the uploader holds the Altinn 3 package "A-ordningen" for the M0 employer before the first live upload (period 2027-01 or 2027-02), and "Lønn" for tax cards. For Brutto the 17.11.2026 date only matters if it submits in 2026, which it doesn't (B44); but confirm that the current system can still submit 2026-11 and 2026-12 after 17.11.2026 (PLAN §2.4). The owner is MYN.

## 9. Biggest risks

1. **Employment continuity at the team's own cutover.** A wrong arbeidsforhold-ID, start date or "last change" date, or one period reported from two systems, creates duplicates in Aa-registeret that hit employees' NAV rights. Mitigation: F-MIG-16/17, the cutover fields and a manual A07 check.
2. **The mid-year switch pulls the annual summary and YTD into the December/January critical path**, under a rule whose legal basis is unverified (D-36). Mitigation: Option A, adopted as B44.
3. **Real payroll data reaching language models.** The team works with coding agents and MCP daily. In M0, connecting the production tenant to any LLM client is a new purpose and a likely US transfer. M0 has no MCP at all (PLAN §4). In M1, B41 MCP with personal data needs a customer DPIA. Special categories leak through pay types (sick pay, union dues) even when "health data" is filtered.
4. **Tenant-isolation defects** once pilots (and, from M2, firms) share the database. Mitigation: `tenant_id` and the policy module from the first migration, RLS on before the first external customer (PLAN E7), IDOR tests in CI, a pentest before M1.
5. **Hosting jurisdiction.** Azure is US-owned. Datatilsynet's 1.7.2026 notice warns that US cloud "on European soil" may be affected without a transition period. Backup in Norway depends on Azure Norway West access or a Norwegian provider. If backup ends up in the EU, every customer gets a notification duty.
6. **Platform creep.** B41 "parity in CI" and the PLA partner design (21 LATER functions) can silently consume a 3-person team. PLAN cuts the CI parity test. Hold PLA to the 13 simplified M0/M1 functions; parity comes from the operation catalogue and the generic MCP tools, not hand-built tools.
7. **Liability boundary.** Brutto staff entering migration data, or support touching production data, edges towards regnskapsføring (D-35). Mitigation: the customer signs imports; break-glass as a logged procedure.
8. **Missed trekkpålegg at migration.** The API only works after the first Brutto a-melding, and the employer is liable. Mitigation: a mandatory checklist item and manual 4-eyes entry (F-MIG-25).
