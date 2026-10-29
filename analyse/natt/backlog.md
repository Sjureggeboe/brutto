# Backlog for nattarbeid

Status: `åpen` → `pågår` → `ferdig` (eller `utsatt` med grunn). Prioritet 1 er viktigst. Fase: `F1` = fase 1, `MVP` = lønnskjøring, `Senere`.
Loopen tar alltid de øverste åpne punktene etter prioritet. Nye punkter legges nederst i riktig prioritet med neste ledige id.

| Id | Prio | Fase | Status | Tittel |
|---|---|---|---|---|
| N01 | 1 | F1 | ferdig | Utleggstrekk, bidragstrekk og andre trekk: hvor kommer informasjonen fra, og kan vi hente alt automatisk? |
| N02 | 1 | F1 | ferdig | Regnskapsføring av lønnskjøringen: bilag per konto eller per ansatt med reskontro? |
| N03 | 1 | F1 | ferdig | Avstemmingsrapporten (A07): eksakt innhold og hvordan A07-avstemming gjøres i praksis |
| N04 | 1 | F1 | ferdig | Lesing fra regnskapssystemene: saldobalanse og lønnskontoer via API |
| N05 | 1 | F1 | ferdig | Ansattoversikt fra a-ordningen: hvilke data finnes, og finnes Skatteetatens arbeidsforhold-API? |
| N06 | 1 | F1 | ferdig | Bli leverandør hos Digdir, Skatteetaten og Altinn: konkret sjekkliste, tid og kostnad |
| N21 | 1 | F1 | ferdig | ReAi, Vinderen Industrier: hvordan lønn, trekk, A07-avstemming og regnskap henger sammen, og hva som er automatisert |
| N22 | 1 | F1 | utsatt | TT02-test av avstemmingsrapporten: svartid, historikk, summering, arbeidsforhold og 429 (utsatt: krever Maskinporten-klient og testmiljø, ingen innlogging i natt) |
| N23 | 1 | F1 | ferdig | A07-mapping som datafil: lønnsbeskrivelse → A07-gruppe og konto/grupperingskode → A07-gruppe med saldoregel |
| N26 | 1 | F1 | ferdig | Tilgang til Trekkpålegg-API uten innsending: teller avstemming som formål? Utkast til henvendelse (sendes av et menneske) |
| N35 | 1 | F1 | ferdig | Arbeidsforhold-ID i Tripletex og ReAi: hvilken verdi sendes som arbeidsforholdId i a-meldingen, og hvordan kobles den mot A07? |
| N36 | 1 | F1 | ferdig | Kontrollkatalog ANS-01–17 for ansattoversikten: verifiser mot Skatteetatens regler, sett terskler og lag kodelister |
| N39 | 1 | F1 | ferdig | Testdata for A07 i TT02 og Tenor: finnes syntetiske virksomheter med a-meldinger, og hvordan settes et testbyrå opp? |
| N40 | 1 | F1 | ferdig | Vilkår og tilgang i grensetilfeller: API-vilkår hos Tripletex, Visma og Fiken, formålsbegrensning i SBS-vilkårene, byråer uten REGN-rolle, klientdelegering |
| N27 | 1 | F1 | ferdig | Dialogporten i fase 1: trekkbrev, «Kontroll av forskuddstrekk» og tilbakemelding (A03) for a-meldinger sendt fra andre systemer |
| N07 | 2 | F1 | ferdig | Kontrollkatalog for lønnsavstemming: hvilke kontroller byråer og revisorer faktisk gjør |
| N08 | 2 | F1 | ferdig | Rust-økosystemet for Brutto: Maskinporten, OpenAPI-klienter, desimaler, PDF, Postgres |
| N09 | 2 | F1 | ferdig | Open banking-leverandører for lønnsutbetaling fra bedriftskonto i Norge |
| N10 | 2 | F1 | ferdig | Godkjenningsflyt for lønn i konkurrentene og i praksis |
| N11 | 2 | F1 | ferdig | Konkurrentenes A07-avstemming og lønnskontroller: Tripletex, PowerOffice, Visma, SD Worx, Intect |
| N12 | 2 | F1 | ferdig | Assistenten: sikre KI-agenter i finans-SaaS, EU-region for Claude, verktøytilgang |
| N24 | 2 | F1 | ferdig | Kontrolloppstillingen (tidl. RF-1022) i næringsspesifikasjonen: poster, feltnavn og levering til årsoppgjørsverktøy |
| N25 | 2 | MVP | ferdig | Tilgang i MVP: Krav og betalinger for byrå, og portveien «Brutto sender a-meldingen» for kunder med eget lønnssystem |
| N28 | 2 | MVP | ferdig | Samordnet utleggstrekk i detalj: prosentgrunnlaget og overgangen for gamle bidragstrekk (puljene P8 og P10) |
| N30 | 2 | MVP | ferdig | Dokumentasjonsmodellen for lønn: holder aggregert bilag + § 5-6-journal i Brutto (NBS 2 pkt. 4.7), eller blir Brutto del av regnskapssystemet (pkt. 4.5)? |
| N31 | 2 | MVP | ferdig | Utlegg via integrasjon og ansattreskontro: hvem bokfører utlegget, og hvordan lukkes posten når utbetalingen går i lønn? |
| N32 | 2 | F1 | ferdig | Integrerte lønnsmoduler i praksis: hvordan fører Tripletex og PowerOffice nettolønn, AGA og feriepenger (samlet/per ansatt, 2910/2930)? |
| N37 | 2 | F1 | ferdig | Ansatt-API i Visma (eAccounting, Payroll, Lønn), Xledger, 24SevenOffice og Uni Micro, og eksport fra Fiken |
| N38 | 2 | F1 | ferdig | Navneliste-import og personvern for A07-data per person i fase 1 (fagforening, permisjon, lønn) |
| N17 | 2 | MVP | ferdig | Lønnsbetaling i bank: ZTLs tillatelse og klientmidler, pain.001/SALA, PSD2-bulk i DNB/Nordea/SpareBank 1/Eika, KID for trekk, adressekrav (prio hevet fra 3) |
| N13 | 3 | MVP | ferdig | Skatteetatens trekkrutine: størrelse, lisens og hvordan den kan brukes fra Rust |
| N14 | 3 | MVP | ferdig | A-melding 2.4: hva er kjent om endringene, og hva betyr det for datamodellen? |
| N15 | 3 | MVP | ferdig | NAV-refusjon og K27: kan avstemmingen av refusjoner automatiseres helt? |
| N16 | 3 | MVP | ferdig | Pensjonsleverandører: rapportering og API hos Storebrand, DNB, KLP, Gjensidige, SPK |
| N18 | 3 | MVP | ferdig | Huma-API i detalj: import av ansatte og fravær, vilkår og begrensninger |
| N19 | 3 | Senere | ferdig | Personvern: DPIA for lønnssystem, Datatilsynets krav, databehandleravtale for byråkanalen |
| N20 | 3 | Senere | ferdig | Tariffdata: hvor finnes lønnstabeller (Virke HUK, NHO Geneo, KS) maskinlesbart? |
| N29 | 3 | MVP | ferdig | Ansvarskrav mot arbeidsgiver ved feil trekk: hjemmel i ny innkrevingslov, varsling og frister |
| N33 | 3 | MVP | ferdig | Bilag til Visma eAccounting, Business NXT, Xledger og 24SevenOffice: dimensjon, ansatt, vedlegg, idempotens, utkast og skjuling av lønn |
| N34 | 3 | Senere | ferdig | Finansiørkrav: kan lønnskost per person per prosjekt til Forskningsrådet og EU dokumenteres fra Brutto uten ansatt i hovedboken? |

