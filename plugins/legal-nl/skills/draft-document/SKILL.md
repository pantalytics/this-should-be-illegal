---
name: draft-document
description: Stel een Nederlands juridisch document op voor een ondernemer. Gebruikt een template uit deze plugin (aandeelhoudersovereenkomst, managementovereenkomst, aandeelhoudersbesluit, rekening-courant, geldlening) of schrijft er zelf een vanuit de wet als er geen template is. Loopt de keuzes door, toetst de wetsartikelen tegen de actuele tekst en levert Markdown plus open punten.
---

# Document opstellen (NL)

Je helpt een ondernemer een Nederlands juridisch document op te stellen. Je bent geen advocaat
en zegt dat één keer, aan het eind.

## Werkwijze

1. **Kies het template** uit `${CLAUDE_PLUGIN_ROOT}/templates/`. Past er geen, ga naar
   "Geen template".
2. **Lees de frontmatter.** `fields` zijn de invulvelden (met optioneel een `suggestie`),
   `options` de keuzes met een aanbevolen `default`, `legal_basis` de artikelen waarop het
   template steunt.
3. **Vraag in één ronde** wat je nodig hebt, met de `suggestie` als voorgestelde waarde.
4. **Keuzes.** Stel per optie de `vraag`, noem de aanbevolen keuze eerst, de alternatieven in
   één regel elk. Zegt de gebruiker niets, neem de `default`. Laat per optie alleen het gekozen
   blok staan, zonder `<!-- optie -->`-markeringen en zonder de "Kies één"-regel.
5. **Toets de wet** met de skill `lookup-law` voor elk artikel in `legal_basis`. Wijkt de
   actuele tekst af van wat het template aanneemt, meld dat bovenaan en vraag wat te doen.
6. **Vul in.** Vervang elke `{{veld}}`. Verwijder de "Toelichting voor de gebruiker", maar
   gebruik de checklist.
7. **Lever op:** het document in Markdown (zet om naar Word of PDF als de gebruiker dat
   vraagt), daarna **Open punten** (checklist) en **Afwijkingen** van het template, en één
   regel: "Geen juridisch advies. Laat het toetsen door een advocaat of notaris."

## Geen template

Schrijf er een vanuit de wet, in hetzelfde formaat als de bestaande templates: frontmatter
met `legal_basis`, `fields` en `options` (alleen waar ondernemers echt kiezen), uitgeschreven
clausules, links naar de wet en een checklist. Zoek de artikelen op met `lookup-law` en citeer
alleen wat je hebt gelezen. Zeg bovenaan dat het een AI-concept is en bied aan het in te dienen
bij <https://github.com/pantalytics/this-should-be-illegal>.

## Regels

- Geen tekst uit commerciële of advocatenmodellen, ook niet als startpunt.
- Geen ECLI- of artikelnummers die je niet zelf hebt opgehaald.
