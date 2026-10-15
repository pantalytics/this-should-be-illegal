---
title: Aandeelhoudersovereenkomst (BV, oprichters)
jurisdiction: NL
entity: bv
language: nl
version: 0.2.0
status: draft
reviewed_by: null
last_checked: 2026-10-15
legal_basis:
  - BW 2:192
  - BW 2:195
  - BW 2:216
  - BW 2:238
  - BW 2:244
  - BW 6:92
  - BW 6:94
  - BW 6:248
  - BW 7:900
fields:
  vennootschap_naam: Statutaire naam van de BV
  vennootschap_kvk: KVK-nummer van de BV
  partijen:
    label: Naam, rechtsvorm, KVK-nummer en vertegenwoordiger per aandeelhouder
    suggestie: "Jansen Holding B.V., KVK 12345678, vertegenwoordigd door P. Jansen"
  aandelenverdeling:
    label: Tabel met aandeelhouder, aantal aandelen, soort en percentage
    suggestie: "Jansen Holding B.V. | 500 gewone aandelen | 50%"
  gekwalificeerde_meerderheid:
    label: Meerderheid voor gekwalificeerde besluiten
    suggestie: "75%"
  vesting_maanden:
    label: Totale vestingperiode in maanden
    suggestie: "48"
  cliff_maanden:
    label: Cliff in maanden
    suggestie: "12"
  drag_along_drempel:
    label: Percentage van de aandelen dat drag-along kan inroepen
    suggestie: "75%"
  non_compete_maanden:
    label: Duur van het concurrentie- of relatiebeding na vertrek, in maanden
    suggestie: "12"
  boete_bedrag:
    label: Boete per overtreding van artikel 6
    suggestie: "10.000"
  boete_per_dag:
    label: Boete per dag dat de overtreding voortduurt
    suggestie: "500"
  plaats: Plaats van ondertekening
  datum: Datum van ondertekening
options:
  vesting:
    vraag: Moeten oprichters hun aandelen verdienen over tijd?
    default: b
    keuzes:
      a: Geen vesting
      b: Vesting met cliff
  leaver:
    vraag: Welke prijs krijgt een vertrekkende oprichter?
    default: a
    keuzes:
      a: Good en bad leaver
      b: Good, intermediate en bad leaver
  non_compete:
    vraag: Wat mag een vertrekkende aandeelhouder niet doen?
    default: a
    keuzes:
      a: Concurrentie- en relatiebeding
      b: Alleen relatiebeding
  impasse:
    vraag: Hoe doorbreek je een patstelling tussen aandeelhouders?
    default: a
    keuzes:
      a: Mediation, daarna koop-of-verkoopregeling
      b: Mediation, daarna bindend advies
      c: Mediation, daarna gezamenlijke verkoop
  forum:
    vraag: Wie beslist bij een geschil?
    default: a
    keuzes:
      a: Rechtbank
      b: Arbitrage (NAI)
---

> **Let op:** concept, opgesteld door een niet-jurist en grotendeels met AI geschreven. Geen
> juridisch advies. Laat dit document toetsen door een advocaat of notaris voordat je het
> gebruikt. Zie [DISCLAIMER.md](../../../../DISCLAIMER.md). *Verwijder dit blok voor ondertekening.*

# Aandeelhoudersovereenkomst {{vennootschap_naam}}

**Partijen**

{{partijen}}

(samen de **Aandeelhouders**, ieder een **Aandeelhouder**), en

**{{vennootschap_naam}}**, ingeschreven in het handelsregister onder nummer
{{vennootschap_kvk}} (de **Vennootschap**).

## Overwegende dat

- de Aandeelhouders alle geplaatste aandelen in de Vennootschap houden, als volgt:

{{aandelenverdeling}}

- de Aandeelhouders afspraken willen maken over bestuur, besluitvorming, overdracht van
  aandelen en hun onderlinge verhouding, aanvullend op de statuten.

## 1. Rangorde

1.1 Bij strijd tussen deze overeenkomst en de statuten gaat deze overeenkomst tussen partijen
voor. De Aandeelhouders stemmen voor een statutenwijziging die de strijdigheid opheft.

1.2 Deze overeenkomst werkt alleen tussen partijen. Verplichtingen die ook tegenover nieuwe
aandeelhouders moeten gelden, nemen partijen op in de statuten (artikel 2:192 BW).

## 2. Bestuur

2.1 Het bestuur bestaat uit de personen die de Aandeelhouders bij gewone meerderheid
benoemen. Benoeming, schorsing en ontslag van bestuurders geschiedt door de algemene
vergadering (artikel 2:244 BW).

