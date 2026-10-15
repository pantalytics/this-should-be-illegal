# this should be illegal

Open legal templates and AI skills for entrepreneurs. Plain Markdown, written from the
statute, checked against the current law text. Netherlands first, then Europe.

> **Not legal advice.** Templates are drafts until a lawyer has reviewed them. See
> [DISCLAIMER.md](DISCLAIMER.md).

## Templates

| | Template | Status |
| - | -------- | ------ |
| 🇳🇱 | [Aandeelhoudersovereenkomst](plugins/legal-nl/templates/bv/aandeelhoudersovereenkomst.md) | draft |
| 🇳🇱 | [Managementovereenkomst](plugins/legal-nl/templates/bv/managementovereenkomst.md) | draft |
| 🇳🇱 | [Aandeelhoudersbesluit buiten vergadering](plugins/legal-nl/templates/bv/aandeelhoudersbesluit-buiten-vergadering.md) | draft |
| 🇳🇱 | [Rekening-courantovereenkomst](plugins/legal-nl/templates/bv/rekening-courantovereenkomst.md) | draft |
| 🇳🇱 | [Geldleningsovereenkomst](plugins/legal-nl/templates/bv/geldleningsovereenkomst.md) | draft |

Full clause text, suggested values for every open field, common options written out with
the recommended one marked, links to the law, and a checklist. Need Word? Ask your AI.

## Skills

| Skill | Does |
| ----- | ---- |
| `draft-document` | Fills a template with you, walks through the options; no template, it drafts one from the law |
| `review-document` | Reviews a contract against the law and case law, as a table with sources |
| `check-counterparty` | Checks a company via VIES and the public KVK search |
| `lookup-law` | Fetches the current text of an NL or EU article |

```bash
/plugin marketplace add pantalytics/this-should-be-illegal
/plugin install legal-nl@this-should-be-illegal
```

## Law sources

Open, free, no account or key:

- **NL law:** [wetgeving-nl](https://github.com/Apolloccrypt/wetgeving-nl), all Dutch
  legislation as Markdown, synced daily with wetten.overheid.nl (CC0)
- **EU law:** [eurlex-mcp-server](https://github.com/Honeyfield-Org/eurlex-mcp-server) (MIT)
- **NL case law:** [rechtspraak-mcp](https://github.com/prudai/rechtspraak-mcp) (MIT)

The choices behind this repo are in [DECISIONS.md](DECISIONS.md). Want to contribute? See
[CONTRIBUTING.md](CONTRIBUTING.md).

## License

Templates and docs [CC BY 4.0](LICENSES/CC-BY-4.0.txt), code and skills [MIT](LICENSE).
Maintained by [Pantalytics](https://pantalytics.com).
