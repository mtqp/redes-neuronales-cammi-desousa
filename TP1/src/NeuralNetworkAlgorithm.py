import sys
import numpy as np

class NeuralNetworkAlgorithm: #por ahora va a tener cableado el perceptron simple, pero la idea es generalizarlo

    def __init__(self, parameters):
        self.parameters = parameters
        self.createContext() #horrible nombre! cambiarlo!
        
    def createContext(self):
        self.layers = [[0,0],[0,0]] #parametrizar, estoy usando esto para ver si aprende or y and.
        self.matrixes = [np.matrix('1 1; 1 1')] #inicializar con algo que sea util
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
        
        print 'this should be implemented!'
        
    def updateEpsilonOnIteration(self):
        print 'updateEpsilonOnIteration method not implemented'
        
    def updateMatrixes(self):
        print 'update matrixes method not implemented'
        
    def correctWith(self, learningData):
        self.activateWith(learningData)
        
        print 'correctWith method not implemented'
        
    def activateWith(self, learningData):
        print 'activateWith method not implemented'
        
    def getLearningInformation(self):
        return None