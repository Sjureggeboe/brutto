# R5: Kvalitetskontroll av kartleggingen

Dato: 2026-10-28. Gjelder `build/data/omr-K1.json` til `omr-K7.json`. Grunnlaget er gründerens føringer fra 28.10.2026 om lønn først og en smal fase 1 for lønnskontroll.

## Sammendrag

| | Før | Etter |
|---|---|---|
| Funksjoner | 668 | 674 (6 nye) |
| Entiteter i K-filene | 193 (3 doble) | 190 (ingen doble) |
| Felt etter fletting | 3 858 | 3 839 |
| Spørsmål i K-filene | 115 | 105 (10 slått inn) |
| Funksjoner merket «Fase 1» | – | 60 |
| Funksjoner merket «Fase 1 design» | – | 25 |
| Entiteter merket «Fase 1» | – | 32 |
| Entiteter merket «Fase 1 design» | – | 16 |

- `build.py` gir nå: `24 områder, 674 funksjoner, 190 entiteter, 3839 felt, 140 spørsmål`, uten merknader om doble eller ukjente entiteter. De 140 spørsmålene er 105 fra K-filene og 35 fra `design.json`.
- Alle sju filene er gyldig JSON og skrevet med samme format som før (innrykk 1).
- Endringene er gjort med `scratchpad/r5/apply.py`. Originalene ligger i `scratchpad/r5/backup/`, og tallene i `scratchpad/r5/stats.json`.

## 1. Doble entiteter

| Entitet | Eier nå | Fjernet fra | Felt lagt til hos eier |
|---|---|---|---|
| D-Tariffavtale | K2 (LON) | K1 (ORG) | avtaletype, gjelder_for, normalarbeidstid_uke, pensjonsordning, lonnsansiennitet_i_amelding, lonnstrinn_i_bruk, siste_virkningsdato_oppgjor |
| D-Pensjonspremie | K2 (PEN) | K4 (REG) | juridisk_enhet, leverandoer_orgnr, amelding_ref, aga_bilag_ref (K4 sin bilag_ref, som gjelder bilaget for AGA av premie), status |
| D-Frist | K4 (MYN) | K5 (BYR) | kildetype (K5 sin kilde). Typelisten er utvidet med fristtypene fra BYR og ORL, og merknaden på referanse nevner objektene BYR og ORL bruker. |

- Feltene ble slått sammen etter innhold, ikke bare navn. Byggrapporten talte +18, +12 og +8 felt fordi like felt hadde ulike navn (for eksempel `id` og `tariffavtale_id`, `faktura_ref` og `fakturanummer`, `forfall` og `forfallsdato`). Slike par er ikke lagt inn to ganger.
- Tomme merknader hos eieren er fylt fra den andre versjonen der den hadde innhold (`parter`, `ansatt_andel`).
- Hver beskrivelse har fått én setning om sammenslåingen.
- Funksjonene viser fortsatt til de samme id-ene.
- Spørsmålet «Eierskap til D-Tariffavtale og AGA-beregningen» (K2) har fått en statuslinje. Eierskapet til AGA-beregningen er fortsatt åpent.

Begrunnelse for valg av eier: Tariffavtalen bærer lønnsstiger, ferieregler og overtidssatser, og K2-versjonen var mest komplett. Pensjonspremien hører faglig til PEN (F-PEN-05). Fristen er felles og bør ligge der myndighetsfristene ligger (F-MYN-19).

## 2. Overlappende entiteter med ulik id

32 entiteter har fått en kort «Se også»-setning i `beskrivelse_md`. Ingen er slått sammen.

### Anbefalte sammenslåinger

| # | Entiteter | Anbefaling | Når |
|---|---|---|---|
| 1 | D-Avvik (K2) og D-Kontrollsak (K4). Beslektet: D-Tilbakemeldingsavvik, D-Migreringsavvik, D-Oppgave | **Slå sammen** til én sakskø med felles felt for kilde, periode, opplysningspliktig, person, forventet og faktisk verdi, status (åpen, forklart, løst), eier, frist, lukkevilkår og kommentar. Tilbakemeldings- og migreringsavvik beholdes som kildeposter som peker til saken. D-Oppgave er bare visningen i innboksen. | Før fase 1. Både kontrollene på A07 og kontrollkøen bruker dette. |
| 2 | D-Godkjenning (K3), D-Kjoringsgodkjenning (K2) og D-Kundegodkjenning (K5). Beslektet: D-Godkjenningsregel, D-Delegering, D-Arbeidsflyt | **Slå sammen** de tre godkjenningene til én D-Godkjenning med objekttype, objektversjon (hash), ledd, rekkefølge, beslutning og metode. D-Godkjenningsregel blir flytmalen per kunde, med maler for «bare regnskapsfører», «leder pluss lønn» og «flere ledd». D-Arbeidsflyt beholdes for HR-prosesser, men bruker samme motor. | I fase 1-designet av godkjenningsmotoren. |
| 3 | D-Kodemapping (K3), D-Mappingregel (K6) og D-Lonnsartmapping (K2) | **Slå sammen** til D-Mappingregel (PLA) med `domene` for lønnsart, fravær, timetype, utleggskategori og kodelister. Feltene er nesten like: kilde, kildekode, mål, versjon, testberegning, godkjenning og gyldighet. D-Kontomapping beholdes for seg. | Før fase 2. |
| 4 | D-Refusjonsavstemming (K3) og D-NavRapportlinje (K4) | **Slå sammen.** Begge modellerer én linje i K27. Behold D-NavRapportlinje og legg matchingen mot D-Refusjonskrav der. | Før fase 2. |
| 5 | D-Lonnsinnstillinger (K2) og D-Regnskapsoppsett (K4) | AGA-metode for NAV-refusjon står i begge. **Behold feltet ett sted** (D-Lonnsinnstillinger) og la regnskapsoppsettet lese det. | Før fase 2. |
| 6 | D-Organisasjonsprofil (K5) og D-Virksomhet (K1) | Skattefri organisasjon og AGA-fritak står i begge. **Flytt feltene til D-Virksomhet**, og behold D-Organisasjonsprofil for 10 000-regelen og forholdet mellom sentralledd og lokallag. | Før fase 2. |
| 7 | D-Sjekkliste (K1) og D-Arbeidsflytmal (K7) | **Slå sammen** senere. En sjekkliste er en arbeidsflytmal med manuelle trinn. | HR-utvidelsen. |
| 8 | D-Rolledefinisjon (K6) og D-Rolletildeling (K5) | **Ikke slå sammen.** Definisjon og tildeling er to ting. Samle eierskapet i SIK, fordi fase 1 trenger begge. | Før fase 1. |
| 9 | D-Kontoendring (K4) og D-Personbankkonto (K1) | **Ikke slå sammen.** Endringen er forespørselen, kontoen er versjonen. Fjern dobbel lagring av verifisering (`verifiseringsmetode`, `verifisert_av` og `verifisert_tid` finnes i begge). La kontoversjonen peke til endringen. | Fase 1-designet. |
| 10 | D-Akkumulator (K2) og D-Feriesaldo (K3) | **Ikke slå sammen.** Den ene er beløp, den andre dager og timer. Avklar grensen for feriepenger og ferietrekk. | – |
| 11 | D-Sats (K2) og D-Godtgjorelsessats (K3) | Vurder å legge statens satser i D-Sats og bare kundens policy i D-Godtgjorelsessats. | Ikke nå. |
| 12 | D-Beregningsspor (K2) og D-Lonnsslippforklaring (K5) | **Ikke slå sammen.** Forklaringen bygges fra sporet. | – |
| 13 | D-Abonnement (K6), D-Myndighetsabonnement (K4) og D-Webhookabonnement (K6) | Navnene kolliderer, men betydningen er ulik. **Gi tenanten en egen entitet** (for eksempel D-Kunde) eller døp om D-Abonnement til D-Kundeavtale. Fase 1-grunnmuren «kunder (tenant)» har i dag ingen egen entitet. D-Abonnement er 1:1 mot tenant og brukes som erstatning. | Før fase 1. |

