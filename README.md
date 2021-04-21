# Event calendar
Kurssiprojekti Helsingin yliopiston Tietokantasovellus-kurssille

Sovelluksen on tarkoitus olla tapahtumakalenteri, johon käyttäjät voivat kirjautua ja lisätä omia tapahtumiaan (konsertteja, urheilutapahtumia, syntymäpäiväjuhlia jne.) sekä liittyä muiden lisäämiin tapahtumiin.

Sovelluksen ominaisuuksia ovat:
* Käyttäjä voi kirjautua sisään tehdä oman tunnuksen ja salasanan
* Käyttäjä voi tehdä omia tapahtumia haluamalleen päivämäärälle
* Omaan tapahtumaan voi tehdä kuvauksen ja luokitella sen tietyntyyppiseksi (esim. musiikki, taide, urheilu) sekä kutsua mukaan haluamiaan käyttäjiä
* Oman tapahtuman voi tehdä joko julkiseksi ja avoimeksi kaikille tai tehdä yksityisen ja vain kutsutuille käyttäjille näkyvän
* Kalenterinäkymä, josta voi esimerkiksi kuukausittain nähdä avoimet tapahtumat sekä ne joihin on itse ilmoittautunut
* Käyttäjä voi liittyä muiden tekemiin avoimiin tapahtumiin
* Käyttäjä voi valita haluaako hyväksyä saamansa kutsun tapahtumaan
* Hakutoiminto jolla voi etsiä tietyntyyppisiä tapahtumia 
* Tekemänsä oman tapahtuman voi halutessaan myös poistaa

## Sovelluksen tilanne
Sovellus on testattavissa [täällä](https://event--calendar.herokuapp.com/)

Tällä hetkellä käyttäjä voi tehdä uuden käyttäjätunnuksen ja kirjautua sisään ja ulos. Etusivulta löytyy lista avoimista tapahtumista ja käyttäjän itse tekemistä yksityisistä tapahtumista, sekä yksityisistä tapahtumista joihin käyttäjä on kutsuttu. 

Jokaiselta tapahtumasivulta löytyy lisätietoa tapahtumasta, sekä mahdollisuus liittyä tai poistua tapahtumasta (riippuen onko käyttäjä sillä hetkellä osallistujana). Jos käyttäjä on kutsuttu tapahtumaan, hän voi hyväksyä kutsun. Tapahtuman luoja voi myös poistaa tapahtuman kokonaan. 

Etusivulta löytyy myös linkki uuden tapahtuman luontiin jossa käyttäjä haluamansa tapahtuman ja kutsua sinne käyttäjiä. Etusivulta pääsee myös menneiden tapahtumien listaukseen jossa näkee tapahtuman tiedot ja osallistujat.

Vielä puuttuvia toimintoja ja asioita ovat ainakin:
* Tarkemmat virheviestit, sekä niitä useampaan tilanteeseen
* Etusivulle kalenterinäkymä tapahtumista
* Tapahtumahaku
* Tapahtumakutsun näkyminen etusivulla
* Ulkoasu
* Csfr-haavoittuvuus
