import numpy as np
import numpy.linalg as linalg
import random
import math

class Utils:

    def createRandomMatrix(self, n, m):

        ROW = 0
        COLUMN = 1

        matrix = np.zeros((n,m))

        for rowIndex in range(0, matrix.shape[ROW]):
            for columnIndex in range(0, matrix.shape[COLUMN]):
                matrix[rowIndex][columnIndex] = random.uniform(-0.1, 0.1)

        return matrix

    def subtractVectorToEachColumnOf(self, matrix, vector):
        matrixVector = np.mat(vector)
        matrixVectorTransposed = np.transpose(matrixVector)
        matrixVectorTransposed2 = np.mat(matrixVectorTransposed)
        return np.subtract(matrix, matrixVectorTransposed2)

    '''
    def subtractVectorToEachColumnOf2(self, matrix, vector):
        #transposeVector = np.transpose(vector)
        #return np.subtract(matrix, vector)
        vectorNorms = []
        TRANSPOSED_COLUMN = 0
        TRANSPOSED_ROW = 1
        trasposeMatrix = np.transpose(matrix)

        for columnIndex in range(0, trasposeMatrix.shape[TRANSPOSED_COLUMN]):
            matrixVector = trasposeMatrix[columnIndex]
            vectorNorms.append(np.subtract(matrixVector, vector))
        return vectorNorms
    '''

    def subtractMatrices(self, matrix1, matrix2):
        return np.subtract(matrix1, matrix2)

    def applyNormToEachColumn2(self, matrix):
        return linalg.norm(matrix)

    def applyNormToEachColumn(self, matrix):

        vectorNorms = []
        TRANSPOSED_COLUMN = 0
        TRANSPOSED_ROW = 1
        trasposeMatrix = np.transpose(matrix)

        for columnIndex in range(0, trasposeMatrix.shape[TRANSPOSED_COLUMN]):
            matrixVector = trasposeMatrix[columnIndex]
            vectorNorms.append(linalg.norm(matrixVector))
        return vectorNorms

    '''
    def sumSquaredNorm(self, vector):
        return sum([math.pow(v,2) for v in vector]) / 2
    '''

    def applyMaskForMinimumOn(self, vector):
        return [1 if min(vector) == item else 0 for item in vector]