import numpy as np
from HopefieldStochastic import HopefieldStochastic
from DataSetCreator import *
from Letter import Letter
import Hamming

''''
    todo: GENERAR LOS 10 VECTORES,
    GENERAR LAS INSTANCIAS DE TEST
    LOOPEAR TODO PARA DISTINTAS TEMPERATURAS
'''

def main():

    dim = 10
    n = dim * dim
    temperature = 0
    hammingPercentage = 0.05
    trainingSetCount = 10
    noiseFactor = 0.01
    MUST_BE_UNIQUE = True
    hopfieldStochastic = HopefieldStochastic(n, temperature, hammingPercentage)

    #DataSet
    dataSetCreator = DataSetCreator(n)
    print 'Creating training set'
    trainingSet = dataSetCreator.getRandomDataSetOfVectors(trainingSetCount, -1, 1, DataSetCreator.UNIFORM, MUST_BE_UNIQUE)
    print 'Ready!'

    #Learning
    hopfieldStochastic.training(trainingSet)

    while temperature <= 0.7:
        checks = []
        print 'Temperature: ' + str(temperature)
        print 'Memory'
        memoryCheck(hopfieldStochastic, trainingSet, trainingSet, dim, temperature, 0).results()

        if temperature > 0:
            print 'Memory with noise'
        while noiseFactor <= 0.7 and temperature > 0:
            trainingSetWithNoise = noiseUp(trainingSet, noiseFactor)
            checks.append(memoryCheck(hopfieldStochastic, trainingSetWithNoise, trainingSet, dim, temperature, noiseFactor))
            noiseFactor += 0.1

        for check in checks:
            check.results()

        noiseFactor = 0.01
        temperature += 0.05


def hammingDistances(set, setWithNoise):
    distances = []
    for i in range(0, len(set)):
        distances.append(Hamming.distance(set[i].flatten(), setWithNoise[i].flatten()))
    return distances

def noiseUp(set, noiseFactor):
    noisedUpSet = []
    for item in set:
        copiedItem = copyItem(item)
        for i in range(0,len(copiedItem.flatten())):
            randomValue = np.random.uniform(0,1)
            if randomValue <= noiseFactor:
                copiedItem[0,i] = -1 * copiedItem[0,i] #reverse item

        noisedUpSet.append(copiedItem)
    return noisedUpSet

def copyItem(item):
    copiedItem = np.zeros((1,len(item.flatten())))
    for i in range(0, len(item.flatten())):
        copiedItem[0, i] = item[0, i]
    return copiedItem

class MemoryCheck:
    def __init__(self, temperature, noise, trainingSet, checkingSet):
        self.temperature = temperature
        self.noise = noise
        self.distances = hammingDistances(trainingSet, checkingSet)

        self.activationResults = []

    def addActivationResult(self, i, equalityReached, hammingDist):
        self.activationResults.append((i, equalityReached, hammingDist))
        '''
        description = 'Vector: ' + str(i) + '. Are equal? ' + str(equalityReached)
        if not equalityReached:
            description += ' - ERROR! - Hamming distance: ' + str(hammingDist)
        print description
        '''

    def results(self):
        maxHammingDist = max(self.distances)
        minHammingDist = min(self.distances)
        avgHammingDist = sum(self.distances) / len(self.distances)
        successFactor = sum([ float(activationResult[1]) for activationResult in self.activationResults ])/len(self.activationResults)
        failFactor = 1.0 - successFactor
        hammingImprovements = [ abs((self.distances[i] - self.iActivationResult(i)[2])) for i in range(0, len(self.distances))]
        '''
        if self.noise > 0:
            print 'With noise: ' + str(self.noise) + ' maxHam: ' + str(maxHammingDist) + ' minHam: ' + str(minHammingDist) + ' avgHam: ' + str(avgHammingDist)
        print ' Success: ' + str(successFactor) + ' - Fail: ' + str(failFactor)
        print ' Hamming dists improvement: Max: ' + str(min(hammingImprovements)) +  ' Min: ' + str(max(hammingImprovements)) + ' Avg: ' + str(sum(hammingImprovements)/len(hammingImprovements))
        '''
        print 'N: ' + str(self.noise) + ' MH: ' + str(maxHammingDist) + ' mH: ' + str(minHammingDist) + ' A: ' + str(avgHammingDist) + ' S: ' + str(successFactor) + ' F: ' + str(failFactor) + ' HImprove: M: ' + str(min(hammingImprovements)) +  ' m: ' + str(max(hammingImprovements)) + ' A: ' + str(sum(hammingImprovements)/len(hammingImprovements))

    def iActivationResult(self, i):
        for activationResult in self.activationResults:
            if activationResult[0] == i:
                return activationResult

