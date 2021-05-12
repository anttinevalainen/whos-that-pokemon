# Testausdokumentti

## Sovelluslogiikka

Sovelluslogiikasta vastaaville services-kansion tiedostoille on jokaiselle tehty omat testitiedostot ja -luokat:

| tiedosto            | testitiedosto            | testiluokka         |
| :----:              |:-----                    | :-----              |
| player_service.py   | player_service_test.py   | TestPlayerService   |
| gamemode_service.py | gamemode_service_test.py | TestGamemodeService |
| pokemon_service.py  | pokemon_service_test,py  | TestPokemonService  |

Vastaavasti myös tietokohteita varten on luotu omat testitiedostot ja -luokat

| tiedosto    | testitiedosto    | testiluokka  |
| :----:      |:-----            | :-----       |
| player.py   | player_test.py   | TestPlayer   |
| gamemode.py | gamemode_test.py | TestGamemode |
| pokemon.py  | pokemon_test,py  | TestPokemon  |
| pokedex.py  | pokedex_test.py  | TestPokedex  |

Huipputuloksien tallennusta varten tehdylle hiscore_service.py -tiedostolle on tehty oma testitiedosto ja -luokka

| tiedosto             | testitiedosto             | testiluokka          |
| :----:               |:-----                     | :-----               |
| hiscore_service.py   | hiscore_service_test.py   | TestHiscoreService   |

## Testauskattavuus

Käyttöliittymäkerrosta lukuunottamatta sovelluksen testauksen haarautumakattavuus on 99%

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/coverage.png>

Testaamatta jäivät vain sovelluksen käyttöliittymästä vastaavat interface-kansion funktiot ja luokat

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellusta on testattu sekä tilanteissa, joissa huipputuloksia varten luotu taulukko on ollut olemassa ja joissa sitä ei ole, jolloin ohjelma luo tyhjän taulukon automaattisesti, kun hiscores.csv -tiedostoa tarvitaan.
Data-kansion Pokedex.csv, joka kattaa 1085 riviä, on löydyttävä sovelluskansiosta jotta sovellus toimii toivotusti.

### Toiminnallisuudet

Toiminnallisuutta on testattu esimerkiksi syöttämällä vääriä arvoja ja arvoja väärässä muodossa, jolloin ohjelmisto huomauttaa niistä. Myös esimerkiksi erikoismerkkien, välilyöntien ja korostusten käyttöä on testattu ja huomioitu arvauksissa. Sovellus ei huomioi erikoismerkkejä, välilyöntejä ja korostuksia arvauksissa, esimerkiksi Eeveen kohdalla myös arvaus 'E é v ë è' hyväksytään.

## Sovellukseen jääneet laatuongelmat

- Sovellus vaatii toimiakseen pokedex-tietokannan olemassaolon, eli se on tallennettava sellaisenaan githubin repositoriosta
- Sovelluksen käyttämät tiedostosijainnit on kirjoitettu koodiin sellaisenaan, suorina yhteyksinä (esim src/data/hiscores.csv)
- Pylint ilmoittaa laatuongelmiksi svelluskoodissa olevat käyttämättömät muuttujat iteraatioista, uudelleenmääritellyt muuttujanimet sekä initin ulkopuoliset self.-muuttujat
