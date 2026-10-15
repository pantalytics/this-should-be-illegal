---
title: Managementovereenkomst (bestuurder via holding)
jurisdiction: NL
entity: bv
language: nl
version: 0.2.0
status: draft
reviewed_by: null
last_checked: 2026-10-15
legal_basis:
  - BW 2:239
  - BW 2:240
  - BW 2:245
  - BW 2:247
  - BW 7:400
  - BW 7:408
fields:
  vennootschap_naam: Statutaire naam van de werkmaatschappij (opdrachtgever)
  vennootschap_kvk: KVK-nummer van de werkmaatschappij
  vennootschap_vertegenwoordiger:
    label: Wie tekent namens de werkmaatschappij
    suggestie: een andere bestuurder, of een persoon die de AVA daartoe aanwijst
  holding_naam: Statutaire naam van de management-BV (opdrachtnemer)
  holding_kvk: KVK-nummer van de management-BV
  bestuurder_naam: Natuurlijk persoon die de werkzaamheden feitelijk uitvoert
  ingangsdatum: Ingangsdatum van de overeenkomst
  ava_besluit_datum: Datum van het AVA-besluit dat deze overeenkomst goedkeurt
  werkzaamheden:
    label: Taken naast de statutaire bestuurstaak
    suggestie: "algemene leiding, strategie, financiën, commercie en personeelsbeleid"
  uren_per_week:
    label: Indicatieve tijdsbesteding per week
    suggestie: "40"
  vergoeding_per_maand:
    label: Vaste vergoeding per maand, exclusief btw
    suggestie: "minimaal het gebruikelijk loon van de DGA plus werkgeverslasten, gedeeld door 12"
  uurtarief:
    label: Uurtarief, exclusief btw
    suggestie: "125"
  opzegtermijn_maanden:
    label: Opzegtermijn in maanden
    suggestie: "3"
  plaats: Plaats van ondertekening
  datum: Datum van ondertekening
options:
  vergoeding:
    vraag: Hoe wordt de Managementvennootschap betaald?
    default: a
    keuzes:
      a: Vaste vergoeding per maand
      b: Uurtarief op basis van urenregistratie
  einde_bestuur:
    vraag: Wat gebeurt er met de overeenkomst als de Managementvennootschap geen bestuurder meer is?
    default: a
    keuzes:
      a: Eindigt van rechtswege
      b: Loopt door tot einde opzegtermijn
  ziekte:
    vraag: Wat gebeurt er met de vergoeding bij langdurige arbeidsongeschiktheid?
    default: a
    keuzes:
      a: Opschorten na 3 maanden
      b: Doorbetalen tot 12 maanden
---

# Managementovereenkomst

**Partijen**

1. **{{vennootschap_naam}}**, ingeschreven in het handelsregister onder nummer
   {{vennootschap_kvk}}, hierbij vertegenwoordigd door {{vennootschap_vertegenwoordiger}}
   (de **Vennootschap**); en
2. **{{holding_naam}}**, ingeschreven in het handelsregister onder nummer {{holding_kvk}},
   hierbij vertegenwoordigd door {{bestuurder_naam}} (de **Managementvennootschap**).

## Overwegende dat

- de Managementvennootschap statutair bestuurder is van de Vennootschap, of zal worden;
- {{bestuurder_naam}} als enige de werkzaamheden onder deze overeenkomst namens de
  Managementvennootschap uitvoert (de **Manager**);
- partijen een overeenkomst van opdracht willen sluiten in de zin van artikel 7:400 BW en
  uitdrukkelijk geen arbeidsovereenkomst;
- de algemene vergadering van de Vennootschap deze overeenkomst en de vergoeding heeft
  goedgekeurd bij besluit van {{ava_besluit_datum}}.

## 1. Opdracht

1.1 De Vennootschap geeft de Managementvennootschap opdracht tot het verrichten van de
volgende werkzaamheden: {{werkzaamheden}}.