def memoryCheck(hopfieldStochastic, trainingSet, checkingSet, dim, temperature, noiseFactor):
    check = MemoryCheck(temperature, noiseFactor, trainingSet, checkingSet)

    PRINT_DETAIL = False
    #Activation
    for i in range(0, len(trainingSet)):
        trainingVector = trainingSet[i]
        checkingVector = checkingSet[i].flatten()
        hopfieldStochastic.temperature = temperature
        hopfieldActivation = hopfieldStochastic.activate(trainingVector)
        equalityReached = (checkingVector == hopfieldActivation).all()
        hammingDist = Hamming.distance(hopfieldActivation.flatten(), checkingVector)
        check.addActivationResult(i, equalityReached, hammingDist)

        if PRINT_DETAIL and not equalityReached:
            printVectorWithDimension("DataSet", dim, trainingSet[i].flatten())
            printVectorWithDimension("Result", dim, hopfieldActivation.flatten())

    return check

def printVectorWithDimension(header, dim, vector):
    print header

    for i in range(0, len(vector), dim):
        vectorLine = vector[i:i+dim]
        vectorLine = [int(v) for v in vectorLine]
        for vi in range(0,len(vectorLine)):
            if(vectorLine[vi] == -1):
                vectorLine[vi] = 0

        print vectorLine

def showVectors(dataSetVectors):
    print 'vectors:'
    i = 0
    for it in dataSetVectors:
        print str(i+1) + ') ' + str(it)
        i += 1

def allLetters():
    letters = []
    letters.append(Letter("A", [0,1,1,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1]))
    letters.append(Letter("B", [1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,0,0,0,1,1,1,1,1,0]))
    letters.append(Letter("C", [0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,1,1]))
    letters.append(Letter("D", [1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0]))
    letters.append(Letter("E", [1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,1,1,1,1]))
    letters.append(Letter("F", [1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0]))
    letters.append(Letter("G", [0,1,1,1,1,1,0,0,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,1,0]))
    letters.append(Letter("H", [1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1]))
    letters.append(Letter("I", [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]))
    letters.append(Letter("J", [0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0]))
    letters.append(Letter("K", [1,0,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1]))
    letters.append(Letter("L", [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1]))
    letters.append(Letter("M", [1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,0,1]))
    letters.append(Letter("N", [1,0,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,1]))
    letters.append(Letter("O", [0,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0]))
    letters.append(Letter("P", [1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,0,0,0,0,1,0,0,0,0]))
    letters.append(Letter("Q", [0,1,1,1,0,1,0,0,0,1,1,0,1,0,1,1,0,0,1,0,0,1,1,0,1]))
    letters.append(Letter("R", [1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,1]))
    letters.append(Letter("S", [0,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,0]))
    letters.append(Letter("T", [1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]))
    letters.append(Letter("U", [1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0]))
    letters.append(Letter("V", [1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0]))
    letters.append(Letter("W", [1,0,0,0,1,1,0,0,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1]))
    letters.append(Letter("X", [1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1]))
    letters.append(Letter("Y", [1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]))
    letters.append(Letter("Z", [1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1]))
    return letters

if __name__ == "__main__":
    main()
