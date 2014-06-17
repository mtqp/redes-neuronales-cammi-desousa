import numpy as np
from Hopefield import Hopefield
from DataSetCreator import DataSetCreator

def main():

    #Initialize
    n = 5
    amountOfVectors = 3
    firstBound = -1
    endBound = 1
    method = DataSetCreator.UNIFORM
    hopfield = Hopefield(n)

    #DataSet Generation
    #dataSetCreator = DataSetCreator(n)
    #dataSetVectors = dataSetCreator.getRandomDataSetOfVectors(amountOfVectors, firstBound, endBound, method)

    dataSetVectors = []

    vector1 = np.matrix([ 1,-1,  1,  1, -1])
    vector2 = np.matrix([ 1, 1, -1, -1,  1])
    vector3 = np.matrix([ 1, 1,  1, -1, -1])
    dataSetVectors.append(vector1)
    dataSetVectors.append(vector2)
    dataSetVectors.append(vector3)

    print 'Ortogonalidad 2-1: ' + str(vector2 * np.transpose(vector1))
    print 'Ortogonalidad 3-2: ' + str(vector3 * np.transpose(vector2))
    print 'Ortogonalidad 1-3: ' + str(vector1 * np.transpose(vector3))

    print 'vectors:'
    i = 0
    for it in dataSetVectors:
        print str(i) + ') ' + str(it)
        i += 1


    #print 'matrix before:'
    #print hopfield.matrix

    #Learning
    hopfield.training(dataSetVectors)
    print 'matrix after:'
    print hopfield.matrix

    #Activation
    print 'Activation step:'
    i = 0
    for it in dataSetVectors:
        s = hopfield.activate(it,False)
        print str(i) + ') ' + str(it) + ' == ' + str(s) + ' = ' + str((it == s).all())
        i += 1



if __name__ == "__main__":
    main()
