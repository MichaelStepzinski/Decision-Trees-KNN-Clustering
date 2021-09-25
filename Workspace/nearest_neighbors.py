import math
import numpy as np
from scipy import spatial
from random import randint

def KNN_test(X_train,Y_train,X_val,Y_val, K):
    iterator = 0
    for coordinates in X_train:
        print("X: {} Y: {}".format(coordinates, Y_train[iterator]))
        iterator = iterator + 1
