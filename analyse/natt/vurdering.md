# Vurdering av forslagene fra nattarbeidet

Seks agenter vurderte de 531 forslagene i `natt/forslag.md` mot kartleggingen i `build/data/` (29.10.2026). Hvert forslag har fått id E001–E531 og én kategori i `natt/vurdering.json`. Ingenting i `build/data/*.json` er endret.

| Kategori | Antall | Hva skjer |
|---|---|---|
| INN | 168 | Kan legges inn uten beslutning fra Sjur. |
| SLÅ_SAMMEN | 178 | Dekket av et annet forslag eller av det som finnes. Legges inn bare én gang. |
| BLOAT | 63 | Droppes eller parkeres: implementasjonsdetaljer, salgstekst, konkurrentlister, «senere» uten følger for datamodellen. |
| PETER_SANDER | 43 | Tekniske valg. Legges som spørsmål i `fase1.json`, ikke som innhold i kartleggingen. |
| KONFLIKT | 23 | Løst nedenfor, eller del av en beslutning. |
| SJUR | 56 | Slått sammen til beslutningene nedenfor. |

Sjur trenger altså bare å ta stilling til beslutningene i del 1–3. Resten følger av dem.

## Del 1: Beslutninger som bare Sjur kan ta

### 1. Leverandørselskap og teknisk eier (E051, M01, M02)
Organisasjonsnummeret inngår i system-ID-en i Altinn. Bytter vi selskap senere, må alle kunder godkjenne på nytt. All myndighetsoppkobling venter på dette valget.
**Anbefaling:** Velg nå det selskapet som skal eie Brutto og kundeavtalene.

### 2. Hvor regnskapsdataene kommer fra (E156, E361, E169, E250, E158, E246, E087, E462)
Sjurs innspill 29.10: Vi kan avstemme mot de regnskapsdataene vi selv har sendt til postering. Det gir tre nivåer:

| Nivå | Avstemming | Datakilde | Når |
|---|---|---|---|
| 1 | A07 mot Bruttos lønnsjournal og bilag | Egne data. Ingen lesing hos andre. | Når Brutto kjører lønnen (MVP) |
| 2 | Bruttos bilag mot det som er bokført | Kvittering med bilagsnummer fra adapteren (F-REG-18), eventuelt tilbakelesing av eget bilag | MVP |
| 3 | Lønnskontoene i hovedboken mot nivå 1 og 2 | Saldo per konto fra regnskapet (SAF-T eller API) | Fase 1 og MVP |

Nivå 1 og 2 trenger ikke API-lesing hos Tripletex eller PowerOffice. Risikoen i konkurranseklausulen (N40) blir da mye mindre for kunder som kjører lønn i Brutto. Nivå 3 er likevel nødvendig av to grunner:
- Fase 1 avstemmer også når lønnen er kjørt i et annet system (F-REG-30). Da finnes det ingen egne bilag.
- Balansekontoene (2600, 2770, 2780, 2940) får posteringer som ikke kommer fra Brutto: betaling av trekk og AGA, periodiseringer, manuelle rettinger og NAV-refusjon. Det er her Finanstilsynet finner feil.

**Anbefaling:**
- Nivå 1 og 2 blir standard i MVP. Tilbakelesing av eget bilag søkes som egen, smal tilgang.
- Nivå 3 kommer fra SAF-T-opplasting i fase 1. Tripletex-lesing bygges parallelt, men går i produksjon først etter skriftlig svar på API-vilkårene.
- Klientoversikten hos byrået viser A07-data fritt. Regnskapsdata vises der først via SAF-T eller etter skriftlig godkjenning.
- ReAi og Huma kommer bare hvis en pilotkunde trenger dem.

