import numpy as np
import math
import random

class HebbianLearning:

    def __init__(self, nDimensionOfWeightMatrix, mDimensionOfWeightMatrix, etta):
        self.matrix = self.createRandomMatrix(nDimensionOfWeightMatrix,mDimensionOfWeightMatrix)
        self.etta = etta
        self.n = nDimensionOfWeightMatrix
        self.m = mDimensionOfWeightMatrix
        self.deltaMatrix = np.zeros((self.n,self.m))

    def algorithm(self, dataSet, rule): # n vector de R6: (a1,a2,a3,a4,a5,a6):

        epoch = 0
        while not self.endConditionIsMet(epoch):
            for x in dataSet:
                print 'Corriendo para dato: ' + str(x)
                y = self.multiplyVectorAndMatrixAndApplyFunction(x,self.matrix)
                for j in range(0,self.m):
                    for i in range(0,self.n):
                        xAcum = np.zeros((self.n,1)).flatten() #Verificar que esto este funcionando correctamente.
                        for k in range(1,rule(j,self.m)):
                            xAcum[i] += y[k] * self.matrix[i][k]
                        self.deltaMatrix[i][j] = self.etta * y[j] * (x[i] - xAcum[i])
                self.matrix = np.add(self.matrix,self.deltaMatrix)

    def createRandomMatrix(self, n, m):
        matrix = np.zeros((n,m))
        COLUMN = 0
        ROW = 1
        for columnIndex in range(0, matrix.shape[COLUMN]):
            for rowIndex in range(0, matrix.shape[ROW]):
                matrix[columnIndex][rowIndex] = random.uniform(-0.1, 0.1)
        return matrix

    def endConditionIsMet(self,epoch):
        return epoch > 1000

    def multiplyVectorAndMatrixAndApplyFunction(self, vector, matrix):
        #el vector se lo multiplica por cada vector columna de la matrix

        columnsAsRows = matrix.transpose() #es un truquito para poder agarrar rapido las columnas, no se si se puede hacer de otra forma mas eficiente
        vectorDotMatrix = [] #H

        for columnIndex in range(0, columnsAsRows.shape[0]):
            matrixVector = columnsAsRows[columnIndex].transpose()
            vectorialProduct = np.dot(vector, matrixVector)
            vectorDotMatrix.append(vectorialProduct.flat[0])

        return vectorDotMatrix
