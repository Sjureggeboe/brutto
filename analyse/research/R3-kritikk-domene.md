# R3 – Faglig kritikk av skjelett-v0 og strategikritikerens MVP

Dato: 2026-10-28. Rolle: lønnsfaglig, regulatorisk og teknisk skeptiker. Skrevet som en lønnssjef, en revisor og en sjefsarkitekt som har sett lønnssystemer feile i produksjon.

**Grunnlag:** `plan/skjelett-v0.md`, `R3-kritikk-strategi.md` (heretter «strategien»), S-avklaringer (høy vekt), B, C (§0, §2–5, §11–12), F (§0, §1, §3–4, §6–10), D (§1–4), E §1–2, R2-moduler-integrasjoner, R2-ansatt-org, R2-okosystem, R2-ansattdata-tripletex-reai, R2-virksomhet, R2-byra og **R2-myndighetsintegrasjoner (lest, finnes)**.

**Merking**
- [U] = usikkert. Må verifiseres før det kodes som fasit.
- [A] = egen faglig vurdering.
- Henvisning i hakeparentes, for eksempel [C §2.3] eller [strategi 4.2].
- Funn har id D-xx. Nye gylne caser har id GC-xx. Nye epics følger skjelettets nummerering.

**Leseveiledning:** (a) dom · (b) feil og mangler, ordnet etter de sju angrepspunktene · (c) skjerpede porter · (d) epics · (e) gylne caser · (f) beslutningene B1–B30 · (g) åpne spørsmål.

---

## (a) Dom

1. Strategiens retning er faglig riktig: smal MVP, liten kohort, alt med rettsvirkning i kjernen og parallellkjøring før drift.
2. Men MVP-en har hull nettopp der lønn blir feil i praksis. Feilene kommer ikke i tabelltrekket. De kommer i overgangene: migrerte saldoer, etterskuddsvis lønn over systemskiftet, pågående sykefravær, trekkpålegg registrert for hånd og lønnsartflagg fra gamle systemer.
3. Tre ting mangler helt: AGA av OTP-premien når premien føres fra faktura [S §6 pkt. 29], en strategi for a-meldingsaggregatet mot regel F532 og erstatningsmeldinger, og en plan for a-melding 2.4, som ikke kan testes med ekte data før første produksjonsmåned.
4. NAV-refusjon og inntektsmelding kan være manuelle i Q1 2028. Det er bare forsvarlig hvis refusjonsreskontro, fristvarsel og import av K27 er med i MVP. Ellers taper kundene refusjoner, eller de trekker refusjonen fra AGA to ganger.
5. Portene måler mengde, ikke dekning. «300 caser» og «10 000 tilfeldige trekk» sier lite. Portene må måle dekning, migrerte saldoer og de to farligste månedene, juni og desember. Parallellkjøringen i oktober og november treffer ingen av dem.
6. Datamodellen er i hovedsak riktig. Bitemporalitet er overbygd som generelt spørrelag, men underbygd i listen over hva som må versjoneres.
7. Kotlin er et trygt standardvalg. Argumentet om Skatteetatens Java-kode holder likevel ikke før lisensen er avklart. TypeScript er forsvarlig med strenge vilkår. Det avgjørende er testorakelet, ikke språket.
8. Skjelettet mangler systembeskrivelsen etter bokføringsforskriften, DPIA og egne roller for helse og fagforening, GRFS-dokumentasjon for byråklienter fra januar 2028, et lagringsstedsregister og en presis grense for hva support og beregningsgaranti kan love uten å bli regnskapsføring.
9. Tidlig skarp drift fra oktober 2027 (EM.7) er klok. Den utløser likevel en sammenstillingsoppgave for 2027 fra Brutto innen 31.1.2028, og det står ingen steder.
10. Med rettingene under er 1.1.2028 faglig forsvarlig for en kohort på 12 kunder. Uten dem er juni 2028 den mest sannsynlige feilmåneden.

---

## (b) Faglige feil og mangler

### b.0 Hvor Brutto vil regne feil første år (rangert) [A]

| # | Feilkilde | Når den slår til | Sannsynlighet | Tiltak |
|---|---|---|---|---|
| 1 | Migrerte saldoer: feriepengegrunnlag 2027, hittil i år, pågående AGP, trekksaldo | Januar og juni 2028 | Høy | D-04, D-07, D-23, EM.8, port M |
| 2 | Lønnsartflagg og mapping fra kundens gamle system | Første kjøring | Høy | D-02, karantene, GC-21 |
| 3 | Etterskuddsvis variabel lønn over systemskiftet (desemberovertid betalt i januar) | Januar 2028 | Høy | GC-02, EM.8 |
| 4 | Trekkpålegg registrert for hånd: feil kode, KID eller prioritet | Januar–mars 2028 | Middels–høy | D-06, D-23, GC-07–09 |
| 5 | Juni: 60+, NAV-dager, delårsansatte, kort med 12 trekkmåneder | Juni 2028 | Middels–høy | D-04, GC-04, GC-05 |
| 6 | AGA av OTP-premie mangler, eller NAV-refusjon trukket fra AGA to ganger | Hver termin | Høy for OTP | D-01, D-08, GC-17, GC-18 |
| 7 | Honorar og mottakerklasse i organisasjonsnisjen | Første honorarkjøring | Middels | D-09, D-40, GC-13–15 |
| 8 | Retro uten følgevirkninger på overtid og tillegg | Første lønnsoppgjør (mai–sep 2028) | Middels | D-03 |
| 9 | KID og forfall for forskuddstrekk, helligdager | Hver kjøring | Middels | D-24, GC-12 |
| 10 | Første a-melding i 2.4 | Februar 2028 | Middels | D-19, port 3b |
| 11 | Kostnadsfordeling og dimensjoner som regnskapet avviser | Hver kjøring | Middels | D-39, GC-20 |
| 12 | Nyansatte uten skattekort når henting bare skjer med polling | Løpende | Middels | D-22, GC-22 |

### b.1 Korrekthet i lønn

