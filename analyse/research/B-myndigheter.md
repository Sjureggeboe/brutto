# B – Myndighetskrav og offentlige grensesnitt for et nytt norsk lønnssystem (SaaS)

**Status per 28.10.2026.** Utarbeidet for et frittstående lønnssystem for virksomheter med 10–1000 ansatte, også lisensiert til regnskapsbyråer.

**Metode og forbehold**
- Kildene er primært skatteetaten.no, skatteetaten.github.io (Skatteetatens API-dokumentasjon; repoet er klonet og lest i kildeform, siste commit 23.10.2026), Skatteetatens RSS-feeder for nyheter til sluttbrukersystemer, lovdata.no, regjeringen.no, nav.no, NAVs GitHub-wikier (navikt), docs.altinn.studio, samarbeid.digdir.no og datatilsynet.no.
- Merking:
  - **[V]** betyr verifisert i primærkilde.
  - **[S]** betyr sekundærkilde eller søkeutdrag (ikke lest i fulltekst hos primærkilden).
  - **[IV]** betyr *ikke verifisert*.
- Websøkebudsjettet for økten tok slutt underveis. Noen punkter (egenmelding-endringer 2026, NAV bidragstrekk, sammenstillingsoppgave-frist m.fl.) er derfor merket [IV] og bør følges opp.
- Ingen satser er gjettet. Der primærkilde mangler, står det «ikke verifisert».

---

## 0. Kortversjon – det viktigste for produktet

1. **Altinn II er borte for lønn.** A-meldingstjenestene A02/A03/A06/A07 i Altinn II ble stengt **15.06.2026**, og A01/A04/A05 stengte 31.05.2026 [V]. All systeminnsending skjer nå via **Skatteetatens egne REST-API-er**. Autentisering skjer med **Maskinporten + Altinn 3 systembruker + tilgangspakker**, og tilbakemelding hentes via **Dialogporten** [V].
2. **Regnskapsbyrå-scenariet** løses med **«systembruker for klientsystem»** (tidligere «agent-systembruker»). Den støtter *kun tilgangspakker*, kan bare opprettes leverandørdrevet, og byrået knytter klienter til den via klientdelegering [V]. Gamle Altinn II-roller gir ikke a-meldingstilgang etter **17.11.2026** og opphører helt **31.12.2026** [V].
3. **Skattetrekkskontoen er avviklet fra 01.01.2026.** Forskuddstrekk og utleggstrekk betales direkte til Skatteetaten **senest første virkedag etter hver lønnsutbetaling**, med 19-sifret KID med *månedsperiode* og som eget betalingsoppdrag [V]. AGA følger fortsatt annenhver måned (15. jan/mar/mai/jul/sep/nov) [V].
4. **Skattekort hentes via nytt REST-API** (i produksjon siden 30.10.2025) [V]. Fra **15.12.2026** fjernes Dialogporten-varsling, så det blir *kun polling*, og det kommer to nye responsverdier [V].
5. **Skatteetaten publiserer trekkrutinen som Java-kildekode på GitHub** (`Skatteetaten/trekktabell`, 2026-versjon). Repoet har **ingen lisensfil**, så gjenbruksrett må avklares [V].
6. **NAV:** API-er for inntektsmelding (sykepenger, foreldre-/svangerskapspenger, «sykdom i familien»), sykmelding/søknad til arbeidsgiver, oppgjørsrapporter m.m. er oppført som **i produksjon** [V]. NAVs egen arbeidsgiverside (oppdatert 11.06.2026) sier likevel at bare sykepenger kan sendes fra lønnssystem. Det er en **motstrid** som må avklares med NAV.
7. **Nye utleggstrekkregler fra januar 2026:** «samordnet utleggstrekk» har egen a-meldingskode og betales dagen etter lønn, og trekkpålegg kan hentes via **Trekkpålegg-API** [V].
8. **Varslede endringer:**
   - Nye forretningsregler F532/F530 fra periode 2027-01 [V].
   - **A-melding versjon 2.4 fra 2028-01** (spesifikasjon senest 01.05.2027, test senest 15.09.2027) [V].
   - Statsbudsjett 2027 (forslag 07.10.2026): trygdeavgift lønn 7,6 → 7,4 %, personfradrag 120 180, nye trinngrenser og **ny firmabilmodell fra 01.01.2027** (20 % av listepris + fast kronetillegg etter motortype) [V – forslag, ikke vedtatt].
9. **Hosting:** Bokføringsloven § 13 krever fortsatt at regnskapsmateriale *oppbevares i Norge*, med forskriftsunntak [V]. Datatilsynet anbefaler en beredskapsplan for US-overføringer (oppdatert 01.07.2026) [V]. Dette er avgjørende for valg av sky/region.

---

## 1. Felles grunnmur: Maskinporten, Altinn 3 systembruker, tilgangspakker og Dialogporten

Alle de nye statlige maskin-til-maskin-grensesnittene for lønn (Skatteetaten og NAV) bygger på samme mønster.

### 1.1 Oppkobling steg for steg (Skatteetaten/Digdir) [V]

1. Norsk organisasjonsnummer og signerte bruksvilkår hos Digdir. Opprett **Maskinporten-klient** i Samarbeidsportalen eller via API. Maskinporten er obligatorisk.
2. Be Digdir om Altinn-scopes: `altinn:authentication/systemregister.write`, `altinn:authentication/systemuser.request.read`, `altinn:authentication/systemuser.request.write` og eventuelt `digdir:dialogporten`. Flere av disse er *ikke allment tilgjengelige* og må bestilles hos Altinn/Digdir (servicedesk@altinn.no) [V, NAV-wiki].
3. **Registrer systemet i Altinns systemregister** (API), knyttet til Maskinporten-klientens `clientId`, med de tilgangspakkene og ressursene systemet trenger.
4. Søk om **etatsspesifikke scopes**. Hos Skatteetaten skjer det via eget søknadsskjema/brukerstøtte og aksept av bruksvilkår. Hos NAV er scopes «tilgjengelig for alle» i selvbetjening, men NAV krever at leverandøren sender kontaktinformasjon.
5. Opprett **systembrukerforespørsel** per kunde. Kunden godkjenner via en URL i Altinn.
6. Hent **Maskinporten-token med systembruker-claim** (`authorization_details` av type `urn:altinn:systemuser`) for etatens scope. Kall API-et.

Kilder:
- https://www.skatteetaten.no/samarbeidspartnere/reetablering-altinn/systemleverandor/oppkobling/
- https://skatteetaten.github.io/api-dokumentasjon/om/systembruker
- https://github.com/navikt/sykepenger-im-lps-api/wiki/6.-Autentisering-og-autorisasjon

**Teknisk detalj (NAV) [V]:** Kall mot NAVs sykepenge-API krever et Maskinporten-token som *ikke* er vekslet til Altinn-token. Vekslingen (`/authentication/api/v1/exchange/maskinporten`) trengs bare for enkelte kall mot Altinn selv.

### 1.2 Standard systembruker vs. systembruker for klientsystem [V]

| | Systembruker for eget system | Systembruker for klientsystem (tidl. «agent») |
|---|---|---|
| Bruk | Kunden rapporterer for egen virksomhet | Byrå rapporterer for sine klienter |
| Rettigheter | Tilgangspakker **og** enkeltrettigheter | **Kun tilgangspakker** |
| Opprettes av | Sluttbruker eller leverandør | Kun leverandørdrevet |
| Klienter | – | Byråets klientadministrator knytter klienter til systembrukeren (GUI eller API) |

- Byrået får fullmakt enten automatisk via Enhetsregisteret (roller REGN/REVI/FFØR) eller ved at klienten delegerer til byråets organisasjonsnummer.
- Opphører klientforholdet, faller klientdelegeringen bort automatisk.
- Støtter produktet begge scenarier, skal det lages **to separate systembrukere**.

Kilde: https://docs.altinn.studio/nb/authorization/guides/system-vendor/system-user/ (underliggende sider: systemregistration, systemuserrequest, client-delegation, usetoken).

### 1.3 Relevante tilgangspakker (fra Skatteetatens og NAVs API-dokumentasjon) [V]

| Tjeneste | Tilgangspakker (URN `urn:altinn:accesspackage:…`) |
|---|---|
| A-melding innsending/tilbakemelding/avstemming | `a-ordning`, `regnskapsforer-lonn`, `regnskapsforer-med-signeringsrettighet`, `regnskapsforer-uten-signeringsrettighet`, `ansvarlig-revisor`, `revisormedarbeider`. Enkeltrettighet: ressurs `ske-innrapportering-amelding` |
| Skattekort til arbeidsgiver | Som over, pluss `lonn` og `skatt-naering` (ikke `a-ordning`). Ressurs `ske-skattekort-til-arbeidsgiver` |
| NAV sykepenger (IM, sykmelding, søknad, dialog) | `lonn-personopplysninger-saerlig-kategori`, alternativt enkeltressurser `nav_sykepenger_*` |

### 1.4 Tidslinje Altinn II → Altinn 3 [V]

| Dato | Hendelse |
|---|---|
| 31.05.2026 | Altinn II avviklet for de fleste Skatteetaten-tjenester. A01/A04/A05 stengt. Tilgangspakker kreves for rapportering fra system |
| 15.06.2026 kl. 12 | A-melding (A02/A03/A06/A07) og skattekort til arbeidsgiver stengt i Altinn II (forlenget frist). NAVs gamle K27-oppgjørsrapport sendt ut siste gang |
| 19.06.2026 | Ikke lenger mulig å delegere Altinn II-roller. Digdir/NAV omtaler 19.06.2026 som dagen Altinn 2 slås av |
| 20.10.2026 | Kontroll (Skatteetaten) ikke lenger via Altinn II-roller |
| 17.11.2026 | A-melding, skattekort, skattemelding m.m. ikke lenger tilgjengelig via Altinn II-roller |
| 01.12.2026 | Alle NAV-tjenester ikke lenger via Altinn II-roller |
| 31.12.2026 | Alle gjenværende Altinn II-roller opphører (bl.a. Statens pensjonskasse og KS) |

Kilder:
- https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/frist-altinn3-forlenges/
- https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/altinn-ii-stenges-15.-juni/
- https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/nye-tilgangspakker-for-a-meldingen/ (oppdatert 01.10.2026)
- https://info.altinn.no/hjelp/ny-tilgangsstyring/utfasing-av-altinn-ii-roller/
- https://www.skatteetaten.no/samarbeidspartnere/reetablering-altinn/regnskapsforer-revisor/

