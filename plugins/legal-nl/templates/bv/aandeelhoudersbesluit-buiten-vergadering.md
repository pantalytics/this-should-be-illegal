---
title: Aandeelhoudersbesluit buiten vergadering (BV)
jurisdiction: NL
entity: bv
language: nl
version: 0.2.0
status: draft
reviewed_by: null
last_checked: 2026-10-15
legal_basis:
  - BW 2:210
  - BW 2:216
  - BW 2:238
  - BW 2:239
  - BW 2:244
  - BW 2:245
fields:
  vennootschap_naam: Statutaire naam van de BV
  vennootschap_zetel: Statutaire zetel (gemeente)
  kvk_nummer: KVK-nummer van de BV
  aandeelhouders:
    label: Naam, adres en aantal aandelen per aandeelhouder
    suggestie: "Jansen Holding B.V., KVK 12345678, houder van 100 gewone aandelen"
  bestuurder_naam: Naam van de bestuurder die wordt benoemd of ontslagen
  ingangsdatum:
    label: Datum waarop het besluit ingaat
    suggestie: datum van ondertekening
  bezoldiging:
    label: Bezoldiging van de bestuurder
    suggestie: "nihil; de bestuurder wordt vergoed via een managementovereenkomst"
  wederpartij_naam: Partij met wie de BV de overeenkomst sluit
  overeenkomst_omschrijving:
    label: Welke overeenkomst wordt goedgekeurd
    suggestie: "de managementovereenkomst tussen de Vennootschap en [holding] van [datum]"
  boekjaar:
    label: Boekjaar van de jaarrekening
    suggestie: vorig kalenderjaar
  dividend_bedrag: Bedrag van de uitkering in euro, of 0
  besluit_tekst: Volledige besluittekst bij een ander besluit
  plaats: Plaats van ondertekening
  datum: Datum van het besluit
options:
  besluit:
    vraag: Welk besluit neemt de algemene vergadering?
    default: c
    keuzes:
      a: Benoeming bestuurder
      b: Ontslag bestuurder
      c: Goedkeuring overeenkomst bij tegenstrijdig belang
      d: Vaststelling jaarrekening en winstbestemming
      e: Ander besluit
---

# Besluit van de algemene vergadering van {{vennootschap_naam}}, genomen buiten vergadering

**De ondergetekenden**, te weten alle aandeelhouders en overige vergadergerechtigden van
**{{vennootschap_naam}}**, een besloten vennootschap met beperkte aansprakelijkheid, statutair
gevestigd te {{vennootschap_zetel}}, ingeschreven in het handelsregister onder nummer
{{kvk_nummer}} (de **Vennootschap**):

{{aandeelhouders}}

## Overwegende dat

1. op grond van artikel 2:238 lid 1 BW besluitvorming van aandeelhouders buiten vergadering
   kan plaatsvinden, mits alle vergadergerechtigden met deze wijze van besluitvorming hebben
   ingestemd;
2. de statuten van de Vennootschap deze wijze van besluitvorming niet uitsluiten;
3. het bestuur (en, indien aanwezig, de raad van commissarissen) voorafgaand aan de
   besluitvorming in de gelegenheid is gesteld advies uit te brengen (artikel 2:238 lid 2 BW).

## Verklaren

1. in te stemmen met besluitvorming buiten vergadering, ook langs elektronische weg;
2. hierbij met algemene stemmen te besluiten als volgt:

> **Kies één:** Welk besluit neemt de algemene vergadering?

<!-- optie besluit=a -->
**Optie A: Benoeming bestuurder**

{{bestuurder_naam}} te benoemen tot bestuurder van de Vennootschap met ingang van
{{ingangsdatum}}, en de bezoldiging vast te stellen op: {{bezoldiging}} (artikel 2:245 BW).
<!-- /optie -->

<!-- optie besluit=b -->
**Optie B: Ontslag bestuurder**

{{bestuurder_naam}} te ontslaan als bestuurder van de Vennootschap met ingang van
{{ingangsdatum}} (artikel 2:244 BW), en de bestuurder decharge te verlenen voor het gevoerde
bestuur, voor zover dat blijkt uit de stukken die aan de aandeelhouders zijn verstrekt.
<!-- /optie -->

