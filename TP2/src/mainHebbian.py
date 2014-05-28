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

    '''
    #Check variance of proyections and covariance matrix is orthogonal
    dataSetCreator = DataSetCreator(n)
    dataSet = dataSetCreator.getRandomDataSet(5)

    proyectionVariance = []
    for a in range(n,0,-1):
        proyectionVariance.append((a**2)/(n/2))
        for x in dataSet:
            proyectionVariance.append((np.array(x)**2).sum()/n)

    visualizer=MatrixVisualizer(n,1)
    visualizer.plot2d(np.asmatrix(proyectionVariance))

    x = num.random.uniform( -5, 5, (1,10000))
    y = num.random.uniform( -3, 3, (1,10000))
    (x*y).sum()/10000
'''


    n = 6
    m = 4
    #Algorithm parameters
    etta = 0.00017 #--> funciono para sanger
    #etta = 0.000016
    amountOfRandomSets = 50
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
    #runOjaM(hebbianLearning, dataSet)
    runSanger(hebbianLearning, dataSet)

    trainingAnalyzer = HebbianTrainingAnalyzer(hebbianLearning.matrix, dataSet)
    trainingAnalyzer.results()
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
