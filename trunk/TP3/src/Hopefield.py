import numpy as np


class Hopefield:

    #s vector de activacion
    #x vectores de aprendizaje (1 sola iteracion) son los patrones que se quieren memorizar

    def __init__(self, n):
        self.n = n
        self.matrix = np.zeros((self.n, self.n))

    def training(self, dataSet):
        for x in dataSet:
            print 'matrix shape: ' + str(self.matrix.shape)
            transposedX = np.transpose(x)
            print 'transposed shape: ' + str(transposedX.shape)
            print 'x shape: ' + str(x.shape)
            '''print 'transposed:'
            print transposedX
            print 'x:'
            print x'''
            self.matrix += transposedX * x
        self.matrix /= self.n
        self.matrix -= np.diag(np.diag(self.matrix))
        return self.matrix

    def energy(self, s, matrix):
        return -0.5 * ((s * matrix) * np.transpose(s))

    def activate(self, x, synch):

        s = np.zeros((1,self.n))
        #s = x

        for i in range(0, len(x)):
            s[i] = x[i]

        previousS = np.zeros((1,self.n))

        while not (s == previousS).all():
            #previousS[:] = s

            for i in range(0, len(s)):
                previousS[i] = s[i]

            if synch:
                s = self.vectorSign( s * self.matrix)
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

            energyValue = self.energy(s,self.matrix)
            self.visualizeEnergy(energyValue,s)

        return s

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

    def visualizeEnergy(self,energyValue, s):
        #print "energyValue: " + str(energyValue)
        #print "s value: " + str(s)
        return None