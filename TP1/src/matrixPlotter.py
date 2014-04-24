"""Simple matshow() example."""
from matplotlib.pylab import *

def samplemat(dims):
    """Make a matrix with all zeros and increasing elements on the diagonal"""
    aa = zeros(dims)
    for i in range(min(dims)):
        aa[i, i] = i
    return aa

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

def clearLetter(letterBinaryInStr):
    cleanInput = letterBinaryInStr.strip("[]")
    inputList = [float(splittedValue) for splittedValue in cleanInput.split(",")]
    letterBinaryIn = np.array(inputList)
    

	#print rand(5,5)

# Display 2 matrices of different sizes
#dimlist = [(5, 5)]
#for d in dimlist:
#    matshow(samplemat(d))

# Display a random matrix with a specified figure number and a grayscale
# colormap

