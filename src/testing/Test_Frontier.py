#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('../')

from TreeNode import TreeNode
from Frontier import Frontier
from Problem import Problem
from JsonManager import JsonManager as jManager


def main():
    problem = Problem(jManager.jsonReading("../../json/x4cube.json"))
    fringe = Frontier()

    for i in range(10):
        node = TreeNode(problem.initial, 0, 0, 0)
        fringe.insert(node)

    for element in fringe.frontier:
        print(element[0])

    print(fringe.isEmpty())

    for i in fringe.frontier:
        fringe.remove()

    print(fringe.isEmpty())
    print(problem.isGoal(problem.initial))


if __name__ == '__main__':
    main()
