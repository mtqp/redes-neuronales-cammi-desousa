import numpy as np
import itertools as itertools
from Hopefield import Hopefield
from DataSetCreator import DataSetCreator
import Hamming

def main():

    #Initialize
    n = 9
    #n = 6
    amountOfMemories = 5
    amountOfVectors = 10
    hopfield = Hopefield(n)


    print '-----------------------------------------------------------'
    print 'Dimension: ' + str(n)
    #DataSet learning generation
    #learningSetVectors = getFixedLearningVector()
    #learningSetVectors = getDecimalesVector()

    dataSetCreator = DataSetCreator(n)
    learningSetVectors = dataSetCreator.getLearningVectorsHopfield(amountOfMemories, 40)

    showVectors('Learning vectors:',learningSetVectors)
    showOrtogonality(learningSetVectors)

    #Learning
    hopfield.training(learningSetVectors)
    #print 'Matrix after:'
    #print hopfield.matrix



    #----------------------------------------------
    #DataSet Generation
    dataSetCreator = DataSetCreator(n)

    #activationSetVectors = dataSetCreator.getRandomDataSetOfVectors(amountOfVectors, -1, 1, DataSetCreator.UNIFORM, True)
    #activationSetVectors =  getModifiedLearningVector();
    #activationSetVectors = getEstadoEspurios(learningSetVectors)
    #activationSetVectors = getDecimalesVector()
    activationSetVectors = binaryGeneration(n)
    #showVectors('Estados espurios',estadosEspurios)

    #showVectors('ActivationVectors', activationSetVectors)
    showOrtogonality(activationSetVectors)

    #Activation
    print 'Activation step:'
    hammingVector = []
    hammingLearningActivation = []
    hammingActivationResult = []
    estadosEspurios = 0
    estadosEspuriosVector = []
    estadosPatrones = 0
    espuriosTotal = 0
    syncronic = False

    if syncronic:
        print 'Mode: Synchronic (bad)'
    else:
        print 'Mode: Asynchronic (good)'


    #activationSetVectors.append(getDecimalesModificados())


    i = 0
    for it in activationSetVectors:
        #print 'activando vector ' + str(it)
        s = hopfield.activate(it,syncronic)
        #print 's: ' + str(s[0])
        #print 'learningSetVectors[0]: ' + str(learningSetVectors)
        if any((s == e).all() for e in learningSetVectors):
            estadosPatrones += 1
            print 'patron:' + str(i)
        else:
            if any((s == e).all() for e in estadosEspuriosVector):
                espuriosTotal += 1

            else:
                #print 'vector:' + str(i)
                estadosEspurios += 1
                espuriosTotal += 1
                estadosEspuriosVector.append(s)

        #print str(i) + ') ' + str((it == s).all())
        #print 'Vector ingresado: ' + str(it)
        #print 'Vector resultado: ' + str(s)
        #hammingDistance = Hamming.distance(it[0],s[0]);
        #hammingDistance = Hamming.distance(learningSetVectors[i][0],s[0]);
        #hammingVector.append(hammingDistance)

        #hammingDistanceLearningActivation = Hamming.distance(learningSetVectors[i][0],activationSetVectors[i][0]);
        #hammingLearningActivation.append(hammingDistanceLearningActivation)

        #hammingDistanceActivationResult = Hamming.distance(activationSetVectors[i][0],s[0]);
        #hammingActivationResult.append(hammingDistanceActivationResult)
        #print 'Distance: ' + str(hammingDistance);
        i += 1
        #print '---'

    print 'Total: ' + str(len(activationSetVectors))
    print 'Patrones: ' + str(estadosPatrones)
    print 'Espurios: ' + str(estadosEspurios)
    print 'EspuriosTotal: ' + str(espuriosTotal)
    #print "EstadosEspurios: " + str(estadosEspuriosVector)
    print 'Hamming distances learning-result: ' + str(hammingVector)
    print 'Hamming distances learning-activation: ' + str(hammingLearningActivation)
    print 'Hamming distances activation-result: ' + str(hammingActivationResult)

    #print 'estadosEspuriosVector' + str(estadosEspuriosVector)

    #for i in range(0, len(estadosEspuriosVector)):
    #    printLetterWithDimension('EstadosEspurio ' + str(i),16, estadosEspuriosVector[i].flatten())

