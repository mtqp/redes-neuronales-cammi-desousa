
from SelfOrganizedMap import SelfOrganizedMap
from DataSetCreator import DataSetCreator
from MatrixVisualizer import MatrixVisualizer

def main():

    epochs =    10          # Cantidad de iteraciones
    alphaEtta = 0.3       # Disminucion del Etta
    alphaSigma = 0.3      # Disminucion del Sigma

    n = 2     #Longitud del vector, debe coincidir con la longitud del vector x
    m1 = 10
    m2 = 10
    intervalInit = 5
    intervalEnd = 10

    firstBoundX1 = 1
    endBoundX1 = 5
    firstBoundX2 = 10
    endBoundX2 = 15

    #1) Generate learning vectors
    #learningVectors = getLearningVectors()

    dataSetCreator = DataSetCreator(n)
    learningVectors = dataSetCreator.getRandomDataSetOfVectorsBidimensional(500, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)

    #2) Generate activation vectors
    #activationVectors = learningVectors
    #dataSetCreator = DataSetCreator(n)
    #activationVectors = dataSetCreator.getRandomDataSetOfVectorsBidimensional(1000, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)
    activationVectors = dataSetCreator.getRandomDataSetOfVectorsBidimensional2(1000, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)
    #activationVectors2 = dataSetCreator.getRandomDataSetOfVectorsBidimensional(250, 5, 10, 5, 10)

    #activationVectors.extend(activationVectors2)
    #dataSetCreator.getRandomDataSetOfVectorsBidimensional2(amountOfVectors, 6,9,16,20)

    #print 'activationVectors: ' + str(activationVectors)

    #3) Learn
    kohonenMap = SelfOrganizedMap(epochs,alphaEtta,alphaSigma,n,m1,m2, intervalInit, intervalEnd)
    kohonenMap.training(learningVectors,firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)

    #3.1) Clean visual Matrix relative boxes positions
    #kohonenMap.clearMatrixBoxesPositions()

    #4) Activate
    kohonenMap.test(activationVectors, m1, m2, 1,5,10,15)
    vTest = MatrixVisualizer(m1,m2)
    vTest.visualizePlotAxis(activationVectors, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)

    #5) See results
    #print 'resultMatrix: ' + str(kohonenMap.matrix)


def main2():

    epochs =    50           # Cantidad de iteraciones
    alphaEtta = 0.00003       # Disminucion del Etta
    alphaSigma = 0.00013      # Disminucion del Sigma

    n = 1     #Longitud del vector, debe coincidir con la longitud del vector x
    m1 = 10
    m2 = 10
    intervalInit = -5
    intervalEnd = 5

    #1) Generate learning vectors
    #learningVectors = getLearningVectors()

    dataSetCreator = DataSetCreator(n)
    learningVectors = dataSetCreator.getRandomDataSetOfVectors(500, intervalInit, intervalEnd, DataSetCreator.UNIFORM)

    #2) Generate activation vectors
    activationVectors = learningVectors
    dataSetCreator = DataSetCreator(n)
    activationVectors = dataSetCreator.getRandomDataSetOfVectors(10000, intervalInit, intervalEnd, DataSetCreator.UNIFORM)

    print 'activationVectors: ' + str(activationVectors)

    #3) Learn
    kohonenMap = SelfOrganizedMap(epochs,alphaEtta,alphaSigma,n,m1,m2, intervalInit, intervalEnd)
    kohonenMap.training(learningVectors)

    #3.1) Clean visual Matrix relative boxes positions
    #kohonenMap.clearMatrixBoxesPositions()

    #4) Activate
    kohonenMap.test(activationVectors, m1, m2)

    #5) See results
    print 'resultMatrix: ' + str(kohonenMap.matrix)

def getLearningVectors():

    learningSetVectors = []

    vector1 = [1]
    vector2 = [2]
    vector3 = [3]
    vector4 = [4]
    vector5 = [5]
    vector6 = [6]
    vector7 = [7]
    vector8 = [8]
    vector9 = [9]
    vector10 = [10]
    vector11 = [11]
    vector12 = [12]
    vector13 = [13]
    vector14 = [14]
    vector15 = [15]
    vector16 = [16]
    vector17 = [17]
    vector18 = [18]
    vector19 = [19]
    vector20 = [20]
    vector21 = [21]
    vector22 = [22]
    vector23 = [23]
    vector24 = [24]
    vector25 = [25]

    learningSetVectors.append(vector1)
    learningSetVectors.append(vector2)
    learningSetVectors.append(vector3)
    learningSetVectors.append(vector4)
    learningSetVectors.append(vector5)
    learningSetVectors.append(vector6)
    learningSetVectors.append(vector7)
    learningSetVectors.append(vector8)
    learningSetVectors.append(vector9)
    learningSetVectors.append(vector10)
    '''
    learningSetVectors.append(vector11)
    learningSetVectors.append(vector12)
    learningSetVectors.append(vector13)
    learningSetVectors.append(vector14)
    learningSetVectors.append(vector15)
    learningSetVectors.append(vector16)
    learningSetVectors.append(vector17)
    learningSetVectors.append(vector18)
    learningSetVectors.append(vector19)
    learningSetVectors.append(vector20)
    learningSetVectors.append(vector21)
    learningSetVectors.append(vector22)
    learningSetVectors.append(vector23)
    learningSetVectors.append(vector24)
    learningSetVectors.append(vector25)
    '''


    return learningSetVectors

if __name__ == "__main__":
    main()
