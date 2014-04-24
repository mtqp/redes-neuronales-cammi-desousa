"""Simple matshow() example."""
from matplotlib.pylab import *

def samplemat(dims):
    """Make a matrix with all zeros and increasing elements on the diagonal"""
    aa = zeros(dims)
    for i in range(min(dims)):
        aa[i, i] = i
    return aa

def printLetters(letters):
    matrix = np.zeros((18, 60)) 

    #COLUMN = 0
    #ROW = 1
    #for columnIndex in range(0, matrix.shape[COLUMN]):
    #    for rowIndex in range(0, matrix.shape[ROW]):
    #        matrix[columnIndex][rowIndex] = 1.0

    #lettersAux = range(2) #np.array(2) 
    #lettersAux[0] = letters[0]
    #lettersAux[1] = letters[1]
    #letters = lettersAux

    startRowIndex = 0
    startColumnIndex = 0
    countletters = 0
    for letter in letters:

        if countletters == 10:
            startRowIndex = startRowIndex + 6
            startColumnIndex = 0
            countletters = 0
            addRowSeparator(matrix, startRowIndex - 1) 

        letterBinaryIn = letterStrToArray(letter)

        rowIndex = startRowIndex
        columnIndex = startColumnIndex
        for bit in letterBinaryIn:
		    if columnIndex == 5 + startColumnIndex:
		        rowIndex = rowIndex + 1
		        columnIndex = startColumnIndex
		    matrix[rowIndex][columnIndex] = 1 - bit
		    columnIndex = columnIndex + 1

        addColumnSeparator(matrix, startRowIndex, columnIndex)
        startColumnIndex = startColumnIndex + 6
        countletters = countletters + 1

    addRowSeparator(matrix, startRowIndex + 5) 

    #print matrix
    matshow(matrix, fignum=1, cmap=cm.gray)
    show()
	
	#print letters[0].binaryIn

def addColumnSeparator(matrix, rowIndex, columnIndex):
    matrix[rowIndex + 0][columnIndex] = 1
    matrix[rowIndex + 1][columnIndex] = 1
    matrix[rowIndex + 2][columnIndex] = 1
    matrix[rowIndex + 3][columnIndex] = 1
    matrix[rowIndex + 4][columnIndex] = 1

def addRowSeparator(matrix, rowIndex):
    ROW = 1
    for columnIndex in range(0, matrix.shape[ROW]): 
        matrix[rowIndex][columnIndex] = 1

def printLetter(letters):
    matrix = np.zeros((5,5)) 
    #for letter in letters:
    letterBinaryInStr = letters[0].binaryIn

    cleanInput = letterBinaryInStr.strip("[]")
    inputList = [float(splittedValue) for splittedValue in cleanInput.split(",")]
    letterBinaryIn = np.array(inputList)

    rowIndex = 0
    columnIndex = 0
    for bit in letterBinaryIn:
        if columnIndex == 5:
            rowIndex = rowIndex + 1
            columnIndex = 0
        matrix[rowIndex][columnIndex] = 1 - bit
        columnIndex = columnIndex + 1

    #print matrix
    matshow(matrix, fignum=1, cmap=cm.gray)
    show()
	
	#print letters[0].binaryIn

def letterStrToArray(letter):
    letterBinaryInStr =	letter.binaryIn
    cleanInput = letterBinaryInStr.strip("[]")
    inputList = [float(splittedValue) for splittedValue in cleanInput.split(",")]
    letterBinaryIn = np.array(inputList)
    return letterBinaryIn

	#print rand(5,5)

# Display 2 matrices of different sizes
#dimlist = [(5, 5)]
#for d in dimlist:
#    matshow(samplemat(d))

# Display a random matrix with a specified figure number and a grayscale
# colormap

