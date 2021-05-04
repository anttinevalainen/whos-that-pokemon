# Käyttöohje

(Sovelluksen viimeisin [release](https://github.com/ohjelmistotekniikka-hy/python-todo-app/releases) löytyy [täältä](https://github.com/anttinevalainen/ot-harjoitustyo/releases). Lataa release klikkaamalla kohtaa _Source code_.)


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

Sovelluksen ensimmäinen näkymä on etusivu, jossa käyttäjä voi suunnistaa pelin aloitukseen, huipputuloksiin tai sulkea sovelluksen:

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/frontpage.PNG width="320" height="240">

Pelin voi aloittaa klikkaamalla Play-painiketta

## Pelaaja- ja peliprofiilin luominen

Etusivulta play-painikkeella siirrytään peliprofiilien luomiseen.

Käyttäjä ilmoittaa kolmikirjaimisen pelaajanimensä ja valitsee ne generaatiot, joilla haluaa sovellusta käyttää.\
Alla olevassa esimerkissä pelaajanimeksi tulee 'AAA' ja pelataan generaatioilla 1,2,3,4 ja 6

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/gametag.PNG width="320" height="240">

Mikäli käyttäjän pelaajanimi ei kelpaa (sisältää esimerkiksi numeroita tai erikoismerkkejä), peli ilmoittaa siitä.\
Peli ilmoittaa myös, mikäli pelaaja ei ole valinnut yhtäkään generaatiota.

Pelaajaprofiilit luodaan 'Choose!'-painikkeella. Mikäli valinnat kelpaavat, ruutuun ilmestyy 'Play!'-painike, jolla peli aloitetaan.

Samassa näkymässä on myös mahdollista ottaa käyttöön Revision mode, joka näyttää oikeat vastaukset näytöllä. Tällöin kuitenkaan tuloksen lähettäminen ei ole mahdollista.

## Pelinäkymä

Pelinäkymässä käyttäjän eteen ilmestyy täysin musta siluetti, joka esittää satunnaista pokemonia niistä generaatioista, jotka pelaaja on valinnut.\
Pelaajan tarkoitus on arvata mikä Pokemon on kyseessä.

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/playpage.PNG width="320" height="240"> <img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/correct.PNG width="320" height="240">

Arvaus kirjoitetaan siluetin alla olevaan ruutuun ja lähetetään huutomerkkinapista tai enteriä painamalla. Sovellus ilmoittaa, mikäli käyttäjän\ arvaus osui oikeaan ja kertoo mahdollisen erikoismuodon nimen.

Vastaavasti sovellus ilmoittaa myös väärästä vastauksesta ja kertoo tällöinkin oikean vastauksen.

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/wronganswer1.PNG width="320" height="240"> <img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/wronganswer2.PNG width="320" height="240">

Väärin vastatessa pelaaja menettää yhden kolmesta elämästään, eli pelaajan on mahdollista vastata väärin kolmesti kierroksen aikana ennen pelin päättymistä.

Molemmissa tapauksissa seuraavaan vaiheeseen pääsee enteriä painamalla tai klikkaamalla 'Next!'-painiketta. Mikäli käyttäjällä on elämiä jäljellä, arpoo peli uuden siluetin arvattavaksi.

## Esimerkkejä Pokemonien nimeämisistä ja oikeista vastauksista:

Käyttäjän syöttämä vastaus tai sen vertaaminen pokemonin nimeen ei ole case sensitive, eli esimerkiksi pelkkien pienten kirjainten käyttö on sallittua. Myöskään erikoismerkeistä tai välilyönneistä ei tarvitse välittää.

| Täysi nimi        | Hyväksytty vastaus | Sovelluksen ilmoitus              |
| :----:            |:-----              | :-----                            |
| Horsea            | horsea             | Correct! It's HORSEA!             |
| Aegislash (Shield)| Aegislash          | Correct! It's Aegislash (Shield)! |
| Mega Venusaur     | mega Venusaur      | Correct! It's MEGA VENUSAUR!      |
| Mega Mewtwo (X)   | mega mewtwo        | Correct! It's MEGA MEWTWO (X)!    |
| Mime Jr.          | Mime jr            | Correct! It's MIME JR.!           |
| Mime Jr.          | mimejr             | Correct! It's MIME JR.!           |
| Mime Jr.          | Mime jr.           | Correct! It's MIME JR.!           |
| Mime Jr.          | mimejr.            | Correct! It's MIME JR.!           |
| Mime Jr.          | Mime.jr.           | Correct! It's MIME JR.!           |

Joillakin pokemoneilla on evoluutiohaaran sisäisiä erikoismuotoja, jotka ilmoitetaan sovelluksessa Pokemonin nimen perässä sulkeissa. Näitä osioita ei tarvitse osata pelatessa ja esimerkiksi 'Aegislash (Sword)' arvatessa sovellus ilmoittaa väärästä vastauksesta.\
\
Joillakin pokemoneilla on oma megaevoluutio, joka täytyy ottaa huomioon sovellusta käytettäessä. Esimerkiksi pelkästään 'Blastoise' merkitään vääräksi vastaukseksi, jos
kyseessä on mega blastoise.
\
Esimerkiksi Mewtwolla ja Charizardilla on kahdenlaiset megaevoluutiot (X ja Y). Näissä tapauksissa sovelluksessa pätee molemmat yllänäkyvät huomiot, eli oikea vastaus on Mega Mewtwo tai Mega Charizard.
\
Mikäli arvailu vaikuttaa monimutkaiselta, suosittelen pelaamaan kierroksen tai pari revision modea käyttäen!

## Game Over

Käyttäjän arvatessa väärin, pelinäkymässä olevat sydämet muuttuvat yksi kerrallaan harmaiksi. Kun arvauksia on osunut kolme kertaa kierroksen aikana väärin, peli päättyy.

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/hearts.png width="354" height="127">

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/sendhiscore.png width="320" height="240">

Mikäli pelaajalla on tarpeeksi pisteitä leaderboardsia varten, sovellus ilmoittaa tästä ja pelaajan tulos on mahdollista tallentaa 'Send hiscore' -napista. Tämän jälkeen pelaajan on mahdollista palata etusivulle ja aloittaa uusi peli, esimerkiksi suuremmalla määrällä generaatioita.

Jos pelaajalla ei ole tarpeeksi pisteitä, ei tuloksen lähettäminen ole mahdollista ja uuden pelin voi aloittaa ruutuun ilmestyvää 'Try again' -nappia painamalla.

## Leaderboards

Etusivun 'Hiscores'-napista siirrytään huipputuloksiin, jonne tallennetaan yhdeksän parhaan tuloksen saaneen pelaajan tulokset.

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/hiscores.png width="320" height="240">

