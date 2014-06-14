import random
import numpy as np

class DataSetCreator:

    UNIFORM = 'UNIFORM'
    NORMAL = 'NORMAL'

    def __init__(self, nDimension):
        self.nDimension = nDimension
        self.boundVector = self.createBoundVector()

    def getRandomDataSet(self, amountOfRandomSets):
        randomDataSet = []

        i = 0
        while i < amountOfRandomSets:
            randomVector = self.createRandomVector()

            if not randomVector in randomDataSet:
                i += 1
                randomDataSet.append(randomVector)
        return randomDataSet

    def createRandomVector(self):
        randomVector = []
        i = 0
        while i < self.nDimension:
            bound = self.boundVector[i]
            randomValue = random.uniform(-bound, bound)

            if not randomValue in randomVector:
                i += 1
                randomVector.append(randomValue)
        return randomVector


    def createBoundVector(self):
        #return [6,5,4,3,2,1]
        #return [6,5,4,3,5,1]
        #return [6,5,1,4,3,1]

        topValue = 10

        boundVector = []
        i = 0
        while i < self.nDimension:
            randomValue = random.uniform(0, topValue)
            #randomValue = int(randomValue) #Just to testing with integers

            if not randomValue in boundVector:
                i += 1
                boundVector.append(randomValue)
        return boundVector

    #Para el ejercicio 2
    def getRandomDataSetOfVectors(self, amountOfRandomSets, firstBound, endBound, randomMethod):
        randomDataSet = []

        #print 'amountOfRandomSets: ' + str(amountOfRandomSets)
        #print 'Interval: (' + str(firstBound) + ',' + str(endBound) + ')'
        #print 'randomMethod: ' + str(randomMethod)

        i = 0
        while i < amountOfRandomSets:
            randomVector = self.createRandomVectorWithBounds(firstBound, endBound, randomMethod)

            #if not randomVector in randomDataSet:
            i += 1
            randomDataSet.append(randomVector)
        return randomDataSet

    def getRandomDataSetOfVectorsBidimensional(self, amountOfRandomSets, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2):
        randomDataSet = []

        #print 'amountOfRandomSets: ' + str(amountOfRandomSets)
        #print 'Interval: (' + str(firstBound) + ',' + str(endBound) + ')'
        #print 'randomMethod: ' + str(randomMethod)

        i = 0
        while i < amountOfRandomSets:
            randomVector = self.createRandomVectorWithBoundsBidimensional(firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)

            #if not randomVector in randomDataSet:
            i += 1
            randomDataSet.append(randomVector)
        return randomDataSet

    def getRandomDataSetOfVectorsBidimensional2(self, amountOfRandomSets, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2):
        randomDataSet = []

        #print 'amountOfRandomSets: ' + str(amountOfRandomSets)
        #print 'Interval: (' + str(firstBound) + ',' + str(endBound) + ')'
        #print 'randomMethod: ' + str(randomMethod)

        i = 0
        while i < amountOfRandomSets:
            randomVector = self.createRandomVectorWithBoundsBidimensional2(firstBoundX1, endBoundX1, firstBoundX2, endBoundX2)

            #if not randomVector in randomDataSet:
            i += 1
            randomDataSet.append(randomVector)
        return randomDataSet

    def createRandomVectorWithBoundsBidimensional(self, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2):
        randomVector = []

        randomValueX = 0
        randomValueY = 0

        upperRandom = random.uniform(0, 1)
        if(upperRandom >= 0.5):
            #upper
            lateralRandom = random.uniform(0, 1)
            if(lateralRandom >= 0.5):
                #right (2do cuadrante)
                randomValueX = random.uniform(firstBoundX2, endBoundX2)
                randomValueY = random.uniform(firstBoundX2, endBoundX2)
            else:
                #left (1er cuadrante)
                randomValueX = random.uniform(firstBoundX1, endBoundX1)
                randomValueY = random.uniform(firstBoundX2, endBoundX2)
        else:
            #down
            lateralRandom = random.uniform(0, 1)
            if(lateralRandom >= 0.5):
                #right (4do cuadrante)
                randomValueX = random.uniform(firstBoundX2, endBoundX2)
                randomValueY = random.uniform(firstBoundX1, endBoundX1)
            else:
                #left (3er cuadrante)
                randomValueX = random.uniform(firstBoundX1, endBoundX1)
                randomValueY = random.uniform(firstBoundX1, endBoundX1)

        randomVector.append(randomValueX)
        randomVector.append(randomValueY)
        return randomVector

    def createRandomVectorWithBoundsBidimensional2(self, firstBoundX1, endBoundX1, firstBoundX2, endBoundX2):
        randomVector = []

        randomValueX = 0
        randomValueY = 0

        upperRandom = random.uniform(0, 1)
        if(upperRandom >= 1):
            #upper
            lateralRandom = random.uniform(0, 1)
            if(lateralRandom >= 0.5):
                #right (2do cuadrante)
                randomValueX = random.uniform(firstBoundX2, endBoundX2)
                randomValueY = random.uniform(firstBoundX2, endBoundX2)
            else:
                #left (1er cuadrante)
                randomValueX = random.uniform(firstBoundX1, endBoundX1)
                randomValueY = random.uniform(firstBoundX2, endBoundX2)
        else:
            #down
            lateralRandom = random.uniform(0, 1)
            if(lateralRandom >= 1):
                #right (4do cuadrante)
                randomValueX = random.uniform(firstBoundX2, endBoundX2)
                randomValueY = random.uniform(firstBoundX1, endBoundX1)
            else:
                #left (3er cuadrante)
                randomValueX = random.uniform(firstBoundX1, endBoundX1)
                randomValueY = random.uniform(firstBoundX1, endBoundX1)

        randomVector.append(randomValueX)
        randomVector.append(randomValueY)
        return randomVector

    def createRandomVectorWithBounds(self, firstBound, endBound, randomMethod):
        randomVector = np.zeros((1,self.nDimension))
        #print 'matrix dimensions ' + str(randomVector.shape)
        #print randomVector
        i = 0
        while i < self.nDimension:

            randomValue = 0

            if(randomMethod == self.UNIFORM):
                randomValue = random.uniform(firstBound, endBound)

                if randomValue >= 0:
                    randomValue = 1
                else:
                    randomValue = -1


            if(randomMethod == self.NORMAL):


                intervalDifference = endBound - firstBound
                #media = (abs(endBound) - abs(firstBound))/2
                #media = (endBound + firstBound)/2
                media = 0
                varianza = intervalDifference/4.0
                randomValue = random.gauss(media, varianza)

                #print 'intervalDifference: ' + str(intervalDifference)
                #print 'media : ' + str(media)
                #print 'varianza: ' + str(varianza)
                #print 'randomValue: ' + str(randomValue)


            #print randomValue
            #if not randomValue in randomVector:
            #print '[0][i]' + str(i)
            randomVector[0][i] = randomValue
            i += 1

        return randomVector
