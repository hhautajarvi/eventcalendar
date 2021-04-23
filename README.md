# Event calendar
Kurssiprojekti Helsingin yliopiston Tietokantasovellus-kurssille

Sovelluksen on tarkoitus olla tapahtumakalenteri, johon käyttäjät voivat kirjautua ja lisätä omia tapahtumiaan (konsertteja, urheilutapahtumia, syntymäpäiväjuhlia jne.) sekä liittyä muiden lisäämiin tapahtumiin.

Sovelluksen ominaisuuksia ovat:
* Käyttäjä voi kirjautua sisään tehdä oman tunnuksen ja salasanan
* Käyttäjä voi tehdä omia tapahtumia haluamalleen päivämäärälle
* Tapahtumaa tehdessä voi kertoa tapahtumapaikan, kuvauksen ja luokitella sen tietyntyyppiseksi (esim. musiikki, taide, urheilu) sekä kutsua mukaan haluamiaan käyttäjiä
* Oman tapahtuman voi tehdä joko julkiseksi ja avoimeksi kaikille tai tehdä yksityisen ja vain kutsutuille käyttäjille näkyvän
* Kalenterinäkymä, josta voi esimerkiksi kuukausittain nähdä avoimet tapahtumat sekä ne joihin on itse ilmoittautunut
* Käyttäjä voi liittyä muiden tekemiin avoimiin tapahtumiin
* Käyttäjä voi valita haluaako hyväksyä saamansa kutsun tapahtumaan
* Hakutoiminto jolla voi etsiä tietyntyyppisiä tapahtumia 
* Tekemänsä oman tapahtuman voi halutessaan myös poistaa

## Sovelluksen tilanne
Sovellus on testattavissa [täällä](https://event--calendar.herokuapp.com/)

Sivustolle tullessaan käyttäjä voi tehdä uuden käyttäjätunnuksen tai kirjautua sisään. Sisäänkirjautumisen jälkeen etusivulta löytyy lista avoimista tapahtumista ja käyttäjän itse tekemistä yksityisistä tapahtumista, sekä yksityisistä tapahtumista joihin käyttäjä on kutsuttu. Käyttäjän saama kutsu tapahtumaan näkyy tapahtuman listauksessa. Käyttäjä näkee myös mihin tapahtumista on itse osallistumassa. Tapahtumia voi listata tyypin mukaan. Yläpalkissa on myös linkki uloskirjautumiseen.

Jokaiselta tapahtumasivulta löytyy lisätietoa tapahtumasta, sekä mahdollisuus liittyä tai poistua tapahtumasta (riippuen onko käyttäjä sillä hetkellä osallistujana). Jos käyttäjä on kutsuttu tapahtumaan, hän voi hyväksyä kutsun liittymällä tapahtumaan. Tapahtuman luoja voi myös poistaa tapahtuman kokonaan tai kutsua lisää käyttäjiä tapahtumaan. Luoja näkee myös jo kutsutut käyttäjät listauksena. 

Yläpalkista löytyy myös linkki uuden tapahtuman luontiin jossa käyttäjä voi tehdä haluamansa tapahtuman ja kutsua sinne käyttäjiä. Etusivulta pääsee myös menneiden tapahtumien listaukseen jossa näkee vanhojen tapahtumien tiedot ja osallistujat.

Sovelluksen toiminnallisuudet ovat pääpiirteittäin valmiina. Ulkoasun tekeminen puuttuu vielä lähes kokonaan, sekä etusivun tapahtumalistaus olisi tarkoitus tehdä jonkin näköiseen kalenterimuotoon.
