import matplotlib.pyplot as plotter

class Plotter:
    def __init__(self, errorFileName, validationFileName):
        self.errorFileName  = errorFileName
        self.validationFileName = validationFileName

        
    def plotError(self, trainingInformation):
        #define some data
        x = [1,2,3,4]
        y = [20, 21, 20.5, 20.8]

        plotter.plot(x, y)
        plotter.show()
    
    