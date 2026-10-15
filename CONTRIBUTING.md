# Contributing

Lawyers reviewing templates is the most valuable contribution. Read
[DECISIONS.md](DECISIONS.md) first.

## Copyright rules

Templates are CC BY 4.0. Only contribute text you may license that way.

1. **Write from the statute.** Legislation and court rulings are not protected by copyright
   (NL: art. 11 Auteurswet). Law-firm and commercial models are.
2. **Do not copy, translate or closely paraphrase** clauses from such models or paid template
   sites.
3. **No client documents**, not even anonymised.
4. **AI-generated text** is fine if you reviewed it and it meets rules 1 to 3.
5. By opening a pull request you confirm you may license your contribution under CC BY 4.0
   (content) or MIT (code). Sign off your commits (`git commit -s`).

## Adding a template

Put it in `plugins/legal-<country>/templates/<entity>/<name>.md`, in the local language, and
copy the frontmatter from an existing template.

- `{{snake_case}}` placeholders, each declared in `fields` as a label or as
  `{label, suggestie}`.
- Where users commonly choose, write out the options and declare them in `options` with a
  `vraag`, the `keuzes` and a recommended `default`. Two or three, not five:

  ```markdown
  > **Kies één:** Wie beslist bij een geschil?

  <!-- optie forum=a -->
  **Optie A: Rechtbank** *(aanbevolen: goedkoper)*

  Clause text…
  <!-- /optie -->
  ```

- Every article you rely on in `legal_basis` (format `BW 2:238`), and linked under
  "Wettelijke grondslag".
- End with "Toelichting voor de gebruiker": when to use it, and a checklist.
- New templates start as `status: draft`.

## Reviewing a template (lawyers)

Check it against current law, then open a PR that sets `status: reviewed`,
`reviewed_by: "Name, role, firm"`, and bumps `version` and `last_checked`.

## Local checks

```bash
pip install pyyaml
python scripts/validate.py
npx markdownlint-cli2 "**/*.md"
```