**Merk:** Skatteetaten innførte midlertidig **ingen tvangsmulkt for a-meldingen for mai, juni og juli 2026** på grunn av overgangen. Fristene gjaldt likevel [V]. Kilde: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/ingen-tvangsmulkt-for-a-meldingen-i-mai-juni-og-juli/

---

## 2. A-ordningen / a-meldingen

### 2.1 Format [V]
- **Gjeldende versjon: a-melding v2.3.**
  - XSD: `20240827 a-meldingen_v2_3.xsd`
  - Informasjonsmodell: `20241002 Informasjonsmodell A02.pdf`
  - Formater: `28102025 Formater v2.3.xlsx`
  - Forretningsregler og kodeliste: **R1 2026**
  - Tilbakemelding: `a-meldingen_tilbakemelding_v2_3.xsd`
  - Avstemming (A07): `a-meldingen-avstemming-opplysningspliktig_v3_3_0.xsd`
- Lønnssystemet bygger a-meldingen som XML etter v2.3. Swagger-spesifikasjonen angir JSON-innpakning for REST-kallene. Payload-spesifikasjonen er den samme for REST- og filopplastings-API.
- Kilde: https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/a-meldingen-sbs/

### 2.2 Innsending (eier: Skatteetaten) [V]
- **REST-API** for innsendinger < 10 000 000 byte: https://app.swaggerhub.com/apis/skatteetaten/innrapportering-amelding-api/
- **Filopplastings-API** (også > 10 MB): https://app.swaggerhub.com/apis/skatteetaten/innrapportering-amelding-filopplasting-api/ (i produksjon fra 09.04.2026).
- **Scope:** `skatteetaten:innrapporteringamelding`. Samme scope brukes for REST, filopplasting, tilbakemelding og avstemmingsrapport.
- **`idempotencyKey` (UUID) er påkrevd** per kall. Gjenbruk av nøkkel gir `AMLD_019` (HTTP 409). Det gjør trygge retries mulig.
- Relevante feilkoder:
  - `AMLD_1062`: oppgavegiver er ikke hovedenhet. Opplysningspliktig er juridisk enhet, og virksomheter/underenheter rapporteres inne i meldingen.
  - `AMLD_1063`: token mangler systembruker.
  - `AMLD_1051/1052`: avvik mellom path og innhold for opplysningspliktig/periode.
- **Fra 2026 er API eneste måte å sende a-melding fra system.**
- **Reserveløsning:** manuell opplasting av XML-fil på skatteetaten.no (i produksjon, nyhet 04.06.2026). Skatteetaten ber leverandører sikre at systemet kan **eksportere gyldig XML** og har brukerveiledning for det.
- Kilder:
  - https://skatteetaten.github.io/api-dokumentasjon/api/innrapportering-amelding (sist oppdatert 17.02.2026)
  - https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/viktig-sikre-stotte-for-manuell-innsending-av-amelding-via-xml-i-overgangsperioden/

### 2.3 Tilbakemelding, kvitteringsflyt og avvik [V]
- Tilbakemeldingen (tidligere A03) hentes via **tilbakemeldings-API**: https://app.swaggerhub.com/apis/skatteetaten/amelding-tilbakemelding-api/
- **Systemet må lytte på hendelser i Dialogporten** for å vite når tilbakemeldingen er klar. Beskrevet hos Digdir: https://samarbeid.digdir.no/altinn/hvordan-hente-meldinger-gjennom-dialogporten/2869
- Fra slutten av mai 2026 (produksjon) har forsendelsen («transmission») i Dialogporten **to URL-er**:
  - `consumerType: Gui` for nedlasting i innboks
  - `consumerType: Api` for maskinell uthenting
  - Systemet må bruke Api-URL-en.
- Skatteetaten meldte en feil i JSON for tilbakemelding (05.06.2026). Det illustrerer at grensesnittet fortsatt modnes.
- Tilbakemeldingen inneholder avviksmeldinger med alvorlighetsnivå (blant annet «øyeblikkelig» og «retningslinje»). Den siste tilbakemeldingen i måneden oppsummerer alle a-meldinger for måneden, inkludert beløp til betaling.
- Kilde: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/arbeidsgiveravgift/betaling-av-forskuddstrekk-og-arbeidsgiveravgift/

### 2.4 Erstatningsmeldinger og korrigering
- En ny a-melding for samme opplysningspliktig og kalendermåned **erstatter hele den forrige** (erstatningsmelding). Bare siste innsendte gjelder [V/S].
- Feil skal rettes innen fristen for a-meldingen for måneden feilmeldingen ble mottatt [S].
- Korrigeringer kan sendes inntil **3 år etter innleveringsfristen**. Skatteetaten har egen avviksmelding for endring av AGA for periode med frist eldre enn tre år [S].
- Etterbetalinger rapporteres i måneden de utbetales [S].
- Kilder:
  - https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/the-a-melding-guide/salary-and-benefits/correcting-errors-in-salary-and-other-benefits/
  - https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/the-a-melding-guide/error-messages-magnetedag-and-feedback/error-messagesdiscrepancies-magnetedag/changes-have-been-made-to-employers-national-insurance-contributions-andor-financial-activity-tax-for-a-period-where-the-submission-deadline-was-more-than-three-years-ago/

### 2.5 Frister og sanksjoner
- **Frist:** den 5. i måneden etter perioden, eller neste virkedag hvis den 5. faller på helg/helligdag [V]. Den 5. desember 2026 er en lørdag, så fristen blir mandag 7.12.2026. Kilde: https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/deadlines-and-payment/
- Levering minst én gang per kalendermåned og elektronisk til mottakssentralen som Skattedirektoratet fastsetter (a-opplysningsloven §§ 4–5) [V]. Kilde: https://lovdata.no/lov/2012-06-22-43/§5
- **Tvangsmulkt** (a-opplysningsloven § 10): daglig løpende til opplysningene er levert, samlet maks **1 000 × rettsgebyret** [V].
  - Sats 1/10 rettsgebyr per inntektsmottaker per dag, og rettsgebyr 2026 = 1 345 kr [S, søkeutdrag fra skatteetaten.no].
- **Lønnsutbetalingsdato** må rapporteres korrekt. Den styrer nå forfall for forskuddstrekk (se kap. 4) [V].
- Skatteetaten minnet 05.10.2026 om at **siste dato for endring av stillingsprosent er obligatorisk** [V, RSS].

### 2.6 Avstemming (tidligere A06/A07) [V]
- **Avstemmingsrapport-API** er i produksjon fra 03.06.2026, og en ny versjon kom 11.09.2026. Det gir samme innhold som portalen «Avstemmingsinformasjon» (ODS/XML/JSON).
- Scope: `skatteetaten:innrapporteringamelding`.
- Kilde: https://skatteetaten.github.io/api-dokumentasjon/api/amelding-avstemmingsrapport | Swagger: https://app.swaggerhub.com/apis/skatteetaten/avstemmingsrapport-amelding-api/
- Tilleggstjeneste: **«Krav og betalinger»-API** (lansert 18.03.2026) for automatisk avstemming mot skatte- og avgiftskrav, og **«Frister»-API** (08.05.2026) [V, RSS]. Begge er valgfrie, men nyttige for byrå-funksjonalitet.

### 2.7 Sammenstillingsoppgave
- Ferieloven § 10 krever at feriepengegrunnlaget fremgår av en sammenstilling som sendes arbeidstakeren [V].
- Frist og hjemmel for årlig sammenstillingsoppgave til inntektsmottaker (antatt 31. januar) er **ikke verifisert** i denne runden. A-opplysningsloven inneholder ikke bestemmelsen. Den må sjekkes i forskrift eller Skatteetatens veiledning [IV].

### 2.8 Testmiljø [V]
- Skatteetatens eksterne testmiljø og Digdirs **TT02**. TT02 dekker Maskinporten-test, systembruker, Dialogporten og Altinn-innboks. Det finnes manuell filopplasting i test: https://ameldingfilopplasting.skatteetaten-test.no/web/amelding-filopplasting/
- **Kun syntetiske data** (Tenor testdatasøk) er tillatt, med begrunnelse i GDPR. Kilder: https://www.skatteetaten.no/testdata/ og https://skatteetaten.github.io/api-dokumentasjon/test/tenor
- For delegering i test må både leverandør og testkunde finnes i TT02 (Altinn servicedesk leser inn). Kilde: https://skatteetaten.github.io/api-dokumentasjon/test/testfrasystemleverandor
- Statusside: https://status.skatteetaten.no/

### 2.9 Krav før produksjon (Skatteetaten generelt) [V]
- Det finnes **ingen formell sertifisering.** Tilgang gis når leverandøren har akseptert bruksvilkår, fullført integrasjonstest mot det delte testmiljøet og koblet seg til produksjon. Testdokumentasjon må kunne fremlegges på forespørsel.
- Bruksvilkårene stiller i tillegg disse kravene:
  - Leverandøren er **databehandler** for kundene sine.
  - Informasjonssikkerhet og internkontroll skal være dokumentert.
  - Systemet skal være hendelsesdrevet fremfor hyppig polling (ellers kan det struping/blokkering skje).
  - Grenser for delings-API: 5 forespørsler/s og 10 000/time.
  - Brytende endringer varsles normalt minst **4 måneder** i forveien.
  - Leverandøren må abonnere på nyheter og statusside.
  - Skatteetaten kan stenge tilgang ved alvorlige brudd.
- Kilde: https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/bruksvilkar/

### 2.10 Data som deles videre fra a-ordningen [V]
- A-meldingen er felles kilde for **NAV og SSB**. Skatteetaten deler data via API-ene Arbeidsforhold, Inntekt, Opptjeningsgrunnlag osv.
- **Det finnes ingen egen SSB-lønnsstatistikkrapportering fra lønnssystemet.** Kvaliteten avhenger av korrekte a-meldingsfelt (stillingsprosent, yrke, arbeidstid osv.).
- Kilde: https://skatteetaten.github.io/api-dokumentasjon/anvendelsesomraader/ameldingen

---

## 3. Skattekort og forskuddstrekk

