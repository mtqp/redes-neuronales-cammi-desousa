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
    #createFunctionInput()
   
    createOCR()
    executeSimplePerceptron()
    
def createFunctionInput():
    trainingCount = 100
    testingCount = 100
    epsilon = 0.01
    etta = 0.07
    epochs = 1500
    hiddenNodes = 10
    neuralType = StandardBP() 
    #neuralType = AdaptiveWithMomentumBP() 
    #neuralType = MomentumBP() 
    fileNameStandard = 'C:\Facultad\RedesNeuronales\TP1\src\FuncAprox\StandardBP - 2daPrueba.m'
    fileNameAdaptativeWithMomentum = 'C:\Facultad\RedesNeuronales\TP1\src\FuncAprox\AdaptativeWithMomentumBP.m'
    fileNameMomentum = 'C:\Facultad\RedesNeuronales\TP1\src\FuncAprox\MomentumBP.m'
    fileName = fileNameStandard #modificar aca para el archivo que quieras!
    functionCreator = FunctionInputCreator(fileName, trainingCount, testingCount, epsilon, etta, epochs, neuralType, hiddenNodes)
    functionCreator.create()    

def createOCR():
    ocrCreator = OCRInputCreator()
    epsilon = 0.1
    etta = 0.45		
    epochs = 3000
    description = 'OCR'
    #fileNameToCreate = 'C:\Facultad\RedesNeuronales\TP1\src\OCR\input_martin.txt'
    fileNameToCreate = '/home/martincammi/workspaceFacu/RedesNeuronales-TP1/src/OCR/input_ocr.txt'
    #expectedOutputSource = 'C:\Facultad\RedesNeuronales\TP1\src\OCR\output - test.txt'
    expectedOutputSource = '/home/martincammi/workspaceFacu/RedesNeuronales-TP1/src/OCR/output - test.txt'
    #allInputLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #output 1
    #inputLetters = ['a','t','u','v','w','x','y','z']
    #inputLetters = ['a','c','k','m','p','s','v','i','z'] Epsilon bound met on epoch: 28 with epsilon value: 0.0957016648753
    #inputLetters = ['a','c','k','m','p','s','v','y','z']  Epsilon bound met on epoch: 32 with epsilon value: 0.0996523297975
    #inputLetters = ['b','c','k','m','p','s','v','i','z']  Epsilon bound met on epoch: 37 with epsilon value: 0.0999554474727
    #inputLetters = ['a','c','k','m','p','s','v','i','z','o'] Epsilon bound met on epoch: 42 with epsilon value: 0.0986877393422
    #inputLetters = ['a','c','k','m','p','s','v','i','z','o','q'] Epsilon bound met on epoch: 53 with epsilon value: 0.0999464836713
    #inputLetters = ['a','o','k','m','p','s','v','i','z'] Epsilon bound met on epoch: 35 with epsilon value: 0.0957142676839
    #inputLetters = ['a','o','k','m','p','s','v','y','z'] Epsilon bound met on epoch: 37 with epsilon value: 0.0960456653437
    #inputLetters = ['a','o','k','n','p','s','v','i','z'] Epsilon bound met on epoch: 37 with epsilon value: 0.0960456653437
    #inputLetters = ['a','o','k','n','p','s','w','i','z'] Epsilon bound met on epoch: 51 with epsilon value: 0.0973521319883 (1.4 el peor error)
    #inputLetters = ['a','o','k','n','p','s','w','i','z','l'] Epsilon bound met on epoch: 60 with epsilon value: 0.0980399216728 (1.2 el peor error)
    #inputLetters = ['a','o','k','n','p','s','w','i','z','l', 'x'] Epsilon bound met on epoch: 81 with epsilon value: 0.0985070701868

    #output 2
    #inputLetters = ['a','o','k','n','p','s','w','i','z','l', 'x'] Epsilon bound met on epoch: 81 with epsilon value: 0.0985070701868
    #inputLetters = ['a','o','k','n','p','s','w','i','z','l', 'x'] 
    #inputLetters = ['r','t','m','v','b','q','p','e','j','s', 'f'] Epsilon bound met on epoch: 68 with epsilon value: 0.0999859423461
    #inputLetters = ['a','b','p','r','o','q','u','v','w','c'] Doble Curva.
    #inputLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    inputLetters = []
    noisePercentage = 0.2
    ocrParameters = OCRParameters(inputLetters,noisePercentage)
    #ocrParameters = OCRParameters(inputLetters, 0.5) #no filter, same input as testinput
    ocrCreator.createInput(epsilon, etta, epochs, description, fileNameToCreate, expectedOutputSource, ocrParameters)
    
def executeSimplePerceptron():
    fileParser = FileParser("/home/martincammi/workspaceFacu/RedesNeuronales-TP1/src/OCR/input_ocr.txt") #open from arguments
    #fileParser = FileParser('/home/martincammi/workspaceFacu/RedesNeuronales-TP1/src/OCR/input_test.txt') #open from arguments
    #fileParser = FileParser('/home/martincammi/workspaceFacu/RedesNeuronales-TP1/src/OCR/input_test_with_testing_data.txt') #open from arguments
    #fileParser = FileParser('/home/martincammi/workspaceFacu/RedesNeuronales-TP1/src/OCR/input_test_with_same_testing_data.txt') #open from arguments
    #fileParser = FileParser('/home/martincammi/workspaceFacu/RedesNeuronales-TP1/src/OCR/input_martin.txt') #open from arguments
    parameters = fileParser.parseInputFile()
    
    function = Exponential(0.5)
    #function = Identity()
    #function = Sign()

    VERBOSE = True
    SHUFFLE_TRAINING_SET = True
    neuralAlgorithm = SimplePerceptron(parameters, function, not SHUFFLE_TRAINING_SET, not VERBOSE)#NeuralNetworkAlgorithm(parameters) #deberia ser abstracto, usar la implementacion concreta
    
    print 'ALGORITHM - Start'
    neuralAlgorithm.train()
    print 'ALGORITHM - Finish'
    
    trainingInformation = neuralAlgorithm.getTrainingInformation()

    errorFileName = './/..//graphics//error - ' + parameters.objective
    validationFileName = './/..//graphics//validation - ' + parameters.objective
    testingFileName = './/..//graphics//testing - ' + parameters.objective
    SAVE_TO_FILE = True
    SHOW = True
    plotter = Plotter(errorFileName, validationFileName, testingFileName, not SAVE_TO_FILE)
    plotter.plot(trainingInformation, SHOW)
    #'''
    
    
if __name__ == "__main__":
    main()
