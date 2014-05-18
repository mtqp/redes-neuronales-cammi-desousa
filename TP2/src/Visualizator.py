from visual import *
import numpy as np
import math
import random

class Visualizator:
    def __init__(self):
        #nothing yet to do
        
    def printMatrix(self):#, matrix):
        redbox=box(pos=vector(4,2,3),size=(8,4,6),color=color.red)
        ball=sphere(pos=vector(4,7,3),radius=2,color=color.green)