| Id | Gjelder | Funn | Konkret retting |
|---|---|---|---|
| D-01 | E1.8, strategi 4.2 «Pensjon», S §6 pkt. 29, C #1 | **AGA av OTP-premien mangler.** Premien føres fra faktura i regnskapet, men AGA av premien skal inn i a-meldingen som AGA-grunnlag («tilskudd og premie til pensjonsordning») per sone. Uten et inndatapunkt blir AGA for lav hver termin hos alle OTP-kunder. C #1 forutsetter at motoren beregner OTP, og det strider mot S §6 pkt. 29. Uavklart: om AGA følger betalingstidspunktet, og om administrasjonskostnader inngår [U] | E1.8 får inndata «betalt premie per måned og underenhet», manuelt eller fra regnskapsadapter. Fordel per sone etter pensjonsgrunnlag. Kontroll: «OTP-kunde uten premie i terminen». Skriv om C #1. Avklar med revisor og Skatteetaten |
| D-02 | E1.1, S §6 pkt. 26, B5 | **Lønnsartmodellen er for tynn.** Flaggene skatt, AGA, feriepenger og sykepenger er ikke nok. Det mangler trekkmetode (tabell eller prosent), halvt trekk, pensjonsgrunnlag, retro, opplysningspliktig og krav til antall (timer, km, døgn). Uten trekkmetode får bonus og overtid tabelltrekk og halveres i desember | Utvid modellen etter C §11.2. Valider kombinasjonen mot a-meldingens kodeliste. Nye lønnsarter går i karantene til de er testet. Flaggsnapshot per linje |
| D-03 | E1.9, strategi 4.2 «enkel retro» og 4.3 | **Enkel retro gir feil overtid ved første lønnsoppgjør.** Oppgjør med virkning 1.4 eller 1.5 utbetales mai–september 2028, før «retro med følgevirkninger» i Q3. Overtid og tillegg som regnes av timesats, blir da feil (C #21) | Differanse i timesats for overtid og tillegg, og konfigurasjonen `retro_ferietrekk`, senest 1.5.2028. Korrigert inntektsmelding kan være manuell |
| D-04 | E1.5, EM.6, port 1 | **Juni 2028 er første feriepengeutbetaling på migrerte data.** Kjente feilkilder: 6G-taket gjelder bare 60+-tillegget, NAV-dager (48) og valget FULL eller BEGRENSET ved forskuttering, trekkfritak bare for dem som var ansatt hele opptjeningsåret, kort med 12 trekkmåneder, overført ferie og forskuddsferie | GC-04 og GC-05. Migrert grunnlag per person avstemt mot gammelt system med diff 0. Skyggeberegning av juni 2027 per pilotkunde (EM.9) |
| D-05 | E1.3 | **Halvt trekk er smalere enn det ser ut.** Det gjelder tabelltrekk på vanlig lønn. Det gjelder ikke bonus, overtid eller honorar, ikke prosentkort [U] og ikke kort med 12 trekkmåneder. Kunden kan legge det halve trekket i november [D §2.4]. 14-dagerslønn er uavklart [U] | Konfigurasjon «måned for halvt trekk». Lønnsartflagg (D-02). GC-06 |
| D-06 | E1.7, E3.6 | **Trekk og vernet beløp har fem regler som må være kode:** (1) Avtalt trekk krever skriftlig forhåndsavtale om akkurat det trekket (HR-2021-2532-A). (2) Vernet beløp for avtalte trekk har ingen lovfestet sats, så livsoppholdssatsen er kundekonfigurasjon, ikke fasit. (3) Ved utleggstrekk gjør arbeidsgiveren ingen vurdering etter dekningsloven § 2-7, men trekker det som er mulig. (4) Et samordnet trekk avslutter alle gamle trekk. (5) Beløpstrekk tas i løpet av måneden, mens prosenttrekk tas av brutto ved hver utbetaling | Alle fem som regler med egne caser (GC-07–09). Avtalt trekk uten avtalereferanse blokkeres (`REQUIRES_WRITTEN_AGREEMENT`) |
| D-07 | E1.6, EM.6 | **Sykefravær over systemskiftet.** Pågående AGP, egenmeldinger siste 12 måneder og snittinntekt siste 3 måneder for timelønte (ftrl. § 8-28) må migreres. Ellers blir AGP og inntektsmelding feil i januar 2028 | EM.6 utvides (se d). GC-01 |
| D-08 | E1.6, C §2.2 steg 13 | **NAV-refusjon og AGA.** Kunden velger metode: fradrag i forskutteringsmåneden eller fradrag når refusjonen mottas, dokumentert med K27. Systemet må hindre at begge brukes. Er refusjonen lavere enn beregnet, må forskutteringsmåneden korrigeres | Metode per kunde. Refusjonsreskontro per ansatt, ytelse og periode. GC-18 |
| D-09 | E1.12, R2-ansatt-org §12–13 | **Fire uavklarte honorarpunkter treffer kohort 1 med en gang:** tapt arbeidsfortjeneste, styrehonorar til en som også er ansatt (arbeidsforholdstype), AGA-sone for frilans-arbeidsforhold, og 10 000-grensen (per organisasjon, og om trekkfrie godtgjørelser teller) [U] | Skriftlig avklaring med Skatteetaten før 1.6.2027. Kunder med uavklarte tilfeller holdes utenfor kohort 1 |
| D-10 | Strategi 4.2, C §2.1 steg 5 | **Naturalytelser mangler i MVP-listen.** Fri bil (ny modell fra 2027 med motortype, hvis vedtatt [U]), elektronisk kommunikasjon og forsikringer finnes hos mange kunder. Trekket begrenses til kontantbeløpet (C #19) | Ny E1.14. Minst en fast fordelslinje med riktige flagg og bilfordel etter 2027-modellen |
| D-11 | E2.3, bokføringsforskriften § 5-6 | **Timelønte:** timer per dag skal dokumenteres [B §10.2]. En CSV med månedssum oppfyller ikke kravet | Importformatet krever dagslinjer for timelønte. Kjernen lagrer dem |
| D-12 | E2.3 (utlegg via import), R2-moduler §4.1 | **Km og diett:** Kjernen må dele i trekkfri og trekkpliktig del og vite om reiseregningen oppfyller skattebetalingsforskriften § 5-6-12. Mangler et påkrevd felt, er hele beløpet trekkpliktig | Kontraktsfelt `reiseregningKomplett` pluss godtgjørelsesmotor i MVP, uansett kilde (Utleggsappen, CSV eller manuelt) |
| D-13 | C §11.2 mot R2-ansattdata F3 | **Underenhet ligger feil i C.** C legger virksomhet på arbeidsforholdsversjonen. R2 legger den på det stabile arbeidsforholdet. Bytte av underenhet betyr i a-meldingen at arbeidsforholdet avsluttes med sluttårsak og et nytt opprettes | Følg R2. Oppdater C |
| D-14 | C §11.3 mot S §6 pkt. 27 | **Konteringen i C avviker fra Sjurs** (styrehonorar 5330 mot 5011, OTP, refusjon) | S §6 pkt. 27 er fasit. Bilagscaser bruker den |
| D-15 | Port 1 i v0 («2026 og 2027») | **Gylne caser for 2026 har liten verdi.** Produksjonen starter i 2028 | Prioriter 2027 (parallellkjøring og EM.7) og 2028 (drift). 2026 brukes bare til historisk skyggeberegning |

### b.2 A-melding og myndigheter

| Id | Gjelder | Funn | Konkret retting |
|---|---|---|---|
| D-16 | E3.2, B11 | **F532 (fra periode 2027-01):** Sum forskuddstrekk per lønnsutbetalingsdato kan ikke være negativ, og avviket er av typen «øyeblikkelig». En korreksjon som reduserer trekket for en tidligere dato kan derfor ikke sendes som egen tilleggsmelding. Den må inn som erstatning for meldingen som har den datoen. Uavklart om summen gjelder per melding eller per måned [U] | Aggregatet velger og dokumenterer én strategi. Anbefalt [A]: én melding per opplysningspliktig og måned, som erstattes ved hver endring. GC-10 og GC-11 |
| D-17 | EM.1, B16, F §6.2 | **«A-melding-XML som fasit» er upresist.** A-meldings-API-et tar JSON (`AMLD_1047`). Siden juni 2026 sender alle systemer JSON. Historikk før juni 2026 er XML | Fasit = innsendt innhold (XML eller JSON) pluss Skatteetatens avstemmingsrapport. Importøren leser begge formater |
| D-18 | Spor M, B16, S #20 | **Kontinuitet ved migrering.** Arbeidsforhold-ID og permisjons-ID beholdes. Antall arbeidsforhold og underenhet skal være uendret (metode 1). Første melding for 2028-01 må ha alle løpende arbeidsforhold og permisjoner. Ingen periode rapporteres fra to systemer | Port M krever 100 % bevarte ID-er og diff 0 mot avstemmingsrapporten. GC-03 |
| D-19 | E3.9, B11, strategi 7.3 | **2.4 kan ikke testes med ekte data før produksjon.** Testmiljøet tar bare syntetiske data. Parallellkjøringen i oktober–november går i 2.3. Første ekte 2.4 sendes i januar 2028, for alle kunder samtidig. Innholdet i 2.4 er ikke endelig per 22.10.2026 | Lag 2.3 og 2.4 fra samme aggregat og krev semantisk diff 0. Lag syntetiske tvillinger i Tenor av hver kohortkunde og få dem godkjent i 2.4-testmiljøet. Sett av 2–3 utviklermåneder mai–november 2027 til 2.4. Avklar om manuell XML-opplasting finnes for 2.4 |
| D-20 | E3.9, B §14 pkt. 11 | **Retting av 2027-perioder etter 1.1.2028.** En erstatningsmelding krever hele månedens innhold, trolig i gjeldende format [U]. For migrerte kunder ligger innholdet for 2027 i det gamle systemet | Pilotavtalen krever at gammelt system beholdes minst 3 måneder for retting av gamle perioder [F §6.4], eller at fullt innhold for de siste 3 månedene importeres som egen versjon av aggregatet. Avklar formatet med Skatteetaten før 1.9.2027 |
| D-21 | E3.1, E8.2 | **Systembruker for klientsystem i skala.** (1) Den støtter bare tilgangspakker. (2) Byrået får pakken via rollen REGN i Enhetsregisteret, eller ved at klienten delegerer. Kildene spriker [U]. (3) Klientdelegerings-API-et krever ID-porten-token, og det er uavklart om en privat leverandør får det. (4) API-et har ikke paginering. (5) Skatteetaten tillater 5 samtidige kall per API per virksomhet, og for agent-token er «virksomheten» trolig byrået [U]. (6) `regnskapsforer-lonn` dekker ikke Krav og betalinger, så byrået kan ikke sjekke via API om trekket er betalt | Jobbkø med kvoter per byrå. Altinn-portalen er standard reservevei for klientdelegering. Avklar (2) og (5) med Digdir og Skatteetaten |
| D-22 | E3.4 | **Skattekort bare med polling fra 15.12.2026.** Daglig `HENT_KUN_ENDRING` per arbeidsgiver (`FOR_004`), maks 1 000 fødselsnumre per bestilling, minst 2 s mellom polleforsøk, og ny henting rett før godkjenning (fryseregel). Bruksvilkårene ber om hendelsesdrevet bruk og åpner for struping av hyppig polling | Pollebudsjett per byrå (bestillinger per døgn). Ingen henting for sluttede eller `registrertSomDoed`. Desemberbestilling for nytt år planlagt per klient. Test av alle resultatkoder. GC-22 |
| D-23 | E3.6, strategi 4.4 | **Trekkpålegg-API har forutsetninger strategien ikke nevner.** Leverandøren må være i produksjon med a-meldings-API-et, kunden må ha sendt minst én a-melding fra Brutto, og testoppsummering og signert avtale kreves. For kohort 1 betyr det at alle løpende pålegg må migreres manuelt med KID, saldo og kode (samordnet eller skatt) før januarlønnen. Manuell lesing i Altinn krever personlig tilgang til kundens innboks | EM.6 omfatter trekkpålegg. API-et aktiveres per kunde etter første a-melding (februar 2028), ikke Q3 2028. Pålegg etter gamle regler og bidrag er alltid manuelle (ny E3.12) |
| D-24 | E4.1, E3.5, strategi 4.2 «Penger» | **Trekk betales første virkedag etter lønn.** (1) Brutto lager KID for forskuddstrekk selv, men algoritmen for kontrollsifferet er ikke funnet [U]. (2) Trekket må være eget betalingsoppdrag, ikke merket lønn/SALA, ellers kan KID falle bort. (3) Hver lønnsutbetalingsdato gir egen frist. (4) Helligdager, og om 24.12 og 31.12 er virkedager [U]. (5) Flytter kunden betalingsdatoen i nettbanken, blir lønnsutbetalingsdatoen i a-meldingen feil | KID verifiseres mot Skatteetatens KID-generator og mot `kidForForskuddstrekk` i tilbakemeldingen (MYN-19). Helligdagskalender. Faktisk betalingsdato bekreftes før a-meldingen sendes. Ny E4.9. GC-12 |
| D-25 | E3.7, strategi 4.3–4.4 | NAV manuelt i 2028. Se b.2.1 | – |
| D-26 | E3.11, strategi 3.4 | **«Aa-registeret i Fase 3» er feil.** Ordinære arbeidsgivere og lønnssystemer får ikke API-tilgang [R2-myndighet §3.17] | Kutt. Bruk avstemmingsrapporten |
| D-27 | EM.7, E3.8 | **Skarp drift fra 1.10.2027 gir to systemer i samme inntektsår.** Ett system skal lage hele årets sammenstillingsoppgave [F §6.3] | EM.7-kunder får sammenstilling for 2027 fra Brutto innen 31.1.2028, med hittil-i-år for januar–september importert. Velg EM.7-kunder med dette i tankene. Brutto AS selv er det tryggeste valget |
| D-28 | Strategi 4.4 «A-melding hvis API-et svikter» | **Reserveveien krever XML.** Brutto lager JSON | XML-eksport (2.3, og 2.4 når XSD finnes) i MVP |
| D-29 | Port 3b i strategien («innen 5.2.2028») | **Fristen for 2028-01 er mandag 7.2.2028.** 5.2.2028 er en lørdag | Bruk intern frist: «sendt senest 2 virkedager etter lønnsutbetaling» |

#### b.2.1 Er det forsvarlig å la NAV-refusjon og inntektsmelding være manuelle i 2028?

**Juridisk ja. Faglig bare med fire ting i MVP.**

- NAV tilbyr portalinnsending, så manuell inntektsmelding er lovlig.
- Motstriden består: nav.no sier at bare sykepenger kan sendes fra lønnssystem. API-oversikten viser API-er for foreldrepenger, svangerskapspenger og sykdom i familien. Omsorgspenger går via Min side fra 21.5.2026 [B §6.1], [R2-moduler §2.1].
- Refusjon kan bare kreves for fravær inntil 3 måneder før søknadsmåneden [C §7]. En manuell rutine som glipper, taper penger for kunden.

**Må være i MVP:**
1. AGP-tilstand og grunnlag for inntektsmelding (ftrl. § 8-28) som utskrift per sak, klar til å skrive inn i NAVs portal.
2. Refusjonsreskontro per ansatt, ytelse og periode, med varsel før 3-månedersfristen.
3. K27-import fra CSV (ISO-8859-1), matching mot forskuttert beløp (MYN-20) og bokføring. API-et er lite arbeid (polling, CSV, PDF), så ta det med hvis kapasiteten tillater.
4. Akkumulator for feriepengerefusjon (48 dager).

**Plan:**
- Inntektsmelding for sykepenger via API senest 1.4.2028, ikke «Q2».
- Foreldrepenger, svangerskapspenger og sykdom i familien bak funksjonsbryter til NAV har svart.
- Send kontaktinformasjonen NAV krever i bruksvilkårene nå (ES.2), til tre adresser [R2-myndighet §4 steg 8].

**Skjult kostnad:** Den manuelle veien krever at noen hos kunden eller byrået har personlig Altinn- eller NAV-tilgang til særlig kategori. Det må inn i onboardingen.

#### b.2.2 Faglig risiko i strategiens MVP (samlet)

| Strategiens valg | Risiko | Retting |
|---|---|---|
| NAV manuelt til Q2 2028 (E3.7) | Tapte refusjoner, dobbelt fradrag i AGA | b.2.1 |
| Trekkpålegg manuelt, API i Q3 2028 (E3.6) | Feil kode, KID eller prioritet. Nye pålegg oversett | D-23. API i februar 2028 |
| Enkel retro, følgevirkninger i Q3 (E1.9) | Feil overtid ved lønnsoppgjør i mai–september | D-03 |
| pain.002 og camt.054 i Q2 2028 | Ingen automatisk bekreftelse av at trekk er betalt. Byrået kan ikke bruke Krav og betalinger | Påkrevd «betalt»-kvittering med dato og påminnelse T+1 (E4.9) |
| Sammenstillingsoppgave til 31.1.2029 (E3.8) | EM.7-kunder og plan B-kunder trenger den tidligere eller for hele året | D-27. Hittil i år per a-meldingsbeskrivelse i EM.6 |
| «Én periode for grønne byråklienter» (port M) | Én novembermåned dekker verken juni eller desember | Godta bare med historisk skyggeberegning av juni 2027 og skyggekjøring av desember 2027 (EM.9) |
| GRFS-støtte (E8.6) i Q2 2028 | Byrået mangler oppdragsdokumentasjon fra første klient i januar 2028 | D-34. GRFS-pakke light i MVP |
| Naturalytelser ikke nevnt | Feil trekk og AGA hos kunder med fri bil | D-10 |
| OTP «føres fra fakturaen» | AGA av premie mangler | D-01 |
| Ansatte uten BankID som «siste utvei» (strategi 2.5) | Grønne byråklienter med D-nummer-ansatte står uten slipp og uten kontoendring | Standard reservevei i MVP (D-49) |
| «Byråets egen lønn er en ufarlig pilot» | Det er ekte a-melding og ekte skattebetaling | Riktig valg, men samme porter som for kunder |

### b.3 Regelverk og ansvar

| Id | Gjelder | Funn | Konkret retting |
|---|---|---|---|
| D-30 | E2.9, B §10.2 | **Systembeskrivelse mangler.** Bokføringsforskriften § 5-6 krever en lettfattelig beskrivelse av lønnssystemets oppbygging og funksjoner. § 3-1 nr. 9 krever at AGA-pliktige ytelser kan vises per sats og sone | Ny E2.11. Versjonert per release, del av revisorpakken |
| D-31 | E7.2 | **Lønnsslippen** skal vise beregning, grunnlaget for feriepenger og trekk (aml. § 14-15 sjette ledd) | Feriepengegrunnlag hittil i år på hver slipp |
| D-32 | B9, S §1 pkt. 4–5 | **Lagringssted.** (1) S viser til bokføringsforskriften § 7-5, R2-moduler til § 7-7. Paragrafen må avklares. (2) Azure Norway West har reservert tilgang. Backup på annet sted i Norge må bekreftes hos Microsoft eller løses med en norsk lagringsleverandør. Om bokføringsforskriften krever «annen lokasjon», eller om det er Sallys tolkning, er [U]. (3) Revisjonsloggen er regnskapsmateriale (S #3). Overvåkingsverktøy i EU (Sentry, Grafana) må ikke få lønnsdata eller revisjonslogg, ellers utløses meldeplikten | Ny E9.9: lagringsstedsregister for alle lagre med formål, eier, oppbevaringstid og land (S #2). Port 9 krever at regnskapsmateriale bare ligger i Norge |
| D-33 | E0.5, S §2 pkt. 7, B §11 | **GDPR art. 9.** Helse (fravær, sykelønnsartene 2018 og 2019, K27, NAV-dokumenter, konto 5800) og fagforening (trekk) er med i MVP. Det mangler: DPIA-mal for kunden, tilgangsrollen «Lønn – helse», maskering i lederrapporter, bilag og lønnsjournal for brukere uten rollen, kortere slettefrist for sykmeldinger og søknader enn for bilag, og rådgivervurdering før drift | Ny E9.8. Inngår i port 9 |
| D-34 | E8.6, strategi 4.2 «Byrå» | **GRFS gjelder fra første byråklient i januar 2028** (ikke for byråets egen lønn). Byrået må dokumentere kontroll (7.2), skattekort (7.4), oppfølging av a-meldingsavvik (7.8), kundens godkjenning (8.6) og avstemming (9.3), og oppbevare det i 5 år (regnskapsførerloven § 5-3) | Ny E8.10 GRFS-pakke light i MVP: PDF/A og CSV per klient og periode fra revisjonsloggen, registrering av godkjenning per e-post med vedlegg (BY-45), lagret i byråets område |
| D-35 | B4, B24, E9.7, EM | **Ansvarsgrensen.** Finanstilsynet regulerer ikke en ren programvareleverandør som ikke «tar ansvar overfor kunden for resultatet av regnskapsføringen» [E §2.1]. Tre ting i planen nærmer seg grensen: (1) beregningsgarantien formulert som «vi retter», (2) implementering og support som registrerer, kjører eller godkjenner for kunden, (3) gratis migrering der Brutto legger inn data | Garantien dekker programvarefeil og dokumenterte renter, tilleggsskatt, tvangsmulkt og gebyrer, med tak. Brutto leverer korreksjonsforslag. Kunden eller byrået kjører og godkjenner. Support har ingen rett til å godkjenne eller sende inn. Tilgang via break-glass logges. Jurist vurderer før pilotavtalene signeres |
| D-36 | E3.8, B §2.7, D §2.6 | **Sammenstillingsoppgaven.** Kildene spriker. D sier at Skatteetaten sender den. B sier at hjemmelen ikke er verifisert. GRFS 7.7 og ferieloven § 10 krever en sammenstilling | Behandle den som lovkrav med frist 31.1 til jurist har svart |
| D-37 | E1.7, E3.6 | **Trekkplikt.** En arbeidsgiver som ikke trekker etter pålegg, kan bli ansvarlig for beløpet [U: hjemmel] | Manuell registrering med fire øyne og fast rutine for å sjekke Altinn-innboksen |

### b.4 Datamodell og arkitektur

| Id | Gjelder | Funn | Konkret retting |
|---|---|---|---|
| D-38 | B6 | **Bitemporalitet: riktig å avgrense, men listen er feil.** Disse må versjoneres med registreringstid: fravær og permisjon (registreres ofte etterpå), kostnadsfordeling (retroaktiv omfordeling), pensjonsmedlemskap, virksomhetsversjon (sone), avtalte trekk og trekkpålegg (`trekkversjon`) og lønnsartversjon. Overbygd: et generelt «som kjent ved»-spørrelag. Retroalgoritmen sammenligner med linjer som allerede er utbetalt, ikke med en as-of-beregning [C §5.2] | Bare-tilføyende versjoner med `registrert_tid`, pluss uforanderlig snapshot av inndata per kjøring. Det gir reproduksjon og revisjonsspor. Bygg as-of-spørringer bare der retro og revisorpakken trenger dem |
| D-39 | E2.10, R2-ansattdata F3–F4 | **Kostnadsfordelingen i MVP er for enkel.** Den mangler gyldighetsdatoer, oppdeling av linjen ved endring midt i perioden, fryst kontering per linje, største rest-avrunding, proporsjonal fordeling av AGA, feriepenger og OTP, validering mot regnskapets dimensjoner før godkjenning, og avdeling på arbeidsforholdet i stedet for personen. Retroaktiv omfordeling kan vente, men modellen må tåle den | E2.10 utvides (d). GC-20 |
| D-40 | E1.12, R2-ansatt-org §2, R2-okosystem §2.4 | **Mottakertyper.** Klassen hører til relasjonen og utbetalingen, ikke personen. Hver utbetaling har betalende juridisk enhet. Frilans-arbeidsforhold rapporteres bare i måneder med utbetaling. Klassifiseringen lagres med begrunnelse. Næringsdrivende, utenlandske artister og frikjøp via egen arbeidsgiver går aldri i lønn. Lokallag med eget organisasjonsnummer er egne opplysningspliktige | Inn i E1.12. Lokallag holdes utenfor kohort 1 eller kjøres som egne klienter |
| D-41 | Kilderegister, R2-okosystem §2.2 og §4.4.7 | **Enkelt eierflagg holder i 2028**, men identitet, bankkonto og skattekort skal være låst til Brutto fra dag én, også ved import fra Huma. Fravær fra Huma kommer bare som webhook uten nye forsøk. Er Huma fraværskilde, avhenger AGP av en upålitelig kanal | Brutto er fraværskilde i kohort 1, ellers obligatorisk fraværsavstemming før cut-off |
| D-42 | A-melding som eget aggregat | **Beskrivelsen mangler** meldingsstrategi (D-16), feltet `kildesystem`, migrert historikk (D-20), livssyklus for permisjons-ID (endret prosent gir ny ID, retting med 0 % og lik start- og sluttdato), hash-lås ved godkjenning og versjonsuavhengig modell med serialisering til 2.3 og 2.4 | Inn i E3.2 og E3.9 |
| D-43 | E0.7, E1.13 | **Regelpakker er ikke «per år».** Kjente virkningsdatoer er 1.1 (budsjett, trekkrutine, kodelister), 1.5 (G), 1.7 (livsoppholdssatser) og særavtalen for statens reisesatser (gjelder til 31.12.2027). Regelpakken slås opp per regel og relevant dato [F §1.3] | E1.13 blir «Regelpakker og årshjul», ikke bare regelår 2028 |

#### b.4.1 Stack: Kotlin/JVM eller TypeScript for et lite team med kodeagenter

| Kriterium | Kotlin/JVM | TypeScript (hele stacken) | C#/.NET |
|---|---|---|---|
| Penger og desimaler | `BigDecimal`, moden | Bibliotek (decimal.js) eller `bigint` i øre. `number` er en felle | `System.Decimal`, best |
| Dato og tid | `java.time`, moden | `Date` er en felle. Temporal API eller bibliotek er nødvendig | Moden |
| Domenetyper | Sealed classes, sterke | Gode typer, men ingen kontroll ved kjøring uten zod e.l. | Records og pattern matching, sterke |
| XML (pain.001, camt.054, reserve-XML) | Moden | Svakere. A-meldings-API-et er JSON, så behovet er mindre enn F antar | Moden |
| Skatteetatens trekkrutine (Java) | Kan brukes direkte, **men lisensen er uavklart** | Må porteres, eller kjøres i JVM bare som testorakel | Må porteres |
| Kodeagenter | Gode. Gradle og kompilering gir tregere sløyfer | Svært gode. Raske testsløyfer | Gode |
| Rekruttering med lønnsfag | NAV, fintech | Stor generell pool, lite lønnsfag | Visma, PowerOffice, Uni Micro: der lønnsfaglige utviklere sitter |
| Én eller to språk | Kotlin bak, TS foran: to språk | Ett språk | C# bak, TS foran: to språk |

**Vurdering [A]:**
- Argumentet «Skatteetatens Java-kode kan brukes direkte» er svakt så lenge repoet ikke har lisens. Får vi ikke lov, må trekkrutinen uansett implementeres fra de publiserte tekst-tabellene og verifiseres 100 %. Da betyr språket mindre.
- Den største risikoen med kodeagenter er kode som ser riktig ut, men er faglig feil. Den fanges av orakelet (gylne caser signert av lønnsfaglig, fullstendig sammenligning med trekktabellene, release-diff, mutasjonstesting), ikke av språket.
- **Anbefaling:** Kotlin for kjerne, gateway og API, TS bare i frontend, hvis tech lead er sterk i JVM. **Full TypeScript er forsvarlig** hvis tech lead er TS-sterk og fire vilkår er låst fra dag én:
  1. `Money` som egen type (heltall øre eller decimal) og lint-forbud mot `number` for beløp.
  2. Ingen `Date` i domenet. Bare kalenderdatoer og Temporal eller tilsvarende.
  3. Kontroll ved kjøring (zod e.l.) på alle grenser.
  4. Egenskapsbaserte tester (fast-check) og mutasjonstesting (Stryker) på regelmodulene.
- .NET er undervurdert i F og strategien. Det er der norske utviklere med lønnsfag sitter.
- Lås valget innen 1.12.2026 som strategien sier. Begrunnelsen bør være tech lead, ikke trekkrutinen.

### b.5 Moduler og kjerne

| Id | Gjelder | Funn | Konkret retting |
|---|---|---|---|
| D-44 | Grensen kjerne/modul, strategi 3.5 pkt. 2–3 | **Strategien flytter AGP, ferietrekk, feriesaldo, permisjon og permittering til kjernen. Det er riktig.** Følgende mangler likevel i kjernen: saldohovedbok for ferie (rett, tatt, trukket, overført, forskudd, 60+), teller for egenmelding med policy og dato for drøfting med tillitsvalgte, omsorgsdager per år med «arbeidsgivers 10 dager», permitteringsteller (26 uker per 18 måneder), timer per dag for timelønte, godtgjørelsesmotor og sperre etter § 14-15 for negative korrigeringer etter låsing | Må være i kjernen før første egne modul lanseres |
| D-45 | Arv fra runde 1 og 2 | **Fem påstander som er rettet i R2, men kan ha sneket seg inn i epics:** utvidet egenmelding (IA) som standard, 6G-tak på hele feriepengegrunnlaget, alt fravær rapportert som permisjon, § 10-7 bare for timelønte og MVA-fradrag på alle utlegg [R2-moduler §9] | Sjekkliste i E1.11 og E6.x |

#### b.5.1 Minimum for å lansere egne moduler trygt, og rekkefølgen

Gründerens krav om egne moduler står fast. Det faglige minimumet:

| Rekkefølge | Modul | Faglig minimum før lansering | Hvorfor i denne rekkefølgen |
|---|---|---|---|
| 1 | **Ferie og fravær** | Søknad og godkjenning. Kjernen eier saldo og konsekvenser. Egenmelding er 3 kalenderdager per tilfelle som standard. Utvidet ordning bare med registrert drøfting. Retten fratas aldri automatisk. Teller for sykt barn. Leder ser periode og grad, aldri diagnose. Ferie: 25 virkedager, 60+, nyansatt etter 30.9 får 6 dager, hovedferie 18 dager, overføring ved sykdom. Byttetest mot Huma eller CSV gir identisk lønn, a-melding og saldo | Mest rettsvirkning. Trengs for å erstatte Huma. Kjernen er allerede i MVP |
| 2 | **Timer** | Timeliste per dag for timelønte. Fast plan med registrerte avvik for fastlønte (aml. § 10-7, avklar med Arbeidstilsynet [U]). Overtidstellere 10/25/200 timer med grenseprofiler for avtale og Arbeidstilsynet. Minst 40 % tillegg. Avspasering bare med skriftlig avtale, og tillegget utbetales. Ingen turnus | Lovkrav (bokføringsforskriften § 5-6 og aml. § 10-7) som kunder uten tidssystem mangler |
| 3 | **Utlegg** | Innenlands reise, km og kvittering. Påkrevde felt: formål, arrangement, rute, km, passasjernavn og datert og signert oppstilling. MVA-kode bestemmes av kategori, med fradragsforbud for representasjon, servering, kost til ansatte og personbil. Ingen MVA i lønnsbilaget når utlegget bokføres i regnskapet. Dublettkontroll med kvitteringshash. Kilderegisteret mot Utleggsappen | Utleggsappen dekker behovet i mellomtiden. Mest risiko for dobbel utbetaling |

### b.6 Sikkerhet og tillit

| Id | Gjelder | Funn | Konkret retting |
|---|---|---|---|
| D-46 | E7.3, B14, port 7 | **Kontonummer-skjoldet har et hull: betalingsfilen.** pain.001 lastes ned og opp i nettbanken for hånd. Filen kan endres underveis [D §1.1 steg 10] | Vis antall, sum og hash av filen og listen over nye kontoer til den som godkjenner i banken. Ellers: BankID-steg, karantene (forslag: endring under 5 virkedager før godkjenning krever fire øyne), varsel på gammel kanal uten beløp, den som verifiserte kontoen kan ikke godkjenne første betaling (S #24), import fra Huma blir bare forslag, ny bekreftelse etter 12 måneder uten bruk |
| D-47 | E0.3, port 2 | **Arbeidsdeling.** Den som forbereder, kan ikke godkjenne. Den som endret en konto, kan ikke godkjenne kjøringen der endringen virker. Den som opprettet en ansatt, kan ikke godkjenne første utbetaling. Ingen kan endre egne data. Små kunder har ofte bare én lønnsperson | Tillat unntak med logg og kompenserende kontroll: rapport til daglig leder eller styreleder etter hver kjøring. Rapport over «hvem kan både X og Y» |
| D-48 | B13, S §3, E0.10 | **Agentgrenser gjelder også kodeagenter.** S §3 håndheves i gatewayen for agenter i produksjon. For kodeagenter mangler regler | Kodeagenter får aldri tilgang til produksjonsdata eller -logger. De kan ikke endre forventede verdier i gylne filer, regelpakker eller a-meldingsmapping uten lønnsfaglig godkjenning (CODEOWNERS). Commits fra agenter merkes, som bevis for endringsstyring i ISAE |
| D-49 | E7.1, strategi 2.5 pkt. 5 | **Ansatte uten BankID** (ofte D-nummer) er vanlige hos grønne byråklienter i renhold og bygg | Standard reservevei i MVP: slipp som kryptert PDF, kontoendring på signert skjema med fire øyne |
| D-50 | E0.4, S #3 mot F §4.9 | **Logging.** S #3 (revisjons-, tilgangs- og hemmelighetslogg i 5 år) går foran F (sikkerhetslogg 12–24 måneder). Lesing av fødselsnummer, konto og helsedata logges. Ingen personopplysninger i applikasjonslogger | Logger i Norge. Hash-kjede. Lesing av sensitive felt er egen hendelsestype |

#### b.6.1 ISAE 3402: når og hvor mye

| Mottaker | Hva de krever i 2028 | Hva Brutto leverer |
|---|---|---|
| Kohort 1 (organisasjoner og grønne byråklienter) | Ikke ISAE ved kontrakt | Sikkerhetsbeskrivelse, DPA, underleverandørliste, sammendrag av pentest, beredskapsplan og SLA |
| Pilotbyrå | GRFS 2.3: byrået må vurdere at lønnssystemet er betryggende og ha egen beredskapsplan | Kontrollbeskrivelse og beredskapsbeskrivelse byrået kan bruke direkte. ISAE type 1 når den finnes |
| Kundenes revisorer, revisjon av 2028 (januar–mars 2029) | Ber om ISAE 3402 type 2 fra lønnsleverandøren, ellers mer testing hos kunden [D §4.2] | **Type 2 for perioden 1.7.–31.12.2028, rapport før 28.2.2029** |
| Kunder over 250 ansatte (2029 og senere) | Type 2 ved kontrakt | Løpende type 2 |

**Anbefaling [A]:** Type 1 per 30.6.2028 er riktig (strategi B15). Men kontrollene må virke med bevis fra 1.1.2028, slik at type 2-perioden kan starte 1.7.2028 og rapporten ligger klar før revisjonssesongen 2029.

**Omfang:**
- Generelle IT-kontroller: endring, tilgang, drift og backup.
- Beregningskontroller: release-diff, godkjenning av regelpakker og gylne caser.
- Innsending: hash-lås og kvittering.
- Betaling: filintegritet og kontonummer-skjold.
- Ikke moduler og ikke KI.

### b.7 Test og drift

| Id | Gjelder | Funn | Konkret retting |
|---|---|---|---|
| D-51 | Release-diff [F §7.6], B28 | **Release-diff er nødvendig, men ikke nok slik den er beskrevet.** (1) Den må sammenligne slipp, a-meldingsbidrag og bilag, ikke bare netto. (2) Forrige måned dekker ikke juni og desember. (3) Den må bruke regelpakken som gjaldt for kjøringen, slik at avvik bare skyldes koden. (4) Den leser ekte data og må kjøre som godkjent jobb som bare logger antall og id-er (S #10) | Kjør forrige måned, et årshjulssett (siste 12 måneder, i alle fall juni og desember) og alle gylne caser. Uforklart avvik stopper utrullingen. Forklarte avvik signeres av lønnsfaglig |
| D-52 | TT02 og Tenor | **Bare syntetiske data, og TT02 er ustabilt.** Testdata for trekkpålegg lages av Skatteetaten på bestilling, med lang ledetid. Frikort med beløpsgrense oppdateres ikke i test. NAV-test går i Dolly. Et testbyrå trenger REGN-rolle for testklientene [U] | Releaseporten skal ikke avhenge av at TT02 er oppe: kontrakttester mot lagrede svar i CI, TT02 hver natt som signal. Bestill testdata for trekkpålegg nå |
| D-53 | E1.13, strategi 7.1 | **Årsskiftet 2027–2028 er farligere enn et vanlig år.** 2.4, regelpakke 2028, kohortstart, EM.7-kundenes første årsskifte og sammenstilling for 2027 kommer samtidig, i romjulen | 2.4-koden ferdig og frosset 1.12, styrt av kalendermåned. Regelpakke 2028 som ren datarelease innen 5 virkedager etter vedtak og trekkrutine (ca. 8.12). Ingen kohortkunde med lønnsdag før 15.1.2028. Tidsreisemiljø [F §7.5] testet i november |
| D-54 | E9.6, port 9 | **Beredskap på lønnsdagen mangler en plan for at Brutto er nede på T-2** | Kunden kan laste ned siste godkjente betalingsfil og slipper, lagret ved godkjenning, eller bruke bankens kopi av forrige lønnsliste, med korreksjon etterpå. Logg av nedetid hos myndighetene som bevis mot tvangsmulkt. Vakt også 1.–7.2.2028 (første frist i 2.4) og hele juni 2028 |
| D-55 | EM.7 | **Brutto AS sin egen lønn bør være første produksjonskunde fra 1.10.2027.** Det gir ekte KID-betaling, ekte a-melding og en ekte desember med halvt trekk, uten kunderisiko | Inn i EM.7 og port 4 |

---

## (c) Skjerpede porter per spor

Datoene følger strategien. Alle terskler er målbare. «Lik på øret» følger F §6.5.

| Spor | Port (dato) | Terskler |
|---|---|---|
| **S** | 31.3.2027 | Strategiens port, pluss: kontaktinfo sendt til NAV (tre adresser). Testscope for trekkpålegg bestilt. Skriftlig svar fra Skatteetaten om lisens for trekkrutinen eller beslutning om egen implementering. Spørsmål om honorar (D-09) sendt til Skatteetaten. Tilgang til Norway West eller norsk backupleverandør avklart |
| **0** | 31.3.2027 | Gående skjelett som i strategien, pluss: databasedump inneholder 0 gyldige fødselsnumre i klartekst (skanning med kontrollsiffer). Hash-kjeden i revisjonsloggen verifiseres uten brudd. Isolasjonstest mellom tenanter: 0 lekkasjer i alle API-endepunkter. Gjenoppretting fra backup i Norge med målt RPO ≤ 5 min og RTO ≤ 4 t |
| **1** | Delport 1.6.2027 | 100 % treff mot **alle** publiserte trekktabeller for 2027 i tekstformat (alle tabellnumre, alle trekkperioder, alle trinn), ikke et utvalg. ≥ 150 gylne caser, 100 % grønne |
| **1** | 1.9.2027 | ≥ 300 gylne caser fordelt etter en dekningsmatrise: lønnsform × fravær × trekkpålegg × sone × spesialmåned (juni, desember, G-regulering) × mottakerklasse, minst 5 caser i hver celle som er relevant for kohort 1. Alle signert av lønnsfaglig. 20 % kontrollsignert av en annen. ≥ 50 laget av ekstern fasit. Alle caser i (e) med. 10 egenskapsbaserte invarianter × 10 000 tilfeller med 0 brudd. 1 000 kjøringer med stokkede inndata gir byte-lik utdata. Mutasjonsscore ≥ 80 % på trekk, AGA, feriepenger og trekkø. 0 åpne feil av alvorlighetsgrad 1–2 i trekk, AGA, feriepenger, trekkø og a-meldingsmapping |
| **1** | 22.12.2027 (regelår 2028) | Regelpakke 2028 publisert innen 5 virkedager etter vedtak og trekkrutine. 100 % treff mot trekktabellene for 2028. Release-diff for desember 2027 med pakke 2027 gir 0 avvik. Alle gylne caser for 2028 grønne |
| **2** | 30.9.2027 | Strategiens port, pluss: 50 innlagte feiltyper (ny konto, negativ netto, manglende skattekort, lønn etter sluttdato, fordeling ≠ 100 %, ukjent lønnsart m.fl.) flagges 100 %. 100 tilfeldige gjentatte importer gir 0 doble linjer. Kjøring for 400 ansatte p95 < 10 s. Arbeidsdeling: 0 godkjenninger av egen kjøring i en egenskapsbasert test |
| **3a** | 1.9.2027 | A-melding 2.3 godkjent i TT02 for ≥ 5 testvirksomheter med 0 avvisninger, 0 «øyeblikkelig» og 0 uforklarte retningslinjeavvik. Scenariene omfatter honorar og frilans, permisjon, permittering, samordnet trekk og trekk etter gamle regler, to utbetalingsdatoer, erstatning og en lokal test som stopper F532. Skattekort hentet for 1 000 testpersoner, alle verdier av `resultatForSkattekort` håndtert. KID for forskuddstrekk lik KID-generatoren i 100 % av 36 måneder. Avstemmingsrapport tur–retur med diff 0. Testoppsummering for trekkpålegg sendt. XML-eksport validerer mot XSD |
| **3b** | 1.12.2027 | 2.4: 100 % av 2.3-scenariene gir semantisk lik 2.4 (diff 0 på mappede felt). Godkjent i 2.4-testmiljøet med 0 avvisninger. Syntetisk tvilling av hver kohortkunde godkjent |
| **3b** | 7.2.2028 | Alle kohortkunder har sendt 2028-01 med 0 avvisninger og 0 «øyeblikkelig» som skyldes Brutto. Internt mål: sendt senest 2 virkedager etter lønnsutbetaling. 0 avvik mellom egenberegnet KID og `kidForForskuddstrekk` |
| **4** | 30.9.2027 | pain.001 godtatt i ≥ 2 banker, med trekk som eget betalingsoppdrag. Ekte betaling av forskuddstrekk med Brutto-KID gjenfunnet hos Skatteetaten (Brutto AS, EM.7). 100 % av bilagene balanserer. 0 bilag avvist av regnskapssystemet i pilot. Lønn mot a-melding mot bilag diff 0 per kunde og periode. 2600 i null etter hver trekkbetaling |
| **6** (moduler) | Før hver modul | Byttetest: samme fakta via egen modul og via ekstern CSV gir identisk lønn, a-melding og saldo (diff 0). Arkitekturtest: modulkode kan ikke importere kjernens regelpakker (0 brudd). Inngående saldo migrert med diff 0. Alle punkter i b.5.1 dekket av caser |
| **7** | 30.9.2027 | 0 utbetalinger til konto endret innenfor karantene uten fire øyne (egenskapsbasert test). 0 beløp eller fødselsnumre i varsler (skanning av alle maler). Reservevei for ansatte uten BankID testet ende til ende |
| **8** | 31.1.2028 | GRFS-pakke laget for 100 % av klientkjøringer. Agent-systembruker i drift for ≥ 5 klienter. Samlehenting av skattekort for 1 000 personer på tvers av klienter < 15 min uten 429. «Send alle som er klare» sender 0 meldinger for klienter uten godkjent kjøring |
| **9** | 1.11.2027 | Pentest uten høye eller kritiske funn. DPIA-mal og art. 9-roller ferdig, og rådgiver har vurdert dem. Lagringsstedsregisteret viser at alt regnskapsmateriale ligger i Norge. Systembeskrivelse (E2.11) publisert. Gjenopprettingstest og beredskapsøvelse «Brutto nede T-2» gjennomført. Vakt bemannet 27.12–15.1, 1.–7.2 og juni |
| **M** | 1.12.2027, per kunde | Hittil i år lik avstemmingsrapporten (diff 0). Arbeidsforhold-ID og permisjons-ID 100 % bevart. Feriepengegrunnlag 2027 per person lik gammelt system (diff 0). Trekkpålegg migrert med KID kontrollert av to personer. To parallelle perioder lik på øret (direktekunder) eller én periode pluss historisk skygge (grønne byråklienter). Historisk skyggeberegning av juni 2027 uten uforklarte avvik. Gammelt system beholdes ≥ 3 måneder etter go-live (avtalefestet). Signert akseptprotokoll |
| **M** | 1.5.2028 (feriepenger) | Junikjøringen 2028 simulert i skygge for alle kohortkunder med migrert grunnlag. Lønnsfaglig har kontrollert 10 % av de ansatte manuelt med 0 uforklarte avvik. GC-04 og GC-05 grønne |
| **Fase 3** | 31.12.2028 | Strategiens port, pluss: 0 a-meldingsavvik som skyldes Brutto i 6 måneder på rad. 0 trekkbetalinger etter forfall som skyldes Brutto. 0 tapte NAV-refusjoner på grunn av fristen. ISAE type 2-perioden løper |

---

## (d) Epics

### d.1 Nye epics

| Id | Tittel | Mål | Fase |
|---|---|---|---|
| E0.11 | Fasitstyring | Gylne caser, regelpakker og a-meldingsmapping kan bare endres med lønnsfaglig signatur. Kodeagenter kan ikke endre fasit | 0 |
| E1.14 | Naturalytelser og fordeler | Fri bil (2027-modellen), elektronisk kommunikasjon og forsikringer gir riktig trekk og AGA, også ved lav kontantlønn | 1 (MVP-light) |
| E2.11 | Systembeskrivelse og lovpålagte lønnsrapporter | Beskrivelse etter bokføringsforskriften § 5-6, AGA per sats og sone (§ 3-1 nr. 9), versjonert per release | 1 |
| E3.0 | Myndighetsgateway, revisjonsspor og kontrollkø | Ett kontrollert punkt for alle myndighetskall med idempotens, saker (MYN-01–23) og agentpolicy [R2-myndighet §7] | 0–1 |
| E3.12 | Bidrag og manuelle trekk | Trekk fra brev (gamle regler, bidrag) med kreditor, KID, konto, prioritet og vernet beløp. Påminnelse når trekket ikke kan gjennomføres [R2-myndighet §7] | 1 (MVP) |
| E3.13 | Leverandøronboarding og avtaler | Alle scopes, vilkår, testdata og avtaler i test og produksjon. Slås sammen med ES.2 | 0 |
| E3.14 | NAV-refusjonsreskontro og K27 | Forskuttert, krevd og mottatt per ansatt og ytelse. K27 fra CSV (API når det er mulig). Varsel om 3-månedersfristen. Valg av AGA-metode | 1 (MVP) |
| E4.9 | Betalingskontroll og trekkforfall | Kontrollsum og hash på pain.001, forfallskalender med helligdager, trekk som eget oppdrag, bekreftet betalingsdato før a-melding, påminnelse T+1 | 1 (MVP) |
| E8.10 | GRFS-pakke light | Oppdragsdokumentasjon per klient og periode fra revisjonsloggen, registrering av godkjenning på e-post, lagret i byråets område i 5 år | 1 (MVP) |
| E9.8 | Personvern for særlige kategorier | DPIA-mal, rollen «Lønn – helse», maskering, slettefrister for helsedata, rådgivervurdering | 1 (MVP) |
| E9.9 | Lagringssted og oppbevaring | Register over alle lagre, alt regnskapsmateriale i Norge, backup etter bokføringsforskriften, eksport og arkiv ved opphør | 0–1 |
| EM.8 | Overgangsregler ved systembytte | Etterskuddsvis variabel lønn, pågående fravær, permisjons-ID, trekkpålegg, retting av gamle perioder, sammenstilling for EM.7-kunder | 1 |
| EM.9 | Historisk skyggeberegning | Juni 2027 og desember (2026 eller 2027) beregnet i Brutto med migrerte inndata og sammenlignet med gammelt system | 1–2 |

### d.2 Epics som bør endres

| Epic | Endring |
|---|---|
| E1.1 | Utvidede flagg (D-02), kombinasjonsvalidering mot kodelisten, karantene for nye lønnsarter |
| E1.5 | 60+, NAV-dager med FULL/BEGRENSET, trekkfritak for delårsansatte, kort med 12 måneder, overført ferie og forskuddsferie. Juniporten 1.5.2028 |
| E1.6 | AGP over migrering, snittinntekt for timelønte (§ 8-28), omsorgsdager, livssyklus for permisjons-ID, permitteringsteller |
| E1.7 | Sperre for trekk uten avtale (HR-2021-2532-A), vernet beløp som kundekonfigurasjon, fremføring og bortfall, samordnet trekk avslutter gamle |
| E1.8 | Inndata for OTP-premie og AGA-grunnlag per sone. Pensjonsinnretning i a-meldingen. 12G-tak med G-regulering |
| E1.9 | Differanse i timesats for overtid og tillegg i MVP eller senest 1.5.2028 |
| E1.12 | Svar fra Skatteetaten (D-09), betalende enhet, klassifisering med begrunnelse, 10 000-regelen |
| E1.13 | «Regelpakker og årshjul»: 1.1, 1.5, 1.7 og særavtaler, ikke bare 2028 |
| E2.3 | Dagslinjer for timelønte. Feltet `reiseregningKomplett`. Godtgjørelsesmotor |
| E2.10 | Versjonert fordeling, oppdeling av linjer, fryst kontering, største rest, validering mot regnskapets dimensjoner, avdeling på arbeidsforholdet |
| E3.2 | Meldingsstrategi mot F532, `kildesystem`, migrert historikk, hash-lås, XML-eksport |
| E3.4 | Pollebudsjett og kvoter per byrå, desemberbestilling, alle resultatkoder |
| E3.6 | Manuell migrering i MVP. API aktiveres per kunde etter første a-melding (februar 2028) |
| E3.7 | Delt: K27 og reskontro i MVP (E3.14). Inntektsmelding for sykepenger via API senest 1.4.2028. Foreldrepenger og sykdom i familien bak bryter |
| E3.8 | Sammenstilling 2027 for EM.7-kunder innen 31.1.2028 |
| E3.9 | Syntetiske tvillinger, semantisk diff mellom 2.3 og 2.4, 2–3 utviklermåneder reservert |
| E3.11 | Brreg bare. Aa-registeret kuttes |
| E4.1 og E4.2 | Trekk som eget oppdrag uten SALA, kontrollsum, helligdager (inn i E4.9) |
| E7.1 og E7.3 | Reservevei for ansatte uten BankID |
| E7.2 | Feriepengegrunnlag på slippen (aml. § 14-15) |
| E9.2 | Type 2-periode 1.7.–31.12.2028, rapport før 28.2.2029 |
| EM.6 | I tillegg: fraværshistorikk, trekkpålegg med KID, permisjons-ID, inntekt siste 3 måneder, etterslep av variabel lønn, permitteringsuker, hittil i år per a-meldingsbeskrivelse for plan B |
| EM.7 | Brutto AS egen lønn først. Sammenstilling 2027 avklart før start |

---

## (e) Gylne caser som mangler eller bør prioriteres

Forutsetninger som C §12 der ikke annet står. Fasiten fylles ut og signeres av lønnsfaglig. Beløp er bare oppgitt der regelen er sikker.

| Id | Case | Inndata (kort) | Forventet logikk og resultat | Før |
|---|---|---|---|---|
| GC-01 | Sykefravær over systemskiftet | Sykmeldt fra man 20.12.2027. Gammelt system har betalt AGP 20.–31.12 (12 dager) | AGP-dag 13–16 = 1.–4.1.2028. Refusjon fra 5.1.2028. Grunnlaget for inntektsmeldingen bruker importert inntekt for oktober–desember 2027 (§ 8-28) | 1.9.2027 |
| GC-02 | Etterslep av variabel lønn | Overtid i desember 2027, registrert i gammelt tidssystem, utbetales i Bruttos januarlønn | Utbetales én gang, i Brutto. Trekk og AGA etter 2028-reglene. Feriepengegrunnlag 2028. Opptjeningsperiode desember 2027. Gammelt system betaler ikke | 1.9.2027 |
| GC-03 | ID-kontinuitet | Pågående foreldrepermisjon 60 % (eksisterende permisjons-ID) og 50 % permittering | Januar 2028: samme arbeidsforhold-ID og permisjons-ID. Permittering rapporteres. Ingen avslutning og ny start | 1.9.2027 |
| GC-04 | Juni 2028 med 60+ og NAV-dager | Grunnlag 2027 = 900 000 fra gammelt system, tariff 12 %, fyller 60 i 2028, 30 sykepengedager refundert av NAV i 2027, valg BEGRENSET | 12 % trekkfritt. 2,3 % av min(grunnlag, 6G) trekkpliktig. Hvilken G som gjelder er [U]. Feriepenger for NAV-dager følger valget | 1.5.2028 |
| GC-05 | Trekkfritak i juni, delårsansatt og 12-månederskort | (a) Ansatt fra 1.9.2027, månedslønn 40 000. (b) Ansatt hele 2027 med kort på 12 trekkmåneder | (a) Feriepengene er trekkfrie, men det er ikke trekkfritak for junilønnen [U: eksakt regel]. (b) Fullt trekk i juni og desember | 1.5.2028 |
| GC-06 | Halvt trekk flyttet til november | Kundekonfigurasjon «halvt trekk i november». Tabellkort, prosentkort og 12-månederskort. Bonus i november | Halvt tabelltrekk bare på vanlig lønn i november, fullt i desember. Prosentkort og 12-månederskort uten halvering. Bonus fullt trukket | 1.9.2027 |
| GC-07 | Samordnet trekk avløser gammelt | Gammelt `utleggstrekkSkatt` 2 000 per måned (KID kravtype 03). Samordnet pålegg 3 500 per måned fra 1.3.2028 | Gammelt avsluttes fra start av samordnet. Ulike a-meldingskoder, kontoer og KID. MYN-16 lukkes bare når gammelt er avsluttet | 1.9.2027 |
| GC-08 | Samordnet trekk ved to utbetalinger | Beløpspålegg 6 000 per måned. Lønn 10.1 og bonus 20.1. Variant med prosentpålegg 20 % | Beløp: hele 6 000 i løpet av måneden. Prosent: 20 % av brutto ved hver utbetaling. Trekkdato = lønnsutbetalingsdato. Betaling neste virkedag per dato | 1.9.2027 |
| GC-09 | Avtalt trekk uten avtale, og negativ korrigering | Ulønnet permisjon registrert etter at perioden er låst. Ingen skriftlig avtale om trekket | `REQUIRES_WRITTEN_AGREEMENT`. Ingen automatisk trekk. Fordring på konto 1570. Med avtale: trekk innenfor vernet beløp | 1.9.2027 |
| GC-10 | F532 ved redusert trekk | Korreksjon som reduserer forskuddstrekket for lønnsutbetalingsdato 10.1 | Sendes som erstatning av meldingen for januar, ikke som egen melding med negativ sum. Lokal validering stopper feil vei | 1.9.2027 |
| GC-11 | Ekstrakjøring etter innsendt a-melding | A-melding for januar sendt 21.1.2028. Bonus utbetales fre 28.1.2028 | Erstatning med fullt innhold for januar. To sumlinjer for trekk per dato. Bonustrekket forfaller man 31.1.2028 | 1.9.2027 |
| GC-12 | Forfall rundt helligdager | (a) Lønn ons 12.4.2028. (b) Lønn tor 23.12.2027 | (a) Forskuddstrekket forfaller tir 18.4.2028 (skjærtorsdag til 2. påskedag er ikke virkedager). (b) Fre 24.12 eller man 27.12 [U: om julaften er virkedag] | 1.9.2027 |
| GC-13 | Styrehonorar og frilans | (a) Styremedlem uten skattekort får 40 000 i mars. (b) En ansatt får styrehonorar | (a) 50 % trekk, AGA, ingen feriepenger eller OTP, frilans-arbeidsforhold bare i mars. (b) Arbeidsforholdstype etter svar fra Skatteetaten [U] | 1.6.2027 |
| GC-14 | 10 000-regelen i skattefri organisasjon | Honorar 4 000 i mars, juni og oktober fra en § 2-32-organisasjon. Regelen «TERSKEL» | Oktober: hele 12 000 rapporteres, trekk fra grensen. AGA-grunnlaget rapporteres for alle tre månedene | 1.6.2027 |
| GC-15 | Honorarmottaker i annen sone | Sentralledd i sone I. Tillitsvalgt bosatt i sone IV får møtegodtgjørelse | Sone etter svar fra Skatteetaten [U]. Det samme for tapt arbeidsfortjeneste | 1.6.2027 |
| GC-16 | Kostnadsfordeling endres midt i måneden | Månedslønn 62 000. 100 % AVD10 til 14.3. Fra 15.3: 60 % PRO-A og 40 % AVD10. Kalenderdager | Linjen deles: 28 000 (1.–14.3) til AVD10. 34 000 (15.–31.3) fordelt 20 400 til PRO-A og 13 600 til AVD10. AGA og feriepenger fordeles proporsjonalt. Summen stemmer på øret | 1.9.2027 |
| GC-17 | AGA av OTP-premie fra faktura | Premie 30 000 betalt 15.2.2028. Pensjonsgrunnlag 70 % i sone I og 30 % i sone III | AGA-grunnlag «tilskudd og premie»: 21 000 × 14,1 % = 2 961 og 9 000 × 6,4 % = 576, til sammen 3 537, i februar [U: tidspunkt og om administrasjonskostnad inngår] | 1.9.2027 |
| GC-18 | NAV-refusjon, valgt metode og avvik | C #12. Refusjon beregnet til 24 032. K27 viser 23 500 | Metode «ved mottak»: AGA-grunnlaget reduseres med 23 500 i måneden K27 viser. Metode «forskuttering»: forskutteringsmåneden korrigeres med 532. Aldri begge | 1.9.2027 |
| GC-19 | Omsorgsdager | Tre barn, 12 dager med sykt barn i 2028 | 15 dager kvote. Arbeidsgiver dekker dag 1–10. Dag 11–12 gir refusjonsgrunnlag (dagsats med 260 som divisor). Ingen permisjon i a-meldingen | H2 2028 |
| GC-20 | Gradert sykmelding for timelønt | 50 % sykmeldt. Ujevn inntekt siste 3 måneder | AGP-lønn per planlagt arbeidsdag etter snittet (§ 8-28). Riktig AGP-telling ved gradering | 1.9.2027 |
| GC-21 | Kundens egen lønnsart med feil flagg | Importert lønnsart «Bonus» med trekkmetode tabell og uten pensjonsgrunnlag | Karantene. Valideringen krever prosenttrekk og avklart pensjonsgrunnlag før bruk. Ingen kjøring før lønnsfaglig har godkjent | 1.6.2027 |
| GC-22 | Skattekort mangler, og nytt kort kommer etter godkjenning | `ikkeSkattekort` ved beregning. Nytt kort hentet etter godkjenning, før utbetaling | 50 % trekk ved beregning. MYN-15: varsel og valg mellom ny beregning og bruk fra neste kjøring. Ingen henting for `registrertSomDoed` | 1.9.2027 |

**Også prioritert fra C §12, «anbefalte tilleggscaser»:** fri bil med lav kontantlønn (C #19, nå med 2027-modellen), for mye utbetalt i november 2027 med avtale om tilbakebetaling i februar 2028 (bruttometoden og erstatning for 2027-11 fra riktig system), import av timelønn med bare månedssum (skal avvises), og permittering etter permisjon med 26-ukersteller over migrering.

---

## (f) Beslutningene B1–B30: strategiens anbefaling vurdert faglig

| Id | Strategiens anbefaling | Vurdering | Begrunnelse eller presisering |
|---|---|---|---|
| B1 | Behold frittstående lønn | **Enig** | – |
| B2 | Endre: fas inn API-mekanismene | **Enig, med presisering** | Lønnsgrunnlags-kontrakten må fra dag én bære faktafelt som avgjør skatt: dagslinjer for timelønte og `reiseregningKomplett` (D-11, D-12) |
| B3 | Endre segment for kohort 1 | **Enig, med presisering** | Hold også utenfor: ambulerende AGA, utsendte, sjøfolk, Svalbard, nettolønnsavtaler, konsern som deler fribeløp, lokallag med eget organisasjonsnummer og organisasjoner med tapt arbeidsfortjeneste før Skatteetaten har svart |
| B4 | Behold programvare, ikke tjeneste | **Enig, med presisering** | Grensen må holde i support, migrering og garanti (D-35) |
| B5 | Endre: ikke uttrykksspråk i MVP | **Enig, med presisering** | Sjurs lønnsartmodell trenger flere flagg (D-02) |
| B6 | Endre: avgrens bitemporalitet | **Delvis enig** | Listen må utvides. Implementer som bare-tilføyende versjoner pluss kjøringssnapshot, ikke som generelt spørrelag (D-38) |
| B7 | Endre: én celle til første store kunde | **Enig** | – |
| B8 | Lås Kotlin innen 1.12.2026 | **Enig i datoen, uenig i begrunnelsen** | Trekkrutinen mangler lisens. Valget bør følge tech lead. TypeScript er forsvarlig med fire vilkår (b.4.1) |
| B9 | Endre: backup også i Norge | **Enig, med presisering** | Bekreft Norway West eller norsk backupleverandør. Avklar § 7-5 mot § 7-7. Ingen lønnsdata eller revisjonslogg i EU-verktøy (D-32) |
| B10 | Behold Maskinporten og systembruker | **Enig, med presisering** | REGN-rolle eller delegering, kvote på 5 samtidige kall, ikke Krav og betalinger for byrå (D-21). ID-porten er ikke innlogging for brukere. Gründerens «ID-porten» betyr Maskinporten og systembruker |
| B11 | Behold versjonsuavhengig aggregat, 2.4 fra 2028 | **Enig, med presisering** | Syntetiske tvillinger, F532, gammelt system i 3 måneder (D-16, D-19, D-20) |
| B12 | Behold: Brutto flytter aldri penger | **Enig, med presisering** | Kontrollsum og hash på filen. Trekk som eget oppdrag (D-24, D-46) |
| B13 | Endre: ingen KI i produksjon før Q4 2028 | **Enig** | Kodeagenter trenger egne grenser (D-48) |
| B14 | Endre: BankID og passkey i MVP, SSO i 2028 | **Enig, med presisering** | Reservevei for ansatte uten BankID må være standard i MVP (D-49) |
| B15 | Endre: ISAE type 1 per 30.6.2028 | **Enig, med presisering** | Type 2-periode 1.7.–31.12.2028 med rapport før revisjonssesongen 2029. Kontroller med bevis fra 1.1.2028 (b.6.1) |
| B16 | Endre: hittil i år fra start, to perioder parallelt | **Enig, med presisering** | Fasit er innsendt innhold (XML eller JSON). Historisk skygge av juni. Én periode for grønne byråklienter bare med historisk skygge (D-17, EM.9) |
| B17 | Endre prismodell | **Ingen faglig merknad** | Enheten «mottaker med utbetaling i måneden» passer med frilans-arbeidsforhold som bare rapporteres i utbetalingsmåneder |
| B18 | Behold mottakere uten arbeidsforhold, med egen epic | **Enig, med presisering** | Klassen hører til utbetalingen. Avklaringer fra Skatteetaten før kohort 1 (D-09, D-40) |
| B19 | Endre: kohort 1.1.2028, tidlig drift fra 1.10.2027 | **Enig, med presisering** | EM.7 utløser sammenstilling 2027 fra Brutto. Brutto AS først. Ingen kohortkunde med lønnsdag før 15.1.2028 (D-27, D-53, D-55) |
| B20 | Endre: fraværskjerne i MVP, moduler senere | **Enig i kjerneflyttingen** | Gründerkravet står. Rekkefølge og minimum i b.5.1 |
| B21 | Endre: Huma-kobling Q3 2028 | **Enig, med presisering** | Fravær fra Huma bare med avstemming før cut-off. Konto og fødselsnummer aldri fra Huma (D-41) |
| B22 | Omfangsregel | **Enig, med presisering** | Lovendringer (2.4, regelpakker, nye forretningsregler) er ikke «nye krav». Reserver ca. 15 % kapasitet til regelverksendringer [A] |
| B23 | Kapital | **Utenfor fagmandatet** | – |
| B24 | Beregningsgaranti | **Enig, med presisering** | Skriv «vi dekker», ikke «vi retter lønnen». Tak, dekker dokumenterte renter, tilleggsskatt, tvangsmulkt og gebyrer. Jurist vurderer mot regnskapsførerloven (D-35) |
| B25 | Kohortgrense | **Enig** | – |
| B26 | Go/no-go-datoer | **Enig, med presisering** | Legg til 22.12.2027 (regelår 2028), 7.2.2028 (første 2.4) og 1.5.2028 (feriepenger) som formelle porter |
| B27 | Kjøp alt rundt motoren | **Enig, med presisering** | Trekkrutinen kan ikke kjøpes. Lisensen avklares, ellers implementeres den fra tabellene |
| B28 | Lønnsfaglig vetorett | **Enig, med presisering** | Gjelder også gylne filer, regelpakker og agentskrevet kode i kjernen. Krever stedfortreder, så vetoretten ikke stopper ved ferie |
| B29 | Integrasjon før modul | **Presisering** | Gjelder modulenes brukerflate, ikke kjernelogikken. Gründerkravet om egne moduler står fast. Faglig minimum og rekkefølge i b.5.1 |
| B30 | Ekstern posisjonering | **Utenfor fagmandatet** | Huma-koblingen krever likevel databehandleravtale i hele kjeden |

---

## (g) Åpne faglige spørsmål

| # | Spørsmål | Hvem avklarer | Frist |
|---|---|---|---|
| 1 | Får vi bruke Skatteetatens trekkrutine (Java) uten lisensfil? Også bare som testorakel? | Skatteetaten og jurist | 1.12.2026 |
| 2 | Gjelder F532 per melding eller per kalendermåned? Hvilken meldingsstrategi anbefales ved flere kjøringer i måneden? | Skatteetaten | 1.3.2027 |
| 3 | Rettes 2027-perioder etter 1.1.2028 i format 2.3 eller 2.4? Finnes manuell XML-opplasting for 2.4? | Skatteetaten | 1.9.2027 |
| 4 | Algoritmen for kontrollsifferet i KID (posisjon 18–19) og terminkoden for AGA | Skatteetaten | 1.3.2027 |
| 5 | Er 24.12 og 31.12 virkedager ved forfall av forskuddstrekk? | Skatteetaten | 1.6.2027 |
| 6 | Tapt arbeidsfortjeneste, styrehonorar til ansatt, AGA-sone for frilans og 10 000-grensen per organisasjon | Skatteetaten | 1.6.2027 |
| 7 | Halvt trekk ved 14-dagers- og ukelønn, prosentkort og trekkfritak i juni for delårsansatte | Skatteetaten | 1.6.2027 |
| 8 | AGA av OTP-premie: betalingstidspunkt, administrasjonskostnader og fordeling per sone | Revisor og Skatteetaten | 1.3.2027 |
| 9 | Får byrået `regnskapsforer-lonn` uten REGN-rollen, ved delegering fra klienten? Gjelder kvoten på 5 samtidige kall byrået eller hver klient? | Digdir/Altinn og Skatteetaten | 1.3.2027 |
| 10 | Får en privat leverandør ID-porten-klient for klientdelegerings-API-et? Når kommer den utvidede systembrukermodellen? | Digdir | 1.3.2027 |
| 11 | Status for inntektsmelding for foreldre- og svangerskapspenger og sykdom i familien via LPS. Gjelder Min side for omsorgspenger fortsatt? | NAV | 1.3.2027 |
| 12 | Kommer bidragstrekk i Trekkpålegg-API-et, eller som brev? | Skatteetaten (Innkrevingsmyndigheten) | 1.6.2027 |
| 13 | Hjemmel og frist for sammenstillingsoppgaven. Kan gammelt system lage den for 2027 når Brutto har rapportert oktober–desember? | Jurist og Skatteetaten | 1.6.2027 |
| 14 | Riktig paragraf for lagring i utlandet (§ 7-5 eller § 7-7). Krever bokføringsforskriften backup på et annet sted? | Revisor | 1.12.2026 |
| 15 | Får vi Azure Norway West, eller må backup ligge hos en norsk leverandør? | Microsoft og tech lead | 1.12.2026 |
| 16 | Beregningsgarantien, implementeringsstøtte og gratis migrering mot regnskapsførerloven § 2-1 | Jurist | 1.3.2027 |
| 17 | Behandlingsgrunnlag og DPIA for helse og fagforening. Slettefrist for sykmeldinger og søknader | Personvernrådgiver | 1.9.2027 |
| 18 | Holder fast arbeidsplan med registrerte avvik som oversikt etter aml. § 10-7? | Arbeidstilsynet | Før timemodulen designes |
| 19 | Utvidelse av lønnsartmodellen (D-02). Hvordan kommer OTP-premien inn (manuelt eller fra regnskap)? Hvilken AGA-metode for NAV-refusjon er standard? | Gründer (Sjur) | 1.2.2027 |
| 20 | Hvem er EM.7-kundene, og godtar gründeren at Brutto AS er først? | Gründer | 1.3.2027 |
| 21 | Hvem eier MVA og bilagskrav for utlegg: Utleggsappen, regnskapet eller Brutto? | Gründer og revisor | Før utleggsmodulen |
| 22 | Krever bankene pain.001.001.03 eller .09, og godtar de trekk som eget oppdrag uten SALA i samme fil? | Pilotbankene | 1.6.2027 |

---

## Kilder brukt

- `plan/skjelett-v0.md`, `research/R3-kritikk-strategi.md` (kap. 2–4, 7, 12)
- S-avklaringer §1–§7
- B §0, §1.2–1.4, §2.3–2.10, §3.1, §4, §6, §7, §8, §10–§15
- C §0, §2, §3, §4.2, §5, §6, §7, §9, §10, §11, §12, §13
- F §0, §1.3–1.10, §3, §4, §6, §7, §8, §9, §10
- D §0, §1, §2, §3, §4
- E §1, §2, §8.3
- R2-myndighetsintegrasjoner §0–§8
- R2-moduler-integrasjoner §0–§4, §9–§10
- R2-ansatt-org §0–§2, §9, §12–§13
- R2-okosystem §2.2–2.4, §4.4.6–4.4.8, §5.1
- R2-ansattdata-tripletex-reai §0, §E, §F
- R2-virksomhet §0, §5.1, §5.7, §7
- R2-byra §0, kap. 2 (BY-01–BY-45)
