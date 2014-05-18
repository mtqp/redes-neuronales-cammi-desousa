from visual import *
import numpy as np
import math
import random


class Visualizator:
    def __init__(self):
        self.ball = sphere(pos=(-5,0,0), radius=0.5, color=color.cyan)
        self.wallR = box(pos=(6,0,0), size=(0.2,12,12), color=color.green)
        self.ball.velocity = vector(25,0,0)

    def printMatrix(self):#, matrix):
        self.ball.pos = self.ball.pos + self.ball.velocity*0.0005