## 3. Overlappende funksjoner på tvers av områder

181 funksjoner har fått «Se også F-…» i `merknad_md`, med til sammen 458 lenker i 63 grupper. Lenken er bare lagt til når funksjonen ikke allerede nevner den andre i beskrivelse, regler eller merknad. Ingenting er slettet.

Gruppene:

- **Godkjenning:** modell og innboks (F-FRA-42, F-LED-01, F-KOM-03), godkjenning av kjøring og betaling (F-KJO-23, F-MYN-11, F-BYR-24, F-BYR-26, F-BYR-27, F-BET-06), regler og stedfortreder (F-FRA-43, F-LED-07, F-LED-11, F-ORG-12, F-BYR-04), arbeidsdeling (F-LED-04, F-SIK-12, F-BET-19), step-up (F-LED-05, F-SIK-03), attestasjonsbilde (F-KJO-22, F-RAP-16) og feriegodkjenning (F-FRA-10, F-POR-19, F-LED-16).
- **Kontonummer-skjold:** F-PER-07, F-BET-18, F-POR-25, F-BET-19.
- **Avstemming:** mot a-ordningen (F-MYN-21, F-REG-25, F-REG-30, F-BYR-15, F-MIG-17, F-MYN-42), mot hovedbok og pakke (F-REG-24, F-REG-27, F-REG-30, F-RAP-15, F-REG-16), K27 (F-FRA-25, F-MYN-35, F-REG-15) og OTP-premie (F-PEN-05, F-PEN-06, F-PEN-08, F-REG-14).
- **Huma:** F-PER-33, F-PLA-22, F-MIG-12, F-MIG-34, F-HR-08, F-FRA-04.
- **Varsler:** F-KOM-01, F-KOM-02, F-POR-27, F-BYR-17, F-LED-08, F-PLA-30.
- **Andre tydelige dubletter:** systembruker for byrå (MYN-04/05 og BYR-07/08/09), «send alle som er klare» (MYN-13 og BYR-16), Brreg (ORG-01, ORG-07, MYN-39), innlogging (POR-01, SIK-01, PLA-29), kontrollpakke (KJO-20, RAP-14, RAP-21, MYN-38, MYN-42), lønnsjournal (KJO-45, RAP-09, REG-06), dimensjonsarv, kontoplansynk, omfordeling, dødsfall, ferietrekk (KJO-39 og FRA-14), sluttoppgjør, skattekort, trekkpålegg, inntektsmelding, sykmelding, pensjon i a-meldingen, sammenstillingsoppgave, ARP, likviditet, bruksmåling, arbeidsforhold-ID, lønnsslipp, regnskapsadaptere, bank, pensjonsleverandør, tid, utlegg, kildebytte, teamkalender, sykefraværsstatistikk, lederkostnad, prosjektlønn, oppgjørssimulering, exit, sandkasse, revisor, organisasjonskart, helsetilgang, agent og KI, personmatching, eierskap per kilde, beredskap og kostnad per arrangement.

Tre par har nesten samme navn og bør vurderes slått sammen i neste runde: F-KJO-22 og F-RAP-16 (Attestasjonsbilde), F-KJO-39 og F-FRA-14 (Ferietrekk), F-MYN-13 og F-BYR-16 («Send alle som er klare»).

## 4. Normalisering

**0 verdier endret.** Alle verdiene var allerede gyldige:

- `niva`: 518 Kjerne, 90 Integrasjon, 60 Modul (før nye funksjoner).
- `behovsvekt`: 472 Må, 158 Bør, 38 Kan.
- `sensitivitet` og `historikk` på 3 875 felt: bare tillatte verdier.
- `sporsmal.status`: alle 115 var «Åpen». Ingen sto som noe annet som måtte gjøres om til «Stopper».
- `sporsmal.omrade`: alle 115 hadde en gyldig områdekode.
- Filene er i Unicode NFC, så «Må» og «Åpen» er skrevet med samme tegn overalt.

Skriptet sjekker verdiene mot en tabell over synonymer og stopper hvis noe er ukjent. Det fant ingenting.