2.2 Het bestuur stelt jaarlijks een begroting en een ondernemingsplan op, ter goedkeuring van
de algemene vergadering.

## 3. Gekwalificeerde besluiten

3.1 De volgende besluiten vereisen een besluit van de algemene vergadering met ten minste
{{gekwalificeerde_meerderheid}} van de uitgebrachte stemmen:

a. uitgifte van aandelen of rechten tot het nemen van aandelen, en uitsluiting van het
   voorkeursrecht;
b. wijziging van de statuten, fusie, splitsing of ontbinding;
c. vervreemding van (een wezenlijk deel van) de onderneming;
d. aangaan van leningen of zekerheden boven een in de begroting vastgesteld bedrag;
e. uitkering van dividend (onverminderd de goedkeuring door het bestuur, artikel 2:216 BW);
f. overeenkomsten tussen de Vennootschap en een Aandeelhouder of een aan hem gelieerde
   partij;
g. benoeming en ontslag van bestuurders en vaststelling van hun bezoldiging.

3.2 De Aandeelhouders mogen besluiten buiten vergadering nemen (artikel 2:238 BW).

## 4. Overdracht van aandelen

4.1 **Aanbiedingsplicht.** Een Aandeelhouder die aandelen wil vervreemden, biedt deze eerst
aan de andere Aandeelhouders aan, naar evenredigheid van hun aandelenbezit, tegen de prijs
die door een onafhankelijke deskundige wordt vastgesteld als partijen het niet eens worden
(artikel 2:195 BW). Deze regeling wordt ook in de statuten opgenomen.

4.2 **Lock-up.** Gedurende twee jaar na ondertekening draagt geen Aandeelhouder aandelen over
zonder toestemming van de andere Aandeelhouders, behalve aan een eigen holding waarvan hij
alle aandelen houdt.

4.3 **Tag-along.** Wil een Aandeelhouder meer dan 50% van de aandelen aan een derde
verkopen, dan kunnen de overige Aandeelhouders verlangen dat de derde ook hun aandelen koopt,
tegen dezelfde prijs en voorwaarden.

4.4 **Drag-along.** Aanvaarden Aandeelhouders die samen ten minste {{drag_along_drempel}}
van de aandelen houden een bonafide bod van een derde op alle aandelen, dan zijn de overige
Aandeelhouders verplicht hun aandelen tegen dezelfde prijs en voorwaarden te verkopen.

4.5 **Toetreding.** Een nieuwe aandeelhouder wordt pas ingeschreven nadat hij tot deze
overeenkomst is toegetreden.

## 5. Vesting en leaver

> **Kies één:** Moeten oprichters hun aandelen verdienen over tijd?

<!-- optie vesting=a -->
**Optie A: Geen vesting** *(alleen als alle oprichters al jaren samenwerken)*

5.1 De aandelen van iedere Aandeelhouder zijn vanaf ondertekening volledig gevest. Artikel 5.2
is alleen van toepassing bij een bad leaver.
<!-- /optie -->

<!-- optie vesting=b -->
**Optie B: Vesting met cliff** *(aanbevolen: marktstandaard bij startende oprichters)*

5.1 De aandelen van iedere oprichtende Aandeelhouder die tevens bestuurder of
managementvennootschap is (een **Oprichter**), vesten over {{vesting_maanden}} maanden vanaf
ondertekening, met een cliff van {{cliff_maanden}} maanden, daarna lineair per maand.
<!-- /optie -->

> **Kies één:** Welke prijs krijgt een vertrekkende oprichter?

<!-- optie leaver=a -->
**Optie A: Good en bad leaver** *(aanbevolen: eenvoudig)*

5.2 Eindigt de betrokkenheid van een Oprichter, dan is hij verplicht zijn aandelen aan te
bieden aan de overige Aandeelhouders of de Vennootschap:

a. **Good leaver** (overlijden, arbeidsongeschiktheid, ontslag zonder dringende reden):
   gevest deel tegen marktwaarde, ongevest deel tegen nominale waarde;
b. **Bad leaver** (dringende reden, schending van deze overeenkomst, eigen vertrek binnen de
   cliff): alle aandelen tegen de laagste van nominale waarde en marktwaarde.
<!-- /optie -->

<!-- optie leaver=b -->
**Optie B: Good, intermediate en bad leaver** *(gebruikelijk zodra er investeerders zijn)*

5.2 Eindigt de betrokkenheid van een Oprichter, dan is hij verplicht zijn aandelen aan te
bieden aan de overige Aandeelhouders of de Vennootschap:

