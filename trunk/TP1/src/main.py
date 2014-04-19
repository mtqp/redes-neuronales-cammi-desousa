from FileParser import FileParser
from OCRInputCreator import OCRInputCreator
from LearningData import LearningData
from Plotter import Plotter
from NeuralNetworkAlgorithm import * 
from SimplePerceptron import *
import sys
import numpy as np
import math

def main():
    '''
    ocrCreator = OCRInputCreator()
    epsilon = 0.1
    etta = 0.07
    epochs = 50
    description = 'test a ver si anda'
    fileNameToCreate = 'C:\Facultad\RedesNeuronales\TP1\src\OCR\input_test.txt'
    expectedOutputSource = 'C:\Facultad\RedesNeuronales\TP1\src\OCR\output - test.txt'
    
    ocrCreator.createInput(epsilon, etta, epochs, description, fileNameToCreate, expectedOutputSource)
    '''
    
    #'''
    #fileParser = FileParser("C:\Facultad\RedesNeuronales\TP1\src\README_INPUT.TXT") #open from arguments
    fileParser = FileParser('C:\Facultad\RedesNeuronales\TP1\src\OCR\input_test.txt') #open from arguments
    parameters = fileParser.parseInputFile()
    
    neuralAlgorithm = SimplePerceptron(parameters)#NeuralNetworkAlgorithm(parameters) #deberia ser abstracto, usar la implementacion concreta
    
    print 'neural algorithm started training'
    neuralAlgorithm.train()
    print 'neural algorithm finished training'
    
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
