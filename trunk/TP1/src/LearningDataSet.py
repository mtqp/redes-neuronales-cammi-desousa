from LearningData import LearningData

class LearningDataSet:

    def __init__(self, objectiveDescription, iterations):
        self.objective = objectiveDescription
        self.iterations = iterations
        self.learningSet = []
        
    def getIterations(self):
        return self.iterations
            
    def getSet(self):
        return self.learningSet
        
    def addLearningData(self, input, expectedOutput):
        self.learningSet.append(LearningData(input, expectedOutput))
