import numpy as np
from HopefieldStochastic import HopefieldStochastic
from DataSetCreator import *
from Letter import Letter
import Hamming

''''
    todo: GENERAR LOS 10 VECTORES,
    GENERAR LAS INSTANCIAS DE TEST
    LOOPEAR TODO PARA DISTINTAS TEMPERATURAS
''''

def main():

    dim = 15
    bitReshapedToSquareDimension = dim / 5
    n = dim * dim
    temperature = 0.2
    hammingPercentage = 0.1
    randomSetsCount = 10
    MUST_BE_UNIQUE = True
    PRINT_DETAIL = False
    hopfieldStochastic = HopefieldStochastic(n, temperature, hammingPercentage)

    #DataSet
    dataSetCreator = DataSetCreator(n)
    dataSetVectors = dataSetCreator.getRandomDataSetOfVectors(randomSetsCount, -1, 1, DataSetCreator.UNIFORM, MUST_BE_UNIQUE)

    '''
    letters = allLetters()
    letters = [Letter("A", [0,1,1,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1])]
    dataSetVectors = [ np.matrix(letter.reshapeEachBitIntoSquareOf(bitReshapedToSquareDimension)) for letter in letters ]
    '''

    #Learning
    hopfieldStochastic.training(dataSetVectors)

    #Activation
    print 'Activation step:'
    i = 0
    for inputVector in dataSetVectors:
        hopfieldActivation = hopfieldStochastic.activate(inputVector)
        equalityReached = (inputVector == hopfieldActivation).all()
        description = 'Vector: ' + str(i) + '. Are equal? ' + str(equalityReached)
        if not equalityReached:
            description += ' - ERROR!'
        print description
        if PRINT_DETAIL and not equalityReached:
            printVectorWithDimension("DataSet", dim, dataSetVectors[i].flatten())
            printVectorWithDimension("Result", dim, hopfieldActivation.flatten())

        i += 1

def printVectorWithDimension(header, dim, vector):
    print header

    for i in range(0, len(vector), dim):
        vectorLine = vector[i:i+dim]
        vectorLine = [int(v) for v in vectorLine]
        for vi in range(0,len(vectorLine)):
            if(vectorLine[vi] == -1):
                vectorLine[vi] = 0

        print vectorLine

def showVectors(dataSetVectors):
    print 'vectors:'
    i = 0
    for it in dataSetVectors:
        print str(i+1) + ') ' + str(it)
        i += 1

def allLetters():
    letters = []
    letters.append(Letter("A", [0,1,1,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1]))
    letters.append(Letter("B", [1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,0,0,0,1,1,1,1,1,0]))
    letters.append(Letter("C", [0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,1,1]))
    letters.append(Letter("D", [1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0]))
    letters.append(Letter("E", [1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,1,1,1,1]))
    letters.append(Letter("F", [1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0]))
    letters.append(Letter("G", [0,1,1,1,1,1,0,0,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,1,0]))
    letters.append(Letter("H", [1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1]))
    letters.append(Letter("I", [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]))
    letters.append(Letter("J", [0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0]))
    letters.append(Letter("K", [1,0,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1]))
    letters.append(Letter("L", [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1]))
    letters.append(Letter("M", [1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,0,1]))
    letters.append(Letter("N", [1,0,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,1]))
    letters.append(Letter("O", [0,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0]))
    letters.append(Letter("P", [1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,0,0,0,0,1,0,0,0,0]))
    letters.append(Letter("Q", [0,1,1,1,0,1,0,0,0,1,1,0,1,0,1,1,0,0,1,0,0,1,1,0,1]))
    letters.append(Letter("R", [1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,1]))
    letters.append(Letter("S", [0,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,0]))
    letters.append(Letter("T", [1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]))
    letters.append(Letter("U", [1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0]))
    letters.append(Letter("V", [1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0]))
    letters.append(Letter("W", [1,0,0,0,1,1,0,0,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1]))
    letters.append(Letter("X", [1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1]))
    letters.append(Letter("Y", [1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]))
    letters.append(Letter("Z", [1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1]))
    return letters

if __name__ == "__main__":
    main()
