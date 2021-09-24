import math
import numpy as np
from scipy import spatial
from random import randint


def DT_train_binary(X, Y, max_depth):
    # step 1 - calculate the entropy of the entire set
    set_length = len(Y)
    num_positive = sum(Y)
    total_entropy = calculate_entropy(num_positive, set_length)
    branch_entropies = []

    # step 2 - split training data using each feature and calculate information gain for each split

    num1 = find_split_entropy(0, 0, X, Y)
    num2 = find_split_entropy(0, 1, X, Y)
    branch_entropies.append(find_IG(num1, num2, total_entropy, set_length))

    num1 = find_split_entropy(1, 0, X, Y)
    num2 = find_split_entropy(1, 1, X, Y)
    branch_entropies.append(find_IG(num1, num2, total_entropy, set_length))

    num1 = find_split_entropy(2, 0, X, Y)
    num2 = find_split_entropy(2, 1, X, Y)
    branch_entropies.append(find_IG(num1, num2, total_entropy, set_length))

    num1 = find_split_entropy(3, 0, X, Y)
    num2 = find_split_entropy(3, 1, X, Y)
    branch_entropies.append(find_IG(num1, num2, total_entropy, set_length))

    # step 3 - split on feature that gives highest IG
    highest_IG = max(branch_entropies)
    max_index = branch_entropies.index(highest_IG)
    branch_entropies.clear()

    # repeat 2 - 4
    # find new set length and entropy splitting on max_index thus far
    #calculate entropy of female lead = N and female lead = Y
    entropyN = find_split_entropy(max_index, 0, X, Y)
    entropyY = find_split_entropy(max_index, 1, X, Y)
    instruction = [max_index]
    if entropyN[0] == 0 and entropyY[0] == 0:
        print("finish command")
    elif entropyN[0] == 0:
        print("entropy x is 0")
        instruction.append(0)
        instruction.append(2)
        rule = [max_index], 1
    elif entropyY[0] == 0:
        print("entropy y is 0")
        instruction.append
        rule = [max_index], 0
    print("Rule: {}".format(rule))
    total_entropy, set_length = find_split_entropy(max_index, 1, X, Y)

    #rule = [max_index], [1]
    num1 = find_split_entropy_rule(0, 1, X, Y, rule)
    num2 = find_split_entropy_rule(0, 0, X, Y, rule)
    branch_entropies.append(find_IG(num1, num2, total_entropy, set_length))

    num1 = find_split_entropy_rule(1, 1, X, Y, rule)
    num2 = find_split_entropy_rule(1, 0, X, Y, rule)
    branch_entropies.append(find_IG(num1, num2, total_entropy, set_length))

    #if column is already in list then append 0 to branch entropies to preserve indexing
    branch_entropies.append(0)

    num1 = find_split_entropy_rule(3, 1, X, Y, rule)
    num2 = find_split_entropy_rule(3, 0, X, Y, rule)
    branch_entropies.append(find_IG(num1, num2, total_entropy, set_length))
    #print(branch_entropies)

    highest_IG = max(branch_entropies)
    max_index = branch_entropies.index(highest_IG)
    print(max_index)
    branch_entropies.clear()

    entropyN = find_split_entropy_rule(max_index, 0, X, Y, rule)
    entropyY = find_split_entropy_rule(max_index, 1, X, Y, rule)
    print("EntropyN: {}".format(entropyN))
    print("EntropyY: {}".format(entropyY))
    instruction = [max_index]
    if entropyN[0] == 0 and entropyY[0] == 0:
        print("finish command")
    elif entropyN[0] == 0:
        print("entropy x is 0")
        #instruction.append(0)
        #instruction.append(2)
        rule1 = [max_index], 1
    elif entropyY[0] == 0:
        print("entropy y is 0")
        #instruction.append
        rule1 = [max_index], 0
    print("Rule1: {}".format(rule1))
    total_entropy, set_length = find_split_entropy(max_index, 1, X, Y)
    #print(total_entropy)
    #print(set_length)

    #part 3!
    num1 = find_split_entropy_rule1(0, 1, X, Y, rule, rule1)
    num2 = find_split_entropy_rule1(0, 0, X, Y, rule, rule1)
    branch_entropies.append(find_IG(num1, num2, total_entropy, set_length))

    branch_entropies.append(0)

    branch_entropies.append(0)
    #num1 = find_split_entropy_rule1(1, 1, X, Y, rule, rule1)
    #num2 = find_split_entropy_rule1(1, 0, X, Y, rule, rule1)
    #branch_entropies.append(find_IG(num1, num2, total_entropy, set_length))

    num1 = find_split_entropy_rule1(3, 1, X, Y, rule, rule1)
    num2 = find_split_entropy_rule1(3, 0, X, Y, rule, rule1)
    branch_entropies.append(find_IG(num1, num2, total_entropy, set_length))
    print(branch_entropies)

    highest_IG = max(branch_entropies)
    max_index = branch_entropies.index(highest_IG)
    print(max_index)
    branch_entropies.clear()

    entropyN = find_split_entropy_rule1(max_index, 0, X, Y, rule, rule1)
    entropyY = find_split_entropy_rule1(max_index, 1, X, Y, rule, rule1)
    print("EntropyN: {}".format(entropyN))
    print("EntropyY: {}".format(entropyY))
    instruction = [max_index]
    if entropyN[0] == 0 and entropyY[0] == 0:
        print("finish command")
    elif entropyN[0] == 0:
        print("entropy x is 0")
        # instruction.append(0)
        # instruction.append(2)
        rule2 = [max_index], 1
    elif entropyY[0] == 0:
        print("entropy y is 0")
        # instruction.append
        rule2 = [max_index], 0
    print("Rule2: {}".format(rule1))
    total_entropy, set_length = find_split_entropy_rule1(max_index, 1, X, Y, rule, rule1)
    print(total_entropy)
    print(set_length)

