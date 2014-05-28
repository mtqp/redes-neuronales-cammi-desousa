import sys
import numpy as np
import math
from DataSetCreator import DataSetCreator
from pprint import pprint
import time
from HebbianLearning import HebbianLearning
from conditions.EpochAmountCondition import EpochAmountCondition
from MatrixVisualizer import MatrixVisualizer
import time
from SelfOrganizedMap import SelfOrganizedMap

def main():

    #Parameters
    epochs = 100
    alphaEtta = 3
    alphaSigma = 5
    n = 1     #debe coincidir con la longitud del vector x
    m1 = 4
    m2 = 5

    vectorDimension = n
    amountOfVectors = 30
    randomIntegerFromZeroTo = 0.1

    #1) Generar los datos aleatorios Uniformes
    dataSetCreator = DataSetCreator(vectorDimension)

    #2) Guardarlos
    vectorsDataSet = dataSetCreator.getRandomDataSetOfVectors(amountOfVectors, -randomIntegerFromZeroTo, randomIntegerFromZeroTo,
                                                              DataSetCreator.UNIFORM)

    #vectorsDataSet = [[1,2],[1,2],[1,2]]
    print "Vector data set " + str(vectorsDataSet)

    #3) Invocar el aprendizaje de la matrix
    map = SelfOrganizedMap(epochs,alphaEtta,alphaSigma,n,m1,m2)
    map.algorithm(vectorsDataSet)

    #4) Generar datos aleatorios normales
    #vectorsDataSetTesteo = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[0]]
    vectorsDataSetTesteo = dataSetCreator.getRandomDataSetOfVectors(100, -randomIntegerFromZeroTo, randomIntegerFromZeroTo,
                                                              DataSetCreator.UNIFORM)

    print 'vectorsDataSetTesteo: ' + str(vectorsDataSetTesteo)

    #5) Invocar la aproximacion con la matriz
    map.test(vectorsDataSetTesteo)




    #Guardar resultados.
        # Activacion de cada neurona
        #

    '''
    #Grafico de la matrixGausiana
    map = SelfOrganizedMap(1,1,1,1,10,7)
    gaussMatrix = map.proxy((4,4))
    visualizer = MatrixVisualizer(10,7)
    visualizer.visualize(gaussMatrix)
    '''

if __name__ == "__main__":
    main()