a. **Good leaver** (overlijden, arbeidsongeschiktheid): alle aandelen tegen marktwaarde;
b. **Intermediate leaver** (eigen vertrek na de cliff, ontslag zonder dringende reden):
   gevest deel tegen marktwaarde, ongevest deel tegen nominale waarde;
c. **Bad leaver** (dringende reden, schending van deze overeenkomst, eigen vertrek binnen de
   cliff): alle aandelen tegen de laagste van nominale waarde en marktwaarde.
<!-- /optie -->

5.3 Marktwaarde wordt bij gebrek aan overeenstemming vastgesteld door een onafhankelijke
registervaluator, aangewezen door het NIRV.

5.4 Partijen nemen de aanbiedingsplicht bij leaver op in de statuten (artikel 2:192 lid 1
sub c BW), zodat deze ook tegenover de Vennootschap afdwingbaar is.

## 6. Geheimhouding en concurrentie

6.1 Iedere Aandeelhouder houdt vertrouwelijke informatie over de Vennootschap geheim.

> **Kies één:** Wat mag een vertrekkende aandeelhouder niet doen?

<!-- optie non_compete=a -->
**Optie A: Concurrentie- en relatiebeding** *(aanbevolen voor oprichters)*

6.2 Zolang een Aandeelhouder aandelen houdt en gedurende {{non_compete_maanden}} maanden
daarna, is het hem niet toegestaan direct of indirect activiteiten te ontplooien die
concurreren met de Vennootschap, of klanten en medewerkers van de Vennootschap te benaderen
om hun relatie met de Vennootschap te beëindigen of te beperken.
<!-- /optie -->

<!-- optie non_compete=b -->
**Optie B: Alleen relatiebeding** *(voor kleine of passieve aandeelhouders)*

6.2 Zolang een Aandeelhouder aandelen houdt en gedurende {{non_compete_maanden}} maanden
daarna, is het hem niet toegestaan klanten en medewerkers van de Vennootschap te benaderen om
hun relatie met de Vennootschap te beëindigen of te beperken.
<!-- /optie -->

6.3 Bij overtreding van dit artikel verbeurt de overtreder een direct opeisbare boete van
EUR {{boete_bedrag}} per overtreding en EUR {{boete_per_dag}} voor elke dag dat de overtreding
voortduurt, onverminderd het recht op volledige schadevergoeding. Partijen sluiten
artikel 6:92 lid 2 BW uit.

## 7. Impasse

7.1 Kunnen de Aandeelhouders over een gekwalificeerd besluit twee keer achter elkaar geen
besluit nemen (een **Impasse**), dan schakelen zij binnen 30 dagen een mediator in.

> **Kies één:** Hoe doorbreek je een patstelling tussen aandeelhouders?

<!-- optie impasse=a -->
**Optie A: Koop-of-verkoopregeling** *(aanbevolen bij twee gelijke oprichters)*

7.2 Is de Impasse 60 dagen na aanvang van de mediation niet opgelost, dan kan iedere
Aandeelhouder de andere(n) schriftelijk een prijs per aandeel noemen. De ontvanger kiest
binnen 30 dagen of hij zijn aandelen tegen die prijs verkoopt, of de aandelen van de
bieder tegen die prijs koopt. Kiest hij niet, dan geldt hij als verkoper.
<!-- /optie -->

<!-- optie impasse=b -->
**Optie B: Bindend advies** *(behoud van de samenwerking, inhoudelijke geschillen)*

7.2 Is de Impasse 60 dagen na aanvang van de mediation niet opgelost, dan legt iedere
Aandeelhouder het geschil voor aan een door partijen gezamenlijk, of bij gebrek aan
overeenstemming door de mediator, aangewezen onafhankelijke deskundige. Diens beslissing geldt
als bindend advies (artikel 7:900 BW) en de Aandeelhouders stemmen daarnaar.
<!-- /optie -->

<!-- optie impasse=c -->
**Optie C: Gezamenlijke verkoop** *(als niemand de ander wil of kan uitkopen)*

7.2 Is de Impasse 60 dagen na aanvang van de mediation niet opgelost, dan zetten de
Aandeelhouders gezamenlijk een verkoopproces op voor alle aandelen, begeleid door een door hen
aangewezen corporate-financeadviseur. Iedere Aandeelhouder werkt mee aan verkoop aan de
hoogste bonafide bieder; artikel 4.4 is van overeenkomstige toepassing.
<!-- /optie -->

## 8. Duur

