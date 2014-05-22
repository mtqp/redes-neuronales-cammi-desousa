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
        self.TRANSPOSED_COLUMN = 0
        self.TRANSPOSED_ROW = 1
        self.matrix = self.createRandomMatrix(n, (m1*m2))

    def createRandomMatrix(self, n, m):
        matrix = np.zeros((n,m))
        for columnIndex in range(0, matrix.shape[self.TRANSPOSED_COLUMN]):
            for rowIndex in range(0, matrix.shape[self.TRANSPOSED_ROW]):
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

    def activate(self, x):
        matrixDifference = self.subtractVectorToEachColumnOf(self.matrix, x)
        vectorOfNorms = self.applyNormToEachColumn(matrixDifference)
        maskedVector = self.applyMaskForMinimumOn(vectorOfNorms)
        print 'the mask is: '  + str(maskedVector)
        return maskedVector

    def subtractVectorToEachColumnOf(self, matrix, vector):
        matrixDifference = []
        trasposeVector = np.transpose(vector)
        print 'transpose vector: ' + str(trasposeVector)
        print 'vector: ' + str(vector)
        trasposeMatrix = np.transpose(matrix)
        for columnIndex in range(0, matrix.shape[self.TRANSPOSED_COLUMN]):
            matrixVector = trasposeMatrix[columnIndex]
            print 'matrixVector: ' + str(matrixVector)
            matrixDifference.append(np.subtract(matrixVector, trasposeVector))
        print 'the difference is: ' + str(matrixDifference)
        return matrixDifference

    def applyNormToEachColumn(self, matrix):
        norms = []
        trasposeMatrix = np.transpose(matrix)
        for columnIndex in range(0, matrix.shape[self.TRANSPOSED_COLUMN]):
            matrixVector = trasposeMatrix[columnIndex]
            norms.append(self.sumSquaredNorm(matrixVector))
        print 'the norms are: ' + str(norms)
        return norms

    def applyMaskForMinimumOn(self, vector):
        return [1 if min(vector) == item else 0 for item in vector]

    def proxy(self, winnerPoint): #TODO: correct/check positions!
        gaussMatrix = np.zeros((self.m1, self.m2))
        gaussMatrix[winnerPoint[0]][winnerPoint[1]] = 1

        for columnIndex in range(0, gaussMatrix.shape[1]):
            for rowIndex in range(0, gaussMatrix.shape[0]):
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
        for j in range(0, self.m2):
            for i in range(0, self.m1):
                if y[(self.m1*j)+i] == 1:
                    return (i, j)


