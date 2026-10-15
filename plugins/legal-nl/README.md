# legal-nl

Nederlandse juridische templates en skills voor ondernemers met een BV.

```bash
/plugin install legal-nl --marketplace pantalytics/this-should-be-illegal
```

In de Claude-app: **Customize** > **Add marketplace** > **Add from a repository** >
`pantalytics/this-should-be-illegal`, en installeer daarna **legal-nl**. Zie de
[README](../../README.md#add-it-to-claude) voor wat waar werkt.

## Templates

| Template | Gebruik |
| -------- | ------- |
| [Aandeelhoudersovereenkomst](templates/bv/aandeelhoudersovereenkomst.md) | Afspraken tussen oprichters: bestuur, overdracht, vesting, leaver |
| [Managementovereenkomst](templates/bv/managementovereenkomst.md) | Bestuurder werkt via eigen holding voor de werkmaatschappij |
| [Aandeelhoudersbesluit buiten vergadering](templates/bv/aandeelhoudersbesluit-buiten-vergadering.md) | Elk AVA-besluit zonder vergadering (art. 2:238 BW) |
| [Rekening-courantovereenkomst](templates/bv/rekening-courantovereenkomst.md) | Lopend onderling geldverkeer tussen BV en DGA of holding |
| [Geldleningsovereenkomst](templates/bv/geldleningsovereenkomst.md) | Zakelijke lening van een vast bedrag aan een BV |

Alle templates zijn `draft`: nog niet beoordeeld door een advocaat.

## Skills

`draft-document`, `review-document`, `check-counterparty`, `lookup-law`.

De plugin start twee MCP-servers via `npx` (Node.js 20+): `rechtspraak` en `eurlex`. Geen
account of key nodig. Nederlandse wetteksten komen rechtstreeks uit
[wetgeving-nl](https://github.com/Apolloccrypt/wetgeving-nl).
