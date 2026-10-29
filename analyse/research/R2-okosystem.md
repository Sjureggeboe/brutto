# R2 – Økosystemet: behovene til dem som bygger mot Brutto, og dem som kobler det sammen

**Produkt:** Brutto, et frittstående lønnssystem (SaaS) for norske virksomheter med 10–1000 ansatte. Det lisensieres også til regnskapsbyråer.
**Runde:** 2 av behovskartleggingen (behov og kontrakter). **Dato:** 28. oktober 2026.
**Grunnlag:**
- R1-rapportene G (moduler/plattform), F (arkitektur), B (myndigheter), C (beregning), D (praksis) og E (byrå)
- Nye oppslag 28.10.2026 hos Skatteetaten (styrehonorar og verv) og Huma (OpenAPI-spesifikasjon, webhooks, integrasjonssider)

**Arbeidsmåte:** Runde A (utkast) → runde B (kritikk) → revidert versjon. Dokumentet viser den **reviderte versjonen**. Kapittel 9 forklarer hva runde B endret og hvorfor.

**Merking:**
- **[R1-x]** = bygger på R1-rapport x
- **[P]** = bekreftet i primærkilde i denne runden
- **[U]** = usikkert, må verifiseres
- **[V]** = min vurdering
- **(B)** = behov eller kontraktsdel som ble endret eller lagt til i runde B
- **[Bekreftet]** og **[Antatt]** brukes i Huma-delene for å skille hva som er sjekket mot Humas egne kilder fra hva jeg har antatt

---

## 0. Sammendrag

1. **«Åpne integrasjoner på like vilkår» betyr at Bruttos offentlige API *er* plattformen.** G foreslo en «føderert plattformkjerne» med felles personkatalog, identitet, rettigheter og fakturering på tvers av selskapene. Det gir søsterproduktene forrang og er for stort for et team på 5–7 utviklere. Utleggsappen, OrgLab, Tikket, Huma, Planday og Bruttos egne moduler for fravær, timer og utlegg er alle klienter av det samme API-et.
2. **Én mekanisme mot konflikt: kilderegisteret.** For hver kunde og hver datatype (fravær, timer, utlegg, arbeidsforhold, person, avtalt lønn …) finnes nøyaktig én aktiv kilde, eventuelt avgrenset til en gruppe arbeidsforhold. Det kan være Bruttos egen modul eller en installert app. API-et og Bruttos eget skjermbilde avviser skriving fra andre enn kilden. Kunden bytter kilde med en planlagt **kildebytte**-prosedyre ved periodeskifte, med skyggeperiode, åpningssaldoer og mulighet til å rulle tilbake. Kilderegisteret erstatter både G-s «attributteierskap» og mitt «kildeansvar per kategori» fra runde A.
3. **OrgLab og Tikket er ikke HR-master og tidssystem, slik G antok.** De betaler i hovedsak **personer som ikke er vanlige ansatte**: styremedlemmer, tillitsvalgte, honorarmottakere, ekstrahjelp og artister. Den nye byggeklossen er **engasjement med innebygd mottaker-onboarding** («honorar-lenke»). Personen bekrefter fødselsnummer og kontonummer selv med BankID, og Brutto eier arbeidsforholdet i a-meldingen.
4. **Én skrivekontrakt for alle kilder: lønnsgrunnlag v2, pluss fravær v1.** Kilden sender alltid *full tilstand*, og Brutto beregner differansen mot det som allerede er låst eller utbetalt. Kilder sender aldri a-meldingskoder, utbetalingsmåned eller kontonummer.
5. **Dobbel utbetaling stoppes av tre ting:**
   - idempotens på (installasjon, eksternId, revisjon)
   - kilderegisteret, som sørger for at bare én kilde leverer for eksempel reiseregning for et arbeidsforhold
   - at direkte utbetaling utenom lønn bare gjelder rene refusjoner, som aldri sendes inn i Brutto
6. **Feil i a-meldingen stoppes av at Brutto eier både klassifisering og arbeidsforhold.**
   - Arbeidsforhold som kommer fra en integrasjon, er utkast til et menneske har godkjent dem.
   - Nye installasjoner går i skyggemodus.
   - Hver linjetype har beløpsgrenser.
   - Fødselsnummer må være BankID-verifisert.
   - Grenser som 10 000 kr for skattefrie organisasjoner holdes bare i Brutto.
7. **Huma:** Huma har et offentlig REST-API med OAuth2 og webhooks for profil, stilling, fravær og grupper [Bekreftet], men ingen API for lønnsresultat eller dokumenter [Bekreftet i spesifikasjonen]. Brutto bygger og drifter Huma-koblingen selv, som en app på egen plattform. Erstatningen skjer i tre faser:
   - **Sameksistens:** Huma er HR-master, og Brutto kjører lønn.
   - **Brutto overtar fravær, timer og utlegg.**
   - **Brutto overtar HR-masteren.**

   Dette krever fra dag én en kanonisk person- og arbeidsforholdsmodell, eierskap som kan flyttes, et dokumentlager og et importrammeverk.
8. **Dogfooding skal kunne måles.** Bruttos egne moduler kjøres som egne klienter mot det offentlige API-et med OAuth. Et byggesteg stopper kall til udokumenterte endepunkter. Ved hver release kjøres en «byttetest», der egen modul erstattes av en åpen referanseintegrasjon og lønnsresultatet skal bli likt på øret.
9. **DX-pakken ved lansering er liten men komplett:**
   - dokumentasjon (OpenAPI, fire guider og en feilkatalog)
   - selvbetjent sandkasse med tidsmaskin
   - OAuth-appregistrering
   - webhook-logg med replay
   - avviklingspolicy og statusside
   - llms.txt
   - en åpen referanseintegrasjon

   SDK-er, iframe-komponenter og markedsplass kommer ikke ved lansering.
10. **AI-agenter:** Agentrollen og token «på vegne av» en bruker må inn i tilgangsmodellen fra start (Må). Selve MCP-serveren er Bør. Agenter kan lese, forklare og lage *utkast*, men aldri godkjenne, sende, utbetale eller endre kontonummer.

---

## 1. Rammer og rettelser fra runde 1

### 1.1 Hva «åpne integrasjoner på like vilkår» betyr for G-s anbefalinger

| G anbefalte [R1-G] | Problem med gründerbeslutningen | Ny anbefaling [V] |
|---|---|---|
| Føderert plattformkjerne med felles identitet, personkatalog, ID-mapping, samtykke, hendelser og fakturering for alle modulene | En kjerne som deles på tvers av selskaper gjør søsterproduktene til «innsidere» | **Bruttos offentlige plattform**: API, hendelser, installasjoner, tilgangspakker og kilderegister. Alle andre er klienter. |
| Felles `personId` på tvers av produktene | Krever en felles master på tvers av selskaper | Brutto eier sine egne ID-er. Hver installasjon har sin egen koblingstabell (ekstern ID ↔ Bruttos ID) via matching-API. |
| Felles SSO, «én konto, mange moduler» | Ikke nødvendig. Kunden har sin egen IdP. | SSO mot kundens Entra ID eller Google. Brutto som OIDC-leverandør for andre: Ikke nå. |
| Entitlements og felles faktura i kjernen | Hvert selskap fakturerer selv | Ingen felles fakturering i år 1. Kommersielle pakker er avtaler, ikke teknikk. |
| Mikrofrontender mellom egne moduler (nivå 3 i G 1.8) | En privilegert kanal | Fjernes. Bare dyplenker og vertsbaserte sider, og de er like for alle. |
| «Utleggsappen-kontrakten i produksjon først» | Rekkefølgen er grei, men kontrakten må ikke bli skreddersydd | Kontrakten dokumenteres som den generiske utlegg/reise-kontrakten som Pleo, Visma Expense, Bruttos egen utleggsmodul og andre bruker. **Lik tilgang betyr ikke lik rekkefølge.** |

### 1.2 Rettelse: OrgLab og Tikket

| Produkt | G antok | Riktig | Konsekvens |
|---|---|---|---|
| **OrgLab** | Organisasjon/HR-master (org.struktur, stillinger, ledere) | **Medlemshåndtering** for organisasjoner (à la Cornerstone): medlemmer, verv, styrer, tillitsvalgte, møter, kontingent | OrgLab eier ikke arbeidsforhold for ansatte. Den leverer honorarer og godtgjørelser for verv, møtegodtgjørelser og tapt arbeidsfortjeneste til personer som oftest ikke er ansatt. Organisasjonens egne ansatte forvaltes i Brutto eller i et HR-system. |
| **Tikket** | Tid/registrering (timer, fravær, saldo) | **Billett og arrangement**: arrangementer, billettsalg, vaktplan for arrangementet, frivillige, artister og foredragsholdere | Tikket leverer vakter for ekstrahjelp og honorarer, med arrangementet som kostnadsdimensjon. Tikket har ikke fraværsregister eller saldoer. |
| G-s **B2** (org/HR → lønn) | – | Flyttes til tredjeparts HR-systemer (Huma, Simployer, HiBob …) | Se 4.4 (Huma) og 4.5 |
| G-s **B3** (tid → lønn) | – | Flyttes til tid/vakt-systemer (Planday, Tamigo, Quinyx) og Bruttos egen timemodul | Tikket bruker vakt-delen |

### 1.3 Nye gründerkrav i denne runden og hva de endrer

| Krav | Hva det endrer i rapporten |
|---|---|
| **Brutto får egne moduler for ferie/fravær, timer og utlegg.** Modulene bruker samme offentlige API og samme lønnsgrunnlagskontrakt som Utleggsappen og tredjeparter. Kunden kan slå av en egen modul og koble på et eksternt system. | (a) Kilderegisteret blir et sentralt plattformobjekt (2.2). (b) Det trengs en egen ressurs for fravær, fordi fravær er fakta med lønnskonsekvens og ikke et beløp (2.6). (c) Kapittel 5 beskriver konfliktregler, kildebytte og målbar dogfooding. (d) **Bruttos utleggsmodul konkurrerer direkte med søsterproduktet Utleggsappen.** Likebehandlingen må derfor gjelde i begge retninger. |
| **Huma-integrasjon. Brutto skal på sikt erstatte Huma.** | Ny kontrakt i 4.4 og erstatningsvei i kapittel 6. Kravene fra dag én (kanonisk modell, flyttbart eierskap, dokumentlager, import) løftes inn som Må-behov. |

### 1.4 Fagfakta som styrer OrgLab og Tikket

