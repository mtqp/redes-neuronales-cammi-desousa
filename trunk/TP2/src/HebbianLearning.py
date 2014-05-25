import numpy as np
import math
import random
import time
from MatrixVisualizer import MatrixVisualizer
from pprint import pprint

class HebbianLearning:

    def __init__(self, n, m, etta, endCondition):
        self.matrix = self.createRandomMatrix(n,m)
        self.etta = etta
        self.n = n
        self.m = m
        self.deltaMatrix = np.zeros((self.n,self.m))
        self.endCondition = endCondition
        self.visualizer = MatrixVisualizer(n, m)

    def algorithm(self, dataSet, rule): # n vector de R6: (a1,a2,a3,a4,a5,a6):

        epoch = 0
        while not self.endCondition.endConditionIsMet(epoch, self.etta):
            print 'Epoch: ' + str(epoch)
            for x in dataSet:
                #print 'Corriendo para dato: ' + str(x)
                y = self.multiplyVectorAndMatrix(x,self.matrix)
                for j in range(0,self.m):
                    for i in range(0,self.n):
                        xAcum = np.zeros((self.n,1)).flatten() #Verificar que esto este funcionando correctamente.
                        for k in range(1,rule(j,self.m)):
                            xAcum[i] += y[k] * self.matrix[i][k]
                        #print "(" + str(i) + "," + str(j) + ") y: " + str(y[j]) + "---- x[i] - xAcum[i]: " + str(x[i] - xAcum[i])
                        self.deltaMatrix[i][j] = self.etta * y[j] * (abs(x[i]) - abs(xAcum[i]))
                self.matrix = np.add(self.matrix,self.deltaMatrix)

                #pprint (self.matrix)
                self.visualizer.visualize(self.matrix)

            epoch = epoch + 1
            #self.etta = 1.0/epoch
            #print 'Epoch: ' + str(epoch)
            #print 'Etta: ' + str(self.etta)

    def createRandomMatrix(self, n, m):
        matrix = np.zeros((n,m))
        COLUMN = 0
        ROW = 1

        for columnIndex in range(0, matrix.shape[COLUMN]):
            for rowIndex in range(0, matrix.shape[ROW]):
                matrix[columnIndex][rowIndex] = random.uniform(-0.1, 0.1)
        return matrix

    def multiplyVectorAndMatrix(self, vector, matrix):
        #el vector se lo multiplica por cada vector columna de la matrix

        columnsAsRows = matrix.transpose() #es un truquito para poder agarrar rapido las columnas, no se si se puede hacer de otra forma mas eficiente
        vectorDotMatrix = []

        for columnIndex in range(0, columnsAsRows.shape[0]):
            matrixVector = columnsAsRows[columnIndex].transpose()
            vectorialProduct = np.dot(vector, matrixVector)
            vectorDotMatrix.append(vectorialProduct.flat[0])

        return vectorDotMatrix
