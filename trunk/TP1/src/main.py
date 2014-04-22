from FileParser import FileParser
from OCRInputCreator import *
from FunctionInputCreator import *
from LearningData import LearningData
from Plotter import Plotter
from MultiLayerPerceptron import * 
from SimplePerceptron import *
from Functions import *
import sys
import numpy as np
import math

def main():
    createFunctionInput()
   
    #createOCR()
    
    #executeSimplePerceptron()
    
def createFunctionInput():
    trainingCount = 5
    testingCount = 20
    epsilon = 0.1
    etta = 0.07
    epochs = 1500
    hiddenNodes = 10
    neuralType = StandardBP() 
    #neuralType = AdaptiveWithMomentumBP() 
    #neuralType = MomentumBP() 
    fileNameStandard = 'C:\Facultad\RedesNeuronales\TP1\src\FuncAprox\StandardBP.m'
    fileNameAdaptativeWithMomentum = 'C:\Facultad\RedesNeuronales\TP1\src\FuncAprox\AdaptativeWithMomentumBP.m'
    fileNameMomentum = 'C:\Facultad\RedesNeuronales\TP1\src\FuncAprox\MomentumBP.m'
    fileName = fileNameStandard #modificar aca para el archivo que quieras!
    functionCreator = FunctionInputCreator(fileName, trainingCount, testingCount, epsilon, etta, epochs, neuralType, hiddenNodes)
    functionCreator.create()
 
def createOCR():
    ocrCreator = OCRInputCreator()
    epsilon = 0.1
    etta = 0.17
    epochs = 1500
    description = 'OCR'
    fileNameToCreate = 'C:\Facultad\RedesNeuronales\TP1\src\OCR\input_martin.txt'
    expectedOutputSource = 'C:\Facultad\RedesNeuronales\TP1\src\OCR\output - test.txt'
    #allInputLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    inputLetters = ['a','t','u','v','w','x','y','z']
    ocrParameters = OCRParameters(inputLetters)
    #ocrParameters = OCRParameters() #no filter, same input as testinput
    ocrCreator.createInput(epsilon, etta, epochs, description, fileNameToCreate, expectedOutputSource, ocrParameters)
    
def executeSimplePerceptron():
    fileParser = FileParser("C:\Facultad\RedesNeuronales\TP1\src\README_INPUT.TXT") #open from arguments
    #fileParser = FileParser('C:\Facultad\RedesNeuronales\TP1\src\OCR\input_test.txt') #open from arguments
    #fileParser = FileParser('C:\Facultad\RedesNeuronales\TP1\src\OCR\input_test_with_testing_data.txt') #open from arguments
    #fileParser = FileParser('C:\Facultad\RedesNeuronales\TP1\src\OCR\input_test_with_same_testing_data.txt') #open from arguments
    #fileParser = FileParser('C:\Facultad\RedesNeuronales\TP1\src\OCR\input_martin.txt') #open from arguments
    parameters = fileParser.parseInputFile()
    
    function = Sign()#Identity()#Exponential(0.5)#
    VERBOSE = True
    SHUFFLE_TRAINING_SET = True
    neuralAlgorithm = SimplePerceptron(parameters, function, SHUFFLE_TRAINING_SET, not VERBOSE)#NeuralNetworkAlgorithm(parameters) #deberia ser abstracto, usar la implementacion concreta
    
    print 'ALGORITHM - Start'
    neuralAlgorithm.train()
    print 'ALGORITHM - Finish'
    
    trainingInformation = neuralAlgorithm.getTrainingInformation()

    errorFileName = '.\\..\\graphics\\error - ' + parameters.objective
    validationFileName = '.\\..\\graphics\\validation - ' + parameters.objective
    testingFileName = '.\\..\\graphics\\testing - ' + parameters.objective
    SAVE_TO_FILE = True
    SHOW = True
    plotter = Plotter(errorFileName, validationFileName, testingFileName, not SAVE_TO_FILE)
    plotter.plot(trainingInformation, SHOW)
    
if __name__ == "__main__":
    main()
