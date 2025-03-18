# Predykcja cen aut

## Analiza danych - notebooks/EDA.ipynb

- ceny kształtują się pomiędzy 0-7000000, ale powyej 2 mln nie ma ofert, dla czytelności danych pozbywamy się oferty za ponad 2mln i poniej 100
- kolumny mają duzo braków:
  - Cena 0
  - Stan 3239
  - Marka_pojazdu 3282
  - Model_pojazdu 3205
  - Wersja_pojazdu 46739
  - Generacja_pojazdu 40485
  - Rok_produkcji 3314
  - Przebieg_km 3894
  - Moc_KM 3629
  - Pojemnosc_cm3 4570
  - Rodzaj_paliwa 3325
  - Emisja_CO2 73885
  - Naped 12638
  - Skrzynia_biegow 3665
  - Typ_nadwozia 3293
  - Liczba_drzwi 4249
  - Kolor 3374
  - Kraj_pochodzenia 58830
  - Pierwszy_wlasciciel 91969
  - Data_pierwszej_rejestracji 78535
  - Lokalizacja_oferty 3245
  - Wyposazenie 3152
- pozbywam się kolumn: "Wersja_pojazdu", "Generacja_pojazdu", "Emisja_CO2","Data_pierwszej_rejestracji" ze względu na duzo braków i małą potencjalną uzyteczność
