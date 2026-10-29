# F – Arkitektur, sikkerhet/compliance, kvalitetssikring og migrering

**Nytt frittstående lønnssystem (SaaS) for norske virksomheter (10–1000 ansatte) og regnskapsbyråer**
Rolle: løsningsarkitekt · Dato: 2026-10-28 · Status: underlag for beslutning, ikke endelig design

> **Avgrensning.** Andre analytikere dekker marked, myndighetskrav og beregningsregler. Her er temaet *hvordan* systemet bygges, sikres, testes, settes i drift og fylles med data fra konkurrentene. Satser, trekkregler og a-meldingsfelter brukes bare som eksempler på arkitekturkrav. **Kildestatus:** Påstander med kilde-URL er sjekket mot kilden 2026-10-28. Kostnads- og ytelsestall er egne anslag og er merket som det. Påstander merket «verifiser» må bekreftes mot primærkilde før de brukes kontraktuelt.

---

## 0. Sammendrag – de viktigste anbefalingene

1. **Beregningen skal være en ren funksjon.** `resultat = f(inndata-øyeblikksbilde, regelpakke-versjon, motorversjon)`. Kjøringen henter ikke klokka, gjør ingen nettverkskall og bruker ikke flyttall. Alle tre identifikatorene og en hash av inndataene lagres per kjøring. Da kan enhver lønnsslipp regnes ut på nytt og gi samme resultat, ned til byte, etter fem år.
2. **Data lagres bitemporalt** med to tidsakser: *gyldighetstid* («fra når gjelder dette i virkeligheten») og *registreringstid* («når fikk systemet vite det»). Godkjente lønnskjøringer er uforanderlige, og alle rettelser gjøres som nye korreksjonskjøringer.
3. **A-meldingen er et eget aggregat** per opplysningspliktig og kalendermåned, adskilt fra lønnskjøringene. Flere kjøringer i samme måned og rettelser av tidligere perioder (erstatningsmelding) blir da håndterbare.
4. **Regellogikk skrives som kode, regelparametre lagres som versjonerte data, og kundespesifikke lønnsarter konfigureres** med et begrenset, typesikkert uttrykksspråk. Et generelt DSL anbefales ikke.
5. **Modulær monolitt i Kotlin/JVM**, med C#/.NET som likeverdig alternativ og teamets kompetanse som avgjørende. PostgreSQL brukes til data, og en Postgres-basert kø med transaksjonell outbox brukes til asynkront arbeid. Kafka og mikrotjenester tas ikke inn de første to årene.
6. **Multi-tenant med delt database og Postgres RLS** som ekstra forsvarslinje bak applikasjonens egen tilgangskontroll. Tenantene fordeles på flere databaseklynger («celler») for å begrense skadeomfang, og store kunder kan få en egen celle. Fødselsnummer, kontonummer, trekkpålegg, fagforeningstrekk og fraværsdetaljer krypteres på feltnivå med en egen nøkkel per tenant (envelope encryption).
7. **Hosting i Azure Norway East** (data i Norge) med katastrofegjenoppretting (DR) i en EU-region. AWS Stockholm er et fullgodt alternativ. Supabase og Vercel passer ikke som produksjonsplattform for lønnskjernen.
8. **Compliance-rekkefølge:** ISAE 3402 type 1 ved første kunde, deretter en type 2-periode (6–12 mnd). ISO 27001 innen 18–24 måneder. SOC 2 tas bare hvis kundene ber om det. Databehandleravtalen må fungere både når kunden kjøper direkte og når kunden går via byrå.
9. **AI skal forberede, forklare og flagge, men aldri godkjenne, sende inn eller utbetale.** Dette håndheves i tilgangsmodellen og ikke bare i prompten. Anthropics førstepartsAPI tilbyr i dag bare inferens i `us` eller `global`, ikke i EU. EU-residens må derfor gå via AWS Bedrock eller Google Cloud i EU-region, eller via en EU-leverandør.
10. **Migrering:** Gamle a-meldinger (XML) og Skatteetatens avstemmingsinformasjon brukes som leverandørnøytral fasit. API-adaptere bygges for Tripletex, PowerOffice Go og Visma.net Payroll. Akseptkriteriet er definert presist: alt som rapporteres, utbetales og bokføres skal være likt på øret. Foretrukne tidspunkter er årsskiftet, eller juli–september etter at feriepengene er utbetalt.
11. **Test:** Gylne filer per regelår som aldri endres når året er lukket, egenskapsbaserte invarianter og en «release-diff» der hver ny versjon regner forrige måned for alle tenanter i skygge før den rulles ut. I tillegg kjøres automatiske ende-til-ende-tester mot TT02 med Tenor-testdata hver natt.
12. **Realistisk tidslinje:** Første pilotkunder går i parallellkjøring oktober–desember 2027 og i produksjon **januar 2028** (årsskiftet). Det krever et team på 5–7 utviklere og 1–2 fulltids lønnsfaglige eksperter fra første dag. Lønnsekspertene er den viktigste ansettelsen.

---

## 1. Arkitekturprinsipper for lønnsmotoren

### 1.1 Prinsippene

| # | Prinsipp | Konsekvens i design |
|---|---|---|
| P1 | **Determinisme**: samme input + samme regelpakke + samme motorversjon gir samme output | Motoren er et rent bibliotek uten I/O. «Nå» sendes inn som parameter. Ingen `float`/`double`. Stabil sortering overalt, og ingen avhengighet til rekkefølgen i hash-maps. |
| P2 | **Reproduserbarhet over tid** | Hver kjøring lagrer `input_hash`, `regelpakke_id`, `motor_versjon`, full inputsnapshot (komprimert JSON) og resultatet. Gamle motor- og regelversjoner kan kjøres i CI. |
| P3 | **Versjonert regelverk** | Regelpakker med virkningsintervall (f.eks. `NO-2027.1`). Parametre som satser, tabeller og grenser er data, logikken er kode. |
| P4 | **Bitemporale fakta** | Alle masterdata som påvirker beregning har gyldighetstid og registreringstid. Etterberegning blir en spørring og ikke et spesialtilfelle. |
| P5 | **Uforanderlighet etter godkjenning** | Godkjente kjøringer, a-meldinger og betalingsfiler muteres aldri. Rettelser lages som nye objekter med referanse til originalen. |
| P6 | **Idempotente sideeffekter** | Innsending til Skatteetaten, NAV og bank går via outbox med stabil idempotensnøkkel og en tilstandsmaskin. Gjentatt forsøk gir aldri dobbel innsending eller dobbel utbetaling. |
| P7 | **Forklarbarhet** | Hver beregnet linje har et forklaringsspor: hvilke regler, parametre og inndata som ga den. Sporet brukes til lønnsslipp, support, revisjon og AI-forklaringer. |
| P8 | **Fullstendig revisjonsspor** | Hvem, hva, når, hvorfor og verdi før/etter, for hver endring og hver godkjenning. Loggen er manipulasjonssikret med hash-kjede. |
| P9 | **Simulering bruker samme motor** | «Hva om» og produksjon kjører samme kode. Den eneste forskjellen er konteksten: ingen outbox og ingen persistens av resultat som «godkjent». |
| P10 | **Tenant-isolasjon i alle lag** | Tenant-kontekst følger hver forespørsel, hver jobb og hver databaseforbindelse. Logger, cache og filer er tenant-merket. |

### 1.2 Determinisme og reproduserbar beregning i praksis

**Beregningskontrakt (pseudokode):**

```
BeregningsInput {
  arbeidsgiver_snapshot      // opplysningspliktig, underenheter, AGA-sone, ordninger
  ansatte_snapshot[]         // arbeidsforhold, lønn, skattekort, trekkpålegg, saldi ... "slik kjent ved T_reg"
  transaksjoner[]            // variable poster, tid/fravær for perioden
  periode, utbetalingsdato
  kjoringstype               // ordinær | ekstra | korreksjon | simulering
  as_of_registreringstid     // T_reg: "kunnskapstidspunktet"
}
BeregningsResultat = Motor(versjon).beregn(input, Regelpakke(id))
lagre(input_hash = SHA-256(kanonisk_json(input)), regelpakke_id, motor_versjon, resultat_hash)
```

- **Kanonisk serialisering** (sorterte nøkler og fast desimalformat) slik at hashen blir stabil.
- **Motorversjon** er en semver-tag på motor-modulen. Gamle versjoner beholdes som byggbare artefakter i et register, slik at en kjøring fra 2028 kan regnes ut på nytt med 2028-motoren selv om koden har endret seg.
- **Reproduksjonstest i CI:** Et utvalg arkiverte produksjonskjøringer (pseudonymisert, eller fra syntetiske tenanter) regnes ut på nytt med sin opprinnelige motor- og regelversjon, og `resultat_hash` skal være identisk.
- **Ikke-determinisme å eliminere:** systemklokke, tidssone (bruk `LocalDate` for virkningsdatoer og Europe/Oslo bare i presentasjonslaget), parallell akkumulering av summer i vilkårlig rekkefølge (desimalsummer er assosiative, men avrunding underveis er det ikke), locale-avhengig formatering, tilfeldige UUID-er i resultatet (bruk deterministiske ID-er avledet av input-hash og linjenummer).

### 1.3 Regelverk versjonert per år og virkningsdato

To typer endringer må holdes fra hverandre:

| Type | Eksempler | Representasjon |
|---|---|---|
| **Parameterendring** | Trinnskatt-satser, personfradrag, AGA-satser per sone, G-beløp (1. mai), feriepengesatser, grenser for OTP (12G), trekktabeller | Data i regelpakken med gyldighetsintervall. Lastes som signert, uforanderlig artefakt. |
| **Logikkendring** | Ny ordning (f.eks. ny type AGA-beregning), endret rekkefølge på trekk, ny a-meldingsversjon | Kode bak versjonsbryter: `if (regelpakke.har(Feature.X))`, eller egen regel-implementasjon registrert for et virkningsintervall |

**Regelpakke-modell:**

```
Regelpakke "NO-2027.2"
  gyldig_fra: 2027-05-01      // f.eks. G-regulering
  arver_fra: "NO-2027.1"
  parametre: { G: …, AGA.sone1: …, … }
  regel_implementasjoner: { forskuddstrekk: "TrekkV2027", feriepenger: "FerieV2021", … }
  status: utkast | forslag (statsbudsjett) | vedtatt | publisert | tilbaketrukket
  signatur: (hash + godkjent av lønnsfaglig ansvarlig + utvikler)
```

- **Hvilken regelpakke gjelder?** Det må bestemmes eksplisitt per regel, ikke globalt:
  - Forskuddstrekk og AGA følger **utbetalingstidspunktet** (kontantprinsippet), slik at et etterslep for desember som betales i januar beregnes med januar-reglene.
  - Feriepenger følger **opptjeningsåret**.
  - Tariffsatser følger **arbeidsperioden** (virkningsdato for lønnsoppgjøret).
  - Konsekvens: motoren slår opp regelpakken per *regel* og per *relevant dato*, ikke én gang per kjøring.
- **Forslagspakker:** Statsbudsjettet legges frem i oktober. Da lages `NO-2028.1-forslag`, og kundene kan simulere effekten. Ved vedtak i desember publiseres `NO-2028.1`. Forslaget arkiveres, men slettes aldri, fordi simuleringer refererer til det.
- **Hurtigrettelser:** Rettes en feil i en publisert pakke, lages en ny pakke-ID (`NO-2027.2a`). Kjøringer som allerede er godkjent med den gamle beholder sin ID. Byrået får en rapport over hvilke kjøringer som ville blitt annerledes, og kan velge korreksjonskjøring.

### 1.4 Bitemporale data

