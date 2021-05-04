# Sovellusarkkitehtuuri

## Rakenne

Ohjelman pakkausrakenne on seuraava:

*Interface-osio* käsittelee graafisen käyttöliittymän ohjelmakoodin, kuten sovelluksen eri sivut sekä graafiseen liittymään kuuluvien osioiden luomisen (create_widget.py) \
\
*Data-osio* kattaa sisällään sovelluksen vaatiman datan, kuten tietokannat sekä kuvat, joiden pohjalta sovellus toimii. Lisäksi data_handling.py on vastuussa data-kansiossa olevien tiedostojen käsittelemisestä \
\
*Services-osio* vastaa pelaajan tietojen tallennuksesta sekä sovelluslogiikasta \
\
*Gameplay-osio* vastaa sovelluksen tietokohteista, joihin kuuluu käyttäjä ja gamemode


## Käyttöliittymä

Käyttöliittymässä on viisi näkymää:

- Etusivu (Suunnistus pelin aloittamiseen, leaderboardsiin tai sovelluksen sulkeminen)
- Uuden peliprofiilin ja gamemoden luominen
- Pelivaihe
- Game Over -sivu, josta pelaaja lähettää tuloksensa leaderboardsiin
- Leaderboard, eli hiscores-näkymä, joka näyttää 9 parhaimmat tulokset

Jokainen viidestä näkymästä on luotu omana luokkanaan. Sovellus näyttää kerrallaan vain yhden pelinäkymän ja niiden välillä tapahtuva suunnistus tapahtuu UI-luokassa.\
Sovelluksessa tapahtuvat muutokset käsitellään data_handling.py -tiedoston sisältämissä funktioissa sekä interface-kansion create_widget.py -funktioiden avulla

## Sovelluslogiikka

Oheinen diagrammi osoittaa karkeasti sovelluksen logiikan



## Päätoiminnallisuudet

Alla oleva sekvenssidiagrammi kuvaa sovelluksen toimintaa pelin aloituksesta ensimmäiseen väärään vastaukseen asti:
<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/sequential_diagram.jpg>
