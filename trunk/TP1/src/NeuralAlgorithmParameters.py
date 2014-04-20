import random
from LearningData import LearningData

class NeuralAlgorithmParameters:

    def __init__(self, objectiveDescription, epochs, epsilon, etta):
        self.objective = objectiveDescription
        self.epochs = epochs        #cantidad maxima de iteraciones
        self.epsilon = epsilon      #error minimo
        self.etta = etta            #coeficiente de aprendizaje
        self.learningSet = []
        self.testingSet = []
        
    def getNDimension(self):
        if len(self.learningSet) > 0:
            return len(self.learningSet[0].input)
        return 0
        
    def getMDimension(self):
        if len(self.learningSet) > 0:
            return len(self.learningSet[0].expectedOutput)
        return 0
        
    def getEpochs(self):
        return self.epochs

    def addLearningData(self, input, expectedOutput):
        self.learningSet.append(LearningData(input, expectedOutput))

    def addTestingData(self, input, expectedOutput):
        self.testingSet.append(LearningData(input, expectedOutput))
        
    def getShuffledData(self):
        setToShuffle = self.learningSet
        random.shuffle(setToShuffle)
        return setToShuffle