---

## Detaljer per punkt

### N01 Utleggstrekk, bidragstrekk og andre trekk
Gründerens spørsmål: Hvor får den som kjører lønn informasjon om utleggstrekk, barnebidrag osv.? Må de hente meldinger i Altinn og registrere dem manuelt på ansattkortet, eller kan vi hente det meste automatisk og kontrollere på ett sted at alle trekk er kommet med?
- Kartlegg alle typer trekkpålegg: utleggstrekk fra Skatteetaten/innkrevingsmyndigheten (samordnet utleggstrekk fra 2026), bidragstrekk (NAV Innkreving, som ble del av Skatteetaten 01.01.2026), namsmannens trekk, kommunale krav, Statens innkrevingssentral, private kreditorer via namsmann, trekk for skatt (restskatt).
- For hver type: hvem sender, i hvilken kanal (Trekkpålegg-API, Altinn-melding, Dialogporten, brev), i hvilket format, og hva arbeidsgiver må gjøre (start, endre, stanse, kvittere, betale med KID, rapportere i a-meldingen).
- Hva kan hentes automatisk i dag (API-er, tilgangspakker, også for byrå med `regnskapsforer-lonn`), og hva må fortsatt gjøres manuelt?
- Fullstendighetskontroll: Finnes det en kilde som viser alle aktive trekk for en arbeidsgiver eller ansatt (Krav og betalinger-API, avstemmingsrapporten, tilbakemelding på a-meldingen, Skatteetatens oversikt)? Hvordan bygge «ett sted å sjekke at alt er med»?
- Hvordan gjør Tripletex, PowerOffice, Visma og SD Worx det i dag?
- Konsekvens for fase 1: kan Brutto vise og kontrollere trekk allerede i fase 1, før lønnskjøring finnes?
- Kilder: research/R2-myndighetsintegrasjoner.md §3 (trekkpålegg), B-myndigheter.md §7, skatteetaten.github.io, skatteetaten.no/fremtidens-innkreving, nav.no.

### N02 Regnskapsføring av lønnskjøringen
Gründerens spørsmål: Hva er foretrukket når lønnskjøringen skal føres i regnskapet? Importerer man ett bilag med sum per konto, eller importerer man slik at man kan spore per ansatt via reskontro? Gründeren tror sporing per ansatt blir et helvete å avstemme og administrere, fordi alle ansatte også må legges inn i regnskapssystemet.
- Hva krever bokføringsloven og -forskriften: lønnsjournal, spesifikasjon per ansatt (§ 5-5?), sporbarhet fra bilag til grunnlag? Holder det med samlebilag pluss lønnsjournal i lønnssystemet?
- Hvordan gjør Tripletex, PowerOffice Go, Visma (eAccounting/Business NXT), Xledger, Fiken og 24SevenOffice import av lønnsbilag fra eksterne lønnssystemer? Hvilke formater og API-er finnes? Støtter de ansattreskontro?
- Hva er vanlig praksis hos byråer og revisorer: samlebilag per kjøring, per avdeling/prosjekt, eller per ansatt? Når trengs ansattreskontro (forskudd, lån, utlegg, trekk)?
- Gründerens egen avklaring (S-avklaringer §2.9 og §6): nettolønn samlet per kjøring på 2930, så hovedboken ikke viser enkeltlønn.
- Anbefaling til Brutto: hva standard, hva valgfritt, og hvordan dimensjoner (avdeling/prosjekt) følger med uten ansattreskontro.

### N03 Avstemmingsrapporten (A07)
- Les OpenAPI for avstemmingsrapport-amelding 1.0.2. Hvilke felt finnes per opplysningspliktig, virksomhet, inntektsmottaker, inntekt, forskuddstrekk, AGA? Finnes arbeidsforhold?
- Bestillingsflyt, svartider, hvor langt tilbake, endringer fra 12.10.2026.
- Hvordan gjøres A07-avstemming i praksis (byråer, Regnskap Norge-maler, revisorer)? Hvilke kontoer mot hvilke lønnsbeskrivelser?

