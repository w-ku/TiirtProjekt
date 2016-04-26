

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
		if len(self.zgloszenia) < self.lq:
			self.zgloszenia.append(zgloszenie)
			self.iq += 1
		else:
			print "Zgloszenie odrzucone"
			# Odrzucone_zgloszenia += 1

	def zwolnij_kolejke(self):
		# tutaj zegar 
		if len(zgloszenia) > 0:
			first_el = zgloszenia[0]
			self.zgloszenia.pop(0)
			self.iq -= 1
			return first_el
		else:
			print "Kolejka pusta"

