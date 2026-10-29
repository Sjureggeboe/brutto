# R2 – Behov rundt lønna: ansatte, ledere og organisasjonslivet

**Runde 2 av behovskartleggingen** · Dato: 28. oktober 2026
**Til:** Gründerteamet for nytt frittstående lønnssystem (SaaS, 10–1000 ansatte, også byrålisens)
**Bygger på:** R1-rapportene A–G (særlig G del 1.4–1.5, B1–B7, del 2.6 og wow-listen i del 3), C (lønnsartmatrisen), D (kap. 3, 7 og 10) og F (tilgangsmodell, kap. 3.3). Hullene er fylt med nettsøk mot Skatteetaten 28.10.2026.

**Hvor sikre påstandene er** (samme merking som i G):
- **[P]** Bekreftet i primærkilde (Skatteetaten, Lovdata, offisiell dokumentasjon).
- **[S]** Sekundærkilde (Sticos, Smarte Penger, rådgivere, bransjeorganisasjoner).
- **[U]** Usikkert eller ikke verifisert. Må sjekkes med Skatteetaten eller revisor før det bygges inn som regel.
- **[V]** Min vurdering eller anbefaling.

**To presiseringer mot R1:**
- I G er **OrgLab** brukt som eksempel på en *HR-modul* og **Tikket** som en *tidsmodul*. I denne runden følger jeg oppdragets definisjoner: **OrgLab = medlemssystem** (medlemmer, tillitsvalgte, styrer, kontingent) og **Tikket = billettsalg og arrangement**. Tid/vakt og HR er egne moduler (egne eller fra tredjepart). Derfor trengs to nye kontrakter: **B8 OrgLab → lønn (verv og godtgjørelse)** og **B9 Tikket → lønn (arrangement, bemanning og honorar)**. Begge er beskrevet i kapittel 2.
- **Nytt krav fra gründeren (lagt inn i denne versjonen):** Lønnssystemet får **egne moduler for ferie/fravær, timer og utlegg**. *Ferie/fravær* dekker søknad, godkjenning, saldo, egenmelding og sykmelding. *Timer* dekker registrering, overtid og godkjenning. *Utlegg* dekker reise og kvittering. Modulene bygges på **det samme offentlige API-et** som eksterne systemer bruker (kontraktene B1 og B3 i G, og den nye B10 i kap. 2.6). Kunden kan bytte dem ut med for eksempel Utleggsappen eller et eksternt tidssystem. Behovene står i kap. 3 (AN-21–AN-36), kap. 4 (LE-14–LE-19) og kap. 11 (app-skissen). Konsekvensene for arkitekturen står i kap. 2.6.
- Rapporten har to runder. **Runde A** var et bredt utkast. **Runde B** kritiserte det med tre spørsmål: hva er gimmick, hva øker risikoen for svindel og feil, og hva er juridisk feil? Behovstabellene viser resultatet etter runde B. Kapittel 9 viser hva som ble endret og hvorfor.

---

## 0. Hovedfunn