Deze overeenkomst geldt zolang ten minste twee partijen aandelen houden. Zij eindigt voor
een Aandeelhouder die geen aandelen meer houdt, behalve voor de artikelen 6 en 9.

## 9. Slotbepalingen

9.1 Wijziging van deze overeenkomst vereist instemming van alle partijen, schriftelijk.

9.2 Partijen sluiten ontbinding van deze overeenkomst uit, behoudens beëindiging op grond van
artikel 8.

9.3 Op deze overeenkomst is Nederlands recht van toepassing.

> **Kies één:** Wie beslist bij een geschil?

<!-- optie forum=a -->
**Optie A: Rechtbank** *(aanbevolen: goedkoper, hoger beroep mogelijk)*

9.4 Geschillen worden voorgelegd aan de bevoegde rechter in het arrondissement waar de
Vennootschap statutair is gevestigd.
<!-- /optie -->

<!-- optie forum=b -->
**Optie B: Arbitrage (NAI)** *(vertrouwelijk, sneller, duurder)*

9.4 Geschillen worden beslecht door arbitrage overeenkomstig het Arbitragereglement van het
Nederlands Arbitrage Instituut. Het scheidsgerecht bestaat uit één arbiter, de plaats van
arbitrage is Amsterdam en de procedure wordt in het Nederlands gevoerd.
<!-- /optie -->

Aldus overeengekomen en ondertekend te {{plaats}} op {{datum}}.

| Partij | Handtekening |
| ------ | ------------ |
|        |              |
|        |              |
|        |              |

## Wettelijke grondslag

Actuele tekst op wetten.overheid.nl:

- [art. 2:192 BW](https://wetten.overheid.nl/BWBR0003045/#Boek2_Titeldeel5_Afdeling2_Artikel192)
- [art. 2:195 BW](https://wetten.overheid.nl/BWBR0003045/#Boek2_Titeldeel5_Afdeling2_Artikel195)
- [art. 2:216 BW](https://wetten.overheid.nl/BWBR0003045/#Boek2_Titeldeel5_Afdeling3_Artikel216)
- [art. 2:238 BW](https://wetten.overheid.nl/BWBR0003045/#Boek2_Titeldeel5_Afdeling4_Artikel238)
- [art. 2:244 BW](https://wetten.overheid.nl/BWBR0003045/#Boek2_Titeldeel5_Afdeling5_Artikel244)
- [art. 6:92 BW](https://wetten.overheid.nl/BWBR0005289/#Boek6_Titeldeel1_Afdeling9_Paragraaf4_Artikel92)
- [art. 6:94 BW](https://wetten.overheid.nl/BWBR0005289/#Boek6_Titeldeel1_Afdeling9_Paragraaf4_Artikel94)
- [art. 6:248 BW](https://wetten.overheid.nl/BWBR0005289/#Boek6_Titeldeel5_Afdeling4_Artikel248)
- [art. 7:900 BW](https://wetten.overheid.nl/BWBR0005290/#Boek7_Titeldeel15_Artikel900)

---

## Toelichting voor de gebruiker (verwijderen voor ondertekening)

**Opties.** Bij elke keuze staat de aanbevolen optie. Laat per keuze één optie staan en
verwijder de andere, inclusief de `<!-- optie -->`-markeringen.

**Statuten eerst.** Een aandeelhoudersovereenkomst bindt alleen de ondertekenaars. Aanbiedings-
plicht, blokkeringsregeling en leaver-verplichtingen horen ook in de statuten, anders kan een
overdracht in strijd met de SHA toch geldig zijn. Laat de notaris de statuten hierop afstemmen.

**Redelijkheid en billijkheid (art. 6:248 BW).** Een rechter kan strenge bepalingen, zoals een
bad-leaverprijs, een lange non-compete of een hoge boete (art. 6:94 BW), matigen of buiten
toepassing laten. Houd ze proportioneel.

**Checklist**

- [ ] Statuten afgestemd op artikelen 3, 4 en 5 (notaris).
- [ ] Gekwalificeerde besluiten passen bij de verhoudingen; een minderheid van 26% met
      vetorecht is een bewuste keuze.
- [ ] Vesting- en leaverregeling fiscaal getoetst (aanmerkelijk belang, lucratief belang).
- [ ] Holdings van oprichters zijn partij, en de oprichter persoonlijk voor artikel 6.
- [ ] Komen er investeerders bij, dan zijn ook voorkeursaandelen, liquidatievoorkeur en
      anti-verwatering nodig. Die zitten niet in deze oprichters-SHA.
