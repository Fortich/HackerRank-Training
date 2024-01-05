#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(10000)
#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#


def minimumPasses(m, w, p, n):
    current_min = math.inf
    current_steps = 1
    c = 0
    while c < n:
        c += m*w
        steps_if_saving_until_n = current_steps + math.ceil((n-c) / (m*w))
        if steps_if_saving_until_n < current_min:
            current_min = steps_if_saving_until_n
        if c >= p:
            purchases = int(c/p)
            if m == w:
                m = int(purchases/2) + m
                w = int(purchases/2) + (purchases % 2) + w
            else:
                diff = abs(m - w)
                if diff >= purchases:
                    if m > w:
                        w = purchases + w
                        m = m
                    else:
                        m = purchases + m
                        w = w
                else:
                    remind = purchases - diff
                    m = max(m, w)
                    w = m
                    m = int(remind/2) + m
                    w = int(remind/2) + (remind % 2) + w
            c -= purchases*p
            current_steps += 1
        else:
            missing_steps_until_p_or_more = math.ceil((p-c) / (m*w))
            current_steps += missing_steps_until_p_or_more
            c += (missing_steps_until_p_or_more - 1)*m*w
        if current_steps > current_min:
            break
    return min(current_steps, current_min)

class MinSteps:
    def __init__(self):
        self.min_steps = math.inf

def minimumPasses2(m, w, p, n):
    min_steps = MinSteps()
    minimumPassesRecur(m, w, p, n, 0, 1, min_steps)
    return min_steps.min_steps
    
def minimumPassesRecur(m, w, p, n, c, steps, min_steps):
    if steps > min_steps.min_steps:
        return math.inf
    if c >= n:
        return 0
    minimum_passes_without_buying = minimumPassesRecur(m, w, p, n, c + (m * w), steps + 1, min_steps)
    if c >= p:
        purchases = int(c/p)
        
        if m == w:
            new_m = int(purchases/2) + m
            new_w = int(purchases/2) + (purchases % 2) + w
        else:
            diff = abs(m - w)
            if diff >= purchases:
                if m > w:
                    new_w = purchases + w
                    new_m = m
                else:
                    new_m = purchases + m
                    new_w = w
            else:
                remind = purchases - diff
                new_m = max(m, w)
                new_w = new_m
                new_m = int(remind/2) + new_m
                new_w = int(remind/2) + (remind % 2) + new_w
        minimum_passes_with_buying = minimumPassesRecur(new_m, new_w, p, n, c - (p * purchases) + (new_m*new_w), steps + 1, min_steps)
    else:
        minimum_passes_with_buying = math.inf
    
    min_found = steps + min(minimum_passes_with_buying, minimum_passes_without_buying)
    if min_found < min_steps.min_steps:
        min_steps.min_steps = min_found
    return min_found

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
