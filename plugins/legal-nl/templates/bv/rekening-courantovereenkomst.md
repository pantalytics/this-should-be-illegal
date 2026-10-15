---
title: Rekening-courantovereenkomst (BV en aandeelhouder)
jurisdiction: NL
entity: bv
language: nl
version: 0.1.0
status: draft
reviewed_by: null
last_checked: 2026-10-15
legal_basis:
  - BW 2:239
  - BW 2:247
  - BW 6:140
  - BW 7:129
  - BW 7:129e
  - Wet IB 2001 4.14a
fields:
  vennootschap_naam: Statutaire naam van de BV
  vennootschap_kvk: KVK-nummer van de BV
  vennootschap_vertegenwoordiger:
    label: Wie tekent namens de BV
    suggestie: een andere bestuurder, of een persoon die de AVA daartoe aanwijst
  rekeninghouder:
    label: Naam, KVK-nummer of adres van de aandeelhouder of holding
    suggestie: "Jansen Holding B.V., KVK 12345678, vertegenwoordigd door P. Jansen"
  ingangsdatum:
    label: Ingangsdatum
    suggestie: datum van ondertekening
  limiet:
    label: Maximaal saldo in euro, in beide richtingen
    suggestie: "50.000"
  rente_vast:
    label: Vaste rente per jaar
    suggestie: "5%"
  rente_opslag:
    label: Opslag boven de referentierente
    suggestie: "2,5%"
  plaats: Plaats van ondertekening
  datum: Datum van ondertekening
options:
  richting:
    vraag: Wie mag schuldenaar worden?
    default: a
    keuzes:
      a: Beide kanten
      b: Alleen de BV
  rente:
    vraag: Welke rente geldt over het saldo?
    default: a
    keuzes:
      a: Vaste rente
      b: Variabele rente
---

> **Let op:** concept, opgesteld door een niet-jurist en grotendeels met AI geschreven. Geen
> juridisch advies. Laat dit document toetsen door een advocaat of notaris voordat je het
> gebruikt. Zie [DISCLAIMER.md](../../../../DISCLAIMER.md). *Verwijder dit blok voor ondertekening.*

# Rekening-courantovereenkomst

**Partijen**

1. **{{vennootschap_naam}}**, ingeschreven in het handelsregister onder nummer
   {{vennootschap_kvk}}, hierbij vertegenwoordigd door {{vennootschap_vertegenwoordiger}}
   (de **Vennootschap**); en
2. **{{rekeninghouder}}** (de **Rekeninghouder**).

## Overwegende dat

- de Rekeninghouder aandeelhouder of bestuurder van de Vennootschap is, of daaraan gelieerd;
- tussen partijen over en weer betalingen plaatsvinden, zoals voorgeschoten kosten,
  managementvergoedingen en dividend;
- partijen deze posten in één rekening willen opnemen en alleen het saldo verschuldigd willen
  laten zijn (artikel 6:140 BW).

## 1. Rekening-courant

1.1 Met ingang van {{ingangsdatum}} houdt de Vennootschap een rekening-courant bij waarin alle
onderlinge geldvorderingen en geldschulden worden opgenomen. Deze worden van rechtswege
verrekend; op ieder moment is alleen het saldo verschuldigd (artikel 6:140 lid 1 BW).

1.2 Voor zover het saldo een geldlening vormt, is titel 7.2c BW (geldlening) van toepassing,
behalve waar deze overeenkomst daarvan afwijkt.

## 2. Limiet

> **Kies één:** Wie mag schuldenaar worden?

<!-- optie richting=a -->
**Optie A: Beide kanten** *(aanbevolen: meest flexibel)*

2.1 Het saldo bedraagt in beide richtingen ten hoogste EUR {{limiet}}. Een hoger saldo vereist
voorafgaande schriftelijke instemming van beide partijen.
<!-- /optie -->

<!-- optie richting=b -->
**Optie B: Alleen de BV** *(de aandeelhouder financiert de BV, nooit andersom)*

2.1 Alleen de Vennootschap kan schuldenaar zijn. Het saldo ten laste van de Vennootschap
bedraagt ten hoogste EUR {{limiet}}. Een saldo ten laste van de Rekeninghouder wordt binnen
30 dagen aangezuiverd.
<!-- /optie -->

## 3. Rente

> **Kies één:** Welke rente geldt over het saldo?

<!-- optie rente=a -->
**Optie A: Vaste rente** *(aanbevolen: eenvoudig te administreren)*

3.1 Over het saldo is een rente verschuldigd van {{rente_vast}} per jaar, berekend over het
dagelijkse saldo. Dezelfde rente geldt in beide richtingen.
<!-- /optie -->

