# Prototype stack: Python first, Rust after proof of concept

**Date:** 29.10.2026 · **Status:** proposal. Backs B47, B48 and D13 in [PLAN.md](../../PLAN.md). Where this paper and PLAN.md disagree, PLAN.md wins.

**How it was made:** four research agents compared a Python stack, a TypeScript stack, the authorities' tooling and the path to Rust.

## 1. What Sjur decided (29.10.2026)
- Sjur builds the MVP and demo himself, with coding agents.
- The team rewrites it in Rust once the proof of concept holds. Rust stays the target (B8).
- The prototype runs on localhost, with no hosting.

## 2. Open: how the prototype fits the Rust plan (D13)
PLAN.md §1.2 has Peter and Sander start Rust code on 2.11. There are two readings:
- **(a) The prototype is M0.**
  - Sjur builds the shadow core in Python.
  - Rust starts once both shadows are clean, and ports against the same golden cases, migrations and API contract.
  - The prototype must then meet E5–E9 and the M0 exit criteria (§1.7).
  - It also moves off localhost before it becomes system of record (B48).
- **(b) The prototype runs beside a Rust M0.**
  - Peter and Sander build M0 in Rust as planned.
  - Sjur's prototype is the demo and the executable spec.

Either way, the pieces in §4 are shared between the two builds.

## 3. Recommendation: Python backend, Postgres, React for the demo
Why Python rather than TypeScript:
- `Decimal` is built in and maps straight to `NUMERIC` (E5). TypeScript drivers return `int8` and `numeric` as strings, and `JSON.stringify` throws on `bigint`.
- lxml validates against the XSD out of the box, for the XML 2.3 fallback.
- Typst has Python bindings, so the same payslip template runs in Rust.
- PyO3 converts `Decimal` to `rust_decimal`, if parts are ever ported one at a time.
- The repo already runs Python.

TypeScript also works. Pick it only to have one language from front to back.

| Layer | Prototype | Rust (E2–E9) |
|---|---|---|
| Tooling | uv, ruff, pyright (strict), pytest, hypothesis, testcontainers | cargo, clippy |
| API | FastAPI and Pydantic v2 with `extra="forbid"`. Each `operation_id` is the operation-catalogue id (E8) | axum and utoipa |
| Contract | `openapi.json` generated from code and committed (E3). oasdiff in CI. Hurl tests that run against any base URL | The same Hurl tests. utoipa output diffed against the committed file |
| Database | Postgres, the same major version as the Azure target (E4). Plain-SQL migrations in the sqlx-cli layout (`migrations/<version>_<name>.sql`). Raw SQL, one query per file. **No ORM** | `sqlx::migrate!` on the same files; `query_file_as!` |
| Money | `NUMERIC` and `Decimal`. Decimal strings in JSON. One named rounding function per legal rule (§1.4) | `rust_decimal` |
| Withholding | `float` in the Java order of operations. Java's `Math.round` breaks ties toward positive infinity, which in practice is `math.floor(x + 0.5)`. Never `round()`. 100 % match on the table file | `f64` in the isolated crate (E5) |
| a-melding | One format-neutral aggregate. JSON for the manual upload [verify the format by 27.11]. XML 2.3 via lxml with XSD validation as the fallback | serde. The XML fallback needs libxml2, through the `libxml` crate or `xmllint` in CI |
| Payslip PDF | Typst through the `typst` Python package. Data in via `sys.inputs`, PDF/A, fixed timestamp | `typst` crate, same `.typ` template |
| pain.001 and voucher | lxml against the Bits guide (pain.001.001.09). Voucher as CSV or JSON | quick-xml, serde |
| ID checks | python-stdnum for national ID, bank account and orgnr | Mod-11 checks by hand |
| Login | Managed OIDC as in §1.3, through authlib. BankID only in M1 | openidconnect |
| MCP | The official `mcp` SDK with a hand-picked tool list. Synthetic data only: §4 rules out MCP on real data in M0 | rmcp |
| Jobs | None in M0 (E3) | – |
| Demo frontend | Vite, React, TanStack Router, Query and Table, shadcn/ui and Tailwind. Client generated from `openapi.json` (orval). No Next.js. The M0 interface stays the CLI; the UI is for demos on synthetic data | Unchanged |

