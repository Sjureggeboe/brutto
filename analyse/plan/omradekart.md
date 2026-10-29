# Områdekart for Brutto – runde 4 (kartlegging av funksjoner og datafelt)

Dato: 2026-10-28. Arbeidsnavn: **Brutto** (ikke bekreftet).

## Gründerens føringer (avklart 28.10.2026)
- **Vi skal ikke bygge noe ennå.** Nå kartlegger vi områder, funksjoner og datafelt. Scope og MVP bestemmes senere. Skriv derfor ingen faser, datoer eller MVP-valg. Behovsvekt (Må/Bør/Kan) er informasjon til den senere scope-jobben.
- Frittstående lønnssystem for norske virksomheter med 10–1000 ansatte (AS, stiftelser, foreninger, organisasjoner), også lisensiert til regnskapsbyråer.
- **Egne moduler for ferie/fravær og for timer** kartlegges fullt.
- **Utlegg og reise løses bare med integrasjoner** (Utleggsappen m.fl.). Ingen egen utleggsmodul. Kjernen har likevel regelmotoren for godtgjørelser (trekkfri/trekkpliktig del, a-meldingskoder) og mottaket av utleggslinjer.
- Åpne integrasjoner på like vilkår: Utleggsappen (utlegg), OrgLab (medlemshåndtering à la Cornerstone), Tikket (billett/arrangement), Huma (HR) og andre.
- Brutto skal på sikt erstatte Huma. HR-området kartlegges derfor fullt.
- Bankintegrasjon kommer etter hvert: først filer, så bank-API.
- Integrasjon mot Skatteetaten, NAV og Altinn: skattekort, trekkpålegg/utleggstrekk, a-melding, K27, inntektsmelding m.m. K27 er NAVs «Oppgjørsrapport arbeidsgiver – refusjoner fra Nav» (`ref-arbg`).
- Ansatte deles inn i avdelinger, prosjekter og andre dimensjoner, med kostnadsfordeling.
- Teknologistakken står åpen.
- Gründerens egne fagavklaringer i S-avklaringer-fra-sally.md gjelder: lønnsartmodell, standardkontering, OTP fra faktura, oppbevaring, personvern og agentgrenser.

## Kilder (scratchpad/research/)
- R0-sdworx-meny.md: SD Worx sin HR-meny (konkurrentreferanse fra gründeren).
- Runde 1: A-marked, B-myndigheter, C-beregning, D-praksis, E-byra, F-arkitektur, G-moduler-2026
- Runde 2:
  - R2-virksomhet, R2-byra, R2-ansatt-org, R2-okosystem, R2-moduler-integrasjoner
  - R2-ansattdata-tripletex-reai: feltlister fra Tripletex og ReAi. Rå API-spesifikasjoner ligger i `scratchpad/r2spec/`.
  - R2-myndighetsintegrasjoner: API-spesifikasjon for Skatteetaten, NAV og Altinn, med tilgangspakker
- Runde 3: R3-kritikk-strategi, R3-kritikk-domene (faglige feil, gylne caser, manglende epics)
- S-avklaringer-fra-sally: gründerens fagavklaringer

