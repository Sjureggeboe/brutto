# E – Regnskapsbyråer som salgskanal for et nytt lønnssystem

**Dato:** 28. oktober 2026
**Oppdrag:** Kartlegge hvordan autoriserte regnskapsforetak (heretter «byråer») leverer lønn i dag, hvilke regler og krav som styrer leveransen, hva byråene krever av et lønnssystem, prisnivåer og partnerøkonomi, markedsstørrelse, lisensmodeller og en anbefalt go-to-market (GTM) for en ny, frittstående SaaS-aktør (kunder med 10–1000 ansatte).

**Merking av påstander**
- **[V]** = verifisert mot primærkilde (lovtekst, standard, myndighetsside, leverandørens eller byråets egen side) i denne runden.
- **[S]** = sekundærkilde eller søkesammendrag. Ikke lest i primærkilden, eller primærkilden var utilgjengelig. Bør dobbeltsjekkes.
- **[A]** = anslag eller egen faglig vurdering. Beregningsmåten står oppgitt.

**Begrensning:** Søkekvoten for økten ble brukt opp underveis. Noen områder ble derfor dekket tynnere enn ønsket: Vismas partnervilkår i detalj, SD Worx Byrå-priser, konkrete integrasjoner i praksissystemer (Tally, Duett, «Kontaktnett»), artikler i Finansavisen, E24 og Revisjon og Regnskap, og Kontali, Amesto, Økonomibistand og Fortytwo/Uniconta. Slike punkter står oppført under «Hull» til slutt.

---

## 0. Sammendrag – de viktigste funnene

1. **Byråmarkedet er stort og konsoliderer raskt.** Ved utgangen av 2024 hadde 2 469 selskaper godkjenning som regnskapsselskap, i tillegg til 352 statsautoriserte regnskapsførere med eget enkeltpersonforetak **[V]**. Bransjen omsatte for 24,6 mrd. kr i 2024 (+5,9 %), og de ti største sto for 38,3 % av omsetningen **[V]**. Aider (størst), Azets og ECIT ligger øverst. Alle tre er PE-eide og kjøper opp aggressivt **[V]**.
2. **Lønn utgjør omtrent 11 % av bransjens omsetning** **[V, Regnskap Norge]**. Det tilsvarer rundt 2,7 mrd. kr i året **[A]**. Vi anslår at byråene kjører omtrent 7–13 millioner lønnsslipper i året **[A]**.
3. **Lønnsystemene byråene bruker i dag er tydelig todelt.** For de største klientene brukes SD Worx Byrå og Visma.net Payroll. De fleste av de største byråene bruker SD Worx for sine største klienter **[V, SD Worx]**, og Azets har valgt SD Worx for storkundesegmentet **[V]**. For små klienter brukes lønnsmodulen i kundens Tripletex- eller PowerOffice-system. Mellom disse er det et gap for klienter med 20–300 ansatte. SMB-verktøyene oppleves som «lettvektere», mens enterprise-verktøyene oppleves som komplekse og ustabile **[V, Regnskap Norges lønnsundersøkelse, mars 2026]**.
4. **Altinn 3 er det store vinduet akkurat nå.** Fra 17. november 2026 kan a-melding, skattekort o.l. ikke lenger sendes med gamle Altinn II-roller **[V, Skatteetaten]**, og alle Altinn II-roller opphører 31. desember 2026 **[V]**. Systemer må bruke **systembruker**. For byråer betyr det en egen **klient-/agent-systembruker**, der klientene knyttes til systembrukeren via API **[V, Altinn/Digdir]**. Leverandøren må selv sørge for innlogging, tilgangsstyring og logging på personnivå **[V]**.
5. **GRFS regulerer i detalj hva byrået skal gjøre ved lønnsoppdrag** (kap. 7, 8 og 12.3) **[V]**. Kunden er ansvarlig for lønnsgrunnlaget, og byrået skal kontrollere at det er rimelig. Utbetalinger skal godkjennes av kunden hvis ikke annet er avtalt. Byrået må ha fire-øyne-rutiner ved betalingsfullmakt, og oppdragsdokumentasjonen skal oppbevares i 5 år. Et lønnssystem som «bygger inn» GRFS er et reelt salgsargument.
6. **Partnerøkonomien i markedet er etablert.** Byrået tjener på lisensen. Uni Micro gir byrået 50 % av lisensinntekten **[V]**, Tripletex og PowerOffice gir provisjon **[V]**, og Visma Business NXT sier at byrået skal kunne tjene på lisensen **[V]**. Gratis migrering av klienter er normen («vi flytter klientene dine helt gratis», Tripletex) **[V]**.
7. **Byråene tar typisk 150–250 kr per lønnsslipp eller 250–650 kr per lønnskjøring, pluss 50–100 kr per a-melding og 70–200 kr per sammenstillingsoppgave** **[V, flere byråer]**. Timepris for lønnsarbeid ligger på 990–1 190 kr. Lisenskostnaden er en mindre del av prisen. **Tid per lønnsslipp avgjør byråets margin** **[A]**.
8. **Typiske utløsere for bytte:** tvungen migrering (Visma Lønn ble stengt for lønnskjøring fra 2024, og Huldt & Lillevik legges ned) **[V]**, regelendringer eller Altinn 3, oppkjøp der kjeden standardiserer (Aider bytter regnskaps-, lønns- og kvalitetssystem i oppkjøpte byråer) **[V]**, at et system ikke håndterer større klienter, og at for mange systemer gir for mye manuelt arbeid.
9. **Anbefalt GTM:** Start med 2–3 mellomstore, uavhengige byråer som har en egen lønnsavdeling og klienter med 10–300 ansatte. Gi dem gratis pilot, gratis migrering, en byråmargin på 30–50 % av listepris og innflytelse som designpartner. Planlegg første produksjonsoverføring til **januar 2027** (eller fra og med lønnskjøringen etter feriepengene i juni). Ha Altinn 3-agent-systembruker, masseoperasjoner og GRFS-dokumentasjon på plass fra første dag.

---

## 1. Hvordan byråer leverer lønn i dag

### 1.1 Ansvarsdeling (styrt av GRFS) [V]
GRFS (standard av 21.12.2022, i kraft 1.1.2023) definerer et lønnsoppdrag som registrering av lønnsgrunnlag, utarbeidelse av lønnsdokumentasjon, grunnlag for utbetaling av lønn, feriepenger, trekk og arbeidsgiveravgift, og/eller innsending av a-melding på vegne av oppdragsgiver. Standarden fastsetter følgende:
- **Kunden har ansvaret for lønnsgrunnlaget** med mindre annet er avtalt (GRFS 7.2). Byrået skal påse at grunnlaget er tilstrekkelig og drøfte poster som virker «urimelige eller usannsynlige». Byrået har ikke plikt til å verifisere grunnlaget hvis det er tilfredsstillende dokumentert.
- Byrået skal sørge for betryggende registrering av arbeidsforhold, personopplysninger og lønnsgrunnlag. Det skal særlig se til at a-meldingen har riktige beskrivelser, at satsene for utgiftsgodtgjørelser er riktige, og at beregningskodene for arbeidsgiveravgift er riktige (7.3).
- Skattetrekket skal bygge på innhentede skattekort (7.4). Utleggstrekk og andre trekk skal bygge på skriftlig dokumentasjon.
- Ved hver utbetaling skal byrået lage lønnsdokumentasjon (bilag) (7.5), betalingsgrunnlag (7.6) og en lønnsslipp til hver mottaker (7.7). Byrået skal også lage en årlig sammenstillingsoppgave (7.7).
- **A-melding:** Byrået skal levere i samsvar med oppdragsavtalen, fullmaktene og lovkravene. Avvik i tilbakemeldingen skal følges opp «uten ugrunnet opphold» (7.8).
- **Betaling:** «Utbetalinger skal attesteres/godkjennes av oppdragsgiver, hvis ikke annet er avtalt» (8.6). Den som har bankfullmakt skal ha *egne* tilgangsrettigheter. Byrået *bør* ha arbeidsdeling slik at ikke samme person både registrerer og godkjenner en utbetaling (8.1).
- Kilde: GRFS, https://www.regnskapnorge.no/globalassets/dokumenter/vedtekter/grfs---fom.-2023---masterfil.pdf

### 1.2 Typisk arbeidsflyt for en månedlig lønnskjøring [A, bygger på GRFS, leverandørsider og byråprislister]

| Steg | Når (lønn den 20.) | Hvem | Kanal i dag |
|---|---|---|---|
| 1. Kunden melder endringer: nyansatte, sluttere, lønnsendringer, timer, overtid, tillegg, fravær, reiser og utlegg | Ca. T-10 til T-5 virkedager | Kunden (daglig leder, HR eller avdelingsledere) | E-post med Excel- eller PDF-timelister, kundeportal, timeføringssystem med eksport eller integrasjon, reise- og utleggsapp |
| 2. Byrået registrerer og importerer, og henter oppdaterte skattekort | T-7 til T-4 | Lønnsmedarbeider i byrået | Lønnssystem (byråets eller kundens) |
| 3. Byrået kontrollerer: rimelighet mot forrige periode, avvik og urimelige verdier (GRFS 7.2) | T-4 til T-3 | Lønnsmedarbeider, ev. fire-øyne med kollega eller oppdragsansvarlig | Kontrollrapporter |
| 4. Kunden godkjenner lønnsgrunnlag og forslag (lønnsliste) | T-3 | Kunden | E-post med PDF-lønnsliste eller godkjenning i portal |
| 5. Byrået lager utbetalingsfil (lønn, skattetrekk, utleggstrekk) og bokføringsbilag | T-3 til T-2 | Byrået | Lønnssystem til nettbank eller ERP |
| 6. **Betaling godkjennes** | T-2 til T-1 (avhenger av bankens frister) | **Normalt kunden** med BankID i nettbank eller ERP. Alternativt byrået med skriftlig fullmakt og egne tilganger | Nettbank, bankintegrasjon (Autopay o.l.) |
| 7. Lønnsslipper distribueres | T | Systemet | E-post, app eller digital postkasse |
| 8. Bokføring av lønnsbilag i kundens regnskap | T til T+5 | Byrået | Integrasjon eller fil til kundens regnskapssystem |
| 9. **A-melding** for måneden | **Innen den 5. i måneden etter** | Byrået (systembruker med tilgangspakken «Regnskapsfører lønn») | Fra lønnssystemet via Altinn 3-systembruker |
| 10. Oppfølging av tilbakemelding på a-meldingen og avstemming mot regnskap | T+5 til T+10 | Byrået | Lønnssystem, Skatteetaten |
| 11. Skattetrekk og AGA betales | Annenhver måned den 15. (f.eks. 15. juli for mai og juni) | Kunden eller byrået med fullmakt | Nettbank |

