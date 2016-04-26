import clock as zegar

class Bucket(object):
	"""Wiadro z zetonami"""
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
			self.iz = self.iz - 1
		
		return self.iz

	def dodaj_zetony(self):
		if (self.iz + self.vz) <= self.lz:
			self.iz = self.iz + self.vz
		else:
			self.iz = self.lz
		print "Dodano zeton do wiadra."
		return self.iz

	def check_zetony(self):
		return self.iz

