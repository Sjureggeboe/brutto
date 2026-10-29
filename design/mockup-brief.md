# Brutto – brief for mockup i Claude Design

Grunnlag: `analyse/build/data/meny.json` (menyen), `fase1.json` (fase 1) og `design.json` (beslutningene B1–B40).
Denne fila er et utgangspunkt for skissene. Den beslutter ikke scope.

## 1. Hva vi skisserer

- Brutto er et norsk lønnssystem for virksomheter med 10–1000 ansatte og for regnskapsbyråer som kjører lønn for kunder.
- Konkurrentene er SD Worx, Visma Payroll og NettLønn. Brutto skal føles roligere og mer forklarende enn dem.
- Fase 1 er smal: ansattoversikt, A07-avstemming, enkle kontroller og grafer. Lønnskjøring kommer i fase 2.
- Skissene bør vise hele menyen, men fase 1-skjermene tegnes i detalj først.

## 2. Prinsipper for hele grensesnittet

- **Vis det som må gjøres nå.** Startsidene er arbeidslister, ikke dashbord med pynt.
- **Vis bare avvik.** Det som stemmer, er grønt og kollapset. Det som avviker, har årsak i klartekst.
- **Hvert tall kan forklares.** Klikk på et beløp viser regel, sats, grunnlag og kilde.
- **Status og frist overalt.** Kjøringer, meldinger og oppgaver har en statuschip og en frist. Det som haster, står først.
- **Fire øyne.** Godkjenn-knappen viser hvem som kan godkjenne. Den som gjorde jobben, kan ikke godkjenne.
- **Gjelder fra.** Endringer har virkningsdato. Tidslinjer viser fortid og framtid.
- **Kilde og eier.** Felt fra Huma, Utleggsappen, a-ordningen eller import har kildemerke og er skrivebeskyttet.
- **Personvern synlig.** Fødselsnummer vises maskert. Helse, fagforening og lønn vises bare med tilgang, og lesing logges.
- **Varsler uten beløp.** E-post og push sier at noe har skjedd. Beløp vises bare etter innlogging.
- **Norsk klarspråk.** Bokmål, korte setninger, faguttrykk fra a-ordningen der de er etablerte (a-melding, AGA, forskuddstrekk).
- **Universell utforming fra dag én (U04).** Kontrast, tastaturnavigasjon og skjermleser. Lys modus først, mørk som variant.
- **Designsystem (U02, forslag).** Lite eget system på Radix eller shadcn/ui, med tokens fra start. Ett grafbibliotek overalt (U03).

## 2b. Visuell stil: Tally-stil

Samme stil som Kontrollrommet (`~/Kontrollrom/ui/stil.css`, etter artefakten «Agenter Kontrollrom»).
Brutto får egen logo og eget navn. Tally-logoen brukes ikke.

**Uttrykk:** varm, lys bakgrunn, hvite kort med store radier, svarte primærknapper, pilleformer overalt, luftig, men tett nok for tabeller.

**Farger (tokens):**

| Token | Verdi | Bruk |
|---|---|---|
| `--bg` | `#f4f3ef` | Varm bakgrunn |
| `--flate` | `#ffffff` | Kort, skinne, skuff |
| `--flate-myk` | `#f7f6f2` | Resultatbokser, hover |
| `--kant` | `#e7e5df` | Kantlinjer |
| `--kant-sterk` | `#dcdad3` | Felt og knapper |
| `--tekst` / `--svart` | `#1c1b19` | Tekst og primærknapp |
| `--dempet` | `#6b6862` | Sekundærtekst |
| `--lilla` | `#a58cf5` | Merke-tall, aksent |

**Statuschips (bakgrunn / tekst):**

| Status | Bakgrunn | Tekst | I Brutto |
|---|---|---|---|
| ok (grønn) | `#e5f3e7` | `#2c6e3f` | Stemmer, Løst, Godkjent |
| kjører (lilla) | `#ece7fd` | `#5b3fc4` | Henter A07, Beregner |
| avvik (oransje) | `#fdebd2` | `#a4570b` | Avvik, Forfaller snart |
| godkjenn (blå) | `#e2eef9` | `#245c90` | Venter på godkjenning, Forklart |
| feil (rød) | `#fbe3df` | `#a32a1d` | Feil fra Skatteetaten, Mangler tilgang, Forfalt |
| nøytral | `#f1f0ec` | `#6b6862` | Utkast, Ikke hentet |

**Typografi:** Figtree (Google Fonts) 400/500/600/700. Brødtekst 14 px. Sidetittel 28 px, vekt 600, `letter-spacing: -0.02em`. Korttittel 18 px, vekt 600. Nøkkeltall 22 px, vekt 600, `tabular-nums`. Beløp alltid med `tabular-nums`.

