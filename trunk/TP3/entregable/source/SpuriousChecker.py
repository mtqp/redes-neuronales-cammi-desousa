import Hamming


class SpuriousChecker:
    def __init__(self, trainingSet, hammingPercentage):
        self.trainingSet = [training.flatten() for training in trainingSet]
        self.activations = []
        self.hammingPercentage = hammingPercentage

    def addActivation(self, activation):
        self.activations.append(activation.flatten())

    def showResults(self):
        exactMatches = [activation for activation in self.activations if self.isActivationIn(self.trainingSet, activation)]
        hammingMatches = [activation for activation in self.activations if self.matchesInHammingPercentage(activation)]
        spurious = [activation for activation in self.activations if not self.isActivationIn(exactMatches, activation)
                                                                 and not self.isActivationIn(hammingMatches, activation)]
        print 'exact: ' + str(len(exactMatches))
        print 'hamming matches: ' + str(len(hammingMatches))
        print 'spurious: ' + str(len(spurious))

    def isActivationIn(self, set, vector):
        return  sum([(vector == vectorInSet).all() for vectorInSet in set]) > 0

    def matchesInHammingPercentage(self, vector):
        return sum([1 for trainingVector
                    in self.trainingSet
                    if (Hamming.distance(trainingVector, vector) /100.0) < self.hammingPercentage ]) \
               > 0

    def clearActivations(self):
        self.activations = []