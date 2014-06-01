import sys
import numpy as np
import math
from DataSetCreator import DataSetCreator
from pprint import pprint
import time
from HebbianLearning import HebbianLearning
from conditions.EpochAmountCondition import EpochAmountCondition
from MatrixVisualizer import MatrixVisualizer
from HebbianTrainingAnalyzer import HebbianTrainingAnalyzer
import time
from SelfOrganizedMap import SelfOrganizedMap

def main():

    nTest = 2
    nRandomTest = 25000
    #print 'Varianza de proyecciones'
    #Check variance of proyections
    dataSetCreator = DataSetCreator(nTest)
    dataSet = dataSetCreator.getRandomDataSet(nRandomTest)

    '''
    proyectionVariance = []
    for i in range(0, nTest):
        print 'i: ' + str(i)
        iExpectedVariance = (dataSetCreator.boundVector[i]**2)/3.0
        print str(iExpectedVariance) + ' --> a_i ^ 2 / 3'
        proyectionVariance.append(iExpectedVariance)

        iComponents = np.array([ x[i] for x in dataSet ])
        iComponentVariance = (iComponents**2).sum()/nRandomTest
        print str(iComponentVariance) + ' --> dataSetVariance'

    '''
    #Check covariance matrix is orthogonal
    print 'Ortogonalidad matrix'
    firstValueOfEachVector = np.array([ x[0] for x in dataSet])
    secondValueOfEachVector = np.array([ x[1] for x in dataSet])
    print (firstValueOfEachVector * secondValueOfEachVector).sum()/nRandomTest


    '''
    n = 6
    m = 4
    #Algorithm parameters
    etta = 0.0017 #--> funciono para sanger
    #etta = 0.000016
    amountOfRandomSets = 1000
    endCondition = EpochAmountCondition()

    dataSetCreator = DataSetCreator(n)
    dataSet = dataSetCreator.getRandomDataSet(amountOfRandomSets)
    #pprint(dataSet)
    pprint('Bound vector')
    pprint(dataSetCreator.boundVector)

    hebbianLearning = HebbianLearning(n , m, etta, endCondition )
    dataSet = DataSetCreator(n).getRandomDataSet(amountOfRandomSets)

    #runHebb(hebbianLearning, dataSet)
    #runOja1(hebbianLearning, dataSet)
    runOjaM(hebbianLearning, dataSet)
    #runSanger(hebbianLearning, dataSet)

    trainingAnalyzer = HebbianTrainingAnalyzer(hebbianLearning.matrix, dataSet)
    trainingAnalyzer.results()
    '''

    '''
    matrix = np.array([[1,2], [3,4], [5,6]])
    matrix = np.asmatrix(matrix)
    x = [[1,2,3]]
    trainingAnalyzer = HebbianTrainingAnalyzer(matrix, x)
    trainingAnalyzer.results()
    '''

def runHebb(hebbianLearning, dataSet):
    pprint('---Hebb---')
    hebbianLearning.algorithm(dataSet, hebbRule)

def runOja1(hebbianLearning, dataSet):
    pprint('---Oja1---')
    hebbianLearning.algorithm(dataSet, oja1Rule)

def runOjaM(hebbianLearning, dataSet):
    pprint('---runOjaM---')
    hebbianLearning.algorithm(dataSet, ojaMRule)

def runSanger(hebbianLearning, dataSet):
    pprint('---runSanger---')
    hebbianLearning.algorithm(dataSet, sangerRule)

def hebbRule(j, m):
    return 0

def oja1Rule(j, m):
    return 1

def ojaMRule(j, m):
    return m

def sangerRule(j, m):
    return j+1


if __name__ == "__main__":
    main()
