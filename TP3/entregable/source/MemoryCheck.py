import Hamming

class MemoryCheck:
    def __init__(self, temperature, noise, trainingSet, checkingSet):
        self.temperature = temperature
        self.noise = noise
        self.distances = hammingDistances(trainingSet, checkingSet)

        self.activationResults = []

    def addActivationResult(self, i, equalityReached, hammingDist):
        self.activationResults.append((i, equalityReached, hammingDist))

    def results(self):
        maxHammingDist = max(self.distances)
        minHammingDist = min(self.distances)
        avgHammingDist = sum(self.distances) / len(self.distances)
        successFactor = sum([ float(activationResult[1]) for activationResult in self.activationResults ])/len(self.activationResults)
        failFactor = 1.0 - successFactor
        hammingImprovements = [ abs((self.distances[i] - self.iActivationResult(i)[2])) for i in range(0, len(self.distances))]
        print 'N: ' + str(self.noise) + ' MH: ' + str(maxHammingDist) + ' mH: ' + str(minHammingDist) + ' A: ' + str(avgHammingDist) + ' S: ' + str(successFactor) + ' F: ' + str(failFactor) + ' HImprove: M: ' + str(min(hammingImprovements)) +  ' m: ' + str(max(hammingImprovements)) + ' A: ' + str(sum(hammingImprovements)/len(hammingImprovements))

    def iActivationResult(self, i):
        for activationResult in self.activationResults:
            if activationResult[0] == i:
                return activationResult

def hammingDistances(set, setWithNoise):
    distances = []
    for i in range(0, len(set)):
        distances.append(Hamming.distance(set[i].flatten(), setWithNoise[i].flatten()))
    return distances