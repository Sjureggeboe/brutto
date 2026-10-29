# S – Avklaringer fra Sally-arbeidet som gjelder Brutto

Kilde: avklaringene (A-tabellen) og spørsmålslisten i Sally-roadmapen brukeren deltok i. **Sally og Brutto er separate produkter uten kobling** (avklart av brukeren 28.10.2026). Bare fagavklaringer om lønn, myndigheter, oppbevaring, personvern og sikkerhet gjenbrukes. Sallys arkitektur, stack, id-er og Tally-kontrakt gjelder ikke. Sally-referansen står i parentes for sporbarhet. Punkter merket **(Sjur)** er brukerens egne lønnsfaglige vedtak. Punkter merket «antatt» må verifiseres.

## 1. Oppbevaring og lagringssted
1. **Oppbevaringstid:** Regnskapsmateriale, inkludert lønnsbilag og lønnsdokumentasjon, oppbevares i fem år etter regnskapsårets slutt og slettes ikke før. Bokføringsloven § 13 endres 1.1.2027, men uten nye frister (Sally A80, A99, spm. 37).
2. **Dokumentér per lager:** Hver datalagring har formål, eier, oppbevaringstid og slettedato i et eget compliance-dokument (Sally spm. 37, A48).
3. **Logger** (revisjonslogg, tilgangslogg, hemmelighetslogg) oppbevares like lenge som regnskapsmaterialet (Sally spm. 37, A80).
4. **Lagring utenfor Norge krever melding:** Lagres regnskapsmateriale i et annet EØS-land, for eksempel Sverige eller Tyskland (også backup), må **hver bokføringspliktig** sende skriftlig melding til skattekontoret etter bokføringsforskriften § 7-5. Søknad har ikke vært nødvendig siden 27.1.2025. Meldingen sier hva som lagres, hvor (selskap og serveradresse) og hvordan myndighetene får tilgang fra Norge. Ny melding kreves når lagringsstedet endres. Plikten ligger hos kunden også når en SaaS-leverandør lagrer dataene (Sally A99, A128, A137, spm. 92).
   **Konsekvens for Brutto:** Ligger både primærdata og backup i Norge, slipper hver kunde og hvert byrå denne meldingen. Det er et konkret salgsargument og styrker B9. Velger vi DR eller backup i EU, må Brutto levere malmelding og en prosess, og byrået må sende for hver klient.
5. **Sikkerhetskopi** (bokføringsforskriften § 7-2): daglig kopi pluss en ekstra kryptert nattkopi i en annen lokasjon, nattkopier i 35 dager, månedskopier i 13 måneder, manifester i fem år og en årlig gjenopprettingstest. Nøkkelkopi lagres separat med navngitt tilgang (Sally A137, A132).

## 2. Personvern og kryptering av lønnsdata
6. **Fødselsnummer og kontonummer krypteres**, og all lesing logges. Lønnsbeløp vernes med egen lønnstilgang og logget lesing, men krypteres ikke, slik at kontrollene i databasen kan lese dem (Sally A10, A44).
7. **Helse- og fagforeningsopplysninger som kan leses ut av lønnsdata, regnes som lønnsdata** og får samme vern. Det gjelder sykepengelønnsarter, fagforeningstrekk og NAV-dokumenter. En rådgiver vurderer løsningen opp mot GDPR art. 9 før drift (Sally A45, spm. 61).
8. **Hva er sensitivt i regnskapet:** 5800-serien (refusjon av sykepenger) er en helseopplysning og skjermes. Kontoene i 5000-serien, for AGA og for forskuddstrekk regnes ikke som sensitive i seg selv. Lønnsdata er selve lønnsbilaget og posteringene mot ansattes reskontro (Sally A84, spm. 66).
9. **Nettolønn per ansatt skal ikke synes i hovedbok eller bank uten lønnstilgang.** Nettolønnen posteres og gjøres opp samlet per kjøring (konto 2930), og bankposter for lønn krever lønnstilgang (Sally A46).
10. **Ekte data** leses bare av godkjente jobber med logg som kun har antall og feilkoder. Utvikling og test bruker syntetiske data (Sally A48, A80).

## 3. KI og agenter
11. **Lønnsdata går ikke til språkmodell via MCP i første versjon** (Sally A25).
12. **Modellsamtaler om lønn vernes som lønnsdata:** inndata og utdata krypteres og krever lønnstilgang. Resultatlogger har bare antall, statuskoder og id-er (Sally A33).
13. **Data fra Skatteetaten, Altinn og NAV brukes aldri til læring eller aggregater** (Sally A43).
14. **Agenter kan hente og validere hos myndighetene, men ikke bestille skattekort eller sende inn.** Innsending krever en navngitt godkjenner, og nyttelasten låses med hash til den er sendt (Sally A9, A32, A28).
15. **Betaling, innsending, fullmakt og samtykke er ikke tilgjengelig for agenter** i første versjon (Sally A24).

