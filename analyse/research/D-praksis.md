# D – Lønn i praksis i virksomheter med 10–1000 ansatte

**Hvordan lønn faktisk håndteres: prosesser, roller, kontroller, integrasjoner og smertepunkter**

Dato: 28. oktober 2026 · Perspektiv: erfaren lønnssjef/HR-konsulent · Målgruppe: gründer som skal bygge et frittstående norsk lønnssystem for AS, stiftelser, foreninger og ideelle organisasjoner (10–1000 ansatte), som også skal lisensieres til regnskapsbyråer.

> **Lesenøkkel.** Påstander med kilde har URL. Uten kilde betyr det erfaringsbasert praksis eller et anslag fra rådgiver. Tidsbruk, bemanning og typiske funn er **anslag**, ikke målte tall, med mindre noe annet står.
> Det offentlige regelverket endret seg mye i 2026: skattetrekkskontoen er borte, utleggstrekk har nye regler, Altinn 2 er stengt og NAV har ny inntektsmelding. Se kapittel 0.

---

## Innhold

0. Kort oppsummering og regelendringer i 2026 som påvirker prosessen
1. Lønnsprosessen måned for måned
2. Årshjulet
3. Roller, ansvarsdeling og tilgangsstyring
4. Internkontroll og revisjon
5. Integrasjonslandskapet
6. Organisasjonskompleksitet: konsern, AGA-soner, kostnadsfordeling, prosjekt og tilskudd
7. Særtrekk for stiftelser, ideelle og frivillige organisasjoner
8. Smertepunkter med dagens systemer
9. Typiske krav i anbud (Doffin/TED)
10. Ansattportal og selvbetjening: forventninger i 2026
11. **Fortelling: en typisk lønnsmåned (november 2026) i en virksomhet med 400 ansatte**
12. Implikasjoner for produktet
13. Kildeliste

---

## 0. Kort oppsummering

