import numpy as np

class LearningData:

    def __init__(self, input, expectedOuput):
        cleanInput = input.strip("[]")
        cleanExpectedOutput = expectedOuput.strip("[]")
        inputList = [float(splittedValue) for splittedValue in cleanInput.split(",")]
        self.input = np.array(inputList)
        print "input:           " + str(self.input)
        
        expectedOutputList = [float(splittedValue) for splittedValue in cleanExpectedOutput.split(",")]
        self.expectedOutput = np.array(expectedOutputList)
        print "expected output: " + str(self.expectedOutput)