## 4. Myndigheter og systembruker
16. **Én systembruker per opplysningspliktig med alle tilgangspakkene.** Lønns- og NAV-pakkene legges til ved første planlagte utbetaling, også når det bare er styrehonorar (Sally A35, A95, spm. 81).
17. **Feil mot myndighetene blir saker etter faste regler**, for eksempel manglende systembruker, 401 og avvisning, og havner i en kontrollkø med eier (Sally A37).
18. **Felles innsendingslogg** for alle innsendinger (a-melding, inntektsmelding) med godkjenner, hash og kvittering (Sally A8, A9).
19. **I byråkontekst sender den som utfører oppdraget a-meldingen.** Godkjenning fra oppdragsansvarlig kreves ikke (Sally A92). Må sjekkes mot GRFS-kravene i E-byra.md.
20. **Bytte av lønnssystem:** arbeidsforhold-ID og startdato beholdes (Sally A95). Dette stemmer med Skatteetatens «metode 1» i A-marked §7.1.
21. **Alle frister har samme format:** type, referanse, periode, forfallsdato, kilde og regel (Sally A38).

## 5. Betaling og avstemming
22. **Forskuddstrekket betales sammen med lønnen**, med KID som beregnes i systemet (Sally oppga kravtype 05, verifiseres mot B-myndigheter §4). **AGA legges til betaling først når lønnen er avstemt**, det vil si når a-melding, pensjon, feriepenger og trekk er avstemt mot hovedboken og 2600 går i null (Sally A94).
23. **Banken starter med filer.** Kunden signerer i nettbanken, og systemet flytter aldri penger selv (Sally A78, A86).
24. **Den som verifiserte en ny mottakerkonto, kan ikke godkjenne den første betalingen til kontoen** (Sally A62). Det støtter kontonummer-skjoldet.

## 6. Lønnsarter og kontering (Sjur)
25. **Lønnsartkatalog (Sjur):** Hele katalogen finnes, med et standardutvalg på 26 lønnsarter i Tripletex-nummerering: 1000–1002, 2000, 2001, 2002, 2015–2017, 2018, 2019, 2020, 2028, 3008, 3009, 3012, 3016, 5500, 5501, 5514, 6000, 6001, 6002, 6003, 6008 og 6011. Sykelønn er 2018 og 2019, og utlegg er 1000 «Gjeld til ansatte». Standardkontoene kommer fra Sjurs A07-mapping og kan konfigureres per kunde (Sally A129, A93).
26. **Modell for lønnsart (Sjur):** En lønnsart er en linje på lønnsslippen. Den har nummer, a-meldingskode, flagg for skatt, AGA, feriepenger og sykepenger, og én debet- og én kreditkonto. Lønnsarten har ingen grupperingskode. Grupperingskoden ligger på kontoen (Sally A141).
27. **Standardkontering (Sjur):**

    | Post | Konto |
    |---|---|
    | 2000 Fastlønn | 5000 |
    | 2020 Styrehonorar | 5011 |
    | Feriepenger 2015–2017 | 2940 |
    | 3012 Gruppelivsforsikring | 5250 mot 5290 |
    | Kost 5500/5501 | 7150 |
    | 5514 Kilometergodtgjørelse | 7100 |
    | Skattetrekk 6000 | 2600 |
    | Utleggstrekk 6001/6002/6011 | 2610 |
    | Bidragstrekk 6003 | 2620 |
    | Pensjonstrekk 6008 | 2690 |
    | Fagforening | 2650 |
    | Ulykkesforsikring | 5252 |
    | Helseforsikring | 5280 |
    | Forskudd på lønn og reiseforskudd | 2910, omklassifiseres ved årsslutt til 1572 og 1570 |
    | Netto lønn, samlet per kjøring | 2930 |
    | AGA | 5400/2770 |
    | Avsetning feriepenger | 5020/2940 |
    | AGA av feriepenger | 5405/2785 |

    Lønnsarter utenfor utvalget får konto etter gruppen sin (Sally A141).
28. **Grupperingskoder (Sjur):**
    - 5011 → 5000
    - 5800 → 5000 (antatt)
    - 7100 og 7150 (opplysningspliktig) → 7155
    - 7140 (ikke opplysningspliktig) → 7165
    - 2940 → 2949
    - alle trekkontoer 2600–2690 → 2600
    - forsikringskontoene 5250/5252/5280/5390 → 5000 (antatt)
    - 1570/1572 → 1570

    (Sally A145)
29. **OTP (Sjur):** Premien føres fra fakturaen fra pensjonsleverandøren, ikke i lønnskjøringen. Posteringen er 5420 Pensjonskostnad og 2690 for ansattes andel mot 2400 Leverandørgjeld. Lønnskjøringen lager ingen pensjonsavsetning. Premien skal likevel rapporteres i a-meldingen, og det beregnes AGA av den (antatt). Lønnsmodulen trenger derfor premiebeløpet per termin, men fører det ikke (Sally A153).
30. **Utleggs- og bidragstrekk fra start**, med egne kontoer atskilt fra utleggstrekk til skatt (Sally A93, A129).

## 7. Åpne punkter fra Sally som også er åpne for Brutto
- Hvem sender meldingen om lagring i utlandet, og hvordan ser malen ut (Sally A128). Bortfaller hvis alt lagres i Norge.
- Rådgiver for vurdering av helse- og fagforeningsopplysninger etter GDPR art. 9 (Sally spm. 61).
- Om personlige kontonumre i bank- og kontaktdata også skal krypteres (Sally spm. 60).
- Hvordan OTP-premien kommer inn i lønnsmodulen for a-melding og AGA (Sally A153).
- KID-kravtype for forskuddstrekk og om AGA av OTP-premie stemmer (antatt).