### N04 Lesing fra regnskapssystemene
- Tripletex, PowerOffice Go, ReAi, Fiken, Visma, Xledger: API for saldobalanse per konto og periode, posteringer på lønnskontoer, dimensjoner. Autentisering, partneravtale, byråtilgang, rate limits, pris.
- Brukerens egne verktøy i økten kan brukes til å lese struktur (Tripletex- og ReAi-skills), kun lesing og uten personopplysninger.
- Fra N03: Avstemmingen trenger debet og kredit per konto og måned, pluss IB og UB for 2931, 2932, 2940, 2945, 2967, 2780, 2785, 2600–2690 og 2770. Saldobalansen alene er ikke nok. Sjekk om hvert API gir dette, og om grupperingskoder (f.eks. 7155/7165) og NS 4102-standardkontoer kan leses.

### N05 Ansattoversikt fra a-ordningen
- Hva kan bygges av avstemmingsrapporten alene? Finnes Skatteetatens `api/arbeidsforhold` (sett i API-listen), og hva gir den? Tilgang for arbeidsgiver og byrå?
- Alternativer: regnskapssystemets ansattregister, Huma, import.

### N06 Bli leverandør
- Konkret sjekkliste med lenker: avtale i Samarbeidsportalen, Maskinporten-klient (test og prod), registrering i Altinns systemregister (standard og klientsystem), Skatteetatens bruksvilkår, testmiljø TT02, Tenor. Hvem i selskapet må gjøre hva, hva koster det, hvor lang tid tar det.

### N21 ReAi og Vinderen Industrier (tenant 2915)
Gründeren har gitt tillatelse til å teste i ReAi på Vinderen Industrier AS, også med skrivende kall, så lenge alt slettes etterpå (natt/reai-opprydding.md).
- Kartlegg hvordan lønn henger sammen: ansatt og arbeidsforhold, lønnsoppsett (salarySettingsApi), skattekort (taxCardApi), faste trekk etter skatt (employeeRecurringPostTaxDeductionApi), lønnsutbetaling (salaryPaymentApi), a-melding (aMeldingApi), A07-avstemming (aMeldingReconciliationApi), ansattreskontro (employeeLedgerApi), bilag og kontering (voucherApi, postingApi) og utlegg (expenseApi).
- Hva gjør ReAi automatisk, og hva må brukeren gjøre? Hvordan føres lønnen i regnskapet: samlet eller per ansatt? Hvordan håndteres trekkpålegg?
- Hvis det trengs testdata: lag dem som utkast, logg alt i oppryddingsfilen og slett i samme runde. Send aldri noe ut (se regler i loop-prompten).
- Ingen personopplysninger i funnet. Beskriv bare struktur, felt, flyt og automatisering.
- Funnet skal brukes i N01, N02, N03 og N04.
- Fra N05: Hvordan lager ReAi arbeidsforhold-ID-en i a-meldingen når `employmentId` er null? Hvilke felt har ansatt og `employment-reporting`?
- Fra N02: Fører ReAi nettolønn, AGA og feriepenger samlet eller per ansatt, og på 2910 eller 2930? Hvilke kontoer er ansattreskontro?

