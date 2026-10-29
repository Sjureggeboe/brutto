# Konkurrent- og markedsanalyse: lønnssystem for norske virksomheter (10–1000 ansatte) og regnskapsbyråer

**Dato:** 2026-10-28
**Formål:** Gi en gründer som kan lønn faglig et faktabasert bilde av markedet før bygging av et nytt, frittstående lønnssystem (direkte salg + lisens til regnskapsbyråer).

## Merking av påstander

| Merke | Betydning |
|---|---|
| **[V]** | Verifisert mot primærkilde: offentlig register (Brreg/Regnskapsregisteret, SSB, Finanstilsynet, Doffin) eller leverandørens egen prisliste/dokument |
| **[L]** | Leverandørens egen påstand (markedsføring), ikke uavhengig bekreftet |
| **[T]** | Tredjepartskilde (blogg, sammenligningsside, søkeutdrag) – ikke bekreftet hos leverandør |
| **[A]** | Mitt anslag eller min analyse, med forutsetningene oppgitt |
| **ukjent** | Fant ikke pålitelig tall. Jeg har ikke gjettet. |

**Metode og begrensninger.** Kildene er nettsøk og direkte henting av produkt- og prissider, Brønnøysundregistrenes åpne API (Enhetsregisteret og Regnskapsregisteret, hentet 2026-10-28), SSB Statistikkbanken (API), Finanstilsynets årsrapport og Doffins kunngjøringsdatabase. Den viktigste enkeltkilden er Regnskap Norges brukerundersøkelse *Lønnssystemer 2025* (publisert 17.03.2026, n=298). Søkekvoten i økten tok slutt mot slutten av arbeidet, så enkelte punkter er markert «ikke verifisert». Det gjelder eierskap til Duett, Unimicro og Fiken, detaljerte partnervilkår og Mamut-historikken. Visma og SD Worx publiserer ikke listepriser for mellomsegmentet.

---

## 0. De viktigste funnene

1. **Markedet er i praksis delt i to.** Det ene er *integrert regnskap + lett lønn* for små kunder: Tripletex, PowerOffice Go, Fiken, Finago og Conta. Det andre er *dedikerte lønnssystemer* for mellomstore og store kunder: SD Worx, Visma Payroll og Visma Enterprise, i tillegg til SAP-, Unit4- og Xledger-moduler. Mellomrommet, omtrent 30–300 ansatte med tariff og ytelser, er dårligst dekket. Der klager brukerne på at de lette systemene er for enkle og at Visma Payroll er rigid. **[A, basert på V-data fra Regnskap Norge]**
2. **Visma eier mer av markedet enn det ser ut til.** Tripletex (siden 2016) og PowerOffice (majoritet siden 2019) eies av Visma, i tillegg til Visma Payroll og Visma Enterprise. I Regnskap Norges undersøkelse står Visma-eide systemer for fire av de fem mest brukte. **[V/T]**
3. **SD Worx er den faglige referansen.** Selskapet har høyest brukertilfredshet (5,4 av 6), størst volum målt i lønnsslipper blant respondentene og oppfattes som dyrest. SD Worx Norway AS omsatte for 360 MNOK i 2025 (+14 %) med 81 MNOK i driftsresultat. Svakhetene er stabilitet etter skyovergangen, Citrix, support og dokumentasjon, og tung implementering. **[V]**
4. **«Nettlønn» er NettLønn fra Adato AS**, en del av ECIT. ECIT ble kjøpt av TowerBrook i 2024. NettLønn har lavest tilfredshet i undersøkelsen (2,9 av 6) og koster 39 kr per lønnsslipp. Selskapet er lite: 7,3 MNOK i omsetning og underskudd i alle tre årene 2023–2025. Kundene er en mulig kilde til overtakelse. **[V]**
5. **Målgruppen er stor nok.** Enhetsregisteret har cirka 40 000 private og ideelle juridiske enheter med 10–999 ansatte, og SSB oppgir cirka 746 000 lønnstakere i private foretak med 10–249 ansatte. Det rene programvaremarkedet for segmentet anslår jeg til omtrent **0,6–1,0 mrd. NOK per år**. **[V for tellingene, A for kroneverdien]**
6. **Regnskapsbyråene er en stor kanal.** Det fantes 2 469 godkjente regnskapsselskaper og 12 839 statsautoriserte regnskapsførere i desember 2024. Lønn utgjør cirka 11 % av bransjens omsetning. De store byråene bruker SD Worx og Visma Payroll for store klienter og Tripletex og PowerOffice for små. **[V]**
7. **Kundene bytter sjelden.** Churn er lav, analytikere anslår den til «et par prosent» hos Zalaris. Kundene bytter som regel når noe tvinger dem, for eksempel da Visma Lønn (Huldt & Lillevik) ble stengt for lønnskjøring fra 2024, eller når programvaren går ut av vedlikehold. Doffin viser også at anbud ender med at eksisterende leverandør fortsetter. **[V/T]**

---

## 1. Markedskart – oversikt

### 1.1 Hvilke systemer bruker lønnsspesialistene? (Regnskap Norge, «Lønnssystemer 2025»)

