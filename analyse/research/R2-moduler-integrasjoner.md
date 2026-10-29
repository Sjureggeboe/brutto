# R2 – Egne moduler (ferie/fravær, timer, utlegg), HR for å erstatte Huma, og integrasjonskatalog for «Brutto»

**Runde 2 i behovskartleggingen · 28.10.2026 · bygger på runde 1 (rapportene A–G i samme mappe)**

**Merking**
- **[V]** verifisert mot primærkilde i denne eller forrige runde: lov, forskrift, myndighet eller leverandørens egen dokumentasjon
- **[S]** sekundærkilde (Sticos, Azets, Revisorforeningen, Smartbyrå o.l.)
- **[K]** kjent fra før, ikke sjekket på nytt i denne runden
- **[U]** usikker, må verifiseres før det bygges
- **[A]** min vurdering eller anbefaling
- **[KONFIG]** skal være innstilling per kunde, tariff eller arbeidsforhold, ikke hardkodet

**Arbeidsmåte:** Først skrev jeg et utkast (runde A). Så kritiserte jeg det (runde B): Hva er for mye for MVP? Hvor bygger vi noe kunden allerede har? Hva er juridisk feil? Dokumentet viser den reviderte versjonen. **Kapittel 9** forteller hva som ble endret og hvorfor.

**Tillegg underveis:** Gründeren har bedt om at Huma (humahr.com) blir en prioritert integrasjon, og at Brutto på sikt skal erstatte Huma. Det dekkes i **kapittel 5** (HR-xx og Huma-paritet for fravær), i **2.5** (konkurrentbildet for fravær) og i **6.6** (katalogen).

---

## 0. Sammendrag

1. **Kjernen eier konsekvensene, modulene eier fakta [A].** En fraværs-, time- eller utleggsmodul, enten den er vår egen eller ekstern, leverer *fakta*: hva som skjedde, når, hvem som godkjente og hvilken dokumentasjon som finnes. Lønnskjernen eier *konsekvensene*:
   - arbeidsgiverperiode (AGP), refusjon og inntektsmelding
   - feriepenger og ferietrekk
   - prising av timer, trekkplikt og AGA
   - rapportering av permisjon og permittering i a-meldingen
   - bilag

   Bare slik kan kunden bytte ut en egen modul med Planday, Huma eller Utleggsappen uten at lønna blir feil. Det er også slik «like vilkår» blir sant i praksis.
2. **Saldoer føres i en hovedbok i kjernen [A].** Det gjelder ferie, avspasering, egenmeldingsdager og omsorgsdager. Modulene poster transaksjoner via det offentlige API-et. Bytter kunden modul, blir saldoene liggende.
3. **Ferie og fravær er lønnskritisk fra dag én.** Følgende må ligge i kjernen ved lansering:
   - tilstandsmaskin for AGP
   - inntektsmelding og sykmelding via NAVs LPS-API
   - feriepenger ved fravær og ferietrekk
   - permisjon over 14 dager og all permittering i a-meldingen

   En enkel egen fraværsmodul (søknad, godkjenning, kalender) bør også være med ved lansering. Det er nødvendig for å kunne erstatte Huma, og fordi kundene forventer det.
4. **Timemodulen holdes smal ved lansering:**
   - timeliste for timelønte
   - avviks- og overtidsføring for fastlønte
   - lovgrensene for overtid
   - oversikten som arbeidsmiljøloven § 10-7 krever
   - import fra vaktsystemer

   Turnus- og vaktplanlegging og stempelklokke bygger vi ikke. Prosjekttimer for Forskningsrådet og EU kommer i fase 2. Det er et tydelig fortrinn i stiftelsessegmentet.
5. **Utlegg:** Godtgjørelsesmotoren hører til kjernen. Den deler bilgodtgjørelse og diett i trekkfri og trekkpliktig del og setter a-meldingsbeskrivelse, antall døgn, km og passasjernavn, MVA-kode og bilag. Ved lansering holder det med en enkel egen reiseregning- og utleggsflyt. Firmakort og avanserte reisepolicyer kommer senere.
6. **Juridiske korreksjoner fra runde B** (detaljer i kap. 9):
   - Egenmelding er 3 kalenderdager per tilfelle etter loven. IA-avtalen 2025–2028 gir ingen rett til utvidet egenmelding.
   - 6G-taket gjelder bare 60+-tillegget i feriepengene.
   - Sykefravær rapporteres ikke som permisjon i a-meldingen, bortsett fra fravær ut over 12 måneder.
   - Oversikten etter aml. § 10-7 gjelder alle ansatte, ikke bare timelønte.
   - Trekk i lønn for å rette opp feil krever forhåndsavtale.
   - Det er ikke fradrag for inngående MVA på representasjon, servering, kost til ansatte eller personbil.
7. **Huma:** Brutto integreres med Huma ved lansering (Open API og webhooks) og lever side om side med Huma til å begynne med. Deretter tar Brutto over HR-funksjonene steg for steg:
   - **Ved lansering:** personalregister, organisasjonsstruktur og lett personalmappe
   - **Fase 2:** digitale arbeidsavtaler med e-signering, on- og offboarding, sykefraværsoppfølging og enkle medarbeidersamtaler
   - **Fase 3:** utstyr

   Fraværsmodulen må ha samme datamodell og hendelser som Huma, så kunder kan flyttes uten tap av historikk.
8. **Integrasjonskatalogen** vurderer over 100 systemer og formater i 16 kategorier. **15 er valgt for lansering** (kap. 7). De fleste andre løses med fil eller CSV, eller ved at partnere bygger mot vårt offentlige API.
9. **Største risiko: omfanget [A].** Lønn, tre moduler og HR er for mye for ett team på 12–18 måneder hvis MVP-grensene ikke holdes. Modulene må lanseres «smale, men lovriktige». Det som skiller oss fra konkurrentene er koblingen mellom fravær og lønn og den gode dataflyten, ikke bredden i HR-funksjonene.

---

## 1. Felles grunnmur for modulene: «like vilkår» i praksis

### 1.1 Hvem eier hva

| Domene | Modulen eier, egen eller ekstern | Kjernen eier |
|---|---|---|
| **Fravær** | Søknad, registrering, godkjenning, kalender, vedlegg og dokumentasjon, fraværstype valgt av ansatt eller leder | Kanonisk fraværsregister per arbeidsforhold, AGP, refusjonskrav, inntektsmelding, feriepengeeffekt, ferietrekk, lønnstrekk ved ulønnet fravær, a-meldingens permisjon og permittering, saldohovedbok |
| **Timer** | Registrering, stempling, vaktplan, godkjenning, prosjekt og aktivitet | Prising (sats × mengde), lønnsarter for tillegg, feriepengegrunnlag, kostnadsfordeling i bilaget, lagret kopi av godkjent tid til § 10-7-oversikt og dokumentasjon etter bokføringsforskriften § 5-6 |
| **Utlegg** | Kvittering, reisefakta (sted, tid, overnatting, måltider, km, passasjerer), godkjenning, forslag til beløp | Klassifisering (trekkfri/trekkpliktig, AGA, a-meldingsbeskrivelse), utbetaling, korrigering, bilag og MVA-kode |

### 1.2 Tekniske regler for «like vilkår» [A]

- **Bare offentlig API.** Egne moduler bruker det samme dokumenterte OpenAPI-et, de samme tilgangsomfangene, de samme grensene for antall kall, de samme webhooks og den samme sandkassen som eksterne. Ingen interne snarveier. Det gir en reell test av API-et før partnerne tar det i bruk («dogfooding»).
- **Lønnskritisk logikk ligger i kjernen.** Kjernen validerer alle innkommende fakta med sin egen regelmotor (mønsteret «fakta + forslag» fra G, B1). En ekstern modul kan ikke gi feil skattetrekk, feil AGP eller feil a-melding.
- **Én skrivende kilde per domene.** Kilden settes per kunde og domene, for eksempel `fravær.kilde = brutto | huma | planday | …`, `timer.kilde` og `utlegg.kilde`. Det skal bare finnes én skrivende master per domene og arbeidsforhold om gangen. Unntak: Sykmeldinger fra NAV-API-et går alltid inn i kjernen, og dubletter fjernes på `sykmeldingId` (se 5.4).
- **Saldohovedbok.** Ferie (virkedager), avspasering og fleks (timer), egenmeldingsdager og -tilfeller, og omsorgsdager per barn føres som saldokontoer med transaksjoner. Lovpålagte poster beregnes av kjernen: årlig ferierett, 60+-tillegg, overføring ved sykdom og forskuddsferie. Modulene poster uttak og manuelle justeringer.
- **Modulbytte skjer med en omleggingsdato.** Historikken importeres, den gamle kilden fryses og den nye blir master. Det er samme løp som migrering fra Huma (5.6). Kunden betaler per modul (G 1.10), så det er lett å bytte.

### 1.3 Felles livssyklus og låsing

Kontraktene følger livssyklusen fra G (1.11):

`RECEIVED → VALIDATED → ACCEPTED → LOCKED → PAID → REPORTED`

Dette gjelder:
- Idempotensnøkkelen er `(kilde, eksternId, versjon)`.
- Etter `LOCKED` kommer bare korrigeringslinjer i neste kjøring.
- Korrigeringer som gir negativ netto stoppes med `REQUIRES_WRITTEN_AGREEMENT`. Etter aml. § 14-15 og HR-2021-2532-A trengs en forhåndsavtale om akkurat det trekket.

Hendelser kjernen sender til alle moduler:

| Hendelse | Bruk |
|---|---|
| `payroll.period.cutoff_scheduled.v1` / `payroll.period.locked.v1` | Fristen for godkjenning av timer, fravær og utlegg. Modulen låser sine data. |
| `payroll.input.accepted/rejected/deferred.v1` | Status per linje med årsakskode |
| `balance.updated.v1` | Ny saldo per konto (ferie, avspasering, egenmelding, omsorgsdager) |
| `absence.consequence.calculated.v1` *(ny i R2)* | Konsekvenser for lønn: «AGP slutter 14.11», «refusjon fra 15.11», «permisjon rapporteres i a-melding for november», «omsorgsdag 11 → refusjon» |
| `payroll.payrun.paid.v1` / `payroll.input.reported.v1` | Utbetalt og innrapportert. Modulen kan vise «utbetalt» og «rapportert». |

---

## 2. Modul 1: Ferie og fravær

### 2.1 (a) Lov- og regelkrav som påvirker modulen

