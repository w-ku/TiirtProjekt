class Queue(object):
    """
            lq - pojemnosc kolejki
            iq - aktualna liczba zgloszen w kolejce
            ig <= lq
    """
    def __init__(self, lq, iq):
        self.lq = lq
        self.iq = iq
        self.zgloszenia = []

    def dodaj_do_kolejki(self, zgloszenie):
        if self.iq < self.lq:
            self.zgloszenia.append(zgloszenie)
            self.iq += 1
            print "Zgloszenie dodane do kolejki"
        else:
            print "Zgloszenie odrzucone"
            # Odrzucone_zgloszenia += 1

    def zwolnij_kolejke(self):
        # tutaj zegar
        if len(self.zgloszenia) > 0:
            first_el = self.zgloszenia[0]
            self.zgloszenia.pop(0)
            self.iq -= 1
            print "Zwolniono kolejke"
            return first_el
        else:
            print "Kolejka pusta"
