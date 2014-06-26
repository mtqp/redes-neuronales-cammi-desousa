import numpy as np
import Hamming


class Hopefield:

    #s vector de activacion
    #x vectores de aprendizaje (1 sola iteracion) son los patrones que se quieren memorizar

    def __init__(self, n):
        self.n = n
        self.matrix = np.zeros((self.n, self.n))

    def training(self, dataSet):
        for x in dataSet:
            transposedX = np.transpose(x)
            self.matrix += transposedX * x
        self.matrix /= self.n
        self.matrix -= np.diag(np.diag(self.matrix))
        return self.matrix

    def energy(self, s, matrix):
        return -0.5 * (np.dot(np.dot(s,matrix),np.transpose(s)))

    def activate(self, x, synch):

        s = np.zeros((1,self.n))
        #s = x

        for i in range(0, len(x)):
            s[i] = x[i]

        previousS = np.zeros((1,self.n))

        #Valores iniciales arbitrarios
        energyValue = 1
        previousEnergy = 0

        energyVector = []
        counter = 1
        while not (s == previousS).all() and not self.insideEnergyThreshhold(energyValue, previousEnergy):
            #while not (s == previousS).all():
            #previousS[:] = s


            #print 'comparacion: ' + str(energyValue - previousEnergy)
            #print 's: ' + str(s)
            #print 'p ' + str(previousS)
            #print 'dist:' + str(Hamming.distance(s[0],previousS[0]))


            #print 'ciclando a lo loco'
            for i in range(0, len(s)):
                previousS[i] = s[i]

            if synch:
                s = self.vectorSign2(np.dot(s, self.matrix))
            else:
                permIndexes = np.random.permutation(self.n)

                for i in permIndexes:
                    #print 'permIndexes: ' + str(permIndexes)
                    #print 'i: ' + str(i)
                    #print 'self.matrix[:,' + str(i) + ']: ' + str(self.matrix[:,i])
                    #print 'result: ' + str(np.dot(s,self.matrix[:,i]))
                    #print 's lengh' + str(s.shape)
                    #print 's:' + str(s)
                    #print 'matrix lengh' + str(self.matrix.shape)
                    #print 'matrix:' + str(self.matrix)
                    s[0, i] = self.sign( np.dot(s,self.matrix[:,i]))

            previousEnergy = energyValue
            energyValue = self.energy(s,self.matrix)[0][0]
            print str(counter) + " " + str(energyValue)
            #print str(energyValue)
            #print 'Energy: ' + str(energyValue)
            #print 'PreviousEnergy: ' + str(previousEnergy)

            energyPoint = []
            energyPoint.append(counter)
            energyPoint.append(energyValue)
            energyVector.append(energyPoint)
            counter += 1

        #print str(counter) + " " + str(energyValue)
        self.visualizeEnergy(energyVector)

        return s

    def insideEnergyThreshhold(self, energyValue, previousEnergy):
        ##return (round(energyValue,2) == round(previousEnergy,2))
        return (abs(energyValue) - abs(previousEnergy)) < 1


    def vectorSign2(self, vector):

        vector = vector.flatten()

        signVector = np.zeros((1,len(vector)))

        for i in range(0, len(vector)):
            signVector[0][i] = (self.sign(vector[i]))

        #print 'vector: ' + str(vector)
        #print 'signVector: ' + str(signVector)

        return signVector

    def invertSign(self, vector):

        invertedVector = []

        for i in range(0, len(vector)):
            invertedVector.append(vector[i] * -1)

        return invertedVector

    def vectorSign(self, vector):
        print 'vector: ' + str(vector)
        signs = [self.sign(x) for x in vector]
        print 'signs: ' + str(signs)
        return signs

    def sign(self, item):
        if item >= 0:
            return 1
        else:
            return -1

    def visualizeEnergy(self,energyVector):

        #for i in range(0, len(energyVector)):
        #print
        #print "energyValue: " + str(energyValue)
        #print "s value: " + str(s)
        return None