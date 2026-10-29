# Opprydding i ReAi (Vinderen Industrier AS, tenant 2915)

Alt som opprettes eller endres i ReAi under nattarbeidet, føres her før kallet gjøres, og krysses av når det er slettet eller tilbakestilt.
Bare tenant 2915. Ingen annen tenant røres.

| Tid | Runde | Objekt | Id | Opprettet med | Slettet med | Status |
|---|---|---|---|---|---|---|
| 2026-10-29 00:25 | 4 | Lønnsutkast (salary payment, under_process), periode 2026-10, N21 | 2011 (nr 2026-1) | salaryPaymentApi_create | salaryPaymentApi_delete (outcome: deleted). Kontrollert: ingen lønnsutbetalinger, ingen SALARY-bilag og ingen a-melding for 2026-10 | Slettet |
| 2026-10-29 00:25 | 4 | Trekklinje POST_TAX_DEDUCTION mot 2610 i lønnsutkast 2011 (test av trekkpålegg), N21 | 4629 | addWageSpec | deleteWageSpec (deretter hele utkastet slettet) | Slettet |

Merknad runde 4 (N21): Lønnsutkastet fikk kjøringsnummer 2026-1 da det ble opprettet. Neste ekte lønnskjøring kan derfor få nummer 2026-2 [verifiseres]. Kjøringsnummeret er ikke et bilagsnummer, og ingen bilag, a-melding eller betaling ble laget.

Merknad runde 36 (N33), 2026-10-29: Ingen objekter opprettet, endret eller slettet i ReAi. Bare lesing i tenant 2915: kontoplan (`/api/chart-of-accounts/accounts`), posteringer (`/api/postings`), MVA-koder (`/api/vat-codes`) og OpenAPI (`/openapi/public`). Ingenting å rydde.
