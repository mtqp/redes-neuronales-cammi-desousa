import numpy as np
import math
import random
import time
#import matplotlib.pyplot as plt
#import matplotlib.cm as cm
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
        epochsModuleToNotify = 50

        while not self.endCondition.endConditionIsMet(epoch, self.etta):
            if epoch % epochsModuleToNotify == 0:
                print 'Epoch: ' + str(epoch)
            for x in dataSet:
                y = np.dot(x,self.matrix)
                for j in range(0, self.m):
                    for i in range(0, self.n):
                        xAcum = 0
                        for k in range(0, rule(j, self.m)): #j+1 == sanger
                            xAcum += (y[k] * self.matrix[i][k])
                        self.deltaMatrix[i][j] = self.etta * y[j] * (x[i] - xAcum)

                self.matrix += self.deltaMatrix

            epoch = epoch + 1

            #self.printOrthogonalVectorCheck(self.matrix)

        #self.visualizer.visualize(self.matrix)
        #self.visualizer.plot2d(self.matrix)

        #self.visualizer.visualizeCovariance(self.matrix)
        #self.visualizer.plot2d(np.cov(self.matrix))

        #self.etta = 1.0/epoch
        #print 'Epoch: ' + str(epoch)
        #print 'Etta: ' + str(self.etta)

    def printOrthogonalVectorCheck(self, matrix):
        columnsAsRows = matrix.transpose() #es un truquito para poder agarrar rapido las columnas, no se si se puede hacer de otra forma mas eficiente
        pairCheck = []
        vectorCount = columnsAsRows.shape[0]
        pairingIndexes = [ (i, (i+1)%vectorCount) for i in range(0, vectorCount)]

        for pairIndex in pairingIndexes:
            vector = columnsAsRows[pairIndex[0]].transpose()
            vectorToMultiply = columnsAsRows[pairIndex[1]].transpose()
            pairCheck.append(np.dot(vector, vectorToMultiply))

        print 'Ortogonalidad:'
        print str(pairCheck)


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
