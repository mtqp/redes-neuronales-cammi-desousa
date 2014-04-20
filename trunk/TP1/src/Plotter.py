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
        self.plotTestError(trainingInformation.testSetErrors)
        #self.plotValidation(trainingInformation.validations)
        if mustShow:
            plotter.show()
        else:
            for figure in self.figures:
                plotter.close(figure)
        
    def plotTestError(self, information): 
        figure(1)
        
        plotter.ylabel(information.yLabel)
        plotter.xlabel(information.xLabel)
        plotter.title(information.title)
        
        xAxis = []
        yAverage = []
        yMax = []
        yMin = []
        for epoch in range(0, information.epochsCount()):
            xAxis.append(epoch)
            yMax.append(information.maxForEpoch(epoch))
            yMin.append(information.minForEpoch(epoch))
            yAverage.append(information.averageForEpoch(epoch))
        
        '''
        plotter.plot(xAxis, yMax, color="blue", linewidth=2.5, linestyle="-", label="Error maximo")
        plotter.plot(xAxis, yMin, color="red", linewidth=2.5, linestyle="-", label="Error minimo")
        plotter.plot(xAxis, yAverage, color="black", linewidth=2.5, linestyle="-", label="Error promedio")
        '''
        plotter.plot(xAxis, yMax, label="Error maximo")
        plotter.plot(xAxis, yMin, label="Error minimo")
        plotter.plot(xAxis, yAverage, label="Error promedio")
        plotter.legend(loc='upper left')
        
    def plotValidation(self, validations):
        print 'PLOTTER - validation information'
        
        figureIndex = 1
        for validation in validations:
            figureIndex += 1    #Figure 0 is used to graphics the error and 1 is for test error
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
                print obtainedOutput
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
    
    def plotError(self, information):
        print 'PLOTTER - error information'
        self.figures.append(figure(0)) #Set error plotting to figure 0
        plotter.plot(information.x, information.y)
        plotter.ylabel(information.yLabel)
        plotter.xlabel(information.xLabel)
        plotter.title(information.title)
        
        self.saveToFile(self.errorFileName)
    
    def getYValue(self, output): #esto hace cualquiera
        output = output.flat
        yValue = 0
        for i in range(len(output)-1,-1,-1):
            sign = self.sign(output[i])
            absIValue = abs(output[i])
            coefficient = 2*absIValue
            coefficient = math.pow(coefficient, i)
            yValue = yValue + (sign * coefficient)
        return yValue
        
    def sign(self, value):
        if value >= 0:
            return 1
        return 0
        
    def saveToFile(self, fileName):
        if self.mustSaveToFile:
            completeFileName = fileName + ' - etta ' + str(information.etta) + ' - ' + self.getNow() + '.png'
            print 'saving on: ' + completeFileName        
            plotter.savefig(completeFileName)

    def getNow(self):
        return datetime.now().strftime("%Y%m%d%H%M%S")
