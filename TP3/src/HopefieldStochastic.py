import numpy as np

#todo: make it work!!
class HopefieldStochastic:

    #s vector de activacion
    #x vectores de aprendizaje (1 sola iteracion) son los patrones que se quieren memorizar

    def __init__(self, n):
        self.n = n
        self.matrix = np.zeros((self.n,self.n))

    def training(self, dataSet):
        for x in dataSet:
            self.matrix += np.transpose(x)*x
        self.matrix /= self.n
        self.matrix -= self.matrix.diagonal(0)
        return self.matrix

    def energy(self, s, matrix):
        return -0.5 * ((s * matrix) * np.transpose(s))

    def activate(self, x, synch):

        s = x
        previousS = np.zeros((1,self.n))

        while not (s == previousS).all():
            previousS[:] = s

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
        return [self.sign(x) for x in vector]

    def sign(self, item):
        if item >= 0:
            return 1
        else:
            return -1

    def visualizeEnergy(self,energyValue, s):
        #print "energyValue: " + str(energyValue)
        #print "s value: " + str(s)
        return None