# this should be illegal

Open-source legal templates and AI skills for entrepreneurs, with real checks against the
law instead of vibes. Netherlands first, then the rest of Europe, one country at a time.

Everything you need is in this repo. No download forms, no sign-up walls: we write the
templates ourselves, with the community, from the statute.

> **Not legal advice.** Templates are drafts until a lawyer has reviewed them. See
> [DISCLAIMER.md](DISCLAIMER.md).

## Templates

| Country | Template | Word | Status |
| ------- | -------- | ---- | ------ |
| 🇳🇱 | [Aandeelhoudersovereenkomst](plugins/legal-nl/templates/bv/aandeelhoudersovereenkomst.md) | [.docx](https://github.com/pantalytics/this-should-be-illegal/releases/latest/download/aandeelhoudersovereenkomst.docx) | draft |
| 🇳🇱 | [Managementovereenkomst](plugins/legal-nl/templates/bv/managementovereenkomst.md) | [.docx](https://github.com/pantalytics/this-should-be-illegal/releases/latest/download/managementovereenkomst.docx) | draft |
| 🇳🇱 | [Aandeelhoudersbesluit buiten vergadering](plugins/legal-nl/templates/bv/aandeelhoudersbesluit-buiten-vergadering.md) | [.docx](https://github.com/pantalytics/this-should-be-illegal/releases/latest/download/aandeelhoudersbesluit-buiten-vergadering.docx) | draft |

Every template has:

- **Full clause text.** Only names, numbers and dates are left open, as `{{placeholders}}`.
  In Word they show as yellow `[● …]` markers.
- **Suggestions.** Each open field carries a suggested value, e.g. vesting 48 months with a
  12-month cliff.
- **Options.** Where founders usually choose (vesting, leaver, deadlock, forum, fee), all
  common options are written out, with the recommended one marked. Keep one, delete the rest.
- **Links to the law.** The articles it relies on, linked to the current text on
  wetten.overheid.nl.
- **A checklist** of what to arrange outside the document (statuten, KVK, tax).

## Real checks

1. **Law changed?** A weekly job looks up every cited article on wetten.overheid.nl and opens
   an issue when an article changed after the template's `last_checked` date.
2. **Template consistent?** CI checks that every placeholder and option is declared and
   complete, and that no template goes unchecked for more than a year.
3. **Live checks in the skills.** The skills call MCP servers for current law, case law
   (ECLI) and the KVK trade register, and say which checks could not run.
4. **Copyright, licenses, secrets.** Every file carries a license via
   [REUSE](https://reuse.software), and [gitleaks](https://github.com/gitleaks/gitleaks) scans
   the full history for API keys. Links are checked weekly.

## Use it

**In Word:** download a `.docx` above, fill in the yellow fields, pick the options, work
through the checklist, have a lawyer look at it.

**With Claude Code / Cowork:**

```bash
/plugin marketplace add pantalytics/this-should-be-illegal
/plugin install legal-nl@this-should-be-illegal
```

Then ask: *"Stel een managementovereenkomst op tussen mijn holding en mijn BV."* The skill
asks for what it cannot look up, walks you through the options, and checks the law live.

The KVK check needs a key from [developers.kvk.nl](https://developers.kvk.nl). Set
`KVK_API_KEY` in your environment. The law server asks for a free Ansvar login on first use.
Case law needs nothing.

**With [Mike](https://github.com/willchen96/mike)** (open-source legal AI platform): import
the `.docx` files into Library → Templates, and add the MCP servers below under
Settings → Connectors. We do not fork Mike; we supply Dutch content it can use.

## MCP servers for legal checks

| Server | Covers | Key | License |
| ------ | ------ | --- | ------- |
| [dutch-law-mcp](https://github.com/ansvar-systems/dutch-law-mcp) | NL legislation, wetten.overheid.nl | free Ansvar account (OAuth) | Apache-2.0 |
| [rechtspraak-mcp](https://github.com/prudai/rechtspraak-mcp) | NL case law by ECLI, LiDO citations | none | MIT |
| [kvk-mcp](https://github.com/BartWaardenburg/kvk-mcp) | NL trade register (KVK) | KVK API key | MIT |

Third-party servers, not maintained by us. Check them before you trust them with client data.
More references are in [SOURCES.md](SOURCES.md).

## Roadmap

- 🇳🇱 more templates: investeerders-SHA, NDA, opdrachtovereenkomst, verwerkersovereenkomst (AVG)
- 🇪🇺 EU law links (EUR-Lex) for templates that rely on EU regulations, starting with the AVG
- 🇧🇪 🇩🇪 next countries: one plugin per country (`legal-be`, `legal-de`), same structure
- lawyer review of the NL templates, so they can move from `draft` to `reviewed`

## Contribute

Lawyers and founders welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), in particular the
copyright rules.

## License

- Templates and other content: [CC BY 4.0](LICENSES/CC-BY-4.0.txt)
- Code, skills and CI: [MIT](LICENSE)

Per-file details are in [REUSE.toml](REUSE.toml).

Maintained by [Pantalytics](https://pantalytics.com).
