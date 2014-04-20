from FileParser import FileParser
from OCRInputCreator import OCRInputCreator
from LearningData import LearningData
from Plotter import Plotter
from NeuralNetworkAlgorithm import * 
from SimplePerceptron import *
from Functions import *
import sys
import numpy as np
import math

def main():
    '''
    ocrCreator = OCRInputCreator()
    epsilon = 0.1
    etta = 0.17
    epochs = 150
    description = 'OCR'
    fileNameToCreate = 'C:\Facultad\RedesNeuronales\TP1\src\OCR\input_test.txt'
    expectedOutputSource = 'C:\Facultad\RedesNeuronales\TP1\src\OCR\output - test.txt'
    
    ocrCreator.createInput(epsilon, etta, epochs, description, fileNameToCreate, expectedOutputSource)
    '''
    
    #'''
    fileParser = FileParser("C:\Facultad\RedesNeuronales\TP1\src\README_INPUT.TXT") #open from arguments
    #fileParser = FileParser('C:\Facultad\RedesNeuronales\TP1\src\OCR\input_test.txt') #open from arguments
    parameters = fileParser.parseInputFile()
    
    function = Exponential(0.5)#Identity()
    VERBOSE = True
    neuralAlgorithm = SimplePerceptron(parameters, function, not VERBOSE)#NeuralNetworkAlgorithm(parameters) #deberia ser abstracto, usar la implementacion concreta
    
    print 'ALGORITHM - Start'
    neuralAlgorithm.train()
    print 'ALGORITHM - Finish'
    
    trainingInformation = neuralAlgorithm.getTrainingInformation()

    errorFileName = '.\\..\\graphics\\error - ' + parameters.objective
    validationFileName = '.\\..\\graphics\\validation - ' + parameters.objective
    SAVE_TO_FILE = True
    SHOW = True
    plotter = Plotter(errorFileName, validationFileName, not SAVE_TO_FILE)
    plotter.plot(trainingInformation, SHOW)
    #'''
    
    
if __name__ == "__main__":
    main()
