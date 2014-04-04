import sys

class NeuralNetworkAlgorithm: #por ahora va a tener cableado el perceptron simple, pero la idea es generalizarlo

    def __init__(self, parameters):
        self.parameters = parameters.epsilon
        self.layersCount = 1 #parametrizar
        
        
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