### 3.1 Skattekort til arbeidsgiver – API (eier: Skatteetaten) [V]
- Erstatter Altinn-skjema RF-1211. **I produksjon siden 30.10.2025.**
- Swagger: https://app.swaggerhub.com/apis/skatteetaten/skattekort-til-arbeidsgiver/
- **Scope** `skatteetaten:skattekorttilarbeidsgiver`. Systembruker-ressurs `ske-skattekort-til-arbeidsgiver`.
- **Flyt:** `bestillSkattekort` returnerer en referanse på formen `BR…`, og `hentSkattekortbestillingSvar` henter svaret ved polling. HTTP 204 betyr at svaret ikke er klart.
  - `bestillingstype`: `HENT_ALLE_OPPGITTE` eller `HENT_KUN_ENDRING`.
  - `varslingstype`, for eksempel `VARSEL_VED_FOERSTE_ENDRING`.
- **Begrensning:** maks 1 000 fødselsnumre per kall. Endringsbestillinger returnerer alle endringer.
- Fra 16.06.2026 er det **krav om å angi arbeidsgiver** ved bestilling av endringer for systembrukere med flere arbeidsgivere (feilkode `FOR_004`). Skatteetaten varslet 23.06.2026 at endringer kunne mangle ved samlet bestilling.
- **Responsmodell:**
  - Per `trekkode` (`LOENN_FRA_HOVEDARBEIDSGIVER`, `LOENN_FRA_BIARBEIDSGIVER`, `LOENN_FRA_NAV`, `PENSJON`, `PENSJON_FRA_NAV` …) kommer enten `trekktabell` (`tabellnummer`, `prosentsats`, `antallMaanederForTrekk`), `trekkprosent` eller `frikort` (`frikortbeloep`).
  - `tilleggsopplysning`, for eksempel `kildeskattPaaLoenn` og `kildeskattPaaPensjon`.
  - `resultatForSkattekort`, for eksempel `skattekortopplysningerOK` og `ikkeSkattekort`.
- XML støttes også i request og respons.
- **Endringer fra 15.12.2026:**
  - **Ingen Dialogporten-dialoger lenger**, bare polling-basert bruk.
  - **To nye verdier** i `resultatForSkattekort`: `registrertSomDoed` (ikke hent – oppslag varsler etterlatte) og `trekkEtterReglerOmKildeskattPaaPensjon15Prosent`.
- **Personvern i praksis:** Skatteetaten varsler den skattepliktige når en ny arbeidsgiver henter skattekortet. Hent derfor ikke for personer som ikke lenger er ansatt (nyhet 21.01.2026).
- **Reserveløsning:** portal med XML-filopplasting via ID-porten, samme format som RF-1211 (forespørsel-XSD v2.0, respons-XSD v3.0), maks 1 MB (ca. 15 000 fnr).
- **Test:** regneark med testpersoner for 2026. Skattekort i test oppdateres daglig kl. 06.
- Kilder:
  - https://skatteetaten.github.io/api-dokumentasjon/api/skattekorttilarbeidsgiver
  - https://skatteetaten.github.io/api-dokumentasjon/anvendelsesomraader/skattekorttilarbeidsgiver
  - https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/endret-bruksmonster-for-henting-av-skattekort/
  - https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/to-nye-responsverdier-i-resultatforskattekort/

### 3.2 Regler for forskuddstrekk 2026 (Forskuddsutskrivingen 2026) [V]
- **Tabelltrekk** gjelder i 10,5 måneder.
  - Fradragstabeller har nummer **8000–8400**, og tilleggstabeller **9010–9400**. De tre siste sifrene angir tusen kroner i fradrag/tillegg.
  - Det finnes måneds-, 14-dagers-, ukes-, 4-, 3-, 2- og 1-dagstabeller.
  - Tabellkort kan bare brukes hos én arbeidsgiver om gangen.
  - Endres skattekortet etter mai, gjøres tabellkortet om til prosentkort.
  - Med fradrag over 400 000 beregnes alltid prosentkort.
- **Juni/desember:** Feriepenger er som hovedregel trekkfrie i utbetalingsåret, og det er **halvt trekk** i november eller desember (arbeidsgiver velger, de fleste bruker desember). Skatten fordeles på 10,5 måneder. Det gjelder ikke for 12-månederskort (for eksempel kildeskatt), som alltid trekkes. Kilde: skattebetalingsforskriften §§ 5-7-1 og 5-7-2, gjengitt i Forskuddsutskrivingen.
- **Frikort:** beløpsgrense **100 000 kr** i 2026. Feriepenger, også trekkfrie, regnes med i fribeløpet. Frikort gis fra året personen fyller 13.
- **Manglende skattekort:** trekk **50 %**.
- **Kildeskatt på lønn (PAYE):**
  - **25 %** for personer mellom 17 og 69 år, **22,5 %** for de under 17 eller over 69, og **17,4 %** for ikke-medlemmer av folketrygden.
  - Inntektsgrense **725 050 kr** (= trinn 3).
  - Trekk på 12 måneder, altså ingen trekkfri juni og intet halvt desembertrekk.
  - Ordningen kan ikke kombineres med blant annet næringsinntekt eller lønn fra den norske stat.
  - Kilde for satsen: også regjeringens satsoversikt (25 % i 2026 og foreslått for 2027).
- Kilde: https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/

### 3.3 Beregning av tabelltrekk – offisiell algoritme [V]
- **Skatteetaten publiserer trekkrutinen som Java-kode:** https://github.com/Skatteetaten/trekktabell.
  - 2026-versjonen ble committet 08.12.2025. Pakke `no.skatteetaten.fastsetting.formueinntekt.forskudd.trekkrutine2026`.
  - Metoden `Trekkrutine.beregnTabelltrekk`, og `beregnHeleTabellen` for hele tabellen.
  - **Overskytende prosent er fjernet fra 2025**, slik at trekket beregnes ordinært også over den tidligere grensen.
  - Klassen `Periode` inneholder periodefaktorer og avrunding per tabellperiode.
- Konstantene for 2026 i `Konstanter.java` samsvarer med satsene:
  - personfradrag 114 540
  - trinn 226 100 / 318 300 / 725 050 / 980 100 / 1 467 200 med 1,7 / 4,0 / 13,7 / 16,8 / 17,8 %
  - trygdeavgift 7,6 % (lav sats 5,1 %), nedre grense 99 650 og opptrapping 25 %
  - minstefradrag 46 %, maks 95 700
  - fellesskatt 8,25 % (Finnmark 4,75 %)
- **Repoet har ingen lisensfil.** GitHub-API-et returnerer «license: None». Juridisk rett til å gjenbruke koden i et kommersielt produkt er derfor uavklart. Alternativene er å avklare med Skatteetaten, implementere selv etter samme logikk, eller validere mot de offisielle tabellene.
- **Offisielle trekktabeller som tekstfil** (zip) kan brukes til regresjonstest. Formatet er tabellnr (4), periode (1), tabelltype (1), trekkgrunnlag (6) og trekk (6). Kilde: https://www.skatteetaten.no/satser/trekktabeller-i-tekstformat/?year=2026 (lenker også til trekkrutinen og søk på https://trekktabell.formueinntekt.skatt.skatteetaten.no/)
- **Risiko:** Ny trekkrutine publiseres normalt først i **desember** før inntektsåret (2026-versjonen kom 08.12.2025). Det gir et kort vindu for produksjonssetting før januarlønn.

---

## 4. Innbetaling: forskuddstrekk, AGA og utleggstrekk (KID)

| Krav | Forfall fra 2026 | KID-type (pos. 12–13) | Kilde |
|---|---|---|---|
| Forskuddstrekk | **Senest første virkedag etter lønnsutbetaling** [V] | 05, periode = **måned** (pos. 16–17) [V] | betalingsside + SBS-nyhet 06.01.2026 |
| Utleggstrekk skatt (gml. regler) | Første virkedag etter lønnsutbetaling (fra januar 2026) [V] | 03 [V] | fremtidens-innkreving |
| Samordnet utleggstrekk (nye regler) | Dagen etter lønnsutbetaling, til **konto og KID i trekkpålegget** [V] | Fra pålegget, unik per ansatt og trekk [S] | fremtidens-innkreving |
| Arbeidsgiveravgift | Annenhver måned: 15.1, 15.3, 15.5, 15.7, 15.9, 15.11 (15.11.2026 er søndag, så fristen er 16.11) [V] | 06 [V] | betalingsside |
| Finansskatt lønn | Samme terminer som AGA [V] | 09 [V] | betalingsside |

- **Skattetrekkskontoen er avviklet fra 01.01.2026.** 6. termin 2025 ble betalt fra kontoen innen 15.01.2026, og restsaldo kan brukes til 2026-trekk [V].
  - Bankgaranti som alternativ til skattetrekkskonto er ikke omtalt på Skatteetatens betalingsside, men faller logisk bort med ordningen [IV].
- **KID-struktur:** 19 siffer.
  - Posisjon 1–11 er betaler (for organisasjoner «00» + organisasjonsnummer).
  - Posisjon 12–13 er kravtype.
  - Posisjon 14–15 er inntektsår.
  - Posisjon 16–17 er periode.
  - Gjenværende posisjoner er ikke beskrevet i kilden. Bruk Skatteetatens KID-generator eller spesifikasjon [IV for full algoritme].
- Forskuddstrekk må sendes som **eget betalingsoppdrag**, ikke merket «Lønn/SALARY», ellers kan KID falle bort [V].
- Minstebeløp per oppgjørsperiode er 100 kr (skattebetalingsforskriften § 10-4-1) [V].
- **Konsekvens for produktet:** Bankintegrasjonen (pain.001/ISO 20022 eller bankfil) må generere separate, strukturerte betalinger med korrekt KID ved *hver* lønnskjøring, ikke terminvis. Lønnsutbetalingsdato i a-meldingen må stemme med faktisk utbetaling.
- Kilder:
  - https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/arbeidsgiveravgift/betaling-av-forskuddstrekk-og-arbeidsgiveravgift/
  - https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/forskuddstrekk-betalingsoppdrag-og-kid/
  - https://www.skatteetaten.no/om-skatteetaten/fremtidens-innkreving/systemleverandorer/lonns--og-personalsystem/
  - https://www.revisorforeningen.no/fag/nyheter/skattetrekkskontoen-fjernes-fra-1.-januar-2026/ [S]

---

## 5. Arbeidsgiveravgift (AGA)

### 5.1 Satser 2026 (Stortingsvedtak 18.12.2025 nr. 2748) [V]

