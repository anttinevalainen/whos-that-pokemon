# Who's that Pokémon
## Harjoitustyön vaatimusmäärittely

### Tarkoitus
Who's that Pokémon on sovellus, joka toimii perinteisen Pokémon-animen rinnalla esitettävien kuva-arvoitusten mukaisesti. Pelissä on tarkoitus tunnistaa kuvassa näkyvä Pokémon vain sen mustan siluetin perusteella ja syöttää sen nimi kirjoitusnäkymään. Käyttäjä saa pisteitä sen mukaan, kuinka nopeasti oikea vastaus syötetään. Sovelluksessa on alustavasti sukupolvien 1-6 Pokémonit (721kpl) sekä näiden mahdolliset megaevoluutiot ja evoluutiohaaran sisällä tapahtuvat mahdolliset erikoismuodot. Sovelluksen perimmäinen tarkoitus on harjoitella Pokémonien nimien muistamista, mutta se voidaan myös mieltää peliksi. Kierroksen päätyttyä (Käyttäjän syötettyä väärän vastauksen tai ajastimen (10 sekuntia per kierros) päättyessä) käyttäjän on mahdollista tallentaa tuloksensa gamertagin (Kolme kirjainta) avulla.

### Käyttäjät
Sovelluksella on alustavasti vain yhdenlaisia käyttäjiä. Myös adminkäyttäjän lisääminen on mahdollista, jolloin kirjautunut admin voisi poistaa suorituksia esimerkiksi gamertagin perusteella. Perustoiminnallisuus, eli Pokémonien tunnistaminen, kierroksen tuloksen tallentaminen sekä tulosten tarkastelu on kuitenkin peruskäyttäjän hallittavissa.

### Käyttöliittymäluonnos
Sovelluksen tarkempi käyttöliittymäluonnos on vielä tekeillä, mutta alla ns. concept art -luonnos sovelluksen päävaiheen ulkoasusta

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/concept.jpeg width="200" height="300">


### Perusversion tarjoama toiminnallisuus
#### Viikkoon 4 palautukseen mennessä tehty:
- Perusversiossa käyttäjä valitsee päävalikosta, haluaako hän tarkastella tuloksia vai siirtyä tunnistamaan Pokémoneja. (✓)
- Päävalikosta on myös mahdollista sulkea sovellus. (✓)
- Tunnistaessa käyttäjä kirjoittaa arvauksensa tekstikenttään ja lähettää vastauksen, jolloin sovellus ilmoittaa, onko vastaus oikein vai väärin. (✓)
- Kun käyttäjä vastaa oikein, sovellus ilmoittaa siitä, näyttää siluetin takana olevan Pokémonin kuvan ja siirtyy seuraavaan kuvaan. (✓)
- Kun käyttäjä vastaa väärin, sovellus ilmoittaa siitä, näyttää siluetin takana olevan Pokémonin kuvan ja ilmoittaa pelin päättymisestä.
(Sovellukseen lisätty health-muuttuja, joka mahdollistaa kolme väärää vastausta, ennen pelin päättymistä! (✓))
- Pelin päättymisen jälkeen käyttäjä voi ilmoittaa pelaajanimensä ja lähettää tuloksensa leaderboardiin.
(Pelaajanimi ilmoitetaan ennen kierroksen alkua ja kierroksen päättyessä, sovellus ilmoittaa onko käyttäjä saanut tarpeeksi pisteitä lähettääkseen tuloksensa leaderboardiin. (✓))

#### Viikkoon 5 palautukseen mennessä tehty:
- Sovelluksella on nyt oma gamemode-luokka, jota varten pelaaja valitsee gamertagin yhteydessä ne generaatiot, joilla haluaa sovellusta käyttää (✓)
- Ajastimen sijaan käyttäjä saa pisteitä sen mukaan, kuinka monella generaatiolla sovellusta käytetään (50p per generaatio = 50-300p per oikea vastaus) (✓)
- Leaderboardsiin tallennetaan myös tieto siitä, kuinka monella generaatiolla tulos on tehty (✓)

#### Viikkoon 5 palautukseen mennessä tehty:
- Sovellukseen on lisätty revision-mode, joka helpottaa testausta oikein ja väärin vastatessa. Revision modessa vastaukset näkyvät vastausalueen alapuolella. Revision modessa tehtyjä ennätyksiä ei ole mahdollista lähettää leaderboardsiin. (✓)

Tekemättä (27.4.)
- Ajastin arvauskierroksille ja pisteidenanto nopeuden mukaan.

Mahdollisen adminkäyttäjän on mahdollista käyttää sovellusta ylläolevan selostuksen mukaisesti, mutta hän voi myös poistaa leaderboardista tuloksia pelaajanimen perusteella. Adminkäyttäjän sisällyttäminen sovellukseen on vielä harkinnassa.
27.4. Adminkäyttäjää ei toistaiseksi luotu

### Jatkokehitysideat
- Puuttuvien Pokémonien lisääminen sovellukseen (722-898)
- Perinteisten Who's that Pokémon -äänefektien lisääminen sovellukseen
- Vastausten tilastointi, esimerkiksi eniten ja vähiten tunnistetut Pokémonit
- Kirjoitusvirheiden huomiointi arvauksissa, jolloin sovellus voisi esimerkiksi palkita käyttäjän osittaisilla pisteillä ja sovellus siirtyy seuraavalle kierrokselle
