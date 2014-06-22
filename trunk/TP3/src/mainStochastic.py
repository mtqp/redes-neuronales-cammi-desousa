import numpy as np
from Hopefield import Hopefield
from DataSetCreator import DataSetCreator
from Letter import Letter
import Hamming

def main():
    a = np.array([1,1,1,-1,-1,-1])
    b = np.array([1,-1,1,-1,1,-1])
    distance = Hamming.distance(a,b)
    print 'distance is: ' + str(distance)

if __name__ == "__main__":
    main()