## Områdene (id-kode → navn → ansvarlig agent)
| Kode | Område | Agent |
|---|---|---|
| ORG | Organisasjon og oppsett (juridisk enhet, underenheter, AGA-sone, avdelinger, prosjekter, dimensjoner, kostnadssteder, kalendere, lønnsperioder, bankkontoer, kontoplan-mapping, pensjonsordninger, tariffavtaler) | K1 |
| PER | Personer og arbeidsforhold (personalregister, arbeidsforhold, stillinger, yrkeskode, arbeidstid, ansettelsesform, kostnadsfordeling per ansatt, bankkonto, pårørende) | K1 |
| HR | HR og personaladministrasjon (Huma-erstatning: onboarding/offboarding, dokumentarkiv, arbeidsavtaler med e-signering, medarbeidersamtaler, utstyr, organisasjonskart, sykefraværsoppfølging, kompetanse) | K1 |
| LON | Lønnsavtaler og lønnsarter (lønnsartkatalog med flagg, faste tillegg og trekk, satser, lønnsstiger og tariff, lønnsoppgjør) | K2 |
| KJO | Lønnskjøring og beregning (kalender, cut-off, grunnlag, beregningspipeline, kontroll og avvik, godkjenning, korreksjon og retro, ekstrakjøring, sluttoppgjør, feriepengeutbetaling, halv skatt, nettolønnsavtaler) | K2 |
| TRK | Skatt og trekk (skattekort, forskuddstrekk, trekkpålegg og utleggstrekk, bidragstrekk, fagforening, lån og forskudd, vernet beløp, trekkprioritet) | K2 |
| PEN | Pensjon og forsikring (OTP, KLP/SPK, AFP, gruppeliv, yrkesskade, rapportering til leverandør, premie fra faktura) | K2 |
| FRA | Ferie og fravær (egen modul + regler i kjernen: feriesøknad, feriesaldo, egenmelding, sykmelding, arbeidsgiverperiode, sykt barn/omsorgsdager, permisjoner, permittering, foreldrepermisjon, NAV-refusjon og K27) | K3 |
| TID | Timer og arbeidstid (egen modul: timeregistrering, overtid, aml. kap. 10, prosjekttid, tillegg, godkjenning, import fra vakt/turnus) | K3 |
| UTL | Utlegg og reise via integrasjoner (mottak av utleggs- og reiselinjer, godtgjørelsesmotor i kjernen, statens satser, trekkfri/trekkpliktig del, forskudd, kvitteringskrav, bytte av kilde) | K3 |
| MYN | Myndigheter (Maskinporten/systembruker, a-melding, tilbakemelding, avstemming, skattekort-API, trekkpålegg-API, KID-innbetaling, NAV inntektsmelding/sykmelding/K27, ARP/likestilling, sammenstillingsoppgave, Brreg) | K4 |
| BET | Utbetaling og bank (betalingsforslag, pain.001, KID, kontonummer-skjold, utbetalingsstatus, camt/pain.002, bank-API senere, straksbetaling) | K4 |
| REG | Regnskap og kostnadsfordeling (bilag, standardkontering, dimensjonsarv, avsetninger, periodisering, omfordeling, regnskapsintegrasjoner, avstemming lønn ↔ regnskap ↔ a-melding ↔ bank) | K4 |
| POR | Ansattportal og app (lønnsslipp med forklaring, sammenstillingsoppgave, ferie- og fraværssøknad, timer, profil, kontonummer, dokumenter, varsler, flerspråk) | K5 |
| LED | Leder og godkjenning (én innboks for godkjenninger fra egne og eksterne kilder, team, kostnader, delegering, fravær i teamet) | K5 |
| BYR | Byrå (klientportefølje, systembruker for klientsystem, samlekjøringer, maler på tvers, kundeportal, GRFS, oppdragsdokumentasjon, fakturagrunnlag, praksissystem-integrasjon) | K5 |
| ORL | Organisasjonsliv (mottakerklasser, engasjement, styrehonorar, vervgodtgjørelse, tapt arbeidsfortjeneste, frivillige, 10 000-regel, arrangement fra Tikket, honorarer fra OrgLab, artistskatt, lokallag) | K5 |
| RAP | Rapporter og analyse (standardrapporter, revisorpakke, lønnsstatistikk, ARP/lønnskartlegging, sykefraværsstatistikk, prognoser og budsjett, headcount, ESG/VSME, eksport) | K6 |
| PLA | Plattform og integrasjoner (offentlig API, webhooks, kilderegister, samtykke og tilkobling, integrasjonskatalog, Huma, regnskap, tid, bank, pensjon, Digipost, BankID, SSO, MCP/agent-API, integrasjonsmonitor) | K6 |
| SIK | Sikkerhet, tilgang og personvern (roller og tilgangsmodell, arbeidsdeling, step-up, revisjonslogg, kryptering, særlige kategorier, oppbevaring og sletting, lagringssted og bokføringsforskriften § 7-5, DPA, agentgrenser, beredskap) | K6 |
| UTV | Kompetanse og utvikling (kompetanse, jobbprofiler, GAP-analyse, sertifikater, kurs, medarbeidersamtaler, mål, talent; SD Worx Competence/Perform) | K7 |
| HEL | Helse og oppfølging (sykefraværsoppfølging etter aml. § 4-6, oppfølgingsplan, dialogmøter, tilrettelegging, Back2Work-oppgaver, helsesøk med skjerming) | K7 |
| KOM | Kommunikasjon og startside (rollebasert startside, kunngjøringer, lenker, meldinger, varslingssentral, oppgaveinnboks, arbeidsflytmotor og prosessoversikt) | K7 |
| MIG | Migrering og import (fra Tripletex, ReAi, Visma, SD Worx, PowerOffice; hittil-i-år, feriepengegrunnlag, arbeidsforhold-ID, trekkpålegg, pågående fravær, parallellkjøring, avstemming) | K6 |

## Format for agentenes JSON-fil
Skriv én fil: `scratchpad/build/data/omr-<agent>.json`, for eksempel `omr-K1.json`.

