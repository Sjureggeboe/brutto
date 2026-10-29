# Morgensammendrag – nattarbeid 28.–29.10.2026

Natten ga 39 ferdige punkter og 1 utsatt (N22, tester i TT02). Backloggen nådde taket på 40 punkter, så loopen stoppet kl. 05:05. Alle funn ligger i `natt/funn/`, alle forslag til endringer og spørsmål i `natt/forslag.md`, og hendelsene i `natt/logg.md`. Ingenting i `build/data/*.json` er endret.

ReAi (tenant 2915): Ett lønnsutkast og én trekklinje ble opprettet og slettet (N21). Ingenting ble postert eller sendt. Bivirkning: utkastet brukte kjøringsnummer 2026-1, så neste ekte kjøring kan få 2026-2.

## De viktigste funnene

1. **Konkurranseklausul hos Tripletex og PowerOffice (N40, N11).** Begge forbyr bruk av API-et til å utvikle et konkurrerende produkt, krever godkjenning for «dashboarding» og aggregering på tvers av kunder, og kan si opp på 30 dager. Tripletex krever samtykke før KI brukes på dataene. Risikoen er middels til høy fordi begge selger egne avstemmingsmoduler. Begge har likevel godkjent tredjeparts avstemmingsverktøy (Accountflow, Account Control, Sticos, Maestro). Forslag: SAF-T-opplasting fra kunden blir første kilde i fase 1, adapterne bygges parallelt, men går ikke i produksjon før skriftlig svar og advokatvurdering.

2. **Hullet i markedet er reelt (N11, N37).** Tripletex, PowerOffice og Fiken avstemmer A07 mot hovedbok bare når lønn og regnskap er i deres eget system, og krever innlogging eller klikk per henting. Ingen kontrollerer per person mot regnskapet eller AGA-sone mot adresse. Løftet bør være: «alle klienter hentet og avstemt i natt, og på nytt ved endring, uansett system, ned på person». Accountflow er nærmeste konkurrent, men tynn i lønn. Prisanker: 15–87 kr per klient per måned.

3. **A07 er ryggraden i fase 1, men gir ikke navn (N03, N05, N35).** Avstemmingsrapport-API-et gir arbeidsforhold, inntekt, trekk og AGA-grunnlag, men ikke navn eller feriepengegrunnlag. Skatteetatens arbeidsforhold-API og Aa-registeret er stengt for oss. Navn kommer fra regnskapssystemet eller en navneliste via BankID-lenke. Tripletex viser ikke rapportert arbeidsforhold-ID; PowerOffice har `ReportingId`. Koblingsregel i fire trinn.

4. **Tilbakemeldingen (A03) kan trolig leses i fase 1 (N27).** Også for a-meldinger sendt fra andre systemer, via Dialogporten, uten nye scopes. Det gir Skatteetatens avvik om arbeidsforhold direkte. Men enkeltrettigheten vi foreslo for direktekunder gir bare A07, så direktekunder bør gi `a-ordning` og `lonn`. Må bekreftes i TT02.

5. **Trekkpålegg-API krever a-melding sendt gjennom Brutto (N26, N01, N28, N29).** Fase 1 bygger på plan B: trekk fra A07, varsel om trekkbrev via Dialogporten og et lett manuelt trekkregister. Samordnet trekk gjelder foreløpig bare noen i Nord-Norge, og gamle trekk løper til 2029. Arbeidsgiver har objektivt ansvar for trukket, men ikke betalt trekk, og fra 1.1.2027 løper rente. T5 (ubetalt trekk) blir kritisk per forfallsdato.

6. **Leverandørveien tar 7–10 uker fra orgnr og er gratis (N06, N39, N25).** Velg leverandørselskap nå: orgnr inngår i system-ID-en i Altinn, og et bytte krever ny godkjenning hos alle kunder. Bruttos orgnr må trolig leses inn i TT02 (e-post til Altinn i uke 1). TT02 har ingen ferdige A07-testdata, så vi trenger en liten generator for syntetiske a-meldinger. Krav og betalinger og «Brutto sender a-meldingen for andre» passer ikke i fase 1; portveien bør strykes fra MVP.

7. **Regnskapsføringen holder, men Tripletex fører annerledes (N02, N30, N32, N33).** Samlebilag per kjøring med full lønnsjournal i Brutto holder etter NBS 2 punkt 4.7, så lenge AGA per sone og sats står i bilaget. Men Tripletex Lønn fører netto per ansatt på 2910 (ikke 2930), med ansatt på nesten alle linjer, og 17 % av lønnsbilagene er reverseringer. Saldomotoren må fjerne reverseringspar, og posteringer leses bare aggregert. Bare Tripletex, PowerOffice og Xledger har idempotensnøkkel for bilag.

