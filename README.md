1. Symulator może być uruchamiany z nastepujacymi atrybutami
  * debug {0,1}
  * accqty {int}
  * lq {int}
  * lz {int}
  * vz {int}
  * lambda {int}

2. Objasnienie atrybutow
  * debug : informuje uzytkownika o kolejnosci uruchomionych funkcji
  * accqty : warunek stopu symulatora, liczba obsluzonych zgloszen
  * lq : maksymalny rozmiar kolejki dla oczekujacych zgloszen
  * lz : maksymalna liczba zetonow w wiadrze
  * vz : predkosc naplywania zetonow do wiadra
  * lambda : intensywnosc naplywu zgloszen

3. Przykład użycia
 
* Poisson (mode: debug - pokazuje obsługiwane tickety)
  * python __init__.py --debug 1 --accqty 100 --lq 20 --lz 40 --vz 30 --lamb 15
 
* OnOff (mode: debug)
  * python onOff.py --debug 1 --on 200 --off 2