**Merk:** De 35 spørsmålene i `design.json` bruker kategorier som område («Gründer», «Lønnsfag», «Marked», «Myndigheter», «Juridisk», «Partnere», «Teknisk»). Filen er ikke en del av oppdraget og lages av `build/gen/p6_sporsmal.py`. Se tvilstilfelle 14.

## 5. Fase 1-merking

Feltet `fase1` står etter `behovsvekt` på funksjoner og etter `omrade` på entiteter. Det står bare der det er merket. Malen viser allerede `fase1` som merke og filter på funksjoner, men ikke på entiteter.

### Prinsipper

- **«Fase 1»** betyr at fase 1 bygger kjernen i funksjonen, også når den bare leser data. Eksempel: F-MYN-21 er med fordi henting av A07 bygges nå, selv om sammenligningen med egen lønn kommer senere.
- **«Fase 1 design»** er brukt på godkjenningsmotoren, utbetaling via open banking med kontonummer-skjold, assistenten og datamodellen for stillingsperioder med gyldighet (fase 1 lagrer registreringstid, og «gjelder fra» kommer senere).
- Ikke merket: alt som beregner lønn, sender a-melding, henter skattekort eller trekkpålegg, bokfører bilag, eller hører til HR, UTV, HEL og KOM.
- Funksjoner som er skrevet for Bruttos egen lønn, men som fase 1 bygger på A07-data, er merket «Fase 1» (for eksempel F-RAP-14, F-RAP-21 og F-RAP-22). Der funksjonen bare gjelder egen lønn, er det laget en ny funksjon i stedet (F-REG-30 ved siden av F-REG-24 og F-REG-25).

### Funksjoner merket «Fase 1» (60)

- **ORG** (4): F-ORG-01 Opprett virksomhet fra Enhetsregisteret, F-ORG-02 Underenheter, F-ORG-07 Løpende synk mot Enhetsregisteret, F-ORG-29 Oppstartsveiviser for virksomheten
- **PER** (3): F-PER-02 Fødselsnummer og D-nummer, F-PER-11 Avansert søk og utvalg i personalregisteret, F-PER-35 Ansattoversikt fra a-ordningen og regnskapssystemet
- **MYN** (12): F-MYN-01 Leverandøroppsett: Maskinporten-klient, nøkler og systemregister, F-MYN-02 Veiviser for systembruker hos direktekunde, F-MYN-04 Systembruker for klientsystem (byrå), F-MYN-05 Klienttilknytning og tilgangsdiagnose per klient, F-MYN-06 Tilgangshelse, utløp og tilbaketrekking, F-MYN-21 Avstemmingsrapport (A07) mot lønn, F-MYN-22 Kontrollkø for myndighetsfeil, F-MYN-23 Myndighetsgateway og revisjonsspor, F-MYN-24 Overvåking av endringer hos myndighetene, F-MYN-38 Datakvalitet for SSB og NAV via a-meldingen, F-MYN-39 Brreg-oppslag og nattlig synk, F-MYN-42 Kontroller på avstemmingsrapporten (A07)
- **REG** (6): F-REG-01 Synk av kontoplan og dimensjoner fra regnskapssystemet, F-REG-02 Standardkontering fra gründerens mal, F-REG-03 Grupperingskoder på konto, F-REG-27 Månedlig avstemmingspakke og AGA-sperre, F-REG-29 Lesing fra regnskapssystemet: saldo, posteringer og ansatte, F-REG-30 Avstemming av A07 mot hovedbok
- **BYR** (8): F-BYR-01 Byråhierarki, F-BYR-02 Opprett klient med oppdragsomfang, F-BYR-03 Byråroller og tilgang per oppdrag, F-BYR-07 Agent-systembruker per byrå, F-BYR-08 Tilknytning og tilgangsdiagnose per klient, F-BYR-09 Klientdelegering i skala og masseretilknytning, F-BYR-11 Fullmaktsregister, F-BYR-15 Samlehenting av tilbakemeldinger, avstemming og trekkpålegg
- **RAP** (8): F-RAP-01 Felles rapportmotor med tilgangsstyrt datagrunnlag, F-RAP-04 Eksport til Excel, CSV og PDF/A, F-RAP-07 Rollebaserte dashbord med nøkkeltall, F-RAP-13 AGA-oversikt per underenhet, sone og sats, F-RAP-14 Kontrollrapporter mot forrige måned, F-RAP-15 Avstemmingsrapporter, F-RAP-21 Cut-off-test og lønn etter sluttdato, F-RAP-22 Headcount, FTE og turnover
- **PLA** (2): F-PLA-17 Personmatching og koblingskø, F-PLA-34 Abonnement, moduler og funksjonsbrytere
- **SIK** (17): F-SIK-01 Innlogging med BankID, passkeys og SSO, F-SIK-03 Step-up for kritiske handlinger, F-SIK-05 Rollekatalog med standardroller, F-SIK-06 Relasjoner og omfang (ReBAC), også for byrå, F-SIK-08 Lønnstilgang og særlige kategorier, F-SIK-09 Revisortilgang, F-SIK-10 Leverandørsupport med break-glass, F-SIK-11 Tenant-isolasjon, F-SIK-15 Revisjonslogg, F-SIK-16 Tilgangslogg, F-SIK-19 Feltkryptering, blind indeks og maskering, F-SIK-20 Nøkkelhåndtering og kryptografisk makulering, F-SIK-25 Sikkerhetskopi og gjenoppretting, F-SIK-27 Databehandleravtale og underleverandører, F-SIK-28 DPIA-mal og vurdering av særlige kategorier, F-SIK-33 Hendelseshåndtering, F-SIK-36 Testdata uten produksjonsdata

### Funksjoner merket «Fase 1 design» (25)