1.2 De Managementvennootschap voert de opdracht zelfstandig uit, zonder toezicht of leiding
van de Vennootschap in de zin van een gezagsverhouding. De wettelijke en statutaire taken en
verplichtingen als bestuurder blijven onverminderd van toepassing.

1.3 De indicatieve tijdsbesteding is {{uren_per_week}} uur per week.

## 2. Vergoeding

> **Kies één:** Hoe wordt de Managementvennootschap betaald?

<!-- optie vergoeding=a -->
**Optie A: Vaste vergoeding per maand** *(aanbevolen: voorspelbaar voor beide partijen)*

2.1 De Vennootschap betaalt een vaste vergoeding van EUR {{vergoeding_per_maand}} per maand,
te vermeerderen met btw, op basis van een maandelijkse factuur. De vergoeding wordt jaarlijks
per 1 januari geïndexeerd met de CPI (alle huishoudens) van het CBS.
<!-- /optie -->

<!-- optie vergoeding=b -->
**Optie B: Uurtarief** *(past bij parttime of wisselende inzet)*

2.1 De Vennootschap betaalt een vergoeding van EUR {{uurtarief}} per gewerkt uur, te
vermeerderen met btw. De Managementvennootschap factureert maandelijks achteraf op basis van
een urenregistratie, die de Vennootschap op verzoek inziet.
<!-- /optie -->

2.2 Redelijke, vooraf goedgekeurde onkosten worden op declaratiebasis vergoed. Facturen worden
binnen 14 dagen betaald.

2.3 Wijziging van de vergoeding vereist een besluit van de algemene vergadering
(artikel 2:245 BW), tenzij de statuten anders bepalen.

## 3. Duur en beëindiging

3.1 Deze overeenkomst gaat in op {{ingangsdatum}} en geldt voor onbepaalde tijd.

3.2 Elke partij kan de overeenkomst schriftelijk opzeggen met inachtneming van een
opzegtermijn van {{opzegtermijn_maanden}} maanden. Partijen sluiten de opzeggingsbevoegdheid
van artikel 7:408 lid 1 BW uit voor zover die afwijkt van deze termijn.

> **Kies één:** Wat gebeurt er met de overeenkomst als de Managementvennootschap geen
> bestuurder meer is?

<!-- optie einde_bestuur=a -->
**Optie A: Eindigt van rechtswege** *(aanbevolen voor de Vennootschap)*

3.3 De overeenkomst eindigt van rechtswege, zonder opzegtermijn en zonder recht op
schadevergoeding, op het moment dat de Managementvennootschap ophoudt bestuurder van de
Vennootschap te zijn.
<!-- /optie -->

<!-- optie einde_bestuur=b -->
**Optie B: Loopt door tot einde opzegtermijn** *(beschermt de Manager)*

3.3 Houdt de Managementvennootschap op bestuurder te zijn, dan geldt dat als opzegging door
de Vennootschap tegen het einde van de opzegtermijn van artikel 3.2. Gedurende die termijn
blijft de vergoeding verschuldigd, ook als de Vennootschap geen werkzaamheden meer verlangt.
<!-- /optie -->

3.4 Elke partij kan de overeenkomst met onmiddellijke ingang opzeggen bij faillissement,
surseance of een dringende reden aan de zijde van de andere partij of de Manager.

## 4. Vervanging en arbeidsongeschiktheid

4.1 De Managementvennootschap mag de Manager alleen vervangen met voorafgaande schriftelijke
toestemming van de algemene vergadering.

> **Kies één:** Wat gebeurt er met de vergoeding bij langdurige arbeidsongeschiktheid?

<!-- optie ziekte=a -->
**Optie A: Opschorten na 3 maanden** *(aanbevolen voor een jonge BV)*

4.2 Is de Manager langer dan drie maanden aaneengesloten arbeidsongeschikt, dan mag de
Vennootschap de vergoeding opschorten voor de verdere duur van de ongeschiktheid.
<!-- /optie -->

