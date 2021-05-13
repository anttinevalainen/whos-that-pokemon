# Käyttöohje

(Sovelluksen viimeisin [release](https://github.com/anttinevalainen/ot-harjoitustyo/releases/tag/FinalRelease) löytyy [täältä](https://github.com/anttinevalainen/ot-harjoitustyo/releases). Lataa release klikkaamalla kohtaa _Source code_.)


## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, käyttäjän tulee asentaa riippuvuudet komennolla:

```bash
poetry install
```

Muita suoritettavia alustustoimenpiteitä ei ole. Ohjelma käynnistetään komennolla:

```
poetry run invoke start
```

## Etusivu

Sovelluksen ensimmäinen näkymä on etusivu, jossa käyttäjä voi suunnistaa kierroksen aloitukseen, huipputuloksiin tai sulkea sovelluksen:

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/frontpage.PNG width="320" height="240">

Kierroksen voi aloittaa klikkaamalla Play-painiketta

## Pelaaja- ja peliprofiilin luominen

Etusivulta play-painikkeella siirrytään käyttäjäprofiilien luomiseen.

Käyttäjä ilmoittaa kolmikirjaimisen gamertaginsa ja valitsee ne generaatiot, joilla haluaa sovellusta käyttää.\
Alla olevassa esimerkissä gamertagiksi tulee 'OWO' ja sovellus toimii generaatioilla 1, 2, 3, 6, 7, 8 sekä Alolan- ja Galarian-muodoilla

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/gametag.PNG width="320" height="240">

Mikäli käyttäjän gamertag ei kelpaa (sisältää esimerkiksi numeroita tai erikoismerkkejä), sovellus ilmoittaa siitä.\
Sovellus ilmoittaa myös, mikäli käyttäjä ei ole valinnut yhtäkään generaatiota.

Sovelluksen profiilit (Player, gamemode ja pokedex) luodaan 'Choose!'-painikkeella. Mikäli valinnat kelpaavat, ruutuun ilmestyy 'Play!'-painike, jolla kierros aloitetaan.

Samassa näkymässä on myös mahdollista ottaa käyttöön Revision mode, joka näyttää oikeat vastaukset näytöllä. Tällöin kuitenkaan tuloksen lähettäminen hiscoreihin ei ole mahdollista.

## Pelinäkymä

Sovelluksen päänäkymässä käyttäjän eteen ilmestyy täysin musta siluetti, joka esittää satunnaista pokemonia niistä generaatioista, jotka käyttäjä on valinnut. Käyttäjän tarkoitus on arvata mikä Pokemon on kyseessä.

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/playpage.PNG width="320" height="240"> <img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/correct.PNG width="320" height="240">

Arvaus kirjoitetaan siluetin alla olevaan ruutuun ja lähetetään huutomerkkinapista tai enteriä painamalla. Sovellus ilmoittaa, mikäli käyttäjän\ arvaus osui oikeaan ja kertoo mahdollisen erikoismuodon nimen.

Vastaavasti sovellus ilmoittaa myös väärästä vastauksesta ja kertoo tällöinkin oikean vastauksen.

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/wronganswer1.PNG width="320" height="240"> <img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/wronganswer2.PNG width="320" height="240">

Väärin vastatessa käyttäjä menettää yhden kolmesta elämästään, eli kierroksen aikana on mahdollista vastata väärin kolmesti ennen sen päättymistä.

Molemmissa tapauksissa seuraavaan vaiheeseen pääsee enteriä painamalla tai klikkaamalla 'Next!'-painiketta. Mikäli käyttäjällä on elämiä jäljellä, arpoo sovellus uuden siluetin arvattavaksi. Jokaisen arvauksen jälkeen, kyseinen Pokémon poistuu pokedexilta, eli samat kuvat eivät näy kierrosksen aikana. Toiminto ei kuitenkaan poista saman Pokémonin erikoismuotoja, eli käyttäjän eteen voi osua myöhemmin esimerkiksi Zygarden toinen evoluutiohaaran sisäinen muoto, kun yksi on jo kierroksella nähty.

## Esimerkkejä Pokemonien nimeämisistä ja oikeista vastauksista:

Käyttäjän syöttämä vastaus tai sen vertaaminen Pokémonin nimeen ei ole case-sensitive, eli esimerkiksi pelkkien pienten kirjainten käyttö on sallittua. Myöskään erikoismerkeistä tai välilyönneistä ei tarvitse välittää.

| Täysi nimi                           | Hyväksytty vastaus    | Sovelluksen ilmoitus                                 |
| :----:                               |:-----                 | :-----                                               |
| Horsea                               | Horsea                | Correct! It's HORSEA!                                |
| Aegislash (Shield)                   | Aegislash             | Correct! It's Aegislash (Shield)!                    |
| Aegislash (Blade)                    | Aegislash             | Correct! It's Aegislash (Blade)!                     |
| Mega Venusaur                        | Mega Venusaur         | Correct! It's MEGA VENUSAUR!                         |
| Mega Mewtwo (X)                      | Mega Mewtwo           | Correct! It's MEGA MEWTWO (X)!                       |
| Mime Jr.                             | Mime jr               | Correct! It's MIME JR.!                              |
| Mime Jr.                             | mimejr                | Correct! It's MIME JR.!                              |
| Mime Jr.                             | Mime jr.              | Correct! It's MIME JR.!                              |
| Mime Jr.                             | mimejr.               | Correct! It's MIME JR.!                              |
| Mime Jr.                             | Mime.jr.              | Correct! It's MIME JR.!                              |
| Gigantamax gengar                    | Gigantamax Gengar     | Correct! It's GIGANTAMAX GENGAR!                     |
| Alolan Persian                       | Alolan Persian        | Correct! It's ALOLAN PERSIAN!                        |
| Galarian Ponyta                      | Galarian Ponyta       | Correct! It's GALARIAN PONYTA!                       |
| Gigantamax Urshifu (Single Strike)   | Gigantamax Urshifu    | Correct! It's GIGANTAMAX URSHIFU (SINGLE STRIKE)!    |

Joillakin pokemoneilla on evoluutiohaaran sisäisiä erikoismuotoja, jotka ilmoitetaan sovelluksessa Pokemonin nimen perässä sulkeissa. Näitä osioita ei tarvitse osata pelatessa ja esimerkiksi 'Aegislash (Blade)' arvatessa sovellus ilmoittaa väärästä vastauksesta.\

Kun sovelluksessa on valittu myös mega- ja gigantamax-evoluutiot sekä regional-muodot, arvauksessa tulee olla myös kyseisen erikoisevoluution nimi. Esimerkiksi Gigantamax Gengarin kohdalla pelkkä 'Gengar' on väärä vastaus.

Esimerkiksi Mewtwolla ja Charizardilla on kahdenlaiset megaevoluutiot (X ja Y). Näissä tapauksissa sovelluksessa pätee molemmat yllänäkyvät huomiot, eli oikea vastaus on Mega Mewtwo tai Mega Charizard.

Mikäli arvailu vaikuttaa monimutkaiselta, suosittelen aloittamaan käymällä kierroksen tai pari läpi revision modea käyttäen!

## Game Over

Käyttäjän arvatessa väärin, pelinäkymässä olevat sydämet muuttuvat yksi kerrallaan harmaiksi. Kun arvauksia on osunut kolme kertaa kierroksen aikana väärin, peli päättyy.

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/hearts.png width="354" height="127">

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/sendhiscore.png width="320" height="240">

Mikäli pelaajalla on tarpeeksi pisteitä leaderboardsia varten, sovellus ilmoittaa tästä ja pelaajan tulos on mahdollista tallentaa 'Send hiscore' -napista. Tämän jälkeen pelaajan on mahdollista palata etusivulle ja aloittaa uusi peli, esimerkiksi suuremmalla määrällä generaatioita.

Jos pelaajalla ei ole tarpeeksi pisteitä, ei tuloksen lähettäminen ole mahdollista ja uuden pelin voi aloittaa ruutuun ilmestyvää 'Try again' -nappia painamalla.

## Leaderboards

Etusivun 'Hiscores'-napista siirrytään huipputuloksiin, jonne tallennetaan yhdeksän parhaan tuloksen saaneen pelaajan tulokset.

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/hiscores.png width="320" height="240">