**Komponenter:**
- **Toppfelt** 64 px høyt på bakgrunnsfargen: logo til venstre, søkepille (300 px, rund) og bjelle med lilla teller til høyre.
- **Ikonskinne til venstre:** flytende hvit søyle, 72 px bred, radius 26 px, ikon med liten etikett under. Aktivt punkt er svart med hvit tekst. Lilla tall-merke for antall som venter. Skinnen erstatter en tradisjonell venstremeny; underpunkter vises som faner øverst på siden.
- **Sidehode:** tittel og undertekst til venstre, knapper til høyre.
- **Knapper:** pilleformede, 44 px (liten: 34 px). Primær er svart med hvit tekst. Farlige handlinger har rød tekst og kant.
- **Faner:** segmentert pille, aktiv fane har svart kant.
- **Filtre:** små piller, aktiv har svart kant.
- **Kort:** hvitt, 1 px kant, radius 18 px, luft 22–24 px.
- **Rader i lister:** 46 px høye, tynn skillelinje, to-linjers tekst (fet tittel, dempet undertekst), chip og tall til høyre.
- **Matrise** (klient × kontroll): hvitt kort med radius 18 px og chips i cellene. Passer arbeidskøen.
- **Skuff** fra høyre for forklaring og detaljer: 560 px, radius 20 px, flytende med skygge. Brukes til «forklaring per tall».
- **Popover:** 380 px, radius 18 px, skygge.
- **Felt:** 40 px høye, radius 10 px.
- **Ikoner:** strekikoner, 2 px strek, runde ender (Lucide-stil).

## 3. Global ramme (alle flater)

Toppfelt:
- Logo «Brutto».
- **Arbeidsflatevelger:** Lønn, Byrå, Leder, Ansatt. Samme person kan ha flere roller og bytter uten ny innlogging.
- **Klientvelger** (bare for byråbrukere): viser hvilken klient du jobber i. «Tilbake til arbeidskøen».
- **Virksomhet og periode:** opplysningspliktig/underenhet og måned (f.eks. «Oktober 2026»).
- **Søk** (Cmd/Ctrl+K): ansatt, klient, kjøring, a-melding, avvik.
- **Varsler** med teller.
- **Brukermeny:** profil, rolle, logg ut.
- Plass til **assistenten** senere (panel til høyre). Den kan aldri sende, godkjenne eller betale (X05).

Ikonskinne til venstre (Tally-stil, se 2b): ett ikon per hovedpunkt for flaten. Underpunktene vises som faner øverst på siden. Punkter som ikke er i fase 1, kan vises dempet med «Kommer».

## 4. Menyen per flate

Merking: **F1** = fase 1 (forslag). Resten er senere.

### 4.1 Lønn (lønnsansvarlig, lønnsmedarbeider, administrator)

| Hovedpunkt | Undersider |
|---|---|
| Hjem | Startside **F1**, Oppgaver og varsler **F1** |
| Lønnskjøring | Lønnskalender, Lønnsgrunnlag, Kjøringer, Kontroll og avvik **F1**, Godkjenning, Korreksjoner og etterbetaling, Sluttoppgjør, Årshjul-veivisere |
| Ansatte | Ansattliste **F1**, Ansattkortet **F1**, Ny ansatt, Honorar og engasjement, Masseendringer |
| Fravær og tid | Fraværskalender, Ferie og saldoer, Sykefravær, Permisjon og permittering, NAV-refusjon, Timer, Arbeidsplaner og tillegg |
| Utlegg og reise | Mottatte utlegg, Godtgjørelser, Kilder for utlegg (bare integrasjon, ingen egen utleggsmodul) |
| Skatt, trekk og pensjon | Skattekort, Trekkpålegg, Andre trekk, Pensjon, Forsikringer |
| Myndigheter | A-melding, Avstemming (A07) **F1**, NAV, Årlige oppgaver, Systembruker **F1**, Kontrollkø |
| Utbetaling og regnskap | Betalinger, Kontoendringer, Bilag, Kostnadsfordeling, Avstemming mot regnskap **F1** |
| Rapporter | Standardrapporter, Kontrollrapporter **F1**, Revisorpakke, Statistikk **F1**, Prognoser, Rapportbygger |
| Oppsett | Virksomhet **F1**, Organisasjon og dimensjoner, Lønnsarter, Tariff og lønnsstiger, Kalendere og perioder, Kontoplan og kontering **F1**, Bank og betaling, Pensjonsordninger, Godkjenningsflyter |
| Administrasjon | Brukere og roller **F1**, Integrasjoner **F1**, API og utviklere, Import og migrering, Revisjonslogg **F1**, Personvern og oppbevaring, Abonnement |

### 4.2 Byrå (lønnsmedarbeider, fagleder, kvalitetsansvarlig)

Når en klient åpnes, går brukeren inn i Lønn-flaten for den klienten.

