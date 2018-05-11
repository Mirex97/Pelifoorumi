# Pelifoorumi Dokumentaatio 
Tämä dokumentti sisältää kaikki alueet käytynä läpi ja myös pika-ohjeet asennukselle
User storyt ovat kuitenkin toisessa tiedostossa documentation kansiosta. (Linkki löytyy myös gitin juuresta!).

### Kuvaus
Pelifoorumi, johon voi luoda palstoja ja jättää kommentteja palstojen alle!
Tietokannan tauluja ovat (Thread, Account, Comment, Tag, Section)!
Thread käsittelee palstan tiedot ja samalla myös näyttää palstaan liittyvät kommentit.

Account sisältää kaikki käyttäjät ja heidän tietonsa. Ja on yhteydessä palstaan ja kommenttiin (omistaja).
Käyttäjällä myös rooli (aluksi "default"), joka antaa eri toiminnallisuuksia sivulla. (Tällä hetkellä suunnitteilla vain ylläpito ja peruskäyttäjät, ei ehkä tarvitse edes enempää).

Comment sisältää käyttäjän asettaman viestin ja on yhteydessä käyttäjään (omistaja) sekä palstaan (sinne minne kirjoitettu).

Tag:in avulla voidaan etsiä samaan aihepiiriin liittyviä palstoja. Ja näin myös järjestellä niitä!
(Tagien asetus tuo + ja helpompi löytää samaan aihepiiriin kuuluvia palstoja).

Section menee vielä syvemmälle kuin Tag luokka. Se on vaadittu jokaiselle palstalle ja sen avulla palstat voidaan luokitella eri osioihin. Joten Section on Threadien vanhempi.

### Syvempi kuvaus tietokohteista.
Melkein kaikista tauluista Full CRUD! Paitsi kommentit, tästä puuttuu muokkaus toiminnallisuus.

Tauluja yhteensä: 5!
Threads: Pystyy luoda, lukea, päivittää ja poistaa.
Tags: Pystyy luoda (Admin), lukea ja poistaa. (Päivitys puuttuu ellei tähän voida laskea lisäämistä ja poistamista threadeille).
Section : Pystyy luoda (Admin), lukea, muokata ja poistaa.
Users: -||-
Comments: Voi luoda, lukea ja poistaa.

Monimutkaisia kyselyitä paljon! Nämä on valittu eri tilanteisiin ja soveltuvat sivun toimintaan.
Kyselyt vaihtelevat ehtolauseilla ja staattisia kyselyitä on useita, jotka on kutsuttu sitten niille tarpeellisissa kohdissa.