| Tema | Fakta | Status |
|---|---|---|
| Styrehonorar og godtgjørelse for verv | Kontantytelse. Skal «alltid førast opp som trekkpliktig». AGA-pliktig, med unntak bare for registrerte trygdeunntak. Rapporteres i utbetalingsmåneden. Gjelder styre, representantskap, utvalg, råd og folkevalgte verv. | [P] [Skatteetaten](https://www.skatteetaten.no/nn/bedrift-og-organisasjon/arbeidsgiver/a-meldinga/rettleiinga-til-a-meldinga/lonn-og-ytingar/oversikt-over-lonn-og-andre-ytingar/styrehonorar-og-godtgjersler-i-samband-med-verv) |
| Feriepenger og OTP av styrehonorar | Nei, prosenttrekk. Egen arbeidsforholdstype (frilanser/oppdragstaker/honorar). | [R1-C] |
| Skattefri organisasjon | Kan markeres fra første krone. Hvis ikke, gjelder en grense på 10 000 kr per mottaker per år for opplysningsplikt og trekk. AGA beregnes av all lønn. | [P] (Skatteetaten-siden over), [R1-D] |
| Minstegrenser for forskuddstrekk | Trekk ≤ 100 kr per måned. Ytelser ≤ 500 kr per måned eller ≤ 2 000 kr per år. | [R1-C] |
| Honorar til frilanser eller oppdragstaker som ikke er næringsdrivende | Lønn med prosenttrekk og AGA, uten feriepenger og OTP. Næringsdrivende som fakturerer, hører ikke hjemme i lønn. | [R1-C] |
| Frivillige | Utlegg mot bilag er ikke lønn | [R1-D] |
| **Frikjøp** | Arbeidsgiveren fakturerer organisasjonen, og personen får vanlig lønn fra egen arbeidsgiver. Det er altså ikke lønn hos organisasjonen. | [V/U] Vanlig praksis etter hovedavtalene. Ikke verifisert i primærkilde. |
| **Tapt arbeidsfortjeneste** utbetalt direkte til personen | Skattepliktig og trekkpliktig. Det er ikke verifisert om riktig a-meldingsbeskrivelse er «verv» eller en annen. Kan være næringsinntekt når mottakeren er selvstendig næringsdrivende. | **[U]** Skatteetatens side om verv nevner det ikke. |
| Ekstrahjelp og tilkallingsvakter | Midlertidig arbeidsforhold uten fast stillingsprosent, timelønn, feriepenger, OTP fra første krone | [R1-C] |
| Utenlandske artister | Egne regler (artistskatt) | [U] Utenfor lansering |
| Offentlig tjenestepensjon (KLP/SPK) | Vanlig hos ideelle og HUK-virksomheter, med fil eller kvartalsrapportering | [R1-D] Relevant for OrgLab-kunder |

### 1.5 Prioritering (MoSCoW) og tidsakse

Tidsaksen følger F: pilot i parallellkjøring oktober–desember 2027, første produksjon januar 2028 [R1-F].

| Klasse | Betyr |
|---|---|
| **Må** | På plass før den første pilotkunden med denne integrasjonen går i parallellkjøring |
| **Bør** | Innen omtrent 6 måneder etter første produksjon |
| **Kan** | Når konkret etterspørsel fra kunder finnes |
| **Ikke nå** | Bevisst utsatt, med en utløser for når det skal vurderes på nytt |

**ID-serier:**

| Serie | Gjelder |
|---|---|
| OK-01–19 | Felles behov |
| OK-20–39 | Utleggsappen |
| OK-40–59 | OrgLab |
| OK-60–79 | Tikket |
| OK-80–109 | Tredjeparter |
| OK-110–119 | Unified API og innebygd lønn |
| OK-120–139 | Kundens IT |
| OK-140–159 | AI-agent |
| OK-160–169 | Bruttos egne modulteam |
| OK-170–189 | Huma og erstatning |

---

## 2. Felles byggeklosser

Alle kontraktene i kapittel 4 bygger på disse sju byggeklossene. Brutto må bygge dem uansett. Det reduserer integrasjonsarbeidet til å «bruke byggeklossene riktig».

### 2.1 Installasjon og tilgangspakker (tilkobling per kunde)

**Flyt:**
1. Utvikleren registrerer en app med `client_id` og `private_key_jwt`.
2. Kundens administrator eller byrå installerer appen. Det skjer med OAuth 2.0 authorization code og en samtykkeskjerm som viser pakker, formål og databehandlerinformasjon.
3. Pakker med skrivetilgang krever step-up med passkey eller BankID.
4. **Organisasjonsnummersjekk:** Kontoen appen kobler fra, må høre til samme juridiske enhet eller kundekonto som Brutto-tenanten. Det hindrer at OrgLab-kontoen til organisasjon A kobles til lønna til organisasjon B. (B)
5. Eventuelle konflikter i kilderegisteret (2.2) må løses før installasjonen aktiveres.
6. **Skyggemodus** er standard i første lønnsperiode (B). Se 4.0.6.
7. Installasjonen opprettes. Driften skjer med client credentials-token som inneholder `installation_id`. Begge sider kan trekke tilbake tilgangen, og da sendes hendelsen `installation.revoked`.

**Byrå:** Et byrå kan installere en app for en klient bare når byrået har oppdrag hos klienten og delegering til saksbehandleren [R1-E]. Klienten ser installasjonen og kan trekke den tilbake.

**Tilgangspakker (revidert fra G 1.9):**

| Pakke | Gir | Typiske brukere |
|---|---|---|
| `virksomhet.les` | Orgnr, underenheter, dimensjoner, lønnskalender | Alle |
| `ansatt.basis.les` | Bruttos personId, navn, e-post, ansattnr, arbeidsforhold (aktiv/ikke), underenhet, avdeling, leder | Utlegg, tid, unified API |
| `engasjement.forespørre` | Be Brutto etablere en mottaker eller et arbeidsforhold (2.4) | OrgLab, Tikket |
| `lønnsgrunnlag.skrive:<datatype>` | Skrive egne linjer for datatyper der installasjonen er kilde | Alle kilder |
| `lønnsgrunnlag.status` | Status, utbetaling og innrapportering for egne linjer | Alle kilder |
| `fravær.skrive` / `fravær.helse` | Fravær. Med `helse` også sykefraværstyper og grad (GDPR art. 9), aldri diagnose. | Fraværskilder (Huma, egen modul) |
| `hr.skrive:<attributtgruppe>` | Masterdata der installasjonen er kilde (person, arbeidsforhold-HR, organisasjon, avtalt lønn) | HR-systemer (Huma) |
| `identitet.foreslå` | Foreslå fødselsnummer. Lagres som *uverifisert*. | HR-systemer |
| `identitet.les` | Lese fødselsnummer | Pensjon, forsikring |
| `dimensjon.skrive:<type>` | Opprette dimensjonsverdier av en bestemt type (for eksempel `arrangement`) | Tikket |
| `kostnad.aggregert.les` | Lønnskostnad per dimensjon, med minste gruppestørrelse | Tikket, BI |
| `lønnsresultat.individ.les` | Lønnsslippdata | Ansattportal-partnere, pensjon |
| `bilag.les` | Posteringer per lønnskjøring | ERP-integratører |
| `agent.utkast` | AI-agent: lese og lage utkast (7) | MCP-klienter |
| *(ingen)* | **Kontonummer kan aldri skrives via integrasjon** (B) | – |

### 2.2 Kilderegisteret: én kilde til sannhet per datatype per kunde (B, utvidet etter nytt gründerkrav)

**Regel:** For hver kombinasjon av (tenant, datatype, omfang, dato) finnes nøyaktig **én** aktiv kilde.

- **Kilde** er enten en Brutto-modul (som også er en installasjon med egen klient, se kapittel 5) eller en installert app.
- **Omfang** er hele tenanten, en juridisk enhet eller en *arbeidsforholdsgruppe* (for eksempel «faste», «ekstrahjelp» eller «honorar/verv»). Omfangene kan ikke overlappe.
- Eierskapet har gyldighetsdato, så historikken viser hvem som var kilde når.

| Datatype | Mulige kilder | Kan eierskapet flyttes? | Merknad |
|---|---|---|---|
| `PERSON_BASIS` (navn, kontakt, adresse) | Brutto, HR-system | Ja | |
| `IDENTITET` (fødselsnr/D-nr) | Brutto (BankID eller verifisert via skattekort). HR-system kan bare *foreslå*. | **Nei** | Feil fødselsnummer går rett i a-meldingen |
| `ARBEIDSFORHOLD_HR` (start/slutt, stilling %, kontraktstype, tittel, prøvetid, sluttårsak) | Brutto, HR-system | Ja | |
| `ARBEIDSFORHOLD_AMELDING` (yrkeskode, arbeidstidsordning, underenhet, arbeidsforholdstype) | Brutto (standard), HR-system | Ja | Brutto validerer alltid mot a-meldingsreglene |
| `ORGANISASJON` (avdeling, team, lokasjon, leder) | Brutto, HR-system | Ja | |
| `AVTALT_LØNN` (fastlønn eller timesats med fra-dato) | Brutto, HR-system (lønnsrevisjon) | Ja | |
| `BANKKONTO` | Bare Brutto (ansattportal med BankID) | **Nei** | Svindel med endret kontonummer [R1-F] |
| `SKATTEKORT` | Bare Brutto (Skatteetaten) | **Nei** | |
| `FRAVÆR` | Brutto Fravær, HR-system (Huma), tid/vakt-system | Ja | |
| `TID` (timer, overtid, tillegg) | Brutto Timer, Planday-type, Tikket (vakter) | Ja | Typisk delt etter arbeidsforholdsgruppe |
| `UTLEGG_REISE` | Brutto Utlegg, Utleggsappen, Pleo-type, OrgLab (for verv) | Ja | |
| `VERV_HONORAR` | OrgLab, Brutto (manuelt) | Ja | |
| `DOKUMENT:<type>` (arbeidsavtale, …) | Brutto dokumentlager, HR-system | Ja, per dokumenttype | Brukes i Huma-erstatningen |
| Lønnsarter, beregning, a-melding, lønnsresultat | Bare Brutto | **Nei** | |

**Slik håndheves regelen:**
- Skriving fra en annen enn kilden gir HTTP 409 `NOT_SOURCE_OF_TRUTH` med lenke til gjeldende kilde. For lønnsgrunnlag brukes `CATEGORY_OWNED_BY_OTHER_SOURCE`.
- **Bruttos eget skjermbilde følger den samme regelen.** Når Huma eier `ARBEIDSFORHOLD_HR`, er feltene skrivebeskyttet i Brutto og har en lenke «Endre i Huma».
- Alle med riktig pakke kan lese.
- Kildebytte er beskrevet i 5.2.

### 2.3 Personmatching og ID-kobling

- `POST /person-links:match` tar imot hint (e-post, ansattnr, og fødselsnummer bare med `identitet.*`) og returnerer kandidater med treffsikkerhet.
- Koblingen skjer automatisk bare ved ett eksakt treff på ansattnr eller på e-post verifisert gjennom kundens IdP. Ellers går den til en **koblingskø** som et menneske behandler i Brutto.
- Koblingen lagres per installasjon: `(installationId, externalPersonRef) → personId (+ standard employmentId)`.
- **Personer slås aldri sammen automatisk.** Brutto oppretter aldri en ny person når det finnes et mulig treff. (B)

### 2.4 Engasjement med innebygd mottaker-onboarding («honorar-lenke») – ny byggekloss

Et **engasjement** er et verv, et honoraroppdrag eller en ekstrahjelp-relasjon som en kilde ber Brutto etablere. Brutto eier alltid arbeidsforholdet som engasjementet fører til.

```
Kilde: POST /engagements ─▶ REQUESTED
   ├─ personen finnes og er koblet ─────────────────────────────▶ DRAFT_EMPLOYMENT
   └─ personen er ukjent ─▶ INVITED (lenke på e-post/SMS fra Brutto)
          └─ personen: BankID → bekrefter konto → svarer «fakturerer du via eget foretak?»
                ├─ ja ─▶ NOT_PAYROLL (kilden må bruke faktura)
                ├─ skattemessig bosatt i utlandet ─▶ MANUAL_REVIEW
                └─ nei ─▶ DRAFT_EMPLOYMENT
DRAFT_EMPLOYMENT ─(lønnsansvarlig godkjenner, eller kundens auto-regel for VERV/HONORAR)─▶ ACTIVE ─▶ ENDED
                                                    (Brutto henter skattekort ved ACTIVE)
```

- **Typer:**
  - `VERV` gir et arbeidsforhold av typen frilanser/oppdragstaker/honorar
  - `HONORAR` gir samme type
  - `EKSTRAHJELP` gir et ordinært, midlertidig timelønnet arbeidsforhold. Brutto gjenbruker et løpende arbeidsforhold per person og juridisk enhet når det finnes et.
- **Hvorfor:** Kilden trenger aldri å samle inn fødselsnummer eller kontonummer. Det fjerner den vanligste feilen («skjema på e-post») og den vanligste svindelveien.

### 2.5 Lønnsgrunnlag v2 (PayInput)

Dette er den felles skrivekontrakten for *beløp og mengder*: utlegg, reise, timer, vakter, honorarer og godtgjørelser. Detaljene står i 4.0.

### 2.6 Fravær v1 (Absence) – ny ressurs (B)

Fravær er fakta med lønnskonsekvenser, ikke et beløp. Kilden sender fraværet. Brutto beregner konsekvensene: ferietrekk, lønn i arbeidsgiverperioden, refusjonskrav og inntektsmelding til NAV, og permisjonsopplysninger i a-meldingen [R1-B, R1-C].

| Felt | Innhold |
|---|---|
| `externalId`, `revision` | Som for lønnsgrunnlag |
| `employmentId` (eller `externalPersonRef` + Bruttos valg) | |
| `type` | Fra katalog: `FERIE`, `EGENMELDING`, `SYKMELDING`, `SYKT_BARN`, `PERMISJON_MED_LØNN`, `PERMISJON_UTEN_LØNN`, `FORELDREPERMISJON`, `PERMITTERING`, `VELFERD`, `ANNET`. Sykefraværstyper krever `fravær.helse`. |
| `from`, `to`, `grade` (0–1), eventuelt `hoursPerDay` | |
| `status` | Bare godkjent fravær påvirker lønn. Tilbaketrukket eller avvist fravær sendes som revisjon med `CANCELLED`. |
| `reference` | For eksempel sykmeldings-ID. **Aldri diagnose.** |
| `approval` | Hvem som godkjente og når |

Låsing og korrigering følger de samme reglene som lønnsgrunnlag (4.0.3–4.0.4). Fravær som registreres etter låsing, gir korrigeringslinjer i neste kjøring.

### 2.7 Hendelser og webhooks (forenklet fra G 1.6)

- **Retning:** Kilder skriver via REST og sender ikke egne hendelser til Brutto. Brutto sender ut webhooks. (B)
- **Format:** Feltnavn etter CloudEvents i JSON. Signering, `webhook-id` og tidsstempel etter Standard Webhooks [R1-G].
- **Levering:** Minst én gang. Brutto prøver igjen med eksponentiell backoff i inntil 72 timer, og kunden kan se køen over feilede leveranser.
- **Endringsstrøm:** `GET /events?after=<sequence>` er fasiten. Webhooks er bare varsling.
- **Sensitive data:** Beløp per person og fødselsnummer sendes aldri i hendelser til apper uten pakke for dette. Da sendes en tynn hendelse, og innholdet hentes via API.

### 2.8 Lønnskalender og cut-off

- `GET /pay-calendar` gir perioder, cut-off-tidspunkt, utbetalingsdato og a-meldingsmåned per juridisk enhet og lønnsfrekvens.
- Hendelser: `pay_period.cutoff_scheduled`, `pay_period.cutoff_passed`, `pay_period.closed`.
- Tid-, fravær- og utleggssystemer bruker dem til å låse timelister og vise frister til brukerne.

---
## 3. Personas: jobs to be done, behov, MoSCoW og «kult i 2026»

### 3.0 Felles behov for alle som bygger mot Brutto

| ID | Behov | MoSCoW | Kommentar |
|---|---|---|---|
| OK-01 | Ett offentlig REST-API (OpenAPI 3.1) som dekker alt egne moduler og søsterprodukter trenger | **Må** | Plattformprinsipp 1 |
| OK-02 | Selvbetjent appregistrering med OAuth 2.0 (authorization code for installasjon, client credentials med `private_key_jwt` for drift) | **Må** | |
| OK-03 | Installasjon per kunde med tilgangspakker, samtykkeskjerm, tilbaketrekking og hendelser | **Må** | 2.1 |
| OK-04 | Selvbetjent sandkasse med syntetiske data og «tidsmaskin» som kan utløse cut-off, godkjenning, betaling og a-meldingskvittering | **Må** | Det viktigste DX-tiltaket (kap. 8) |
| OK-05 | Idempotens på all skriving: `Idempotency-Key` og naturlig nøkkel (installasjon, eksternId, revisjon) | **Må** | 4.0.2 |
| OK-06 | Maskinlesbare årsakskoder med forklaring på norsk og engelsk og lenke til dokumentasjon | **Må** | 4.0.5 |
| OK-07 | Webhooks med signering, retry, leveringslogg og manuell replay, i tillegg til endringsstrøm | **Må** | 2.7 |
| OK-08 | API for lønnskalender og cut-off | **Må** | 2.8 |
| OK-09 | Batch-endepunkt (opptil 1 000 linjer) med delvis suksess per linje | **Må** | |
| OK-10 | Publiserte grenser for antall kall per installasjon, med `RateLimit`-headere og 429 + `Retry-After` | **Må** | Like for alle |
| OK-11 | Versjonering: bare tillegg innen hovedversjon, minst 12 måneders avvikling, `Deprecation`/`Sunset`-headere og endringslogg | **Må** | |
| OK-12 | Endepunkt som bare validerer (dry-run) med de samme reglene som ved mottak | **Må** (B) | Billig fordi det er samme kode. Brukes av utleggsapper før direkte refusjon og av integratører i test. |
| OK-13 | Forespørselslogg per installasjon (30 dager) med korrelasjons-ID, synlig for utvikler og kunde | Bør | |
| OK-14 | Statusside og varsling. Planlagt vedlikehold aldri i lønnsuka. | **Må** | |
| OK-15 | Sandkasse og produksjon skilt med egne vertsnavn og nøkkelprefiks (`sk_test_`) | **Må** (B) | Hindrer at testdata havner i a-meldingen |
| OK-16 | Engelsk dokumentasjon | Bør | Unified-API-leverandører og internasjonale HR-systemer |
| OK-17 | Maskinlesbar katalog over linjetyper (kind) og fraværstyper. JSON Schema per type med påkrevde fakta. | **Må** (B) | Erstatter at kildene sender a-meldingskoder |
| OK-18 | API for personmatching og koblingskø | **Må** | 2.3 |
| OK-19 | Skyggemodus for nye installasjoner og beløpsgrenser per linjetype | **Må** (B) | 4.0.6 |

**Kult i 2026 (felles):**
- **«Tidsmaskin» i sandkassen.** Integratøren ser hele livsløpet fra mottatt til innrapportert på fem minutter i stedet for å vente en måned.
- **llms.txt og dokumentasjon i markdown,** slik at utviklernes kodeagenter kan bygge integrasjonen.
- **Integrasjonsrapport til kunden:** «Dette har hver app gjort i november.»

---

### 3.1 Persona 1: Utvikler eller produkteier i Utleggsappen

**Hvem:** Et eget selskap med drift hos Advania i Norge. Det har egen godkjenningsflyt, kvitteringer og policymotor. Kundene bruker også andre lønnssystemer, så Utleggsappen har allerede adaptere mot Tripletex, PowerOffice og Visma. Den vil at Brutto skal være like enkel å koble mot, eller enklere. **Bruttos egen utleggsmodul er en direkte konkurrent** (1.3).

**Jobs to be done:**
1. *Når* et krav er godkjent, *vil jeg* få det riktig utbetalt og innrapportert uten at økonomi taster noe, *så* den ansatte får pengene og arbeidsgiveren følger reglene.
2. *Når* Brutto avviser eller endrer noe, *vil jeg* vise den ansatte og godkjenneren hvorfor, på et språk de forstår.
3. *Når* kravet er utbetalt og innrapportert, *vil jeg* lukke det med status «utbetalt dd.mm, innrapportert».
4. *Når* et krav må rettes etter utbetaling, *vil jeg* sende riktig versjon og stole på at Brutto håndterer differansen lovlig.
5. *Når* en ny kunde kobler seg til, *vil jeg* at det tar minutter, også når kunden har et byrå.

| ID | Behov | MoSCoW | Kommentar |
|---|---|---|---|
| OK-20 | Godkjente reise- og utleggslinjer leveres som lønnsgrunnlag med fakta og totalbeløp. Brutto klassifiserer. | **Må** | 4.1 |
| OK-21 | Brutto splitter selv trekkfri og trekkpliktig del av kilometergodtgjørelse og diett fra én linje | **Må** | [R1-C] |
| OK-22 | API for satsoppslag (statens satser og trekkfrie satser per dato), slik at Utleggsappen viser samme beløp som Brutto | Bør | Færre overraskelser |
| OK-23 | Obligatorisk felt for fordel («privat kostnad dekket av arbeidsgiver») uten standardverdi | **Må** (B) | Ellers blir det feilrapportering |
| OK-24 | Status per linje: utsatt, sen endring, låst, utbetalt (sendt eller bekreftet) og innrapportert | **Må** | 4.0.7 |
| OK-25 | Korrigering ved at kilden sender full tilstand. Brutto beregner differansen. | **Må** (B) | 4.0.4 |
| OK-26 | Negativ differanse stoppes inntil det finnes trekkavtale eller tilbakebetaling (aml. § 14-15) | **Må** for stoppet, Bør for e-signert avtaleflyt | [R1-G] |
| OK-27 | Planlagt utleggskjøring (for eksempel en ekstra kjøring hver uke) | Bør | |
| OK-28 | Kvitteringsreferanse (krav-ID og sha256) på linjen og i bilaget | **Må** | Hvem som skal arkivere, er et åpent spørsmål (kap. 10) |
| OK-29 | Valuta: originalbeløp, valuta, kurs, kursdato og NOK-beløp | **Må** | |
| OK-30 | Utenlandsdiett med ISO-landkode | Bør | |
| OK-31 | Dimensjoner (avdeling, prosjekt) validert mot Bruttos dimensjonsregister | **Må** | |
| OK-32 | Dry-run-klassifisering før direkte refusjon. Svaret `reportable=false` betyr at linjen ikke skal til lønn. | Bør | Rammene for vei B |
| OK-33 | Direkte utbetaling av opplysningspliktige linjer med reservasjon i to faser | **Ikke nå** (B) | Utløser: mer enn 3 kunder ber om det og mønsteret er testet |
| OK-34 | Duplikatsjekk på tvers av kilder med kvitterings-hash | Bør | Fanger for eksempel at samme reise er sendt fra OrgLab og fra Utleggsappen |

**Kult i 2026:**
- **«Utlegg på konto i dag»:** Rene refusjoner betales med straksbetaling fra Utleggsappen. Det som skal i a-meldingen, går via Brutto.
- Den ansatte ser **«Innrapportert til Skatteetaten 07.12»** i appen og vet at alt er gjort riktig.
- Den samme kvitteringen oppdages hvis den er sendt to ganger.

---

### 3.2 Persona 2: Utvikler i OrgLab (medlemshåndtering)

**Hvem:** Medlemssystem for fagforeninger, interesseorganisasjoner, idrett og frivillige organisasjoner. Systemet har:
- medlemmer
- verv (rolle, organ og periode)
- vedtak om honorarsatser
- møter og deltakelse

Kundene har typisk 10–200 ansatte, men mange honorarmottakere. Mange er skattefrie organisasjoner, bruker byrå og har KLP eller tilsvarende pensjon.

**Jobs to be done:**
1. *Når* årsmøtet eller styret har vedtatt honorar for vervene, *vil jeg* at riktige personer får riktig beløp til riktig tid, uten at kassereren lager regneark til byrået.
2. *Når* en tillitsvalgt har vært i møte eller tatt fri uten lønn, *vil jeg* kunne utløse møtegodtgjørelse eller tapt arbeidsfortjeneste med dokumentasjon.
3. *Når* noen får et nytt verv, *vil jeg* at personen blir klar for utbetaling uten at organisasjonen samler inn fødselsnummer og kontonummer på e-post.
4. *Når* et verv avsluttes, *vil jeg* at utbetalingene stopper og at arbeidsforholdet avsluttes i a-meldingen.
5. *Når* organisasjonen kjøper fri en tillitsvalgt, *vil jeg* at refusjonen til arbeidsgiveren går til regnskap og ikke til lønn.

| ID | Behov | MoSCoW | Kommentar |
|---|---|---|---|
| OK-40 | Engasjement av typen VERV med innebygd mottaker-onboarding (BankID, kontonummer, spørsmålet «fakturerer du?») | **Må** | 2.4 |
| OK-41 | Når et verv avsluttes, avsluttes arbeidsforholdet. Endringen er et utkast som godkjennes. | **Må** | |
| OK-42 | Linjetypene `BOARD_FEE` (styrehonorar og godtgjørelse for verv) og `MEETING_FEE` | **Må** | [P] |
| OK-43 | Linjetypen `LOST_EARNINGS` (tapt arbeidsfortjeneste) | Bør | **[U]** a-meldingsbeskrivelsen må avklares faglig før lansering |
| OK-44 | Frikjøp avvises med `NOT_PAYROLL` og veiledning om å bokføre det som leverandørfaktura | **Må** (B) | Ellers dobbel inntekt i a-meldingen |
| OK-45 | Skattefri organisasjon: Brutto holder 10 000 kr-akkumulatoren og merkingen. **OrgLab bruker aldri grensen selv.** | **Må** | [P] |
| OK-46 | Minstegrenser for trekk, og AGA-fritak for veldedige og allmennyttige organisasjoner, i Brutto | Bør | [R1-D] |
| OK-47 | Brutto fungerer for kunder med bare honorarer og ingen ordinære ansatte, med en enkel pris | **Må** | Stort segment av OrgLab-kunder |
| OK-48 | Konfidensielt styrehonorar, synlig bare for navngitte brukere i Brutto | Bør | [R1-D] |
| OK-49 | OrgLab kan *be om* en honorarkjøring. Brutto foreslår, og et menneske starter kjøringen. | Bør | En kommando, ikke en hendelse [R1-G 1.12] |
| OK-50 | OrgLab kan levere reise og diett for tillitsvalgte bare hvis den er kilde for `UTLEGG_REISE` for gruppen «honorar/verv» | **Må** (B) | Kilderegisteret |
| OK-51 | Dimensjoner (lag, krets, utvalg) på honorarlinjer | Bør | |
| OK-52 | Mottaker som er skattemessig bosatt i utlandet stoppes og behandles manuelt | **Må** som stoppregel | Full støtte er «Ikke nå» |
| OK-53 | Frikjøpsgrunnlag: Brutto beregner full kostnad (lønn, feriepenger, AGA og pensjon) for en *egen* ansatt som er frikjøpt, som grunnlag for faktura | Kan | Kult |
| OK-54 | Sum utbetalt per verv og år tilbake til OrgLab (egne linjer, uten trekk) | Bør | Til kasserer og revisor |
| OK-55 | OrgLab som kilde for HR-data om organisasjonens ansatte, via `hr.skrive` på samme vilkår som andre | Kan | OrgLab er ikke HR-master som standard |

**Kult i 2026:**
- **«Honorar på 60 sekunder»:** Den tillitsvalgte får en lenke, logger inn med BankID, bekrefter kontonummeret og ser forventet netto etter trekk. Styret godkjenner honorarlisten i OrgLab, og Brutto kjører.
- Vervsperioden styrer arbeidsforholdet automatisk, så «glemte» honorarmottakere ligger ikke igjen i a-meldingen.

---

### 3.3 Persona 3: Utvikler i Tikket (billett og arrangement)

**Hvem:** Kulturhus, festivaler, idrettslag, konferansearrangører og foreninger. Kundene har disse gruppene:
- faste ansatte (i Brutto Timer eller Planday)
- ekstrahjelp og vakter (garderobe, bar, scene, vakthold)
- ulønnede frivillige
- artister og foredragsholdere (honorar eller faktura)
- mannskap fra bemanningsbyrå (faktura)

**Jobs to be done:**
1. *Når* et arrangement er gjennomført og vaktene er bekreftet, *vil jeg* sende timene for ekstrahjelpen til lønn, *så* de får betalt på neste lønningsdag.
2. *Når* jeg rekrutterer ekstrahjelp, *vil jeg* at de blir klare for lønn uten papirskjema.
3. *Når* en artist skal ha honorar, *vil jeg* vite om det skal gå som lønn eller faktura.
4. *Når* lønna er kjørt, *vil jeg* se den faktiske lønnskostnaden per arrangement, med feriepenger og AGA.
5. *Når* en vakt endres etter at den er sendt, *vil jeg* rette den uten å skape dobbel betaling.

| ID | Behov | MoSCoW | Kommentar |
|---|---|---|---|
| OK-60 | Linjetypen `SHIFT` med **tidsstempler** for start og slutt, pause, rolle, arrangement og sted. Brutto priser vakten (timesats, kvelds- og helgetillegg). | **Må** (B) | Tidsstempler i stedet for antall timer fjerner feil med enheter |
| OK-61 | Bare vakter bekreftet av vaktleder (`approvedBy`, metode). Brutto betaler aldri ugodkjent tid. | **Må** | [R1-G] |
| OK-62 | Engasjement av typen EKSTRAHJELP. **Brutto velger eller oppretter ett løpende arbeidsforhold** per person og juridisk enhet, ikke ett per arrangement. | **Må** (B) | Ellers kommer det støy og feil i a-meldingen |
| OK-63 | Linjetypen `FEE_ASSIGNMENT` (honorar for oppdrag) med sjekk av om det skal være lønn eller faktura | **Må** | 2.4 |
| OK-64 | Tikket kan opprette dimensjonsverdier av typen `arrangement`, som Brutto tar med til bilaget | **Må** (B) | Ellers blir kostnaden per arrangement stille feil |
| OK-65 | Lønnskostnad per arrangement tilbake (sum, feriepengeavsetning, AGA og pensjon), med minste gruppestørrelse | Bør | Personvern: én artist alene avslører individuell lønn |
| OK-66 | Estimat av hva vaktplanen koster, via simulerings-API | Kan | Kult |
| OK-67 | Frivillige er ikke lønn. Honorar til frivillige går via engasjement, og Brutto holder grensene. | **Må** som regel | |
| OK-68 | Utenlandske artister og artister via byrå avvises (`UNSUPPORTED_TAX_REGIME` / `NOT_PAYROLL`) | **Må** som stoppregel | [U] artistskatt |
| OK-69 | Tåler toppvolum i helger og festivaler: batch med 1 000 vakter og kortvarige topper i kallraten | **Må** | |
| OK-70 | Kilderegister for `TID` per arbeidsforholdsgruppe, og sjekk av overlappende vakter på tvers av kilder | **Må** (B) | For eksempel Tikket for ekstrahjelp og Planday for faste |
| OK-71 | Linjetypen `SHIFT_FIXED` (fast sats per vakt) | Bør | Vanlig i kulturhus |
| OK-72 | Fribilletter som godtgjørelse | **Ikke nå** | [U] skattespørsmål |

**Kult i 2026:**
- **«Fra vakt til lønnsslipp på én dag»:** Ekstrahjelpen sjekker inn og ut med QR, vaktlederen bekrefter, og Brutto kjører.
- **Dekningsbidrag per arrangement** med reell lønnskostnad.
- Lønnsslippen viser hvilket arrangement timene gjelder.

---

### 3.4 Persona 4: Tredjeparter (tid/vakt, HR, ERP, pensjon og bank)

**Tid og vakt** (Planday, Tamigo, Quinyx, GAT). I dag eksporterer de mest CSV i lønnssystemets format [R1-D].

**Jobs to be done:**
- Levere godkjente timer per periode med minimalt med mapping.
- Vite når cut-off er.
- Få avvisninger per linje.

| ID | Behov | MoSCoW |
|---|---|---|
| OK-80 | Linjetypene `TIME_HOURS` og `SHIFT`, med leverandørens egne koder (`sourceCode`) koblet til lønnsarter i en mappingtabell per installasjon i Brutto | **Må** |
| OK-81 | CSV-import som reserve, med samme validering og idempotens (filhash og linjenøkkel) og **flere importer per kjøring** (Tripletex kritiseres for bare én [R1-D]) | **Må** |
| OK-82 | Hendelser for cut-off og lås, slik at timelister kan låses | **Må** |
| OK-83 | Fravær via fravær v1 (når tidssystemet er kilde for `FRAVÆR`) | Bør |
| OK-84 | Saldoer tilbake (ferie, avspasering) | Kan |
| OK-85 | Kostnadsestimat per vakt (simulering) | Kan |

**HR-systemer** (Huma, Simployer, Sympa, HiBob, Personio). Huma er beskrevet i detalj i 4.4.

**Jobs to be done:**
- Være master for person og arbeidsforhold.
- Få feil mot a-meldingsreglene allerede ved registrering.

| ID | Behov | MoSCoW |
|---|---|---|
| OK-86 | API for arbeidsforhold med gyldighetsdato (bitemporalt), skriving per attributtgruppe der appen er kilde | **Må** (B), fordi Huma-kunder er i målgruppen |
| OK-87 | Endepunkt som validerer mot a-meldingsreglene (yrkeskode, stillingsprosent, arbeidstidsordning) | Bør |
| OK-88 | Hendelser tilbake: `employment.validation_failed`, `employment.payroll_ready` | Bør |
| OK-89 | Nyansatt-flyt: Brutto henter skattekort og ber den ansatte om kontonummer via BankID | **Må** |

**ERP og regnskap** (Tripletex, PowerOffice Go, Business Central, Xledger). Tripletex og PowerOffice er også konkurrenter innen lønn, så bruk bare deres offentlige API-er.

| ID | Behov | MoSCoW |
|---|---|---|
| OK-90 | Brutto bygger og drifter adaptere for Tripletex og PowerOffice Go, som skyver bilag [R1-G B4] | **Må** |
| OK-91 | Generisk pull-API for bilag (`GET /journal-entries?payRun=`) som balanserer, med dimensjoner, referansen `payrun:<id>:rev<n>` og reversering ved ny revisjon | **Må**. Gjør at konsulenter kan koble på BC og Xledger. |
| OK-92 | Synkronisering av kontoplan og dimensjoner | **Må** |
| OK-93 | Filformat som reserve (CSV eller Excel per ERP) | **Må** |
| OK-94 | Tilbakemelding om at bilaget er bokført | Bør |
| OK-95 | Avstemmingsdata (a-melding mot bokført) | Bør |

**Pensjon og bank**

| ID | Behov | MoSCoW |
|---|---|---|
| OK-96 | OTP via a-meldingen (ingen egen integrasjon) | **Må** |
| OK-97 | Pensjonsgrunnlag til KLP og SPK (fil) | **Må** hvis en pilot er HUK/ideell. Ellers Bør. |
| OK-98 | Satser og medlemskap fra pensjonsleverandøren | Kan |
| OK-99 | Betalingsfil pain.001 (SALA, unike ID-er) og import av pain.002/camt.054 | **Må** |
| OK-100 | Direkte bank-API | Bør |
| OK-101 | Betalingsstatus skilt i *sendt*, *bekreftet* og *returnert*, og synlig for kildene | **Må** (B) |

**Kult i 2026:**
- **Tid uten CSV:** En Planday-kunde kobler til på fem minutter med en mappingveiviser der AI foreslår lønnsart per kode.
- **Bilaget lenker tilbake til forklaringen** av hver linje (glassboks [R1-G #3]).

---

### 3.5 Persona 5: Unified-API-leverandører og «embedded payroll»-kunder

**Unified API** (Kombo, Merge, Finch, Apideck).

**Jobs to be done:**
- Legge til «Norway payroll – Brutto» som kobling med minimalt spesialarbeid.
- Lese ansatte, arbeidsforhold, lønnskjøringer og sammendrag av lønnsslipper for sine kunder (forsikring, pensjon, fordeler, HR-apper).
- Senere: skrive trekk.

**Embedded payroll** (bransjesystemer for bygg, renhold, frisør og helse).

**Job to be done:** Tilby norsk lønn i sitt eget produkt.

| ID | Behov | MoSCoW | Kommentar |
|---|---|---|---|
| OK-110 | Lese-API for ansatte, arbeidsforhold, organisasjon, lønnskjøringer og sammendrag av lønnsslipper, med `updated_since` | Bør | Dekkes stort sett av OK-01 |
| OK-111 | Partnerapp som mange kunder kan installere, med én partneravtale | Bør | Samme mekanisme som 2.1 |
| OK-112 | Engelsk dokumentasjon og tabell som mapper mellom datamodellene (arbeidsforhold → employment …) | Bør | |
| OK-113 | Skriving av avtalte trekk (for eksempel egenandel for forsikring) med flagg for skriftlig avtale | Kan | aml. § 14-15 |
| OK-114 | Partnervilkår om formålsbegrensning og databehandlerkjede ved videre deling | Bør | |
| OK-115 | Opprette tenant via API (juridisk enhet hentes fra Brønnøysund) | Kan | Byråer trenger det også |
| OK-116 | Vertsbaserte flyter med retur-URL og logo (systembruker-veiviser, mottaker-onboarding) | Kan | |
| OK-117 | Grossistfakturering og white-label | **Ikke nå** | År 2–3 [R1-G] |
| OK-118 | Iframe- eller React-komponenter | **Ikke nå** | |

**Kult i 2026:** **«Norsk lønn som én kobling»** hos Kombo og Merge gir rekkevidde mot hundrevis av HR-, forsikrings- og pensjonsapper uten at Brutto bygger noe ekstra.

---

### 3.6 Persona 6: Kundens IT-ansvarlige eller integrasjonskonsulent

**Jobs to be done:**
- Godkjenne leverandøren (sikkerhet, databehandleravtale, underleverandører).
- Koble på SSO og brukerprovisjonering.
- Ha oversikt over og kontroll med hvilke apper som har hvilke data.
- Feilsøke integrasjoner raskt.
- Få data inn (migrering) og ut (exit).

| ID | Behov | MoSCoW | Kommentar |
|---|---|---|---|
| OK-120 | SSO med OIDC mot Entra ID og Google, mulighet for å kreve SSO per tenant. Step-up med BankID eller passkey beholdes for kritiske handlinger. | **Må** (OIDC), Bør (SAML) | [R1-F] |
| OK-121 | SCIM 2.0 for brukere, med mapping fra gruppe til rolle | Bør | |
| OK-122 | Installasjonsoversikt: alle apper og Brutto-moduler, pakker, hvem som godkjente, siste aktivitet, tilbaketrekking | **Må** | |
| OK-123 | **Integrasjonsmonitor:** mottatt, avvist, holdt og utsatt per kilde og periode, med årsak | **Må** (B) | Den eneste måten å se feil før a-meldingen |
| OK-124 | Eksport av revisjonsloggen (API, SIEM) inkludert API-handlinger per installasjon | Bør | |
| OK-125 | Sikkerhetspakke: databehandleravtale, underleverandørliste, datakart (inkludert AI), sammendrag av pentest, plan for ISAE 3402 | **Må** | [R1-F] |
| OK-126 | Kundens egen integrasjon (en app kunden eier, med begrenset tilgang, for eksempel for Power BI) | Bør | |
| OK-127 | Full dataeksport og exit | **Må** | |
| OK-128 | IP-allowlist for API-klienter | Kan | |
| OK-129 | Anonymisert sandkassekopi av egen tenant | Kan | Personvernrisiko [R1-G #31] |
| OK-130 | Mappingverktøy for lønnsarter, dimensjoner, ansattnumre og fraværstyper, med CSV inn og ut | **Må** | |
| OK-131 | Publiserte faste IP-adresser for utgående webhooks | Bør | For mottak bak brannmur |
| OK-132 | **Kilderegister i UI:** hvem er kilde for hva, planlagte kildebytter, historikk | **Må** (B) | 2.2 og 5.2 |

**Kult i 2026:** **«Integrasjonsrøntgen»:** Én side som viser alle dataflyter inn og ut, med volumer, feil og hvem som er kilde for hva. Kunden kan slå skyggemodus av og på for en ny integrasjon.

---

### 3.7 Persona 7: AI-agent som bruker

Det finnes to typer:
- **kundenes egne agenter** (Claude, ChatGPT, Copilot via MCP)
- **byråenes agenter**, som jobber på tvers av mange klienter

**Jobs to be done:**
- Hente status og avvik før lønnskjøringen.
- Forklare avvik og lønnsslipper.
- Forberede: lage utkast til lønnsgrunnlag, purre på manglende godkjenninger, lage sjekklister.
- Svare ansatte basert på deres egne data.
- For byrå: prioritere klienter etter risiko.

| ID | Behov | MoSCoW | Kommentar |
|---|---|---|---|
| OK-140 | Agentidentitet: OAuth «på vegne av bruker» med agentflagg. Rettighetene er snittet av brukerens rettigheter og agentpakken. | **Må** i tilgangsmodellen | Billig nå, dyrt å bygge inn senere [R1-F 3.3] |
| OK-141 | Harde grenser i policymodulen: agenten kan aldri godkjenne, sende a-melding, utbetale, endre kontonummer eller roller, eller installere apper | **Må** | [R1-F 5.2] |
| OK-142 | MCP-server oppå det offentlige API-et (lese, forklare, simulere, utkast) | Bør | Tynt lag |
| OK-143 | Agentutkast som kilde: lønnsgrunnlag med `source=agent` og status `DRAFT`. Et menneske godtar endringen i UI og ser forskjellen. | Bør | |
| OK-144 | API som forklarer hver beregnet linje (beregningsspor) | Bør | [R1-F P7] |
| OK-145 | Dataminimering: fødselsnummer, kontonummer og adresse kommer aldri i agentsvar, og verdier maskeres | **Må** | |
| OK-146 | Fritekst fra integrasjoner merkes som uklarert data i verktøysvar (vern mot prompt-injeksjon) | **Må** når OK-142 leveres | |
| OK-147 | Revisjonslogg «agent X på vegne av Y», og kvoter per agent | **Må** når OK-142 leveres | |
| OK-148 | Byrå: lesing av metadata (status, frister, avvik) på tvers av klienter uten persondata | Bør | [R1-F 3.2] |
| OK-149 | Kunden slår på agenttilgang per tenant (opt-in) | **Må** når OK-142 leveres | |

**Kult i 2026:**
- **«Lønnsklar-agent»:** Tre dager før lønning går agenten gjennom alle klienter, purrer på manglende godkjenninger i utleggs- og vaktsystemene og lager en sjekkliste. Mennesket godkjenner i UI.
- **«Spør lønnsslippen».**

---

### 3.8 Persona 8: Bruttos egne modulteam (fravær, timer, utlegg) – nytt

**Hvem:** Teamene som bygger Brutto Fravær, Brutto Timer og Brutto Utlegg. De er de første og viktigste brukerne av det offentlige API-et.

**Jobs to be done:**
1. *Når* jeg bygger en modulfunksjon, *vil jeg* bare bruke offentlige endepunkter, *så* kunden fritt kan bytte modulen ut.
2. *Når* API-et mangler noe, *vil jeg* at det lages offentlig for alle, ikke som et internt unntak.
3. *Når* kunden bytter til et eksternt system, *vil jeg* overlevere data ryddig.

| ID | Behov | MoSCoW | Kommentar |
|---|---|---|---|
| OK-160 | Hver Brutto-modul er en egen app (egen OAuth-klient og installasjon) som er forhåndsinstallert, men synlig og kan slås av | **Må** | 5.3 |
| OK-161 | Byggeregel: modulene kan bare bruke den genererte klienten for det offentlige API-et. Kall til udokumenterte endepunkter stopper bygget. | **Må** | |
| OK-162 | Byttetest i CI: samme scenarioer kjøres med egen modul og med referanseintegrasjonen, og resultatet skal være likt på øret | **Må** | |
| OK-163 | Eksport og overlevering ved kildebytte: åpne saker, saldoer og historikk som signert importbatch | **Må** | 5.2 |
| OK-164 | Åpen referanseintegrasjon (utlegg og timer, for eksempel på GitHub) som modulteamene vedlikeholder | **Må** | Bevis og DX |
| OK-165 | Modulteamene utvikler mot sandkassen med de samme grensene som alle andre | **Må** | |

---
## 4. Integrasjonskontrakter (revidert)

### 4.0 Felles kontrakt: lønnsgrunnlag v2

Mønsteret bygger bevisst på PowerOffice Go salary lines [R1-G], slik at Utleggsappen og andre kan gjenbruke adaptermønsteret de allerede har.

#### 4.0.1 Ressurs

| Felt | Satt av | Innhold |
|---|---|---|
| `externalId` | Kilde | Stabil ID for linjen i kilden. Kan **aldri** gjenbrukes til en annen linje. |
| `revision` | Kilde | Heltall som øker for hver nye versjon av samme `externalId` |
| `category` | Kilde | Datatype i kilderegisteret (`UTLEGG_REISE`, `TID`, `VERV_HONORAR` …) |
| `kind` | Kilde | Linjetype fra den publiserte katalogen (OK-17). **Ikke a-meldingskode.** |
| `person.personId` / `person.externalPersonRef` / `engagementId` | Kilde | Én av dem. `employmentId` er valgfri. Brutto velger når den mangler. |
| `workDate` / `earnedPeriod` / `facts.start`/`end` | Kilde | Når arbeidet eller utlegget skjedde. **Ikke utbetalingsmåned.** |
| `quantity` + `unit` (`HOUR`, `DAY`, `KM`, `PIECE`, `MEETING`) | Kilde | Bare der katalogen krever det. Vakter bruker tidsstempler. |
| `amount` {`value` som tekststreng med 2 desimaler, `currency`} og eventuelt `fx` | Kilde | Totalbeløpet kilden har godkjent |
| `facts` | Kilde | Fakta per linjetype, validert mot JSON Schema |
| `proposed` | Kilde | Bare forslag til visning (for eksempel kildens egen splitting). Brutto bruker det aldri som grunnlag. |
| `dimensions[]` {`type`, `code`} | Kilde | |
| `approval` {`approvedByRef`, `approvedAt`, `method`, `policyRef`} | Kilde | Påkrevd for alle linjetyper som skal betales |
| `evidence[]` {`ref`, `sha256`} | Kilde | Kvittering, vedtak eller kontrakt |
| `isPrivateBenefit` | Kilde | Påkrevd for utleggskategorier, **uten standardverdi** |
| `confidential` | Kilde | Valgfri |
| `description` | Kilde | Fritekst, maks 200 tegn. Merkes som uklarert data. |
| `status`, `holds[]`, `lockState`, `payRunId`, `deferredTo`, `classification` (lesbar lønnsart og a-meldingsbeskrivelse), `payment` {`state`, `payDate`, `payslipId`}, `reporting` {`aMeldingMonth`, `state`}, `rejection` {`code`, `field`, `message`} | **Brutto** | Kan bare leses |

#### 4.0.2 Identitet og idempotens

- **Identitet:** `(installationId, externalId)` er unik per tenant. `installationId` kommer fra tokenet og aldri fra innholdet i kallet.
- **Idempotens:**
  - Samme `(installationId, externalId, revision)` med samme innhold gir samme svar.
  - Samme nøkkel med annet innhold gir 409 `IDEMPOTENCY_CONFLICT`.
  - En lavere revisjon enn gjeldende gir 409 `STALE_REVISION`. Det beskytter mot kilder som har gjenopprettet en gammel backup.
  - I tillegg kreves headeren `Idempotency-Key` på alle POST-kall.
- **Ingen `supersedes` til en ny `externalId`** (B). En rettet linje er en ny *revisjon* av samme `externalId`. En ny `externalId` med samme `evidence.sha256` og person gir varselet `POSSIBLE_DUPLICATE` og holdes tilbake.

#### 4.0.3 Tilstander og låsing

```
                 ┌──────────── HELD (grunner: PENDING_PAYEE, PENDING_LINK, NEEDS_MAPPING,
                 │                    NEEDS_REVIEW, POSSIBLE_DUPLICATE, REQUIRES_WRITTEN_AGREEMENT)
                 │                         │ (grunnen løst)
RECEIVED ─▶ VALIDATED ─▶ ACCEPTED ─(cut-off)─▶ IN_RUN ─(kjøring godkjent)─▶ LOCKED ─▶ PAID ─▶ REPORTED
   │                        │                     │
   └─▶ REJECTED (kode)      ├─▶ WITHDRAWN         └─▶ LATE_CHANGE (menneske: ta med nå / utsett)
                            └─▶ DEFERRED (til neste periode; skjer automatisk med alt som er HELD ved cut-off)
Eldre revisjoner: SUPERSEDED
```

| Fase | Hva kilden kan gjøre | Hva Brutto gjør |
|---|---|---|
| Før cut-off (`ACCEPTED`/`HELD`) | Sende ny revisjon (erstatter) eller trekke tilbake (`POST …:withdraw`) | Validerer og klassifiserer på nytt |
| Mellom cut-off og godkjent kjøring (`IN_RUN`) | Sende ny revisjon eller trekke tilbake. Det blir `LATE_CHANGE`. (B) | Lønnsansvarlig velger «ta med i denne kjøringen» (kjøringen beregnes på nytt) eller «utsett». **Tallene endres aldri uten at den lønnsansvarlige vet det.** |
| Etter godkjent kjøring (`LOCKED`/`PAID`/`REPORTED`) | Sende ny revisjon med full tilstand. Tilbaketrekking = revisjon med `amount: "0.00"`. | Beregner differansen mot den låste revisjonen og lager en korrigeringslinje i neste kjøring (4.0.4) |

En linje tilhører alltid **nøyaktig én kjøring**. En ekstra kjøring og en ordinær kjøring kan ikke ta med den samme linjen.

#### 4.0.4 Korrigering (B)

- **Kilden sender full tilstand, og Brutto beregner differansen.** Kilder lager aldri egne korrigeringslinjer. De vet ikke hva som faktisk er betalt, trukket eller rapportert.
- **Positiv differanse** blir en tilleggslinje i neste ordinære eller ekstra kjøring. Den rapporteres i a-meldingen for utbetalingsmåneden (etterbetalingsregelen [R1-C]).
- **Negativ differanse** som gir trekk i netto, holdes tilbake med `REQUIRES_WRITTEN_AGREEMENT` til det finnes en forhåndsavtale om trekket eller tilbakebetaling er registrert (aml. § 14-15, HR-2021-2532-A [R1-G]).
- **Klassifiseringen endres** (for eksempel diett som blir trekkpliktig): Brutto reverserer den gamle linjen og lager en ny. Om dette skal gi en *økonomisk* rettelse (korreksjonskjøring) eller en *rapporteringsrettelse* (erstatnings-a-melding), avgjør Brutto og den lønnsansvarlige, ikke kilden [R1-F 1.5].

#### 4.0.5 Årsakskoder (revidert)

| Gruppe | Koder |
|---|---|
| Person og arbeidsforhold | `PERSON_NOT_LINKED`, `PAYEE_NOT_READY`, `EMPLOYMENT_NOT_FOUND`, `EMPLOYMENT_ENDED` |
| Kilde og tilgang | `CATEGORY_NOT_GRANTED`, `CATEGORY_OWNED_BY_OTHER_SOURCE`, `NOT_SOURCE_OF_TRUTH`, `SOURCE_RETIRED`, `SANDBOX_KEY_IN_PRODUCTION` |
| Innhold | `KIND_UNKNOWN`, `FACTS_INVALID`, `INVALID_QUANTITY_UNIT`, `CURRENCY_REQUIRED`, `MISSING_APPROVAL`, `UNKNOWN_DIMENSION`, `BENEFIT_FLAG_REQUIRED` |
| Grenser | `RATE_EXCEEDS_LIMIT`, `AMOUNT_EXCEEDS_LIMIT`, `SHIFT_OVERLAP`, `SHIFT_TOO_LONG` |
| Lønn eller ikke | `NOT_PAYROLL` (frikjøp, faktura fra foretak, ren refusjon som skal til regnskap), `UNSUPPORTED_TAX_REGIME` (utenlandsk mottaker, artistskatt) |
| Versjon | `STALE_REVISION`, `IDEMPOTENCY_CONFLICT` |
| Hold (ikke avvisning) | `NEEDS_MAPPING`, `NEEDS_REVIEW`, `POSSIBLE_DUPLICATE`, `REQUIRES_WRITTEN_AGREEMENT`, `PENDING_PAYEE` |

#### 4.0.6 Vern mot feil data (B)

- **Skyggemodus:** I den første perioden for en ny installasjon blir linjene validert og klassifisert, men de går i en «skyggekjøring». Lønnsansvarlig ser diff mot det som ellers ville blitt kjørt, og slår på produksjon.
- **Beløpsgrenser per linjetype og tenant**, for eksempel at én vakt ikke kan overstige 16 timer eller 10 000 kr, og at et honorar per verv ikke kan overstige X. Over grensen holdes linjen med `NEEDS_REVIEW`. Det fanger feil med øre/kroner og minutter/timer.
- **Mapping mangler:** Linjen holdes med `NEEDS_MAPPING` til den kobles til en lønnsart. Brutto bruker **aldri** en standard lønnsart.

#### 4.0.7 Tilbakemelding om utbetalt og innrapportert

| Hendelse | Når | Merknad |
|---|---|---|
| `payinput.status_changed.v1` | Hver overgang | Fra- og til-tilstand, grunner, kjøring, `deferredTo` |
| `payinput.paid.v1` | Kjøringen er godkjent og betalingen sendt | `payment.state = SUBMITTED` (fil laget og utbetalingsdato satt) |
| `payinput.payment_confirmed.v1` | Banken har bekreftet (pain.002/camt.054) | **Kommer bare hvis kunden har bankintegrasjon.** Uten den finnes bare `SUBMITTED`. Kilden må vise «utbetales dd.mm», ikke «betalt». (B) |
| `payinput.payment_returned.v1` | Banken har returnert betalingen | Brutto betaler på nytt når kontonummeret er rettet. **Kilden skal aldri betale selv.** |
| `payinput.reported.v1` | A-meldingen er godtatt av Skatteetaten | Måned og status |
| `payinput.correction_created.v1` | Ny revisjon etter låsing | Opprinnelig revisjon, ny revisjon og differanse |

---

### 4.1 Utleggsappen → Brutto (kontrakt K-UTLEGG)

Den samme kontrakten brukes av Brutto Utlegg, Pleo, Visma Expense og andre.

**Hvem eier sannheten:**

| Hva | Eier |
|---|---|
| Kravet: kvitteringer, reisefakta, godkjenning, policy og totalbeløp | **Utleggsappen** |
| Om noe er *utlegg* eller *fordel* (`isPrivateBenefit`) | Utleggsappen erklærer det, Brutto kontrollerer det |
| Klassifisering (lønnsart, a-meldingsbeskrivelse, trekk og AGA), splitting i trekkfri og trekkpliktig del, utbetaling (vei A), a-melding og korrigeringsdifferanse | **Brutto** |
| Satser (statens og trekkfrie) | Brutto publiserer (kilden er Skatteetaten) |
| Koblingen person → Brutto | Brutto (koblingstabell per installasjon) |
| Dimensjonskoder | Regnskapet, via Bruttos dimensjonsregister |
| Kontonummer for lønn | Brutto |
| Kvitteringsarkiv | Utleggsappen (**åpent spørsmål**, kap. 10) |

**Utbetalingsveier (revidert i B):**

| Vei | Hva | Status |
|---|---|---|
| **A. Via Brutto** | Alle linjer som er opplysningspliktige eller trekkpliktige (diett, kilometergodtgjørelse, nattillegg, fordeler). Betales i ordinær kjøring eller planlagt utleggskjøring (OK-27). | **Må** |
| **B. Ren refusjon utenom Brutto** | Utlegg mot bilag som ikke er opplysningspliktig, betales av Utleggsappen eller regnskapet og **sendes aldri til Brutto**. Utleggsappen kan spørre Brutto med dry-run (`POST /pay-inputs:validate`) og får `reportable=false`. | Bør |
| B2. Opplysningspliktige linjer betalt direkte, med reservasjon i to faser | – | **Ikke nå** (OK-33) |

**Linjetyper (utdrag fra katalogen):**
- `EXPENSE_REFUND` (bare når kunden vil ha refusjoner via lønn)
- `PER_DIEM` (fakta: overnattingstype, land, måltider, tidspunkter, avstand)
- `MILEAGE` (km, passasjerer, kjøretøytype)
- `NIGHT_ALLOWANCE`
- `BENEFIT_PRIVATE_COST`
- `TRAVEL_TAXABLE_OTHER`

**Beløp mot klassifisering (B):** Utleggsappens **totalbeløp** er avtalt med den ansatte og godkjent etter kundens policy. Brutto godtar det og splitter det i trekkfri del (opp til satsen) og trekkpliktig overskudd. Avvik mellom Utleggsappens forslag og Bruttos splitting gir et *varsel*, ikke avvisning. Brutto avviser bare når fakta er ufullstendige eller selvmotsigende (`FACTS_INVALID`).

**Eksempel:**

```json
POST /v1/pay-inputs:batch
Idempotency-Key: 6f1c2a0e-…
{
  "items": [{
    "externalId": "UA-2026-004512:L2",
    "revision": 2,
    "category": "UTLEGG_REISE",
    "kind": "PER_DIEM",
    "person": { "externalPersonRef": "ua-usr-88121" },
    "earnedPeriod": { "from": "2026-10-20T07:10:00+02:00", "to": "2026-10-22T18:30:00+02:00" },
    "amount": { "value": "1650.00", "currency": "NOK" },
    "facts": { "overnight": "HOTEL", "country": "NO", "mealsProvided": ["BREAKFAST"], "distanceFromHomeKm": 210 },
    "dimensions": [ { "type": "avdeling", "code": "200" }, { "type": "prosjekt", "code": "P-4411" } ],
    "approval": { "approvedByRef": "ua-usr-19", "approvedAt": "2026-10-27T12:44:00Z", "method": "MANAGER", "policyRef": "reise-standard" },
    "evidence": [ { "ref": "UA-2026-004512", "sha256": "9f2c…" } ],
    "isPrivateBenefit": false
  }]
}
→ 207 { "results": [ { "externalId": "UA-2026-004512:L2", "revision": 2, "id": "pi_4Kd2",
         "status": "ACCEPTED", "holds": [],
         "classificationPreview": [ { "payElement": "Kost hotell – trekkfri", "amount": "…" },
                                    { "payElement": "Kost – trekkpliktig overskudd", "amount": "…" } ] } ] }
```

| Tema | Regel |
|---|---|
| **Idempotens** | `externalId = <kravId>:<linjeId>`, `revision = kravversjon` |
| **Låsing og korrigering** | Som i 4.0.3–4.0.4. Utleggsappen sender kravet på nytt med full tilstand. En linje som er fjernet etter låsing, sendes som revisjon med 0 kr. |
| **Tilbakemelding** | Hendelsene i 4.0.7. Utleggsappen viser «utbetales 20.11», «utbetalt (bekreftet)» og «innrapportert november» per linje. |
| **Samtykke og tilkobling** | Pakkene `ansatt.basis.les`, `lønnsgrunnlag.skrive:UTLEGG_REISE` og `lønnsgrunnlag.status`. Utleggsappen må være kilde for `UTLEGG_REISE` i ønsket omfang. Hvis Brutto Utlegg er aktiv, krever det et kildebytte (5.2). Personer kobles på e-post fra kundens IdP eller på ansattnummer. |
| **Drift** | Utleggsappen kaller det offentlige API-et over internett fra Advania. Faste utgående IP-adresser kan registreres (OK-128). Det finnes ingen privat linje. |

---

### 4.2 OrgLab → Brutto (kontrakt K-VERV)

**Hvem eier sannheten:**

| Hva | Eier |
|---|---|
| Medlem, verv (rolle, organ, periode), vedtak om satser, møtedeltakelse, dokumentasjon av tapt inntekt | **OrgLab** |
| Personen i Brutto, fødselsnummer (BankID-verifisert), kontonummer, skattekort, arbeidsforhold (type, start og slutt) i a-meldingen, klassifisering, grenseakkumulatorer (skattefri organisasjon og minstegrenser), trekk, AGA, utbetaling og a-melding | **Brutto** |
| Frikjøpsrefusjon til en annen arbeidsgiver | **Regnskapet** (leverandørfaktura). **Ikke lønn.** |

**Ressurser:**
- `engagements` av typen `VERV` (2.4)
- `pay-inputs` med linjetypene:
  - `BOARD_FEE`, med fakta `decisionRef` og periode
  - `MEETING_FEE`, med fakta `meetingRef`, dato og antall
  - `LOST_EARNINGS` (Bør, [U]), med fakta dato, timer, sats, `documented: true|false` og `recipientStatus: EMPLOYED_ELSEWHERE | SELF_EMPLOYED | OTHER`
  - reise og diett bare når OrgLab er kilde for `UTLEGG_REISE` for gruppen «honorar/verv»

**Eksempel:**

```json
POST /v1/engagements
{ "externalId": "OL-verv-5512", "revision": 1, "type": "VERV",
  "legalEntityOrgnr": "987654321",
  "person": { "externalPersonRef": "medlem-104233", "name": "Kari Nordmann",
              "email": "kari@example.no", "mobile": "+4790000000" },
  "role": { "title": "Styremedlem", "body": "Sentralstyret", "from": "2026-06-01", "to": "2028-05-31" },
  "decisionRef": "Årsmøtevedtak 2026-05-12 sak 7" }
→ 201 { "id": "eng_7Hq2", "status": "INVITED", "onboarding": { "sentBy": "BRUTTO", "expiresAt": "2026-11-11" } }

POST /v1/pay-inputs
{ "externalId": "OL-verv-5512:2026H2", "revision": 1, "category": "VERV_HONORAR", "kind": "BOARD_FEE",
  "engagementId": "eng_7Hq2", "earnedPeriod": { "from": "2026-06-01", "to": "2026-11-30" },
  "amount": { "value": "15000.00", "currency": "NOK" }, "confidential": true,
  "facts": { "decisionRef": "Årsmøtevedtak 2026-05-12 sak 7" },
  "approval": { "approvedByRef": "medlem-100001", "approvedAt": "2026-11-25T09:00:00Z", "method": "BOARD_DECISION" } }
→ 201 { "id": "pi_9Lm1", "status": "HELD", "holds": ["PENDING_PAYEE"] }   // blir ACCEPTED når Kari har fullført onboardingen
```

**Regler som stopper feil:**
- **Frikjøp:** Det finnes ingen linjetype for refusjon til arbeidsgiver. Forsøk gir `NOT_PAYROLL` med lenke til veiledning. Dette hindrer at personen får inntekt rapportert både fra egen arbeidsgiver og fra organisasjonen.
- **Skattefri organisasjon:** OrgLab sender alle beløp. Bare Brutto vurderer grensen på 10 000 kr per mottaker og år, eller merking fra første krone. Bare Brutto ser summen fra alle kilder (OrgLab, Tikket, manuelle linjer).
- **Tapt arbeidsfortjeneste der mottakeren er næringsdrivende:** Holdes med `NEEDS_REVIEW` til fagavklaringen [U] er gjort.
- **Medlem som også er ansatt i organisasjonen:** Brutto kobler mot eksisterende person (2.3). Brutto avgjør om vervshonoraret skal på et eget honorar-arbeidsforhold [U], og OrgLab trenger ikke vite det.

| Tema | Regel |
|---|---|
| **Idempotens** | Engasjement: `OL-verv-<vervId>`. Honorar: `OL-verv-<vervId>:<periode>`. Møte: `OL-mote-<møteId>:<medlemsnr>`. Alle med revisjon. |
| **Låsing og korrigering** | Som i 4.0.3–4.0.4. Hvis årsmøtet endrer satsen med tilbakevirkende kraft, sender OrgLab en ny revisjon, og Brutto lager en tilleggslinje i neste kjøring. |
| **Slutt på verv** | `PATCH /engagements/{id}` med ny `role.to` eller `status: ENDED`. Brutto lager et utkast til sluttdato på arbeidsforholdet. |
| **Tilbakemelding** | `engagement.status_changed.v1` (INVITED, ACTIVE, NOT_PAYROLL, MANUAL_REVIEW, ENDED) og hendelsene i 4.0.7. `GET /engagements/{id}/summary?year=` gir sum utbetalt for egne linjer (OK-54). |
| **Samtykke og tilkobling** | Pakkene `engasjement.forespørre`, `lønnsgrunnlag.skrive:VERV_HONORAR` (og eventuelt `UTLEGG_REISE` for gruppen «honorar/verv») og `lønnsgrunnlag.status`. OrgLab trenger **ikke** `ansatt.basis.les`. Orgnr-sjekken (2.1) er særlig viktig, fordi organisasjoner ofte har flere juridiske enheter (forbund og avdelinger). |

---

### 4.3 Tikket → Brutto (kontrakt K-ARRANGEMENT)

**Hvem eier sannheten:**

| Hva | Eier |
|---|---|
| Arrangement (ID, navn, dato, sted), vaktplan, vakter (planlagt og faktisk), innsjekk, bekreftelse fra vaktleder, artistkontrakt (beløp) | **Tikket** |
| Arbeidsforhold (ett løpende per person og juridisk enhet for ekstrahjelp), prising (timesats og tillegg), feriepenger, trekk, AGA, a-melding og underenhet | **Brutto** |
| Dimensjonsverdien «arrangement» | Tikket oppretter den i Bruttos register. ERP-adapteren mapper den til prosjekt i regnskapet. |
| Lønnskostnad per arrangement | **Brutto** (aggregert) |

**Ressurser:**
- `engagements` av typen `EKSTRAHJELP` eller `HONORAR`
- `pay-inputs` med linjetypene:
  - `SHIFT`, med fakta `start`, `end`, `breakMinutes`, `role` og `venueRef`
  - `SHIFT_FIXED` (Bør)
  - `FEE_ASSIGNMENT`
- `PUT /dimensions/arrangement/values/{code}`

**Eksempel:**

```json
PUT /v1/dimensions/arrangement/values/TK-EVT-2026-311
{ "name": "Julekonsert 14.11.2026", "validFrom": "2026-11-01", "validTo": "2027-03-31" }

POST /v1/pay-inputs:batch
{ "items": [{
  "externalId": "TK-shift-88123", "revision": 3, "category": "TID", "kind": "SHIFT",
  "engagementId": "eng_Ek91",
  "facts": { "start": "2026-11-14T17:30:00+01:00", "end": "2026-11-15T01:15:00+01:00",
             "breakMinutes": 30, "role": "bar", "venueRef": "storsalen" },
  "dimensions": [ { "type": "arrangement", "code": "TK-EVT-2026-311" } ],
  "approval": { "approvedByRef": "tk-usr-77", "approvedAt": "2026-11-15T02:00:00+01:00", "method": "CHECKOUT_CONFIRMED" } }] }
```

Hendelsen om kostnad per arrangement kommer etter godkjent kjøring. Tallene er et eksempel for sone I, med AGA 14,1 % av lønn og feriepenger, feriepenger 10,2 % og OTP 2 %:

```json
{ "type": "no.brutto.cost.allocated.v1", "subject": "dimensions/arrangement/TK-EVT-2026-311",
  "data": { "payRunId": "pr_2026-11", "headcount": 14, "grossPay": "48210.00",
            "holidayPayAccrual": "4917.42", "employerTax": "7490.97", "pension": "964.20",
            "total": "61582.59", "currency": "NOK" } }
```

**Regler som stopper feil:**
- **Arbeidsforholdet velges av Brutto.** Tikket sender aldri `employmentId` for ekstrahjelp. Brutto gjenbruker det løpende arbeidsforholdet. Et nytt arbeidsforhold blir et utkast som godkjennes.
- **Vakter med tidsstempler.** Brutto regner ut timer, natt og helg fra tidsstemplene og kundens tariff eller regler. Tikket regner aldri ut tillegg.
- **Overlapp:** To vakter for samme person som overlapper i tid, også fra forskjellige kilder (Tikket og Planday), holdes med `SHIFT_OVERLAP`. Vakter over 16 timer gir `SHIFT_TOO_LONG`.
- **Frivillige uten engasjement** kan ikke få lønnslinjer (`PERSON_NOT_LINKED`). Det er bevisst.
- **Utenlandske artister** gir `UNSUPPORTED_TAX_REGIME`. Artister via byrå eller eget foretak gir `NOT_PAYROLL`.
- **Kostnad per arrangement** sendes bare når `headcount ≥ 3`. Ellers trengs pakken `lønnsresultat.individ.les`.

| Tema | Regel |
|---|---|
| **Idempotens** | Vakt: `TK-shift-<vaktId>` med revisjon lik vaktversjonen. Honorar: `TK-contract-<kontraktId>:<avdrag>`. |
| **Låsing og korrigering** | Som i 4.0.3–4.0.4. En vakt som endres etter låsing, gir differanse i neste kjøring. |
| **Tilbakemelding** | Hendelsene i 4.0.7, `engagement.status_changed.v1` og `cost.allocated.v1` |
| **Samtykke og tilkobling** | Pakkene `engasjement.forespørre`, `lønnsgrunnlag.skrive:TID` (omfang: gruppen «ekstrahjelp») og `lønnsgrunnlag.skrive:VERV_HONORAR` (omfang: «honorar»), `dimensjon.skrive:arrangement`, `kostnad.aggregert.les` og `lønnsgrunnlag.status` |

---
### 4.4 Huma ↔ Brutto (kontrakt K-HUMA)

#### 4.4.1 Hva vi vet om Huma (sjekket 28.10.2026)

| Påstand | Status | Kilde |
|---|---|---|
| Norsk og nordisk HR-system med personaladministrasjon, onboarding og offboarding, fravær, dokumenter og håndbøker, digitale arbeidsavtaler med e-signering, medarbeidersamtaler, utstyr, lønnsrevisjon, likelønn, undersøkelser, varsling, avvik og mobilapp | **[Bekreftet]** | [humahr.com](https://www.humahr.com) |
| Integrasjoner mot blant annet Tripletex, PowerOffice Go, Visma.net Payroll, Xledger, Fortnox, Finago, Unimicro, NAV, Entra ID og Teamtailor, og eksport i PAXml | **[Bekreftet]** | [humahr.com/no/integrasjon](https://humahr.com/no/integrasjon) |
| NAV-integrasjonen henter sykmeldingsinformasjon fra NAV til Huma | **[Bekreftet]** | Samme side |
| Tripletex-integrasjonen synkroniserer ansatte i begge retninger, lønn fra Huma til Tripletex ved lønnsrevisjon, og fravær fra Huma til Tripletex («nylig lagt til») | **[Bekreftet]**, men siden sier ikke hvem som er master | [Tripletex og Huma](https://humahr.com/no/tripletex-og-huma-integrasjon) |
| Huma kjører ikke lønn selv | **[Antatt]**. Det er gründerens opplysning og stemmer med integrasjonssidene. | – |
| Integrasjon mot 24SevenOffice | **[Ikke bekreftet]**. Står ikke på integrasjonssiden. | – |
| Altinn-integrasjon | **[Ikke bekreftet]**. Står ikke på siden. | – |
| Pris fra 49 kr per ansatt per måned | **[Ikke bekreftet]**. Prissiden viser planene Free, Standard og Premium og «Contact us for pricing». Fravær, arbeidsavtaler og integrasjoner krever Standard eller Premium. | [humahr.com/plans-pricing](https://humahr.com/plans-pricing) |
| **Offentlig REST-API**: «Huma API» 1.89.0, OpenAPI 3.1, `https://openapi.humahr.com`, OAuth2 client credentials | **[Bekreftet]** | [openapi.humahr.com/v3/api-docs](https://openapi.humahr.com/v3/api-docs), [Open API-artikkel](https://humahr.com/knowledge/open-api) |
| API-ressurser: `users` (liste, opprette, hente, endre, ikke slette), `users/{id}/positions` (full CRUD), `identifications` (`national`/`passport`), `children`, `emergency`, `supervisor`/`subordinates`, `work-schedule`, `groups` (selskap med `organizationNumber`, team, lokasjon), `job-titles`, `holidays`. Paginering med `limit`/`offset`, maks 50. | **[Bekreftet]** i spesifikasjonen | Samme |
| Brukerdetaljer har feltene `bankAccount`, `identifications`, `salary` (bare gjeldende), `employmentId` og `custom`. Hvert felt er pakket inn med `editable` og `integrations` (advarsel `locked_disconnect`). | **[Bekreftet]** i skjemaet. **[Antatt]** at feltene kan låses per integrasjon. | Samme |
| **Ingen** API-ressurs for fravær, dokumenter, arbeidsavtaler, lønnshistorikk eller lønnsresultat. API-et kan ikke deaktivere brukere. | **[Bekreftet]** i spesifikasjonen 1.89.0 | Samme |
| **Webhooks**: emnene `users-*`, `user-email-update`, `positions-*`, `absence-*` og `groups-*` (create, update, delete, export). Signering med headeren `huma-hmac-sha256` og hemmelighet. Svarfrist 1 sekund. **Retry er ikke beskrevet.** Lønn kommer foreløpig via profilhendelser og som egne hendelser «in 2026». | **[Bekreftet]** | [Webhooks](https://humahr.com/knowledge/webhooks), [Profilwebhook](https://humahr.com/knowledge/this-is-how-the-profile-webhook-work) |
| Felter i fraværshendelsen: `id`, `status` (`pending`/`approved`/`rejected`), `type.name` (for eksempel `vacation`, `sick`), `user` {`id`, `email`}, `startDate`, `endDate`, `grade` (0–1), `workRelated`, `reviewedAt`, `reviewedBy`, `registeredAt` | **[Bekreftet]** | Webhooks-siden |
| Fraværstypene er kundedefinerte policyer og ikke en fast liste | **[Antatt]** | – |

**Det viktigste for kontrakten:**
- Huma kan *sende* person, stilling, gruppe og fravær.
- Huma kan *ta imot* endringer på person og stilling via API.
- Huma har **ingen kanal for lønnsresultat**.
- Fravær finnes **bare som webhook**, ikke som API.
- Webhooks har ingen dokumentert retry.

#### 4.4.2 Hvem bygger og drifter koblingen

- **Brutto bygger «Huma-koblingen» selv**, slik Huma har bygget sin Tripletex-kobling. Det er en app på Bruttos egen plattform, med egen OAuth-klient, synlige pakker og Bruttos offentlige API på den ene siden og Humas offentlige API og webhooks på den andre.
- Andre HR-leverandører kan bygge det samme på like vilkår, og Huma kan overta koblingen senere.
- **Avhengighetsrisiko:** Brutto vil konkurrere med Huma. Huma kan begrense API-tilgangen, og den krever i dag Standard- eller Premium-plan. Reserveløsningen er PAXml- eller CSV-eksport [Bekreftet at PAXml finnes] og import via Bruttos importrammeverk.

#### 4.4.3 Hvem er master (fase 1, sameksistens)

| Datatype i kilderegisteret | Kilde i fase 1 | Merknad |
|---|---|---|
| `PERSON_BASIS` | **Huma** | Navn, e-post, telefon, adresse |
| `ARBEIDSFORHOLD_HR` | **Huma** (`positions`) | Se mapping 4.4.4 |
| `ORGANISASJON` | **Huma** (`groups`, `supervisor`) | Brukes i godkjenningskjedene i Bruttos egne moduler |
| `AVTALT_LØNN` | Huma **hvis** kunden bruker Humas lønnsmodul eller lønnsrevisjon, ellers Brutto | Kunden velger |
| `FRAVÆR` | Huma **eller** Brutto Fravær, aldri begge | Se 4.4.7 |
| `ARBEIDSFORHOLD_AMELDING` (yrkeskode, arbeidstidsordning, underenhet, arbeidsforholdstype) | **Brutto** | Huma har ikke disse feltene [Bekreftet: ikke i `Position`]. Brutto supplerer og validerer. |
| `IDENTITET` | **Brutto**. Huma kan bare foreslå. | Huma-verdien lagres *uverifisert* til skattekortet er hentet eller personen har bekreftet med BankID |
| `BANKKONTO` | **Brutto** | Se 4.4.6 |
| `SKATTEKORT`, lønn, a-melding | **Brutto** | |
| `DOKUMENT:*` | Huma | Brutto lagrer egne dokumenter (lønnsslipper, trekkavtaler) |

#### 4.4.4 Huma → Brutto: flyt og mapping

| Huma | Brutto | Regel |
|---|---|---|
| `users-create/update/delete` og `user-email-update` (webhook) | Person (`PERSON_BASIS`) | **«Varsle, så hente»:** Webhooken er bare en trigger. Koblingen henter gjeldende tilstand med `GET /users/{id}` og `…/positions`. Det løser rekkefølge og duplikater, fordi Huma ikke har dokumentert hendelses-ID eller sekvens. |
| `users/{id}.employmentId` | Ansattnummer (hint for matching) | Huma sier at verdien kan endres. Brukes derfor bare til matching, aldri som nøkkel. **Nøkkelen er Humas `user.id`.** |
| `positions` | Arbeidsforhold og stillingsperioder | **En ny Huma-stilling er ikke automatisk et nytt arbeidsforhold i a-meldingen.** Stillingsbytte innen samme juridiske enhet (`endReason = change_in_organization_or_internal_job_transfer`, eller ny stilling som starter dagen etter forrige) blir en *ny stillingsperiode i samme arbeidsforhold*. Et nytt arbeidsforhold opprettes bare ved ny juridisk enhet eller reell slutt og nyansettelse. Uklare tilfeller blir et utkast som et menneske avgjør. (B) |
| `contractType` | Arbeidsforholdstype og ansettelsesform | `Permanent` → ordinært/fast. `Temporary`/`Seasonal` → ordinært/midlertidig. `Casual` → ordinært/midlertidig (tilkalling). `Freelance` → frilanser/oppdragstaker/honorar. `Consultant`/`ThirdParty` → **ikke lønn** (holdes). `Trainee`/`JobTrainingProgram` → holdes til det er mappet [U]. |
| `percentage`, `contractStartDate`, `contractEndDate`/`lastDayOfWork`, `endReason` | Stillingsprosent, start, slutt, sluttårsak | Hvilken Huma-dato som tilsvarer a-meldingens start- og sluttdato [U] avgjøres i mappingtabellen per tenant. Sluttårsakene mappes til a-meldingens kodeliste [U]. |
| `groups` (selskap med `organizationNumber`, lokasjon, team) | Juridisk enhet, underenhet, avdeling | Selskapets orgnr må stemme med tenanten. Lokasjon → underenhet settes i en mappingtabell ved installasjonen, fordi AGA-sonen følger underenheten [R1-D 6.2]. |
| `supervisor` | Lederrelasjon | |
| `salary` (gjeldende, `periodUnit`, `fromDate`) | Fastlønn eller timesats (hvis Huma eier `AVTALT_LØNN`) | Huma sender bare gjeldende lønn, ikke historikk [Bekreftet]. Hvis `fromDate` ligger i en låst periode, lager Brutto et forslag om etterberegning som lønnsansvarlig godkjenner. |
| `identifications` (`national`) | Fødselsnummer, uverifisert | Kontrollsiffer sjekkes. Verifiseres når skattekortet er hentet eller personen har bekreftet med BankID. |
| `bankAccount` | – | 4.4.6 |
| `absence-*` (webhook) | Fravær v1 (2.6) | Bare når Huma er kilde for `FRAVÆR`. 4.4.7. |

#### 4.4.5 Brutto → Huma: hva kan gå tilbake

| Data | Kanal | Status |
|---|---|---|
| Lønnsslipp, lønnsresultat, saldo for feriepenger, AGP-status | **Ingen API-ressurs hos Huma** [Bekreftet] | Ikke mulig nå. Den ansatte bruker Bruttos ansattportal. SSO via kundens IdP gjør overgangen sømløs. |
| Lenke fra Huma-profilen til Brutto | `PATCH /users/{id}` med `custom`-felt | [Antatt mulig]. Egendefinerte felt finnes i `UserDetailsInput`. |
| «Mangler for lønn» (for eksempel yrkeskode, kontonummer ikke bekreftet) | Arbeidsliste i Brutto, eventuelt `custom`-felt i Huma | [Antatt]. Brutto skriver **aldri** til felt Huma eier. |
| Ansattnummer fra Brutto | `employmentId` | Bare hvis kunden velger at Brutto skal nummerere ansatte |
| Lønnshendelser når Huma lager slike («in 2026») | – | Følges opp. Kan gi en bedre kanal senere. |

#### 4.4.6 Kontonummer og fødselsnummer fra Huma

- **Første import (onboarding):** Kontonumre fra Huma kan importeres **én gang** som en signert importbatch. Kundens administrator godkjenner med step-up, og Brutto sender varsel til hver ansatt om at kontonummeret er registrert.
- **Senere endringer i Huma brukes aldri automatisk.** De blir et *endringsforslag* som den ansatte må bekrefte med BankID i Bruttos ansattportal. Kunden rådes til å låse feltet i Huma.
- **Fødselsnummer:** Se tabellen over. A-meldingen sendes ikke for en person med uverifisert fødselsnummer før skattekortet er hentet uten feil.

#### 4.4.7 Fravær fra Huma, og konflikt med Bruttos egen fraværsmodul

1. **Kilderegisteret avgjør:** `FRAVÆR` (eventuelt per arbeidsforholdsgruppe) er enten «Huma» eller «Brutto Fravær».
2. **Huma er kilde:**
   - Bare `status = approved` blir fravær i Brutto. `rejected` og `absence-delete` blir revisjoner med `CANCELLED`.
   - `type.name` mappes til Bruttos fraværstyper i en tabell per tenant. En type uten mapping holdes med `NEEDS_MAPPING`.
   - Brutto Fravær viser bare konsekvensene (arbeidsgiverperiode, refusjon, inntektsmelding, ferietrekk) og har lenken «Registreres i Huma».
3. **Brutto er kilde:** Koblingen ignorerer `absence-*` fra Huma. Det logges i integrasjonsmonitoren («Huma sender fravær, men Brutto er kilde»), så kunden kan slå av fraværsmodulen i Huma.
4. **NAV-dobbeltført:** Huma henter sykmeldinger fra NAV [Bekreftet]. Brutto får forespørsler om inntektsmelding fra NAV [R1-B]. Når Huma er kilde, oppretter Brutto **ikke** fravær fra NAV-data. Brutto sammenligner NAV-forespørselen med fraværet fra Huma og varsler om avvik.
5. **Webhooks uten retry:**
   - **Innboks-mønster:** Brutto lagrer og svarer med 200 under 1 sekund, og behandler etterpå.
   - **Fraværsavstemming før cut-off:** Brutto viser antall fravær mottatt fra Huma per periode og ber lønnsansvarlig bekrefte mot Humas fraværsrapport, eller utløse `absence-export` hvis Huma tillater det [U].
   - Siden fravær ikke kan hentes via API, er dette den eneste kontrollen.

#### 4.4.8 Idempotens, låsing og samtykke

| Tema | Regel |
|---|---|
| **Inn fra Huma** | Webhook-innboksen dedupliserer på (emne, enhets-ID, hash av innholdet). For person og stilling løser «varsle, så hente» resten. For fravær brukes `reviewedAt`/`registeredAt` som versjon, og eldre versjoner forkastes. |
| **Mot Brutto** | `externalId` = `huma:user:<id>`, `huma:position:<id>`, `huma:absence:<id>`. `revision` øker når hashen av innholdet endres. Vanlig `Idempotency-Key`. |
| **Avstemming** | Hver natt hentes alle brukere og stillinger (`GET /users` side for side, 50 per side) og sammenlignes. Avvik vises i integrasjonsmonitoren. |
| **Låsing og korrigering** | Endringer i masterdata eller fravær som gjelder en låst periode, gir et forslag om etterberegning eller korrigeringslinjer i neste kjøring (4.0.4). Lønnsansvarlig godkjenner. |
| **Samtykke og tilkobling** | (1) Kunden installerer «Huma-kobling» i Brutto med pakkene `hr.skrive:{PERSON_BASIS, ARBEIDSFORHOLD_HR, ORGANISASJON[, AVTALT_LØNN]}`, `identitet.foreslå`, eventuelt `fravær.skrive` + `fravær.helse`, og `ansatt.basis.les`. (2) Kunden lager en API-klient (client_id og secret) og et webhook-abonnement med hemmelighet i Huma. Hemmelighetene lagres i Bruttos KMS. (3) Mappingveiviser for selskap, lokasjon, underenhet, kontraktstyper og fraværstyper. (4) Første import i skyggemodus med diff-rapport. (5) Aktivering. |

---

### 4.5 Kort: tredjeparter bruker de samme byggeklossene

| Tredjepart | Bruker |
|---|---|
| Pleo, Visma Expense, Brutto Utlegg | K-UTLEGG (4.1) uendret |
| Planday, Tamigo, Quinyx, Brutto Timer | Lønnsgrunnlag v2 med `TIME_HOURS`/`SHIFT` og `sourceCode`-mapping, fravær v1, kilderegister per arbeidsforholdsgruppe |
| Simployer, Sympa, HiBob, Personio | Samme mønster som K-HUMA: `hr.skrive` per attributtgruppe, mapping av arbeidsforhold, «varsle, så hente» |
| Tripletex, PowerOffice, BC, Xledger | Bilag-push via egne adaptere (OK-90) eller generisk pull (OK-91) |
| KLP, SPK, OTP-leverandører | Fil eller API for pensjonsgrunnlag (OK-97). OTP via a-meldingen. |
| Banker | pain.001/pain.002/camt.054 (OK-99–101) |
| Kombo, Merge, Finch, Apideck | Lese-API og partnerapp (OK-110–114) |

---
## 5. Bruttos egne moduler: konflikt med eksterne kilder, og dogfooding

### 5.1 Regler mot konflikt når kunden har både egen og ekstern modul

| Situasjon | Regel |
|---|---|
| Brutto Utlegg og Utleggsappen | Én kilde for `UTLEGG_REISE` per omfang. Vanligvis én kilde for hele tenanten. Det er lov å dele, for eksempel Utleggsappen for ansatte og Brutto Utlegg for honorarmottakere, så lenge gruppene ikke overlapper. |
| Brutto Timer for faste, Tikket for ekstrahjelp og Planday for butikk | `TID` per arbeidsforholdsgruppe. Et arbeidsforhold tilhører nøyaktig én gruppe på en gitt dato. Overlappende vakter sjekkes på tvers av kilder (`SHIFT_OVERLAP`). |
| Brutto Fravær og Huma, eller Brutto Fravær og Planday-fravær | Én kilde for `FRAVÆR` per omfang (4.4.7) |
| Fravær og timer fra forskjellige kilder | Det er lov, fordi det er to datatyper. **Konsistenskontroll:** Timer på en dag med 100 % fravær gir `NEEDS_REVIEW`. |
| Lønnsansvarlig registrerer manuelt i Brutto for en datatype en ekstern kilde eier | Blokkert i UI. Det eneste unntaket er datatypen `MANUELL_KORRIGERING`, som bare lønnsansvarlig kan bruke. Den logges og vises i integrasjonsmonitoren. Det er en nødventil, ikke en vanlig kanal. |
| Kunden slår på Brutto-modulen mens en ekstern kilde er aktiv | Modulen blir aktiv først etter et kildebytte (5.2). Til da er registrering i modulen skjult. |

### 5.2 Kildebytte: slik bytter kunden mellom egen og ekstern modul

```
Planlagt ─▶ Forberedt (ny kilde installert, mapping ferdig) ─▶ Skygge (≥ 1 periode, diff) ─▶ Byttet ─▶ Kontrollert
                                                                     │                    │
                                                                     └── avbryt ◀─────────┴── rull tilbake (til første kjøring etter byttet er godkjent)
```

1. **Planlegg** med `POST /source-switches` {datatype, omfang, fra, til, `effectiveDate`}. Byttedatoen må være første dag i en lønnsperiode.
2. **Forbered:** Installer den nye kilden og sett opp mapping (fraværstyper, lønnsartkoder, grupper).
3. **Skygge** (Må for `FRAVÆR` og HR-datatypene, Bør for de andre): Den nye kilden leverer i skyggemodus i minst én periode. Brutto viser diff mellom gammel og ny kilde.
4. **Åpningsbalanse:** Saldoer importeres som en signert importbatch med dry-run og step-up:
   - feriedager igjen
   - avspasering
   - egenmeldingsdager brukt og arbeidsgiverperioder siste 12 måneder
   - åpne fravær som krysser byttedatoen
5. **Bytt** på byttedatoen:
   - Den nye kilden blir aktiv.
   - Den gamle kilden får `SOURCE_RETIRED` for data datert på eller etter byttedatoen.
   - Den gamle kilden kan fortsatt korrigere *egne* linjer datert før byttedatoen i et overgangsvindu på 2 lønnsperioder. Etter det korrigeres det manuelt i Brutto.
   - **Linjer under behandling flyttes aldri.** Den gamle kildens linjer som er `ACCEPTED` eller `IN_RUN`, går ferdig.
   - **Fravær som krysser byttedatoen** deles. Den gamle kilden eier delen før, og den nye kilden registrerer delen etter (en del av åpningsbalansen).
6. **Kontroller:** Integrasjonsmonitoren viser første periode etter byttet sammenlignet med skyggeperioden.
7. **Hendelser:** `source.switch_scheduled` og `source.switched` sendes til begge kildene, slik at den gamle kan slutte å sende og vise «Håndteres nå av …».

### 5.3 Dogfooding: hvordan egne moduler beviser at API-et er godt nok

| # | Bevis | Hvordan | Mål |
|---|---|---|---|
| 1 | **Samme vei inn** | Brutto Fravær, Timer og Utlegg er egne OAuth-klienter og installasjoner. De kaller den offentlige API-gatewayen. Nettverksregler hindrer moduldriften i å nå kjernens database eller interne endepunkter. | 0 unntak |
| 2 | **Byggeregel** | Modulene kan bare bruke den genererte klienten for det offentlige API-et. Operasjoner i OpenAPI merkes med publikum (offentlig/internt). Humas dokumentasjonsvisning støtter tilsvarende filtrering med `x-audience` («External Only (Public)» / «Internal & External (Full)») [Bekreftet i visningen. Den offentlige spesifikasjonen har ingen slike merker.]. Bygget stopper hvis en modul kaller noe som ikke er offentlig. | Bygget stopper |
| 3 | **API først** | Ingen modulfunksjon lanseres før API-evnen den bruker, er dokumentert og tilgjengelig i sandkassen for alle. Endringsloggen merker hvilke endepunkter som ble «drevet av Brutto Timer» eller «drevet av partner X». | 0 dager mellom intern bruk og offentlig dokumentasjon |
| 4 | **Byttetest i CI** | De gylne lønnsscenarioene [R1-F 7] kjøres to ganger ved hver release: med Brutto-modulen og med den **åpne referanseintegrasjonen**, som er egen kode bygget bare fra dokumentasjonen. Lønnsresultat, a-melding-XML og bilag skal være identiske. | 100 % likt på øret |
| 5 | **Samme grenser og sertifisering** | Modulene består samme samsvarstest som partnere, har samme grenser for antall kall og ligger på samme statusside | Ingen spesialgrenser |
| 6 | **Ekstern prøve** | Før lansering, og hvert halvår, bygger en ekstern utvikler (for eksempel fra Utleggsappen eller pilotbyråets integratør) referanseflyten bare fra dokumentasjonen. Vi måler tid til første godtatte linje og antall spørsmål til support. | Under 1 dag. Antall spørsmål går ned. |
| 7 | **Synlig for kunden** | Installasjonsoversikten viser Brutto-modulene som apper med de samme pakkene. Kunden kan trekke dem tilbake. | – |

**Kostnad [V]:** Å kjøre modulene som egne klienter gir en ekstra enhet å deploye og litt mer forsinkelse sammenlignet med kall i samme prosess i en modulær monolitt [R1-F ADR-01]. Prisen er lav, og det er den eneste måten å *bevise* likebehandling på. Kjernen kan fortsatt være en modulær monolitt.

**Om Utleggsappen:** Når Brutto Utlegg finnes, er dogfooding også et konkurransevern for søsterproduktet. Utleggsappen kan se at Brutto Utlegg ikke har noe Utleggsappen mangler.

---

## 6. Huma: erstatningsvei i faser og krav fra dag én

### 6.1 Oversikt

```
Fase 0 (nå → lansering)        Fase 1 Sameksistens             Fase 2 Brutto tar fravær,         Fase 3 Brutto tar HR-masteren
Krav fra dag én (6.5)          Huma = HR-master                timer og utlegg                   Migrering fra Huma, Huma sies opp
                               Brutto = lønn                   Huma = HR-master
                               Fravær: Huma eller Brutto       Kildebytte FRAVÆR → Brutto
──────────────────────────────▶ (fra første Huma-kunde) ──────▶ (per kunde, etter 6.3) ──────────▶ (per kunde, år 2–3, etter 6.4)
```

Hver fase gjelder **per kunde** og gjennomføres med kildebytte (5.2). Ingen kunde tvinges videre.

### 6.2 Fase 1: Sameksistens (Huma er master, Brutto tar lønn)

- **Eierskap:** Som i 4.4.3. Huma eier person, arbeidsforhold-HR og organisasjon, eventuelt også fravær og avtalt lønn. Brutto eier identitet, bankkonto, skattekort, felt som bare gjelder a-meldingen, og alt om lønn.
- **Brutto leverer:**
  - Huma-koblingen (4.4)
  - mappingveiviser
  - nattlig avstemming
  - fraværsavstemming
  - ansattportal med lønnsslipp (via SSO)
- **Brutto lagrer fra første dag** lønnshistorikk, fraværshistorikk og arbeidsforholdshistorikk bitemporalt, selv om Huma er kilden. Det gjør fase 3 enklere, fordi Humas API bare gir gjeldende lønn og ikke har fravær.
- **Kriterier for å gå videre:** 3 lønnsperioder på rad uten avvik i avstemmingen, og Brutto Fravær dekker kundens fraværstyper, godkjenningsflyt og saldoer.

### 6.3 Fase 2: Brutto overtar fravær, timer og utlegg

| Datatype | Fra | Til | Merknad |
|---|---|---|---|
| `FRAVÆR` | Huma | Brutto Fravær | Kildebytte med skygge og åpningsbalanse:<ul><li>Fraværshistorikken har Brutto allerede (6.2).</li><li>Saldoer og egenmeldingsdager hentes fra Bruttos lagrede historikk og kontrolleres mot Humas rapport.</li><li>Kunden slår av fravær i Huma.</li><li>Brutto overtar også sykmeldingsdata fra NAV, som Huma hentet før.</li></ul> |
| `TID` | Planday, Excel eller ingenting | Brutto Timer | Huma er ikke kilde [Antatt: tidsregistrering er ikke funnet på Humas sider]. Øker Bruttos verdi i forhold til Huma. |
| `UTLEGG_REISE` | Utleggsappen, Pleo eller ingenting | Brutto Utlegg, **eller fortsatt Utleggsappen** | Kunden velger fritt. Prinsipp 2. |

**Kriterier for å gå videre:** Brutto Fravær har vært kilde i 3 perioder, og Brutto har dokumentlager, e-signering og en HR-kjerne med person, arbeidsforhold, organisasjon og onboarding light (6.4).

### 6.4 Fase 3: Brutto overtar HR-masteren

**Kildebytte** for `PERSON_BASIS`, `ARBEIDSFORHOLD_HR`, `ORGANISASJON`, `AVTALT_LØNN` og `DOKUMENT:*`. Brutto har allerede kopier av de fleste data fra fase 1, så migreringen handler mest om dokumenter og «det siste».

| Data i Huma | Hvordan det hentes | Status |
|---|---|---|
| Profil, barn, nødkontakter, identifikasjoner, egendefinerte felt | API (`/users`, `/children`, `/emergency`, `/identifications`, `custom`) | [Bekreftet] |
| Stillinger (nåværende, avsluttede, kommende) | API (`/users/{id}/positions`) | [Bekreftet] |
| Selskap, team, lokasjon, stillingstitler, ledere | API (`/groups`, `/job-titles`, `/supervisor`) | [Bekreftet] |
| Lønnshistorikk | **Ikke i API** [Bekreftet]. Brutto har egen historikk fra fase 1. Lønn fra før fase 1 hentes fra Humas eksport eller lønnsrevisjonsrapport. | [Antatt] eksport |
| Fraværshistorikk | **Ikke i API** [Bekreftet]. Brutto har den fra fase 1–2. Historikk fra før det hentes fra Humas rapport eller CSV. | [Antatt] |
| Dokumenter og **signerte arbeidsavtaler** | **Ikke i API** [Bekreftet]. Hentes som masseeksport fra Humas admin, eller som dataportabilitetsforespørsel. Importeres som *uforanderlige* dokumenter med originalfil (inkludert signaturbevis), signatarer, signeringsdato og sha256. Kunden bekrefter at alt er med, mot en liste over antall per ansatt. | [Antatt] eksportvei, må avklares med Huma |
| Medarbeidersamtaler, utstyr, kompetanse, undersøkelser, varsling og avvik | **Ikke i API** [Bekreftet] | Eksporteres som PDF-arkiv til dokumentlageret, eller beholdes i et partnerverktøy. Brutto bygger ikke dette i første omgang. |
| Systemer som lytter på Huma (Entra ID, Teamtailor, Slack) | – | Flyttes til Bruttos webhooks og SCIM (OK-178, OK-179) |

**Fremgangsmåte:**
1. Skyggeperiode der Brutto er «master i venteposisjon»: Bruttos data sammenlignes med Huma begge veier.
2. Bytte ved periodeskifte.
3. Huma beholdes skrivebeskyttet i 3 måneder som reserve.
4. Kunden sier opp Huma.

**Hva «erstatte Huma» betyr [V]:** Huma har mange moduler (4.4.1). Det realistiske målet er å erstatte **HR-kjernen**:
- personalia, arbeidsforhold og organisasjon
- fravær
- dokumentlager med arbeidsavtaler og e-signering etter malkravene i aml. § 14-6
- onboarding og offboarding light
- ansattportal og mobil

Medarbeidersamtaler, undersøkelser, varsling og kompetanse overlates til partnere gjennom åpne integrasjoner, eller bygges senere. Ellers vokser omfanget forbi det et team på 5–7 kan bære.

### 6.5 Krav til plattformen fra dag én som gjør erstatningen mulig

| ID | Krav | MoSCoW | Hvorfor fra dag én |
|---|---|---|---|
| OK-170 | **Kanonisk person- og arbeidsforholdsmodell** som dekker alle Huma-feltene: person 1–n arbeidsforhold 1–n stillingsperioder, kontraktstype, prøvetid, oppsigelsesdato, sluttårsak, ønsket slutt, barn, nødkontakter og identifikasjoner. Bitemporal. | **Må** | Å utvide modellen senere krever migrering av alle kunder [R1-F ADR-03] |
| OK-171 | **Kilderegister med flyttbart eierskap** per attributtgruppe og omfang, med gyldighetsdato, håndhevet i API og UI (2.2) | **Må** | Alle fasene er kildebytter |
| OK-172 | Stabile eksterne referanser per installasjon som beholdes etter kildebytte | **Må** | Sporbarhet og revisjon |
| OK-173 | **Dokumentlager:** per person og arbeidsforhold, typede dokumenter, uforanderlige versjoner, metadata (kilde, signatarer, signeringsdato, hash), oppbevaringsregler og sletting, feltkryptering og import-API | **Må** (basis) | Brukes fra dag én til lønnsslipper, trekkavtaler og kvitteringer for skattekort. Utvides i fase 3. |
| OK-174 | E-signering bak et grensesnitt der leverandøren kan byttes | **Må** | Trekkavtaler etter aml. § 14-15 trengs nå. Gjenbrukes til arbeidsavtaler. |
| OK-175 | **Importrammeverk:** idempotent, dry-run, diff-rapport, signert batch, tilbakerulling | **Må** | Trengs også for migrering fra konkurrenter [R1-F ADR-15] |
| OK-176 | Organisasjonsmodell: juridisk enhet, underenhet, avdeling, team og lokasjon, og lederrelasjon med gyldighet | **Må** | |
| OK-177 | Typede egendefinerte felt med eierskap | Bør | Huma har `custom` |
| OK-178 | Hendelser for alle endringer i masterdata (person, arbeidsforhold, organisasjon, fravær) | Bør (**Må** før fase 3) | Systemer som lytter på Huma i dag, må kunne flyttes |
| OK-179 | Utgående SCIM- og Entra-provisjonering når Brutto er HR-master | Kan (**Må** før fase 3) | |
| OK-180 | Fraværsmodell med detaljer NAV trenger (grad, telling av arbeidsgiverperiode, egenmeldingsdager, sykmeldingsreferanse), også når Huma er kilde | **Må** | Lønn trenger det uansett |
| OK-181 | Lønnshistorikk lagres i Brutto fra første dag | **Må** | Huma-API-et gir bare gjeldende lønn [Bekreftet] |
| OK-182 | Mappingtabeller per tenant (kontraktstype, sluttårsak, fraværstype, lokasjon → underenhet), delt av koblingen og migreringen | **Må** | |
| OK-183 | Huma-koblingen (4.4) | **Må** hvis en pilotkunde bruker Huma, ellers Bør | |
| OK-184 | Fraværsavstemming mot Huma før cut-off | **Må** sammen med OK-183 | Humas webhooks har ingen dokumentert retry |
| OK-185 | Ansattportalen bygges slik at den kan bli den ansattes «hjem» (lønnsslipp nå, HR senere) | **Må** (portal), utvides i fase 3 | |

---
## 7. Plattformprinsipper for åpne integrasjoner på like vilkår

| # | Prinsipp | Hva det betyr konkret | Hvordan det etterprøves |
|---|---|---|---|
| 1 | **Ett offentlig API, ingen bakdører, heller ikke for oss selv** | Bruttos egne moduler, søsterprodukter og tredjeparter bruker de samme dokumenterte endepunktene, hendelsene og tilgangspakkene | Byggeregel og nettverksregler (5.3 punkt 1–2). Kvartalsvis gjennomgang av trafikken. |
| 2 | **Publisert likebehandlingserklæring** | Utleggsappen, OrgLab, Tikket, Bruttos moduler og tredjeparter har samme tilgangspakker, grenser, SLA, sertifiseringskrav og tidspunkt for tilgang til nye API-er (åpen beta for alle samtidig). Designpartnere kan være både søsterprodukter og tredjeparter, og listen er offentlig. | Erklæringen ligger på utviklerportalen. Avvik kan meldes. |
| 3 | **Én kilde til sannhet per datatype per kunde** | Kilderegisteret (2.2) avgjør hvem som kan skrive. Bruttos eget UI følger det samme. Kunden bytter kilde med en planlagt prosedyre (5.2). | API-et gir 409 `NOT_SOURCE_OF_TRUTH`. Kilderegisteret er synlig i UI. |
| 4 | **Brutto eier rapporteringssannheten, kildene eier fakta** | Kildene sender fakta og full tilstand. Brutto klassifiserer, oppretter arbeidsforhold (som utkast), beregner differanser og rapporterer. Kildene sender aldri a-meldingskoder, utbetalingsmåned eller kontonummer. | Kontraktene (kap. 4). Skjemaet har ikke slike felt. |
| 5 | **Kunden eier tilkoblingen** | Installasjon med tilgangspakker, samtykke, orgnr-sjekk, oversikt, tilbaketrekking, skyggemodus og integrasjonsmonitor | OK-03, OK-122, OK-123 |
| 6 | **Kontrakten kommer først, og den er stabil** | OpenAPI 3.1 og JSON Schema for hendelser ligger i et offentlig repo. Innen en hovedversjon kommer bare tillegg. Avvikling tar minst 12 måneder, med `Deprecation`/`Sunset`. **«Lønnsfred»:** ingen breaking endringer eller avviklinger i desember–januar og i juni (feriepenger). | Endringslogg. Kontraktstester mot sandkassen. |
| 7 | **Sandkassen er produksjon minus penger og myndigheter** | Samme kode og regler, syntetiske data og tidsmaskin. Sandkassenøkler virker aldri i produksjon. | OK-04, OK-15 |
| 8 | **Asynkront, robust og etterprøvbart** | Webhooks er varsling, og endringsstrømmen er fasiten. Levering minst én gang, idempotent. **Lønnskjøringen avhenger aldri synkront av en integrasjon.** | Kaostest: lønn kjøres med alle integrasjoner nede |
| 9 | **Publiserte og like grenser** | Grenser for antall kall per installasjon, ikke per avtale. Volum håndteres med batch. Lønnsdagen prioriteres for kjernen. Ingen betalt «premium-grense» i år 1. | Grensene står i dokumentasjonen og i headere |
| 10 | **Nøytral katalog og lett, lik sertifisering** | Katalogen sorteres etter kategori og deretter alfabetisk. Søsterprodukter merkes «samme eier». Ingen app er forhåndsvalgt i onboarding. Sertifisering = sjekkliste og automatisk samsvarstest i sandkassen. Den kreves for katalogen og for skrivepakker, ikke for kundens egne integrasjoner. Bruttos moduler sertifiseres på samme måte. | Kriteriene er offentlige |
| 11 | **Gratis API, ingen markedsplass i år 1** | Kunden betaler for lønn, ikke for API-kall. Partnere betaler ikke for tilgang. Inntektsdeling og markedsplass vurderes først ved 30–50 integrasjoner [R1-G]. **Kommersielle samlepakker (for eksempel Lønn + Utlegg) påvirker aldri teknisk tilgang.** | Prisliste. Åpent spørsmål om samlepakker (kap. 10). |
| 12 | **Sikkerhet og personvern er innebygd** | `private_key_jwt`, step-up for sensitive pakker, kontonummer aldri via integrasjon, fødselsnummer bare verifisert, sensitive felt aldri i webhooks uten pakke, agentrolle uten godkjenningsrett, full revisjonslogg per installasjon | Pentest. Revisjonslogg. Policytester [R1-F 3.3]. |

---

## 8. Minimum «Developer Experience»-pakke ved lansering

| # | Element | Innhold | MoSCoW | Anslag [V] |
|---|---|---|---|---|
| 1 | **Utviklerportal** (statisk) | Referanse generert fra OpenAPI. **Fire guider:** (a) Koble til en kunde (installasjon, pakker, orgnr, kilderegister), (b) Send lønnsgrunnlag og følg status, (c) Ta imot webhooks og ta igjen med endringsstrømmen, (d) Engasjement: mottakere som ikke er ansatte. **To fagguider:** «Lønn for utviklere» (perioder, cut-off, arbeidsforhold, hvorfor du ikke sender a-meldingskoder) og «Korrigeringer og § 14-15». | **Må** | M |
| 2 | **Feilkatalog** | Hver årsakskode med årsak, eksempel og løsning, på norsk og engelsk | **Må** | S |
| 3 | **Selvbetjent sandkasse** | Én tenant per utviklerkonto, syntetiske ansatte og honorarmottakere, ferdig mapping av lønnsarter, test-BankID for onboarding, og **tidsmaskin**: `POST /sandbox/clock:advance` og `POST /sandbox/pay-runs/{id}:approve\|pay\|report\|return-payment` | **Må** | M (den største posten) |
| 4 | **Appregistrering og nøkler** | `private_key_jwt`, rotasjon av nøkler, redirect-URI-er, navn og logo for samtykkeskjermen | **Må** | S |
| 5 | **Webhook-verktøy** | Registrere endepunkt, sende testhendelse, leveringslogg i 30 dager, replay, rotasjon av hemmelighet | **Må** | S |
| 6 | **Endringslogg, avviklingspolicy, statusside og likebehandlingserklæring** | Abonnement på endringer | **Må** | S |
| 7 | **Postman- eller Bruno-samling** | Generert fra OpenAPI | **Må** | S |
| 8 | **llms.txt og dokumentasjonen i markdown** | Så kodeagenter kan bygge integrasjoner | **Må** | S |
| 9 | **Åpen referanseintegrasjon** | Utlegg og vakt, vedlikeholdt av modulteamene. Brukes i byttetesten (5.3). | **Må** | S/M |
| 10 | **Supportkanal** | E-post og offentlig forum (for eksempel GitHub Discussions). Svar innen 1 virkedag. Navngitt kontakt for pilotpartnere. | **Må** | Løpende |
| 11 | Samsvarstest | Skript som kjører 25 scenarioer mot sandkassen: idempotens, sen endring, korrigering, avvisning, kildebytte | Bør | S |
| 12 | Forespørselslogg i portalen | OK-13 | Bør | S |
| 13 | TypeScript-SDK | Generert | Bør | S |
| 14 | Engelsk dokumentasjon og katalogside | | Bør | S |
| 15 | MCP-dokumentasjonsserver | | Kan | S |
| – | SDK-er i mange språk, iframe- og React-komponenter, partnerportal med inntektsrapporter, GraphQL, AsyncAPI-studio | | **Ikke nå** | |

**Samlet anslag [V]:** Omtrent én utvikler i 3 måneder pluss en lønnsfaglig skribent i 1 måned, hvis API-et er laget kontrakt-først. Det meste faller ut av OpenAPI og sandkassen.

---

## 9. Runde B: kritikk og revisjon

### 9.1 Slik så runde A ut

Runde A tok G nesten som den var og rettet bare OrgLab og Tikket. Utkastet hadde:
- en føderert plattformkjerne med felles personkatalog, SSO og fakturering
- CloudEvents-hendelser *inn* fra kildene og *ut* fra lønn
- AsyncAPI, et eget skjemaregister og Pact-tester
- et register for attributteierskap med tre profiler, ved siden av «kildeansvar per kategori» for lønnsgrunnlag
- iframe-flyter for onboarding
- vei B for alle trekkfrie linjer (`alreadyPaid=true`)
- `proposed.classification` med a-meldingskode fra kildene
- egne ressurser for mottakerforespørsel og engasjement
- OrgLab-reiser uten avgrensning
- Tikket med arbeidsforhold per arrangement
- linjer som kunne endres helt til låsing
- «utbetalt» som én status
- MCP med skriveverktøy ved lansering
- SDK-er i tre språk og partnerkatalog med sertifiseringsportal

Runde A hadde flere plattformverktøy som Må: skjemaregister, SDK-er, partnerkatalog og MCP. Runde B flyttet dem ned, men gjorde flere stoppregler om til Må.

### 9.2 Hva er overbygd for et lite team?

| Funn | Vurdering | Tiltak |
|---|---|---|
| Plattformkjerne delt på tvers av selskaper (personkatalog, SSO, entitlements, fakturering) | Stort, politisk vanskelig, og i strid med like vilkår | Fjernet (1.1) |
| Hendelser *inn* fra kildene | Dobbel kontraktsflate. Kildene må drive infrastruktur for hendelser. | Inn = REST, ut = webhooks (2.7) |
| AsyncAPI, skjemaregister-tjeneste og Pact | Tre verktøy før første partner | JSON Schema i offentlig repo og en samsvarstest |
| To eierskapsmekanismer (attributteierskap og kildeansvar) | Dobbelt så mye å bygge og forklare | **Slått sammen til ett kilderegister** (2.2). Først kuttet i B, så gjeninnført i én felles form da egne moduler og Huma kom inn. |
| Iframe/postMessage, mikrofrontender og utvidelsespunkter i lønns-UI | Mye sikkerhets- og UX-arbeid | Vertsbaserte sider og dyplenker |
| Vei B med reservasjon i to faser | Tilstandsmaskin på tvers av selskaper | Ikke nå (OK-33) |
| Egne ressurser for mottakerforespørsel og engasjement | To livsløp for samme ting | Slått sammen (2.4) |
| SDK-er i tre språk, partnerportal, markedsplass | Vedlikehold uten etterspørsel | OpenAPI-samling nå, TypeScript-SDK som Bør |
| MCP med skriveverktøy ved lansering | Risiko og lite verdi før kjernen er stabil | Agentpolicy er Må, MCP er Bør, og agenten lager bare utkast |
| Simulering av kostnad for vaktplaner | Kult, men ikke kjerne | Kan |
| **Beholdt tross kostnaden:** sandkasse med tidsmaskin, integrasjonsmonitor, engasjement med BankID, kilderegister, byttetest | Billigste vei til færre feil, mindre support og bevisbar likebehandling | – |

**Sjekk av Må-omfanget [V]:** Rapporten har 149 behov, og 90 av dem er merket Må:
- 21 kommer fra de nye kravene (egne moduler og Huma, OK-160–185).
- 11 er betingede: stoppregler, eller Må bare når noe annet leveres.
- Mange av de øvrige er regler i kode som uansett skal skrives (avvisningskoder, grenser).

Arbeidspakkene er:

| Arbeidspakke | Anslag |
|---|---|
| Offentlig API, installasjon/OAuth, webhooks og endringsstrøm | M |
| Lønnsgrunnlag v2 med katalog, holdlogikk og skyggemodus | M |
| Kilderegister og kildebytte | M |
| Fravær v1 | S/M |
| Engasjement med BankID-onboarding | M |
| Sandkasse og DX | M |
| ERP-adaptere ×2 og pull-API | M |
| Bankfil | S |
| Integrasjonsmonitor og installasjonsoversikt | S |
| Dokumentlager (basis), e-signering og import | M |
| Huma-koblingen | M |
| Agentpolicy | S |

Det tilsvarer **omtrent 2–3 utviklere i 9–12 måneder** av F-s 5–7. Det er stramt, men det passer med at F legger plattformarbeidet til kvartal 2–3 [R1-F 9.7, R1-G 4]. Hvis noe må kuttes, gjelder det Huma-koblingen (hvis ingen pilot bruker Huma), fravær v1 fra eksterne kilder (behold egen modul) og ERP-pull-API-et (behold de to adapterne).

### 9.3 Hvor kan det oppstå dobbeltregistrering?

| # | Scenario | Tiltak i B |
|---|---|---|
| D1 | Reise for en tillitsvalgt registreres både i OrgLab og i Utleggsappen | Kilderegister for `UTLEGG_REISE` per gruppe (OK-50) og duplikatsjekk på kvitterings-hash (OK-34) |
| D2 | Vakter for ekstrahjelp registreres både i Tikket og i Planday, eller i Brutto Timer | `TID` per arbeidsforholdsgruppe og overlappsjekk på tvers av kilder (OK-70) |
| D3 | Samme person opprettes to ganger (medlem i OrgLab, ansatt i Brutto, bruker i Huma) | Matching før oppretting. Brutto oppretter aldri en ny person ved et mulig treff, og slår aldri sammen automatisk (2.3). |
| D4 | Ett arbeidsforhold per arrangement eller per Huma-stilling | Brutto velger arbeidsforhold (OK-62). Et stillingsbytte i Huma blir en ny stillingsperiode (4.4.4). |
| D5 | Kunden registrerer manuelt i Brutto i tillegg til integrasjonen | Blokkert for datatyper med en ekstern kilde. Bare `MANUELL_KORRIGERING` er tillatt, og den vises i monitoren (5.1). |
| D6 | Fravær registreres i Huma *og* i Brutto Fravær, eller hentes fra NAV i begge | Én kilde for `FRAVÆR`. Brutto lager ikke fravær fra NAV når Huma er kilde (4.4.7). |
| D7 | Kunden slår på Brutto Utlegg mens Utleggsappen er aktiv | Modulen blir aktiv først etter kildebytte (5.1) |
| D8 | Byrået importerer CSV i tillegg til at integrasjonen sender | CSV-import er en kilde i kilderegisteret som alle andre (OK-81) |

### 9.4 Hvor kan det oppstå dobbel utbetaling?

| # | Scenario | Tiltak i B |
|---|---|---|
| U1 | Nytt forsøk etter tidsavbrudd | `Idempotency-Key` og (installasjon, eksternId, revisjon) |
| U2 | Kilden sender en rettelse som en *ny* linje med ny `externalId` | Ingen `supersedes`. Rettelse = ny revisjon. Ny ID med samme kvitterings-hash holdes med `POSSIBLE_DUPLICATE` (4.0.2). |
| U3 | Utleggsappen betaler direkte, og Brutto betaler også | Vei B bare for rene refusjoner som aldri sendes til Brutto. Opplysningspliktige linjer går alltid via Brutto (4.1). |
| U4 | Endring etter godkjent kjøring sendes som full linje | Brutto beregner differansen (4.0.4) |
| U5 | En linje er med i både ekstra og ordinær kjøring | En linje tilhører nøyaktig én kjøring (`IN_RUN`) |
| U6 | Returnert betaling betales på nytt av både kilden og Brutto | Bare Brutto betaler på nytt. Kilden får `payment_returned` og skal ikke betale. |
| U7 | Kilden gjenoppretter en backup og sender gamle revisjoner | `STALE_REVISION` |
| U8 | Ved kildebytte sender både gammel og ny kilde for samme periode | Byttedato, `SOURCE_RETIRED` og deling av fravær som krysser datoen (5.2) |
| U9 | Kilden viser «betalt» før banken har bekreftet, og den ansatte ber om manuell utbetaling | Skille mellom `SUBMITTED` og `CONFIRMED` (4.0.7) |

### 9.5 Hvor kan en integrasjon sende feil data rett inn i a-meldingen?

| # | Scenario | Tiltak i B |
|---|---|---|
| A1 | Kilden sender feil a-meldingsbeskrivelse | Kildene sender `kind`. Brutto mapper til lønnsart per kunde (OK-17). Manglende mapping gir hold, aldri standardverdi. |
| A2 | Integrasjonen oppretter arbeidsforhold med feil type eller datoer | Arbeidsforhold fra integrasjoner er alltid utkast som godkjennes. Typen settes av Brutto via mapping (2.4, 4.4.4). |
| A3 | Feil fødselsnummer | BankID-verifisert, eller uverifisert til skattekortet er hentet (2.2, 4.4.6) |
| A4 | Feil måned (utbetaling eller opptjening) | Kildene sender arbeidsdato. Brutto setter utbetalingsdato. |
| A5 | Testdata havner i produksjon | Sandkasse og produksjon er skilt med egne vertsnavn og nøkkelprefiks (OK-15) |
| A6 | Feil enhet (minutter og timer, øre og kroner) | Tidsstempler for vakter, beløp som tekst med to desimaler, beløpsgrenser per linjetype og skyggemodus (4.0.6) |
| A7 | Hver kilde bruker 10 000 kr-grensen for skattefrie organisasjoner selv | Bare Brutto har akkumulatoren (OK-45) |
| A8 | Frikjøp rapporteres som lønn hos organisasjonen | `NOT_PAYROLL` (OK-44) |
| A9 | En fordel er ikke merket | `isPrivateBenefit` er påkrevd uten standardverdi (OK-23) |
| A10 | Utenlandsk mottaker eller artist | Stoppregler (OK-52, OK-68) |
| A11 | Linjer kommer etter at a-meldingen er sendt | Utsettes automatisk og rapporteres i utbetalingsmåneden. Erstatningsmelding bare etter valg fra lønnsansvarlig. |
| A12 | Et stillingsbytte i Huma gir nytt arbeidsforhold i a-meldingen | Mapping av stillingsperiode (4.4.4) |
| A13 | Uklar klassifisering av tapt arbeidsfortjeneste | Bør, og `NEEDS_REVIEW` til det er fagavklart (OK-43) |
| A14 | Fravær fra Huma uten mapping, eller tapt webhook, gir feil trekk eller sykelønn | `NEEDS_MAPPING` og fraværsavstemming før cut-off (OK-184) |

### 9.6 Hva jeg endret i runde B og hvorfor

| # | Endring | Fra (A) | Til (B) | Hvorfor | Berører |
|---|---|---|---|---|---|
| 1 | Plattformkjerne | Føderert kjerne delt med søsterprodukter | Bruttos offentlige plattform. Alle er klienter. | Like vilkår og teamstørrelse | 1.1, prinsipp 1–2 |
| 2 | Retning på hendelser | Inn og ut | Inn = REST, ut = webhooks | Halverer kontraktsflaten. Gjør idempotens enklere. | 2.7 |
| 3 | Korrigering | Kilden sendte korrigerings- eller `supersedes`-linjer | Kilden sender full tilstand, og Brutto beregner differansen | Kilden vet ikke hva som er betalt, så det var risiko for dobbel utbetaling | 4.0.4, OK-25 |
| 4 | Sen endring | Linjen kunne erstattes helt til låsing | `LATE_CHANGE` etter cut-off krever et menneske | Tallene skal ikke endres etter at de er kontrollert | 4.0.3 |
| 5 | Direkte utbetaling | Alle trekkfrie linjer kunne betales utenom (`alreadyPaid`) | Bare rene refusjoner, og de sendes aldri til Brutto. Opplysningspliktige linjer går via Brutto. | Risiko for feil a-meldingsmåned og dobbel utbetaling | 4.1, OK-32/33 |
| 6 | Klassifisering | Kilden foreslo a-meldingskode. Avvik over en terskel ga avvisning. | Katalog over `kind`. Brutto mapper. Kildens totalbeløp gjelder. Avvik gir varsel. | Feil kode rett i a-meldingen, kobling til kodelisteversjoner, unødige avvisninger | OK-17, 4.1 |
| 7 | Eierskap | Attributteierskap og kildeansvar per kategori (to mekanismer) | **Ett kilderegister** for masterdata og lønnsgrunnlag, med omfang og gyldighetsdato, og kildebytte | Enklere. Nødvendig for egne moduler og for erstatning av Huma. | 2.2, 5, 6 |
| 8 | Mottakere | Egen mottakerforespørsel og eget engasjement | Ett engasjement med innebygd onboarding | Mindre API | 2.4 |
| 9 | Arbeidsforhold fra integrasjoner | Tikket kunne be om arbeidsforhold per arrangement, og Huma-stilling = arbeidsforhold | Brutto velger eller oppretter, alltid som utkast. Stillingsbytte blir stillingsperiode. | Feil i og støy fra arbeidsforhold i a-meldingen | OK-62, 4.4.4 |
| 10 | Kontonummer | OrgLab og HR kunne levere kontonummer med en pakke | Aldri via integrasjon. Engangsimport fra Huma med signering og varsel. | Svindel med endret kontonummer | 2.1, 4.4.6 |
| 11 | Ny installasjon | Rett i produksjon | Skyggemodus i første periode og beløpsgrenser | Fanger feil i mapping og enheter før a-meldingen | 4.0.6, OK-19 |
| 12 | Dimensjonen arrangement | Ukjent dimensjon → standard og varsel | Tikket kan opprette verdier av typen `arrangement` | Kostnaden per arrangement ble ellers stille feil | OK-64 |
| 13 | Vakter | Antall og enhet | Start- og sluttidspunkt | Feil med enheter | OK-60 |
| 14 | Utbetalingsstatus | «Betalt» | `SUBMITTED`, `CONFIRMED` og `RETURNED` | Brutto vet ofte ikke om pengene er betalt når kunden laster opp fil manuelt | 4.0.7, OK-101 |
| 15 | Frikjøp | Ikke behandlet | `NOT_PAYROLL` | Dobbel inntekt i a-meldingen | OK-44 |
| 16 | Integrasjonsmonitor | Bør | **Må** | Den eneste måten kunden og byrået ser feil på før a-meldingen | OK-123 |
| 17 | Dry-run | Fantes ikke | **Må** | Billig. Brukes av vei B og i test. | OK-12 |
| 18 | MCP | Må, med skriveverktøy | Agentpolicy er Må, MCP er Bør, og agenten lager bare utkast | Policy er billig tidlig. MCP er et tynt lag som kan vente. | OK-140–149 |
| 19 | DX | SDK-er i tre språk, partnerportal, iframe-komponenter | Minimal pakke (kap. 8) med referanseintegrasjon | Teamstørrelse. Referanseintegrasjonen gir samtidig dogfooding-bevis. | Kap. 8 |
| 20 | Egne moduler (nytt krav) | – | Egne OAuth-klienter, byggeregel og byttetest | Gjør likebehandlingen etterprøvbar | 5.3 |
| 21 | Huma (nytt krav) | – | Brutto bygger koblingen selv. «Varsle, så hente». Fraværsavstemming. Erstatning i tre faser. Krav fra dag én. | Humas API mangler fravær, dokumenter og lønnsresultat, og webhooks har ingen dokumentert retry [Bekreftet] | 4.4, 6 |

---

## 10. Åpne spørsmål

**Faglig, må verifiseres [U]:**
1. A-meldingsbeskrivelse for **tapt arbeidsfortjeneste** til tillitsvalgte («verv» eller noe annet), og behandling når mottakeren er næringsdrivende.
2. Vervshonorar til en person som også er ansatt i samme juridiske enhet: eget honorar-arbeidsforhold eller på det ordinære?
3. Arbeidsforholdsmodell for **ekstrahjelp og tilkalling**: ett løpende arbeidsforhold eller ett per oppdrag, stillingsprosent, og regler for korte arbeidsforhold.
4. Underenhet og AGA-sone for arrangementer utenfor fast adresse.
5. Artistskatt for utenlandske artister, og fribilletter til frivillige og ansatte som fordel.
6. **Frikjøp:** Bekreft at refusjon til en annen arbeidsgiver ikke er opplysningspliktig hos den som betaler.
7. **Kvitteringsarkiv:** Når Utleggsappen er kilde og Brutto lager bilaget, hvem oppfyller kravene til oppbevaring i bokføringsforskriften, også etter at kunden har sluttet med Utleggsappen?
8. Mapping fra Humas datoer (`contractStartDate` eller `firstDayOfWork`), `endReason` og `contractType` (`Trainee`) til a-meldingens felt og kodelister.

**Til gründeren:**

9. Er kommersielle samlepakker (Lønn + Utlegg med Utleggsappen) forenlige med «like vilkår»? Forslag: ja, hvis tilsvarende pakkerabatt kan tilbys sertifiserte tredjeparter på publiserte vilkår.
10. **Brutto Utlegg mot Utleggsappen:** Hvordan skal de posisjoneres? Hvem får plass i onboardingen? Forslag: nøytral katalog, ingen forhåndsvalgt app.
11. Skal søsterprodukter være designpartnere? Forslag: ja, men listen er offentlig og betaen åpen.
12. **Huma:** Skal Brutto søke partnerskap med Huma før fase 1, vel vitende om at målet er erstatning? Hvordan skal risikoen håndteres hvis Huma strammer inn API-tilgangen?
13. Hvor langt skal «erstatte Huma» gå? Forslag: HR-kjernen (6.4), ikke medarbeidersamtaler, undersøkelser og varsling.

**Til Utleggsappen, Advania og Huma:**

14. Vil Utleggsappen sende rene refusjoner via Brutto, eller bokføre dem selv (vei B)?
15. Har Advania krav til nettverket (faste IP-er, mTLS)?
16. **Huma:** Finnes det retry og hendelses-ID for webhooks, kan `absence-export` utløses fra API, finnes masseeksport av dokumenter og signerte avtaler, og når kommer de egne lønnshendelsene («in 2026»)?

**Teknisk:**

17. Volumet av skattekortforespørsler for mange engangsmottakere (festivaler), og grensene i Skatteetatens API [R1-B].
18. Kostnad per BankID-innlogging hos meglere ved mange små honorarer (påvirker prisen for «bare honorarer»-kunder, OK-47).

---

## 11. Kilder

**Runde 1 (i samme mappe):**
- `G-moduler-2026.md` (særlig del 1 og B1–B8)
- `F-arkitektur.md` (prinsipper, komponenter, tilgangsmodell, AI, ADR)
- `B-myndigheter.md`
- `C-beregning.md` (lønnsarter og spesialtilfeller)
- `D-praksis.md` (kap. 5 integrasjonslandskap, kap. 7 ideelle og frivillige)
- `E-byra.md` (krav fra byråene, systembruker)

**Nye oppslag 28.10.2026:**
- Skatteetaten, styrehonorar og godtgjørelser i forbindelse med verv: https://www.skatteetaten.no/nn/bedrift-og-organisasjon/arbeidsgiver/a-meldinga/rettleiinga-til-a-meldinga/lonn-og-ytingar/oversikt-over-lonn-og-andre-ytingar/styrehonorar-og-godtgjersler-i-samband-med-verv
- Huma, forside og moduler: https://www.humahr.com
- Huma, integrasjoner: https://humahr.com/no/integrasjon
- Huma, Tripletex-integrasjon: https://humahr.com/no/tripletex-og-huma-integrasjon
- Huma, priser: https://humahr.com/plans-pricing
- Huma, Open API (artikkel): https://humahr.com/knowledge/open-api
- Huma, OpenAPI-spesifikasjon 1.89.0: https://openapi.humahr.com/v3/api-docs (dokumentasjonsvisning: https://openapi.humahr.com/redoc/index.html)
- Huma, webhooks: https://humahr.com/knowledge/webhooks
- Huma, profilwebhook: https://humahr.com/knowledge/this-is-how-the-profile-webhook-work

**Søk uten treff i primærkilde:**
- Frikjøp eller refusjon til arbeidsgiver og a-melding: ingen primærkilde funnet. Kommunale skjemaer for refusjon av tapt arbeidsfortjeneste til folkevalgte viser at mønsteret er faktura fra arbeidsgiver, for eksempel https://www.rendalen.kommune.no/_f/p1/i04586f41-0f0b-40bc-844d-eff82bcd67a5/folkevalgte-utregning-av-refusjonskrav-fra-arbeidsgiver.pdf
