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
import random

def main():

    #ejercicio2()
    ejercicio3()

def ejercicio2():
    #Parameters
    epochs = 50
    alphaEtta = 0.7
    alphaSigma = 0.19
    interval = 10
    n = 1     #debe coincidir con la longitud del vector x
    m1 = 10
    m2 = 10
    intervalInit = -0.05
    intervalEnd = 0.05

    vectorDimension = n
    amountOfVectors = 100

    #1) Generar los datos aleatorios Uniformes
    dataSetCreator = DataSetCreator(vectorDimension)

    #2) Guardarlos
    vectorsDataSetLearning = dataSetCreator.getRandomDataSetOfVectors(amountOfVectors, -interval, interval,DataSetCreator.UNIFORM)

    #UNIFORM
    #vectorsDataSetLearning = [[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]
    #vectorsDataSetLearning = [[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]
    random.shuffle(vectorsDataSetLearning)
    #print "Vector desordenado" +  str(vectorsDataSetLearning)
    #time.sleep(10)
    #vectorsDataSetLearning = [[-1],[-1],[-1],[-1],[-1],[-2],[-2],[-2],[-2],[-2],[-3],[-3],[-3],[-3],[-3],[-4],[-4],[-4],[-4],[-4],[-5],[-5],[-5],[-5],[-5],[-6],[-6],[-6],[-6],[-6],[-7],[-7],[-7],[-7],[-7],[-8],[-8],[-8],[-8],[-8],[-9],[-9],[-9],[-9],[-9],[1],[1],[1],[1],[1],[2],[2],[2],[2],[2],[3],[3],[3],[3],[3],[4],[4],[4],[4],[4],[5],[5],[5],[5],[5],[6],[6],[6],[6],[6],[7],[7],[7],[7],[7],[8],[8],[8],[8],[8],[9],[9],[9],[9],[9]]

    #NEGATIVES
    #vectorsDataSetLearning = [[-1],[-1],[-1],[-1],[-1],[-2],[-2],[-2],[-2],[-2],[-3],[-3],[-3],[-3],[-3],[-4],[-4],[-4],[-4],[-4],[-5],[-5],[-5],[-5],[-5],[-6],[-6],[-6],[-6],[-6],[-7],[-7],[-7],[-7],[-7],[-8],[-8],[-8],[-8],[-8],[-9],[-9],[-9],[-9],[-9]]
    #vectorsDataSetLearning = [[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]
    #vectorsDataSetLearning = [[-1],[-2],[-3],[-4],[-5],[-6],[-7],[-8],[-9],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]

    #vectorsDataSetLearning = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[1.5],[2.5],[3.5],[4.5],[5.5],[6.5],[7.5],[8.5],[9.5],[1.7],[2.7],[3.7],[4.7],[5.7],[6.7],[7.7],[8.7],[9.7],[1.2],[2.2],[3.2],[4.2],[5.2],[6.2],[7.2],[8.2],[9.2],[-9.7],[-8.7],[-7.7],[-6.7],[-5.7],[-4.7],[-3.7],[-2.7],[-1.7],[-9.3],[-8.3],[-7.3],[-6.3],[-5.3],[-4.3],[-3.3],[-2.3],[-1.3],[-9.5],[-8.5],[-7.5],[-6.5],[-5.5],[-4.5],[-3.5],[-2.5],[-1.5],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1]]

    #vectorsDataSet = [[1,2],[1,2],[1,2]]
    print "Vectores de aprendizaje " + str(vectorsDataSetLearning)

    #3) Invocar el aprendizaje de la matrix
    map = SelfOrganizedMap(epochs,alphaEtta,alphaSigma,n,m1,m2, intervalInit, intervalEnd)
    #map.matrix = np.matrix('-1 0.5 0 -0.5')
    #map.matrix = np.matrix('-1 0.5 0.4 0 -0.5 0.4 0.7 0.2 0.6')
    #print map.matrix
    map.algorithm(vectorsDataSetLearning)

    #4) Generar datos aleatorios normales
    #vectorsDataSetTesteo = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[0]]

    vectorsDataSetTesteo = dataSetCreator.getRandomDataSetOfVectors(120, -interval, interval,DataSetCreator.UNIFORM)
    #vectorsDataSetTesteo = [[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]
    #vectorsDataSetTesteo = [[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-9]]


    #Uniforme simgle
    #vectorsDataSetTesteo = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
    #vectorsDataSetTesteo = [[-1],[-2],[-3],[-4],[-5],[-6],[-7],[-8],[-9]]
    #vectorsDataSetTesteo = [[-9],[-8],[-7],[-6],[-5],[-4],[-3],[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[-5.7],[-4.2],[6.7]]

    #Uniforme
    #vectorsDataSetTesteo = [[1],[1],[1],[1],[1],[2],[2],[2],[2],[2],[3],[3],[3],[3],[3],[4],[4],[4],[4],[4],[5],[5],[5],[5],[5],[6],[6],[6],[6],[6],[7],[7],[7],[7],[7],[8],[8],[8],[8],[8],[9],[9],[9],[9],[9]]
    #vectorsDataSetTesteo = [[-1],[-1],[-1],[-1],[-1],[-2],[-2],[-2],[-2],[-2],[-3],[-3],[-3],[-3],[-3],[-4],[-4],[-4],[-4],[-4],[-5],[-5],[-5],[-5],[-5],[-6],[-6],[-6],[-6],[-6],[-7],[-7],[-7],[-7],[-7],[-8],[-8],[-8],[-8],[-8],[-9],[-9],[-9],[-9],[-9]]
    #vectorsDataSetTesteo = [[0],[0],[0],[0],[0],[-1],[-1],[-1],[-1],[-1],[-2],[-2],[-2],[-2],[-2],[-3],[-3],[-3],[-3],[-3],[-4],[-4],[-4],[-4],[-4],[-5],[-5],[-5],[-5],[-5],[-6],[-6],[-6],[-6],[-6],[-7],[-7],[-7],[-7],[-7],[-8],[-8],[-8],[-8],[-8],[-9],[-9],[-9],[-9],[-9]]

    #vectorsDataSetTesteo = [[3],[3],[3],[3],[3],[2],[2],[2],[2],[2],[1],[1],[1],[1],[1],[0],[0],[0],[0],[0],[-1],[-1],[-1],[-1],[-1],[-2],[-2],[-2],[-2],[-2],[-3],[-3],[-3],[-3],[-3],[-4],[-4],[-4],[-4],[-4],[-5],[-5],[-5],[-5],[-5],[-6],[-6],[-6],[-6],[-6],[-7],[-7],[-7],[-7],[-7],[-8],[-8],[-8],[-8],[-8],[-9],[-9],[-9],[-9],[-9]]


    #Progresivo
    #vectorsDataSetTesteo = [[1],[2],[2],[3],[3],[3],[4],[4],[4],[4],[5],[5],[5],[5],[5],[6],[6],[6],[6],[6],[6],[7],[7],[7],[7],[7],[7],[7],[8],[8],[8],[8],[8],[8],[8],[8],[9],[9],[9],[9],[9],[9],[9],[9],[9]]
    #vectorsDataSetTesteo = [[-1],[-2],[-2],[-3],[-3],[-3],[-4],[-4],[-4],[-4],[-5],[-5],[-5],[-5],[-5],[-6],[-6],[-6],[-6],[-6],[-6],[-7],[-7],[-7],[-7],[-7],[-7],[-7],[-8],[-8],[-8],[-8],[-8],[-8],[-8],[-8],[-9],[-9],[-9],[-9],[-9],[-9],[-9],[-9],[-9]]


    #Se jode
    #vectorsDataSetTesteo = [[-1],[-2],[-2],[-3],[-3],[-3],[-4],[-4],[-4],[-4],[-5],[-5],[-5],[-5],[-5],[-6],[-6],[-6],[-6],[-6],[-6],[-7],[-7],[-7],[-7],[-7],[-7],[-7],[-8],[-8],[-8],[-8],[-8],[-8],[-8],[-8],[-9],[-9],[-9],[-9],[-9],[-9],[-9],[-9],[-9]]

    print 'Vectores de testeo: ' + str(vectorsDataSetTesteo)
    map.seeResult()

    #5) Invocar la aproximacion con la matriz
    map.test(vectorsDataSetTesteo, m1, m2)




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

