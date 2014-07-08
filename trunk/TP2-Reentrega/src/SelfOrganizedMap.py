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
        self.etta = 0
        self.sigma = 0
        self.n = n
        self.m1 = m1
        self.m2 = m2
        self.matrix = Utils().createRandomMatrixBetween(n, (m1*m2),random1, random2)
        #self.matrix = Utils().createFixedMatrixWithValue(n, (m1*m2),5)
        self.seeResultBool = False
        self.vTest = MatrixVisualizer(m1,m2)
        self.acumWinnerPoints = []
        self.vTest.showLabel = False

    def clearMatrixBoxesPositions(self):
        self.vTest.matrixAcumBoxes = np.zeros((self.m1,self.m2))

    def training(self, dataSet,firstBoundX1, endBoundX1, firstBoundX2, endBoundX2):
        print '--------------- Learning step ---------------- '
        runningEpoch = 1
        start_time = time.time()
        elapsed_time = 0
        while runningEpoch < self.epochs:
            self.updateEtta(runningEpoch)
            self.updateSigma(runningEpoch)

            if(runningEpoch % 1 == 0):
                print 'epoch ' + str(runningEpoch)
                #timeSleep = 5
                #time.sleep(timeSleep)
                #elapsed_time -= timeSleep
                #print 'elapsedTime: ' + str(time.time() - start_time - elapsed_time)

            #print '---------- epoch: ' + str(runningEpoch)
            #print '---------- etta: ' + str(self.etta)
            #print '---------- sigma: ' + str(self.sigma)
            for x in dataSet:
                self.correctWeightMatrix(x,firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)
            runningEpoch += 1

        elapsed_time += time.time() - start_time
        print 'elapsedTime: ' + str(elapsed_time)

    def test(self, dataSet,  m1, m2, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2):
        print '--------------- Activating step ---------------- '

        self.vTest.showLabel = False
        acumWinnerMatrix = np.zeros((self.n,self.m1*self.m2))
        acumMaximumPerNeuron = np.zeros((self.m1,self.m2))

        counter = 0
        neuralAcumVector = []

        for x in dataSet:
            counter = counter + 1
            #print 'Activation: ' + str(x);
            print 'activation: ' + str(counter)
            y = self.activate(x)

            winnerPoint = self.winner(y)

            #neuronaActivada = winnerPoint[1]+winnerPoint[0]*self.m2
            #visualPoint = (neuronaActivada,1)
            #print 'Neurona activated: ' + str(neuronaActivada);

            #self.acumWinnerPoints.append(visualPoint)

            winnerMatrix = self.proxy(winnerPoint)
            winnerId = (winnerPoint[0]*winnerMatrix.shape[1]) + winnerPoint[1]
            neuralAcumVector.append(winnerId)
            acumWinnerMatrix += winnerMatrix
            #self.vTest.visualizeNeuralPoints(winnerPoint, neuronaActivada, x, 0)
            self.vTest.visualizeNeuralPointsBidimensionalOnline(winnerPoint, x, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)
            #time.sleep(0.5)
        #self.vTest.visualizePlotAxis(self.acumWinnerPoints, 5, 10, 5, 10)
        #self.vTest.waitForKey()


    def updateEtta(self, epoch):
        self.etta = pow(epoch, -(self.alphaEtta))

    def updateSigma(self, epoch):
        self.sigma = pow(epoch, -(self.alphaSigma))

    def correctWeightMatrix(self, x,firstBoundX1, endBoundX1, firstBoundX2, endBoundX2):

        #print 'Matrix: ' + str(self.matrix.reshape((self.n,self.m1*self.m2)))
        #print 'Learning vector: ' + str(x)
        y = self.activate(x)
        #print 'Winner vector: ' + str(y)
        point = self.winner(y)
        #print 'Winner position:' + str(point)
        #print str(point[0]) + ',' + str(point[1])

        neuronaActivada = point[1]+point[0]*self.m2
        #self.vTest.visualizeNeuralPoints(point, neuronaActivada, x, 20)

        propagationMatrix = self.proxy(point)
        #randomValue = random.uniform(0.1, 0.2)
        #propagationMatrix = Utils().createFixedMatrixWithValue(self.n, (self.m1*self.m2),randomValue)

        #print 'propagationMatrix:' + str(propagationMatrix)

        matrixDifference = Utils().subtractMatrixFromVector(self.matrix, x)
        flattenPropagationMatrix = propagationMatrix.reshape((self.n,self.m1*self.m2)) # es n porque es el vector de propagacion que ira multiplicando a cada fila de la matrix (cada una de las n matrices de m1.m2)

        deltaMatrix = Utils().multiplyPositionToPosition(self.etta * matrixDifference, flattenPropagationMatrix)
        self.matrix = self.matrix + deltaMatrix
        #self.vTest.visualizeNeuralPointsBidimensionalOnline(point, x, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)
        #time.sleep(0.5)

    def seeResult(self):
        self.seeResultBool = True

    #Devuelve  y (1, m1.m2)
    def activate(self, x):
        #print 'Activation x: ' + str(x)
        #print 'Matrix : ' + str(self.matrix)

        matrixDifference = Utils().subtractVectorToEachColumnOf(self.matrix, x)
        #print '|W - Xt|: (' + str(matrixDifference.shape[0]) + "," + str(matrixDifference.shape[1]) + ")"
        #print '|W - Xt|: ' + str(matrixDifference)
        vectorOfNorms = Utils().applyNormToEachColumn(matrixDifference)
        #print 'Norm: ' + str(vectorOfNorms)

        maskedVector = Utils().applyMaskForMinimumOn(vectorOfNorms)

        return maskedVector

    def proxy(self, winnerPoint): #TODO: correct/check positions!
        #print 'proxy'
        #print 'Calculating Proxy, winner point is: (' + str(winnerPoint[0]) + ',' + str(winnerPoint[1]) + ')'
        gaussMatrix = np.zeros((self.n,self.m1*self.m2))
        #print 'winnerPointOneDimension: ' + str(self.m1*winnerPoint[0]+winnerPoint[1])

    #for i in range (0,self.n):
        #print 'm1: ' + str(self.m1)
        #print 'winnerPoint: (' + str(winnerPoint[1]) + ',' + str(winnerPoint[0]) + ')'
        #print 'i: ' + str(i)
        #print 'j: ' + str(self.m1*winnerPoint[1]+winnerPoint[0])
        #VER SI ESTO NO ESTA AL REVES
        #gaussMatrix[i][self.m1*winnerPoint[1]+winnerPoint[0]] = 1

        #gaussMatrix[i][self.m1*winnerPoint[0]+winnerPoint[1]] = 1
        #print '['+str(i)+']['+str(self.m1*winnerPoint[0]+winnerPoint[1])+'] = 1'
        #print 'GaussMatrix: ' + '(' +  str(gaussMatrix.shape[0]) + ',' + str(gaussMatrix.shape[1]) + ')'

        #print '---- winnerPoint: ' + str(winnerPoint) + '-------'

        for rowIndex in range(0, gaussMatrix.shape[0]):
            for columnIndex in range(0, gaussMatrix.shape[1]):


                #pointOneDimension = (rowIndex,columnIndex)
                #point = pointOneDimension

                #winnerPointOneDimension =  (rowIndex,self.m1*winnerPoint[0]+winnerPoint[1])
                #winnerPoint = winnerPointOneDimension
                #print 'winnerPointOneDimension: ' + str((rowIndex,self.m1*winnerPoint[0]+winnerPoint[1]))

                parteEntera = math.modf(columnIndex/self.m2)[1]
                point2 = columnIndex-(parteEntera*self.m2)
                point = (parteEntera, point2)

                #print 'point: ' + str(point)


                #print 'rowsIndex, colIndex: ' + str(rowIndex) + ',' + str(columnIndex)
                gaussValue = self.gaussianFormula(point, winnerPoint)

                #if(point[0] == winnerPoint[0] and point[1] == winnerPoint[1]):
                    #print 'Winner point found value: '
                    #print '['+str(i)+']['+str(self.m1*winnerPoint[0]+winnerPoint[1])+'] = ' + str(gaussValue)
                    #print '['+str(rowIndex)+']['+str(columnIndex)+'] = ' + str(gaussValue)

                gaussMatrix[rowIndex][columnIndex] = gaussValue

                #print 'gaussValue: ' + str(gaussValue)

        return gaussMatrix

    def gaussianFormula(self, point, winnerPoint):

        #print 'Gaussian Formula: ' +  'point: (' + str(point[0]) + ',' + str(point[1]) + ') == winner point: (' + str(winnerPoint[0]) + ',' + str(winnerPoint[1]) + ')'


        pointDifference = np.subtract(point, winnerPoint)
        squaredNorm = Utils().sumSquaredNorm(pointDifference)
        squaredSigma = math.pow(self.sigma, 2)
        coefficient = (-squaredNorm)/squaredSigma
        epow = math.pow(math.e, coefficient)

        #if(point[0] == winnerPoint[0] and point[1] == winnerPoint[1]):
            #print 'WinnerPoint equals to Point: ' + str(point)
            #print 'pointDifference: ' + str(pointDifference)

        return epow


    # y: 1,m1 x m2
    def winner(self, y):
        #print 'len(y):' + str(len(y))
        for j in range(0, self.m1):
            for i in range(0, self.m2):
                if y[(self.m1*j)+i] == 1:
                    return (j, i)
                    #return (i, j)


    def winnerINverted(self, y):
        for j in range(0, self.m1):
            for i in range(0, self.m2):
                if y[(self.m2*j)+i] == 1:
                    return (i, j)



