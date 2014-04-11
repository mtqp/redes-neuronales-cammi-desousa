import sys
import numpy as np

class NeuralNetworkAlgorithm: #por ahora va a tener cableado el perceptron simple, pero la idea es generalizarlo

    def __init__(self, parameters):
        self.parameters = parameters
        self.createContext() #horrible nombre! cambiarlo!
        
    def createContext(self): #parametrizar, estoy usando esto para ver si aprende or y and.
        self.layers = [[0,0],[0,0]] 
        self.matrixes = [np.matrix('1 1; 1 1')] #inicializar con algo que sea util
        self.modificationMatrixes = [np.matrix('1 1; 1 1')] #guarda los valores que modifico la iteracion
        self.evaluationVectors = [[1,1]]
        self.layerErrors = [0,0]  #error de cada capa

        #falta inicializar todo el resto
        
    def train(self):
        epsilonOnIteration = 1
        iteratedEpochs = 0
        
        while epsilonOnIteration > self.parameters.epsilon and iteratedEpochs < self.parameters.epochs:
            shuffledLearningDatas = self.parameters.getShuffledData()
            
            for learningData in shuffledLearningDatas:
                self.correctWith(learningData)
                self.updateMatrixes()
                
                #Hp = E_l * E_l --> que es esto?
        
            epsilonOnIteration = self.updateEpsilonOnIteration()
            iteratedEpochs += 1
        
    def updateEpsilonOnIteration(self):
        print 'updateEpsilonOnIteration method not implemented'
        
    def updateMatrixes(self):
        for index in range(0,len(self.matrixes)-1):
            ettaDotModificationMatrix = np.dot(self.parameters.etta, self.modificationMatrixes[index])
            self.matrixes[index] = self.matrixes[index] + ettaDotModificationMatrix
        
    def correctWith(self, learningData): #aplica backpropagation
        self.activateWith(learningData)
        
        networkOutput = self.evaluationVectors[len(self.evaluationVectors)-1]
        networkError = learningData.expectedOuput - networkOutput
        
        for index in range(len(self.layers),1):
            derivedEvaluationVector = self.applyDerivedG(self.evaluationVectors[index])
            
            
        print 'correctWith method not implemented'
        
    def activateWith(self, learningData):
        self.evaluationVectors[0] = self.applyG(learningData.input, self.matrixes[0])
        for index in range(1, len(self.matrixes)-1): # activa el nivel I con el nivel I-1 * el valor de la matrix I
            previousVector = self.evaluationVectors[index-1]
            self.evaluationVectors[index] = self.applyG(previousVector, self.matrixes[index])
    
    def applyG(self, vector, matrix): #hay que ponerle un mejor nombre!!!
        print 'applyG method not implemented' 
    
    def getLearningInformation(self):
        return None