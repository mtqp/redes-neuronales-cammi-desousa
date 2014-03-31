#from LearningData import LearningData
from LearningDataSet import LearningDataSet
import sys

class FileParser:

    def __init__(self, inputFileName, outputFileName):
        self.inputFileName  = inputFileName
        self.outputFileName = outputFileName
 
    def parseInputFile(self):
        inputFile = open(self.inputFileName, 'r')

        firstLine = inputFile.readline()
        objectiveDescription = firstLine.lstrip("name=").strip()
        print "objective description: " + objectiveDescription
        
        secondLine = inputFile.readline()
        iterations = secondLine.lstrip("iterations=").strip()
        print "iterations: " + iterations
 
        learningDataSet = LearningDataSet(objectiveDescription, int(iterations))
        
        for line in inputFile.readlines():
            setLine = line.lstrip("set").strip()
            splittedSetLine = line.split("=")
            
            input = splittedSetLine[0].strip()
            expectedOutput = splittedSetLine[1].strip()
            
            learningDataSet.addLearningData(input, expectedOutput)
        
        inputFile.close()
        return learningDataSet
   