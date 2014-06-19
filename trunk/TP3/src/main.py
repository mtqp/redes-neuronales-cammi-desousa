import numpy as np
from Hopefield import Hopefield
from DataSetCreator import DataSetCreator

def main():

    #Initialize
    n = 20
    #n = 6
    amountOfVectors = 3
    firstBound = -1
    endBound = 1
    method = DataSetCreator.UNIFORM
    hopfield = Hopefield(n)

    #DataSet learning
    dataSetVectors = []
    vector1 = np.matrix([ 1.,-1,  1.,  1, -1, -1,  1,  1,  1, -1,  1,  1, -1,  1,  1,  1,  1,  1, -1,  1])
    vector2 = np.matrix([ 1., 1, -1.,  1,  1,  1,  1,  1, -1,  1,  1, -1,  1, -1,  1,  1,  1,  1,  1,  1])
    vector3 = np.matrix([ 1., -1, 1., -1, -1,  1,  1, -1, -1,  1,  1,  1, -1, -1, -1,  1, -1,  1,  1, -1])

    #DataSet Generation
    #dataSetCreator = DataSetCreator(n)
    #dataSetVectors = dataSetCreator.getRandomDataSetOfVectors(amountOfVectors, firstBound, endBound, method)



    #vector1 = np.matrix([ -1.,  1,  1,  1,  1,  1])
    #vector2 = np.matrix([ -1.,  1, -1,  1,  -1, 1])
    #vector3 = np.matrix([  1.,  1,  -1, -1,  1, 1])



    dataSetVectors.append(vector1)
    dataSetVectors.append(vector2)
    dataSetVectors.append(vector3)

    showVectors(dataSetVectors)

    print 'Ortogonalidad 1-2: ' + str(vector1 * np.transpose(vector2))
    print 'Ortogonalidad 2-3: ' + str(vector2 * np.transpose(vector3))
    print 'Ortogonalidad 3-1: ' + str(vector3 * np.transpose(vector1))

    print 'Matrix should be'
    untercio = 1/6.0
    matrixShouldBe = untercio * (np.transpose(vector1) * vector1 + np.transpose(vector2) * vector2 + np.transpose(vector3) * vector3)
    print str(matrixShouldBe)

# 1/3 (vector1*vector1 +  vector2*vector2 + vector3*vector3 )

    #print 'matrix before:'
    #print hopfield.matrix

    #Learning
    hopfield.training(dataSetVectors)
    print 'Matrix after:'
    print hopfield.matrix

    #Activation
    print 'Activation step:'
    i = 0
    for it in dataSetVectors:
        s = hopfield.activate(it,False)
        print str(i) + ') ' + str((it == s).all())
        print 'Vector ingresado: ' + str(it)
        print 'Vector resultado: ' + str(s)
        i += 1

def showVectors(dataSetVectors):
    print 'vectors:'
    i = 0
    for it in dataSetVectors:
        print str(i+1) + ') ' + str(it)
        i += 1


if __name__ == "__main__":
    main()