| Sone | Generelle næringer | Merknad |
|---|---|---|
| I | 14,1 % | |
| Ia | 10,6 % inntil fribeløpet er brukt, deretter 14,1 % | Fribeløp |
| II | 10,6 % | |
| III | 6,4 % | |
| IV | 5,1 % | |
| IVa | 7,9 % | |
| V | 0 % | |

- Ingen endringer i soner eller satser fra 2025 til 2026.
- **Fribeløp (bagatellmessig støtte): 850 000 kr per foretak/konsern per år.** Fribeløpet gjelder sone Ia (generelle næringer) og sektorunntatte/vanskeligstilte foretak i sone II–V. Det må avkortes mot annen bagatellmessig støtte, med samlet tak på 300 000 euro over tre år.
- **Særregler:**
  - Statsforvaltning og helseforetak har ikke fribeløp i Ia.
  - Sektorunntatt er stål, kull, finans/forsikring og hovedkontortjenester i konsern.
  - Foretak i økonomiske vanskeligheter har særregler.
  - For jord- og skogbruk i Ia/IVa gjelder redusert sats på all lønn.
  - Svalbard har 0 %.
- **Forslag 2027 (Prop. 1 LS 2026–2027):** uendrede satser og fribeløp 850 000 [V – forslag].
- Kilder:
  - https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/
  - https://www.regjeringen.no/no/tema/okonomi-og-budsjett/skatter-og-avgifter/skatte-og-avgiftssatser/skattesatser-2027/id3173438/

### 5.2 Ekstra arbeidsgiveravgift [V]
- Den ekstra arbeidsgiveravgiften på 5 % av lønn over 850 000 kr er **avviklet fra 01.01.2025**. Den skal ikke svares for ytelser etter 2024.
- Systemet trenger logikk for ekstra AGA bare ved korrigering av perioder til og med 2024 (innenfor treårsgrensen).
- Kilde: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/arbeidsgiveravgift-og-finansskatt/ekstra-arbeidsgiveravgift (merket «UTGÅTT») og regjeringen.no.

### 5.3 Virksomhetsprinsippet og underenheter [V]
- Satsen følger sonen der **virksomheten (underenheten) er registrert i Enhetsregisteret**. Hver underenhet er egen beregningsenhet, og «postkasseadresse» godtas ikke.
- **Ambulerende arbeid:** Utfører den ansatte mer enn halvparten av arbeidsdagene i en måned i en annen sone, gjelder den sonens sats for tilsvarende andel. For ikke-stedbundet arbeid gjelder dette bare hvis sonen har høyere sats.
- Arbeid i utlandet eller på sokkelen (mer enn 50 % av månedens arbeid) får sone I-sats.
- **Systemkrav:**
  - Sone- og beregningskode per virksomhet.
  - Fribeløpsforbruk aggregert per foretak/konsern på tvers av underenheter og år.
  - Støtte for ambulerende fordeling per ansatt og måned.

### 5.4 Utenlandske arbeidstakere
- Hovedregelen er at avgiftsplikt følger trygdemedlemskap (folketrygdloven § 23-2; A1-attest/trygdeavtaler gir unntak).
- Detaljregler for 2026 er **ikke gjennomgått i primærkilde i denne runden** [IV].
- Avgiftsmeldingen omtaler bare utenlandsarbeid ved ambulerende virksomhet/sokkel.

---

## 6. NAV

### 6.1 API-oversikt for lønns- og personalsystemer (LPS) – alle oppført med status «Produksjon» [V]

| API | Scope (Maskinporten) | Altinn-ressurs / tilgang | Dokumentasjon |
|---|---|---|---|
| Inntektsmelding sykepenger, forespørsel om IM, sykmelding og sykepengesøknad til arbeidsgiver (inkl. PDF-kopi), Dialogporten | `nav:helseytelser/sykepenger` | `nav_sykepenger_inntektsmelding`, `_sykmelding`, `_soeknad`, `_dialog`. Samlet i pakken `lonn-personopplysninger-saerlig-kategori` | https://sykepenger-api.nav.no/swagger · https://github.com/navikt/sykepenger-im-lps-api/wiki |
| Inntektsmelding foreldrepenger og svangerskapspenger | `nav:inntektsmelding/foreldrepenger` | `nav_foreldrepenger_inntektsmelding` | https://github.com/navikt/fp-inntektsmelding-api/wiki |
| Inntektsmelding «sykdom i familien» (omsorgs-, opplærings- og pleiepenger) + **refusjonskrav omsorgspenger** uten forespørsel | `nav:inntektsmelding/sif` | `nav_sykdom-i-familien_inntektsmelding` | https://github.com/navikt/k9-inntektsmelding-api/wiki (prod https://k9-inntektsmelding-api.nav.no) |
| Oppgjørsrapporter (refusjoner fra NAV, tidl. K27/T12/T14) | `nav:utbetaling/oppgjorsrapporter` | – | https://github.com/navikt/sokos-oppgjorsrapporter/wiki |
| Sykefraværsdokumenter (Dialogporten), oppfølgingsplan, nærmeste leder | `nav:syfo/dokumentporten` m.fl. | – | https://github.com/navikt/syfo-dokumentporten/wiki · https://lps-oppfolgingsplan-mottak.nav.no/swagger |
| Arbeidsforhold (Aa-registeret) | – | – | https://navikt.github.io/aareg/ |

- Oversiktskilde: https://www.nav.no/samarbeidspartner/ekstern-datautveksling/api-oversikt
- Statusside for sykepenge-API-et viser at sykmelding, søknad, forespørsel, inntektsmelding, Dialogporten og PDF-kopier er i produksjon. Kilde: https://github.com/navikt/sykepenger-im-lps-api/wiki/Status-produksjonssetting
- **Bruksvilkår:**
  - NAVs API-vilkår (PDF, v1) aksepteres ved bruk.
  - **Leverandøren må sende kontaktinformasjon til nav.prosjekt.2.inntektsmelding@nav.no**, ellers anses vilkårene ikke oppfylt.
  - Egne vilkår finnes for foreldrepenger/svangerskapspenger og «sykdom i familien».
- **Motstrid:** NAVs arbeidsgiverside https://www.nav.no/arbeidsgiver/sende-inntektsmelding (oppdatert 11.06.2026) sier at bare sykepenger kan sendes fra lønnssystem, mens API-oversikten viser foreldrepenger- og K9-API i produksjon. Den sannsynlige forklaringen er at arbeidsgiversiden er utdatert. **Bekreft med NAV (ekstern.datautveksling@nav.no) [usikkert].**
- **Flyt:**
  - NAV oppretter en *forespørsel om inntektsmelding*.
  - LPS lytter via Altinn Events/Dialogporten eller poller, henter A-ordningsinntekt for beregning av månedsinntekt etter ftrl. § 8-28 (API-et eksponerer inntekt) og sender inntektsmeldingen inklusive eventuelt refusjonskrav.
  - Refusjon av sykepenger kreves i inntektsmeldingen. For omsorgspenger finnes eget refusjonskrav.
  - Utbetalte refusjoner kommer i oppgjørsrapporten.

### 6.2 Sykepengeregler med systemkonsekvens [V]
- **Arbeidsgiverperiode** på 16 kalenderdager (ftrl. § 8-19). Fravær med mindre enn 16 dager mellomrom slås sammen.
- **Egenmelding** (ftrl. §§ 8-23 til 8-27):
  - Inntil 3 kalenderdager om gangen etter minst 2 måneders ansettelse.
  - Arbeidsgiver kan utvide i arbeidsgiverperioden, etter drøfting med tillitsvalgte.
  - Retten kan fratas etter 4 tilfeller på 12 måneder.
  - **Eventuelle endringer i 2026 er ikke sjekket** [IV].
- **Sykepengegrunnlaget er maks 6 G** (§ 8-10). Minsteinntekten er 50 % av G (§ 8-3).
- **G = 136 549 kr fra 01.05.2026** (opp fra 130 160) [V]. Kilde: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/oppdatert-grunnbelop-i-folketrygden-fra-1.-mai-2026/
- Forsikring mot arbeidsgiverperioden (§ 8-21) er tilgjengelig for små arbeidsgivere (lønn ≤ 40 G).
- Kilder: https://lovdata.no/lov/1997-02-28-19/§8-19 og https://lovdata.no/lov/1997-02-28-19/§8-10

### 6.3 Permittering, AAP og andre ytelser
- **Permittering, masseoppsigelse og innskrenkning** meldes via **skjema på nav.no**. Det krever en egen Altinn-delegering. **Ingen API er identifisert** [V for skjema, S for detaljer].
- Permittering skal rapporteres i a-meldingen (permisjon/permittering per arbeidsforhold) uansett lengde [S].
- Feil avslutning av arbeidsforhold ved streik gir konsekvenser hos NAV (Skatteetaten-nyhet 22.05.2026) [V, RSS].
- **AAP:** Ingen eget arbeidsgivergrensesnitt er identifisert [IV].

### 6.4 NAV og Altinn II [V]
- NAV flyttet arbeidsgivertjenester til nav.no og API-er. Oppgjørsrapport K27 ble sendt i gammel løsning til 15.06.2026.
- Alle NAV-tjenester mister Altinn II-roller **01.12.2026** (info.altinn.no).

---

## 7. Trekkpålegg (utleggstrekk) – elektroniske kanaler

### 7.1 Skatteetaten – Trekkpålegg-API [V]
- **Nytt regelverk fra januar 2026 med gradvis overgang.** Etter nye regler har en ansatt bare **ett samordnet utleggstrekk**, som kan dekke flere krav. Trekk etter gamle regler løper videre i flere år.
- Påleggsgivere er Skatteetaten, alminnelig namsmann og kommunene.
- **A-meldingskoder:**
  - `utleggstrekkSamordnet` (nye regler) og `utleggstrekkSkatt` (gamle regler, skattekrav). De skal ikke blandes.
  - Begge rapporteres med lønnsutbetalingsdato.
  - Skatteetaten varslet 24.02.2026 om utbredt feilrapportering av disse kodene.
- **API:**
  - REST/JSON. Scope `skatteetaten:trekkpaalegg`, systembruker-ressurs `ske-informasjon-om-trekkpaalegg`.
  - `GET /api/trekkpaalegg/v1` med `fraSekvensnummer`/`maksAntall` for inkrementell henting, og `GET /api/trekkpaalegg/v1/{trekkid}/{trekkversjon}`.
  - Produksjon: `https://api.skatteetaten.no/api/trekkpaalegg/v1`. Test: `https://api-test.sits.no`.
  - Det er polling i dag. Varsling via Dialogporten er planlagt eller valgfri.
  - Pålegget inneholder trekkstatus (aktiv/avsluttet), perioder, beløp/prosent, KID og kontonummer.
