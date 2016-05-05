#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ticket import Ticket
from generator import TokenGenerator
from decision import DecisionModule
from bucket import Bucket
from kolejka import Queue
import time
import threading


# start = time.time()
SAMPLE_SIZE = 4000000
LAMBDA = 20
tablica_zgloszen = []
tc = TokenGenerator()
dm = DecisionModule()
bucket = Bucket(4,40,35)
kolejka = Queue(4,3)
sum_odstep = 0

if __name__ == "__main__":
	start = time.time()
	total = 0

	for i in xrange(SAMPLE_SIZE):
			
		

		print "---------------------------------------"
		print "DLA %s : " % (i+1)
		# i_sample = tc.generate(2,1)
		# print " I_SAMPLE: %s : " % i_sample
		
		# wygenerowane = 0
		# for x in xrange(i_sample):
		
		gen = Zgloszenie("pending", None, None)
		print gen.__dict__
		dm.make_decision(gen, bucket, kolejka)
		
		# wygenerowane += 1
		
		# print "Wygenerowano: %s zgloszen" % wygenerowane
		print "ZETONY W WIADRZE: %d " % (bucket.iz)
		# total += wygenerowane
		print "ZGLOSZENIA W KOLEJCE: %s" % kolejka.iq
		
		# losowanie odstepu czasowego
		odstep = tc.generate_ts(LAMBDA)
		sum_odstep = sum_odstep + odstep
		print "Opoznienie na odstepie: %s" % sum_odstep
		print "Odstep: %s" % odstep
		time.sleep(odstep)

		print "Działanie programu: %s" % (time.time()-start)


	# print "Wszystkie wygenerowane zgłoszenia: %s" % total




# print("--- time ---")
# end = time.time() - start
# print end