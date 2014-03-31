from FileParser import FileParser
from LearningData import LearningData
from NeuralNetworkAlgorithms import * 
import sys

def main():
    fileParser = FileParser("inputFileName", "outputFileName") #open from arguments
    learningIterations = fileParser.getLearningIterations() 
    learningDataSet = fileParser.getLearningDataSet()
    neuralAlgorithm = NeuralNetworkAlgorithm() #deberia ser abstracto, usar la implementacion concreta
    
    for iteration in range(0, learningIterations):
        for learningData in learningDataSet:
            neuralAlgorithm.learnWith(learningData)

if __name__ == "__main__":
    main()