- **Krav før produksjon (strengere enn a-meldingen):**
  - Testtilgang bestilles på e-post (fremtidensinnkreving@skatteetaten.no).
  - Testdata opprettes av Skatteetaten på syntetiske Tenor-virksomheter.
  - Leverandøren må levere en **testoppsummering**: «Du får ikke tilgang til produksjonsmiljø før dette er gjennomført».
  - **Avtale om bruksvilkår signeres** ved produksjonstilgang.
- Kilder:
  - https://skatteetaten.github.io/api-dokumentasjon/api/trekkpaalegg (Swagger: https://app.swaggerhub.com/apis/skatteetaten/trekkpaalegg-app/1.4)
  - https://www.skatteetaten.no/om-skatteetaten/fremtidens-innkreving/systemleverandorer/lonns--og-personalsystem/
  - https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/feil-rapporteringer-i-a-meldingen-knyttet-til-bruk-av-ny-kode-utleggstrekksamordnet/

### 7.2 Andre påleggsgivere
- **NAV (bidragstrekk/NAV Innkreving):** Elektronisk kanal og status er **ikke verifisert** i denne runden [IV].
- **Statens innkrevingssentral:** Organisatorisk status og kanal for trekkpålegg er **ikke verifisert** [IV]. Skatteetatens side nevner Skatteetaten, alminnelig namsmann og kommuner.
- Konsekvens: Lønnssystemet må i overgangsperioden håndtere *både* API-baserte pålegg og pålegg mottatt som brev (Altinn-innboks/papir) med manuell registrering.

---

## 8. Feriepenger, OTP og yrkesskadeforsikring

### 8.1 Feriepenger (ferieloven) [V]
- **Sats 10,2 %** av feriepengegrunnlaget (arbeidsvederlag i opptjeningsåret, uten feriepenger, utgiftsgodtgjørelser og naturalytelser).
- Arbeidstakere **over 60 år** med rett til ekstraferie får **+2,3 prosentpoeng**. Dette tillegget gis ikke for den delen av grunnlaget som overstiger **6 G** (§ 10 nr. 3: «Feriepenger etter første ledd ytes ikke for den del …»). Tolkningen er at taket gjelder tillegget; anbefalt kontrollert mot forarbeider.
- Utbetaling skjer siste vanlige lønningsdag før ferien, og alt utbetales ved fratreden (§ 11).
- Grunnlaget skal fremgå av en sammenstilling til arbeidstakeren.
- Høyere satser (12 %, femte ferieuke) følger av tariff og avtale, ikke loven.
- **Systemkrav:**
  - Avsetning per ansatt.
  - Støtte for tariffsatser og 60+.
  - Ferietrekk i juni (trekk i lønn for ferie).
  - Trekkfrie feriepenger i forskuddstrekket (kap. 3).
  - Korrekt a-meldingsrapportering. Skatteetaten presiserte 08.06.2026 at *hele* beløpet som utbetales som feriepenger skal oppgis som feriepenger, uavhengig av beregningsmåte.
- **Endringer:** Departementets utredning av nytt opptjeningssystem (Moum-rapporten, høringsfrist 21.10.2024) er ferdigbehandlet som høring. **Ingen vedtatt eller fremmet lovendring for 2026/2027 er funnet** [V/IV – ikke funnet].
- Kilder:
  - https://lovdata.no/lov/1988-04-29-21/§10
  - https://www.regjeringen.no/no/dokumenter/horing-utredning-av-ferielovens-system-for-opptjening-av-feriepenger/id3046142/
  - https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/hvordan-oppgi-feriepenger-i-a-meldingen/

### 8.2 Obligatorisk tjenestepensjon (OTP)
- **Minstekrav:** innskudd minst **2 % av lønn opp til 12 G** (OTP-loven § 4) [V].
- **Omfattede foretak** (§ 1) har minst én av følgende [V]:
  - minst 2 personer med minst 75 % stilling
  - 1 arbeidstaker uten eierinteresse med minst 75 % stilling
  - flere personer med minst 20 % stilling som til sammen utgjør minst 2 årsverk
- Ordningen må opprettes innen 6 måneder (§ 2) [V].
- **«Fra første krone og første dag»:** Innført med virkning **2022**, ikke 2023 som oppdraget antydet. Foretak måtte tilpasse seg innen 30.06.2022, og 13-åringer har opptjening fra 01.07.2022. Datoene er [S] (regjeringen/Revisorforeningen/DNB) og ikke lest i endringslovens tekst. **Et forslag om å øke minstesatsen fra 2 til 4 %** ble behandlet i Stortinget i 2026 (Innst. 263 S (2025–2026)), men utfallet er **ikke verifisert** [IV].
- **Rapportering:**
  - Private arbeidsgivere omfattet av OTP skal oppgi **pensjonsinnretning** i a-meldingen (fra 2021). Det gir egen avviksmelding hvis den mangler [S/V].
  - Pensjonsinnretninger henter data fra a-ordningen via Skatteetatens API-er *Inntektsmottakere* og *Tjenestepensjonsavtale*. Disse krever lovhjemmel og er **ikke tilrettelagt for systembruker/LPS** [V].
  - I tillegg krever mange leverandører fortsatt egne lønnsfiler eller portalrapportering. Det finnes en bransjestandard fra Finans Norge [S]. Format er **leverandørspesifikt og ikke kartlagt** [IV].
- Kilder:
  - https://lovdata.no/lov/2005-12-21-124/§4
  - https://skatteetaten.github.io/api-dokumentasjon/api/inntektsmottakere
  - https://skatteetaten.github.io/api-dokumentasjon/api/tjenestepensjonsavtale

### 8.3 Yrkesskadeforsikring [V]
- Arbeidsgiver **plikter å tegne yrkesskadeforsikring** (yrkesskadeforsikringsloven § 3). Staten er unntatt. Brudd kan straffes (§ 19).
- Loven har **ingen rapporteringsplikt for lønnssystemet**. Premie er typisk lønnsavhengig, men det er avtalespørsmål.
- Kilde: https://lovdata.no/lov/1989-06-16-65/§3

---

## 9. Annen rapportering

### 9.1 SSB
- Lønnsstatistikk, sysselsetting m.m. baseres på a-meldingen (se 2.10). Det finnes ingen egen rapportering fra lønnssystemet [V].
- **Sykefraværsstatistikk:** Ingen egen arbeidsgiverrapportering er identifisert. Statistikken antas å bygge på NAVs sykmeldingsregister og a-ordningen [IV].

### 9.2 Likestillings- og diskrimineringsloven §§ 26 og 26 a [V]
- **Aktivitetsplikt for alle arbeidsgivere.**
- **Kartleggingsplikt** gjelder alle offentlige virksomheter og private virksomheter som *jevnlig sysselsetter mer enn 50 ansatte*. For private med 20–50 ansatte gjelder den når en av partene krever det.
- Kartleggingen omfatter blant annet **lønn fordelt på kjønn annethvert år** og **ufrivillig deltid**. Den skal dokumenteres i samarbeid med de ansattes representanter.
- **Redegjørelse** gis i årsberetningen eller et annet offentlig dokument. Lønnskartleggingen skal fremgå **anonymisert**, med innsynsrett for blant annet ansatte og ombudet under taushetsplikt.
- **Systemkrav:** rapport for lønn per kjønn, stillingskategori og nivå, deltid/ufrivillig deltid, anonymisering (minste gruppestørrelse), periodisitet og eksport.
- **EU-direktivet om lønnstransparens (2023/970):** EU-fristen var 07.06.2026. Direktivet er EØS-relevant, men **ikke innlemmet i EØS-avtalen**. Departementet arbeider med gjennomføring [S, Virke/Altinget]. Det er sannsynlig at det kommer krav om lønnsgap-rapportering i 2027–2028, så datamodellen bør forberedes.
- Kilde: https://lovdata.no/lov/2017-06-16-51/§26

### 9.3 Offentlige pensjonsordninger (SPK/KLP)
- **SPK:** Medlemsdata rapporteres **månedlig**, primært via portalen «Min virksomhet», eller fra **godkjente lønnssystemer** etter SPKs *kravspesifikasjon for elektronisk overføring av medlemsdata* (sist sett v2.7). Feltene er blant annet fødselsnummer, stillingskode, stillingsprosent, lønn/lønnstrinn, tillegg og permisjonskode [S]. Det kreves **godkjenning av lønnssystemet**, en egen sertifiseringsprosess hvis offentlig sektor er målgruppe. Kilde: https://www.spk.no/globalassets/virksomhet/bilder-og-illustrasjoner/kravspesifikasjon-v.2.7-.pdf [S]
- **KLP:** Rapportering via «Kundeside» med lønnsfil fra lønnssystemet (format KLP-spesifikt) [S]. Kilde: https://www.klp.no/virksomhet/pensjon/hr-lonn-og-personal/rapportering-av-ansattopplysninger
- SPK mister Altinn II-roller 31.12.2026 [V].

---

## 10. Bokføring, dokumentasjon, lønnsslipp og oppbevaring

### 10.1 Lønnsslipp – arbeidsmiljøloven § 14-15 [V]
- Ved utbetaling, eller umiddelbart etter, skal arbeidstaker få **skriftlig oppgave over beregning av lønn, grunnlaget for feriepenger og foretatte trekk** (sjette ledd, ikke femte).
- Lønn utbetales minst to ganger i måneden, med mindre annet er avtalt, og som kontantlønn til konto.
- **Trekk i lønn** er bare tillatt etter uttømmende liste (lov, pensjonsandel, skriftlig forhåndsavtale, tariff, erstatning med vilkår, streik/lockout), med eksistensminimumsvern for bokstav c, e og f.
- Kilde: https://lovdata.no/lov/2005-06-17-62/§14-15

### 10.2 Bokføringsforskriften [V]
- **§ 5-6 Dokumentasjon av lønn:**
  - Per motpart: lønn og oppgavepliktige ytelser, forskuddstrekk og utleggstrekk, fødselsnummer, navn og tabellnummer eller trekkprosent.
  - For utleggstrekk: når pålegget er mottatt og trekkprosent eller beløp.
  - Per periode: utbetalingsdato, brutto, naturalytelser, fradrag, trekkgrunnlag og trekk.
  - For timelønnede: timer per dag og samlet for perioden.
  - Dokumentasjonen utstedes senest når ytelsen kan utbetales.
  - **Det skal finnes en lettfattelig beskrivelse av lønnssystemets oppbygging og funksjoner.** Dette er et leveransekrav til oss som leverandør.
