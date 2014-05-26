from numpy.lib.financial import rate
from visual import *
import numpy as np
import math
import random
import time


class MatrixVisualizer:
    def __init__(self, nDimension, mDimension):
        self.n = nDimension
        self.m = mDimension
        self.boxes = self.createMatrixBoxes(nDimension, mDimension)
        #self.scene = display(title='Visualizacion de matriz', x=0, y=0, width=600, height=200, center=(5,0,0), background=(0,1,1))
        #self.scene.select()

    def visualize(self, matrix):
        scene.center = vector(3,2,-1)
        scene.forward =  vector(0,20,10)
        rate(100)
        time.sleep(0.01)
        for columnIndex in range(0, self.n):
            for rowIndex in range(0, self.m):
                matrixValue = matrix[columnIndex][rowIndex]
                boxItem = self.boxes[columnIndex][rowIndex]
                boxItem.color = color.rgb_to_hsv(self.createVectorForValue2(matrixValue))
                #boxItem.color = color.rgb_to_hsv((1,0,0))
                boxItem.size = (0.5, 0.5, 10*abs(matrixValue))

    def createVectorForValue(self, aValue):
        aValue = 0.5 - aValue
        if aValue < 0:
            aValue = 0
        #print 'Color: ' + str(aValue)
        return (aValue, aValue, 0)

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
