---
name: check-counterparty
description: Controleer een zakelijke tegenpartij in de EU voordat je tekent of factureert, via het gratis btw-register VIES en de openbare KVK-zoekpagina. Gebruik dit bij vragen als "bestaat dit bedrijf", "klopt dit btw-nummer", "mag deze persoon tekenen" of als onderdeel van een contractreview.
---

# Tegenpartij controleren

Alleen open bronnen, zonder account of key.

## Werkwijze

1. **Btw-nummer (VIES).** Haal op:
   `https://ec.europa.eu/taxation_customs/vies/rest-api/ms/<LAND>/vat/<NUMMER>`,
   bijvoorbeeld `.../ms/NL/vat/NL123456789B01`. Rapporteer `isValid`, `name` en `address`.
   Werkt voor alle EU-landen. Geen btw-nummer bekend? Vraag erom; het staat op elke factuur.
2. **Handelsregister (NL).** Zoek op <https://www.kvk.nl/zoeken/?source=all&q=NAAM> en noem
   KVK-nummer, rechtsvorm, plaats en of de inschrijving actief is. Lukt het ophalen niet,
   geef de gebruiker de link en ga verder met wat je hebt.
3. **Bevoegdheid.** Wie mag tekenen staat alleen in een (betaald) KVK-uittreksel. Raad het
   niet. Geef de vraag mee die de gebruiker aan de tegenpartij stelt: "Wie is bestuurder, en
   is die alleen of zelfstandig bevoegd? Stuur een recent uittreksel mee."
4. **Rode vlaggen**, elk met reden:
   - naam in het contract wijkt af van de naam in VIES of KVK;
   - btw-nummer ongeldig;
   - adres wijkt af van het contract;
   - rechtsvorm is een eenmanszaak of vof terwijl het contract een BV noemt.
5. Eindig met **OK**, **Navragen** of **Niet tekenen**, en waarom in één zin.
