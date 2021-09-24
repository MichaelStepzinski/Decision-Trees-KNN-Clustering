import math
import numpy as np
from scipy import spatial
from random import randint


def DT_train_binary(X, Y, max_depth):
    # step 1 - calculate entropy of the entire set
    branch_entropies = []
    tree = []
    #rules = []
    instruction = []
    solved_features = []
    key_instruction = 0
    num_features = len(X[0])
    set_length = len(Y)
    num_positive = sum(Y)
    total_entropy = calculate_entropy(num_positive, set_length)

    while(max_depth != len(tree)):
        for x in range(num_features):
            if x not in solved_features:
                no_entropy = find_split_entropy(x, 0, X, Y, tree)
                yes_entropy = find_split_entropy(x, 1, X, Y, tree)
                branch_entropies.append(find_IG(no_entropy, yes_entropy, total_entropy, set_length))
            if x in solved_features:
                branch_entropies.append(0)
        highest_IG = max(branch_entropies)
        max_index = branch_entropies.index(highest_IG)
        #instruction.clear()
        instruction.append(max_index)
        branch_entropies.clear()

        entropyN = find_split_entropy(max_index, 0, X, Y, tree)
        if entropyN[0] == 0:
            instruction.append(0) #this value can vary, find pattern of what to put

            instruction.append(2)
            key_instruction = 1
        entropyY = find_split_entropy(max_index, 1, X, Y, tree)
        if entropyY[0] == 0:
            instruction.append(2)
            instruction.append(1) #this value can vary
            key_instruction = 0
        solved_features.append(max_index)
        tree.append(instruction)
        instruction = []
        #instruction.clear()
        # CALLING INSTRUCTION.CLEAR ALSO CLEARS TREE >:(
        total_entropy, set_length, total_positive, total_negative = find_split_entropy(max_index, key_instruction, X, Y, tree)

        # LEFT OFF AT DOUBLE CHECKING ALL FEATURES WORK PROPERLY
    print("end")

    print(tree)

def find_IG(splitL, splitR, total_entropy, length):
    return total_entropy - ((splitL[1] / length) * splitL[0] + (splitR[1] / length) * splitR[0])


def find_split_entropy(column, value, X, Y, rules):
    split_positive = 0
    split_total = 0
    split_negative = 0
    for idx in enumerate(X):
        if idx[1][column] == value and table_checker(idx[1], rules):
            #check for tree in here
            split_total = split_total + 1
            if Y[idx[0]] == 1:
                split_positive = split_positive + 1
    split_negative = split_total - split_positive
    return calculate_entropy(split_positive, split_total), split_total, split_positive, split_negative


def table_checker(line, rules):
    for x in rules:
        for y in range(len(x)-1):
            if x[y+1] != 2:
                if line[x[0]] == x[y+1]:
                    return False
            #print("true")
    return True

def calculate_entropy(pos, total):
    neg = total - pos
    if neg == 0:
        return - (pos / total) * math.log2(pos / total)
    elif pos == 0:
        return - (neg / total) * math.log2(neg / total)
    else:
        return -(neg / total) * math.log2(neg / total) - (pos / total) * math.log2(pos / total)