def ejercicio3():
    #Parameters
    epochs = 50
    alphaEtta = 0.13
    alphaSigma = 0.95
    interval = 10
    n = 2     #debe coincidir con la longitud del vector x
    m1 = 5
    m2 = 5
    intervalInit = -0.5
    intervalEnd = 0.5
    vectorDimension = n
    amountOfVectors = 200

    firstBoundX1 = 1
    endBoundX1 = 5
    firstBoundX2 = 10
    endBoundX2 = 15

    #1) Generar los datos aleatorios Uniformes aprendizaje
    dataSetCreator = DataSetCreator(vectorDimension)

    #2) Guardarlos
    vectorsDataSetLearning = dataSetCreator.getRandomDataSetOfVectorsBidimensional(amountOfVectors, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)

    random.shuffle(vectorsDataSetLearning)
    print "Vectores de aprendizaje " + str(vectorsDataSetLearning)

    #3) Invocar el aprendizaje de la matrix
    map = SelfOrganizedMap(epochs,alphaEtta,alphaSigma,n,m1,m2, intervalInit, intervalEnd)
    map.algorithm(vectorsDataSetLearning)

    #4) Generar datos aleatorios Uniformes Testeo
    #vectorsDataSetTesteo = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[0]]

    vectorsDataSetTesteo = dataSetCreator.getRandomDataSetOfVectorsBidimensional2(amountOfVectors, 6,9,16,20)
    #vectorsDataSetTesteo = vectorsDataSetLearning
    #print 'Vectores de testeo: ' + str(vectorsDataSetTesteo)
    map.seeResult()

    vectorsDataSetLearning = vectorsDataSetLearning + vectorsDataSetTesteo
    print 'Vectores de aprendizaje + testeo: ' + str(vectorsDataSetLearning)

    #5) Invocar la aproximacion con la matriz
    map.test(vectorsDataSetLearning, m1, m2, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)

    vTest = MatrixVisualizer(m1,m2)
    vTest.visualizePlotAxis(vectorsDataSetLearning, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)

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
