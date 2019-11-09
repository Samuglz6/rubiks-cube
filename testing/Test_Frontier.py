#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('../src')

from TreeNode import TreeNode
from Frontier import Frontier
from Problem import Problem


def main():
    problem = Problem("../json/x4cube.json")
    fringe = Frontier()

    print("Inserting...\n")
    for i in range(10):
        node = TreeNode(problem.initial, 2, None, 1)
        fringe.insert(node)

    print("Elements:")
    for element in fringe.frontier:
        print((element.getF(), element))

    print("\nRemoving...")
    for i in range(10):
        fringe.remove()

    print("\nisEmpty: ", fringe.isEmpty())

if __name__ == '__main__':
    main()