8. **Kontrollkatalogene er klare til vurdering (N07, N23, N36, N16, N15, N24).** L-01–L-32 (byrå og revisor), ANS-01–20 (ansattoversikt), T1–T10 (trekk), L-21a–j (OTP), L-22a–h (NAV-refusjon) og en A07-mapping med 280 regler. Kontrolloppstillingen (tidl. RF-1022) kan ikke sendes alene, men Brutto kan lage arbeidspapiret med Skatteetatens feltnavn og forklarte differanser. Finanstilsynet finner mangelfull avstemming av balansekontoer igjen og igjen; det er salgsargumentet.

9. **Utbetaling: ingen ren PSD2-bulk i dag (N09, N17).** ZTL (brukt av Tripletex og ReAi) er betalingsforetak med full tillatelse, men lønnen går via klientkonto, og vilkårene sier ingenting om sikring ved konkurs. Anbefaling: pain.001-fil som grunnmur, ZTL som første partner etter gjennomgang, og to godkjenningslag (Brutto med hash og fire øyne, så signering i banken). Ingen av ni konkurrenter krever fire øyne på lønnskjøringen (N10).

10. **Personvern, KI og sky (N12, N19, N38).** Claude i EU går bare via AWS Bedrock (Opus/Sonnet/Haiku 5.5) og Google; Fable 5.1 passer ikke for lønnsdata. Azure Norway East har Key Vault, Managed HSM og Postgres 18. Kunden må trolig lage DPIA; Brutto leverer referanse-DPIA. DPA på EUs standardklausuler, med direkte avtale kunde–Brutto som standard. Fase 1 bygger ingen KI, men dataklasse per felt, agentgrenser og KI-samtykke må på plass nå.

## Anbefalte endringer i kartleggingen (utvalg, alle står i forslag.md)

