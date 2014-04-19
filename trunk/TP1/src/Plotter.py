import matplotlib.pyplot as plotter
import math
from pylab import * 
from datetime import datetime
from datetime import time

class Plotter:
    def __init__(self, errorFileName, validationFileName, mustSaveToFile):
        self.errorFileName  = errorFileName
        self.validationFileName = validationFileName
        self.mustSaveToFile = mustSaveToFile
        self.figures = []

    def plot(self, trainingInformation, mustShow):
        self.plotError(trainingInformation.errors)
        self.plotValidation(trainingInformation.validations)
        if mustShow:
            plotter.show()
        else:
            for figure in self.figures:
                plotter.close(figure)
        
    def plotValidation(self, validations):
        print 'plotting validation information'
        
        figureIndex = 0
        for validation in validations:
            figureIndex += 1    #Figure 1 is used to graphics the error
            self.figures.append(figure(figureIndex)) #Set error plotting to figure i
            
            xAxis = []
            yExpectedAxis = []
            yObtainedAxis = []
            
            expectedYValue = self.getYValue(validation.expectedOutput)
            
            plotter.ylabel(validation.yLabel)
            plotter.xlabel(validation.xLabel)
            plotter.title(validation.title + ' para valor: ' + str(expectedYValue))
            
            '''
            print 'expected Y: ' + str(expectedYValue)
            print 'got instead'
            '''
            x = 1
            for obtainedOutput in validation.obtainedOutputs:
                obtainedYValue = self.getYValue(obtainedOutput)
                xAxis.append(x)
                yExpectedAxis.append(expectedYValue)
                yObtainedAxis.append(obtainedYValue)
                #print obtainedYValue
                x += 1
            
            plotter.plot(xAxis, yExpectedAxis)
            plotter.plot(xAxis, yObtainedAxis)
            
            self.saveToFile(self.validationFileName + ' letra ' + str(expectedYValue))
        self.figureCount = figureIndex
    
    def getYValue(self, output):
        output = output.flat
        yValue = 0
        for i in range(len(output)-1,-1,-1):
            absIValue = abs(output[i])
            coefficient = 2*absIValue
            coefficient = math.pow(coefficient, i)
            yValue = yValue + coefficient
        return yValue
        
    def saveToFile(self, fileName):
        if self.mustSaveToFile:
            completeFileName = fileName + ' - etta ' + str(information.etta) + ' - ' + self.getNow() + '.png'
            print 'saving on: ' + completeFileName        
            plotter.savefig(completeFileName)
    
    def plotError(self, information):
        print 'plotting error information'
        self.figures.append(figure(0)) #Set error plotting to figure 0
        plotter.plot(information.x, information.y)
        plotter.ylabel(information.yLabel)
        plotter.xlabel(information.xLabel)
        plotter.title(information.title)
        
        self.saveToFile(self.errorFileName)
      
    
    def getNow(self):
        return datetime.now().strftime("%Y%m%d%H%M%S")
