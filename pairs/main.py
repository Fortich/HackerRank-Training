#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    pairs = 0
    number_frequency = {}
    for num in arr:
        if number_frequency.get(num) is None:
            number_frequency[num] = 0
        number_frequency[num] += 1
    for number, frequency in number_frequency.items():
        diff = number - k
        if number_frequency.get(diff) is not None:
            pair_frequency = number_frequency.get(diff)
            pairs += frequency * pair_frequency
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
