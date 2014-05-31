import numpy as np
from MatrixVisualizer import MatrixVisualizer
from pylab import *

class HebbianTrainingAnalyzer:
    def __init__(self, matrix, dataSet):
        self.matrix = matrix
        self.dataSet = dataSet

    def results(self):
        itemNumber = 0
        for x in self.dataSet:
            y = self.activate(x,self.matrix)
            average = np.average(y)
            variance = np.var(y)
            if itemNumber < 100:
                print 'Item: ' + str(itemNumber) + ' - Avg: ' + str(average) + ' - Var: ' + str(variance)
                print '     Input: ' + str(x)
                print '     Output: ' + str(y)
                print '  '
            '''if itemNumber == 0:
                plotter = MatrixVisualizer(-1,-1) #malisimo! ya no es un matrix visualizer
                plotter.plotHistogram(self.getAbsolute(x))
                figure(1)
                plotter.plotHistogram(self.getAbsolute(y))
            '''
            itemNumber += 1

    def activate(self, x, matrix):
        y = []
        for j in range(0, matrix.shape[1]):
            y_i = 0
            for i in range(0, matrix.shape[0]):
                y_i += x[i] * matrix[i,j]
            y.append(y_i)
        return y

    def getAbsolute(self, vector):
        return [ abs(x_i) for x_i in vector ]
