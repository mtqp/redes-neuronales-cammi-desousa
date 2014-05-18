import sys
import numpy as np
import math
from DataSetCreator import DataSetCreator
from pprint import pprint
from HebbianLearning import HebbianLearning
from conditions.EpochAmountCondition import EpochAmountCondition
from MatrixVisualizer import MatrixVisualizer
import time

def main():

    '''
    n = 6
    m = 4
    etta = 0.17
    hebbianLearning = HebbianLearning(n, m, etta)
    matrix = hebbianLearning.createRandomMatrix(n, m)
    vTest = MatrixVisualizer(n, m)
    vTest.visualize(matrix)
    #while True:
    #    vTest.printMatrix()
    '''


    #Algorithm parameters
    n = 6
    m = 4
    etta = 0.0017
    amountOfRandomSets = 100
    endCondition = EpochAmountCondition()

    dataSetCreator = DataSetCreator(n)
    dataSet = dataSetCreator.getRandomDataSet(amountOfRandomSets)
    pprint(dataSet)
    pprint('boundVector')
    pprint(dataSetCreator.boundVector)

    hebbianLearning = HebbianLearning(n , m, etta, endCondition )
    dataSet = DataSetCreator(n).getRandomDataSet(amountOfRandomSets)
    time.sleep(5)

    #runHebb(hebbianLearning, dataSet)
    #runOja1(hebbianLearning, dataSet)
    #runOjaM(hebbianLearning, dataSet)
    runSanger(hebbianLearning, dataSet)

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
    return j


if __name__ == "__main__":
    main()