- **ORG** (2): F-ORG-12 Lederlinje, stedfortreder og delegering av personalansvar, F-ORG-25 Virksomhetens bankkontoer
- **PER** (2): F-PER-07 Personlig bankkonto med kontonummerskjold, F-PER-22 Stillingsperiode med bitemporal historikk
- **KJO** (1): F-KJO-23 Godkjenning med fire øyne og flere ledd
- **FRA** (2): F-FRA-42 Én godkjenningsmodell for egne og eksterne kilder, F-FRA-43 Godkjenningsregler, stedfortreder og frister
- **BET** (9): F-BET-01 Betalingsforslag per lønnskjøring, F-BET-06 Godkjenning av betalinger og harde sperrer, F-BET-08 pain.001-fil, F-BET-10 Bankkanal via multibank eller regnskapssystemets bankmodul, F-BET-13 Utbetalingsstatus per betaling, F-BET-18 Kontonummer-skjold, F-BET-19 Første betaling til ny konto, F-BET-21 Lønnskonfidensialitet i betalingsdata, F-BET-22 Utbetaling via open banking-leverandør
- **LED** (3): F-LED-01 Én innboks for egne moduler og eksterne kilder, F-LED-07 Godkjenningskjede fra lederhierarkiet, F-LED-11 Tidsavgrenset stedfortreder
- **BYR** (2): F-BYR-24 Kundens godkjenning av lønn på mobil, F-BYR-27 Hvem trykker betal
- **PLA** (2): F-PLA-32 Agentidentitet og agentpakke, F-PLA-36 Innebygd assistent for enkle oppgaver
- **SIK** (2): F-SIK-12 Håndhevet arbeidsdeling, F-SIK-31 Agentgrenser og KI-policy

### Entiteter

**«Fase 1» (32):** D-Underenhet (ORG), D-Virksomhet (ORG), D-Arbeidsforhold (PER), D-Person (PER), D-Personbankkonto (PER), D-Stillingsperiode (PER), D-Avvik (KJO), D-Avstemmingsrapport (MYN), D-Klienttilknytning (MYN), D-Kontrollsak (MYN), D-Myndighetsabonnement (MYN), D-Myndighetskall (MYN), D-Systembruker (MYN), D-Avstemming (REG), D-Avstemmingslinje (REG), D-Kontomapping (REG), D-Regnskapskonto (REG), D-Bruker (POR), D-Innloggingsmetode (POR), D-Rolletildeling (LED), D-Byra (BYR), D-Fullmakt (BYR), D-Klient (BYR), D-Rapportdefinisjon (RAP), D-Rapportkjoring (RAP), D-Abonnement (PLA), D-Integrasjon (PLA), D-Personkobling (PLA), D-Krypteringsnokkel (SIK), D-Revisjonslogg (SIK), D-Rolledefinisjon (SIK), D-Tilgangslogg (SIK)

**«Fase 1 design» (16):** D-Bankkonto (ORG), D-Lederrelasjon (ORG), D-Organisasjonsenhet (ORG), D-Kjoringsgodkjenning (KJO), D-Godkjenning (FRA), D-Bankmelding (BET), D-Betalingsfil (BET), D-Betalingsforslag (BET), D-Betalingslinje (BET), D-Betalingsoppdrag (BET), D-KID (BET), D-Kontoendring (BET), D-Delegering (LED), D-Godkjenningsregel (LED), D-Kundegodkjenning (BYR), D-Arbeidsdelingsregel (SIK)

Entitetene til F-SIK-25, F-SIK-27 og F-SIK-33 (D-Lagringssted, D-Underleverandor, D-Sikkerhetshendelse) er ikke merket. De kan være dokumenter og driftsrutiner i fase 1, ikke tabeller i produktet.

## 6. Dekning

### Nye funksjoner

| Id | Navn | Gruppe | Merking | Hvorfor |
|---|---|---|---|---|
| F-PER-35 | Ansattoversikt fra a-ordningen og regnskapssystemet | PER.5 | Fase 1 | Ingen funksjon dekket en ansattoversikt uten at Brutto er master. F-PER-01 forutsetter registrering i Brutto. |
| F-MYN-42 | Kontroller på avstemmingsrapporten (A07) | MYN.4 | Fase 1 | Kontrollene i fase 1 kjører på A07-data. «Arbeidsforhold uten lønn» var ikke dekket noe sted. |
| F-REG-29 | Lesing fra regnskapssystemet: saldo, posteringer og ansatte | REG.4 | Fase 1 | Adapterne F-REG-18 og F-REG-19 skriver bilag. Ingen funksjon leste saldo og posteringer. |
| F-REG-30 | Avstemming av A07 mot hovedbok | REG.5 | Fase 1 | F-REG-24 og F-REG-25 forutsetter at lønnen er kjørt i Brutto. |
| F-BET-22 | Utbetaling via open banking-leverandør | BET.2 | Fase 1 design | F-BET-10 og F-BET-11 dekker multibank og direkte bank-API, ikke betalingsinitiering via en leverandør med BankID-signering i bankens flyt. |
| F-PLA-36 | Innebygd assistent for enkle oppgaver | PLA.6 | Fase 1 design | F-PLA-33 er en MCP-server for eksterne agenter. Ingen funksjon dekket en assistent i grensesnittet. |

Innholdet bygger på gründerens føringer og forslagene i `fase1.json` (P01–P09, K01–K05, R01–R03, B01–B09, X01–X05). Det som ikke er avklart, er merket som forslag eller [verifiseres].

### Fase 1-punktene og grunnmuren

Alle punktene har minst én funksjon.

