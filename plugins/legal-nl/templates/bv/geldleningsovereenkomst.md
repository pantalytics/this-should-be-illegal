---
title: Geldleningsovereenkomst (zakelijke lening aan een BV)
jurisdiction: NL
entity: bv
language: nl
version: 0.1.0
status: draft
reviewed_by: null
last_checked: 2026-10-15
legal_basis:
  - BW 2:239
  - BW 3:237
  - BW 6:119a
  - BW 7:129
  - BW 7:129c
  - BW 7:850
  - BW 7:857
fields:
  uitlener:
    label: Naam, KVK-nummer of adres van de uitlener
    suggestie: "Jansen Holding B.V., KVK 12345678, vertegenwoordigd door P. Jansen"
  lener_naam: Statutaire naam van de BV die leent
  lener_kvk: KVK-nummer van de lener
  lener_vertegenwoordiger: Bestuurder die namens de lener tekent
  hoofdsom:
    label: Geleend bedrag in euro
    suggestie: "100.000"
  verstrekkingsdatum: Datum waarop het geld wordt overgemaakt
  rekeningnummer: IBAN van de lener
  rente:
    label: Rente per jaar
    suggestie: "6%"
  looptijd_maanden:
    label: Looptijd in maanden
    suggestie: "60"
  borg_naam: Naam en adres van de borg
  borg_maximum:
    label: Maximum waarvoor de borg instaat, in euro
    suggestie: gelijk aan de hoofdsom
  plaats: Plaats van ondertekening
  datum: Datum van ondertekening
options:
  aflossing:
    vraag: Hoe wordt de lening terugbetaald?
    default: a
    keuzes:
      a: Lineair per maand
      b: Annuïteit per maand
      c: Ineens aan het einde
  zekerheid:
    vraag: Welke zekerheid krijgt de uitlener?
    default: a
    keuzes:
      a: Geen
      b: Borgtocht
      c: Pandrecht
  achterstelling:
    vraag: Gaat de lening voor of na andere schuldeisers?
    default: a
    keuzes:
      a: Niet achtergesteld
      b: Achtergesteld
---

# Geldleningsovereenkomst

**Partijen**

1. **{{uitlener}}** (de **Uitlener**); en
2. **{{lener_naam}}**, ingeschreven in het handelsregister onder nummer {{lener_kvk}},
   hierbij vertegenwoordigd door {{lener_vertegenwoordiger}} (de **Lener**).

## 1. Lening

1.1 De Uitlener leent aan de Lener een bedrag van EUR {{hoofdsom}} (de **Hoofdsom**), en de
Lener verbindt zich een overeenkomstig bedrag terug te betalen (artikel 7:129 BW).

1.2 De Uitlener maakt de Hoofdsom op {{verstrekkingsdatum}} over op rekening
{{rekeningnummer}} van de Lener.

1.3 De Lener gebruikt de Hoofdsom alleen voor de uitoefening van haar onderneming.

## 2. Rente

2.1 Over het uitstaande bedrag is een rente verschuldigd van {{rente}} per jaar
(artikel 7:129c lid 2 BW), berekend per dag en maandelijks achteraf te betalen.

2.2 Betaalt de Lener niet op tijd, dan is over het achterstallige bedrag de wettelijke
handelsrente verschuldigd (artikel 6:119a BW) in plaats van de rente uit artikel 2.1.

## 3. Aflossing

> **Kies één:** Hoe wordt de lening terugbetaald?

<!-- optie aflossing=a -->
**Optie A: Lineair per maand** *(aanbevolen: schuld daalt snel, rente daalt mee)*

3.1 De Lener lost de Hoofdsom af in {{looptijd_maanden}} gelijke maandelijkse termijnen, voor
het eerst één maand na verstrekking, telkens met de rente over die maand.
<!-- /optie -->

<!-- optie aflossing=b -->
**Optie B: Annuïteit per maand** *(vaste maandlast)*

3.1 De Lener betaalt in {{looptijd_maanden}} maanden een gelijkblijvend maandbedrag aan rente
en aflossing samen, berekend op basis van de Hoofdsom en de rente uit artikel 2.1, voor het
eerst één maand na verstrekking. De Uitlener stelt bij verstrekking een aflossingsschema op.
<!-- /optie -->

<!-- optie aflossing=c -->
**Optie C: Ineens aan het einde** *(meeste ruimte voor de Lener, meeste risico voor de
Uitlener)*

3.1 De Lener lost de Hoofdsom ineens af, {{looptijd_maanden}} maanden na verstrekking. De rente
wordt maandelijks betaald.
<!-- /optie -->

3.2 De Lener mag altijd geheel of gedeeltelijk vervroegd aflossen, zonder boete.

## 4. Opeisbaarheid

4.1 Het uitstaande bedrag met rente is direct en volledig opeisbaar als:

a. de Lener een betaling meer dan 30 dagen na de vervaldatum nog niet heeft gedaan, ook na
   schriftelijke aanmaning;
b. de Lener in staat van faillissement wordt verklaard of surseance van betaling aanvraagt;
c. de Lener wordt ontbonden of haar onderneming geheel of grotendeels staakt of
   overdraagt;
d. de Lener een wezenlijke verplichting uit deze overeenkomst niet nakomt.

## 5. Zekerheid

> **Kies één:** Welke zekerheid krijgt de uitlener?

<!-- optie zekerheid=a -->
**Optie A: Geen** *(gebruikelijk bij een lening van een aandeelhouder)*

