# TKT20002 - Ohjelmistotekniikka

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/playpage.PNG width="320" height="240">

# Who's that Pokémon -tunnistussovellus

Who's that Pokémon on sovellus, joka toimii perinteisen Pokémon-animen rinnalla esitettävien kuva-arvoitusten mukaisesti.

Pelissä on tarkoitus tunnistaa kuvassa näkyvä Pokémon vain sen mustan siluetin perusteella ja syöttää sen nimi kirjoitusnäkymään. Käyttäjä saa pisteitä sen mukaan, kuinka monella evoluutiolla sovellusta käytetään.

Sovelluksessa on sukupolvien 1-8 Pokémonit (898kpl). Tavallisten evoluutioiden lisäksi Pokémoneista on evoluutiohaaran sisällä tapahtuvat mahdolliset erikoismuodot. Sukupolvien 1-8 lisäksi käyttäjän on mahdollista lisätä arvuuteltavien Pokémonien joukkoon mahdolliset mega- sekä gigantamax-evoluutiot sekä aluekohtaiset erikoisevoluutiot (Alola ja Galar).

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/wronganswer1.PNG width="320" height="240"> <img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/wronganswer2.PNG width="320" height="240">

Sovelluksen perimmäinen tarkoitus on harjoitella Pokémonien nimien muistamista, mutta se voidaan myös mieltää peliksi.\
\
Kierroksen päätyttyä (Käyttäjän syötettyä väärän vastauksen kolmesti kierroksen aikana tai kun Pokedexin kaikki Pokémonit on käyty läpi), mikäli kierroksella kerätyt pisteet riittävät, käyttäjän on mahdollista tallentaa tuloksensa huipputuloksiina.

Sovellus on luotu ja testattu Pythonin versiolla 3.9.2.

## Dokumentaatio

- *[Sovelluksen kansio](https://github.com/anttinevalainen/ot-harjoitustyo/tree/main/dokumentaatio)*
- *[Tuntikirjanpito](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)*
- *[Sovelluksen vaatimusmäärittely](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)*
- *[Sovellusarkkitehtuuri](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)*
- *[Sovelluksen käyttöohjeet](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/ohjeet.md)*

## Releaset

- *[Release 1](https://github.com/anttinevalainen/ot-harjoitustyo/releases/tag/Viikko5)*
- *[Release 2](https://github.com/anttinevalainen/ot-harjoitustyo/releases/tag/Viikko6)*
- *[Final Release](https://github.com/anttinevalainen/ot-harjoitustyo/releases/tag/FinalRelease)*

## Asennus

1. Sovelluksen riippuvuudet (dependencies) sennetaan suorittamalla juurikansiossa komento:

```bash
poetry ínstall
```

2. Sovellus voidaan käynnistää komennolla:

```bash
poetry run invoke start
```


## Testaus

Sovelluksen testit suoritetaan komennolla:

```bash
poetry run invoke test
```

## Testikattavuus

Sovelluksen HTML-testikattavuusraportti generoidaan suorittamalla komento:

```bash
poetry run invoke coverage-report
```

### Pylint

Pylint suoritetaan komennolla:

```bash
poetry run invoke lint
```