| Punkt | Funksjoner (F1 = Fase 1, F1D = Fase 1 design) |
|---|---|
| 1. Oversikt over alle ansatte | F-PER-35 Ansattoversikt fra a-ordningen og regnskapssystemet **F1**<br>F-PER-02 Fødselsnummer og D-nummer **F1**<br>F-PER-11 Avansert søk og utvalg i personalregisteret **F1**<br>F-PLA-17 Personmatching og koblingskø **F1** |
| 2. Avstemming A07 mot regnskapet | F-MYN-21 Avstemmingsrapport (A07) mot lønn **F1**<br>F-REG-30 Avstemming av A07 mot hovedbok **F1**<br>F-REG-27 Månedlig avstemmingspakke og AGA-sperre **F1**<br>F-BYR-15 Samlehenting av tilbakemeldinger, avstemming og trekkpålegg **F1**<br>F-RAP-15 Avstemmingsrapporter **F1** |
| 3. Enkle kontroller og grafer | F-MYN-42 Kontroller på avstemmingsrapporten (A07) **F1**<br>F-MYN-38 Datakvalitet for SSB og NAV via a-meldingen **F1**<br>F-RAP-14 Kontrollrapporter mot forrige måned **F1**<br>F-RAP-21 Cut-off-test og lønn etter sluttdato **F1**<br>F-RAP-07 Rollebaserte dashbord med nøkkeltall **F1**<br>F-RAP-13 AGA-oversikt per underenhet, sone og sats **F1**<br>F-RAP-22 Headcount, FTE og turnover **F1** |
| 4. Innebygd assistent | F-PLA-36 Innebygd assistent for enkle oppgaver *F1D*<br>F-SIK-31 Agentgrenser og KI-policy *F1D*<br>F-PLA-32 Agentidentitet og agentpakke *F1D* |
| 5. Godkjenningsflyt og open banking | F-FRA-42 Én godkjenningsmodell for egne og eksterne kilder *F1D*<br>F-FRA-43 Godkjenningsregler, stedfortreder og frister *F1D*<br>F-LED-01 Én innboks for egne moduler og eksterne kilder *F1D*<br>F-LED-07 Godkjenningskjede fra lederhierarkiet *F1D*<br>F-KJO-23 Godkjenning med fire øyne og flere ledd *F1D*<br>F-BYR-24 Kundens godkjenning av lønn på mobil *F1D*<br>F-BET-06 Godkjenning av betalinger og harde sperrer *F1D*<br>F-BET-22 Utbetaling via open banking-leverandør *F1D*<br>F-BET-13 Utbetalingsstatus per betaling *F1D* |
| Kunder (tenant) | F-PLA-34 Abonnement, moduler og funksjonsbrytere **F1**<br>F-SIK-11 Tenant-isolasjon **F1** |
| Byrå og klient | F-BYR-01 Byråhierarki **F1**<br>F-BYR-02 Opprett klient med oppdragsomfang **F1**<br>F-BYR-11 Fullmaktsregister **F1** |
| Tilgang og roller | F-SIK-05 Rollekatalog med standardroller **F1**<br>F-SIK-06 Relasjoner og omfang (ReBAC), også for byrå **F1**<br>F-BYR-03 Byråroller og tilgang per oppdrag **F1**<br>F-SIK-08 Lønnstilgang og særlige kategorier **F1**<br>F-SIK-09 Revisortilgang **F1** |
| BankID-innlogging | F-SIK-01 Innlogging med BankID, passkeys og SSO **F1**<br>F-SIK-03 Step-up for kritiske handlinger **F1** |
| Kryptering av fødselsnummer og kontonummer | F-SIK-19 Feltkryptering, blind indeks og maskering **F1**<br>F-SIK-20 Nøkkelhåndtering og kryptografisk makulering **F1**<br>F-PER-02 Fødselsnummer og D-nummer **F1** |
| Revisjonslogg | F-SIK-15 Revisjonslogg **F1**<br>F-SIK-16 Tilgangslogg **F1** |
| Maskinporten og systembruker | F-MYN-01 Leverandøroppsett: Maskinporten-klient, nøkler og systemregister **F1**<br>F-MYN-02 Veiviser for systembruker hos direktekunde **F1**<br>F-MYN-04 Systembruker for klientsystem (byrå) **F1**<br>F-MYN-05 Klienttilknytning og tilgangsdiagnose per klient **F1**<br>F-MYN-06 Tilgangshelse, utløp og tilbaketrekking **F1**<br>F-BYR-07 Agent-systembruker per byrå **F1**<br>F-BYR-08 Tilknytning og tilgangsdiagnose per klient **F1** |
| Brreg | F-ORG-01 Opprett virksomhet fra Enhetsregisteret **F1**<br>F-ORG-07 Løpende synk mot Enhetsregisteret **F1**<br>F-MYN-39 Brreg-oppslag og nattlig synk **F1** |
| Lesing fra regnskapssystem | F-REG-29 Lesing fra regnskapssystemet: saldo, posteringer og ansatte **F1**<br>F-REG-01 Synk av kontoplan og dimensjoner fra regnskapssystemet **F1** |
| Lagring av rådata | F-MYN-23 Myndighetsgateway og revisjonsspor **F1** |
| Kontrollkø | F-MYN-22 Kontrollkø for myndighetsfeil **F1** |

### Topp 20-behovene

Alle de 20 behovene i `analyse-a.json` har funksjoner. Dekningen er sjekket både mot behov-id-ene i funksjonene (alle 20 rader treffer 3–47 funksjoner) og mot innholdet. Tabellen viser de viktigste funksjonene per behov.

