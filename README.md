<div align="center">

<a href="assets/launch.mp4"><img src="assets/banner.jpg" width="100%"
  alt="Folding screen: a rabbit buried in contracts gets a brush from a frog and draws its way out"></a>

# this should be illegal

**Everything a founder needs to run a company in Europe. Free, open, and readable by
people and AI alike.**

The rules for running a company are public. Yet every country has its own, and the help is
locked behind lawyers, API keys and subscriptions. That should be illegal.

[![Templates](https://img.shields.io/badge/templates-5-1f6feb)](#templates)
[![Lawyer reviewed](https://img.shields.io/badge/lawyer_reviewed-0%2F5-d1242f)](https://github.com/pantalytics/this-should-be-illegal/labels/lawyer-review)
[![License](https://img.shields.io/badge/license-CC_BY_4.0-2da44e)](LICENSES/CC-BY-4.0.txt)
[![Stars](https://img.shields.io/github/stars/pantalytics/this-should-be-illegal?style=flat&color=e3b341)](https://github.com/pantalytics/this-should-be-illegal/stargazers)

**[Watch the 8-second film](assets/launch.mp4)** ·
**[Use it in Claude](#add-it-to-claude)** ·
**[Help build it](#help-build-it)** ·
**[Star it](https://github.com/pantalytics/this-should-be-illegal/stargazers)**

</div>

> [!CAUTION]
> **I am not a lawyer, and large parts of this repo were written with AI.**
> Nothing here is legal advice. Every template is a draft until a lawyer has reviewed it,
> and none have been reviewed yet. Have a lawyer or notary check any document before you
> sign it. See [DISCLAIMER.md](DISCLAIMER.md).

If every founder adds a little, every founder benefits. This repo collects what running a
company actually takes, as plain Markdown:

- **Templates** for the documents you need, written from the statute.
- **Skills** that let any AI fill them in, check them and look up the current law.
- **Checks** that flag when the law changed. Next: telling you when AI is enough and when
  you need a lawyer, notary or tax advisor.

Legal first (shareholders, management, loans), then tax, accounting, notarial deeds and the
Chamber of Commerce. Netherlands first, then country by country.

- **Open source only.** Content CC BY 4.0, code MIT, nothing else. CI enforces it.
- **No gates.** Only open sources: no accounts, API keys or download forms.
- **Kept current.** A weekly check flags templates whose cited articles changed.

Purpose and principles: [DECISIONS.md](DECISIONS.md).

## Help build it

Five templates is a start. Every one you add or review makes it useful for the next
founder.

| You are | Do this | Takes |
| ------- | ------- | ----- |
| **Lawyer or notary** | [Review one template](https://github.com/pantalytics/this-should-be-illegal/labels/lawyer-review) and get credited by name in it | 1 hour |
| **Entrepreneur** | [Ask for the document you need](https://github.com/pantalytics/this-should-be-illegal/issues/new?template=template-request.yml) | 2 minutes |
| **Anyone with an AI** | [Pick a missing template](https://github.com/pantalytics/this-should-be-illegal/labels/good%20first%20issue), let `draft-document` write it from the law, open a PR | 30 minutes |
| **Everyone** | [Star the repo](https://github.com/pantalytics/this-should-be-illegal/stargazers) so others find it | 1 second |

Rules for contributions: [CONTRIBUTING.md](CONTRIBUTING.md). Short version: write from the
statute, never copy a commercial model.

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

No install button exists for the app yet, so add it by hand:

1. Open **Customize** and choose **Add marketplace**.
2. Choose **Add from a repository** and enter `pantalytics/this-should-be-illegal`.
3. Install the plugin **legal-nl** from that marketplace.
4. Try: *"Stel een rekening-courantovereenkomst op tussen mijn holding en mijn BV."*

**Claude Code**

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_legal--nl-0098FF?logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect?url=vscode%3A%2F%2Fanthropic.claude-code%2Finstall-plugin%3Fplugin%3Dlegal-nl%26marketplace%3Dpantalytics%2Fthis-should-be-illegal)

Or in the terminal:

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
