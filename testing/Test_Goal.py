#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('../src')

from TreeNode import TreeNode
from Frontier import Frontier
from Problem import Problem
from JsonManager import JsonManager as jManager


def main():
    problem = Problem(jManager.jsonReading("../json/x4cube_solution.json"))
    print("x4cube_solution.json\nisGoal: ", problem.isGoal(problem.initial))

    problem = Problem(jManager.jsonReading("../json/x4cube.json"))
    print("\nx4cube.json\nisGoal: ", problem.isGoal(problem.initial))

if __name__ == '__main__':
    main()
