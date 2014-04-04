import sys

class NeuralNetworkAlgorithm: #por ahora va a tener cableado el perceptron simple, pero la idea es generalizarlo

    def __init__(self, parameters):
        self.parameters = parameters
        self.layersCount = 1 #parametrizar
        createContext() #horrible nombre! cambiarlo!
        
    def createContext(self):
        layers = [[0,0],[0,0]] #parametrizar, estoy usando esto para ver si aprende or y and.
        #falta inicializar todo el resto
        
    def train(self):
        epsilonOnIteration = 1
        iteratedEpochs = 0
        
        while epsilonOnIteration > self.parameters.epsilon && iteratedEpochs < self.parameters.epochs:
            #shuffledLearningDatas = self.parameters.getShuffledData()
            
            #for learningData in shuffledLearningDatas:
            #    correction(learningData)
        print 'this should be implemented!'
        
    def getLearningInformation(self):
        return None