
class Ticket(object):
    def __init__(self, stan, czas_wygenerowania):
        self.stan = stan
        self.czas_wygenerowania = czas_wygenerowania
        self.czas_akceptacji = None
        self.czas_oczekiwania = 0

    def get_czas_oczekiwania(self):
        self.czas_oczekiwania = (self.czas_akceptacji-self.czas_wygenerowania)
        return self.czas_oczekiwania
