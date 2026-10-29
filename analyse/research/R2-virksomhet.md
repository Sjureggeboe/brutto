# R2 – Behovskartlegging: virksomhetskunden (direkte kunde)

**Runde 2 av behovskartleggingen** · Produkt: **Brutto** · Dato: 28. oktober 2026 · Grunnlag: rapportene A–G fra runde 1 (særlig D-praksis) + målrettede søk · Status: revidert etter egen kritikkrunde (runde B), med to nye krav fra gründeren lagt inn etterpå (egne moduler for ferie/fravær, timer og utlegg, og integrasjon med Huma som Brutto på sikt skal erstatte)

> **Lesenøkkel**
> - Kildehenvisninger peker til runde 1-rapportene, for eksempel **[D 11.2]** = D-praksis, avsnitt 11.2. Primærkildene (URL-er) står i de rapportene.
> - **MoSCoW:** **Må** = uten dette signerer ikke kunden eller kan ikke gå live. **Bør** = viktig for å vinne og beholde kunden, bør komme innen 6–12 måneder etter første kunde. **Kan** = differensierende når grunnmuren står. **Ikke nå** = bevisst utsatt.
> - Segmentmerking: «(HUK)» = kunder med Virke HUK eller lignende offentlig-lik tariff og pensjon, «(250+)» = kunder med 250 ansatte eller flere.
> - Behov-ID-er: **VK-01–VK-84** = lønn og plattform, **VK-M/F/T/U** = de egne modulene for ferie/fravær, timer og utlegg (kap. 5), **VK-H** = HR og Huma (kap. 2.4.1).
> - Alle tall for tidsbruk og baseline er **anslag** fra D-rapporten, ikke målinger. De må verifiseres hos pilotkundene.
> - Modulene er tolket slik oppdragsgiver beskriver dem: **Utleggsappen** = utlegg og reiseregning, **OrgLab** = medlemshåndtering for organisasjoner, **Tikket** = billett og arrangement. NB: G-rapporten brukte OrgLab som eksempel på en HR-modul og Tikket som eksempel på en tidsmodul [G, innledning]. Kontraktene B2 og B3 i G må derfor skrives om (se kap. 4).

---

## Innhold

0. Sammendrag
1. Personas på én side
2. Personas i dybden
   - 2.1 Lønnsansvarlig i stiftelse (400 ansatte)
   - 2.2 Lønnsmedarbeider i AS (150 ansatte, turnus, flere AGA-soner)
   - 2.3 Økonomisjef/CFO
   - 2.4 HR-sjef
     - 2.4.1 HR i Huma i dag, og hva som skal til for å samle HR og lønn i Brutto (nytt krav)
   - 2.5 Ekstern revisor
   - 2.6 Liten virksomhet (10–25 ansatte) der daglig leder kjører lønn
3. Tverrgående behov og behov for skala (lagt til i runde B)
4. Modulene: Utleggsappen, OrgLab og Tikket sett fra virksomhetskunden
5. Egne moduler for ferie/fravær, timer og utlegg (nytt krav)
6. Hva jeg endret i runde B, og tillegg etter runde B
7. Topp 20 tverrgående behov, rangert
8. Ti øyeblikk i lønnsmåneden der vi kan vinne kunden
9. Det vi bevisst IKKE skal bygge for dette segmentet
10. Åpne spørsmål til runde 3
11. Kilder

---

## 0. Sammendrag

1. **Kunden kjøper ikke en lønnsmotor, men en kontrollert flyt.** Tiden i en lønnsmåned går til innhenting og purring (30–40 %), kontroll og avviksanalyse (25–35 %) og korrigeringer (10–15 %), ikke til beregningen [D 1.4]. Behovene som skiller oss fra andre, ligger i disse fasene.
2. **Retro er den største enkeltsmerten og det tydeligste angrepspunktet mot Visma Payroll** [D 2.2, D 8.1, A 6.1]. I fortellingen om en stiftelse med 400 ansatte gikk ca. 58 av 280 timer i november til etterbetaling [D 11.3]. Et førsteklasses retro må også ta med følgevirkningene: tillegg som avhenger av timelønn, sluttede, korrigert inntektsmelding til NAV og pensjonsgrunnlag til KLP.
3. **2026-reglene gjør økonomisjefen til en hovedperson.** Forskuddstrekk og utleggstrekk betales nå ved hver lønnskjøring med KID og forfall første virkedag etter utbetaling [B 4, D 0.4]. Attestasjon, betaling og avstemming må derfor henge sammen i én flyt med sporbarhet.
4. **Importen er der de store feilene skjer.** Kristiansand kommune ga 2 338 ansatte feil tillegg på grunn av feil mapping mellom tid og lønn [D 4.4]. Nye lønnskoder skal i karantene og testes før de brukes.
5. **Revisor og økonomisjef har vetorett i praksis.** Endringslogg, fire øyne, håndhevet arbeidsdeling (SoD), revisorpakke og en ISAE 3402-plan er salgskrav fra ca. 250 ansatte [D 4, F 4.1].
6. **Migrering og support er reelle behov, ikke prosjektdetaljer.** Lønnssjefen har mer å tape enn å vinne på et bytte [A 6.2]. Uten migrering der alt blir likt på øret, parallellkjøring og lønnsfaglig support i lønnsvinduet blir det ikke noe salg [F 6.5, A 6.2].
7. **Stiftelser og organisasjoner har særbehov vi kan vinne på:** Virke HUK-stiger, KLP, lønn fordelt på prosjekter og finansiører, honorarer og styrehonorar [D 7, D 6.4]. Med OrgLab og Tikket kommer verv, møtegodtgjørelser og arrangementshonorarer i tillegg.
8. **Den lille virksomheten (10–25 ansatte) er et sekundært segment.** Den skal betjenes av samme produkt i en veiledet modus, ikke med egne funksjoner. Behovet som avgjør, er at systemet hindrer feil og kan overleveres til et byrå.
9. **KI skal forberede, forklare og flagge, aldri godkjenne, sende eller betale** [F 5.2]. Avviksforklaringer skal komme fra beregningssporet. Språkmodellen formulerer bare teksten.
10. **Egne moduler for ferie/fravær, timer og utlegg (nytt krav):** Alt med rettsvirkning (arbeidsgiverperiode, ferietrekk, skatteklassifisering, a-meldingskoder) må ligge i lønnskjernen. Modulene samler bare fakta og godkjenninger. Ellers bryter kunden reglene når hun bytter modul. Modulene er en hovedgrunn til å velge Brutto for små kunder og for prosjektdokumentasjon i stiftelser. Kunder med skift og eget tidssystem skal ikke presses til å bruke dem. Det som avgjør, er blanding per ansattgruppe (VK-M02) og bytte uten tap (VK-M03) (kap. 5).
11. **Huma (nytt krav):** Første steg er en førsteklasses integrasjon, der bankkonto endret i Huma ikke blir aktiv uten bekreftelse. Å samle HR og lønn i Brutto er **et kjøpsargument på sikt, men en risiko som førstesalg**. Det som overbeviser kunden, er én registrering, kontrakt og lønn som stemmer overens, og lavere pris. Det som skremmer, er to systembytter samtidig, tynnere HR-funksjoner og avhengighet av én ung leverandør (kap. 2.4.1).
12. **Rapporten inneholder 140 behov:**
    - 83 for lønn og plattform (VK-01–84). 52 av dem er Må, og 9 av disse gjelder bare enkelte segmenter.
    - 39 for de egne modulene (VK-M/F/T/U). 24 av dem er Må.
    - 18 for HR og Huma (VK-H). 4 er Må i fase 1 og 7 er Må i fase 2.

    Mange Må er lovkrav, så bruk topp 20 (kap. 7) til å prioritere. De ti «øyeblikkene» står i kap. 8 og det vi ikke skal bygge i kap. 9.

---

## 1. Personas på én side

| # | Persona | Rolle i kjøpet | Viktigste jobb | Største smerte i dag | Dette vinner dem |
|---|---|---|---|---|---|
| 1 | **Kari**, lønnsansvarlig i Stiftelsen Nordlys (400 ansatte, 3 selskaper, Virke HUK, KLP, turnus, prosjekter) | Hovedbruker og faglig evaluator. Har i praksis veto. | Riktig lønn til 412 mottakere den 20., med dokumentert kontroll | Etterbetalinger fra lønnsoppgjør, import fra vaktplan og ledergodkjenning som ikke kommer inn i tide | Et lønnsoppgjør som kan kjøres på en formiddag, og avvik som er forklart før hun rekker å lete etter dem |
| 2 | **Jonas**, lønnsmedarbeider i et produksjons- og serviceselskap AS (150 ansatte, skift, Quinyx/Planday, 3 underenheter i tre AGA-soner) | Daglig bruker. Har sterk innflytelse på valget. | Få vakter og tillegg fra tidssystemet riktig inn, på riktig underenhet | Mapping av CSV-filer, ukjente vaktkoder, feil AGA-sone som først oppdages i tilbakemeldingen. Er alene om lønn. | En import som sier fra om de tre tingene som trenger ham, og en kjøreplan som en stedfortreder kan følge |
| 3 | **Lise**, økonomisjef/CFO | Beslutter og budsjetteier | Attestere trygt, få trekk betalt i tide, ha avstemt lønn hver måned | Attestasjon på e-post, avstemming som skyves til januar, og nye trekkfrister med strafferisiko | Attestasjon på 10 minutter med bevis, og en grønn hake for «trekk betalt og avstemt» |
| 4 | **Ingrid**, HR-sjef (bruker Huma eller lignende) | Påvirker og eier av masterdata. Blir beslutter hvis HR og lønn skal samles. | Gjennomføre lønnsoppgjøret, ARP/lønnskartlegging og rapporter til styret, og drive personaladministrasjonen i HR-systemet | Oppgjørsprotokoll i Excel blir importfil, ARP lages manuelt, og HR-data registreres både i HR-system og lønn | Fra protokoll til validert import uten Excel, ARP-grunnlaget på ett klikk, og på sikt ansettelse i én flyt (kap. 2.4.1) |
| 5 | **Revisor** (statsautorisert, mellomstort revisjonsselskap) | Påvirker. Kan stoppe valget gjennom krav om ISAE. | Teste kontroller, avstemme og ta stikkprøver | Ber om alt på e-post. Endringslogg og SoD er usynlig. | Eget revisorinnsyn med bevis bak hvert tall |
| 6 | **Daglig leder** i en forening eller et AS med 15 ansatte | Beslutter og bruker | Kjøre lønn riktig på kort tid uten å kunne lønn | Vet ikke hva hun ikke vet (2026-trekk, AGP, OTP, feriepenger, sluttoppgjør) | «Systemet stopper meg før jeg gjør feil» og et byrå som kan ta over med ett klikk |

---

## 2. Personas i dybden

### 2.1 Persona 1 – Lønnsansvarlig i stiftelse med 400 ansatte

**Kontekst** [D 11.1]
- Stiftelsen Nordlys driver omsorg, rus, et kompetansesenter og forskning. Den har tre juridiske enheter (stiftelse 280, Omsorg AS 100, Kompetanse AS 20) og sju underenheter, hvorav én i en sone med lavere AGA-sats.
- Lønnsmottakerne er 230 med fast månedslønn, 110 i turnus og 60 timelønnede ekstravakter. I tillegg kommer ca. 15 honorarmottakere og 7 styremedlemmer per måned, til sammen 412 mottakere.
- Tariff er Virke HUK for stiftelsen og AS-et innen omsorg. Pensjon er KLP for HUK-enhetene og OTP for AS-et som ikke har tariffavtale.
- Finansieringen kommer fra kommunale avtaler, Helsedirektoratet, to Forskningsråd-prosjekter og ett EU-prosjekt. 45 ansatte har lønnen fordelt i prosent på prosjekter.
- Lønnsteamet er Kari (100 %), Ola (100 %) og Fatima (60 %), med ca. 3 FTE inkludert HR og controller. Det gir ca. 130 lønnsmottakere per FTE, mot en internasjonal median på ca. 350 [D 1.4, D 11.1].
- Utbetaling er den 20. Variable tillegg betales én måned etterskuddsvis.
- Systemene er HR-system, vaktplan/tid, reise og utlegg, Xledger, DNB med filintegrasjon og Digipost.

**Jobs to be done**
1. Når lønnsmåneden starter, vil jeg at frister og status for alle 40 ledere skal styre seg selv, slik at jeg bruker tiden på avvik og ikke på purring.
2. Når lokale forhandlinger er ferdige, vil jeg etterbetale 258 ansatte fra 1. mai riktig, med alle tillegg og følgevirkninger, uten regneark.
3. Før jeg signerer, vil jeg vite at hvert avvik over terskel er forklart og kontrollert av en annen, slik at jeg kan stå for kontrollen overfor CFO og revisor.
4. Når en finansiør eller prosjektleder spør, vil jeg kunne vise lønnskost per prosjekt med sosiale kostnader, også bakover i tid.
5. Når noe er feil etter utbetaling, vil jeg rette det raskt uten å svekke kontrollen.

**Dagens smerter**

| Smerte | Konsekvens | Kilde |
|---|---|---|
| Retro dekker ikke tillegg som beregnes av timelønn (overtid, ubekvem arbeidstid, vakttillegg) | Etterbetalingen regnes i Excel. «Det største tidstyvet.» | [D 11.2 (10.11)], [D 2.2] |
| Retro som endrer skattetrekk og AGA tilbake i tid gir avstemmingsproblemer | Differanser som ingen forstår ved årsslutt | [D 8.1 Visma.net Payroll], [A 2.2] |
| Ledere godkjenner ikke innen fristen | Kari ringer rundt, og vakter flyttes til neste måned | [D 11.2 (5.11, 9.11)], [D 8.2 SAFE] |
| Nye vaktkoder fra vaktplanen ankommer umappet | Risiko for feil tillegg på mange ansatte (Kristiansand) | [D 4.4], [D 11.2 (9.11)] |
| Kontrollrapportene er laget for utskrift | Lange Excel-lister uten terskler eller forklaringsfelt | [D 1.3], [D 8.3] |
| Prosjektfordeling og lønn ligger i hvert sitt system | Rettelser med tilbakevirkende kraft gjøres som manuelle bilag | [D 6.3 pkt. 4], [D 11.2 (11.11)] |
| KLP krever egen fil og avstemming av premie | Kvartalsvis manuelt arbeid | [D 2.7], [B 9.3] |
| NAV-refusjoner følges ikke opp | «Svart hull». Penger kan gå tapt. | [D 11.2 (25.11)] |
| Ekstrakjøringer er like tunge som hovedkjøringen | Feil får vente til neste måned | [D 11.2 (26.11)] |

**Behov**

