class Bucket(object):

    def __init__(self, vz, lz, iz):
        """
                vz - predkosc naplywu zetonow
                lz - maksymalna liczba zetonow (pojemnosc wiadra)
                iz - aktualna liczba zetonow
                iz < lz
        """
        self.vz = vz
        self.lz = lz
        self.iz = iz

    def odejmij_zetony(self):
        if self.iz > 0 and self.iz >= 1:
            self.iz -= 1

        return self.iz

    def dodaj_zetony(self):
        # bucket = Bucket(1,40,35)

        if (self.iz + 1) <= self.lz:
            self.iz += 1
        else:
            self.iz = self.lz
        print "Dodano zeton do wiadra."

        return self.iz

    def ile_zetonow(self):
        return self.iz