def find_split_entropy_rule1(column, value, X, Y, rule, rule1):
    split_positive = 0
    split_total = 0
    for idx in enumerate(X):
        if idx[1][column] == value and idx[1][rule[0]] == rule[1] and idx[1][rule1[0]] == rule1[1]:
            split_total = split_total + 1
            if Y[idx[0]] == 1:
                split_positive = split_positive + 1
    return calculate_entropy(split_positive, split_total), split_total

def find_split_entropy_rule(column, value, X, Y, rule):
    split_positive = 0
    split_total = 0
    for idx in enumerate(X):
        if idx[1][column] == value and idx[1][rule[0]] == rule[1]:
            split_total = split_total + 1
            if Y[idx[0]] == 1:
                split_positive = split_positive + 1
    return calculate_entropy(split_positive, split_total), split_total


def test_accuracy(max_index, set_length, X, Y):
    accuracy = 0
    for idx in enumerate(X):
        if idx[1][max_index] == 1 and Y[idx[0]] == 1:
            accuracy = accuracy + 1
        elif idx[1][max_index] == 0 and Y[idx[0]] == 0:
            accuracy = accuracy + 1
    return accuracy / set_length


def find_IG(splitL, splitR, total_entropy, length):
    return total_entropy - ((splitL[1] / length) * splitL[0] + (splitR[1] / length) * splitR[0])


def find_split_entropy(column, value, X, Y):
    split_positive = 0
    split_total = 0
    for idx in enumerate(X):
        if idx[1][column] == value:
            split_total = split_total + 1
            if Y[idx[0]] == 1:
                split_positive = split_positive + 1
    return calculate_entropy(split_positive, split_total), split_total


def calculate_entropy(pos, total):
    neg = total - pos
    #print("{} {} {}".format(neg, pos, total))
    if neg == 0:
        return - (pos / total) * math.log2(pos / total)
    elif pos == 0:
        return - (neg / total) * math.log2(neg / total)
    else:
        return -(neg / total) * math.log2(neg / total) - (pos / total) * math.log2(pos / total)