- Ekstern guide oppgir at kundens frist for månedslønn **ofte ligger 5–10 virkedager før lønningsdag** **[S]** (https://accessfinancial.com/no/ordliste/payroll-cut-off-date/).
- Fristen for a-melding (den 5.) og terminen for skattetrekk og AGA (f.eks. 15. juli for mai og juni) er bekreftet av Azets **[V]**: https://www.azets.com/no-no/ressurser/artikler/viktige-frister-innen-regnskap-og-lonn
- Regnskap Norge har avgitt høringssvar på et forslag om at forskuddstrekk skal forfalle **første virkedag etter lønnsutbetaling** og at skattetrekkskonto skal avvikles. Regnskap Norge ba om to virkedager **[S]**. *Jeg har ikke verifisert om forslaget er vedtatt eller når det eventuelt trer i kraft. Dette bør sjekkes fordi det påvirker designet av betalingsflyten direkte.* https://regnskapnorge.no/globalassets/naringspolitikk/horingssvar/2024/regnskap-norge----horingssvar---forslag-om-endret-forfallstidspunkt-for-forskuddstrekk-mv-og-avvikling-av-skattetrekkskonto.pdf

### 1.3 Hvem trykker «betal»?
- **Utgangspunktet er kunden** (GRFS 8.6) **[V]**. Finanstilsynet skriver at digitale systemer der kunden har portaltilgang **reduserer behovet for betalingsfullmakter**: byrået tilrettelegger, og kunden betaler selv **[V]**.
- **Mange byråer har likevel betalingsfullmakt.** I Finanstilsynets tematilsyn (18 byråer, 123 oppdrag med betalingsfullmakt) omfattet 73 % av betalingsoppdragene lønn, og 74 % omfattet skattetrekk og AGA. Ni av 18 byråer hadde verken rutine for eller praksis med arbeidsdeling. Ett byrå delte kodebrikker mellom ansatte, noe som ble vurdert som brudd **[V]**. https://www.finanstilsynet.no/contentassets/759a5db7872849ae817375466fb830e1/regnskapsforeres-betalingsoppdrag---tematilsyn-2018.pdf
- *Det finnes ingen offentlig statistikk over hvor stor andel av lønnsutbetalingene som godkjennes av kunden og hvor stor andel byrået godkjenner med fullmakt.* Mitt anslag er at kunden godkjenner i de fleste tilfeller ved moderne skybasert regnskap med bankintegrasjon, mens fullmakt er vanligere hos små kunder og i borettslag og sameier **[A]**.

### 1.4 Bruker byrået kundens system eller sitt eget? Begge deler.
- **Kunden som lisenshaver (vanligst i SMB-segmentet):** Tripletex, PowerOffice Go og Fiken. Kunden betaler abonnementet, og byrået får gratis tilgang. Tripletex: «Regnskapsførere med en regnskapsførerkonto i Tripletex får gratis tilgang til plattformen» og «Regnskapsføreren din administrerer kontoen» **[V]**. https://www.tripletex.no/priser/
- **Byrået som lisenshaver:** Uni Micro selger komplettlisens per byråbruker med ubegrenset antall klienter, og byrået viderefakturerer klientene **[V]**. SD Worx Byrå er et flerklientsystem som byrået kjører for mange klienter, med portaler for klient, leder og ansatt **[V]**.
- **Standardklausul i oppdragsavtalen:** ECITs klausul om «felles bruk av IT-system» dekker eksplisitt at *enten* kunden *eller* regnskapsforetaket kan være lisenshaver, og fordeler ansvar etter det **[V]**. https://www.ecit.com/no/wp-content/uploads/2026/06/felles-bruk-av-it-system.pdf
- **Skatteetaten:** «Bytter du regnskapsfører er det sannsynlig at du også må bytte lønnssystem» **[V]**. Det tyder på at byrået ofte bestemmer lønnssystemet. https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/arbeidsforholdet/spesielle-forhold/bytte-lonnssystem
- **Byråer kjører ofte flere lønnssystemer side om side** etter klientstørrelse. Skatt & Regnskap AS bruker ulike skysystemer for klienter med 1–400 ansatte, og Visma Payroll for de største **[V]** (https://www.vismasoftware.no/kundehistorier/payroll-gjor-det-enklere-a-handtere-storre-lonnskunder). Regnskap Norges veileder om personvern nevner også eksplisitt bruk av «to lønnssystemer» **[V]**.

### 1.5 Hvilke lønnssystemer brukes? (Regnskap Norges lønnsundersøkelse 2025, publisert 17.3.2026) [V]
298 respondenter. 45 % jobber i regnskapsforetak og 77 % har lønn som primært fagområde. Én person kan bruke flere systemer.

| System | Antall brukere | Total fornøydhet (1–6) | Fornøydhet med sluttbrukerfunksjoner (1–6) |
|---|---|---|---|
| Visma.net Payroll | 106 | 4,6 | 4,5 |
| SD Worx | 103 | 5,4 | 5,1 |
| Tripletex | 76 | 4,9 | 4,6 |
| PowerOffice GO | 72 | 5,1 | 5,2 |
| Xledger | 46 | 4,5 | 4,4 |
| Finago (24SevenOffice) | 31 | 4,6 | 4,6 |
| Duett | 20 | 4,8 | 4,7 |
| Nettlønn | 20 | 2,9 | 2,8 |
| Unit4/Agresso | 18 | 4,2 | 3,9 |
| Unimicro | 14 | 4,4 | – |
| Visma Enterprise HRM | 14 | 3,4 | 3,3 |

Kilde: https://www.regnskapnorge.no/contentassets/b173a1e31cd741af9b610fc80db70ddf/lonnssystemer---resultater-til-publisering.pdf

---

## 2. Regulatoriske rammer for byrået

### 2.1 Regnskapsførerloven (LOV-2022-12-16-90, i kraft 1.1.2023) [V]
https://lovdata.no/dokument/NL/lov/2022-12-16-90
- **§ 2-1:** Regnskapsføring i næring for andre kan bare utføres av regnskapsforetak, det vil si godkjente regnskapsselskap eller statsautoriserte regnskapsførere med ENK.
- **§ 4-1:** Krav til kapasitet, kompetanse og forsvarlig kvalitetsstyring. En statsautorisert regnskapsfører skal ha ansvaret for kvalitetsstyringen.
- **§ 4-2:** Taushetsplikt. Byrået skal hindre at uvedkommende får tilgang. Dette gir krav til tilgangsstyring per klient.
- **§ 5-1:** Byrået skal utpeke en statsautorisert regnskapsfører som **oppdragsansvarlig** for hvert oppdrag.
- **§ 5-2:** Det skal være en **skriftlig oppdragsavtale** for hvert oppdrag og **skriftlige fullmakter** overfor tredjepart, med oversikt over hvilke personer som kan bruke fullmaktene.
- **§ 5-3:** Oppdragsdokumentasjonen oppbevares i **5 år** etter regnskapsårets slutt. Skriftlig kommunikasjon om lovbrudd oppbevares i 10 år.
- **§ 5-4:** Oppdraget skal utføres etter **god regnskapsføringsskikk**. Vesentlige brudd hos kunden skal tas opp skriftlig.
- **§ 5-5:** Plikt til å frasi seg oppdraget.
- **§§ 6-1 til 6-6:** Tilbakekall, overtredelsesgebyr og straff.

**Konsekvens for gründeren [V + A]:** Ifølge Finanstilsynet er lønnstjenester godkjenningspliktig regnskapsføring når de er en integrert del av kundens regnskapssystem, omfatter pliktig regnskapsrapportering eller oppfyller dokumentasjonsplikten. En ren programvareleverandør er *ikke* regulert, så lenge den ikke «tar ansvar overfor kunden for resultatet av regnskapsføringen» **[V]**. https://www.finanstilsynet.no/tillatelser/regnskapsselskap/hvem-ma-ha-godkjenning-som-regnskapsforetak/
→ **Selg programvare til byråer. Ikke selg «lønn som tjeneste» med resultatansvar uten godkjenning.** Det er også et godt kanalargument: leverandøren konkurrerer ikke med byrået.

### 2.2 GRFS – krav som gjelder lønn, og hva de betyr for systemet [V for kravene, A for systemkonsekvensene]

| GRFS-punkt | Krav | Hva lønnssystemet bør støtte |
|---|---|---|
| 2.3 IT-systemer | Systemene skal sikre at lovkrav kan overholdes. Regnskapsdata skal være «betryggende sikret» mot urettmessig tilgang, tap og endring, også i utkontrakterte systemer. **Lønnssystem er nevnt eksplisitt som kritisk system.** Byrået skal ha en dokumentert beredskapsplan som testes årlig. Eksempler på tiltak er tofaktorautentisering og tilgangskontroll. Kundens tilgang skal begrenses til det som er avtalt | 2FA/SSO, rollebasert tilgang, revisjonslogg, dokumentert beredskap og SLA som byrået kan bruke i sin egen beredskapsplan, eksport og backup |
| 2.4 Taushetsplikt | Tilgang begrenses til dem som trenger den | Tilgang per klient og per medarbeider |
| 3.3 Oppdragsavtale | Separat avtale per juridisk enhet. Avtalen skal angi oppgaver, rapportering og kontaktperson hos kunden | Feltet «oppdragsomfang» per klient, f.eks. hvem som godkjenner og betaler. Kobling til praksissystem |
| 3.4 Fullmakter | Skriftlig fullmakt. Oversikt over fullmakter og hvilke personer som kan bruke dem. Rettigheter skal tilbakekalles ved opphør. **Delegering i bank eller Altinn er ikke nok alene** | Register over fullmakter per klient (Altinn, bank) med personer, gyldighet og varsling ved opphør av ansettelse |
| 5.2 Oppdragsansvar | Oppdragsansvarlig skal sørge for tilstrekkelig kvalitetssikring, også når andre gjør arbeidet. Kontrollnivået er risikobasert, og «de IT-systemer som benyttes» er et moment i vurderingen | Rolle for oppdragsansvarlig, kontroll og signering, risikoflagg per klient |
| 7.1 Kundens interne rutiner | Byrået skal vurdere om kunden har betryggende rutiner for riktig lønn, dokumentasjon, skattetrekkskonto eller bankgaranti, OTP og refusjoner av sykepenger og foreldrepenger | Sjekklister per klient, OTP-kontroll, NAV-refusjonsoppfølging |
| 7.2 Lønnsgrunnlag | Urimelige grunnlag skal drøftes med kunden | **Automatiske rimelighetskontroller** (avvik mot forrige måned, terskler) med dokumentert oppfølging |
| 7.4 Skattetrekk | Skal baseres på innhentede skattekort | Masseinnhenting av skattekort og varsel om manglende skattekort |
| 7.5–7.7 | Bilag, betalingsgrunnlag, lønnsslipp og sammenstillingsoppgave | Standard |
| 7.8 A-melding | Levering etter avtale og fullmakt. Avvik følges opp uten ugrunnet opphold | Status for tilbakemelding per klient, avvikskø og dashbord |
| 8.1 og 8.6 Betaling | Egne tilganger, arbeidsdeling, kunden godkjenner | Skille mellom å registrere og å godkjenne. Godkjenningsflyt der kunden godkjenner |
| 9.3 Kvalitetssikring | Avstemminger, analyser og testet automatikk. Kontrollen kan gjøres av kunden, byrået eller tredjepart, men byrået må se til at den er gjort | Avstemming av lønn mot regnskap og a-melding, med automatisk dokumentasjon |
| 12.2 og 12.3 Dokumentasjon | Lønnsoppdrag krever minst a-melding og sammenstillingsoppgaver i tillegg til fullmakter, kvalitetssikring osv. Dokumentasjonen kan ligge i lønnssystemet, men byrået er ansvarlig | Arkiv i 5 år, også etter at kunden har sluttet. Eksport ved opphør |
| 4.1 og 4.2 Opphør | Regnskapsdata skal utleveres. For regnskapsdata brukes SAF-T Regnskap hvis ikke annet er avtalt | Full eksport av lønnsdata. *Det finnes ikke noe tilsvarende obligatorisk SAF-T-format for lønn* **[A]** |

Merk: Tidligere GRFS (før 2023) krevde avstemming av **skyldig skattetrekk og AGA** ved hver periodiske avslutning. Finanstilsynet viste til dette kravet i en tilsynsrapport fra 2024, og skrev at lovkravene i hovedsak er videreført **[V]**. https://www.finanstilsynet.no/49a292/contentassets/4238fac7aaff4b31a5f4caed943cc7b9/tilsynsrapport-pluss-1-regnskap-as.pdf

### 2.3 Regnskap Norges kvalitetskontroll [V]
Det dokumentbaserte kontrollskjemaet for 2026 ber byrået laste opp rutiner for blant annet **«Utførelse av lønnsoppdrag (jf. GRFS 7)»** og fullmaktsoversikt (Altinn, «Betale lønn, skattetrekk, AGA og MVA – fullmakt»). Regnskap Norge gjennomførte 261 kvalitetskontroller for kontrollåret 2025 **[S]**. https://www.regnskapnorge.no/contentassets/8e5067b14da943d4b109d0c5879499a1/kontrollskjema-foretak-2026-dokumentbasert---med-henvisning-til--ks-komplett.pdf

### 2.4 Hvitvaskingsloven (KYC)
- Regnskapsførere er rapporteringspliktige (hvitvaskingsloven § 4 nr. 2 b). De skal ha en virksomhetsinnrettet risikovurdering, gjennomføre kundetiltak (§§ 10–20) og løpende oppfølging (§ 24) **[S, Finanstilsynets veiledning 2019]**. https://finanstilsynet.no/nyhetsarkiv/rundskriv/2019/veiledning-om-regnskapsforeres-og-regnskapsforerselskapers-etterlevelse-av-hvitvaskingsregelverket
- I 2024 fikk 3 regnskapsforetak overtredelsesgebyr for brudd på hvitvaskingsloven **[V]**.
- **Relevans for lønnssystemet [A]:** KYC er byråets plikt og ligger normalt i praksissystemet (Sticos Oversikt, PowerOffice Quality). Lønnssystemet trenger ikke egen KYC-modul. Lønnsdata kan likevel gi signaler til *løpende oppfølging*, for eksempel lønn til personer uten arbeidsforhold, uvanlig store utbetalinger, mange korte arbeidsforhold eller utbetaling til utenlandske kontoer. En enkel funksjon for å eksportere slike signaler til praksissystemet er et pluss, men ikke et krav.

### 2.5 Personvern
- Standard leveransevilkår fra Regnskap Norge: **Kunden er behandlingsansvarlig og regnskapsbyrået er databehandler** **[V]**. https://www.regnskapnorge.no/contentassets/c7363c239fce4751b8ece8fc27f00c91/standard-leveransevilkar.pdf
- Regnskap Norges veileder (2020) slår fast at byrået skal dokumentere oppbevaringssted (land og system) for alle leverandører og underleverandører, og ha databehandleravtaler gjennom hele kjeden. Hvis systemene mangler innebygd personvern og leverandøren ikke retter det, **«må regnskapsførervirksomheten bytte systemer»** **[V]**. Større byråer skal begrense tilgangen til de teamene som jobber med oppdraget, mens egne lønnsavdelinger som betjener mange kontorer har et legitimt behov for tilgang **[V]**. https://www.regnskapnorge.no/contentassets/d1e263a4d94542668b2ad099a3c2fc52/veiledning-for-behandling-av-personopplysninger-i-regnskapsbransjen-v1_1.pdf

### 2.6 Finanstilsynets tilsynsfunn
- **2024:** 39 tilsyn (36 risikobaserte). 10 vedtak om å tilbakekalle godkjenning som regnskapsselskap, 6 om å tilbakekalle godkjenning som statsautorisert regnskapsfører, og 1 suspensjon **[V]**. https://www.finanstilsynet.no/publikasjoner-og-analyser/arsrapport/arsrapport-2024/rapporter-fra-tilsynsomradene-for-2024/regnskapsvirksomhet
- **Gjentakende funn [V]:** manglende eller fraværende kvalitetssikring på oppdragene, mangelfull avstemming og dokumentasjon av balansekontoer, oppdragsansvarlige uten gyldig godkjenning, og for byråenes egen del feil håndtering av skattetrekksmidler (skattebetalingsloven § 5-12). Se for eksempel https://www.finanstilsynet.no/contentassets/058f1189095841fdaa3f8697327cd537/tilsynsrapport-og-vedtak---regnskapsforer.pdf og https://www.finanstilsynet.no/contentassets/edefd0252c6f422da5753e04ecd00eda/tilsynsrapport-regnskapsselskap.pdf
- **Lønnsspesifikt:** Det mest relevante tematilsynet er betalingsoppdragene fra 2018 (se 1.3), der lønn var den største betalingstypen etter inngående fakturaer **[V]**. *Jeg fant ikke noe nyere tematilsyn rettet spesielt mot lønnsoppdrag.*

---

## 3. Fullmakter og Altinn

### 3.1 Tilgangspakker for regnskapsførere i Altinn 3 [V]
- Det finnes tre pakker: **Regnskapsfører med signeringsrettighet**, **Regnskapsfører uten signeringsrettighet** og **Regnskapsfører lønn** (`urn:altinn:accesspackage:regnskapsforer-lonn`, som «lar en regnskapsfører rapportere lønn for klienten»). Pakkene gis **når kunden registrerer regnskapsføreren i Enhetsregisteret**, og bare til autoriserte regnskapsførere. https://docs.altinn.studio/en/authorization/what-do-you-get/accesspackages/business/regnskapsforer/
- Følgende tilgangspakker gir rett til å levere **a-melding**, både i portal og fra system: A-ordningen, Ansvarlig revisor, **Regnskapsfører lønn**, Regnskapsfører med og uten signeringsrettighet, og Revisormedarbeider **[V]**. https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/nye-tilgangspakker-for-a-meldingen/
- Rollene for regnskapsfører overføres automatisk, men **uten garanti for at innholdet blir det samme**. Tilganger som kundene *aktivt* har delegert gjennom Altinn-roller må gis på nytt for å gjelde etter 31.12.2026 **[V, Digdir/Regnskap Norge]**.

### 3.2 Datoer (Skatteetaten og Digdir) [V]

| Dato | Hendelse |
|---|---|
| Des. 2025 | Tilgangspakker for virksomheter lansert |
| 3. mars 2026 | API for klientadministrasjon fra eksterne systemer lansert |
| 31. mai 2026 | Tilgangspakker kreves ved rapportering fra system |
| 19. juni 2026 | Siste frist for å delegere Altinn II-roller. **Filbasert klientdelegering avviklet** |
| 20. okt. 2026 | Kontroll ikke lenger tilgjengelig via Altinn II-roller |
| **17. nov. 2026** | **A-melding, skattemelding, skattekort og skatteoppgjør ikke lenger tilgjengelig via Altinn II-roller** |
| 31. des. 2026 | Alle Altinn II-roller opphører |
| 1. jan. 2027 | Ifølge Tripletex må systemtilgangen ha gyldig tilgangspakke for å sende a-melding **[S]** |

Kilder: https://www.skatteetaten.no/samarbeidspartnere/reetablering-altinn/regnskapsforer-revisor/ · https://www.skatteetaten.no/en/our-partners/reetablering-altinn/systemleverandor/ · https://www.regnskapnorge.no/globalassets/a3-for-regnskapsforere-1.pdf · https://www.revisorforeningen.no/fag/nyheter/altinn-3-klientdelegering-pa-fil-avvikles-og-erstattes-av-ny-funksjonalitetny-side/

### 3.3 Klientadministrasjon og klientdelegering [V]
- Klientadministratoren i byrået bestemmer hvilke ansatte (og systemer) som har tilgang til hvilke klienter. Byrået kan nå **videredelegere** tilgangspakker som kunden har gitt det. Hvis kunden trekker delegeringen, forsvinner også klientdelegeringene automatisk.
- **Filbasert massedelegering er avviklet** og erstattet av et **API** som systemleverandører kan bygge inn: legge til brukere, gi klientrettigheter og liste hvem som har tilgang til en klient. Digdir sier at det er opp til systemleverandøren å ta API-et i bruk, og at BDO og PwC tester egne integrasjoner.
- Revisorforeningen påpeker at sluttbrukersystemer som bruker systembruker ikke trenger klientadministrasjon på ansattnivå i Altinn. Det holder å sørge for at systembrukeren har tilgang til klienten **[V]**.

### 3.4 Systembruker. Slik sender byrået a-melding for hundrevis av klienter [V + A]
- En **systembruker** er en upersonlig bruker basert på Maskinporten. Den erstatter virksomhetssertifikat og virksomhetsbruker. **Tilgangspakker kreves for alle Skatteetatens tjenester ved innsending fra system** **[V]**.
- Det finnes to typer systembruker: **standard** (for virksomhetens egne tjenester) og **agent/klient** (for virksomheter som opptrer på vegne av klienter) **[V]**. https://docs.altinn.studio/en/authorization/guides/system-vendor/system-user/userscenarios/
- **Flyten for et byrå [V]:**
  1. Leverandøren registrerer systemet i Altinns systemregister med påkrevde tilgangspakker og ber om scopes i Maskinporten. Systemet testes i TT02.
  2. Leverandøren eller systemet sender en forespørsel om å opprette en systembruker for klientforhold med én tilgangspakke, f.eks. `regnskapsforer-lonn`. Byrået godkjenner.
  3. Byråets klientadministrator knytter klientene til systembrukeren (i Altinn-portalen eller via API i lønnssystemet). For registrerte klienter delegeres tilgangen automatisk.
  4. Systemet henter Maskinporten-token for systembrukeren og sender a-melding eller henter skattekort per klient (organisasjonsnummer).
  - API-et for klientdelegering kan liste, legge til og fjerne klienter, men har **foreløpig ikke paginering** **[V]**. https://docs.altinn.studio/en/authorization/guides/system-vendor/system-user/client-delegation/
- **Leverandørens ansvar [V]:** Det offentlige vet ikke hvilken person som står bak en innsending. Leverandøren må derfor ha gode rutiner for autentisering og autorisasjon og sørge for at bare autoriserte ansatte kan bruke tokenene til systembrukeren. Behovet for logging på personnivå må håndteres av sluttbrukersystemet. Skatteetaten skriver at det er leverandørens ansvar, i samarbeid med kunden, å sørge for at bare de som skal ha tilgang faktisk har det.
- **Anbefaling [A]:** Én agent-systembruker per byrå og tilgangspakke («Regnskapsfører lønn»). Bygg inn klientadministrasjon i produktet: «legg til klient» skal også knytte klienten i Altinn. Kjør a-melding og skattekort som **masseoperasjoner** med kø, retry og statusdashbord. Logg hvilken ansatt i byrået som utløste hver innsending, for å oppfylle GRFS 3.4 og 2.3 og personvernkravene. Lagre fortsatt den **skriftlige fullmakten** fra kunden (GRFS 3.4), fordi Altinn-delegering ikke er nok alene.

---

## 4. Byråenes funksjonelle krav (forskjellen fra direkte kunder)

Benchmark fra SD Worx Byrå **[V]**: ett system for alle klienters lønnskjøringer. Byrået kan automatisere **kjøreplaner, periodeplaner og kontroller**, og har rollebasert tilgang. Kunden leverer og godkjenner lønnsgrunnlaget i systemet, og det finnes ansatt-, klient-, leder- og byråportal. Løsningen er ISO-sertifisert (bl.a. 27701) og lagrer data i Norden. https://www.sdworx.no/nb-no/vare-losninger/lonn/lonnssystem-regnskapsbyra
Benchmark fra Unimicro Byrå **[V]**: samlejobber for å gi mange ansatte tilgang til mange selskaper, oppgaveliste på tvers av klienter, og fakturagrunnlag fra timer og systemkostnader per klient, med samlefakturering. https://unimicro.no/moduler/byra
Benchmark fra PowerOffice-partnere **[V]**: brukerstyring på tvers (aktivere og deaktivere brukere og endre roller fra ett sted) og «full oversikt over kundene». https://www.poweroffice.no/partner/

| # | Krav | Prioritet [A] | Begrunnelse og kilde |
|---|---|---|---|
| 1 | **Flerklientarkitektur med byråhierarki** (byrå → avdeling/kontor → klient → juridisk enhet/underenhet), konsernstøtte | Må | Byråer kjører hundrevis av klienter. GRFS krever avtale per juridisk enhet |
| 2 | **Én innlogging og rask bytting mellom klienter**, SSO (Entra ID), 2FA | Må | GRFS 2.3 (2FA nevnt) og effektivitet |
| 3 | **Klientdashbord**: status per klient (grunnlag mottatt, kontrollert, godkjent av kunden, utbetalt, a-melding sendt og tilbakemelding OK, avvik), frister og ansvarlig | Må | GRFS 7.8 (oppfølging uten ugrunnet opphold). SD Worx og Unimicro har dette |
| 4 | **Masseoperasjoner**: hent skattekort for alle, send a-melding for alle, kjør lønn etter kjøreplan, generer sammenstillingsoppgaver, oppdater satser (f.eks. G, km-sats) | Må | Altinn 3-agent-systembruker. SD Worx: kjøreplaner og periodeplaner |
| 5 | **Byråmaler**: standard lønnsarter, kontoplanmapping, kontroller og rapporter som klientene arver, med lokale unntak | Må | Standardisering. Aider bytter systemer for å standardisere (se 9) |
| 6 | **Kundeportal**: kunden laster opp eller legger inn timer og endringer, **godkjenner lønnsgrunnlag og lønnsliste**, ser rapporter. Lederportal og ansattapp for lønnsslipp, fravær, reise og utlegg | Må | GRFS 7.2 og 8.6. SD Worx-portaler. PowerOffice får ros for samarbeidet med klienten i appen (RN 2026) |
| 7 | **Fire-øyne og kvalitetssikring**: skille mellom den som registrerer og den som godkjenner. Kontroll og signering fra oppdragsansvarlig. Automatiske rimelighetskontroller (avvik mot forrige periode, negative beløp, manglende skattekort, feil AGA-sone). Logg som dokumentasjon | Må | GRFS 5.2, 7.2, 8.1, 9.3 og 12.2 |
| 8 | **Rollebasert tilgang per medarbeider og klient**, tidsbegrenset tilgang, revisjonslogg | Må | Regnskapsførerloven § 4-2, personvernveileder, GRFS 2.4 |
| 9 | **Altinn 3**: agent-systembruker, klientadministrasjon via API, a-melding, skattekort, tilbakemeldinger, NAV-refusjoner og inntektsmelding | Må | Se kap. 3 |
| 10 | **Integrasjon mot ulike regnskapssystemer per klient**: Tripletex, PowerOffice Go, Visma eAccounting og Business NXT (åpent API og GraphQL **[V]**), Fiken, Xledger, Finago/24SevenOffice, Uni Micro. Bokføring av lønnsbilag med mapping per klient, og fil som reserve | Må | Byrået velger ofte ikke kundens regnskapssystem. Brukerne i RN-undersøkelsen kritiserer svak integrasjon mot regnskap (Visma Payroll) |
| 11 | **Bank**: utbetalingsfil eller -integrasjon som kunden godkjenner, og alternativt flyt der byrået har fullmakt | Må | GRFS 8 |
| 12 | **Import av timer** fra timeføringssystemer og standardisert Excel-import (flere importer per kjøring) | Må | Tripletex kritiseres for at det bare kan gjøres én import før systemet oppretter en ny kjøring (RN 2026) |
| 13 | **Retro og korrigeringer** som avstemmer skattetrekk og AGA tilbake i tid uten manuelt arbeid | Må | Største kritikk mot Visma Payroll i RN 2026 |
| 14 | **Dokumentasjonsarkiv i 5 år** per klient (a-meldinger, sammenstillingsoppgaver, godkjenninger, kontroller), også etter at kunden har sluttet. Full eksport | Må | Regnskapsførerloven § 5-3, GRFS 12.3 og 12.7 |
| 15 | **Timeføring og fakturagrunnlag for byrået**: antall lønnsslipper, kjøringer, a-meldinger og ekstraarbeid per klient og måned, eksportert til praksissystem eller regnskap | Bør | Byråer fakturerer per slipp eller per kjøring (se 5.2). Unimicro Byrå har automatisk fakturagrunnlag |
| 16 | **Integrasjon mot praksissystem**: Sticos Oversikt (integrerer i dag med Tripletex og Business NXT **[V]**), PowerOffice Quality, Maestro (Maestro Soft, årsoppgjør og avstemming **[S]**), Tally og andre. Tilbakemelding om status, frister og timer | Bør | Praksissystemet er der oppdragsavtale, KYC og frister ligger |
| 17 | **Fullmaktsregister** (Altinn, bank) per klient med personer og tilbakekalling | Bør | GRFS 3.4 |
| 18 | **White-label eller «powered by»**: byråets logo og farger på portal, app og lønnsslipp, ev. eget domene | Bør (light), Kan (full) | Kjeder vil eie kundeopplevelsen (Azets har sin egen portal, Cozone **[S]**) |
| 19 | **Migreringsverktøy** fra Visma Payroll, SD Worx, Tripletex, PowerOffice, Xledger og Huldt & Lillevik: ansatte, arbeidsforhold-ID, saldoer, feriepengegrunnlag, trekk | Må for GTM | Skatteetaten krever kontinuitet i arbeidsforhold (se 10.4) |
| 20 | **Sikkerhet og compliance-pakke**: ISO 27001 (og ev. 27701), databehandleravtale-maler, liste over underleverandører, data i EØS/Norden, beredskapsdokumentasjon | Må for de større byråene | GRFS 2.3, personvernveileder. SD Worx markedsfører dette |
| 21 | **Kompleksitet ved 50–1000 ansatte**: tariffavtaler, skift og turnus, timebank, fravær, OTP, feriepenger 60+, flere underenheter og AGA-soner | Må for målsegmentet | Tripletex og PowerOffice kritiseres som «lettvektere». Finago hadde feil i skattetrekk og feriepenger 60+ ved oppstart i 2025 (RN 2026) |

---

## 5. Prismodeller

### 5.1 Hva byråene betaler leverandøren

| Leverandør | Modell | Konkrete tall | Merking |
|---|---|---|---|
| **Uni Micro** (byrålisens) | Per byråbruker (ubegrenset antall klienter) pluss forbruk per klient. Byrået viderefakturerer og **«sitter igjen med halvparten»**. Byrået kan gi inntil 20 % rabatt på veiledende utpris, eller prise høyere | Komplett per byråbruker: 1 343 kr/mnd (1–10 brukere), 1 177 (11–20), 1 104 (21+). Lønnsmodul per klientbruker: innpris 272, veiledende utpris 543. **Lønn per aktiv ansatt: innpris 12 kr (0–49) og 9 kr (50+)**, veiledende utpris 20 og 15 kr. Lønnsgodkjenner per bruker: 28 og 56 kr. Selskap per måned: 75 og 200 kr. Kan bare selges til byråer med næringskode 69.201 | [V] https://unimicro.no/byrapriser |
| **Tripletex** | Kunden betaler listepris. Byrået får **gratis tilgang** og **provisjon** på systemkostnadene (sats ikke oppgitt) | Pro fra 479 kr/mnd (lønn med 1 bruker inkludert). Lønn og reiseregning 65 kr per bruker/mnd. Timeregistrering mot lønn 39 kr per ansatt/mnd. Ingen binding, 3 mnd oppsigelse | [V] https://www.tripletex.no/priser/ og https://www.tripletex.no/for-regnskapsforer/priser/ |
| **PowerOffice** | Sertifiserte partnere er forhandlere med **provisjon etter egen trappemodell** og gratis Quality, timeregistrering og ferie/fravær | Satser ikke offentlige. Sammenligningssider oppgir PowerOffice Go med lønn til ca. 550–700 kr/mnd for 1–3 ansatte | [V] for modellen, [S] for prisen. https://www.poweroffice.no/partner/ |
| **Nettlønn** | Per kjørt lønnsslipp | **39 kr per lønnsslipp** (direkte), reise og utlegg 35 kr per aktiv bruker. Byråpris etter avtale | [V] https://nettlonn.com/priser-nettlonn |
| **Visma Business NXT (byrå)** | Leveres gjennom partnere. «Regnskapsbyrået ditt skal kunne ha en fortjeneste på lisensen» | Ikke offentlig | [V] https://www.vismasoftware.no/erp/business-nxt/regnskapsbyra |
| **Visma.net Payroll** | Ikke offentlig for byrå | – | Hull |
| **SD Worx Byrå** | Ikke offentlig | – | Hull |

### 5.2 Hva byråene fakturerer kunden (2023–2026)

| Byrå | Pris (eks. mva.) | Merking |
|---|---|---|
| Regnskapsfirmaet | **150 kr per lønnsslipp**. A-melding 50 kr. Lønnsarbeid 1 000 kr/t | [V] https://regnskapsfirmaet.no/prissetting/ |
| StyreWeb Regnskap | **190 kr per lønnsslipp eller årsoppgave**. Timepris 1 030 kr. Generelt oppstartsgebyr 2 000 kr | [V] https://www.styrewebregnskap.no/priser/ |
| Millor | **249 kr per lønnskjøring** (fastpris). A-melding 100 kr. Sammenstillingsoppgave 200 kr. Inntektsmelding til NAV 500 kr. Timepris 1 190 kr. Lisenser (24SevenOffice, Tripletex, Xledger) kommer i tillegg | [V] https://millor.no/finn-din-pris/ |
| Arctic Regnskap | **650 kr per kjøring for inntil 10 ansatte**, inkludert a-melding og lønnsslipper | [V] https://www.arctic-regnskap.no/vare-priser/ |
| SpareBank 1 Forretningspartner (2023) | Lønnsarbeid 990 kr/t. Sammenstillingsoppgave 70 kr. Lønnsrådgivning 1 400–1 600 kr/t | [V] https://www.sparebank1.no/content/dam/SB1/bank/ostlandet/vedlegg/Prisliste-web-ForretningsPartner-v3-2023.pdf |
| Guide fra Regnskapsførertjenester.no (2026) | 150–300 kr per ansatt per kjøring. Noen tar oppstartsgebyr | [V] https://www.xn--regnskapsfrertjenester-fjc.no/blogg/outsourcing-av-lonn |
| Regnskapene.no (nå done.ai), Solid Regnskap, Syni | Fra 149 kr per slipp, 250 kr per slipp og 60–120 kr per ansatt/mnd | [S] (sidene var ikke tilgjengelige eller er utdaterte) |

**Typisk prisbilde [A]:** 150–250 kr per lønnsslipp for faste lønninger. Større klienter med mange like slipper får volumrabatt. Kjøringer med variable timer, tillegg og reiser prises opp eller faktureres per time. Tilleggsposter er a-melding (50–100 kr), sammenstillingsoppgave (70–200 kr), inntektsmelding eller refusjon (ca. 500 kr), oppstart (ca. 1 500–5 000 kr per klient) og lisens (viderefaktureres eller betales av kunden).

### 5.3 Marginer [A]
- **Lisensmargin:** Uni Micro dokumenterer 50 %: klienten faktureres 887 kr når byrået betaler 443,5 kr **[V]**.
- **Arbeidsmargin (avgjørende):** En lønningsmedarbeider tjener i snitt 691 200 kr i året (SSB via Regnskap Norge **[V]**). Med sosiale kostnader og ca. 1 500 fakturerbare timer i året gir det en kostnad på rundt **600–650 kr per time** **[A]**.
  - Eksempel: Byrået tar 200 kr per slipp og betaler 40 kr i lisens. Da gjenstår 160 kr til arbeid, som tilsvarer **ca. 15 minutter per slipp** før byrået går i null. For å få 40 % margin på arbeidet må tiden ned mot **ca. 9 minutter per slipp** **[A]**.
- **Implikasjon:** Et nytt lønnssystem bør selges på **«minutter per lønnsslipp»** og **«antall klienter per lønnsmedarbeider»**, ikke på lisenspris. En lisenspris på 20–50 kr per slipp er akseptabel hvis systemet sparer 3–5 minutter per slipp **[A]**.

---

## 6. Partnerprogrammer hos konkurrentene

| | Tripletex | PowerOffice | Uni Micro (også DNB, SpareBank 1 og Eika Regnskap) | Visma (Business NXT / Payroll) | SD Worx |
|---|---|---|---|---|---|
| Nivåer | Partner. Det finnes også «premiumpartnere» **[S]**. Sertifisering | **Sertifisert partner** (minst 20 klienter på Go og én sertifisert superbruker) og **Premium partner** (over 100 kunder på regnskap og faktura, kunder på alle moduler, spisskompetanse) | Partner, Bronze, Silver, Gold og Platinum (1+, 20+, 50+, 100+ og 250+ selskaper) | Partnerkanal (VAR) for NXT. Detaljer ikke offentlige | «SD Worx Byrå»-team. Detaljer ikke offentlige |
| Økonomi | **Provisjon** på systemkostnadene. Gratis tilgang for regnskapsfører | **Provisjon etter trappemodell**. Gratis Quality, timeregistrering og ferie/fravær | Rabatt og kickback. 50 % av lisensinntekten via veiledende utpris | «Fortjeneste på lisensen» | Ikke offentlig |
| Sertifisering | Gratis | Superbrukersertifisering. Mulighet for årlig resertifisering | Gratis digitalt kurs (ca. 8 timer) | Partneropplæring | – |
| Leads og markedsføring | Partnerkart, Regnskapsmatch, felles kampanjer, dedikerte selgere som holder kundemøter. «Nærmere 3000 nye kunder hver måned» | Synlighet for premiumpartnere. Nye kunder sendes direkte. Pilotprosjekter | Promotering og prospekter fra bankene | Partnerdirektorat | Referanser (Aider) |
| Migrering | **Flyttehjelpen: «Vi flytter klientene dine helt gratis»** | – | Oppstartshjelp | Partnerne hjelper. Kundehistorier om overgang fra Huldt & Lillevik | – |
| Hvem eier kundeavtalen? | Kunden (kunden betaler listepris, byrået administrerer) | Kunden, med byrået som forhandler **[A]** | **Valgfritt**: fakturaen kan gå til byrået eller sluttkunden. For DNB og SpareBank 1 Regnskap går den alltid til sluttkunden | Varierer per partner | Byrået (flerklientsystem) **[A]** |
| Kilde | [V] https://www.tripletex.no/for-regnskapsforer/ og https://www.tripletex.no/for-regnskapsforer/flyttehjelpen/ | [V] https://www.poweroffice.no/partner/ (siden oppgir ca. 500 partnerbyråer) | [V] https://unimicro.no/partnerprogram og https://unimicro.no/byrapriser | [V] https://www.vismasoftware.no/erp/business-nxt/regnskapsbyra | [V] https://www.sdworx.no/nb-no/vare-losninger/lonn/lonnssystem-regnskapsbyra |

**Flytting av kunder [V + A]:** Tripletex har ingen binding og 3 måneders oppsigelsestid **[V]**. Standard leveransevilkår fra Regnskap Norge gir byrået krav på 75 % av gjennomsnittshonoraret i oppsigelsestiden hvis kunden går tidligere **[V]**. Det binder kunden til *byrået*, ikke til systemet. Når kunden bytter byrå, bytter den ofte også lønnssystem (Skatteetaten). Konklusjonen er at **byrået, ikke systemleverandøren, i praksis kontrollerer om kunden blir værende** **[A]**.

---

## 7. Markedsstørrelse

### 7.1 Tall [V]
- **Regnskapsforetak:** 2 469 godkjente regnskapsselskap og 352 statsautoriserte regnskapsførere med ENK, til sammen ca. **2 800 foretak**. Det er **12 839 statsautoriserte regnskapsførere** (des. 2024). https://www.finanstilsynet.no/publikasjoner-og-analyser/arsrapport/arsrapport-2024/rapporter-fra-tilsynsomradene-for-2024/regnskapsvirksomhet
- **Omsetning 2024:** 24,6 mrd. kr (+5,9 %). Topp 10 sto for **38,3 %** (Regnskap Norge, 29.10.2025). https://kommunikasjon.ntb.no/pressemelding/18701549/solid-vekst-i-regnskapsbransjen-aider-troner-overst-etter-oppkjopsraid?publisherId=89513&lang=no

| # | Aktør | Norsk omsetning 2024 (1 000 kr) | Vekst |
|---|---|---|---|
| 1 | Aider | 1 604 826 | +52,9 % |
| 2 | Azets | 1 569 327 | +7,4 % |
| 3 | ECIT | 1 297 042 | -4,4 % |
| 4 | Rantalainen | 1 217 752 | +17,2 % |
| 5 | SpareBank 1 Regnskapshuset SMN | 800 218 | +13,6 % |
| 6 | View Group | 747 672 | +73,8 % |
| 7 | Saga/KL | 580 221 | +3,8 % |
| 8 | Accountor/Aspia | 561 606 | +0,6 % |
| 9 | SpareBank 1 Sør-Norge Forretningspartner | 549 732 | +15,5 % |
| 10 | Økoråd | 531 012 | -1,1 % |

(BDO, Kontali, Amesto, Økonomibistand og andre er ikke på topp 10-listen. Tallene deres er ikke hentet.)

- **Lønnsandel:** **11 %** av bransjens omsetning kommer fra lønnstjenester **[V, Regnskap Norge 2026]**. Det gir **ca. 2,7 mrd. kr** i året **[A]**.
- **Lønnsfaget:** Det er nær 4 000 lønningsmedarbeidere (SSB-kategori 4313), og 80 % er kvinner **[V, RN 2026]**.
- **Bruk av ekstern regnskapsfører:** ca. 440 000 virksomheter, rundt 70 % av næringslivet (Regnskap Norge 2021) **[S]**.
- **Volumreferanser:** SD Worx har over 500 000 lønnsslipper per måned i Norge (alle kanaler) **[V]**. Nettlønn har over 30 000 lønnsslipper per måned og over 3 000 kunder **[V]**.

### 7.2 Hvor mange lønnsslipper kjører byråene? [A]
- **Metode 1 (fra omsetning):** 2,7 mrd. kr delt på 200–350 kr i gjennomsnittlig inntekt per slipp (inkl. a-melding, administrasjon og timer) gir **7,7–13,5 millioner slipper i året**, eller 0,65–1,1 millioner per måned.
- **Metode 2 (fra bemanning):** Rundt 2 000–3 500 årsverk på lønn i byråene, som hver behandler 250–400 slipper i måneden, gir 0,5–1,4 millioner per måned.
- **Beste anslag: 0,6–1,1 millioner lønnsslipper per måned (7–13 millioner per år)** gjennom byråer. Usikkerheten er stor. Regnskap Norge kan trolig hjelpe til med å kalibrere tallet.
- **Programvarepotensial i byråkanalen [A]:** 7–13 millioner slipper × 25–50 kr ≈ **175–650 mill. kr i året** i lisensverdi.

### 7.3 Konsolidering [V]
- **Aider:** nær 100 oppkjøp siden 2019. **Bytter «regnskapssystem, lønnssystem og kvalitetssystemer»** i oppkjøpte byråer og bruker en sjekkliste på 248 punkter før fusjon (26.2.2026). Bruker SD Worx Byrå. https://www.okonomi24.com/nyheter/aider-kjoper-ikke-livsverk-vi-kjoper-vilje-og-evne-til-vekst/125377
- **ECIT:** Tatt av børs i 2024 (TowerBrook). Kjøpte virksomheter med rundt 1,2 mrd. kr i omsetning i 2025, bl.a. 50,1 % av SpareBank 1 Sør-Norge Forretningspartner. Har ca. 3 000 ansatte i 11 land. https://www.okonomi24.com/nyheter/nummer-3-ecit/120137
- **Azets:** Tidligere Visma Services, nå britisk/Hg-eid. Valgte SD Worx for storkundesegmentet (17.1.2024). https://www.azets.com/no-no/ressurser/pressemeldinger/azets-inngar-samarbeid-med-sd-worx-lonn
- **Andre:** Rantalainen kjøpte Value Group. Cedra og RSM Norge slo seg sammen (over 1 200 ansatte). Accountor er en del av Aspia. Utenlandske PE-eiere (Vitruvian, Valedo, Hg, PAI, TowerBrook) er tungt inne i bransjen **[V/S]**. https://www.okonomi24.com/nyheter/full-oversikt-dette-er-de-utenlandske-eierne-i-den-norske-regnskapsbransjen/114943

### 7.4 Segmentering for en ny lønnsleverandør [A]

| Segment | Antall (ca.) | Typisk lønnsoppsett | Kjøpsatferd | Prioritet |
|---|---|---|---|---|
| A. Topp 10-kjeder | 10 | SD Worx eller Visma Payroll for store klienter, Tripletex eller PowerOffice for små. Standardiserer sentralt | Sentralt innkjøp, RFP, 12–24 mnd salgssyklus, høye krav til sikkerhet og skala | Senere (år 2–3), men vær på radaren |
| B. Mellomstore uavhengige byråer og regionale kjeder (20–200 ansatte) | ca. 100–200 | Egen lønnsavdeling. 2–4 lønnssystemer side om side. Mange klienter med 10–300 ansatte | Partner eller fagansvarlig for lønn bestemmer. 3–6 mnd salgssyklus | **Beachhead** |
| C. Små byråer (under 10 ansatte) | ca. 2 500 | Kjører lønn i kundens Tripletex, PowerOffice eller Fiken | Prissensitive. Følger kundens system | Bare via selvbetjening |
| D. Bankeide regnskapshus (SpareBank 1, DNB-partnere) | ca. 10–20 | Uni Micro-plattformen og andre | Bankstrategi styrer | Opportunistisk |

---

## 8. Lisensieringsmodeller og juridiske forhold

### 8.1 Modeller

| Modell | Beskrivelse | Fordeler | Ulemper | Eksempel |
|---|---|---|---|---|
| **1. Direkte SaaS med byråtilgang** | Kunden er lisenshaver og betaler. Byrået får gratis tilgang og ev. provisjon | Enkelt å fakturere. Kunden «eier» data. Lav terskel for byrået | Byrået mister lisensmarginen. Kunden kan bytte byrå og beholde systemet, noe byrået ikke liker. Mindre insentiv for byrået | Tripletex, PowerOffice |
| **2. Byrålisens / reseller** | Byrået er lisenshaver eller videreselger og fakturerer kunden med påslag | Byrået får margin (opptil 50 %) og kontroll. Byrået blir en aktiv selger | Leverandøren har ikke direkte kunderelasjon. Byrået får kredittrisiko. Prisene blir mindre transparente | Uni Micro, Visma NXT |
| **3. Flerklientplattform for byrå** | Ett system for byrået med hierarki, masseoperasjoner og klientportaler | Passer byråets arbeidsflyt best (kjøreplaner). Høy byttekostnad gir lojalitet | Krever mer produktutvikling. Ny aktør må ha høy tillit (stabilitet) | SD Worx Byrå |
| **4. White-label** | Byråets merkevare på alt. Leverandøren er usynlig | Attraktivt for kjeder (egen kundeopplevelse) | Dyr support og drift. Leverandøren bygger ingen merkevare. Krever kontraktsvolum | Azets Cozone **[S]** |
| **5. «Powered by»** | Byråets logo og farger, med «drevet av [leverandør]» | De fleste fordelene ved white-label til lav kostnad | Noen kjeder krever full white-label | – |

**Anbefaling [A]:** Bygg **modell 3 (flerklientplattform med byråhierarki)** som teknisk kjerne. Gjør **fakturamottaker fleksibel**, slik Uni Micro gjør: byrået velger per klient om leverandøren fakturerer byrået (modell 2, med byråmargin) eller sluttkunden direkte (modell 1, med provisjon til byrået). Tilby **«powered by»-branding** fra start, og **full white-label** bare til kjeder over en volumterskel.
Hovedgrunnen er at ny aktør trenger byrået som *aktiv selger*, og byråene er vant til å tjene på lisensen. Samtidig vil mange kunder med 50–1000 ansatte ha egen avtale og eget eierskap til data.

### 8.2 Personvern: rollene (behandlingsansvarlig og databehandler) [V for byrå og kunde, A for leverandøren]
- **Kunden (arbeidsgiveren)** er alltid **behandlingsansvarlig** for de ansattes lønnsdata **[V, Standard leveransevilkår 7.2]**.
- **Byrået** er **databehandler** for kunden **[V]**.
- **Leverandøren:**
  - Når **byrået er lisenshaver** (modell 2 og 3), er leverandøren **underdatabehandler** for byrået. Kjeden blir kunde → byrå (databehandleravtale) → leverandør (underdatabehandleravtale som speiler kravene). Byrået må ha kundens forhåndsgodkjenning av underdatabehandleren, typisk en generell godkjenning i oppdragsavtalen, og føre oversikt over databehandlere og oppbevaringssted **[V, RN-veileder]**.
  - Når **kunden er lisenshaver** (modell 1), er leverandøren **databehandler direkte for kunden**, og byrået er en *separat* databehandler som bruker kundens system.
  - Leverandøren må levere: databehandleravtale-maler for begge varianter, liste over underleverandører med land, sikkerhetsdokumentasjon (helst ISO 27001), mulighet for revisjon, avviksvarsling innen 24–48 timer, og sletting eller tilbakelevering ved opphør. Leverandøren må også støtte at byrået oppbevarer *oppdragsdokumentasjon* i 5 år (byrået er da selvstendig ansvarlig etter regnskapsførerloven) **[A]**.

### 8.3 Ansvar ved feil i lønn [V + A]
- **Byrå overfor kunde:** Byrået har profesjonsansvar for egne feil. Etter Regnskap Norges standardvilkår har byrået ikke ansvar for feil som skyldes mangelfull dokumentasjon eller informasjon fra kunden, med mindre byrået åpenbart burde ha oppdaget det. Kunden beholder sitt eget ansvar for korrekt rapportering **[V]**.
- **Systemfeil:** ECITs systemklausul fastsetter at partene (kunde og byrå) **ikke kan holdes ansvarlig for tap som skyldes feil eller mangler i systemleverandørens programvare** **[V]**. **Ansvaret skyves dermed mot leverandøren.** Byråer vil kreve at leverandøren svarer for beregningsfeil i skattetrekk, AGA, feriepenger og a-melding.
- **Anbefaling [A]:**
  - Ha en tydelig ansvarsbegrensning, f.eks. 12 måneders lisensvederlag, men ikke for grov uaktsomhet eller brudd på personvern og sikkerhet.
  - Gi en **«beregningsgaranti»** som differensiator: leverandøren dekker dokumenterte renter, tilleggsskatt og gebyrer som skyldes en påvist systemfeil, ev. med et tak per hendelse.
  - Tegn **ansvarsforsikring** (programvare/IT) og **cyberforsikring**.
  - Unngå formuleringer der leverandøren tar «ansvar for resultatet av lønnsføringen». Det kan utløse godkjenningsplikt (se 2.1).

---

## 9. Hva får byråer til å bytte lønnssystem? Smertepunkter

### 9.1 Dokumenterte utløsere [V]
1. **Tvungen migrering:** «Fra 2024 er det ikke lenger mulig å kjøre lønn fra Visma Lønn» (https://www.vismasoftware.no/visma-lonn). Huldt & Lillevik «skal legges ned», ifølge en kundehistorie (https://www.vismasoftware.no/kundehistorier/byttet-lonnssystem-fra-huldt-og-lillevik-til-payroll). Slike utfasinger skaper store byttebølger.
2. **Oppkjøp og standardisering i kjeder:** Aider bytter regnskaps-, lønns- og kvalitetssystem etter oppkjøp. Azets byttet til SD Worx for storkunder.
3. **Klienter vokser ut av systemet:** Merkantil Service skriver at det gamle systemet ikke var godt nok for mer kompliserte lønnskunder. Skatt & Regnskap AS valgte Visma Payroll for klienter med 50–500 ansatte, og sa at store kunder tar mindre tid der enn små kunder i andre systemer **[V, Vismas kundehistorier]**.
4. **Regelendringer og Altinn 3:** systembruker og tilgangspakker 2026 **[V]**. Ved oppstarten i 2025 hadde Finago feil i bl.a. skattetrekk og feriepenger 60+ **[V, RN 2026]**.

### 9.2 Smertepunkter per system (Regnskap Norges lønnsundersøkelse 2026, kommentarer sammenfattet) [V]
- **SD Worx:** Får ros for lønnsmotor, fleksibilitet, rapporter og fravær. Kritiseres for **ustabilitet etter overgangen til sky**, tung implementering, svak support og dokumentasjon, Citrix-frustrasjon ved import og oppdatering for flere selskaper, og at det er «for åpent» og sårbart for brukerfeil.
- **Visma.net Payroll:** Ryddig og automatisert. Kritiseres for at det er **rigid** på grunn av datostyring, at **retroføringer** skaper store avstemmingsproblemer i skattetrekk og AGA, doble arbeidsprosesser, begrensede rapporter, svak integrasjon mot regnskap og at det er for avansert for små kunder.
- **Tripletex:** Enkelt for små kunder. Kritiseres for lite automasjon, mye manuell registrering, ingen fullverdig fraværsmodul og bare én import per kjøring. Oppleves som dyrt i forhold til funksjonaliteten og som en «lettvekter».
- **PowerOffice Go:** Intuitivt og godt for samarbeid mellom byrå og klient. Kritiseres for at det er tungvint ved avanserte behov (ansatteoppsett, faste lønnslinjer, fravær, timebank) og for feil i feriepenger og kombinerte kjøringer. Ikke laget for større virksomheter.
- **Xledger:** Lønn er tett integrert med økonomi og konsern. Lønnsmodulen kritiseres som tungvint, manuell og utdatert, og for manglende automasjon mot Altinn.
- **Finago:** Har sterkt byråfokus, men er tregt og hadde mange feil ved oppstart i 2025.
- Kilde: https://www.regnskapnorge.no/contentassets/b173a1e31cd741af9b610fc80db70ddf/lonnssystemer---resultater-til-publisering.pdf

### 9.3 Tolkning: muligheten [A]
- Det finnes et **tydelig gap i midtsegmentet (20–300 ansatte)**. Byråene opplever SMB-modulene som for lette og enterprise-systemene som for tunge, rigide eller ustabile. Ingen har vunnet på **«enkelt å bruke + automatisert + byråfunksjoner + robust retro»**.
- Lønnsfolkene vil også ha **AI som kontrollfunksjon** for lønn og reiseregninger, men med trygge rammer **[V, RN 2026]**.
- **Barrierer mot bytte [A]:** opplæring av lønnsteamet, migrering av mange klienter, risiko midt i året (feriepenger i juni, sammenstillingsoppgave i januar), oppsett i Altinn, at kundene må godkjenne nye databehandlere og portaler, og frykt for å være «første byrå» på et nytt system. Stabilitet og support er det som avgjør tilliten.

---

## 10. Anbefalt go-to-market mot byråer

### 10.1 Posisjonering [A]
- **Budskap:** «Lønnssystemet for byråets lønnsavdeling. Halvparten av tiden per lønnsslipp, alle klienter i ett dashbord, GRFS og Altinn 3 innebygd.»
- **Bevispunkter å måle i pilot:** minutter per lønnsslipp, klienter per lønnsmedarbeider, andel kjøringer uten manuell korrigering, avvik på a-melding (mål: 0), og tid fra kundens frist til utbetaling.
- Ikke konkurrer med byrået. Selg programvare, ikke lønnstjeneste. Gi byrået leads fra direktesalg (kunder med 10–50 ansatte som vil ha hjelp).

### 10.2 Valg av pilotbyråer
- **Profil [A]:** 2–3 uavhengige byråer eller regionale kjeder med 20–150 ansatte og egen lønnsavdeling (3–15 personer). De bør ha klienter med 10–300 ansatte og bruke i dag Visma Payroll, SD Worx, Xledger eller Duett, eller ha «for mange systemer». En fagleder for lønn som er misfornøyd med retro, stabilitet eller manuelt arbeid er ideelt.
- **Hvor finne dem:** byråer som har deltatt i Regnskap Norges lønnslag eller lønnsundersøkelse, byråer som har kommentert Altinn 3-overgangen, ECIT- og andre partnerbyråer som ikke er fullt integrert ennå, og byråer som mister systemstøtte.
- **Unngå i fase 1:** topp 3-kjedene (sentrale RFP-er, standardiserer på SD Worx) og helt små byråer (følger kundens Tripletex eller PowerOffice).

### 10.3 Pilotmodell [A]

| Fase | Varighet | Innhold | Kriterium for å gå videre |
|---|---|---|---|
| 0. Avtale og oppsett | 4–6 uker | Pilotavtale med databehandleravtale. Byråmaler for lønnsarter og kontoplan. Agent-systembruker i Altinn TT02, deretter produksjon. Integrasjon mot 1–2 regnskapssystemer klientene bruker | Teknisk godkjenning fra byråets IT og compliance |
| 1. Parallellkjøring | 2 lønnsperioder | 3–5 klienter (10–100 ansatte) kjøres i både gammelt og nytt system. Sammenligning per lønnsslipp, a-melding *ikke* sendt fra nytt system | 100 % samsvar eller forklarte avvik. Byrået signerer |
| 2. Produksjon, liten skala | 2–3 perioder | 10–20 klienter i produksjon med a-melding fra nytt system og kundeportal | Ingen a-meldingsavvik som skyldes systemet. Tidsbesparelse dokumentert |
| 3. Utrulling | 3–6 mnd | 50+ klienter. Hele lønnsavdelingen. Masseoperasjoner | Måltid per slipp nådd. Byråets NPS |

- **Tidspunkt:** Start fase 0 nå (nov.–des. 2026). Gjør **første produksjonsoverføring i januar 2027** (rent inntektsår og ingen overføring av saldo midt i året), eventuelt etter feriepengene (juli 2027). Unngå juni og januar for *store* klienter i første runde.
- **Avtaledokumenter:** pilotavtale, databehandleravtale og underdatabehandleravtale, SLA, beredskapsbeskrivelse til byråets GRFS-beredskapsplan, og en GRFS-matrise (kap. 2.2) som byrået kan bruke i kvalitetskontrollen.

### 10.4 Migrering av klientporteføljen [V for kravene, A for metoden]
- **Arbeidsforhold i a-meldingen:** Skatteetaten tillater tre metoder. **Metode 1 (videreføre)** er best for byråer: samme underenhet, type arbeidsforhold, arbeidsforhold-ID og startdato i nytt system, uten endringer i det gamle. Antall arbeidsforhold per ansatt skal være det samme, og samme arbeidsforhold må ikke sendes fra to systemer for samme periode **[V]**.
- **Hva som må flyttes [A]:** ansatte og arbeidsforhold-ID, faste lønnslinjer, trekk (utleggstrekk, fagforening, OTP), saldoer hittil i år (brutto, forskuddstrekk, feriepengegrunnlag hittil og i fjor, AGA-grunnlag), feriesaldoer, permisjoner og permitteringer, skattekort (hentes på nytt), kontoplanmapping og dimensjoner, samt banksetup.
- **Verktøy:** importmaler og ferdige konvertere fra de mest brukte systemene: Visma.net Payroll, SD Worx, Tripletex, PowerOffice, Xledger og Huldt & Lillevik (for byråer som fortsatt ligger på eksport). Ha en **avstemmingsrapport** for gammelt mot nytt system.
- **Tilbud:** «Vi flytter klientene dine gratis» er markedsstandard (Tripletex). Ta det inn i prisen.

### 10.5 Insentiver for byrået [A]
1. **Gratis pilot** (fase 0–2) og deretter **12–24 måneders prisgaranti** for pilotbyråene.
2. **Byråmargin:** veiledende utpris med **30–50 % margin** for byrået (Uni Micro-modellen), eller provisjon på 15–25 % av lisensen når sluttkunden faktureres direkte.
3. **Gratis migrering og opplæring.** Egen kontaktperson (Tripletex og PowerOffice gjør det samme).
4. **Status som designpartner:** innflytelse på veikartet, tidlig tilgang og ev. små eierandeler eller warrants for 1–2 strategiske byråer (vurder juridisk).
5. **Leads:** send direktekunder som ønsker byrå til partnerne (Tripletex fremhever 3 000 nye kunder i måneden som partnerargument).
6. **Volumtrapp:** Partner, Sertifisert og Premium etter antall klienter og lønnsslipper (f.eks. 10, 50 og 200 klienter) med økende margin, slik PowerOffice og Uni Micro gjør.

### 10.6 Forslag til prismodell [A]
- **Byrå:** *ingen* pris per byråbruker (lønnsmedarbeidere og kontrollører skal være gratis, siden byrået vil ha mange inne). Pris **per kjørt lønnsslipp**: veiledende innpris 25–45 kr med volumtrapp, og veiledende utpris 45–80 kr. Tillegg per klient for portal og app (f.eks. 0–10 kr per ansatt). Ingen oppstartspris.
- **Hvorfor:** Prisen ligger i samme størrelsesorden som Nettlønn (39 kr per slipp) og Uni Micro (12 kr per ansatt pluss brukerlisens), og godt under byråets egen pris på 150–250 kr per slipp. Lisensen blir da en liten del av byråets pris, mens tidsbesparelsen er stor (se 5.3).

### 10.7 Avhengigheter som må være på plass før salg [A]
- Altinn 3: systemregistrering, agent-systembruker, API for klientdelegering, Maskinporten-scopes for a-melding, skattekort og ev. inntektsmelding (NAV). **Produksjonsklart før januar 2027.**
- GRFS-funksjoner (kap. 2.2), masseoperasjoner og et dashbord.
- Integrasjoner mot minst Tripletex, PowerOffice Go og Visma (eAccounting og Business NXT), deretter Fiken, Xledger og Finago.
- Sikkerhetspakke: ISO 27001-veikart, pentest, databehandleravtale-maler, liste over underleverandører og hosting i EØS.
- Support med svartid som byrået merker i lønnsuka, f.eks. responstid under 1 time T-3 til T.

### 10.8 Risikoer [A]
- **Stabilitet og tillit:** Én feil i en lønnskjøring kan koste et byrå en klient. Feilene til Finago i 2025 viser hvor raskt omdømmet påvirkes. Mitigering: parallellkjøring, beregningsgaranti og en egen fagansvarlig for lønn hos leverandøren.
- **Byråer som binder seg:** Kjeder standardiserer, og når Aider eller Azets har valgt SD Worx, er de låst i flere år.
- **Konkurrentenes svar:** Visma (eier både Tripletex, PowerOffice og Visma Payroll **[S]**) kan bunte lønn med regnskap og gi høyere provisjon.
- **Regulatorisk grense:** Ikke selg «lønn levert» med resultatansvar.
- **Altinn 3-avhengighet:** Endringer i API eller tilgangspakker og manglende paginering kan skape problemer ved skala.

---

## 11. Hull og videre arbeid
- **Ikke verifisert eller ikke funnet:** Vismas partnerprogram for Payroll (nivåer, rabatter), SD Worx Byrå-priser og -vilkår, Tripletex' provisjonssatser og nivåer, PowerOffice' trappemodell, integrasjoner for Tally, Duett og «Kontaktnett», data om Kontali, Amesto, Økonomibistand og Fortytwo/Uniconta, nyheter fra Finansavisen, E24 og Revisjon og Regnskap om lønnssmerte, status for forslaget om endret forfall for forskuddstrekk, og fordelingen av hvem som godkjenner betaling (kunde eller byrå med fullmakt).
- **Neste steg:** 10–15 intervjuer med fagledere for lønn i segment B (kan kalibrere tallene i 5.3 og 7.2), henvendelse til Regnskap Norges lønnslag om data, innhenting av prislister fra SD Worx og Visma via byråkontakter, og testtilgang i Altinn TT02.

---

## Kilder (utvalg)
- GRFS (21.12.2022): https://www.regnskapnorge.no/globalassets/dokumenter/vedtekter/grfs---fom.-2023---masterfil.pdf
- Regnskapsførerloven: https://lovdata.no/dokument/NL/lov/2022-12-16-90
- Finanstilsynet, godkjenningsplikt: https://www.finanstilsynet.no/tillatelser/regnskapsselskap/hvem-ma-ha-godkjenning-som-regnskapsforetak/
- Finanstilsynet, årsrapport 2024 (regnskapsvirksomhet): https://www.finanstilsynet.no/publikasjoner-og-analyser/arsrapport/arsrapport-2024/rapporter-fra-tilsynsomradene-for-2024/regnskapsvirksomhet
- Finanstilsynet, tematilsyn betalingsoppdrag: https://www.finanstilsynet.no/contentassets/759a5db7872849ae817375466fb830e1/regnskapsforeres-betalingsoppdrag---tematilsyn-2018.pdf
- Finanstilsynet, tilsynsrapporter: https://www.finanstilsynet.no/contentassets/058f1189095841fdaa3f8697327cd537/tilsynsrapport-og-vedtak---regnskapsforer.pdf · https://www.finanstilsynet.no/49a292/contentassets/4238fac7aaff4b31a5f4caed943cc7b9/tilsynsrapport-pluss-1-regnskap-as.pdf
- Finanstilsynet, hvitvaskingsveiledning: https://finanstilsynet.no/nyhetsarkiv/rundskriv/2019/veiledning-om-regnskapsforeres-og-regnskapsforerselskapers-etterlevelse-av-hvitvaskingsregelverket
- Regnskap Norge, lønnsundersøkelse 2025/2026: https://www.regnskapnorge.no/contentassets/b173a1e31cd741af9b610fc80db70ddf/lonnssystemer---resultater-til-publisering.pdf
- Regnskap Norge, topp 10 2024: https://kommunikasjon.ntb.no/pressemelding/18701549/solid-vekst-i-regnskapsbransjen-aider-troner-overst-etter-oppkjopsraid?publisherId=89513&lang=no
- Regnskap Norge, Standard leveransevilkår: https://www.regnskapnorge.no/contentassets/c7363c239fce4751b8ece8fc27f00c91/standard-leveransevilkar.pdf
- Regnskap Norge, personvernveileder: https://www.regnskapnorge.no/contentassets/d1e263a4d94542668b2ad099a3c2fc52/veiledning-for-behandling-av-personopplysninger-i-regnskapsbransjen-v1_1.pdf
- Regnskap Norge, kontrollskjema 2026: https://www.regnskapnorge.no/contentassets/8e5067b14da943d4b109d0c5879499a1/kontrollskjema-foretak-2026-dokumentbasert---med-henvisning-til--ks-komplett.pdf
- Regnskap Norge og Digdir, Altinn 3 for regnskapsførere: https://www.regnskapnorge.no/globalassets/a3-for-regnskapsforere-1.pdf
- ECIT, klausul om felles bruk av IT-system: https://www.ecit.com/no/wp-content/uploads/2026/06/felles-bruk-av-it-system.pdf
- Skatteetaten, Altinn 3 for regnskapsfører og revisor: https://www.skatteetaten.no/samarbeidspartnere/reetablering-altinn/regnskapsforer-revisor/
- Skatteetaten, systemleverandører: https://www.skatteetaten.no/en/our-partners/reetablering-altinn/systemleverandor/
- Skatteetaten, tilgangspakker for a-melding: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/siste-fra-a-ordningen/nye-tilgangspakker-for-a-meldingen/
- Skatteetaten, bytte lønnssystem: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/arbeidsforholdet/spesielle-forhold/bytte-lonnssystem
- Altinn, tilgangspakker for regnskapsfører: https://docs.altinn.studio/en/authorization/what-do-you-get/accesspackages/business/regnskapsforer/
- Altinn, brukerscenarier for systembruker: https://docs.altinn.studio/en/authorization/guides/system-vendor/system-user/userscenarios/
- Altinn, API for klientdelegering: https://docs.altinn.studio/en/authorization/guides/system-vendor/system-user/client-delegation/
- Revisorforeningen, klientdelegering: https://www.revisorforeningen.no/fag/nyheter/altinn-3-klientdelegering-pa-fil-avvikles-og-erstattes-av-ny-funksjonalitetny-side/
- Tripletex: https://www.tripletex.no/for-regnskapsforer/ · https://www.tripletex.no/priser/ · https://www.tripletex.no/for-regnskapsforer/priser/ · https://www.tripletex.no/for-regnskapsforer/flyttehjelpen/
- PowerOffice: https://www.poweroffice.no/partner/
- Uni Micro: https://unimicro.no/byrapriser · https://unimicro.no/partnerprogram · https://unimicro.no/moduler/byra
- Visma: https://www.vismasoftware.no/erp/business-nxt/regnskapsbyra · https://www.vismasoftware.no/visma-lonn · https://www.vismasoftware.no/kundehistorier/payroll-gjor-det-enklere-a-handtere-storre-lonnskunder · https://www.vismasoftware.no/kundehistorier/lonnssystemet-var-perfekt-match-for-regnskapsbyraet · https://www.vismasoftware.no/kundehistorier/byttet-lonnssystem-fra-huldt-og-lillevik-til-payroll
- SD Worx: https://www.sdworx.no/nb-no/vare-losninger/lonn/lonnssystem-regnskapsbyra · https://www.sdworx.no/nb-no
- Nettlønn: https://nettlonn.com/priser-nettlonn
- Azets: https://www.azets.com/no-no/ressurser/pressemeldinger/azets-inngar-samarbeid-med-sd-worx-lonn · https://www.azets.com/no-no/tjenester/systemer/lonnssystemer · https://www.azets.com/no-no/ressurser/artikler/viktige-frister-innen-regnskap-og-lonn
- Økonomi24: https://www.okonomi24.com/nyheter/aider-kjoper-ikke-livsverk-vi-kjoper-vilje-og-evne-til-vekst/125377 · https://www.okonomi24.com/nyheter/nummer-3-ecit/120137 · https://www.okonomi24.com/nyheter/full-oversikt-dette-er-de-utenlandske-eierne-i-den-norske-regnskapsbransjen/114943
- Sticos Oversikt: https://www.sticos.no/produkter/sticos-oversikt/timeregistrering-og-ressursplanlegging
- Byråpriser: https://regnskapsfirmaet.no/prissetting/ · https://www.styrewebregnskap.no/priser/ · https://millor.no/finn-din-pris/ · https://www.arctic-regnskap.no/vare-priser/ · https://www.sparebank1.no/content/dam/SB1/bank/ostlandet/vedlegg/Prisliste-web-ForretningsPartner-v3-2023.pdf · https://www.xn--regnskapsfrertjenester-fjc.no/blogg/outsourcing-av-lonn
