# R2 – Byråkanalen: behov, prioriteringer og standpunkter

**Dato:** 28. oktober 2026
**Runde:** 2 av flerrunders behovskartlegging (runde 1 = fakta, filene A–G)
**Status:** Revidert versjon etter runde B (selvkritikk). Endringene står i kapittel 4.4.
**Produkt:** Frittstående lønnssystem (SaaS) for virksomheter med 10–1000 ansatte, også lisensiert til regnskapsbyråer som kjører lønn for kundene sine.

---

## Leseveiledning

**Kildehenvisninger**
- **[E§1.3]** = E-byra.md, kapittel 1.3. Tilsvarende **[B§…]** myndigheter, **[A§…]** marked og konkurrenter, **[C§…]** beregning, **[D§…]** praksis, **[F§…]** arkitektur og **[G§…]** moduler.
- **[Tally-grensesnitt]** = observasjon av verktøyene som praksissystemet Tally eksponerer i denne økten (bare verktøynavn og -beskrivelser, ingen kundedata er lest).
- **[ans.]** = eget anslag eller egen vurdering. Regnestykket står oppgitt der det finnes.

**MoSCoW og tidshorisont.** Tidslinjen følger F, ikke E: pilot med parallellkjøring i oktober–desember 2027 og første produksjon i januar 2028 [F§9.7].
- **Må** = på plass før første byrå går i produksjon (januar 2028).
- **Bør** = innen 12 måneder etter det (2028).
- **Kan** = senere, når etterspørselen er dokumentert.
- **Ikke nå** = bevisst valgt bort (se også kapittel 7).

**Eksempelbyrået** brukes gjennom hele dokumentet [ans.]:
- Regionalt, uavhengig byrå med ca. 90 ansatte.
- Lønnsavdelingen har 15 lønnsmedarbeidere, ca. 800 lønnsklienter og ca. 9 000 lønnsslipper i måneden.
- Lønn står for ca. 15–20 % av byråets omsetning, mot 11 % i bransjen som helhet [E§7.1].
- Byrået bruker i dag tre lønnssystemer: kundens Tripletex eller PowerOffice Go for de små klientene, Visma Payroll for de mellomstore og SD Worx Byrå for to store klienter.

---

## 0. Sammendrag – de tolv viktigste konklusjonene

1. **Byrået kjøper minutter per lønnsslipp, ikke funksjoner.** Byrået går i null ved ca. 15 minutter per slipp [E§5.3]. 60–75 % av tiden går til å hente inn og purre på grunnlag og til kontroll og avviksanalyse, ikke til beregning [D§1.4]. De to høyest rangerte behovene er derfor **strukturert lønnsgrunnlag inn** og **avviksbasert kontroll med forklaring**. Klientdashbord og maler kommer etter.
2. **Tidslinjen må være realistisk.** E foreslår produksjon i januar 2027. Produktet blir tidligst klart i januar 2028 [F§9.7]. Da har alle konkurrenter systembruker for klientsystem, så **Altinn 3 er hygiene innen vi lanserer, ikke et salgsargument**. Det som skiller oss ut, er hvor enkelt oppsettet og feilsøkingen av klienttilgangen er.
3. **Systembruker for klientsystem:** Én per byrå (juridisk enhet). Tilknytning og diagnose av klienter bygges som en produktfunksjon. Samlekjøringer brukes fullt ut for henting (skattekort, tilbakemeldinger, avstemming). Innsending skjer bare som «send alle som er klare», med en port per klient. **Det blir ingen blind massesending av a-meldinger.**
4. **Vi bygger en arbeidskø, ikke et porteføljesystem.** Praksissystemet eier allerede frister, oppgaver, timeføring, fakturagrunnlag og lønnsomhet. Tally har alle disse [Tally-grensesnitt]. Vi skal *mate* praksissystemet med lønnsstatus og bruksdata, ikke konkurrere med det.
5. **Kundeportalen er et Må, men skal være minimal.** Den skal ha innsending, godkjenning og spørsmål knyttet til avvik, uten innloggingsfriksjon. Tiden spares bare hvis kundene faktisk bruker portalen. Derfor trengs også en dokumentert reservevei (godkjenning på e-post eller fullmakt i oppdragsavtalen).
6. **Det er kunden som «trykker betal»** [E§1.3]. Én godkjenning skal dekke hele betalingssettet: netto lønn, forskuddstrekk til forfall første virkedag etter utbetaling med KID, og utleggstrekk [B§4]. Byråer med fullmakt støttes med arbeidsdeling som systemet håndhever. Vi rører aldri pengene.
7. **Ansvarsgrensen:** Vi selger programvare med en beregningsgaranti som har et tak. Vi tilbyr ikke lønn som tjeneste og driver ikke BPO, heller ikke «bare i januar». Det er samtidig salgsargumentet, fordi SD Worx har startet sin egen tjenesteenhet [A§2.1].
8. **Lisens:** Standarden er at byrået betaler per lønnsslipp. Det er ingen pris per byråbruker, og prisen har volumtrinn og et årlig tak. Per klient kan byrået i stedet velge at sluttkunden betaler. For partneren betyr **kanalbeskyttelse og en exit-pakke** mer enn 50 % lisensmargin.
9. **Migrering skjer i bølger etter en porteføljeanalyse.** Byråets egen lønn går først, deretter de enkle klientene. A-melding-XML og avstemmingsdata fra Skatteetaten er fasiten [F§6.2]. Byrået får en ferdig samtykkepakke å sende til klientene om ny databehandler og ny Altinn-tilgang.
10. **Kvalitet:** Byrået trenger oppdragsdokumentasjon som det eier selv og kan oppbevare i 5 år, også etter at klienten har gått [E§2.1, §5-3]. Lite tyder på at konkurrentene løser dette godt [ans.]. Det er billig å bygge når revisjonsloggen allerede finnes.
11. **Kjedene:** Bygg hierarkiet i datamodellen nå, og selg til kjedene senere (år 2–3). Full white-label kommer ikke nå.
12. **Sweet spot er klienter med 10–300 ansatte.** Klienter med under 10 ansatte kjører lønn i kundens Tripletex eller PowerOffice der lønnsmodulen allerede er betalt. Dem flytter vi ikke i år 1. Et dashbord som bare viser halve porteføljen, må derfor levere status til praksissystemet for å bli brukt.

---

## 1. Personas: kontekst, jobber, smerter og behov

### 1.1 Persona 1 – Lønnskonsulenten i byrå (60 klienter)

**Kontekst [ans., basert på E§1.2, D§1.4]**
- Hun har 60 klienter med 2–400 ansatte:
  - 30 klienter under 10 ansatte (ca. 120 slipper)
  - 24 klienter med 10–29 ansatte (ca. 340 slipper)
  - 5 klienter med 30–60 ansatte (ca. 200 slipper)
  - 1 klient med ca. 400 ansatte, som hun deler med en kollega (kollegaen kjører, hun kontrollerer)
- Totalt kjører hun **ca. 660 lønnsslipper i måneden**.
- Lønnsdatoene er spredt: den 10. (4 klienter), den 15. (6), den 20. (22), den 25. (18) og siste virkedag (10).
- Klientene bruker fem regnskapssystemer: Tripletex (28), PowerOffice Go (17), Visma eAccounting eller Business NXT (9), Fiken (4) og Xledger (2).
- Hun bruker ca. 140 timer i måneden på lønn, altså **ca. 13–14 minutter per slipp** alt inkludert. Det er nær byråets nullpunkt [E§5.3].

**Jobs to be done**
- «Få riktig lønn ut til riktig tid for alle klientene uten å jobbe overtid i lønnsuka.»
- «Vite til enhver tid hvilke klienter som venter på meg, og hvilke jeg venter på.»
- «Finne de fem lønnsslippene som er feil, ikke se gjennom alle 300.»
- «Få a-meldingen godkjent uten avvik, og forstå avviket når det kommer.»
- «Overta en kollegas klient på kort varsel uten å lete i e-posten hennes.»

**Dagens smerter**

