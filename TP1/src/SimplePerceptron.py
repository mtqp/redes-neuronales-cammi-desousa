import sys
import numpy as np
import math
import random
from TrainingInformation import *
from Functions import *

class SimplePerceptron: 

    def __init__(self, parameters, function, mustShuffleLearningSet, verbose):
        m = parameters.getMDimension()
        n = parameters.getNDimension()
        
        self.parameters = parameters
        self.function = function
        self.mustShuffleLearningSet = mustShuffleLearningSet
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
            trainingSet = self.parameters.learningSet
            if self.mustShuffleLearningSet:
                trainingSet = self.parameters.getShuffledData() #ver si no nos conviene hacer las prueba sin el shuffle
            
            iterationErrors = []
            for learningData in trainingSet:
                
                evaluationOutput, vectorDotMatrix = self.multiplyVectorAndMatrixAndApplyFunction(learningData.input, self.matrix)
                                
                iterationError = np.subtract(learningData.expectedOutput, evaluationOutput) #delta

                if self.function.isSigmoid():
                    iterationError = self.correctIterationError(iterationError, vectorDotMatrix)
                
                    
                iterationErrors.append(iterationError)
                    
                #---> Line below does: 
                #---- etta * ( learninData.input.transpose() x iterationerror ) *gprima /en nuestro caso no va xq la derivada es 1
                transposeInput = np.matrix(learningData.input).transpose()
                iterationErrorMatrix = np.matrix(iterationError)
                deltaMatrix = np.dot(self.parameters.etta, np.dot(transposeInput, iterationErrorMatrix)) 
                self.matrix = np.add(self.matrix,deltaMatrix) #algoritmo incremental
            
            epsilonOnIteration = self.sumVectorsSquaredNorms(iterationErrors)
            self.collectEpochInformation(iteratedEpochs, epsilonOnIteration)
            iteratedEpochs += 1
        self.printReasonToFinish(epsilonOnIteration, iteratedEpochs)
        
    def multiplyVectorAndMatrixAndApplyFunction(self, vector, matrix):
        #el vector se lo multiplica por cada vector columna de la matrix 
        #y luego se le aplica la funcion signo
        
        columnsAsRows = matrix.transpose() #es un truquito para poder agarrar rapido las columnas, no se si se puede hacer de otra forma mas eficiente
        vectorDotMatrix = [] #H

        for columnIndex in range(0, columnsAsRows.shape[0]):
            matrixVector = columnsAsRows[columnIndex].transpose()
            vectorialProduct = np.dot(vector, matrixVector)
            vectorDotMatrix.append(vectorialProduct.flat[0])
        
        evaluationOutput = [self.function.value(acum) for acum in vectorDotMatrix]  #O
        
        return evaluationOutput, vectorDotMatrix

    
    def correctIterationError(self, delta, h):
        correctedDelta = []
        for i in range(0,len(delta)):
            correctedDelta.append(delta[i] * self.function.derive(h[i]))
        return correctedDelta

    def collectEpochInformation(self, epoch, epsilon):
        self.errorInformation.add(epoch, epsilon) #esta hecho muy desprolijo esto... tendriamos en enviarle mjes solo a training information
        self.collectValidationInformation()
        self.collectTestSetInformation(epoch)
        
        if self.verbose:
            self.consolePrintEpochInformation(epoch, epsilon)
           
    def collectTestSetInformation(self, epoch):
        for learningData in self.parameters.testingSet:
            evaluationOutput, notUsefulReturn = self.multiplyVectorAndMatrixAndApplyFunction(learningData.input, self.matrix)
            iterationError = np.subtract(learningData.expectedOutput, evaluationOutput)

            cuadraticError = self.sumSquaredNorms(iterationError.flat)
            self.trainingInformation.addTestSetInformation(epoch, cuadraticError)
            
    def collectValidationInformation(self):
        for learningData in self.parameters.testingSet:
            obtainedVector, notUsefulReturn = self.multiplyVectorAndMatrixAndApplyFunction(learningData.input, self.matrix)
            validation = ValidationInformation(learningData.expectedOutput, obtainedVector, self.parameters.objective)
            self.trainingInformation.addValidationInformation(validation)
        
    def getTrainingInformation(self):
        return self.trainingInformation
        
    def sumVectorsSquaredNorms(self, errors):
        return sum([self.sumSquaredNorms(e) for e in errors])
        
    def sumSquaredNorms(self, vector):
        return sum([math.pow(v,2) for v in vector]) / 2

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
            obtainedVector, notUsefulReturn = self.multiplyVectorAndMatrixAndApplyFunction(learningData.input, self.matrix)
            print 'input: ' + str(learningData.input)
            print str(learningData.expectedOutput) + ' --> expected'
            print str(obtainedVector) + ' --> obtained'
            print '--------------'
        #'''    
    
    def printReasonToFinish(self, epsilon, epoch):
        if epsilon < self.parameters.epsilon:
            print 'ALGORITHM - Epsilon bound met on epoch: ' + str(epoch) + ' with epsilon value: ' + str(epsilon)
        elif epoch == self.parameters.epochs:
            print 'ALGORITHM - Epochs bound met'
        else:
            print 'ALGORITHM - It shouldn\'t have stopped'
        
    def showEvolution(self):
        print 'matrix evolution, counter: ' + str(self.counter)
        print self.matrix
        self.counter+=1        