```json
{
  "omrader": [
    {
      "id": "ORG",
      "navn": "Organisasjon og oppsett",
      "ingress_md": "2–4 setninger: hva området dekker, hvem som bruker det, og grensene mot andre områder.",
      "grupper": [
        {
          "id": "ORG.1",
          "navn": "Juridiske enheter og underenheter",
          "funksjoner": [
            {
              "id": "F-ORG-01",
              "navn": "Opprett virksomhet fra Brønnøysundregistrene",
              "beskrivelse_md": "Hva funksjonen gjør, sett fra brukeren. 2–5 setninger eller punkter.",
              "niva": "Kjerne | Modul | Integrasjon",
              "behovsvekt": "Må | Bør | Kan",
              "roller": ["Lønnsansvarlig", "Byrå"],
              "regler_md": "Lovkrav, forretningsregler og kanttilfeller, med paragraf eller kilde. Tom streng hvis ingen.",
              "data": ["D-Virksomhet", "D-Underenhet"],
              "integrasjoner": ["Brreg Enhetsregisteret"],
              "behov": ["VK-12", "BY-03"],
              "kilder": ["B-myndigheter §5.3", "https://…"],
              "merknad_md": "Uenighet mellom kilder, usikkerhet [verifiseres], kritikernes merknader. Tom streng hvis ingen."
            }
          ]
        }
      ]
    }
  ],
  "entiteter": [
    {
      "id": "D-Virksomhet",
      "navn": "Virksomhet (opplysningspliktig)",
      "omrade": "ORG",
      "beskrivelse_md": "Hva entiteten er, hovedrelasjoner (1:n osv.), invarianter og historikkbehov.",
      "felt": [
        {
          "navn": "organisasjonsnummer",
          "type": "tekst(9)",
          "pakrevd": "Ja | Nei | Betinget",
          "kilde": "Brreg | Bruker | Beregnet | Skatteetaten | NAV | Integrasjon:<navn>",
          "historikk": "Nei | Gyldighet | Bitemporal",
          "sensitivitet": "Åpen | Intern | Personopplysning | Lønnsdata | Særlig kategori",
          "amelding": "a-meldingsfelt eller –",
          "tripletex": "felt i Tripletex eller –",
          "reai": "felt i ReAi eller –",
          "huma": "felt i Huma eller –",
          "merknad": "Kort. Validering, kodeliste, eksempelverdi (aldri ekte persondata)."
        }
      ]
    }
  ],
  "sporsmal": [
    {"tittel": "…", "omrade": "ORG", "status": "Åpen", "eier": "Gründer | Lønnsfag | Skatteetaten | NAV | Jurist | Revisor | Teknisk | Partner", "md": "Hva er uklart, hvorfor det betyr noe, hvilke funksjoner det gjelder (F-id), forslag til avklaring."}
  ]
}
```

## Regler for id-er
- Funksjon: `F-<KODE>-<nn>`, f.eks. `F-ORG-01`. Nummerer fortløpende innen området.
- Gruppe: `<KODE>.<n>`.
- Entitet: `D-<Navn>` i PascalCase uten æøå, f.eks. `D-Arbeidsforhold`, `D-Lonnsart`, `D-Fravaer`.
- Du kan vise til entiteter andre agenter eier. Bruk da id-ene i listen nedenfor, så alle snakker om de samme.
- Ikke opprett en entitet med samme betydning som en på listen. Trenger du en ny entitet som hører til et annet område, legg den til i din fil og nevn det i svaret ditt.

## Felles entitetsliste (eier → entiteter)
- K7 (UTV, HEL, KOM): D-Kompetanse, D-Kompetansekrav, D-Jobbprofil, D-Sertifikat, D-Kurs, D-Medarbeidersamtale (flyttet fra K1), D-Samtalemal, D-Mal, D-Oppfolgingsplan, D-Dialogmote, D-Oppfolgingsoppgave, D-Kunngjoring, D-Melding, D-Varsel, D-Arbeidsflyt, D-Arbeidsflytmal
- **K1 (ORG, PER, HR):**
  - D-Virksomhet, D-Underenhet, D-Organisasjonsenhet (avdeling/seksjon i hierarki), D-Dimensjonstype, D-Dimensjonsverdi (prosjekt, kostnadssted, aktivitet, egendefinert), D-Kostnadsfordeling
  - D-Lonnskalender, D-Bankkonto (virksomhetens)
  - D-Person, D-Kontaktinfo, D-Personbankkonto, D-Parorende
  - D-Arbeidsforhold, D-Stillingsperiode, D-Stilling
  - D-Dokument, D-Arbeidsavtale, D-Sjekkliste, D-Medarbeidersamtale, D-Utstyr
