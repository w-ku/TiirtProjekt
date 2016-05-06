#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zgloszenie import Zgloszenie
from generator import TokenGenerator
from modul_decydujacy import DecisionModule
from bucket import Bucket
from kolejka import Queue
import time
import threading


# start = time.time()
SAMPLE_SIZE = 40
tablica_zgloszen = []
tc = TokenGenerator()
dm = DecisionModule()
bucket = Bucket(4,40,35)
kolejka = Queue(100,3)


if __name__ == "__main__":

	total = 0

	for i in xrange(SAMPLE_SIZE):
		print "DLA %s : " % (i+1)
		i_sample = tc.generate(2,1)
		print " I_SAMPLE: %s : " % i_sample
		wygenerowane = 0
		for x in xrange(i_sample):
			gen = Zgloszenie("pending", None, None)
			print gen
			dm.make_decision(gen, bucket, kolejka)
			
			wygenerowane += 1
		print "Wygenerowano: %s zgloszen" % wygenerowane
		print "ZETONY W WIADRZE: %d " % (bucket.iz)
		total += wygenerowane
		time.sleep(0.1)

	print "Wszystkie wygenerowane zgłoszenia: %s" % total




# print("--- time ---")
# end = time.time() - start
# print end