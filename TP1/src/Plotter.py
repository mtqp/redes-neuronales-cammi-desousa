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

    def plot(self, trainingInformation, mustShow):
        #self.plotError(trainingInformation.errors)
        self.plotValidation(trainingInformation.validations)
        if mustShow:
            plotter.show()
        
    def plotValidation(self, validations):
        print 'plotting validation information'
        
        figureIndex = 0
        for validation in validations:
            figureIndex += 1    #Figure 1 is used to graphics the error
            figure(figureIndex) #Set error plotting to figure i
            
            xAxis = []
            yExpectedAxis = []
            yObtainedAxis = []
            
            plotter.ylabel(validation.yLabel)
            plotter.xlabel(validation.xLabel)
            plotter.title(validation.title)
            
            expectedYValue = self.getYValue(validation.expectedOutput)
            
            x = 1
            for obtainedOutput in validation.obtainedOutputs:
                obtainedYValue = self.getYValue(obtainedOutput)
                xAxis.append(x)
                yExpectedAxis.append(expectedYValue)
                yObtainedAxis.append(obtainedYValue)
                x += 1
            
            plotter.plot(xAxis, yExpectedAxis)
            plotter.plot(xAxis, yObtainedAxis)
            
            self.saveToFile(self.validationFileName + ' letra ' + str(expectedYValue))
    
    def getYValue(self, output):
        output = output.flat
        #print 'output to plot: '+ str(output)
        #print 'output length: ' + str(len(output))
        yValue = 0
        for i in range(len(output)-1,-1,-1):
            absIValue = abs(output[i])
            #print 'absivalue: ' + str(absIValue)
            coefficient = math.pow(2,absIValue)
            #print '2 pow abs: ' + str(coefficient)
            coefficient = math.pow(coefficient, i)
            #print 'final coef: ' + str(coefficient)
            yValue = yValue + coefficient
        print 'value in y terms: ' + str(yValue)
        return yValue
        
    def saveToFile(self, fileName):
        if self.mustSaveToFile:
            completeFileName = fileName + ' - etta ' + str(information.etta) + ' - ' + self.getNow() + '.png'
            print 'saving on: ' + completeFileName        
            plotter.savefig(completeFileName)
    
    def plotError(self, information):
        print 'plotting error information'
        figure(0) #Set error plotting to figure 0
        plotter.plot(information.x, information.y)
        plotter.ylabel(information.yLabel)
        plotter.xlabel(information.xLabel)
        plotter.title(information.title)
        
        self.saveToFile(self.errorFileName)
    
    def getNow(self):
        return datetime.now().strftime("%Y%m%d%H%M%S")
