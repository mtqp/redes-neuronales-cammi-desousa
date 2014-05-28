import numpy as np

class HebbianTrainingAnalyzer:
    def __init__(self, matrix, dataSet):
        self.matrix = matrix
        self.dataSet = dataSet

    def results(self):
        for x in self.dataSet:
            y = self.activate(x,self.matrix)
            average = np.average(y)
            covariance = np.cov(y)
            print str(y) + ' - Avg: ' + str(average) + ' - Cov: ' + str(covariance)

    def activate(self, x, matrix):
        y = []
        for i in range(0, matrix.shape[0]):
            y_i = 0
            for j in range(0, matrix.shape[1]):
                y_i += x[i] * matrix[i,j]
            y.append(y_i)
        return y