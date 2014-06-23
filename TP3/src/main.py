import numpy as np
from Hopefield import Hopefield
from DataSetCreator import DataSetCreator
import Hamming

def main():

    #Initialize
    n = 20
    #n = 6
    amountOfMemories = 3
    amountOfVectors = 1000
    hopfield = Hopefield(n)


    print '-----------------------------------------------------------'
    print 'Dimension: ' + str(n)
    #DataSet learning generation
    learningSetVectors = getFixedLearningVector()

    dataSetCreator = DataSetCreator(n)
    #learningSetVectors = dataSetCreator.getLearningVectorsHopfield(amountOfMemories, 90)

    #showVectors('Learning vectors:',learningSetVectors)
    showOrtogonality(learningSetVectors)

    #Learning
    hopfield.training(learningSetVectors)
    #print 'Matrix after:'
    #print hopfield.matrix


    #----------------------------------------------
    #DataSet Generation
    #dataSetCreator = DataSetCreator(n)

    #activationSetVectors = dataSetCreator.getRandomDataSetOfVectors(amountOfVectors, -1, 1, DataSetCreator.UNIFORM)
    #activationSetVectors =  getModifiedLearningVector()
    activationSetVectors =  learningSetVectors
    #activationSetVectors = getEstadoEspurios(learningSetVectors)
    #showVectors('Estados espurios',estadosEspurios)

    #showVectors('ActivationVectors', activationSetVectors)
    #showOrtogonality(activationSetVectors)

    #Activation
    print 'Activation step:'
    hammingVector = []
    hammingLearningActivation = []
    hammingActivationResult = []
    estadosEspurios = 0
    estadosEspuriosVector = []
    estadosPatrones = 0
    espuriosTotal = 0
    i = 0
    for it in activationSetVectors:
        s = hopfield.activate(it,True)
        #print 's: ' + str(s[0])
        #print 'learningSetVectors[0]: ' + str(learningSetVectors)
        if any((s == e).all() for e in learningSetVectors):
            estadosPatrones += 1
        else:
            if any((s == e).all() for e in estadosEspuriosVector):
                espuriosTotal += 1
            else:
                estadosEspurios += 1
                espuriosTotal += 1
                estadosEspuriosVector.append(s)

        #print str(i) + ') ' + str((it == s).all())
        #print 'Vector ingresado: ' + str(it)
        #print 'Vector resultado: ' + str(s)
        hammingDistance = Hamming.distance(it[0],s[0]);
        hammingDistance = Hamming.distance(learningSetVectors[i][0],s[0]);
        hammingVector.append(hammingDistance)

        hammingDistanceLearningActivation = Hamming.distance(learningSetVectors[i][0],activationSetVectors[i][0]);
        hammingLearningActivation.append(hammingDistanceLearningActivation)

        hammingDistanceActivationResult = Hamming.distance(activationSetVectors[i][0],s[0]);
        hammingActivationResult.append(hammingDistanceActivationResult)
        print 'Distance: ' + str(hammingDistance);
        i += 1

    print 'Total: ' + str(len(activationSetVectors))
    print 'Patrones: ' + str(estadosPatrones)
    print 'Espurios: ' + str(estadosEspurios)
    print 'EspuriosTotal: ' + str(espuriosTotal)
    print "EstadosEspurios: " + str(estadosEspuriosVector)
    print 'Hamming distances learning-result: ' + str(hammingVector)
    print 'Hamming distances learning-activation: ' + str(hammingLearningActivation)
    print 'Hamming distances activation-result: ' + str(hammingActivationResult)





def showVectors(title, dataSetVectors):
    print title
    i = 0
    for it in dataSetVectors:
        print str(i+1) + ') ' + str(it)
        i += 1

def showOrtogonality(dataSetVectors):

    #print 'Ortogonalidad 1-2: ' + str(vector1 * np.transpose(vector2))
    dimension = len(dataSetVectors[0][0])
    #print 'dimension: ' + str(dimension)
    vectorOrtogonality = []
    vectorOrtogonalityPercentage = []
    ortogonalityAcum = 0
    i = 0
    for i in range(0, len(dataSetVectors)):
        for j in range(0, len(dataSetVectors)):
            if i < j :
                ortogonalValueInMatrix = np.dot(dataSetVectors[i], np.transpose(dataSetVectors[j]));
                ortogonalValue = ortogonalValueInMatrix[0][0]
                vectorOrtogonality.append(ortogonalValue)
                ortogonalityPercentage = 100.0 - (100.0 / (dimension) * abs(ortogonalValue))

                #print 'ortogonalityPercentageVector: ' + str(ortogonalityPercentage)
                vectorOrtogonalityPercentage.append(ortogonalityPercentage)
                ortogonalityAcum += ortogonalityPercentage
                #print 'Ortogonalidad: ' + str(i+1) + '-' + str(j+1) + ': ' + str(np.dot(dataSetVectors[i], np.transpose(dataSetVectors[j])))

    #print 'Valores de Ortogonalidad: ' + str(vectorOrtogonality)
    #print 'OrtoginalityPercentageVector: ' + str(vectorOrtogonalityPercentage)

    if ortogonalityAcum == 0:
        print '% de Ortogonalidad: ' + str(ortogonalityAcum)
    else:
        print '% de Ortogonalidad: ' + str(ortogonalityAcum / len(vectorOrtogonalityPercentage))