| # | Behov | Funksjoner |
|---|---|---|
| 1 | Myndighetsflyt uten drama: a-melding med forhåndsvalidering og klartekst, skattekort i … | F-MYN-10 Forhåndsvalidering mot forretningsregler og kodelister<br>F-MYN-16 Avvik fra tilbakemeldingen i klartekst<br>F-MYN-25 Skattekortbestilling<br>F-TRK-17 Samordnet utleggstrekk fra API<br>F-MYN-31 Inntektsmelding for sykepenger via API<br>F-MYN-05 Klienttilknytning og tilgangsdiagnose per klient **F1** |
| 2 | Kontrollsenter med forklarte avvik, terskler, fire øyne og signering | F-KJO-20 Kontrollpakke og avvik mot forrige måned<br>F-KJO-21 Klartekstforklaring av differanser<br>F-RAP-14 Kontrollrapporter mot forrige måned **F1**<br>F-MYN-42 Kontroller på avstemmingsrapporten (A07) **F1**<br>F-BYR-19 Kvalitetskontroll med fire øyne |
| 3 | Strukturert grunnlag inn: innsending via lenke, import med mapping, karantene for nye … | F-BYR-22 Grunnlag via lenke<br>F-KJO-03 Mottak av lønnsgrunnlag med idempotens<br>F-LON-05 Kundens egne lønnsarter med karantene<br>F-LON-08 Mappingregister for eksterne koder<br>F-MIG-10 Excel- og CSV-maler |
| 4 | Retro med følgevirkninger og import av oppgjørsprotokoll | F-KJO-26 Retro med følgevirkninger<br>F-KJO-27 Følgevirkninger av retro utenfor lønnen<br>F-LON-28 Import av forhandlingsprotokoll<br>F-LON-29 Iverksetting og etterbetaling |
| 5 | Komplett betalingsforslag i én godkjenning: netto, forskuddstrekk og utleggstrekk med … | F-BET-01 Betalingsforslag per lønnskjøring *F1D*<br>F-BET-03 AGA og finansskatt per termin<br>F-BYR-27 Hvem trykker betal *F1D*<br>F-TRK-22 Rapportering og betaling per trekk |
| 6 | Godkjenning som låser opp bankfilen, håndhevet arbeidsdeling og kontonummer-skjold | F-BET-06 Godkjenning av betalinger og harde sperrer *F1D*<br>F-KJO-24 Hard sperre og fryseregel<br>F-BET-18 Kontonummer-skjold *F1D*<br>F-SIK-12 Håndhevet arbeidsdeling *F1D* |
| 7 | Migrering uten risiko: arbeidsforhold-ID videreført, saldoer, parallellkjøring og likt … | F-MIG-16 Arbeidsforhold-ID og startdato bevares (metode 1)<br>F-MIG-21 Hittil i år per ansatt<br>F-MIG-31 Parallell live-måned med avviksrapport<br>F-MIG-32 «Lik på øret»-protokoll |
| 8 | Godkjenning på mobil for kunde og leder, i én innboks med kontekst og stedfortreder | F-LED-01 Én innboks for egne moduler og eksterne kilder *F1D*<br>F-BYR-24 Kundens godkjenning av lønn på mobil *F1D*<br>F-LED-11 Tidsavgrenset stedfortreder *F1D*<br>F-FRA-42 Én godkjenningsmodell for egne og eksterne kilder *F1D* |
| 9 | Månedlig automatisk avstemming av lønn, hovedbok, a-melding og bank | F-REG-24 Avstemming lønn mot hovedbok<br>F-REG-25 Avstemming lønn mot a-melding<br>F-REG-26 Avstemming lønn mot bank<br>F-REG-27 Månedlig avstemmingspakke og AGA-sperre **F1**<br>F-REG-30 Avstemming av A07 mot hovedbok **F1**<br>F-MYN-21 Avstemmingsrapport (A07) mot lønn **F1** |
| 10 | Bilag med dimensjoner til kundens ERP, fordelingsprofiler og periodisering | F-REG-05 Lønnsbilag per kjøring<br>F-REG-08 Dimensjonsarv og fryst kontering per linje<br>F-ORG-16 Kostnadsfordeling per arbeidsforhold<br>F-REG-12 Periodisering av etterskuddsvise tillegg og lønnsoppgjør<br>F-REG-18 Adapter for Tripletex |
| 11 | Lønnskalender, cut-off-motor og arbeidskø med eksakte frister | F-ORG-22 Lønnskalendere<br>F-KJO-02 Cut-off og utsettelse<br>F-BYR-12 Arbeidskø på tvers av egne klienter<br>F-MYN-19 Frister og fristkalender |
| 12 | Fravær og NAV i kjernen: arbeidsgiverperiode, sykmelding og inntektsmelding via API, … | F-FRA-21 Arbeidsgiverperiode med telling og sammenslåing<br>F-FRA-23 Forespørsel om inntektsmelding: kontroll og grunnlag<br>F-MYN-31 Inntektsmelding for sykepenger via API<br>F-FRA-25 Refusjonsreskontro og avstemming mot K27 |
| 13 | Forklart lønnsslipp, generert fra beregningen | F-KJO-43 Forklaring på lønnsslippen<br>F-POR-09 Forklart lønnsslipp: «Hvorfor endret lønna seg?»<br>F-KJO-16 Forklaringsspor per linje |
| 14 | Mottakerklasse og betalende enhet, med BankID-onboarding av honorarmottakere | F-ORL-01 Sju mottakerklasser per relasjon og utbetaling<br>F-ORL-09 Betalende juridisk enhet per utbetaling<br>F-ORL-05 Engangsinvitasjon med BankID-bekreftelse |
| 15 | Egne moduler som kan byttes ut: felles offentlig API, kilderegister, blanding per … | F-PLA-01 Offentlig REST-API som egne moduler også bruker<br>F-PLA-13 Kilderegister per datatype og omfang<br>F-PLA-14 Kildebytte ved periodeskifte<br>F-PLA-15 Lønnsgrunnlag v2: felles skrivekontrakt |
| 16 | Revisorinnsyn, oppdragsdokumentasjon og compliance-pakke med ISAE 3402 | F-SIK-09 Revisortilgang **F1**<br>F-RAP-19 Revisorpakke per periode<br>F-BYR-29 Oppdragsdokumentasjon etter GRFS i 5 år<br>F-SIK-32 Sikkerhetspakke for innkjøp og attestasjoner |
| 17 | Driftssikkerhet i lønnsvinduet, beregningsgaranti og lønnsfaglig support | F-SIK-34 Beredskap på lønnsdagen<br>F-SIK-25 Sikkerhetskopi og gjenoppretting **F1**<br>F-KJO-18 Regelpakker og årshjul<br>F-SIK-35 Endringsstyring, release-diff og lønnsfaglig godkjenning |
| 18 | Ideell sektor: tariffbibliotek, KLP og prosjekt- og finansiørrapport | F-LON-19 Tariffbibliotek med lønnsstiger<br>F-PEN-11 KLP: lønnsfil og endringsmeldinger<br>F-ORG-21 Prosjektlønn og finansiørprosjekter<br>F-RAP-29 Prosjektlønn og timeark for tilskudd |
| 19 | Byråmaler med arv, stedfortreder og omfordeling med ett grep | F-BYR-18 Byråmaler med arv og utrulling<br>F-BYR-04 Tildeling, stedfortreder og masseomfordeling<br>F-LON-07 Lønnsartmaler for byrå og konsern<br>F-REG-04 Byråmal og kjedemal for kontering |
| 20 | Huma-integrasjon med eierskap per felt og sikret bankkontoendring, og en datamodell … | F-PER-33 Huma som HR-master: mapping av person, stilling og organisasjon<br>F-PER-32 Eierskap per attributtgruppe<br>F-PLA-22 Huma-kobling (K-HUMA)<br>F-BET-18 Kontonummer-skjold *F1D* |