<!-- optie ziekte=b -->
**Optie B: Doorbetalen tot 12 maanden** *(alleen als de Vennootschap dit kan dragen)*

4.2 Bij arbeidsongeschiktheid van de Manager betaalt de Vennootschap de vergoeding door
gedurende ten hoogste twaalf maanden, verminderd met uitkeringen die de
Managementvennootschap of de Manager ontvangt uit een arbeidsongeschiktheidsverzekering.
<!-- /optie -->

## 5. Geheimhouding en intellectueel eigendom

5.1 De Managementvennootschap en de Manager houden alle vertrouwelijke informatie over de
Vennootschap geheim, ook na einde van de overeenkomst.

5.2 Alle intellectuele eigendomsrechten op resultaten van de werkzaamheden komen toe aan de
Vennootschap. Voor zover nodig draagt de Managementvennootschap deze rechten hierbij over en
staat zij in voor medewerking van de Manager.

## 6. Aansprakelijkheid

De aansprakelijkheid van de Managementvennootschap onder deze overeenkomst is beperkt tot het
bedrag van de vergoeding over de laatste twaalf maanden, behalve bij opzet of bewuste
roekeloosheid. Dit laat de aansprakelijkheid als bestuurder op grond van de wet onverlet.

## 7. Slotbepalingen

7.1 Op deze overeenkomst is Nederlands recht van toepassing.

7.2 Geschillen worden voorgelegd aan de bevoegde rechter in het arrondissement waar de
Vennootschap statutair is gevestigd.

Aldus overeengekomen en ondertekend te {{plaats}} op {{datum}}.

| Namens de Vennootschap | Namens de Managementvennootschap |
| ---------------------- | -------------------------------- |
|                        |                                  |

---

## Toelichting voor de gebruiker (verwijderen voor ondertekening)

**Opties.** Bij elke keuze staat de aanbevolen optie. Laat per keuze één optie staan en
verwijder de andere, inclusief de `<!-- optie -->`-markeringen.

**Tegenstrijdig belang (art. 2:239 lid 6 BW).** De bestuurder sluit deze overeenkomst
feitelijk met zichzelf. Hij neemt niet deel aan het bestuursbesluit. Is hij de enige
bestuurder, dan beslist de RvC of, zonder RvC, de algemene vergadering. Gebruik daarvoor het
template *aandeelhoudersbesluit-buiten-vergadering*, optie C.

**Wie tekent namens de Vennootschap?** De vertegenwoordigingsbevoegdheid van een bestuurder
blijft ook bij tegenstrijdig belang bestaan (art. 2:240 BW). Laat bij voorkeur een andere
bestuurder of een door de AVA aangewezen persoon tekenen.

**Enig aandeelhouder?** Vertegenwoordigt de enig aandeelhouder de Vennootschap, dan moet de
overeenkomst schriftelijk worden vastgelegd, anders kan zij worden vernietigd (art. 2:247 BW).

**Checklist**

- [ ] AVA-besluit genomen dat deze overeenkomst en de vergoeding goedkeurt.
- [ ] Statuten nagekeken op afwijkende regels voor tegenstrijdig belang en bezoldiging.
- [ ] Gebruikelijkloonregeling (art. 12a Wet LB 1964): de Manager heeft als DGA meestal een
      salaris nodig vanuit de holding. De vergoeding moet dat kunnen dragen. Laat dit fiscaal
      toetsen.
- [ ] Geen gezagsverhouding in de praktijk (Wet DBA). Een arbeidsovereenkomst kan ontstaan
      ongeacht wat partijen opschrijven.
- [ ] Btw: de management-BV factureert in de regel met btw, tenzij er een fiscale eenheid is.
- [ ] Optie B bij ziekte: is er een arbeidsongeschiktheidsverzekering afgesloten?
- [ ] Concurrentiebeding nodig? Dan apart en redelijk afspreken, met duur en gebied.
