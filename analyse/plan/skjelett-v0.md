# Skjelett v0 – roadmap for lønnssystemet (arbeidsnavn «Brutto»)

Dato: 2026-10-28. Utkast laget etter runde 1 (fakta A–G). Skal kritiseres i runde 3 og fylles ut i runde 4.

## Rammer fra gründeren (avklart)
- Frittstående lønnssystem (ikke regnskapsmodul) for norske virksomheter med 10–1000 ansatte: AS, stiftelser, foreninger, organisasjoner.
- Lisensieres til regnskapsbyråer som kjører lønn for sine kunder.
- Norge først.
- Åpne integrasjoner på like vilkår: Utleggsappen (utlegg/reise), OrgLab (medlemshåndtering à la Cornerstone), Tikket (billett/arrangement) og andre bruker samme offentlige API som tredjeparter. Ingen forrang.
- Egne moduler for ferie/fravær, timer og utlegg (krav fra gründer 28.10.2026). Bygges på samme offentlige API, kan byttes ut med eksterne.
- Bankintegrasjon kommer etter hvert: start med filer (pain.001/camt), deretter direkte bank-API (krav 28.10.2026).
- Ansattmodellen skal støtte inndeling i avdelinger, prosjekter o.l.; kartlegging av Tripletex og ReAi pågår (R2-ansattdata-tripletex-reai.md).
- Integrasjon mot ID-porten/Skatteetaten for skattekort, lønnstrekk, utleggstrekk, «K27» m.m. (krav 28.10.2026). Teknisk spesifikasjon i R2-myndighetsintegrasjoner.md. ID-porten = personinnlogging; Maskinporten + systembruker = system-til-system.
- Huma (HR-system) skal integreres, og Brutto skal på sikt erstatte Huma (krav 28.10.2026).
- Gründeren vil senere ha en oversikt over alle områdene for å designe siden/produktet.
- Konkurrenter: SD Worx, Visma Payroll, NettLønn (+ Tripletex/PowerOffice nedenfra, Intect som ny utfordrer).

## Tidslinje (forslag)
- Nå–Q1 2027: Start nå + fundament.
- Q1–Q3 2027: Lønnsmotor, kjøring, myndigheter (TT02), penger/regnskap, plattform-API.
- Mai 2027: a-melding 2.4-spesifikasjon publiseres. Sep 2027: testmiljø 2.4.
- Sep–Des 2027: parallellkjøring hos 2–3 pilotbyråer og 3–5 direktekunder.
- 1.1.2028: første produksjon (årsskifte, a-melding 2.4 fra dag én).
- 2028: skala, ISAE type 2, ISO 27001.
Åpent: om nyetablerte småkunder (ingen migrering) kan gå i produksjon tidligere, f.eks. etter feriepengene 2027.

## Spor, avhengigheter og porter
| Spor | Navn | Bygger på | Port (må passeres før sporet regnes ferdig / går i drift) |
|---|---|---|---|
| S | Start nå | – | Ingen felles port; hver oppgave har eget kriterium |
| 0 | Fundament | – | Syntetisk arbeidsgiver opprettet fra Brreg med ansatte, kryptert fnr, bitemporal historikk og revisjonslogg; pentest uten høy/kritisk; tilgangspolicy testet |
| 1 | Lønnsmotor | 0 | Alle gylne caser for 2026 og 2027 regner likt på øret; 100 % treff mot Skatteetatens trekkrutine; samme input gir byte-lik output |
| 2 | Lønnskjøring og kontroll | 0, 1 | Full lønnsmåned for syntetisk virksomhet med 400 ansatte, fra cut-off til godkjent kjøring, med fire-øyne og avviksliste; korreksjonskjøring endrer aldri godkjent kjøring |
| 3 | Myndigheter | 0, 1 | A-melding for testvirksomheter godkjent i TT02 uten avvik (2.3 og 2.4); skattekort hentet; inntektsmelding sendt i test; KID-betaling generert riktig |
| 4 | Penger og regnskap | 0, 2 | Testbetaling (pain.001) godkjent i bank; bilag bokført i Tripletex, PowerOffice og Visma; avstemming lønn ↔ regnskap ↔ a-melding ↔ bank går i null |
| 5 | Plattform og moduler | 0, 2 | Utleggsappen, OrgLab og Tikket leverer data via offentlig API i sandkasse uten spesialtilgang; ingen dobbel utbetaling i randomisert test |
| 6 | Fravær, timer og utlegg (egne moduler) | 0, 2, 5 | Ferie/fravær, timer og utlegg går fra ansatt via leder til godkjent lønnsgrunnlag kun gjennom det offentlige API-et; feriesaldo og arbeidsgiverperiode stemmer for alle gylne fraværscaser; kunden kan bytte vår utleggsmodul mot Utleggsappen uten dobbel utbetaling |
| 7 | Ansatt og leder | 0, 2 | Pilotansatte logger inn med BankID/passkey, ser forklart slipp; kontonummerendring krever step-up og kontroll; ledere godkjenner alt i én innboks |
| 8 | Byrå | 0, 2, 3 | Pilotbyrå kjører 10 klienter fra byråkonsollen, med samlekjøring av skattekort og a-melding |
| 9 | Tillit og drift | 0 | ISAE 3402 type 1 utstedt; DPA-pakke ferdig; lønnsdag-SLA og beredskap testet |
| M | Migrering og pilot | 1, 2, 3, 4 | Pilotkunder parallellkjørt 2 perioder lik på øret; første ordinære a-melding sendt fra Brutto 2028-01 |
| 10 | Vekst | M, 8 | 3 byråer og 30 direktekunder i drift; første kunde over 300 ansatte |
| 11 | HR-plattform (erstatte Huma) | 5, 6, 7 | Huma-integrasjon i drift hos pilotkunder; første kunde har flyttet personalregister, dokumenter og arbeidsavtaler fra Huma til Brutto uten tap av data |

