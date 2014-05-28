import random
import numpy as np

class DataSetCreator:

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
    def getRandomDataSetOfVectors(self, amountOfRandomSets, endBound):
        randomDataSet = []

        i = 0
        while i < amountOfRandomSets:
            randomVector = self.createRandomVectorWithBounds(0,endBound)

            #if not randomVector in randomDataSet:
            i += 1
            randomDataSet.append(randomVector)
        return randomDataSet

    def createRandomVectorWithBounds(self, firstBound, endBound):
        randomVector = []
        i = 0
        while i < self.nDimension:
            randomValue = random.randint(firstBound, endBound)
            #print randomValue
            #if not randomValue in randomVector:
            i += 1
            randomVector.append(randomValue)
        return randomVector
