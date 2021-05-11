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
Sovelluksessa tapahtuvat muutokset käsitellään [services](https://github.com/anttinevalainen/ot-harjoitustyo/tree/main/src/services) -kansion sisältämissä tiedostoissa ja funktioissa sekä [interface-kansion](https://github.com/anttinevalainen/ot-harjoitustyo/tree/main/src/interface) [create_widget.py](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/interface/create_widget.py) -funktioiden avulla.

Kun sovelluksessa luodaan uusi gamemode-olio, räätälöidään sen avulla [data-kansiossa](https://github.com/anttinevalainen/ot-harjoitustyo/tree/main/src/data) olevan [pokedex.csv](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/data/pokedex.csv) -tiedoston pohjalta uusi dataframe, joka sisältää vain käyttäjän valitsemat generaatiot. Käyttäjän arvatessa Pokémoneja, kierroksen Pokedex-oliosta poistetaan rivejä. Huipputuloksia tallennettaessa sovellus tarkistaa aina [hiscores.csv](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/data/hiscores.csv) -tiedoston olemassaolon ja luo uuden tiedoston, mikäli sitä ei ennestään löydy tai jos tiedostonimellä löytyvä taulukko on vääränkokoinen.

## Sovelluslogiikka

Sovellus varastoi tietoa neljään eri luokkaan, jotka ovat:
- [Player](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/gameplay/player.py), joka pitää sisällään käyttäjän gamertagin, gamemoden ja pokedexin sekä hallinnoi pistetilannetta ja käyttäjän elämiä.
- [Gamemode](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/gameplay/gamemode.py), joka tallentaa käyttäjän valikoimat generaatiot sekä revision-moden
- [Pokedex](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/gameplay/pokedex.py), joka hallinnoi kierroksen Pokedexiä ja valikoi sieltä Pokémoneja
- [Pokemon](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/gameplay/pokemon.py), joka kuvaa pokedex.py:ssä luotua satunnaista Pokémonia

Oheinen diagrammi osoittaa sovelluksen pakkauslogiikan:
<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/packaging.png>

### Tiedostot

Sovellus lukee data-kansiossa olevia [hiscores.csv](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/data/hiscores.csv) ja [pokedex.csv](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/data/pokedex.csv) tiedostoja. Hiscores.csv-tiedostoa sovellus myös päivittää, mikäli käyttäjän pistemäärät ovat tarpeeksi korkeita.

Sovellus lukee csv-tiedostoja seuraavassa muodossa:

```
POKEDEX.CSV
id,pdno,name,secondary_name,gen
'809giga',809,'Gigantamax Melmetal','-','7giga'
'809',809,'Melmetal','-','7'
'810',810,'Grookey','-','8'
```

```
HISCORES.CSV
gamertag,points,correct,gens
'III',1150,23,1
'OIO',6000,10,12
'OWO',3600,9,8
```

Eli yksittäisestä pokemonista tallennetaan uniikki id, kansallinen Pokedex-numero, yksinkertainen nimi, nimen jatko-osa, sekä generaatio. Solujen arvot erotellaan pilkulla (,).

Yksittäisestä hiscoresta tallennetaan gamertag, pistemäärä, oikeiden vastausten määrä sekä generaatioiden määrä. Solujen arjot erotellaan pilkulla (,).

## Päätoiminnallisuudet

Sovelluksen päätoiminnallisuus tapahtuu play-käyttöliittymäsivulla, johon sovellus esittää satunnaisia Pokémoneja, kutsuu [service-kansion](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/services) toiminnallisuuksia esimerkiksi tarkistamaan vastauksia ja luomaan photoimage-objekteja, joilla [create_widget.py:n](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/src/interface/create_widget.py) funktiot luo pelinäkymään kuvia.

Esimerkiksi alla oleva sekvenssidiagrammi kuvaa sovelluksen toimintaa pelin aloituksesta ensimmäiseen väärään vastaukseen asti:
<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/sequential_diagram.png>
