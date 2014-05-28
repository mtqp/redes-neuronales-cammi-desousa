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
        return [6,5,4,3,2,1]
        #return [6,5,4,3,5,1]
        #return [6,5,1,4,3,1]

        topValue = 10

        boundVector = []
        i = 0
        while i < self.nDimension:
            randomValue = random.uniform(0, topValue)
            randomValue = int(randomValue) #Just to testing with integers

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

    def createRandomVectorWithBounds(self, firstBound, endBound, randomMethod):
        randomVector = []
        i = 0
        while i < self.nDimension:

            randomValue = 0

            if(randomMethod == self.UNIFORM):
                randomValue = random.uniform(firstBound, endBound)

            if(randomMethod == self.NORMAL):


                intervalDifference = endBound - firstBound
                media = (abs(endBound) - abs(firstBound))/2
                varianza = intervalDifference/4.0
                randomValue = random.gauss(media, varianza)

                #print 'intervalDifference: ' + str(intervalDifference)
                #print 'media : ' + str(media)
                #print 'varianza: ' + str(varianza)
                #print 'randomValue: ' + str(randomValue)


            #print randomValue
            #if not randomValue in randomVector:
            i += 1
            randomVector.append(randomValue)
        return randomVector
