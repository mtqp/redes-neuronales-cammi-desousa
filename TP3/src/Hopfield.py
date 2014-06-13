import numpy as np

class Hopfield:

    def __init__(self, n):
         self.n = n
         self.matrix = np.zeros((self.n,self.n))

def training(self, dataSet):
    for x in dataSet:
        self.matrix += np.transpose(x)*x
    self.matrix /= self.n
    self.matrix -= self.matrix.diagonal(0)
    return self.matrix

def energy(self, s, matrix):
    return -0.5 * ((s * matrix) * np.transpose(s))

def activate(self, x, synch):

    s = x
    previousS = np.zeros((1,self.n))

    while previousS != s:
        previousS[:] = s