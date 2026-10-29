# G – Modulplattform, integrasjonskontrakter og «lønn i 2026»

**Til:** Gründerteamet for nytt frittstående lønnssystem (SaaS, 10–1000 ansatte, også lisensiert til regnskapsbyråer)
**Dato:** 28. oktober 2026
**Rolle:** Produktstrateg / plattformarkitekt
**Metode:** Nettsøk og -henting (oktober 2026) mot primærkilder der det var mulig (Skatteetaten, regjeringen.no, EFTA, utviklerdokumentasjon), ellers sekundærkilder. Kilde-URL står ved påstanden og samlet i kapittel 6.

**Hvor sikre påstandene er:**
- **[P]** Bekreftet i en primærkilde (myndighet, offisiell dokumentasjon, selskapets egen pressemelding).
- **[S]** Sekundærkilde (bransjemedier, analyse- og konsulentblogger, leverandørsammenligninger). Kan være unøyaktig.
- **[U]** Usikkert, motstridende eller ikke verifisert. Må sjekkes før det brukes i salg eller jus.
- **[V]** Min egen vurdering eller anbefaling, ikke et faktum.

OrgLab og Tikket er brukt som **eksempler på modultyper** (organisasjon/HR og tid/registrering). Jeg har ikke hentet inn fakta om dem. Alt som står om dem, beskriver hvordan en slik modul *bør* kobles på.

---

## 0. Hovedkonklusjoner

1. **Bygg en «føderert compound-plattform», ikke en monolitt.** Rippling får verdi av at alle modulene leser fra og skriver til én ansattgraf i én database [S]. Dere kan ikke gjøre det samme, fordi Utleggsappen er et eget produkt med egen drift hos Advania [S]. Bygg i stedet de samme egenskapene som felles tjenester: identitet, virksomhets- og personregister, ID-mapping, samtykke, hendelser og fakturering. Modulene eier fortsatt sine egne data. [V]
2. **Det viktigste kravet i 2026 står ikke på trendlistene: myndighetsintegrasjonen.** Fra 2026 er API den eneste måten å sende a-melding fra et system på [P]. Innsending via system krever **systembruker og tilgangspakker** i Altinn 3. Eksisterende roller gjelder bare ut 2026 [P]. Skattekort hentes via nytt API med Maskinporten og systembruker [P]. Et nytt lønnssystem som gjør dette elegant, særlig klientdelegering for byråer, har et konkret salgsargument nå. [V]
3. **Lønn eier lønnsfakta, ikke alt.** Bruk et register over hvem som eier hvilke attributter. Lønn må kunne være eier av alt når kunden ikke har en HR-modul, og gi fra seg eierskapet til attributtgrupper når for eksempel en OrgLab-type modul kobles på. [V]
4. **Lønnsgrunnlag inn, lønnsresultat ut.** Alle moduler (Utleggsappen, tid, fravær, bonus) leverer *lønnsgrunnlag* gjennom én felles kontrakt med idempotens, versjonering og en låsemekanisme. Lønn leverer tilbake *utbetalt og bokført*-hendelser. PowerOffice Go sitt salary lines-API har det samme mønsteret: linjer som låses når de er tatt inn i en lønnskjøring [P].
5. **Hendelsesstandard:** Bruk CloudEvents 1.0 som konvolutt (CNCF «graduated» siden januar 2024 [S]) og Standard Webhooks for signering, levering og replay-vern [S]. Kontraktene publiseres i et skjemaregister, og egne moduler bruker de samme offentlige kontraktene som tredjeparter, uten bakdører.
6. **Samtykke etter Altinn-modellen:** Kunden «installerer» en modul og godkjenner navngitte **tilgangspakker** (for eksempel «Lønnsgrunnlag – skrive», «Ansattidentitet – fødselsnummer»). Tilgangen kan trekkes tilbake, og alt logges. Byråer får klientdelegering. [V]
7. **Lønnstransparens:** EU-direktivet 2023/970 er **ikke** innlemmet i EØS-avtalen, og EU-fristen 7. juni 2026 gjelder ikke Norge [P]. ARP og lønnskartlegging etter likestillings- og diskrimineringsloven § 26 gjelder allerede og er et krav nå [P]. Å bygge en datamodell som er klar for direktivet er et fortrinn i dag og vil trolig bli et krav i 2027–2028 [V/U].
8. **KI:** I 2026 forventer markedet avviksdeteksjon og avviksforklaring før godkjenning. Gusto, Deel og SD Worx lanserer KI-agenter i lønn [S/P]. «Spør lønnsslippen» og et MCP- eller agent-API skiller dere fra andre. **Autonom kjøring uten et menneske som godkjenner er for tidlig** (ansvar, feilrisiko). KI-forordningen er dessuten utsatt både i EU og Norge, så rammene er fortsatt i bevegelse [P/S].
9. **Lønn på forskudd (EWA), Vipps-utbetaling, sanntidslønn og lønn i flere valutaer:** Mest hype i det norske segmentet. Straksbetaling finnes som infrastruktur (NICS Real/Straks) [S], men jeg fant ikke noe offentlig API for utbetaling fra Vipps MobilePay [P]. Arbeidsgiverfinansiert lønnsforskudd er lovlig med skriftlig avtale og skattetrekk [S], men har lite produktverdi. [V]
10. **Forretningsmodell for en liten aktør:** Tilby en kjerne og 2–3 modulpakker, en byrålisens med forutsigbar pris, gratis offentlig API og en sertifiseringsordning for partnere. **Ikke** bygg en markedsplass med fakturering og inntektsdeling før dere har rundt 30–50 integrasjoner og etterspørsel fra kundene. Få dere heller oppført hos unified-API-leverandører som Kombo, Apideck og Merge som en kanal. [V]

---

# DEL 1 – Modulplattform og økosystem

## 1.0 Referanser: hva de andre gjør og hva dere kan lære

