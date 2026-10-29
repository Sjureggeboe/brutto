# R6 – API og MCP for Brutto

Dato 29.10.2026. Rapporten er faktagrunnlag for beslutning B41.

Rapporten bygger på kilder lest 29.10.2026. Fakta uten bekreftet kilde har merket «(verifiseres)».

## §1 MCP-spesifikasjonen

**Gjeldende versjon er 2026-07-28.** Spesifikasjonen merker den «current» ([versjonering](https://modelcontextprotocol.io/specification/versioning)). Forrige versjon var 2025-11-25.

**Hovedendringer i 2026-07-28** ([endringslogg](https://modelcontextprotocol.io/specification/2026-07-28/changelog)):
- Protokollen er tilstandsløs. Revisjonen fjerner håndtrykket `initialize` og headeren `Mcp-Session-Id`. Hver forespørsel bærer versjon og klientkapabiliteter i `_meta`.
- Serveren må implementere `server/discover`.
- Serveren sender ikke lenger egne forespørsler til klienten. Den svarer `input_required` (Multi Round-Trip Requests), og klienten sender forespørselen på nytt med svarene.
- `subscriptions/listen` erstatter GET-strømmen og `resources/subscribe`.
- Roots, Sampling og Logging er Deprecated. Spesifikasjonen kan fjerne dem tidligst i første revisjon etter 28.07.2027 ([register](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)).
- Spesifikasjonen har fått tilstandene Active, Deprecated og Removed, med minst tolv måneders varsel før fjerning.

**Status per funksjon**

| Funksjon | Status i 2026-07-28 | Kilde |
|---|---|---|
| Streamable HTTP | Standard transport for fjernservere. Ett POST-endepunkt. Svar som JSON eller SSE per forespørsel. Ingen sesjoner, ingen GET-strøm, ingen gjenopptak. Headerne `MCP-Protocol-Version`, `Mcp-Method` og `Mcp-Name` er påkrevd. Serveren MÅ validere `Origin`. HTTP+SSE er Deprecated. | [transport](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http) |
| Autorisasjon | Valgfri i protokollen. Over HTTP gjelder OAuth 2.1, som fortsatt er et IETF-utkast (draft 13). | [autorisasjon](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) |
| Protected Resource Metadata (RFC 9728) | MÅ for servere og klienter. | samme |
| Resource indicators (RFC 8707) | Klienten MÅ sende `resource`. Serveren MÅ sjekke at tokenet er utstedt til den. | samme |
| Issuer-validering (RFC 9207) | Ny. Klienten MÅ sjekke `iss` når den finnes. | samme |
| Client ID Metadata Documents (CIMD) | BØR støttes. Bygger på IETF-utkast -00. | [klientregistrering](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration) |
| Dynamic Client Registration (DCR) | Deprecated fra 2026-07-28. Beholdes for bakoverkompatibilitet. | [register](https://modelcontextprotocol.io/specification/2026-07-28/deprecated) |
| Forbud mot token passthrough | Gjelder. Serveren MÅ IKKE akseptere eller videresende tokens som er utstedt til andre. | [autorisasjon](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) |
| Tool annotations | Uendret. Standardverdier: `readOnlyHint` false, `destructiveHint` true, `idempotentHint` false, `openWorldHint` true. Alle er hint. Klienten MÅ regne dem som upålitelige fra servere den ikke stoler på. | [schema.ts](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2026-07-28/schema.ts), [tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) |
| outputSchema og structuredContent | Active. Nå tillatt med alle JSON Schema 2020-12-nøkkelord og alle JSON-verdier. Serveren MÅ følge `outputSchema` når den oppgir et. | [tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) |
| Elicitation, skjemamodus | Active. Serveren MÅ IKKE be om passord, nøkler, tokens eller betalingsdata i skjema. | [elicitation](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation) |
| Elicitation, URL-modus | Kom i 2025-11-25. Siden sier at designet kan endres. Brukes til sensitive steg som skal skje utenfor klienten. | samme |
| Lange operasjoner | Tasks ligger nå i utvidelsen `io.modelcontextprotocol/tasks`, med status «Beta, to Core». Serveren returnerer et håndtak, og klienten poller med `tasks/get`. | [utvidelser](https://modelcontextprotocol.io/extensions/overview), [tasks](https://modelcontextprotocol.io/extensions/tasks/overview) |
| Resources og prompts | Active. Listesvar må ha `ttlMs` og `cacheScope`. | [endringslogg](https://modelcontextprotocol.io/specification/2026-07-28/changelog) |
| MCP Apps (UI i samtalen) | Utvidelse, Stable. | [utvidelser](https://modelcontextprotocol.io/extensions/overview) |
| OAuth Client Credentials og Enterprise-Managed Authorization | Utvidelser, Stable. | samme |

**Klientstøtte for fjern-MCP med OAuth**
- **Claude** (web, Desktop, mobil, Cowork, Claude Code) støtter Streamable HTTP og HTTP+SSE. OAuth følger autorisasjonsspesifikasjonene 2025-03-26, 2025-06-18 og 2025-11-25. Siden nevner ikke 2026-07-28 ([Claude](https://claude.com/docs/connectors/building)). Claude registrerer seg med DCR eller CIMD, og velger CIMD bare når autorisasjonsserveren oppgir både `client_id_metadata_document_supported` og `none` som autentiseringsmetode. `client_credentials` støttes ikke ([Claude auth](https://claude.com/docs/connectors/building/authentication)). Grenser i de hostede appene: cirka 150 000 tegn per verktøysvar og 240 sekunder per kall. Resource subscriptions og sampling støttes ikke.
- **ChatGPT** bruker OAuth 2.1 med PKCE (S256), sender `resource` i autorisasjons- og tokenkall, leser Protected Resource Metadata og foretrekker CIMD. DCR støttes fortsatt ([OpenAI Apps SDK](https://developers.openai.com/apps-sdk/build/auth)). Hvilke abonnement som gir tilgang (verifiseres).
- **Microsoft Copilot Studio** støtter bare Streamable HTTP, og har ikke støttet SSE etter august 2025. Autentisering: ingen, API-nøkkel eller OAuth 2.0 med DCR og discovery, DCR uten discovery eller manuell klient ([Microsoft Learn](https://learn.microsoft.com/microsoft-copilot-studio/mcp-add-existing-server-to-agent)). Microsoft 365 Copilot støtter MCP i deklarative agenter med OAuth (verifiseres) ([Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/build-mcp-plugins)).
- **Cursor** støtter stdio, SSE og Streamable HTTP, OAuth med PKCE og DCR, og faste klientdata i `mcp.json`. Tools, prompts, resources, roots, elicitation og MCP Apps er støttet ([Cursor](https://cursor.com/docs/context/mcp)).
- Hvilke klienter som støtter Tasks (verifiseres). [Matrisen](https://modelcontextprotocol.io/extensions/client-matrix) lot seg ikke lese maskinelt.

## §2 Rust: rmcp

- **Versjon:** rmcp 3.8.0 kom 26.10.2026. Versjon 1.0.0 kom 03.03.2026, 2.0.0 kom 29.06.2026 og 3.0.0 kom 28.07.2026, samme dag som spesifikasjonen. Minste Rust-versjon er 1.88 ([crates.io](https://crates.io/crates/rmcp/versions)).
- **Modenhet:** MCP-prosjektet plasserer Rust-SDK-en i Tier 1, sammen med TypeScript, Python, C#, Go og Ruby ([SDK-oversikt](https://modelcontextprotocol.io/docs/sdk)). Tre hovedversjoner fra mars til juli 2026 betyr hyppige migreringer.
- **Protokoll:** rmcp implementerer 2026-07-28 og er kompatibel med 2025-11-25 og eldre ([rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)).
- **Streamable HTTP-server:** `StreamableHttpService` er en Tower-tjeneste som monteres i en axum-router. Den kjører tilstandsløst mot 2026-07-28-klienter. Tasks-utvidelsen er støttet (samme kilde).
- **OAuth:** Dokumentasjonen dekker klientsiden: discovery, token og fornyelse. Serversiden finnes bare som eksempel ([OAUTH_SUPPORT.md](https://github.com/modelcontextprotocol/rust-sdk/blob/main/docs/OAUTH_SUPPORT.md)). Tokenvalidering og metadata-endepunkt må Brutto bygge selv i axum.

**OpenAPI til MCP-verktøy**
- `rmcp-openapi` 0.32.0 lager MCP-verktøy fra OpenAPI. Den er tredjepart (lx-industries) og før 1.0 ([crates.io](https://crates.io/crates/rmcp-openapi)).
- Stainless og Speakeasy genererer MCP-servere fra OpenAPI. Speakeasy lar deg merke operasjoner `read`, `write` eller `destructive` og starte serveren med et utvalg ([Speakeasy](https://www.speakeasy.com/mcp/tool-design/generate-mcp-tools-from-openapi)).
- **Erfaring med 1:1-mapping:**
  - Stainless (07.05.2025): Brukerne vil som regel ha rundt et dusin verktøy om gangen. For store API-er bruker Stainless en dynamisk modus med tre meta-verktøy: søk etter endepunkt, hent skjema og kall. Cursor hadde da et tak på 40 verktøy ([Stainless](https://stainless.com/blog/lessons-from-openapi-to-mcp-server-conversion)).
  - FastMCP: Kuraterte servere gir betydelig bedre resultater enn autokonverterte, særlig for store API-er ([FastMCP](https://gofastmcp.com/integrations/openapi)).
  - Anthropic fraråder å pakke inn hvert endepunkt ([Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents)).
  - Claudes katalog avviser et samleverktøy som tar både lesende og skrivende HTTP-metoder ([Claude review](https://claude.com/docs/connectors/building/review-criteria)).

## §3 OpenAPI i Rust

| Crate | Siste versjon | OpenAPI | Rammeverk | Nedlastinger siste 90 dager |
|---|---|---|---|---|
| utoipa | 6.0.0 (22.09.2026) | 3.1 | axum (via utoipa-axum 0.3.0), actix-web, rocket | 20,3 mill. |
| aide | 0.15.1 (14.04.2026) | bare 3.1.0 | bare axum | 1,3 mill. |
| poem-openapi | 5.1.16 (28.07.2025) | 3.0.0 | bare poem | 0,5 mill. |

Kilder: [crates.io utoipa](https://crates.io/crates/utoipa), [utoipa README](https://github.com/juhaku/utoipa), [aide docs.rs](https://docs.rs/aide/latest/aide/), [poem-openapi kildekode](https://github.com/poem-web/poem/blob/master/poem-openapi/src/registry/ser.rs), [crates.io aide](https://crates.io/crates/aide), [crates.io poem-openapi](https://crates.io/crates/poem-openapi).

- **utoipa er mest brukt.** utoipa-axum alene har 4,5 mill. nedlastinger siste 90 dager ([crates.io](https://crates.io/crates/utoipa-axum)).
- aide henter skjema fra schemars ([docs.rs](https://docs.rs/aide/latest/aide/)).
- poem-openapi skriver `"openapi": "3.0.0"` og krever poem. Den passer ikke med axum.

**Verktøy**
- **oasdiff** v1.35.0 (28.10.2026) finner brytende endringer (`breaking`) og lager endringslogg (`changelog`). Den støtter OpenAPI 3.1 og 3.2 og har en GitHub Action ([oasdiff](https://github.com/oasdiff/oasdiff)).
- **Spectral** v6.17.0 (01.10.2026) linter OpenAPI 2.0, 3.0, 3.1 og 3.2, AsyncAPI og Arazzo, med egne regelsett ([Spectral](https://github.com/stoplightio/spectral)).
- **Redocly CLI** 2.72.1 (29.10.2026) linter OpenAPI 3.x og 2.0, AsyncAPI og Arazzo, med konfigurerbare regler ([Redocly](https://github.com/Redocly/redocly-cli)).

## §4 Beste praksis for agentvennlige API-er og MCP-verktøy

**Anthropic, «Writing effective tools for agents» (11.09.2025)** ([lenke](https://www.anthropic.com/engineering/writing-tools-for-agents)):
1. Lag få, målrettede verktøy for viktige arbeidsflyter. Slå sammen kjedede steg til ett kall.
2. Bruk navnerom med prefiks per tjeneste eller ressurs. Test hvilken form modellen treffer best med.
3. Returner kontekst med høyt signal. Navn fungerer bedre enn UUID-er. Tilby `response_format` (kort eller detaljert). I eksempelet brukte kort svar cirka en tredjedel av tokenene.
4. Bruk paginering, filtrering og avkorting med fornuftige standardverdier. Claude Code kutter verktøysvar ved 25 000 tokens som standard.
5. Skriv feilmeldinger som forteller agenten hva som er galt og hvordan den retter det.
6. Beskriv verktøyet som for en nyansatt. Bruk entydige parameternavn som `user_id`.
7. Evaluer med realistiske oppgaver i flere steg, og les transkriptene.

**Anthropic, «Advanced tool use» (24.11.2025)** ([lenke](https://www.anthropic.com/engineering/advanced-tool-use)): 58 verktøy fra fem servere brukte cirka 55 000 tokens før samtalen startet. Tool Search anbefales fra 10 verktøy. Treffsikkerheten for Opus 4.5 økte fra 79,5 % til 88,1 %. Eksempler i verktøydefinisjonen økte treffsikkerheten på komplekse parametere fra 72 % til 90 %.

**Anthropic, «Code execution with MCP» (04.11.2025)** ([lenke](https://www.anthropic.com/engineering/code-execution-with-mcp)): Kodekjøring kuttet et eksempel fra cirka 150 000 til 2 000 tokens. Klienten kan bytte ut personopplysninger med plassholdere før modellen ser dem.

**MCP-spesifikasjonen** ([tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)):
- Verktøynavn BØR ha 1 til 128 tegn og bare bruke A–Z, a–z, 0–9, `_`, `-` og `.`.
- Serveren BØR returnere verktøylisten i fast rekkefølge, slik at klienten og prompt-cachen kan gjenbruke den.
- Feil kommer som protokollfeil (JSON-RPC) eller som verktøyfeil med `isError: true`. Verktøyfeil skal gi modellen nok informasjon til å rette kallet.
- Tilstand mellom kall: Serveren returnerer et eksplisitt håndtak, sjekker tilgang på hvert kall, oppgir levetiden i beskrivelsen og gir en tydelig feil når håndtaket er utløpt.
- MCP-paginering med ugjennomsiktig cursor gjelder bare listeoperasjonene, som `tools/list`. Paginering i verktøysvar designer serveren selv ([paginering](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination)).
- MCP-prosjektet oppgir ikke et anbefalt antall verktøy (verifiseres).

**Claudes katalogkrav** ([review](https://claude.com/docs/connectors/building/review-criteria)): Skill lesende og skrivende verktøy, gjerne videre i opprett, endre og slett. Alle verktøy må ha `title` og riktig hint. Claude kan kjøre lesende verktøy uten bekreftelse og spør alltid før destruktive. Navn kan ha maks 64 tegn. Beskrivelser skal ikke gi Claude atferdsinstrukser. Generiske feil uten detaljer stryker. Svar skal ha rimelig størrelse.

## §5 Hvem har offentlig API og MCP

| Leverandør | Offentlig API | MCP | Kilde |
|---|---|---|---|
| Visma (Payroll Norge) | Delvis. Visma.net Payroll Norway har Employee Public API og Payroll Norway API. Tilgang krever trolig partneravtale (verifiseres). | Nei for lønn (verifiseres). Visma Business NXT har offisiell MCP i pilot med begrenset tilgang fra 08.05.2026. | [Visma API](https://www.vismasoftware.no/api-en), [Business NXT MCP](https://docs.vismasoftware.no/businessnxtapi/ai/mcp/), [release notes](https://docs.vismasoftware.no/businessnxtapi/release-notes/2026-05-08-mcp-documentation/) |
| Tripletex | Ja, API v2. | Offisiell, beta. OAuth. Dekker timer, ordre, kunder, leverandører og egne lønnsslipper. | [Tripletex MCP](https://github.com/Tripletex/tripletex-mcp) |
| PowerOffice Go | Ja. Lønnslinjer kan skrives, lønnsdetaljer per ansatt er ikke eksponert. | Tredjepart (Peliqan). Offisiell ikke funnet. | [PowerOffice](https://developer.poweroffice.net/workflows/endpoints/payroll/salary-lines), [Peliqan](https://peliqan.io/academy/how-to-connect-poweroffice-to-claude/) |
| Fiken | Ja, API v2 med OAuth2. | Tredjepart, bare lesing. | [Chift](https://docs.chift.eu/connectors/accounting/fiken), [fiken-read-only-mcp](https://www.remoteopenclaw.com/mcp/heim/fiken-read-only-mcp) |
| SD Worx | Delvis. Tilgang via support med OAuth 2.0 (verifiseres). | Tredjepart (Apideck). | [Apideck](https://developers.apideck.com/connectors/sdworx/docs/application_owner+oauth_credentials), [Apideck MCP](https://www.apideck.com/mcp-server/sdworx-webservice) |
| NettLønn | Nei funnet. Nettsiden nevner integrasjoner, ikke API (verifiseres). | Nei funnet. | [nettlonn.com](https://nettlonn.com) |
| Huma | Ja, Open API med OAuth2 client credentials. | Ikke funnet (verifiseres). | [Huma Open API](https://openapi.humahr.com/redoc/index.html) |
| Gusto | Ja. | Offisiell. Godkjenning av lønnskjøring forblir et menneskelig valg (verifiseres). | [Gusto](https://gusto.com/product/agents), [docs.gusto.com](https://docs.gusto.com/embedded-payroll/v2023-04-01/reference) |
| Deel | Ja. | Offisiell. OAuth2 eller personlig token. Har skrivende verktøy. | [Deel MCP](https://developer.deel.com/mcp) |
| Rippling | Ja, Platform API. | Tredjepart. Offisiell ikke funnet. | [rippling-mcp](https://mcpservers.org/servers/bifrost-mcp/rippling-mcp) |
| Personio | Ja (verifiseres). | Offisiell, beta. OAuth, egen URL per kunde. | [Personio](https://support.personio.de/hc/en-us/articles/38314656674333-Personio-MCP-server-Beta-access-overview) |
| HiBob | Ja. | Offisiell. Byttet til OAuth med brukertilgang 30.06.2026. | [HiBob MCP](https://apidocs.hibob.com/docs/hibob-mcp-server) |

Norske Simployer (HR) har også MCP ([Simployer](https://mysupport.simployer.com/en/support/solutions/articles/201000132208-simployer-mcp-model-context-protocol-tools-customer-guide)). Ingen av de norske leverandørene i tabellen har en offisiell MCP som kjører lønn.

## §6 Sikkerhet ved MCP for sensitive data

| Risiko | Hva skjer | Anbefalte kontroller |
|---|---|---|
| Prompt injection og dataeksfiltrering | En agent med sensitive data, upålitelig innhold og en vei ut kan lekke data ([Willison, 16.06.2025](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)). En ondsinnet GitHub-issue fikk en agent til å lekke private repoer via GitHubs MCP-server ([Invariant Labs, mai 2025](https://invariantlabs.ai/blog/mcp-github-vulnerability)). | Serveren MÅ validere input, ha tilgangskontroll, begrense kallrate og rense output. Klienten BØR vise input før kallet og be om bekreftelse på sensitive operasjoner. Et menneske BØR kunne avvise kall ([tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)). |
| Confused deputy | En MCP-proxy med statisk klient-ID mot en tredjepart, DCR og samtykke-cookie lar en angriper få autorisasjonskoden. | Samtykke per klient før tredjepartsflyten, eksakt match på `redirect_uri`, `state` som brukes én gang og utløper raskt, cookies med `__Host-`, vern mot innramming ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)). |
| Token passthrough | Serveren godtar et token utstedt til en annen tjeneste og sender det videre. Kontroller og revisjonsspor forsvinner. | MÅ IKKE godta tokens som ikke er utstedt til serveren. Valider audience (samme kilde). |
| For brede scopes | Et lekket token med `*` eller `admin:*` gir tilgang til alt. | Minimal startscope. Step-up med 403 og `insufficient_scope` når et privilegert verktøy brukes første gang. Ingen jokertegn. Logg eskaleringer (samme kilde, [autorisasjon](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)). |
| Kapring av tilstandshåndtak | En angriper gjetter et håndtak og bruker en annen brukers tilstand. | Tilfeldige håndtak, bundet til bruker-ID fra tokenet. Håndtaket gir aldri tilgang alene ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)). |
| Phishing via URL-elicitation | En angriper sender lenken videre til en annen bruker, som fullfører flyten. | Serveren MÅ sjekke at samme bruker åpner URL-en. Ingen personopplysninger i URL-en. Ingen forhåndsautentiserte URL-er ([elicitation](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation)). |
| SSRF | Autorisasjonsserveren henter en CIMD-URL som peker til interne tjenester. | Blokker private IP-er og bruk egress-proxy ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)). |
| Mix-up | En ondsinnet autorisasjonsserver får koden fra en ærlig server. | Send `iss` og la klienten validere den ([autorisasjon](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)). |
| DNS rebinding | En nettside når en lokal MCP-server. | Serveren MÅ validere `Origin` ([transport](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)). |

## §7 Hva det betyr for Brutto

1. **Bygg mot 2026-07-28 og støtt 2025-11-25.** Claude dokumenterer bare autorisasjon til og med 2025-11-25. rmcp 3.x håndterer begge. Lås rmcp-versjonen og sett av tid til en hovedversjon per kvartal.
2. **Bygg ressursserveren selv i axum.** rmcp gir ikke tokenvalidering eller Protected Resource Metadata på serversiden. Brutto trenger egen OAuth 2.1-autorisasjonsserver eller en IdP som støtter både CIMD og DCR. Claude og Copilot Studio faller tilbake på DCR, og ChatGPT støtter den fortsatt, selv om spesifikasjonen har gjort DCR Deprecated. Microsoft Entra manglet per 05.08.2026 støtte for DCR og CIMD for disse klientene ([Microsoft](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-ga/)).
3. **Lag arbeidsflytverktøy for fase 1.** Sikt på 10 til 15 verktøy med prefikset `brutto_`, for eksempel `brutto_ansatte_sok`, `brutto_a07_start_henting`, `brutto_a07_status`, `brutto_a07_avvik` og `brutto_kontroller_kjor`. REST-API-et dekker hele domenet. MCP-laget kaller de samme domenetjenestene og den samme tilgangskontrollen. Generer det ikke 1:1 fra OpenAPI.
4. **Skill lesing og skriving i egne verktøy med annotations.** Gi alle verktøy `title`, `readOnlyHint` eller `destructiveHint`. Det er et krav for Claudes katalog. Behandle annotations som hjelp til klienten. Sikkerheten ligger i Bruttos egen tilgangskontroll.
5. **La MCP starte handlinger med rettsvirkning og BankID fullføre dem.** Verktøyet lager en ventende forespørsel og svarer med URL-elicitation til en BankID-side hos Brutto. Brutto sjekker at det er samme bruker (`sub`), og URL-en inneholder verken personopplysninger eller innloggingsdata. Claudes katalog godtar ikke koblinger som overfører penger. Et verktøy som starter utbetaling kan derfor stoppe en katalogoppføring (verifiseres).
6. **Gjør A07-hentingen asynkron med håndtak.** Claude avbryter kall etter 240 sekunder, og Tasks er fortsatt Beta med uklar klientstøtte. Bruk start- og statusverktøy med eksplisitt håndtak bundet til bruker og klient, og legg til Tasks når klientene støtter det.
7. **Design scopes etter domene og risiko.** Eksempler: `ansatte:les`, `a07:les`, `a07:hent`, `lonn:forbered`, `lonn:godkjenn`. Start med lesescopes og bruk step-up for resten. For byråer binder tokenet bruker og klient. Gi hver virksomhet egne brytere for lese- og skrivetilgang via KI, slik Visma Business NXT gjør.
8. **Gi kompakte, strukturerte svar.** Returner `structuredContent` med `outputSchema` og en kort tekstversjon. Bruk cursor, standardgrense og `response_format`. Hold svarene godt under 25 000 tokens. Vis ansattnummer og navn som standard, og fødselsnummer bare med eget scope.
9. **Behandle innholdet i Brutto som upålitelig for modellen.** Fritekst fra ansatte, Huma og A07 kan inneholde injiserte instrukser. Ha ingen MCP-verktøy som sender data ut av Brutto, som e-post eller webhooks. Logg hvert kall med klient-ID, bruker, scope og argumenter.
10. **Bruk utoipa 6 med utoipa-axum for OpenAPI 3.1, og kjør oasdiff og Spectral i CI.** Bryt bygget ved brytende endringer uten ny versjon. MCP Apps er Stable og støttes av Claude og Cursor, så grafene i fase 1 kan også vises direkte i samtalen.
