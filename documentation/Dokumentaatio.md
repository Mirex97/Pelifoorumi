# Pelifoorumi Dokumentaatio 
Tämä dokumentti sisältää kaikki alueet käytynä läpi ja myös ohjeet asennukselle
User storyt ovat kuitenkin toisessa tiedostossa documentation juuressa. (Linkki löytyy myös gitin juuresta!).

### Kuvaus
Pelifoorumi, johon voi luoda palstoja ja jättää kommentteja!
Tietokannan luokkia ovat (Thread, Account, Comment, Tag, Section)!
Thread käsittelee palstan tiedot ja samalla myös näyttää palstaan liittyvät kommentit.

Account sisältää kaikki käyttäjät ja heidän tietonsa. Ja on yhteydessä palstaan ja kommenttiin (omistaja).
Käyttäjällä myös rooli (aluksi "default"), joka antaa eri toiminnallisuuksia sivulla. (Tällä hetkellä suunnitteilla vain ylläpito ja peruskäyttäjät, ei ehkä tarvitse edes lisää).

Comment sisältää käyttäjän asettaman viestin ja on yhteydessä käyttäjään (omistaja) sekä palstaan (sinne minne kirjoitettu).

Tag:in avulla voidaan etsiä samaan aihepiiriin liittyviä palstoja. Ja näin myös järjestellä niitä!
(Tagin asettaminen ei pakollinen).

Section menee vielä syvemmälle kuin Tag luokka. Se on vaadittu jokaiselle palstalle ja sen avulla palstat voidaan luokitella eri osioihin. 

### Käyttöohje
Linkki foorumille --> Foorumi[https://mirex-pelifoorumi.herokuapp.com/]

# HUOM!!!
JOS Heroku valittaa internal server errorista, niin odota hetki ja palaa sivulle tai spämmää F5:sta. Heroku jostain syystä ei reagoi hetken aikaan, mutta melkein välittömästi pyynnön jälkeen se pitäisi herätä!

#### Käyttöohjeet jatkuvat

1. Ensiksi tulee näkymä indeksistä, ja yläpalkista voi löytää "Login", "Register", "List threads" ja "Create a new Thread".
- Login --> kirjaudu olemassa olevaan käyttäjään.
- Register --> Luo käyttäjä
- List threads --> Palstojen listaus
- Create a bew Thread --> Palstan luonti
2. Edetään Registeriin. Täältä löytyy heti lomake uuden käyttäjän luontiin!
- Name --> Nimesi
- Username --> Käyttäjänimesi
- Password --> Salasana
- Retype Password --> Salasanan varmistus.
  - Jos käyttäjänimi, salasanat ovat väärin tai jokin kenttä on tyhjä niin lomake ei etene ja sivu alkaa valittamaan.
3. Klikkaa registeriä ja käyttäjään pitäisi kirjautua sisään! Nyt yläpalkkiin pitäisi tulla "Profile information" ja "Logout".
- Logout kirjaa ulos! (Melko selvänpäiväistä).
- Profile information näyttää käyttäjän tiedot! Ja mahdollistaa myös muokkaukseen.
  - Palataan näihin kohta!
4. Tarkkaillaan "Create a new Thread" sivua. Ilmestyy lomake josta voi suoraan luoda uuden palstan pelkällä nimellä.
  - Tähän tulee vielä lisää vaihtoehtoja, kuten mihin osioon lisätään ja tagit JA myös kuvaus!
- Create new Thread! Luo uuden palstan ja vie listaukseen.
5. List threads sivulla on nyt uusi palstasi ja tämä löytyy kahdesta kohdasta. Omat palstat ja kaikki palstat (tarvitsee hidden kentän).
- Palstan vierestä löytyy "Open Thread!", joka avaa kyseisen palstan.
6. Palstan avauduttua voi listata kommentit ja myös lisätä alla olevalla lomakkeella.
7. Palataan Profile informationin pariin.
- Sivulta löytyy Modify nappi ja sen alta listana käyttäjän tiedot.
8. Modify nappi avaa uuden lomakkeen jonka avulla voi muokata käyttäjän tietoja!
- Sivulta löytyy myös "DELETE ACCOUNT", joka poistaa oman käyttäjäsi! Klikataan sitä kohta.
- Taas melko selkestä kentät: "Name", "Username", "Old Password", "New Password".  Samat validoinnit pätee kuten rekisteröinnissä.
9. Update napilla voi päivittää tiedot ja tämä vie takaisin profiilin listaukseen!
10. Mennään vielä Modify napilla modify sivulle ja klikataan DELETE ACCOUNT
11. Onnittelut pääsit tutoriaalista läpi!
- Ohjeisiin tulee vielä lisättävää kun saan kaikki toiminnot kasaan.

### Asennusohje
Paikallista toteutusta varten Kloonaa tai lataa repositorio koneellesi (ja pura se).
Tämän jälkeen suorita 'run.py' pythonilla ja sivun pitäisi aueta koneellesi osoitteseen 127.0.0.1:5000.
- Tarvitsen vielä tarkennusta oliko asennusohje näin lyhyt...?

### Rajoitteet
... TODO

### Puuttuu tällä hetkellä:
- Linkki peliin
- Ulkonäkö
- Thread luokan kuvaus (description) toiminnallisuus! (Helppo).
- Tag luokan toiminnallisuus
- Section luokan toiminnallisuus ja sen lisäys listaukseen!
- Ylläpito ja tämän näkymät!
- Käyttäjien ylennys
- Palstan ja viestien sisällön muokkaus ja poisto (Tällä hetkellä vain koko käyttäjän poisto poistaa kaikki tämän viestit ja palstat).
- Tykkäämis toiminto (Ei pakollinen!)



### Kokemukset taulukossa (päivämäärä  kokemus)
|Päiväys|Kokemus|
-|-|
Ennen pääsiäistä | Hieman rauhallisempaan otteeseen vain tutustunut pythonin käyttöön. (En aikaisemmin ole käyttänyt pythonia yhtään. Mutta nyt alkaa tulla tutuksi!
3.4.2018 | Nyt aloin vasta kunnolla erkanemaan esimerkki materiaalista ja suuntaamaan enemmän kohti omaa työtäni. Rekisteröitymisen ja autentikaation ansiosta ja myös hyvien todoappin esimerkkien kautta sain projektin kunnolla vauhtiin.
4.4.2018 | Koko päivän tapellut pythonin kanssa!!! Aloitin klo 8:30 ja nyt klo 22 kaikki vasta pelittää :D. Ei meinannut näkyä loppua virheille, mutta nyt! Kaikki ok! Herokussa tietokannat ja käyttäjään voi kirjautua ja rekisteröityä ja luoda palstan ja lisätä kommentteja. Käyttäjistä tehty täysi CRUD. Myös omat validoinnit ettei löydy duplikaatti käyttäjiä. Nimi ja salasana voi kuitenkin olla sama paitsi käyttäjätunnus! LISÄKSI hieman Tag ja Section taulu aloitettu mutta ei vielä valmis! Sen lisään seuraavalle kerralle.
