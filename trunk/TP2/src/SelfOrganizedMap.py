import numpy as np
import random
import math

class SelfOrganizedMap:

    def __init__(self, epochs, alphaEtta, alphaSigma, n, m1, m2):
        self.epochs = epochs
        self.alphaEtta = alphaEtta
        self.alphaSigma = alphaSigma
        self.etta = 1 #es correcto inicializarlo con frula?
        self.sigma = 2 #es correcto inicializarlo con frula?
        self.n = n
        self.m1 = m1
        self.m2 = m2
        self.matrix = self.createRandomMatrix(n, (m1*m2))

    def createRandomMatrix(self, n, m):
        matrix = np.zeros((n,m))
        COLUMN = 0
        ROW = 1
        for columnIndex in range(0, matrix.shape[COLUMN]):
            for rowIndex in range(0, matrix.shape[ROW]):
                matrix[columnIndex][rowIndex] = random.uniform(-0.1, 0.1)
        return matrix

    def algorithm(self, dataSet):
        runningEpoch = 1

        while runningEpoch < self.epochs:
            self.updateEtta(runningEpoch)
            self.updateSigma(runningEpoch)

            for x in dataSet:
                self.correctWeightMatrix(x)

            runningEpoch += 1

    def updateEtta(self, epoch):
        self.etta = pow(epoch, -(self.alphaEtta))

    def updateSigma(self, epoch):
        self.sigma = pow(epoch, -(self.alphaSigma))

    def correctWeightMatrix(self, x):
        y = self.activate(x)
        point = self.winner(y)
        D = self.proxy(point, self.sigma)
        deltaMatrix = self.etta * (x.transpose - w). flatten(D) #se supone que tiene que dar una matrix
        self.matrix += deltaMatrix

#    def activate(self, x):

    def proxy(self, winnerPoint): #TODO: correct/check positions!
        gaussMatrix = np.zeros((self.m1, self.m2))
        gaussMatrix[winnerPoint[0]][winnerPoint[1]] = 1
        COLUMN = 0
        ROW = 1
        for columnIndex in range(0, gaussMatrix.shape[COLUMN]):
            for rowIndex in range(0, gaussMatrix.shape[ROW]):
                gaussMatrix[columnIndex][rowIndex] = self.gaussianFormula((columnIndex, rowIndex), winnerPoint)
        return gaussMatrix

    def gaussianFormula(self, point, winnerPoint):
        pointDifference = np.subtract(point, winnerPoint)
        squaredNorm = self.sumSquaredNorm(pointDifference)
        squaredSigma = math.pow(self.sigma, 2)
        coefficient = (-squaredNorm)/squaredSigma
        return math.pow(math.e, coefficient)

    def sumSquaredNorm(self, vector):
        return sum([math.pow(v,2) for v in vector]) / 2


    def winner(self, y):
        print 'm1: ' + str(self.m1)
        print 'm2: ' + str(self.m2)

        for j in range(0, self.m2):
            for i in range(0, self.m1):
                if y[(self.m1*j)+i] == 1:
                    return (i, j)