5.1 Voor deze lening wordt geen zekerheid gesteld.
<!-- /optie -->

<!-- optie zekerheid=b -->
**Optie B: Borgtocht** *(een persoon staat in voor terugbetaling)*

5.1 {{borg_naam}} (de **Borg**) stelt zich als borg tegenover de Uitlener voor de nakoming
door de Lener van haar verplichtingen uit deze overeenkomst, tot een maximum van
EUR {{borg_maximum}} (artikel 7:850 BW). De Borg tekent deze overeenkomst mede.
<!-- /optie -->

<!-- optie zekerheid=c -->
**Optie C: Pandrecht** *(op voorraad, inventaris of vorderingen)*

5.1 De Lener verpandt aan de Uitlener tot zekerheid van deze lening haar huidige en
toekomstige inventaris, voorraden en vorderingen. Partijen leggen dit vast in een
afzonderlijke pandakte, die wordt geregistreerd of notarieel verleden (artikel 3:237 BW).
<!-- /optie -->

## 6. Achterstelling

> **Kies één:** Gaat de lening voor of na andere schuldeisers?

<!-- optie achterstelling=a -->
**Optie A: Niet achtergesteld** *(aanbevolen voor een externe uitlener)*

6.1 De vordering van de Uitlener staat gelijk met die van andere concurrente schuldeisers.
<!-- /optie -->

<!-- optie achterstelling=b -->
**Optie B: Achtergesteld** *(gebruikelijk bij een aandeelhouderslening; helpt bij de bank)*

6.1 De vordering van de Uitlener is achtergesteld bij alle huidige en toekomstige
vorderingen van andere schuldeisers van de Lener. Bij faillissement of vereffening wordt zij
pas voldaan nadat alle andere schuldeisers volledig zijn voldaan. De Lener betaalt rente en
aflossing alleen zolang zij daarna haar opeisbare schulden kan blijven betalen.
<!-- /optie -->

## 7. Slotbepalingen

7.1 Deze overeenkomst kan alleen schriftelijk worden gewijzigd. De Uitlener kan haar rechten
alleen met toestemming van de Lener overdragen.

7.2 Op deze overeenkomst is Nederlands recht van toepassing. Geschillen worden voorgelegd
aan de bevoegde rechter in het arrondissement waar de Lener statutair is gevestigd.

Aldus overeengekomen en ondertekend te {{plaats}} op {{datum}}.

| De Uitlener | Namens de Lener | De Borg (alleen bij optie 5B) |
| ----------- | --------------- | ----------------------------- |
|             |                 |                               |

## Wettelijke grondslag

Actuele tekst op wetten.overheid.nl:

- [art. 2:239 BW](https://wetten.overheid.nl/jci1.3:c:BWBR0003045&boek=2&titeldeel=5&artikel=239)
- [art. 3:237 BW](https://wetten.overheid.nl/jci1.3:c:BWBR0005291&boek=3&titeldeel=9&afdeling=2&artikel=237)
- [art. 6:119a BW](https://wetten.overheid.nl/jci1.3:c:BWBR0005289&boek=6&artikel=119a)
- [art. 7:129 BW](https://wetten.overheid.nl/jci1.3:c:BWBR0005290&boek=7&titeldeel=2c&artikel=129)
- [art. 7:129c BW](https://wetten.overheid.nl/jci1.3:c:BWBR0005290&boek=7&titeldeel=2c&artikel=129c)
- [art. 7:850 BW](https://wetten.overheid.nl/jci1.3:c:BWBR0005290&boek=7&titeldeel=14&artikel=850)
- [art. 7:857 BW](https://wetten.overheid.nl/jci1.3:c:BWBR0005290&boek=7&titeldeel=14&artikel=857)

---

## Toelichting voor de gebruiker (verwijderen voor ondertekening)

**Wanneer gebruik je dit?** Voor een lening van een vast bedrag aan een BV, van een
aandeelhouder, holding, familielid of andere zakelijke partij. Voor lopend onderling verkeer
tussen BV en DGA: gebruik de *rekening-courantovereenkomst*.

**Opties.** Laat per keuze één optie staan en verwijder de andere, inclusief de
`<!-- optie -->`-markeringen.

**Checklist**

- [ ] **Zakelijke rente.** Bij een lening tussen BV en aandeelhouder toetst de
      Belastingdienst of de voorwaarden zakelijk zijn. Laat dit fiscaal toetsen.
- [ ] **Tegenstrijdig belang.** Is de uitlener ook bestuurder van de lener, dan neemt hij
      niet deel aan het bestuursbesluit; zonder andere bestuurders beslist de AVA
      (art. 2:239 lid 6 BW).
- [ ] **Borgtocht door een particulier** (optie 5B): voor een borg die niet handelt in
      beroep of bedrijf gelden extra beschermingsregels (art. 7:857 e.v. BW). Die gelden niet
      als de borg bestuurder is van de lener en (met medebestuurders) de meerderheid van de
      aandelen heeft. Laat de borg de overeenkomst lezen en zelf tekenen.
- [ ] **Pandrecht** (optie 5C): de pandakte apart opstellen en registreren bij de
      Belastingdienst of laten passeren bij de notaris. Zonder registratie geen stil pandrecht.
- [ ] **Geld ophalen bij veel mensen?** Het aantrekken van terugbetaalbare gelden van het
      publiek is gereguleerd (Wft). Leen alleen van een kleine, bekende kring.
- [ ] Geld daadwerkelijk overmaken en het bewijs bewaren.