| Hovedpunkt | Undersider |
|---|---|
| Arbeid | Arbeidskø **F1**, Samlekjøringer, Kontrollkø på tvers av klienter **F1** |
| Klienter | Klientliste **F1**, Klienttilganger (Altinn/systembruker) **F1**, Kundeportal |
| Kvalitet | Maler, Kontroll og GRFS |
| Økonomi | Fakturagrunnlag, Praksissystem |

### 4.3 Leder (linjeleder, prosjektleder)

| Hovedpunkt | Undersider |
|---|---|
| Godkjenninger | Innboks (alt som skal godkjennes) |
| Mitt team | Teamkalender, Timer og saldoer, Kostnader |
| Innstillinger | Delegering (stedfortreder i en periode) |

### 4.4 Ansatt (app og nett, BankID)

| Hovedpunkt | Undersider |
|---|---|
| Hjem | Startside |
| Lønn | Lønnsslipper (forklart linje for linje), Skatt |
| Ferie og tid | Ferie og fravær, Timer, Utlegg (lenke til utleggssystemet) |
| Meg | Profil, Dokumenter |

### 4.5 Kundeportal (byråets kunde, ofte daglig leder)

Minimal: Lever grunnlag, Godkjenn lønn, Spørsmål om avvik.

### 4.6 Honorarmottaker (styre, tillitsvalgte, frivillige)

Bekreft deg (engangsinvitasjon med BankID), Mine utbetalinger.

### 4.7 HR (senere)

Personal, Kompetanse og utvikling, Helse og oppfølging, Kommunikasjon. Huma er HR-kilden fram til da. Vis gjerne som dempet punkt.

## 5. Startsider

### 5.1 Byrå › Arbeidskø (trolig første skjerm i fase 1)

Første bruker er foreslått å være regnskapsbyrå (P02, ikke avklart). Da er dette forsiden.

- Overskrift med periode og frister: «Oktober 2026 · a-melding frist 5. november».
- **Klienttabell, én rad per klient:**
  - Klientnavn og org.nr.
  - Ansvarlig medarbeider.
  - Én statuskolonne per kontrollgruppe: Trekk, AGA, Lønn, År (grønn / gul / rød med antall avvik). Salgsdemo: «alle klienter, alle terminer, ett skjermbilde».
  - Sist hentet A07 og status på systembruker.
  - Neste steg (knapp): «Hent A07», «Se 3 avvik», «Mangler tilgang».
- Filtre: ansvarlig, status, kontrollgruppe, «bare med avvik».
- Sidepanel: frister denne måneden (a-melding 5., forskuddstrekk og AGA-termin), klienter uten gyldig systembruker.
- Ikke porteføljedashbord med grafer først. Arbeidskø først.

### 5.2 Lønn › Startside (én virksomhet)

- **Neste lønnsdag** og status for kjøringen (fase 2; i fase 1 vises siste periode og avstemmingsstatus).
- **Frister:** a-melding, forskuddstrekk, AGA-termin, med dager igjen.
- **Avstemming A07:** stemmer / avvik per kontroll, med lenke til «Kontroll og avvik».
- **Åpne oppgaver og saker i kontrollkøen,** med eier og frist.
- **Nytt siden sist:** nye skattekort, trekkpålegg, meldinger fra NAV og Skatteetaten.
- **Nøkkeltall** (små grafer): lønnskostnad siste 12 måneder, antall ansatte og årsverk, AGA og forskuddstrekk per termin (P06).

### 5.3 Leder › Startside

- Innboks med godkjenninger (timer, fravær, utlegg, lønn) med frist.
- Hvem i teamet er borte denne uka.
- Lønnskostnad for enheten mot forrige måned.

### 5.4 Ansatt › Startside

- Siste lønnsslipp (beløp først etter innlogging), neste lønnsdag.
- Feriesaldo og «Søk ferie».
- Oppgaver: timer som skal sendes, dokumenter som skal signeres.

### 5.5 Kundeportal › Startside

- Én kort med det byrået trenger nå: «Lever grunnlag innen 20.», «Godkjenn lønn», «2 spørsmål fra byrået».

## 6. Skjermer å skissere først (fase 1)

1. **Byrå › Arbeidskø / Klientliste** (se 5.1).
2. **Myndigheter › Avstemming (A07):** per måned og opplysningspliktig. Kolonner: hva Skatteetaten har mottatt, hva regnskapet viser, differanse, status. Kontrollene (P05, forslag):
   1. Forskuddstrekk i a-meldingen mot konto 2600.
   2. AGA mot 2770 og 5400.
   3. Opplysningspliktig lønn mot lønnskostnad.
   4. Feriepengegrunnlag og avsetning på 2940.
   5. Lønn uten aktivt arbeidsforhold.
   6. Arbeidsforhold uten lønn.
   7. Manglende stillingsprosent eller timer.
   8. Store endringer mot forrige måned.
   9. Feil Skatteetaten har registrert.