### N22 TT02-test av avstemmingsrapporten (fra N03)
Mål svartid og hvor lenge rapporten kan hentes. Test hvor langt tilbake API-et svarer, om flere måneder summeres, om arbeidsforhold og navn kommer med ved bestilling for flere måneder, hva `utenInntektsmottakere` fjerner, om `utleggstrekk[]` fylles og hvor grensen for 429 går. Utsatt: krever Maskinporten-klient og TT02-tilgang. Oppgave for Peter og Sander når klienten finnes (se N06).
- Fra N06: Test også om `authorizedparties` med agent-token gir de delegerte klientene med `authorizedAccessPackages`, og om det finnes et vendor-API for klientlisten uten ID-porten.
- Fra N33: Tripletex testmiljø: kan `voucherType` settes til «Lønnsbilag» via API, virker `:reverse` på manuelt lønnsbilag, skjuler «Lønnsinformasjon» API-bilag, krever `:closePostings` samme ansatt og sum 0? ReAi tenant 2915 (krever eksplisitt ja fra brukeren i sesjonen): manuelt bilag mot 2930/2940 uten `employeeId`, lukking med `postings/employee/close`, sletting. PowerOffice: avvises samlet netto på 2930 når kontoen er ansattreskontro?
- Fra N20: Har A07 beregningskode og annen bagatellmessig støtte per virksomhet og måned? Hvor stor andel av Brreg-adresser for underenheter i de 12 delte kommunene finnes i Kartverkets adresse-API, og hvor mange er postboks?
- Fra N18: Test Huma Open API med nøkkel fra en pilotkunde: minste rolle som gir `identifications` uten lønn og bankkonto, innhold i `connectedIntegrations`, om `GET /users` tar med deaktiverte, rate limit-headere, hvilken dato tilsvarer a-meldingens startdato.
- Fra N16: Kalibrer L-21a–j på klienter vi leser fra (andel med innretning, treff i L-21a, L-21g-differanse per termin). Gir A07 for flere måneder `pensjonsinnretning[]` per måned eller samlet? Vises MAGNET_EDAG-507 i A07 `avvik[]`? Hvilken grupperingskode gir Tripletex, PowerOffice og ReAi kontoene 5945 og 5950 for AS?
- Fra N15: Testrapporter `ref-arbg` i NAVs dev (`sokos-oppgjorsrapporter.ekstern.dev.nav.no`), Altinn Events for `nav_utbetaling_oppgjorsrapport-refusjon-arbeidsgiver`, `etterId` over årsskiftet, negativ rapportsum. Banktekst for NAV-refusjon i camt.053/054. Fordringskonto for refusjon hos Tripletex- og PowerOffice-klienter (bare kontonavn og saldo).
- Fra N13: AGA-avrunding: send a-meldinger med AGA på x,30, x,50 og x,99 kr – godtar F185 nedrunding, nærmeste krone eller toleranse? Maks antall desimaler i `Beloep` (F280)? Retning for «ned» ved negative trekk og korreksjoner?
- Fra N14: Tvangsmulktdialoger i TT02: hvilke felt skiller a-meldingsmulkt fra andre, er påminnelse, vedtak og faktura egne dialoger, kan PDF hentes? Hva inneholder `ske-arbeidsgiverkontroll`-dialogene?
- Fra N38: Hvilke summer er med i A07 med `utenInntektsmottakere = true` (fradrag per type, fagforening, utleggstrekk)? Holder modusen «Avstemming» for kontrollene i P05?
- Fra N37: Henter Tripletex' avstemmingsmodul A07 med byråets systembruker etter Altinn 3, eller kreves Altinn-innlogging? Er Visma.net Payroll `position.id` arbeidsforhold-ID-en som rapporteres?
- Fra N32: Kjør N23-regelsettet `tripletex_lonn` på 2–3 Tripletex-klienter (bare aggregert) og mål hvor mye av differansen mot A07 som forklares med og uten fjerning av reverseringspar. Les et PowerOffice `PayrollJournal` med flere ansatte når OAuth virker (2930 samlet? 2940 én eller to linjer? AGA per sone?). Hva returnerer Tripletex `/ledger/posting` og `/balanceSheet` når tokenet mangler lønnstilgang? Hva er tomme lønnsbilag og «Øreavrunding» på 2770?
- Fra N28: Får arbeidsgiver stoppmelding fra hver gamle påleggsgiver ved overgang til samordnet trekk, eller bare samlebrev? Test T9-grov (implisitt prosent) på syntetiske A07-data og mål falske avvik.
- Fra N25: TT02-test av Correspondence med standard systembruker (enkeltrettigheter på `skd-migratedcorrespondence-*`, status «Hentet», tokenveksling). Tenor-test av Krav og betalinger (vises samordnet utleggstrekk eller utleggstrekk skatt i arbeidsgiverens reskontro, `terminTekniskNavn`, enkeltpersonforetak). Subjektformat i Dialogporten-hendelser og `includeSubunits`.
- Fra N24: Kalibrer L-30a–i (natt/funn/N24.md §6) på én klient og mål hvor mange treff som er reelle. Kan revisor bekrefte `spesifikasjonAvLoennsOgPensjonskostnad` for seg i TT02?
- Fra N11: Bekreft at `utleggstrekk[]` fylles i A07 (PowerOffice skriver at A07 ikke har utleggstrekk). T4, T5 og L-03 avhenger av det.
- Fra N07: Test L-18: hvor nær treffer estimert feriepengegrunnlag fra A07 avsetningen på 2940? (Bare summer.)
- Fra N27: Test A03 fra annet system (testplan i natt/funn/N27.md §6) med standard- og agent-systembruker. Bekreft at `/transmissions` ikke skriver sett-logg. Én dialog per innsending eller per periode? Hvordan ser dialogene ut når et byrå sender? Hva står i tittel, sammendrag, `extendedStatus` og `externalReference` for trekkbrev og trekkontroll?
- Fra N40: Test direkte delegering av `a-ordning` til et Tenor-byrå uten REGN, systembruker for klientsystem med `a-ordning`, OG-forholdet med to pakker, og om styreleder i en forening kan gi fullmakt. Test systembruker med `klientadministrator` mot `authentication/api/v1/enduser/systemuser/clients`.
- Fra N39: Første test: gir A07 i TT02 data for Tenors «Inntekt A-ordningen» (H1), eller bare for innsendte test-a-meldinger (H2)? Krever test-innsending at inntektsmottakerne finnes i det syntetiske Folkeregisteret? Hvor langt bakover kan vi sende (`AMLD_1027`)? Nullstiller en tom erstatningsmelding måneden? Holder daglig leder for manuell filopplasting i test? Slettes innsendte test-a-meldinger jevnlig? Godtas `utleggstrekkSamordnet` med KID uten testpålegg? Gir KQL `regnskapsfoerere:<orgnr>` byråets klienter i Tenor? Kan godkjenning av systembruker i TT02 skriptes (Playwright)? Testplan: natt/funn/N39.md (TV-1–TV-8, S01–S27).
- Fra N36: Skiller a-ordningen `abc` fra `ABC` og `07` fra `7`? Gir alternativ 2 avvik 108 for den gamle ID-en? Format på `avvik.id` i A07 og A03 (`MAGNET_EDAG-529` eller `529`)? Kommer F529 i `inntekt.avvik[]`? Hvordan vises stillingsprosent over 100? Er `permittering[]` tom og permittering i `permisjon[]`? Godtas tom `arbeidsforholdId`?
- Fra N23: Kjør mappingen (natt/funn/N23-mapping.csv) på A07 og hovedbok for én klient og mål hvor mye av differansen regelsettet forklarer. Er forskuddstrekk og fradrag negative i A07-JSON? Har virksomhetsnivået fradrag og forskuddstrekk per beskrivelse? Les grupperingskodene for lønnskontoene i PowerOffice (MCP ga 401 i natt).
- Fra N35: Sammenlign A07 med Tripletex `Employment.id` for en testklient, og bekreft at importert `employmentId` sendes. Viser PowerOffice `GET /Employees/Employments` den tildelte `ReportingId`? Hvordan ser A07 ut når en gammel ID ikke avsluttes (alternativ 2, avvik 108)? Er `reportedName` og `employeeNumber` fylt for personer med fødselsnummer?
- Fra N04: Test også lesingen i Tripletex' testmiljø (api-test.tripletex.tech) og PowerOffice demo: stemmer `/balanceSheet` med summen av `/ledger/posting`, skjules lønnsposteringer uten lønnstilgang, og hva er faktisk rate limit? Gründeren må opprette testkontoene.
- Fra N05: Test også om `identifiserendeInformasjon.navn` fylles for personer med fødselsnummer, om personer med arbeidsforhold uten inntekt i måneden er med, og om avsluttede arbeidsforhold gjentas måneden etter. Bruk Tenor-data med tilkallingsvikar, permisjon og permittering.

