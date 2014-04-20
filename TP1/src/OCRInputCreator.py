import sys
from pprint import pprint

class OCRInputCreator:

    def __init__(self):
        self.letters = []
        self.expectedOutputs = []

    def createInput(self, epsilon, etta, epochs, description, fileNameToCreate, expectedOutputSource, ocrParameters):
        self.readInputNoNoise()
        self.readExpectedOutputs(expectedOutputSource)
        
        print 'OCR - Writing to file'
        f = open(fileNameToCreate,'w')
        f.write('name=' + description +'\n') 
        f.write('etta=' + str(etta) +'\n') 
        f.write('epsilon=' + str(epsilon) +'\n') 
        f.write('epochs=' + str(epochs) +'\n') 

        for letter in ocrParameters.getLearningSet(self.letters): 
            f.write('set ' + letter.binaryIn + ' = ' + letter.binaryOut + '\n')
        for letter in ocrParameters.getTestingSet(self.letters):
            f.write('testingset ' + letter.binaryIn + ' = ' + letter.binaryOut + '\n')
        
        print 'OCR - Writing completed'
        f.close() 
     
    #def createInput(self, epsilon, etta, epochs, description, learningSet, noisePercentage):
    def readExpectedOutputs(self, fileName):
        print 'OCR - Reading expected output'
        inputFile = open(fileName, 'r')
        
        while True:
            stringLetter = inputFile.readline()
            stringLetter = stringLetter.rstrip('\n').strip()
            if not stringLetter: 
                break
            letter = [l for l in self.letters if l.stringValue == stringLetter][0]
            letter.binaryOut = inputFile.readline().strip() #lee su representacion binaria
                
        inputFile.close()
 
    def readInputNoNoise(self):
        print 'OCR - Reading letter representation'
        inputFile = open('C:\Facultad\RedesNeuronales\TP1\src\OCR\letter_representation.txt', 'r')
        
        while True:
            letter = inputFile.readline()
            letter = letter.rstrip('\n').strip()
            if not letter: 
                break
            
            binaryArray = inputFile.readline().strip()                  #1ros 5 bits
            binaryArray =  binaryArray + inputFile.readline().strip()   #2dos 5 bits
            binaryArray =  binaryArray + inputFile.readline().strip()   #3ros 5 bits
            binaryArray =  binaryArray + inputFile.readline().strip()   #4tos 5 bits
            binaryArray =  binaryArray + inputFile.readline().strip()   #5tos 5 bits
            self.letters.append(Letter(letter, binaryArray))
                
        inputFile.close()
  
class OCRParameters:
    def __init__(self, stringLettersLearningSet=[], noiseCoefficient=0.0):
        self.stringLettersLearningSet = [stringLetter.upper() for stringLetter in stringLettersLearningSet]
        self.noise = noiseCoefficient
        
    def getTestingSet(self, allLetters):
        if len(self.stringLettersLearningSet) == 0:
            return allLetters
        filteredLetters = [letter for letter in allLetters if letter.stringValue not in self.stringLettersLearningSet]
        filteredLetters = self.applyNoise(filteredLetters)
        return filteredLetters
        
    def getLearningSet(self, allLetters): #no filtra el learningSet si se lo pasa vacio
        if len(self.stringLettersLearningSet) == 0:
            return allLetters
        filteredLetters = [letter for letter in allLetters if letter.stringValue in self.stringLettersLearningSet]
        return filteredLetters

    def applyNoise(self, letters):
        if self.noise == 0.0:
            return letters

        print 'OCR - No noise is being applied to letter inputs'
        noisedUpLetters = []
        for letter in letters:
            letterWithNoise = self.addNoiseTo(letter)
            noisedUpLetters.append(letterWithNoise)
        return noisedUpLetters

    def addNoiseTo(self, letter):
        return letter
        ''' No se me ocurre un buen algoritmo para aplicar ruido y que nos pueda servir
        binaryWithoutBrackets = letter.binaryIn.strip().lstrip('[').rstrip(']')
        splittedBits = binaryWithoutBrackets.split(',')
        '''
        
class Letter:
    def __init__(self, aString, binaryArray):
        self.stringValue = aString
        self.binaryIn = binaryArray
        self.binaryOut = ''
        
    def setOutput(self, aBinaryArray):
        self.binaryOut = aBinnaryArray
    
    def __str__(self):
        return self.stringValue
