
from Hopfield import Hopfield
from DataSetCreator import DataSetCreator

def main():

    #Initialize
    n = 10
    amountOfVectors = 5
    firstBound = -1
    endBound = 1
    method = DataSetCreator.UNIFORM
    hopfield = Hopfield(n)

    #DataSet Generation
    dataSetCreator = DataSetCreator(n)
    dataSetVectors = dataSetCreator.getRandomDataSetOfVectors(amountOfVectors, firstBound, endBound, method)

    print 'random vectors:'
    i = 0
    for it in dataSetVectors:
        print str(i) + ') ' + str(it)
        i += 1


    print 'matrix before:'
    print hopfield.matrix

    #Learning
    hopfield.training(dataSetVectors)
    print 'matrix after:'
    print hopfield.matrix

    #Activation
    print 'Activation step:'
    i = 0
    for it in dataSetVectors:
        s = hopfield.activate(it,False)
        print str(i) + ') ' + str(s)
        print 'Check: ' + str((dataSetVectors[i] == s).all())
        i += 1


if __name__ == "__main__":
    main()
