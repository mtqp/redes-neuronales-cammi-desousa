from FileParser import FileParser
from LearningData import LearningData
from NeuralNetworkAlgorithm import * 
import sys

def main():
    fileParser = FileParser("C:\Facultad\RedesNeuronales\TP1\src\README_INPUT.TXT", "outputFileName") #open from arguments
    parameters = fileParser.parseInputFile()
    
    neuralAlgorithm = NeuralNetworkAlgorithm(parameters) #deberia ser abstracto, usar la implementacion concreta
    
    print 'neural algorithm started training'
    neuralAlgorithm.train()
    print 'neural algorithm finished training'
    
    learningInformation = neuralAlgorithm.getLearningInformation()

    fileParser.save(learningInformation)
    print 'learning information saved'

if __name__ == "__main__":
    main()