1. **Det viktigste skillet er ikke ansatt eller ikke ansatt. Det er hvilken av sju mottakerklasser personen tilhører.** Klassen styrer a-melding, skattetrekk, arbeidsgiveravgift (AGA), feriepenger og pensjon. Klassene er: arbeidstaker, honorar- eller vervmottaker, mottaker av bare utgiftsgodtgjørelse, næringsdrivende (ENK/AS), utenlandsk artist (artistskatt), frikjøpt tillitsvalgt via egen arbeidsgiver, og ulønnet frivillig. Mottakerklassen skal være et eksplisitt, versjonert og begrunnet felt per utbetaling. Den skal ikke kunne utledes av hvilken modul en linje kom fra. [V]
2. **Styrehonorar og vervgodtgjørelse rapporteres med arbeidsforholdstypen «frilanser, oppdragstaker og personer som mottar honorarer», og bare i månedene det utbetales** [P]. Ytelsen skal alltid oppgis som trekkpliktig, og det skal beregnes AGA [P]. Den gir ikke feriepenger og er ikke pensjonsgivende [P/S, jf. C]. Tillitsvalgte er altså *ikke* ansatte, men de er heller ikke usynlige for a-meldingen.
3. **Personer som bare får utgiftsgodtgjørelse skal ikke ha arbeidsforhold i a-meldingen** [P]. Selve godtgjørelsen kan likevel være opplysningspliktig. Hovedgrensen for opplysningsplikt er **2 000 kr lønn per person per år**, og **1 000 kr for utgiftsgodtgjørelse** [P, Skatteetaten 28.10.2026]. Utlegg mot bilag rapporteres ikke [P/S, jf. C #46]. For frivillige betyr det: Utleggsappen ja, arbeidsforhold nei.
4. **10 000-kronersregelen for skattefrie organisasjoner (sktl. § 2-32) har tre sider som ofte blandes sammen** [P]:
   - Organisasjonen har ikke opplysningsplikt under 10 000 kr per person per år. Den kan alternativt bruke regelen «Skattefri organisasjon» fra første krone.
   - Mottakeren er skattefri for lønn under 10 000 kr fra organisasjonen [P]. Grensen gjelder trolig per organisasjon [S].
   - **AGA skal likevel beregnes av alt** [P], med mindre fritaket i ftrl. § 23-2 gjelder (veldedig eller allmennyttig, samlet lønn ≤ 800 000 kr og ≤ 80 000 kr per person) [P].

   Systemet trenger en akkumulator per mottaker per betalende enhet, og det må ikke «optimalisere» på tvers av enheter. [V]
5. **Hvem som er arbeidsgiver, er ofte uklart i organisasjoner med lokallag.** Et lokallag med eget organisasjonsnummer er selv opplysningspliktig og skal levere egen a-melding hvis det betaler honorar. Hvis sentralleddet betaler, er det sentralleddet som er opplysningspliktig. Hver utbetaling må derfor ha en **betalende juridisk enhet**. Sentralleddet bør kunne kjøre lønn for lokallagene som klienter, på samme måte som et byrå. [V]
6. **Artister og foredragsholdere går i fire ulike spor.**
   - Norsk privatperson får honorar via lønn (frilanser-type).
   - ENK som fakturerer betales via leverandørreskontro. Kjøperen har da plikt til å rapportere betalinger til ENK uten fast forretningssted innen 15. februar (RF-1301/RF-1321). Plikten gjelder også skattefrie foreninger, og det er ingen beløpsgrense [P].
   - AS betales mot faktura uten rapportering.
   - Utenlandsk artist som ikke er bosatt i Norge, får **artistskatt på 15 %**. Det skal sendes RF-1091 tre uker før arrangementet og RF-1092 senest sju dager etter trekket. Dette går **ikke** i a-meldingen og gir **ikke** grunnlag for AGA [P].

   Et lønnssystem som bare kan «lønn», gir feil i tre av fire spor.
7. **Ekstrahjelp og vakter på arrangementer er arbeidstakere**, ikke frivillige og ikke honorarmottakere. De rapporteres som midlertidig ansatt eller tilkallingsvikar, med stillingsprosent 0 og timelønn med antall timer [P/S]. De får feriepenger, og normalt OTP fra første krone [S/U]. Det er Tikket-integrasjonen som avgjør om timene blir korrekte.
8. **Tapt arbeidsfortjeneste og frikjøp er de største hullene i kunnskapsgrunnlaget.** Jeg fant ingen eksplisitt veiledning fra Skatteetaten om tapt arbeidsfortjeneste for tillitsvalgte i frivillige organisasjoner [U]. Beste anslag er at det rapporteres som «styrehonorar og godtgjørelse i forbindelse med verv», med trekk og AGA [U/V]. Frikjøp har tre modeller med helt ulik behandling (kap. 7). Produktet må støtte alle tre og la organisasjonen velge, med dokumentasjon. [V]
9. **De to største svindelvektorene i organisasjonslivet er endret kontonummer og fiktive verv eller honorarer.** Ansatte trenger et kontonummer-skjold. For ikke-ansatte trengs i tillegg at den som oppretter et verv i OrgLab ikke kan godkjenne utbetalingen, at honorarer refererer til et vedtak, og at onboardingen skjer med BankID der navnet må stemme med OrgLab. [V]
10. **Ansattappen skal være én app med roller, ikke tre apper.** Samme person kan være ansatt, tillitsvalgt med honorar, attestant i et lokallag og frivillig. Appen viser «lønn», «fravær og ferie», «timer», «utlegg», «honorar og verv» og «godkjenninger» etter hvilke relasjoner personen har og hvilke moduler kunden bruker. Hver fane har sin egen tilgangsregel. [V]
11. **Egne moduler for ferie/fravær, timer og utlegg må være utbyttbare i praksis, ikke bare på papiret.** Det krever tre ting [V]:
    - Modulene bruker bare offentlige kontrakter (B1, B3 og B10), uten bakdører.
    - Hvert domene har én eier per kunde. Det er enten egen modul eller et eksternt system.
    - Lederens godkjenningsinnboks og ansattappens oversikt bygges på en felles kontrakt for **godkjenningsoppgaver og status** (B10), ikke på interne tabeller i egne moduler.

    Hvis kunden bytter til Utleggsappen, skal innboksen og appen fortsatt fungere. Det er testen på om plattformen er ekte (G 1.12).

---

## 1. Avgrensning: hva lønn eier, og hva den ikke skal eie

| Område | Eier | Lønn får | Lønn skal *ikke* få |
|---|---|---|---|
| Medlemskap, kontingent, medlemshistorikk | OrgLab | Ingenting | Medlemsregister og kontingent. Medlemskap i fagforening, parti, trossamfunn eller pasientforening kan avsløre særlige kategorier etter GDPR art. 9 [P/V] |
| Verv (organ, rolle, periode, lokallag) | OrgLab | Bare verv som gir rett til godtgjørelse, og bare når det skal utbetales | Alle 3 000 tillitsvalgte «for sikkerhets skyld» |
| Honorarpolitikk (satser per verv og møte, tak) | Lønn (regler), vedtatt av styret | Vedtaksreferanse fra OrgLab (styremøte, protokoll) | – |
| Arrangement, billetter, vakter, innsjekk | Tikket | Arrangement-ID (dimensjon), godkjente timer, honoraravtaler, utlegg dekket av arrangør | Billettkjøpere og publikumsdata |
| Ferie, fravær, egenmelding, sykmelding | **Egen modul «Fravær og ferie»** *eller* eksternt HR- eller tidssystem (B3/B10) | Godkjent fravær med type, grad og periode. Saldo hvis kjernen eier den | Diagnose eller helseopplysninger utover det NAV-flyten krever |
| Timer og overtid for ansatte | **Egen modul «Timer»** *eller* eksternt tid- eller vaktsystem (B3/B10) | Godkjente timer per timetype og dimensjon | Rå GPS- eller posisjonsdata |
| Utlegg og reise | **Egen modul «Utlegg»** *eller* Utleggsappen (B1/B10) | Fakta, forslag til klassifisering og kvitteringsreferanse (hash) | – |
| Fødselsnummer, kontonummer, skattekort | **Lønn** (via BankID-onboarding og Skatteetaten) | – | Aldri fra OrgLab eller Tikket. Lønn innhenter dem selv, akkurat når de trengs [V] |
| Mottakerklasse, a-melding, trekk, AGA, utbetaling | **Lønn** | – | – |

---

## 2. Grunnmodell: ansatte og ikke-ansatte mottakere

### 2.1 Sju mottakerklasser

| Klasse | Typiske personer | Arbeidsforhold i a-meldingen | Betales via | Kilde |
|---|---|---|---|---|
| **K1 Arbeidstaker** | Ansatte, ekstrahjelp, vakter med timelønn, midlertidige | Ordinært (fast, midlertidig eller tilkalling) | Lønn | [P] |
| **K2 Honorar- eller vervmottaker** | Styremedlem, tillitsvalgt med godtgjørelse, foredragsholder uten næring, dommer eller instruktør med honorar | «Frilanser, oppdragstaker og personer som mottar honorarer», bare i utbetalingsmåneder | Lønn | [P] |
| **K3 Mottaker av bare utgiftsgodtgjørelse** | Frivillig eller tillitsvalgt som bare får dekket reise og utlegg | **Ingen** arbeidsforhold. Utgiftsgodtgjørelser rapporteres etter beløpsgrensene | Utleggsappen → lønn (rapportering) eller bank (refusjon) | [P] |
| **K4 Næringsdrivende** | ENK eller AS som fakturerer (artist, foredragsholder, vaktselskap) | Ingen. For ENK uten fast forretningssted: RF-1301/1321 innen 15.2 | Leverandørreskontro (regnskap) | [P] |
| **K5 Utenlandsk artist eller idrettsutøver** | Artist som ikke er skattemessig bosatt i Norge | Ingen. Artistskatt 15 % via RF-1091 og RF-1092. Ikke AGA | Lønn (trekkmodul) eller leverandørreskontro med trekk | [P] |
| **K6 Frikjøpt tillitsvalgt (modell A)** | Tillitsvalgt der egen arbeidsgiver fortsetter å betale lønn og fakturerer organisasjonen | Ingen hos organisasjonen. Arbeidsgiveren rapporterer | Leverandørreskontro | [V/S] |
| **K7 Ulønnet frivillig** | Frivillige på arrangement uten noen utbetaling | Ingen | – (eventuelt K3) | [V] |

**Regel [V]:** En *person* kan ha flere klasser samtidig. En ansatt kan for eksempel også være styremedlem (K1 + K2) og frivillig på et arrangement (K7). Klassen tilhører **relasjonen og utbetalingen**, ikke personen.

### 2.2 Datamodell (tillegg til G 1.4)

```
Person (Personkatalog)                         ← felles. Lønn eier fnr/D-nr og kontonummer
 ├─ Rolle i OrgLab (medlem, tillitsvalgt, …)   ← eies av OrgLab. Speiles IKKE til lønn
 ├─ Arbeidsforhold (K1)                        ← a-melding: ordinært
 ├─ Oppdragsforhold (K2)                       ← a-melding: frilanser/oppdragstaker/honorar
 │    └─ grunnlag: vervId | oppdragId | engasjementId (fra OrgLab/Tikket)
 ├─ Utgiftsmottaker (K3)                       ← ingen arbeidsforhold
 └─ Leverandør (K4/K5/K6)                      ← regnskap/leverandørreskontro. RF-1301-flagg / artistskatt-flagg

Utbetalingsgrunnlag (PayInput, G 1.11) får nye felt:
  betalendeEnhet (orgnr + underenhet)   – hvem er opplysningspliktig
  mottakerklasse (K1–K7)                – versjonert, med begrunnelse og hvem som avgjorde
  hjemmel/vedtak-ref                    – styrevedtak, honorarsats, avtale
  dimensjoner                           – lokallag, prosjekt, tilskudd, arrangement
  skattefriOrgRegel                     – TERSKEL | FRA_FØRSTE_KRONE | IKKE_AKTUELL
```

**Klassifiseringsbeslutningen er et eget objekt** [V]: spørsmål og svar fra veiviseren (2.5), dokumentasjon (for eksempel at personen fakturerer fra ENK med orgnr), dato, hvem som avgjorde og når den skal vurderes på nytt. Ved bokettersyn kan organisasjonen da vise *hvorfor* en foredragsholder ble behandlet som næringsdrivende.

### 2.3 Kontrakt B8: OrgLab → lønn (verv og godtgjørelse) [V]

**OrgLab eier vervet. Lønn eier pengene.** OrgLab sender aldri fødselsnummer eller kontonummer. Lønn henter dem ved å invitere personen til BankID-onboarding (flyt F4, kap. 11).

| Retning | Hendelse | Nøkkelfelt |
|---|---|---|
| OrgLab → lønn | `org.verv.compensable.created/changed/ended.v1` | vervId, personRef (Personkatalog), organ (styre, landsstyre, lokallagsstyre, utvalg), rolle, fra/til, lokallag (orgUnit og eventuelt eget orgnr), godtgjørelsesordning-ref, dimensjoner |
| OrgLab → lønn | `org.meeting.attendance.attested.v1` | møteId, organ, dato, varighet, deltakere (personRef), attestert av (møteleder), reise registrert ja/nei |
| OrgLab → lønn | `org.compensation.policy.adopted.v1` | Vedtak: dato, organ, protokoll-ref (dokument-URL og hash), satser per verv og møte, tak, gyldighet |
| OrgLab → lønn | `org.lost_earnings.claim.submitted.v1` | Krav om tapt arbeidsfortjeneste: dato og timer, møte- eller oppdragsref, kravtype (lønnstaker eller næringsdrivende), dokumentasjon (vedlegg og hash), krevd sats |
| OrgLab → lønn | `org.release_agreement.registered.v1` | Frikjøpsavtale: modell A/B/C, prosent, periode, motpart (arbeidsgivers orgnr), refusjonsgrunnlag |
| Lønn → OrgLab | `payroll.recipient.onboarding.status.v1` | invitert, BankID-verifisert, skattekort hentet, klar for utbetaling (uten persondata) |
| Lønn → OrgLab | `payroll.input.accepted/rejected.v1` | Årsakskoder fra G og nye: `NO_POLICY_REFERENCE`, `ATTENDANCE_NOT_ATTESTED`, `CAP_EXCEEDED`, `RECIPIENT_NOT_ONBOARDED`, `SOD_VIOLATION` |
| Lønn → OrgLab | `payroll.payrun.paid.v1` (filtrert) | Utbetalt brutto per verv (til OrgLab-rapport om godtgjørelser per organ), aldri netto eller trekk |

**Idempotens:** `(OrgLab, vervId|møteId|kravId, revisjon)`, med samme livssyklus som G (RECEIVED → … → REPORTED).

### 2.4 Kontrakt B9: Tikket → lønn (arrangement, bemanning og honorar) [V]

| Retning | Hendelse | Nøkkelfelt |
|---|---|---|
| Tikket → lønn | `event.created/changed/cancelled.v1` | eventId, navn, dato(er), sted (adresse og kommune), arrangør (orgnr og underenhet), prosjekt- eller kostnadssted |
| Tikket → lønn | `event.shift.staffed.v1` | shiftId, eventId, rolle, personRef, **engasjementstype: FRIVILLIG \| ARBEIDSTAKER \| INNLEID**, planlagte timer |
| Tikket → lønn | `event.shift.attendance.approved.v1` | Inn- og utsjekk, pauser, godkjent av, timer per timetype (kveld, natt, helg). Lønn priser timene |
| Tikket → lønn | `event.performer.engaged.v1` | engagementId, eventId, utøvertype (PERSON_NO, ENK, AS, UTENLANDSK_ARTIST, AGENT), avtalt honorar, valuta, fordeling mellom kunstnerisk og annet arbeid, arrangørdekkede kostnader (reise, hotell, kost), forfallsdato, kontrakt-ref |
| Tikket → lønn | `event.revenue.summary.v1` | Billettinntekter per arrangement (til kostnadsoversikten, og fordi plassutleier kan bli trekkpliktig for artistskatt) [P] |
| Lønn → Tikket | `payroll.event.cost.updated.v1` | Faktisk og estimert lønnskostnad per arrangement: brutto, feriepenger, AGA, OTP, honorar og artistskatt (aggregert, ikke per person) |
| Lønn → Tikket | `payroll.worker.ready.v1` | Ekstrahjelp er klar: arbeidsavtale signert, skattekort hentet og konto verifisert (ja/nei) |

**Viktig regel [V]:** Tikket kan aldri sende en *frivillig*-vakt med beløp. Hvis en frivillig skal ha penger, må engasjementet først klassifiseres om (K2, K3 eller K1). Det stopper «svart honorar fra kassa» og feilrapportering.

### 2.5 Klassifiseringsveiviser: «hvem betaler vi?» [V, bygger på P-kilder]

```
1  Er mottaker et AS/ANS/SA eller annet selskap?           → K4 faktura. Ingen a-melding
2  Er mottaker et ENK som fakturerer og reelt driver næring
   (egen regning og risiko, flere oppdragsgivere,
   resultatansvar)?                                          → K4 faktura. RF-1301-flagg hvis
                                                               ENK uten fast forretningssted [P]
3  Er mottaker en utenlandsk artist/idrettsutøver
   som ikke er skattemessig bosatt i Norge?                  → K5 artistskatt 15 %, RF-1091/1092 [P]
4  Er mottaker ansatt hos betalende enhet?
     4a ekstra arbeid/foredrag                               → K1 honorar på ordinært arbeidsforhold
     4b styreverv (f.eks. ansattrepresentant)                → styrehonorar [P]. Arbeidsforholdstype [U]
5  Er det et verv (styre, råd, utvalg, tillitsverv)?        → K2 «styrehonorar og godtgjørelse
                                                               i forbindelse med verv» [P]
6  Er det arbeid under instruks, med tid og sted
   bestemt av oss (vakt, rigg, kasse)?                       → K1 arbeidstaker (midlertidig/tilkalling)
7  Er det et avgrenset oppdrag uten instruks
   (foredrag, kurs, dommer)?                                 → K2 honorar, frilanser-type [P]
8  Bare refusjon av utlegg eller trekkfrie godtgjørelser?   → K3. Ingen arbeidsforhold [P]
9  Ingen utbetaling?                                         → K7 (ikke i lønn)
Deretter: Er betalende enhet skattefri (sktl. § 2-32)?       → 10 000-regelen (TV-09)
          Er betalende enhet veldedig/allmennyttig
          under 800 000 / 80 000?                            → AGA-fritak og forenklet a-melding [P]
```

Grensen mellom arbeidstaker og selvstendig næringsdrivende avgjøres av de faktiske forholdene, ikke av hva avtalen kaller forholdet [P/S] ([Skatteetaten, prinsipputtalelse](https://www.skatteetaten.no/nn/rettskjelder/type/uttalelser/prinsipputtalelser/grensedragningen-mellom-arbeidstakere-og-selvstendig-naringsdrivende/)). Veiviseren gir derfor et **forslag med begrunnelse**, og en person må signere. Den avgjør ikke. [V]

### 2.6 Egne moduler for ferie/fravær, timer og utlegg, og hvordan de kan byttes ut [V]

**Prinsipp:** Egne moduler er «førstepartsmoduler» med samme status som Utleggsappen eller et eksternt tidssystem. De har egne datalagre og snakker med lønnskjernen bare gjennom de offentlige kontraktene. Kjernen vet ikke om lønnsgrunnlaget kom fra en egen modul eller fra en ekstern.

| Modul | Eier (når aktiv) | Kontrakt til kjernen | Kjernen eier fortsatt | Kan byttes med |
|---|---|---|---|---|
| **Fravær og ferie** | Søknader, godkjenninger, fraværsperioder (type, grad), egenmeldingskvote, feriekalender, *visning* av saldo | B3 (`absence.*`, `leave.*`) og B10 | Feriepenger, trekk i lønn for ferie, arbeidsgiverperiode og sykepengeberegning, inntektsmelding og refusjon fra NAV, permisjoner i a-meldingen. Feriedagssaldo eies av kjernen *eller* modulen per kunde (G B3) | HR-system (Simployer, Sympa o.l.) eller tid/vakt-system |
| **Timer** | Registrering, overtid med begrunnelse, valg mellom avspasering og utbetaling, periodelås, godkjenning | B3 (`time.period.approved` m.fl.) og B10 | Prising (satser, tillegg, overtidsprosent), avspaseringsverdi i sluttoppgjør, AGA og feriepengegrunnlag | Tid/vakt-system, Tikket (innsjekk) for arrangement |
| **Utlegg** | Kvitteringsfoto, OCR-forslag, reiseregning (km, diett, overnatting), attestasjon, policy | B1 og B10 | Endelig klassifisering (trekkfri eller trekkpliktig), utbetaling, a-melding | Utleggsappen |

**Ny kontrakt B10: godkjenningsoppgave og status** (forutsetning for én innboks og én app):

| Retning | Hendelse | Nøkkelfelt |
|---|---|---|
| Modul → kjerne | `approval.task.created/updated/withdrawn.v1` | taskId, kilde (modul og tenant), type (ferie, fravær, timer, overtid, utlegg, reise, vervkrav), søker (personRef), godkjenner eller rolle, frist (gjerne utledet av lønnens cut-off), sammendrag uten sensitive data, beløp eller estimat, avviksflagg med begrunnelse, dyplenke eller innebygd visning, `actions` (godkjenn, avvis, send tilbake) |
| Kjerne → modul | `approval.task.decided.v1` | taskId, beslutning, kommentar, beslutter, tidspunkt, sterk autentisering ja/nei |
| Modul → kjerne | `employee.item.status.v1` | Status til ansattappen: «søkt», «godkjent», «utbetales med lønn 20.11», «avvist: mangler kvittering» |

**Det som må gjelde for at modulene skal kunne byttes ut [V]:**
1. **Én eier per domene per kunde.** For eksempel utlegg: egen modul *eller* Utleggsappen. I en overgangsperiode kan begge levere, men da fjernes duplikater med kvitteringshash og `(kilde, eksternId)`. Kjernen avviser data om et domene fra en kilde som ikke er registrert som eier (`SOURCE_NOT_OWNER`).
2. **Ingen bakdører.** Egne moduler kan ikke bruke interne tabeller i kjernen. Det testes med kontrakttester i CI som kjøres mot både egen modul og en referanseimplementasjon av en ekstern modul.
3. **Innboksen og appen leser bare B10.** En ekstern modul som ikke støtter B10, vises med dyplenke («Godkjenn i Utleggsappen») og telles med i innboksen. Den forsvinner ikke.
4. **Bytte uten tap av historikk.** Når kunden bytter modul, ligger historiske godkjenninger og bilag igjen hos kjernen som referanser og hash. Ansatte ser fortsatt gamle utlegg og fravær i appen (lesekopi).
5. **Regler som er lovpålagte ligger i kjernen eller i en felles regeltjeneste**, ikke i hver modul: satser for diett og km, AML-grenser for overtid og egenmeldingsregler. Da følger reglene med når en modul byttes. Eksterne moduler kan få et *forslag* (G B1, «fakta + forslag»).

---

## 3. Persona 1 – Ansatt (mobil først)

**Kontekst.** Kari (34) er ansatt i en interesseorganisasjon med 60 ansatte. Hun har fastlønn, tar av og til kveldsmøter, reiser med Utleggsappen og har OTP. Kollegaen Andrii (41) er timelønnet i renhold og bruker ukrainsk og engelsk. Begge bruker telefonen og åpner lønnsslippen «når noe ser rart ut». Referansen deres er DFØ-appen og nettbanken [S, jf. D 10].

**Jobber som skal gjøres**
- Forstå *hvorfor* netto er som den er denne måneden, uten å spørre lønn.
- Vite når og hvor mye som kommer: lønn, feriepenger og utlegg.
- Sjekke at skattetrekket er riktig og vite hva hun kan gjøre selv.
- Endre kontonummer og kontaktinfo trygt.
- Finne dokumentasjon: slipper, årsoversikt og avtaler, også etter at hun har sluttet.
- Søke ferie, melde egenmelding eller sykt barn, føre timer og levere utlegg fra telefonen på under ett minutt per gang, og se status uten å purre.

**Smerter**
- Juni og desember forvirrer: feriepenger, trekk i lønn for ferie og halv skatt. Overtid og honorar trekkes likevel fullt i desember [P, jf. C].
- 50 % trekk fordi skattekortet manglet, uten at noen sa fra.
- Utlegg forsvinner i et «svart hull» mellom godkjenning og utbetaling.
- Lønnsslippen er full av koder, og bare norsk.
- E-post med vedlegg eller passord på SMS. Tilgangen forsvinner når hun slutter [S, jf. D 10].
- Ferie avtales på e-post eller i Excel, og saldoen er usikker. Egenmelding sendes på SMS til lederen. Timelister og kvitteringer leveres på papir eller i tre forskjellige systemer.

**Behov (etter runde B)**

| ID | Behov | MoSCoW | Merknad, risiko og avhengighet |
|---|---|---|---|
| AN-01 | Lønnsslipp på mobil og i Digipost, med arkiv | Må | G B7. Varsel *uten* beløp |
| AN-02 | **Forklart lønnsslipp**: deterministisk endring mot forrige måned (feriepenger, trekk i lønn for ferie, halv skatt, etterbetaling, nye tillegg, egenmeldingsdager) | Må | Hentes fra beregningsgrafen (G #3), ikke fra en språkmodell. Hevet fra Bør i runde B |
| AN-03 | Neste lønn: dato og foreløpig estimat etter cut-off | Bør | Merket «foreløpig». Vises ikke før cut-off, for å unngå feil forventninger |
| AN-04 | Skattekortstatus: tabell, prosent eller frikort, hentet dato, forklaring ved 50 %-trekk og lenke til Skatteetaten | Må | Ikke skatterådgivning. Ingen «du bør endre til X» |
| AN-05 | Be om frivillig ekstra forskuddstrekk (beløp eller prosent) | Bør | Støttes i a-meldingen [P, jf. C]. Krever lønnsgodkjenning |
| AN-06 | Feriepenger: grunnlag i fjor og i år, sats, når de utbetales. Prognose for juni | Må (saldo) / Bør (prognose) | Typisk norsk spørsmål (G #6) |
| AN-07 | Fravær og ferie i appen | Må | Erstattet av modulbehovene AN-21–AN-27 nedenfor |
| AN-08 | Utleggsstatus: godkjent → utbetales med lønn *dato* eller utbetalt i dag, både fra egen modul og fra Utleggsappen | Må | G B1, vei A/B. Status via B10. Se AN-32–AN-36 |
| AN-09 | **Kontonummer-skjold**: BankID-steg, karantene, varsel på gammel kanal, kontroll før lønnskjøring | Må | G #13 og F 3.3. Se flyt F2 |
| AN-10 | Ingen beløp, fødselsnummer eller kontonummer i push, e-post eller SMS | Må | Ny i runde B (personvern) |
| AN-11 | Årsoversikt over lønn og trekk og historikk | Må | Plikt og frist bør verifiseres [S/U] |
| AN-12 | Språk: bokmål og engelsk må finnes. Polsk, litauisk, ukrainsk m.fl. med ordliste | Må (EN) / Bør (flere) | Juridisk gjelder den norske slippen. Oversettelsen er en hjelp |
| AN-13 | Pensjon: innskudd hittil i år og lenke til leverandøren | Bør | Avhenger av pensjonsintegrasjon (G B6) |
| AN-14 | Se og e-signere trekkavtaler og nedbetalingsplaner | Må (når aktuelt) | aml. § 14-15 (G B1, #27) |
| AN-15 | Én identitet med flere roller: lønn, honorar og verv, utlegg, godkjenninger | Bør | Kap. 11. Ny i runde B |
| AN-16 | Tilgjengelighet etter WCAG 2.1 AA | Må | F |
| AN-17 | «Spør lønnsslippen» (KI-chat over egne data med kildehenvisning) | Kan | Nedgradert i runde B |
| AN-18 | Totalkompensasjonskort | Kan | Krever pensjons- og forsikringsdata |
| AN-19 | Lønnskalender som kalenderabonnement (ICS) | Kan | Billig. Ingen beløp i kalenderen |
| AN-20 | Lønnsforskudd (EWA), Vipps-utbetaling, sparekonto-splitt | Ikke nå | G pkt. 9 |

**Behov til de egne modulene for fravær og ferie, timer og utlegg** (nytt krav fra gründeren). Behovene gjelder også når kunden bruker en ekstern modul. Da kommer status og godkjenninger via B10, og appen dyplenker eller viser innholdet innebygd.

| ID | Modul | Behov | MoSCoW | Merknad, regel og risiko |
|---|---|---|---|---|
| AN-21 | Fravær og ferie | **Søke ferie fra mobil**: velge dager i kalenderen, se saldoen *etter* søknaden, se kolleger som er borte (bare «borte», ikke hvorfor), følge status og trekke søknaden | Må | Arbeidsgiver fastsetter ferien etter drøfting. Arbeidstaker kan kreve 18 virkedager hovedferie i perioden 1.6–30.9 og skal ha beskjed senest to måneder før (ferieloven §§ 5–6) [P/S]. Regelvarsler, ikke sperrer |
| AN-22 | Fravær og ferie | **Feriesaldo**: dager til gode i år, overført fra i fjor, femte ferieuke og 60+-uke, planlagt og avviklet. Vises i dager og timer for deltid og turnus | Må | Lovens 25 virkedager [P]. Overføring krever skriftlig avtale [P/S]. Tariff (5 uker) konfigureres |
| AN-23 | Fravær og ferie | **Egenmelding fra mobil**: registrere egen sykdom på 30 sekunder, se gjenstående kvote, ingen diagnose | Må | Kvoten er konfigurerbar: lovens hovedregel (inntil 3 kalenderdager per tilfelle, 4 tilfeller per 12 måneder, etter 2 måneders ansettelse) eller virksomhetens utvidede ordning [S, jf. B 6.2. Verifiser 2026-regelverket] |
| AN-24 | Fravær og ferie | Sykt barn og omsorgsdager: registrere, se saldo, laste opp dokumentasjon for utvidet rett (aleneomsorg, kronisk syk) | Må | Refusjon fra NAV gjennom kjernen (B, K9-API) [P/S]. Antall dager per regelverk og situasjon [U for 2026] |
| AN-25 | Fravær og ferie | Sykmelding: se at den er mottatt (fra NAV via API), sykmeldingsgrad og periode, og at lønn under sykdom er håndtert. Påminnelse når perioden utløper | Bør | Helseopplysninger: bare tilgangspakken «Fravær – helse» (G B3). Leder ser periode og grad, aldri annet |
| AN-26 | Fravær og ferie | Permisjon (velferd, ulønnet, foreldre): søknad og *estimert* konsekvens for lønn, feriepenger og pensjon | Bør | Merket som estimat. Permisjoner i a-meldingen eies av kjernen |
| AN-27 | Timer | Saldo for avspasering og fleks, og ta ut avspasering som fravær | Bør | Saldoen eies av én kilde per kunde (G B3) |
| AN-28 | Timer | **Timeføring på mobil**: dag eller uke, prosjekt eller aktivitet (dimensjoner), kopiere forrige uke, start/stopp. Fungerer uten nett | Må (timelønnede og prosjektførende) | Arbeidsgiver skal ha oversikt over arbeidstiden (aml. § 10-7) [P/S]. Ingen GPS-sporing (runde B) |
| AN-29 | Timer | **Overtid**: registrere med begrunnelse og hvem som påla den, velge utbetaling eller avspasering, se estimert verdi før innsending | Må | Prisingen gjøres i kjernen. Overtid uten godkjenning utbetales aldri (G B3) |
| AN-30 | Timer | Periodestatus: levert, godkjent, sendt tilbake med kommentar, låst. Varsel før cut-off | Må | Fristen kommer fra lønnens `cutoff_scheduled` |
| AN-31 | Timer | Tillegg beregnet *før* lønn (kveld, natt, helg, helligdag) og vist på timelisten | Bør | Kjernen beregner. Modulen viser |
| AN-32 | Utlegg | **Utlegg med foto av kvittering**: OCR-forslag (beløp, dato, mva, leverandør), kategori og prosjekt. Kø uten nett. Flere kvitteringer i ett krav | Må | Kvitteringen lagres som bilag (bokføringsregler). Hash for duplikatsjekk (G B1) |
| AN-33 | Utlegg | **Reiseregning**: km med rute og kart, passasjertillegg, diett med måltidstrekk, overnatting. Satsene beregnes automatisk med deling i trekkfri og trekkpliktig del | Må | Satser fra Skatteetatens satsside, i en felles regeltjeneste (2.6, pkt. 5). 2026-satsene er delvis sekundærkilder [S, jf. C] |
| AN-34 | Utlegg | Status: attestert → utbetales med lønn *dato*, eller straks for rene refusjoner (vei B) | Må | G B1. Trekkpliktige deler går alltid via lønn |
| AN-35 | Utlegg | Duplikatvarsel (samme kvittering to ganger, også på tvers av moduler) og varsel om policyavvik før innsending | Bør | Hash over kilder. Varselet forklarer, det anklager ikke |
| AN-36 | Alle | Samme inngang i appen om kunden bruker egne moduler eller eksterne (Utleggsappen, tidssystem): én fane, dyplenke eller innebygd visning | Bør | B10. Den ansatte merker ikke at kunden bytter modul |

**Kult i 2026**
- **«Hvorfor endret lønna seg?»** To til fire linjer i klartekst øverst på slippen, med lenke til hver lønnsart. Teksten genereres fra regelgrafen og er derfor forklarbar og testbar.
- **Utlegg utbetalt samme dag** (UA vei B), med sporing: *godkjent – sendt banken – på konto*.
- **Feriepengekort i mai:** «Du får ca. X 18. juni. Junilønna blir lavere fordi …»
- **Ferie på tre trykk:** Velg uke, se «saldo etter søknad: 7 dager», send. Lederen får den i innboksen med teamkalenderen ved siden av.
- **Kvittering → penger:** Ta bilde av kvitteringen. Beløp og dato fylles ut. Etter attestasjon står det «utbetales i dag».

**Suksessmål**
- Henvendelser til lønn om lønnsslippen ned ≥ 50 % per 100 ansatte per måned innen 6 måneder.
- Feriesøknader avgjort på median < 2 virkedager. ≥ 90 % av egenmeldingene registrert digitalt samme dag.
- ≥ 95 % av timelistene levert før cut-off. Median tid fra kvittering til utbetaling < 5 virkedager. < 3 % av utleggene sendt tilbake for manglende opplysninger.
- ≥ 85 % åpner slippen digitalt (app eller Digipost).
- 0 vellykkede omdirigeringer av lønn. Alle kontoendringer i kontrollrapporten.
- ≥ 4,3 av 5 på «jeg forstår lønnsslippen min» (kort måling i appen to ganger i året).

---

## 4. Persona 2 – Linjeleder

**Kontekst.** Ole leder 8 ansatte og, i arrangementshøsten, 25 ekstrahjelpere. En lokallagsleder i samme organisasjon er *ikke ansatt*, men attesterer reiseregninger for frivillige. Begge godkjenner på mobil mellom møter.

**Jobber som skal gjøres**
- Godkjenne timer, fravær, utlegg og tillegg før fristen, med nok kontekst til å se feil.
- Se hva teamet koster mot budsjett.
- Delegere når han er borte.
- Melde endringer (tillegg, stillingsprosent) uten e-post.

**Smerter**
- Tre apper og tre innbokser. Påminnelser kommer etter fristen [S, jf. D 8].
- Godkjenning uten kontekst («godkjenn 34 linjer»).
- Ser enten for mye (individuell lønn, sykdomsårsak) eller for lite (ingen kostnad).
- Stedfortreder løses ved å dele passord.

**Behov**

| ID | Behov | MoSCoW | Merknad, risiko og avhengighet |
|---|---|---|---|
| LE-01 | **Én godkjenningsinnboks** for ferie, fravær, timer, overtid, utlegg, reise, tillegg og vervkrav, styrt av lederkjeden. Den samler oppgaver fra **egne moduler og eksterne systemer** (Utleggsappen, tidssystem) | Må | G #12. Bygges på B10 (2.6), ikke på egne modulers tabeller. Eksterne uten B10 vises med dyplenke |
| LE-02 | Godkjenning på mobil med kontekst: hva, hvorfor, beløp eller estimat og avvik mot normalen | Må | |
| LE-03 | «Godkjenn alle» bare for linjer uten avvik. Avvik må åpnes én og én | Må | Ny i runde B, mot å godkjenne i blinde |
| LE-04 | Kan ikke godkjenne egne krav, nærståendes krav eller krav der lederen selv er attestant. Eskalering til neste nivå | Må | Arbeidsdeling (D 3) |
| LE-05 | Tidsavgrenset stedfortreder, med logg | Må | |
| LE-06 | Innsyn etter rolle. Standard er aggregert kostnad. Individuell lønn bare for ledere med personalansvar etter tenantpolicy. **Aldri** fødselsnummer, kontonummer, trekkpålegg, fagforeningstrekk eller fraværsårsak | Må | F 3.3 ABAC. Skjerpet i runde B |
| LE-07 | Teamkostnad (lønn, feriepenger, AGA, OTP) mot budsjett per måned | Bør | Minste gruppestørrelse ≥ 5, ellers vises bare totalsum (LE-11) |
| LE-08 | Varsel om ugodkjente timer før cut-off og overtid nær AML-grensene | Bør | Grensene kommer fra tid-modulen |
| LE-09 | Endringsønske (tillegg, stillingsprosent) som skjema med virkningsdato → HR eller lønn | Bør | |
| LE-10 | Attestant som ikke er ansatt (lokallagsleder) får en smal rolle: bare krav i egen enhet, uten lønnsinnsyn | Bør | Ny i runde B. Vanlig i organisasjoner |
| LE-11 | Minste gruppestørrelse (k ≥ 5) på aggregerte tall | Bør | Ny i runde B. Hindrer at enkeltlønninger kan utledes |
| LE-12 | «Hva koster en ansettelse?»-kalkulator | Kan | G #30 |
| LE-13 | Godkjenning i Teams eller Slack | Kan | Bare med passkey-steg. Ellers ny vei inn for angrep |
| LE-14 | **Ferie**: teamkalender ved hver søknad (hvem er borte, minimumsbemanning), hovedferieønsker samlet i én visning, godkjenne eller foreslå annen periode | Må | Ferieloven: drøfting og varsel to måneder før [P/S]. Regler gir varsler, ikke sperrer |
| LE-15 | **Fravær**: se *at* noen er borte og hvor lenge (ferie, syk, permisjon på grovt nivå), aldri diagnose. Ved sykmelding: periode og grad for å planlegge arbeidet. Påminnelse om frister for sykefraværsoppfølging | Må (fravær) / Bør (oppfølging) | Helseopplysninger bare med pakken «Fravær – helse». Oppfølgingsfristene etter aml. § 4-6 [S]. Detaljert oppfølging hører til HR |
| LE-16 | **Timer og overtid**: godkjenne per uke eller periode, avvik markert (manglende dager, overtid, timer på avsluttet prosjekt), og varsel mot AML-grensene (hovedregel 10 t per 7 dager, 25 t per 4 uker, 200 t per 52 uker) | Må | aml. § 10-6 [P/S]. Grensene kan endres ved avtale. Konfigureres per kunde |
| LE-17 | **Utlegg og reise**: attestere med kvitteringsbilde, policyavvik markert (over sats, mangler formål eller deltakere, alkohol), sende tilbake med kommentar | Må | Attestasjon i egen modul eller i Utleggsappen. Samme innboks |
| LE-18 | Påminnelse før cut-off til leder *og* ansatt, med «hva mangler» per person | Må | Fra lønnens `cutoff_scheduled` |
| LE-19 | Stedfortreder og eskalering gjelder alle moduler samtidig, også eksterne som støtter B10 | Må | LE-05 utvidet |

**Kult i 2026:** Innboks med konsekvens: «Godkjenner du disse 12 timene med overtid, koster det ca. 7 900 kr inkl. AGA. Per har 9 timer igjen før AML-grensen denne uken.» Ved ferie: «Hvis du godkjenner, er 2 av 6 i teamet borte uke 29.»

**Suksessmål**
- ≥ 95 % av linjene godkjent før cut-off.
- Mediantid fra innsending til godkjenning < 24 timer.
- 0 tilfeller i revisjonsloggen der en leder har sett data utenfor rollen sin.
- Ledere bruker < 10 minutter i måneden på godkjenninger, alle moduler samlet.
- Innboksen fungerer uendret etter at kunden bytter modul (måles i bytte-testen før lansering, se 2.6).

---

## 5. Persona 3 – Tillitsvalgt, styremedlem eller frivillig

**Kontekst.** Tre typiske personer i samme organisasjon:
- **Siri (58)** er sykepleier i en kommune og fylkesleder i organisasjonen. Hun får årlig vervgodtgjørelse, møtegodtgjørelse og tapt arbeidsfortjeneste for dager med permisjon uten lønn.
- **Jon (67)** er pensjonist og styremedlem i sentralstyret. Han får styrehonorar to ganger i året.
- **Amir (22)** er student og frivillig. Han får dekket togbilletter og kilometer når han kjører utstyr.

Alle er registrert i OrgLab. Ingen er ansatt i HR-forstand.

**Jobber som skal gjøres**
- Få utbetalt riktig beløp, til riktig tid, med riktig trekk, uten å fylle ut et PDF-skjema med fødselsnummer.
- Dokumentere tapt inntekt enkelt.
- Se hva som er utbetalt og hva som er rapportert til Skatteetaten.
- Ikke få restskatt eller 50 % trekk.

**Smerter**
- Honorarskjema på e-post med fødselsnummer og kontonummer i klartekst. Ingen vet hvor det lagres.
- 50 % trekk fordi organisasjonen ikke har hentet skattekortet.
- Uklart om godtgjørelsen er skattefri («er ikke under 10 000 skattefritt?»).
- Tapt arbeidsfortjeneste krever bekreftelse fra arbeidsgiveren, og satsen varierer fra lokallag til lokallag.
- Venter i flere måneder fordi organisasjonen samler honorarer til én kjøring i desember.

**Behov**

| ID | Behov | MoSCoW | Merknad, risiko og avhengighet |
|---|---|---|---|
| TV-01 | **Riktig mottakerklasse fra start**: verv med godtgjørelse → K2 (frilanser-type, bare i utbetalingsmåneder). Bare utgifter → K3 (ingen arbeidsforhold). Ingen utbetaling → ikke i lønn | Må | [P]. Grunnmuren |
| TV-02 | **BankID-onboarding akkurat når det trengs**: personen inviteres først når en utbetaling er godkjent eller nært forestående. Identitet, fødselsnummer eller D-nummer, kontonummer og Digipost i én flyt. Navnet fra BankID må stemme med OrgLab | Må | Erstatter skjema på e-post. Engangslenke. Avvik i navn gir manuell kontroll |
| TV-03 | Skattekort hentes automatisk før utbetaling. Mangler det, får mottakeren beskjed *før* utbetalingen («du blir trukket 50 % hvis …»). Frikort håndteres | Må | Prosenttrekk på honorar. Halv skatt i desember gjelder ikke [P, jf. C] |
| TV-04 | Godtgjørelse etter vedtatt honorarordning: sats per verv og møte, årlig styrehonorar, alltid med vedtaksreferanse | Må | B8 `policy.adopted`. Uten referanse avvises linjen (`NO_POLICY_REFERENCE`) |
| TV-05 | Møtegodtgjørelse basert på oppmøte attestert av møteleder | Bør | Selvrapportert oppmøte gir ingen utbetaling (runde B) |
| TV-06 | **Krav om tapt arbeidsfortjeneste**: kravtype (lønnstaker eller næringsdrivende), dokumentasjon (arbeidsgivers bekreftelse på trekk eller inntektsgrunnlag), tak per time og dag fra honorarordningen, attestasjon | Må (for organisasjoner som bruker det) | Rapporteringskoden er usikker [U]. Se matrisen |
| TV-07 | Frikjøp i tre modeller: A (faktura fra arbeidsgiver → leverandørreskontro), B (midlertidig arbeidsforhold i organisasjonen), C (vervgodtgjørelse). Avtale, periode og prosent registreres | Bør | Kap. 7. Modell A er ikke lønn |
| TV-08 | Utlegg og reise via Utleggsappen også for ikke-ansatte. Klassifiseres som K3, og trekkpliktig overskudd (for eksempel km over 3,50 kr) håndteres | Må | G B1. Frivillige uten arbeidsforhold [P] |
| TV-09 | **10 000-kronersregelen** for skattefrie organisasjoner: akkumulator per mottaker per *betalende enhet*, valg mellom «regel fra første krone» og «terskel», AGA av alt, trekk fra grensen er passert | Må | [P]. Ingen funksjon som «sprer» utbetalinger for å holde seg under grensen (runde B) |
| TV-10 | **Mottakerportal light**: honorarslipper, årsoversikt, skattekortstatus, kontonummer-skjold og vervoversikt. Ingen HR-funksjoner | Må | Kap. 11, fanen «Honorar og verv» |
| TV-11 | Personvern: OrgLab sender bare verv som gir godtgjørelse. Ingen medlemsdata eller kontingent. Varsel ved særlige kategorier (fagforening, parti, pasientforening) | Må | GDPR art. 9 [P/V]. Vurdering av personvernkonsekvenser (DPIA) |
| TV-12 | Styremedlem bosatt i utlandet: kildeskatt på lønn og skattebostedsland i a-meldingen | Bør | Gjelder også styrehonorar fra 2019 [P] |
| TV-13 | Faste honorarkjøringer (for eksempel to i måneden) i stedet for en kjøring per krav | Bør | Fra 2026 betales forskuddstrekk første virkedag etter hver utbetaling [P, jf. D]. Mange småkjøringer gir mange innbetalinger |
| TV-14 | Mottakeren kan gi avkall på godtgjørelse *før* den er opptjent | Kan | Skattemessig virkning av avkall [U]. Avkall etter opptjening kan være skattepliktig |
| TV-15 | Automatisk behandling av gaver, gavekort og fribilletter til frivillige | Ikke nå | Regelverket er uklart for frivillige [U]. Krever revisorvurdering |

**Kult i 2026**
- **«Registrert på to minutter, aldri fødselsnummer på e-post»:** invitasjon fra organisasjonen, BankID, kontonummer, ferdig. Organisasjonen ser bare «klar for utbetaling».
- **«Jeg var der»:** Når møtelederen har attestert oppmøtet, beregnes godtgjørelsen og vises som «på vei» i appen. Reise fra Utleggsappen havner i samme oversikt.
- **Årsoversikt per organisasjon:** «Dette fikk du fra oss i 2026, og slik er det rapportert.» Den forklarer også om 10 000-regelen gjelder.

**Suksessmål**
- Median tid fra invitasjon til «klar for utbetaling» < 5 minutter. ≥ 90 % fullfører uten hjelp.
- < 1 % av honorarutbetalingene har 50 %-trekk fordi skattekort mangler.
- 0 fødselsnumre eller kontonumre mottatt på e-post (mål ved å fase ut skjemaene).
- < 0,5 % av vervlinjene må rettes i en senere a-melding.
- Vervgodtgjørelse utbetalt ≤ 10 virkedager etter godkjenning.

---

## 6. Persona 4 – Arrangementsansvarlig (Tikket)

**Kontekst.** Mona har ansvar for en todagers festival med 4 000 billetter i Tikket. Bemanningen er 120 frivillige, 40 timelønnede ekstrahjelpere (rigg, bar, garderobe, mange under 25), et vaktselskap som fakturerer, 6 norske artister (2 privatpersoner, 3 ENK, 1 via agentur-AS), 1 svensk band og 3 foredragsholdere.

**Jobber som skal gjøres**
- Bemanne raskt og lovlig.
- Få timene inn i lønn uten Excel.
- Betale artister og foredragsholdere riktig og raskt.
- Vite hva arrangementet faktisk kostet, også mens det pågår.

**Smerter**
- Ekstrahjelp mangler arbeidsavtale, skattekort og kontonummer på festivaldagen.
- Timelister på papir.
- Artister vil ha betalt på kvelden. Ingen vet om honorar til en privatperson skal gjennom lønn eller ikke.
- Det utenlandske bandet gir artistskatt som ingen husker før det er for sent (RF-1091 tre uker før) [P].
- Lønnskostnaden per arrangement blir kjent først etter at regnskapet er lukket.

**Behov**

| ID | Behov | MoSCoW | Merknad, risiko og avhengighet |
|---|---|---|---|
| AR-01 | Vakttype per vakt i Tikket: FRIVILLIG, ARBEIDSTAKER eller INNLEID. Lønn validerer typen | Må | B9. Frivillig-vakter kan ikke ha beløp |
| AR-02 | **Rask ansettelse av ekstrahjelp**: e-signert arbeidsavtale (aml. § 14-6), midlertidig eller tilkalling, BankID, skattekort og konto. Status «klar» tilbake til Tikket | Må | Fast ansettelse krever avtalt stillingsomfang [S]. Tidskravet til arbeidsavtalen bør verifiseres [S/U] |
| AR-03 | Inn- og utsjekk i Tikket → timer per timetype → godkjenning av ansvarlig → lønn. Uten Tikket brukes den egne Timer-modulen, med arrangement-ID som dimensjon | Må | B9 og B3. Lønn priser timene. Ugodkjente timer utbetales aldri. Én eier per domene (2.6): Tikket eier arrangementstimer, Timer-modulen eier ordinær arbeidstid |
| AR-04 | Rapporteres riktig: stillingsprosent 0 og timelønn med antall timer for tilkalling. Aldri 0 % med fastlønn (feil F529) | Må | [P/S] |
| AR-05 | **Klassifiseringsveiviser for utøvere** (2.5): privatperson → K2, ENK → K4 med RF-1301-flagg, AS → K4, utenlandsk → K5 | Må | [P]. Forslag. En person signerer |
| AR-06 | Artistskatt: påminnelse om RF-1091 tre uker før, trekk 15 %, RF-1092 senest sju dager etter trekk, arrangørdekkede kostnader holdes utenfor, avtaleunntak dokumenteres | Bør (Må for organisasjoner med utenlandske artister) | [P]. Ikke a-melding og ikke AGA |
| AR-07 | Arrangement-ID som dimensjon på alle lønns-, honorar- og trekklinjer helt fram til bilaget | Må | G #28 |
| AR-08 | **Kostnad per arrangement**: brutto, feriepenger, AGA, OTP-estimat, honorar og artistskatt mot billettinntekter fra Tikket. Estimat før lønnskjøring, faktisk etter | Bør | Merk tydelig hva som er estimat. Aggregert, ikke per person |
| AR-09 | Rask utbetaling etter arrangementet: ekstra lønnskjøring innen 3–5 virkedager | Bør | Ikke Vipps (ingen offentlig utbetalings-API funnet [S/U]). Straksbetaling via bank der det støttes [U] |
| AR-10 | Massebehandling: 40–80 ekstrahjelpere i én helg | Må | Import og forhåndsvalidering |
| AR-11 | Flagg for unge arbeidstakere (under 18): arbeidstid og frikort er vanlig | Bør | Arbeidstidsregler eies av Tikket eller tid-modulen |
| AR-12 | Gjenbruk: ekstrahjelp fra i fjor kan aktiveres igjen med ny avtale uten ny onboarding (konto og BankID gjenbrukes) | Bør | Kontoen bekreftes på nytt hvis den ikke er brukt på 12 måneder (runde B) |
| AR-13 | Kontantutbetaling eller Vipps fra kassa til frivillige og ekstrahjelp | Ikke nå | Svindel, ikke rapportert og hvitvaskingsrisiko. Systemet skal gjøre det lettere å la være |

**Kult i 2026**
- **Live arrangementsregnskap:** «Festivalen så langt: bemanning 312 000, honorarer 410 000, AGA 101 000, artistskatt 22 500. Billettinntekter 1,94 mill.» Oppdateres når timer godkjennes.
- **Innsjekk er timelisten:** Frivillige og ekstrahjelp skanner seg inn i Tikket. Bare ekstrahjelpens timer går til lønn.
- **Artistskatt-veiviser** som oppretter frister og fyller inn RF-1092-grunnlaget.

**Suksessmål**
- 100 % av ekstrahjelpene har signert avtale, skattekort og konto før første vakt.
- Timer klare for lønn ≤ 48 timer etter at arrangementet er slutt.
- Honorar utbetalt ≤ 5 virkedager etter at fakturaen eller kravet er godkjent.
- 100 % av utenlandske artister har RF-1091 innen fristen.
- Avvik mellom estimert og faktisk lønnskostnad per arrangement < 5 %.

---

## 7. Persona 5 – Generalsekretær i interesseorganisasjon

**Kontekst.** Generalsekretæren leder en landsdekkende interesseorganisasjon med 60 ansatte i sekretariatet, 3 000 tillitsvalgte og 180 lokallag. 40 av lokallagene har eget organisasjonsnummer. Rundt 400 tillitsvalgte får godtgjørelse i løpet av året, og over 1 500 får reiseutlegg. Organisasjonen får offentlige tilskudd (drifts- og prosjekttilskudd) og innsamlede midler. Regnskapet føres av et byrå. Landsmøtet holdes annethvert år med 350 delegater.

**Jobber som skal gjøres**
- Holde lønns- og honorarkostnader innenfor budsjett og vedtak.
- Fordele kostnader riktig på lokallag, prosjekter og tilskudd.
- Dokumentere for revisor, tilskuddsgiver, styret og Innsamlingskontrollen.
- Unngå skandaler: feil honorar, svindel, brudd på personvernet.
- Bruke mindre tid i sekretariatet på administrasjon.

**Smerter**
- Honorarer i regneark i hvert lokallag.
- Uklart hvem som er arbeidsgiver (sentralledd eller lokallag).
- Tilskuddsrapporter som krever fullastet lønnskostnad per prosjekt, med retroaktive omfordelinger.
- Styrehonorarer skal være konfidensielle i det daglige, men stå i noten i årsregnskapet [S, jf. D].
- Landsmøtet gir 350 reiseregninger og 120 krav om tapt arbeidsfortjeneste på én uke.

**Behov**

| ID | Behov | MoSCoW | Merknad, risiko og avhengighet |
|---|---|---|---|
| GS-01 | **Betalende juridisk enhet** per utbetaling: sentralledd eller lokallag med eget organisasjonsnummer | Må | Styrer a-melding, AGA, 10 000-grensen og § 23-2 |
| GS-02 | **Flerenhetsmodus**: sentralleddet kjører lønn og honorar for lokallagene som egne klienter, med klientdelegering og systembruker per enhet i Altinn | Bør (Må for organisasjoner med mange egne lokallag) | Samme mekanisme som for byråer (E). Lokallaget godkjenner |
| GS-03 | Kostnadsfordeling på lokallag, prosjekt og tilskudd med fordelingsnøkler, retroaktiv omfordeling og spor | Må | D 6.3–6.4 |
| GS-04 | **Tilskuddsrapport**: fullastet lønnskost (brutto, feriepenger, AGA, OTP) per prosjekt og finansiør, med timegrunnlag og revisorspor | Må | Timegrunnlaget kommer fra tid-modulen |
| GS-05 | **Honorarpolitikk som regler**: satser per verv og møte, tak for tapt arbeidsfortjeneste, gyldighet, vedtaksreferanse | Må | B8 `policy.adopted` |
| GS-06 | **Arbeidsdeling**: den som oppretter verv eller honorar i OrgLab, kan ikke godkjenne utbetalingen. Fire øyne over en terskel. Rapport over hvem som kan både X og Y | Må | D 3. Ny i runde B: hindrer fiktive verv |
| GS-07 | Konfidensiell gruppe for styrehonorar og ledelse. Eksport til noteopplysninger (ytelser til daglig leder og styret) | Må | D 3.3 |
| GS-08 | Overvåking av AGA-fritak og forenklet a-melding (§ 23-2: 800 000 / 80 000) for små lokallag med eget organisasjonsnummer | Bør | [P]. Varsel før grensen passeres |
| GS-09 | Årsoversikt per mottaker per enhet (10 000-regelen, TV-09) | Må | |
| GS-10 | **Landsmøtemodus**: massekrav (reise, tapt arbeidsfortjeneste, møtegodtgjørelse) for 300–500 delegater, en egen kjøring og avviksliste | Bør | Deltakerliste og oppmøte fra OrgLab |
| GS-11 | Budsjett og prognose for honorarer og lønnskost 12 måneder fram | Bør | G #29 |
| GS-12 | Styrerapport: lønnskost, honorarer mot vedtak, avvik og revisjonslogg | Bør | |
| GS-13 | Byrået kjører, organisasjonen godkjenner på mobil | Må | E. G #19 |
| GS-14 | AGA-sone riktig for honorarmottakere og lokallag i ulike soner | Må | Regelen for frilanser-type er [U] (kap. 13) |
| GS-15 | Simulator for honorarpolitikk («hva koster +10 % på møtegodtgjørelsen?») | Kan | |
| GS-16 | KI-forslag til fordeling på prosjekter | Kan | Bare som forslag. En person godkjenner |

**Kult i 2026**
- **Kostnadskart:** lokallag × prosjekt × tilskudd, med drill-down fra totalbeløpet til bilag og regel. Aggregert (k ≥ 5) for alle unntatt lønnsansvarlig.
- **Tilskuddsrapport med ett klikk**, med revisorspor (hvilke timer, hvilke satser, hvilke omfordelinger).
- **Honorar mot vedtak:** Hver utbetaling viser vedtaket den bygger på. Styret ser avvik, ikke regneark.

**Suksessmål**
- Tilskuddsrapport på under en time (i dag dager).
- 100 % av vervgodtgjørelsene har vedtaksreferanse.
- 0 revisormerknader om lønn og honorar.
- Lønnskostnad per lokallag og prosjekt er tilgjengelig ≤ 3 virkedager etter kjøring.
- Tid i sekretariatet brukt på honorarer ned ≥ 60 %.

---

## 8. Persona 6 – Ny og sluttende ansatt

**Kontekst.**
- **Lina** begynner 1. desember. Hun har fått kontrakt på e-post og spørsmål om kontonummer på SMS.
- **Per** slutter 31. januar. Han har feriedager og avspasering til gode, et utlegg som ikke er behandlet og et lønnsforskudd han skylder.

**Jobber som skal gjøres**
- *Lina:* bli registrert og få riktig første lønn uten å sende fødselsnummer og kontonummer i klartekst.
- *Per:* få et korrekt sluttoppgjør og beholde tilgangen til slipper og årsoversikt.

**Smerter**
- Første lønn med 50 % trekk eller til feil konto.
- Delmåned som ingen forstår.
- Sluttoppgjør med uventede trekk.
- Tilgangen til slipper forsvinner samme dag han slutter [S, jf. D 10].
- Kontonummeret endres rett før siste lønn. Dette er et kjent svindelmønster [V].

**Behov**

| ID | Behov | MoSCoW | Merknad, risiko og avhengighet |
|---|---|---|---|
| OB-01 | Lenke før oppstart med BankID: personalia, kontonummer, Digipost, språk, pårørende | Må | Personer uten BankID: invitasjon og ID-kontroll hos arbeidsgiver. De kan ikke endre konto selv (F) |
| OB-02 | Skattekort hentes automatisk når arbeidsforholdet opprettes, og oppdateres ved endringsvarsel | Må | B (skattekort-API) |
| OB-03 | E-signert arbeidsavtale som følger kravene i aml. § 14-6 | Bør | HR-modulen eier. Lønn trenger stillingsdata |
| OB-04 | **«Klar for første lønn»-sjekkliste**: skattekort, konto, stillingsprosent, yrkeskode, arbeidstid, OTP-innmelding og lønnsart. Grønn eller rød | Må | Stopper feil før kjøring |
| OB-05 | Første lønnsslipp forklart: delmåned, startdato og hvorfor beløpet avviker | Bør | AN-02 |
| OB-06 | OTP-innmelding fra første dag (fra første krone) | Må | [S, jf. B] |
| OB-07 | **Veiviser for sluttoppgjør**: feriepenger, avspasering, utlegg, forskudd og lån. Trekk bare med gyldig hjemmel eller avtale (aml. § 14-15). Ellers betalingsplan | Må | G #26 og #27 |
| OB-08 | Sluttdato og sluttårsak i a-meldingen. Utmelding fra OTP | Må | [P] |
| OB-09 | Tilgang til slipper og årsoversikt etter fratreden med BankID, og arkiv i Digipost | Må | D 10 |
| OB-10 | Kontoendring de siste 30 dagene før siste lønn gir ekstra kontroll (fire øyne og kontakt via kjent kanal) | Må | Ny i runde B |
| OB-11 | Tilgangene trekkes automatisk tilbake ved sluttdato: godkjennerrolle, leder og attestant | Må | Ny i runde B |
| OB-12 | Feriepenger ved fratreden: utbetaling nå eller i ferieåret, etter reglene | Bør | C |
| OB-13 | Prøveberegning av første lønn før oppstart | Kan | Merket «estimat». Lav prioritet |
| OB-14 | Ny ansatt: feriesaldo første år, med forklaring på ferie uten feriepenger hos oss (feriepengene kom fra forrige arbeidsgiver) og mulighet til å søke ferie fra første dag | Bør | Modulen Fravær og ferie. Feriepengegrunnlaget eies av kjernen |
| OB-15 | Sluttende: saldo for ferie, avspasering og fleks går automatisk inn i sluttoppgjøret. Åpne timelister og utlegg vises som «må leveres før …» | Må | Henger sammen med OB-07. Gjelder også når modulene er eksterne (B3/B10) |

**Kult i 2026**
- **Grønt lys for første lønn:** Lina ser at alt er klart før hun har møtt opp.
- **Ta med deg lønnshistorikken:** Når Per slutter, legges alle slipper og årsoversikten i Digipost og er tilgjengelige med BankID.

**Suksessmål**
- 100 % av nyansatte har skattekort og verifisert konto før første kjøring.
- 0 sluttoppgjør med trekk uten hjemmel.
- ≥ 95 % av tidligere ansatte henter dokumenter uten å kontakte lønn.

---

## 9. Runde B: kritikk og hva jeg endret

### 9.1 Gimmick, eller ikke verdt prisen nå

| Runde A-forslag | Kritikk | Runde B |
|---|---|---|
| «Spør lønnsslippen» som KI-chat (Bør) | Mesteparten av verdien kommer fra en *deterministisk* forklaring (AN-02). Chatten gir risiko for feilsvar og krav til personvern og KI-merking (F) | AN-02 hevet til **Må**. Chatten flyttet til **Kan** og skal bare svare med kildehenvisning |
| Neste lønnsdag i Apple/Google Wallet | Gir lite nytte, og informasjon lekker på låseskjermen | **Strøket** |
| Gamification for frivillige (merker, poeng) | Hører hjemme i OrgLab, ikke i lønn | **Strøket** fra lønn |
| Honorar utbetalt samme kveld via Vipps | Fant ingen offentlig utbetalings-API [S/U]. Trekk og AGA må beregnes. Øker svindelrisikoen | **Ekstra kjøring på 3–5 dager** (AR-09). Straks bare der banken støtter det |
| KI klassifiserer automatisk lønn eller næring | Vurderingen er juridisk og bygger på faktiske forhold [P]. KI kan ikke ta ansvaret | **Veiviser med forslag og signatur** (2.5, AR-05) |
| Swipe for å godkjenne alt | Godkjenning i blinde | **«Godkjenn alle» bare uten avvik** (LE-03) |
| Lønnsforskudd (EWA) for ekstrahjelp | Liten verdi, regulatorisk usikkert (G) | **Ikke nå** |

### 9.2 Øker risikoen for svindel eller feil

| Runde A-forslag | Risiko | Runde B |
|---|---|---|
| Selvbetjent honorarskjema via åpen lenke på nettsiden | Hvem som helst kan registrere en mottaker. Fødselsnummer og kontonummer samles inn ukontrollert | **Personlig engangsinvitasjon** knyttet til personRef i OrgLab, BankID, og navnet må stemme (TV-02) |
| OrgLab sender alle tillitsvalgte med fødselsnummer til lønn | Dataminimering (GDPR art. 5) og mulige særlige kategorier (art. 9) | **Bare verv med godtgjørelse.** Fødselsnummer innhentes av lønn akkurat når det trengs (TV-11) |
| Verv opprettet i OrgLab utløser utbetaling automatisk | Fiktive verv blir en vei til å tappe organisasjonen | **Krever vedtaksreferanse og arbeidsdeling** mellom OrgLab-administrator og godkjenner (GS-06, TV-04) |
| Selvrapportert møteoppmøte | Godtgjørelse for møter personen ikke var på | **Oppmøte attestert av møteleder** (TV-05) |
| Tapt arbeidsfortjeneste etter egenerklæring | Oppblåste krav | **Dokumentasjon og tak** fra honorarordningen (TV-06) |
| Kontonummer kan endres fritt i appen | Lønnen omdirigeres | **Skjold**: BankID-steg, karantene, varsel på gammel kanal og fire øyne nær lønnsdag eller fratreden (AN-09, OB-10) |
| Leder ser individuell lønn for teamet | Personvern og tillit | **Aggregert er standard.** Individuelt bare med personalansvar. k ≥ 5 (LE-06, LE-11) |
| Gjenbruk av ekstrahjelp fra i fjor med samme konto | Kontoen kan være overtatt | **Bekreft kontoen på nytt** etter 12 måneder uten bruk (AR-12) |
| Push med beløp | Lekker på låseskjermen | **Aldri beløp eller personnummer i varsler** (AN-10) |
| Tilganger består etter fratreden | Tidligere leder kan fortsatt godkjenne | **Automatisk tilbaketrekking** (OB-11) |

### 9.3 Juridisk feil eller uklart i runde A

| Runde A-påstand | Hva er riktig | Kilde | Runde B |
|---|---|---|---|
| «Tillitsvalgte med honorar får feriepenger» | Styrehonorar og vervgodtgjørelse er ikke feriepengegrunnlag. Ferieloven gjelder arbeidstakere | [P/S] C #16–17 | Rettet i matrisen |
| «Honorar under 10 000 kr er alltid skattefritt» | Gjelder bare lønn fra **skattefrie organisasjoner** (§ 2-32), trolig per organisasjon. For et festival-AS gjelder vanlige grenser (2 000 kr) | [P] / [S] | TV-09 er begrenset til § 2-32-enheter |
| «Under 10 000 kr gir ingen AGA» | AGA beregnes av all lønn, med mindre § 23-2 gir fritak | [P] | Rettet |
| «Frivillige må ha arbeidsforhold for å få kjøregodtgjørelse» | Personer med bare utgiftsgodtgjørelse skal ikke ha arbeidsforhold | [P] | K3 |
| «Utenlandske artister kjøres i a-meldingen med kildeskatt (PAYE)» | Artistskatt 15 %, RF-1091/1092, ikke a-melding og ikke AGA | [P] | K5 og AR-06 |
| «Foredragsholdere med ENK kan betales via lønn for enkelhets skyld» | Hvis personen reelt driver næring, er det leverandørkjøp. Kjøperen kan ha plikt til å rapportere ENK-betalinger (RF-1301) | [P] | K4 og AR-05 |
| «Ekstrahjelp kan være fast ansatt på tilkalling uten avtalt stillingsomfang» | Fast ansettelse krever avtalt stillingsomfang. Tilkalling skal rapporteres som midlertidig, stillingsprosent 0 | [S] / [P/S] | AR-02, AR-04 |
| «For mye utbetalt honorar motregnes i neste utbetaling» | Krever avtale. For arbeidstakere gjelder aml. § 14-15. For ikke-ansatte gjelder alminnelige regler for motregning og avtale [V/U] | [P] for arbeidstakere | Samme flyt for avtale og betalingsplan for alle |
| «Frikjøp er alltid lønn hos organisasjonen» | Tre modeller. I modell A er det leverandørfaktura fra arbeidsgiveren | [V/S] | TV-07, matrisen |
| «Tapt arbeidsfortjeneste er skattefri erstatning» | Erstatning for tapt *inntekt* er normalt skattepliktig og AGA-pliktig som godtgjørelse [U/V]. Rapporteringskoden er ikke verifisert | [U] | Merket usikker. Avklares med Skatteetaten |

### 9.4 Kritikk av det nye kravet om egne moduler for ferie/fravær, timer og utlegg

| Risiko eller forslag | Kritikk | Hvordan det er håndtert |
|---|---|---|
| Egne moduler bruker kjernens interne data «fordi det går fortere» | Da kan de ikke byttes ut, og eksterne partnere taper på ulike vilkår (G pkt. 5) | Bare offentlige kontrakter, kontrakttester i CI og bytte-test før lansering (2.6) |
| Innboks og app bygges direkte på egne moduler | Kunder med Utleggsappen eller et eget tidssystem får en dårligere app. Det undergraver «like vilkår» | Kontrakten B10 for godkjenningsoppgaver og status. Dyplenke som minimum (LE-01, AN-36) |
| To kilder for samme domene (egen utleggsmodul og Utleggsappen) | Dobbel utbetaling | Én eier per domene, `SOURCE_NOT_OWNER`, duplikatsjekk med kvitteringshash |
| GPS eller geofence ved timeføring | Personvern og kontroll av ansatte. Krever saklig grunn og drøfting. Liten nytte for målgruppen | **Ikke nå.** Innsjekk ved arrangement skjer i Tikket med skanning, ikke med sporing |
| Automatisk godkjenning av ferie og utlegg under en terskel | Ferie krever drøfting og planlegging. Små utlegg uten attest er en kjent lekkasje | Ingen automatisk godkjenning av ferie. Utlegg: bare med kundens skriftlige policy, stikkprøver og logg (Kan) |
| Egenmeldingsregler hardkodet i modulen | Reglene kan endres, og mange virksomheter har utvidet ordning. 2026-reglene er ikke verifisert | Konfigurerbar kvote i felles regeltjeneste [S/U] |
| OCR fremstilt som «KI som fører utlegget for deg» | Forventet i 2026 og ikke et «wow». Feil i OCR gir feil beløp | OCR fyller bare inn et forslag. Den ansatte bekrefter. Attestanten ser bildet |
| Turnus og vaktplan bygget inn i Timer | Stort og eget fagfelt (helse, omsorg). Gjør modulen tung | **Utenfor nå.** Timer tar imot fra vaktsystem via B3 |
| Sykmeldingsdetaljer i lederens innboks | Helseopplysninger (GDPR art. 9) | Leder ser bare periode og grad (LE-15) |

### 9.5 Hva jeg la til i runde B
- Den sjuende mottakerklassen (K6 frikjøp, modell A) og betalende enhet (GS-01). De manglet helt i runde A.
- Attestant som ikke er ansatt (LE-10). I organisasjoner er det ofte lokallagsledere som attesterer.
- Faste honorarkjøringer (TV-13), fordi forskuddstrekket fra 2026 skal betales etter hver utbetaling.
- Landsmøtemodus (GS-10), som er den største toppbelastningen i organisasjonslivet.

---

## 10. Topp 15 behov, rangert [V]

Rangert etter verdi × risiko hvis det mangler × hvor mye det skiller produktet fra andre. Behov som henger sammen, er slått sammen.

| # | Behov (ID) | Hvorfor så høyt | Persona | Avhengighet |
|---|---|---|---|---|
*Revidert etter gründerens krav om egne moduler for ferie/fravær, timer og utlegg. Modulbehovene og innboksen er tatt inn. Noen behov er slått sammen for å få plass.*

| # | Behov (ID) | Hvorfor så høyt | Persona | Avhengighet |
|---|---|---|---|---|
| 1 | **Mottakerklasse og betalende enhet** i datamodellen (TV-01, GS-01, kap. 2) | Alt annet blir feil uten dette: a-melding, AGA, feriepenger, 10 000-regelen og lokallag | 3, 4, 5 | Kjerne |
| 2 | **Kontonummer-skjold** (AN-09, OB-10) | Den vanligste lønnssvindelen. Billig å bygge | 1, 3, 6 | BankID |
| 3 | **Én godkjenningsinnboks på mobil** for egne og eksterne moduler, med kontekst, innsyn etter rolle og stedfortreder (LE-01–06, LE-14–19) | Gjør at fristene nås. Personvern. Beviser at modulene kan byttes ut | 2 | **B10**, B1, B3, B8, B9 |
| 4 | **Fravær og ferie på mobil**: søknad, saldo, egenmelding, sykt barn og sykmeldingsstatus (AN-21–25) | Det ansatte bruker oftest etter lønnsslippen. Gir data til lønn, AGP og NAV-refusjon | 1, 2, 6 | Fravær- og feriemodul, NAV-API |
| 5 | **Timer og overtid** med periodelås, AML-varsel og status før cut-off (AN-28–30, LE-16). Omfatter innsjekk for ekstrahjelp (AR-02–04) | Feil og sene timer er den største feilkilden i lønnskjøringen | 1, 2, 4 | Timer-modul, B3, B9 |
| 6 | **Utlegg med foto og automatisk satsberegning** (trekkfri og trekkpliktig del), med status til utbetaling (AN-32–34, LE-17) | Synlig «wow» sammen med straksutbetaling. Riktig klassifisering i a-meldingen | 1, 2, 3 | Utleggsmodul eller Utleggsappen, B1 |
| 7 | **BankID-onboarding akkurat når det trengs**, for ansatte og ikke-ansatte, og **mottakerportal light** (OB-01, TV-02, TV-10) | Fjerner fødselsnummer på e-post. 3 000 tillitsvalgte får slipp og konto uten HR-funksjoner | 3, 4, 6 | eID, B8, B9 |
| 8 | **Automatisk skattekort for alle mottakere** med forvarsel (OB-02, TV-03) | 50 %-trekk er den vanligste klagen fra honorarmottakere og nyansatte | 1, 3, 6 | Skattekort-API |
| 9 | **Forklart lønnsslipp** (deterministisk) (AN-02, OB-05) | Fjerner det vanligste supportspørsmålet | 1, 6 | Beregningsgraf |
| 10 | **Klassifiseringsveiviser** for lønn, næring og artistskatt (AR-05, 2.5) | Feil spor gir feil i a-meldingen, mangler i RF-1301 og glemt artistskatt | 4, 5 | B9 |
| 11 | **Arbeidsdeling og vedtaksreferanse** for honorarer (GS-06, TV-04, GS-05) | Hindrer fiktive verv. Gir styret kontroll | 5, 3 | B8 |
| 12 | **10 000-kronersregelen og § 23-2-overvåking** (TV-09, GS-08, GS-09) | Gjelder alle skattefrie organisasjoner. Feil gir både for mye og for lite rapportert | 3, 5 | – |
| 13 | **Kostnadsfordeling og tilskuddsrapport** (GS-03, GS-04, AR-07) | Organisasjoner lever av tilskudd. Revisor krever spor. Timer-modulen gir timegrunnlaget | 5, 4 | Timer, regnskap |
| 14 | **Sluttoppgjør etter aml. § 14-15**, med saldoer fra modulene (OB-07, OB-15, AN-14) | Juridisk risiko. Synlig for den som slutter | 6, 1 | B3/B10 |
| 15 | **Krav om tapt arbeidsfortjeneste og frikjøp i tre modeller** (TV-06, TV-07) | Særnorsk for organisasjonslivet. Mangler i standardsystemene [V] | 3, 5 | B8. Rapporteringskoden er usikker |

*Rett under streken:* flerenhetsmodus for lokallag (GS-02), kostnad per arrangement live (AR-08), landsmøtemodus (GS-10), artistskatt-veiviser (AR-06), feriepengeprognose (AN-06), straksutbetaling av utlegg (AN-08 vei B).

---

## 11. Skisse av ansattportal og app

### 11.1 Prinsipper [V]
- **Én app med faner som vises etter relasjon og etter hvilke moduler kunden har**: Hjem, Lønn (K1), **Fravær og ferie**, **Timer**, **Utlegg** (egen modul *eller* Utleggsappen), Honorar og verv (K2), Godkjenn (ledere og attestanter), Meg (alle). Bunnmenyen har maks fem faner. Resten ligger under «Mer», etter hvor ofte de brukes.
- **Fanene for fravær, timer og utlegg er like uansett modul.** Med egne moduler er visningen innebygd. Med eksterne moduler kommer status via B10, og handlingene skjer innebygd (hvis modulen tilbyr en innebygd UI-flate, G 1.8) eller via dyplenke.
- **Innlogging:** BankID første gang og ved kritiske endringer. Passkey til daglig. Personer uten BankID får begrenset funksjon (F).
- **Ingen sensitive data i varsler.** WCAG 2.1 AA. Språkvalg øverst.
- **Hvert tall kan forklares:** Trykk på et beløp for å se regelen, satsen og kilden (glassboks, G #3).

### 11.2 Skjermer

```
┌─ HJEM ──────────────────────────┐   ┌─ LØNNSSLIPP (okt) ───────────────┐
│ Neste lønn: 20. nov (foreløpig) │   │ Netto  31 412   (+1 240 fra sept)│
│ ● 3 ting trenger deg            │   │ Hvorfor endret den seg?          │
│   – Timer uke 45: fredag mangler│   │  • Overtid 6 t (+2 180)          │
│   – Godkjenn 3 timelister       │   │  • Ny trekkprosent fra 1.10 (−940)│
│   – Bekreft nytt kontonummer    │   │                                  │
│ Ferie: 9 dager igjen · [Søk]    │   │                                  │
│ [Egenmelding] [📷 Kvittering]   │   │                                  │
│ Utlegg: 1 249 kr på vei (i dag) │   │ [Se alle linjer] [PDF] [EN/PL/UK]│
│ Feriepenger juni: ca. 48 000 ›  │   │ Hvert beløp → regel og sats ›    │
└─────────────────────────────────┘   └──────────────────────────────────┘
┌─ SKATT ─────────────────────────┐   ┌─ HONORAR OG VERV ────────────────┐
│ Skattekort 2026: tabell 7xxx    │   │ Verv: Fylkesleder (2025–2027)    │
│ Hentet 3.1.2026 fra Skatteetaten│   │ Utbetalt i 2026: 18 400 kr       │
│ Prosent på honorar/overtid: 38 %│   │  • Vervgodtgjørelse  12 000      │
│ Hvorfor trekk i juni/desember?› │   │  • Møter (4)          2 400      │
│ [Be om ekstra trekk]            │   │  • Tapt arbeidsfortj. 4 000      │
│ Endre skattekort → skatteetaten │   │ [Send krav om tapt arbeidsfortj.]│
└─────────────────────────────────┘   │ Rapportert til Skatteetaten ✓    │
                                      └──────────────────────────────────┘
┌─ FRAVÆR OG FERIE ───────────────┐   ┌─ SØK FERIE ──────────────────────┐
│ Ferie 2026: 9 av 25 dager igjen │   │ [kalender] 13.–24. juli          │
│  + 3 overført fra 2025          │   │ 10 virkedager                    │
│ Egenmelding: 2 av 4 tilfeller   │   │ Saldo etter søknad: 2 dager      │
│  brukt siste 12 mnd             │   │ Borte i teamet da: Ola, Siv      │
│ Sykt barn: 6 av 10 dager igjen  │   │ Kommentar til leder (valgfri)    │
│ [Søk ferie] [Egenmelding]       │   │ [Send til Anne Leder]            │
│ [Sykt barn] [Permisjon]         │   │ Status: ● sendt  ○ godkjent      │
│ Sykmelding: mottatt 3.11, 50 %  │   └──────────────────────────────────┘
└─────────────────────────────────┘
┌─ TIMER (uke 45) ────────────────┐   ┌─ UTLEGG ─────────────────────────┐
│ Ma 7,5  Ti 7,5  On 9,0  To 7,5  │   │ [📷 Ny kvittering] [Ny reise]    │
│ Fr –   ← mangler                │   │ Kvittering 412,00 kr · 3.11      │
│ Prosjekt P-4411: 18,5 t         │   │  Leverandør: Flytoget (OCR) ✎    │
│ Overtid on 1,5 t (50 %)         │   │  Prosjekt: P-4411  Formål: ✎     │
│  pålagt av: Anne · utbetales    │   │ Reise Oslo–Hamar t/r 248 km      │
│  ≈ 620 kr før skatt             │   │  trekkfritt 868 · trekkpl. 446   │
│ Frist for levering: to 9.11     │   │ Status: attestert → utbetales i  │
│ [Kopier forrige uke] [Lever]    │   │  dag (refusjon) / 20.11 (rest)   │
└─────────────────────────────────┘   └──────────────────────────────────┘
┌─ GODKJENN (leder/attestant) ────┐   ┌─ MEG ────────────────────────────┐
│ Frist om 2 dager (cut-off 10.11)│   │ Kontonummer ••••.••.•4471 [Endre]│
│ Ferie (2) · Fravær (1) · Timer  │   │ Digipost: på   Språk: Bokmål     │
│  (6) · Utlegg (4) · Verv (1)    │   │ Dokumenter: arbeidsavtale, års-  │
│ ▸ Uten avvik (11)  [Godkjenn]   │   │  oversikt 2025, trekkavtaler     │
│ ▸ Med avvik (3) – åpne én og én │   │ Stedfortreder: Anne til 15.11    │
│   Overtid Per 9 t → ca. 7 900 kr│   │ Sikkerhet: passkey, siste innl.  │
│   Ferie Siv uke 29: 3 av 6 borte│   └──────────────────────────────────┘
│   Utlegg Ola: over diettsats    │
│ ▸ I Utleggsappen (2) → åpne     │   ← ekstern modul uten innebygd UI
│ Teamkost okt: 412 000 / budsj.  │
│ [Teamkalender] [Stedfortreder]  │
└─────────────────────────────────┘
```

*Beløp og saldoer i skissene er illustrasjoner.*

### 11.3 Hovedflyter

| Flyt | Steg | Kontroller |
|---|---|---|
| **F1 Første innlogging (ansatt)** | Invitasjon → BankID → bekreft navn og fødselsdato → kontonummer → Digipost og varsler → passkey | Engangslenke med utløpstid. Kontonummeret får status «ny» og vises i kontrollrapporten |
| **F2 Endre kontonummer** | Meg → Endre → BankID-steg → nytt nummer to ganger → oppsummering → **karantene (f.eks. 72 t)** → varsel på *gammel* e-post eller telefon og til lønnsansvarlig → gjelder fra neste kjøring | ≤ 5 virkedager før lønn eller ≤ 30 dager før fratreden gir fire øyne. Navnesjekk mot banken der den finnes (Verification of Payee i EØS er omtalt fra 2027 [S/U]) |
| **F3 Forstå lønnsslippen** | Varsel «lønnsslipp klar» (uten beløp) → slipp → «Hvorfor endret den seg?» → trykk på linje → regel, sats og kilde | Forklaringen er generert fra regelmotoren og testet |
| **F4 Onboarding av honorarmottaker (ikke-ansatt)** | Utbetaling godkjent i OrgLab eller Tikket → lønn sender **personlig invitasjon** → BankID → navnet sjekkes mot OrgLab → kontonummer → skattekort hentes → status «klar» tilbake til OrgLab eller Tikket | Personvernerklæring med formål. Ingen fødselsnummer i OrgLab. Avvik i navn går til manuell kontroll |
| **F5 Krav om tapt arbeidsfortjeneste** | Honorar og verv → Nytt krav → velg møte eller oppdrag → timer → kravtype → last opp dokumentasjon → beregnet beløp med tak → send → attestant → lønn | Taket fra honorarordningen. Dokumentasjon er påkrevd. Attestanten kan ikke være søkeren |
| **F6 Godkjenning (leder eller attestant)** | Innboks (alle moduler via B10) → linjer uten avvik (masse) → linjer med avvik (én og én med konsekvens: kostnad, AML-grense, bemanning) → godkjenn, avvis eller send tilbake med årsak → beslutningen går til modulen som eier oppgaven | Kan ikke godkjenne egne krav eller nærståendes. Passkey-steg ved store beløp. Eksterne oppgaver uten B10-handlinger åpnes med dyplenke |
| **F9 Søk ferie** | Fravær og ferie → Søk ferie → velg datoer → se saldo etter søknad og teamoverlapp → valgfri kommentar → send → leder får oppgave (B10) → godkjent eller annen periode foreslått → kalender og saldo oppdateres → kjernen får `absence.approved` | Varsel ved brudd på ferielovens regler eller tariff, men ingen sperre. Trekk i lønn for ferie og feriepenger beregnes i kjernen |
| **F10 Egenmelding** | Hjem eller Fravær → Egenmelding → «syk fra i dag» eller dager tilbake i tid → kvote vises → send → leder får *melding* (ikke godkjenning) → kjernen teller arbeidsgiverperioden | Ingen diagnose. Kvoten fra regeltjenesten. Når den er brukt opp, vises «Du trenger sykmelding fra lege» |
| **F11 Timeføring og overtid** | Timer → uke → registrer eller kopier → marker overtid med begrunnelse, hvem som påla den og valg mellom utbetaling og avspasering → lever → leder godkjenner → periodelås ved cut-off → kjernen priser | Avvik (manglende dager, AML-grense) vises før levering. Etter lås kan bare korrigeringslinjer sendes (G 1.11) |
| **F12 Utlegg med kvittering** | Utlegg → kamera → OCR-forslag → bekreft beløp, dato, formål og prosjekt → (reise: rute og diett) → send → attestant (B10) → kjernen klassifiserer → refusjon straks eller med lønn → status «på konto» | Kvitteringshash mot duplikater på tvers av kilder. Trekkpliktige deler går alltid via lønn |
| **F7 Ekstrahjelp** | Tikket-vakt (ARBEIDSTAKER) → invitasjon → BankID, kontonummer, arbeidsavtale (e-signatur) → skattekort → «klar» → innsjekk og utsjekk → godkjenning → lønn → slipp | Uten «klar» kan vakten ikke låses i Tikket |
| **F8 Sluttet** | Etter sluttdato: lesetilgang til slipper og årsoversikt med BankID. Rollene trekkes tilbake. Tilbud om Digipost-arkiv | Ingen kontoendring etter siste utbetaling uten kontakt med lønn |

---

## 12. Regelmatrise: mottakertype × ytelse → a-melding, AGA og trekk

**Forklaring:**
- **AF-type:** arbeidsforholdstype. *Ord.* = ordinært. *Frilans* = «frilanser, oppdragstaker og personer som mottar honorarer». *Ingen* = ikke arbeidsforhold.
- **Trekk:** T = tabell, P = prosent, – = ikke trekkpliktig.
- **FP:** feriepengegrunnlag. **OTP:** pensjonsgrunnlag (Ja/Kan/Nei, jf. C).
- **⚠** = usikkert og må verifiseres.

| # | Mottaker | Ytelse | A-melding (AF-type / beskrivelse) | Trekk | AGA | FP | OTP | Merknad / kilde |
|---|---|---|---|---|---|---|---|---|
| 1 | Ansatt | Fastlønn / timelønn | Ord. / fastlønn, timelønn | T | Ja | Ja | Ja | [P, C] |
| 2 | Ansatt | Honorar for ekstra oppdrag (foredrag, kurs) | Ord. / honorar | P | Ja | Ja | Kan | [P/S, C #15] |
| 3 | Ansatt | Styrehonorar (f.eks. ansattrepresentant) | ⚠ Ord. eller frilans / styrehonorar og godtgjørelse verv | P | Ja | Nei | Nei | Hvilken AF-type som skal brukes når mottakeren også er ansatt, er ⚠ [U] |
| 4 | Styremedlem (ikke ansatt) | Styrehonorar | **Frilans**, bare i utbetalingsmåneder / styrehonorar og godtgjørelse verv | P (alltid trekkpliktig) | Ja | Nei | Nei | [P] |
| 5 | Tillitsvalgt (ikke ansatt) | Fast vervgodtgjørelse eller møtegodtgjørelse | Frilans / styrehonorar og godtgjørelse verv | P | Ja | Nei | Nei | Siden omfatter «tillitsverv», representantskap, utvalg og råd [P] |
| 6 | Tillitsvalgt | **Tapt arbeidsfortjeneste** (lønnstaker) | ⚠ Frilans / trolig «godtgjørelse verv» | P ⚠ | Ja ⚠ | Nei | Nei | Ingen eksplisitt veiledning funnet [U]. AGA-begrepet «godtgjørelse» er vidt og kan omfatte erstatning [S/U] |
| 7 | Tillitsvalgt | Tapt arbeidsfortjeneste (selvstendig næringsdrivende) | ⚠ Som #6, eller næringsinntekt mot faktura | ⚠ | ⚠ | Nei | Nei | [U]. Avklar med Skatteetaten før bygging |
| 8 | Frikjøpt tillitsvalgt, **modell A** | Arbeidsgiver betaler lønn og fakturerer organisasjonen | Ingen hos organisasjonen (arbeidsgiveren rapporterer) | – | – (hos arbeidsgiver) | – | – | Leverandørfaktura [V/S] |
| 9 | Frikjøpt, **modell B** | Permisjon hos egen arbeidsgiver, midlertidig ansatt i organisasjonen | Ord. (midlertidig) | T | Ja | Ja | Ja | Full lønnsbehandling [V] |
| 10 | Frikjøpt, **modell C** | Vervgodtgjørelse direkte | Som #5 | P | Ja | Nei | Nei | [V] |
| 11 | Frivillig / tillitsvalgt | Refusjon av utlegg mot bilag | Ikke rapportert | – | Nei | Nei | Nei | [P/S, C #46] |
| 12 | Frivillig / tillitsvalgt | Trekkfri km-, kost- og nattgodtgjørelse | **Ingen AF** / utgiftsgodtgjørelse hvis > 1 000 kr/år (hovedregel) | – | Nei | Nei | Nei | [P]. ⚠ Om trekkfrie godtgjørelser teller mot 10 000-grensen i § 2-32-enheter, er uklart. Skatteetaten nevner *trekkpliktige* godtgjørelser [P/U] |
| 13 | Frivillig / tillitsvalgt | Trekkpliktig overskudd (km over 3,50 kr, kost over sats) | Ingen AF ⚠ / trekkpliktig godtgjørelse | P | Ja | Nei | Nei | [P, C #39 og #43]. ⚠ Om det utløser frilans-AF, er uklart |
| 14 | Mottaker i **skattefri organisasjon** (§ 2-32) | Lønn eller godtgjørelse ≤ 10 000 kr/år | Ikke opplysningsplikt, *eller* «Skattefri organisasjon» fra første krone. AGA-grunnlaget rapporteres uansett | Nei | **Ja** | Ja hvis K1 | Per plan | [P]. Skattefritt for mottakeren [P], trolig per organisasjon [S] |
| 15 | Samme | > 10 000 kr/år | **Hele** beløpet rapporteres i måneden grensen passeres | Fra grensen, der det er kontantytelser | Ja | Ja hvis K1 | Per plan | [P] |
| 16 | Veldedig/allmennyttig enhet ≤ 800 000 kr samlet og ≤ 80 000 kr per person | All lønn | Forenklet a-melding. ≤ 10 000 kr per person: ingen a-melding | Etter vanlige regler ⚠ | **Fritak** | Ja hvis K1 | Per plan | [P] ftrl. § 23-2. Gjelder ikke lønn knyttet til næringsvirksomhet |
| 17 | Ekstrahjelp / vakt | Timelønn, kvelds- og helgetillegg | Ord. (midlertidig eller tilkalling), **stillingsprosent 0**, timelønn med antall timer | T/P | Ja | **Ja** | Ja ⚠ | [P/S]. OTP-reglene for små stillinger ⚠ [U] |
| 18 | Foredragsholder / artist, norsk privatperson uten næring | Honorar | **Frilans** / honorar | P (50 % uten skattekort) | Ja | Nei | Nei | [P] «Ytelsen skal alltid oppgis som trekkpliktig» |
| 19 | Foredragsholder / artist med ENK (reell næring) | Faktura | Ingen a-melding. **RF-1301/1321 innen 15.2** hvis ENK uten fast forretningssted | – | – | – | – | [P]. Gjelder også skattefrie foreninger. Ingen beløpsgrense |
| 20 | Artist via AS eller agentur | Faktura | Ingen | – | – | – | – | [P] (AS er unntatt fra RF-1301) |
| 21 | Utenlandsk artist eller idrettsutøver (ikke bosatt) | Honorar for opptreden | **Ikke a-melding.** RF-1091 tre uker før, RF-1092 senest sju dager etter trekk | **Artistskatt 15 %** | **Nei** | – | – | [P]. Skatteavtale kan begrense. Arrangørdekkede reise-, kost- og losjiutgifter holdes utenfor |
| 22 | Utenlandsk foredragsholder (ikke artist) | Honorar | ⚠ Frilans med kildeskatt (PAYE) eller ordinær skatt. Krever D-nummer | ⚠ | ⚠ (avhenger av trygdetilhørighet, A1) | Nei | Nei | [U] |
| 23 | Styremedlem bosatt i utlandet | Styrehonorar | Frilans / styrehonorar, skattebostedsland oppgis | Kildeskatt (PAYE) fra 2019 | Ja (unntak ved A1 eller avtale) | Nei | Nei | [P] |
| 24 | Alle i ikke-skattefri enhet (AS, stiftelse med næring) | Lønn eller honorar ≤ 2 000 kr/år | Ikke opplysningsplikt | Nei | ⚠ Avgiftsplikt uavhengig av opplysningsplikt | – | – | [P] for grensen, ⚠ [U] for AGA under grensen |
| 25 | Frivillig | Gave, gavekort, fribillett, mat på arrangement | ⚠ Mulig naturalytelse | ⚠ | ⚠ | – | – | [U]. Bygg ikke automatikk (TV-15) |
| 26 | Lokallag med eget organisasjonsnummer | Alt over | Lokallaget er selv opplysningspliktig, med egen a-melding, egen 10 000-akkumulator og egen § 23-2-vurdering | – | – | – | – | [V] følger av enhetsprinsippet. Sentralleddet kan kjøre lønn som klient (GS-02) |

**Felles systemregler [P/V]:**
- Rapporter i **utbetalingsmåneden**. Frilans-AF rapporteres bare i måneder med utbetaling [P].
- Forskuddstrekk betales første virkedag etter hver utbetaling (fra 2026) [P, jf. D]. Samle honorarer i faste kjøringer (TV-13).
- Halv skatt i desember gjelder ikke honorar, overtid eller bonus [P, jf. C].
- Minstegrenser for trekk: trekk ≤ 100 kr i måneden, ytelser ≤ 500 kr i måneden eller ≤ 2 000 kr i året, og ≤ 10 000 kr for skattefrie organisasjoner [P, jf. C].
- AGA-sone: For arbeidstakere følger sonen underenheten. **For frilans-AF og tillitsvalgte spredt over landet er regelen ikke verifisert ⚠ [U].**

---

## 13. Åpne spørsmål (avklares med Skatteetaten eller revisor før bygging)

1. **Tapt arbeidsfortjeneste** til tillitsvalgte i frivillige organisasjoner: Hvilken beskrivelse skal brukes i a-meldingen? Er det trekk- og AGA-pliktig? Er behandlingen annerledes for selvstendig næringsdrivende? [U]
2. **Styrehonorar til ansatte:** Skal det rapporteres på det ordinære arbeidsforholdet eller på et eget frilans-arbeidsforhold? [U]
3. **AGA-sone** for frilans-arbeidsforhold (tillitsvalgte i sone III–V med sentralledd i sone I). [U]
4. **Trekkfrie utgiftsgodtgjørelser** og 10 000-grensen i skattefrie organisasjoner: Teller de med? Skatteetaten nevner bare trekkpliktige godtgjørelser og naturalytelser. [P/U]
5. **Er 10 000-grensen for mottakeren per organisasjon** (sekundærkilde) eller samlet for alle skattefrie organisasjoner? Hva gjelder for lokallag med eget organisasjonsnummer? [S/U]
6. **OTP for ekstrahjelp og tilkalling** (stillingsgrense og unntak). [U]
7. **Gaver og fribilletter til frivillige** (skattefrihet og eventuelle grenser). [U]
8. **Frist og innhold for skriftlig arbeidsavtale** for korte engasjementer etter endringene i aml. § 14-6. [S/U]
9. **Kontonavnesjekk (Verification of Payee) i Norge:** når og hvordan for innenlandske betalinger i NOK. [S/U]
10. **Utenlandske foredragsholdere** som ikke er artister: PAYE eller ordinær skatt, krav til D-nummer, og AGA ved A1. [U]
11. **Frikjøp modell A:** Bekreft at organisasjonen ikke har opplysningsplikt når den bare refunderer arbeidsgiverens lønnskostnad mot faktura. [V/U]
12. **Egenmelding og omsorgsdager i 2026:** Gjeldende kvoter (ftrl. §§ 8-23 flg. og kap. 9) og hva som er vanlig i utvidede ordninger. Reglene må ligge i en konfigurerbar regeltjeneste, ikke hardkodes. [S/U]
13. **Hvem eier feriedagssaldo og avspasering** når kunden bytter fra egen fraværsmodul til et eksternt HR-system midt i ferieåret? Det trengs en overføringsregel og en protokoll for avstemming. [V]

---

## 14. Kilder

**Runde 1 (interne):** `A-marked-konkurrenter.md`, `B-myndigheter.md`, `C-beregning.md` (lønnsartmatrise #15–17, #38–46; minstegrenser), `D-praksis.md` (kap. 3, 7, 10), `E-byra.md` (klientdelegering), `F-arkitektur.md` (3.3 tilgang, eID), `G-moduler-2026.md` (1.4–1.5, B1–B7, 2.6, wow-liste).

**Hentet 28.10.2026:**
- Skatteetaten – Hvem må levere a-melding (beløpsgrensene 2 000 og 1 000 kr, styrehonorar som frilans-AF, bare utgiftsgodtgjørelse uten AF): https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/hjelp/hvem-ma-levere-a-melding/
- Skatteetaten – Skattefrie organisasjoner (a-meldingen, 10 000 kr, to rapporteringsmåter, AGA av alt): https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/spesielle-grupper/skattefrie-organisasjoner/
- Skatteetaten – Skattefrie organisasjoner (bransjeside: skattefritt for mottakeren under 10 000 kr, forenklet a-melding 80 000 / 800 000): https://www.skatteetaten.no/bedrift-og-organisasjon/rapportering-og-bransjer/bransjer-med-egne-regler/frivillige-og-ideelle-organisasjoner/skattefrie-organisasjoner/
- Skatteetaten – Styrehonorar og godtgjersler i samband med verv: https://www.skatteetaten.no/nn/bedrift-og-organisasjon/arbeidsgiver/a-meldinga/rettleiinga-til-a-meldinga/lonn-og-ytingar/oversikt-over-lonn-og-andre-ytingar/styrehonorar-og-godtgjersler-i-samband-med-verv
- Skatteetaten – Honorar, akkord, prosent eller provisjonslønn: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/lonn-og-ytelser/oversikt-over-lonn-og-andre-ytelser/honorar-akkord-prosent-eller-provisjonslonn
- Skatteetaten – Utenlandske artister og idrettsutøvere (artistskatt 15 %, RF-1091/1092, ikke AGA): https://www.skatteetaten.no/bedrift-og-organisasjon/utenlandsk/utenlandske-artister-og-idrettsutovere/
- Skatteetaten – Betalinger til selvstendig næringsdrivende, rettledning (RF-1301/1321, frist 15.2, skattefrie foreninger omfattet): https://www.skatteetaten.no/en/business-and-organisation/reporting-and-industries/third-part-data/andre-bransjer/betalinger-til-s-n/rettledning/
- Skatteetaten – Grensedragningen mellom arbeidstakere og selvstendig næringsdrivende: https://www.skatteetaten.no/nn/rettskjelder/type/uttalelser/prinsipputtalelser/grensedragningen-mellom-arbeidstakere-og-selvstendig-naringsdrivende/
- Skatteetaten – Stillingsprosent / ansettelsesform / feil F529 (tilkalling): https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/arbeidsforholdet/opplysninger-om-arbeidsforholdet/stillingsprosent · https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/arbeidsforholdet/opplysninger-om-arbeidsforholdet/ansettelsesform · https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/feilmeldinger-magnetedag-og-tilbakemelding/oversikt-over-feilmeldinger-magnetedag/forholdet-mellom-stillingsprosent-og-fastlonn-er-ulogisk-529/
- Lovdata – folketrygdloven § 23-2 (fritak for veldedige og allmennyttige organisasjoner, via D): https://lovdata.no/lov/1997-02-28-19/§23-2
- Smarte Penger – Skattefri inntekt fra skattefrie foreninger (per organisasjon; utgiftsdekning for verv) [S]: https://www.smartepenger.no/pluss/1520-skattefri-inntekt-fra-skattefrie-selskaper-foreninger-og-institusjoner
- Sticos – Utbetalinger til enkeltpersonforetak må rapporteres [S]: https://www.sticos.no/fagstoff/utbetalinger-til-enkeltpersonforetak-maa-rapporteres-innen-16-februar
- Fagforbundet Nittedal – organisatorisk frikjøp, faktura fra kommunen (eksempel på modell A) [S]: https://www.fagforbundet.no/globalassets/_fagforeninger/akershus/nittedal/filer/2023/40-organisatorisk-frikjop-fra-februar-2023-til-februar-2024.pdf
- KPMG – Verification of Payee, utvidelse til EØS fra 1.1.2027 [S/U]: https://kpmg.com/de/en/insights/corporate-governance-and-compliance/verification-of-payee.html
- DNB – Verification of Payee [S]: https://www.dnb.no/bedrift/dagligbank/betaling/betale-til-utlandet/verification-of-payee
- Lovdata – ferieloven (25 virkedager, hovedferie, varsel, overføring): https://lovdata.no/lov/1988-04-29-21 · arbeidsmiljøloven §§ 10-6, 10-7 og 14-15: https://lovdata.no/lov/2005-06-17-62
- NAV – egenmelding (arbeidsgiver utformer rutiner): https://www.nav.no/egenmelding · Sticos – reglene for egenmelding [S]: https://www.sticos.no/fagstoff/slik-er-reglene-for-egenmelding
