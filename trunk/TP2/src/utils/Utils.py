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
        return [1 if min(vector) == item else 0 for item in vector] #Falla si hay dos que dan igual.

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
                value1 = matrix1[i,j]
                value2 = matrix2[i,j]

                matrixResult[i][j] = value1 * value2

        return matrixResult

    def createHistogram(self, matrix):

        matrixRows = matrix.shape[0]
        matrixColumns = matrix.shape[1]
        print 'matrixAcumWinner: ' + '(' + str(matrix.shape[0]) + ',' + str(matrix.shape[1]) + ')'
        print matrix

        #matrixHistogram = np.zeros((matrixRows*matrixColumns,matrixRows*5)) #si, es matrix rows porque quedemos armar una matriz mas grande para el histograma
        matrixHistogram = self.unos((matrixRows*matrixColumns,matrixRows*matrixColumns)) #si, es matrix rows porque quedemos armar una matriz mas grande para el histograma
        print 'matrixHistogram: ' + '(' + str(matrixHistogram.shape[0]) + ',' + str(matrixHistogram.shape[0]) + ')'

        for i in range(0, matrixRows):
            for j in range(0, matrixRows):
                acumulated = int(np.asscalar(matrix[i][j]))
                for k in range(0, acumulated):
                    matrixHistogram[j*(i+1)][k] = 0
                    #print '(' + str(j) + ',' + str(k) + ')'

        #matrixHistogram = self.rotateMatrix(matrixHistogram, 1)
        #matrixHistogram = self.rotateMatrix(matrixHistogram, 1)
        #matrixHistogram = self.rotateMatrix(matrixHistogram, 1)

        return matrixHistogram


    def unos(self, pair):

        n = pair[0]
        m = pair[1]

        matrixResult = np.zeros((n, m))

        for i in range(0, n):
            for j in range(0, m):
                matrixResult[i][j] = 1

        return matrixResult

    def rotateMatrix(self, matrix, n):
        n = matrix.shape[0]
        m = matrix.shape[1]
        matrixResult = np.zeros((n, m))

        for i in range(0, n):
            for j in range(0, n):
                matrixResult[i][j] = matrix[n - j -1][i];

        return matrixResult;
