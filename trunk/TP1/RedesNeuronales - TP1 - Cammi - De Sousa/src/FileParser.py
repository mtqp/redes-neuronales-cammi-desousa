from NeuralAlgorithmParameters import NeuralAlgorithmParameters
import sys

class FileParser:

    def __init__(self, inputFileName):
        self.inputFileName  = inputFileName
 
    def parseInputFile(self):
        inputFile = open(self.inputFileName, 'r')

        firstLine = inputFile.readline()
        objectiveDescription = firstLine.lstrip("name=").strip()
        print "FP - objective description: " + objectiveDescription
        
        secondLine = inputFile.readline()
        etta = secondLine.lstrip("etta=").strip()
        print "FP - etta: " + etta
        
        thirdLine = inputFile.readline()
        epsilon = thirdLine.lstrip("epsilon=").strip()
        print "FP - epsilon: " + epsilon
        
        fourthLine = inputFile.readline()
        epochs = fourthLine.lstrip("epochs=").strip()
        print "FP - epochs: " + epochs
 
        parameters = NeuralAlgorithmParameters(objectiveDescription, int(epochs), float(epsilon), float(etta))
        
        for line in inputFile.readlines():
            setLine = ''
            isTestingData = 'testing' in line
            if isTestingData:
                setLine = line.lstrip("testingset").strip()
            else:
                setLine = line.lstrip("set").strip()
            splittedSetLine = setLine.split("=")
            
            input = splittedSetLine[0].strip()
            expectedOutput = splittedSetLine[1].strip()
            
            if isTestingData:
                parameters.addTestingData(input, expectedOutput)
            else:
                parameters.addLearningData(input, expectedOutput)
        
        self.addTestsIfNoOneWasProvided(parameters)
       
        inputFile.close()
        return parameters
        
        
    def addTestsIfNoOneWasProvided(self, parameters):
        if len(parameters.testingSet) == 0:
            for learningData in parameters.learningSet:
                parameters.testingSet.append(learningData)
  