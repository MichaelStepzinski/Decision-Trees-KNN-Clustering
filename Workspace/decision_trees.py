import math
import numpy as np
from scipy import spatial
from random import randint


def DT_train_binary(X, Y, max_depth):
    # step 1 - calculate entropy of the entire set
    branch_entropies = []  # should be renamed to branch information gains
    tree = []
    instruction = []
    solved_features = []
    key_instruction = 0
    stop = False
    num_features = len(X[0])
    set_length = len(Y)
    num_positive = sum(Y)
    total_entropy = calculate_entropy(num_positive, set_length)

    while (max_depth != len(tree) and len(solved_features) < num_features and not stop):
        for x in range(num_features):
            if x not in solved_features:
                no_entropy = find_split_entropy(x, 0, X, Y, tree)
                yes_entropy = find_split_entropy(x, 1, X, Y, tree)
                branch_entropies.append(find_IG(no_entropy, yes_entropy, total_entropy, set_length))
            if x in solved_features:
                branch_entropies.append(0)
        highest_IG = max(branch_entropies)
        max_index = branch_entropies.index(highest_IG)
        instruction.append(max_index)
        branch_entropies.clear()

        entropyN = find_split_entropy(max_index, 0, X, Y, tree)
        entropyY = find_split_entropy(max_index, 1, X, Y, tree)
        if entropyN[0] == 0 and entropyY[0] == 0:
            if entropyN[3] == entropyN[1]:
                instruction.append(0)
            elif entropyN[2] == entropyN[1]:
                instruction.append(1)
            if entropyY[3] == entropyY[1]:
                instruction.append(0)
            # else if split_positive == split_total instruction is 1
            elif entropyY[2] == entropyY[1]:
                instruction.append(1)
            stop = True
        else:
            if entropyN[0] == 0:
                # if split_negative == split_total instruction is 0
                if entropyN[3] == entropyN[1]:
                    instruction.append(0)
                # else if split_positive == split_total instruction is 1
                elif entropyN[2] == entropyN[1]:
                    instruction.append(1)

                # ADD QUALIFIER HERE - IF ENTROPIES OF BOTH SPLITS ARE 0
                instruction.append(2)
                key_instruction = 1

            if entropyY[0] == 0:
                instruction.append(2)
                if entropyY[3] == entropyY[1]:
                    instruction.append(0)
                elif entropyY[2] == entropyY[1]:
                    instruction.append(1)
                key_instruction = 0

        #if(stop):
        #    break
        solved_features.append(max_index)
        tree.append(instruction)
        instruction = []
        if (stop):
            break
        if (len(solved_features) + 1 != num_features):
            total_entropy, set_length, total_positive, total_negative = find_split_entropy(max_index, key_instruction,
                                                                                           X, Y, tree)
            # find instructions for last split
        else:
            # put last remaining index as max index
            for x in range(num_features):
                if x not in solved_features:
                    max_index = x
            instruction.append(max_index)
            entropyN = find_split_entropy(max_index, 0, X, Y, tree)
            entropyY = find_split_entropy(max_index, 1, X, Y, tree)
            if entropyN[3] == entropyN[1]:
                instruction.append(0)
            elif entropyN[2] == entropyN[1]:
                instruction.append(1)
            if entropyY[3] == entropyY[1]:
                instruction.append(0)
            elif entropyY[2] == entropyY[1]:
                instruction.append(1)
            tree.append(instruction)
            solved_features.append(max_index)
    return(tree)


def find_IG(splitL, splitR, total_entropy, length):
    return total_entropy - ((splitL[1] / length) * splitL[0] + (splitR[1] / length) * splitR[0])


def find_split_entropy(column, value, X, Y, rules):
    split_positive = 0
    split_total = 0
    for idx in enumerate(X):
        if idx[1][column] == value and table_checker(idx[1], rules):
            # check for tree in here
            split_total = split_total + 1
            if Y[idx[0]] == 1:
                split_positive = split_positive + 1
    split_negative = split_total - split_positive
    return calculate_entropy(split_positive, split_total), split_total, split_positive, split_negative


def table_checker(line, rules):
    for x in rules:
        for y in range(len(x) - 1):
            if x[y + 1] == 2:
                if y + 1 == 1:
                    # in false instruction column
                    if line[x[0]] == 1:
                        return False
                if y + 1 == 2:
                    # in true instruction column
                    if line[x[0]] == 0:
                        return False
    return True


def calculate_entropy(pos, total):
    neg = total - pos
    if total == 0:
        return 0
    elif neg == 0:
        return - (pos / total) * math.log2(pos / total)
    elif pos == 0:
        return - (neg / total) * math.log2(neg / total)
    else:
        return -(neg / total) * math.log2(neg / total) - (pos / total) * math.log2(pos / total)


def DT_test_binary(X, Y, DT):
    correct = 0
    index = 0
    for line in X:
        if DT_make_prediction(line, DT) == Y[index]:
            correct = correct + 1
        index = index + 1
    return correct/index


def DT_make_prediction(x,DT):
    for instruction in DT:
        index = instruction[0]
        if x[index] == instruction[1]:
            return instruction[1]
        elif x[index] == instruction[2]:
            return instruction[2]