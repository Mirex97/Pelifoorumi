Nimi | Linkki
-|-
Heroku | [Mirex-Pelifoorumi!](https://mirex-pelifoorumi.herokuapp.com/)!
User storyt | [Stories!](https://github.com/Mirex97/Pelifoorumi/blob/master/documentation/UserStories.md)
Kaavio | [Kaavio!](https://raw.githubusercontent.com/Mirex97/Pelifoorumi/master/documentation/Tietokanta.png)
Dokumentaatio | [KESKEN!](https://github.com/Mirex97/Pelifoorumi/blob/master/documentation/Dokumentaatio.md)

### Ongelmia


- Yritin lisätä bcryptiä salasanoille, mutta tämä osoittautui jostain syystä mahdottomaksi Herokussa! Väittää ettei salasana ole enkoodattu vaikka tallensin sen käyttäen bcryptin omia metodeita. Sovellus toimi lokaalisti omalla koneellani ja se osasi myös lukea cryptatun salasanan oikein.
  - En ymmärrä mikä Herokussa on vikana, mutta mistään ei löydy ohjeita tai apua tähän ongelmaan. Joten poistin koko cryptauksen, jonka kanssa tappelin yli 5h. 
    - Onko oma Herokuni jotenkin onnistunut sekoittamaan itsensä, koska se on mahdottoman surkeampi kuin pyörittää lokaalisti koneella.
- Lisäksi Herokussa on koko ajan SSL ongelmia, kun yritän kirjautua sisään. Tähänkään en ole löytänyt vastausta.

### Viimeisin päivitys
- Päivitetty ulkonäköä
- Korjattu Tagi taulu
- Korjattu koodikatselmoinnissa huomattuja virheitä

#### Puuttuvat toiminnallisuudet jotka jäivät kesken:
- Threadin muokkaaminen ja kuvauksen asettaminen, palstan asettaminen piilotetuksi. Niitä en ehtinyt lisäämään mutta ovat kuitenkin olemassa. 

# Pelifoorumi
Pelifoorumi, johon käyttäjä voi rekisteröityä ja kirjautua. Foorumilla käyttäjä voi kommentoida / luoda keskustelupalstoja, joilla on
otsikko ja siihen liittyvät tagit. Foorumilla on myös rooleja, joita ylläpito voi asettaa käyttäjille, jotka mahdollistavat käyttäjille
erikoistoimintoja. Eli ylläpito voi ylentää käyttäjiä ns. ylläpitäjiksi (palkkioksi aktiivisuudesta). Aluksi siis kaikki käyttäjät ovat
default roolissa.

Keskustelupalstat voidaan luoda tiettyjen luokkien sisälle, kuten "Uutiset" tai "Ehdotukset" taikka "Kysymykset"... Näitä luokkia
voidaan siis lisätä tarpeen mukaan.

Ylläpito ja keskustelupalstan omistaja voi lukita keskustelupalstan ja vain ylläpito voi poistaa sen. Omistaja voi myös asettaa palstan
näkymättömäksi, ettei se näy julkisesti muille (samoin myös ylläpito). Huom. Ylläpidolla on kaikki oikeudet ja voivat poistaa
sopimattomia keskustelupalstoja ja myös vaihtaa niitten tagejä, jos ne on asetettu väärään luokkaan.

Tagien avulla voidaan luokitella palstoja ja etsiä niitä.

Ja koska tämä on pelifoorumi niin tähän foorumiin tietysti liittyy peli, jota olen tällä hetkellä luomassa kursilla "Ohjelmisto
tekniikan menetelmät". Niin mahdollisesti tämä foorumi sisältää myös latauslinkin peliä varten kun se on valmiina julkaistavaksi.

Käyttäjien profiileista: Käyttäjä voi muokata profiilin tietoja ja muokata omaa kuvaustaan, (profiilikuvaa) ja salasanan. Käyttäjät
eivät voi muokata nimeään (se pysyy minkä valitsee). Ei voi muokata käyttäjän luomishetkeä (sisältää ajankohdan jolloin liittyi
foorumiin). Ja muita pysyviä muuttujia, kuten viestienmäärä, keskustelupalstojen luomis määrä.

## Toimintoja:

- Kirjautuminen / Rekisteröityminen
- Profiilin muokkaus (mahdollisesti myös profiilikuvan lisääminen)
- Keskustelupalstan luominen luokan sisälle
- Keskustelupalstan muokkaus (Ylläpito ja Omistaja)
- Keskustelupalstan lukeminen ja kommentoiminen (kaikki)
- Keskustelupalstojen etsintä tagien avulla
- Ja tietysti keskustelupalstojen listaus oletetusti. (Listaus joko viimeksi luotujen mukaan, tai mahdollisesti suosion mukaan tai
aakkosjärjestyksessä.)
- Kommentien tykkääminen ja myös palstojen tykkääminen. (Voisi listata tykkäämisien mukaan)

## Ylläpidon toiminnot:
- Ylentää käyttäjiä
- Vapaasti muokata keskustelupalstoja (paitsi sisältö), voi kuitenkin poistaa sopimattomia palstoja!
- Siirtää keskustelupalstoja luokkien väleissä.
- Poistaa käyttäjiä