## Epics per spor (id – tittel)
S: ES.1 Team og lønnsfaglig kjerne · ES.2 Myndighetstilgang og avtaler · ES.3 Pilotbyråer og pilotkunder · ES.4 Juridisk grunnmur · ES.5 Økosystempartnere · ES.6 Avklaringer
0: E0.1 Repo, plattform og miljøer · E0.2 Tenant- og organisasjonsmodell · E0.3 Identitet og tilgang · E0.4 Bitemporal kjerne og revisjonslogg · E0.5 Personvern og kryptering · E0.6 Hendelser, outbox og jobbkø · E0.7 Regelpakker og satsforvaltning · E0.8 API-rammeverk · E0.9 Observability og drift · E0.10 KI-gateway
1: E1.1 Lønnsartkatalog og flagg · E1.2 Beregningspipeline og forklaringsspor · E1.3 Forskuddstrekk · E1.4 Arbeidsgiveravgift · E1.5 Feriepenger · E1.6 Fravær og sykepenger · E1.7 Trekk og vernet beløp · E1.8 Pensjon · E1.9 Retro og korreksjon · E1.10 Tariff og lønnsstiger · E1.11 Gylne testcaser og regelårsrutine
2: E2.1 Arbeidsgiver- og ansattoppsett · E2.2 Lønnskalender og cut-off · E2.3 Variable data inn · E2.4 Kjøringsarbeidsflyt og godkjenning · E2.5 Avviksbasert kontroll · E2.6 Korreksjons- og ekstrakjøringer · E2.7 Lønnsoppgjør · E2.8 Sluttoppgjør og særhendelser · E2.9 Rapporter og revisorpakke · E2.10 Kostnadsfordeling og prosjektlønn
3: E3.1 Maskinporten og systembruker · E3.2 A-melding-aggregat · E3.3 Innsending, tilbakemelding og avstemming · E3.4 Skattekort · E3.5 Innbetaling til Skatteetaten · E3.6 Trekkpålegg og lønnstrekk (utleggstrekk, bidragstrekk) · E3.7 NAV · E3.10 ID-porten for personer · E3.11 Registeroppslag (Brreg, Aa-registeret, ev. Folkeregisteret) · E3.8 Årlige rapporter · E3.9 A-melding 2.4
4: E4.1 Betalingsoppdrag · E4.2 Bankfiler og avstemming (pain.001/002, camt.054) · E4.8 Direkte bankintegrasjon (bank-API/host-to-host, senere fase) · E4.3 Regnskapsposter og mapping · E4.4 Regnskapsadaptere · E4.5 Pensjonsleverandører · E4.6 Avstemmingsrobot · E4.7 Straksutbetaling av refusjoner
5: E5.1 Offentlig API og utviklerportal · E5.2 Hendelser og webhooks · E5.3 Lønnsgrunnlag-API · E5.4 Samtykke og tilkobling · E5.5 Utleggsappen · E5.6 OrgLab · E5.7 Tikket · E5.8 Tid/vakt- og HR-adaptere · E5.9 MCP/agent-API · E5.10 Integrasjonsmonitor · E5.11 Partnerprogram
6: E6.1 Ferie og feriesaldo · E6.2 Fravær, egenmelding og sykefravær · E6.3 Permisjoner og permittering · E6.4 Timer og arbeidstid · E6.5 Turnus/skift og tillegg (import) · E6.6 Utlegg og kvittering · E6.7 Reiseregning · E6.8 Bytte mellom egen og ekstern modul
7: E7.1 Ansattportal/app · E7.2 Forklart lønnsslipp · E7.3 Kontonummer og personalia · E7.4 Lederinnboks · E7.5 Digital distribusjon · E7.6 Spør lønnsslippen · E7.7 Onboarding og offboarding
8: E8.1 Byråkonsoll · E8.2 Klientdelegering i skala · E8.3 Masseoperasjoner · E8.4 Byråmaler · E8.5 Kundeportal · E8.6 GRFS-støtte · E8.7 Lisens og fakturagrunnlag · E8.8 Praksissystem-integrasjon · E8.9 Powered-by
9: E9.1 ISMS og ISO 27001 · E9.2 ISAE 3402 · E9.3 DPA og underleverandører · E9.4 Pentest og sikker utvikling · E9.5 Support og lønnsdag-SLA · E9.6 Beredskap
M: EM.1 Migreringskit · EM.2 Importadaptere · EM.3 Parallellkjøring · EM.4 Pilotgjennomføring · EM.5 Go-live 2028
11: E11.1 Huma-integrasjon (sameksistens) · E11.2 Personalregister og attributteierskap · E11.3 Onboarding og offboarding · E11.4 Dokumentarkiv og arbeidsavtaler med e-signering · E11.5 Medarbeidersamtaler · E11.6 Utstyr og organisasjonskart · E11.7 Migrering fra Huma
10: E10.1 Flere tariffbibliotek · E10.2 Konsern · E10.3 Lønnstransparens og lønnsoppgjørsmodul · E10.4 Prognoser og budsjett · E10.5 Tidsreise og sandkassekopi · E10.6 Unified-API · E10.7 Enterprise-pakke

