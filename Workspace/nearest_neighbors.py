import math
import numpy as np
from scipy import spatial
from random import randint

def KNN_test(X_train,Y_train,X_val,Y_val, K):
    total_size = 0
    accuracy = 0
    iterator = 0
    value = 0
    y_values = []
    neighbor_distance_list = []
    closest_neighbors_iterators = []
    sum = 0
    # k_values = []
    for coordinates in X_train:
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
        iterator = iterator + 1
    iterator = 0
    total_size = len(Y_train)
    for x in range (total_size):
        if y_values[x] == Y_val[x]:
            accuracy = accuracy + 1
    return accuracy / total_size
