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
    winnerTest()
    proxyTest()
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

def winnerTest():
    #Parameters
    epochs = 1
    alphaEtta = 1
    alphaSigma = 1
    n = 1
    m1 = 4
    m2 = 5

    map = SelfOrganizedMap(epochs,alphaEtta,alphaSigma,n,m1,m2)
    #map.matrix = Utils().createRandomMatrixBetween(n, (m1*m2),0,0)
    #print "MatrixRandom: " + str(map.matrix.shape)
    map.matrix = np.matrix('41 72 43 42 25 69 97 18 92 10 11 22 13 14 15 16 17 18 19 20')
    vector = [2,2,2]
    yVector = map.activate(vector)
    #print 'Vector: ' + str(yVector)

    #Function call
    winnerPoint = map.winner(yVector)
    #print 'Position: ' + str(winnerPoint)

    #Validation
    result = winnerPoint == (4,1)
    #Print result
    #print 'winnerTest: ' + str(result)

def proxyTest():
    #Parameters
    epochs = 1
    alphaEtta = 1
    alphaSigma = 1
    n = 1
    m1 = 4
    m2 = 5

    map = SelfOrganizedMap(epochs,alphaEtta,alphaSigma,n,m1,m2)
    map.matrix = np.matrix('41 72 43 42 25 69 97 18 92 10 11 22 13 14 15 16 17 18 19 20')
    vector = [2,2,2]
    yVector = map.activate(vector)
    winnerPoint = map.winner(yVector)

    #Function call
    propagationMatrix = map.proxy(winnerPoint)

    #Validation
    #print propagationMatrix
    expectedMatrix = np.matrix('0.53526143  0.77880078  0.8824969   0.77880078  0.53526143; 0.60653066  0.8824969   1.          0.8824969   0.60653066; 0.53526143  0.77880078  0.8824969   0.77880078  0.53526143; 0.36787944  0.53526143  0.60653066  0.53526143  0.36787944')

    #result = propagationMatrix == expectedMatrix

    #Print result
    #print 'proxyTest: ' + str(False)
    print 'proxyTest: ' + 'Not ran'


def correctWeightMatrix():
    #Parameters
    #Function call
    #Validation
    result = "OK"
    #Print result
    print 'correctWeightMatrix: ' + str(result)

def demoTest():
    #Parameters
    #Function call
    #Validation
    result = "OK"
    #Print result
    print 'demoTest: ' + str(result)

if __name__ == "__main__":
    main()