def getFixedLearningVector():

    learningSetVectors = []
    vector1 = np.array([[ 1.,-1,  1.,  1, -1, -1,  1,  1,  1, -1,  1,  1, -1,  1,  1,  1,  1,  1, -1,  1]])
    vector2 = np.array([[ 1., 1, -1.,  1,  1,  1,  1,  1, -1,  1,  1, -1,  1, -1,  1,  1,  1,  1,  1,  1]])
    vector3 = np.array([[ 1., -1, 1., -1, -1,  1,  1, -1, -1,  1,  1,  1, -1, -1, -1,  1, -1,  1,  1, -1]])

    #print 'Learning hamming distance:' + str(Hamming.distance(vector1[0], vector2[0]))
    #print 'Learning hamming distance:' + str(Hamming.distance(vector2[0], vector3[0]))
    #print 'Learning hamming distance:' + str(Hamming.distance(vector3[0], vector1[0]))

    learningSetVectors.append(vector1)
    learningSetVectors.append(vector2)
    learningSetVectors.append(vector3)

    return learningSetVectors


def getModifiedLearningVector():

    learningSetVectors = []

    vector1 = np.array([[ 1.,-1,  1.,  1, -1, 1,  1,  1,  1, 1,  1,  1, 1,  1,  1,  1,  1,  1, -1,  -1]])
    vector2 = np.array([[ 1., 1, -1.,  1,  1,  -1,  -1,  1, -1,  -1,  1, -1,  1, 1,  1,  1,  1,  1,  1,  1]])
    vector3 = np.array([[ 1., 1, 1., 1, -1,  1,  1, -1, -1,  1,  -1,  1, -1, 1, -1,  1, -1,  1,  1, -1]])

    learningSetVectors.append(vector1)
    learningSetVectors.append(vector2)
    learningSetVectors.append(vector3)

    return learningSetVectors


def getEstadoEspurios(learningSetVectors):
    estadoEspurioSetVectors = []

    #vector1 = np.array([[ 1.,-1,  1.,  1, -1, -1,  1,  1,  1, -1,  1,  1, -1,  1,  1,  1,  1,  1, -1,  1]])
    #vector2 = np.array([[ 1., 1, -1.,  1,  1,  1,  1,  1, -1,  1,  1, -1,  1, -1,  1,  1,  1,  1,  1,  1]])
    #vector3 = np.array([[ 1., -1, 1., -1, -1,  1,  1, -1, -1,  1,  1,  1, -1, -1, -1,  1, -1,  1,  1, -1]])

    #vector1 = np.array([[ 1.,-1, 1., 1, -1, 1,  1,  1,  -1, 1,  1,  1, -1,  -1,  1,  1,  1,  1, 1,  1]])
    #vector2 = np.array([[1, 1, 1,  1,  -1, 1,  1,  1,  -1, 1,  1,  1, -1, -1,  -1, 1,  1,  1,  1,  1]])
    #vector3 = np.array([[1, -1, 1,  -1,  -1, 1,  1,  1,  -1, 1,  1,  1, -1, 1,  1, 1,  1,  1,  1,  1]])

    vector1 = np.array( [[ -1, 1, -1,  1,  1,  1, -1,  1, -1,  1, -1, -1,  1, -1,  1, -1, 1, -1,  1, 1]])
    vector2 = np.array([[ -1,  1, -1, 1,  1,  1,  -1, 1, -1,  1,  -1,  -1, 1,  -1, 1,  -1, 1, -1,  1, 1]])
    vector3 = np.array([[ -1,  1, -1, 1,  1,  1,  -1, 1, -1,  1,  -1,  -1, 1,  -1, 1,  -1, 1, -1,  1, 1]])

    estadoEspurioSetVectors.append(vector1)
    estadoEspurioSetVectors.append(vector2)
    estadoEspurioSetVectors.append(vector3)

    return estadoEspurioSetVectors





if __name__ == "__main__":
    main()
