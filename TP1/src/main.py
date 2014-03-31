from FileParser import FileParser
from LearningData import LearningData
from NeuralNetworkAlgorithms import * 
import sys

def main():
    fileParser = FileParser("C:\Facultad\RedesNeuronales\TP1\src\README_INPUT.TXT", "outputFileName") #open from arguments
    learningDataSet = fileParser.parseInputFile()
    
    neuralAlgorithm = NeuralNetworkAlgorithm() #deberia ser abstracto, usar la implementacion concreta
    
    for iteration in range(0, learningDataSet.getIterations()):
        for learningData in learningDataSet.getSet():
            neuralAlgorithm.learnWith(learningData)

if __name__ == "__main__":
    main()