- **K2 (LON, KJO, TRK, PEN):**
  - D-Lonnsart, D-Lonnsavtale, D-Fastlinje, D-Lonnstabell (stige/trinn)
  - D-Lonnsgrunnlag (variabel linje inn), D-Lonnskjoring, D-Lonnslinje (beregnet transaksjon), D-Lonnsslipp, D-Akkumulator (hittil i år / saldoer), D-Beregningsspor, D-Avvik
  - D-Skattekort, D-Trekkpalegg, D-Trekk (andre trekk og avtaler)
  - D-Pensjonsordning, D-Pensjonsmedlemskap, D-Forsikring
- **K3 (FRA, TID, UTL):**
  - D-Fravaer, D-Fravaerstype, D-Feriesaldo (saldohovedbok for ferie og andre saldoer), D-Permisjon (inkl. permittering), D-Sykefravaerstilfelle (AGP, refusjon), D-Refusjonskrav
  - D-Timeregistrering, D-Arbeidstidsordning, D-Godkjenning
  - D-Utleggslinje (inn fra integrasjon), D-Reise, D-Godtgjorelsessats
- **K4 (MYN, BET, REG):**
  - D-AMelding, D-Innsending, D-Tilbakemelding, D-Systembruker, D-Inntektsmelding, D-NavRapport (K27)
  - D-Betalingsoppdrag, D-Betalingslinje, D-KID
  - D-Bilag, D-Postering, D-Kontomapping
- **K5 (POR, LED, BYR, ORL):**
  - D-Bruker, D-Rolletildeling, D-Delegering
  - D-Klient (byråoppdrag), D-Oppdragsdokumentasjon, D-Fakturagrunnlag
  - D-Engasjement (mottaker uten vanlig arbeidsforhold), D-Mottakerklasse, D-Honorarvedtak, D-Arrangement (kostnadsbærer fra Tikket)
- **K6 (RAP, PLA, SIK, MIG):**
  - D-Integrasjon (installasjon), D-Kilderegister (eier per datatype), D-Hendelse (webhook), D-Revisjonslogg, D-Tilgangslogg, D-Lagringssted, D-Oppbevaringsregel
  - D-Importjobb, D-Migreringsavvik, D-Rapportdefinisjon

## Krav til innhold
- **Grundig:** Gå bredt og dypt. Et område har typisk 3–7 grupper og 10–35 funksjoner. En entitet har typisk 10–40 felt.
  - Ta med kanttilfeller og årshjul: juni, desember, januar, lønnsoppgjør, sluttoppgjør.
  - Skill mellom virksomhet med egen lønn og byrå.
- **Datafelt er hovedsaken.**
  - Bruk a-meldingens offisielle feltnavn der de finnes. Kilder: Skatteetatens informasjonsmodell og JSON-skjema for a-meldingen, kodelister for lønnsbeskrivelse, arbeidsforholdstype, arbeidstidsordning, yrke (STYRK) og permisjon.
  - Bruk feltnavnene fra Tripletex og ReAi (R2-ansattdata-tripletex-reai.md og `scratchpad/r2spec/`).
  - For Huma: bruk OpenAPI-en (https://openapi.humahr.com/v3/api-docs).
  - Skriv «–» når et felt ikke finnes.
- **Sensitivitet:** Følg S-avklaringer §2. Fødselsnummer og kontonummer er Personopplysning og krypteres. Lønnsbeløp er Lønnsdata. Helse og fagforening er Særlig kategori.
- **Historikk:**
  - Bitemporal: alt som påvirker beregning (arbeidsforhold, stillingsperioder, lønn, faste linjer, organisasjonstilhørighet, kostnadsfordeling, skattekort, fravær og permisjon). Se R3-kritikk-domene om hva som må versjoneres.
  - Gyldighet: det som bare har fra/til-dato.
- **Kjernen eier regler med rettsvirkning:** arbeidsgiverperiode, feriesaldo, ferietrekk, skatteklassifisering, a-meldingskoder og godtgjørelsesregler. Moduler og integrasjoner leverer fakta (R2-moduler-integrasjoner, R2-okosystem).
- **Ikke finn på noe.** Merk usikre felt og regler med [verifiseres]. Oppgi kilde-URL for nye fakta.
- **Stil:** norsk bokmål, korte og direkte setninger, ingen tankestrek-innskudd.
- **Valider JSON** med python3 før du er ferdig.
