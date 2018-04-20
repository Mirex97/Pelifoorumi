Nimi | Linkki
-|-
Heroku | [Mirex-Pelifoorumi!](https://mirex-pelifoorumi.herokuapp.com/)!
User storyt | [Stories!](https://github.com/Mirex97/Pelifoorumi/blob/master/documentation/UserStories.md)
Kaavio | [Kaavio!](https://raw.githubusercontent.com/Mirex97/Pelifoorumi/master/documentation/Tietokanta.png)
Dokumentaatio | [KESKEN!](https://github.com/Mirex97/Pelifoorumi/blob/master/documentation/Dokumentaatio.md)

### Viimeisimmät Github päivitykset
- Lisätty tagit jotka toimivat mutta ovat hieman hankalasti saavutettavissa tällä hetkellä!
- Tagit sisältävät monesta moneen suhteen palstojen välillä!
#### Puuttuvat toiminnallisuudet jotka jäivät kesken:
- Threadin muokkaaminen ja kuvauksen asettaminen, palstan asettaminen piilotetuksi. Niitä en ehtinyt lisäämään mutta ovat kuitenkin olemassa. 

##### **Viimeisin MAJOR päivitys**
- Muokattu ulkonäköä ja myös tehty muutamia korjauksia joita palautuksessa mainittiin.
- Tein autorisoinnin toisin lisäämällä roolit käyttäjille. Koska rooleja on vain kaksi "Admin" ja "Default" niin en nähnyt tarpeen tehdä koko autorisointia uudelleen vaikka se toimii tällä hetkellä erittäin hyvin vaikka itse sanon!

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