### 3. Kontrollene i første utgave av fase 1 (E190, E191, P05)
To agenter foreslo ulike lister. Felles for begge er L-01, L-03, L-05, L-06, L-12, L-13, L-17 og L-24. Bare én av listene har L-25, L-02, L-14, L-07 og L-26.
**Anbefaling:** L-katalogen blir datamodellen. Første utgave får høyst 12 kontroller: de åtte felles, pluss L-02 og L-14 hvis A03 kan leses (beslutning 4), ellers L-25 og L-26. L-16 og L-32g vises bare som indikasjon.

### 4. Hva skal med i fase 1 (som Bør)
| Tema | Anbefaling | Id-er |
|---|---|---|
| Dialogporten-sensor og A03 | Ja, bare polling og metadata. Forutsetter at TT02 bekrefter at A03 kan leses når et annet system har sendt a-meldingen. Ellers MVP. | E173, E179, E183 |
| Kontrolloppstilling som arbeidspapir | Ja | E272 |
| Smalt revisorutdrag og lett systembeskrivelse | Ja | E194, E321 |
| Godkjenning | Kvittering i ett ledd med hash. Den som kvitterer et avvik, kan ikke kontrollere pakken. Små byråer kan få unntak med begrunnelse. | E233, E238 |
| Navneliste og kobling | Navnelisteimport og permisjon som A07-kopi. Automatisk kobling bare på eksakt fødselsnummer. Navn og fødselsdato gir bare et forslag. Fullt kilderegister kommer i MVP. | E044, E371, E103, E362 |
| Modus «Avstemming» uten inntektsmottakere | Tilgjengelig som valg. Standard er «Ansattoversikt». | E376 |

**Ikke i fase 1:** manuelt trekkregister (E098, kommer i MVP, se beslutning 6), T9 (E301), K27 for direktekunder (E434), åpne poster på 2910 (E333), kontonummer og L-31 (E042, E196) og kjønn i grafer (E047).

### 5. Regnskapsfaglige standarder (E086, E011, E453, E357)
- Nettolønn føres samlet på 2930 som standard. Netto per ansatt er bare et tilvalg der regnskapssystemet krever det.
- Underkontoene 2611–2613 for trekk er en valgfri, finere mapping. 2610 og 2620 forblir standard.
- OTP-premien føres på 5950 i stedet for 5420, når grupperingskoden for AS er avklart.
- AGA-fradraget for NAV-refusjon følger `aga_refusjonsmetode`.

### 6. Trekk (E015, E427, E308, E098)
- **Besluttet av Sjur 29.10:** Trekkpålegg registreres manuelt på ansattkortet fra start (MVP), med `kilde` = manuell. Trekkpålegg-API-et åpner først når kunden har sendt minst én a-melding gjennom Brutto (N26). Da sammenlignes det manuelle registeret med API-et.
- **Besluttet av Sjur 29.10:** Ved SAF-T-import av historisk lønnsgrunnlag flagger Brutto bevegelser på trekkontoene (via kontomappingen) som tegn på aktive trekk. Flagget sammenlignes med `utleggstrekk[]` i A07 og med manuelt registrerte pålegg.
- Nytt trekkpålegg etter beregning gir et varsel. Nytt skattekort blokkerer fortsatt.
- Tillegg som utbetales med lønnen, får halvt trekk etter § 5-7-2 fjerde ledd. Reglene om 21 % og 12,3 % i juni tas inn.
- Foreløpige regler for samordnet trekk: ingen fremføring, nedrunding til hel krone og trekk så tidlig som mulig. Alle merkes [verifiseres] til Skatteetaten har svart.

### 7. Lønnsfaglig (E135, E136)
- Lønnsbeskrivelser etter sluttdato følger N36 §4 som standard. Unntak gir et infovarsel og krever kvittering.
- Årsverk regnes uten tilkallingsvikarer og arbeidsforhold på 0 %, som snitt per måned. Definisjonen står i rapporten.

### 8. Pris for fase 1 (E252)
**Anbefaling:** Pris per klient per måned, med 15–87 kr som anker og påslag for kontroll per person. Prisen testes i intervjuene.