Kilde: Regnskap Norge, 17.03.2026, 298 respondenter, lansert 04.12.2025. [PDF](https://www.regnskapnorge.no/contentassets/b173a1e31cd741af9b610fc80db70ddf/lonnssystemer---resultater-til-publisering.pdf) **[V]**

**Utvalgsskjevhet:** 45 % av respondentene jobber i regnskapsforetak, 34 % i private virksomheter og 12 % i økonomihus. 47 % sitter i virksomheter med over 250 ansatte. Utvalget er derfor tungt på byråer og store virksomheter.

| System | Antall brukere i utvalget* | Total tilfredshet (1–6) | Tilfredshet med sluttbrukerfunksjoner (1–6) | Eier (merknad) |
|---|---|---|---|---|
| Visma.net Payroll (nå «Payroll») | 106 | 4,6 | 4,5 | Visma |
| SD Worx | 103 | **5,4** | 5,1 | SD Worx (BE) |
| Tripletex | 76 | 4,9 | 4,6 | Visma (siden 2016) |
| PowerOffice Go | 72 | 5,1 | **5,2** | Visma (majoritet siden 2019) [T] |
| Xledger | 46 | 4,5 | 4,4 | ukjent / ikke verifisert |
| Finago (24SevenOffice) | 31 | 4,6 | 4,6 | Finago (fusjon av Accountor Software, 24SevenOffice og Heeros) [T] |
| Duett | 20 | 4,8 | 4,7 | PE-eid ifølge Preqin [T]. Eier ikke verifisert |
| Nettlønn | 20 | **2,9** | **2,8** | Adato AS / ECIT |
| Unit4 / Agresso | 18 | 4,2 | 3,9 | Unit4 |
| Unimicro | 14 | 4,4 | – | ikke verifisert |
| Visma Enterprise HRM | 14 | 3,4 | 3,3 | Visma |
| SAP | 13 | 3,9 | 3,6 | SAP (via partnere) |
| Intect | 10 | – | – | Intect ApS (DK) |
| Systima | 10 | – | – | Systima AS |
| Fiken | 9 | – | – | ikke verifisert |
| Conta | 5 | – | – | Conta AS |
| DNB Regnskap, Personec, Unimicro V3 | 4 hver | – | – | – |
| Vivaldi 3, Paga 2, Hogia / SpareBank 1 Regnskap / Visma Contracting 1 hver | – | – | – | – |

\*Én person kan bruke flere systemer. Konfidensintervallene er brede for systemer med få svar.

**Pris mot tilfredshet** (s. 8 i rapporten): Finago, PowerOffice Go og SD Worx ligger på «Pareto-fronten», der ingen andre systemer er både billigere og bedre. SD Worx og SAP oppfattes som dyrest. Boblestørrelsen viser markedsandel målt i lønnsslipper blant respondentene. SD Worx er klart størst, fulgt av Unit4/Agresso, Visma.net Payroll, Xledger og SAP. Tripletex, PowerOffice, Duett, Unimicro og Finago er små målt i lønnsslipper. **[V]**

### 1.2 Selskapstall fra Regnskapsregisteret (hele selskapet, ikke bare lønn)

Kilde: `data.brreg.no/regnskapsregisteret/regnskap/{orgnr}`, hentet 2026-10-28. **[V]** Driftsinntektene gjelder hele den juridiske enheten. Lønnsandelen er **ukjent** for alle selskapene unntatt SD Worx og Adato, som i praksis bare driver med lønn og HR.

| Selskap (orgnr) | Ansatte (Brreg) | Driftsinntekter 2023 | 2024 | 2025 | Driftsresultat 2025 |
|---|---|---|---|---|---|
| SD Worx Norway AS (913143663) | 121 | 265,5 MNOK | 316,9 | **360,2** | 81,5 MNOK |
| SD Worx Services Norway AS (936947794), stiftet 05.01.2026 | 32 | – | – | – | – |
| Adato AS / NettLønn (995221608) | 8 | 7,9 | 7,0 | **7,3** | −7,5 MNOK |
| Visma Software AS (933646920) | 280 | 1 408,8 | 1 546,6 | 1 568,1 | 437,0 |
| Visma Enterprise AS (982410339) | 339 | 1 447,2 | 1 032,8 | 1 112,4 | 344,6 |
| Tripletex AS (914286018) | 298 | 1 123,6 | 1 390,0 | 1 653,5 | 661,6 |
| PowerOffice AS (980386465) | 116 | 616,6 | 769,9 | 925,0 | 400,7 |
| Fiken AS (913312465) | 81 | 281,5 | 375,7 | 464,2 | 282,8 |
| Xledger AS (987290986) | 92 | 321,6 | 392,7 | 462,6 | 29,3 |
| Unit4 AS (961329310) | 43 | 475,0 | 468,2 | 510,6 | 54,1 |
| Duett AS (932971917) | 99 | 288,3 | 319,6 | 325,2 | 29,8 |
| 24SevenOffice Norway AS (995251094) | 126 | 245,9 | 320,6 | 339,3 | 37,4 |
| Conta AS (998807867) | 52 | 105,4 | 129,0 | 137,2 | 25,3 |
| Systima AS (918817166) | 17 | 1,0 | 2,7 | 6,1 | −11,3 |
| Zalaris ASA, konsern (981953134) | – | 1 131,2 | 1 356,8 | 1 503,2 | 158,9 |
| Zalaris HR Services Norway AS (990796378) | 96 | 248,3 | 272,0 | 292,6 | 11,7 |
| Simployer AS (986419454) | 111 | 408,8 | 485,4 | 532,0 | 33,5 |
| Talentech AS (985360421) | 34 | 157,4 | 174,5 | 185,0 | 17,7 |

**Kalibrering [A]:** SD Worx oppgir «nesten 500 000 lønnsslipper i Norge, hver måned» **[L]**. 360 MNOK fordelt på cirka 6 mill. lønnsslipper i året gir **cirka 60 NOK per lønnsslipp per måned**, inkludert konsulent- og SAP-inntekter. Tallet er en grov indikasjon på hva mellom- og storsegmentet betaler totalt per ansatt, ikke en listepris.

---

## 2. Hovedkonkurrentene i dybden

### 2.1 SD Worx Norge (tidligere Aditro; «SDworks»)

**Historikk (verifisert):**
- **9. mars 2015:** Visma kjøper programvareporteføljen **Huldt & Lillevik** fra **Aditro**. Porteføljen var lønn og HRM for småbedrifter i Norge: Lønn, Ansattportal, Oppfølging, Kjørebok og Håndbøker. [Cinven/Visma](https://www.cinven.com/news-insights/visma-strengthens-its-focus-on-hrm-solutions) **[V]** Huldt & Lillevik gikk altså til *Visma*, ikke til SD Worx.
- **28. april 2021:** SD Worx kjøper Aditro. Aditro hadde cirka 1 200 kunder i mellom- og storsegmentet, over 600 ansatte (SE, NO, FI, EE) og 614,5 MSEK i omsetning i 2020, og SD Worx oppgir at Aditro hadde **34 % markedsandel i Norge i 2020**. [SD Worx-pressemelding](https://www.sdworx.com/en-en/about-sd-worx/press/2021-04-28-sd-worx-continues-international-growth-and-enters-scandinavia-aditro) **[L]** Det er uklart hva markedsandelen er målt mot.
- Konsernet SD Worx har over 84 000 organisasjoner, lønn for cirka 5,2 mill. ansatte, over 7 500 ansatte i 26 land og over 1 mrd. EUR i omsetning (2023). [Azets-pressemelding 17.01.2024](https://www.azets.com/no-no/ressurser/pressemeldinger/azets-inngar-samarbeid-med-sd-worx-lonn) **[L]**
- I Norge har SD Worx cirka 120 ansatte i Oslo og Trondheim [SD Worx karriere](https://careers.sdworx.com/jobs/5728040-lonnsspesialist) **[L]**. SD Worx Norway AS har 121 ansatte i Brreg **[V]**.
- **Nytt i 2026:** *SD Worx Services Norway AS* ble stiftet 05.01.2026 og har 32 ansatte. Formålet er å «levere regnskapstjenester innen lønnstjenester». [Brreg](https://data.brreg.no/enhetsregisteret/api/enheter/936947794) **[V]** Tolkning **[A]**: SD Worx bygger egen BPO-kapasitet i Norge og konkurrerer dermed delvis med sine egne byråpartnere.

| Dimensjon | Funn |
|---|---|
| **Produktnavn** | *SD Worx Lønn* (skybasert), *SD Worx Byrå* (for regnskapsbyråer), *SD Worx HR*, Workforce Management (tid, adgang, planlegging), SAP-løsninger (SAP Lønn, SuccessFactors), *HRM for offentlig sektor*. [sdworx.no](https://www.sdworx.no/nb-no) **[V]** |
| **Målgruppe** | Mellomstore og store virksomheter, offentlig sektor, regnskapsbyråer og internasjonale virksomheter. SD Worx skriver selv: «SD Worx sine løsninger passer best for selskaper med over 100 ansatte». Under 100 ansatte henvises kundene til outsourcing via sertifiserte partnere. [Mindre virksomheter](https://www.sdworx.no/nb-no/trygg-lonn-mindre-virksomheter) **[L]** |
| **Moduler** | Kjøreplaner og periodeplaner, kontroller, import, automatisk kjøring, automatisert fravær og NAV-refusjon, ansattportal, lederportal, lønnsportal, klientportal (byrå og konsern), mange standardrapporter (a-melding, bank, trekk, pensjon, SSB, fri rapport). [Lønnssystem](https://www.sdworx.no/nb-no/vare-losninger/lonn/lonnssystem) **[V]** |
| **Integrasjoner** | «Integrasjoner mot HR-systemer, økonomisystemer og offentlige myndigheter». Et åpent API er **ikke nevnt** på produktsiden. **[V]** |
| **Leveranse** | Sky (SaaS) og outsourcing/BPO («Outsource alt, litt – eller behold kontrollen selv»), samt ISAE-revisjonsrapport og lønnskonsulent til leie. **[V]** |
| **Pris** | **Ukjent**, ikke publisert. Oppfattes som dyrest i Regnskap Norge-undersøkelsen. **[V]** |
| **Volum** | «Nesten 500 000 lønnsslipper i Norge, hver måned». **[L]** |
| **Byråkanal** | «De fleste av Norges største regnskapsbyråer bruker SD Worx Byrå for håndtering av lønn for sine største klienter». [Byrå](https://www.sdworx.no/nb-no/vare-losninger/lonn/lonnssystem-regnskapsbyra) **[L]** Azets valgte SD Worx for storkundesegmentet sitt i januar 2024. **[V]** |
| **Styrker** (Regnskap Norge, brukerkommentarer) | Fleksibel og avansert lønnsmotor, høy automatisering, konfigurering uten spesialtilpasninger, rikt rapportunivers og egne importmaler. Spesielt god på mange tariffavtaler og regulativer. Fraværsmodulen får særlig ros. **[V]** |
| **Svakheter og typiske klager** | Ustabilitet etter skyovergangen og hyppige endringer. Komplekst og tungt å implementere, lite intuitivt for sluttbrukere uten lønnskompetanse. Feilretting, support og dokumentasjon beskrives som «klart utilstrekkelig». Citrix-løsningen skaper fortsatt frustrasjon, særlig ved import og oppdatering for flere selskaper. Systemet er «for åpent» og sårbart for brukerfeil, og retting av historikk og kontrollrapporter er mangelfullt. **[V]** |
| **Anbud (Doffin)** | Tapte *Entur – Lønnstjenester* (9 MNOK, 2024) til View Ledger AS og *Avinor – Lønnssystem* (20 MNOK, 2025) til Sariba. [Doffin 2025-102738](https://doffin.no/notices/2025-102738), [Doffin 2025-103548](https://doffin.no/notices/2025-103548) **[V]** |

### 2.2 Visma-familien

| Produkt | Status 2026 | Målgruppe | Kilde |
|---|---|---|---|
| **Payroll** (tidligere *Visma.net Payroll*) | Visma Software AS sitt skybaserte lønnssystem. Pakkene heter **Start, Pluss og Smart**. | SMB til store, «for større bedrifter» ifølge eldre produktark | [vismasoftware.no/lonn-hr](https://www.vismasoftware.no/lonn-hr) **[V]** |
| **Visma Lønn** (Huldt & Lillevik) | **«Fra 2024 er det ikke lenger mulig å kjøre lønn fra Visma Lønn.»** Kundene ble henvist til Payroll. | Småbedrifter og byråer | [vismasoftware.no/visma-lonn](https://www.vismasoftware.no/visma-lonn) **[V]** |
| **Visma Business Lønn** | Fant ikke et eget produkt med dette navnet i dag. Visma Business, Business NXT og Visma.net presenteres som ERP og er integrasjonsmål for Payroll. | – | **ikke verifisert** |
| **Visma Enterprise HRM**, *Multi* og *Enterprise Plus* (ERP inkl. lønn) | Visma Enterprise AS. Brukes av kommuner og store virksomheter. *Gat* er ressursstyring og turnus (Optur Plus). | Offentlig sektor og store private | [vismaenterprise.no](https://vismaenterprise.no) **[V]** |
| **«Visma Lønn for byrå»** | Fant ikke et eget byråprodukt. På prissiden står det at «regnskapsførere kan be om et prisestimat». | Byråer | [pakker-priser](https://www.vismasoftware.no/lonn-hr/pakker-priser) **[V]** |
| **Tripletex lønn** og **PowerOffice Go lønn** | Visma-eide, men drives som egne merker (se kap. 3). | Små kunder | se kap. 3 |
| **Mamut** | Kjøpt av Visma i 2011 og senere faset ut (fra egen kunnskap, **ikke verifisert i denne økten**). | – | – |

**Visma Payroll – detaljer**

- **Moduler [V]:** lønn, HR (Dottie HR), reise og utlegg (Visma Expense), timeføring, ferie og fravær, godkjenning (Visma Manager-appen), rapportering og dashboards, ARP-verktøy (aktivitets- og redegjørelsesplikt), lønnsslipp på mobil (Visma Employee-appen). Visma oppgir at KI løser «8 av 10 supporthenvendelser» **[L]**.
- **Prismodell [V]:** abonnement, fakturert etterskuddsvis per *aktiv ansatt* (startdato uten sluttdato). Expense faktureres per bruker i tillegg for Start og Pluss. Implementering, tilpasning og integrasjoner kommer i tillegg. **Kronebeløpene er skjult** bak «Sjekk pris».
- **Listepriser fra tredjepart [T]:** Start fra 57 NOK, Pluss fra 67 NOK og Smart fra 100 NOK per ansatt per måned, ifølge [hr.software](https://www.hr.software/reviews/visma-net-payroll), som oppgir at prisene ble verifisert i juni 2026. Start har ingen eksterne integrasjoner. Implementering gjøres av partnere og varierer med antall ansatte.
- **Styrker (Regnskap Norge) [V]:** brukervennlig og strukturert, god automatisering ved korrigeringer og a-melding, god sykefraværsmodul, god support med artikler og raske svar, kontinuerlig forbedring.
- **Svakheter og typiske klager (Regnskap Norge) [V]:** rigid og lite fleksibelt på grunn av streng datostyring. Retro og korrigeringer bakover i tid er komplisert og feilutsatt, og avstemming blir vanskelig når skattetrekk og arbeidsgiveravgift endres tilbake i tid. Brukerne nevner også doble arbeidsprosesser, begrensede rapporter, svak HRM, mangelfull informasjon på lønnsslippen, at systemet er tidvis tregt og tungt å sette opp, svak integrasjon mot regnskap, dårlig oppsett av nye ansattkort og at det er for avansert for små kunder.
- **Kundehistorie som viser byttemønsteret [V]:** Noregs Mållag (9 ansatte) måtte bytte fordi Huldt & Lillevik «skulle legges ned». Payroll var det naturlige valget fordi de allerede brukte Visma til regnskap. Saldoene ble overført direkte, de hadde noen småfeil i første måned, og de savner lønnstrinn på lønnsslippen og rapportene fra H&L. [Kundehistorie](https://www.vismasoftware.no/kundehistorier/byttet-lonnssystem-fra-huldt-og-lillevik-til-payroll)
- **Visma Enterprise HRM** har bare 3,4 av 6 i tilfredshet **[V]**. Randaberg og Kvitsøy kommune utlyste et nytt skybasert HR- og lønnssystem i 2024 fordi de ville bort fra Enterprise HRM. Konkurransen fikk **ett tilbud**, fra Visma Enterprise, til 10 MNOK. [Doffin 2024-117782](https://doffin.no/notices/2024-117782) **[V]** Movar IKS publiserte i juli 2026 en *intensjonskunngjøring* om å fortsette med Visma ved overgangen til sky. [Doffin 2026-112251](https://doffin.no/notices/2026-112251) **[V]** Dette er tydelige tegn på at kundene er låst fast.
- **Kundebase:** **ukjent** for lønn spesifikt. Visma Software AS og Visma Enterprise AS omsatte for henholdsvis 1,57 og 1,11 mrd. NOK i 2025, men lønnsandelen er ukjent. **[V]**

### 2.3 Nettlønn (NettLønn)

| Dimensjon | Funn |
|---|---|
| **Eier** | **Adato AS** (orgnr 995221608, Fornebu) og «en del av ECIT siden 2016». Produktet ble grunnlagt i 2007. [Om NettLønn](https://nettlonn.com/om-nettlonn-1) **[V]** ECIT ble kjøpt av Olympus BidCo (TowerBrook-tilknyttet) for 10 NOK per aksje (cirka 4,65 mrd. NOK). Oppkjøpet ble gjennomført i november 2024, og selskapet ble deretter tatt av børs. [Euronext](https://live.euronext.com/en/products/equities/company-news/2024-10-17-settlement-notification-and-results-voluntary-recommended), [MFN](https://mfn.se/all/a/ecit/ecit-completion-of-voluntary-recommended-offer-to-the-shareholders-of-ecit-as-2211afa7) **[T/V]** |
| **Team** | «7 dedikerte personer» (teamsiden viser 8). Brreg oppgir 8 ansatte. **[V]** |
| **Målgruppe** | Lønnskonsulenter og lønnsteam, i praksis små kunder og byråer. Oppgir «3000+ fornøyde kunder» og «30 000+ lønnsslipper per måned», altså cirka 10 lønnsslipper per kunde. [nettlonn.com](https://nettlonn.com) **[L]** |
| **Moduler** | Lønn, NettLønn People (reise og utlegg, app med lønnsslipp), integrasjoner mot «flere regnskaps- og timesystemer» (ingen fullstendig liste). **[L]** |
| **Pris** | **39 kr per lønnsslipp per måned**, og kunden betaler bare for ansatte som får lønn den måneden. NettLønn People koster 35 kr per aktiv bruker per måned. Alle priser er eks. mva. Oppstarts- og byråpris er ikke oppgitt. [Priser](https://nettlonn.com/priser-nettlonn) **[V]** |
| **Økonomi** | 7,3 MNOK i omsetning i 2025, underskudd hvert år 2023–2025 (−9,0, −17,1 og −9,3 MNOK). **[V]** Tolkning **[A]**: 30 000 lønnsslipper × 12 × 39 kr ville gitt cirka 14 MNOK. Den faktiske omsetningen tyder på byrårabatter eller lavere reelt volum. |
| **Tilfredshet** | **Lavest i markedet:** 2,9 totalt og 2,8 for sluttbrukerfunksjoner (Regnskap Norge). **[V]** |
| **Vurdering [A]** | Lite, underfinansiert produkt i et PE-eid konsern som også eier byråvirksomhet. Kundene er sannsynligvis små og byråbetjente og har lav tilfredshet, så de er lette å vinne med god migrering. Merk at ECIT i Danmark har lyst ut stillinger knyttet til **Intect** («Lønnsspesialist implementering»), så ECIT kan erstatte NettLønn med Intect. **Ikke verifisert.** |

---

## 3. Andre relevante aktører (kort)

| Aktør | Hva | Segment | Lønnspris (liste, eks. mva.) | Tilfredshet (RN) | Kommentar |
|---|---|---|---|---|---|
| **Tripletex** (Visma) | Regnskap + lønnsmodul | Mikro/små. 150 000 kunder (nov. 2025) [MFN](https://mfn.se/all/a/visma/tripletex-reaches-150-000-customers-f2288527) **[L]** | «Lønn og reiseregning» 65 kr per bruker/mnd, timeregistrering mot lønn 39 kr per ansatt/mnd. Pro og Komplett inkluderer 1 bruker. Regnskapsførere får gratis tilgang. [Priser](https://www.tripletex.no/priser/) **[V]** | 4,9 | Kritikk: manglende automasjon og fraværsmodul, importbegrensninger, «lettvekter», dyrt i forhold til funksjonaliteten. **[V]** |
| **PowerOffice Go** (Visma) | Regnskap + lønn. Lønn kan kjøpes frittstående. | Små | **195 kr/mnd + 35 kr per lønnsmottaker**. Timer 100 kr + 50 kr per bruker, reise 100 kr + 50 kr per bruker, ferie og fravær 35 kr per bruker. [Priser](https://poweroffice.no/no/priser) **[V]** | 5,1 (best på sluttbruker, 5,2) | God for små kunder og samarbeid mellom byrå og klient. Brukerne rapporterer feil i forskuddstrekk og feriepenger, svak timebank og få lønnsarter, og at systemet ikke holder for større virksomheter. **[V]** |
| **Fiken** | Regnskap + lønn | Mikro | 69 kr per bruker/mnd. [Priser](https://fiken.no/priser) **[V]** | n=9 | Ikke relevant over cirka 10 ansatte **[A]**. Eier ikke verifisert. |
| **Conta** | Regnskap. Lønn er merket «Kommer snart» på prissiden. | Mikro | Lønnspris ikke oppgitt. [Priser](https://conta.no/priser) **[V]** | n=5 | – |
| **Finago** (tidligere 24SevenOffice) | ERP + *Finago Payday* (lønn) | Små og mellomstore + byrå | **49 kr per lønnsslipp**, 49 kr per sammenstillingsoppgave, reise og utlegg 29 kr per bruker. Multiklient er inkludert. [Priser](https://finago.no/priser), [Byråpriser](https://finago.no/priser-for-regnskapsbyra) **[V]** | 4,6 | Accountor Software, 24SevenOffice og Heeros ble slått sammen til «Finago» [Procountor](https://procountor.fi/en/wp-json/wp/v2/news/2361) **[T]**. Brukerne fant mange feil ved oppstarten i 2025, blant annet i skattetrekk og feriepenger for 60+. Sterkt byråfokus. **[V]** |
| **Xledger** | Sky-ERP med lønnsmodul | Mellomstore, konsern, byrå | ukjent | 4,5 | Lønnsmodulen kritiseres som tungvint, manuell og utdatert, med for lite fokus på lønn og manglende Altinn-automasjon. **[V]** [xledger.com](https://www.xledger.com/no/lonn/) |
| **Unit4** (Agresso) | ERP inkl. lønn | Store og offentlige | ukjent | 4,2 | Stort volum målt i lønnsslipper blant respondentene. Unit4 AS omsatte for 511 MNOK i 2025. **[V]** |
| **Duett** | Regnskap, prosjekt, eiendom. Lønn i Duett Økonomi. | Små og mellomstore + byrå | ukjent (ikke på prissiden) | 4,8 | PE-eid ifølge Preqin («Buyout») **[T]**. Strategisk partnerskap med Aider **[T]**. |
| **Unimicro** | Regnskap + lønn | Små og mellomstore + byrå | ukjent | 4,4 | Har partnerprogram med byråsertifisering [unimicro.no](https://unimicro.no/partnerprogram) **[T]**. |
| **Zalaris** | SAP-basert HR- og lønnsoutsourcing (BPO) | Store / enterprise | ukjent | (SAP 3,9) | Konsernet omsatte for 1,5 mrd. NOK i 2025 **[V]**. Analytikere anslår churn til «et par prosent» og beskriver høye byttekostnader [Affärsvärlden](https://www.affarsvarlden.se/analys/zalaris-lon-for-modan) **[T]**. Tapte Avinor og Entur **[V]**. |
| **Simployer** (+ Talentech) | HR-system (ikke lønn). Integrerer mot Visma, Tripletex og PowerOffice. | SMB–store. Over 12 000 kunder i Norden. [simployer.com](https://www.simployer.com/no) **[L]** | – | – | Viktig integrasjonspartner, ikke konkurrent på lønn. KI-assistenten heter «Sia». Talentech fikk nye eierstrukturer (Topco, Midco og Bidco) i august 2025 **[V, Brreg]**. |
| **Sympa** | HR-system (HRIS) | Mellomstore og store | – | – | Ser ikke ut til å kjøre norsk lønn selv. Uklart. [sympa.com](https://www.sympa.com/no/) |
| **Intect** (DK) | Rent lønnssystem for Skandinavia | SMB–mellomstore, outsourcere | 39 DKK per lønnsslipp på den skandinaviske siden. Norsk pris er ukjent. [intect.io](https://intect.io/en/scandinavian-payroll-system/) **[V]** | n=10 | **Ny aktør:** norsk versjon (v13) ble lansert i april 2025 [Intect support](https://support.intect.io/hc/da-dk/articles/20305730100764-Intect-opdatering-v-13-april-2025) **[V]**. Har multiselskapsmodul, ansattapp og åpent API. Den mest direkte «nye» konkurrenten til konseptet ditt. |
| **Systima** | Ny norsk regnskapsplattform med lønn | Små og byrå | ukjent | n=10 | Stiftet 2017, 17 ansatte. Omsetningen vokser raskt (1,0 → 2,7 → 6,1 MNOK), men med økende underskudd (−11,3 MNOK i 2025). **[V]** |
| **Zenegy** (DK) | Nordisk lønn og regnskap for SMB | SMB | ukjent | – | Oppgis å betjene Norge **[T]**. Ikke verifisert. |
| **DNB Regnskap / SpareBank 1 Regnskap** | Bankeide regnskapsløsninger | Mikro | – | n=4 / n=1 | Bankeide regnskapsforetak vokser (Finanstilsynet). DNB oppgir «kr 0» for regnskapsfører i partnerprogrammet sitt **[T, søkeutdrag]**. |
| **Kontali** | Ikke en lønnsaktør. Kontali Analyse AS er et analyseselskap for havbruk (næringskode 73.200). | – | – | – | Trolig forveksling. **[V, Brreg]** |
| **Gate** | Fant ingen lønnsaktør med dette navnet. Trolig forveksling med Visma Enterprise **Gat** (ressursstyring og turnus). | – | – | – | [vismaenterprise.no](https://vismaenterprise.no) |
| **BPO-/byråaktører i anbud** | View Ledger AS, Tower Newco (tidligere BDO Business Services), Norian Regnskap, Amesto AccountHouse, Azets, Aider | Mellomstore og store offentlig eide selskaper | – | – | Vinner kontrakter for «system + tjeneste», se kap. 8. |

**KI-først-aktører:** Søket fant **ingen** norsk, KI-først lønnsoppstart med synlig trekkraft per oktober 2026. Søkekvoten begrenset dette, så det kan finnes aktører i stealth-fase. De nye aktørene jeg fant er Intect (DK, 2025), Finago Payday (2025) og Systima. Etablerte aktører markedsfører KI i support (Visma) og HR (Simployer «Sia»). **[V/L]**

---

## 4. Markedsstørrelse

### 4.1 Antall virksomheter etter størrelse

**A) Enhetsregisteret, juridiske enheter (hovedenheter) per 28.10.2026**, filtrert på `konkurs=false&underAvvikling=false` og ansatte fra Aa-registeret. **[V]** Kilde: `data.brreg.no/enhetsregisteret/api/enheter?organisasjonsform=…&fraAntallAnsatte=…&tilAntallAnsatte=…` (rådata i `research/brreg_counts.txt`).

| Organisasjonsform | 10–19 | 20–49 | 50–99 | 100–249 | 250–999 | 1000+ |
|---|---|---|---|---|---|---|
| **Alle** | 20 534 | 13 940 | 3 878 | 2 237 | 1 313 | 589 |
| AS | 18 128 | 11 852 | 3 182 | 1 601 | 707 | 187 |
| ASA | 22 | 31 | 19 | 14 | 8 | 8 |
| **Stiftelse (STI)** | 216 | 303 | 112 | 55 | 17 | 5 |
| **Forening/lag/innretning (FLI)** | 737 | 586 | 152 | 101 | 18 | 2 |
| Samvirkeforetak (SA) | 279 | 367 | 43 | 34 | 33 | 16 |
| NUF | 142 | 91 | 32 | 24 | 8 | 6 |
| ENK / ANS / DA | 632 | 155 | 14 | 11 | 3 | 0 |
| *Offentlig og kirke (KOMM, FYLK, ORGL, STAT, KF, IKS, SF, KIRK)* | 309 | 472 | 290 | 362 | 498 | 342 |
| **Private og ideelle (Alle minus offentlig)** [A, utregnet] | **20 225** | **13 468** | **3 588** | **1 875** | **815** | 247 |

- **Målgruppen 10–999 ansatte, private og ideelle:** cirka **39 970 juridiske enheter** [A, sum av V-tall]. Av disse er **703 stiftelser** og **1 594 foreninger/lag/innretninger**.
- Til sammenligning har 1–4 ansatte 105 424 enheter og 5–9 ansatte 29 282 (alle former). **[V]**
- Enheter i **Frivillighetsregisteret** med ansatte: 5 134 med minst 1 ansatt og **1 638 med minst 10 ansatte**, av 72 913 registrerte i alt. **[V]**

**B) SSB tabell 14002, «Føretak med lønnstakarar» (2023, siste publiserte år med denne fordelingen).** Tabellen omfatter ikke offentlig forvaltning og dekker ideelle organisasjoner dårlig. [SSB 14002](https://www.ssb.no/statbank/table/14002) **[V]**

| Lønnstakere | 10–19 | 20–49 | 50–99 | 100–249 | 250+ |
|---|---|---|---|---|---|
| Antall foretak | 14 387 | 7 538 | 2 212 | 1 197 | 686 |
| Antall lønnstakere | 192 231 | 223 517 | 150 467 | 179 666 | 550 448 |

SSB deler ikke 250+ i 250–999 og 1000+. Brreg viser 1 313 enheter med 250–999 ansatte (alle sektorer).

**Hvorfor A og B er ulike [A]:** Brreg teller alle aktive arbeidsforhold i Aa-registeret, også små stillinger og ekstrahjelp, så flere enheter havner i høyere størrelsesklasser. SSB bruker en strengere definisjon av lønnstakere. Bruk SSB som **konservativt** tall og Brreg som **øvre grense**. Brregs tall er mest relevant for *antall lønnsslipper*.

**C) SSB tabell 10308, bedrifter (virksomheter, ikke juridiske enheter) per 2026.** Sektoren «Husholdninger og ideelle organisasjoner» har 806 bedrifter med 10–19 ansatte, 561 med 20–49, 183 med 50–99, 83 med 100–249 og 23 med 250+. [SSB 10308](https://www.ssb.no/statbank/table/10308) **[V]**

### 4.2 Regnskapsbyråer og regnskapsførere

| Mål | Tall | Kilde |
|---|---|---|
| Godkjente regnskapsselskaper (des. 2024) | **2 469** (+175 nye godkjenninger i 2024) | [Finanstilsynet årsrapport 2024](https://www.finanstilsynet.no/publikasjoner-og-analyser/arsrapport/arsrapport-2024/rapporter-fra-tilsynsomradene-for-2024/regnskapsvirksomhet) **[V]** |
| Statsautoriserte regnskapsførere (des. 2024) | **12 839** (716 nye i 2024. 352 driver i enkeltpersonforetak) | samme **[V]** |
| Tall for 2025 | **ukjent** (siden for årsrapporten 2025 ga 404) | – |
| Juridiske enheter med næringskode 69.202 (regnskapsføring), okt. 2026 | 4 395 i alt. 2 107 med minst 1 ansatt, **845 med minst 5**, **145 med minst 20**. | Brreg API **[V]** |
| Største byråer (ansatte i Brreg) | Aider AS 1 342, Azets Insight AS 884, SpareBank 1 Regnskapshuset SMN 582, SpareBank 1 Regnskapshuset Nord-Norge 273. BDO AS 1 286 inkluderer revisjon. | Brreg **[V]** |
| Personer som jobber med lønn | «Nær 4 000 personer»: lønningsmedarbeidere (STYRK 4313, cirka 2 000+) og regnskapsførere som jobber med lønn (STYRK 3313, under 2 000). 80 % er kvinner. | Regnskap Norge s. 4 **[V]** |
| Lønnstjenesters andel av regnskapsbransjens omsetning | **11 %** | Regnskap Norge s. 4 **[V]** |
| Trend | Bankeide regnskapsforetak vokser. Antallet statsautoriserte i enkeltpersonforetak faller kraftig. | Finanstilsynet **[V]** |

### 4.3 Andel som setter ut lønn

| Påstand | Kilde | Vurdering |
|---|---|---|
| «Blant bedrifter med færre enn 250 ansatte velger hele 43 % å outsource lønnshåndteringen i Norge.» | [SD Worx](https://www.sdworx.no/nb-no/trygg-lonn-mindre-virksomheter) | **[L]**. Ingen kildehenvisning. Bruk med forsiktighet. |
| «Almost 6 in 10 Norwegian companies are willing to outsource payroll processing entirely» | [SD Worx Payroll Proficiency Index 2023](https://go.sdworx.com/en/payroll-proficiency-index/drivers/partner) | **[L]**. Gjelder *villighet*, ikke faktisk andel. Utvalgsstørrelse ukjent. |
| Uavhengig tall fra SSB eller Regnskap Norge | – | **ukjent**. Fant ikke noe. |

**Anslag [A]:** Andelen som setter ut lønn faller med størrelsen. Under 20 ansatte bruker trolig de fleste regnskapsfører, mens virksomheter med over 100 ansatte oftest har egen lønnsfunksjon. Dette er et resonnement, ikke målt.

### 4.4 Anslått markedsverdi (programvare, eksklusive tjenester) [A]

| Forutsetning | Verdi |
|---|---|
| Lønnstakere i private foretak med 10–249 ansatte (SSB 2023) | 745 881 [V] |
| Antatt andel av 250+-gruppen som har 250–999 ansatte | 40–50 % av 550 448, altså cirka 220 000–275 000 [A] |
| Ideelle enheter (STI og FLI, 10–999) som SSB ikke fanger | 2 297 enheter × cirka 35 ansatte ≈ 80 000 [A] |
| **Ansatte i målgruppen, sum** | **≈ 1,05–1,10 mill.** [A] |
| Programvarepris per ansatt eller lønnsslipp per måned | 50–80 NOK (spenn mellom PowerOffice/NettLønn på 35–39 kr, Finago på 49 kr, Visma på 57–100 kr [T] og SD Worx' implisitte cirka 60 kr) [A] |
| **Programvaremarked per år** | **≈ 0,63–1,05 mrd. NOK** [A] |
| Tjenester (implementering, BPO og byrålønn) | Sannsynligvis flere ganger programvareverdien. Lønn utgjør 11 % av regnskapsbransjens omsetning [V], men bransjens totale omsetning er ikke hentet her (**ukjent**). |

**Enhetsøkonomi [A]:** En kunde med 300 ansatte gir cirka 300 × 60 kr × 12 ≈ **216 000 NOK i årlig programvareinntekt (ARR)**. 30 MNOK i ARR krever omtrent 140 slike kunder, eller cirka 42 000 lønnsmottakere på plattformen. Det tilsvarer under 10 % av SD Worx' oppgitte volum.

---

## 5. Hvordan regnskapsbyråer kjøper lønnssystem i dag

### 5.1 Observerte modeller

| Modell | Hvem eier kundeforholdet og lisensen | Eksempler (kilde) |
|---|---|---|
| **Klienten eier lisensen, byrået får gratis tilgang** | Klienten betaler leverandøren. Byrået har gratis regnskapsførertilgang og får eventuelt partnerfordeler. | Tripletex: «regnskapsførere med regnskapsførerkonto får gratis tilgang» [V]. DNB Regnskap: «kr 0» for regnskapsfører [T]. PowerOffice: partnernivåer som «Premium Partner» (Azets) [V]. |
| **Byrålisens / byråprodukt** | Byrået kjøper en flerklientplattform og fakturerer lønnstjenesten til klienten. | SD Worx Byrå (flerklient, klientportal) [V]. Finago Payday med multiklient inkludert, og Finago Mikro som «må kjøpes gjennom regnskapsbyrå» [V]. NettLønn har egen byråpris (ikke publisert) [V]. |
| **Leverandør som BPO via sertifiserte byråpartnere** | Leverandøren eier plattformen, og byrået leverer tjenesten. | SD Worx overfor kunder under 100 ansatte: «levert av sertifiserte partnere på SD Worx sin lønnsplattform» [L]. Intect: «local Intect partners» [L]. |
| **Leverandøren leverer BPO selv** | Leverandøren eier både plattform og tjeneste og konkurrerer med byråene. | SD Worx Services Norway AS (stiftet 2026) [V]. Zalaris [V]. |
| **Store byråer velger standardsystemer per segment** | Byråkjeden forhandler sentralt. | Azets: SD Worx for storkunder (fra jan. 2024), i tillegg Visma Payroll og Visma.net Payroll [V]. |

### 5.2 Partnerprogram og rabatter

- Tripletex deler byråpartnere i segmenter: «Growth» (vekstpartnere), «Core» (bred portefølje) og de «3–4 største premiumpartnerne». **[T, stillingsannonser på finn.no]**
- Visma Payroll: «Regnskapsførere kan be om et prisestimat». Implementering gjøres av sertifiserte partnere. **[V/T]**
- **Rabattnivå, provisjon og kickback er ukjent.** Ingen leverandør publiserer dette. Må kartlegges i intervjuer med byråer.

### 5.3 Hva byråene klager på (Regnskap Norge) [V]

- **SD Worx:** Citrix og import for flere selskaper er tungvint.
- **Visma Payroll:** retroføring og avstemming er vanskelig, og integrasjonen mot regnskap er svak.
- **Xledger:** svært manuelt, med mange klikk.
- **Tripletex:** bare én import før systemet oppretter en ny lønnskjøring.
- **PowerOffice:** mange unødvendige klikk ved oppsett av ansatte og faste lønnslinjer.
- **Finago:** brukerne må innom både regnskap og bank for å fullføre lønnskjøringen.

**Konsekvens [A]:** Byråer verdsetter masseoperasjoner på tvers av klienter, maler, felles kontroller og avvikslister, rask import, og mindre klikk og kontekstbytte.

---

## 6. Hull i markedet og differensiering for 2026–2027

### 6.1 Hull som dataene peker på [A, basert på V-data]

1. **«SD Worx-motor med Tripletex-brukervennlighet» for 30–500 ansatte.** SD Worx sier selv at de passer best over 100 ansatte. PowerOffice og Tripletex holder ikke for større virksomheter, og Visma Payroll oppleves som rigid. Ingen leverandør scorer høyt på både lønnsmotor og brukervennlighet *i mellomsegmentet*.
2. **Retro og korreksjon som kjernefunksjon.** Dette er den største enkeltklagen mot Visma Payroll, og SD Worx-brukerne savner «oppretting av historikk og kontrollrapporter». Et system som håndterer tilbakevirkende endringer med full sporbarhet og automatisk avstemming av skattetrekk og arbeidsgiveravgift, adresserer et konkret og dokumentert problem.
3. **Kontroll og «andre øyne» med KI.** Lønnsfolk ønsker KI som *kontrollfunksjon*, særlig for lønn og reiseregninger. 62 % bruker Copilot, 52 % ChatGPT og 19 % Sticos Zipp. Samtidig er de skeptiske til treffsikkerhet på tall. **[V, s. 15–17]** KI-verdien ligger derfor i å finne avvik før kjøring (uvanlige endringer, manglende trekk, feriepenger 60+, inntektsmelding og refusjon) og i å forklare differanser mot forrige måned. KI skal *ikke* beregne lønn.
4. **Byrå-arbeidsflate.** Tilbud som trengs: flerklient-dashbord, standardmaler, endringer i satser, lønnsarter og tariff på tvers av klienter med ett klikk, felles kontrollregler, import uten begrensninger, klientportal for innsending av variable data og godkjenning, og ingen Citrix.
5. **Stabilitet, support og dokumentasjon.** Dette er SD Worx' tydeligste svakhet. Det er billig å differensiere på og vanskelig for de store å fikse raskt.
6. **Ideell sektor og stiftelser** med 703 stiftelser og cirka 1 600 foreninger med 10–999 ansatte [V]. Typiske behov er tariff (Virke HUK, Spekter), pensjon og støttet arbeid. *Antagelse:* mange ideelle i helse og omsorg har offentlig tjenestepensjon (KLP eller SPK) og krever elektronisk pensjonsrapportering. NMBUs anbud krever eksplisitt godkjenning for innrapportering til Statens pensjonskasse [V]. **Hvor utbredt KLP- og SPK-ordninger er i målgruppen, er ikke verifisert.**
7. **Åpen prising og åpent API.** Visma og SD Worx skjuler prisene, og SD Worx-siden nevner ikke et åpent API. Intect har både åpent API og offentlig pris, og er dermed nærmeste konkurrent på dette punktet.
8. **Låste kunder i offentlig og offentlig eid sektor.** Doffin viser én tilbyder (Randaberg) og intensjonskunngjøringer om å fortsette med Visma (Movar). Det er mulig å komme inn, men det krever en anbudsorganisasjon og blir en senere fase.

### 6.2 Hva skal til for å vinne en kunde med 300 ansatte fra Visma Payroll? (kritisk) [A]

**Den ærlige utgangen:** Lønn er en «skal ikke feile»-prosess. Lønnssjefen risikerer jobben sin og har lite å vinne på å bytte. Du konkurrerer derfor mot *status quo* og ikke bare mot Visma. Funksjonsparitet er inngangsbilletten, ikke grunnen til å bytte.

**Må-krav for å komme med i vurderingen**
- Norsk lønnsmotor som håndterer:
  - a-melding med korrekt kontinuitet i arbeidsforhold (se kap. 7)
  - forskuddstrekk med tabell og prosent, halvt trekk i juni og desember
  - feriepenger inkludert 60+ og ferielov eller tariff
  - arbeidsgiveravgift per sone
  - sykepenger og NAV-refusjon
  - fagforeningstrekk
  - OTP og pensjonsrapportering
  - reise etter statens satser
  - ARP og likelønnsrapport
- Integrasjoner fra første dag mot kundens regnskap (Visma Business NXT og Visma.net, Xledger, Unit4, Tripletex, PowerOffice) og bank (remittering), samt timer og turnus, HR (Simployer og lignende) og SSO.
- Sikkerhet og revisjon: ISO 27001, ISAE 3402-rapport (SD Worx tilbyr ISAE), databehandleravtale og data i EØS.
- Referanser fra virksomheter av samme størrelse. Et nytt selskap uten referanser taper på risiko, ikke på funksjonalitet.

**Det som faktisk utløser et bytte**
1. **En målbar smerte hos kunden:** for eksempel retroføring, avstemming eller doble prosesser (dokumentert for Visma), eller reise, timer og fravær i separate verktøy. Vis det i en demo på *kundens egne data*.
2. **Migrering uten risiko:**
   - Gratis eller fastpris import av ansattregister og saldoer hittil i år (feriepengegrunnlag, trekk, fravær).
   - Kartlegging av lønnsarter.
   - Parallellkjøring av 1–2 lønnskjøringer med automatisk avviksrapport.
   - En navngitt implementeringsansvarlig.
   - Garanti: blir lønnen feil på grunn av systemet, retter dere det og betaler for det.
3. **Tidsvindu:** Skriv kontrakt i Q3, gjør en prøvekjøring i november og desember, og gå live med første lønnskjøring i januar (se kap. 7).
4. **Pris:** Ligg på eller under Visma per ansatt, med alt inkludert (tid, fravær, reise og app) i stedet for Visma-modellen med tillegg per bruker for Expense. Pris alene vinner sjelden kunden, men den fjerner en innvending.
5. **Inngang via regnskapsbyrå:** Mange 300-ansatte kunder har regnskapet hos et byrå. Hvis byrået anbefaler deg, er halve salget gjort. Byrålisensen er derfor også en salgskanal mot direktekunder.
6. **Realistisk salgssyklus:** 3–9 måneder **[A]**. Rekkefølgen gir seg selv: Vinn først kunder med 30–150 ansatte som er i ferd med å vokse ut av Tripletex eller PowerOffice, og NettLønn-kunder med lav tilfredshet. Bygg deretter referanser oppover mot 300+.

---

## 7. Byttebarrierer og hvordan kunder bytter lønnssystem

### 7.1 Regelverk for a-meldingen ved bytte (Skatteetaten) [V]

Kilde: [Skatteetaten – Bytte lønnssystem](https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/arbeidsforholdet/spesielle-forhold/bytte-lonnssystem/)

- Arbeidsforholdene må flyttes til det nye systemet og rapporteres hver måned. Det er **ikke lov** å sende a-melding med de samme arbeidsforholdene fra to systemer for samme periode.
- Antall arbeidsforhold per ansatt og tilknytningen til underenhet må være lik før og etter byttet.
- Det finnes tre alternativer:
  1. **Videreføring:** samme arbeidsforholdId, startdato og type i det nye systemet. Dette er den beste kundeopplevelsen og krever at systemet kan importere ID-ene.
  2. Ny arbeidsforholdId uten å avslutte i det gamle systemet.
  3. Avslutning i det gamle systemet med årsak «byttet lønnsystem eller regnskapsfører», og ny ID i det nye systemet fra dagen etter.
- Bestill **avstemmingsrapport** for siste måned for å kontrollere.

**Produktkonsekvens [A]:** Import av arbeidsforholdId, permisjoner og permitteringer (alternativ 1), og automatisk avstemming mot avstemmingsrapporten fra a-ordningen, bør være standardfunksjonalitet i migreringsverktøyet.

### 7.2 Tidspunkt og praksis [A, med V-støtte der det er angitt]

| Tema | Vurdering |
|---|---|
| **Når kundene bytter** | Oftest ved **årsskiftet** (lønnskjøringen i januar), fordi da nullstilles hittil-i-år-saldoer for trekk og opptjening av feriepenger. Det er mulig å bytte midt i året, siden a-meldingen er månedlig, men da må feriepengegrunnlag, trekk og saldoer hittil i år, fravær og eventuelle permisjoner overføres. Noregs Mållag gikk live i februar 2023 med overførte saldoer [V]. |
| **Parallellkjøring** | Vanlig for mellomstore kunder: 1–2 måneder med «skyggekjøring» i nytt system og sammenligning med gammelt. Ikke dokumentert i Visma-kundehistorien. Antallet er et anslag. |
| **Historikk** | Kundene trenger tilgang til historiske lønnsslipper, arbeidsgiveravgift og trekk i flere år for kontroll og revisjon (*antagelse om varighet, ikke verifisert*). Mange lar det gamle systemet stå i lesemodus eller eksporterer til PDF/arkiv. Et godt historikkarkiv i det nye systemet senker barrieren. |
| **Byttekostnad** | Høy. Churn hos lønnsleverandører anslås til «et par prosent», og kundene bytter sjelden mens løsningen fungerer [T, Zalaris-analyse]. |
| **Utløsende hendelser** | (1) Leverandøren avvikler produktet: Visma Lønn ble stengt for lønnskjøring fra 2024 [V], og Vinmonopolets lønnssystem er «basert på utgående programvare» [V, Doffin 2026-111156]. (2) Kunden vokser ut av integrert regnskapslønn (Tripletex og PowerOffice). (3) Skifte av regnskapsbyrå, som ofte betyr systembytte (Skatteetaten nevner dette eksplisitt) [V]. (4) Fusjon eller oppkjøp. (5) Dårlig erfaring med stabilitet eller support (SD Worx, Finago og NettLønn). |
| **Hvem bestemmer** | Lønnsleder og økonomisjef, ofte med regnskapsbyrået som rådgiver. I offentlig eid sektor går det via anbud (kap. 8). |

---

## 8. Signaler fra offentlige anskaffelser (Doffin) [V]

Kilde: Doffin-API (`api.doffin.no/webclient/api/v2/…`), søk på «lønnssystem», «lønn og HR-system» og «lønnstjenester». Utvalg fra 2024–2026:

| Kunngjøring | Oppdragsgiver | Verdi | Resultat |
|---|---|---|---|
| [2025-102738](https://doffin.no/notices/2025-102738) Lønnstjenester (system + tjeneste) | Entur AS | Anslått 11 MNOK, tildelt 9 MNOK | **View Ledger AS** vant. Tapte: Zalaris, Norian Regnskap, Amesto AccountHouse, **SD Worx Norway**. Vekting: kvalitet 60 %, pris 40 %. |
| [2025-103548](https://doffin.no/notices/2025-103548) Lønnssystem | Avinor AS | 20 MNOK | **Sariba** (SAP-partner) vant. Tapte: Zalaris, **SD Worx Norway**. |
| [2026-105021](https://doffin.no/notices/2026-105021) HR- og lønnssystem (SaaS) | Norske tog AS | Anslått 8 MNOK, vinnerverdi 2,5 MNOK | **Tower Newco (tidligere BDO Business Services)** vant. Tapte: Norian Regnskap. |
| [2024-117782](https://doffin.no/notices/2024-117782) System for HR og lønn | Randaberg og Kvitsøy kommune | 10 MNOK | **Ett tilbud**: Visma Enterprise (fortsetter med Enterprise HRM). |
| [2026-112251](https://doffin.no/notices/2026-112251) Intensjonskunngjøring | Movar IKS | – | Fortsetter med Visma i overgangen til sky. |
| [2026-111156](https://doffin.no/notices/2026-111156) Kjøp av lønnssystem | Vinmonopolet | ukjent | Kvalifisering avsluttet 12.08.2026. Bytter ut «utgående programvare». |
| [2026-106493](https://doffin.no/notices/2026-106493) Nytt lønns- og reiseregningssystem | Eidsiva Energi AS | ukjent | Konkurranse kunngjort april 2026. |
| [2026-111133](https://doffin.no/notices/2026-111133) Lønnssystem | NMBU | ukjent | Avlyst eller ikke inngått (juni 2026). Krav om godkjenning for innrapportering til Statens pensjonskasse. |

**Tolkning [A]:** Offentlig eide selskaper med 300–2 000 ansatte kjøper ofte **system og tjeneste samlet**, og regnskaps- og BPO-aktører vinner. SD Worx taper av og til mot både byråer og SAP-partnere. **En plattform som byråer kan by med** (lisensmodellen din) gir derfor indirekte tilgang til anbudsmarkedet uten at du selv må ha en anbudsorganisasjon.

---

## 9. Åpne spørsmål å følge opp (anbefalt primærinnsikt)

1. Faktiske priser og rabatter hos Visma Payroll og SD Worx i mellomsegmentet (be om tilbud eller intervju 5–10 lønnssjefer).
2. Partnervilkår i byråkanalen (rabatt, provisjon, hvem som fakturerer). Intervju 5–10 byråer (Aider, Azets, SpareBank 1 Regnskapshuset, Norian, Accountor/Finago-partnere).
3. Hvor stor andel av virksomheter med 10–249 ansatte som setter ut lønn (finnes ikke uavhengig tall).
4. Om ECIT faser ut NettLønn til fordel for Intect (påvirker overtakelsesmuligheten).
5. Eierskap til Duett, Xledger, Unimicro og Fiken, og hvem som står bak Finago (ikke verifisert i denne økten).
6. Pensjon (KLP og SPK) og tariff (Virke HUK, Spekter) i ideell sektor: andel og krav.

---

## Kildeliste (hovedkilder)

- Regnskap Norge – *Lønnssystemer 2025* (17.03.2026): https://www.regnskapnorge.no/contentassets/b173a1e31cd741af9b610fc80db70ddf/lonnssystemer---resultater-til-publisering.pdf
- SD Worx Norge: https://www.sdworx.no/nb-no · https://www.sdworx.no/nb-no/vare-losninger/lonn/lonnssystem · https://www.sdworx.no/nb-no/vare-losninger/lonn/lonnssystem-regnskapsbyra · https://www.sdworx.no/nb-no/trygg-lonn-mindre-virksomheter · https://www.sdworx.no/nb-no/lonnssystem-best-i-test-pa-brukertilfredshet
- SD Worx kjøper Aditro (2021): https://www.sdworx.com/en-en/about-sd-worx/press/2021-04-28-sd-worx-continues-international-growth-and-enters-scandinavia-aditro
- Visma kjøper Huldt & Lillevik (2015): https://www.cinven.com/news-insights/visma-strengthens-its-focus-on-hrm-solutions
- Azets–SD Worx (17.01.2024): https://www.azets.com/no-no/ressurser/pressemeldinger/azets-inngar-samarbeid-med-sd-worx-lonn · https://www.azets.com/no-no/tjenester/systemer/lonnssystemer
- Visma Payroll: https://www.vismasoftware.no/lonn-hr · https://www.vismasoftware.no/lonn-hr/pakker-priser · https://www.vismasoftware.no/visma-lonn · https://www.vismasoftware.no/kundehistorier/byttet-lonnssystem-fra-huldt-og-lillevik-til-payroll · https://www.hr.software/reviews/visma-net-payroll · https://vismaenterprise.no
- NettLønn: https://nettlonn.com · https://nettlonn.com/priser-nettlonn · https://nettlonn.com/om-nettlonn-1
- ECIT-oppkjøp: https://live.euronext.com/en/products/equities/company-news/2024-10-17-settlement-notification-and-results-voluntary-recommended · https://mfn.se/all/a/ecit/ecit-completion-of-voluntary-recommended-offer-to-the-shareholders-of-ecit-as-2211afa7
- Tripletex: https://www.tripletex.no/priser/ · https://mfn.se/all/a/visma/tripletex-reaches-150-000-customers-f2288527
- PowerOffice: https://poweroffice.no/no/priser · Visma-eierskap: https://www.apideck.com/blog/visma-api-portfolio (T)
- Fiken: https://fiken.no/priser · Conta: https://conta.no/priser · Finago: https://finago.no/priser · https://finago.no/priser-for-regnskapsbyra · https://procountor.fi/en/wp-json/wp/v2/news/2361
- Intect: https://intect.io/en/scandinavian-payroll-system/ · https://support.intect.io/hc/da-dk/articles/20305730100764-Intect-opdatering-v-13-april-2025
- Xledger: https://www.xledger.com/no/lonn/ · Simployer: https://www.simployer.com/no · Sympa: https://www.sympa.com/no/
- Zalaris: https://zalaris.com/managed-services/hr-%26-payroll-outsourcing · https://www.affarsvarlden.se/analys/zalaris-lon-for-modan
- SD Worx Payroll Proficiency Index: https://go.sdworx.com/en/payroll-proficiency-index/drivers/partner
- Finanstilsynet årsrapport 2024: https://www.finanstilsynet.no/publikasjoner-og-analyser/arsrapport/arsrapport-2024/rapporter-fra-tilsynsomradene-for-2024/regnskapsvirksomhet
- Skatteetaten – bytte lønnssystem: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/arbeidsforholdet/spesielle-forhold/bytte-lonnssystem/
- SSB: https://www.ssb.no/statbank/table/14002 · https://www.ssb.no/statbank/table/10308
- Brønnøysundregistrene (API): https://data.brreg.no/enhetsregisteret/api/enheter · https://data.brreg.no/regnskapsregisteret/regnskap/{orgnr}
- Doffin: https://doffin.no/notices/2025-102738 · /2025-103548 · /2026-105021 · /2024-117782 · /2026-112251 · /2026-111156 · /2026-106493 · /2026-111133