<!-- optie rente=b -->
**Optie B: Variabele rente** *(volgt de markt)*

3.1 Over het saldo is een rente verschuldigd gelijk aan de 3-maands Euribor, met een minimum
van 0%, vermeerderd met {{rente_opslag}} per jaar, berekend over het dagelijkse saldo. De
rente wordt per kwartaal aangepast aan de Euribor op de eerste werkdag van dat kwartaal.
<!-- /optie -->

3.2 De rente wordt per 31 december bijgeschreven op de rekening-courant.

## 4. Afrekening

4.1 De Vennootschap sluit de rekening-courant jaarlijks per 31 december af en deelt het saldo
binnen drie maanden mee aan de Rekeninghouder, met de posten waaruit het bestaat
(artikel 6:140 lid 2 BW).

4.2 Protesteert de Rekeninghouder niet binnen 30 dagen na ontvangst, dan geldt het saldo als
tussen partijen vastgesteld (artikel 6:140 lid 3 BW).

## 5. Duur en opeisbaarheid

5.1 Deze overeenkomst geldt voor onbepaalde tijd. Elke partij kan haar schriftelijk opzeggen
met een termijn van drie maanden. Het saldo is opeisbaar bij het einde van de overeenkomst.

5.2 Het saldo is direct opeisbaar als een partij in staat van faillissement wordt verklaard,
surseance van betaling aanvraagt, of als de Rekeninghouder geen aandeelhouder of bestuurder
van de Vennootschap meer is.

5.3 Een saldo boven de limiet is opeisbaar binnen zes weken na een verzoek daartoe
(artikel 7:129e BW).

## 6. Slotbepalingen

6.1 Op deze overeenkomst is Nederlands recht van toepassing.

6.2 Geschillen worden voorgelegd aan de bevoegde rechter in het arrondissement waar de
Vennootschap statutair is gevestigd.

Aldus overeengekomen en ondertekend te {{plaats}} op {{datum}}.

| Namens de Vennootschap | De Rekeninghouder |
| ---------------------- | ----------------- |
|                        |                   |

## Wettelijke grondslag

Actuele tekst op wetten.overheid.nl:

- [art. 2:239 BW](https://wetten.overheid.nl/jci1.3:c:BWBR0003045&boek=2&titeldeel=5&artikel=239)
- [art. 2:247 BW](https://wetten.overheid.nl/jci1.3:c:BWBR0003045&boek=2&titeldeel=5&artikel=247)
- [art. 6:140 BW](https://wetten.overheid.nl/jci1.3:c:BWBR0005289&boek=6&titeldeel=1&afdeling=12&artikel=140)
- [art. 7:129 BW](https://wetten.overheid.nl/jci1.3:c:BWBR0005290&boek=7&titeldeel=2c&artikel=129)
- [art. 7:129e BW](https://wetten.overheid.nl/jci1.3:c:BWBR0005290&boek=7&titeldeel=2c&artikel=129e)
- [art. 4.14a Wet IB 2001](https://wetten.overheid.nl/jci1.3:c:BWBR0011353&artikel=4.14a)

---

## Toelichting voor de gebruiker (verwijderen voor ondertekening)

**Wanneer gebruik je dit?** Voor het lopende verkeer tussen een BV en haar DGA of holding:
voorgeschoten kosten, opnames, vergoedingen. Gaat het om één vast bedrag met een
aflossingsschema, gebruik dan de *geldleningsovereenkomst*.

**Opties.** Laat per keuze één optie staan en verwijder de andere, inclusief de
`<!-- optie -->`-markeringen.

**Checklist**

- [ ] **Excessief lenen.** Schulden van de DGA en partner aan de eigen BV boven
      € 500.000 op 31 december worden belast als inkomen uit aanmerkelijk belang
      (art. 4.14a Wet IB 2001). Eigenwoningschulden tellen onder voorwaarden niet mee.
- [ ] **Zakelijke rente.** De Belastingdienst toetst of de rente is wat onafhankelijke
      partijen zouden afspreken. Een onzakelijke lening aan de DGA kan als verkapte uitkering
      worden gezien. Laat de rente fiscaal toetsen.
- [ ] **Tegenstrijdig belang.** Is de Rekeninghouder ook bestuurder, dan neemt hij niet deel
      aan het bestuursbesluit; zonder andere bestuurders beslist de AVA (art. 2:239 lid 6 BW).
- [ ] **Enig aandeelhouder?** Vertegenwoordigt die de BV bij deze overeenkomst, dan moet
      zij schriftelijk zijn, anders is zij vernietigbaar (art. 2:247 BW).
- [ ] Rekening-courant per jaar aansluiten met de boekhouding van beide partijen.
