---
name: check-counterparty
description: Controleer een Nederlandse zakelijke tegenpartij in het KVK-handelsregister voordat je tekent of factureert. Gebruik dit bij vragen als "bestaat dit bedrijf", "mag deze persoon tekenen", "klopt dit KVK-nummer" of als onderdeel van een contractreview.
---

# Tegenpartij controleren (NL)

Gebruik de `kvk` MCP-server. Zonder die server: zeg dat de check niet kan draaien en verwijs
naar <https://www.kvk.nl/zoeken/>. Raad niets.

## Werkwijze

1. Zoek op KVK-nummer, of anders op naam en plaats. Meerdere treffers: toon ze en laat kiezen.
2. Haal het basisprofiel op en rapporteer:
   - statutaire naam, handelsnamen, rechtsvorm, KVK-nummer, vestigingsadres;
   - datum inschrijving, en of de inschrijving actief is;
   - recente mutaties (naamswijziging, adreswijziging, opheffing) als de server die levert.
3. **Bevoegdheid.** Het basisprofiel van de KVK API bevat geen functionarissen. Zeg dat
   tekenbevoegdheid alleen blijkt uit een uittreksel (betaald, via kvk.nl) en welke vraag de
   gebruiker aan de tegenpartij kan stellen: "Wie is bestuurder en is die alleen/zelfstandig
   bevoegd?"
4. **Rode vlaggen**, elk met reden:
   - naam in het contract wijkt af van statutaire naam;
   - inschrijving jonger dan drie maanden bij een grote opdracht;
   - adres is een virtueel kantoor of afwijkt van het contract;
   - rechtsvorm is een eenmanszaak of vof terwijl het contract een BV noemt.
5. Eindig met: **OK**, **Navragen** of **Niet tekenen**, en waarom in één zin.
