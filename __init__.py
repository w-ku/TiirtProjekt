#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ticket import Ticket
from generator import TokenGenerator
from decision import DecisionModule
from bucket import Bucket
from queue import Queue
import time
from threading import Thread

SAMPLE_SIZE = 400
LAMBDA = 10
tablica_zgloszen = []
tc = TokenGenerator()
dm = DecisionModule()
bucket = Bucket(10, 40, 10)
kolejka = Queue(10, 3)
STOP = False


def generator_zgloszen():
    """generator zgloszen"""
    sum_odstep = 0
    start = time.time()
    total = 0

    for i in xrange(SAMPLE_SIZE):
        print "---------------------------------------"
        print "DLA %s : " % (i+1)

        gen = Ticket("pending", None, None)

        print gen.__dict__

        dm.make_decision(gen, bucket, kolejka)

        print "ZETONY W WIADRZE: %d " % (bucket.iz)
        print "ZGLOSZENIA W KOLEJCE: %s" % kolejka.iq

        # losowanie odstepu czasowego
        odstep = tc.generate_ts(LAMBDA)
        sum_odstep = sum_odstep + odstep
        print "Opoznienie na odstepie: %s" % sum_odstep
        print "Odstep: %s" % odstep
        time.sleep(odstep)
        print "Działanie programu: %s" % (time.time()-start)
        # if i == STOP = True


def uzupelnij_wiadro():
    """funkcja uzupelniajaca wiadro"""
    for i in xrange(SAMPLE_SIZE):
        x = (1.0/bucket.vz)
        time.sleep(x)
        bucket.dodaj_zetony()
        print "Zetonow w wiadrze: %s" % bucket.iz


def main():
    t1 = Thread(target=generator_zgloszen)
    t2 = Thread(target=uzupelnij_wiadro)
    t1.start()
    t2.start()


if __name__ == "__main__":
    print main()
