import sys
import numpy as np
import math
from DataSetCreator import DataSetCreator
from pprint import pprint
from HebbianLearning import HebbianLearning

def main():
    nDimensionOfWeightMatrix = 6
    mDimensionOfWeightMatrix = 4
    etta = 0.1
    amountOfRandomSets = 100

    dataSetCreator = DataSetCreator(nDimensionOfWeightMatrix)
    dataSet = dataSetCreator.getRandomDataSet(amountOfRandomSets)
    pprint(dataSet)
    pprint('boundVector')
    pprint(dataSetCreator.boundVector)

    hebbianLearning = HebbianLearning(nDimensionOfWeightMatrix , mDimensionOfWeightMatrix, etta )
    dataSet = DataSetCreator(nDimensionOfWeightMatrix).getRandomDataSet(amountOfRandomSets)
    runHebb(hebbianLearning, dataSet)


def runHebb(hebbianLearning, dataSet):
    hebbianLearning.algorithm(dataSet, hebbRule)

def runOja1(hebbianLearning, dataSet):
    hebbianLearning.algorithm(dataSet, oja1Rule)

def runOjaM(hebbianLearning, dataSet):
    hebbianLearning.algorithm(dataSet, ojaMRule)

def runSanger(hebbianLearning, dataSet):
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
