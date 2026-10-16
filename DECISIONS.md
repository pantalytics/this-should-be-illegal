# Purpose and principles

## Purpose

Give every founder in Europe what it takes to run a company well: legal documents first,
then tax, accounting, notarial deeds and the Chamber of Commerce. Free, in a format both
people and AI can work with, with skills that check it against the current law.

Running a company is largely standard, but the rules differ per country and the help sits
behind lawyers, API keys and subscriptions. AI can make this simple once the knowledge is
open. If every founder contributes a little, everyone benefits.

AI does most of the work; experts step in where it matters. The repo should tell you when AI
is enough and when you need a lawyer, notary or tax advisor.

Start with what a Dutch BV needs, then add countries one by one.

This repo is a library, not a product: plain text that people and AI assistants can read,
fill in, check and improve.

## Principles

Change one only with a pull request that edits this file.

### 1. Small

A handful of good templates and a few good skills. No platform, no build step, no
integrations we have to maintain. Fewer, better documents beat a large catalogue.

### 2. Made for AI: Markdown only

Everything is Markdown with YAML frontmatter, so any AI assistant can read, fill in and
convert it. No Word, PDF, images or other binary files. Need a `.docx`? Ask your AI.

Templates are structured so a machine can work with them:

- `{{placeholders}}` declared in `fields`, with a suggested value;
- choices declared in `options`, with a recommended default;
- the law it relies on in `legal_basis`, with links to the current text.

CI enforces this structure.

### 3. Open source only

All material in this repo is licensed under exactly two licenses:

- **CC BY 4.0** for templates and documentation;
- **MIT** for code and skills.

No material under any other license, and no material whose license is unclear. CI fails if
another license shows up (REUSE check).

Linking is fine, copying is not: we may point to other open sources, but their content stays
in their repo.

### 4. Open sources, no gates

Everything we use or recommend is free to use right away: code under an OSI license,
content under an open license or public domain. No accounts, API keys, download forms or
paywalls.

Law text comes from [wetgeving-nl](https://github.com/Apolloccrypt/wetgeving-nl) (NL, CC0)
and [eurlex-mcp-server](https://github.com/Honeyfield-Org/eurlex-mcp-server) (EU, MIT).

### 5. Written from the statute

We write every template ourselves, from the law. No text from commercial or law-firm models,
not even as a starting point. Legislation and court rulings are public domain, so the result
can be CC BY 4.0.

### 6. No template? The AI drafts one

The `draft-document` skill writes a missing document from the statute in the same format,
marked `draft`, and offers it back as a contribution. The library grows from real requests.

### 7. Honest status

The maintainer is not a lawyer and much of this repo was written with AI. Every template is
`draft` until a named lawyer has reviewed it. Nothing here is legal advice. See
[DISCLAIMER.md](DISCLAIMER.md).

### 8. Law changes are caught three ways

1. **Every use.** The skills read the current article text before they rely on it, and flag
   any difference with the template.
2. **Every week.** CI compares each cited article with its text on the template's
   `last_checked` date, using the history of wetgeving-nl, and opens an issue when one changed.
3. **Every year.** A template whose `last_checked` is more than a year old fails CI, so it
   gets a full re-read even if no cited article changed. New laws that matter but are not yet
   cited are only caught this way.
