from FileParser import FileParser
from LearningData import LearningData
from NeuralNetworkAlgorithm import * 
from SimplePerceptron import *
import sys
import numpy as np
import math

def main():
    fileParser = FileParser("C:\Facultad\RedesNeuronales\TP1\src\README_INPUT.TXT", "outputFileName") #open from arguments
    parameters = fileParser.parseInputFile()
    
    neuralAlgorithm = SimplePerceptron(parameters)#NeuralNetworkAlgorithm(parameters) #deberia ser abstracto, usar la implementacion concreta
    
    print 'neural algorithm started training'
    neuralAlgorithm.train()
    print 'neural algorithm finished training'
    
    learningInformation = neuralAlgorithm.testWhatWasLearnt()
    #learningInformation = neuralAlgorithm.testWhatWasLearnt()

    fileParser.save(learningInformation)
    print 'learning information saved'

if __name__ == "__main__":
    main()
