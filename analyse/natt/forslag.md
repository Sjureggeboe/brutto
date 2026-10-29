# Forslag fra nattarbeidet

Forslag til endringer i kartleggingen og spørsmål til Peter og Sander. Hvert forslag har id-en til punktet det kommer fra. Ingenting her er lagt inn i build/data/*.json.

## N03 Avstemmingsrapporten (A07)

### Endringer i kartleggingen
- **F-REG-30:** Rett «Feriepengegrunnlag og avsetning mot 2940». A07 har ikke feriepengegrunnlag. Fase 1 kan bare avstemme utbetalte feriepenger mot debet på 2940 og gjøre en rimelighetskontroll av avsetningen.
- **F-REG-30, F-REG-02, F-REG-03:** Erstatt 1:1-mapping konto ↔ lønnsbeskrivelse med to nye entiteter: D-A07Gruppe og D-A07Kontoregel (konto eller grupperingskode → A07-gruppe, med saldotype: bevegelse, debet, kredit, IB eller UB). Mappingen må finnes i to retninger: lønnsart → konto og konto → A07-gruppe.
- **F-REG-27 / F-RAP-15:** Ny funksjon: årlig kontrolloppstilling over lønns- og pensjonskostnader (tidl. RF-1022, skatteforvaltningsforskriften § 7-2-11) med kolonnene bokført, tillegg, fradrag og innrapportert, og signering av arbeidsgiver og revisor.
- **F-MYN-42 / P05:** Legg til kontrollene «flere kildesystemer» (`kildesystem`) og «Skatteetatens avvik per inntekt» (`inntekt.avvik[]`).
- **F-PER-35:** Noter at arbeidsforhold finnes i avstemmingsrapporten, men at navn, ansattnummer og avdeling må komme fra regnskapssystemet (F-REG-29). Navn og arbeidsforhold ved flermånedsbestilling [verifiseres].
- **F-REG-29:** Lesekravet blir debet og kredit per konto og måned, pluss IB og UB for 2931, 2932, 2940, 2945, 2967, 2780, 2785, 2600–2690 og 2770.
- **F-MYN-21 / F-MYN-24:** Endringen 12.10.2026 kom uten nytt versjonsnummer. Legg til overvåking av SBS-nyheter og kontraktstester mot TT02.
- **D-Avstemmingsrapport, D-Avstemmingslinje, D-Kontomapping, D-Avvik, D-Kontrollsak:** Juster etter datamodellen og avvikskodene i natt/funn/N03.md §6–§7.

### Spørsmål til Peter og Sander
1. Generere Rust-klient fra OpenAPI 1.0.2 (96 skjemaer, tre endepunkter), eller håndskrevne typer med `Option` overalt og egne typer for `Beloep`, `BeloepSomHeltall` og `Desimaltall`?
2. Jobbkø med én aktiv bestilling per opplysningspliktig, retry ved 429 og `FEILET`, og kvote per byrå (M10): hvordan?
3. Lagre én rapport per måned og én per år per opplysningspliktig, eller bare månedlige og summere selv? Tallene kan avvike etter erstatningsmeldinger.
4. Normalisert lag som Postgres-tabeller eller visninger over rå JSONB? Påvirker RLS, kryptering av fødselsnummer (D09) og kjøretid for kontrollene.
5. Hvordan tolkes tidspunkter uten tidssone i rådata fra før 12.10.2026?

## N01 Utleggstrekk, bidragstrekk og andre trekk

### Endringer i kartleggingen
- **F-PER-35:** Ny trekkoversikt per ansatt og måned med `utleggstrekk[]` fra A07 (type, beløp, dato). Krever ingen ny tilgang.
- **F-MYN-42 / F-REG-30 (P05, K01):** Legg til trekkontrollene T1–T6 i fase 1 og T7–T10 i MVP (se natt/funn/N01.md). T4 og T5 krever mapping av trekkontoer per kunde (R02).
- **Standard kontoplan-mapping (R02, S #27/#28):** Foreslå underkontoer 2611 samordnet, 2612 gammel skatt, 2613 annet gammelt og 2620 gammelt bidrag, gruppert til 2600.
- **D-Myndighetsabonnement:** Ny tjeneste `dialogporten_utleggstrekkbrev` (brevsensor T6, bare søke-API og metadata).
- **F-MYN-03 / M05:** Direktekunder må gi `lonn` i tillegg til `a-ordning` for brevsensoren. Byrå har tilgang med `regnskapsforer-lonn`.
- **F-MYN-28 / F-TRK-17:** Trekkpålegg-API flyttes til MVP. Aktiveres per kunde etter første a-melding fra Brutto. Daglig henting med `sekvensnummer` som vannmerke, og rett før beregning.
- **F-KJO-24:** Nytt eller endret pålegg etter beregning blir et varsel, ikke en hard sperre. Pålegget tas med i neste kjøring.
- **F-TRK-21 / F-MYN-29:** Avgrens til gamle trekk. For samordnet trekk er a-meldingen meldingen.
- **F-TRK-22:** Gammelt bidragstrekk rapporteres ikke i a-meldingen. Bidrag i samordnet trekk rapporteres som `utleggstrekkSamordnet`. Fjern [verifiseres].
- **F-MYN-17 / R2 §3.10:** Samordnet trekk betales til 7694 05 69814. KID for gammel utleggstrekk skatt kommer ikke lenger i tilbakemeldingen, og Brutto må lage den selv (kravtype 03, termin-KID, se N17).
- **D-Trekkpalegg:** Samordnet pålegg har ingen saldo, sluttdato eller kreditor. `saldo_kjent` og `prioritet` gjelder bare gamle trekk. Påleggsgiver for samordnet er alltid Innkrevingsmyndigheten. Utvid `regelverk` med `gammelt_si`, `gammelt_namsmann` og `gammelt_kommune`. Nytt felt `kilde_dialog_id`.
- **F-BET-01 / F-BET-05:** Hvert samordnet trekk er en egen betaling med egen KID. Gammel skatt betales samlet med én KID.
- **F-BYR-15:** Kolonne for trekkavvik per klient i samlehentingen.
- **F-SIK-08 / F-SIK-16:** Trekkdata bak lønnstilgang med logget lesing. Ingen henting av brevinnhold i fase 1.

### Spørsmål til Peter og Sander
1. Skal fase 1 be direktekunder om `lonn` i tillegg til `a-ordning`, slik at brevsensoren virker? Samtykket blir større, men skattekort åpnes også for MVP.
2. Dialogporten-klient i Rust allerede i fase 1 (scope `digdir:dialogporten`, systembruker-token, bare søk)? Kan gjenbrukes for tilbakemelding på a-meldingen og NAV-dialoger.
3. D-Trekkpalegg i fase 1 som lett register for manuell registrering, eller vente til MVP? I så fall bitemporal versjonering (R3 D-38) fra start.
4. Godtar dere T1–T6 som startliste for trekkontroller i fase 1, som kode med versjon (K01)?
5. Skal Brutto foreslå underkontoene 2611/2612/2613 i standard mapping, eller bare lese det kunden har?
6. Lagre rå pålegg og dialogmetadata uendret (D07)? Pålegg har fødselsnummer og skal krypteres (F-SIK-19).

## N02 Regnskapsføring av lønnskjøringen

### Endringer i kartleggingen
- **F-REG-30:** Presiser «per person der det er mulig». A07 mot hovedbok avstemmes per konto og grupperingskode. Avvik per person kan bare finnes mot lønnssystemets data.
- **F-REG-29 / D-Regnskapskonto:** Fyll `reskontro`, `krever_avdeling`, `krever_prosjekt` og `krever_fri_dimensjon` allerede ved lesingen i fase 1 (Tripletex `ledgerType`, `requiresDepartment`, `requiresProject`, `requiresFreeDimension1–3`). Posteringer på lønnskontoer er Lønnsdata og leses bare med lønnstilgang (S #6, #9).
- **P05:** Ny kontroll: saldo på 2930 er null etter betalt lønn, eller lik ubetalt netto. Åpne poster per ansatt på 2910 venter til MVP.
- **F-PER-35:** Ansattoversikten krever ikke at Brutto oppretter ansatte i regnskapssystemet.
- **F-REG-05 / D-Regnskapsoppsett:** Ett bilag per kjøring. AGA per sone og sats som egne linjer. Standard `aggregering` = per konto og dimensjon.
- **F-REG-06 / F-RAP-09:** Lønnsjournalen er dokumentasjonen etter forskriften § 5-6 og ligger i Brutto. Standard `loennsjournal_vedlegg` = `aggregert`.
- **F-REG-07 / D-Regnskapsoppsett:** Ansatt settes bare når kontoen har `reskontro = ansatt`. Nytt felt `ansattreskontro` (ingen, reskontrokontoer, netto_per_ansatt). Standard: reskontrokontoer.
- **Ny kobling (D-Person eller eget objekt i PLA):** regnskapssystemets ansatt-id per person og integrasjon. Trengs bare for personer med reskontrolinjer.
- **F-REG-17/18/19/22:** Feltgrenser: Tripletex `externalVoucherNumber` 70 tegn, PowerOffice-referanse 50, `SaftBatchId` 35. Bruk kort, stabilt kjøringsnummer i stedet for `payrun:<uuid>:rev<n>`. `SaftSourceId` = Bruttos system-id.
- **F-REG-10:** Reversering og ny revisjon etter bokføringsloven § 9 og forskriften § 5-12 (gjensidig referanse).
- **F-KJO-31 / F-UTL-20:** Saldo per ansatt for forskudd holdes i Brutto og posteres mot 2910 med ansatt når kontoen er reskontro.
- **F-UTL-01:** Avklar hvem som bokfører utlegget (se N31).
- **F-REG-16:** Saldoliste per ansatt for 2910, 1570 og 1572 ved årsslutt (bokføringsloven § 11).
- **F-SIK-26 / F-SIK-29:** Eksport ved opphør må ha lønnsjournal og bokføringsgrunnlag med regnskapets bilagsnummer, så sporet holder i fem år. Systembeskrivelsen skal forklare samlebilaget.
- **F-REG-28:** Varsel ved dimensjon med én eller to ansatte.

### Spørsmål til Peter og Sander
1. Standard aggregering per konto og dimensjon, eller per lønnsart og dimensjon? Lønnsart gir flere linjer, men enklere avstemming mot A07-kodene.
2. Kort kjøringsnummer i stedet for uuid i ekstern referanse (`SaftBatchId` 35 tegn, PowerOffice 50)?
3. Bilag som utkast (Tripletex `sendToLedger=false`, PowerOffice `JournalEntryVouchers`) og eget steg i godkjenningsflyten, eller direkte bokføring?
4. Skal Brutto opprette ansatte i regnskapssystemet når en reskontrolinje trenger det, eller kreve at de finnes?
5. Reskontrotype og dimensjonskrav på D-Regnskapskonto allerede i fase 1-lesingen?
6. PDF for bokføringsgrunnlag og lønnsjournal i Rust, låst med hash (F-REG-06): hvordan?

## N05 Ansattoversikt fra a-ordningen

### Endringer i kartleggingen
- **P03 (fase1.json):** Svaret er «Kombinasjon». A07 per måned er ryggraden. Navn, ansattnummer og avdeling fra regnskapssystemet (Tripletex, PowerOffice Go, ReAi) eller CSV/Excel-import. Virksomhetsdata fra Brreg. (Endres ikke i databasen, bare forslag.)
- **F-PER-35:** Grunnlaget er `a07_arbeidsforhold` per måned. Fjern D-Personbankkonto og kontonummer fra fase 1 (S #6). Legg til D-Feltkilde og D-Feltkonflikt. Personer uten navnekilde vises med maskert fødselsnummer og tilbud om kobling eller navneliste.
- **F-MYN-21:** Bestill per måned. Start med 3 måneder og fyll bakover til 13 (P07, M10). Bestill på nytt ved ny innsending.
- **F-MYN-42:** Erstatt den foreløpige listen med ANS-01–ANS-17. Første utgave: ANS-01, 02, 03, 04, 05, 07, 09, 12, 13 og 15. Avvikstyper i D-Avvik (K02).
- **F-REG-29:** Lesing av ansatte: fødselsnummer (kobling), navn, ansattnummer, avdeling, arbeidsforhold-ID, underenhet, start/slutt, stillingsprosent. Tripletex `/employee` + `/employee/employment`, PowerOffice `/Employees`, `/Employees/Employments`, `/FtePercentages` (`ReportingId`), ReAi ansatte + `employment-reporting`. Fiken: import. Kontonummer hentes ikke.
- **F-PLA-17:** Unntak for fase 1: automatisk kobling på eksakt fødselsnummer (blind indeks, D09). Arbeidsforhold kobles på arbeidsforhold-ID, så (fødselsnummer, underenhet, startdato), ellers koblingskø.
- **F-PLA-13, F-MIG-10, D-Permisjon:** Flyttes inn i fase 1 i enkel form (kilderegel per feltgruppe, navnelisteimport, permisjon/permittering som skrivebeskyttet kopi fra A07).
- **F-MYN-39 / F-ORG-02:** ANS-13 og ANS-14. Merknad: Skatteetatens `api/arbeidsforhold`, Opplysningspliktig-, Underenhet- og Opptjeningsgrunnlag-API-ene er bare for NAV og SSB.
- **F-MYN-38:** ANS-07 og ANS-08 som konkrete datakvalitetskontroller. **F-RAP-21:** ANS-02 med unntak for feriepenger og etterbetaling.
- **F-RAP-22 / F-RAP-07 / P06:** Antall, årsverk og turnover fra A07 alene. Kjønn og alder krever HR-kilde eller import, ikke fødselsnummer.
- **F-SIK-08 / F-SIK-19 / F-SIK-28:** Lønn per person fra A07 krever lønnstilgang. Fagforeningskontingent er særlig kategori. Tas inn i DPIA.
- **Datamodell (D06, D07, D08, L03):** Tre lag (rå, observasjon, sammenstilt). Nøkkel for arbeidsforhold: (opplysningspliktig, underenhet, person, `arbeidsforhold_id`). Nye entiteter D-Kildeobservasjon, D-Feltkilde, D-Feltkonflikt. D-Stillingsperiode utledes av månedsbildene.
- **MVP:** Brutto blir master for arbeidsforhold. ANS-04, 08 og 09 kjøres før innsending. Leserne fra fase 1 gjenbrukes som importadaptere i migreringen (F-MIG-05/06/07/16/17).

### Spørsmål til Peter og Sander
1. Tre lag (rå, observasjon, sammenstilt) med kilde per felt i fase 1, eller «siste henting vinner» og kildefelt først i MVP?
2. Greit med automatisk kobling på eksakt fødselsnummer via blind indeks (D09) som unntak fra F-PLA-17?
3. Lønn per person normalisert i fase 1 (`a07_inntekt_sum` per person), eller bare rå JSON og summer per virksomhet? Avgjør hvor mye lønnstilgang (F-SIK-08) som må finnes før første kunde.
4. Kan kontonummer tas helt ut av fase 1?
5. Hente 3 måneder først og fylle bakover til 13 i bakgrunnen, med én bestilling om gangen per opplysningspliktig?
6. Hvilket regnskapssystem først for ansattdata? PowerOffice Go har `ReportingId` og enkel kobling. Tripletex er uklart (N35).
7. Én rad per arbeidsforhold og måned i `a07_arbeidsforhold`, eller bare endringer (intervaller)?

## N06 Bli leverandør hos Digdir, Skatteetaten og Altinn

### Endringer i kartleggingen
- **M02 / M01:** Avgjøres før alt annet. Velg leverandørselskap og navngi teknisk eier og reserve. Orgnr inngår i system-id-en i Altinn, så et senere bytte krever ny godkjenning hos alle kunder.
- **F-MYN-01 / M03:** Egen nøkkel (JWK) i KMS i Norge, manuell rotasjon hver 6. måned med alarm 30 og 7 dager før. Ikke kjøp virksomhetssertifikat i fase 1. Systemregistrering som kode med `isVisible: false` [verifiseres]. Egne klienter og nøkler for test og prod (H04).
- **Søknader i uke 1:** `skatteetaten:innrapporteringamelding`, `skatteetaten:skattekorttilarbeidsgiver` og `altinn:events.subscribe` i samme runde, så MVP-tilgangene er klare uten ny kø.
- **F-MYN-02:** Direktekunde ber om `ske-avstemmingsinformasjon-amelding` eller `a-ordning` (se spørsmål 3). Brevsensoren (N01, T6) krever `lonn` og `digdir:dialogporten`.
- **F-MYN-04/05, F-BYR-07/08/09:** Én agent-systembruker per byrå med `regnskapsforer-lonn`. Klientkobling i Altinn-portalen som standard (M09). Status per klient fra `authorizedparties` og REGN-sjekk i Brreg. D-Klienttilknytning får `kilde_status` og `sist_verifisert`.
- **F-MYN-06 / F-MYN-22:** Nattlig helsesjekk (`bysystem`, MP-303) og saker ved `TimedOut`, `Rejected` og slettet systembruker, med ferdig tekst til kunde og byrå.
- **F-MYN-24 / C4:** Abonnement på SBS-nyheter, statusside og Slack er en plikt etter vilkårene. Altinn-varslingspunktet holdes oppdatert.
- **F-SIK-27 / E1:** Databehandleravtale signert før første produksjonskall med kundedata. Røyktest mot eget orgnr med `utenInntektsmottakere = true` kan gjøres før.
- **F-SIK-36 / M07 / M11:** Bare syntetiske Tenor-data i test. Testbyrået må være et Tenor-selskap registrert som regnskapsfører for testklientene.
- **D-Systembruker:** Nye felt `foresporsel_id`, `confirm_url_hentet`, `utloper` (opprettet + 10 dager), `paaminnelser_sendt`, `godkjent_av_rolle` (bare rollenavn).
- **Ny F-id: «Leverandøravtaler og tilgangsregister» (E3.13 i R2):** Internt register over vilkår, scopes per miljø, nøkler med utløpsdato, varslingspunkt og kontakter per etat. Logg dato for hver søknad og hvert svar, så neste estimat bygger på egne tall.
- **F-MYN-03 (MVP):** Endringsforespørsel (`systemuser/changerequest/vendor`) legger til `lonn` og `lonn-personopplysninger-saerlig-kategori` når lønnskjøring startes (S #16). Må inn i onboarding-UX.
- **F-MYN-28 (MVP):** Trekkpålegg først etter produksjon med innsending og minst én a-melding gjennom Brutto. Planlegg 1–3 uker for testoppsummering og avtale.
- **Tidsplan:** 7–10 uker fra orgnr til første produksjonskall [verifiseres]. Kritisk vei er tildeling av scopes. Køene er trolig lange fram mot Altinn II-fristene 17.11 og 31.12.

### Spørsmål til Peter og Sander
1. Hvilket selskap er leverandør (M02), og hvem er teknisk eier og reserve (M01)? Søknadene kan ikke sendes før dette er avklart.
2. Hvilken KMS i Norge for Maskinporten-nøkkelen? Holder manuell rotasjon hver 6. måned i fase 1?
3. Direktekunder i fase 1: enkeltrettigheten `ske-avstemmingsinformasjon-amelding` (minst samtykke), eller `a-ordning` + `lonn` med en gang (S #16)?
4. Ett eller to systemer (standard og agent) i systemregisteret? Tåler dere `isVisible: false`?
5. Klientstatus for byrå: `authorizedparties`, testkall per klient, eller begge? Hvor ofte, gitt Altinns krav om hendelser framfor polling?
6. Kvitteringssiden for `redirectUrl`: hvordan knytter vi den til riktig tenant uten å stole på URL-parametere?
7. Røyktest i produksjon mot vårt eget orgnr før pilotkunden: hvem godkjenner den systembrukeren?

## N04 Lesing fra regnskapssystemene

### Endringer i kartleggingen
- **F-REG-29:** Tripletex (`/ledger/account` med `groupingCode`/`saftCode`, `/balanceSheet` med `includeActiveAccountsWithoutMovements=true`, `/ledger/posting`, klientliste `/company/>withLoginAccess`) og PowerOffice Go (`/GeneralLedgerAccounts`, `/TrialBalance` på to datoer, `/AccountTransactions`, `/ClientAdmin/Clients`) dekker alt. ReAi er billigste tredje adapter (ett kall gir IB, posteringer og UB).
- **F-REG-29 (reserve):** SAF-T 1.30-opplasting dekker andre systemer. Filen har hele hovedboken: strøm den, behold bare lønnskontoene, ikke lagre hele filen. Skriv det inn i rådata-regelen.
- **F-REG-01 / F-REG-03:** Les `grupperingskode` fra regnskapet der den finnes (Tripletex, PowerOffice), bruk Sjurs tabell ellers, og sett `grupperingskode_kilde`. Avled `grupperingskategori` fra Skatteetatens CSV.
- **S #28 (rettes, bare forslag):** 5800 → 5000 er bekreftet. 5390 → **5300** i Tripletex, ikke 5000.
- **F-REG-30:** Saldomotor med kontrollsum IB + D − K = UB mot systemets egen saldo, og håndtering av reverseringer. Map på grupperingskode og kundens kontoplan, ikke bare kontonummer. Ved nettoføring faller kontrollen tilbake på bevegelse og merkes «delvis».
- **F-REG-28:** Bruk feltvalg (`fields`/`Fields`) for å unngå ansattnavn. ReAi-adapteren fjerner `employeeName` før lagring. Skjerm 5800 og 2650 i lest hovedbok.
- **F-BYR-15 / F-BYR-08:** Én tilkobling for alle klienter i Tripletex, PowerOffice (partnernøkkel) og ReAi. Tilgangsdiagnosen viser om regnskapstilkoblingen virker og om orgnr stemmer med opplysningspliktig i A07. Felles jobbkø med A07, og én global grense per abonnementsnøkkel i PowerOffice (10 kall/s).
- **D-Regnskapskonto:** `standardkonto` = Tripletex `saftCode`, `grupperingskode` = `groupingCode`. Fjern `saldo` og `saldo_dato`.
- **Nye entiteter:** D-Regnskapssaldo (klient, konto, periode, dimensjonsnøkkel, IB, debet, kredit, UB, kilde, kontrollstatus, henting), D-Hovedbokslinje (lest postering, adskilt fra D-Postering) og D-Regnskapshenting (tidspunkt, metode, rådata-hash, antall linjer; evt. type av D-Importjobb).
- **D-Integrasjon:** `tredjeparts_hemmelighet_ref` må dekke Tripletex employee token, PowerOffice klientnøkkel (vises bare én gang) og ReAi-token. `ekstern_kontoreferanse` = companyId, clientId, tenantId eller companySlug.
- **F-REG-18/19 (MVP):** PowerOffice krever `JournalEntryVoucher` med manuell bokføring når et eksternt system tar imot bilag. Om det gjelder lønnsbilag [verifiseres].
- **F-REG-21 (MVP):** Visma.net ERP som første Visma-variant (`generalLedgerBalance` gir debet og kredit per periode).
- **F-REG-22 (MVP):** Fiken har ikke kontofilter på bilag og koster kunden 99 kr/mnd for API. Bruk `transactionType=Lønn` og filtrer i Brutto.
- **F-REG-24 (MVP):** Samme saldomotor for Bruttos egen lønn mot hovedbok, med matching på `externalVoucherNumber`/`ExternalImportReference`. Webhooks (Tripletex) og `lastChanged…` (PowerOffice) trigger ny avstemming.
- **Senere:** ISV-avtale med Visma (550 kr/mnd) når to Visma-adaptere finnes. Bruttos egen SAF-T-eksport med grupperingskoder på lønnskontoene.

### Spørsmål til Peter og Sander
1. Én trait med `Evner` og standardmetoder, eller separate traits (`Saldo`, `Periodesaldo`, `Posteringer`)? `async_trait` eller nativ async-trait med `BoxStream` for paginering?
2. Én felles token-bucket per (system, legitimasjon) i jobbkøen, delt med A07-bestillingene?
3. Beløp: parse JSON-tall direkte til `rust_decimal` (serde `arbitrary_precision`), aldri via `f64`. Fiken bruker øre som heltall. Enige?
4. Klienter: generere fra OpenAPI (Tripletex 4,8 MB) eller håndskrive lesestien og generere modellene?
5. PowerOffice-klientnøkkel og Tripletex employee token kan ikke leses igjen. Rett i KMS, med rotasjon og varsel ved 401?
6. Opptak og avspilling med syntetiske data, og nattlige kontrakttester mot Tripletex test og PowerOffice demo i CI?

## N21 ReAi og Vinderen Industrier (tenant 2915)

### Endringer i kartleggingen
- **F-REG-29 / F-MIG-06 (ReAi-lesing):** Ansatte via `/api/employees`, `/employees/{id}` og `/employment-reporting`. Kontoplan med reskontrotype fra `GET /api/chart-of-accounts/accounts` (`subsidiaryLedger.type = employee` → `D-Regnskapskonto.reskontro = ansatt`: 2910, 2930, 2940). Posteringer via `/api/postings` (filter `accountNumber`, `employeeId`) og bilag via `/api/vouchers?voucherType=SALARY`. Ikke les kontonummer.
- **F-REG-28 / F-SIK-08:** Hos ReAi-kunder ligger nettolønn og feriepenger per person i hovedboken. Posteringer på 2930 og 2940 er lønnsdata og krever lønnstilgang (S #9). Saldo per konto som standard.
- **F-REG-30 (feriepenger):** For ReAi-kunder kan 2940 avstemmes per ansatt. Legg ReAis kontoer inn i D-A07Kontoregel og D-Kontomapping: 5092/2940 og 5405/2785.
- **F-REG-30 / F-MYN-42:** ReAi avstemmer A07 bare mot egne a-meldinger, ikke mot hovedboken. Bruttos avstemming mot hovedboken er et tillegg ReAi-kunder ikke har.
- **Ny kontroll (F-MYN-42, T4/T5 i N01):** Saldo på 2610 uten tilsvarende `utleggstrekk` i A07 er avvik. Treffer ReAi-kunder hvis ReAi ikke rapporterer trekket [verifiseres].
- **F-PER-35 / F-PLA-17:** ReAi gir `employmentId = null` for genererte ID-er. Koble på (fødselsnummer, underenhet, startdato), resten til koblingskøen. Mangler `enterpriseOrganizationNumber`, slår ANS-13 til. `name` er ett felt.
- **F-REG-07 / D-Regnskapsoppsett (MVP):** For ReAi bør standard `ansattreskontro` være `netto_per_ansatt`, fordi 2930 er ansattreskontro der. Avklar om ReAi godtar 2930/2940 uten ansatt (N33).
- **Ny F-id (MVP): F-REG-ReAi:** ReAi-adapter som skriver manuelle bilag (`POST /api/manual-vouchers`) med `employeeId` på reskontrolinjene. Ikke `salary-payments/import` (kan ikke endres og sperrer ReAis a-melding for måneden).
- **F-UTL-01 / F-REG-09:** ReAi-utlegg står på 2910 per ansatt. Utbetaler Brutto utlegget, må bilaget debitere 2910 med ansatt-id og lukke postene.
- **F-MIG-06 / F-MIG-25 / D-Trekkpalegg:** Faste trekk fra ReAi mangler konto, saldo, mottaker og periode. Importer som D-Trekk, aldri D-Trekkpalegg. Utleggstrekk hentes på nytt fra Skatteetaten eller brev, med fire øyne.
- **F-MIG-16 / F-MIG-17:** ReAi-genererte arbeidsforhold-ID-er hentes fra A07 før første a-melding fra Brutto.
- **F-TRK-06 / F-TRK-07:** Bruk ikke trekkhistorikk fra ReAi som fasit (tabelltrekk bare for støttede 2026-tabeller og `mainEmployer=true`).
- **F-KJO-23 / F-KJO-24:** ReAi sender a-meldingen i samme kall som fullføringen, uten fire øyne. Brutto skiller godkjenning fra innsending. Salgsargument.
- **F-REG-11 / F-KJO-28:** Korreksjon av feriepengeavsetning som eget bilag (5092/2940, 5405/2785) uten ny lønn er et godt mønster.
- **Senere:** Utlegg fra ReAi som kilde for F-UTL-01. ReAi betaler skatt og AGA automatisk etter godkjent a-melding: målbilde for Bruttos betalingsflyt.

### Spørsmål til ReAi (stilles av et menneske)
1. Hvordan konteres SALARY-bilaget: samlet eller per ansatt på 5000, 2600 og 5400/2770? Følger avdeling, prosjekt og AGA-sone med?
2. Hvilket format har genererte arbeidsforhold-ID-er, og hva skjer når underenheten er tom eller endres?
3. Rapporteres utleggstrekk registrert som «trekk etter skatt» i a-meldingen?

### Spørsmål til Peter og Sander
1. Egen ReAi-adapter i F-REG, med lesing i fase 1 og bilag i MVP?
2. Standard for ReAi-kunder: netto per ansatt på 2930 (ReAis modell) eller samlet 2930 (N02)?
3. Bruke ReAis bufrede A07 (`GET /api/a-melding-reconciliations`) for ReAi-kunder i fase 1, eller alltid hente selv via Maskinporten? ReAis svar har fullt fødselsnummer og krever brukerens token.
4. Er hullet i trekkpålegg hos ReAi et salgsargument vi vil bruke, eller noe vi først bekrefter med ReAi?

## N26 Tilgang til Trekkpålegg-API uten innsending

### Endringer i kartleggingen
- **F-MYN-28:** Ingen Trekkpålegg-API i fase 1. Tjenestebeskrivelsen godtar bare «Innrapportering A-melding API», og kunden må ha rapportert gjennom Brutto. Planen skal ikke avhenge av svaret fra Skatteetaten.
- **F-BYR-15 (rettes):** I fase 1 bare tilbakemelding (når den finnes), avstemmingsrapport (F-MYN-21) og brevsensor. Trekkpålegg-API og D-Trekkpalegg som API-data flyttes til MVP.
- **F-MYN-42 / F-REG-30:** Kontrollene T1–T6 fra N01 inngår (svar på P05, K01).
- **D-Trekkpalegg (Bør i fase 1):** Lett manuelt register med `regelverk` (samordnet, gammelt_skatt, gammelt_annet, bidrag), skyldner, startdato, beløp eller prosent, KID, mottatt dato, `kilde_dialog_id` og nytt felt `innhentet_fra` (`brev_manuell` eller `api`). Bitemporal historikk fra start (R3 D-38).
- **D-Myndighetsabonnement:** `dialogporten_utleggstrekkbrev` i enumen `tjeneste`. Hvert nytt brev blir en sak (D-Avvik) som lukkes når trekket er registrert eller forklart.
- **F-MYN-28 / F-TRK-17 (MVP):** Aktiveres per kunde etter første a-melding fra Brutto. Krav: testoppsummering, signert bruksvilkår og tjenestebeskrivelse, databehandleravtale som dekker innhenting, visning og bruk. To moduser per klient: API for kunder som kjører lønn i Brutto, plan B for kontrollkunder.
- **F-MIG-25 (MVP):** Første lønnskjøring bruker manuelt registrerte trekk. Etter første a-melding sammenlignes registeret med API-et. Avvik blir sak.
- **F-KJO-24 (MVP):** Ny henting rett før godkjenning gjelder bare kunder med aktivt API.

### Handling (gjøres av et menneske)
- Henvendelsen til Skatteetaten (utkast med seks spørsmål i natt/funn/N26.md §8) sendes når leverandørselskapet er valgt (M02). Be samtidig om test-scope i TT02 hvis mulig. Registrer svaret og oppdater F-MYN-28, F-BYR-15 og D-Trekkpalegg.
- Spør Regnskap Norge om det finnes eller planlegges en avtale for regnskapsførere, lik revisorenes segmentavtale, som også dekker trekkpålegg.

### Spørsmål til Peter og Sander
1. Godtar dere at F-BYR-15 i fase 1 bare dekker avstemmingsrapport og brevsensor, og at trekkpålegg flyttes til MVP?
2. Lett manuelt trekkregister (D-Trekkpalegg) i fase 1 som Bør, så T7–T9 kan kjøres på manuelle data?
3. `innhentet_fra` (`brev_manuell` eller `api`) på D-Trekkpalegg fra start?
4. Utrede portveien «Brutto sender a-meldingen» for kunder med eget lønnssystem (åpner trekkpålegg, men gir Brutto ansvaret for innsendingen)? Se N25.
5. Hvem i leverandørselskapet sender henvendelsen, og når?
6. Bygge mot Trekkpålegg-API i TT02 sent i fase 1 hvis vi får test-scope uten innsending?

## N35 Arbeidsforhold-ID i Tripletex og ReAi

### Endringer i kartleggingen
- **F-PLA-17 / F-PER-35:** Koblingsregel i prioritert rekkefølge: (1) manuell kobling, (2) rapportert ID fra kilden, (3) lært ID, (4) (fødselsnummer, virksomhet, startdato) med ett treff på hver side. Resten til koblingskøen med årsakskoder (natt/funn/N35.md §6). Regel 4 er unntak fra F-PLA-17, som koblingen på fødselsnummer i N05.
- **D-Arbeidsforhold:** `arbeidsforhold_id` for Tripletex er ikke `Employment.employmentId` (bare importert hint). Riktig kilde er A07. For ReAi: `employmentId` når satt, ellers A07. `ekstern_ref` skiller `rapportert_id` og `intern_id`.
- **Ny entitet D-Arbeidsforholdkobling** (eller utvidelse av D-Personkobling): kilde, kildenøkkel, A07-nøkkel, metode (`manuell`, `rapportert_id`, `laert_id`, `person_virksomhet_start`), treffsikkerhet, status, gyldig fra/til, behandlet av.
- **D06:** Arbeidsforhold-ID og permisjons-ID lagres som tekst (150), aldri tall. Skatteetaten: høyst 150 tegn, `a-z A-Z 0-9 - _ .`, unik bare per person og virksomhet.
- **F-REG-29:** Tripletex `GET /employee` med `employments(id,employmentId,startDate,endDate,division)`. ReAi `employment-reporting`. PowerOffice arbeidsforhold med `ReportingId` og `EnterpriseId`.
- **R01:** PowerOffice Go gir eksakt kobling fra første dag. Tripletex og ReAi kobles med regel 4 og lært ID.
- **F-MYN-42:** Nye kontroller ANS-18 (ny arbeidsforhold-ID uten avslutning) og ANS-19 (ugyldig arbeidsforhold-ID). Sendt videre til N36.
- **F-MIG-16/17 og F-MIG-05/06/07 (MVP):** For Tripletex og ReAi tas ID-en fra A07. Lærte koblinger fra fase 1 er migreringsgrunnlag (Skatteetatens alternativ 1). PowerOffice `ReportingId` brukes direkte, også for permisjon og permittering.
- **D-Arbeidsforhold invariant (MVP):** Bruttos egne ID-er er korte og i ASCII (løpenummer per opplysningspliktig eller UUIDv7 i base32), aldri utledet av underenhet, aldri gjenbrukt. Importerte ID-er valideres mot XSD-mønsteret. Bytte av underenhet gir nytt arbeidsforhold med `forrige_arbeidsforhold`.
- **Synlighet (MVP):** Brutto viser arbeidsforhold-ID-en og lar kunden eksportere den.
- **F-PLA-22 (Senere):** Huma `employmentId` er ikke a-meldingens ID. Huma kobles til Bruttos arbeidsforhold.

### Handling (gjøres av et menneske)
- Spør Tripletex' utviklerstøtte om rapportert arbeidsforhold-ID kan vises i API-et.
- Spør ReAi om å dokumentere formatet på genererte ID-er og returnere dem i `employment-reporting`, hva som skjer når underenheten er tom eller endres, og om `employmentId` valideres mot Skatteetatens tegnsett og 150 tegn.

### Spørsmål til Peter og Sander
1. Automatisk kobling på (fødselsnummer, virksomhet, startdato) med ett treff på hver side, og A07-ID lagret som lært ID?
2. Egen tabell D-Arbeidsforholdkobling, eller D-Personkobling utvidet med arbeidsforholdsnivå?
3. Format på Bruttos egne arbeidsforhold-ID-er i MVP: løpenummer per opplysningspliktig eller UUID-basert?
4. Skal byrået kunne godta alle forslag fra regel 4 for én kunde i én operasjon? Hvem får lov?
5. ANS-18 og ANS-19 i første kontrollpakke?

## N23 A07-mapping som datafil

### Endringer i kartleggingen
- **F-REG-02 / F-REG-03:** `natt/funn/N23-mapping.csv` (280 rader: 41 A07-grupper, 131 beskrivelsesregler, 94 kontoregler med saldoregel og fortegn, 14 reserveregler på grupperingskode) blir Brutto-malen (nivå `brutto_mal`) for D-A07Gruppe og D-A07Kontoregel.
- **S #28 (rettes, bare forslag):** 5390 → 5300. 5800 → 5000 bekreftet. 5252 og 5280 → 5000 bekreftet i Tripletex. Fjern [verifiseres] i F-REG-03 om at Sjurs koder er Skatteetatens.
- **D-Regnskapskonto:** `grupperingskategori` fra Skatteetatens CSV. `grupperingskode_kilde` = `regnskap` når lest, ellers `sjur_standard`.
- **F-REG-30:** Formlene i N23 §5, avstemming på hovedgruppe. Regelsett per kunde og gruppe (feriepenger via 2940 eller 2945, 5090 med eller uten 2931). Feriepengegrunnlag finnes ikke i A07: FP mot debet 2940, FPA mot feriepengelisten.
- **F-REG-29:** Debet og kredit for 2600–2690, 2770, 2940, 2945 og 5290. IB og UB for 2780, 2781, 2785, 2931, 2940 og 2980.
- **F-MYN-42:** Nye kontroller A07-K5 (uvanlig flaggkombinasjon) og A07-K6 (NAV-kode i arbeidsgivers A07). Kodeliste og inntektskombinasjoner som versjonert data (D-Regelpakke).
- **F-MYN-21:** Utleggstrekk finnes bare på personnivå. UTL-avstemmingen krever bestilling med inntektsmottakere.
- **F-RAP-15 / N24:** Kontrolloppstillingen fylles fra de samme reglene. Feltnavnene er kjent.
- **F-RAP-13:** AGA per virksomhet og sone krever avdeling eller underenhet på posteringene [verifiseres].
- **D-Avstemmingslinje:** Nytt felt `regelsett` ved siden av `a07_gruppe` og `kontoregel_refs`.
- **Personvern (S #7, #8, F-SIK-08):** 5800, 2650 og FR.FAGF er særlige kategorier. Skjermes også når de bare er lest fra hovedboken.
- **F-LON-01/02, D-Lonnsart (MVP):** De 26 standardlønnsartene får `fordel`, `amelding_beskrivelse`, `trekkpliktig`, `aga_pliktig` og `feriepengegrunnlag` fra beskrivelsesreglene, validert mot inntektskombinasjonene.
- **F-LON-06, D-Kontomapping (MVP):** Lønnsart → konto og konto → A07-gruppe må gi samme gruppe. Test begge veier.
- **F-KJO-14 / F-REG-11 (MVP):** Avsetning 5020/2940, utbetaling debet 2940, AGA av feriepenger flyttes fra 2785 til 2770 ved utbetaling.
- **F-REG-15 / F-FRA-26 (MVP):** Lagre metoden for NAV-refusjon per virksomhet. Den avgjør REF-regelen.
- **Senere:** Ny kodeliste (f.eks. R1 2027) lastes som ny versjon med diff-jobb. KI-støttet mapping av lønnsarter (F-MIG-13) kan bruke beskrivelsesreglene som fasit.

### Spørsmål til Sjur
1. Skal OTP ligge på 5420 (S #29) eller på 5945/5950? 5420 blander pensjon rapportert per person med AGA-grunnlag. Avgjøres før lønnskjøringen bygges (F-PEN-03).
2. Åpent for MVP: feriepengegrunnlag i grensetilfeller (trekk i lønn for ferie, sluttvederlag, tips, honorar). Kontrolleres mot forarbeidene til ferieloven og standardlønnsartene i Tripletex og Visma.

### Spørsmål til Peter og Sander
1. CSV-en i repoet bygget til Rust-tabeller (`build.rs`), eller lastet i Postgres som D-A07Gruppe og D-A07Kontoregel med nivå `brutto_mal`? Versjonering må følge kodelisten.
2. «Mest spesifikk regel vinner» og regelsett per kunde uten dobbelttelling: test som feiler når én konto treffer to regler i samme gruppe og regelsett?
3. Én saldokonvensjon (debet-positiv) i adapterlaget? Tripletex gir gjeld som negativ saldo.
4. Import fra Skatteetatens Excel: trim mellomrom og harde mellomrom, sammenlign eksakt, lagre kodelisteversjon på hver regel.
5. Toleranser for OTP og NAV-refusjon: logikk for tidsforskjell, ikke 0 kroner (K03). Hvordan modellere «forventet snur neste måned»?
6. Holder (type, fordel, beskrivelse, trekkflagg) som nøkkel for beskrivelsesregler, eller trengs `skatteOgAvgiftsregel` (nettolønn, Svalbard)?

## N36 Kontrollkatalog ANS-01–19

### Endringer i kartleggingen
- **F-MYN-42:** Erstatt listen med ANS-01–ANS-19 (natt/funn/N36.md). Første utgave av fase 1 har 13 kontroller i rekkefølgen ANS-12, 04 og 18, 07, 11, 19, 01 og 02, 03 og 05, 09 og 17, 13 og 15. Hver kontroll har id, versjon, `speiler_regel`, alvor og standardtekst i Rust (K01). Tersklene er data per kunde. P05 punkt 5, 6, 7 og 9 tilsvarer ANS-01, 03, 07 og 12.
- **F-MYN-38 / F-PER-24 (rettes):** Yrkeskoden (7 sifre) valideres mot SSBs yrkeskatalog (Klass 145, bygger på STYRK-98), ikke STYRK-08. STYRK-08 (Klass 7) brukes til visning og statistikk via korrespondansetabell 426. Lederkodesjekken gjøres på STYRK-08-koden. `sisteDatoForStillingsprosentendring` skal finnes (ANS-07b).
- **F-MYN-16:** Skatteetatens regneark med forretningsregler R1 2026 (179 regler) har meldingstekst på bokmål, nynorsk og engelsk. Grunnlag for tekstkatalogen. Snevre inn merknaden «API-et har ingen forklaringstekst».
- **F-MYN-10 / D-Regelpakke:** Forretningsregler og kodeliste importeres fra regneark som versjonerte data, valgt etter kalendermåned. Ingen API finnes.
- **F-PER-35:** Status `forsvunnet`, lenke til forgjenger (ANS-18), visning av når NAV setter maskinell sluttdato (etter tre måneder). Permitteringer leses fra `permisjon[]` med `beskrivelse = permittering`; `permittering[]` er tom til 2030.
- **F-RAP-21:** ANS-02 med unntakene i N36 §4 (tre lovlige rapporteringsmåter, opptjeningsperiode, én måned etterskuddslønn).
- **F-RAP-22:** Årsverk uten tilkallingsvikarer og 0 %. Headcount telles for seg. Utleide ansatte som eget filter.
- **F-MIG-14:** Avlønningstype utgikk i 2019 (F282). Kan leses ved import, aldri mappes til a-meldingen. R5 punkt 11 løst.
- **F-PER-20 / F-MIG-16:** Arbeidsforhold-ID lagres nøyaktig som den kommer, aldri trimmet eller normalisert. ANS-19 ved import, ANS-18 ved henting av A07.
- **F-PER-16:** Skatteetatens eksempel for fast flytting: avslutt med `endringIOrganisasjonsstrukturEllerByttetJobbInternt` og start dagen etter. Ny ID er også gyldig.
- **D-Avvik / D-Kontrollsak / D-Tilbakemeldingsavvik:** Nye felt `kontroll_id`, `speiler_regel`, `kilde` (`brutto`, `a07`, `a03`) og koblingsnøkkel (regel, O, V, P, arbeidsforhold-ID, M). Skatteetatens `oeyeblikkelig` → feil, `retningslinje` → advarsel.
- **D-Arbeidsforhold:** `arbeidsforhold_id` som tekst med sortering som skiller store og små bokstaver. Nye felt `forgjenger_id` og `nav_maskinell_sluttdato_forventet`. Ny status `forsvunnet`.
- **D-Permisjon:** Permitteringsfeltene (`varslingsdato`, `sluttdatoLoennsplikt`, `permitteringsaarsak`, `loennet`) er tomme til 2030-01.
- **Ny D-Kodeverk** (eller domenet `kodeliste` i D-Mappingregel): lokal kopi av eksterne kodelister (Skatteetaten-regneark, Klass 145, 7, 426) med versjon, gyldighet og tekst på tre språk.
- **MVP:** Samme kontroller på egen melding før innsending. Alle F-regler fra regnearket kjøres. ANS-04a og ANS-18 B/C blir harde stopp (F108 er øyeblikkelig). ANS-07b obligatorisk. F530 og F532 lastes når R2 2026 publiseres.

### Spørsmål til Sjur (lønnsfaglig)
1. Vurder gruppene av lønnsbeskrivelser i N36 §4: hvilke krever arbeidsforhold, og hvilke kan lovlig komme etter slutt? Sluttvederlag og lønn etter dødsfall er ikke nevnt i veiledningen.
2. Støttekontakter og avlastere: ordinært arbeidsforhold eller frilanser?

### Handling (gjøres av et menneske, tas med i henvendelsen til Skatteetaten)
- Skiller a-ordningen store og små bokstaver og ledende nuller i arbeidsforhold-ID? Gir alternativ 2 avvik 108? Hva er nøkkelen for arbeidsforhold-ID ved flytting (opplysningspliktig, underenhet, person, ID)? Blir grensen i F256 for sluttdato (31.12.2029) flyttet?
- Brreg: teller `antallAnsatte` personer eller arbeidsforhold, og regnes frilansere og korte arbeidsforhold med?

### Spørsmål til Peter og Sander
1. Mapping av alvor: `oeyeblikkelig` → feil, `retningslinje` → advarsel, Bruttos egne kontroller feil/advarsel/info?
2. Koblingsnøkkel (regel, O, V, P, arbeidsforhold-ID, M) med ett avvik og flere kilder, i stedet for ett avvik per kilde?
3. Regneark til D-Regelpakke ved bygging (data i repoet) eller ved oppstart fra lagret kopi?
4. Arbeidsforhold-ID som tekst, med sortering som skiller store og små bokstaver, uten normalisering?
5. Månedssammenligningen (ANS-04, 08, 11, 18): kjøres på nytt for M+1 hver gang M erstattes, eller bare når M+1 hentes?
6. ANS-18: lenke forgjengeren automatisk, eller foreslå og la brukeren bekrefte?
7. ANS-15 sist i første utgave, avhengig av F-REG-29?

## N39 Testdata for A07 i TT02 og Tenor

### Endringer i kartleggingen
- **M07 (besvares):** TT02 og Skatteetatens testmiljø med Tenor-virksomheter. Ingen ferdige testvirksomheter med a-meldinger for avstemmingsrapporten. Brutto må trolig sende egne syntetiske a-meldinger (H2). Bekreftes med første kall i TT02.
- **M11 / N22:** Testplanen kjøres på TV-1–TV-8 og S01–S27 (natt/funn/N39.md). Testbyrå: syntetisk regnskapsførerselskap med REGN-rolle fra det syntetiske Enhetsregisteret.
- **F-SIK-36 (utvides):** Testdataregister i repoet (bare syntetiske data), to identitetsvakter og opptaksvask. Tenor-API brukes ikke fra lavnivåtester.
- **F-MYN-01 / H04:** TT02-registreringen kan få test-only-rettighet for innsending (`ske-innrapportering-amelding`). **Bruttos ekte orgnr må trolig leses inn i TT02**: e-post til servicedesk@altinn.no i uke 1 [verifiseres].
- **F-MYN-21 / F-MYN-42 / F-REG-30:** Hver ANS-kontroll og A07-kode får minst én fixture, med fasit fra generatoren. S19–S22 bare med fixtures.
- **F-MYN-24:** Nattlig kontrakttest mot TT02 fanger endringer uten nytt versjonsnummer. Abonner på Tenors ATOM-feed og statussiden for testmiljøet.
- **F-MYN-04 / F-BYR-07 / F-BYR-08:** Tilgangsdiagnosen testes med TV-3c (fjernet) og TV-8 (uten REGN).
- **M10:** S27 måler 429 for samme og ulike opplysningspliktige gjennom byråtoken før jobbkøen bygges.
- **D07 / D-Avstemmingsrapport:** Opptak fra TT02 lagres i samme rå format som i prod.
- **Ny intern funksjon:** «Syntetisk A07- og a-meldingsgenerator» (scenario → a-melding v2.3 + forventet A07). Brukes til TT02-innsending, CI-fasit og senere sandkasse (F-PLA-06). Ny D-Testscenario.
- **MVP:** Generatoren blir testharnisk for egen a-melding (lukket sløyfe mot A07 i TT02). Testpålegg for trekk bestilles hos fremtidensinnkreving@skatteetaten.no (sendes av et menneske). Dolly bestilles via dolly@nav.no når NAV-integrasjonen starter.

### Handling (gjøres av et menneske)
- Send e-post til servicedesk@altinn.no om innlesing av Bruttos orgnr i TT02 (uke 1).
- Logg inn i Tenor og sjekk om KQL `regnskapsfoerere:<orgnr>` gir byråets klienter (fem minutter).
- Still spørsmål om validering av test-a-meldinger i Skatteetatens Slack eller brukerstøtte (se N22).

### Spørsmål til Peter og Sander
1. En liten a-meldingsgenerator allerede i fase 1 (1–2 uker)? Trolig nødvendig for A07-data i test, gjenbrukes i MVP.
2. Verktøy for opptak og avspilling i Rust (egen `reqwest`-mellomvare og `wiremock`, eller annet)? Syntetiske fixtures i repoet bak identitetsvaktene?
3. Hvem eier testdataene (Tenor-innlogging med egen BankID, velge TV-1–TV-8, holde registeret oppdatert)?
4. Test-only-rettighet for innsending i TT02, eller `a-ordning` for testkundene (avvik fra prod)?
5. Ett felles testbyrå for alle utviklere, eller ett per utvikler?
6. Skal nattjobben mot TT02 bare varsle, eller stoppe utrulling når kontrakten endres?
7. Hvem sender e-posten til servicedesk@altinn.no, og når?

## N40 Vilkår og tilgang i grensetilfeller

**Viktig:** Utviklervilkårene til Tripletex (10.2026) og PowerOffice/Visma (23.04.2020) forbyr å bruke API-et til å utvikle et eget konkurrerende produkt, krever forhåndsgodkjenning for «dashboarding» og aggregering på tvers av kunder, og kan sies opp med 30 dagers varsel eller straks ved mistanke. Tripletex krever i tillegg skriftlig samtykke før KI brukes på dataene. Fiken har et lignende forbud. Dette er ikke juridisk vurdert.

### Endringer i kartleggingen
- **F-REG-29 / F-REG-30:** SAF-T-opplasting fra kunden blir første kilde i fase 1. Adapterne for Tripletex og PowerOffice bygges parallelt, men går ikke i produksjon før skriftlig svar foreligger. Ikke hent hele SAF-T via Tripletex-API-et (masseuttrekk, dataminimering). Hent posteringer med kontofilter.
- **F-BYR-23 / KI:** Ingen KI på regnskapsdata i fase 1 uten samtykke fra Tripletex. Gjelder også interne verktøy og MCP mot kundedata i produksjon.
- **F-BYR-12 / F-BYR-13 / F-BYR-20:** Ingen aggregering på tvers av kunder (benchmark, normalnivåer) i fase 1. Byråets porteføljevisning krever godkjenning fra Tripletex og Visma og samtykke i kundeavtalen.
- **F-SIK-27:** Kundeavtale og databehandleravtale tar med samtykke til integrasjonen, byråvisning på tvers av klienter, eventuell KI, Altinns vilkår (§ 1.2) og Skatteetatens formålsgrense.
- **F-SIK-22 / F-SIK-26:** Data merkes med kildesystem. Sletting når kunden går eller utviklervilkårene opphører, etter retur til kunden, med skriftlig bekreftelse.
- **D-Integrasjon:** Nye felt `vilkaar_dokument`, `vilkaar_versjon`, `akseptert_dato`, `tillegg_ref`, `ki_samtykke` og `godkjent_bruk`.
- **Leverandøravtaler og tilgangsregister (ny F-id fra N06):** Utvides med private API-vilkår. PDF og hash per versjon, sjekk hver måned (F-MYN-24).
- **UI:** Tekstnavn, ikke logoer, til skriftlig godkjenning foreligger. Samtykkedialogen sier hvilket system kunden kobler til.
- **F-MYN-01:** Formålsspørsmålet til Altinn sendes før SBS-vilkårene godtas. Formålsregelen står i leverandørvilkårene § 1.2.1. A07-avstemming er trolig innenfor når dataene bare brukes for kunden [verifiseres med Digdir].
- **F-MYN-02/04/05, F-BYR-07/08, F-ORG-05/06, M13:** Standard systembruker per klient er reserven for lønnsbyråer, konsern og lokallag. Byråer uten REGN kan bruke egen systembruker for klientsystem med `a-ordning` når klientene har delegert pakken direkte. Én systembruker for klientsystem per byrå og pakkesett. Veiviser for klienten: «Gi fullmakt til byrået».
- **D-Systembruker:** Nye felt `tilgangsgrunnlag` (`er_regn`, `direkte_delegering`, `egen_virksomhet`) og `pakkesett`. **D-Klienttilknytning:** `tilgangsgrunnlag` per klient.
- **F-BYR-11:** Lagre tilgangsgrunnlag og byråets egenerklæring om autorisasjon eller unntak. Ikke markedsfør mot uautoriserte lønnsbyråer [advokat].
- **F-REG-02 / N23-malen:** Erstatt kontonavn fra SAF-T-standardkontoene med kundens egne kontonavn eller egne beskrivelser.
- **F-REG-18 / F-REG-19 (MVP):** Ikke start lønnskjøring for Tripletex- og PowerOffice-kunder før skriftlig svar. Reserve: bilagsfil kunden importerer (F-REG-17).
- **F-MYN-03 (MVP):** Direkte delegerte klienter må også delegere `lonn`. Ny systembruker for klientsystem med `a-ordning` og `lonn` i stedet for endringsforespørsel [verifiseres].
- **F-BYR-09 (MVP):** Klientdelegering i skala med systembruker og `klientadministrator`. Godkjenning av to personer i Brutto før en klient legges til eller fjernes.
- **F-REG-20/21/22 (MVP):** Be Xledger, Visma og Fiken om skriftlige API-vilkår før adapterne bygges. Fiken tillater ett samtidig kall.

### Handling (gjøres av et menneske)
1. Send skriftlig spørsmål til Tripletex (kontaktskjema for API-støtte) og PowerOffice (go-api@poweroffice.no) om konkurranseklausulen, dashboarding, aggregering for byråer og lønnsbilag. Beskriv Brutto ærlig. Be om bekreftelse eller tillegg til vilkårene.
2. Be en advokat vurdere utviklervilkårene (Tripletex 10.2026, Visma 23.04.2020, Fiken), sletteplikten etter opphør mot dokumentasjonsplikten, og konkurranserettslig stilling.
3. Send formålsspørsmålet til servicedesk@altinn.no (utkast i natt/funn/N40.md).
4. Be ReAi, Xledger og Visma (Visma.net, eAccounting) om skriftlige API-vilkår.

### Spørsmål til Peter og Sander
1. SAF-T-opplasting før adapterne, så fase 1 ikke avhenger av Tripletex og PowerOffice? Forslag: felles trait først, adaptere parallelt, ikke i produksjon før skriftlig svar.
2. Bruker noe i Brutto (også logging, feilsøking, interne verktøy) en språkmodell på regnskapsdata? I så fall trengs samtykke fra Tripletex.
3. Holder `tilgangsgrunnlag` på D-Systembruker og D-Klienttilknytning for flere systembrukere per byrå og kunde?
4. «Slett alt fra kildesystem X», inkludert avledede saldoer og rapporter, som én operasjon med skriftlig bekreftelse: hvordan?
5. Grenser per kildesystem i jobbkøen (F-BYR-15), ikke bare per abonnementsnøkkel?
6. Bare tekstnavn på regnskapssystemene, ikke logoer, til godkjenning foreligger?
7. Slå opp byråets autorisasjon i Finanstilsynets register ved onboarding?

## N27 Dialogporten i fase 1

### Endringer i kartleggingen
- **Ny F-id: F-MYN-43 «Dialogporten-sensor (polling)»:** Felles motor som poller søke-API-et per systembruker med `serviceResource` og `contentUpdatedAfter` og leser forsendelser med `/transmissions`. Kaller aldri `GET /dialogs/{id}` eller FCE-URL-er (endrer kundens «sett»/«åpnet»). Gjenbrukes av F-BYR-15, F-MYN-42, F-MYN-22, senere F-MYN-15 og F-MYN-28.
- **F-MYN-15 deles:** Fase 1 = lesing av A03 for meldinger fra andre systemer (polling). MVP = Events for meldinger Brutto sender selv.
- **F-BYR-15 (fase 1):** Tilbakemeldinger (A03) for alle klienter, også når et annet system har sendt [verifiseres i TT02]. Trekkpålegg er fortsatt bare brevsignal.
- **F-MYN-16 (fase 1, bare lesing):** Avvik fra A03 i klartekst per nivå. Retting i kundens eget lønnssystem. `avvisning` og `oeyeblikkelig` blir saker med frist den 5.
- **F-MYN-42 / N36:** ANS-kontrollene kobles mot A03 (`kilde = a03`). Doble varsler fjernes med koblingsnøkkelen.
- **F-MYN-22, nye saksregler:** nytt trekkbrev (T6), ny kontroll av forskuddstrekk, vedtak/påminnelse om tvangsmulkt, a-melding avvist i annet system, nytt `kildesystem` i måneden (signal om systembytte), flere innsendere for samme måned.
- **F-REG-30 / F-MYN-17 (Bør i fase 1):** `innbetalingsinformasjon` (KID, forfall) og `mottattAvgiftOgTrekkTotalt` fra A03 avstemmes mot 2600/2770 og bank.
- **F-MYN-02 / F-MYN-03 (endrer N06):** Enkeltrettigheten `ske-avstemmingsinformasjon-amelding` gir bare A07, ikke A03. Direktekunder bør gi `a-ordning` (A07, A03, trekkontroll, tvangsmulkt) og `lonn` (trekkbrev). Alternativ: fem enkeltrettigheter. Policyen har ingen ren lesetilgang; pakkene gir også innsending. Forklares i veiviseren.
- **F-MYN-04:** Byrå klarer seg med `regnskapsforer-lonn` for alt i fase 1.
- **F-MYN-01:** Systemregistreringen må ha `a-ordning`, `lonn` og `regnskapsforer-lonn` (eventuelt enkeltrettighetene).
- **Scopes:** Ingen nye for A03. `digdir:dialogporten` og `skatteetaten:innrapporteringamelding` dekker fase 1.
- **F-MYN-24:** Daglig jobb mot metadata-API-et varsler drift når en ny ressurs får dialoger i prod.
- **F-MYN-23 / F-SIK-08 / F-SIK-16:** Kall mot Dialogporten logges uten svarinnhold. A03 og brevmetadata bak lønnstilgang. Rå A03-JSON kryptert som A07.
- **D-Myndighetsabonnement:** `tjeneste` får `dialogporten_utleggstrekkbrev`, `dialogporten_trekkontroll`, `dialogporten_tvangsmulkt`, `dialogporten_trekkpaalegg_varsel`. `orgnr` valgfritt, nytt felt `omfang` (`per_orgnr`, `per_systembruker`), `vannmerke_type = content_updated_at`, nytt felt `ressurs_urn`.
- **D-Tilbakemelding:** Nye felt `kilde` (`brutto`/`annet_system`), `kildesystem[]`, `dialog_party`, `transmission_id`. `innsending_ref` tom for andre systemer.
- **D-Kontrollsak / D-Trekkpalegg:** `kilde_dialog_id` bekreftet. Dialogen har ingen strukturerte trekkfelt (KID, prosent, startdato), så registeret fylles for hånd.
- **MVP:** Events med `resourceFilter urn:altinn:resource:ske-innrapportering-amelding`. Trekkontroll-PDF via `skatteetaten:skattdialogdokument`, hentet bare når brukeren åpner saken. Migrerte Altinn 2-ressurser via Altinn Correspondence (se N25).

### Handling (gjøres av et menneske, tas med i henvendelsen til Skatteetaten)
- Er det innenfor vilkårene for `skatteetaten:innrapporteringamelding` å lese A03 for meldinger sendt fra andre systemer? Registrerer A03-API-et at forsendelsen er «åpnet»?

### Spørsmål til Peter og Sander
1. Én felles sensor-crate for Dialogporten i fase 1, med polling, uten webhook og med en handler per ressurs?
2. Håndskrevet klient for tre kall og A03-typer generert fra OpenAPI? Håndtering av ukjente enum-verdier og eksperimentelle felt?
3. Ett Maskinporten-token med begge scopes, eller ett per API (cachet per systembruker)?
4. Vannmerke `contentUpdatedAfter` med 10 minutters overlapp og duplikatfjerning, eller i tillegg full gjennomgang hver natt?
5. Direktekunder: `a-ordning` + `lonn` (enkelt, bred tilgang) eller fem enkeltrettigheter (minst tilgang, mer vedlikehold)?
6. Rå A03-JSON med samme lagring og oppbevaring som A07 (kryptert, uforanderlig, i Norge)?

## N07 Kontrollkatalog for lønnsavstemming (byråer og revisorer)

### Endringer i kartleggingen
- **F-REG-30 / F-MYN-42 / F-REG-27:** L-katalogen (L-01–L-31, natt/funn/N07.md) blir kontrollpunktene i avstemmingspakken. Månedspakke: L-01–09, L-23, L-24, L-26–29, L-31. Terminpakke: L-12–16, L-21, L-22. Årspakke: L-17–22, L-25, L-30. A07-kodene fra N03 blir `differansetype`. ANS- og T-kodene blir i D-Kontrollsak.
- **Første utgave (rekkefølge):** L-01, L-13, L-02, L-14, L-05, L-06, L-07, L-12, L-24, L-26, L-17. Dekker GRFS-minimumet (trekk og AGA per termin) og kontrolloppstillingen.
- **F-REG-30:** Feriepengepunktet blir L-06 (utbetalt mot debet 2940) og L-18 (rimelighet av avsetningen). Samme retting som N03 og N23.
- **F-RAP-15 / ny F-id:** «Kontrolloppstilling etter skatteforvaltningsforskriften § 7-2-11 med signering» (L-17), i strukturen fra `LoennsOgPensjonskostnad`, med signaturfelt for arbeidsgiver og revisor. Kan kjøres løpende hittil i år. Samme forslag som N03.
- **F-RAP-19 (merkes fase 1):** Revisorutdrag med A07-delen, avstemmingspakker for alle måneder og terminer, kontrolloppstilling, avviksliste med kvitteringer, rapport-ID og hash, regel- og programversjon. Lønnsjournal, attestasjon og endringslogg i MVP.
- **F-SIK-09 / F-RAP-04:** Revisortilgang og eksport i fase 1: PDF/A, xlsx og CSV med stabile nøkler. Personnivå bare med step-up. Fagforening (L-04) og 5800 (L-22) bare som sum.
- **F-REG-29:** Lesingen må også gi bokføringsdato på betalinger til 2600 og 2770, bilagstype, bruker og opprettet-tidspunkt per postering (L-29), kostnader for bil og telefon (L-30), og bankkonto på ansatte hvis API-et har det (L-31).
- **F-MYN-39 / F-RAP-13:** L-16 krever underenhetens adresse fra Brreg og AGA-sone per kommune som versjonert data i D-Regelpakke.
- **F-BYR-15 / F-RAP-07:** Klientlisten får én kolonne per kontrollgruppe (trekk, AGA, lønn, år) med status. Salgsdemo: «alle klienter, alle terminer, ett skjermbilde».
- **F-MYN-21:** L-04 og L-18 krever bestilling med inntektsmottakere.
- **D-Avstemmingslinje:** `kontrollpunkt` = L-xx, `differansetype` = A07-xx. Nye felt `toleranse_brukt`, `forventet_reversert_i_periode`, `regelsett_versjon`.
- **D-Avstemming:** Nye felt `kontrollkatalog_versjon`, `a07_raa_hash`, `hovedbok_uttrekk_hash`.
- **Ny D-Kontrolloppsett:** kontroll-ID, aktiv, toleransetype (kroner, prosent, per inntektsmottaker, virkedager), verdi, arv Brutto-mal → byråmal → kunde (K01, K03, BY-04).
- **D-Rapportkjoring:** Kontrolloppstilling og revisorutdrag er signerte kjøringer som ikke kan endres. Erstatningsmelding gir ny kjøring.
- **D-Oppdragsdokumentasjon:** Lenke til D-Avstemming per klient og periode for kvalitetskontrollen (GRFS 12). Lagring i 5 år fra fase 1.
- **MVP:** L-10 (lønnsjournal mot hovedbok) og L-11 (bank). L-02 eksakt mot camt.054. L-18/L-19 eksakte mot feriepengelisten. L-21 mot pensjonsgrunnlag (N16), L-22 mot K27 (N15). L-31 før utbetaling med fire øyne på endret bankkonto. L-01, L-12, L-15 på egen a-melding før innsending.
- **Salgsargument:** Finanstilsynet finner mangelfull avstemming av balansekontoer igjen og igjen (30 av 60 oppdrag i 2017; alle seks i et tilsyn for regnskapsåret 2024). Må bekreftes i intervjuer (N10, N30).

### Spørsmål til Peter og Sander
1. Kontrollene som én trait med `id`, `versjon`, `frekvens`, `datakrav` og en funksjon som gir D-Avstemmingslinje, så planleggeren hopper over kontroller uten data og samme katalog dekker fase 1 og MVP?
2. Toleranse som datatype (kroner, prosent, per inntektsmottaker, virkedager, «tidsforskjell som skal snu innen N perioder»). Hvordan følges en åpen tidsforskjell over flere måneder uten nye avvik hver gang?
3. Kalender for norske virkedager til L-02 og L-14: egen tabell eller crate?
4. Hash av rå A07-JSON og hovedbokuttrekk per kjøring, og diff mellom to signerte kjøringer: hvordan lagres den?
5. Kontrolloppstillingen fra samme rapportdefinisjon som skjermvisningen?
6. Gir Tripletex og PowerOffice bilagstype, bruker og opprettet-tidspunkt per postering (L-29)?

## N08 Rust-økosystemet

### Endringer i kartleggingen
- **A01–A06, T03, T04:** Anbefalt stack (natt/funn/N08.md §13): tokio, reqwest, axum, sqlx 0.9 med RLS, rust_decimal, quick-xml, calamine, Typst for PDF/A, wiremock/httpmock. CI: `cargo-deny` med lisensliste, `clippy -D warnings` med `disallowed-methods` for `Decimal::round`/`round_dp`, `sqlx prepare --check`. MSRV minst 1.94.
- **F-MYN-01 / M03 / M04:** Ingen Maskinporten- eller Altinn-klient i Rust, og ingen JWT-crate kan signere asynkront i KMS. Egen modul med `Rs256Signer` (KMS + lokal PEM i dev). `exp − iat` = 120 s (maks 180). Token-cache i moka. Skyvalget (H01) avgjør crate.
- **F-MYN-21 / M06 / D05 / D07:** Typer for avstemmingsrapporten genereres fra 1.0.2 med egne typer for `Beloep`, `BeloepSomHeltall`, `Desimaltall`, `DatoKlokkeslett`. Kall håndskrives. Ukjente felt fanges med `serde_ignored` og går til F-MYN-24. Rådata kryptert som `bytea` med hash; normalisert lag i tabeller med RLS.
- **F-MYN-24:** Skatteetatens RSS (`/rss/sbs/a-meldingen/`, `/rss/sbs/alle/`) pluss lenkediff og hash av regnearkene på SBS-siden.
- **F-MYN-10 / F-KJO-18:** calamine-import av regnearkene til D-Regelpakke med SHA-256 og gyldig fra.
- **F-MYN-38 / F-PER-24:** Ukentlig Klass-synk (145, 7, 426) til D-Kodeverk. Sak når 145 har koder som mangler i 426.
- **F-REG-29 / F-REG-30:** Adaptere som enum med nativ async og `BoxStream`. Tripletex-modeller for 85 av 3 007 skjemaer, med `number` → `Decimal` (2 096 beløpsfelt blir ellers `f64`). **SAF-T-leseren må tåle 1.30 og 1.40** (1.40 obligatorisk fra 1.1.2027), minimere (ingen kunde-/leverandør-id, ingen beskrivelsestekst) og kontrollere mot `NumberOfEntries`, `TotalDebit`, `TotalCredit`. Rettelse til N04: XSD-en har ikke eget ansattregister.
- **D02 / D03 / F-SIK-11:** `TenantTx` som eneste vei til databasen. `ENABLE` og `FORCE` RLS, applikasjonsrolle uten `BYPASSRLS`, visninger med `security_invoker`. Isolasjonstester med `#[sqlx::test]`.
- **D09 / F-SIK-19 / F-SIK-20:** AES-256-GCM på applikasjonsnivå med DEK per (tenant, dataklasse) og AAD. Blind indeks med HMAC-SHA256 og egen nøkkel. Ikke pgcrypto.
- **D08:** Registreringstid på alt via repolag. `WITHOUT OVERLAPS` (PG18) og `btree_gist` for gyldighetstid. Arbeidsforhold-ID som `text COLLATE "C"`.
- **A04 / M10 / F-BYR-15:** Egen kø med `aktiv_nokkel` (opplysningspliktig) og felles token-bøtte per (system, legitimasjon).
- **D05 / K03:** `brutto-penger` med avrundingsstrategi som data. AGA-toleranse med eksplisitt strategi, aldri `round()`.
- **F-RAP-03 / F-RAP-04:** Typst PDF/A-2b (3b med JSON-vedlegg), lås med to hasher. Excel med `rust_xlsxwriter`, CSV med `csv`.
- **MVP:** Lønnsslipp og lønnsjournal i Typst som PDF/A med veraPDF i CI. A-melding-XML med `quick-xml` og typer fra XSD (`xsd-parser`). XSD-validering med `xmllint`/Xerces i CI (ingen moden validator i ren Rust).

### Forslag til spikes (Peter og Sander)
1. Maskinporten-modul med KMS-signering mot `test.maskinporten.no`: svartid, feilkoder, `expires_in`.
2. `serde_json/arbitrary_precision` mot f64-stien, testet på opptak fra Tripletex, PowerOffice og ReAi. Se etter `flatten`/`untagged` i genererte modeller.
3. Jobbkø: egen kø mot `graphile_worker` og `apalis` 1.0. Krav: samtidighetsnøkkel, global bøtte, RLS, outbox.
4. typify/progenitor på Skatteetaten 1.0.2 og Tripletex-utdraget (85 skjemaer). Hva blir `date-time` og `allOf`?
5. SAF-T 1.30 og 1.40 med testfiler fra Tripletex `/saft/exportSAFT`: minne og tid på stor fil.
6. PDF/A-løp: Typst-mal, veraPDF i CI, PDF/A-2b eller 3b.
7. Sjekk at kodene i Skatteetatens regneark er lagret som tekst (ledende nuller). XSD-verktøy for CI. Lisenspolicy i `cargo-deny` (MPL-2.0, ISC, BSD-2).

### Spørsmål til Peter og Sander
1. Egen JWS (ca. 60 linjer) med KMS-signering, og `jsonwebtoken` bare for verifisering i tester?
2. Hvilken sky og KMS (H01)? Se N12.
3. `serde_json/arbitrary_precision` i hele workspace fra dag én (forbyr `flatten`/`untagged` på typer med tall), eller f64-stien med kontroll på 15 sifre?
4. Sjekke inn generert kode (egen crate per system) eller `build.rs`?
5. Enum-dispatch for regnskapsadapterne, eller `dyn` med `async-trait`?
6. Egen jobbkø (1–2 uker) eller `graphile_worker`? Hvordan deles token-bøtten mellom arbeidsnoder?
7. Rådata kryptert som `bytea` (kan ikke spørres med JSONB): kontroller bare på normalisert lag?
8. `clippy.toml` som forbyr `Decimal::round`/`round_dp`, og `clippy::float_arithmetic` i crate-ene for penger og regler?
9. MSRV-policy: siste stabile eller låst og kvartalsvis oppgradering?
10. Typst til all PDF, eller HTML→PDF (Gotenberg) for lik visning med frontend?

## N09 Open banking for lønnsutbetaling

### Endringer i kartleggingen
- **B01–B09 (fase1.json, bare forslag):** ZTL og Aritma er reelle kandidater. Neonomics har maks 20 mottakere per batch (kan brukes til trekk). Tink, Enable Banking, Token.io, TrueLayer og Yapily dokumenterer ikke norsk bedriftsbulk. Signering skjer i banken med BankID av personer med betalingsrett (flere signaturer støttes). Regnskapsfører kan signere hvis banken har gitt betalingsrett. Konsesjon ligger hos partneren; Brutto er teknisk leverandør. Bankfil må med som reserve.
- **P08:** Utbetaling holdes utenfor fase 1, men modellen låses nå. Fase 1 trenger ikke AIS.
- **F-BET-01/08/10/11/22 (kanalnøytral modell):** Ett D-Betalingsforslag ut gjennom adaptere `fil`, `betalingspartner` (ZTL), `multibank` (Aritma) og `regnskap_bankmodul` (PowerOffice). Utvid `D-Bankkonto.betalingskanal` og `D-Betalingsforslag.kanal` med `betalingspartner`.
- **F-KJO-23 / F-BET-06 / F-MYN-11 / G04 (to godkjenningslag):** (1) Brutto-godkjenning med fire øyne, step-up og hash av forslaget; (2) signering i banken med N signaturer og SCA. Hash av det som sendes skal være lik den godkjente. Endring nullstiller godkjenningen.
- **Ny entitet D-Banksignering:** `forslag_ref`, `kanal`, `ekstern_approval_id`, `signaturer_kreves`, `signaturer_mottatt`, `status` (Unsigned, PartlySigned, Accepted, Rejected), `signert_av_ref`.
- **Ny entitet D-Banksamtykke:** `bankkonto_ref`, `partner`, `consent_id`, `psu_corporate_id`, `gitt_av`, `gyldig_til` (180 dager), `status`, `fornyet_tid`. Knyttes til D-Fullmakt (bankfullmakt) for regnskapsfører (B04, F-BYR-27).
- **F-BET-13:** Statustabell som kobler partnerstatuser, ISO-statuser (RCVD, PATC, ACSP, ACSC, RJCT) og Bruttos statuser. `InProgress` hos ZTL er ikke bevis for betalt lønn.
- **Datakrav før MVP:** debetkonto (BBAN) og BIC, orgnr, mottakers navn og kontonummer (kryptert, S #6), mottakers adresse (SpareBank 1 krever i bulk), KID per trekk (D-KID), `EndToEndId` ≤ 35 tegn, utførelsesdato, formålskode SALA (netto) / SUPP (trekk).
- **D-Person.adressebeskyttelse:** Fortrolig adresse skal ikke sendes til bank eller partner [verifiseres hva som brukes i stedet].
- **F-BET-02:** Kanalens frister i forfallskalenderen (ZTL kl. 11.00). Én lønnsbetaling per utbetalingsdato.
- **S #15 / X05:** Agenter har ingen tilgang til samtykke, signering eller betaling. Håndheves i tilgangskontrollen.
- **MVP:** pain.001.001.09 etter Bits MIG 2.0 (reserve .03), SALA på netto, trekk i egne `PmtInf` med SUPP. Import av pain.002 og camt.054D. ZTL som første partner etter sjekk av tillatelse og konkursrisiko, og med tydelig kundeavtale om klientkonto. Nordea Corporate og utenlandsk konto via fil. AGA betales bare etter avstemming (S #22), bevisst avvik fra ReAi. Den som forberedte kjøringen kan ikke godkjenne (BY-34).

### Handling (gjøres av et menneske)
- Ta kontakt med ZTL om partnervilkår, onboarding av kunde (kundekontroll, BankID etter signaturrett) og rolle i databehandleravtalen.
- Juridisk vurdering av om unntaket for teknisk tjenesteleverandør gjelder for Brutto (se N17).

### Spørsmål til Peter og Sander
1. ZTLs modell med lønn via klientkonto, eller krav om direkte betaling fra kundens konto (da blir Aritma eller fil hovedvei)?
2. Fra Brutto-godkjenning rett til bankens signering i samme økt, eller eget steg med varsel?
3. Hvordan vises `PartlySigned`, og hvem får lenken til signatar nummer to?
4. Trekk og AGA automatisk etter godkjent a-melding (ReAi-modellen), eller alltid ny godkjenning?
5. Regnskapsfører kan signere i banken der banken tillater det, eller kunden alltid selv?
6. Betalingsadapter mot regnskapssystemer (PowerOffice), eller bare fil og partner?

## N10 Godkjenningsflyt for lønn

### Endringer i kartleggingen
- **G01–G07 (fase1.json, bare forslag):** G01 «begge»: maler M1–M5 som kan justeres per kunde. G04: arbeidsdeling i policymodulen (I04), gjelder uansett mal. G06: godkjenning bindes til hash. G07: én motor, tatt i bruk i fase 1 på avstemmingspakken (F-REG-27) og kvittering av kontrollsaker.
- **F-SIK-05 / F-SIK-06 / D-Rolletildeling:** Hele rollekatalogen nå, også KUNDEGODKJENNER, BYRA_KONTROLLOR og BETALINGSFULLMEKTIG. I02: legg til kontrollør og kundegodkjenner.
- **F-BYR-02 / D-Klient:** Ved oppstart fylles hvem som godkjenner, betaler og sender, risikonivå, kontrollkrav og bankfrist. Nye felt `godkjenningsmal` og `godkjenningskanal_i_dag`.
- **F-BYR-11 / D-Fullmakt:** Nye felt `betalingstyper` og `kan_delegeres`. `bankkonto_id` påkrevd for bankfullmakt (Finanstilsynet 2018).
- **D-Godkjenning / D-Godkjenningsregel:** Nye objekttyper og oppgavetyper (AVSTEMMING, LONNSKJORING, BETALINGSFORSLAG m.fl.) og feltet `ledd`. Dagens modell dekker bare timer, fravær og utlegg.
- **F-SIK-12 / D-Arbeidsdelingsregel:** FORBEREDE_GODKJENNE i drift på avstemmingen i fase 1. Unntak for små byråer med kompenserende kontroll (F-SIK-13).
- **F-SIK-15 / F-SIK-03:** Logg godkjenning og avvisning med step-up, rolle og objekt-hash.
- **F-KJO-23/24, F-BET-06, F-BYR-24/26/27 (ADR):** Frys tilstandsmaskinen (natt/funn/N10.md §6.2). `D-Lonnskjoring.status` blir hovedstatus (UTKAST, BEREGNET, KONTROLLERT, TIL_GODKJENNING, GODKJENT, FULLFØRT, FORKASTET) med tre nye spor: `betalingsstatus`, `ameldingstatus`, `bokforingsstatus`.
- **MVP:** Slå sammen D-Kundegodkjenning og D-Kjoringsgodkjenning til én tabell (`ledd = kunde`). Kundegodkjenning på mobil med `sammendrag_hash` og endringsvisning. Betalingsforslag først ved GODKJENT. A-melding sendes som standard når betalingen er signert. Bilag som utkast til regnskapsfører for byråklienter. Korreksjon i stedet for gjenåpning. Frister fra bankfristen. Kvalitetsnøkkeltall: rettet etter godkjenning < 2 %, godkjent i tide > 90 %.
- **Salgsargument:** «Godkjenning, betaling og a-melding er adskilte steg med hash», mot PowerOffice, ReAi og Intect (ett klikk sender alt) og Tripletex (valgfri lønnsgodkjenning).

### Handling (gjøres av et menneske)
- Gjennomfør intervjuene i natt/funn/N10.md §7 (12 spørsmål, L-kontrolltabell) med 2–3 byråer før MVP-planen låses.
- Be om demo eller brukerdokumentasjon via partnerbyrå for Visma Payroll (AutoPay, bekreft levering, endring etter betaling), SD Worx (godkjenning og remittering), PowerOffice Go (hvem kan godkjenne, arbeidsdeling), Intect Norge og Xledger.

### Spørsmål til Peter og Sander
1. Hovedstatus pluss tre parallelle spor (betaling, a-melding, bokføring), eller én lineær status?
2. Én godkjenningstabell for alle objekter (D-Godkjenning med objekttype og ledd), eller egne tabeller?
3. Hva hashes (`resultat_hash`, `sammendrag_hash`, betalingsforslag, a-meldingens nyttelast), og hvordan sikres kanonisk serialisering i Rust?
4. Ledd og betingelser som data (JSON i D-Godkjenningsregel), og arbeidsdeling som kode i policymodulen?
5. Kanal for kundegodkjenning i MVP (e-post, SMS, push), og magisk lenke sammen med step-up?
6. Bankens avskjæringstid på D-Klient eller D-Bankkonto?
7. Bruke godkjenningsmotoren allerede i fase 1 på avstemmingspakken? Forslaget er ja.

## N11 Konkurrentenes A07-avstemming og lønnskontroller

### Endringer i kartleggingen
- **F-REG-30 / F-MYN-21 / F-BYR-15 (hovedargument):** Maskinell A07-henting for alle klienter uten innlogging, med ny henting når `innsendinger[]` endres. Tripletex, PowerOffice og Fiken avstemmer mot hovedboken, men bare i eget økosystem og med innlogging for hver henting. Demo: «alle klienter avstemt i natt».
- **F-REG-30:** Ikke krev at betalingen er ført i lønnsmodulen. Finn betalinger på 2600, 2610 og 2770 ut fra dato, beløp og bilagstype. Manuelt førte betalinger blir forklart tidsforskjell eller kobling, ikke avvik.
- **F-REG-27 / D-Avstemming:** Statusflyt minst som Tripletex (avstemt, kontroll bedt om, kontrollert, én av flere kontrollører holder) pluss `gjenaapnet` med årsak når A07 endres etter kontroll (L-24). Ta vare på alle versjoner (PowerOffice sletter forrige utkast).
- **F-BYR-12 / F-BYR-13 / F-RAP-07:** Klientoversikt med kolonner per kontrollgruppe og termin, med alle klienter uansett regnskapssystem.
- **N07 første utgave:** Legg til L-03 (utleggstrekk mot 2610–2620; bare Tripletex har det) og deretter L-16 (AGA-sone mot adresse; ingen har det).
- **F-RAP-15 / F-RAP-19:** Kontrolloppstillingen (L-17) må finnes i fase 1. Tripletex og Periode & År har den.
- **F-PER-35 / F-MYN-42:** Kontroller per person er en differensiator.
- **N40 / D-Integrasjon:** Konkurranseklausul-risikoen (T2) oppgraderes til «middels til høy» i fase 1, fordi Tripletex og PowerOffice selger egne avstemmingsmoduler. I henvendelsen: vis til godkjente tredjeparts avstemmingsverktøy som leser lønnskontoer (Accountflow, Account Control, Sticos Oversikt, Periode & År, Maestro). Søk om lesing for avstemming (fase 1) og lønnsbilag (MVP) hver for seg.
- **F-REG-29:** SAF-T-opplasting som første kilde blir viktigere, fordi den dekker kunder med lønn og regnskap i ulike systemer.
- **F-BYR-33 (prising):** Generelle avstemmingsverktøy koster 15–87 kr per klient per måned. Accountflow er nærmeste konkurrent til fase 1.
- **F-TRK-17 / F-MYN-28 (MVP):** Trekkpålegg-API er standard hos Tripletex, PowerOffice, Fiken og Finago. Må med i første lønnsversjon.
- **F-MYN-40 (flyttes til MVP):** Krav og betalinger. Tripletex viser det allerede. Gjør L-02 og L-14 eksakte uten bankdata.
- **F-REG-17/18/19 (MVP):** Planlegg filimport (GBAT10/lønnsimport i Tripletex, lønnsjournal i PowerOffice) som reserve før lønnskjøring går live for Tripletex- og PowerOffice-kunder.
- **F-REG-25 / L-24 (MVP):** «A-melding historikk» med diff, som Visma.net.
- **F-KJO-20 (MVP):** Sperre ved alvorlige avvik før innsending (som NettLønns terminrapport).
- **F-MIG-06:** ReAi rapporterer ikke utleggstrekk. Ved migrering hentes utleggstrekk alltid på nytt.
- **F-SIK-32 (Senere):** Intect har ISAE 3000/3402-erklæring. Byråer vil spørre.

### Handling (gjøres av et menneske)
- Ta med i advokatvurderingen (N40): gjelder T2 i Tripletex' vilkår funksjoner Tripletex selger som tillegg, for eksempel Avstemming?
- Spør salg hos Tripletex og PowerOffice om pris på Avstemming og Quality per klient (prisanker).
- Spør NettLønn og Caspeco om de har skriftlige tillegg til vilkårene hos PowerOffice og Tripletex for lønnsbilag.
- Avklar SD Worx' A07-avstemming, trekk-API og regnskapsintegrasjon i kundeintervju eller demo.
- Spør ReAi hvilken standardkonto som brukes for `counterAccountNumber` på faste trekk etter skatt.

### Spørsmål til Peter og Sander
1. Kobling av betalinger på 2600, 2610 og 2770 uten lønnsmodul (dato, beløp, bilagstype, KID i tekst): hvor robust er det på posteringer fra Tripletex og PowerOffice?
2. Kan jobbkøen hente A07 for 500 klienter hver natt innenfor kvoten og regelen om én bestilling per opplysningspliktig, og hente på nytt ved erstatningsmelding?
3. Statusmodell med én av N kontrollører, gjenåpning ved ny A07-versjon og signerte versjoner: passer det i D-Avstemming og D-Rapportkjoring?
4. Lese avstemmingsstatusen i Tripletex (hvis API-et har den), eller bevisst holde seg unna for å ikke overlappe med T2?
5. Krav og betalinger i MVP: scope og rolle, og passer det med systembrukeren for klientsystem fra N40?
6. Eksportformat for kontrolloppstillingen til Maestro og Periode & År? (Sendt til N24.)

## N12 Assistenten, Claude i EU, sky og KMS i Norge

### Endringer i kartleggingen
- **Fase 1:** Ingen KI i produksjon og ingen MCP mot kundedata (S #11, B13, N40). Kodeagenter får ikke tilgang til produksjonsdata (F-SIK-31, D-48).
- **H01 (F-SIK-20, F-SIK-25, F-MYN-01, D09, H06):** Azure Norway East. Key Vault Premium for `Rs256Signer` og KEK i fase 1 (Managed HSM ca. 2 300 USD/mnd, senere). PG Flexible PG18 med `btree_gist` og innebygd PgBouncer, ikke Burstable. Geo-backup til Norway West ved opprettelse (bestill tilgang nå). Reserve: Aiven på `azure-norway-east`. Google og AWS har ingen region i Norge.
- **Ny F-id: dataklasse per felt:** Hvert felt i API-svar får `x-dataklasse` i OpenAPI (utoipa) med kodene fra `D-Rolledefinisjon.dataklasser`. CI feiler ved manglende klasse. Felt fra integrasjoner merkes `x-uklarert`.
- **F-PLA-32 / F-SIK-05 / F-SIK-03 / I02:** `aktor_type = agent` og listen over forbudte handlinger implementeres og testes i fase 1, én test per forbudt handling.
- **F-SIK-15 / F-SIK-17 / D10 / H05:** D-Revisjonslogg `kanal` får `assistent`. D-KI-kall defineres, men fylles ikke. D-Lagringssted får rad for KI-logg i Norge.
- **D-Abonnement / D-Integrasjon / F-PLA-09:** Nye felt `ki_datanivaa` (0–3), `ki_samtykke_versjon`, `ki_samtykke_av`, `ki_samtykke_tid`, `ki_underleverandor_id`, alt av som standard. `D-Integrasjon.ki_samtykke` per kildesystem. Byrået kan ikke samtykke for kunden uten at databehandleravtalen sier det.
- **F-SIK-27 / F-SIK-28 / H08:** DPA og kundeavtale nevner KI som valgfri underleverandør (av til kunden slår på, 30 dagers varsel). DPIA-mal med KI-tillegg. D-Underleverandor får `inferensprofil`, `leverandor_oppbevaring_dager`, `menneskelig_gjennomgang_mulig`.
- **F-KJO-16 / D-Avvik / X04:** Nye felt `forklaringskode` og `parametere` (json), så mal og modell kan forklare avvik uten fritekst.
- **X01:** Svar skiller id-er og koder fra visningstekst. Fødselsnummer aldri i id-er eller URL-er.
- **Visning:** KI-svar senere som ren tekst uten eksterne bilder og lenker (CSP `img-src 'self'`).
- **MVP:** Agenter har aldri rett til å godkjenne, sende eller utbetale. Sykelønnsarter og fagforeningstrekk merkes `helse` og `fagforening`. F-MIG-13 (KI-mapping av lønnsarter) er første kandidat: kode, navn og flagg, aldri beløp, med samtykke. KI-gateway med «null-leverandør» for testing uten modell.
- **Senere:** Modell via AWS Bedrock EU-profil (`eu.anthropic.claude-*-5-5`, Haiku 5.5 og Sonnet 5.5). Fable 5.1 passer ikke for lønnsdata (ingen EU-profil, 30 dagers lagring med mulig menneskelig gjennomgang). Anthropics API har bare `us`/`global`; Microsoft Foundry bare Global/US. Vurder på nytt hvert halvår. AI Act: ikke høyrisiko så lenge assistenten forklarer, søker og rapporterer; blir det ved rangering eller profilering av enkeltansatte.

### Forslag til spikes (Peter og Sander)
1. H01-test: `max_prepared_statements` på Azures innebygde PgBouncer og sqlx 0.9 med navngitte preparerte setninger i transaksjonsmodus. Tilgang til Norway West. Hva betyr stjernen ved Norway East for PG Flexible?
2. Key Vault Premium mot Managed HSM: pris, FIPS-nivå, RS256 for Maskinporten, grenser for nøkkeloperasjoner.
3. Senere: Bedrock-sandkasse fra `eu-north-1` med syntetiske data (krever konto).

### Spørsmål til Peter og Sander
1. `x-dataklasse` og `x-uklarert` på hvert felt i OpenAPI med CI-sjekk allerede i fase 1?
2. Agentgrensene testet i fase 1 selv om ingen agent finnes?
3. KI-gateway som egen deploy-enhet med egen utgående trafikk, eller modul i monolitten? Forslaget er egen enhet.
4. Azure for data og AWS Bedrock for modellen, eller Google `eu`, eller vente på Claude i Azure EU?
5. Key Vault Premium eller Managed HSM i fase 1? Azure PG Flexible eller Aiven?
6. KI-svar som ren tekst uten lenker og bilder?

## N24 Kontrolloppstillingen

### Endringer i kartleggingen
- **F-RAP-15 / L-17 (ny funksjon «Kontrolloppstilling etter § 7-2-11 med signering»):** Arbeidspapir og eksport, ikke innsending. Brutto kan ikke levere bare kontrolloppstillingen; API-et tar én konvolutt med hele skattemeldingen og næringsspesifikasjonen, og det er årsoppgjørsverktøyet som leverer. Linjene følger `LoennsOgPensjonskostnad` i XSD v4–v7 (uendret 2023–2026). Avstemmes mot A07, og hver differanse peker til D-Avstemmingslinje.
- **D-Rapportdefinisjon:** `kontrolloppstilling_ns_v7` med mapping per inntektsår. **D-Rapportkjoring:** signert av arbeidsgiver eller byrå, kan ikke endres.
- **F-RAP-04:** Eksport i xlsx/CSV med Skatteetatens feltnavn, PDF/A, og XML-fragment `spesifikasjonAvLoennsOgPensjonskostnad` validert mot offisiell XSD.
- **Overføringsark per verktøy:** Tripletex (Bokført, Tillegg, Fradrag, naturalytelser uten fortegn), Maestro (postene 100, 111, 112), Periode & År (tilleggslinje med type). Brutto gir de tre tallene verktøyene ikke regner selv: kredit på 5290, innbetalt pensjonspremie, tillegg og fradrag per påløpskonto. Maestro og Periode & År tar ikke imot ferdige lønnstall i dag.
- **Kontoutvalg:** Minst Tripletex' intervaller (5000–5289, 5300–5399, 5500–5599, 5800–5809, 5940–5949, 7100–7159), pluss 5290 (kredit) og 2930–2949 (IB/UB), via reglene i N23. Vis uttrekkstidspunkt og hash av saldobalansen.
- **Ikke** bygg innsending til Skatteetaten. Fase 1 trenger ikke `skatteetaten:formueinntekt/skattemelding`.
- **F-RAP-19 (revisorutdrag):** kontrolloppstilling med forklarte differanser, rå A07 med hash, termin og betalingsdato for trekk, naturalytelser med kvitteringer, regelsett med versjon, utkast til ledelsens uttalelse. Revisor signerer i Altinn (per element). Etter SA 3801 signerer revisor ikke ved avstemmingsdifferanser av betydning.
- **F-REG-30 / F-REG-27 / L-30:** Reglene L-30a–i (natt/funn/N24.md §6). Terskler i D-Kontrolloppsett. Satser (4 392 kr, 370 300 kr) i D-Regelpakke med gyldighetsår. L-30a, b, f og g først.
- **F-REG-29:** Lesingen må også gi bevegelse på 6440, 6900–6909, 7000–7090, 5900–5905, 5920–5930, 5250–5280, kredit på 5290 og saldo på 1230–1239.
- **D-Virksomhet:** Nye felt `revisjonsplikt` (styrer revisorutdrag; revisor fra rollen REVI i Enhetsregisteret) og `foretakskategori` (mikro, små, mellomstore, store etter rskl. § 1-5).
- **F-RAP-22 / L-27:** Årsverk fra A07 er notegrunnlag etter rskl. § 7-43 og § 7-30. Definisjonen publiseres i rapporten.
- **F-ORL-13 / F-RAP-17:** Små foretak har ikke plikt etter § 7-31 (fjern [verifiseres]). For andre lages grunnlag med lønn, naturalytelser og styrehonorar per rolle fra A07 og Enhetsregisteret.
- **F-SIK-09:** Revisortilgang i Brutto for å lese pakken.
- **MVP:** Kontrolloppstillingen fylles fra lønnsjournalen. L-30c, d og h blir eksakte via D-Fordelsavtale. Innbetalt pensjonspremie fra F-PEN-05/06.
- **Senere:** Tilby Sticos (Periode & År), Maestro, Tripletex og Wolters Kluwer import av kontrolloppstillingen (API eller XML-fragment). Ikke bygg Brutto som årsoppgjørsverktøy.

### Handling (gjøres av et menneske)
- Spør Fiken skriftlig om `spesifikasjonAvLoennsOgPensjonskostnad` fylles automatisk for AS.
- Senere: spør Sticos og Maestro om de vil ta imot kontrolloppstillingen fra et lønnssystem.

### Spørsmål til Sjur
- Hvordan regnes årsverk i noten (timelønnede, tilkallingsvikarer, permitterte, sluttere) etter god regnskapsskikk?

### Spørsmål til Peter og Sander
1. Rust-typer for kontrolloppstillingen: generert fra XSD v7 eller serde-structs med versjonert enum per inntektsår?
2. XML-fragmentet validert mot offisiell XSD i CI (xmllint), med nedlasting per inntektsår?
3. Avrunding per linje eller bare summen (K03)? XSD tillater to desimaler.
4. Signert PDF/A med uttrekkstidspunkt og hash for både A07 og saldobalansen?
5. Terskler i L-30 som data med arv; kvitteringer for negativ bekreftelse per år, gjenåpnet av hendelser?
6. Notegrunnlag for § 7-31 med lønn per person for daglig leder og styret: step-up og egen rettighet?

## N25 Tilgang i MVP

### Endringer i kartleggingen
- **F-MYN-01:** Legg `krav-og-utlegg`, `regnskapsforer-uten-signeringsrettighet` og enkeltrettigheter for de fire migrerte ressursene inn i systemregistreringen nå. Forespørslene i fase 1 ber bare om det som trengs [verifiseres at delmengde er mulig].
- **F-MYN-02 / F-MYN-04:** Ingen endring i fase 1. `regnskapsforer-uten-signeringsrettighet` ikke i fase 1-systembrukeren til byrået.
- **F-REG-30 / F-REG-27:** Betalingskontroll i fase 1 bruker bank, regnskap (2600, 2770) og `innbetalingsinformasjon` fra A03. Krav og betalinger krever at kunden sender a-melding via Brutto.
- **Retting i N06:** Krav og betalinger bestilles via brukerstøtten. `altinn:events.subscribe` er offentlig og trenger ikke bestilles. **Retting i N11:** F-MYN-40 i MVP gjelder bare kunder som sender a-melding via Brutto.
- **Tilgangsregister (ny F-id fra N06):** Tjenestebeskrivelse for Krav og betalinger, grenser for delings-API (5 kall/s, 10 000/time), Correspondence-scope.
- **F-MYN-40 (MVP, «Kan» → «Bør» for lønnskunder):** Scope `skatteetaten:kravogbetalinger`, rettighetspakke `regnskapssystem`. Direktekunde gir `krav-og-utlegg`; byrå trenger `regnskapsforer-uten-signeringsrettighet` eller `-med-`. Hent åpne krav daglig og krav og innbetalinger etter hvert forfall. Hviteliste over kravtyper (forskuddstrekk, AGA, utleggstrekk skatt, tvangsmulkt, renter); MVA og restskatt lagres ikke. `KB-007` = ingen data.
- **Nye D-id-er (MVP):** D-Skattekrav (`kravidentifikator`, `kravtype`, `kravgruppe`, `kravperiode`, `forfallsdato`, `opprinneligBeloep`, `gjenstaaendeBeloep`, `kid`, `hentet_tid`, `raa_json_ref`) og D-Skatteinnbetaling (`innbetalingsidentifikator`, `innbetalingsdato`, `innbetaltBeloep`, `uplassertBeloep`, `innbetalt_fra_kid`, plasseringer). Kobles til D-KID (nytt felt `kontroll_mot_krav`), D-Betalingslinje og D-Avstemmingslinje.
- **MYN-18 / L-02 / L-14:** Bruker Krav og betalinger når tilgang finnes. Uplasserte innbetalinger blir egne saker.
- **F-MYN-03:** Endringsforespørselen som legger til `lonn` tar også med `krav-og-utlegg`.
- **F-MYN-04 / F-BYR-07 / F-BYR-09:** Egen agent-systembruker for Krav og betalinger med `regnskapsforer-uten-signeringsrettighet` (en eksisterende agent-systembruker kan ikke endres). D-Systembruker `pakkesett` får `krav_og_betalinger`.
- **F-MYN-15:** Events per klient og ressurs bare for klienter der Brutto sender a-melding. Dialogporten-polling (F-MYN-43) er grunnmuren. Ikke `typeFilter`.
- **D-Myndighetsabonnement:** Én rad per (klient, ressurs) med `altinn_subscription_id`, `resourceFilter`, `subjectFilter`, nytt felt `validert`. F-MYN-06: helsesjekk sletter abonnement når klienttilknytningen opphører.
- **F-MIG-25 / F-TRK-19 / F-MIG-17 / F-MIG-11:** Leser for Altinn Correspondence (`altinn:correspondence.read`) som henter migrerte trekkbrev og historiske A03 ved oppstart. Bare søk og oversikt (status «Hentet», ikke «Lest»). Aldri `/content` eller `/markasread`. Byrå bruker `regnskapsforer-lonn`; direktekunder enkeltrettigheter [verifiseres]. Ellers opplasting.
- **F-MYN-14 / F-MYN-22:** Portveien «Brutto sender a-meldingen» strykes fra MVP (ansvar hos opplysningspliktig, fare for dobbel rapportering, ingen dokumentert XML-eksport hos Tripletex/PowerOffice, passer ikke formålet). Saksregelen «flere innsendere for samme måned» fanger dobbel innsending ved systembytte.

### Handling (gjøres av et menneske)
- Utvid henvendelsen til Skatteetaten (N26 §8) med: Kan kontrollkunder og byråklienter som sender a-melding fra et annet system, få Krav og betalinger til avstemming? Gjelder pilotbegrensningen for Krav og betalinger fortsatt? Be om offentlige kodelister for `kravgruppe` og `innbetalingstype`.
- Spør Digdir (Slack produkt-dialogporten eller servicedesk@altinn.no) om skala for Events: hvor mange abonnement per konsument, og anbefales polling av Dialogporten for agent-systembrukere?

### Spørsmål til Peter og Sander
1. Krav og betalinger i MVP bare for kunder som sender a-melding via Brutto, og bank + A03 for kontrollkunder?
2. Egen agent-systembruker for Krav og betalinger, eller én ny felles systembruker i MVP med begge pakker? Begge krever ny klientdelegering.
3. Polling av Dialogporten for alle, og Events bare for egne innsendinger?
4. Filtrere bort kravtyper som ikke gjelder lønn ved henting, ikke etterpå?
5. Stryke portveien fra MVP?
6. Leser for migrerte trekkbrev og A03 i MVP, eller manuell opplasting ved oppstart?

## N28 Samordnet utleggstrekk i detalj

### Endringer i kartleggingen
- **F-MYN-42 (T9-grov i fase 1):** Per person og måned fra A07: U = sum `utleggstrekkSamordnet`, K = sum inntekt med `fordel = kontantytelse`. Avvik når U > K, U finnes og K = 0, U/K ikke rundt men U/(kontant + natural + utgift) er det (feil grunnlag), eller U/K endres uten ny versjon i registeret. Med kjent prosent: forventet = p × K, ±1 kr per utbetalingsdato. Merkes «indikasjon», ikke «feil».
- **T1 (N01) rettes:** Sammenlign `datoForUtleggstrekk`, ikke bare måned. `utleggstrekkSkatt` før første samordnede dato i samme måned er lovlig.
- **D-Trekkpalegg:** Perioder som liste. `regelverk` får egen grunnlagsregel (samordnet = kontant; gammelt skattetrekk = som forskuddstrekk). Enum `paleggsgiver`: `namsmann` → `namsfogd` (innkrevingsloven § 28 fra 1.7.2026).
- **D-Regelpakke:** Grunnlagsregler for utleggstrekk som versjonert kode med virkningsdato, og datoen 1.1.2027 for renter.
- **F-PER-35:** Trekkoversikt med kode, beløp, dato og implisitt prosent, bak lønnstilgang.
- **Produkttekst:** Utenfor Nord-Norge er samordnet trekk sjeldent i dag (fra 1.11.2026 gjelder nytt regelverk bare skyldnere i Nord-Norge uten bidragsgjeld og uten løpende gamle trekk, unntatt Alta og Målselv). Kontrolltekster må ikke anta at alle trekk er samordnet.
- **Kildeovervåking:** Følg utrullingsforskriften (FOR-2025-12-12-2508), som endres hver eller annenhver måned, med manuell sjekk ved hver endring.
- **F-TRK-20 (MVP) som algoritme:** Per ansatt og utbetalingsdato: siste versjon og periode; K = lønnslinjer i grunnlaget; tak = K − forskuddstrekk (≥ 0); prosent: U = min(gulv(p × K), tak); beløp: U = min(restbeløp i måneden, tak), standard «så tidlig som mulig»; ingen fremføring. Heltall i øre (i64), avrunding til hele kroner til slutt.
- **D-Lonnsart / F-LON-02:** Nytt flagg `inngar_i_utleggstrekkgrunnlag` (standard fra `fordel = kontantytelse`, overstyring med fire øyne).
- **D-Trekkpalegg → ny barnetabell D-Trekkperiode** (startdato, sluttdato, beløp eller prosent). D-Lonnslinje lagrer `trekkid`, `trekkversjon` og brukt periode.
- **F-TRK-18:** Gamle trekk sperres fra første samordnede startdato. Begge typer på samme utbetaling = hard sperre i F-KJO-20. Nytt gammelt brev etter samordnet trekk = sak. `avsluttet_arsak = erstattet_av_samordnet` settes automatisk og bekreftes av menneske.
- **F-TRK-21 / F-MYN-29:** Ingen melding for samordnet trekk; riktig sluttdato og fravær i a-meldingen holder (innkrevingsloven § 30 fjerde ledd).
- **F-TRK-26/27/28:** Samordnet trekk har ingen vernet beholdning hos arbeidsgiver, ingen saldo og ingen fremføring. Netto kan gå til 0.
- **F-TRK-22 / F-BET-01 / F-BET-05 / D-KID:** Samordnet: én betalingslinje per person per utbetaling til 7694 05 69814 med KID fra pålegget, frist første virkedag etter. Gammelt skattetrekk: én samlet linje med termin-KID kravtype 03 til 7694 05 24802. Bidrag: konto fra brevet.
- **A-melding:** Én `utleggstrekk`-forekomst per person, kode og utbetalingsdato, negativt beløp per person, positiv `sumUtleggstrekk`. Valider F294, F295, F528 før innsending. A-meldingen har ikke KID.
- **F-MYN-28 / F-KJO-24:** Hent daglig, rett før beregning og rett før godkjenning. Ny versjon etter godkjenning = varsel.
- **Testsuite:** K1–K44 som egenskaps- og gylne tester; eksemplene A–D som fixtures. **F-RAP-12:** Vis grunnlag, prosent, beløp, tak og periode per utbetaling.

### Handling (gjøres av et menneske, tas med i henvendelsen til fremtidensinnkreving@skatteetaten.no)
- Avrunding av prosenttrekk (ned, nærmeste krone, ingen)? To beløpsperioder i samme måned med flere utbetalinger? Grensetilfeller i grunnlaget (trekkpliktig del av utgiftsgodtgjørelser, skattefrie kontantytelser, negative kontantlinjer, pensjonsegenandel før tak)? Hvordan formidles kombinert beløp og prosent (FOR-2025-07-09-1507 § 1 c) i API-et? Egen `trekkid` og KID per trekkpliktig og underenhet? Godtas én samlet a-meldingsforekomst per person og måned? Når oppheves bokstav e for bidrag, og hva betyr «PAK»?

### Spørsmål til Peter og Sander
1. `inngar_i_utleggstrekkgrunnlag` utledet av `fordel`, eller eget flagg med fire øyne?
2. D-Trekkperiode som egen tabell med bitemporal historikk, eller JSON på D-Trekkpalegg?
3. Heltall i øre (i64) i trekkmotoren og avrunding ned til hel krone som foreløpig regel?
4. Fordeling av beløpstrekk ved flere utbetalinger: «så tidlig som mulig» eller forholdsmessig? Kundevalg?
5. Hard sperre når samordnet og gammelt trekk treffer samme utbetaling, selv kort før utbetaling?
6. Er T9-grov verdt det i fase 1 når den bare gir «indikasjon»? Vises til byråer først?
7. Overvåking av regelkilder: manuell ukentlig sjekk eller lite verktøy som varsler?

## N30 Dokumentasjonsmodellen for lønn

### Endringer i kartleggingen
- **ADR: modell A som standard:** Samlebilag per kjøring i regnskapet og full § 5-6-journal i Brutto holder etter NBS 2 («Kontrollsporet») punkt 4.7 (lønnssystem som forsystem). Brutto blir del av kundens regnskapssystem (punkt 4.5: 3,5 års elektronisk tilgjengelighet og SAF-T) bare hvis noe en pliktig spesifikasjon krever finnes bare i Brutto, typisk AGA per sone og sats som ikke står i bilaget, eller ett bilag for flere kjøringer. Unntaket for kunder under 5 mill. kr i omsetning faller bort 1.1.2027. Lås feltene i N30 §6.3 på D-Bilag, D-Postering og D-Regnskapsoppsett nå.
- **Hjemler rettes:** Forskriften § 13-5 finnes ikke; § 7-1 og § 4-1 gjelder noe annet. Riktige hjemler i natt/funn/N30.md.
- **F-REG-27 / F-REG-30 / F-RAP-15 / F-SIK-26 (fase 1):** Avstemmingspakker og kontrolloppstilling er dokumentasjon av balansen og kontrollsporet. D-Oppbevaringsregel 60 måneder, med i eksporten ved opphør allerede i fase 1.
- **F-SIK-29 (lett versjon i fase 1):** Systembeskrivelse per programversjon (kilder, kontrollkatalog-versjon, toleranser, regelsett), inn i revisorutdraget.
- **F-SIK-25 / D-Lagringssted:** Alt regnskapsmateriale i Norge. Kartlegg underleverandører for logg, feilsporing og e-post som kan inneholde lønnsdata (meldeplikt etter § 7-5).
- **D-Fullmakt:** Nytt felt `vilkaar` for AVTALT_GODKJENNING_UTEN_KUNDE. Forhåndsgodkjenning bare som skriftlig og avgrenset fullmakt (ingen klausul om taus aksept funnet i offentlige standardvilkår).
- **F-REG-05 / F-REG-17 (MVP):** Ett bilag per kjøring, AGA-linjer per (sone, sats) med grunnlag påkrevd. Ett bilag for flere kjøringer bare i modell B.
- **F-REG-06 / F-RAP-09 (MVP):** Journal låst med hash. Bokføringsgrunnlaget viser til journalens id og hash.
- **F-REG-18/19/22 (MVP):** Adapterne skriver regnskapets bilagsnummer tilbake; status BOKFØRT først da. L-10 avstemmer journal mot hovedbok.
- **Ny funksjon «Kontrollsporbeskrivelse per kunde og år» (MVP):** Generert fra D-Regnskapsoppsett, D-Kontomapping og D-Programversjon, årsmerket, ny full versjon ved vesentlig endring.
- **F-SIK-26 / F-BYR-30 (MVP):** Exit-pakke med utvidet `D-Eksportpakke.innhold` (journal, bokføringsgrunnlag, betalingsdokumentasjon, systembeskrivelse, kontrollsporbeskrivelse, bilagsnumre uendret). Sletting bare etter kvittering for mottak. Arkivabonnement (`D-Abonnement.status = arkiv`).
- **F-BYR-24/26, F-KJO-23, F-BET-06 (MVP):** «Godkjenn og signer» = én handling med to bevis: godkjenning i Brutto med hash, deretter SCA i banken [advokatvurdering]. `kanal = BANK_SIGNERING` bare sammen med PORTAL, aldri i M4. Lagre `betalingsfil_hash` og bankens status.
- **F-REG-26 / F-BET-17 / F-BET-22 (MVP):** Returfiler (camt.054, pain.002) lagres som betalingsdokumentasjon i 5 år og tas med i eksporten.
- **F-RAP-19 (MVP):** Revisorpakken får kontrollsporrapport, systembeskrivelse, kontrollsporbeskrivelse og godkjenningsbevis.
- **Modell B som valg:** SAF-T-delfil per regnskapsår og 42 måneder elektronisk tilgjengelighet. Bygges bare hvis intervjuene eller kundene krever det.

### Handling (gjøres av et menneske)
- Bestill advokatvurdering (N30 §4.6) av SCA som attestasjon, «Godkjenn og signer», forhåndsgodkjenning og sletting ved opphør, før malene M1 og M3 designes ferdig. Kan slås sammen med advokatvurderingen fra N40.
- Gjennomfør revisorintervjuene med guiden i N30 §5 (13 spørsmål), sammen med byråintervjuene fra N10.
- Be et medlemsbyrå vise vedleggene «Betalingsoppdrag» og «Bruk av IT-systemer i fellesskap» i Regnskap Norges KS Komplett.

### Spørsmål til Peter og Sander
1. `dokumentasjonsmodell` som policy på D-Regnskapsoppsett som styrer validering av bilag, oppbevaring og eksport: hvor ligger policyen i koden?
2. Kjøringsnummer ≤ 35 tegn, stabilt over revisjoner?
3. Arkivmodus i 5 år: minste som må kjøre (PDF/A og CSV i objektlager og enkel leser)?
4. Kontrollsporbeskrivelse som Rust-mal fra versjonert oppsett, med diff mellom år?
5. SAF-T Financial 1.30 generert fra D-Bilag og D-Postering med XSD-validering: kostnad hvis bare for modell B?
6. «Godkjenn og signer»: knytte bankstatus (PmtInfId, hash av betalingsfil) til `sammendrag_hash` i én D-Godkjenning med to separate autentiseringer?
7. Slettejobben: sjekk av D-Oppbevaringsregel, kvittering og juridisk hold. Bevis for sletting, f.eks. kryptografisk makulering?

## N31 Utlegg via integrasjon og ansattreskontro

### Endringer i kartleggingen
- **F-REG-29 (fase 1):** Les åpne poster på 2910 med dato i tillegg til saldo (Tripletex `GET /ledger/openPost?accountId=…`, ReAi `/api/ledger/employee`). Vis antall, sum og alder uten navn; per person krever lønnstilgang.
- **L-23 / L-08 (N07):** Ny kontroll L-32 (2910 og mellomkonto mot mottatte utleggslinjer). L-32c og L-32d i månedspakken. L-32g finner kunder som betaler trekkfri km og diett utenfor lønn uten å rapportere (kan vises i fase 1).
- **D-Regnskapskonto:** `reskontro` avgjør om kunden kan bruke flyt A eller må bruke C.
- **F-UTL-01 (MVP):** Regelen «den som utbetaler, bokfører». Flyt B (kilden sender linjer, Brutto bokfører i samlebilaget) som standard. Flyt A (utlegg allerede på 2910 per ansatt; Brutto debiterer 2910 og lukker paret med begge `postingId`) og flyt C (mellomkonto uten reskontro, avstemt per utleggs-id; for Fiken o.l.) som moduser per installasjon og linjetype.
- **F-UTL-02:** Andre nøkkel (kilde, kildeinstans, `kildeKravId`), som ReAi. Samme krav fra to integrasjoner holdes.
- **F-UTL-04:** Nye holdårsaker (natt/funn/N31.md §6).
- **F-UTL-07:** Status tilbake per kilde: Utleggsappen `PATCH /invoices/{id}` (bare «levert», ingen «utbetalt»), Expensify `REIMBURSED`, Pleo `successful`, ReAi `external-settlement`.
- **F-UTL-18 (rettes):** Flyt D (betaling utenfor lønn) holder bare for rene refusjoner mot kvittering (skatteforvaltningsforskriften § 7-2-3). Trekkfri km og kost skal også i a-meldingen for utbetalingsmåneden (§ 7-2-9). Kilden som betaler, bokfører også.
- **F-UTL-20 / F-KJO-31:** Forskudd avregnes på linjen (`forskuddRef`). Forskudd Brutto fører på 2910 merkes med `ekstern_ref` eller føres på egen konto.
- **F-UTL-22 / F-UTL-23:** Utleggsskjema (PDF per rapport) legges ved lønnsbilaget eller lagres med hash og lenke. MVA aggregeres per MVA-kode.
- **F-REG-05:** Tre slags utleggslinjer i samlebilaget: B (kostnad, MVA, godtgjørelse per konto, dimensjon og MVA-kode), A (D 2910 per utleggslinje med `ansatt_ref`), C (D mellomkonto med spesifikasjon per krav-ID i vedlegget).
- **F-REG-18 / ReAi-adapter:** Etter bokføring lukkes poster (Tripletex `PUT /ledger/posting/:closePostings`, ReAi `POST /api/postings/employee/close`). PowerOffice ukjent (N33).
- **D-Utleggslinje / D-Utleggsoppsett / D-Kilderegister:** Nye felt (N31 §6). Kilderegisteret må vite om kilden også leverer til regnskapet, ellers kan flyt B gi dobbel bokføring.
- **Senere:** OK-33 (rapporteringslinje for opplysningspliktige godtgjørelser kilden har betalt, med `utbetaltDato`). Åpne 2910-poster foreslått til utbetaling. Adaptere for Pleo og Expensify. Utlegg for ikke-ansatte via leverandørreskontro.

### Handling (gjøres av et menneske)
- Avklar med Utleggsappen: webhook-hendelser og innhold, om lønnsintegrasjon kan skrive «utbetalt dd.mm» og «innrapportert måned», og om deres deling i trekkfri og trekkpliktig del er forslag eller fasit.

### Åpne spørsmål (tas med i N30-intervjuene)
- Hvem oppbevarer kvitteringen i 5 år når Brutto bokfører utlegget (flyt B) og kunden slutter med kilden?
- Gjelder grensen på 1 000 kr per mottaker per år (skatteforvaltningsforskriften § 7-2-1 andre ledd) også ansatte med lønn?

### Spørsmål til Peter og Sander
1. «Den som utbetaler, bokfører» med B som standard og A og C som moduser?
2. Skal Brutto lukke poster i kundens regnskap (skriving utover bilag), eller bare varsle?
3. Hente åpne 2910-poster og foreslå dem til utbetaling, eller bare ta imot linjer fra kilden?
4. Forskudd på 2910 (S #27): egen konto eller merking?
5. MVA-linjer per MVA-kode i samlebilaget i flyt B?
6. Utleggsappen gir kontonummer per rapport (`payee`). Betale til egen D-Personbankkonto og varsle ved avvik?

## N32 Integrerte lønnsmoduler i praksis

**Viktig retting av N23 og N02:** Tripletex Lønn fører nettolønn per ansatt på 2910, ikke 2930 (696 lønnsbilag hos 14 klienter; 2930 aldri brukt). Ansatt står på nesten alle linjer. PowerOffice Go og Visma.net Payroll fører samlet per kjøring med netto på 2930.

### Endringer i kartleggingen
- **F-REG-29:** Saldo per konto og måned som standard (`/balanceSheet`, `/TrialBalance`). Debet og kredit for 2600–2690, 2770, 2940 og 5290 fra `/ledger/posting` med `fields=account(number),date,amountGross,voucher(id,voucherType(name),reverseVoucher(id))`, uten `employee` og `department`. Summer i minnet; lagre bare summer i D-Regnskapssaldo. I Tripletex er hver linje lønn per person, også uten ansatt-id.
- **F-REG-28:** Hos Tripletex-kunder har 5800 (sykepengerefusjon, helse) og 2650 (fagforening) ansatt. Les bare som saldo; adapteren ber aldri om `employee` på disse.
- **Saldomotor (N04 §7) / F-REG-30:** Reverseringspar trekkes ut før debet og kredit (Tripletex `reverseVoucher`, PowerOffice `IsReversed`/`ReversedVoucherId`, ReAi `reversesPostingId`). 17 % av lønnsbilagene i Tripletex er original eller reversering; uten fjerning gir «FP = debet 2940» feil i 37 av 101 klientmåneder. Posteringsdato teller, ikke bilagsdato. Fallback til bevegelse («delvis») bare når debet/kredit faktisk er nettet (Visma.net Payroll-bunter [verifiseres]).
- **N23-rettinger (F-REG-02, F-REG-03, D-A07Kontoregel):**
  - **2945** er «Periodisering av lønn» i Tripletex, ikke utbetalte feriepenger. Ut av FP. Månedsavstemming: 2945, 5095, 5096, 5495, 5496 = IKKE. Årsoppstilling: IB 2945 tillegg, UB 2945 fradrag (fordeling [verifiseres]).
  - **5401** «AGA av opptjente feriepenger» (Tripletex) legges til i AGA-gruppen. 5405 er «AGA av andre påløpte lønnskostnader» i Tripletex; rett kildemerket på K036.
  - **K080 (2930 UB = 0)** treffer ikke Tripletex Lønn. For Tripletex: «2930 har ingen bevegelse» (info). Kontroll på 2910 per ansatt venter til MVP.
  - **AGA per måned:** kredit 2770 minus debet 2770 fra bilag som ikke er betaling (Tripletex debiterer 2770 ved sykepengerefusjon). Betaling kjennes på bilagstype eller motkonto 19xx.
  - **Finansskatt:** Tripletex bruker 2771 (kostnad 5430/5431). Legg til 2771.
  - **Regelsett per lønnsmodul:** `tripletex_lonn`, `poweroffice_lonn`, `visma_payroll`, `ekstern`. Velges automatisk fra bilagstyper og kontonavn; kunden kan overstyre.
- **F-RAP-13:** Ingen av de tre gir virksomhet eller sone på posteringen. AGA per sone kommer bare fra A07 i fase 1.
- **F-RAP-15 / F-RAP-19:** Tripletex Årsoppgjør henter bare «bokført». Brutto kan foreslå tillegg og fradrag fra IB/UB på 2931, 2945, 2780, 2785 og 2980, med kilde per beløp. Differensiator.
- **R01:** Tripletex som første adapter (reverseringslenker, reskontrotype og kontonavn finnes; rene debet/kredit).
- **F-REG-17 (MVP):** Brutto netter aldri debet og kredit på samme konto og dimensjon i et bilag. 2940 avsetning og utbetaling alltid på egne linjer.
- **F-REG-07 / F-MIG (MVP):** Kunder fra Tripletex Lønn har netto og åpne poster per ansatt på 2910. Migreringen må lukke eller føre videre. Kunden må få beskjed om at Bruttos standard (samlet 2930) avviker.
- **F-REG-10 (MVP):** Tripletex' reverseringsmodell (samme dato, gjensidig referanse, per ansatt), ikke Vismas korreksjon i inneværende periode.
- **F-REG-14 / F-REG-15 (MVP):** AGA av OTP-premie som eget bilag. NAV-refusjon reduserer AGA (2770 mot 5400) i samme bilag. Ikke ansatt på 5800.
- **F-REG-18 / F-REG-19 (MVP):** PowerOffice tar imot `PayrollJournal` med `EmployeeNo` bare på reskontrolinjer. Tripletex' API for lønnstransaksjoner er DEPRECATED (N33).
- **F-TRK-17:** Visma.net Payroll henter ikke trekkpålegg fra API [verifiseres]. Brutto med API og kontering er en forskjell.

### Handling (krever godkjenning fra Sjur)
- Agenten fant en Visma-PDF («Payroll Extension – Info og bruksanvisning», ca. 1,3 MB, Visma Kundeportal) som trolig svarer på nettoføring og bilagstype hos tredjeparts-ERP. Den er ikke lastet ned. Skal den lastes ned?

### Spørsmål til Sjur
- Skattetrekk betalt fra lønnsbilaget i 2026: hvilken regel gjelder, og hva betyr den for kontrollen «UB 2600 = 0 etter forfall» (A07-T1)?
- Hvordan fordeler Tripletex 2945 mellom lønn, feriepenger og AGA i kontrolloppstillingen?

### Spørsmål til Peter og Sander
1. Tripletex-adapteren summerer posteringer i minnet og lagrer bare summer med rådata-hash; aldri D-Hovedbokslinje for 5xxx og 29xx?
2. Reverseringspar i saldomotoren med felles felt `reverserer` og `reversert_av` fra alle adaptere? Test: reversert lønnsbilag gir null.
3. Test med periodisert Tripletex-bilag der linjene ligger i to måneder (posteringsdato, ikke bilagsdato)?
4. Valg av regelsett i adapterens `Kapabiliteter` eller i D-Regnskapsoppsett? Overstyring?
5. Status «delvis» ved nettoføring: visning og toleranse (K03)?
6. Sperreliste i adapteren for 5800 og 2650 der posteringer aldri hentes?

## N37 Ansatt-API i andre systemer, markedsandeler og konkurrentenes henting

### Endringer i kartleggingen
- **F-REG-30 / F-MYN-21 / F-BYR-15 (salgsløftet rettes):** «Uten innlogging» holder ikke alene. PowerOffice henter A07 med systembruker (ett klikk per klient), Maestro med systembruker men krever ID-porten-innlogging, Sticos har systemtilgang per byrå, Fiken krever ID-porten, Tripletex er uklart. Nytt løfte: «alle klienter hentet og avstemt i natt, og på nytt ved endring, uansett system, ned på person og arbeidsforhold».
- **R01 / F-REG-29:** Behold Tripletex, PowerOffice og SAF-T. For ansatte: CSV først, deretter Visma.net Payroll (`/employees/withPosition`, `/taxUnits`, `fromLastChangedDate`) hvis pilotkunde har lønn der. Regnskapsadaptere etter Tripletex/PowerOffice: SAF-T, Business NXT, Xledger, Uni Micro.
- **F-PLA-17 / D-Personkobling:** Merk hver kilde med om den gir fødselsnummer (Tripletex, PowerOffice, Visma.net Payroll, Xledger, ReAi) eller ikke (24SevenOffice, trolig Business NXT). Kilder uten fødselsnummer går til koblingskøen, unntatt ett treff på navn og fødselsdato [verifiseres].
- **F-PLA-13 / D-Kilderegister / D-Feltkilde:** Kildetyper `regnskap_api`, `lonn_api`, `hr_api`, `fil`, `a07`. Visma.net Payroll og Xledger gir virksomhet (`taxUnitNrs`) til ANS-13.
- **D-Integrasjon:** `autentiseringstype` dekker Visma Connect (client credentials + tenant), Xledger-token per entitet, Unimicro OIDC, NXT-tjenestebruker per selskap.
- **F-BYR-08:** Tilgangsdiagnosen viser ansattkilde (API, fil, ingen) og andel koblede personer.
- **F-BYR-33:** Pris mot 15–87 kr per klient per måned; personnivå og ansattoversikt forsvarer høyere pris.
- **F-REG-21 / F-REG-20 (MVP):** Business NXT før eAccounting; Xledger etter Visma (samme GraphQL-klient for ansatte).
- **F-MIG-08 / F-MIG-09 (MVP):** Visma Lønn (Huldt & Lillevik) bare som historisk import (lønnskjøring stengt 2024). SD Worx via fil.
- **Posisjonering:** Accountflow er bred og tynn i lønn (ingen dokumentert kontroll per person, 2610, sone eller kontrolloppstilling). Brutto som lønnsspesialisten ved siden av dem, med eksport til Accountflow, Maestro og Periode & År.
- **Marked:** Ingen offentlige tall for 10–1000 ansatte. Omtrent en av tre bruker ulik leverandør for lønn og regnskap; minst 44 % av systemene lønnsspesialistene oppgir har ingen hovedbok.

### Handling (gjøres av et menneske)
- Ta med i henvendelsen til Skatteetaten: tillater bruksvilkårene at A07 hentes maskinelt om natten uten en person bak, og hva må logges?
- Spør pilotbyråene om fordeling av regnskaps- og lønnssystemer per størrelse (10–49, 50–249, 250–1000 ansatte). Be Regnskap Norge om fordeling per system i Teknologiundersøkelsen 2025.
- Gå gjennom Accountflows offentlige webinarer og kundecaser for lønnsdybde.
- Har noen tilgang til en Tripletex-byråkonto der det kan sjekkes om A07-hentingen krever innlogging? (Ikke opprett kontoer.)

### Spørsmål til Peter og Sander
1. Egen Rust-trait `AnsattKilde` (personer, arbeidsforhold, virksomhet, `har_fnr`) ved siden av regnskapstraiten, eller én felles adaptertrait per system?
2. Felles modul for Visma Connect-token og nøkler (Visma.net Payroll og Business NXT), som for Maskinporten?
3. GraphQL for NXT og Xledger: `cynic`, `graphql_client` eller rene spørringer med `reqwest` og `serde`?
4. Webhook `EMPLOYEE_CHANGED` fra Visma.net Payroll i fase 1, eller nattlig spørring med `fromLastChangedDate`?

## N38 Navneliste-import og personvern for A07-data

### Endringer i kartleggingen
- **F-MIG-10 (inn i fase 1):** Navneliste med fødselsnummer, fornavn, etternavn, ansattnummer og avdeling (fødselsdato bare reserve, ingen e-post i fase 1). Originalfila lagres ikke. Rader uten treff i A07 eller regnskapssystemet forkastes. Fødselsnummer oppfyller personopplysningsloven § 12 (A07 har ikke navn), men brukes bare som koblingsnøkkel med blind indeks.
- **F-PER-02:** Én Rust-crate for identifikatorer på server og i WebAssembly. Dagens k1-regel og 2032-regelen med byttedato i D-Regelpakke. H-nummer og FH-nummer avvises. Produksjon avviser syntetiske numre; test-tenanter godtar bare syntetiske. Fødselsdato fra D-nummer er ikke pålitelig.
- **Ny F-id (BYR): «Innhenting av navneliste via lenke»:** Kunden logger inn med BankID; fila leses og valideres i nettleseren (Rust/WASM); serveren krypterer fødselsnummeret straks og lagrer ikke fila. Enkel del av F-BYR-22, med D-Grunnlagsinnsending. Helst regnskapssystemets API; aldri e-post.
- **F-PLA-17:** Navneliste med fødselsnummer gir eksakt automatisk kobling. Fødselsdato alene går til koblingskøen. § 7-31-koblinger aldri automatiske.
- **F-SIK-07 / F-SIK-08 / F-SIK-19:** Dataklassene (natt/funn/N38.md §7) i D-Rolledefinisjon og som `x-dataklasse`. Fagforening og utleggstrekk per person normaliseres ikke (bare summer). Permisjonsbeskrivelsen krypteres (sykdom over 12 måneder rapporteres som permisjon). A07 rå får egen DEK.
- **F-MYN-21 / D07:** Klienten velger modus «Avstemming» (`utenInntektsmottakere`) eller «Ansattoversikt»; valget er del av instruksen.
- **P05 / F-MYN-42:** Ny kontroll «Fagforeningstrekk i A07 mot 2650» på sumnivå.
- **F-SIK-27 / H08:** DPA-vedlegget lister kategorier, formål og instruks som konfigurasjon. D-Abonnement får instruksfelt, versjon, hvem som godtok og når.
- **F-SIK-28:** Risikolista (15 risikoer og tiltak) inn i referanse-DPIA. DPIA trolig påkrevd hos kunden (fire av Datatilsynets ni kriterier).
- **F-SIK-03:** Step-up for å bekrefte navneliste-import, vise § 7-31-grunnlag per person og eksportere persondata.
- **F-SIK-16 / D10:** Nye hendelsestyper `import.identitet`, `identitet.vis_full`, `lonn.vis_person`, `fravaer.vis_beskrivelse`, `rollematching.dekrypter`.
- **F-SIK-21 / F-SIK-22:** Oppbevaring: importfil lagres ikke, importrad 30 dager, A07 rå 13 måneder (5 år når den inngår i en låst rapport), rolle-øyeblikksbilder.
- **F-ORG-01 / F-ORL-13 / F-RAP-17:** Øyeblikksbilde av roller ved hver A07-henting. Ny entitet D-Rolleinnehaver (rolle, navn, fødselsdato, først sett, sist sett). Status «ingen ytelse rapportert» skilles fra «ikke koblet».
- **I02:** Nye rettigheter `lonn.les`, `identitet.les`, `fravaer.les`, `konfidensiell_gruppe`. Ingen `fagforening.les` eller `trekk.les` per person i fase 1.
- **D09:** Fødselsdato lagres ikke som eget felt.
- **MVP:** Navn med Brutto som kilde, bekreftet med BankID i ansattportalen. E-post i malen. Fagforening og trekk per person med egne roller og kryptering. Innsynsuttrekk med kilde per felt (F-SIK-30).

### Handling (gjøres av et menneske)
- Få rådgiver til å vurdere art. 9 (fagforening, permisjon) i avstemmingsverktøyet (S §7, Sally spm. 61).
- Søk om tilgang til Brønnøysundregistrenes rolleutskrift-API (avklar om Brutto kan bruke det som databehandler).

### Spørsmål til Sjur
- § 7-31 i praksis: regnes varamedlemmer med? Daglig leder alene og styret samlet?

### Spørsmål til Peter og Sander
1. Kan calamine og validatoren kompileres til `wasm32-unknown-unknown` med akseptabel størrelse? Ellers CSV i WASM og `.xlsx` på serveren uten lagring?
2. TLS avsluttes i egen ingress eller i Azure Front Door / Application Gateway? Avgjør om importruten trenger JWE.
3. Permisjonsbeskrivelse som kryptert kolonne i D-Permisjon eller egen tabell med egen DEK?
4. Egen tabell for summer av fradrag og trekk (f.eks. `a07_fradrag_sum`), så ingen spørring leser per person ved en feil?
5. Step-up ved bekreftelse av navneliste, eller bare når importen overstyrer navn fra regnskapet?
6. Hvor bor matchingjobben for roller (dekrypteringsrett for `identitet`, én masselesing logget per klient)?
7. Testfiler for CSV fra Excel (Windows og Mac), Numbers og Google Sheets i CI?

## N17 Lønnsbetaling i bank

### Endringer i kartleggingen
- **F-BET-22 / D-Betalingsforslag.kanal:** Behold `betalingspartner`. ZTL Payment Solution AS er betalingsforetak med full tillatelse fra 3.7.2020 (pengeoverføring, PIS, AIS; ikke e-penger). Kunden er avtalepart med ZTL; byrået er ikke part. Brutto er ERP/teknisk leverandør, flytter aldri penger (S #23), og yter førstelinjesupport (ZTLs vilkår 11.1).
- **Ny entitet D-Partnerkunde:** `klient_ref`, `partner`, `onboarding_id`, `onboarding_status` (Created, AwaitingCustomerAction, Processing, ManualHandling, Accepted, Rejected), `signatarer_status`, `vilkar_versjon`, `akseptert_tid`, `internasjonal_aktivert`. Knyttes til F-BYR-02.
- **D-KID / F-BET-01:** Skatteetatens KID: 19 siffer, MOD11 (vekttall 2–7), buffertall i posisjon 18, kontrollsiffer i 19. Del `kontrollsiffer` i `buffertall` og `kontrollsiffer`. Testvektor 0099999999905210217 som gyllen test.
- **D-Betalingslinje / D-Betalingsoppdrag:** Nytt felt `adressepolicy` (`ingen`, `kun_land`, `full`; standard `ingen` innenlands, `kun_land` PSD2-bulk). Hard sperre: adressebeskyttet person får aldri gateadresse; utenlandsbetaling da til manuell sak. Nytt felt `tillat_logisk_duplikat`. Kravet om strukturert adresse gjelder ikke innenlands og er utsatt på ubestemt tid.
- **F-BET-20:** Kontroll før sending: samme dato, beløp, debetkonto og kreditkonto i samme forslag gir varsel (SpareBank 1 avviser like betalinger uten å se på KID; to samordnede trekk med samme beløp til 7694 05 69814 kan stoppes).
- **D-Banksignering:** `signert_av_ref` nesten alltid tom via ZTL (ingen bank oppgir signatar). Nytt felt `signatar_pseudonym`. Bevis for godkjenning ligger i Bruttos lag 1.
- **D-Banksamtykke:** ZTL krever `userId` (fødselsnummer eller bank-ID) for den som gir samtykke. Krypteres, lagres bare så lenge samtykket varer.
- **F-BET-21:** Via ZTL én sum i banken; fil: SALA på `PmtInf`; PSD2-bulk SpareBank 1: SALA per betaling, skjult lønn ikke bekreftet. PowerOffice-kanalen kan ikke skjule lønn.
- **Kundeavtale (S #23):** Lønnen går via ZTLs klientkonto; ZTL har tillatelse som betalingsforetak; ansvaret er begrenset til én måneds gebyrer; arbeidsgiveren har risikoen til hver mottaker er `Completed`. Ved ZTL-konkurs har arbeidsgiveren separatistrett bare hvis midlene faktisk er holdt atskilt (finansforetaksloven § 13-18). Mal for informasjon til ansatte om ZTLs behandling.
- **F-BET-08 (MVP, fil):** pain.001.001.09 med `SvcLvl` NURG. Netto: SALA på `PmtInf`, uten `RmtInf`. Trekk: eget `PmtInf` med SUPP og KID (SCOR). Ingen `PstlAdr` innenlands. Bankprofil i `D-Betalingsfil.bankguide`.
- **F-BET-22 (MVP, ZTL):** Lønn via `POST /api/v2/payroll` med nøytral melding (f.eks. «Lønn 2026-11»). Trekk som egne innenlandske betalinger med `ocr`. Webhooks + polling; grunn hentes fra status-API.
- **F-BET-13 / F-BET-17:** `InProgress` er aldri «betalt». Ny alarm når mottakere står i `InProgress` etter lønnsdatoen.
- **F-BET-09:** Fil skal alltid kunne lages som beredskap mot ZTL-nedetid eller konkurs.
- **Teknisk leverandør:** Unntaket i finansforetaksforskriften § 1-7 bokstav j kan passe for Brutto, men gjelder ikke PIS/AIS. Brutto kan bli agent hvis vi opptrer for ZTL overfor kunden [advokat].
- **Banker:** SpareBank 1 har PSD2-bulk med SALA og flere signaturer (PATC). Eika har psd2.eika.no uten bulk. DNB og Nordea bak innlogging.

### Handling (gjøres av et menneske)
1. Advokatvurdering av Bruttos rolle overfor ZTL (teknisk leverandør, agent eller utkontraktering; forskriften § 1-7 j, § 2-3, § 2-4, PSD2 art. 3 j og art. 19, DORA) og innholdet i partneravtalen. Kan slås sammen med advokatvurderingene fra N30 og N40.
2. Be ZTL om partneravtale, sandkasse og dokumentasjon av klientmiddelsikringen (sikringsmetode, bank, daglig avstemming, revisorbekreftelse, gebyrer og renter, tid fra trekk til utbetaling, Movitz' rolle, oppdaterte vilkår, `allowLogicalDuplicate` for trekk, rolle i personvern).
3. Opprett brukere på bits-standards.org (Bits MIG 2.0 for pain.001.001.09) og developer.dnb.no (PSD2 3.25.0) for å lese spesifikasjonene.

### Spørsmål til Peter og Sander
1. `kid::skatteetaten` i Rust med løkke for buffertall, testvektor og egenskapstester?
2. pain.001-generator med `adressepolicy` per linje og hard sperre på `adressebeskyttelse`?
3. ZTL-adapter: lønn og trekk som ulike ressurser, webhook uten grunn, `InProgress` dekker tre faser, ny godkjenning ved `PartlySigned`?
4. Duplikatnøkkel før sending: dato, beløp, debetkonto og kreditkonto, uten KID?
5. PSU-ID og ZTL-`userId` kryptert og aldri logget?

## N14 A-melding 2.4 og varsler

### Endringer i kartleggingen
- **Tidsplan (Skatteetaten 22.10.2026):** Endelig innhold 01.04.2027, spesifikasjon senest 01.05.2027, testmiljø senest 15.09.2027, produksjon fra periode 2028-01. Innholdet er ikke bestemt. Sterkeste kandidat: utsatte arbeidsforholdsfelt (permittering, lønnet permisjon, maritime forhold, frilanser), som finnes i JSON-modellen og A07 allerede. Trolig mer regler enn struktur [verifiseres].
- **F-MYN-21 / D-Avstemmingsrapport:** Nye felt `api_versjon` og `meldingsformat_periode` (utledet av inntektsåret). Parser per inntektsår og API-versjon. Bestill alltid per inntektsår.
- **F-MYN-15 / D-Tilbakemelding:** Nytt felt `api_versjon`. A03-leseren tåler ny tilbakemeldingsversjon og tomme felt for forfall og KID for utleggstrekk.
- **F-MYN-24 (overvåking):** SBS-RSS for a-meldingen, SwaggerHub-versjoner for innsending, filopplasting, tilbakemelding og avstemmingsrapport, informasjonsmøtet 10.12.2026 og januarinformasjonen 2027, høringer om a-opplysningsforskriften, Dialogporten-metadata for `ske-arbeidsgiverkontroll`. Milepælene 01.04, 01.05, 01.09, 15.09 og 01.12.2027 som D-Kontrollsak med frist.
- **F-MYN-43:** Tvangsmulktsensoren klassifiserer dialogene i `ske-vedtak-tvangsmulkt-overtredelsesgebyr` (i prod, med `subscribe`). Handler for `ske-arbeidsgiverkontroll` (bare dialoger i TT02, ingen dokumentasjon) ligger klar, men av. A50/A51 finnes bare som migrert historikk.
- **F-MYN-22, nye saksregler:** Tvangsmulktrisiko ved måned uten a-melding i A07; ved F108 eller F231 i A03, med anslått mulkt per dag; mottatt påminnelse eller vedtak; ny sak i arbeidsgiverkontrollen (når i prod).
- **F-MYN-42 / ANS-04:** Funn som tilsvarer F108 og F231 merkes «kan gi tvangsmulkt».
- **D-Myndighetsabonnement:** `tjeneste` får `dialogporten_arbeidsgiverkontroll`. Nytt felt `aktiv` for sovende handlere.
- **D-Kontrollsak:** Nye felt `klassifisering` (`amelding`, `annen`, `ukjent`) og `kilde_ressurs`.
- **D-Permisjon:** `loennet` blir tre verdier (ja, nei, ukjent). Fra A07 alltid ukjent.
- **D-Lonnsart / D-Lonnsartmapping:** Mapping til a-meldingen med gyldighet per regelpakke, ikke faste felt på lønnsarten. Ingen egen D-Inntekt før 2.4 er kjent.
- **D-Regelpakke / D-Kodeverk:** `gyldig_fra`, `gyldig_til` og `meldingsformat` på hver regel og kode.
- **F-MYN-20 (MVP):** Én serialiseringstrait med genererte moduler per format; domenet ser aldri formattyper. Spesifikasjon 01.05.2027 gir typer, testmiljø 15.09.2027 gir lukket sløyfe med A07, kodefrys 01.12.2027. Presedens fra 2.3: ny versjon fra januar, kunne brukes for eldre perioder [verifiseres for 2.4].
- **F-MYN-12 / F-MYN-14 / F-MYN-10 / D-AMelding (MVP):** Basis-URL, sti og versjon som konfigurasjon per format. Reserve blir JSON-eksport fra 2027 (`xml_eksport_ref` → `reserve_eksport_ref`). Kontroller før innsending per format. Nytt felt `api_versjon`.
- **Tvangsmulkt (MVP):** Altinn Events for tvangsmulktressursen. Kravtyper for tvangsmulkt fra Krav og betalinger kobles til saken. A50/A51 leses ved migrering.

### Handling (gjøres av et menneske)
- Følg informasjonsmøtet 10.12.2026 og januarinformasjonen 2027, og høringer om permittering, lønnet permisjon, maritime forhold og frilanser før 01.04.2027.
- Spør Skatteetatens brukerstøtte hva `ske-arbeidsgiverkontroll` inneholder og erstatter, om REST-API-et tar imot 2.3 for 2027-perioder etter 01.01.2028 (og hvor lenge), når ny A03-versjon kommer, format for manuell opplasting i JSON fra 2027, og om tvangsmulkt for a-meldingen er tatt opp igjen fra august 2026 og satsen for 2027.

### Spørsmål til Peter og Sander
1. Én trait for serialisering med genererte moduler per format, og domenet uten formattyper?
2. A07-parser per inntektsår og API-versjon, med nattlig kontrakttest mot TT02?
3. Hvis MVP lanseres etter januar 2028 og 2.4 kan brukes for eldre perioder, trengs kanskje bare 2.4. Hvilken lanseringsdato planlegger vi med?
4. Kapasitet fra 15.09 til 01.12.2027 til 2.4-testing?
5. Brutto svarer aldri i arbeidsgiverkontrollen og klager aldri på mulkt, selv om pakkene gir `write`?
6. Tvangsmulktsensoren: daglig polling i fase 1 og Events i MVP; holder pollingbudsjettet fra N27? JSON Schema-validering (`jsonschema`) som erstatning for XSD?

## N13 Trekkrutinen, avrunding og skatteplikt

### Endringer i kartleggingen
- **K03 / F-REG-27 / F-REG-30 / F-RAP-13 (toleranser i fase 1):** Forskuddstrekk og utleggstrekk 0 kr (heltall i A07; øre på 26xx gir lavt signal). AGA: |Σ(grunnlag × sats) − `sumArbeidsgiveravgift`| < 1 kr per a-melding (× antall meldinger i måneden); større avvik behandles som F185. Inntekt ≤ 1 kr per inntektsmottaker.
- **D-Regelpakke (ADR-06 i N08):** Avrundingstabellen (natt/funn/N13.md §2) som data: nøkkel, strategi (`ToZero`, `AwayFromZero`, `MidpointAwayFromZero`), nivå, retning for negative beløp, hjemmel, gyldig fra. Prosenttrekk ned på grunnlag og trekk (skattebetalingsforskriften §§ 5-10-4, 5-5-4); fagforeningskontingent opp (§ 5-9-1); skatte- og avgiftskrav ned (§ 10-4-4). I a-meldingen er trekk og «AGA å betale» heltall.
- **D-Sats / D-Kontrolloppsett (L-30h, L-30i):** Skattefrie gaver 5 000 kr per år, 4 000 kr jubileum/oppmerksomhet, 8 000 kr etter 20 års tjeneste (FSFIN § 5-15-1, uendret siden 2021). Gruppeliv, behandlingsforsikring, ulykkesforsikring utover yrkesskadeloven og privat del av reiseforsikring er skattepliktig fra første krone, men kan dekkes av gavegrensen.
- **F-MYN-24:** Overvåk grener og commits i `Skatteetaten/trekktabell`, `Last-Modified` og SHA-256 for tabellfila, siden med tabelltrinn, og endringer i skattebetalingsforskriften kap. 5 og 10 og FSFIN § 5-15-1.
- **Trekkrutine:** Skatteetaten publiserer Java-kode (8 filer, ca. 25 kB, én gren per år, ny versjon tidlig i desember) og en tabellfil (96 tabeller, 5,6 MB zip, til testing, stopper på 200 000 kr/mnd). Repoet har ingen lisensfil. Brutto skriver egen port.
- **F-TRK-07 (MVP):** Egen crate `brutto-trekkrutine` med `fn tabelltrekk(år, tabell, periode, grunnlag_kr: i64) -> i64`. Algoritme som kode per inntektsår, konstanter i D-Regelpakke/D-Sats. **`f64` tillatt bare her**, i samme rekkefølge som Java (eksakt desimalregning ga 1 kr feil i 60 av 1,09 mill. rader). CI: 100 % treff mot tabellfila, egenskapstester fra `TrekkrutineTest`, vektorer over 200 000 kr. Negativt grunnlag settes til 0.
- **F-TRK-08:** Prosenttrekk = ⌊⌊grunnlag⌋ × p / 100⌋; grunnlag i øre (i64), kuttet til hele kroner.
- **F-TRK-09 / F-TRK-16:** Tabelltrekk av summert grunnlag minus allerede trukket (§ 5-10-1). Trekk summeres per utbetalingsdato som heltall.
- **Ny funksjon «velg trekkperiode» i F-TRK-07:** Lønnsperiode → tabell og faktor (N13 §1.7), med testcaser.
- **F-TRK-10:** Frikort følges hittil i år, inkl. feriepenger; over grensen 50 %.
- **F-TRK-11 / F-TRK-12 (rettes):** Juni: feriepenger trekkfrie (standard) eller én vanlig månedslønn trekkfri; 21 %-regelen og tak 12,3 %. Desember: ⌊tabelltrekk / 2⌋. 14-dagers: én trekkfri utbetaling; time/dag/uke: to trekkfrie uker. **Tillegg utbetalt med lønnen omfattes av halvt trekk inntil gjennomsnittsfortjenesten (§ 5-7-2 fjerde ledd)** – rett F-TRK-12 og C. D-Lonnsart får flaggene `trekkfritak_juni` og `med_i_halvt_trekk`.
- **F-TRK-23:** Kontingent rundes opp til hel krone.
- **F-KJO-13:** AGA eksakt per virksomhet, rundes én gang per opplysningspliktig og måned; standard ned til TT02 bekrefter F185.
- **F-KJO-14 / F-KJO-37:** Feriepenger i øre per ansatt og utbetaling med `MidpointAwayFromZero`.
- **F-KJO-18 (årshjul):** Forslagspakke for 2027 fra statsbudsjettet (trygdeavgift 7,4 %, personfradrag 120 180 kr; med forbehold om vedtak). Bytt trekkrutine når 2027-grenen kommer; kjør hele tabelltesten før januarlønnen.
- **F-KJO-33:** Brutto fra netto med binærsøk på heltallsgrunnlag (minste grunnlag som gir netto ≥ målet).
- **F-KJO-42:** Lønnsslippen viser trekkperiode, tabell eller sats, bruttolønn, beregningsgrunnlag med fradrag, forskuddstrekk og utleggstrekk (§ 5-10-20).

### Handling (gjøres av et menneske)
1. Be Skatteetaten om skriftlig lisens (f.eks. Apache-2.0) eller samtykke til kommersiell gjenbruk av trekkrutinen og tabellfila, og om varsling ved nye versjoner.
2. Godkjenn nedlasting av tabellfila for 2025 og 2026 (5,6 MB zip fra Skatteetaten) til repoet, så hele tabelltesten kan kjøres.
3. Spør Skatteetaten om dokumentasjon for «anvendt minstefradrag» på 88 % og inntektsperiode 12,12, og om det finnes fast privat andel av reiseforsikring.

### Spørsmål til Sjur
- Gruppeliv i tjenestepensjon mot frittstående gruppeliv: hvilke kontoer og A07-koder skiller dem?
- Hvordan beregner Tripletex, Visma og PowerOffice gjennomsnittsfortjenesten ved halvt trekk med tillegg?

### Spørsmål til Peter og Sander
1. `f64` i én isolert crate som unntak fra «aldri `f64`», vokset av gylden test mot alle tabellrader?
2. Egen Rust-port (anbefalt) eller JVM-sidecar med Skatteetatens Java-kode?
3. Skatteetatens Java-kode som orakel i CI for beløp over 200 000 kr (krever JDK og ekstern kode), eller bare tabellfil og faste vektorer?
4. Algoritme som kode per inntektsår og konstanter som data, eller alt som data?
5. AGA-standard: ned (forskriften) eller nærmeste krone før TT02 har svart? Toleranse «< 1 kr per a-melding» i fase 1?
6. Negative beløp: `ToZero` eller `ToNegativeInfinity`?

## N15 NAV-refusjon og K27

### Endringer i kartleggingen
- **F-MYN-34 (delvis til fase 1):** K27 (`ref-arbg`) hentes via NAVs Oppgjørsrapporter-API (scope `nav:utbetaling/oppgjorsrapporter`). Én rapport per utbetaling, CSV med én linje per ansatt, ytelse, periode og beløp; ingen KID og ingen kobling til inntektsmeldingen. Byråkunder via agent-systembrukeren med `regnskapsforer-lonn`. Direktekunder trenger `lonn-personopplysninger-saerlig-kategori` eller laster opp CSV. NAVs bruksvilkår og kontakt nav.ur.og.os@nav.no inn i oppkoblingsplanen (M01).
- **Polling:** `etterId` per orgnr daglig, to ganger i døgnet virkedag 1–5, og søk med forrige år i januar. Rapport-`id` er idempotensnøkkel. Ikke bruk `arkiver` som lest-markør.
- **Ny D-NavRapport:** `id`, `orgnr`, `datoValutert`, `bankkonto`, `belop`, `opprettet`, hash av rå CSV og PDF. **D-NavRapportlinje i fase 1:** bare aggregater per (rapport, bedriftsnummer, ytelsesgruppe: ordinær, feriepenger, trekk); fødselsnummer og navn forkastes i minnet.
- **L-22 (N07) deles i L-22a–L-22h** (natt/funn/N15.md §4) i terminpakken, mot A07-fradrag, 5800, fordringskonto og bank. Egne `differansetype` for tidsforskjell, trekk og dobbelt fradrag.
- **F-FRA-26 / F-REG-15:** AGA-metode for refusjon per virksomhet og år i fase 1. Brutto kan foreslå metoden ut fra K27-valutering.
- **F-REG-30 / N23:** Regelsett `refusjon_kontant` (bank → 5800) og `refusjon_periodisert` (1579x ↔ 5800), valgt automatisk.
- **F-REG-15 (rettes):** Fordringskonto 1579 (eller underkonto mappet til SAF-T 1579 og grupperingskode 1570), ikke 1580 (tapsavsetning) eller 1570 (reiseforskudd i SAF-T).
- **F-REG-28 / F-SIK-08:** 5800 og K27 bare som sum i fase 1. Rå CSV og PDF er særlig kategori.
- **F-REG-29:** Posteringer på bankkonto (beløp, dato, uten ansatt) for L-22b; debet og kredit for fordringskontoen.
- **F-BYR-15:** Kolonne «NAV-refusjon» med L-22-status per termin.
- **MVP:** Refusjonsreskontro per ansatt, ytelse og periode (D-Refusjonskrav: `forventet` → `krevd` → `delvis_mottatt` → `mottatt`/`avvik`/`avskrevet`/`foreldet`; D-Refusjonsavstemming). Matching på fødselsnummer + ytelsesgruppe + bedriftsnummer + overlappende periode, så beløp med toleranse; støtte 1:n, n:1, negative linjer. Mål ≥ 75 % auto-lukket (Trondheim kommunes nivå). Forventet beløp for sykepenger, FP, omsorgspenger og feriepenger etter formlene i N15. `FEILET`/`FORKASTET` på inntektsmelding setter kravet i avvik. camt.054 fra NAV matches mot D-NavRapport. Lønnsbilag fører D 1579x / K 5800. Varsler for frist (3 mnd, 6 fra 2027 hvis vedtatt), ikke mottatt, maksdato, lønn under foreldrepermisjon uten krav. Migrering av historiske K27 og åpne krav.
- **Konkurrenter:** Tripletex fører refusjon manuelt; PowerOffice importerer K27-CSV uten sammenligning; Visma- og SD Worx-kunder bruker egne team og roboter. Arbeidsgiver får ikke NAVs vedtak, så forventet refusjon er alltid et estimat.

### Handling (gjøres av et menneske)
- Kontakt NAV (nav.ur.og.os@nav.no) om testrapporter for TT02-virksomheter i NAVs dev-miljø (Dolly eller generator), status for FP/SVP-forespørsel i Dialogporten og K9-API i produksjon, og om lovforslaget om seks måneders frist er vedtatt.

### Spørsmål til Sjur
- Når valuteres feriepengerefusjonen (slutten av mai eller juni), og hvilken måned får AGA-fradraget? Hvordan avrunder NAV dagsats og månedsbeløp?

### Spørsmål til Peter og Sander
1. Rå K27 (særlig kategori, dokumentasjon for AGA-fradrag i 5 år) kryptert med egen nøkkel og egen rolle, eller bare hash og aggregater?
2. Parser: beløp i øre med fortegn bak tallet, `i64`, ukjent ytelseskode → `Ukjent(char)` og sak; test at sum av linjer = `belop`?
3. Samme matchemotor for L-22 (fase 1) og reskontroen (MVP), deterministisk og mulig å kjøre på nytt per rapport-id?
4. AGA-metode i D-Virksomhet eller D-Regnskapsoppsett, versjonert per år, og sperre mot metodebytte midt i året?
5. Polling i fase 1 og Altinn Events senere, felles med A07?
6. `lonn-personopplysninger-saerlig-kategori` for direktekunder fra start, eller bare CSV-opplasting til lønnskjøringen kommer?

## N16 Pensjonsleverandører og OTP

### Endringer i kartleggingen
- **F-REG-30 / F-MYN-42 / F-REG-27:** L-21 (N07) erstattes av L-21a–j (natt/funn/N16.md §7). Månedspakke: L-21a, b, c. Terminpakke: L-21d, g. Årspakke: L-21g, h, i. Første utgave: L-21c, d, e, g; så L-21a og h etter kalibrering.
- **F-MYN-08 / F-PEN-10 (rettes):** A-ordningen gir bare avvik (MAGNET_EDAG-507, retningslinje) når premie er oppgitt uten innretning; OTP-plikt uten ordning gir ingen melding. Feltet er `JuridiskEntitet.pensjonsinnretning` (0..n) med `identifikator` i XSD v2.3; fjern [verifiseres].
- **F-PEN-02:** OTP-loven § 1 a–c (to personer ≥ 75 %, én uten eierinteresse ≥ 75 %, eller stillinger ≥ 20 % som til sammen er to årsverk), unntak § 1 (3), seks måneders frist § 2 (2), Skatteetatens vedtak § 2 (4), § 4: 2 % opp til 12G, medlem fra 13 år (§ 4-2) uten 20 %-grense for medlemskap. 4 %-forslaget ikke vedtatt etter komiteens tilråding [voteringen verifiseres].
- **D-Regelpakke:** OTP-regler per år, G per dato, Finans Norges klassifisering av lønnsbeskrivelser (alltid, kan, aldri; bransjenorm v1.03, faktor 12,16), kjente pensjonsinnretninger med orgnr.
- **D-Kontrolloppsett:** Karenstid L-21a (6 mnd), toleranser L-21g og L-21h (forslag 10 %).
- **D-Virksomhet:** Nye felt `pensjonsordningstype` (privat OTP, offentlig, ikke pliktig, vedtak) og `forventede_pensjonsinnretninger[]`. D-Pensjonsordning tar over i MVP (F-ORG-27).
- **F-REG-29:** Leverandørens orgnr på posteringer mot OTP-kontoene (L-21f), bevegelse på 5941–5950 og 5255, IB/UB på 2690, 1700–1749, 2960 og 1394.
- **N23 / S #29:** Anbefal 5950 «Obligatorisk tjenestepensjon (OTP)» (SAF-T) eller kundens egen OTP-konto i stedet for 5420 (5420 er pensjon over drift, rapportert per person). Grupperingskode for OTP i AS må avklares.
- **F-RAP-15 / N24:** `aaretsInnbetalingAvArbeidsgiveravgiftspliktigTilskuddOgPremieTilPensjonsordning` fylles med Σ `tilskuddOgPremieTilPensjon` fra A07, med bokført ved siden av.
- **D-Avstemmingslinje:** Nye `differansetype` A07-P1 (innretning mangler), A07-P2 (ugyldig), A07-P3 (under minstesats).
- **MVP (ingen integrasjon per privat leverandør):** Private OTP-leverandører henter lønn og arbeidsforhold fra a-ordningen når a-meldingen har leverandørens orgnr i `pensjonsinnretning[].identifikator` hver måned. Brutto garanterer innretning i hver melding (også ved flere avtaler og bytte), i erstatningsmeldinger, lønnsarter flagget etter Finans Norges norm, arbeidsforhold med endringsdatoer, `tilskuddOgPremieTilPensjon` i betalingsmåneden. L-21 kjøres på egen a-melding før innsending.
- **F-PEN-06 / F-REG-14 (rettes):** AGA følger betalingsmåneden (bekreftet). Grunnlaget fordeles på soner etter øvrige avgiftspliktige ytelser i samme måned, ikke etter pensjonsgrunnlaget – GC-17 må regnes om. Administrasjonskostnader inngår, ikke meglerhonorar og flyttekostnad. Premiefond: innbetaling gir AGA, bruk gir ikke.
- **F-PEN-05 / D-Pensjonspremie:** Premie fra regnskapet (postering på OTP-konto med leverandør og betalingsdato), manuelt, senere Finans Norges returfil. Felt `betalingsdato`, `sparing`, `risiko`, `omkostninger`, `fra_premiefond`, `egenandel`.
- **F-PEN-08:** Forventet premie med leverandørens lønnsbegrep og faktor 12,16; avvik over 12 måneder.
- **F-PEN-04 / F-PEN-17:** HR-oppgaver i leverandørens portal (pensjonsgivende lønnsarter, inn- og utmeldinger, sykdom over 12 måneder).
- **F-PEN-11 (KLP)** bare hvis pilotkunde har offentlig ordning (format ikke offentlig). **F-PEN-12 (SPK)** Kan, krever fastformat 2.7 og godkjenning. **F-PEN-14 (AFP):** ingen rapportering. **F-PEN-09:** egenandel ≤ 4 % og ≤ arbeidsgivers innskudd. **F-MIG-27:** første a-melding fra Brutto med samme innretning som forrige system.

### Handling (gjøres av et menneske)
- Kontakt Finans Norge om returfilen (hvilke leverandører, versjon) og spesifikasjonen for den elektroniske lønnsfilen (XML).
- Hvis pilotkunde er HUK eller ideell: hent KLPs lønnsfilformat via pilotkunden, og følg saken om kommunale leverandørers tilgang til a-ordningen.

### Spørsmål til Sjur
1. OTP-konto (S #29): 5950 (SAF-T) eller kundens egen, i stedet for 5420? Hvilken grupperingskode for AS?
2. Eierinteresse i OTP-loven § 1 b: hvordan skille eier fra arbeidstaker uten aksjonærregisteret?
3. Hvilken G bruker leverandørene for 12G-taket, og hvordan påvirker 12,16 og feriepenger minimumet i L-21h?

### Spørsmål til Peter og Sander
1. `pensjonsinnretning` som `Vec<Pensjonsinnretning>` med `#[serde(default)]`; `identifikator` som `Norsk(Orgnr) | Utenlandsk(String)` etter validering?
2. Tidsserie med arbeidsforhold per måned (snapshot per A07-måned) for L-21a, med `regelsett_versjon` på resultatet?
3. Minstesats i `rust_decimal` med G fra datert tabell; tak per person og år, lagret bare som sum?
4. L-21f krever leverandørens orgnr fra regnskapsadapteren; ellers faller kontrollen bort med beskjed til kunden?
5. Finans Norges klassifisering som data koblet til kodelisteversjonen?

## N18 Huma-API

### Endringer i kartleggingen
- **Ny valgfri ansattkilde `hr_api: huma` (F-REG-29, F-PER-35, F-PLA-13):** Huma Open API 1.89.0, OAuth2 client credentials per Huma-organisasjon, maks 50 per side, uten endringsfilter, uten dokumentert rate limit og uten byråtilgang. Fase 1: bare henting (`GET /users`, `/users/{id}`, `/users/{id}/positions`) nattlig og på forespørsel. Bygges bare hvis pilotkunde har Huma; ellers importmal for Humas personeksport (F-MIG-10).
- **Hent:** navn, foretrukket navn, e-post, `employmentId` (hint), `identifications[national]` (bare kobling, blind indeks), `birthDate`, `companies[].organizationNumber`, `teams`, `locations`, `supervisor`, stillingstittel og stillinger, `connectedIntegrations`, `status.active`. **Ikke hent i fase 1:** `bankAccount`, `salary`, `children`, `emergencyContacts`, `homeAddress`, `privateEmail`, `custom`.
- **Kilderegel (D-Feltkilde/D-Feltkonflikt):** Huma master for navn, e-post, avdeling (team eller lokasjon per kunde), leder og stillingstittel. Regnskapssystemet for ansattnummer. A07 for fødselsnummer og arbeidsforhold. Brreg/A07 for juridisk enhet (orgnr ulikt tenanten blokkerer koblingen).
- **F-PLA-17:** Kobling i rekkefølge fødselsnummer mot A07 → `connectedIntegrations`-ID mot regnskapets ansatt-ID → `employmentId` mot ansattnummer → koblingskø. Aldri bare e-post. Kildenøkkel = Humas `user.id`.
- **F-MYN-42:** ANS-15 utvides med Huma (aktiv stilling uten A07-arbeidsforhold, motsatt, startdato > N dager, stillingsprosent > 1 prosentpoeng fordi Huma har heltall). Ny ANS-20 «HR-type mot A07» (`Consultant`/`ThirdParty`/`Freelance` i Huma mot ordinært arbeidsforhold i A07).
- **D-Integrasjon / F-SIK-20:** `organizationId`, nøkkelens navn og roller, vilkårsversjon. Veiviseren ber om ny nøkkel med minste leserolle (gamle nøkler fra før september 2026 har Manager over Everyone).
- **MVP:** Webhooks med HMAC, innboks og nattlig full avstemming. Brutto master for arbeidsforhold. Fravær fra Huma (bare webhooks, `absence-export` eller Excel/PAXml; ikke i API-et): mapp sju faste typer, `parentalLeave` og `unpaidTimeOff` som permisjon i a-meldingen, bare `approved` gir lønnseffekt, fraværsavstemming før cut-off. NAV-dubletter: Huma lager sykefravær fra NAV automatisk; NAV-dataene vinner. Bankkonto fra Huma blir forslag som den ansatte bekrefter med BankID (Huma skriver rett inn i Visma.net Payroll, Tripletex, Xledger). Kunder som flytter lønn til Brutto må slå av Humas synk mot gammelt lønnssystem.
- **Vilkår:** Huma har ingen egne API-vilkår, ingen API-pris og ingen konkurranseklausul, men kunden får ikke gi tredjepart tilgang (§ 3.4(a)), en «Contractor» må ikke være konkurrent (§ 2), og Huma kan begrense API-et og slå av integrasjoner uten varsel. Risikoen øker når Brutto bygger HR. Ikke bygg forretningsmodellen på at tilgangen varer.

### Handling (gjøres av et menneske)
- Skriftlig spørsmål til Huma om at kundens nøkkel kan brukes av Brutto som lønnsleverandør, og at Brutto senere vil tilby HR. Ta Humas vilkår (§ 2, § 3.2, § 3.4(a), § 3.5, § 6) med i advokatvurderingen fra N40.
- Finn ut hvor mange i målgruppen og pilotkundene som bruker Huma, og med hvilket lønnssystem.

### Spørsmål til Peter og Sander
1. Huma i fase 1 som kobling som bare henter, og webhooks i MVP?
2. Uten endringsfilter blir det N+1 kall per natt: samtidighet og backoff per tenant? Detaljer bare for endrede brukere, og alt én gang i uka?
3. Toleranse 1 prosentpoeng i ANS-15 for stillingsprosent?
4. Ett webhook-endepunkt per tenant med HMAC-hemmelighet i nøkkelhvelvet og innboks-tabell i MVP?
5. Sjekke `organizationId` og `company.organizationNumber` mot tenantens orgnr før første import, og blokkere ved avvik?

## N19 Personvern, DPIA, databehandleravtale og regelverk

### Endringer i kartleggingen
- **F-SIK-27 (H08, M02):** DPA på grunnlag av EU-kommisjonens standardklausuler for art. 28 (2021/915, innlemmet i EØS). Valg 2 i klausul 7.7 med varsel 30 dager. Tillegg for særlige kategorier, Altinns vilkår, Skatteetatens formålsgrense og KI av til kunden slår den på. **Modell A (standard):** avtale direkte mellom kunde og Brutto; byrået er egen databehandler og bruker. **Modell B (byrålisens):** kunde → byrå → Brutto som underdatabehandler, med kundens forhåndsgodkjenning, samme plikter videre og retur ved byråskifte. Advokat før første kunde.
- **D-Abonnement:** Nye felt `dpa_modell` (`DIREKTE`, `BYRA_UNDERDATABEHANDLER`), `dpa_versjon`, `dpa_akseptert_av`, `dpa_akseptert_tid`, `dpa_fullmakt_ref`. `D-Klient.klientinstruks` versjoneres.
- **F-SIK-23 / D-Underleverandor:** Nye felt `underleverandor_av`, `adresse`, `kontaktpunkt` (EDPB 22/2024), `morselskap_land`. Offentlig liste viser ledd to.
- **F-SIK-23 / F-SIK-24 / D-Lagringssted / H05:** `regnskapsmateriale = sann` krever `land = NO`, også backup og revisjonslogg (meldeplikten etter bokføringsforskriften § 7-5 gjelder også backup i annet EØS-land). Filtre for feilsporing, telemetri og e-post; CI feiler ved utgående endepunkt uten registrering.
- **F-SIK-28:** Referanse-DPIA for produktet (WP248): risikoliste, mal, terskelvurdering, tiltaksvedlegg. Ingen av Datatilsynets 14 listepunkter treffer fase 1, men tre av ni kriterier er oppfylt (ikke fire som N38 talte), så DPIA er trolig påkrevd hos hver kunde. R16–R21 legges til N38s liste. Inn i oppstarten (F-PLA-09) med D-Dokument.
- **F-SIK-07 / F-SIK-08 / F-SIK-19:** Terskel for summer av fagforeningstrekk (R20); antall bidragsytere lagres som flagg. Permisjonsbeskrivelsen forblir kryptert.
- **F-SIK-21 / F-SIK-22 / D-Oppbevaringsregel / D11 (erstatter N38 R9):** Låst avstemmingsrapport er regnskapsmateriale (§ 13 nr. 3) i 60 måneder, med sumutdrag og hash av A07. A07 rå per person: 13 måneder rullerende. Endringsforskriften 29.9.2026 nr. 1933 endrer ikke § 5-6, § 7-2 eller § 7-5; ny § 13 fra 2027 beholder fristene.
- **F-RAP-19 / F-REG-27:** Revisorpakke og avstemmingspakke får sumutdrag og hash.
- **F-PER-02:** Validator etter N19 §8; gammel og ny kontrollsifferregel i D-Regelpakke. Fra 2032 bærer fødselsnummeret ikke kjønn eller århundre.
- **F-ORG-01 / F-ORL-13:** Søk om scope for rolleutskrift når vilkår for bruk som databehandler er bekreftet.
- **F-SIK-30:** Informasjonsmal (art. 14) sier at A07 hentes fra Skatteetaten og hvorfor.
- **MVP:** DPIA oppdateres for lønnskjøring. Exit i modell B ved byråskifte; eksport for 6 måneders elektronisk tilgjengelighet ved avvikling (ny § 7-7 tredje ledd fra 2027). Sikkerhetspakke for Regnskap Norges kontrollskjema. Egne roller og dataklassen `helse` for sykefravær.
- **Senere:** KI via Bedrock EU (AWS EMEA SARL), null lagring, TIA-mal, merking etter art. 50 (KI-omnibus 2026/1744; art. 50 gjelder i EU fra 2.8.2026). Anthropic står ikke på DPF-listen [verifiseres]. Data Act er ikke innlemmet i EØS og gir bare tredjepartstilgang for tilkoblede produkter, så SAF-T fra kunden er veien. Folkeregisteret bare ved behov, med søknad og delegering per kunde.

### Handling (gjøres av et menneske)
1. Advokat: DPA-modell A og B, fullmakt til å godta DPA for kunden, retur ved byråskifte, art. 9 (summer under terskel, foreldrepermisjon), standardklausulene mellom byrå og Brutto. Kan slås sammen med advokatvurderingene fra N17, N30 og N40.
2. Be et pilotbyrå om Regnskap Norges DPA-mal i KS Komplett (godkjenning av system- og driftsleverandører, varsling av kunder).
3. Ta med i revisorintervjuet (N30 §5): holder sumutdrag og hash av A07 for etterkontroll, eller kreves råfila?
4. Send e-post til opendata@brreg.no om rolleutskrift-API på vegne av kunder (vilkår, pris, grenser).
5. TIA for Microsoft Azure: kontraktspart, DPF-status, EU Data Boundary for Norge, supporttilgang fra USA.

### Spørsmål til Peter og Sander
1. Terskel for summer (f.eks. under 3 bidragsytere), og hvor lagres flagget så ingen spørring regner seg tilbake?
2. Sumutdrag ved låsing som egen tabell med hash, så råfila kan slettes etter 13 måneder?
3. Stoppe lønnsdata i feilsporing og OpenTelemetry: filter i koden, i collectoren eller begge?
4. CI-kontroll av at alle utgående endepunkter for logg og telemetri har rad i D-Lagringssted med `land = NO`?
5. Bekrefte at den som godtar DPA kan binde kunden: BankID mot roller i Enhetsregisteret, eller fullmakt i F-BYR-11?
6. Varsel om nye underleverandører 30 dager før: e-post, webhook eller begge? Hvor lagres kvitteringen?
7. Eget flagg for kilden «NAV-testdata» i identifikator-validatoren?

## N29 Ansvarskrav mot arbeidsgiver ved feil trekk

### Endringer i kartleggingen
- **Hjemmel:** Innkrevingsloven § 31 første ledd (samordnet utleggstrekk) og skattebetalingsloven § 16-20 (forskuddstrekk). Trukket, ikke betalt = objektivt ansvar. Ikke trukket = ansvar med omvendt bevisbyrde for aktsomhet (snevert tolket). Ansvar oppstår uten vedtak og innkreves med utlegg etter varsel med minst tre ukers frist. Ansvar for manglende eller feil rapportering (§ 31 andre ledd, § 39 tredje ledd: 20 % av trekkgrunnlaget fra 14 dager etter oppstart) krever vedtak med klagerett. Gamle trekk og bidrag følger opphevede regler med samme mønster [verifiseres]. Paragrafnumrene §§ 23, 28, 30, 31 og § 3 i FOR-2025-07-09-1509 stemmer med Lovdata (N26 spørsmål 8 lukket).
- **Rente:** Fra 1.1.2027 forsinkelsesrente på trukket, ubetalt samordnet trekk (innkrevingsforskriften § 31-1, nå 12,25 %). Forskuddstrekk har rente fra forfall allerede.
- **D-Avvik / D-Kontrollsak:** Nye felt `ansvarsrisiko` (`ingen | mulig | objektiv | rente`), `ansvarsgrunnlag` (kode, f.eks. `innkl-31-1`, `sbl-16-20`), `belop_i_risiko` (Lønnsdata), `rente_fra`. Settes fra metadata på kontrollregelen, versjonert med regelpakken.
- **T5 (kritisk):** Regnes per lønnsutbetalingsdato fra A07 (`sumForskuddstrekkPerLoennsutbetalingsdato`, `datoForUtleggstrekk`) med virkedagskalender, ikke saldo per månedsslutt. Omfatter 2600, 2610–2613 og 2620.
- **Kontrolltekster:** T1, T3, T4, T6, T7, T9, T10 og ANS-01, 02, 04, 11, 18 får ansvarssetning med hjemmel («Kan gi ansvarskrav» / «Trukket, ikke betalt»).
- **D-Regelpakke:** Virkedagskalender, forsinkelsesrentesats per halvår med virkningsdato (12,25 % fra 1.7.2026), datoen 1.1.2027 for § 31-1, § 21 (motregning) og § 4 i FOR-2025-07-09-1509.
- **F-MYN-43 / F-MYN-22:** To nye sensorhandlere `ske-korrespondanse-innkreving-faktura-virksomhet` og `ske-motregning-disponeringsbrev-virksomhet`; `tjeneste` får `dialogporten_innkreving_virksomhet` og `dialogporten_motregning`. Nye saksregler «Brev fra Innkrevingsmyndigheten» (frist 21 dager) og «Motregning» (frist én måned). Byrå klarer seg med `regnskapsforer-lonn`; direktekunder trenger `krav-og-utlegg` eller `ordinaer-post-til-virksomheten` (ikke `lonn`). Bare metadata lagres.
- **Aktsomhetslogg (fase 1):** Tidspunkt Brutto oppdaget hvert brev, varsler, kvitteringer med begrunnelse, A07-hentinger med regelversjon. Lagre både Skatteetatens og Bruttos tidspunkt i UTC.
- **Rettinger:** F-TRK-19 «[verifiseres hjemmel]» → innkrevingsloven § 31 (samordnet) og tvangsfullbyrdelsesloven § 7-22 tredje ledd / skattebetalingsloven § 16-20 slik de lød før 1.1.2026 (gamle). N28 §3.3: aktsomhetsunntaket gjelder bare unnlatt trekk.
- **Kundeavtale (fase 1):** Brutto er kontrollverktøy med begrenset dekning; kunden og byrået eier oppfølgingen [advokat før første betalende kunde].
- **MVP:** T7 blokkerende før godkjenning (overstyring med begrunnelse og fire øyne). T10 blokkerende ved manglende trekk for registrert gammelt pålegg. T9 høy advarsel. Pålegg etter godkjenning gir varsel og lagret hendelse. Ny sakstype «Gammelt trekk etter samordnet startdato» (rutine i natt/funn/N29.md §5). Betalingsforslag viser forfall per trekk; manglende bankbekreftelse første virkedag etter gir kritisk sak med renteestimat (i64 øre, sats i basispunkter). `datoForUtleggstrekk` alltid fylt.
- **Ny F-id: F-TRK-29 «Trekkdokumentasjon og aktsomhetslogg»:** Eksport per ansatt og periode med hele kjeden (pålegg, henting, beregning, betaling, rapportering, avvik, kontakt med Innkrevingsmyndigheten), bare med lønnstilgang og logget lesing.

### Handling (gjøres av et menneske)
- Ta med i henvendelsen til Skatteetaten: hvilken Altinn-ressurs og dialogtittel brukes for krav etter § 31, kommer varsel før kravet, svarfrist; rutine for gammelt trekk tatt etter samordnet startdato (omfordeling, tilbakebetaling, retting, kode); renteberegning (dagkonvensjon, minstebeløp, sats).
- Advokat: avtalemal for ansvarsfordeling og ansvarsbegrensning (direktekunde og byrålisens; utkast trengs før første kunde), aktsomhetsunntaket i praksis (systemfeil, feil hos regnskapsfører, sene brev), ansvarsregler for gamle trekk og bidrag, og oppbevaring av aktsomhetsloggen (foreldelsesloven § 9).

### Spørsmål til Peter og Sander
1. Ansvarsrisiko som metadata på kontrollregelen (`const ANSVAR`, `const HJEMMEL`), versjonert med regelpakken?
2. Virkedagskalender i Rust, lokal og deterministisk (påske), med egenskapstester for månedsskifte og påske?
3. Rente i i64 øre, sats i basispunkter, dager som heltall, én avrunding til slutt?
4. Aktsomhetslogg som hendelser per trekkpålegg med hash-kjede fra F-SIK-15: holder D-Revisjonslogg og en visning, eller egen D-id?
5. To nye sensorhandlere som aldri kaller `GET /dialogs/{id}`: kan tittelen klassifiseres uten å lagre navn?
6. Kan T5 per forfallsdato hente posteringsdato på 2600/2610–2620 fra Tripletex, PowerOffice og ReAi, og hvordan ser T5 ut uten bankdata i fase 1?

## N20 Tariffdata og AGA-sonetabell

### Endringer i kartleggingen
- **L-16 (F-REG-30, F-MYN-39, F-ORG-03) i to trinn:** (1) kommunenummer fra Brreg-adressen → D-Sonedel for året (sikkert for 345 av 357 kommuner); (2) for 12 delte kommuner (soner følger grunnkretser) geokodes adressen med Kartverkets adresse-API og sonen slås opp i Geonorge-WMS (`GetFeatureInfo`) eller lokalt i polygonene (CC BY 4.0). Utfall `OK`, `AVVIK`, `UAVKLART` (ny i D-Avstemmingslinje), `IKKE_RELEVANT`.
- **L-16 fribeløp:** Spart avgift per juridisk enhet hittil i år fra A07-grunnlag og sats; varsel nær 850 000 kr (2026; forslag 2027 uendret). Avkortes med annen bagatellmessig støtte. Uten D-Konsern blir kontrollen `UAVKLART` for mulige konsern.
- **D-Kommune / ny D-Sonedel:** Importer Skatteetatens kommunekatalog (CSV bak Datawrapper, 370 rader for 2026) for 2026 og tilbake til minst 2023, med Klass-korrespondanse for 2024-numrene. Kilde-URL, hash og hentetidspunkt i D-Kilderegister. Kommuneendringer fra SSB Klass 131 (`/changes`); neste 1.1.2028 (Vest-Lofoten, Gran).
- **D-Regelpakke:** `kodeliste_versjoner` får sonetabell- og geometriversjon.
- **D-Underenhet:** Nye felt `koordinat` og `sone_kilde`; sone vises per underenhet i ansattoversikten.
- **F-LON-19 / C-beregning §8 (rettes):** Statens hovedlønnstabell (A-tabellen) falt bort 1.5.2024; lønn i staten angis i kroner. F-PER-26 (lønnstrinn i a-meldingen for staten) må vurderes.
- **F-ORG-04 / F-KJO-13 (rettes):** Fribeløpet gjelder også sektorunntatte og vanskeligstilte i sone Ia–V. Fordeling i konsern via annen bagatellmessig støtte i januar.
- **Tariff:** Ingen store tariffområder publiserer lønnstabeller maskinlesbart i 2026 (Virke HUK, KS, Spekter, NHO, Fellesforbundet: PDF; NHO-avtaler som tekst på Lovdata; Virke hadde Excel til 2023). Ingen offentlig dokumentasjon av ferdig tariffbibliotek hos SD Worx, Visma eller Huldt & Lillevik [verifiseres].
- **MVP:** AGA-satser som matrise (sone × beregningskode) i D-Sats, fribeløp per konsern med løpende forbruk, overgang til 14,1 % fra riktig måned. D-Konsern med fordeling av fribeløp. **F-LON-19:** Kuratert bibliotek for Virke HUK § 27 og § 26 (2026) først; KS-garantilønn hvis pilotkunder trenger det; andre avtaler via CSV/JSON-import (F-LON-28). F-LON-12/20: begge opprykksregler. F-LON-29/F-KJO-26: retro fra virkningsdato. **Ny D-Tariffpakke** med signering, hash og arv som D-Regelpakke.
- **Senere:** Flere bibliotek (NHO Geneo, KA, Spekter, Industrioverenskomsten), kontroll mot allmenngjort minstelønn (Lovdatas åpne forskriftspakke), beredskap for nytt sonekart fra 2028.

### Handling (gjøres av et menneske)
- Les KS HTA kap. 4 på ks.no/hta manuelt (automatisk lesing ble blokkert): tabellstruktur, ansiennitetstrinn, om tillegget legges til individuell lønn.
- Kartlegg pilotkundenes tariffavtaler (HUK § 26/§ 27, NHO Geneo-avtalenummer, KA, Spekter, egne). Avgjør rekkefølgen i biblioteket.
- Senere: avklar rett til å videreformidle partenes tabeller (Virke, NHO/Lovdata, KS) i et kommersielt bibliotek, og fribeløp i konsern mot Støtteregisteret.

### Spørsmål til Peter og Sander
1. Punktoppslag via WMS `GetFeatureInfo` eller lokalt point-in-polygon i Rust (`geo`) for de 12 kommunene? CC BY 4.0 krever kildeangivelse.
2. Hentejobb for Datawrapper-CSV (versjonsnummer i URL-en): finn URL fra Skatteetaten-siden, lagre øyeblikksbilde og hash, varsle ved kolonneendring?
3. Sonen i egen D-Sonedel, eller eget felt for delområde på D-Kommune?
4. D-Tariffpakke med samme motor som D-Regelpakke, men egen tabell?
5. Verktøykjede for PDF → CSV og kontroll med fire øyne i grensesnittet; kilde-PDF som D-Dokument?
6. Én felles synk for referansedata (Brreg, Klass, Geonorge, Skatteetaten) med alarmer og «sist verifisert» i grensesnittet?

## N33 Bilag til regnskapssystemene

### Endringer i kartleggingen
- **F-REG-29 / F-REG-01:** Business NXT: saldo, debet og kredit fra `generalLedgerBalance`, grupperingskode fra `generalLedgerAccount.groupingCode` (rett N04-tabellen). Uni Micro: debet/kredit fra `/api/statistics`, ingen grupperingskode (`grupperingskode_kilde = brutto_tabell`). Xledger: debet/kredit fra transaksjonene (5 000 kall per entitet per måned; aggreger i få kall).
- **D-Regnskapskonto:** Nye felt `mva_laast` og `tillatte_mva_koder` (Tripletex `vatLocked`/`vatTypeIds`). Dimensjonskrav fra NXT, Uni Micro og eAccounting. `reskontro` får `leverandoer_per_ansatt` (Xledger, Uni Micro).
- **F-REG-30 (salgsargument):** Tripletex' avstemmingsmodul henter a-meldinger fra Tripletex selv og gir avvik for kunder med eksternt lønnssystem; Tripletex anbefaler manuell avstemming. Årsoppgjør virker uansett bilagstype.
- **D-Integrasjon:** Xledger-token per domene med `X-XL-Owner-To-Run-As`, Uni `CompanyKey` per selskap, NXT `customerNo` og tjenestebruker per selskap.
- **F-REG-17 (bilagskontrakt, MVP):** Hver linje: `mva_kode`, `netto`, `mva_beloep`, `brutto` (adapteren velger grunnlag: brutto i Tripletex/PowerOffice/ReAi, netto i Fiken), `posteringsdato`, `tekst` (≤ 50 tegn), `reskontro_type`, `motpart_ekstern_id`. Ikke mengdefelt.
- **F-REG-05 / D-Bilag `ekstern_referanse`:** Kort, stabil kjøringsreferanse ≤ 20 tegn (f.eks. `BR-2026-0042-r1`), ikke `payrun:<uuid>:rev<n>` (48 tegn).
- **F-REG-23 / D-Bilag (utboks):** «Slå opp før skriv» for systemer uten innebygd nøkkel (Fiken, eAccounting, 24SevenOffice, NXT, Uni Micro, ReAi). Bare Tripletex (`externalVoucherNumber`), PowerOffice (`ExternalImportReference`) og Xledger (`X-XL-Idempotency-Key`) har nøkkel. Nytt felt `idempotens_metode` (`native_noekkel`, `oppslag`).
- **F-REG-05 / F-RAP-13 (AGA):** Ingen system har AGA-grunnlagsfelt uten kundeoppsett. AGA per (sone, sats) som egen linje med grunnlaget i teksten (`AGA <sone> <sats>% gr <beløp>`); i Fiken eget `journalEntry`.
- **F-UTL-22/23 (MVA):** Tripletex, PowerOffice, Fiken og ReAi godtar inngående MVA på linjer; havner på kode 1, 11, 13 uansett bilagstype. Kontroll før sending: kontoen godtar koden; MVA-kontoer brukes aldri direkte (ReAi sperrer 2700–2714).
- **F-REG-18 (Tripletex):** Send med `voucherType=null` eller egen type, ikke «Lønnsbilag» (`:reverse` støtter ikke lønnstransaksjoner). `:closePostings` etter bokføring i flyt A. Gi kunden beskjed om avstemmingsmodulen.
- **F-REG-19 (PowerOffice):** `Vouchers/ManualJournals` med `ExternalImportReference`, `SaftSourceId`, `SaftBatchId` som standard; utkast (`JournalEntryVouchers`) som valg (`bilagsmodus`). `PostingDate` per linje. Flyt A virker ikke uten felles `CustomMatchingReference`; bruk B eller C.
- **F-REG-22 (Fiken):** Bruttos bilag får `transactionType` «Fri», så F-REG-24 må matche på bilags-id. Ingen ansattreskontro → flyt C.
- **Ny F-REG-ReAi:** `POST /api/manual-vouchers` med `vatCode` på alle linjer, PDF-vedlegg, lukking med `postings/employee/close`, oppslag før skriv (ingen ekstern referanse).
- **F-REG-20 (Xledger):** `addGLImportItems` med `jobLevel` 2 eller 1, `X-XL-Idempotency-Key`, `extIdentifier`, `glObject1–5` per kunde; ansatt som leverandør i `Employee.subledger`.
- **F-REG-21 (Visma):** NXT `batch_create` → validering → `updateBatch`, ingen reversering via API (motbilag). eAccounting alltid via `voucherdrafts` + `convert`; bilag kan ikke slettes.
- **F-REG-28:** Ingen system har minste gruppestørrelse per dimensjon (bare Tripletex' skjuling av hele bilaget). Brutto må aggregere grupper med én eller to ansatte selv.
- **F-REG-10:** Reversering via API i Tripletex, PowerOffice, ReAi og Uni Micro; motbilag med gjensidig referanse i NXT, eAccounting, Fiken og 24SevenOffice.
- **Senere:** 24SevenOffice REST (ansatt som dimensjon 3, ingen reskontro/utkast/nøkkel). Uni Micro som én adapter (utkast, `ExternalReference`, lukking, ansatt med fødselsnummer og `SubEntity`). SAF-T 1.40-delfil som dokumentasjon til Skatteetaten (modell B), ikke kanal inn i regnskapssystemene.

### Handling (krever ja fra Sjur)
- ReAi-test i tenant 2915: manuelt bilag mot 2930/2940 uten `employeeId`, lukking og sletting. Agenten testet ikke, fordi ReAi-skillen krever eksplisitt ja i sesjonen før hver skriving, og tenanten har ingen lønnsposteringer. Avgjør formatet på F-REG-ReAi.
- Ta med i N40-henvendelsen til PowerOffice: gir de ManualVoucher_Full og Import_Full til et konkurrerende lønnssystem?

### Spørsmål til Peter og Sander
1. Én tilstandsmaskin for bilag (klar, sendt, bokført, feilet) med strategiene `native_noekkel` og `oppslag`. Hvordan søke trygt uten nøkkel (tekstprefiks i NXT `reference`, Fiken-beskrivelse, ReAi `description`, eller bare lagret id)?
2. Kjøringsreferanse ≤ 20 tegn: unik per tenant eller per juridisk enhet?
3. Kontrakt med netto, MVA og brutto per linje; `rust_decimal` med øresavrunding per linje, så summen stemmer i Fiken der MVA beregnes av systemet?
4. Vedlegg som én aggregert PDF per bilag (ReAi avviser CSV/XLSX; NXT 15 MB, Xledger 64 MB), CSV bare i Brutto?
5. `bilagsmodus` (utkast/bokført) per kunde; status BOKFØRT først når regnskapet har bokført, også ved langvarige utkast?

## N34 Finansiørkrav

### Endringer i kartleggingen
- **ADR: Brutto er underreskontroen for prosjektlønn.** Ingen finansiør krever ansatt i hovedboken. De krever prosjektregnskap som finnes igjen i regnskapet og underlag per person som revisor kan avstemme mot hovedbok, lønnssystem og timesystem (EUs CFS-mal). Samlebilag med prosjekt på alle personalkostnadslinjer og låst spesifikasjon per person fra Brutto holder [verifiseres i revisorintervjuene].
- **D-Tilskuddsprofil (lås nå, ingen funksjoner i fase 1):** n:1 til prosjekt; finansiørfeltene flyttes hit fra D-Dimensjonsverdi; `kostnadsmetode` = `nfr_faktisk`, `nfr_institutt_kategori`, `promille_sjablong`, `eu_dagsats_215`, `faktisk_kost`, `fast_sats`. Nye felt `aarsverk_timer` (1 695/1 600), `signering`, `tak_gjelder`, `stotteberettigede_lonnsartgrupper`, `oppbevaring_aar_etter_slutt`, `rapportert_til`.
- **D-Regelpakke:** Satsene (1,2 promille, 700 kr, 1 100 kr, 1 695, 215) som data. **Rettes:** SkatteFUNN og Innovasjon Norge bruker 1,2 promille med tak 700 kr, ikke 1,6 promille. Forskningsrådets 0,8–1,1 promille gjelder bare budsjettet; institutter bruker godkjente satser per stillingskategori.
- **D-Stilling:** Nytt felt `stillingskategori_finansior` med gyldighet.
- **D-Oppbevaringsregel:** Ny klasse `prosjektdokumentasjon`: 10 år etter prosjektets sluttdato (Forskningsrådet), foran de vanlige 60 månedene. Med i eksporten ved opphør (F-SIK-26).
- **F-REG-29:** Saldo per konto, måned og prosjekt for 5000–5999 når kunden har prosjekter med tilskuddsprofil.
- **MVP:** Alle personalkostnadslinjer i lønnsbilaget får prosjekt og dimensjoner, også feriepengeavsetning, AGA, AGA av feriepenger og forsikring; `aggregering` slår aldri sammen dimensjonskombinasjoner. **F-REG-14 nytt:** OTP-fordelingsbilag per termin etter pensjonsgrunnlaget (avklares mot S #29). F-REG-24 avstemming per prosjekt, konto og måned; null differanse før en finansiørrapport låses. Største rest-avrunding riktig per prosjekt. F-TID-25: kostnad følger arbeidsmåneden [verifiseres med revisor]. Omfordeling respekterer `rapportert_til`.
- **Senere:** Prosjektlønnsrapport per prosjekt, finansiør, periode og person (F-RAP-29, F-TID-27, F-ORG-21), låst med hash. Kontroller L-P1–L-P9 (timetak, dagsekvivalenter, timer på fraværsdager, lønn i A07, timer etter slutt, sats over tak, ikke-støtteberettigede lønnsarter, manglende signaturer, spesifikasjon = hovedbok per prosjekt). Timeark med to signaturer (F-TID-26). Eksport per finansiør (Forskningsrådet, EU/CFS, SkatteFUNN/RF-1053, Innovasjon Norge, generisk ISRS 4400). Grunnlag for instituttenes timesatser. Rolle «prosjektøkonom». Ansatt i hovedboken som smalt tilvalg (`D-Regnskapsoppsett.ansattdimensjon = prosjektlinjer`), bygges først når betalende kunde krever det.
- **Konkurrenter:** De priser timer med kostpris, ikke faktisk lønnskost; ingen har ferdig finansiørrapport.

### Handling (gjøres av et menneske)
- Ta med prosjektrevisjon i revisorintervjuet (N30 §5): holder samlebilag + spesifikasjon fra Brutto for SkatteFUNN, CFS og ISRS 4400? Hvilken måned bærer kostnaden? Godtas elektronisk signatur på timeark?
- Senere: be en kunde vise Forskningsrådets prosjektregnskapsskjema på Mitt nettsted; spør to eller tre forskningsinstitutter hvordan de beregner timesatser.

### Spørsmål til Peter og Sander
1. Største rest på to nivåer: Σ D-Linjekontering per prosjekt lik bilagslinjen per prosjekt til øret, også for AGA og feriepenger?
2. Rapportlås i bitemporal modell: hvordan hindrer `rapportert_til` at tilbakevirkende kostnadsfordeling endrer en sendt rapport?
3. Beregningsmotor per `kostnadsmetode` som ren funksjon med gylne caser (Forskningsrådet 800 000 kr → 1 128 388 kr / 666 kr/t; SkatteFUNN 415 000 × 1,2 ‰ = 498 kr/t; EU deltid 215/12)?
4. Godkjenningsspor ved timeimport (Tripletex `MonthlyStatus.approvedBy`/`approvedDate`) i D-Godkjenning uten å kopiere timesystemet?
5. `ansattdimensjon` som tilvalg: konsekvens for bilagskontrakt, linjeantall og feltgrenser?
6. Rollen «prosjektøkonom» med radnivåtilgang via D-Prosjektdeltakelse i samme policymodell?
7. 10 års oppbevaring for prosjektdata mot arkivabonnement på 5 år: egen lagringsklasse og slettejobb?