### N23 A07-mapping som datafil (fra N03)
- Lag et utkast til datafil (i natt/funn, ikke i build/data) med to retninger: lønnsbeskrivelse (a-meldingskode) → A07-gruppe, og konto eller grupperingskode → A07-gruppe med saldoregel (bevegelse, debet, kredit, IB, UB).
- Kontroller mot kodelisten for a-meldingen (R1 2026), NS 4102 og grupperingskodene i S-avklaringer #28 (7155/7165). Ta med naturalytelser, feriepenger, pensjon, refusjoner og AGA.
- Se natt/funn/N03.md §6–§7 for avvikskatalog og datamodell (D-A07Gruppe, D-A07Kontoregel).

### N24 Kontrolloppstillingen i næringsspesifikasjonen (fra N03)
- Kartlegg poster og feltnavn for kontrolloppstilling over lønns- og pensjonskostnader (tidl. RF-1022, skatteforvaltningsforskriften § 7-2-11) i skattemeldingen for selskap.
- Hvordan lages den i dag i Tripletex, Maestro og Sticos? Kan Brutto levere tallene ferdig, og i hvilket format?
- Fra N23: Feltnavnene er funnet (natt/funn/N23.md §6). Snevres inn til levering og eksport til årsoppgjørsverktøyene.

### N25 Krav og betalinger for byrå (fra N03)
- Hvilken tilgangspakke i Altinn trengs for Krav og betalinger-API i tillegg til `regnskapsforer-lonn`? Vil kundene typisk gi den? Hva viser API-et om betalt forskuddstrekk, AGA og trekkpålegg?

### N26 Tilgang til Trekkpålegg-API uten innsending (fra N01)
- Vilkårene krever at kunden har rapportert gjennom systemet. Teller avstemmingsrapport-API-et som «innrapporterings-API», og godtas kontroll og avstemming som formål? Les bruksvilkår og dokumentasjon på skatteetaten.github.io.
- Lag et utkast til henvendelse til Skatteetaten (fremtidensinnkreving@skatteetaten.no) i funnfilen. Utkastet sendes av et menneske, ikke av agenten.

### N27 Dialogporten i fase 1 (fra N01, N26 og N36, prio hevet til 1)
- Fra N36: Kan en systembruker med `regnskapsforer-lonn` eller `a-ordning` finne tilbakemeldingen (A03) i Dialogporten og hente `GET /forsendelser/{id}` når et annet lønnssystem har sendt a-meldingen? Går det, får Brutto Skatteetatens avvik om arbeidsforhold (108, 291, 297, 526, 115B) direkte i fase 1. Bare lesing av dokumentasjon.
- Hvilken ressurs bærer nye og gamle trekkbrev (`ske-korrespondanse-innkreving-utleggstrekk-virksomhet`?). Hva viser dialogen (tittel, vedlegg, strukturert innhold)? Finnes et eget brev når samordnet trekk erstatter gamle? Bruk offentlig dokumentasjon og ressursregisteret. TT02-test er ikke mulig i natt.

### N28 Samordnet utleggstrekk i detalj (fra N01)
- Nøyaktig definisjon av prosentgrunnlaget i lov eller forskrift: kontantytelser, feriepenger, naturalytelser, utgiftsgodtgjørelser.
- Når og hvordan flyttes løpende gamle bidragstrekk over i samordnet trekk (puljene P8 og P10)?

### N29 Ansvarskrav mot arbeidsgiver (fra N01)
- Hjemmel i ny innkrevingslov for ansvar ved for lite trekk. Hvordan varsler Innkrevingsmyndigheten avvik (brevressurs, frist)?

### N30 Dokumentasjonsmodellen for lønn (fra N02)
- Holder et aggregert vedlegg i regnskapet og full § 5-6-journal i Brutto etter NBS 2 punkt 4.7? Eller blir Brutto del av kundens regnskapssystem etter punkt 4.5, med krav om SAF-T-gjengivelse og 3,5 års elektronisk tilgang? Se også F-SIK-26 og F-SIK-29 (eksport ved opphør). Lag spørsmål til en revisor som et menneske kan stille.

### N31 Utlegg via integrasjon og ansattreskontro (fra N02)
- Hvem bokfører utlegget, på hvilken konto, og hvordan lukkes posten når utbetalingen går i lønn? Gjelder Utleggsappen, Tripletex reiseregning og PowerOffice utlegg. Alternativ: mellomkonto uten reskontro som Brutto avstemmer per utleggs-id (F-UTL-01).

### N32 Integrerte lønnsmoduler i praksis (fra N02)
- Hvordan fører Tripletex lønn og PowerOffice lønn nettolønn, AGA og feriepenger: samlet eller per ansatt, på 2910 eller 2930? Les struktur fra historiske bilag (bare kontoer, bilagstyper og felt, ingen persondata). Avgjør hva fase 1 leser og om postene har persondata. ReAi dekkes av N21.

### N33 Bilag til øvrige regnskapssystemer (fra N02)
- Visma eAccounting, Business NXT, Xledger og 24SevenOffice: felt for dimensjon, ansatt, vedlegg, idempotens og utkast. Ta med minste gruppestørrelse per dimensjon og hvordan Tripletex og PowerOffice skjuler lønnsbilag for brukere uten lønnstilgang.

### N34 Finansiørkrav (fra N02)
- Kan dokumentasjon av lønnskost per person per prosjekt til Forskningsrådet og EU komme fra Brutto uten ansatt i hovedboken?

### N35 Arbeidsforhold-ID i Tripletex (fra N05)
- Hvilken verdi sender Tripletex som `arbeidsforholdId` i a-meldingen: `Employment.id`, `employmentId` eller noe annet? Les dokumentasjon og API-struktur (bare lesing, ingen persondata). PowerOffice har `ReportingId`.
- Fra N21: ReAi lager ID-en ut fra virksomheten (underenhet) og den interne relasjons-ID-en når `employmentId` er `null`. Formatet er ukjent. Hva skjer når underenheten er `null` eller endres? Les struktur i ReAi (tenant 2915, bare lesing, f.eks. lagrede a-meldinger og `employmentIdOverrides`) og offentlig dokumentasjon. Ingen persondata i funnet.

