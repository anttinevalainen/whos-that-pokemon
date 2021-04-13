# TKT20002 - Ohjelmistotekniikka


# Who's that Pokémon -tunnistussovellus

Who's that Pokémon on sovellus, joka toimii perinteisen Pokémon-animen rinnalla esitettävien kuva-arvoitusten mukaisesti. Pelissä on tarkoitus tunnistaa kuvassa näkyvä Pokémon vain sen mustan siluetin perusteella ja syöttää sen nimi kirjoitusnäkymään. Käyttäjä saa pisteitä sen mukaan, kuinka nopeasti oikea vastaus syötetään.

Sovelluksessa on alustavasti sukupolvien 1-6 Pokémonit (721kpl) sekä näiden mahdolliset megaevoluutiot ja evoluutiohaaran sisällä tapahtuvat mahdolliset erikoismuodot. Sovelluksen perimmäinen tarkoitus on harjoitella Pokémonien nimien muistamista, mutta se voidaan myös mieltää peliksi. Kierroksen päätyttyä (Käyttäjän syötettyä väärän vastauksen tai ajastimen (10 sekuntia per kierros) päättyessä) käyttäjän on mahdollista tallentaa tuloksensa gamertagin (Kolme kirjainta) avulla.

## Huomio Python-versiosta

Sovellus on luotu ja testattu Pythonin versiolla 3.9.2.

## Dokumentaatio

- *[Sovelluksen kansio](https://github.com/anttinevalainen/ot-harjoitustyo/tree/main/dokumentaatio)*\
- *[Tuntikirjanpito](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)*\
- *[Sovelluksen vaatimusmäärittely](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)*

## Asennus

1. Sovelluksen riippuvuudet (dependencies) sennetaan suorittamalla juurikansiossa komento:

```bash
poetry install
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

Sovelluksen testikattavuusraportti generoidaan suorittamalla komento:

```bash
poetry run invoke coverage-report
```
