from FileParser import FileParser
from LearningData import LearningData
from Plotter import Plotter
from NeuralNetworkAlgorithm import * 
from SimplePerceptron import *
import sys
import numpy as np
import math

def main():
    fileParser = FileParser("C:\Facultad\RedesNeuronales\TP1\src\README_INPUT.TXT") #open from arguments
    parameters = fileParser.parseInputFile()
    
    neuralAlgorithm = SimplePerceptron(parameters)#NeuralNetworkAlgorithm(parameters) #deberia ser abstracto, usar la implementacion concreta
    
    print 'neural algorithm started training'
    neuralAlgorithm.train()
    print 'neural algorithm finished training'
    
    trainingInformation = neuralAlgorithm.getTrainingInformation()

    errorFileName = '.\\..\\graphics\\error - ' + parameters.objective
    plotter = Plotter(errorFileName, "validationfile")
    plotter.plotError(trainingInformation.errors)
    
if __name__ == "__main__":
    main()
