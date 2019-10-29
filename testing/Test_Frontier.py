#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('../src')

from TreeNode import TreeNode
from Frontier import Frontier
from Problem import Problem
from JsonManager import JsonManager as jManager


def main():
    problem = Problem(jManager.jsonReading("../json/x4cube.json"))
    fringe = Frontier()

    for i in range(10):
        node = TreeNode(problem.initial, 0, 0, 0)
        fringe.insert(node)

    for element in fringe.frontier:
        print(element[0])

    for i in range(10):
        fringe.remove()

    print("isEmpty: ", fringe.isEmpty())
    print("isGoal: ", problem.isGoal(problem.initial))


if __name__ == '__main__':
    main()