| Referanse | Hva de gjør | Lærdom for dere |
|---|---|---|
| **Rippling** («compound startup») | En ansattgraf er datalaget under 25+ produkter. Én ansettelse kan utløse tilbud, forsikring, kontoer, utstyr, lønn og kort [S] ([rippling.com/platform](https://www.rippling.com/platform/analytics), [Sacra](https://sacra.com/research/rippling), [SaaStr](https://saastr.com/ripplings-ai-bet-the-data-graph-is-the-moat)) | Verdien ligger i én sannhet og hendelser på tvers av moduler. Dere må få det til *føderert*, med ID-mapping og hendelser og uten felles database. Ulempen med Rippling-modellen er at den er meningsstyrt og forutsetter at Rippling er sannheten. Det fungerer dårlig når kunden allerede har et HR-system [S]. |
| **Gusto Embedded** | Lønn som API og innebygde UI-«Flows» via lenke eller iframe, i tillegg til et React SDK. Fra v2024-03-01 sender Flows hendelser til vertsappen [P] ([docs.gusto.com flows](https://docs.gusto.com/embedded-payroll/docs/flows-intro), [changelog](https://docs.gusto.com/embedded-payroll/changelog/added-flow-events)) | Tre nivåer av innbygging (API, ferdige komponenter, iframe-flyt). Flyten må fortelle vertsappen når brukeren er ferdig. Gusto skriver selv at iframe-flyter har begrenset stilstyring [P]. |
| **Check (checkhq)** | «Components»: ferdige lønnsflyter som legges inn med få kodelinjer [P] ([docs.checkhq.com](https://docs.checkhq.com/reference-link/components-overview)) | Samme som over. Komponenter kan bli et eget produkt. |
| **Personio Marketplace** | Partnerprogram med godkjenning og utviklerkonto. Webhooks i API v2 for person.* og employment.* (opprettet/endret/startet/avsluttet). Partnerintegrasjoner er ofte enveis, fra Personio til partneren [P/S] ([developer.personio.de webhooks](https://developer.personio.de/v2.0/reference/webhooks), [partner](https://www.personio.com/partner/tech), [marketplace](https://www.marketplace.personio.com/)) | Begynn med hendelser på få kjerneobjekter (person og arbeidsforhold). Vær bevisst på hvem som får skrive. Partnergodkjenning beskytter kvaliteten. |
| **HiBob** | Markedsplass med kategorier for lønn, EOR og regnskap. Egen lønn bare i noen land, resten via partnere. Har ifølge tredjepart offentlig API, webhooks og MCP-server [S/U] ([hibob.com/integrations](https://hibob.com/integrations/), [erpresearch](https://erpresearch.com/erp-add-ons/hcm-extensions/hibob)) | HR-plattformer kobler seg på lønn via partnere. Dere bør være en god lønnspartner for HR-systemer (HiBob, Personio og lignende), ikke bare for egne moduler. |
| **Deel API** | Webhooks for kontrakt, arbeider, lønn og faktura. Global Payroll API: *send inn lønnsgrunnlag, hent lønnsresultat* [P/S] ([developer.deel.com webhooks](https://developer.deel.com/api/webhooks/introduction), [global payroll](https://developer.deel.com/api/global-payroll), [Supergood](https://supergood.ai/api-report-card/deel)) | Grensesnittet «lønnsgrunnlag inn, resultat ut» er nettopp den kontrakten dere trenger. |
| **Finch / Merge / Kombo / Apideck** (unified HRIS-API) | Normaliserer HR- og lønnsdata på tvers av hundrevis av systemer. Finch sier den er alene om å kunne *skrive* lønnstrekk programmatisk (USA) [S]. Kombo er europeisk og Berlin-basert, men norsk dekning er uklar [S/U]. Apideck sier Visma.net Payroll er det lønnssystemet som nevnes oftest i Regnskap Norges undersøkelse for 2025, men har det bare «på radaren» [S] ([Finch](https://tryfinch.com/vs/merge), [Knit om Kombo](https://www.getknit.dev/blog/a-detailed-evaluation-of-kombo-as-a-unified-hr-api-platform), [Apideck Norge](https://www.apideck.com/integrations/country/norway/hris)) | (1) **Kanal:** Bli koblet til av unified-API-leverandørene, så kommer hundrevis av HR-, forsikrings- og pensjonsverktøy til dere. (2) **Innhenting:** Bruk dem til å lese HR-masterdata hos kunder som har Personio, HiBob og lignende, i stedet for å bygge hver kobling selv. |
| **Visma Developer / Visma Connect** | Apper registreres i Visma Developer Portal (client-id/secret, tenant via invitasjonskode). Visma.net HRM/Payroll-API. App Store og ISV-partnerprogram. Visma Connect er felles innlogging på tvers av produktene [S] ([HelloID-README](https://github.com/Tools4everBV/HelloID-Conn-Prov-Source-Visma.net-HRM-API/blob/main/README.md), [vismasoftware.no/api](https://www.vismasoftware.no/api-en), [FlexHRM release notes](https://www.flexhrm.com/release-notes?page=62)) | Den største aktøren bygde **felles identitet og felles utviklerportal** først. Dere bør gjøre det samme fra dag 1. |
| **Tripletex API v2** | Tre token-typer: consumer token (fra Tripletex), employee token (laget av kundens administrator) og session token. Lønnslinjer kan skrives via API (RecMan-integrasjonen). Over 100 integrasjoner og 150 000 kunder (nov. 2025) [S/P] ([rubydoc tripletex_api](https://rubydoc.info/gems/tripletex_api/index), [RecMan](https://help.recman.io/hc/en-us/articles/33443902243346), [Visma/Cision](https://publish.ne.cision.com/Release/ViewReleaseHtml/82E61C8B666E36B0)) | Tokenmodellen er enkel for SMB, men tungvint for byråer med mange klienter. Tripletex er det viktigste regnskapsmålet for bilagseksport. |
| **PowerOffice Go API** | **Salary Lines**: linjer importeres til en fremtidig lønnskjøring, kan endres (PATCH) eller slettes til de er tatt inn i et lønnsutkast, og er **låst** etter det. Slettede linjer kan fortsatt hentes. Kunden må ha lønnsmodulen. PowerOffice anbefaler sine egne ID-er som mapping-nøkkel [P] ([developer.poweroffice.net salary lines](https://developer.poweroffice.net/workflows/endpoints/payroll/salary-lines)) | Den beste norske malen for livssyklusen til lønnsgrunnlag: upsert, låsing og sporbar sletting. Kopier mønsteret. |
| **Fiken API v2** | OAuth2-apper, opptil 5 tilkoblede brukere gratis under utvikling. API-modulen koster 99 kr/mnd ifølge BDO [S/U] ([Chift](https://docs.chift.eu/connectors/accounting/fiken), [BDO](https://www.bdo.no/en-gb/services/audit-and-assurance/transferring-accounting-data/fiken)) | Fiken har egen enkel lønn. Dere trenger først og fremst bilagseksport dit for kunder som har vokst ut av Fiken-lønn. |
| **Altinn 3 / Maskinporten / systembruker** | Systembruker er en upersonlig bruker som virksomheten gir fullmakt via **tilgangspakker**. Klientdelegering styrer hvilke ansatte i et byrå som kan handle for hvilke klienter. I Altinn 3 er det Maskinporten som utsteder samtykketokener [P] ([Skatteetaten regnskapsfører](https://www.skatteetaten.no/nn/samarbeidspartnere/reetablering-altinn/regnskapsforer-revisor/), [Skatteetaten virksomheter](https://www.skatteetaten.no/samarbeidspartnere/reetablering-altinn/virksomheter/), [docs.altinn.studio](https://docs.altinn.studio/en/api/authentication/)) | Det er nettopp denne modellen deres eget samtykke per modul bør likne: navngitte pakker, kunden godkjenner, upersonlig systemidentitet, klientdelegering. Norske kunder og byråer kjenner den allerede. |
| **CloudEvents 1.0** | CNCF-spesifikasjon for hendelseskonvolutter: id, source, type, subject, time, dataschema og utvidelser som partitionkey. «Graduated» 25. januar 2024 [S] ([cloudevents.io](https://cloudevents.io/), [InfoQ](https://www.infoq.com/news/2024/04/cncf-cloudevents-graduation)) | En nøytral konvolutt gir felles verktøy (Kafka, Azure Event Grid, Knative) og lavere terskel for partnere. |
| **Standard Webhooks** | Headerne `webhook-id`, `webhook-timestamp` og `webhook-signature` (v1 = HMAC-SHA256 over «id.timestamp.body», v1a = Ed25519). Anbefalt toleranse rundt 5 minutter. Flere signaturer er tillatt for nøkkelrotasjon [S] ([webhookrelay](https://webhookrelay.com/verify-standard-webhooks-signature/), [Svix-ordliste](https://www.svix.com/resources/glossary/webhook-signature/)) | Ta det i bruk fra start. Partnere kan da bruke ferdige biblioteker. |

**Samlet lærdom [V]:** De som lykkes, har (a) én kanonisk modell for ansatt og arbeidsforhold, (b) få, stabile hendelsestyper på kjerneobjekter, (c) en avgrenset kontrakt for *skriving* (lønnsgrunnlag), (d) en partnerport med godkjenning, og (e) felles identitet tidlig. Ingen av de vellykkede starter med en markedsplass.

---

## 1.1 Målbilde

```
                     ┌──────────────────────── Plattformkjerne (felles tjenester) ─────────────────────────┐
                     │  Identitet (OIDC/SSO, BankID, passkeys) · Virksomhetsregister (orgnr/underenheter)  │
                     │  Personkatalog + ID-mapping · Attributteierskap · Samtykke/tilgangspakker           │
                     │  Hendelsesbuss (CloudEvents) + webhook-levering · Skjemaregister · Revisjonslogg    │
                     │  Entitlements/fakturering · Utviklerportal/sandkasse · Designsystem/UI-SDK          │
                     └───────────────▲───────────────────▲───────────────────▲──────────────────▲─────────┘
                                     │                   │                   │                  │
     ┌───────────────┐   lønnsgrunnlag   ┌──────────────────────┐   bilag   ┌─────────────┐  betaling ┌──────┐
     │ Utleggsappen  │ ───────────────▶ │                      │ ────────▶ │  Regnskap   │           │ Bank │
     │ (Advania)     │ ◀─────────────── │      LØNN (kjerne)   │ ─────────────────────────────────▶ │      │
     └───────────────┘   utbetalt/feil   │  beregning · a-mld   │ ◀──────── bokført ── ◀── status ── └──────┘
     ┌───────────────┐   org/stilling    │  skattekort · AGA    │  pensjonsgrunnlag ┌──────────┐
     │ OrgLab-type   │ ───────────────▶ │  feriepenger · NAV   │ ────────────────▶ │ Pensjon  │
     └───────────────┘                   │                      │                   └──────────┘
     ┌───────────────┐   timer/fravær    │                      │   lønnsslipp      ┌─────────────────┐
     │ Tikket-type   │ ───────────────▶ │                      │ ────────────────▶ │ Ansattportal /  │
     └───────────────┘ ◀── cut-off/lås ──└──────────┬───────────┘                   │ Digipost        │
                                                    │ API + Maskinporten/systembruker└─────────────────┘
                                         ┌──────────▼──────────┐
                                         │ Skatteetaten (a-mld, │
                                         │ skattekort), NAV     │
                                         └──────────────────────┘
```

**Prinsipp [V]:** Modulene snakker med hverandre via kjernens hendelser og offentlige API-er. Ingen modul leser en annens database. Lønn er én modul blant flere, men den eneste som snakker med Skatteetaten om lønn.

---

## 1.2 (a) Felles identitet

Tre typer identitet, hver med sin løsning:

| Identitetstype | Hvem | Anbefaling [V] |
|---|---|---|
| **Mennesker – virksomhetsbrukere** | Lønnsansvarlig, HR, leder, økonomi | OIDC-basert SSO som felles innlogging på tvers av moduler («én konto, mange moduler», slik Visma Connect gjør det). Støtt Entra ID og Google som føderasjon for kunder som ønsker det. **Passkeys** som standard 2FA. BankID som ekstra steg (step-up) for kritiske handlinger: godkjenne lønn, endre kontonummer, godkjenne systembruker. |
| **Mennesker – ansatte** | Alle ansatte (ansattportal, Utleggsappen) | Én ansattidentitet på tvers av appene (samme pålogging i Utleggsappen og lønnsslippen). BankID eller ID-porten-nivå ved første gangs aktivering og ved endring av sensitive data. Passkeys etterpå. NB: Fra april 2026 er **Stø** (tidligere BankID BankAxept AS) utsteder av BankID, og mange brukere blir bedt om å identifisere seg på nytt i appen [S] ([bytt.no](https://www.bytt.no/artikler/forbruker/a-jpml/alternativer-til-bankid-slik-beholder-du-tilgangen-til-nav-og-helsenorge-i-2026), [Altinget](https://www.altinget.no/digital/artikkel/politiet-advarer-mot-bankid-panikk-blant-eldre-trodde-de-kunne-miste-sparepenger)). Bruk en mellomvare (for eksempel Signicat, Criipto eller ID-porten) så dere ikke integrerer direkte mot hver eID. |
| **Mennesker – byrå** | Regnskapsførere med mange klienter | **Byråorganisasjon** med egne brukere og *klientdelegering* (hvem i byrået har tilgang til hvilken klient, med hvilke rettigheter). Speil Altinns modell, for eksempel med pakken «Regnskapsfører lønn» [P]. |
| **Maskiner – moduler og partnere** | Utleggsappen, OrgLab, partnere | OAuth2 client credentials per *installasjon* (kunde × modul), med scopes avledet av godkjente tilgangspakker. Helst privat nøkkel og JWT (`private_key_jwt`) eller mTLS i stedet for delte hemmeligheter. |
| **Maskiner – myndigheter** | Skatteetaten, NAV | Maskinporten-klient og **systembruker** per kunde med riktige tilgangspakker (A-ordningen / Regnskapsfører lønn) [P]. Dere er *systemleverandør*. Kunden godkjenner systembrukeren i Altinn. |

**Viktig for 2026 [P]:** Skatteetaten skriver at innsending via system krever tilgangspakker for de reetablerte tjenestene fra **31. mai 2026**. **19. juni 2026** var siste frist for å delegere Altinn-roller. Eksisterende tilganger beholdes til **31. desember 2026**, og fra januar 2027 kreves riktig tilgangspakke ([Skatteetaten regnskapsfører/revisor](https://www.skatteetaten.no/nn/samarbeidspartnere/reetablering-altinn/regnskapsforer-revisor/), [Skatteetaten levering fra system](https://www.skatteetaten.no/nn/bedrift-og-organisasjon/arbeidsgiver/a-meldinga/levere-a-melding/levering-fra-system/)). Tripletex beskriver lukking av A02/A03/A06/A07 fra system i Altinn II 15. juni 2026 [S] ([Tripletex hjelp](https://hjelp.tripletex.no/hc/no/articles/46595139601937)). **Ny kunde-onboarding må derfor ha en veiviser for systembruker.**

## 1.3 (a) Felles virksomhets- og personregister?

**Virksomhetsregister: ja, og hent det fra Enhetsregisteret [V].**
- Tenant = juridisk enhet (orgnr). Underenheter (virksomheter med eget orgnr) hentes automatisk. De trengs i a-meldingen og avgjør sone for arbeidsgiveravgift via kommunen.
- Én kunde kan ha flere juridiske enheter (konsern, eller stiftelse + AS). Modeller en «kundekonto» over flere tenants.
- Byrå = egen organisasjonstype med klientrelasjoner.

**Personregister: ja, men minimalt («Personkatalog», ikke HR-master) [V].**
- Kjernen eier: plattformens `personId` (stabil og pseudonym), navn, kontaktpunkter, påloggingsidentiteter og koblingstabell til modul-ID-er (Utleggsappen-ID, OrgLab-ID, ansattnummer).
- **Fødselsnummer/D-nummer** lagres kryptert på eget sted. Det deles bare med moduler som har godkjent tilgangspakken «Ansattidentitet» (lønn, pensjon). Utleggsappen trenger det normalt ikke og bør klare seg med `personId`.
- Unngå gudeobjektet: Personkatalogen skal ikke ha lønn, stilling eller fravær. Det hører til modulene som eier dataene.

**Hvorfor ikke en full felles HR-master i kjernen? [V]** Kunder på 200–1000 ansatte har ofte Personio, HiBob, Simployer eller Visma som HR-master. Hvis kjernen *krever* å være masteren, mister dere dem. Løsningen er attributteierskap (1.5).

## 1.4 (a) Kanonisk modell for ansatt og arbeidsforhold

Modellen bør følge **a-meldingens arbeidsforholdsbegrep**, fordi det er det lønn til slutt må rapportere. Den bør også ha **gyldighetsdatoer** (effective dating), og helst bitemporalitet: *gyldig fra/til* og *registrert tidspunkt*.

| Objekt | Nøkkelfelt (utdrag) | Kommentar |
|---|---|---|
| **Person** | personId, navn, fødselsnr (beskyttet), statsborgerskap*, språk, kontakt | *Bare når det trengs (for eksempel for kildeskatt eller PAYE). |
| **Arbeidsforhold** (Employment) | employmentId, personId, juridisk enhet, underenhet (orgnr), type (ordinært/maritimt/frilans/pensjon), start/slutt, sluttårsak, stillingsprosent, arbeidstidsordning, yrkeskode (STYRK-08), ansettelsesform, lønnsform (fast/time), tariffavtale-ref, ansiennitet | Ett arbeidsforhold per a-meldingsrelasjon. Person og arbeidsforhold er én-til-mange. |
| **Organisasjonsenhet** | orgUnitId, navn, forelder, gyldighet, kostnadssted, leder-ref | Eies av OrgLab-typen hvis den finnes. |
| **Stilling** (Position) | positionId, tittel, orgUnit, stillingskategori («arbeid av lik verdi»), lønnsramme/-band | Viktig for lønnstransparens (DEL 2). |
| **Lederrelasjon** | employmentId → managerEmploymentId, type (linje/godkjenner/fag) | Brukes til godkjenningsflyt i Utleggsappen og Tikket. |
| **Kostnadsdimensjon** | dimensjonstype (avdeling/prosjekt/kostnadssted/egendefinert), kode, gyldighet, kilde-ID i regnskap | Regnskapet er sannheten for koder. Moduler refererer til dem. |
| **Lønnsart** (PayElement) | kode, navn, a-meldingsbeskrivelse (fra kodeliste), trekkpliktig, AGA-pliktig, feriepengegrunnlag, pensjonsgrunnlag, kontomapping | Eies av lønn. |
| **Lønnsgrunnlag** (PayInput) | kilde, ekstern ID, versjon, employmentId, lønnsart/klassifisering, antall, sats, beløp, periode, dimensjoner, status | **Den felles skrivekontrakten** for alle moduler (1.11). |
| **Lønnskjøring / Lønnsslipp / Bilagsbunt / Betalingsbunt** | … | Eies av lønn og publiseres som hendelser. |

## 1.5 (a) Attributteierskap: hvem eier sannheten?

Konfigureres per tenant, slik at lønn kan stå alene **eller** samarbeide med en HR-modul:

| Attributtgruppe | Lønn alene | Lønn + OrgLab-type | Lønn + OrgLab + Tikket-type |
|---|---|---|---|
| Person (navn, kontakt) | Personkatalog | Personkatalog (OrgLab skriver) | samme |
| Fødselsnummer/D-nummer | Lønn | Lønn (eller OrgLab med pakken) | samme |
| **Bankkonto for lønn** | **Lønn/ansattportal** | **Lønn/ansattportal** | samme. *Bør aldri eies av HR-modulen, fordi svindel med endret kontonummer er en kjent angrepsvei [V].* |
| Org.struktur, leder, kostnadssted | Lønn (enkel) | **OrgLab** | OrgLab |
| Stilling, stillingsprosent, yrkeskode, start/slutt | Lønn | **OrgLab** (lønn validerer mot a-meldingens regler) | OrgLab |
| Fastlønn, timesats, tillegg | Lønn | Lønn (eller OrgLab som «kompensasjonsmaster», valgfritt) | Lønn |
| Skattekort | Lønn (fra Skatteetaten) | Lønn | Lønn |
| Arbeidstid/timer | Lønn (manuelt) | Lønn | **Tikket** |
| Fravær og permisjon | Lønn | Lønn/OrgLab | **Tikket** (lønn eier konsekvensen i lønn og NAV) |
| Utlegg og reise | – | – | **Utleggsappen** (lønn eier a-meldingsklassifiseringen) |
| Lønnsresultat, a-melding, AGA, feriepenger | Lønn | Lønn | Lønn |

**Regel [V]:** Bare eieren kan skrive. Andre moduler får hendelser og kan *foreslå* endringer via API (et endringsforslag som eieren godtar eller avviser). Konflikter løses av eieren, aldri av siste skriver.

## 1.6 (a) Hendelser: CloudEvents og webhooks

**Konvolutt (eksempel) [V]:**

```json
{
  "specversion": "1.0",
  "id": "01JBX9Q7M3K8T2V5N6R4P0WZ1E",
  "source": "urn:plattform:module:lonn:tenant:987654321",
  "type": "no.plattform.payroll.payrun.paid.v1",
  "subject": "payrun/pr_2026-11",
  "time": "2026-11-20T06:01:12Z",
  "datacontenttype": "application/json",
  "dataschema": "https://schemas.plattform.no/payroll/payrun.paid/v1.json",
  "partitionkey": "tenant:987654321",
  "tenantid": "987654321",
  "sequence": "000000000000004711",
  "data": { "payRunId": "pr_2026-11", "payDate": "2026-11-20", "lines": [ /* refs til kildelinjer */ ] }
}
```

**Regler [V]:**
- **Navngiving:** `no.plattform.<domene>.<objekt>.<hendelse>.v<major>`. Hendelser beskriver fakta i fortid (`approved`, `paid`, `locked`), ikke kommandoer.
- **Levering:** Minst én gang (at-least-once). Mottakeren må deduplisere på `id`. Rekkefølge garanteres bare per `partitionkey` (per tenant eller per arbeidsforhold), med et `sequence`-felt.
- **Fete nok hendelser:** Ta med de feltene mottakeren trenger i 80 % av tilfellene, pluss en lenke for å hente full ressurs. Det gir færre tilbakekall. Sensitive felt (fødselsnummer, beløp per person) skal aldri ligge i hendelser til moduler uten den tilgangspakken. Da sendes en tynn hendelse med henting via API.
- **Webhooks:** Standard Webhooks-headere og signering, automatisk retry med eksponentiell backoff i opptil 3 dager, dead-letter-kø synlig for kunden, rotasjon av hemmeligheter med to gyldige signaturer i overgangen.
- **Replay:** Endepunktet `GET /events?after=<sequence>` (endringsstrøm) lar partnere ta seg inn igjen etter nedetid uten å be om ny sending. Webhooks er bare en varsling. Strømmen er sannheten.
- **Utgående side:** Bruk outbox-mønsteret (hendelsen skrives i samme transaksjon som tilstandsendringen) så det ikke oppstår «spøkelseshendelser».
- **Katalog:** Dokumenter alt i AsyncAPI og JSON Schema i et offentlig skjemaregister. Bare additive endringer innen en major-versjon. Breaking changes betyr ny `.v2` og at v1 kjøres parallelt i minst 12 måneder.

## 1.7 (a) API: REST eller GraphQL?

| Valg | Anbefaling [V] | Begrunnelse |
|---|---|---|
| **Offentlig API** | **REST + OpenAPI 3.1** | Alle norske referanser (Tripletex, PowerOffice, Fiken, Visma, Altinn) er REST, og byråer og integratører kan det. Det er lettere å cache, hastighetsbegrense, revidere og versjonere. |
| **GraphQL** | Bare internt som BFF for eget UI, eventuelt et lesebasert GraphQL senere | Skriving i lønn må være eksplisitt og revisjonssporet. GraphQL-mutasjoner gir mindre tydelige kontrakter. Det er nyttig til sammensatte lesebilder i ansattportal og dashboards. |
| **Bulk** | `POST /pay-inputs:batch` med opptil N linjer og delvis suksess per linje | Byråer og tidssystemer sender hundrevis av linjer. |
| **Idempotens** | `Idempotency-Key`-header på alle POST-kall, og naturlig nøkkel (kilde, eksternId, versjon) på lønnsgrunnlag | Gjør retry trygt. |
| **Samtidighet** | `ETag` og `If-Match` på oppdatering | Unngår at siste skriver vinner. |
| **Paginering** | Markørbasert | Stabilt ved store datamengder. |
| **Sandkasse** | Selvbetjent sandkasse-tenant med syntetiske ansatte og a-melding mot Skatteetatens testmiljø | Skatteetaten tilbyr test, og produksjonsdelen av det nye API-et lanseres «senere» ifølge SBS-siden [P] ([Skatteetaten SBS](https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/a-meldingen-sbs/)). |
| **Agent-API (MCP)** | En MCP-server over det offentlige API-et, med de samme tilgangspakkene og *uten* godkjenningsrett | Gusto, Deel og HiBob (ifølge tredjepart) åpner for KI-assistenter [S]. Billig å lage og gir mye synlighet (DEL 2.4). |

## 1.8 (a) Innebygde UI-flater

| Nivå | Teknikk | Bruk [V] |
|---|---|---|
| 1. Dyplenker med kontekst | Signerte, kortlevde lenker (`/payslip/123?ctx=…`) og felles navigasjonsskall | Raskest. Godt nok for lenker mellom Utleggsappen og lønn. |
| 2. Innebygde flyter | **Iframe med postMessage-kontrakt** (som Gusto Flows) eller Web Components. Kortlevd sesjonstoken utstedt av kjernen. CSP `frame-ancestors` begrenset til kjente vertsapper. Hendelsene `flow.completed`, `flow.cancelled` og `flow.resized` | Eksempler: «Vis lønnsslipp» i ansattportalen, «Godkjenn lønnsgrunnlag» inne i Tikket, «Sett opp systembruker» i byråportalen. |
| 3. Mikrofrontender | Module Federation og delt designsystem | **Bare mellom egne moduler.** Gir tett kobling i byggeprosessen og passer ikke for tredjeparter. |
| 4. Utvidelsespunkter | Navngitte plasser i lønns-UI (for eksempel en fane på ansattkortet) der en installert modul kan vise en iframe | Gir partnere plass i lønns-UI uten at dere skriver kode for dem. |

**Sikkerhet [V]:** Sjekk alltid `event.origin` i postMessage, bruk iframe-sandbox, send aldri token i URL ut over én bruk, og skill innebygd sesjon fra hovedsesjonen.

## 1.9 (a) Samtykke og tilgang per modul (Altinn-inspirert)

**Installasjonsflyt [V]:**
1. Kundeadministratoren velger «Installer Utleggsappen» (eller en partnerapp).
2. Skjermen viser **tilgangspakkene** modulen ber om, med formål og databehandleravtale.
3. Administratoren godkjenner, med BankID-steg for pakker som omfatter identitet eller lønn. Det opprettes en installasjon (tenant × modul) med OAuth-klient og scopes.
4. Alt logges: hvem, hva, når og hvilken versjon av pakkedefinisjonen.
5. Tilgangen kan trekkes tilbake når som helst. Da stoppes webhooks og tokens umiddelbart, og modulen får hendelsen `installation.revoked`.

**Forslag til tilgangspakker [V]:**

| Pakke | Gir | Typisk modul |
|---|---|---|
| Virksomhet – basis | orgnr, underenheter, dimensjoner | alle |
| Ansatt – basis | personId, navn, e-post, arbeidsforhold (aktiv/ikke), org.enhet, leder | Utleggsappen, Tikket |
| Ansatt – identitet | fødselsnr/D-nr | pensjon, forsikring |
| Ansatt – bankkonto (les) | kontonummer | bank-/utbetalingsmodul |
| Lønnsgrunnlag – skrive | opprette og endre egne lønnsgrunnlag | Utleggsappen, Tikket |
| Lønnsresultat – egne linjer | status og utbetaling for linjer modulen selv har levert | Utleggsappen |
| Lønnsresultat – individ | lønnsslipp-data | ansattportal, pensjon |
| Lønnsresultat – aggregert | summer per enhet eller dimensjon | regnskap, BI |
| Fravær – helse | fraværsårsak = sykdom (særlige kategorier, GDPR art. 9) | **bare lønn/NAV-flyt.** Andre moduler ser bare «fraværende». |
| Organisasjon – skrive | org.struktur og stillinger | OrgLab-type |

**Byrå:** En byråbruker handler for en klient bare når (a) klienten har godkjent byrået og (b) byrået har delegert klienten til brukeren. Det tilsvarer klientdelegering i Altinn [P].

## 1.10 (a) Fakturering per modul

- **Entitlements-tjeneste i kjernen:** Hvilke moduler og pakker hver tenant har, med grenser. Alle moduler spør den, eller får innholdet i token-claims.
- **Måling via hendelser:** Lønn sender `billing.usage` (for eksempel «aktiv ansatt = fikk lønnsslipp i måneden»). Andre moduler måler sitt eget. Kjernen lager én samlet faktura, eller én per modul hvis Utleggsappen fakturerer selv.
- **Byråfakturering:** Grossistpris til byrået, som fakturerer klienten selv, eller direkte fakturering av klienten med byrårabatt. Begge må støttes.
- **Inntektsdeling** mellom søsterselskaper eller partnere beregnes fra de samme måledataene, så det blir ingen diskusjon om tallgrunnlaget.

---

## 1.11 (b) Integrasjonskontrakter

### Felles konvensjoner for alle «X → lønn»-kontrakter

**Livssyklus for lønnsgrunnlag [V]** (etter mønster fra PowerOffice Go salary lines [P]):

```
RECEIVED ─▶ VALIDATED ─▶ ACCEPTED ─▶ LOCKED (tatt inn i lønnskjøring) ─▶ PAID ─▶ REPORTED (a-melding)
     │            │            │
     └──▶ REJECTED (med årsakskode)   └──▶ WITHDRAWN (kilden trakk linjen før låsing)
```

- **Idempotensnøkkel:** `(kilde, eksternId, versjon)`. Samme nøkkel gir ingen endring. Ny versjon med samme eksternId erstatter forrige versjon **til linjen er låst**.
- **Etter låsing:** Bare **korrigeringslinjer** (motpost og ny linje) i neste lønnskjøring, med henvisning til opprinnelig linje.
- **Cut-off:** Lønn publiserer `payroll.period.cutoff_scheduled` og `payroll.period.locked`. Linjer etter cut-off går automatisk til neste periode, og kilden får beskjed om det.
- **Årsakskoder** (maskinlesbare): `EMPLOYMENT_NOT_FOUND`, `EMPLOYMENT_ENDED`, `PERIOD_LOCKED`, `INVALID_CLASSIFICATION`, `RATE_EXCEEDS_LIMIT`, `MISSING_DIMENSION`, `DUPLICATE`, `NEGATIVE_NET_NOT_ALLOWED`, `REQUIRES_WRITTEN_AGREEMENT`.
- **A-meldingsperspektivet:** Lønn rapporteres i utbetalingsmåneden. En retting av en innsendt måned gjøres ved å sende en ny a-melding for samme måned som erstatter den forrige [V/P – følger a-ordningens prinsipper]. Kontraktene må derfor bære både `opptjeningsperiode` og `utbetalingsdato`.
- **Trekk i lønn:** Hvis en korrigering fører til at noe skal trekkes fra den ansattes nettolønn (for eksempel et utlegg som ble utbetalt dobbelt), krever **arbeidsmiljøloven § 14-15** en lovhjemmel eller en *forhåndsavtale om akkurat dette trekket*. En generell klausul i arbeidsavtalen er ikke nok (HR-2021-2532-A) [P/S] ([Høyesterett](https://www.domstol.no/globalassets/upload/hret/avgjorelser/2021/desember-2021/hr-2021-2532-a.pdf), [Virke](https://www.virke.no/arbeidsgiverstotte/lonn/trekk-lonn/), [KS](https://www.ks.no/ks-advokatene/nyheter/arbeidsgiver-adgang-til-trekk-i-lonn-for-a-korrigere-feilutbetalinger/)). Lønn må stoppe slike negative korrigeringer med `REQUIRES_WRITTEN_AGREEMENT` og tilby en flyt for avtale eller tilbakebetaling. Det er en konkret funksjon som skiller produktet fra andre.

---

### B1. Utleggsappen → lønn (godkjente utlegg og reiseregninger)

**Hvem eier sannheten [V]:**
- **Utleggsappen** eier selve kravet: kvitteringer, reisefakta (sted, dato, overnatting, måltider, km), godkjenning, kostnadsdimensjoner og sitt eget *forslag* til klassifisering og beløp.
- **Lønn** eier den endelige *skatte- og rapporteringsklassifiseringen* (a-meldingsbeskrivelse, trekkplikt, AGA), utbetalingen og a-meldingen. Det er lønn (arbeidsgiver) som står ansvarlig overfor Skatteetaten.
- **Mønsteret «fakta + forslag»:** Utleggsappen sender fakta og sitt beregnede forslag. Lønn kjører en egen regelmotor (dobbel kontroll). Ved avvik over terskel avvises linjen med `INVALID_CLASSIFICATION`, og Utleggsappen får en forklaring.

**To utbetalingsveier (viktig designvalg) [V]:**
- **A. Via lønn:** Alle linjer utbetales i ordinær eller ekstra lønnskjøring.
- **B. Direkte utbetaling:** Rene refusjoner og trekkfrie godtgjørelser utbetales raskt via bank, for eksempel samme dag eller ukentlig. Linjer som skal *rapporteres* sendes likevel til lønn som `alreadyPaid=true` og kommer med i a-meldingen for utbetalingsmåneden. Trekkpliktige deler går **alltid** via lønn, fordi skattetrekk og AGA må beregnes der.

Dette er en reell forbedring for brukeren: Den ansatte får igjen kvitteringspengene med en gang, og reglene følges likevel.

**Linjetyper og hvordan de behandles:**

| Linjetype | Trekkpliktig | AGA | A-melding | Merknad og kilde |
|---|---|---|---|---|
| Refusjon av dokumenterte utlegg (arbeidsgivers kostnad) | Nei | Nei | Normalt ikke opplysningspliktig [U, verifiser per type] | Bilaget må følge med for regnskapet. |
| Trekkfri kostgodtgjørelse, reise med overnatting på hotell | Nei | Nei | **Ja**, som «utgiftsgodtgjørelse» med beskrivelsen «reise kost med overnatting på hotell» [P] | [Skatteetaten](https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/lonn-og-ytelser/oversikt-over-lonn-og-andre-ytelser/trekkfri-godtgjorelse-til-kost-pa-reise-med-overnatting). Egne beskrivelser for hybel, pensjonat og brakke, og for opphold utover 28 døgn [P]. |
| Kostgodtgjørelse over trekkfri sats | Ja | Ja | Ja (trekkpliktig kostgodtgjørelse) | Overskuddet skal rapporteres som trekkpliktig [P]. |
| Kilometergodtgjørelse | Del | Del | Ja | 2026: statens sats 5,30 kr/km, trekkfri sats 3,50 kr/km. Differansen (1,80 kr/km) er **trekkpliktig bilgodtgjørelse** og skal splittes [S – verifiser mot Skatteetatens satsside] ([Skatteetaten trekkpliktig bilgodtgjørelse](https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/lonn-og-ytelser/oversikt-over-lonn-og-andre-ytelser/trekkpliktig-bilgodtgjorelse), [Revisorforeningen satser 2026](https://www.revisorforeningen.no/fag/nyheter/satser-for-inntektsaret-2026/)). |
| Fordeler (privat kostnad dekket av arbeidsgiver) | Ja (kontantytelse) / avhenger (naturalytelse) | Ja | Ja | Utleggsappen må kunne merke en linje som «privat/fordel». Ellers blir det feilrapportering. |
| Utenlandsdiett | Avhenger av sats og land | – | Ja | Satser per land. Kontrakten må ha med land og ISO-landkode. |

*Satsene for 2026 bør hentes fra [Skatteetatens satsside for kost og losji](https://www.skatteetaten.no/satser/kost-og-losji-satser-for-trekk-og-skattefri-godtgjorelse/?year=2026) og [forskuddssatser 2026](https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/forskuddssatser-2026/). Jeg har ikke verifisert hver sats.*

**Hendelser:**

| Retning | Hendelse | Innhold |
|---|---|---|
| UA → kjerne | `no.plattform.expense.claim.approved.v1` | Hele kravet, linjer og dimensjoner (se payload) |
| UA → kjerne | `…expense.claim.corrected.v1` | Ny versjon, med `supersedes` |
| UA → kjerne | `…expense.claim.withdrawn.v1` | Trekk tilbake før låsing |
| Lønn → UA | `no.plattform.payroll.input.accepted.v1` / `.rejected.v1` | Per linje: status og årsakskode |
| Lønn → UA | `…payroll.input.deferred.v1` | Flyttet til neste periode (cut-off) |
| Lønn → UA | `…payroll.payrun.paid.v1` (filtrert til UAs linjer) | Linjereferanser, utbetalingsdato, lønnskjøring, lønnsslipp-ID |
| Lønn → UA | `…payroll.input.reported.v1` | A-melding sendt og godkjent for måneden (UA kan vise «innrapportert») |
| Bank → UA (direkte) | `…payment.item.settled.v1` / `.returned.v1` | For vei B |

**Payload (utdrag) [V]:**

```json
{
  "claimId": "UA-2026-004512",
  "claimVersion": 2,
  "supersedes": 1,
  "employee": { "personId": "per_8fK2", "employmentId": "arb_31Qa" },
  "approval": { "approvedBy": "per_19Xz", "approvedAt": "2026-10-27T12:44:00Z", "policyId": "reise-standard" },
  "payout": { "route": "PAYROLL", "requestedPayDate": "2026-11-20" },
  "currency": "NOK",
  "lines": [
    { "lineId": "L1", "kind": "EXPENSE_REFUND", "amount": "1249.00",
      "receipt": { "url": "https://…/kvittering/abc", "sha256": "…" },
      "dimensions": { "avdeling": "200", "prosjekt": "P-4411" } },
    { "lineId": "L2", "kind": "PER_DIEM_HOTEL", "quantity": 2, "unit": "døgn",
      "facts": { "from": "2026-10-20", "to": "2026-10-22", "country": "NO", "mealsProvided": ["frokost"] },
      "proposed": { "amount": "…", "classification": "<a-meldingsbeskrivelse fra kodeliste>", "taxable": false } },
    { "lineId": "L3", "kind": "MILEAGE_CAR", "quantity": 412, "unit": "km",
      "facts": { "route": "Stavanger–Bergen t/r", "passengers": 0 },
      "proposed": { "splits": [
        { "part": "TAX_FREE", "rate": "3.50", "amount": "1442.00" },
        { "part": "TAXABLE",  "rate": "1.80", "amount": "741.60" } ] } }
  ]
}
```

**Feilhåndtering [V]:**
- Ukjent eller avsluttet arbeidsforhold → `REJECTED` (`EMPLOYMENT_NOT_FOUND`/`EMPLOYMENT_ENDED`). Lønn foreslår et sluttoppgjør hvis det er relevant.
- Utbetalt beløp som senere viser seg feil → korrigering. Negativ netto trekkes **ikke** automatisk (aml. § 14-15). Flyt: be om en forhåndsavtale (e-signert) eller tilbakebetaling via betalingslenke.
- Dimensjon som ikke finnes i regnskapet → linjen godtas, og bilaget får standarddimensjon og et varsel (`MISSING_DIMENSION`). Det stopper ikke lønna.
- Utleggsappen er nede → lønn kjører uten. Linjer som kommer for sent, går til neste periode. Ingen synkrone avhengigheter i lønnskjøringen.

**Idempotens:** `(UA, claimId:lineId, claimVersion)`. Kvitteringens hash er med, så en duplisert kvittering kan oppdages på tvers av krav. Det er også en mulig KI-funksjon.

---

### B2. Organisasjons-/HR-modul (OrgLab-type) → lønn

**Eier:** Org.struktur, stillinger, lederrelasjoner, kostnadssteder og (valgfritt) arbeidsforholdets HR-attributter (start/slutt, stillingsprosent, yrkeskode). Lønn eier lønnsattributter, skattekort, bankkonto og alt som gjelder a-meldingen.

| Retning | Hendelse | Nøkkelfelt |
|---|---|---|
| Org → lønn | `org.unit.created/updated/closed.v1` | orgUnitId, forelder, kostnadssted, gyldig fra |
| Org → lønn | `org.manager.assigned.v1` | employmentId, managerEmploymentId, type (linje/godkjenner), gyldig fra |
| Org → lønn | `hr.employment.planned.v1` (før start) | person, start, stilling, %, yrkeskode, underenhet. Lønn oppretter et utkast til arbeidsforhold og ber om skattekort. |
| Org → lønn | `hr.employment.changed.v1` | Endrede attributter med gyldighetsdato (bitemporalt) |
| Org → lønn | `hr.employment.terminated.v1` | Sluttdato og årsak (fra kodeliste). Lønn starter sluttoppgjør (feriepenger, avspasering). |
| Org → lønn | `org.position.changed.v1` | Stillingskategori og lønnsband (for lønnstransparens) |
| Lønn → org | `payroll.employment.validation_failed.v1` | Feltet som bryter a-meldingens forretningsregler (for eksempel yrkeskode mangler) |
| Lønn → org | `payroll.compensation.changed.v1` (aggregert eller pakkestyrt) | Til lønnsoppgjør og budsjett |

**Feil og idempotens [V]:** Endringer med tilbakevirkende kraft (gyldig fra tidligere enn låst periode) fører til `payroll.retro_adjustment.proposed`. Lønnsansvarlig godkjenner etterberegningen. Idempotensnøkkel: `(org, objektId, gyldigFra, revisjon)`. Kjernen speiler lederrelasjonen, slik at Utleggsappen og Tikket kan bruke samme godkjenningskjede uten å spørre OrgLab synkront.

---

### B3. Tid/registrering (Tikket-type) → lønn

**Eier:** Registrerte og godkjente timer, klassifisert etter arbeidstidsordning (normaltid, overtid 50/100, kvelds-, natt- og helgetillegg, beredskap), fraværsregistreringer (egenmelding, sykmelding, ferie, permisjon) og avspaseringssaldo. **Lønn eier prisingen** (sats per lønnsart og arbeidsforhold), feriepenger, sykelønn og refusjonskrav mot NAV, og a-meldingens permisjonsrapportering.

| Retning | Hendelse | Nøkkelfelt |
|---|---|---|
| Tid → lønn | `time.period.approved.v1` | employmentId, periode, linjer {timetype, antall, dato, dimensjoner}, godkjenner |
| Tid → lønn | `time.period.reopened.v1` | Bare før låsing. Etter låsing kommer korrigeringslinjer. |
| Tid → lønn | `absence.registered/approved/cancelled.v1` | type, fra/til, grad (%), referanse (for eksempel sykmeldings-ID). *Helseopplysninger bare med pakken «Fravær – helse».* |
| Tid → lønn | `leave.started/ended.v1` | Permisjon eller permittering med prosent og ID (trengs i a-meldingen) |
| Lønn → tid | `payroll.period.cutoff_scheduled/locked.v1` | Fristen styrer «lås timeliste» i tidsmodulen |
| Lønn → tid | `payroll.input.accepted/rejected.v1` | Per linje |
| Lønn → tid | `payroll.balance.updated.v1` | Ferie- og avspaseringssaldo hvis lønn eier saldoen (avklares per tenant) |

**Feil og idempotens [V]:** `(tid, employmentId:periode:linjeId, revisjon)`. Timer for avsluttet arbeidsforhold går til sluttoppgjør. Overtid uten godkjenning blir `REJECTED`. Lønn betaler aldri ut ugodkjent tid.

---

### B4. Lønn → regnskap (Tripletex, PowerOffice Go, Fiken, Visma …)

**Eier:** Regnskapet eier kontoplan, dimensjonskoder, bilagsnummerserie og periodelås. Lønn eier bilagsinnholdet (posteringer fra lønnskjøringen).

| Retning | Hendelse/kall | Innhold |
|---|---|---|
| Regnskap → lønn | Synk av kontoplan og dimensjoner (henting, eventuelt webhook) | Kontoer, avdelinger, prosjekter |
| Lønn → regnskap | `payroll.posting.ready.v1` og push via adapter | Bilag per lønnskjøring: brutto per lønnsart → konto, skattetrekk, AGA, feriepengeavsetning (og AGA av den), pensjon, nettolønn mot bank, dimensjoner per linje, vedlegg (lønnsjournal-PDF) |
| Regnskap → lønn | `accounting.voucher.booked.v1` / `.failed.v1` | Bilagsnummer, eller feil (for eksempel «periode låst») |
| Lønn → regnskap | Termin- og månedsbilag | Betaling av skattetrekk og AGA, avstemming mot A07 |

**Idempotens:** Ekstern referanse `payrun:<id>:rev<n>` på bilaget. Ved ny revisjon reverseres forrige bilag og et nytt sendes. **Feil:** Periode låst i regnskapet → foreslå bokføring i neste åpne periode med merknad. Feil konto → mappingdialog. Lønn er ferdig selv om bokføringen henger. Status vises på lønnskjøringen. **Adaptere:** Én per regnskapssystem, bak en intern bilagskontrakt (antikorrupsjonslag). Tripletex og PowerOffice først, fordi byråene bruker dem mest [V].

---

### B5. Lønn → bank

**Eier:** Banken eier betalingsstatus. Lønn eier betalingsoppdraget.

| Retning | Format/hendelse | Innhold |
|---|---|---|
| Lønn → bank | ISO 20022 **pain.001** (via bankens bedrifts-API eller filkanal) | Nettolønn per ansatt, utbetalingsdato, entydig referanse per transaksjon (EndToEndId = payslipId), eventuelt hasteflagg |
| Bank → lønn | **pain.002** (status), **camt.054** (debet-/kreditbekreftelser) | Godtatt, avvist, returnert (feil kontonummer) |
| Lønn → kjerne | `payment.batch.submitted/accepted/rejected.v1`, `payment.item.returned.v1` | Til ansattportal («lønn er på vei») og Utleggsappen (vei B) |
| Lønn → bank | Overføring til **skattetrekkskonto** | Trekkmidler skal settes på særskilt skattetrekkskonto eller sikres med bankgaranti (skattebetalingsloven § 5-12) [U – verifiser ordlyd] |

**Feil [V]:** Returnert betaling → ny betaling når kontonummeret er rettet, med BankID-bekreftet endring. To nøkler (fire øyne) ved betalingsgodkjenning skjer i banken eller i lønn. Straksbetaling (NICS Real/Straks) er teknisk mulig [S] ([Atlar](https://www.atlar.com/guides/bank-payments-in-norway)), men om bedrifts-API-ene støtter straks i bulk varierer fra bank til bank [U].

---

### B6. Lønn ↔ pensjon

**Situasjonen [P/S]:** Siden 1.1.2021 har Skatteetaten og Nav hjemmel til å dele inntekts- og arbeidsforholdsopplysninger med pensjonsinnretninger. Private OTP-leverandører kan derfor hente mye fra a-ordningen ([Skatteetaten veiledning pensjonsinnretning](https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/pensjonsinnretning-obligatorisk-tjenestepensjon), [Finans Norge høring](https://finansnorge.no/contentassets/bc1467c5df834729bd980f741b72b763/finans-norge--horing-oftp---a---ordningen-m.m.-20.08.2024.pdf)). A-meldingen har med pensjonsinnretning og ordning. For offentlig og kommunal tjenestepensjon (KLP, SPK), som er relevant for mange stiftelser og organisasjoner, var tilgangen smalere ifølge høringen fra 2024 [S/U].

| Retning | Hendelse | Innhold |
|---|---|---|
| Pensjon → lønn | `pension.scheme.updated.v1` | Avtalenummer, innskuddssatser (for eksempel 2/5/7 %), arbeidstakerandel (trekk), grenser |
| Pensjon → lønn | `pension.membership.changed.v1` | Inn- og utmelding, unntak |
| Lønn → pensjon | `payroll.pension_basis.reported.v1` (der leverandøren ikke henter fra a-ordningen, og for KLP/SPK-type) | Pensjonsgrunnlag per arbeidsforhold og måned, stillingsprosent, start/slutt |
| Lønn → pensjon | `payroll.employee_contribution.withheld.v1` | Arbeidstakers egenandel trukket (lovhjemlet eller avtalt trekk) |

**Idempotens:** `(arbeidsforhold, måned, revisjon)`. Retting av en måned erstatter hele måneden.

---

### B7. Lønn → ansattportal (og Digipost)

| Retning | Hendelse | Innhold |
|---|---|---|
| Lønn → portal | `payroll.payslip.published.v1` | payslipId, personId, periode. Selve innholdet hentes via API (pakken «Lønnsresultat – individ»). |
| Lønn → portal | `payroll.payment.scheduled/sent.v1` | Varsel om at lønna er på vei |
| Lønn → portal | `payroll.annual_statement.published.v1` | Sammenstillingsoppgave/årsoversikt |
| Portal → lønn | `employee.bank_account.change_requested.v1` | Krever BankID-steg, gjelder fra neste lønnskjøring, varsler lønnsansvarlig |
| Portal → lønn | `employee.contact.changed.v1` | Adresse og kontaktinfo (går til Personkatalogen) |
| Lønn → Digipost | Sending via Digipost-API | Lønnsslipp til digital postkasse. Digipost har lønnspartnere (Aditro, Sariba/SAP) [S] ([Digipost partnere](https://www.digipost.no/en/business/partners), [Digipost API](https://digipost-docs.readthedocs.io/en/latest/api/introduction.html)) |

---

### B8. Myndighetskontrakter (ikke moduler, men en del av plattformen)

| Mot | Hva | Status 2026 |
|---|---|---|
| Skatteetaten – a-melding | Nytt API, a-melding v2.3, regelrunde R1 2026, tilbakemelding (A03), avstemming (A06/A07). API er eneste vei fra system fra 2026 [P] | [Skatteetaten SBS](https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/a-meldingen-sbs/). Skatteetaten holdt informasjonsmøte om a-ordningen 22.10.2026 [P]. |
| Skatteetaten – skattekort | Nytt API med Maskinporten, systembruker og tilgangspakker. Fra 15.12.2026 opprettes ingen dialoger i Dialogporten ved API-kall. Kjent feil 23.6.2026 ved bestilling av endringer for flere arbeidsgivere samtidig [P] | [Skatteetaten skattekort SBS](https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/skattekort-sbs/), [endret bruksmønster](https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/endret-bruksmonster-for-henting-av-skattekort/) |
| Nav | Inntektsmelding (sykepenger, foreldrepenger) fra lønnssystem. Flere Nav-tjenester ligger i pakken «Regnskapsfører lønn» [S] | Nav-detaljer og API-status ikke verifisert i denne runden [U]. Se [nav.no/arbeidsgiver/tilganger](https://www.nav.no/arbeidsgiver/tilganger). |
| Brønnøysund | Enhetsregisteret (underenheter, kommune → AGA-sone) | Åpent API (kjent). |

---

## 1.12 (c) Ekte plattform eller bare integrasjoner?

| Kjennetegn | «Bare integrasjoner» | Ekte plattform [V] |
|---|---|---|
| Kontrakter | Punkt-til-punkt, skreddersydd per par | Publisert felles modell (Person, Arbeidsforhold, Lønnsgrunnlag), versjonert og med skjemaregister |
| Egne moduler | Har bakdører og interne kall | **Bruker de samme offentlige API-ene og hendelsene som tredjeparter** |
| Identitet | Egen innlogging per app | Én identitet og én ansattprofil på tvers |
| Samtykke | Kunden limer inn API-nøkler | Installasjon med tilgangspakker, tilbaketrekking og revisjon |
| Utvidbarhet | Leverandøren må kode alt | Webhooks, endringsstrøm, utvidelsespunkter i UI, egendefinerte felt, valideringshooks før lønnskjøring |
| Selvbetjening | Kontakt salg for API | Utviklerportal, sandkasse med testdata, OpenAPI og AsyncAPI, SDK-er, statusside |
| Stabilitet | Endringer brekker kunder | Policy for utfasing (≥12 mnd), kontraktstester, endringslogg |
| Økonomi | Ingen | Felles fakturering, partnernivåer, sertifisering, felles salg |

**Slik unngår dere tett kobling [V]:**
1. **Data eies per modul.** Ingen delt database. Referer med ID og gyldighetsdato, og lagre et *øyeblikksbilde* av det som ble brukt i beregningen (lønnsslippen må kunne reproduseres selv om OrgLab endrer historikk).
2. **Hendelser er fakta, kommandoer går via API.** Ikke «LønnSkalKjøres»-hendelser fra andre moduler.
3. **Antikorrupsjonslag.** Utleggsappens språk oversettes til lønnsgrunnlag i en adapter *utenfor* lønnskjernen. Kjernen kjenner bare `PayInput` med `source`. Da kan en konkurrerende utleggsapp kobles på like enkelt. Det gjør plattformen mer attraktiv for byråer.
4. **Ingen synkrone kjeder i lønnskjøringen.** Ved cut-off fryses et øyeblikksbilde av alle innkomne grunnlag. Beregningen trenger ingen andre moduler for å være oppe.
5. **Kontraktstester drevet av konsumentene** (for eksempel Pact) i CI for hver modul. Skjemaregisteret avviser endringer som ikke er bakoverkompatible.
6. **Uavhengige releaser og feature flags per modul.** Lønn fungerer når en modul er deaktivert.
7. **Unngå et «Utleggsappen-felt»** i lønnsdatamodellen. Hvis noe er nødvendig, skal det gjøres generisk (for eksempel `attachments[]`, `externalUrl`).
8. **Eierskapsregisteret** (1.5) håndheves i API-laget, ikke bare i dokumentasjonen.

## 1.13 (d) Forretningsmodell

| Modell | Fordel | Ulempe | Passer for dere nå? [V] |
|---|---|---|---|
| **Kjerne + modulpakker** («Lønn», «Lønn + Utlegg», «Lønn + Tid», «Komplett») | Enkel å forstå, mersalg | Pakkene må gi mening også uten egne moduler | **Ja, hovedmodell** |
| **Pris per aktiv ansatt og måned** (+ grunnpris per selskap) | Skalerer med kunden og er bransjestandard | Kunder med sesongarbeidere vil ha «betal bare når lønnsslipp» | **Ja**, definer «aktiv» som «fikk lønnsslipp» |
| **Byrålisens** (volumtrinn per klient eller lønnsslipp, grossistpris, byrået fakturerer selv) | Byråer gir distribusjon. De foretrekker forutsigbare lisensmodeller fremfor stykkpris [S] ([KI-undersøkelse 2025/26](https://storage.mfn.se/fec97e8d-0f9d-4629-a7f6-0b72622d9ff3/ki-bruk-i-norsk-administrasjon-og-ledelse.pdf)) | Prispress | **Ja, kritisk kanal** |
| **Partnerprogram** (gratis API, sertifisering, oppføring i katalog) | Bygger økosystem billig | Krever dokumentasjon og support | **Ja**, lett versjon |
| **Markedsplass med fakturering og inntektsdeling** | Inntekt fra tredjepart | Dyr å drive (fakturering, support, kvalitetskontroll). Gir lite før det er volum | **Nei, ikke ennå.** Først ved ca. 30–50 integrasjoner [V] |
| **Videresalg av partnermoduler** (dere fakturerer, partner leverer) | Én faktura for kunden | Inntektsdeling må forhandles. 15–30 % er vanlig i SaaS-markedsplasser [U – ikke verifisert for HR/lønn i Norge] | Selektivt (for eksempel pensjon eller forsikring) |
| **Lønn som infrastruktur** (innebygd lønn i norske bransjesystemer: bygg, renhold, frisør, helse) | Ny kanal à la Gusto Embedded [P] | Krever modne UI-komponenter og API. Lite marked i Norge | **Senere** (år 2–3) |
| **Oppføring hos unified-API-leverandører** (Kombo, Apideck, Merge, Finch) | Gratis rekkevidde mot hundrevis av HR-, forsikrings- og pensjonsapper | Lite kontroll over hvordan dataene brukes | **Ja, lavthengende frukt** |

**Søsterproduktet Utleggsappen [V]:** Lag en felles pakke («Lønn + Utlegg») med felles pålogging og felles faktura, men hold kontrakten åpen og symmetrisk. Det verste som kan skje, er at lønn bare er «Utleggsappens lønn» eller at Utleggsappen bare fungerer med deres lønn. Begge mister da markedet hos kunder med andre systemer.

---

# DEL 2 – Lønn i 2026: hva er forventet, hva er kult, hva er hype?

## 2.0 Oversikt

| Tema | Status oktober 2026 | Klassifisering | Kort begrunnelse |
|---|---|---|---|
| **Altinn 3, systembruker, a-melding-API og skattekort-API** | Krav nå. Roller faller bort 31.12.2026 [P] | **Må ha 2026** | Uten dette ingen lovlig innsending fra 2027 |
| Klientdelegering og massehåndtering for byrå | Ny modell i Altinn 3 [P] | **Må ha 2026** | Byråkanalen står og faller på det |
| ARP og lønnskartlegging (ldl. § 26) | Gjeldende rett [P] | **Må ha 2026** | Lovkrav for >50 ansatte og offentlig sektor |
| EUs lønnstransparensdirektiv | Ikke i EØS ennå [P]. Sverige utsetter til 2027 [S] | **Differensierende** (blir trolig krav 2027–2028) [V/U] | Klar datamodell nå gir et forsprang |
| Sanntidslønn/kontinuerlig lønn | Mest leverandørprat [S] | **Hype/vent** (men *live forhåndsberegning* er differensierende) | Norsk lønn er månedlig og forankret i a-meldingen |
| Lønn på forskudd (EWA) | Uavklart regulatorisk, ingen norske aktører funnet [U] | **Hype/vent** | Risiko for omdømme og kredittregulering |
| Straks-utbetaling (bank) | Infrastruktur finnes [S] | **Differensierende** for utlegg og sluttoppgjør | Lite behov for vanlig lønn |
| Vipps-utbetaling | Fant ingen offentlig utbetalings-API [P] | **Vent** | Ingen API å bygge mot |
| Lønn i flere valutaer | Nisje | **Vent** (nisje-differensierende) | Lite relevant for målgruppen |
| KI: avviksdeteksjon og -forklaring | Lanseres hos Deel, SD Worx, Gusto, Rippling [S/P] | **Må ha 2026** | Markedet forventer det |
| KI: «spør lønnsslippen» og ansatt-Q&A | Personio-assistent til alle ansatte (okt. 2025) [P] | **Differensierende** og raskt på vei mot krav | Avlaster lønnsansvarlig |
| KI: tariff-tolkning | Tidlig | **Differensierende**, høy risiko | Feil tolkning gir feil lønn |
| KI: autonom lønnskjøring | Gusto Cofounder i «early access», SD Worx med menneske i løkka [S/P] | **Hype/vent** | Ansvar og tillit mangler |
| MCP- eller agent-API | Gusto (ChatGPT/Claude), Deel (ChatGPT), HiBob (MCP ifølge tredjepart) [S] | **Differensierende** og billig | Synlighet, og passer med plattformstrategien |
| API-first og innebygd lønn | Etablert i USA [P] | **Må ha** internt / **differensierende** eksternt | Grunnlaget for modulplattformen |
| Mobil-først og digital lønnsslipp | Standard | **Må ha** | Hygienefaktor |
| Forklart lønnsslipp, feriepenge- og skatteprognose | Sjelden godt løst | **Differensierende** | Norsk særpreg (feriepenger, halv skatt) |
| Totalkompensasjon | Etablert i HR-suiter | **Differensierende** | Krever pensjons- og fordelsdata |
| Økonomisk velvære | Vagt | **Hype/vent** | Lite etterspurt i norsk SMB |
| CSRD/ESRS S1 fra lønnsdata | Omnibus: >1000 ansatte og >450 mill. euro [S] | **Vent** (VSME-eksport = lett differensiering) | Målgruppen er stort sett utenfor |
| Sykefraværsanalyse | Etterspurt (IA, kostnad) | **Differensierende** | Konkret verdi, krever ryddig personvern |
| BankID, passkeys og MFA | Standard | **Må ha** | Lønn er et mål for svindel |
| Norsk drift og datasuverenitet | Politisk tema, ikke lovkrav [P/S] | **Differensierende** for offentlig nære, stiftelser og byråer | Salgsargument, men ikke avgjørende alene |
| Byråautomatisering | KI og digitalisering er toppsaker i bransjen [S] | **Må ha** (cockpit) / **differensierende** (KI) | Kanalstrategi |

---

## 2.1 Myndighetsintegrasjonen 2026: det egentlige «må ha»

- **A-melding:** Fra 2026 er API-integrasjon mot Skatteetatens API den eneste måten å sende a-meldinger fra system [P]. Gjeldende format er v2.3, siste regelrunde R1 2026 [P] ([Skatteetaten SBS](https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/a-meldingen-sbs/)).
- **Tilgang:** Systembruker og tilgangspakker. For a-meldingen gjelder A-ordningen, Regnskapsfører lønn, Regnskapsfører med/uten signeringsrett, Ansvarlig revisor og Revisormedarbeider [P]. Tidslinje: 31.5.2026 (tilgangspakker kreves for reetablerte tjenester), 19.6.2026 (siste frist for å delegere roller), 31.12.2026 (eksisterende roller utløper), januar 2027 (bare tilgangspakker) [P] ([Skatteetaten](https://www.skatteetaten.no/nn/samarbeidspartnere/reetablering-altinn/regnskapsforer-revisor/)).
- **Skattekort:** Nytt API med Maskinporten og systembruker. RF-1211-skjemaet erstattes [P].
- **Vurdering [V]:** Mange etablerte systemer har brukt 2026 på å migrere. **Et nytt system kan gjøre onboarding til en styrke:** en veiviser som (1) oppretter systembruker-forespørsel, (2) viser kunden nøyaktig hva som skal godkjennes i Altinn, (3) poller status og (4) varsler før tilgangen utløper. For byråer: klientliste med «tilgang OK / mangler pakke / utløper».

## 2.2 Lønnstransparens, lønnskartlegging og ARP

**Direktivet (EU) 2023/970 – hovedinnhold** (fra direktivteksten, [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2023/970/oj)):
- Lønnsnivå eller lønnsintervall skal oppgis før ansettelse. Det blir forbudt å spørre om tidligere lønn (art. 5).
- Kriteriene for lønnsfastsettelse og lønnsutvikling skal være tilgjengelige. Medlemsland kan unnta virksomheter under 50 ansatte fra kravet om utviklingskriterier (art. 6).
- Ansatte får rett til informasjon om eget lønnsnivå og gjennomsnitt fordelt på kjønn for samme arbeid eller arbeid av lik verdi, med svar innen 2 måneder. Hemmelighold av lønn blir forbudt (art. 7).
- Rapportering om lønnsgap (gjennomsnitt, median, variable komponenter, kvartiler, per kategori): 250+ ansatte årlig fra 7.6.2027, 150–249 hvert 3. år fra 2027, 100–149 hvert 3. år fra 7.6.2031 (art. 9).
- **Felles lønnsvurdering** når gapet er ≥ 5 % i en kategori, ikke er objektivt begrunnet og ikke er rettet innen 6 måneder (art. 10).

**Status for Norge [P]:**
- «Per 20.11.2025 er likelønnsdirektivet ikke innlemmet i EØS-avtalen». Regjeringen anser det som EØS-relevant, og EU-fristen 7.6.2026 gjelder ikke Norge. Kultur- og likestillingsdepartementet arbeider med gjennomføringen sammen med partene. Siden ble sist endret 10.4.2026 ([regjeringen.no](https://www.regjeringen.no/no/tema/likestilling-og-mangfold/likestilling-og-inkludering/om-likelonnsdirektivet/id3140297/)).
- EFTA: «under scrutiny for incorporation». Ingen EØS-komitébeslutning er oppført ([EFTA eea-lex](https://www.efta.int/eea-lex/32023l0970)).
- I EU: Fristen 7.6.2026 gikk ut, og «de færreste land» har oppfylt kravene. Bare rundt ti land har startet lovarbeid. Sverige har utsatt sitt forslag til 2027 ([Altinget, 23.6.2026](https://www.altinget.no/artikkel/eu-landene-bommer-paa-fristen)) [S]. NHO venter at direktivet kommer, men senere enn i EU ([NHO](https://www.nho.no/tema/eos-og-internasjonal-handel/samleside-eu-regelverk/eus-pay-transparancy-directive/)) [S].

**Gjeldende norsk rett [P]:** ldl. § 26: Offentlige virksomheter og private med mer enn 50 ansatte skal kartlegge lønn fordelt på kjønn **annethvert år** og kartlegge ufrivillig deltid. Private med 20–50 ansatte må gjøre det hvis en av partene krever det ([regjeringen.no](https://www.regjeringen.no/no/tema/likestilling-og-mangfold/likestilling-og-inkludering/om-likelonnsdirektivet/id3140297/), [NHO ARP](https://www.nho.no/contentassets/64d740fc67114bf0b7a95b0d4ae70cfe/arp_2025_030325.pdf)).

**Klassifisering:**
- **Må ha 2026:** ARP-rapport (lønnskartlegging etter kjønn per stillingskategori, deltid, uttak av foreldrepermisjon) fra lønnsdata.
- **Differensierende:** En datamodell klar for direktivet (stillingskategori og «arbeid av lik verdi», lønnsband, skille mellom fast og variabel lønn), en 5 %-alarm, og en ferdig flyt for informasjonskrav fra ansatte. Ekstra viktig for kunder med datterselskaper i EU.
- **Vurdering [V/U]:** Innlemmelse i EØS og norsk lov tar normalt 1–2 år etter at EØS-komiteen har behandlet saken. Et realistisk anslag for norske plikter er tidligst 2027–2028. Det er usikkert. Bygg modellen nå, men ikke selg det som et lovkrav.

## 2.3 Sanntidslønn, lønn på forskudd, straksbetaling, Vipps og valuta

**Kontinuerlig lønn/sanntidslønn – Hype/vent.** Det meste er leverandørmarkedsføring. Det sterkeste argumentet kommer fra land med kontinuerlig myndighetsrapportering (Australia, LATAM-land) [S] ([Multiplier](https://www.usemultiplier.com/global-payroll/future-of-global-payroll), [Ramco](https://www.ramco.com/blog/payroll/global-payroll-trends-2026-ai-cloud-real-time-payroll), [Lano](https://www.lano.io/blog/global-payroll-compliance-and-tax-news-june-2026-round-up)). I Norge er a-meldingen månedlig, og tabelltrekk er laget for månedslønn. **Det som faktisk gir verdi [V]:** *Live forhåndsberegning*, der neste lønn beregnes fortløpende etter hvert som timer, fravær og utlegg kommer inn. Da blir lønnsdagen en formalitet, og avvik oppdages tidlig. Kall det gjerne «alltid klar lønn».

**Lønn på forskudd (EWA) – Hype/vent.**
- Arbeidsgiver kan avtale lønnsforskudd. Det skal trekkes skatt ved utbetaling, og avtalen bør være skriftlig [S] ([ung.no/arbeidsrett](https://www.ung.no/oss/3l1VIsAj4GaxYni5cXE4fN)). Trekk i senere lønn krever en forhåndsavtale om det konkrete trekket (aml. § 14-15, HR-2021-2532-A) [P/S].
- Feriepenger kan ikke utbetales på forskudd [S] ([Revisorforeningen](https://www.revisorforeningen.no/revisornytt/utbetaling-av-feriepenger-pa-forskudd/)).
- **Tredjeparts EWA:** Jeg fant ingen norske aktører og ingen vurdering fra Finanstilsynet [U]. Om det er kreditt som krever konsesjon, avhenger av norsk klassifisering. I USA er dette fortsatt omstridt (CFPB-uttalelse desember 2025 og søksmål) [S] ([Crowdfund Insider](https://www.crowdfundinsider.com/2026/02/260873-us-fintech-associations-ask-circuit-court-to-decide-earned-wage-access-services-are-not-loans/)).
- **Vurdering [V]:** Lite etterspørsel i norsk SMB og risiko for omdømme («forbrukslån light»). Hvis noe, er en enkel *arbeidsgiverstyrt forskuddsflyt* (søknad, godkjenning, e-signert trekkavtale, ekstra utbetaling med skattetrekk, automatisk motregning) det som passer. Det er en nisjefunksjon.

**Straksbetaling – Differensierende for utlegg og sluttoppgjør.** NICS Real (Straks) gir avregning døgnet rundt hele året. Bits eier ordningen, og Mastercard Payment Services drifter den [S] ([Atlar](https://www.atlar.com/guides/bank-payments-in-norway)). Den beste bruken er **refusjon av utlegg i dag** (Utleggsappen, vei B), ekstra utbetalinger ved feil og sluttoppgjør. Ordinær lønn trenger det ikke. Hvor godt bankene støtter straks i bedrifts-API varierer [U].

**Vipps MobilePay-utbetaling – Vent.** Utviklerdokumentasjonen (oppdatert juli 2026) viser ingen API for utbetaling eller disbursement, bare Report API for oppgjørsdata [P] ([developer.vippsmobilepay.com/llms.txt](https://developer.vippsmobilepay.com/llms.txt)). Det er dessuten et lovkrav at lønn utbetales via bank eller annen godkjent betalingstjeneste [S] ([Globalization Partners](https://www.globalization-partners.com/fr/globalpedia/norway/payroll/), lovendring 2021).

**Lønn i flere valutaer – Vent/nisje.** Målgruppen (norske AS, stiftelser og organisasjoner) betaler i NOK. Utenlandske arbeidstakere og utsendte (PAYE/kildeskatt) er et reelt behov i noen bransjer, men det handler om skatt og trygd, ikke valuta. Utleggsappen må likevel håndtere utlegg i valuta (originalbeløp, kurs og NOK-beløp i kontrakten).

## 2.4 KI-agenter i lønn

**Hva de andre gjør:**

| Aktør | Hva | Kilde og kvalitet |
|---|---|---|
| **Deel** | «AI Workforce» i beta fra august 2025 med sju agenter, blant dem «The Payroll Detective» (avvik før utbetaling). Lansert som en pakke agenter på The Big Deel 19.3.2026. Første B2B HR- og lønnsapp i ChatGPT. «Akai» (agentplattform) i mai 2026 | [S] ([CFOtech](https://cfotech.co.uk/story/deel-launches-ai-workforce-to-streamline-global-hr-payroll), [PeopleMatters](https://me.peoplemattersglobal.com/news/hr-technology/deel-rolls-out-ai-workforce-heres-how-its-bringing-ai-agents-to-workflows-46535), [CryptoBriefing om Akai](https://cryptobriefing.com/deel-launches-akai-automation-tool-replacing-600-employees/) – svak kilde) |
| **Gusto** | «Gus» (KI-assistent, september 2024). Lønn i ChatGPT (januar 2026) og Claude/Slack (april 2026), der assistenten forbereder og brukeren godkjenner. «Cofounder»-agenten (juni 2026, early access) | [P] ([gusto.com Gus](https://gusto.com/company-news/gus-ai-assistant)), [S] ([CPA Practice Advisor](https://www.cpapracticeadvisor.com/2026/01/23/gusto-launches-payroll-inside-chatgpt/176791/), [ForgeNEX](https://www.forgenex.com/en/blog/agente-de-ia-para-rrhh-gusto-lanza-un-cofundador-que-automatiza-n-minas-sin-esperar-instrucciones)) |
| **Rippling** | «Rippling AI» (mars 2026): rapportering, analyse, svar til ansatte og tilgangsstyrte handlinger på tvers av HR, IT og økonomi. Administratoragenter omtalt fra november 2025 | [S/U] ([getperspective](https://getperspective.ai/blog/rippling-ai-strategy-hr-platform-customer-conversations-product-velocity-2026/markdown), [ZenML](https://www.zenml.io/llmops-database/building-production-ai-agents-for-enterprise-hr-it-and-finance-platform)) |
| **Personio** | KI-assistenten tilgjengelig for alle ansatte (oktober 2025). Kjøpte KI-rekrutteringsselskapet aurio i april 2026 [S] | [P] ([Personio HUG 2025](https://www.personio.com/about-personio/press/hug-2025-feature-updates/)) |
| **SD Worx** | Agentisk KI i lønn (24.6.2026), sammen med Yuma. Rulles ut gradvis i Belgia, Nederland og Finland. «7+ agenter per lønnsmedarbeider». Rundt 500 belgiske lønnskonsulenter i hybride team. Mennesket kan alltid kontrollere output og kilder | [P] ([SD Worx presse](https://www.sdworx.com/en-en/about-sd-worx/press/2026-06-24-sd-worx-introduces-agentic-ai-payroll-enhance-customer-engagement), [Q2 2026](https://www.sdworx.com/en-en/sd-worx-quarterly-updates-q2-2026/innovation-and-tech)) |
| **Visma** | Rundt 250 produktrelaterte KI-initiativer i konsernet (februar 2026). GAiA Assistant i Visma Software-dokumentasjonen. Jeg fant **ingen** konkret KI-funksjon for norsk lønnskjøring [S/U] | ([Visma/MFN](https://mfn.se/all/pr/visma/visma-delivers-strong-2025-with-record-customer-intake-and-continued-ai-led-innovation), [GAiA](https://docs.vismasoftware.no/gaia-assistant/what-is-gaia/)) |
| **HiBob** | MCP-server for eksterne KI-klienter (ifølge tredjepart) | [U] ([erpresearch](https://erpresearch.com/erp-add-ons/hcm-extensions/hibob)) |

**Klassifisering [V]:**

| Bruksområde | Klasse | Hvorfor |
|---|---|---|
| **Lønnsforberedelse og avviksdeteksjon** («hvorfor avviker 7 lønnsslipper fra forrige måned?») | **Må ha 2026** | Alle de store har det eller lanserer det. Lav risiko når det er kombinert med deterministiske regler. |
| **Avviksforklaring i klartekst** | **Må ha 2026** | Forklaringen kan genereres fra beregningsgrafen (deterministisk), med KI bare som språklag. |
| **«Spør lønnsslippen»** (ansatt) | **Differensierende**, raskt mot krav | Avlaster lønnsansvarlig. Må svare *bare* fra data og regelverk med kildehenvisning. |
| **Tariff-tolkning** | **Differensierende, høy risiko** | Tariffavtaler er tvetydige. KI bør foreslå med henvisning til paragraf, og mennesket bestemmer. |
| **Autonom kontroll** (agent kjører og godkjenner) | **Hype/vent** | Ansvaret for lønnsutbetaling og a-melding ligger hos arbeidsgiver. Tilliten er ikke på plass, og selv SD Worx har menneske i løkka. |
| **MCP- eller agent-API** | **Differensierende** | Billig å lage over det offentlige API-et. Viser at dere er moderne. Krever tilgangspakker og *ingen godkjenningsrett* for agenter. |

**Regulatorisk ramme [P/S]:** Regjeringen sender KI-loven på ny høring høsten 2026 og vil legge den fram for Stortinget våren 2027. Opprinnelig skulle den tre i kraft sensommeren 2026. EUs høyrisikoregler (der arbeidsliv er et høyrisikoområde) er utsatt til 2.12.2027 og 2.8.2028 ([regjeringen.no 4.8.2026](https://www.regjeringen.no/no/aktuelt/tung-vil-sende-ki-loven-med-endringer-pa-horing/id3169693/), [Altinget](https://www.altinget.no/artikkel/ny-forsinkelse-for-ki-loven)). **Vurdering [V]:** Ren lønnsberegning er neppe høyrisiko. KI som påvirker *lønnsbeslutninger*, som lønnsoppgjørsforslag eller vurderinger, kan bli det. Hold slike funksjoner rådgivende og godt dokumentert.

**Rekkverk (må designes inn) [V]:** Svar bare fra beregningsdata med kildesporing. Ingen fri generering av tall. Logg prompt og svar per tenant. Ingen trening på kundedata uten avtale. Personvernkonsekvensvurdering (DPIA). Tydelig merking av KI-innhold. Agenter får aldri godkjennings- eller betalingsrett.

## 2.5 Innebygd lønn, API-first og «lønn som infrastruktur»

- **Fakta [P/S]:** Gusto Embedded tilbyr API, Flows og React SDK og oppgir selv store volumer. Check og andre konkurrerer på innebygde komponenter ([Gusto Embedded](https://embedded.gusto.com/), [banq.ai](https://www.banq.ai/embedded-finance/category/payroll)).
- **Klassifisering:** **Må ha internt.** API-first er grunnlaget for modulplattformen. **Differensierende eksternt** (byråportaler, bransjesystemer). **Vent** på en fullskala «lønn som infrastruktur»-forretning i Norge, fordi markedet er lite. Bygg komponentene for egne moduler først, så kan de selges senere.

## 2.6 Ansattopplevelse

| Funksjon | Klasse | Begrunnelse [V] |
|---|---|---|
| Mobil lønnsslipp, varsel og Digipost-levering | **Må ha** | Hygiene. Digipost er norsk standard for digital post [S]. |
| Lønnsslippen forklart («hvorfor er netto lavere i juni?») | **Differensierende** | Feriepengemåned, halv skatt i desember, prosent- eller tabelltrekk. Typiske norske spørsmål som lønnsansvarlig får hver måned. |
| Feriepengeprognose | **Differensierende** | Norsk særpreg. Svært konkret nytte. |
| Skatteprognose og «sjekk skattekortet ditt» | **Differensierende** (moderat risiko) | Varsle når trekket ser for lavt ut i forhold til årsprognosen og lenke til Skatteetaten. Det skal ikke framstå som skatterådgivning. |
| Totalkompensasjon | **Differensierende** | Krever pensjons- og fordelsdata (pensjonsmodul). |
| Økonomisk velvære og sparing | **Hype/vent** | Vagt behov. Lite tillit til arbeidsgiver som økonomirådgiver. Kan senere komme som delt utbetaling til sparekonto. |
| Flerspråklig lønnsslipp | **Differensierende** | Mange utenlandske arbeidstakere i bygg, renhold og helse. |

## 2.7 Bærekraft/ESG, likestilling og sykefravær

- **CSRD etter Omnibus I [S]:** I kraft i EU mars 2026 (18. eller 19. mars, kildene spriker). Omfanget er snevret inn til **>1000 ansatte og >450 mill. euro omsetning**. Bedrifter med opptil 1000 ansatte i verdikjeden kan avslå forespørsler som går ut over den frivillige standarden (VSME) ([William Fry](https://www.williamfry.com/wp-content/uploads/2026/03/Omnibus-1-Directive-comes-into-force-in-March-2026-key-amendments-to-CSRD-and-CS3D.pdf), [AKD](https://www.akd.eu/insights/provisional-agreement-on-omnibus-i-changes-to-the-scope-and-reporting-obligations-under-the-csrd), [Accountancy Europe](https://accountancyeurope.eu/wp-content/uploads/2026/01/260129-Omnibus-explained-CSRD-factsheet.pdf)). Norge vedtok «stop-the-clock» 3.7.2025 [S] ([BDO](https://www.bdo.no/en-gb/insights/csrd-the-stop-the-clock-directive-has-now-been-adopted-in-norway)). Når og hvordan Omnibus I tas inn i Norge, er ikke verifisert [U].
- **Vurdering [V]:** Målgruppen (10–1000 ansatte) faller nesten helt utenfor CSRD. **Vent** med full ESRS S1. **Lett differensiering:** én knapp som eksporterer «sosiale nøkkeltall» etter VSME/S1-lite (antall ansatte etter kjønn og alder, turnover, sykefravær, lønnsgap, kollektiv dekning). Banker og større kunder ber om dette.
- **Likestilling og ARP:** **Må ha** (2.2).
- **Sykefraværsanalyse:** **Differensierende**. Trend per enhet, kostnad, oppfølging av refusjoner fra NAV (forventet mot mottatt). Personvern: aggregert ned til en minstestørrelse per gruppe, og helseopplysninger bare i lønns- og NAV-flyten.

## 2.8 Sikkerhet, tillit og datasuverenitet

- **BankID og passkeys – Må ha.** Lønn er et svindelmål (særlig endring av kontonummer). Passkeys for daglig innlogging, BankID for aktivering og kritiske endringer. NB: Stø har vært utsteder fra april 2026, mange BankID-brukere må identifisere seg på nytt, og Nkoms avgjørelse om nivå Høyt ventet «etter sommeren 2026» [S/U] ([bytt.no](https://www.bytt.no/artikler/forbruker/a-jpml/alternativer-til-bankid-slik-beholder-du-tilgangen-til-nav-og-helsenorge-i-2026)). BankID beskrives som på vei mot en app med passkeys og liveness [S] ([FIDO Alliance](https://fidoalliance.org/fido-webinar-the-spectrum-of-authentication-how-bankid-norway-unifies-passkeys-biometric-liveness)). Bruk derfor en eID-mellomvare som tåler endringer.
- **Datasuverenitet – Differensierende, ikke avgjørende alene.**
  - Utleggsappen valgte Advania for «suveren skydrift» med norsk drift og norsk lov [S] ([LinkedIn-innlegg, Advania](https://no.linkedin.com/in/steffentors)).
  - Regjeringen skrev 6.3.2026 til Stortinget at digital suverenitet ikke trengs som eget mål i digitaliseringsstrategien, men stiller krav om nasjonal kontroll over skytjenester [S] ([stortinget.no](https://stortinget.no/link/f72e81f7cbda4b2d90ec312ab08b1ebf.aspx)).
  - Det som avgjør eksponeringen for CLOUD Act, er eierkjeden, ikke hvor serverne står [S]. Jeg fant **ingen norsk lov** som pålegger bedrifter å bruke leverandører uten CLOUD Act-eksponering [U].
  - **Vurdering [V]:** Argumentet virker sterkest overfor offentlig nære virksomheter, stiftelser og ideelle organisasjoner, fagforbund og byråer som selger trygghet videre. Det blir troverdig når hele kjeden (drift, support, underleverandører og KI-modell) er dokumentert. Lønn i Norge og en KI-modell hos en amerikansk hyperscaler undergraver budskapet. Lag en offentlig «datakart»-side.
- **Annet som er forventet:** ISAE 3402/SOC 2 type II-rapport (byråer og revisorer spør), revisjonslogg, fire øyne ved godkjenning, tilgang med minste privilegium for supportpersonell, bevisbar sletting og eksport.

## 2.9 Regnskapsbyråenes digitalisering

- **Fakta [S]:** KI og digitalisering er de mest omtalte temaene om bransjen (Regnskap Norge, omdømmeundersøkelse april–mai 2026) ([NTB](https://kommunikasjon.ntb.no/pressemelding/19006403/regnskapsbransjen-star-stott-i-befolkningen-og-stoltheten-i-bransjen-oker?lang=no)). En undersøkelse ved årsskiftet 2025/26 med 1410 respondenter viser at KI tas i bruk av behov for effektivisering, og at byråene foretrekker lisensmodeller fremfor stykkpris ([MFN-PDF](https://storage.mfn.se/fec97e8d-0f9d-4629-a7f6-0b72622d9ff3/ki-bruk-i-norsk-administrasjon-og-ledelse.pdf)).
- **Må ha:** Byråcockpit på tvers av klienter (status, frister, avvik, tilgangsstatus i Altinn), klientdelegering, maler (lønnsarter og kontomapping) som kan rulles ut til mange klienter, masseoperasjoner, og godkjenningsflyt der klienten godkjenner lønn fra mobilen.
- **Differensierende:** KI-avviksliste per klient sortert etter risiko, automatisk avstemming lønn ↔ regnskap ↔ a-melding ↔ bank, byråfaktura basert på faktisk forbruk, og hvitmerking.
- **Hype/vent:** «Selvkjørende lønn for byrå». Byrået selger trygghet og ansvar, ikke bare klikk.

---

# DEL 3 – «Wow»-liste: 38 konkrete funksjoner for et moderne lønnssystem i 2026

Kompleksitet: **S** = uker, **M** = 1–3 måneder, **L** = over et kvartal. Modulbehov: **UA** = Utleggsappen, **OL** = OrgLab-type, **TK** = Tikket-type, **–** = ingen. Alle vurderinger er mine [V].

| # | Funksjon | Hvem får verdi | Hvorfor kult | Kompl. | Risiko | Krever modul |
|---|---|---|---|---|---|---|
| 1 | **Avviksbasert godkjenning:** Bare avvik vises. Resten er «grønt» med forklaring | Lønnsansvarlig, byrå | Lønnskjøringen går fra timer til minutter | M | Falsk trygghet hvis reglene er svake | – (bedre med TK/UA) |
| 2 | **Avvik forklart i klartekst** («Kari: −3 412 kr netto fordi …») | Lønnsansvarlig, leder | Forklaring i stedet for regneark | M | Feil forklaring hvis den ikke er grunnet i beregningsgrafen | – |
| 3 | **Glassboks-lønn:** Hvert tall kan spores til regel, sats, kildehendelse og kvittering | Lønn, revisor, ansatt | Revisjon og support blir lett. Grunnmuren for KI | L | Ytelse og datamengde | – (lenker til UA/TK) |
| 4 | **«Spør lønnsslippen»:** Ansatt-chat som svarer bare fra egne data med kilder | Ansatt, lønnsansvarlig | Færre e-poster til lønn | M | Feilsvar, personvern | – |
| 5 | **Alltid klar lønn:** Live forhåndsberegning av neste lønn | Lønn, økonomi | Ingen overraskelser på lønnsdagen | M | Kostnad ved omberegning | TK, UA |
| 6 | **Feriepengeprognose** («du får ca. X i juni, og dette trekkes») | Ansatt | Typisk norsk spørsmål besvart på forhånd | S | Lav | – |
| 7 | **Netto-forklarer for juni og desember** (feriepenger, halv skatt) | Ansatt | Fjerner det vanligste supportspørsmålet | S | Lav | – |
| 8 | **«Sjekk skattekortet»-varsel** når årsprognosen tyder på for lavt trekk | Ansatt | Unngår restskatt | M | Kan oppfattes som skatterådgivning | – |
| 9 | **Hva skjer hvis …?-simulator** (80 % stilling, permisjon, lønnsøkning) | Ansatt, HR | Gir trygghet ved store valg | M | Prognosefeil | (OL) |
| 10 | **Totalkompensasjonskort** (lønn, pensjon, forsikring, fordeler) | Ansatt, arbeidsgiver | Synliggjør verdien av ansettelsen | M | Datakvalitet | Pensjon |
| 11 | **Utlegg utbetalt i dag** (straks for refusjoner, korrekt i a-melding) | Ansatt, økonomi | Synlig «wow» for alle ansatte | M | Feil klassifisering | **UA** + bank |
| 12 | **Én godkjenningsinnboks** for timer, fravær og utlegg, styrt av lederkjeden | Leder | Én app i stedet for tre | M | Krever modne kontrakter | **OL, TK, UA** |
| 13 | **Kontonummer-skjold:** BankID-steg, to personer, karantene og varsel ved endring | Arbeidsgiver, ansatt | Stopper vanlig lønnssvindel | S | Friksjon | – |
| 14 | **Systembruker-veiviser:** Altinn-oppsett med statussjekk og utløpsvarsel | Kunde, byrå | Løser et reelt problem i 2026 | S | Endringer i Altinn | – |
| 15 | **A-melding uten drama:** Forhåndsvalidering mot forretningsreglene, tilbakemelding (A03) oversatt til klartekst og forslag til retting | Lønn, byrå | Ingen kryptiske feilkoder | M | Endringer i regelrunder | – |
| 16 | **Avstemmingsrobot:** lønn ↔ regnskap ↔ A07 ↔ bank, med avvik pekt ut | Byrå, økonomi | Termin- og årsoppgjøret går raskere | M | Ulike regnskapssystemer | Regnskap, bank |
| 17 | **Byråcockpit:** Alle klienter, frister, tilgangsstatus og risiko | Byrå | Kanalens viktigste skjerm | M | Lav | – |
| 18 | **Byråmaler:** Lønnsarter, kontomapping og regler rullet ut til N klienter | Byrå | Standardisering og skala | M | Feil sprer seg til mange klienter | – |
| 19 | **Godkjenn lønn fra mobil eller chat** (Slack/Teams) med passkey | Daglig leder, klient | Ingen innlogging for å godkjenne | S | Sikkerhet | – |
| 20 | **MCP- eller agent-API:** Lønn kan forberedes fra Claude eller ChatGPT, men ikke godkjennes | Kraftbrukere, byrå | Moderne, og gir mye synlighet | M | Misbruk av tilgang | – |
| 21 | **Tariff-assistent:** Satstabeller og tillegg foreslått med paragrafhenvisning | Lønn i tariffbundne virksomheter | Sparer manuell tolkning | L | Feiltolkning | (OL for stilling) |
| 22 | **Lønnsoppgjørsmodul:** Pottfordeling, kjønnsbalanse og budsjett i sanntid | HR, ledere | Lønnsoppgjøret flyttes ut av Excel | M | Konfidensialitet | **OL** |
| 23 | **Lønnstransparens-pakke:** Lønnsgap per kategori, 5 %-alarm og informasjonskrav (art. 7) besvart automatisk | HR, ansatt | Klar for direktivet før konkurrentene | L | Regelverket er ikke endelig i Norge | **OL** (stillingskategori) |
| 24 | **ARP på ett klikk:** Lønnskartlegging, deltid og permisjon | HR, styre | Lovkrav løst på minutter | M | Kategorisering | (OL) |
| 25 | **Sykefraværsradar og NAV-refusjonssporing** (forventet mot mottatt) | Økonomi, HR | Penger som ellers går tapt | M | Helseopplysninger | **TK** (+ bank) |
| 26 | **Sluttoppgjørsveiviser:** Feriepenger, avspasering og trekk med avtale-sjekk | Lønn | Færre feil ved fratreden | M | Jus (§ 14-15) | TK |
| 27 | **Trekkavtale på sekunder:** E-signert forhåndsavtale når en korrigering krever trekk | Lønn, ansatt | Gjør det lovlig og ryddig | S | Jus | – |
| 28 | **Kostnadsdimensjoner hele veien:** Prosjekt og avdeling fra timer og utlegg helt til bilag | Økonomi, prosjektleder | Prosjektlønnsomhet blir korrekt | M | Mapping | TK, UA |
| 29 | **Prognose for lønnskostnad 12 måneder** (inkl. AGA, feriepenger, pensjon og planlagte ansettelser) | Daglig leder, CFO | Kobler lønn til budsjett | M | Prognosefeil | **OL** |
| 30 | **«Hva koster en ansettelse?»-kalkulator** | Leder, rekruttering | Raskt beslutningsgrunnlag | S | Lav | – |
| 31 | **Sandkassekopi:** Test neste måneds lønn eller en ny tariff på en kopi | Lønn, byrå | Trygt å eksperimentere | M | Personvern i kopier | – |
| 32 | **Tidsreise:** Se ansattens data per dato (bitemporalt) | Revisor, lønn | Forklarer historikk og etterberegning | L | Kompleks modell | – |
| 33 | **Integrasjonsmonitor for kunden:** Hva kom fra hvilken modul, og hva feilet | Kunde, byrå | Tillit til plattformen | M | Lav | Alle |
| 34 | **Lønnskalender for ansatte:** Lønn, feriepenger og halv skatt på ett sted | Ansatt | Forutsigbarhet | S | Lav | – |
| 35 | **Pensjonsinnsikt:** Årets innbetaling og lenke videre | Ansatt | Synliggjør en skjult fordel | M | Data fra leverandør | Pensjon |
| 36 | **VSME/S1-lite-eksport** (sosiale nøkkeltall) | Økonomi, bank/kunder | Svarer på ESG-spørreskjemaer | S | Lav | (TK for fravær) |
| 37 | **Flerspråklig og forklart lønnsslipp** (EN, PL, LT, UK, …) | Ansatte med annet morsmål | Inkludering, færre misforståelser | S/M | Oversettelseskvalitet | – |
| 38 | **Konsern- og flerselskapslønn:** Én ansatt i flere enheter, konsernrapport | Konsern, stiftelser med AS | Vanlig behov som løses dårlig i dag | L | A-meldingskompleksitet | (OL) |

**Topp 10 å bygge først [V]:** #14, #15, #13, #1, #2, #3 (grunnmur), #17, #18, #11, #6/#7. Det gir en løsning som er korrekt og sikker i 2026, attraktiv for byråene, og som har ett tydelig «wow» sammen med Utleggsappen.

---

## 4. Anbefalt rekkefølge (12–18 måneder) [V]

1. **Kvartal 1–2: Grunnmur.** Identitet, virksomhetsregister via Brønnøysund, personkatalog, kanonisk arbeidsforhold, lønnsgrunnlags-API med låsing, a-melding- og skattekort-API med systembruker-veiviser, bilagseksport til Tripletex og PowerOffice, pain.001 til bank, Digipost.
2. **Kvartal 2–3: Plattform.** CloudEvents- og webhook-levering, endringsstrøm, tilgangspakker og installasjonsflyt, utviklerportal og sandkasse, Utleggsappen-kontrakten i produksjon (vei A, deretter B), byråcockpit.
3. **Kvartal 3–4: Differensiering.** Avviksbasert godkjenning og forklaring, glassboks-sporing, feriepenge- og nettoforklarer, ARP-rapport, kontrakter for tid og fravær, avstemmingsrobot.
4. **Kvartal 5–6: Utvidelse.** «Spør lønnsslippen», MCP-API, lønnstransparens-pakke, kontrakt for OrgLab-type, prognoser, partnerprogram og oppføring hos unified-API-leverandører.

## 5. Usikkerheter og åpne spørsmål

- **Lønnstransparens i Norge:** Ingen EØS-komitébeslutning er funnet (EFTA: «under scrutiny»). Tidslinjen for norsk lov er ukjent [U].
- **Altinn-datoer:** Kildene spriker noe (31.5, 15.6, 19.6, 31.12.2026). Hold dere til Skatteetatens og Digdirs sider, og følg SBS-nyhetene, blant annet informasjonsmøtet 22.10.2026 [U].
- **Satser 2026:** Km-sats 5,30 og trekkfri 3,50 kommer fra sekundærkilder. Diettsatsene er ikke verifisert. Hent alt fra Skatteetatens satsside [U].
- **Refusjon av utlegg og rapportering i a-meldingen:** Normalt ikke opplysningspliktig, men det finnes unntak. Avklar per linjetype med Skatteetatens veiledning eller en revisor [U].
- **Skattetrekkskonto (§ 5-12):** Ordlyden er ikke verifisert i denne runden [U].
- **EWA i Norge:** Ingen vurdering fra Finanstilsynet funnet [U].
- **Vipps-utbetaling:** Ingen API for utbetaling funnet i dokumentasjonen per juli 2026. Kan endre seg [U].
- **Konkurrentenes KI-påstander:** Mye er sekundærkilder og markedsføring. Datoene for Rippling AI og Gusto Cofounder bør sjekkes mot deres egne pressemeldinger [U].
- **Unified-API-dekning i Norge:** Kombo og Apideck oppgir ikke tydelig at de støtter norsk Visma, Tripletex eller PowerOffice-lønn [U].
- **Nettlønn:** Jeg fant ikke oppdatert eier- eller strategiinformasjon i denne runden [U].
- **OrgLab og Tikket:** Ingen fakta er innhentet. Kontraktene i B2 og B3 er generiske og må tilpasses når produktene er kjent.

## 6. Kilder (utvalg, gruppert)

**Myndigheter og regelverk**
- Skatteetaten – a-meldingen for sluttbrukersystemer: https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/a-meldingen-sbs/
- Skatteetaten – levering fra system / tilgangspakker: https://www.skatteetaten.no/nn/bedrift-og-organisasjon/arbeidsgiver/a-meldinga/levere-a-melding/levering-fra-system/
- Skatteetaten – nye tilgangspakker for a-meldingen: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/nye-tilgangspakker-for-a-meldingen/
- Skatteetaten – reetablering Altinn, regnskapsfører/revisor: https://www.skatteetaten.no/nn/samarbeidspartnere/reetablering-altinn/regnskapsforer-revisor/
- Skatteetaten – reetablering Altinn, virksomheter: https://www.skatteetaten.no/samarbeidspartnere/reetablering-altinn/virksomheter/
- Skatteetaten – skattekort SBS: https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/skattekort-sbs/
- Skatteetaten – endret bruksmønster skattekort: https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/endret-bruksmonster-for-henting-av-skattekort/
- Skatteetaten – trekkfri kost, reise med overnatting: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/lonn-og-ytelser/oversikt-over-lonn-og-andre-ytelser/trekkfri-godtgjorelse-til-kost-pa-reise-med-overnatting
- Skatteetaten – trekkpliktig bilgodtgjørelse: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/lonn-og-ytelser/oversikt-over-lonn-og-andre-ytelser/trekkpliktig-bilgodtgjorelse
- Skatteetaten – satser kost og losji 2026: https://www.skatteetaten.no/satser/kost-og-losji-satser-for-trekk-og-skattefri-godtgjorelse/?year=2026
- Skatteetaten – pensjonsinnretning (OTP) i a-meldingen: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/pensjonsinnretning-obligatorisk-tjenestepensjon
- Regjeringen – om likelønnsdirektivet: https://www.regjeringen.no/no/tema/likestilling-og-mangfold/likestilling-og-inkludering/om-likelonnsdirektivet/id3140297/
- EFTA eea-lex 32023L0970: https://www.efta.int/eea-lex/32023l0970
- EUR-Lex, direktiv (EU) 2023/970: https://eur-lex.europa.eu/eli/dir/2023/970/oj
- Regjeringen – KI-loven på ny høring (4.8.2026): https://www.regjeringen.no/no/aktuelt/tung-vil-sende-ki-loven-med-endringer-pa-horing/id3169693/
- Høyesterett HR-2021-2532-A (trekk i lønn): https://www.domstol.no/globalassets/upload/hret/avgjorelser/2021/desember-2021/hr-2021-2532-a.pdf
- Finans Norge – høring OTP/a-ordningen (2024): https://finansnorge.no/contentassets/bc1467c5df834729bd980f741b72b763/finans-norge--horing-oftp---a---ordningen-m.m.-20.08.2024.pdf
- Stortinget – brev om digital suverenitet (6.3.2026): https://stortinget.no/link/f72e81f7cbda4b2d90ec312ab08b1ebf.aspx
- Altinn docs – autentisering: https://docs.altinn.studio/en/api/authentication/

**Plattform- og API-referanser**
- Rippling platform: https://www.rippling.com/platform/analytics · Sacra: https://sacra.com/research/rippling · SaaStr: https://saastr.com/ripplings-ai-bet-the-data-graph-is-the-moat
- Gusto Embedded Flows: https://docs.gusto.com/embedded-payroll/docs/flows-intro · Flow events: https://docs.gusto.com/embedded-payroll/changelog/added-flow-events · https://embedded.gusto.com/
- Check Components: https://docs.checkhq.com/reference-link/components-overview
- Personio webhooks: https://developer.personio.de/v2.0/reference/webhooks · Partner: https://www.personio.com/partner/tech · Marketplace: https://www.marketplace.personio.com/
- HiBob integrations: https://hibob.com/integrations/ · erpresearch: https://erpresearch.com/erp-add-ons/hcm-extensions/hibob
- Deel webhooks: https://developer.deel.com/api/webhooks/introduction · Global payroll: https://developer.deel.com/api/global-payroll · Supergood: https://supergood.ai/api-report-card/deel
- Finch vs Merge: https://tryfinch.com/vs/merge · Knit om Kombo: https://www.getknit.dev/blog/a-detailed-evaluation-of-kombo-as-a-unified-hr-api-platform · Apideck Norge HRIS: https://www.apideck.com/integrations/country/norway/hris
- Visma (HelloID-README for Visma.net HRM API): https://github.com/Tools4everBV/HelloID-Conn-Prov-Source-Visma.net-HRM-API/blob/main/README.md · https://www.vismasoftware.no/api-en
- Tripletex: https://rubydoc.info/gems/tripletex_api/index · RecMan: https://help.recman.io/hc/en-us/articles/33443902243346 · 150 000 kunder: https://publish.ne.cision.com/Release/ViewReleaseHtml/82E61C8B666E36B0
- PowerOffice Go salary lines: https://developer.poweroffice.net/workflows/endpoints/payroll/salary-lines
- Fiken via Chift: https://docs.chift.eu/connectors/accounting/fiken · BDO: https://www.bdo.no/en-gb/services/audit-and-assurance/transferring-accounting-data/fiken
- CloudEvents: https://cloudevents.io/ · InfoQ (graduation): https://www.infoq.com/news/2024/04/cncf-cloudevents-graduation
- Standard Webhooks (verifisering): https://webhookrelay.com/verify-standard-webhooks-signature/ · Svix: https://www.svix.com/resources/glossary/webhook-signature/
- Digipost API: https://digipost-docs.readthedocs.io/en/latest/api/introduction.html · Partnere: https://www.digipost.no/en/business/partners
- Vipps MobilePay utviklerindeks: https://developer.vippsmobilepay.com/llms.txt
- Betalinger i Norge (NICS/Straks): https://www.atlar.com/guides/bank-payments-in-norway

**Trender, KI og marked**
- Deel AI Workforce: https://cfotech.co.uk/story/deel-launches-ai-workforce-to-streamline-global-hr-payroll · https://me.peoplemattersglobal.com/news/hr-technology/deel-rolls-out-ai-workforce-heres-how-its-bringing-ai-agents-to-workflows-46535
- Gusto Gus: https://gusto.com/company-news/gus-ai-assistant · ChatGPT: https://www.cpapracticeadvisor.com/2026/01/23/gusto-launches-payroll-inside-chatgpt/176791/
- Personio HUG 2025: https://www.personio.com/about-personio/press/hug-2025-feature-updates/
- SD Worx agentisk KI: https://www.sdworx.com/en-en/about-sd-worx/press/2026-06-24-sd-worx-introduces-agentic-ai-payroll-enhance-customer-engagement
- Visma 2025/KI: https://mfn.se/all/pr/visma/visma-delivers-strong-2025-with-record-customer-intake-and-continued-ai-led-innovation
- Rippling AI (sekundær): https://getperspective.ai/blog/rippling-ai-strategy-hr-platform-customer-conversations-product-velocity-2026/markdown
- Altinget – EU-land bommer på fristen (23.6.2026): https://www.altinget.no/artikkel/eu-landene-bommer-paa-fristen
- Altinget – ny forsinkelse for KI-loven: https://www.altinget.no/artikkel/ny-forsinkelse-for-ki-loven
- NHO om direktivet: https://www.nho.no/tema/eos-og-internasjonal-handel/samleside-eu-regelverk/eus-pay-transparancy-directive/
- CSRD Omnibus I: https://www.williamfry.com/wp-content/uploads/2026/03/Omnibus-1-Directive-comes-into-force-in-March-2026-key-amendments-to-CSRD-and-CS3D.pdf · https://accountancyeurope.eu/wp-content/uploads/2026/01/260129-Omnibus-explained-CSRD-factsheet.pdf · BDO stop-the-clock Norge: https://www.bdo.no/en-gb/insights/csrd-the-stop-the-clock-directive-has-now-been-adopted-in-norway
- BankID/Stø: https://www.bytt.no/artikler/forbruker/a-jpml/alternativer-til-bankid-slik-beholder-du-tilgangen-til-nav-og-helsenorge-i-2026 · FIDO: https://fidoalliance.org/fido-webinar-the-spectrum-of-authentication-how-bankid-norway-unifies-passkeys-biometric-liveness
- Utleggsappen/Advania (LinkedIn): https://no.linkedin.com/in/steffentors
- Regnskap Norge omdømme 2026: https://kommunikasjon.ntb.no/pressemelding/19006403/regnskapsbransjen-star-stott-i-befolkningen-og-stoltheten-i-bransjen-oker?lang=no · KI-undersøkelse: https://storage.mfn.se/fec97e8d-0f9d-4629-a7f6-0b72622d9ff3/ki-bruk-i-norsk-administrasjon-og-ledelse.pdf
- Kontinuerlig lønn (leverandørsyn): https://www.usemultiplier.com/global-payroll/future-of-global-payroll · https://www.ramco.com/blog/payroll/global-payroll-trends-2026-ai-cloud-real-time-payroll
- EWA-regulering (USA, kontekst): https://www.crowdfundinsider.com/2026/02/260873-us-fintech-associations-ask-circuit-court-to-decide-earned-wage-access-services-are-not-loans/
- Trekk i lønn: https://www.virke.no/arbeidsgiverstotte/lonn/trekk-lonn/ · https://www.ks.no/ks-advokatene/nyheter/arbeidsgiver-adgang-til-trekk-i-lonn-for-a-korrigere-feilutbetalinger/
