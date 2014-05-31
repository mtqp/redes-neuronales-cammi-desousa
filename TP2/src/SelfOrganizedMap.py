import numpy as np
import random
import math
from utils.Utils import Utils
from MatrixVisualizer import MatrixVisualizer
import time
from copy import copy, deepcopy
import pylab as P

class SelfOrganizedMap:

    def __init__(self, epochs, alphaEtta, alphaSigma, n, m1, m2, random1, random2):
        self.epochs = epochs
        self.alphaEtta = alphaEtta
        self.alphaSigma = alphaSigma
        self.etta = 0.001 #es correcto inicializarlo con frula?
        self.sigma = 0.01 #es correcto inicializarlo con frula?
        self.n = n
        self.m1 = m1
        self.m2 = m2
        self.matrix = Utils().createRandomMatrixBetween(n, (m1*m2),random1, random2)

    def algorithm(self, dataSet):
        #vTest = MatrixVisualizer(self.n, self.m1*self.m2)
        runningEpoch = 1

        while runningEpoch < self.epochs:
            self.updateEtta(runningEpoch)
            self.updateSigma(runningEpoch)

            if(runningEpoch % 20 == 0):
                print 'epoch ' + str(runningEpoch)

            for x in dataSet:
                #print counter
                #print 'Etta :' + str(self.etta)
                #print 'Sigma:' + str(self.sigma)

                visualMatrix  = deepcopy(self.matrix)
                #print "learning matrix: " + str(visualMatrix.shape)
                #print str(visualMatrix)
                #vTest.visualize(visualMatrix.reshape((self.n,self.m1*self.m2,)))
                #vTest.visualize(visualMatrix)
                self.correctWeightMatrix(x)
                #time.sleep(0.5)
            runningEpoch += 1

    def test(self, dataSet):
        print '--------------- testing step ---------------- '
        #vTest = MatrixVisualizer(self.m1*5,self.m2*5)
        vTest = MatrixVisualizer(5,5)

        acumWinnerMatrix = np.zeros((self.m1,self.m2))

        counter = 0
        neuralAcumVector = []
        for x in dataSet:
            counter = counter + 1
            #GET WINNER MATRIX
            #print 'Point: ' + str(x)
            y = self.activate(x)
            #print 'Y: ' + str(y)
            winnerPoint = self.winner(y)

            print 'Winner Point: ' + str(winnerPoint)
            winnerMatrix = self.proxy(winnerPoint)

            print 'Testing iteration: ' + str(counter)
            print 'winnerMatrix: ' + str(winnerMatrix.shape)
            print winnerMatrix


            winnerId = (winnerPoint[0]*winnerMatrix.shape[1]) + winnerPoint[1]
            #print 'winnerMatrix.shape[0]' + str(winnerMatrix.shape[0])
            #print 'winnerMatrix.shape[1]' + str(winnerMatrix.shape[1])

            #print 'winnerId: (' + str(winnerPoint[0]) + ',' + str(winnerPoint[1]) + ') ' + str(winnerId)

            neuralAcumVector.append(winnerId)
            #vTest.visualizeWinnerMatrix(winnerMatrix, winnerMatrix.shape[0], winnerMatrix.shape[1],(5,5))

            #print 'reshape: ' + str(self.n) + ',' + str(self.m1*self.m2)
            #winnerMatrix.reshape(self.n,self.m1*self.m2)

            #GET matrix result
            #matrixResult = Utils().subtractVectorToEachColumnOf(self.matrix, x)
            #vTest.visualizeWithParams(matrixResult, matrixResult.shape[0], matrixResult.shape[1],(1,1))

            #GET matrix histogram
            acumWinnerMatrix += winnerMatrix


            #acumWinnerMatrixToDisplay  = deepcopy(acumWinnerMatrix.reshape(1,acumWinnerMatrix.shape[0]*acumWinnerMatrix.shape[1]))
            #vTest.visualizeWithParams(acumWinnerMatrixToDisplay, acumWinnerMatrixToDisplay.shape[0], acumWinnerMatrixToDisplay.shape[1], (6,0))

            vTest.visualizeNeuralPoints(winnerPoint, x)

            #print "visualizada"
            #time.sleep(1)
            #print "sleep paso"

        #acumWinnerMatrixToDisplay  = deepcopy(acumWinnerMatrix.reshape(1,acumWinnerMatrix.shape[0]*acumWinnerMatrix.shape[1]))
        #vTest.visualizeWithParams(acumWinnerMatrix, acumWinnerMatrix.shape[0], acumWinnerMatrix.shape[1], (6,0))

        print 'vector: ' + str(neuralAcumVector)
        vTest.plotHistogram(neuralAcumVector)

        #P.hist(anArray, 50, normed=1, histtype='stepfilled')
        #P.plot
        #vTest.plot2d(matrixHistogram)

    def updateEtta(self, epoch):
        self.etta = pow(epoch, -(self.alphaEtta))

    def updateSigma(self, epoch):
        self.sigma = pow(epoch, -(self.alphaSigma))

    def correctWeightMatrix(self, x):

        #print 'x vector: ' + str(x)
        y = self.activate(x)
        #print 'y vector: ' + str(y)
        point = self.winner(y)
        #print 'winner: ' + str(point)
        propagationMatrix = self.proxy(point)
        #print 'propagationMatrix: ' + str(propagationMatrix.shape)
        #print propagationMatrix

        #matrixDifference = Utils().subtractVectorToEachColumnOf(self.matrix, x)
        matrixDifference = Utils().subtractMatrixFromVector(self.matrix, x)
        #print 'matrixDifference: ' + str(matrixDifference.shape)
        #print matrixDifference


        #flattenPropagationMatrix = propagationMatrix.flatten()
        #print 'reshaping propagation matrix to (' + str(self.m1) + '*' + str(self.m2) + ',' + str(1) + ')'
        #print 'reshaping propagation matrix to (' + str(self.m1*self.m2) + ',' + str(self.n) + ')'
        flattenPropagationMatrix = propagationMatrix.reshape((self.n,self.m1*self.m2)) # es n porque es el vector de propagacion que ira multiplicando a cada fila de la matrix (cada una de las n matrices de m1.m2)

        #print 'flattenPropagationMatrix: ' + str(flattenPropagationMatrix.shape)
        #print flattenPropagationMatrix

        #print 'Etta: ' + str(self.etta)

        deltaMatrix = Utils().multiplyPositionToPosition(self.etta * matrixDifference, flattenPropagationMatrix)

        #print 'deltaMatrix: ' + str(deltaMatrix.shape)
        #print deltaMatrix


        self.matrix = self.matrix + deltaMatrix

        #print 'matrix: ' + str(self.matrix.shape)
        #print self.matrix

    #Devuelve  y (1, m1.m2)
    def activate(self, x):

        matrixDifference = Utils().subtractVectorToEachColumnOf(self.matrix, x)
        #print 'MatrixDifference: ' + str(matrixDifference)
        vectorOfNorms = Utils().applyNormToEachColumn(matrixDifference)
        #print 'vectorOfNorms: ' + str(vectorOfNorms)

        maskedVector = Utils().applyMaskForMinimumOn(vectorOfNorms)
        #print 'maskedVector: ' + str(maskedVector)

        return maskedVector

    def proxy(self, winnerPoint): #TODO: correct/check positions!

        gaussMatrix = np.zeros((self.m1, self.m2))
        #print gaussMatrix.shape
        #print 'winnerPoint[0]: ' + str(winnerPoint[0])
        #print 'winnerPoint[1]: ' + str(winnerPoint[1])

        gaussMatrix[winnerPoint[0]][winnerPoint[1]] = 1

        for columnIndex in range(0, gaussMatrix.shape[1]):
            for rowIndex in range(0, gaussMatrix.shape[0]):
                gaussMatrix[rowIndex][columnIndex] = self.gaussianFormula((rowIndex,columnIndex), winnerPoint)
        return gaussMatrix

    def gaussianFormula(self, point, winnerPoint):
        pointDifference = np.subtract(point, winnerPoint)
        squaredNorm = Utils().sumSquaredNorm(pointDifference)
        squaredSigma = math.pow(self.sigma, 2)
        coefficient = (-squaredNorm)/squaredSigma
        return math.pow(math.e, coefficient)


    # y: 1,m1 x m2
    def winner(self, y):
        for j in range(0, self.m2):
            for i in range(0, self.m1):
                if y[(self.m1*j)+i] == 1:
                    return (i, j)


    def winnerINverted(self, y):
        for j in range(0, self.m1):
            for i in range(0, self.m2):
                if y[(self.m2*j)+i] == 1:
                    return (i, j)



