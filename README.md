# README – Selenium Testiranje za Swag Labs web trgovinu

## Pregled:
Projektni zadatak iz kolegija: Metode i tehnike testiranja programske podrške
Projekt sadrži automatizirane **Selenium** testove za web stranicu **Swag Labs**. 
Skripta testira funkcionalnosti stranice: prijava korisnika (defaultni podaci koji su dani na stranici), dodavanje prvog itema u košaricu, odlazak u košaricu, uklanjanje itema iz košarice, vraćanje na početnu stranicu i odjavu korisnika sa stranice.

## O Swag Labs stranici:
[Swag Labs](https://www.saucedemo.com/) je **dummy web trgovina** namijenjena za testiranje i vježbanje automatizacije testiranja. Stranica simulira funkcionalnosti e-trgovine, uključujući:
- Registraciju i prijavu korisnika
- Pregled proizvoda
- Sortiranje proizvoda
- Dodavanje proizvoda u košaricu
- Uklanjanje proizvoda iz košarice
- Proces kupnje (Unos podataka za dostavu)

## Korišteni alati:
Za izradu i izvođenje testova korišteni su alati:
- **Python** – programski jezik korišten za pisanje testova
- **Selenium WebDriver** – alat za automatizaciju web preglednika
- **Google Chrome** – preglednik korišten za testiranje
- **Chrome WebDriver** – potreban za kontrolu preglednika putem Seleniuma

## Napomena:
Koristi webdriver_manager za automatsko preuzimanje i postavljanje ChromeDrivera. Razlog tome jest što sam kod pisao na MacOS-u međutim htio sam i mogućnost pokretanja na Windows OS.
Ne koristim platform-specifične putanje, odnosno koristi se Service(ChromeDriverManager().install()) koji se automatski brine o tome.

## Preduvjet:
Prije pokretanja skripte potrebno je instalirati **Selenium** pomoću sljedeće naredbe:

```bash
pip install selenium
python3 -m pip install selenium
