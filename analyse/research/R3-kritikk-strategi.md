# R3 – Strategisk kritikk av skjelett-v0 for Brutto

Dato: 2026-10-28. Rolle: strategisk skeptiker, skrevet som en investor og produktsjef som har sett to lønnsoppstarter feile.

Grunnlag: `plan/skjelett-v0.md`, runde 1 (A, D, E, F, G, med oppslag i B og C), runde 2 (R2-virksomhet, R2-byra, R2-ansatt-org, R2-okosystem) og S-avklaringer. Henvisninger står i hakeparentes, for eksempel [F §9.7]. Egne anslag er merket (anslag). Fakta jeg ikke har sjekket, er merket (verifiseres).

**Leseveiledning**
- Kap. 1: dommen (a).
- Kap. 2: omfang mot team, med regnestykke.
- Kap. 3: konkrete endringer i skjelettet med id-er (b).
- Kap. 4: MVP-listen (c).
- Kap. 5–7: moduler mot integrasjoner, segment og tidslinje.
- Kap. 8: revidert faseplan (d).
- Kap. 9–10: pris, økonomi og konkurrentenes svar.
- Kap. 11: topp 10-risiko (e).
- Kap. 12: beslutningene B1–B21 og nye beslutninger (f).
- Kap. 13: spørsmål gründeren må svare på (g).

---

## 1. Dom (a)

1. Skjelettet er en god produktvisjon og en dårlig plan for 2027.
2. Det har 14 spor og 116 epics (96 uten S, 10 og 11). Lønnskjerne, plattform-API, tre egne moduler, tre partnerkontrakter, Huma-kobling, byråkonsoll og sertifisering skal inn i de samme 11 månedene fram til pilot.
3. Med 5–7 utviklere og 1–2 lønnsfaglige rekker teamet 40–45 utviklermåneder før parallellkjøringen starter i oktober 2027 (anslag). Bare MVP-en i kap. 4 trenger rundt 60. Hele skjelettet trenger 250–400.
4. Skjelettet mangler et kapasitetsregnestykke, datoer på portene, go/no-go-kriterier, en plan B for 1.1.2028 og et økonomispor med kapitalbehov.
5. Flere beslutninger trekker hver sin vei. Egen utleggsmodul (B20) undergraver like vilkår (B2) for søsterproduktet Utleggsappen. Målet om å erstatte Huma (B21) gjør oss avhengige av API-et til en framtidig konkurrent. DR i EU (B9) koster kundene en meldeplikt som data i Norge ellers sparer dem for [S §1 pkt. 4].
6. Segmentvalget «30–300 med tariff» (B3) peker på den tyngste lønnen i markedet og på kundene som har mest å tape på å bytte.
7. Tre ting kan drepe selskapet: én kjent lønnsfeil, en forsinkelse som skyver første kohort til 2029, og kapital som tar slutt før kohorten har kjørt feriepenger.
8. Riktig plan er smal: lønnskjerne, myndigheter, regnskaps- og bankfil, en enkel ansattportal og migrering for én kohort på maks 12 kunder 1.1.2028.
9. Alt annet kommer etter at kohorten har kjørt feriepenger i juni 2028 uten feil.

---

## 2. Omfang mot team

### 2.1 Hva teamet rekker før pilot (anslag)

Norske seniorutviklere har normalt 3 måneders oppsigelse. Den som signerer i november, begynner i februar.

| Periode | Utviklere i snitt | Måneder | Utviklermåneder |
|---|---|---|---|
| Nov 2026–jan 2027 | 1,5 (tech lead og én innleid) | 3 | 4,5 |
| Feb–mar 2027 | 3,5 | 2 | 7 |
| Apr–sep 2027 | 6 | 6 | 36 |
| **Brutto til 30.9.2027** | | | **≈ 47** |
| Minus 30 % til drift, møter, myndighetstesting, feilretting, rekruttering og opplæring | | | ≈ 33 |
| Pluss kodeagenter: ×1,5 på de ca. 60 % som er ren koding | | | **≈ 43** |
| Okt–des 2027 med halv kapasitet til nytt arbeid (resten går til pilot, a-melding 2.4 og regelår 2028) | 6 | 3 | + ≈ 10 |
| **Til 1.1.2028** | | | **≈ 50–55** |

F anslår selv 5–7 utviklere og 1–2 lønnsfaglige for en plan som bare har fundament, kjernelønn, byrå og migrering fram til januar 2028 [F §9.7]. Skjelettet la til spor 5, 6 og 11, bank-API, Huma, OrgLab, Tikket og ISAE før drift, uten å legge til folk.

### 2.2 Hva skjelettet krever

- 116 epics. Med 2,5–3,5 utviklermåneder i snitt for fullt omfang blir det **250–400 utviklermåneder** (anslag).
- MVP-en i kap. 4 berører 55 epics, men hver er skåret ned til MVP-omfang. Den er **ca. 60 utviklermåneder** (kap. 4.5).
- **Konklusjon:** Skjelettet er 5–8 ganger større enn kapasiteten fram til pilot. Selv MVP-en ligger på grensen. Den går bare opp hvis 2–3 innleide seniorer starter i desember 2026, alt rundt motoren kjøpes, og listen i 2.5 brukes hvis kapasiteten svikter.

### 2.3 Lønnsfag er den egentlige flaskehalsen

Kodeagenter gjør koding raskere. De lager ikke fasit, de tester ikke i TT02, de migrerer ikke en kunde og de svarer ikke i telefonen på lønnsdagen.

| Lønnsfaglig arbeid i 2027 | Timer (anslag) |
|---|---|
| 300 gylne caser for 2026–2028 med fasit og signatur | 600 |
| Regelpakker og satser for 2027 og 2028, trekkrutine og a-meldingskoder | 250 |
| Gjennomgang av beregningsresultater og avvikslister fra test | 400 |
| Lønnsartkatalog, kontering og maler (bygger på Sjurs katalog [S §6]) | 150 |
| Migrering og mapping for 10–12 pilotkunder (ca. 40 t per kunde) | 450 |
| Parallellkjøring: 2 perioder × 10–12 kunder × 8 t | 180 |
| Hjelpetekster, supportrutiner og opplæring av pilotbyråer | 250 |
| Spesifikasjon og akseptanse av a-melding 2.4 | 120 |
| **Sum** | **≈ 2 400** |

Én lønnsfaglig gir ca. 1 400–1 500 produktive timer i året [E §5.3]. **To lønnsfaglige må være på plass senest 1.2.2027.** Med én lønnsfaglig feiler planen, uansett hvor mange utviklere og agenter teamet har.

### 2.4 Kutt, utsett og kjøp

**Kuttes** (ut av roadmapen til en betalende kunde ber om det):

| Epic | Hvorfor |
|---|---|
| E4.7 Straksutbetaling av refusjoner | Ingen utbetalings-API og liten verdi [G §0 pkt. 9] |
| E5.11 Partnerprogram | For tidlig før 30–50 integrasjoner [G §0 pkt. 10], [R2-byra §7 nr. 13] |
| E6.7 Reiseregning | Utleggsappen gjør det bedre [R2-virksomhet §9] |
| E7.6 Spør lønnsslippen | Deterministisk forklaring gir det meste av verdien [R2-ansatt-org §9.1]. Lønnsdata går ikke til språkmodell i første versjon [S §3 pkt. 11] |
| E10.5 Tidsreise og sandkassekopi som UI | Bitemporale data i kjernen holder |
| E10.6 Unified-API | Ingen bekreftet norsk dekning [G §5] |
| E10.7 Enterprise-pakke | 300–1000 ansatte kommer tidligst i 2030 |
| E11.5 Medarbeidersamtaler og E11.6 Utstyr | Overlates til partnere [R2-okosystem §6.4] |
| E3.10 ID-porten for personer | Ansatte logger inn med BankID via megler (E0.3). ID-porten brukes bare i Skatteetatens egne reserveportaler [B §13 rad 7 og 9] |
| Folkeregisteret i E3.11 | Krever hjemmel og avtale. Skattekortet verifiserer fødselsnummeret [R2-okosystem §4.4.6] |

**Utsettes:** Se faseplanen i kap. 8. Hovedtrekkene er spor 5 og 6 (unntatt E5.3 og fraværskjernen), spor 10 og 11, E0.10, E1.10, E2.7, E3.7, E3.8, E4.5, E4.6, E4.8, E7.4, E7.7, E8.4–E8.9, E9.1 og E9.2.

**Kjøpes eller gjenbrukes:**

| Hva | Hvordan | Sparer (anslag) |
|---|---|---|
| Tabelltrekk | Skatteetatens trekkrutine i Java (`Skatteetaten/trekktabell`) brukes direkte på JVM. Repoet har ingen lisensfil, så retten til gjenbruk må avklares [B §0 pkt. 5], [C §0 pkt. 5] | 1–2 utviklermåneder og mye risiko |
| BankID og e-signering | Megler (for eksempel Signicat eller Criipto) (verifiseres pris) | ca. 2 |
| Innlogging for administratorer | Administrert IdP i EU [F ADR-13] | 1–2 |
| Testdata | Tenor [F §7.4] | – |
| PDF, e-post og overvåking | Standardbibliotek og administrerte tjenester i Norge eller EU | ca. 1 |
| Lønnsfaglig kvalitetssikring | Kjøp 150–250 timer fra lønnsavdelingen i et byrå eller en lønnsrevisor som lager og signerer gylne caser | Fasit som ikke er vår egen |
| Pentest og ISAE | Kjøpes. Ingen egen compliance-stab før 2028 | – |
| Bank | pain.001-fil. Ingen bankavtaler i 2027 | 3–6 |
| Sykepengelogikk | NAVs åpne kode (`navikt/helse-spleis`, Kotlin) som referanse [F, kildeliste] | – |

