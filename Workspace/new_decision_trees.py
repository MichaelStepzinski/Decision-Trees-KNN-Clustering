import math
import numpy as np
from scipy import spatial
from random import randint

def DT_train_binary(X, Y, max_depth):
    # step 1 - calculate entropy of the entire set


def calculate_entropy(pos, total):
    #print("{} {} {}".format(neg)
    neg = total - pos
    if neg == 0:
        return - (pos / total) * math.log2(pos / total)
    elif pos == 0:
        return - (neg / total) * math.log2(neg / total)
    else:
        return -(neg / total) * math.log2(neg / total) - (pos / total) * math.log2(pos / total)