| ID | Behov (konkret) | MoSCoW | Begrunnelse / kilde |
|---|---|---|---|
| VK-01 | **Lønnskalender** med flere kjøringstyper (hovedlønn, reise/utlegg, honorar, ekstra) per juridisk enhet. Utbetaling flyttes automatisk ved helg og helligdag, og juni og desember har egne kalendere. | Må | [D 1.1 steg 1], [D 1.2] |
| VK-02 | **Cut-off-motor:** status per leder og enhet i sanntid og automatisk purring (U-14, U-11, kl. 08 på fristdagen). Ved fristen utsettes ugodkjente linjer automatisk til neste periode, og ansatt og leder varsles. Unntak krever begrunnelse og logges. | Må | [D 11.2 (9.11)], [D 11.4 pkt. 1] |
| VK-03 | **Import av oppgjørsprotokoll** (Excel/CSV) med validering før registrering: ansattnummer, virkningsdato, at trinnet finnes i stigen, beløp mot forventet tillegg og duplikater. Forhåndsvisning av total kost inkl. sosiale kostnader, deretter fire-øyne-godkjenning. | Må | [D 11.2 (30.10)], [D 2.2 pkt. 1] |
| VK-04 | **Etterberegning (retro)** for alle perioder fra virkningsdato, per måned og lønnsart. Den tar med tillegg som avhenger av timelønn (ubekvem arbeidstid, overtid, vakttillegg, merarbeid for deltidsansatte), tar hensyn til permisjoner og endret stillingsprosent i perioden, utelater sluttede etter tariffens regel om vedtaksdato og setter «siste lønnsendringsdato» riktig. Retroen er idempotent: to kjøringer uten nye fakta gir null nye linjer. | Må | [D 2.2], [C 5.2], [A 6.1 pkt. 2] |
| VK-05 | **Følgevirkninger av retro:** systemet flagger sykefravær der sykepengegrunnlaget endres (korrigert inntektsmelding må sendes innen 3 måneder etter signering), oppdaterer pensjonsgrunnlaget til KLP og øker feriepengegrunnlaget i utbetalingsåret. | Må | [C 5.4 pkt. 4], [C 5.2], [D 2.2 pkt. 5] |
| VK-06 | **Tariffbibliotek** for Virke HUK (og NHO Geneo) lagret som data: lønnsstiger og trinn med datogyldighet, ansiennitetsdato med automatisk opprykk (sen registrering utløser retro) og generelle tillegg som ny tabellversjon. | Må (HUK) | [C 8.1], [D 7] |
| VK-07 | **KLP:** pensjonsgrunnlag per ansatt (fast lønn × stillingsprosent + pensjonsgivende tillegg), lønnsfil i KLPs format, løpende endringsmeldinger og avstemming av premiefaktura mot grunnlaget. | Må (HUK) | [D 2.7], [B 9.3], [C 9] |
| VK-08 | **Prosjekt- og finansiørfordeling:** profiler med datogyldighet og kontroll av at fordelingen summerer til 100 %. Avsluttede prosjekter blokkeres. AGA, feriepenger og pensjon følger fordelingen, og kost per prosjekt vises **før** låsing. | Må | [D 6.3], [D 11.2 (11.11)] |
| VK-09 | **Retroaktiv omfordeling** av lønnskost mellom prosjekter uten å kjøre lønnen på nytt. Det lages et sporbart omfordelingsbilag. | Bør | [D 6.3 pkt. 4] |
| VK-10 | **Finansiørrapport:** timer, kost per time og sosiale kostnader per person, prosjekt og måned, i formatene til Forskningsrådet og Horizon Europe (årlig personalkostnad / 215 × dager). Satsene må verifiseres. | Bør | [D 6.4] |
| VK-11 | **Honorar og styrehonorar:** hurtigregistrering der mottakeren selv legger inn fødselsnummer og konto via BankID-lenke, egne honorarkjøringer og styrehonorar i konfidensiell gruppe. | Bør | [D 7], [C 6] |
| VK-12 | **NAV-refusjonsreskontro:** forventet refusjon per sak (fra inntektsmeldingen) matchet mot NAVs oppgjørsrapport-API, aldersfordelt utestående og forslag til purreliste. | Må | [D 11.2 (25.11)], [B 6.1] |
| VK-13 | **Ekstrakjøring på minutter med de samme kontrollene:** utvalg av ansatte → kontrollpakke → godkjenning → bankfil, trekkbetaling og erstatnings-a-melding for måneden. | Må | [D 11.2 (26.11)] |
| VK-14 | **Konsernvisning:** felles kalender, kontrollpakke og attestasjon for flere juridiske enheter, med separate a-meldinger, bilag og bankfiler. | Må (flere enheter) | [D 6.1], [D 11.1] |

**Det som ville vært kult i 2026**
- **Lønnsoppgjøret på en formiddag.** Kari laster opp protokollen og får tilbake: «258 endringer, 3 trenger deg (2 ukjente ansattnumre, 1 virkningsdato avviker fra protokollen). Etterbetaling mai–oktober 1,92 MNOK brutto, 2,35 MNOK med sosiale kostnader. 7 sluttede er utelatt etter HUK § x. 12 sykefravær trenger korrigert inntektsmelding innen 9.1.» Ingen regneark.
- **Etterbetalingen forklart på lønnsslippen** måned for måned: «Mai: +1 240 kr fastlønn, +86 kr kveldstillegg …». Det fjerner hovedtyngden av henvendelsene på lønnsdagen [D 11.2 (20.11)].
- **Prosjektleder bekrefter før låsing:** Hver prosjektleder får en lenke til «din lønnskost for oktober inkl. sosiale kostnader. Stemmer fordelingen?». Rettelser går inn som fordelingsendringer med dato.
- **NAV-refusjon som avstemmer seg selv** mot oppgjørsrapporten. Kari ser bare sakene som mangler.

**Suksessmål**

| Mål | Baseline (anslag) | Mål etter 6 mnd | Måles slik |
|---|---|---|---|
| Timer lønnsteamet bruker i en vanlig måned (400 ansatte) | 200–220 t [D 11.3] | ≤ 140 t (−30–35 %) | Tidsregistrering hos pilotkunden før og etter |
| Timer på et lokalt oppgjør med 258 ansatte | ~58 t [D 11.3] | ≤ 12 t, og 0 linjer beregnet utenfor systemet | Tid fra protokoll mottatt til attestert. Telling av manuelle linjer. |
| Andel avvik i kontrollpakken som systemet forklarer selv | ukjent (i fortellingen ble 28 av 31 forklart manuelt) | ≥ 85 % får automatisk årsak | Telemetri: avvik med systemårsak / alle avvik |
| Korrigeringer etter låsing per 100 mottakere | ukjent | < 0,5 per måned | Antall korreksjonslinjer og ekstrakjøringer |
| NAV-refusjoner eldre enn 60 dager uten kjent status | ukjent («svart hull») | 0 | Aldersfordelt reskontro |
| Henvendelser til lønn de tre første dagene etter lønnsdag | 9 per 412 i fortellingen. Typisk høyere uten forklaring. | < 1 per 100 ansatte | Merking av henvendelser |

---

### 2.2 Persona 2 – Lønnsmedarbeider i AS med 150 ansatte, skift og flere AGA-soner

**Kontekst** (sammensatt eksempel bygd på [D 1.4], [D 1.5], [D 5], [D 6.2])
- Produksjons- og serviceselskap med hovedkontor i sone I, en fabrikk i sone III og et lager i sone IV. Det gir tre underenheter med hver sin AGA-sats.
- Ca. 90 ansatte i 2- og 3-skift med kvelds-, natt-, helge- og helligdagstillegg, overtid og forskjøvet arbeidstid. 20 er timelønnede.
- Tiden registreres i et eksternt system (Quinyx, Planday, Tamigo eller GAT). Overføringen til lønn skjer i dag med CSV-fil.
- **Jonas** er den eneste lønnsmedarbeideren. Økonomisjefen er reserve, men har aldri kjørt lønn alene. Ifølge [D 1.4] bruker én person 15–30 t per hovedkjøring ved 100 ansatte. Med turnus er det trolig 30–45 t ved 150 ansatte (anslag).
- Regnskapet er Visma Business eller Tripletex. OTP-ordningen rapporteres via a-meldingen.

**Jobs to be done**
1. Når perioden er lukket i tidssystemet, vil jeg få alle godkjente vakter inn som riktige lønnslinjer og bare forholde meg til det som ikke passer.
2. Når en ansatt bytter arbeidssted eller jobber på flere steder, vil jeg at underenhet og AGA blir riktig uten at jeg må huske det.
3. Når en skiftarbeider blir syk, vil jeg at arbeidsgiverperioden, sykelønnen og refusjonskravet blir riktige etter reglene for skift.
4. Når jeg er borte, vil jeg at en kollega kan kjøre lønnen trygt etter en kjøreplan.

**Dagens smerter**

