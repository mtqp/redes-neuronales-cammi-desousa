import numpy as np
import math
import Hamming

#todo: make it work!!
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

    def training(self, dataSet):
        for x in dataSet:
            transposedX = np.transpose(x)
            self.matrix += transposedX * x
        self.matrix /= self.n
        self.matrix -= np.diag(np.diag(self.matrix))
        return self.matrix

    def energy(self, s, matrix):
        return -0.5 * ((s * matrix) * np.transpose(s))

    def activate(self, x):
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

            energyValue = self.energy(s,self.matrix)
            self.visualizeEnergy(energyValue,s)

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
            return self.randomActivationConditionStopper.shouldStop(s)

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

    def visualizeEnergy(self,energyValue, s):
        #print "energyValue: " + str(energyValue)
        #print "s value: " + str(s)
        return None

class RandomActivationConditionStopper:
    def __init__(self, hammingPercentage):
        self.timeCount = 0
        self.timeCountLoops = 0
        self.partialResults = []
        self.hammingPercentage = hammingPercentage

    def shouldStop(self, partialResult):
        partialResult = partialResult.flatten()
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
            itsAMatch = hitPercentage > 0.65
            if itsAMatch:
                self.partialResults = []
            return itsAMatch
        return False

