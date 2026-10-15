# Contributing

Read [DECISIONS.md](DECISIONS.md) first: purpose and principles.

## Ways to help

| You are | Most useful |
| ------- | ----------- |
| Lawyer or notary | Review a template and mark it `reviewed` |
| Entrepreneur | Report what was unclear or missing, via an issue |
| Anyone with an AI assistant | Let `draft-document` write a missing template, check it, open a PR |
| Developer | Improve a skill or the checks |

Small pull requests are best: one template or one fix per PR.

## The license rule

Everything you contribute is published as **CC BY 4.0** (content) or **MIT** (code and
skills). Nothing else.

1. **Write from the statute.** Legislation and court rulings are public domain
   (NL: art. 11 Auteurswet). Law-firm models, commercial templates and paid template sites
   are not: do not copy, translate or closely paraphrase them.
2. **No material under another license**, including CC BY-SA, GPL or "free for personal use".
   Link to it instead.
3. **No client documents**, not even anonymised.
4. **AI-generated text** is fine if you reviewed it and it meets rules 1 to 3.
5. By opening a pull request you confirm you may license your contribution this way. Sign
   off your commits (`git commit -s`).

## Adding a template

Markdown only. Put it in `plugins/legal-<country>/templates/<entity>/<name>.md`, in the local
language, and copy the frontmatter from an existing template.

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

## When the law changes

The weekly check opens an issue naming the template and article. To resolve it:

1. Read the new article text (skill `lookup-law`, or the link under "Wettelijke grondslag").
2. Adjust the template if needed and bump `version`.
3. Set `last_checked` to today, also when nothing had to change. That closes the loop.
4. A template marked `reviewed` goes back to `draft` if the change affects its content.

A law the check does not know yet? Add it to `LAWS` in `scripts/check_law.py`.

## Reviewing a template (lawyers)

Check it against current law, then open a PR that sets `status: reviewed`,
`reviewed_by: "Name, role, firm"`, and bumps `version` and `last_checked`.

## Local checks

```bash
pip install pyyaml
python scripts/validate.py
python scripts/check_law.py   # online, compares cited articles
npx markdownlint-cli2 "**/*.md"
```
