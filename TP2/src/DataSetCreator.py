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

        topValue = 1000

        boundVector = []
        i = 0
        while i < self.nDimension:
            randomValue = random.uniform(0, topValue)

            if not randomValue in boundVector:
                i += 1
                boundVector.append(randomValue)
        return boundVector