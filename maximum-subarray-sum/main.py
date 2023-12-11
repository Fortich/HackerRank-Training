#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#


def maximumSum(a, m):
    partial_sums_tree_root = RBTree()
    current_sum = 0
    max_sum = 0
    for i in a:
        current_sum = (current_sum + i % m) % m
        if current_sum > max_sum:
            max_sum = current_sum
        minimum_greater_than_current_sum = (
            partial_sums_tree_root.search_minimum_greater_than(current_sum)
        )
        if (
            minimum_greater_than_current_sum is not None
            and (current_sum - minimum_greater_than_current_sum + m) % m > max_sum
        ):
            max_sum = (current_sum - minimum_greater_than_current_sum + m) % m
        partial_sums_tree_root.insert(current_sum)
    return max_sum


class RBTree:
    class Node:
        def __init__(self, key):
            self.key = key
            self.is_red = False
            self.parent = None
            self.left = None
            self.right = None

    def __init__(self):
        self.none_node = RBTree.Node(-1)
        self.none_node.is_red = False
        self.none_node.left = None
        self.none_node.right = None
        self.root = self.none_node

    def insert(self, key):
        new_node = RBTree.Node(key)
        new_node.parent = None
        new_node.left = self.none_node
        new_node.right = self.none_node
        new_node.is_red = True

        parent = None
        current = self.root
        while current != self.none_node:
            parent = current
            if new_node.key < current.key:
                current = current.left
            elif new_node.key > current.key:
                current = current.right
            else:
                return

        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self.__balance(new_node)

    def __balance(self, inserted_node):
        current_node = inserted_node
        while current_node != self.root and current_node.parent.is_red:
            if self.__is_right_children(current_node.parent):
                uncle = current_node.parent.parent.left
                if uncle.is_red:
                    uncle.is_red = False
                    current_node.parent.is_red = False
                    current_node.parent.parent.is_red = True
                    current_node = current_node.parent.parent
                else:
                    if current_node == current_node.parent.left:
                        current_node = current_node.parent
                        self.__rotate_right(current_node)
                    current_node.parent.is_red = False
                    current_node.parent.parent.is_red = True
                    self.__rotate_left(current_node.parent.parent)
            else:
                uncle = current_node.parent.parent.right
                if uncle.is_red:
                    uncle.is_red = False
                    current_node.parent.is_red = False
                    current_node.parent.parent.is_red = True
                    current_node = current_node.parent.parent
                else:
                    if current_node == current_node.parent.right:
                        current_node = current_node.parent
                        self.__rotate_left(current_node)
                    current_node.parent.is_red = False
                    current_node.parent.parent.is_red = True
                    self.__rotate_right(current_node.parent.parent)
        self.root.is_red = False

    def __is_right_children(self, node):
        return (
            node is not None and node.parent is not None and node == node.parent.right
        )

    def __rotate_left(self, node):
        temp_node = node.right
        node.right = temp_node.left
        if temp_node.left != self.none_node:
            temp_node.left.parent = node

        temp_node.parent = node.parent
        if node.parent == None:
            self.root = temp_node
        elif node == node.parent.left:
            node.parent.left = temp_node
        else:
            node.parent.right = temp_node
        temp_node.left = node
        node.parent = temp_node

    def __rotate_right(self, node):
        temp_node = node.left
        node.left = temp_node.right
        if temp_node.right != self.none_node:
            temp_node.right.parent = node

        temp_node.parent = node.parent
        if node.parent == None:
            self.root = temp_node
        elif node == node.parent.right:
            node.parent.right = temp_node
        else:
            node.parent.left = temp_node
        temp_node.right = node
        node.parent = temp_node

    def search_minimum_greater_than(self, key):
        return self.__search_minimum_greater_than_in_node(self.root, key)

    def __search_minimum_greater_than_in_node(self, node, key):
        if node is None:
            return None
        if key >= node.key:
            return self.__search_minimum_greater_than_in_node(node.right, key)
        if key < node.key:
            minimum_left = self.__search_minimum_greater_than_in_node(node.left, key)
            if minimum_left is None:
                return node.key
            return minimum_left


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + "\n")

    fptr.close()