## Beslutninger (utkast)
| Id | Beslutning | Status |
|---|---|---|
| B1 | Frittstående lønnssystem, ikke regnskapsmodul | Avklart |
| B2 | Åpne integrasjoner på like vilkår; egne og andres moduler bruker samme offentlige API | Avklart |
| B3 | Segmentrekkefølge: 30–300 ansatte med tariff og byråer først; 1000 senere | Forslag |
| B4 | Vi selger programvare, ikke lønnstjeneste med resultatansvar | Forslag |
| B5 | Lønnsmotor som ren funksjon; lovregler som kode, satser som data, kundens lønnsarter i begrenset uttrykksspråk | Forslag |
| B6 | Bitemporal data; godkjente kjøringer uforanderlige; a-melding eget aggregat | Forslag |
| B7 | Kunden eier dataene; byrå har tilgangsavtale; delt DB + RLS + celler | Forslag |
| B8 | Stack: modulær monolitt, Kotlin/JVM eller .NET, Postgres | Delvis avklart |
| B9 | Data lagres i Norge (Azure Norway East), DR i EU | Forslag |
| B10 | Myndigheter via Maskinporten + systembruker; klientsystem for byrå; Skatteetatens trekkrutine som fasit | Delvis avklart |
| B11 | A-melding-aggregat versjonsuavhengig; 2.4 i produksjon fra 2028 | Forslag |
| B12 | Brutto flytter aldri penger; lager betalingsoppdrag som kunden godkjenner i banken | Forslag |
| B13 | KI forbereder, forklarer og flagger, aldri godkjenner, sender eller betaler; EU-region | Forslag |
| B14 | BankID + passkeys + SSO/SCIM; kontonummer-skjold | Forslag |
| B15 | ISAE 3402 type 1 ved første kunde → type 2 → ISO 27001 innen 24 mnd | Forslag |
| B16 | Migrering: a-melding-XML som fasit, parallellkjøring lik på øret, go-live ved årsskifte | Forslag |
| B17 | Pris: per aktiv ansatt direkte; per kjørt slipp for byrå, ingen brukerpris, byråmargin 30–50 % | Forslag |
| B18 | Mottakere uten arbeidsforhold (honorar fra OrgLab/Tikket) som egen mottakertype | Forslag |
| B19 | Første produksjon 1.1.2028 | Forslag |
| B21 | Brutto integreres med Huma først og erstatter Huma over tid; plattformen designes fra dag én for at eierskap til persondata kan flyttes | Avklart (mål) / Forslag (vei) |
| B20 | Egne moduler for ferie/fravær, timer og utlegg, bygget på det offentlige API-et og utskiftbare med eksterne systemer (én kilde per datatype per kunde) | Avklart (moduler) / Forslag (utforming) |
