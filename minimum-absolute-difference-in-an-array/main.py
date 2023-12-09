#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    sorted_arr = sorted(arr)
    min_difference = 1e10
    for i in range(len(sorted_arr)-1):
        current_difference = abs(sorted_arr[i] - sorted_arr[i+1])
        if current_difference < min_difference:
            min_difference = current_difference
    return min_difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

