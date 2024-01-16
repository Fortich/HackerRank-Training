#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    machines_dict = get_machines_dict(machines)
    possible_minimum = 0
    possible_maximum = max(machines) * goal
    while possible_minimum < possible_maximum:
        mid = (possible_maximum + possible_minimum) // 2
        production_in_mid = production_in_day(machines_dict, mid)
        print(possible_minimum, possible_maximum, mid, production_in_mid)
        if production_in_mid < goal:
            possible_minimum = mid + 1
        if production_in_mid >= goal:
            possible_maximum = mid
    return possible_minimum

def get_machines_dict(machines):
    machines_dict = {}
    for machine_produce_days in machines:
        if machines_dict.get(machine_produce_days) is None:
            machines_dict[machine_produce_days] = 1
        else:
            machines_dict[machine_produce_days] += 1
    return machines_dict

def production_in_day(machines_dict, day):
    production = 0
    for machine_produce_days, quantity in machines_dict.items():
        production += (math.floor(day/machine_produce_days) * quantity)
    return production
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
