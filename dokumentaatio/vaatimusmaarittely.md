# Who's that Pokémon
## Harjoitustyön vaatimusmäärittely

### Tarkoitus
Who's that Pokémon on sovellus, joka toimii perinteisen Pokémon-animen rinnalla esitettävien kuva-arvoitusten mukaisesti. Pelissä on tarkoitus tunnistaa kuvassa näkyvä Pokémon vain sen mustan siluetin perusteella ja syöttää sen nimi kirjoitusnäkymään. Käyttäjä saa pisteitä sen mukaan, kuinka monella generaatiolla sovellusta käytetään. Sovelluksessa on sukupolvien 1-8 Pokémonit (898kpl) sekä näiden mahdolliset evoluutiohaaran sisällä tapahtuvat mahdolliset erikoismuodot. Käyttäjän valittavissa on tavallisten generaatioiden lisäksi megaevoluutiot, gigantamax-evoluutiot, Alolan erikoisevoluutiot sekä Galarin erikoisevoluutiot. Valittavia evoluutiomahdollisuuksia aloitusnäkymässä on siis 12kpl.\Pisteytys tapahtuu periaatteella 50/generaatio, eli yhdellä generaatiolla pelatessa oikeasta vastauksesta saa 50 pistettä ja kaikilla generatiovalinnoilla oikean vastauksen arvo on 360 pistettä.\
\
Sovelluksen perimmäinen tarkoitus on harjoitella Pokémonien nimien muistamista, mutta se voidaan myös mieltää peliksi. Kierroksen päätyttyä (Käyttäjän syötettyä väärän vastauksen kolmesti kierroksen aikana), mikäli käyttäjän saamat pisteet riittävät, käyttäjän on mahdollista tallentaa tuloksensa hiscoreihin.

### Käyttäjät
Sovelluksella on vain yhdenlaisia käyttäjiä. Perustoiminnallisuus, eli Pokémonien tunnistaminen, kierroksen tuloksen tallentaminen sekä tulosten tarkastelu on peruskäyttäjän hallittavissa eikä tarvetta sisäänkirjautumiselle tai adminkäyttäjälle ole tarpeellista.

### Käyttöliittymäluonnos
Alla sovelluksen ensimmäinen käyttöliittymäluonnos, joka on tehty 24.3.21

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/concept.jpeg width="400" height="600">

Sovelluksen lopullinen käyttöliittymänäkymä (11.5.21) samassa pelitilanteessa näyttää tältä:

<img src = https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/wronganswer1.PNG width="200" height="300">
<img src = https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/wronganswer2.PNG width="200" height="300">


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

#### Loppupalautukseen tehty:
 - Sovellusta varten on ladattu, muokattu ja alustettu nyt myös generaatioiden 7-8 pokemonit sekä kaikki mahdolliset gigantamax-muodot sekä Alolan ja Galarian-muodot. Myös yksittäisiä erikoismuotoja on lisätty eri generaatioihin (✓)
    - Myös gigantamax-, Alolan-, ja Galarian-muotojen kohdalla arvauksen on sisällettävä Megaevoluutioiden tavoin oma etuliitteensä (Gigantamax, Alolan tai Galarian)
 - Sovelluksen päätoiminnallisuutta ja hierarkiaa on paranneltu runsaasti. Sovelluksen toiminnallisuus on täysin siirretty services-kansion tiedostoihin ja gameplay-kansioon on eristetty sovelluksessa käytettävät objektit: Player, Gamemode, Pokedex ja Pokemon (✓)
 - Testien kattavuus on nyt 100% (✓)

### Jatkokehitysideat
- Perinteisten Who's that Pokémon -äänefektien lisääminen sovellukseen
- Vastausten tilastointi, esimerkiksi eniten ja vähiten tunnistetut Pokémonit
- Kirjoitusvirheiden huomiointi arvauksissa, jolloin sovellus voisi esimerkiksi palkita käyttäjän osittaisilla pisteillä ja sovellus siirtyy seuraavalle kierrokselle. Nykyisessä versiossaan sovellus ei huomioi isoja kirjaimia, välilyöntejä tai erikoismerkkejä.