def binaryGeneration(n):
    print "---binaryGeneration for " + str(n)
    permutationTuplas = list(itertools.product(*[(0, 1)] * n))

    permutationList = []

    for tupla in permutationTuplas:
        auxList = []
        auxList.append(list(tupla))
        permutationList.append(np.array(auxList))

    print permutationList

    return permutationList

def showVectors(title, dataSetVectors):
    print title
    i = 0
    for it in dataSetVectors:
        print str(i+1) + ') ' + str(it)
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
                #print str(i) + 'leng:' + str(len(dataSetVectors[i][0]))
                #print str(j) + 'leng:' + str(len(dataSetVectors[j][0]))
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
    #Ortogonalidad 100%
    vector1 = np.array([[ 1.,-1,  1.,  1, -1, -1,  1,  1,  1, -1,  1,  1, -1,  1,  1,  1,  1,  1, -1,  1]])
    vector2 = np.array([[ 1., 1, -1.,  1,  1,  1,  1,  1, -1,  1,  1, -1,  1, -1,  1,  1,  1,  1,  1,  1]])
    vector3 = np.array([[ 1., -1, 1., -1, -1,  1,  1, -1, -1,  1,  1,  1, -1, -1, -1,  1, -1,  1,  1, -1]])

    #Ortogonalidad 86%
    #vector1 = np.array([[ 1.,1,  1.,  1, 1, 1,  -1,  -1,  -1, -1,  -1,  -1, 1,  -1,  -1,  -1,  -1,  -1, -1,  -1]])
    #vector2 = np.array([[ 1.,-1,  1.,  -1, 1, 1,  -1,  -1,  -1, -1,  -1, 1, -1,  -1,  -1,  -1,  -1,  -1, -1,  -1]])
    #vector3 = np.array([[ 1.,1,  1.,  1, 1, 1,  -1,  -1,  -1, 1,  -1,  -1, -1,  -1,  -1,  -1,  -1,  -1, -1,  -1]])

    learningSetVectors.append(vector1)
    learningSetVectors.append(vector2)
    learningSetVectors.append(vector3)

    return learningSetVectors


