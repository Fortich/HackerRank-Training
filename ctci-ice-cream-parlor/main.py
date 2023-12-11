#!/bin/python3

def whatFlavors(costs, money):
    costs_index_dict = {}
    for i in range(len(costs)):
        cost = costs[i]
        if costs_index_dict.get(cost) is None:
            costs_index_dict[cost] = i
        if costs_index_dict.get(money - cost) is not None and costs_index_dict.get(money - cost) != i:
            print(costs_index_dict.get(money - cost) + 1, i + 1)
            return
        

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        costs = list(map(int, input().rstrip().split()))

        whatFlavors(costs, money)