### 9. Begreper for faser (B31)
«MVP» er ikke en vedtatt fase. CLAUDE.md kaller fase 1 «MVP nivå 1», `fase1.json` kaller lønnskjøring «fase 2», og forslagene sier «MVP».
**Anbefaling:** Bestem ett sett navn, for eksempel Fase 1 (avstemming) og Fase 2 (lønnskjøring = MVP), og legg det inn som beslutning.

## Del 2: Pakker Sjur kan godkjenne samlet

**Tilgang og myndigheter**
- Direktekunder gir `a-ordning` og `lonn` fra start. Dette løser konflikten mellom F-MYN-02 og F-MYN-03 og presiserer S #16 (E054, E062, E180, E489).
- Formålsspørsmålet sendes til Altinn/Digdir før SBS-vilkårene godtas. `events.subscribe` strykes fra søknadslisten fordi scopet er offentlig (E164, E053).
- Tidsanslaget for myndighetsoppkoblingen er 3–5 måneder. 7–10 uker er beste tilfelle (E064).
- Byråer uten REGN og rene lønnsbyråer er ikke målgruppe i fase 1. Datamodellen skal likevel tåle dem (E165, E167).

**Senere faser**
- Krav og betalinger løftes fra Kan til Bør for kunder som sender a-melding via Brutto (E292).
- Første KI-bruk er F-MIG-13: bare metadata, og bare når kunden slår det på (E270).
- Tariff: bare Virke HUK kuratert. Alt annet via import (E503).
- KLP-filen bygges bare hvis en pilotkunde har offentlig ordning (E461).

**Nye beslutninger med status Forslag** (verifiseres med 2–3 revisorer)
- Dokumentasjonsmodell A: samlebilag i regnskapet og full journal i Brutto (E318).
- Brutto er underreskontroen for prosjektlønn (E523).
- Den som utbetaler, bokfører. Utlegg følger flyt B som standard (E336).

**Rettinger fra konfliktene**
- Løftet blir «hentet etter fristen og ved hver endring», ikke «hver natt» (E243).
- OTP-differanser får eget kodeprefiks (A07-O1–O3), fordi A07-P er brukt (E455).
- Bank leses bare med motkonto 5800 eller 1579x (E442).
- D-Trekkpalegg revideres samlet i én runde (E019).
- A-meldingsfeltene blir værende på den versjonerte lønnsarten (E412).
- Målbildet «ReAi betaler automatisk» strykes (E094).
- Fødselsdato lagres ikke i fase 1. Aldersgruppe utledes av fødselsnummer (E385, E047).
- Huma er kilde for navn når den er koblet til, ellers regnskapet (E464).
- F-BYR-15 lover ikke lenger trekkpålegg i fase 1 (E098).

## Del 3: Én samlet advokatvurdering

Disse spørsmålene samles i én bestilling:
- API-vilkår og konkurranseklausul hos Tripletex og PowerOffice (E169, E250, E158). Sjurs nivå 1–2 gjør spørsmålet smalere.
- ZTL med klientkonto mot B12, og førstelinjesupport som agentrolle (E232, E387).
- Kundeavtale med begrenset dekning for et kontrollverktøy (E492).
- DPA med modell A som standard og KI av som standard (E470).
- Oppbevaring: A07 rå i 13 måneder, låst rapport med sumutdrag og hash i 60 måneder (E476, E382).
- Fullmakt og «godkjenn og signer» (E323, E329).
- Byråenes egenerklæring om autorisasjon (E167).
- Rolleinnehavere fra Brreg (E383).
- Partneravtale med Huma (E469).

## Del 4: Til Peter og Sander

43 forslag er tekniske valg (`kategori = PETER_SANDER` i `vurdering.json`). De legges inn som spørsmål i `fase1.json`, blant annet om `f64` i trekkrutinen mot D05 (E422) og om pengerepresentasjon (E493).
