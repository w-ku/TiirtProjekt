#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time


class DecisionModule(object):
    def __init__(self, debug):
        self.obsluzone = []
        self.debug = debug

    def make_decision(self, zgloszenie, bucket, kolejka):

        if bucket.ile_zetonow() > 0:
            if len(kolejka.zgloszenia) > 0:
                kolejka.dodaj_do_kolejki(zgloszenie)

                zgloszenie = kolejka.zwolnij_kolejke()
                self.obsluzone.append(zgloszenie)
                bucket.odejmij_zetony()
            else:
                zgloszenie.czas_akceptacji = time.clock()
                self.obsluzone.append(zgloszenie)
                bucket.odejmij_zetony()
            czas_oczek = zgloszenie.get_czas_oczekiwania()
            if self.debug == 1:
                print "Czas oczekiwania: %s" % czas_oczek
                print "\tZgloszenie obsluzone"

        else:
            dodano = kolejka.dodaj_do_kolejki(zgloszenie)
            if self.debug == 1:
                print dodano
        # print "\tJuż obsłużono: %s " % len(self.obsluzone)
