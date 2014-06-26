import numpy as np
import math
import Hamming
import matplotlib as mpl
import matplotlib.pyplot as plt
from pylab import *

class HopefieldStochastic:
    #s vector de activacion
    #x vectores de aprendizaje (1 sola iteracion) son los patrones que se quieren memorizar
    ACTIVATION_STOP_BY_HAMMING_CONDITION = 0
    ACTIVATION_STOP_BY_PROBABILITY_CONDITION = 1

    def __init__(self, n, temperature, hammingPercentageDifference, stopCondition):
        self.n = n
        self.matrix = np.zeros((self.n, self.n))
        self.hammingPercentageDifference = hammingPercentageDifference
        if temperature == 0:
            temperature = 0.01
        self.temperature = temperature
        self.stopCondition = stopCondition
        self.randomActivationConditionStopper = RandomActivationConditionStopper(hammingPercentageDifference)
        self.energies = []
        self.iEnergy = 0
        ion()
        self.f = None
        self.p1 = None
        self.p2 = None
        self.plots = []

    def training(self, dataSet):
        for x in dataSet:
            transposedX = np.transpose(x)
            self.matrix += transposedX * x
        self.matrix /= self.n
        self.matrix -= np.diag(np.diag(self.matrix))
        return self.matrix

    def addEnergy(self, s, matrix):
        energy = -0.5 * (np.dot(np.dot(s,matrix),np.transpose(s)))
        self.energies.append( energy[0][0])
        self.iEnergy += 1

    def activate(self, x):
        #self.f, (self.p1, self.p2) = plt.subplots(nrows = 2)
        self.f, self.p1 = plt.subplots()
        self.iEnergy = 0
        self.energies = []

        #s = x
        s = np.zeros((1,self.n))
        for i in range(0, len(x)):
            s[i] = x[i]

        previousS = np.zeros((1,self.n))

        while not self.shouldStop(s, previousS):
            for i in range(0, len(s)):
                previousS[i] = s[i]

            permIndexes = np.random.permutation(self.n)

            for i in permIndexes:
                s[0, i] = self.stochasticActivation(s, self.matrix[:,i])

            self.addEnergy(s,self.matrix)
            self.visualizeEnergy(s)

        self.plots.append((self.f,self.p1,self.p2))
        return s

    def stochasticActivation(self, s, matrix_i):
        h_i = np.dot(s,matrix_i)
        mu = np.random.uniform(0,1)
        probability_i  = self.temperatureProbability(h_i)
        return self.sign(probability_i - mu)

    def temperatureProbability(self, value):
        exponent = (-1.0) * value / self.temperature
        return 1.0 / (1.0 + (math.pow(math.e,exponent)))

    def shouldStop(self, s, previousS):
        if self.stopCondition == HopefieldStochastic.ACTIVATION_STOP_BY_HAMMING_CONDITION:
            maxDifference = int(self.n * self.hammingPercentageDifference)
            return Hamming.distance(s.flatten(), previousS.flatten()) <= maxDifference
        else:
            return self.randomActivationConditionStopper.shouldStop(s, self.iEnergy)

    def vectorSign(self, vector):
        print 'vector: ' + str(vector)
        signs = [self.sign(x) for x in vector]
        print 'signs: ' + str(signs)
        return signs

    def sign(self, item):
        if item >= 0:
            return 1
        else:
            return -1

    def visualizeEnergy(self, s):
        self.p1.clear()
        x = [i for i in range(0, self.iEnergy)]
        self.p1.plot(x, self.energies)
        self.p1.set_ylabel('Energia')
        self.p1.set_title('Energia en funcion de las iteraciones')
        self.p1.set_xlabel('Iteraciones')

        draw()

class RandomActivationConditionStopper:
    def __init__(self, hammingPercentage):
        self.timeCount = 0
        self.timeCountLoops = 0
        self.partialResults = []
        self.hammingPercentage = hammingPercentage

    def shouldStop(self, partialResult, iterationCount):
        partialResult = partialResult.flatten()
        if iterationCount > 250:
            return True
        if self.timeCount < 8:
            self.timeCount += 1
            return False

        self.partialResults.append(partialResult)
        self.timeCount = 0
        self.timeCountLoops += 1

        if self.timeCountLoops > 10:
            hitPercentage = sum([1
                                 for vector
                                 in self.partialResults
                                 if Hamming.distance(vector, partialResult)/100.0 < self.hammingPercentage
                                ]) \
                            / float(len(self.partialResults))
            #print 'hit percentage: ' + str(hitPercentage)
            itsAMatch = hitPercentage > 0.7
            if itsAMatch:
                self.partialResults = []
            return itsAMatch
        return False

