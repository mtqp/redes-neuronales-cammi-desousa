import sys
import numpy as np
import math
import random
from TrainingInformation import *
from Functions import *

class SimplePerceptron: 

    def __init__(self, parameters, function, verbose):
        m = parameters.getMDimension()
        n = parameters.getNDimension()
        
        self.parameters = parameters
        self.function = function
        self.matrix = self.createRandomMatrix(n,m)
        
        if verbose:
            self.consolePrintStartingContext(n, m)
        
        self.errorInformation = ErrorInformation([],[], self.parameters.objective, parameters.etta)
        self.trainingInformation = TrainingInformation(self.errorInformation)
        self.verbose = verbose
        self.counter = 0
        
    def createRandomMatrix(self, n, m):
        matrix = np.zeros((n,m)) 
        COLUMN = 0
        ROW = 1
        for columnIndex in range(0, matrix.shape[COLUMN]):
            for rowIndex in range(0, matrix.shape[ROW]):
                matrix[columnIndex][rowIndex] = random.uniform(-0.1, 0.1)
        return matrix
        
    def train(self):
        epsilonOnIteration = 1000
        iteratedEpochs = 0
        
        while epsilonOnIteration > self.parameters.epsilon and iteratedEpochs < self.parameters.epochs:
            shuffledLearningDatas = self.parameters.getShuffledData() #ver si no nos conviene hacer las prueba sin el shuffle
            
            iterationErrors = []
            for learningData in shuffledLearningDatas:
                evaluationVector = self.evaluateMultiplication(learningData.input, self.matrix)
                iterationError = np.subtract(learningData.expectedOutput, evaluationVector)
                iterationErrors.append(iterationError)
                
                #---> Line below does: 
                #---- etta * ( learninData.input.transpose() x iterationerror ) *gprima /en nuestro caso no va xq la derivada es 1
                transposeInput = np.matrix(learningData.input).transpose()
                iterationErrorMatrix = np.matrix(iterationError)
                deltaMatrix = np.dot(self.parameters.etta, np.dot(transposeInput, iterationErrorMatrix)) 
                self.matrix = np.add(self.matrix,deltaMatrix) #algoritmo incremental
            
            '''
            print 'iteration errors on epoch: ' + str(iteratedEpochs)
            print iterationErrors
            '''
            epsilonOnIteration = self.sumSquaredNorms(iterationErrors)
            self.collectEpochInformation(iteratedEpochs, epsilonOnIteration)
            iteratedEpochs += 1
            
    def collectEpochInformation(self, epochs, epsilon):
        self.errorInformation.add(epochs, epsilon) #esta hecho muy desprolijo esto... tendriamos en enviarle mjes solo a training information
        for learningData in self.parameters.learningSet:
            obtainedVector = np.dot(learningData.input, self.matrix)
            validation = ValidationInformation(learningData.expectedOutput, obtainedVector, self.parameters.objective)
            self.trainingInformation.addValidationInformation(validation)
        
        if self.verbose:
            self.consolePrintEpochInformation(epochs, epsilon)
            
    def getTrainingInformation(self):
        return self.trainingInformation
        
    def sumSquaredNorms(self, errors):
        return sum([self.squaredNorm(e) for e in errors]) / 2
        
    def squaredNorm(self, vector):
        potVector = [math.pow(v,2) for v in vector]
        return sum(potVector)
        
    def evaluateMultiplication(self, vector, matrix): 
        #el vector se lo multiplica por cada vector columna de la matrix 
        #y luego se le aplica la funcion signo
        
        columnsAsRows = matrix.transpose() #es un truquito para poder agarrar rapido las columnas, no se si se puede hacer de otra forma mas eficiente
        vectorDotMatrix = []

        for columnIndex in range(0, columnsAsRows.shape[0]):
            matrixVector = columnsAsRows[columnIndex].transpose()
            vectorialProduct = np.dot(vector, matrixVector)
            vectorDotMatrix.append(vectorialProduct.flat[0])

        return [self.function.value(acum) for acum in vectorDotMatrix]
        
    def consolePrintStartingContext(self, n, m):
        print 'n: ' + str(n)
        print 'm: ' + str(m)
        print 'whole learning matrix: ' + str(self.matrix)
        
    def consolePrintEpochInformation(self, iteratedEpochs, iterationEpsilon):
        print '--------------'
        #''' Used for debugging
        print 'Epoch: ' + str(iteratedEpochs)
        print 'Epsilon: '+ str(iterationEpsilon)
        for learningData in self.parameters.learningSet:
            obtainedVector = np.dot(learningData.input, self.matrix)
            print 'input: ' + str(learningData.input)
            print str(learningData.expectedOutput) + ' --> expected'
            print str(obtainedVector) + ' --> obtained'
            print '--------------'
        #'''    
        
    def showEvolution(self):
        print 'matrix evolution, counter: ' + str(self.counter)
        print self.matrix
        self.counter+=1        

