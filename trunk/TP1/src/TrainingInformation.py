import numpy as np

class TrainingInformation:
    def __init__(self, errors):
        self.errors = errors
        self.validations = []
        self.testSetErrors = TestSetInformation()

    def addValidationInformation(self, validation):
        matchingValidation = [val for val in self.validations if (validation.expectedOutput == val.expectedOutput).all()]
        
        if len(matchingValidation) == 1:
            matchingValidation[0].addObtainedOutput(validation)
        elif len(matchingValidation) == 0:
            self.validations.append(validation)
        else:
            raise Exception("There are more than one matching validation for this expected output: " + str(validation.expectedOutput))
            
    def addTestSetInformation(self, epoch, epsilon):
        self.testSetErrors.add(epoch, epsilon)

class TestSetInformation:
    def __init__(self):
        self.information = {}
        self.yLabel = "Error"
        self.xLabel = "Epoca"
        self.title = "Error en funcion de epoca para generalizacion"
        
    def add(self, epoch, epsilon):
        if epoch in self.information:
            self.information[epoch].append(epsilon)
        else:
            self.information[epoch] = [epsilon]
    
    def epochsCount(self):
        return  max(self.information.keys())
        
    def maxForEpoch(self, epoch):
        return max(self.information[epoch])
        
    def minForEpoch(self, epoch):
        return min(self.information[epoch])
        
    def averageForEpoch(self, epoch):
        n = len(self.information[epoch])
        epochSum = sum(self.information[epoch])
        return epochSum / n
        
class ErrorInformation: #falta la clase abstracta de esto!
    def __init__(self, x, y, description, etta):
        self.x = x
        self.y = y
        self.yLabel = 'Error'
        self.xLabel = 'Epoca'
        self.title = 'Error en funcion del tiempo para aprendizaje de: ' + description 
        self.etta = etta
        
    def add(self, xValue, yValue):
        self.x.append(xValue)
        self.y.append(yValue)

class ValidationInformation: #falta la clase abstracta de esto!
    def __init__(self, expectedOutput, obtainedOutput, description):
        self.expectedOutput = expectedOutput
        self.obtainedOutputs = [] 
        self.obtainedOutputs.append(obtainedOutput)
        self.yLabel = 'Valor funcion'
        self.xLabel = 'Epoca'
        self.title = 'Validacion de aprendizaje de:' + description
        
    def addObtainedOutput(self, validation):
        self.obtainedOutputs = self.obtainedOutputs + validation.obtainedOutputs 
    