- **§ 3-1 første ledd nr. 9:** Lønnsopplysningspliktige ytelser spesifiseres per periode etter kontoene i regnskapssystemet. AGA-pliktige ytelser skal kunne vises samlet per sats og sone.
- Kilde: https://lovdata.no/forskrift/2004-12-01-1558

### 10.3 Oppbevaring – bokføringsloven § 13 [V]
- **5 år:** regnskapsrapportering, spesifikasjoner og dokumentasjon av bokførte opplysninger (nr. 1–4).
- **3 år og 6 måneder:** avtaler, korrespondanse, pakksedler og prislister (nr. 5–8).
- **Elektronisk tilgjengelighet i 3,5 år** (§ 13 b).
- **Oppbevaring «i Norge»**, med unntak gitt ved forskrift eller enkeltvedtak. Unntakene (for eksempel elektronisk oppbevaring i EØS) er **ikke gjennomgått i denne runden [IV] og er kritiske for SaaS-hosting.**
- **Lovendring 19.06.2026 nr. 39** (Prop. 44 L (2025–2026)), med ikrafttredelse delvis 01.01.2027 og 01.01.2030:
  - Ny definisjon av «elektronisk regnskapssystem».
  - Krav om at bokføring skal skje i elektronisk regnskapssystem (§ 7, 2030).
  - E-faktura mellom bokføringspliktige (2027).
  - § 13 videreført med «i Norge» og nytt krav om at e-faktura oppbevares i originalformat.
  - Lønnssystemet berøres indirekte via posteringer til regnskapssystemet.
- Kilder:
  - https://lovdata.no/lov/2004-11-19-73/§13
  - https://lovdata.no/dokument/LTI/lov/2026-06-19-39
  - https://www.regjeringen.no/no/aktuelt/nye-lovregler-om-e-fakturering-i-naringslivet-og-enkelte-andre-lovendringer-pa-finansmarkedsomradet-settes-i-kraft/id3166726/
- **Spenning mot GDPR:** Lønnsdata må slettes når formålet er borte, men bokføringsplikten krever 5 år. Slettepolicy må skille mellom regnskapsdokumentasjon og HR-data (se kap. 11).

### 10.4 SAF-T
- **SAF-T Regnskap v1.30** kreves fra 01.01.2025 for bokføringspliktige med digitale regnskapsopplysninger, og leveres på forespørsel [S]. Den omfatter hovedbok og kunde-/leverandørreskontro.
- **Ingen egen SAF-T for lønn er identifisert.** Lønnsposteringer inngår via hovedboken i regnskapssystemet.
- Lønnssystemet må levere posteringer med kontoplan- og standardkontomapping, dimensjoner og bilagsreferanser som gjør regnskapssystemets SAF-T-eksport korrekt.
- SAF-T 2.0-prosjekt pågår (planlagt ferdig 31.12.2026) [S].
- Kilde: https://www.skatteetaten.no/en/business-and-organisation/start-and-run/best-practices-accounting-and-cash-register-systems/saf-t-financial/

---

## 11. GDPR og personvern spesifikt for lønn

- **Rollefordeling:** Kunden (arbeidsgiver) er behandlingsansvarlig. Lønnssystemleverandøren er **databehandler**, noe Skatteetatens bruksvilkår også forutsetter [V].
  - Det krever **databehandleravtale** etter GDPR art. 28 og oversikt over underdatabehandlere.
  - For byrå-scenariet blir byrået typisk databehandler for klienten og vi *underdatabehandler*. Kjeden må avtales.
- **Særlige kategorier (art. 9):**
  - **Helseopplysninger** omfatter sykefravær, sykmeldinger og inntektsmeldinger. NAV-pakken heter nettopp `lonn-personopplysninger-saerlig-kategori`.
  - **Fagforeningsmedlemskap** avdekkes av trekk av kontingent.
  - Arbeidsgiver kan be om opplysninger om *arbeidsevne*, ikke diagnose.
  - Lønnsopplysninger til fagforening bør gis på gruppenivå hvis det ikke er særskilt behov [V Datatilsynet].
  - **Systemkrav:** egne tilgangsroller for fravær og helse, minimering (ikke lagre diagnose), logging av innsyn og kryptering.
- **Sletting:** Datatilsynet sier at opplysninger kun skal lagres så lenge det er nødvendig, men at bokføringsloven kan kreve lengre oppbevaring [V]. Det krever differensierte slettefrister: 5 år og 3,5 år for regnskapsmateriale, kortere for helse og egenmelding.
  - Kilde: https://www.datatilsynet.no/personvern-pa-ulike-omrader/personvern-pa-arbeidsplassen/
- **Tredjelandsoverføring og Schrems II:**
  - EU-US Data Privacy Framework gjelder for selvsertifiserte amerikanske virksomheter.
  - Datatilsynet (oppdatert **01.07.2026**) peker på at PCLOB ikke er beslutningsdyktig og på høyesterettsavgjørelsen *Trump v. Slaughter* (29.06.2026). Tilsynet **anbefaler en beredskapsplan** og advarer om at amerikanske skytjenester «på europeisk jord» også kan bli berørt, uten overgangsperiode ved oppheving [V].
  - Kilde: https://www.datatilsynet.no/aktuelt/aktuelle-nyheter-2025/informasjon-om-overforinger-til-usa/
  - **Anbefaling:** Velg EØS-region og helst leverandører uten US-jurisdiksjon for primærdata, eller ha en dokumentert exit-plan. Det må uansett ses sammen med kravet om oppbevaring i Norge (10.3).
- **Testdata:** Skatteetaten og NAV krever **kun syntetiske testdata**. Produksjonsdata i test er ikke tillatt [V].
- **DPIA:** Behandling av helse og fagforening i stor skala for mange arbeidsgivere tilsier at en vurdering av personvernkonsekvenser (art. 35) bør gjennomføres. Dette er en faglig vurdering, ikke en kildeverifisert plikt.
- **Skattekortoppslag varsler den ansatte.** Oppslagslogikken må styres av ansettelsesstatus (se 3.1).

---

## 12. Varslede endringer 2026 → 2028

| Når | Endring | Konsekvens for systemet | Status / kilde |
|---|---|---|---|
| 01.01.2026 | Skattetrekkskonto avviklet. Forskuddstrekk og utleggstrekk forfaller første virkedag etter lønn. KID med månedsperiode | Betalingsmodul og KID-generator | Vedtatt, i kraft [V] |
| Jan. 2026 | Nytt regelverk for samordnet utleggstrekk, ny a-meldingskode og Trekkpålegg-API | Ny trekktype, API-integrasjon | I kraft, gradvis [V] |
| 31.05 / 15.06.2026 | Altinn II-tjenester for a-melding og skattekort stengt | Nye API-er obligatoriske | Gjennomført [V] |
| 10.2026 | Forretningsregel F529 (0 % stilling + fastlønn) som retningslinje | Validering før innsending | I kraft [V] |
| 17.11.2026 | A-melding og skattekort ikke via Altinn II-roller | Kunder/byråer må ha tilgangspakker | [V] |
| 01.12.2026 | NAV-tjenester ikke via Altinn II-roller | Samme | [V] |
| 15.12.2026 | Skattekort-API: Dialogporten fjernes (kun polling), to nye `resultatForSkattekort`-verdier | Kodeendring før årsskiftet | [V] |
| Des. 2026 | Ny trekkrutine 2027 og trekktabeller forventes, og skattekort 2027 hentes | Årlig release | Forventet ut fra mønster [S] |
| 31.12.2026 | Alle Altinn II-roller opphører | – | [V] |
| 01.01.2027 (periode 2027-01) | Ny forretningsregel **F532** (sum forskuddstrekk per lønnsutbetalingsdato kan ikke være negativ, nivå «øyeblikkelig», erstatter F277-2), **F530** (privat arbeidsgiver med f-nummer kan ikke rapportere seg selv) og ny inntektsbeskrivelse «jobbsjansen» | Validering og kodeliste | Besluttet av a-ordningen [V] |
| 01.01.2027 | Statsbudsjett 2027 (forslag 07.10.2026): trygdeavgift lønn **7,4 %** (fra 7,6), personfradrag **120 180**, trinn 1–5: 235 150 / 331 050 / 754 050 / 1 019 300 / 1 525 900 (satser uendret), minstefradrag maks 99 550, fagforeningsfradrag 8 950, AGA uendret, PAYE 25 % | Nye konstanter. Trekkrutine 2027 | **Forslag**, vedtak ventet etter 14.12.2026 [V] |
| 01.01.2027 | **Ny firmabilmodell:** fordel = 20 % av listepris som ny + fast årlig kostnadskomponent (elbil 16 200, bensin 39 700, diesel 28 100, ladbar hybrid 22 400). Forskrift fastsettes etter budsjettvedtaket | Ny beregning av naturalytelse og ny datamodell (motortype) | **Forslag** (Prop. 1 LS (2026–2027) kap. 3.2) [V] |
| 01.01.2027 / 2030 | Bokføringsloven: e-faktura (2027), elektronisk regnskapssystem (2030) | Indirekte | Vedtatt [V] |
| 01.05.2027 | Spesifikasjon for **a-melding v2.4** publiseres (senest) | Planlegg utvikling | [V] |
| 15.09.2027 | Testmiljø for v2.4 klart | – | [V] |
| 01.01.2028 (periode 2028-01) | **A-melding v2.4 i produksjon** | Ny XSD/modell | [V] |
| Uavklart | EU-direktivet om lønnstransparens i EØS/norsk rett | Lønnsgap-rapportering | Ikke innlemmet [S] |
| Uavklart | OTP-minstesats 2 → 4 % | Pensjonsberegning | Ikke verifisert [IV] |
| Uavklart | Nytt opptjeningssystem for feriepenger | Feriepengemotor | Ingen lovforslag funnet |

