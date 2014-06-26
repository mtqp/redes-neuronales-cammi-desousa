import time
import numpy as np
from HopefieldStochastic import HopefieldStochastic
from DataSetCreator import *
from Letter import Letter
import Hamming
from MemoryCheck import MemoryCheck
from SpuriousChecker import SpuriousChecker

def main():
    dim = 10
    n = dim * dim
    temperature = 0.2
    hammingPercentage = 0.1
    trainingSetCount = 10
    activationSetCount = 1000
    noiseFactor = 0.01
    MUST_BE_UNIQUE = True
    #hopfieldStochastic = HopefieldStochastic(n, temperature, hammingPercentage, HopefieldStochastic.ACTIVATION_STOP_BY_HAMMING_CONDITION)
    hopfieldStochastic = HopefieldStochastic(n, temperature, hammingPercentage, HopefieldStochastic.ACTIVATION_STOP_BY_PROBABILITY_CONDITION)

    #DataSet
    dataSetCreator = DataSetCreator(n)
    print 'Creating training set'
    trainingSet = dataSetCreator.getRandomDataSetOfVectors(trainingSetCount, -1, 1, DataSetCreator.UNIFORM, MUST_BE_UNIQUE)
    print 'Ready!'

    print 'Creating activation set'
    activationSet = dataSetCreator.getRandomDataSetOfVectors(activationSetCount, -1, 1, DataSetCreator.UNIFORM, MUST_BE_UNIQUE)
    print 'Ready!'

    #Activation with random sets
    hopfieldStochastic.training(trainingSet)

    spuriousChecker = SpuriousChecker(trainingSet, hammingPercentage)

    while temperature <= 0.7:
        print 'Temperature: ' + str(temperature)
        #Activation
        for i in range(0, len(activationSet)):
            #print 'Activando vector i=' + str(i)
            activationVector = activationSet[i]
            hopfieldStochastic.temperature = temperature
            hopfieldActivation = hopfieldStochastic.activate(activationVector)
            spuriousChecker.addActivation(hopfieldActivation)

        spuriousChecker.showResults()
        spuriousChecker.clearActivations()
        temperature += 0.05

    #----------------------------------------------
    #Learning and testing of memories
    '''
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
    '''

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

def memoryCheck(hopfieldStochastic, trainingSet, checkingSet, dim, temperature, noiseFactor):
    check = MemoryCheck(temperature, noiseFactor, trainingSet, checkingSet)

    #Activation
    for i in range(0, len(trainingSet)):
        trainingVector = trainingSet[i]
        checkingVector = checkingSet[i].flatten()
        hopfieldStochastic.temperature = temperature
        hopfieldActivation = hopfieldStochastic.activate(trainingVector)
        equalityReached = (checkingVector == hopfieldActivation).all()
        hammingDist = Hamming.distance(hopfieldActivation.flatten(), checkingVector)
        check.addActivationResult(i, equalityReached, hammingDist)

    return check

if __name__ == "__main__":
    main()
