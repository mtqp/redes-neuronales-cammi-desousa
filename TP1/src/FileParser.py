from NeuralAlgorithmParameters import NeuralAlgorithmParameters
import sys

class FileParser:

    def __init__(self, inputFileName):
        self.inputFileName  = inputFileName
 
    #deberia tener en cada linea el archivo algo mas representativo, en el caso de OCR por ejemplo la letra que representa
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
            setLine = line.lstrip("set").strip()
            splittedSetLine = setLine.split("=")
            
            input = splittedSetLine[0].strip()
            expectedOutput = splittedSetLine[1].strip()
            
            parameters.addLearningData(input, expectedOutput)
        
        inputFile.close()
        return parameters
   