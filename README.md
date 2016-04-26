Wersja bardzo pierwsza
prosimy bez uwag o polish-english, etc



1. generujemy strumien zgloszen, ktory trafia do modułu decydujacego
2. modul decydujacy pyta wiadro czy sa wolne zetony
	jesli sa wolne zetony to zgloszenie jest obslugiwane
	jesli nie ma zetonow to odrzucamy

------------------------------------

1. strumien zgloszen
2. zgloszenia trafiaja do kolejki
3. z kolejki trafiaja do modulu
4. modul pyta wiadro czy sa zetony
	jesli tak to zgloszenie obslugiwane
	jesli nie to czeka w kolejce
5. akceptacja zgloszenia


------------------------------------

1. strumien zgloszen
2. sprawdz czy kolejka jest pelna
	jesli pelna to odrzuc
	jesli nie to przejsc do 3
3. dodaj zglosznenie do kolejki
-- || --