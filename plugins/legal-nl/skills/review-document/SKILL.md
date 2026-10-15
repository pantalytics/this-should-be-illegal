---
name: review-document
description: Beoordeel een bestaand Nederlands contract of vennootschapsdocument (SHA, managementovereenkomst, AVA-besluit, NDA, opdrachtovereenkomst) op juridische risico's onder Nederlands recht. Gebruik dit wanneer een ondernemer een concept van de andere partij of een advocaat wil laten checken. Controleert wetsartikelen, relevante rechtspraak en de tegenpartij, alleen met open bronnen.
---

# Document beoordelen (NL)

Je beoordeelt een document vanuit het belang van de gebruiker. Conclusie eerst.

## Werkwijze

1. **Bepaal type en partij.** Wat voor document is het, en welke partij is de gebruiker?
   Vraag dit als het niet blijkt uit het document.
2. **Vergelijk met het template** in `${CLAUDE_PLUGIN_ROOT}/templates/` als er een passend
   template is. Ontbrekende clausules zijn bevindingen.
3. **Echte checks**, alleen met open bronnen:
   - **Wet** (skill `lookup-law`): lees elk artikel dat het document noemt of nodig heeft.
     Klopt de verwijzing? Is het artikel nog geldend? Wordt dwingend recht opzij gezet?
   - **Rechtspraak** (MCP-server `rechtspraak`): zoek bij elke zware bevinding (boetebeding,
     non-compete, bad-leaverprijs, aansprakelijkheidsbeperking) één tot drie recente
     uitspraken. Noem de ECLI en wat de rechter besliste. Geen ECLI gevonden, dan zeg je dat.
   - **Tegenpartij**: gebruik de skill `check-counterparty`.
4. **Rapporteer** als tabel, zwaarste eerst:

   | Ernst | Clausule | Probleem | Bron | Voorstel |
   | ----- | -------- | -------- | ---- | -------- |

   Ernst is `hoog` (ongeldig, nietig of groot financieel risico), `midden` (onredelijk of
   onduidelijk) of `laag` (redactioneel). Bron is een artikel of ECLI, nooit "algemeen".
5. **Sluit af** met welke checks niet konden draaien (bron onbereikbaar, MCP ontbrak) en één regel
   dat dit geen juridisch advies is.

## Regels

- Verzin geen ECLI-nummers of artikelnummers. Alleen wat een tool teruggeeft of wat letterlijk
  in het document staat.
- Bij twijfel over geldigheid: noem het een risico, geen zekerheid.
- Toon voorgestelde tekst als concrete vervangende clausule, niet als advies in proza.
