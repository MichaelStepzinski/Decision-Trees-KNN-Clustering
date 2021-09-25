import math
import numpy as np
from scipy import spatial
from random import randint

def KNN_test(X_train,Y_train,X_val,Y_val, K):
    iterator = 0
    value = 0
    y_values = []
    neighbor_distance_list = []
    closest_neighbors_iterators = []
    sum = 0
    # k_values = []
    for coordinates in X_train:
        print("X: {} Y: {}".format(coordinates, Y_train[iterator]))
        # find iterators of K closest neighbors
        for x_test in X_val:
            neighbor_distance_list.append(math.dist(coordinates, x_test))
        for x in range(K):
            min_index = neighbor_distance_list.index(min(neighbor_distance_list))
            closest_neighbors_iterators.append(min_index)
            neighbor_distance_list[min_index] = 9999
        #add up all neighbor values
        for x in range(K):
            sum = sum + Y_train[closest_neighbors_iterators[x]]
        #Sum = sum(k_values)
        if sum > 0:
            value = 1
        elif sum < 0:
            value = -1
        elif sum == 0:
            value = 1
        else:
            print("sum of neighbors is weird")
        y_values.append(value)
        closest_neighbors_iterators.clear()
        neighbor_distance_list.clear()
        value = 0
        sum = 0
        print("guess: {}".format(y_values[iterator]))
        iterator = iterator + 1
