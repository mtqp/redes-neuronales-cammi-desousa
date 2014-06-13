
from Hopfield import Hopfield
from DataSetCreator import DataSetCreator

def main():

    #Initialize
    n = 4
    amountOfVectors = 5
    firstBound = 0
    endBound = 10
    method = DataSetCreator.UNIFORM
    hopfield = Hopfield()

    #DataSet Generation
    dataSetCreator = DataSetCreator(n)
    dataSetVectors = dataSetCreator.getRandomDataSetOfVectors(amountOfVectors, firstBound, endBound, method)

    #Learning
    hopfield.training(dataSetVectors)


if __name__ == "__main__":
    main()
