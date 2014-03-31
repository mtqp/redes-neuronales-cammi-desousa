
class LearningData:

    def __init__(self, input, expectedOuput):
        cleanInput = input.strip("[]")
        cleanExpectedOutput = expectedOuput.strip("[]")
        self.input = [int(splittedValue) for splittedValue in cleanInput.split(",")]
        print "input:           " + str(self.input)
        
        self.expectedOutput = [int(splittedValue) for splittedValue in cleanExpectedOutput.split(",")]
        print "expected output: " + str(self.expectedOutput)
