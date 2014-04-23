import random
from math import sin
from math import pi

class StandardBP:
    def matlabName(self):
        return '\'traingd\''
        
class AdaptiveWithMomentumBP:
    def matlabName(self):
        return '\'traingdx\''
        
class MomentumBP:
    def matlabName(self):
        return '\'traingdm\''

class FunctionInputCreator:
    def __init__(self, fileName, trainingSetCount, testingSetCount, epsilon, etta, epochs, neuralType, hiddenNodes):
        self.fileName = fileName
        self.trainingSetCount = trainingSetCount
        self.testingSetCount = testingSetCount
        self.epsilon = epsilon
        self.etta = etta
        self.epochs = epochs
        self.neuralType = neuralType
        self.hiddenNodes = hiddenNodes
        
    def create(self):
        print 'FUNCTION - Creating file'
        f = open(self.fileName,'w')
        
        trainingVectorXYValue = self.getTrainingSet()
        testingVectorXYValue = self.getTestingSet()
        
        f.write('%training\n')
        self.writeVector(f, 'training', trainingVectorXYValue)
        f.write('%testing\n')
        self.writeVector(f, 'testing', testingVectorXYValue)
        
        self.writeProgram(f)
        '''
        f.write('name=' + description +'\n') 
        f.write('etta=' + str(etta) +'\n') 
        f.write('epsilon=' + str(epsilon) +'\n') 
        f.write('epochs=' + str(epochs) +'\n') 
        '''
        print 'FUNCTION - File created'
        f.close() 
        
    def writeProgram(self, f):
        
        f.write('%Parameters set dynamically\n')
        f.write('hiddenNodes = ' + str(self.hiddenNodes) + ';\n')
        f.write('epochs = ' + str(self.epochs) + ';\n')
        f.write('etta = ' + str(self.etta) + ';\n')
        f.write('neuralType = ' + self.neuralType.matlabName() + ';\n')
        f.write('epsilon = ' + str(self.epsilon) + ';\n')

        f.write('\n%Set net\n')
        f.write('net = feedforwardnet(hiddenNodes);  %Set neuronal net with N hidden nodes\n')
        f.write('net.trainFcn = neuralType;\n')
        f.write('net.trainParam.goal = epsilon      %Set epsilon\n')
        f.write('net.trainParam.epochs = epochs;    %Set epochs\n')
        f.write('net.trainParam.lr = etta;          %Set etta\n\n')

        f.write('net = train(net,trainingInput,trainingOutput);\n')
        f.write('view(net)\n')
        f.write('netTestingOutput = net(testingInput);\n')
        f.write('perf = perform(net,netTestingOutput,testingOutput)\n')
        
    def getTrainingSet(self):
        trainingSet = []
        
        minimalTrainingSet = self.getMinimalTrainingSet()
        
        if len(minimalTrainingSet) <= self.trainingSetCount:
            trainingSet += minimalTrainingSet
       
        if len(trainingSet) < self.trainingSetCount:
            extraCount = self.trainingSetCount - len(trainingSet)
            trainingSet = trainingSet + self.getRandomSets(extraCount)
            
        return trainingSet
        
    def getMinimalTrainingSet(self):
        minimalTrainingSet = []

        minimalTrainingSet.append([0,0,0])              #0
        minimalTrainingSet.append([pi,2*pi,0])          #2pi
        minimalTrainingSet.append([pi/2,0,1])           #pi/2
        minimalTrainingSet.append([0,pi,1])             #pi/2
        minimalTrainingSet.append([pi/2,pi,1])          #pi
        minimalTrainingSet.append([0,pi/2,0.707106])    #pi/4
        minimalTrainingSet.append([pi/2,pi/2,0.707106]) #3pi/4
        minimalTrainingSet.append([pi/4,2*pi,-0.707106])#5pi/4
        minimalTrainingSet.append([pi,pi,-1])           #3pi/2
        minimalTrainingSet.append([5*pi/4,pi,-0.707106])#7pi/4
        
        return minimalTrainingSet
        
    def getRandomSets(self, count):
        randomSet = []
        for i in range(count):
            x = random.uniform(0,2*pi)
            maxPossibleY = 2*(2*pi - x) #valor maximo de y para que sen este definida entre 0 y 2pi
            y = random.uniform(0, maxPossibleY)
            result = sin(x+y/2)
            
            randomSet.append([x,y,result])
        return randomSet
        
    def getTestingSet(self):
        return self.getRandomSets(self.testingSetCount)
        
    def writeVector(self, file, vectorName, vectorXYValue):
        inputAsString = '['
        outputAsString = '['
        for xyValue in vectorXYValue:
            x = xyValue[0]
            y = xyValue[1]
            value = xyValue[2]
            inputAsString +=  str(x) + ' ' + str(y) + ';'
            outputAsString+= str(value) + ' '
        inputAsString += '];'
        outputAsString += '];'
        
        file.write(vectorName + 'Input = ' + inputAsString + '\n')
        file.write(vectorName + 'Output = ' + outputAsString + '\n')
        file.write(vectorName + 'Input = transpose(' + vectorName + 'Input);\n')
            
            
            
            