import sys
import numpy as np
import math

class SimplePerceptron: 

    def __init__(self, parameters):
        self.parameters = parameters
        self.matrix = np.matrix('0.1 0.1 0.1; 0.1 0.1 0.1').transpose() #inicializar con algo que sea util
        print 'whole learning matrix: ' + str(self.matrix)
        self.counter = 0
        
    def train(self): #COMO SE QUE UMBRAL, PARAMETROS DEBO PONER?
        epsilonOnIteration = 1
        iteratedEpochs = 0
        
        while epsilonOnIteration > self.parameters.epsilon and iteratedEpochs < self.parameters.epochs:
            shuffledLearningDatas = self.parameters.getShuffledData()
            
            iterationErrors = []
            for learningData in shuffledLearningDatas:
                evaluationVector = self.applySignFunction(learningData.input, self.matrix)
                iterationError = np.subtract(learningData.expectedOutput, evaluationVector)
                iterationErrors.append(iterationError)
                
                #---> Line below does: 
                #---- etta * ( learninData.input.transpose() x iterationerror ) *gprima /en nuestro caso no va xq la derivada es 1
                transposeInput = np.matrix(learningData.input).transpose()
                iterationErrorMatrix = np.matrix(iterationError)
                deltaMatrix = np.dot(self.parameters.etta, np.dot(transposeInput, iterationErrorMatrix)) 
                
                self.matrix = np.add(self.matrix,deltaMatrix) #algoritmo incremental
                self.showEvolution()
        
            epsilonOnIteration = 0.5 * self.sumSquaredNorms(iterationErrors)
            iteratedEpochs += 1
        
    def sumSquaredNorms(self, errors):
        return sum([self.squaredNorm(e) for e in errors])
        
    def squaredNorm(self, vector):
        return sum([math.pow(v,2) for v in vector])
        
    def applySignFunction(self, vector, matrix): 
        #el vector se lo multiplica por cada vector columna de la matrix 
        #y luego se le aplica la funcion signo
        
        columnsAsRows = matrix.transpose() #es un truquito para poder agarrar rapido las columnas, no se si se puede hacer de otra forma mas eficiente
        vectorDotMatrix = []
        for columnIndex in range(0, columnsAsRows.shape[0]-1):
            matrixVector = columnsAsRows[columnIndex].transpose()
            vectorDotMatrix.append(np.dot(vector, matrixVector))
        
        return [self.sign(acum) for acum in vectorDotMatrix]
    
    def sign(self, value):
        if value > 0:
            return 1
        return -1
       
    def testWhatWasLearnt(self):
        print '--------------'
        for learningData in self.parameters.learningSet:
            obtainedVector = np.dot(learningData.input, self.matrix)
            print 'input: ' + str(learningData.input)
            print str(learningData.expectedOutput) + ' --> expected'
            print str(obtainedVector) + ' --> obtained'
            print '--------------'
            
    def showEvolution(self):
        print 'matrix evolution, counter: ' + str(self.counter)
        print self.matrix
        self.counter+=1        

