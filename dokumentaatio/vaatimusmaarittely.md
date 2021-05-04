# Who's that Pokémon
## Harjoitustyön vaatimusmäärittely

### Tarkoitus
Who's that Pokémon on sovellus, joka toimii perinteisen Pokémon-animen rinnalla esitettävien kuva-arvoitusten mukaisesti. Pelissä on tarkoitus tunnistaa kuvassa näkyvä Pokémon vain sen mustan siluetin perusteella ja syöttää sen nimi kirjoitusnäkymään. Käyttäjä saa pisteitä sen mukaan, kuinka monella generaatiolla sovellusta käytetään. Sovelluksessa on alustavasti sukupolvien 1-6 Pokémonit (721kpl) sekä näiden mahdolliset megaevoluutiot ja evoluutiohaaran sisällä tapahtuvat mahdolliset erikoismuodot. Pisteytys tapahtuu periaatteella 50/generaatio, eli yhdellä generaatiolla pelatessa oikeasta vastauksesta saa 50 pistettä ja kuudella generaatiolla oikean vastauksen arvo on 300 pistettä.\
\
Sovelluksen perimmäinen tarkoitus on harjoitella Pokémonien nimien muistamista, mutta se voidaan myös mieltää peliksi. Kierroksen päätyttyä (Käyttäjän syötettyä väärän vastauksen kolmesti kierroksen aikana) käyttäjän on mahdollista tallentaa tuloksensa gamertagin (Kolme kirjainta) avulla.

### Käyttäjät
Sovelluksella on alustavasti vain yhdenlaisia käyttäjiä. Myös adminkäyttäjän lisääminen on mahdollista, jolloin kirjautunut admin voisi poistaa suorituksia esimerkiksi gamertagin perusteella. Perustoiminnallisuus, eli Pokémonien tunnistaminen, kierroksen tuloksen tallentaminen sekä tulosten tarkastelu on kuitenkin peruskäyttäjän hallittavissa.

### Käyttöliittymäluonnos
Sovelluksen tarkempi käyttöliittymäluonnos on vielä tekeillä, mutta alla ns. concept art -luonnos sovelluksen päävaiheen ulkoasusta

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/concept.jpeg width="200" height="300">


### Perusversion tarjoama toiminnallisuus
#### Viikon 4 palautukseen mennessä tehty:
- Perusversiossa käyttäjä valitsee päävalikosta, haluaako hän tarkastella tuloksia vai siirtyä tunnistamaan Pokémoneja. (✓)
- Päävalikosta on myös mahdollista sulkea sovellus. (✓)
- Tunnistaessa käyttäjä kirjoittaa arvauksensa tekstikenttään ja lähettää vastauksen, jolloin sovellus ilmoittaa, onko vastaus oikein vai väärin. (✓)
- Kun käyttäjä vastaa oikein, sovellus ilmoittaa siitä, näyttää siluetin takana olevan Pokémonin kuvan ja siirtyy seuraavaan kuvaan. (✓)
- Kun käyttäjä vastaa väärin, sovellus ilmoittaa siitä, näyttää siluetin takana olevan Pokémonin kuvan ja ilmoittaa pelin päättymisestä.
(Sovellukseen lisätty health-muuttuja, joka mahdollistaa kolme väärää vastausta, ennen pelin päättymistä! (✓))
- Pelin päättymisen jälkeen käyttäjä voi ilmoittaa pelaajanimensä ja lähettää tuloksensa leaderboardiin.
(Pelaajanimi ilmoitetaan ennen kierroksen alkua ja kierroksen päättyessä, sovellus ilmoittaa onko käyttäjä saanut tarpeeksi pisteitä lähettääkseen tuloksensa leaderboardiin. (✓))

#### Viikon 5 palautukseen mennessä tehty:
- Sovelluksella on nyt oma gamemode-luokka, jota varten pelaaja valitsee gamertagin yhteydessä ne generaatiot, joilla haluaa sovellusta käyttää (✓)
- Ajastimen sijaan käyttäjä saa pisteitä sen mukaan, kuinka monella generaatiolla sovellusta käytetään (50p per generaatio = 50-300p per oikea vastaus) (✓)
- Leaderboardsiin tallennetaan myös tieto siitä, kuinka monella generaatiolla tulos on tehty (✓)

#### Viikon 6 palautukseen mennessä tehty:
- Sovellukseen on lisätty revision-mode, joka helpottaa testausta oikein ja väärin vastatessa. Revision modessa vastaukset näkyvät vastausalueen alapuolella. Revision modessa tehtyjä ennätyksiä ei ole mahdollista lähettää leaderboardsiin. (✓)
    - Revision mode otettu mukaan myös Viikko5 -merkittyyn releaseen (29.4.)
 - Sovellus hyväksyy megaevoluutioiden kohdalla vastauksen VAIN mikäli vastaus on muotoa 'Mega [Pokemonin nimi]', eli esimerkiksi 'Mega Mewtwo'. Erikoismuotoja ei kuitenkaan tarvitse tietää (Esim Hoopan unchained muodon oikea vastaus on vain 'Hoopa') (✓)
 - Sovelluksesta on päätetty jättää kokonaan pois ajastin testipelaajien kommenttien myötä. Sovelluksen koetaan olevan tarpeeksi vaikea ja joidenkin siluettien kohdalla 10sek ei riitä nimen muistamiseen. Myös adminkäyttäjän lisääminen on poistettu todo-listalta (✓)

Tekemättä (4.5.)
 - Sovellusta varten on ladattu, muokattu ja alustettu nyt myös generaatioiden 7-8 pokemonit sekä kaikki mahdolliset gigantamaxmuodot sekä alolan ja galarian-muodot. Näitä ei kuitenkaan ole vielä lisätty uusimpaan releaseen (2) vaan ne tulee olemaan mukana loppupalautuksessa!

### Jatkokehitysideat
- Puuttuvien Pokémonien lisääminen sovellukseen (722-898)
- Perinteisten Who's that Pokémon -äänefektien lisääminen sovellukseen
- Vastausten tilastointi, esimerkiksi eniten ja vähiten tunnistetut Pokémonit
- Kirjoitusvirheiden huomiointi arvauksissa, jolloin sovellus voisi esimerkiksi palkita käyttäjän osittaisilla pisteillä ja sovellus siirtyy seuraavalle kierrokselle
