# Skrivemal for roadmap-spor (runde 4)

Alle filer skrives som gyldig JSON (UTF-8). Valider med `python3 -c "import json,sys; json.load(open(sys.argv[1]))" <fil>` før du er ferdig.

## Språk og stil
- Norsk bokmål. Korte, direkte setninger i aktiv form. Skriv slik en erfaren fagperson snakker.
- Ingen tankestrek-innskudd, ingen «ikke X, men Y»-konstruksjoner, ingen floskler («verdt å merke seg»).
- Konkret: tall, datoer, satser, navn på API-er, tilgangspakker og lovparagrafer der det finnes. Hent dem fra research-rapportene. Merk usikre fakta med «(verifiseres)».
- Navnet på systemet er arbeidsnavnet **Brutto**.
- Henvis til beslutninger som B1, B2 … (se skjelett-v1.md), til epics som E1.3 og til oppgaver som T1.3.2. Bruk bare id-er som finnes.

## Format: én fil per spor-sett
Filen er en JSON-liste med spor-objekter:

```json
[
  {
    "id": "1",
    "navn": "Lønnsmotor",
    "bygger_pa": ["0"],
    "nar": "Jan–jun 2027",
    "leveranse": "Én til tre setninger om hva sporet leverer.",
    "port": "Målbar port. Hva må være sant før sporet regnes som ferdig.",
    "notat_md": "Kort markdown om hvorfor sporet er skåret slik og hva det deler med andre spor.",
    "epics": [
      {
        "id": "E1.3",
        "tittel": "Forskuddstrekk",
        "bygger_pa": ["E0.7", "E1.2"],
        "kilder": ["B5", "B10", "C-beregning §3", "B-myndigheter §3"],
        "mal": "Hva epicen oppnår, 2–4 setninger.",
        "hvorfor": "Hvorfor den trengs og hvorfor nå, 2–5 setninger. Vis til beslutninger og funn.",
        "ferdig": "Når epicen er ferdig, målbart.",
        "oppgaver": [
          {
            "id": "T1.3.1",
            "tittel": "Kort handling i imperativ eller substantivform",
            "type": "kode",
            "utfores_av": "agent",
            "bygger_pa": ["T0.7.2"],
            "berorer": ["beregning", "myndighet"],
            "body_md": "### Bakgrunn\n…\n\n### Hva skal gjøres\n- …\n\n### Akseptansekriterier\n- [ ] …\n\n### Pekere\n- …"
          }
        ]
      }
    ]
  }
]
```

## Felter
- `type`: én av `kode`, `test`, `data`, `design`, `avtale`, `avklaring`, `drift`, `innhold`.
  - `innhold` = fagstoff/tekster/maler (f.eks. lønnsartbibliotek, hjelpetekster).
- `utfores_av`: én av `agent` (kodeagent kan gjøre det alene), `menneske` (krever innlogging, signatur, avtale, fagvurdering eller kundekontakt), `agent med menneske` (agent gjør arbeidet, menneske godkjenner eller leverer input).
- `berorer`: velg fra `beregning`, `myndighet`, `penger`, `sikkerhet`, `personvern`, `integrasjon`, `byrå`, `ai`, `ux`, `drift`, `data`.
- `bygger_pa` på oppgavenivå: oppgave-id-er eller epic-id-er. Kryss-spor-avhengigheter er lov, men bare til id-er som står i skjelett-v1.md eller som du selv lager.
- Id-format: epic `E{spor}.{n}`, oppgave `T{spor}.{epic-nr}.{n}`. Spor S bruker `ES.n` / `TS.n.m`, spor M bruker `EM.n` / `TM.n.m`.

## Omfang og kvalitet
- 4–7 oppgaver per epic. Hver oppgave skal kunne bli et GitHub-issue som en kodeagent eller et menneske kan starte på uten å spørre.
- `body_md` 600–1600 tegn. Alltid de fire overskriftene. 3–7 akseptansekriterier som checkbox-liste, målbare.
- Under «Pekere»: vis til research-rapport og seksjon (f.eks. `C-beregning.md §3.2`), beslutninger, og offisielle kilder (URL) når du har dem.
- Skriv minst én test-oppgave per epic i motor-, myndighets- og pengespor.
- Ikke finn på API-endepunkter eller satser. Bruk det rapportene sier, ellers «(verifiseres)».

## Åpne spørsmål
Hvis du finner noe som må avklares, legg det i en egen fil `sporsmal-<dine spor>.json`:
```json
[{"tittel": "…", "omrade": "Myndigheter", "status": "Åpen", "eier": "Gründer|Lønnsfag|Teknisk|Juridisk|Partner", "md": "Hva er uklart, hvorfor det betyr noe, hvilke oppgaver det stopper (id-er), forslag til hvordan det avklares."}]
```
Status: `Stopper` (hindrer oppstart av et spor) eller `Åpen`.