Pin current versions when scaffolding.

**Also considered:** Vercel. It is fine for the static frontend and for demos on synthetic data. It is not for real payroll data:
- Vercel is a US company with no Norway region.
- The database would have to face the internet.
- It has no long-running worker.

## 4. Rules while prototyping (keeps the Rust rewrite cheap)
1. **Pure calculation core.** No database, clock or I/O: inputs + rule pack + engine version → lines and an explanation trace (§1.3).
2. **Shared golden cases.** They live in a language-neutral folder as JSON, and the Rust build must pass the same files. Agents never edit them (PLAN.md "Rules").
3. **Every rounding names its legal rule.** Python's `round()` and `Decimal`'s default context both round half to even, so neither is ever used directly.
4. **Hash the stored bytes at approval.** That covers the payslip, a-melding, pain.001 and voucher. Never regenerate them for the hash, because Rust serialises differently.
5. **Append-only audit and per-output status** (E9, B43). A trigger blocks UPDATE and DELETE.
6. **No personal data in errors.** FastAPI's 422 errors echo the input, so national IDs reach responses and logs. Use a custom error handler with redaction (E9).
7. **Nothing that won't port:** no ORM, no framework sessions, no Celery.

## 5. Localhost (B48)
**Why it fits:**
- The data stays in Norway, and there is no hosting decision to make.
- No database faces the internet.
- M0 needs no inbound traffic: the a-melding is uploaded by hand on skatteetaten.no, and pain.001 in the online bank.

**Rules:**
- **Postgres is bound to 127.0.0.1.** In Docker Compose that is `"127.0.0.1:5432:5432"`. A plain `"5432:5432"` listens on every network interface.
- **Disk encryption (FileVault) is on.**
- **Coding agents never see real payroll data** (§5, §11).
  - Develop and demo on synthetic data.
  - Real data lives in a separate database, with a database role the agent's tools cannot reach. Sjur loads it and runs it by hand for the shadow runs.
- **Backups:**
  - Take an encrypted `pg_dump` and copy the generated files (a-meldinger, payslips, pain.001).
  - Keep them on an encrypted drive in Norway, for 5 years after each year-end (§1.4 item 7).
  - Test a restore on another machine once.
- **Sharing with Peter and Sander:** Tailscale. A public tunnel (Cloudflare) is only for demos on synthetic data.
- **The laptop is a single point of failure.** That is acceptable for shadow runs, because the current system is the fallback. It is not acceptable for a system of record.

**Leave localhost** when Brutto becomes system of record (M0-L), when the first external user needs access, or when a customer's agent needs MCP. The prototype then moves to Azure Norway East (E4). Run everything in Docker Compose from day one, so the move is just moving the containers.

## 6. The rewrite path
1. A Rust calculation crate passes all golden cases and the table file.
2. Shadow run: Rust and Python results on the same inputs, compared to the øre.
3. axum goes in front and forwards every unported route to Python. Operations move over one at a time on the same database, migrations, contract and tokens. There is no big-bang switch.

Don't call Rust from Python (PyO3) before then: it means debugging two languages.

## 7. What the research confirmed
These are already reflected in PLAN.md:
- **Manual upload is not in Altinn.** It is Skatteetaten's own file upload, with an ID-porten login and the "A-ordningen" package.
- **The file format is changing.** XML upload is accepted through 2026, and JSON after that [verify which periods]. The a-melding REST API takes JSON only.
- **The trekkrutine still has no licence.** GitHub issue #7 has had no answer since 10.12.2025.
- **Forskuddstrekk is paid as its own payment order** to Skatteetaten.

**Not in PLAN.md:** XSD validation in Rust is the weakest piece.
- The `libxml` crate wraps libxml2 and is not tested for multithreaded use.
- libxml2's maintenance is uncertain [verify].

This matters only for the XML fallback.
