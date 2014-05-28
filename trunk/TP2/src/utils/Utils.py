import numpy as np
import numpy.linalg as linalg
import random
import math

class Utils:

    def createRandomMatrix(self, n, m):
        return self.createRandomMatrixBetween(n,m,-0.1, 0.1)

    def createRandomMatrixBetween(self, n, m, initRandom, endRandom):

        ROW = 0
        COLUMN = 1

        matrix = np.zeros((n,m))

        for rowIndex in range(0, matrix.shape[ROW]):
            for columnIndex in range(0, matrix.shape[COLUMN]):
                matrix[rowIndex][columnIndex] = random.uniform(initRandom, endRandom)

        return matrix

    # matrix: (n, m1.m2) -> (1,n) -> (n,m1.m2)
    def subtractVectorToEachColumnOf(self, matrix, vector):
        matrixVector = np.mat(vector)
        matrixVectorTransposed = np.transpose(matrixVector)
        matrixVectorTransposed2 = np.mat(matrixVectorTransposed)
        return np.subtract(matrix, matrixVectorTransposed2)

    def subtractMatrixFromVector(self, matrix, vector):
        matrixVector = np.mat(vector)
        matrixVectorTransposed = np.transpose(matrixVector)
        matrixVectorTransposed2 = np.mat(matrixVectorTransposed)
        return np.subtract(matrixVectorTransposed2,matrix)

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
        linalg.norm(vector)
    '''

    def sumSquaredNorm(self, vector):
        return sum([math.pow(v,2) for v in vector]) / 2

    def applyMaskForMinimumOn(self, vector):
        return [1 if min(vector) == item else 0 for item in vector]

    def multiplyVectorAndMatrix(self, vector, matrix):
        #el vector se lo multiplica por cada vector columna de la matrix

        columnsAsRows = matrix.transpose() #es un truquito para poder agarrar rapido las columnas, no se si se puede hacer de otra forma mas eficiente
        vectorDotMatrix = [] #H

        for columnIndex in range(0, columnsAsRows.shape[0]):
            matrixVector = columnsAsRows[columnIndex].transpose()
            print 'vector: ' + str(vector)
            print 'matrixVector: ' + str(matrixVector)

            vectorialProduct = np.dot(vector, matrixVector)
            print 'resultado: ' + str(vectorialProduct)

            vectorDotMatrix.append(vectorialProduct.flat[0])

        return vectorDotMatrix

    def multiplyPositionToPosition(self, matrix1, matrix2):
        ROW = 0
        COLUMN = 1

        n = matrix1.shape[ROW]
        m = matrix1.shape[COLUMN]

        matrixResult = np.zeros((n,m))

        for i in range(0, n):
            for j in range(0, m):
                matrixResult[i][j] = matrix1[i][j] * matrix2[i][j]

        return matrixResult