# Minimal API and MCP scope for Brutto (M0 / M1 / M2 / LATER / CUT)

> **Status:** Working paper from the scope review of 29.10.2026. [PLAN.md](../../PLAN.md) is the main plan; where this paper and PLAN.md disagree, PLAN.md wins.
>
> **What it is for:** the detail behind PLAN.md §4 "API and MCP" (B41 narrowed) – what must be right from the first commit, the first operations and MCP tools, human confirmations, privacy limits for MCP, and what waits.

Reviewer: API and MCP. Date: 29.10.2026.
Inputs: `analyse/build/data/design.json` B2, B12, B13, B19, B37, B41, B42, B43 and the `a-api-mcp` architecture section; `analyse/build/data/fase1.json` A01–A06, I01–I04, J01–J13; `analyse/build/data/omr-K6.json` PLA and SIK functions; `analyse/research/R6-api-mcp.md`, `analyse/research/F-arkitektur.md` (§1.6, §1.7, §2, §3.3, §4.8, §5.3), `analyse/research/R2-okosystem.md` (§3.7, §7, §8, §9.2), `analyse/research/R3-kritikk-strategi.md` (E5.9), `analyse/research/S-avklaringer-fra-sally.md` §2–§3; per-function tiers in [`scope.csv`](scope.csv).
Effort figures marked [E] are my estimates, not measurements.

---

## 0. Bottom line

