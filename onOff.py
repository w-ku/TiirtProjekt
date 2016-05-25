#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread
import time
import optparse

from ticket import Ticket
from generator import TokenGenerator
from decision import DecisionModule
from bucket import Bucket
from queue import Queue

parser = optparse.OptionParser()

parser.add_option('--debug', type="int", default=0)
# docelowa liczba zaakceptowanych zgloszen -> warunek stopu
parser.add_option('--accqty', type="int", default=60)
# maksymalny rozmiar kolejki dla oczekujacych zgloszen
parser.add_option('--lq', type="int", default=100)
# maksymalna liczba zetonow w wiadrze
parser.add_option('--lz', type="int", default=40)
# predkosc naplywania zetonow
parser.add_option('--vz', type="int", default=5)
# intensywnosc zgloszen
parser.add_option('--lamb', type="int", default=15)
parser.add_option('--on', type="int", default=200)
parser.add_option('--off', type="int", default=2)


options, remainder = parser.parse_args()
print options.__dict__
# debug mode
DEBUG = options.debug
# warunek stopu
ACCQTY = options.accqty
# kolejka max:
LQ = options.lq
# pojemnosc wiadra
LZ = options.lz
# predkosc naplywania zetonow
VZ = options.vz
# intensywnosc zgloszen
LAMBDA = options.lamb

ON = options.on
OFF = options.off

tc = TokenGenerator()
dm = DecisionModule(DEBUG)
bucket = Bucket(VZ, LZ, 1, DEBUG)
kolejka = Queue(LQ, 0, DEBUG)


def generator_zgloszen():
    """generator zgloszen"""
    sum_odstep = 0
    sum_on_off = 0
    start = time.time()
    total = 0
    print [ACCQTY, LQ, LZ, VZ, LAMBDA]
    while len(dm.obsluzone) < ACCQTY:

        # print "DLA %s : " % (i+1)
        gen_on = tc.generate_onOff(ON)
        gen_off = tc.generate_onOff(OFF)
        sum_on_off = sum_on_off + gen_on

        while sum_on_off > sum_odstep:
            print "ON:"
            gen = Ticket("pending", time.clock())
            dm.make_decision(gen, bucket, kolejka)

            # losowanie odstepu czasowego
            odstep = tc.generate_ts(LAMBDA)
            sum_odstep = sum_odstep + odstep
            time.sleep(odstep)

        sum_on_off = sum_on_off + gen_off

        while sum_on_off > sum_odstep:
            print "OFF:"
            # losowanie odstepu czasowego
            odstep = tc.generate_ts(LAMBDA)
            sum_odstep = sum_odstep + odstep
            time.sleep(odstep)

        if DEBUG == 1:
            print "---------------------------------------"
            print "ZETONY W WIADRZE: %d " % (bucket.iz)
            print "ZGLOSZENIA W KOLEJCE: %s" % kolejka.iq
            print "Opoznienie na odstepie: %s" % sum_odstep
            print "Odstep: %s" % odstep
            print "Obsluzono: {}".format(len(dm.obsluzone))
            print "Działanie programu: %s" % (time.time()-start)

    for ticket in dm.obsluzone:
        total += ticket.czas_oczekiwania

    print "\n\n========== WYNIK =============\n"
    sredni_czas_oczekiwania = total/len(dm.obsluzone)
    print "SREDNI CZAS OCZEKIWANIA: {}".format(sredni_czas_oczekiwania)
    # print "ZGLOSZENIA OBSLUZONE: {}".format(len(dm.obsluzone))
    # print "ZGLOSZENIA W KOLEJCE: {}".format(len(kolejka.zgloszenia))
    # print "ZGLOSZENIA ODRZUCONE: {}".format(kolejka.odrzucone)
    # print "ZOSTALO ZETONOW W WIADRZE: {}".format(bucket.iz)
    print "PRAWDOPODOBIENSTWO ODRZUCENIA: {}".format(float(kolejka.odrzucone)/(kolejka.odrzucone+len(dm.obsluzone)))
    print '\n\n'

def uzupelnij_wiadro():
    """funkcja uzupelniajaca wiadro"""
    sum_odstep = 0
    while len(dm.obsluzone) < ACCQTY:
        # 1/lambda:
        x = (1.0/bucket.vz)
        sum_odstep += x
        time.sleep(x)
        bucket.dodaj_zetony()
        # print "Zetonow w wiadrze: %s" % bucket.iz


def main():
    t1 = Thread(target=generator_zgloszen)
    t2 = Thread(target=uzupelnij_wiadro)
    t2.start()
    t1.start()

if __name__ == '__main__':
    print main()
