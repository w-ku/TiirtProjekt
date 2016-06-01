import numpy as np
import matplotlib.pyplot as plt


class TokenGenerator(object):
    def generate_onOff(self, On):
        r = np.random.exponential(On)
        return r
        
    def generate_ts(self, lam):
        x = (1.0/lam)
        r = np.random.exponential(x)
        return r

    def generate(self, lam, sample_size):
        s = np.random.poisson(lam,sample_size)
        return s
