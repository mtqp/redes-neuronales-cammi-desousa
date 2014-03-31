from LearningData import LearningData
import sys

class FileParser:

    def __init__(self, inputFileName, outputFileName):
        self.inputFileName  = inputFileName
        self.outputFileName = outputFileName
            
    def getLearningIterations(self):
        return 4 #levantar del archivo!
            
    def getLearningDataSet(self):
        return [LearningData(), LearningData()] #levantar del archivo
    
    def testMethod(self):
        print "this is a test: " + self.inputFileName
