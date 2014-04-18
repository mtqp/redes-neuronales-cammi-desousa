import sys
import numpy as np
import math
from TrainingInformation import *

class SimplePerceptron: 

    def __init__(self, parameters):
        self.parameters = parameters
        self.matrix = self.createRandomMatrix(3,2)
        print 'whole learning matrix: ' + str(self.matrix)
        self.errorInformation = ErrorInformation([],[], self.parameters.objective)
        self.counter = 0
        
    def createRandomMatrix(self, n, m):
        #np.matrix('0.1 0.1 0.1; 0.1 0.1 0.1').transpose() #inicializar con algo que sea util (segun el profe randoms entre -0.1 y 0.1
        return np.random.rand(n,m) #normalizar a valores entre -0.1 y 0.1
        
    def train(self): #COMO SE QUE UMBRAL, PARAMETROS DEBO PONER?
        epsilonOnIteration = 1
        iteratedEpochs = 0
        
        while epsilonOnIteration > self.parameters.epsilon and iteratedEpochs < self.parameters.epochs:
            shuffledLearningDatas = self.parameters.getShuffledData() #ver si no nos conviene hacer las prueba sin el shuffle
            
            iterationErrors = []
            for learningData in shuffledLearningDatas:
                evaluationVector = self.applySignFunction(learningData.input, self.matrix)
                iterationError = np.subtract(learningData.expectedOutput, evaluationVector)
                '''Used for debugging
                print 'input: ' + str(learningData.input)
                print 'matrix: ' + str(self.matrix)
                print 'evaluationVector: ' + str(evaluationVector)
                print 'expectedOuput: ' + str(learningData.expectedOutput)
                print 'iteration error: ' + str(iterationError)
                print '---------------'
                '''
                iterationErrors.append(iterationError)
                
                #---> Line below does: 
                #---- etta * ( learninData.input.transpose() x iterationerror ) *gprima /en nuestro caso no va xq la derivada es 1
                transposeInput = np.matrix(learningData.input).transpose()
                iterationErrorMatrix = np.matrix(iterationError)
                deltaMatrix = np.dot(self.parameters.etta, np.dot(transposeInput, iterationErrorMatrix)) 
                '''
                print 'transpose input: ' + str(transposeInput)
                print 'iteration error: ' + str(iterationError)
                print 'delta matrix: ' 
                print str(deltaMatrix)
                print 'matrix: '
                print str(self.matrix)
                '''
                self.matrix = np.add(self.matrix,deltaMatrix) #algoritmo incremental
                '''
                print 'new matrix (after add):'
                print str(self.matrix)
                '''
                #self.showEvolution()
                
        
            epsilonOnIteration = 0.5 * self.sumSquaredNorms(iterationErrors)
            self.saveIterationError(iteratedEpochs, epsilonOnIteration)
            iteratedEpochs += 1
            self.testWhatWasLearnt(iteratedEpochs)

    def saveIterationError(self, epochs, epsilon):
        self.errorInformation.add(epochs, epsilon)
            
    def getTrainingInformation(self):
        validationInformation = ValidationInformation(None, None, 'Completar') #completar
        return TrainingInformation(self.errorInformation, validationInformation)
        
    def sumSquaredNorms(self, errors):
        return sum([self.squaredNorm(e) for e in errors])
        
    def squaredNorm(self, vector):
        return sum([math.pow(v,2) for v in vector])
        
    def applySignFunction(self, vector, matrix): 
        #el vector se lo multiplica por cada vector columna de la matrix 
        #y luego se le aplica la funcion signo
        
        columnsAsRows = matrix.transpose() #es un truquito para poder agarrar rapido las columnas, no se si se puede hacer de otra forma mas eficiente
        vectorDotMatrix = []
        #print '----> shape 0: ' + str(columnsAsRows.shape[0])
        for columnIndex in range(0, columnsAsRows.shape[0]):
            matrixVector = columnsAsRows[columnIndex].transpose()
            vectorialProduct = np.dot(vector, matrixVector)
            vectorDotMatrix.append(vectorialProduct)
            ''' Used for debugging
            print '-----> columnIndex : ' + str(columnIndex)
            print '-----> matrix vector : ' + str(matrixVector)
            print '-----> vector: ' + str(vector)
            print '-----> vectorial product: ' + str(vectorialProduct)
        
        print '-----> vector dot matrix: ' + str(vectorDotMatrix)
        '''
        return [self.sign(acum) for acum in vectorDotMatrix]
    
    def sign(self, value):
        if value >= 0:
            return 1
        return -1
       
    def testWhatWasLearnt(self, iteratedEpochs):
        print '--------------'
        #print self.matrix
        #''' Used for debugging
        print 'Epoch: ' + str(iteratedEpochs)
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

