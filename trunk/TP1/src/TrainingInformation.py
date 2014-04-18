
class TrainingInformation:
    def __init__(self, errors, validations):
        self.errors = errors
        self.validations = validations
        
class ErrorInformation: #falta la clase abstracta de esto!
    def __init__(self, x, y, description):
        self.x = x
        self.y = y
        self.yLabel = 'Error'
        self.xLabel = 'Epoch'
        self.title = 'Error en funcion del tiempo para aprendizaje de: ' + description 
        
    def add(self, xValue, yValue):
        self.x.append(xValue)
        self.y.append(yValue)

class ValidationInformation: #falta la clase abstracta de esto!
    def __init__(self, x, y, description):
        self.x = x
        self.y = y        
        self.yLabel = 'MISSING!'
        self.xLabel = 'MISSING!'
        self.title = 'MISSING!'
