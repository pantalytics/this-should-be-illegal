---
name: lookup-law
description: Haal de actuele tekst op van een Nederlands wetsartikel (bijv. art. 2:238 BW) of een EU-regel (bijv. AVG art. 28), uit open bronnen zonder account. Gebruik dit om een template of contract te toetsen, of als iemand vraagt wat de wet precies zegt.
---

# Wetstekst opzoeken

## Nederland: wetgeving-nl

[wetgeving-nl](https://github.com/Apolloccrypt/wetgeving-nl) bevat alle Nederlandse wetten
als Markdown, dagelijks gesynchroniseerd met wetten.overheid.nl. Wetteksten zijn CC0.

1. Zoek het bestand. Voor het BW:
   `https://raw.githubusercontent.com/Apolloccrypt/wetgeving-nl/main/wetten/burgerlijk-recht/burgerlijk-wetboek-boek-<N>.md`.
   Andere wetten: zoek op titel of BWBR-nummer in
   `https://raw.githubusercontent.com/Apolloccrypt/wetgeving-nl/main/index.json` en gebruik
   het veld `pad`.
2. Het artikel staat onder de kop `##### Artikel <nummer>`, tot de volgende kop.
3. Noem de `toestand` uit de frontmatter van het bestand: de datum van de versie.

Lukt dit niet, gebruik dan `https://wetten.overheid.nl/<BWBR-nummer>` en zeg dat je de
officiële site hebt gebruikt.

## Europa: EUR-Lex

Gebruik de MCP-server `eurlex`: zoek de regeling (`eurlex_search`), haal de geconsolideerde
tekst op (`eurlex_consolidated`) en, bij een richtlijn, hoe Nederland die heeft omgezet
(`eurlex_transposition`).

## Rechtspraak

Gebruik de MCP-server `rechtspraak` voor uitspraken bij een artikel: zoek, en noem ECLI,
instantie, datum en de kern in één zin.

## Rapporteer

Per artikel: het nummer, de versiedatum, de letterlijke tekst van de relevante leden, en de
link naar wetten.overheid.nl of EUR-Lex.