### N36 Kontrollkatalog ANS-01–17 (fra N05)
- Verifiser ANS-01 til ANS-17 (natt/funn/N05.md) mot Skatteetatens feilmeldinger og veiledning for a-meldingen. Hvilke lønnsbeskrivelser krever arbeidsforhold? Hva gjelder for permittering og lønn etter slutt?
- Sett standardterskler. Lag kodelister for årsak til sluttdato, ansettelsesform og arbeidstidsordning (R1 2026).
- Yrkeskoder: hvor kommer kodelisten med 7 sifre fra, og hvordan kobles den til STYRK-08 i SSB Klass (klassifikasjon 7)?

### N37 Ansatt-API i andre systemer (fra N05)
- Visma eAccounting, Visma.net Payroll, Visma Lønn (Huldt & Lillevik), Xledger, 24SevenOffice og Uni Micro: navn, ansattnummer, fødselsnummer, arbeidsforhold-ID, underenhet og tilgangsmodell. Har Fiken en eksport av ansatte?

### N38 Navneliste-import og personvern for A07-data (fra N05)
- Mal for navneliste (CSV/Excel): felt, validering og kryptering ved opplasting. Hvordan får byrået lista fra kunden uten e-post med fødselsnumre?
- A07 per person viser fagforeningskontingent (særlig kategori), permisjonstyper og lønn. Hva lagres normalisert, hva bare rått, og hvem får se det? Innspill til DPIA (F-SIK-28, N19).

### N39 Testdata for A07 i TT02 og Tenor (fra N06)
- Finnes syntetiske Tenor-virksomheter med a-meldinger som gir data i avstemmingsrapporten i TT02? Eller må Brutto sende testmeldinger selv via filopplasting?
- Hvordan settes et testbyrå opp, slik at det er registrert som regnskapsfører for testklientene (M07, M11)? Bare offentlig dokumentasjon, ingen innlogging.

### N40 Vilkår og tilgang i grensetilfeller (fra N06 og N04, prio hevet til 1)
- Fra N04: Les Tripletex Developer Terms, Visma Developer Terms (gjelder PowerOffice) og Fikens API-vilkår. Forbyr noen av dem integrasjoner fra et konkurrerende lønnssystem? Begrensninger på lagring og bruk av data? Krav til sikkerhet?
- Formålsbegrensningen i Altinns SBS-vilkår: er lesing av A07 for avstemming mot regnskapet et «ledd i offentlig oppgaveløsning»? Gjelder vilkårene for private eller for leverandører? Lag utkast til spørsmål til servicedesk@altinn.no som et menneske sender.
- `regnskapsforer-lonn` gis bare til autoriserte regnskapsførere. Hva gjør lønnsbyråer, konsernselskaper og lokallag (M13)? Virker direkte delegering av `a-ordning` til byråets orgnr med egen agent-systembruker?
- Klientdelegering med Maskinporten-systembruker og Klientadministrator: hvordan ber leverandøren om pakken, og hvem godkjenner?
- Lav prioritet: pris og vilkår for ID-porten-klient for en privat SBS-leverandør.

### N33 tillegg (fra N21)
ReAi: godtar ReAi manuelle bilag (`POST /api/manual-vouchers`) mot 2930 og 2940 uten ansatt-id? Lukker ReAi postene på 2910 og 2930 automatisk når netto er utbetalt og utlegg refundert? Bruk ikke `salary-payments/import` (sperrer ReAis a-melding for måneden).

### N10 tillegg (fra N07)
Lag en intervjuguide for 2–3 byråer om dagens lønnsavstemming: hvilke L-kontroller (natt/funn/N07.md) gjør de, med hvilket verktøy, hvor lang tid per klient og termin, og hvordan godkjennes lønn hos kunden? Intervjuene gjøres av et menneske.

### N30 tillegg (fra N07)
Lag en intervjuguide for 2–3 revisorer: hvilke L-kontroller vektlegger de, godtar de A07 levert via Brutto eller vil de bestille selv, eksportformat, vanlige toleranser etter SA 3801, og hva testes på interim. Intervjuene gjøres av et menneske.

### N30 tillegg (fra N10)
Juridisk: teller kundens SCA i banken som attestasjon etter GRFS 8.6, slik at «Godkjenn og signer» kan erstatte egen kundegodkjenning? Hvilke formuleringer om taus aksept eller fullmakt bruker byråene i oppdragsavtalen (f.eks. standardvilkår «Betalingsoppdrag»)?

### N24 tillegg (fra N07)
SA 3801: hva krever standarden konkret for lønn, og hvordan signerer revisor kontrolloppstillingen i den nye skattemeldingen? Hvilke kontoer og terskler for naturalytelser (bil, telefon, forsikring) gir få falske positive (L-30)? Notekrav for årsverk og ytelser til ledende personer for små foretak (rskl. kap. 7), og hva kan A07 gi?

### N16 tillegg (fra N07)
OTP-plikt og minstesats: hvilke terskler i OTP-loven brukes i L-21, og hvordan ser en manglende `pensjonsinnretning` ut i A07?

### N20 tillegg (fra N07)
AGA-sone per kommune: finnes Skatteetatens sonetabell maskinlesbar, og hvordan følges kommunesammenslåinger og endringer i fribeløp i sone 1a (L-16)?

### N11 tillegg (fra N07)
Har PowerOffice og Visma.net egen A07-avstemming mot regnskap?

### N17 tillegg (fra N09, prio hevet til 2)
- ZTLs tillatelse i Finanstilsynets konsesjonsregister: PIS, AIS, pengeoverføring? Hvordan sikres klientmidler, og hva skjer ved konkurs? Hvem er avtalepart for kunden og for byrået?
- Teknisk tjenesteleverandør i norsk rett: gjelder unntaket (betalingstjenestedirektivet / finansforetaksloven) for Brutto? Merk for advokatvurdering.
- Støtter DNB og Nordea `bulk-payments` og `purposeCode` SALA for bedriftskontoer i PSD2-grensesnittet? Skjuler SpareBank 1 lønn i nettbanken ved PSD2-bulk med SALA? Har Eika-bankene eget PSD2-grensesnitt med bedriftsbulk?
- Adressekrav: hvilken adresse sendes for ansatte med fortrolig adresse når banken krever mottakeradresse? Treffer SpareBank 1s regel for logiske duplikater trekkbetalinger?
- Fra N10: Støtter partneren signering med to personer for bedriftskontoer (status PATC), og får vi vite hvem som signerte? Kan regnskapsfører signere med egen BankID på klientens konto via PIS, og gjelder bankenes regler for betalingsrett (RGB, AG08, 90 dager) også for PIS?
- Lav prioritet: Fiken via Aritma, PowerOffice `BankTransfer` (konfidensiell lønn?), status for PSD3/PSR i EU og EØS.