def getModifiedLearningVector():

    learningSetVectors = []

    #vector1 = np.array([[ 1.,-1,  1.,  1, -1, -1,  1,  1,  1, -1,  1,  1, -1,  1,  1,  1,  1,  1, -1,  1]])
    #vector2 = np.array([[ 1., 1, -1.,  1,  1,  1,  1,  1, -1,  1,  1, -1,  1, -1,  1,  1,  1,  1,  1,  1]])
    #vector3 = np.array([[ 1., -1, 1., -1, -1,  1,  1, -1, -1,  1,  1,  1, -1, -1, -1,  1, -1,  1,  1, -1]])

    #dos bits
    #vector1 = np.array([[ 1., -1.,  1.,  1., -1., 1.,  1.,  1.,  1., 1.,  1.,  1., -1.,  1.,  1.,  1.,  1.,  1.,  -1.,  1.,]])
    #vector2 = np.array([[ 1.,  1., 1.,  1.,  1.,  1.,  1.,  1., -1.,  -1.,  1., -1.,  1., -1.,  1.,  1.,  1.,  1.,   1.,  1.,]])
    #vector3 = np.array([[ 1., -1.,  1., -1., -1.,  1.,  1., -1., -1.,  1.,  1.,  1., -1., 1., -1.,  1., -1.,  1.,  1., -1.,]])

    #tres bits
    #vector1 = np.array([[ 1., -1.,  1.,  1., -1., 1.,  1.,  1.,  1., 1.,  1.,  1., 1.,  1.,  1.,  1.,  1.,  1.,  -1.,  -1.,]])
    #vector2 = np.array([[ 1.,  1., -1.,  1.,  1.,  -1.,  -1.,  1., -1.,  -1.,  1., -1.,  1., 1.,  1.,  1.,  1.,  1.,   1.,  1.,]])
    #vector3 = np.array([[ 1., 1.,  1., 1., -1.,  1.,  1., -1., -1.,  1.,  -1.,  1., -1., 1., -1.,  1., -1.,  1.,  1., -1.,]])

    #cinco bits
    #vector1 = np.array([[ 1., -1.,  1.,  1., -1., 1.,  -1.,  1.,  1., 1.,  1.,  1., 1.,  1.,  1.,  1.,  1.,  1.,  -1.,  -1.,]])
    #vector2 = np.array([[ 1.,  1., -1.,  1.,  1.,  -1.,  -1.,  -1., -1.,  -1.,  1., -1.,  1., 1.,  1.,  1.,  1.,  1.,   1.,  1.,]])
    #vector3 = np.array([[ 1., 1.,  1., 1., -1.,  -1.,  1., -1., -1.,  1.,  -1.,  1., -1., 1., -1.,  1., -1.,  1.,  1., -1.,]])

    #7 bits
    #vector1 = np.array([[ -1., -1.,  1.,  1., -1., 1.,  -1.,  1.,  1., 1.,  1.,  -1., 1.,  1.,  -1.,  -1.,  1.,  -1.,  -1.,  -1.,]])
    #vector2 = np.array([[ -1.,  1., -1.,  1.,  1.,  -1.,  -1.,  -1., -1.,  -1.,  -1., -1.,  -1., 1.,  1.,  -1.,  1.,  -1.,   1.,  1.,]])
    #vector3 = np.array([[ 1., -1.,  1., 1., -1.,  -1.,  -1., -1., -1.,  1.,  -1.,  1., -1., 1., -1.,  -1., -1.,  -1.,  1., -1.,]])

    vector1 = np.array( [[ 1.,  1., -1., -1.,  1., -1., -1., -1.,  1., -1., -1.,  1., -1.,  1.,  1.,  1., -1.,  1., -1., -1.,]])
    vector2 = np.array( [[-1.,  1., -1.,  1.,  1.,  1., -1., -1.,  1., -1., -1., -1.,  1., -1., -1., -1.,  1.,  1.,  1.,  1.,]])
    vector3 = np.array( [[-1., -1.,  1.,  1.,  1., -1.,  1., -1.,  1., -1., -1., -1., -1.,  1.,  1., -1., -1.,  1.,  1.,  1.,]])


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

    #vector1 = np.array( [[ -1, 1, -1,  1,  1,  1, -1,  1, -1,  1, -1, -1,  1, -1,  1, -1, 1, -1,  1, 1]])
    #vector2 = np.array([[ -1,  1, -1, 1,  1,  1,  -1, 1, -1,  1,  -1,  -1, 1,  -1, 1,  -1, 1, -1,  1, 1]])
    #vector3 = np.array([[ -1,  1, -1, 1,  1,  1,  -1, 1, -1,  1,  -1,  -1, 1,  -1, 1,  -1, 1, -1,  1, 1]])

    vector1 = np.array( [[ -1, 1, -1,  1,  1,  1, -1,  1, -1,  1, -1, -1,  1, -1,  1, -1, 1, -1,  -1, 1]])
    vector2 = np.array([[ -1,  1, -1, -1,  1,  -1,  -1, 1, -1,  1,  -1,  -1, 1,  -1, 1,  -1, 1, -1,  1, 1]])
    vector3 = np.array([[ -1,  1, -1, -1,  1,  -1,  -1, 1, -1,  1,  -1,  -1, 1,  -1, 1,  -1, 1, -1,  1, 1]])

    estadoEspurioSetVectors.append(vector1)
    estadoEspurioSetVectors.append(vector2)
    estadoEspurioSetVectors.append(vector3)

    return estadoEspurioSetVectors

def getDecimalesModificados():

    decimalesVector = []

    decimal0 =  np.array([[-1,-1,-1,-1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,1,-1,-1,
                -1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,-1,-1,
                -1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,1,1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                -1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,-1,
                -1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,
                -1,-1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,
                -1,-1,1,1,1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,
                -1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1]])

    #decimalesVector.append(decimal0)
    #return decimalesVector
    return decimal0

