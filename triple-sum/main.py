#!/bin/python3

import math
import os
import random
import re
import sys

def binary_search(arr, n):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if n < arr[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo



# Complete the triplets function below.
def triplets(a, b, c):
    found_triplets = 0
    for q in b:
        less_than_q_in_a = binary_search(a, q)
        less_than_q_in_c = binary_search(c, q)
        found_triplets += less_than_q_in_a*less_than_q_in_c
    return found_triplets
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = sorted(list(set(map(int, input().rstrip().split()))))

    arrb = sorted(list(set(map(int, input().rstrip().split()))))

    arrc = sorted(list(set(map(int, input().rstrip().split()))))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