**Vurdert og forkastet:** å kjøpe eller lisensiere selve lønnsmotoren, for eksempel via Intects API eller et oppkjøp av NettLønn. Det kunne gitt 6–12 måneders forsprang. Den varige fordelen ligger likevel i beregningssporet, retro og a-melding-aggregatet [A §6.1 pkt. 2], [G del 3 #3]. Kjøper vi motoren, gir vi bort fordelen. Et oppkjøp av en *kundebase* kan vurderes i 2029, særlig hvis ECIT faser ut NettLønn (verifiseres) [A §0 pkt. 4].

### 2.5 Kuttes sist hvis kapasiteten svikter før 1.9.2027

I denne rekkefølgen:
1. PowerOffice Go-adapteren. Behold Tripletex-API og generisk fil.
2. Klient-systembruker. Bruk standard systembruker per klient, godkjent av klienten i Altinn.
3. Byråets arbeidskø. Bruk en tenantvelger med status per klient.
4. Automatikk i sluttoppgjør. Bruk sjekkliste og manuelle linjer.
5. Ansattportalen. Send lønnsslipp kryptert eller via Digipost, og ta kontonummerendring på signert skjema med fire øyne. Dette er siste utvei, fordi kontonummer-skjoldet da blir manuelt.

---

## 3. Konkrete endringer i skjelettet (b)

### 3.1 Spor

| Spor | Endring | Begrunnelse |
|---|---|---|
| S | Beholdes. Får port 31.3.2027 og fire nye epics (ES.7–ES.10). ES.5 begrenses til intensjonsbrev og høring på lønnsgrunnlagskontrakten | Uten team, piloter og kapital innen mars ryker 1.1.2028 |
| 0 | Slankes. E0.10 flyttes til Fase 3. E0.8 begrenses til kontrakt-først API-rammeverk for egne flater og lønnsgrunnlag. E0.3 får SSO først i Fase 3 | |
| 1 | Kritisk sti. Tar inn kjernen fra E6.1–E6.3 (feriesaldo, ferietrekk, egenmelding, arbeidsgiverperiode, permisjon og permittering). E1.10 flyttes til Fase 3. Får E1.12 og E1.13 | Regler med rettsvirkning hører i kjernen [R2-virksomhet §5.7 pkt. 3] |
| 2 | Tar inn E5.3 i E2.3. E2.7 flyttes til Fase 3 | Én vei inn: CSV-importen er første klient av lønnsgrunnlag-API-et |
| 3 | Porten deles i 3a (a-melding 2.3, 1.9.2027) og 3b (a-melding 2.4, 1.12.2027). E3.7 og E3.8 flyttes til Fase 3. E3.10 kuttes | Testmiljøet for 2.4 åpner 15.9.2027 [B §12] |
| 4 | Slankes til betalingsforslag, pain.001 og bilag. E4.2 deles: pain.001 nå, pain.002 og camt.054 i Fase 3. E4.5 og E4.6 til Fase 3. E4.7 kuttes. E4.8 til Fase 4 | |
| 5 og 6 | Slås sammen til «5 Plattform og egne moduler» i Fase 3–4. Id-ene E6.x beholdes for sporbarhet | Begge forutsetter stabil kjerne og offentlig API |
| 7 | E7.1 (lett webportal), E7.2, E7.3 og E7.5 i MVP. E7.4 til Fase 3. E7.6 kuttes. E7.7 slås sammen med E11.3 i Fase 4 | E7.7 og E11.3 overlapper |
| 8 | E8.1 (lett arbeidskø), E8.2 og E8.3 i MVP. E8.4–E8.7 til Fase 3. E8.8 og E8.9 til Fase 4 | Byrået kjøper minutter per slipp [R2-byra §0 pkt. 1] |
| 9 | Deles i drift og sikkerhet (E9.3–E9.6, ny E9.7) i MVP og sertifisering (E9.1, E9.2) i Fase 3–4 | ISAE er salgskrav fra ca. 250 ansatte [R2-virksomhet §6 pkt. 10] |
| M | Starter i Fase 1, parallelt med spor 1–4. Får EM.6 og EM.7 | Migreringskit må være ferdig før parallellkjøring |
| 10 | Flyttes til Fase 4. «Første kunde over 300» flyttes til 2030 | |
| 11 | Legges under spor 10 i Fase 4. E11.1 flyttes til spor 5 i Fase 3. Datamodellkravene (OK-170, OK-173, OK-175, OK-181) flyttes inn i E0.4 og E2.1 | Å erstatte Huma er et nytt produkt med en ny kjøper [R2-virksomhet §2.4.1] |

### 3.2 Porter

Portene i v0 er kvalitetskrav uten dato. Uten dato styrer de ikke noe.

| Spor | Ny port | Dato |
|---|---|---|
| S | Tech lead, minst 4 utviklere og 2 lønnsfaglige har signert. 2 byråer og 5 direktekunder har signert pilotavtale eller intensjonsbrev. Maskinporten-klient og systemregistrering er godkjent for TT02. Finansiering for minst 24 måneder er sikret | 31.3.2027 |
| 0 | **Gående skjelett:** Én ansatt med fastlønn og tabelltrekk går fra registrering til beregning, a-melding 2.3 godkjent i TT02, bilagsfil og pain.001-fil. Fødselsnummer og kontonummer er feltkryptert. Revisjonslogg og tilgangspolicy er testet | 31.3.2027 |
| 1 | Minst 300 gylne caser for 2026–2027 i MVP-omfang, signert av lønnsfaglig ansvarlig, regner likt på øret. Tabelltrekk treffer trekkrutinen 100 % på et tilfeldig utvalg av 10 000 kombinasjoner. Samme input gir byte-lik output. Ingen åpne feil i trekk, AGA eller feriepenger | Delmål 1.6.2027, port 1.9.2027 |
| 2 | Full lønnsmåned for to syntetiske virksomheter fra cut-off til godkjent kjøring på under én arbeidsdag: et AS med 150 ansatte, timelønn og fravær, og en forening med 40 ansatte og 200 honorarmottakere. Avvikslisten klassifiserer minst 70 % av avvikene automatisk. Korreksjonskjøring endrer aldri en godkjent kjøring. Samme importfil to ganger gir ingen dobbel linje | 30.9.2027 |
| 3a | A-melding 2.3 for tre testvirksomheter godkjent i TT02 uten avvik, også erstatningsmelding. Skattekort hentet via API. KID for forskuddstrekk og utleggstrekk er riktig | 1.9.2027 |
| 3b | A-melding 2.4 godkjent i testmiljøet for de samme virksomhetene. Første produksjonsmelding for 2028-01 sendt innen 5.2.2028 uten avvik som skyldes Brutto | 1.12.2027 og 5.2.2028 |
| 4 | pain.001 akseptert i bankene pilotkundene bruker (minst to). Bilag bokført i Tripletex og PowerOffice Go og lest inn som generisk fil i ett tredje system. Lønn, a-melding og bilag avstemmer i null for alle pilotkunder | 30.9.2027 |
| 5 (sammenslått) | En ekstern kilde (Utleggsappen eller annen) leverer lønnsgrunnlag via offentlig API uten spesialtilgang. Byttetest mellom egen fraværsmodul og en ekstern kilde gir likt lønnsresultat | 31.12.2028 |
| 7 | Pilotansatte logger inn med BankID og ser lønnsslippen med forklaring per linje. Nytt kontonummer krever BankID-steg, karantene og varsel. Ingen beløp i varsler | 30.9.2027 |
| 8 | Pilotbyrået kjører egen lønn i produksjon fra oktober 2027 og minst 5 klienter fra januar 2028. Skattekort for alle klienter hentes i én operasjon. A-meldinger sendes per klient med port | 31.1.2028 |
| 9 | Pentest uten høye eller kritiske funn. DPA og underleverandørliste er klare. Backup og gjenoppretting er testet i Norge. Vakt 27.12.2027–15.1.2028 er bemannet | 1.11.2027 |
| M | Hver direktekunde har to perioder på rad lik på øret før produksjon. Byråets grønne klienter trenger én periode og byråets signatur. Go/no-go per kunde 1.12.2027. Første ordinære a-melding for 2028-01 sendt fra Brutto | 1.12.2027 og 5.2.2028 |
| 10 | Kohort 2 (1.1.2029): minst 25 nye kunder eller 15 000 slipper per måned. Første kunde over 300 ansatte i 2030 | 31.12.2028 |

### 3.3 Epics som flyttes

| Epic | Fra | Til | Merknad |
|---|---|---|---|
| E5.3 Lønnsgrunnlag-API | Spor 5 | E2.3, MVP | CSV-importen er første klient |
| Kjernen i E6.1 og E6.2 (feriesaldo, ferietrekk, egenmelding, AGP) | Spor 6 | E1.5 og E1.6, MVP | Rettsvirkning |
| Kjernen i E6.3 (permisjon og permittering) | Spor 6 | E1.6, MVP | Permisjon må rapporteres i a-meldingen |
| E6.5 Turnus og tillegg (import) | Spor 6 | E2.3 (generisk import) | Ingen egen turnusimport |
| E1.10 Tariff og lønnsstiger | MVP | Fase 3 (H2 2028) | Ingen stiger i kohort 1 |
| E2.7 Lønnsoppgjør | MVP | Fase 3, før 1.5.2028 | Lønnsoppgjør i AS har ofte virkning fra mai |
| E3.7 NAV | MVP | Fase 3 (Q2 2028) | Reservevei i NAVs portal. NAVs kilder spriker om hva som kan sendes fra lønnssystem [B §0 pkt. 6] |
| E3.8 Årlige rapporter | MVP | Fase 3, frist 31.1.2029 | Sammenstillingsoppgaven for 2027 lages i forrige system |
| E4.5 Pensjonsleverandører | MVP | Fase 3 (KLP-fil, verifiseres format) og Fase 4 (API) | |
| E4.6 Avstemmingsrobot | MVP | Fase 3 | Avstemming lønn mot a-melding er med i E3.3 |
| E7.4 Lederinnboks | MVP | Fase 3 | Krever moduler eller eksterne kilder |
| E8.4–E8.7 | MVP | Fase 3 | |
| E9.2 ISAE 3402 | Før drift | Type 1 per 30.6.2028 | |
| E9.1 ISO 27001 | 2028 | 2029 | |
| E0.10 KI-gateway | Fase 0 | Fase 3 (Q4 2028) | |
| E11.1 Huma-kobling | Spor 11 | Spor 5, Fase 3 | Tidligere bare hvis en kohort 1-kunde krever det |
| E5.1, E5.2, E5.4, E5.10 | 2027 | Fase 3 | Offentlig API med portal når kjernen er stabil |
| E5.5, E5.6 | 2027 | Fase 3 | CSV-reserve i MVP |
| E5.7, E5.8, E5.9 | 2027 | Fase 4 | |
| E6.1, E6.2 (selvbetjening) | 2027 | Fase 3 (H2 2028) | |
| E6.4, E6.6, E6.8 | 2027 | Fase 4 | E6.6 bare hvis B29 utløses |
| E4.8 Direkte bank-API | «Senere» | Fase 4 | |

### 3.4 Epics som legges til

| Ny id | Tittel | Fase | Hvorfor |
|---|---|---|---|
| ES.7 | Kapital og runway | 0 | Kapitalbehov 60–70 MNOK før break-even (kap. 9.4) |
| ES.8 | Kunde- og prisvalidering: 15 intervjuer med fagledere for lønn i byrå og 10 med organisasjoner | 0 | Portaladopsjon og pris er de største antakelsene [R2-byra §8 spm. 1 og 6] |
| ES.9 | Beregningsgaranti, ansvarstak og ansvarsforsikring | 0–1 | Tillit for en ny leverandør [E §10.8], [R2-byra §2.7] |
| ES.10 | Produktdesign og brukertesting (0,5–1 designer) | 0–3 | Brukervennlighet er hovedargumentet [A §6.1 pkt. 1]. Skjelettet har ingen designkapasitet |
| E1.12 | Mottakerklasser, honorar og styrehonorar | 1 | B18 har ingen epic. Kjernen i organisasjonsnisjen [R2-ansatt-org §0 pkt. 1–4] |
| E1.13 | Regelår 2028: statsbudsjett, trekktabeller og satser | 2 | Januarlønnen 2028 avhenger av regler som publiseres i desember |
| E9.7 | Lønnsfaglig support og implementering, 2 personer fra 1.9.2027 | 1–2 | Support i lønnsuka er det byråene betaler for [R2-byra §4.2] |
| EM.6 | Saldoer hittil i år og feriepengegrunnlag fra forrige system | 1 | Gir plan B-datoer, byråbølger og riktig feriepengeutbetaling i juni 2028 |
| EM.7 | Tidlig skarp drift for 1–2 lavrisikokunder fra 1.10.2027 | 2 | Ekte a-meldinger og ekte lønnsdager før januar |

I tillegg deles fire epics i to deler, uten nye id-er:
- **E1.5:** opptjening og fratreden i MVP. Juniutbetaling med frist 1.5.2028.
- **E1.9:** korreksjon og enkel retro i MVP. Retro med følgevirkninger i Fase 3.
- **E3.6:** manuell registrering av trekkpålegg i MVP. Trekkpålegg-API i Fase 3.
- **E3.11:** Brreg i MVP. Aa-registeret i Fase 3.

### 3.5 Feil og hull i skjelettet

1. **B18 har ingen epic.** Honorar og mottakere uten arbeidsforhold finnes bare som beslutning. Ny E1.12.
2. **Permisjon og permittering ligger i modulsporet (E6.3)**, men må rapporteres i a-meldingen. Flyttes til E1.6.
3. **Feriesaldo, ferietrekk, egenmelding og AGP ligger delvis i spor 6.** Det bryter R2-regelen om at alt med rettsvirkning ligger i kjernen [R2-virksomhet §5.7 pkt. 3].
4. **E5.3 ligger i spor 5, som bygger på spor 2**, mens importen i E2.3 trenger den. Én vei inn.
5. **E3.10 ID-porten for personer** løser et problem vi ikke har. BankID via megler dekker innlogging.
6. **Port 3 krever 2.4 godkjent i TT02**, men testmiljøet åpner først 15.9.2027. Porten må deles.
7. **Port 4 krever bokføring i Visma.** Ingen pilotkunde er kjent på Visma. Generisk fil holder.
8. **Port 9 krever ISAE type 1 før drift.** Det er urealistisk i 2027 og unødvendig for kohort 1.
9. **Spor M bygger på spor 1–4.** Migreringskittet må likevel være ferdig før parallellkjøringen. M starter i Fase 1.
10. **Ingen epic for saldoer hittil i år.** Uten den finnes ingen plan B og ingen byråbølger midt i året. Ny EM.6.
11. **Ingen epic for regelår 2028.** Statsbudsjettet vedtas og trekktabellene kommer i desember (verifiseres dato). Ny E1.13.
12. **Ingen frist for feriepenger i juni 2028.** Første juni i drift bruker opptjening fra forrige system.
13. **Ingen frist for sammenstillingsoppgaven** (31.1.2029 for inntektsåret 2028).
14. **Ingen kommersiell del.** Salg, implementering, prising og kapital mangler. Nye ES.7–ES.9 og E9.7.
15. **Ingen designkapasitet**, selv om «SD Worx-motor med Tripletex-brukervennlighet» er hovedargumentet [A §6.1 pkt. 1]. Ny ES.10.
16. **Tidslinjen har «plattform-API» i Q1–Q3 2027** sammen med motor, kjøring, myndigheter og penger. Det er fem spor på ni måneder med et team som ikke er ansatt.
17. **Porten i spor 10 («første kunde over 300») ligger i 2028.** Realistisk er 2030.
18. **E7.7 og E11.3 overlapper** (onboarding og offboarding). Slås sammen.

---

## 4. MVP-listen (c)

### 4.1 Hvem MVP-en er for

**Kohort 1, maks 12 kunder og 1 500 lønnsmottakere:**
- **Pilotbyrå (1–2):** byråets egen lønn (20–150 ansatte) og 5–10 *grønne* klienter: 10–100 ansatte, fastlønn og timelønn, standard lønnsarter, OTP-innskudd, én juridisk enhet og ingen turnus [R2-byra §2.9 steg 1].
- **Direktekunder (3–5):** 30–150 ansatte, organisasjoner ned til 20. Organisasjon, forening, forbund, stiftelse eller AS. Månedslønn og timelønn, OTP-innskudd, regnskap i Tripletex eller PowerOffice Go. Honorar og styrehonorar er med.

**Holdes utenfor kohort 1:** offentlig tjenestepensjon (KLP, SPK), lønnsstiger etter tariff med ansiennitet, turnus og vakt i helse og omsorg, konsern med ansatte i flere enheter, utenlandske artister og kunder over 150 ansatte.

### 4.2 Med

| Område | Med i MVP 1.1.2028 | Epic |
|---|---|---|
| Mottakere og arbeidsforhold | Person, arbeidsforhold (fast, midlertidig, tilkalling, frilanser/honorar), stillingsperioder, underenhet, avdeling og prosjekt. Mottakerklasse som eksplisitt felt: arbeidstaker, honorar- eller vervmottaker, bare utgiftsgodtgjørelse | E2.1, E1.12 |
| Lønnsarter | Sjurs standardutvalg på 26 lønnsarter og kundens egne som konfigurasjon (nummer, a-meldingskode, flagg, debet og kredit) [S §6 pkt. 25–26]. Ingen uttrykksspråk | E1.1 |
| Beregning | Månedslønn, timelønn fra import, faste og variable tillegg som sats × antall, forklaringsspor per linje | E1.2 |
| Forskuddstrekk | Tabell og prosent via Skatteetatens trekkrutine, frikort, 50 % uten skattekort, halvt trekk og junireglene | E1.3 |
| Arbeidsgiveravgift | Sone per underenhet, satser og fribeløp (verifiseres omfang) | E1.4 |
| Feriepenger | Opptjening 10,2 og 12 %, tillegg for 60+, ferietrekk og utbetaling ved fratreden. Juniutbetaling ferdig og testet 1.5.2028 | E1.5 |
| Fravær og permisjon (kjerne) | Fravær registrert av lønn eller via import, egenmelding og sykmelding, telling av arbeidsgiverperiode, sykepengegrunnlag og refusjonskrav som rapport, permisjon og permittering i a-meldingen | E1.6 |
| Trekk | Fagforening, pensjonstrekk, samordnet utleggstrekk (manuelt registrert med KID), bidragstrekk og trekk etter avtale | E1.7, E3.6 |
| Pensjon | OTP-innskudd, pensjonsgrunnlag i a-meldingen og rapport til leverandøren. Premien føres fra fakturaen [S §6 pkt. 29] | E1.8 |
| Korreksjon | Korreksjonskjøring og enkel retro for fastlønn og faste tillegg med differanse per måned | E1.9, E2.6 |
| Kjøring | Lønnskalender, cut-off, testkjøring, avviksliste mot forrige måned med regelbasert årsak, fire øyne, uforanderlig godkjent kjøring og ekstrakjøring | E2.2, E2.4, E2.5, E2.6 |
| Grunnlag inn | Lønnsgrunnlag-API v1 og CSV/Excel-import med mapping, karantene for nye koder og idempotens | E2.3 (med E5.3) |
| Slutt | Sluttoppgjør med feriepenger og trekk etter avtale | E2.8 |
| Rapporter | Lønnsjournal, avstemming lønn mot a-melding, feriepengeliste, trekkliste, AGA-oversikt og CSV-eksport til revisor | E2.9 |
| Avdeling og prosjekt | Dimensjoner på arbeidsforhold og linje, og fordeling i prosent | E2.10 |
| Myndigheter | Maskinporten og systembruker (standard og klient), a-melding 2.3 (test og tidlig drift) og 2.4 (fra 2028-01), tilbakemelding, erstatningsmelding, skattekort-API og Brreg | E3.1–E3.5, E3.9, E3.11 |
| Penger | Ett betalingsforslag med netto lønn, forskuddstrekk med KID til første virkedag etter utbetaling, utleggstrekk med KID og AGA per termin. pain.001-fil som kunden laster opp i nettbanken [D §0 pkt. 4], [S §5] | E4.1, E4.2 |
| Regnskap | Bilag med dimensjoner og Sjurs standardkontering [S §6 pkt. 27–28]. Tripletex-API, PowerOffice Go-API og generisk fil | E4.3, E4.4 |
| Ansatte | Webportal med BankID: lønnsslipp (PDF og forklaring), kontonummer med skjold og varsel på e-post uten beløp | E7.1, E7.2, E7.3, E7.5 |
| Byrå | Klientliste med status per kjøring, klient-systembruker, samlehenting av skattekort og «send alle som er klare» med port per klient [R2-byra §0 pkt. 3] | E8.1, E8.2, E8.3 |
| Sikkerhet | Tenant og RLS, feltkryptering av fødselsnummer og kontonummer, revisjonslogg, step-up og roller (lønn, godkjenner, byrå, revisor med lesetilgang) | E0.2–E0.5 |
| Drift | Data og backup i Norge, overvåking, vakt på lønnsdager, beredskapsplan, pentest, DPA og underleverandørliste | E0.9, E9.3–E9.7 |
| Migrering | A-melding-XML som fasit, Tripletex- og PowerOffice-adapter, Excel-mal, import av saldoer hittil i år og feriepengegrunnlag, parallellkjøring med avviksrapport | EM.1–EM.3, EM.6 |

### 4.3 Ikke med, og når det kommer

| Ikke med | Kommer | Epic |
|---|---|---|
| NAV-inntektsmelding via API | Q2 2028 | E3.7 |
| Trekkpålegg-API | 2028 | E3.6 |
| pain.002, camt.054 og bankavstemming | Q2 2028 | E4.2 |
| Avstemmingsrobot lønn, regnskap og bank | Q3 2028 | E4.6 |
| Lønnsoppgjør med masseoppdatering | Før 1.5.2028 | E2.7 |
| Retro med følgevirkninger (timelønnsavhengige tillegg, korrigert inntektsmelding, pensjon) | Q3 2028 | E1.9 |
| Tariff og lønnsstiger | H2 2028 | E1.10 |
| KLP og SPK | H2 2028–2029 (verifiseres format) | E4.5 |
| Sammenstillingsoppgave | Frist 31.1.2029 | E3.8 |
| Byråmaler, kundeportal, GRFS-dokumentasjon, lisens og fakturagrunnlag | 2028 | E8.4–E8.7 |
| Lederinnboks | H2 2028 | E7.4 |
| Ferie og fravær som selvbetjening | H2 2028 | E6.1, E6.2 |
| Offentlig API med utviklerportal, webhooks, installasjoner og sandkasse | 2028 | E5.1, E5.2, E5.4, E5.10 |
| Kontrakter for Utleggsappen og OrgLab | 2028 | E5.5, E5.6 |
| Huma-kobling | Q3 2028 | E11.1 |
| SSO | 2028 | E0.3 |
| ISAE 3402 type 1 | 30.6.2028 | E9.2 |
| KI (språk på avviksforklaringer) | Q4 2028 | E0.10 |
| Timer | 2029 | E6.4 |
| Egen utleggsmodul | 2029 eller aldri (B29) | E6.6 |
| Tikket | 2029 | E5.7 |
| Direkte bank-API | 2029 | E4.8 |
| HR og erstatning av Huma | 2029–2030 | spor 11 |
| Konsern, prognoser, lønnstransparens og enterprise | 2029+ | spor 10 |
| ISO 27001 og SCIM | 2029 | E9.1, E0.3 |

### 4.4 Manuell reservevei

| Mangler i MVP | Reservevei | Hvem | Tid (anslag) |
|---|---|---|---|
| NAV-inntektsmelding | Brutto lager grunnlaget (AGP, beregningsgrunnlag og refusjon). Lønn sender i NAVs portal | Lønn eller byrå | 15 min per sykefravær |
| Trekkpålegg | Leses i Altinn og registreres manuelt med KID, med fire øyne | Lønn | 5 min per pålegg |
| Bankavstemming | Kunden laster opp pain.001 og markerer kjøringen som betalt. Avstemmingen lønn mot a-melding er automatisk | Kunde eller byrå | 10 min per kjøring |
| Ferie og fravær | Lønn registrerer fra e-post, Huma-rapport eller Excel-mal. Feriesaldo står på slippen | Lønn | 1–3 t per 100 ansatte |
| Timer | CSV fra kundens tidssystem eller Excel-mal via importen | Lønn | 30 min |
| Utlegg | Eksport fra Utleggsappen eller annet system som CSV med lønnsgrunnlag. Rene refusjoner kan betales utenom lønn | Lønn | 15 min |
| Huma | PAXml- eller CSV-eksport ved endringer og en månedlig avstemming. Kontonummer hentes aldri fra Huma [R2-okosystem §4.4.6] | Lønn og HR | 30 min |
| OrgLab-honorar | CSV med vedtaksreferanse og mottakere. Mottakeren registrerer konto selv med BankID i portalen | Organisasjonen | 30 min per honorarkjøring |
| Lønnsoppgjør | Ny lønn via import med virkningsdato. Enkel retro regner differansen | Lønn | 2–4 t |
| Lønnsstiger | Fast lønnslinje per ansatt. Opprykk via import | Lønn | – |
| Byråmaler | Eksport og import av oppsett mellom klienter | Byrå | 1 t per ny klient |
| Kundeportal | Grunnlag på e-post eller i byråets kanal. Godkjenning på e-post logges i oppdragsdokumentasjonen [R2-byra §0 pkt. 5] | Byrå | – |
| OTP-rapport | Rapport lastes opp hos pensjonsleverandøren | Lønn | 15 min |
| A-melding hvis API-et svikter | Manuell XML-opplasting i Skatteetatens portal. Overgangsløsning uten oppgitt sluttdato [B §13 rad 7] (verifiseres for 2.4) | Lønn eller byrå | Bare ved feil |
| Skattekort hvis API-et svikter | Filopplasting i portal i RF-1211-format [B §13 rad 9] | Lønn eller byrå | Bare ved feil |
| Klient-systembruker (hvis 2.5 slår inn) | Standard systembruker per klient, godkjent i Altinn | Klienten | 15 min per klient, én gang |
| SSO | BankID og passkey | – | – |

### 4.5 Hvor stor MVP-en er (anslag)

| Spor | Epics i MVP-omfang | Utviklermåneder |
|---|---|---|
| 0 | E0.1–E0.7, E0.9 | 11 |
| 1 | E1.1–E1.9, E1.11, E1.12 | 15 |
| 2 | E2.1–E2.6, E2.8–E2.10 | 10 |
| 3 | E3.1–E3.6, E3.9, E3.11 | 9 |
| 4 | E4.1–E4.4 | 4 |
| 7 | E7.1–E7.3, E7.5 | 3 |
| 8 | E8.1–E8.3 | 2,5 |
| 9 | E9.3–E9.6 | 1,5 |
| M | EM.1–EM.3, EM.6 | 5 |
| **Sum** | **55 epics, skåret ned** | **≈ 61** |

Mot 50–55 tilgjengelige utviklermåneder (2.1) mangler det 6–11. Gapet lukkes med 2–3 innleide seniorer fra desember 2026, med kjøpslisten i 2.4 og, hvis det trengs, med listen i 2.5.

---

## 5. Moduler mot integrasjoner

### 5.1 Verdi tidlig eller distraksjon

| Byggekloss | Verdi tidlig for | Kostnad (anslag) | Vurdering | Fase |
|---|---|---|---|---|
| Fraværskjerne (AGP, ferietrekk, permisjon, feriesaldo) | Alle | M | Nødvendig. Ligger i lønnskjernen | MVP |
| Lønnsgrunnlag-API v1 med CSV-import | Byrå, direkte og alle partnere | S–M | Høy verdi. Én vei inn og grunnmuren for like vilkår | MVP |
| Regnskapsadaptere (Tripletex, PowerOffice) | Alle | M | Nødvendig. Byrået velger ikke kundens regnskapssystem [R2-byra §5 nr. 10] | MVP |
| Bankfil (pain.001 med KID) | Alle | S | Nødvendig etter 2026-reglene [D §0 pkt. 4] | MVP |
| Ferie og fravær som selvbetjening | Direktekunder uten HR-system | M–L | Verdi, ikke nødvendig ved start | H2 2028 |
| Huma-kobling | Kunder med Huma (ofte 100–400 ansatte) | M | Verdi hvis kunden har Huma. Avhengig av en framtidig konkurrent | Q3 2028 |
| Utleggsappen-kontrakt | Kunder med Utleggsappen | S (generisk kontrakt) | Billig fordi den er lønnsgrunnlag-API-et | 2028 |
| OrgLab-kontrakt (verv, møtegodtgjørelse) | Organisasjoner | M | Verdi i organisasjonsnisjen, distraksjon utenfor | 2028 (CSV i MVP) |
| Offentlig API med portal, sandkasse og webhooks | Partnere | M (én utvikler i 3 mnd [R2-okosystem §8]) | Distraksjon før første kunde. Verdi når tre partnere står klare | 2028 |
| Timer | Prosjektlønn og små kunder | L | Distraksjon i 2027. Glir mot turnus [R2-virksomhet §5.7 pkt. 1] | 2029 |
| Egen utleggsmodul | Små kunder uten Utleggsappen | M–L | Distraksjon og konflikt med søsterprodukt | 2029 eller aldri |
| Tikket-kontrakt | Arrangement og ekstrahjelp | M | Nisje i nisjen, med artistskatt og sesongtopper | 2029 |
| Direkte bank-API | Store kunder | L, egen avtale med hver bank | Distraksjon før 50 kunder | 2029 |
| HR-plattform (erstatte Huma) | 100–400 ansatte med HR-sjef | XL | Nytt produkt og ny konkurransefront | 2029–2030 |

### 5.2 Rekkefølge

1. **MVP:** kjerne og lønnsgrunnlag-API, der CSV-importen er første klient.
2. **MVP:** integrasjonene pilotkundene faktisk har: regnskap, bankfil og CSV fra tid, utlegg og Huma.
3. **Q2–Q3 2028:** API-et blir offentlig (portal, webhooks, installasjoner). Utleggsappen og OrgLab kobles som de to første eksterne kildene. Huma-koblingen bygges når minst to kunder trenger den.
4. **H2 2028:** egen ferie og fravær som selvbetjening, med byttetest mot Huma som kilde.
5. **2029:** timer (registrering og prosjekt, aldri turnus), Tikket og bank-API.
6. **2029–2030:** HR-kjerne og erstatning av Huma, per kunde.

**Prinsipp (B29):** Integrasjon før modul. En egen modul bygges først når minst fem betalende kunder mangler et eksternt alternativ.

### 5.3 Like vilkår og egen utleggsmodul

R2-okosystem kaller Utleggsappen et søsterprodukt og påpeker at Brutto Utlegg konkurrerer direkte med det [R2-okosystem §1.3]. Det gir tre problemer:

1. **Troverdighet.** En plattformeier som konkurrerer med partneren sin, får partnere som holder igjen på investeringer. «Like vilkår» blir et løfte ingen tester.
2. **Verdi i gruppen.** Har produktene samme eier, kannibaliserer Brutto Utlegg inntekten til Utleggsappen med et svakere produkt. Brutto Utlegg vil mangle kortintegrasjon, utenlandsreiser og OCR-automatikk i flere år [R2-virksomhet §9].
3. **Kapasitet.** M–L i den perioden der hver måned teller.

Like vilkår krever lite: én offentlig kontrakt, egne moduler som bare bruker den, en byttetest og en nøytral katalog [R2-okosystem §7]. Det kan bevises uten egen utleggsmodul. Den åpne referanseintegrasjonen (S/M) holder som bevis [R2-okosystem §5.3 pkt. 4].

**Anbefaling:**
- Tilby «Lønn + Utleggsappen» som kommersiell samlepakke. Det er tillatt etter prinsipp 11, fordi samlepakker aldri endrer teknisk tilgang [R2-okosystem §7].
- Ingen egen utleggsmodul før 2029. Hvis den kommer, bare som en enkel variant for honorarmottakere og frivillige der Utleggsappen ikke passer. Varsle Utleggsappen seks måneder før og kjør byttetesten.
- Er Utleggsappen ikke under samme eier, må ordet «søsterprodukt» ut av dokumentene. Da er egen utleggsmodul et rent produktvalg, og det hører fortsatt hjemme i 2029.

### 5.4 Huma

- Huma har et offentlig API for brukere, stillinger og grupper. Fravær finnes bare som webhook uten dokumentert retry, og det er ingen kanal for lønnsresultat [R2-okosystem §4.4.1].
- API-et krever Standard- eller Premium-plan, og Huma kan begrense tilgangen [R2-okosystem §4.4.2].
- Et offentlig mål om å erstatte Huma inviterer Huma til å stenge API-et eller samarbeide med Visma. Hold målet internt (B30).
- **Bygg nå, fordi det er billig og trengs uansett:** kanonisk person- og arbeidsforholdsmodell, lønnshistorikk i Brutto fra dag én, importrammeverk og dokumentlager for lønnsslipper og trekkavtaler (OK-170, OK-173, OK-175, OK-181).
- **Vent med:** kilderegister med full kildebytte-prosedyre (i 2028 holder et enkelt eierflagg per datatype og skrivebeskyttet UI) og alle HR-funksjoner.
- Å erstatte Huma betyr et nytt marked med en ny kjøper. HR-sjefen eier HR-systemet, og CFO eier lønn [R2-virksomhet §2.4.1]. Det hører hjemme etter at Brutto har minst 100 lønnskunder og minst 20 % av dem har bedt om det.

---

## 6. Segment og go-to-market

### 6.1 Hva er galt med B3

«30–300 ansatte med tariff og byråer først» blander to ting.
- **30–300 er riktig gap.** De lette systemene er for enkle, og Visma Payroll oppleves som rigid [A §0 pkt. 1].
- **«Med tariff» er feil start.** Tariff betyr i praksis Virke HUK eller NHO Geneo med lønnsstiger, ansiennitet, lokale tillegg og retro. Ofte følger KLP og turnus med [D §7].

Disse kundene har mest å tape, trenger referanser og krever ISAE fra ca. 250 ansatte [R2-virksomhet §6 pkt. 10]. De er riktige i 2029.

### 6.2 Byrå eller direkte først

| | Byrå først | Direkte først |
|---|---|---|
| Kunder per salg | 5–10 klienter per beslutning | 1 |
| Hvem bruker systemet | Lønnsfolk som tåler reserveveier | Ofte én lønnsansvarlig som trenger mer hjelp |
| Enkleste lønn | Grønne klienter [R2-byra §2.9] | Varierer |
| Inntekt per kunde | Lav (per slipp) | Høyere |
| Funksjoner som trengs i tillegg | Klient-systembruker og arbeidskø | Ansattportal og etter hvert godkjenning |
| Risiko | Byråer konsoliderer. Januar er høysesong. Én feil koster byrået en klient [E §10.8] | Lang salgssyklus på 3–9 måneder [A §6.2 pkt. 6] |

**Anbefaling:** Kohort 1 ledes av byrå, med en liten direkte organisasjonsnisje ved siden av.
- Byråets egen lønn går i skarp drift i oktober 2027 (EM.7). Det er en ufarlig pilot på egne data [R2-byra §2.9 steg 2].
- Altinn 3 er hygiene innen vi lanserer [R2-byra §0 pkt. 2]. Vi selger minutter per slipp.
- **Ikke i 2028:** 10–25 ansatte direkte (de kommer via byrå), 150–300 (2029), 300–1000 (2030) og offentlig sektor (ingen plan).

### 6.3 Stiftelser og organisasjoner

Det finnes 703 stiftelser og 1 594 foreninger, lag og innretninger med 10–999 ansatte. Frivillighetsregisteret har 1 638 enheter med minst 10 ansatte [A §4.1]. Gruppen må deles i tre:

| Delsegment | Behov | Når |
|---|---|---|
| Interesseorganisasjoner, forbund, idrett og kultur | Honorar, styrehonorar, verv, lokallag, 10 000-kronersregelen [R2-ansatt-org §0 pkt. 4–5]. Ellers moderat lønn | Kohort 1 |
| Stiftelser og forskning med prosjektlønn | Prosjektfordeling, timer som dokumentasjon, retroaktiv omfordeling [D §6.4] | 2029, når timer og fordeling er modne |
| Helse og omsorg | HUK, KLP og turnus [D §7] | 2029–2030 |

OrgLab-synergien er reell bare hvis OrgLab har nok kunder med minst 10 ansatte. Det vet vi ikke [R2-virksomhet §10 spm. 3]. Det må telles før mars 2027.

### 6.4 Det skarpeste første segmentet

**Grønne klienter hos ett uavhengig designpartnerbyrå.** Hvis jeg bare får velge ett segment, er det dette.
- Kjøperen er byråets fagleder for lønn. Hun vurderer minutter per slipp og tar risikoen på tvers av en portefølje.
- Klientene følger byrået. Byrået *er* referansen, så vi trenger ingen fra før.
- Lønnen er den enkleste i markedet.
- Byråets egen lønn gir en ufarlig start i oktober 2027.

**Nummer to:** interesseorganisasjoner og forbund med 20–150 ansatte fra OrgLab-nettverket. Visma og SD Worx bryr seg ikke om en nisje på noen hundre enheter. Smerten med honorar og verv er reell, og de lette systemene håndterer den dårlig.

### 6.5 Slik vinner vi de første 10 uten referanser

1. Tell OrgLab-kunder med minst 10 ansatte, og list uavhengige byråer med 3–15 lønnsfolk som har hatt Altinn 3-problemer eller mistet et system [E §10.2].
2. Signer 2 byråer og 5–7 direktekunder for å ende med 1 byrå og 3–5 direktekunder.
3. Tilbudet:
   - gratis til 30.6.2028, deretter 24 måneders prisgaranti
   - gratis migrering
   - navngitt implementeringsansvarlig
   - parallellkjøring med avviksrapport
   - beregningsgaranti: blir lønnen feil på grunn av systemet, retter vi og betaler [A §6.2]
   - designpartnerstatus med innflytelse på veikartet [E §10.5]
4. Mål det byrået betaler for: minutter per slipp, andel kjøringer uten manuell korrigering og avvik på a-meldingen (mål: 0) [E §10.1].

---

## 7. Tidslinje og avhengigheter

### 7.1 Kalender med harde datoer

| Dato | Hendelse | Konsekvens for Brutto |
|---|---|---|
| 17.11.2026 | A-melding og skattekort er ikke lenger tilgjengelig via Altinn II-roller [E §3.2] | Byråene er opptatt fra november til februar. Designpartnerarbeidet starter i februar |
| 31.12.2026 | Alle Altinn II-roller opphører [E §3.2] | Brutto bygger på systembruker fra dag én. Det gir ingen salgsgevinst i 2028 |
| Jan. 2027 | Ny regel F532/F530 i a-meldingen [B §13 rad 4] | Med i implementasjonen av 2.3 |
| 1.2.2027 | Siste dato for to lønnsfaglige og tech lead (ny) | Ellers flyttes kohort 1 |
| 31.3.2027 | Port Fase 0: gående skjelett | |
| 1.5.2027 | Spesifikasjon for a-melding 2.4 publiseres senest [B §12] | 2.4 er på kritisk sti fra mai |
| 1.6.2027 | Delport for motoren | Første go/no-go |
| Juni 2027 | Feriepenger hos pilotkundene i gammelt system | Hent feriepengegrunnlag for 2026 og opptjening for 2027 til migreringen |
| 1.9.2027 | Port 3a: 2.3 i TT02 | Andre go/no-go |
| 15.9.2027 | Testmiljø for 2.4 er klart [B §12] | 2,5 måneder til 2.4 må være godkjent |
| 1.10.2027 | Parallellkjøring starter. Tidlig skarp drift (EM.7) | |
| Okt. 2027 | Statsbudsjettet for 2028 legges fram (verifiseres dato) | Forslagspakke `NO-2028.1-forslag` [F §1.3] |
| 1.11.2027 | Funksjonsfrys | Bare feilretting fram til 31.1.2028 |
| 1.12.2027 | Go/no-go per kunde. 2.4 godkjent i test | |
| Des. 2027 | Statsbudsjettet vedtas. Trekktabeller og skattekort for 2028 kommer (verifiseres datoer) | Regelpakken publiseres innen 5 virkedager |
| 1.1.2028 | Første produksjon for kohort 1, a-melding 2.4 | |
| 5.2.2028 | Frist for a-melding 2028-01 | Port 3b |
| 1.3.2028 | Plan B, vindu 1 (to måneder hittil i år) | |
| 1.5.2028 | Feriepengeutbetaling klar og testet med migrerte data | |
| Juni 2028 | Feriepenger | Høyeste risiko i 2028 |
| 1.8.2028 | Plan B, vindu 2 (etter feriepenger) | |
| Nov.–des. 2028 | Halvt trekk | |
| 31.1.2029 | Sammenstillingsoppgave for 2028 | E3.8 |

### 7.2 Er 1.1.2028 riktig?

- **For skjelettet:** umulig.
- **For MVP-en:** riktig mål, men stramt. Mine anslag:
  - ca. 40 % sannsynlighet for at alle kohortkundene går live 1.1.2028
  - ca. 70 % for at minst tre gjør det
  - ca. 85 % for at kohorten er i drift innen 1.3.2028
- **For tidlig?** Nei, så lenge kohorten er liten. E sitt forslag om januar 2027 er umulig [R2-byra §0 pkt. 2].
- **For sent?** Nei. Alt senere enn 2028 er dødelig for kapitalen (kap. 9.4).
- **Januar er høysesong for byråene** [E §10.3]. Alt migreringsarbeid må være gjort i oktober og november, slik at januar bare er kjøring. Byråklienter som vil vente, kan gå live 1.2 eller 1.3 med EM.6.

### 7.3 Hvis piloten glipper

| Situasjon | Konsekvens | Handling |
|---|---|---|
| 1.6.2027: gylne caser for trekk, AGA eller feriepenger under 100 % | Motoren er ikke klar | Frys alt utenfor spor 1. Vurder 1.3.2028 |
| 1.9.2027: a-melding 2.3 ikke godkjent i TT02 for tre testvirksomheter | Ingen trygg parallellkjøring | Flytt kohorten til 1.3.2028. Avlys tidlig skarp drift |
| 1.12.2027: en kunde har uforklarte avvik etter to perioder | Kunden er ikke klar | Kunden går live 1.3.2028 med to måneder hittil i år. De andre går 1.1.2028 |
| 1.12.2027: 2.4 ikke godkjent i test | 2028-01 kan ikke sendes fra system | Reserve: manuell XML-opplasting (verifiseres for 2.4), eller utsett |
| Desember 2027: trekktabeller eller satser kommer sent | Januarlønnen blir feil | Vakt 27.12–10.1, release-diff og regelpakke innen 5 virkedager |
| Pilotbyrået trekker seg | Ingen byråreferanse | Ha to byråer i løypa. Direktekundene går uansett |
| Alt glipper | Ingen kunder 2028-01 | Neste vindu er 1.8.2028 etter feriepenger. Ikke vent til 2029 |

**Kostnaden ved forsinkelse:** Hver måned uten kunder koster 1,7–1,8 MNOK i drift (anslag). Utsettelse til 1.8.2028 koster ca. 12 MNOK. Utsettelse til 1.1.2029 koster ca. 21 MNOK og et år med referanser.

---

## 8. Revidert faseplan (d)

### Fase 0: nå til 31.3.2027 – team, tilgang og gående skjelett

| Spor | Epics |
|---|---|
| S | ES.1 (to lønnsfaglige og tech lead innen 1.2), ES.2 (systemregister, scopes, TT02, Tenor), ES.3 (pilotavtaler), ES.4 (vilkår, DPA-mal), ES.6, ES.7, ES.8, ES.9 (start), ES.10. ES.5 bare med intensjonsbrev |
| 0 | E0.1, E0.2, E0.3 (BankID-megler valgt), E0.4, E0.5, E0.6, E0.7 |
| 1 | E1.1, E1.2, E1.3, E1.11 (rammeverk og de første 150 casene) |
| 3 | E3.1, E3.2 (skjelett for 2.3), E3.4 |
| 4 | E4.2 (skjelett for pain.001), E4.4 (generisk fil) |

**Port:** S og 0 i kap. 3.2. Stack låst innen 1.12.2026 (B8).

### Fase 1: 1.4.2027 til 30.9.2027 – MVP til pilot

| Spor | Epics |
|---|---|
| 1 | E1.4, E1.5 (opptjening og fratreden), E1.6 (med kjernen fra E6.1–E6.3), E1.7, E1.8, E1.9 (enkel), E1.11 (300 caser), E1.12 |
| 2 | E2.1, E2.2, E2.3 (med E5.3), E2.4, E2.5, E2.6, E2.8, E2.9, E2.10 |
| 3 | E3.2, E3.3, E3.5, E3.6 (manuell), E3.9 (fra 1.5.2027), E3.11 (Brreg) |
| 4 | E4.1, E4.2 (pain.001), E4.3, E4.4 (Tripletex, PowerOffice Go og fil) |
| 7 | E7.1 (lett), E7.2, E7.3, E7.5 |
| 8 | E8.1 (lett), E8.2, E8.3 |
| 9 | E9.3, E9.4 (pentest i august), E9.5, E9.6, E9.7 (fra 1.9) |
| M | EM.1, EM.2, EM.6, EM.3 (forberedelse og prøvemigrering per kunde) |

**Delporter:** 1.6.2027 (motor) og 1.9.2027 (3a, prøvemigrering ferdig for hver pilotkunde). **Port 30.9.2027:** spor 1, 2, 4, 7 og 9 i kap. 3.2.

### Fase 2: 1.10.2027 til 31.1.2028 – lansering 1.1.2028

| Spor | Epics |
|---|---|
| M | EM.3 (parallellkjøring oktober og november), EM.4, EM.5, EM.7 (skarp drift fra 1.10) |
| 3 | E3.9 (2.4 godkjent 1.12) |
| 1 | E1.13 (regelår 2028), E1.11 (caser for 2028) |
| 9 | E9.5, E9.6, E9.7 (vakt 27.12–15.1) |

Funksjonsfrys 1.11.2027. **Port:** M, 3b og 8 i kap. 3.2. Første a-melding 2028-01 sendt innen 5.2.2028.

### Fase 3: 2028 – bevise og bygge bredde

| Kvartal | Epics |
|---|---|
| Q1 | Stabilisering. E1.5 (juniutbetaling, frist 1.5), E2.7 (lønnsoppgjør før mai), E3.7 (NAV-inntektsmelding, sykepenger først) |
| Q2 | E4.2 (pain.002 og camt.054), E8.4, E8.5, E8.6, E8.7, E9.2 (ISAE type 1 per 30.6), E5.1, E5.2, E5.4, E5.10, E5.5 (Utleggsappen), E5.6 (OrgLab) |
| Q3 | E1.9 (retro med følgevirkninger), E1.10 (tariff), E4.5 (KLP-fil, verifiseres), E4.6, E7.4, E11.1 (Huma-kobling), E3.6 (trekkpålegg-API), E3.11 (Aa-registeret), SSO i E0.3 |
| Q4 | E6.1 og E6.2 (selvbetjening, med byttetest mot Huma som kilde), E0.10 med KI-tekst på avviksforklaringer, E3.8 (sammenstillingsoppgave til 31.1.2029), halvt trekk, salg av kohort 2 |

**Port 31.12.2028:**
- Minst 10 av 12 kohort 1-kunder fornyer etter gratisperioden.
- Feriepenger i juni og halvt trekk i desember er kjørt uten systemfeil.
- Ingen a-meldingsavvik som skyldes Brutto tre måneder på rad.
- Kohort 2 for 1.1.2029 er signert (kap. 3.2, spor 10).
- ISAE 3402 type 1 er utstedt.
- Pilotbyrået bruker høyst 8 minutter per slipp [R2-byra §4.3].

### Fase 4: 2029 og senere – skala og plattform

| År | Epics |
|---|---|
| 2029 | E6.4 (timer: registrering og prosjekt), E5.7 (Tikket), E5.8, E4.8 (bank-API), E9.1 (ISO 27001), SCIM i E0.3, E10.1, E10.2, E10.3, E10.4, kunder med 150–300 ansatte |
| 2029–2030 | Spor 11: E11.2, E11.3 (med E7.7), E11.4, E11.7. E6.6 og E6.8 bare hvis B29 utløses. E5.9 (MCP, bare lesing og utkast). E10.5. Kunder over 300 ansatte |

**Port:** ARR på minst 20 MNOK og break-even innen utgangen av 2030 i godt scenario, 2031 i basisscenario (kap. 9).

---

## 9. Pris og økonomi

### 9.1 Holder prisforslagene?

1. **«Per aktiv ansatt» må defineres.** Visma fakturerer per ansatt med startdato og uten sluttdato [A §2.2]. En organisasjon med 3 000 tillitsvalgte som får ett honorar i året, ville betalt for alle hele året. Enheten bør være *lønnsmottaker med minst én utbetaling i måneden*.
2. **Kanalarbitrasje.** Direkte ca. 60 kr per ansatt og byrå 25–45 kr per slipp gir et smutthull: en direktekunde kan kjøpe lisensen via et byrå. Regel: byråpris gjelder bare når byrået utfører lønnskjøringen.
3. **30–50 % byråmargin er et svakt argument.** 50 % av 35 kr er 17,50 kr. Byrået tar 150–250 kr per slipp [R2-byra §2.8], [E §5.2]. Byrået kjøper minutter. Gi en nettopris og en veiledende utpris, og lov ingen margin.
4. **Prisankeret er lavere enn det ser ut.** For et byrå med 10 lønnsfolk og 9 000 slipper blir Uni Micros byråpris ca. 10 kr per slipp (12 000 kr i brukerlisens og 9 kr per ansatt) (anslag fra [E §5.1]). Med lav portaladopsjon må prisen ligge nederst i spennet [R2-byra §4.3].
5. **Minstepris mangler.** En kunde med 10 ansatte gir 600 kr i måneden. Det dekker ikke onboarding og support.
6. **Onboarding.** Gratis migrering er normen for byrå [E §0 pkt. 6]. For direktekunder over 50 ansatte er en fastpris vanlig, og den luker ut dem som bare vil se.
7. **Moduler.** Er alt inkludert [A §6.2 pkt. 4], gir modulene ingen inntekt. Da skal de bare bygges når de vinner kunder.

### 9.2 Forslag til prismodell (anslag, testes i ES.8)

| Element | Forslag |
|---|---|
| Enhet | Lønnsmottaker med minst én utbetaling i måneden |
| Direkte: lønn med ansattportal, kontroll, myndigheter, regnskap og bankfil | 69 kr per mottaker per måned |
| Direkte: minstepris | 1 490 kr per måned per juridisk enhet |
| Honorar- og vervmottakere uten arbeidsforhold | 15 kr per mottaker med utbetaling |
| Moduler (fra H2 2028) | 15–25 kr per ansatt per modul, eller pakke |
| Byrå (byrået utfører kjøringen) | Netto 29 kr per slipp for 0–2 000 slipper, 25 kr for 2 000–10 000 og 22 kr over 10 000. Ingen brukerpris og ingen oppstart. Valgfritt årstak |
| Veiledende utpris i byråkanalen | 45–60 kr, så byrået kan vise påslag |
| Onboarding direkte | Gratis i kohort 1. Deretter fastpris 15 000–40 000 kr for kunder over 50 ansatte |
| Pilot | Gratis til 30.6.2028, deretter 24 måneders prisgaranti |

Til sammenligning: Visma Payroll 57–100 kr per ansatt [A §2.2], NettLønn 39 kr per slipp [E §5.1], Tripletex 65 kr per bruker for lønn og reise [E §5.1].

### 9.3 Kostnad og break-even (anslag)

**Kostnad i 2028.** Full kostnad per årsverk er satt til lønn × ca. 1,3.

| Post | Årsverk | MNOK per år |
|---|---|---|
| Utviklere | 6 | 8,4 |
| Lønnsfaglige | 2 | 2,4 |
| Produkt og design | 1,5 | 2,0 |
| Support og implementering | 2 | 1,9 |
| Salg og partner | 1 | 1,3 |
| Sikkerhet og compliance (innleid) | 0,5 | 0,7 |
| Daglig ledelse | 1 | 1,2 |
| Drift, eID og verktøy | – | 1,2 |
| Revisjon, ISAE, pentest, juridisk og forsikring | – | 1,8 |
| **Sum** | **14** | **≈ 21** |

**Break-even ved ca. 22 MNOK i årlig gjentakende inntekt (ARR):**

| Scenario | Volum som trengs | Tilsvarer |
|---|---|---|
| Bare direkte (69 kr) | 26 600 mottakere | ca. 270 kunder med 100 ansatte |
| Bare byrå (25 kr i snitt) | 73 000 slipper per måned | ca. 8 byråer med 9 000 slipper |
| Blandet | 13 000 direkte mottakere og 37 000 byråslipper | ca. 130 direktekunder og 4 byråer |

Til sammenligning regner A med 140 kunder à 300 ansatte for 30 MNOK ARR [A §4.4]. Break-even krever ca. 2,5 % av ansatte i målgruppen hvis alt går direkte. Det er gjørbart, men det tar tid når kundene bytter ved årsskiftet og salgssyklusen er 3–9 måneder.

### 9.4 Kapitalbehov (anslag)

| År | Kostnad | Inntekt | Netto |
|---|---|---|---|
| Nov.–des. 2026 | 1 | 0 | −1 |
| 2027 | 15 | 0 | −15 |
| 2028 | 21 | 1–2 (gratis til 30.6) | ca. −19,5 |
| 2029 | 24 | 4–7 | ca. −18,5 |
| 2030 | 26 | 15–20 | ca. −8,5 |
| 2031 | 27 | 24–30 | ca. 0 |
| **Sum til break-even** | | | **≈ −62** |

- **Kapitalbehov:** 60–70 MNOK med seks måneders buffer. Break-even i 2031 i basisscenario, 2030 hvis ett stort byrå eller en kjede kommer inn tidlig.
- **Én forsinkelse på seks måneder** koster ca. 10 MNOK. En halvert kohort 2 skyver break-even til 2032.
- **Finansieringsrekkefølge:** såkornrunde som dekker minst 24 måneder fra 1.1.2027 (25–30 MNOK). Neste runde hentes i Q2–Q3 2028, på kunder i drift og en vellykket feriepengemåned.
- **Den eneste spaken som endrer bildet, er byråvolum.** Et byrå med 20 000 slipper er verdt 6 MNOK ARR. Derfor må byråkanalen med i kohort 1, selv om den starter tregere.

---

## 10. Konkurrentenes svar

### 10.1 Hva de gjør når Brutto har 20 kunder (2028–2029)

| Aktør | Sannsynlig svar | Hva vi gjør |
|---|---|---|
| Visma (Payroll, Tripletex, PowerOffice) | Merker det knapt. Lokale partnere gir rabatt og gratis migrering til kunder som vurderer å gå. Tripletex og PowerOffice styrker lønn for 30–100 ansatte og gjør veien til Payroll enklere. Vekstveien «vokser ut av Tripletex» [A §6.2 pkt. 6] er Vismas egen oppsalgsvei | Unngå Tripletex-kunder Visma allerede løfter. Vinn der byrået velger, og i organisasjonsnisjen |
| SD Worx | Ignorerer kunder under 100 ansatte og henviser dem selv til partnere [A §2.1]. Gir byråpartnere bedre vilkår. Bygger SD Worx Services, og blir dermed konkurrent til byråene | Kanalbeskyttelse og løftet om at vi aldri blir BPO (B4) |
| Intect | Den farligste. Norsk versjon siden april 2025, åpent API, offentlig pris, flere selskaper og ansattapp [A §3]. Har to til tre års forsprang på norske referanser. Kan bli ECITs plattform | Unngå å konkurrere på «moderne og åpen». Konkurrer på byråflyt, kontroll med forklaring og organisasjonsnisjen |
| ECIT og NettLønn | Kan flytte NettLønn-kundene til Intect (ikke verifisert) [A §0 pkt. 4] | Et tvunget bytte er en mulighet. Ha migrering fra NettLønn klar |
| Huma | Hvis vi annonserer erstatning: begrenser API-et eller samarbeider med Visma | B21 og B30 |
| Uni Micro, Finago, 24SevenOffice | Priskonkurranse i byråsegmentet | Selg på minutter per slipp. Hold lisensprisen i nedre del av spennet |

### 10.2 Wow-funksjoner: kopieres på seks måneder eller varig

| Funksjon [G del 3] | Kopieres innen 6 mnd? | Hvorfor |
|---|---|---|
| #4 Spør lønnsslippen | Ja | Språkmodell over eksisterende data. Visma markedsfører KI allerede [A §2.2] |
| #2 Avvik forklart i klartekst, overflaten | Ja | En KI-tekst over dagens avviksrapport ser lik ut i en demo |
| #13 Kontonummer-skjold | Ja | Liten funksjon |
| #14 Systembruker-veiviser | Ja | Alle må løse Altinn 3 uansett [R2-byra §0 pkt. 2] |
| #19 Godkjenning på mobil | Ja | Visma Manager finnes [A §2.2] |
| #6 og #7 Feriepengeprognose og nettoforklarer | Ja | Små funksjoner |
| Åpen pris | Ja | En beslutning. Intect har det allerede [A §6.1 pkt. 7] |
| #1 og #3 Avviksbasert godkjenning med årsak fra beregningssporet | Nei | Motoren må lagre forklaringsspor. Gamle motorer må bygges om |
| Retro med automatisk differanse for trekk og AGA | Nei | Krever bitemporale data og uforanderlige kjøringer. Vismas største svakhet [D §8.1] |
| A-melding-aggregat med enkle korrigeringer | Nei | Arkitektur |
| Migreringsfabrikk med a-melding-XML som fasit | Delvis | Kan kopieres med folk, men tar tid |
| GRFS-dokumentasjon byrået eier i 5 år | Delvis | Lite tyder på at konkurrentene løser det [R2-byra §0 pkt. 10] |
| Mottakerklasser og honorarflyt for organisasjoner | Nei | Markedet er for lite for Visma og SD Worx |
| Nøytralitet: ingen regnskap og ingen BPO | Nei | Visma eier regnskapet. SD Worx har egen tjenesteenhet |

**Konklusjon:** Den varige fordelen er arkitektur (beregningsspor, bitemporale data og a-melding-aggregat), posisjon (nøytral og byråvennlig) og nisje. Resten er hygiene innen 6–12 måneder. Bygg det varige først, og hold det som kan kopieres billig.

---

## 11. Topp 10-risiko (e)

| # | Risiko | Sannsynlighet | Konsekvens | Tidlig signal | Tiltak |
|---|---|---|---|---|---|
| 1 | Lønnsfeil i produksjon hos en tidlig kunde (trekk, feriepenger, a-melding) blir kjent i byråmiljøet | Middels | Kritisk | Gylne caser under 100 % 1.6.2027. Uforklarte avvik i parallellkjøring. Avviste a-meldinger i TT02 | Lønnsfaglig vetorett (B28). Trekkrutinen som orakel. To perioder parallelt. Release-diff [F §7.6]. Beregningsgaranti og forsikring (B24). Kohortgrense (B25) |
| 2 | Omfanget sprenger teamet, og MVP-en er ikke klar 1.10.2027 | Høy | Kritisk | Gående skjelett ikke ferdig 31.3.2027. Under 60 % av MVP-listen ferdig 1.6.2027. Arbeid på Fase 3-epics før port 1 | Omfangsregel (B22). Listen i 2.5. Grense for arbeid i gang. Ukentlig framdrift mot MVP-listen |
| 3 | For lite lønnsfaglig kompetanse, eller en nøkkelperson slutter | Middels–høy | Kritisk | To lønnsfaglige ikke signert 31.1.2027. Utviklere lager de gylne casene | Rekrutter fra byråer, NettLønn og SD Worx-partnere. Opsjoner. Kjøp 150–250 timer ekstern fasit. All fagkunnskap ned i caser |
| 4 | Kapitalen tar slutt før kohort 1 har bevist produktet | Middels | Kritisk | Under 12 måneders runway ved pilotstart. Mer enn to måneders forsinkelse | B23. Milepælsfinansiering. Lave faste kostnader til 1.1.2028 |
| 5 | Pilotbyråer og direktekunder forplikter seg ikke, eller trekker seg i Q3 2027 | Middels | Høy | Ingen signert pilotavtale 31.3.2027. Byrået setter av under 4 timer i uka. Kunden vil ikke dele a-melding-XML | Dobbel løype (2 byråer og 5–7 direktekunder). Gratis til 30.6.2028, prisgaranti og navngitt implementeringsansvarlig |
| 6 | Myndighetsavhengigheter: 2.4 forsinkes eller endres, scopes og systemregistrering tar tid, TT02 er ustabilt, trekktabellene kommer sent | Middels | Høy | Scopes ikke innvilget 1.3.2027. 2.4 ikke publisert 1.5.2027. Nedetid i TT02 | ES.2 nå. Versjonsuavhengig aggregat (B11). Manuell XML-opplasting som reserve. Vakt i romjulen. Plan B-datoer |
| 7 | Migreringsdata er ufullstendige (hittil i år, feriepengegrunnlag, arbeidsforhold-ID) og gir feil i juni 2028 | Middels–høy | Høy | Prøvemigrering gir avvik på over 2 % av linjene. Kunden mangler a-melding-XML for 2027 | A-melding-XML som fasit [F §6.2]. EM.6. Feriepengetest med migrerte data innen 1.5.2028 |
| 8 | Fokusdrift: nye gründerkrav (moduler, Huma, plattform, KI) tar kapasitet fra kjernen | Høy | Høy | Nye epics uten at noe tas ut. Over 15 % av kapasiteten utenfor MVP før 1.10.2027 | B22 og B29. Kvartalsvis kuttgjennomgang med styret |
| 9 | Konkurrentene svarer: Visma bunter og øker provisjonen, Intect tar posisjonen «moderne og åpen», ECIT flytter NettLønn til Intect | Middels | Middels–høy | Norske byråer får Intect-referanser. Visma-kampanjer mot byråer. Pilotbyrået får motbud | Nisje, nøytralitet, kanalbeskyttelse og exit-pakke [R2-byra §0 pkt. 8]. Forsprang på beregningsspor og retro |
| 10 | Sikkerhetshendelse eller lønnssvindel via endret kontonummer, eller manglende sikkerhetsdokumentasjon stopper salg | Lav–middels | Kritisk | Høye eller kritiske pentestfunn. Kunder ber om ISAE type 2 før kontrakt | Kontonummer-skjold, feltkryptering, step-up, data i Norge og ISAE type 1 innen 30.6.2028 |

**Rett under topp 10:**
- Huma begrenser API-et (middels sannsynlighet, middels konsekvens).
- Lav portaladopsjon hos byråkundene svekker byrå-caset [R2-byra §4.3].
- Konflikt med Utleggsappen hvis egen utleggsmodul bygges (kap. 5.3).
- Tolkningen av KI-forordningen for avviksdeteksjon [F ADR-14].

---

## 12. Beslutninger (f)

### 12.1 B1–B21

| Id | Beslutning i v0 | Anbefaling | Hvordan og hvorfor |
|---|---|---|---|
| B1 | Frittstående lønnssystem | **Behold** | Nøytralitet er den eneste posisjonen Visma ikke kan ta. Visma eier Tripletex, PowerOffice og Payroll [A §0 pkt. 2] |
| B2 | Like vilkår, samme offentlige API | **Endre** | Behold prinsippet, fas inn mekanismene. 2027: kontrakt-først lønnsgrunnlag-API der CSV-importen er første klient. 2028: utviklerportal, installasjoner, webhooks, sandkasse og byttetest. Lik tilgang gjelder vilkår og kontrakt. Kundene styrer rekkefølgen [R2-okosystem §1.1] |
| B3 | 30–300 med tariff og byråer først | **Endre** | Kohort 1: 1–2 designpartnerbyråer (egen lønn og grønne klienter med 10–100 ansatte) og 3–5 organisasjoner med 20–150 ansatte uten turnus, offentlig tjenestepensjon og lønnsstiger. Tariff og KLP fra H2 2028. 150–300 fra 2029. 300–1000 fra 2030 |
| B4 | Programvare, ikke tjeneste | **Behold** | Legg til beregningsgaranti med tak og ansvarsforsikring (B24). Juridisk nødvendig og et salgsargument mot SD Worx Services [R2-byra §2.7] |
| B5 | Ren funksjon, lovregler som kode, satser som data, uttrykksspråk for kundens lønnsarter | **Endre** | Behold ren funksjon, kode og data. Utsett uttrykksspråket til tariff (E1.10). Lønnsarter i MVP følger Sjurs modell: nummer, a-meldingskode, flagg, debet, kredit, sats × antall [S §6 pkt. 26] |
| B6 | Bitemporale data, uforanderlige kjøringer, a-melding som eget aggregat | **Endre (avgrens)** | Uforanderlige kjøringer og aggregat er ikke til forhandling. Bitemporalitet bare for det som påvirker beregning: arbeidsforhold, stillingsperioder, avtalt lønn, faste linjer, organisasjonstilhørighet og skattekort. Tidsreise som UI tidligst 2029 |
| B7 | Kunden eier dataene. Delt DB, RLS og celler | **Endre** | Delt DB og RLS fra dag én. Én celle til første kunde over 300 ansatte eller 50 000 slipper. Bygg rutingen, vent med cellene |
| B8 | Modulær monolitt, Kotlin/JVM eller .NET, Postgres | **Endre (lås)** | Lås Kotlin/JVM innen 1.12.2026. Skatteetatens trekkrutine er Java og kan brukes direkte [C §0 pkt. 5]. NAVs sykepengelogikk er Kotlin. Hver måned uten valg forsinker ansettelser |
| B9 | Data i Norge, DR i EU | **Endre** | Både primærdata og backup i Norge. Backup i Sverige utløser meldeplikt for hver bokføringspliktig kunde etter bokføringsforskriften § 7-5 [S §1 pkt. 4]. Å slippe den er et salgsargument. Verifiser to norske lokasjoner, for eksempel Azure Norway East og Norway West eller en norsk leverandør for backup (verifiseres) |
| B10 | Maskinporten og systembruker, klientsystem for byrå, trekkrutinen som fasit | **Behold** | Søk scopes og systemregistrering nå (ES.2). Standard systembruker per klient er reservevei for byrå. ID-porten for personer trengs ikke |
| B11 | A-melding-aggregat versjonsuavhengig, 2.4 fra 2028 | **Behold** | 2.3 bygges først for TT02 og tidlig drift. 2.4 er kritisk sti fra 1.5.2027. Korrigering av 2027-perioder etter overgangen må avklares med Skatteetaten [B §14 pkt. 11], [R2-byra §8 spm. 9] |
| B12 | Brutto flytter aldri penger | **Behold** | Utvid: pain.001 i MVP, direkte bank-API tidligst 2029 |
| B13 | KI forbereder, forklarer og flagger, EU-region | **Endre** | Behold policyen. Ingen KI i produksjon før Q4 2028 og ingen lønnsdata til språkmodell i første versjon [S §3 pkt. 11]. Forklaringer i MVP er deterministiske og kommer fra beregningssporet |
| B14 | BankID, passkeys, SSO/SCIM, kontonummer-skjold | **Endre** | MVP: BankID via megler for ansatte, BankID eller passkey med step-up for administratorer, og kontonummer-skjold. SSO (Entra ID) i 2028. SCIM i 2029 |
| B15 | ISAE 3402 type 1 ved første kunde, så type 2, ISO 27001 innen 24 mnd | **Endre** | Kohort 1 krever ikke ISAE [R2-virksomhet §6 pkt. 10]. 2027: ISMS light, pentest og DPA. ISAE type 1 per 30.6.2028, type 2-periode fra 1.7.2028, ISO 27001 i 2029 |
| B16 | Migrering med a-melding-XML som fasit, lik på øret, årsskifte | **Endre** | Behold fasit og «lik på øret». Bygg import av saldoer hittil i år fra start (EM.6), så 1.3 og 1.8 kan være plan B. To perioder parallelt for direktekunder, én for grønne byråklienter med byråets signatur |
| B17 | Pris per aktiv ansatt direkte, per slipp for byrå, byråmargin 30–50 % | **Endre** | Se 9.2: én enhet (mottaker med utbetaling i måneden), direkte 69 kr, honorarmottakere 15 kr, minstepris per enhet, byrå netto 22–29 kr per slipp med trinn og ingen lovet margin |
| B18 | Mottakere uten arbeidsforhold som egen mottakertype | **Behold** | Gi den en epic (E1.12) og ta den inn i MVP. Mottakerklassen er et eksplisitt felt per utbetaling [R2-ansatt-org §0 pkt. 1] |
| B19 | Første produksjon 1.1.2028 | **Endre** | Første betalende kohort (maks 12 kunder) 1.1.2028 med 2.4 fra dag én. 1–2 lavrisikokunder i skarp drift fra 1.10.2027. Plan B 1.3.2028 og 1.8.2028. Go/no-go per kunde 1.12.2027 |
| B20 | Egne moduler for ferie/fravær, timer og utlegg | **Endre** | Fraværskjernen i spor 1 (MVP). Ferie og fravær som selvbetjening i H2 2028. Timer i 2029. Egen utleggsmodul tidligst 2029, og bare hvis Utleggsappen ikke dekker behovet. Utleggsappen tilbys som samlepakke |
| B21 | Integrer Huma først, erstatt over tid | **Endre** | Huma-kobling i Q3 2028, tidligere bare hvis en kohort 1-kunde krever det. Erstatning tidligst 2029–2030 og per kunde. Kommuniser ikke målet eksternt. Behold datamodellkravene fra dag én (OK-170, OK-173, OK-175, OK-181) |

### 12.2 Nye beslutninger

| Id | Beslutning | Hvorfor |
|---|---|---|
| B22 | **Omfangsregel.** MVP-listen fryses 1.2.2027. Nye krav før 1.1.2028 tas bare inn hvis noe av samme størrelse tas ut. Gründeren eier listen og signerer endringer | Skjelettet fikk tre nye krav på én dag (28.10.2026) |
| B23 | **Kapital.** Finansier minst 24 måneder fra 1.1.2027 før pilot. Neste runde hentes på kunder i drift i 2028 | Kap. 9.4 |
| B24 | **Beregningsgaranti.** Vi retter og betaler for feil systemet har laget, med tak (for eksempel 12 måneders lisens) og ansvarsforsikring | [A §6.2], [E §10.8] |
| B25 | **Kohortgrense.** Maks 12 kunder og 1 500 lønnsmottakere i kohort 1. Ingen nye oppstarter før 1.3.2028 | Support i lønnsuka er knapp |
| B26 | **Go/no-go-datoer.** 31.3.2027, 1.6.2027, 1.9.2027, 1.12.2027 og 5.2.2028, med kriteriene i kap. 3.2 | Porter uten datoer styrer ingenting |
| B27 | **Kjøp alt rundt motoren:** eID, e-signering, IdP, PDF, varsling, overvåking, pentest og ISAE | Kap. 2.4 |
| B28 | **Lønnsfaglig vetorett.** En navngitt lønnsfaglig ansvarlig godkjenner hver release som endrer beregning eller rapportering | Release-diff [F §7.6] |
| B29 | **Integrasjon før modul.** En egen modul bygges først når minst fem betalende kunder mangler et eksternt alternativ | Kapasitet og like vilkår |
| B30 | **Ekstern posisjonering.** Brutto er nøytral lønn for byråer og organisasjoner. Vi posisjonerer oss aldri mot Huma eller Utleggsappen | Vi er avhengige av API-ene deres |

---

## 13. Spørsmål gründeren må svare på (g)

1. **Kapital:** Hvor mye kapital er sikret, og hvor mange måneders runway gir det fra 1.1.2027? Er du forberedt på 60–70 MNOK før break-even i 2030–2031?
2. **Eierskap:** Hvem eier Utleggsappen, OrgLab og Tikket, og hva er de lovet om tilgang og rekkefølge? Har de samme eier som Brutto: hvorfor skal Brutto bygge en utleggsmodul som konkurrerer med Utleggsappen?
3. **Lønnsfag:** Hvem er de to lønnsfaglige, og kan begge starte før 1.2.2027? Hvor mange timer i uka vil du selv være lønnsfaglig fasit?
4. **Piloter:** Hvilke byråer og direktekunder kan du navngi i dag? Har du selv, eller en nær partner, en lønnsavdeling som kan være pilotbyrå nr. 1 med egen lønn fra oktober 2027?
5. **Når noe må gi seg:** Ranger dato (1.1.2028), omfang og kvalitet. Min anbefaling er kvalitet først, deretter dato, så omfang.
6. **Segment:** Hvor mange OrgLab-kunder har minst 10 ansatte, og hvilket lønnssystem bruker de i dag? Godtar du at tariff og KLP venter til H2 2028?
7. **Huma:** Hvorfor Huma spesifikt? Har du kunder, eierinteresser eller avtale der? Godtar du at målet om å erstatte Huma ikke kommuniseres eksternt før 2029?
8. **Moduler:** Godtar du at timer og egen utleggsmodul venter til 2029, og at utlegg løses med Utleggsappen som samlepakke i mellomtiden?
9. **Ansvar:** Hvilken beregningsgaranti er du villig til å gi (tak og forsikring), og hvem får vetorett på releaser som endrer beregning?
10. **Team og teknologi:** Hvem er tech lead? Skal kodeagenter skrive hovedtyngden av koden, og hvordan skal vi kvalitetssikre det de lager i lønnskjernen?
11. **Pris:** Skal byrået betale grossistpris per slipp som standard? Skal moduler prises per ansatt også når byrået kjører lønnen?
12. **Data i Norge:** Godtar du at også backup skal ligge i Norge (B9), selv om det begrenser valget av skyleverandør?

---

## Kilder brukt fra runde 1 og 2

- A-marked-konkurrenter.md §0, §2.1–2.2, §3, §4.1, §4.4, §6, §7.2
- B-myndigheter.md §0 og kanal- og datotabeller (a-melding 2.4, reservekanaler, trekkpålegg, NAV)
- C-beregning.md §0 pkt. 5 (trekkrutinen)
- D-praksis.md §0, §6.4, §7, §8
- E-byra.md §0, §3.2, §5, §10
- F-arkitektur.md §0, §1.3, §6.2, §7, §9.7, §10
- G-moduler-2026.md §0, del 3, §4, §5
- R2-virksomhet.md §0, §2.4.1, §5.7, §6, §7, §9, §10
- R2-byra.md §0, §2.7–2.9, §4.2–4.3, §5, §7, §8
- R2-ansatt-org.md §0, §9, §10
- R2-okosystem.md §0, §1.1–1.3, §2.2, §4.4, §5, §6, §7, §8
- S-avklaringer-fra-sally.md §1, §3, §5, §6
