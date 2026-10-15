# legal-nl

Nederlandse juridische templates en skills voor ondernemers met een BV.

```bash
/plugin install legal-nl --marketplace pantalytics/this-should-be-illegal
```

## Templates

| Template | Gebruik | Status |
| -------- | ------- | ------ |
| [Aandeelhoudersovereenkomst](templates/bv/aandeelhoudersovereenkomst.md) | Afspraken tussen oprichters: bestuur, overdracht, vesting, leaver | draft |
| [Managementovereenkomst](templates/bv/managementovereenkomst.md) | Bestuurder werkt via eigen holding voor de werkmaatschappij | draft |
| [Aandeelhoudersbesluit buiten vergadering](templates/bv/aandeelhoudersbesluit-buiten-vergadering.md) | Elk AVA-besluit zonder vergadering (art. 2:238 BW) | draft |

`draft` betekent: nog niet beoordeeld door een advocaat.

## Skills

| Skill | Doet |
| ----- | ---- |
| `draft-document` | Kiest een template, vult KVK-gegevens in, toetst de wetsartikelen live, levert document plus open punten |
| `review-document` | Beoordeelt een concept: wet, rechtspraak (ECLI) en tegenpartij, als tabel met bronnen |
| `check-counterparty` | Controleert een tegenpartij in het handelsregister en geeft OK / Navragen / Niet tekenen |

## MCP-servers

| Server | Hoe | Nodig |
| ------ | --- | ----- |
| `dutch-law` | Gehoste gateway van Ansvar (HTTP) | Gratis account, OAuth bij eerste gebruik |
| `rechtspraak` | `npx rechtspraak-mcp` | Node.js 20+ |
| `kvk` | `npx kvk-mcp` | Node.js 20+ en `KVK_API_KEY` in je omgeving |

Ontbreekt een server of key, dan werken de skills door en melden ze welke check niet kon
draaien. De lokale variant van dutch-law-mcp (`npx @ansvar/dutch-law-mcp`) faalde in oktober
2026 op het downloaden van de database; daarom de gateway.