1. **En lønnskjøring er en flyt med mange aktører, ikke én beregning.** I en virksomhet med 100–1000 ansatte gjør lønnsavdelingen bare en del av arbeidet selv. Resten kommer fra andre: ansatte (timer, fravær, utlegg), ledere (godkjenning), HR (masterdata, lønnsendringer), tid/vakt-systemet, økonomi (attestasjon, bank, regnskap) og myndighetene (skattekort, trekkpålegg, NAV). Det som skiller systemene, er hvordan de **samler inn, validerer, kontrollerer og dokumenterer**, ikke selve lønnsmotoren.
2. **Cut-off ligger 1–2 uker før utbetaling.** Store virksomheter har en kjøreplan med faste datoer. Ansatte leverer typisk ca. 2 uker før utbetaling og ledere godkjenner 8–10 dager før. UiB og NTNU (DFØ) utbetaler den 12. og har ledergodkjenning den 2.–4. i måneden ([UiB](https://www.uib.no/foransatte/175460/utbetaling), [NTNU](https://i.ntnu.no/wiki/-/wiki/English/Payment+schedule+for+salaries+and+refunds)). Variable tillegg betales nesten alltid **etterskuddsvis**, altså oktobers overtid i novemberlønnen.
3. **Testkjøring og avviksanalyse mot forrige måned er standard** i alt over ca. 50 ansatte. Det samme gjelder fire-øyne-kontroll og attestasjon av totalsummer før bankfilen frigis. Kontrollrapportene er der lønnsmedarbeidere bruker mest tid, og det er her mange systemer er svake.
4. **Fra 1.1.2026 er skattetrekkskontoen avviklet.** Forskuddstrekk og utleggstrekk skal betales direkte til Skatteetaten **senest første virkedag etter lønnsutbetalingen**, med ny KID hver måned. AGA betales fortsatt per termin ([Skatteetaten](https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/arbeidsgiveravgift/betaling-av-forskuddstrekk-og-arbeidsgiveravgift/), [Skatteetaten KID](https://www.skatteetaten.no/kid/), [Revisorforeningen](https://www.revisorforeningen.no/fag/nyheter/skattetrekkskontoen-fjernes-fra-1.-januar-2026/)). Betaling av trekk er dermed en del av selve lønnskjøringen, og et lønnssystem bør lage disse betalingene automatisk.
5. **Nye regler for utleggstrekk fra januar 2026.** Trekkpålegg hentes via Skatteetatens API, de nye trekkene rapporteres med egen kode (`utleggstrekkSamordnet`) og betales til egen konto med en KID per ansatt. Gamle og nye trekk skal holdes adskilt ([Skatteetaten – systemleverandører](https://www.skatteetaten.no/om-skatteetaten/fremtidens-innkreving/systemleverandorer/lonns--og-personalsystem/)).
6. **Altinn 2 ble skrudd av 19. juni 2026.** NAV flytter inntektsmelding til et API som svarer på en forespørsel fra NAV ([NAV](https://www.nav.no/arbeidsgiver/moderniserte-tjenester), [Digdir](https://samarbeid.digdir.no/sites/samarbeid/files/2025-12/Viktig%20informasjon%20-%20Overgang%20fra%20Altinn%20II%20til%20Altinn%203.pdf)). Et nytt system må bygges på Altinn 3 og Maskinporten fra første dag.
7. **Det er stor misnøye med lønnssystemene for store virksomheter.** I Regnskap Norges undersøkelse «Lønnssystemer 2025» (n=298 lønnsspesialister, publisert mars 2026) scorer Visma Enterprise HRM 3,4 og SAP 3,9 på en skala fra 1 til 6. SD Worx (5,4) og PowerOffice GO (5,1) scorer høyest. Gjennomgående klager er retro og korrigeringer, manuelt arbeid, svake kontrollrapporter, ustabilitet etter skyflytting og dårlig support ([Regnskap Norge](https://www.regnskapnorge.no/contentassets/b173a1e31cd741af9b610fc80db70ddf/lonnssystemer---resultater-til-publisering.pdf)).
8. **Mange anbud kjøper system og lønnskjøring samlet.** Ferde, Norske tog, Entur, Tensio, Gassnova og GRID-Arendal kjøper alle lønn som tjeneste. Byråer og outsourcing-leverandører er derfor både kunder og kanal, og byråversjonen må støtte at byrået kjører lønn for kunden mens kunden selv godkjenner. Kvalitet vektes ofte 60–75 %. I kommunale anbud vektes miljø ofte 30 % ([TED](https://ted.europa.eu/en/notice/-/detail/169076-2025), [TED](https://ted.europa.eu/en/notice/-/detail/367086-2024)).
9. **Stiftelser og ideelle har særbehov.** De har tariff fra Virke HUK eller NHO Geneo (ofte med lønnsstiger etter offentlig modell), offentlig tjenestepensjon (KLP og lignende), lønn fordelt på mange prosjekter og finansiører, timeregistrering som dokumentasjon overfor Forskningsrådet og EU, og mange honorarmottakere. AGA-fritaket for ideelle (800 000 kr totalt / 80 000 kr per ansatt) er bare relevant for de minste ([Lovdata ftrl. § 23-2](https://lovdata.no/lov/1997-02-28-19/§23-2)).

---

## 1. Lønnsprosessen måned for måned

### 1.1 Prosesskart: de 13 stegene

| # | Steg | Hvem | Hva skjer i praksis | Typiske feil og risiko |
|---|---|---|---|---|
| 1 | **Kjøreplan / lønnskalender** | Lønnsansvarlig | Frister publiseres for hele året (intranett eller e-post) og følges opp med påminnelser. Egne kjøringer for reise og utlegg samt honorar/bonus er vanlig i større virksomheter. UiB har fem kjøringer per måned: hovedlønn, to reisekjøringer og to bonus/honorar ([UiB](https://www.uib.no/foransatte/175460/utbetaling)). | Helligdager (utbetaling flyttes til virkedagen før), desember og juni |
| 2 | **Masterdata (stamdata)** | HR registrerer, lønn kontrollerer | Nyansatte, sluttere, stillingsprosent, lønnstrinn/ansiennitet, permisjoner, kostnadssted og prosjektfordeling, bankkonto, skattekort, pensjonsinnmelding, fagforening. I store virksomheter kommer dette fra HR-systemet via integrasjon. | Feil startdato eller stillingsprosent gir feil lønn, a-melding og pensjon. Feil kontonummer er både en svindelrisiko og gir feilutbetaling. |
| 3 | **Innhenting av variable data** | Ansatte, ledere, tid/vakt-system, reise/utlegg-system | Timelister (timelønnede), overtid, ubekvem arbeidstid, vakttillegg, fravær (sykdom, sykt barn, permisjon, ferie), reiser og utlegg, engangsbeløp fra HR (bonus, funksjonstillegg), trekk (fagforening, kantine, lån, utleggstrekk) | Ugodkjente timer ved cut-off, ukjente lønnsarter fra tidssystemet, ansatte uten match, dobbel import |
| 4 | **Cut-off** | Lønnsansvarlig | Det som ikke er godkjent innen fristen, går til neste måned eller en ekstrakjøring. | Press om unntak. Manglende sperre i systemet. |
| 5 | **Forhåndskontroll** | Lønnsmedarbeider | Importlogger, feillister og manglende godkjenninger gjennomgås. Ansatte uten skattekort (50 % trekk) og nye bankkontoer kontrolleres. | Feil oppdages for sent |
| 6 | **Testkjøring / simulering** | Lønnsmedarbeider | Hele lønnen beregnes uten å låses. Ofte 2–3 iterasjoner. | Systemer som ikke støtter ubegrenset reberegning eller simulering per person |
| 7 | **Avviksanalyse** | Lønnsmedarbeider og lønnsansvarlig | Sammenligning mot forrige måned per ansatt og lønnsart, store beløp, negativ netto, null-lønn, AGA-sone, ferietrekk, trekk over grense | Lange Excel-rapporter. Lite støtte for terskelverdier og forklaringer. |
| 8 | **Attestasjon / godkjenning** | Lønnsansvarlig (faglig), CFO/økonomisjef (økonomisk) | Kontrollskjema med totalsummer: brutto, netto, forskuddstrekk, AGA, pensjon, antall ansatte, avvik forklart | Godkjenning på e-post uten sporbarhet |
| 9 | **Endelig kjøring og låsing** | Lønnsmedarbeider | Perioden låses. Lønnsjournal, bilag, bankfil og a-meldingsgrunnlag produseres. | Endringer etter låsing |
| 10 | **Bankfil og remittering** | Lønn lager, økonomi godkjenner i bank | Bankfil (ISO 20022 pain.001) sendes til banken og kvitteres med pain.002 ([DNB filoverføring](https://www.dnb.no/bedrift/hjelp-og-veiledning/filoverforing)). Godkjenning i nettbanken krever egne rettigheter, f.eks. kontorettigheten «Lønn» i SpareBank 1 ([SpareBank 1 SN](https://sn.no/-/media/NYE-NETTSIDER/BM/Brukerveiledning-Lnnslister-ny-nettbank-bedrift.pdf)). **Fra 2026** betales forskuddstrekk og utleggstrekk senest første virkedag etter utbetaling. | Én person kan både lage og godkjenne bankfilen. Fil endret mellom system og bank. |
| 11 | **A-melding** | Lønnsmedarbeider | Fristen er den 5. i måneden etter, men i praksis sendes den samme dag eller dagen etter kjøringen. Tilbakemeldingen sjekkes for feil og avvik. Korrigeringer gjøres ved å sende erstatningsmelding. | Avvik som ikke følges opp, f.eks. ugyldig kombinasjon av lønnsart og beskrivelse ([Revisjon og Regnskap](https://www.revregn.no/asset/pdf/2014/7-45-6.pdf)) |
| 12 | **Regnskapsbilag** | Lønn lager, regnskap kontrollerer | Lønnsjournalen konteres per konto og dimensjon (selskap, avdeling, prosjekt, finansiør, aktivitet) og overføres til økonomisystemet. | Feil eller manglende dimensjoner, fordeling i prosent som ikke summerer til 100, periodisering |
| 13 | **Lønnsslipper og etterarbeid** | Lønn | Lønnsslipp i app, portal eller Digipost. Deretter avstemming (lønn mot hovedbok, a-melding mot regnskap, bank), pensjonsrapportering, oppfølging av NAV-refusjon, rapporter til ledere og prosjekter, arkiv. | Avstemming skyves til årsslutt. Differanser hoper seg opp. |

### 1.2 Lønnskalender og cut-off: konkrete eksempler

**UiB 2026 (DFØ-kunde, utbetaling den 12.):** Frist for registrering og ledergodkjenning av hovedlønn er kl. 20:00 omtrent 8–10 dager før utbetaling. Eksempler: frist 02.01 for utbetaling 12.01, frist 04.11 for utbetaling 12.11 og frist 02.12 for utbetaling 11.12. Reise og utlegg betales to ganger i måneden, og honorar og bonus også to ganger. Timelønn forutsetter innlevert timeliste for måneden ([UiB](https://www.uib.no/foransatte/175460/utbetaling)).

**NTNU 2026:** Ansatte leverer ca. 2 uker før utbetaling og ledere godkjenner ca. 8 dager før. Eksempel for november 2026: ansatt 28.10, leder 04.11, utbetaling 12.11. Timelønnede må levere timelisten senest siste virkedag i måneden for å få betalt måneden etter. Reisekjøringer går *fire ganger i måneden* ([NTNU](https://i.ntnu.no/wiki/-/wiki/English/Payment+schedule+for+salaries+and+refunds)).

**Typisk privat eller ideell virksomhet med 100–1000 ansatte** (erfaringsbasert):

| Utbetaling | Masterdata-frist (HR) | Frist ansatte | Frist leder | Testkjøring | Attestasjon | Bankfil |
|---|---|---|---|---|---|---|
| 20. eller 25. | U-16 | U-14 | U-10 (kl. 12) | U-9 til U-6 | U-5 | U-4 til U-3 |

U = utbetalingsdag; tallene er kalenderdager. Bankfilen sendes 2–3 bankdager før for å være sikker på at pengene er fremme. Desember-kjøringen flyttes ofte tidlig (utbetaling rundt 15.–18.12) og juni har feriepenger, så begge har egne kalendere.

**Prinsipp for variable data:** De fleste med turnus eller vakter betaler variable tillegg *én måned etterskuddsvis*. Fastlønn for november og vakttillegg for oktober utbetales i november. Dette gir tid til godkjenning, men skaper periodiseringsbehov i regnskapet ([Sticos](https://www.sticos.no/fagstoff/skal-a-meldingen-alltid-stemme-med-regnskapet)).

### 1.3 Kontrollrapporter lønnsavdelingen faktisk bruker

Dette er en erfaringsbasert «standardpakke» før attestasjon. Systemer som ikke har disse som innebygde, konfigurerbare kontroller, tvinger fram Excel.

- **Avvik mot forrige måned** per ansatt: brutto og netto ±X % eller ±Y kr, nye og bortfalte lønnsarter.
- **Ansatte med null eller negativ nettolønn** og ansatte med lønn etter sluttdato.
- **Nye eller endrede bankkontonumre** siden forrige kjøring, med hvem som endret og når.
- **Manglende eller utdatert skattekort** (prosenttrekk 50 %), frikort-grenser og kildeskatt.
- **Svært høye enkeltbeløp** (terskel), engangsutbetalinger og etterbetalinger.
- **Timer over grenser:** overtid utover arbeidsmiljølovens rammer og vakttillegg uten vakt.
- **Fravær:** sykefravær utover arbeidsgiverperioden uten refusjonskrav, og permisjon uten lønn som likevel får lønn.
- **AGA:** grunnlag per underenhet og sone, ansatte flyttet mellom underenheter.
- **Feriepenger:** grunnlag, ferietrekk, 60+ og sluttoppgjør.
- **Trekk:** utleggstrekk (nye og gamle regler), fagforening og påleggstrekk mot trekkfri grense.
- **Kostnadsfordeling:** fordelinger som ikke summerer til 100 %, avsluttede prosjekter og manglende dimensjoner.
- **Totalsummer mot budsjett og forrige måned**, antall lønnsmottakere og antall ansatte (headcount).

### 1.4 Typisk tidsbruk (anslag)

| Størrelse | Kjøringer per mnd. | Lønns-FTE (ekskl. HR) | Timer per hovedkjøring (lønn) | Kommentar |
|---|---|---|---|---|
| 20 ansatte, fastlønn | 1 | 0,05–0,1 (ofte byrå) | 3–6 t | Ofte byrå. Kunden sender endringer på e-post eller Excel. |
| 100 ansatte, noe variabel | 1–2 | 0,3–0,6 | 15–30 t | Én person, sårbar ved fravær |
| 400 ansatte, turnus og prosjekt | 2–4 | 1,5–3,0 | 60–120 t | Lønnsansvarlig og 1–2 medarbeidere. Fire-øyne mulig. |
| 1000 ansatte, flere selskaper | 4–8 | 3–6 | 150–300 t | Eget lønnsteam, systemforvalter, egne kjøringer for reise og honorar |

**Benchmark:** APQC oppgir ca. **350 lønnsmottakere per FTE** i lønnsprosessen som median (n=1 168, internasjonalt). Tallet bør verifiseres, og norske virksomheter med turnus, tariff og NAV-refusjoner ligger ofte lavere ([APQC](https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/number-employees-paid-fte-performs)). Lønnsbransjen i Norge har nær 4 000 sysselsatte, og 80 % er kvinner ([Regnskap Norge 2026](https://www.regnskapnorge.no/contentassets/b173a1e31cd741af9b610fc80db70ddf/lonnssystemer---resultater-til-publisering.pdf)).

Tiden går i liten grad til selve beregningen. Den fordeles typisk slik (anslag): 30–40 % til innhenting og purring av variable data, 25–35 % til kontroll og avviksanalyse, 10–15 % til korrigeringer og ekstrakjøringer, 10–15 % til avstemming og etterarbeid, og 5–10 % til henvendelser fra ansatte.

### 1.5 Skalering fra 20 til 1000 ansatte

| Dimensjon | 20 | 100 | 400 | 1000 |
|---|---|---|---|---|
| **Hvem kjører lønn** | Daglig leder og regnskapsbyrå | Økonomimedarbeider (deltid lønn) eller byrå | Lønnsansvarlig og 1–2 lønnsmedarbeidere, eventuelt co-sourcing med byrå | Lønnsteam på 3–6, systemforvalter, eventuelt shared service eller BPO (Zalaris, SD Worx, Azets, BDO/Tower) |
| **Innhenting** | E-post/Excel | Enkel app (timer og utlegg) | Tid/vakt-system (Tamigo, Quinyx, Planday, Visma Ressursstyring/GAT) og reise/utlegg-modul | Flere tidssystemer, HR-system som master, API |
| **Godkjenning** | Daglig leder | Nærmeste leder i app | Leder → lønn → CFO, attestasjonsregler per kostnadssted | Hierarkisk, stedfortreder, beløpsgrenser, konsernregler |
| **Kontroller** | Øyekontroll | Avvik mot forrige måned | Full kontrollpakke, fire-øyne, endringslogg | Formalisert internkontroll (kontrollmatrise, testing), ISAE-krav til leverandør |
| **Struktur** | Ett selskap | Ett selskap, noen avdelinger | 1–3 selskaper, mange avdelinger og prosjekter, flere underenheter | Konsern, flere AGA-soner, mange tariffer |
| **Kjøringer** | Én per måned | Én pluss ekstra ved behov | Hovedlønn, reise, honorar, ekstrakjøringer | Ukes- eller 14-dagerslønn for enkelte, mange spesialkjøringer |
| **Rapportering** | Lønnsslipp og a-melding | Lønnskost per avdeling | Prosjekt- og finansiørrapporter, sykefravær, FTE | BI og datavarehus, prognoser, likelønnsanalyser |

---

## 2. Årshjulet

### 2.1 Årshjul (praksis for en privat eller ideell virksomhet)

| Måned | Lønnsfaglige hendelser | Systemkrav |
|---|---|---|
| **Desember (forbereder januar)** | Skattekort for nytt år kan hentes. Satser og grunnbeløp som gjelder fra 1.1 legges inn (G gjelder fra 1.5). Halv skatt i desemberlønnen. Desemberlønnen kjøres tidlig. | Masseinnhenting av skattekort via API, datostyrte satser |
| **Januar** | Nye skattekort tas i bruk. Feriepengegrunnlaget for fjoråret låses. AGA for november–desember forfaller 15.1. Årsavstemming lønn mot regnskap og A07. Revisor starter årsoppgjøret. Pensjon: årsoppgaver og regulering. | Rapport for feriepengegrunnlag, årsavstemming, revisorpakke |
| **Februar–mars** | Revisjonen avsluttes. Lønnsinnslag i årsregnskapet (ytelser til ledende personer, styrehonorar, pensjon, antall årsverk). Årsberetning med likestillingsredegjørelse. Frist for timesatser til Forskningsrådet (instituttsektoren har hatt frist 28.2) ([Forskningsrådet](https://www.forskningsradet.no/forskningspolitikk-strategi/instituttsektoren/innmelding-timesatser)). | Noteopplysninger, rapport for ledende ansatte |
| **April** | Frontfaget forhandles. Planlegging av ferie. | — |
| **Mai** | Lønnsoppgjør i privat sektor. Virkningsdato for HUK-oppgjørene er ofte 1. mai. G reguleres (påvirker pensjon, 6G-grenser og 60+-feriepenger). | Datostyrt G, retro-klargjøring |
| **Juni** | **Feriepenger** utbetales (vanligvis i junilønnen). Ferietrekk gjøres, og juni er trekkfri etter tabelltrekket ([Skatteetaten](https://www.skatteetaten.no/nn/presse/nyhenderommet/derfor-trekkes-det-ikke-skatt-av-feriepengene/), [SNL](https://snl.no/tabelltrekk)). Ekstra ferieuke for ansatte over 60. Sommervikarer starter. | Feriepengemodul, ferietrekk, trekkfri måned, masseopprettelse av vikarer |
| **Juli–august** | Lavt bemannet lønnsavdeling. Sommervikarer slutter. Lokale forhandlinger og etterbetalinger begynner. | Robust kjøring med færre folk, sluttoppgjør med feriepenger |
| **September–oktober** | Lokale forhandlinger. I HUK 2026 skal de være gjennomført innen 31.10.2026 ([NTL – HUK-protokoll 2026](https://www.ntl.no/Content/236135/cache=1781783091000/attr=54859A4B558E247CE0630B00000A6027/HUK-oppgj%C3%B8r%202026%20-%20Protokoll%20-%20Landsoverenskomst%20for%20virksomheter.pdf)). Masseoppdatering og etterbetaling. Interimrevisjon hos revisor. Budsjett for neste år (lønnsbudsjett og prognose). | Masseimport av lønnsendringer, retroberegning, budsjetteksport |
| **November** | Etterbetalinger fra lokale oppgjør. AGA for september–oktober forfaller 15.11. Noen tar halv skatt i november. Julegaver og velferd. | Valgfri måned for halv skatt |
| **Annethvert år** | **Lønnskartlegging etter kjønn og ufrivillig deltid.** Gjelder alle offentlige virksomheter og private med mer enn 50 ansatte, og virksomheter med 20–50 ansatte når en av partene krever det ([Lovdata ldl. § 26a](https://lovdata.no/lov/2017-06-16-51/§26a)). | Analyse på grupper av arbeid av lik verdi |

### 2.2 Lønnsoppgjør: masseoppdatering og etterbetaling

Eksempel fra **Virke HUK 2026:** Virkningsdato for lønnsendringer er **1. mai 2026**, med mindre partene lokalt blir enige om noe annet. Ledere får 4,0 % av grunnlønnen per 30.4.2026. Det gis ikke etterbetaling til ansatte som sluttet før vedtakelsen. Lokale forhandlinger skal være gjennomført innen 31.10.2026 ([NTL – protokoll](https://www.ntl.no/Content/236135/cache=1781783091000/attr=54859A4B558E247CE0630B00000A6027/HUK-oppgj%C3%B8r%202026%20-%20Protokoll%20-%20Landsoverenskomst%20for%20virksomheter.pdf), [FO – uravstemningsdokument](https://www.fo.no/content/uploads/2026/06/Uravstemningsdokument-Virke-HUK-Landsoverenskomsten-for-Virksomheter-118.pdf)). Virke oppgir at hovedoppgjøret var godkjent for seks HUK-overenskomster 9. juli 2026 ([Virke](https://www.virke.no/tariff-og-lonn/tariffoppgjor-2026-dette-ma-du-vite/gjennomforte-forhandlinger/)).

Konsekvensen for lønn er at et oppgjør godkjent i juli med virkning fra 1. mai typisk betales ut i august eller september. Lokale tillegg kommer i november og har også virkning fra 1. mai. Lønnssystemet må da gjøre følgende:

1. **Masseoppdatere** lønnstabeller og stiger (sentrale tillegg per lønnstrinn eller ansiennitet), prosenttillegg for grupper (f.eks. ledere 4 %) og individuelle lokale tillegg. Det skjer via import fra HR eller forhandlingsprotokollen, med sporbarhet.
2. **Etterberegne** (retro) alle måneder fra virkningsdatoen. Det gjelder både fastlønn og alt som beregnes av timelønn: overtid, ubekvem arbeidstid, vakttillegg, deltidsmerarbeid og eventuelt feriepengegrunnlag og pensjonsgrunnlag.
3. **Utelate sluttede** etter tariffens regel (dato for vedtakelse).
4. **Rapportere riktig i a-meldingen.** Etterbetalingen rapporteres i utbetalingsmåneden, og **«siste lønnsendringsdato»** skal være den opprinnelige endringsdatoen, ikke utbetalingsdatoen ([Skatteetaten](https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/arbeidsforholdet/opplysninger-om-arbeidsforholdet/siste-lonnsendringsdato)).
5. **Oppdatere pensjon.** For innskuddspensjon via a-melding skjer dette automatisk. For offentlig tjenestepensjon (KLP og lignende) er det fil eller manuell rapportering.

Ved HUK-oppgjøret i 2022 innførte Virke en ny lønnsstruktur, og etter det kom egne «ofte stilte spørsmål om nytt lønnssystem». Det viser hvor mye tariffendringer driver systemarbeid ([Virke](https://www.virke.no/tariff-og-lonn/huk-omradet/huk-oppgjoret-nytt-lonnssystem)).

**Smertepunkt:** Retro er det som oftest nevnes som vanskelig. Brukerne av Visma.net Payroll beskriver datostyringen som rigid og retro som «feilsensitiv». Retro som endrer skattetrekk og AGA tilbake i tid gjør avstemmingen vanskelig ([Regnskap Norge](https://www.regnskapnorge.no/contentassets/b173a1e31cd741af9b610fc80db70ddf/lonnssystemer---resultater-til-publisering.pdf)).

### 2.3 Feriepenger (juni)

- **Satser:** 10,2 % etter loven og 12 % ved avtalefestet femte ferieuke. Ansatte over 60 får tillegg for den ekstra uken, med grunnlag begrenset til 6G. Feriepengene utbetales normalt i juni i stedet for vanlig lønn. Juni er trekkfri etter tabelltrekket, som bygger på 10,5 måneder ([Skatteetaten](https://www.skatteetaten.no/nn/presse/nyhenderommet/derfor-trekkes-det-ikke-skatt-av-feriepengene/), [SNL](https://snl.no/tabelltrekk)).
- **Ferietrekk** (trekk i lønn for ferie) skal ikke rapporteres som negativ fastlønn ([Skatteetaten – trekk i lønn for ferie](https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/lonn-og-ytelser/oversikt-over-lonn-og-andre-ytelser/trekk-i-lonn-for-ferie)).
- **Dette tar tid i praksis:** kontroll av feriepengegrunnlaget for hver ansatt (permisjoner, NAV-perioder med feriepenger fra NAV, sluttede, nyansatte med feriepenger fra tidligere arbeidsgiver), forskuddsferie og avstemming av feriepengeavsetningen mot hovedboken. Regnskap Norges undersøkelse nevner feil i feriepengeberegningen som et konkret problem i enkelte systemer, bl.a. 60+ i ett system ved oppstart i 2025.

### 2.4 Halv skatt (desember)

Tabelltrekket er beregnet for 10,5 måneder: juni er trekkfri på grunn av feriepenger, og desember har halvt trekk. Arbeidsgiver kan legge det halve trekket til en annen måned, typisk november ([SNL – tabelltrekk](https://snl.no/tabelltrekk)). Ansatte med prosenttrekk, kildeskatt eller ekstra trekk må håndteres særskilt.

### 2.5 Skattekort (januar)

Arbeidsgiver henter skattekort elektronisk for alle arbeidsforhold. Skattekort for neste år kan hentes fra desember, og endringer må fanges opp løpende. Ansatte uten skattekort skal ha 50 % trekk. Systemkrav: automatisk henting for nyansatte, varsel når skattekort mangler, og logg over hvilket skattekort som ble brukt i hver kjøring.

### 2.6 Årsavslutning

Det gjøres ikke lenger egne lønnsoppgaver. Alt går gjennom a-meldingen, og den ansatte får sammenstillingsoppgaven fra Skatteetaten. Årsavslutningen består derfor av:

- **Avstemming av lønn og AGA mot A07-oversikten fra Altinn.** Sum innrapportert lønn, AGA-grunnlag og AGA avstemmes mot resultatregnskapet ([Sticos – avstemming](https://support.sticos.no/hubfs/Avstemming%20av%20l%C3%B8nn%20%26%20arbeidsgiveravgift.pdf)). Differanser skyldes typisk kontantprinsippet i a-meldingen mot periodisering i regnskapet ([Sticos](https://www.sticos.no/fagstoff/skal-a-meldingen-alltid-stemme-med-regnskapet)).
- **Avstemming av feriepengeavsetningen** (konto 2940) og AGA av feriepenger.
- Skyldig forskuddstrekk, utleggstrekk og AGA. Fra 2026 er det ikke lenger noen skattetrekkskonto å avstemme mot. Kontrollen er nå at trekkene er betalt innen fristen.
- Pensjon: avsetning og premieavstemming.
- Rapporter til noter: ytelser til ledende personer, styrehonorar, revisjonshonorar (ikke lønn) og årsverk.
- Korrigeringer av tidligere måneder sendes som erstatningsmeldinger før fristen. Revisor ser etter sene korrigeringer.

### 2.7 Pensjon

- **Innskuddspensjon (OTP):** Siden 2021 skal private arbeidsgivere med OTP-plikt oppgi pensjonsinnretning i a-meldingen ([Skatteetaten](https://www.skatteetaten.no/nn/bedrift-og-organisasjon/arbeidsgiver/a-meldinga/rettleiinga-til-a-meldinga/pensjonsinnretning-obligatorisk-tenestepensjon)). DNB oppdaterer innskuddspensjon ut fra a-meldingen hver måned, med automatisk inn- og utmelding. Pensjonsgrunnlaget er faktisk utbetalt lønn, omregnet med faktor 12,16. Andre produkter, som personalforsikringer, må oppdateres manuelt ([DNB](https://www.dnb.no/bedrift/a-aa/pensjon/a-melding)). Nordea påpeker at overtid, bonus og utgiftsgodtgjørelser ikke skal inngå i lønnsgrunnlaget ([Nordea](https://www.nordea.no/bedrift/kundeservice/sporsmal-og-svar/Innskuddspensjon.html)). Feil stillingsprosent i a-meldingen gir derfor feil pensjon.
- **Offentlig tjenestepensjon (KLP, SPK, Storebrand OfTP):** Dette er vanlig for ideelle virksomheter under HUK. Hos KLP rapporteres lønn normalt én gang per kvartal, med anbefaling om å melde lønnsendringer løpende ([KLP](https://www.klp.no/virksomhet/pensjon/hr-lonn-og-personal/rapportering-av-ansattopplysninger)). Det krever fil eller integrasjon og egen avstemming av premie mot lønn.

### 2.8 Likestilling og lønnskartlegging

- **Krav i dag:** Lønnskartlegging etter kjønn og ufrivillig deltid **annethvert år** for offentlige virksomheter og private med mer enn 50 ansatte (20–50 på krav), og redegjørelse i årsberetningen ([Lovdata ldl. § 26a](https://lovdata.no/lov/2017-06-16-51/§26a)).
- **EUs lønnstransparensdirektiv (2023/970):** Fristen i EU var 7. juni 2026. Direktivet er ennå ikke tatt inn i EØS-avtalen, men Norge ventes å få tilsvarende regler ([NHH](https://nhh.no/nhh-bulletin/artikkelarkiv/2026/juni/likelonnsdirektivet-eu-landene-bommer-pa-fristen/)). For et system som lanseres nå, bør datamodellen likevel støtte stillingskategorier og «arbeid av lik verdi», lønnskomponenter per kjønn og gap-analyse med 5 %-terskel.

### 2.9 Revisjon

Revisjonen deles typisk i en interimrevisjon (høst) med test av kontroller og en årsrevisjon (januar–mars) med avstemminger og analyser. Detaljer i kapittel 4.

---

## 3. Roller, ansvarsdeling og tilgangsstyring

### 3.1 Roller og ansvar (RACI, forenklet)

| Aktivitet | Ansatt | Leder | HR | Lønnsmedarb. | Lønnsansvarlig | Controller/regnskap | CFO/økonomisjef | Revisor |
|---|---|---|---|---|---|---|---|---|
| Registrere timer, fravær og utlegg | **R** | A | | I | | | | |
| Godkjenne timer, fravær og utlegg | | **R/A** | | I | | | | |
| Nyansettelse, stillings- og lønnsendring (vedtak) | | C | **R/A** | I | | | | |
| Registrere masterdata i lønn | | | R | **R** | A | | | |
| Endre bankkonto | **R** (selvbetjening med BankID) | | | C (kontroll) | A | | | |
| Lønnskjøring og avviksanalyse | | | | **R** | A | C | | |
| Fire-øyne-kontroll | | | | R (kollega) | **A** | | | |
| Attestasjon av totalsummer | | | | | R | C | **A** | |
| Godkjenne bankfil i bank | | | | | | R | **A** (to signaturer) | |
| A-melding | | | | **R** | A | I | | |
| Bilag, periodisering og avstemming | | | | R | C | **R/A** | I | |
| Tilgangsgjennomgang | | | C | | R | | **A** | I |
| Revisjon | | | | C | C | C | C | **R** |

R = utfører, A = ansvarlig, C = konsulteres, I = informeres.

**Eksempel fra praksis, Bærum kommune:** Lønnsenheten har egne stillinger for *faglig systemgruppe – utvikling* (oppsett av moduler, test ved oppgraderinger, feilretting, rapportmaler, store organisasjonsendringer) og *kontroll og oppfølging av reise og utlegg* (kontroll av elektronisk innsendte krav, purring, rådgivning, direkte remittering). Målet er at ansatte selv registrerer variable data og vedlikeholder egne personopplysninger ([Bærum – systemgruppe](https://www.baerum.kommune.no/globalassets/bilder/diverse-dokumenter-og-mediefiler/stab-stotte-stillinger/lonnsenheten/07.8-lonnsenheten-radgiver-faglig-systemgruppe-utvikling.pdf), [Bærum – reise og utlegg](https://www.baerum.kommune.no/globalassets/bilder/diverse-dokumenter-og-mediefiler/stab-stotte-stillinger/lonnsenheten/07.11-lonnsenheten-konsulent-kontroll-og-oppfolging-reise-og-utlegg.pdf)). I store virksomheter er **systemforvalter for lønn** en egen rolle, og systemet må ha et forvalter-grensesnitt (lønnsarter, regler, maler, testmiljø) som er adskilt fra den daglige kjøringen.

### 3.2 Arbeidsdeling (segregation of duties): de kritiske kombinasjonene

Disse kombinasjonene bør være **umulige for samme person**, eller kreve en kompenserende kontroll:

1. **Endre bankkonto og kjøre lønn.** Dette er den klassiske svindelvektoren. Beste praksis er at den ansatte selv endrer kontonummer med BankID, eller at to personer er involvert (registrerer og godkjenner), og at alle endringer vises i kontrollrapporten før neste kjøring.
2. **Opprette ansatt og kjøre lønn eller godkjenne utbetaling**, som åpner for fiktive ansatte.
3. **Lage bankfil og godkjenne den i banken.** Banken bør kreve to signaturer. En svensk kommunerevisjon anbefalte nettopp at to personer signerer filen som sendes til banken ([Tierp kommun](https://www.tierp.se/download/18.2327b1a186880afa36a5073/1679989412503/7a.%20Revisionsrapport%20-%20Granskning%20av%20intern%20kontroll%20i%20l%C3%B6nehanteringsprocessen.pdf)).
4. **Endre egen lønn eller eget ansattkort.** Lønnsmedarbeidere skal ikke kunne endre sine egne data. Tilsvarende sperre gjelder for nære relasjoner.
5. **Lønn og bokføring:** Den som kjører lønn bør ikke alene kunne bokføre og avstemme lønnskontoene.

Sykehuset Innlandets interimrevisjon fant manglende arbeidsdeling mellom bokføring og endring av stamdata og bankopplysninger. Tilgangene ble ryddet, svakheten ble redusert til tre personer, og revisor anbefalte kompenserende kontroller ([Sykehuset Innlandet](https://www.sykehuset-innlandet.no/4946ed/siteassets/styret/2018/2018-03/025-2018-vedlegg-03-oppsummering-interimrevisjon.pdf)). En sak fra Trondheim kommune fant at enhetsledere ofte ikke gikk gjennom lønnslistene, og pekte på at det betyr manglende arbeidsdeling ([Trondheim kommune](https://publikum.trondheim.kommune.no/application/get_saksfremlegg/35235)).

**Innebygd SoD-sjekk er et konkurransefortrinn.** Systemet bør kunne vise «hvem kan både X og Y» og blokkere eller varsle.

### 3.3 Tilgang til sensitive data

- **Konfidensielle grupper:** toppledere, styret, lønnsavdelingen selv, ansatte med sperret adresse eller skjermingsbehov, og eventuelt personalsaker (trekk, lån, utleggstrekk). Data om disse ses bare av en navngitt liten gruppe, ofte lønnsansvarlig og CFO. Kontrollrapporter, bilag og bankfil må da enten aggregere eller maskere dem.
- **Lederes innsyn:** Ledere ser lønnskost og FTE for egne enheter, men ikke nødvendigvis individuell lønn. Mange virksomheter gir innsyn i individuell lønn kun til ledere med personalansvar og HR.
- **Bank:** Brukere uten lønnsrettighet bør ikke se detaljer i lønnsbetalinger. Rettigheter som «Lønn» gis kontovis ([SpareBank 1 SN](https://sn.no/-/media/NYE-NETTSIDER/BM/Brukerveiledning-Lnnslister-ny-nettbank-bedrift.pdf)).
- **Regnskap:** Lønn bokføres ofte samlet per avdeling og lønnsart, slik at detaljene ikke vises i hovedboken. Individuell lønn finnes i lønnssystemet.
- **Byrå-scenario:** Byråets lønnsmedarbeidere skal ha tilgang til kunden, men kundens ledere skal ikke se andre kunder. Kunden godkjenner, og byrået kjører. Byrået har behov for oversikt over mange kunder: status, frister og avvik på tvers.
- **Revisor:** Revisor trenger lesetilgang eller eksport for perioden, og helst et eget revisorinnsyn med logg.

---

## 4. Internkontroll og revisjon

### 4.1 Kontrollkatalog (det revisor forventer å se)

| Kontroll | Frekvens | Eier | Bevis | Hva systemet bør gjøre |
|---|---|---|---|---|
| Avviksanalyse mot forrige måned og budsjett | Hver kjøring | Lønnsansvarlig | Signert kontrollrapport | Innebygd rapport med terskler og forklaringsfelt |
| Fire-øyne-gjennomgang av endringer i masterdata | Hver kjøring | Lønnsmedarb. B | Endringslogg med «kontrollert av» | Endringslogg per felt (før/etter, hvem, når), kvittering |
| Kontroll av endrede bankkontoer | Hver kjøring | Lønnsansvarlig | Liste med signatur | Egen rapport. Gjerne verifisering mot kontoeier. |
| Attestasjon av lønnsutbetaling (totaler) | Hver kjøring | CFO | Elektronisk godkjenning | Godkjenningsflyt i systemet, sperre for bankfil uten godkjenning |
| To signaturer på bankfil | Hver kjøring | Økonomi | Banklogg | Integrasjon som ikke tillater endring av fil |
| Lønnsjournal mot hovedbok | Månedlig | Regnskap | Avstemmingsark | Automatisk bilag, avstemmingsrapport |
| A-melding (tilbakemelding) mot lønnsjournal og regnskap | Månedlig | Lønn/regnskap | A07-avstemming | Hente tilbakemelding og A07, vise avvik |
| AGA per sone og underenhet | Månedlig/termin | Regnskap | Avstemming | Rapport per underenhet og sone |
| Forskuddstrekk og utleggstrekk betalt innen første virkedag | Hver kjøring | Økonomi | Betalingskvittering | Lage betalingene automatisk med riktig KID og forfall |
| Feriepengeavsetning | Månedlig/årlig | Regnskap | Avstemming mot konto 2940 | Rapport for feriepengegrunnlag og avsetning |
| Pensjonspremie mot lønnsgrunnlag | Kvartal/år | Regnskap | Avstemming | Pensjonsgrunnlag per ansatt |
| Tilgangsgjennomgang | Halvår/år | Lønnsansvarlig og CFO | Signert liste | Tilgangsrapport og SoD-konflikter |
| NAV-refusjon (sykepenger, foreldrepenger) | Månedlig | Lønn | Fordringsliste | Refusjonskrav, matching mot innbetaling |
| Sluttere: lønn stoppet, sluttoppgjør riktig | Hver kjøring | Lønn | Rapport | Varsel om lønn etter sluttdato |

### 4.2 Hva revisor typisk ber om (revisorpakke)

- Rutinebeskrivelse for lønnsprosessen, tilgangsoversikt og SoD-oversikt.
- Lønnsjournal per måned, eventuelt sammendrag for året per lønnsart.
- Avstemming av lønn, AGA og feriepenger mot regnskapet (A07). Differanser mellom lønnssystem og regnskap bør ryddes løpende, ikke ved årsslutt ([Revisjon og Regnskap](https://www.revregn.no/asset/pdf/2014/7-45-6.pdf)).
- Utvalg av ansatte (stikkprøver): arbeidskontrakt mot lønn i systemet, endringsvedtak, timelister og godkjenning, bankkonto.
- Endringslogg for masterdata og bankkonto i perioden.
- Dokumentasjon av attestasjon per kjøring.
- Liste over nyansatte og sluttere (cut-off-test: ingen lønn etter sluttdato).
- Ytelser til ledende personer og styret (note) og eventuelle lån til ansatte.
- **ISAE 3402 type II fra lønnsleverandøren** når lønnen er satt ut eller kjøres i skyen.

Kommunerevisjoner viser hvilke funn som går igjen: Feil betalt AGA og manglende avstemming mellom lønn og regnskap har gitt anbefaling om å gjennomgå avstemmingsrutinene ([Konsek](https://www.konsek.no/wp-content/uploads/2025/01/0005-32_25-Revisjonsnotat-til-arsregnskapet-2024.pdf)). Oslo kommunerevisjon har lønn og sosiale kostnader som et eget transaksjonsområde ([Oslo kommunerevisjon 4/2026](https://www.oslo.kommune.no/politikk/budsjett-regnskap-og-rapportering/rapporter-fra-kommunerevisjonen/rapport-4-2026-regnskapsrevisjonen-2025---med-vekt-pa-okonomisk-internkontroll/)).

### 4.3 ISAE 3402 / SOC 1 fra leverandør

- **Hva det er:** en uavhengig revisorrapport om tjenesteleverandørens kontroller som er relevante for kundens finansielle rapportering. Type I vurderer design, og type II vurderer at kontrollene har virket over en periode ([KPMG](https://kpmg.com/no/nb/tjenester/revisjon/attestation-services.html)).
- **Hvem har det:** Zalaris oppgir ISAE 3402 type II, ISO 9001 og ISO 27001 for sine lønnstjenester. Selskapet har også et «Payroll Control Centre» med løpende kontroller av masterdata, lønn og tid, inkludert validering av skatte-ID og bankdetaljer ([Zalaris](https://zalaris.com/managed-services/hr-&-payroll-outsourcing/managed-payroll-&-hr-services)). SAP publiserer halvårlige SOC 1-rapporter for SuccessFactors Employee Central Payroll ([SAP](https://www.sap.com/about/trust-center/certification-compliance/sap-successfactors-ecp-soc-1-2023-h2.html)). Visma Nmbrs har ISAE 3402 type II ([Nmbrs](https://support.nmbrs.com/hc/en-us/articles/360011742239)).
- **Implikasjon:** For kunder med 250+ ansatte, offentlig eide selskaper og byråer som selger lønn som tjeneste, er en årlig **ISAE 3402 type II** (generelle IT-kontroller: endringshåndtering, tilgang, drift, backup) et reelt salgskrav fra år 2–3. ISO 27001 og databehandleravtale kommer i tillegg. Kostnaden for rapporten bør med i forretningsplanen.

### 4.4 Feil som skjer: et konkret norsk eksempel

**Kristiansand kommune:** 2 338 ansatte, hovedsakelig helsefagarbeidere, sykepleiere og vernepleiere, fikk feil tillegg for forskjøvet arbeidstid på grunn av **feil koding i grensesnittet** mellom timelisteløsningen (Visma Enterprise Ressursstyring) og lønnssystemet (HRM), begge fra Visma. Feilen ble sett i testlønnskjøringen i januar 2020 og oppdaget av en avdelingsleder ([Kristiansand – rapport om lønnshendelse](https://www.kristiansand.kommune.no/contentassets/d6fb88872a7b4f88b84e57f20e50318e/rapport.lonnshendelse.pdf)). **Læringen** er at de største feilene skjer i overgangen mellom tid og lønn (mapping av lønnsarter), ikke i lønnsmotoren. Kontroll av mappingen, en test av hver ny lønnsart og lederinnsyn før utbetaling er avgjørende.

---

## 5. Integrasjonslandskapet

### 5.1 Arkitektur i en typisk virksomhet med 400 ansatte

```
            ┌───────────── Myndigheter (Altinn 3 / Maskinporten) ─────────────┐
            │ a-melding + tilbakemelding · skattekort · trekkpålegg (utlegg)   │
            │ NAV inntektsmelding (API) · A07 · sykmelding                      │
            └──────────────▲──────────────────────────────────▲──────────────┘
                           │                                  │
 HR/HRM (master)  ──────►  │                                  │
 Simployer, Sympa,         │         ┌──────────────────┐     │
 CatalystOne, HiBob,  ───► ├───────► │   LØNNSSYSTEM    │ ────┘
 Workday, SuccessFactors   │         │ motor · kontroll │ ─────► Regnskap/ERP (bilag + dimensjoner)
                           │         │ godkjenning      │        Xledger, Unit4, Visma Business,
 Tid/vakt  ───────────────►│         │ selvbetjening    │        Tripletex, PowerOffice, BC, SAP
 Tamigo, Quinyx, Planday,  │         └──┬───┬───┬───┬───┘
 Visma Ressursstyring/GAT  │            │   │   │   └──────► Pensjon: a-melding (innskudd) /
                           │            │   │   │            fil (KLP/SPK/OfTP), forsikring
 Reise/utlegg ────────────►│            │   │   └──────────► Bank: pain.001 → pain.002/camt.054
 Visma Expense, Pleo,      │            │   │                (DNB, Nordea, SB1, Mastercard DR)
 Folio, innebygd modul     │            │   └──────────────► Lønnsslipp: app, Digipost, e-Boks
                           │            └──────────────────► BI/rapport, budsjett, SSO (Entra ID)
```

### 5.2 Integrasjoner per kategori: praksis og krav

| Kategori | Typiske produkter i Norge | Integrasjonsform i dag | Kritiske detaljer |
|---|---|---|---|
| **Myndigheter** | Skatteetaten (a-melding, skattekort, trekkpålegg), NAV (inntektsmelding, refusjon), Altinn 3 | API med Maskinporten. Altinn 2 ble stengt 19.6.2026. | Inntektsmelding sendes som svar på forespørsel fra NAV. Det kreves begrunnelse hvis man avviker fra snittet av tre måneder fra a-ordningen ([Digdir](https://samarbeid.digdir.no/sites/samarbeid/files/2025-12/Viktig%20informasjon%20-%20Overgang%20fra%20Altinn%20II%20til%20Altinn%203.pdf)). API for foreldrepenger og pleiepenger var under utvikling ([NAV](https://www.nav.no/arbeidsgiver/moderniserte-tjenester)). Trekkpålegg-API og nye koder for utleggstrekk fra 2026 ([Skatteetaten](https://www.skatteetaten.no/om-skatteetaten/fremtidens-innkreving/systemleverandorer/lonns--og-personalsystem/)). |
| **Tid/vakt** | Tamigo, Quinyx, Planday, Visma Enterprise Ressursstyring/GAT, MinTid, Timeplan, Simployer | Fil (CSV/flatfil) i lønnssystemets importformat, noe API | Mapping av lønnsarter, ansattnumre og kostnadssteder må stemme. Planday anbefaler en liten testeksport før første kjøring ([Planday–Visma](https://www.planday.com/how-it-works/integrations/visma), [Planday–Tripletex](https://www.planday.com/how-it-works/integrations/tripletex), [Planday–Visma Lønn](https://www.planday.com/how-it-works/integrations/vismalon)). Tripletex-brukere klager over at det bare kan gjøres én import før en ny lønnskjøring opprettes ([Regnskap Norge](https://www.regnskapnorge.no/contentassets/b173a1e31cd741af9b610fc80db70ddf/lonnssystemer---resultater-til-publisering.pdf)). |
| **HR/HRM** | Simployer, Sympa, Talentech, CatalystOne, HiBob, Personio, Workday, SAP SuccessFactors, Cornerstone | API eller fil. HR er ofte master for person, stilling og organisasjon, og lønn er master for lønnsberegning. | NORCE (800+ ansatte) kjøpte HRM separat, mens lønn og tid ligger i Unit4 ERP, og ønsket at overgangen skulle være så sømløs som mulig for brukerne ([TED](https://ted.europa.eu/en/notice/-/detail/373762-2024)). |
| **Reise/utlegg** | Visma Expense, Tripletex, Pleo, Folio, Expensify, innebygd i lønn eller ERP | Reiseregninger går til lønn (trekkpliktige og trekkfrie godtgjørelser i a-meldingen). Rene utlegg går ofte til leverandørreskontro. | Avvik mellom regnskap (godkjent) og a-melding (utbetalt) ([Sticos](https://www.sticos.no/fagstoff/skal-a-meldingen-alltid-stemme-med-regnskapet)). |
| **Regnskap/ERP** | Xledger, Unit4, Visma Business/Global, Tripletex, PowerOffice, Business Central, SAP | Bilag via API eller fil med dimensjoner | Ferde krevde at systemet kommuniserer direkte med Xledger ([TED](https://ted.europa.eu/en/notice/-/detail/169076-2025)). Tensio krevde filintegrasjon mot Unit4 ([TED](https://ted.europa.eu/en/notice/-/detail/291054-2024)). |
| **Pensjon** | Storebrand, DNB, Gjensidige, Nordea Liv, KLP, SPK | Innskuddspensjon via a-melding. Offentlig tjenestepensjon via fil eller portal. | DNB: data fra a-meldingen brukes bare for innskuddspensjon, og forsikringer må oppdateres manuelt ([DNB](https://www.dnb.no/bedrift/a-aa/pensjon/a-melding)). KLP: kvartalsvis rapportering ([KLP](https://www.klp.no/virksomhet/pensjon/hr-lonn-og-personal/rapportering-av-ansattopplysninger)). |
| **Bank** | DNB, Nordea, SpareBank 1, Handelsbanken, Mastercard Payment Services (Direkte remittering) | pain.001 inn, pain.002 kvittering, camt.054 for avstemming. Direktekobling eller opplasting. | Godkjenning i bank med to signaturer og lønnsrettigheter ([Mastercard DR](https://www.mastercard.com/no/nb/business/payments/commercial-payments/mastercard-payment-services-avdelingsside/mastercard-direkte-remittering/mastercard-direkt-remittering-produktside.html)). Nordea varsler validering av betalingsfiler etter hvitvaskingsloven fra 9.9.2026, så filformatet må følges nøye ([Nordea](https://support.e-markets.nordea.com/hc/en-us/articles/38984795305501-To-users-of-Norwegian-accounts-Validation-of-payment-files-according-to-the-Norwegian-AML-ACT-requirement-will-start-on-the-9th-of-September-2026)). Fra 2026 kommer egne betalinger for forskuddstrekk og utleggstrekk med KID. |
| **Lønnsslipp** | Digipost, e-Boks, app eller portal, e-post (PDF) | API | Digipost er integrert i flere lønnssystemer (Aditro/SD Worx, Visma Services). Det finnes partnerløsninger for SAP ([SAP/Sariba](https://www.sap.com/canada/products/hcm/partners/sariba-as-pay-slips-and-annual-statements-in-digipost.html)). |
| **ID/SSO** | Entra ID (Azure AD), Google, BankID, ID-porten | OIDC/SAML, SCIM for brukere | SSO for ledere og ansatte. BankID ved endring av kontonummer og ved innsyn for sluttede. |
| **BI/rapport** | Power BI, Excel, Qlik | OData, API eller dataeksport | Store virksomheter vil ha rådata, ikke bare PDF-rapporter. |

### 5.3 Må ha og fint å ha, per segment

| Integrasjon | 10–50 ansatte | 50–250 | 250–1000 | Regnskapsbyrå (lisens) |
|---|---|---|---|---|
| A-melding, skattekort, A07, tilbakemelding (API) | **Må** | **Må** | **Må** | **Må**, med massehåndtering på tvers av klienter |
| Trekkpålegg-API og utleggstrekk (2026-regler) | **Må** | **Må** | **Må** | **Må** |
| NAV inntektsmelding-API og refusjonsoppfølging | **Må** | **Må** | **Må** | **Må** |
| Regnskap/ERP (bilag med dimensjoner) | **Må** (Tripletex, PowerOffice, Fiken, Xledger) | **Må** | **Må** (Xledger, Unit4, Visma Business, BC) | **Må**, mange ERP-er |
| Bank (pain.001/002, camt.054) | Må (fil holder) | **Må** (direkte) | **Må** (direkte og godkjenningsflyt) | **Må** (klientens bank) |
| Betaling av forskuddstrekk og utleggstrekk med KID | **Må** | **Må** | **Må** | **Må** |
| Tid/vakt | Fint (CSV) | **Må** for turnus/handel, ellers fint | **Må** (API, flere systemer) | Må (CSV-maler) |
| Reise/utlegg | Må (innebygd holder) | **Må** | **Må** | **Må** |
| HR/HRM masterdata-sync | Ikke nødv. (innebygd HR-light) | Fint | **Må** | Fint |
| Innskuddspensjon (via a-melding) | Må (fås gratis) | Må | Må | Må |
| Offentlig tjenestepensjon (KLP/SPK) | Må for HUK/ideelle | **Må** for HUK/ideelle | **Må** for HUK/ideelle | Må |
| Digital lønnsslipp (Digipost/e-Boks/app) | Fint (e-post/PDF holder) | **Må** | **Må** | **Må** |
| SSO (Entra ID) | Fint | Fint/må | **Må** | Må for byråets egne ansatte |
| BI/dataeksport | Fint | Fint | **Må** | Fint |
| Budsjett/prognose | Fint | Fint | Må | Fint |

---

## 6. Organisasjonskompleksitet

### 6.1 Flere juridiske enheter og konsern

- Hver juridisk enhet har eget organisasjonsnummer, egen a-melding, egen bankkonto og egne bilag. Ansatte kan bytte selskap, og det gir nytt arbeidsforhold. Lønnsavdelingen kjører ofte lønn for alle selskapene samme dag, med felles kalender og felles kontrollrapport.
- **Krav:** konsernvisning (samlet kontroll og attestasjon), felles lønnsart- og regelsett med lokale avvik, intern fakturering eller viderefakturering av lønnskostnader og konsoliderte rapporter. BIR AS og Tensio AS anskaffet HR og lønn for hele konsernet ([TED – BIR](https://ted.europa.eu/en/notice/-/detail/440999-2026), [TED – Tensio](https://ted.europa.eu/en/notice/-/detail/291054-2024)). Narvik-anbudet omfattet kommune, KF, IKS, kirkelig fellesråd og sokn i én avtale ([TED](https://ted.europa.eu/en/notice/-/detail/396670-2024)).

### 6.2 Underenheter og AGA-soner

- Arbeidsforhold rapporteres på underenhet (virksomhet), og AGA-sonen følger i hovedsak underenhetens kommune. Virksomheter med avdelinger i flere soner (f.eks. Oslo og Nord-Norge) må ha riktig underenhet per arbeidsforhold, ellers blir AGA feil.
- Spesialtilfeller: ansatte som jobber i flere soner, fribeløp og bagatellmessig støtte i soner med redusert sats, og flytting mellom underenheter midt i måneden.
- **Krav:** sone per underenhet, kontroll av fribeløp og AGA-rapport per sone.

### 6.3 Kostnadsfordeling (avdeling, prosjekt, kostnadssted, aktivitet)

Praksis spenner fra enkelt til komplekst:

1. **Fast prosentfordeling per ansatt**, f.eks. 60 % prosjekt A, 40 % drift. Fordelingen gjelder fra en dato og legges inn av HR eller controller.
2. **Timebasert fordeling** fra timeføring per prosjekt, med faktiske timer per måned.
3. **Lønnsart-spesifikk fordeling**, f.eks. vakttillegg på enheten der vakten ble gått.
4. **Retroaktiv omfordeling.** Når et prosjekt blir innvilget i mars med virkning fra januar, må lønnskostnad for januar og februar flyttes. Det gjøres ofte som manuelt bilag i regnskapet. Et lønnssystem som kan omfordele med sporbarhet, uten å kjøre lønn på nytt, sparer mye tid.

**Krav:** dimensjoner fritt definerbare (2–6 nivåer), fordelingsprofiler med datogyldighet, kontroll av at fordelingen summerer til 100 %, avsluttede prosjekter og at AGA, feriepenger og pensjon følger fordelingen.

### 6.4 Prosjektlønn og tilskudd (kritisk for stiftelser og forskningsinstitutter)

- **Forskningsrådet (næringsliv og offentlig sektor):** Mottaker **må ha et system for registrering av arbeidstid i prosjektet**. Uten det kan man ikke bruke timesatser. Timesatsen er anbefalt til ca. 0,8 promille av avtalt årslønn ved lave indirekte kostnader og inntil 1,1 promille ved høye. Det er tak på 1 100 kr per time (personal og indirekte) og maks 1 850 timer per år per person på Forskningsråds-prosjekter. Satsene bør verifiseres mot gjeldende utlysning ([Forskningsrådet](https://www.forskningsradet.no/finansiering/hvordan-skrive-soknad/budsjett/kostnader-naringsliv-offentlig-sektor/)). Instituttsektoren melder inn timesatser årlig ([Forskningsrådet](https://www.forskningsradet.no/forskningspolitikk-strategi/instituttsektoren/innmelding-timesatser)).
- **EU Horizon Europe:** Dagssats er årlige personalkostnader delt på 215, ganger antall dager på prosjektet. Tiden må kunne identifiseres og etterprøves, med timelister eller erklæring ([EMDESK](https://www.emdesk.com/horizon-2020-horizon-europe-basics-guide/how-to-calculate-horizon-europe-personnel-costs)).
- **Innovasjon Norge, Helsedirektoratet, Stiftelsen Dam, kommunale tilskudd:** krever typisk prosjektregnskap med lønnskostnader per prosjekt og eventuelt timer, ofte revisorbekreftet.
- **Praksis:** Lønnskostnad per person per måned, inkludert sosiale kostnader (AGA, feriepenger, pensjon), eksporteres til et prosjektøkonomiark eller ERP-modul. Timeark signeres av ansatt og leder. Dagens systemer klarer sjelden å levere en ferdig «prosjektlønnsrapport per finansiør» med timer, kost per time og sosiale kostnader. **Dette er en klar mulighet** for et nytt system rettet mot stiftelser og forskning.

### 6.5 Budsjett, prognoser og headcount

- **Lønnsbudsjett:** HR og controller lager budsjett per stilling (FTE, lønn, tillegg, forventet oppgjør, AGA, pensjon, feriepenger) i Excel eller budsjettverktøy, basert på eksport fra lønn. Oppgjørsavsetninger beregnes med feriepenger og AGA. Regjeringens beregning for 2024 brukte 12 % feriepenger og 14,1 % AGA ([Regjeringen](https://regjeringen.no/contentassets/1748128b0f124a3bbe9157b0822486ad/lonnsavsetning-for-lonnsoppgjoret-2024.pdf)).
- **Prognose:** Faktisk hittil i år pluss resten av året for kjente ansatte, inkludert planlagte endringer (sluttere, nyansatte, oppgjør).
- **Headcount og FTE:** antall ansatte, årsverk og stillingsprosent per enhet, kjønn og alder, turnover og sykefravær. Dette brukes i styrerapporter, årsberetning, likestillingsredegjørelse og tilskuddsrapporter.
- **Krav:** posisjons- og stillingsmodell, simulering av lønnsoppgjør og eksport av lønnsgrunnlag til budsjettverktøy.

---

## 7. Særtrekk for stiftelser, ideelle og frivillige organisasjoner

| Tema | Hva er spesielt | Systembehov |
|---|---|---|
| **Tariff** | Virke HUK (landsoverenskomster for f.eks. helse og sosiale tjenester, virksomheter, utdanning) har sentrale tillegg per stige og lokale forhandlinger med frist. Virkningsdato 1. mai 2026 ([NTL](https://www.ntl.no/Content/236135/cache=1781783091000/attr=54859A4B558E247CE0630B00000A6027/HUK-oppgj%C3%B8r%202026%20-%20Protokoll%20-%20Landsoverenskomst%20for%20virksomheter.pdf)). NHO Geneo har egne overenskomster for helse og omsorg. Mange ideelle følger offentlige lønnsstiger og ansiennitet. | Lønnsstiger med ansiennitet, automatisk opprykk, masseoppdatering, retro |
| **Pensjon** | HUK-virksomheter har ofte offentlig tjenestepensjon (KLP eller lignende), ikke OTP-innskudd | Pensjonsgrunnlag, fil eller integrasjon, kvartalsrapportering |
| **Prosjekt- og tilskuddsfinansiering** | Lønn fordelt på mange finansiører, ofte med retroaktive endringer | Se 6.3–6.4 |
| **Honorarer** | Foredragsholdere, artister, oppdragstakere uten ENK, styremedlemmer. Rapporteres i a-meldingen (honorar uten arbeidsforhold), med trekk og AGA. | Rask registrering av «ikke-ansatte» med minimalt med data, egne honorarkjøringer |
| **Styrehonorar** | Er lønn: trekkpliktig og AGA-pliktig, men inngår ikke i grunnlaget for feriepenger og pensjon. Rapporteres som styrehonorar eller godtgjørelse for verv. Ofte konfidensielt. | Egen lønnsart, konfidensiell gruppe, årlig utbetaling |
| **Frivillige** | Ulønnede frivillige får bare dekket utlegg mot bilag. Det er ikke lønn. | Utleggsmodul for ikke-ansatte uten lønnsforhold |
| **Skattefri organisasjon** (skatteloven § 2-32) | Opplysningsplikt når lønn og andre ytelser overstiger **10 000 kr i året** per mottaker. Man kan bruke regelen «Skattefri organisasjon» fra første krone, eller vente til grensen passeres og da rapportere alt. Ikke forskuddstrekk under 10 000 kr. **AGA skal beregnes av all lønn**, også under grensen for opplysningsplikt ([Skatteetaten](https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/spesielle-grupper/skattefrie-organisasjoner)). | Akkumulator per mottaker per år, automatisk overgang, merking i a-meldingen |
| **AGA-fritak, veldedig eller allmennyttig** | Ingen AGA når de totale lønnsutgiftene er **opp til 800 000 kr** og bare for utbetalinger **opp til 80 000 kr per ansatt**, og lønnen ikke er knyttet til næringsvirksomhet ([Lovdata ftrl. § 23-2](https://lovdata.no/lov/1997-02-28-19/§23-2)). Det finnes en forenklet a-melding for slike organisasjoner ([Skatteetaten](https://www.skatteetaten.no/skjema/a-melding-veldedig-allmennyttig/)). | Gjelder i praksis små foreninger, ikke 50+ ansatte, men er relevant for byråkunder. Grenseovervåking. |
| **Innkjøp og outsourcing** | Mange stiftelser outsourcer regnskap og lønn. GRID-Arendal anskaffet regnskap, lønn og ERP samlet, med fastpris per måned ([TED](https://ted.europa.eu/en/notice/-/detail/763121-2023)). | Byråmodus: byrå kjører, kunden godkjenner |
| **Styring og åpenhet** | Styre- og givertillit. Innsamlingskontrollen og åpenhetsloven gjør at lønn behandles som risikoområde. Kirkens Bymisjon har som mål at alle ansatte får lønn fastsatt etter lovverk, tariff og lønnspolitikk ([Kirkens Bymisjon](https://kirkensbymisjon.no/content/uploads/2026/06/Redegjorelse-Apenhetsloven-2025.pdf)). | Revisjonsspor, rapporter for lønnspolitikk |

---

## 8. Smertepunkter med dagens systemer

### 8.1 Regnskap Norge: «Lønnssystemer 2025» (n=298, publisert mars 2026)

**Mest brukte systemer** blant spesialistene (en person kan bruke flere): Visma.net Payroll (106), SD Worx (103), Tripletex (76), PowerOffice GO (72), Xledger (46), Finago/24SevenOffice (31), Duett (20), Nettlønn (20), Unit4 (18), Unimicro (14), Visma Enterprise HRM (14), SAP (13).

**Samlet fornøydhet (skala 1–6):** SD Worx 5,4 · PowerOffice GO 5,1 · Tripletex 4,9 · Duett 4,8 · Visma.net Payroll 4,6 · Finago 4,6 · Xledger 4,5 · Unimicro 4,4 · Unit4 4,2 · SAP 3,9 · **Visma Enterprise HRM 3,4** · **Nettlønn 2,9**.
**Fornøydhet med funksjoner for sluttbruker** (samhandling, godkjenning, rapportering): PowerOffice 5,2 · SD Worx 5,1 · … · SAP 3,6 · Visma Enterprise HRM 3,3 · Nettlønn 2,8.
([Regnskap Norge](https://www.regnskapnorge.no/contentassets/b173a1e31cd741af9b610fc80db70ddf/lonnssystemer---resultater-til-publisering.pdf))

**Kommentarene i undersøkelsen** (oppsummert av Regnskap Norge med Copilot, her parafrasert):

| System | Styrker | Smertepunkter |
|---|---|---|
| **SD Worx** | Fleksibel og sterk lønnsmotor, konfigurerbar uten spesialtilpasning, godt rapportunivers, gode importmaler, god fraværsmodul. Passer for store virksomheter med mange tariffer. | Ustabilitet etter overgangen til sky, komplekst og tungt å implementere, lite intuitivt for sluttbrukere, svak support og dokumentasjon, Citrix-frustrasjon ved import og oppdateringer for flere selskaper, for åpent og dermed sårbart for brukerfeil, mangler på historikkretting og kontrollrapporter |
| **Visma.net Payroll** | Ryddig, god automatisering ved korrigering og a-melding, god sykefraværsmodul, god support | Rigid datostyring, retro er komplisert og feilsensitivt og skaper store avstemmingsproblemer når skattetrekk og AGA endres tilbake i tid, doble arbeidsprosesser, begrensede rapporter, svak HRM, lite informasjon på lønnsslippen, svak integrasjon mot regnskap, tungvint oppsett av nye ansatte |
| **PowerOffice GO** | Intuitivt, godt integrert med regnskap, godt for samarbeid mellom byrå og klient via app (reise, utlegg, timer) | Tungvint ved avanserte behov: mange klikk, faste lønnslinjer, fraværsmodul, timebank, mange ansatte. Feil i forskuddstrekk ved kombinerte kjøringer og i feriepenger er rapportert. |
| **Tripletex** | Enkelt og godt for små virksomheter | Lite automasjon, mye manuell registrering, mangler full fraværsmodul, begrenset import, oppleves dyrt i forhold til funksjonalitet |
| **Finago** | Moderne og byråfokusert | Tregt, grunnleggende feil ved oppstart 2025 (skattetrekk, feriepenger 60+), må innom både regnskap og bank for å fullføre lønnen |
| **Xledger** | Lønn tett integrert med økonomi, bank og konsern, sterk i store organisasjoner | Lønnsmodulen er tungvint, svært manuell og har mange klikk, særlig for variable ytelser. Vanskelig å korrigere, mangler automasjon mot Altinn, oppleves som «bak» dedikerte lønnssystemer. |

**AI:** 62 % bruker Copilot og 52 % ChatGPT. Brukerne ser stort potensial for **AI som kontrollfunksjon i lønn og reiseregninger**, men etterlyser trygge rammer for personvern og kvalitetssikring av tall.

### 8.2 Andre kilder

- **Implementering og bytte:** Universitetene i BOTT-samarbeidet (UiB, UiO, NTNU, UiT) gikk over til DFØs SAP-baserte lønn i 2021–2022. Det var krevende både teknisk og organisatorisk, med uløste problemer nesten to år etter oppstart ([UiB styresak](https://ekstern.filer.uib.no/ledelse/universitetsstyret/2022/2022-03-10/S_26-22BOTT_%C3%98konomi_og_l%C3%B8nn_Status.pdf), [UiO](https://jus.uio.no/om/organisasjon/styret/moter/2023/231012/v-sak-2.pdf)).
- **Grensesnittfeil mellom tid og lønn:** Kristiansand kommune, 2 338 ansatte med feil tillegg (se 4.4).
- **Excel og Word som HR-system:** NORCE (800+ ansatte) beskrev at dagens løsning for kompetanse og personalarkiv var basert på Word, PDF og Excel ([TED](https://ted.europa.eu/en/notice/-/detail/373762-2024)).
- **Godkjenning når ikke fram til cut-off:** Fra fagforeningshold (SAFE) beskrives godkjenningsprosessen for arbeidstimer som så omfattende at timene ikke blir godkjent i tide til lønnskjøringen ([SAFE](https://safe.no/wp-content/uploads/2023/10/SAFElement-11.10.2023.pdf)).
- **Oppgraderinger og versjoner:** Ferde krevde at siste versjon alltid er tilgjengelig uten ekstra kostnad og at nye funksjoner kan tas inn i kontraktsperioden ([TED](https://ted.europa.eu/en/notice/-/detail/169076-2025)). Det sier noe om erfaringer med tilleggsbetaling for nye moduler.
- **Prising per API-kall og datavolum:** Tensio ba om priser for lisens og variable kostnader knyttet til datavolum og API-kall ([TED](https://ted.europa.eu/en/notice/-/detail/291054-2024)). Kundene har altså erfart overraskende integrasjonskostnader.
- **Bytte fra Visma Enterprise HRM:** Randaberg kommune skrev at den bruker Visma Enterprise HRM og skal anskaffe et nytt skybasert system for HR og lønn. Visma Enterprise vant likevel i oktober 2024 ([TED](https://ted.europa.eu/en/notice/-/detail/367086-2024), [TED – tildeling](https://ted.europa.eu/en/notice/-/detail/752679-2024)). Det viser hvor høye byttekostnadene er.

### 8.3 Smertepunkter fra praksis, og hva et nytt system kan gjøre

| Smertepunkt | Hvorfor det skjer | Mulighet |
|---|---|---|
| Excel-import av variable data | Tidssystemet eksporterer CSV, og mapping skjer manuelt | API-først, mapping-UI med validering, import som kan kjøres flere ganger (idempotent), forhåndsvisning |
| Retro og etterbetaling | Datostyring uten god deltaberegning | Gjenberegning av hele perioden med differanse per måned og lønnsart, forklart linje for linje |
| Korrigering etter at perioden er låst | Må reversere og kjøre på nytt manuelt | Korrigeringskjøring med automatisk erstatningsmelding og reversbilag |
| Kontrollrapporter i Excel | Rapportene er laget for utskrift | Kontrollsenter med terskler, «forklar avvik» og signering |
| Avstemming lønn, regnskap og a-melding | Ulike perioder og kilder | Automatisk tre-veis avstemming med periodiseringsforklaring |
| Tunge oppgraderinger og konsulentavhengighet | On-prem, Citrix, tilpasninger | Ren SaaS, konfigurasjon i stedet for kode, testmiljø (sandbox) per kunde |
| Dyr support | Kompleksitet og få eksperter | Innebygd regelforklaring, AI-assistent med regelverkskilde, kunnskapsbase |
| A-melding-avvik | Valideres først når meldingen sendes | Forhåndsvalidering mot Skatteetatens kodeverk før kjøring |
| Prosjektfordeling | Lønn og prosjekt ligger i ulike systemer | Fordelingsprofiler med retro-omfordeling og finansiørrapporter |
| Byrå: mange klienter | Ett klientbilde om gangen | Porteføljeoversikt med status, frister og avvik på tvers |

---

## 9. Typiske krav i anbud (Doffin/TED)

### 9.1 Faktiske anbud: utdrag fra TED-kunngjøringer

Kunngjøringene er hentet via TED-API-et (norske oppdragsgivere, CPV 48450000/79211110/79631000 m.fl.). Selve kravspesifikasjonene ligger i Mercell, TendSign og EU-Supply bak innlogging. Det som er hentet ut under, er det kunngjøringen sier om omfang og vekting.

| # | Oppdragsgiver (størrelse) | Hva ble kjøpt | Tildelingskriterier og vekt | Vinner / merknad | Kilde |
|---|---|---|---|---|---|
| 1 | **Ferde AS** (ca. 50 lønnsmottakere) | Fullt integrert HR- og lønnssystem. HR: on- og offboarding, medarbeidersamtaler, sykefraværsoppfølging, kompetanse, håndbøker, personalregister. Lønn: rapportering, godtgjørelser, personforsikringer, trekk, reiseregninger, direkte mot **Xledger**, NAV-refusjon, Altinn, skattekort, fravær og timer. Lønnstjeneste fra leverandøren, med opsjon på å kjøre selv. | **Pris 35 / Kvalitet 65** | Siste versjon uten ekstra kostnad, rett til å ta inn ny funksjonalitet, leverandøren bistår med import fra gamle systemer | [TED 169076-2025](https://ted.europa.eu/en/notice/-/detail/169076-2025) |
| 2 | **Norske tog AS** (ca. 80 ansatte) | Felles HR- og lønnssystem (eller separate med integrasjon og én kontaktpunkt hos leverandøren), SaaS, automatisering og integrasjon. Leverandøren kjører lønnen. Ca. 8 MNOK, opsjon 1+1+1+1+1 år. | Fremgår ikke av kunngjøringen | Tildelt **Tower Newco (tidligere BDO Business Services)**. Norian Regnskap leverte også tilbud. | [TED 419499-2025](https://ted.europa.eu/en/notice/-/detail/419499-2025), [tildeling 177740-2026](https://ted.europa.eu/en/notice/-/detail/177740-2026) |
| 3 | **Randaberg og Kvitsøy kommune** (inkl. kirkesokn) | Skybasert HR og lønn som erstatter Visma Enterprise HRM og skal være grunnmur for organisasjonsstrukturen. Brukervennlighet, automatisering, informasjonssikkerhet. Ca. 10 MNOK. | **Funksjonalitet og brukervennlighet 30 / Pris 30 / Miljø 30 / Implementering 5 / SLA 5** | **Visma Enterprise AS** (13.10.2024) | [TED 367086-2024](https://ted.europa.eu/en/notice/-/detail/367086-2024), [752679-2024](https://ted.europa.eu/en/notice/-/detail/752679-2024) |
| 4 | **Stiftelsen GRID-Arendal** | Regnskap og lønn som tjeneste, ERP-valg og implementering, månedsavslutning og rapportering | **Pris 25** (underkriterier: integrasjon 10 %, system 20 %, fastpris regnskap og lønn 70 %) / **ERP-system 30** / **Erfaring og referanser 15** (minst tre referanser av sammenlignbar størrelse) / **Miljø 30** | Stiftelse som kjøper samlet tjeneste | [TED 763121-2023](https://ted.europa.eu/en/notice/-/detail/763121-2023) |
| 5 | **Entur AS** | Lønnstjenester og lønnsadministrasjon med lønns- og reiseregningssystem: lønnsberegning, kjøring, godkjenning og refusjon av reiser, rapportering og kontroll | **Kvalitet 60 / Pris 40** | | [TED 107323-2024](https://ted.europa.eu/en/notice/-/detail/107323-2024) |
| 6 | **Tensio AS** (konsern med datterselskaper) | Rammeavtale for lønnstjenester: produksjon, drift og forvaltning av systemer, reise og utlegg, saldotjeneste, enkel tilgang til lønnsdata for sluttbrukere, filintegrasjon mot **Unit4 ERP**, utvikling av integrasjoner | **Kvalitet, kompetanse og funksjonalitet 70** (funksjonell og ikke-funksjonell spesifikasjon, brukervennlighet ved presentasjon, CV-er, prosjektmodell) / **Pris 30** (etablering, løpende tjeneste, lisens, variable kostnader for datavolum og API-kall) | | [TED 291054-2024](https://ted.europa.eu/en/notice/-/detail/291054-2024) |
| 7 | **Gassnova SF** | ERP med regnskaps- og lønnstjenester: regnskap, lønn og reise, timefangst, e-faktura, rapportering, 4+2+2 år | To trinn: kvalifisering av inntil fem, deretter forhandling med de tre beste | | [TED 46448-2024](https://ted.europa.eu/en/notice/-/detail/46448-2024) |
| 8 | **Narvik kommune m.fl.** (KF, IKS, kirkelig fellesråd, sokn, friluftsråd) | ERP for økonomi, lønn, HR og innkjøp, tett integrert for å unngå dobbeltregistrering | **Pris 10 / Løsning, funksjonalitet og brukervennlighet 40 / Implementering 10 / Kompetanse 10 / Miljø 30** | Tildelt des. 2024 | [TED 396670-2024](https://ted.europa.eu/en/notice/-/detail/396670-2024) |
| 9 | **NORCE** (800+ ansatte, 8 kontorsteder) | HRM-skytjeneste (kompetanse, CV, personalarkiv). Lønn, tid, fravær og reise forblir i Unit4 ERP. | **Kvalitet 75** (funksjonalitet 65–75 %, teknisk (integrasjon, GDPR og sikkerhet) 15–20 %, implementering og support 20–25 %) / **Pris 25** | **CatalystOne** | [TED 373762-2024](https://ted.europa.eu/en/notice/-/detail/373762-2024) |
| 10 | **Bergen kommune** | Nytt skybasert **lønnssystem**: kjøring, utbetaling, rapportering, NAV-refusjon, reise og kjøregodtgjørelse, utlegg, med konvertering og integrasjoner, etter SSA-Sky. HR-systemet anskaffes separat. | Kvalifiseringsfase | Separat anskaffelse av lønn og HR | [TED 745040-2025](https://ted.europa.eu/en/notice/-/detail/745040-2025), [HR 745370-2025](https://ted.europa.eu/en/notice/-/detail/745370-2025) |

Andre relevante kunngjøringer: Nofima HRM (Pris 25 / Kvalitet 75, CatalystOne, SSA-L) ([TED](https://ted.europa.eu/en/notice/-/detail/102696-2024)), Høgskolen i Østfold HRM (Kvalitet 70 / Pris 30) ([TED](https://ted.europa.eu/en/notice/-/detail/322096-2025)), BIR AS HRM for konsernet (ca. 10 MNOK, 2026) ([TED](https://ted.europa.eu/en/notice/-/detail/440999-2026)), Nye Veier HR-system med selvbetjening for ansatte og ledere (2026) ([TED](https://ted.europa.eu/en/notice/-/detail/449466-2026)), NAV lønns- og personalsystem (2025) ([TED](https://ted.europa.eu/en/notice/-/detail/245618-2025)), KS co-sourcing av lønnstjenester (2025) ([TED](https://ted.europa.eu/en/notice/-/detail/690251-2025)) og UiS markedsdialog om HRM/HCM, enten som suite eller «composable HR» (2026) ([TED](https://ted.europa.eu/en/notice/-/detail/612548-2026)). Statens eldre «Funksjonell kravspesifikasjon for statlige lønns- og personaldatasystem» viser hvordan staten har strukturert krav ([Regjeringen](https://www.regjeringen.no/no/dokumenter/funksjonell-kravspesifikasjon-for-statli/id507085/)).

### 9.2 Mønstre og lærdommer

1. **Kvalitet veier tyngst:** typisk 60–75 % kvalitet og 25–40 % pris i rene system- og tjenesteanbud.
2. **Miljø 30 % i mange offentlige anbud** (Randaberg, Narvik, GRID-Arendal). Dette følger av regelen i anskaffelsesforskriften om at klima- og miljøhensyn skal vektes minst 30 % (gjelder fra 2024, med unntak). Ha en ferdig miljødokumentasjon: datasenter, energi, reiser ved implementering, papirløs lønnsslipp.
3. **Lønn som tjeneste.** Mindre offentlige foretak kjøper system pluss lønnskjøring. Vinnerne er ofte outsourcing- eller byråaktører (BDO/Tower Newco, Norian). For en leverandør er byråpartnere derfor en vei inn i anbudene.
4. **Standardavtaler:** SSA-L (løpende tjenestekjøp), SSA-Sky (skytjenester, også en liten variant) og SSA-T. Leverandørens standardvilkår legges ofte som bilag.
5. **Bilagsstruktur:** Bilag 1 er kravspesifikasjon med skal- og bør-krav, bilag 2 prisskjema, bilag 3 miljø, bilag 4 etableringsplan og bilag 5 SLA (jf. Randaberg).
6. **Integrasjon mot eksisterende ERP** nevnes eksplisitt (Xledger, Unit4).
7. **Kommersielle signaler:** siste versjon inkludert, rett til ny funksjonalitet, priser for API-kall og datavolum, eksport ved avslutning, og lagring i EU/EØS (et krav DFØ også har fremhevet).

### 9.3 Kravkategorier: sjekkliste for kravspesifikasjon

| Kategori | Typiske krav (skal/bør) |
|---|---|
| **Lønnsberegning** | Fast og variabel lønn, timelønn, tariffstiger og ansiennitet, tillegg, overtid, ubekvem arbeidstid, retro og etterbetaling, flere arbeidsforhold, feriepenger (10,2/12/60+), ferietrekk, halv skatt, sluttoppgjør, ekstrakjøringer, simulering |
| **Fravær og NAV** | Fraværstyper, arbeidsgiverperiode, refusjonskrav, inntektsmelding via API, oppfølging av refusjoner, feriepenger av refusjon |
| **Trekk** | Forskuddstrekk (tabell, prosent, kildeskatt), utleggstrekk etter nye og gamle regler, fagforening, lån, påleggstrekk og trekkfri grense |
| **Reise og utlegg** | Statens satser og særavtaler, diett, km, trekkpliktig og trekkfritt, kvitteringsfoto, godkjenning, utbetaling i egen kjøring |
| **Rapportering til myndigheter** | A-melding (inkl. pensjonsinnretning), skattekort, A07, trekkpålegg, likestilling og lønnskartlegging |
| **Pensjon og forsikring** | Innskudd via a-melding, offentlig tjenestepensjon via fil eller API, forsikringer |
| **Regnskap** | Bilag med dimensjoner, fordelingsprofiler, periodisering, avsetninger (feriepenger, AGA) |
| **Bank** | pain.001/pain.002/camt.054, betaling av trekk med KID, godkjenningsflyt |
| **Kontroll og internkontroll** | Kontrollrapporter, terskler, fire-øyne, endringslogg, tilgangsstyring og SoD, attestasjon, revisorinnsyn |
| **Selvbetjening** | Lønnsslipp, skattekort, fravær, timer, reise og utlegg, bankkonto (BankID), feriepenger, mobil og godkjenning for ledere |
| **HR (hvis kombinert)** | Personalregister, organisasjon, on- og offboarding, medarbeidersamtaler, kompetanse, håndbok, sykefraværsoppfølging |
| **Integrasjon** | Åpent og dokumentert API, standardintegrasjoner (ERP, tid, HR, bank, Digipost, pensjon), webhooks |
| **Ikke-funksjonelle krav** | SaaS, tilgjengelighet og SLA, ytelse, universell utforming (WCAG), SSO (Entra ID), MFA, logging, sikkerhetskopi, ISO 27001, ISAE 3402, GDPR og databehandleravtale, lagring i EU/EØS, exit og dataeksport |
| **Etablering** | Prosjektmetodikk, konvertering av historikk, parallellkjøring, opplæring, testmiljø |
| **Forvaltning** | Oppgraderinger inkludert, release notes, brukerforum, support (responstider, norsk språk) |
| **Miljø** | Miljøtiltak og -dokumentasjon (30 %) |
| **Pris** | Etablering, lisens per ansatt per måned, eventuelt per lønnsslipp, konsulentpriser, opsjoner, eventuelt API-kall og datavolum |

---

## 10. Ansattportal og selvbetjening: forventninger i 2026

Referansen mange ansatte har, er **DFØ-appen og selvbetjeningsportalen** i staten. Der registrerer ansatte arbeidstid, timer, ferie, fravær og permisjon, reiseregninger, utgiftsrefusjon og ekstra skattetrekk, og ser lønnsslippen ([UiB – selvbetjeningsportalen](https://www.uib.no/foransatte/175680/selvbetjeningsportalen-og-df%C3%B8-appen)). UiB minner om at tilgangen forsvinner når man slutter, så ansatte må laste ned lønnsslipper før det. **Her finnes en mulighet:** innsyn med BankID for tidligere ansatte, eller automatisk arkiv i Digipost.

### 10.1 Ansatte forventer

| Funksjon | Minimum 2026 | Forventet eller differensierende |
|---|---|---|
| Lønnsslipp | Mobil, PDF, arkiv | Forklart lønnsslipp («hvorfor er lønnen lavere enn sist?»), sammenligning, varsel |
| Skattekort | Vise trekkprosent eller tabell | Lenke til Skatteetaten for endring, varsel når skattekortet endres |
| Feriepenger og ferie | Saldo for feriedager og opptjente feriepenger | Prognose for juni-utbetaling, 60+-uke |
| Fravær | Egenmelding, sykt barn, ferie- og permisjonssøknad | Saldo (egenmeldingsdager, avspasering, fleks), status i sanntid |
| Timer og vakter | Registrere og se godkjenningsstatus | Integrert med vaktplan, ta vakter, se tillegg før lønn |
| Reise og utlegg | Foto av kvittering, km med kart, diett | Kortintegrasjon (Pleo, Folio), automatisk satsberegning |
| Personopplysninger | Adresse, pårørende | **Bankkonto med BankID** og verifisering |
| Dokumenter | Arbeidsavtale, endringsbrev | E-signering |
| Etter at man har sluttet | — | Innsyn i lønnsslipp og årsoversikt med BankID |
| Språk | Norsk og engelsk | Flere språk (helse, omsorg, renhold) |

### 10.2 Ledere forventer

- **Godkjenninger på mobil** (timer, fravær, reise, utlegg) i én samlet innboks, med påminnelse før cut-off og stedfortreder ved fravær.
- **Lønnskost og FTE for egen enhet** mot budsjett, og sykefravær per enhet.
- **Endringsønsker** (stillingsprosent, tillegg) sendt som skjema til HR, ikke e-post.
- **Varsel** om ansatte med høyt overtidsforbruk eller brudd på AML-grenser.

### 10.3 Lønnsavdelingen forventer

- Selvbetjening skal **redusere henvendelser**. De vanligste spørsmålene gjelder skattetrekk, feriepenger, etterbetaling og variable tillegg.
- Én sannhet: endringer ansatte gjør selv (f.eks. bankkonto) skal logges og inngå i kontrollrapporten.

---

## 11. Fortelling: en typisk lønnsmåned i en virksomhet med 400 ansatte

### 11.1 Virksomheten (fiktiv, men sammensatt av typiske trekk)

**Stiftelsen Nordlys** driver omsorgs- og rusinstitusjoner, et kompetansesenter og en forskningsavdeling.

- **400 ansatte** fordelt på **tre juridiske enheter**: stiftelsen (280), Nordlys Omsorg AS (100) og Nordlys Kompetanse AS (20). Det er sju underenheter, hvorav én i en kommune med lavere AGA-sats.
- **Lønnstyper:** 230 med fast månedslønn uten variable tillegg, 110 i turnus med kvelds-, natt-, helge- og helligdagstillegg og overtid, og 60 timelønnede ekstravakter. I tillegg ca. 15 honorarmottakere per måned og 7 styremedlemmer.
- **Tariff:** Virke HUK for stiftelsen og omsorgsselskapet. Kompetanse AS har ingen tariffavtale.
- **Pensjon:** offentlig tjenestepensjon via KLP for HUK-enhetene, innskuddspensjon (OTP) for AS-et.
- **Finansiering:** kommunale driftsavtaler, Helsedirektoratet-tilskudd, to Forskningsråds-prosjekter og ett EU-prosjekt. 45 ansatte har prosentfordeling på prosjekter.
- **Systemer:** HR-system (masterdata, organisasjon), vaktplan/tid (turnus og timelister), reise- og utleggsmodul, ERP (Xledger), bank (DNB, filintegrasjon), Digipost og app for lønnsslipp.
- **Lønnsteam:** Kari (lønnsansvarlig, 100 %), Ola og Fatima (lønnsmedarbeidere, 100 % og 60 %). Ingrid (HR-rådgiver, ca. 50 % på masterdata og oppgjør), Per (controller, ca. 30 % på lønn og prosjekt) og Lise (økonomisjef, attestasjon og bankgodkjenning). Det gir ca. 3 FTE for 400 ansatte, eller **ca. 130 per FTE**, godt under APQC-medianen på ca. 350. Turnus, prosjektfordeling og NAV-refusjoner trekker ned.
- **Utbetalingsdag: den 20.** Variable tillegg betales én måned etterskuddsvis.
- **Novembers ekstra utfordringer:** **lokale HUK-forhandlinger** ble avsluttet innen 31.10 med virkning fra 1.5.2026, så det kommer etterbetaling for mai–oktober. AGA-terminen for september–oktober forfaller i november, og desember-kjøringen må forberedes.

### 11.2 Tidslinje dag for dag: november 2026

| Dato | Hvem | Hva skjer | Hva kan gå galt / systemets rolle |
|---|---|---|---|
| **Fre 23.10** | Kari | Lønnskalender og påminnelse for november sendes til alle ledere: «Frist ledergodkjenning mandag 9.11 kl. 12». | Systemet bør sende påminnelser automatisk og vise status per leder. |
| **Fre 30.10** | Ingrid, tillitsvalgte | **Lokale forhandlinger avsluttet** (fristen var 31.10). Protokollen gir tillegg til 258 ansatte, virkning 1.5.2026. Ingrid lager en importfil med ansattnr., nytt lønnstrinn eller beløp og virkningsdato. | Excel-protokoll blir importfil. Risiko for feil virkningsdato eller feil ansattnr. |
| **Lør 31.10** | — | Vaktperioden for oktober avsluttes i tidssystemet. | |
| **Man 2.11** | Ola, Ingrid | **Masterdata:** 6 nyansatte fra 1.11 kommer inn fra HR-systemet. Ola kontrollerer stillingsprosent, lønnstrinn, kostnadssted og prosjektfordeling, at skattekort er hentet automatisk, at bankkonto er registrert av den ansatte med BankID og at KLP-innmelding er gjort. 4 sluttere (31.10) settes opp med sluttoppgjør og feriepenger. | Ansatte uten skattekort får 50 % trekk. Systemet varsler. Manglende prosjektfordeling stoppes av kontrollregel. |
| **Tir 3.11** | Ledere (40 stk.) | Ledere kontrollerer og godkjenner oktobervakter og timelister for ekstravakter. Ansatte har levert reiser og utlegg. | Status per leder viser 12 av 40 ferdig. |
| **Ons 4.11 kl. 12** | Ingrid | **HR-cut-off for masterdata** (permisjoner, stillingsendringer, sluttere). Én foreldrepermisjon og to endringer i stillingsprosent kommer inn. | Endringer etter fristen må vente eller merkes som unntak med begrunnelse. |
| **Tor 5.11** | Kari | Automatisk purring til 15 ledere som ikke har godkjent. Kari ringer de tre største enhetene. | Den klassiske flaskehalsen er ledergodkjenning ([SAFE](https://safe.no/wp-content/uploads/2023/10/SAFElement-11.10.2023.pdf)). |
| **Fre 6.11** | Fatima | Reiseregninger og utlegg fra oktober kontrolleres (diett, km, trekkpliktig og trekkfritt). 3 avvises med beskjed til den ansatte. Honorarskjemaer for 15 eksterne kontrolleres (fødselsnr., konto, skattekort). | |
| **Man 9.11 kl. 12** | Ledere | **Cut-off for ledergodkjenning.** 2 ledere har ikke godkjent. Deres vakter går til desember, etter beslutning fra Kari og etter varsel til de ansatte. | Systemet sperrer ugodkjente linjer automatisk og gir rapport. |
| **Man 9.11 ettermiddag** | Ola | **Import av variable data** fra tidssystemet (ca. 4 800 linjer). Feillisten viser 3 ansatte uten match (nyansatte med feil ansattnr. i vaktplanen), 1 ukjent lønnsart (en ny vaktkode for «forsterket natt» som noen har opprettet i vaktplanen) og 22 linjer uten prosjekt. | **Kristiansand-lærdommen:** en ny lønnsart må mappes og testes, ellers får mange feil tillegg ([Kristiansand](https://www.kristiansand.kommune.no/contentassets/d6fb88872a7b4f88b84e57f20e50318e/rapport.lonnshendelse.pdf)). |
| **Tir 10.11** | Ola, Ingrid | **Etterbetaling:** masseimport av 258 lønnsendringer med virkningsdato 1.5. Systemet etterberegner mai–oktober: fastlønn og tillegg som beregnes av timelønn (ubekvem arbeidstid, overtid). 7 som sluttet før vedtaksdato utelates etter tariffen. Sum etterbetaling ca. 1,9 MNOK brutto. «Siste lønnsendringsdato» settes til 1.5.2026 ([Skatteetaten](https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/arbeidsforholdet/opplysninger-om-arbeidsforholdet/siste-lonnsendringsdato)). | Hvis retro ikke dekker tillegg, må de beregnes i Excel. **Det er det største tidstyvet i dag.** |
| **Tir 10.11 ettermiddag** | Ola | **Testkjøring 1** for alle tre selskaper. Kontrollpakken kjøres: 31 ansatte har avvik over ±20 % mot oktober (28 forklares av etterbetaling, 2 av permisjon og 1 av feil: dobbelt registrert nattillegg). 1 ny bankkonto er endret av en ansatt via BankID. 2 får 50 % trekk (skattekort mangler). 1 har negativ netto (lønnsforskudd trekkes). Det er 1 utleggstrekk etter nye regler (trekkpålegg hentet fra Skatteetatens API) og 3 etter gamle. | Utleggstrekk etter nye og gamle regler skal rapporteres og betales hver for seg ([Skatteetaten](https://www.skatteetaten.no/om-skatteetaten/fremtidens-innkreving/systemleverandorer/lonns--og-personalsystem/)). |
| **Ons 11.11** | Ola, Per | Korrigeringer: Ola sletter det doble nattillegget og mapper den nye vaktkoden. **Testkjøring 2.** Per sender kostnadsrapport per prosjekt og finansiør til 6 prosjektledere: «Stemmer fordelingen for oktober?». Ett EU-prosjekt fikk 20 % for mye. Fordelingen rettes fra 1.10. | Systemet bør vise kostnad per prosjekt *før* låsing, inkludert AGA, feriepenger og pensjon. |
| **Tor 12.11** | Fatima | **Fire-øyne:** Fatima kontrollerer Olas masterdata-endringer i endringsloggen (6 nyansatte, 4 sluttere, 3 endringer, 1 bankkonto). Hun går over etterbetalingen med stikkprøver på 10 ansatte. Hun signerer i systemet. | Krever endringslogg per felt og funksjonen «kontrollert av». |
| **Tor 12.11 ettermiddag** | Kari | Kari gjennomgår kontrollrapportene, ser at alle avvik er forklart og signerer **faglig godkjenning**. Hun fyller ut kontrollskjemaet med brutto ca. 23,4 MNOK (inkl. etterbetaling), netto, forskuddstrekk, AGA per selskap og sone, pensjonsgrunnlag, antall lønnsmottakere (412 inkl. honorarer) og antall ansatte. | |
| **Fre 13.11** | Lise | **Attestasjon:** Lise sammenligner totalsummene med forrige måned og budsjett. Etterbetalingen var avsatt i regnskapet, så hun godkjenner i systemet. **Endelig kjøring** gjøres, og perioden låses. | Uten godkjenning i systemet skal bankfil ikke kunne lages. |
| **Man 16.11** | Lise, Per | **AGA for termin 5 (september–oktober)** forfaller 15.11, som er søndag, og betales derfor mandag. Bankfil (pain.001) for nettolønn til 412 mottakere lages med betalingsdato 20.11 og overføres via integrasjon. Samme dag lages betalinger for **forskuddstrekk** (ny KID for november) og **utleggstrekk** (KID per ansatt for nye trekk) med forfall **mandag 23.11**, første virkedag etter utbetaling ([Skatteetaten](https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/arbeidsgiveravgift/betaling-av-forskuddstrekk-og-arbeidsgiveravgift/)). Fagforeningstrekk og andre trekk betales til kreditorene. **To godkjennere** med lønnsrettighet (Lise og Per) signerer i nettbanken. pain.002 bekrefter at banken har mottatt filen. | Før 2026 ble trekket satt inn på skattetrekkskonto, og AGA og trekk ble betalt annenhver måned. Nå er trekket en del av lønnsbetalingen hver måned, med sanksjoner ved for sen betaling ([KPMG](https://kpmg.com/no/nb/innsikt/skatt-regulatorisk/krav-skattetrekkskonto-opphorer.html)). |
| **Tir 17.11** | Ola | **A-melding** for november sendes per selskap via API (Altinn 3/Maskinporten). Tilbakemeldingen viser ingen feil. Ett avvik: en ansatt har arbeidsforhold på feil underenhet. Det rettes i masterdata, og erstatningsmelding sendes samme dag. Pensjonsinnretning er oppgitt. | Feil underenhet gir feil AGA-sone. Systemet bør fange det i forhåndsvalideringen. |
| **Tir 17.11** | Per | **Regnskapsbilag** overføres til Xledger: 3 selskaper, 14 avdelinger, 38 prosjekter. Lønnskostnad, skyldig trekk, AGA, feriepengeavsetning og pensjon. Etterbetalingen bokføres mot avsetningen. | Dimensjoner må finnes i ERP (validering før overføring). |
| **Ons 18.11** | System | **Lønnsslipper** publiseres i appen og Digipost med varsel. Slippen forklarer etterbetalingen per måned. Ledere får rapport over lønnskost og FTE for egen enhet. | Mange henvendelser kommer dersom etterbetalingen ikke er forklart. |
| **Fre 20.11** | Alle | **Utbetaling.** Lønnsavdelingen har ekstra bemanning i chat og e-post. 9 henvendelser: 5 om etterbetaling (forklart), 2 om skattetrekk på etterbetalingen og 2 om reelle feil i vakttillegg (en leder godkjente feil vakttype). | |
| **Man 23.11** | Lise | **Forskuddstrekk og utleggstrekk trekkes fra konto** (forfall). Lise kontrollerer at beløpene stemmer med a-meldingen. | Trekk som ikke er betalt, får strafferettslige konsekvenser. Systemet bør vise betalingsstatus. |
| **Tir 24.11** | Per | **Avstemming:** lønnsjournal mot hovedbok (lønnskostnad, skyldig forskuddstrekk og utleggstrekk, AGA, feriepenger, pensjon), a-meldingens tilbakemelding mot bokført og bank (camt.054) mot nettolønn. Differanser dokumenteres (reiseregninger godkjent i oktober, betalt i november) ([Sticos](https://www.sticos.no/fagstoff/skal-a-meldingen-alltid-stemme-med-regnskapet)). | En automatisk tre-veis avstemming ville spart ca. 4–6 timer. |
| **Ons 25.11** | Fatima | **NAV:** Fatima følger opp refusjonskrav for sykepenger og foreldrepenger (ca. 25 saker). Inntektsmeldinger er sendt løpende via API når NAV har sendt forespørsel ([NAV](https://www.nav.no/arbeidsgiver/moderniserte-tjenester)). Hun sammenligner NAVs utbetalinger med fordringen og purrer 3 saker. | Refusjoner er ofte et «svart hull» i dagens systemer. |
| **Tor 26.11** | Ola | **Ekstrakjøring** for 2 ansatte med feil vakttillegg (beløp 3 400 kr) i stedet for å vente til desember. Det gir egen bankfil, en ny a-melding for november som oppsummeres i tilbakemeldingen, og betaling av forskuddstrekket første virkedag etter. | En ekstrakjøring må være like kontrollert som hovedkjøringen, men raskere. |
| **Fre 27.11** | Per, Ingrid | **Rapportering:** timer og lønnskost per prosjekt til prosjektøkonomi (Forskningsrådet: timeregistrering er et krav ([Forskningsrådet](https://www.forskningsradet.no/finansiering/hvordan-skrive-soknad/budsjett/kostnader-naringsliv-offentlig-sektor/)); EU: timelister signeres). HR-statistikk (sykefravær, FTE, turnover) går til ledermøtet. KLP-rapporten for kvartalet forberedes. | |
| **Man 30.11** | Per | **Månedsavslutning:** periodisering av novembers variable tillegg, som utbetales i desember, avsetning for feriepenger og AGA, og ferdig prosjektregnskap. | |
| **Tir 1.12 → fre 4.12** | Kari | **Desember starter allerede.** Utbetaling er fredag 18.12, så ledernes cut-off er torsdag 10.12. Desember har **halv skatt**. Skattekort for 2027 hentes. Styrehonorar for 2026 utbetales. Julegaver avklares skattemessig. Revisor har varslet interimbesøk i januar. | Desember har den mest komprimerte kalenderen i året. |

### 11.3 Tidsbruk i november (anslag)

| Rolle | Timer i november | Hvorav på grunn av etterbetaling |
|---|---|---|
| Kari (lønnsansvarlig) | ~45 | ~10 |
| Ola (lønnsmedarbeider) | ~90 | ~25 |
| Fatima (lønnsmedarbeider, 60 %) | ~55 | ~8 |
| Ingrid (HR, masterdata og oppgjør) | ~25 | ~12 |
| Per (controller) | ~22 | ~3 |
| Lise (økonomisjef) | ~4 | — |
| 40 ledere (godkjenning) | ~40 i sum | — |
| **Totalt** | **~280 timer** | **~58** |

En vanlig måned uten oppgjør bruker ca. 200–220 timer. Med bedre retro, automatisk avstemming, færre importfeil og selvbetjening er det realistisk å spare 25–40 % (anslag).

### 11.4 Hva fortellingen viser for produktet

1. Lønnssystemet må **eie kalenderen og fristene**: statusbilde per leder, purringer og sperrer.
2. **Importen er det kritiske punktet**: mapping, validering, feillister og nye lønnsarter som stoppes til de er godkjent.
3. **Retro må være førsteklasses**, også for tillegg som avhenger av timelønn.
4. **Kontroll og attestasjon skal skje i systemet**, med sporbarhet: kontrollpakke, fire-øyne og CFO-godkjenning som låser opp bankfilen.
5. **Utbetaling innebærer nå både nettolønn og trekk** (forskuddstrekk og utleggstrekk med KID og forfall første virkedag etter).
6. **Etterarbeidet** (avstemming, NAV-refusjon, prosjektrapport) er der byråer og lønnsavdelinger kan spare mest tid.

---

## 12. Implikasjoner for produktet (prioritert)

**Grunnmur (må være på plass før første kunde med mer enn 50 ansatte):**
1. Lønnskalender med flere kjøringer per måned, cut-off-sperre, statusbilde og purring.
2. API-først import av tid, fravær, reise og HR-data med mapping-UI, validering og idempotens.
3. Retroberegning med differanse per periode og lønnsart (inkl. tillegg avhengig av timelønn), masseoppdatering fra oppgjørsprotokoll.
4. Kontrollsenter: konfigurerbare kontroller, terskler, forklaringer, signering og fire-øyne.
5. Godkjenningsflyt (lønnsansvarlig → CFO) som låser opp bankfilen. Endringslogg per felt.
6. Bankintegrasjon (pain.001/002, camt.054) og automatiske betalinger av forskuddstrekk og utleggstrekk med KID og riktig forfall (2026-regler).
7. Altinn 3/Maskinporten: a-melding med tilbakemelding, skattekort, trekkpålegg, A07, NAV inntektsmelding-API og oppfølging av refusjoner.
8. Regnskapsbilag med fleksible dimensjoner og fordelingsprofiler (prosent, timer, retro-omfordeling).
9. Tilgangsstyring med konfidensielle grupper, SoD-rapport og revisorinnsyn.
10. Selvbetjening på mobil: lønnsslipp (forklart), fravær, timer, reise og utlegg, bankkonto med BankID, feriepengeoversikt. Leder-innboks.

**Differensiering for stiftelser, forskning og byrå:**
11. Prosjekt- og finansiørrapport (timer, kost per time, sosiale kostnader, Forskningsrådet og EU-format).
12. Tariffmotor for Virke HUK og NHO Geneo (stiger, ansiennitet, lokale tillegg) og offentlig tjenestepensjon (KLP-fil).
13. Honorarer, styrehonorar og skattefri organisasjon (10 000 kr-akkumulator), overvåking av AGA-fritaket for små klienter.
14. Byråmodus: porteføljeoversikt, kunden godkjenner og byrået kjører, felles maler og lønnsarter på tvers av klienter.
15. Tillit: ISAE 3402 type II (plan for år 2), ISO 27001, lagring i EU/EØS, dataeksport ved exit og miljødokumentasjon for anbud.

---

## 13. Kildeliste (utvalg)

**Myndigheter og lovverk**
- Skatteetaten – betaling av forskuddstrekk og AGA (2026): https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/arbeidsgiveravgift/betaling-av-forskuddstrekk-og-arbeidsgiveravgift/
- Skatteetaten – KID: https://www.skatteetaten.no/kid/
- Skatteetaten – fremtidens innkreving for lønns- og personalsystemer: https://www.skatteetaten.no/om-skatteetaten/fremtidens-innkreving/systemleverandorer/lonns--og-personalsystem/
- Skatteetaten – bytte lønnssystem: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/arbeidsforholdet/spesielle-forhold/bytte-lonnssystem
- Skatteetaten – siste lønnsendringsdato: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/arbeidsforholdet/opplysninger-om-arbeidsforholdet/siste-lonnsendringsdato
- Skatteetaten – skattefrie organisasjoner: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/spesielle-grupper/skattefrie-organisasjoner
- Skatteetaten – forenklet a-melding for veldedige organisasjoner: https://www.skatteetaten.no/skjema/a-melding-veldedig-allmennyttig/
- Skatteetaten – pensjonsinnretning: https://www.skatteetaten.no/nn/bedrift-og-organisasjon/arbeidsgiver/a-meldinga/rettleiinga-til-a-meldinga/pensjonsinnretning-obligatorisk-tenestepensjon
- Skatteetaten – trekk i lønn for ferie: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/lonn-og-ytelser/oversikt-over-lonn-og-andre-ytelser/trekk-i-lonn-for-ferie
- Skatteetaten – feriepenger og halv skatt: https://www.skatteetaten.no/nn/presse/nyhenderommet/derfor-trekkes-det-ikke-skatt-av-feriepengene/
- Lovdata – folketrygdloven § 23-2: https://lovdata.no/lov/1997-02-28-19/§23-2
- Lovdata – likestillings- og diskrimineringsloven § 26a: https://lovdata.no/lov/2017-06-16-51/§26a
- NAV – moderniserte tjenester: https://www.nav.no/arbeidsgiver/moderniserte-tjenester
- Digdir – overgang fra Altinn II til Altinn 3: https://samarbeid.digdir.no/sites/samarbeid/files/2025-12/Viktig%20informasjon%20-%20Overgang%20fra%20Altinn%20II%20til%20Altinn%203.pdf
- Revisorforeningen – skattetrekkskontoen fjernes: https://www.revisorforeningen.no/fag/nyheter/skattetrekkskontoen-fjernes-fra-1.-januar-2026/
- KPMG – krav om skattetrekkskonto opphører: https://kpmg.com/no/nb/innsikt/skatt-regulatorisk/krav-skattetrekkskonto-opphorer.html
- Forskningsrådet – kostnader for næringsliv og offentlig sektor: https://www.forskningsradet.no/finansiering/hvordan-skrive-soknad/budsjett/kostnader-naringsliv-offentlig-sektor/
- Forskningsrådet – timesatser i instituttsektoren: https://www.forskningsradet.no/forskningspolitikk-strategi/instituttsektoren/innmelding-timesatser

**Praksis, kalendere og roller**
- UiB – kjøreplan for utbetaling 2026: https://www.uib.no/foransatte/175460/utbetaling
- NTNU – betalingsplan 2026: https://i.ntnu.no/wiki/-/wiki/English/Payment+schedule+for+salaries+and+refunds
- UiB – selvbetjeningsportalen og DFØ-appen: https://www.uib.no/foransatte/175680/selvbetjeningsportalen-og-df%C3%B8-appen
- Bærum kommune – stillingsbeskrivelser i lønnsenheten: se lenker i 3.1
- Sticos – a-melding mot regnskap: https://www.sticos.no/fagstoff/skal-a-meldingen-alltid-stemme-med-regnskapet
- Sticos – avstemming av lønn og AGA: https://support.sticos.no/hubfs/Avstemming%20av%20l%C3%B8nn%20%26%20arbeidsgiveravgift.pdf
- Revisjon og Regnskap 2014: https://www.revregn.no/asset/pdf/2014/7-45-6.pdf
- APQC – lønnsmottakere per FTE: https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/number-employees-paid-fte-performs
- Azets – lønnshåndtering: https://www.azets.com/no-no/tjenester/lonnstjenester/alt-du-trenger-a-vite-om-lonnshandtering

**Tariff**
- NTL – HUK-protokoll 2026: https://www.ntl.no/Content/236135/cache=1781783091000/attr=54859A4B558E247CE0630B00000A6027/HUK-oppgj%C3%B8r%202026%20-%20Protokoll%20-%20Landsoverenskomst%20for%20virksomheter.pdf
- Virke – gjennomførte forhandlinger 2026: https://www.virke.no/tariff-og-lonn/tariffoppgjor-2026-dette-ma-du-vite/gjennomforte-forhandlinger/
- Virke – nytt lønnssystem i HUK 2022: https://www.virke.no/tariff-og-lonn/huk-omradet/huk-oppgjoret-nytt-lonnssystem
- NHH – likelønnsdirektivet: https://nhh.no/nhh-bulletin/artikkelarkiv/2026/juni/likelonnsdirektivet-eu-landene-bommer-pa-fristen/

**Kontroll og revisjon**
- Sykehuset Innlandet – interimrevisjon: https://www.sykehuset-innlandet.no/4946ed/siteassets/styret/2018/2018-03/025-2018-vedlegg-03-oppsummering-interimrevisjon.pdf
- Trondheim kommune – saksfremlegg: https://publikum.trondheim.kommune.no/application/get_saksfremlegg/35235
- Kristiansand kommune – rapport om lønnshendelse: https://www.kristiansand.kommune.no/contentassets/d6fb88872a7b4f88b84e57f20e50318e/rapport.lonnshendelse.pdf
- Oslo kommunerevisjon – rapport 4/2026: https://www.oslo.kommune.no/politikk/budsjett-regnskap-og-rapportering/rapporter-fra-kommunerevisjonen/rapport-4-2026-regnskapsrevisjonen-2025---med-vekt-pa-okonomisk-internkontroll/
- Zalaris – managed payroll: https://zalaris.com/managed-services/hr-&-payroll-outsourcing/managed-payroll-&-hr-services
- SAP – SOC 1 for Employee Central Payroll: https://www.sap.com/about/trust-center/certification-compliance/sap-successfactors-ecp-soc-1-2023-h2.html
- KPMG – attestasjonstjenester: https://kpmg.com/no/nb/tjenester/revisjon/attestation-services.html

**Smertepunkter og marked**
- Regnskap Norge – Lønnssystemer 2025 (publisert 17.3.2026): https://www.regnskapnorge.no/contentassets/b173a1e31cd741af9b610fc80db70ddf/lonnssystemer---resultater-til-publisering.pdf
- UiB styresak – BOTT økonomi og lønn: https://ekstern.filer.uib.no/ledelse/universitetsstyret/2022/2022-03-10/S_26-22BOTT_%C3%98konomi_og_l%C3%B8nn_Status.pdf

**Integrasjoner**
- DNB – pensjon og a-melding: https://www.dnb.no/bedrift/a-aa/pensjon/a-melding
- KLP – rapportering av ansattopplysninger: https://www.klp.no/virksomhet/pensjon/hr-lonn-og-personal/rapportering-av-ansattopplysninger
- Nordea – innskuddspensjon: https://www.nordea.no/bedrift/kundeservice/sporsmal-og-svar/Innskuddspensjon.html
- DNB – filoverføring: https://www.dnb.no/bedrift/hjelp-og-veiledning/filoverforing
- SpareBank 1 SN – lønnslister i nettbank: https://sn.no/-/media/NYE-NETTSIDER/BM/Brukerveiledning-Lnnslister-ny-nettbank-bedrift.pdf
- Planday – integrasjoner: https://www.planday.com/how-it-works/integrations/visma · https://www.planday.com/how-it-works/integrations/tripletex

**Anbud (TED, norske oppdragsgivere):** 169076-2025 (Ferde), 419499-2025 og 177740-2026 (Norske tog), 367086-2024 og 752679-2024 (Randaberg), 763121-2023 (GRID-Arendal), 107323-2024 (Entur), 291054-2024 (Tensio), 46448-2024 (Gassnova), 396670-2024 (Narvik), 373762-2024 (NORCE), 745040-2025 og 745370-2025 (Bergen), 102696-2024 (Nofima), 322096-2025 (HiØ), 440999-2026 (BIR), 449466-2026 (Nye Veier). URL-format: `https://ted.europa.eu/en/notice/-/detail/<nr>`.

---

### Metode og begrensninger

- Anbudsdata er hentet fra TED sitt søke-API (norske oppdragsgivere, relevante CPV-koder, 2020–2026). Kravspesifikasjonene (bilag 1) ligger bak innlogging i Mercell, TendSign og EU-Supply og er ikke lest. Kategoriene i 9.3 bygger derfor på kunngjøringstekstene og erfaring.
- Tidsbruk, bemanning og fortellingen i kapittel 11 er erfaringsbaserte anslag, ikke målinger.
- Forskningsrådets satser (0,8–1,1 promille, 1 100 kr per time, 1 850 timer) er hentet fra en side med uklar versjonsdato og må verifiseres mot gjeldende utlysning.
- Søkebudsjettet ble brukt opp mot slutten av arbeidet. Enkelte detaljer (bl.a. Skatteetatens veiledning om styrehonorar, bankenes regler for skjuling av lønnsbetalinger og Nordeas valideringsregler fra 9.9.2026) er beskrevet ut fra praksis eller kildeoverskrifter og bør kontrolleres.