### N12 tillegg (fra N08)
Sky og KMS i Norge (H01): bekreft Azure Key Vault og Managed HSM i Norway East, GCP-region i Norge og Cloud KMS der, AWS-alternativ, og Postgres 18 med `btree_gist` og PgBouncer hos aktuelle leverandører. Se også EU/EØS-region for Claude.

### N13 tillegg (fra N08)
Avrundingsregler for prosenttrekk, tabelltrekk, AGA og feriepenger i forskrift og hos Skatteetaten. Lag en tabell over avrundingsstrategi per regel (rust_decimal `round()` bruker bankers avrunding).

### N14 tillegg (fra N27)
Hvor kommer påminnelser om manglende a-melding nå (`ske-vedtak-tvangsmulkt-overtredelsesgebyr`, A50/A51 i Altinn 3)? Hva er `ske-arbeidsgiverkontroll`, hva erstatter den, og når kommer den i produksjon?

### N25 tillegg (fra N27)
Migrerte Altinn 2-ressurser (gamle trekkbrev 5360, 5759, 5996 og historiske A03 3476) via Altinn Correspondence: hvilket scope (`altinn:correspondence.read`?), gir henting status «lest», og kan direktekunder få tilgang med `lonn` eller `a-ordning`? Events med agent-systembruker: virker abonnement per klient, og hvor mange tåler Altinn per byrå?

### N11 tillegg (fra N40)
Har Tripletex Lønn og PowerOffice Lønn egen avstemming av a-melding mot regnskap? (Avgjør hvor hardt konkurranseklausulen i utviklervilkårene treffer fase 1.) Hvilke eksterne lønnssystemer (Intect, Finago, SD Worx, NettLønn m.fl.) bruker i dag API-ene til Tripletex og PowerOffice for lønnsbilag, og har de tillegg til vilkårene?

### N11 tillegg (fra N21)
ReAi har ingen modell for trekkpålegg og ingen kobling til Trekkpålegg-API-et. Rapporterer ReAi utleggstrekk i a-meldingen, og hvilken konto krediteres for faste trekk etter skatt?

### N25 tillegg (fra N26)
Portveien «Brutto sender a-meldingen» for kunder med eget lønnssystem (åpner Trekkpålegg-API og tilbakemelding): juridisk ansvar, `kildesystem` i meldingen, tilbakemelding, fare for dobbel innsending, og om Tripletex, PowerOffice og Visma kan eksportere a-melding som XML.

### N27 tillegg (fra N26)
Har dialogen i `ske-korrespondanse-innkreving-utleggstrekk-virksomhet` strukturerte felt (KID, prosent, startdato) som kan fylle det manuelle trekkregisteret? Ligger `ske-trekkontroll-forskuddstrekk` («Kontroll av forskuddstrekk») i Dialogporten, og hva inneholder meldingene?

### N29 tillegg (fra N28)
Hvordan behandler Innkrevingsmyndigheten et gammelt trekk tatt på en utbetaling etter samordnet startdato når lønnen ikke kjøres på nytt? Renter på ubetalt trekk fra 1.1.2027 (innkrevingsforskriften § 31-1).

### N29 tillegg (fra N26)
Kontroller paragrafnumrene i innkrevingsloven (§§ 23, 28, 30 og 31) mot Lovdata, og § 3 i forskriften om elektronisk kommunikasjon med alminnelig namsmann og Innkrevingsmyndigheten.

### N40 tillegg (fra N23)
Kan Brutto bruke kontonavn fra SAF-T-standardkontoene (© Regnskap Norge, lisensiert for SAF-T-mapping) og NS 4102 (Standard Norge) i malen?

### N40 tillegg (fra N26)
Lav prioritet: rollekodene i policyen for Trekkpålegg-API (`loper`, `a0241`, `siskd`, `knuf`) og delegeringsplanen «Trekkpålegg API – På vegne av». Kan en systembruker få tilgang gjennom dem?

### N08 tillegg (fra N04)
Fra N36: Importør for Skatteetatens regneark (forretningsregler, kodeliste, inntektskombinasjoner), f.eks. med `calamine`, overvåking av SBS-siden for nye versjoner, og synk av SSB Klass 145, 7 og 426 (frekvens, manglende koder, `validTo`).
SAF-T 1.30-leser i Rust: strømmende parsing, filter på konto, `Analysis` som dimensjon, testfil fra Tripletex `/saft/exportSAFT`. Lagring og minimering (filen har hele hovedboken med kunder, leverandører og ansatte).

### N32 tillegg (fra N04)
Reverseringer og nettoføring: hvordan viser hvert system korrigeringer, og hvor ofte føres avsetning og utbetaling på 2940 som én linje?

### N37 tillegg (fra N11)
- Kan Tripletex, PowerOffice, Fiken, Maestro og Accountflow hente A07 med systembruker uten at noen logger inn? (Avgjør Bruttos hovedargument.)
- Hvor stor andel av byråklientene og kundene med 10–1000 ansatte har lønn og regnskap i ulike systemer? Bruk Regnskap Norges lønnsundersøkelse og andre offentlige tall.
- Hvor dype er Accountflow og Account Control i lønn (A07 per person, 2610, AGA-sone, kontrolloppstilling, pris)?

