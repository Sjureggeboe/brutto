/loop Nattarbeid for lønnssystemet Brutto. Kjør til kl. 08:00 torsdag 29.10.2026.

KONTEKST: Mappen er analyse/ i repoet (finn full sti med `git rev-parse --show-toplevel`). Stiene under er relative til analyse/.
- Les i hver runde: natt/backlog.md, natt/logg.md og natt/reai-opprydding.md.
- Bakgrunn ved behov: research/ (A–G, R2-*, R3-*, R5-kvalitet, S-avklaringer-fra-sally, R0-sdworx-meny) og plan/omradekart.md.
- Fase 1 er ansattoversikt, A07-avstemming mot regnskapet via Maskinporten og systembruker, og enkle kontroller og grafer. Assistenten kommer senere.
- Godkjenningsflyt per kunde og utbetaling via open banking designes nå, men bygges senere.
- Teamet er Sjur, Peter og Sander. Brutto bygges i Rust.
- Lønn først, HR senere. Utlegg bare via integrasjoner.

HVER RUNDE:
1. Tid. Fra kl. 07:30 starter du ingen nye undersøkelser. Vent på agenter som allerede jobber, rydd i ReAi og skriv natt/morgen.md. Morgensammendraget skal ha de 5–10 viktigste funnene, anbefalte endringer og spørsmål til Sjur, Peter og Sander. Publiser (punkt 4) og stopp loopen.
2. Ta inn ferdige funn. Gjelder punkter med status «pågår» der natt/funn/<id>.md finnes:
   - Les bare «Kort svar», «Konsekvens for Brutto» og «Nye spørsmål».
   - Sett status «ferdig».
   - Legg nye undersøkelsespunkter inn i backloggen med nye id-er og riktig prioritet.
   - Skriv forslag til endringer i kartleggingen og nye spørsmål til Peter og Sander i natt/forslag.md, med id på punktet. Ikke endre build/data/*.json.
   - Skriv én linje per hendelse i natt/logg.md.
3. Start neste bolk. Det skal alltid være 3 agenter i gang til backloggen er tom.
   - Sett status «pågår» og start general-purpose-agenter i bakgrunnen på de øverste åpne punktene etter prioritet.
   - Hver agent får punktets detaljtekst fra backloggen, stien til research/, filformatet og reglene under.
   - Agenten skriver natt/funn/<id>.md, sletter egne midlertidige filer og svarer med maks 8 linjer.
4. Publiser. Kjør `python3 -I natt/oppdater.py` (full sti). Publiser deretter build/brutto.html (full sti) med Artifact-verktøyet til url https://claude.ai/artifact/ChbZpocS4VZCfMrVCU9M1d, uten capabilities og med en kort label.
5. Neste runde. Kall ScheduleWakeup med 1800 sekunder som reserve, siden agentene vekker deg når de er ferdige.
   - Er backloggen tom og ingen agenter jobber, lager du opptil 5 nye, relevante punkter ut fra funnene. Maks 40 punkter totalt.
   - Er det ikke mer som er verdt å undersøke, skriver du morgensammendraget og stopper.

FILFORMAT FOR FUNN (natt/funn/<id>.md):
- Frontmatter mellom to linjer med `---`, med feltene id, tittel, fase (F1, MVP eller Senere), dato og sikkerhet (Høy, Middels eller Lav).
- Deretter disse overskriftene:
  - «## Kort svar» med 3–6 setninger som svarer direkte på spørsmålet.
  - «## Funn» med detaljene, tabeller der de hjelper.
  - «## Konsekvens for Brutto», delt i fase 1, MVP og senere, og med F-id-er og D-id-er fra kartleggingen der det passer.
  - «## Nye spørsmål», både til backloggen og til Peter og Sander.
  - «## Kilder» med URL-er.
- Skriv på norsk bokmål, med korte og direkte setninger og primærkilder.
- Merk alt som er usikkert med [verifiseres].
- Ingen personopplysninger.

REGLER:
- Nett: bare lesing. Ikke send e-post, meldinger eller skjema. Ikke opprett kontoer, og ikke logg inn noe sted.
- ReAi: bare tenant 2915 (Vinderen Industrier AS).
  - Lesing er fritt.
  - Skriving er tillatt for å se hvordan flyten virker, helst som utkast. Før kallet føres objektet i natt/reai-opprydding.md. Det slettes i samme runde og krysses av.
  - Lønnsbilag kan posteres (gründeren har gitt tillatelse 28.10.2026), for eksempel for å se kontering, ansattreskontro og A07-avstemming. Bokførte lønnsbilag skal slettes, eller reverseres hvis sletting ikke går. Det gjøres i samme runde, og senest før noen tester innsending av a-melding. Noter i opprydningsfilen om bilaget ble slettet eller reversert.
  - Det som ikke kan slettes, skal ikke opprettes.
  - Aldri send noe ut av ReAi: ingen submit, send, sendEhf, sendEmail eller sign, ingen godkjenning eller fullføring av lønnsutbetaling, ingen registerPayment eller createPayment, ingen aMeldingApi_submit eller vatReturnApi_submit, ingen innsending til Altinn, Skatteetaten, NAV eller bank, og ingen meldinger til kunder eller ansatte.
  - Ingen personopplysninger i funnene, bare struktur, felt, flyt og automatisering.
- Tripletex og andre koblede systemer: bare lesing og ingen personopplysninger.
- Ikke publiser andre artefakter, og ikke endre svarene i databasen til Fase 1-siden.
- Hold hovedtråden liten. Les bare de korte delene av funnene, og la agentene gjøre det tunge arbeidet.