| Smerte | Konsekvens | Kilde |
|---|---|---|
| CSV-import med manuell mapping. I noen systemer kan importen bare kjøres én gang per kjøring (Tripletex). | Dobbeltimport, eller at rettelser må tastes inn | [D 5.2], [E 9.2] |
| Nye vaktkoder blir opprettet i tidssystemet uten at lønn får vite det | Ukjente lønnsarter eller feil tillegg | [D 11.2 (9.11)], [D 4.4] |
| Ansatte uten match (feil ansattnummer, nyansatt ikke opprettet) | Lønn mangler eller blir utsatt | [D 11.2 (9.11)] |
| Arbeidsforhold på feil underenhet | Feil AGA-sone, oppdaget først i tilbakemeldingen på a-meldingen | [D 11.2 (17.11)], [D 6.2] |
| Avviksmeldingene fra a-meldingen er kryptiske | Tid går til tolkning og søk | [G 3 #15], [B 2.3] |
| Jonas er alene om lønn | Høy risiko ved sykdom eller ferie | [D 1.4] («én person, sårbar ved fravær») |
| Systemene er laget for kontorlønn | Arbeidsgiverperioden for skift og timelønnede regnes manuelt | [C 7] |

**Behov**

| ID | Behov (konkret) | MoSCoW | Begrunnelse / kilde |
|---|---|---|---|
| VK-15 | **Import fra tidssystem** via API eller fil. Importen kan kjøres mange ganger (idempotent per linje), viser hva som er endret siden forrige import og gir forhåndsvisning før linjene går inn i lønnsgrunnlaget. | Må | [D 8.3], [G 1.11 B3] |
| VK-16 | **Mappingregister** fra tidskode til lønnsart, med versjoner. Ukjente koder legges i karantene uten å stoppe resten av importen. En ny mapping må testberegnes på reelle vakter og godkjennes av en annen før den tas i bruk. | Må | [D 4.4] (Kristiansand), [D 11.4 pkt. 2] |
| VK-17 | **Matching av ansatte og arbeidsforhold** med tydelig feilliste (feil ansattnummer, ikke opprettet, sluttet) og forslag til riktig match | Må | [D 11.2 (9.11)] |
| VK-18 | **Underenhet per arbeidsforhold med datogyldighet.** AGA-sonen utledes fra Enhetsregisteret, arbeidssted valideres mot underenhet, og flytting midt i måneden håndteres. AGA-rapport per underenhet og sone. | Må | [D 6.2], [B 5.3] |
| VK-19 | **Overvåking av fribeløpet** i sone Ia (850 000 kr i spart avgift per foretak eller konsern) | Bør (Må i sone Ia) | [C 0.1] |
| VK-20 | **Regler for skift og turnus:** sykelønn i arbeidsgiverperioden med dagsats per faktisk arbeidsdag for timelønnede i skift, samt helligdagstillegg og forskjøvet arbeidstid etter tariff | Må | [C 7], [D 4.4] |
| VK-21 | **AML-kontroll i lønnsdata:** varsel om overtid ut over rammene og tillegg uten tilhørende vakt. Dette er kontroll, ikke planlegging. | Bør | [D 1.3] |
| VK-22 | **Forhåndsvalidering av a-meldingen** mot forretningsreglene før lønnen kjøres, inkludert F529 og F532 fra 2027. Tilbakemeldingen oversettes til klartekst med lenke til ansatt og felt, og et forslag til retting. | Må | [B 2.3], [B 12], [D 8.3] |
| VK-23 | **Veiledet kjøreplan:** en sjekkliste med status per steg, slik at en stedfortreder kan kjøre lønnen uten å ringe leverandøren | Bør | [D 1.4]. Viktig, men stopper ikke signering. Grunnstrukturen dekkes av VK-01, VK-02 og VK-59. |
| VK-24 | **Timebank og avspaseringssaldo** synkronisert med tidssystemet. Hvem som eier saldoen, avklares per kunde. (Bruker kunden Bruttos timemodul, gjelder VK-T04.) | Bør | [G 1.11 B3] |
| VK-25 | **Masseendringer med forhåndsvisning**, for eksempel nytt skifttillegg for 60 ansatte fra en gitt dato | Bør | [D 2.1] |
| VK-26 | **Løpende forhåndsberegning** av neste lønn etter hvert som godkjente timer kommer inn | Kan | [G 2.3] |

**Det som ville vært kult i 2026**
- **En import som sier fra:** «4 812 linjer lest. 4 809 klare. 3 trenger deg: 2 ansatte uten match (forslag: ansattnr 1043 → 1034), 1 ny kode `NATT-F` ("forsterket natt") som ligner `NATT` + 25 %. Forslaget er testberegnet på 14 vakter fra oktober.»
- **Sonevakt før kjøring:** «Per Hansen har 22 vakter på lageret i sone IV, men arbeidsforholdet ligger på hovedkontoret i sone I. Konsekvens: 3 140 kr for mye i AGA.»
- **Stedfortredermodus:** Økonomisjefen kan kjøre lønnen med en guidet versjon av kjøreplanen, der hvert steg forklarer hva som skal sjekkes.

**Suksessmål**

| Mål | Baseline (anslag) | Mål | Måles slik |
|---|---|---|---|
| Tid fra import startet til grunnlaget er klart for testkjøring | 1–2 arbeidsdager (anslag) | < 2 timer | Tidsstempler i systemet |
| Andel importlinjer som matches og mappes på første forsøk | ukjent | ≥ 99,5 % | Telemetri |
| Arbeidsforhold med feil underenhet i tilbakemeldingen fra a-meldingen | ≥ 1 per måned i fortellingen | 0, fordi feilen fanges før innsending | Avvikstyper i tilbakemeldingen |
| Tilbakemeldinger uten avvik på første innsending | ukjent | ≥ 98 % | Tilbakemeldings-API |
| Lønn kjørt av stedfortreder uten hjelp fra leverandør | sjelden mulig | Ja, i test hos pilotkunden | Øvelse med økonomisjef |

---

### 2.3 Persona 3 – Økonomisjef/CFO

**Kontekst**
- Har det økonomiske ansvaret for lønn. Lønnsansvarlig har det faglige [D 3.1]. Attesterer totalsummer og godkjenner bankfilen sammen med en annen person i nettbanken [D 1.1 steg 8 og 10].
- Eier internkontrollen og møter revisor. Er budsjettansvarlig for lønnskost, som ofte er 50–80 % av kostnadene i en stiftelse eller serviceorganisasjon (anslag).
- **Ny situasjon fra 2026:** Forskuddstrekk og utleggstrekk forfaller senest første virkedag etter hver lønnsutbetaling, og manglende betaling kan få strafferettslige konsekvenser. AGA betales fortsatt annenhver måned [B 4], [D 11.2 (23.11)].

**Jobs to be done**
1. Når lønnen skal attesteres, vil jeg se på få minutter at totalene er rimelige og at avvik er forklart og kontrollert, slik at jeg kan godkjenne med god samvittighet.
2. Når lønnen er utbetalt, vil jeg vite at trekk er betalt i tide og at lønn, regnskap, a-melding og bank stemmer, hver måned og ikke først i januar.
3. Når budsjett og prognose lages, vil jeg ha lønnskost med sosiale kostnader og kjente endringer uten Excel-akrobatikk.
4. Jeg vil at svindel og feilutbetalinger skal være vanskelige: ingen skal alene kunne endre en bankkonto og utbetale.

**Dagens smerter**

| Smerte | Konsekvens | Kilde |
|---|---|---|
| Attestasjon skjer på e-post uten sporbarhet | Svakt bevis overfor revisor | [D 1.1 steg 8] |
| Avstemmingen skyves til årsslutt | Differansene hoper seg opp. Revisor har funnet feil betalt AGA og manglende avstemming. | [D 1.1 steg 13], [D 4.2] |
| Tre-veis avstemming tar 4–6 timer per måned | Tid og risiko | [D 11.2 (24.11)] |
| Retro endrer skattetrekk og AGA tilbake i tid | Avstemmingsproblemer | [D 8.1] |
| Samme person kan lage og godkjenne bankfilen, eller endre en bankkonto | Svindelvektor | [D 3.2] |
| Prognose og budsjett lages i Excel fra en eksport | Tidkrevende og utdatert | [D 6.5] |
| Bilag med feil eller manglende dimensjoner | Rettes i regnskapet | [D 1.1 steg 12] |

**Behov**

| ID | Behov (konkret) | MoSCoW | Begrunnelse / kilde |
|---|---|---|---|
| VK-27 | **Attestasjonsbilde:** totaler per selskap (brutto, netto, forskuddstrekk, utleggstrekk, AGA per sone, pensjon, feriepenger, antall mottakere og ansatte) mot forrige måned, samme måned i fjor og budsjett. Avvikslisten viser hvem som forklarte og kontrollerte hvert avvik. Godkjenning med passkey eller BankID, også på mobil. | Må | [D 1.1 steg 8], [D 11.2 (12.–13.11)] |
| VK-28 | **Hard sperre:** bankfil og trekkbetalinger kan ikke lages før godkjenningskjeden er fullført. Enhver endring etter godkjenning nullstiller godkjenningen. | Må | [D 4.1], [D 11.4 pkt. 4] |
| VK-29 | **Betalinger etter 2026-reglene:** nettolønn (pain.001), forskuddstrekk (KID med månedsperiode, som eget betalingsoppdrag), utleggstrekk (KID per pålegg, nye og gamle regler hver for seg) og kreditortrekk, med riktig forfall. Status fra pain.002/camt.054, og varsel hvis noe ikke er betalt. | Må | [B 4], [D 0.4–0.5], [D 4.1] |
| VK-30 | **Håndhevet arbeidsdeling (SoD), ikke bare rapportert:** samme person kan ikke endre bankkonto og godkjenne kjøringen, og ingen kan endre egne data. Rapport over SoD-konflikter og halvårlig tilgangsgjennomgang med signering. | Må | [D 3.2], [D 4.1] |
| VK-31 | **Kontonummerskjold:** bare den ansatte (med BankID) eller to personer kan endre kontonummer. Endringen får karantene eller varsel og kommer på en egen liste i kontrollpakken. | Må | [D 3.2 pkt. 1], [G 3 #13] |
| VK-32 | **Regnskapsbilag** per konto og dimensjon (selskap, avdeling, prosjekt, finansiør), validert mot kontoplan og dimensjoner i ERP-systemet før overføring. Støtter Xledger, Tripletex, PowerOffice, Business Central, Visma Business og Unit4. | Må | [D 5.2], [D 11.2 (17.11)] |
| VK-33 | **Periodisering og avsetninger:** variable tillegg som betales etterskuddsvis, feriepengeavsetning (konto 2940), AGA av feriepenger, og avsatt mot utbetalt lønnsoppgjør | Må (250+), Bør (<250) | [D 1.2], [D 2.6] |
| VK-34 | **Månedlig automatisk avstemming** av lønn mot hovedbok, a-melding (avstemmingsrapport-API) og bank, med forklarte og signerte differanser | Må | [D 4.1], [B 2.6], [G 3 #16] |
| VK-35 | **Lønnskostprognose for 12 måneder** for kjente ansatte, med planlagte endringer og oppgjør inkl. AGA, feriepenger og pensjon, og simulering av «hva koster oppgjøret?» | Bør | [D 6.5], [G 3 #29] |
| VK-36 | **Likviditetskalender:** forventede utbetalinger (netto, trekk, AGA-termin, pensjonspremie) per dato | Bør | [B 4] |
| VK-37 | **Lederrapport:** lønnskost og FTE per enhet mot budsjett. Ledere uten personalansvar ser ikke individuell lønn. | Bør | [D 3.3], [D 10.2] |
| VK-38 | **Kontinuitet:** mulighet til å la en byråpartner kjøre lønnen i samme system ved fravær eller vakanse (co-sourcing), med egne roller og full logg | Bør | [D 1.5], [E 4] |

**Det som ville vært kult i 2026**
- **Attestasjon på 8 minutter fra mobilen:** «3 selskaper, 412 mottakere, brutto 23,4 MNOK (+1,9 MNOK etterbetaling, avsatt). 31 avvik, alle forklart og kontrollert av Fatima. Ingen nye bankkontoer uten BankID.» Godkjent med passkey, og bankfil og trekkbetalinger lages automatisk.
- **En grønn hake dagen etter forfall:** «Forskuddstrekk 6 214 312 kr betalt 23.11 med KID …, matchet mot camt.054. Utleggstrekk 4 av 4 betalt.»
- **Avstemt dagen etter lønn:** lønn = hovedbok = a-melding = bank, og eneste differanse er reiseregninger godkjent i oktober og betalt i november, med forklaring.
- **«Hva koster oppgjøret?»-knappen** når budsjettet for 2027 lages.

**Suksessmål**

| Mål | Baseline (anslag) | Mål | Måles slik |
|---|---|---|---|
| Tid CFO bruker på attestasjon | ~4 t per måned inkl. oppfølging [D 11.3] | < 15 min per kjøring | Tid fra varsel til godkjent |
| Uforklart differanse mellom lønn, hovedbok, a-melding og bank ved månedsslutt | Ryddes ofte først ved årsslutt [D 1.1] | 0 kr hver måned | Avstemmingsmodul |
| Trekk betalt innen forfall | Ny risiko fra 2026 | 100 % | Betalingsstatus |
| Merknader fra revisor på lønnsområdet | Typiske funn: avstemming og SoD [D 3.2, D 4.2] | 0 vesentlige | Revisjonsbrev |
| Tid til avstemming per måned | 4–6 t [D 11.2] | < 30 min | Tidsregistrering |

---

### 2.4 Persona 4 – HR-sjef

**Kontekst**
- Eier masterdata (ansettelser, stillingsprosent, lønnsendringer) og registrerer i HR-systemet. Lønn kontrollerer [D 3.1].
- Leder lønnsoppgjøret. I HUK 2026 var virkningsdato 1.5, sentrale tillegg ble godkjent 9.7 og lokale forhandlinger skulle være ferdige innen 31.10 [D 2.2].
- Har ansvar for ARP og lønnskartlegging etter kjønn annethvert år (private med flere enn 50 ansatte), redegjørelse i årsberetningen, sykefraværsstatistikk og rapporter til ledermøte og styre [D 2.8], [B 9.2].
- Har ofte HR-system (Huma, Simployer, CatalystOne, HiBob, Sympa). Brutto skal integreres med Huma først og på sikt erstatte det (se 2.4.1). Ved 250+ ansatte er HR-systemet master for person, stilling og organisasjon [D 5.2].

**Jobs to be done**
1. Når oppgjøret forhandles, vil jeg ha et riktig grunnlag (lønn, trinn, ansiennitet, kjønn, stillingskategori) og kunne regne på kost og kjønnsbalanse.
2. Når protokollen er signert, vil jeg få resultatet inn i lønn uten feil og uten å lage en importfil for hånd.
3. Annethvert år vil jeg lage lønnskartleggingen og ARP-redegjørelsen uten å bygge datasettet fra bunnen.
4. Jeg vil at endringene mine skal komme inn i riktig kjøring og at jeg ser status på dem.

**Dagens smerter**

| Smerte | Konsekvens | Kilde |
|---|---|---|
| Protokollen i Excel blir en importfil som lages for hånd | Risiko for feil virkningsdato og feil ansattnummer | [D 11.2 (30.10)] |
| ARP og lønnskartlegging lages manuelt fra eksport | Tar tid, og stillingskategoriene er ikke definert i dataene | [D 2.8], [G 2.2] |
| Uklart hvem som er master for hvilke data mellom HR og lønn | Dobbel registrering og avvik | [D 5.2], [G 1.5] |
| HR-data i Word, PDF og Excel (NORCE) | Lav datakvalitet | [D 8.2] |
| Endringer etter cut-off forsvinner eller kommer for sent | Feil lønn og retro neste måned | [D 11.2 (4.11)] |

**Behov**

| ID | Behov (konkret) | MoSCoW | Begrunnelse / kilde |
|---|---|---|---|
| VK-39 | **Grunnlag for lønnsoppgjør:** eksport eller arbeidsflate med lønn, trinn, ansiennitet, kjønn, stillingskategori og siste endring per ansatt. Resultatet importeres tilbake via VK-03. | Må | [D 2.2], [D 11.2] |
| VK-40 | **Oppgjørssimulering:** kost av sentrale og lokale tillegg inkl. sosiale kostnader og retro, fordelt på kjønn og enhet | Bør | [D 6.5], [G 3 #22] |
| VK-41 | **Pottfordeling med lederforslag og arbeidsflyt** | Kan | [G 3 #22]. Ofte i HR-system eller Excel. |
| VK-42 | **Lønnskartlegging/ARP:** lønn per kjønn per stillingskategori og nivå, deltid, permisjon og fravær, med anonymisering (minste gruppestørrelse) og eksport til redegjørelsen. NB: Ufrivillig deltid finnes ikke i lønnsdata og må komme fra kartlegging. | Må (>50 ansatte) | [D 2.8], [B 9.2], [G 2.2] |
| VK-43 | **Datamodell for stillingskategori og «arbeid av lik verdi»**, med skille mellom fast og variabel lønn. (Lønnsgap-pakke med 5 %-alarm er Kan til direktivet er tatt inn i EØS-avtalen.) | Må (modell) | [G 2.2], [D 2.8] |
| VK-44 | **HR-systemet som master:** synkronisering av person, stilling, organisasjon og leder fra Huma (først, se VK-H01), Simployer, CatalystOne, HiBob, Sympa og lignende, med register over hvem som eier hvilke attributter og logg over konflikter | Må (250+, og for alle med Huma), Bør (<250) | [D 5.3], [G 1.5], kap. 2.4.1 |
| VK-45 | **Sykefravær fra lønnsperspektivet:** fraværsprosent og kostnad per enhet (aggregert), kost i arbeidsgiverperioden mot refusjon | Bør | [G 2.7] |
| VK-46 | **Standardrapporter:** headcount, FTE, turnover, alder og kjønn per enhet, til styre, årsberetning og tilskuddsrapporter | Bør | [D 6.5] |
| VK-47 | **Status på HR-endringer:** mottatt, kontrollert, med i kjøring. Endringer etter cut-off merkes som unntak. | Bør | [D 11.2 (4.11)] |
| VK-48 | **Rollebasert innsyn:** HR ser lønn, men ikke trekkpålegg, fagforeningstrekk eller helsedetaljer uten tjenstlig behov | Må | [B 11], [F 3.3] |

**Det som ville vært kult i 2026**
- **ARP-grunnlaget på ett klikk:** lønn per kjønn og kategori, deltid og uttak av foreldrepermisjon, anonymisert og ferdig til redegjørelsen.
- **Oppgjør med kost og kjønnsbalanse i sanntid:** Når et tillegg legges inn, oppdateres kost (inkl. sosiale kostnader og retro), kjønnsfordelingen og andelen av potten med en gang.

**Suksessmål**

| Mål | Baseline (anslag) | Mål | Måles slik |
|---|---|---|---|
| Tid for å lage grunnlaget til lønnskartleggingen | Dager eller uker (anslag) | < 1 dag | Intervju og tidsregistrering |
| Feil i oppgjørsimport som når testkjøringen | ukjent | 0 (fanges i validering) | Valideringslogg |
| Parallelle Excel-ark i HR for lønnsdata | Vanlig | Fjernet hos pilotkunden | Intervju |

#### 2.4.1 HR i Huma i dag, og hva som skal til for å samle HR og lønn i Brutto (nytt krav)

**Kravet:** Brutto skal integreres med HR-systemet **Huma** (humahr.com) og på sikt erstatte det. Huma dekker personaladministrasjon, onboarding, fravær, dokumenter, digitale arbeidsavtaler, medarbeidersamtaler og utstyr, men kjører ikke lønn selv.

**Hva vi vet om Huma (søk 28.10.2026):**
- Uni Micro beskriver Huma som en nordisk HR-løsning for små og mellomstore virksomheter. Den har personaladministrasjon, fravær, digitale arbeidsavtaler, on- og offboarding, medarbeidersamtaler og undersøkelser, utstyr, digitale håndbøker og kompetanseoversikt [Uni Micro], [humahr.com].
- Huma har lønnsintegrasjoner mot Tripletex, Visma.net Payroll og PowerOffice Go (Fiken er også nevnt). Mot Visma.net Payroll synkroniseres ansatte begge veier, og **endringer i bankkonto i Huma oppdateres også i Visma.net Payroll**. Fravær kan synkroniseres, men hver fraværstype må mappes til en hendelseskode i Visma [humahr.com].
- Det er ikke avklart om Huma har et offentlig API, eller hvor mye sykefraværsoppfølging produktet dekker (se kap. 10).

**Kontekst for en kunde med 100–400 ansatte:** HR-sjefen (eller HR-rådgiveren hos de minste) bruker Huma daglig. Lønn ligger i et annet system med en integrasjon som oftest bare synkroniserer ansatte og fravær. HR registrerer masterdata, og lønn kontrollerer [D 3.1]. Feil startdato eller stillingsprosent gir feil lønn, a-melding og pensjon [D 1.1 steg 2].

**HR-behov kunden dekker i Huma eller lignende systemer i dag, og koblingen til lønn**

| HR-område | Hva HR gjør i dag | Kobling til lønn | Tap hvis koblingen mangler |
|---|---|---|---|
| Personalregister og organisasjon | Personalia, pårørende, stilling, avdeling, leder og organisasjonskart | Stamdata for arbeidsforhold, underenhet, kostnadssted og lederkjede for godkjenning | Dobbel registrering og feil underenhet eller AGA-sone [D 6.2] |
| Onboarding og offboarding | Sjekklister, oppgaver til leder, IT og HR, og velkomstpakke | Ny ansatt utløser skattekort, OTP/KLP-innmelding og bankkonto. Slutt utløser sluttoppgjør, feriepenger og innlevering av utstyr. | 50 % trekk ved manglende skattekort og lønn etter sluttdato [D 1.3] |
| Digitale arbeidsavtaler | Maler, e-signering og endringsbrev | Lønn, stillingsprosent og tariffplassering i avtalen må være lik det som ligger i lønn. | Revisor finner avvik mellom kontrakt og lønn i stikkprøver [D 4.2] |
| Fravær | Søknad, godkjenning og saldo | Arbeidsgiverperiode, refusjon, ferietrekk og permisjon i a-meldingen | Mapping av hendelseskoder per fraværstype (som i Visma-integrasjonen) og dobbel registrering |
| Dokumenter og personalmappe | Avtaler, attester og personalsaker | Lønnsrelevante dokumenter (trekkavtaler, lån, lønnsendringer) | Dokumentene ligger to steder |
| Medarbeidersamtaler og undersøkelser | Maler, oppfølging og mål | Grunnlag for lønnssamtale og lokalt oppgjør | Lite. Svak kobling til lønn. |
| Utstyr | PC, telefon, nøkler og bil | Innlevering ved slutt, eventuell fordel (fri telefon, firmabil) og trekk etter avtale (aml. § 14-15) | Fordeler kan bli feil rapportert |
| Håndbøker og kompetanse | Personalhåndbok med lesebekreftelse, sertifikater og kurs | Liten, unntatt autorisasjon og politiattest i helse og omsorg | Lite |

**Behov (VK-H).** Kolonnen «Fase» viser når behovet gjelder: **1** = Brutto integrert med Huma (kunden beholder Huma), **2** = kunden samler HR og lønn i Brutto. MoSCoW gjelder for fasen: Må i fase 2 betyr at kunden **ikke** vil flytte HR fra Huma til Brutto uten dette.

| ID | Behov (konkret) | Fase | MoSCoW | Begrunnelse / kilde |
|---|---|---|---|---|
| VK-H01 | **Toveis synkronisering mellom Huma og Brutto** av ansatte og arbeidsforhold (start, slutt, stillingsprosent, stilling, avdeling, leder). Et register viser hvilket system som eier hvert attributt: Huma eier personalia og organisasjon, Brutto eier lønn, skattekort og a-meldingsfelt. Konflikter logges. | 1 | Må | [G 0 pkt. 3], [G 1.5], [D 5.2] |
| VK-H02 | **Fravær fra Huma inn i Brutto** som fraværsepisoder. Fraværskodene mappes én gang, og arbeidsgiverperioden beregnes i Brutto-kjernen (VK-F05). Huma blir kilde for fravær etter VK-M02. | 1 | Må | [humahr.com] (fraværssynk med hendelseskoder), kap. 5.1 |
| VK-H03 | **Bankkonto endret i Huma behandles som ekstern endring.** Den blir ikke aktiv før den er bekreftet av den ansatte med BankID eller godkjent av en annen person, og den vises i kontrollpakken (VK-31). | 1 | Må | Huma oppdaterer bankkonto direkte i Visma.net Payroll [humahr.com]. Det er den klassiske svindelveien [D 3.2 pkt. 1]. |
| VK-H04 | **Onboarding og offboarding i Huma utløser handlinger i Brutto:** en planlagt ansettelse oppretter et utkast til arbeidsforhold og ber om skattekort, OTP- eller KLP-innmelding og bankkonto. Slutt starter sluttoppgjøret. | 1 | Må | [G 1.11 B2] (hendelsene `hr.employment.planned/terminated`), [C 10.1] |
| VK-H05 | **Begrenset lønnsdata tilbake til Huma** (for eksempel lønnsnivå til medarbeider- og lønnssamtale), styrt av tilgangspakke | 1 | Bør | [G 1.9] |
| VK-H06 | **Lenke fra Huma til lønnsslippen** i Brutto med samme innlogging (SSO) | 1 | Kan | [G 1.2] |
| VK-H07 | **Personalregister:** personalia, pårørende, stillingshistorikk, organisasjonskart, lederhierarki, egendefinerte felt og personalmappe | 2 | Må | Huma-funksjonalitet (over), VK-M05 |
| VK-H08 | **Digitale arbeidsavtaler og endringsbrev** laget fra de samme dataene som lønnen beregnes av: maler for fast, midlertidig og tilkallingsavtale med lovens minimumsinnhold (aml. § 14-6), e-signering med BankID, og endringsbrev automatisk ved lønns- eller stillingsendring | 2 | Må | Fjerner avvik mellom kontrakt og lønn [D 4.2]. Største gevinst ved å samle HR og lønn. |
| VK-H09 | **Onboarding og offboarding** med sjekklister, oppgaver per rolle (leder, IT, HR) og maler | 2 | Må | [humahr.com/knowledge/onboarding] |
| VK-H10 | **Dokumentarkiv og personalmappe** med tilgangsstyring per dokumenttype, oppbevaringstider og sletting etter GDPR | 2 | Må | [B 11], [F 4.11] |
| VK-H11 | **Fravær i egen modul** med samme dekning som Huma (VK-F01–F09) | 2 | Må | Kap. 5.3 |
| VK-H12 | **Medarbeidersamtaler** (maler, oppfølging, mål) og enkle undersøkelser | 2 | Må for full erstatning, ellers Bør | Uten dette beholder kunden Huma for samtalene, og prisgevinsten faller bort. |
| VK-H13 | **Utstyr** koblet til offboarding (innlevering) og til fordeler i lønn (fri telefon, firmabil) | 2 | Bør | [C 1.4] (fordeler) |
| VK-H14 | **Kompetanse og sertifikater med utløpsvarsel**, for eksempel autorisasjon, politiattest og kurs | 2 | Bør (helse og omsorg), Kan (ellers) | Nordlys driver omsorg [D 11.1]. |
| VK-H15 | **Digitale håndbøker** med lesebekreftelse | 2 | Kan | Huma-funksjonalitet |
| VK-H16 | **Migrering fra Huma uten tap:** personalmapper, signerte avtaler, historikk og saldoer. Eierskapet til attributtgruppene flyttes fra Huma til Brutto uten at kjernen ser bruddet. | 2 | Må | [G 0 pkt. 3], [F 6] |
| VK-H17 | **Samlet pris lavere enn Huma + lønnssystem**, og dokumentert eksport ved exit | 2 | Bør | [A 6.2 pkt. 4], [D 9.2 pkt. 7] |
| VK-H18 | **Rekruttering (ATS), HMS og avvik, læringsplattform og avansert prestasjonsstyring (OKR, 360)** | 2 | Ikke nå | Integreres (Huma integrerer f.eks. med Teamtailor [Teamtailor]). Se kap. 9. |

**Er det et kjøpsargument eller en risiko å samle HR og lønn?**

| Kjøpsargument | Risiko for virksomhetskunden |
|---|---|
| **Én registrering:** ansettelse → arbeidsavtale → lønn → a-melding uten dobbel registrering. Det fjerner en klassisk feilkilde [D 1.1 steg 2]. | **To endringer på én gang:** Lønnssjefen vil ikke risikere lønnen for en HR-gevinst [A 6.2]. Å bytte lønn og HR samtidig dobler risikoen ved implementeringen. |
| **Kontrakt og lønn kan ikke spriker** når endringsbrevet lages fra lønnsdataene. Revisors stikkprøve «kontrakt mot lønn» blir automatisk [D 4.2]. | **Mindre dybde i HR i flere år:** Brutto blir tynnere enn Huma på samtaler, undersøkelser og håndbøker. HR-sjefen taper funksjoner hun bruker daglig. |
| **Fravær registreres én gang** i stedet for to systemer med mapping av hendelseskoder [humahr.com]. | **Én leverandør for alt:** Personaldata og lønn ligger hos en ung leverandør. Faller den, rammes både HR og lønn. Det krever dokumentert exit, ISAE og ISO. |
| **Onboarding utløser skattekort, pensjon og bankkonto automatisk**, og offboarding starter sluttoppgjøret. | **Mer sensitive data på ett sted** (personalsaker, helse, fagforening). Et sikkerhetsbrudd får større konsekvens. Krever DPIA og streng rollestyring [B 11]. |
| **Én app, én innlogging og én databehandleravtale** for ansatte og ledere | **Svekket arbeidsdeling:** HR registrerer og lønn kontrollerer [D 3.1]. I samme system må rollene fortsatt være adskilt (VK-30). |
| **Lavere samlet pris** (én lisens i stedet for HR-system + lønn) | **Delt beslutning:** HR-sjef og CFO eier ofte hvert sitt system. Kjøpsprosessen blir tyngre. |
| **Oppgjør og ARP** får HR-data (stillingskategori) og lønn på samme sted. | **Integrasjonen med Huma kan bli svakere** hvis Huma ser Brutto som konkurrent. Kunden i fase 1 er avhengig av at begge leverandørene vedlikeholder den. |

**Vurdering:** For kunder med 100–400 ansatte er det å samle HR og lønn **et kjøpsargument på sikt, men en risiko som førstesalg.**
- Det som overbeviser, er ikke «ett system». Det er **én registrering, kontrakt og lønn som henger sammen, og lavere totalpris**.
- Det som skremmer, er **to endringer samtidig og avhengighet av én ung leverandør**.

**Anbefalt rekkefølge:**
1. Selg lønn med en førsteklasses Huma-integrasjon (fase 1: VK-H01–H04).
2. Tilby å samle HR og lønn når Brutto dekker Må-listen for fase 2 og kan vise referanser.
3. Tilby migrering fra Huma (VK-H16) som et eget, valgfritt steg.

Argumentet er sterkest hos de minste i dette segmentet (100–150 ansatte uten egen HR-fagperson). Det er svakest hos 300–400 ansatte med en HR-sjef som bruker samtaler, undersøkelser og håndbøker aktivt.

**Kult i 2026:** **Ansettelse i én flyt.** Lederen fyller ut tilbudet → arbeidsavtalen signeres med BankID → den nyansatte legger inn kontonummer med BankID → skattekort hentes og OTP eller KLP meldes inn → første lønn er klar. HR og lønn rører ikke dataene.

**Suksessmål for HR i Brutto**

| Mål | Baseline (anslag) | Mål | Måles slik |
|---|---|---|---|
| Felt som registreres to ganger (HR og lønn) per nyansatt | 10–20 felt (anslag) | 0 i fase 2, < 3 i fase 1 | Gjennomgang hos pilotkunden |
| Avvik mellom lønn i arbeidsavtalen og lønn i lønnssystemet | ukjent (revisorfunn) | 0 | Automatisk kontroll |
| Tid fra signert arbeidsavtale til ansatt klar for lønn | dager (anslag) | samme dag | Tidsstempler |
| Bankkontoendringer fra Huma uten bekreftelse | Dagens praksis i Visma-integrasjonen | 0 | Kontrollpakken |

---

### 2.5 Persona 5 – Ekstern revisor

**Kontekst**
- Revisjonen deles i interimrevisjon om høsten (test av kontroller) og årsrevisjon i januar–mars (avstemminger og analyser) [D 2.9], [D 4.2].
- Lønn er et eget transaksjonsområde, og typiske funn er manglende avstemming, feil betalt AGA og svak arbeidsdeling [D 4.2], [D 3.2].
- Ber om ISAE 3402 type II fra leverandøren når lønnen kjøres i skyen eller er satt ut [D 4.3], [F 4.1].
- NB: Mange små AS har ikke revisor. Persona 5 er viktigst for stiftelser (revisjonsplikt) og kunder med 50+ ansatte.

**Jobs to be done**
1. Når jeg tester kontrollene, vil jeg se bevis for at hver kontroll faktisk ble utført, av riktig person og på riktige data.
2. Når jeg avstemmer, vil jeg ha lønn mot regnskap og a-melding for året, med forklarte differanser.
3. Når jeg tar stikkprøver, vil jeg finne kontrakt, vedtak, timer, godkjenning og beregning for en ansatt uten å sende e-post.
4. Jeg vil vite at leverandørens generelle IT-kontroller er testet (ISAE 3402).

**Dagens smerter**

| Smerte | Konsekvens | Kilde |
|---|---|---|
| Revisor ber om alt på e-post, og kunden lager PDF-er | Mye tid hos kunden og revisor | [D 4.2] |
| Endringslogg for masterdata og bankkonto er ikke tilgjengelig eller er ufullstendig | Kontrollen kan ikke testes | [D 4.1] |
| SoD er usynlig | Funn og kompenserende kontroller | [D 3.2] (Sykehuset Innlandet) |
| Avstemming er ikke gjort løpende | Funn | [D 4.2] (Konsek) |

**Behov**

| ID | Behov (konkret) | MoSCoW | Begrunnelse / kilde |
|---|---|---|---|
| VK-49 | **Revisorrolle:** invitert av kunden, tidsbegrenset, bare lesetilgang, alle oppslag logget | Må | [D 3.3], [D 4.2] |
| VK-50 | **Revisorpakke per periode:** lønnsjournal per lønnsart, avstemming mot a-meldingen, endringslogg for masterdata og bankkonto, attestasjonsbevis per kjøring, tilgangsliste og SoD-rapport, nyansatte og sluttere, ytelser til ledende personer og styret | Må | [D 4.2] |
| VK-51 | **Automatisk kontrollbevis:** hvem kontrollerte hva, når, og hvilken versjon av dataene de så | Må | [D 4.1], [F 1.7] |
| VK-52 | **Eksport av rådata** (CSV/Excel med stabile nøkler) for revisors analyseverktøy | Må | [D 5.2 BI] |
| VK-53 | **Støtte for stikkprøver:** velg utvalg → per ansatt lenke til kontrakt og vedtak (fra HR), timelister og godkjenning, bankkonto og beregningsspor | Bør | [D 4.2] |
| VK-54 | **Reproduserbar beregning:** «hvorfor fikk X dette beløpet i mars» med regel, sats og kildehendelse, og visning av data slik de var på en gitt dato | Bør | [F 1.2], [G 3 #3, #32] |
| VK-55 | **Cut-off-test innebygd:** rapport over lønn etter sluttdato og ugodkjente linjer som er utbetalt (skal være 0) | Må | [D 4.1], [D 4.2] |
| VK-56 | **ISAE 3402:** type 1 ved første produksjonskunde, type 2 fra år 2 | Må (250+), Bør (<250) | [F 4.2], [D 4.3] |
| VK-57 | **Grunnlag for noter:** ytelser til ledende personer, styrehonorar, årsverk og pensjonskostnad | Bør | [D 2.6], [D 2.1] |

**Det som ville vært kult i 2026**
- **Klikk deg ned gjennom tallene:** Revisor klikker på et tall i avstemmingen mot a-meldingen og følger kjeden ned til lønnslinjen, regelen, timelisten, lederens godkjenning og Faticas kontrollsignatur.
- **Revisorpakken er klar 2. januar** og oppdateres hvis noe rettes senere.

**Suksessmål**

| Mål | Baseline (anslag) | Mål | Måles slik |
|---|---|---|---|
| Andel av revisors forespørsler om lønn som besvares i portalen uten kundens hjelp | ~0 % | ≥ 80 % | Spørreundersøkelse og logg |
| Tid kunden bruker på revisjon av lønn | ukjent | −50 % | Intervju med pilotkunde og revisor |
| Kontroller uten bevis | Vanlig | 0 | Kontrollmatrise |

---

### 2.6 Persona 6 – Liten virksomhet med 10–25 ansatte der daglig leder kjører lønn

**Kontekst**
- Forening, interesseorganisasjon eller AS med ca. 15 ansatte, de fleste på fastlønn og noen timelønnede. Regnskapet ligger i Fiken, Tripletex eller PowerOffice, ofte ført av et byrå. Daglig leder kjører lønnen selv én gang i måneden. Ved 20 ansatte med fastlønn tar det 3–6 timer [D 1.4].
- Mange i denne størrelsen bruker byrå eller lønnsmodulen i regnskapssystemet [D 1.4], [A 3]. Et frittstående lønnssystem er derfor et ekstra system. Det må forsvare plassen sin med trygghet og tidsbesparelse og koste omtrent det samme som PowerOffice (195 kr/mnd + 35 kr per lønnsmottaker [A 3]).
- Vet ikke hva hun ikke vet: trekk betales nå ved hver kjøring [B 4], OTP fra første krone [C 9], arbeidsgiverperioden og refusjon [C 7], feriepenger og trekkfri juni, halv skatt i desember [D 2.3–2.4] og sluttoppgjør [C 10.1].
- Det finnes ingen arbeidsdeling: daglig leder registrerer, godkjenner og betaler, også sin egen lønn.

**Jobs to be done**
1. Når det er lønnsdag, vil jeg bli ferdig på kort tid og vite at alt er riktig, uten å kunne lønnsreglene.
2. Når noe uvanlig skjer (ny ansatt, sykmelding, foreldrepermisjon, permittering, oppsigelse), vil jeg bli tatt gjennom det steg for steg.
3. Jeg vil aldri få tvangsmulkt, renter eller trekk som ikke er betalt.
4. Hvis det blir for mye, vil jeg kunne gi jobben til et byrå uten å bytte system.

**Dagens smerter**

| Smerte | Konsekvens | Kilde |
|---|---|---|
| Endringene i 2026 (trekk ved hver kjøring, KID, Altinn 3 og systembruker) er ukjente for mange | Betalinger og innsendinger kan feile | [B 0], [B 4], [G 2.1] |
| De lette systemene mangler fravær, timebank og automatikk | Manuelt arbeid og feil | [D 8.1] (Tripletex, PowerOffice) |
| Feil i feriepenger og forskuddstrekk i enkelte systemer | Tillitsbrudd | [D 8.1] (PowerOffice, Finago) |
| NettLønn har lavest tilfredshet i markedet (2,9 av 6) | Kunder som kan vinnes | [A 2.3] |
| Ingen fire øyne | Feil og misbruk oppdages ikke | [D 3.2] |

**Behov**

| ID | Behov (konkret) | MoSCoW | Begrunnelse / kilde |
|---|---|---|---|
| VK-58 | **Oppstartsveiviser:** henter data fra Enhetsregisteret, setter opp systembruker i Altinn med statussjekk, kobler bank, regnskap og OTP-leverandør og henter ansatte fra forrige system eller fra a-meldingen | Må | [G 2.1], [F 6.2] |
| VK-59 | **Månedens kjøring som gjøremålsliste** i klarspråk, med fornuftige standardvalg og en tydelig «du er ferdig»-tilstand | Må | [D 1.5] |
| VK-60 | **Automatikk:** skattekort, a-melding, trekkbetaling med KID og påminnelse om AGA-terminer | Må | [B 3], [B 4] |
| VK-61 | **Veivisere for hendelser:** ny ansatt (OTP-innmelding, skattekort, bankkonto lagt inn av den ansatte), sykmelding (telling av arbeidsgiverperioden, inntektsmelding når NAV ber om det, refusjon), foreldrepermisjon, permittering og slutt (sluttoppgjør) | Må | [C 7], [C 10.1], [B 6] |
| VK-62 | **Feriepenger og halv skatt** beregnes automatisk, med forhåndsvarsel og forklaring til ansatte | Må | [D 2.3], [D 2.4] |
| VK-63 | **Rimelighetssperrer:** stopper åpenbare feil (netto 0 eller negativ, manglende skattekort, lønn etter sluttdato, uvanlig mange timer) | Må | [D 1.3] |
| VK-64 | **Kompenserende kontroll når daglig leder er alene:** endringer i egen lønn eller bankkonto varsles automatisk til styreleder eller regnskapsfører | Bør | [D 3.2 pkt. 4] |
| VK-65 | **Regnskapsintegrasjon** mot Fiken, Tripletex og PowerOffice uten oppsett | Må | [D 5.3], [G 1.0] |
| VK-66 | **Ansattapp** med lønnsslipp, feriepenger og kontonummer (endret med BankID) | Må | [D 10.1] |
| VK-67 | **Hjelp fra et menneske:** «spør en lønnsekspert» i appen, og mulighet til å gi et byrå tilgang med ett klikk | Bør | [E 0 pkt. 9], [D 1.5] |
| VK-68 | **Forutsigbar pris** uten moduler (lønn, fravær og app inkludert) | Bør | [A 6.1 pkt. 7], [A 6.2 pkt. 4] |
| VK-69 | **Skattefri organisasjon og AGA-fritak:** akkumulator på 10 000 kr per mottaker, overvåking av fritaksgrensene (800 000 kr totalt / 80 000 kr per ansatt), og varsler | Bør (Må for skattefrie organisasjoner) | [D 7] |
| VK-70 | **Enkel timeliste** for timelønnede og ekstrahjelp når kunden ikke har eget tidssystem. Erstattet av Bruttos timemodul (VK-T01, Må). Telles ikke separat. | → VK-T01 | [D 1.5], kap. 5.4 |

**Det som ville vært kult i 2026**
- **Lønn på 10 minutter fra mobilen:** «Alt ser normalt ut. 1 ny ansatt fikk skattekort automatisk. Godkjenn? → Ferdig. A-melding sendt. Forskuddstrekk 48 210 kr betales automatisk mandag 23.11.»
- **Første sykmelding:** «Vi har talt arbeidsgiverperioden (16 dager) og laget inntektsmeldingen NAV ba om. Sjekk tallene og send. Refusjonen forventes i januar, og vi sier fra hvis den ikke kommer.»
- **Juni uten spørsmål:** De ansatte får automatisk beskjed om at juni-utbetalingen er feriepenger, at det ikke trekkes tabelltrekk og hvorfor netto er høyere.

**Suksessmål**

| Mål | Baseline (anslag) | Mål | Måles slik |
|---|---|---|---|
| Tid per ordinær kjøring | 3–6 t [D 1.4] | < 20 min | Telemetri |
| Trekk betalt for sent / tvangsmulkt | Ny risiko fra 2026 | 0 | Betalingsstatus, Skatteetaten |
| Supporthenvendelser per kunde per måned | ukjent | < 0,3 | Supportsystem |
| Kunder som overleverer til byrå uten å bytte system | – | Mulig på én dag | Pilot |

---

## 3. Tverrgående behov og behov for skala (lagt til i runde B)

Kritikken i runde B (kap. 6) viste at utkastet var skrevet for en virksomhet med 150–400 ansatte og manglet det som avgjør for kunder med opptil 1000 ansatte, i tillegg til migrering og drift. Disse behovene gjelder flere personas.

| ID | Behov (konkret) | MoSCoW | Personas | Begrunnelse / kilde |
|---|---|---|---|---|
| VK-77 | **Migrering uten risiko:** ArbeidsforholdId, permisjoner og saldoer hittil i år videreføres. HiÅ avstemmes mot Skatteetatens avstemmingsdata. 1–2 måneders parallellkjøring der alt som rapporteres, utbetales og bokføres er likt på øret. Navngitt implementeringsansvarlig og en feilgaranti. | Må | 1, 2, 3, 6 | [F 6], [A 6.2], [A 7.1] |
| VK-78 | **Driftssikkerhet i lønnsvinduet:** 99,95 % tilgjengelighet i kritiske perioder, endringsfrys, lønnsfaglig support med utvidet åpningstid rundt lønnsdag, statusside, og varsel om regelendringer («dette endres for dere i januar») | Må | Alle | [F 8.1], [A 6.1 pkt. 5] (SD Worx sin svakhet), [B 12] |
| VK-79 | **Forklart lønnsslipp** (deterministisk, fra beregningssporet): hvorfor netto endret seg, etterbetaling per måned, feriepenger i juni og halv skatt i desember. KI-chat («spør lønnsslippen») er Kan. | Bør | 1, 2, 6 + ansatte | [D 10.1], [G 2.6], [F 5.1] |
| VK-80 | **Lønnsslipp på flere språk** (engelsk, polsk, litauisk, ukrainsk m.fl.) | Bør (helse, omsorg, renhold) | 1, 2 | [D 10.1], [G 3 #37] |
| VK-81 | **SSO med Entra ID og SCIM** for brukere og ledere | Må (250+) | 1, 3, 4 | [D 5.3] |
| VK-82 | **Systemforvalterflate:** testmiljø (sandbox), endringslogg på lønnsarter og regler, testkjøring av konfigurasjonsendringer før aktivering, og egne release notes | Bør (Må 1000) | 1, 2, 5 | [D 3.1] (Bærum), [D 8.3], [G 3 #31] |
| VK-83 | **Ytelse og flere kjøringer:** testkjøring av 1000 ansatte på under 2 minutter, ubegrenset antall testkjøringer, 4–8 kjøringer per måned og 14-dagerslønn for enkelte grupper | Må (ytelse), Bør (14-dagers) | 1, 2 | [D 1.1 steg 6], [D 1.5] |
| VK-84 | **BI og dataeksport** (API/OData) med stabile nøkler og samme tilgangsstyring som i appen | Må (250+), Bør (<250) | 3, 4, 5 | [D 5.2], [D 5.3] |

**Konfidensielle grupper** (toppledelse, styret, lønnsavdelingen selv, ansatte med sperret adresse) dekkes av VK-30 og VK-48. De må også maskeres i kontrollrapporter, bilag og bankfil [D 3.3]. Dette er Må fra 100 ansatte.

---

## 4. Modulene: Utleggsappen, OrgLab og Tikket sett fra virksomhetskunden

Kunden vil ha integrasjonene på like vilkår: egne moduler og kundens andre systemer (Planday, Simployer, Xledger) skal bruke det samme offentlige API-et [G 0 pkt. 5]. For virksomhetskunden betyr modulene dette:

| ID | Behov | MoSCoW | Kommentar / kilde |
|---|---|---|---|
| VK-71 | **Utleggsappen → lønn** (eksternt alternativ til Bruttos egen utleggsmodul, kap. 5.5): godkjente reiseregninger og utlegg kommer inn som lønnsgrunnlag med dimensjoner, med samme kontrakt som egen modul. Lønn eier skatte- og a-meldingsklassifiseringen og sender status tilbake (mottatt, avvist, utbetalt, innrapportert). | Må | [G 1.11 B1]. Avvik mellom regnskap (godkjent) og a-melding (utbetalt) må forklares i avstemmingen [D 5.2]. |
| VK-72 | **Utlegg utbetalt direkte samme dag (vei B)** og likevel rapportert riktig i a-meldingen | Kan | [G 1.11 B1], [G 2.3]. Synlig for ansatte, men ikke kjøpskritisk. |
| VK-73 | **OrgLab → lønn: verv og medlemmer.** Når en organisasjon betaler godtgjørelse for verv (styre, tillitsvalgte, utvalg), møtegodtgjørelse eller kompensasjon for tapt arbeidsinntekt, skal personen registreres én gang (i OrgLab). Lønn oppretter da et honorararbeidsforhold, henter skattekort og beregner trekk og AGA. Frivillige som bare får dekket utlegg, går via Utleggsappen og er ikke lønn. | Bør (Må for organisasjoner med mange verv) | [D 7]. **Rapporteringsform for tapt arbeidsfortjeneste må verifiseres per type.** Skatteetaten slår fast at kompensasjon for tapt arbeidsfortjeneste er skattepliktig inntekt [Skatteetaten, se kap. 11]. |
| VK-74 | **Tikket → lønn: arrangementer.** Honorar til foredragsholdere og artister og timelønn for arrangementsmannskap knyttes til arrangement-ID, slik at lønnskost kan brukes som dimensjon (kost per arrangement). Mottakere som allerede finnes i Tikket, skal ikke registreres på nytt. | Bør | Avledet av [D 7] (honorarer) og [D 6.3] (dimensjoner) |
| VK-75 | **Utenlandske artister:** lønn skal kjenne igjen og stoppe dem i ordinær lønnskjøring. Honorar til utenlandske artister er underlagt **artistskatt** (for tiden 15 %, normalt trekkplikt for norsk arrangør, melding til Skatteetaten senest tre uker før arrangementet). Hele artistskatt-flyten er Ikke nå. | Må (stopp og varsel) | Skatteetaten (kap. 11). Hvordan dette henger sammen med a-meldingen må verifiseres. |
| VK-76 | **Like vilkår og integrasjonsmonitor:** kunden ser hva som kom fra hvilken modul eller hvilket system, hva som feilet og hvorfor | Må | [G 3 #33], [G 0 pkt. 5] |

**Konsekvens for runde 1:** Kontraktene i G (B2 «OrgLab-type → lønn» som HR-modul og B3 «Tikket-type → lønn» som tidsmodul) passer ikke med beskrivelsen av produktene. HR- og tidskontraktene trengs fortsatt, men for tredjepartssystemer (Simployer, Quinyx, Planday). OrgLab og Tikket trenger egne kontrakter for honorar og verv, med **honorarmottaker** som kjerneobjekt og arrangement- og verv-ID som dimensjon.

---

## 5. Egne moduler for ferie/fravær, timer og utlegg (nytt krav etter runde B)

Gründeren har bestemt at lønnssystemet skal ha tre egne moduler:
- **Ferie/fravær:** søknad, godkjenning, saldo, egenmelding og sykmelding.
- **Timer:** registrering, overtid og godkjenning.
- **Utlegg:** reise og kvittering.

Modulene skal bygges på det **samme offentlige API-et** som eksterne systemer bruker, og kunden skal kunne bytte dem ut, for eksempel med Utleggsappen eller et tidssystem. Behovene her har egne ID-er: **VK-M** (felles for modulene), **VK-F** (ferie/fravær), **VK-T** (timer) og **VK-U** (utlegg).

### 5.1 Hva hører hjemme hvor? Grensen mellom lønnskjernen, egne moduler og integrasjon

**Tommelfingerregel:** Alt som har rettsvirkning overfor Skatteetaten, NAV eller den ansattes lønn, skal ligge i **lønnskjernen** og fungere likt uansett hvor dataene kommer fra. Modulene samler inn **fakta og godkjenninger**. Hvis regler som arbeidsgiverperiode, ferietrekk eller skatteklassifisering ligger i en modul, slutter de å virke når kunden bytter modulen ut.

| Funksjon | Lønnskjernen (alltid, uansett kilde) | Egen modul (kan byttes ut) | Kan overlates til integrasjon |
|---|---|---|---|
| Ferie | Ferietrekk, feriepenger, feriepengeavsetning og forpliktelse for ferie som ikke er avviklet | Saldo for feriedager, søknad, godkjenning og ferieoversikt | HR-system eller tidssystem med feriefunksjon |
| Egenmelding | Arbeidsgiverperioden telles som tilstandsmaskin over fraværsepisoder [C 7] | Registrering i appen, telling av kvote og tilfeller, varsel | Tidssystem eller HR-system |
| Sykmelding | Mottak av sykmelding og søknad fra NAVs API [B 6.1], inntektsmelding, refusjonskrav og oppgjørsrapport | Visning, kobling til fraværsepisode, varsel til leder (uten diagnose) | – (myndighetsdelen skal alltid ligge i kjernen) |
| Permisjon og permittering | Kodeverk for a-meldingen (type, prosent, ID) | Søknad og registrering | HR-system |
| Timer | Prising (sats per lønnsart og arbeidsforhold), overtidstillegg, cut-off og låsing | Registrering, overtidsforespørsel, godkjenning og timebank | Vaktplan- og turnussystemer (Quinyx, GAT, Planday, Tamigo) |
| Grensene i arbeidsmiljøloven | Kontroll før lønnskjøring (VK-21) | Varsel allerede ved registrering | Tidssystemets egne regler |
| Prosjekttimer | Kostfordeling, sosiale kostnader og finansiørrapport (VK-08, VK-10) | Registrering per prosjekt og signering per måned | Prosjekt- eller tidssystem |
| Utlegg og reise | Skatteklassifisering (trekkpliktig eller trekkfri), a-melding og utbetaling («fakta + forslag» [G 1.11 B1]) | Kvittering, reisefakta, satsforslag, godkjenning og dimensjoner | Utleggsappen, kortløsninger (Pleo, Folio), utenlandsreiser og OCR |
| Godkjenningskjede | Lederhierarki og stedfortreder (speilet fra HR-system eller registrert i lønn), beløpsgrenser | Felles godkjenningsinnboks | Eksterne systemer godkjenner i sitt eget grensesnitt |
| Dimensjoner | Hentes fra regnskapet og valideres | Brukes ved registrering | – |
| Revisjonsspor | Kreves fra alle kilder: registrert av, godkjent av, tidspunkt, kildesystem og versjon | Leverer sporet | Må levere det samme sporet via API-et |

### 5.2 Felles behov for modulene (VK-M)

| ID | Behov (konkret) | MoSCoW | Begrunnelse / kilde |
|---|---|---|---|
| VK-M01 | **Samme API for egne moduler og eksterne systemer, uten bakdører.** Lønnskjernen behandler en linje fra egen timemodul og en linje fra Quinyx likt (samme kontrakt, idempotens og validering). | Må | Gründerkrav. [G 0 pkt. 4–5] |
| VK-M02 | **Blanding per ansattgruppe:** for eksempel turnus fra vaktplansystemet, prosjekttimer i egen timemodul og fravær i egen modul for fastlønnede. Kilden settes per datatype og ansattgruppe, og systemet varsler hvis to kilder sender data for samme person og periode. | Må (flere ansattgrupper), Bør (ellers) | Nordlys har både turnus og prosjektfinansierte forskere [D 11.1]. |
| VK-M03 | **Bytte av modul uten tap**, begge veier: saldoer (feriedager, avspasering, egenmeldingsdager og -tilfeller), åpne søknader, pågående fraværsepisoder og historikk overføres. Full eksport. | Må | Kravet om utskiftbarhet er tomt uten dette. [F 6.1] (saldoer er kritiske ved migrering) |
| VK-M04 | **Én godkjenningsinnboks på mobil** for fravær, timer og utlegg, med lederkjede, stedfortreder, beløpsgrenser og påminnelse før cut-off. Når en ekstern kilde brukes, vises status i innboksen, men godkjenningen skjer der. | Må (når egne moduler brukes) | [D 10.2], [G 3 #12] |
| VK-M05 | **Lederhierarki** hentet fra HR-systemet eller registrert enkelt i lønn. NB: OrgLab er medlemshåndtering, ikke organisasjonskart. | Må | [G 1.11 B2], kap. 4 |
| VK-M06 | **Lønnskjernen styrer cut-off og låsing.** Modulene låser perioden når lønnen låses. Etter låsing kommer bare korrigeringslinjer, som går til neste kjøring. | Må | [D 1.1 steg 4 og 9], [G 1.11 B3] |
| VK-M07 | **Felles dimensjoner** (avdeling, prosjekt, finansiør, arrangement) i alle moduler, validert mot regnskapet | Må | [D 6.3], [G 3 #28] |
| VK-M08 | **Revisjonsspor uavhengig av kilde:** hver linje har registrert av, godkjent av, tidspunkt, kildesystem og versjon. API-et krever det samme av eksterne systemer. | Må | [D 4.1], [D 4.2] |
| VK-M09 | **Modulene er inkludert i prisen**, men kan slås av per modul når kunden bruker et eksternt system, slik at kunden ikke betaler dobbelt | Bør | PowerOffice tar ekstra for timer, reise og fravær, og Visma tar ekstra per bruker for Expense [A 3], [A 2.2]. |
| VK-M10 | **Én ansattapp** med lønnsslipp, feriesøknad, egenmelding, timer og utlegg og én innlogging | Må (10–250), Bør (250+ med egne systemer) | [D 10.1], [G 1.2] |

### 5.3 Ferie og fravær (VK-F)

| ID | Behov (konkret) | MoSCoW | Begrunnelse / kilde |
|---|---|---|---|
| VK-F01 | **Ferie:** søknad og godkjenning, saldo i feriedager etter ferieloven og tariff (inkl. avtalefestet femte uke og ekstra uke for ansatte over 60), overført og forskuttert ferie, og varsel om ferie som ikke er avviklet ved årsslutt | Må | [D 2.3], [B 8.1] |
| VK-F02 | **Avviklet ferie styrer ferietrekket i lønnskjernen**, med valgt metode for ferietrekk. Feriepengene eies av lønn. | Må (kjerne) | [C 3.3], [D 2.3] |
| VK-F03 | **Egenmelding i appen** med telling av dager og tilfeller per 12 måneder etter loven eller utvidet avtale (IA), varsel når kvoten er brukt opp og kontroll av opptjeningskravet | Må | [C 7], [B 6.2] |
| VK-F04 | **Sykmelding mottatt digitalt fra NAV** (sykmelding og søknad via API) og koblet til fraværsepisoden med sykmeldingsgrad | Må | [B 6.1] |
| VK-F05 | **Arbeidsgiverperioden beregnes i kjernen** (16 kalenderdager, og fravær med mindre enn 16 dager mellomrom slås sammen), uansett om fraværet kom fra egen modul eller et eksternt system. Inntektsmelding sendes når NAV ber om det, og refusjonen følges opp (VK-12). | Må (kjerne) | [B 6.2], [C 7] |
| VK-F06 | **Andre fraværstyper:** sykt barn og omsorgsdager med kvoter, velferdspermisjon, permisjon med og uten lønn, foreldrepermisjon med refusjon og permittering. Alle mappes til permisjonstypene i a-meldingen. | Må | [C 7], [B 6.3] |
| VK-F07 | **Saldoer synlige for den ansatte:** feriedager, egenmeldingsdager, omsorgsdager og avspasering | Må | [D 10.1] |
| VK-F08 | **Helseopplysninger skjermes:** lederen ser fravær og grad, men ikke diagnose. Dette er en egen tilgangspakke for særlige kategorier. | Må | [B 11], [G 1.11 B3] |
| VK-F09 | **Ferieoversikt for leder:** hvem er borte når, og sommerferieplan | Bør | [D 2.1] (juli–august med lav bemanning) |
| VK-F10 | **Fravær per vakt for turnusansatte** | Ikke nå i egen modul | Hentes fra vaktplansystemet (integrasjon) |
| VK-F11 | **Sykefraværsoppfølging** (oppfølgingsplan, dialogmøter) | Ikke nå | HR-system og NAV. Se kap. 9. |

### 5.4 Timer (VK-T)

| ID | Behov (konkret) | MoSCoW | Begrunnelse / kilde |
|---|---|---|---|
| VK-T01 | **Timeliste for timelønnede og ekstrahjelp** (per dag eller uke) med godkjenning før cut-off. Erstatter VK-70. | Må | [D 1.1 steg 3], [D 1.5] |
| VK-T02 | **Prosjekttimer for fastlønnede** (timer per prosjekt og aktivitet), signert av ansatt og leder per måned, som dokumentasjon overfor Forskningsrådet og EU | Må (prosjektfinansierte), Bør (ellers) | Forskningsrådet krever et system for registrering av arbeidstid [D 6.4]. |
| VK-T03 | **Overtid:** forhåndsgodkjenning eller godkjenning i etterkant, valg mellom utbetaling og avspasering, og varsel mot grensene i arbeidsmiljøloven § 10-6 (lovens hovedregel er 10 t per 7 dager, 25 t per 4 uker og 200 t per 52 uker, med minst 40 % tillegg. Verifiser ved avtale om utvidet overtid). Satsene hentes fra lønnsarten. | Må | [D 1.3], [D 10.2], aml. § 10-6 |
| VK-T04 | **Avspasering, timebank og fleksitid** med saldo for den ansatte og lederen | Bør | [C 7], [E 9.2] (timebank er svakt hos PowerOffice) |
| VK-T05 | **Låsing og korrigering:** timer låses når lønnen er kjørt. En rettelse blir en korrigeringslinje i neste kjøring. | Må | [G 1.11 B3] |
| VK-T06 | **Ubekvem arbeidstid** (kveld, natt, helg) beregnes ut fra klokkeslett for timelønnede som registrerer i modulen | Bør | Organisasjoner med arrangementsmannskap (Tikket) |
| VK-T07 | **Mobilregistrering** med arrangement- eller prosjektdimensjon | Bør | VK-74, VK-M07 |
| VK-T08 | **Vaktplan, turnusplanlegging og skifttillegg** beregnet fra planlagte vakter | Ikke nå | Integrasjon (VK-15 til VK-17). Se kap. 9. |
| VK-T09 | **Stempling, GPS og adgangskontroll** | Ikke nå | Tidssystemer |

### 5.5 Utlegg og reise (VK-U)

| ID | Behov (konkret) | MoSCoW | Begrunnelse / kilde |
|---|---|---|---|
| VK-U01 | **Utlegg med kvitteringsfoto,** beløp, mva, kategori, dimensjon og godkjenning. Utbetales i lønnskjøringen eller i en egen utleggskjøring, og kvitteringen følger bilaget til regnskapet. | Må | [D 10.1], [D 1.1 steg 1] (egne reisekjøringer) |
| VK-U02 | **Reiseregning innenlands:** diett etter statens satser og trekkfrie satser, trekk for måltider, kilometergodtgjørelse splittet i trekkfri og trekkpliktig del (5,30 / 3,50 kr/km i 2026) og passasjertillegg, reise med og uten overnatting. Satsene er versjonert. | Må | [C 0.1], [G 1.11 B1] |
| VK-U03 | **Klassifiseringen avgjøres i lønnskjernen** («fakta + forslag»): modulen foreslår, og kjernen bestemmer trekkplikt, AGA og a-meldingsbeskrivelse. Det fungerer likt med Utleggsappen. | Må (kjerne) | [G 1.11 B1] |
| VK-U04 | **Kontroll av policy og dubletter:** beløpsgrenser, manglende kvittering, samme kvittering sendt to ganger (hash) | Bør | [G 1.11 B1] (idempotens), [D 8.1] (lønnsfolk vil ha kontroll av reiseregninger) |
| VK-U05 | **Utlegg for frivillige og ikke-ansatte** (styre, tillitsvalgte, frivillige) uten arbeidsforhold. Ren refusjon er ikke lønn. | Bør (Må for organisasjoner) | [D 7] |
| VK-U06 | **Utenlandsreise** med satser per land og valuta (originalbeløp, kurs og NOK) | Bør | [G 1.11 B1], [G 2.3] |
| VK-U07 | **Automatisk tolkning av kvittering (OCR)** | Kan | Sparer tid, men er ikke kjøpskritisk |
| VK-U08 | **Straksutbetaling av refusjon** | Kan | Samme som VK-72 |
| VK-U09 | **Kortintegrasjon** (Pleo, Folio, firmakort), reisebestilling og avanserte reisepolicyer | Ikke nå | Utleggsappen eller ekstern løsning |

### 5.6 Innebygd eller integrasjon? Vurdering per persona

| Persona | Ferie/fravær | Timer | Utlegg | Må ligge i lønnskjernen uansett | Konklusjon |
|---|---|---|---|---|---|
| **1 Lønnsansvarlig, stiftelse (400)** | Egen modul for de 230 fastlønnede (søknad, saldo, egenmelding). De 170 i turnus og ekstravakter får fravær fra vaktplansystemet. | Egen modul passer godt for de 45 prosjektfinansierte (VK-T02). Turnus kommer fra vaktplansystemet (integrasjon, Må). | Egen modul holder for innenlandsreiser. Utleggsappen ved kortbehov eller mange utenlandsreiser. | Arbeidsgiverperiode og refusjon, ferietrekk og feriepenger, prising av vakter, prosjektfordeling og KLP-grunnlag | **Blandet oppsett. VK-M02 avgjør.** Uten blanding per ansattgruppe må Kari velge mellom vaktplansystemet og egne moduler, og da taper vi. |
| **2 Lønnsmedarbeider, AS (150, skift)** | Tidssystemet (Quinyx o.l.) har ofte fravær for skift. Integrasjon er Må. Egen modul for ca. 20 kontoransatte er Kan, fordi kunden helst vil ha én kilde. | **Integrasjon, Må.** Egen timemodul er ikke aktuell for skift (Ikke nå: VK-T08). | Egen modul, siden det er få som reiser. | Arbeidsgiverperiode for skift (dagsats), mapping og karantene, AML-kontroll før kjøring og underenhet | **Integrasjonskvaliteten avgjør.** Vi skal ikke presse egne moduler på denne kunden. |
| **3 CFO** | Bryr seg ikke om hvilket grensesnitt. Vil ha feriepengeavsetning og forpliktelse for ferie som ikke er avviklet. | Periodisering av godkjente timer som ikke er utbetalt | Beløpsgrenser og attestasjonsregler for utlegg, og at kvitteringen følger bilaget | Godkjenningsregler, dimensjoner, periodisering og avsetninger | **Styringen er innebygd, grensesnittet er valgfritt.** Vil ikke betale dobbelt (VK-M09). |
| **4 HR-sjef** | Fraværsmodulen ligger nærmest HR: saldo, ferieplan, statistikk og foreldrepermisjon (til ARP). **Har kunden Huma, kommer fravær derfra** (VK-H02). Bruttos fraværsmodul tar over først når kunden samler HR og lønn (VK-H11). | Lite relevant | Lite relevant | Kodeverk for fraværstyper → a-melding, arbeidsgiverperiode, aggregert statistikk og skjerming av helseopplysninger | **Fase 1: integrasjon (Må). Fase 2: egen modul (Må for å erstatte Huma).** Sykefraværsoppfølging ligger foreløpig i HR-systemet. |
| **5 Revisor** | Kilden er likegyldig, men sporet må være like godt. | Timelister og godkjenninger må kunne tas ut som stikkprøver. | Kvitteringen er bilag og må oppbevares (bokføringsloven) [B 10]. | Revisjonssporet (VK-M08) og kvittering koblet til bilag | **API-et må kreve revisjonsspor fra eksterne systemer.** Ellers blir integrasjon en kontrollsvakhet. |
| **6 Liten virksomhet (10–25)** | Egen modul, på som standard | Egen modul for timelønnede | Egen modul | Alt automatisk: arbeidsgiverperiode, ferietrekk, klassifisering | **Alle tre modulene er innebygd og inkludert i prisen.** Det er en hovedgrunn til å velge oss framfor lønnsmodulen i regnskapssystemet, der modulene ofte koster ekstra [A 3]. Integrasjon er sjelden aktuelt. |

### 5.7 Kritiske merknader til det nye kravet

1. **Fare for at timemodulen glir inn i turnus og vaktplan.** Grensen må være klar: registrering og godkjenning, ikke planlegging. Ellers konkurrerer vi med Quinyx og GAT på deres hjemmebane.
2. **Egen utleggsmodul mot Utleggsappen.** Utleggsmodulen må holdes enkel (innenlandsreise og kvittering). Utleggsappen kan posisjoneres som oppgradering for kortintegrasjon, utenlandsreiser og automatikk. Felles API sikrer like vilkår.
3. **Regler med rettsvirkning må aldri ligge i en modul** (arbeidsgiverperiode, ferietrekk, skatteklassifisering, a-meldingskoder). Ellers bryter kunden reglene i det øyeblikket hun bytter modul.
4. **«Samme offentlige API» utvider API-et fra dag én.** Det må da også håndtere vedlegg (kvitteringer), saldoer, lederhierarki, tilgangspakker for helseopplysninger og revisjonsspor. Det er mer enn lønnsgrunnlag inn og resultat ut [G 0 pkt. 4].
5. **Dubletter ved blanding.** Uten tydelige regler for hvilken kilde som gjelder per ansattgruppe og datatype (VK-M02), vil samme fravær komme fra to steder.

---

## 6. Hva jeg endret i runde B, og tillegg etter runde B

Utkastet (runde A) hadde ca. 60 behov, og ca. 70 % var merket Må. Kritikken under er skrevet som en erfaren lønnssjef, en CFO og en revisor ville sagt det.

| # | Kritikk av utkastet | Endring | Hvorfor |
|---|---|---|---|
| 1 | **«Lønn på 30 minutter» for 400 ansatte er latterlig.** Tiden går til innhenting, purring og kontroll, ikke til å trykke på kjøreknappen [D 1.4]. | Suksessmålene måler nå faser (import → klar, testkjøring → attestert, korrigeringer etter låsing, henvendelser) per 100 mottakere og mot baseline fra D. «10 minutter» brukes bare for den lille virksomheten. | Målene må kunne måles og ikke være markedsføring. |
| 2 | **«Retro med virkningsdato» er ikke nok.** En lønnssjef med HUK-erfaring spør straks om tillegg som avhenger av timelønn, permisjoner og endret stillingsprosent i perioden, sluttede, inntektsmelding og KLP. | VK-04 er utvidet, og VK-05 (følgevirkninger) er nytt, inkludert korrigert inntektsmelding innen 3 måneder [C 5.4] og KLP-grunnlag. | Dette er der konkurrentene feiler [D 8.1], og det er vårt viktigste bevis. |
| 3 | **«Kontrollsenter med terskler» er generisk.** Alle leverandører sier det. | Kravet er nå at systemet skal **klassifisere årsaken** til hvert avvik ut fra beregningssporet (etterbetaling, permisjon, ny lønnsart, mistenkt duplikat). Målet er andelen avvik som forklares automatisk (≥ 85 %). KI brukes bare til språket [F 5.1–5.2]. | Det reduserer kontrolltiden og kan måles. Det er også det SD Worx-brukerne savner [D 8.1]. |
| 4 | **Vi kan ikke få ledere til å godkjenne.** Utkastet lovet «flere godkjenninger i tide» via app. | VK-02 handler nå om å gjøre konsekvensen av fristen automatisk og synlig (ugodkjent utsettes, ansatt varsles, unntak logges). Godkjenningsflyten for timer eies av tidssystemet. | Flaskehalsen er organisatorisk [D 8.2 SAFE]. Lønn kan bare gjøre den smertefri å håndheve. |
| 5 | **Utkastet ville ikke overlevd en kunde med 1000 ansatte.** Det manglet SSO og SCIM, HR som master, BI, systemforvalter og testmiljø, ytelse, 4–8 kjøringer, konfidensielle grupper og nøkkelpersonrisiko. | Kap. 3 er lagt til (VK-81 til VK-84), sammen med VK-38 (co-sourcing med byrå) og VK-44 som Må for 250+. | [D 1.5], [D 3.1], [D 5.3] |
| 6 | **Migrering og support manglet.** Det er de reelle byttebarrierene. | VK-77 (migrering likt på øret) og VK-78 (drift i lønnsvinduet og support) er lagt til som Må og står høyt på topp 20. | [A 6.2], [A 7], [F 6.5], [F 8.1] |
| 7 | **Mye var egentlig «fint å ha».** | Nedgradert: pottfordeling (Må → Kan), finansiørformat for Forskningsrådet og EU (Må → Bør), KI-chat på lønnsslippen (Bør → Kan), løpende forhåndsberegning (Bør → Kan), feriepengeprognose og totalkompensasjon (tatt ut av personas), «sykefraværsradar» (omformulert til kost og refusjon, Bør). | Dette vinner ikke kontrakten. Det reduserer henvendelser, som utgjør 5–10 % av tiden [D 1.4]. |
| 8 | **ARP ble lovet for mye.** Ufrivillig deltid finnes ikke i lønnsdata, og stillingskategorier for «arbeid av lik verdi» er sjelden definert. | VK-42 sier tydelig hva lønnsdata dekker. VK-43 krever at kunden kan definere kategoriene. Lønnsgap-pakken er Kan til direktivet er tatt inn i EØS-avtalen. | [G 2.2]: ikke selg det som lovkrav før det er det. |
| 9 | **Den lille virksomheten var behandlet som et eget kjernesegment.** Hun har ofte byrå eller lønn i regnskapssystemet, og SoD er umulig. | Persona 6 betjenes av samme produkt i veiledet modus. Lagt til: kompenserende kontroll mot styreleder (VK-64), overlevering til byrå (VK-67) og prisforventning. Ingen egne funksjoner bare for dette segmentet. | [A 6.2 pkt. 6]: vinn 30–150 ansatte først. |
| 10 | **Revisorpersonaen antok at alle har revisor og ber om ISAE.** | Presisert: viktigst for stiftelser og 50+ ansatte. ISAE er Må fra 250+. Eksport av rådata er lagt til (VK-52). | [D 4.3], [F 4.2] |
| 11 | **Modulene var misforstått i runde 1.** G behandlet OrgLab som HR-modul og Tikket som tidsmodul. | Kap. 4 er skrevet om etter oppdragsgivers beskrivelse: verv, møtegodtgjørelser og tapt arbeidsinntekt (OrgLab), arrangementshonorar og arrangement som dimensjon (Tikket), og stopp for utenlandske artister (artistskatt). | Riktig produktforståelse. Kontraktene i G må justeres. |
| 12 | **For mange Må.** | Andelen Må i VK-01–84 er redusert fra ca. 70 % i utkastet til 63 % (52 av 83, fordi VK-70 nå er slått sammen med VK-T01), og Må er segmentmerket. 9 av de 52 gjelder bare HUK, 250+, flere enheter eller >50 ansatte. For en typisk kunde med 150 ansatte uten HUK er ca. 44 Må. **Ærlig vurdering:** Andelen er fortsatt høy fordi mye i lønn er lovkrav (a-melding, trekk, AGA, feriepenger). MoSCoW skiller derfor dårlig mellom hygiene og det som skiller oss fra andre. Bruk topp 20 (kap. 7) til å prioritere. | Ellers blir MoSCoW verdiløs som prioriteringsverktøy. |

### 6.1 Tillegg etter runde B: to nye krav fra gründeren

Etter runde B kom to nye krav. De er tatt inn slik:

**1. Egne moduler for ferie/fravær, timer og utlegg**
- Nytt kapittel 5 med behovene VK-M01–M10, VK-F01–F11, VK-T01–T09 og VK-U01–U09, og en vurdering per persona av hva som må være innebygd og hva som kan overlates til integrasjon (5.6).
- VK-70 (enkel timeliste) er erstattet av VK-T01. VK-24 viser til VK-T04.
- Kap. 9 er justert: «egen reiseregningsmotor» er byttet ut med en enkel egen utleggsmodul. Vaktplan og turnus er fortsatt utenfor.
- Topp 20 nr. 11–12 og øyeblikk 10 er oppdatert.
- **Kritisk merknad:** Regler med rettsvirkning (arbeidsgiverperiode, ferietrekk, skatteklassifisering) skal ligge i lønnskjernen, ikke i modulene. Ellers slutter reglene å virke når kunden bytter modul (5.7).

**2. Integrasjon med Huma, som Brutto på sikt skal erstatte**
- Nytt underkapittel 2.4.1 med behovene VK-H01–H18 i to faser, og en vurdering av om det er et kjøpsargument eller en risiko å samle HR og lønn.
- VK-44 er Må for alle kunder med Huma. Oversiktstabellen i kap. 1 og raden for persona 4 i 5.6 er oppdatert.
- Raden om «full HR-suite» i kap. 9 er byttet ut med en faseinndelt plan. Topp 20 nr. 13 er ny.
- **Kritiske merknader:**
  - Huma oppdaterer i dag bankkonto direkte i Visma.net Payroll [humahr.com]. Brutto skal ikke kopiere dette (VK-H03).
  - Å samle HR og lønn er en risiko som førstesalg og blir først et kjøpsargument når Må-listen for fase 2 er dekket.

**Antall behov etter tilleggene:** 140 i alt.
- 83 gjelder lønn og plattform (VK-01–84 minus VK-70). 52 av dem er Må.
- 39 gjelder egne moduler. 24 av dem er Må, hvorav 4 bare gjelder i bestemte situasjoner.
- 18 gjelder HR og Huma. 4 er Må i fase 1 og 7 er Må i fase 2.

---

## 7. Topp 20 tverrgående behov, rangert

Rangeringen vekter fire ting: (a) om behovet er avgjørende i evalueringen, (b) tid og risiko det fjerner, (c) hvor mange personas det gjelder og (d) hvor godt det skiller oss fra SD Worx, Visma og Intect. Nr. 1–2 er inngangsbilletter, ikke differensiering.

| # | Behov | VK | Personas | Hvorfor så høyt |
|---|---|---|---|---|
| 1 | **Komplett myndighetsintegrasjon 2026:** a-melding-API med forhåndsvalidering og tilbakemelding i klartekst, skattekort, trekkpålegg, NAV-inntektsmelding, avstemmingsrapport og systembruker-veiviser | VK-22, VK-58, VK-60 | Alle | Altinn II-roller opphører 31.12.2026 [B 0]. Uten dette ingen lovlig innsending. |
| 2 | **Utbetaling og trekk etter 2026-reglene** med KID, forfall første virkedag etter, og betalingsstatus | VK-29 | 3, 6, 1 | Ny plikt med strafferisiko. Mange systemer er fortsatt umodne her [D 0.4]. |
| 3 | **Kontrollsenter med automatisk forklarte avvik** (årsak fra beregningssporet), terskler, fire øyne og signering | VK-27, VK-51, VK-63 | 1, 2, 3, 5 | 25–35 % av tiden går til kontroll [D 1.4]. Svak kontroll er et gjennomgående smertepunkt [D 8.1]. |
| 4 | **Førsteklasses retro med følgevirkninger** (tillegg, sluttede, inntektsmelding, KLP) og oppgjørsimport | VK-03, VK-04, VK-05 | 1, 4, 3 | Største enkeltklage [D 8.1], [A 6.1]. Ca. 20 % av timene i en oppgjørsmåned [D 11.3]. |
| 5 | **Godkjenningskjede som låser opp bankfilen**, håndhevet SoD, endringslogg per felt og kontonummerskjold | VK-28, VK-30, VK-31 | 3, 5, 1 | Svindel og revisjonsfunn [D 3.2], [D 4.1] |
| 6 | **Robust import av variable data** med mapping, karantene, idempotens og matching | VK-15, VK-16, VK-17 | 2, 1 | De største feilene oppstår mellom tid og lønn [D 4.4]. 30–40 % av tiden går til innhenting [D 1.4]. |
| 7 | **Migrering uten risiko** (likt på øret, parallellkjøring, garanti) | VK-77 | 1, 3, 6 | Den viktigste byttebarrieren [A 6.2], [A 7] |
| 8 | **Månedlig automatisk avstemming** av lønn, hovedbok, a-melding og bank | VK-34 | 3, 5 | 4–6 t per måned, og typisk revisjonsfunn [D 11.2], [D 4.2] |
| 9 | **Regnskapsbilag med dimensjoner og fordelingsprofiler**, validert mot ERP, med periodisering | VK-08, VK-32, VK-33 | 3, 1 | Kritiske detaljer for alle ERP-integrasjoner [D 5.2] |
| 10 | **Lønnskalender og cut-off-motor** med status per leder og automatisk utsettelse | VK-01, VK-02 | 1, 2 | Den klassiske flaskehalsen [D 11.2], [D 11.4 pkt. 1] |
| 11 | **Fravær og NAV:** arbeidsgiverperiode i kjernen (også for skift), sykmelding og inntektsmelding via NAVs API, refusjonsreskontro mot oppgjørsrapporten, og egenmelding og fravær registrert i egen modul eller hentet fra Huma eller tidssystem | VK-12, VK-20, VK-61, VK-F03–F05 | 1, 2, 6, 3 | Penger går tapt i dag [D 11.2 (25.11)]. Arbeidsgiverperioden må virke uansett kilde (kap. 5.1). |
| 12 | **Egne moduler for timer, utlegg og ferie/fravær som kan byttes ut,** med felles API, blanding per ansattgruppe, bytte uten tap, én godkjenningsinnboks og én ansattapp med forklart lønnsslipp | VK-M01–M04, VK-M10, VK-T01–T03, VK-U01–U03, VK-79 | 6, 1, 3 | Gründerkrav. Avgjørende for kunder uten egne systemer (P6) og for prosjektdokumentasjon (P1), men modulene må ikke låse inne kunder med eget tidssystem (P2) [A 3] (modulene koster ekstra hos konkurrentene). |
| 13 | **HR-integrasjon med Huma først,** med register over hvem som eier attributtene, onboarding som utløser lønnsoppsett og sikret bankkontoendring | VK-H01–H04, VK-44 | 4, 1, 3 | Gründerkrav. Kunder med 100–400 ansatte har ofte et HR-system. Integrasjonen er grunnlaget for å kunne erstatte Huma senere (kap. 2.4.1). |
| 14 | **Organisasjonskompleksitet:** flere juridiske enheter, underenheter, AGA-soner, fribeløp og flytting | VK-14, VK-18, VK-19 | 2, 1, 3 | Feil sone gir feil AGA [D 6.2]. Konsern er vanlig hos stiftelser [D 11.1]. |
| 15 | **Ideell sektor:** tariffbibliotek (Virke HUK, NHO Geneo) med stiger, ansiennitet og opprykk som data, og offentlig tjenestepensjon (KLP-fil, grunnlag og premieavstemming) | VK-06, VK-07 | 1, 3, 4 | Avgjørende for ideell sektor og dårlig dekket i dag [D 7], [D 2.7], [A 6.1 pkt. 6] |
| 16 | **Driftssikkerhet i lønnsvinduet**, lønnsfaglig support og varsel om regelendringer | VK-78 | Alle | SD Worx' tydeligste svakhet, og billig å vinne på [A 6.1 pkt. 5] |
| 17 | **Revisorinnsyn, revisorpakke og ISAE 3402**, og revisjonsspor fra alle kilder | VK-49, VK-50, VK-56, VK-M08 | 5, 3 | Salgskrav fra 250+ [D 4.3] |
| 18 | **Tilgangsstyring og konfidensielle grupper**, med skjerming av helseopplysninger og SSO og SCIM for store kunder | VK-48, VK-81, VK-F08 | 3, 4, 5 | GDPR art. 9-data (fagforening, helse) [B 11]. SSO er Må fra 250+ [D 5.3]. |
| 19 | **Prosjekt- og finansiørkost** med prosjekttimer fra timemodulen, sosiale kostnader synlige før låsing, og retroaktiv omfordeling | VK-08, VK-09, VK-10, VK-T02 | 1, 3 | Klar mulighet for stiftelser og forskning [D 6.4] |
| 20 | **Rapporter og data:** ARP-grunnlag, lederrapport (lønnskost og FTE), BI-eksport og oppgjørsgrunnlag | VK-37, VK-39, VK-42, VK-84 | 4, 3 | Lovkrav for >50 ansatte (ARP), og store kunder vil ha rådata [D 5.3] |

**Like under topp 20:**
- Samle HR og lønn i Brutto (fase 2: VK-H07–H12, VK-H16)
- Honorar og styrehonorar for ikke-ansatte, med verv (OrgLab) og arrangementer (Tikket) (VK-11, VK-73, VK-74)
- Veiledet modus for små virksomheter (VK-59, VK-61)
- Utleggsappen-kontrakten (VK-71, som er Må, men teknisk avgrenset)
- Lønnsslipp på flere språk (VK-80)
- Systemforvalter og testmiljø (VK-82)
- Co-sourcing med byrå (VK-38)

---

## 8. Ti øyeblikk i lønnsmåneden der vi kan vinne kunden

Kalenderen følger Stiftelsen Nordlys i november 2026 (utbetaling fredag 20.11, U = utbetalingsdag) [D 11.2]. Øyeblikk 10 gjelder den lille virksomheten.

| # | Når | Hvem | Hva skjer | Hvorfor det vinner |
|---|---|---|---|---|
| 1 | **Fre 23.10 kl. 07:00 (U-28)** | Kari, 40 ledere | Lønnskalenderen for november går automatisk ut til alle ledere med personlige frister. Kari har en statusside som allerede viser «0 av 40 ferdig». | Kari skriver ikke én e-post om frister. |
| 2 | **Man 9.11 kl. 12:01 (U-11), rett etter cut-off** | Kari, ledere og ansatte | De to lederne som ikke har godkjent, får vaktene sine automatisk utsatt til desember. De berørte ansatte får beskjed med begrunnelse. Kari får en rapport. | Ingen telefonrunde og ingen «kan du ta den med likevel?» uten logg. |
| 3 | **Man 9.11 kl. 13:15** | Ola (lønnsmedarbeider) | Importen fra vaktplanen: «4 812 linjer, 3 trenger deg». Den nye koden «forsterket natt» ligger i karantene med et testberegnet forslag og venter på godkjenning fra Fatima. | Kristiansand-feilen kan ikke skje [D 4.4]. |
| 4 | **Tir 10.11 kl. 09:00** | Ingrid (HR), Ola | Oppgjørsprotokollen for 258 ansatte lastes opp. Systemet melder tre valideringsfeil, beregner etterbetalingen for mai–oktober inkl. tillegg, utelater sju sluttede med begrunnelse og lister 12 sykefravær som trenger korrigert inntektsmelding. | Det tyngste arbeidet i året blir en formiddag [D 11.3]. |
| 5 | **Ons 11.11 kl. 08:15 (U-9)** | Kari, Ola | Testkjøringen har gått automatisk i natt. Avvikslisten er klar: 31 avvik, 28 forklart som «etterbetaling oppgjør 2026», 2 som «permisjon», og 1 flagget som «mistenkt dobbelt nattillegg 14.10». | Kontrolltiden går fra dager til timer, og den ene reelle feilen er det eneste som krever arbeid. |
| 6 | **Ons 11.11 kl. 10:00** | Per (controller), 6 prosjektledere | Hver prosjektleder får sin oktoberkost inkl. sosiale kostnader med en knapp for å bekrefte. EU-prosjektet har fått 20 % for mye. Rettelsen legges inn fra 1.10, før lønnen låses. | Prosjektrapporten stemmer før den sendes til finansiøren, og ingen manuelle bilag trengs [D 6.4]. |
| 7 | **Fre 13.11 kl. 10:00 (U-7)** | Lise (CFO) | Attestasjon på mobilen på 8 minutter: totaler mot forrige måned og budsjett, alle avvik forklart og kontrollert. Hun godkjenner med passkey, og bankfil, forskuddstrekk (KID), utleggstrekk (KID per ansatt) og kreditortrekk lages automatisk med riktige forfall. | CFO-en ser kontrollen, ikke bare tallene. Ingen betaling uten godkjenning. |
| 8 | **Tir 17.11 kl. 10:00** | Ola | A-meldingen for tre selskaper sendes. Feilen med underenhet ble fanget allerede i forhåndsvalideringen 11.11. Tilbakemeldingen kommer etter noen minutter: «Ingen avvik.» | Ingen erstatningsmelding og ingen kryptiske koder [D 11.2 (17.11)]. |
| 9 | **Fre 20.11 kl. 06:00 (U)** | 412 mottakere, lønnsavdelingen | Lønnsslippene forklarer etterbetalingen måned for måned og hvorfor skatten er høyere. Henvendelsene på lønnsdagen faller til en håndfull. Tirsdag 24.11 viser avstemmingen grønt: lønn = hovedbok = a-melding = bank, og trekkene er betalt 23.11 og matchet mot camt.054. | Lønnsdagen er rolig, og CFO-en har avstemt måned uten å vente til januar. |
| 10 | **Søndag kveld før lønnsdag, liten virksomhet** | Daglig leder (15 ansatte) | «Alt ser normalt ut. 2 egenmeldinger og 3 reiseregninger er registrert i appen og godkjent. 1 sykmeldt: arbeidsgiverperioden er talt og inntektsmeldingen er klar. Godkjenn?» Ti minutter på mobilen, deretter «Ferdig: a-melding sendt, trekk betales automatisk mandag 23.11.» | Trygghet for den som ikke kan lønn. Dette er grunnen til å velge et eget lønnssystem framfor lønnsmodulen i regnskapssystemet. |

---

## 9. Det vi bevisst IKKE skal bygge for dette segmentet

| Ikke bygg | Hvorfor | I stedet |
|---|---|---|
| **HR-funksjoner for å erstatte Huma i første versjon** (endret etter gründerens krav om at Brutto på sikt skal erstatte Huma) | Å bytte lønn og HR samtidig er en risiko for kunden (kap. 2.4.1). Bruttos HR-del blir tynnere enn Huma i lang tid. | Fase 1: førsteklasses integrasjon med Huma (VK-H01–H04). Fase 2: bygg Må-listen i 2.4.1 (personalregister, arbeidsavtaler, on- og offboarding, dokumenter, fravær, samtaler og migrering) før erstatning tilbys. |
| **Rekruttering (ATS), HMS og avvik, læringsplattform og avansert prestasjonsstyring** (OKR, 360) | Dette er egne markeder, og Huma dekker dem heller ikke fullt ut. | Integrasjon (for eksempel Teamtailor) (VK-H18) |
| **Sykefraværsoppfølging** (oppfølgingsplan, dialogmøter) | NAV og HR-system eier prosessen. Det er uklart hvor mye Huma dekker. | Fraværsmodulen dekker registrering, egenmelding, sykmelding og arbeidsgiverperiode (VK-F01–F08). Vurderes på nytt i fase 2. |
| **Vaktplanlegging og turnus** | Quinyx, GAT, Planday og Tamigo eier dette. Lønn skal ikke planlegge. | Robust import, mapping og kontroll (VK-15 til VK-17, VK-21). Bruttos timemodul dekker timelister, prosjekttimer og overtid, ikke vakter (VK-T01–T05, VK-T08). |
| **Avansert reise- og utleggsplattform** (kortintegrasjon, reisebestilling, OCR-automatikk, komplekse reisepolicyer) | Utleggsappen og andre eksterne løsninger gjør dette bedre [G 1.11 B1]. | Enkel egen utleggsmodul (innenlandsreise og kvittering, VK-U01–U05) og kontrakt der lønn eier skatteklassifiseringen (VK-U03, VK-71) |
| **Budsjett- og FP&A-verktøy** | Controller bruker eget verktøy | Data, prognose for lønnskost og simulering av oppgjør (VK-35, VK-40) |
| **Egen BI-plattform og dashbordbygger** | Store kunder vil ha rådata, ikke vår grafikk [D 5.2] | API- og OData-eksport (VK-84) og et lite sett standardrapporter |
| **Fullverdig verktøy for lønnsoppgjør** (pottfordeling, lederforslag, forhandlingsflyt) i første versjon | HR-system og Excel dekker det i dag. Lav verdi for kost. | Grunnlag, simulering og validert import (VK-39, VK-40, VK-03) |
| **Autonom KI-kjøring og KI-tolkning av tariff som aktiveres automatisk** | Ansvar, tillit og regulering (KI-loven er utsatt) [F 5.2], [G 2.4] | KI forbereder, forklarer og flagger. Agenter får aldri rett til å godkjenne, sende eller betale. |
| **Lønn på forskudd (EWA), Vipps-utbetaling, sanntidslønn og lønn i flere valutaer** | Hype i dette segmentet, regulatorisk uklart, og det finnes ikke noe API [G 2.3] | Ekstrakjøring (VK-13) og eventuelt arbeidsgiverstyrt forskudd senere |
| **Totalkompensasjon og «økonomisk velvære»** | Vinner ikke kontrakten og har lite norsk etterspørsel [G 2.6] | Forklart lønnsslipp (VK-79) |
| **Statlig og kommunal sektor** (SPK-sertifisering, full KS-hovedtariffavtale, anbudsorganisasjon) i første versjon | Kunder som er låst til eksisterende leverandør, og krever sertifisering [A 6.1 pkt. 8], [B 9.3] | Senere fase. Arkitekturen må tåle det. |
| **Ytelsespensjon og premieberegning** | Leverandøren beregner [C 9] | Riktig pensjonsgrunnlag og fil |
| **Behandling av konkurs og lønnsgaranti** | Skjer normalt ikke i kundens lønnssystem [C 10.3] | Kravoppstilling som eksport |
| **Flyten for artistskatt** (utenlandske artister) | Egen ordning, sjelden i segmentet | Stopp og varsel (VK-75), og henvisning |
| **Full ESRS S1/CSRD** | Segmentet faller nesten helt utenfor etter Omnibus [G 2.7] | Eventuelt en enkel eksport av sosiale nøkkeltall (VSME) senere |
| **Fullstendig pakke for lønnstransparens** (svar på informasjonskrav etter art. 7) før direktivet er tatt inn i EØS-avtalen | Regelverket er ikke vedtatt i Norge [G 2.2] | Datamodellen (VK-43) nå |
| **Kundespesifikk kode, tilpasninger, Citrix eller on-prem** | Dette er grunnen til at kundene forlater SD Worx og Visma Enterprise [D 8.1], [D 8.3] | Konfigurasjon, testmiljø og ren SaaS |

---

## 10. Åpne spørsmål til runde 3

1. **KLP:** Er formatet på lønnsfilen offentlig, og finnes det API? Hvor mange i målgruppen har KLP eller lignende offentlig tjenestepensjon? [A 6.1 pkt. 6] sier at utbredelsen ikke er verifisert.
2. **NAV:** Kan inntektsmelding for foreldrepenger og «sykdom i familien» sendes fra lønnssystem i dag? [B 6.1] beskriver en motstrid mellom NAVs kilder.
3. **OrgLab og Tikket:** Hvordan ser datamodellene ut (person, verv, arrangement)? Hvor mange honorarmottakere har en typisk organisasjonskunde per måned?
4. **Tapt arbeidsfortjeneste og møtegodtgjørelse:** Hvilken a-meldingsbeskrivelse brukes, og er det trekk og AGA, per type mottaker?
5. **Artistskatt:** Hvor mye av ordningen går via a-meldingen i dag?
6. **Validering hos pilotkunder:** baseline-timer per fase, andel avvik som kan forklares automatisk, og om CFO faktisk vil attestere på mobil.
7. **Segment 10–25:** Vil de kjøpe et frittstående lønnssystem, eller kommer de bare via byrå? Test med NettLønn-kunder [A 2.3].
8. **Skattefrie organisasjoner blant stiftelsene:** Hvor mange bruker 10 000 kr-regelen, og hvor ofte går honorarmottakere over grensen?
9. **Huma:** Har Huma et offentlig API eller en partnerordning, og vil de vedlikeholde en integrasjon med en leverandør som på sikt vil erstatte dem? Hvor mye sykefraværsoppfølging dekker Huma, og hvilke HR-funksjoner bruker kunder med 100–400 ansatte faktisk hver uke? (Det avgjør Må-listen for fase 2.)
10. **Egne moduler:** Hvor mange i målgruppen har allerede et tidssystem med fravær (og vil beholde det)? Er en enkel timemodul nok til å dokumentere prosjekttimer overfor Forskningsrådet og i EU-revisjoner?

---

## 11. Kilder

**Runde 1 (scratchpad/research/):** A-marked-konkurrenter.md, B-myndigheter.md, C-beregning.md, D-praksis.md (hovedkilde), E-byra.md, F-arkitektur.md og G-moduler-2026.md. Primærkildene (Skatteetaten, NAV, Regnskap Norges «Lønnssystemer 2025», TED-anbud, Virke/NTL-protokoller m.fl.) står i rapportene.

**Nye søk i runde 2 (28.10.2026):**
- Skatteetaten – Utenlandske artister og idrettsutøvere (artistskatt 15 %, arrangørens trekkplikt, melding tre uker før): https://www.skatteetaten.no/bedrift-og-organisasjon/utenlandsk/utenlandske-artister-og-idrettsutovere/
- Skatteetaten – Lønn og andre ytelser til utenlandske artister (a-meldingsveiledningen): https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/lonn-og-ytelser/oversikt-over-lonn-og-andre-ytelser/lonn-og-andre-ytelser-til-utenlandske-artister
- Skatteetaten – Trekkpliktig stipend (sier at kompensasjon for tapt arbeidsfortjeneste er skattepliktig inntekt. Rapporteringsformen for organisasjoner er ikke avklart): https://www.skatteetaten.no/nn/bedrift-og-organisasjon/arbeidsgiver/a-meldinga/rettleiinga-til-a-meldinga/lonn-og-ytingar/oversikt-over-lonn-og-andre-ytingar/trekkpliktig-stipend/
- Skatteetaten – Skattefrie organisasjoner: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/spesielle-grupper/skattefrie-organisasjoner
- [Uni Micro] Uni Micro – integrasjon med Huma (Humas funksjonsomfang): https://unimicro.no/integrasjoner/huma
- [humahr.com] Huma – produktoversikt: https://humahr.com/productoverview · onboarding: https://humahr.com/knowledge/onboarding · integrasjoner: https://humahr.com/integrations · Visma.net Payroll-integrasjon (synkronisering av ansatte, bankkonto og fravær med hendelseskoder): https://humahr.com/knowledge/visma-net-payroll-integration · nyheter om integrasjoner 2024 (fraværssynk mot Tripletex og Visma): https://humahr.com/blog/huma-news-3-2024
- [Teamtailor] Teamtailor – Huma-integrasjon: https://integrations.teamtailor.com/nl/integrations/huma-hr
- Capterra – Huma (integrasjoner og brukeromtaler, tredjepart): https://www.capterra.co.uk/software/1064929/huma

**Begrensninger:** Huma-beskrivelsen bygger på leverandørens egne sider og tredjepartssider, ikke på test av produktet. Personas 2–6 er sammensatte og bygger på D-rapportens erfaringsbaserte beskrivelser, ikke på intervjuer. Baselinetallene er anslag. Satser for Forskningsrådet, rapporteringsformen for tapt arbeidsfortjeneste og artistskatt i a-meldingen er ikke verifisert.