3. **Kontroll og avvik:** liste med bare avvikene. Hvert avvik har type, periode, forventet og faktisk beløp, forklaring og status (åpen, forklart, løst). «Marker som forklart» krever kommentar og logges (K02, K05).
4. **Forklaringspanel** (sidepanel eller drawer): regel, sats, grunnlag, kilde og historikk for ett tall.
5. **Ansattliste:** søk, filtre (virksomhet, avdeling, status, mottakerklasse), valgbare kolonner, eksport, merke når noe mangler (skattekort, konto).
6. **Ansattkortet** med faner: Oversikt, Personalia, Arbeidsforhold, Lønn og faste linjer, Skatt og trekk, Ferie og fravær, Pensjon, Kostnadsfordeling, Lønnsslipper, Dokumenter, Historikk. I fase 1 er dataene hentet fra a-ordningen og har kildemerke.
7. **Statistikk:** de fire grafene fra P06, pluss avvik over tid per klient.
8. **Klienttilganger / Systembruker:** status per klient (aktiv, venter, mangler), med veiledning for å sette opp systembruker i Altinn.

Senere, men nyttig å skissere for å teste mønstrene:
- **Kjøringer** med statusløp: utkast → beregnet → kontrollert → godkjent → utbetalt → rapportert.
- **Godkjenning** med fire øyne og oppsummering (netto, trekk, AGA, antall mottakere).
- **Ansatt › Lønnsslipp** forklart linje for linje, på mobil.

## 7. Statuser og komponenter

- Statuschip: Stemmer, Avvik, Forklart, Løst, Mangler tilgang, Venter, Utkast, Godkjent, Låst.
- Fristmerke: «om 3 dager», «i dag», «forfalt».
- Kildemerke: A-ordningen, Regnskap, Huma, Utleggsappen, Import, Manuelt.
- Skjermet felt: lås-ikon, «Vis» krever tilgang og logges.
- Tom tilstand: «Alt stemmer for oktober» med tidspunkt for siste henting.
- Tidslinje med «gjelder fra».
- Tabell med valgbare kolonner, filterlinje og eksport.
- Sidepanel for forklaring og historikk.
- Veiviser med steg (ny ansatt, sluttoppgjør, oppsett av systembruker).

## 8. Data i mockupen

- Bruk bare oppdiktede navn, fødselsnumre og kontonumre. Ingen ekte personer eller ekte kunder.
- Bruk fiktive firmanavn, f.eks. «Fjordlys AS», «Stiftelsen Nordlys», «Idrettslaget Ørn».
- Realistiske tall: 10–1000 ansatte, beløp i NOK med mellomrom som tusenskille («1 234 567 kr»).
- Datoformat: «5. nov. 2026» i tekst, «05.11.2026» i tabeller.

## 9. Forslag til første prompt i Claude Design

> Lag en klikkbar mockup av Brutto, et norsk lønnssystem for regnskapsbyråer og virksomheter med 10–1000 ansatte. Tekst på bokmål.
> Start med byråflaten: toppfelt med arbeidsflatevelger (Lønn, Byrå, Leder, Ansatt), klientvelger, periode (oktober 2026), søkepille og bjelle. Ikonskinne til venstre: Arbeid, Klienter, Kvalitet, Økonomi.
> Forsiden er en arbeidskø: én rad per klient med ansvarlig, statuskolonner for Trekk, AGA, Lønn og År (grønn/gul/rød), sist hentet A07 og en knapp for neste steg.
> Klikk på en klient åpner Lønn-flaten med A07-avstemming: kontrollene forskuddstrekk mot 2600, AGA mot 2770/5400, lønn mot lønnskostnad og feriepenger mot 2940. Vis bare avvik, med forklaring i et sidepanel.
> Stil: varm lys bakgrunn (#f4f3ef), hvite kort med radius 18 px, svarte pilleformede primærknapper, pillefiltre og segmenterte faner, flytende ikonskinne til venstre med svart aktivt punkt, statuschips i grønt/lilla/oransje/blått/rødt, font Figtree. Detaljer i en skuff som glir inn fra høyre.
> Bruk bare oppdiktede navn og firma.

## 10. Åpne spørsmål som påvirker skissene

- P02: Er første bruker byrå, virksomhet eller begge? Avgjør om forsiden er arbeidskø eller én virksomhet.
- P01: Avstemmes A07 mot regnskapet, lønnssystemet eller begge? Avgjør kolonnene i avstemmingen.
- P03: Hvor kommer ansattdataene fra i fase 1? Avgjør hvor mye av ansattkortet som er redigerbart.
- P08: Er godkjenning og utbetaling med i fase 1? Forslaget er fase 2.
