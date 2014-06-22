import numpy as np
from Hopefield import Hopefield
from DataSetCreator import DataSetCreator
from Letter import Letter

def main():
    SYNCH = True
    dim = 25
    bitReshapedToSquareDimension = dim / 5
    n = dim * dim
    hopfield = Hopefield(n)

    #DataSet
    letters = allLetters()
    #letters = [Letter("A", [0,1,1,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1])]
    dataSetVectors = [ np.matrix(letter.reshapeEachBitIntoSquareOf(bitReshapedToSquareDimension)) for letter in letters ]

    #Learning
    hopfield.training(dataSetVectors)

    #Activation
    print 'Activation step:'
    i = 0
    for inputVector in dataSetVectors:
        hopfieldActivation = hopfield.activate(inputVector,not SYNCH)
        equalityReached = (inputVector == hopfieldActivation).all()
        description = 'Letter: ' + letters[i].stringValue + '. Are equal? ' + str(equalityReached)
        if not equalityReached:
            description += ' - ERROR!'
        print description
        if not equalityReached:
            printLetterWithDimension("DataSet", dim, letters[i].reshapeEachBitIntoSquareOf(bitReshapedToSquareDimension))
            printLetterWithDimension("Result", dim, hopfieldActivation.flatten())

        i += 1

def printLetterWithDimension(header, dim, vector):
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