Martin Fowler beskriver payroll som skoleeksempelet på to tidsakser: *faktisk historikk* (gyldighetstid) og *registrert historikk* (hva vi visste når). Registrert historikk er bare-tilføyende, mens faktisk historikk kan endres bakover i tid ([Bitemporal History](https://martinfowler.com/articles/bitemporal-history.html), [Temporal Patterns](https://martinfowler.com/eaaDev/timeNarrative.html)).

**Eksempel:** 10. mars registreres en lønnsøkning med virkning fra 1. januar.
- Spørringen «hva var lønnen i januar, *slik vi visste det 25. januar*?» gir gammel lønn. Den forklarer januarslippen og må kunne reproduseres.
- Spørringen «hva var lønnen i januar, *slik vi vet det nå*?» gir ny lønn. Grunnlaget for etterberegningen er differansen mellom de to.

**Tabellmønster i PostgreSQL:**

```sql
CREATE TABLE arbeidsforhold_lonn (
  tenant_id       uuid        NOT NULL,
  arbeidsforhold_id uuid      NOT NULL,
  gyldig          daterange   NOT NULL,          -- gyldighetstid (virkning)
  registrert      tstzrange   NOT NULL,          -- registreringstid [registrert_fra, erstattet_ved)
  arslonn         numeric(14,2),
  stillingsprosent numeric(7,4),
  endret_av       uuid NOT NULL, endringsgrunn text,
  EXCLUDE USING gist (tenant_id WITH =, arbeidsforhold_id WITH =,
                      gyldig WITH &&, registrert WITH &&)   -- ingen overlapp i begge dimensjoner
);
```

- PostgreSQL 18 har innebygde temporale nøkler (`PRIMARY KEY … WITHOUT OVERLAPS`, `FOREIGN KEY … PERIOD`) for *gyldighetstid*, men ikke for systemtid ([PostgreSQL feature matrix](https://www.postgresql.org/about/featurematrix/detail/temporal-constraints), [Neon: PG18 temporal constraints](https://neon.com/postgresql/postgresql-18/temporal-constraints)). Registreringstiden må derfor håndteres i applikasjonen: kun `INSERT` og «lukking» av `registrert`, aldri `UPDATE` av forretningsfelter og aldri `DELETE`.
- **Hjelpelag:** Et repository-lag gir to funksjoner, `som_kjent(T_reg).gyldig_på(dato)` og `historikk(gyldig_periode)`. Utviklere skal aldri skrive bitemporale spørringer for hånd.
- **Hva skal *ikke* være bitemporalt:** Ren UI-konfigurasjon, brukerpreferanser og saksbehandlingsnotater. Bruk vanlig revisjonslogg der. Bitemporalitet koster i kompleksitet og bør begrenses til data som påvirker beregning, rapportering eller utbetaling.
- **Alternativer vurdert:**
  - *Full event sourcing* er elegant for revisjon, men dyrt for et lite team (projeksjoner, skjemaversjonering av hendelser, replay-ytelse). NAVs sykepengemotor `spleis` (Kotlin) er et norsk eksempel på en hendelsesdrevet beregningsmotor ([github.com/navikt/helse-spleis](https://github.com/navikt/helse-spleis)). Den viser at modellen kan fungere, men den har et stort team bak seg.
  - *Bitemporal database* (f.eks. XTDB) gir mindre driftserfaring og compliance-støtte i markedet.
  - **Valg:** «Event-sourcing light». Bitemporale tilstandstabeller, en bare-tilføyende domenehendelseslogg (som også er outbox) og uforanderlige kjøringssnapshot.

### 1.5 Uforanderlige lønnskjøringer og korrigeringer

**Tilstandsmaskin for lønnskjøring:**

```
Utkast → Beregnet → Kontrollert (avvik kvittert) → Til godkjenning → Godkjent (LÅST)
   → Betalingsfil generert → Betalt (camt/pain.002 bekreftet) → Inngår i a-melding → Lukket
                         ↘ Avvist (tilbake til Utkast, ny versjon)
```

- Fram til *Godkjent* kan kjøringen beregnes på nytt fritt, og hver beregning blir en ny versjon.
- **Etter *Godkjent*:** Ingen mutasjon. Feil rettes med:
  - **Korreksjonskjøring:** Kjører perioden på nytt med dagens kunnskap (`som_kjent(nå)`), beregner differansen mot den opprinnelige og utbetaler eller trekker differansen i en ny kjøring (ekstra eller neste ordinære). Differanselinjene merkes med opprinnelig periode og årsak.
  - **Tilbakeføring:** Hele kjøringen nulles med en speilvendt kjøring. Det brukes nesten bare før utbetaling er sendt til bank.
- **A-meldingsaggregatet** er adskilt. A-meldingen leveres per opplysningspliktig og kalendermåned og settes sammen av alle godkjente kjøringer med utbetalingsdato i måneden. Rettelser av en *tidligere* periode (feil i innrapporterte opplysninger) sendes som erstatningsmelding for den perioden. Etterbetaling rapporteres i måneden den betales. Det er derfor to ulike rettelsesmekanismer:
  1. **Økonomisk rettelse** = korreksjonskjøring, rapporteres i utbetalingsmåneden.
  2. **Rapporteringsrettelse** = ny versjon av a-meldingen for den gamle måneden.

  Arkitekturen må støtte begge. Hvilken som brukes i hvert enkelt tilfelle avgjøres av regelanalytikerne.
- **Godkjenning:** To personer som standard (den som forbereder kan ikke godkjenne samme kjøring). Kunden kan slå det av for små virksomheter, men det logges. Godkjenning krever step-up-autentisering (passkey eller BankID).

### 1.6 Idempotente innsendinger (Skatteetaten, NAV, bank)

**Mønster:** transaksjonell outbox → gateway-worker → ekstern tjeneste → kvittering/tilbakemelding → avstemming.

| Element | Krav |
|---|---|
| Idempotensnøkkel | Deterministisk, f.eks. `hash(tenant, opplysningspliktig, kalendermåned, meldingsversjon)` for a-melding, og `PmtInfId`/`EndToEndId` for betaling. Den genereres **én gang** når objektet godkjennes og regenereres **aldri** ved nye forsøk. |
| Tilstand per innsending | `Klar → Sendt → Mottatt (kvittering) → Behandlet OK / Avvik / Avvist → Erstattet`. Hver overgang lagres med rå forespørsel og respons (kryptert). |
| Ukjent utfall | Ved tidsavbrudd etter sending: **ikke send på nytt** før status er avklart via status-API eller tilbakemelding. Hvis tjenesten ikke har statusoppslag, send med samme meldingsId slik at mottakeren kan gjenkjenne duplikater. |
| Bank | pain.001 med unike `MsgId`, `PmtInfId` og `EndToEndId`. Banken gjør duplikatkontroll. pain.002 (status) og camt.054 (bokførte poster) avstemmes mot kjøringen. Lønn sendes med *category purpose* `SALA` (lønnsbetaling, ISO 20022 eksternt kodesett), som i norske banker kan skjule detaljer for brukere uten lønnstilgang. ISO-versjon (pain.001.001.03 eller .09) og bankspesifikke implementasjonsguider: **verifiser per bank**. |
| Myndighetsgateway | Egen modul og eget deploy med egne hemmeligheter (Maskinporten-nøkkel/virksomhetssertifikat). Ingen andre tjenester har tilgang til de nøklene. |

**Myndighetsintegrasjonene er i endring:**
- Skatteetaten har flyttet a-meldingen og skattekort fra Altinn II til egne API-er (JSON/OpenAPI) med **Maskinporten, systembruker og tilgangspakker**.
- Altinn II-roller fases helt ut **31. desember 2026**. Tilganger etter 19. juni må gis med tilgangspakker. Teknisk dokumentasjon ligger på Skatteetatens GitHub-sider, og testing skjer i TT02 ([Skatteetaten – for leverandører av sluttbrukersystemer](https://www.skatteetaten.no/samarbeidspartnere/reetablering-altinn/systemleverandor/)).
- Skattekort hentes via nye API-er som erstatter RF-1211. Fra 15. desember 2026 opprettes det ikke lenger dialoger i Dialogporten ved henting ([Skatteetaten – skattekort til arbeidsgiver](https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/endret-bruksmonster-for-henting-av-skattekort/)).
- NAV bruker samme modell: leverandøren oppretter én systembruker per kunde, og kunden godkjenner den i Altinn Autorisasjon ([nav.no – ekstern datautveksling](https://www.nav.no/samarbeidspartner/ekstern-datautveksling)). Se også Digdirs veileder for systemleverandører ([docs.altinn.studio](https://docs.altinn.studio/authentication/guides/systemauthentication-for-systemproviders/)).

**Arkitekturkonsekvens:** «Systembruker per kunde (opplysningspliktig)» blir en førsteklasses entitet i Organisasjon-modulen. Den har livssyklus (forespurt → godkjent av kunde i Altinn → aktiv → trukket tilbake), og onboarding-flyten i byråkonsollen må hjelpe byrået med å få hundrevis av klienter til å godkjenne.

### 1.7 Hendelseslogg og revisjonsspor

To logger med ulike formål:

| | Domenehendelseslogg | Revisjonslogg (audit) |
|---|---|---|
| Formål | Integrasjon (outbox), webhooks, projeksjoner | Bevis: hvem gjorde hva, når og hvorfor |
| Innhold | `LønnskjøringGodkjent`, `ArbeidsforholdEndret` … | Aktør (bruker, agent eller system og «på vegne av»), handling, objekt, før/etter (diff), IP/klient, begrunnelse, korrelasjons-ID |
| Lagring | Postgres-tabell (bare-tilføyende), partisjonert per måned | Postgres og daglig eksport til WORM-lagring (uforanderlig blob med juridisk oppbevaring) |
| Integritet | – | Hash-kjede per tenant (`hash_n = H(hash_{n-1} ‖ hendelse)`), daglig forankring (signert «kontrollsum»-hendelse) |
| Oppbevaring | Kort, så lenge den trengs til prosessering | ≥ 5 år etter regnskapsårets slutt for lønnsrelaterte handlinger (se 4.11) |

**Lesing av sensitive felt logges også.** Det gjelder visning av fullt fødselsnummer, kontonummer og trekkpålegg, og eksport.

### 1.8 Regelmotor: kode vs konfigurasjon/DSL

| Alternativ | Fordeler | Ulemper | Vurdering |
|---|---|---|---|
| **Regler som kode** (Kotlin/C#) | Typesikkerhet, refaktorering, testbarhet, ytelse, vanlig utviklerverktøy | Krever utvikler for hver endring | **Ja for lovpålagt logikk** (skatt, AGA, feriepenger, trekkrekkefølge, a-melding) |
| **Parametre som data** | Satsendringer uten deploy, enkelt å revidere | Kan ikke uttrykke ny logikk | **Ja for alle satser, tabeller og grenser** |
| **Begrenset uttrykksspråk** for kundeformler (f.eks. Common Expression Language/CEL eller eget typesikkert mini-språk) | Byrå og kunde kan definere tariff-tillegg som `timer * sats * 1.5` | Må sandkasses, tidsbegrenses og typesjekkes | **Ja, for lønnsarter og tariffregler**, med forhåndsdefinerte funksjoner |
| **Generelt DSL / regelmotor** (Drools, DMN) | Lover at «forretningen kan endre selv» | Det indre plattform-problemet: et nytt programmeringsspråk uten verktøy, tester og feilsøking. Vanskelig å gjøre deterministisk og reproduserbart. | **Nei** |
| **Kjøpt beregnings-API** (slik USA-markedet bruker Symmetry o.l.) | Raskt | Finnes ikke for Norge i moden form, og kjernen ligger hos andre | Nei |

**Lønnsart som konfigurasjon:** Hver lønnsart har egenskaper som trekkpliktig, AGA-pliktig, feriepengegrunnlag, OTP-grunnlag, a-melding-kode (inntektstype/beskrivelse/fordel), regnskapskonto og dimensjoner, sats-kilde (fast, fra arbeidsforhold, fra tariff, formel) og avrundingsregel. Standardlønnsarter leveres av leverandøren og kan ikke endres i sine lovbestemte egenskaper. Kunden kan lage egne lønnsarter ved å arve fra en standard. **Valideringsregler** hindrer ugyldige kombinasjoner, f.eks. en a-melding-kode som krever trekkplikt.

### 1.9 Beregningsgraf

Beregningen modelleres som en **rettet asyklisk graf (DAG)** av noder med eksplisitte avhengigheter:

```
[Inndata: arbeidsforhold, transaksjoner, tid/fravær, skattekort, trekkpålegg, saldi]
   ↓
[Bruttokomponenter] fast lønn → tillegg (tariff) → overtid → fravær (trekk i lønn / sykelønn) → engangsposter → naturalytelser
   ↓
[Grunnlag] trekkgrunnlag (tabell/prosent) │ AGA-grunnlag per sone │ feriepengegrunnlag │ OTP-grunnlag │ trekkfri grense (utlegg)
   ↓
[Trekk i prioritert rekkefølge] forskuddstrekk → (utleggstrekk/bidrag – begrenset av trekkfri beløp) → pensjon egenandel → fagforening → andre trekk
   ↓
[Netto] → [Arbeidsgiverkostnader] AGA, OTP arbeidsgiverdel, feriepengeavsetning
   ↓
[Utdata] lønnsslipp-linjer · a-melding-bidrag · posteringer · betalingslinjer · forklaringsspor
```

- **Hver node** er en ren funksjon `(inndata, parametre) → (verdier, forklaring)`. Grafen sorteres topologisk, og sykler gir byggefeil.
- **Kjente «sykler»** (brutto-for-netto, trekkbegrensning der netto avhenger av trekk) modelleres som en eksplisitt node med fastpunkt-iterasjon, maksimalt antall iterasjoner og deterministisk startverdi. De skal ikke skjules i tilfeldig rekkefølge.
- **Gevinster:** Delvis omregning ved simulering (bare noder som er berørt av endringen), automatisk forklaringsspor («hvorfor er skattetrekket 4 812 kr?» gir node, parametre og inndata), og parallell beregning per ansatt.
- **Forklaringssporet** lagres per linje (kompakt) og er grunnlaget for AI-forklaringer (kap. 5). Språkmodellen formulerer da bare tall som allerede er beregnet og forklart.

### 1.10 Presisjon og avrunding

**Regler for representasjon:**
- Penger: `Decimal` med fast skala i motoren (`BigDecimal` i JVM og `System.Decimal` i .NET). I lagring og ut-formater brukes heltall øre (`bigint`) eller `numeric(14,2)`. **Aldri binært flyttall.**
- Satser og mellomregninger: høyere skala (f.eks. 10 desimaler for timesats × prosent). Avrunding skjer bare på definerte avrundingspunkter.
- **Avrundingspolicy er en del av regelpakken.** Den er ikke spredt i koden: modus (HALF_UP, nedover osv.), presisjon (øre eller krone) og nivå (linje, grunnlag, sum).

**Norske konvensjoner (arkitekturmessig). Faktiske regler bekreftes av beregningsanalytikerne:**

| Område | Vanlig praksis | Arkitekturkrav |
|---|---|---|
| Lønnsslipp-linjer | Hver linje avrundes til øre (kommersiell avrunding, HALF_UP). Summen er summen av avrundede linjer. | Avrunding per linje. Netto = Σ avrundede linjer, slik at slippen alltid summerer. |
| Forskuddstrekk | Tabelltrekk gir hele kroner (tabellverdier). Prosenttrekk avrundes i praksis til hele kroner (**verifiser** mot skattebetalingsforskriften). | Egen avrundingsregel per trekktype. Trekktabeller valideres mot Skatteetatens publiserte tabeller (100 % treff, se 7.3). |
| Arbeidsgiveravgift | Beregnes på **summen** av grunnlag per sone og måned × sats. Summen av avgift per ansatt kan avvike fra dette med noen øre. | AGA beregnes på grunnlagsnivå per opplysningspliktig, sone og måned. Fordeling per ansatt og avdeling (til regnskap) gjøres med **største-rest-metoden**, slik at delsummene alltid treffer totalen. |
| Feriepenger | Grunnlag × sats, avrundet til øre per ansatt og opptjeningsår | Beregnes på årsgrunnlag. Ved delutbetalinger beregnes og avrundes kumulativt (utbetalt hittil trekkes fra), så det ikke oppstår avrundingsdrift. |
| Bank | Ingen øreavrunding ved elektronisk betaling ([Uni Micro](https://unimicro.no/blogg/du-skal-ikke-oereavrunde-ved-elektronisk-betaling)) | Netto utbetales eksakt i øre. |
| Kostnadsfordeling (prosjekt/avdeling) | Prosentfordeling av lønnskostnad | Største-rest-fordeling. Testinvariant: Σ fordelt = total. |

**Migreringsaspekt:** Konkurrentene kan ha andre avrundingspunkter. Under parallellkjøring (kap. 6) må forskjeller klassifiseres som «akseptert konvensjon» eller «feil». Det må finnes en dokumentert liste over kjente konvensjonsavvik.

### 1.11 Ytelse: 1000 ansatte × 500 klienter

**Dimensjonering (anslag):**
- Verste tilfelle: 500 klienter × 1000 ansatte = **500 000 lønnsslipper per måned**. Realistisk byråportefølje: 500 klienter × median 15–40 ansatte, altså 10–20 000. Systemet dimensjoneres for 500 000 med topp i ~72 timer (ca. 18.–25. og siste virkedager).
- **Beregning i minnet:** En lønnsslipp med 30–150 linjer og en DAG med ~50–200 noder tar typisk under 1 ms CPU på JVM/.NET når data er forhåndslastet (eget anslag, må verifiseres med benchmark tidlig). 1000 ansatte gir **under 1 s CPU**, og flaskehalsen blir I/O.
- **Ende-til-ende-mål (SLO):**
  - Beregning av én kjøring for 1000 ansatte: **p95 under 10 s**, inkludert lasting og lagring.
  - Simulering for én ansatt: **p95 under 1 s**.
  - 500 000 slipper: **under 30 min** med horisontal skalering.

**Designgrep:**
1. **Mengdebasert lasting:** Én spørring per entitetstype per arbeidsgiver (ikke per ansatt) gir ingen N+1-problemer. Bitemporale «som kjent ved»-spørringer gjøres med indeks på `(tenant_id, arbeidsforhold_id)` og GiST på intervallene.
2. **Beregning i minnet**, parallelt per ansatt (arbeidspool), med deterministisk sammenstilling.
3. **Bulkskriving** (`COPY`/batch-insert). Resultatet lagres som komprimert JSONB-snapshot per kjøring, med normaliserte linjer bare for det rapportering og a-melding trenger. Tabellene partisjoneres per periode.
4. **Jobbkø med rettferdig planlegging** per tenant, slik at én stor kunde ikke sulter de andre. Køen har mottrykk (backpressure) og prioritet for godkjenningsklare kjøringer.
5. **PDF-generering er den egentlige flaskehalsen** (20–100 ms per slipp med HTML→PDF). Den gjøres asynkront etter godkjenning og skalerer separat. PDF/A lagres i objektlager. Alternativt brukes en rask maltekst-motor (f.eks. Typst).
6. **Forhåndsberegning:** Utkastkjøringer kan beregnes automatisk når nye transaksjoner kommer inn («kontinuerlig lønn»), slik at «Beregn» på lønnsdagen nesten bare er en bekreftelse.

### 1.12 Simulering og «hva om»

| Scenario | Mekanisme |
|---|---|
| Lønnsoppgjør (tariff +X % fra 1.5.) | Overlay av hypotetiske bitemporale fakta (kopier-ved-skriving, ikke persistert som ekte data) og beregning av differanse mot baseline per ansatt |
| Statsbudsjettforslag | Kjøring med forslagspakken `NO-2028.1-forslag` mot desember-data. Viser endring i nettolønn og arbeidsgiverkostnad. |
| Ny ansettelse / endret stilling | Simulering for én ansatt i ansattkort og rekrutteringsverktøy |
| Brutto-for-netto | Fastpunktnoden kjøres «baklengs» |
| Release-diff (intern QA) | Ny motorversjon mot forrige måned for alle tenanter (se 7.6) |

Simuleringer lagres som «scenarier» med utløpstid, skrives aldri til outbox og kan aldri godkjennes. Det håndheves i typen: `SimuleringsKontekst` har ikke metoden `godkjenn()`.

---

## 2. Komponentkart

### 2.1 Oversikt

```
                   ┌───────────────────────── Klienter ──────────────────────────┐
                   │ Byråkonsoll │ Kunde-app (lønnsansvarlig) │ Ansattportal/app │ API-klienter │
                   └───────┬──────────────┬───────────────────┬──────────────┬────┘
                           ▼              ▼                   ▼              ▼
                  ┌────────────────── API-lag / BFF (REST+OpenAPI, OAuth2) ──────────────┐
                  │  Identitet & tilgang (IdP, BankID, SSO, policy)  │  Revisjonslogg      │
                  └──────────────────────────────┬───────────────────────────────────────┘
   ┌──────────────┬──────────────┬───────────────┼───────────────┬──────────────┬──────────────┐
   ▼              ▼              ▼               ▼               ▼              ▼              ▼
Organisasjon  Person/HR-   Avtaler &      Tid & fravær    Lønnskjøring   Rapportering   AI-assistent
/Arbeidsgiver  master      lønnsarter     (import)        & arbeidsflyt  & avstemming   (rådgivende)
   │              │              │               │               │
   └──────────────┴──────────────┴───────┬───────┴───────────────┘
                                         ▼
                              Beregningsmotor (ren, stateless) ◄── Regelpakker (signerte)
                                         │
              ┌──────────────┬───────────┴──────┬──────────────────┬───────────────────┐
              ▼              ▼                  ▼                  ▼                   ▼
      A-melding-aggregat  Betaling        Regnskapsintegrasjon  Lønnsslipp/         API/Webhooks
              │          (pain.001/002,   (posteringer, API)    distribusjon        (ut)
              ▼           camt.054)                             (PDF, Digipost/e-Boks)
     Myndighetsgateway ── Maskinporten/systembruker ──► Skatteetaten (a-melding, skattekort,
     (egen deploy)                                       avstemming) · NAV · Altinn 3 · Brreg
```

### 2.2 Komponenter, ansvar og grensesnitt

| Komponent | Ansvar (eier data om …) | Grensesnitt inn | Grensesnitt ut / hendelser | Kritikalitet |
|---|---|---|---|---|
| **Identitet & tilgang** | Brukere, innlogging (BankID, passkey, SSO), sesjoner, roller, relasjoner (byrå→klient), policyer, systembruker-koblinger | OIDC/SAML (Entra ID, Google), BankID via OIDC-megler, SCIM (provisjonering) | Token med tenant-kontekst, `Policy.tillat(aktør, handling, ressurs)` | Svært høy |
| **Organisasjon/Arbeidsgiver** | Tenant, byrå, juridisk enhet (opplysningspliktig), underenheter, AGA-sone/beregningskode, fribeløp-forbruk, avdelinger/dimensjoner, bankkontoer, pensjonsordninger, systembruker-status | Enhetsregisteret (Brreg), skjema | `ArbeidsgiverEndret`, `SystembrukerGodkjent` | Høy |
| **Person/HR-master** | Person (fnr/D-nr, navn, adresse, adressebeskyttelse), arbeidsforhold (ID, type, start/slutt, stilling%, yrke, arbeidstid), lønn, permisjoner/permitteringer, bankkonto, skattekort (hentet), trekkpålegg | UI, import, API, HR-systemer (Simployer, Sympa o.l.), skattekort-API | `ArbeidsforholdEndret`, `KontonummerEndret` (høy risiko) | Svært høy |
| **Avtaler & lønnsarter** | Lønnsarter (standard + kundens), tariffavtaler, satstabeller, lønnsstiger, kalendere, formler (CEL), kobling lønnsart → a-melding-kode → konto | UI, malbibliotek, AI-forslag (krever godkjenning) | Versjonert katalog til motoren | Høy |
| **Tid & fravær (import)** | Normalisering av timer, overtid, tillegg og fravær fra eksterne systemer. Fraværsregister (egenmeldinger, arbeidsgiverperiode, sykmeldingsgrad), refusjonskrav-grunnlag | Fil (CSV/Excel), API (Tripletex-timer, Planday, Visma Time, Simployer o.l.), webhook | Transaksjoner til kjøring, avviksliste (manglende godkjenning) | Høy |
| **Beregningsmotor** | Ingen data. Ren funksjon: input-snapshot + regelpakke → resultat + forklaring | Bibliotek-kall (in-process), CLI for test | Resultatobjekt | Svært høy |
| **Lønnskjøring/arbeidsflyt** | Kjøringer, versjoner, tilstandsmaskin, godkjenninger, kontrollregler/avvik, korreksjoner, sjekklister, frister | UI, API, AI-agent (begrensede rettigheter) | `KjøringGodkjent` → betaling, a-melding, regnskap, slipp | Svært høy |
| **A-melding-aggregat** | Sammenstilling per opplysningspliktig og måned, versjoner/erstatninger, validering, tilbakemeldinger og avvik | Godkjente kjøringer, manuelle rettelser | Melding til gateway, status til UI | Svært høy |
| **Myndighetsgateway** | Maskinporten-token, systembruker, innsending og henting (a-melding, tilbakemelding, avstemming, skattekort), NAV (inntektsmelding, refusjon), Altinn 3/Dialogporten, Brreg. Kvitteringer og tilbakeforsøk. | Outbox-hendelser | Status-hendelser, rå kvitteringer (kryptert arkiv) | Svært høy |
| **Betaling** | pain.001-generering (lønn, forskuddstrekk/AGA med KID, trekkpålegg til kreditorer, pensjon), pain.002/camt.054-avstemming | `KjøringGodkjent` | Fil via bankintegrasjon (direkte host-to-host, bankintegrasjonspartner eller kundens regnskapssystem). **Kunden godkjenner utbetaling i banken.** | Svært høy |
| **Regnskapsintegrasjon** | Posteringsforslag per kjøring (konto + dimensjoner), periodiseringer (feriepenger/AGA-avsetning), eksport | Konto-mapping per kunde | API-push (Tripletex, PowerOffice Go, Visma eAccounting/Business NXT, Fiken, Xledger, 24SevenOffice …) og fil (SAF-T-kompatible kontoer, CSV) | Høy |
| **Lønnsslipp/distribusjon** | Rendering (HTML/PDF/A, WCAG), arkiv, distribusjon, sammenstillingsoppgave (årlig) | `KjøringGodkjent` | Ansattportal, digital postkasse (Digipost/e-Boks), e-post-varsel *uten* vedlegg | Høy |
| **Ansattportal** | Selvbetjening: slipper, sammenstillingsoppgave, skattekortinfo, fravær, endring av kontonummer (step-up + kontroll), kontaktinfo | BankID/ID-porten-lignende pålogging, passkey | Endringsforespørsler (krever godkjenning hos arbeidsgiver) | Middels–høy |
| **Byråkonsoll** | Porteføljeoversikt: status per klient (kjøring, a-melding, systembruker, avvik, frister), masseoperasjoner, oppdragsansvarlig, maler på tvers av klienter | Policy-filtrert lesemodell | Integrasjon til praksissystem (oppgaver/frister) | Høy |
| **Rapportering & avstemming** | Standardrapporter, lønnsstatistikk, feriepengeliste, avstemming (a-melding ↔ Skatteetatens avstemmingsdata ↔ regnskap ↔ bank), likestillingsrapport (ARP), senere lønnsåpenhet | Lesemodeller/replika | Excel/CSV/PDF, API | Middels |
| **API/webhooks** | Offentlig REST-API (OpenAPI), OAuth2 client credentials, idempotensnøkler, hastighetsbegrensning, signerte webhooks (HMAC), sandkasse-tenant | – | Hendelser til tredjepart | Middels–høy |
| **Revisjonslogg** | Uforanderlig logg, hash-kjede, WORM-eksport, søk for revisor og kunde | Alle moduler (bibliotek) | Revisjonsrapporter | Høy |
| **AI-assistent** | Avviksforklaring, slippforklaring, Q&A (RAG), migrerings-mapping, tariff-tolkning, agent som forbereder kjøring | Lesetilgang via samme API og policy, «agent»-rolle | Forslag som krever menneskelig godkjenning | Middels (rådgivende) |
| *Fellestjenester* | Varsling (e-post/SMS/push), dokumentlager, jobbkø, konfig/funksjonsbrytere, fakturering/abonnement, regelpakke-forvaltning (intern) | | | |

**Prinsipper for grensesnitt:** Moduler kommuniserer i prosess via eksplisitte grensesnitt (porter/adaptere) og domenehendelser. Ingen modul leser en annen moduls tabeller direkte, og det håndheves med arkitekturtester (ArchUnit/Konsist). Da kan moduler skilles ut senere uten omskriving.

---

## 3. Multi-tenant-modell med byrå-hierarki

### 3.1 Domenemodell for tenant

```
Plattform
 └─ Partner (regnskapsbyrå)  ──(tilgangsavtale)──►  Kunde-tenant (arbeidsgiver-konsern)
                                                    ├─ Juridisk enhet (opplysningspliktig, org.nr)
                                                    │   └─ Underenhet (virksomhet, AGA-sone)
                                                    └─ Ansatte / arbeidsforhold
 Direktekunde = Kunde-tenant uten partner (eller med «egen lønnsavdeling» som intern partner)
```

- **Kunden eier sine data** og er behandlingsansvarlig. Byrået har *tilgang* via en tidsbestemt, revisjonslogget tilgangsavtale, men eier ikke dataene. Bytter kunden byrå, overføres tilgangen. Dataene flyttes ikke.
- **Tenant-nøkkelen** er kunde-tenanten. Byrået er en egen entitet med relasjoner til mange tenanter.

### 3.2 Dataisolasjon

| Modell | Isolasjon | Drift/kost | Skalering til 500+ klienter per byrå × mange byråer | Tverrgående byråvisning |
|---|---|---|---|---|
| **Delt skjema + `tenant_id` + Postgres RLS** | Logisk (policy i DB og applikasjon) | Lav. Én migrering. | Svært god (titusenvis av tenanter) | Enkel (filtrert lesemodell) |
| Skjema per tenant | Sterkere logisk | Migrering × N skjemaer, katalog-oppblåsing ved tusenvis | Dårlig over noen tusen skjemaer | Vanskelig (UNION på tvers) |
| Database per tenant | Sterk, egen backup/gjenoppretting per kunde | Høy (tilkoblinger, kost, migrering) | Dårlig for mange små byråklienter | Svært vanskelig |
| **Hybrid: delt pool i celler + egen celle for store kunder** | Delt for små, dedikert for store | Middels | God | Mulig (per celle) |

**Anbefaling:** Delt skjema med RLS, organisert i **celler**. En celle er en Postgres-klynge med N tusen tenanter. Ny celle åpnes ved terskel, og tenanter flyttes mellom celler med logisk eksport/import. Store virksomheter (≥ 500 ansatte) eller kunder med krav kan få dedikert celle mot pristillegg.

**RLS-detaljer og fallgruver:**
- `ENABLE` og `FORCE ROW LEVEL SECURITY` på alle tenant-tabeller. Applikasjonen kobler til som en rolle uten `BYPASSRLS`. Tenant-kontekst settes med `SET LOCAL app.tenant_id = …` *per transaksjon*, noe som er påkrevd ved PgBouncer i transaksjonsmodus.
- RLS er **forsvar i dybden** og erstatter ikke tilgangskontroll i applikasjonen ([praksisoppsummering](https://stackharbor.com/en/knowledge-base/pg-row-level-security-multi-tenant/)). Bruk enkle policyer (likhet på `tenant_id`) for å unngå ytelsestap, og indekser alltid `tenant_id` først.
- Byråkonsollen trenger *metadata* på tvers av klienter (status, frister, avvik), ikke sensitive persondata. Den leses fra en **egen lesemodell** (projeksjon) med byrå-ID og eksplisitt liste over tillatte tenanter. Policyen kan være `tenant_id = ANY(current_setting('app.tenant_ids')::uuid[])`.
- `pg_dump` kjører som standard med `row_security=off` og feiler hvis den mangler tilgang. Backup- og adminroller må håndteres eksplisitt.
- **Automatisert isolasjonstest:** En egen testsuite prøver å lese og skrive på tvers av tenanter via alle API-endepunkter (IDOR-tester) og direkte i DB med feil kontekst. Den kjøres i CI og i pentest.

### 3.3 Tilgangsmodell: RBAC + ReBAC + ABAC

- **Relasjoner (ReBAC):** `byrå-medarbeider —medlem→ byrå —har_oppdrag→ kunde`, `bruker —oppdragsansvarlig→ kunde`, `leder —leder_for→ avdeling`. Dette passer Zanzibar-modellen (OpenFGA) eller Cedar.
- **Roller (RBAC):**

| Rolle | Typiske rettigheter |
|---|---|
| Byrå-admin | Administrere byråbrukere, oppdrag og maler. Ingen automatisk tilgang til persondata hos alle klienter. |
| Byrå-lønnsmedarbeider | Forberede kjøringer for tildelte klienter. Kan ikke godkjenne egne kjøringer. |
| Oppdragsansvarlig (byrå) | Godkjenne kjøringer for sine klienter (to personer) |
| Kunde-admin / lønnsansvarlig | Full tilgang i egen tenant, godkjenne |
| Godkjenner (attestant) | Kun godkjenne og avvise |
| Leder | Se og godkjenne timer og fravær for egne ansatte, ikke lønn (konfigurerbart) |
| Ansatt | Egne data |
| Revisor | Lesetilgang, tidsbegrenset, alt logges |
| Leverandørsupport | Ingen tilgang som standard. «Break-glass» krever kundens samtykke, er tidsbegrenset (f.eks. 4 t), varsles kunden og logges. |
| AI-agent | Lese og lage utkast. Aldri `godkjenn`, `send`, `utbetal` eller `endre_kontonummer`. |

- **Attributter (ABAC):**
  - *Sensitivitetsnivå på ansatt:* «skjermet» for ledergruppe, HR- og lønnsansatte selv. Gir kun tilgang til navngitte brukere.
  - *Adressebeskyttelse* (strengt fortrolig adresse fra Folkeregisteret): adresse skjules for alle unntatt nødvendige prosesser.
  - *Dataklasse:* trekkpålegg, fagforeningstrekk (avslører fagforeningsmedlemskap, som er særlig kategori etter GDPR art. 9), sykefraværsdetaljer og kontonummer.
  - *Handling og kontekst:* step-up gjort ja/nei, IP/land, tidspunkt.
- **Arbeidsdeling (Segregation of Duties):**
  - Den som endrer kontonummer kan ikke godkjenne lønnskjøringen der endringen får effekt. Endring av kontonummer fra ansattportalen krever BankID og varsles til lønnsansvarlig. Dette er en kjent svindelvektor («payroll diversion»).
  - Den som forbereder kan ikke godkjenne.
  - Policy-endringer (roller) logges og varsles.
- **Implementasjon:** En egen policymodul (`Policy.tillat(...)`) med enhetstestede policyer og en relasjonstabell i Postgres. **OpenFGA** eller **Cedar** vurderes når modellen vokser. Velg ikke et eksternt policy-system i første versjon med mindre teamet kan det fra før.

### 3.4 Kryptering og nøkkelhåndtering

| Lag | Tiltak |
|---|---|
| Transport | TLS 1.2+ (helst 1.3) eksternt. mTLS eller privat nettverk internt. HSTS. |
| Lagring (disk) | Skyleverandørens kryptering av disk, database og backup (standard) |
| **Felt-nivå (applikasjon)** | Konvoluttkryptering (envelope encryption): datakrypteringsnøkkel (DEK) per tenant og dataklasse, pakket inn av nøkkelkrypteringsnøkkel (KEK) i KMS/HSM (Azure Key Vault Managed HSM / AWS KMS). AES-256-GCM med tenant-ID som tilleggsdata (AAD), så chiffertekst ikke kan flyttes mellom tenanter. |
| Felter som krypteres | Fødselsnummer/D-nummer, kontonummer, adresse ved adressebeskyttelse, trekkpålegg (saksnr, kreditor, beløp), fagforeningstilknytning, fraværsårsak/gradering, fritekst-notater om ansatt, rå myndighetskvitteringer |
| Søk/oppslag | **Blind indeks:** HMAC-SHA256(fnr, tenant-spesifikk indeksnøkkel) for oppslag og duplikatkontroll uten å dekryptere |
| Visning | Maskering som standard (`010190 *****`). Full visning krever rettighet og logges. |
| Dekryptering | Bare moduler som trenger klartekst: myndighetsgateway (a-melding/skattekort), betaling (pain.001), PDF-rendering. Øvrige moduler ser token eller maskert verdi. |
| Rotasjon | KEK roteres årlig (DEK-er pakkes inn på nytt, data krypteres ikke på nytt). DEK roteres ved mistanke. |
| Sletting | **Kryptografisk makulering (crypto-shredding):** Slett tenantens DEK når oppbevaringstiden er ute. Da blir også data i backup uleselige. |
| Nøkkelsikkerhet | Slettebeskyttelse (soft-delete/purge-protection) på KMS. Nøkkeltilgang via administrert identitet. Ingen menneskelig tilgang til KEK. **Tap av nøkkel = tap av data**, så nøkkelgjenoppretting testes i DR-øvelser. |
| Kundestyrt nøkkel (BYOK/HYOK) | Ikke i første versjon. Kan tilbys store kunder senere. |

**Logger:** Fødselsnummer, kontonummer og beløp per navngitt person skal aldri i applikasjonslogger. Bruk et loggfilter med mønstergjenkjenning (11 siffer med gyldig kontrollsiffer, kontonummer-mønster) og PII-skrubbing i feilsporing (Sentry o.l.).

**Fødselsnummer:** Personopplysningsloven § 12 krever saklig behov for sikker identifisering. For lønn er behovet åpenbart (a-melding og skattekort), men bruken bør begrenses til de prosessene ([lovtekst via Stortinget](https://stortinget.no/no/Saker-og-publikasjoner/Vedtak/Beslutninger/Lovvedtak/2017-2018/vedtak-201718-054/)). Bruk intern person-ID som nøkkel overalt.

---

## 4. Sikkerhet og compliance for å selge til 300–1000-ansatte-kunder og byråer

### 4.1 Hva kjøperne faktisk spør om

1. **ISAE 3402 type 2-rapport (SOC 1-ekvivalent).** Lønn er vesentlig for kundens regnskap, så kundens revisor ber om rapport på leverandørens kontroller. Dette er de facto standard for lønnsleverandører i Norden. Nmbrs bruker for eksempel ISAE 3402 som salgsargument ([nmbrs.com/isae-3402](https://nmbrs.com/isae-3402)). Byråer bruker rapporten i sin egen kvalitetskontroll.
2. **ISO 27001-sertifikat** eller som minimum et dokumentert styringssystem for informasjonssikkerhet (ISMS) etter ISO 27001/27002. Store kunder og offentlig sektor stiller ofte dette som krav.
3. **Databehandleravtale + underleverandørliste + datalokasjon** (EU/EØS, gjerne Norge).
4. **Sikkerhetsspørreskjema**, ofte basert på NSMs grunnprinsipper for IKT-sikkerhet ([NSM v2.1](https://nsm.no/getfile.php/1313975-1717589722/NSM/Filer/Dokumenter/Veiledere/NSMs%20Grunnprinsipper%20for%20IKT-sikkerhet%20v2.1.pdf)), ISO 27001 Annex A eller CAIQ.
5. **Siste pentest-rapport** (sammendrag), SSO, MFA, tilgjengelighets-SLA, exitplan og dataportabilitet, forsikring (cyber/ansvar).
6. **SOC 2 type 2:** Sjelden i Norge, men noen ganger hos internasjonale konsern. KPMG Norge påpeker at SOC 2 (i Norge ofte under ISAE 3000) er mest relevant for SaaS og sky ([KPMG](https://kpmg.com/no/nb/tjenester/revisjon/attestation-services.html)).

### 4.2 Standarder: krav, tid og kostnad (anslag)

> Kostnadene er egne anslag for et selskap med 10–25 ansatte, uten Big Four og i NOK eks. mva. De må erstattes av tilbud. Den interne innsatsen er ofte den største kostnaden.

| Rammeverk | Hva kreves | Tid til første resultat | Ekstern kostnad (anslag) | Intern innsats |
|---|---|---|---|---|
| **ISAE 3402 type 1** | Beskrivelse av tjenesten og kontrollmål (endringsstyring, tilgangsstyring, drift, backup, hendelser, beregningskontroller, innsending, betaling). Revisor tester *utforming* på et tidspunkt. | 3–6 mnd etter at kontrollene er på plass | 200–500 kNOK | 0,3–0,5 årsverk |
| **ISAE 3402 type 2** | Som type 1, pluss testing av *operasjonell effektivitet* over en periode, typisk **6–12 mnd** ([KPMG](https://kpmg.com/no/nb/tjenester/revisjon/attestation-services.html), [DEKRA](https://www.dekra.nl/en/blog-isae-3402-type-1-and-2/)) | Første rapport 9–15 mnd etter at perioden starter | 350 kNOK–1 MNOK per år | 0,5 årsverk løpende |
| **ISO 27001** | ISMS: risikovurdering, erklæring om anvendelse (Statement of Applicability, SoA), 93 Annex A-kontroller (2022), internrevisjon, ledelsens gjennomgang, sertifiseringsrevisjon trinn 1 og 2, årlige oppfølgingsrevisjoner | 6–12 mnd | Rådgiver 200–600 kNOK, sertifiseringsorgan 100–250 kNOK første år og ~60–120 kNOK per år deretter | 0,3–0,5 årsverk |
| **SOC 2 type 2** | AICPA Trust Services Criteria. Revisor må ha AICPA-tilknytning. | 6–12 mnd | Internasjonale anslag USD 30–110k første år totalt ([Drata](https://drata.com/blog/soc-2-audit-cost), [bdemerson](https://www.bdemerson.com/article/soc-2-cost)) | Overlapper 70–80 % med ISO 27001 |
| Compliance-plattform (Vanta, Drata o.l.) | Automatisk innsamling av bevis | – | 100–500 kNOK per år | Sparer innsats |
| ISO 27701 (personvern), ISO 42001 (AI) | Tillegg til ISO 27001 | +3–6 mnd | +30–50 % | Valgfritt, senere |

**Anbefalt veikart (gitt 12–18 mnd til første kunde):**
- **Mnd 0–6:** ISMS-light fra dag én: policyer, risikoregister, tilgangsstyring, endringsstyring via PR med to personers godkjenning og CI, logging, backup-test, leverandørstyring. Kontrollene bygges slik at de *genererer bevis automatisk*.
- **Mnd 9–12:** ISAE 3402 type 1 (eventuelt kombinert ISAE 3402/3000) klar før pilotkunder går i produksjon.
- **Fra første produksjonsmåned:** Type 2-perioden starter. Første type 2-rapport kommer ca. 9–12 mnd etter.
- **Mnd 18–24:** ISO 27001-sertifisering.
- SOC 2 tas bare ved konkret etterspørsel.

### 4.3 Databehandleravtale (DPA)

- **Roller:**
  - Arbeidsgiver er behandlingsansvarlig.
  - Leverandøren er databehandler.
  - Byrået er databehandler for klienten.
- **To kontraktsmodeller** må støttes:
  - (a) Kunden kontraherer direkte med leverandøren, og byrået får tilgang. Da har leverandøren en DPA med kunden, og byrået har sin egen DPA med kunden.
  - (b) Byrået lisensierer og videreselger. Da er leverandøren **underdatabehandler** for byrået, og byrået må ha kundens godkjenning av leverandøren som underleverandør.
- Grunnlag: EU-kommisjonens standardavtaleklausuler mellom behandlingsansvarlig og databehandler (gjennomføringsbeslutning 2021/915) tilpasset norsk lov. Følgende må inn:
  - instruks, formål og kategorier (inkl. særlige kategorier: helse via fravær, fagforening via trekk)
  - sikkerhetstiltak (vedlegg, kobles til ISAE-kontrollene)
  - bistand ved innsyn og ved konsekvensvurdering (DPIA)
  - **varsling av avvik til kunden uten ugrunnet opphold, maks 24 t**, slik at kunden når 72-timersfristen i GDPR art. 33
  - revisjonsrett (oppfylles normalt med ISAE-rapport)
  - sletting og tilbakelevering ved opphør
- **Leverandøren som selvstendig behandlingsansvarlig:** Bare for egne formål, som fakturering, brukerkontoer for innlogging og sikkerhetslogging. **Ikke** bruk kundedata til produktanalyse eller AI-trening uten eget grunnlag. Anbefalingen er å ikke gjøre det i det hele tatt.

### 4.4 Underleverandører

Typisk liste:
- skyplattform
- IdP/BankID-megler
- e-post/SMS
- digital postkasse
- bankintegrasjon
- LLM-leverandør
- overvåking/feilsporing
- supportverktøy
- compliance-plattform

**Krav:**
- Offentlig liste over underleverandører med lokasjon.
- Varsel om endringer (30 dager) og kundens rett til å protestere.
- Vurdering av overføringsrisiko (TIA) for leverandører med tilknytning til USA. EU–US Data Privacy Framework gjelder fortsatt (Latombe-saken ble avvist av EU-domstolens underrett i 2025, men saken er anket; **verifiser** status). Behandling skal likevel ligge i EU/EØS.
- Prinsipp: **all behandling av persondata i EU/EØS**, og ingen supportpersonell utenfor EU/EØS med tilgang.

### 4.5 Datalokasjon

| Alternativ | Status | Vurdering |
|---|---|---|
| **Azure Norway East** (Oslo) | GA med tre tilgjengelighetssoner. Norway West er en region med reservert tilgang for DR ([DCD](https://datacenterdynamics.com/en/news/microsoft-launches-availability-zones-in-norway-east-azure-cloud-region)). | **Anbefalt primær.** Kunder og byråer verdsetter «data i Norge», og offentlig sektor spør ofte. DR til en EU-region (f.eks. Sweden Central), siden Norway West krever egen tilgang. |
| AWS eu-north-1 (Stockholm) | Moden. Ingen full AWS-region i Norge ([DCK](https://www.datacenterknowledge.com/hyperscalers/sweden-gets-its-own-aws-data-centers-amazon-s-first-in-the-nordics)). | Fullgodt (EU/EØS). Bedrock med Claude i EU-regioner. |
| Google Cloud | Norge-region annonsert i 2022 ([Google](https://www.googlecloudpresscorner.com/2022-10-11-Google-Cloud-Announces-Plans-for-First-Cloud-Region-in-Norway-to-Accelerate-Sustainable-Digital-Transformation)). Lansering ikke verifisert. europe-north1 (Finland). | Mulig, men mindre utbredt i norsk B2B-økosystem |
| Norske/nordiske skyleverandører | Suverenitetsargument | Mer driftsansvar og færre administrerte tjenester. Lite team bør unngå det. |

**CLOUD Act-risiko:** Den begrenses med feltkryptering med nøkler i HSM, at nøkkelen aldri forlater regionen, Microsofts EU Data Boundary og avtalefestet håndtering av myndighetsforespørsler. Svar ærlig i anbud: risikoen er redusert, ikke eliminert.

### 4.6 NIS2, digitalsikkerhetsloven og DORA

- **Digitalsikkerhetsloven** trådte i kraft **1. oktober 2025** og gjennomfører NIS1 ([Deloitte](https://www.deloitte.com/no/no/services/legal/perspectives/digital-sikkerhet-i-Norge-nye-krav-for-kritiske-virksomheter-fra-oktober-2025.html), [Legiscope](https://www.legiscope.com/blog/nis2-norge-gjennomforing.html)). Den omfatter tilbydere av samfunnsviktige tjenester i bestemte sektorer og visse digitale tjenester. Små virksomheter er normalt unntatt.
- **NIS2** er per 2026 ikke innlemmet i EØS-avtalen, og norsk ikrafttredelse er ikke fastsatt (samme kilde, **verifiser**). Når NIS2 kommer, kan *skytjenester* og *administrerte IKT-tjenester* (B2B) omfattes når virksomheten er mellomstor (≥ 50 ansatte eller > 10 MEUR omsetning).
- **Konsekvens for oss:**
  - Trolig ikke direkte omfattet de første årene, men **kundene våre er det** (energi, helse, transport, offentlig).
  - NIS2 art. 21 krever at de stiller krav til sikkerheten i leverandørkjeden. Vi vil møte krav om hendelsesvarsling, sårbarhetshåndtering, MFA, kryptering, BCP/DR og leverandørstyring i kontrakt.
  - Bygg derfor på NIS2-nivå fra start. Det overlapper i stor grad med ISO 27001.
- **DORA** (finanssektoren, gjeldende i Norge fra 2025, **verifiser** dato): Banker, forsikring og fond som kunder vil kreve DORA-klausuler (art. 30) og registrere oss i sitt register over IKT-tredjeparter. Kontraktsmalen bør ha et DORA-vedlegg.
- **Personvern:** DPIA er sannsynligvis påkrevd hos kundene (systematisk behandling av ansattdata og særlige kategorier). Leverandøren bør levere en **DPIA-mal** og en referanse-DPIA.

### 4.7 Penetrasjonstester og sikker utvikling

- **Ekstern pentest årlig** og ved store endringer: web, API, autentiseringsflyt, **tenant-isolasjon (IDOR)**, tilgangseskalering, filopplasting og import, og gjennomgang av skykonfigurasjon. Anslag 150–400 kNOK per test. Første test 2–3 mnd før første kunde.
- **Bug bounty** (privat program) etter 12–24 mnd.
- **Sikker utviklingslivssyklus (SDLC):**
  - trusselmodellering per epic
  - statisk kodeanalyse (SAST), avhengighetsskanning (SCA) og SBOM i CI
  - hemmelighetsskanning
  - dynamisk skanning (DAST) mot staging
  - signerte artefakter
  - avhengighets-pinning
  - Renovate/Dependabot med SLA på kritiske sårbarheter (≤ 7 dager)
- **Infrastruktur som kode** med policysjekk (Checkov/Defender) og ingen manuelle endringer i produksjon.

### 4.8 Autentisering: BankID og SSO

| Brukergruppe | Metode |
|---|---|
| Ansatte (portal/app) | **BankID** via OIDC-megler (f.eks. Signicat eller Criipto), alternativt Buypass. **Passkeys** (WebAuthn) etter første BankID-innlogging for rask pålogging. |
| Ansatte uten BankID (utenlandske arbeidstakere med D-nummer, vanlig i bygg, renhold og landbruk) | E-postinvitasjon med passkey eller TOTP, og identitetsbekreftelse hos arbeidsgiver. Begrenset funksjon: kan ikke endre kontonummer selv. |
| Kunde- og byråbrukere | SSO (Entra ID / Google Workspace via OIDC/SAML) med MFA påkrevd, eller passkey/BankID. SCIM for provisjonering hos store kunder. |
| Sensitive handlinger | **Step-up** (ny BankID eller passkey med brukerverifisering) ved godkjenning av kjøring, endring av kontonummer, eksport av persondata og endring av roller |
| Maskin-til-maskin | OAuth2 client credentials med privat nøkkel (private_key_jwt), kortlevde tokens, scopes per tenant |

### 4.9 Logging og overvåking

- **Sikkerhetslogg:** innlogging, mislykkede forsøk, MFA-endringer, rolleendringer, break-glass, eksport, visning av sensitive felt, API-nøkler. Sendes til SIEM (Microsoft Sentinel eller Elastic) med varsling på mønstre som masseeksport, umulig reise, mange mislykkede innlogginger og endring av kontonummer etterfulgt av godkjenning.
- **Oppbevaring:** sikkerhetslogger 12–24 mnd. Revisjonslogg ≥ 5 år (bokføringsrelatert). Applikasjonslogger 30–90 dager uten persondata.
- **Tilgang til logger** er selv en rolle som logges.

### 4.10 Hendelseshåndtering

- **Plan** med roller (hendelsesleder, kommunikasjon, juridisk/personvern, teknisk), alvorlighetsgrader, kontaktlister og varslingsmaler (kunder, Datatilsynet via kunden, NSM/NCSC ved behov).
- **Øvelser:** To bordøvelser i året (løsepengevirus, datalekkasje, kompromittert byrå-konto, feil i skattetrekk for alle kunder rett før 25.).
- **Varsling av personvernbrudd:** Databehandler varsler kunden innen 24 t (DPA). Kunden varsler Datatilsynet innen 72 t.
- **Statusside** og proaktiv kommunikasjon. Etterarbeid uten skyldfordeling (blameless post-mortem) med tiltak i backlog.
- **«Beregningshendelser»** (feil beregning publisert) er egen hendelsestype. Rutinen er å identifisere berørte kjøringer med release-diff, generere korreksjonsforslag per kunde og kommunisere med byråene.

### 4.11 Sletting og oppbevaring

| Datatype | Oppbevaringsgrunnlag | Forslag |
|---|---|---|
| Lønnsgrunnlag, kjøringer, a-meldinger, betalingsfiler, posteringer | Bokføringsloven/-forskriften: primærdokumentasjon 5 år etter regnskapsårets slutt ([Stortinget 2013–14](https://stortinget.no/no/Saker-og-publikasjoner/Publikasjoner/Innstillinger/Stortinget/2013-2014/inns-201314-004/29/), [Revisorregnskap 2020](https://www.revregn.no/asset/pdf/2020/05/2020-05_48.pdf)) | 5 år + inneværende år. Deretter crypto-shredding eller anonymisering (statistikk). |
| Lønnsslipper | Arbeidsgivers dokumentasjon (**verifiser** eksakt hjemmel) | Som over. Ansatte kan laste ned sine før sletting. |
| Systemdokumentasjon (beskrivelse av lønnssystemets funksjon og regelpakker) | Bokføringsregelverket | Regelpakker og motorversjoner oppbevares minst like lenge som kjøringene som brukte dem. |
| Skattekort | Bare for inntektsåret | Slettes etter at sammenstillingsoppgaven er levert og korreksjonsvinduet er ute (f.eks. 1 år) |
| Fraværsdetaljer | Dataminimering | Behold bare det lønnsberegning og NAV-refusjon krever. Ingen diagnoser. |
| Trekkpålegg | Til trekket er avsluttet, deretter som bokføringsgrunnlag | Som lønnsgrunnlag |
| Revisjonslogg | Bevis | 5 år + inneværende år |
| Kunde som avslutter | Kunden har oppbevaringsplikten | (1) Full eksport: PDF-slipper, CSV/JSON av alle data, a-melding-XML, betalingsfiler, posteringer. (2) **Arkivabonnement** (skrivebeskyttet) i 5 år, eller sletting innen 90 dager etter opphør. |

### 4.12 Andre forhold

- **Universell utforming:** Ansattportalen bør oppfylle WCAG 2.1 AA. Store kunder krever det, og regelverket utvides løpende.
- **Arbeidsmiljøloven kap. 9 (kontrolltiltak)** blir relevant hvis AI eller analyse brukes til å overvåke ansatte. Kunden må drøfte med tillitsvalgte, så funksjonaliteten må kunne slås av og forklares.
- **Lønnsåpenhetsdirektivet (EU 2023/970)** er ennå ikke innlemmet i EØS ([NHH](https://www.nhh.no/en/nhh-bulletin/article-archive/2026/june/pay-transparency-directive-eu-countries-miss-the-deadline/)). Datamodellen bør likevel nå ha kjønn, stillingskategori («likt arbeid / arbeid av lik verdi») og komplette lønnskomponenter, slik at rapportering kan legges til uten migrering.

---

## 5. AI i lønn (2026)

### 5.1 Realistiske bruksområder

| Bruksområde | Hvordan | Verdi | Risiko | Kontrollmekanisme |
|---|---|---|---|---|
| **Avviksdeteksjon mot forrige måned** | Primært regler og statistikk (endring > X %, ny lønnsart, netto ≤ 0, manglende timer, ny bankkonto, skattekort-endring). Språkmodell *forklarer og prioriterer*. | Høy. Fanger feil før godkjenning. | Lav | Avvik må kvitteres av menneske før godkjenning |
| **Forklaring av lønnsslipp til ansatt** | Forklaringssporet fra beregningsgrafen pluss en språkmodell som formulerer svaret i et enkelt språk. Tallene settes inn fra strukturerte data, og modellen siterer linjer. | Høy. Færre henvendelser til lønn. | Middels (hallusinasjon) | Automatisk kontroll av at alle tall i svaret finnes i kildedata. Ved avvik avvises svaret og en mal brukes i stedet. |
| **Tolkning av tariffavtaler** | Modellen leser tariff-PDF, foreslår lønnsarter, satser, betingelser og CEL-formler, og genererer testcaser med forventet resultat | Høy for byråer med mange tariffer | Høy (feiltolkning) | Forslag må gjennomgås av lønnsekspert. Ingenting aktiveres uten godkjenning og testkjøring. |
| **Import-mapping av lønnsarter ved migrering** | Modellen kombinert med heuristikk mapper kildens lønnsarter (kode, navn, egenskaper, a-melding-koder) til målkatalogen | Svært høy. Sparer dager per kunde. | Middels | Validering via parallellkjøring (kap. 6) |
| **Spørsmål og svar** (lønnsmedarbeider, kunde) | Søk med kildegrunnlag (RAG) over egen dokumentasjon, Skatteetatens a-meldingsveiledning og kundens egne regler, med kildehenvisning | Middels–høy | Middels | Kildekrav, «vet ikke» som gyldig svar |
| **Forklaring av a-melding-tilbakemeldinger** | Avvikskode → forklaring → forslag til retting (som utkast) | Høy | Lav–middels | Rettingen gjøres av menneske |
| **Agent som forbereder lønnskjøring** | Henter timer og fravær, purrer manglende godkjenninger, oppretter utkastkjøring, kjører kontroller, lager sjekkliste og avvikssammendrag, foreslår korrigeringer | Høy (byråskala) | Middels | Agentrolle uten `godkjenn`, `send` og `utbetal`. Alle handlinger logges som «agent på vegne av bruker». Grenser for antall og omfang. |
| Avstemming (a-melding ↔ regnskap ↔ bank) | Matching og forklaring av differanser | Middels | Lav | Rapport |

### 5.2 Absolutte grenser

- AI **godkjenner aldri** lønnskjøringer, **sender aldri** a-melding, **utbetaler aldri** og **endrer aldri** kontonummer eller roller. Grensene håndheves i policymodulen (kap. 3.3), ikke i prompten.
- Selve lønnsberegningen er **deterministisk og regelbasert**, ikke AI. Det er også viktig for AI-forordningen og GDPR art. 22.
- AI-genererte forslag merkes i UI og revisjonslogg (modell, versjon, prompt-ID, kildereferanser).
- Kunden aktiverer AI-funksjoner per tenant (opt-in). Ansattvendte funksjoner kan slås av separat.

### 5.3 Personopplysninger mot språkmodeller

| Tiltak | Detalj |
|---|---|
| **Dataminimering** | Send aldri fødselsnummer, kontonummer eller adresse. Navn erstattes med tokens (`ANSATT_17`) og settes tilbake etterpå. Send bare feltene oppgaven trenger. |
| **Regionvalg** | Anthropics førstepartsAPI tilbyr i dag inferens-geografi `us` eller `global`, og lagring i arbeidsområdet bare `us` ([Claude docs – data residency](https://platform.claude.com/docs/en/manage-claude/data-residency)). **For EU-residens:** Claude via **Amazon Bedrock i EU-regioner** eller **Google Cloud (Google-administrert) i EU-region**, der regionen bestemmes av endepunktet (samme kilde). Alternativt Azure OpenAI med EU Data Zone eller en EU-leverandør (Mistral). Modell- og regiontilgang endres ofte, så **verifiser i konsollen**. |
| **Lagring hos leverandør** | Avtale om null lagring (Zero Data Retention), ingen trening på kundedata, og leverandøren listet som underdatabehandler |
| **Egen logging** | Prompt og svar lagres i egen database under samme tenant-isolasjon og oppbevaringsregler. Kortere oppbevaring for prompter (f.eks. 90 dager). |
| **Arkitektur** | **AI-gateway** som abstraherer leverandøren (byttbar), med maskering, policy, kostnadsgrenser per tenant, evaluering og logging. Modellvalg per brukstilfelle. |
| **Innholdssikkerhet** | Prompt-injeksjon fra importerte dokumenter (tariff-PDF, CSV) behandles som data. Agentens verktøy har minste privilegium. Ingen fri nettilgang i agentmodus. |
| **DPIA** | AI-tillegg i leverandørens referanse-DPIA |

### 5.4 EU AI Act

- **Vedlegg III punkt 4** gjør KI-systemer for (a) rekruttering og utvelgelse og (b) beslutninger om arbeidsvilkår, forfremmelse og oppsigelse, fordeling av oppgaver basert på atferd eller egenskaper, og overvåking og evaluering av ytelse og atferd, til høyrisiko ([artificialintelligenceact.eu – Annex III](https://artificialintelligenceact.eu/annex/3/)).
- **Gjelder det lønn?**
  - Selve lønnsberegningen er regelbasert programvare definert av mennesker og er normalt ikke et «KI-system» etter definisjonen i art. 3(1).
  - Slippforklaring, Q&A, mapping og tariff-tolkning med menneskelig godkjenning tar ikke beslutninger om arbeidsvilkår. De er trolig ikke høyrisiko, og art. 6(3) unntar «snevre prosedyreoppgaver» og «forberedende oppgaver».
  - Avviksdeteksjon må utformes som **datakvalitetskontroll** og ikke som vurdering av den ansattes atferd (f.eks. «mistenkelig overtid hos person X»). Ellers nærmer den seg 4(b).
  - **Unngå i produktet** (eller behandle som høyrisiko): individuelle lønnsanbefalinger basert på ytelse, prediksjon av at ansatte vil slutte (flight risk), produktivitetsscore.
- **Tidslinje:**
  - Plikter om KI-kompetanse (art. 4) og forbudene gjelder allerede i EU.
  - Det er politisk enighet (7. mai 2026) i «Digital Omnibus» om å utsette høyrisikopliktene for vedlegg III til **2. desember 2027** ([Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)). Formell publisering må **verifiseres**.
  - Åpenhetsplikter (art. 50: opplyse om at brukeren snakker med KI) gjelder fra august 2026.
  - Norge gjennomfører via EØS og nasjonal KI-lov. Norsk ikrafttredelse og tilsynsmyndighet må **verifiseres**.
- **Praktisk:** Merk AI-svar i ansattportalen («generert av KI, kontroller mot lønnsslippen»), dokumenter hvert brukstilfelle (formål, data, risiko, menneskelig kontroll) og før et AI-register. Da er vi forberedt hvis tolkningen endres.

---

## 6. Migrering fra konkurrenter

### 6.1 Data som må med

| Kategori | Innhold | Hvorfor | Kritikalitet |
|---|---|---|---|
| **Arbeidsgiver** | Opplysningspliktig/underenheter, AGA-sone og beregningskode, **forbrukt fribeløp hittil i år** (sone 1a), næringskode, pensjonsordning (OTP-leverandør/avtalenr, sats), AFP-tilknytning, bankkontoer, kontoplan-mapping, dimensjoner | Korrekt AGA og posteringer | Kritisk |
| **Ansatte** | Ansattnr (behold), fnr/D-nr, navn, adresse, adressebeskyttelse, kontonummer, e-post/mobil, språk | Identitet, utbetaling | Kritisk |
| **Arbeidsforhold** | **ArbeidsforholdId (behold!)**, type, startdato, underenhet, stillingsprosent-historikk, yrkeskode (STYRK), arbeidstidsordning, avlønningstype, årslønn/timelønn, dato for siste lønnsendring, tariff/lønnsstige/ansiennitet, sluttdato/årsak | A-melding-kontinuitet. Skatteetaten krever at antall arbeidsforhold og underenhet er uendret, og anbefaler å beholde ID-en (alternativ 1) ([Skatteetaten – bytte lønnssystem](https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/arbeidsforholdet/spesielle-forhold/bytte-lonnssystem)) | Kritisk |
| **Permisjoner/permitteringer** | ID, periode, prosent, type | A-melding (må videreføres eller avsluttes og startes riktig) | Kritisk |
| **Lønnsarter** | Kode, navn, egenskaper (trekk, AGA, ferie, OTP), a-melding-koder, konto | Mapping til målkatalog | Kritisk |
| **Faste transaksjoner** | Faste tillegg og trekk med periode, lån/forskudd med saldo, fri bil/naturalytelser | Neste kjøring | Høy |
| **Hittil i år (HiÅ)** | Per ansatt per a-melding-beskrivelse og lønnsart: brutto, forskuddstrekk, trekkgrunnlag, AGA-grunnlag per sone, feriepengegrunnlag, OTP-grunnlag, naturalytelser, trekkpålegg-summer | Sammenstillingsoppgave (frist 31.1.), prosent- og halvtrekk, grenser | Kritisk ved migrering midt i året |
| **Feriepenger** | Grunnlag i fjor (til utbetaling i år) og utbetalt hittil, grunnlag i år hittil, 60+-grunnlag, sluttoppgjør | Korrekt feriepengeutbetaling og avsetning | Kritisk |
| **A-meldinghistorikk** | Innsendte a-meldinger (XML) for inneværende og forrige år, med meldingsId | Erstatningsmeldinger for gamle perioder, revisjonsspor | Høy |
| **Saldoer** | Feriedager, avspasering/fleks, egenmeldingsdager og pågående sykefravær (arbeidsgiverperiode), omsorgsdager | Fravær og NAV-refusjon | Høy |
| **Trekkpålegg** | Utleggstrekk (namsmann, Skatteetaten/SI), bidragstrekk (NAV), saksnr, KID, mottaker, beløp/prosent, gjenstående | Lovpålagt trekk | Kritisk |
| **Pensjon** | Innmeldingsstatus, grunnlag hittil, egenandel, offentlig tjenestepensjon (KLP/SPK)-medlemskap | Rapportering til pensjonsleverandør | Høy |
| **Historiske lønnsslipper (PDF)** | 1–5 år | Ansattportal, arbeidsgivers oppbevaringsplikt | Ønskelig (eller arkivabonnement hos gammel leverandør) |
| **Skattekort** | **Migreres ikke.** Hentes på nytt fra Skatteetaten. | Ferskhet | – |

### 6.2 Eksportformater og kilder

| Kilde | Hva finnes | Vurdering |
|---|---|---|
| **A-meldinger (XML)**, alle systemer | Arbeidsforhold, inntekter per beskrivelse, forskuddstrekk, AGA-grunnlag og permisjoner per måned | **Leverandørnøytral og autoritativ.** Bygg en importør som rekonstruerer arbeidsforhold og HiÅ per a-melding-beskrivelse. Lønnsarter rekonstrueres ikke (de er aggregert), så de må komme fra kilden. |
| **Skatteetatens avstemmingsinformasjon** | Det Skatteetaten har registrert per arbeidsforhold og inntektsmottaker for valgte perioder | **Fasit for HiÅ-avstemming.** Hentes via API (systembruker). |
| **Tripletex** (API v2, OpenAPI) | Ansatte, arbeidsforhold, lønnstransaksjoner og slipper, lønnsarter ([Apideck-guide](https://www.apideck.com/blog/how-to-integrate-with-the-tripletex-api)). Autentisering med consumer- og employee-token. | Adapter i v1. Kunden gir token. |
| **PowerOffice Go** (API) | Ansatte, lønnsarter, lønnslinjer, lønnsinnstillinger | Adapter i v1. Mange byråkunder. |
| **Visma.net Payroll (Norge)** | Visma oppgir egne norske tjenester som «Payroll Norway API» og «Employee Public API» (navn fra Vismas statusoversikt, endepunkter ikke kartlagt: **verifiser** på developer.visma.com). Krever trolig partneravtale. Eksport via rapporter (Excel). | Adapter i v1–v2 hvis API-tilgang oppnås. Ellers rapport-eksport. |
| **Visma Lønn / Huldt & Lillevik** (Windows, Visma-eid ([Cinven](https://www.cinven.com/news-insights/visma-strengthens-its-focus-on-hrm-solutions))) | Rapporter til Excel/CSV, ASCII-filer med faste posisjoner for import av transaksjoner ([Moment docs](https://docs.moment.team/help/moment-by-topic/integrations/file-exports/wage-system/huldt-and-lillevik-lonn)) | Malbasert Excel-import og a-melding-XML |
| **SD Worx** | Typisk leveranse som tjeneste (BPO). Eksport bestilles fra leverandøren (filer/rapporter). | Kontraktsfestet eksport. A-melding-XML og avstemmingsinformasjon som kontroll. |
| **Generisk** | Excel/CSV-maler: ansatte, arbeidsforhold, HiÅ, feriepenger, faste transaksjoner, trekkpålegg | Alltid tilgjengelig. **AI-assistert kolonne- og lønnsart-mapping.** |

**Migreringskit (produktkomponent):** kilde-adaptere → staging-skjema (rådata) → mapping (regler + AI-forslag + manuell godkjenning) → validering (referanseintegritet, summer, a-melding-konsistens) → avstemming mot Skatteetatens avstemmingsdata → import som bitemporale fakta med `registrert = migreringstidspunkt` og kilde-referanse → parallellkjøring.

### 6.3 Beste tidspunkt

| Tidspunkt | Fordeler | Ulemper | Anbefaling |
|---|---|---|---|
| **Årsskifte (januar)** | Ingen HiÅ for lønn. Gammelt system lager sammenstillingsoppgave for fjoråret. Rent snitt. | Alle vil bytte da. Desember er byråenes travleste måned. Regelendringer kommer samtidig. Fjorårets feriepengegrunnlag må likevel med. | **Primærvindu.** Kapasiteten styres med bookingkalender. |
| **Juli–september** (etter feriepengeutbetaling) | Fjorårets feriepenger er utbetalt, så bare årets grunnlag trengs. Rolig periode. | HiÅ må migreres, og sammenstillingsoppgaven lages av nytt system med migrerte HiÅ. | **Sekundærvindu** |
| Mai–juni | – | Feriepenger og G-regulering | Unngå |
| Oktober–desember | – | Halvt trekk i desember, årsskiftearbeid, lønnsoppgjør med etterbetaling | Unngå (unntatt forberedelse og parallellkjøring for januar-oppstart) |

Ved oppstart midt i året skal **ett system** stå for hele årets sammenstillingsoppgave. Det betyr det nye systemet, basert på HiÅ per a-melding-beskrivelse. Arbeidsforhold skal ikke rapporteres fra to systemer for samme periode (Skatteetaten, se 6.1).

### 6.4 Metode for parallellkjøring

1. **Innlesning og datavalidering:** Antall ansatte, arbeidsforhold og permisjoner skal stemme mot siste a-melding. HiÅ skal stemme mot avstemmingsinformasjonen (diff = 0).
2. **Skyggeberegning av historiske måneder:** Beregn de siste 1–3 avsluttede månedene i nytt system med migrerte inndata. Sammenlign linje for linje med gammelt systems resultater (slipp per ansatt, per lønnsart, per grunnlag, AGA, posteringer).
3. **Parallell live-måned (1–2 mnd):** Begge systemer kjører. **Gammelt system er master** (sender a-melding og utbetaler). Nytt system genererer a-melding og pain.001 som valideres, men ikke sendes. A-meldingen valideres mot skjema og kontrollregler, eventuelt i testmiljø.
4. **Avviksklassifisering:** Hvert avvik får én av kategoriene:
   - (A) migreringsfeil, som rettes i data
   - (B) feil i nytt system, som rettes i kode eller regel
   - (C) feil i gammelt system, som dokumenteres for kunden og eventuelt korrigeres
   - (D) akseptert konvensjonsforskjell (avrunding, rekkefølge)

   Kundens lønnsansvarlig godkjenner alle avvik i kategori C og D.
5. **Go/no-go → overgang:** Nytt system blir master. Gammelt system fryses (skrivebeskyttet, lisens beholdes ≥ 3 mnd for oppslag og tilbakefall). Systembruker aktiveres.
6. **Oppfølging (hypercare) i 2 kjøringer:** Utvidet kontroll, daglig statusmøte for pilotkunder.

### 6.5 Akseptansekriterier («lik på øret»)

**Definisjon:** *Alle beløp som rapporteres (a-melding), utbetales (bank) og bokføres (regnskap) skal være identiske til øre mellom gammelt og nytt system for 100 % av ansatte. Unntak er dokumenterte og kundegodkjente avvik i kategori C og D.* Mellomregninger som ikke forlater systemet kan avvike så lenge sluttbeløpene er like.

| Kontrollpunkt | Krav |
|---|---|
| Netto utbetalt per ansatt | Diff 0,00 |
| Forskuddstrekk per ansatt | Diff 0 |
| AGA-grunnlag per sone og AGA-beløp per opplysningspliktig | Diff 0,00 |
| Feriepengegrunnlag og OTP-grunnlag per ansatt | Diff 0,00 |
| Sum per lønnsart (mappet) | Diff 0,00 |
| A-melding | Struktur og innhold likt per arbeidsforhold og inntektsbeskrivelse. Ingen avvik ved validering. |
| Posteringer | Balanserer. Sum per konto og dimensjon er lik. |
| Betalingsfil | Sum = Σ netto + trekk til kreditorer. Antall mottakere er likt. |
| HiÅ etter migrering | Lik avstemmingsinformasjonen fra Skatteetaten |
| Dekning | 100 % av ansatte sammenlignet, ikke stikkprøver |
| Godkjenning | Signert akseptprotokoll fra kunde (og byrå) |

---

## 7. Teststrategi

### 7.1 Testpyramide for lønn

| Nivå | Innhold | Verktøy (JVM / .NET / TS) |
|---|---|---|
| Enhetstester per regelnode | Hver node i grafen, med grensetilfeller | JUnit/Kotest · xUnit · Vitest |
| **Gylne filer per regelår** | Scenario-katalog (300–1000 scenarier): input-JSON (bitemporale fakta) + regelpakke → forventet slipp, grunnlag, a-melding-fragment og posteringer | Godkjenningstesting (snapshot), diff i PR |
| Egenskapsbaserte og metamorfe tester | Invarianter (7.2) | jqwik/Kotest-property · FsCheck/CsCheck · fast-check |
| Differensielle tester | Mot offisielle tabeller og konkurrent (7.3) | Egen sammenligningsmotor |
| Integrasjonstester | Gateway mot TT02, bank-XSD, regnskaps-API-er (sandkasse) | Testcontainers, kontrakttester |
| Ende-til-ende | Syntetisk tenant: import → kjøring → godkjenning → a-melding (TT02) → tilbakemelding → bankfil → posteringer | Playwright + API-tester, hver natt |
| Ytelse og last | 500 000 slipper, topp-simulering | k6/Gatling, før hver topp-sesong |
| Sikkerhet | IDOR- og tenant-isolasjon, avhengigheter, DAST | Egen suite + ZAP |
| Mutasjonstesting | På regelkode (måler testenes styrke) | PIT · Stryker |

**Regler for gylne filer:**
- Scenariene lages og **signeres av lønnsfaglig ekspert**, ikke bare av utviklere.
- Gylne filer for år N **låses når år N er avsluttet**. Feil som oppdages senere legges inn som «kjent feilliste» med korreksjonsscenario. Filen endres ikke.
- CI kjører **alle år** hver gang, fordi korreksjoner og reproduksjon krever at gamle år fortsatt beregnes likt.
- Dekningsmatrise:
  - lønnsform × fravær × trekkpålegg × AGA-sone × spesialmåneder (feriepengemåned uten trekk, halvt trekk i desember, G-regulering)
  - sluttoppgjør, flere arbeidsforhold, D-nummer/kildeskatt, naturalytelser, 60+-ferie
  - korreksjoner på tvers av år

### 7.2 Egenskapsbaserte invarianter (eksempler)

- **Konsistens:** netto = Σ opptjening − Σ trekk. Σ a-melding-beløp = Σ relevante slipplinjer. Σ posteringer = 0.
- **Determinisme:** `beregn(x) == beregn(x)` byte for byte, også med tilfeldig rekkefølge på inputlister.
- **Korreksjonslikhet:** `original + korreksjon ≡ omregning fra bunnen med korrigerte data` (økonomisk sluttresultat).
- **Fordeling:** Σ avrundede fordelte beløp = avrundet total (største rest).
- **Monotonisitet** der regelverket tilsier det, f.eks. at høyere bruttolønn aldri gir lavere tabelltrekk innen samme tabell.
- **Trekkgrenser:** Netto etter utleggstrekk ≥ trekkfri beløp når regelen gjelder.
- **Metamorf:** Å dele en måned i to kjøringer gir samme månedssum (for regler der det skal være slik). Å endre registreringstid uten å endre gyldighet gir uendret resultat.

### 7.3 Sammenligning mot fasit og konkurrentsystem

- **Trekktabeller:** Skatteetaten publiserer trekktabellene. Motoren skal reprodusere **alle** tabeller og alle trinn med 100 % treff. Testen kjøres automatisk når tabellene publiseres (desember).
- **Konkurrent:** Hver migrering er en differensiell test (kap. 6). Avvik i kategori B blir nye gylne filer, så testsuiten vokser med kundebasen.
- **Byrå-partnere:** Med samtykke og pseudonymisering kan et utvalg byråklienter skyggeberegnes jevnlig i forkant av lansering.

### 7.4 Testmiljøer hos myndighetene

- **Altinn TT02 og Skatteetatens testmiljø** for de nye a-melding- og skattekort-API-ene. Oppsett av autentisering er beskrevet i Samarbeidsportalens «Kom i gang i testmiljøet (TT02)» ([Skatteetaten](https://www.skatteetaten.no/samarbeidspartnere/reetablering-altinn/systemleverandor/)).
- **Tenor testdatasøk:** syntetiske personer (fnr/D-nr), syntetiske virksomheter (Brønnøysund) og arbeidsforhold (NAV) ([Tenor](https://www.skatteetaten.no/skjema/testdata/)). Testmiljøene behandler bare syntetiske data ([Skatteetaten testinnsending](https://www.skatteetaten.no/no/Bedrift-og-organisasjon/rapportering-og-bransjer/tredjepartsopplysninger/Testinnsending-xml/)), så **produksjonsdata skal aldri brukes i test**.
- **Maskinporten testmiljø** og systembruker i TT02 med egen testklient. Hemmeligheter adskilt fra produksjon.
- **NAV:** testmiljø for arbeidsgiver-API-er (inntektsmelding/refusjon) i henhold til NAVs API-oversikt.
- **Bank:** pain.001 valideres mot ISO-XSD og bankens implementasjonsguide. Sandkasse hos bank eller integrasjonspartner.
- **Automatisering:** Ende-til-ende mot TT02 kjøres hver natt med varsling ved brudd. Endringer i myndighets-API-er oppdages før kundene merker dem.

### 7.5 Testing av årsskifte og regelendringer

**Årshjul (regelpakke-prosess):**

| Når | Hendelse | Aktivitet |
|---|---|---|
| Okt (uke 41) | Statsbudsjettet legges frem | Forslagspakke `NO-ÅÅÅÅ.1-forslag` innen ~2 uker. Simulering for kunder. Gylne filer for nytt år påbegynnes. |
| Nov–des | Budsjettforlik og vedtak, nye trekktabeller og skattekort | Endelig pakke. Full regresjon. Trekktabell-test. Kodefrys for annet enn regelpakker fra ~10. des. Publisering ~20. des. |
| Jan | Første kjøring i nytt år | Ekstra overvåking, nye skattekort hentes, HiÅ nullstilles, feriepengegrunnlag rulles over, sammenstillingsoppgave (frist 31.1.) |
| Mai | G-regulering, revidert nasjonalbudsjett | Midtårspakke (`NO-ÅÅÅÅ.2`) |
| Vår–høst | Lønnsoppgjør (tariff) | Tariffpakker og etterbetaling (korreksjonskjøringer i stor skala). Testes som scenario. |

**Testing av årsskifte:**
- **Tidsreise-miljø** der klokken settes til 15. desember og videre over nyttår. Hele tenanter (syntetiske) kjøres for desember og januar.
- **Korreksjoner på tvers av år:** feil i desember rettet i januar. Riktig regelpakke per regel (kap. 1.3), riktig a-melding-periode og riktig sammenstillingsoppgave.
- **Øvelse** i november med pilotkunder og byråer.

### 7.6 Kontinuerlig oppdatering og release-diff

- **Regelpakker** forvaltes i egen modul med eget releaseløp (kan publiseres uten full plattformrelease). To-personers godkjenning: lønnsfaglig og utvikler.
- **Release-diff (skyggeberegning før utrulling):** Før hver produksjonsrelease beregnes **forrige måneds kjøringer for alle tenanter** på nytt med ny kode. Avvik som ikke er forklart i release-notatet **stopper utrullingen**. Dette er den viktigste enkeltkontrollen mot regresjon i lønn, og den er god evidens for ISAE.
- **Funksjonsbrytere per tenant** (f.eks. Unleash, som opprinnelig er norsk) for gradvis utrulling til pilotkunder først.
- **Kundevendt endringslogg** for regelendringer: hva endret seg, fra når, og hvordan det påvirker deg.

---

## 8. Drift

### 8.1 Tilgjengelighetskrav rundt lønnsdager

**Kritiske vinduer:**
- ca. den 15. til 25. (forberedelse og utbetaling 25.)
- siste 3 virkedager (lønn ved månedsslutt)
- den 1. til 5. (a-meldingsfrist den 5.)
- bankenes avskjæringstid typisk 1–2 virkedager før lønnsdag

| Mål | Normalt | Kritisk vindu |
|---|---|---|
| Tilgjengelighet (SLO) | 99,9 % per måned | 99,95 % |
| Endringer | Kontinuerlig utrulling | **Endringsfrys** for ikke-kritiske releaser (f.eks. den 20.–25. og siste 2 virkedager). Kun nødrettelser med to-personers godkjenning. |
| Support | Kontortid | Utvidet (f.eks. 07–20) og vakt |

**Avhengigheter vi ikke styrer** (Maskinporten, Skatteetaten-API, Altinn, bank):
- Syntetisk overvåking hvert 5. minutt.
- Køing og automatisk nytt forsøk.
- Kunden informeres proaktivt.
- Bevis lagres (logg over forsøk og nedetid hos myndigheten) med tanke på tvangsmulkt. Skatteetaten har tidligere frafalt tvangsmulkt i overgangsperioder ([Skatteetaten](https://www.skatteetaten.no/nn/bedrift-og-organisasjon/arbeidsgiver/a-meldinga/siste-fra-a-ordningen/ingen-tvangsmulkt-for-a-meldingen-i-mai-juni-og-juli/)).

### 8.2 Varsling

- **Internt:** Varsler basert på SLO og feilbudsjett (feilrate, latenstid, køalder, outbox-etterslep, mislykkede innsendinger, alder på manglende kvitteringer), vaktplan (24/7 for P1 i kritiske vinduer) og runbooks per varsel.
- **Mot kunde og byrå:**
  - statusside
  - meldinger i appen
  - e-post eller SMS ved hendelser som påvirker deres kjøringer
  - «fristvarsler» i byråkonsollen (klienter som ikke har godkjent kjøring X dager før lønnsdag, a-melding ikke sendt den 3.)

### 8.3 Skalering ved månedsskifte

- Toppene er **forutsigbare**: Planlagt forhåndsskalering av arbeidsnoder fra ca. den 18. og før månedsslutt, pluss køstyrt autoskalering (KEDA eller tilsvarende) for beregning, PDF og gateway.
- **Database:** Vertikal skalering i topp, lesereplika for rapporter og byråkonsoll, partisjonering, ingen lange transaksjoner, tilkoblingspool.
- **Rettferdighet:** Kvoter per tenant og byrå i køen. Hastighetsbegrensning mot eksterne API-er (myndighetenes kvoter).
- **Lasttest** hver høst (før desember og januar) og før store kundeoppstarter.

### 8.4 Backup og gjenoppretting

| Mål | Verdi | Tiltak |
|---|---|---|
| **RPO** (kjernedatabase) | ≤ 5 min (regionhendelse), ≈ 0 ved sone-/instansfeil | Sone-redundant HA (synkron standby), kontinuerlig WAL-arkivering (PITR, 35 dager) |
| **RTO** | ≤ 30 min ved sone-/instansfeil, ≤ 4 t ved regionbortfall | Infrastruktur som kode, automatisert gjenopprettingsløype, DR-region i EU |
| Backup-integritet | Uforanderlig | Daglige snapshot til separat konto/abonnement med uforanderlighet (WORM). Beskyttelse mot løsepengevirus. |
| Dokumenter (PDF, XML, kvitteringer) | Ingen tap | Objektlager med versjonering og uforanderlighet, replikert til DR-region |
| Nøkler (KMS/HSM) | Kritisk | Soft-delete og purge-protection, backup av nøkkelmateriale der det støttes. Testes i DR-øvelse. |
| Gjenoppretting av én tenant | Ønsket | Daglig logisk eksport per tenant (kryptert), eventuelt avspilling av hendelseslogg. Uforanderlig design (ingen harde slettinger) reduserer behovet. |
| Test | – | Automatisert gjenopprettingstest månedlig, full DR-øvelse årlig (evidens for ISAE) |

### 8.5 Supportmodell

| Nivå | Hvem | Innhold |
|---|---|---|
| L0 | Selvbetjening og AI | Hjelpesenter, AI-Q&A med kilder, forklaringer i produktet |
| L1 | Kundesenter (norsk, lønnsfaglig grunnkompetanse) | Bruk, konfigurasjon, enkle feil |
| L2 | Lønnsfaglige spesialister | Beregningsspørsmål, a-melding-avvik, migrering |
| L3 | Utvikling (vaktordning) | Feil i kode og regel, hendelser |
| Partnerkanal | Egen kø og prioritet for byråer, partnersertifisering (kurs) | Byråer løser mye selv og gir høyere tilfredshet |

- **SLA per prioritet:** P1 (lønn kan ikke kjøres eller utbetales) har responstid ≤ 30 min i kritiske vinduer.
- **Supporttilgang** til kundedata kun via break-glass med samtykke (kap. 3.3).
- **Måltall:** henvendelser per 100 lønnsslipper, tid til løsning, andel løst på L0/L1.

---

## 9. Teknologivalg

### 9.1 Rammebetingelser

Lite team (5–7 utviklere), 12–18 måneder til første kunde, regulert domene, levetid på 10+ år, korrekthet viktigere enn utviklingshastighet, revisjonskrav og norsk rekrutteringsmarked.

### 9.2 Språk for backend og beregningsmotor

| Kriterium | **Kotlin/JVM** | **C#/.NET** | TypeScript/Node | Go |
|---|---|---|---|---|
| Desimal for penger | `BigDecimal` (moden, eksplisitt skala og avrunding) | `System.Decimal` (innebygd 128-bit, svært godt egnet) | Bibliotek (decimal.js/big.js). `number` er en felle, så strenge lint-regler trengs. | Ingen innebygd (shopspring/decimal) |
| Domenemodellering | Sealed classes, data classes, null-sikkerhet: utmerket | Records, pattern matching: utmerket | Diskriminerte unioner: god, men typene håndheves ikke ved kjøring | Begrenset (ingen sum-typer) |
| Ytelse | Svært god | Svært god | God nok (enkelttrådet CPU, worker threads) | Svært god |
| XML/XSD (a-melding, ISO 20022) | Moden (JAXB, Xerces) | Moden (System.Xml) | Svakere (libxml-bindinger) | Middels |
| Egenskapsbasert testing | jqwik, Kotest | FsCheck, CsCheck | fast-check | gopter/rapid |
| Norsk rekruttering | Stor (NAV, Finn, fintech) | Stor (Visma, PowerOffice, Uni Micro, mange fintech) | Svært stor | Mindre |
| Norsk referanse | NAVs beregningssystemer i Kotlin (f.eks. spleis) | Mange regnskapssystemer | – | – |

**Anbefaling:**
- **Kotlin på JVM (LTS)** for backend og motor.
- **C#/.NET er likeverdig** og bør velges hvis kjerneteamet er .NET-sterkt. Velg det språket de to–tre første seniorutviklerne er best i, og **ikke bland** backend-språk.
- **TypeScript** (React) i frontend.
- **Full TypeScript** er akseptabelt *bare* hvis teamet er rent TS. Da trengs en egen `Money`-type, et lint-forbud mot `number` for beløp og ekstra fokus på XML-validering.
- **Go** frarådes for regeltung domenekode.

**Arkitekturstil:**
- **Modulær monolitt** i ett repo med heksagonal arkitektur. Motoren er en egen modul uten DB-avhengighet, så den kan kjøres fra CLI (gylne filer), i arbeidsnoder og i simulering.
- Tre deploybare enheter:
  1. web/API
  2. arbeidsnoder (beregning, PDF, import)
  3. **myndighets- og betalingsgateway** (isolerte hemmeligheter og nettverk)

### 9.3 Database

- **PostgreSQL 17/18 administrert:** Azure Database for PostgreSQL Flexible Server (sone-redundant HA) eller AWS RDS/Aurora.
  - PG18 gir temporale nøkler for gyldighetstid.
  - JSONB brukes for kjøringssnapshot.
  - Partisjonering per periode.
- Ingen separat hendelseslager-database, Kafka eller Redis i v1. Postgres håndterer kø, outbox og cache-behov i den skalaen det er snakk om.
- Analyse og BI senere via CDC (Debezium) til et separat analyselager **med pseudonymisering**.

### 9.4 Hosting

| Alternativ | Fordeler | Ulemper | Vurdering |
|---|---|---|---|
| **Azure Norway East** | Data i Norge, Entra ID-økosystem (byråer og kunder bruker M365), Key Vault Managed HSM, Container Apps/AKS, Service Bus, PG Flexible | Norway West er reservert, så DR må gå til Sweden Central (EU) | **Anbefalt** |
| AWS eu-north-1 | Modent, bredt, Bedrock (Claude) i EU | Ikke Norge, selv om EU/EØS er tilstrekkelig juridisk | Godt alternativ |
| GCP | Godt produkt | Norge-region ikke verifisert, mindre utbredt | Nei, med mindre teamet kan det |
| Supabase + Vercel | Rask prototyping og god utvikleropplevelse | Begrenset kontroll over nøkler, nettverk, logging og dataflyt for ISAE/ISO. Vercels funksjons- og logglokasjon må styres. Leverandørbinding i auth og RLS-mønstre. | **Ikke for lønnskjernen.** Greit for markedsside og dokumentasjon. |
| Egen drift / norsk sky | Suverenitet | Driftsbyrde | Nei for lite team |

**AI på Azure:** Claude i Microsoft Foundry har i dag bare US Data Zone som regionalternativ ([Claude docs](https://platform.claude.com/docs/en/manage-claude/data-residency)). For EU-residens brukes enten Azure OpenAI EU Data Zone, eller et kryss-sky-kall til AWS Bedrock (Claude) i EU-region. AI-gatewayen (kap. 5.3) gjør valget byttbart.

### 9.5 Hendelsesbuss, kø og arbeidsflyt

- **v1:** Transaksjonell outbox i Postgres og Postgres-basert jobbkø: JobRunr eller db-scheduler (JVM), Wolverine eller Hangfire (.NET), pg-boss eller Graphile Worker (Node). Tilstandsmaskiner i domenet for langvarige prosesser (kjøring → betaling → a-melding → tilbakemelding).
- **v2 (ved behov):** Azure Service Bus eller AWS SQS/SNS for integrasjoner og webhooks med høyt volum.
- **Kafka:** Ikke før det finnes et konkret behov for strømming.
- **Temporal.io:** Vurderes hvis antall langvarige arbeidsflyter eksploderer. Det gir mer infrastruktur, så vent.

### 9.6 Øvrige byggeklosser

| Behov | Forslag |
|---|---|
| Identitet | Administrert IdP med EU-datalagring (Entra External ID, Auth0 EU, Zitadel) + BankID-megler. Ikke bygg egen innlogging. |
| PDF | HTML→PDF/A via headless Chromium (Gotenberg), eller Typst for ytelse |
| Observerbarhet | OpenTelemetry → Azure Monitor/Grafana (EU), Sentry (EU-region) med PII-skrubbing |
| Funksjonsbrytere | Unleash (selvhostet eller EU) |
| CI/CD og infrastruktur som kode | GitHub Actions, Terraform/OpenTofu eller Bicep, miljøer: dev → test (TT02) → staging (produksjonslik, syntetiske data) → produksjon |
| Hemmeligheter | Key Vault/KMS, administrerte identiteter, ingen hemmeligheter i CI-logger |
| Compliance-bevis | Vanta/Drata eller tilsvarende, koblet til sky, Git og HR |

### 9.7 Team og tidslinje (12–18 mnd)

| Fase | Periode (fra nov. 2026) | Leveranser |
|---|---|---|
| Fundament | Mnd 0–3 | Tenant/IAM, bitemporal datamodell, motor-skjelett og rammeverk for gylne filer, Maskinporten og systembruker i TT02, ISMS-light |
| Kjerne-lønn | Mnd 3–9 | Månedslønn og timelønn, fravær og refusjonsgrunnlag, feriepenger, OTP, AGA, forskuddstrekk, a-melding, skattekort, pain.001, regnskapseksport, slipp og portal |
| Byrå og migrering | Mnd 9–12 | Byråkonsoll, migreringskit (Tripletex, PowerOffice, Visma.net, a-melding-XML, Excel), release-diff, ISAE 3402 type 1-klarhet, pentest |
| Pilot | Mnd 11–14 (okt.–des. 2027) | Parallellkjøring med 3–5 piloter (helst via 1–2 byråer) |
| Første produksjon | **Januar 2028** | Oppstart ved årsskiftet, oppfølging, type 2-periode starter |
| Bredde | Mnd 14–18 | Tariffmaler, flere integrasjoner, AI-funksjoner (avvik, slippforklaring først) |

**Bemanning:**
- 5–7 utviklere (inkl. 1 med plattform- og sikkerhetsprofil)
- **1–2 fulltids lønnseksperter fra dag 1**
- produktleder
- 0,5 compliance/sikkerhet (kan være innleid de første 12 mnd)
- supportoppbygging fra mnd 10

---

## 10. Arkitekturbeslutninger (ADR-stil)

| ADR | Beslutning | Alternativer | Anbefaling | Åpent |
|---|---|---|---|---|
| **ADR-01** | Arkitekturstil | Mikrotjenester · modulær monolitt · serverløs | **Modulær monolitt** med tre deploybare enheter (web/API, arbeidsnoder, gateway). Modulgrenser håndheves med arkitekturtester. | Når første modul skal skilles ut (kandidat: gateway og PDF) |
| **ADR-02** | Backend- og motorspråk | Kotlin/JVM · C#/.NET · TypeScript · Go | **Kotlin/JVM**, eller C#/.NET hvis teamet er .NET-sterkt. TS i frontend. | Avgjøres av kompetansen til de første ansettelsene |
| **ADR-03** | Data- og tidsmodell | Full event sourcing · bitemporale tabeller · temporal DB (XTDB) · kun revisjonslogg | **Bitemporale tabeller i Postgres** + bare-tilføyende domenehendelser/outbox + uforanderlige kjøringssnapshot | Hvilke entiteter som *ikke* skal være bitemporale. Ytelse på «som kjent ved»-spørringer (benchmark mnd 2). |
| **ADR-04** | Regelmotor | Kode · DSL · DMN/Drools · kjøpt API | **Kode for lovpålagt logikk + parametre som data + typesikkert uttrykksspråk (CEL o.l.) for kundens lønnsarter og tariffer** | Valg av uttrykksspråk. Hvor mye tariff-logikk kunden selv skal kunne definere. |
| **ADR-05** | Regelversjonering og reproduserbarhet | Én versjon per år · per virkningsdato · per kjøring | **Signerte regelpakker med virkningsintervall.** Oppslag per regel og relevant dato. Kjøring lagrer `input_hash` + `regelpakke_id` + `motor_versjon`. | Regel-for-regel-tabell over hvilken dato som styrer (utbetaling, opptjening, arbeid), med beregningsanalytikerne |
| **ADR-06** | Penger og avrunding | Flyttall · heltall øre · Decimal | **Decimal med fast skala i motoren, heltall øre eller `numeric(14,2)` i lagring.** Avrundingspolicy er del av regelpakken. Største-rest-fordeling. | Endelige avrundingsregler for prosenttrekk og AGA bekreftes mot regelverk |
| **ADR-07** | Lønnskjøringens livssyklus | Muterbar · uforanderlig + korreksjon | **Uforanderlig etter godkjenning.** Korreksjonskjøringer og egne versjoner av a-melding-aggregatet per opplysningspliktig og måned. | UX for korreksjoner i byråskala (masseretting etter regelfeil) |
| **ADR-08** | Tenant-isolasjon | RLS i delt skjema · skjema per tenant · DB per tenant · hybrid | **Delt skjema + RLS (FORCE) + celler.** Dedikert celle for store kunder. | Celle-størrelse og ruting. Prising av dedikert celle. |
| **ADR-09** | Tilgangsmodell | RBAC · ABAC · ReBAC; egenutviklet · OpenFGA · Cedar · OPA | **RBAC + relasjoner (byrå→klient→avdeling) + ABAC for sensitivitet**, i egen policymodul med tester. To personers kontroll og step-up. | Overgang til OpenFGA/Cedar når modellen vokser. Detaljer for leder-rollen. |
| **ADR-10** | Kryptering og nøkler | Kun disk-kryptering · feltkryptering · tokenisering | **Konvoluttkryptering på feltnivå per tenant (DEK) med KEK i HSM, blind indeks for fnr, crypto-shredding** | BYOK for enterprise. Ytelseseffekt på importer. |
| **ADR-11** | Hosting og region | Azure Norway East · AWS Stockholm · GCP · Supabase/Vercel | **Azure Norway East**, DR i Sweden Central (EU) | AWS hvis teamet har sterkere AWS-kompetanse. Bekreft tjenestetilgjengelighet i Norway East (PG Flexible HA, Managed HSM). |
| **ADR-12** | Integrasjoner og asynkronitet | Synkrone kall · outbox + Postgres-kø · meldingsbuss · Kafka · Temporal | **Outbox + Postgres-kø + tilstandsmaskiner. Isolert myndighets- og betalingsgateway.** Én systembruker per opplysningspliktig. | Bankintegrasjon: direkte host-to-host vs integrasjonspartner vs via regnskapssystem |
| **ADR-13** | Identitet og autentisering | Egenutviklet · Keycloak · administrert IdP | **Administrert IdP (EU) + BankID-megler + passkeys + SSO/SCIM for enterprise**, step-up for sensitive handlinger | Løsning for ansatte uten BankID. Valg av megler (pris per innlogging). |
| **ADR-14** | AI-arkitektur | Direkte leverandør-API · AI-gateway · ingen AI | **Leverandøruavhengig AI-gateway, EU-region (Bedrock/Google Cloud EU eller Azure OpenAI EU), pseudonymisering, null lagring, agentrolle uten godkjennings- og betalingsrettigheter**, forankret i forklaringsspor | Leverandørvalg. Tolkning av AI-forordningen for avviksdeteksjon. Norsk KI-lov. |
| **ADR-15** | Migreringsstrategi | Manuell registrering · rapport-import · API-adaptere · a-melding-basert | **Migreringskit:** a-melding-XML + Skatteetatens avstemmingsdata som fasit, API-adaptere (Tripletex, PowerOffice Go, Visma.net), Excel-maler med AI-mapping, obligatorisk parallellkjøring med «lik på øret» | Tilgang til Visma.net- og SD Worx-data (avtaler). Prising av migrering. |
| **ADR-16** | Compliance-veikart | ISO 27001 først · ISAE 3402 først · SOC 2 | **ISAE 3402 type 1 ved første kunde → type 2-periode fra produksjonsstart → ISO 27001 innen 18–24 mnd.** SOC 2 kun ved etterspørsel. | Revisorvalg og om ISAE 3000 skal kombineres. Budsjett. |

---

## 11. Avhengigheter og åpne spørsmål til de andre analysene

1. **Beregningsregler:** Tabell over hvilken dato som styrer regelvalget (utbetaling, opptjening eller arbeidsperiode) per regel, endelige avrundingsregler og trekkprioritet ved flere trekkpålegg. Disse er input til ADR-05 og ADR-06.
2. **Myndighetskrav:**
   - endepunkter og tilgangspakker for a-melding, skattekort og avstemming på Skatteetatens GitHub-dokumentasjon
   - NAV-API-er for inntektsmelding og refusjon
   - rutiner for erstatningsmelding
   - eventuelle krav om sertifisering eller godkjenning av sluttbrukersystem
3. **Marked:** Hvilke regnskapssystemer og tidssystemer som dominerer hos målbyråene (prioritet for integrasjoner og migreringsadaptere), og om «data i Norge» gir betalingsvilje.
4. **Juridisk:** Hjemmel for oppbevaring av lønnsslipper, DPA-modell for byrå som videreselger, status for EU–US DPF, norsk KI-lov og NIS2-gjennomføring.

---

## Kilder

- Skatteetaten – for leverandører av sluttbrukersystemer (Altinn 3, Maskinporten, systembruker, tilgangspakker, TT02): https://www.skatteetaten.no/samarbeidspartnere/reetablering-altinn/systemleverandor/
- Skatteetaten – skattekort til arbeidsgiver, endret bruksmønster: https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/endret-bruksmonster-for-henting-av-skattekort/
- Skatteetaten – frist Altinn 3 forlenges: https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/frist-altinn3-forlenges/
- Skatteetaten – a-meldingen for sluttbrukersystemer: https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/a-meldingen-sbs/
- Skatteetaten – juridisk vurdering av systembruker: https://www.skatteetaten.no/samarbeidspartnere/reetablering-altinn/skatteetatens-juridiske-vurdering-av-systembruker/
- Skatteetaten – bytte lønnssystem: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/arbeidsforholdet/spesielle-forhold/bytte-lonnssystem
- Skatteetaten – Tenor testdata: https://www.skatteetaten.no/skjema/testdata/
- Skatteetaten – testinnsending (kun syntetiske data): https://www.skatteetaten.no/no/Bedrift-og-organisasjon/rapportering-og-bransjer/tredjepartsopplysninger/Testinnsending-xml/
- Skatteetaten – ingen tvangsmulkt i overgang: https://www.skatteetaten.no/nn/bedrift-og-organisasjon/arbeidsgiver/a-meldinga/siste-fra-a-ordningen/ingen-tvangsmulkt-for-a-meldingen-i-mai-juni-og-juli/
- Digdir/Altinn – systemautentisering for systemleverandører: https://docs.altinn.studio/authentication/guides/systemauthentication-for-systemproviders/
- NAV – ekstern datautveksling (Maskinporten, systembruker): https://www.nav.no/samarbeidspartner/ekstern-datautveksling
- Martin Fowler – Bitemporal History: https://martinfowler.com/articles/bitemporal-history.html
- Martin Fowler – Temporal Patterns: https://martinfowler.com/eaaDev/timeNarrative.html
- PostgreSQL – temporal constraints (feature matrix): https://www.postgresql.org/about/featurematrix/detail/temporal-constraints
- Neon – PostgreSQL 18 temporal constraints: https://neon.com/postgresql/postgresql-18/temporal-constraints
- NAV – helse-spleis (Kotlin, sykepengeberegning): https://github.com/navikt/helse-spleis
- Postgres RLS multi-tenant praksis: https://stackharbor.com/en/knowledge-base/pg-row-level-security-multi-tenant/
- NSM – Grunnprinsipper for IKT-sikkerhet v2.1: https://nsm.no/getfile.php/1313975-1717589722/NSM/Filer/Dokumenter/Veiledere/NSMs%20Grunnprinsipper%20for%20IKT-sikkerhet%20v2.1.pdf
- KPMG Norge – attestasjonstjenester (ISAE 3402/SOC 2): https://kpmg.com/no/nb/tjenester/revisjon/attestation-services.html
- DEKRA – ISAE 3402 type 1 vs 2: https://www.dekra.nl/en/blog-isae-3402-type-1-and-2/
- Nmbrs – ISAE 3402 (lønnsleverandør): https://nmbrs.com/isae-3402
- Drata – SOC 2 audit cost: https://drata.com/blog/soc-2-audit-cost
- BD Emerson – SOC 2 cost: https://www.bdemerson.com/article/soc-2-cost
- Deloitte – digitalsikkerhetsloven fra oktober 2025: https://www.deloitte.com/no/no/services/legal/perspectives/digital-sikkerhet-i-Norge-nye-krav-for-kritiske-virksomheter-fra-oktober-2025.html
- Legiscope – NIS2 i Norge: https://www.legiscope.com/blog/nis2-norge-gjennomforing.html
- Personopplysningsloven 2018 (lovvedtak, § 12): https://stortinget.no/no/Saker-og-publikasjoner/Vedtak/Beslutninger/Lovvedtak/2017-2018/vedtak-201718-054/
- Oppbevaringstid bokføring (5 år): https://stortinget.no/no/Saker-og-publikasjoner/Publikasjoner/Innstillinger/Stortinget/2013-2014/inns-201314-004/29/ og https://www.revregn.no/asset/pdf/2020/05/2020-05_48.pdf
- Claude – data residency (inference geo us/global, Bedrock/Google Cloud regioner): https://platform.claude.com/docs/en/manage-claude/data-residency
- EU AI Act vedlegg III: https://artificialintelligenceact.eu/annex/3/
- Gibson Dunn – AI Act Omnibus-enighet (utsatt høyrisiko): https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
- NHH – lønnsåpenhetsdirektivet: https://www.nhh.no/en/nhh-bulletin/article-archive/2026/june/pay-transparency-directive-eu-countries-miss-the-deadline/
- Azure Norway East tilgjengelighetssoner: https://datacenterdynamics.com/en/news/microsoft-launches-availability-zones-in-norway-east-azure-cloud-region
- AWS Stockholm: https://www.datacenterknowledge.com/hyperscalers/sweden-gets-its-own-aws-data-centers-amazon-s-first-in-the-nordics
- Google Cloud Norge-region (kunngjøring 2022): https://www.googlecloudpresscorner.com/2022-10-11-Google-Cloud-Announces-Plans-for-First-Cloud-Region-in-Norway-to-Accelerate-Sustainable-Digital-Transformation
- Tripletex API-guide: https://www.apideck.com/blog/how-to-integrate-with-the-tripletex-api
- Huldt & Lillevik eksportformat: https://docs.moment.team/help/moment-by-topic/integrations/file-exports/wage-system/huldt-and-lillevik-lonn
- Visma kjøp av Huldt & Lillevik: https://www.cinven.com/news-insights/visma-strengthens-its-focus-on-hrm-solutions
- Uni Micro – ikke øreavrunding ved elektronisk betaling: https://unimicro.no/blogg/du-skal-ikke-oereavrunde-ved-elektronisk-betaling