**Ferie (ferieloven) [V]** ([Lovdata ferieloven](https://lovdata.no/dokument/NL/lov/1988-04-29-21), [§ 7](https://lovdata.no/lov/1988-04-29-21/§7); sist endret ved lov 2023-03-17-3, i kraft 1.1.2024)

| Tema | Regel | Konsekvens for systemet |
|---|---|---|
| Feriefritid | 25 virkedager per ferieår. Lørdag er virkedag, søn- og helligdager er ikke. Arbeidsgiver skal sørge for at ferien gis, og arbeidstaker plikter å avvikle den (§ 5). | Saldo i virkedager. Konvertering til arbeidsdager eller timer for deltid og turnus [KONFIG]. Varsel når ferie ikke er planlagt. |
| Nyansatte | Begynner man senest 30.9, har man rett til full feriefritid. Begynner man senere: 6 virkedager. Arbeidstaker kan nekte å avvikle ferie i den grad feriepengene ikke dekker lønnsbortfallet (§ 5). | Ferieretten første år beregnes etter startdato. Varsel om «ulønnet ferie» når opptjente feriepenger mangler (C, testcase 11). |
| 60+ | 6 ekstra virkedager for den som fyller 60 i ferieåret. Arbeidstaker bestemmer selv tidspunktet, med minst 2 ukers varsel (§ 6). Feriepengene øker med 2,3 prosentpoeng, og **bare tillegget** kan begrenses til 6G (§ 10). | Egen saldokonto «60+», som ikke må godkjennes på vanlig måte (bare varselfrist). Taket gjelder bare tillegget (se kap. 9). |
| 5. ferieuke | Avtalefestet i tariffavtale, ikke lovfestet. Feriepengesatsen er da gjerne 12 %. § 15 gir Kongen adgang til å gi lengre ferie (10,6–12,3 % ved 26–30 dager). | Tariff- eller avtaleprofil per arbeidsforhold [KONFIG]. Regler for når den 5. uken kan tas, står i tariffavtalen [U – verifiser per tariff]. |
| Fastsetting og varsling | Arbeidsgiver skal drøfte i god tid. Arbeidstaker kan kreve varsel senest 2 måneder før ferien. Fastsatt ferie kan bare endres ved uforutsette hendelser, og da med erstatning av merutgifter (§ 6). | Frister i ferieplanleggingen. Endring av godkjent ferie krever årsak og loggføres (bevis ved krav om erstatning). |
| Hovedferie og restferie | Arbeidstaker kan kreve 18 virkedager hovedferie i perioden 1.6–30.9. Det gjelder ikke den som begynner etter 15.8. Restferien på 7 virkedager kan kreves samlet innenfor ferieåret (§ 7 nr. 1–2). | Kontroll mot hovedferieperioden. Varsel til leder. |
| Overføring og forskudd | Inntil 12 virkedager overføring og inntil 12 virkedager forskuddsferie, begge etter skriftlig avtale. Ferie som ikke ble tatt på grunn av lovbrudd eller sykdom (§ 9), **skal** overføres (§ 7 nr. 3). Erstatningsansvar etter § 14. | Årsskiftejobb med tre kategorier: avtalt (krever avtaledokument), tvunget (sykdom/lovbrudd) og fortapt. Ingen automatisk sletting uten kontroll. |
| Sykdom og ferie | Blir man helt arbeidsufør før ferien, kan man kreve at ferien utsettes (legeerklæring, senest siste arbeidsdag). Blir man syk under ferien, kan man få like mange nye dager senere (legeerklæring, uten ugrunnet opphold). Ferie kan ikke legges til foreldrepermisjon uten samtykke (§ 9). | Flyt «syk i ferien» med dokumentasjon, som gir tilbakeføring til saldoen. Sperre mot ferie i foreldrepermisjon uten samtykke. |
| Feriepenger | 10,2 % (12 % ved fem uker etter avtale), +2,3 pp for 60+. Grunnlaget er arbeidsvederlag utbetalt i opptjeningsåret. Utbetales siste vanlige lønningsdag før ferien, og ved fratreden alt opptjent (§§ 10–11). | Kjernen, se C kap. 3. Modulen viser bare. |
| Feriepenger ved fravær | NAV betaler feriepenger av sykepenger for inntil 48 dager per opptjeningsår, og av foreldrepenger for 12 eller 15 uker. Arbeidsgiver kan begrense egen plikt ved forskuttering [KONFIG] (C 3.2). | Kjernen fører akkumulatorer for refusjonsdager. |

**Sykefravær (folketrygdloven kap. 8) [V]** ([ftrl. § 8-24 m.fl.](https://lovdata.no/lov/1997-02-28-19/§8-24), [§ 8-19](https://lovdata.no/lov/1997-02-28-19/§8-19))

| Tema | Regel | Konsekvens for systemet |
|---|---|---|
| Egenmelding, lovens minimum | Etter minst 2 måneders ansettelse: inntil 3 kalenderdager per tilfelle. Etter et avbrudd på over 2 uker må man ha 2 nye måneder i arbeid, men 4 uker holder etter bedriftspermittering og enkelte permisjoner (§ 8-24). Fravær over et døgnskille regnes som én egenmeldingsdag. Ved nytt fravær innen 16 dager telles tidligere fraværsdager uten legeerklæring med. | Teller per arbeidsforhold med kontroll av opptjening. Sammenslåing med tidligere fravær. |
| Utvidet egenmelding | Arbeidsgiver kan utvide retten innenfor AGP **etter drøfting med tillitsvalgte** (§ 8-24). | Policy per virksomhet med dager per tilfelle, dager og tilfeller per 12 måneder og løpende 12-månedersvindu [KONFIG]. Dato for drøftingen lagres (revisjonsspor). |
| Tap av egenmeldingsrett | Arbeidsgiver kan frata retten etter minst 4 fravær uten legeerklæring på 12 måneder, eller ved rimelig grunn til å tro at fraværet ikke skyldes sykdom. Arbeidstaker skal få uttale seg, og vedtaket skal vurderes på nytt etter 6 måneder (§ 8-27). Arbeidsgiver kan kreve skriftlig bekreftelse av muntlig egenmelding (§ 8-26), og kan nekte egenmelding ved turnus eller reiserute (§ 8-25). | Varsel til leder ved 4 tilfeller. Status «egenmelding fratatt» med dato og ny vurdering om 6 måneder. **Systemet skal ikke frata retten automatisk.** |
| IA-avtalen | IA-avtalen 2019–2024 gikk ut ved nyttår. Ny IA-avtale for 2025–2028 ble signert i februar 2025. 2025–26 brukes til kunnskapsinnhenting, og nye tiltak kommer i 2027–28. Regelverket for egenmelding er uendret ([regjeringen.no](https://www.regjeringen.no/no/tema/arbeidsliv/arbeidsmiljo-og-sikkerhet/inkluderende_arbeidsliv/hva-skjer-med-inkluderende-arbeidsliv-nar-ia-avtalen-ikke-forlenges/id3078097/), [IA-avtalen 2025–2028](https://www.regjeringen.no/no/tema/arbeidsliv/arbeidsmiljo-og-sikkerhet/inkluderende_arbeidsliv/innsikt/ia-avtalen-2025-2028/id3151146/)). Jeg fant ingen lovendring for egenmelding i 2026. | Ikke noe «IA-flagg». Malen «8 dager per tilfelle / 24 dager per 12 måneder», den gamle IA-praksisen, kan tilbys som forslag til policy [S]. |
| Arbeidsgiverperioden (AGP) | 16 kalenderdager. Fravær med mindre enn 16 dager mellomrom slås sammen. Krever 4 ukers opptjening. NAV dekker deretter opp til 6G (§§ 8-19, 8-10; B 6.2). | Tilstandsmaskin over fraværsepisoder i kjernen. |
| Sykmelding og søknad | NAV leverer sykmelding og søknad om sykepenger til arbeidsgiver. Et lønns- og personalsystem (LPS) kan hente dem via API, og sende inntektsmelding med refusjonskrav som svar på forespørsel fra NAV (scope `nav:helseytelser/sykepenger`, tilgangspakken `lonn-personopplysninger-saerlig-kategori`) (B 6.1). | Automatisk opprettet fravær fra sykmeldingen. Inntektsmelding fra kjernen. |
| Refusjon | Refusjon kan kreves for fravær inntil 3 måneder før søknadsmåneden (C 7). Utbetalte refusjoner kommer i oppgjørsrapport fra NAV (API). | Fordring på NAV i regnskapet og avstemming. |
| Oppfølging | Oppfølgingsplan senest etter 4 uker, med mindre det åpenbart er unødvendig. Innkalling til dialogmøte senest etter 7 uker ved helt fravær. Planen sendes NAV minst 1 uke før dialogmøte 2. Arbeidsgiver må kunne dokumentere oppfølgingen ([aml. § 4-6](https://lovdata.no/lov/2005-06-17-62/§4-6)). | Oppgaver med frister (fase 2, kap. 5). |
| Personvern | Opplysninger om fravær på grunn av sykdom er helseopplysninger (GDPR art. 9). Arbeidsgivers kopi av sykmeldingen har ikke diagnose [K]. | Egen tilgangsrolle «Fravær – helse» (G 1.9). Grunnen til egenmeldingen lagres ikke. |

**Sykt barn og pleie av nærstående [V]** ([NAV omsorgspenger](https://www.nav.no/arbeidsgiver/omsorgspenger), [aml. kap. 12](https://lovdata.no/lov/2005-06-17-62/§12-10))

| Tema | Regel | Konsekvens for systemet |
|---|---|---|
| Omsorgsdager | 10 dager per år med 1–2 barn og 15 med 3 eller flere. Dobbelt ved aleneomsorg. Ved kronisk sykdom eller funksjonshemning gis 10 ekstra per barn (20 ved aleneomsorg). Gjelder ut kalenderåret barnet fyller 12 år, og til 18 år ved vedtak om ekstra dager. | Saldokonto per år. Antall barn og fødselsår trengs (HR-05). Vedtak om ekstra dager registreres manuelt. |
| Hvem betaler | Arbeidsgiver betaler lønn for alle dagene og dekker de første 10 selv. Fra dag 11 kan arbeidsgiver kreve refusjon (dagsats med 260 som divisor, maks 6G). Krever 4 ukers opptjening. Delvise dager: 7,5 timer regnes som én dag. | Teller for «arbeidsgivers 10 dager» og refusjonsgrunnlag. |
| Dokumentasjon | Egenmelding de tre første dagene. Legeerklæring kan kreves fra og med fjerde sammenhengende dag. | Varsel om krav til legeerklæring. |
| Refusjonskrav | NAV skriver at alle inntektsmeldinger og refusjonskrav for omsorgspenger fra 21.5.2026 må sendes via Min side – arbeidsgiver. NAVs API-oversikt har samtidig et LPS-API for «sykdom i familien» i produksjon (B 6.1). | **[U]** Avklar med NAV om LPS-API-et gjelder etter 21.5.2026. Inntil videre: fase 2, med manuell innsending og oppfølging i Brutto. |
| Pleie av nærstående | 10 dager per kalenderår for nødvendig omsorg for foreldre, ektefelle eller samboer, og 60 dager ved pleie i livets sluttfase (aml. § 12-10). | Permisjonstype med teller. |
| A-melding | Sykt barn rapporteres ikke som permisjon ([Skatteetaten](https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/the-a-melding-guide/employment/information-on-employment/leave/)). | Ingen permisjonslinje. |

**Foreldrepermisjon og andre permisjoner [V]**

| Tema | Regel | Konsekvens for systemet |
|---|---|---|
| Rettigheter | Aml. §§ 12-1 til 12-8: svangerskapskontroll, svangerskapspermisjon, omsorgspermisjon (2 uker), fødselspermisjon, foreldrepermisjon, delvis permisjon, varslingsplikt og ammefri. | Permisjonstyper med lovhenvisning. |
| Foreldrepenger | Med ett barn: 49 uker med 100 % eller 61 uker og 1 dag med 80 %. Maks 6G. Inntektsmelding sendes tidligst 4 uker før fraværet og er samtidig refusjonskrav. Refusjonsperioder skal beholdes fra første fraværsdag, og ved start eller stans av refusjon legges en periode med 0 kr inn ([NAV](https://www.nav.no/arbeidsgiver/foreldrepenger)). | Inntektsmelding for foreldrepenger via API (fp-inntektsmelding-api, oppført som i produksjon, B 6.1). Refusjonsplan per periode. |
| Utdanningspermisjon | Krever minst 3 år i arbeidslivet og 2 år hos arbeidsgiveren. Inntil 3 år, hel eller delvis. Skriftlig melding. Arbeidsgiver kan nekte av hensyn til driften (aml. § 12-11). | Kontroll av vilkår. A-melding: «utdanningspermisjon (lovfestet)» eller «(ikke lovfestet)». |
| Andre lovfestede | Militærtjeneste (§ 12-12), offentlige verv (§ 12-13), religiøse høytider (§ 12-15). | Permisjonstyper. |
| Velferdspermisjon | Ingen generell lovrett. Følger tariffavtale eller personalhåndbok [K]. | Policy: lønnet eller ulønnet, maks dager, krav om dokumentasjon [KONFIG]. |
| Ulønnet permisjon | Etter avtale. Over 14 dager gir krav om ny opptjening for sykepenger (C 7). | Forholdsmessig lønnstrekk i kjernen. Varsel om sykepengerett. |
| A-melding | **Permisjon over 14 dager**, hel eller delvis, lønnet eller ulønnet, sammenhengende eller ikke, skal rapporteres. Kortere permisjon *kan* rapporteres. Hver permisjon har en beskrivelse (foreldrepermisjon, militærtjeneste, utdanning lovfestet/ikke lovfestet, annen lovfestet, annen ikke lovfestet), permisjonsId, startdato, sluttdato og prosent. Endres prosenten, avsluttes ID-en og en ny opprettes. **Sykefravær rapporteres ikke**, med unntak av fravær ut over 12 måneder ([Skatteetaten, permisjon](https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/the-a-melding-guide/employment/information-on-employment/leave/)). | Kjernen lager permisjonslinjer automatisk fra fraværsregisteret. |

**Permittering [V/S]**

| Tema | Regel | Konsekvens for systemet |
|---|---|---|
| Lønnsplikt og maksimal tid | Arbeidsgiver har lønnsplikt i 15 arbeidsdager. Deretter er det lønnsfritak i inntil 26 uker innenfor 18 måneder (C 0.1 [V NAV]; [SNL](https://snl.no/permitteringsl%C3%B8nnsloven) [S]). Jeg fant ingen endring for 2026. | Tellere i kjernen og varsel før 26 uker. |
| Varsel og NAV | Varsel normalt 14 dager etter Hovedavtalen og tariff [K]. Melding til NAV gis via skjema på nav.no. Det finnes **ikke noe API** (B 6.3). | Brutto lager varselbrev og en sjekkliste, men sender ikke noe til NAV. |
| A-melding | Permittering rapporteres **uansett lengde** og uansett om den ligger innenfor lønnspliktperioden. Rapporteres hver måned til den er slutt, med ID, start, slutt og prosent av stillingsprosenten. Permittering som starter etter en permisjon, rapporteres fra dagen etter at permisjonen slutter ([Skatteetaten, permittering](https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/the-a-melding-guide/employment/information-on-employment/layoffs/)). | Automatisk fra fraværsregisteret. |

**Avspasering og fleksitid [V]**
- Arbeidstaker og arbeidsgiver kan **skriftlig** avtale at overtid avspaseres helt eller delvis ([aml. § 10-6 tolvte ledd](https://lovdata.no/lov/2005-06-17-62/§10-6)). Overtidstillegget på minst 40 % (ellevte ledd) skal etter vanlig praksis utbetales selv om timene avspaseres [K].
- Arbeidstaker har rett til fleksibel arbeidstid hvis det kan gjennomføres uten vesentlig ulempe for virksomheten ([§ 10-2 tredje ledd](https://lovdata.no/lov/2005-06-17-62/§10-2)). Fleksitidsordninger og timebank styres av avtale, for eksempel statens fleksitidsavtale [K].
- **Systemet trenger:** saldokonto for timebank, en markering av at det finnes skriftlig avtale om avspasering, og en regel om at tillegget utbetales mens grunntimene går i banken.

### 2.2 (b) Funksjonelle behov – ferie og fravær (FT-xx)

MoSCoW: **Må / Bør / Kan / Ikke nå**. «Lansering» betyr at kravet må være med når lønn lanseres.

**Ansatt**

| ID | Behov | MoSCoW | Merknad |
|---|---|---|---|
| FT-01 | Søke ferie (hele og halve dager) og se saldo: rett, planlagt, avviklet, overført, forskudd og 60+ | Må | Saldoen hentes fra kjernens hovedbok |
| FT-02 | Registrere egenmelding for egen sykdom, med teller mot lov eller virksomhetens policy | Må | Ingen årsak lagres |
| FT-03 | Registrere sykt barn eller barnepasser, med teller per år og barn | Må | Krever barneopplysninger (HR-05) |
| FT-04 | Sykmelding fra NAV dukker opp automatisk som fravær, uten at ansatt eller leder registrerer noe | Må | NAV-API (samme tilgang som inntektsmelding). Flyttet opp i runde B. |
| FT-05 | Søke permisjon (velferd, ulønnet, utdanning, foreldre, pleie) med vedlegg og prosent | Må | Permisjonstyper fra lov og policy |
| FT-06 | Melde «syk i ferien» med legeerklæring, som gir dagene tilbake | Må | Ferieloven § 9 |
| FT-07 | Ta ut avspasering eller fleks mot timebank | Bør | Avhenger av timemodulen |
| FT-08 | Egen fraværskalender og abonnement i Outlook/Google (ICS) | Bør | ICS er billig. Toveis kalender kommer i fase 2. |
| FT-09 | Se hvordan fravær påvirker lønn og feriepenger («hvorfor er lønna lavere i juni?») | Bør | Forklaring på lønnsslippen |
| FT-10 | Varsel om ulønnet ferie (nyansatt uten feriepenger) | Bør | Ferieloven § 5 |

**Leder**

| ID | Behov | MoSCoW | Merknad |
|---|---|---|---|
| FT-20 | Godkjenne eller avslå med kommentar. Stedfortreder og delegering ved fravær. | Må | Godkjenningskjeden kommer fra organisasjonsstrukturen (HR-03) |
| FT-21 | Teamkalender som viser hvem som er borte, med varsel om bemanningskonflikt | Må | Det kundene ser først hos Huma og Planday |
| FT-22 | Ferieplanlegging: kontroll av hovedferie, varsel 2 måneder før, purring på uplanlagt ferie, ferieliste | Bør | Ferieloven §§ 6–7 |
| FT-23 | Varsel ved 4 egenmeldingstilfeller på 12 måneder, med flyt for å frata retten (uttalelse og ny vurdering etter 6 måneder) | Bør | Ftrl. § 8-27. Aldri automatisk. |
| FT-24 | Sykefraværsoppfølging: oppfølgingsplan innen 4 uker og dialogmøte innen 7 uker, med dokumentasjon | Bør (fase 2) | Aml. § 4-6. Kreves for å erstatte Huma (kap. 5). |
| FT-25 | Registrere nærmeste leder hos NAV og dele oppfølgingsplan digitalt | Kan (fase 2) | NAVs syfo-API-er (B 6.1) |

**Lønn og HR**

| ID | Behov | MoSCoW | Merknad |
|---|---|---|---|
| FT-40 | Fraværstyper med effekt på lønn: lønnet eller ulønnet, trekkmetode, feriepengeopptjening, teller i AGP, a-meldingsbeskrivelse for permisjon og lovhjemmel | Må | Kan konfigureres, men leveres med norske standardtyper |
| FT-41 | Ferieprofil per arbeidsforhold: 25 eller 30 virkedager eller arbeidsdager, 5. uke etter tariff, 60+, nyansattregel og deltid eller timer | Må | Ferieloven §§ 5 og 15 |
| FT-42 | Saldohovedbok med årsskiftejobb: avtalt overføring og forskudd (inntil 12 dager, skriftlig), tvunget overføring ved sykdom eller lovbrudd, rapport over fortapte dager før sletting | Må | Ferieloven § 7 nr. 3 |
| FT-43 | Ferietrekk etter valgt metode (1/26, 1/21,67, faktiske dager) og tidspunkt (juni eller når ferien tas) | Må | Kjernen (C 3.3) |
| FT-44 | Tilstandsmaskin for AGP: 16 dager, sammenslåing når det er under 16 dager mellom fraværene, egenmeldingsdager telles med, 4 ukers opptjening | Må | Kjernen |
| FT-45 | Inntektsmelding for sykepenger via NAV-API når NAV ber om det, med refusjonskrav, korrigering og oppfølging mot oppgjørsrapporten | Må | Kjernen (B 6.1) |
| FT-46 | Inntektsmelding og refusjon for foreldre- og svangerskapspenger via API | Må | Avklar status med NAV (B 6.1, motstrid) [U] |
| FT-47 | Omsorgspenger: teller for arbeidsgivers 10 dager, refusjonsgrunnlag fra dag 11, refusjonskrav | Bør | Kanal uavklart etter 21.5.2026 [U] |
| FT-48 | Permittering: prosent, lønnspliktdager, teller for 26 uker per 18 måneder, a-melding hver måned | Må | A-meldingen er lovpålagt |
| FT-49 | Permisjon over 14 dager rapporteres automatisk i a-meldingen, med ID, beskrivelse og prosent. Ny ID når prosenten endres. | Må | Skatteetaten |
| FT-50 | Ulønnet fravær gir forholdsmessig trekk, påvirker feriepengegrunnlaget og gir varsel om sykepengerett ved over 14 dager | Må | Kjernen |
| FT-51 | Feriepenger av forskuttert sykelønn eller foreldrepenger: FULL eller BEGRENSET_TIL_TRYGD, og akkumulator for 48 dager / 12–15 uker | Må | Kjernen (C 3.2) |
| FT-52 | Sykefravær ut over 12 måneder rapporteres som permisjon | Bør | Sjeldent, men lovpålagt |
| FT-53 | Endring av fravær etter låst periode gir korrigering. Negativ effekt gir flyt for forhåndsavtale eller tilbakebetaling. | Må | Aml. § 14-15 |
| FT-54 | Sluttoppgjør: feriepenger og ikke-avviklet ferie. Trekk for forskuddsferie krever skriftlig avtale. | Må | Ferieloven § 7, aml. § 14-15 |
| FT-55 | Sykefraværsstatistikk: fraværsprosent, egenmeldt og legemeldt, per avdeling og periode | Bør | Huma-paritet (5.5) |
| FT-56 | Import av inngående saldoer ved oppstart: ferie, avspasering, brukte egenmeldingsdager, pågående AGP og omsorgsdager | Må | Ved migrering midt i året (A 7) |
| FT-57 | Norsk helligdagskalender (bevegelige helligdager). Andre land senere. | Må / Kan | Huma har flere land |
| FT-58 | Tilgangsstyring for helseopplysninger: rollen «Fravær – helse» og logging av innsyn | Må | GDPR art. 9 |
| FT-59 | Policy for utvidet egenmelding med dato for drøfting med tillitsvalgte | Må | Ftrl. § 8-24 |

**Økonomi**

| ID | Behov | MoSCoW | Merknad |
|---|---|---|---|
| FT-70 | Avsetning for feriepenger med AGA per periode, og NAV-refusjon som fordring i bilaget | Må | B4 |
| FT-71 | Rapport over utestående refusjonskrav (krevd, innbetalt, avvist) | Må | Avstemming mot oppgjørsrapporten |
| FT-72 | Forpliktelse for skyldig og overført ferie i timer eller kroner, til årsoppgjøret | Bør | |

### 2.3 (c) Hvordan fravær mater lønnsmotoren og a-meldingen

**Kontrakt (offentlig API, lik for egen modul, Huma og Planday)**

| Retning | Hendelse | Nøkkelfelt |
|---|---|---|
| Modul → kjerne | `absence.requested.v1` | Bare når kunden ønsker at kjernen skal se søknader, for eksempel til feriepengeprognose |
| Modul → kjerne | `absence.approved.v1` / `absence.changed.v1` / `absence.cancelled.v1` | Se payload under |
| NAV → kjerne (direkte) | `nav.sykmelding.received.v1`, `nav.soknad.received.v1`, `nav.im_forespørsel.received.v1` | sykmeldingId, periode, grad, arbeidsgiverperiode-info |
| Kjerne → modul | `absence.consequence.calculated.v1` | AGP-id, AGP-dager brukt, refusjon fra-dato, a-melding-permisjonId, lønnseffekt (+/−) |
| Kjerne → modul | `balance.updated.v1` | Konto, saldo, transaksjon |
| Kjerne → modul | `payroll.input.rejected.v1` | For eksempel `EMPLOYMENT_NOT_FOUND`, `PERIOD_LOCKED`, `INVALID_CLASSIFICATION`, `REQUIRES_WRITTEN_AGREEMENT` |

**Payload (utdrag) [A]**

```json
{
  "absenceId": "ext:huma:abs_88213",
  "version": 3, "supersedes": 2,
  "employmentId": "arb_31Qa",
  "type": "SICK_SELF_CERTIFIED",
  "policyCode": "EGENMELDING_UTVIDET",
  "from": "2026-11-02", "to": "2026-11-04",
  "partialDay": null,
  "grade": 100,
  "child": null,
  "source": "EXTERNAL", "sourceSystem": "huma",
  "documentation": { "kind": "SELF_DECLARATION", "navSykmeldingId": null },
  "status": "APPROVED",
  "approvedBy": "per_19Xz", "approvedAt": "2026-11-05T08:12:00Z"
}
```

**Fraværstype → lønn, feriepenger, NAV og a-melding**

| Fraværstype | Lønn i perioden | Feriepengegrunnlag | AGP og refusjon | A-melding | NAV-kanal |
|---|---|---|---|---|---|
| Ferie | Ferietrekk (juni eller når ferien tas) | Feriepenger utbetales og inngår ikke i nytt grunnlag | – | Feriepenger og ferietrekk som egne linjer (C 3.3). Ingen permisjon. | – |
| Egenmelding | Full lønn | Ja | Teller i AGP | Ingen permisjon | Inntektsmelding hvis fraværet går ut over AGP |
| Sykmelding i AGP | Full lønn (beregnet sykelønn) | Ja | AGP | Ingen permisjon (under 12 måneder) | Inntektsmelding via API |
| Sykmelding etter AGP | Forskuttering (lønn) eller stans | Arbeidsgiver: [KONFIG]. NAV: 48 dager. | Refusjon opptil 6G | Ingen permisjon (under 12 måneder) | Inntektsmelding med refusjon, oppgjørsrapport |
| Sykt barn | Full lønn | Ja | Arbeidsgiver dekker 10 dager, refusjon fra dag 11 | Rapporteres ikke | Min side eller API [U] |
| Foreldrepermisjon | Lønn og refusjon, eller stans | NAV: 12/15 uker. Arbeidsgiver: [KONFIG]. | Refusjon opptil 6G | Permisjon «foreldrepermisjon» over 14 dager | Inntektsmelding for foreldrepenger via API |
| Ulønnet permisjon | Forholdsmessig trekk | Nei | Ny opptjening etter 14 dager | Permisjon over 14 dager | – |
| Velferdspermisjon (lønnet) | Full lønn | Ja | – | Normalt under 14 dager, så ikke rapportert | – |
| Utdanningspermisjon | Etter avtale | Etter lønn | – | Permisjon, lovfestet eller ikke | – |
| Permittering | Lønnsplikt i 15 arbeidsdager, deretter bare arbeidet andel | Bare lønnspliktdager og arbeidet tid | – | **Alltid** permittering med prosent | Skjema på nav.no (ikke API) |
| Avspasering eller fleks | Ingen effekt på lønn (tillegget er allerede betalt) | – | – | – | – |

**Låsing og korrigering**
- Fravær registrert *før* frist (`cutoff`) tas med i perioden. Fravær registrert *etter* frist går til neste periode, og modulen får `deferred`.
- Fravær som endres *etter* `LOCKED`:
  - Kjernen beregner differansen. Gir den mer lønn (for eksempel kansellert ulønnet permisjon), kommer en positiv korrigeringslinje i neste kjøring.
  - Gir den mindre lønn (for eksempel ulønnet permisjon registrert etter utbetaling), blir resultatet `REQUIRES_WRITTEN_AGREEMENT`. Trekk krever da en forhåndsavtale om akkurat dette trekket (aml. § 14-15 andre ledd bokstav c, HR-2021-2532-A), og ellers tilbakebetaling.
- **AGP og inntektsmelding:** Endres fraværet etter at inntektsmeldingen er sendt, lages en korrigert inntektsmelding. NAVs API støtter endret inntektsmelding [K – verifiser i API-wikien].
- **A-melding:** Endres en permisjon eller permittering i en måned som allerede er rapportert, sendes ny a-melding for samme måned som erstatter den forrige (B 2.4). Endres prosenten, avsluttes den gamle ID-en og en ny opprettes. Feil rettes med 0 % og lik start- og sluttdato, og så ny ID (Skatteetaten).

### 2.4 (d) MVP eller senere

**Må være innebygd i kjernen fra dag én for at lønna skal bli riktig** (uavhengig av hvilken modul som brukes):
1. Kanonisk fraværsregister og saldohovedbok, med inngående saldoer ved migrering
2. AGP-tilstandsmaskin, inntektsmelding for sykepenger og sykmelding via NAV-API, refusjonsfordring
3. Feriepengeakkumulatorer, inkludert FULL eller BEGRENSET ved forskuttering og grensene for NAV-dager
4. Ferietrekk og sluttoppgjør
5. A-melding: permisjon over 14 dager (med ID-håndtering) og all permittering
6. Lønnstrekk ved ulønnet fravær, og korrigering etter låsing med sperre etter § 14-15

**Egen fraværsmodul ved lansering (smal):** FT-01 til FT-06, FT-20, FT-21, FT-57 (Norge) og FT-59. Altså søknad, godkjenning, teamkalender og egenmelding og sykt barn med tellere.

**Fase 2 (3–9 måneder etter lansering):**
- sykefraværsoppfølging etter § 4-6 (FT-24)
- ferieplanlegging (FT-22)
- egenmeldingskontroll (FT-23)
- refusjon av omsorgspenger (FT-47)
- statistikk (FT-55)
- toveis kalender
- nærmeste leder hos NAV (FT-25)

**Kan overlates til integrasjon:**
- vakt- og turnusbasert fravær (Planday, Tamigo, Quinyx og GAT eier fraværsregistreringen i turnus)
- HR-funksjonene rundt fraværet hos kunder som beholder Huma eller Simployer

Lønnskonsekvensene kan *aldri* overlates til andre.

### 2.5 (e) Konkurrentbilde – ferie og fravær (inkludert Huma)

| Aktør | Hva de har | Svakheter (kilde) |
|---|---|---|
| **Visma (Payroll, Employee og Manager-appene)** | Ferie og fravær, sykefravær og NAV-refusjon som egen modul, godkjenning i Visma Manager (A 2.2) [V] | Brukerne roser sykefraværsmodulen, men kaller Visma «rigid». Retro er komplisert, og det er dobbelt arbeid (Regnskap Norge, A 2.2) [V] |
| **SD Worx** | Automatisert fravær og NAV-refusjon. Fraværsmodulen får særlig ros (A 2.1) [V] | Tungt og avansert. Passer best for store kunder og tariffkompleksitet (A 2.1) |
| **Tripletex** | Ferie- og fraværssøknad som legges i timelisten etter godkjenning, feriesaldo per ansatt ([Tripletex hjelp](https://hjelp.tripletex.no/hc/no/articles/6932761980305)) [S] | Kritikk for manglende automasjon og fraværsmodul (A 3) [V] |
| **PowerOffice Go** | Ferie og fravær til 35 kr per bruker (A 3) [V] | Svak timebank og få lønnsarter, holder ikke for større virksomheter (A 3) [V] |
| **Simployer** | HR-system (ikke lønn) med integrasjoner mot Visma, Tripletex og PowerOffice (A 3) [V]. Har trolig ferie- og fraværsfunksjoner [U] | Er ikke lønn, så lønnskonsekvensene må gjøres i lønnssystemet |
| **Planday** | Fraværskontoer med fast eller opptjent saldo, godkjenning, helligdagskalender. Godkjent fravær sendes til lønn som godkjent timelisteoppføring. Har API for fravær med kontoer, saldo og transaksjoner ([Planday hjelp](https://help.planday.com/en/articles/30535-leave-management-explained), [Planday API](https://openapi.planday.com/)) [V] | Ingen norsk logikk for feriepenger, egenmelding eller NAV dokumentert. Administrator må selv sette opp reglene [V] |
| **Huma** | Selvbetjening i app, ledergodkjenning, felles kalender, helligdager per land og lokasjon, automatisk import av sykmeldinger fra NAV, oppfølging av sykmeldte som starter automatisk, sykefraværsrapporter med filtre, webhooks for fravær (`absence-create/update/delete/export`) ([Huma fravær](https://humahr.com/no/fravaer), [Huma NAV](https://humahr.com/no/nav), [webhooks](https://humahr.com/knowledge/webhooks)) [V] | Kjører ikke lønn. Ingen dokumentert AGP, refusjon eller inntektsmelding. Integrasjonssiden beskriver synkronisering av *ansattdata* mot lønnssystemer, men ikke fravær ([Huma integrasjoner](https://humahr.com/no/integrasjon)) [V]. Eksportkoden fra fraværspolicyen er ikke med i webhook-dataene [V]. **Overgangen fra fravær til lønn er altså manuell.** |
| **Huldt & Lillevik / Finago / NettLønn** | Lønn med fravær i varierende grad [K] | Feil i feriepenger og 60+ ved oppstart (Finago, A 3) [V] |

**Muligheten [A]:** Ingen av de mindre aktørene har en sammenhengende kjede fra registrering til AGP, inntektsmelding, refusjon, feriepenger og a-melding. Huma og Planday er gode på registrering, men stopper der. Visma og SD Worx har hele kjeden, men er tunge.

Brutto kan vinne på dette:
- Fravær registrert i appen gir riktig lønn, inntektsmelding og a-melding uten at noen taster det inn på nytt.
- Kunden kan likevel beholde Huma eller Planday hvis hun vil.

---

## 3. Modul 2: Timer

### 3.1 (a) Lov- og regelkrav

| Tema | Regel | Konsekvens for systemet |
|---|---|---|
| **Arbeidstidsregistrering (aml. § 10-7) [V]** | Det skal finnes en oversikt over hvor mye *hver enkelt arbeidstaker* har arbeidet. Den skal være tilgjengelig for Arbeidstilsynet og de tillitsvalgte ([§ 10-7](https://lovdata.no/lov/2005-06-17-62/§10-7)). Gjelder **alle**, også fastlønte, med unntak for ledende og særlig uavhengige stillinger (§ 10-12). | Hver ansatt trenger et arbeidstidsgrunnlag: fast plan pluss avvik, eller full registrering. Rapporten etter § 10-7 skal kunne eksporteres. Om en fast plan med registrering av avvik er godt nok, bør avklares med Arbeidstilsynet sin veiledning [U]. |
| **Unntak (§ 10-12) [V]** | Kapittel 10 gjelder ikke ledende eller særlig uavhengige stillinger, bortsett fra § 10-2 første, andre og fjerde ledd. | Flagg på arbeidsforholdet med begrunnelse. Ingen overtid og ingen kontroll av grenser. |
| **Alminnelig arbeidstid (§ 10-4) [V]** | 9 timer per døgn og 40 timer per uke. 38 timer ved blant annet todelt skift med jevnlig søn- og helgedagsarbeid, arbeid minst hver tredje søndag og hovedsakelig nattarbeid. 36 timer ved døgnkontinuerlig skift og arbeid under jord. Vekting ved tredelt skift ([§ 10-4](https://lovdata.no/lov/2005-06-17-62/§10-4)). Tariffen kan gi kortere tid, som 37,5 eller 35,5 timer. | `arbeidstidsordning` og `timer per uke for full stilling` på arbeidsforholdet. Begge rapporteres i a-meldingen [K]. |
| **Gjennomsnittsberegning (§ 10-5) [V]** | Skriftlig avtale med arbeidstaker: inntil 52 uker, maks 10 t/døgn og 48 t/uke i snitt over 8 uker, maks 50 t i én uke. Med tillitsvalgte i tariffbundet virksomhet: 12,5 t/døgn og 54 t i én uke. Med Arbeidstilsynets samtykke: inntil 26 uker og 13 t/døgn ([§ 10-5](https://lovdata.no/lov/2005-06-17-62/§10-5)). | Avtaletype og periode på arbeidsforholdet. Overtid regnes mot snittet (fase 2). |
| **Overtid (§ 10-6) [V]** | Bare ved særlig og tidsavgrenset behov, og drøftet med tillitsvalgte når det er mulig. **Grenser:** 10 t per 7 dager, 25 t per 4 uker og 200 t per 52 uker. Etter skriftlig avtale med tillitsvalgte i tariffbundet virksomhet: 20 t / 7 d, 50 t / 4 uker og 300 t / 52 uker. Med Arbeidstilsynet: 25 t / 7 d og 200 t / 26 uker. **Samlet arbeidstid** maks 13 t per døgn og 48 t per uke (snitt over 8 uker, maks 69 t i én uke). Tillitsvalgte kan avtale inntil 16 t per døgn. Overtid ut over den alminnelige rammen krever frivillighet. **Tillegg minst 40 %.** Avspasering etter skriftlig avtale ([§ 10-6](https://lovdata.no/lov/2005-06-17-62/§10-6)). | Overtidshovedbok per arbeidsforhold med rullerende vinduer (7 d, 4 uker, 26 og 52 uker). Grenseprofil per virksomhet: lov, tariffavtale eller Arbeidstilsynet [KONFIG]. Minst 40 % som laveste sats. |
| **Hviletid (§ 10-8) [V]** | 11 timer sammenhengende fri per 24 timer og 35 timer per 7 dager. Søndag skal så langt mulig være fri. Tariffavtale kan gi minst 8 og 28 timer med kompenserende hvile ([§ 10-8](https://lovdata.no/lov/2005-06-17-62/§10-8)). | Kontrollen krever start- og sluttidspunkt. Det har vaktsystemene, men ikke timelister med bare antall timer. Hviletidskontroll i egen modul kommer derfor i fase 2. |
| **Nattarbeid (§ 10-11)** | Arbeid mellom kl. 21 og 06 er nattarbeid, og det er bare tillatt når arbeidets art gjør det nødvendig [K]. | Tidsvindu for natt-tillegg og natt-kontroll [KONFIG etter tariff]. |
| **Dokumentasjon av lønn (bokføringsforskriften § 5-6) [V]** | For timelønte skal antall timer per dag og samlet for perioden dokumenteres (B 10.2). | **Lovkrav for timelønte:** Timer per dag må lagres i kjernen, ikke bare summer. |
| **Tariff [K]** | Tillegg for kveld, natt, helg, helligdag, skift og turnus, beredskap og hjemmevakt, og ulike overtidssatser (50 og 100 %). Typisk for Virke HUK og NHO Geneo (D 7). | Timetyper som mappes til lønnsarter. Satsene eies av lønn. |
| **Sykepenger for timelønte** | AGP og inntektsmeldingen bygger på snittinntekten de 3 siste månedene (ftrl. § 8-28). Det finnes spesialregler for turnus (C 7). | Timehistorikk per måned i kjernen. |
| **Forskningsrådet [V via D 6.4]** | Mottakeren *må* ha et system for registrering av arbeidstid i prosjektet for å bruke timesatser. Timesatsen er anbefalt til 0,8–1,1 promille av årslønnen, med tak på 1 100 kr per time og 1 850 timer per år ([Forskningsrådet](https://www.forskningsradet.no/finansiering/hvordan-skrive-soknad/budsjett/kostnader-naringsliv-offentlig-sektor/)). | Prosjekttimer med kobling til finansiør og timesatsberegning (fase 2). |
| **EU Horizon Europe [S]** | Personalkostnader dokumenteres med pålitelige timelister, minst månedlig, signert av ansatt og leder. Den som jobber 100 % på prosjektet kan bruke en erklæring i stedet. Tak på 215 dagsverk per år i dagsatsmodellen ([FFG](https://www.ffg.at/en/europe/heu/legal-financial/personnel-costs), [Cambridge](https://www.research-services.admin.cam.ac.uk/manage-project/manage-ec-project/staff-costs-and-timesheets-ec-grants)). Sjekk mot gjeldende Annotated Grant Agreement [U]. | Månedlig timeark med signatur av ansatt og leder, erklæringsmal, dagsverkskvote. |

### 3.2 (b) Funksjonelle behov – timer (TI-xx)

**Ansatt**

| ID | Behov | MoSCoW | Merknad |
|---|---|---|---|
| TI-01 | Registrere timer per dag (antall eller fra–til, med pause), også på mobil | Må | Timelønte og ekstrahjelp |
| TI-02 | Registrere overtid og avvik (fastlønte) med grunn og eventuell forhåndsgodkjenning | Må | § 10-6, § 10-7 |
| TI-03 | Velge utbetaling eller avspasering. Krever skriftlig avtale, og tillegget utbetales. | Bør | § 10-6 tolvte ledd |
| TI-04 | Se saldo for timebank og fleks | Bør | Saldohovedbok i kjernen |
| TI-05 | Føre timer på prosjekt, aktivitet og finansiør | Bør (fase 2) | Må for forsknings- og stiftelsessegmentet |
| TI-06 | Stempelklokke og geolokasjon | Ikke nå | Planday, Tamigo og Quinyx |
| TI-07 | Signere månedlig timeark for prosjekter (ansatt og leder) | Bør (fase 2) | Forskningsrådet og EU |

**Leder**

| ID | Behov | MoSCoW | Merknad |
|---|---|---|---|
| TI-20 | Godkjenne timer og overtid per periode, med lås ved frist (`cutoff`) | Må | Lønn betaler aldri ugodkjent tid (B3) |
| TI-21 | Varsel ved overtid over grensene (7 d, 4 uker, 52 uker, lov eller tariff) og samlet tid over 13 t per døgn eller 48 t per uke | Må | Tellerne ligger i kjernen. Billig og juridisk viktig. |
| TI-22 | Varsel ved brudd på hviletid (11 t og 35 t) | Bør (fase 2) | Krever fra–til-tider |
| TI-23 | Vaktplan, turnus og bemanning | Ikke nå | Integrasjon |

**Lønn og HR**

| ID | Behov | MoSCoW | Merknad |
|---|---|---|---|
| TI-40 | Mapping fra timetype til lønnsart: normaltid, overtid 40/50/100 %, kveld, natt, helg, helligdag, skift, beredskap, reisetid | Må | Kjernen |
| TI-41 | Lønn eier satsene. Modulen sender bare mengder. | Må | B3 |
| TI-42 | Arbeidstidsordning per arbeidsforhold: 40/38/37,5/36/35,5, gjennomsnittsberegning, unntak etter § 10-12 | Må | Brukes også i a-meldingen |
| TI-43 | Oversikt etter § 10-7 som rapport og eksport for Arbeidstilsynet og tillitsvalgte | Må | Lovkrav |
| TI-44 | Import av timer: API og CSV-maler for Planday, Tamigo, Quinyx og GAT, med mapping og testimport før første kjøring | Må | D 5.2 |
| TI-45 | Flere importer per periode (ikke bare én før ny lønnskjøring) | Må | Kjent smerte hos Tripletex (D 5.2) |
| TI-46 | Korrigering etter låsing med korrigeringslinjer og § 14-15-sperre | Må | |
| TI-47 | Timer per dag lagres for timelønte | Må | Bokføringsforskriften § 5-6 |
| TI-48 | Overtid beregnet mot gjennomsnittsberegnet arbeidstid (§ 10-5) | Kan (fase 2) | |
| TI-49 | Prosjektlønnsrapport per finansiør: timer, timesats (Forskningsrådet 0,8–1,1 ‰, EU dagsats), sosiale kostnader | Bør (fase 2) | Tydelig fortrinn for stiftelser (D 6.4) |
| TI-50 | Timer inngår i feriepengegrunnlaget og i sykelønnsgrunnlaget for timelønte | Må | Kjernen |

**Økonomi**

| ID | Behov | MoSCoW | Merknad |
|---|---|---|---|
| TI-70 | Kostnadsfordeling av lønn på prosjekt og avdeling ut fra timer, som dimensjoner på bilaget | Må | B4 |
| TI-71 | Periodisering av timer opptjent, men ikke utbetalt (forskjøvet lønn) | Kan | |

### 3.3 (c) Hvordan timer mater lønn og a-melding

| Retning | Hendelse | Nøkkelfelt |
|---|---|---|
| Modul → kjerne | `time.period.approved.v1` | employmentId, periode, linjer {dato, timetype, antall, fra/til (valgfritt), prosjekt/aktivitet/finansiør, dimensjoner}, godkjenner |
| Modul → kjerne | `time.period.reopened.v1` | Bare før låsing |
| Modul → kjerne | `time.balance.transaction.v1` | Avspasering: inn (overtid til bank) og ut (uttak) |
| Kjerne → modul | `payroll.period.cutoff_scheduled/locked.v1` | Fristen styrer låsingen av timelisten |
| Kjerne → modul | `payroll.input.accepted/rejected.v1` | Per linje, for eksempel `RATE_EXCEEDS_LIMIT`, `EMPLOYMENT_ENDED` |
| Kjerne → modul | `time.compliance.warning.v1` *(ny)* | Overtidsteller over grense, samlet tid over 13 t eller 48 t |

**A-melding [K]:** Timelønn, overtidsgodtgjørelse og tillegg rapporteres med egne lønnsbeskrivelser i utbetalingsmåneden. Eksempler er «timelønn», «overtidsgodtgjørelse», «skifttillegg» og «uregelmessige tillegg knyttet til arbeidet tid». Arbeidsforholdet har arbeidstidsordning og antall timer per uke for full stilling. Om antall timer er påkrevd på timelønnslinjer, må sjekkes i gjeldende kodeliste [U].

**Låsing [A]:**
- Timer godkjent etter frist går til neste periode (`deferred`).
- Endringer etter `LOCKED` gir korrigeringslinjer.
- Negative korrigeringer (for mye utbetalte timer) stoppes med `REQUIRES_WRITTEN_AGREEMENT`.
- Overtidstellerne i kjernen regnes på *arbeidsdato*. Lønnen regnes på *utbetalingsdato*. Begge datoene må derfor være med.

### 3.4 (d) MVP eller senere

- **Må være i kjernen fra dag én:**
  - mapping fra timetype til lønnsart og prising
  - arbeidstidsordning på arbeidsforholdet
  - overtidstellere med grenseprofiler
  - lagring av timer per dag for timelønte
  - import via API og CSV med flere importer per periode
  - rapporten etter § 10-7
  - timer inn i grunnlaget for feriepenger og sykelønn
- **Egen timemodul ved lansering (smal):** TI-01, TI-02, TI-20 og TI-21. Altså timeliste for timelønte, overtid og avvik for fastlønte, godkjenning og varsler.
- **Fase 2:** prosjekttid og prosjektlønnsrapport (TI-05, TI-07, TI-49), timebank og avspasering (TI-03, TI-04), hviletidskontroll (TI-22) og gjennomsnittsberegning (TI-48).
- **Overlates til integrasjon:** vaktplan, turnus, stempelklokke og bemanningsoptimering (Planday, Tamigo, Quinyx, GAT, MinTid). Prosjektstyring for konsulenter (Harvest, Timely, Tripletex-prosjekt) i fase 2.

### 3.5 (e) Konkurrentbilde – timer

| Aktør | Hva de har | Svakheter |
|---|---|---|
| **Visma** | Timeføring i Payroll-familien. Visma Enterprise Ressursstyring og GAT for turnus, særlig i helse (A 2.2, D 5.2) [V] | Mange produkter. Integrasjonen er tung og egnet for store kunder. |
| **Tripletex** | Timeregistrering mot lønn til 39 kr per ansatt per måned. Sterk på prosjekt og fakturering (A 3) [V] | Bare én import før ny lønnskjøring må opprettes (Regnskap Norge, D 5.2) [V]. «Lettvekter» på lønn. |
| **PowerOffice Go** | Timer til 100 kr pluss 50 kr per bruker (A 3) [V] | Svak timebank (Regnskap Norge) [V] |
| **Planday** | Vakt, stempelklokke og timelister. API for timelister med kontroll av brudd på arbeidstidsregler, lønnseksport og fravær ([Planday API](https://openapi.planday.com/)). Integrasjoner mot Visma Lønn og Tripletex [V] | Lønnsartene må mappes manuelt. Norske regler settes opp av kunden selv. |
| **Quinyx / Tamigo** | Arbeidskraftstyring for kjeder (varehandel, service) [K]. Quinyx har en egen utviklerportal ([developer.quinyx.com](https://developer.quinyx.com/)) [V] | Krever enterprise-oppsett. Lønnseksport via fil eller koblinger. |
| **Harvest / Timely** | Prosjekttid for konsulenter og byråer [K] | Ingen kobling til norsk lønn |
| **Huma** | Timeregistrering står i produktoversikten, men integrasjonssiden sier at «timeføring kommer» [U, motstrid på humahr.com] | Ikke koblet til lønn |
| **SD Worx** | [U] Ikke kartlagt for timer i Norge | |

**Muligheten [A]:** Ingen tilbyr en ferdig prosjektlønnsrapport per finansiør (D 6.4). Små og mellomstore systemer mangler også overtidskontroll knyttet til lovgrensene. Brutto bør ikke konkurrere med Planday på vakt. Brutto bør vinne på det som skjer mellom timer og lønn: tellere, satser, sosiale kostnader og prosjektregnskap.

---

## 4. Modul 3: Utlegg (reiseregning, kjøregodtgjørelse, kvitteringer)

### 4.1 (a) Lov- og regelkrav

| Tema | Regel | Konsekvens for systemet |
|---|---|---|
| **Dokumentasjon av kjøp og utlegg (bokføringsforskriften § 5-5-1) [V]** | Kjøpsdokumentet er salgsdokumentet fra selgeren. Ved kontantkjøp over **1 000 kr** inkl. MVA skal kjøperen angis, men ikke når kjøpet betales med virksomhetens eget betalingskort. Er kjøperen ikke angitt, skal formål eller bruk fremgå, og dokumentasjonen dateres og signeres. **Ansattes utlegg:** Ved varer til videresalg eller direkte innsatsfaktor over 1 000 kr skal arbeidsgiveren angis som kjøper. Ved andre kjøp lager den ansatte en *datert og signert oppstilling med formål eller bruk*, så vidt mulig innen MVA-terminen. Kassakvitteringer oppbevares ([Lovdata, bokføringsforskriften](https://lovdata.no/forskrift/2004-12-01-1558)). | Hvert krav har formål, dato og signatur (innlogget bekreftelse) og kvittering. Varsel når en kvittering over 1 000 kr for innsatsfaktor mangler arbeidsgiver som kjøper. Frist i forhold til MVA-terminen. |
| **Reiseregning (bokføringsforskriften § 5-9) [V]** | Dokumentasjonen skal vise hvem utgiftene gjelder, formålet med reisen og hvilke arrangementer den reisende har deltatt på. Består den av flere dokumenter, skal de vise til hverandre. Den skal samsvare med skattebetalingsforskriften. | Obligatoriske felt for formål og arrangement. Lenker mellom kvitteringer og reiseregning. |
| **Bevertning og representasjon (bokføringsforskriften § 5-10) [V]** | Dokumentasjonen skal angi formålet og hvem bevertningen gjaldt. | Obligatorisk liste over deltakere og formål for kategoriene bevertning og representasjon. |
| **Krav til reiseregningen for trekkfrihet (skattebetalingsforskriften § 5-6-12) [V]** | For trekkfri bilgodtgjørelse må reiseregningen minst ha den ansattes navn, adresse og underskrift, dato for avreise og hjemkomst, formålet, arrangementer, ruten med start og mål, grunn til eventuelle omveier og samlet kjørelengde. Km kan dokumenteres med kilometerteller, GPS-kjørebok eller kart ([Skatteetaten](https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/lonn-og-ytelser/oversikt-over-lonn-og-andre-ytelser/trekkfri-bilgodtgjorelse-passasjertillegg-mv)). For kost på reise med overnatting kreves reiseregning etter forskriften, og antall døgn skal oppgis. | Mangler et felt, blir hele beløpet trekkpliktig. Systemet må stoppe mangelfulle krav før godkjenning. |
| **Trekkfrie satser 2026 (Skatteetaten) [V/S]** | Hotell 693 kr (554 med frokost). Pensjonat, hybel uten kokemuligheter eller brakke 400. Hybel med kokemuligheter eller privat overnatting 107. Uten overnatting: 6–12 t 200 kr, over 12 t 400 kr. Ulegitimert nattillegg 452. Måltidstrekk 20/30/50 % ([Skatteetaten satser](https://www.skatteetaten.no/satser/kost-og-losji-satser-for-trekk-og-skattefri-godtgjorelse/?year=2026)). Bil 3,50 kr/km, passasjer 1,00, tilhenger 1,00, skogs- og anleggsvei 1,00 ([Azets 2026](https://www.azets.com/no-no/innsikt/artikler/nye-regler-pa-hr-og-lonnsomradet-i-2026/)) [S]. | Satstabell med versjon per år. Skatteetatens satsside oppgir ikke år i teksten, så tallene kontrolleres mot satsforskriften [U]. |
| **Statens satser 2026–2027 (særavtalen) [S]** | Særavtalen for reiser innenlands gjelder 1.1.2026–31.12.2027. Egen bil 5,30 kr/km. Kost: over 12 t med overnatting 1 012 kr, 6–12 t 397, over 12 t uten overnatting 736 ([Revisorforeningen](https://www.revisorforeningen.no/en/fag/nyheter/endringer-i-saravtalene-for-reiser-fra-2026/)). Utenlandssatser per land. | Policy «statens satser» som mal. **Differansen mellom statens sats og trekkfri sats er trekkpliktig**, for eksempel 1,80 kr/km på bil. |
| **A-melding [V]** | Trekkfri bilgodtgjørelse rapporteres som «utgiftsgodtgjørelse» med riktig beskrivelse (bil, passasjertillegg, andre fremkomstmidler). Bruttobeløp og antall km oppgis. Ikke trekk og ikke AGA. Beløp over satsen rapporteres som trekkpliktig bilgodtgjørelse. **Ved passasjertillegg oppgis passasjerens navn.** Rapporteres i utbetalingsmåneden (Skatteetaten, se over). Trekkfri kost med overnatting oppgis med antall døgn. Hybel, pensjonat, brakke og opphold over 28 døgn har egne beskrivelser (G, B1). Refusjon av dokumenterte utlegg er normalt ikke opplysningspliktig [U per type]. | Regelmotor i kjernen. Passasjernavn er obligatorisk. |
| **MVA (mval. §§ 8-3 og 8-4) [V]** | Ikke fradrag for inngående MVA på **a)** servering, **b)** leie av selskapslokaler ved servering, **c)** kunst og antikviteter (med unntak), **d)** kost og naturalavlønning til eier, ledelse, ansatte og pensjonister, **e)** representasjon, **f)** gaver som ikke er av ubetydelig verdi, **g)** bolig og velferd (kantine unntatt). Ikke fradrag for personkjøretøy (§ 8-4) ([mval. § 8-3](https://lovdata.no/lov/2009-06-19-58/§8-3)). Fradrag for overnatting på hotell (12 %) i MVA-registrert virksomhet [K]. | MVA-kode bestemmes av utleggskategorien, ikke av den ansatte. Kategorien «representasjon» gir alltid kode uten fradrag. Kvitteringen må vise MVA for å gi fradrag [K]. |
| **Oppbevaring [V]** | Dokumentasjon av bokførte opplysninger skal oppbevares i 5 år (bokføringsloven § 13, B 10.3). Lagres den i utlandet, må den være tilgjengelig fra Norge (bokføringsforskriften § 7-7). | Kvitteringsbilder lagres uforanderlig med hash i 5 år. Om papiroriginalen kan kastes etter skanning, må sjekkes i bokføringsforskriften kap. 7 [U]. |
| **Firmakort og privat utlegg [A/K]** | Firmakort: kostnaden er virksomhetens og dokumenteres med kvittering mot korttransaksjonen. Den ansatte får ingen utbetaling. Private kjøp på firmakort som skal trekkes i lønn, krever skriftlig forhåndsavtale (aml. § 14-15 andre ledd c). Privat utlegg: refusjon via lønn eller leverandørreskontro. | Krav av typen «kortkvittering» har ingen utbetaling. Trekk for privat bruk krever avtale. |
| **Fordeler og trekkpliktige godtgjørelser** | Dekker arbeidsgiver en privat kostnad, er det en trekkpliktig fordel. Fast bilgodtgjørelse er trekkpliktig (G, B1). | Linjen kan merkes «privat/fordel» og blir rapportert. |
| **Ikke-ansatte** | Frivillige og styremedlemmer uten honorar får dekket utlegg mot bilag. Det er ikke lønn (D 7). | Utlegget går til leverandørreskontro og ikke til lønn. Honorarer går til lønn. |
| **Korrigering** | Trekk i lønn for å rette en feil utbetaling krever en forhåndsavtale om akkurat dette trekket ([HR-2021-2532-A](https://www.domstol.no/globalassets/upload/hret/avgjorelser/2021/desember-2021/hr-2021-2532-a.pdf)). | `REQUIRES_WRITTEN_AGREEMENT` (G) |

### 4.2 (b) Funksjonelle behov – utlegg (UT-xx)

**Ansatt**

| ID | Behov | MoSCoW | Merknad |
|---|---|---|---|
| UT-01 | Ta bilde av kvittering. OCR-forslag til beløp, dato, MVA og selger. | Må | Kjøp OCR som tjeneste. Ikke bygg den selv. |
| UT-02 | Reiseregning innenlands: fra–til med klokkeslett, formål, arrangement, sted, type overnatting, måltider dekket. Gir automatisk trekkfri og trekkpliktig diett. | Må | § 5-9 og skattebetalingsforskriften § 5-6-12 |
| UT-03 | Kjøregodtgjørelse: rute med start og mål, km (kart), passasjerer med navn, tilhenger og anleggsvei | Må | A-meldingen krever passasjernavn |
| UT-04 | Utenlandsreise med satser per land og valuta | Bør (fase 2) | Statens utenlandssatser |
| UT-05 | Utlegg i valuta med kurs | Bør (fase 2) | |
| UT-06 | Status og utbetalingsdato synlig, med varsel | Må | |
| UT-07 | Datert og signert oppstilling (innlogget bekreftelse) | Må | § 5-5-1 fjerde ledd |
| UT-08 | Koble kvittering til firmakorttransaksjon | Bør (fase 2) | |
| UT-09 | Reiseforskudd med avregning | Kan | |
| UT-10 | Utlegg for ikke-ansatte (frivillige, styre) med enkel innlogging | Bør (fase 2) | Viktig for organisasjoner |

**Leder og attestant**

| ID | Behov | MoSCoW | Merknad |
|---|---|---|---|
| UT-20 | Attestere og godkjenne etter policy: beløpsgrenser, to nivåer, ikke godkjenne eget krav | Må | Arbeidsdeling (D 3.2) |
| UT-21 | Avvise eller sende tilbake med grunn | Må | |
| UT-22 | Varsel om dublett (hash av kvittering, beløp, dato, selger) | Bør | |

**Lønn**

| ID | Behov | MoSCoW | Merknad |
|---|---|---|---|
| UT-40 | Regelmotor: deler i trekkfri og trekkpliktig, setter a-meldingsbeskrivelse, antall døgn og km og passasjernavn | Må | Kjernen (G, B1) |
| UT-41 | Satstabeller med versjon: Skatteetatens trekkfrie satser, statens særavtale, egen policy | Må | |
| UT-42 | To utbetalingsveier: via lønn (vei A) eller direkte for rene refusjoner (vei B) | Bør (fase 2) | Ved lansering: vei A og ekstra lønnskjøring |
| UT-43 | Korrigering etter utbetaling uten automatisk trekk, med flyt for forhåndsavtale eller tilbakebetaling | Må | Aml. § 14-15 |
| UT-44 | Opphold over 28 døgn, hybel, pensjonat og brakke med egne beskrivelser | Bør | |
| UT-45 | Bevertning og representasjon: krav om formål og deltakere, MVA-kode uten fradrag | Må | § 5-10, mval. § 8-3 |

**Økonomi**

| ID | Behov | MoSCoW | Merknad |
|---|---|---|---|
| UT-60 | Bilag med konto, MVA-kode, dimensjoner og kvittering som vedlegg til regnskapet | Må | B4 |
| UT-61 | Kvitteringer lagres uforanderlig i 5 år og er tilgjengelige fra Norge | Må | Bokføringsloven § 13, bokføringsforskriften § 7-7 |
| UT-62 | Avstemming mellom utlegg i regnskapet og i a-meldingen | Bør | Kjent smerte (Sticos, D 5.2) |
| UT-63 | Import av firmakort: Eurocard, Amex, Mastercard Corporate, Pleo og Folio | Senere | Hører egentlig til regnskapet |
| UT-64 | Rene refusjoner utbetales via betalingsfil (pain.001) uten lønnskjøring | Bør (fase 2) | Vei B |

### 4.3 (c) Hvordan utlegg mater lønn og a-melding

Kontrakten B1 i G (1.11) gjelder uendret for både egen modul og Utleggsappen. I runde 2 legges det til:
- `category` med konto og MVA-regel (`REPRESENTATION`, `MEAL_EMPLOYEES`, `HOTEL`, `TRANSPORT`, `CAR_PRIVATE_MILEAGE`, `OTHER`)
- `participants[]` for bevertning
- `passengers[] {navn}` for passasjertillegg
- `purpose` og `events[]` som obligatoriske felt
- `signedAt` og `signedBy`

| Linjetype | Lønn | A-melding | Regnskap |
|---|---|---|---|
| Refusjon av dokumentert utlegg | Utbetales via lønn (A) eller direkte (B) | Normalt ikke [U] | Kostnadskonto og MVA etter kategori |
| Trekkfri diett med overnatting | Utbetales | Utgiftsgodtgjørelse, antall døgn | Reisekostnad, ingen MVA |
| Diett over trekkfri sats | Trekk og AGA | Trekkpliktig kostgodtgjørelse | Lønnskonto |
| Km-godtgjørelse innenfor 3,50 kr | Utbetales | Utgiftsgodtgjørelse, km | Bilgodtgjørelse |
| Km-godtgjørelse over 3,50 kr | Trekk og AGA | Trekkpliktig bilgodtgjørelse | Lønnskonto |
| Passasjertillegg | Utbetales | Utgiftsgodtgjørelse og passasjernavn | |
| Privat kostnad dekket (fordel) | Trekk og AGA | Fordel | |
| Firmakortkvittering | Ingen utbetaling | Ingen | Mot kortkonto |

**Låsing:** Krav godkjent etter frist går til neste periode, eller til ekstra lønnskjøring hvis kunden har slått det på. Etter `LOCKED` kommer korrigeringer. Utbetalte linjer som viser seg feil, gir aldri automatisk trekk.

### 4.4 (d) MVP eller senere

- **Må være i kjernen fra dag én:**
  - godtgjørelsesmotor (UT-40, UT-41, UT-45)
  - mapping til MVA-kode
  - bilag med vedlegg
  - § 14-15-sperre
  - API for mottak etter B1 (slik at Utleggsappen fungerer ved lansering)
- **Egen utleggsmodul ved lansering (smal):** UT-01, UT-02, UT-03, UT-06, UT-07, UT-20 og UT-21. Altså kvittering, innenlands reiseregning, kjøregodtgjørelse og godkjenning.
- **Fase 2:** utland og valuta, firmakortkobling, direkte utbetaling (vei B), utlegg for ikke-ansatte og dublettkontroll.
- **Overlates til integrasjon:** kortutstedelse og korttransaksjoner (Pleo, Folio, banker), reisebestilling og avansert reisepolicy.

### 4.5 (e) Konkurrentbilde – utlegg

| Aktør | Hva de har | Svakheter |
|---|---|---|
| **Visma Expense (Visma.net Expense)** | Reiseregning, kjørebok og utlegg. Kvitteringsapp (Visma Attach). Mye brukt i kommuner og virksomheter ([eksempel, Lom kommune](https://lom.kommune.no/tenester/politikk/for-politikarar/rettleiing-visma-expense)) [S]. Faktureres per bruker i tillegg til lønn (A 2.2) [V] | Ekstra pris per bruker. Knyttet til Visma-økosystemet. |
| **Tripletex** | «Lønn og reiseregning» til 65 kr per bruker per måned (A 3) [V] | Følger kritikken av Tripletex-lønn |
| **PowerOffice Go** | Reise til 100 kr pluss 50 kr per bruker (A 3) [V] | Holder ikke for større virksomheter (A 3) |
| **Finago** | Reise og utlegg til 29 kr per bruker (A 3) [V] | Feil ved oppstart (A 3) |
| **NettLønn People** | Reise og utlegg, app med lønnsslipp (A 2.3) [S] | Liten leverandør |
| **Pleo / Folio** | Kort først, kvittering i app, integrasjon mot regnskap. Folio er rettet mot organisasjoner og har et åpent API (v2) [K] | Diett og km med deling for a-meldingen må gjøres i lønn. De er regnskapsverktøy. |
| **Expensify** | Internasjonalt, med API [K] | Svak norsk logikk for diett og a-melding [U] |
| **Utleggsappen** | Gründerens partner og referansekontrakt B1 [U – ingen offentlig API-dokumentasjon funnet] | – |

**Muligheten [A]:**
- Prisen inkluderer utlegg, i stedet for et påslag per bruker.
- Regelmotoren for a-meldingen ligger i lønn, så regnskap og a-melding stemmer per konstruksjon.
- Vei B (direkte utbetaling av refusjoner) gir raskere utbetaling til den ansatte.

---

## 5. HR for å erstatte Huma

### 5.1 Hva Huma er (fakta per 28.10.2026)

- **Produkt:** Norsk HR-plattform for virksomheter i Norden. Moduler: personalregister og masterdata, onboarding og offboarding, fravær, automatisk import av sykmeldinger fra NAV, dokumenter og håndbøker, digitale arbeidsavtaler, medarbeidersamtaler, kompetanse, oppgaver og prosesser, utstyr, timeregistrering, lønnsadministrasjon og lønnskartlegging, rapporter, varsling, undersøkelser, avvik, GDPR og app ([humahr.com/no](https://humahr.com/no)) [V]. Huma kjører ikke lønn.
- **Størrelse:** «over 1000» kunder (egen opplysning) [V]. Smartbyrå anslår at systemet passer for 5–100 ansatte [S]. Omsetning og antall ansatte er usikre (tredjepartsprofiler uten årstall) [U].
- **Planer:** Free, Standard og Premium. **Standard** har fravær, digital signering, onboarding og offboarding, medarbeidersamtaler med maler og integrasjoner. **Premium** har i tillegg utstyrsoversikt, ubegrenset onboarding og planlegging av samtaler for alle. Prisene er ikke publisert («kontakt oss») ([Huma prisplan](https://humahr.com/no/prisplan)) [V]. Prisen starter på 49 kr per ansatt per måned ifølge Smartbyrå og gründeren ([Smartbyrå](https://smartbyra.no/vurdering/huma-hr)) [S].
- **Integrasjoner** ([Huma integrasjoner](https://humahr.com/no/integrasjon)) [V]:
  - lønn: Visma.net Payroll, PowerOffice Go, Xledger, Netvisor, Finago, Crona lön
  - regnskap: Tripletex, Fortnox, Unimicro (og DNB, SpareBank 1 og Eika Regnskap via Unimicro)
  - rekruttering: Teamtailor, Nuu
  - SSO: Google, Microsoft, Entra ID med provisjonering, Okta, Auth0, OpenID
  - NAV, Slack, eksport i PAXml, Twine Integrations

  Lønnsintegrasjonene synkroniserer **ansattdata**. Fravær til lønn er ikke beskrevet.
- **API:** Open API med OAuth2 (client credentials) ([dokumentasjon](https://openapi.humahr.com/redoc/index.html), [Huma Open API](https://humahr.com/knowledge/open-api)) [V]:
  - kan leses og skrives: ansatte (opprette og oppdatere, men ikke slette eller deaktivere), stillinger, barn, nødkontakter, ID, grupper (team, lokasjoner, selskaper) og stillingstitler
  - bare lesing: arbeidsplan, jubileer, helligdager og gjeldende lønn (krever lønnsmodulen)
  - **ikke dokumentert i API-et:** fravær, dokumenter og utstyr
- **Webhooks:** `users-*`, `user-email-update`, `positions-*`, `absence-*` og `groups-*`, inkludert `*-export` for full eksport i porsjoner på 50 ([Huma webhooks](https://humahr.com/knowledge/webhooks)) [V]:
  - Mottakeren må svare innen 1 sekund.
  - Valgfri HMAC-signatur (`huma-hmac-sha256`) og bearer-token.
  - Fraværsobjektet har status (pending, approved, rejected), type, datoer, `grade` og hvem som registrerte og godkjente. Eksportkoden fra fraværspolicyen er ikke med.

### 5.2 HR-funksjoner Brutto trenger (HR-xx)

| ID | Funksjon | Innhold | MoSCoW | Fase |
|---|---|---|---|---|
| HR-01 | **Personalregister** | Person, kontaktinfo, adresse, ID, bankkonto (endres med BankID-steg), statsborgerskap, språk, personlige felt | **Må** | Lansering (er uansett lønnsdata) |
| HR-02 | **Arbeidsforhold med historikk** | Bitemporal historikk for stilling, prosent, yrkeskode (STYRK), arbeidstidsordning, underenhet, tariff og lønn | **Må** | Lansering |
| HR-03 | **Organisasjonsstruktur og organisasjonskart** | Juridisk enhet, underenhet, avdeling, team, lokasjon, linjeleder og godkjenner. Visuelt organisasjonskart. | **Må** (data) / **Bør** (visuelt kart) | Lansering / fase 2 |
| HR-04 | **Roller og tilgang** | Leder ser sine ansatte. Delegering og stedfortreder. HR, lønn, økonomi og byrå (F 3.3) | **Må** | Lansering |
| HR-05 | **Nærmeste pårørende og barn** | Nødkontakt, barn (fødselsår) for omsorgsdager | **Må** (barn) / **Bør** (nødkontakt) | Lansering |
| HR-06 | **Personalmappe og dokumentarkiv** | Kategorier, tilgangsnivå per kategori, opplasting, versjoner, oppbevaringsregler og sletteplan (GDPR), innsynseksport. Lønnsslipper og arbeidsavtaler arkiveres automatisk. | **Må** (lett: lønnsslipp, opplastet arbeidsavtale, lese-tilgang) / **Bør** (full) | Lansering / fase 2 |
| HR-07 | **Digitale arbeidsavtaler med e-signering** | Maler som oppfyller aml. § 14-6 (17 punkter, a–q), flettefelt fra arbeidsforholdet, varsel om fristen (7 dager etter start når arbeidsforholdet varer over én måned, og straks ved kortere, § 14-5), e-signering med BankID, tillegg ved endringer, arkiv i HR-06 ([aml. § 14-5](https://lovdata.no/lov/2005-06-17-62/§14-5)) | **Bør** | Fase 2 |
| HR-08 | **Onboarding med sjekklister** | Maler per rolle. Oppgaver til HR, IT, leder og ansatt med frister regnet fra startdato. Automatiske trinn: bestille skattekort, sende arbeidsavtale, BankID-registrering av konto, utstyr og SSO-konto (SCIM). Utløses av `hr.employment.planned.v1` eller Teamtailor. | **Bør** | Fase 2 |
| HR-09 | **Offboarding med sjekklister** | Sluttdato utløser sluttoppgjør (feriepenger, avspasering, forskuddsferie), retur av utstyr, stenging av tilganger (SCIM), attest og avslutning av arbeidsforholdet i a-meldingen | **Må** (lønnsdelen) / **Bør** (sjekklister) | Lansering / fase 2 |
| HR-10 | **Medarbeidersamtaler** | Maler, planlegging for alle, forberedelse, referat, mål og oppfølging, signatur | **Bør** | Fase 2b (trengs for å matche Huma Standard) |
| HR-11 | **Utstyr** | Register, utlevert til, serienummer, retur, kobling til offboarding. Kobling til lønn for fordeler (mobil og PC som elektronisk kommunikasjon, bil) | **Kan** (register) / **Bør** (fordel i lønn) | Fase 3 |
| HR-12 | **Sykefraværsoppfølging** | Oppgaver med frister etter aml. § 4-6 (plan innen 4 uker, dialogmøte innen 7 uker), maler, dokumentasjon, varsel til leder | **Bør** | Fase 2 (kreves for å erstatte Huma) |
| HR-13 | **NAV: nærmeste leder og oppfølgingsplan** | Registrere nærmeste leder og dele plan via NAVs syfo-API-er (B 6.1) | **Kan** | Fase 2b |
| HR-14 | **Lønnsrevisjon og lønnskartlegging** | Lønnsoppgjør, plikten til likestillingsarbeid (ARP), lønnsbånd og åpenhet om lønn (G 2.2) | **Bør** | Fase 2 |
| HR-15 | **SSO og brukerprovisjonering** | OIDC/SAML og SCIM mot Entra ID, Google og Okta | **Må** (Entra SSO) / **Bør** (SCIM) | Lansering / fase 2 |
| HR-16 | **Import og migrering fra Huma** | Via Open API og webhook-eksport (5.6) | **Må** | Lansering |
| HR-17 | **API og webhooks på nivå med Huma** | Hendelser for ansatte, stillinger, grupper og fravær, slik at kundens integrasjoner bygget mot Huma kan pekes om | **Bør** | Fase 2 |
| HR-18 | **Ansattapp (selvbetjening)** | Lønnsslipp, fravær, utlegg, timer, profil. Progressiv webapp holder ved lansering. | **Må** | Lansering |
| HR-19 | **Kompetanse og sertifikater med utløpsdato** | | **Ikke nå** | Partner |
| HR-20 | **Personalhåndbok og HMS-dokumenter** | Innhold med juridisk vedlikehold | **Ikke nå** | Partner (Simployer o.l.) |
| HR-21 | **Varslingskanal (aml. kap. 2 A)** | | **Ikke nå** | Partner |
| HR-22 | **Medarbeiderundersøkelser og avvik** | | **Ikke nå** | Partner |
| HR-23 | **Jubileer og påminnelser** | | **Kan** | Fase 3 |

### 5.3 Hva bør komme før og etter lønnslanseringen? [A]

| Fase | Innhold | Hvorfor |
|---|---|---|
| **Ved lønnslansering** | HR-01–05, HR-06 (lett), HR-09 (lønnsdelen), HR-15 (SSO), HR-16 (Huma-import), HR-18 (app). **Huma-integrasjonen i sameksistens (5.4).** Egen fraværsmodul (2.4). | Alt dette trenger lønn uansett. Brutto kan lanseres til Huma-kunder uten at de må bytte HR samtidig, noe som senker terskelen. |
| **Fase 2 (3–9 mnd)** | HR-07 (arbeidsavtaler og e-signering), HR-08 og HR-09 (sjekklister), HR-12 (sykefraværsoppfølging), HR-14, HR-03 (visuelt kart), HR-06 (fullt), HR-17 | **Med dette kan Brutto erstatte Huma** for kunder som bruker fravær, arbeidsavtaler og on/offboarding, som er kjernen i Standard. |
| **Fase 2b (9–12 mnd)** | HR-10 (medarbeidersamtaler, enkel versjon), HR-13 | Full paritet med Huma Standard |
| **Fase 3 (12–18 mnd)** | HR-11 (utstyr), HR-23 | Paritet med Huma Premium |
| **Ikke nå** | HR-19–22 | Innholdstungt eller nisje. Løses med partnere. |

**Begrunnelse:** Lønn er det som vinner kunden og har høyest byttekostnad. HR er mersalg og en grunn for kunden til å bli. Kommer HR-funksjonene før lønn er stabil, blir lønnslanseringen forsinket uten at kunden får noe hun ikke allerede har i Huma. Sameksistens først og så erstatning gir også Brutto ekte data om hvilke Huma-funksjoner kundene faktisk bruker.

### 5.4 Sameksistens med Huma: integrasjonsdesign

| Data | Master i sameksistens | Retning | Mekanisme |
|---|---|---|---|
| Person, kontaktinfo, nødkontakt, barn | Huma | Huma → Brutto | Webhooks `users-*` med nattlig avstemming via Open API (`GET /users`). Webhooks må svares innen 1 sekund. Mottaket lagres derfor først og behandles etterpå. Om Huma sender på nytt etter feil er ikke dokumentert [U]. |
| Stilling, stillingsprosent, startdato, organisasjon og leder | Huma | Huma → Brutto | `positions-*`, `groups-*`. Brutto validerer mot a-meldingens regler og varsler HR om feil, for eksempel manglende yrkeskode. |
| Lønnsfelt (skattekort, bankkonto, lønnsart, sats, tariff, pensjon) | **Brutto** | Brutto → Huma (lesing) | Huma kan *lese* gjeldende lønn via egen lønnsmodul. Om Huma kan *motta* lønn, er ikke dokumentert [U]. |
| Fravær: søknad, godkjenning, kalender | Huma | Huma → Brutto | `absence-*`. Bare `approved` gir effekt på lønn. **Mapping per kunde** fra Huma-type eller policy til Brutto-type, fordi eksportkoden ikke er med i webhooken. |
| Sykmelding fra NAV | **Brutto** (kjernen må ha den for inntektsmeldingen) | NAV → Brutto | NAV-API. **Dubletter fjernes:** Hvis Huma også oppretter fravær fra samme sykmelding, kobler Brutto dem på arbeidsforhold, periode og grad, og NAV-dataene vinner. |
| Konsekvenser (AGP, refusjon, feriepenger, a-melding) | **Brutto** | Brutto → Huma: ingen | Huma-API-et har ikke dokumentert skriving av fravær eller saldo. Kunden ser konsekvensene i Brutto. |
| Feriesaldo | **Brutto** (hovedbok) | – | Hvis kunden også ser saldo i Huma, blir det to sannheter. Anbefal at saldo vises i Brutto [A]. |

**Eksportformat som reserve:** Huma kan eksportere masterdata som PAXml [V]. Brutto bør kunne importere PAXml. Det er nyttig også mot andre nordiske systemer.

### 5.5 Fraværsmodulen designet for å erstatte Humas [A]

| Funksjon hos Huma [V] | Slik må Brutto bygge det | Fase |
|---|---|---|
| Ansatt registrerer i app, leder godkjenner eller avslår, varsel til leder | FT-01–05, FT-20, push og e-post | Lansering |
| Én felles kalender som viser hvem som er på jobb | FT-21 med filter på avdeling, team og lokasjon. ICS-abonnement. | Lansering |
| Helligdager per land og lokasjon | Norge ved lansering. Helligdagskalender knyttet til lokasjon i datamodellen fra dag én, så flere land kan legges til uten migrering. | Lansering (modell) / Kan (flere land) |
| Fraværstyper og -policyer med eksportkode | Fraværstype med lønnseffekt (FT-40). **Brutto trenger ingen eksportkode, fordi lønn ligger i samme system.** | Lansering |
| Automatisk import av sykmelding fra NAV | FT-04 via NAV-API (scope `nav:helseytelser/sykepenger`, Altinn-ressursen `nav_sykepenger_sykmelding`). Kunden delegerer til Bruttos systembruker i Altinn 3. Se 6.2. | Lansering |
| Oppfølgingsprosess starter automatisk | HR-12 og FT-24: oppgaver etter § 4-6 opprettes når sykmeldingen kommer | Fase 2 |
| Sykefraværsrapporter med filter, «eksport til SSB og NAV» | FT-55: fraværsprosent egenmeldt og legemeldt, per avdeling og periode. SSB og NAV henter statistikken fra registre, så det er ingen lovpålagt innsending [U]. | Fase 2 |
| Webhooks `absence-create/update/delete/export` | `absence.*.v1` med CloudEvents og signatur, med samme livssyklusfelt (status, type, datoer, grad, registrert av, godkjent av) og i tillegg konsekvenser for lønn | Fase 2 (HR-17) |
| Ansatte i flere land | Kan. Fokus på Norge. | Senere |
| *Det Huma ikke har* | AGP, inntektsmelding, refusjon, feriepenger, ferietrekk, a-meldingens permisjon og permittering, tellere for egenmelding og omsorgsdager, feriesaldo etter ferieloven | **Fortrinnet** |

**Designregler [A]:**
1. Samme felles kjerne av felt som Huma (status, type, fra, til, grad, registrertAv, godkjentAv). Da kan historikken importeres tapsfritt.
2. Fraværstypen må stå for seg selv, uavhengig av hvordan modulen viser den. Kunden skal kunne flytte mellom Huma og Brutto i begge retninger uten å miste konsekvensene for lønn.
3. Helseopplysninger skilles fra annet fravær i tilgangsmodellen fra dag én (FT-58).
4. Ingen funksjon i fraværsmodulen bruker interne API-er. Huma, Planday eller kundens egen løsning skal kunne gjøre det samme (1.2).

### 5.6 Migrering fra Huma til Brutto (steg)

1. Kunden lager en API-nøkkel i Huma (systeminnstillinger → Open API) og gir den roller. Brutto henter ansatte, stillinger, grupper, barn, nødkontakter, stillingstitler og eventuelt gjeldende lønn.
2. Brutto registrerer et webhook-endepunkt og ber om `users-export`, `positions-export`, `groups-export` og `absence-export`. Det gir full historikk.
3. Fraværstypene mappes. Inngående saldoer (ferie, brukte egenmeldinger, omsorgsdager) hentes fra Excel eller rapport. **Huma eksponerer ikke saldoer i API-et** [U].
4. Dokumenter (arbeidsavtaler, personalmappe) har ikke dokumentert API. De må eksporteres manuelt eller som zip-fil, og lastes opp i Brutto [U].
5. **Parallellperiode:** Huma er master, og Brutto beregner og viser konsekvensene.
6. **Omleggingsdato:** Brutto blir master for fravær. Fravær i Huma fryses, og de ansatte tar i bruk Brutto-appen.
7. Senere HR-moduler (arbeidsavtalemaler, onboardingmaler) bygges opp i Brutto, og Huma sies opp.

### 5.7 Risikoer ved Huma-strategien [A]

- **Avhengighet av Huma-API-et:** Huma har en lønnsadministrasjonsmodul og lønnspartnere (Visma.net Payroll, PowerOffice). Huma kan se Brutto som konkurrent og stramme inn API-vilkårene. **Tiltak:** Adapteren bygges som en vanlig kobling bak et lag som isolerer Huma-modellen fra vår. PAXml- og CSV-import er reserve. Vilkårene for API-bruk må avklares skriftlig.
- **To sannheter for fravær og saldo i sameksistensen.** **Tiltak:** Kjernen er alltid fasit for konsekvensene, og det skal tydelig vises «saldo fra Brutto».
- **Omfanget av HR-funksjoner.** Huma har mer enn 15 moduler. Brutto skal bare dekke dem som henger sammen med lønn, pluss arbeidsavtaler, on/offboarding og samtaler. Resten løses med partnere.
- **Byrå:** Byråer har sjelden Huma for klientene, men Huma har integrasjon mot Tripletex og Unimicro. HR-funksjonene er mindre viktige for byråsegmentet.

---

# DEL 2 – Integrasjonskatalog

## 6. Katalog

### 6.1 Prioriteter, retning og mønstre

**Prioritet**
- **MVP:** klar ved lansering
- **Fase 2:** 3–9 måneder etter lansering
- **Senere:** 9–24 måneder, styrt av etterspørsel
- **Vurder:** usikker verdi eller usikkert API; må undersøkes
- **Ikke nå**

**Retning:** «→» betyr fra Brutto til systemet. «←» betyr inn i Brutto. «↔» betyr begge veier.

**Integrasjonsmønstre**
- **N:** Brutto bygger og drifter adapteren selv
- **P:** partneren bygger mot Bruttos offentlige API, etter prinsippet om like vilkår
- **F:** fil eller CSV med mal
- **U:** via en «unified API»-leverandør

**API-merking:** «Ja [V]» betyr at offentlig dokumentasjon er funnet og sjekket. «Ja [K]» betyr kjent, men ikke sjekket i denne runden. «[U]» betyr at ingen offentlig dokumentasjon er funnet.

**Hovedregel [A]:** Ved lansering bygger vi selv bare integrasjoner mot myndigheter, bank, de tre viktigste regnskapssystemene og fire økosystempartnere (Huma, Planday, Utleggsappen og identitet). Alt annet dekkes av fil eller CSV med maler, eller ved at partnere bygger mot vårt API.

### 6.2 Myndigheter

| System | Hva utveksles | Retning | Prioritet | Begrunnelse | Åpent API |
|---|---|---|---|---|---|
| Skatteetaten – a-melding | A-melding, tilbakemelding, avstemmingsdata | ↔ | **MVP** | Lovpålagt. Fra 2026 er API eneste vei fra system (B 2, G B8). | Ja [V]: [a-meldingen SBS](https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/a-meldingen-sbs/) |
| Skatteetaten – skattekort | Bestilling, henting, endringer | ↔ | **MVP** | Lovpålagt | Ja [V]: [skattekort SBS](https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/skattekort-sbs/) |
| Skatteetaten – trekkpålegg | Pålegg om utleggstrekk, endringer, samordnet utleggstrekk med KID | ← | **MVP** | Nye regler fra 2026 (C 0) | Ja [V]: [LPS-info](https://www.skatteetaten.no/om-skatteetaten/fremtidens-innkreving/systemleverandorer/lonns--og-personalsystem/) |
| Skatteetaten – skatte- og avgiftsopplysninger | Krav og innbetalinger (forskuddstrekk, AGA, utleggstrekk) til avstemming | ← | Fase 2 | Leverandører kan hente dette via API (Skatteetaten). Ved lansering avstemmes det manuelt. | Ja [S]: samme side |
| Skatteetaten – trekkrutine | Offisiell beregning av tabelltrekk (Java) | intern | **MVP** | Skal ikke lages på nytt (C 0) | Ja [V]: [GitHub](https://github.com/Skatteetaten/trekktabell) |
| NAV – sykepenger (inntektsmelding, forespørsel, sykmelding, søknad, PDF) | ← sykmelding, søknad, forespørsel · → inntektsmelding med refusjon | ↔ | **MVP** | Grunnlaget for refusjon og AGP. Sykmeldingen gir Huma-paritet (FT-04). | Ja [V]: [wiki](https://github.com/navikt/sykepenger-im-lps-api/wiki), [swagger](https://sykepenger-api.nav.no/swagger) |
| NAV – inntektsmelding for foreldre- og svangerskapspenger | → inntektsmelding og refusjonskrav | → | **MVP** | Vanlig refusjon. Oppført i produksjon, men NAVs arbeidsgiverside sier noe annet (B 6.1) [U]. | Ja [V]: [wiki](https://github.com/navikt/fp-inntektsmelding-api/wiki) |
| NAV – sykdom i familien (omsorgs-, pleie- og opplæringspenger) | → inntektsmelding og refusjonskrav for omsorgspenger | → | Fase 2 | NAV krever Min side fra 21.5.2026. Om API-et gjelder, må avklares [U]. | Ja [V]: [wiki](https://github.com/navikt/k9-inntektsmelding-api/wiki) |
| NAV – oppgjørsrapporter | ← utbetalte refusjoner | ← | Fase 2 | Avstemming av refusjon (manuelt ved lansering) | Ja [V]: [wiki](https://github.com/navikt/sokos-oppgjorsrapporter/wiki) |
| NAV – syfo (dokumentporten, oppfølgingsplan, nærmeste leder) | ↔ dokumenter og plan, → nærmeste leder | ↔ | Fase 2 | HR-12 og HR-13 | Ja [V]: [wiki](https://github.com/navikt/syfo-dokumentporten/wiki) |
| NAV – Aa-registeret | ← arbeidsforhold slik NAV ser dem | ← | Senere | Avstemming og kontroll | Ja [V]: [aareg](https://navikt.github.io/aareg/) |
| NAV – permittering og masseoppsigelse | – | – | Ikke integrasjon | Skjema på nav.no, ikke API (B 6.3). Brutto lager brev og sjekkliste. | Nei [V] |
| Altinn 3 (systembruker, klientsystem, tilgangspakker, Dialogporten, Events) | Autorisasjon, delegering, varsler | ↔ | **MVP** | Grunnmur. Byråer trenger systembruker for klientsystem (B 1). | Ja [K]: [docs.altinn.studio](https://docs.altinn.studio/) |
| Maskinporten | Tokens | → | **MVP** | Grunnmur | Ja [K]: [Digdir](https://docs.digdir.no/docs/Maskinporten/) |
| Brreg – Enhetsregisteret | ← enheter, underenheter, adresse og kommune (AGA-sone), organisasjonsform | ← | **MVP** | Kundeoppstart, underenheter og AGA-sone | Ja [K]: [API-dokumentasjon](https://data.brreg.no/enhetsregisteret/api/docs/index.html) |
| SSB – Klass | ← kodelister for yrke (STYRK-08), kommune og næring | ← | **MVP** | Yrkeskode i a-meldingen og validering | Ja [K]: [Klass API](https://data.ssb.no/api/klass/v1/) |
| SSB – statistikk | – | – | Ikke nå | Lønnsstatistikken bygger på a-meldingen. Ingen egen innsending [K]. | – |
| SPK | → medlemsdata (lønn, stilling, permisjon), månedlig | → | Vurder / fase 2 | Bare virksomheter med SPK-ordning (noen stiftelser). Krever SPK-godkjent lønnssystem. Kravspesifikasjonen er fra 2014 [S]. | Spesifikasjon [S]: [SPK v2.2](https://www.spk.no/globalassets/virksomhet/kravspesifikasjon-v.2.2.pdf) |
| KLP | → ansattopplysninger | → | Fase 2 | Virke HUK og ideelle med offentlig tjenestepensjon (D 5.3) | Fil eller portal [V]: [KLP](https://www.klp.no/virksomhet/pensjon/hr-lonn-og-personal/rapportering-av-ansattopplysninger) |
| Arbeidstilsynet | – | – | Ikke integrasjon | Rapporten etter § 10-7 eksporteres ved behov | – |

### 6.3 Bank og betaling

| System | Hva utveksles | Retning | Prioritet | Begrunnelse | Åpent API |
|---|---|---|---|---|---|
| ISO 20022-fil (pain.001 / pain.002 / camt.054) | Nettolønn, trekk med KID, status og avregning | ↔ | **MVP** | Virker mot alle banker, og byråer bruker klientens bank (D 5.3). Nordea validerer betalingsfiler etter hvitvaskingsloven fra 9.9.2026, så formatet må følges presist (D 5.2). | Standard [K] |
| Betaling av forskuddstrekk, AGA og utleggstrekk med KID | Betalinger med KID, første virkedag etter lønnsutbetaling | → | **MVP** | Regler fra 2026 (C 0) | Inngår i bankfilen |
| Multibank-kanal (Mastercard Payment Services Direkte remittering, Zdata, Aritma) | pain.001 og kvitteringer mot mange banker via én avtale | ↔ | **Vurder for MVP** | Kan gi direkte bankintegrasjon fra dag én uten en avtale med hver bank. Velg én. | Mastercard [V]: [Direkte remittering](https://www.mastercard.com/no/nb/business/payments/commercial-payments/mastercard-payment-services-avdelingsside/mastercard-direkte-remittering/mastercard-direkt-remittering-produktside.html) · Zdata og Aritma [U] |
| DNB | Betalingsoppdrag, status, kontoinformasjon | ↔ | Fase 2 | Størst i bedriftsmarkedet | Ja [K]: [developer.dnb.no](https://developer.dnb.no/) |
| Nordea | Samme | ↔ | Fase 2 | | Ja [K]: [Nordea](https://developer.nordeaopenbanking.com/) |
| SpareBank 1 | Samme | ↔ | Fase 2 | Mange SMB-er og organisasjoner | Ja [K]: [SpareBank 1](https://developer.sparebank1.no/) |
| Handelsbanken | Samme | ↔ | Senere | | Ja [K]: [Handelsbanken](https://developer.handelsbanken.com/) |
| Danske Bank | Samme | ↔ | Senere | | Ja [K]: [Danske Bank](https://developers.danskebank.com/) |
| Folio | → utbetalinger · ← konto og hendelser | ↔ | Fase 2 | Utbredt hos foreninger og organisasjoner. Har API for utgående betalinger. | Ja [V]: [api.folio.no/v2](https://api.folio.no/v2/api.yml) |
| Vipps MobilePay | Vipps Login (identitet). Utbetalinger til ikke-ansatte, som honorar og frivilliges utlegg. | ↔ | Vurder | Om det finnes utbetalings-API for dette, er usikkert [U] | Ja [K]: [developer.vippsmobilepay.com](https://developer.vippsmobilepay.com/) |
| Straksbetaling (NICS Real) | Umiddelbar lønn og refusjon | → | Vurder | Støtten for straks i bulk varierer mellom bankene (G B5) [U] | – |

### 6.4 Regnskap og ERP

Alle får samme interne bilagskontrakt (G, B4) med én adapter per system.

| System | Hva utveksles | Retning | Prioritet | Begrunnelse | Åpent API |
|---|---|---|---|---|---|
| Tripletex | → lønnsbilag med dimensjoner og vedlegg · ← kontoplan, avdelinger, prosjekter · (fase 2) ← timer | ↔ | **MVP** | Mest brukt av byråer og små kunder (A 3; 150 000 kunder) | Ja [K]: [v2-docs](https://tripletex.no/v2-docs/) |
| PowerOffice Go | Samme | ↔ | **MVP** | Byråer og SMB, sterk kobling mellom byrå og klient (A 3) | Ja [K]: [developer.poweroffice.net](https://developer.poweroffice.net/) |
| Xledger | Samme | ↔ | **MVP** | Stiftelser, organisasjoner og mellomstore. Anbudskrav om direkte kommunikasjon (Ferde, D 5.2). Huma har også integrasjon mot Xledger. | GraphQL [S]: xledger.net/graphql ([ConnectMyApps-guide](https://connectmyapps.atlassian.net/wiki/x/OwC9DQ)) |
| Fiken | Samme | ↔ | Fase 2 | Små foreninger og bedrifter, ofte under 10 ansatte | Ja [K]: [api.fiken.no](https://api.fiken.no/api/v2/docs/) |
| Visma Business NXT | Samme | ↔ | Fase 2 | Mellomstore. Overgang fra Visma Business. | Ja [K]: [docs.business.visma.net](https://docs.business.visma.net/) |
| Visma.net ERP | Samme | ↔ | Fase 2 | Mellomstore | Ja [K]: [integration.visma.net](https://integration.visma.net/API-index/) |
| Visma eAccounting (eRegnskap) | Samme | ↔ | Senere | Mikro | Ja [K]: [developer.vismaonline.com](https://developer.vismaonline.com/) |
| 24SevenOffice / Finago | Samme | ↔ | Fase 2 | Byråer | Ja [K]: [developer.24sevenoffice.com](https://developer.24sevenoffice.com/) |
| Uni Micro (og DNB, SpareBank 1 og Eika Regnskap) | Samme | ↔ | Fase 2 | Regnskap distribuert via bankene til SMB | [U] |
| Microsoft Dynamics 365 Business Central | Samme | ↔ | Fase 2 | Mellomstore med Microsoft-partnere (D 5.1) | Ja [K]: [API v2.0](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/) |
| Unit4 ERP | Samme, fil ved lansering | ↔ | Senere | 250–1000 ansatte, forskningsinstitutter (NORCE, Tensio, D 5.2) | [U] |
| Conta | Samme | ↔ | Vurder | Mikro | [U] |
| Duett | Samme | ↔ | Vurder | Har egen lønn, så de er konkurrent | [U] |
| Generisk bilagsfil (CSV, SAF-T-lignende) | → bilag | → | **MVP** | Reserveløsning for alle andre | – |

### 6.5 Tid og vakt

| System | Hva utveksles | Retning | Prioritet | Begrunnelse | Åpent API |
|---|---|---|---|---|---|
| Planday | ← godkjente timer og tillegg, fravær og saldo · → ansatte og arbeidsforhold, eventuelt satser | ↔ | **MVP** | Mye brukt i varehandel og service. Offentlig API for timelister, fravær, lønn og HR. Viser at modulbytte virker (1.2). | Ja [V]: [openapi.planday.com](https://openapi.planday.com/) |
| Tamigo | ← timer og tillegg | ← | Fase 2 (CSV ved lansering) | Kjeder i varehandel | [U] |
| Quinyx | ← timer og tillegg | ← | Fase 2 (CSV ved lansering) | Kjeder og enterprise | Ja [V]: [developer.quinyx.com](https://developer.quinyx.com/) |
| Visma Enterprise Tid / GAT | ← timer og turnus | ← | Senere (fil) | Helse og ideelle i helse | [U] lukket |
| MinTid | ← timer | ← | Vurder | | [U] |
| Timely | ← prosjekttimer | ← | Senere | Konsulenter og byråer | Ja [K]: [dev.timelyapp.com](https://dev.timelyapp.com/) |
| Harvest | ← prosjekttimer | ← | Senere | | Ja [K]: [Harvest API v2](https://help.getharvest.com/api-v2/) |
| Tripletex timer | ← timer og prosjekt | ← | Fase 2 | Kunder som har prosjekt i Tripletex og lønn i Brutto | Ja [K]: [v2-docs](https://tripletex.no/v2-docs/) |
| Tikket (registrering ved arrangementer) | ← timer for bemanning på arrangementer (B3) | ← | Fase 2 | Gründernevnt partner, se 6.9 | [U] |
| Generisk CSV-mal for timer | ← timer | ← | **MVP** | Dekker alle andre fra dag én (TI-44) | – |

### 6.6 HR og HRM

| System | Hva utveksles | Retning | Prioritet | Begrunnelse | Åpent API |
|---|---|---|---|---|---|
| **Huma** | ← personer, stillinger, grupper (organisasjon og leder), barn, nødkontakter, fravær (webhooks) · migrering via eksport | ← (↔ ved behov) | **MVP** | Gründerkrav. Sameksistens først, deretter erstatning (kap. 5). Over 1000 norske kunder. Integrerer allerede med Visma.net Payroll og PowerOffice, så kundene er vant til at lønn ligger et annet sted. | Ja [V]: [Open API](https://openapi.humahr.com/redoc/index.html), [webhooks](https://humahr.com/knowledge/webhooks) |
| Simployer | ← ansatt og organisasjon · → lønnsnøkkeltall? | ← | Fase 2 | Over 12 000 kunder i Norden. Integrerer mot Visma, Tripletex og PowerOffice (A 3). | [U] |
| Sympa | ← ansatt og organisasjon | ← | Senere | Mellomstore og store | [U] |
| HiBob | ← ansatt og organisasjon | ← | Senere | Internasjonale teknologiselskaper med avdeling i Norge | Ja [K]: [apidocs.hibob.com](https://apidocs.hibob.com/) |
| Personio | ← ansatt og organisasjon | ← | Senere | | Ja [K]: [developer.personio.de](https://developer.personio.de/) |
| Workday | ← ansatt og organisasjon | ← | Vurder | Over 1000 ansatte og internasjonale. Partnerløp. | Partner [K] |
| CatalystOne | ← ansatt og organisasjon | ← | Senere | | [U] |
| Talentech | ← kandidat ansatt (pre-hire) | ← | Vurder | Eierskiftet med Simployer gjør veikartet uklart (A 3) | [U] |
| Teamtailor | ← kandidat ansatt, som starter onboarding (HR-08) | ← | Fase 2 | Huma har også denne koblingen | Ja [K]: [docs.teamtailor.com](https://docs.teamtailor.com/) |
| PAXml (format) | ← masterdata | ← | **MVP** (import) | Nordisk eksportformat, også fra Huma | Standard [K] |

### 6.7 Reise, utlegg og kort

| System | Hva utveksles | Retning | Prioritet | Begrunnelse | Åpent API |
|---|---|---|---|---|---|
| **Utleggsappen** | ← godkjente krav og reiseregninger (fakta og forslag) · → status, utbetalt, rapportert | ↔ | **MVP** | Gründerens referansekontrakt B1. Beviser at «egen modul kan byttes ut». | [U] Ingen offentlig dokumentasjon funnet |
| Pleo | ← refusjonskrav for utlegg (ikke kort) · → status | ↔ | Fase 2 | Utbredt hos SMB | Ja [K]: [developers.pleo.io](https://developers.pleo.io/) |
| Folio (kort og utlegg) | ← utlegg til refusjon, kvitteringer | ← | Fase 2 | Organisasjoner | Ja [V]: [api.folio.no/v2](https://api.folio.no/v2/api.yml) |
| Expensify | ← refusjonskrav | ← | Senere | Internasjonale | Ja [K]: [Integration Server](https://integrations.expensify.com/Integration-Server/doc/) |
| Visma Expense | ← historikk ved migrering | ← | Vurder | Kunder som går fra Visma vil ha med historikken | [U] lukket |
| Eurocard (SEB Kort) | ← transaksjonsfil | ← | Senere | Firmakort hører mest til regnskapet | [U] |
| American Express Corporate | ← transaksjonsfil | ← | Senere | | [U] |
| Mastercard Corporate (kort utstedt av bank) | ← transaksjoner | ← | Senere | | [U] |

### 6.8 Organisasjon og medlem

| System | Hva utveksles | Retning | Prioritet | Begrunnelse | Åpent API |
|---|---|---|---|---|---|
| OrgLab (medlemshåndtering, Cornerstone-type) | ← verv og tillitsvalgte (blir honorarmottakere), organisasjonsstruktur (B2) · → honorar utbetalt | ↔ | Fase 2 | Gründernevnt. Viktig for organisasjoner: styre- og vervhonorar, akkumulator for skattefrie organisasjoner (D 7) | [U] |
| Hypersys | Samme | ↔ | Vurder | Medlemssystem for organisasjoner | [U] |
| NIF / idrettens systemer (KlubbAdmin, MinIdrett) | ← trenere og dommere som får honorar | ← | Vurder | Mange honorarmottakere, få ansatte | [U] |
| Fagforeninger (kontingenttrekk) | → trekklister og innbetaling per forbund | → | Fase 2 | Tariffbundne kunder. Trekket har hjemmel i tariffavtale (aml. § 14-15). | Fil per forbund [U] |

### 6.9 Arrangement

| System | Hva utveksles | Retning | Prioritet | Begrunnelse | Åpent API |
|---|---|---|---|---|---|
| Tikket | ← timer for arrangementsbemanning (B3), honorar til artister og frivillige | ← | Fase 2 | Gründernevnt. Relevant for festivaler og kulturorganisasjoner. | [U] |
| Checkin | Samme | ← | Senere | | [U] |
| Hoopla | Samme | ← | Senere | | [U] |
| TicketCo | Samme | ← | Senere | | [U] |

### 6.10 Pensjon og forsikring

| System | Hva utveksles | Retning | Prioritet | Begrunnelse | Åpent API |
|---|---|---|---|---|---|
| OTP-leverandører (Storebrand, DNB, Gjensidige, Nordea Liv, KLP Bedrift m.fl.) | → pensjonsgrunnlag, pensjonsinnretning og ordning i a-meldingen · ← ordning og satser (manuelt) | → | **MVP (via a-meldingen)** | Leverandørene henter fra a-ordningen (G B6). Riktige a-meldingsfelt er hele integrasjonen ved lansering. | Via a-ordningen [V] |
| Storebrand, DNB m.fl. – ordningsdata | ← satser, inn- og utmelding | ← | Senere | Forsikringer må oppdateres manuelt (DNB, D 5.2) | [U] |
| KLP (offentlig tjenestepensjon) | → ansattopplysninger | → | Fase 2 | HUK og ideelle | Se 6.2 |
| SPK | → medlemsdata | → | Vurder | Se 6.2 | Se 6.2 |
| Tryg, If, Fremtind, Gjensidige (yrkesskade, gruppeliv) | → årlig lønnssum og antall årsverk | → | Senere (rapport) | Premiegrunnlag | [U] |

### 6.11 Identitet og signering

| System | Hva utveksles | Retning | Prioritet | Begrunnelse | Åpent API |
|---|---|---|---|---|---|
| BankID (via megler) | Innlogging, sterk bekreftelse ved endring av kontonummer, innsyn for sluttede | ↔ | **MVP** | Sikkerhet og tillit (F 4.8) | Ja [K]: [developer.bankid.no](https://developer.bankid.no/) |
| Signicat | BankID-megler og e-signering | ↔ | **MVP** (velg én megler) | Samme leverandør for innlogging og arbeidsavtaler (HR-07) | Ja [K]: [developer.signicat.com](https://developer.signicat.com/) |
| Criipto | Alternativ megler | ↔ | Vurder | Pris og enkelhet | Ja [K]: [docs.criipto.com](https://docs.criipto.com/) |
| ID-porten | Innlogging | ↔ | Vurder | Brukes normalt av offentlige tjenester. Om private SaaS-tjenester kan få tilgang, er usikkert [U]. | Ja [K]: [docs.digdir.no](https://docs.digdir.no/) |
| Microsoft Entra ID | OIDC-SSO · SCIM-provisjonering | ↔ | **MVP** (SSO) / Fase 2 (SCIM) | Kunder med over 50 ansatte og byråene selv (D 5.3) | Ja [K]: [SCIM](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups) |
| Google Workspace | OIDC · katalog | ↔ | Fase 2 | | Ja [K] |
| Okta | OIDC/SAML · SCIM | ↔ | Fase 2 | | Ja [K]: [developer.okta.com](https://developer.okta.com/) |
| Penneo | E-signering | → | Vurder | Populært hos revisorer og byråer | [U] |
| Scrive | E-signering | → | Vurder | | Ja [K]: [apidocs.scrive.com](https://apidocs.scrive.com/) |
| Verified | E-signering | → | Vurder | | [U] |
| Vipps Login | Innlogging for ansatte og ikke-ansatte | ↔ | Vurder | Enkelt for frivillige (UT-10) | Ja [K] |

### 6.12 Digital post og kommunikasjon

| System | Hva utveksles | Retning | Prioritet | Begrunnelse | Åpent API |
|---|---|---|---|---|---|
| Push og e-post fra Bruttos app | Varsler (ikke lønnsslipp-PDF med persondata i e-post) | → | **MVP** | Selvbetjening (HR-18) | – |
| Digipost | → lønnsslipp og årsoppgave | → | Fase 2 | Konkurrentene har det (SD Worx, Visma), men egen app dekker behovet ved lansering | Ja [V]: [Digipost API](https://digipost-docs.readthedocs.io/en/latest/api/introduction.html) |
| e-Boks | → lønnsslipp | → | Senere | Den andre godkjente digitale postkassen ([norge.no](https://www.norge.no/en/node/83375)), men har mindre andel [K] | Ja [K] |
| SMS (Link Mobility, Sveve m.fl.) | → varsler, engangskoder | → | Fase 2 | Ansatte uten app, for eksempel ekstrahjelp | Ja [K] |
| Slack | → godkjenningsoppgaver, «hvem er borte» · ← godkjenning med knapp | ↔ | Fase 2 | Huma har det | Ja [K]: [api.slack.com](https://api.slack.com/) |
| Microsoft Teams | Samme | ↔ | Fase 2 | Mange norske SMB-er bruker Microsoft 365 | Ja [K]: Microsoft Graph |

### 6.13 Kalender

| System | Hva utveksles | Retning | Prioritet | Begrunnelse | Åpent API |
|---|---|---|---|---|---|
| ICS-feed (abonnement) | → ferie og fravær, personlig og for teamet | → | **MVP** | Nesten gratis å lage. Virker i alle kalendere. | Standard |
| Outlook (Microsoft Graph) | → hendelser i kalenderen | → | Fase 2 | Krever tilgang til postkassen. Hold det utenfor MVP av sikkerhetshensyn. | Ja [K] |
| Google Calendar | → hendelser i kalenderen | → | Fase 2 | | Ja [K] |

### 6.14 Praksissystemer for regnskapsbyråer

| System | Hva utveksles | Retning | Prioritet | Begrunnelse | Åpent API |
|---|---|---|---|---|---|
| Bruttos byrå-API og webhooks (status per klient) | → status for lønnskjøring, a-melding sendt og godkjent, frister, antall lønnsslipper (fakturagrunnlag) | → | **MVP** (som API, ikke som adapter) | Alle praksissystemer kan hente status. Det er grunnlaget for byråsegmentet (E). | Vårt eget |
| Tally | ← klientliste · → status, frister, fakturagrunnlag | ↔ | Fase 2 | Praksissystem for byråer. Har MCP-server (observert i dette miljøet). | [U] REST, MCP finnes |
| Maestro | Samme | ↔ | Vurder | | [U] |
| Duett | Samme | ↔ | Vurder | Har også egen lønn | [U] |
| «Visma Practice» | Samme | ↔ | Vurder | Ikke entydig identifisert. Kan være Visma sitt praksisverktøy for byråer [U]. | [U] |
| Kontaktnett | – | – | Vurder | Ikke identifisert i denne runden [U] | [U] |

### 6.15 BI og data

| System | Hva utveksles | Retning | Prioritet | Begrunnelse | Åpent API |
|---|---|---|---|---|---|
| Excel og CSV-eksport | → alle rapporter og rådata | → | **MVP** | Kundene vil ha rådata (D 5.2) | – |
| Power BI (OData eller REST) | → lønnsdata etter tilgangspakke | → | Fase 2 | Må-krav for 250–1000 (D 5.3) | Vårt API |
| Google Sheets | → rapporter | → | Senere | | – |
| Datavarehus (Parquet på S3, Snowflake, BigQuery, Fabric) | → hendelser og rådata | → | Senere | Store kunder og konsern | – |

### 6.16 Unified API-leverandører

| Leverandør | Rolle for Brutto | Prioritet | Begrunnelse | API |
|---|---|---|---|---|
| Kombo | **Bli listet som kilde**, slik at HR- og fordelsapper får tak i Bruttos data | Fase 2 | EU-fokus og stor dekning av HR og lønn. Ikke for å *hente* data selv. | [docs.kombo.dev](https://docs.kombo.dev/) [V] |
| Apideck | Bli listet | Senere | Har norske HR-systemer «på radaren» | [Norway HRIS](https://www.apideck.com/integrations/country/norway/hris) [V] |
| Merge | Bli listet | Senere | USA-tung | [docs.merge.dev](https://docs.merge.dev/) [K] |
| Finch | – | Ikke nå | Lønn i USA | [developer.tryfinch.com](https://developer.tryfinch.com/) [K] |

### 6.17 KI og agenter

| System | Hva utveksles | Retning | Prioritet | Begrunnelse | Åpent API |
|---|---|---|---|---|---|
| Bruttos MCP-server | Lesing: status, avvik, saldoer, forklaringer. Skriving: bare *utkast* som et menneske godkjenner. Tilgangsomfang per tilgangspakke (G 1.9). | ↔ | Fase 2 | API-first gjør MCP til et tynt lag. Byråer og KI-agenter (G 2.4). KI skal ikke beregne lønn (F 5.2). | [modelcontextprotocol.io](https://modelcontextprotocol.io/) [K] |
| Eksterne MCP-er (Tripletex, PowerOffice, Tally) | Agentflyt på tvers av systemer | ↔ | Vurder | Markedet beveger seg. Det finnes MCP-servere for Tripletex, PowerOffice og Tally (observert). | – |

---

## 7. Topp 15 integrasjoner for lansering

●●● kritisk · ●● viktig · ● nyttig · – lite relevant

| # | Integrasjon | Direkte 30–300 | Byrå | Organisasjon/stiftelse | Hvorfor ved lansering |
|---|---|---|---|---|---|
| 1 | **Skatteetaten a-melding** (innsending, tilbakemelding, avstemming) | ●●● | ●●● | ●●● | Lovpålagt. Uten den er det ikke noe produkt. |
| 2 | **Skatteetaten skattekort** | ●●● | ●●● | ●●● | Lovpålagt. Byråer trenger masseoperasjoner. |
| 3 | **Skatteetaten trekkpålegg og KID-betaling** | ●●● | ●●● | ●●● | 2026-reglene: samordnet utleggstrekk og betaling første virkedag. |
| 4 | **NAV sykepenge-API** (inntektsmelding, forespørsel, sykmelding, søknad) | ●●● | ●●● | ●●● | Refusjon og AGP. Sykmelding gir Huma-paritet uten ekstra tilgang. |
| 5 | **NAV inntektsmelding for foreldre- og svangerskapspenger** | ●● | ●●● | ●●● | Vanlig refusjon. Organisasjoner betaler ofte full lønn i permisjon. |
| 6 | **Altinn 3 og Maskinporten** (systembruker og klientsystem) | ●●● | ●●● | ●●● | Grunnmur for 1–5. Uten klientsystem kan ikke byråer bruke Brutto. |
| 7 | **Brreg Enhetsregisteret og SSB Klass** (referansedata) | ●● | ●●● | ●● | Oppstart, underenheter, AGA-sone og yrkeskode med svært lite arbeid. |
| 8 | **Bank: ISO 20022-fil og én multibank-kanal** | ●●● | ●●● | ●●● | Lønn må ut. Filen virker mot alle banker, og multibank-kanalen gir direkte flyt. |
| 9 | **Tripletex** | ●● | ●●● | ●● | Byråenes mest brukte. Mange SMB-er. |
| 10 | **PowerOffice Go** | ●● | ●●● | ●● | Byråer og samarbeid mellom byrå og klient |
| 11 | **Xledger** | ●● | ● | ●●● | Stiftelser og organisasjoner. Anbudskrav. |
| 12 | **Huma** | ●●● | ● | ●● | Gründerkrav. Sameksistens senker byttekostnaden. Veien til å erstatte Huma. |
| 13 | **Planday** | ●● | ● | ●● | Timelønte i service og arrangement. Viser i praksis at modulen kan byttes ut. |
| 14 | **Utleggsappen** | ●● | ●● | ●● | Referansekontrakt B1. Viser at egen utleggsmodul kan byttes ut. |
| 15 | **Identitet: BankID via megler (Signicat eller Criipto) og Entra ID-SSO** | ●●● | ●● | ●● | Sikker kontoendring, innlogging for ansatte, SSO for 50+ og byråene selv |

**Det som ikke kom med, og hvorfor [A]:**
- **Fiken, Visma Business NXT og Business Central:** Generisk bilagsfil holder ved lansering. Adapter kommer i fase 2 når det er etterspørsel.
- **KLP:** viktig for HUK-organisasjoner, men kvartalsvis rapportering kan gjøres med fil de første månedene.
- **Digipost:** egen app dekker behovet.
- **Simployer:** fase 2. Huma prioriteres etter gründerkrav.
- **Quinyx og Tamigo:** CSV-mal ved lansering.
- **Slack og Teams:** fine å ha.
- **Kombo:** distribusjon, ikke lansering.
- **OrgLab og Tikket:** ikke verifisert API. Krever partnerarbeid.

---

## 8. Hvor vi ikke skal bygge det kunden allerede har [A]

| Kunden har ofte | Brutto gjør |
|---|---|
| Vaktplan, turnus, stempelklokke (Planday, Tamigo, Quinyx, GAT) | Importerer timer og fravær. Ingen egen vaktplan. |
| Firmakort og kortapp (Pleo, Folio, bankkort) | Tar imot refusjonskrav og kobler kvitteringer i fase 2. Ingen kortutstedelse. |
| Personalhåndbok, HMS, varsling, kompetanse (Simployer, Huma) | Partnere. Bare HR som henger sammen med lønn, pluss arbeidsavtaler, on/offboarding og samtaler. |
| Kalender (Outlook, Google) | ICS-feed. Ingen egen kalender. |
| E-signering og OCR | Kjøpes som tjeneste (Signicat og en OCR-leverandør) |
| BI-verktøy | Eksport, OData og API. Ingen egen BI-motor. |
| Reisebestilling | Ikke nå |

---

## 9. Runde B: Hva jeg endret og hvorfor

| # | Runde A (utkast) | Runde B (revidert) | Hvorfor |
|---|---|---|---|
| 1 | Standard egenmelding «IA: 8 dager per tilfelle / 24 per 12 måneder» | Lovens minimum (3 kalenderdager per tilfelle, etter 2 måneders ansettelse) er standard. Utvidet ordning er en policy som krever registrert drøfting. | **Juridisk feil.** Ftrl. § 8-24. IA-avtalen 2019–2024 gikk ut, og IA-avtalen 2025–2028 gir ingen rett. Ingen lovendring for 2026 funnet. |
| 2 | «Retten bortfaller etter 4 egenmeldinger» | Arbeidsgiver *kan* frata retten etter minst 4 tilfeller. Arbeidstaker skal få uttale seg, og vedtaket vurderes på nytt etter 6 måneder. Systemet varsler, men fratar ikke automatisk. | **Juridisk feil** (§ 8-27) |
| 3 | 6G-tak på feriepengegrunnlaget | Taket gjelder bare 60+-tillegget på 2,3 prosentpoeng | **Juridisk feil** (ferieloven § 10, C 3.1) |
| 4 | Alt fravær rapporteres som permisjon i a-meldingen | Bare permisjon over 14 dager er pliktig. Permittering rapporteres alltid. Sykefravær under 12 måneder og sykt barn rapporteres ikke. | **Juridisk feil** (Skatteetaten) |
| 5 | Arbeidstidsregistrering bare for timelønte | § 10-7 gjelder alle unntatt § 10-12. Ved lansering: fast plan med avvik og rapport. Timer per dag for timelønte etter bokføringsforskriften § 5-6. | **Juridisk feil** |
| 6 | Overtidsgrenser «10 t per uke, 200 t per år» | Hele settet: 10/25/200, tariffavtale 20/50/300, Arbeidstilsynet 25 og 200 per 26 uker, samlet 13 t og 48 t (69 t i én uke), minst 40 % tillegg | **Ufullstendig** (§ 10-6) |
| 7 | Avspasering som fritt valg for den ansatte | Krever skriftlig avtale. Tillegget utbetales. | **Juridisk** (§ 10-6 tolvte ledd) |
| 8 | Fradrag for inngående MVA på alle utlegg med kvittering | MVA-kode bestemmes av kategorien. Ikke fradrag for servering, representasjon, kost til ansatte, gaver og personbil. | **Juridisk feil** (mval. §§ 8-3 og 8-4) |
| 9 | Utleggskravet trenger bare kvittering | Formål, arrangement, datert og signert oppstilling. Arbeidsgiver som kjøper ved over 1 000 kr for innsatsfaktor. Deltakere ved bevertning. Passasjernavn. | **Juridisk** (bokføringsforskriften §§ 5-5-1, 5-9, 5-10, Skatteetaten) |
| 10 | Automatisk trekk ved negative korrigeringer (fravær, utlegg, timer) | Stopp med `REQUIRES_WRITTEN_AGREEMENT` | **Juridisk** (aml. § 14-15, HR-2021-2532-A) |
| 11 | Sykmeldingsimport fra NAV i fase 2 | Flyttet til **MVP** | Samme tilgang og pakke som inntektsmeldingen, som uansett må bygges. Kreves for Huma-paritet. |
| 12 | Inntektsmelding og refusjon for omsorgspenger ved lansering | Flyttet til **fase 2** | NAV sier at Min side gjelder fra 21.5.2026. Statusen for LPS-API-et er uklar. |
| 13 | Egen timemodul med turnus og vaktplan og stempelklokke | Fjernet. Smal timeliste og overtid ved lansering. Prosjekttid i fase 2. | **For mye for MVP** og **bygger noe kunden har** (Planday m.fl.) |
| 14 | Utleggsmodul med firmakort, utland og direkte utbetaling ved lansering | Innenlands reise, km og kvittering ved lansering. Resten i fase 2. | **For mye for MVP.** Kort hører til regnskapet. |
| 15 | Full sykefraværsoppfølging, medarbeidersamtaler og utstyr ved lansering | Fase 2, 2b og 3. Sameksistens med Huma ved lansering. | **For mye for MVP.** Forsinker lønn, som er det som vinner kunden. |
| 16 | 28 integrasjoner i MVP (inkludert Fiken, Visma NXT, Digipost, e-Boks, Slack, Teams, Google, Okta, KLP) | 15 i MVP. Resten via fil eller CSV, eller i fase 2. | **For mye for MVP** |
| 17 | Direkte bankintegrasjon mot DNB, Nordea og SpareBank 1 ved lansering | Fil og én multibank-kanal ved lansering. Direkte i fase 2. | Det tar lang tid å få avtale med hver bank. Filen dekker byråer og alle banker. |
| 18 | Bruke Kombo eller Merge for å *hente* data fra mange HR-systemer | Brutto skal være *kilde* i katalogene deres (fase 2), ikke bruke dem | Unified API-leverandører finnes for apper som skal lese HR- og lønnsdata. Brutto er systemet de leser fra. |
| 19 | ID-porten som innlogging | Vurder | Normalt for offentlige tjenester [U]. BankID via megler dekker behovet. |
| 20 | Toveis kalender (Graph) ved lansering | ICS ved lansering, Graph i fase 2 | **Bygger noe kunden har.** Tilgang til postkassen er sikkerhetsrisiko. |
| 21 | Huma var ikke med | Med i MVP, kap. 5, 2.5 og 6.6 | Nytt gründerkrav underveis |
| 22 | IA-virksomhet som systemflagg | Fjernet | Etter 2024 gir IA-status ingen rettighet i loven |

---

## 10. Åpne spørsmål til gründeren

1. **Utleggsappen, Tikket og OrgLab:** Er de egne søsterprodukter eller uavhengige partnere? Jeg fant ingen offentlig API-dokumentasjon for noen av dem. Hvis de er søsterprodukter, må «like vilkår» også gjelde dem: bare offentlig API.
2. **Huma:** Er Huma partner eller konkurrent? Har vi skriftlig avklart vilkårene for API-bruk? Huma har egen lønnsadministrasjon og lønnspartnere (Visma.net Payroll, PowerOffice).
3. **Saldo for ferie:** Godtar dere at kjernen alltid er fasit for feriesaldo, også når Planday eller Huma viser saldo? Det anbefaler jeg.
4. **Prising:** Skal egne moduler være inkludert i grunnprisen? Konkurrentene tar betalt per bruker for reise og timer (A 3), og A 6.2 anbefaler «alt inkludert».
5. **Tariff:** Hvilke tariffavtaler skal støttes først? Virke HUK og NHO Geneo avgjør timetyper og tillegg.
6. **NAV:** Send kontaktinformasjon til NAV (krav i bruksvilkårene, B 6.1). Avklar også status for API-ene for foreldrepenger og for sykdom i familien etter 21.5.2026.
7. **Arbeidstilsynet:** Holder fast plan med registrering av avvik som oversikt etter § 10-7? Bør bekreftes før timemodulen designes ferdig.
8. **Multibank-kanal:** Velg mellom Mastercard Direkte remittering, Zdata og Aritma ut fra pris og bankdekning.

---

## 11. Kilder

**Lov og forskrift (Lovdata)**
- Ferieloven: https://lovdata.no/dokument/NL/lov/1988-04-29-21 · § 7: https://lovdata.no/lov/1988-04-29-21/§7
- Arbeidsmiljøloven § 4-6: https://lovdata.no/lov/2005-06-17-62/§4-6 · § 10-2 og § 10-4: https://lovdata.no/lov/2005-06-17-62/§10-4 · § 10-5: https://lovdata.no/lov/2005-06-17-62/§10-5 · § 10-6: https://lovdata.no/lov/2005-06-17-62/§10-6 · § 10-7: https://lovdata.no/lov/2005-06-17-62/§10-7 · § 10-8: https://lovdata.no/lov/2005-06-17-62/§10-8 · kap. 12 (§ 12-10): https://lovdata.no/lov/2005-06-17-62/§12-10 · § 14-5: https://lovdata.no/lov/2005-06-17-62/§14-5 · § 14-15: https://lovdata.no/lov/2005-06-17-62/§14-15
- Folketrygdloven § 8-24 (og §§ 8-23 til 8-27): https://lovdata.no/lov/1997-02-28-19/§8-24 · § 8-19: https://lovdata.no/lov/1997-02-28-19/§8-19
- Bokføringsforskriften (§§ 5-5-1, 5-6, 5-9, 5-10, 7-6, 7-7): https://lovdata.no/forskrift/2004-12-01-1558
- Merverdiavgiftsloven §§ 8-3 og 8-4: https://lovdata.no/lov/2009-06-19-58/§8-3
- Høyesterett HR-2021-2532-A (trekk i lønn): https://www.domstol.no/globalassets/upload/hret/avgjorelser/2021/desember-2021/hr-2021-2532-a.pdf

**Myndigheter**
- Skatteetaten, permisjon i a-meldingen: https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/the-a-melding-guide/employment/information-on-employment/leave/
- Skatteetaten, permittering i a-meldingen: https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/the-a-melding-guide/employment/information-on-employment/layoffs/
- Skatteetaten, trekkfri bilgodtgjørelse og passasjertillegg: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/lonn-og-ytelser/oversikt-over-lonn-og-andre-ytelser/trekkfri-bilgodtgjorelse-passasjertillegg-mv
- Skatteetaten, trekkpliktig bilgodtgjørelse: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/lonn-og-ytelser/oversikt-over-lonn-og-andre-ytelser/trekkpliktig-bilgodtgjorelse
- Skatteetaten, trekkfri kost med overnatting: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/lonn-og-ytelser/oversikt-over-lonn-og-andre-ytelser/trekkfri-godtgjorelse-til-kost-pa-reise-med-overnatting
- Skatteetaten, satser for kost og losji: https://www.skatteetaten.no/satser/kost-og-losji-satser-for-trekk-og-skattefri-godtgjorelse/?year=2026
- Skatteetaten, a-meldingen for sluttbrukersystemer: https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/a-meldingen-sbs/ · skattekort: https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/skattekort-sbs/ · lønns- og personalsystemer: https://www.skatteetaten.no/om-skatteetaten/fremtidens-innkreving/systemleverandorer/lonns--og-personalsystem/
- NAV, omsorgspenger for arbeidsgiver: https://www.nav.no/arbeidsgiver/omsorgspenger
- NAV, foreldrepenger for arbeidsgiver: https://www.nav.no/arbeidsgiver/foreldrepenger
- NAV, API-oversikt: https://www.nav.no/samarbeidspartner/ekstern-datautveksling/api-oversikt · sykepenge-API: https://github.com/navikt/sykepenger-im-lps-api/wiki · foreldrepenger: https://github.com/navikt/fp-inntektsmelding-api/wiki · sykdom i familien: https://github.com/navikt/k9-inntektsmelding-api/wiki · oppgjørsrapporter: https://github.com/navikt/sokos-oppgjorsrapporter/wiki · syfo: https://github.com/navikt/syfo-dokumentporten/wiki
- Regjeringen, IA-avtalen utløper: https://www.regjeringen.no/no/tema/arbeidsliv/arbeidsmiljo-og-sikkerhet/inkluderende_arbeidsliv/hva-skjer-med-inkluderende-arbeidsliv-nar-ia-avtalen-ikke-forlenges/id3078097/ · IA-avtalen 2025–2028: https://www.regjeringen.no/no/tema/arbeidsliv/arbeidsmiljo-og-sikkerhet/inkluderende_arbeidsliv/innsikt/ia-avtalen-2025-2028/id3151146/
- Forskningsrådet, kostnader: https://www.forskningsradet.no/finansiering/hvordan-skrive-soknad/budsjett/kostnader-naringsliv-offentlig-sektor/
- SPK, kravspesifikasjon: https://www.spk.no/globalassets/virksomhet/kravspesifikasjon-v.2.2.pdf · KLP: https://www.klp.no/virksomhet/pensjon/hr-lonn-og-personal/rapportering-av-ansattopplysninger
- norge.no, digital postkasse: https://www.norge.no/en/node/83375

**Sekundærkilder**
- Revisorforeningen, særavtalene for reiser fra 2026: https://www.revisorforeningen.no/en/fag/nyheter/endringer-i-saravtalene-for-reiser-fra-2026/
- Azets, nye regler 2026: https://www.azets.com/no-no/innsikt/artikler/nye-regler-pa-hr-og-lonnsomradet-i-2026/
- SNL, permitteringslønnsloven: https://snl.no/permitteringsl%C3%B8nnsloven
- FFG, personalkostnader i Horizon Europe: https://www.ffg.at/en/europe/heu/legal-financial/personnel-costs · Cambridge: https://www.research-services.admin.cam.ac.uk/manage-project/manage-ec-project/staff-costs-and-timesheets-ec-grants
- Smartbyrå om Huma: https://smartbyra.no/vurdering/huma-hr
- Simployer om ny IA-avtale (pressemelding): https://www.mynewsdesk.com/no/simployer-norge/news/dette-betyr-den-nye-ia-avtalen-for-arbeidsgivere-494066

**Leverandører**
- Huma: https://humahr.com/no · fravær: https://humahr.com/no/fravaer · NAV: https://humahr.com/no/nav · integrasjoner: https://humahr.com/no/integrasjon · priser: https://humahr.com/no/prisplan · webhooks: https://humahr.com/knowledge/webhooks · Open API: https://humahr.com/knowledge/open-api og https://openapi.humahr.com/redoc/index.html
- Planday, fravær: https://help.planday.com/en/articles/30535-leave-management-explained · API: https://openapi.planday.com/
- Quinyx: https://developer.quinyx.com/ · Kombo: https://docs.kombo.dev/ · Apideck Norge HRIS: https://www.apideck.com/integrations/country/norway/hris
- Folio API: https://api.folio.no/v2/api.yml · Xledger (tredjepartsguide): https://connectmyapps.atlassian.net/wiki/x/OwC9DQ
- Tripletex hjelp om ferie og fravær: https://hjelp.tripletex.no/hc/no/articles/6932761980305
- Øvrige API-lenker i katalogen er merket [K]. De er kjent fra før, men ikke åpnet i denne runden.

**Runde 1 (interne):** A-marked-konkurrenter.md, B-myndigheter.md (kap. 1, 2, 6, 10), C-beregning.md (kap. 0, 3, 7), D-praksis.md (kap. 5–7), F-arkitektur.md, G-moduler-2026.md (1.11 B1–B8).