**Kilder statsbudsjett 2027:**
- https://www.regjeringen.no/no/tema/okonomi-og-budsjett/skatter-og-avgifter/skatte-og-avgiftssatser/skattesatser-2027/id3173438/ (publisert 07.10.2026)
- https://www.regjeringen.no/no/statsbudsjett/2027/statsbudsjettet-2027-skatter-og-avgifter/statsbudsjettet-2027-provenyvirkninger-av-skatte-og-avgiftsendringer-for-2027/id3173279/
- Skatteetatens presentasjon til LPS 22.10.2026: https://www.skatteetaten.no/contentassets/91b8e194f12e4acb86d75259ec55c3e5/2026-10-02---statsbudsjett-2027-.pdf
- Sekundærkilde: https://www.sticos.no/fagstoff/statsbudsjettet-2027 [S]

**Kilde a-ordningen 2027/2028:** https://www.skatteetaten.no/contentassets/91b8e194f12e4acb86d75259ec55c3e5/2026-10-01---informasjon-fra-a-ordningen-22-10.pdf

**Årshjul for nye a-meldingsversjoner (Skatteetaten):**
- Desember år 1: varsel.
- 01.04: endelig innhold.
- 01.05: spesifikasjon.
- 01.09: veiledninger.
- 15.09: testmiljø.
- 01.12: IT ferdig.
- 01.01: produksjon.

---

## 13. Grensesnitt → krav → status 2026 → kilde

| # | Grensesnitt | Eier | Protokoll / autentisering | Test- og godkjenningskrav før produksjon | Status okt. 2026 | Frister og endringer | Kilde |
|---|---|---|---|---|---|---|---|
| 1 | Maskinporten | Digdir | OAuth2 JWT-grant, virksomhetssertifikat/nøkkel | Signerte Digdir-vilkår. Testklient i selvbetjening | Produksjon | – | https://samarbeid.digdir.no/maskinporten/dette-er-maskinporten/96 |
| 2 | Altinn 3 systemregister, systembruker og klientdelegering | Digdir | REST. Scopes `altinn:authentication/*` (bestilles hos Digdir) | TT02. Kunde godkjenner forespørsel | Produksjon | Altinn II-roller ut 31.12.2026 | https://docs.altinn.studio/nb/authorization/guides/system-vendor/system-user/ |
| 3 | Dialogporten og Altinn Events | Digdir | REST, `digdir:dialogporten`, `altinn:events.subscribe` | TT02 | Produksjon | Skatteetaten endret transmission-URL-er mai 2026 | https://samarbeid.digdir.no/altinn/hvordan-hente-meldinger-gjennom-dialogporten/2869 |
| 4 | A-melding innsending (REST og filopplasting) | Skatteetaten | REST/JSON-innpakning av v2.3-XML. `skatteetaten:innrapporteringamelding` + systembruker. idempotencyKey | Bruksvilkår, søknad om scope, test i delt testmiljø og TT02, syntetiske data. Ingen sertifisering | Produksjon (REST og fil, sistnevnte fra 09.04.2026). Eneste systemkanal | Frist den 5. Ny regel F532/F530 2027-01. v2.4 2028-01 | https://skatteetaten.github.io/api-dokumentasjon/api/innrapportering-amelding |
| 5 | A-melding tilbakemelding | Skatteetaten (+ Dialogporten) | REST + Dialogporten-hendelser | Som 4 | Produksjon | Bruk `consumerType: Api`-URL | https://app.swaggerhub.com/apis/skatteetaten/amelding-tilbakemelding-api/ |
| 6 | Avstemmingsrapport (erstatter A06/A07) | Skatteetaten | REST, samme scope | Som 4 | Produksjon fra 03.06.2026, ny versjon 11.09.2026 | – | https://skatteetaten.github.io/api-dokumentasjon/api/amelding-avstemmingsrapport |
| 7 | Manuell XML-opplasting av a-melding (reserve) | Skatteetaten | Nettportal (ID-porten) | Systemet må eksportere gyldig XML | Produksjon | Overgangsløsning, sluttdato ikke oppgitt | https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/viktig-sikre-stotte-for-manuell-innsending-av-amelding-via-xml-i-overgangsperioden/ |
| 8 | Skattekort til arbeidsgiver | Skatteetaten | REST (JSON/XML). `skatteetaten:skattekorttilarbeidsgiver` + systembruker. Polling | Som 4. Testpersoner 2026 | Produksjon fra 30.10.2025 | 15.12.2026: kun polling og nye responsverdier. Hentes i desember for nytt år | https://skatteetaten.github.io/api-dokumentasjon/api/skattekorttilarbeidsgiver |
| 9 | Skattekort via portal-filopplasting (reserve) | Skatteetaten | Portal (ID-porten), RF-1211-XML | – | Produksjon | Parallell med API | https://skatteetaten.github.io/api-dokumentasjon/anvendelsesomraader/skattekorttilarbeidsgiver |
| 10 | Trekkrutine og trekktabeller | Skatteetaten | Java-kildekode (GitHub) og tekstfil (zip) | Ingen. **Lisens uavklart** | 2026-versjon publisert 08.12.2025 | 2027-versjon forventes desember 2026 | https://github.com/Skatteetaten/trekktabell · https://www.skatteetaten.no/satser/trekktabeller-i-tekstformat/?year=2026 |
| 11 | Innbetaling av forskuddstrekk, AGA og utleggstrekk | Skatteetaten (via bank) | Bankbetaling med 19-sifret KID | – | Ny ordning fra 01.01.2026 | Forskuddstrekk første virkedag etter lønn. AGA annenhver måned den 15. | https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/arbeidsgiveravgift/betaling-av-forskuddstrekk-og-arbeidsgiveravgift/ |
| 12 | Trekkpålegg (samordnet utleggstrekk) | Skatteetaten | REST/JSON. `skatteetaten:trekkpaalegg` + ressurs `ske-informasjon-om-trekkpaalegg`. Polling | **Testoppsummering kreves før produksjonstilgang.** Signert avtale | Produksjon (prod-URL publisert). Gamle brev løper parallelt | Event-varsling planlagt | https://skatteetaten.github.io/api-dokumentasjon/api/trekkpaalegg |
| 13 | Krav og betalinger / Frister (valgfritt) | Skatteetaten | REST + systembruker | Som 4 | Lansert 18.03 / 08.05.2026 | – | RSS: https://www.skatteetaten.no/rss/sbs/a-meldingen/ |
| 14 | NAV inntektsmelding sykepenger, sykmelding og søknad til arbeidsgiver | NAV | REST/JSON. `nav:helseytelser/sykepenger` + systembruker (token ikke vekslet) | Test i dev (`*.ekstern.dev.nav.no`) og TT02. Bruksvilkår og kontaktinfo til NAV | Produksjon | – | https://github.com/navikt/sykepenger-im-lps-api/wiki |
| 15 | NAV inntektsmelding foreldrepenger og svangerskapspenger | NAV | REST. `nav:inntektsmelding/foreldrepenger` | Som 14 | Produksjon ifølge API-oversikt (**motstrid** med arbeidsgiverside) | – | https://github.com/navikt/fp-inntektsmelding-api/wiki |
| 16 | NAV inntektsmelding «sykdom i familien» + refusjon omsorgspenger | NAV | REST. `nav:inntektsmelding/sif` | Som 14 | Produksjon ifølge API-oversikt (**motstrid**) | – | https://github.com/navikt/k9-inntektsmelding-api/wiki |
| 17 | NAV oppgjørsrapporter (refusjon) | NAV | REST. `nav:utbetaling/oppgjorsrapporter` | Som 14 | Produksjon. K27 i Altinn II stengt 15.06.2026 | – | https://github.com/navikt/sokos-oppgjorsrapporter/wiki |
| 18 | NAV sykefraværsoppfølging (dokumentporten, oppfølgingsplan, nærmeste leder) | NAV | REST. `nav:syfo/dokumentporten` m.fl. | Som 14 | Produksjon | Relevant for HR-modul | https://www.nav.no/samarbeidspartner/ekstern-datautveksling/api-oversikt |
| 19 | NAV permittering og masseoppsigelse | NAV | Skjema på nav.no (ingen API funnet) | – | Manuell | – | https://www.nav.no/arbeidsgiver/permittere-nedbemanne |
| 20 | Pensjonsleverandør (OTP) | Den enkelte leverandøren | Felt i a-meldingen + leverandørspesifikke filer/portaler | Avtale per leverandør | Varierer [IV] | Mulig 4 %-minstesats [IV] | https://lovdata.no/lov/2005-12-21-124/§4 |
| 21 | SPK medlemsdata | SPK | Fil etter SPK-kravspesifikasjon (v2.7 sist sett) eller portal | **Godkjenning av lønnssystem** [S] | Produksjon [S] | Altinn II-roller ut 31.12.2026 | https://www.spk.no/globalassets/virksomhet/bilder-og-illustrasjoner/kravspesifikasjon-v.2.7-.pdf |
| 22 | KLP | KLP | Kundeside, lønnsfil | KLP-spesifikk [S] | [S] | – | https://www.klp.no/virksomhet/pensjon/hr-lonn-og-personal/rapportering-av-ansattopplysninger |
| 23 | SSB-statistikk | SSB (via a-ordningen) | Ingen egen kanal | – | Via a-melding | v2.4 2028 | https://skatteetaten.github.io/api-dokumentasjon/anvendelsesomraader/ameldingen |
| 24 | Likestillingsredegjørelse | Ingen myndighetsmottak (årsberetning) | Rapport/eksport | – | Gjeldende lov | EU-direktivet om lønnstransparens uavklart | https://lovdata.no/lov/2017-06-16-51/§26 |
| 25 | SAF-T Regnskap | Skatteetaten (via regnskapssystemet) | XML v1.30 | – | Krav fra 2025 | SAF-T 2.0 under arbeid [S] | https://www.skatteetaten.no/en/business-and-organisation/start-and-run/best-practices-accounting-and-cash-register-systems/saf-t-financial/ |
| 26 | Testdata (Tenor) og TT02 | Skatteetaten / Digdir | Nettportal/API | Kun syntetiske data | Produksjon | – | https://www.skatteetaten.no/testdata/ · https://samarbeid.digdir.no/altinn/kom-i-gang-i-testmiljoet-tt02/2868 |

---

## 14. Risikoer for en ny leverandør

