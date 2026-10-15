# this should be illegal

Open-source legal templates and AI skills for entrepreneurs, with real checks against the
law instead of vibes. Netherlands first, then the rest of Europe, one country at a time.

> **Not legal advice.** Templates are drafts until a lawyer has reviewed them. See
> [DISCLAIMER.md](DISCLAIMER.md).

## What's in it

| Country | Plugin | Templates | Skills |
| ------- | ------ | --------- | ------ |
| 🇳🇱 Netherlands | [`legal-nl`](plugins/legal-nl) | Aandeelhoudersovereenkomst, managementovereenkomst, aandeelhoudersbesluit buiten vergadering | `draft-document`, `review-document`, `check-counterparty` |

Every template:

- is plain Markdown with `{{placeholders}}`, written from the statute, not copied from a
  commercial model;
- lists the articles it relies on in `legal_basis`;
- carries a `status` (`draft` or `reviewed`) and who reviewed it.

## Real checks

1. **Law changed?** A weekly job looks up every cited article on wetten.overheid.nl and fails
   when an article changed after the template's `last_checked` date.
2. **Template consistent?** CI checks frontmatter, that every placeholder is declared, and
   that no template goes unchecked for more than a year.
3. **Live checks in the skills.** The skills call MCP servers for current law, case law
   (ECLI) and the KVK trade register, and say which checks could not run.
4. **Copyright, licenses, secrets.** Every file carries a license via
   [REUSE](https://reuse.software), and [gitleaks](https://github.com/gitleaks/gitleaks) scans
   the full history for API keys. Links are checked weekly.

## Use it

**Claude Code / Cowork**

```bash
/plugin marketplace add pantalytics/this-should-be-illegal
/plugin install legal-nl@this-should-be-illegal
```

Then ask: *"Stel een managementovereenkomst op tussen mijn holding en mijn BV."*

The KVK check needs a key from [developers.kvk.nl](https://developers.kvk.nl). Set
`KVK_API_KEY` in your environment. The other servers need no key.

**Without AI:** open a template, replace the `{{placeholders}}`, work through the checklist at
the bottom, and have a lawyer look at it.

## MCP servers for legal checks

| Server | Covers | Key | License |
| ------ | ------ | --- | ------- |
| [dutch-law-mcp](https://github.com/ansvar-systems/dutch-law-mcp) | NL legislation, wetten.overheid.nl | none | Apache-2.0 |
| [rechtspraak-mcp](https://github.com/prudai/rechtspraak-mcp) | NL case law by ECLI, LiDO citations | none | MIT |
| [kvk-mcp](https://github.com/BartWaardenburg/kvk-mcp) | NL trade register (KVK) | KVK API key | MIT |

Third-party servers, not maintained by us. Check them before you trust them with client data.
More sources, including law-as-Markdown repos and other legal AI projects, are in
[SOURCES.md](SOURCES.md).

## Roadmap

- 🇳🇱 more templates: oprichtersovereenkomst, NDA, opdrachtovereenkomst, verwerkersovereenkomst (AVG)
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
