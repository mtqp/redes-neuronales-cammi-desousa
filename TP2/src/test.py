import sys
import numpy as np
import math
from DataSetCreator import DataSetCreator
from pprint import pprint
import time
from HebbianLearning import HebbianLearning
from conditions.EpochAmountCondition import EpochAmountCondition
from MatrixVisualizer import MatrixVisualizer
import time
from SelfOrganizedMap import SelfOrganizedMap
from utils.Utils import Utils

prefix = ' ---------------------- '
posfix = ' ---------------------- '

def main():
    #vector = vector.reshape((2, 3))

    beginTests()
    subtractMatricesTest()
    subtractVectorToEachColumnOfTest()
    applyNormToEachColumnTest()
    activateTest()
    endTests()

def beginTests():
    print ''
    print prefix + 'Begining Tests' + posfix
    print ''

def endTests():
    print ''
    print prefix + 'End Tests' + posfix
    print ''

def subtractMatricesTest():
    #Parameters
    matrix = np.matrix('2 4; 2 4; 2 4')
    vector = np.matrix('2; 2; 2')

    #Function call
    matrixDifference = Utils().subtractMatrices(matrix, vector)

    #Validation
    result = (matrixDifference == np.matrix('0 2; 0 2; 0 2')).all()

    #Print result
    print 'subtractMatricesTest: ' + str(result)

def subtractVectorToEachColumnOfTest():
     #Parameters
    matrix = np.matrix('2 4; 2 4; 2 4')
    vector = [2,2,2]

    #Function call
    matrixDifference = Utils().subtractVectorToEachColumnOf(matrix, vector)

    #Validation
    result = (matrixDifference == np.matrix('0 2; 0 2; 0 2')).all()

    #Print result
    print 'subtractVectorToEachColumnOfTest: ' + str(result)

def applyNormToEachColumnTest():
    #Parameters
    matrix = np.matrix('3 4; 3 4; 3 4')

    #Function call
    matrixWithNorm = Utils().applyNormToEachColumn(matrix)

    #Validation
    result = (matrixWithNorm == [5.196152422706632, 6.9282032302755088])

    #Print result
    print 'applyNormToEachColumnTest: ' + str(result)


def activateTest():
    #Parameters
    epochs = 1
    alphaEtta = 1
    alphaSigma = 1
    n = 1
    m1 = 4
    m2 = 5

    map = SelfOrganizedMap(epochs,alphaEtta,alphaSigma,n,m1,m2)
    #map.matrix = np.matrix('1 2 3 4 5; 6 7 8 9 10; 11 12 13 14 15; 16 17 18 19 20')
    #Function call
    vector = [2,2,2]
    yVector = map.activate(vector)

    #Validation
    result = len(yVector) and (yVector.count(1) == 1)

    #Print result
    print 'activateTest: ' + str(result)

def demoTest():
    #Parameters
    #Function call
    #Validation
    result = "OK"
    #Print result
    print 'demoTest: ' + str(result)

if __name__ == "__main__":
    main()