## 7. A-meldingsfeltnavn

Navnene `arbeidsforholdId`, `norskIdentifikator`, `kalendermaaned`, `loennsutbetalingsdato`, `inngaarIGrunnlagForTrekk`, `utloeserArbeidsgiveravgift` og `sisteLoennsendringsdato` er skrevet likt overalt der de brukes som a-meldingsnavn. Ingen varianter som `arbeidsforholdID`, `lonnsbeskrivelse` eller `kalendermaned` ble funnet.

**14 verdier i kolonnen `amelding` er rettet:**

| Entitet og felt | Før | Etter |
|---|---|---|
| D-Klient.organisasjonsnummer | `Opplysningspliktig.norskIdentifikator` | `opplysningspliktig.norskIdentifikator` |
| D-Engasjement.betalende_virksomhet_id | `Opplysningspliktig / Virksomhet` | `opplysningspliktig / virksomhet` |
| D-Engasjement.periode_fra | `Arbeidsforhold.startdato` | `arbeidsforhold.startdato` |
| D-Engasjement.periode_til | `Arbeidsforhold.sluttdato` | `arbeidsforhold.sluttdato` |
| D-Engasjement.arbeidsforhold_id | `Arbeidsforhold.arbeidsforholdId` | `arbeidsforhold.arbeidsforholdId` |
| D-Engasjement.arbeidsforholdstype | `Arbeidsforhold.arbeidsforholdstype` | `arbeidsforhold.typeArbeidsforhold` |
| D-Mottakerklasse.mottakerklasse | `Avledet: Arbeidsforhold.arbeidsforholdstype` | `Avledet: arbeidsforhold.typeArbeidsforhold` |
| D-Honorarsats.lonnsart_id | `Inntekt.beskrivelse (styrehonorarOgGodtgjoerelseVerv)` | `inntekt.loennsinntekt.beskrivelse (styrehonorarOgGodtgjoerelseVerv)` |
| D-Organisasjonsprofil.regel_10000 | `Inntekt.skatteOgAvgiftsregel (skattefriOrganisasjon)` | `inntekt.skatteOgAvgiftsregel (skattefriOrganisasjon)` |
| D-Organisasjonsprofil.aga_fritak_23_2 | `Inntekt.beskrivelse (loennUtbetaltAvVeldedigEllerAllmennyttigInstitusjonEllerOrganisasjon)` | `inntekt.loennsinntekt.beskrivelse (loennUtbetaltAvVeldedigEllerAllmennyttigInstitusjonEllerOrganisasjon)` |
| D-TaptArbeidsfortjeneste.a_melding_beskrivelse | `Inntekt.beskrivelse [verifiseres]` | `inntekt.beskrivelse [verifiseres]` |
| D-Virksomhet.spraak_for_tilbakemelding | `Leveranse/spraakForTilbakemelding` | `leveranse/spraakForTilbakemelding` |
| D-Lonnsperiode.rapporteringsmaaned | `Leveranse/kalendermaaned` | `leveranse/kalendermaaned` |
| D-Migreringsprosjekt.metode_arbeidsforhold_id | `arbeidsforholdId, sluttaarsak (verifiseres)` | `arbeidsforholdId, aarsakTilSluttdato (verifiseres)` |

De to viktigste er `arbeidsforholdstype` → `typeArbeidsforhold` (K1 bruker det offisielle navnet) og `sluttaarsak` → `aarsakTilSluttdato` (K1 skriver selv at a-meldingen ikke bruker navnet «sluttaarsak»). De andre er store forbokstaver i elementnavn og en manglende `loennsinntekt` foran `beskrivelse` der koden er en lønnsbeskrivelse.

Tvilstilfeller er ikke endret. De står i listen nedenfor (punkt 9–12).

## 8. Spørsmål

10 spørsmål er slått inn i 9 andre. Det beholdte spørsmålet har fått et avsnitt som sier hva som er slått inn, og tar med det som var nytt i duplikatet (forslag, funksjoner og kontaktadresser).

| Beholdt | Slått inn |
|---|---|
| Standard AGA-metode for NAV-refusjon (K4, MYN) | «Standard AGA-metode for NAV-refusjon» fra K3 (FRA, Lønnsfag) |
| Hjemmel, frist og avsender for sammenstillingsoppgaven (K4, MYN) | «Sammenstillingsoppgave: hjemmel, frist og avsender» fra K5 (POR, Jurist) |
| Timesatser for Forskningsrådet og Horizon Europe (K1, ORG) | «Satser for Forskningsrådet og Horizon Europe» fra K6 (RAP, Lønnsfag) |
| Minste gruppestørrelse i statistikk (K6, RAP) | «Minste gruppestørrelse for kostnadstall» fra K5 (LED, Gründer) |
| Huma: API-vilkår, dokumenteksport og retry (K6, PLA) | «Huma: retry og eksport av fravær» fra K3 (FRA, Partner) |
| Klientdelegering, REGN-rollen og kvoten på 5 samtidige kall for byrå (K4, MYN) | «Tilgangspakke uten REGN-rolle og kvote for samtidige kall» fra K5 (BYR, Teknisk)<br>«ID-porten-klient for klientdelegering» fra K5 (BYR, Teknisk) |
| Bidragstrekk: kanal og a-meldingskode (K2, TRK) | «Kommer bidragstrekk i Trekkpålegg-API-et?» fra K4 (MYN, Skatteetaten) |
| Hvordan OTP-premien kommer inn, og AGA av den (K2, PEN) | «AGA av OTP-premie fra faktura» fra K4 (REG, Revisor) |
| Inntektsmelding for foreldre- og svangerskapspenger og sykdom i familien fra lønnssystem (K4, MYN) | «Omsorgspenger: LPS-API eller Min side etter 21.5.2026?» fra K3 (FRA, NAV) |

