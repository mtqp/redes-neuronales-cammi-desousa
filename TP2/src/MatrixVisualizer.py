from visual import *
import numpy as np
import math
import random


class MatrixVisualizer:
    def __init__(self, nDimension, mDimension):
        self.n = nDimension
        self.m = mDimension
        self.boxes = self.createMatrixBoxes(nDimension, mDimension)

    def visualize(self, matrix):
        for columnIndex in range(0, self.n):
            for rowIndex in range(0, self.m):
                matrixValue = matrix[columnIndex][rowIndex]
                boxItem = self.boxes[columnIndex][rowIndex]
                boxItem.color = color.rgb_to_hsv(self.createVectorForValue(matrixValue))
                boxItem.size = (0.4, 0.4, 10*abs(matrixValue))

    def createVectorForValue(self, aValue):
        aValue = 255 - (10*aValue)
        return (aValue, aValue, aValue)

    def createMatrixBoxes(self, n, m):
        matrix = []

        for columnIndex in range(0, n):
            row = []
            for rowIndex in range(0, m):
                row.append(box(pos=(columnIndex, rowIndex, 0), size=(0.4, 0.4, 0.4), color=color.rgb_to_hsv((columnIndex*3, rowIndex*5, 10))))
            matrix.append(row)
        return matrix
