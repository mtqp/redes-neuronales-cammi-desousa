from numpy.lib.financial import rate
from visual import *
import numpy as np
import math
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time


class MatrixVisualizer:
    def __init__(self, nDimension, mDimension):
        self.n = nDimension
        self.m = mDimension
        self.boxes = self.createMatrixBoxes(nDimension, mDimension)
        currentDisplay = display.get_selected()
        currentDisplay.background = color.white

    def visualize(self, matrix):
        scene.center = vector(3,2,-1)
        #scene.forward = vector(0,20,10)
        rate(100)
        time.sleep(0.01)
        for columnIndex in range(0, self.n):
            for rowIndex in range(0, self.m):
                matrixValue = matrix[columnIndex][rowIndex]
                boxItem = self.boxes[columnIndex][rowIndex]
                boxItem.color =  color.rgb_to_hsv(self.createVectorForValue(matrixValue))
                boxItem.size = (0.5, 0.5, 1*abs(matrixValue))

    def visualizeWinnerMatrix(self, matrix):
        #scene.center = vector(3,2,-1)
        #scene.forward =  vector(0,20,10)
        rate(100)
        time.sleep(0.01)
        for columnIndex in range(0, self.n):
            for rowIndex in range(0, self.m):
                matrixValue = matrix[columnIndex][rowIndex]
                boxItem = self.boxes[columnIndex][rowIndex]

                if(matrixValue == 1):
                    boxItem.color = color.red
                else:
                    boxItem.color = color.green

                boxItem.size = (0.5, 0.5, 1*abs(matrixValue))

    def createVectorForValue(self, aValue): #por precondicion se supone que los valores estan en [0,1]
        aValue = abs(aValue)
        return (aValue, aValue, aValue)

    #red= (1,0,0)
    #green= (0,1,0)
    def createVectorForValue2(self, aValue):
        posAValue = abs(aValue)
        topValue = 10

        if(posAValue > topValue):
            firstComponent = 1
            secondComponent = 0
        else:
            firstComponent = posAValue/topValue
            secondComponent = (topValue - posAValue)/topValue

        #print 'Color: ' + str((firstComponent, secondComponent, 0))
        return (firstComponent,secondComponent, 0)

    def createMatrixBoxes(self, n, m):
        matrix = []

        for columnIndex in range(0, n):
            row = []
            for rowIndex in range(0, m):
                row.append(box(pos=(columnIndex, rowIndex, 0), size=(0.4, 0.4, 0.4), color=color.rgb_to_hsv((columnIndex*3, rowIndex*5, 10))))
            matrix.append(row)
        return matrix

    def plot2d(self, matrix):
        plt.imshow(matrix, interpolation="none", cmap=cm.gray )
        plt.colorbar()
        plt.show()

    def visualizeCovariance(self, matrix):
        covarianceMatrix = np.cov(matrix)
        self.visualize(covarianceMatrix)