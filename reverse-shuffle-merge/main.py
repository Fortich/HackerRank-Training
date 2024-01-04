#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# WAAW S = AW


def reverseShuffleMerge(s):
    s_prime = s[::-1]
    char_count = {}
    for char in s_prime:
        if char_count.get(char) is not None:
            char_count[char] += 1
        else:
            char_count[char] = 1
    string_chars = { 
        char: int(count / 2) for char, count in char_count.items() 
    }
    shuffled_chars = { 
        char: int(count / 2) for char, count in char_count.items() 
    }
    A = []
    for char in s_prime:
        if string_chars[char] > 0:
            reversed_a = A[::-1]
            for a_char in reversed_a:
                if a_char > char and shuffled_chars[a_char] > 0:
                    A.pop()
                    string_chars[a_char] += 1
                    shuffled_chars[a_char] -= 1
                else:
                    break
            A.append(char)
            string_chars[char] -= 1
        else:
            shuffled_chars[char] -= 1
    return "".join(A)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
