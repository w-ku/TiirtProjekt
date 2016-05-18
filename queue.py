import time

class Queue(object):
    """
            lq - pojemnosc kolejki
            iq - aktualna liczba zgloszen w kolejce
            ig <= lq
    """
    def __init__(self, lq, iq, debug):
        self.lq = lq
        self.iq = iq
        self.odrzucone = 0
        self.zgloszenia = []
        self.debug = debug

    def dodaj_do_kolejki(self, zgloszenie):
        if self.iq < self.lq:
            self.zgloszenia.append(zgloszenie)
            self.iq += 1
            if self.debug == 1:
                print "Zgloszenie dodane do kolejki"
        else:
            if self.debug == 1:
                print "Zgloszenie odrzucone"
            self.odrzucone += 1

    def zwolnij_kolejke(self):
        if len(self.zgloszenia) > 0:
            first_el = self.zgloszenia[0]
            first_el.czas_akceptacji = time.clock()
            self.zgloszenia.pop(0)
            self.iq -= 1
            if self.debug == 1:
                print "Zwolniono kolejke"
            return first_el
        else:
            if self.debug == 1:
                print "Kolejka pusta"
