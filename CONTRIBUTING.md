# Contributing

Thanks for helping. Lawyers reviewing templates is the most valuable contribution.

## Copyright rules (read first)

Templates are published under CC BY 4.0. You may only contribute text you have the right to
license that way.

1. **Write from the statute, not from someone else's model.** Legislation and court rulings
   are not protected by copyright (NL: art. 11 Auteurswet). Commercial and "free download"
   models usually are, including those listed in [SOURCES.md](SOURCES.md).
2. **Do not copy, translate or closely paraphrase** clauses from law-firm templates, model
   documents (Capital Waters, Captain Legal, Grant Thornton, NVP, etc.) or paid template
   sites. Link to them in `SOURCES.md` instead.
3. **No client documents.** Never contribute a contract you drafted for a client, even
   anonymised, unless you own the rights and the client agreed.
4. **AI-generated text** is fine if you reviewed it and it meets rules 1 to 3.
5. By opening a pull request you confirm you have the right to license your contribution
   under CC BY 4.0 (content) or MIT (code). Sign off your commits (`git commit -s`).

## Adding a template

1. Put it in `plugins/legal-<country>/templates/<entity>/<name>.md`, in the language of the
   jurisdiction.
2. Copy the frontmatter from an existing template. Required: `title`, `jurisdiction`,
   `language`, `version`, `status`, `last_checked`, `legal_basis`, `fields`.
3. Use `{{snake_case}}` placeholders and declare each one in `fields`.
4. Cite every article you rely on in `legal_basis` (format `BW 2:238`). The weekly law check
   uses this list.
5. End with a "Toelichting voor de gebruiker" section: when to use it, and a checklist.
6. New templates start as `status: draft`.

## Reviewing a template (lawyers)

Check it against current law, then open a PR that sets `status: reviewed`,
`reviewed_by: "Name, role, firm"`, bumps `version` and `last_checked`. A review is a
statement about the template text, not advice to any user.

## Adding a country

Create `plugins/legal-<iso-code>/` with the same layout as `legal-nl`, add it to
`.claude-plugin/marketplace.json`, and extend `BWB_IDS` in `scripts/check_law_changes.py`
or add an equivalent lookup for that country's official law portal.

## Local checks

```bash
pip install pyyaml
python scripts/validate.py
python scripts/check_law_changes.py
npx markdownlint-cli2 "**/*.md"
```
