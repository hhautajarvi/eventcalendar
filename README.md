# Event calendar
Kurssiprojekti Helsingin yliopiston Tietokantasovellus-kurssille

Sovelluksen on tarkoitus olla tapahtumakalenteri, johon käyttäjät voivat kirjautua ja lisätä omia tapahtumiaan (konsertteja, urheilutapahtumia, syntymäpäiväjuhlia jne.) sekä liittyä muiden lisäämiin tapahtumiin.

Sovelluksen ominaisuuksia ovat:
* Käyttäjä voi kirjautua sisään tehdä oman tunnuksen ja salasanan
* Käyttäjä voi tehdä omia tapahtumia haluamalleen päivämäärälle
* Tapahtumaa tehdessä voi kertoa tapahtumapaikan, kuvauksen ja luokitella sen tietyntyyppiseksi (esim. musiikki, taide, urheilu) sekä kutsua mukaan haluamiaan käyttäjiä
* Oman tapahtuman voi tehdä joko julkiseksi ja avoimeksi kaikille tai tehdä yksityisen ja vain kutsutuille käyttäjille näkyvän
* Etusivulla avoimet, omat ja tapahtumat joihin olet kutsuttu näkee päivämäärän mukaan listattuna
* Listauksessa on merkittynä jos olet tapahtuman järjestäjä, osallistumassa siihen tai jos olet kutsuttu
* Käyttäjä voi liittyä muiden tekemiin avoimiin tapahtumiin
* Käyttäjä voi valita haluaako hyväksyä saamansa kutsun tapahtumaan
* Listaustoiminto jolla voi etsiä tietyntyyppisiä tapahtumia 
* Tekemänsä oman tapahtuman voi halutessaan myös poistaa
* Tapahtuman järjestäjä voi päivittää tapahtuman tietoja

## Sovelluksen tilanne
Sovellus on testattavissa [täällä](https://event--calendar.herokuapp.com/)

Sivustolle tullessaan ylävalikosta löytyy linkit uuden käyttäjätunnuksen tekemiseen ja sisäänkirjautumiseen. Sisäänkirjautumisen jälkeen etusivulta löytyy lista avoimista tapahtumista ja käyttäjän itse tekemistä yksityisistä tapahtumista, sekä yksityisistä tapahtumista joihin käyttäjä on kutsuttu. Käyttäjän saama kutsu tapahtumaan näkyy tapahtuman listauksessa. Käyttäjä näkee myös mihin tapahtumista on itse osallistumassa. Myös käyttäjän itse tekemät tapahtumat on kerrottu. Tapahtumia voi listata tyypin mukaan.

Yläpalkissa löytyy linkit uuden tapahtuman tekemiseen, menneisiin tapahtumiin ja uloskirjautumiseen, sekä myös takaisin tulevien tapahtumien listaukseen.

Jokaiselta tapahtumasivulta löytyy lisätietoa tapahtumasta, sekä mahdollisuus liittyä tai poistua tapahtumasta. Jos käyttäjä on kutsuttu tapahtumaan, hän voi hyväksyä kutsun liittymällä tapahtumaan. Tapahtuman järjestäjä voi myös päivittää tapahtuman tietoja, poistaa tapahtuman kokonaan tai kutsua lisää käyttäjiä tapahtumaan. Järjestäjä näkee myös jo kutsutut käyttäjät listauksena. 

Menneiden tapahtumien listauksessa etusivun tapaan tiedot vanhoista tapahtumista ja tapahtumien omilta sivuilta löytää tapahtumien tarkemmat tiedot ja osallistujat.

Sovelluksen toiminnallisuudet ja ulkoasu ovat tältä erää valmiina. Mahdollisia jatkokehitysideoita ovat etusivun tapahtumien listaus-/hakutapojen lisäys ja esimerkiksi erilaisten ystävä/harrastus-ryhmien luominen.