<!-- optie besluit=c -->
**Optie C: Goedkeuring overeenkomst bij tegenstrijdig belang** *(aanbevolen bij een
managementovereenkomst)*

Vast te stellen dat de enige bestuurder bij het aangaan van {{overeenkomst_omschrijving}}
een tegenstrijdig belang heeft in de zin van artikel 2:239 lid 6 BW, en daarom zelf het
besluit te nemen tot het aangaan van die overeenkomst met {{wederpartij_naam}}, op de
voorwaarden van het concept dat aan dit besluit is gehecht. {{bestuurder_naam}} wordt
gemachtigd de overeenkomst namens de Vennootschap te ondertekenen.
<!-- /optie -->

<!-- optie besluit=d -->
**Optie D: Vaststelling jaarrekening en winstbestemming**

1. de jaarrekening over boekjaar {{boekjaar}} vast te stellen zoals opgemaakt door het
   bestuur;
2. een uitkering te doen van EUR {{dividend_bedrag}} ten laste van de vrij uitkeerbare
   reserves, onder voorbehoud van goedkeuring door het bestuur (artikel 2:216 BW), en het
   restant van het resultaat toe te voegen aan de overige reserves;
3. de bestuurders decharge te verlenen voor het gevoerde bestuur over dat boekjaar.
<!-- /optie -->

<!-- optie besluit=e -->
**Optie E: Ander besluit**

{{besluit_tekst}}
<!-- /optie -->

Elk ondergetekende heeft voor dit besluit gestemd met alle aandelen die hij houdt.

Dit besluit kan in meerdere exemplaren en elektronisch worden ondertekend. Alle exemplaren
samen vormen één besluit.

Getekend te {{plaats}} op {{datum}}.

| Aandeelhouder | Handtekening |
| ------------- | ------------ |
|               |              |
|               |              |

## Wettelijke grondslag

Actuele tekst op wetten.overheid.nl:

- [art. 2:210 BW](https://wetten.overheid.nl/BWBR0003045/#Boek2_Titeldeel5_Afdeling3_Artikel210)
- [art. 2:216 BW](https://wetten.overheid.nl/BWBR0003045/#Boek2_Titeldeel5_Afdeling3_Artikel216)
- [art. 2:238 BW](https://wetten.overheid.nl/BWBR0003045/#Boek2_Titeldeel5_Afdeling4_Artikel238)
- [art. 2:239 BW](https://wetten.overheid.nl/BWBR0003045/#Boek2_Titeldeel5_Afdeling5_Artikel239)
- [art. 2:244 BW](https://wetten.overheid.nl/BWBR0003045/#Boek2_Titeldeel5_Afdeling5_Artikel244)
- [art. 2:245 BW](https://wetten.overheid.nl/BWBR0003045/#Boek2_Titeldeel5_Afdeling5_Artikel245)

---

## Toelichting voor de gebruiker (verwijderen voor ondertekening)

**Opties.** Laat alleen de gekozen optie staan en verwijder de andere, inclusief de
`<!-- optie -->`-markeringen. Wil je meerdere besluiten tegelijk nemen, neem dan meerdere
opties op en nummer ze.

**Checklist**

- [ ] *Alle* vergadergerechtigden tekenen, dus ook houders van certificaten met vergaderrecht en
      vruchtgebruikers met stemrecht. Eén ontbrekende handtekening maakt het besluit nietig.
- [ ] Statuten nagekeken: sluiten ze besluitvorming buiten vergadering of elektronische
      stemming uit?
- [ ] Bestuur en RvC vooraf om advies gevraagd en dat vastgelegd (e-mail volstaat).
- [ ] Optie D met uitkering: het bestuur doet daarna de uitkeringstest en keurt goed
      (art. 2:216 BW). Dat is een apart bestuursbesluit.
- [ ] Optie D: zijn alle aandeelhouders ook bestuurder, dan geldt ondertekening van de
      jaarrekening door alle bestuurders al als vaststelling en kwijting (art. 2:210 lid 5
      BW). Het besluit is dan alleen nodig voor de winstbestemming.
- [ ] Besluit opnemen in het aandeelhoudersregister/notulenboek van de BV.
- [ ] Optie A of B: bestuurswijziging binnen 8 dagen doorgeven aan KVK.
