# Sovellusarkkitehtuuri

## Rakenne

Ohjelman pakkausrakenne on seuraava:

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/logics.png>

*[Interface-osio](https://github.com/anttinevalainen/ot-harjoitustyo/tree/main/src/interface)* käsittelee graafisen käyttöliittymän ohjelmakoodin, kuten sovelluksen eri sivut sekä graafiseen liittymään kuuluvien osioiden luomisen ([create_widget.py](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/interface/create_widget.py)) \
\
*[Data-osio](https://github.com/anttinevalainen/ot-harjoitustyo/tree/main/src/data)* kattaa sisällään sovelluksen vaatiman datan, kuten tietokannat sekä kuvat, joiden pohjalta sovellus toimii. Lisäksi [data_handling.py](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/data/data_handling.py) on vastuussa data-kansiossa olevien tiedostojen käsittelemisestä \
\
*[Services-osio](https://github.com/anttinevalainen/ot-harjoitustyo/tree/main/src/services)* vastaa pelaajan tietojen tallennuksesta sekä sovelluslogiikasta \
\
*[Gameplay-osio](https://github.com/anttinevalainen/ot-harjoitustyo/tree/main/src/gameplay)* vastaa sovelluksen tietokohteista, joihin kuuluu käyttäjä ja gamemode


## Käyttöliittymä

Käyttöliittymässä on viisi näkymää:

- [Etusivu](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/interface/index.py) (Suunnistus pelin aloittamiseen, leaderboardsiin tai sovelluksen sulkeminen)
- [Gamertag page](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/interface/gamertag_input.py) - Uuden peliprofiilin ja gamemoden luominen
- [Pelinäkymä](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/interface/play.py)
- [Game over -sivu](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/interface/game_over.py), josta pelaaja lähettää tuloksensa leaderboardsiin
- [Hiscores](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/interface/hiscores.py), joka näyttää 9 parhaimmat tulokset

Jokainen viidestä näkymästä on luotu omana luokkanaan. Sovellus näyttää kerrallaan vain yhden pelinäkymän ja niiden välillä tapahtuva suunnistus tapahtuu [UI-luokassa](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/interface/ui.py).\
Sovelluksessa tapahtuvat muutokset käsitellään [data_handling.py](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/data/data_handling.py) -tiedoston sisältämissä funktioissa sekä [interface-kansion](https://github.com/anttinevalainen/ot-harjoitustyo/tree/main/src/interface) [create_widget.py](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/interface/create_widget.py) -funktioiden avulla

## Sovelluslogiikka

Oheinen diagrammi osoittaa sovelluksen pakkauslogiikan:

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/packaging.png>

## Päätoiminnallisuudet

Alla oleva sekvenssidiagrammi kuvaa sovelluksen toimintaa pelin aloituksesta ensimmäiseen väärään vastaukseen asti:
<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/sequential_diagram.png>