1. **Ledetid for onboarding.** Følgende må på plass før første kunde kan rapportere:
   - Digdir-scopes som ikke er allment tilgjengelige (systemregister og systembruker-forespørsel).
   - Skatteetaten-scopes via brukerstøttetjenesten, som selv krever tilgang.
   - Avtale og testoppsummering for trekkpålegg.
   - Registrering av kontaktinfo hos NAV.
   - Godkjenning hos SPK hvis offentlig sektor er målgruppe.

   Steget «tilpass systemet for kundene» (systembrukeroppsett per kunde) er ifølge Skatteetaten det som tar lengst tid.
2. **Byrå-modellen er ny.** Systembruker for klientsystem støtter kun tilgangspakker. Byråets klientadministrator må knytte klienter, og klientforhold som opphører fjerner tilgang automatisk. Onboarding-UX og feilsøking (403/`AMLD_1063`) må bygges godt. Overgangsfasen fram til 31.12.2026 gir mange tilgangsfeil i markedet.
3. **Umoden og raskt skiftende plattform.** Eksempler fra 2026:
   - Dialogporten-URL-er endret.
   - JSON-feil i tilbakemelding.
   - Skattekortendringer kunne mangle.
   - Bruksmønster for skattekort endres 15.12.2026.
   - Avstemmings-API i ny versjon etter tre måneder.

   Abonnement på RSS (`/rss/sbs/alle/`), statusside og Slack (Skatteetaten) er nødvendig. Normale brytende endringer varsles bare med 4 måneders frist.
4. **Årlig hard deadline i desember og januar.** Trekkrutine og trekktabeller publiseres rundt 8. desember. Skattekort for nytt år hentes i desember. Budsjettvedtak skjer etter 14. desember (for eksempel firmabilforskrift). Forretningsregler fra 01.01. Det krever beredskap for release i romjulen.
5. **Lisens på trekkrutinen.** Skatteetatens Java-kode har ingen lisensfil. Det må avklares, eller algoritmen må implementeres selv og verifiseres mot de offisielle tabellene.
6. **Betalingsflyt endret.** Skattetrekk forfaller dagen etter *hver* lønnskjøring og må betales som eget oppdrag med KID. Feil gir straffbar for sen betaling hos kunden. Bankintegrasjon (pain.001) og avstemming mot «Krav og betalinger» bør være kjernefunksjonalitet.
7. **Sanksjonsrisiko for kunder.** Tvangsmulkt (opptil 1 000 rettsgebyr per periode) og nye øyeblikkelige forretningsregler (F532 fra 2027) gjør robust forhåndsvalidering mot gjeldende forretningsregler og kodelister nødvendig.
8. **Hosting og jurisdiksjon.** Bokføringsloven krever oppbevaring i Norge (unntak ikke kartlagt), og Datatilsynet anbefaler beredskap for US-overføringer. Valg av skyleverandør og region må juridisk avklares tidlig.
9. **Særlige kategorier personopplysninger.** NAV-integrasjonene gir helseopplysninger, og fagforeningstrekk avslører medlemskap. Det krever tilgangsstyring, logging, DPIA og databehandleravtale-kjede (kunde, byrå, oss).
10. **Uavklarte NAV-kanaler.** Motstrid om hvorvidt foreldrepenger/svangerskapspenger og «sykdom i familien» kan sendes fra LPS. Bidragstrekk og eventuelle andre påleggsgivere er ikke kartlagt.
11. **Versjonsskifte i 2028** (a-melding v2.4). Arkitekturen bør abstrahere meldingsmodellen og støtte parallelle versjoner, fordi korrigering av eldre perioder skal skje i gjeldende format. Hvordan korrigering av 2027-perioder etter overgangen skal skje er **ikke verifisert**.

---

## 15. Ikke verifisert / anbefalt oppfølging

- Frist og hjemmel for **sammenstillingsoppgave** til inntektsmottaker (antatt 31. januar).
- **Unntak fra kravet om oppbevaring i Norge** (bokføringsforskriften) for SaaS i EØS.
- **Egenmelding:** eventuelle regelendringer i 2025–2026.
- **NAV bidragstrekk** og eventuelle andre påleggsgiveres elektroniske kanaler, samt Statens innkrevingssentrals status.
- **OTP:** utfall av forslaget om 4 % og eksakte ikrafttredelsesdatoer for «første krone/13 år» i lovtekst.
- **Utenlandske arbeidstakere:** detaljregler for AGA og trygdetilhørighet 2026.
- **Full KID-algoritme** (kontrollsiffer, posisjon 18–19) for forskuddstrekk og AGA.
- **SPK/KLP:** gjeldende versjon av spesifikasjoner og godkjenningsprosess.
- **Frikortgrense 2027** og **PAYE-inntektsgrense 2027.** Grensen antas lik trinn 3 = 754 050, men det er avledet og ikke bekreftet.
- **Sykefraværsstatistikk:** bekreft at ingen egen rapportering kreves.
- **Endelig vedtak av statsbudsjett 2027** (forventet medio desember 2026), inkludert firmabilforskriften.

---

## 16. Kildeliste (hovedkilder)

**Skatteetaten**
- https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/a-meldingen-sbs/
- https://skatteetaten.github.io/api-dokumentasjon/api/innrapportering-amelding
- https://skatteetaten.github.io/api-dokumentasjon/api/amelding-avstemmingsrapport
- https://skatteetaten.github.io/api-dokumentasjon/api/skattekorttilarbeidsgiver
- https://skatteetaten.github.io/api-dokumentasjon/api/trekkpaalegg
- https://skatteetaten.github.io/api-dokumentasjon/om/systembruker
- https://skatteetaten.github.io/api-dokumentasjon/test/tenor
- https://www.skatteetaten.no/samarbeidspartnere/reetablering-altinn/systemleverandor/
- https://www.skatteetaten.no/samarbeidspartnere/reetablering-altinn/systemleverandor/oppkobling/
- https://www.skatteetaten.no/samarbeidspartnere/reetablering-altinn/regnskapsforer-revisor/
- https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/bruksvilkar/
- https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/frist-altinn3-forlenges/
- https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/altinn-ii-stenges-15.-juni/
- https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/nye-tilgangspakker-for-a-meldingen/
- https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/arbeidsgiveravgift/betaling-av-forskuddstrekk-og-arbeidsgiveravgift/
- https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/forskuddstrekk-betalingsoppdrag-og-kid/
- https://www.skatteetaten.no/om-skatteetaten/fremtidens-innkreving/systemleverandorer/lonns--og-personalsystem/
- https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/
- https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/
- https://www.skatteetaten.no/satser/trekktabeller-i-tekstformat/?year=2026
- https://github.com/Skatteetaten/trekktabell
- https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/endret-bruksmonster-for-henting-av-skattekort/
- https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/to-nye-responsverdier-i-resultatforskattekort/
- https://www.skatteetaten.no/contentassets/91b8e194f12e4acb86d75259ec55c3e5/2026-10-01---informasjon-fra-a-ordningen-22-10.pdf
- https://www.skatteetaten.no/contentassets/91b8e194f12e4acb86d75259ec55c3e5/2026-10-02---statsbudsjett-2027-.pdf
- RSS: https://www.skatteetaten.no/rss/sbs/a-meldingen/, https://www.skatteetaten.no/rss/sbs/skattekort-til-arbeidsgiver/, https://www.skatteetaten.no/rss/bedrift/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/

**Digdir og Altinn**
- https://docs.altinn.studio/nb/authorization/guides/system-vendor/system-user/
- https://samarbeid.digdir.no/altinn/systembruker/2542
- https://samarbeid.digdir.no/altinn/kom-i-gang-i-testmiljoet-tt02/2868
- https://info.altinn.no/hjelp/ny-tilgangsstyring/utfasing-av-altinn-ii-roller/

**NAV**
- https://www.nav.no/samarbeidspartner/ekstern-datautveksling/api-oversikt
- https://www.nav.no/arbeidsgiver/sende-inntektsmelding
- https://github.com/navikt/sykepenger-im-lps-api/wiki
- https://github.com/navikt/fp-inntektsmelding-api/wiki
- https://github.com/navikt/k9-inntektsmelding-api/wiki
- https://github.com/navikt/sokos-oppgjorsrapporter/wiki
- https://github.com/navikt/syfo-dokumentporten/wiki

**Lovdata**
- https://lovdata.no/lov/2012-06-22-43/§5 (a-opplysningsloven)
- https://lovdata.no/lov/2005-06-17-62/§14-15 (arbeidsmiljøloven)
- https://lovdata.no/lov/1988-04-29-21/§10 (ferieloven)
- https://lovdata.no/lov/2005-12-21-124/§4 (OTP-loven)
- https://lovdata.no/lov/1989-06-16-65/§3 (yrkesskadeforsikringsloven)
- https://lovdata.no/lov/1997-02-28-19/§8-19 og §8-10 (folketrygdloven)
- https://lovdata.no/lov/2017-06-16-51/§26 (likestillings- og diskrimineringsloven)
- https://lovdata.no/lov/2004-11-19-73/§13 (bokføringsloven)
- https://lovdata.no/dokument/LTI/lov/2026-06-19-39 (endringslov 2026)
- https://lovdata.no/forskrift/2004-12-01-1558 (bokføringsforskriften)

**Regjeringen**
- https://www.regjeringen.no/no/tema/okonomi-og-budsjett/skatter-og-avgifter/skatte-og-avgiftssatser/skattesatser-2027/id3173438/
- https://www.regjeringen.no/no/statsbudsjett/2027/statsbudsjettet-2027-skatter-og-avgifter/statsbudsjettet-2027-provenyvirkninger-av-skatte-og-avgiftsendringer-for-2027/id3173279/
- https://www.regjeringen.no/no/aktuelt/nye-lovregler-om-e-fakturering-i-naringslivet-og-enkelte-andre-lovendringer-pa-finansmarkedsomradet-settes-i-kraft/id3166726/
- https://www.regjeringen.no/no/dokumenter/horing-utredning-av-ferielovens-system-for-opptjening-av-feriepenger/id3046142/

**Datatilsynet**
- https://www.datatilsynet.no/aktuelt/aktuelle-nyheter-2025/informasjon-om-overforinger-til-usa/
- https://www.datatilsynet.no/personvern-pa-ulike-omrader/personvern-pa-arbeidsplassen/

**Sekundære [S]**
- https://www.sticos.no/fagstoff/statsbudsjettet-2027
- https://www.revisorforeningen.no/fag/nyheter/skattetrekkskontoen-fjernes-fra-1.-januar-2026/
- SPK-kravspesifikasjon v2.7
- KLP Kundeside
- Virke/Altinget (lønnstransparens)
