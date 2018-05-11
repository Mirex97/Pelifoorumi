#### Huom. Sivulla on paljon SQL kyselyitä, koska rooleille on eri tyyppiset kyselynsä. Heitän siis vain muutamia kyselyitä Stoorien ohelle. Simppeleitä, kuten query.get() kyselyitä en lisää ohelle, koska ne ovat itsestään selviä. (Veisi liikaa tilaa).

### Käyttäjänä voin:
- [x] Luoda käyttäjän foorumiin.
- [x] Asettaa käyttälle uniikin nimen ja muita tietoja.
- [x] Kirjautua sivulle
- [x] Ihailla sivun hienoa ulkonäköä!
- [x] Etsiä palstoja palstan nimen tai käyttäjän avulla.
- [x] Avata julkisia osioita (Section) ja sieltä keskustelupalstoja (Threads).
```
find_threads_with_section(section_id)
SELECT  thread.id, thread.name, account.username FROM thread"
                    " LEFT JOIN account ON thread.account_id = account.id"
                    " WHERE (thread.section_id = :sectionid)"
                    " AND NOT thread.hidden"
                    " ORDER BY thread.date_created"
                    " DESC
```
- [x] Kommentoida palstoja (Tykkääminen vaihtoehtoinen).
- [x] Etsiä keskustelupalstoja tägien avulla.
```
find_threads_by_tag(tag)
SELECT DISTINCT thread.id, thread.name, account.username, section.name, thread.date_created FROM thread"
                    " LEFT JOIN account ON account.id = thread.account_id"
                    " LEFT JOIN section ON section.id = thread.section_id"
                    " LEFT JOIN tag_thread ON thread.id = tag_thread.thread_id"
                    " LEFT JOIN tag ON tag.id = tag_thread.tag_id"
                    " WHERE LOWER(tag.name) LIKE LOWER(:tagi)"
                    " ORDER BY thread.date_created DESC
```
- [x] Luoda keskustelupalstan (Kuvaus "modify" osiossa palstalla)
- [x] Muokata palstaa omistajana.
- [x] Lisätä tekstiä ja kommentteja ja myös poistaa niitä.
- [x] Kirjautua ulos
- [x] Avata linkkejä ja myös ladata foorumiin liittyvän pelin!

### Ylläpitäjänä voin:
- [x] Tehdä samat kuin käyttäjä!
- [x] Luoda luokkia/osioita (Sections) joihin voi muut luoda palstoja. (Vaikuttaa suoraan thread.list.html:ään ja luo sinne oman osion luokalle).
- [x] Poistaa vapaasti keskustelupalstoja.
- [x] Poistaa käyttäjiä (hyvään syyn puitteissa)
- [x] Siirtää palstoja ja asettaa ne piilotetuiksi tai näkyviksi! (Hidden)
- [x] Lukita palstoja, ettei palstan omistajalla ole oikeuksia siirtää sitä tai vaihtaa pois Hidden tilasta (Evil).
- [x] Avata piilotettuja palstoja ja myös kommentoida niitä.
- [x] Pinnata palstoja (Pin). Ja asettaa ne palstojen listaamisen kärkeen.
- [x] Luoda tägejä, joita muut voi lisätä palstoilleen.

### Anonyyminä henkilönä voin:
- [x] Käydä sivulla.
- [x] Ihannoida sivuja!
- [x] Lukea palstoja.
- [x] Etsiä palstoja.
- [x] Ladata foorumiin liittyvän pelin!
- [x] rekisteröityä!
