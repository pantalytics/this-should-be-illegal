# this should be illegal

> [!CAUTION]
> **I am not a lawyer, and large parts of this repo were written with AI.**
> Nothing here is legal advice. Every template is a draft until a lawyer has reviewed it,
> and none have been reviewed yet. Have a lawyer or notary check any document before you
> sign it. See [DISCLAIMER.md](DISCLAIMER.md).

Free, good legal documents for every entrepreneur in Europe, with AI skills that check them
against the current law. Netherlands first, then country by country.

- **Made for AI.** Plain Markdown with structured frontmatter. Any AI assistant can fill in,
  check and convert the templates.
- **Open source only.** Content CC BY 4.0, code MIT, nothing else. CI enforces it.
- **No gates.** Only open sources: no accounts, API keys or download forms.
- **Written from the statute,** never copied from commercial models.
- **Kept current.** A weekly check flags templates whose cited articles changed.

Purpose and principles: [DECISIONS.md](DECISIONS.md). How to help:
[CONTRIBUTING.md](CONTRIBUTING.md).

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

## Add it to Claude

**Claude app (claude.ai, Desktop, Cowork)**

1. Open **Customize** and choose **Add marketplace**.
2. Choose **Add from a repository** and enter `pantalytics/this-should-be-illegal`.
3. Install the plugin **legal-nl** from that marketplace.
4. Try: *"Stel een rekening-courantovereenkomst op tussen mijn holding en mijn BV."*

**Claude Code**

```bash
/plugin marketplace add pantalytics/this-should-be-illegal
/plugin install legal-nl@this-should-be-illegal
```

**What works where.** Templates and skills work everywhere. The case-law and EU-law servers
run locally through `npx`, so they need Claude Code or Cowork (Claude Desktop) and
[Node.js](https://nodejs.org) 20 or later; on claude.ai in the browser the skills say which
checks could not run. Dutch law text is fetched from GitHub, so Claude needs web access.

**Without a plugin.** Every template is plain Markdown: copy one into any AI chat and ask it
to fill it in with you.

## Law sources

Open, free, no account or key:

- **NL law:** [wetgeving-nl](https://github.com/Apolloccrypt/wetgeving-nl), all Dutch
  legislation as Markdown, synced daily with wetten.overheid.nl (CC0)
- **EU law:** [eurlex-mcp-server](https://github.com/Honeyfield-Org/eurlex-mcp-server) (MIT)
- **NL case law:** [rechtspraak-mcp](https://github.com/prudai/rechtspraak-mcp) (MIT)

## License

Templates and docs [CC BY 4.0](LICENSES/CC-BY-4.0.txt), code and skills [MIT](LICENSE).
Maintained by [Pantalytics](https://pantalytics.com).
