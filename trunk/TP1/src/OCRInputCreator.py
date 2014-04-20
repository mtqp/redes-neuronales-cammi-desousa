import sys

class OCRInputCreator:

    def __init__(self):
        self.letters = []
        self.expectedOutputs = []

    def createInput(self, epsilon, etta, epochs, description, fileNameToCreate, expectedOutputSource):
        self.readInputNoNoise()
        self.readExpectedOutputs(expectedOutputSource)
        
        f = open(fileNameToCreate,'w')
        f.write('name=' + description +'\n') 
        f.write('etta=' + str(etta) +'\n') 
        f.write('epsilon=' + str(epsilon) +'\n') 
        f.write('epochs=' + str(epochs) +'\n') 

        for letter in self.getLearningSet(): 
            f.write('set ' + letter.binaryIn + ' = ' + letter.binaryOut + '\n')
        for letter in self.getTestingSet():
            f.write('testingset ' + letter.binaryIn + ' = ' + letter.binaryOut + '\n')
        
        f.close() 
     
    #def createInput(self, epsilon, etta, epochs, description, learningSet, noisePercentage):
    def readExpectedOutputs(self, fileName):
        inputFile = open(fileName, 'r')
        
        while True:
            stringLetter=inputFile.readline()
            if not stringLetter: break
            letter = [l for l in self.letters if l.stringValue == stringLetter][0]
            letter.binaryOut = inputFile.readline().strip() #lee su representacion binaria
                
        inputFile.close()
    
    def getTestingSet(self):
        return self.letters #en realidad hay que devolver un subset, xq el resto es el que vas a usar para testear
        
    def getLearningSet(self):
        return self.letters #en realidad hay que devolver un subset, xq el resto es el que vas a usar para testear
        
    def readInputNoNoise(self):
        inputFile = open('C:\Facultad\RedesNeuronales\TP1\src\OCR\letter_representation.txt', 'r')
        
        while True:
            letter=inputFile.readline()
            if not letter: break
            
            binaryArray = inputFile.readline().strip()                  #1ros 5 bits
            binaryArray =  binaryArray + inputFile.readline().strip()   #2dos 5 bits
            binaryArray =  binaryArray + inputFile.readline().strip()   #3ros 5 bits
            binaryArray =  binaryArray + inputFile.readline().strip()   #4tos 5 bits
            binaryArray =  binaryArray + inputFile.readline().strip()   #5tos 5 bits
            self.letters.append(Letter(letter, binaryArray))
                
        inputFile.close()
        
class Letter:
    def __init__(self, aString, binaryArray):
        self.stringValue = aString
        self.binaryIn = binaryArray
        self.binaryOut = ''
        
    def setOutput(self, aBinaryArray):
        self.binaryOut = aBinnaryArray