# vectores de 16x16 = 256
def getDecimalesVector():

     decimalesVector = []

     decimal0 =  np.array([[-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,
                 -1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,
                 -1,-1,-1,-1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,
                 -1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,
                 -1,-1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,
                 -1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                 -1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                 -1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                 -1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                 -1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                 -1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                 -1,-1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,
                 -1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,
                 -1,-1,-1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,
                 -1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,
                 -1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,-1]])

     decimal1 =  np.array([[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1]])

     decimal2 =  np.array([[-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,-1,
                -1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,-1,
                -1,-1,1,1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,
                -1,-1,1,1,1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,
                -1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,1,-1,-1,
                -1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,
                -1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,
                -1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,
                -1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1]])

     decimal3 =  np.array([[-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,-1,
                            -1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,
                            -1,-1,-1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,-1,
                            -1,-1,-1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,-1,
                            -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,
                            -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,
                            -1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,-1,
                            -1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,-1,
                            -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                            -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,
                            -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,
                            -1,-1,-1,1,1,1,-1,-1,1,1,1,1,1,1,-1,-1,
                            -1,-1,-1,1,1,1,-1,-1,1,1,1,1,1,1,-1,-1,
                            -1,-1,-1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,-1,
                            -1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,
                            -1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,-1]])


     decimal4 = np.array([[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,
                -1,-1,-1,-1,-1,1,1,-1,1,1,1,1,1,-1,-1,-1,
                -1,-1,-1,-1,1,1,-1,-1,1,1,1,1,1,-1,-1,-1,
                -1,-1,-1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,-1,
                -1,-1,-1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,
                -1,-1,1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,
                -1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,
                -1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1]])

     decimal5 = np.array([[-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,
                            -1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,
                            -1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,
                            -1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
                            -1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
                            -1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
                            -1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,
                            -1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,
                            -1,-1,-1,1,1,1,-1,1,1,1,1,1,1,-1,-1,-1,
                            -1,-1,-1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,
                            -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,
                            -1,-1,1,1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,
                            -1,-1,1,1,1,-1,-1,-1,1,1,1,1,1,1,-1,-1,
                            -1,-1,1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,
                            -1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,
                            -1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1]])

     decimal6 = np.array([[-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,
                -1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,-1,
                -1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,
                -1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,
                -1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,
                -1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,
                -1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,
                -1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,
                -1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                -1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                -1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                -1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                -1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                -1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,
                -1,-1,-1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,-1]])

     decimal7 = np.array([[-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,
                -1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,-1,
                -1,-1,-1,1,1,1,-1,-1,-1,-1,-1,1,1,1,-1,-1,
                -1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1]])

     decimal8 = np.array([[-1,-1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,
                            -1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,-1,
                            -1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,-1,
                            -1,-1,-1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,-1,
                            -1,-1,-1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,-1,
                            -1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,-1,-1,-1,
                            -1,-1,-1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,
                            -1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,
                            -1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,-1,
                            -1,-1,-1,1,1,1,-1,1,1,1,1,1,1,1,-1,-1,
                            -1,-1,1,1,1,1,-1,-1,-1,1,1,1,1,1,-1,-1,
                            -1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,
                            -1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,
                            -1,-1,-1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,-1,
                            -1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,-1,
                            -1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,-1]])

     decimal9 = np.array([[-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,
                -1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                -1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                -1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                -1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                -1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,1,-1,-1,
                -1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,
                -1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,
                -1,-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,-1,
                -1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1]])

     decimalesVector.append(decimal0)
     decimalesVector.append(decimal1)
     decimalesVector.append(decimal2)
     decimalesVector.append(decimal3)
     #decimalesVector.append(decimal4)
     #decimalesVector.append(decimal5)
     #decimalesVector.append(decimal6)
     #decimalesVector.append(decimal7)
     #decimalesVector.append(decimal8)
     #decimalesVector.append(decimal9)

     return  decimalesVector



if __name__ == "__main__":
    main()
