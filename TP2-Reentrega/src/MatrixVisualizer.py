from numpy.lib.financial import rate
from visual import *
import numpy as np
import math
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time
from mpl_toolkits.axes_grid.axislines import SubplotZero
import matplotlib.pyplot as plt
from visual.graph import * #
#from pylab import *


class MatrixVisualizer:
    def __init__(self, nDimension, mDimension):
        self.n = nDimension
        self.m = mDimension
        self.boxes = self.createMatrixBoxes(nDimension, mDimension)
        #self.referenceBoxes = self.createReferenceBoxes(1, nDimension*mDimension)
        self.referenceIndex = 0
        currentDisplay = display.get_selected()
        currentDisplay.background = color.white
        self.backgroundColor = currentDisplay.background
        self.matrixAcumBoxes = np.zeros((nDimension,mDimension))
        self.showLabel = True
        self.labels = []

    def initializeMatrixBoxesWithBackgroundColor(self):
        self.initializeMatrixBoxesWithColor(self.n,self.m, color.white)

    def visualize(self, matrix):
        scene.center = vector(3,2,-1)
        #scene.forward = vector(0,20,10)
        rate(100)
        time.sleep(0.01)
        for columnIndex in range(0, self.n):
            for rowIndex in range(0, self.m):
                matrixValue = matrix[columnIndex][rowIndex]
                boxItem = self.boxes[columnIndex][rowIndex]
                boxItem.color =  color.rgb_to_hsv(self.createVectorForValue(matrixValue))
                boxItem.size = (0.5, 0.5, 1*abs(matrixValue))

    def hideLabel(self):
        self.showLabel = False

    def visualizeWithParams(self, matrix, n, m, initialPosition):
        #scene.center = vector(3,2,-1)
        #scene.forward = vector(0,20,10)

        print 'visualizeWithParams - matrixValue: ' + str(matrix)
        rate(100)
        time.sleep(0.01)

        print 'n: ' + str(n)
        print 'm: ' + str(m)
        #self.boxes = self.createMatrixBoxes(n, m)

        xInitial = initialPosition[0]
        yInitial = initialPosition[1]
        #extraer la initialPosition y sumarla a las columIndes y rowIndex.

        for columnIndex in range(0, n):
            for rowIndex in range(0, m):
                matrixValue = matrix[columnIndex, rowIndex]
                boxItem = self.boxes[columnIndex+xInitial][rowIndex+yInitial]
                boxItem.color =  color.rgb_to_hsv(self.createVectorForValue(matrixValue))
                boxItem.size = (0.5, 0.5, 1*abs(matrixValue))

    def visualizeWinnerMatrix(self, matrix, n, m, initialPosition):
        #scene.center = vector(3,2,-1)
        #scene.forward =  vector(0,20,10)
        rate(100)
        time.sleep(0.01)
        for columnIndex in range(0, n):
            for rowIndex in range(0, m):
                matrixValue = matrix[columnIndex][rowIndex]
                boxItem = self.boxes[columnIndex][rowIndex]

                if(matrixValue == 1):
                    boxItem.color = color.red
                else:
                    boxItem.color = color.green

                boxItem.size = (0.5, 0.5, 0)

    def createVectorForValue(self, aValue): #por precondicion se supone que los valores estan en [0,1]
        aValue = abs(aValue)
        return (aValue, aValue, aValue)

    #red= (1,0,0)
    #green= (0,1,0)
    def createVectorForValue2(self, aValue):
        posAValue = abs(aValue)
        topValue = 10

        if(posAValue > topValue):
            firstComponent = 1
            secondComponent = 0
        else:
            firstComponent = posAValue/topValue
            secondComponent = (topValue - posAValue)/topValue

        #print 'Color: ' + str((firstComponent, secondComponent, 0))
        return (firstComponent,secondComponent, 0)

    def createMatrixBoxes(self, n, m):
        matrix = []

        for columnIndex in range(0, n):
            row = []
            for rowIndex in range(0, m):
                #row.append(box(pos=(columnIndex, rowIndex, 0), size=(0.4, 0.4, 0.4), color=color.rgb_to_hsv((columnIndex*3, rowIndex*5, 10))))
                row.append(box(pos=(columnIndex, rowIndex, 0), size=(0.4, 0.4, 0), color=color.white))
            matrix.append(row)
        return matrix

    def createReferenceBoxes(self, n, m):
        matrix = []

        for columnIndex in range(0, n):
            row = []
            count = 0
            for rowIndex in range(0, m):
                count = count + 0.4
                #row.append(box(pos=(columnIndex, rowIndex, 0), size=(0.4, 0.4, 0.4), color=color.rgb_to_hsv((columnIndex*3, rowIndex*5, 10))))

                row.append(box(pos=(columnIndex+10, count, 0), size=(0.4, 0.4, 0), color=color.white))
                print 'x: ' + str(columnIndex+m*1.5)
                print 'x: ' + str(rowIndex - rowIndex/2)
            matrix.append(row)
        return matrix

    def initializeMatrixBoxesWithColor(self, n, m, acolor):
        matrix = []

        for columnIndex in range(0, n):
            row = []
            for rowIndex in range(0, m):
                row.append(box(pos=(columnIndex, rowIndex, 0), size=(0.4, 0.4, 0.4), color=acolor))
            matrix.append(row)
        return matrix

    def plot2d(self, matrix):
        plt.imshow(matrix, interpolation="none", cmap=cm.gray )
        plt.colorbar()
        plt.show()
        plt.ylim([20,0])

    def plotAxis(self, matrix):
        #funct = gvbars(delta=0.05, color=color.blue)
        #for i in range(0, len(matrix[0])):
        #    funct.plot(pos=(0,matrix[0][i]))

        #pylab.scatter(3,4, s=100 ,marker='o', c=color.green)
        #pylab.show()

        fig = plt.figure(1)
        ax = SubplotZero(fig, 111)
        fig.add_subplot(ax)
        flattenMatrix = np.transpose(matrix).flatten()
        x = np.linspace(0., 10., len(flattenMatrix))
        print 'x ' + str(x)
        print 'matrix: ' + str(np.transpose(matrix).flatten())
        #ax.plot(x, np.sin(x*np.pi), linewidth=2.0)
        ax.plot(matrix, 0, linewidth=2.0)
        plt.show()

    def visualizePlotAxis2(self, listOfVectors):

        f1 = gdots(color=color.cyan, background=color.white) # a graphics curve

        #[[1,2],[3,4],[5,6]]
        for i in range (0,len(listOfVectors)):
            arra0 = []
            arra1 = []

            vector = listOfVectors[i]
            arra0.append(vector[0])
            arra1.append(vector[1])

            #plt.plot(arra0, arra1)

            f1.plot(pos=(vector[0],vector[1])) # add a single point
        plt.show()

    def visualizeZones(self, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2):

        array1 = []
        array1.append(firstBoundX1)
        array1.append(endBoundX1)
        array1.append(endBoundX1)

        array2 = []
        array2.append(firstBoundX1)
        array2.append(firstBoundX1)
        array2.append(endBoundX1)


        #plt.plot(array1,array2)
        #plt.plot([1,5],[1,1])
        plt.plot([1,5],[1,5])

        plt.show()

    def visualizePlotAxis(self, listOfVectors, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2):

        for i in range (0,len(listOfVectors)):
            vector = listOfVectors[i]

            x = vector[0]
            y = vector[1]

            zone = self.whichZoneBelongs(vector, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)

            #colorRGB = (random.uniform(0,1),random.uniform(0,1) ,random.uniform(0,1) )
            colorRGB = color.black

            if(zone ==  1):
                colorRGB = color.blue

            if(zone ==  2):
                colorRGB = color.green

            if(zone ==  3):
                colorRGB = color.red

            if(zone ==  4):
                colorRGB = color.yellow

            plt.scatter(x,y, s=20, color=colorRGB)
        plt.show()

    def plotHistogram(self, vector):

        #mu, sigma = 100, 15
        #x = mu + sigma * np.random.randn(10000)
        #print x
        hist, bins = np.histogram(vector, bins=20)
        width = 0.7 * (bins[1] - bins[0])
        center = (bins[:-1] + bins[1:]) / 2
        plt.bar(center, hist, align='center', width=width)
        plt.show()

    def visualizeCovariance(self, matrix):
        covarianceMatrix = np.cov(matrix)
        self.visualize(covarianceMatrix)

    def visualizeNeuralMaximums(self, neuralMaximumsMatrix):

        scene.center = vector(3,2,-1)
        #scene.forward =  vector(0,0,1)

        for i in range (0, neuralMaximumsMatrix.shape[0]):
            for j in range (0, neuralMaximumsMatrix.shape[1]):
                box = self.boxes[i][j]

                if(neuralMaximumsMatrix[i][j] != 0):
                    #box.pos[2] = neuralMaximumsMatrix[i][j]

                    print '-------------'
                    print 'maximum value: ' + str(neuralMaximumsMatrix[i][j])

                    print 'box size prev: (' + str(box.size[0]) + ',' + str(box.size[1]) + ',' + str(box.size[2])  + ')'
                    print 'box position prev: (' + str(box.pos[0]) + ',' + str(box.pos[1]) + ',' + str(box.pos[2])  + ')'


                    if(neuralMaximumsMatrix[i][j] >= 0):
                        box.size = (box.size[0],box.size[1],neuralMaximumsMatrix[i][j])
                        box.pos[2] = box.pos[2] + (neuralMaximumsMatrix[i][j]/2.0)
                    else:
                        print 'negative'
                        box.size = (box.size[0],box.size[1],-neuralMaximumsMatrix[i][j])
                        box.pos[2] = box.pos[2] + (neuralMaximumsMatrix[i][j]/2.0)

                    #box.size[2] = neuralMaximumsMatrix[i][j]*10
                    #box.size[1] = neuralMaximumsMatrix[i][j]*10
                    #box.size[1] = neuralMaximumsMatrix[i][j]*10
                    box.color = color.blue
                    print 'box size post: (' + str(box.size[0]) + ',' + str(box.size[1]) + ',' + str(box.size[2])  + ')'
                    print 'box position post: (' + str(box.pos[0]) + ',' + str(box.pos[1]) + ',' + str(box.pos[2])  + ')'
                    print '-------------'

                    if(self.showLabel):
                        aLabel = label(pos=(box.pos[0],box.pos[1],box.pos[2]), text=str(round(neuralMaximumsMatrix[i][j],2)), color=color.white, opacity=0, border=0, box = False)
                        self.labels.append(aLabel)
                #box.color = color.blue

    def visualizeNeuralPointsBidimensionalOnline(self, winnerPoint, inputValue, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2):

        scene.center = vector(3,2,-1)
        #scene.forward =  vector(0,0,1)
        rate(100)
        time.sleep(0.01)

        posX = winnerPoint[0]
        posY = winnerPoint[1]


        desvio = self.matrixAcumBoxes[posX, posY]
        posZ = desvio

        referenceBox = self.boxes[posX][posY]

        #print 'graficando box (' + str(posX) + ',' + str(posY) + ',' + str(posZ) + ')';

        valueAbs = abs(inputValue[0])

        valueZeroOne = 0
        if(valueAbs == inputValue[0]):
            valueZeroOne = valueAbs/10.0
        else:
            valueZeroOne = valueAbs*2/10.0

        zone = self.whichZoneBelongs(inputValue, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)
        #print 'belogns to zone: ' + str(zone)
        #zone = color.black

        commonSize = 0.7

        #colorRGB = (random.uniform(0,1),random.uniform(0,1) ,random.uniform(0,1) )
        colorRGB = color.black

        if(zone ==  1):
            colorRGB = color.blue

        if(zone ==  2):
            colorRGB = color.green

        if(zone ==  3):
            colorRGB = color.red

        if(zone ==  4):
            colorRGB = color.yellow

        #box(pos=(posX, posY, posZ), size=(0.4, 0.4, 0.4), color=color.red)
        #box(pos=(posX, posY, posZ), size=(0.4, 0.4, 0.4), color=color.rgb_to_hsv(colorRGB))
        #box(pos=(posX, posY, posZ), size=(commonSize, commonSize, commonSize), color=colorRGB)

        if(self.showLabel):
            texto = '(' + str(round(inputValue[0],2)) + ',' +  str(round(inputValue[1],2)) + ')'

            aLabel = label(pos=(posX,posY,posZ), text=texto, color=color.white, opacity=0, border=0, box = False)
            self.labels.append(aLabel)

        #print 'referenceIndex: '  + str(self.referenceIndex)
        #print self.referenceBoxes[0][0]


        #referenceBox = self.referenceBoxes[0][self.referenceIndex]
        referenceBox.color = colorRGB

        #boxPosX = referenceBox.pos[0]
        #boxPosY = referenceBox.pos[1]
        #boxPosZ = referenceBox.pos[2]

        #referenceBox.size = (referenceBox.size[0], referenceBox.size[1], referenceBox.size[2] + posZ)

        #label(pos=(boxPosX,boxPosY,boxPosZ), text=str(inputValue[0]))
        self.referenceIndex = self.referenceIndex + 1

        self.matrixAcumBoxes[posX, posY] = self.matrixAcumBoxes[posX, posY] + 1

    def visualizeNeuralPointsBidimensional(self, winnerPoint, inputValue, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2):

        #scene.center = vector(3,2,-1)
        #scene.forward =  vector(0,0,1)

        posX = winnerPoint[0]
        posY = winnerPoint[1]


        desvio = self.matrixAcumBoxes[posX, posY]
        posZ = desvio

        #print 'graficando box (' + str(posX) + ',' + str(posY) + ',' + str(posZ) + ')';

        valueAbs = abs(inputValue[0])

        valueZeroOne = 0
        if(valueAbs == inputValue[0]):
            valueZeroOne = valueAbs/10.0
        else:
            valueZeroOne = valueAbs*2/10.0

        zone = self.whichZoneBelongs(inputValue, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)
        #print 'belogns to zone: ' + str(zone)
        #zone = color.black

        commonSize = 0.7

        #colorRGB = (random.uniform(0,1),random.uniform(0,1) ,random.uniform(0,1) )
        colorRGB = color.black

        if(zone ==  0):
            colorRGB = color.black
            print '--------- ColorBlack detected ---------'

        if(zone ==  1):
            colorRGB = color.blue

        if(zone ==  2):
            colorRGB = color.green

        if(zone ==  3):
            colorRGB = color.red

        if(zone ==  4):
            colorRGB = color.yellow

        #box(pos=(posX, posY, posZ), size=(0.4, 0.4, 0.4), color=color.red)
        #box(pos=(posX, posY, posZ), size=(0.4, 0.4, 0.4), color=color.rgb_to_hsv(colorRGB))
        box(pos=(posX, posY, posZ), size=(commonSize, commonSize, commonSize), color=colorRGB)

        if(self.showLabel):
            texto = '(' + str(round(inputValue[0],2)) + ',' +  str(round(inputValue[1],2)) + ')'

            aLabel = label(pos=(posX,posY,posZ), text=texto, color=color.white, opacity=0, border=0, box = False)
            self.labels.append(aLabel)

        #print 'referenceIndex: '  + str(self.referenceIndex)
        #print self.referenceBoxes[0][0]


        #referenceBox = self.referenceBoxes[0][self.referenceIndex]
        #referenceBox.color = colorRGB

        #boxPosX = referenceBox.pos[0]
        #boxPosY = referenceBox.pos[1]
        #boxPosZ = referenceBox.pos[2]

        #label(pos=(boxPosX,boxPosY,boxPosZ), text=str(inputValue[0]))
        self.referenceIndex = self.referenceIndex + 1

        self.matrixAcumBoxes[posX, posY] = self.matrixAcumBoxes[posX, posY] + 1

    def whichZoneBelongs(self,inputValue, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2):

        #print '--------'
        #print 'inputValue: ' + str(inputValue)
        #print 'firstBoundX1: ' + str(firstBoundX1)
        #print 'endBoundX1: ' + str(endBoundX1)
        #print 'firstBoundX2: ' + str(firstBoundX2)
        #print 'endBoundX2:' + str(endBoundX2)
        #print '--------'


        x = inputValue[0]
        y = inputValue[1]

        if(x >= firstBoundX1 and x <= endBoundX1):

            if(y >= firstBoundX2 and y <= endBoundX2):
                return 1

            if (y >= firstBoundX1 and y <= endBoundX1):
                return 3

        if(x >= firstBoundX2 and x <= endBoundX2):

            if(y >= firstBoundX2 and y <= endBoundX2):
                return 2

            if (y >= firstBoundX1 and y <= endBoundX1):
                return 4

        return 0



    def visualizeNeuralPoints(self, winnerPoint, neuronaActivada, inputValue, zPosition):

        scene.center = vector(3,2,-1)
        #scene.forward =  vector(0,0,1)

        posX = winnerPoint[0]
        posY = winnerPoint[1]

        desvio = self.matrixAcumBoxes[posX, posY]
        posZ = desvio + zPosition

        posX = neuronaActivada
        posY = 1

        #print 'graficando box (' + str(posX) + ',' + str(posY) + ',' + str(posZ) + ')';

        valueAbs = abs(inputValue[0])

        valueZeroOne = 0
        if(valueAbs == inputValue[0]):
            valueZeroOne = valueAbs/10.0
        else:
            valueZeroOne = valueAbs*2/10.0

        commonSize = 0.7

        #colorRGB = (random.uniform(0,1),random.uniform(0,1) ,random.uniform(0,1) )
        colorRGB = color.hsv_to_rgb((valueZeroOne,valueZeroOne,valueZeroOne))

        #box(pos=(posX, posY, posZ), size=(0.4, 0.4, 0.4), color=color.red)
        #box(pos=(posX, posY, posZ), size=(0.4, 0.4, 0.4), color=color.rgb_to_hsv(colorRGB))
        box(pos=(posX, posY, posZ), size=(commonSize, commonSize, commonSize), color=colorRGB)

        if(self.showLabel):
            #aLabel = label(pos=(posX,posY,posZ), text=str(round(inputValue[0],2)), color=color.white, opacity=0, border=0, box = False)
            aLabel = ''
            self.labels.append(aLabel)

        #print 'referenceIndex: '  + str(self.referenceIndex)
        #print self.referenceBoxes[0][0]


        #referenceBox = self.referenceBoxes[0][self.referenceIndex]
        #referenceBox.color = colorRGB

        #boxPosX = referenceBox.pos[0]
        #boxPosY = referenceBox.pos[1]
        #boxPosZ = referenceBox.pos[2]

        posX = winnerPoint[0]
        posY = winnerPoint[1]

        #label(pos=(boxPosX,boxPosY,boxPosZ), text=str(inputValue[0]))
        self.referenceIndex = self.referenceIndex + 1

        self.matrixAcumBoxes[posX, posY] = self.matrixAcumBoxes[posX, posY] + 1

    def waitForKey(self):
        key = scene.kb.getkey()

        for i in range(0,len(self.labels)):
            oneLabel = self.labels[i]
            oneLabel.text = ''


