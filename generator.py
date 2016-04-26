import numpy as np
import matplotlib.pyplot as plt


class TokenGenerator(object):
	def __init__(self):
		pass

	def generate(self, lam, sample_size):
		s = np.random.poisson(lam,sample_size)
		return s

	def histogram(self, lam, sample_size):
		s = self.generate(lam,sample_size)
		count, bins, ignored = plt.hist(s, normed=True)
		plt.show()
		return [count, bins, ignored]