### Käyttöohje
Linkki foorumille --> [Foorumi](https://mirex-pelifoorumi.herokuapp.com/)

##### Navbar
- Tämä on oleellisin osa sivua ja käyttäjän paras ystävä.
- Vasemmasta osasta löytyy nopeat linkit eri osiin ((My Threads), Forum, Users, Tags).
- Löytyy myös Threadien etsintä osio johon avainsanan avulla voi etsiä palstoja.
  - Palstan löytyminen määräytyy palstan nimen mukaan.
  - Kuitenkin voi valita vieressä olven 'checkbox' avulla, että etsitään palstoja käyttäjän nimellä.
    - Kenttään tarvitsee vain laittaa osan etsittävän nimestä.
- Oikealla löytyy (Login ja Register) tai (Profile info, Logout).
- Navbarin yläpuolella olevaa logoa klikkaamalla pääsee takaisin 'Index' sivulle.
- Lisäksi otetaan tähän **Breadcrumb** toiminto (Navbarin alapuolella oleva osa), jonka avulla voi peruuttaa vanhempaan sivuun.
  - Tämä päivittyy eri sivuilla.

##### Index
- Tältä sivulta löytyy latauslinkki peliin pohjalta. Tämä on siis esittely sivu peliä varten.
  - Myös linkki viimeisimpään javaan ja OTM repositorioon githubbiin.
- Muuten alkusivu on yksinkertainen.

##### Forums (Navbar)
- Täältä pääsee osioiden (Section) listaukseen. Klikkaamalla nimeä pääsee seuraavalle sivulle.

##### Section
- Tältä sivulta löytyy osion palstat. Nämä on joko listattu "Pinned", "My Threads" ja "All Threads".
  - Listaus riippuu onko käyttäjä minkälainen (Admin, default, anonymous).
- Listauksen oikealla olevasta "Open thread!" linkistä pääsee palstan sisälle.
  - Tällä sivulla voi myös luoda nopeasti palstan osion sisään, joka luodaan vain nimen avulla.

##### Thread
- Täältä löytyy sitten informaatio.
- Tagejä voidaan lisätä sivulla olevasta listasta, ja ne päivittyvät tämän vieressä olevaan luotteloon.
  - Luettelon tagejä klikkaamalla tämä poistuu palstasta.
- Riippuen käyttäjän roolista hänelle voi näkyä vasemmassa kulmassa olevia vaihtoehtoja.
  - (Modify, Lock, Pin). Modify avulla voidaan muokata palstaa (Piilottaa, siirtää tai antaa kuvaus).
    - Jos palstan on Admin lukinnut, niin omistaja ei voi siirtää palstaa muualle tai muuttaa sen Hidden tilaa.
- Jos palstan tila on Hidden, sitä ei voi etsiä tai listata.
  - Admin kuitenkin näkee 'Hidden' palstat.
- Alta löytyy kommenteille osio ja kenttä niiden lisäämistä varten.
  - Pitää olla kirjautuneena.
  
##### Tags
- Täältä löytyy lista tageistä.
  - Tagien lisäys Adminin vastuulla. Vain tärkeimmät tagit siis käytössä.
- Tagiä klikkaamalla voi listata kaikki tagiin kuuluvat palstat.
  - Kuten search! (Aluksi sille oli oma metodi, mutta tämä oli hankala, kiitokset issuen antajalle).
##### Users
- Kaikki sivun käyttäjät listassa. (Nimi ja rooli).
  - Admin pystyy täältä hallinnoida käyttäjiä.
    - Tähän voisi toteuttaa jos käyttäjien määrä kasvaa, niin oma etsintä. (Jatkokehitys idea).

##### Muita sivuja.
Modify sivut ovat melko itsestään selittäviä.
"Profile informationista", voi muokata käyttäjän nimeä tai poistaa käyttäjän. (Poistaa samalla kaikki käyttäjän threadit).

## Asennusohje
Paikallista toteutusta varten Kloonaa tai lataa repositorio koneellesi (ja pura se).
Tämän jälkeen suorita 'python run.py' komentorivillä kansion sisällä ja sivun pitäisi aueta koneellesi osoitteseen 127.0.0.1:5000.
Tai checkkaa foorumia herokussa (Suosittelen tätä löytyy enemmän materiaalia)!

### Rajoitteet
Alussa 'Admin' rooli täytyy antaa jollekkin käyttäjälle manuaalisesti. Joten ei Admin käyttäjää ei ole kovakoodattuna missään.
Lisäksi BCryptiä en saanut toimimaan Herokussa. Vaikka enkoodaa oikein lokaalisti niin kaikki menee pieleen kun sen laittaa nettiin.
Salasanat ovat siis selkokielisinä (Siksi älä käytä samoja salasanoja tällä sivulla).

### Puuttuu tällä hetkellä:
- Tykkäämis toiminto (Ei pakollinen! Kommentit ovat jo tarpeeksi riittäviä!)
- Joistain syötteiden kohdista puuttuu ilmoitus mikä syötteessä on pielessä. (Tätä olen oikonut asettamalla ohjeeksi jo ennen kuinka kenttään kuuluu kirjoittaa esim: mikä pituus sallittu tai kommentti kentän laskuri).
  - Koska sovellus käyttää paljon redirect kutsuja ja sivuista löytyy kenttiä, joita ei ole suoraan otettu wtformista, niin en ole ymmärtänyt kuinka tähän lisätään virheen näyttäminen... (Tyhjiä kenttiä sivun syötteet eivät koskaan hyväksy (poislukien kuvaus)).

### Kokemukset taulukossa (päivämäärä  kokemus)
|Päiväys|Kokemus|
-|-|
Ennen pääsiäistä | Hieman rauhallisempaan otteeseen vain tutustunut pythonin käyttöön. (En aikaisemmin ole käyttänyt pythonia yhtään. Mutta nyt alkaa tulla tutuksi!
3.4.2018 | Nyt aloin vasta kunnolla erkanemaan esimerkki materiaalista ja suuntaamaan enemmän kohti omaa työtäni. Rekisteröitymisen ja autentikaation ansiosta ja myös hyvien todoappin esimerkkien kautta sain projektin kunnolla vauhtiin.
4.4.2018 | Koko päivän tapellut pythonin kanssa!!! Aloitin klo 8:30 ja nyt klo 22 kaikki vasta pelittää :D. Ei meinannut näkyä loppua virheille, mutta nyt! Kaikki ok! Herokussa tietokannat ja käyttäjään voi kirjautua ja rekisteröityä ja luoda palstan ja lisätä kommentteja. Käyttäjistä tehty täysi CRUD. Myös omat validoinnit ettei löydy duplikaatti käyttäjiä. Nimi ja salasana voi kuitenkin olla sama paitsi käyttäjätunnus! LISÄKSI hieman Tag ja Section taulu aloitettu mutta ei vielä valmis! Sen lisään seuraavalle kerralle.
6.4.2018 | Materiaalin ohjeistus korjattu mutta silti pitää listata jokin taulukko ja tätä en tehnyt aikaisemmin. Nyt kuitenkin käyttäjien listaus pitäisi toimia ja tämä listaa aktiiviset käyttäjät keitä foorumilta löytyy.
20.4.2018 | Tuli hieman kiire, koska aloin pohtimaan onko Tag taulu edes hyödyllinen... Mutta! Sitten hoksasin, että se voisi olla itseasiassa erittäin hyvä foorumille. Ja nyt hieman kiireessä tein tag taulun foorumille. Lisäksi foorumilla ei ollut monesta moneen suhdetta niin sen takia se on myös hyvä!
10.5.2018 | Koko päivä hiottu projektia valmiiseen muotoon. Ja näyttää hyvältä vaikka itse sanon :D!
11.5.2018 | Vielä muutama korjailu dokumentaation. Vähensin paljon tekstiä ensimmäisestä readmestä, koska tämä on selitetty paremmin itse täällä dokumentaatiossa.
