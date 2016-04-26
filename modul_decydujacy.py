#!/usr/bin/env python
# -*- coding: utf-8 -*-

class DecisionModule(object):
	def __init__(self ):
		self.obsluzone = []
	
	def make_decision(self, zgloszenie, bucket, kolejka):
		print "Wywołuje moduł decyzyjny:"
	
		if bucket.check_zetony() > 0:
			if len(kolejka.zgloszenia) > 0:
				obsluzone_zgloszenie = kolejka.zwolnij_kolejke()
				self.obsluzone.append(obsluzone_zgloszenie)
				bucket.odejmij_zetony()
			else:
				self.obsluzone.append(zgloszenie)
				bucket.odejmij_zetony()

			print "Zgloszenie obsluzone"
		else:
			kolejka.dodaj_do_kolejki(zgloszenie)
			print "Zgloszenie dodane do kolejki"

		print "Już obsłużono: %s " % len(self.obsluzone )



		# dla kazdego I_SAMPLE sprawdzamy ile ma zgloszen, OK
			# czy sa zetony w wiadrze + kolejka(czy jest miejsce)
			# nadajemy czasy_otrzymania i akceptacji dla each zgloszenia


	# ogarnac ile zgloszen pojdzie do kolejki a ile przejdzie
	# dodaj zgloszenie do kolejki