1. **"API first" fits a three-person team if it means "the API is the application layer", not "a developer platform".** Every action is one typed operation in an operation catalog, run through one `dispatch` function. That function does policy, idempotency, audit and masking. REST, the CLI, MCP and later the UI are thin adapters over the catalog. Parity then follows from the structure, and no CI test has to police it. For M0 this is *cheaper* than building a UI first: there is no UI to build. The `brutto` CLI over REST/OpenAPI and an auto-generated API reference page are the M0 "screens" (PLAN.md §1.3). The CI parity test is CUT (PLAN.md §7.2, §8 B41).
2. **B41's platform deliverables do not fit before M1:** developer portal, sandbox with time machine, webhooks, an OAuth 2.1 authorization server with DCR/CIMD, MCP Apps, SDKs beyond TypeScript, a UI-action parity test and automated agent evals. R2-okosystem §8 puts the portal alone at about 3 developer-months. These are LATER or CUT, each with a named trigger (§2).
3. **About ten things must be right from the first commit, because retrofitting them is expensive** (§1). They cost about 1.5–2 developer-weeks [E], and most of that is needed for any backend anyway.
4. **M0 has no MCP at all, not even an optional stdio server, because real payroll data is in the system** (PLAN.md §1.3, §4). The interface is the `brutto` CLI over REST. **M1** adds remote MCP with read tools, draft tools (pay inputs and run drafts) and two generic tools, off by default per tenant (§5). Because of the catalog, adding MCP in M1 needs no retrofit.
5. **In M0 the legal-effect gates sit outside Brutto.** A human uploads the a-melding (the monthly employer report to the tax authority, NAV and SSB) manually as the JSON payload the a-melding API takes (F-MYN-14). The uploader must hold the Altinn 3 package "A-ordningen" for the M0 employer; confirm this before the first live upload (period 2027-01, deadline 5.2.2027, or 2027-02 at the planning date, deadline 5.3.2027). A human signs pain.001 in the bank with BankID (B12). Brutto's own `pay_run.approve` is a human-only operation and needs a fresh re-authentication through the managed identity provider (F-SIK-03). There is no BankID in M0. In M1, actions with legal effect stay human-only operations, now with BankID step-up (F-SIK-03), and agent tokens cannot call them (§3.3). The flow where an agent starts such an action and a human confirms it (F-PLA-37) is LATER.
6. **Privacy, minimal lawful stance:**
   - National identity numbers (fødselsnummer/D-nummer), bank account numbers, protected addresses and GDPR art. 9 data (health from sick-pay pay types, account 5800, NAV refund data, union dues) **never leave via MCP in M1**, and M0 has no MCP. No scope can unlock them. Matching and payment happen server-side, so agents never need them.
   - Salary amounts may go out in M1 (that is B41's point), but every such read is logged. In M0 no payroll data reaches an AI model through Brutto at all: there is no MCP, and coding agents never touch production data (PLAN.md §2.2 D5, §11).
   - M1: MCP is off by default per tenant. A tenant admin turns it on with BankID and accepts an MCP addendum to the data processing agreement (DPA). Brutto writes a reference DPIA for the MCP server before the first pilot turns it on (§4).
7. **Agent-started actions with legal effect are LATER.** In M1, approve, submit, pay, and changes to a bank account or a role are human-only operations; agent tokens can neither call nor start them. Agent tokens are issued by a named human, and there is no OAuth server in M1. Agent-started actions with BankID confirmation (F-PLA-37), agent submission for customers (after the DPIA and an MCP addendum to the DPA), the OAuth server, webhooks and the developer portal are LATER (PLAN.md §4, §9).
8. **Accounting firms are M2** (B45). Firm tools, firm roles and firm confirmations move there. A firm's own payroll can be an M1 pilot as a direct customer.

---

## 1. Must be true from day one (expensive to retrofit)

| # | Must be true | Why retrofitting is expensive | Minimal M0 version | M0 cost [E] |
|---|---|---|---|---|
| D1 | **One application layer with an operation catalog.** Each operation is a Rust type with `META` (id, kind, flags), typed `Input`/`Output`, and `run(ctx, tx, input)`. REST handlers, CLI and MCP only call `dispatch(ctx, op, input)`. No business logic or SQL in handlers. The crate graph enforces it: `brutto-http` cannot depend on `brutto-db`. | Logic that leaks into HTTP handlers is the classic way parity dies. Pulling it out later means rewriting every endpoint, and the MCP tools then drift. | `brutto-app` crate with a `trait Operation` and `dispatch`, and a `cargo deny`/crate-graph check in CI. | 3–4 days |
| D2 | **Stable operation ids** (`pay_run.approve`, `employee.update`). Each id is used as the OpenAPI `operationId`, policy key, audit `handling` value, CLI subcommand, MCP generic-tool argument and (M1) UI action tag. | The id is part of the contract for agents, the audit log and scopes. Renaming it later breaks clients and the history. | Naming convention `resource.verb` in snake_case. Decide J08 now. | in D1 |
| D3 | **Operation metadata drives everything:** `kind` (read, write, job, legal_effect), `human_only`, `requires_confirmation` (LATER, F-PLA-37), `scopes`, `output_data_classes`, `mcp: curated/generic/none`. | Without one declared source, the confirmation list (F-PLA-37), agent limits (F-SIK-31), MCP annotations and masking get spread across code and drift. | A struct literal per operation. `human_only` is enforced already in M0. | in D1 |
| D4 | **An actor context on every call:** `tenant_id`, `actor` (user, agent or system), `on_behalf_of`, `channel` (rest, cli, mcp, ui, job), `auth_strength`, `scopes`, `correlation_id` and an injected `now` (clock). | Adding the agent identity later (F-PLA-32: "Må inn i tilgangsmodellen fra start", must be in the access model from the start, OK-140) means touching every call path. An injected clock keeps calculation deterministic (P1). It also makes the later sandbox time machine (F-PLA-06) almost free. | `Ctx` struct built by auth middleware. Tokens carry `actor_kind`. | 1 day |
| D5 | **One policy module:** `policy::authorize(ctx, meta, resource)`, called inside `dispatch` and never in handlers (I04). Agent tokens are always denied `human_only` operations. | Scattered checks cannot be audited, and agent limits cannot be proved (B13). | Roles in M0: `payroll_admin` and `approver` as code (PLAN.md §1.3). The `agent` actor kind exists and is denied every `human_only` operation, but no agent tokens are issued in M0. Tenant check in the same place. | 1–2 days |
| D6 | **`tenant_id` on every table, and the tenant set per transaction** (`SET LOCAL app.tenant_id`). | Adding a tenant column to a populated schema is a full migration plus a review of every query. RLS (F-SIK-11) can then be switched on in M1 without code changes. | Column and per-transaction setting now. RLS policies in M1, before the second tenant. | 0.5 day |
| D7 | **An append-only audit log written in the same transaction by `dispatch`.** Fields: actor, on behalf of, channel, operation id, resource, before/after or diff, idempotency key, correlation id, and a `hash_prev`/`hash` chain (F-SIK-15, D-Revisjonslogg fields). | Logs that are added afterwards have holes, and a hash chain added later only proves integrity from that point on. Agent accountability ("agent X on behalf of Y", OK-147) needs the log from the first write. | Append-only, with UPDATE and DELETE revoked (PLAN.md E9). The per-tenant hash chain comes later, before ISAE; reserve the columns now. Daily sealing to WORM storage is LATER. | 1–2 days |
| D8 | **Stable errors:** RFC 9457 `problem+json` with a `code` from one Rust error enum (thiserror, A05), an HTTP status, `detail`, and a `fix` hint written for an agent. | Error codes are contract. Agents and integrations branch on them, so changing them breaks clients. | One enum. Codes such as `VALIDATION_FAILED`, `NOT_FOUND`, `STALE_REVISION`, `IDEMPOTENCY_CONFLICT`, `HUMAN_ONLY_OPERATION`, `PAY_RUN_LOCKED`, `HASH_MISMATCH`. | 1 day |
| D9 | **Safe writes:** an `Idempotency-Key` on every non-idempotent POST, stored as (tenant, key, op, request hash, response). A `revision` on mutable resources, with `If-Match` or `expected_revision`. Side effects only through an outbox with a deterministic key (P6, F-arkitektur §1.6). | Clients and agents built without these flows will double-post or overwrite each other's changes. Adding them later is a breaking change. | Table plus checks in `dispatch`. The outbox table exists but has few consumers in M0. | 1–2 days |
| D10 | **Contract conventions that are breaking to change:** `/v1` in the path. Opaque, prefixed ids (`emp_…`, `run_…`) and never fødselsnummer as an id (F-SIK-19). Money as decimal strings (`"41250.00"`), never JSON floats. Periods as `YYYY-MM` and dates as ISO dates. Cursor pagination on every list through one shared `Page<T>`. A `source` and `external_id` on records that integrations will write later. | Each one is a breaking change once a client exists. Offset-to-cursor and float-to-string migrations are notorious. | Shared types in a `brutto-api-types` crate. | 1 day |
| D11 | **OpenAPI 3.1 generated from code** (utoipa 6 + utoipa-axum, A03/J02). The generated `openapi.json` is checked in, CI fails if it is stale, and every PR shows the contract diff. | Hand-written specs drift. A spec added later has to be reverse-engineered from code. | Checked-in spec plus a CI freshness check. Spectral and oasdiff wait until M1. | 1–2 days |
| D12 | **Data-class tags on output fields** (`fnr`, `bank_account`, `address_protected`, `health`, `union`, `salary`), with masking applied in `dispatch` by channel and scope. | Classifying fields after the fact means re-auditing every response type. The tags drive masking, the access log (F-SIK-16) and the J10 limits. | A field attribute plus a masker. M0 has no MCP channel; the tags drive CLI and API masking from M0 and the MCP masks in M1. | 1–2 days |
| D13 | **Environment-prefixed tokens** (`brt_live_…`, `brt_test_…`). Coding agents never get production tokens (D-48, F-SIK-36). | Mix-ups between sandbox and production are a known incident class (F-PLA-06 rule `SANDBOX_KEY_IN_PRODUCTION`). | Prefix check in auth middleware. | 0.5 day |

**Total for D1–D13: about 12–17 developer-days [E].** Roughly half is plumbing any backend needs anyway. The extra cost of doing "API first properly" is about 1–1.5 developer-weeks.

Rust sketch (to give an idea of size, not a design mandate):
```rust
pub trait Operation {
    type Input: DeserializeOwned + utoipa::ToSchema;
    type Output: Serialize + utoipa::ToSchema;
    const META: OpMeta; // id, kind, human_only, scopes, output_classes, mcp
    async fn run(ctx: &Ctx, tx: &mut Tx, input: Self::Input) -> Result<Self::Output, AppError>;
}
pub async fn dispatch<O: Operation>(ctx: &Ctx, input: O::Input, opts: CallOpts) -> Result<O::Output, AppError> {
    policy::authorize(ctx, &O::META)?;               // D5
    let mut tx = db::begin_for_tenant(ctx.tenant).await?;   // D6
    idempotency::check(&mut tx, ctx, &O::META, &opts).await?;  // D9
    let out = O::run(ctx, &mut tx, input).await?;
    audit::append(&mut tx, ctx, &O::META, &out).await?;     // D7
    if opts.dry_run { tx.rollback().await? } else { tx.commit().await? } // dry-run for free (M1)
    Ok(mask::apply(ctx, out))                               // D12
}
```
Note on schemas: utoipa derives `ToSchema`, while rmcp's curated tools use `schemars::JsonSchema`. The generic MCP tools should take their input schema from the generated `openapi.json`, which keeps one source of truth. Curated tools have small hand-written input types with a schemars derive. If keeping two derives in sync becomes painful, switch to `aide` (schemars-based, axum-only, R6 §3). Decide this at A03/J02.

---

## 2. What can wait, and until when

| Item | B41/function ref | Tier | Trigger / when | Interim substitute |
|---|---|---|---|---|
| Paritetstest i CI, with UI actions tagged by operation id (J01) | F-PLA-01, B41 | **CUT** (PLAN.md §7.2, §8 B41) | Parity holds by construction: REST, CLI and (from M1) MCP only call `dispatch`, and the generic MCP tools reach every catalog operation an agent token may call. M1: the UI uses only the generated TS client, and a lint rule bans raw `fetch`. | – |
| OpenAPI lint (Spectral) and breaking-change gate (oasdiff) | J02, F-PLA-02 | **M1** | When the first pilot or integration consumes v1. Freeze v1 then. Before that, breaking changes are free. | PR diff of the checked-in spec |
| Versioning policy, `Deprecation`/`Sunset`, payroll freeze (lønnsfred) in December, January and June | F-PLA-02, J09 | `/v1` path **M0**; written policy **M1** (as a team rule); headers **LATER** | First external partner | – |
| Async job API (`202` + `/v1/jobs/{id}`) | J06, A04 | **M1** | A07 fetch (A07 = the reconciliation report from the a-ordning), tax-card fetch, a-melding API submission and feedback. All need Maskinporten, so none exist in M0. | M0 operations are synchronous (≤10 employees, milliseconds) |
| Dry-run on every write | F-PLA-03 | **M1** | Implemented once in `dispatch` as a rollback. Cheap. | `pay_run.calculate` is itself a preview |
| Batch up to 1,000 lines | F-PLA-03 | **LATER** | First partner with volume | M1 CSV import job |
| Developer portal and guides | F-PLA-05 | Full portal **LATER** (about H2 2027); F-PLA-05 itself is M1 in scope.csv as the reference page | First third party or sister product builds against Brutto | M1: an API reference page (Scalar or Redoc) rendered from `openapi.json`, an error catalog generated from the enum, and `llms.txt`. About 1 day. |
| Self-service sandbox with time machine | F-PLA-06 | **LATER** | First external developer | M1: a `test` environment with a synthetic tenant (F-SIK-36) for pilots and agent tests. The injected clock (D4) makes the later time machine cheap. |
| Conformance test and certification | F-PLA-07 | **CUT** (scope.csv) | Revisit with an app catalog | – |
| App registration, installation, consent, shadow mode | F-PLA-08–12 | **LATER** | First third-party app writing into a customer tenant | Tokens per named user |
| Source registry (kilderegister) and `NOT_SOURCE_OF_TRUTH` | F-PLA-13/14, B2 | **LATER** (field `source` in **M0**) | First data type with two possible writers (Huma or Utleggsappen) | Manual and CSV are the only sources |
| Webhooks and change feed | F-PLA-19 | **LATER** | First partner that needs push (Utleggsappen or Huma status back) | Polling `?updated_since=`. The outbox table from D9 makes a later `GET /v1/events?after=` cheap. |
| Integration monitor, pay calendar API | F-PLA-20/21 | **LATER** | Several live integrations | – |
| Published rate limits and tiers | F-PLA-04 | Simple per-token limit **M1**; published limits **LATER**; paid tiers **CUT** (R2 principle 9) | A runaway agent loop (M1) | `tower-governor`, 429 + `Retry-After` |
| TypeScript client | J11 | **M1** | The first real UI screens are built in M1 | – |
| `brutto` CLI | J11 | **M0** | It is the M0 "UI" | – |
| Python client and other SDKs | J11, R2 §9.2 | **CUT** | A partner asks for one and will co-maintain it | OpenAPI + any generator |
| Postman or Bruno collection | F-PLA-05 | **LATER** | Portal | Generated in minutes when needed |
| **MCP read tools** | F-PLA-33 | **M1** remote. **None in M0**: no MCP while real payroll data is in the system (PLAN.md §4) | When the draft tools are cut, read-only MCP stays (PLAN.md §6.3). Zero retrofit cost thanks to D1–D3. | CLI |
| **MCP draft tools** (pay inputs and run drafts; no legal effect) | F-PLA-33, B41 | **M1**, opt-in per tenant. First item on the M1 cut order (PLAN.md §6.3) | – | CLI |
| **MCP legal-effect starts** (request approval, a-melding submit for an approved run) | F-PLA-37, J05 | **LATER** (F-PLA-37 is LATER in scope.csv). In M1 these are human-only operations that agent tokens cannot call or start | Partner or customer demand, and the DPIA done (PLAN.md §9). Agent submission for customers also needs the MCP addendum to the DPA. a-melding submission needs Maskinporten and a system user (gate MP: 31.3.2027, best case 29.1.2027) | A human uses the UI or CLI, with BankID step-up in M1 |
| Remote MCP endpoint (`/mcp`, Streamable HTTP) | F-PLA-33 | **M1** (bearer agent token issued by a named human) | It is the M1 MCP transport | – |
| OAuth 2.1 for MCP: Protected Resource Metadata (RFC 9728), audience/resource check (RFC 8707), external authorization server with CIMD + DCR | J04, R6 §1–§2, §7.2 | **LATER**. No OAuth server in M1 (PLAN.md §4) | A customer needs claude.ai, ChatGPT or Copilot hosted connectors, or a directory listing. Brutto builds only the resource-server side in axum. The authorization server is bought or self-hosted (e.g. Keycloak in a Norway region, or an IdP with both CIMD and DCR; verify CIMD support). About 2–3 developer-weeks plus a security review [E]. | Agent token issued by a named human (F-PLA-32). Claude Code and Cursor accept static `Authorization` headers for remote HTTP servers. Whether claude.ai web custom connectors accept static headers: (verify). |
| URL-mode elicitation for confirmations | F-PLA-37, R6 §1 | **LATER** | The spec marks the design as still changing, and the confirmation flow itself is LATER | In M0 and M1 an agent calling a human-only operation gets `HUMAN_ONLY_OPERATION`, and the human does it in the UI or CLI |
| MCP Tasks extension | J06, R6 §1 | **LATER** | Client support is confirmed | Start tool plus status tool with a handle |
| MCP Apps (charts in chat) | R6 §7.10 | **CUT** | A customer asks | Chart numbers via `brutto_api_read` |
| Claude directory listing | R6 §4 | **LATER** | Needs OAuth. Brutto never moves money (B12), so the money-transfer rule should not block it (verify). | – |
| Agent eval suite (J12) | J12 | **M1 lite** (10 tasks run by hand before each pilot onboarding); automated in CI **LATER** | – | – |
| Built-in Brutto assistant | F-PLA-36, X02 | **LATER** | After X02, and after the core is stable (B13, critic) | Customer's own agent via MCP |
| Usage metering | F-PLA-35 | **LATER** | Billing | Manual |
| MCP documentation server | R2 §8 #15 | **CUT** | – | `llms.txt` |

---

## 3. Is "API first" compatible with a three-person team shipping M0 in weeks?

**Yes, with two conditions.**
- **(a) API first means structure, not platform.** The operation catalog and `dispatch` from §1 are the API. Everything in §2 is packaging and waits.
- **(b) M0 has no custom UI and no MCP.** The M0 operator is the founder running his own payroll for at most 10 people. A CLI and an auto-generated reference page are enough. The shadow runs for November and December 2026 (B19 reworded, B44) compare figures to the øre, and CLI tables and CSV diffs do that better than screens.

The real risk to M0 is the payroll domain, not the API, as long as the API work stays at about 3–4 developer-weeks in total (§1 plus the CLI and the managed login).

Calendar check (PLAN.md §1.2, §3): the current system submits all of income year 2026, so there is no November a-melding deadline for Brutto. The calculation core must be ready for the engine spike (27.11.2026) and shadow #1 (18.12.2026, latest 31.12.2026). M0 is about 20–31 developer-weeks (5–8 developer-months). The decision on 15.1.2027 is for period 2027-01, which is a stretch (about 40 %); the planning date is 2027-02 (about 65 %). API work must stay a small share of that.

### 3.1 M0 shape (own payroll, internal)

```
crates/
  brutto-domain     pure calculation engine, no IO, no clock (P1)
  brutto-app        operation catalog, dispatch, policy, audit, idempotency, masking
  brutto-db         sqlx/Postgres, tenant per transaction, outbox table
  brutto-api-types  request/response DTOs (serde + utoipa::ToSchema)
  brutto-http       axum REST adapter, utoipa-axum → openapi.json (checked in), Scalar page
  brutto-cli        clap + reqwest using brutto-api-types:
                      `brutto login`   OIDC device flow against the managed identity provider
                      typed commands for the ~15 M0 operations
                      `brutto call <operation_id> --json @file`   (generic, any operation)
```
- **Auth: managed OIDC login with MFA and a CLI device flow** (PLAN.md §1.3, F-SIK-01). No BankID in M0.
  - Each person has a personal account in a managed identity provider (for example Entra ID, since hosting is Azure), with MFA. Personal accounts only.
  - The CLI logs in with the OAuth 2.0 device authorization flow against that provider and calls the API with the person's token. Brutto is a resource server only; it runs no authorization server.
  - Personal tokens for scripts, if needed: format `brt_live_<32 random bytes>`, with a SHA-256 hash stored server-side. Fields: user, tenant, `actor_kind` (always human in M0), scopes, `expires_at` (≤90 days), `last_used_at`. `token.create` is a human-only operation.
  - M0 scopes are coarse: `read`, `draft`, `approve` (human only), `admin` (human only).
  - `pay_run.approve` and `employee.set_bank_account` also need a fresh re-authentication through the identity provider (`max_age` / `prompt=login`, F-SIK-03). A token alone is not enough.
  - No agent tokens are issued in M0. Coding agents never get production tokens (D13).
- **No MCP in M0** (PLAN.md §4): no MCP while real payroll data is in the system. The M1 design is ready in the catalog:
  - The MCP server is a client of the same API (B41 "MCP-serveren er en klient av det samme API-et"). It only calls `dispatch`, so parity follows.
  - Pin the rmcp version when it is built: there were three major versions in five months (R6 §2). Keep rmcp confined to one adapter crate, so churn never touches the core.
- **Human approval in M0:**
  - Sjur, or the named approver who is not the preparer, runs `brutto payrun approve run_… --expect-hash <h>` after a fresh re-authentication through the identity provider.
  - Any token with `actor_kind = agent` gets `HUMAN_ONLY_OPERATION`; none is issued in M0.
  - This is a procedural guarantee. Human tokens must never sit in an environment an agent can read (D-48).
  - The legally binding gates are external: the manual a-melding upload (F-MYN-14), and BankID in the bank for pain.001 (B12).
  - Sjur approving his own salary conflicts with F-SIK-12. Record a F-SIK-13-style exception: a one-person payroll with a compensating report to a second team member or the board chair (PLAN.md D11).
- **Lanes after approval** (B43): manual `track.mark` calls record "a-melding uploaded manually, receipt ref …" and "payment signed in bank".

### 3.2 M1 shape (pilots: 3–5 direct customers; firm clients are M2)

- **UI.** The first real screens use a TypeScript client generated from `openapi.json`. They include the BankID login and step-up (I01: broker such as Criipto/Idura or Signicat). Server-side session cookie for the UI (I03). Personal and agent tokens for the API; no OAuth server (PLAN.md §4).
- **Remote MCP.** Read tools, draft tools (pay inputs and run drafts) and two generic tools (§5); off by default per tenant. `/mcp` uses Streamable HTTP in the same binary, with bearer agent tokens. It validates `Origin` (spec MUST). It forwards to the REST layer over loopback or calls `dispatch` in-process, but the resource server is the same, so there is no token passthrough to a third party.
- **Agent tokens are issued by a named human.** Creating an agent token, or enabling MCP for a tenant, is a human-only operation with BankID step-up by a tenant admin (OK-149, F-SIK-03, F-PLA-32). Agent tokens carry read or draft scope only and can never approve or confirm.
- **Scopes refined per domain:** `employees:read`, `employees:write`, `payroll:read`, `payroll:draft`, `a07:read`, `a07:fetch`, `amelding:submit`, `audit:read`. No wildcards (R6 §6). Agent tokens get only read scopes and `payroll:draft`; `employees:write` and `amelding:submit` are for humans. M2: for accounting firms (byrå), a token binds one user, and cross-client reads return metadata only (OK-148, F-SIK-06).
- **OAuth 2.1:** LATER, not in M1 (PLAN.md §4; see §2).
- **Hygiene added:** Spectral and oasdiff, RLS switched on, the access log (F-SIK-16) for reads of salary data, a per-token rate limit, and dry-run.

### 3.3 Actions with legal effect in M1: human-only (the F-PLA-37 confirmation flow is LATER)

In M1 there is no agent-started confirmation flow. Actions with legal effect are human-only operations in the catalog (`human_only = true`). An agent token that calls one gets `HUMAN_ONLY_OPERATION` and cannot start it either. A human performs the action in the UI or CLI with BankID step-up (F-SIK-03). Because nothing waits for confirmation, M1 needs no storage for pending confirmations (data-model.md §10).

**LATER design (F-PLA-37), kept so the metadata in D3 is ready.** When partner or customer demand arrives and the DPIA is done (PLAN.md §9), there is one mechanism, modelled on the fields of the mapped `D-Godkjenning` entity (`objektVersjonHash`, `sterkAutentisering`, `metode`, `frist`, `dyplenke`). It then needs one small table for pending confirmations:
1. An operation marked `requires_confirmation` creates a confirmation with the operation id, input hash, preview, requester (agent on behalf of a user) and expiry.
2. The API or MCP returns `202` with `status: awaiting_confirmation` and a `confirm_url`. The URL contains no personal data.
3. A human with the right role opens the URL in the Brutto UI and does a BankID step-up (check `acr`). Segregation-of-duties rules apply as in the UI (F-SIK-12/13).
4. Execution re-checks the hash. If the content changed, the confirmation expires.
5. Agents can read the status but can never confirm.

**M1 list:**

| Action | M1 rule |
|---|---|
| Pay inputs and run drafts | Agents may create and change them with draft scope (the MCP draft tools). A draft has no legal effect until a human approves the run. |
| Approve a pay run | Human only, BankID step-up. Approval locks the a-melding and pain.001 with a hash. |
| Submit an a-melding for an approved run | Human only, BankID step-up. The gateway sends only if the hash matches. Exists only once Maskinporten is live (gate MP: 31.3.2027, best case 29.1.2027). Agent submission (J05, founder 29.10.2026) is **LATER**: first agent-started with human confirmation (F-PLA-37), and for customers only after the DPIA and the MCP addendum to the DPA. |
| Corrections or replacement messages not based on an approved run | Human only, BankID step-up |
| Change of bank account | Human only. An admin with BankID step-up and four eyes (PLAN.md §6.2); the employee portal is LATER. Never via MCP. |
| Roles, access, segregation-of-duties exceptions, agent tokens, enabling MCP | Human only, BankID step-up |
| Bulk export of personal data, including downloads of the a-melding JSON and pain.001 (both contain fødselsnummer or account numbers) | Human only. BankID step-up in M1 (F-SIK-03). |
| Payment and payment file | **Simplification:** no separate Brutto confirmation. The file is derived from the approved, hash-locked run, and the bank requires BankID signing (B12). The approval screen shows count, sum and hash (B12 critic). A changed file means a new approval. |
| Ordering tax cards | **Simplification:** a system job for active employments, not something an agent starts. That keeps it off this list. |
| System user (systembruker) and powers of attorney (fullmakter) | Confirmed in Altinn (external). |
| **M2:** firm actions – recorded customer approval (F-BYR-26), who presses pay (F-BYR-27), firm role grants per client (F-BYR-03), agent system user and client linking (F-MYN-04, F-MYN-05) | Decided with M2 (B45). Not in M1. |

---

## 4. Privacy constraints for MCP access (J10, DPIA)

### M0: internal use, own employees, the M0 employer (PLAN.md D2) as controller

M0 has no MCP, so no payroll data reaches an AI model through Brutto in M0 (PLAN.md §4, §11). The exclusions below are still built into the data-class tags and masking from M0 (D12), so they are in place when MCP arrives in M1.

1. **Server-side exclusion, not configuration.** MCP output never contains:
   - fødselsnummer or D-nummer (`fnr` class)
   - bank account numbers
   - addresses
   - art. 9 data: sick-pay pay types 2018/2019, account 5800, union dues (fagforeningstrekk) lines.

   Restricted payslip lines appear as `"restricted": true` with the amount withheld. Totals per run (gross, forskuddstrekk = tax withholding, AGA = employer's social security contribution, feriepenger = holiday pay, net) are allowed.
2. **Before any production data reaches MCP (not in M0), the LLM runs under commercial terms only:** a DPA, no training on data, and a documented transfer basis for any non-EEA processing (verify the provider's terms). Claude via an EU region (Bedrock or Vertex, F-arkitektur §5.3) is preferred.
3. **Before any production data reaches MCP (not in M0), the employees are told in writing** (GDPR art. 13) that payroll data may be processed by an AI agent the employer uses. In M0, record a one-page DPIA screening and an art. 30 record entry for own employees (F-SIK-28). Full DPIA in M1.
4. **Every MCP call (from M1) is audited** with channel `mcp`, the agent flag, the operation id and masked arguments (D7).
5. **Coding agents get no production tokens, and no production DB or log access** (D-48, F-SIK-31). Development uses the `brt_test_` tenant with synthetic data (F-SIK-36).

### M1: external pilots, Brutto as processor (sub-processor via a byrå only from M2)
1. **MCP is off by default per tenant.** A tenant admin turns it on with BankID step-up (OK-149). They accept an **MCP addendum to the DPA** (F-SIK-27). It states that the customer chooses the agent and LLM, that the customer's own DPA with that provider covers onward processing, and that Brutto's processing ends when it returns data to the customer-authorised client.
2. **Brutto writes a reference DPIA for the MCP server, plus an MCP section in the customer DPIA template** (F-SIK-28), before the first pilot turns MCP on. Have an external adviser review it together with the open art. 9 question (design.json open question "Behandlingsgrunnlag og DPIA", legal basis and DPIA).
3. **Fødselsnummer, bank account and protected address are never available via MCP in M1, with no scope to unlock them.** This is simpler than J10's "separate scope" proposal. Person matching against A07 runs server-side (F-PLA-17), so agents never need them. Revisit with an `identity:read` scope LATER, only for a concrete use case.
4. **Art. 9 data never goes out via MCP in M1**, and neither do per-person aggregates that reveal it. Deviation explanations refer to "a restricted line, see Brutto".
5. **Salary data goes out with `payroll:read`.** Each MCP read of individual salary is logged in the access log (F-SIK-16) as one event with a record count.
6. **Free text from integrations or employees is wrapped as untrusted data** in tool results (OK-146). No MCP tool sends data out of Brutto: no email, webhook or export-to-URL (R6 §6, lethal trifecta).
7. **A per-token quota** limits mass extraction. Bulk exports are human-only (§3.3), so MCP cannot be used as an export channel.
8. **Byrå agents (M2):** one user per token, client-scoped calls only where the user has an assignment, and metadata-only portfolio reads (OK-148).

---

## 5. First API operations (M0) and first MCP tools

JSON uses snake_case and paths use kebab-case plurals. Actions are sub-paths (`/approve`), not colon verbs (`{id}:approve` as in F-PLA-06), to keep axum routing and client generation simple. Names follow J08 (§6).

| # | Operation id(s) | REST | Kind | MCP exposure (M1; there is no MCP in M0) |
|---|---|---|---|---|
| 1 | `employer.get`, `employer.update` (opplysningspliktig = the legal entity that reports, with its `units` = virksomhet/sub-unit, AGA zone and calculation code, and payer bank account) | `GET/PATCH /v1/employers/{id}` | read / write | read (generic); update none |
| 2 | `employee.list` | `GET /v1/employees?employer_id&status&cursor` | read | curated |
| 3 | `employee.get` (person + employments (arbeidsforhold) + tax-card summary, masked) | `GET /v1/employees/{id}` | read | curated |
| 4 | `employee.create`, `employee.update` (`If-Match`; excludes bank account and fnr changes) | `POST /v1/employees`, `PATCH /v1/employees/{id}` | write | none in M1: agent writes are limited to pay inputs and run drafts (PLAN.md §4). LATER |
| 5 | `employee.set_bank_account` | `PUT /v1/employees/{id}/bank-account` | write, **human_only** | none |
| 6 | `tax_card.set` (manual, four eyes: table number, percentage or frikort = tax-free card; year; source) | `PUT /v1/employees/{id}/tax-cards/{year}` | write | none (calculation-critical, four eyes) |
| 7 | `pay_type.list` (the 8–12 signed pay types in M0, PLAN.md §1.3; the 26 standard types in M1, S §6 pkt. 25) | `GET /v1/pay-types` | read | generic read |
| 8 | `opening_balance.import` (opening state per employee: year-to-date if go-live is after January; the 2026 holiday-pay basis on the M0+ track by JUN27, F-MIG-22. No 2026 year-to-date import and no 2026 sammenstillingsoppgave from Brutto, B44) | `POST /v1/employers/{id}/opening-balances` | write | none (CLI/CSV) |
| 9 | `pay_run.create` (period, pay date; prefilled with fixed salaries) | `POST /v1/pay-runs` | write (Idempotency-Key) | curated (`prepare`) |
| 10 | `pay_run.upsert_lines` (full state per employee, `external_id`, `source`) | `PUT /v1/pay-runs/{id}/lines` | write | curated (`prepare`) |
| 11 | `pay_run.calculate` (synchronous; results + controls) | `POST /v1/pay-runs/{id}/calculate` | write (recompute) | curated (`prepare`) |
| 12 | `pay_run.get`, `payslip.get` (JSON, or PDF via `Accept`), `pay_run.explain` (calculation trace per line, P7) | `GET /v1/pay-runs/{id}`, `…/payslips/{employee_id}`, `…/lines/{line_id}/explanation` | read | curated |
| 13 | `pay_run.approve` (expected hash; fresh re-authentication through the identity provider; locks; generates payslips, pain.001, voucher CSV, a-melding JSON) and `pay_run.discard` | `POST /v1/pay-runs/{id}/approve`, `…/discard` | **legal_effect, human_only** | none (refused) |
| 14 | `pay_run.compare` (upload the existing system's results; diff to the øre, B16/B19) | `POST /v1/pay-runs/{id}/comparisons` | write (stores the diff) | curated read of stored diffs |
| 15 | `artifact.download` (`amelding_json` for manual upload, `pain001`, `payslips_zip`: human_only because they contain fnr or accounts; `voucher_csv`: allowed, net is posted in aggregate on 2930, S §2 pkt. 9) and `track.mark` (B43 lanes: uploaded manually + receipt ref, paid in bank) | `GET /v1/pay-runs/{id}/artifacts/{kind}`, `POST /v1/pay-runs/{id}/tracks/{lane}/events` | read / write | voucher: generic; others none |
| meta | `operation.list` (the catalog), `audit_event.list`, `token.create`/`token.revoke` (human_only), `me.get` | `GET /v1/operations`, `GET /v1/audit-events`, `POST/DELETE /v1/tokens` | read / admin | catalog search runs as `operation.list` through `brutto_api_read` |

**MCP tools.** Each has a `title`, `readOnlyHint` or `destructiveHint`, `structuredContent` with an `outputSchema`, and `response_format` short or detailed. There is no MCP in M0. M1 is remote, off by default per tenant, with read tools, draft tools and two generic tools.

There are **two generic tools**, as in PLAN.md §4: `brutto_api_read` and `brutto_api_write`. Searching the catalog is the read operation `operation.list`, so it runs through `brutto_api_read` and needs no separate find tool. The read/write split stays, because Claude's directory rejects one tool that does both (R6 §2).

| Tool | Hint | Tier | What it does |
|---|---|---|---|
| `brutto_employees_search` | read | M1 | Employees with employment status, salary basis and tax-card type (masked) |
| `brutto_employee_get` | read | M1 | One employee with employments and history |
| `brutto_payrun_get` | read | M1 | Run status and lanes, totals (gross, forskuddstrekk, AGA per zone, feriepenger accrual, net), and controls |
| `brutto_payrun_explain` | read | M1 | Calculation trace for one employee or line |
| `brutto_payrun_compare` | read | M1 | Diff against the reference system's result, per employee and pay type |
| `brutto_api_read` | read | M1 | Runs any `kind=read` operation, including `operation.list` to find operation ids and input schemas |
| `brutto_payrun_prepare` | write (not destructive) | M1 (draft tool; first on the M1 cut order) | Create the draft or upsert pay inputs, then recalculate, in one call. This follows the consolidation advice in R6 §4. |
| `brutto_api_write` | destructive | M1 (draft scope) | Runs any write operation an agent token may call: pay inputs and run drafts (`mcp: generic`, not human_only, no legal effect). Human-only operations return `HUMAN_ONLY_OPERATION` (§3.3). |

**M1 also adds read tools** (`scope.csv` F-PLA-33 says about 10 curated tools plus the 2 generic ones, so consolidate where possible):
- `brutto_a07_get` (the latest A07 fetched by a human or a system job) and `brutto_job_status`
- `brutto_reconciliation_get` (payroll ↔ a-melding ↔ A07, F-REG-25, F-RAP-15). The general-ledger leg and F-REG-30 are LATER, a separate product line (B46).
- `brutto_deviations` (list and explain)
- `brutto_amelding_status`

**LATER:** `brutto_employee_update` and `brutto_deviation_resolve` (agent writes beyond pay inputs and run drafts), and `brutto_payrun_request_approval` and `brutto_amelding_submit` (agent-started actions with legal effect; a human confirms with BankID, F-PLA-37, §3.3).

**M2 adds:** `brutto_clients_list` (byrå, metadata only).

---

## 6. Recommended answers to the fase1.json questions (API/MCP/security)

| Q | Recommendation | Tier |
|---|---|---|
| A01 | Modular monolith: one server binary (API, background jobs added at M1) plus the CLI binary | M0 |
| A02 | axum + tokio + tower | M0 |
| A03 | REST + OpenAPI 3.1 from code (utoipa 6 / utoipa-axum) | M0 |
| A04 | Postgres queue (`SKIP LOCKED`) + outbox. Outbox table in M0, workers in M1. | M0/M1 |
| A05 | thiserror in the domain, one public error enum → problem+json with stable codes and `fix` hints | M0 |
| A06 | Secrets in a managed vault. M0 may use the host's secret store, never the repo. | M0 |
| I01 | M0: no login UI; managed OIDC login (e.g. Entra ID) with MFA and a CLI device flow, personal accounts only, re-authentication through the identity provider on approval and bank-account change. M1: BankID via a broker for login and step-up. | M0/M1 |
| I02 | M0: payroll admin and approver as code (PLAN.md §1.3); the agent actor kind exists but no agent tokens are issued. M1: customer admin, payroll manager, approver, read-only, agent modifier (auditor access is LATER, F-SIK-09). M2: byrå admin, byrå payroll consultant. Break-glass support is M1 (F-SIK-10, PLAN.md §6.2). | M0/M1/M2 |
| I03 | Server-side session cookie for the UI (M1). Tokens for the API. | M1 |
| I04 | One policy module inside `dispatch` (M0). RLS as a backstop (M1, before the second tenant). | M0/M1 |
| J01 | Structural parity via the catalog (M0) plus UI-only-via-generated-client lint (M1). The CI parity test is CUT. | M0/M1 |
| J02 | Code first, spec checked in, CI freshness check (M0). Spectral + oasdiff at the v1 freeze (M1). | M0/M1 |
| J03 | Curated workflow tools plus **two** generic tools (read, write); catalog search is `operation.list` through read. M0: no MCP. M1: remote, read tools and draft tools (pay inputs and run drafts). | M1 |
| J04 | M0: human tokens only, via the CLI device flow; no agent tokens. M1: agent tokens issued by a named human behind BankID step-up; no OAuth server. OAuth 2.1 resource server plus external authorization server LATER on a trigger. Byrå night jobs (M2) use a token tied to a responsible person, the same mechanism. | M0/M1/M2/LATER |
| J05 | Section 3.3. M0 relies on re-authentication through the identity provider for approval, the manual a-melding upload and bank BankID. M1: actions with legal effect are human-only operations with BankID step-up; agents cannot call or start them. Agent-started actions with human confirmation (F-PLA-37) and agent submission for customers LATER. | M0/M1/LATER |
| J06 | Generic `jobs` resource; an MCP status tool. Agent-started jobs with legal effect and the Tasks extension LATER. | M1 |
| J07 | M0: cursor pagination, Idempotency-Key, revision/If-Match, problem+json. M1: dry-run. LATER: examples for every operation (only MCP-exposed operations in M1). | M0/M1 |
| J08 | **Decide now.** English for structure and every concept with a precise English term (employee, employment, pay_run, payslip, tax_card, holiday_pay, tax_withholding, employer, unit). Norwegian only for names of government artefacts without an equivalent (`a_melding`, `a07`, `aga`). An `x-no` glossary extension on each schema. One lint rule. | M0 |
| J09 | `/v1` path (M0). Deprecation policy and lønnsfred when the first external client exists (M1 rule, headers LATER). | M0/M1 |
| J10 | Section 4. No MCP in M0. Never fnr, bank account or art. 9 via MCP in M1. Salary allowed and access-logged. MCP opt-in per tenant with BankID. | M0/M1 |
| J11 | CLI (M0, hand-written thin plus generic `call`), TS client (M1, generated), Python CUT | M0/M1/CUT |
| J12 | 10 hand-run agent tasks before each pilot onboarding (M1). Automated suite LATER. | M1/LATER |
| J13 | Cut from MVP: developer portal, sandbox time machine, webhooks, OAuth authorization server, MCP Apps, URL elicitation, Tasks, SDKs except TS, rate-limit tiers, automated agent evals, CI parity test, agent-started actions with legal effect (F-PLA-37), agent submission for customers | – |

---

## 7. Tiering of the API/MCP-related function ids

The tier column is the tier in [`scope.csv`](scope.csv), which is the source of truth per function. The note says what is built earlier, as PLAN.md §2.1 (E7–E9) and §4 require.

| Function | Tier (scope.csv) | Note |
|---|---|---|
| F-PLA-01 Public REST API used by own modules | **M0** (catalog, dispatch, OpenAPI) | Swap test and module-as-app parts LATER |
| F-PLA-02 Versioning, deprecation, lønnsfred | **M1** (policy) | `/v1` path from M0 (PLAN.md E8); headers LATER |
| F-PLA-03 Idempotency, batch, dry-run, reason codes | **M1** | Idempotency keys and problem+json codes from M0 (PLAN.md E8); dry-run M1 (scope.csv: imports and pay input only); batch LATER |
| F-PLA-04 Published rate limits | **LATER** | Simple per-token limit as M1 hygiene |
| F-PLA-05 Developer portal | **M1** (reference page, quick-start, `llms.txt`) | Full portal LATER (PLAN.md §9) |
| F-PLA-06 Sandbox with time machine | **LATER** | M1: test tenant; injected clock now |
| F-PLA-07 Conformance and certification | **CUT** | |
| F-PLA-08–12 Apps, installation, consent, shadow mode | **LATER** | Tokens per named user until then |
| F-PLA-13/14 Source registry | **LATER** (`source` field in M0) | |
| F-PLA-17 Person matching | **M1** (server-side, for A07) | |
| F-PLA-19 Webhooks | **LATER** | |
| F-PLA-32 Agent identity and agent package | **M1** | The actor context with `actor_kind` and `on_behalf_of`, and the audit, are built from M0 (PLAN.md E8). Agent tokens are issued by a named human, with read or draft scope only; no OAuth server in M1 |
| F-PLA-33 MCP server | **M1** remote: read tools, draft tools (pay inputs and run drafts), two generic tools; off by default per tenant | M0: none (no MCP while real payroll data is in the system). Legal-effect actions are human-only. OAuth LATER |
| F-PLA-36 Built-in assistant | **LATER** | |
| F-PLA-37 Confirmation of actions started via API/MCP | **LATER** | M0 and M1: the `human_only` flag; agents can neither call nor start legal-effect operations (§3.3). No pending-confirmation storage until then (data-model.md §10) |
| F-SIK-01 Login | **M0**: managed OIDC login (e.g. Entra ID) with MFA and a CLI device flow, personal accounts only | **M1**: BankID via a broker for customer users and approvers |
| F-SIK-03 Step-up | **M0**: re-authentication through the identity provider on approval and bank-account change | **M1**: BankID step-up |
| F-SIK-11 Tenant isolation | **M0** | Column + per-transaction tenant from the first migration; RLS on before the first external customer (PLAN.md E7); IDOR test suite M1 |
| F-SIK-15 Audit log | **M0** | Append-only from the first migration (PLAN.md E9); hash chain before ISAE, daily sealing LATER |
| F-SIK-16 Access log | **M1** | M0: sensitive reads in the audit log (no MCP in M0) |
| F-SIK-19 Field encryption and masking | **M0** | Field encryption with one key and a blind index for national ID and account numbers from day one (PLAN.md E9); per-tenant keys M1 (PLAN.md §6.2). Masking by data class from M0 |
| F-SIK-27/28 DPA and DPIA | **M1**: DPA with MCP addendum + reference DPIA | M0: screening + art. 30 record |
| F-SIK-31 Agent limits and AI policy | **M1** | The hard limits (agents never approve or confirm) are enforced in the policy module from M0 |
| F-BYR-01, -02, -03, -10, -12, -19, -26, -27, F-MYN-04, F-MYN-05 (firm entity, clients, roles, work queue, approvals, agent system user) | **M2** (B45) | Not in M1. The other F-BYR functions are LATER or CUT |

---

## 8. Effort and risks

**Effort [E]:**
- M0 API platform: about 3–4 developer-weeks in total.
  - D1–D13: 2.5–3.5 weeks.
  - CLI: about 3 days.
  - Managed OIDC login and the CLI device flow: part of PLAN.md's 0.5–1 developer-week for login and roles (§1.3).
  - No MCP.
- M1 increment: about 4–5 developer-weeks.
  - Jobs API: 1 week.
  - Scopes, access log and RLS: 1.5 weeks.
  - Remote MCP with read tools, and agent tokens issued by a human: 0.5–1 week.
  - TS client, docs page, Spectral/oasdiff: 0.5 week.
  - Draft tools: 0.5–1 week.
- Deferred:
  - Confirmation flow for agent-started actions (F-PLA-37): about 2 weeks.
  - OAuth authorization server: +2–3 weeks.
  - Portal: about 3 developer-months (R2 §8).
  - Sandbox with time machine: the largest DX item.

**Risks:**
- rmcp churn, mitigated by pinning and confining it to one adapter crate.
- Schema drift between utoipa and schemars, mitigated by generating generic tool schemas from `openapi.json`.
- "Best API in the industry" ambition pulling platform work into M0. Hold the line with §2's triggers.
- Agent-started a-melding submission is LATER (F-PLA-37), and agent submission for customers also needs the DPIA. In M1 a human submits with BankID, once Maskinporten and the system user are live (gate MP: 31.3.2027, best case 29.1.2027). B41's flagship example (the agent submits on its own) is LATER.
- In M0, the human-only guarantee rests on there being no agent tokens and no MCP, plus re-authentication through the identity provider on approval. It is acceptable because the binding gates are the manual a-melding upload and BankID in the bank.

## 9. Proposed changes to record

Items 1, 2 and 4 are reflected in PLAN.md §4 and §8 (B41 narrowed).

1. **B41:** define "API first" for M0/M1 as structural parity through the operation catalog and `dispatch`. Drop the CI parity test (CUT). Platform deliverables become LATER with triggers. Agent-started actions with legal effect and agent submission for customers are LATER, after the DPIA.
2. **F-PLA-33:** no MCP in M0. Remote MCP with read tools, draft tools (pay inputs and run drafts) and two generic tools (read, write) is M1. OAuth 2.1 is LATER.
3. **F-PLA-37:** LATER (scope.csv). In M1, actions with legal effect are human-only operations. When the flow is built, its list is simplified: the payment file is covered by the run approval plus bank BankID, tax-card ordering is a system job, downloads of the a-melding JSON and pain.001 are human-only exports, and firm confirmations move to M2.
4. **J10:** fnr, bank account, protected address and art. 9 data are never available via MCP in M1 (M0 has no MCP), with no scope to unlock them.
5. **J08:** decide the naming rule now (English plus `a_melding`/`a07`/`aga`, with a glossary). It is the one API decision that cannot wait.
