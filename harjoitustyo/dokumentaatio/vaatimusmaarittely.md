# Who's that Pokémon
## Harjoitustyön vaatimusmäärittely

### Tarkoitus
Who's that Pokémon on sovellus, joka toimii perinteisen Pokémon-animen rinnalla esitettävien kuva-arvoitusten mukaisesti. Pelissä on tarkoitus tunnistaa kuvassa näkyvä Pokémon vain sen mustan siluetin perusteella ja syöttää sen nimi kirjoitusnäkymään. Käyttäjä saa pisteitä sen mukaan, kuinka nopeasti oikea vastaus syötetään. Sovelluksessa on alustavasti sukupolvien 1-6 Pokémonit (721kpl) sekä näiden mahdolliset megaevoluutiot ja evoluutiohaaran sisällä tapahtuvat mahdolliset erikoismuodot. Sovelluksen perimmäinen tarkoitus on harjoitella Pokémonien nimien muistamista, mutta se voidaan myös mieltää peliksi. Kierroksen päätyttyä (Käyttäjän syötettyä väärän vastauksen tai ajastimen (10 sekuntia per kierros) päättyessä) käyttäjän on mahdollista tallentaa tuloksensa gamertagin (Kolme kirjainta) avulla.

### Käyttäjät
Sovelluksella on alustavasti vain yhdenlaisia käyttäjiä. Myös adminkäyttäjän lisääminen on mahdollista, jolloin kirjautunut admin voisi poistaa suorituksia esimerkiksi gamertagin perusteella. Perustoiminnallisuus, eli Pokémonien tunnistaminen, kierroksen tuloksen tallentaminen sekä tulosten tarkastelu on kuitenkin peruskäyttäjän hallittavissa.

### Käyttöliittymäluonnos
Sovelluksen tarkempi käyttöliittymäluonnos on vielä tekeillä, mutta alla ns. concept art -luonnos sovelluksen päävaiheen ulkoasusta

<img src=kuvat/concept.jpeg width="200" height="300">

### Perusversion tarjoama toiminnallisuus
Perusversiossa käyttäjä valitsee päävalikosta, haluaako hän tarkastella tuloksia vai siirtyä tunnistamaan Pokémoneja. Päävalikosta on myös mahdollista sulkea sovellus. Tunnistaessa käyttäjä kirjoittaa arvauksensa tekstikenttään ja lähettää vastauksen, jolloin sovellus ilmoittaa, onko vastaus oikein vai väärin. Kun käyttäjä vastaa oikein, sovellus ilmoittaa siitä, näyttää siluetin takana olevan Pokémonin kuvan ja siirtyy seuraavaan kuvaan. Kun käyttäjä vastaa väärin, sovellus ilmoittaa siitä, näyttää siluetin takana olevan Pokémonin kuvan ja ilmoittaa pelin päättymisestä. Pelin päättymisen jälkeen käyttäjä voi ilmoittaa pelaajanimensä ja lähettää tuloksensa leaderboardiin.

Mahdollisen adminkäyttäjän on mahdollista käyttää sovellusta ylläolevan selostuksen mukaisesti, mutta hän voi myös poistaa leaderboardista tuloksia pelaajanimen perusteella. Adminkäyttäjän sisällyttäminen sovellukseen on vielä harkinnassa.

### Jatkokehitysideat
- Puuttuvien Pokémonien lisääminen sovellukseen (722-898)
- Perinteisten Who's that Pokémon -äänefektien lisääminen sovellukseen
- Vastausten tilastointi, esimerkiksi eniten ja vähiten tunnistetut Pokémonit
- Kirjoitusvirheiden huomiointi arvauksissa, jolloin sovellus voisi esimerkiksi palkita käyttäjän osittaisilla pisteillä ja sovellus siirtyy seuraavalle kierrokselle
