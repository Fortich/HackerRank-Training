#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort()
    n = len(c)
    sum = 0
    multiplier = 0
    for i in range(n-1, -1, -1):
        if (n-i-1) % k == 0:
            multiplier = multiplier + 1
        sum += multiplier*c[i]
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
