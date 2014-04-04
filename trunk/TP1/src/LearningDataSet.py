from LearningData import LearningData

class LearningDataSet:

    def __init__(self, objectiveDescription, epochs, epsilon, etta):
        self.objective = objectiveDescription
        self.epochs = epochs
        self.epsilon = epsilon
        self.etta = etta
        self.learningSet = []
        
    def getEpochs(self):
        return self.epochs
            
    def getSet(self):
        return self.learningSet
        
    def addLearningData(self, input, expectedOutput):
        self.learningSet.append(LearningData(input, expectedOutput))