### N32 tillegg (fra N24)
Tripletex Årsoppgjør: fylles tillegg og fradrag i kontrolloppstillingen automatisk fra 2930–2949, eller alltid manuelt?

### N13 tillegg (fra N24)
Skatteplikt i 2026 for arbeidsgiverbetalt forsikring (gruppeliv, behandlingsforsikring) og grensen for skattefri gave (Skatte-ABC), før tersklene i L-30h og L-30i settes.

### N38 tillegg (fra N24)
Kobling av daglig leder og styret (roller i Enhetsregisteret med navn og fødselsdato) til A07 (fødselsnummer) for notegrunnlaget etter rskl. § 7-31: holder fødselsdato pluss navn fra regnskapssystemet, og hvordan unngås feil kobling?

### N32 tillegg (fra N11)
Visma.net Payroll: går «Avstemming av A-melding mot regnskap» mot hovedboken i ERP eller mot Payrolls egen bokføring? Henter Payroll trekkpålegg fra API?

### N37 tillegg (fra N04)
Markedsandeler: hvilke regnskapssystemer bruker målgruppen (10–1000 ansatte) og byråklientene? Avgjør rekkefølgen på adaptere etter Tripletex og PowerOffice. R2-byra fant 28/17/9/4/2 i ett byrå.

### N33 tillegg (fra N04)
Verifiser saldo, debet/kredit, grupperingskode og byråtilgang for Xledger, Business NXT og Uni Micro mot offisiell dokumentasjon. Avklar om PowerOffice krever manuell bokføring av lønnsbilag (`JournalEntryVoucher`).

### N19 tillegg (fra N38)
Rådgivers vurdering av art. 9 for fagforeningstrekk og permisjonsbeskrivelser i et avstemmingsverktøy (holder summer? er foreldrepermisjon helseopplysning?). Er en låst avstemmingsrapport regnskapsmateriale etter bokføringsloven § 13, og hvor lenge må A07 rå da lagres? Brreg rolleutskrift-API for databehandler: vilkår, formål, kall og søknadstid. Rollehistorikk med fra/til-dato i Enhetsregisteret. Bekreft mønstre for NAVs syntetiske numre og FH-nummer. Fødselsdato i fødselsnummer fra 2032.

### N19 tillegg (fra N30)
Les endringsforskriften 29.9.2026 nr. 1933 og ny § 13 i bokføringsforskriften i fulltekst: flere endringer i kap. 7 (§ 7-5, § 7-8) eller § 5-6 som treffer Brutto? Gjelder meldeplikten etter § 7-5 all lagring i EØS, også sikkerhetskopier og logg (underleverandører)? Krav til elektroniske regnskapssystemer fra 2030 (bokføringsloven § 7 fjerde ledd): treffer de forsystemer som lønn?

### N33 tillegg (fra N37)
Business NXT `Associate` (fødselsnummer, org.enhet, virksomhet, ansettelsesdatoer via `useModel`). Xledger: prismodell for GraphQL, token for byråer med mange entiteter, `Employee` med virksomhet og dimensjoner. Uni Micro: vilkår i distribusjonsavtalen og felt i `employees`/`employments`.

### N33 tillegg (fra N32)
Bilagstype og format for eksterne lønnsbilag i Tripletex (manuelt bilag eller «Lønnsbilag»; API for lønnstransaksjoner er DEPRECATED), og hva det gjør med Tripletex' avstemmingsmodul og Årsoppgjør. Periodisering i PowerOffice.

### N33 tillegg (fra N31)
- Lukker Tripletex en åpen post på 2910 når et eksternt bilag debiterer 2910 for samme ansatt og beløp? Hva skjer med `travelExpense.state`? PowerOffice Go: konto for utlegg (bilagstype 14), ansatt på bilagslinjer, kan en integrasjon lukke åpne poster per ansatt?
- Godtar Tripletex, PowerOffice, Fiken og ReAi inngående MVA på linjer i et lønnsbilag via API, og hvordan vises det i MVA-meldingen?
- Xledger og Business NXT: føres ansattes utlegg mot ansatt som leverandør, og betales de via remittering eller lønn?

### N33 tillegg (fra N30)
Hvordan tar Tripletex, PowerOffice og Fiken imot AGA-grunnlag per sone og sats i lønnsbilaget (mengdefelt, tekst eller egen linje)? SAF-T-delfil fra Brutto: kan ansatt-ID ligge i `Analysis` i SAF-T Financial 1.30, og godtar Skatteetaten en delfil fra et forsystem?

### N19 tillegg (fra N12)
KI senere: er et modellkall i EU uten lagring «oppbevaring» av regnskapsmateriale etter bokføringsloven § 7-5? Overføringsgrunnlag (er Anthropic på DPF-listen, hvilken AWS-enhet er avtalepart i EØS, mal for TIA). AI Act etter Omnibus (forordning 2026/1744, datoer for art. 50) og norsk KI-lov. Hvilke felt i A07 og a-meldingen er fritekst og kan bære prompt-injeksjon?

### N19 tillegg (fra N40)
Datadelingsforordningen (Data Act): gjelder den i Norge (EØS), og gir den kunden rett til å la en tredjepart hente data fra regnskapssystemet?

### N19 tillegg (fra N05)
Folkeregisteret «Privat virksomhet»: kan en lønnsleverandør bruke kundens rettighetspakke via delegering eller systembruker? Hva koster det?

### N25 tillegg (fra N01)
Sjekk også om API-et viser utleggstrekk skatt og innbetalinger til 7694 05 69814 for arbeidsgiveren, og finn kodelisten for `kravtype`.

### N11 tillegg (fra N01)
Sjekk om PowerOffice Go, Visma.net Payroll og SD Worx henter samordnede pålegg fra Trekkpålegg-API-et. Bare Tripletex er bekreftet.

### N07 tillegg (fra N03)
Ta med revisorbruk av A07: hvilke revisjonshandlinger gjøres på lønn og A07 (interim og år), og hva trenger revisor i en eksport?

### N07–N20
Se tittelen. Hold samme form: hva vet vi, hva er uklart, konsekvens for Brutto.