## 9. Tvilstilfeller

1. **Assistenten** er merket «Fase 1 design», ikke «Fase 1». Gründeren har lagt den i fase 1, men skriver at den kan komme senere. Grensene (F-SIK-31) bør uansett bestemmes nå.
2. **D-Personbankkonto** er merket «Fase 1» fordi grunnmuren krever kryptering av kontonummer. Kontonummeret kan hentes fra regnskapssystemet (F-REG-29). Funksjonen F-PER-07 med kontonummer-skjold er bare merket «Fase 1 design», fordi skjoldet først trengs ved utbetaling.
3. **Godkjenning og utbetaling** er merket «Fase 1 design» fordi det ikke er avklart om de hører til fase 1 eller 2. Hva som skal godkjennes før Brutto kjører lønn selv, er heller ikke avklart. D-Lonnskjoring er derfor ikke merket.
4. **F-REG-27** er merket «Fase 1» for selve avstemmingspakken. AGA-sperren i samme funksjon hører ikke til fase 1.
5. **F-ORG-29** (oppstartsveiviser) er merket «Fase 1» for Brreg, underenheter, systembruker og regnskapssystem. Bankkontoer, pensjon og lønnskalender i samme veiviser hører ikke til fase 1.
6. **F-MYN-24** (overvåking av endringer hos myndighetene), **F-SIK-28** (DPIA) og **F-SIK-33** (hendelseshåndtering) er tatt med fordi fase 1 er helt avhengig av Skatteetatens API og behandler lønn og fødselsnummer fra første kunde. De kan flyttes ut hvis fase 1 skal være enda smalere.
7. **F-PER-35** forutsetter at avstemmingsrapporten har med nok om arbeidsforholdet (stillingsprosent, yrke). Det er merket [verifiseres].
8. **Ingen egen tenant-entitet.** Se anbefaling 13 i kapittel 2.
9. **Skilletegn i a-meldingsstier:** K1 skriver `arbeidsforhold/yrke`, de andre `arbeidsforhold.yrke`. K3 utelater ofte `inntekt.` foran `loennsinntekt`. K4 bruker skjemanavn fra OpenAPI som `Bestilling.` og `Feil.`. Alt er forståelig, men bør gjøres likt hvis kolonnen skal leses av maskin. Det er en mekanisk endring på om lag 200 verdier.
10. **Feltnavnkonvensjon:** K1, K2, K5, K6 og K7 bruker `arbeidsforhold_id` og `norsk_identifikator`, mens K3 og K4 bruker `arbeidsforholdId`. K2 skriver `maned`, `lonn` og `arsak`, de andre `maaned`, `loenn` og `aarsak`. NAV-feltet heter `redusertLoennIAgpBeloep` i K3 og `redusertLoennIAgp_beloep` i K4. Dette er interne navn og ikke skrivefeil, så de er ikke endret. Velg én konvensjon før datamodellen kodes.
11. **avloenningstype:** K2 (D-Lonnsavtale) peker til `arbeidsforhold.avloenningstype`, mens K1 (D-Stillingsperiode) skriver at feltet utgikk fra a-meldingen i 2019. Det må sjekkes mot gjeldende informasjonsmodell.
12. **D-TaptArbeidsfortjeneste:** Bare forbokstaven er rettet (`inntekt.beskrivelse [verifiseres]`). Om tapt arbeidsfortjeneste rapporteres som `loennsinntekt` eller noe annet, er ikke avklart.
13. **Spørsmål som overlapper, men ikke er slått sammen:**
    - «Huma: datoer, sluttårsak og API-vilkår» (K1) og «Huma: API-vilkår, dokumenteksport og retry» (K6). Hovedtemaet er ulikt.
    - «Retting av 2027-perioder etter overgangen til a-melding 2.4» (K4) og «Format for retting av perioder fra før overgangen» (K6). Det ene gjelder formatskiftet, det andre systembytte.
    - «Endringer i a-meldingens kodeliste fra 2030» (K1) og «Nye permitteringsfelt i a-meldingen» (K3).
    - «Egen rolle «Lønn: helse» eller samme vern som lønnsdata» (K6) og «Én helserolle eller tre» (K7).
    - «Grensen mellom D-Godkjenning, D-Arbeidsflyt og godkjenningsregler» (K5) og «Grensen mellom KOM og LED/POR for innboks og varsler» (K7).
    - «Slettefrist for sykmeldinger og søknader» (K3) og «Oppbevaring og behandlingsgrunnlag for HR-data» (K7).
14. **design.json:** De 35 spørsmålene der er en sammenstilling og dekker mange av K-spørsmålene på nytt (for eksempel AGA-metode for NAV-refusjon, AGA av OTP-premie, REGN-rollen og ID-porten-klient, inntektsmelding fra lønnssystem, bidragstrekk, sammenstillingsoppgaven, Huma, 2027-perioder, F532 og KID). Siden byggeren fletter begge listene, vises disse to ganger under «Åpne spørsmål». Feltet `omrade` er en kategori, ikke en områdekode, og statusen «Stopper» brukes bare der. Filen er ikke endret fordi den lages av `build/gen/p6_sporsmal.py` og sorteres på kategoriene i `gen/main.py`. Forslag: la `design.json` være oversikten, gi hvert design-spørsmål en lenke til K-spørsmålene det dekker, og skjul eller merk K-spørsmålene som er dekket.

## 10. Filer

- Oppdatert: `scratchpad/build/data/omr-K1.json` til `omr-K7.json`.
- Skript: `scratchpad/r5/apply.py` (kjør med `--dry` for å se tallene uten å skrive).
- Originaler: `scratchpad/r5/backup/`.
- Tall og endringslogg: `scratchpad/r5/stats.json`.