- **F-REG-30 / F-REG-02 / F-REG-03:** Regel per konto med saldotype (D-A07Gruppe, D-A07Kontoregel), ikke 1:1-mapping. Rett «feriepengegrunnlag mot 2940» (A07 har ikke grunnlaget). Rett N23: 2945 er periodisering i Tripletex, legg til 5401 og 2771, AGA-regel minus refusjon, 5390 → 5300 (S #28).
- **F-REG-29:** SAF-T 1.30/1.40 som første kilde. Saldo per konto som standard; posteringer bare aggregert; reverseringspar fjernes i saldomotoren; posteringsdato, ikke bilagsdato.
- **F-BYR-15 / F-MYN-28:** Trekkpålegg flyttes fra fase 1 til MVP. Lett manuelt trekkregister (D-Trekkpalegg med `innhentet_fra`) som Bør i fase 1.
- **F-MYN-02:** Direktekunder gir `a-ordning` + `lonn`, ikke bare enkeltrettigheten for avstemming.
- **F-PER-24:** Yrkeskoden valideres mot SSB Klass 145 (STYRK-98), ikke STYRK-08.
- **F-TRK-12:** Tillegg utbetalt med lønnen omfattes av halvt trekk. **F-REG-15:** Refusjonsfordring på 1579, ikke 1580/1570. **F-PEN-06 / GC-17:** AGA på pensjonspremie følger betalingsmåneden og fordeles på soner som øvrige ytelser. **F-LON-19:** Statens A-tabell er borte fra 2024.
- **F-UTL-18:** Utlegg utenfor lønn bare for rene refusjoner; trekkfri km og kost skal i a-meldingen.
- **Nye funksjoner:** Kontrolloppstilling med signering; Dialogporten-sensor (F-MYN-43); Leverandøravtaler og tilgangsregister; Innhenting av navneliste via lenke; Dataklasse per felt i API-et; Kontrollsporbeskrivelse per kunde og år; F-TRK-29 Trekkdokumentasjon og aktsomhetslogg; Syntetisk a-meldingsgenerator (internt).
- **Nye entiteter (utvalg):** D-Regnskapssaldo, D-Hovedbokslinje, D-Feltkilde, D-Feltkonflikt, D-Arbeidsforholdkobling, D-Banksignering, D-Banksamtykke, D-Partnerkunde, D-Skattekrav, D-Skatteinnbetaling, D-NavRapport, D-Trekkperiode, D-Rolleinnehaver, D-Sonedel, D-Tariffpakke, D-Kontrolloppsett.
- **Bilagskontrakt:** Kjøringsreferanse ≤ 20 tegn. Netto, MVA og brutto per linje. «Slå opp før skriv» der systemet mangler nøkkel. Aldri «Lønnsbilag» som bilagstype i Tripletex.
- **Oppbevaring:** Låst avstemmingsrapport 5 år med sumutdrag og hash; A07 rå 13 måneder; prosjektdokumentasjon 10 år etter prosjektslutt.

## Spørsmål og beslutninger til Sjur

1. **Velg leverandørselskap (M02) og teknisk eier med reserve (M01).** Alt annet på myndighetssiden venter på dette.
2. **Bestill én samlet advokatvurdering:** API-vilkår hos Tripletex, Visma/PowerOffice og Fiken (N40, N11), Humas vilkår (N18), Bruttos rolle overfor ZTL (N17), «Godkjenn og signer» og forhåndsgodkjenning (N30), DPA-modell og art. 9 (N19), ansvarsfordeling ved feil trekk (N29).
3. **Godkjenn utsendelse av henvendelser** (utkast i funnene): Skatteetaten (N26 §8 med tillegg fra N25, N27, N28, N29, N36, N37), Tripletex og PowerOffice (N40), Altinn servicedesk (formål og orgnr i TT02, N40, N39), ZTL (N17), NAV (N15), Huma (N18), Finans Norge (N16), Brreg (N19), Utleggsappen (N31), ReAi (N21, N35).
4. **OTP-konto (S #29):** 5950 (SAF-T) eller kundens egen konto i stedet for 5420? Og bekreft rettingen 5390 → 5300 i S #28.
5. **Godkjenn nedlastinger:** Skatteetatens tabellfil for trekk (5,6 MB, N13) og Vismas PDF om Payroll Extension (1,3 MB, N32). Godkjenn også at det spørres om lisens for trekkrutinen.
6. **ReAi-test (N33):** Vil du gi ja til et manuelt bilag mot 2930/2940 uten ansatt-id i tenant 2915, med sletting etterpå?
7. **Lønnsfaglig:** Hvilke lønnsbeskrivelser kan komme etter sluttdato (N36)? Støttekontakter og avlastere: ansatt eller frilanser? Hvordan regnes årsverk i noten (N24)? Varamedlemmer i § 7-31 (N38)? Skattetrekk betalt fra lønnsbilaget i 2026 (N32)?
8. **Intervjuer:** 2–3 byråer (guide i N10 §7) og 2–3 revisorer (guide i N30 §5) før MVP-planen låses.

## Spørsmål til Peter og Sander

1. **Sky og nøkler:** Azure Norway East med Key Vault Premium i fase 1, og Postgres 18 Flexible (ikke Burstable)? Egen JWS-bygger med KMS-signering for Maskinporten (N08, N12)?
2. **Penger i Rust:** `rust_decimal` med forbud mot `round()`, `arbitrary_precision` i hele workspace, og `f64` bare i en isolert `brutto-trekkrutine`-crate med 100 % treff mot Skatteetatens tabellfil (N08, N13)?
3. **Jobbkø:** Egen Postgres-kø med én aktiv bestilling per opplysningspliktig og felles token-bøtte per system og legitimasjon, eller `graphile_worker`? Kan den hente A07 for 500 klienter per natt (N03, N08, N11)?
4. **Datamodell:** Tre lag (rå, observasjon, sammenstilt) med kilde per felt i fase 1? Rådata kryptert som `bytea`, kontroller bare på normalisert lag? Aldri D-Hovedbokslinje for 5xxx og 29xx (N05, N08, N32)?
5. **Saldomotor og kontroller:** Reverseringspar i motoren med felles felt fra alle adaptere? Kontroller som kode med `datakrav`, versjon og ansvarsrisiko som metadata (N07, N29, N32)?
6. **Godkjenningsmotor:** Én tilstandsmaskin med hash og tre spor (betaling, a-melding, bokføring), tatt i bruk allerede i fase 1 på avstemmingspakken (N10)?
7. **Integrasjoner:** Én felles Dialogporten-sensor med polling som aldri åpner enkeltdialoger (N27)? Felles trait for regnskap og egen `AnsattKilde` (N04, N37)?
8. **Tidslinje:** Hvilken lanseringsdato for MVP? A-melding 2.4 gjelder fra 2028-01, med testmiljø 15.09.2027 (N14). Hvem kjører testplanen i N22 når Maskinporten-klienten finnes?
