from visual import *
import numpy as np
import math
import random


class MatrixVisualizer:
    def __init__(self, nDimension, mDimension):
        self.boxes = self.createMatrixBoxes(nDimension, mDimension)

    #def visualize(self, matrix):
    #    self.ball.pos = self.ball.pos + self.ball.velocity*0.000

    def createMatrixBoxes(self, n, m):
        matrix = np.zeros((n,m))
        COLUMN = 0
        ROW = 1
        print 'blah1: ' +  str(matrix.shape[COLUMN])
        print 'blah2 ' +  str(matrix.shape[ROW])
        for columnIndex in range(0, matrix.shape[COLUMN]):
            for rowIndex in range(0, matrix.shape[ROW]):
                print 'column: ' + str(columnIndex) + ' row: ' + str(rowIndex)
                #matrix[columnIndex][rowIndex] =
                box(pos=(columnIndex, rowIndex, 0), size=(0.4, 0.4, 0.4), color=color.rgb_to_hsv((columnIndex*3, rowIndex*5, 10)))
        return matrix