| Smerte | Kilde |
|---|---|
| Grunnlaget kommer på e-post, i Excel eller som PDF. 30–40 % av tiden går til å hente inn og purre | [D§1.4], [E§1.2] |
| Tripletex tillater bare én import før det oppretter en ny kjøring. Det blir mye manuell registrering | [E§9.2], [A§5.3] |
| Kontrollrapportene er laget for utskrift. Sammenligningen med forrige måned gjøres i Excel | [D§1.3], [D§8.3] |
| Retroføring i Visma Payroll gir avstemmingsproblemer i skattetrekk og AGA | [E§9.2] |
| Citrix i SD Worx er tungvint ved import og oppdatering for flere selskaper | [E§9.2] |
| Hun må veksle mellom tre lønnssystemer og fem regnskapssystemer | [E§1.4] |
| A-meldingsavvik oppdages først etter innsending. Feilkodene er kryptiske | [D§8.3], [G§DEL 3 #15] |
| **Nytt fra 2026:** Forskuddstrekket forfaller første virkedag etter *hver* lønnsutbetaling, med KID og som eget betalingsoppdrag. Før gikk dette annenhver måned via skattetrekkskontoen | [B§4], [D§0 pkt. 4] |
| **Nytt fra 2026:** Uten riktig Altinn 3-delegering får systemet 403/`AMLD_1063` på lønnsdagen | [B§2.2], [B§14 pkt. 2] |

**Behov**

| ID | Behov | MoSCoW | Begrunnelse og kilde |
|---|---|---|---|
| **BY-01** | **Arbeidskø på tvers av egne klienter.** Én liste over kjøringer sortert etter neste handling og frist. Status per steg: *grunnlag mottatt → kontrollert → godkjent av kunden → betalingsforslag levert → betaling bekreftet → a-melding OK → bokført*. Frister beregnes eksakt: lønnsdato, bankens avskjæringstid, forskuddstrekk T+1, a-melding den 5. flyttet ved helg og AGA-termin | Må | GRFS 7.8 [E§2.2]. Kø i stedet for dashbord, se kap. 2.2 |
| **BY-02** | **Strukturert lønnsgrunnlag inn.** Forhåndsutfylt innsendingsskjema for kunden (BY-42), import fra tids- og vaktsystemer, Utleggsappen og Tikket via felles grunnlagskontrakt [G§0 pkt. 4], og Excel- og CSV-import med *lagret mapping per klient*. Flere importer per kjøring, idempotent og med forhåndsvisning | Må | Den største tidsposten [D§1.4]. Tripletex-kritikken [E§9.2] |
| **BY-03** | **Ustrukturert grunnlag tolket med KI.** E-post, Excel med kundens eget format eller PDF videresendes til klientens innboks. KI foreslår lønnslinjer med kildehenvisning, og lønnskonsulenten godkjenner | Bør | De fleste små kunder vil fortsette med e-post [ans.]. KI forbereder og godkjenner aldri [F§0 pkt. 9] |
| **BY-04** | **Avviksbasert kontroll.** Standard kontrollpakken [D§1.3] med terskler fra byråmalen og lokale justeringer per klient. Bare avvik vises. Hvert avvik må kvitteres («forventet», «drøftet med kunden», «rettet»), og kvitteringen blir GRFS-dokumentasjon | Må | GRFS 7.2 [E§2.2]. Kontroll er 25–35 % av tiden [D§1.4]. Wow #1 [G§DEL 3] |
| **BY-05** | **Klartekstforklaring av differanser** mot forrige måned per ansatt, avledet fra beregningsgrafen og ikke generert fritt. Eksempel: «−3 412 kr netto fordi …» | Må | [G§2.4] «må ha 2026». [F§1.9] |
| **BY-06** | **Ubegrenset testkjøring og retro.** Reberegning uten låsing, og tilbakevirkende endringer med automatisk differanse for skattetrekk og AGA per måned og forklaring linje for linje | Må | Største klage mot Visma Payroll [E§9.2]. [C§5] |
| **BY-07** | **Samlekjøring av skattekort.** Endringspolling for alle *aktive* arbeidsforhold på tvers av klienter, og årsskiftebestilling for alle klienter i desember. Arbeidsgiver oppgis per bestilling (`FOR_004`), og det er maks 1 000 fødselsnumre per kall. Systemet varsler om manglende skattekort. Det henter **ikke** skattekort for personer som har sluttet, fordi den skattepliktige får varsel | Må | [B§3.1]. GRFS 7.4 [E§2.2] |
| **BY-08** | **A-melding uten drama.** Forhåndsvalidering mot gjeldende forretningsregler (F532 og F530 fra 2027-01) før innsending. «Send alle som er klare» gjelder bare klienter med godkjent kjøring og kvitterte kontroller. Tilbakemeldinger hentes automatisk. Avvikslisten går på tvers av klienter, med klartekst og forslag til retting | Må | [B§2.2–2.3], [B§12]. Wow #15 [G§DEL 3]. GRFS 7.8 |
| **BY-09** | **Lønnsbilag til klientens regnskapssystem.** Mapping arves fra byråmalen, status «bokført» kommer tilbake, og fil brukes som reserve. Ved lansering: Tripletex, PowerOffice Go og én Visma-variant. Senere: Fiken, Xledger og Finago | Må (3 systemer) / Bør (resten) | [E§4 krav 10], [G§1.11 B4] |
| **BY-10** | **Fristvarsler** på e-post, Teams eller i appen: kunden har ikke sendt grunnlag innen fristen, kunden har ikke godkjent innen T-x, a-meldingen er ikke sendt den 3., forskuddstrekket er ikke bekreftet betalt T+1, og AGA-terminen nærmer seg | Må | [F§8.2], [B§4] |
| **BY-11** | **Ekstrakjøringer, sluttoppgjør og korrigeringskjøringer** som ikke forstyrrer hovedkjøringen. A-meldingen samles per opplysningspliktig og måned, og erstatningsmelding lages automatisk | Må | [F§0 pkt. 3], [B§2.4] |
| **BY-12** | **Rask veksling mellom klienter**, søk og tastatursnarveier. Ingen Citrix. Samme skjermbilde for alle klienter. Ytelse: én kjøring med 1 000 ansatte under 10 s (p95) | Må | [E§9.2], [F§1.11] |
| **BY-13** | **Klientinstruks i kjøringen.** Særregler, kontaktperson og «husk at …» vises der arbeidet gjøres. Instruksen kan hentes fra praksissystemet | Bør | Overlevering ved fravær (BY-17). Tally har kundeinstrukser [Tally-grensesnitt] |
| **BY-14** | **Ansattapp med lønnsslipp og «forklar lønnsslippen»**, slik at klientens ansatte spør lønnskonsulenten sjeldnere | Bør | Henvendelser er 5–10 % av tiden [D§1.4]. Wow #4 og #7 [G§DEL 3] |
| **BY-15** | **Tilknytning og tilgangsdiagnose for systembruker per klient.** «Legg til klient» knytter også klienten til byråets klientsystem-systembruker via API. Status per klient: tilknyttet, riktig tilgangspakke og tilgang mistet. Feilkoder forklares i klartekst. Når kunden selv må delegere (oppdrag med bare lønn, der byrået ikke er registrert regnskapsfører), får byrået en ferdig instruks å sende kunden | Må | [B§1.2], [E§3.1–3.4], [B§14 pkt. 2]. Wow #14 [G§DEL 3] |

**Hva som er «kult» i 2026**
- Ferdig forhåndsberegnet lønn: kjøringen regnes ut på nytt hver gang nytt grunnlag kommer inn, så «beregn» på lønnsdagen er bare en bekreftelse [F§1.11 pkt. 6].
- En avvikskø der hvert avvik har en forklaring i én setning og et forslag til handling.
- KI som gjør kundens hjemmesnekrede Excel-ark om til lønnslinjer på sekunder (BY-03).

**Suksessmål**

| Mål | I dag [ans.] | Mål etter 6 mnd i produksjon |
|---|---|---|
| Minutter per lønnsslipp (all byråtid på lønnsoppdraget delt på antall slipper) | 13–14 | **≤ 8** |
| Klienter per lønnskonsulent uten overtid i lønnsuka | ca. 60 (med overtid) | **≥ 85** |
| Andel lønnsgrunnlag mottatt strukturert (portal, integrasjon eller lagret import) | < 20 % | **≥ 70 %** |
| Presisjon i avvikslisten (andel avvik som krever handling) | ikke målt | **≥ 50 %** |
| A-meldingsavvik der årsaken er systemet | ukjent | **0** |
| Overtid i lønnsuka | 8–12 t per måned | **≤ 2 t** |

---

### 1.2 Persona 2 – Leder for lønnsavdelingen (15 lønnsmedarbeidere)

**Kontekst [ans.]**
- Hun leder lønnsavdelingen i eksempelbyrået: 15 medarbeidere, ca. 800 klienter og ca. 9 000 slipper i måneden.
- Hun har ansvar for kapasitet, kvalitet og lønnsomhet per klient. Hun er gjerne også fagansvarlig for lønn og den som vurderer systembytte [E§10.2].
- Det er vanskelig å rekruttere, fordi faget har nær 4 000 personer på landsbasis og 80 % er kvinner [E§7.1].

**Jobs to be done**
- «Fordele klientene slik at ingen drukner rundt den 20.»
- «Se tidlig hvor det brenner: hvilke kunder som ikke har godkjent, og hvilke avvik som er åpne.»
- «Få en nyansatt produktiv på uker, ikke måneder.»
- «Vite hvilke klienter som tar mer tid enn fastprisen dekker.»
- «Innføre én standard for hele avdelingen i stedet for 15 private varianter.»

**Dagens smerter**

| Smerte | Kilde |
|---|---|
| Tre lønnssystemer gir tre opplæringsløp og ingen felles oversikt | [E§1.4], [E§9.1 pkt. 3] |
| Status ligger i hodet og innboksen til hver medarbeider. Sykdom på T-3 gir kaos | [ans.] |
| Lønnsomhet per klient krever korrekt timeføring, og den føres etter hukommelsen | [ans.]. Tally regner effektiv timepris per klient [Tally-grensesnitt] |
| Lønnsarter og kontoplanmapping er satt opp ulikt hos hver klient. Det finnes ingen arv | [E§4 krav 5], [A§6.1 pkt. 4] |
| Support fra leverandøren er svak i lønnsuka (SD Worx) | [E§9.2] |

**Behov**

| ID | Behov | MoSCoW | Begrunnelse og kilde |
|---|---|---|---|
| **BY-16** | **Avdelingsoversikt:** alle kjøringer per lønnsdato og status, flaskehalser (kundegodkjenninger som venter, åpne a-meldingsavvik, tapt Altinn-tilgang) og belastning per medarbeider de neste 10 dagene | Må | [F§2.2 Byråkonsoll], [D§8.3 «Byrå: mange klienter»] |
| **BY-17** | **Tildeling, stedfortreder og masseomfordeling.** Hver klient har en primæransvarlig og en stedfortreder. Ved fravær omfordeles klientene med ett grep, og kontekst, notater og historikk følger med | Må | Stor driftsrisiko i dag [ans.] |
| **BY-18** | **Byråroller og tilgang per oppdrag:** lønnskonsulent, kontrollør/oppdragsansvarlig, avdelingsleder og byråadministrator. Tilgang følger tildelte klienter. Ingen får tilgang til persondata hos alle klienter som standard. Tilgangen er tidsbegrenset og logges | Må | Regnskapsførerloven § 4-2, GRFS 2.4 [E§2.1–2.2], [F§3.3]. Personvernveilederen [E§2.5] |
| **BY-19** | **Byråmaler.** Malen omfatter lønnsartkatalog med a-meldingskoder, kontoplanmapping per regnskapssystem, kontrollterskler, rapportpakker og kjøreplaner. Klientene arver malen og kan ha lokale unntak. Før en endring vises hvilke klienter som berøres. Endringer versjoneres, rulles ut fra en bestemt periode og kan rulles tilbake | Må (lønnsarter, mapping, kontroller) / Bør (tariffbibliotek) | [E§4 krav 5]. Risikoen er at «feil sprer seg til mange klienter» [G§DEL 3 #18]. [C§8] |
| **BY-20** | **Målt tidsbruk per klient og kjøring** (aktiv tid i systemet). Tiden eksporteres som *timeforslag* til praksissystemet. Funksjonen er valgfri per byrå og vises aggregert, ikke som overvåking av enkeltpersoner | Bør | Gir lønnsomhet per klient uten ekstra registrering. Praksissystemet eier lønnsomhetsanalysen [Tally-grensesnitt] |
| **BY-21** | **Kvalitetsnøkkeltall:** andel kjøringer korrigert etter godkjenning, a-meldingsavvik per klient, andel kunder som godkjenner i tide, og falske positive i kontrollene | Bør | Grunnlag for egen internkontroll (GRFS 5.2) [E§2.2] |
| **BY-22** | **Sandkasse og opplæring:** kopi av en klient med pseudonymiserte data, og øvingskjøringer for nyansatte | Bør | Wow #31 [G§DEL 3]. Krever pseudonymisering av hensyn til personvernet [ans.] |
| **BY-23** | **Integrasjon mot praksissystem.** Inn: klientregister (organisasjonsnummer, oppdragsansvarlig, kontaktpersoner, lønnsdato). Ut: statushendelser, frister, fullførte kjøringer, a-meldingsavvik, bruksdata og timeforslag. Det generiske API-et og webhooks er Må. Egne integrasjoner mot de 1–2 praksissystemene designpartnerne bruker er Bør | Må (generisk) / Bør (native) | Se kap. 2.10 |
| **BY-24** | **Kapasitetsprognose:** forventet antall slipper og kjøringer per uke neste måned, med juni, desember og januar markert | Kan | Praksissystemet har allerede kapasitetsvisning [Tally-grensesnitt] |

**Hva som er «kult» i 2026**
- Overlevering ved fravær med en KI-oppsummering per klient: «Siste 3 måneder: kunden sender overtid sent, avdeling B har turnus, åpent avvik på a-melding for september.» Oppsummeringen bygger på hendelseslogg og notater, med kildehenvisninger.
- Byråmal med «diff før utrulling»: «Denne endringen påvirker 143 klienter, og 12 av dem har lokale unntak som overstyrer den.»

**Suksessmål**

| Mål | I dag [ans.] | Mål |
|---|---|---|
| Slipper per lønns-FTE per måned | 600 | **≥ 900** |
| Andel kjøringer korrigert etter godkjenning | ikke målt (antatt 5–8 %) | **< 2 %** |
| Tid til en ny lønnskonsulent er selvgående | 3–6 mnd | **≤ 4 uker** |
| Tid til å omfordele én klient ved fravær | 30–60 min | **< 5 min** |
| Antall lønnssystemer i avdelingen | 3 | **1–2** (små klienter kan bli værende i kundens system) |

---

### 1.3 Persona 3 – Daglig leder eller partner i byrået

**Kontekst**
- Partneren styrer forretningsmodell, pris, margin og risiko. I eksempelbyrået gir lønn ca. 9 000 × 180 kr × 12 ≈ **19 MNOK** i omsetning per år [ans., prisnivå fra E§5.2].
- Byrået har tre store bekymringer:
  - prispress fra automatisering
  - mangel på lønnsmedarbeidere
  - at kunder og leverandører tar over relasjonen. SD Worx etablerte for eksempel SD Worx Services Norway AS i januar 2026 for å levere lønnstjenester [A§2.1].

**Jobs to be done**
- «Øke dekningsbidraget på lønn uten å ansette.»
- «Bytte system uten å miste en eneste klient på feil i overgangen.»
- «Ikke bli låst til en liten leverandør som kan forsvinne.»
- «Ha et prisbilde jeg kan forutsi og videreformidle til kundene.»

**Dagens smerter**

| Smerte | Kilde |
|---|---|
| Tiden per slipp ligger nær nullpunktet. Ved 200 kr per slipp og 40 kr i lisens gjenstår ca. 15 minutters arbeid før byrået går i null | [E§5.3] |
| Byrået vet ikke om det tjener penger på hver klient | [ans.] |
| Byrået frykter å være det første byrået på et nytt system | [E§9.3] |
| Leverandører bygger egne tjenesteenheter og blir dermed konkurrenter | [A§2.1], [A§5.1] |
| Bytte midt i året er risikabelt (feriepenger i juni, sammenstillingsoppgave i januar) | [E§9.3], [F§6.3] |
| Visma kan bunte lønn med regnskap og gi høyere provisjon | [E§10.8] |

**Behov**

| ID | Behov | MoSCoW | Begrunnelse og kilde |
|---|---|---|---|
| **BY-25** | **Fleksibel fakturamottaker per klient.** Standard er at byrået betaler (grossistpris), og byrået viderefakturerer. Alternativt fakturerer vi sluttkunden direkte og byrået får provisjon. Valget kan endres per klient uten at data flyttes | Må | Uni Micro-modellen [E§5.1], [E§8.1]. [G§1.10] |
| **BY-26** | **Pris per lønnsslipp**, definert som en aktiv lønnsmottaker som har fått lønnsslipp i måneden. Ingen pris per byråbruker, slik at kontrollører og stedfortredere er gratis. Volumtrinnene gjelder på byrånivå på tvers av klienter. Byrået kan velge en årsavtale med tak for å få forutsigbarhet. Kundeportal og godkjennere er gratis. Det er ingen oppstartspris | Må | [E§10.6]. Byråer foretrekker forutsigbare lisensmodeller fremfor stykkpris [G§2.9] [S]. Se kap. 2.8 |
| **BY-27** | **Bruksdata som fakturagrunnlag.** Per klient og periode telles slipper, kjøringer, ekstrakjøringer, korrigeringskjøringer, a-meldinger, sammenstillingsoppgaver, inntektsmeldinger og nyansatte/sluttere. Dataene leveres som CSV, API eller webhook. **Vi lager ikke fakturaene** | Må (eksport) / Bør (dytt til praksissystem) | Byråer fakturerer per slipp, kjøring og a-melding [E§5.2]. Se kap. 2.5 |
| **BY-28** | **Kanalbeskyttelse i partneravtalen.** Vi selger ikke lønnstjeneste. Vi driver ikke aktivt salg mot byråets klienter. Går en klient direkte til oss innen 12 måneder etter at den forlot byrået, får byrået provisjon | Må (kontrakt) | [E§10.1]. SD Worx-eksempelet [A§2.1] |
| **BY-29** | **Exit-pakke og kontinuitet.** Full eksport per klient og for hele porteføljen: ansatte, arbeidsforhold-ID, lønnsarter, faste transaksjoner, saldoer hittil i år, a-melding-XML, lønnsslipper som PDF/A og revisjonslogg. Eksportformatet er dokumentert. Det finnes en kontinuitetsplan som byrået kan legge inn i beredskapsplanen etter GRFS 2.3 | Må | GRFS 2.3 og 4.1–4.2 [E§2.2]. «Hva skjer med klientene mine hvis dere går konkurs?» (kap. 4.1) |
| **BY-30** | **Beregningsgaranti, SLA og support i lønnsuka.** Vi dekker dokumenterte renter, gebyrer og tilleggsskatt som skyldes en påvist systemfeil, med tak per hendelse. Ansvarsforsikring. Egen kø for byråer, og P1 besvares innen 30 minutter i kritiske vinduer. L2-support har lønnsfaglig kompetanse | Må | [E§8.3], [E§10.7], [F§8.5] |
| **BY-31** | **Migreringsfabrikk for hele porteføljen:** porteføljeanalyse, bølgeplan, adaptere, parallellkjøring der det trengs, «lik på øret»-protokoll og samtykkepakke til klientene | Må | Se kap. 2.9. [F§6], [E§10.4] |
| **BY-32** | **Måling av business case i piloten.** Før og etter måles minutter per slipp, klienter per FTE og andel strukturert grunnlag. Byrået får en rapport det kan bruke internt og overfor styret | Bør | Bevispunkter [E§10.1] |
| **BY-33** | **Leads fra direktesalg.** Kunder med 10–50 ansatte som vil ha byrå, sendes til partnere | Kan | [E§10.5 pkt. 5] |

**Hva som er «kult» i 2026**
- **Prisrådgivning per klient:** systemet sammenligner målt tid per klient (BY-20) med byråets pris og viser hvilke klienter som må prises om. Funksjonen ligger i praksissystemet, men med våre data.
- **Dokumentert risikoreduksjon:** et samlet bilde av andel kjøringer uten manuell korrigering og antall a-meldingsavvik. Det kan brukes overfor profesjonsforsikringen og i Regnskap Norges kvalitetskontroll.

**Suksessmål**

| Mål | I dag [ans.] | Mål |
|---|---|---|
| Dekningsbidrag på lønn (etter lønnskostnad og lisens) | 10–25 % | **+10–15 prosentpoeng** |
| Lisenskostnad som andel av byråets pris per slipp | 0–25 % (varierer med modell) | **≤ 20 %** |
| Byråets egen tid per klient som migreres (grønn klient) | 4–8 t | **≤ 1 t** |
| Tid til hele den aktuelle porteføljen er flyttet | – | **≤ 9 mnd** |
| Klienter tapt på grunn av feil i overgangen | – | **0** |

---

### 1.4 Persona 4 – Kvalitetsansvarlig (statsautorisert regnskapsfører)

**Kontekst**
- Den kvalitetsansvarlige har ansvar for byråets kvalitetsstyring (regnskapsførerloven § 4-1) og for å dokumentere at byrået følger GRFS. Det skal vises frem til Regnskap Norges kvalitetskontroll, som gjennomførte 261 kontroller i kontrollåret 2025, og til Finanstilsynet [E§2.3], [E§2.6].
- Kontrollskjemaet for 2026 ber eksplisitt om rutiner for «Utførelse av lønnsoppdrag (jf. GRFS 7)» og om oversikt over fullmakter [E§2.3].

**Jobs to be done**
- «Kunne vise at hvert lønnsoppdrag er utført og kontrollert etter GRFS, uten å lete i e-post.»
- «Sikre arbeidsdeling, slik at ingen både registrerer og godkjenner en utbetaling.»
- «Ha kontroll på fullmakter og tilganger, og fjerne dem når noen slutter.»
- «Oppbevare oppdragsdokumentasjonen i 5 år, også for kunder som har gått.»

**Dagens smerter**

| Smerte | Kilde |
|---|---|
| Ni av 18 byråer hadde verken rutine for eller praksis med arbeidsdeling ved betalingsoppdrag. Ett byrå delte kodebrikker | [E§1.3] |
| Gjentakende tilsynsfunn er manglende kvalitetssikring, mangelfull avstemming og feil håndtering av skattetrekksmidler | [E§2.6] |
| Altinn-delegering er ikke nok alene. Byrået må ha skriftlig fullmakt og en oversikt over hvem som kan bruke den | [E§2.2, GRFS 3.4] |
| Oppdragsdokumentasjonen skal oppbevares i 5 år, mens kundens data i et kundeeid system blir utilgjengelige når kunden går | [E§2.1 § 5-3], [F§3.1] |
| Det offentlige vet ikke hvilken person som står bak en innsending. Logging på personnivå er systemets ansvar | [E§3.4] |

**Behov**

| ID | Behov | MoSCoW | Begrunnelse og kilde |
|---|---|---|---|
| **BY-34** | **Arbeidsdeling håndheves av systemet.** Den som forbereder en kjøring, kan ikke kontrollere eller godkjenne den. Hver bruker har personlig pålogging med MFA eller SSO, og delte kontoer er umulige. Endring av kontonummer krever kontroll av en annen person. Systemet viser «hvem kan både X og Y» | Må | GRFS 8.1 [E§2.2]. [D§3.2], [F§3.3] |
| **BY-35** | **Oppdragsdokumentasjon som byrået eier.** Pakken lages per klient og periode og viser: hvem som registrerte og hvem som kontrollerte, hvem hos kunden som godkjente og på hvilket grunnlag (portal, e-post eller fullmakt), når skattekort ble hentet, når a-meldingen ble sendt med tilbakemelding og oppfølging av avvik, og avstemmingen. Formatet er PDF/A pluss maskinlesbart. Pakken lagres i **byråets** område og beholdes i 5 år, også etter at klienten har gått | Må | Regnskapsførerloven § 5-3 og GRFS 12.2–12.3 [E§2.1–2.2]. Løser motsetningen mellom «kunden eier dataene» [F§3.1] og byråets oppbevaringsplikt |
| **BY-36** | **Avstemming per klient og periode.** Lønn mot a-melding gjøres via API-et for avstemmingsrapport. Lønn mot regnskap og bank gjøres der data finnes. Avvik må kvitteres | Må (lønn mot a-melding) / Bør (regnskap og bank) | GRFS 9.3 [E§2.2]. [B§2.6]. Finanstilsynet viser til avstemming av skyldig skattetrekk og AGA [E§2.2] |
| **BY-37** | **Fullmaktsoversikt.** Altinn-status hentes automatisk (se BY-15). I tillegg et register over skriftlige fullmakter og bankfullmakter med personer og gyldighet. Systemet varsler når en person med fullmakt slutter i byrået | Bør (det manuelle registeret) | GRFS 3.4 [E§2.2]. Kontrollskjemaet [E§2.3] |
| **BY-38** | **Søkbar revisjonslogg** per klient og per person. Innsyn i sensitive felt logges, og innsendinger logges med den personen i byrået som utløste dem | Må | [E§3.4], [F§3.3], [F§4.9] |
| **BY-39** | **Compliance-pakke:** GRFS-matrise, rutinebeskrivelse for «lønnsoppdrag etter GRFS 7» som byrået kan tilpasse og bruke i kontrollskjemaet, databehandleravtaler for begge modellene, underleverandørliste, beredskapsbeskrivelse og ISAE 3402 type 1. Type 2 kommer etter 9–12 måneder | Må (dokumenter og type 1) / Bør (type 2) | [E§10.3], [F§4.2–4.3], [F§0 pkt. 8] |
| **BY-40** | **Risikobasert kontrollnivå per klient.** Oppdragsansvarlig setter nivået: høy risiko krever fire øyne på hver kjøring, lav risiko gir stikkprøver | Bør | GRFS 5.2 [E§2.2] |
| **BY-41** | **Signaler til løpende oppfølging (hvitvasking)** sendes til praksissystemet: lønn uten arbeidsforhold, store engangsbeløp og utenlandske kontoer | Kan | [E§2.4] (et pluss, ikke et krav) |

**Hva som er «kult» i 2026**
- «Revisjonspakke på ett klikk» per oppdrag og år, som en ZIP-fil med indeks.
- Sporbarhet til kilden: hvert tall i lønnsslippen kan følges til regel, sats, kildehendelse og kvittering [G§DEL 3 #3].
- Altinn-tilgangen sjekkes kontinuerlig, og systemet varsler *før* lønnsdagen.

**Suksessmål**

| Mål | I dag [ans.] | Mål |
|---|---|---|
| Tid til å fremskaffe lønnsdokumentasjon til kvalitetskontroll per oppdrag | 1–3 t | **≤ 10 min** |
| Kjøringer med registrert kontrollør som ikke er samme person som utføreren | ukjent | **100 % (der byrået krever det)** |
| Delte pålogginger | forekommer | **0 (teknisk umulig)** |
| Klienter med gyldig Altinn-tilgang tre virkedager før lønnsdag | ukjent | **100 %** |

---

### 1.5 Persona 5 – Byråets kunde: daglig leder i en forening med 15 ansatte

**Kontekst**
- Foreningen har 11 fastlønte, 4 timelønnede instruktører eller trenere og enkelte honorarmottakere ved arrangementer.
- Den bruker Tikket til arrangementer, OrgLab til medlemmer og tillitsvalgte, og Utleggsappen til reiser og utlegg.
- Daglig leder sender timer og endringer til byrået, godkjenner lønnen og betaler i nettbanken.
- Lønnsutgiftene er langt over grensen for AGA-fritak for ideelle organisasjoner [D§7]. Grensene for fritaket er likevel relevante for andre, mindre byråkunder.

**Jobs to be done**
- «Bruke minst mulig tid på lønn og slippe å tenke på det mellom gangene.»
- «Være trygg på at det jeg godkjenner er riktig, selv om jeg ikke er lønnsekspert.»
- «Ikke få purring eller renter fordi jeg har glemt noe.»
- «Kunne svare styret på hva lønn koster og hvorfor den har endret seg.»

**Dagens smerter**

| Smerte | Kilde |
|---|---|
| Byrået sender en Excel-mal, og den sendes frem og tilbake på e-post | [E§1.2 steg 1], [D§1.4] |
| Han godkjenner en PDF-lønnsliste han ikke forstår | [ans.] |
| **Fra 2026 må forskuddstrekket betales som eget oppdrag med KID senest første virkedag etter lønnsutbetalingen.** Skattetrekkskontoen er borte, og det er lett å glemme betalingen | [B§4], [B§14 pkt. 6] |
| Utlegg og timer fra arrangementer kommer gjennom en egen kanal og blir registrert manuelt på nytt | [G§1.11 B1/B3] |
| Han glemmer fristen for innsending, og byrået må purre | [D§8.2] (godkjenning når ikke frem til cut-off) |

**Behov**

| ID | Behov | MoSCoW | Begrunnelse og kilde |
|---|---|---|---|
| **BY-42** | **Innsending via lenke uten innloggingsfriksjon.** Kunden får lenke på e-post eller SMS til et forhåndsutfylt skjema med de ansatte, de timelønnede og faste tillegg. Skjemaet fungerer på mobil. BankID eller passkey kreves bare ved innsending. Påminnelse kommer før fristen | Må | Forutsetningen for BY-02. Adopsjon er den kritiske risikoen (kap. 4.3) |
| **BY-43** | **Godkjenning av lønn på mobil på under ett minutt.** Sammendraget er i klartekst: totalbeløp, endring fra forrige måned og hvorfor, og hva som skal betales når. Kunden godkjenner, eller avviser med kommentar, med BankID eller passkey som step-up. Godkjenningen logges | Må | GRFS 8.6 [E§1.1]. Wow #19 [G§DEL 3]. PowerOffice får ros for samarbeidet med klienten [E§9.2] |
| **BY-44** | **Komplett betalingsforslag i én godkjenning:** netto lønn på lønnsdatoen, forskuddstrekk første virkedag etter med riktig KID (type 05, månedsperiode), utleggstrekk etter gamle og nye regler til riktig konto og KID, og pensjon der det er aktuelt. Leveres som fil til kundens nettbank eller til regnskapssystemets bankmodul. Kunden får påminnelse, og systemet bekrefter når betalingen er gjennomført (camt.054) | Må (fil og påminnelse) / Bør (direkte bankintegrasjon og bekreftelse) | [B§4], [F§2.2 Betaling]. Se kap. 2.6 |
| **BY-45** | **Dokumentert reservevei for godkjenning:** godkjenning per e-post eller telefon som byrået registrerer med vedlegg, eller «byrået godkjenner etter fullmakt i oppdragsavtalen». Grunnlaget lagres i oppdragsdokumentasjonen | Må | GRFS 8.6: «hvis ikke annet er avtalt» [E§1.1] |
| **BY-46** | **Grunnlag fra egne og andre moduler via felles kontrakt:** godkjente utlegg og reiser fra Utleggsappen, arrangementstimer og honorarer fra Tikket, og honorarmottakere og tillitsvalgte fra OrgLab. De samme åpne kontraktene gjelder for tredjeparter | Bør | [G§0 pkt. 4], [G§1.11 B1–B3]. Like vilkår for alle (produktpremiss) |
| **BY-47** | **Enkel lønnskostrapport til styret:** per måned, per prosjekt eller tilskudd, og mot budsjett | Kan | [D§6.4], [D§7] |
| **BY-48** | **Godkjenningsregler hos kunden:** for eksempel to godkjennere over et beløp, eller at styreleder godkjenner lønnen til daglig leder | Bør | [D§3.2 pkt. 4] (egen lønn) |

**Hva som er «kult» i 2026**
- Kunden godkjenner lønnen i en SMS- eller Teams-melding med passkey og får svar på «hvorfor er lønnen 4 % høyere enn i oktober?» i én setning.
- Utlegg fra Utleggsappen havner automatisk på lønnsslippen, og trekkpliktige deler blir klassifisert riktig.

**Suksessmål**

| Mål | I dag [ans.] | Mål |
|---|---|---|
| Daglig leders tid på lønn per måned | 1–2 t | **≤ 15 min** |
| Godkjenning innen 24 timer etter at den er sendt | ca. 50 % | **≥ 90 %** |
| Forsinket betaling av forskuddstrekk | forekommer (ny risiko i 2026) | **0** |
| Excel-filer på e-post til byrået per måned | 1–3 | **0** |

---

### 1.6 Persona 6 – Kjede (Aider, Azets, ECIT og lignende): IT og innkjøp

**Kontekst**
- Kjedene er PE-eide og har kjøpt mange byråer. Aider har gjort nær 100 oppkjøp siden 2019 og bytter regnskaps-, lønns- og kvalitetssystem etter oppkjøp etter en sjekkliste med 248 punkter [E§7.3].
- Azets har valgt SD Worx for store kunder [E§7.3]. ECIT eier NettLønn, og kanskje Intect, så kjeden har egne interesser i lønnsprogramvare [A§2.3]. **ECIT er derfor en lite sannsynlig kunde** [ans.].
- Kjedene kjøper sentralt gjennom RFP, med en salgssyklus på 12–24 måneder [E§7.4].

**Jobs to be done**
- «Standardisere lønn i oppkjøpte byråer raskt og uten tap av klienter.»
- «Styre tilgang for flere tusen brukere fra Entra ID.»
- «Rapportere volum, kvalitet og lønnsomhet på tvers av byråer og land.»
- «Eie kundeopplevelsen med kjedens merkevare.»
- «Bestå sikkerhetsrevisjon og innkjøp.»

**Dagens smerter**

| Smerte | Kilde |
|---|---|
| Hvert oppkjøpte byrå har sin egen systemmiks. Standardiseringen er manuell og dyr | [E§7.3], [E§9.1 pkt. 2] |
| Kjeden er låst til store leverandører med svak stabilitet og support (SD Worx etter skyovergangen) | [E§9.2] |
| **Fusjoner endrer klientforholdene i Enhetsregisteret. Da faller klientdelegeringene i Altinn bort automatisk** | [B§1.2] («Opphører klientforholdet, faller klientdelegeringen bort automatisk»). Konsekvensen er [ans.] |
| Innkjøp krever ISAE 3402 type 2, ISO 27001, pentest og data i Norge eller EØS | [F§4.1] |

**Behov**

| ID | Behov | MoSCoW | Begrunnelse og kilde |
|---|---|---|---|
| **BY-49** | **Hierarki: kjede → byrå (juridisk enhet) → kontor eller avdeling → team → klient.** Maler og roller arves | Må (i datamodellen) / Bør (i brukergrensesnittet) | Billig nå og dyrt å bygge om senere [F§3.1]. [E§4 krav 1] |
| **BY-50** | **SSO med Entra ID, SCIM-provisjonering og automatisk deprovisjonering** | Bør (Må for en kjedeavtale) | [F§4.8], [D§5.3] |
| **BY-51** | **Flere systembrukere for klientsystem** (én per juridisk byråenhet) i ett grensesnitt, og **masseretilknytning** av klienter ved fusjon eller omorganisering | Bør | [B§1.2]. Følger av kjedenes oppkjøpstakt [ans.] |
| **BY-52** | **Kjedemaler** som arves fra kjede til byrå til klient. Kjeden kan låse felt | Bør | Utvidelse av BY-19 |
| **BY-53** | **Rapportering på tvers:** volum, kvalitetsnøkkeltall og SLA-brudd per byrå. API eller eksport til kjedens datavarehus, uten persondata | Bør | [F§3.2] (lesemodell uten sensitive persondata) |
| **BY-54** | **«Powered by»-merkevare:** kjedens logo og farger i kundeportal, ansattapp og lønnsslipp. Eget domene senere. **Full white-label kommer ikke nå** | Bør / Ikke nå (full white-label) | [E§8.1 modell 4–5] |
| **BY-55** | **Sikkerhetspakke for innkjøp:** ISAE 3402 type 2, veikart for ISO 27001, pentest-sammendrag, data i Norge, dedikert celle mot tillegg og exit-plan | Bør (år 1–2) | [F§4.1–4.2], [F§3.2] |
| **BY-56** | **Sentral fakturering:** én faktura til kjeden, spesifisert per byrå og klient | Bør | [G§1.10] |
| **BY-57** | **Agent- eller MCP-API**, slik at kjedens egne KI-verktøy kan forberede kjøringer og hente status, men aldri godkjenne, sende inn eller utbetale | Kan | [G§2.4], [F§3.3] (agentrollen) |

**Hva som er «kult» i 2026**
- En migreringsfabrikk som gjør «oppkjøpt byrå på standard lønn» til et 90-dagersprosjekt med bølgeplan og protokoll per klient.
- SCIM som fjerner tilgangen samme dag som en medarbeider slutter.
- Kvalitetsnøkkeltall for hele kjeden hver måned uten manuelt arbeid.

**Suksessmål**

| Mål | I dag [ans.] | Mål |
|---|---|---|
| Tid fra oppkjøp til at lønnsklientene i det oppkjøpte byrået er på kjedens standard | 12–24 mnd | **≤ 6 mnd** |
| Brukere som logger inn via SSO | varierer | **100 %** |
| Tid fra en medarbeider slutter til tilgangen er fjernet | dager | **≤ 1 t** |
| Klienter som må tilknyttes Altinn manuelt på nytt etter fusjon | alle | **0 manuelle (masseoperasjon)** |

---

## 2. Standpunkter på de ti temaene

### 2.1 Systembruker for klientsystem og samlekjøringer

**Standpunkt:** Vi bruker én systembruker for klientsystem per byrå (juridisk enhet) med tilgangspakken `regnskapsforer-lonn`. Tilknytningen er en produktfunksjon (BY-15). Samlekjøringer brukes fullt ut for **henting**, men innsending skjer bare med en port per klient.

| Operasjon | Samlekjøring? | Hvorfor |
|---|---|---|
| Skattekort: endringspolling og årsskiftebestilling | **Ja, alle klienter** | Leses inn uten risiko. Maks 1 000 fødselsnumre per kall. Arbeidsgiver må oppgis ved flere arbeidsgivere (`FOR_004`). Det blir bare polling fra 15.12.2026 [B§3.1] |
| Tilbakemelding på a-melding, avstemmingsrapport og trekkpålegg | **Ja** | Gir en avviksliste på tvers av klienter [B§2.3], [B§2.6], [B§7.1] |
| A-melding: innsending | **Bare «send alle som er klare»** | Bare klienter med godkjent kjøring og kvitterte kontroller. En erstatningsmelding erstatter *hele* den forrige [B§2.4], så en feilaktig massesending kan skade mange klienter samtidig. Bruk `idempotencyKey` per melding [B§2.2] |
| Satsoppdateringer (G, trekktabeller, AGA) | **Ikke byråets jobb** | Lovpålagte satser og regler vedlikeholder vi sentralt i versjonerte regelpakker [F§1.3]. Byrået skal ikke måtte «oppdatere satser for alle» |
| Inntektsmelding til NAV | **Uavklart** | Systembruker for klientsystem støtter bare tilgangspakker [B§1.2]. NAV krever `lonn-personopplysninger-saerlig-kategori` [B§1.3]. Om regnskapsførerpakkene dekker NAV-ressursene, er **ikke verifisert** (kap. 8) |

**Detaljer som avgjør om dette fungerer i praksis**
- **Klientregisteret må vi føre selv.** API-et for klientdelegering har foreløpig ikke paginering [E§3.4], og det bærer ikke byråets egen struktur.
- **Logging på personnivå:** Skatteetaten vet ikke hvem som sto bak en innsending. Derfor logger vi personen som utløste den [E§3.4].
- **Kunder som deler arbeidet med byrået** (kundens HR registrerer og byrået sender a-melding): For hver opplysningspliktig angis det hvem som sender a-meldingen. Da trengs to separate systembrukere [B§1.2], og systemet må hindre at begge sender.
- **Byrået driver ikke kunderådgivning om Altinn.** Systemet lager instruksen kunden trenger når byrået ikke er registrert som regnskapsfører i Enhetsregisteret (BY-15).

**Selvkritikk:** E fremhever Altinn 3 som «det store vinduet» [E§0 pkt. 4]. Det stemmer for 2026, men ikke for vår lansering i 2028. Systembruker er da et inngangskrav. Det som skiller oss ut, er (a) tilknytning på få minutter, (b) at systemet oppdager tapt tilgang før lønnsdagen, og (c) feilmeldinger i klartekst.

### 2.2 Klientdashbord med frister og status

**Standpunkt:** Vi bygger en **arbeidskø** (BY-01) og en **avdelingsoversikt** (BY-16) for klientene i vårt system. Vi bygger *ikke* et fristsystem for hele porteføljen.

- **Begrunnelse:** Praksissystemet har allerede frister på tvers av klienter, inkludert lovpålagte frister, oppgaver fra rutiner, kapasitet og lønnsomhet [Tally-grensesnitt]. I år 1 ligger dessuten halve porteføljen i kundens Tripletex eller PowerOffice. Et dashbord som viser halve porteføljen, blir ikke brukt som hovedskjerm.
- **Konsekvens:** Vi beregner *lønnsfristene* eksakt, fordi bare vi kjenner dem (lønnsdato, bankens avskjæringstid, forskuddstrekk T+1, a-melding den 5. og AGA-termin) [B§2.5], [B§4]. Vi sender dem som hendelser til praksissystemet (BY-23). Generelle frister som mva og årsoppgjør hører hjemme i praksissystemet.

### 2.3 Kundeportal for godkjenning

**Standpunkt:** Kundeportalen er et Må, men den skal være minimal. Den skal ha tre funksjoner: **sende inn** (BY-42), **godkjenne** (BY-43) og **svare på spørsmål knyttet til et konkret avvik**. Den skal *ikke* ha dokumentarkiv, chat, oppgavelister eller rapportbibliotek, fordi byrået har egne klientportaler eller praksissystemer for det.

- **Påloggingen** skjer med magisk lenke. BankID eller passkey kreves bare som step-up ved innsending og godkjenning [F§4.8].
- **Reserveveien** (BY-45) er obligatorisk. Uten den mister byrået GRFS-dokumentasjonen for kunder som ikke bruker portalen.
- **Måltallet** er adopsjon: andel kjøringer der grunnlaget kom strukturert og godkjenningen ble gitt digitalt. Hele tidsbesparelsen hviler på dette (kap. 4.3).

### 2.4 Maler på tvers av klienter

**Standpunkt:** Malene er et Må (BY-19), med arv og lokale unntak, forhåndsvisning av endringer («påvirker 143 klienter»), versjonering, utrulling fra en bestemt periode og tilbakerulling. Malen omfatter lønnsartkatalog med a-meldingskoder, kontoplanmapping per regnskapssystem (NS 4102), kontrollterskler, kjøreplaner og rapportpakker.

- **Det som ikke er byråets ansvar:** lovpålagte satser og regler (se 2.1).
- **Tariffbibliotek** som deles på byrånivå (Virke HUK, Spekter og lignende) er Bør [C§8].
- **Største risiko:** én feil i malen sprer seg til hundrevis av klienter [G§DEL 3 #18]. Derfor kreves fire øyne ved malendringer, og en release-diff kjøres mot forrige måned for alle berørte klienter før utrulling [F§7.6].

### 2.5 Fakturagrunnlag for lønnsoppdraget

**Standpunkt:** Vi leverer **bruksdata, ikke fakturaer** (BY-27).

- Per klient og periode teller vi slipper, kjøringer, ekstrakjøringer, korrigeringskjøringer, a-meldinger, sammenstillingsoppgaver, inntektsmeldinger og nyansatte/sluttere. Dataene leveres som CSV og API, og som webhook til praksissystemet.
- **Begrunnelse:** Byråene fakturerer per slipp, kjøring og a-melding [E§5.2], men fakturaen lages i praksissystemet eller i byråets eget regnskap. Tally har fakturagrunnlag per klient og periode [Tally-grensesnitt]. Unimicro har funksjonen fordi Unimicro også *er* regnskapssystemet [E§4].
- **Kan:** Et prisoppsett per byrå, slik at bruksdata kan leveres som ferdig prisede linjer. Det bygges bare hvis et praksissystem ikke kan ta imot rå tellinger.

### 2.6 Hvem trykker «betal»

**Standpunkt:** **Kunden** godkjenner betalingen i egen bank eller i regnskapssystemets bankmodul. Det er utgangspunktet etter GRFS 8.6 [E§1.1]. Finanstilsynet påpeker at kundeportaler reduserer behovet for betalingsfullmakt [E§1.3]. Vi lager et komplett betalingsforslag (BY-44), men **vi holder aldri penger og setter aldri i gang betalinger fra egen konto**.

**Hvorfor dette er viktigere fra 2026:** Skattetrekkskontoen er avviklet. Hver lønnskjøring gir nå minst *to* betalinger med ulik dato: netto lønn på lønnsdatoen og forskuddstrekk første virkedag etter, med KID som eget oppdrag. I tillegg kommer eventuelle utleggstrekk til kontoen og KID-en i pålegget [B§4]. Antallet betalingshendelser per klient og måned har altså økt, og det samme har risikoen for for sen betaling. Den er straffbar for kunden [B§14 pkt. 6].

| Scenario | Hvordan systemet støtter det |
|---|---|
| **Kunden betaler (standard)** | Én godkjenning (BY-43) gir et betalingssett med riktige forfallsdatoer og KID. Det leveres som pain.001-fil eller til regnskapssystemets bankmodul. Kunden får påminnelse, og betalingen bekreftes med camt.054 eller ved at kunden bekrefter. Om én pain.001-fil med flere betalingsblokker med ulike utførelsesdatoer støttes av alle banker, må verifiseres [ans.] |
| **Byrået betaler med fullmakt** | Rollen «betalingsfullmektig» er knyttet til navngitte personer (BY-37). Den som forbereder kjøringen, kan ikke registreres som den som godkjenner betalingen (BY-34). Hvem som faktisk godkjente i banken, logges. Dette svarer på Finanstilsynets funn [E§1.3] |
| **AGA annenhver måned** | Frist med KID per klient i arbeidskøen (BY-10). AGA er ikke en del av lønnsbetalingen [B§4] |

**Ikke nå:** betalingsinitiering via egen PSD2-lisens, bankkonto for klientmidler, og direkte bankintegrasjon mot alle banker. Vi starter med fil og/eller regnskapssystemets bankmodul, og legger til én integrasjonspartner når volumet forsvarer det.

### 2.7 Ansvarsgrensen: vi selger programvare, ikke lønnstjeneste

**Standpunkt:** Grensen er juridisk nødvendig og er samtidig et salgsargument.

- **Juridisk:** Lønnstjenester er godkjenningspliktig regnskapsføring. En ren programvareleverandør er ikke regulert, så lenge den ikke tar ansvar overfor kunden for resultatet av regnskapsføringen [E§2.1].
- **Kanal:** Leverandører som bygger egen tjenesteenhet (SD Worx Services Norway AS, 2026), blir konkurrenter til byråene [A§2.1]. Vi lover at det aldri skjer hos oss.

| Område | Hvor grensen går |
|---|---|
| Kontrakt | Vi svarer for at beregningen er i samsvar med regelverket (beregningsgaranti med tak) [E§8.3]. Vi svarer ikke for kundens grunnlag eller for byråets vurderinger |
| Tjenester | Ingen BPO og ingen «vi kjører lønnen i januar når dere har kapasitetsproblemer». Henvis heller til andre partnerbyråer |
| Support | Supporten hjelper med systemet og forklarer regelverket med kilder. Den vurderer ikke kundens grunnlag (for eksempel «skal denne personen ha overtid?») |
| KI | KI er rådgivende. Den forbereder, forklarer og flagger, men godkjenner, sender inn og utbetaler aldri. Dette håndheves i tilgangsmodellen [F§0 pkt. 9] |
| Språk i produktet | Dokumentasjonen sier «Kontroll utført av [navn], [dato]», aldri «Godkjent av systemet». Det er byråets oppdragsansvarlige som signerer [GRFS 5.2] |
| Direktekunder | Kunder som kjøper direkte og ønsker hjelp, henvises til partnere (BY-33). Vi gir ikke arbeidsrettslig rådgivning |

### 2.8 Lisensmodell: byrå betaler eller sluttkunde betaler per klient

**Standpunkt:** **Byrået betaler (grossist) er standard.** Sluttkunden kan betale direkte per klient, med provisjon til byrået. Valget kan endres uten at data flyttes (BY-25). Kunden er alltid behandlingsansvarlig og eier dataene sine [F§3.1], [E§8.2].

| Spørsmål | Standpunkt | Begrunnelse |
|---|---|---|
| Hvorfor er byrå betaler standard? | Byrået blir en aktiv selger, kan pakke lisensen inn i prisen per slipp («190 kr per slipp, alt inkludert») og slipper å be kunden om enda et abonnement | Byråene er vant til å tjene på lisensen [E§0 pkt. 6]. Mange byråer viderefakturerer lisensen [E§5.2 Millor] |
| Når betaler sluttkunden? | Når kunden har 100 ansatte eller mer, vil ha egen avtale, har egen lønnsavdeling eller deler arbeidet med byrået, eller når byrået ikke vil ta kredittrisikoen | [E§8.1] |
| Hvilken enhet prises? | Lønnsslipp, det vil si en aktiv lønnsmottaker med slipp i måneden. Ingen pris per byråbruker | Samme enhet som byrået selv fakturerer [E§5.2]. Kontrollører og stedfortredere skal være gratis [E§10.6] |
| Forutsigbarhet | Volumtrinn summert på byrånivå, og en valgfri årsavtale med tak («inntil N slipper per måned for X kr») | Byråer foretrekker forutsigbare lisensmodeller [G§2.9] [S] |
| Prisnivå | E foreslår en veiledende innpris på 25–45 kr per slipp [E§10.6]. **Se regnestykket i kap. 4.3:** Med lav portaladopsjon må prisen ligge nederst i spennet | [ans.] |
| Hva er gratis? | Kundeportal, godkjennere, ansattapp med lønnsslipp, migrering og opplæring | Markedsstandard [E§6] |
| Hvem eier kunderelasjonen? | Kunden eier dataene. Byrået eier oppdraget. Kanalbeskyttelsen (BY-28) står i partneravtalen | Byrået, ikke leverandøren, styrer i praksis om kunden blir [E§6] |

**Selvkritikk:** E fremhever 30–50 % byråmargin [E§10.5]. Ved 35 kr per slipp er 50 % margin 17,50 kr. Det er lite mot byråets 150–250 kr per slipp. Lisensmarginen er et signal om at vi satser på kanalen, ikke hovedargumentet. Hovedargumentet er minutter per slipp, kanalbeskyttelse og exit-pakke.

### 2.9 Migrering av en hel klientportefølje

**Standpunkt:** Vi migrerer **i bølger, aldri alt på én gang**, og vi gjør jobben. Byrået skal bruke høyst 1 time per enkel klient.

| Steg | Innhold | Kilde |
|---|---|---|
| 1. Porteføljeanalyse | Alle klienter klassifiseres ut fra a-melding-XML eller kildesystem. **Grønn:** fastlønn, standard lønnsarter. **Gul:** variable timer eller turnus, fravær med refusjon. **Rød:** tariff med lønnsstiger, offentlig pensjon (KLP eller SPK), konsern eller flere AGA-soner | [F§6.2], [D§7] |
| 2. Byråets egen lønn først | Byrået kjører lønnen til sine egne ansatte i systemet før kundene flyttes. Det er en ufarlig pilot, og lønnsavdelingen lærer systemet på egne data | [ans.] (fra kritikken i runde B) |
| 3. Samtykkepakke til klientene | Ferdige maler: varsel om ny (under)databehandler, instruks for Altinn-delegering der den trengs, og invitasjon til portalen. Sendes samlet | Kundene må godkjenne nye databehandlere [E§9.3], [E§8.2] |
| 4. Datainnhenting | Kilder: a-melding-XML og avstemmingsdata fra Skatteetaten (fasit), adaptere for Tripletex, PowerOffice Go og Visma.net Payroll, og Excel-maler med KI-støttet mapping. **Arbeidsforhold-ID videreføres** | [F§6.2], [A§7.1], [C§4.2] |
| 5. Kontroll | Grønne klienter: skyggeberegning av 1–3 historiske måneder. Gule og røde: i tillegg 1–2 parallelle måneder. Akseptkriteriet er «lik på øret», og protokollen signeres av byrået | [F§6.4–6.5] |
| 6. Bølgeplan | Primærvindu er januar. Sekundærvindu er juli–september. Mai–juni og oktober–desember unngås (bortsett fra parallellkjøring før januar). Vi har et tak på antall klienter per byrå per måned i januar | [F§6.3] |

**Risikoer**
- A-melding versjon 2.4 settes i produksjon fra 2028-01 [B§12], samtidig med vår første produksjon. Rettelser av perioder i 2027 etter overgangen må avklares [B§14 pkt. 11].
- Tilgang til data fra SD Worx og Visma.net Payroll kan kreve avtale med leverandøren [F§10 ADR-15].

### 2.10 Integrasjon mot praksissystem (oppgaver, frister og tid)

**Standpunkt:** Først kommer et generisk API og webhooks (Må). Deretter bygger vi egne integrasjoner mot de 1–2 praksissystemene designpartnerne faktisk bruker (Bør). **Oppgavesynk begge veier bygger vi ikke.** Oppgavene eies av praksissystemet.

| Retning | Innhold | Prioritet |
|---|---|---|
| Lønn → praksis: **status og frister** | Kjøring opprettet eller endret status, lønnsfrist, kunden har ikke godkjent, a-melding sendt eller avvik, kjøring fullført | 1. Gjør at praksissystemets porteføljevisning også dekker lønn |
| Praksis → lønn: **klientregister** | Organisasjonsnummer, oppdragsansvarlig, kontaktpersoner, lønnsdato, oppdragsomfang (hvem godkjenner, hvem betaler) | 2. Unngår dobbel registrering ved oppstart av en klient [GRFS 3.3] |
| Lønn → praksis: **bruksdata** | Tellingene fra BY-27 | 3. Fakturagrunnlag |
| Lønn → praksis: **timeforslag** | Målt aktiv tid per klient og kjøring (BY-20), med idempotensnøkkel | 4. Valgfritt per byrå |

- **Format:** CloudEvents og Standard Webhooks med signering og replay-vern [G§0 pkt. 5].
- **Observasjon:** Tallys grensesnitt har timeføring med idempotensnøkkel og oppgave- og klientkobling, fakturagrunnlag per klient og periode, frister på tvers, kapasitet, lønnsomhet, og bestilling av a-meldingsrapport via byråets egen Maskinporten-tilgang [Tally-grensesnitt]. Praksissystemene beveger seg altså inn mot myndighetsdata. Vi skal ikke konkurrere der, men levere lønnsdata dit.
- **Hull:** API-er og integrasjonsmønstre for Maestro, Duett, Visma Practice og Sticos Oversikt mot lønn er ikke kartlagt. Sticos lister bare regnskapssystemer på integrasjonssiden sin, ingen rene lønnssystemer ([sticos.no/integrasjoner](https://www.sticos.no/integrasjoner)). Søk om Maestro ga bare integrasjonen for årsoppgjør mot Unimicro ([unimicro.no](https://unimicro.no/integrasjoner/maestro-årsoppgjør)).

---

## 3. Hvordan behovene henger sammen (flyt for én kjøring)

```
Kunde (BY-42 lenke)  ─┐
Tikket/Utleggsappen/  ├─► Lønnsgrunnlag (BY-02/03) ─► Kontinuerlig beregning ─► Avvikskø (BY-04/05)
OrgLab (BY-46)       ─┘                                                          │ kvitteres
                                                                                  ▼
Praksissystem ◄── status/frister (BY-23) ◄── Arbeidskø (BY-01) ◄── Fire øyne (BY-34/40)
                                                                                  │
                                    Kunde godkjenner (BY-43/45) ◄─────────────────┘
                                                  │
              ┌───────────────────────────────────┼─────────────────────────┐
              ▼                                   ▼                         ▼
   Betalingsforslag (BY-44)            A-melding (BY-08, BY-15)     Bilag (BY-09)
   netto + trekk T+1 + KID             valider → send → tilbakemelding  → regnskapssystem
              │                                   │                         │
              └────────────► Avstemming (BY-36) ◄─┴─────────────────────────┘
                                          │
                                          ▼
                       Oppdragsdokumentasjon, byrå-eid i 5 år (BY-35) + bruksdata (BY-27)
```

---

## 4. Runde B: kritikk og revisjon

### 4.1 Kritikken: hva en byråleder med 20 års erfaring ville avfeid

Dette er innvendingene mot utkastet fra runde A, formulert slik en erfaren leder for en lønnsavdeling ville sagt dem [ans.]:

1. **«Ett klikk sender a-melding for alle klienter? Aldri.** Jeg sender når klienten er ferdig og kontrollert. En massesending som går feil, erstatter riktige meldinger for femti kunder.» → Innsending skjer med port per klient (2.1).
2. **«Kundene mine logger ikke inn i en portal til.** De svarer ‘ok’ på e-post.» → Innsending og godkjenning uten innlogging, en dokumentert reservevei og adopsjon som måltall (2.3, BY-45).
3. **«Jeg har dashbordet i praksissystemet.** Deres viser halve porteføljen min.» → Arbeidskø i stedet for porteføljesystem, og status sendes til praksissystemet (2.2, 2.10).
4. **«Fakturaen lager jeg i Tally eller regnskapet.** Gi meg tallene.» → Bruksdata i stedet for fakturamodul (2.5).
5. **«50 % margin på 35 kroner er lommerusk.** Det jeg lurer på, er hvem som gjør migreringsjobben, og hva som skjer om dere går konkurs.» → Migreringsfabrikk, exit-pakke og kanalbeskyttelse (BY-28, BY-29, BY-31).
6. **«Januar 2027? Vi står midt i Altinn-kaoset.** Ingen bytter lønnssystem nå.» → Tidslinjen følger F: pilot høsten 2027 og produksjon januar 2028.
7. **«KI som kontrollerer lønnen? Det er jeg som har ansvaret.** Vis meg fem avvik, ikke femti.» → Presisjon i avvikslisten som måltall, KI bare som forklaring, og dokumentasjonen navngir den menneskelige kontrolløren.
8. **«Jeg piloterer ikke på en kunde.** Jeg piloterer på vår egen lønn.» → Byråets egen lønn først (2.9).
9. **«White-label koster dere mye og meg lite.** Logoen min på lønnsslippen holder.» → «Powered by» er Bør, full white-label kommer ikke nå.
10. **«Kvalitetsdashbord per medarbeider? Da slutter halve avdelingen.»** → Tallene aggregeres, tidsmåling er valgfri og er ikke overvåking av enkeltpersoner (BY-20, BY-21).
11. **«De små kundene mine har lønn gratis i Tripletex-pakken.** Hvorfor skal de betale dere?» → Sweet spot er 10–300 ansatte. Små klienter tvinges ikke over (kap. 0 pkt. 12).
12. **«Hva skjer med dokumentasjonen min når kunden går til et annet byrå?»** → Oppdragsdokumentasjon som byrået eier (BY-35).

### 4.2 Hva byråene sier de vil ha, men ikke betaler for

| Uttalt ønske | Betaler de for det? [ans.] | Vår respons |
|---|---|---|
| Full white-label med eget domene og egen app | Nei. Kjedene vil ha det, men tar ikke kostnaden for support og drift | «Powered by» med logo (BY-54). Full white-label kommer ikke nå |
| Rik kundeportal med dokumenter, chat og rapporter | Nei. Kundene bruker den ikke, og byrået har egne kanaler | Minimal portal (2.3) |
| Fakturamodul | Nei. Praksissystemet gjør det | Bruksdata (BY-27) |
| Lønnsomhetsanalyse og kapasitetsplan | Nei. Praksissystemet gjør det | Timeforslag og bruksdata dit (BY-20, BY-23) |
| KYC- og hvitvaskingsmodul | Nei | Signaler kan sendes ut (BY-41, Kan) |
| BI-rapportbygger | Sjelden | Eksport og API. Standard rapportpakker i malen |
| «Selvkjørende lønn» med KI | Nei, de selger trygghet [G§2.9] | KI forbereder og forklarer, mennesket godkjenner |
| Integrasjon mot alle praksissystemer | Bare mot det de selv bruker | Generisk API, deretter 1–2 egne integrasjoner |
| **Det de faktisk betaler for** | **Ja** | Færre minutter per slipp (innhenting og kontroll), færre feil, at migreringen blir gjort for dem, Altinn som ikke svikter på lønnsdagen, support i lønnsuka og å slippe å miste klienter |

### 4.3 Hva som faktisk gir margin (regnestykke)

Utgangspunktet er 13–14 minutter per slipp i dag, fordelt etter D§1.4. Reduksjonene er anslag [ans.].

| Tidspost | Andel [D§1.4] | Minutter i dag | Reduksjon med oss | Sparte minutter | Hva som gir besparelsen |
|---|---|---|---|---|---|
| Innhenting og purring | 30–40 % | ca. 5,0 | −50 % | 2,5 | BY-02, BY-42, BY-46, BY-10 (forutsetter portaladopsjon) |
| Kontroll og avviksanalyse | 25–35 % | ca. 4,2 | −50 % | 2,1 | BY-04, BY-05 |
| Korrigeringer og ekstrakjøringer | 10–15 % | ca. 1,7 | −40 % | 0,7 | BY-06, BY-11 |
| Avstemming og etterarbeid | 10–15 % | ca. 1,7 | −60 % | 1,0 | BY-09, BY-36, BY-35 |
| Henvendelser fra ansatte | 5–10 % | ca. 1,0 | −30 % | 0,3 | BY-14 |
| **Sum** | | **ca. 13,6** | | **ca. 6,6** | **ca. 7 minutter per slipp** |

**For eksempelbyrået (9 000 slipper i måneden)**
- **Besparelse:** 6,6 min × 9 000 ≈ 990 t per måned ≈ 6 årsverk. Med 600–650 kr per time i kostnad [E§5.3] tilsvarer det ca. **600 000–640 000 kr per måned**.
- **Lisens:** 35 kr × 9 000 = **315 000 kr per måned**.
- **Følsomhet:** Hvis portaladopsjonen bare blir 30 %, faller innhentingsbesparelsen til ca. 1 minutt, og totalen til ca. 5 minutter per slipp, altså ca. 450 000–490 000 kr per måned. Da blir marginen over lisensen tynn. Konklusjonen er at **portaladopsjon og presisjon i avvikslisten er de to viktigste produktrisikoene**, og at prisen må ligge nederst i E-spennet hvis adopsjonen blir lav.
- **Verdien er bare reell hvis kapasiteten brukes** til flere klienter eller til å la være å ansette. Det er sannsynlig, fordi det er mangel på lønnsmedarbeidere [E§7.1].

### 4.4 Hva jeg endret i runde B og hvorfor

| # | Utkast A sa | Endret i B til | Hvorfor |
|---|---|---|---|
| 1 | Første produksjon i januar 2027 (fra E§10.3) | Pilot i oktober–desember 2027 og produksjon i januar 2028 | F§9.7 viser realistisk byggetid. E og F var ikke samkjørt |
| 2 | Altinn 3 som viktigste differensiator | Altinn 3 er et inngangskrav, og differensieringen ligger i tilknytning og diagnose | Innen 2028 har alle konkurrentene systembruker |
| 3 | Klientdashbord over alle klienter med alle frister som Må nr. 1 | Arbeidskø for klientene i vårt system, og status sendes til praksissystemet | Praksissystemet har allerede frister og oppgaver [Tally-grensesnitt]. Halve porteføljen ligger utenfor oss i år 1 |
| 4 | Massesending av a-melding for alle klienter | «Send alle som er klare» med port per klient | En erstatningsmelding erstatter hele den forrige [B§2.4]. Veteranen ville avvist blind massesending |
| 5 | Kundeportal med dokumenter, meldinger og rapporter | Minimal portal (innsending, godkjenning, avviksspørsmål) uten innloggingsfriksjon, og reservevei som Må | Adopsjon avgjør besparelsen (4.3). Rike portaler brukes ikke av små kunder |
| 6 | Egen fakturamodul for byrået | Bruksdata som eksport eller webhook | Praksissystemet fakturerer allerede |
| 7 | Timeføring for byrået inne i lønnssystemet | Passiv tidsmåling som valgfritt timeforslag til praksissystemet | Unngår et parallelt timesystem og hensyntar personvern og kultur |
| 8 | Byråmargin på 30–50 % som hovedargument | Minutter per slipp, kanalbeskyttelse og exit-pakke som hovedargument. Marginen er et signal | 50 % av 35 kr er lommerusk mot 150–250 kr per slipp |
| 9 | Ren stykkpris per slipp | Stykkpris som enhet, men med volumtrinn på byrånivå og valgfri årsavtale med tak | Byråer foretrekker forutsigbarhet [G§2.9] |
| 10 | Skattetrekk og AGA annenhver måned i betalingsflyten (fra E§1.2) | Forskuddstrekk første virkedag etter hver lønnsutbetaling, med KID og som eget oppdrag | E var utdatert. B§4 er verifisert: skattetrekkskontoen ble avviklet 1.1.2026 |
| 11 | Byrået kan sette i gang betaling | Kunden godkjenner. Byrå med fullmakt støttes med arbeidsdeling. Vi rører aldri pengene | GRFS 8.6, Finanstilsynets funn, og unngår PSD2-lisens |
| 12 | Oppdragsdokumentasjon «i lønnssystemet» | Egen pakke som byrået eier og oppbevarer i 5 år, uavhengig av kundens data | Motsetningen mellom F§3.1 (kunden eier data) og regnskapsførerloven § 5-3 |
| 13 | Pilot på 3–5 kundeklienter | Byråets egen lønn først, deretter grønne klienter | Lavere risiko og bedre opplæring |
| 14 | Full white-label som Bør for kjeder | «Powered by» er Bør, full white-label kommer ikke nå | Kostnad uten betalingsvilje. Kjeder er dessuten et marked for år 2–3 |
| 15 | Kvalitetsnøkkeltall per medarbeider | Aggregert og valgfritt | Kultur og personvern |
| 16 | Alle klientstørrelser i målgruppen | Sweet spot er 10–300 ansatte. Små klienter flyttes ikke i år 1 | Lønn er allerede betalt i kundens Tripletex- eller PowerOffice-pakke |
| 17 | Fullmaktsregister som eget Må | Altinn-status hentes automatisk (Må). Det manuelle registeret er Bør | Det automatiske gir verdi uten registrering. Det manuelle overlapper med praksissystemet |
| 18 | Inntektsmelding til NAV via byråets systembruker som en selvfølge | Markert som uavklart | NAV krever en pakke for særlige kategorier. Om den dekkes av klientsystem-systembrukeren, er ikke verifisert |
| 19 | Fusjon i kjeder ikke vurdert | Masseretilknytning av klienter (BY-51) | Klientdelegeringer faller bort når klientforholdet opphører [B§1.2] |

---

## 5. Topp 20 behov, rangert

Rangeringen vekter (1) effekt på minutter per slipp, (2) om behovet hindrer bytte når det mangler, og (3) om det er et krav etter regelverk eller GRFS.

| Rang | ID | Behov | MoSCoW | Persona | Hvorfor så høyt |
|---|---|---|---|---|---|
| 1 | BY-04 + BY-05 | Avviksbasert kontroll med klartekstforklaring | Må | 1, 4 | Størst tidsbesparelse etter innhenting. Gir også GRFS 7.2-dokumentasjon |
| 2 | BY-02 + BY-42 | Strukturert lønnsgrunnlag inn og innsending via lenke uten friksjon | Må | 1, 5 | Den største tidsposten (30–40 %). Hele business caset avhenger av adopsjonen |
| 3 | BY-31 | Migreringsfabrikk (porteføljeanalyse, bølger, «lik på øret», samtykkepakke) | Må | 3, 6 | Uten den blir det ikke noe bytte |
| 4 | BY-15 | Tilknytning og tilgangsdiagnose for systembruker per klient | Må | 1, 4 | Uten tilgang ingen a-melding. Feil her rammer på lønnsdagen |
| 5 | BY-08 | A-melding med forhåndsvalidering, «send alle klare» og avviksliste på tvers | Må | 1 | Lovkrav, tvangsmulkt og GRFS 7.8 |
| 6 | BY-43 + BY-45 | Godkjenning på mobil med klartekst, pluss dokumentert reservevei | Må | 5, 4 | GRFS 8.6. Godkjenning er flaskehalsen på T-3 |
| 7 | BY-06 | Ubegrenset testkjøring og retro med automatisk differanse for trekk og AGA | Må | 1 | Største klage mot den største konkurrenten [E§9.2] |
| 8 | BY-01 | Arbeidskø på tvers av egne klienter med eksakte lønnsfrister | Må | 1 | Daglig hovedskjerm |
| 9 | BY-44 | Komplett betalingsforslag (netto + forskuddstrekk T+1 med KID + utleggstrekk) i én godkjenning | Må | 5, 1 | Ny smerte fra 2026 [B§4]. Feil er straffbart for kunden |
| 10 | BY-09 | Lønnsbilag til klientens regnskapssystem (Tripletex, PowerOffice Go, Visma) | Må | 1 | Byrået velger ikke kundens regnskapssystem [E§4 krav 10] |
| 11 | BY-34 | Arbeidsdeling håndhevet av systemet og personlig pålogging | Må | 4 | Finanstilsynets funn [E§1.3]. GRFS 8.1 |
| 12 | BY-35 | Oppdragsdokumentasjon som byrået eier i 5 år | Må | 4 | Regnskapsførerloven § 5-3. Lite tyder på at konkurrentene løser det [ans.]. Billig når loggen finnes |
| 13 | BY-19 | Byråmaler med arv, forhåndsvisning av endringer og versjonering | Må | 2 | Skala og standardisering. Risikostyring av feil som sprer seg |
| 14 | BY-07 | Samlekjøring av skattekort (bare aktive ansatte) | Må | 1 | GRFS 7.4. Årsskiftet for alle klienter |
| 15 | BY-30 | Beregningsgaranti, SLA og byråsupport i lønnsuka | Må | 3 | Tillit for en ny leverandør [E§10.8] |
| 16 | BY-25 + BY-26 | Lisensmodell: byrået betaler per slipp, ingen brukerlisens, volumtrinn og tak, sluttkunde-betaler som alternativ | Må | 3 | Gjør byrået til aktiv selger og gir forutsigbarhet |
| 17 | BY-28 + BY-29 | Kanalbeskyttelse og exit-pakke | Må | 3 | Fjerner partnerens to største frykter (konkurranse og konkurs) |
| 18 | BY-17 + BY-16 | Stedfortreder og masseomfordeling, og avdelingsoversikt | Må | 2 | Driftsrisiko ved fravær i lønnsuka |
| 19 | BY-23 + BY-27 | Generisk praksissystem-API (status, frister, klientregister) og bruksdata | Må | 2, 3 | Gjør praksissystemet til porteføljevisning og grunnlag for faktura |
| 20 | BY-36 | Avstemming: lønn mot a-melding (Må), regnskap og bank (Bør) | Må / Bør | 4 | GRFS 9.3. Gjentakende tilsynsfunn [E§2.6] |

**Like under topp 20:** BY-03 (KI-tolking av Excel og e-post), BY-14 (forklar lønnsslippen), BY-46 (Utleggsappen og Tikket inn), BY-49 (hierarkiet i datamodellen), BY-39 (compliance-pakke og ISAE 3402 type 1). BY-49 og BY-39 er Må, men lite synlige for brukerne.

---

## 6. Byråets lønnsdag: én dag i lønnsuka for lønnskonsulenten med 60 klienter

**Situasjonen [ans.]:** Det er tirsdag den 17. i lønnsuka. Lønnskonsulenten fra persona 1 har denne dagen:
- **22 klienter med lønn den 20.:** dagen er T-3, så kundegodkjenning og betalingsforslag må være ferdig i dag på grunn av bankens frist.
- **18 klienter med lønn den 25.:** fristen for grunnlag er i dag.
- **6 klienter som fikk lønn den 16.:** forskuddstrekket forfaller i dag (første virkedag etter) [B§4].
- **Kollega syk:** 5 av kollegaens klienter med lønn den 20. må dekkes.
- **Ny klient** overtatt fra et annet byrå.
- **2 åpne a-meldingsavvik** fra forrige måned.
- **1 sluttoppgjør**, som ekstrakjøring.

**«I dag»** betyr dagens verktøy: kundens Tripletex eller PowerOffice, Visma Payroll, Excel, e-post, nettbank og praksissystem.
**«Hos oss»** betyr samme dag i 2028 i vårt system, med 70 % strukturert grunnlag.

Klokkeslettene gjelder «i dag». I «hos oss»-kolonnen er stegene gjort etter hverandre fra 07:45, og radene står ved siden av hverandre bare for sammenligningens skyld.

| Tid | I dag | Min. | Hos oss | Min. |
|---|---|---|---|---|
| 07:45 | 23 nye e-poster fra klienter med Excel-timelister, «se vedlagt» og endringer. Sorterer manuelt per klient | 35 | Arbeidskøen (BY-01): 22 kjøringer for den 20. 13 er godkjent av kunden i går kveld på mobil, 6 har avvik og 3 venter på kunden. Kollegaens 5 klienter ligger allerede i køen hennes fordi lederen omfordelte dem kl. 07:30 (BY-17) | 10 |
| 08:20 | Sjekker hvem av klientene med lønn den 20. som har godkjent PDF-lønnslisten fra i går. 9 av 22 har svart. Purrer på e-post og telefon | 30 | Grunnlag: 17 innsendinger via lenke, 4 automatisk fra Tikket og Utleggsappen, og 2 Excel-filer på e-post som KI har gjort om til lønnslinjer. Hun godkjenner forslagene (BY-02, BY-03, BY-46) | 25 |
| 08:50 | Registrerer timer for 6 klienter med variable timer. Kopierer Excel inn i importmaler. Tripletex-klienten må ha ny kjøring fordi bare én import er tillatt | 80 | Avvikskøen: 31 avvik på ca. 300 slipper, hvert med forklaring. 24 kvitteres som forventet. 7 sendes som spørsmål til kunden i portalen (BY-04, BY-05) | 55 |
| 10:10 | Kontrollrapporter i tre systemer, eksport til Excel og sammenligning med forrige måned for 13 klienter | 70 | Kollegaens 5 klienter: leser klientinstruks og KI-oppsummering og går gjennom avvikene (BY-13) | 30 |
| 11:20 | Kollegaen er syk. Leter etter status i kollegaens notater og delte innboks, og ringer to kunder for å finne ut hva som er sendt | 45 | Ny klient: tilgangsdiagnosen viste for 3 dager siden at delegering manglet, og instruksen gikk automatisk til kunden. Status er nå grønn (BY-15) | 5 |
| 12:05 | Lunsj | – | Fire øyne: hun kontrollerer og signerer kollegaens kjøringer. Systemet hindrer at kollegaens kjøringer godkjennes av den som forberedte dem (BY-34) | 20 |
| 12:30 | A-meldingen for den nye klienten feiler med tilgangsfeil. Ringer kunden og forklarer hvordan tilgangspakken delegeres i Altinn. Venter | 30 | Kundegodkjenninger: 19 av 22 er godkjent. Påminnelse gikk automatisk kl. 09. Hun ringer én kunde (BY-43) | 10 |
| 13:00 | Lager betalingsfiler for 15 godkjente klienter og sender e-post: «Husk å godkjenne i nettbanken i dag.» For 4 fullmaktsklienter legger hun inn betalingen i kundens nettbank og må få en kollega til å godkjenne | 45 | Betalingsforslag (netto den 20., forskuddstrekk den 21. med KID) er levert til kundenes bank eller regnskapssystem. For 4 fullmaktsklienter legger hun det klart, og en annen person godkjenner (BY-44) | 15 |
| 13:45 | Forskuddstrekk for de 6 klientene med lønn den 16.: sjekker hvem som har betalt. 2 har glemt det. Lager KID og ringer | 30 | Oversikten over forskuddstrekk viser at 5 av 6 er bekreftet betalt. Den sjette har fått automatisk varsel både i går og i dag (BY-10) | 5 |
| 14:15 | Eksporterer lønnsjournal og importerer i kundens regnskapssystem for 8 klienter. Noe må registreres manuelt | 40 | Bilagene ble bokført automatisk i går for alle godkjente kjøringer. 2 feil i mappingen rettes i malen (BY-09, BY-19) | 10 |
| 14:55 | To a-meldingsavvik: slår opp feilkodene, retter og sender erstatningsmelding | 35 | Avvikene er forklart i klartekst med forslag. Det ene er allerede løst av siste erstatningsmelding. Det andre rettes (BY-08) | 15 |
| 15:30 | Lønn den 25.: sender purring til 11 av 18 som ikke har levert grunnlag | 25 | Lønn den 25.: systemet purret i går og i dag, og 13 av 18 har levert. Hun ringer 2 kunder | 10 |
| 15:55 | Sluttoppgjør som ekstrakjøring, med feriepenger og trekk regnet ut manuelt i regneark | 40 | Sluttoppgjørsveiviser i en egen kjøring. A-meldingen samles automatisk (BY-11) | 20 |
| 16:35 | Fører timer i praksissystemet etter hukommelsen | 15 | Timeforslag sendes automatisk til praksissystemet, og hun godkjenner dem der (BY-20) | 3 |
| 16:50 → 18:30 | Overtid: 7 av 22 kjøringer for den 20. er ikke godkjent av kunden, og 3 av kollegaens klienter er ikke kontrollert | 100 | Ferdig ca. kl. 12:15 med dagens fristarbeid (inkludert lunsj). Resten av dagen går til forberedelse av lønn den 25. (som allerede er beregnet) og 2 nye klienter i migreringsbølge 3 | – |
| **Sum fristarbeid** | | **ca. 620 min (10,3 t), med 3 av kollegaens klienter uferdige** | | **ca. 233 min (3,9 t), med alle 27 klienter ferdige** |

**Hva tidslinjen viser**
- **Det store hoppet** kommer fra innhenting (lenke og integrasjoner), kontroll (avvikskø) og etterarbeid (bilag og a-melding). Beregningen tar like lite tid i begge tilfeller.
- **Robusthet:** Kollegaens sykdom koster ca. 50 minutter hos oss (overlevering og fire øyne). I dag koster den 45 minutter med leting, en stor del av overtiden, og arbeid som likevel ikke blir ferdig.
- **Ny risiko fra 2026:** Det daglige forskuddstrekket er en ny, tilbakevendende kilde til feil og telefoner. Systemet fjerner den nesten helt.
- **Forbehold:** Besparelsen forutsetter at minst ca. 70 % av kundene bruker innsending og godkjenning digitalt. Uten det faller besparelsen i innhentingssteget med to tredjedeler (kap. 4.3).

---

## 7. Ting vi bevisst IKKE skal bygge for byråer

| # | Ikke bygg | Hvorfor | Hva vi gjør i stedet |
|---|---|---|---|
| 1 | **Praksissystem-funksjoner:** oppgaver, rutiner, timeføring, fakturering, lønnsomhet, kapasitet, oppdragsavtaler, CRM og KYC | Praksissystemene har dette allerede [Tally-grensesnitt], [E§2.4]. Vi ville tapt både fokus og partnere | API, webhooks, bruksdata og timeforslag (BY-23, BY-27, BY-20) |
| 2 | **Lønn som tjeneste, BPO eller kapasitetshjelp i lønnsuka** | Godkjenningsplikt og resultatansvar [E§2.1]. Kanalkonflikt [A§2.1] | Henvis til partnerbyråer |
| 3 | **Betalingsinitiering fra egen konto, klientmidler eller egen PSD2-lisens** | Regulatorisk byrde. Feil håndtering av trekkmidler er et tilsynsfunn [E§2.6] | Betalingsforslag som kunden godkjenner i egen bank (BY-44) |
| 4 | **Blind massesending av a-meldinger** | En erstatningsmelding erstatter hele den forrige [B§2.4] | «Send alle som er klare» med port per klient |
| 5 | **Full white-label** (egen app i butikkene, skjult leverandør) | Kostnad uten betalingsvilje. Vi bygger ingen merkevare | «Powered by» med logo (BY-54) |
| 6 | **Rik kundeportal** med dokumentarkiv, chat og rapportbibliotek | Brukes ikke av små kunder. Byrået har egne kanaler | Minimal portal (2.3) |
| 7 | **Autonom KI som godkjenner, sender inn eller utbetaler** | Ansvaret ligger hos arbeidsgiver og byrå. Tilliten er ikke på plass [G§2.4] | KI forbereder, forklarer og flagger, og agentrollen er sperret [F§3.3] |
| 8 | **Fristsystem for klienter som ligger i andre lønnssystemer** | Praksissystemet gjør dette | Lønnsstatus sendes til praksissystemet |
| 9 | **Pris per byråbruker og oppstartsgebyr per klient** | Straffer gode byråpraksiser (fire øyne, stedfortreder) | Pris per slipp (BY-26) |
| 10 | **Spesialtilpasninger i kode per byrå** | Ødelegger modellen med én kodebase og kontrollen i release-diff [F§7.6] | Konfigurasjon, maler og et begrenset uttrykksspråk for lønnsarter [F§0 pkt. 4] |
| 11 | **Egne integrasjoner mot alle praksissystemer samtidig** | Små markeder hver for seg, og API-ene er ikke kartlagt | Generisk API først, deretter 1–2 egne integrasjoner styrt av designpartnerne |
| 12 | **Vedlikehold av lovpålagte satser og regler hos byrået** | Satser og regler er vårt ansvar | Sentrale, versjonerte regelpakker [F§1.3] |
| 13 | **Markedsplass med inntektsdeling** | For tidlig før ca. 30–50 integrasjoner [G§0 pkt. 10] | Partnerprogram light og åpent API |
| 14 | **Overvåkingsdashbord per lønnsmedarbeider** | Kultur, personvern og frafall | Aggregerte kvalitetstall (BY-21) |
| 15 | **Citrix eller skrivebordsklient** | Kjent smerte hos SD Worx [E§9.2] | Ren nettløsning |
| 16 | **Tvungen flytting av små klienter (under 10 ansatte) fra kundens Tripletex eller PowerOffice** | Lønnsmodulen er allerede betalt der. Lav gevinst | Fokus på klienter med 10–300 ansatte. De små kan komme senere |

---

## 8. Åpne spørsmål til intervjuer og verifisering

1. **Portaladopsjon:** Hvor stor andel av byråenes kunder med 10–50 ansatte vil faktisk sende inn og godkjenne digitalt? Dette er den viktigste antakelsen i business caset (4.3). *Test med 10–15 fagledere for lønn [E§11].*
2. **Hvem trykker betal:** Hvordan fordeler det seg mellom kunde og byrå med fullmakt? Det finnes ingen offentlig statistikk [E§1.3].
3. **NAV via byrå:** Kan en systembruker for klientsystem med regnskapsførerpakker sende inntektsmelding, eller kreves `lonn-personopplysninger-saerlig-kategori` delegert separat? [B§1.3]
4. **Bank:** Kan én pain.001-fil med flere utførelsesdatoer brukes i de største bankene? Kan Tripletex og PowerOffice ta imot betalingsforslag fra et eksternt lønnssystem via API?
5. **Praksissystemer:** Hvilke praksissystemer bruker byråene i segment B, og hvilke API-er har Maestro, Duett, Visma Practice og Sticos Oversikt for status, frister og tid? (Hull fra E§11 er fortsatt åpent.)
6. **Pristoleranse:** Hvor går smertegrensen per slipp når lisensen viderefaktureres og når byrået absorberer den? Foretrekker byråene årsavtale med tak?
7. **Fusjoner i kjeder:** Hvordan håndteres klientdelegering i praksis når byråer fusjoneres? Bekreftes med Digdir [B§1.2].
8. **Byråets egen lønn som pilot:** Har designpartnerne en egen lønnsavdeling med variable elementer som er representativ nok?
9. **A-melding 2.4:** Hvordan rettes perioder i 2027 etter at versjon 2.4 er tatt i bruk fra 2028-01? Det påvirker migreringer i januar 2028 [B§14 pkt. 11].

---

## Kilder

**Interne (runde 1):**
- `E-byra.md` (hovedkilde)
- `B-myndigheter.md`: systembruker, skattekort, a-melding og betaling av forskuddstrekk
- `A-marked-konkurrenter.md`: konkurrenter, SD Worx Services Norway AS og kjøpsmodeller
- `F-arkitektur.md`: multi-tenant, tilgangsmodell, migrering, drift og tidslinje
- `D-praksis.md`: tidsbruk, kontrollrapporter og arbeidsdeling
- `G-moduler-2026.md`: modulkontrakter, KI, byråenes digitalisering og «wow»-listen
- `C-beregning.md`: migrering av saldoer hittil i år og tariffbibliotek

Alle filene ligger i samme mappe som denne rapporten.

**Observasjon i økten:** Tallys MCP-grensesnitt, bare verktøybeskrivelser (`list_deadlines`, `log_time`, `list_invoice_basis`, `profitability`, `kapasitet`, `request_amelding_report`, `frister_fra_staten`, `create_task_from_routine`). Ingen kundedata er lest.

**Eksterne (nettsøk i runde 2, med lite funn):**
- [Sticos – integrasjoner](https://www.sticos.no/integrasjoner)
- [Unimicro – Maestro Årsoppgjør](https://unimicro.no/integrasjoner/maestro-årsoppgjør)

**Viktigste primærkilder, gjengitt via runde 1:**
- [GRFS](https://www.regnskapnorge.no/globalassets/dokumenter/vedtekter/grfs---fom.-2023---masterfil.pdf)
- [Regnskapsførerloven](https://lovdata.no/dokument/NL/lov/2022-12-16-90)
- [Altinn – systembruker](https://docs.altinn.studio/nb/authorization/guides/system-vendor/system-user/)
- [Skatteetaten – betaling av forskuddstrekk og AGA](https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/arbeidsgiveravgift/betaling-av-forskuddstrekk-og-arbeidsgiveravgift/)
- [Finanstilsynet – tematilsyn om betalingsoppdrag](https://www.finanstilsynet.no/contentassets/759a5db7872849ae817375466fb830e1/regnskapsforeres-betalingsoppdrag---tematilsyn-2018.pdf)
- [Regnskap Norge – Lønnssystemer 2025](https://www.regnskapnorge.no/contentassets/b173a1e31cd741af9b610fc80db70ddf/lonnssystemer---resultater-til-publisering.pdf)
